#!/usr/bin/env python3
"""Enumerate all truth restrictions on each discovered affine four-flat."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def walsh(signs):
    values = list(signs)
    step = 1
    while step < len(values):
        for base in range(0, len(values), 2 * step):
            for j in range(step):
                a, b = values[base + j], values[base + j + step]
                values[base + j], values[base + j + step] = a + b, a - b
        step *= 2
    return values


def core(points):
    if len(points) != 15 or len(set(points)) != 15:
        raise ValueError("expected 15 distinct points")
    base = points[0]
    differences = {0}
    for p in points[1:]:
        differences |= {x ^ p ^ base for x in differences}
    if len(differences) != 16:
        raise ValueError("affine hull is not a 4-flat")
    hull = {base ^ x for x in differences}
    missing = hull - set(points)
    if len(missing) != 1:
        raise ValueError("incorrect punctured 4-flat")
    origin = next(iter(missing))
    rows, span = [], {0}
    for x in sorted(differences):
        if x not in span:
            rows.append(x)
            span |= {old ^ x for old in span}
    if len(rows) != 4 or len(span) != 16:
        raise RuntimeError("basis construction mismatch")
    coords = []
    for mask in range(16):
        x = origin
        for i, row in enumerate(rows):
            if (mask >> i) & 1:
                x ^= row
        coords.append(x)
    return origin, rows, coords


def load_seeds(path):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    result = []
    for line in lines:
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        n = int(line, 16)
        result.append([(n >> (N - 1 - x)) & 1 for x in range(N)])
    return result


def analyze(bits, points, seed_index, output_dir):
    origin, rows, coords = core(points)
    original_local = [bits[x] for x in coords]
    original_local_w = walsh([1 - 2 * bit for bit in original_local])
    global_w = walsh([1 - 2 * bit for bit in bits])
    groups = [collections.Counter() for _ in range(16)]
    for a in range(N):
        alpha = sum(((a & row).bit_count() & 1) << i for i, row in enumerate(rows))
        sign = 1 - 2 * ((a & origin).bit_count() & 1)
        groups[alpha][sign * global_w[a] - original_local_w[alpha]] += 1
    if any(sum(group.values()) != 32 for group in groups):
        raise RuntimeError("frequency fibre size mismatch")
    universal_interval = all(-22 in group and 26 in group and set(group) <= {-22, -6, 10, 26}
                             for group in groups)
    valid = 0
    balanceable = 0
    original_seen = False
    max_hist = collections.Counter()
    local_hist_classes = collections.Counter()
    for local in range(1 << 16):
        local_bits = [(local >> u) & 1 for u in range(16)]
        loc_w = walsh([1 - 2 * bit for bit in local_bits])
        if any(abs(r + loc_w[alpha]) > 28 for alpha, group in enumerate(groups) for r in group):
            continue
        valid += 1
        original_seen |= local_bits == original_local
        absolute = collections.Counter()
        for alpha, group in enumerate(groups):
            for r, multiplicity in group.items():
                absolute[abs(r + loc_w[alpha])] += multiplicity
        peak = max(absolute)
        zeros = absolute.get(0, 0)
        max_hist[peak] += 1
        local_hist_classes[tuple(sorted(collections.Counter(loc_w).items()))] += 1
        if zeros:
            balanceable += 1
            if balanceable == 1:
                changed = bits.copy()
                for u, position in enumerate(coords):
                    changed[position] = local_bits[u]
                spectrum = walsh([1 - 2 * bit for bit in changed])
                a0 = spectrum.index(0)
                truth = "".join(str(bit ^ ((x & a0).bit_count() & 1)) for x, bit in enumerate(changed))
                name = output_dir / f"frontier-20261028-core-witness-seed{seed_index}.json"
                with name.open("x", encoding="utf-8") as out:
                    json.dump({"format": "boolean-truth-v1", "seed_index_1based": seed_index,
                               "local_index": local, "affine_twist_frequency": a0, "bits": truth}, out, indent=2)
                    out.write("\n")
    return {"core_origin": origin, "basis": rows, "local_restrictions_checked": 1 << 16,
            "outside_interval_hypotheses_verified": universal_interval,
            "allowed_peak28_restrictions": valid, "balanceable_peak28_restrictions": balanceable,
            "original_restriction_seen": original_seen, "peak_histogram": dict(sorted(max_hist.items())),
            "local_walsh_classes": [{"histogram": dict(k), "count": v} for k, v in sorted(local_hist_classes.items())],
            "outside_histograms": [dict(sorted(g.items())) for g in groups]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--span-results", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    seeds = load_seeds(args.seeds)
    spans = json.loads(args.span_results.read_text(encoding="utf-8"))["reports"]
    if len(seeds) != len(spans):
        raise ValueError("seed/span count mismatch")
    reports = []
    for i, (bits, item) in enumerate(zip(seeds, spans), 1):
        result = analyze(bits, item["points"], i, args.output.parent)
        reports.append({"seed_index_1based": i, **result})
        print(f"seed={i} local_states={result['local_restrictions_checked']} "
              f"outside_hypotheses={result['outside_interval_hypotheses_verified']} "
              f"peak28={result['allowed_peak28_restrictions']} target={result['balanceable_peak28_restrictions']} "
              f"local_classes={len(result['local_walsh_classes'])}", flush=True)
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "span_results_sha256": hashlib.sha256(args.span_results.read_bytes()).hexdigest(),
               "method": "full global/local FWHT; all 65536 local Boolean restrictions",
               "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()
