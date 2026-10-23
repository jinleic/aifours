"""Exact verification of two attaining gates for the 15/16 bound (sympy, no floating point).

W1  U_s(2pi/3) := S * U(2pi/3), U(theta) = thesis eq. (3.36) as transcribed in gates.py (entries in Q(sqrt3)).
W2  H over Q(sqrt6): the normal-form data proposed in the parent's Codex hostile review
    (institute/runs/six-lane-2026-10-16/review/qutrit-sharp-codex-hostile-review-v1.note.md, lines 98-111):
      N_0 = R_0 = I/2;  N_1 = Q_1 = R_1 = T_1 = tZ;  N_2 = Q_2 = tX;  R_2 = T_2 = -tX;  Omega_ad = -(1/2) delta_ad I;
      t = sqrt6/4;  assembled with the lane normal-form conventions
      phi(a,b,c,d) = H[(c,d),(a,b)], phi(0000) = 1, N_d[b,c] = phi(0,b,c,d), Q_a[b,c] = phi(a,b,c,0),
      R_c[a,d] = phi(a,0,c,d), T_b[a,d] = phi(a,b,0,d), Omega_ad[b,c] = phi(a,b,c,d) (a,b,c,d in K = {1,2}),
      all other entries 0.
For each gate: unitary; realignment G^R unitary (dual) and equal to G (self-dual); W := G^Gamma G^Gamma^dag satisfies
W^2 = (3/2) W, tr W = 9, tr W^2 = 27/2, rank W = rank G^Gamma = 6 (so G^Gamma is not unitary: not 2-unitary);
e_p = [E(G) + E(GS) - E(S)]/E(S) = 15/16 with E(X) = 1 - tr[(X^R X^R^dag)^2]/81.  For H also W == (3/4)(I + S).
Mutation controls must FAIL.  The script prints the integer tables 2*U_s and 4*H (tokens s3 = sqrt3, s6 = sqrt6).
Usage:  python -B witnesses_exact.py                 -> ../evidence/witnesses_exact.json
        python -B witnesses_exact.py --check-doc F   -> exit 0 iff the tables in F match the exact matrices
"""
import json
import os
import re
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402

R3 = range(3)
I9 = sp.eye(9)
S9 = sp.Matrix(g.swap())
ix = lambda i, j: 3 * i + j


def realign(M):
    return sp.Matrix(g.realign(M.tolist()))


def ptrans(M):
    return sp.Matrix(g.ptrans(M.tolist()))


def zero(M):
    return M.applyfunc(sp.expand) == sp.zeros(*M.shape)


def E(X):
    XR = realign(X)
    A = (XR * XR.H).applyfunc(sp.expand)
    return 1 - sp.expand((A * A).trace()) / 81


def certify(G, name, extra_W=None):
    out = {}
    GH = G.H
    out["unitary G G^dag = I"] = zero(G * GH - I9)
    GR = realign(G)
    out["dual: G^R unitary"] = zero(GR * GR.H - I9)
    out["self-dual: G^R == G"] = zero(GR - G)
    GG = ptrans(G)
    W = (GG * GG.H).applyfunc(sp.expand)
    out["W^2 == (3/2) W"] = zero(W * W - sp.Rational(3, 2) * W)
    out["tr W"] = str(sp.nsimplify(sp.expand(W.trace())))
    out["tr W^2"] = str(sp.nsimplify(sp.expand((W * W).trace())))
    out["rank W (= rank G^Gamma)"] = int(W.rank(simplify=True))
    out["not 2-unitary (W != I)"] = not zero(W - I9)
    ep = sp.nsimplify(sp.expand((E(G) + E(G * S9) - E(S9)) / E(S9)))
    out["E(S)"] = str(sp.nsimplify(E(S9)))
    out["e_p"] = str(ep)
    if extra_W is not None:
        out["W == (3/4)(I + S)"] = zero(W - extra_W)
    ok = (out["unitary G G^dag = I"] and out["dual: G^R unitary"] and out["self-dual: G^R == G"]
          and out["W^2 == (3/2) W"] and out["tr W"] == "9" and out["tr W^2"] == "27/2"
          and out["rank W (= rank G^Gamma)"] == 6 and out["not 2-unitary (W != I)"] and out["e_p"] == "15/16"
          and out["E(S)"] == "8/9" and (extra_W is None or out["W == (3/4)(I + S)"]))
    out["all_ok"] = bool(ok)
    return out


def build_us():
    c, s = sp.Rational(-1, 2), sp.sqrt(3) / 2
    return S9 * sp.Matrix(g.U36(c, s, one=sp.Integer(1), zero=sp.Integer(0)))


def build_h(t=None, r2_sign=-1, omega=sp.Rational(-1, 2)):
    t = sp.sqrt(6) / 4 if t is None else t
    I2 = sp.eye(2)
    Z = sp.Matrix([[1, 0], [0, -1]])
    X = sp.Matrix([[0, 1], [1, 0]])
    N = [I2 / 2, t * Z, t * X]
    Q = [None, t * Z, t * X]
    Rm = [I2 / 2, t * Z, r2_sign * t * X]
    Tm = [None, t * Z, -t * X]
    phi = {}
    phi[(0, 0, 0, 0)] = sp.Integer(1)
    for d in R3:
        for b in (1, 2):
            for c in (1, 2):
                phi[(0, b, c, d)] = N[d][b - 1, c - 1]
    for a in (1, 2):
        for b in (1, 2):
            for c in (1, 2):
                phi[(a, b, c, 0)] = Q[a][b - 1, c - 1]
    for c in R3:
        for a in (1, 2):
            for d in (1, 2):
                phi[(a, 0, c, d)] = Rm[c][a - 1, d - 1]
    for b in (1, 2):
        for a in (1, 2):
            for d in (1, 2):
                phi[(a, b, 0, d)] = Tm[b][a - 1, d - 1]
    for a in (1, 2):
        for d in (1, 2):
            for b in (1, 2):
                for c in (1, 2):
                    phi[(a, b, c, d)] = omega * (1 if (a == d and b == c) else 0)
    H = sp.zeros(9, 9)
    for (a, b, c, d), v in phi.items():
        H[ix(c, d), ix(a, b)] = v
    return H


def tok(e, k):
    e = sp.nsimplify(sp.expand(e))
    if e.is_Integer:
        return str(int(e))
    q = sp.nsimplify(sp.expand(e / sp.sqrt(k)))
    assert q.is_Integer, (e, k)
    return ("" if q > 0 else "-") + ("" if abs(q) == 1 else str(abs(int(q)))) + "s%d" % k


def table(M, scale, k, label):
    return ["%s[%d] = " % (label, r) + " ".join("%4s" % tok(scale * M[r, cc], k) for cc in range(9)) for r in range(9)]


def parse_tables(path):
    pat = re.compile(r"^\s*(2Us|4H)\[(\d)\] =\s*(.*?)\s*$")
    got = {"2Us": {}, "4H": {}}
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = pat.match(line)
            if m:
                got[m.group(1)][int(m.group(2))] = m.group(3).split()
    return got


def untok(s):
    m = re.fullmatch(r"(-?)(\d*)s(\d+)", s)
    if m:
        coef = int(m.group(2)) if m.group(2) else 1
        return (-1 if m.group(1) else 1) * coef * sp.sqrt(int(m.group(3)))
    return sp.Integer(int(s))


def main():
    Us = build_us()
    H = build_h()
    if len(sys.argv) == 3 and sys.argv[1] == "--check-doc":
        got = parse_tables(sys.argv[2])
        ok = True
        for label, M, scale in (("2Us", Us, 2), ("4H", H, 4)):
            rows = got[label]
            ok &= sorted(rows) == list(range(9))
            for r in range(9):
                vals = rows.get(r, [])
                ok &= len(vals) == 9 and all(sp.expand(untok(v) - scale * M[r, cc]) == 0 for cc, v in enumerate(vals))
        # also certify the parsed matrices themselves
        if ok:
            Usd = sp.Matrix(9, 9, lambda r, cc: untok(got["2Us"][r][cc]) / 2)
            Hd = sp.Matrix(9, 9, lambda r, cc: untok(got["4H"][r][cc]) / 4)
            ok &= certify(Usd, "U_s(doc)")["all_ok"] and certify(Hd, "H(doc)", sp.Rational(3, 4) * (I9 + S9))["all_ok"]
        print(json.dumps({"doc": sys.argv[2], "tables_match_and_certify": bool(ok)}, indent=1))
        sys.exit(0 if ok else 1)
    out = {
        "W1 U_s(2pi/3) = S*U(2pi/3)": certify(Us, "U_s"),
        "W2 H over Q(sqrt6) (Codex normal-form data)": certify(H, "H", sp.Rational(3, 4) * (I9 + S9)),
        "W2 normal form: H[(00),(00)] == 1": H[0, 0] == 1,
        "W2 real entries in Q(sqrt6)": all(sp.nsimplify(e).is_real for e in H),
        "table 2*U_s (s3 = sqrt3)": table(Us, 2, 3, "2Us"),
        "table 4*H (s6 = sqrt6)": table(H, 4, 6, "4H"),
    }
    ctrl = {}
    Usm = Us.copy()
    Usm[0, 2] = sp.Rational(1, 3)
    ctrl["U_s with entry (0,2) 1/2 -> 1/3: unitary?"] = zero(Usm * Usm.H - I9)
    Hm = build_h(t=sp.Rational(1, 2))
    ctrl["H with t = 1/2: unitary?"] = zero(Hm * Hm.H - I9)
    Hm = build_h(r2_sign=+1)
    ctrl["H with R_2 = +tX: unitary and self-dual?"] = zero(Hm * Hm.H - I9) and zero(realign(Hm) - Hm)
    Hm = build_h(omega=sp.Rational(1, 2))
    ctrl["H with Omega_ad = +(1/2) delta I: unitary?"] = zero(Hm * Hm.H - I9)
    GG = ptrans(H)
    W = (GG * GG.H).applyfunc(sp.expand)
    ctrl["H: W == (3/4)(I - S)?"] = zero(W - sp.Rational(3, 4) * (I9 - S9))
    out["mutation controls (each must be False)"] = ctrl
    out["all_ok"] = bool(out["W1 U_s(2pi/3) = S*U(2pi/3)"]["all_ok"] and out["W2 H over Q(sqrt6) (Codex normal-form data)"]["all_ok"]
                         and out["W2 normal form: H[(00),(00)] == 1"] and out["W2 real entries in Q(sqrt6)"]
                         and not any(ctrl.values()))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "witnesses_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
