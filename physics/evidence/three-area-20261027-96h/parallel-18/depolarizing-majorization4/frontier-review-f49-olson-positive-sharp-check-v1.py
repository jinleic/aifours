#!/usr/bin/env python3
"""Check an actual-word equality case for the positive crosscut count bound."""

import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("olson_check", ROOT / "frontier-review-f49-olson-selector-check-v1.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def main():
    rows = []
    for p in (3, 5, 7, 11, 13):
        h = (p - 1) // 2
        A = set(range(h + 1))
        B0 = (set(range(p)) - A) | {0}
        for delta in range(p):
            B = {(delta + z) % p for z in B0}
            left = sorted(A) + [1] * p
            right = sorted(B)
            refs = [(1, z) for z in left + right]
            word = refs + [(0, delta)] + [(0, 0)] * (2 * p - 3)
            I = list(range(len(refs), len(word)))
            assert len(word) == 4 * p - 1 and len(I) == 2 * p - 2
            S, z = c.potential_data(p, word, I)
            assert S == delta
            count = sum(c.ordered_product(p, word, I + [a[0], b[0]]) == (0, 0) for a, b in itertools.product(z[:len(left)], z[len(left):]))
            assert count == len(A) + len(B) - p == 1
        rows.append({"p": p, "deltas_checked": p, "distinct_selectors_for_each": 1})
    print(json.dumps({"scope": "bounded exact actual-word checks of positive-count equality; written construction applies to every odd prime", "rows": rows, "total_actual_words": sum(row["deltas_checked"] for row in rows)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
