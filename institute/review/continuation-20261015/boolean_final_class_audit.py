#!/usr/bin/env python3
"""Parent-written exclusion audit for one odd fixed-half completion class.

Inputs are the immutable epoch-2 source corpus and known NL242 seed tables.
No research-lane code is imported. Positive controls use real NL242 tables,
whose true complementary halves must survive every necessary condition.
"""
import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import re
import time

import numpy as np

ROOT = Path("/Users/jinleic/repos/aifours/institute/runs/hard-2026-10-15/problems/info-p0403/attack-e2")
SLICE_SHA256 = "200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d"
SLICE = ROOT / "results/slice-screen.json.gz"
def allowed_magnitudes(bit, cap):
    return [m for m in range(2, cap + 1, 4) if residue_bit(m) == bit]


def parity(value):
    return value.bit_count() & 1


def canonical(magnitude):
    return magnitude if magnitude % 8 == 2 else -magnitude


def residue_bit(magnitude):
    return ((magnitude * magnitude - 4) // 32) & 1


def walsh_direct(table):
    size = len(table)
    signs = np.array([-1 if bit else 1 for bit in table], dtype=np.int64)
    characters = np.array([[1 - 2 * parity(a & x) for x in range(size)] for a in range(size)], dtype=np.int64)
    return characters @ signs


def decode_hex(text):
    bits = "".join(format(int(c, 16), "04b") for c in text.strip())
    if len(bits) != 512:
        raise ValueError("hex table must encode 512 bits")
    return [int(c) for c in bits]


def split(table, normal, base_index):
    """Return halves g,h and the map between 9-bit and 8-bit characters."""
    if normal == 0 or not 0 <= base_index < 9 or not (normal >> base_index) & 1:
        raise ValueError("base_index must be a coordinate in the normal")
    other = [i for i in range(9) if i != base_index]
    kernel = []
    for y in range(256):
        x = 0
        for position, coordinate in enumerate(other):
            if (y >> position) & 1:
                x |= 1 << coordinate
        if parity(x & normal):
            x |= 1 << base_index
        kernel.append(x)
    outside = 1 << base_index
    if parity(outside & normal) != 1 or any(parity(x & normal) for x in kernel):
        raise ValueError("bad hyperplane basis")
    g = [table[x] for x in kernel]
    h = [table[x ^ outside] for x in kernel]
    return g, h, kernel, outside


def quadratic_monomials():
    return [()] + [(i,) for i in range(8)] + list(itertools.combinations(range(8), 2))


def evaluate_monomial(monomial, point):
    return int(all((point >> i) & 1 for i in monomial))


def gf2_solve(rows, rhs, width):
    """Return particular solution and nullspace basis, or None if inconsistent."""
    pivots = []
    reduced = []
    for row, bit in zip(rows, rhs):
        for pivot, (prow, pbit) in zip(pivots, reduced):
            if (row >> pivot) & 1:
                row ^= prow
                bit ^= pbit
        if row == 0:
            if bit:
                return None
            continue
        pivot = row.bit_length() - 1
        for index, (prow, pbit) in enumerate(reduced):
            if (prow >> pivot) & 1:
                reduced[index] = (prow ^ row, pbit ^ bit)
        pivots.append(pivot)
        reduced.append((row, bit))
    particular = 0
    for pivot, (row, bit) in zip(pivots, reduced):
        if bit:
            particular |= 1 << pivot
    free = [i for i in range(width) if i not in set(pivots)]
    basis = []
    for column in free:
        vector = 1 << column
        for pivot, (row, _) in zip(pivots, reduced):
            if (row >> column) & 1:
                vector |= 1 << pivot
        basis.append(vector)
    return particular, basis


def quadratic_candidates(forced_zero):
    monomials = quadratic_monomials()
    rows = []
    for b in forced_zero:
        row = 0
        for index, monomial in enumerate(monomials):
            if evaluate_monomial(monomial, b):
                row |= 1 << index
        rows.append(row)
    solved = gf2_solve(rows, [0] * len(rows), len(monomials))
    particular, basis = solved
    candidates = []
    for mask in range(1 << len(basis)):
        coeffs = particular
        for index, vector in enumerate(basis):
            if (mask >> index) & 1:
                coeffs ^= vector
        values = []
        for b in range(256):
            bit = 0
            for index, monomial in enumerate(monomials):
                if (coeffs >> index) & 1 and evaluate_monomial(monomial, b):
                    bit ^= 1
            values.append(bit)
        candidates.append(values)
    return candidates, len(monomials) - len(basis)


def test_candidate(G, J, true_H=None, minimize=True, bound=28):
    caps = [bound - abs(int(value)) for value in G]
    domains = []
    for cap, bit in zip(caps, J):
        allowed = allowed_magnitudes(bit, cap)
        if not allowed:
            return {"excluded": True, "reason": "empty residue/capacity domain"}
        domains.append(allowed)
    m0 = [max(domain) for domain in domains]
    K0 = [canonical(m) for m in m0]
    slack = sum(m * m for m in m0) - 65536
    if slack < 0:
        return {"excluded": True, "reason": "maximum Parseval energy below 65536", "slack": slack}
    if slack % 64:
        return {"excluded": True, "reason": "Parseval slack not divisible by 64", "slack": slack}
    if sum(min(domain) ** 2 for domain in domains) > 65536:
        return {"excluded": True, "reason": "minimum Parseval energy above 65536", "slack": slack}
    A = [sum((1 - 2 * parity(b & x)) * K0[b] for b in range(256)) for x in range(256)]
    if any(value % 16 for value in A):
        return {"excluded": True, "reason": "FWHT(K0) not divisible by 16", "slack": slack}
    r = [(value // 16 - 16) % 32 for value in A]
    equations = []
    for size in range(0, 9):
        for subset in itertools.combinations(range(8), size):
            mask = sum(1 << i for i in subset)
            parities = set()
            for x in range(256):
                value = 0
                sub = mask
                while True:
                    value += (-1) ** sub.bit_count() * r[x ^ sub]
                    if sub == 0:
                        break
                    sub = (sub - 1) & mask
                if size >= 5:
                    if value % 32:
                        return {"excluded": True, "reason": f"Moebius consistency fails for |S|={size}", "slack": slack}
                    continue
                if value % (1 << size):
                    return {"excluded": True, "reason": f"Moebius divisibility fails for |S|={size}", "slack": slack}
                parities.add((value >> size) & 1)
            if size >= 5:
                continue
            if len(parities) != 1:
                return {"excluded": True, "reason": f"x-dependent parity for |S|={size}", "slack": slack}
            row = 0
            for a in range(256):
                if a & mask == mask:
                    row |= 1 << a
            equations.append((row, parities.pop()))
    locked = [a for a in range(256) if len(domains[a]) == 1]
    rows = [row for row, _ in equations] + [1 << a for a in locked]
    rhs = [bit for _, bit in equations] + [0] * len(locked)
    solved = gf2_solve(rows, rhs, 256)
    if solved is None:
        return {"excluded": True, "reason": "parity system inconsistent", "slack": slack}
    particular, basis = solved
    odd_cost = []
    for a in range(256):
        costs = [(K0[a] ** 2 - canonical(m) ** 2) // 64 for m in domains[a]
                 if ((K0[a] - canonical(m)) // 16) % 2]
        odd_cost.append(min(costs) if costs else None)
    if any(((particular >> a) & 1) and odd_cost[a] is None for a in range(256)):
        raise AssertionError("locked point has parity one")
    result = {"slack_units": slack // 64, "parity_dimension": len(basis),
              "equations": len(equations), "locked_points": len(locked)}
    if minimize:
        if len(basis) > 22:
            return {**result, "excluded": False, "reason": "parity space too large for this audit"}
        weights = {}
        for a, cost in enumerate(odd_cost):
            if cost:
                weights.setdefault(cost, 0)
                weights[cost] |= 1 << a
        best = None
        current = particular
        gray_previous = 0
        for counter in range(1 << len(basis)):
            gray = counter ^ (counter >> 1)
            changed = gray ^ gray_previous
            if changed:
                current ^= basis[changed.bit_length() - 1]
            gray_previous = gray
            total = sum(cost * (current & mask).bit_count() for cost, mask in weights.items())
            if best is None or total < best:
                best = total
        excluded = best * 64 > slack
        result.update({"excluded": excluded, "minimum_odd_cost_units": best, "patterns": 1 << len(basis),
                       "reason": "minimum odd-parity energy deficit exceeds Parseval slack" if excluded
                       else "parity screen passed"})
    else:
        result.update({"excluded": False, "reason": "minimization skipped for positive-control truth check"})
    if true_H is not None:
        true_K = None
        sign_options = []
        for epsilon in (1, -1):
            for s in range(256):
                candidate = [epsilon * (1 - 2 * parity(a & s)) * int(true_H[a]) for a in range(256)]
                if all(value % 8 == 2 for value in candidate):
                    sign_options.append(candidate)
        if len(sign_options) != 1:
            raise AssertionError("canonical phase not unique")
        true_K = sign_options[0]
        e = [(K0[a] - true_K[a]) // 16 for a in range(256)]
        if any((K0[a] - true_K[a]) % 16 for a in range(256)):
            raise AssertionError("true spectrum not on the K0-16e lattice")
        true_p = sum(1 << a for a in range(256) if e[a] % 2)
        consistent = all(((row & true_p).bit_count() & 1) == bit for row, bit in zip(rows, rhs))
        true_deficit = sum(K0[a] ** 2 - true_K[a] ** 2 for a in range(256))
        result.update({"true_completion_satisfies_parity_system": consistent,
                       "true_energy_deficit_units": true_deficit // 64,
                       "true_odd_cost_units": sum(odd_cost[a] for a in range(256) if (true_p >> a) & 1)})
    return result


def audit_class(table, normal, base_index, include_truth=False, bound=28):
    g, h, kernel, outside = split(table, normal, base_index)
    G = walsh_direct(g)
    H = walsh_direct(h)
    full = walsh_direct(table)
    for a in range(512):
        b = 0
        for position in range(8):
            if parity(a & kernel[1 << position]):
                b |= 1 << position
        expected = int(G[b]) + (1 - 2 * parity(a & outside)) * int(H[b])
        if int(full[a]) != expected:
            raise AssertionError("half-spectrum decomposition failed")
    if sum(g) % 2 != 1:
        raise ValueError("class requires an odd-weight fixed half")
    forced = [b for b in range(256) if abs(int(G[b])) == bound - 2]
    summary = {"fixed_half_weight": sum(g), "max_abs_G": int(np.max(np.abs(G))), "forced_zero_points": len(forced),
               "full_max_abs_walsh": int(np.max(np.abs(full)))}
    if include_truth:
        true_J = [residue_bit(abs(int(value))) for value in H]
        monomials = quadratic_monomials()
        rows = []
        for b in range(256):
            row = 0
            for index, monomial in enumerate(monomials):
                if evaluate_monomial(monomial, b):
                    row |= 1 << index
            rows.append(row)
        if gf2_solve(rows, true_J, len(monomials)) is None:
            raise AssertionError("true residue is not quadratic")
        if any(true_J[b] for b in forced):
            raise AssertionError("true residue violates a forced zero")
        report = test_candidate(G, true_J, H, minimize=False, bound=bound)
        report["is_true_completion_residue"] = True
        return {**summary, "quadratic_candidates": "true residue only", "candidates": [report]}
    candidates, rank = quadratic_candidates(forced)
    reports = []
    for J in candidates:
        report = test_candidate(G, J, bound=bound)
        report["is_true_completion_residue"] = False
        reports.append(report)
    return {**summary, "residue_constraint_rank": rank, "quadratic_candidates": len(candidates), "candidates": reports}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("boolean-final-class-audit.json"))
    args = parser.parse_args()
    started = time.monotonic()
    raw = SLICE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SLICE_SHA256:
        raise AssertionError("immutable epoch-2 corpus hash changed")
    corpus = json.loads(gzip.decompress(raw))
    source = corpus["sources"][96]
    table = [int(c) for c in source["bits"]]
    if hashlib.sha256(source["bits"].encode()).hexdigest() != source["sha256_ascii_bits"]:
        raise AssertionError("source table hash mismatch")
    spectrum = walsh_direct(table)
    if sum(table) != 256 or 256 - int(np.max(np.abs(spectrum))) // 2 != 240:
        raise AssertionError("source is not balanced NL240")
    target = audit_class(table, 511, 8)
    target_excluded = all(c["excluded"] for c in target["candidates"])
    def checked_truth(label, report):
        truth = [c for c in report["candidates"] if c["is_true_completion_residue"]]
        if len(truth) != 1 or truth[0]["excluded"] or not truth[0].get("true_completion_satisfies_parity_system"):
            raise AssertionError(f"positive control {label} was wrongly excluded")
        if truth[0]["true_energy_deficit_units"] != truth[0]["slack_units"]:
            raise AssertionError(f"positive control {label} violates exact Parseval deficit")
        if truth[0]["true_odd_cost_units"] > truth[0]["slack_units"]:
            raise AssertionError(f"positive control {label} exceeds odd-parity lower bound")
        return truth[0]

    controls = []
    # Genuine bound-32 completions: each listed source is a completion of its own fixed half.
    for source_index, normal in ((96, 511), (0, None), (37, None), (123, None)):
        record = corpus["sources"][source_index]
        source_table = [int(c) for c in record["bits"]]
        source_xor = record["support_xor"]
        if normal is None:
            normal = next(v for v in range(511, 0, -1) if parity(v & source_xor) == 1)
        base_index = next(i for i in range(9) if (normal >> i) & 1)
        report = audit_class(source_table, normal, base_index, include_truth=True, bound=32)
        controls.append({"kind": "listed source completes its own class at bound 32", "source": source_index,
                         "normal": normal, "true_candidate": checked_truth(f"source{source_index}", report)})
    seed_text = (ROOT / "code/seeds.py").read_text() + (ROOT / "code/extra_seeds.py").read_text()
    seeds = {}
    for name, body in re.findall(r"['\"]([A-Za-z0-9_-]+)['\"]\s*:\s*\(\s*((?:['\"][0-9A-Fa-f]+['\"]\s*)+)\)", seed_text):
        seeds[name] = "".join(re.findall(r"[0-9A-Fa-f]{16,}", body))
    for name, hex_table in sorted(seeds.items()):
        seed = decode_hex(hex_table)
        seed_spectrum = walsh_direct(seed)
        if 256 - int(np.max(np.abs(seed_spectrum))) // 2 != 242:
            raise AssertionError(f"seed {name} is not NL242 under the documented bit order")
        support_xor = 0
        for x, bit in enumerate(seed):
            if bit:
                support_xor ^= x
        if support_xor == 0:
            controls.append({"kind": "published NL242 seed", "seed": name, "applicable": False,
                             "reason": "support XOR zero, so every hyperplane half has even weight"})
            continue
        normal = next(v for v in range(511, 0, -1) if parity(v & support_xor) == 1)
        base_index = next(i for i in range(9) if (normal >> i) & 1)
        report = audit_class(seed, normal, base_index, include_truth=True)
        controls.append({"kind": "published NL242 seed at bound 28", "seed": name, "weight": sum(seed),
                         "normal": normal, "support_xor": support_xor, "applicable": True,
                         "true_candidate": checked_truth(name, report)})
    result = {"status": "PASS" if target_excluded else "NOT_EXCLUDED",
              "input_sha256": hashlib.sha256(raw).hexdigest(),
              "target": {"source": 96, "normal": 511, "source_bits_sha256": source["sha256_ascii_bits"], **target},
              "target_excluded": target_excluded, "positive_controls": controls,
              "seconds": round(time.monotonic() - started, 1),
              "scope": "One listed fixed odd-half completion class; no global nonexistence. Positive controls are genuine odd-half completions (listed sources at bound 32 and applicable published NL242 seeds at bound 28)."}
    args.output.write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({"status": result["status"], "target": {k: v for k, v in target.items() if k != "candidates"},
                      "target_reasons": [c["reason"] for c in target["candidates"]],
                      "target_minimum_costs": [c.get("minimum_odd_cost_units") for c in target["candidates"]],
                      "controls": [{k: v for k, v in c.items() if k != "true_candidate"}
                                   | ({"true": {k: c["true_candidate"].get(k) for k in ("slack_units", "parity_dimension", "true_odd_cost_units", "true_energy_deficit_units", "true_completion_satisfies_parity_system")}}
                                      if "true_candidate" in c else {})
                                   for c in controls],
                      "seconds": result["seconds"]}, indent=1))
    if not target_excluded:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
