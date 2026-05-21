# Divi 5 Interactions And Canvases

Use this for hover reveals, hotspots, popups, off-canvas content, Canvas Portal, and interaction logic.

## Table Of Contents

- Interaction Model
- Canvases And Canvas Portal
- Hover Reveal Pattern
- Hotspot Pattern
- Touch And Accessibility Notes

## Interaction Model

Every interaction has:

- Trigger: what starts it.
- Effect: what happens.
- Target: which element changes.

Common triggers:

- Page Load.
- Mouse Enter.
- Mouse Exit.
- Click.
- Viewport Enter.
- Viewport Exit.
- Breakpoint Enter.
- Breakpoint Exit.

Common effects:

- Show Element.
- Hide Element.
- Toggle Visibility.
- Add Preset.
- Remove Preset.
- Scroll to element.
- Transform/animate behavior.

Use clear Element Labels before wiring interactions.

## Canvases And Canvas Portal

A Canvas is a detached workspace tied to a page or global site context.

Use canvases for:

- Mobile menus.
- Popups.
- Slide-ins.
- Mega menus.
- Reusable badges.
- Hotspot content.
- Floating cards.
- Detached overlays.

Canvas Portal renders a detached canvas in a chosen place in the main layout or template.

Workflow:

1. Create and name canvas.
2. Build content there.
3. Return to Main Canvas.
4. Add Canvas Portal module.
5. Select canvas.
6. Label portal.
7. Position and wire interactions as needed.

## Hover Reveal Pattern

Example: image hover reveals content and changes title style.

1. Build two-column row.
2. Left: Image module.
3. Right: Group with author/title headings.
4. Add second Group with hidden content: testimonial, text, button.
5. Label hidden Group.
6. Add Page Load -> Hide Element on hidden Group.
7. Create alternate title preset.
8. On Image, add Mouse Enter:
   - Show Element -> hidden Group.
   - Add Preset -> title Heading.
9. On Image, add Mouse Exit:
   - Hide Element -> hidden Group.
   - Remove Preset or restore original title preset.
10. Add short Fade animation to hidden Group.

Check that revealed content does not destabilize layout. On touch devices, consider Click + Toggle Visibility instead.

## Hotspot Pattern

Hotspots combine base image, marker, canvas content, portal, positioning, and interactions.

Workflow:

1. Add Image module.
2. Enable Force Fullwidth for predictable scaling.
3. Add Module Group in same column.
4. Add Icon module inside Group as marker.
5. Style icon with variables; use fluid size if useful.
6. Save marker as Element Preset if reused.
7. Create new canvas for hotspot content.
8. Build compact card: heading, text, button, background, padding, radius, shadow.
9. Return to Main Canvas.
10. Add Canvas Portal inside marker Group.
11. Select hotspot canvas.
12. Label portal.
13. Hide portal by default.
14. Set marker Group to Absolute position.
15. Use offset origin and offsets to place marker.
16. Set z-index above image.
17. Position portal relative to marker.
18. On Icon: Mouse Enter -> Show Element -> portal.
19. Hide behavior:
    - If card has links/buttons, put Mouse Exit -> Hide Element on the Group.
    - If display-only, Mouse Exit can live on Icon.

For touch-heavy layouts, use Click + Toggle Visibility.

To add more hotspots:

1. Duplicate canvas.
2. Rename and change content.
3. Duplicate Module Group.
4. Point portal to new canvas.
5. Reposition.
6. Update interaction targets.

## Touch And Accessibility Notes

- Hover-only patterns need touch alternatives.
- Keep interactive targets large.
- Keep revealed content short.
- Ensure contrast between markers and images.
- Use labels so interactions can be audited later.
- Avoid interactions that trap or hide essential content from keyboard/touch users.
