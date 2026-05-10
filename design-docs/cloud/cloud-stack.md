# Cloud Tech Stack

This document defines the backend technologies used for managing the data pipeline off-device.

## Prototype Stack (Getting Started)

During the early prototype phase, "cloud" infrastructure might just run locally on a developer's laptop or a single local server to avoid AWS/GCP costs.
- **Storage**: Local filesystem mapping.
- **Database**: SQLite (easy to manage, single file).
- **API**: FastAPI (Python).
- **Dashboard**: Simple React frontend talking to the FastAPI backend.
- **Path to scaling**: Move images to an S3-compatible local server like MinIO if needed.

## Scaling Stack (Production Deployment)

When deploying multiple devices and training large models, the stack moves to managed services.
- **Object Storage**: AWS S3 or GCP Cloud Storage. Devices use *Signed URLs* to upload images directly to the bucket, bypassing the API server bottleneck.
- **Relational Database**: PostgreSQL (for the Device Registry, User Auth, and Scan Metadata).
- **Experiment Tracking**: MLflow or Weights & Biases (W&B) hosted centrally.
- **Containerization**: Docker for all API and Dashboard services.
- **CI/CD**: GitHub Actions to run tests, build Docker images, and trigger model evaluations.
- **Model Registry**: MLflow Model Registry or HuggingFace Hub (Private) to version control `.onnx` models.
- **Background Workers**: Celery or RabbitMQ/Redis to handle heavy background tasks (like cloud-side image stitching or dataset compilation).
