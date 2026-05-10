# Cloud Architecture

This document describes the planned cloud architecture for data management, model training, and device fleet management.

*Important Note: This is an engineering prototype system. There are no clinical use claims, and the data handled is for research and development purposes only.*

## Key Components

- **Local-first storage**: The Raspberry Pi acts as the primary data store during acquisition. The system must be fully functional offline.
- **Optional cloud upload**: Devices can be configured to push scan data (raw images, stitched images, metadata) to cloud storage when connected.
- **Scan dashboard**: A web interface to review uploaded scans, examine image quality, and view AI/CV results.
- **Training data storage**: A centralized repository for accumulating the datasets described in the pretraining plan.
- **Experiment tracking**: Logging metrics, hyperparameters, and model checkpoints during AI training.
- **Model registry**: Version-controlled storage for trained AI models. Devices can pull the latest approved models from this registry.
- **Device registry**: Tracking the fleet of active prototype scanners, including hardware versions, calibration status, and software versions.
- **User/project access control**: Managing permissions for researchers and engineers accessing the data and dashboard.
- **Secure data handling**: Ensuring all data is stored securely and access is auditable, even in a non-clinical research context.
