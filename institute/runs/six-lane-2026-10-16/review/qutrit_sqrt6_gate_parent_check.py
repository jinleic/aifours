"""Parent exact check of the Codex-proposed second attaining gate, built from normal-form data:
N0=R0=I/2, N1=Q1=R1=T1=tZ, N2=Q2=tX, R2=T2=-tX, Omega_ad=-(1/2)delta_ad I, t=sqrt(6)/4.
phi(a,b,c,d)=U[(c,d),(a,b)]; |ij> <-> 3i+j; <ij|U^R|ab> = <ia|U|jb>; <ib|U^Gamma|ja> = <ia|U|jb>.
Checks U U^dag = I, U^R unitary, U^Gamma U^Gamma^dag = (3/4)(I+S), rank U^Gamma = 6, e_p = 15/16 via
1 - e_p = (tr W^2 - 9)/72. Usage: python -B qutrit_sqrt6_gate_parent_check.py NEW_RECEIPT.json (needs sympy)
"""
from datetime import datetime
from itertools import product
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo
import sympy as sp


def main():
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    t = sp.sqrt(6) / 4
    I2 = sp.eye(2)
    X = sp.Matrix([[0, 1], [1, 0]])
    Z = sp.Matrix([[1, 0], [0, -1]])
    N = {0: I2 / 2, 1: t * Z, 2: t * X}
    Q = {1: t * Z, 2: t * X}
    R = {0: I2 / 2, 1: t * Z, 2: -t * X}
    T = {1: t * Z, 2: -t * X}
    Om = {(a, d): (-sp.Rational(1, 2) * I2 if a == d else sp.zeros(2, 2)) for a, d in product((1, 2), repeat=2)}

    def phi(a, b, c, d):
        if a == 0 and d == 0:
            if b == 0 and c == 0:
                return 1
            return N[0][b - 1, c - 1] if b and c else 0
        if a == 0:
            return N[d][b - 1, c - 1] if b and c else 0
        if d == 0:
            return Q[a][b - 1, c - 1] if b and c else 0
        if b == 0 and c == 0:
            return R[0][a - 1, d - 1]
        if b == 0:
            return R[c][a - 1, d - 1]
        if c == 0:
            return T[b][a - 1, d - 1]
        return Om[a, d][b - 1, c - 1]

    U = sp.zeros(9, 9)
    for a, b, c, d in product(range(3), repeat=4):
        U[3 * c + d, 3 * a + b] = phi(a, b, c, d)
    UR = sp.zeros(9, 9)
    UG = sp.zeros(9, 9)
    for i, a, j, b in product(range(3), repeat=4):
        UR[3 * i + j, 3 * a + b] = U[3 * i + a, 3 * j + b]
        UG[3 * i + b, 3 * j + a] = U[3 * i + a, 3 * j + b]
    S = sp.zeros(9, 9)
    for i, j in product(range(3), repeat=2):
        S[3 * j + i, 3 * i + j] = 1
    W = (UG * UG.H).applyfunc(sp.nsimplify)
    checks = {
        'unitary': (U * U.H).applyfunc(sp.simplify) == sp.eye(9),
        'realignment_unitary': (UR * UR.H).applyfunc(sp.simplify) == sp.eye(9),
        'self_realigned': (UR - U).applyfunc(sp.simplify) == sp.zeros(9, 9),
        'W_equals_three_quarters_I_plus_S': (W - sp.Rational(3, 4) * (sp.eye(9) + S)).applyfunc(sp.simplify) == sp.zeros(9, 9),
        'rank_U_Gamma_is_6': UG.rank(simplify=True) == 6,
        'not_2_unitary': W.applyfunc(sp.simplify) != sp.eye(9),
    }
    trW2 = sp.simplify((W * W).trace())
    ep = sp.simplify(1 - (trW2 - 9) / 72)
    checks['entangling_power_15_16'] = ep == sp.Rational(15, 16)
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'checks': checks,
              'trace_W2': str(trW2), 'e_p': str(ep),
              'status': 'PARENT_EXACT_SQRT6_ATTAINING_GATE_PASS' if all(checks.values()) else 'FAILED'}
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=1))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
