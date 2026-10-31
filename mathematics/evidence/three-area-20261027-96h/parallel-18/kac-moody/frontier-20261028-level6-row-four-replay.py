#!/usr/bin/env python3
"""Independent whole-ideal/source/target replay of a fourth-row L6 family.

Regenerates the full Serre ideal with the independent string-word/tree-Jacobi
engine; checks both-way equality with every serialized source/target ideal
space; reselects the actual primitive quotient basis; verifies D3 containment
and every affine selected entry; checks the whole determinant polynomial on a
shifted unisolvent grid. Integer root exclusion uses a fresh prime and own
integer Hensel code. FLINT exact determinant/gcd arithmetic is shared, not a
claim of independent-model or formal verification.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-fastalgebra'))
import flint


def load(name,file):
    sp=importlib.util.spec_from_file_location(name,ROOT/file)
    m=importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


r=load('independent_helpers','frontier-20261028-level6-two-minor-general-replay.py')
character=load('character_only','frontier-20261028-level6-positive-small-replay.py').character
ind=r.ind


def parsed(rows):
    return [{w:Q(c) for w,c in row.items() if Q(c)} for row in rows]


def projection(rows):
    pairs=sorted((min(row),row) for row in rows)
    assert len({w for w,row in pairs})==len(pairs)
    assert all(row[w]==1 for w,row in pairs)
    def reduce(vector):
        result=dict(vector)
        for w,row in pairs:
            c=result.get(w,Q(0))
            if c:
                for word,coef in row.items():
                    result[word]=result.get(word,Q(0))-c*coef
        return {w:c for w,c in result.items() if c}
    for row in rows:
        assert not reduce(row)
    return reduce


def same_space(computed,claimed):
    fresh=ind.ind.ReducedSpace(claimed)
    assert len(computed)==len(fresh)==len(claimed)
    for row in claimed:
        assert not computed.remainder(row)
    for row in computed.pivots.values():
        assert not fresh.remainder(row)
    return fresh


def integer_roots(poly):
    repeated=poly.gcd(poly.derivative())
    W,rem=divmod(poly,repeated)
    assert not rem and W*repeated==poly
    if repeated.degree()>0:
        modulus=flint.fmpq_poly(repeated)
        base=flint.fmpq_poly(W)%modulus
        value=flint.fmpq_poly([1])
        exponent=poly.degree()
        while exponent:
            if exponent&1:
                value=(value*base)%modulus
            exponent//=2
            if exponent:
                base=(base*base)%modulus
        assert not value, 'repeated factor root coverage failed'
    cs=[int(c) for c in W]
    ds=[i*cs[i] for i in range(1,len(cs))]
    bound=1+(max(abs(c) for c in cs[:-1])+abs(cs[-1])-1)//abs(cs[-1])
    p=5000
    while True:
        p+=1
        if all(p%d for d in range(2,math.isqrt(p)+1)) and cs[-1]%p and len(r.gcd_modp(cs,ds,p))==1:
            break
    mod=p
    while mod<=2*bound:
        mod*=p
    roots=[]
    residues=[a for a in range(p) if r.ev(cs,a,p)==0]
    for a in residues:
        for _ in range(64):
            if r.ev(cs,a,mod)==0:
                break
            a=(a-r.ev(cs,a,mod)*pow(r.ev(ds,a,mod),-1,mod))%mod
        assert r.ev(cs,a,mod)==0
        a=a if a<=mod//2 else a-mod
        if abs(a)<=bound and r.ev(cs,a)==0:
            roots.append(a)
    return sorted(roots),p


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--fixed',choices=['r','s'],required=True)
    ap.add_argument('--sha256',required=True)
    args=ap.parse_args()
    name=f'frontier-20261028-level6-{args.fixed}4-quotient-family-v1.json'
    raw=(ROOT/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==args.sha256
    C=json.loads(raw)
    out=ROOT/f'frontier-20261028-level6-{args.fixed}4-quotient-independent-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    def params(t):
        return (4,6+t) if args.fixed=='r' else (6+t,4)
    rr,ss=params(0)
    spaces=ind.ideal_spaces((6,6,6),rr,ss)
    char=character()
    summaries=[]
    for pin,e in zip(C['inputs'],C['records']):
        praw=(ROOT/pin['file']).read_bytes()
        assert hashlib.sha256(praw).hexdigest()==pin['sha256']
        P=json.loads(praw)
        degree=tuple(e['degree'])
        a,b,n=degree
        assert tuple(P['source_words'])==ind.lyndon_words(degree)
        basis=[ind.ind.standard_bracket(w) for w in P['source_words']]
        assert len(basis)==char[a,b] and all(v.get(w)==1 and min(v)==w for w,v in zip(P['source_words'],basis))
        vectors=[ind.combine(basis,co) for co in P['horizontal_kernel_coefficients']]
        expected=char.get((a,b),0)-char.get((a-1,b),0)-char.get((a,b-1),0)+char.get((a-2,b-1),0)+char.get((a-1,b-2),0)-char.get((a-2,b-2),0)
        assert len(vectors)==expected
        coefs=[{int(i):Q(q) for i,q in co.items()} for co in P['horizontal_kernel_coefficients']]
        assert len(ind.ind.ReducedSpace(coefs))==expected
        for v in vectors:
            for g in ('f1','f2'):
                assert not ind.act(v,g,rr,ss)
        I=spaces.get(degree,ind.ind.ReducedSpace())
        T=spaces.get((a,b,5),ind.ind.ReducedSpace())
        claimedI=parsed(e['source_ideal_rows'])
        claimedT=parsed(e['target_ideal_rows'])
        same_space(I,claimedI)
        same_space(T,claimedT)
        assert len(I)==e['full_source_ideal_dimension'] and len(T)==e['full_target_ideal_dimension']
        reduce=projection(claimedT)
        for row in T.pivots.values():
            assert not reduce(row)
        quotient=ind.ind.ReducedSpace(I.pivots.values())
        selected=[]
        for j,v in enumerate(vectors):
            if quotient.insert(v):
                selected.append(j)
        assert selected==e['retained_free_primitive_indices']
        k=len(selected)
        assert k==e['actual_primitive_quotient_dimension']
        for t in (0,1):
            rr_,ss_=params(t)
            for row in I.pivots.values():
                assert not reduce(ind.d3(row,degree,rr_,ss_))
        chosen=[vectors[j] for j in selected]
        base=[reduce(ind.d3(v,degree,*params(0))) for v in chosen]
        next_=[reduce(ind.d3(v,degree,*params(1))) for v in chosen]
        if k==0:
            assert e['status']=='ZERO_ACTUAL_PRIMITIVE_SOURCE'
            summaries.append({'degree':list(degree),'actual_primitive_dimension':0})
            continue
        matrix=[]
        for word in e['selected_target_words']:
            matrix.append([[Q(base[j].get(word,0)),Q(next_[j].get(word,0))-Q(base[j].get(word,0))] for j in range(k)])
        assert matrix==[[[Q(c) for c in v] for v in row] for row in e['matrix']]
        scales=[math.lcm(*(c.denominator for v in row for c in v)) for row in matrix]
        integers=[[[int(c*sc) for c in v] for v in row] for row,sc in zip(matrix,scales)]
        poly=[Q(c) for c in e['determinant_coefficients_low_to_high']]
        for t in range(1,k+2):
            determinant=flint.fmpz_mat([[u+t*v for u,v in row] for row in integers]).det()
            assert Q(int(determinant),math.prod(scales))==sum(c*t**i for i,c in enumerate(poly))
        assert sum(c*(-1)**i for i,c in enumerate(poly))!=0, 'fifth endpoint vanishes'
        if poly[0] and (all(c>=0 for c in poly) or all(c<=0 for c in poly)):
            roots,prime=[],None
        else:
            den=math.lcm(*(c.denominator for c in poly))
            Z=flint.fmpz_poly([int(c*den) for c in poly])
            roots,prime=integer_roots(Z)
            assert roots==e['integer_minor_roots']
        assert not any(t>=0 for t in roots)
        summaries.append({'degree':list(degree),'source_ideal_dimension':len(I),'target_ideal_dimension':len(T),
                          'actual_primitive_dimension':k,'exact_shifted_grid_determinants':k+1,
                          'nonnegative_integer_minor_roots':[],
                          'all_integer_roots_when_Hensel_used':roots if prime else None,
                          'exclusion_method':'independent Hensel' if prime else 'one-sign coefficients',
                          'second_hensel_prime':prime,'endpoint_minus_one_nonzero':True})
        print('PASS actual quotient',args.fixed,degree,'source',k,'ideals',len(I),len(T),flush=True)
    assert len(summaries)==7
    with out.open('x') as stream:
        json.dump({'input_sha256':args.sha256,'fixed_parameter':args.fixed,'fixed_value':4,'records':summaries,
                   'status':'PASS_ALL_SEVEN_WHOLE_IDEAL_SOURCE_TARGET_QUOTIENT_FAMILIES',
                   'scope':'independent tree-Jacobi/full Serre ideals and source/target projection; FLINT determinant/gcd arithmetic shared; named finite-Levi/actual-source interfaces'},stream,indent=2)
        stream.write('\n')
    print('WROTE',out.name,flush=True)


if __name__=='__main__':
    main()
