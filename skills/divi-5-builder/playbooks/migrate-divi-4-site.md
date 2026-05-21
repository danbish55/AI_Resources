# Migrate Divi 4 Site To Divi 5

Use this playbook when the user asks to convert, migrate, upgrade, or assess an existing Divi 4 site for Divi 5.

## Table Of Contents

- Non-Negotiables
- Inventory
- Migration Path
- Rebuild Opportunities
- Verification

## Non-Negotiables

- Use staging first.
- Take a current file and database backup before conversion.
- Preserve a rollback path.
- Do not rely on Divi 4 tutorials or control paths for Divi 5 behavior.
- Treat third-party Divi modules, child theme code, custom CSS, shortcodes, global modules, and WooCommerce templates as risk areas.

## Inventory

Before converting, identify:

- WordPress, PHP, Divi, WooCommerce, and plugin versions.
- Active child theme and custom PHP/CSS/JS.
- Theme Builder templates, global modules/layouts, Divi Library items, and Divi Cloud usage.
- Third-party Divi modules and marketplace extensions.
- WooCommerce checkout/cart/product templates.
- Forms, opt-ins, integrations, memberships, LMS, booking, multilingual, cache, security, and SEO plugins.
- Pages that drive revenue or traffic.

## Migration Path

1. Update staging to a known-good Divi 4 state.
2. Disable aggressive cache/minification on staging during conversion.
3. Run the Divi 5 Migrator compatibility scan.
4. Read the report before converting.
5. Convert a small representative batch when possible.
6. Keep backward compatibility only where needed while rebuilding risky areas.
7. Rebuild brittle custom CSS as variables, presets, Flexbox, Grid, Composable Settings, or native modules when practical.
8. Re-test after every group of high-value pages/templates.

## Rebuild Opportunities

Prefer native Divi 5 systems when old Divi 4 workarounds are no longer needed:

- Use Design Variables for repeated colors, fonts, spacing, images, business info, and links.
- Use Option Group Presets and Element Presets instead of copied one-off styling.
- Use Flexbox/Grid instead of float/column CSS hacks.
- Use Loop Builder for repeated post/product/resource cards.
- Use Canvases for popups, slide-ins, off-canvas menus, and reusable panels.
- Use Composable Settings for sub-element styling before adding CSS.

## Verification

Test at minimum:

- Homepage, revenue pages, contact forms, checkout/cart/account, blog/archive/search, and all Theme Builder templates.
- Desktop, tablet, and phone.
- Menus, sticky headers, global sections, popups/canvases, interactions, sliders, galleries, forms, opt-ins, dynamic content, and Woo states.
- Frontend output after clearing caches and regenerating static CSS where applicable.
- Third-party module rendering and any shortcodes retained in backward compatibility.

Record remaining backward compatibility modules and rebuild candidates in handoff notes.
