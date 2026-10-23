"""Deterministic bounded balanced tabu search with exact integer updates.

All swaps preserve weight. Two integer FWHTs give the exact change of a
separable spectral penalty for all 65536 swaps at once. Search failures
are logs only, never exclusions. Every saved table includes its complete
spectrum and the exact input-bit convention.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')
import argparse
import hashlib
import json
from pathlib import Path
import random
import time
import numpy as np
from seeds import SEEDS,decode


def hadamard(values):
    out=np.array(values,dtype=np.int64,copy=True)
    h=1
    while h<len(out):
        v=out.reshape(-1,2*h)
        a=v[:,:h].copy()
        b=v[:,h:].copy()
        v[:,:h]=a+b
        v[:,h:]=a-b
        h*=2
    return out


def make_starts(H):
    starts=[]
    rng=random.Random(20261015)
    for name,hx in SEEDS.items():
        f=np.array(decode(hx),dtype=np.int64)
        w=hadamard(1-2*f)
        hi=np.flatnonzero(abs(w)==28).tolist()
        lo=np.flatnonzero(abs(w)==4).tolist()
        B=[]
        C=[]
        for x in range(512):
            b=c=0
            for k,a in enumerate(hi):
                if H[a,x]*(1-2*f[x])*w[a]<0: b|=1<<k
            for k,a in enumerate(lo):
                if H[a,x]*(1-2*f[x])*w[a]>0: c|=1<<k
            B.append(b)
            C.append(c)
        choices=[]
        for x in range(511):
            for y in range(x+1,512):
                zeros=C[x]&C[y]
                if zeros:
                    violations=bin(B[x]&B[y]).count('1')
                    choices.append((violations,rng.random(),x,y,zeros))
        choices.sort()
        for violations,_,x,y,zeros in choices[:40]:
            shift=lo[(zeros&-zeros).bit_length()-1]
            g=f.copy()
            g[x]^=1
            g[y]^=1
            g^=(1-H[shift])//2
            wg=hadamard(1-2*g)
            assert g.sum()==256 and max(abs(wg))==32
            assert int(np.maximum(abs(wg)//4-7,0).dot(np.maximum(abs(wg)//4-7,0)))==violations
            starts.append((g,{'seed':name,'flips':[x,y],'linear_shift':shift,'tail_penalty':violations}))
        print('initial',name,'best number of magnitude-32 coefficients',choices[0][0],flush=True)
    baseline=np.array([((x>>0)&1)^(((x>>1)&1)&((x>>2)&1))^(((x>>3)&1)&((x>>4)&1))^(((x>>5)&1)&((x>>6)&1))^(((x>>7)&1)&((x>>8)&1)) for x in range(512)],dtype=np.int64)
    starts.append((baseline,{'seed':'quadratic-baseline'}))
    return starts


def phi(v,scale):
    excess=np.maximum(abs(v)-7,0)
    return scale*excess*excess+v*v*v*v


def record(f,w,meta):
    bits=''.join(map(str,f.tolist()))
    v=w//4
    tail=int(np.sum(np.maximum(abs(v)-7,0)**2))
    return dict(meta,bits=bits,bit_order='bits[x]=f(x), x=0..511; x_i=(x>>i)&1',sha256_ascii_bits=hashlib.sha256(bits.encode()).hexdigest(),weight=int(f.sum()),nonlinearity=256-int(max(abs(w)))//2,walsh=w.tolist(),tail_penalty=tail,max_abs_walsh=int(max(abs(w))))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seed',type=int,default=20261015)
    p.add_argument('--steps',type=int,default=200000)
    p.add_argument('--seconds',type=float,default=600)
    p.add_argument('--prefix',default='results/heuristic')
    p.add_argument('--scale',type=int,default=1000000)
    args=p.parse_args()
    rng=np.random.default_rng(args.seed)
    H=np.array([[1-2*(bin(a&x).count('1')%2) for x in range(512)] for a in range(512)],dtype=np.int64)
    starts=make_starts(H)
    Path(args.prefix+'-starts.json').write_text(json.dumps([dict(meta,bits=''.join(map(str,f.tolist()))) for f,meta in starts],indent=2)+'\n')
    start=time.monotonic()
    bestcost=None
    besttail=512*512
    tailrec=None
    bestrec=None
    tabu=np.zeros(512,dtype=np.int64)
    step=0
    logs=[]
    f=None
    while step<args.steps and time.monotonic()-start<args.seconds:
        if step%400==0:
            f,origin=starts[int(rng.integers(len(starts)))]
            f=f.copy()
            for k in range(int(rng.integers(0,6))):
                one=int(rng.choice(np.flatnonzero(f==1)))
                zero=int(rng.choice(np.flatnonzero(f==0)))
                f[one]^=1
                f[zero]^=1
            w=hadamard(1-2*f)
            tabu.fill(0)
        assert int(w[0])==0
        v=w//4
        currentphi=phi(v,args.scale)
        cost=int(currentphi.sum())
        tail=int(np.sum(np.maximum(abs(v)-7,0)**2))
        if tailrec is None or tail<besttail:
            besttail=tail
            tailrec=record(f,w,dict(random_seed=args.seed,step=step,origin=origin,objective=cost,elapsed_seconds=time.monotonic()-start))
            Path(args.prefix+'-best-tail.json').write_text(json.dumps(tailrec,indent=2)+'\n')
        if bestcost is None or cost<bestcost:
            bestcost=cost
            bestrec=record(f,w,dict(random_seed=args.seed,step=step,origin=origin,objective=cost,elapsed_seconds=time.monotonic()-start))
            Path(args.prefix+'-best.json').write_text(json.dumps(bestrec,indent=2)+'\n')
            print('best',step,'tail',tail,'max|W|',bestrec['max_abs_walsh'],'cost',cost,'sec',round(time.monotonic()-start,2),flush=True)
        if tail==0:
            bestrec=record(f,w,dict(random_seed=args.seed,step=step,origin=origin,objective=cost,elapsed_seconds=time.monotonic()-start))
            Path(args.prefix+'-witness.json').write_text(json.dumps(bestrec,indent=2)+'\n')
            print('TARGET WITNESS FOUND',flush=True)
            break
        A2=phi(v+1,args.scale)-phi(v-1,args.scale)
        B2=phi(v+1,args.scale)+phi(v-1,args.scale)-2*currentphi
        G=hadamard(A2)
        K=hadamard(B2)
        ones=np.flatnonzero(f==1)
        zeros=np.flatnonzero(f==0)
        xor=ones[:,None]^zeros[None,:]
        numerator=G[ones[:,None]]-G[zeros[None,:]]+K[0]-K[xor]
        # x=zero is changed +1 to -1, y=one is changed -1 to +1.
        assert not np.any(numerator%4)
        delta=numerator//4
        allowed=(tabu[ones[:,None]]<=step)&(tabu[zeros[None,:]]<=step)
        allowed|=(cost+delta<bestcost)
        ranked=np.where(allowed,delta,np.iinfo(np.int64).max)
        target=int(ranked.min())
        ties=np.flatnonzero(ranked==target)
        selected=int(ties[int(rng.integers(len(ties)))])
        i,j=np.unravel_index(selected,ranked.shape)
        one,zero=int(ones[i]),int(zeros[j])
        wp=w+2*H[:,one]-2*H[:,zero]
        if step<20 or step%1000==0:
            assert int(phi(wp//4,args.scale).sum())-cost==target
            ff=f.copy()
            ff[one]^=1
            ff[zero]^=1
            assert np.array_equal(wp,hadamard(1-2*ff))
        f[one]^=1
        f[zero]^=1
        w=wp
        tabu[one]=step+int(rng.integers(5,13))
        tabu[zero]=step+int(rng.integers(5,13))
        step+=1
        if step%1000==0:
            log={'step':step,'best_tail':besttail,'seconds':round(time.monotonic()-start,3)}
            logs.append(log)
            Path(args.prefix+'-progress.json').write_text(json.dumps(logs,indent=2)+'\n')
            print('progress',log,flush=True)
    final={'status':'witness' if bestrec['tail_penalty']==0 else 'inconclusive','steps':step,'seed':args.seed,'seconds':time.monotonic()-start,'best_tail':besttail,'best_max_abs_walsh':tailrec['max_abs_walsh'],'objective_scale':args.scale,'scope':'heuristic log only; non-find proves no exclusion'}
    Path(args.prefix+'-summary.json').write_text(json.dumps(final,indent=2)+'\n')
    print(json.dumps(final),flush=True)


if __name__=='__main__': main()
