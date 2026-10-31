#!/opt/homebrew/bin/python3
"""Necessary low-rank energy/mod3 profiles, balanced-Q sign cases, and coarse D12 control."""
import argparse
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def profiles(rank):
    N=1<<rank;mmax=122 if rank==2 else 112;z=64 if rank==2 else 96
    Ds=range(12,29,4) if rank==2 else range(8,25,2);rows=set()
    for D in Ds:
        for a in range(N+1):
            for b in range(N+1-a):
                S=a-b;m=116+D//2+(2 if rank==2 else 1)*S
                if m%2 or m>mmax or m<0 or m%3!=(1-D)%3:continue
                if (9216-20*z-64*m)//16<1:continue
                for n1 in range(D+1):
                    n3=D-n1;num=8*(m-60)-2*D-4*n1
                    if num%3:continue
                    h=num//3;n5=h-n3;n7=256-h-n1
                    if min(n3,n5,n7)<0:continue
                    rows.add((D,m,S,n1,n3,n5,n7))
    return sorted(rows)


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    r2=profiles(2);r4=profiles(4)
    assert len(r2)==17 and sorted({(x[0],x[1]) for x in r2})==[(12,118),(16,120),(20,122)]
    assert (min(x[-1] for x in r2),max(x[-1] for x in r2))==(104,113)
    assert len(r4)==50 and sorted({(x[0],x[1]) for x in r4})==[(8,104),(8,110),(10,108),(12,106),(12,112),(14,110),(16,108),(18,112),(20,110),(24,112)]
    assert (min(x[-1] for x in r4),max(x[-1] for x in r4))==(126,146)
    # Balanced Q implies X in [-2,2], s=0 or128, 12H0=s+16X.
    xs=[(X,s) for X in range(-2,3) for s in (0,128) if (s+16*X)%12==0]
    assert set(xs)=={(0,0),(-2,128),(1,128)}
    balanced_signs=[]
    for X,s in xs:
        H0=(s+16*X)//12
        for n1 in range(29):
            for c0 in range(n1+1):
                c1=n1-c0
                for d0 in range(H0//2+1):
                    d1=H0//2-d0
                    if c0-c1==X and d1-d0==X and abs(c0-d0)<=1 and abs(d1-c1)<=1:
                        balanced_signs.append((n1,X,s,c0,c1,d0,d1))
    assert {v[0] for v in balanced_signs}=={0,2}
    assert [(r[0],r[1],r[3]) for r in r2 if r[3] in (0,2)]==[(12,118,2),(20,122,0)]
    # Coarse D12 sign/quadratic/ternary model: all profile/congruence constraints pass;
    # inverse spectrum fails peak and Q, so it is not a target witness.
    pts=[135,215,70,187,156,39,65,84,131,230,172,202]
    signs=[-1,1,-1,1,1,-1,-1,-1,-1,-1,-1,1]
    delta=[0]*256
    for x,v in zip(pts,signs):delta[x]=v
    u,w,ell,const=66,82,122,0
    bit=lambda a,x:(a&x).bit_count()%2
    Q=[bit(u,x)*bit(w,x)^bit(ell,x)^const for x in range(256)];g=[-1 if q else 1 for q in Q]
    G=fw(g);F=fw(delta);Y=[y for y,v in enumerate(G) if v]
    assert len(Y)==4 and all(abs(G[y])==128 for y in Y)
    v=[]
    for y in range(256):
        n=(G[y]-F[y])%3;v.append(0 if n==0 else (1 if n==1 else -1))
    m=256-sum(x!=0 for x in v);S=sum((1 if G[y]>0 else -1)*v[y] for y in Y)
    n3=sum(delta[x]*g[x]==1 for x in pts);n1=12-n3;M=sum(x%3!=0 for x in F)
    assert (m,S,n1,n3,M)==(118,-2,8,4,138) and M%3==12%3 and m%3==(1-12)%3
    H=(8*(m-60)-2*12-4*n1)//3;n5=H-n3;n7=256-H-n1
    assert (12,m,S,n1,n3,n5,n7) in r2
    V=fw(v);peakbad=sum(abs(z) not in (2,6,10,14) for z in V)
    paritybad=sum(z%4!=2 for z in V);qbad=sum(int((V[x]//2)%4==3)!=Q[x] for x in range(256))
    assert (max(map(abs,V)),peakbad,paritybad,qbad)==(38,25,0,136)
    # Integer parity counterexample: high-peak actual rank2 target-like 4 flips.
    f=[x&1 for x in range(512)]
    for x in (336,202,71,313):f[x]^=1
    t=0
    for x,b in enumerate(f):
        if b:t^=x
    W=fw([1-2*b for b in f]);assert sum(f)==256 and t==228 and max(map(abs,W))==504
    out={'scope':'necessary low-rank profiles; coarse control is NOT a Boolean witness',
         'columns':['D','m','S','n1','n3','n5','n7'],'rank2_profiles':r2,'rank4_profiles':r4,
         'balanced_Q_sign_cases':balanced_signs,
         'D12_coarse_control':{'points':pts,'signs':signs,'Q_product_masks':[u,w],
             'Q_linear_mask':ell,'Q_constant':const,'Q_weight':sum(Q),'D':12,'M':M,'m':m,'S':S,
             'n1':n1,'n3':n3,'odd_Walsh_v_peak':38,'peak_failures':25,'parity_failures':0,'Q_mismatches':136},
         'actual_rank2_highpeak_control':{'T':t,'peak':504,'balanced':True}}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('17 rank2 and 50 rank4 coarse profiles; balanced-Q n1 in {0,2}; D12 non-witness')


if __name__=='__main__':main()
