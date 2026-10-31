#!/usr/bin/env python3
"""Actual L6 omitted coordinate/wall quotient pencils when one parameter is four.

The other parameter is >=6. The ENTIRE level5/6 node3 ideal is generated with
the existing Serre-ideal engine. Complete reducibility of finite sl3 makes the
free horizontal space surject onto the quotient horizontal space. Therefore
reduce the full free primitive basis modulo the actual source ideal and retain
independent classes; do NOT rebuild a costly full-source horizontal RREF.

D3 source-ideal containment is checked at the two affine parameter values. All
F3 target reductions use the FULL level5 ideal. A single exact univariate minor
is certified for all nonnegative integer parameters by sign or Hensel/Cauchy;
any integer roots receive a direct full-matrix rank check. No free/actual
source equality is assumed when the source ideal is nonzero.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    sp = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(module)
    return module


fast = load('fast_pair', 'frontier-20261028-level6-fast-pair.py')
levi = load('actual_quotient', 'frontier-20261028-levi-lie-engine.py')
interp = load('one_variable', 'frontier-20261028-level5-small-row-quotient-determinant.py')
lift = levi.lift


def encode(vector):
    return {''.join(map(str,w)):str(c) for w,c in sorted(vector.items()) if c}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fixed', choices=['r','s'], required=True)
    args = ap.parse_args()
    out = ROOT / f'frontier-20261028-level6-{args.fixed}4-extra-quotient-family-v1.json'
    if out.exists():
        raise FileExistsError(out)
    fixed = args.fixed
    def parameters(t):
        return (4,6+t) if fixed=='r' else (6+t,4)
    r0,s0 = parameters(0)
    spaces = levi.ideal_bases((4,5,6),r0,s0)
    records, pins = [], []
    for a,b in ((0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,4),(4,5)):
        degree = (a,b,6)
        name = f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json'
        raw = (ROOT/name).read_bytes()
        P = json.loads(raw)
        pins.append({'file':name,'sha256':hashlib.sha256(raw).hexdigest()})
        basis = levi.lie_basis(degree)
        assert [''.join(map(str,w)) for w,_ in basis] == P['source_words']
        free_vectors = [lift.combine([v for _,v in basis],{int(i):Q(q) for i,q in co.items()})
                        for co in P['horizontal_kernel_coefficients']]
        I = spaces.get(degree,lift.Span())
        T = spaces.get((a,b,5),lift.Span())
        span = lift.Span()
        for row in I.rows.values():
            span.add(row)
        chosen, indices = [], []
        for i,vector in enumerate(free_vectors):
            assert not levi.levi_action(vector,'f1',r0,s0) and not levi.levi_action(vector,'f2',r0,s0)
            if span.add(vector) is not None:
                chosen.append(vector)
                indices.append(i)
        for t in (0,1):
            rr,ss = parameters(t)
            for row in I.rows.values():
                assert not T.reduce(levi.lower3(row,rr,ss)), 'D3 ideal containment failed'
        base = [T.reduce(levi.lower3(v,r0,s0)) for v in chosen]
        r1,s1 = parameters(1)
        following = [T.reduce(levi.lower3(v,r1,s1)) for v in chosen]
        slope = []
        for aa,bb in zip(base,following):
            d = dict(bb)
            for w,c in aa.items():
                d[w] = d.get(w,Q(0))-c
            slope.append({w:c for w,c in d.items() if c})
        k = len(chosen)
        rank = lift.Span()
        for col in base:
            rank.add(col)
        rec = {'degree':list(degree),'fixed_parameter':fixed,'fixed_value':4,'other_parameter_class':'>=6',
               'variable':'t=other_parameter-6','free_weight_dimension':len(basis),
               'full_source_ideal_dimension':len(I),'full_target_ideal_dimension':len(T),
               'free_primitive_dimension':len(free_vectors),'actual_primitive_quotient_dimension':k,
               'retained_free_primitive_indices':indices,'baseline_D3_rank':len(rank),
               'source_ideal_rows':[encode(v) for v in I.rows.values()],
               'target_ideal_rows':[encode(v) for v in T.rows.values()],
               'affine_source_ideal_derivative_containment_checks':[0,1]}
        if k==0:
            rec['status']='ZERO_ACTUAL_PRIMITIVE_SOURCE'
        elif len(rank)<k:
            rec['status']='BASELINE_ACTUAL_QUOTIENT_RANK_DEFECT'
        else:
            words = sorted(rank.rows)
            matrix = [[[col.get(w,Q(0)),dy.get(w,Q(0))] for col,dy in zip(base,slope)] for w in words]
            scales = [math.lcm(*(q.denominator for e in row for q in e)) for row in matrix]
            integer = [[[int(q*scale) for q in e] for e in row] for row,scale in zip(matrix,scales)]
            values = [int(fast.flint.fmpz_mat([[c+t*m for c,m in row] for row in integer]).det()) for t in range(k+1)]
            # Use the published level-five exact forward-difference and
            # falling-binomial conversion, with integer-scaled values.
            work, differences = values[:], []
            while work:
                differences.append(work[0])
                work = [b-a for a,b in zip(work,work[1:])]
            co = [Q(0)]*(k+1)
            for i,d in enumerate(differences):
                for j,c in enumerate(interp.det.falling_binomial(i)):
                    co[j] += d*c
            assert len(co)==k+1
            poly = fast.flint.fmpq_poly([fast.flint.fmpq(c.numerator,c.denominator*math.prod(scales)) for c in co])
            for t,v in enumerate(values):
                assert poly(t)*math.prod(scales)==v
            rec['selected_target_words']=[''.join(map(str,w)) for w in words]
            rec['matrix']=[[[str(q) for q in e] for e in row] for row in matrix]
            rec['determinant_coefficients_low_to_high']=[str(c) for c in poly]
            ints = [Q(str(c)) for c in poly]
            den = math.lcm(*(c.denominator for c in ints))
            Z = fast.flint.fmpz_poly([int(c*den) for c in ints])
            coefficients = list(Z)
            if Z[0] and (all(c>=0 for c in coefficients) or all(c<=0 for c in coefficients)):
                roots,cert = [],{'method':'all coefficients one weak sign and nonzero constant'}
            elif Z.degree()==0:
                roots,cert = [],{'method':'nonzero constant'}
            else:
                rep = Z.gcd(Z.derivative())
                squarefree,rem = divmod(Z,rep)
                assert not rem
                roots,cert = fast.integer_root_certificate(squarefree,1000)
            exceptional=[]
            all_words=sorted(set(w for col in base+slope for w in col))
            for t in [v for v in roots if v>=0]:
                full = [[base[j].get(w,0)+t*slope[j].get(w,0) for j in range(k)] for w in all_words]
                rr = fast.flint.fmpq_mat([[fast.flint.fmpq(Q(c).numerator,Q(c).denominator) for c in row] for row in full]).rank()
                exceptional.append({'t':t,'rank':rr,'columns':k})
            rec['integer_minor_roots']=roots
            rec['root_certificate']=cert
            rec['full_matrix_rank_checks_at_nonnegative_roots']=exceptional
            rec['status']='ALL_INTEGER_PARAMETER_VALUES_FULL_ACTUAL_QUOTIENT_RANK' if all(e['rank']==k for e in exceptional) else 'ACTUAL_QUOTIENT_RANK_DEFECT_FOUND'
        records.append(rec)
        print('ACTUAL ROW',fixed,degree,'ideal',len(I),'target ideal',len(T),'primitive',len(free_vectors),'->',k,rec['status'],flush=True)
    with out.open('x') as stream:
        json.dump({'fixed_parameter':fixed,'fixed_value':4,'other_parameter_lower_bound':6,'inputs':pins,
                   'source_reduction':'finite-sl3 complete reducibility: free primitive -> quotient primitive is surjective; kernel=source ideal intersection',
                   'records':records,'status':'ALL_EIGHT_EXTRA_ACTUAL_PRIMITIVE_FAMILIES_CERTIFIED' if all(e['status'] in ('ZERO_ACTUAL_PRIMITIVE_SOURCE','ALL_INTEGER_PARAMETER_VALUES_FULL_ACTUAL_QUOTIENT_RANK') for e in records) else 'OPEN_FAMILIES_REMAIN',
                   'limits':'actual-source/free-Levi and complete-reducibility inputs; independent reconstruction pending; not formal verification'},stream,indent=2)
        stream.write('\n')
    print('WROTE',out.name,flush=True)


if __name__=='__main__':
    main()
