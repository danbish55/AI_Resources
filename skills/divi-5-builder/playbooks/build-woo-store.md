# Build Divi 5 WooCommerce Store

Use this playbook for Divi 5 work involving WooCommerce products, shop/category pages, product pages, cart, checkout, account pages, notices, or ecommerce conversion flows.

## Table Of Contents

- Store Intake
- Template Strategy
- Checkout Strategy
- Verification

## Store Intake

Confirm:

- Product types: simple, variable, grouped, subscription, booking, digital, or custom.
- Required payment gateways, tax, shipping, coupons, email, inventory, and fulfillment behavior.
- Product taxonomy structure: categories, tags, brands, collections, or custom taxonomies.
- Required legal and trust content: returns, privacy, terms, shipping, accepted payments.
- Whether existing products/orders are live and require staging.

## Template Strategy

Use Theme Builder for global ecommerce structure:

- Shop/category/archive templates for product browsing.
- Single product templates for product detail pages.
- Cart and checkout templates when native Woo modules can replace shortcode-only layouts.
- Search/no-results/404 templates that direct users back to products or support.

Use Loop Builder when product cards need custom layout beyond the standard Woo Products module. Use dynamic content for product title, image, price, rating, sale badges, categories, excerpt, and add-to-cart behavior when available.

## Checkout Strategy

For a branded checkout, create a `WooCommerce Pages > Checkout` Theme Builder template. Prefer dedicated modules:

- Woo Notice near the top, Page Type set to Checkout.
- Woo Checkout Billing.
- Woo Checkout Shipping when shipping is collected.
- Woo Checkout Information for order notes.
- Woo Checkout Details for order summary.
- Woo Checkout Payment for payment methods and Place Order.

Use a two-column desktop layout when appropriate: customer information on the left, order review/payment on the right. Stack cleanly on mobile.

## Verification

Before launch:

- Place a real test order through the full cart, checkout, confirmation, and email path.
- Test guest checkout, logged-in checkout, coupons, taxes, shipping rates, payment gateways, failed payment states, and validation errors.
- Confirm Woo notices are visible and styled consistently.
- Verify fields, labels, radio/checkbox states, focus states, and Place Order button on mobile.
- Confirm product variation selections, stock states, sale states, related products, breadcrumbs, cart totals, and account links.
- Clear cache/static CSS and verify public frontend.
