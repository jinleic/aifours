#!/usr/bin/env python3
"""Independent standard-library verifier for a 30-word P-code diagnostic."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path


class CertificateError(ValueError):pass


def verify(W):
    if len(W)!=30:raise CertificateError('wrong word count')
    if any(len(x)!=4 or any(type(a)!=int or a<0 or a>5 for a in x) for x in W):raise CertificateError('invalid coordinate')
    if len(set(W))!=30:raise CertificateError('duplicate word')
    hist=Counter(sum(x<3 for x in w) for w in W)
    if hist!={1:12,2:18}:raise CertificateError('wrong active distribution')
    allpairs={(x,y) for x in range(6) for y in range(6)}
    summaries={}
    for i,j in itertools.combinations(range(4),2):
        P={(w[i],w[j]) for w in W}
        if len(P)!=30:raise CertificateError('two-coordinate collision')
        missing=allpairs-P
        if len(missing)!=6 or any(x>=3 or y>=3 for x,y in missing):raise CertificateError('residual pair alphabet')
        if any(sum(x==u for x,y in missing)!=2 for u in range(3)) or any(sum(y==u for x,y in missing)!=2 for u in range(3)):
            raise CertificateError('residual projection not 2-regular')
        summaries[f'{i}{j}']={'P_pairs':len(P),'missing_active_pairs':sorted(missing)}
    for i in range(4):
        if any(sum(w[i]==x for w in W)!=4 for x in range(3)):raise CertificateError('wrong active symbol multiplicity')
    return summaries


def expect(W,reason):
    try:verify(W)
    except CertificateError as exc:
        if str(exc)!=reason:raise ValueError(f'wrong rejection {exc}; expected {reason}')
        return reason
    raise ValueError(f'mutation accepted; expected {reason}')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
    data=a.candidate.read_bytes();src=json.loads(data)
    if src.get('status')!='sat':raise ValueError('candidate is not a SAT record')
    W=[tuple(r['coordinates']) for r in src['records']];summary=verify(W)
    controls={}
    controls['drop_word']=expect(W[:-1],'wrong word count')
    D=W[:];D[1]=D[0];controls['duplicate_word']=expect(D,'duplicate word')
    D=W[:];D[0]=(6,)+D[0][1:];controls['out_of_range']=expect(D,'invalid coordinate')
    collision=None
    for i,j in itertools.permutations(range(4),2):
      for p,q in itertools.permutations(range(30),2):
        if W[p][i]!=W[q][i] or W[p][j]==W[q][j] or (W[p][j]<3)!=(W[q][j]<3):continue
        row=list(W[p]);row[j]=W[q][j];D=W[:];D[p]=tuple(row)
        if len(set(D))!=30:continue
        try:verify(D)
        except CertificateError as exc:
            if str(exc)=='two-coordinate collision':collision=(i,j,p,q);break
      if collision:break
    if collision is None:raise ValueError('could not construct intended pair collision')
    controls['two_coordinate_collision']={'reason':'two-coordinate collision','indices':collision}
    result={'candidate_sha256':hashlib.sha256(data).hexdigest(),'words':30,'P_pair_summaries':summary,
            'intended_mutation_controls':controls,
            'scope':'P code only: no residual 16-term support, phases, or AME claim.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='P_pair_summaries'},indent=2))


if __name__=='__main__':main()
