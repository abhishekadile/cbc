from __future__ import annotations

from .fusion_context import PartModel


def add_box_envelope(model: PartModel, name: str, x_mm: float, y_mm: float, z_mm: float, center: tuple[float, float, float], source: str) -> None:
    model.add_feature(
        "bought_part_envelope",
        name,
        shape="box",
        center=list(center),
        size=[x_mm, y_mm, z_mm],
        source=source,
    )


def add_cylinder_envelope(model: PartModel, name: str, diameter_mm: float, length_mm: float, center: tuple[float, float, float], axis: str, source: str) -> None:
    model.add_feature(
        "bought_part_envelope",
        name,
        shape="cylinder",
        center=list(center),
        diameter_mm=diameter_mm,
        length_mm=length_mm,
        axis=axis,
        source=source,
    )
