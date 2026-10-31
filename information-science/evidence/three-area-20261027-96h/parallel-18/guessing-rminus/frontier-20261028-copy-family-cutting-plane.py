#!/usr/bin/env python3
"""Bounded conditioned/multiblock copy-inequality separation for R-minus.

Numerical LPs propose bounds only. No objective is a verified inequality until
an independent exact rational dual certificate is constructed and checked.
"""
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import hashlib
import json
import time
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent
spec = spec_from_file_location('copy_family_upper', ROOT / 'frontier-20261028-copy-family-upper-lp.py')
base = module_from_spec(spec)
spec.loader.exec_module(base)
sys.path.insert(0, str(ROOT / 'frontier-20261028-highspy'))
import highspy

OUTPUT = ROOT / 'frontier-20261028-copy-family-cutting-plane-result.json'
MAX_WALL_SECONDS = 90.0
MAX_ROUNDS = 6
MAX_CUTS_PER_ROUND = 1500
PER_SOLVE_SECONDS = 20.0
CUTOFF = -1e-8


def solve(rows, fd, orbit, reps, sample):
    starts, indices, vals, lower, upper, labels = [], [], [], [], [], []
    inf = highspy.kHighsInf
    def add(key,lo,hi,metadata):
        starts.append(len(indices))
        for c,a in key:
            indices.append(c); vals.append(float(a))
        lower.append(lo); upper.append(hi); labels.append((metadata,key))
    for key,metadata in rows.items():
        assert sum(coef*sample[col] for col,coef in key) > -1e-8, metadata
        add(key,0.0,inf,metadata)
    for key,metadata in fd.items():
        assert abs(sum(coef*sample[col] for col,coef in key)) < 1e-8, metadata
        add(key,0.0,0.0,metadata)
    count = len(reps)
    lower_cols = np.zeros(count)
    upper_cols = np.full(count,inf)
    for i in range(base.N):
        upper_cols[orbit[1 << i]] = 1.0
    costs = np.zeros(count); costs[orbit[base.FULL]] = 1.0
    lp = highspy.HighsLp()
    lp.num_col_,lp.num_row_ = count,len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_ = costs,lower_cols,upper_cols
    lp.row_lower_,lp.row_upper_ = np.array(lower),np.array(upper)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(starts+[len(indices)],dtype=np.int32)
    lp.a_matrix_.index_ = np.array(indices,dtype=np.int32)
    lp.a_matrix_.value_ = np.array(vals,dtype=float)
    lp.sense_ = highspy.ObjSense.kMaximize
    solver = highspy.Highs()
    solver.silent()
    solver.setOptionValue('threads',1)
    solver.setOptionValue('time_limit',PER_SOLVE_SECONDS)
    solver.passModel(lp)
    t = time.monotonic(); solver.run(); elapsed = time.monotonic()-t
    status = solver.modelStatusToString(solver.getModelStatus())
    info, sol = solver.getInfo(),solver.getSolution()
    info_result = {'status':status,'objective_float_unverified':float(info.objective_function_value),
                   'rows':len(starts),'columns':count,'nnz':len(indices),'solve_elapsed_s':elapsed}
    if status != 'Optimal':
        return info_result,None
    info_result['row_duals_nonzero_float'] = [
        {'meta':metadata,'row':key,'dual':float(dual)}
        for (metadata,key),dual in zip(labels,sol.row_dual) if abs(float(dual))>1e-9]
    info_result['column_duals_nonzero_float'] = [
        {'orbit_representative_mask':reps[i],'dual':float(value)}
        for i,value in enumerate(sol.col_dual) if abs(float(value))>1e-9]
    return info_result,sol.col_value


def scan(primal,orbit,existing):
    h = [0.0]+[primal[orbit[mask]] for mask in range(1,base.FULL+1)]
    def cmi(a,b,z):
        return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    violations = {}
    checked = 0
    for ai,bi in combinations(range(base.N),2):
        a,b = 1 << ai,1 << bi
        others = [i for i in range(base.N) if i not in (ai,bi)]
        for csize,dsize in ((1,1),(2,1),(1,2)):
            for cs in combinations(others,csize):
                remaining = [i for i in others if i not in cs]
                c = sum(1 << i for i in cs)
                for ds in combinations(remaining,dsize):
                    d = sum(1 << i for i in ds)
                    rest = base.FULL ^ (a|b|c|d)
                    z = rest
                    while True:
                        aterm = cmi(a,b,c|z)
                        base_delta = cmi(a,b,d|z)+cmi(c,d,z)-cmi(a,b,z)
                        dterm = cmi(a,c,b|z)+cmi(b,c,a|z)
                        for n in (1,2,3,4):
                            checked += 1
                            factor = n*(n+1)//2
                            slack = (n+1)*aterm+n*base_delta+factor*dterm
                            if slack < CUTOFF:
                                terms = (base.cmi(a,b,c|z,n+1)+base.cmi(a,b,d|z,n)
                                         +base.cmi(c,d,z,n)+base.cmi(a,b,z,-n)
                                         +base.cmi(a,c,b|z,factor)+base.cmi(b,c,a|z,factor))
                                key = base.row_from_terms(terms,orbit)
                                if key and key not in existing:
                                    metadata = {'kind':'copy-family','n':n,'A_mask':a,'B_mask':b,
                                                'C_mask':c,'D_mask':d,'condition_mask':z}
                                    old = violations.get(key)
                                    if old is None or slack < old[0]:
                                        violations[key] = (slack,metadata)
                        if z == 0:
                            break
                        z = (z-1) & rest
    return checked,violations


def main():
    started = time.monotonic()
    raw = base.INPUT.read_bytes()
    candidate = json.loads(raw)
    group = base.automorphism_group()
    orbit,reps = base.canonical_orbits(group)
    rows = base.shannon_rows(orbit)
    for family in base.copy_rows(orbit).values():
        for key,meta in family.items():
            rows.setdefault(key,meta)
    fd = base.fd_rows(orbit)
    sample = base.sample_sym_entropy(group,orbit,reps,candidate)
    rounds = []
    stop = 'round limit'
    for round_index in range(MAX_ROUNDS):
        if time.monotonic()-started >= MAX_WALL_SECONDS:
            stop = 'wall limit before next round'; break
        result,primal = solve(rows,fd,orbit,reps,sample)
        result['round'] = round_index
        if primal is None:
            rounds.append(result); stop='LP not optimal'; break
        before = time.monotonic()
        checked,violations = scan(primal,orbit,rows)
        result['scan_elapsed_s'] = time.monotonic()-before
        result['expanded_substitutions_checked'] = checked
        result['unique_new_violated_rows'] = len(violations)
        result['most_negative_slack_float'] = min((v[0] for v in violations.values()),default=0.0)
        selected = sorted(violations.items(),key=lambda item:item[1][0])[:MAX_CUTS_PER_ROUND]
        result['cuts_added'] = len(selected)
        for key,(slack,meta) in selected:
            rows[key] = meta
        rounds.append(result)
        if not selected:
            stop='no violations in the scanned substitution family'; break
    out = {'candidate_sha256':hashlib.sha256(raw).hexdigest(),
           'base_module_sha256':hashlib.sha256((ROOT/'frontier-20261028-copy-family-upper-lp.py').read_bytes()).hexdigest(),
           'highspy_version':highspy.Highs().version(), 'group_size':len(group),
           'orbit_columns':len(reps), 'substitution_scope':'A,B singleton; (|C|,|D|)=(1,1),(2,1),(1,2); all disjoint; Z any subset of remaining vertices; n=1..4.',
           'max_rounds':MAX_ROUNDS, 'max_wall_s_checked_between_rounds':MAX_WALL_SECONDS,
           'max_cuts_added_per_round':MAX_CUTS_PER_ROUND,
           'stop':stop,'rounds':rounds,'total_elapsed_s':time.monotonic()-started,
           'limits':'All LP objectives/duals are floating-point search output only. No exact certificate, global optimum or target-bound improvement is claimed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(out,stream,indent=2); stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rounds'},indent=2))
    print(json.dumps([{k:v for k,v in r.items() if not k.endswith('_duals_nonzero_float')}
                      for r in rounds],indent=2))


if __name__ == '__main__':
    main()
