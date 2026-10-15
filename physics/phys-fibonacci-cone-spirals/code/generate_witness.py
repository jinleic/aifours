#!/usr/bin/env python3
"""Generate the fixed triangular-lattice witness; no search or optimization."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def orbit(a, b):
    points = []
    for _ in range(6):
        points.append((a, b))
        a, b = -b, a + b
    return points


def main():
    representatives = sorted({
        min(orbit(a, b))
        for a in range(-24, 25)
        for b in range(-24, 25)
        if 100 <= a * a + a * b + b * b <= 400
    })
    witness = {
        "model": "intrinsic cone R^2/C6, sector angle pi/3",
        "basis": ["(1,0)", "(1/2,sqrt(3)/2)"],
        "center_radius_squared_bounds": [100, 400],
        "frustum_radius_bounds": ["19/2", "41/2"],
        "disk_diameter": 1,
        "centers": representatives,
    }
    target = ROOT / "results" / "lattice-witness.json"
    target.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"GENERATED: {len(representatives)} orbit representatives")


if __name__ == "__main__":
    main()
