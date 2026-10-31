#!/usr/bin/env python3
"""Independent exact verifier for a 4x4 PPT/SN<=2 full-support certificate.

Uses only standard-library integers and Fraction. It independently reconstructs
the physical state, all complex rank minors, all projector entries, and PPT.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
HERE=Path(__file__).parent
CERT=HERE/'frontier-20261028-grid-generic-exact-certificate-v1.json'


def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,n):return (a[0]*n,a[1]*n)
def conj(a):return (a[0],-a[1])
ZERO=(0,0)


def projected_4M(z):
    a,b,c,d,e,f,g,i,h=z
    return [[scale(a,4),scale(b,4),scale(c,4),scale(h,4)],
            [scale(d,4),scale(a,4),scale(b,4),ZERO],
            [add(scale(e,4),f),add(scale(neg(d),4),f),add(scale(a,4),f),f],
            [add(scale(g,4),e),e,add(scale(i,4),e),add(e,scale(c,4))]]


def minor3(m,r,c):
    a,b,d=r;x,y,z=c
    t1=mul(m[a][x],add(mul(m[b][y],m[d][z]),neg(mul(m[b][z],m[d][y]))))
    t2=mul(m[a][y],add(mul(m[b][x],m[d][z]),neg(mul(m[b][z],m[d][x]))))
    t3=mul(m[a][z],add(mul(m[b][x],m[d][y]),neg(mul(m[b][y],m[d][x]))))
    return add(add(t1,neg(t2)),t3)


def physical_source():
    def ket(*terms):
        v=[0]*20
        for a,b,c in terms:v[5*a+b]+=c
        return v
    terms=[(1,ket((0,0,1),(1,1,1),(2,2,1))),
           (1,ket((0,1,1),(1,2,1))),(1,ket((1,0,1),(2,1,-1))),
           (3,ket((0,2,1),(3,4,1))),(3,ket((2,0,1),(3,3,1))),
           (3,ket((2,3,1))),(3,ket((3,0,1))),(3,ket((3,2,1))),(3,ket((0,4,1)))]
    R=[[0]*20 for _ in range(20)]
    for w,v in terms:
        for i,x in enumerate(v):
            for j,y in enumerate(v):R[i][j]+=w*x*y
    return R


def state_4K():
    # 4*K, with K|3>=(|0>+|1>+|2>+|3>)/4 and K|4>=|3>.
    K=((4,0,0,1,0),(0,4,0,1,0),(0,0,4,1,0),(0,0,0,1,4))
    R=physical_source()
    return [[sum(K[b][x]*R[5*a+x][5*c+y]*K[d][y] for x in range(5) for y in range(5))
             for c in range(4) for d in range(4)] for a in range(4) for b in range(4)]


def pt(m):
    return [[m[4*(i//4)+(j%4)][4*(j//4)+(i%4)] for j in range(16)] for i in range(16)]


def psd(m):
    a=[[F(x) for x in row] for row in m];pivots=[]
    while a:
        if any(a[i][i]<0 for i in range(len(a))):raise AssertionError('negative Schur diagonal')
        p=next((i for i in range(len(a)) if a[i][i]>0),None)
        if p is None:
            if any(x for row in a for x in row):raise AssertionError('nonzero zero-diagonal block')
            break
        s=a[p][p];pivots.append(str(s));keep=[i for i in range(len(a)) if i!=p]
        a=[[a[i][j]-a[i][p]*a[p][j]/s for j in keep] for i in keep]
    return pivots


def main():
    c=json.loads(CERT.read_text()); denominator=int(c['common_denominator'])
    if denominator<=0:raise AssertionError('bad common denominator')
    sums=[[(0,0) for _ in range(16)] for _ in range(16)]
    gram=[[(0,0) for _ in range(9)] for _ in range(9)]
    for entry in c['atoms']:
        weight=int(entry['weight_numerator'])
        if weight<=0:raise AssertionError('nonpositive coefficient')
        z=[(int(x),int(y)) for x,y in entry['coefficients']]
        if len(z)!=9:raise AssertionError('bad coefficient vector')
        M=projected_4M(z)
        for rr in combinations(range(4),3):
            for cc in combinations(range(4),3):
                if minor3(M,rr,cc)!=ZERO:raise AssertionError('rank>2 atom')
        flat=[x for row in M for x in row]
        for i in range(16):
            for j in range(16):sums[i][j]=add(sums[i][j],scale(mul(flat[i],conj(flat[j])),weight))
        for i in range(9):
            for j in range(9):gram[i][j]=add(gram[i][j],scale(mul(z[i],conj(z[j])),weight))
    diag=(1,1,3,1,3,3,3,3,3)
    for i in range(9):
        for j in range(9):
            if gram[i][j]!=(denominator*diag[i] if i==j else 0,0):
                raise AssertionError(('coefficient Gram mismatch',i,j))
    T=state_4K()
    for i in range(16):
        for j in range(16):
            if sums[i][j]!=(denominator*T[i][j],0):
                raise AssertionError(('physical matrix mismatch',i,j))
    state_piv=psd(T);pt_piv=psd(pt(T))
    # Core after keeping Alice/Bob output coordinates 0,1,2. T=16*R_K.
    c_aa=F(T[0][0],16); c_bb=F(T[1][1],16); c_ab=F(T[0][1],16)
    j21=4*2+1; j10=4*1+0
    c_ff=F(16*(T[j21][j21]+T[j21][j10]+T[j10][j21]+T[j10][j10]),16)
    if (c_aa,c_bb,c_ab,c_ff)!=(F(1),F(1),F(0),F(3)):
        raise AssertionError(('unexpected entanglement moments',c_aa,c_bb,c_ab,c_ff))
    print(json.dumps({'positive_weights':len(c['atoms']),'rank_minor_checks':16*len(c['atoms']),
                      'coefficient_gram_entries_checked':81,'physical_state_entries_checked':256,
                      'mismatches':0,'trace_4K_state':sum(T[i][i] for i in range(16)),
                      'state_rank':len(state_piv),'partial_transpose_rank':len(pt_piv),
                      'state_schur_pivots':state_piv,'partial_transpose_schur_pivots':pt_piv,
                      'entanglement_moments':{'C_aa':str(c_aa),'C_bb':str(c_bb),
                                              'C_ab':str(c_ab),'C_ff':str(c_ff),
                                              'necessary_if_separable':'4 <= 3/8 (false)'}},indent=2))


if __name__=='__main__':main()
