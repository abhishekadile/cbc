# Future Hardware Sync

1. Pi sends high-level command (e.g., `START_GRID_SCAN`)
2. Microcontroller moves XY stage to position.
3. Microcontroller selects LED channel.
4. Microcontroller triggers camera.
5. Camera strobe output gates LED driver for perfect exposure.
6. Pi receives frame over CSI.
7. Repeat until grid is complete.
