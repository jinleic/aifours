#!/opt/homebrew/bin/python3
"""Corrected mod3, odd-energy and bounded q/Q profile checks; no Boolean witness."""
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


def profiles(rank):
    N=1<<rank;mmax=122 if rank==2 else 112
    Ds=range(12,29,4) if rank==2 else range(8,25,2)
    rows=[]
    for D in Ds:
        choices={a-b for a in range(N+1) for b in range(N+1-a) if (a+2*b)%3==0}
        for S in sorted(choices):
            m=116+D//2+(2 if rank==2 else 1)*S
            if m%2 or m>mmax or m<0:continue
            for n1 in range(D+1):
                n3=D-n1;hnum=8*(m-60)-2*D-4*n1
                if hnum%3:continue
                h=hnum//3;n5=h-n3;n7=256-h-n1
                if min(n3,n5,n7)<0:continue
                rows.append({'D':D,'m':m,'S':S,'n1':n1,'n3':n3,'n5':n5,'n7':n7})
    return rows


def main():
    p=argparse.ArgumentParser();p.add_argument('--control',type=pathlib.Path,required=True)
    p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    rows2=profiles(2);rows4=profiles(4)
    assert len(rows2)==29 and {v['D'] for v in rows2}=={12,16,20,24}
    assert {v['m'] for v in rows2}=={116,118,120,122}
    assert (min(v['n7'] for v in rows2),max(v['n7'] for v in rows2))==(99,118)
    assert len(rows4)==40 and {v['D'] for v in rows4}=={8,10,12,14,16,18,22}
    assert {v['m'] for v in rows4}=={106,108,110,112}
    assert (min(v['n7'] for v in rows4),max(v['n7'] for v in rows4))==(124,143)
    # For rank two, D=28 forces S=-4, but a=0,b=4 has a+2b=8, not 0 mod3.
    assert not any(A-B==-4 and (A+2*B)%3==0 for A in range(5) for B in range(5-A))
    # Balanced Q: Z64/128 structure bounds signed delta class X to [-2,2].
    # For allowed odd-half first sum 0/128, exact 12H = s+16X forces:
    feasible=[]
    for X in range(-2,3):
        for s in (0,128):
            if (s+16*X)%12==0:feasible.append((X,s))
    assert feasible==[(0,0),(-2,128),(1,128)] or set(feasible)=={(0,0),(-2,128),(1,128)}
    # Enumerate c0,c1 (unit switches) and d0,d1 (nonswitch 3s) in balanced Q classes.
    # E=2X, H0=wt(v0-v1)=2(d0+d1), and Q-switch modulation obeys |c0-d0|,|d1-c1|<=1.
    qbalanced=[]
    for row in rows2:
        D=row['D'];n1=row['n1'];n3=row['n3'];H=n3+row['n5']
        for X,s in feasible:
            H0=(s+16*X)//12
            for c0 in range(n1+1):
                c1=n1-c0
                if c0-c1!=X:continue
                for d0 in range(H0//2+1):
                    d1=H0//2-d0
                    if d1-d0!=X or abs(c0-d0)>1 or abs(d1-c1)>1:continue
                    n10=c0+d0;n11=c1+d1
                    if n1!=2*n10-7+X:continue
                    nr0=n10-H0//2;nr1=n11-H0//2
                    if min(nr0,nr1)<0 or nr0+nr1!=n3:continue
                    for t00 in (n10//2,(n10+1)//2):
                        t01=n10-t00
                        for t10 in (nr1//2,(nr1+1)//2):
                            for t11 in (nr0//2,(nr0+1)//2):
                                A=t00+t10;B=t01+t11
                                if 2*A-n1==X and 2*B-n3==X:
                                    qbalanced.append((row,X,s,c0,c1,d0,d1,A,B))
    assert not qbalanced
    # Explicit D12 modulo-three and collective near miss; it fails full inverse caller.
    ctrl=json.loads(a.control.read_text());v=ctrl['ternary_v'];D=ctrl['D'];M=ctrl['M'];b=ctrl['b']
    assert len(v)==256 and D==12 and M==138 and M%3==D%3 and M+3*b==144-D//2
    assert ctrl['odd_peak_failures']==140 and ctrl['odd_nonparity_positions']==128 and ctrl['odd_Q_mismatches']==144
    out={'scope':'exact corrected necessary-profile arithmetic; D12 control is NON-WITNESS',
         'rank2_profiles':rows2,'rank4_profiles':rows4,'Qbalanced_first_moment_Xs':feasible,
         'balanced_Q_coarse_sign_solutions':len(qbalanced),'D28_forced_a_b':[0,4],
         'D12_mod3_control':{'D':D,'M':M,'b':b,'m':ctrl['m'],'S':ctrl['S'],
                             'peak_failures':140,'odd_parity_failures':128,'Q_mismatches':144}}
    with a.output.open('x',encoding='utf-8') as dst:json.dump(out,dst,indent=2,sort_keys=True);dst.write('\n')
    print('M≡D, M≡256−m: rank2 D28 impossible; rank4 D=20,24 impossible; D12 coarse control remains')


if __name__=='__main__':main()
