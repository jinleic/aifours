#!/usr/bin/env python3
"""New matched controls requested by the static Gram reviews; frozen encoders untouched.

Covers heavy+sym and its distinguishing negative, classical-light negatives,
K2-shaped classical data, exact net transport/conjugation, and designed G2/G3/G5
mutants. Independently evaluates the violated families before fixing the complete
Gram support into each CNF. Retains input, CNF, solver output and SHA bindings.
These controls were added after the earlier K2 production runs, not before them.
Usage: gram_review_controls.py OUTDIR
"""
import argparse
import datetime
import hashlib
import itertools
import json
import os
import subprocess
import sys

import gram_enc
from k2_classes import square_from_key

HERE = os.path.dirname(os.path.abspath(__file__))
P = [(i, j) for i in range(7) for j in range(7)]
PAIRS = list(itertools.combinations(P, 2))


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def edges(fn):
    return {frozenset((p, q)) for p, q in PAIRS if fn(p, q)}


def linear(a):
    return edges(lambda p, q: (a * p[0] + p[1]) % 7 == (a * q[0] + q[1]) % 7)


def transform(E, inverse):
    return edges(lambda p, q: frozenset((inverse(p), inverse(q))) in E)


def evaluate(gs, L, heavy, sym):
    lines = [[(i, j) for j in range(7)] for i in range(7)] + [[(i, j) for i in range(7)] for j in range(7)]
    if L is not None:
        assert all(sorted(row) == list(range(7)) for row in L)
        assert all(sorted(L[i][j] for i in range(7)) == list(range(7)) for j in range(7))
        lines += [[p for p in P if L[p[0]][p[1]] == k] for k in range(7)]
    assert not (sym and L is not None)
    failures = set()
    for a, E in enumerate(gs, 1):
        g = lambda p, q: p == q or frozenset((p, q)) in E
        for line in lines:
            assert all(not g(p, q) for p, q in itertools.combinations(line, 2)), ("invalid fixed G1", a)
            off = [p for p in P if p not in line]
            for p, q in itertools.combinations(off, 2):
                n = sum(g(p, r) and g(q, r) for r in line)
                if n == 0 and g(p, q):
                    failures.add("G2_zero")
                if n == 1 and not g(p, q):
                    failures.add("G2_one")
            if heavy and not any(sum(g(p, r) for r in line) >= 3 for p in off):
                failures.add("G4_light")
        for line1, line2 in itertools.permutations(lines, 2):
            for p in line1:
                if p in line2:
                    continue
                ns = [q for q in line2 if q not in line1 and g(p, q)]
                if not ns:
                    failures.add("G3_empty")
                elif len(ns) == 1:
                    q = ns[0]
                    if any(g(r, q) for r in line1 if r != p and r not in line2):
                        failures.add("G3_singleton")
        if sym and a == 1 and not all(g((1, 0), (0, k)) for k in (1, 2, 3)):
            failures.add("SYM_units")
    if any(E & F for E, F in itertools.combinations(gs, 2)):
        failures.add("G5_edge")
    return sorted(failures)


def fixtures():
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(7)]
    perm = lambda seq: len({x % 7 for x in seq}) == 7
    m0 = next(m for m in range(7) if perm([f0[x] - m * x for x in range(7)]))
    f = [(f0[x] - m0 * x) % 7 for x in range(7)]
    Q = edges(lambda p, q: not perm([(q[0] - p[0]) * f[x] + (q[1] - p[1]) * x for x in range(7)]))
    C1, C2, C3, C4 = (linear(a) for a in (1, 2, 3, 4))
    with open(os.path.join(HERE, "..", "evidence", "ls7_main_classes.txt")) as source:
        key = source.readline().split()[0]
    Z = square_from_key(key)
    assert Z == [[(i + j) % 7 for j in range(7)] for i in range(7)]
    swap14 = lambda p: (p[0], {1: 4, 4: 1}.get(p[1], p[1]))
    moved = transform(Q, swap14)
    reduced = transform(Q, lambda p: ((2 * p[0]) % 7, p[1]))   # inverse of old-row -> 4*old-row
    conjugate = transform(reduced, lambda p: ((p[0] - p[1]) % 7, p[1]))
    Lconj = [[(i - j) % 7 for j in range(7)] for i in range(7)]
    add = C1 | {frozenset(((1, 0), (0, 2)))}
    remove = C1 - {frozenset(((1, 0), (0, 1)))}
    conflict_edge = min(C4, key=lambda edge: sorted(edge))
    conflict = Q | {conflict_edge}
    return [
        ("sym_positive", [Q], None, True, True, "SAT", []),
        ("sym_missing_edge", [moved], None, True, True, "UNSAT", ["SYM_units"]),
        ("sym_negative_without_sym", [moved], None, True, False, "SAT", []),
        ("classical_light", [C1], None, False, False, "SAT", []),
        ("classical_heavy_negative", [C1], None, True, False, "UNSAT", ["G4_light"]),
        ("classical_K2_shape", [C2, C3], Z, False, False, "SAT", []),
        ("classical_K2_heavy_negative", [C2, C3], Z, True, False, "UNSAT", ["G4_light"]),
        ("classical_triple_heavy_sym_negative", [C1, C2, C3], None, True, True, "UNSAT", ["G4_light", "SYM_units"]),
        ("psi_transported_to_decoded_Z7", [reduced], Z, True, False, "SAT", []),
        ("psi_conjugate_transport", [conjugate], Lconj, True, False, "SAT", []),
        ("g2_one_and_g3_singleton_mutant", [add], None, False, False, "UNSAT", ["G2_one", "G3_singleton"]),
        ("g3_empty_mutant", [remove], None, False, False, "UNSAT", ["G3_empty"]),
        ("g5_conflicting_edge_mutant", [conflict, C4], None, False, False, "UNSAT", ["G5_edge"]),
    ]


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    pins = {n: sha(os.path.join(HERE, n)) for n in
            ("gram_enc.py", "gram_encB.py", "k2_classes.py", "gram_review_controls.py")}
    records = []
    for name, gs, L, heavy, sym, expected, targets in fixtures():
        failures = evaluate(gs, L, heavy, sym)
        assert (not failures) if expected == "SAT" else set(targets) <= set(failures), (name, failures)
        fix = {"g%d" % a: [sorted(edge) for edge in sorted(E, key=lambda edge: sorted(edge))]
               for a, E in enumerate(gs, 1)}
        fixpath = os.path.join(outdir, name + ".fix.json")
        with open(fixpath, "x") as file:
            json.dump(fix, file)
        Lpath = None
        if L is not None:
            Lpath = os.path.join(outdir, name + ".L.json")
            with open(Lpath, "x") as file:
                json.dump(L, file)
        for encoder in ("A", "B"):
            base = os.path.join(outdir, encoder + "_" + name)
            cnf, logfile = base + ".cnf", base + ".solver.log"
            if os.path.exists(cnf) or os.path.exists(logfile):
                raise FileExistsError(base)
            if encoder == "A":
                F, _ = gram_enc.build(len(gs), L, heavy, sym, fix)
                text = F.text()
                with open(cnf, "x") as file:
                    file.write(text)
            else:
                cmd = ["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"), "--squares", str(len(gs)),
                       "--fix-json", fixpath, "--out", cnf]
                if Lpath:
                    cmd += ["--net-L", Lpath]
                if heavy:
                    cmd += ["--heavy"]
                if sym:
                    cmd += ["--sym"]
                subprocess.run(cmd, check=True, capture_output=True)
                with open(cnf) as file:
                    text = file.read()
            lines = text.splitlines()
            assert "None" not in text and all(line.strip() != "0" for line in lines[1:]), name
            assert int(lines[0].split()[3]) == len(lines) - 1
            command = (["cadical", "-q", "-t", "300", cnf] if encoder == "A"
                       else ["kissat", "-q", "--time=300", cnf])
            with open(logfile, "x") as file:
                result = subprocess.run(command, stdout=file, stderr=subprocess.STDOUT)
            status = {10: "SAT", 20: "UNSAT"}.get(result.returncode, "UNKNOWN")
            rec = {"encoder": encoder, "name": name, "expected": expected, "observed": status,
                   "intended_failures": targets, "independent_family_evaluation": failures,
                   "cnf_sha256": sha(cnf), "fix_sha256": sha(fixpath), "solver_log_sha256": sha(logfile),
                   "solver_rc": result.returncode, "no_None_or_empty_clause": True, "pins": pins}
            with open(base + ".json", "x") as file:
                json.dump(rec, file, indent=2)
                file.write("\n")
            records.append(rec)
            print(json.dumps({k: rec[k] for k in ("encoder", "name", "expected", "observed")}), flush=True)
            assert status == expected, (name, encoder, status)
    summary = {"recorded_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
               "status": "PASS", "cases": len(records), "pins": pins, "records": records,
               "chronology": "New controls after the K2 producer certificates; not represented as preceding those runs"}
    with open(os.path.join(outdir, "summary.json"), "x") as file:
        json.dump(summary, file, indent=2)
        file.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])
