# Scan Session Format

All data captured during a single scanning operation must be structured uniformly to allow the AI pipeline and cloud dashboard to parse it without ambiguity.

## Folder Structure

When a scan is initiated, a new directory is created using the current timestamp and a unique ID.

```
data/
  scans/
    YYYY/
      MM/
        DD/
          scan_YYYYMMDD_HHMMSS_ID/
            raw/             # Unprocessed TIFFs or Bayer RAW files directly from sensor
            thumbnails/      # 8-bit JPEGs heavily compressed for quick UI rendering
            stitched/        # The final mosaic image (if computed locally)
            metadata/
              manifest.json  # The single source of truth for this scan
            logs/            # Diagnostic text logs (errors, warnings, timing)
```

## `manifest.json` Schema

The manifest file binds the images to the hardware state at the moment of capture. It must adhere to the following schema:

```json
{
  "scan_id": "scan_20260510_143000_abc123",
  "timestamp": "2026-05-10T14:30:00Z",
  "device_id": "pi4_proto_001",
  "hardware_version": "v1.0-prototype",
  "software_version": "1.2.4",
  "camera": {
    "model": "IMX296",
    "exposure_us": 15000,
    "analog_gain": 2.0
  },
  "optics": {
    "objective": "AmScope_40X_Plan",
    "tube_length_mm": 160
  },
  "images": [
    {
      "filename": "raw/img_001_405nm.tiff",
      "wavelength_nm": 405,
      "tile_index": {"row": 0, "col": 0},
      "stage_position_mm": {"x": 12.5, "y": 8.0, "z": 0.4},
      "focus_score_laplacian": 450.2
    },
    {
      "filename": "raw/img_001_530nm.tiff",
      "wavelength_nm": 530,
      "tile_index": {"row": 0, "col": 0},
      "stage_position_mm": {"x": 12.5, "y": 8.0, "z": 0.4},
      "focus_score_laplacian": 410.8
    }
  ]
}
```
