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

## Flexbox Course Notes

Source: https://www.elegantthemes.com/blog/divi-resources/part-10-mastering-flexbox-in-divi-5

Part 10 of the Divi 5 Mastery Course centers the native Flexbox controls in the Visual Builder:

- `Layout Style` chooses Flexbox versus other layout modes.
- Horizontal and vertical gaps handle spacing between child elements without margins.
- `Layout Direction` sets the main axis: Row, Row Reverse, Column, or Column Reverse.
- `Justify Content` distributes items along the main axis; `Align Items` handles the cross axis.
- Layout wrapping and `Align Content` are useful when child elements can flow onto multiple lines.

Workflow recommendation: use Flexbox for headers, nav rows, grouped buttons, card internals, icon/text rows, and responsive one-dimensional stacks. Adjust layout direction at responsive breakpoints instead of rebuilding the structure when desktop side-by-side content should stack on smaller screens.

## Timeline Module

Source: https://help.elegantthemes.com/en/articles/15162149-the-timeline-module-in-divi-5
Changelog source: https://www.elegantthemes.com/api/changelog/divi-5.txt

Divi 5.5.2 added the Timeline parent module and Timeline Item child modules. Use it for company histories, product roadmaps, resumes/CVs, case studies, process pages, onboarding flows, and other dated or sequenced content.

Key behavior:

- Each event is a Timeline Item child module that can be added, edited, duplicated, deleted, and reordered independently.
- Parent Timeline content settings include item management, link, background, Loop, order, and meta options.
- Parent design settings include Timeline, Track, Item, Spacer, Connector, Marker, Card, Date Text, Title Text, Body Text, Sizing, Spacing, Border, Box Shadow, Filters, Transform, and Animation.
- The parent module can enable Loop Builder when timeline events should come from a dynamic source.
- Several option groups include Even sub-options so every second item can be styled differently, supporting alternating timeline layouts without custom CSS.

Workflow recommendation: use the parent module for shared structure, track, marker, card, and typography styles; use child item settings only for per-event content or intentional overrides. Verify exact alternating-side labels in the live builder before giving precise click paths because the Help Center article flags one card-side label for verification.

## Horizontal Blog Loop

Source: https://www.elegantthemes.com/blog/divi-resources/how-to-build-a-horizontal-blog-loop-in-divi-5

Use Loop Builder instead of the Blog module when the design needs a fully custom repeated post card. The horizontal blog loop pattern designs one post card with ordinary Divi elements, connects image/title/date/excerpt/link elements to dynamic post data, and lets Divi repeat the card for the query.

Recommended uses: editorial blog indexes, resources, projects, products, events, team members, and other repeated content where the card layout should not follow the fixed Blog module structure. Add pagination when the query can return more items than the page should show at once.

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
