#!/usr/bin/env python3
"""README B2-direct: FDGDD/RDGDD(3,4,5{m}) under regular Gamma=Z5 x H, with O(m^3) orbit construction
instead of canonicalizing all subsets of 5m points. H is a regular group of order m; coordinate names are
those in pipeline_s.coord_gens. Quad orbit representatives have groups0,1,2,3 and coordinate0 at group0
(unique since Z5 rotates the missing group to4 and a left translation normalizes the first coordinate).
Triple orbit representatives have group patterns012 or013, coordinate0 at group0: exactly2m^2 columns.
Every triple/quad orbit is free for this direct-product action. The coupled frame/resolution model is the
same as B1, but class-order symmetry breaking uses prefix OR variables: if the i-th anchor triple is put
in class j>0, a smaller anchor triple must be in class j-1. This replaces quadratic pairwise ordering by
O(number_of_anchor_triples * number_of_classes) clauses. Prefix ordering is sound because every class has
exactly one anchor triple. Output is Format D; all actual point frames are transported by Gamma and later
checked directly. No symmetry restriction is part of the target.
Usage: gdd_regular_fast.py FD|RD HNAME M OUTDIR NATIVE_SECONDS SEED [--build-only]
"""
import lane_guard  # noqa: F401
import itertools
import json
import os
import resource
import subprocess
import sys
import time
from collections import defaultdict
from lane_guard import fresh_dir, xopen
from lanelib import CNF, closure, parse_status, model_satisfies
from pipeline_s import coord_gens


def main():
    kind, hname, m, out, tl, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
    build_only = '--build-only' in sys.argv[7:]
    assert kind in ('FD', 'RD') and m % 2 == 0
    fresh_dir(out)
    started = time.perf_counter()
    hp = closure(coord_gens(hname, m), m)
    assert len(hp) == m and len({p[0] for p in hp}) == m, 'H action is not regular'
    byzero = {p[0]: p for p in hp}
    mul = [byzero[a] for a in range(m)]
    inv = [next(b for b in range(m) if mul[a][b] == 0) for a in range(m)]

    def action(gamma, p):
        k, h = gamma
        return m * ((p // m + k) % 5) + mul[h][p % m]

    def canonical(T):
        candidates = []
        for k in range(5):
            rotated = sorted((m * ((p // m + k) % 5) + p % m) for p in T)
            h = inv[rotated[0] % m]
            candidates.append(tuple(m * (p // m) + mul[h][p % m] for p in rotated))
        return min(candidates)

    cols = [(0, m * b + x, m * c + y) for b, c in ((1, 2), (1, 3)) for x in range(m) for y in range(m)]
    cols.sort()
    assert len(set(cols)) == 2 * m * m
    cidx = {T: i for i, T in enumerate(cols)}
    rows = []
    for a, b, c in itertools.product(range(m), repeat=3):
        Q = (0, m + a, 2 * m + b, 3 * m + c)
        cs = [cidx[canonical(T)] for T in itertools.combinations(Q, 3)]
        if len(set(cs)) == 4:
            rows.append((Q, cs))
    gamma = [(k, h) for k in range(5) for h in range(m)]
    cnf = CNF()
    yvars = [cnf.var() for _ in rows]
    colvars = defaultdict(list)
    for ri, (_, cs) in enumerate(rows):
        for c in cs:
            colvars[c].append(yvars[ri])
    for c in range(len(cols)):
        cnf.exactly_one(colvars[c])
    potential = {}
    for ri, (Q, _) in enumerate(rows):
        for p in Q:
            e = ((-(p // m)) % 5, inv[p % m])
            image = sorted(action(e, q) for q in Q)
            assert image[0] == 0
            T = tuple(q for q in image if q != 0)
            assert T not in potential or potential[T] == ri
            potential[T] = ri
    missing = {T: (set(range(1, 5)) - {p // m for p in T}).pop() for T in potential}
    nclass = m // 2 if kind == 'FD' else 3 * m // 2
    z = {}
    for T, ri in potential.items():
        lits = []
        for j in range(nclass):
            var = cnf.var()
            z[(T, j)] = var
            lits.append(var)
            cnf.add([-var, yvars[ri]])
        cnf.add([-yvars[ri]] + lits)
        cnf.amo(lits)
    families = [(y, [p for p in range(m, 5*m) if p // m != y]) for y in range(1,5)] if kind == 'FD' else [(0, list(range(m,5*m)))]
    pointvars = defaultdict(list)
    for (T, j), var in z.items():
        family = missing[T] if kind == 'FD' else 0
        for p in T:
            pointvars[(family,j,p)].append(var)
    for family, points in families:
        for j in range(nclass):
            for p in points:
                cnf.exactly_one(pointvars[(family,j,p)])
    nsb = 0
    for family, points in families:
        anchor = min(points)
        Ts = sorted(T for T in potential if anchor in T and (kind == 'RD' or missing[T] == family))
        before = [None] * nclass
        for T in Ts:
            for j in range(1, nclass):
                cnf.add([-z[(T,j)], before[j-1]] if before[j-1] is not None else [-z[(T,j)]])
                nsb += 1
            after = []
            for j in range(nclass):
                var = cnf.var()
                zi = z[(T,j)]
                if before[j] is None:
                    cnf.add([-var, zi]); cnf.add([var, -zi]); nsb += 2
                else:
                    cnf.add([-before[j], var]); cnf.add([-zi, var]); cnf.add([-var, before[j], zi]); nsb += 3
                after.append(var)
            before = after
    path = os.path.join(out, 'model.cnf')
    sha = cnf.write(path)
    rec = {'kind':kind, 'H':hname, 'm':m, 'group_order':5*m, 'columns':len(cols), 'rows':len(rows),
           'potential_derived_triples':len(potential), 'vars':cnf.nv, 'clauses':len(cnf.clauses),
           'prefix_symbreak_clauses':nsb, 'cnf_sha256':sha, 'seed':seed,
           'build_seconds':time.perf_counter()-started, 'build_peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with xopen(os.path.join(out,'model-info.json')) as fh:
        json.dump(rec,fh,indent=1)
    print(json.dumps({'stage':'built',**rec}),flush=True)
    if build_only:
        return
    solve_started = time.perf_counter()
    run = subprocess.run(['kissat','-q',f'--time={tl}',f'--seed={seed}',path], capture_output=True,text=True)
    with xopen(path+'.log') as fh:
        fh.write(run.stdout+'\n--stderr--\n'+run.stderr)
    status, model = parse_status(run.stdout)
    rec.update({'status':status, 'solve_seconds':time.perf_counter()-solve_started,
                'solver_peak_rss_bytes':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss})
    if status == 'SAT':
        assert model_satisfies(path,model), 'SAT model fails direct DIMACS replay'
        selected = [Q for ri,(Q,_) in enumerate(rows) if yvars[ri] in model]
        blocks = sorted({tuple(sorted(action(e,p) for p in Q)) for e in gamma for Q in selected})
        classes = [(family,[T for T in potential if (kind=='RD' or missing[T]==family) and z[(T,j)] in model])
                   for family,_ in families for j in range(nclass)]
        L = [f'GDD34 {kind}GDD 5 {m}','GROUPS']+[' '.join(str(m*i+a) for a in range(m)) for i in range(5)]+['BLOCKS']
        L += [' '.join(map(str,Q)) for Q in blocks]
        for e in gamma:
            x = action(e,0)
            L.append(f'POINT {x}')
            for ci,(family,C) in enumerate(classes):
                label = (family+e[0])%5 if kind=='FD' else ci
                L.append(f"{'FRAME' if kind=='FD' else 'PC'} {label}")
                L += [' '.join(map(str,T)) for T in sorted(tuple(sorted(action(e,p) for p in T)) for T in C)]
        text = '\n'.join(L)+'\n'
        cert = os.path.join(out,f'{kind.lower()}gdd_5_{m}_candidate.txt')
        with xopen(cert) as fh:
            fh.write(text)
        import hashlib
        rec.update({'certificate':cert,'sha256':hashlib.sha256(text.encode()).hexdigest(),'blocks':len(blocks)})
    with xopen(os.path.join(out,'summary.json')) as fh:
        json.dump(rec,fh,indent=1)
    print(json.dumps(rec),flush=True)


if __name__=='__main__':
    main()
