#!/usr/bin/env python3
"""Deterministically regenerate the unreviewed E2 finite-constant certificate. Output path must be new (mode x).
Search domains are finite CONSTANTS only; this generator is not the checker or the universal implication proof.
"""
import json,sys,hashlib
from math import ceil
FD={-3:4,-2:2,-1:0,0:1,1:0,2:0,3:1}
def balanced(D,h,d):
    cand=[]
    for t in range(-16,9):
        for u in range(t,13):
            kind='S' if u==t else 'P'
            if 7+h+t<1 or 2*t>12+D:continue
            if kind=='S':
                if 2*t>D+2+FD[d]:continue
            elif t+u>D-8+2*FD[d] or 7+h+2*t-u<0:continue
            L=min(-h+D+2-t,u+t,(u-h)//2+1)
            U=max(t-1,u-h-t-1,ceil((u-h+D)/2)-1)
            LP=min(-h+D+1-t,u+d+t+1,(u+d-h)//2+1)
            UP=max(t,u+d-h-t-2,ceil((u+d-h+D)/2)-1)
            lo,hi=LP-U,UP-L
            if lo< -8 or hi>8:continue
            cand.append((lo,hi,abs(t)+abs(u),kind,t,u))
    lo=max(v[0] for v in cand);hi=min(v[1] for v in cand)
    wl=min((v for v in cand if v[0]==lo),key=lambda v:(v[2],v[1]-v[0]))
    wh=min((v for v in cand if v[1]==hi),key=lambda v:(v[2],v[1]-v[0]))
    return {'delta':D,'h':h,'d':d,'lo':lo,'hi':hi,'witnesses':[{'kind':v[3],'t':v[4],'u':v[5],'lo':v[0],'hi':v[1]} for v in (wl,wh)]}

def small(D,g,rho,d):
    a=(rho-3)//2;p0=33 if rho==1 else 31;cand=[]
    for t in range(-5,1):
        if 2*t>g-3+FD[d]:continue
        for y in range(16):
            m0=(p0-3)//2+t
            if y>m0 or (y-a-t)%2 or m0-y>p0-D-g-8:continue
            L=min(rho-a-t+1,a+t+y-g,(y+rho-D-1-g)//2+1)
            U=max(a+t-1,y+rho-D-2-g-a-t,ceil((rho-g-1+y)/2)-1)
            LP=min(rho-a-t,a+t+y+d+1-g,(y+d+rho-D-1-g)//2+1)
            UP=max(a+t,y+d+rho-D-3-g-a-t,ceil((rho-g-1+y+d)/2)-1)
            lo,hi=LP-U,UP-L
            if lo<max(-12,d-D-g-2) or hi>12:continue
            cand.append((lo,hi,abs(t)+y,t,y))
    lo=max(v[0] for v in cand);hi=min(v[1] for v in cand)
    wl=min((v for v in cand if v[0]==lo),key=lambda v:v[2]);wh=min((v for v in cand if v[1]==hi),key=lambda v:v[2])
    return {'delta':D,'g':g,'rho':rho,'d':d,'lo':max(lo,d+1-g),'hi':hi,'witnesses':[{'t':v[3],'y':v[4],'lo':v[0],'hi':v[1]} for v in (wl,wh)]}

def main():
    data={'schema':1,'scope':{'E':2,'p_min':31,'delta_min':4,'delta_max':8},'balanced':[],'small_g':[]}
    for D in range(4,9):
        for h in range(D-4,17-D,2):
            for d in range(-3,4):data['balanced'].append(balanced(D,h,d))
    for D in range(4,9):
        for g in (1,2):
            for rho in (1,3):
                for d in range(-3,4):data['small_g'].append(small(D,g,rho,d))
    text=json.dumps(data,indent=2,sort_keys=True)+'\n'
    with open(sys.argv[1],'x') as f:f.write(text)
    print(json.dumps({'sha256':hashlib.sha256(text.encode()).hexdigest(),'balanced':len(data['balanced']),'small_g':len(data['small_g'])}),flush=True)
if __name__=='__main__':
    main()
