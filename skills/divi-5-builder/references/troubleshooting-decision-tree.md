# Troubleshooting Decision Tree

Use this reference when a Divi 5 problem needs diagnosis before instructions or changes.

## Table Of Contents

- First Question
- Visual Builder Problems
- Frontend Problems
- Save Or Persistence Problems
- Migration Problems
- WooCommerce Problems
- Escalation Notes

## First Question

Ask where the issue appears:

- Visual Builder only.
- Public frontend only.
- Both builder and frontend.
- WordPress admin or Theme Builder.
- Only one breakpoint, browser, user role, page, template, module, or product.

Then ask what changed most recently.

## Visual Builder Problems

If the builder will not load or controls are missing:

1. Check current Divi 5 status/changelog.
2. Reload builder and browser.
3. Check user role permissions and Builder Settings.
4. Try Wireframe, Layers, or X-Ray to locate hidden modules.
5. Test a minimal draft page with the same module.
6. On staging, isolate cache/minify, plugin, child theme, or browser-extension conflicts.

## Frontend Problems

If frontend output differs from the builder:

1. Clear page/cache/CDN/minify layers and regenerate static CSS when available.
2. Check Theme Builder template assignment.
3. Verify responsive state, hover state, dynamic content source, conditions, and visibility.
4. Check presets and Design Variables for inherited values.
5. Inspect whether custom CSS/JS still targets Divi 5 output correctly.

## Save Or Persistence Problems

If edits disappear:

1. Save with the module settings panel still open.
2. Change one field at a time and save immediately.
3. Confirm the correct responsive/hover/focus/checked state is active.
4. Check whether a preset controls or overrides the field.
5. Test the same field in a fresh module.
6. Record the exact module, setting path, value, and Divi version.

## Migration Problems

If a Divi 4-to-Divi 5 conversion looks wrong:

1. Work only on staging.
2. Check the migrator compatibility report.
3. Identify backward compatibility modules.
4. Check third-party Divi modules, custom shortcodes, child theme code, and global modules.
5. Rebuild high-risk sections using Divi 5 variables, presets, Flexbox/Grid, Loop Builder, and Composable Settings.
6. Verify frontend output after cache refresh.

## WooCommerce Problems

If product/cart/checkout output fails:

1. Confirm WooCommerce and payment/shipping settings outside Divi.
2. Check Theme Builder assignments for product, shop, cart, and checkout pages.
3. Verify Woo module Page Type or product context where applicable.
4. Test guest and logged-in flows.
5. Test a real order on staging or with a safe payment method.
6. Check notices, validation, coupons, taxes, shipping, payment, and confirmation emails.

## Escalation Notes

When reporting or documenting:

- Include the Divi version and exact release date.
- Link official changelog/status sources.
- Include the smallest reproduction.
- Name affected templates, modules, presets, variables, plugins, and custom code locations.
