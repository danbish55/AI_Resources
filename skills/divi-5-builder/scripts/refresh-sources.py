#!/usr/bin/env python3
"""Fetch Divi 5 source URLs and compare them with the source ledger.

This helper does not rewrite skill references. It produces a compact report so
Codex can decide what changed and patch the smallest relevant files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html.parser
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
import urllib.parse


CHANGELOG_VERSION_RE = re.compile(r"\bversion\s+([0-9]+(?:\.[0-9]+)+)", re.IGNORECASE)
DIVI_VERSION_RE = re.compile(r"\bDivi\s+([0-9]+(?:\.[0-9]+)+)", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)>\]]+")


class TitleParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.parts.append(data)

    @property
    def title(self) -> str:
        return " ".join(" ".join(self.parts).split())


class LinkParser(html.parser.HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.current_href: str | None = None
        self.current_text: list[str] = []
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attrs_dict = dict(attrs)
        href = attrs_dict.get("href")
        if href:
            self.current_href = urllib.parse.urljoin(self.base_url, href)
            self.current_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.current_href:
            text = " ".join(" ".join(self.current_text).split())
            self.links.append({"url": self.current_href, "text": text})
            self.current_href = None
            self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.current_href:
            self.current_text.append(data)


def skill_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def load_protocol_urls(path: pathlib.Path) -> list[str]:
    urls: list[str] = []
    for match in URL_RE.finditer(path.read_text(encoding="utf-8")):
        url = match.group(0).rstrip(".,")
        if url not in urls:
            urls.append(url)
    return urls


def fetch(url: str, timeout: int) -> dict[str, object]:
    req = urllib.request.Request(url, headers={"User-Agent": "Codex Divi 5 skill refresh checker"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            body = response.read()
            content_type = response.headers.get("Content-Type", "")
            text = body.decode("utf-8", errors="replace")
            return {
                "url": url,
                "ok": True,
                "status": getattr(response, "status", None),
                "content_type": content_type,
                "bytes": len(body),
                "sha256": hashlib.sha256(body).hexdigest(),
                "title": extract_title(text, content_type),
                "version": extract_version(url, text),
                "discovered_links": extract_divi_links(url, text, content_type),
                "error": None,
            }
    except (urllib.error.URLError, TimeoutError) as exc:
        return {
            "url": url,
            "ok": False,
            "status": None,
            "content_type": None,
            "bytes": 0,
            "sha256": None,
            "title": None,
            "version": None,
            "discovered_links": [],
            "error": str(exc),
        }


def extract_title(text: str, content_type: str) -> str | None:
    if "html" not in content_type.lower():
        first = next((line.strip() for line in text.splitlines() if line.strip()), "")
        return first[:120] or None
    parser = TitleParser()
    parser.feed(text)
    title = parser.title or None
    if title and len(title) > 180:
        title = title[:177].rstrip() + "..."
    return title


def extract_version(url: str, text: str) -> str | None:
    if url.endswith("/api/changelog/divi-5.txt"):
        match = CHANGELOG_VERSION_RE.search(text)
        return match.group(1) if match else None
    match = DIVI_VERSION_RE.search(text)
    return match.group(1) if match else None


def extract_divi_links(url: str, text: str, content_type: str) -> list[dict[str, str]]:
    if "html" not in content_type.lower():
        return []
    parser = LinkParser(url)
    parser.feed(text)
    discovered: list[dict[str, str]] = []
    seen: set[str] = set()
    for link in parser.links:
        link_url = link["url"].split("#", 1)[0]
        link_text = link["text"]
        parsed = urllib.parse.urlparse(link_url)
        if parsed.netloc not in {"www.elegantthemes.com", "help.elegantthemes.com", "elegantthemes.com"}:
            continue
        if "divi-5" not in link_url.lower() and "divi 5" not in link_text.lower():
            continue
        if link_url in seen:
            continue
        seen.add(link_url)
        discovered.append({"url": link_url, "text": link_text[:160]})
    return discovered


def load_ledger(path: pathlib.Path) -> dict[str, object]:
    if not path.exists():
        return {"schema_version": 1, "sources": []}
    return json.loads(path.read_text(encoding="utf-8"))


def source_map(ledger: dict[str, object]) -> dict[str, dict[str, object]]:
    return {str(item["url"]): item for item in ledger.get("sources", []) if isinstance(item, dict) and "url" in item}


def compare(result: dict[str, object], previous: dict[str, object] | None) -> list[str]:
    changes: list[str] = []
    if not previous:
        changes.append("new-url")
        return changes
    if result["ok"] is False:
        changes.append("fetch-failed")
        return changes
    if previous.get("last_known_version") and result.get("version") and previous.get("last_known_version") != result.get("version"):
        changes.append(f"version {previous.get('last_known_version')} -> {result.get('version')}")
    if previous.get("last_known_title") and result.get("title") and previous.get("last_known_title") != result.get("title"):
        changes.append("title-changed")
    content_type = str(result.get("content_type") or "").lower()
    is_stable_text = "html" not in content_type
    if is_stable_text and previous.get("last_sha256") and result.get("sha256") and previous.get("last_sha256") != result.get("sha256"):
        changes.append("content-hash-changed")
    return changes


def update_ledger(ledger: dict[str, object], results: list[dict[str, object]]) -> dict[str, object]:
    today = dt.date.today().isoformat()
    mapped = source_map(ledger)
    for result in results:
        url = str(result["url"])
        item = mapped.setdefault(url, {"url": url, "category": "discovered", "priority": "review"})
        item["last_checked"] = today
        if result.get("ok"):
            content_type = str(result.get("content_type") or "").lower()
            item["last_status"] = result.get("status")
            if "html" not in content_type:
                item["last_sha256"] = result.get("sha256")
            if result.get("title"):
                item["last_known_title"] = result.get("title")
            if result.get("version"):
                item["last_known_version"] = result.get("version")
            item.pop("last_error", None)
        else:
            item["last_error"] = result.get("error")
    ledger["last_script_refresh"] = today
    ledger["sources"] = sorted(mapped.values(), key=lambda item: (str(item.get("priority", "")), str(item.get("url", ""))))
    return ledger


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    root = skill_root()
    parser = argparse.ArgumentParser(description="Check Divi 5 skill sources for changes.")
    parser.add_argument("--ledger", default=str(root / "references" / "source-ledger.json"))
    parser.add_argument("--protocol", default=str(root / "references" / "source-update-protocol.md"))
    parser.add_argument("--limit", type=int, default=0, help="Only fetch the first N URLs; 0 means all.")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--update-ledger", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON instead of Markdown.")
    args = parser.parse_args()

    ledger_path = pathlib.Path(args.ledger)
    protocol_path = pathlib.Path(args.protocol)
    ledger = load_ledger(ledger_path)
    urls = load_protocol_urls(protocol_path)
    if args.limit > 0:
        urls = urls[: args.limit]
    previous = source_map(ledger)

    results = []
    for url in urls:
        result = fetch(url, args.timeout)
        result["changes"] = compare(result, previous.get(url))
        results.append(result)

    if args.update_ledger:
        ledger = update_ledger(ledger, results)
        ledger_path.write_text(json.dumps(ledger, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps({"count": len(results), "results": results}, indent=2))
        return 0

    failures = [r for r in results if not r["ok"]]
    changed = [r for r in results if r.get("changes")]
    known_urls = set(urls) | set(previous)
    discovered = []
    seen_discovered: set[str] = set()
    for result in results:
        for link in result.get("discovered_links", []):
            link_url = link["url"]
            if link_url in known_urls or link_url in seen_discovered:
                continue
            seen_discovered.add(link_url)
            discovered.append(link)
    print("# Divi 5 Source Refresh Report")
    print()
    print(f"- Checked URLs: {len(results)}")
    print(f"- Changed or new URLs: {len(changed)}")
    print(f"- Newly discovered Divi 5 links: {len(discovered)}")
    print(f"- Failed URLs: {len(failures)}")
    print()
    for result in changed:
        print(f"## {result['url']}")
        print(f"- Status: {result.get('status') or 'failed'}")
        print(f"- Title: {result.get('title') or 'n/a'}")
        print(f"- Version: {result.get('version') or 'n/a'}")
        print(f"- Changes: {', '.join(result.get('changes', []))}")
        if result.get("error"):
            print(f"- Error: {result['error']}")
        print()
    if discovered:
        print("# Newly Discovered Divi 5 Links")
        print()
        for link in discovered[:50]:
            print(f"- {link['text'] or 'Untitled'}: {link['url']}")
        if len(discovered) > 50:
            print(f"- ...and {len(discovered) - 50} more")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
