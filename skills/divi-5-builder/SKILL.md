---
name: divi-5-builder
description: Expert workflow support for building, maintaining, troubleshooting, or documenting Divi 5 WordPress websites. Use when Codex is asked to plan or execute Divi 5 work involving Visual Builder workflows, Design Variables, Presets, Theme Builder headers/footers/templates, Command Center, layouts, responsive behavior, menus, interactions, canvases, Canvas Portal, Loop Builder, components, migration from Divi 4, or repeatable site-building procedures.
---

# Divi 5 Builder

Use this skill to act as a Divi 5 website-building expert. Prefer Divi 5's native design-system workflow: prepare site materials, define variables, create presets, assemble layouts, then refine with responsive tools, interactions, and Theme Builder context.

Source of truth: The canonical Divi 5 skill lives in the GitHub-backed `danbish55/AI_Resources` repository at `skills/divi-5-builder/SKILL.md`. Before starting Divi 5 work, refresh or compare against that GitHub/repo copy when available. Treat `C:\Users\bdanb\.codex\skills\divi-5-builder\SKILL.md` as the installed runtime copy, not the long-term source of truth. When updating this skill, update the GitHub-backed copy, sync the installed runtime copy, and commit/push the repository change.

Source freshness: Divi 5 changes quickly. For current release status, current bugs, feature availability, or update-sensitive claims, verify Elegant Themes' Divi 5 Update Status or changelog before answering.

Source boundary: For active Divi 5 site-building work, do not use, rely on, cite, or accept Divi 4 documentation, tutorials, forum answers, legacy control paths, or memory-based Divi 4 behavior. Treat Divi 4 material as forbidden unless the user explicitly asks for a Divi 4-to-Divi 5 migration comparison. Use only the live builder/UI, clearly labeled Divi 5 Help Center/docs, current Elegant Themes Divi 5 status/changelog pages, and behavior directly verified on the site.

## Core Workflow

Follow this order unless the user asks for a narrow fix:

1. Clarify whether the project is a from-scratch build, a reference-site mimic/replication, or a Divi 4 migration.
2. If the project is a mimic/replication, inventory the reference before building: fonts, logos, images, icons, colors, section patterns, module types, copy, CTAs, menus, forms, animations/interactions, breakpoints, and any third-party services. Use the provided screenshot as the visual target, and use the live reference site when available to inspect exact assets, source paths, responsive behavior, hover states, interactive states, and real typography. Provide the user with a concise list of needed assets and likely sources before editing the target page.
3. Work with the user to get required assets installed or available in the target site before construction. For fonts, identify the exact family/weight/style and whether it is available from an open source, an existing site/theme asset, an Adobe/Typekit or commercial service, or a licensed file the user must provide. The agent has authority to search the internet for missing asset sources, font availability, licensing/source pages, and reasonable substitutes when the exact asset is unavailable. If a font cannot be obtained or installed, notify the user and suggest close alternatives before proceeding.
4. Confirm the project has the needed brand inputs: logo, colors, fonts, sitemap, copy, images, CTAs, and references.
5. Build or verify Design Variables before styling pages.
6. Build Option Group Presets, nested option presets, and Element Presets before repeating patterns.
7. Build structure with Sections, Rows, Columns, Groups, Flexbox, Grid, and Command Center queueing when useful.
8. Apply variables and presets instead of hardcoded one-off values.
9. Use Theme Builder for global headers, footers, templates, and editable site areas.
10. Use Interactions, Canvases, Canvas Portal, Loop Builder, and Divi-native component patterns for dynamic or reusable UI. Recommend custom module development only when the project explicitly requires code.
11. Review breakpoints, accessibility, performance, naming, and maintainability before calling work complete.

## Reference Selection

Load only the reference needed for the task:

- For new multi-page site builds, read `playbooks/build-new-site.md`.
- For Divi 4-to-Divi 5 migrations, read `playbooks/migrate-divi-4-site.md` and `references/divi-4-forbidden-assumptions.md`.
- For WooCommerce store, product, cart, or checkout work, read `playbooks/build-woo-store.md`.
- For builder bugs, rendering problems, saving issues, migration glitches, or frontend mismatches, read `playbooks/debug-builder-issue.md` and, when diagnosis is broad, `references/troubleshooting-decision-tree.md`.
- For design-system setup or cleanup, read `playbooks/create-design-system.md`.
- For handoff notes, maintenance instructions, or client training, read `playbooks/client-handoff.md`.
- For setup, migration, interface orientation, and the overall course sequence, read `references/core-workflow.md`.
- For Design Variables, Variable Generator, presets, nested option presets, and Extend Attributes, read `references/design-system.md`.
- For homepages, content sections, responsive layout, Flexbox, Grid, and Command Center queueing, read `references/page-building.md`.
- For Theme Builder, custom headers, editable headers/footers, and complete site editing, read `references/theme-builder.md`.
- For Interactions, Canvases, Canvas Portal, hover reveals, hotspots, and reusable off-canvas content, read `references/interactions-canvases.md`.
- For Link modules, Dropdown modules, Menu Loops, mobile menus, text badges, card carousels, Divi Cloud/library reuse, and component patterns, read `references/components-menus.md`.
- For choosing a Divi-native module/system before proposing custom code, read `references/module-capability-matrix.md`.
- For official Elegant Themes documentation links across setup, builder tools, design options, modules, and WooCommerce modules, read `references/official-docs-map.md`.
- For current Divi 5 status, fact-versus-hype guidance, beginner explanations, feature selection, WooCommerce, Dynamic Content, Help Center/blog source coverage, and source confidence, read `references/divi-5-field-guide.md`.
- For refreshing this skill from Elegant Themes sources, read `references/source-update-protocol.md`, use `scripts/refresh-sources.py` for a source-change report when useful, and compare against `references/source-ledger.json`.

If a task spans several areas, read the smallest set of references that covers it.

## Safety And Change Scope

- For existing or production sites, recommend a current backup and staging environment before migrations, global Theme Builder edits, preset refactors, variable changes, plugin/theme updates, or bulk Extend Attributes operations.
- When the user explicitly authorizes production Divi page-building work, the agent may upload/install needed WordPress/Divi assets such as fonts, logos, icons, and source images; adjust Divi Design Variables, presets, and reusable styles that support the current page or future related pages; save/publish after each completed section so progress is durable; purge or refresh relevant site cache when saved Divi changes do not appear publicly; and inspect live reference sites or search the web for missing asset/font sources.
- Do not add CSS unless the user approves it first. If CSS is approved, place it only inside the specific module it affects. Do not add global CSS, theme-wide CSS, Customizer CSS, page-wide CSS, or broad selectors.
- If a Divi module's own custom CSS editor or native controls cannot persist the necessary fix, ask before escalating to WordPress `Appearance > Customize > Additional CSS`. Any Additional CSS must be tightly scoped to the specific page/module classes, include responsive guards when appropriate, and be verified on the public page after publishing.
- Ask before making site-wide changes to Design Variables, Option Group Presets, Element Presets, Theme Builder templates, menus, reusable canvases, or dynamic content assignments.
- Treat migration from Divi 4 as a compatibility project: check third-party modules/plugins, convert on staging first, verify frontend output, and keep a rollback path.
- Prefer official Elegant Themes documentation for current feature/status claims. Treat blog tutorials as implementation patterns and local troubleshooting notes as observed behavior, not universal product guarantees.
- Keep custom CSS, JavaScript, PHP, or custom module development scoped and documented. Prefer native Divi controls when they satisfy the requirement.

## Divi 5 Operating Principles

- Treat Divi 5 as a design-system builder, not only a page builder.
- Build pages in Divi's actual hierarchy: Section first, then Row, then Column structure, then Modules. For each page section, decide the required row count, choose the row column layout (including uneven column structures when needed), add only the modules required for that section, and finish the section before moving down the page. For mimic/replication work, compare the completed section against the reference section and verify desktop/tablet/mobile responsiveness before beginning the next section.
- When the user is watching Visual Builder work, make progress feel coherent. Work visibly from top to bottom so the page appears to improve in a human-readable sequence. Avoid jumping between distant sections unless fixing a dependency such as a global font, design variable, header/footer asset, or preset. Explain those dependencies briefly before leaving the current section.
- Use variables for repeated values: colors, fonts, fluid sizes, spacing, gaps, borders, radius, logos, business text, CTA labels, and external links.
- Use Option Group Presets for shared setting groups and Element Presets for full module/component styles.
- Use nested and stacked presets where scopes are complementary.
- Use Composable Settings to expose sub-element controls instead of adding small custom CSS fixes.
- Use Command Center for navigation, panels, state switching, saving, and queued structure creation.
- Use Extend Attributes during refinement to propagate selected styles, content, variables, or presets across a defined scope.
- Use Admin Labels and Layers aggressively on complex pages, menus, canvases, and interactions.
- When working on sliders or repeated child modules, use Layers to distinguish the parent Slider module from individual Slide modules. Parent Slider settings can override every child, while child Slide settings may only affect the selected slide.
- Use Responsive Editor, customizable breakpoints, row structure templates, and column order early.
- Use Interactions for explicit trigger/effect/target behavior; prefer click/toggle alternatives for touch-heavy layouts.
- Use Canvases and Canvas Portal for off-canvas menus, popups, slide-ins, reusable badges, hotspots, and detached content.
- Use Loop Builder when repeated content should stay connected to WordPress data.
- Check `references/module-capability-matrix.md` before recommending custom code for a problem that may have a native Divi module or system.

## Quality Bar

- Accessibility: preserve heading order, meaningful alt text, readable contrast, form labels, keyboard/focus behavior, and reduced-motion alternatives when motion is significant.
- Responsive behavior: verify custom breakpoints, column order, menu behavior, canvas overlays, touch targets, and fluid spacing/type values.
- Performance: use optimized images, avoid unnecessary animations or heavy embeds, keep custom code minimal, and verify frontend rendering rather than relying only on builder previews.
- Maintainability: use variables, presets, Theme Builder templates, reusable patterns, Admin Labels, Layers naming, and clear handoff notes for non-obvious decisions.
- Section completion for top-down mimic builds means: the section's Divi hierarchy is correct; required rows/columns/modules are in place; approved fonts/assets are applied or documented as unavailable; desktop/tablet/mobile states have been checked; the public page has been compared against the reference section; and the section has been saved before moving down.

## Observed Builder Quirks And Troubleshooting

- For reference-site replication, work top down. Finish and verify the header/hero before moving to the next visible section. Before styling a text module, inspect the reference page's rendered/source font stack. If the reference uses custom fonts that are not loaded on the target site, stop the section match and either install the font through Divi/WordPress font controls with permission or tell the user exactly which font files/service are missing. On the Just Cabins to Just Rooms replication, verified reference fonts are `Tablet Gothic Wide` bold for headings, `Avenir` for body copy, and `Tablet Gothic Narrow` bold for navigation/buttons. The reference loads local TTFs from the child theme webfonts stylesheet plus an Adobe Typekit kit; the target page initially loaded Google fonts such as Roboto/Open Sans instead, causing a visible mismatch even when Divi heading weight/color were correct.
- For the current Just Cabins to Just Rooms mimic, the user approved `Libre Franklin` as the Tablet Gothic substitute and `Nunito Sans` as the Avenir substitute. Use Libre Franklin for headings/navigation/buttons and Nunito Sans for body/supporting copy unless the user later provides licensed Tablet Gothic/Avenir files or changes the substitution.
- In Divi 5 Heading module settings, the `Design > Heading Text > Heading Font` dropdown includes a `Custom Fonts` section and an `Upload` option. When a licensed font file is available, use this Divi-native upload path before considering CSS or theme-level font injection.
- In some Divi 5 installs, newly added module field edits may appear accepted but fail to persist if the module settings panel is closed before saving the page. When this happens, keep the module settings panel open after filling the field, save the page from the top builder bar, verify publicly or through rendered content, and only then close the module panel.
- If a module setting does not persist, retry with a smaller single-field change and save immediately before moving to the next setting. Document stubborn controls and continue with the next useful Divi-native task instead of stalling.
- If canvas plus buttons or wireframe add controls do not respond reliably, open the Layers panel, expand the target Section > Row > Column, select the column settings, then use Content > Elements > Add Element. This keeps the work inside native Divi 5 modules while avoiding flaky canvas hit targets.
- Some generated Divi style values may not appear as raw strings in rendered page content or REST output even when they save correctly. Verify module styling visually on the public page as well as checking text/link persistence in rendered content.
- Divi 5's code-editor fields can sometimes show newly typed CSS visually without committing that value into generated frontend styles. After editing a code field, save the page, inspect the generated output or public page, and if the old rule remains, use the field's Reset control before retrying or escalating.
- Stale custom CSS on a parent Slider can silently override child Slide styling. For slider layout problems, inspect and clear parent `Advanced > Custom CSS` fields such as `Slide Description` before changing individual slides. A child slide can look corrected in the panel while the parent slider still emits stronger centering/width rules.
- For hero/slider alignment work, compare against the reference site with actual viewport measurements, not only visual judgment. Measure logo bounds, title/container x positions, text widths, and responsive breakpoints; then verify the published page in a full desktop viewport and mobile/tablet widths.
- If slider text remains centered after alignment settings are changed, check for generated rules on `.et_pb_slide_description` such as `margin: 0 auto`, narrow `max-width`, or `text-align:center`. The effective block position is often controlled by the description container, not the title text itself.
- When Divi's copy/extend style tools are unavailable or unreliable, applying the same reset/fix through the Layers panel one slide at a time is acceptable. Record which parent and child modules were touched and verify all repeated slides after saving.
- Browser previews inside the builder or Customizer can be narrower than the target desktop viewport. If a rule uses a desktop media query such as `@media (min-width: 981px)`, verify in a public full-width browser before deciding the rule failed.
- WordPress or page-cache layers can preserve stale frontend CSS after Divi saves. After visual-builder styling changes, publish/save, purge relevant cache when available, refresh a non-builder public URL with cache-busting if needed, and compare the public output rather than trusting only the builder frame.
- When adding repeated placeholder modules inside existing card columns, a native Divider module can be used as an editable image placeholder. Set its width/height/background in the module settings and use the module's `Order` field to move it above existing heading/copy modules when drag ordering is unreliable. For newly added Button modules, open the Button module's `Content > Text` group before filling the label; otherwise the text field may not be present even when the module is selected.
- In some Divi 5 panels, an accordion can show as active before its inner fields are mounted. If expected fields such as Divider `Design > Sizing` width/height are missing, click the same active accordion once more, then fill the fields and save with the module panel still open.
- Divi numeric fields may append typed digits instead of replacing the current value when browser automation selection does not take. If a field changes from `72` to `730` or similar, clear it with repeated Backspace, type the intended value, press Enter or blur the field, confirm the panel shows the exact value, then save immediately as a single-field or small-field change. Verify on the public page because the builder can show unsaved spacing values that do not persist.
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
