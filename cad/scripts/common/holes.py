from __future__ import annotations

from .fusion_context import PartModel


def add_hole(model: PartModel, x_mm: float, y_mm: float, diameter_mm: float, through: bool = True, name: str = "hole") -> None:
    model.add_feature("hole", name, center=[x_mm, y_mm], diameter_mm=diameter_mm, through=through)


def add_hole_pattern(model: PartModel, span_x_mm: float, span_y_mm: float, diameter_mm: float, name: str) -> None:
    for x in (-span_x_mm / 2, span_x_mm / 2):
        for y in (-span_y_mm / 2, span_y_mm / 2):
            add_hole(model, x, y, diameter_mm, True, f"{name}_{x:g}_{y:g}")


def add_slot(model: PartModel, x_mm: float, y_mm: float, length_mm: float, diameter_mm: float, axis: str, name: str) -> None:
    model.add_feature(
        "slot",
        name,
        center=[x_mm, y_mm],
        length_mm=length_mm,
        diameter_mm=diameter_mm,
        axis=axis,
    )


def add_slot_pattern(model: PartModel, span_x_mm: float, span_y_mm: float, length_mm: float, diameter_mm: float, axis: str, name: str) -> None:
    for x in (-span_x_mm / 2, span_x_mm / 2):
        for y in (-span_y_mm / 2, span_y_mm / 2):
            add_slot(model, x, y, length_mm, diameter_mm, axis, f"{name}_{x:g}_{y:g}")
