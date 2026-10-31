#!/usr/bin/env python3
"""Independent squarefree-prime-support overapproximation, NOT group enumeration.

Checks necessary pair constraints for the two reduced contradictions in the
Sun8 C3-transfer candidate. A zero count cannot authenticate imported Sun7 or
replace the written all-index group proof.
"""
from itertools import combinations
from math import gcd
import json


PRIMES = (2, 3, 5, 7)
SUPPORTS = tuple(
    __import__("math").prod(p for j, p in enumerate(PRIMES) if mask & (1 << j))
    for mask in range(16)
)


def satisfies_pair(i, bi, j, bj, proper):
    ni = (3 if proper[i] else 1) * bi
    nj = (3 if proper[j] else 1) * bj
    if gcd(ni, nj) > 7:
        return False
    if not (proper[i] and proper[j]) and gcd(bi, bj) == 1:
        return False
    return True


def run_case(proper_seven):
    names = ("A", "B", "V", "W", "F") if proper_seven else ("A", "B", "V", "W")
    proper = tuple(name in ("A", "B") for name in names)
    domains = []
    for name in names:
        domain = []
        for b in SUPPORTS:
            if name == "A" and ((b % 7 == 0) != proper_seven):
                continue
            if name in ("B", "F") and b % 7 == 0:
                continue
            if name in ("V", "W") and b % 7 != 0:
                continue
            if name == "V" and b % 2 == 0:
                continue
            domain.append(b)
        domains.append(tuple(domain))
    stages = [1] + [0] * len(names)
    first = None

    def rec(values):
        nonlocal first
        i = len(values)
        if i == len(names):
            if first is None:
                first = dict(zip(names, values))
            return
        for b in domains[i]:
            if all(satisfies_pair(j, old, i, b, proper)
                   for j, old in enumerate(values)):
                stages[i + 1] += 1
                rec(values + (b,))

    rec(())
    return {"labels": names, "proper": proper, "domain_sizes": list(map(len, domains)),
            "partial_counts": stages, "terminal_models": stages[-1],
            "first_terminal": first}


def main():
    print(json.dumps({"primes": PRIMES, "no_proper_7": run_case(False),
                      "one_proper_7": run_case(True),
                      "limits": "squarefree-support overapproximation of necessary constraints; not a group construction"},
                     indent=2))


if __name__ == "__main__":
    main()
