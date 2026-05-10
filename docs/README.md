# CBC Project Documentation Guide

This `docs/` folder organizes the project into four workstreams:

1. **Hardware** - mechanical, optical, motion, cartridge, and production design.
2. **Embedded Software** - Raspberry Pi, camera control, LED control, motion control, and device orchestration.
3. **AI** - model pretraining, dataset organization, computer vision, and final AI/CV pipeline.
4. **Cloud** - storage, APIs, dashboards, training infrastructure, model registry, and future remote device management.

The root `README.md` should remain the quick-start guide for running the current repo. This folder is for deeper engineering plans, design decisions, and implementation roadmaps.

## Folder structure

```text
docs/
  README.md
  hardware/
    README.md
    prototype/
      README.md
      prototype-spec.md
      prototype-product-list.md
    production/
      README.md
      production-spec.md
      production-product-list.md
  embedded-software/
    README.md
  AI/
    README.md
    01-model-strategy.md
    02-pretraining-plan.md
    03-computer-vision-system.md
    04-final-ai-cv-pipeline.md
  cloud/
    README.md
```

## Build order

### Phase 1: Prototype imaging system

Goal: prove that the device can capture clear microscope images, capture a small number of overlapping fields, and stitch 5 to 10 images together.

Primary docs:

- `hardware/prototype/prototype-spec.md`
- `hardware/prototype/prototype-product-list.md`
- `embedded-software/README.md`
- `AI/03-computer-vision-system.md`

### Phase 2: AI dataset and pretraining

Goal: prepare public datasets, normalize labels, train a pretrained image model on blood-cell microscopy data, and fine-tune with images captured from this device.

Primary docs:

- `AI/01-model-strategy.md`
- `AI/02-pretraining-plan.md`

### Phase 3: Hybrid CV plus neural model

Goal: use classical computer vision to generate candidate masks, coordinates, and pseudo-labels, then use reviewed labels to train the neural model.

Primary docs:

- `AI/03-computer-vision-system.md`
- `AI/04-final-ai-cv-pipeline.md`

### Phase 4: Production hardware direction

Goal: evolve from a mostly 3D-printed prototype to a controlled cartridge, more rigid optical path, calibrated motion, and repeatable image acquisition.

Primary docs:

- `hardware/production/production-spec.md`
- `hardware/production/production-product-list.md`

### Phase 5: Cloud and scaling

Goal: support remote data upload, experiment tracking, model registry, training jobs, dashboarding, and future device fleet management.

Primary docs:

- `cloud/README.md`

## Current principle

The first milestone is not clinical CBC accuracy. The first milestone is engineering validation:

- capture clear images,
- capture multiple nearby images,
- stitch fields together,
- segment visible cell-like objects,
- create a repeatable dataset loop,
- compare CV counts, model counts, and reviewed labels.

This project is a research and engineering prototype. It is not for diagnosis, treatment, or clinical decision-making.
