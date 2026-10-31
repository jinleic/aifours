# An actual nonuniform PH7 family on the explicit band [7/9, 813/1000]

**MathResearch96h-2 / original math-1. NEW CONSTRUCTIVE CANDIDATE with executed exact symbolic/rational checks; not yet independently reviewed or novelty-cleared.** Native observation before this write: **Wed Oct28 17:16:40 PDT2026**. All files mentioned below are new under the exclusive owner root unless explicitly identified as immutable earlier sources.

## 1. Exact target, result and nonclaims

For arbitrary `a>c>0`, `b>0`, put `d=a-c` and `z=b^2/d^2`. The original target is

    H(s)=c(a^2+b^2)^2 / [(s+c)((s+a)^2+b^2)^2].

**New upper-bound candidate.** For EVERY `c,d>0` and EVERY real

    7/9 <= z <= 813/1000,

there is an explicit actual seven-state PH realization of this SAME transfer, with nonnegative initial row, literal nonnegative exit, Hurwitz Metzler subgenerator and all row ties. Equivalently choose `a=c+d`, `b=d sqrt(z)`. The construction below contains no search-dependent floating point coefficient.

At the previously written-supported unrestricted PH6 lower theorem, cited exactly in §7 rather than re-proved here, this gives **minimum order exactly7 on this entire band**. Without that independently retained lower input, the new result is ONLY `order<=7`. The general `z=8/9` point, maximum band, full minimum-order function and unrestricted all-topology classification remain open.

The old parent-supported explicit chain has `7/9<z_star` and works through z_star. The separate exact chart obstruction in `frontier-20261028-ph7-three-chain-explicit-global-obstruction.md` shows that OLD equal-rate-within-each-chain family has no physical realization for `z>=389/500`. Since `7/9<389/500<813/1000`, the nonuniform family here reaches beyond that ENTIRE old one-free-u chart. This is not a proof of literature priority or that every previously known PH7 construction stops there.

## 2. Actual six-rate matrix and coefficient formulas

First take d=1 and leave c>0 arbitrary. Fix the SIX positive rational raw rates

    u1=657/500,  u2=34/25,   u3=701/500,
    v1=333/250,  v2=973/1000, v3=1083/1000.

Define the elementary symmetric functions e_j of these SAME six rates, j=1,...,6. Put

    A=e1,       B2=e2,       C3=e3,
    H0=B2+4A-A^2-6,
    L=B2-4A+10-2z,
    N=4H0+4-C3-B2(4-A)-4z,
    p=N/L,
    q=(A-4)p+H0-2z,
    w=p+4-A,
    B=p-u1-u2,
    C=q-u1u2-u1 B,
    Q(y)=y^2+p y+q.

The single common denominator is L. Algebra gives the ACTUAL numerator identity

    Q(y)=(y+u1)(y+u2)+B(y+u1)+C.                (Q)

Set

    phi=e4+C3*w-[(6+2z)q+(4+4z)p+(1+z)^2],
    R2=e5+e4*w-(4+4z)q-(1+z)^2 p,
    R1=e6+e5*w-(1+z)^2 q,
    R0=e6*w,
    D1=R2-phi(u1+u2+u3),
    D2=R1-phi(u1u2+u1u3+u2u3)-(v2+v3)D1,
    D3=R0-phi u1u2u3-v2v3 D1-v3 D2.

Define the SINGLE raw7-by7 real matrix G(z), row beta and column gamma(c,z) by

    G = [ -u1  1    0    0    0    0    0
           0  -u2   1    0    0    0    0
           0   0   -u3   1    0    0    0
           0   0    0   -w    1    0    0
           D1  0    0    0   -v1   1    0
           D2  0    0    0    0   -v2   1
           D3  0    0   phi   0    0   -v3 ],
    beta=(C,B,1,0,0,0,0),
    gamma=K e7,
    K=D_z(c),  D_z(y)=y[(y+1)^2+z]^2.

All matrix entries, initial coefficients, feedback and hidden factors are linked by these definitions. This is a NEW six-rate nonuniform construction, not the equal-u/equal-v chart or an independently assigned characteristic polynomial.

## 3. Entire characteristic AND actual numerator, including coincident roots

The exact identities for the SAME G,beta are

    det(y I-G)=D_z(y)Q(y),
    beta adj(y I-G)e7=Q(y).                      (ID)

The first is checked as the full symbolic7-by7 determinant, coefficientwise in BOTH y and z. For the second use the polynomial rank-one determinant identity

    det(yI-G+e7 beta)-det(yI-G)=beta adj(yI-G)e7,

then compare the entire symbolic polynomial with Q(y). The checker does NOT infer the numerator from only a subset of coefficients or from roots. Equivalently, the upstream bidiagonal adjugate column is

    (1, y+u1, (y+u1)(y+u2))^T,

and the downstream entry-to-last-state adjugate coefficient is1; the beta combination is exactly(Q). Both identities are polynomial, so repeated/coincident hidden or principal roots require no inverse-at-a-root exception.

The executable symbolic check in §6 confirms(ID) exactly over rational functions of z; its assumptions/poles are separately dealt with by L>0 on the interval. It is not a numerical interpolation.

## 4. Strict positivity on the ENTIRE CLOSED z-band

For each coefficient below, multiply by L; retain L itself as the first polynomial. Write each resulting polynomial in the Bernstein basis on `[7/9,813/1000]`. The degree and the SMALLEST exact Bernstein coefficient are:

|Polynomial|Bernstein degree|Exact smallest coefficient|
|---|---:|---:|
|L|1|`1655827/1000000`|
|L p|1|`197624241/25000000`|
|L q|2|`821082825464857/81000000000000`|
|L w|1|`387385171/187500000`|
|L B|1|`15434139089/4500000000`|
|L C|2|`206156361843349/81000000000000`|
|L phi|3|`1537854116399697/250000000000000000`|
|L D1|3|`1101567448349339830399/281250000000000000000`|
|L D2|4|`8070475831016351252607/62500000000000000000000`|
|L D3|4|`313487595401834859325348379107/136687500000000000000000000000`|

ALL coefficients, not just the minima, are listed exactly in the certificate JSON in §6. Bernstein basis functions are nonnegative and sum to1, so these strict rational margins prove

    L,p,q,w,B,C,phi,D1,D2,D3 > 0

simultaneously for EVERY real z in the CLOSED interval, with no numerical interpolation, uncorrelated-parameter relaxation, root ordering or endpoint-only argument. The small phi margin at the upper end is positive exactly, not merely in floating point.

## 5. Positive normalization and exact PH realization for EVERY c>0

Because p,q>0, `Q(c)>0` for c>0. Define the actual positive vector h by

    h1=1/Q(c),
    h2=(c+u1)h1,
    h3=(c+u2)h2,
    h4=(c+u3)h3,
    h7=[K+D3 h1+phi h4]/(c+v3),
    h6=[h7+D2 h1]/(c+v2),
    h5=[h6+D1 h1]/(c+v1).

Every numerator and denominator is strictly positive by §4, so every component of h is strictly positive. The seven actual row equations are

    (cI-G)h=K e7.                                (ROW)

All except the center row follow directly from the recurrence. For the center row, substitute the recurrence into `(c+w)h4=h5` and multiply by `Q(c) product_j(c+v_j)`. The resulting polynomial identity is exactly the value at y=c of(ID). Thus no positivity of an unexplained inverse or separate guessed center equation is assumed. A second independent symbolic checker verifies ALL seven row equations directly as identities in c,z.

By(Q),

    beta h=[C+B(c+u1)+(c+u1)(c+u2)]/Q(c)=1.

Set `Delta=diag(h)` and

    T=Delta^(-1)(G-cI)Delta,
    alpha=beta Delta,
    omega=Delta^(-1)K e7.

Strict positivity of all G off-diagonal coefficients makes T Metzler; alpha>=0 and alpha1=1; omega>=0; and(ROW) gives the LITERAL identity `-T1=omega`. From(ID), the raw eigenvalues in y are0, `-1±i sqrt(z)` each twice, and the roots of `y^2+p y+q`. Both latter roots have negative real part because p,q>0. Shifting by c>0 makes T Hurwitz. Similarity and the same-matrix numerator yield, for all s,

    alpha(sI-T)^(-1)omega
      =K Q(s+c)/[D_z(s+c)Q(s+c)]
      =K/D_z(s+c).

Polynomial clearing handles any cancellations/coincidences. This is an ACTUAL PH representation, not merely stable poles, a positive density, a signed realization or a list of independent residues.

For general d>0, apply the construction with `c0=c/d`, then multiply T and omega by d, leaving alpha unchanged. The target becomes exactly the original dimensional H with `a=c+d`, `b=d sqrt(z)`. This proves the full c,d quantified upper construction.

## 6. Executed exact verification and reproducible artifacts

The scientific discovery search was numerical only at the proposal stage; the proof does NOT rely on its optimizer residuals. The following completed exact checks are the actual verification evidence:

1. `python3 frontier-20261028-ph7-seven-band-check.py` returned **“SymPy 1.14.0 Fraction exact symbolic determinant/numerator/positivity assertions PASS.”** It checked the FULL symbolic7x7 determinant, the rank-one-update adjugate numerator, and ALL Bernstein coefficients of L and the nine L-scaled coefficients over the entire closed interval. Script:76LF/3944B SHA256 `3721a481c2a292b6edbcdea657f319bc291b0d327c3765cb36f58f096e2f24c2`. Full exact certificate:86LF/3505B SHA256 `76c10f36fbd92829b98d76c8df00c6a36178d64403eaf8028275f9deb5061d57`.
2. `python3 frontier-20261028-ph7-seven-band-normalizer-check.py` returned **“all 7 row equations and beta*h=1 symbolic assertions PASS.”** Independently constructs the coefficient functions and symbolic h in c,z and checks EVERY row of(ROW) plus beta h=1. Script:53LF/2688B SHA256 `bde1e3fc0cf07d3095869a0510357e2090bfbc4c92c9b7d15a547a15205c9604`; certificate:24LF/539B SHA256 `4d16f1b70f9ed4bd6a579f6198ada3c497412afe5c65905b28d0584524d0124f`.
3. `python3 frontier-20261028-ph7-nonuniform-range-search.py` produced exact-rational matrix witnesses at `z=79/100`, `4/5` and `13/16` via its ACTUAL7-by7 determinant, adjugate numerator, positive h, Metzler, row/probability/exit and Hurwitz checks. Script:76LF/3840B SHA256 `f88de00c1d2b358a2146c26ff931f26693ea2c8a6b3c101513bcf4659519cf9e`; result:747LF/17755B SHA256 `a67d20049aa4f19db1194cd630fada152ad84768a4af379e49aac35df28a2bd3`. Those point checks are redundant evidence, NOT the proof of the closed continuum.

Local cached SymPy1.14.0/SciPy1.17.1 were installed in the owner-local `frontier-20261028-localdeps` directory; no global Python installation was changed. The checks are exact symbolic/rational program outputs, NOT formal/kernel proof, independent-family review, source-priority or publication acceptance. No reported unsuccessful search is used to establish a negative result.

## 7. Exact-order composition and original open remainder

The old parent-supported unrestricted lower source is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. It states a topology-unrestricted PH6 exclusion whenever `z>1/2`, including reducible/canceled-mode cases. This is a named earlier written-supported input, NOT newly reverified by the above construction.

With that input, every z in `[7/9,813/1000]` has minimum exactly7. Because the earlier parent-supported direct exact-order7 band `[13/20,z_star]` has `z_star>7/9`, the intervals overlap. Consequently their UNION gives the candidate composition

    minimum PH order = 7 for EVERY z in [13/20,813/1000].

This composition retains the B6 lower and earlier parent-written construction/review at their actual named boundaries; no fresh full historical proof-DAG, unconditional extension down to1/2, formal verification or priority/SOTA conclusion is claimed. The new upper construction itself is independent of B6.

The present band exceeds the entire previously examined equal-rate one-free-u chart, whose exact physical obstruction begins at389/500, but it does NOT cover `z=8/9`. Whether seven states work at8/9, whether a different topology reaches further, the optimal new endpoint, and the exact minimum throughout the whole PH-existence region remain open. No numerical miss at8/9 is evidence of universal impossibility.

## 8. Controls and trust

The earlier held/quarantined outputs remain historical/unvalidated; no result is accepted merely by the new owner direction. This work uses the explicit allowed earlier common-matrix formulation and new independently written derivation/checkers, not a prior held diagnostic or private guide as proof. All old process/exposure findings remain; no clean-cognition/noninfluence certificate is asserted. This new source needs full source/dependency review, independent symbolic checking and parent disposition before scientific adoption.

No Git/push, deletion, publication, secret access, unsolicited external model/paid API or infrastructure mutation. Same18/exclusive new root; research deadline2026-10-31T21:23:27Z. Exact executable evidence is described only where actually exercised; no human/formal/kernel/configured-family/novelty acceptance is implied.

**END — explicit ACTUAL PH7 upper construction on the full rational band; exact-order conclusion conditional on the named unrestricted PH6 lower.**
