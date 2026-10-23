#!/usr/bin/env python3
"""Finite auxiliary diagnosis of the chosen bare H(5,6,4,3), not an unrestricted nonexistence theorem.
At point0 each missing-group family has18 triples on18 points. Enumerate ALL C(18,6)=18564 six-triple subsets
for a perfect matching, then enumerate decompositions into3 disjoint matchings. A family with no matching
cannot be resolved, so this specific master is not frame-derived. The inflated size18 object is checked
independently and does not rely on this diagnosis. A separately known KF(6^4) is a positive enumeration control.
Usage: diagnose_h6_frame.py MASTER_H6.json KNOWN_KF6.json NEW_RECEIPT.json
"""
import lane_guard  # noqa: F401
import hashlib
import itertools
import json
import sys
from math import comb
from lane_guard import xopen


def matchings(Ts,target):
    pcs=[]
    for ids in itertools.combinations(range(len(Ts)),6):
        pts=[p for i in ids for p in Ts[i]]
        if len(set(pts))==18 and set(pts)==target:pcs.append(sum(1<<i for i in ids))
    full=(1<<len(Ts))-1;pcset=set(pcs)
    count=sum(1 for a,b in itertools.combinations(pcs,2) if not a&b and (full^(a|b)) in pcset)//3
    return pcs,count


def main():
    master,known,out=sys.argv[1:4]
    d=json.load(open(master));der=sorted(tuple(p for p in B if p!=0) for B in d['blocks'] if 0 in B)
    assert len(der)==72
    fam=[]
    for omit in range(1,5):
        Ts=[T for T in der if omit not in {p//6 for p in T}]
        target={p for p in range(6,30) if p//6!=omit}
        assert len(Ts)==18
        pcs,count=matchings(Ts,target)
        fam.append({'missing_group':omit,'triples':Ts,'subsets_examined':comb(len(Ts),6),
                    'perfect_matching_masks':pcs,'perfect_matchings':len(pcs),'three_class_decompositions':count})
    positive=[]
    for key,Cs in json.load(open(known))['frames'].items():
        Ts=sorted(T for C in Cs for T in C);target={p for T in Ts for p in T}
        pcs,count=matchings(Ts,target)
        assert len(pcs)>=3 and count>=1, 'positive frame enumeration failed'
        positive.append({'missing_group':int(key),'perfect_matchings':len(pcs),'three_class_decompositions':count})
    rec={'master':master,'master_sha256':hashlib.sha256(open(master,'rb').read()).hexdigest(),
         'point':0,'families':fam,'known_positive_frame':known,'positive_control_results':positive,
         'specific_master_not_frame_derived':any(f['three_class_decompositions']==0 for f in fam),
         'scope':'Only this exact finite master. No conclusion that FDGDD(5{6}) or FDGDD(5{18}) is impossible.'}
    with xopen(out) as fh:json.dump(rec,fh,indent=1)
    print(json.dumps({'families':[{'missing_group':f['missing_group'],'perfect_matchings':f['perfect_matchings'],
                                  'decompositions':f['three_class_decompositions']} for f in fam],
                      'positive_controls':positive,'specific_master_not_frame_derived':rec['specific_master_not_frame_derived']}))


if __name__=='__main__':main()
