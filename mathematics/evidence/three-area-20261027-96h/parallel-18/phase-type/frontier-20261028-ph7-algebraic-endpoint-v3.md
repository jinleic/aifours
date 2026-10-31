# A closed algebraic PH7 band beyond 41/50

**MathResearch96h-2 / math-1. NEW CONSTRUCTIVE CANDIDATE; exact symbolic/rational checks executed, independent review and novelty clearance pending.** Actual native observation before writing: **Wed Oct28 17:25:19 PDT2026**. Additive successor to `frontier-20261028-ph7-explicit-band-41over50-v2.md`, SHA256 `8e9d10653ef1c930a07bf8a6ee06ae6e99f61194eccb2edaeeac4f51c4ffde91`; no previous frozen file is changed.

## 1. The exact new endpoint and claimed result

Let z_star be the UNIQUE real root of

    g(z)=6000000000000000000 z^3
         +1102901000000000000 z^2
         -5748481270830000000 z
         +660610321325765899                              (g)

in the EXACT rational interval

    820409/1000000 < z_star < 82041/100000.                (I)

Here `820409/1000000 > 41/50`, while `82041/100000 < 8/9`. These inequalities only locate the explicitly defined algebraic root; no floating root or maximality assertion is used.

For EVERY c,d>0 and EVERY real `z in [7/9,z_star]`, the explicit SAME-matrix construction below is an actual seven-state PH realization of

    H(s)=c(a^2+b^2)^2 / [(s+c)((s+a)^2+b^2)^2],
    a=c+d,   b=d sqrt(z).

The upper endpoint is INCLUDED: one off-diagonal feedback coefficient phi vanishes there, while every other required physical coefficient remains strictly positive and the normalizer remains strictly positive. The construction does NOT claim that z_star is the endpoint for all PH7 topologies, or even the optimum across all six-rate chains. It is not the unrelated earlier endpoint also called z_star; this source's root is fixed unambiguously by(g),(I).

With the named prior topology-unrestricted PH6 lower (z>1/2), this gives exact minimum7 on `[7/9,z_star]`. Combining with the named earlier direct seven-band parent, which extends beyond7/9, gives exact7 on `[13/20,z_star]` at those explicit prior boundaries. All exact-order statements are conditional on the separately written-supported old lower/overlap inputs and independent review of this source; the new actual upper construction is self-contained apart from ordinary finite algebra.

## 2. Literal matrix family and common coefficient formulas

Normalize d=1, set y=s+c, c>0, and fix the six positive rational raw rates

    u1=669/500, u2=1339/1000, u3=671/500,
    v1=669/500, v2=1043/1000, v3=1041/1000.

Let e_j denote the jth elementary symmetric polynomial of THESE SAME six rates. Put

    A=e1, B2=e2, C3=e3,
    H0=B2+4A-A^2-6,
    L=B2-4A+10-2z,
    N=4H0+4-C3-B2(4-A)-4z,
    p=N/L, q=(A-4)p+H0-2z, w=p+4-A,
    B=p-u1-u2, C=q-u1u2-u1 B,
    Q(y)=y^2+p y+q
        =(y+u1)(y+u2)+B(y+u1)+C.

Define the actual feedback coefficients

    phi=e4+C3 w-[(6+2z)q+(4+4z)p+(1+z)^2],
    R2=e5+e4 w-(4+4z)q-(1+z)^2 p,
    R1=e6+e5 w-(1+z)^2 q,     R0=e6 w,
    D1=R2-phi(u1+u2+u3),
    D2=R1-phi(u1u2+u1u3+u2u3)-(v2+v3)D1,
    D3=R0-phi u1u2u3-v2v3 D1-v3 D2.

All are rational functions of z with common denominator L. Put

    G = [ -u1  1    0    0    0    0    0
           0  -u2   1    0    0    0    0
           0   0   -u3   1    0    0    0
           0   0    0   -w    1    0    0
           D1  0    0    0   -v1   1    0
           D2  0    0    0    0   -v2   1
           D3  0    0   phi   0    0   -v3 ],
    beta=(C,B,1,0,0,0,0),
    D_z(y)=y[(y+1)^2+z]^2,
    K=D_z(c),     gamma=K e7.

For this exact SAME matrix, symbolic coefficient comparison gives

    det(yI-G)=D_z(y)Q(y),
    beta adj(yI-G)e7=Q(y).                              (ID)

Both identities are checked over rational functions of z in §6. The second is verified independently through `det(yI-G+e7 beta)-det(yI-G)`. These identities are polynomial in y after clearing L and remain valid at repeated/coincident hidden roots; no inverse at a root is used.

## 3. Exact endpoint existence, uniqueness and all signs

Direct algebra gives the particularly simple exact relation

    L(z) phi(z)=-g(z)/10^18.                            (F)

Its derivative has the following degree-2 Bernstein coefficients on the ENTIRE interval `[7/9,82041/100000]`:

    -2056809418751/300000000000,
    -3374955732361/450000000000,
    -817648697379/100000000000.

All are strictly negative, so `L phi` is strictly decreasing there. At the two rational endpoints of(I), exact evaluation gives

    (L phi)(820409/1000000)=521568424227/125000000000000000 > 0,
    (L phi)(82041/100000)=-4003923709699/1000000000000000000 < 0.

The intermediate value theorem and strict decrease prove existence and uniqueness of z_star in(I), and

    phi(z)>0 for 7/9<=z<z_star,
    phi(z_star)=0.

Division by L is justified by the next table.

On the ENTIRE larger rational interval `[7/9,82041/100000]`, all Bernstein coefficients of L and of each L-scaled OTHER physical coefficient are positive. The exact smallest coefficients are:

|Polynomial|degree|smallest exact Bernstein coefficient|
|---|---:|---:|
|L|1|`1606469/1000000`|
|L p|1|`3837854807/500000000`|
|L q|2|`398112206694083/40500000000000`|
|L w|1|`3644970697/1800000000`|
|L B|1|`29857212649/9000000000`|
|L C|2|`19118264445187/8100000000000`|
|L D1|3|`301828646415859008085787/81000000000000000000000`|
|L D2|4|`13235747258488798197/50000000000000000000000`|
|L D3|4|`963209484610026707374851401641/437400000000000000000000000000`|

All lists are fully reproduced in the pinned certificate JSON. Since Bernstein basis functions are nonnegative and sum to1, every listed coefficient is strictly positive on the WHOLE interval, not just sampled endpoints. Thus on `[7/9,z_star]`:

    L,p,q,w,B,C,D1,D2,D3>0,       phi>=0.

The simultaneous correlated parameters, endpoint zero and all actual matrix ties are retained.

## 4. Explicit all-c physical normalizer and target transfer

Let `Q_c=c^2+p c+q>0`, and define

    h1=1/Q_c,
    h2=(c+u1)h1,
    h3=(c+u2)h2,
    h4=(c+u3)h3,
    h7=[K+D3 h1+phi h4]/(c+v3),
    h6=[h7+D2 h1]/(c+v2),
    h5=[h6+D1 h1]/(c+v1).

All seven entries remain strictly positive even when phi=0 at z_star: K>0 and D3 h1>0. The six noncenter rows of `(cI-G)h=K e7` follow directly. The center row is the polynomial(ID) at y=c with actual recurrence substituted; the exact verifier also checks all seven rows directly as symbolic rational identities in c,z. The identity for Q gives `beta h=1`.

Let Delta=diag(h) and put

    T=Delta^(-1)(G-cI)Delta,
    alpha=beta Delta,
    omega=Delta^(-1)K e7.

Every off-diagonal G entry is nonnegative, alpha is a nonnegative probability row and omega>=0. The actual row identity gives `-T1=omega`. From(ID), the eigenvalues of G are0, `-1±i sqrt(z)` each twice and the roots of Q. Since p,q>0, the hidden roots have negative real parts. Therefore G-cI, and its positive diagonal similarity T, are Hurwitz for EVERY c>0. The SAME input/output and(ID) give

    alpha(sI-T)^(-1)omega=K/D_z(s+c)

with no separate spectral or sign assumption. The construction remains valid at zero phi and any root coincidence.

For general d>0, use the construction at `c/d`, then multiply T and omega by d, leaving alpha unchanged. This is the exact original-dimensional PH pair for every c,d>0 and every z in the stated closed band.

## 5. Verification actually exercised

Completed exact check:

    python3 frontier-20261028-ph7-algebraic-endpoint-check.py
    SymPy 1.14.0 Fraction exact identities/signs/unique-root assertions PASS

It verifies over exact rationals:

- the FULL actual7-by7 determinant and actual adjugate numerator, symbolically in y,z;
- all seven normalizer equations and beta h=1, symbolically in c,z;
- every Bernstein coefficient in §3 for L and all eight non-phi L-scaled entries on the larger rational interval;
- all three strictly negative Bernstein coefficients of `(L phi)'`;
- the exact opposite rational signs in(I).

Checker `frontier-20261028-ph7-algebraic-endpoint-check.py`: **66LF/3743B**, SHA256 `f825b2bea32faf4ca13bb4e902b08d1935d0fc4c294755600911d78186e00e6a`.

Certificate `frontier-20261028-ph7-algebraic-endpoint-certificate.json`: **83LF/2580B**, SHA256 `4ec6738b0825b99b0899917f264009fb9ee96d8720bb1646cd9d88f7813c3cb0`.

These are exact executable algebra checks, not Lean/kernel or an independent-family/human review. The root is defined by exact signs and monotonicity, not a numeric optimizer. The previous independent Fraction actual-matrix witnesses and earlier `[7/9,41/50]` certificate remain preserved at their own cuts; none is substituted for the present all-z identities.

## 6. Exact old inputs, original gap and trust boundaries

The old unrestricted PH6 lower source is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, whose written-supported `z>1/2` exclusion is a named earlier input, not re-proved by the present upper construction. The earlier direct exact-order7 band `[13/20,z_old]`, with `z_old>7/9`, is reported at the explicit parent `PH7-entire-rational-seven-ninths-band-parent-v1.md`. Both old inputs retain their actual ordinary-written/trust limits and any prior process qualifications; no entire old DAG or priority claim is silently reverified.

Consequently the supported-input composition would be exact order7 throughout `[13/20,z_star]`. This z_star is explicitly greater than41/50, strengthening the v2 construction. It is NOT proved globally maximal, and no upper construction or exclusion at `z=8/9` follows. The original full H_(1,2) minimum-order function and all-topology seven-versus-eight gap remain open. A different family might extend farther.

The all-u obstruction for the old equal-rate-per-chain chart is a separate current candidate, not a general PH7 lower bound. Numeric searches outside this successful fixed-rational-rate family are merely proposal/failure observations; they cannot be used as impossibility evidence.

Earlier quarantined outputs remain historical/unvalidated and were not accepted as premises. No prior finding is erased. Same18/exclusive owner root, no deletion/Git push/publication/secrets/unsolicited external-model campaign or infrastructure mutation; original research deadline2026-10-31T21:23:27Z. Full independent source/matrix/sign/normalization/dependency review and parent disposition remain required before adoption; no human/formal/kernel/priority/novelty acceptance is claimed.

**END — actual PH7 family on [7/9,z_star] with explicit unique algebraic root and endpoint included; no 8/9 decision.**
