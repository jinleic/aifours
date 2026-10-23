#!/usr/bin/env python3
"""Direct-character/support-moment audit; imports no research producer code."""
import hashlib
import json
from pathlib import Path
import random
import time


def polynomial(support, dimension):
    weight = len(support)
    if weight % 2 != 1 or dimension < 4:
        raise ValueError("The lemma requires odd weight and dimension >=4")
    counts = [sum((x >> i) & 1 for x in support) for i in range(dimension)]
    gamma = (1 - weight) // 2
    linear = [(c * (c - 1) // 2 + gamma * c) % 2 for c in counts]
    cross = {
        (i, j): ((counts[i] & 1) * (counts[j] & 1)
                 + sum(((x >> i) & 1) * ((x >> j) & 1) for x in support)) % 2
        for i in range(dimension) for j in range(i + 1, dimension)
    }
    constant = ((weight * weight - 1) // 8) % 2
    return [
        (constant + sum(linear[i] * ((a >> i) & 1) for i in range(dimension))
         + sum(c * ((a >> i) & 1) * ((a >> j) & 1)
               for (i, j), c in cross.items())) % 2
        for a in range(1 << dimension)
    ]


def direct_walsh(support, dimension):
    marked = set(support)
    return [sum(1 if ((x in marked) + ((a & x).bit_count() % 2)) % 2 == 0 else -1
                for x in range(1 << dimension))
            for a in range(1 << dimension)]


def check(spectrum, expected):
    if len(spectrum) != len(expected):
        raise ValueError("Spectrum dimension mismatch")
    for a, (value, bit) in enumerate(zip(spectrum, expected)):
        numerator = value * value - 4
        if numerator % 32 or (numerator // 32) % 2 != bit:
            raise ValueError(f"Quadratic residue mismatch at character {a}")


def main():
    started = time.monotonic()
    generator = random.Random(20261015)
    cases = []
    for dimension in (4, 5, 6, 7, 8):
        size = 1 << dimension
        weights = sorted({1, 3, size // 2 - 1, size // 2 + 1, size - 3, size - 1})
        for weight in weights:
            support = sorted(generator.sample(range(size), weight))
            expected = polynomial(support, dimension)
            spectrum = direct_walsh(support, dimension)
            check(spectrum, expected)
            corrupt = spectrum.copy()
            corrupt[generator.randrange(size)] += 8
            try:
                check(corrupt, expected)
            except ValueError:
                pass
            else:
                raise AssertionError("Corrupted spectrum was accepted")
            cases.append({"dimension": dimension, "weight": weight,
                          "table_sha256": hashlib.sha256(bytes(int(x in set(support)) for x in range(size))).hexdigest(),
                          "characters": size, "corrupt_spectrum_rejected": True})
    rejected_inputs = 0
    for support, dimension in (([], 8), ([1, 2], 8), ([1], 3)):
        try:
            polynomial(support, dimension)
        except ValueError:
            rejected_inputs += 1
        else:
            raise AssertionError("Out-of-contract input was accepted")
    result = {"status": "PASS", "cases": cases,
              "direct_characters_checked": sum(c["characters"] for c in cases),
              "out_of_contract_inputs_rejected": rejected_inputs,
              "seconds": round(time.monotonic() - started, 4),
              "scope": "Finite deterministic implementation controls; universal proof is boolean-residue-audit.md, not a finite test.",
              "implementation": "Direct character sums and explicit support moments; no producer imports."}
    destination = Path(__file__).with_name("boolean-residue-audit.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
