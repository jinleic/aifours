# A rigorously isolated two-cycle PH7 endpoint and its entire lower band

**MathResearch96h-2 / math-1. NEW ACTUAL CONSTRUCTION CANDIDATE with exact rational interval and symbolic checks; independent review and novelty clearance pending.** Actual native observation before writing: **Wed Oct28 17:37:22 PDT2026**. This additive v4 is separate from the earlier root-family `frontier-20261028-ph7-algebraic-endpoint-v3.md` (SHA256 `99ec7400496a91963cffd55a16202e4ca07d5e5e90e734bcf6585931b2d14ed2`); no earlier bytes are changed.

## 1. Result and exact algebraic parameters

Let `d=a-c>0`, `z=b^2/d^2`, and consider the original repeated-pole transform

    H(s)=c(a^2+b^2)^2 / [(s+c)((s+a)^2+b^2)^2].

We define an algebraic triple `(U,V,z_*)` as the UNIQUE solution inside the rational closed box

    |U-1338787907/10^9| <= 10^-7,
    |V-1042029691/10^9| <= 10^-7,
    |z_*-820420441/10^9| <= 10^-7,                (BOX)

of THREE EXPLICIT polynomial equations defined in §2. A fully rational contraction certificate for existence and uniqueness is given in §3. In particular

    820420341/10^9 < z_* < 820420541/10^9 < 8/9.  (LOC)

The strict inequalities follow because the contraction maps the box into its interior. The previous v3 root was below `82041/100000=820410000/10^9`, so this new z_* is strictly beyond it.

**Actual PH7 theorem candidate.** For EVERY c,d>0 and EVERY real z in the ENTIRE CLOSED interval `[7/9,z_*]`, the explicit same-matrix construction in §4 is an actual seven-state PH representation of H. Its endpoint has two zero feedback entries but retains positive normalization and all physical ties. No numerical solution is promoted to a witness: BOX and its exact polynomial/contraction definitions fix the parameters mathematically.

The earlier topology-unrestricted PH6 lower, at its named existing written-support cut, then gives minimum exactly7 on this interval; the earlier supported band overlapping7/9 extends the conditional composition to `[13/20,z_*]`. No all-topology optimum or 8/9 decision follows.

## 2. Three exact coefficient equations, not a numerical fit

For indeterminates U,V,z,y define

    p0=5U+2V-4,
    q0=10U^2+10UV-20U+V^2-8V-2z+10,
    D_z(y)=y[(y+1)^2+z]^2,
    R(y)=(y+U)^5(y+V)^2-D_z(y)(y^2+p0 y+q0).

Write `[y^j]R` for the literal coefficient of y^j, and put

    D1_0=[y^2]R,
    E4=[y^4]R,
    E3=[y^3]R,
    E1=[y]R-2V D1_0,
    D3_0=[y^0]R-V^2 D1_0.                          (EQ)

The defining equations of the triple are

    E4(U,V,z)=E3(U,V,z)=E1(U,V,z)=0.

These are fully specified rational-coefficient polynomials; no hidden root, matrix data or solver-output table is needed to interpret them. For orientation, the expanded E4 is

    10U^3+20U^2V-40U^2+5UV^2-40UV-10Uz+50U
      -4V^2-4Vz+20V+12z-20.

The leading y7 terms in R cancel automatically. The definitions of p0,q0 cancel y6,y5, while D1_0 and D3_0 cancel y2 and y0. Consequently for the actual two-cycle matrix at the root the complete characteristic residual is EXACTLY `E4 y^4+E3 y^3+E1 y`, not a selected-coefficient approximation.

## 3. Rational contraction: actual existence and uniqueness in BOX

Let `F=(E4,E3,E1)` and let J be its 3-by3 Jacobian in variables(U,V,z). The exact rational center x0 and radius r are those displayed in(BOX). Define the rational matrix

    A=J(x0)^(-1),      Phi(x)=x-A F(x).

The pinned checker verifies J(x0) is invertible and `A J(x0)=I` exactly. It then expands every polynomial Jacobian entry about x0, bounds every nonconstant monomial by the product of the rational radii, and checks the following uniform inequalities on the WHOLE box:

    ||I-A J(x)||_infinity < 1/100,
    ||A F(x0)||_infinity < r/100.                    (CONTR)

Thus Phi is a strict contraction on the closed box and maps it into its interior: for x in BOX, `||Phi(x)-x0|| <= r/100+r/100<r`. The ordinary contraction principle follows here by iterating Phi from x0: the geometric difference bound gives a Cauchy sequence in the complete box; continuity gives a fixed point; the strict Lipschitz factor gives uniqueness. Since A is invertible, that fixed point is exactly a zero of F. This proves the triple exists and is unique in BOX, without relying on the floating optimizer that originally suggested the box.

The exact rational centered-polynomial bounds and actual residual/norm values are stored in the pinned certificate. The displayed coarse strict inequalities are the proof predicates, not rounded estimates. No assumption of simple roots outside BOX or global uniqueness is made.

## 4. Actual nonuniform family for EVERY z <= z_*

Fix the algebraic U,V just constructed and choose the six raw principal-chain rates

    u1=u2=u3=U,      v1=U,      v2=v3=V.

For arbitrary z in `[7/9,z_*]`, let e_j be the jth elementary symmetric polynomial of these six rates. Define

    A0=e1, B0=e2, C0=e3,
    H0=B0+4A0-A0^2-6,
    L=B0-4A0+10-2z,
    N=4H0+4-C0-B0(4-A0)-4z,
    p=N/L, q=(A0-4)p+H0-2z, w=p+4-A0,
    B=p-2U, C=q-U p+U^2,
    Q(y)=y^2+p y+q=(y+U)^2+B(y+U)+C.

As in the fully printed v2/v3 construction, define the SAME-matrix feedback

    phi=e4+C0 w-[(6+2z)q+(4+4z)p+(1+z)^2],
    R2=e5+e4 w-(4+4z)q-(1+z)^2 p,
    R1=e6+e5 w-(1+z)^2 q,  R0=e6 w,
    D1=R2-3U phi,
    D2=R1-3U^2 phi-2V D1,
    D3=R0-U^3 phi-V^2 D1-V D2.

The actual raw generator is

    G = [ -U  1   0   0   0   0   0
           0 -U   1   0   0   0   0
           0  0  -U   1   0   0   0
           0  0   0  -w   1   0   0
           D1 0   0   0  -U   1   0
           D2 0   0   0   0  -V   1
           D3 0   0  phi  0   0  -V ],
    beta=(C,B,1,0,0,0,0),
    gamma=K e7,  K=D_z(c).

For ALL formal z with L!=0, the same actual-matrix elimination as v2 gives

    det(yI-G)=D_z(y)Q(y),
    beta adj(yI-G)e7=Q(y).                          (ID)

The proof uses the explicit coefficient definitions, not an independently guessed characteristic polynomial. Its full actual7-by7 determinant pattern is also verified by the pinned checker at the two-cycle endpoint; the source v2 gives the general symbolic determinant/normalizer derivation with arbitrary six rates.

At z=z_*, the defining equations imply `w=U`, `phi=0`, `D2=0`: E4=0 is exactly `L p0=N`, so p=p0 and w=U. Then E3 is the y3 residual and forces phi=0; E1 is the remaining y coefficient after D1 and forces D2=0. Thus endpoint G is the TWO-CYCLE graph with five consecutive U diagonals, two V diagonals, positive D1 from its fifth state back to its first and positive D3 from its last state back to its first. The checker independently verifies its full characteristic residual is `E4*y^4+E3*y^3+E1*y`.

## 5. Uniform signs on the whole band, INCLUDING the algebraic endpoint

The checker converts each polynomial below to Bernstein form in z over the larger rational interval `[7/9,820421/10^6]`. Each Bernstein coefficient is itself a polynomial in U,V. Expanding it exactly about the rational rate center of(BOX), then bounding nonconstant monomials by `10^-7` to their total degree, proves UNIFORMLY for every U,V in the entire rate box:

    L>1, Lp>7, Lq>9, Lw>2,
    LB>3, LC>2, LD1>3, LD3>2,
    partial_z(L phi)<-6,   partial_z(L D2)<-9/10.    (SIGN)

The last two are strict negative upper bounds on EVERY z in that full rational interval, not evaluated sample points. At the actual root, `L phi=L D2=0` by §4. Therefore, for EVERY z<=z_* in the band, both `phi>=0` and `D2>=0` (strict for z<z_*). All other displayed physical quantities are strictly positive. The root BOX lies wholly inside the larger sign interval. No assumption that U,V are rational, no division by a possibly zero feedback, and no unproved positivity of an independently chosen scalar profile is used.

## 6. Complete actual PH normalization for all c,d>0

For d=1, c>0 set `K=D_z(c)`, `Q_c=c^2+p c+q>0`, and

    h1=1/Q_c, h2=(c+U)h1, h3=(c+U)h2, h4=(c+U)h3,
    h7=[K+D3 h1+phi h4]/(c+V),
    h6=[h7+D2 h1]/(c+V),
    h5=[h6+D1 h1]/(c+U).

All entries are strictly positive throughout the CLOSED band, including phi=D2=0 at z_*. The six noncenter rows of `(cI-G)h=K e7` are immediate. The center row follows from(ID) at y=c and the recurrence, exactly as in the fully detailed v2 §5; beta h=1 follows from Q's numerator identity. Equivalently one can verify the actual seven row identities symbolically in the general six-rate construction, as already done by the pinned v2 checker; substitution of the algebraic U,V is legitimate because L>0 and the denominators are nonzero.

Set Delta=diag(h), `T=Delta^(-1)(G-cI)Delta`, `alpha=beta Delta`, `omega=Delta^(-1)K e7`. Then T is Metzler, `alpha>=0`, `alpha1=1`, `omega>=0` and `-T1=omega`. By(ID), G has the simple zero, the repeated pair `-1±i sqrt(z)` and the roots of `Q`; p,q>0 put the latter roots strictly in the left half-plane. Shifting by c>0 makes T Hurwitz. The SAME beta,G,gamma give exact transfer `K/D_z(s+c)`.

For arbitrary physical d>0 perform this construction at c/d, multiply T and omega by d, and keep alpha unchanged. This yields the actual original H for ALL positive c,d throughout the closed interval.

## 7. Exact verification actually performed

Completed command:

    python3 frontier-20261028-ph7-two-cycle-interval-check.py
    SymPy 1.14.0 exact rational contraction/interval signs/matrix identity PASS
    q <1/100, center error < radius/100
    root z in 820420341/1000000000 820420541/1000000000
    all positivity floors and both derivative upper bounds PASS

The checker uses exact SymPy polynomial expressions and Python `fractions.Fraction`; no floating arithmetic is used in the certificate. It checks:

1. the full 7x7 two-cycle determinant and all residual-coefficient definitions;
2. J(x0) invertibility, exact rational preconditioner and all Jacobian/remainder bounds yielding(CONTR);
3. ALL z-Bernstein coefficients of the physical numerators, uniformly over the entire rational U,V box by exact centered-polynomial bounds;
4. the two strict derivative bounds in(SIGN) on the entire z interval/rate box.

Checker `frontier-20261028-ph7-two-cycle-interval-check.py`, **127LF/6150B**, SHA256 `dd202e2dfa2039f535834edcd4d2ff184376d03a5d4fe1289b68683ecaf54e97`.

Exact certificate `frontier-20261028-ph7-two-cycle-interval-certificate.json`, **62LF/2684B**, SHA256 `2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88`.

The general six-rate symbolic determinant/normalizer checker is the already pinned `frontier-20261028-ph7-band-41over50-check.py`, SHA256 `e0172cb2005b0de9b0bcf7285d53632fe754466ebe1d9a9078d945663861aa89`. Its particular fixed rational rates are not substituted as the present U,V. Its general matrix derivation is reproduced in v2; a fresh reviewer should either redo it for symbolic U,V or verify the displayed algebra directly. No claim is made that the earlier fixed-rate script alone checked this algebraic family.

The initial floating optimization suggested a neighborhood only; it is not a proof premise. Its actual result is `frontier-20261028-ph7-ordered-continuation-search-result.json`: numerical candidate near the box, no exact witness was claimed by that optimizer. Exact rational box/contraction and full signs above are the actual evidence. No all-u or all-PH7 optimality follows from the optimizer convergence.

## 8. Prior dependencies and honest original boundary

The exact upper construction is a new candidate, not automatically parent-adopted. To claim EXACT minimum7, use the named old topology-unrestricted PH6 lower `proof-unrestricted-six-state-barrier-v1.md` SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25` at its ordinary written-supported z>1/2 cut. To extend the lower end from7/9 to13/20, also use the earlier parent `PH7-entire-rational-seven-ninths-band-parent-v1.md` at its explicit overlap/import scopes. The prior fixed-rate v2/v3 candidate alone is not prior parent adoption. All source/trust qualifications remain.

This source proves no optimum endpoint, PH7 existence/exclusion at8/9, general upper band beyond z_*, or entire H_(1,2) minimum-order function. A differently parametrized graph can do better. Exact symbolic/rational executable checks are not formal/kernel/independent-family/human review, priority or novelty acceptance.

Prior held outputs remain historical/unvalidated and were not used as accepted premises; no process finding is cured. Same18/exclusive owner root, no Git push/deletion/publication/secrets/unsolicited external-model campaign/infrastructure mutation; research deadline2026-10-31T21:23:27Z. Full separate review must reconstruct root existence, all uniform sign bounds, exact SAME-matrix coefficient/normalizer identities and each old lower/overlap application before adoption.

**END — exact isolated algebraic two-cycle PH7 endpoint with full closed lower band; 8/9 and global optimality remain open.**
