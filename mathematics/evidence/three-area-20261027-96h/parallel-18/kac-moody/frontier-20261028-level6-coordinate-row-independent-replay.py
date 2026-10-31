#!/usr/bin/env python3
"""Independent whole-ideal/primitive/matrix replay of actual small-row families.

No producer module is imported. The separate matrix-unit/bracket-tree engine
supplies all actions; a raw integral PBW/adjoint construction supplies the WHOLE
Serre ideals. Supports either the original tensor-word certificates or the
successor's faithful Lyndon-coordinate certificates. Rechecks every ideal basis
derivative, all primitive classes, every selected pencil entry, a shifted exact
determinant grid, independent integer-root exclusions, and the fifth endpoint.
FLINT final RREF/determinant/gcd arithmetic is shared and explicitly disclosed.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


whole=load('independent_whole_ideals','frontier-20261028-level6-independent-coordinate-ideals.py')
rootcheck=load('independent_root_tools','frontier-20261028-level6-row-four-extra-replay.py')
ind=whole.ind
flint=whole.flint


def parsed(rows):
    return [{w:Q(c) for w,c in row.items() if Q(c)} for row in rows]


def source_character():
    tensor={0:Counter({(0,0):1})}
    for n in range(1,7):
        tensor[n]=Counter()
        for (a,b),c in tensor[n-1].items():
            for u,v in ind.WEIGHTS:
                tensor[n][a+u,b+v]+=c
    result=Counter(tensor[6])
    for d,sign in ((2,-1),(3,-1),(6,1)):
        for (a,b),c in tensor[6//d].items():
            result[d*a,d*b]+=sign*c
    assert all(c%6==0 and c>=0 for c in result.values())
    return Counter({degree:c//6 for degree,c in result.items() if c})


@lru_cache(None)
def action_coordinates(word,g,r,s):
    if g=='f3':
        vector=ind.tree_d3(word,r,s)
    else:
        vector=ind.act(ind.ind.standard_bracket(word),g,r,s)
    return whole.decompose(vector) if vector else {}


def linear_image(vector,g,r,s):
    result={}
    for word,c in vector.items():
        ind.ind.add_scaled(result,action_coordinates(word,g,r,s),c)
    return result


def basis_span(vectors):
    return ind.ind.ReducedSpace(vectors)


def polynomial_rank(base,slope,t):
    labels=sorted(set(w for col in base+slope for w in col))
    columns=len(base)
    matrix=[[Q(v.get(w,0))+t*Q(dy.get(w,0)) for v,dy in zip(base,slope)] for w in labels]
    assert len(labels)>=columns
    return flint.fmpq_mat([[flint.fmpq(c.numerator,c.denominator) for c in row] for row in matrix]).rank()


def replay_entry(e,pin,fixed,value,spaces,char):
    degree=tuple(e['degree'])
    a,b,n=degree
    def params(t):
        return (value,6+t) if fixed=='r' else (6+t,value)
    r,s=params(0)
    raw=(ROOT/pin['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==pin['sha256']
    P=json.loads(raw)
    words=P['source_words']
    assert len(words)==len(set(words))==char.get((a,b),0) and words==sorted(words)
    assert all(len(w)==6 and ind.ind.lyndon(w) and ind.deg(w)==degree for w in words)
    vectors=[{words[int(i)]:Q(c) for i,c in co.items() if Q(c)} for co in P['horizontal_kernel_coefficients']]
    expected=char.get((a,b),0)-char.get((a-1,b),0)-char.get((a,b-1),0)+char.get((a-2,b-1),0)+char.get((a-1,b-2),0)-char.get((a-2,b-2),0)
    assert len(vectors)==expected and len(basis_span(vectors))==expected
    for v in vectors:
        assert not linear_image(v,'f1',r,s) and not linear_image(v,'f2',r,s)
    coordinate_certificate='source_ideal_lyndon_coordinate_rows' in e
    if coordinate_certificate:
        claimedI=parsed(e['source_ideal_lyndon_coordinate_rows'])
        claimedT=parsed(e['target_ideal_lyndon_coordinate_rows'])
        target_basis={min(v):v for v in claimedT}
        selected=e.get('selected_target_lyndon_coordinates',[])
    else:
        claimedI=[whole.decompose(v) for v in parsed(e['source_ideal_rows'])]
        tensorT=parsed(e['target_ideal_rows'])
        claimedT=[whole.decompose(v) for v in tensorT]
        target_basis={min(v):v for v in tensorT}
        selected=e.get('selected_target_words',[])
    I=spaces[degree]
    T=spaces[(*degree[:2],5)]
    whole.same_space(I,claimedI)
    whole.same_space(T,claimedT)
    assert len(I)==e['full_source_ideal_dimension'] and len(T)==e['full_target_ideal_dimension']
    quotient=basis_span(I.rows.values())
    retained=[]
    for j,v in enumerate(vectors):
        if quotient.insert(v):
            retained.append(j)
    assert retained==e['retained_free_primitive_indices']
    k=len(retained)
    assert k==e['actual_primitive_quotient_dimension']
    for t in (0,1):
        rr,ss=params(t)
        for row in I.rows.values():
            assert not T.reduce(linear_image(row,'f3',rr,ss)), 'independent full ideal derivative containment failed'
    summary={'degree':list(degree),'source_ideal_dimension':len(I),'target_ideal_dimension':len(T),
             'actual_primitive_dimension':k,'free_horizontal_completeness_checks':expected,
             'both_whole_ideal_span_directions_checked':True,'all_fresh_ideal_basis_derivatives_checked_at':[0,1]}
    if not k:
        assert e['status']=='ZERO_ACTUAL_PRIMITIVE_SOURCE'
        summary['fifth_endpoint']='zero lowest source persists under further quotient'
        return summary
    chosen=[vectors[j] for j in retained]
    def columns_at(t,full=False):
        rr,ss=params(t)
        cache={}
        def image(word):
            if word not in cache:
                if coordinate_certificate:
                    raw=action_coordinates(word,'f3',rr,ss)
                else:
                    raw=ind.tree_d3(word,rr,ss)
                reduced=whole.normal_form(raw,target_basis)
                cache[word]=reduced if full else {w:reduced[w] for w in selected if w in reduced}
            return cache[word]
        cols=[]
        for v in chosen:
            out={}
            for word,c in v.items():
                ind.ind.add_scaled(out,image(word),c)
            cols.append(out)
        return cols
    base=columns_at(0)
    after=columns_at(1)
    slope=[]
    for aa,bb in zip(base,after):
        v=dict(bb)
        ind.ind.add_scaled(v,aa,-1)
        slope.append(v)
    matrix=[[[Q(v.get(w,0)),Q(dy.get(w,0))] for v,dy in zip(base,slope)] for w in selected]
    assert len(matrix)==k and matrix==[[[Q(c) for c in pair] for pair in row] for row in e['matrix']]
    scales=[math.lcm(*(c.denominator for pair in row for c in pair)) for row in matrix]
    integer=[[[int(c*scale) for c in pair] for pair in row] for row,scale in zip(matrix,scales)]
    poly=[Q(c) for c in e['determinant_coefficients_low_to_high']]
    assert len(poly)<=k+1 and poly[0]
    for t in range(1,k+2):
        actual=int(flint.fmpz_mat([[c+t*m for c,m in row] for row in integer]).det())
        assert Q(actual,math.prod(scales))==sum(c*t**i for i,c in enumerate(poly))
    if poly[0] and (all(c>=0 for c in poly) or all(c<=0 for c in poly)):
        roots=[]
        prime=None
        method='all coefficients one weak sign and nonzero constant'
    else:
        denominator=math.lcm(*(c.denominator for c in poly))
        Z=flint.fmpz_poly([int(c*denominator) for c in poly])
        roots,prime=rootcheck.integer_roots(Z)
        assert roots==e['integer_minor_roots']
        method='independent squarefree coverage, Cauchy bound and Hensel at a distinct prime'
    extra_checks=[]
    if any(t>=0 for t in roots):
        full_base=columns_at(0,True)
        full_after=columns_at(1,True)
        full_slope=[]
        for aa,bb in zip(full_base,full_after):
            v=dict(bb)
            ind.ind.add_scaled(v,aa,-1)
            full_slope.append(v)
        for t in [z for z in roots if z>=0]:
            rank=polynomial_rank(full_base,full_slope,t)
            assert rank==k
            extra_checks.append({'t':t,'rank':rank,'columns':k})
        assert extra_checks==e['full_matrix_rank_checks_at_nonnegative_roots']
    endpoint=sum(c*(-1)**i for i,c in enumerate(poly))
    deleted=(fixed=='r' and degree==(0,1,6)) or (fixed=='s' and degree==(1,0,6))
    if deleted:
        assert k==1 and endpoint==0
        index=2 if fixed=='r' else 1
        q6=whole.decompose(ind.seed(index,5))
        enlarged=basis_span(list(I.rows.values())+[q6])
        assert not enlarged.remainder(chosen[0])
        endpoint_status='whole old one-dimensional lowest source removed by new level6 Serre seed'
    elif endpoint:
        endpoint_status='selected actual target minor nonzero at t=-1'
    else:
        full=columns_at(-1,True)
        assert len(basis_span(full))==k
        endpoint_status='independent full target rank at t=-1 despite zero selected minor'
    summary.update({'all_selected_pencil_entries_matched':True,'selected_target_basis':'Lyndon coordinates' if coordinate_certificate else 'associative-word coefficient functionals',
                    'shifted_exact_grid_determinants':k+1,'nonnegative_integer_minor_root_rank_checks':extra_checks,
                    'all_integer_roots_when_hensel_used':roots if prime else None,'root_exclusion_method':method,'second_hensel_prime':prime,
                    'fifth_endpoint':endpoint_status,'endpoint_minus_one_minor_nonzero':bool(endpoint)})
    print('PASS independent actual quotient',fixed,value,degree,'P',k,'ideals',len(I),len(T),flush=True)
    return summary


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--family',required=True)
    ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    raw=(ROOT/args.family).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==args.sha256
    C=json.loads(raw)
    fixed=C['fixed_parameter']
    value=C['fixed_value']
    assert fixed in ('r','s') and value in (1,2,3,4)
    entries=[]
    if 'parts' in C:
        for part in C['parts']:
            body=(ROOT/part['file']).read_bytes()
            assert hashlib.sha256(body).hexdigest()==part['sha256']
            e=json.loads(body)
            entries.append((e,e['pencil']))
    else:
        assert len(C['inputs'])==len(C['records'])
        entries=list(zip(C['records'],C['inputs']))
    assert len({tuple(e['degree']) for e,pin in entries})==len(entries)
    queries={tuple(e['degree']) for e,pin in entries}|{(*e['degree'][:2],5) for e,pin in entries}
    r,s=(value,6) if fixed=='r' else (6,value)
    spaces=whole.ideal_spaces(queries,r,s)
    char=source_character()
    results=[replay_entry(e,pin,fixed,value,spaces,char) for e,pin in entries]
    output=ROOT/f'frontier-20261028-level6-{fixed}{value}-coordinate-independent-replay-v1.json'
    with output.open('x') as stream:
        json.dump({'input_family':args.family,'input_sha256':args.sha256,'fixed_parameter':fixed,'fixed_value':value,
                   'independent_ideal_builder_sha256':hashlib.sha256((ROOT/'frontier-20261028-level6-independent-coordinate-ideals.py').read_bytes()).hexdigest(),
                   'operator_integer_scales':whole.SCALES,'independent_ideal_trace':whole.TRACE,'records':results,
                   'status':'PASS_ENTIRE_SELECTED_ACTUAL_QUOTIENT_FAMILIES_AND_FIFTH_ENDPOINTS',
                   'total_shifted_grid_determinants':sum(e.get('shifted_exact_grid_determinants',0) for e in results),
                   'limits':'independent source/ideal/operator implementation, shared exact FLINT arithmetic; named actual free-Levi/PBW and finite-sl3 semisimplicity inputs. Not formal/kernel, independent-model, source-authentication or novelty acceptance.'},stream,indent=2)
        stream.write('\n')
    print('WROTE',output.name,flush=True)


if __name__=='__main__':
    main()
