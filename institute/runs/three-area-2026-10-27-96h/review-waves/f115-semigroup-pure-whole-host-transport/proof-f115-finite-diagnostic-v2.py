#!/usr/bin/env python3
"""proof-f115-finite-diagnostic-v2.py -- REVIEWER-WRITTEN independent exact finite
diagnostic for review f115 (pure whole-host transport).  It shares no code, group,
band, sandwich or gauge data with the author scripts; author scripts were read but
never imported or executed.

v2 history: v1 used B = left-zero(3) x semilattice(2); left multiplication discards the
acted coordinate, so b*alpha_w(c) did not depend on w and the section-5 negative controls
were vacuous (v1 exit 1 at its own control assertion; see the v1 run record).  v2 uses a
RIGHT-zero factor and asserts non-vacuity explicitly.  Nothing else changed.

Reviewer example (chosen to differ from the author's S3/C2/5-element band):
  G0 = C3 (additive), G1 = A4, H = phi(C3) a NONNORMAL order-3 subgroup of A4,
  B  = right-zero(3) x semilattice(2): a 6-element locally regular band that is
       NOT rectangular, has NO identity, and carries a C3-action with NO fixed point,
  D0 = M[C3;3,3;P0], D1 = M[A4;2,2;P1], row map 3->2 and column map 3->2 both
       collapse, f: D0 -> D1 pure, not onto, not injective.
What is checked (every assert is a complete finite enumeration, no sampling):
  1  f is a homomorphism, pure, nononto; D0, D1 associative.
  2  f restricted to EVERY local group of D0 is injective and (for this f) NOT onto.
  3  Rees homomorphism gauges are DERIVED from f as a black box by the
     normalize-at-(i0,l0) / read X_i,Y_l,K_g / h(g)=K_g p* / undo-gauge recipe of
     the frozen text, then (RH) and (RH-P) are verified in ORIGINAL coordinates;
     control: skipping the un-gauge step breaks (RH).
     Also: base local group map equals x -> u_i0 h(x) u_i0^-1 in group parameters.
  4  Coinduction with LEFT cosets rH (1 in R) and RIGHT shifts (gamma_g F)(x)=F(xg):
     C = B^G1 pointwise band, gamma is a left action by automorphisms, J is an
     injective band homomorphism and H-equivariant.
     controls: left-shift convention fails; right-coset convention fails.
  5  Whole-host Psi: P(B,D0) -> P((I0xL0) x B^G1, D1) is a homomorphism on all
     |P(B,D0)|^2 pairs and injective.  controls: dropping the rectangle collides;
     dropping the u_i gauge breaks the homomorphism; wrong shift convention breaks it.
  6  Onto specialisation f2: D0 -> D2 = M[C3;2,2;P2] (pure, onto, collapsing), gauges
     derived again, Psi2 into P((I0xL0) x B, D2) with the SAME B is a homomorphism
     and injective; the one-coset orbit subband J2(B) is gamma-invariant.
  7  tau = syntactic congruence of E with S^1 contexts.  For S = P(B,D0) (regular,
     actor projection onto and pure): tau_S = pi^-1(tau_D0); tau_D0 saturates E;
     D0 -> D0/tau_D0 is pure; D0/tau_D0 is simple and completely regular (CS);
     ker f2 == tau_D0, so Psi2 is a same-B host over the ACTUAL tau quotient.
     controls: nonpure onto C4 -> C2 violates (3); pure NONONTO inclusion of one
     row of D0 violates the forward direction of (3).
Exit code 0 means every assertion passed; counts for controls are printed.
"""
import sys, time
from itertools import product, permutations

T0 = time.time()
def log(*a):
    print(*a, flush=True)

# ---------------------------------------------------------------- groups
def pmul(a, b):
    return tuple(a[b[x]] for x in range(len(a)))
def pinv(a):
    r = [0] * len(a)
    for x, y in enumerate(a):
        r[y] = x
    return tuple(r)
def parity(p):
    return sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j]) % 2

A4 = tuple(sorted(p for p in permutations(range(4)) if parity(p) == 0))
ONE4 = (0, 1, 2, 3)
assert len(A4) == 12 and A4[0] == ONE4
assert all(pmul(a, b) in A4 for a in A4 for b in A4)
IDX = {x: n for n, x in enumerate(A4)}
c3 = (1, 2, 0, 3)
phi = {0: ONE4, 1: c3, 2: pmul(c3, c3)}
assert pmul(phi[2], c3) == ONE4
Hset = frozenset(phi.values())
assert all(pmul(phi[a], phi[b]) == phi[(a + b) % 3] for a in range(3) for b in range(3))
assert any(pmul(pmul(g, hh), pinv(g)) not in Hset for g in A4 for hh in Hset)  # H nonnormal
def c3mul(a, b):
    return (a + b) % 3
def c3inv(a):
    return (-a) % 3

# ---------------------------------------------------------------- band B with action
B = tuple(product(range(3), range(2)))  # right-zero(3) x semilattice(2)
def bmul(x, y):
    return (y[0], x[1] if x[1] < y[1] else y[1])
def alpha(k, x):
    return ((x[0] + k) % 3, x[1])
assert all(bmul(x, x) == x for x in B)
assert all(bmul(bmul(x, y), z) == bmul(x, bmul(y, z)) for x in B for y in B for z in B)
assert all(alpha(0, x) == x and alpha(a, alpha(b, x)) == alpha((a + b) % 3, x)
           for a in range(3) for b in range(3) for x in B)
assert all(alpha(k, bmul(x, y)) == bmul(alpha(k, x), alpha(k, y)) for k in range(3) for x in B for y in B)
assert not any(all(bmul(e, x) == x == bmul(x, e) for x in B) for e in B)      # no identity
assert not any(alpha(k, x) == x for k in (1, 2) for x in B)                    # no fixed point
assert any(bmul(bmul(x, y), x) != x for x in B for y in B)                      # not rectangular
assert any(bmul(b, alpha(1, c)) != bmul(b, alpha(0, c)) for b in B for c in B)  # weight is NOT invisible (v1 defect guard)
def exe(e, x):
    return bmul(bmul(e, x), e)
assert all(bmul(bmul(bmul(bmul(exe(e, x), exe(e, y)), exe(e, x)), exe(e, z)), exe(e, x))
           == bmul(bmul(bmul(exe(e, x), exe(e, y)), exe(e, z)), exe(e, x))
           for e in B for x in B for y in B for z in B)                         # locally regular
log("band B: size", len(B), "no identity, fixed-point-free C3 action, not rectangular, locally regular, weight-sensitive")

# ---------------------------------------------------------------- Rees matrix semigroups
def rees(P, gmul):
    def mul(x, y):
        return (x[0], gmul(gmul(x[1], P[x[2]][y[0]]), y[1]), y[2])
    return mul
def idem(mul, x):
    return mul(x, x) == x

# ---------------------------------------------------------------- 1. pure nononto f: D0 -> D1
rho = (0, 0, 1)
sig = (0, 1, 1)
dI = (ONE4, (1, 0, 3, 2))
cL = (ONE4, (2, 3, 0, 1))
assert dI[1] in A4 and cL[1] in A4 and dI[1] not in Hset and cL[1] not in Hset
kJ = (phi[0], phi[1], phi[2])
hL = (phi[0], phi[2], phi[1])
hLI = ((phi[0], phi[1]), (phi[1], phi[0]))
u_c = tuple(pmul(dI[rho[j]], kJ[j]) for j in range(3))   # construction gauges: NOT used by Psi
v_c = tuple(pmul(hL[l], cL[sig[l]]) for l in range(3))
P1 = [[pmul(pmul(pinv(cL[l]), hLI[l][i]), pinv(dI[i])) for i in range(2)] for l in range(2)]
phinv = {w: k for k, w in phi.items()}
P0 = [[phinv[pmul(pmul(hL[l], hLI[sig[l]][rho[j]]), kJ[j])] for j in range(3)] for l in range(3)]
D0 = tuple(product(range(3), range(3), range(3)))
m0 = rees(P0, c3mul)
D1 = tuple(product(range(2), A4, range(2)))
m1 = rees(P1, pmul)
assert all(m0(m0(x, y), z) == m0(x, m0(y, z)) for x in D0 for y in D0 for z in D0)
assert all(m1(m1(x, y), z) == m1(x, m1(y, z)) for x in D1 for y in D1 for z in D1)
def f(x):
    return (rho[x[0]], pmul(pmul(u_c[x[0]], phi[x[1]]), v_c[x[2]]), sig[x[2]])
assert all(f(m0(x, y)) == m1(f(x), f(y)) for x in D0 for y in D0)
assert all(idem(m0, x) == idem(m1, f(x)) for x in D0)          # pure (and E preserved)
img = {f(x) for x in D0}
assert 0 < len(img) < len(D0) and len(img) < len(D1)
log("1 PASS f: D0(27) -> D1(48) homomorphism, pure, image", len(img), "(nononto, noninjective); P0 =", P0)

# ---------------------------------------------------------------- 2. local groups
def local_group(elems, mul, e):
    return sorted({mul(mul(e, x), e) for x in elems})
E0 = [x for x in D0 if idem(m0, x)]
nonsurj = 0
for e in E0:
    L0g = local_group(D0, m0, e)
    L1g = local_group(D1, m1, f(e))
    imgs = {f(x) for x in L0g}
    assert len(imgs) == len(L0g) and imgs <= set(L1g)
    nonsurj += len(imgs) < len(L1g)
assert nonsurj == len(E0) == 9
log("2 PASS local-group injectivity at all", len(E0), "idempotents; local maps NOT onto for nononto f:", nonsurj)
# control: nonpure CS homomorphism C4 -> C2 is not injective on the local group
C4 = tuple(range(4)); C2 = tuple(range(2))
r4 = lambda k: k % 2
assert all(r4((a + b) % 4) == (r4(a) + r4(b)) % 2 for a in C4 for b in C4)
assert r4(2) == 0 and (2 + 2) % 4 != 2                        # not pure
assert len({r4(k) for k in C4}) < 4                           # not injective on the (only) local group
log("2 CONTROL nonpure C4->C2: local group map not injective (purity hypothesis necessary)")

# ---------------------------------------------------------------- 3. gauges derived from f as a black box
def derive_gauges(D0, m0, P0, G0, g0mul, g0inv, g0one, fmap, P1, g1mul, g1inv, g1one, I0, L0, i0=0, l0=0):
    rho_, sig_ = {}, {}
    for (i, g, l) in D0:
        y = fmap((i, g, l))
        assert rho_.setdefault(i, y[0]) == y[0]
        assert sig_.setdefault(l, y[2]) == y[2]
    A = {i: P0[l0][i] for i in I0}
    Bg = {l: g0mul(P0[l][i0], g0inv(P0[l0][i0])) for l in L0}
    Pn = {(l, i): g0mul(g0mul(g0inv(Bg[l]), P0[l][i]), g0inv(A[i])) for l in L0 for i in I0}
    assert all(Pn[(l0, i)] == g0one for i in I0) and all(Pn[(l, i0)] == g0one for l in L0)
    def orig(i, gp, l):                     # normalized (i,g',l) -> original coordinates
        return (i, g0mul(g0mul(g0inv(A[i]), gp), g0inv(Bg[l])), l)
    # the gauge is an isomorphism: check B_l * Pn(l,i) * A_i == P0(l,i)
    assert all(g0mul(g0mul(Bg[l], Pn[(l, i)]), A[i]) == P0[l][i] for l in L0 for i in I0)
    # E_i T_g F_l == (i,g,l) in normalized coordinates
    def mn(x, y):
        return (x[0], g0mul(g0mul(x[1], Pn[(x[2], y[0])]), y[1]), y[2])
    assert all(mn(mn((i, g0one, l0), (i0, g, l0)), (i0, g0one, l)) == (i, g, l) for i in I0 for g in G0 for l in L0)
    X = {i: fmap(orig(i, g0one, l0))[1] for i in I0}
    Y = {l: fmap(orig(i0, g0one, l))[1] for l in L0}
    K = {g: fmap(orig(i0, g, l0))[1] for g in G0}
    pstar = P1[sig_[l0]][rho_[i0]]
    h = {g: g1mul(K[g], pstar) for g in G0}
    assert all(h[g0mul(a, b)] == g1mul(h[a], h[b]) for a in G0 for b in G0)
    assert h[g0one] == g1one and len(set(h.values())) == len(G0)
    up = {i: g1mul(X[i], pstar) for i in I0}
    vp = {l: Y[l] for l in L0}
    uu = {i: g1mul(up[i], h[A[i]]) for i in I0}
    vv = {l: g1mul(h[Bg[l]], vp[l]) for l in L0}
    return rho_, sig_, h, uu, vv, up, vp, A, Bg

def check_RH(D0, P0, fmap, P1, g1mul, rho_, sig_, h, uu, vv, I0, L0):
    bad_rh = sum(fmap((i, g, l)) != (rho_[i], g1mul(g1mul(uu[i], h[g]), vv[l]), sig_[l]) for (i, g, l) in D0)
    bad_rhp = sum(g1mul(g1mul(vv[l], P1[sig_[l]][rho_[j]]), uu[j]) != h[P0[l][j]] for l in L0 for j in I0)
    return bad_rh, bad_rhp

G0 = tuple(range(3)); I0 = tuple(range(3)); L0 = tuple(range(3))
rho_, sig_, h, uu, vv, up, vp, Agauge, Bgauge = derive_gauges(D0, m0, P0, G0, c3mul, c3inv, 0, f, P1, pmul, pinv, ONE4, I0, L0)
assert dict(enumerate(rho)) == rho_ and dict(enumerate(sig)) == sig_
assert any(a != 0 for a in Agauge.values()) or any(b != 0 for b in Bgauge.values())  # P0 not already normalized
bad_rh, bad_rhp = check_RH(D0, P0, f, P1, pmul, rho_, sig_, h, uu, vv, I0, L0)
assert bad_rh == 0 and bad_rhp == 0
ctrl_rh, ctrl_rhp = check_RH(D0, P0, f, P1, pmul, rho_, sig_, h, up, vp, I0, L0)   # forgot to undo gauge
assert ctrl_rh > 0
# base local group: (i0, x p0^-1, l0) -> parameter u_i0 h(x) u_i0^-1 where target param z means (.., z p1^-1, ..)
p0 = P0[0][0]; p1 = P1[sig_[0]][rho_[0]]
for x in G0:
    z = pmul(f((0, c3mul(x, c3inv(p0)), 0))[1], p1)
    assert z == pmul(pmul(uu[0], h[x]), pinv(uu[0]))
log("3 PASS derived gauges: (RH) violations", bad_rh, "(RH-P) violations", bad_rhp, "; h injective, |h(G0)|=", len(set(h.values())),
    "; A_i =", Agauge, "B_l =", Bgauge, "; local map = conjugate of h")
log("3 CONTROL un-gauge omitted: (RH) violations", ctrl_rh, "(RH-P) violations", ctrl_rhp)

# ---------------------------------------------------------------- 4. coinduction (left cosets, right shifts)
Hd = frozenset(h.values())                          # derived subgroup image
hinv = {val: g for g, val in h.items()}
R, decomp = [], {}
for x in A4:                                        # A4 sorted, identity first
    if x in decomp:
        continue
    R.append(x)
    for hh in sorted(Hd):
        y = pmul(x, hh)
        assert y not in decomp
        decomp[y] = (x, hh)
assert R[0] == ONE4 and len(decomp) == 12 and len(R) == 4
RIGHT = {g: tuple(IDX[pmul(x, g)] for x in A4) for g in A4}          # (gamma_g F)(x) = F(x g)
LEFT = {g: tuple(IDX[pmul(pinv(g), x)] for x in A4) for g in A4}     # wrong convention F(g^-1 x)
def gam(g, F):
    return tuple(F[n] for n in RIGHT[g])
def gamL(g, F):
    return tuple(F[n] for n in LEFT[g])
def cmul(F, G_):
    return tuple(bmul(a, b) for a, b in zip(F, G_))
def J(b):
    return tuple(alpha(hinv[decomp[x][1]], b) for x in A4)
# gamma is a left action: RIGHT[gk][n] == RIGHT[k][RIGHT[g][n]] for all g,k,n  (so gamma_g gamma_k = gamma_gk on every F)
assert all(RIGHT[pmul(g, k)][n] == RIGHT[k][RIGHT[g][n]] for g in A4 for k in A4 for n in range(12))
assert all(RIGHT[ONE4][n] == n for n in range(12))
assert all(J(bmul(a, b)) == cmul(J(a), J(b)) for a in B for b in B)       # J band hom
assert len({J(b) for b in B}) == len(B)                                    # J injective
assert all(J(b)[0] == b for b in B)                                        # evaluation at 1 recovers b
assert all(gam(h[g], J(b)) == J(alpha(g, b)) for g in G0 for b in B)       # equivariance
# controls
wrong_left = sum(gamL(h[g], J(b)) != J(alpha(g, b)) for g in G0 for b in B)
decompR = {}
for x in A4:
    if x in decompR:
        continue
    for hh in sorted(Hd):
        y = pmul(hh, x)
        assert y not in decompR
        decompR[y] = (hh, x)
def JR(b):
    return tuple(alpha(hinv[decompR[x][0]], b) for x in A4)
wrong_rcoset = sum(gam(h[g], JR(b)) != JR(alpha(g, b)) for g in G0 for b in B)
assert wrong_left > 0 and wrong_rcoset > 0
log("4 PASS coinduction: |R| =", len(R), "left cosets, J hom+injective+H-equivariant, right shift is a left action")
log("4 CONTROL left-shift convention failures", wrong_left, "of", 3 * len(B), "; right-coset convention failures", wrong_rcoset, "of", 3 * len(B))

# ---------------------------------------------------------------- 5. whole host Psi
S = tuple(product(B, D0))
def smul(x, y):
    b, d = x
    cb, e = y
    w = c3mul(d[1], P0[d[2]][e[0]])
    return (bmul(b, alpha(w, cb)), m0(d, e))
assert all(smul(smul(x, y), z) == smul(x, smul(y, z)) for x in S for y in S for z in S)   # 162^3 triples
assert all(any(smul(smul(x, y), x) == x for y in S) for x in S)                            # regular
ES = {x for x in S if smul(x, x) == x}
assert ES == {(b, d) for b in B for d in E0}                                                # E(P(B,D0)) = B x E(D0)
def tmul(x, y):
    (r1, F1), d = x
    (r2, F2), e = y
    w = pmul(d[1], P1[d[2]][e[0]])
    return (((r1[0], r2[1]), cmul(F1, gam(w, F2))), m1(d, e))
def Psi(x):
    b, (i, g, l) = x
    return (((i, l), gam(uu[i], J(b))), f((i, g, l)))
PS = {x: Psi(x) for x in S}
bad_hom = sum(PS[smul(x, y)] != tmul(PS[x], PS[y]) for x in S for y in S)
assert bad_hom == 0
assert len(set(PS.values())) == len(S)
# controls
norect = len({(PS[x][0][1], PS[x][1]) for x in S})
assert norect < len(S)
def PsiNG(x):
    b, (i, g, l) = x
    return (((i, l), J(b)), f((i, g, l)))
PNG = {x: PsiNG(x) for x in S}
bad_nogauge = sum(PNG[smul(x, y)] != tmul(PNG[x], PNG[y]) for x in S for y in S)
def tmulL(x, y):
    (r1, F1), d = x
    (r2, F2), e = y
    w = pmul(d[1], P1[d[2]][e[0]])
    return (((r1[0], r2[1]), cmul(F1, gamL(w, F2))), m1(d, e))
def PsiL(x):
    b, (i, g, l) = x
    return (((i, l), gamL(uu[i], J(b))), f((i, g, l)))
PL = {x: PsiL(x) for x in S}
bad_leftshift = sum(PL[smul(x, y)] != tmulL(PL[x], PL[y]) for x in S for y in S)
assert bad_nogauge > 0 and bad_leftshift > 0
log("5 PASS whole host |P(B,D0)| =", len(S), ": associative, regular, E = B x E(D0); Psi homomorphism on", len(S) ** 2,
    "pairs with", bad_hom, "violations; Psi injective")
log("5 CONTROL no rectangle: distinct images", norect, "of", len(S), "; no u_i gauge: hom violations", bad_nogauge,
    "; left-shift convention: hom violations", bad_leftshift)

# ---------------------------------------------------------------- 6. onto specialisation with the same B
u2 = (0, 2, 1); v2 = (2, 0, 1)
def phi2(k):
    return (-k) % 3
P2 = [[None] * 2 for _ in range(2)]
for l in range(3):
    for j in range(3):
        val = c3mul(c3mul(phi2(P0[l][j]), c3inv(v2[l])), c3inv(u2[j]))
        if P2[sig[l]][rho[j]] is None:
            P2[sig[l]][rho[j]] = val
D2 = tuple(product(range(2), range(3), range(2)))
m2 = rees(P2, c3mul)
def f2(x):
    return (rho[x[0]], c3mul(c3mul(u2[x[0]], phi2(x[1])), v2[x[2]]), sig[x[2]])
assert all(f2(m0(x, y)) == m2(f2(x), f2(y)) for x in D0 for y in D0)
assert all(idem(m0, x) == idem(m2, f2(x)) for x in D0)
assert {f2(x) for x in D0} == set(D2)
rho2, sig2, h2, uu2, vv2, up2, vp2, A2, B2 = derive_gauges(D0, m0, P0, G0, c3mul, c3inv, 0, f2, P2, c3mul, c3inv, 0, I0, L0)
b_rh2, b_rhp2 = check_RH(D0, P0, f2, P2, c3mul, rho2, sig2, h2, uu2, vv2, I0, L0)
assert b_rh2 == 0 and b_rhp2 == 0 and set(h2.values()) == set(G0)
for e in E0:                                                   # local maps now onto
    assert {f2(x) for x in local_group(D0, m0, e)} == set(local_group(D2, m2, f2(e)))
h2inv = {val: g for g, val in h2.items()}
def gam2(z, b):
    return alpha(h2inv[z], b)
def tmul2(x, y):
    (r1, b1), d = x
    (r2, b2), e = y
    w = c3mul(d[1], P2[d[2]][e[0]])
    return (((r1[0], r2[1]), bmul(b1, gam2(w, b2))), m2(d, e))
def Psi2(x):
    b, (i, g, l) = x
    return (((i, l), gam2(uu2[i], b)), f2((i, g, l)))
P2S = {x: Psi2(x) for x in S}
bad_hom2 = sum(P2S[smul(x, y)] != tmul2(P2S[x], P2S[y]) for x in S for y in S)
assert bad_hom2 == 0 and len(set(P2S.values())) == len(S)
# one-coset coinduction J2 into B^{C3}: orbit subband gamma-invariant and isomorphic to B
def J2(b):
    return tuple(alpha(h2inv[z], b) for z in G0)
def gam2C(g, F):
    return tuple(F[c3mul(z, g)] for z in G0)
J2B = {J2(b) for b in B}
assert len(J2B) == len(B) and all(gam2C(z, F) in J2B for z in G0 for F in J2B)
assert all(J2(bmul(a, b)) == tuple(bmul(p, q) for p, q in zip(J2(a), J2(b))) for a in B for b in B)
assert all(gam2C(h2[g], J2(b)) == J2(alpha(g, b)) for g in G0 for b in B)
log("6 PASS onto f2: D0 -> D2(12), pure, local maps onto, derived h2 bijective, (RH)/(RH-P) violations", b_rh2, b_rhp2,
    "; Psi2 into P((I0xL0) x B, D2) homomorphism violations", bad_hom2, "and injective; J2(B) gamma-invariant; P2 =", P2)

# ---------------------------------------------------------------- 7. tau = syntactic congruence of E
def tau_ids(elems, mul):
    E = {x for x in elems if mul(x, x) == x}
    E1 = list(elems) + [None]
    cls, cid = {}, {}
    for s in elems:
        prof = []
        for x in E1:
            xs = s if x is None else mul(x, s)
            for y in E1:
                t = xs if y is None else mul(xs, y)
                if t in E:
                    prof.append((x, y))
        cid[s] = cls.setdefault(frozenset(prof), len(cls))
    return cid, len(cls)
pi = lambda x: x[1]
cidS, nS = tau_ids(S, smul)
cid0, n0 = tau_ids(D0, m0)
assert nS == n0
assert all((cidS[s] == cidS[t]) == (cid0[pi(s)] == cid0[pi(t)]) for s in S for t in S)           # (3)
assert all(cid0[x] != cid0[y] for x in E0 for y in D0 if not idem(m0, y))                        # saturation
assert all((cid0[m0(x, x)] == cid0[x]) == idem(m0, x) for x in D0)                               # quotient map pure
# quotient table, simplicity and complete regularity
rep = {}
for x in D0:
    rep.setdefault(cid0[x], x)
Q = sorted(rep)
qm = {(a, b): cid0[m0(rep[a], rep[b])] for a in Q for b in Q}
assert all(qm[(a, b)] == cid0[m0(x, y)] for x in D0 for y in D0 for a in [cid0[x]] for b in [cid0[y]])  # well defined
assert all(any(qm[(qm[(x, a)], y)] == b for x in Q for y in Q) for a in Q for b in Q)           # simple: b in QaQ
sq = {a: qm[(a, a)] for a in Q}
assert all(any(qm[(sq[a], x)] == a for x in Q) and any(qm[(x, sq[a])] == a for x in Q) for a in Q)  # a in a^2 Q and Q a^2
ker_eq_tau = all((f2(x) == f2(y)) == (cid0[x] == cid0[y]) for x in D0 for y in D0)
assert ker_eq_tau
log("7 PASS tau: |D0/tau| =", n0, "|S/tau_S| =", nS, "; tau_S = pi^-1(tau_D0) on all", len(S) ** 2,
    "pairs; tau saturates E; quotient map pure; quotient simple + completely regular; ker f2 == tau_D0:", ker_eq_tau)
# control A: nonpure onto C4 -> C2 violates (3)
cid4, n4 = tau_ids(C4, lambda a, b: (a + b) % 4)
cid2, n2 = tau_ids(C2, lambda a, b: (a + b) % 2)
viol_nonpure = sum((cid4[s] == cid4[t]) != (cid2[r4(s)] == cid2[r4(t)]) for s in C4 for t in C4)
assert n4 == 4 and n2 == 2 and viol_nonpure > 0
# control B: pure NONONTO inclusion of row 0 of D0 violates the forward direction of (3)
Srow = tuple(x for x in D0 if x[0] == 0)
cidR, nR = tau_ids(Srow, m0)
viol_nononto = sum(cidR[s] == cidR[t] and cid0[s] != cid0[t] for s in Srow for t in Srow)
assert all(m0(x, y) in Srow for x in Srow for y in Srow) and viol_nononto > 0   # row is a subsemigroup; inclusion is trivially pure
log("7 CONTROL nonpure onto C4->C2: (3) violations", viol_nonpure, "of 16; pure nononto row inclusion (9 elements):",
    "tau_row classes", nR, "vs restricted tau_D0 classes", len({cid0[x] for x in Srow}), "; forward (3) violations", viol_nononto)

log("ALL ASSERTIONS PASSED in %.1fs; python %s" % (time.time() - T0, sys.version.split()[0]))
log("LIMIT: one reviewer-written finite instance (A4/C3, 6-element band, 27->48 and 27->12 actors);"
    " the all-variable theorem is the written argument in proof-review-v1.md, not this run.")
