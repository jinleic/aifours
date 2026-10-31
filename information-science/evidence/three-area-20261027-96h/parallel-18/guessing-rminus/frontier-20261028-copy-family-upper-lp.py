#!/usr/bin/env python3
"""Symmetry-reduced Shannon + valid copy-family R-minus upper-bound search.

This is an EXPLORATORY floating-point LP. A solver objective is NOT an exact
upper proof: any improvement requires a separate exact rational identity
checker. No held/reviewed historical outcome is assumed as a premise.
"""
from collections import Counter, deque
from itertools import combinations
from math import log
from pathlib import Path
import hashlib
import json
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-highspy'))
import highspy

INPUT = ROOT / 'frontier-20261028-fd-law-search-precise-result.json'
OUTPUT = ROOT / 'frontier-20261028-copy-family-upper-lp-result.json'
NEIGHBOURS = {
    1: (2,3,4,5,6,7), 2: (1,3,7,9,10), 3: (1,2,4,8,9),
    4: (1,3,5,8,10), 5: (1,4,6,9,10), 6: (1,5,7,8,9),
    7: (1,2,6,8,10), 8: (3,4,6,7,9,10), 9: (2,3,5,6,8),
    10: (2,4,5,7,8),
}
# 0-based vertex maps; independently verified on every graph edge below.
GENERATORS = ((7,9,6,5,8,2,3,0,1,4), (0,4,5,6,1,2,3,7,8,9))
N = 10
FULL = (1 << N) - 1
SOLVER_TIME_LIMIT = 30.0


def permute_mask(mask, permutation):
    return sum(1 << permutation[i] for i in range(N) if mask & (1 << i))


def automorphism_group():
    edges = {frozenset((u-1,v-1)) for u, ns in NEIGHBOURS.items() for v in ns}
    assert len(edges) == 26
    for p in GENERATORS:
        assert sorted(p) == list(range(N))
        assert {frozenset(p[i] for i in e) for e in edges} == edges
    identity = tuple(range(N))
    group = {identity}
    queue = deque([identity])
    while queue:
        p = queue.popleft()
        for g in GENERATORS:
            q = tuple(g[p[i]] for i in range(N))
            if q not in group:
                group.add(q)
                queue.append(q)
    return sorted(group)


def canonical_orbits(group):
    representatives = {0: 0}
    for mask in range(1, FULL+1):
        representatives[mask] = min(permute_mask(mask, p) for p in group)
    distinct = sorted(set(representatives.values()) - {0})
    ids = {mask: i for i, mask in enumerate(distinct)}
    return {m: (None if not m else ids[r]) for m,r in representatives.items()}, distinct


def row_from_terms(terms, orbit):
    row = {}
    for mask, coefficient in terms:
        if not mask or not coefficient:
            continue
        col = orbit[mask]
        row[col] = row.get(col,0) + coefficient
    return tuple(sorted((k,v) for k,v in row.items() if v))


def cmi(a,b,z,multiplier=1):
    return ((a|z,multiplier),(b|z,multiplier),(a|b|z,-multiplier),(z,-multiplier))


def shannon_rows(orbit):
    rows = {}
    for i in range(N):
        key = row_from_terms(((FULL,1),(FULL ^ (1 << i),-1)),orbit)
        if key:
            rows.setdefault(key, {'kind':'Hconditional','i':i+1})
    for i,j in combinations(range(N),2):
        remaining = FULL ^ (1 << i) ^ (1 << j)
        z = remaining
        while True:
            key = row_from_terms(cmi(1 << i,1 << j,z),orbit)
            if key:
                rows.setdefault(key, {'kind':'CMI','i':i+1,'j':j+1,'condition_mask':z})
            if z == 0:
                break
            z = (z-1) & remaining
    return rows


def copy_rows(orbit):
    by_order = {order:{} for order in (1,2,3,4)}
    variables = range(N)
    for ai,bi in combinations(variables,2):
        others = [x for x in variables if x not in (ai,bi)]
        a,b = 1 << ai,1 << bi
        for ci in others:
            for di in others:
                if ci == di:
                    continue
                c,d = 1 << ci,1 << di
                residual = [x for x in others if x not in (ci,di)]
                # Empty and single-vertex conditioning, all choices.
                for z in (0, *(1 << x for x in residual)):
                    for order, rows in by_order.items():
                        factor = order*(order+1)//2
                        terms = (cmi(a,b,c|z,order+1) + cmi(a,b,d|z,order)
                                 + cmi(c,d,z,order) + cmi(a,b,z,-order)
                                 + cmi(a,c,b|z,factor) + cmi(b,c,a|z,factor))
                        key = row_from_terms(terms,orbit)
                        if key:
                            rows.setdefault(key, {'kind':'copy-family','n':order,
                                'A':ai+1,'B':bi+1,'C':ci+1,'D':di+1,'condition_mask':z})
    return by_order


def fd_rows(orbit):
    rows = {}
    for v,ns in NEIGHBOURS.items():
        mask = sum(1 << (u-1) for u in ns)
        key = row_from_terms(((mask | (1 << (v-1)),1),(mask,-1)),orbit)
        if key:
            rows.setdefault(key, {'kind':'FD','vertex':v})
    return rows


def sample_sym_entropy(group, orbit, representatives, candidate):
    words = candidate['support_words_one_based_bitsets']
    weights = candidate['rounded_probability_numerators']
    total = sum(weights)
    full_entropy = [0.0] * (FULL+1)
    for mask in range(1,FULL+1):
        counts = Counter()
        for word,w in zip(words,weights):
            counts[word & mask] += w
        full_entropy[mask] = -sum((count/total)*log(count/total) for count in counts.values())
    return np.array([sum(full_entropy[permute_mask(mask,p)] for p in group) / len(group)
                     for mask in representatives])


def solve(rows, fd, orbit, representatives, sample):
    starts, indexes, values, lower, upper, metadata = [], [], [], [], [], []
    def add(key,lo,hi,meta):
        starts.append(len(indexes))
        for index,value in key:
            indexes.append(index)
            values.append(float(value))
        lower.append(lo)
        upper.append(hi)
        metadata.append(meta)
    inf = highspy.kHighsInf
    min_sample_ineq = float('inf')
    for key,meta in rows.items():
        value = sum(coef*sample[col] for col,coef in key)
        min_sample_ineq = min(min_sample_ineq,value)
        assert value > -1e-8, (meta,value)
        add(key,0.0,inf,meta)
    for key,meta in fd.items():
        value = sum(coef*sample[col] for col,coef in key)
        assert abs(value) < 1e-8, (meta,value)
        add(key,0.0,0.0,meta)
    count = len(representatives)
    col_lower = np.zeros(count)
    col_upper = np.full(count,inf)
    for i in range(N):
        col_upper[orbit[1 << i]] = 1.0
    costs = np.zeros(count)
    costs[orbit[FULL]] = 1.0
    lp = highspy.HighsLp()
    lp.num_col_, lp.num_row_ = count, len(starts)
    lp.col_cost_, lp.col_lower_, lp.col_upper_ = costs, col_lower, col_upper
    lp.row_lower_, lp.row_upper_ = np.array(lower), np.array(upper)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(starts+[len(indexes)],dtype=np.int32)
    lp.a_matrix_.index_ = np.array(indexes,dtype=np.int32)
    lp.a_matrix_.value_ = np.array(values,dtype=float)
    lp.sense_ = highspy.ObjSense.kMaximize
    solver = highspy.Highs()
    solver.silent()
    solver.setOptionValue('threads',1)
    solver.setOptionValue('time_limit',SOLVER_TIME_LIMIT)
    solver.passModel(lp)
    started = time.monotonic()
    solver.run()
    status = solver.modelStatusToString(solver.getModelStatus())
    info = solver.getInfo()
    solution = solver.getSolution()
    result = {'status':status,'elapsed_s':time.monotonic()-started,
              'rows':len(starts),'columns':count,'nnz':len(indexes),
              'sample_min_inequality_float':min_sample_ineq,
              'objective_float_unverified':float(info.objective_function_value)}
    if status == 'Optimal':
        result['nonzero_row_duals_float'] = [
            {'metadata':meta,'row':rowspec,'dual':float(dual)}
            for meta,rowspec,dual in zip(metadata,list(rows.keys())+list(fd.keys()),solution.row_dual)
            if abs(float(dual)) > 1e-9]
        result['nonzero_column_duals_float'] = [
            {'orbit_representative_mask':representatives[i],'dual':float(value)}
            for i,value in enumerate(solution.col_dual) if abs(float(value)) > 1e-9]
    return result


def main():
    started = time.monotonic()
    raw = INPUT.read_bytes()
    candidate = json.loads(raw)
    group = automorphism_group()
    orbit, representatives = canonical_orbits(group)
    shannon = shannon_rows(orbit)
    fd = fd_rows(orbit)
    family = copy_rows(orbit)
    sample = sample_sym_entropy(group,orbit,representatives,candidate)
    results = {}
    for name,orders in (('shannon',()),('copy_n1',(1,)),('copy_n1_through_n4',(1,2,3,4))):
        rows = dict(shannon)
        for order in orders:
            for key,meta in family[order].items():
                rows.setdefault(key,meta)
        results[name] = solve(rows,fd,orbit,representatives,sample)
    out = {'candidate_sha256':hashlib.sha256(raw).hexdigest(),
           'highspy_version':highspy.Highs().version(),
           'automorphism_group_size':len(group),
           'nonempty_subset_orbit_columns':len(representatives),
           'symmetry_generators_0_based':GENERATORS,
           'distinct_shannon_rows':len(shannon),
           'distinct_Fn_rows_by_order':{str(k):len(v) for k,v in family.items()},
           'F_family':'(n+1)I(A;B|CZ)+n I(A;B|DZ)+n I(C;D|Z)-n I(A;B|Z)+n(n+1)/2 [I(A;C|BZ)+I(B;C|AZ)] >= 0',
           'substitution_scope':'A,B,C,D are distinct single original vertices, Z empty or one distinct original vertex; n=1..4.',
           'solver_threads':1,'per_solve_time_limit_s':SOLVER_TIME_LIMIT,
           'results':results,'total_elapsed_s':time.monotonic()-started,
           'limits':'Exploratory HiGHS double precision only; no objective is an exact certificate or an adopted original upper bound. Restricting substitution choices is not an entropic impossibility result.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:
        json.dump(out,stream,indent=2)
        stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'results'},indent=2))
    print(json.dumps({k:{kk:vv for kk,vv in r.items() if not kk.startswith('nonzero_')}
                      for k,r in results.items()},indent=2))


if __name__ == '__main__':
    main()
