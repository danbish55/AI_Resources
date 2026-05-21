# Core Divi 5 Workflow

Use this for setup, migration, orientation, and overall build sequence.

## Table Of Contents

- Build Sequence
- Pre-Build Gate
- WordPress And Divi Roles
- Install And Activate Divi 5
- Visual Builder Map
- Getting Started And Migration
- Accuracy Checklist

## Build Sequence

Use this sequence for serious Divi 5 work:

1. Prepare brand, sitemap, copy, media, CTAs, and references.
2. Install WordPress and Divi 5.
3. Learn the interface: Page Bar, Builder Bar, Canvas, Sidebar.
4. Create Design Variables.
5. Create Option Group Presets and Element Presets.
6. Build pages from sections and reusable patterns.
7. Build the global Theme Builder header.
8. Build the global Theme Builder footer.
9. Build remaining Theme Builder templates.
10. Add menus, loops, interactions, canvases, and component patterns where useful.
11. Test responsive behavior, accessibility, performance, and maintainability.

The main principle: build from system to page, not page to system.

## Pre-Build Gate

Before opening the builder for major page work, confirm:

- Brand direction: primary, secondary, accent, neutral colors, heading font, body font.
- Logo: SVG or transparent high-resolution PNG; dark and light variants if possible.
- Images: optimized, enough alternates, relevant to the section purpose.
- Sitemap: start with core pages before adding optional pages.
- Copy: usable drafts for headlines, value props, about text, service/plan descriptions, CTAs, and contact info.
- References: five to ten industry or adjacent sites for structure, navigation, spacing, typography, and color ideas.
- Organization: `/brand`, `/images`, `/content`, `/reference`.

## WordPress And Divi Roles

- WordPress is the CMS for pages, posts, media, settings, and database-backed content.
- Divi is both a WordPress theme and a visual page builder.
- Theme Builder controls global templates such as headers, footers, blog post layouts, archives, 404 pages, product templates, and assigned body templates.

## Install And Activate Divi 5

1. Log in to the Elegant Themes Members Area.
2. Download the Divi 5 zip file.
3. In WordPress, go to `Appearance > Themes > Add New > Upload Theme`.
4. Upload the Divi 5 zip file.
5. Click `Install Now`.
6. Click `Activate`.
7. Follow onboarding to connect the Elegant Themes license for updates.

After activation, use the `Divi` sidebar menu as the command center for Divi features outside the front-end builder.

## Visual Builder Map

Page Bar:

- Top toolbar for page settings, canvas navigation, responsive tools, history, import/export, preview, exit, and save.
- Use Responsive Select for exact widths.
- Use Canvas Grid View for detached canvases.

Builder Bar:

- Left toolbelt for Add Layout, Layers, Inspector, Variable Manager, Preset Manager, Page Manager, Command Center, Wireframe, X-Ray, Builder Settings, Help, and UI mode.
- The Help button opens a Help modal with a Knowledge Base tab that links out to Divi 5 documentation sources (confirmed in Divi 5.4.0 changelog: https://www.elegantthemes.com/api/changelog/divi-5.txt).

Canvas:

- Live workspace for direct editing.
- Right-click for duplicate, move, delete, copy/paste, inspect, add above/inside/below, reset, save to library, and Extend Attributes.
- Use one-click editing, multi-select, Wireframe, and X-Ray as needed.

Sidebar:

- Right contextual settings panel.
- Uses Content, Design, and Advanced tabs.
- Includes breadcrumbs, Element Presets, Responsive State Picker, search/filter, Nested Modules, Loop settings, Flexbox, CSS Grid, semantic elements, custom wrappers, and Interactions.

## Performance Note (Confirmed)

- Divi 5 uses "Speculative Prerendering" to reduce builder navigation load times when entering, exiting, and switching pages in the builder. Official overview: https://help.elegantthemes.com/en/articles/13820117-speculative-prerendering-in-divi-5

## Getting Started And Migration

New sites:

1. Start directly in Divi 5.
2. Create a page and click `Edit With Divi`.
3. Choose blank page, premade layout, Layout Pack, Divi Quick Sites, or Divi AI layout based on need.

Existing Divi 4 sites:

1. Create a staging copy.
2. Run the Divi 5 Migrator compatibility scan.
3. Review the report.
4. Migrate on staging.
5. Test key pages, templates, and third-party extensions.
6. Repeat on live only after staging is clean.

Divi 5 backward compatibility can use Divi 4 framework only where needed, per page or per module.

## Accuracy Checklist

- Prepare content and design direction before major builder work.
- Use Divi 5 for new builds.
- Use staging for migrations.
- Use variables and presets before repeated page styling.
- Use Builder Settings to hide Theme Builder layouts when they distract.
- Use Admin Labels and Layers for complex structures.
- Build global header and global footer before broader template work so every page has consistent brand structure.
