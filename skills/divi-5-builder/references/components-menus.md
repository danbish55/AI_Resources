# Divi 5 Components And Menus

Use this for custom navigation, Link/Dropdown modules, Menu Loops, text badges, card carousels, and reusable component patterns.

## Table Of Contents

- Custom Menus
- Menu Loop Architecture
- Desktop/Mobile Menu Workflow
- Text Badges
- Card Carousel

## Custom Menus

Use classic Menu module for simple menus. Use modular menu features when more design/control is needed.

Link module:

- Standalone menu item.
- Supports dynamic content for text and URL.
- Supports icons and hover states.
- Can be styled as text link, button-like link, or special item.

Dropdown module:

- Container revealed by Hover or Click.
- Placement: Above, Below, Left, Right.
- Alignment: Start, Center, End.
- Offset supports Advanced Units.
- Behavior: Floating overlays content; Inline pushes content.
- Can contain Links, Rows, Columns, Images, Buttons, forms, videos, or other modules.

Interactions targeting:

- Parent: containing element of trigger.
- Root Container: top-level component element.
- Child: children inside trigger container.

## Menu Loop Architecture

Use Loop Builder with `Menu` query type when WordPress should remain the menu source but Divi controls visual output.

Workflow:

1. Build one Link module pattern.
2. Enable looping / place it in a loop structure.
3. Query Type: `Menu`.
4. Choose the WordPress menu.
5. Link text: dynamic `Loop Menu Text`.
6. Link URL: dynamic menu URL.
7. Style the one pattern; Divi repeats it for each item.

## Desktop/Mobile Menu Workflow

1. Create Global Header in Theme Builder.
2. Add single-column Flex Row.
3. Column Layout: Row, Space Between, Align Center.
4. Add section padding.
5. Add Image module for logo with responsive width.
6. Add Module Group for desktop links, direction Row.
7. Add Link modules with text and dynamic Page Link URLs.
8. Duplicate Link modules for remaining links.
9. Add Button and hamburger Icon.
10. For dropdowns, add Dropdown module inside Link via Elements > Add Element.
11. Add Link modules inside Dropdown.
12. Style dropdown background, layout, alignment, and offsets.
13. Create Mobile Menu canvas with high z-index.
14. Add close Icon, Link modules, Button, or Menu Loop.
15. Wire interactions:
    - Close icon Click -> Hide Element -> Root Container.
    - Desktop group Breakpoint Enter Tablet -> Hide Element.
    - Desktop group Breakpoint Enter Desktop -> Show Element.
    - Hamburger hidden by default.
    - Hamburger Breakpoint Enter Tablet -> Show Element.
    - Hamburger Click -> Show Element -> mobile menu canvas section.

Best practices:

- Use Admin Labels and Layers.
- Use Responsive Editor early.
- Use variables and presets before deep styling.
- Check accessibility and touch alternatives.

## Text Badges

Badges are short labels such as `New`, `Sale`, `Beta`, or `Popular`.

Workflow:

1. Add Text module for visual labels; Heading only when semantic structure calls for it.
2. Keep text one to three words.
3. Use font and color variables.
4. Add contrasting background.
5. Design > Sizing > Width: `fit-content`.
6. Add padding; horizontal about 1.5x vertical.
7. Add radius: high for pill, low for rectangular badge.
8. Add subtle shadow only when needed.
9. Use Advanced > Position for overlaps.
10. Adjust offsets responsively.

Accessibility:

- Add `aria-label` if the short visible label needs more context.
- Use `aria-hidden="true"` only if decorative and redundant.

Reusable badge options:

- Save as Preset.
- Use Icon List for icon badges.
- Use outline badges with border/no fill.
- Use Module Group row for paired labels.
- Use detached global Canvas plus Canvas Portal for badges reused across templates.

## Card Carousel

Use Group Carousel module for native multi-item carousels.

Core concept:

- Each slide is a Group.
- Groups can contain Image, Heading, Text, Button, Icon, Rating, Price, or dynamic content.
- Design > Groups styles inactive/base cards.
- Design > Active Groups styles focused card.

Workflow:

1. Add single-column Row.
2. Insert Group Carousel.
3. Build first Group carefully as template card.
4. Content > Elements: enable arrows/dots as needed.
5. Content > Carousel Settings: Automatic Rotation, Slides to Show, Slides to Scroll, Transition Speed, Center Mode.
6. Use Variables and Presets inside the first card.
7. Duplicate Group for remaining cards.
8. Replace content.
9. Add Admin Labels.
10. Style Groups and Active Groups at carousel level.
11. Style Arrows and Dots.
12. Use Responsive Editor for Slides to Show, spacing, text, image ratio, and padding.
13. Test swipe and tap targets on a real phone.

Guidance:

- Manual navigation is better for content-heavy cards.
- Automatic rotation should be deliberate.
- Center Mode works when spotlighting one active card.
- Keep card height and copy length consistent.
- Use Loop Builder for posts, products, team members, listings, or custom post types.
