from __future__ import annotations

from cad.scripts.assemblies import cbc_stage1_static_optical_stack
from cad.scripts.common.params import load_all


def build_all_assemblies():
    data = load_all()
    return [cbc_stage1_static_optical_stack.build(data)]


if __name__ == "__main__":
    for model in build_all_assemblies():
        print(model.name)
