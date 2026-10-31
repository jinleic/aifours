#!/usr/bin/env python3
"""Exact sparse support search over four simultaneous two-level local gates.

Each party independently chooses one of 15 coordinate pairs and relative phase
1 or i in an equal-angle U(2) gate. Arithmetic uses Z[sqrt(2),i]. The global
normalizing denominator is sqrt(72*2**4). Relative phases -1 and -i are
output-monomially equivalent to 1 and i, respectively, for a single gate;
therefore the search represents the full {+/-1,+/-i} relative-phase set up
to output row phases/permutations. This is not a general U(6)^4 search.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys

Z = (0, 0, 0, 0)


def plus(x, y):
    return tuple(a+b for a, b in zip(x, y))


def neg(x):
    return tuple(-a for a in x)


def phase_i(x):
    a, b, c, d = x
    return -c, -d, a, b


def accumulate(result, key, value):
    value = plus(result.get(key, Z), value)
    if value == Z:
        result.pop(key, None)
    else:
        result[key] = value


def apply_gate(tensor, axis, p, q, phase):
    """Unnormalized block [[1,z],[-conj(z),1]], sqrt(2) on rest."""
    result = {}
    for coord, val in tensor.items():
        j = coord[axis]
        if j not in (p, q):
            a, b, c, d = val
            accumulate(result, coord, (2*b, a, 2*d, c))
            continue
        kp = coord[:axis] + (p,) + coord[axis+1:]
        kq = coord[:axis] + (q,) + coord[axis+1:]
        if j == p:
            accumulate(result, kp, val)
            # -conj(1)=-1, -conj(i)=i
            accumulate(result, kq, neg(val) if phase == 0 else phase_i(val))
        else:
            accumulate(result, kp, val if phase == 0 else phase_i(val))
            accumulate(result, kq, val)
    return result


def conjugate_product(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (a*e+2*b*f+c*g+2*d*h, a*f+b*e+c*h+d*g,
            c*e+2*d*f-a*g-2*b*h, c*f+d*e-a*h-b*g)


def verify_six(tensor, depth):
    denominator = 72*(2**depth)
    norm = Z
    for x in tensor.values():
        norm = plus(norm, conjugate_product(x, x))
    if norm != (denominator, 0, 0, 0):
        raise ValueError(f"normalization mismatch: {norm} != {denominator}")
    for pair in itertools.combinations(range(4), 2):
        other = tuple(a for a in range(4) if a not in pair)
        gram = collections.defaultdict(lambda: Z)
        grouped = collections.defaultdict(list)
        for coord, coeff in tensor.items():
            grouped[tuple(coord[a] for a in other)].append((tuple(coord[a] for a in pair), coeff))
        for entries in grouped.values():
            for i, x in entries:
                for j, y in entries:
                    gram[(i,j)] = plus(gram[(i,j)], conjugate_product(x,y))
        for i in itertools.product(range(6), repeat=2):
            for j in itertools.product(range(6), repeat=2):
                expected = (denominator//36, 0, 0, 0) if i == j else Z
                if gram.get((i,j), Z) != expected:
                    raise ValueError(f"marginal {pair} failed at {i},{j}")
    return {"norm_numerator": norm, "denominator": denominator,
            "marginals": 6, "entries_checked_per_marginal": 1296}


def final_counts(state, pairs):
    """Compute exact final support for every last pair and both phases."""
    fibers = collections.defaultdict(dict)
    for coord, coeff in state.items():
        fibers[coord[:3]][coord[3]] = coeff
    stats = {pair: [0, 0] for pair in pairs}
    for fiber in fibers.values():
        for p, q in pairs:
            x, y = fiber.get(p), fiber.get(q)
            if (x is None) != (y is None):
                stats[(p,q)][0] += 1
                stats[(p,q)][1] += 1
            elif x is not None:
                if x == y or x == neg(y):
                    stats[(p,q)][0] -= 1
                iy = phase_i(y)
                if x == iy or x == neg(iy):
                    stats[(p,q)][1] -= 1
    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("verifier", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("dense_verifier", args.verifier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    raw, table_sha = module.load_table(args.table)
    state0 = {key: (a,b,0,0) for key,(a,b) in raw.items()}
    if len(state0) != 60:
        raise ValueError("expected support-60 input")
    pairs = tuple(itertools.combinations(range(6), 2))
    options = tuple((p,q,phase) for p,q in pairs for phase in range(2))
    histogram = collections.Counter()
    by_phase = collections.defaultdict(collections.Counter)
    min_support = None
    best = None
    count = 0
    # Fixed order 0,1,2,3 is complete because gates act on distinct parties.
    for g0 in options:
        t0 = apply_gate(state0, 0, *g0)
        for g1 in options:
            t1 = apply_gate(t0, 1, *g1)
            for g2 in options:
                t2 = apply_gate(t1, 2, *g2)
                deltas = final_counts(t2, pairs)
                for pair in pairs:
                    for phase in range(2):
                        support = len(t2) + deltas[pair][phase]
                        pattern = (g0[2], g1[2], g2[2], phase)
                        histogram[support] += 1
                        by_phase[pattern][support] += 1
                        count += 1
                        if min_support is None or support < min_support:
                            min_support = support
                            best = (g0, g1, g2, (*pair, phase))
    # Independently materialize the reported best and its marginals.
    state = state0
    for axis, gate in enumerate(best):
        state = apply_gate(state, axis, *gate)
    if len(state) != min_support:
        raise ValueError(f"final support formula mismatch: {len(state)} != {min_support}")
    check = verify_six(state, 4)
    if count != 15**4 * 16:
        raise ValueError(f"incomplete search: {count}")
    result = {"table_sha256": table_sha,
              "gate": "(1/sqrt2)[[1,z],[-conj(z),1]] on pair, identity elsewhere; z in {1,i}",
              "sequence_count": count, "support_histogram": dict(sorted(histogram.items())),
              "phase_pattern_minima": [{"phases": key, "minimum": min(v), "count": sum(v.values())} for key,v in sorted(by_phase.items())],
              "best_support": min_support, "best_gates_party_p_q_phase": best,
              "best_exact_six_marginal_check": check,
              "best_coefficients_Qsqrt2_i": [[*coord,*coeff] for coord,coeff in sorted(state.items())],
              "limitations": "Discrete equal-angle, fourth-root phases and one coordinate pair per party only. One in-harness search implementation; no global orbit or AME minimum claim."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    summary = {k:result[k] for k in ("table_sha256","sequence_count","best_support","best_gates_party_p_q_phase","best_exact_six_marginal_check","limitations")}
    json.dump(summary, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
