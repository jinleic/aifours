# No seven-state PH representation for any ratio z >= 83/100 = 0.83

**NEW ALL-TOPOLOGY THEOREM CANDIDATE (strengthens the adopted z>=17/20 result).** Written proof; exact SymPy identities for symbolic z; exact integer Bernstein certificates at the single ratio z3=83/100; an independently implemented standard-library replay. Not independently reviewed. MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 08:21:51 PDT 2026**. Conventions and wording follow the additive MINOR-fix file `frontier-20261029-ph7-f159-f160-minor-fixes-addendum-v1.md` (SHA256 `a447c10752b9c876b8eaa9754ce5246bda11e40778f26bf98fa5c4fd345ac4d1`): rates are POSITIVE, `𝒜:=-S` is the matrix, the letter A is the scalar `f2-4f1+10-2z`, "threshold" means the supremum of PH7-realizable ratios.

## 1. Statement

For c,d>0, a=c+d, z=b²/d², `H(s)=c(a²+b²)²/[(s+c)((s+a)²+b²)²]`.

**Theorem.** If `z>=83/100`, H has no phase-type representation with at most seven states (every topology, every c,d>0), conditional only on the adopted irreducibility caller.

Hence the supremum of PH7-realizable ratios is at most 0.83. With the adopted v2 band (realizable on [7/9,41/50]) it lies in **[41/50, 83/100]**; with the unreviewed-by-disposition v4 endpoint it would lie in [z_*, 0.83] with z_*≈0.8204204.

## 2. Reduction

Exactly as in the adopted 0.85 packet: the caller gives an irreducible 7x7 Metzler G with `s(G)=0`, `det(yI-G)=y[(y+1)²+z]²(y²+py+q)`, p,q>0; Lemma S (adopted) moves G to the ratio exactly z3; Lemmas 1-4 (symmetrization, cover identity, coefficient extraction, Ky Fan) and Lemma 5 (the y² inequality `Y2b>=0`) apply with eigenvalues `v1<=...<=v7` of 𝒜, all positive. Below, x=v7 and `f_k` are the elementary sums of `v1..v6`; `A, B, h0, h1, D=h1-A*S4, E=h0-B*S4, Qpol, Hpol` are as in the core, `W3=E4`, `K=E3-W3*S4=E+xD`.

## 3. New: the y¹ inequality

**Lemma 6.** With `E1:=e6(v)-(1+z)²q`, `E2:=e5(v)-[(1+z)²p+(4+4z)q]`,

    alpha = e3(v1..v4) - (v1+v2) e2(v4,v5,v6,v7),
    beta  = e2(v1,v2,v3) - (v1+v2)(v5+v6+v7)   (<0),
    Y1+   = E1 - (v1+v2) E2 - W3*alpha - K*beta + W3²/2,

every realization satisfies `Y1+ >= 0`.

*Proof.* The target's y¹ coefficient is `(1+z)²q` (identity checked). In the cover identity the y¹ coefficient receives, besides `e6(v)`: from single extra cycles of length 3,4,5,6 the terms `-omega_C e3(𝒜_U)`, `-omega_C e2(𝒜_U)`, `-omega_C tr(𝒜_U)`, `-omega_C` (U the complementary states, |U|=4,3,2,1); from pairs of disjoint 3-cycles `+omega omega'` (one state left, y-coefficient 1); nothing else (pairs cover at least six states; three disjoint extra cycles need nine). Hence

    E1 = a3 + b2 + c1 + W6 - P33,  a3=sum_{|C|=3} omega e3(𝒜_U), b2=sum_{|C|=4} omega e2(𝒜_U), c1=sum_{|C|=5} omega tr(𝒜_U),

`W6>=0`, and `0<=P33<=W3²/2` (sum over unordered pairs of distinct cycles). Cauchy interlacing (`v_k<=mu_k<=v_{k+7-|U|}`) gives `a3>=W3 e3(v1..v4)`, `b2>=W4 e2(v1,v2,v3)`, `c1>=W5(v1+v2)`. From the y² relation of Lemma 5, `E2=a2+b1+W5` with `a2<=W3 e2(v4..v7)` and `b1<=W4(v5+v6+v7)`, so `W5>=E2-W3 e2(v4..v7)-W4(v5+v6+v7)`; since `v1+v2>0` this lower bound can be inserted whatever its sign. Collecting, `E1>=(v1+v2)E2+W3*alpha+W4*beta-W3²/2`. Finally `W4=E3-a1<=E3-W3*S4=K` (Lemma 4) and `beta<0`: for sorted rates `-beta=(v1+v2)(v5-v3)+(v1+v2)v7+((v1+v2)v6-v1v2)>0` (identity checked). So `W4*beta>=K*beta`. □

Y1+ is a quadratic in x (coefficients `d2,d1,d0` polynomials in the six sorted rates).

## 4. Lemma C3 at z3=83/100

**Lemma C3.** No seven positive reals `v1<=...<=v7` satisfy `p>0, q>0, W3>=0, K>=0, Y2b>=0, Y1+>=0` at z=83/100.

*Proof.* Cases by the six non-largest rates.

- (a) `f1<4`: as before (`z3>3/7`).
- (d) `f1>=4, A>0, D>0`: the three-parameter residual cover at z3.
- (b) `f1>=4, A<=0`. If the six rates are not all in `N=[11/21,37/27]`, the compactified cover QO gives `Qpol(z3)>0`, contradicting the crude case (b). Otherwise the sorted cover NB of `N^6` puts the point in a leaf with one of: F (`f1<4`), A (`A>0`), Q (`Qpol>0`), E4v6 (`A<0`, `E4(v6)<0`, so `E4(x)<0` for `x>=v6`), Y2v6 (`A<0`, `Y2b(v6)<0`, `Y2b'(v6)<=0`), Y2tan, Y2E, Disc (`A<0`, discriminant of Y2b negative). Here Y2b is concave (`c2=S3*A<0`), the crude interval is `x_q<x<=x_E` with `x_q=-A/(f1-4)`, `x_E=-B/A`, and
  - **Y2tan**: `A<0`, `f1>4`, `(f1-4)²Y2b(x_q)<0` and `A*(f1-4)²Y2b(x_q)+(f1-4)Y2b'(x_q)*Q0>0` with the UNSCALED `Q0:=A²-(f1-4)B` (Qpol is a positive multiple of Q0); since `(f1-4)(x_E-x_q)=Q0/A`, the second inequality is `Y2b(x_q)+Y2b'(x_q)(x_E-x_q)<0`; the tangent line at x_q dominates the concave Y2b and is negative at both ends of `[x_q,x_E]`;
  - **Y2E**: `A<0`, `A²Y2b(x_E)<0`, `2c2B-c1A>=0` (i.e. `Y2b'(x_E)>=0`), so Y2b<0 for all `x<=x_E`.
  Each selector contradicts the hypotheses (Y2b>=0 or E4>=0); "unsorted" leaves contain no sorted point.
- (c) `f1>=4, A>0, D<=0`. If the six rates are not all in `M=[7/9,5/3]`, the cover HO gives `Hpol(z3)>0` (crude case (c) contradiction). Otherwise the sorted cover MC of `M^6` gives a leaf with: mA (`A<0`), D (`D>0`), H (`Hpol>0`), or **Y1end**: `A>0`, `D<0`, `d2>0` (Y1+ convex in x), `A²Y1+(-B/A)<0` and `D²Y1+(-E/D)<0`. In case (c) the crude constraints give `-B/A<=x<=-E/D` (W3>=0, K>=0); a convex quadratic negative at both ends of a segment is negative on it, contradicting Lemma 6. □

The endpoint formulas `a²g(-b/a)=g2 b²-g1 a b+g0 a²`, `a g'(-b/a)=-2g2 b+g1 a` are checked in both scripts.

## 5. Certificates (exact integers) and actual runs

Generator `frontier-20261029-ph7-threshold-z3-check.py`, **323LF/19488B**, SHA256 `802dfcdb686c85ab24166ffda1c8119f032536d4ff146dcf995bfdbf0fc34440`, run 08:05:23-08:10:27 PDT, actually printed (result lines)

    symbolic-z identities PASS (incl. y^1 coefficient, c2=S3*A, -beta decomposition, endpoint formulas)
    QO leaves 25674 {'pos': 21673, 'R': 4001}
    HO leaves 9473 {'pos': 9345, 'R': 128}
    NB exact leaves 14034 {'Q': 4728, 'Y2tan': 3472, 'unsorted': 4838, 'Y2v6': 67, 'E4v6': 888, 'Disc': 36, 'Y2E': 5} refinements 0
    MC exact leaves 2046 {'H': 601, 'Y1end': 386, 'unsorted': 1059} refinements 0
    SymPy 1.14.0 z3=83/100 exact PASS: ... residual {'Abar<=0': 1051, 'Dbar<=0': 1026, 'f1-4<0': 68}

Certificate `frontier-20261029-ph7-threshold-z3-certificate-v1.json`, **213732LF/2072339B**, SHA256 `b1946079fc0a380e77cdfd1e04dd9e88a6fac6e5379bf8dce65e0ef3acad6d10`. Excluded cubes: `[11/32,37/64]^6` (QO, = N^6 compactified) and `[7/16,5/8]^6` (HO, = M^6). Leaf rules and conventions as in §6 of the addendum; for NB/MC all listed tensors are strictly positive except `mD6` (Y2v6) and `mDE` (Y2E), which are >=0. The NB/MC leaf searches are float-guided; every leaf is verified with integers.

Separately written standard-library replay `frontier-20261029-ph7-threshold-z3-integer-replay.py`, **301LF/18089B**, SHA256 `3ccb226fa299de1307d6db51525035bb5783ba5df338fd9938a9053581d269c1`, run 08:10:43-08:21:45 PDT, actually printed

    identities PASS (stdlib, symbolic z, incl. y^1 coefficient, c2=S3*A, -beta decomposition)
    compactified covers replayed: QO {'pos': 21673, 'R': 4001} HO {'pos': 9345, 'R': 128}
    NB cover replayed: {'Q': 4728, 'Y2tan': 3472, 'unsorted': 4838, 'Y2v6': 67, 'E4v6': 888, 'Disc': 36, 'Y2E': 5}
    MC cover replayed: {'H': 601, 'Y1end': 386, 'unsorted': 1059}
    Independent stdlib replay PASS at z3=83/100: ... residual {'f1-4<0': 68, 'Abar<=0': 1051, 'Dbar<=0': 1026}

It rebuilds Y2b and Y1+ from e1..e6 of seven variables, all selector polynomials, digests, affine Bernstein tensors (own shift-and-convert) and replays every leaf. Same-owner implementation, not human/cross-vendor/Lean verification. A floating regression `frontier-20261029-ph7-coefficient-inequalities-regression.py` (SHA256 `7bf3f369bcc7a0cd8140a84d2a8b60ec72a5a76882ac461d30c76172dd01fe58`) checks Lemma 5 on 2000 random Metzler matrices (diagnostic only).

## 6. Diagnostics (not premises)

All five cover pieces also close in floating arithmetic at z=33/40=0.825 (NB about 1.3e5 leaves). Kernel searches on the system {p,q,W3,K,Y2b,Y1,Y0} (Y0 from the y⁰ coefficient) found feasible points up to z=0.822 and none at 0.823-0.84, so this route cannot go below about 0.8225; the numerically constructed seven-state family reaches about 0.82042.

## 7. Scope and review targets

Review should reconstruct Lemma 6 (y¹ coefficient of the cover identity, pair term bound, interlacing directions, the W5 and W4 substitutions, beta<0), the new selectors Y2tan/Y2E/Y1end and their interval logic, the region inclusions (QO/HO excluded cubes vs N^6/M^6), and the certificates. Imports: the adopted caller, Lemma S, Lemmas 1-5 (adopted in f159/f160). No formal, kernel, human, cross-vendor, novelty or priority acceptance is claimed; historical holds and process findings are unchanged.

END - no seven-state PH representation exists for any z>=0.83; the supremum of PH7-realizable ratios lies in [41/50, 0.83].
