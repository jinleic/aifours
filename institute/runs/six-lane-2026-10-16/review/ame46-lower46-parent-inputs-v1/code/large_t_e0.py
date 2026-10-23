#!/usr/bin/env python3
"""large_t_e0.py: structured exclusion of (t, e = 0) for large t (lane ame46-support).

Pipeline (all steps exact; review/LEMMAS gives the lemmas):
 1. Deficit profiles. For each coordinate i the positive deficits d_{i,a} (a in V_i) are parts >= 2 summing to
    h = 36 - t (Lemma 9). Within slice (i,a) coordinate j takes d_{i,a} distinct values of V_j, so
    max_a d_{i,a} <= min_{j != i} |V_j|. Up to coordinate permutation and relabelling, V_i = {6-p_i, ..., 5} with the
    parts assigned in non-increasing order to increasing values.
 2. For each profile, the N-only exact-two CNF on the product space prod V_i (Lemma 11: every hole line has exactly two
    elements; row overlap; hole-line counts per slice equal d_{i,a}; phase families TBL/TWIN restricted to the
    product space) is solved repeatedly. Each solution's whole orbit under the CNF's symmetry group (value
    permutations inside V_i preserving d, and profile-preserving coordinate permutations) is blocked. The final UNSAT
    is proved with CaDiCaL --lrat and checked by code/lratcheck.
 3. Each orbit representative gets the exact 2x2 phase check (phase_check.py). For phase-consistent
    representatives, the classical completion CNF (T avoids every hole line and meets every non-hole line exactly
    once) is solved with CaDiCaL --lrat and checked.
Output: evidence/large_t_e0_t<t>.json plus the CNF/LRAT files under explore/large_t/.
"""
import argparse
import itertools
import json
import os
import subprocess
import sys

import ame_e0_cnf as base
import phase_check as pc

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "explore", "large_t")
PAIRS = base.PAIRS


def partitions(h, lo=2):
    """Non-increasing tuples of parts >= lo summing to h, at most 6 parts."""
    out = []

    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        if len(cur) == 6:
            return
        for p in range(min(rem, mx), lo - 1, -1):
            rec(rem - p, p, cur + [p])
    rec(h, 6, [])
    return out


def profiles(h):
    parts = partitions(h)
    res = []
    for combo in itertools.combinations_with_replacement(range(len(parts)), 4):
        prof = [parts[k] for k in combo]
        ok = all(max(prof[i]) <= min(len(prof[j]) for j in range(4) if j != i) for i in range(4))
        if ok:
            res.append(prof)
    return res


class Small:
    def __init__(self, prof):
        self.prof = prof
        self.V = [list(range(6 - len(p), 6)) for p in prof]
        self.d = [{a: p[k] for k, a in enumerate(self.V[i])} for i, p in enumerate(prof)]
        self.points = list(itertools.product(*self.V))
        self.var = {x: k + 1 for k, x in enumerate(self.points)}
        self.nv = len(self.points)
        self.cl = []

    def new(self):
        self.nv += 1
        return self.nv

    def amk(self, lits, k):
        F = base.CNF()
        F.nv = self.nv
        F.at_most_k(lits, k)
        self.nv = F.nv
        self.cl.extend(F.clauses)

    def eqk(self, lits, k):
        self.amk(lits, k)
        self.amk([-l for l in lits], len(lits) - k)

    def build(self, phase=True):
        V, d = self.V, self.d
        hl = {}
        for (i, j) in PAIRS:
            for a in V[i]:
                for b in V[j]:
                    mem = [x for x in self.points if x[i] == a and x[j] == b]
                    ns = [self.var[x] for x in mem]
                    v = self.new()
                    hl[(i, j, a, b)] = v
                    self.cl.append([-v] + ns)
                    for nx in ns:
                        self.cl.append([-nx, v])
                    for x in mem:
                        self.cl.append([-self.var[x]] + [self.var[y] for y in mem if y != x])
                    self.amk(ns, 2)
        for i in range(4):
            for j in range(4):
                if i == j:
                    continue
                P = (min(i, j), max(i, j))
                for a in V[i]:
                    lits = [hl[(P[0], P[1], a, b) if P[0] == i else (P[0], P[1], b, a)] for b in V[j]]
                    self.eqk(lits, d[i][a])
        for rows, cols in base.RESHAPINGS:
            rv = list(itertools.product(V[rows[0]], V[rows[1]]))
            cv_all = list(itertools.product(V[cols[0]], V[cols[1]]))

            def el(r, c):
                x = [0] * 4
                x[rows[0]], x[rows[1]] = r
                x[cols[0]], x[cols[1]] = c
                return tuple(x)
            for r1, r2 in itertools.combinations(rv, 2):
                aux = {}
                for c in cv_all:
                    a_ = self.new()
                    aux[c] = a_
                    self.cl.append([-a_, self.var[el(r1, c)]])
                    self.cl.append([-a_, self.var[el(r2, c)]])
                for c in cv_all:
                    self.cl.append([-self.var[el(r1, c)], -self.var[el(r2, c)]] + [aux[c2] for c2 in cv_all if c2 != c])
        if phase:
            Vs = [set(v) for v in V]
            for fam in (base.tbl_sets(), base.twin_sets()):
                for s in fam:
                    if all(all(x[i] in Vs[i] for i in range(4)) for x in s):
                        self.cl.append([-self.var[x] for x in s])

    def group(self):
        """Symmetry group of the CNF: (perm of coordinates, value perms) as point maps."""
        sig = [tuple(p) for p in self.prof]
        coord_perms = [pi for pi in itertools.permutations(range(4)) if all(sig[pi[i]] == sig[i] for i in range(4))]
        vperms = []
        for i in range(4):
            classes = {}
            for a in self.V[i]:
                classes.setdefault(self.d[i][a], []).append(a)
            opts = []
            for combo in itertools.product(*[list(itertools.permutations(c)) for c in classes.values()]):
                m = {}
                for c, img in zip(classes.values(), combo):
                    m.update(dict(zip(c, img)))
                opts.append(m)
            vperms.append(opts)
        maps = []
        for pi in coord_perms:
            for vs in itertools.product(*vperms):
                maps.append((pi, vs))
        return maps

    @staticmethod
    def apply(g, x):
        pi, vs = g
        y = [vs[i][x[i]] for i in range(4)]
        z = [0] * 4
        for i in range(4):
            z[pi[i]] = y[i]
        return tuple(z)

    def write(self, path, extra=()):
        with open(path, "w") as fh:
            fh.write(f"p cnf {self.nv} {len(self.cl) + len(extra)}\n")
            for c in itertools.chain(self.cl, extra):
                fh.write(" ".join(map(str, c)) + " 0\n")


def solve(path, lrat=None):
    cmd = ["cadical", "-q", path] + ([lrat, "--lrat", "--binary=false"] if lrat else [])
    if lrat:
        cmd = ["cadical", "-q", "--lrat", "--binary=false", path, lrat]
    r = subprocess.run(cmd, capture_output=True, text=True)
    status = r.returncode
    model = set()
    for line in r.stdout.splitlines():
        if line.startswith("v "):
            for tok in line.split()[1:]:
                v = int(tok)
                if v > 0:
                    model.add(v)
    return status, model


def lrat_check(cnf, lrat):
    r = subprocess.run([os.path.join(HERE, "lratcheck"), cnf, lrat], capture_output=True, text=True)
    return r.returncode == 0 and "s VERIFIED" in r.stdout, r.stdout.strip().splitlines()[-1] if r.stdout else r.stderr


def completion_cnf(N, path):
    """Classical completion: T avoids hole lines, meets every non-hole line exactly once."""
    holes = {P: {tuple(x[i] for i in P) for x in N} for P in PAIRS}
    allowed = [x for x in itertools.product(range(6), repeat=4)
               if all(tuple(x[i] for i in P) not in holes[P] for P in PAIRS)]
    var = {x: k + 1 for k, x in enumerate(allowed)}
    F = base.CNF()
    F.nv = len(allowed)
    for P in PAIRS:
        for z in itertools.product(range(6), repeat=2):
            if z in holes[P]:
                continue
            lits = [var[x] for x in allowed if tuple(x[i] for i in P) == z]
            if not lits:
                F.add([])
                continue
            F.add(lits)
            F.at_most_k(lits, 1)
    with open(path, "w") as fh:
        fh.write(f"p cnf {F.nv} {len(F.clauses)}\n")
        for c in F.clauses:
            fh.write(" ".join(map(str, c)) + " 0\n")
    return len(allowed)


def run(t, phase_clauses=True):
    h = 36 - t
    os.makedirs(OUT, exist_ok=True)
    suffix = "" if phase_clauses else "_nophase"
    report = {"t": t, "e": 0, "h": h, "phase_clauses_in_cnf": phase_clauses, "profiles": []}
    for prof in profiles(h):
        tag = "t%d%s_" % (t, suffix) + "_".join("-".join(map(str, p)) for p in prof)
        S = Small(prof)
        S.build(phase=phase_clauses)
        G = S.group()
        blocks, reps = [], []
        it = 0
        while True:
            it += 1
            path = os.path.join(OUT, tag + ".cnf")
            S.write(path, blocks)
            st, model = solve(path)
            if st == 20:
                lrat = os.path.join(OUT, tag + ".final.lrat")
                st2, _ = solve(path, lrat)
                ok, msg = lrat_check(path, lrat)
                break
            if st != 10:
                raise RuntimeError("solver status %d" % st)
            N = [x for x in S.points if S.var[x] in model]
            orbit = {frozenset(S.apply(g, x) for x in N) for g in G}
            for img in orbit:
                blocks.append([-S.var[x] for x in sorted(img)])
            reps.append({"N": N, "orbit_size": len(orbit)})
        prof_rep = {"profile": [list(p) for p in prof], "orbits": len(reps), "group_order": len(G),
                    "final_unsat_lrat_verified": ok, "lrat_msg": msg, "reps": []}
        for k, rep in enumerate(reps):
            N = rep["N"]
            eqs = pc.block_equations(set(N))
            elems = sorted({x for _, tt in eqs for x, _ in tt})
            ph = pc.phase_consistency(eqs, elems)
            entry = {"N": ["".join(map(str, x)) for x in N], "orbit_size": rep["orbit_size"],
                     "phase_complex_consistent": ph["complex_consistent"],
                     "phase_obstruction_verified": ph.get("obstruction_verified")}
            if ph["complex_consistent"]:
                cpath = os.path.join(OUT, tag + "_rep%d_completion.cnf" % k)
                nallowed = completion_cnf(N, cpath)
                clrat = cpath.replace(".cnf", ".lrat")
                st, model = solve(cpath, clrat)
                entry["completion_allowed_points"] = nallowed
                entry["completion_status"] = {10: "SAT", 20: "UNSAT"}.get(st, str(st))
                if st == 20:
                    entry["completion_lrat_verified"], entry["completion_lrat_msg"] = lrat_check(cpath, clrat)
            prof_rep["reps"].append(entry)
        report["profiles"].append(prof_rep)
        print(json.dumps({k: v for k, v in prof_rep.items() if k != "reps"}), flush=True)
    excluded = all(p["final_unsat_lrat_verified"] and all(
        (not r["phase_complex_consistent"] and r["phase_obstruction_verified"]) or
        (r.get("completion_status") == "UNSAT" and r.get("completion_lrat_verified")) for r in p["reps"])
        for p in report["profiles"])
    report["t_e0_excluded"] = excluded
    with open(os.path.join(HERE, "..", "evidence", "large_t_e0_t%d%s.json" % (t, suffix)), "w") as fh:
        json.dump(report, fh, indent=1)
    print("t=%d e=0 excluded: %s" % (t, excluded))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--no-phase-clauses", action="store_true")
    a = ap.parse_args()
    run(a.t, phase_clauses=not a.no_phase_clauses)
