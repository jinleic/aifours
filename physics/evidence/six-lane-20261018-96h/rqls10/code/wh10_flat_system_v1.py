#!/usr/bin/env python3
"""wh10_flat_system_v1: EXACT stdlib check (fractions over Q(zeta_5); no floats) of the explicit flat-plane system for the
WH_10 line triple {L_inf, L_0, L_2} of Z_5^2 (lane note evidence/wh10-flat-planes-v1.md, written alongside).

Conventions: zeta = e^(2 pi i/5); X e_t = e_(t+1), Z e_t = zeta^t e_t; tau = zeta^3 (tau^2 = zeta); D_(a,c) = tau^(ac) X^a Z^c;
<(a,c),(a',c')> = a c' - c a'. Flat planes: P = (2/5) I + S, S = sum over the complementary lines L_k (k in {1, 3, 4})
of alpha_k(x) D_(x e_k), e_k = (1, k), alpha_k(-x) = conj(alpha_k(x)); P^2 = P <=> M := S^2 - S/5 - (6/25) I = 0.
Notation a_x = alpha_1(x), b_x = alpha_3(x), g_x = alpha_4(x); c(n) = tau^n + tau^-n.
Claimed components m_w = tr(D_w^* M)/5 (note, section 2):
 w = 0: sum |a|^2 + |b|^2 + |g|^2 (over x in Z_5^*) - 6/25
 w = (0, c): a_2c b_3c c(2c^2) + a_3c g_2c c(3c^2) + b_4c g_c c(4c^2)
 w = (a, 0): a_4a b_2a c(a^2) + a_3a g_3a c(2a^2) + b_4a g_2a c(3a^2)
 w = (a, 2a): a_3a b_3a c(3a^2) + a_4a g_2a c(4a^2) + b_2a g_4a c(3a^2)
 w = z e_1: sum_(x+y=z) a_x a_y + b_3z g_3z c(4z^2) - a_z/5
 w = z e_3: sum_(x+y=z) b_x b_y + a_2z g_4z c(4z^2) - b_z/5
 w = z e_4: sum_(x+y=z) g_x g_y + a_2z b_4z c(z^2) - g_z/5      (x, y in Z_5^*)
Checks: (1) D_u D_v = tau^(-<u,v>) D_(u+v), D_u^* = D_(-u) for all u, v; (2) the 25 claimed components equal the exact
components at 40 random Hermitian coefficient choices (integer coefficients in Q(zeta_5)); (3) c(1) = c(4) = -phi,
c(2) = c(3) = 1/phi with phi = 1 + zeta + zeta^4; the six displayed equations U1-U6 (multiplied by phi) of the note;
(4) positive controls: the 30 MUB-pair planes span(psi^k_m, psi^k_m'), k in {1, 3, 4}, psi^k_m(t) = zeta^(3kt^2+mt)/sqrt5:
P^2 = P, trace 2, normal form (no component on used lines, identity component 2/5), all 25 claimed components zero;
negative control: a perturbed MUB-pair coefficient set violates the system; (5) the one-vanishing-block lemma's ratio
sets R u (-R) = Z_5^* for every pair of complementary lines and every used line, for this triple and for the W8 triple
{inf, 0, 4}; (6) the same derivation for the W8 triple compared with the three equations printed in the W8 note
(evidence/w8-decision-v1.md, section 5) - reported, not gated. Output JSON (exclusive) argv[1]. Budget 250 s.
"""
import json, random, sys, time
from fractions import Fraction as Fr

T0 = time.monotonic()
OUT = sys.argv[1]
P5 = 5
ZERO = tuple(Fr(0) for _ in range(5))
ONE = (Fr(1),) + ZERO[1:]


def el(q=0):
    return (Fr(q),) + ZERO[1:]


def zp(e):
    v = [Fr(0)] * 5
    v[e % 5] = Fr(1)
    return tuple(v)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul(a, b):
    c = [Fr(0)] * 5
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    c[(i + j) % 5] += x * y
    return tuple(c)


def scal(q, a):
    return tuple(Fr(q) * x for x in a)


def conj(a):
    return tuple(a[(-k) % 5] for k in range(5))


def is_zero(a):
    return all(x == a[0] for x in a)


def eq(a, b):
    return is_zero(sub(a, b))


TAU = 3


def D(a, c):
    """5x5 monomial matrix: D[(t + a) % 5][t] = tau^(ac) zeta^(ct)."""
    M = [[ZERO] * 5 for _ in range(5)]
    for t in range(5):
        M[(t + a) % 5][t] = zp(TAU * a * c + c * t)
    return M


def mmul(A, B):
    C = [[ZERO] * 5 for _ in range(5)]
    for i in range(5):
        for k in range(5):
            if is_zero(A[i][k]) and A[i][k] == ZERO:
                continue
            for j in range(5):
                if B[k][j] != ZERO:
                    C[i][j] = add(C[i][j], mul(A[i][k], B[k][j]))
    return C


def madd(A, B):
    return [[add(A[i][j], B[i][j]) for j in range(5)] for i in range(5)]


def mscal(q, A):
    return [[scal(q, A[i][j]) for j in range(5)] for i in range(5)]


def mel(e, A):
    return [[mul(e, A[i][j]) for j in range(5)] for i in range(5)]


def dag(A):
    return [[conj(A[j][i]) for j in range(5)] for i in range(5)]


def meq(A, B):
    return all(eq(A[i][j], B[i][j]) for i in range(5) for j in range(5))


def ident():
    return [[ONE if i == j else ZERO for j in range(5)] for i in range(5)]


def symp(u, v):
    return (u[0] * v[1] - u[1] * v[0]) % 5


DM = {(a, c): D(a, c) for a in range(5) for c in range(5)}


def comp(M, w):
    """tr(D_w^* M) / 5."""
    Dw = DM[w]
    s = ZERO
    for i in range(5):
        for j in range(5):
            if Dw[j][i] != ZERO:
                s = add(s, mul(conj(Dw[j][i]), M[j][i]))
    return scal(Fr(1, 5), s)


# (1) multiplication law
law_ok = True
for u in DM:
    for v in DM:
        lhs = mmul(DM[u], DM[v])
        w = ((u[0] + v[0]) % 5, (u[1] + v[1]) % 5)
        rhs = mel(zp(-TAU * symp(u, v)), DM[w])
        if not meq(lhs, rhs):
            law_ok = False
    if not meq(dag(DM[u]), DM[((-u[0]) % 5, (-u[1]) % 5)]):
        law_ok = False


def cfun(n):
    return add(zp(TAU * n), zp(-TAU * n))


PHI = add(add(ONE, zp(1)), zp(4))
c_ok = eq(cfun(1), scal(-1, PHI)) and eq(cfun(4), scal(-1, PHI)) and eq(mul(cfun(2), PHI), ONE) and eq(mul(cfun(3), PHI), ONE)


def build_S(alpha, comp_lines):
    S = [[ZERO] * 5 for _ in range(5)]
    for k in comp_lines:
        for x in range(1, 5):
            S = madd(S, mel(alpha[k][x], DM[(x % 5, (k * x) % 5)]))
    return S


def M_of(S):
    return madd(madd(mmul(S, S), mscal(Fr(-1, 5), S)), mscal(Fr(-6, 25), ident()))


def claimed(alpha):
    a, b, g = alpha[1], alpha[3], alpha[4]
    out = {}
    nrm = ZERO
    for x in range(1, 5):
        nrm = add(nrm, add(add(mul(a[x], a[-x % 5]), mul(b[x], b[-x % 5])), mul(g[x], g[-x % 5])))
    out[(0, 0)] = sub(nrm, el(Fr(6, 25)))
    for c in range(1, 5):
        out[(0, c)] = add(add(mul(mul(a[2 * c % 5], b[3 * c % 5]), cfun(2 * c * c)), mul(mul(a[3 * c % 5], g[2 * c % 5]), cfun(3 * c * c))),
                          mul(mul(b[4 * c % 5], g[c % 5]), cfun(4 * c * c)))
    for s in range(1, 5):
        out[(s, 0)] = add(add(mul(mul(a[4 * s % 5], b[2 * s % 5]), cfun(s * s)), mul(mul(a[3 * s % 5], g[3 * s % 5]), cfun(2 * s * s))),
                          mul(mul(b[4 * s % 5], g[2 * s % 5]), cfun(3 * s * s)))
        out[(s, 2 * s % 5)] = add(add(mul(mul(a[3 * s % 5], b[3 * s % 5]), cfun(3 * s * s)), mul(mul(a[4 * s % 5], g[2 * s % 5]), cfun(4 * s * s))),
                                  mul(mul(b[2 * s % 5], g[4 * s % 5]), cfun(3 * s * s)))
    for z in range(1, 5):
        def selfsum(h):
            s_ = ZERO
            for x in range(1, 5):
                y = (z - x) % 5
                if y:
                    s_ = add(s_, mul(h[x], h[y]))
            return s_
        out[(z, z)] = sub(add(selfsum(a), mul(mul(b[3 * z % 5], g[3 * z % 5]), cfun(4 * z * z))), scal(Fr(1, 5), a[z]))
        out[(z, 3 * z % 5)] = sub(add(selfsum(b), mul(mul(a[2 * z % 5], g[4 * z % 5]), cfun(4 * z * z))), scal(Fr(1, 5), b[z]))
        out[(z, 4 * z % 5)] = sub(add(selfsum(g), mul(mul(a[2 * z % 5], b[4 * z % 5]), cfun(z * z))), scal(Fr(1, 5), g[z]))
    return out


def U_eqs(alpha):
    a, b, g = alpha[1], alpha[3], alpha[4]
    Phi = mul(PHI, PHI)
    return [sub(add(mul(a[2], b[3]), mul(a[3], g[2])), mul(Phi, mul(b[4], g[1]))),
            sub(add(mul(a[4], b[1]), mul(a[1], g[4])), mul(Phi, mul(b[3], g[2]))),
            add(add(scal(-1, mul(Phi, mul(a[4], b[2]))), mul(a[3], g[3])), mul(b[4], g[2])),
            add(add(scal(-1, mul(Phi, mul(a[3], b[4]))), mul(a[1], g[1])), mul(b[3], g[4])),
            add(sub(mul(a[3], b[3]), mul(Phi, mul(a[4], g[2]))), mul(b[2], g[4])),
            add(sub(mul(a[1], b[1]), mul(Phi, mul(a[3], g[4]))), mul(b[4], g[3]))]


U_TARGETS = [(0, 1), (0, 2), (1, 0), (2, 0), (1, 2), (2, 4)]


def rand_el(rng):
    return tuple(Fr(rng.randint(-3, 3), rng.choice([1, 2, 5])) for _ in range(5))


def rand_alpha(rng, lines):
    al = {}
    for k in lines:
        v = [None] * 5
        v[1], v[2] = rand_el(rng), rand_el(rng)
        v[4], v[3] = conj(v[1]), conj(v[2])
        al[k] = v
    return al


rng = random.Random(20261019)
LINES = (1, 3, 4)
rand_ok, rand_tests, u_ok = True, 0, True
for trial in range(40):
    if time.monotonic() - T0 > 200:
        break
    al = rand_alpha(rng, LINES)
    M = M_of(build_S(al, LINES))
    cl = claimed(al)
    rand_tests += 1
    for w in DM:
        if not eq(comp(M, w), cl[w]):
            rand_ok = False
    for Ue, w in zip(U_eqs(al), U_TARGETS):
        if not eq(Ue, mul(PHI, comp(M, w))):
            u_ok = False


def psi(k, m):
    return [zp(3 * k * t * t + m * t) for t in range(5)]          # times 1/sqrt5


mub_ok, mub_count, normal_form_ok = True, 0, True
mub_alphas = []
for k in LINES:
    for m1 in range(5):
        for m2 in range(m1 + 1, 5):
            P = [[scal(Fr(1, 5), add(mul(psi(k, m1)[i], conj(psi(k, m1)[j])), mul(psi(k, m2)[i], conj(psi(k, m2)[j]))))
                  for j in range(5)] for i in range(5)]
            ok = meq(mmul(P, P), P)
            tr = ZERO
            for i in range(5):
                tr = add(tr, P[i][i])
            ok = ok and eq(tr, el(2))
            al = {kk: [None] + [comp(P, (x % 5, (kk * x) % 5)) for x in range(1, 5)] for kk in LINES}
            used = [(0, c) for c in range(1, 5)] + [(s, 0) for s in range(1, 5)] + [(s, 2 * s % 5) for s in range(1, 5)]
            nf = eq(comp(P, (0, 0)), el(Fr(2, 5))) and all(is_zero(comp(P, w)) for w in used)
            normal_form_ok = normal_form_ok and nf
            cl = claimed(al)
            ok = ok and all(is_zero(v) for v in cl.values())
            mub_ok = mub_ok and ok
            mub_count += 1
            mub_alphas.append(al)
pert = {kk: list(v) for kk, v in mub_alphas[0].items()}
pert[3][1] = add(pert[3][1], el(Fr(1, 10)))
pert[3][4] = conj(pert[3][1])
neg_violates = not all(is_zero(v) for v in claimed(pert).values())


def ratio_sets(used_slopes, comp_lines):
    res, all_ok = [], True
    inv = {1: 1, 2: 3, 3: 2, 4: 4}
    for ii in range(len(comp_lines)):
        for jj in range(ii + 1, len(comp_lines)):
            i, j = comp_lines[ii], comp_lines[jj]
            R = set()
            for s in used_slopes:
                for x in range(1, 5):
                    for y in range(1, 5):
                        w = ((x + y) % 5, (x * i + y * j) % 5)
                        on = (w[0] == 0 and w[1] != 0) if s == "inf" else (w[0] != 0 and w[1] == (s * w[0]) % 5)
                        if on:
                            R.add((y * inv[x]) % 5)
            Rm = {(-r) % 5 for r in R}
            res.append({"pair": [i, j], "R": sorted(R), "R_union_minus_R": sorted(R | Rm)})
            all_ok = all_ok and (R | Rm) == {1, 2, 3, 4}
    return res, all_ok


rs_wh10, rs_wh10_ok = ratio_sets(["inf", 0, 2], [1, 3, 4])
rs_w8, rs_w8_ok = ratio_sets(["inf", 0, 4], [1, 2, 3])

# (6) W8 triple: compare with the note's printed equations (multiplied by phi), searching the matching w on each line
W8L = (1, 2, 3)


def w8_printed(al, s):
    a, b, g = al[1], al[2], al[3]
    Phi = mul(PHI, PHI)
    EZ = add(add(scal(-1, mul(Phi, mul(a[-s % 5], b[s % 5]))), mul(a[2 * s % 5], g[3 * s % 5])), scal(-1, mul(Phi, mul(b[-s % 5], g[s % 5]))))
    EX = add(add(mul(a[2 * s % 5], b[4 * s % 5]), scal(-1, mul(Phi, mul(a[4 * s % 5], g[2 * s % 5])))), scal(-1, mul(Phi, mul(b[3 * s % 5], g[3 * s % 5]))))
    ET = add(add(scal(-1, mul(Phi, mul(a[3 * s % 5], b[3 * s % 5]))), scal(-1, mul(Phi, mul(a[2 * s % 5], g[4 * s % 5])))), mul(b[4 * s % 5], g[2 * s % 5]))
    return {"Z": EZ, "X": EX, "T": ET}


w8_lines = {"Z": [(0, c) for c in range(1, 5)], "X": [(c, 0) for c in range(1, 5)], "T": [(c, 4 * c % 5) for c in range(1, 5)]}
w8_match = {}
al1 = rand_alpha(random.Random(7), W8L)
al2 = rand_alpha(random.Random(8), W8L)
M1, M2 = M_of(build_S(al1, W8L)), M_of(build_S(al2, W8L))
for name in ("Z", "X", "T"):
    for s in range(1, 5):
        hits = []
        for w in w8_lines[name]:
            for sign in (1, -1):
                if eq(w8_printed(al1, s)[name], scal(sign, mul(PHI, comp(M1, w)))) and \
                        eq(w8_printed(al2, s)[name], scal(sign, mul(PHI, comp(M2, w)))):
                    hits.append([list(w), sign])
        w8_match["%s(s=%d)" % (name, s)] = hits

out = {"probe": "wh10_flat_system_v1", "arithmetic": "Q(zeta_5) with Fraction coefficients (exact)",
       "multiplication_law_and_adjoint_ok": law_ok, "c_values_ok": c_ok,
       "random_tests": rand_tests, "claimed_components_equal_exact_components": rand_ok, "U1_U6_equal_phi_times_components": u_ok,
       "mub_pair_planes": mub_count, "mub_pair_planes_projector_trace2_and_system_zero": mub_ok,
       "mub_pair_planes_normal_form": normal_form_ok, "negative_control_perturbed_violates": neg_violates,
       "ratio_sets_wh10": rs_wh10, "ratio_sets_wh10_all_cover": rs_wh10_ok,
       "ratio_sets_w8": rs_w8, "ratio_sets_w8_all_cover": rs_w8_ok,
       "w8_note_equations_matching_components": w8_match,
       "w8_note_equations_all_matched": all(len(v) > 0 for v in w8_match.values()),
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: v for k, v in out.items() if k not in ("ratio_sets_wh10", "ratio_sets_w8", "w8_note_equations_matching_components")}))
print(json.dumps(out["w8_note_equations_matching_components"]))
