# Documentation Audit

## Previous State
The initial iteration of the `design-docs/` folder established a broad structure but lacked the depth required for a true engineering package. Specifically:
- **Hardware Docs**: Read more like a high-level summary. They lacked specific part recommendations, pricing, 3D printing parameters, and clear risk mitigation strategies.
- **AI Docs**: Were generic and lacked concrete model names, dataset lists, or integration strategies.
- **Embedded & Cloud**: Only contained single `README.md` files with brief bullet points.
- **Missing Elements**: No defined tech stacks, no labeling schemas, no evaluation metrics, and no rigorous image/asset management rules.

## Improvements Made
- **Real Product & Price Research**: Replaced placeholders with real vendor links, estimated costs, and specific part names (e.g., MGN12 rails, TMC2209 drivers, AmScope 40X objectives) via the `sources/product-sources.csv` and detailed BOMs.
- **Engineering Specificity**: Expanded the hardware specs to include tolerances, failure modes, and clear logic for when to use 3D printed vs. metal parts.
- **Comprehensive AI Strategy**: Outlined specific model architectures (YOLO11-seg, U-Net, EfficientNet-B0), identified public datasets (BCCD, PBC, Raabin-WBC), and detailed a concrete active learning workflow.
- **Tech Stacks Defined**: Created `05-ai-tech-stack.md`, `embedded-stack.md`, and `cloud-stack.md` to define Python 3.11+, `uv`, PyTorch, Ultralytics, and FastAPI as the core technologies.
- **Actionable Guides**: Rewrote the 3D printing plan and assembly guides to be step-by-step engineering instructions, including print settings and heat-set insert requirements.
- **Asset Tracking**: Established an image inventory system (`sources/image-sources.csv`) to manage assets without violating copyright, favoring Mermaid diagrams where possible.
