#!/usr/bin/env python3
"""Independent six-fiber incidence replay via12-stub partitions and integer products.

No producer code is read or imported. Families are independently generated as
set partitions of twelve edge-end stubs; loops are forbidden and every vertex
has degree>=2. Complete compatible triples are enumerated by numpy int64 matrix
products (sum<=6), not compatible-column bitmask tests. Every supplied structural
certificate is directly checked and all triple coverage is exact.
"""
import argparse
from collections import Counter
from copy import deepcopy
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np


class CertificateError(ValueError):pass


def generate_families():
    result={r:set() for r in range(2,7)};nodes=0
    def visit(pos,blocks):
        nonlocal nodes
        nodes+=1;remaining=12-pos
        if sum(x.bit_count()==1 for x in blocks)>remaining:return
        if pos==12:
            if len(blocks) in result and all(x.bit_count()>=2 for x in blocks):result[len(blocks)].add(tuple(sorted(blocks)))
            return
        bit=1<<(pos//2)
        for i,x in enumerate(blocks):
            if x&bit:continue
            new=blocks[:];new[i]=x|bit;visit(pos+1,new)
        if len(blocks)<6:visit(pos+1,blocks+[bit])
    visit(0,[])
    return {r:sorted(F) for r,F in result.items()},nodes


def matrices(F,r):
    out=np.zeros((len(F),6,r),dtype=np.int64)
    for k,cols in enumerate(F):
        for j,c in enumerate(cols):
            for g in range(6):out[k,g,j]=int(bool(c>>g&1))
    if not np.all(out.sum(axis=2)==2) or not np.all(out.sum(axis=1)>=2):raise CertificateError('family incidence invariant')
    return out


def compatibility(A,B):
    out=np.zeros((len(A),len(B)),dtype=np.bool_)
    for i,M in enumerate(A):
        products=np.einsum('gi,kgj->kij',M,B)
        out[i]=np.all((products==0)|(products==2),axis=(1,2))
    return out


def rowsets(cols):return [{j for j,c in enumerate(cols) if c>>g&1} for g in range(6)]


def validate_certificate(rec,F):
    sizes=tuple(rec['partner_sizes']);indices=tuple(rec['class_indices'])
    if len(sizes)!=3 or len(indices)!=3:raise CertificateError('invalid triple index shape')
    try:mats=[rowsets(F[r][i]) for r,i in zip(sizes,indices)]
    except (KeyError,IndexError) as exc:raise CertificateError('invalid incidence class index') from exc
    cert=rec['certificate'];kind=cert['kind']
    if kind=='COMMON_ROW_PAIRING':
        pairs=cert['pairs']
        if len(pairs)!=3 or any(len(p)!=2 for p in pairs) or sorted(x for p in pairs for x in p)!=list(range(6)):
            raise CertificateError('common pairing not a partition')
        if any(M[g]!=M[h] for M in mats for g,h in pairs):raise CertificateError('common pairing row mismatch')
    elif kind=='TWO_SINGLETON_INTERSECTIONS':
        fibers=cert['fibers'];coords=cert['partner_coordinates']
        if len(fibers)!=2 or len(set(fibers))!=2 or any(type(x)!=int or not 0<=x<6 for x in fibers):raise CertificateError('invalid fiber pair')
        if len(coords)!=2 or len(set(coords))!=2 or any(type(x)!=int or not 0<=x<3 for x in coords):raise CertificateError('invalid partner coordinate pair')
        g,h=fibers
        if any(len(mats[j][g]&mats[j][h])!=1 for j in coords):raise CertificateError('intersection not singleton')
    else:raise CertificateError('unknown certificate kind')
    return kind


def verify_records(records,F,expected):
    seen=set();counts=Counter()
    for r in records:
        key=(tuple(r['partner_sizes']),tuple(r['class_indices']))
        if key not in expected or key in seen:raise CertificateError('unexpected or duplicate triple')
        seen.add(key);counts[validate_certificate(r,F)]+=1
    if seen!=expected:raise CertificateError('triple coverage mismatch')
    return counts


def expect(call,reason):
    try:call()
    except CertificateError as exc:
        if str(exc)!=reason:raise ValueError(f'wrong rejection {exc}; expected {reason}')
        return str(exc)
    raise ValueError('mutation accepted')


def main():
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('out',type=Path);a=p.parse_args();raw=a.candidate.read_bytes();src=json.loads(raw)
    F,nodes=generate_families()
    for r in F:
        if F[r]!=[tuple(x) for x in src['incidence_classes'][str(r)]]:raise CertificateError('incidence family coverage mismatch')
    counts={r:len(F[r]) for r in F}
    if counts!={2:1,3:115,4:1150,5:1295,6:130}:raise CertificateError('unexpected family counts')
    M={r:matrices(F[r],r) for r in F};adj={}
    for r,s in itertools.combinations_with_replacement(range(2,7),2):adj[r,s]=compatibility(M[r],M[s])
    def A(r,s):return adj[r,s] if r<=s else adj[s,r].T
    profiles=[P for P in itertools.combinations_with_replacement(range(2,7),3) if all(x*y>=12 for x,y in itertools.combinations(P,2))]
    expected=set();profile_counts={}
    for sizes in profiles:
        r,s,t=sizes;BC=A(r,s);BD=A(r,t);CD=A(s,t);total=0
        ii,jj=np.nonzero(BC)
        for i,j in zip(ii,jj):
            for k in np.nonzero(BD[i]&CD[j])[0]:expected.add((sizes,(int(i),int(j),int(k))));total+=1
        profile_counts[','.join(map(str,sizes))]=total
    result_counts=verify_records(src['records'],F,expected)
    if len(expected)!=1035 or result_counts!={'COMMON_ROW_PAIRING':1005,'TWO_SINGLETON_INTERSECTIONS':30}:raise CertificateError('unexpected certificate counts')
    controls=[]
    common=deepcopy(next(r for r in src['records'] if r['certificate']['kind']=='COMMON_ROW_PAIRING'))
    common['certificate']['pairs'][0][1]=common['certificate']['pairs'][0][0]
    controls.append(expect(lambda:validate_certificate(common,F),'common pairing not a partition'))
    bad=deepcopy(next(r for r in src['records'] if r['certificate']['kind']=='TWO_SINGLETON_INTERSECTIONS'))
    bad['certificate']['fibers'][1]=bad['certificate']['fibers'][0]
    controls.append(expect(lambda:validate_certificate(bad,F),'invalid fiber pair'))
    bad2=deepcopy(src['records'][0]);bad2['certificate']['kind']='UNKNOWN'
    controls.append(expect(lambda:validate_certificate(bad2,F),'unknown certificate kind'))
    controls.append(expect(lambda:verify_records(src['records'][:-1],F,expected),'triple coverage mismatch'))
    result={'candidate_sha256':hashlib.sha256(raw).hexdigest(),'independent_set_partition_nodes':nodes,
      'independent_family_counts':counts,'profile_compatible_triples':profile_counts,
      'compatible_triples_total':len(expected),'certificate_counts':dict(result_counts),
      'intended_mutation_controls':controls,
      'scope':'Exact finite incidence coverage and structural certificates only. No original AME/no-Hamming-one/no-OLS composition or formal proof.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
