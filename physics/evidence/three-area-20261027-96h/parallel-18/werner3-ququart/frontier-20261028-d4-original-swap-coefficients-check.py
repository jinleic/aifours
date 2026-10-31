#!/usr/bin/env python3
"""Exact coefficientwise d4 q3 trace/swap identity on all 64x2 U,V.

This expands two independent index formulas as integer polynomials in formal
U, conj(U), V, conj(V) entries. It covers all eight subsets and every mixed
column contraction; no physical instance is substituted and no floats are used.
"""
import collections
import itertools
import json
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-d4-original-swap-coefficients-check-results.json'
D=4; COPIES=3; COLS=2
BASIS=list(itertools.product(range(D),repeat=COPIES))
LABEL={x:i for i,x in enumerate(BASIS)}


def merge(coords_s,coords_c,S,C):
    out=[None]*COPIES
    for i,x in zip(S,coords_s): out[i]=x
    for i,x in zip(C,coords_c): out[i]=x
    return tuple(out)


def direct_trace_polynomial(S):
    """Expand ||Tr_S(UV†)||HS² independently by trace and complement indices."""
    S=tuple(sorted(S)); C=tuple(i for i in range(COPIES) if i not in S)
    traced=list(itertools.product(range(D),repeat=len(S)))
    outside=list(itertools.product(range(D),repeat=len(C)))
    terms=collections.Counter()
    for p,q,z,z2 in itertools.product(outside,outside,traced,traced):
        x=LABEL[merge(z,p,S,C)]; y=LABEL[merge(z,q,S,C)]
        x2=LABEL[merge(z2,p,S,C)]; y2=LABEL[merge(z2,q,S,C)]
        for a,b in itertools.product(range(COLS),repeat=2):
            # U[x,a] conj(U[x2,b]) V[y2,b] conj(V[y,a])
            terms[(COLS*x+a,COLS*x2+b,COLS*y2+b,COLS*y+a)]+=1
    return terms


def swap_polynomial(S):
    """Expand <U⊗V,F_Q F_S(U⊗V)> by literal swapped tensor entries."""
    S=set(S); terms=collections.Counter()
    for x,y in itertools.product(BASIS,repeat=2):
        xp=tuple(y[i] if i in S else x[i] for i in range(COPIES))
        yp=tuple(x[i] if i in S else y[i] for i in range(COPIES))
        lx,ly,lxp,lyp=LABEL[x],LABEL[y],LABEL[xp],LABEL[yp]
        for r,s in itertools.product(range(COLS),repeat=2):
            # conj(U[x,r]) conj(V[y,s]) U[xp,s] V[yp,r]
            terms[(COLS*lxp+s,COLS*lx+r,COLS*lyp+r,COLS*ly+s)]+=1
    return terms


def main():
    start=time.monotonic(); reports=[]; total_terms=0; failures=[]
    for k in range(COPIES+1):
        for S in itertools.combinations(range(COPIES),k):
            direct=direct_trace_polynomial(S); swap=swap_polynomial(S)
            bad=[key for key in set(direct)|set(swap) if direct[key]!=swap[key]]
            total_terms+=sum(direct.values())
            reports.append({'traced_sites':list(S),'coefficient_monomials':len(direct),
                            'direct_terms':sum(direct.values()),'coefficient_mismatches':len(bad),
                            'q3_weight_times_8':(-1)**k*2**(COPIES-k)})
            if bad: failures.append({'subset':list(S),'mismatch_count':len(bad),'first':list(bad[0])})
    result={'kind':'exact_coefficientwise_original_q3_swap_identity',
            'd':D,'physical_copies':COPIES,'factor_columns':COLS,
            'formal_variables':'U[x,r],conj(U[x,r]),V[x,r],conj(V[x,r])',
            'matrix_caller':'C=UV†; U,V arbitrary complex 64x2 (rank C<=2)',
            'trace_convention':'unnormalized traces',
            'subsets':reports,'total_direct_terms':total_terms,'mismatches':failures,
            'identity':'8q3(C) = sum_S (-1)^|S| 2^(3-|S|) <U⊗V,F_Q F_S(U⊗V)>',
            'scope':'Exact polynomial coefficients for all U,V and every trace subset. Does not prove nonnegativity or check certificate identity/PSD.',
            'elapsed_seconds':round(time.monotonic()-start,3),
            'verdict':'PASS' if not failures else 'FAIL'}
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if not failures else 1


if __name__=='__main__': raise SystemExit(main())
