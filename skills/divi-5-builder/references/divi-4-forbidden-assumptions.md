# Divi 4 Forbidden Assumptions

Use this reference before answering migration, troubleshooting, or UI-control questions where old Divi 4 memory could leak into Divi 5 guidance.

## Table Of Contents

- Forbidden Unless User Asks For Migration Comparison
- Allowed Uses Of Divi 4 Knowledge
- Safer Divi 5 Substitutions

## Forbidden Unless User Asks For Migration Comparison

Do not rely on:

- Divi 4 shortcode structure as the source of truth for Divi 5 module behavior.
- Divi 4 tutorials for current Divi 5 control paths.
- Divi 4 CSS selectors as reliable Divi 5 selectors.
- Divi 4 performance or caching assumptions.
- Divi 4 global module behavior as a substitute for current Divi 5 presets, Theme Builder, or library behavior.
- Divi 4 limitations as evidence that Divi 5 needs custom CSS or code.
- Forum answers or old blog posts that do not explicitly identify Divi 5.

## Allowed Uses Of Divi 4 Knowledge

Use Divi 4 knowledge only to:

- Explain what is changing during migration.
- Interpret a migration compatibility report.
- Identify likely risk areas in old layouts, shortcodes, child theme code, and third-party modules.
- Plan a staged rebuild from legacy patterns into Divi 5-native systems.

Always label this as migration context, not current Divi 5 behavior.

## Safer Divi 5 Substitutions

- Use Design Variables instead of scattered global colors or repeated values.
- Use Option Group Presets and Element Presets instead of copied module styles.
- Use Flexbox/Grid instead of legacy column hacks or broad CSS selectors.
- Use Composable Settings instead of small CSS fixes for sub-element controls.
- Use Loop Builder instead of manually duplicated cards where content is dynamic.
- Use Canvases and Interactions instead of ad hoc popup/off-canvas scripts when native behavior fits.
- Use official Divi 5 Help Center, changelog, current builder behavior, and this skill's references for active work.
