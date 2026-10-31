#!/usr/bin/env python3
"""Exact finite checks of the spin-flip projector-budget candidate.

Checks only one physical pure input, two actual rank-three projectors (one
complex), and three actual physical p values. Integer and Fraction arithmetic;
no NumPy, floats, author helper imports, files, or optimization.
"""
import itertools
import json
from fractions import Fraction as F

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
AMPS = {0: 3, 3: 1, 5: 1, 14: 1}


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def conjugate(a):
    return (a[0], -a[1])


def matmul(A, B):
    C = {}
    for (i, k), a in A.items():
        for (j, m), b in B.items():
            if k == j:
                C[i, m] = add(C.get((i, m), ZERO), mul(a, b))
    return {k:v for k,v in C.items() if v != ZERO}


def trace(A):
    out = ZERO
    for (i, j), val in A.items():
        if i == j:
            out = add(out, val)
    return out


def transpose(A):
    return {(j, i):v for (i, j),v in A.items()}


def gamma(A, *, conjugate_entries=True):
    # Theta=Y^tensor4 K sends |x> to (-1)^wt(x)|15-x>.
    return {(15-i, 15-j):tuple(F((-1)**((i.bit_count()+j.bit_count())%2))*z
                                   for z in (conjugate(v) if conjugate_entries else v))
            for (i,j),v in A.items()}


def pauli_expect(A, labels):
    flip = sum(1 << (3-i) for i,a in enumerate(labels) if a in (1, 2))
    ny = labels.count(2)
    phase = (ONE, (F(0),F(1)), (F(-1),F(0)), (F(0),F(-1)))[ny % 4]
    out = ZERO
    for x in range(16):
        sign = (-1)**sum((x >> (3-i)) & 1 for i,a in enumerate(labels) if a in (2,3))
        out = add(out, mul(A.get((x,x^flip),ZERO), (sign*phase[0],sign*phase[1])))
    assert out[1] == 0
    return out[0]


def weights(A):
    B = [F(0)]*5
    for labels in itertools.product(range(4), repeat=4):
        value = pauli_expect(A, labels)
        B[sum(a != 0 for a in labels)] += value*value
    return B


def bit(x, i):
    return (x >> (3-i)) & 1


def channel_entry(u, v, s):
    a, b = (1+s)/2, (1-s)/2
    result = F(0)
    for x, ax in AMPS.items():
        for y, ay in AMPS.items():
            term = F(ax*ay, 12)
            for i in range(4):
                ui,vi,xi,yi = bit(u,i),bit(v,i),bit(x,i),bit(y,i)
                if ui != vi:
                    if (ui,vi) != (xi,yi):
                        term = F(0)
                        break
                    term *= s
                else:
                    if xi != yi:
                        term = F(0)
                        break
                    term *= a if xi == ui else b
            result += term
    return result


def channel_trace(Q, s):
    out = ZERO
    for (i,j), val in Q.items():
        element = channel_entry(j,i,s)
        out = add(out, (val[0]*element,val[1]*element))
    assert out[1] == 0
    return out[0]


def sector_data(rho, Q):
    B = weights(Q)
    Qt = gamma(Q)
    assert matmul(Q,Q) == Q and trace(Q) == (F(3),F(0))
    assert matmul(Qt,Qt) == Qt and trace(Qt) == (F(3),F(0))
    kappa = trace(matmul(Q,Qt))
    assert kappa[1] == 0
    kap = kappa[0]
    assert B[1]+B[3] == 24-8*kap
    assert B[2]+B[4] == 15+8*kap
    assert B[1] <= min(F(20),24-8*kap)
    q = trace(matmul(Q,rho))
    qtilde = trace(matmul(Qt,rho))
    assert q[1] == qtilde[1] == 0
    diff = q[0]-qtilde[0]
    assert diff*diff <= 3-kap
    return B,kap,diff


def main():
    rho = {(i,j):(F(a*b,12),F(0)) for i,a in AMPS.items() for j,b in AMPS.items()}
    assert trace(rho) == ONE and matmul(rho,rho) == rho
    assert trace(matmul(rho,gamma(rho))) == ZERO
    A = weights(rho)
    assert A == [F(1),F(73,36),F(145,36),F(215,36),F(107,36)]
    Qdiag = {(i,i):ONE for i in (0,3,5)}
    Qcomplex = {
        (0,0):ONE,(5,5):ONE,(3,3):(F(1,2),F(0)),(15,15):(F(1,2),F(0)),
        (3,15):(F(0),F(-1,2)),(15,3):(F(0),F(1,2))
    }
    assert gamma(Qcomplex) != gamma(Qcomplex,conjugate_entries=False)
    Qs = {'diagonal':Qdiag, 'complex':Qcomplex}
    data = {}
    for name,Q in Qs.items():
        B,kap,diff=sector_data(rho,Q)
        if name == 'diagonal':
            assert B == [F(9),F(12),F(6),F(12),F(9)] and kap == 0 and diff == F(11,12)
        else:
            assert B[1] == 6 and kap == 1 and diff == F(1,2)
        cases=[]
        for p in (F(9,16),F(2,3),F(4,3)):
            s=1-p; t=abs(s)
            actual=channel_trace(Q,s)
            direct=F(0)
            for labels in itertools.product(range(4),repeat=4):
                wt=sum(a != 0 for a in labels)
                direct += s**wt * pauli_expect(rho,labels)*pauli_expect(Q,labels)
            assert direct/16 == actual
            ref=(3+8*t+6*t*t-t**4)/16
            assert actual <= ref
            cases.append({'p':str(p),'trace':str(actual),'reference':str(ref),'actual_gap':str(ref-actual)})
        data[name]={'Pauli_weight_norms':list(map(str,B)),'kappa':str(kap),'q_minus_qtilde':str(diff),'cases':cases}
    S,L=F(73,36),F(35,6)
    t=F(7,16)
    H=A[2]+t*t*A[3]+t**4*A[4]
    He=A[2]+t**4*A[4]
    u=L*L/S
    x0=39*S/(S+t*t*H)
    z0=39*(1-t*t)**2*S/((1-t*t)**2*S+t*t*He)
    T=8+6*t-t**3
    old_fail=H*(39-u)-((T-L)/t)**2
    root0=F(48,5)**2-He*(39-u)
    root1=F(81,20)**2-8*S
    root2=F(51,4)**2-39*He
    U0=(1-t*t)*L+8*t*t+t*F(48,5)
    U2=(1-t*t)*F(81,20)+8*t*t+t*F(51,4)
    assert x0>u and old_fail>0 and z0>u
    assert all(z>0 for z in (root0,root1,root2,T-U0,T-U2))
    assert U0>U2 and T-U0 == F(1909,20480)
    gap=t*(T-U0)/16
    assert gap == F(13363,5242880)
    delta=8-L
    d_fail=39*(15-S)-(5+delta/t)**2
    assert d_fail == F(717713,1764)>0
    print(json.dumps({'scope':'Exact constants and two specified actual projectors only; not a universal proof',
        'input_A':list(map(str,A)),'t':str(t),'physical_p':'9/16','H_t':str(H),'H_even':str(He),
        'projectors':data,'old_186_optimizer_x0_minus_u':str(x0-u),
        'old_186_squared_failure_slack':str(old_fail),'new_branch_y0_minus_u':str(z0-u),
        'new_root_squared_slacks':list(map(str,(root0,root1,root2))),
        'new_branch_upper_0':str(U0),'new_branch_upper_2':str(U2),
        'reference_bracket_minus_upper':str(T-U0),'proven_gap_lower':str(gap),
        'prior_D_failure_squared_slack':str(d_fail),
        'wrong_no_transpose_on_complex_projector_detected':True},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
