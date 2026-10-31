#!/usr/bin/env python3
"""Three complete actual fixed-small-row L7 primitive quotients, in faithful Lyndon coordinates.

All source-ideal basis derivatives are STILL checked at both affine values.
Only the representation changes: compute D3 once per standard bracket and
combine in the independent monic Lyndon basis of L6, rather than repeatedly
lowering dense expanded representatives. No ideal, source or target is omitted.
The original suffix-Cartan lowering implementation is retained here. A replay
must use the separate bracket-tree/Jacobi engine and independently rebuild the
whole ideal. Shared exact FLINT arithmetic is a disclosed trust boundary.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CATALOG=((2,2),(3,2),(2,4))


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ideals=load('coordinate_ideals','frontier-20261028-lyndon-native-ideals-v2.py')
fast=load('integer_roots','frontier-20261028-level6-fast-pair.py')
levi=ideals.levi
lift=levi.lift
flint=fast.flint


def encode(v):
    return {''.join(map(str,w)):str(c) for w,c in sorted(v.items()) if c}


def publish(path,record):
    with path.open('x') as stream:
        json.dump(record,stream,indent=2)
        stream.write('\n')
    return {'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}


seventh=load('exact_seventh_character','frontier-20261029-level7-canonical-small-type.py')


@lru_cache(None)
def prime_dimensions(a,b):
    return seventh.dimensions(a,b)


def lowest_multiplicity(a,b):
    return prime_dimensions(a,b)[1]


def weight_dimension(a,b):
    return prime_dimensions(a,b)[0]


@lru_cache(None)
def operator_word(word,operator,r,s):
    vector=ideals.standard(word)
    if operator=='f3':
        result=levi.lower3(vector,r,s)
    else:
        result=levi.levi_action(vector,operator,r,s)
    return ideals.decompose(result) if result else {}


def apply(vector,operator,r,s):
    result={}
    for word,c in vector.items():
        for w,b in operator_word(word,operator,r,s).items():
            result[w]=result.get(w,Q(0))+c*b
            if not result[w]:
                del result[w]
    return result


def difference(a,b):
    result=dict(a)
    for w,c in b.items():
        result[w]=result.get(w,Q(0))-c
        if not result[w]:
            del result[w]
    return result


def scalar_polynomial(values,scale):
    work=list(values)
    result=flint.fmpq_poly([])
    binomial=flint.fmpq_poly([1])
    index=0
    while work:
        result+=binomial*flint.fmpq(work[0],scale)
        work=[b-a for a,b in zip(work,work[1:])]
        binomial*=flint.fmpq_poly([-index,1])
        binomial/=index+1
        index+=1
    for t,v in enumerate(values):
        assert result(t)*scale==v
    return result


def certify_scalar(poly):
    rational=[Q(str(c)) for c in poly]
    den=math.lcm(*(c.denominator for c in rational))
    integral=flint.fmpz_poly([int(c*den) for c in rational])
    co=list(integral)
    if integral[0] and (all(c>=0 for c in co) or all(c<=0 for c in co)):
        return [],{'method':'all coefficients one weak sign and nonzero constant'}
    repeated=integral.gcd(integral.derivative())
    squarefree,rem=divmod(integral,repeated)
    assert not rem
    return fast.integer_root_certificate(squarefree,1000)


def run_case(a,b,fixed,value,spaces):
    def parameters(t):
        return (value,7+t) if fixed=='r' else (7+t,value)
    r0,s0=parameters(0)
    degree=(a,b,7)
    name=f'frontier-20261029-level7-{a}{b}-complete-primitive-source-v1.json'
    raw=(ROOT/name).read_bytes()
    P=json.loads(raw)
    words=[tuple(map(int,w)) for w in P['source_words']]
    assert len(words)==len(set(words))==weight_dimension(a,b)
    assert words==sorted(words)
    for w in words:
        assert len(w)==7 and lift.is_lyndon(w)
        assert tuple(sum(levi.WEIGHTS[i][j] for i in w) for j in range(2))==(a,b)
    free=[]
    independent=lift.Span()
    for co in P['horizontal_kernel_coefficients']:
        vector={words[int(i)]:Q(q) for i,q in co.items() if Q(q)}
        assert independent.add(vector) is not None
        assert not apply(vector,'f1',r0,s0) and not apply(vector,'f2',r0,s0)
        free.append(vector)
    assert len(free)==lowest_multiplicity(a,b)
    I=spaces.get(degree,ideals.WordSpace())
    T=spaces.get((a,b,6),ideals.WordSpace())
    source_span=lift.Span()
    for co in I.coordinate_rows.values():
        source_span.add(co)
    chosen=[]
    indices=[]
    for i,v in enumerate(free):
        if source_span.add(v) is not None:
            chosen.append(v)
            indices.append(i)
    for t in (0,1):
        r,s=parameters(t)
        for co in I.coordinate_rows.values():
            assert not T.coordinate_reduce(apply(co,'f3',r,s)), 'whole source-ideal derivative containment failed'
    base=[T.coordinate_reduce(apply(v,'f3',r0,s0)) for v in chosen]
    r1,s1=parameters(1)
    after=[T.coordinate_reduce(apply(v,'f3',r1,s1)) for v in chosen]
    slope=[difference(x,y) for x,y in zip(after,base)]
    rank=lift.Span()
    for v in base:
        rank.add(v)
    k=len(chosen)
    result={'degree':list(degree),'fixed_parameter':fixed,'fixed_value':value,'other_parameter_class':'>=7',
            'variable':'t=other_parameter-7','coordinate_basis':'standard monic Lyndon brackets, NOT associative-word coefficients',
            'pencil':{'file':name,'sha256':hashlib.sha256(raw).hexdigest()},
            'free_weight_dimension':len(words),'free_primitive_dimension':len(free),
            'full_source_ideal_dimension':len(I),'full_target_ideal_dimension':len(T),
            'source_ideal_lyndon_coordinate_rows':[encode(v) for v in I.coordinate_rows.values()],
            'target_ideal_lyndon_coordinate_rows':[encode(v) for v in T.coordinate_rows.values()],
            'retained_free_primitive_indices':indices,'actual_primitive_quotient_dimension':k,
            'all_free_primitive_basis_vectors_checked':True,'free_completeness_check':'independence, horizontal membership and exact Witt/Weyl multiplicity',
            'all_source_ideal_basis_derivatives_checked_at':[0,1],
            'primitive_quotient_completeness_import':'finite-sl3 complete reducibility',
            'baseline_D3_rank':len(rank)}
    if k==0:
        result['status']='ZERO_ACTUAL_PRIMITIVE_SOURCE'
        return result
    if len(rank)<k:
        result['status']='BASELINE_ACTUAL_QUOTIENT_RANK_DEFECT'
        kernel=lift.kernel_with_coefficients(base)
        result['baseline_kernel_source_coefficients']=[{str(i):str(c) for i,c in v.items()} for v in kernel]
        return result
    selected=sorted(rank.rows)
    matrix=[[[v.get(w,Q(0)),dy.get(w,Q(0))] for v,dy in zip(base,slope)] for w in selected]
    scales=[math.lcm(*(c.denominator for e in row for c in e)) for row in matrix]
    integer=[[[int(c*scale) for c in e] for e in row] for row,scale in zip(matrix,scales)]
    vals=[int(flint.fmpz_mat([[c+t*m for c,m in row] for row in integer]).det()) for t in range(k+1)]
    poly=scalar_polynomial(vals,math.prod(scales))
    assert poly.degree()<=k and poly(0)
    roots,certificate=certify_scalar(poly)
    exceptions=[]
    support=sorted(set(w for v in base+slope for w in v))
    for t in [x for x in roots if x>=0]:
        full=[[v.get(w,Q(0))+t*dy.get(w,Q(0)) for v,dy in zip(base,slope)] for w in support]
        actual_rank=flint.fmpq_mat([[flint.fmpq(c.numerator,c.denominator) for c in row] for row in full]).rank()
        exceptions.append({'t':t,'rank':actual_rank,'columns':k})
    result.update({'selected_target_lyndon_coordinates':[''.join(map(str,w)) for w in selected],
                   'matrix':[[[str(c) for c in e] for e in row] for row in matrix],
                   'determinant_coefficients_low_to_high':[str(c) for c in poly],
                   'exact_determinant_grid_points':k+1,'integer_minor_roots':roots,'root_certificate':certificate,
                   'full_matrix_rank_checks_at_nonnegative_roots':exceptions,
                   'status':'ALL_INTEGER_PARAMETER_VALUES_FULL_ACTUAL_QUOTIENT_RANK' if all(e['rank']==k for e in exceptions) else 'ACTUAL_QUOTIENT_RANK_DEFECT_FOUND'})
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--fixed',choices=['r','s'],required=True)
    ap.add_argument('--value',type=int,choices=[1,2,3,4,5],required=True)
    ap.add_argument('--types',nargs='*')
    ap.add_argument('--tag',default='v1')
    args=ap.parse_args()
    types=CATALOG if args.types is None else tuple(ab for ab in CATALOG if f'{ab[0]}{ab[1]}' in args.types)
    assert types and (args.types is None or len(types)==len(set(args.types)))
    prefix=f'frontier-20261029-level7-{args.fixed}{args.value}-coordinate'
    output=ROOT/f'{prefix}-family-{args.tag}.json'
    if output.exists():
        raise FileExistsError(output)
    r,s=(args.value,7) if args.fixed=='r' else (7,args.value)
    bound=(max(a for a,b in types),max(b for a,b in types),7)
    spaces=ideals.ideal_bases(bound,r,s)
    parts=[]
    statuses=[]
    for a,b in types:
        part=ROOT/f'{prefix}-part-{a}{b}-{args.tag}.json'
        if part.exists():
            raise FileExistsError(part)
        record=run_case(a,b,args.fixed,args.value,spaces)
        parts.append(publish(part,record))
        statuses.append(record['status'])
        print('ACTUAL COORDINATE ROW',args.fixed,args.value,(a,b,7),'I',record['full_source_ideal_dimension'],'T',record['full_target_ideal_dimension'],
              'P',record['free_primitive_dimension'],'Q',record['actual_primitive_quotient_dimension'],record['status'],part.name,flush=True)
    good={'ZERO_ACTUAL_PRIMITIVE_SOURCE','ALL_INTEGER_PARAMETER_VALUES_FULL_ACTUAL_QUOTIENT_RANK'}
    record={'owner':'MathKacMoody-2','fixed_parameter':args.fixed,'fixed_value':args.value,'other_parameter_lower_bound':7,
            'types':[list(ab) for ab in types],'complete_declared_three_type_catalogue':types==CATALOG,'parts':parts,
            'native_ideal_helper_sha256':hashlib.sha256((ROOT/'frontier-20261028-lyndon-native-ideals-v2.py').read_bytes()).hexdigest(),
            'native_ideal_construction':ideals.LAST_TRACE,'representation':'faithful monic Lyndon coordinate source and target quotients',
            'all_source_ideal_basis_derivatives_checked_at_two_affine_points':True,
            'status':'ALL_SELECTED_ACTUAL_PRIMITIVE_FAMILIES_CERTIFIED' if all(s in good for s in statuses) else 'OPEN_FAMILIES_REMAIN',
            'limits':'Named actual free-Levi/PBW and complete-reducibility imports; exact computation pending independent source/matrix reconstruction and scientific review. NOT whole level7/B7, formal verification or parent acceptance.'}
    publish(output,record)
    print('WROTE',output.name,flush=True)


if __name__=='__main__':
    main()
