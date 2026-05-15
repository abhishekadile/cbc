import pytest

from cad.scripts.tools.export_stage1 import export_stage1


def test_export_stage1_refuses_placeholder_outputs_outside_fusion():
    with pytest.raises(RuntimeError, match="Real Stage 1 exports require running this script inside Autodesk Fusion"):
        export_stage1()
