#!/usr/bin/env python3
"""k3_cuts_r1.py: generator and controls for the AMENDMENT-4.r1 draft cut family (NOT FROZEN, INACTIVE).

Emits, for every own row/column frame (14), every off-frame point p (42) and the 6 structurally available frame
cells (all frame cells except the one sharing p's other line):
  at-most-three: for each square x and 4-subset R of the 6 cells, OR_{r in R} NOT g_x(p,r)        (26460)
  mixed: for each ordered x != y, 3-subset R, disjoint 2-subset T: OR_R NOT g_x(p,r) OR OR_T NOT g_y(p,t)  (211680)
No auxiliary variables. Literals use each encoder's own map: encoder A's map from gram_enc.build at run time,
encoder B's map decoded at run time through B's own --fix-json branch (as in the B-map oracle). The clause block is
serialised canonically and SHA-bound; it is NOT written to disk. No solver is run.

Controls (each designed to fail on a wrong family):
 (a) exact counts, distinctness, literal validity, and an independent shape characterisation of every clause;
 (b) C1 local coverage on an independently built specification, equality of the emission template with it,
     zero violations on classical triples (weights 1), and an exact predicted violation count for the genuine
     weight-5 square Psi(f) (Ball-Simoens Ex. 15, q=7) placed as each square beside classical squares;
 (c) deliberately mistransported or mutated families must each be caught by at least one check;
 (d) invariance of the emitted set under all 22 AMENDMENT-3 lex generators (and transposition), with a
     non-vacuity control;
 (e) A and B emissions agree under their maps, with a non-vacuity control.
Usage: /usr/bin/python3 -B k3_cuts_r1.py OUT.json
"""
import collections
import datetime
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time

import gram_enc
import k3_cubes
import k3_lex

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
ENC_B = os.path.join(HERE, "gram_encB.py")
N = 7
NG = 2646
PTS = [(r, c) for r in range(N) for c in range(N)]
FRAMES = [("row", k) for k in range(N)] + [("col", k) for k in range(N)]
SQUARES = (1, 2, 3)
GATE = 12200000000
GROWTH = 1048576
EXPECTED = {"at_most_three": 26460, "mixed": 211680, "total": 238140}


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def frame_cells(frame):
    kind, k = frame
    return [(k, c) for c in range(N)] if kind == "row" else [(r, k) for r in range(N)]


def positions(frame, p):
    kind, k = frame
    if kind == "row":
        return [(k, c) for c in range(N) if c != p[1]]
    return [(r, k) for r in range(N) if r != p[0]]


def off_points(frame):
    on = set(frame_cells(frame))
    return [q for q in PTS if q not in on]


def template():
    out = []
    for x in SQUARES:
        for R in itertools.combinations(range(6), 4):
            out.append(((x, R),))
    for x, y in itertools.permutations(SQUARES, 2):
        for R in itertools.combinations(range(6), 3):
            rest = [i for i in range(6) if i not in R]
            for T in itertools.combinations(rest, 2):
                out.append(((x, R), (y, T)))
    return out


def emit(lit_map, positions_fn=positions):
    tpl = template()
    clauses = []
    for frame in FRAMES:
        for p in off_points(frame):
            pos = positions_fn(frame, p)
            for clause in tpl:
                lits = []
                for x, idxs in clause:
                    for i in idxs:
                        r = pos[i]
                        lits.append(-lit_map[(x, min(p, r), max(p, r))])
                clauses.append(tuple(lits))
    return clauses


def serialise_sha(clauses):
    h = hashlib.sha256()
    for c in clauses:
        h.update((" ".join(map(str, c)) + " 0\n").encode())
    return h.hexdigest()


def shape_report(clauses, inv):
    """Independent characterisation of the family; returns a dict of failure counts."""
    groups = collections.defaultdict(lambda: [set(), set()])
    bad_literal = bad_shape = duplicates = 0
    for c in clauses:
        if any(l >= 0 for l in c) or len(set(c)) != len(c) or any(-l not in inv for l in c):
            bad_literal += 1
            continue
        pairs = [inv[-l] for l in c]
        common = {pairs[0][1], pairs[0][2]}
        for _, a, b in pairs[1:]:
            common &= {a, b}
        if len(common) != 1:
            bad_shape += 1
            continue
        p = common.pop()
        others = [b if a == p else a for _, a, b in pairs]
        sqs = [s for s, _, _ in pairs]
        rows = {o[0] for o in others}
        cols = {o[1] for o in others}
        if len(rows) == 1 and p[0] not in rows:
            frame = ("row", next(iter(rows)))
            excluded = (frame[1], p[1])
        elif len(cols) == 1 and p[1] not in cols:
            frame = ("col", next(iter(cols)))
            excluded = (p[0], frame[1])
        else:
            bad_shape += 1
            continue
        if excluded in others or len(set(others)) != len(others):
            bad_shape += 1
            continue
        g = groups[(frame, p)]
        if len(c) == 4 and len(set(sqs)) == 1:
            key = (sqs[0], frozenset(others))
            target = g[0]
        elif len(c) == 5 and len(set(sqs)) == 2 and sorted(collections.Counter(sqs).values()) == [2, 3]:
            cnt = collections.Counter(sqs)
            x = next(s for s in cnt if cnt[s] == 3)
            y = next(s for s in cnt if cnt[s] == 2)
            key = (x, frozenset(o for o, s in zip(others, sqs) if s == x),
                   y, frozenset(o for o, s in zip(others, sqs) if s == y))
            target = g[1]
        else:
            bad_shape += 1
            continue
        if key in target:
            duplicates += 1
        target.add(key)
    wrong_groups = sum(1 for g in groups.values() if len(g[0]) != 45 or len(g[1]) != 360)
    return {"clauses": len(clauses), "bad_literal": bad_literal, "bad_shape": bad_shape,
            "duplicates": duplicates, "groups": len(groups), "groups_not_45_360": wrong_groups,
            "ok": (len(clauses) == EXPECTED["total"] and bad_literal == 0 and bad_shape == 0 and duplicates == 0
                   and len(groups) == 588 and wrong_groups == 0)}


def distinct_ok(clauses):
    return len({frozenset(c) for c in clauses}) == len(clauses) == EXPECTED["total"]


def spec_family():
    """Specification of the per-point family built independently of template(): returns a set of clauses on
    abstract positions, each clause a frozenset of (square, position)."""
    fam = set()
    for x in SQUARES:
        for R in itertools.combinations(range(6), 4):
            fam.add(frozenset((x, i) for i in R))
    for x in SQUARES:
        for y in SQUARES:
            if x == y:
                continue
            for R in itertools.combinations(range(6), 3):
                for T in itertools.combinations(range(6), 2):
                    if set(R) & set(T):
                        continue
                    fam.add(frozenset([(x, i) for i in R] + [(y, i) for i in T]))
    return fam


def local_coverage(fam):
    """C1: over all assignments of 6 positions to {unused,1,2,3} with every square nonempty, the family rejects
    exactly the assignments containing a (4,1,1) or (3,2,1) pattern."""
    total = mismatches = rejected = 0
    for labels in itertools.product(range(4), repeat=6):
        w = [labels.count(s) for s in SQUARES]
        if min(w) == 0:
            continue
        total += 1
        true = {(labels[i], i) for i in range(6) if labels[i]}
        rej = any(cl <= true for cl in fam)
        forbidden = max(w) >= 4 or any(w[a] >= 3 and w[b] >= 2 for a in range(3) for b in range(3) if a != b)
        rejected += rej
        mismatches += rej != forbidden
    return {"assignments": total, "rejected": rejected, "mismatches": mismatches, "ok": total == 2100 and mismatches == 0}


def psi_gram():
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(N)]
    perm = lambda seq: len({v % N for v in seq}) == N
    m0 = next(m for m in range(N) if perm([f0[x] - m * x for x in range(N)]))
    f = [(f0[x] - m0 * x) % N for x in range(N)]
    return lambda p, q: not perm([(q[0] - p[0]) * f[x] + (q[1] - p[1]) * x for x in range(N)])


def classical_gram(slope):
    return lambda p, q: (slope * p[0] + p[1]) % N == (slope * q[0] + q[1]) % N


def violations(clauses, inv, grams):
    val = [False] * (NG + 1)
    for v, (s, a, b) in inv.items():
        val[v] = bool(grams[s](a, b))
    amt = mixed = 0
    for c in clauses:
        if all(val[-l] for l in c):
            if len(c) == 4:
                amt += 1
            else:
                mixed += 1
    return amt, mixed


def run_b(fix):
    cmd = ["/usr/bin/python3", "-B", ENC_B, "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout",
           "--fix-json", "/dev/stdin"]
    r = subprocess.run(cmd, input=json.dumps(fix).encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise RuntimeError("encoder B failed: rc %d" % r.returncode)
    lines = r.stdout.splitlines()
    if not lines[-1].startswith(b"vars "):
        raise RuntimeError("unexpected encoder B output")
    units = {}
    for line in lines[-1 - NG:-1]:
        toks = line.split()
        lit = int(toks[0])
        if len(toks) != 2 or toks[1] != b"0" or not 1 <= abs(lit) <= NG or abs(lit) in units:
            raise RuntimeError("unexpected appended unit")
        units[abs(lit)] = lit > 0
    if len(units) != NG:
        raise RuntimeError("missing appended units")
    return units


def decode_b_map(amap):
    """Encoder B's literal map, decoded through B's own --fix-json branch: B variable v carries the pair whose A
    index has the bits of v's unit signs over 12 designs."""
    by_index = {v: key for key, v in amap.items()}
    codes = {v: 0 for v in range(1, NG + 1)}
    for b in range(12):
        fix = {"g1": [], "g2": [], "g3": []}
        for (a, p, q), v in sorted(amap.items(), key=lambda item: item[1]):
            if (v >> b) & 1:
                fix["g%d" % a].append([list(p), list(q)])
        for v, positive in run_b(fix).items():
            if positive:
                codes[v] |= 1 << b
    if sorted(codes.values()) != list(range(1, NG + 1)):
        raise RuntimeError("decoded B codes are not a permutation of 1..2646")
    return {by_index[code]: v for v, code in codes.items()}


def main(out):
    if os.path.exists(out):
        raise FileExistsError(out)
    t0 = time.monotonic()
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    gate = {"at": now(), "available_bytes": available, "threshold_bytes": GATE, "projected_growth_bytes": GROWTH}
    if available < GATE + GROWTH:
        gate["status"] = "UNKNOWN / DEFERRED_RESOURCE; generator not run"
        with open(out, "x") as f:
            json.dump({"status": "DEFERRED", "gate": gate}, f, indent=2)
            f.write("\n")
        print(json.dumps(gate))
        return
    gate["status"] = "PASS"
    rec = {"started_at": now(), "gate": gate, "generator_sha256": sha_file(os.path.abspath(__file__)),
           "encoder_A_sha256": sha_file(os.path.join(HERE, "gram_enc.py")), "encoder_B_sha256": sha_file(ENC_B),
           "cube_wrapper_sha256": sha_file(os.path.join(HERE, "k3_cubes.py")),
           "lex_wrapper_sha256": sha_file(os.path.join(HERE, "k3_lex.py")),
           "draft": {"path": "review/drafts/AMENDMENT-4.r1.md",
                     "sha256": sha_file(os.path.join(LANE, "review", "drafts", "AMENDMENT-4.r1.md"))},
           "bmap_oracle_receipt_sha256": sha_file(os.path.join(LANE, "evidence", "k3cubes", "bmap_oracle_r1.json")),
           "status_note": "Draft family only; NOT FROZEN, INACTIVE; no solve run; clause block not written"}
    failures = []

    F, amap_str = gram_enc.build(3, None, True, True, None)
    del F
    amap = {}
    for key, v in amap_str.items():
        a, p, q = key.split("|")
        amap[(int(a), tuple(map(int, p.split(","))), tuple(map(int, q.split(","))))] = v
    if amap != k3_cubes.variable_map():
        failures.append("A map differs from the cube wrapper map")
    inv = {v: key for key, v in amap.items()}

    clauses_a = emit(amap)
    counts = {"at_most_three": sum(1 for c in clauses_a if len(c) == 4),
              "mixed": sum(1 for c in clauses_a if len(c) == 5), "total": len(clauses_a)}
    rec["counts"] = counts
    rec["block_sha256_A"] = serialise_sha(clauses_a)
    rec["block_bytes_A"] = sum(len(" ".join(map(str, c))) + 3 for c in clauses_a)
    rec["block_header"] = {"variables_referenced_max": max(-l for c in clauses_a for l in c), "clauses": len(clauses_a),
                           "append_rule": "nv unchanged; nc += 238140; all literals negative g variables"}
    if counts != EXPECTED:
        failures.append("counts %r differ from %r" % (counts, EXPECTED))

    # (a)
    shape = shape_report(clauses_a, inv)
    rec["control_a"] = {"shape": shape, "distinct": distinct_ok(clauses_a)}
    if not (shape["ok"] and rec["control_a"]["distinct"]):
        failures.append("control (a) failed")

    # (b)
    spec = spec_family()
    tpl_set = {frozenset((x, i) for x, idxs in cl for i in idxs) for cl in template()}
    c1 = local_coverage(spec)
    classical = {}
    for slopes in ((1, 2, 3), (1, 2, 4), (2, 3, 5), (4, 5, 6), (1, 3, 6)):
        grams = {s: classical_gram(m) for s, m in zip(SQUARES, slopes)}
        classical["slopes_%d%d%d" % slopes] = violations(clauses_a, inv, grams)
    genuine = {}
    for x in SQUARES:
        others = [s for s in SQUARES if s != x]
        grams = {x: psi_gram(), others[0]: classical_gram(4), others[1]: classical_gram(2)}
        genuine["psi_as_square_%d" % x] = violations(clauses_a, inv, grams)
    rec["control_b"] = {
        "spec_size": len(spec), "template_equals_spec": tpl_set == spec, "local_coverage": c1,
        "classical_triples_violations": classical,
        "genuine_weight5_violations": genuine,
        "prediction": "classical triples (weights 1): (0,0); Psi(f) has weight 5 at every frame/point, so exactly "
                      "C(5,4)=5 at-most-three clauses per frame/point for its square: (2940,0)",
        "scope": "Psi(f) with two classical squares is not a K3 triple; the lemma does not apply there, so this is a "
                 "non-vacuity check that the cuts bite, not a claim about K3"}
    ok_b = (len(spec) == 405 and tpl_set == spec and c1["ok"]
            and all(v == (0, 0) for v in classical.values())
            and all(v == (2940, 0) for v in genuine.values()))
    if not ok_b:
        failures.append("control (b) failed")

    # (c) mutations
    def battery(fam):
        rep = shape_report(fam, inv)
        return {"shape_ok": rep["ok"], "distinct_ok": distinct_ok(fam), "count_ok": len(fam) == EXPECTED["total"]}
    mutations = {}
    first_amt = next(i for i, c in enumerate(clauses_a) if len(c) == 4)
    s, a, b = inv[-clauses_a[first_amt][-1]]
    p = next(iter({a, b} & set(inv[-clauses_a[first_amt][0]][1:])))
    r = b if a == p else a
    k2 = next(k for k in range(N) if k not in (r[0], p[0]))
    moved = (k2, r[1])
    m1 = list(clauses_a)
    m1[first_amt] = clauses_a[first_amt][:-1] + (-amap[(s, min(p, moved), max(p, moved))],)
    mutations["cross_frame_literal"] = battery(m1)
    first_mixed = next(i for i, c in enumerate(clauses_a) if len(c) == 5)
    sx = inv[-clauses_a[first_mixed][0]][0]
    merged = []
    for l in clauses_a[first_mixed]:
        _, a2, b2 = inv[-l]
        merged.append(-amap[(sx, a2, b2)])
    m2 = list(clauses_a)
    m2[first_mixed] = tuple(merged)
    mutations["mixed_square_merge"] = battery(m2)
    def frame_kind(c):
        cell = next(iter(set(inv[-c[0]][1:]) & set(inv[-c[1]][1:])))
        others = [b2 if a2 == cell else a2 for _, a2, b2 in (inv[-l] for l in c)]
        return "row" if len({o[0] for o in others}) == 1 else "col"
    rows_only = [c for c in clauses_a if frame_kind(c) == "row"]
    m3 = rows_only + rows_only
    mutations["column_frames_replaced_by_row_frames"] = battery(m3)
    m4 = [c for c in clauses_a if len(c) == 5]
    for frame in FRAMES:
        for pp in off_points(frame):
            pos = positions(frame, pp)
            for x in SQUARES:
                for R in itertools.combinations(range(6), 5):
                    m4.append(tuple(-amap[(x, min(pp, pos[i]), max(pp, pos[i]))] for i in R))
    mutations["at_most_four_instead_of_three"] = battery(m4)
    m5 = clauses_a[1:]
    mutations["one_clause_dropped"] = battery(m5)

    def wrong_positions(frame, pp):
        kind, k = frame
        if kind == "row":
            return [(k, c) for c in range(N) if c != pp[1]]
        return [(r2, k) for r2 in range(N) if r2 != pp[1]]
    try:
        emit(amap, wrong_positions)
        mutations["column_frame_exclusion_mistransported"] = {"emitted": True}
    except KeyError:
        mutations["column_frame_exclusion_mistransported"] = {"emitted": False,
                                                              "detected_by": "literal validity (collinear pair has no variable)"}
    detected = {}
    for name, res in mutations.items():
        detected[name] = (not res.get("emitted", True)) or not all(v for k, v in res.items() if k.endswith("_ok"))
    rec["control_c"] = {"mutations": mutations, "detected": detected}
    if not all(detected.values()):
        failures.append("control (c): an undetected mutation")

    # (d)
    fam = {frozenset(c) for c in clauses_a}
    inv_results = {}
    for cube in ("C311", "C321", "C411"):
        for gen in k3_lex.generators(cube):
            perm = k3_lex.image(amap, gen)
            img = {frozenset(-perm[-l] for l in c) for c in fam}
            inv_results["%s %s" % (cube, json.dumps(gen, sort_keys=True))] = img == fam
    tperm = {}
    for (sq, pa, pb), v in amap.items():
        ta, tb = (pa[1], pa[0]), (pb[1], pb[0])
        tperm[v] = amap[(sq, min(ta, tb), max(ta, tb))]
    transposition_ok = {frozenset(-tperm[-l] for l in c) for c in fam} == fam
    dropped = clauses_a[0]
    reduced = fam - {frozenset(dropped)}
    nonvac = []
    for cube in ("C311", "C321", "C411"):
        for gen in k3_lex.generators(cube):
            perm = k3_lex.image(amap, gen)
            nonvac.append({frozenset(-perm[-l] for l in c) for c in reduced} == reduced)
    rec["control_d"] = {"generators": len(inv_results), "all_invariant": all(inv_results.values()),
                        "transposition_invariant": transposition_ok,
                        "nonvacuity_family_minus_one_clause_invariant_under_all": all(nonvac),
                        "per_generator": inv_results}
    if not (len(inv_results) == 22 and all(inv_results.values()) and transposition_ok and not all(nonvac)):
        failures.append("control (d) failed")

    # (e)
    bmap = decode_b_map(amap)
    clauses_b = emit(bmap)
    rec["block_sha256_B"] = serialise_sha(clauses_b)
    swapped = dict(amap)
    k1 = next(k for k, v in amap.items() if v == 1)
    kn = next(k for k, v in amap.items() if v == NG)
    swapped[k1], swapped[kn] = swapped[kn], swapped[k1]
    rec["control_e"] = {"B_map_equals_A_map": bmap == amap, "block_sha_equal": rec["block_sha256_A"] == rec["block_sha256_B"],
                        "sets_equal": {frozenset(c) for c in clauses_b} == fam,
                        "nonvacuity_swapped_map_sha_differs": serialise_sha(emit(swapped)) != rec["block_sha256_A"],
                        "B_map_source": "decoded at run time through gram_encB.py --fix-json (12 designs)"}
    if not all(v for k, v in rec["control_e"].items() if k != "B_map_source"):
        failures.append("control (e) failed")

    rec.update({"status": "PASS" if not failures else "FAIL", "failures": failures, "finished_at": now(),
                "seconds": round(time.monotonic() - t0, 3), "block_written": False})
    with open(out, "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps({"status": rec["status"], "counts": counts, "block_sha256_A": rec["block_sha256_A"],
                      "seconds": rec["seconds"], "failures": failures}))
    print("receipt_sha256", sha_file(out))


if __name__ == "__main__":
    OUT = sys.argv[1]
    try:
        main(OUT)
    except Exception as exc:
        if not os.path.exists(OUT):
            with open(OUT, "x") as f:
                json.dump({"status": "FAIL", "failures": ["exception: %r" % (exc,)], "finished_at": now(),
                           "generator_sha256": sha_file(os.path.abspath(__file__))}, f, indent=2)
                f.write("\n")
        raise
