# Divi 5 Source Update Protocol

Use this when the user asks to refresh, update, re-crawl, or automatically maintain the Divi 5 Builder skill from Elegant Themes and approved third-party Divi 5 sources.

## Important Limitation

A `SKILL.md` file cannot wake itself up, browse websites on a schedule, or rewrite itself without a Codex run. True automatic updating requires a Codex automation or a user-triggered refresh session. This protocol makes the skill updateable; an external automation makes it scheduled.

## Refresh Helper

Use `scripts/refresh-sources.py` to produce a compact change report before patching references. The script fetches URLs listed in this protocol, compares them with `references/source-ledger.json`, detects version/title/content-hash changes when ledger data exists, and reports failed sources.

Examples:

```powershell
python C:\Users\bdanb\.codex\skills\divi-5-builder\scripts\refresh-sources.py
python C:\Users\bdanb\.codex\skills\divi-5-builder\scripts\refresh-sources.py --limit 5
python C:\Users\bdanb\.codex\skills\divi-5-builder\scripts\refresh-sources.py --update-ledger
```

The script does not rewrite Divi reference guidance. Treat it as an evidence-gathering step, then patch the smallest relevant Markdown files manually. Use `--update-ledger` only after reviewing the report and updating reference notes as needed.

## Canonical Sources To Revisit

Current/status sources:

- https://help.elegantthemes.com/en/articles/9973580-divi-5-update-status
- https://www.elegantthemes.com/api/changelog/divi-5.txt
- https://www.elegantthemes.com/blog/

Divi 5 Help Center:

- https://help.elegantthemes.com/en/collections/10650977-divi-5
- https://help.elegantthemes.com/en/collections/16928111-getting-started
- https://help.elegantthemes.com/en/collections/16928144-initial-site-setup-new-sites
- https://help.elegantthemes.com/en/collections/18679262-migrating-from-divi-4-existing-sites
- https://help.elegantthemes.com/en/collections/16928149-divi-5-visual-builder
- https://help.elegantthemes.com/en/collections/16928157-divi-5-visual-builder-basics
- https://help.elegantthemes.com/en/collections/16928174-divi-5-visual-builder-core-concepts
- https://help.elegantthemes.com/en/collections/17812093-divi-5-visual-builder-advanced-concepts
- https://help.elegantthemes.com/en/collections/10650978-divi-5-modules
- https://help.elegantthemes.com/en/collections/14719628-divi-5-woocommerce-modules
- https://help.elegantthemes.com/en/collections/10777927-divi-5-options-groups
- https://help.elegantthemes.com/en/collections/11349519-divi-5-features
- https://help.elegantthemes.com/en/collections/13895918-flexbox-layout-system
- https://help.elegantthemes.com/en/collections/15495410-css-grid-layout-system
- https://help.elegantthemes.com/en/collections/14577685-divi-5-faq-and-troubleshooting
- https://help.elegantthemes.com/en/collections/19029167-email-service-provider-integrations
- https://help.elegantthemes.com/en/collections/19619840-divi-5-cloud

Core blog/tutorial sources:

- https://www.elegantthemes.com/blog/divi-resources/everything-you-need-to-know-about-divi-5s-nested-option-presets
- https://www.elegantthemes.com/blog/divi-resources/5-svg-sections-for-divi-5
- https://www.elegantthemes.com/blog/divi-resources/how-to-build-custom-woo-checkout-pages-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/17-graphs-charts-for-divi-5
- https://www.elegantthemes.com/blog/divi-resources/how-to-build-a-horizontal-blog-loop-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/part-10-mastering-flexbox-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/part-9-building-the-core-inner-pages-of-your-divi-5-website
- https://www.elegantthemes.com/blog/divi-resources/everything-you-need-to-know-about-divi-5s-new-form-field-options
- https://www.elegantthemes.com/blog/divi-resources/divi-5-5-release-notes
- https://www.elegantthemes.com/blog/divi-resources/part-1-what-to-prepare-before-building-your-divi-5-website
- https://www.elegantthemes.com/blog/divi-resources/part-2-exploring-every-aspect-of-the-divi-5-interface
- https://www.elegantthemes.com/blog/divi-resources/part-3-creating-a-divi-5-global-design-system-with-design-variables
- https://www.elegantthemes.com/blog/divi-resources/part-4-mastering-divi-5-presets-for-faster-more-consistent-web-design
- https://www.elegantthemes.com/blog/divi-resources/part-5-building-a-divi-5-homepage-from-scratch
- https://www.elegantthemes.com/blog/divi-resources/part-6-building-a-custom-header-and-navigation-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/part-7-building-a-custom-footer-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/part-8-using-divi-5s-theme-builder-to-create-global-website-templates
- https://www.elegantthemes.com/blog/divi-resources/how-to-get-started-with-divi-5
- https://www.elegantthemes.com/blog/divi-resources/how-the-command-center-changes-the-divi-5-workflow
- https://www.elegantthemes.com/blog/divi-resources/queueing-commands-in-divi-5-to-build-entire-layouts
- https://www.elegantthemes.com/blog/divi-resources/everything-you-need-to-know-about-composable-settings-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/how-extend-attributes-helps-you-design-faster-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/divi-5-commands-every-power-user-should-know
- https://www.elegantthemes.com/blog/divi-resources/everything-you-need-to-know-about-divi-5s-new-menu-features
- https://www.elegantthemes.com/blog/divi-resources/building-an-image-hover-reveal-effect-using-divi-5s-interactions
- https://www.elegantthemes.com/blog/divi-resources/how-to-add-hotspots-to-images-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/editing-headers-and-footers-faster-with-divi-5-editable-areas
- https://www.elegantthemes.com/blog/divi-resources/how-to-create-a-card-carousel-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/how-to-enable-composable-settings-by-default-using-presets-in-divi-5
- https://www.elegantthemes.com/blog/divi-resources/divi-design-youtube-channels-you-should-follow

Core release/feature sources:

- https://help.elegantthemes.com/en/articles/15162149-the-timeline-module-in-divi-5
- https://www.elegantthemes.com/blog/theme-releases/variable-generator
- https://www.elegantthemes.com/blog/theme-releases/complete-site-editing
- https://www.elegantthemes.com/blog/theme-releases/nested-option-presets
- https://www.elegantthemes.com/blog/theme-releases/composable-settings
- https://www.elegantthemes.com/blog/theme-releases/design-variables
- https://www.elegantthemes.com/blog/theme-releases/preset-based-design
- https://www.elegantthemes.com/blog/theme-releases/preset-manager
- https://www.elegantthemes.com/blog/theme-releases/extend-attributes
- https://www.elegantthemes.com/blog/theme-releases/command-center
- https://www.elegantthemes.com/blog/theme-releases/flexbox
- https://www.elegantthemes.com/blog/theme-releases/css-grid
- https://www.elegantthemes.com/blog/theme-releases/interactions
- https://www.elegantthemes.com/blog/theme-releases/divi-canvases
- https://www.elegantthemes.com/blog/theme-releases/loop-builder
- https://www.elegantthemes.com/blog/theme-releases/new-menu-modules-menu-looping-and-interactions
- https://www.elegantthemes.com/blog/theme-releases/semantic-elements
- https://www.elegantthemes.com/blog/theme-releases/divi-ai-for-divi-5
- https://www.elegantthemes.com/blog/theme-releases/aspect-ration-image-framing-image-presets-for-divi-5

Approved third-party Divi 5 sources:

- https://diviengine.com/divi-5/

Use third-party sources as supporting intelligence, not as canonical truth about Divi itself. They are useful for plugin compatibility, real-world workflows, tutorials, examples, and ecosystem signals. When a third-party claim conflicts with Elegant Themes, prefer Elegant Themes unless the topic is specifically the third-party vendor's own plugin status.

## Refresh Workflow

1. Fetch the current/status sources first.
2. Record the newest Divi 5 version, release date, and top-level feature/fix changes.
3. Crawl the Help Center hub and its Divi 5 collections for new article links.
4. Crawl the Elegant Themes blog home, Divi Resources category, and Theme Releases category for new Divi 5 posts.
5. Crawl approved third-party Divi 5 sources for ecosystem updates, plugin compatibility notes, tutorials, and practical examples.
6. Compare discovered URLs against `references/source-ledger.json` and the existing reference files.
7. Summarize only new or changed knowledge. Do not duplicate existing notes unless the old note needs correction.
8. Classify each update as `confirmed fact`, `third-party ecosystem note`, `workflow recommendation`, `tutorial pattern`, `marketing claim`, or `needs verification`.
9. Patch the smallest relevant reference file:
   - `core-workflow.md` for setup, migration, interface, and general workflow.
   - `design-system.md` for variables, presets, generated palettes/sizes, relative colors, advanced units, Extend Attributes, and style inspection.
   - `page-building.md` for layout, responsive design, Flexbox, Grid, Command Center queueing, Page Manager, and content creation.
   - `theme-builder.md` for headers, footers, templates, editable areas, dynamic content, archives, and search.
   - `interactions-canvases.md` for Interactions, Canvases, Canvas Portal, hover/reveal, hotspots, popups, and off-canvas content.
   - `components-menus.md` for menu modules, Link/Dropdown modules, semantic navigation, carousels, badges, and component patterns.
   - `divi-5-field-guide.md` for broad feature maps, current status, source coverage, and beginner coaching.
   - `official-docs-map.md` for general official documentation links.
10. Update `references/source-ledger.json` after reviewed source changes are reflected in the reference notes.
11. Update this file if new canonical or approved third-party sources should be watched in future runs.
12. Validate the skill with `python C:\Users\bdanb\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\bdanb\.codex\skills\divi-5-builder`.

## Update Quality Rules

- Prefer official Elegant Themes Help Center, changelog, documentation, and blog sources over third-party summaries for Divi core facts.
- Use third-party sites for ecosystem/plugin status and practical implementation ideas, and label them clearly.
- For version-sensitive claims, include exact release dates when available.
- Preserve source URLs beside important claims.
- Do not paste long source text. Summarize in original wording.
- Separate stable workflow guidance from current release status.
- When a blog post is mostly promotional, extract the concrete capability or workflow and label the promotional claim as marketing.
- If a source conflicts with older skill notes, prefer the newer official source and mark the older claim as superseded.

## Suggested Automation Prompt

Use this prompt for a scheduled Codex automation:

```text
Refresh the local Divi 5 Builder skill at C:\Users\bdanb\.codex\skills\divi-5-builder. Follow references/source-update-protocol.md. Revisit the canonical Elegant Themes Help Center, changelog, documentation, and blog sources plus approved third-party Divi 5 sources; discover new Divi 5 articles and ecosystem updates; summarize only new or changed knowledge; patch the smallest relevant reference files; keep source URLs; separate confirmed facts, third-party ecosystem notes, workflow recommendations, and marketing claims; validate the skill with the skill-creator quick validator; report what changed and any sources that failed to load.
```

Preferred automation prompt after this upgrade:

```text
Refresh the local Divi 5 Builder skill at C:\Users\bdanb\.codex\skills\divi-5-builder. Follow references/source-update-protocol.md. Run scripts/refresh-sources.py to compare current Elegant Themes and approved third-party sources against references/source-ledger.json; then browse or fetch changed/new sources as needed, summarize only new or changed knowledge, patch the smallest relevant reference/playbook files, preserve source URLs, separate confirmed facts, third-party ecosystem notes, workflow recommendations, tutorial patterns, marketing claims, and needs-verification items, update references/source-ledger.json after reviewed source changes are reflected, validate the skill with the skill-creator quick validator, and report what changed plus any sources that failed to load.
```
