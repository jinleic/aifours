#!/usr/bin/env python3
"""Exact integer critical-pair certificate for the seven published TriDend rules.

No third-party dependencies. All leaves remain symbolic and ordered. The finite
certificate is load-bearing only together with proof.md's order and overlap
exhaustion arguments; finite dimension counts are not a confluence proof.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from functools import lru_cache
from itertools import product
import hashlib
import json
from pathlib import Path

OPS = ("d", "p", "s")  # dot < prec < succ
RANK = {op: i for i, op in enumerate(OPS)}


def node(op, left, right):
    return (op, left, right)


def freeze(t):
    return t if isinstance(t, int) else tuple([t[0], freeze(t[1]), freeze(t[2])])


def plus(terms):
    out = defaultdict(int)
    for c, t in terms:
        out[t] += c
    return {t: c for t, c in out.items() if c}


def root_rule(t, dot_sign=1):
    if isinstance(t, int) or isinstance(t[1], int):
        return None
    outer, (inner, a, b), c = t
    right = lambda x, y: node(x, a, node(y, b, c))
    if outer == "p":
        if inner == "p":
            return [(1, right("p", x)) for x in OPS]
        return [(1, right(inner, "p"))]
    if outer == "d":
        if inner == "p":
            return [(1, right("d", "s"))]
        return [(dot_sign if inner == "d" else 1, right(inner, "d"))]
    if outer == "s" and inner == "s":
        return [(1, right("s", "s")),
                (-1, node("s", node("p", a, b), c)),
                (-1, node("s", node("d", a, b), c))]
    return None


def paths(t):
    if isinstance(t, int):
        return ((),)
    op, left, right = t
    return tuple((RANK[op],) + w for u in (left, right) for w in paths(u))


def order_key(t):
    ps = paths(t)
    return (len(ps), tuple((len(w), w) for w in ps))


def redexes(t, path=()):
    if isinstance(t, int):
        return []
    here = [path] if root_rule(t) is not None else []
    return here + redexes(t[1], path + (1,)) + redexes(t[2], path + (2,))


def contract(t, path, dot_sign=1):
    if not path:
        ans = root_rule(t, dot_sign)
        if ans is None:
            raise ValueError("not a redex")
        return ans
    side, *rest = path
    if isinstance(t, int) or side not in (1, 2):
        raise ValueError("invalid path")
    return [(c, node(t[0], u, t[2]) if side == 1 else node(t[0], t[1], u))
            for c, u in contract(t[side], rest, dot_sign)]


def serialize(poly):
    return [[c, t] for t, c in sorted(poly.items(), key=lambda tc: order_key(tc[0]))]


def deserialize(poly):
    return plus((c, freeze(t)) for c, t in poly)


def normal_form(poly, dot_sign=1):
    poly = dict(poly)
    trace = []
    while True:
        candidates = [(t, redexes(t)) for t in poly if redexes(t)]
        if not candidates:
            return poly, trace
        t, positions = max(candidates, key=lambda tp: order_key(tp[0]))
        pos = positions[0]
        coeff = poly.pop(t)
        replacements = contract(t, pos, dot_sign)
        assert all(order_key(u) < order_key(t) for _, u in replacements)
        trace.append({"term": t, "path": pos, "coefficient": coeff})
        poly = plus(list((c, u) for u, c in poly.items()) +
                    [(coeff * c, u) for c, u in replacements])


@lru_cache(None)
def trees(n, first=0):
    if n == 1:
        return (first,)
    return tuple(node(op, left, right)
                 for k in range(1, n)
                 for left in trees(k, first)
                 for right in trees(n-k, first+k)
                 for op in OPS)


def symbolic(t):
    if isinstance(t, int):
        return "abcd"[t] if t < 4 else f"x{t}"
    return f"({symbolic(t[1])} {t[0].upper()} {symbolic(t[2])})"


def symbolic_poly(p):
    parts = []
    for t, c in sorted(p.items(), key=lambda tc: order_key(tc[0]), reverse=True):
        mag = "" if abs(c) == 1 else f"{abs(c)}*"
        parts.append(("+" if c > 0 else "-") + mag + symbolic(t))
    return " ".join(parts).removeprefix("+") or "0"


def build_certificate():
    cert = []
    for t in trees(4):
        positions = redexes(t)
        if len(positions) < 2:
            continue
        assert positions == [(), (1,)]
        branches = []
        for pos in positions:
            start = plus(contract(t, pos))
            final, steps = normal_form(start)
            branches.append({"first_path": pos, "start": serialize(start),
                             "steps": steps, "final": serialize(final)})
        assert deserialize(branches[0]["final"]) == deserialize(branches[1]["final"])
        cert.append({"name": t[0]+t[1][0]+t[1][1][0], "tree": t,
                     "branches": branches})
    assert len(cert) == 15
    return cert


def replay_certificate(cert):
    expected = {t for t in trees(4) if len(redexes(t)) == 2}
    actual = [freeze(row["tree"]) for row in cert]
    assert len(actual) == len(set(actual)) == 15
    assert set(actual) == expected
    step_count = 0
    for row in cert:
        t = freeze(row["tree"])
        finals = []
        assert [tuple(b["first_path"]) for b in row["branches"]] == [(), (1,)]
        for branch in row["branches"]:
            state = plus(contract(t, branch["first_path"]))
            assert state == deserialize(branch["start"])
            for step in branch["steps"]:
                term = freeze(step["term"])
                coeff = step["coefficient"]
                assert coeff != 0 and state.get(term) == coeff
                repl = contract(term, step["path"])
                assert all(order_key(u) < order_key(term) for _, u in repl)
                state.pop(term)
                state = plus(list((c, u) for u, c in state.items()) +
                             [(coeff*c, u) for c, u in repl])
                step_count += 1
            assert state == deserialize(branch["final"])
            assert all(not redexes(u) for u in state)
            finals.append(state)
        assert finals[0] == finals[1]
    return step_count


def mutation_controls(cert):
    altered = json.loads(json.dumps(cert))
    altered[0]["branches"][0]["steps"][0]["coefficient"] += 1
    try:
        replay_certificate(altered)
    except AssertionError:
        rejected = True
    else:
        rejected = False
    assert rejected
    broken = []
    for row in cert:
        t = freeze(row["tree"])
        a, _ = normal_form(plus(contract(t, (), -1)), -1)
        b, _ = normal_form(plus(contract(t, (1,), -1)), -1)
        if a != b:
            broken.append(row["name"])
    assert broken
    return {"corrupted_coefficient_rejected": rejected,
            "negative_dot_associativity_nonjoining_peaks": sorted(broken)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--replay", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    cert = json.loads(args.replay.read_text()) if args.replay else build_certificate()
    steps = replay_certificate(cert)
    controls = mutation_controls(cert)
    counts = [sum(not redexes(t) for t in trees(n)) for n in range(1, 7)]
    assert counts == [1, 3, 11, 45, 197, 903]
    payload = json.dumps(cert, indent=2) + "\n"
    (args.output / "critical-pairs.json").write_text(payload)
    table = []
    for row in sorted(cert, key=lambda x: x["name"]):
        final = deserialize(row["branches"][0]["final"])
        table.append(f"{row['name'].upper()}\t{symbolic(freeze(row['tree']))}\t"
                     f"{symbolic_poly(final)}\t"
                     f"{len(row['branches'][0]['steps'])}/{len(row['branches'][1]['steps'])}")
    (args.output / "critical-pairs.tsv").write_text("top-middle-bottom\tpeak\tcommon normal form\tsteps after first reduction\n" +
                                                  "\n".join(table) + "\n")
    receipt = {"status": "PASS", "coefficient_ring": "Z", "critical_peaks": 15,
               "trace_steps_after_first_reductions": steps,
               "irreducible_counts_arities_1_to_6": counts,
               "controls": controls,
               "certificate_sha256": hashlib.sha256(payload.encode()).hexdigest(),
               "all_arity_argument": "proof.md: admissible order, exhaustive overlap classification, linear diamond induction",
               "scope": "All symbolic minimal overlaps; counts only corroborative"}
    (args.output / "certificate-receipt.json").write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
