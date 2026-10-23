"""Exact certification that the diamond FDs do NOT imply Ingleton(U,V;P,Q).

Distribution: P,Q independent uniform bits, U = P AND Q, V = P OR Q (four atoms, probability 1/4 each).
FDs checked on the support: U,V functions of (P,Q); P function of (U,Q,V); Q function of (U,P,V).
Every entropy is a + b*log2(3) with rational a,b (probabilities are multiples of 1/4); we compute these
pairs exactly and decide the sign of the Ingleton expression by an integer power comparison.
These are exactly the conditional FDs of (X3,X10,X4,X8) given Z={1,2,5,6,7,9} in R^-:
3 and 10 are functions of (4,8) (their other neighbours lie in Z), 4 = f(3,8,10 | Z), 8 = f(3,4,10 | Z).
"""
from fractions import Fraction as Fr
from collections import Counter
import json, sys

atoms = [(p, q, p & q, p | q) for p in (0, 1) for q in (0, 1)]  # (P,Q,U,V)
P, Q, U, V = 0, 1, 2, 3

def is_function(src, dst):
    seen = {}
    for a in atoms:
        k = tuple(a[i] for i in src); val = tuple(a[i] for i in dst)
        if seen.setdefault(k, val) != val: return False
    return True

def ent(idx):
    """H in bits as (rational, coefficient of log2 3) for the uniform distribution on the 4 atoms."""
    cnt = Counter(tuple(a[i] for i in idx) for a in atoms)
    a = Fr(0); b = Fr(0)
    for c in cnt.values():
        p = Fr(c, 4)
        # -p log2 p with p in {1/4,1/2,3/4,1}: log2(3/4) = log2 3 - 2
        if p == 1: continue
        if p == Fr(1, 4): a += p * 2
        elif p == Fr(1, 2): a += p * 1
        elif p == Fr(3, 4): a += -p * (-2); b += -p
        else: raise ValueError(p)
    return a, b

def I(x, y, z=()):
    hxz, hyz, hxyz = ent(x + z), ent(y + z), ent(x + y + z)
    hz = ent(z) if z else (Fr(0), Fr(0))
    return (hxz[0] + hyz[0] - hxyz[0] - hz[0], hxz[1] + hyz[1] - hxyz[1] - hz[1])

terms = [I((U,), (V,), (P,)), I((U,), (V,), (Q,)), I((P,), (Q,)), I((U,), (V,))]
ing = (terms[0][0] + terms[1][0] + terms[2][0] - terms[3][0], terms[0][1] + terms[1][1] + terms[2][1] - terms[3][1])
a, b = ing   # Ingleton = a + b*log2(3)
# sign: a + b log2 3 < 0  <=>  2^(a) * 3^(b) < 1 ; clear denominators: 2^(a*D) * 3^(b*D) < 1
D = a.denominator * b.denominator // __import__("math").gcd(a.denominator, b.denominator)
A, Bx = int(a * D), int(b * D)
lhs_num = (2 ** max(A, 0)) * (3 ** max(Bx, 0)); lhs_den = (2 ** max(-A, 0)) * (3 ** max(-Bx, 0))
negative = lhs_num < lhs_den
out = dict(fd_U_of_PQ=is_function((P, Q), (U,)), fd_V_of_PQ=is_function((P, Q), (V,)),
           fd_P_of_UQV=is_function((U, Q, V), (P,)), fd_Q_of_UPV=is_function((U, P, V), (Q,)),
           I_UV_given_P=str(terms[0]), I_UV_given_Q=str(terms[1]), I_PQ=str(terms[2]), I_UV=str(terms[3]),
           ingleton_rational_part=str(a), ingleton_log2_3_coeff=str(b),
           integer_comparison=f"2^{A}*3^{Bx} < 1  <=>  {lhs_num} < {lhs_den}", ingleton_negative=negative)
print(json.dumps(out, indent=1))
if not (all(out[k] for k in out if k.startswith("fd_")) and negative and terms[0] == terms[1] == terms[2] == (0, 0)):
    sys.exit(1)
