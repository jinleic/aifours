#!/usr/bin/env python3
"""Append safe residual-symmetry lex leaders; see AMENDMENT-3.r1.md.

Commands: controls OUT.json; make A|B C311|C321|C411 OUT.cnf OUT.json.
No solver is launched. Original base and cube CNFs are untouched.
"""
import argparse
import datetime
import hashlib
import itertools
import json
import os

import k3_cubes

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def generators(cube):
    out = [{"rows": [i, i + 1]} for i in range(2, 6)]
    out.extend({"columns": [i, i + 1]} for i in (1, 2))
    if cube == "C311":
        out.append({"columns": [4, 5], "squares": [2, 3]})
    elif cube == "C321":
        out.append({"columns": [4, 5]})
    else:
        out.extend(({"columns": [3, 4]}, {"columns": [5, 6], "squares": [2, 3]}))
    return out


def swap(x, pair):
    if not pair or x not in pair:
        return x
    return pair[1] if x == pair[0] else pair[0]


def image(vmap, gen):
    result = {}
    for (a, p, q), v in vmap.items():
        a2 = swap(a, gen.get("squares"))
        p2 = (swap(p[0], gen.get("rows")), swap(p[1], gen.get("columns")))
        q2 = (swap(q[0], gen.get("rows")), swap(q[1], gen.get("columns")))
        result[v] = vmap[(a2, min(p2, q2), max(p2, q2))]
    assert set(result) == set(result.values()) == set(range(1, 2647))
    return result


def lex_clauses(pairs, nv):
    clauses, prefix = [], None
    pairs = [(x, y) for x, y in pairs if x != y]
    for i, (x, y) in enumerate(pairs):
        guard = [-prefix] if prefix is not None else []
        clauses.append(guard + [-x, y])
        if i + 1 == len(pairs):
            continue
        nv += 1
        next_prefix = nv
        # If the previous prefix and the next pair are equal, equality of
        # the extended prefix must be true. No reverse implication is needed.
        clauses.append(guard + [-x, -y, next_prefix])
        clauses.append(guard + [x, y, next_prefix])
        prefix = next_prefix
    return nv, clauses


def controls():
    comparisons = 0
    for n in range(1, 5):
        pairs = [(i + 1, n + i + 1) for i in range(n)]
        nv, clauses = lex_clauses(pairs, 2 * n)
        for xs in itertools.product((False, True), repeat=n):
            for ys in itertools.product((False, True), repeat=n):
                exists = False
                for aux in itertools.product((False, True), repeat=nv - 2 * n):
                    values = (None,) + xs + ys + aux
                    if all(any(values[abs(lit)] == (lit > 0) for lit in cl) for cl in clauses):
                        exists = True
                        break
                assert exists == (xs <= ys), (n, xs, ys)
                comparisons += 1
    vmap = k3_cubes.variable_map()
    info = {}
    for cube in k3_cubes.CUBES:
        clauses, units, _ = k3_cubes.cube_clauses(vmap, cube)
        unit_set = {cl[0] for cl in clauses[:units]}
        records = []
        for gen in generators(cube):
            perm = image(vmap, gen)
            moved_units = {perm[abs(lit)] * (1 if lit > 0 else -1) for lit in unit_set}
            assert moved_units == unit_set, (cube, gen)
            records.append({"generator": gen, "moved_predicates": sum(v != w for v, w in perm.items()),
                            "predicate_bijection": True, "signed_cube_units_preserved": True})
        info[cube] = records
    return {"status": "PASS", "truth_table_comparisons": comparisons, "max_comparator_length": 4,
            "all_auxiliary_choices_considered_for_existence": True, "generators": info,
            "wrapper_sha256": sha(__file__),
            "recorded_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds")}


def make(encoder, cube, out, metadata):
    for path in (out, metadata):
        if os.path.exists(path):
            raise FileExistsError(path)
    control = controls()
    source = os.path.join(LANE, "explore", "k3cubes", encoder + "_" + cube + ".cnf")
    with open(source) as f:
        header, body = f.read().split("\n", 1)
    _, kind, old_nv, old_nc = header.split()
    assert kind == "cnf"
    nv, extra, records = int(old_nv), [], []
    vmap = k3_cubes.variable_map()
    for gen in generators(cube):
        perm = image(vmap, gen)
        nv, clauses = lex_clauses(sorted(perm.items()), nv)
        extra.extend(clauses)
        records.append({"generator": gen, "clauses": len(clauses)})
    with open(out, "x") as f:
        f.write("p cnf %d %d\n" % (nv, int(old_nc) + len(extra)))
        f.write(body)
        for cl in extra:
            f.write(" ".join(map(str, cl)) + " 0\n")
    meta = {"encoder": encoder, "cube": cube, "source_cube_cnf_sha256": sha(source),
            "cnf_sha256": sha(out), "wrapper_sha256": sha(__file__),
            "cube_wrapper_sha256": sha(os.path.join(HERE, "k3_cubes.py")),
            "generators": records, "new_auxiliaries": nv - int(old_nv),
            "extra_clauses": len(extra), "finite_controls_status": control["status"]}
    with open(metadata, "x") as f:
        json.dump(meta, f, indent=2)
        f.write("\n")
    print(json.dumps(meta))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)
    ctl = sub.add_parser("controls")
    ctl.add_argument("out")
    mk = sub.add_parser("make")
    mk.add_argument("encoder", choices=("A", "B"))
    mk.add_argument("cube", choices=tuple(k3_cubes.CUBES))
    mk.add_argument("out")
    mk.add_argument("metadata")
    a = ap.parse_args()
    if a.command == "controls":
        with open(a.out, "x") as f:
            json.dump(controls(), f, indent=2)
            f.write("\n")
        print("PASS: 340 exhaustive comparator truth tables and 22 stabilizing predicate permutations")
    else:
        make(a.encoder, a.cube, a.out, a.metadata)


if __name__ == "__main__":
    main()
