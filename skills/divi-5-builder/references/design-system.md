# Divi 5 Design System

Use this for variables, Variable Generator, presets, nested presets, Composable Settings, and Extend Attributes.

## Table Of Contents

- Design Variables
- Variable Generator
- Preset Hierarchy
- Option Group Presets
- Element Presets
- Nested And Stacked Presets
- Composable Settings
- Extend Attributes

## Design Variables

Create variables before presets. Divi 5 variable types:

- Colors.
- Fonts.
- Numbers.
- Images.
- Text.
- Links.

Access:

1. Open any page or template in Visual Builder.
2. Click Design Variable icon in Builder Bar.
3. Filter by type.
4. Add variable, name it by role/function, set value, save.

Use role names for broad values: `Primary Color`, `Secondary Color`, `Body Text Color`. Use functional names for jobs: `Border - Fields Dark`, `Background Overlay - Dark`, `Rounded Corners - Buttons`.

Store repeated business text and CTA labels as Text Variables. Store external URLs as Link Variables. Use Image Variables for logo variants.

## Variable Generator

Color generator:

1. Open Variable Manager.
2. Hover over color group.
3. Click `Generate Color Palette Variables`.
4. Use primary color as base.
5. Adjust secondary relationship and shade count.
6. Save generated palette.

Generated colors are global color variables, not a static palette. Divi uses the primary color to generate a relative color system, including light-to-dark shades and transparent colors based on the primary and secondary colors. The generator can also update base colors such as primary, secondary, body text, header text, and link. Because the generated colors are relative, changing the primary color updates the related palette.

Use the color generator when a site needs a coherent palette quickly or when the brand color may change later. Use manual variables when the brand already has a strict, approved palette that should not be mathematically derived.

Sizing generator:

1. Open Variable Manager.
2. Hover over numbers group.
3. Click `Generate Fluid Sizing Variables`.
4. Choose type: Font Size, Spacing, Gap, Radius, Border Width, Clamp, or Size.
5. Choose count and customize if needed.
6. Add variables.

Generated sizing systems can cover text size, spacing, gap, width, border radius, border width, generic clamp variables, and generic size variables. Font Size variables are for responsive headings and body text. Spacing variables are for margin and padding. Gap variables belong in Flexbox horizontal/vertical gap settings. Radius variables can scale corner roundness. Border Width variables can scale border widths.

Generated sizes use `clamp()` by default. The preferred value scales with viewport width while minimum and maximum values prevent it from becoming too small or too large. This can reduce the need for manual responsive editing because the value adapts fluidly across screen sizes.

Advanced controls include scaling function, min/max website width, individual variable values, static non-clamp systems, suffixes, and prefixes. Use these when the generated defaults are close but the site needs a more tailored type scale, spacing ramp, or naming convention.

## Preset Hierarchy

Use this stack:

1. Design Variables: raw values.
2. Option Group Presets: typography, spacing, borders, buttons, backgrounds, fields.
3. Element Presets: complete module/component styles.
4. Pages and Theme Builder templates.

Create Option Group Presets before Element Presets.

## Option Group Presets

Generic workflow:

1. Style one element.
2. Open a setting group such as Title Text, Spacing, Border, Button, or Background.
3. Use the preset icon.
4. Choose `New Preset From Current Styles`.
5. Name clearly and save.
6. Confirm in Preset Manager under Option Groups.

Core examples:

- `Heading 1` through `Heading 6`.
- `Dark Text`, `Light Text`, `Small Text`.
- `Padding - Medium`, `Padding - Large`.
- `Top Border`, `Bottom Border`, `Outlined - Dark`, `Rounded - Regular`.
- `Filled - Primary Color`, `Filled - Black`, `Filled - White`.
- `Text - Primary Color`, `Text - White`.

## Element Presets

Generic workflow:

1. Add or open the module.
2. Apply relevant Option Group Presets.
3. Add element-specific choices.
4. Use module header preset icon.
5. Choose `New Preset From Current Styles`.
6. Name and save.

Useful Element Presets:

- Heading variants.
- Text variants.
- Button variants.
- Rounded Image and Video.
- Icon treatments.
- Blurb variants.
- Group containers such as `Contained - Light` and `Contained - Dark`.
- Accordion, Countdown, Email Opt-In, and card patterns.

## Image Presets, Aspect Ratio, And Framing

Source: https://www.elegantthemes.com/blog/theme-releases/aspect-ration-image-framing-image-presets-for-divi-5
Release-note source: https://www.elegantthemes.com/blog/divi-resources/divi-5-5-release-notes

Divi 5 adds image system controls that belong in the design-system workflow:

- Aspect ratio settings are available for images through sizing controls, so images scale proportionally across screen sizes.
- Image framing controls let a cropped image be repositioned inside a defined aspect ratio or explicit width/height without stretching the image.
- Image option groups now support presets, allowing shared image styles across the many Divi modules that contain image sub-elements.
- Image option groups are harmonized and support Composable Settings, so image sub-elements can expose more of Divi's design options when needed.

Divi 5.5 release notes confirm the image changes as part of the May 12, 2026 update: new aspect-ratio settings were added to the sizing group for all modules, framing settings were added to modules with images, image group presets were implemented, image option groups were harmonized, and image option groups gained Composable Settings support.

Use image presets for repeatable card images, blog loops, product grids, team photos, testimonials, feature thumbnails, and any place where non-technical editors may upload inconsistent image dimensions. Create role-based presets such as `Image - Card 4x3`, `Image - Square Crop`, `Image - Avatar Rounded`, or `Image - Hero Wide` instead of restyling each module manually.

## Nested And Stacked Presets

Nested presets:

- Put Option Group Presets inside Element Presets.
- Put Option Group Presets inside other Option Group Presets when useful.
- Example: CTA preset -> Button preset -> Pill Border preset.

Stacked presets:

- Apply multiple presets to one element when each controls a different concern.
- Good stacks: spacing + border + typography + background.
- Avoid stacking presets that fight for the same property.

Use Preset Preview before saving global changes. Export presets as backup or reuse package.

## Composable Settings

Composable Settings expose additional option groups for module sub-elements.

Confirmed workflow: Composable Settings toggles can be saved into presets so the extra option groups are enabled by default whenever that preset is used. Official tutorial: https://www.elegantthemes.com/blog/divi-resources/how-to-enable-composable-settings-by-default-using-presets-in-divi-5

Workflow:

1. Open module.
2. Go to Design tab.
3. Open sub-element group such as Title Text, Quote Icon, Button, Image, or Body Text.
4. Hover the group heading and click Toggle Options.
5. Enable needed option groups.
6. Configure nested settings.
7. Save to a preset if reusable.

Use for Blurb title spacing, Person image transforms, CTA/Pricing buttons, quote icon styling, and repeated sub-element patterns. Enable only what is needed. Check responsive views early.

## Extend Attributes

Use Extend Attributes during refinement to propagate attributes from one element to matching elements.

Access:

1. Right-click styled element.
2. Choose `Extend Attributes`.
3. Or right-click a specific option group to start focused there.

Controls:

- `Extend From Element`: source.
- `Extend To Location`: parent column, row, section, or entire page.
- `Extend To Element Type`: target element type.
- `Attribute Type To Extend`: styles, content, presets, or combination.
- `Option Group To Extend`: group or all groups.
- `Modified Fields To Extend`: only changed values.

Use for pricing cards, team/person modules, testimonials, imported layout cleanup, and late client changes. Prefer extending variable/preset-linked values. Start with narrow scope.
