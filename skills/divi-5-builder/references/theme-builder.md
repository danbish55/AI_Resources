# Divi 5 Theme Builder

Use this for headers, footers, global templates, editable areas, and complete site editing.

## Table Of Contents

- Theme Builder Purpose
- Global Header Workflow
- Custom Header Details
- Global Footer Workflow
- Custom Footer Details
- Global Body Templates
- Editable Theme Builder Areas
- Role Editor Safety
- Verification

## Theme Builder Purpose

Theme Builder controls global templates:

- Headers.
- Footers.
- Blog post templates.
- Product templates.
- Archive templates.
- 404 pages.
- Assigned body templates.

Use a Global Header/Footer for simple sites. Create specific templates only when pages, post types, products, or archives need different structure.

## Global Header Workflow

1. Go to `Divi > Theme Builder`.
2. Under `Default Website Template`, click `Add Global Header`.
3. Build/edit in Visual Builder.
4. Use variables and presets from the design system.
5. Save template and Theme Builder changes.

## Custom Header Details

Target header:

- Announcement bar.
- Logo.
- Menu.
- Social links.
- CTA.
- Sticky behavior.
- Responsive show/hide behavior.

Section:

- Use sticky position `Stick to Top`.
- Set high z-index, such as `999`.
- Use controlled top/bottom padding.

Announcement row:

- Full width.
- Primary color background.
- Centered heading/subheading.
- White text.

Navigation row:

- Flex row.
- Align center.
- Wrap on smaller screens.
- Use Site Logo through Image module dynamic content.
- Use Menu module for basic menus; remove built-in logo if separate logo module exists.
- Add Social Media Follow with no-background network items.
- Add CTA Button.

Responsive Interactions:

- Social links: Breakpoint Enter Tablet -> Hide Element; Breakpoint Enter Desktop -> Show Element.
- CTA Button: hide at tablet/below; show at desktop.
- Test wrapping, menu width, sticky behavior, and spacing.

## Global Footer Workflow

Use this for the Divi 5 Mastery Course Part 7 footer pattern or any reusable global footer.

1. Go to `Divi > Theme Builder`.
2. In `Default Website Template`, click `Add Global Footer > Build Global Footer`.
3. Save the template once before building so the global footer assignment is committed.
4. Open the global footer in the Visual Builder.
5. Build structure first, then modules, then presets, then dynamic content.
6. Save the Visual Builder.
7. Return to Theme Builder and click `Save Changes`.
8. Open a front-end page and verify the footer appears globally.

## Custom Footer Details

Course footer target:

- Three styled columns up top.
- Column 1: brand block with light logo and tagline.
- Column 2: address plus social icons.
- Column 3: contact CTA on primary/accent background.
- Row 2: single-line copyright using dynamic current year.

Section setup:

- Content > Background: use `Background - Light Gray` Design Variable or matching background preset.
- Design > Layout: Vertical Gap = `Spacing - Medium`.
- Advanced > HTML: Element Type = `footer` for semantic markup.

Row 1:

- Add `Flex Three Equal Columns`.
- Design > Layout: Layout Wrapping = `Wrap`.
- Horizontal Gap and Vertical Gap = `Spacing - XSmall`.

Modules:

- Column 1: Image module, then Text module.
- Column 2: Heading module, then Social Media Follow module.
- Column 3: Heading module, second Heading module, then Button module.
- Row 2: `Flex Single Column` row with one Text module.

Column styling:

- Apply `Contained - Dark` Element Preset to Row 1 Column 1.
- Column Design > Layout: Justify Content = `Space Between`.
- Use Extend Design Attributes to send the same column settings to other columns in the parent row.
- Override Column 3 background with `Primary Color` Design Variable for the CTA block.

Responsive column classes:

- Desktop: base `Flex Three Equal Columns` handles three-card layout.
- Tablet:
  - Column 1 Sizing > Column Class = `Fullwidth`.
  - Columns 2 and 3 Sizing > Column Class = `Grow To Fill`.
- Phone:
  - Columns 2 and 3 Sizing > Column Class = `Fullwidth`.
- Row wrapping plus these breakpoint-specific classes creates full-width first card on tablet, two-card second row on tablet, and fully stacked cards on phone.

Logo:

- Image Content > Image: bind dynamic content to `Logo Light` Design Variable.
- Alt text: use brand name unless text beside it already announces the brand; if decorative/redundant, leave alt empty.
- Design > Sizing: Max Height = `64px`.

Headings and contact:

- Apply `Heading 5` Element Preset.
- Create/apply a `Light` Heading Element Preset using `White` text.
- Bind Column 2 heading to `Address` Design Variable.
- Bind Column 3 headings to `Phone Number` and `Email` Design Variables.
- Add matching Link URL variables:
  - Phone uses `tel:` URL.
  - Email uses `mailto:` URL.

Social Media Follow:

- Apply `Isolated Icons - Light` Element Preset.
- Add Social Network children for brand platforms.
- Add destination URLs.
- For each Network child, apply `No Background` Element Preset.

Button:

- Apply `Text - White` Element Preset.
- Button text: `Send a message`.
- Link to contact page, `Contact Page URL` Design Variable, or the `mailto:` variable.

Text modules:

- Column 1 tagline: apply `Light Text` Element Preset.
- Example tagline: `Premium workspace for focus and collaboration.`
- Row 2 copyright Text:
  - Stack `Dark Text` first, then `Small Text`.
  - Insert Dynamic Content > `Current Date`.
  - Dynamic Before field: `Copyright © Your Coworking Space `
  - Dynamic After field: `. All Rights Reserved.`
  - Date Format = `Custom`.
  - Custom Date Format = `Y`.
  - Body Text Color = `Text - Dark Transparent`.

Footer verification:

- Tablet: Column 1 full-width; Columns 2 and 3 share the next row.
- Phone: all three cards stack.
- Logo, tagline, address, phone, email, socials, button, and copyright all render correctly.
- Social links, button URL, `tel:` link, and `mailto:` link work.
- Current year updates dynamically.
- Footer appears on front-end pages after Theme Builder save.

## Global Body Templates

Use this for the Divi 5 Mastery Course Part 8 pattern or any site that needs reusable templates for posts, archives, search, author pages, or 404 pages.

Source: https://www.elegantthemes.com/blog/divi-resources/part-8-using-divi-5s-theme-builder-to-create-global-website-templates

Purpose:

- Build one layout and assign it to a class of WordPress content.
- Keep template-driven pages consistent with Design Variables and Presets.
- Use Dynamic Content so the same layout pulls the correct WordPress data for each post, archive, author, search query, or error page.

Recommended templates:

- `All Posts`: single blog post layout.
- `Category Pages`: category archive layout.
- `Author Pages`: author archive layout.
- `Search Results`: search result layout with Search module and results list/loop.
- `404 Page`: helpful not-found page with search, popular links, recent posts, or CTA.

Create a body template:

1. Go to `Divi > Theme Builder`.
2. Click `Add New Template`.
3. Choose `Build New Template`.
4. Select the assignment, such as `All Posts`.
5. Click `Create Template`.
6. Click `Add Custom Body > Build Custom Body`.
7. Build in Visual Builder with variables, presets, and Dynamic Content.
8. Save in Visual Builder, then save Theme Builder changes.

Dynamic Content patterns:

- Post template: Post Title module, Featured Image dynamic image, Post Content module, publish date, author name, author bio, comment count, previous/next navigation, comments, and optional related posts.
- Category template: dynamic archive/category title plus Blog module or Loop Builder filtered to current archive context.
- Author template: author name, author profile picture, author bio, and posts by that author.
- Search template: Search module plus Blog module or Loop Builder showing matching results; configure exclusions when needed.
- 404 template: no post body; include Search module, recent/popular links, helpful copy, and return-home CTA.

All Posts template example:

1. Add Section, apply vertical gap variable.
2. Add Row and Post Title module; disable featured image when using a separate Image module.
3. Apply heading/meta presets and variables to Post Title.
4. Add Image module, bind Image field to Dynamic Content > Featured Image, and apply the appropriate image preset.
5. Add Post Content module and style heading levels/body text with typography variables and presets.
6. Add Pagination module for previous/next navigation.
7. Add Post Author section with author profile picture, author name, author bio, and author posts button via Dynamic Content.
8. Add Related Posts section with Blog module or Loop Builder, limiting post count and disabling pagination if it is a small related-post block.
9. Add Comments module and apply form/title/button/meta presets.
10. Test with real posts, long titles, missing featured images, different authors, comments on/off, and all active responsive breakpoints.

Best practices:

- Name sections, rows, and modules clearly in Layers.
- Use Loop Builder for custom archives when the Blog module is not flexible enough.
- Back up/export templates before major refactors.
- Test templates with real content, not only ideal sample content.
- Use Design Variables and Presets so global design changes propagate predictably.

## Woo Checkout Templates

Source: https://www.elegantthemes.com/blog/divi-resources/how-to-build-custom-woo-checkout-pages-in-divi-5

Use a Theme Builder Checkout template when a WooCommerce store needs a branded checkout page that remains connected to WooCommerce functionality.

Recommended structure:

1. Go to `Divi > Theme Builder`.
2. Click `Add New Template > Build New Template`.
3. Under `WooCommerce Pages`, select `Checkout`, then create the template.
4. Add a custom body and open it in the Visual Builder.
5. Add a dynamic page heading if useful.
6. Place a Woo Notice module near the top and set its Page Type to Checkout.
7. Build the checkout with dedicated Woo Checkout modules:
   - Woo Checkout Billing.
   - Woo Checkout Shipping.
   - Woo Checkout Information.
   - Woo Checkout Details.
   - Woo Checkout Payment.

Layout guidance:

- A two-column layout often works well on desktop: customer fields on the left, order details and payment on the right.
- Use Design Variables and form field presets so checkout fields match the rest of the site.
- Keep the Place Order button visually dominant and avoid styling secondary links, coupon notices, or login prompts so they compete with it.
- On tablet and phone, verify clean stacking, field tap size, labels, payment method readability, notices, coupon spacing, and the Place Order button.

Before launch, place a real test order and verify cart-to-checkout-to-confirmation behavior, coupons, shipping rates, taxes, payment gateways, confirmation emails, and mobile layout.

## Editable Theme Builder Areas

Divi 5 can load assigned header, body template, page context, and footer into one front-end Visual Builder session.

Workflow:

1. Browse to relevant page, archive, product, or template-driven area.
2. Click `Edit With Divi`.
3. Look for green Header/Footer labels.
4. Use Layers to select Header/Footer if crowded.
5. Edit modules directly in context.
6. Save once; updates apply wherever template is assigned.

Benefits:

- Less context switching.
- Better decisions because global areas are seen with page content.
- Copy/paste or drag modules between page, header, and footer.

Limit:

- WordPress menu items remain in WordPress menu settings when a WordPress menu powers the Menu module.

Focus mode:

- Disable `Show Theme Builder Layouts` in Builder Settings when page editing should exclude global areas.

## Role Editor Safety

For client handoff:

1. Go to `Divi > Role Editor`.
2. Restrict Theme Builder, Divi Library, Theme Options, and global modules as needed.
3. Limit module movement/deletion if needed.
4. Disable Design and Advanced tabs for content-only users if appropriate.

## Verification

- Header/footer display on intended pages.
- Sticky header does not cover content unexpectedly.
- Menus work at all breakpoints.
- Global edits save and propagate correctly.
- Client roles cannot alter protected global areas.
