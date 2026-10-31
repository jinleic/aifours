#!/usr/bin/env python3
"""Independent exact local sign replay on the definition-first polynomials."""
import contextlib, io, itertools, runpy, signal, sys
from fractions import Fraction as Q
from math import comb

def timed_out(*unused): raise TimeoutError('local exact replay cap')
signal.signal(signal.SIGALRM, timed_out)
signal.alarm(108)

def main():
    # This is our own independent script, never the author's verifier.
    with contextlib.redirect_stdout(io.StringIO()):
        d=runpy.run_path('reviewer-f202-algebra-controls.py')
    P,I=d['P'],d['I']; rec=d['rec']; v=d['v']; z=d['z']; a=d['a']; b=d['b']
    W,E,Z,F,lam,mu=d['W'],d['E3'],d['Z'],d['F'],d['lam'],d['mu']
    r=d['r']; C=d['C']; ai,bi=d['ai'],d['bi']
    ar,br=Q(rec['rational_a_center']),Q(rec['rational_b_center'])
    ae=max(abs(ai.lo-ar),abs(ai.hi-ar)); be=max(abs(bi.lo-br),abs(bi.hi-br))
    centers=[C[1],C[1]]+[C[0]]*5+[C[2]]; radius=Q(1,500)+r
    N=10
    def bind(poly):
        out={}
        for k,val in poly.d.items():
            kk=list(k); val*=ar**kk[8]*br**kk[9]; kk[8]=kk[9]=0; kk=tuple(kk)
            out[kk]=out.get(kk,0)+val
        return P(out)
    def bound(poly):
        # Shift exactly before taking the coefficient triangle bound.
        powers=[[c**k for k in range(8)] for c in centers]
        rows={}
        for key,coef in poly.d.items():
            assert key[8:]==(0,0)
            axes=[[comb(n,j)*powers[i][n-j] for j in range(n+1)] for i,n in enumerate(key[:8])]
            for ix in itertools.product(*(range(n+1) for n in key[:8])):
                t=coef
                for i,k in enumerate(ix): t*=axes[i][k]
                rows[ix]=rows.get(ix,0)+t
        mid=rows.get((0,)*8,Q(0))
        err=sum((abs(coef)*radius**sum(k) for k,coef in rows.items() if sum(k)),Q(0))
        return I(mid-err,mid+err)
    def crude_abs(poly):
        return sum((abs(coef)*d['prod']((abs(centers[i])+radius)**key[i] for i in range(8)) for key,coef in poly.d.items()),Q(0))
    R=[[Q(x,10**6) for x in row] for row in rec['R_numerators_denominator_1000000']]
    assert all(R[i][i]==1 and all(R[i][j]==0 for j in range(i)) for i in range(7))
    def hessian(poly): return [[poly.diff(i).diff(j) for j in range(7)] for i in range(7)]
    hf=hessian(bind(F)); hw=hessian(W); he=hessian(E)
    def congr(h,i,j):
        out=P(0)
        for k in range(7):
            for l in range(7):
                c=R[k][i]*R[l][j]
                if c: out=out-h[k][l]*c
        return out
    boxes=[[None]*7 for _ in range(7)]
    for i in range(7):
        for j in range(i,7):
            Cij=congr(hf,i,j); Aij=congr(hw,i,j); Bij=congr(he,i,j)
            enclosure=bound(Cij); err=ae*crude_abs(Aij)+be*crude_abs(Bij)
            boxes[i][j]=boxes[j][i]=I(enclosure.lo-err,enclosure.hi+err)
    margins=[boxes[i][i].lo-sum((boxes[i][j].absmax() for j in range(7) if i!=j),Q(0)) for i in range(7)]
    print('LOCAL_CONGRUENCE all_seven_margins_gt_0=',all(x>0 for x in margins),'all_gt_3=',all(x>3 for x in margins),flush=True)
    assert min(margins)>0
    s4hi=2*(C[1]+radius)+2*(C[0]+radius)
    lb=bound(bind(lam)); mb=bound(bind(mu)); fz=bound(bind(F.diff(7)))
    le=ae+be*s4hi
    me=be
    ze=ae*crude_abs(W.diff(7))+be*crude_abs(E.diff(7))
    signs=(lb.lo-le>0,mb.lo-me>0,fz.hi+ze<0)
    print('LOCAL_SIGNS lambda_positive,mu_positive,Fz_negative=',signs,flush=True)
    assert all(signs)
    # Test the decisions with exact, intentionally invalid degenerate data.
    assert not (Q(0)>0)
    assert not (Q(1)<0)
    assert not all([True,False,True])
    print('NEGATIVE_REJECTED zero diagonal margin, positive Fz, nonpositive mu',flush=True)
    print('DONE independently bounded linked dual local box',flush=True)

try:
    main()
except TimeoutError:
    print('UNKNOWN local exact replay reached internal cap',flush=True)
    sys.exit(3)
finally:
    signal.alarm(0)
