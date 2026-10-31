#!/usr/bin/env python3
"""Calibration controls for the wedge-2 modular flattening implementation."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("implementation", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("koszul", args.implementation)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    controls = []
    single = {(0, 0, 0, 0): (1, 0)}
    separated = {(0, 0, 0, 0): (1, 0), (0, 1, 1, 1): (1, 0)}
    for wedge in (1, 2, 3):
        zero_rank = mod.rank_mod(mod.flatten({}, 0, 0, wedge))
        one_rank = mod.rank_mod(mod.flatten(single, 0, 0, wedge))
        two_rank = mod.rank_mod(mod.flatten(separated, 0, 0, wedge))
        if (zero_rank, one_rank, two_rank) != (0, 10, 20):
            raise ValueError(f"unexpected calibration ranks {(zero_rank, one_rank, two_rank)}")
        controls.append({"wedge_axis": wedge, "zero_rank": zero_rank,
                         "one_simple_tensor_rank": one_rank, "two_separated_simple_tensors_rank": two_rank})
    result = {"prime": mod.PRIME, "controls": controls,
              "scope": "Calibration only, not independent verification of candidate modular pivots."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
