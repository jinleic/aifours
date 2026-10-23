#!/usr/bin/env python3
"""EXPLORATORY count-relaxation over the nine residue rank/weight pairs.

A satisfiable relaxation proves nothing. An unsatisfiable relaxation is only a lead until
its constraints receive a written proof and an independently checked certificate.
"""
import json
from pathlib import Path
import time

import z3

QUAD_WEIGHTS = {0: 0, 256: 0, 64: 1, 192: 1, 96: 2, 160: 2, 112: 3, 144: 3, 120: 4, 136: 4, 128: 3}
TYPES = [(0, 256), (2, 192), (4, 128), (4, 160), (6, 112), (6, 128), (6, 144), (8, 120), (8, 136)]


def residue(k):
    return ((k * k - 4) // 32) % 2


def pairs():
    out = []
    for d in (0, 1):
        s_values = [s for s in range(-28, 29) if s % 16 == (4 + 8 * d) % 16]
        r_values = [r for r in range(-24, 25) if r % 16 == (8 * d) % 16]
        for s in s_values:
            for r in r_values:
                kg, kh = (s + r) // 2, (s - r) // 2
                if abs(kg) > 26 or abs(kh) > 26 or kg % 8 != 2 or kh % 8 != 2:
                    continue
                if (residue(kg) ^ residue(kh)) != d:
                    raise AssertionError("residue/difference mismatch")
                out.append({"D": d, "S": s, "R": r, "Kg": kg, "Kh": kh, "Jg": residue(kg), "Jh": residue(kh)})
    return out


def check(rank, weight, rows):
    r = rank // 2
    solver = z3.Solver()
    n = [z3.Int(f"n{i}") for i in range(len(rows))]
    for var in n:
        solver.add(var >= 0)
    total = lambda f: z3.Sum([f(row) * var for row, var in zip(rows, n)])
    solver.add(total(lambda row: 1) == 256)
    solver.add(total(lambda row: row["D"]) == weight)
    ns, nr = z3.Int("NS"), z3.Int("NR")
    solver.add(ns >= 0, nr >= 0, ns + nr == 256)
    solver.add(total(lambda row: row["S"] ** 2) == 1024 * ns)
    solver.add(total(lambda row: row["R"] ** 2) == 1024 * nr)
    solver.add(total(lambda row: row["S"] * row["R"]) == 0)
    sum_g, sum_h = total(lambda row: row["Kg"]), total(lambda row: row["Kh"])
    solver.add(z3.Or(sum_g == 256, sum_g == -256), z3.Or(sum_h == 256, sum_h == -256))
    solver.add(z3.Sum([var for row, var in zip(rows, n) if row["D"] == 0 and row["R"] == 0]) >= 1)
    corr_s = total(lambda row: (-1) ** row["D"] * row["S"])
    corr_r = total(lambda row: (-1) ** row["D"] * row["R"])
    scale = 1 << (9 - r)
    solver.add(corr_s <= scale * ns, -corr_s <= scale * ns, corr_s <= 1 << (9 + r), -corr_s <= 1 << (9 + r))
    solver.add(corr_r <= scale * nr, -corr_r <= scale * nr, corr_r <= 1 << (9 + r), -corr_r <= 1 << (9 + r))
    for key, kkey in (("Jg", "Kg"), ("Jh", "Kh")):
        w = total(lambda row: row[key])
        z = total(lambda row: (-1) ** row[key] * row[kkey])
        options = []
        for qw, qr in QUAD_WEIGHTS.items():
            bound = 1 << (8 + qr)
            options.append(z3.And(w == qw, z <= bound, -z <= bound))
        solver.add(z3.Or(options))
    solver.set("timeout", 120000)
    result = solver.check()
    return str(result)


def main():
    rows = pairs()
    started = time.monotonic()
    results = [{"rank": rank, "weight": weight, "relaxation": check(rank, weight, rows)} for rank, weight in TYPES]
    report = {"status": "EXPLORATORY", "pair_states": len(rows), "results": results,
              "seconds": round(time.monotonic() - started, 2),
              "scope": "Count relaxation only. sat is not evidence of existence; unsat is not an exclusion until independently proved and certified."}
    Path(__file__).with_name("type-count-explore.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
