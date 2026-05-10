# Prototype Image Assets

This document manages the visual assets, diagrams, and CAD renders used in the prototype documentation.

## Image Management Rules

1. **Vendor Images**: It is acceptable to download and commit product images found via web search to ensure the documentation remains complete even if external links die. 
2. **Local Storage**: Always download images and place them in the appropriate `assets/` directory rather than hotlinking them.
3. **Prefer self-created diagrams**: Use Mermaid.js within Markdown for system diagrams, flowcharts, and architecture maps. These render natively on GitHub.
4. **CAD Screenshots**: Screenshots of your own CAD models are encouraged. Use `.png` format.
5. **Image Inventory**: Every image saved in the repository must be tracked in the `design-docs/sources/image-sources.csv` file.

## Image Folder Structure
- `design-docs/assets/images/hardware/prototype/`: Photos of the actual built prototype.
- `design-docs/assets/images/hardware/production/`: Photos or renders of production hardware.
- `design-docs/assets/diagrams/`: Non-Mermaid diagrams (e.g., complex SVG optical ray traces).
- `design-docs/assets/stl-previews/`: Renders or screenshots of individual STL parts.

## File Naming Conventions
- Use lowercase, hyphen-separated names: `assembled-prototype-v1.png`.
- Provide descriptive names, not generic ones like `image1.jpg`.

## Alt Text Conventions
Always include descriptive alt text for accessibility and context if the image fails to load.
*Example:* `![CAD render of the 3D printed optical tower showing the IMX296 camera mount](.../optical-tower.png)`

## Visual Placeholders

If an image is needed but not yet created, use an HTML comment placeholder in the markdown files:

<!-- TODO: Add product image: Raspberry Pi 5 board. Source: [URL] -->
<!-- TODO: Add CAD render: prototype frame v1 -->
<!-- TODO: Add optical path diagram -->

## Adding Vendor Image References
When referencing a specific part in documentation without committing an image, use markdown links to point the reader to the source:
`[View Raspberry Pi 4 on official site](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)`
