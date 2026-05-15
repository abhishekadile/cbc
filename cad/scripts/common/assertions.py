from __future__ import annotations

from .fusion_context import PartModel


def assert_bbox_within(model: PartModel, max_x_mm: float, max_y_mm: float, max_z_mm: float) -> None:
    x_mm, y_mm, z_mm = model.bbox_mm
    if x_mm > max_x_mm or y_mm > max_y_mm or z_mm > max_z_mm:
        raise AssertionError(
            f"{model.name} bbox {model.bbox_mm} exceeds {(max_x_mm, max_y_mm, max_z_mm)}"
        )


def assert_positive_bbox(model: PartModel) -> None:
    if any(value <= 0 for value in model.bbox_mm):
        raise AssertionError(f"{model.name} has non-positive bbox {model.bbox_mm}")


def assert_feature_present(model: PartModel, kind: str) -> None:
    if not any(feature.kind == kind for feature in model.features):
        raise AssertionError(f"{model.name} is missing feature kind {kind}")


def assert_optical_stack(distance_mm: float, target_mm: float = 160.0, tolerance_mm: float = 0.01) -> None:
    if abs(distance_mm - target_mm) > tolerance_mm:
        raise AssertionError(f"Optical stack {distance_mm} mm does not equal {target_mm} mm")
