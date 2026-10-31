#!/usr/bin/env python3
"""Independent exact verification of the coupled 14-variable 1+3 primal with fixed branch-1 profile.

Rebuilds every elemental Shannon row, every named copy equation and seven
inter-branch conditional-independence equations. The publisher parser only
binds previously audited source rows and does not generate these checks.
"""
from collections import deque
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import lcm
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'frontier-20261028-separator-bound-primal.json'
BASE_HASH='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
CAND=ROOT/'frontier-20261028-crossbranch13-one-cut-exact-candidate.json'
CAND_HASH='7769476a34e418e76b2387305533fe688b4d5aee2ec975e8f6b1d8aef311da48'
SHARED=ROOT/'frontier-20261028-crossbranch12-exact-candidate.json'
SHARED_HASH='1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739'
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-crossbranch13-one-cut-independent-check-result.json'
ORIGINAL=tuple('abcdefghij');AUX=("b'0","f'3","g'3","h'4");VARS=ORIGINAL+AUX
N={'a':set('bcdefg'),'b':set('acgij'),'c':set('abdhi'),'d':set('acehj'),'e':set('adfij'),
   'f':set('aeghi'),'g':set('abfhj'),'h':set('cdfgij'),'i':set('bcefh'),'j':set('bdegh')}
GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
COPIES=[({'b':"b'0"},set('adefghij'),set(ORIGINAL)),
        ({'f':"f'3",'g':"g'3"},set('abcdehij'),set(ORIGINAL)),
        ({'h':"h'4"},set('abcdefij')|{"f'3"},set(ORIGINAL)|{"f'3","g'3"})]


def pin(path,h):
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=h:raise ValueError(('HASH',path.name))
    return json.loads(raw)


def group():
    edges={tuple(sorted((ORIGINAL.index(u),ORIGINAL.index(v)))) for u,ns in N.items() for v in ns}
    if len(edges)!=26 or any(u not in N[v] for u,ns in N.items() for v in ns):raise ValueError('GRAPH')
    for p in GEN:
        if {tuple(sorted((p[u],p[v]))) for u,v in edges}!=edges:raise ValueError('AUTOMORPHISM')
    seen={tuple(range(10))};q=deque(seen)
    while q:
        p=q.popleft()
        for g in GEN:
            z=tuple(g[p[i]] for i in range(10))
            if z not in seen:seen.add(z);q.append(z)
    if len(seen)!=8:raise ValueError('GROUP')
    return seen


def read_values(base,shared,candidate):
    if tuple(candidate['variables'])!=VARS:raise ValueError('VARIABLES')
    idx={v:i for i,v in enumerate(VARS)};out={0:Fraction(0)}
    for e in base['primal_values']:
        labels=e['entropy_variables']
        if set(labels)<=set(ORIGINAL):
            m=sum(1<<idx[v] for v in labels)
            if not m or m in out:raise ValueError('BASE_DUPLICATE')
            out[m]=Fraction(e['value'])
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for e in shared['auxiliary_values']:
        labels=e['entropy_variables']
        if set(labels)<=set(ORIGINAL)|{"b'0"}:
            if "b'0" not in labels:raise ValueError('SHARED_LABEL')
            m=sum(1<<idx[v] for v in labels)
            if m in out:raise ValueError('SHARED_DUPLICATE')
            out[m]=Fraction(e['value'])
    if len(out)!=2048:raise ValueError('SHARED_SIZE')
    for e in candidate['auxiliary_values']:
        labels=e['entropy_variables']
        if not set(labels)<=set(VARS) or not set(labels)&set(AUX[1:]):raise ValueError('AUX_LABEL')
        m=sum(1<<idx[v] for v in labels)
        if m in out:raise ValueError('AUX_DUPLICATE')
        out[m]=Fraction(e['value'])
    if len(out)!=16384:raise ValueError('ALL_SIZE')
    return out


def verify(values,perms,source=None):
    index={v:i for i,v in enumerate(VARS)}
    if len(values)!=16384 or values[0]!=0:raise ValueError('SIZE')
    if values[1023]!=Fraction(1847,276):raise ValueError('OBJECTIVE')
    for v in ORIGINAL:
        b=1<<index[v];nb=sum(1<<index[u] for u in N[v])
        if values[b]>1 or values[nb|b]!=values[nb]:raise ValueError('BASE_CAP_OR_FD')
    for m in range(1,1024):
        for p in perms:
            pm=sum(1<<p[i] for i in range(10) if m>>i&1)
            if values[m]!=values[pm]:raise ValueError('BASE_SYMMETRY')
    scale=lcm(*(x.denominator for x in values.values()));h=[int(values[m]*scale) for m in range(16384)]
    if min(h)<0:raise ValueError('NEGATIVE_ENTROPY')
    full=16383;checks=0
    for i in range(14):
        if h[full]-h[full^(1<<i)]<0:raise ValueError('SHANNON_H')
        checks+=1
    for i,j in combinations(range(14),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            if h[z|a]+h[z|b]-h[z|a|b]-h[z]<0:raise ValueError(('SHANNON_CMI',i,j,z))
            checks+=1
            if not z:break
            z=(z-1)&(full^a^b)
    def mask(labels):return sum(1<<index[v] for v in labels)
    copycount=0
    for mapping,Y,past in COPIES:
        olds=tuple(mapping);y=mask(Y);p=mask(past);fresh=mask(mapping.values())
        if Y-past or set(mapping)-past or Y&set(mapping):raise ValueError('BAD_COPY_PROTOCOL')
        for choose in range(1,1<<len(olds)):
            original=mask(olds[i] for i in range(len(olds)) if choose&(1<<i))
            duplicate=mask(mapping[olds[i]] for i in range(len(olds)) if choose&(1<<i))
            z=y
            while True:
                if h[z|original]!=h[z|duplicate]:raise ValueError(('COPY_MARGINAL',choose,z))
                copycount+=1
                if not z:break
                z=(z-1)&y
        if h[y|fresh]+h[p]-h[p|fresh]-h[y]!=0:raise ValueError('COPY_INDEPENDENCE')
        copycount+=1
    # The two whole auxiliary branches are conditionally independent given X_V.
    original=mask(ORIGINAL);first=mask(("b'0",));second=("f'3","g'3","h'4");cross=0
    for choice in range(1,8):
        picked=mask(second[i] for i in range(3) if choice&(1<<i))
        if h[original|first]+h[original|picked]-h[original|first|picked]-h[original]!=0:
            raise ValueError(('CROSS_INDEPENDENCE',choice))
        cross+=1
    tight=0
    if source is not None:
        for row in source:
            labels={v for names in row['terms'] for v in names}
            if labels<=set(VARS):
                value=sum(c*h[mask(names)] for names,c in row['terms'].items())
                if value!=row['rhs']*scale:raise ValueError(('SOURCE_TIGHT',row['name']))
                tight+=1
    return {'scale_digits':len(str(scale)),'elemental_shannon_checks':checks,'copy_equalities':copycount,
            'cross_branch_independence_equalities':cross,'source_tight_rows':tight,'base_symmetry_masks':1023*8}


def main():
    base=pin(BASE,BASE_HASH);shared=pin(SHARED,SHARED_HASH);candidate=pin(CAND,CAND_HASH);values=read_values(base,shared,candidate);perms=group()
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info[0]).read_bytes() for k,info in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);audit.validate(source)
    counts=verify(values,perms,source)
    cutfile=ROOT/'frontier-20261028-cross-pair-farkas-independent-check-result.json';cutraw=cutfile.read_bytes()
    if sha256(cutraw).hexdigest()!='199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45':raise ValueError('CUT_HASH')
    cut=json.loads(cutraw);dvalues={}
    for e in shared['auxiliary_values']:
        labs=e['entropy_variables']
        if "d'1" in labs and set(labs)<=set(ORIGINAL)|{"d'1"}:
            m=sum(1<<ORIGINAL.index(v) for v in labs if v in ORIGINAL);dvalues[m]=Fraction(e['value'])
    if len(dvalues)!=1024:raise ValueError('D_VALUES')
    cutvalue=Fraction(0)
    for mask,coefficient in cut['exact_identity']['known_terms']:
        if mask&3072==3072:raise ValueError('CUT_CROSS_TERM')
        orig=mask&1023
        x=dvalues[orig] if mask&1024 else values[orig|(1<<11)] if mask&2048 else values[orig]
        cutvalue+=Fraction(coefficient)*x
    if cutvalue!=Fraction(4751,1725000) or cutvalue<0:raise ValueError(('CUT_VALUE',str(cutvalue)))
    if counts['elemental_shannon_checks']!=372750 or counts['copy_equalities']!=1539 or counts['cross_branch_independence_equalities']!=7 or counts['source_tight_rows']!=1491:
        raise ValueError(('COUNTS',counts))
    controls={}
    def expect(name,mutation):
        changed=dict(values);mutation(changed)
        try:verify(changed,perms)
        except (ValueError,KeyError):controls[name]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',name))
    expect('mutated_first_branch_singleton',lambda h:h.__setitem__(1<<10,h[1<<10]+1))
    expect('mutated_second_branch_singleton',lambda h:h.__setitem__(1<<11,h[1<<11]+1))
    expect('mutated_second_copy_singleton',lambda h:h.__setitem__(1<<13,h[1<<13]+1))
    expect('mutated_full_entropy',lambda h:h.__setitem__(16383,h[16383]+Fraction(1,7)))
    expect('missing_cross_coordinate',lambda h:h.pop((1<<10)|(1<<11)))
    expect('mutated_base_singleton',lambda h:h.__setitem__(1,h[1]+1))
    out={'base_sha256':BASE_HASH,'shared_branch1_sha256':SHARED_HASH,'candidate_sha256':CAND_HASH,'source_hashes':{k:v[1] for k,v in audit.FILES.items()},
         'variables':VARS,'exact_checks':counts,'one_cross_copy_cut_value':str(cutvalue),'cut_receipt_sha256':'199a7471622c6c3085a669e2b43e7235676e680ee7e8cb3fa8f636449a1aff45','all_checked':True,'mutation_controls':controls,
         'limits':'Coupled branches 1+3 with the branch1 profile fixed from cross12 and one valid d1/f3 cross-copy cut; no all-cross Shannon or entropic realization is asserted. No entropic realization or global guessing-number improvement follows.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
