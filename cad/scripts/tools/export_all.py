from __future__ import annotations

from cad.scripts.tools.export_stage1 import export_stage1


def export_all():
    """Export the currently implemented Stage 1 manufacturing files.

    This intentionally delegates to the Fusion-only Stage 1 exporter so the
    legacy all-parts command cannot create offline placeholder STL/STEP files.
    """
    return export_stage1()


if __name__ == "__main__":
    for path in export_all():
        print(path)
