#!/usr/bin/env python3
"""Independent C2 squarefree support overapproximation, not group enumeration."""
from math import gcd, prod
import json


PRIMES = (2, 3, 5, 7)
SUPPORTS = tuple(prod(p for j, p in enumerate(PRIMES) if mask & (1 << j))
                 for mask in range(16))


def run_case(proper_seven):
    names = ("A", "B", "V", "W", "F") if proper_seven else ("A", "B", "V", "W")
    proper = tuple(name in ("A", "B") for name in names)
    domains = []
    for name in names:
        choices = []
        for b in SUPPORTS:
            if name == "A" and ((b % 7 == 0) != proper_seven):
                continue
            if name in ("B", "F") and b % 7 == 0:
                continue
            if name in ("V", "W") and (b % 7 != 0 or b % 2 == 0):
                continue
            choices.append(b)
        domains.append(choices)
    counts = [1] + [0] * len(names)
    first = None

    def visit(values):
        nonlocal first
        i = len(values)
        if i == len(names):
            if first is None:
                first = dict(zip(names, values))
            return
        for bi in domains[i]:
            ni = (2 if proper[i] else 1) * bi
            valid = True
            for j, bj in enumerate(values):
                nj = (2 if proper[j] else 1) * bj
                if gcd(ni, nj) > 7 or (not (proper[i] and proper[j]) and gcd(bi, bj) == 1):
                    valid = False
                    break
            if valid:
                counts[i + 1] += 1
                visit(values + (bi,))

    visit(())
    return {"labels": names, "domain_sizes": list(map(len, domains)),
            "partial_counts": counts, "terminal_models": counts[-1], "first_model": first}


print(json.dumps({"no_proper_7": run_case(False), "one_proper_7": run_case(True),
                  "limits": "squarefree-support necessary conditions only; not group enumeration"}, indent=2))
