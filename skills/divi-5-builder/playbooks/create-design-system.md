# Create Divi 5 Design System

Use this playbook when the user asks to create, clean up, standardize, or document a Divi 5 design system with variables, presets, typography, color, spacing, forms, cards, or reusable components.

## Table Of Contents

- Inputs
- Variable Layer
- Preset Layer
- Component Layer
- Governance

## Inputs

Gather:

- Logo variants and usage needs.
- Color palette or primary/secondary color direction.
- Heading and body fonts.
- Spacing/rhythm preference.
- Button, card, form, image, menu, and section examples.
- Accessibility requirements and brand constraints.

## Variable Layer

Create role-based variables before styling modules:

- Colors: primary, secondary, accent, body text, heading text, link, background, border, status colors.
- Fonts: heading and body families.
- Numbers: type scale, spacing scale, gaps, radius, border width, max widths.
- Images: logo variants, default placeholders, recurring brand images.
- Text: business name, phone, email, address, CTA labels.
- Links: contact page, phone `tel:`, email `mailto:`, socials, booking, privacy.

Use generators when the brand allows mathematically related colors or fluid sizing. Use manual variables when the brand guide is strict.

## Preset Layer

Build small presets first:

- Typography presets for headings, body, eyebrow, caption, meta, and links.
- Button presets for primary, secondary, text, outline, danger, and disabled/quiet actions.
- Spacing presets for sections, rows, cards, and content groups.
- Border/radius/shadow presets for cards, images, forms, badges, and buttons.
- Image presets for aspect ratio, framing, avatars, product images, and blog cards.
- Form field presets for Input, Checkbox, and Radio groups.

Then build Element Presets for modules/components that combine the smaller presets.

## Component Layer

Create reusable patterns after the base system is stable:

- Header and footer patterns.
- CTA bands, feature cards, testimonial cards, pricing cards, process/timeline sections.
- Blog/product/resource loops.
- Forms, notices, badges, and reusable canvases.
- WooCommerce product, cart, and checkout patterns if ecommerce is in scope.

Use Admin Labels and Layers names that explain role, not just appearance.

## Governance

- Name variables and presets by role: `Button - Primary`, `Border - Soft Card`, `Image - Card 4x3`.
- Avoid vague names such as `Blue`, `Style 1`, or `New Preset`.
- Use local overrides only when a one-off change should not propagate.
- Back up/export presets before large refactors.
- Document which presets are safe for clients to edit and which are structural.
