#!/opt/homebrew/bin/python3
"""Place a four-zero rank-four count model through the quartic filter only."""
import argparse
import json
import pathlib


def q(x):return (((x&1)*((x>>1)&1))^(((x>>2)&1)*((x>>3)&1)))
def Q(x):return q(x)^((x>>4)&1)
def h(x):return ((x>>2)&1)*(1^((x>>1)&1))*(((x&1)*((x>>3)&1))^((x>>4)&1))


def fwht(vals):
    a=list(vals);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(step):
                x,y=a[i+j],a[i+j+step];a[i+j],a[i+j+step]=x+y,x-y
        step*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--histogram',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists():raise FileExistsError('output exists')
    model=json.loads(args.histogram.read_text(encoding='utf-8'));A={int(t):v for t,v in model['histogram'].items()}
    if (model['q_zero_count'],model['odd_Q_weight'],model['peakunit_weight'],model['nonpeak_Q_intersection'])!=(160,128,224,24):raise ValueError('unexpected histogram')
    assert sum(q(x)==0 for x in range(256))==160 and sum(Q(x) for x in range(256))==128
    assert sum(h(x) for x in range(256))==32 and sum(h(x)*Q(x) for x in range(256))==24
    zero={0,64,128,192};K=[None]*512
    for x in range(256):
        if x in zero:K[x]=0
        elif not q(x):K[x]=-4
    qzero=[x for x in range(256) if not q(x) and x not in zero]
    assert len(qzero)==156 and A[-4]+A[4]==156
    for x in qzero[:A[4]]:K[x]=4
    qone=[x for x in range(256) if q(x)]
    even=[-6]*A[-6]+[-2]*A[-2]+[2]*A[2]+[6]*A[6]
    assert len(qone)==len(even)==96
    for x,v in zip(qone,even):K[x]=v
    blocks={(1,1):[-5]*A[-5]+[3]*A[3],(1,0):[-3]*A[-3]+[5]*A[5],
            (0,1):[-1]*A[-1]+[7]*A[7],(0,0):[-7]*A[-7]+[1]*A[1]}
    for key,vals in blocks.items():
        coords=[x for x in range(256) if (h(x),Q(x))==key]
        assert len(coords)==len(vals)
        for x,v in zip(coords,vals):K[256+x]=v
    assert all(v is not None for v in K)
    assert {t:K.count(t) for t in range(-7,8)}=={t:A[t]+(t==0) for t in range(-7,8)}
    assert K[0]==0 and sum(K)==128 and sum(v*v for v in K)==16384 and max(map(abs,K))==7
    assert all(K[a]%4==(2*q(a&255)+(a>>8)*(1+2*((a>>4)&1)))%4 for a in range(512))
    inv=fwht(K);bad=sum(abs(x)!=128 for x in inv)
    if not bad:
        with args.candidate.open('x',encoding='utf-8') as out:json.dump({'format':'boolean-truth-v1','bits':''.join('1' if x<0 else '0' for x in inv)},out,indent=2);out.write('\n')
    receipt={'spectrum_k':K,'q_zero_count':160,'Q_weight':128,'P_weight':224,'Pzero_Q_intersection':24,
             'global_mod4_and_forced_quartic':True,'inverse_nonsign_count':bad,'inverse_l1':sum(map(abs,inv)),
             'actual_boolean_candidate_written':not bad,'scope':'formal placement; no actual Boolean realization'}
    with args.output.open('x',encoding='utf-8') as out:json.dump(receipt,out,indent=2,sort_keys=True);out.write('\n')
    print('rank4 formal placement c=24 inverse_nonsign=',bad,flush=True)


if __name__=='__main__':main()
