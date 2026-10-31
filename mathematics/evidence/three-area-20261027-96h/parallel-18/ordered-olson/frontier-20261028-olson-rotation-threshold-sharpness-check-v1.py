#!/usr/bin/env python3
"""R=p control (not L_RES): length4p-2 words avoiding identity2p."""
import argparse
import json


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',required=True);args=ap.parse_args()
    cases=[]
    for p in (3,5,7,11,13,17):
        b=(-pow(2,-1,p))%p
        w=[[0,1] for _ in range(2*p-1)]+[[b,0]]
        for j in range(1,p):w.extend([[j,1],[b,0]])
        states={(0,0,0)}
        for y,f in w:
            new=set(states)
            for k,x,e in states:
                if k<2*p:new.add((k+1,(x+(-y if e else y))%p,e^f))
            states=new
        support=sorted([x,e] for k,x,e in states if k==2*p)
        if [0,0] in support:raise ValueError('SHARPNESS_COUNTEREXAMPLE_FAILED')
        if len(w)!=4*p-2:raise ValueError('COUNTS')
        cases.append({'p':p,'a':1,'b':b,'word':w,'target_length':2*p,'support':support})
    result={'result':'PASS_R_P_SHARPNESS_CONTROL','cases':cases,
            'scope':'R=p length4p-2 avoiding words, NOT a counterexample to R=p+1 or L_RES'}
    with open(args.output,'x',encoding='utf-8') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
    print(json.dumps({'result':result['result'],'primes':[c['p'] for c in cases]},sort_keys=True))


if __name__=='__main__':main()
