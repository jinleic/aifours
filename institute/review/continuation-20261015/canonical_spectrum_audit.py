#!/usr/bin/env python3
"""Independent direct-sum controls for canonical phase and energy distance."""
import json
from pathlib import Path
import random
import time

from boolean_residue_audit import direct_walsh


def canonical(value):
    magnitude = abs(value)
    if magnitude % 4 != 2:
        raise ValueError("Odd-weight spectrum requires magnitude two modulo four")
    return magnitude if magnitude % 8 == 2 else -magnitude


def direct_inverse(values):
    return [sum((-1 if (a & x).bit_count() % 2 else 1) * value
                for a, value in enumerate(values))
            for x in range(len(values))]


def check_inverse(values):
    size = len(values)
    transformed = direct_inverse(values)
    if any(abs(value) != size for value in transformed):
        raise ValueError("Canonical inverse is not a Boolean sign table")
    return transformed


def main():
    started = time.monotonic()
    generator = random.Random(20261016)
    cases = []
    for dimension in (4, 6, 8):
        size = 1 << dimension
        for weight in (1, 3, size // 2 - 1, size // 2 + 1, size - 1):
            support = set(generator.sample(range(size), weight))
            spectrum = direct_walsh(support, dimension)
            values = [canonical(value) for value in spectrum]
            transformed = check_inverse(values)
            xor = 0
            for x in support:
                xor ^= x
            phase = -1 if ((weight + 1) // 2) % 2 else 1
            expected = [phase * size * (-1 if (x ^ xor) in support else 1) for x in range(size)]
            if transformed != expected:
                raise AssertionError("Explicit phase/translation identity failed")
            corrupt = values.copy()
            corrupt[generator.randrange(size)] += 8
            try:
                check_inverse(corrupt)
            except ValueError:
                pass
            else:
                raise AssertionError("Corrupt inverse was accepted")
            cases.append({"dimension": dimension, "weight": weight,
                          "explicit_phase_and_translation": True,
                          "corrupt_inverse_rejected": True})
    pair_checks = 0
    for capacity in range(2, 27):
        for residue in (0, 1):
            domain = [m for m in range(2, capacity + 1, 4)
                      if ((m * m - 4) // 32) % 2 == residue]
            if not domain:
                continue
            upper = max(domain)
            for value in domain:
                if 4 * abs(canonical(upper) - canonical(value)) > upper * upper - value * value:
                    raise AssertionError("Energy-distance inequality failed")
                pair_checks += 1
    result = {"status": "PASS", "cases": cases,
              "finite_capacity_pair_checks": pair_checks,
              "seconds": round(time.monotonic() - started, 4),
              "scope": "Direct-sum phase/inverse and complete finite-domain inequality controls; no class exclusion count or novelty certified."}
    Path(__file__).with_name("canonical-spectrum-audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
