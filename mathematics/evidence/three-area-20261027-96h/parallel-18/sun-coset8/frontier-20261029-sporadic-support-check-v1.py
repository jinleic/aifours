#!/usr/bin/env python3
"""Exact checks of sporadic-group order data used in the conditional assembly.

For each of the 26 sporadic groups and the Tits group: the stated factorization multiplies to
an order printed in the pinned Wikipedia HTML (tags stripped); report whether 7 divides |S|,
the number of distinct primes of |S|/7, and whether |S| divides 2520 = 7!/2.
"""
import hashlib
import re
import sys

PIN_SHA = "b22e8da1b42c3bf62bbfacff1bc795bafad3932527dff941a000eca907f349af"
ORDERS = {
    "M11": {2: 4, 3: 2, 5: 1, 11: 1}, "M12": {2: 6, 3: 3, 5: 1, 11: 1},
    "M22": {2: 7, 3: 2, 5: 1, 7: 1, 11: 1}, "M23": {2: 7, 3: 2, 5: 1, 7: 1, 11: 1, 23: 1},
    "M24": {2: 10, 3: 3, 5: 1, 7: 1, 11: 1, 23: 1}, "J1": {2: 3, 3: 1, 5: 1, 7: 1, 11: 1, 19: 1},
    "J2": {2: 7, 3: 3, 5: 2, 7: 1}, "J3": {2: 7, 3: 5, 5: 1, 17: 1, 19: 1},
    "J4": {2: 21, 3: 3, 5: 1, 7: 1, 11: 3, 23: 1, 29: 1, 31: 1, 37: 1, 43: 1},
    "HS": {2: 9, 3: 2, 5: 3, 7: 1, 11: 1}, "McL": {2: 7, 3: 6, 5: 3, 7: 1, 11: 1},
    "Suz": {2: 13, 3: 7, 5: 2, 7: 1, 11: 1, 13: 1}, "Co3": {2: 10, 3: 7, 5: 3, 7: 1, 11: 1, 23: 1},
    "Co2": {2: 18, 3: 6, 5: 3, 7: 1, 11: 1, 23: 1}, "Co1": {2: 21, 3: 9, 5: 4, 7: 2, 11: 1, 13: 1, 23: 1},
    "He": {2: 10, 3: 3, 5: 2, 7: 3, 17: 1}, "Ly": {2: 8, 3: 7, 5: 6, 7: 1, 11: 1, 31: 1, 37: 1, 67: 1},
    "Ru": {2: 14, 3: 3, 5: 3, 7: 1, 13: 1, 29: 1}, "ON": {2: 9, 3: 4, 5: 1, 7: 3, 11: 1, 19: 1, 31: 1},
    "HN": {2: 14, 3: 6, 5: 6, 7: 1, 11: 1, 19: 1}, "Th": {2: 15, 3: 10, 5: 3, 7: 2, 13: 1, 19: 1, 31: 1},
    "Fi22": {2: 17, 3: 9, 5: 2, 7: 1, 11: 1, 13: 1},
    "Fi23": {2: 18, 3: 13, 5: 2, 7: 1, 11: 1, 13: 1, 17: 1, 23: 1},
    "Fi24'": {2: 21, 3: 16, 5: 2, 7: 3, 11: 1, 13: 1, 17: 1, 23: 1, 29: 1},
    "B": {2: 41, 3: 13, 5: 6, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 31: 1, 47: 1},
    "M": {2: 46, 3: 20, 5: 9, 7: 6, 11: 2, 13: 3, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1, 41: 1, 47: 1, 59: 1, 71: 1},
    "Tits": {2: 11, 3: 3, 5: 2, 13: 1},
}
TABLE_D = {"J4": (29, "29:28"), "Fi24'": (29, "29:14"), "B": (47, "47:23"), "M": (71, "L2(71)")}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: check PINNED_WIKIPEDIA_HTML")
    raw = open(sys.argv[1], "rb").read()
    if hashlib.sha256(raw).hexdigest() != PIN_SHA:
        raise SystemExit("pinned page hash mismatch")
    text = re.sub("<[^>]+>", "", raw.decode("utf-8"))
    uncovered = []
    for g, f in ORDERS.items():
        n = 1
        for p, e in f.items():
            n *= p ** e
        if f"{n:,}" not in text:
            raise SystemExit(f"order of {g} not found in pinned page")
        if 2520 % n == 0:
            raise SystemExit(f"{g}: order divides 2520")
        if 7 not in f:
            status = "7 does not divide |S|"
        else:
            omega = sum(1 for p, e in f.items() if (e - (1 if p == 7 else 0)) > 0)
            if omega <= 7:
                status = f"omega(|S|/7)={omega}<=7"
            elif g in TABLE_D:
                status = f"omega(|S|/7)={omega}; BBGT Table D r={TABLE_D[g][0]}, H={TABLE_D[g][1]}"
            else:
                status = f"omega(|S|/7)={omega} UNCOVERED"
                uncovered.append(g)
        print(f"{g}: |S|={n}; {status}")
    if uncovered:
        raise SystemExit(f"FAIL uncovered {uncovered}")
    print("PASS: every sporadic group and the Tits group is covered by 7-free order, support<=7, or a Table D row")


if __name__ == "__main__":
    main()
