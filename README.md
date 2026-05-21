# AI Resources

Shared AI resources for Codex, ChatGPT, and related workflows.

## Structure

- `skills/` - reusable Codex skills and supporting files.
- `skills/<skill-name>/` - one folder per skill, using a clear lowercase kebab-case name.

## Skills

- `skills/divi-5-builder/` - Divi 5 WordPress site-building workflow support.

## Installing a Skill Locally

Copy the specific skill folder into your local Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\skills\divi-5-builder "$env:USERPROFILE\.codex\skills\divi-5-builder"
```
