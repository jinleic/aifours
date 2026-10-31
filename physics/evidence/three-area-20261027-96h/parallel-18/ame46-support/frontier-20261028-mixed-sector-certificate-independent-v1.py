#!/usr/bin/env python3
"""Independent modular replay of mixed-sector homogeneous resultant certificates.

Direct determinant evaluation at 32 points verifies each degree<=31 polynomial;
a separate integer Gauss-Jordan routine verifies each 62x62 resultant. NumPy
is used solely for bounded int64 modular row operations, never floating point.
"""
import argparse
import copy
import hashlib
import itertools
import json
from math import isqrt
from pathlib import Path
import re
import sys
import numpy as np

P=257; DEG=31


class CertificateError(ValueError):pass


def load_table(path):
    raw=path.read_bytes();out={};cells=[]
    for line in raw.decode('utf-8').splitlines():
        if not line or line.startswith('#'):continue
        fields=line.split()
        if len(fields)<3 or not all(re.fullmatch('[0-5]',v) for v in fields[:2]):raise CertificateError('bad cell')
        a,b=map(int,fields[:2]);cells.append((a,b))
        for token in fields[2:]:
            if not re.fullmatch(r'[+\-s][0-5][0-5]',token):raise CertificateError('bad token')
            key=(a,b,int(token[1]),int(token[2]))
            if key in out:raise CertificateError('duplicate coefficient')
            out[key]=(0,1) if token[0]=='s' else (1 if token[0]=='+' else -1,0)
    if cells!=list(itertools.product(range(6),repeat=2)) or len(out)!=60:raise CertificateError('wrong table coverage')
    return out,hashlib.sha256(raw).hexdigest()


def elimination(matrix,p,need_det=False):
    a=np.array(matrix,dtype=np.int64,copy=True)%p;rows,cols=a.shape
    rank=0;det=1
    for col in range(cols):
        hits=np.flatnonzero(a[rank:,col])
        if not len(hits):
            if need_det:return 0
            continue
        pivot=rank+int(hits[0])
        if pivot!=rank:
            a[[rank,pivot],:]=a[[pivot,rank],:]
            det=(-det)%p
        v=int(a[rank,col]);det=det*v%p;inv=pow(v,-1,p)
        if rank+1<rows:
            factors=(a[rank+1:,col]*inv)%p
            a[rank+1:,col:]=(a[rank+1:,col:]-factors[:,None]*a[rank,col:])%p
        rank+=1
        if rank==rows:break
    return det if need_det else rank


def pencil(tensor,free,h,k):
    a,b=free; wed=list(itertools.combinations(range(6),2));widx={v:i for i,v in enumerate(wed)}
    mats=[np.zeros((60,36),dtype=np.int64),np.zeros((60,36),dtype=np.int64)]
    count=0
    for x,(r,s) in tensor.items():
        if x[h] not in (1,2) or x[k] not in (0,3,4,5):continue
        if s or r not in (-1,1):raise CertificateError('unexpected nonintegral mixed-sector coefficient')
        count+=1; av=x[a];bv=x[b];kv=(0,3,4,5).index(x[k]);m=mats[x[h]-1]
        for t in range(6):
            if t==av:continue
            pos=(min(av,t),max(av,t));sgn=1 if av<t else -1
            m[widx[pos]*4+kv,t*6+bv]+=sgn*r
    if count!=16:raise CertificateError('mixed sector not 16 terms')
    return mats


def poly_eval(coeffs,x,p):
    y=0
    for c in reversed(coeffs):y=(y*x+c)%p
    return y


def verify_minor(mats,minor):
    rows=minor['rows'];cols=minor['cols'];f=minor['polynomial']
    if len(rows)!=DEG or len(set(rows))!=DEG or any(not 0<=v<60 for v in rows):raise CertificateError('minor row indices')
    if len(cols)!=DEG or len(set(cols))!=DEG or any(not 0<=v<36 for v in cols):raise CertificateError('minor col indices')
    if len(f)>DEG+1 or any(type(x)!=int or not 0<=x<P for x in f):raise CertificateError('minor polynomial encoding')
    sub0=mats[0][np.ix_(rows,cols)];sub1=mats[1][np.ix_(rows,cols)]
    for t in range(DEG+1):
        if elimination(sub0+t*sub1,P,True)!=poly_eval(f,t,P):
            raise CertificateError(f'minor polynomial mismatch at {t}')
    inf=elimination(sub1,P,True)
    if inf!=minor['infinity'] or inf!=(f[DEG] if len(f)>DEG else 0):
        raise CertificateError('minor infinity mismatch')


def resultant(f,g):
    f=(f+[0]*(DEG+1-len(f)))[:DEG+1];g=(g+[0]*(DEG+1-len(g)))[:DEG+1]
    mat=np.zeros((2*DEG,2*DEG),dtype=np.int64)
    # Independent direct Sylvester construction, fixed homogeneous degree.
    for shift in range(DEG):
        mat[shift,shift:shift+DEG+1]=f[::-1]
        mat[DEG+shift,shift:shift+DEG+1]=g[::-1]
    return elimination(mat,P,True)


def verify_case(tensor,case):
    mats=pencil(tensor,tuple(case['free_parties']),case['H_party'],case['K_party'])
    minors=case['minors'];weights=case['combination_weights']
    if len(weights)!=len(minors) or not minors:raise CertificateError('combination length')
    for minor in minors:verify_minor(mats,minor)
    combined=[0]*(DEG+1)
    for weight,minor in zip(weights,minors):
        if type(weight)!=int or not 0<=weight<P:raise CertificateError('invalid weight')
        for j,c in enumerate(minor['polynomial']):combined[j]=(combined[j]+weight*c)%P
    while combined and combined[-1]==0:combined.pop()
    if combined!=case['combination_polynomial']:raise CertificateError('combination polynomial mismatch')
    res=resultant(minors[0]['polynomial'],combined)
    if not res or res!=case['homogeneous_resultant_mod_p']:raise CertificateError('resultant mismatch/zero')
    return len(minors),res


def source_sector_rank(tensor,free,mask):
    rest=tuple(j for j in range(4) if j not in free)
    entries=[(x,v) for x,v in tensor.items() if all((x[rest[i]] in (1,2))==bool(mask[i]) for i in range(2))]
    alph=[tuple(range(6)) if j in free else ((1,2) if mask[rest.index(j)] else (0,3,4,5)) for j in range(4)]
    ranks=[]
    for j in (1,2,3):
        ra=(0,j);ca=tuple(i for i in range(4) if i not in ra)
        m=np.zeros((len(alph[ra[0]])*len(alph[ra[1]]),len(alph[ca[0]])*len(alph[ca[1]])),dtype=np.int64)
        for x,(a,b) in entries:
            r=alph[ra[0]].index(x[ra[0]])*len(alph[ra[1]])+alph[ra[1]].index(x[ra[1]])
            c=alph[ca[0]].index(x[ca[0]])*len(alph[ca[1]])+alph[ca[1]].index(x[ca[1]])
            m[r,c]+=a+6*b
        ranks.append(elimination(m,17))
    return len(entries),ranks


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('candidate',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    if not all(P%d for d in range(2,isqrt(P)+1)):raise CertificateError('field modulus not prime')
    tensor,sha=load_table(a.table);raw=a.candidate.read_bytes();candidate=json.loads(raw)
    if candidate['table_sha256']!=sha or candidate['prime']!=P or candidate['minor_size']!=DEG:
        raise CertificateError('candidate provenance mismatch')
    expected={(free,h,k) for free in itertools.combinations(range(4),2)
              for rest in [tuple(j for j in range(4) if j not in free)] for h,k in (rest,rest[::-1])}
    observed=set();results=[];nminors=0
    for case in candidate['cases']:
        key=(tuple(case['free_parties']),case['H_party'],case['K_party'])
        if key in observed or key not in expected or case['status']!='CERTIFIED':raise CertificateError('case coverage')
        observed.add(key);n,res=verify_case(tensor,case);nminors+=n
        results.append({'free':key[0],'H':key[1],'K':key[2],'minors_checked':n,'resultant_mod257':res})
    if observed!=expected or candidate['certified_count']!=12:raise CertificateError('incomplete case universe')
    sectors=[]
    for free in itertools.combinations(range(4),2):
        zero=source_sector_rank(tensor,free,(0,0));one=source_sector_rank(tensor,free,(1,1))
        if zero[0]!=20 or max(zero[1])!=20 or one[0]!=8 or max(one[1])!=8:
            raise CertificateError(f'pure-sector rank mismatch {free}: {zero},{one}')
        sectors.append({'free':free,'sector00_source_terms_and_ranks':zero,'sector11_source_terms_and_ranks':one})
    mutant=copy.deepcopy(candidate['cases'][0]['minors'][0]);mutant['polynomial'][0]=(mutant['polynomial'][0]+1)%P
    try:verify_minor(pencil(tensor,(0,1),2,3),mutant)
    except CertificateError as exc:
        if not str(exc).startswith('minor polynomial mismatch'):raise
        negative=str(exc)
    else:raise CertificateError('mutant minor incorrectly accepted')
    result={'table_sha256':sha,'candidate_sha256':hashlib.sha256(raw).hexdigest(),
            'prime':P,'numpy_version':np.__version__,'integer_only':True,
            'cases_verified':len(results),'minors_verified':nminors,'resultants':results,
            'pure_sector_rank_checks_mod17':sectors,'mutated_polynomial_control':negative,
            'scope':'Exact field checks; written resultant/Koszul lift to complex and original-orbit scope are separate.'}
    with a.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:v for k,v in result.items() if k not in ('resultants','pure_sector_rank_checks_mod17')},sys.stdout,indent=2);print()


if __name__=='__main__':main()
