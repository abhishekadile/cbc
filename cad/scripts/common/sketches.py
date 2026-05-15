from __future__ import annotations

from .fusion_context import PartModel


def add_centered_plate(model: PartModel, x_mm: float, y_mm: float, z_mm: float, name: str = "main_plate") -> None:
    model.add_feature("extrude_box", name, center=[0, 0, z_mm / 2], size=[x_mm, y_mm, z_mm])


def add_upright(model: PartModel, x_mm: float, y_mm: float, z_mm: float, center_x_mm: float, center_y_mm: float, name: str) -> None:
    model.add_feature("extrude_box", name, center=[center_x_mm, center_y_mm, z_mm / 2], size=[x_mm, y_mm, z_mm])


def add_cylinder(model: PartModel, diameter_mm: float, height_mm: float, center: tuple[float, float, float], name: str) -> None:
    model.add_feature("cylinder", name, center=list(center), diameter_mm=diameter_mm, height_mm=height_mm)


def add_ring(model: PartModel, outer_d_mm: float, inner_d_mm: float, height_mm: float, name: str) -> None:
    model.add_feature("ring", name, center=[0, 0, height_mm / 2], outer_d_mm=outer_d_mm, inner_d_mm=inner_d_mm, height_mm=height_mm)
