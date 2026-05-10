# Production Product List

This table outlines the anticipated shift in components from the prototype phase to the production phase.

| Subsystem | Prototype Option | Production Option | Why Upgrade | Supplier Type | Estimated Cost | Risk | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Main Frame** | 3D Printed PETG | Folded Sheet Metal / Machined Al | Rigidity, thermal stability, repeatability | Custom Fabrication | $50 - $150 | Tooling costs | |
| **Enclosure** | Cardboard/None | Injection Molded Plastic or Sheet Metal | Light blocking, dust protection, aesthetics | Custom Fabrication | $30 - $100 | High upfront tooling cost for molding | |
| **Linear Motion (XY)** | 8mm smooth rods or cheap generic MGN12 | High-grade linear guides (e.g., genuine HIWIN/THK) | Precision, reduced backlash, long lifespan | Automation Supplier | $100 - $300 | Sourcing authentic parts, cost | |
| **Actuation (Motors)** | NEMA 17 Open Loop | NEMA 17 Steppers with Encoders (Closed Loop) | Prevent missed steps, guarantee positioning | Automation Supplier | $50 - $120 | Complexity in tuning closed-loop drivers | |
| **Optics Mount** | 3D Printed Plastic | Machined Aluminum Block | Prevent thermal expansion from shifting focus | Custom Fabrication | $30 - $80 | Machining tolerances | |
| **Illumination** | Generic White LED Ring | Custom PCB with specific wavelength LEDs | Consistency across devices, exact spectral control | PCB Manufacturer | $20 - $50 | Sourcing specific narrow-band LEDs | Requires custom driver circuit |
| **Sample Holder** | 3D Printed Slide Clamp | Injection Molded Cartridge Receiver | Needed for known-volume concentration calc | Medical Plastics | $5 - $15 | High tooling cost, fluidic issues | |
| **Compute** | Raspberry Pi 4 | Raspberry Pi Compute Module 4/5 (CM4/CM5) | Allows custom carrier board, smaller footprint | Electronics Distributor| $40 - $70 | Supply chain availability of CM modules | Requires custom carrier PCB |
