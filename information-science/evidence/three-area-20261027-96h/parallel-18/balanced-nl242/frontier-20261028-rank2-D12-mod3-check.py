#!/opt/homebrew/bin/python3
"""A rank-two D12 modulo-three/collective near miss, not a Boolean witness."""
import argparse
import json
import pathlib


def fw(a):
    a=list(a);step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(i,i+step):x,y=a[j],a[j+step];a[j]=x+y;a[j+step]=x-y
        step*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    pts=[209,232,162,25,92,180,3,156,116,216,24,129]
    signs=[-1,1,-1,1,1,1,-1,-1,-1,1,-1,1];delta=[0]*256
    for x,e in zip(pts,signs):delta[x]=e
    assert sum(v!=0 for v in delta)==12
    u,w,lin,const=186,1,121,1
    Q=[(((u&x).bit_count()%2)*((w&x).bit_count()%2))^((lin&x).bit_count()%2)^const for x in range(256)]
    G=fw([-1 if z else 1 for z in Q]);Y=[y for y,z in enumerate(G) if z]
    assert len(Y)==4 and all(abs(G[y])==128 for y in Y)
    F=fw(delta);M=sum(z%3!=0 for z in F);b=sum(((1 if G[y]>0 else -1)*F[y])%3==1 for y in Y)
    assert (M,b)==(138,0) and M+3*b==144-12//2
    v=[]
    for y in range(256):
        r=(G[y]-F[y])%3;v.append(0 if r==0 else (1 if r==1 else -1))
    m=256-sum(z!=0 for z in v);S=sum((1 if G[y]>0 else -1)*v[y] for y in Y)
    n3=sum(delta[x]*(-1 if Q[x] else 1)==1 for x in pts);n1=12-n3
    assert (m,S,n1,n3)==(118,-2,5,7) and m==116+2*S+12//2
    assert sum((1 if G[y]>0 else -1)*F[y] for y in Y)==2*(n3-n1)
    V=fw(v);peakbad=sum(abs(z) not in (2,6,10,14) for z in V)
    nonodd=sum(z%4!=2 for z in V);qbad=sum(int((V[x]//2)%4==3)!=Q[x] for x in range(256))
    assert all(z%2==0 for z in V) and (max(map(abs,V)),peakbad,nonodd,qbad)==(40,140,128,144)
    out={'scope':'D12 rank2 modulo-three/count near miss; NOT a target witness',
         'positions':pts,'signs':signs,'Q_product_masks':[u,w],'Q_linear_mask':lin,'Q_constant':const,
         'D':12,'M':M,'b':b,'m':m,'S':S,'n1':n1,'n3':n3,'ternary_v':v,
         'Walsh_v_peak':40,'odd_peak_failures':peakbad,'odd_nonparity_positions':nonodd,
         'odd_Q_mismatches':qbad,'collective_and_mod3_identities_hold':True}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('D12 coarse model: M138 b0 m118 S−2; fails peak/parity/Q, NON-WITNESS')


if __name__=='__main__':main()
