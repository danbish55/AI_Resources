# Debug Divi 5 Builder Issue

Use this playbook when the user reports that Divi 5 controls, modules, rendering, saving, migration, templates, interactions, or frontend output are not behaving as expected.

## Table Of Contents

- Triage
- Isolation
- Common Checks
- Evidence

## Triage

Capture:

- Exact symptom and whether it occurs in Visual Builder, WordPress admin, public frontend, or all three.
- Page/template/module affected.
- Recent changes: Divi update, plugin update, migration, import, preset edit, variable edit, cache/minify change, or custom code.
- Browser/device and whether responsive breakpoint matters.
- Whether the site is production, staging, or local.

For production issues, recommend backup/staging before destructive tests.

## Isolation

Work from low-risk checks to more invasive ones:

1. Save, exit, and reload the builder.
2. Test the public frontend after clearing caches/static CSS.
3. Confirm the module still exists in Layers/Wireframe.
4. Check responsive visibility, display conditions, dynamic content source, and Theme Builder assignment.
5. Reproduce on a draft page with a minimal module.
6. Disable cache/minification on staging if CSS/JS output is suspect.
7. Compare with the current Divi 5 changelog/status page for known fixes.
8. Temporarily isolate plugin/child-theme conflicts on staging only.

## Common Checks

- Missing module on mobile: check Visibility, responsive display, layout direction/order, and conditions.
- Setting does not persist: save with the module panel still open; retry one small field; check presets and active responsive/hover state.
- Styling differs frontend/builder: clear cache/static CSS, inspect presets/variables, confirm Theme Builder template context.
- Dynamic content wrong: verify post/product/archive context and Loop Builder query.
- Import issue: check whether presets, images, Lottie JSON, global sections, or library categories came from another site.
- Migration issue: check backward compatibility mode, third-party modules, custom shortcodes, child theme code, and unsupported attributes.

## Evidence

When escalating or documenting:

- Record Divi version and release date if relevant.
- Link the official source or changelog line when a known issue/fix applies.
- Capture affected URL, template assignment, module name, preset names, and exact settings path.
- Describe the smallest reproduction and whether it happens with default modules.
