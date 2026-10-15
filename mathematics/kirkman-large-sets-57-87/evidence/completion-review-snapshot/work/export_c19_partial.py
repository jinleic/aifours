#!/usr/bin/env python3
"""Expand the frozen17-system auxiliary packing to clearly labelled plain text.
Run: python3 work/export_c19_partial.py
Then: python3 work/check_partial_packing.py evidence/c19-partial17.txt --expected-systems 17
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
packing = json.loads((root/"evidence/c19-17-staged.frozen-packing.json").read_text())
assert len(packing)==17

def shift(block,t):
    return sorted(19*(x//19)+(x%19+t)%19 for x in block)

with (root/"evidence/c19-partial17.txt").open("w") as f:
    f.write("# NOT an LKTS(57): only17 of the55 required constituents.\nPACKING 57 17\n")
    for i,candidate in enumerate(packing):
        f.write(f"\nKTS {i}\n")
        classes = [[shift(b,t) for b in candidate["starter_class"]] for t in range(19)]
        classes += [[shift(b,t) for t in range(19)] for b in candidate["fixed_class_seeds"]]
        assert len(classes)==28
        for j,pc in enumerate(classes):
            f.write(f"CLASS {j}\n")
            for block in pc:
                f.write(" ".join(map(str,block))+"\n")
print("Exported17 resolved systems; this is a partial packing, not an LKTS.")
