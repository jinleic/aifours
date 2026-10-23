#!/usr/bin/env python3
"""Stdlib-only FDGDD18 seed replay; no producer/checker/solver code imported.
make CERT MASTER_H6.json NEW_SEED.json: reconstruct all zero-sum blocks from the540 master blocks and all90
point frames from the two representative frames at points0,1, using30 master permutations and copy negation;
require literal byte identity. Verify master action closure/block invariance and a negative transposition.
expand SEED.json NEW_CERT: regenerate the same raw Format D certificate without any SAT model.
Only block-set actions and the designated transport are claimed. In particular, the chosen frames at copy0
need not be invariant under copy negation (which fixes that representative).
"""
import os
import sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
from lane_guard import xopen  # noqa: E402
import hashlib
import itertools
import json
from collections import Counter


def read_raw(path):
    data=open(path,'rb').read()
    L=[s.split('#',1)[0].split() for s in data.decode('ascii').splitlines()]
    L=[s for s in L if s]
    assert L[0]==['GDD34','FDGDD','5','18'] and L[1]==['GROUPS']
    assert [[int(z) for z in s] for s in L[2:7]]==[list(range(18*i,18*i+18)) for i in range(5)]
    assert L[7]==['BLOCKS']
    pos,blocks=8,[]
    while pos<len(L) and L[pos][0]!='POINT':
        blocks.append(tuple(int(z) for z in L[pos]));pos+=1
    sec={};x=None
    for row in L[pos:]:
        if row[0]=='POINT':
            x=int(row[1]);assert x not in sec;sec[x]=[]
        elif row[0]=='FRAME':sec[x].append((int(row[1]),[]))
        else:sec[x][-1][1].append(tuple(int(z) for z in row))
    assert sorted(sec)==list(range(90))
    return data,set(blocks),sec


def regenerate(seed):
    master=seed['master_blocks'];G=seed['master_permutations']
    B=set()
    for Q in master:
        for a,b,c in itertools.product(range(3),repeat=3):
            d=(-a-b-c)%3
            B.add(tuple(sorted((3*Q[0]+a,3*Q[1]+b,3*Q[2]+c,3*Q[3]+d))))
    sec={}
    for e in G:
        for alpha in range(3):
            root=str(0 if alpha==0 else 1)
            x=3*e[0]+alpha
            assert x not in sec
            def image(p):
                q,b=divmod(p,3)
                return 3*e[q]+((-b)%3 if alpha==2 else b)
            sec[x]=[(e[6*family]//6,sorted(tuple(sorted(image(p) for p in T)) for T in C))
                    for family,C in seed['representative_frames'][root]]
    assert sorted(sec)==list(range(90))
    L=['GDD34 FDGDD 5 18','GROUPS']+[' '.join(str(p) for p in range(18*i,18*i+18)) for i in range(5)]+['BLOCKS']
    L+=[' '.join(map(str,Q)) for Q in sorted(B)]
    for x in range(90):
        L.append(f'POINT {x}')
        for y,C in sec[x]:
            L.append(f'FRAME {y}')
            L+=[' '.join(map(str,T)) for T in C]
    return ('\n'.join(L)+'\n').encode('ascii'),B,sec


def main():
    mode=sys.argv[1]
    if mode=='make':
        cert,mp,out=sys.argv[2:5]
        raw,B,sec=read_raw(cert);master=json.load(open(mp))
        mb={tuple(Q) for Q in master['blocks']};G={tuple(e) for e in master['permutations']}
        assert len(G)==30 and len({e[0] for e in G})==30 and tuple(range(30)) in G
        assert all(tuple(a[b[p]] for p in range(30)) in G for a in G for b in G), 'permutation set not closed'
        assert all(tuple(sorted(e[p] for p in Q)) in mb for e in G for Q in mb), 'master block action failed'
        cov=Counter(T for Q in mb for T in itertools.combinations(Q,3))
        universe={T for T in itertools.combinations(range(30),3) if len({p//6 for p in T})==3}
        assert len(mb)==540 and set(cov)==universe and set(cov.values())=={1}
        seed={'source_certificate':cert,'source_sha256':hashlib.sha256(raw).hexdigest(),
              'master_source':mp,'master_source_sha256':hashlib.sha256(open(mp,'rb').read()).hexdigest(),
              'master_blocks':sorted(mb),'master_permutations':sorted(G),
              'representative_frames':{'0':sec[0],'1':sec[1]}}
        rebuilt,B2,sec2=regenerate(seed)
        assert B2==B and sec2==sec and rebuilt==raw,'seed regeneration mismatch'
        trans=list(range(90));trans[0],trans[1]=1,0
        assert any(tuple(sorted(trans[p] for p in Q)) not in B for Q in B),'negative action control did not fail'
        seed['audit']={'master_group_order':30,'copy_point_orbits':[30,30,30],
                       'representatives_used':[0,1],'copy_negation_transports_1_to_2':True,
                       'chosen_copy0_frames_negation_invariance':'not required and not claimed',
                       'negative_action_control':'transposition(0 1) fails block invariance',
                       'byte_identical':True}
        with xopen(out) as fh:json.dump(seed,fh,indent=1)
        print(json.dumps({'seed':out,'certificate_sha256':seed['source_sha256'],**seed['audit']}))
    elif mode=='expand':
        path,out=sys.argv[2:4];seed=json.load(open(path))
        data,B,sec=regenerate(seed);sha=hashlib.sha256(data).hexdigest()
        assert sha==seed['source_sha256']
        with xopen(out,'xb') as fh:fh.write(data)
        print(json.dumps({'output':out,'sha256':sha,'blocks':len(B),'point_sections':len(sec)}))
    else:raise SystemExit(__doc__)


if __name__=='__main__':main()
