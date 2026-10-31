#!/opt/homebrew/bin/python3
"""Place a formal directed-fiber model on a common rank-six quotient.

Checks the even-half mod8 polynomial; not an actual Boolean solution unless verified.
"""
import argparse
import itertools
import json
import pathlib

TERMS=[sum(1<<i for i in I) for d in range(4) for I in itertools.combinations(range(8),d)]

def g0(x):return sum(((x>>(2*i))&1)*((x>>(2*i+1))&1) for i in range(3))+(x&1)+((x>>1)&1)

def solve():
    piv={}
    for x in range(256):
        if g0(x)%2:continue
        row=sum(1<<j for j,t in enumerate(TERMS) if x&t==t);rhs=(g0(x)//2)%2 ^ int((x&63)!=0)
        while row:
            j=row.bit_length()-1
            if j in piv:row^=piv[j][0];rhs^=piv[j][1]
            else:piv[j]=(row,rhs);break
        if not row:assert rhs==0
    value=0
    for j in sorted(piv):
        row,rhs=piv[j]
        if ((value&(row^(1<<j))).bit_count()%2)^rhs:value|=1<<j
    assert len(piv)==76
    return value

def eval_anf(coeff,x):return sum((coeff>>j)&1 for j,t in enumerate(TERMS) if x&t==t)%2

def expand(records):return [row['tuple'] for row in records for _ in range(row['fibers'])]

def main():
    p=argparse.ArgumentParser();p.add_argument('--fibers',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--candidate',type=pathlib.Path,required=True);args=p.parse_args()
    if args.output.exists() or args.candidate.exists():raise FileExistsError('output exists')
    src=json.loads(args.fibers.read_text(encoding='utf-8'))
    if src['status']!='sat' or src['lambda_mode']!=1 or src['qrad_bit']!=0 or src['q_zero_count']!=112 or src['odd_Q_weight']!=144:
        raise ValueError('unexpected formal model')
    coeff=solve()
    def q(x):return g0(x)%2
    def h(x,r):return eval_anf(coeff,x|(r<<6)) ^ ((r&1)*q(x))
    # Particular solution must have no radical dependence; adding r1*q gives lambda=r1.
    for x in range(64):assert len({eval_anf(coeff,x|(r<<6)) for r in range(4)})==1
    for x in range(64):
        if not q(x):
            for r in range(4):assert (g0(x)+2*h(x,r))%4==(0 if x==0 else 2)
    groups=src['fiber_groups'];k=[None]*512
    for r in range(4):k[r<<6]=0
    even_zero=[x for x in range(1,64) if not q(x)];even_one=[x for x in range(64) if q(x)]
    rows0=expand(groups['zero']);rows1=expand(groups['evenmixed'])
    assert len(even_zero)==len(rows0)==27 and len(even_one)==len(rows1)==36
    for x,row in zip(even_zero,rows0):
        for r in range(4):k[x|(r<<6)]=row[r]
    for x,row in zip(even_one,rows1):
        options=[]
        for shift in range(4):
            if all((row[r^shift]//2)%4==(g0(x)+2*h(x,r))%4 for r in range(4)):options.append(shift)
        if not options:raise ValueError('fiber cannot align with cubic phase')
        shift=options[0]
        for r in range(4):k[x|(r<<6)]=row[r^shift]
    odd0=[x for x in range(64) if not q(x)];odd1=[x for x in range(64) if q(x)]
    for xs,tag in ((odd0,'odd0'),(odd1,'odd1')):
        rows=expand(groups[tag]);assert len(xs)==len(rows)
        for x,row in zip(xs,rows):
            for r in range(4):k[256|x|(r<<6)]=row[r]
    assert all(v is not None for v in k)
    expected={int(t):n for t,n in src['histogram'].items()};expected[0]+=1
    assert {t:k.count(t) for t in range(-7,8)}==expected
    assert k[0]==0 and sum(k)==128 and sum(v*v for v in k)==16384 and max(map(abs,k))<=7
    for x in range(64):
        for r in range(4):
            a=x|(r<<6)
            assert (k[a]//2)%4==(g0(x)+2*h(x,r))%4
            assert ((k[256|a]-1)//2)%2==q(x)
            assert (k[a]-k[x]-4*(r&1)*q(x))%8==0
    corr=[sum(k[a]*k[a^b] for a in range(512)) for b in range(512)]
    assert corr[0]==16384 and all(corr[b]==0 for b in (64,128,192))
    nonrad=[b for b in range(1,512) if b not in (64,128,192) and corr[b]!=0]
    P=[int(abs(k[256|x]) in (1,7)) for x in range(256)];anf=P[:]
    for i in range(8):
        for x in range(256):
            if x>>i&1:anf[x]^=anf[x^(1<<i)]
    degree=max((x.bit_count() for x,v in enumerate(anf) if v),default=0)
    inv=k[:];d=1
    while d<512:
        for i in range(0,512,2*d):
            for j in range(d):a,b=inv[i+j],inv[i+j+d];inv[i+j],inv[i+j+d]=a+b,a-b
        d*=2
    bad=sum(abs(v)!=128 for v in inv)
    if not bad:
        with args.candidate.open('x',encoding='utf-8') as out:json.dump({'format':'boolean-truth-v1','bits':''.join('1' if v<0 else '0' for v in inv)},out,indent=2);out.write('\n')
    result={'scope':'formal labeled spectrum; no actual Boolean realization unless independently verified',
            'spectrum_k':k,'q_zero_count':112,'Q_weight':144,'lambda':1,'rho':0,
            'radical':[0,64,128,192],'zero_indices':[a for a,v in enumerate(k) if not v],
            'common_q_and_odd_Q':True,'even_half_full_mod8_cubic':True,'radical_correlations':[corr[x] for x in (64,128,192)],
            'nonradical_correlations_failing':len(nonrad),'first_nonradical_failure':nonrad[0] if nonrad else None,
            'odd_P_anf_degree':degree,'inverse_nonsign_count':bad,'actual_boolean_candidate_written':bad==0}
    with args.output.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2,sort_keys=True);out.write('\n')
    print('q/Q placed, mod8 even true, radical correlations=0, other_failures=',len(nonrad),'Pdegree=',degree,'inverse_bad=',bad,flush=True)


if __name__=='__main__':main()
