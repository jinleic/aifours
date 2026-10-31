#!/opt/homebrew/bin/python3
"""Controls for rank-four modulo-three signed-support identity."""
import argparse
import collections
import json
import pathlib


def fw(a):
    a=list(a);s=1
    while s<len(a):
        for i in range(0,len(a),2*s):
            for j in range(i,i+s):x,y=a[j],a[j+s];a[j]=x+y;a[j+s]=x-y
        s*=2
    return a


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    d6={}
    nz=[x for x in range(64) if (6-2*x.bit_count())%3!=0]
    assert len(nz)==42 and 4*len(nz)==168
    for weight in (4,6):
        rel=(1<<weight)-1
        d6[str(weight)]={str(s):8*sum(((x&rel).bit_count()%2)==s for x in nz) for s in (0,1)}
    assert {v for row in d6.values() for v in row.values()}=={96,144,192,240}
    # A concrete D=8 ternary inverse passes the modulo-three count and collective m/S identity,
    # but fails both the odd peak bound and the prescribed odd quadratic.
    points=[216,157,49,209,29,252,168,12];signs=[-1,1,1,-1,-1,-1,1,1];delta=[0]*256
    for x,e in zip(points,signs):delta[x]=e
    F=fw(delta);M=sum(x%3!=0 for x in F);assert M==152
    lin=92;const=1
    Q=[(((x&1)*((x>>1)&1))^(((x>>2)&1)*((x>>3)&1))^((lin&x).bit_count()%2)^const) for x in range(256)]
    G=fw([-1 if v else 1 for v in Q]);Y=[y for y,v in enumerate(G) if v]
    assert len(Y)==16 and all(abs(G[y])==64 for y in Y)
    a0=sum(F[y]%3==0 for y in Y);assert a0==0 and M+3*a0==156-8//2
    v=[]
    for y in range(256):
        r=(G[y]-F[y])%3;v.append(0 if r==0 else (1 if r==1 else -1))
    m=256-sum(t!=0 for t in v);S=sum((1 if G[y]>0 else -1)*v[y] for y in Y)
    n3=sum(delta[x]*(-1 if Q[x] else 1)==1 for x in points);n1=8-n3
    assert (m,S,n1,n3)==(110,-10,3,5) and m==116+S+8//2
    assert sum((1 if G[y]>0 else -1)*F[y] for y in Y)==4*(n3-n1)
    fv=fw(v);qbad=sum(int((fv[x]//2)%4==3)!=Q[x] for x in range(256))
    peakbad=sum(abs(t) not in (2,6,10,14) for t in fv)
    assert all(t%4==2 for t in fv) and max(map(abs,fv))==50 and peakbad==43 and qbad==256
    out={'scope':'six-atom exact finite controls and D8 modulo-three near miss; NOT a target witness',
         'D6_rank5_M':168,'D6_rank4_M_by_relation_weight_and_syndrome':d6,
         'D6_rank3_M_multiple_of_32':True,'D8_nearmiss':{'positions':points,'signs':signs,
           'Q_linear_mask':lin,'Q_constant':const,'M':M,'a':a0,'m':m,'S':S,'n1':n1,'n3':n3,
           'maximum_abs_Walsh_v':50,'odd_peak_failures':peakbad,'odd_Q_mismatches':qbad}}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('D6 residue cases checked; D8 coarse control passes collective identity but fails target peak/Q')


if __name__=='__main__':main()
