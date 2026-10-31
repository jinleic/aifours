#!/usr/bin/env python3
"""Independent exact verification of the frozen sparse-core primal witness.

Checks original Shannon/FD/symmetry, source rows and cap constraints, then
scans all disjoint original-variable block substitutions and all n>=1 with a
quadratic-minimum method different from the producing scanner. This is an
outer-relaxation witness, not an entropic law or a global bound.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
spec=spec_from_file_location('cert2',ROOT/'frontier-20261028-gurpinar-certificate-independent.py')
cert=module_from_spec(spec);spec.loader.exec_module(cert)
PRIMAL=ROOT/'frontier-20261028-all-order-primal-frozen.json'
OUTPUT=ROOT/'frontier-20261028-all-order-primal-independent-result.json'
EXPECTED='af431478fdad330f5f79fa416bdcaf1c56a56fb30ed4855fc65b50d1cac50545'


def key(mask):return tuple(cert.BASE[i] for i in range(10) if mask & (1<<i))


def check_original(values,source):
    def H(mask):return Fraction(0) if not mask else values[key(mask)]
    if any(value<0 for value in values.values()):raise ValueError('NEGATIVE_COORDINATE')
    if any(H(1<<v)>1 for v in range(10)):raise ValueError('SINGLETON_CAP')
    if H(1023)!=Fraction(1847,276):raise ValueError('OBJECTIVE')
    checked_source=0
    for row in source:
        value=sum((Fraction(coef)*values[s] for s,coef in row['terms'].items()),Fraction(0))
        relation=row['relation'];rhs=Fraction(row['rhs'])
        if (relation=='=' and value!=rhs) or (relation=='>=' and value<rhs) or (relation=='<=' and value>rhs):
            raise ValueError(('SOURCE_ROW',row['name'],str(value)))
        checked_source+=1
    for i in range(10):
        if H(1023)<H(1023^(1<<i)):raise ValueError(('SHANNON_MONOTONIC',i))
    cmi_count=0
    for i,j in combinations(range(10),2):
        remainder=1023^(1<<i)^(1<<j);z=remainder
        while True:
            value=H(z|(1<<i))+H(z|(1<<j))-H(z|(1<<i)|(1<<j))-H(z)
            if value<0:raise ValueError(('SHANNON_CMI',i,j,z,str(value)))
            cmi_count+=1
            if z==0:break
            z=(z-1)&remainder
    fd_count=0
    for v,neighbours in cert.NEIGHBOURS.items():
        mask=sum(1<<cert.BASE.index(u) for u in neighbours)
        if H(mask|(1<<cert.BASE.index(v)))!=H(mask):raise ValueError(('FD',v))
        fd_count+=1
    symmetry_count=0
    for permutation in cert.GENS:
        for mask in range(1,1024):
            mapped=sum(1<<permutation[i] for i in range(10) if mask & (1<<i))
            if H(mask)!=H(mapped):raise ValueError(('SYMMETRY',mask,mapped))
            symmetry_count+=1
    return {'source_rows':checked_source,'conditional_entropy_rows':10,
            'elemental_CMI_rows':cmi_count,'original_FDs':fd_count,
            'generator_symmetry_equalities':symmetry_count}


def all_n_scan(h):
    # Independent base-6 enumeration: six low variables, four high variables.
    # For d>0 check the two integers adjacent to the real quadratic vertex;
    # for d=0 use its linear slope. No producer scanner is imported.
    started=time.monotonic();nlow=6**6
    codes=np.arange(nlow,dtype=np.int64);low=[np.zeros(nlow,dtype=np.int64) for _ in range(5)]
    t=codes.copy()
    for i in range(6):
        digit=t%6;t//=6
        for j in range(5):low[j]|=np.where(digit==j+1,1<<i,0)
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    checked=0; min_twice=None;max_n=1
    for code in range(6**4):
        t=code;high=[0]*5
        for i in range(6,10):
            digit=t%6;t//=6
            if digit:high[digit-1]|=1<<i
        masks=[low[j]|high[j] for j in range(5)]
        valid=(masks[0]>0)&(masks[1]>0)&(masks[2]>0)&(masks[3]>0)&(masks[0]<masks[1])
        A,B,C,D,Z=(x[valid] for x in masks);checked+=len(A)
        if not len(A):continue
        a=I(A,B,C|Z)
        c=a+I(A,B,D|Z)+I(C,D,Z)-I(A,B,Z)
        d=I(A,C,B|Z)+I(B,C,A|Z)
        if np.any(a<0) or np.any(d<0):raise ValueError('NEGATIVE_SHANNON_COMPONENT')
        if np.any((d==0)&(c<0)):
            j=int(np.flatnonzero((d==0)&(c<0))[0])
            raise ValueError(('NEGATIVE_LINEAR_SLOPE',*[int(x[j]) for x in (A,B,C,D,Z)]))
        n1=np.ones(len(A),dtype=np.int64);nz=d>0
        n1[nz]=np.maximum(1,np.floor_divide(-(2*c[nz]+d[nz]),2*d[nz]))
        n2=n1+1;max_n=max(max_n,int(n2.max()))
        maximum=int(max(np.max(np.abs(a)),np.max(np.abs(c)),np.max(np.abs(d)),1))
        if 2*maximum*(max_n+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
        q1=2*a+2*n1*c+n1*(n1+1)*d
        q2=2*a+2*n2*c+n2*(n2+1)*d
        least=int(min(q1.min(),q2.min()));min_twice=least if min_twice is None else min(min_twice,least)
        if least<0:raise ValueError(('FAMILY_VIOLATION',least))
    expected=(6**10-4*5**10+6*4**10-4*3**10+2**10)//2
    if checked!=expected:raise ValueError(('ENUMERATION_COUNT',checked,expected))
    return {'disjoint_substitutions_mod_AB_swap':checked,
            'positive_integers_n':'all, via exact quadratic-minimum check',
            'min_twice_slack_scaled':min_twice,'max_tested_vertex_neighbor_n':max_n,
            'elapsed_s':time.monotonic()-started}


def main():
    t=time.monotonic();raw=PRIMAL.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    data=json.loads(raw);items=data['primal_values']
    values={tuple(x['entropy_variables']):Fraction(x['value']) for x in items}
    if len(values)!=len(items):raise ValueError('DUPLICATE_COORDINATE')
    rawsrc={name:(ROOT/info[0]).read_bytes() for name,info in cert.FILES.items()}
    for name,(_,digest) in cert.FILES.items():cert.pin(name,rawsrc[name],digest)
    source=cert.parse_input(rawsrc['layout'],rawsrc['text'])
    exact=check_original(values,source)
    fractions=[Fraction(0)]+[values[key(m)] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in fractions));integer=[int(x*scale) for x in fractions]
    if max(map(abs,integer))>=10**8:raise ValueError('INTEGER_RANGE')
    family=all_n_scan(np.array(integer,dtype=np.int64))
    # Focused in-memory controls: known cap and target corruptions must be rejected.
    controls=[]
    for tag,column,value,expected in (('cap',('a',),Fraction(2),'SINGLETON_CAP'),
                                      ('objective',tuple(cert.BASE),Fraction(7),'OBJECTIVE')):
        mutated=dict(values);mutated[column]=value
        try:check_original(mutated,source)
        except ValueError as exc:
            if str(exc)!=expected:raise ValueError(('MUTATION_WRONG_REASON',tag,str(exc)))
            controls.append({'mutation':tag,'expected':expected,'observed':str(exc)})
        else:raise ValueError(('MUTATION_ACCEPTED',tag))
    out={'primal_sha256':EXPECTED,'coordinates':len(values),'base_scale':scale,
         'exact_source_and_original_rows':exact,'exact_objective':'1847/276',
         'all_disjoint_blocks_all_positive_n':family,'mutation_controls':controls,
         'total_elapsed_s':time.monotonic()-t,
         'limits':'This is a non-entropic-feasibility-unestablished witness for the 1920-source-row core, not the full three-branch LP or the true guessing-number problem. Only disjoint A,B,C,D,Z substitutions of the one F_n family are covered.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
