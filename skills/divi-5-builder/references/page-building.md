# Divi 5 Page Building

Use this for homepage sections, layouts, Flexbox, Grid, Command Center, and responsive assembly.

## Table Of Contents

- Page Build Pattern
- Command Center
- Command Queueing
- Homepage Section Pattern
- Responsive Layout Tools
- Page Quality Checklist

## Page Build Pattern

For each page section:

1. Add Section.
2. Configure Rows and Columns.
3. Add Groups when modules should move/style together.
4. Drop modules into the correct containers.
5. Apply presets.
6. Add content.
7. Refine responsive behavior.

Build structure first, apply the design system second, fill content third.

## Command Center

Open with `CMD+K` on Mac or `CTRL+K` on Windows.

Use for:

- Page navigation.
- Theme Builder and Theme Options navigation.
- Canvas Grid View.
- Breakpoint switching.
- Hover state and default state.
- Opening Layers or Inspector.
- Saving and save variants.
- Editing labeled elements.
- Adding modules and running actions.

High-value commands: `canvas grid`, `hover state`, `default state`, `save`, page names, `Theme Builder`, `Theme Options`, `layers`, `inspector`.

## Command Queueing

Before queueing:

1. Select the insertion point.
2. Confirm presets exist.
3. Confirm preset names are searchable.

Syntax:

- `Shift+Enter`: add to queue.
- `Enter`: execute queue.
- `>`: nest next element.
- `+`: apply preset to previous element.
- Repeated `+`: apply multiple presets.
- `*`: duplicate.

Example:

```text
Section > Row > Column + Spacing Medium + BG Dark + Container Corners > Heading + Text Headings Light > Text + Body Text Light > Button + Off-White
```

Good targets: CTAs, feature rows, card layouts, testimonial strips, icon lists, two-button callouts, team grids. Use queueing when structure is known and presets are mature.

## Homepage Section Pattern

Course homepage sequence:

1. Hero.
2. Features Grid.
3. Split Features.
4. Testimonials.
5. Pricing.
6. Countdown CTA.
7. FAQ.

Hero:

- Three rows: headline/buttons, image, three value statements.
- Use Button Group with Flex Row and `10px` gap.
- Use `Heading 1 Big`, button presets, rounded image, top borders, and dark text.

Features Grid:

- Light gray section.
- Video row plus six-feature grid.
- Desktop 3 columns, tablet 2, mobile 1.
- Use Video Rounded, Icon contained, Heading 5, Dark Text.

Split Features:

- Two-column equal Flex row.
- Left Image, right Groups.
- Use Extend Attributes to copy group layout.
- Buttons often use text-style preset.

Testimonials:

- Heading row plus three card columns.
- Use outlined columns, icon, quote text, Blurb for author, Extend Attributes for repeated styling.

Pricing:

- Three cards, middle emphasized.
- Use Groups for header/content/footer.
- Middle card dark, others light.
- Tablet often becomes one column.

Countdown:

- Contained dark row.
- Heading, Countdown Timer, Button.
- Hide countdown internal heading if redundant.

FAQ:

- Offset columns.
- Left heading/intro; right Accordion.

## Responsive Layout Tools

Use:

- Customizable Responsive Breakpoints.
- Responsive Editor for field values.
- Row Structure Templates for breakpoint-specific row structure.
- Column Order for stacking order.
- Flexbox for one-axis alignment, gaps, wrapping, nav rows, grouped buttons, card internals.
- CSS Grid for two-axis grids, card grids, feature grids, galleries, asymmetry.
- Advanced Units such as `clamp()`, `calc()`, `min()`, and `max()`.
- Aspect ratio settings in module sizing controls when media or repeated card areas must scale proportionally across responsive widths. Divi 5.5 release notes confirm aspect-ratio settings were added to the sizing group for all modules: https://www.elegantthemes.com/blog/divi-resources/divi-5-5-release-notes

Prefer native responsive tools before custom CSS.

## Divi 5.5 Layout And Builder Notes

Official release-note source: https://www.elegantthemes.com/blog/divi-resources/divi-5-5-release-notes

Confirmed facts from the May 12, 2026 Divi 5.5 release notes:

- Visual Builder left-toolbar actions should remain reachable on short desktop viewports.
- Column `Apply Structure Template` now shows Flex structure templates when the column uses Flex layout, instead of only Grid templates.
- Wireframe view fixes improve first-load rendering for nested modules inside global layouts and expanded global layouts.
- Portfolio module grid row classes now match frontend behavior in the Visual Builder, including when the module is the final content module in a column.
- Slider true-parallax transitions were fixed so background images should no longer jump or render inconsistently during slide changes.

Workflow recommendation: after updating to Divi 5.5, re-check layouts that use true-parallax sliders, global layouts in Wireframe view, Flex column structure templates, Portfolio grids, and short-height desktop builder sessions before assuming older workarounds are still needed.

## Page Quality Checklist

- Variables and presets are used instead of one-off values.
- Sections have clear Admin Labels.
- Layers panel is understandable.
- Repeated patterns use presets, Extend Attributes, or components.
- Desktop, tablet, and phone layouts are checked.
- Hover states and touch behavior are checked.
- CTAs have correct text and links.
- Images are optimized and visually relevant.
