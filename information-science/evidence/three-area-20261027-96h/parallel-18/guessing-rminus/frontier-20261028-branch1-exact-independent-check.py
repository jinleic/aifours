#!/usr/bin/env python3
"""Independent exact check of a full first-copy Shannon extension.

Rebuilds all 11-variable elemental rows and the 257 copy equations. The
previously independently audited publisher parser is used only for binding
its exact tight source rows, not for generating the Shannon/copy checks.
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
CAND=ROOT/'frontier-20261028-affine-exact-branch-1.json'
CAND_HASH='1898339bb4ba63c53dbda6dff9603f82414f29645543631bc21d82d752941e37'
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-branch1-exact-independent-check-result.json'
ORIGINAL=tuple('abcdefghij');AUX="b'0";VARS=ORIGINAL+(AUX,)
N={'a':set('bcdefg'),'b':set('acgij'),'c':set('abdh i'.replace(' ','')),
   'd':set('acehj'),'e':set('adfij'),'f':set('aeghi'),
   'g':set('abfhj'),'h':set('cdfgij'),'i':set('bcefh'),'j':set('bdegh')}
GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))


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


def read_values(base,candidate):
    out={0:Fraction(0)};idx={v:i for i,v in enumerate(VARS)};orig=set(ORIGINAL)
    for entry in base['primal_values']:
        labels=entry['entropy_variables']
        if set(labels)<=orig:
            m=sum(1<<idx[v] for v in labels)
            if not m or m in out:raise ValueError('BASE_DUPLICATE')
            out[m]=Fraction(entry['value'])
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for entry in candidate['auxiliary_values']:
        labels=entry['entropy_variables']
        if AUX not in labels or not set(labels)<=set(VARS):raise ValueError('AUX_LABEL')
        m=sum(1<<idx[v] for v in labels)
        if m in out:raise ValueError('AUX_DUPLICATE')
        out[m]=Fraction(entry['value'])
    if len(out)!=2048:raise ValueError('ALL_SIZE')
    return out


def verify(values,perms,source=None):
    if len(values)!=2048 or values[0]!=0:raise ValueError('SIZE')
    if values[1023]!=Fraction(1847,276):raise ValueError('OBJECTIVE')
    for v in ORIGINAL:
        bit=1<<ORIGINAL.index(v);nb=sum(1<<ORIGINAL.index(u) for u in N[v])
        if values[bit]>1 or values[nb|bit]!=values[nb]:raise ValueError('BASE_CAP_OR_FD')
    for m in range(1,1024):
        for p in perms:
            pm=sum(1<<p[i] for i in range(10) if m>>i&1)
            if values[m]!=values[pm]:raise ValueError('BASE_SYMMETRY')
    scale=lcm(*(x.denominator for x in values.values()))
    h=[int(values[m]*scale) for m in range(2048)]
    if min(h)<0:raise ValueError('NEGATIVE_ENTROPY')
    full=2047;checks=0
    for i in range(11):
        if h[full]-h[full^(1<<i)]<0:raise ValueError('SHANNON_H')
        checks+=1
    for i,j in combinations(range(11),2):
        ai,bj=1<<i,1<<j;rest=full^ai^bj;z=rest
        while True:
            if h[z|ai]+h[z|bj]-h[z|ai|bj]-h[z]<0:raise ValueError(('SHANNON_CMI',i,j,z))
            checks+=1
            if not z:break
            z=(z-1)&rest
    Y=sum(1<<ORIGINAL.index(v) for v in 'adefghij');b=1<<ORIGINAL.index('b');aux=1<<10
    z=Y;copycount=0
    while True:
        if h[z|b]!=h[z|aux]:raise ValueError(('COPY_MARGINAL',z))
        copycount+=1
        if not z:break
        z=(z-1)&Y
    if h[Y|aux]+h[1023]-h[1023|aux]-h[Y]!=0:raise ValueError('COPY_INDEPENDENCE')
    copycount+=1
    tight=0
    if source is not None:
        index={v:i for i,v in enumerate(VARS)}
        for row in source:
            labels={v for names in row['terms'] for v in names}
            if labels<=set(VARS):
                value=sum(c*h[sum(1<<index[v] for v in names)] for names,c in row['terms'].items())
                if value!=row['rhs']*scale:raise ValueError(('SOURCE_TIGHT',row['name']))
                tight+=1
    return {'scale_digits':len(str(scale)),'elemental_shannon_checks':checks,
            'copy_equalities':copycount,'source_tight_rows':tight,'base_symmetry_masks':1023*8}


def main():
    base=pin(BASE,BASE_HASH);candidate=pin(CAND,CAND_HASH);values=read_values(base,candidate);perms=group()
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info[0]).read_bytes() for k,info in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);audit.validate(source)
    counts=verify(values,perms,source)
    if counts['elemental_shannon_checks']!=28171 or counts['copy_equalities']!=257 or counts['source_tight_rows']!=623:
        raise ValueError(('COUNTS',counts))
    controls={}
    def expect(name,mutation):
        changed=dict(values);mutation(changed)
        try:verify(changed,perms)
        except (ValueError,KeyError):controls[name]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',name))
    expect('mutated_aux_singleton',lambda h:h.__setitem__(1<<10,h[1<<10]+1))
    expect('mutated_full_entropy',lambda h:h.__setitem__(2047,h[2047]+Fraction(1,7)))
    expect('missing_aux_coordinate',lambda h:h.pop(1<<10))
    expect('mutated_base_singleton',lambda h:h.__setitem__(1,h[1]+1))
    out={'base_sha256':BASE_HASH,'candidate_sha256':CAND_HASH,'source_hashes':{k:v[1] for k,v in audit.FILES.items()},
         'branch':1,'variables':VARS,'exact_checks':counts,'all_checked':True,'mutation_controls':controls,
         'limits':'First-copy Shannon/copy extension of the fixed original profile only; no full three-branch LP primal, entropy realization or guessing-number improvement follows.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
