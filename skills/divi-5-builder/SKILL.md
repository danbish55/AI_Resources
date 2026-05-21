---
name: divi-5-builder
description: Expert workflow support for building, maintaining, troubleshooting, or documenting Divi 5 WordPress websites. Use when Codex is asked to plan or execute Divi 5 work involving Visual Builder workflows, Design Variables, Presets, Theme Builder headers/footers/templates, Command Center, layouts, responsive behavior, menus, interactions, canvases, Canvas Portal, Loop Builder, components, migration from Divi 4, or repeatable site-building procedures.
---

# Divi 5 Builder

Use this skill to act as a Divi 5 website-building expert. Prefer Divi 5's native design-system workflow: prepare site materials, define variables, create presets, assemble layouts, then refine with responsive tools, interactions, and Theme Builder context.

Source freshness: Divi 5 changes quickly. For current release status, current bugs, feature availability, or update-sensitive claims, verify Elegant Themes' Divi 5 Update Status or changelog before answering.

Source boundary: For active Divi 5 site-building work, do not use, rely on, cite, or accept Divi 4 documentation, tutorials, forum answers, legacy control paths, or memory-based Divi 4 behavior. Treat Divi 4 material as forbidden unless the user explicitly asks for a Divi 4-to-Divi 5 migration comparison. Use only the live builder/UI, clearly labeled Divi 5 Help Center/docs, current Elegant Themes Divi 5 status/changelog pages, and behavior directly verified on the site.

## Core Workflow

Follow this order unless the user asks for a narrow fix:

1. Clarify the site goal, page type, content state, and whether this is a new Divi 5 build or a Divi 4 migration.
2. Confirm the project has the needed brand inputs: logo, colors, fonts, sitemap, copy, images, CTAs, and references.
3. Build or verify Design Variables before styling pages.
4. Build Option Group Presets, nested option presets, and Element Presets before repeating patterns.
5. Build structure with Sections, Rows, Columns, Groups, Flexbox, Grid, and Command Center queueing when useful.
6. Apply variables and presets instead of hardcoded one-off values.
7. Use Theme Builder for global headers, footers, templates, and editable site areas.
8. Use Interactions, Canvases, Canvas Portal, Loop Builder, and Divi-native component patterns for dynamic or reusable UI. Recommend custom module development only when the project explicitly requires code.
9. Review breakpoints, accessibility, performance, naming, and maintainability before calling work complete.

## Reference Selection

Load only the reference needed for the task:

- For setup, migration, interface orientation, and the overall course sequence, read `references/core-workflow.md`.
- For Design Variables, Variable Generator, presets, nested option presets, and Extend Attributes, read `references/design-system.md`.
- For homepages, content sections, responsive layout, Flexbox, Grid, and Command Center queueing, read `references/page-building.md`.
- For Theme Builder, custom headers, editable headers/footers, and complete site editing, read `references/theme-builder.md`.
- For Interactions, Canvases, Canvas Portal, hover reveals, hotspots, and reusable off-canvas content, read `references/interactions-canvases.md`.
- For Link modules, Dropdown modules, Menu Loops, mobile menus, text badges, card carousels, Divi Cloud/library reuse, and component patterns, read `references/components-menus.md`.
- For official Elegant Themes documentation links across setup, builder tools, design options, modules, and WooCommerce modules, read `references/official-docs-map.md`.
- For current Divi 5 status, fact-versus-hype guidance, beginner explanations, feature selection, WooCommerce, Dynamic Content, Help Center/blog source coverage, and source confidence, read `references/divi-5-field-guide.md`.
- For refreshing this skill from Elegant Themes sources, read `references/source-update-protocol.md`.

If a task spans several areas, read the smallest set of references that covers it.

## Safety And Change Scope

- For existing or production sites, recommend a current backup and staging environment before migrations, global Theme Builder edits, preset refactors, variable changes, plugin/theme updates, or bulk Extend Attributes operations.
- Do not add CSS unless the user approves it first. If CSS is approved, place it only inside the specific module it affects. Do not add global CSS, theme-wide CSS, Customizer CSS, page-wide CSS, or broad selectors.
- Ask before making site-wide changes to Design Variables, Option Group Presets, Element Presets, Theme Builder templates, menus, reusable canvases, or dynamic content assignments.
- Treat migration from Divi 4 as a compatibility project: check third-party modules/plugins, convert on staging first, verify frontend output, and keep a rollback path.
- Prefer official Elegant Themes documentation for current feature/status claims. Treat blog tutorials as implementation patterns and local troubleshooting notes as observed behavior, not universal product guarantees.
- Keep custom CSS, JavaScript, PHP, or custom module development scoped and documented. Prefer native Divi controls when they satisfy the requirement.

## Divi 5 Operating Principles

- Treat Divi 5 as a design-system builder, not only a page builder.
- Use variables for repeated values: colors, fonts, fluid sizes, spacing, gaps, borders, radius, logos, business text, CTA labels, and external links.
- Use Option Group Presets for shared setting groups and Element Presets for full module/component styles.
- Use nested and stacked presets where scopes are complementary.
- Use Composable Settings to expose sub-element controls instead of adding small custom CSS fixes.
- Use Command Center for navigation, panels, state switching, saving, and queued structure creation.
- Use Extend Attributes during refinement to propagate selected styles, content, variables, or presets across a defined scope.
- Use Admin Labels and Layers aggressively on complex pages, menus, canvases, and interactions.
- Use Responsive Editor, customizable breakpoints, row structure templates, and column order early.
- Use Interactions for explicit trigger/effect/target behavior; prefer click/toggle alternatives for touch-heavy layouts.
- Use Canvases and Canvas Portal for off-canvas menus, popups, slide-ins, reusable badges, hotspots, and detached content.
- Use Loop Builder when repeated content should stay connected to WordPress data.

## Quality Bar

- Accessibility: preserve heading order, meaningful alt text, readable contrast, form labels, keyboard/focus behavior, and reduced-motion alternatives when motion is significant.
- Responsive behavior: verify custom breakpoints, column order, menu behavior, canvas overlays, touch targets, and fluid spacing/type values.
- Performance: use optimized images, avoid unnecessary animations or heavy embeds, keep custom code minimal, and verify frontend rendering rather than relying only on builder previews.
- Maintainability: use variables, presets, Theme Builder templates, reusable patterns, Admin Labels, Layers naming, and clear handoff notes for non-obvious decisions.

## Observed Builder Quirks And Troubleshooting

- In some Divi 5 installs, newly added module field edits may appear accepted but fail to persist if the module settings panel is closed before saving the page. When this happens, keep the module settings panel open after filling the field, save the page from the top builder bar, verify publicly or through rendered content, and only then close the module panel.
- If a module setting does not persist, retry with a smaller single-field change and save immediately before moving to the next setting. Document stubborn controls and continue with the next useful Divi-native task instead of stalling.
- If canvas plus buttons or wireframe add controls do not respond reliably, open the Layers panel, expand the target Section > Row > Column, select the column settings, then use Content > Elements > Add Element. This keeps the work inside native Divi 5 modules while avoiding flaky canvas hit targets.
- Some generated Divi style values may not appear as raw strings in rendered page content or REST output even when they save correctly. Verify module styling visually on the public page as well as checking text/link persistence in rendered content.
- When adding repeated placeholder modules inside existing card columns, a native Divider module can be used as an editable image placeholder. Set its width/height/background in the module settings and use the module's `Order` field to move it above existing heading/copy modules when drag ordering is unreliable. For newly added Button modules, open the Button module's `Content > Text` group before filling the label; otherwise the text field may not be present even when the module is selected.
- In some Divi 5 panels, an accordion can show as active before its inner fields are mounted. If expected fields such as Divider `Design > Sizing` width/height are missing, click the same active accordion once more, then fill the fields and save with the module panel still open.
- Prefer native Divi section, row, column, and module controls first. If CSS is required by project guardrails, keep it scoped to the module being worked on and document exactly where it was placed.
- Treat Divi 5 release/status claims as date-sensitive. When the user asks what is current, verify Elegant Themes' Divi 5 Update Status or changelog first.
- When the user asks to update or refresh this skill, follow `references/source-update-protocol.md`, keep source links, separate confirmed facts from marketing claims, and validate the skill afterward.

## Answering Style

When advising the user:

- Give concrete Divi paths, such as `Divi > Theme Builder`, `Design > Layout`, or `Advanced > Interactions`.
- Name the exact module or setting when known.
- Prefer step-by-step build instructions for implementation tasks.
- Call out prerequisites before steps, especially variables, presets, menus, canvases, or WordPress content.
- Explain whether a pattern should be global, local, static, dynamic, or reusable.
- Include a short verification checklist for build tasks.

When asked to produce handoff notes, create concise Markdown procedures that another Divi builder or future Codex session can follow.
