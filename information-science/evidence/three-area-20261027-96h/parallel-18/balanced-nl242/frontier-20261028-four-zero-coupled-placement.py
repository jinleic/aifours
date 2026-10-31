#!/opt/homebrew/bin/python3
"""Place the coupled-rank histogram with a globally quadratic mod-4 spectrum.

Output is formal unless its Boolean inverse is independently verified.
"""
import argparse
import collections
import json
import pathlib


def fwht(k):
    v=list(k);h=1
    while h<len(v):
        for base in range(0,len(v),2*h):
            for j in range(h):
                x,y=v[base+j],v[base+j+h];v[base+j],v[base+j+h]=x+y,x-y
        h*=2
    return v


def q(x): return sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(3))%2

def main():
    p=argparse.ArgumentParser();p.add_argument('--histogram',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists():raise FileExistsError('output exists')
    data=json.loads(args.histogram.read_text(encoding='utf-8'));a={int(t):v for t,v in data['histogram'].items()}
    if data['q_zero_count']!=144 or data['odd_Q_one_count']!=144:raise ValueError('unexpected formal model')
    zero={0,64,128,192}; evenzero={x for x in range(256) if not q(x)}
    assert len(evenzero)==144 and zero<=evenzero
    k=[None]*512
    for x in zero:k[x]=0
    for x in evenzero-zero:k[x]=4
    evenone=sorted(set(range(256))-evenzero); evenvals=[-6]*100+[2]*8+[6]*4
    assert len(evenone)==len(evenvals)==112
    for x,v in zip(evenone,evenvals):k[x]=v
    # Complement of the affine 5-flat x0=1,x2=x4=0 has degree three.
    excluded={x for x in range(256) if (x&1) and not (x&4) and not (x&16)}
    assert len(excluded)==32 and sum(q(x) for x in excluded)==16
    blocks={(0,1):[-5]*16,(0,0):[-3]*16,(1,1):[-1]*10+[7]*118,(1,0):[-7]*82+[1]*14}
    for (P,Q),vals in blocks.items():
        coords=[x for x in range(256) if (int(x not in excluded),1^q(x))==(P,Q)]
        assert len(coords)==len(vals)
        for x,v in zip(coords,vals):k[256+x]=v
    assert all(v is not None for v in k)
    assert {t:k.count(t) for t in range(-7,8)}=={t:a[t]+(t==0) for t in range(-7,8)}
    assert k[0]==0 and sum(k)==128 and sum(t*t for t in k)==16384 and max(map(abs,k))==7
    assert all(k[a]%4==(2*q(a&255)+3*(a>>8))%4 for a in range(512))
    inv=fwht(k); bad=sum(abs(v)!=128 for v in inv)
    if not bad:
        candidate={'format':'boolean-truth-v1','bits':''.join('1' if v==-128 else '0' for v in inv)}
        with args.candidate.open('x',encoding='utf-8') as out:json.dump(candidate,out,indent=2);out.write('\n')
    result={'scope':'formal spectrum; selected filters only; no actual Boolean realization claimed',
            'spectrum_k':k,'zero_indices':sorted(zero),'magnitude4_indices':[x for x in range(512) if abs(k[x])==4],
            'q_zero_count':144,'odd_Q_one_count':144,'peakunit_indicator_degree_at_most':3,
            'q_and_odd_Q_same_polar_form':True,'global_mod4_formula_verified':True,
            'inverse_nonsign_count':bad,'inverse_max_abs':max(map(abs,inv)),
            'inverse_l1':sum(map(abs,inv)),'boolean_candidate_written':bad==0}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('qzeros=144 F=140 peak=200 global_mod4=true inverse_nonsign=',bad,'L1=',result['inverse_l1'],flush=True)


if __name__=='__main__':main()
