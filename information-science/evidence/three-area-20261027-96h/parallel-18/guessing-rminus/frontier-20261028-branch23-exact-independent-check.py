#!/usr/bin/env python3
"""Independent exact verification of both thirteen-variable copy branches.

Rebuilds all elemental Shannon rows and the named joint/conditional copy
protocols using integer-scaled entropy values. The publisher parser is used
only to bind its exact source rows, not to generate Shannon/copy checks.
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
CAND={2:('frontier-20261028-affine-exact-branch-2.json','09981982317f1659a9a291dbbc416f77d2ac8a91eac818191048cb0ac9cd7a87'),
      3:('frontier-20261028-affine-exact-branch-3.json','fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0')}
AUDITOR=ROOT/'frontier-20261028-gurpinar-certificate-independent.py'
OUT=ROOT/'frontier-20261028-branch23-exact-independent-check-result.json'
ORIGINAL=tuple('abcdefghij')
N={'a':set('bcdefg'),'b':set('acgij'),'c':set('abdhi'),'d':set('acehj'),'e':set('adfij'),
   'f':set('aeghi'),'g':set('abfhj'),'h':set('cdfgij'),'i':set('bcefh'),'j':set('bdegh')}
GEN=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
CONFIG={
 2:{'aux':("d'1","e'1","g'2"),'copies':[
     ({'d':"d'1",'e':"e'1"},set('abcfghi'),set(ORIGINAL)),
     ({'g':"g'2"},set('abcdfhi')|{"e'1"},set(ORIGINAL)|{"d'1","e'1"})]},
 3:{'aux':("f'3","g'3","h'4"),'copies':[
     ({'f':"f'3",'g':"g'3"},set('abcdehij'),set(ORIGINAL)),
     ({'h':"h'4"},set('abcdefij')|{"f'3"},set(ORIGINAL)|{"f'3","g'3"})]}}


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


def read_values(base,candidate,number):
    aux=CONFIG[number]['aux'];variables=ORIGINAL+aux;idx={v:i for i,v in enumerate(variables)}
    if candidate['branch']!=number or tuple(candidate['variables'])!=variables:raise ValueError('CANDIDATE_BRANCH')
    out={0:Fraction(0)}
    for entry in base['primal_values']:
        labels=entry['entropy_variables']
        if set(labels)<=set(ORIGINAL):
            m=sum(1<<idx[v] for v in labels)
            if not m or m in out:raise ValueError('BASE_DUPLICATE')
            out[m]=Fraction(entry['value'])
    if len(out)!=1024:raise ValueError('BASE_SIZE')
    for entry in candidate['auxiliary_values']:
        labels=entry['entropy_variables']
        if not set(labels)<=set(variables) or not set(labels)&set(aux):raise ValueError('AUX_LABEL')
        m=sum(1<<idx[v] for v in labels)
        if m in out:raise ValueError('AUX_DUPLICATE')
        out[m]=Fraction(entry['value'])
    if len(out)!=8192:raise ValueError('ALL_SIZE')
    return out


def verify(values,number,perms,source=None):
    variables=ORIGINAL+CONFIG[number]['aux'];index={v:i for i,v in enumerate(variables)}
    if len(values)!=8192 or values[0]!=0:raise ValueError('SIZE')
    if values[1023]!=Fraction(1847,276):raise ValueError('OBJECTIVE')
    for v in ORIGINAL:
        b=1<<index[v];nb=sum(1<<index[u] for u in N[v])
        if values[b]>1 or values[nb|b]!=values[nb]:raise ValueError('BASE_CAP_OR_FD')
    for m in range(1,1024):
        for p in perms:
            pm=sum(1<<p[i] for i in range(10) if m>>i&1)
            if values[m]!=values[pm]:raise ValueError('BASE_SYMMETRY')
    scale=lcm(*(x.denominator for x in values.values()));h=[int(values[m]*scale) for m in range(8192)]
    if min(h)<0:raise ValueError('NEGATIVE_ENTROPY')
    full=8191;checks=0
    for i in range(13):
        if h[full]-h[full^(1<<i)]<0:raise ValueError('SHANNON_H')
        checks+=1
    for i,j in combinations(range(13),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            if h[z|a]+h[z|b]-h[z|a|b]-h[z]<0:raise ValueError(('SHANNON_CMI',i,j,z))
            checks+=1
            if not z:break
            z=(z-1)&(full^a^b)
    def mask(labels):return sum(1<<index[v] for v in labels)
    copycount=0
    for mapping,Y,past in CONFIG[number]['copies']:
        olds=tuple(mapping);y=mask(Y);p=mask(past);fresh=mask(mapping.values())
        if Y-set(past) or set(mapping)-past or Y&set(mapping):raise ValueError('BAD_COPY_PROTOCOL')
        for choose in range(1,1<<len(olds)):
            original=mask(olds[i] for i in range(len(olds)) if choose&(1<<i))
            duplicate=mask(mapping[olds[i]] for i in range(len(olds)) if choose&(1<<i))
            z=y
            while True:
                if h[z|original]!=h[z|duplicate]:raise ValueError(('COPY_MARGINAL',number,choose,z))
                copycount+=1
                if not z:break
                z=(z-1)&y
        if h[y|fresh]+h[p]-h[p|fresh]-h[y]!=0:raise ValueError(('COPY_INDEPENDENCE',number))
        copycount+=1
    tight=0
    if source is not None:
        for row in source:
            labels={v for names in row['terms'] for v in names}
            if labels<=set(variables):
                value=sum(c*h[mask(names)] for names,c in row['terms'].items())
                if value!=row['rhs']*scale:raise ValueError(('SOURCE_TIGHT',row['name']))
                tight+=1
    return {'scale_digits':len(str(scale)),'elemental_shannon_checks':checks,
            'copy_equalities':copycount,'source_tight_rows':tight,'base_symmetry_masks':1023*8}


def main():
    base=pin(BASE,BASE_HASH);perms=group()
    spec=spec_from_file_location('publisher_audit',AUDITOR);audit=module_from_spec(spec);spec.loader.exec_module(audit)
    data={k:(ROOT/info[0]).read_bytes() for k,info in audit.FILES.items()}
    for k,(_,digest) in audit.FILES.items():audit.pin(k,data[k],digest)
    source=audit.parse_input(data['layout'],data['text']);audit.validate(source)
    verdicts=[]
    for number in (2,3):
        name,digest=CAND[number];cand=pin(ROOT/name,digest);values=read_values(base,cand,number)
        counts=verify(values,number,perms,source)
        if counts['elemental_shannon_checks']!=159757 or counts['copy_equalities']!={2:642,3:1282}[number] or counts['source_tight_rows']!={2:933,3:1372}[number]:
            raise ValueError(('COUNTS',number,counts))
        controls={}
        def expect(name,mutation):
            changed=dict(values);mutation(changed)
            try:verify(changed,number,perms)
            except (ValueError,KeyError):controls[name]='rejected'
            else:raise ValueError(('CONTROL_ACCEPTED',number,name))
        expect('mutated_first_aux_singleton',lambda h:h.__setitem__(1<<10,h[1<<10]+1))
        expect('mutated_second_copy_singleton',lambda h:h.__setitem__(1<<12,h[1<<12]+1))
        expect('mutated_full_entropy',lambda h:h.__setitem__(8191,h[8191]+Fraction(1,7)))
        expect('missing_aux_coordinate',lambda h:h.pop(1<<10))
        expect('mutated_base_singleton',lambda h:h.__setitem__(1,h[1]+1))
        verdicts.append({'branch':number,'candidate_sha256':digest,'exact_checks':counts,'mutation_controls':controls})
    out={'base_sha256':BASE_HASH,'source_hashes':{k:v[1] for k,v in audit.FILES.items()},'branches':verdicts,
         'all_checked':True,'limits':'Verifies branches 2 and 3 on the same exact original profile only; a combined three-branch/source audit is still required. No entropic realization or improved guessing number follows.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
