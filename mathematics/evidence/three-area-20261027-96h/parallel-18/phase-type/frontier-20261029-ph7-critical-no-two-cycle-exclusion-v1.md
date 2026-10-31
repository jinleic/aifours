# Every critical PH7 realization at 8/9 must contain a directed 2-cycle

**NEW ALL-TOPOLOGY CRITICAL-RATIO THEOREM CANDIDATE.** Written proof, exact SymPy identity checks, an exact integer three-parameter Bernstein selector certificate, and a separately implemented standard-library Fraction replay. It imports the already pinned girth-four positivity certificate. Not independently reviewed; parent adoption, formal proof and novelty clearance are pending. MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 04:37:23 PDT 2026**.

This is NOT an 8/9 existence/exclusion verdict and NOT a minimum-order claim.

## 1. Theorem

At `z=b²/(a-c)²=8/9`, if the original H has an actual PH representation with at most seven states, its directed off-diagonal transition graph must contain a **directed 2-cycle**.

Equivalently: no irreducible seven-by-seven Metzler matrix G of spectral bound0 whose characteristic polynomial contains the factor

    D(y)=y[(y+1)^2+8/9]^2

has a graph without directed 2-cycles. Any number of directed 3-, 4-, 5-, 6- or 7-cycles, any edge count, holding rates, hidden roots and input/exit supports are allowed in the contradiction.

The PH caller is the same as in the girth-four theorem `frontier-20261028-ph7-critical-two-or-three-cycle-theorem-v1.md` (SHA256 `76ff376815423d69546c10e2608f7c373a80f3e7752d306c911751e8eb50f33b`): the separately supported SCC/irreducibility theorem `frontier-20261028-ph7-global-irreducibility-v1.md` (SHA256 `729926c5fa9779ec4b1ca27156f80c4ca80c49c973ca4c7cbf352da614a94b49`) supplies exactly seven reachable states, irreducibility and spectral bound0 after shift/scale. The argument below is spectral-only.

Relation to earlier candidates: this strictly strengthens the girth-four theorem (which needed a 2- OR 3-cycle). Every earlier owner exclusion of a specific no-2-cycle graph class (unique triangle, two disjoint triangles, three-triangle chains/shared edges, linear families, nested fork, ...) is a special case, but none of those manuscripts is used here. If the separately pending mandatory-triangle candidate is also accepted, a critical realization would need both a 2-cycle and a 3-cycle; that combination is not asserted here.

## 2. Characteristic coefficients without 2-cycles

Irreducibility and the positive Perron vector make every diagonal entry strictly negative; write the escape rates `u_1,...,u_7>0` and their elementary sums `e_k`. Let `W` be the sum of the weights (products of off-diagonal entries) of all directed 3-cycles, `CW=sum_t w_t U(V\t)` where `U(V\t)` is the sum of the four rates outside the 3-cycle t, and `C4>=0` the total weight of directed 4-cycles.

In the permutation expansion of `det(yI-G)`, a term of y-degree at least3 moves at most four vertices. Without 2-cycles it is the identity, one 3-cycle t, contributing `-w_t prod_{i not in t}(y+u_i)`, or one 4-cycle c, contributing `-w_c prod_{i not in c}(y+u_i)` (permutation sign times four negated off-diagonal entries). Hence

    [y^6]=e1,  [y^5]=e2,  [y^4]=e3-W,  [y^3]=e4-CW-C4.                (CHAR)

Write `det(yI-G)=D(y)(y^2+p y+q)`. Matching (CHAR) gives `p=e1-4`, `q=e2-4e1+74/9` and

    E4:=e3-4e2+(74/9)e1-28/3 = W >= 0,
    E3:=e4-(70/9)e2+(212/9)e1-1007/27 = CW+C4.

All non-Perron eigenvalues of irreducible G have negative real part, so the hidden roots give **p>0 and q>0**. Every 3-cycle has `U(V\t)>=S4`, the sum of the four smallest rates. Therefore

    K:=E3-E4*S4 = C4 + sum_t w_t (U(V\t)-S4) >= 0.                     (REQ)

## 3. Reduction to six rates and four exhaustive cases

Let x be a largest rate and `f_1,...,f_4` the elementary sums of the other six rates; `S4` is then the sum of the four smallest of those six. With the girth-four notation

    A=f2-4f1+74/9,  B=f3-4f2+(74/9)f1-28/3,
    h0=f4-(70/9)f2+(212/9)f1-1007/27,  h1=f3-(70/9)f1+212/9,

the exact identities are

    q=A+x(f1-4),  E4=A x+B,  E3=h0+x h1,
    K=E+x D,  D:=h1-A*S4,  E:=h0-B*S4,  E*A-B*D=h0*A-h1*B.           (SPLIT)

Imported fact (the only earlier computer-assisted inequality): for EVERY six positive rates,

    Qpol=81[A^2-(f1-4)B]>0,   Hpol=-243[h0 A-h1 B]>0,

from the pinned girth-four certificate (5332 and 5334 integer Bernstein leaves). The present checker and replay both recompute the exact Qpol/Hpol coefficient digests and match them to that certificate.

**(a) f1<4.** p>0 gives `x>4-f1`. q>0 forces A>0 and `x<A/(4-f1)`, so `A>(4-f1)^2`. But `5f1^2-12f2=sum_{i<j}(r_i-r_j)^2>=0`, hence

    A-(4-f1)^2 = f2+4f1-f1^2-70/9 <= -(7/12)f1^2+4f1-70/9 = -58/63-(7/12)(f1-24/7)^2 < 0.

**(b) f1>=4, A<=0.** If A<0: `E4>=0` gives `x<=B/|A|`; q>0 gives f1>4 and `x>|A|/(f1-4)`; hence `A^2<(f1-4)B`, i.e. Qpol<0. If A=0: q>0 gives f1>4, `E4=B>=0`, so `Qpol=-81(f1-4)B<=0`. Both contradict Qpol>0. (If f1=4 and A<=0 then q=A<=0 directly.)

**(c) f1>=4, A>0, D<=0.** `E4>=0` gives `x>=-B/A`; since D<=0, `K=E+xD<=E-BD/A=(EA-BD)/A=-Hpol/(243A)<0`, contradicting (REQ).

**(d) f1>=4, A>0, D>0.** Impossible by Section4.

These cases are exhaustive, so no 2-cycle-free realization exists. □

## 4. The residual case (d)

Split the six rates into the four smallest `a_1..a_4` (elementary sums `alpha_k`) and the two largest `r5,r6` (`beta1=r5+r6`, `beta2=r5 r6`). Exact identities (checked):

    D = K1 + beta1*K2   (beta2 cancels),
    K1 = alpha3-alpha1*alpha2+4alpha1^2-16alpha1+212/9,
    K2 = alpha2-alpha1^2+4alpha1-70/9,
    A  = (alpha2-4alpha1+74/9) + beta1(alpha1-4) + beta2.

Elementary bounds: `beta2<=beta1^2/4`; `alpha1*alpha2-6alpha3=(1/2)sum_{i not in {j,k}} a_i(a_j-a_k)^2>=0`; `3alpha1^2-8alpha2=sum_{i<j}(a_i-a_j)^2>=0`; and `beta1>=2 max_i a_i>=alpha1/2`. Hence

    A <= Abar := (alpha2-4alpha1+74/9)+beta1(alpha1-4)+beta1^2/4,      Abar-A=(r5-r6)^2/4,
    D <= Dbar := 4alpha1^2-16alpha1+212/9-(5/6)alpha1*alpha2+beta1*K2,  Dbar-D=alpha1*alpha2/6-alpha3.

Put `y=alpha1>0`, `alpha2=(3/8)tau*y^2` with `tau in (0,1]`, and `gam=beta1-y/2>=0`. Case (d) would produce a point with `Abar>0`, `Dbar>0` and `f1-4=(3/2)y+gam-4>=0`. The scaled polynomials are

    144 Abar = 36gam^2+180gam*y-576gam+54tau*y^2+81y^2-864y+1184,
    144 Dbar = 54gam*tau*y^2-144gam*y^2+576gam*y-1120gam-18tau*y^3-72y^3+864y^2-2864y+3392,
    2(f1-4)  = 2gam+3y-8.

**Certificate.** Compactify `y=s/(1-s)`, `gam=g/(1-g)` and multiply by the positive factors `(1-s)^deg_y (1-g)^deg_gam`; keep tau on [0,1]. Exact rational tensor Bernstein coefficients are scaled to integers and subdivided by exact midpoint de Casteljau, splitting coordinate `depth mod 3`. A complete prefix-free binary cover of the closed unit cube has **1653 leaves**: 800 with every Abar coefficient <=0, 789 with every Dbar coefficient <=0, and 64 with every `f1-4` coefficient <0. Every finite point (s,g<1) lies in some leaf, where the positive compactification factor preserves signs; thus at every admissible point `Abar<=0` or `Dbar<=0` or `f1<4`. Non-strict signs suffice for Abar and Dbar because case (d) needs both strictly positive. This closes case (d).

## 5. Actual checks

Primary `frontier-20261029-ph7-no-two-cycle-reduction-check.py`, **150LF/9161B**, SHA256 `6c88f6707f9af73b77de262b8704dabe1fafcf968ebe1a705234aee72960c93c`, actually printed

    identities PASS
    girth-four Qpol/Hpol digests match pinned certificate
    SymPy 1.14.0 exact 3D residual selector cover PASS; leaves 1653 {'Abar<=0': 800, 'Dbar<=0': 789, 'f1-4<0': 64}

It verifies by SymPy expansion: the seventh-rate splitting of q, E4, E3; the coefficient matching constants; (SPLIT) including `EA-BD=h0A-h1B`; the beta2 cancellation and the A decomposition; `Abar-A` and `Dbar-D`; the three sum-of-squares identities; and the completed square in case (a).

Certificate `frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json`, **6659LF/76318B**, SHA256 `45256245ecda8aed8ec18150c642fd70c3665cd9af31c49dc59fb25e367ed6be` (polynomials, coefficient digests, all 1653 leaf paths with selector labels).

Separately written STANDARD-LIBRARY-ONLY replay `frontier-20261029-ph7-no-two-cycle-integer-replay.py`, **188LF/9774B**, SHA256 `abaa152c15444dbe7333465f65fc873533399366bfb9ad870f77281ec10a80a3`, actually printed

    identities PASS (stdlib sparse Fraction polynomials)
    characteristic matching constants PASS
    girth-four Qpol/Hpol digests reproduced independently
    Independent stdlib Fraction replay PASS: complete binary cover, 1653 leaves {'f1-4<0': 64, 'Abar<=0': 800, 'Dbar<=0': 789}

It rebuilds every identity with its own sparse Fraction polynomial arithmetic, recomputes the Qpol/Hpol digests, rebuilds the three residual polynomials from their defining formulas and matches their digests, checks the leaf set is prefix-free and complete, and replays every leaf with exact Fraction midpoint subdivision. It is same-owner independent implementation evidence, not human/cross-vendor/Lean verification.

Imported, unchanged: girth-four certificate `frontier-20261028-ph7-girth4-critical-bernstein-certificate.json` SHA256 `b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8`, its checker SHA256 `8f5fc02b87996bbda2ea8b7af1976b467ef3c9a46c3a9b9274e538eea941e1c4`, stdlib replay SHA256 `ac5b069e3d4d5c108b9b9a6e3df12172f5bc360390f92c119a0af58e48116177`, and boundary check SHA256 `03d2853e583ddb5284eb2d5a35a0bae063ab1b104df40350a5283128359ee204`. Their review status is the parent's record and is not asserted here.

## 6. Review targets and remaining gap

A disjoint reviewer should reconstruct (CHAR), the Perron signs p>0 and q>0, the inequality `U(V\t)>=S4` and (REQ), the case split (a)-(d) including the boundary cases f1=4 and A=0, (SPLIT), the residual-case reductions (beta2 monotonicity, the alpha3 and alpha2 bounds, `beta1>=alpha1/2`), the parametrization, and the cover's compactification and completeness.

The theorem does NOT exclude graphs with a directed 2-cycle, does not decide the original 8/9 question, and does not establish minimum8. The exploratory numerical observation that the crude no-2-cycle system has tiny relative margins near equal rates is not a premise; the exact proof routes that region through Hpol>0. Historical holds and process findings are unchanged and are not used as premises.

END - every critical seven-state PH realization at 8/9 must contain a directed 2-cycle.
