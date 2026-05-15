from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Feature:
    kind: str
    name: str
    data: dict[str, Any]


@dataclass
class PartModel:
    name: str
    material_tag: str
    bbox_mm: tuple[float, float, float]
    features: list[Feature] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_feature(self, kind: str, name: str, **data: Any) -> None:
        self.features.append(Feature(kind=kind, name=name, data=data))

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "material_tag": self.material_tag,
            "bbox_mm": list(self.bbox_mm),
            "features": [
                {"kind": f.kind, "name": f.name, "data": f.data} for f in self.features
            ],
            "warnings": self.warnings,
            "metadata": self.metadata,
        }


class FusionDesignContext:
    """Safe wrapper around Fusion when available, with deterministic offline specs."""

    def __init__(self, design_name: str):
        self.design_name = design_name
        self.component_occurrences: dict[str, Any] = {}
        try:
            import adsk.core  # type: ignore
            import adsk.fusion  # type: ignore

            self.adsk_core = adsk.core
            self.adsk_fusion = adsk.fusion
            self.app = adsk.core.Application.get()
            self.design = adsk.fusion.Design.cast(self.app.activeProduct)
            if self.design is None:
                self.app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
                self.design = adsk.fusion.Design.cast(self.app.activeProduct)
        except Exception:
            self.adsk_core = None
            self.adsk_fusion = None
            self.app = None
            self.design = None

    @property
    def is_live_fusion(self) -> bool:
        return self.design is not None


def create_context(design_name: str) -> FusionDesignContext:
    return FusionDesignContext(design_name)


def create_part(name: str, material_tag: str, bbox_mm: tuple[float, float, float]) -> PartModel:
    return PartModel(name=name, material_tag=material_tag, bbox_mm=bbox_mm)


def write_spec(model: PartModel, path: Path) -> None:
    import json

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(model.to_dict(), indent=2), encoding="utf-8")


def mm_to_cm(value_mm: float) -> float:
    return float(value_mm) / 10.0


def value_cm(ctx: FusionDesignContext, value_mm: float):
    return ctx.adsk_core.ValueInput.createByReal(mm_to_cm(value_mm))


def new_component(ctx: FusionDesignContext, name: str):
    if not ctx.is_live_fusion:
        raise RuntimeError("Fusion API is required to create CAD components")
    matrix = ctx.adsk_core.Matrix3D.create()
    try:
        occurrence = ctx.design.rootComponent.occurrences.addNewComponent(matrix)
        component = occurrence.component
        component.name = name
        ctx.component_occurrences[name] = occurrence
    except RuntimeError:
        component = ctx.design.rootComponent
        try:
            component.name = name
        except Exception:
            pass
    return component


def move_component(ctx: FusionDesignContext, name: str, x_mm: float, y_mm: float, z_mm: float = 0.0) -> None:
    occurrence = ctx.component_occurrences.get(name)
    if occurrence is None:
        return
    matrix = ctx.adsk_core.Matrix3D.create()
    matrix.translation = ctx.adsk_core.Vector3D.create(mm_to_cm(x_mm), mm_to_cm(y_mm), mm_to_cm(z_mm))
    occurrence.transform = matrix


def add_user_parameter(ctx: FusionDesignContext, name: str, value_mm: float, comment: str = "") -> None:
    if not ctx.is_live_fusion:
        return
    params = ctx.design.userParameters
    existing = params.itemByName(name)
    if existing:
        existing.expression = f"{value_mm} mm"
        existing.comment = comment
        return
    params.add(name, ctx.adsk_core.ValueInput.createByString(f"{value_mm} mm"), "mm", comment)
