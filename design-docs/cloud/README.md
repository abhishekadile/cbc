# Cloud Architecture

This document describes the cloud infrastructure required to scale data collection, manage a fleet of prototype devices, and orchestrate model training.

*Important Note: This is an engineering prototype system. There are no clinical use claims. The data handled is for research and development purposes only. However, future architectures will need to observe HIPAA guidelines if transitioning to human clinical trials.*

## System Philosophy

- **Local-first system**: The scanner must be capable of completing a scan, running local CV preprocessing, and saving data without an active internet connection. The cloud is an enhancement, not a strict dependency for operation.
- **Optional cloud sync**: When connected to Wi-Fi, the device can background-upload scan sessions to cloud storage.

## Key Components

- **Storage**: Highly scalable object storage for millions of raw TIFF/JPEG images.
- **Dashboard**: A web portal for engineers and researchers to view uploaded scans, verify image quality, and manage devices.
- **Training Data Repository**: A centralized, version-controlled repository where data is formatted for PyTorch/Ultralytics consumption.
- **Experiment Tracking**: A central server logging loss curves, metrics, and configs for every AI training run.
- **Model Registry**: A version-controlled storage bin for compiled AI models (`.pt`, `.onnx`, or `.tflite`).
- **Device Registry**: A database tracking every active scanner in the field, its MAC address, current IP, hardware version, and deployed model version.
- **Access Control**: Role-Based Access Control (RBAC) ensuring only authorized engineers can trigger remote updates or access datasets.
- **Security**: TLS for all API traffic, signed URLs for direct-to-storage image uploads.
