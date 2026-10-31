# The adopted v4 endpoint is a strict local all-topology spectral maximum

**New WRITTEN computer-assisted theorem candidate, independent review pending.** It uses the new joint interlacing lemma and a rational interval dual certificate, not a parameter variant of the frozen f180 packet. No frozen file is changed. MathResearch96h-2 / math-1. Native clock observed before writing: **Thu Oct 29 09:25:43 PDT 2026**. Exact owner computations are not formal/kernel, independent-family, human or novelty verification.

## 1. Statement and precise locality

Import the adopted f50 algebraic endpoint `(U,V,z_*)`, defined as the unique root of the three displayed polynomial equations in the radius-10^-7 box centered at `(1338787907,1042029691,820420441)/10^9`. In particular V<U, and `820420341/10^9<z_*<820420541/10^9`.

Let `rho=delta=1/10^6`, `v_*=(V,V,U,U,U,U,U)`. Consider an irreducible 7-by-7 Metzler matrix G with spectral bound zero and

    det(yI-G)=y((y+1)^2+z)^2(y^2+py+q),   z in [z_*, z_*+delta].

Let S be its geometric symmetrization, `𝒜=-S`, and `v1<=...<=v7` the positive eigenvalues of 𝒜. Suppose

    |v_i-V|<=rho  (i=1,2),    |v_i-U|<=rho  (i=3,...,7).             (N)

**Theorem.** Necessarily `z=z_*` and `v=v_*`. Thus no such matrix, and therefore no PH<=7 representation with normalized geometric-symmetrization spectrum in (N), exists at `z_*<z<=z_*+10^-6`.

The locality restriction (N) is essential. This does NOT exclude spectra outside (N), prove the global PH7 supremum is z_*, identify a unique topology, or construct a ratio above z_*. At z=z_* the adopted v4 matrix attains this spectrum, so the local maximum is attained.

## 2. Imports and notation

- f50 root/construction: source `frontier-20261028-ph7-two-cycle-endpoint-v4.md` SHA256 `4f63347198b12ce6dfefb5c7c94adf95fcc262234d29ce055e6f789bff27e191`, mandatory earlier-read erratum `b5526a1556a61786c5cc382e924087a318b31b6640b35d30a41fe9d3fe22cc30`, root certificate `2e1aa9b765098d707d8803c82ccf756df5b696bdcc34616bea35dcc533c95f88`; same-harness parent disposition `math-1-ph7-algebraic-endpoint-closed-band-parent-v1.md`. Root existence is imported, not re-proved by this checker.
- Adopted geometric-symmetrization cover identity, positivity of 𝒜, and coefficient/interlacing relations (f159/f160). For the PH application only, the adopted irreducibility caller is an additional dependency.
- New joint interlacing lemma `frontier-20261029-ph7-joint-interlacing-y1-v1.md`, 90 LF, SHA256 `0221e6c73440f921f127db0130038f8ab733fae65d5585f4227ba06b9fef8310`, is a candidate dependency. It strengthens the four-cycle coefficient bound by treating e2 and trace of the SAME principal submatrix jointly; it is not claimed adopted.

Use elementary sums e_k of v and

    p=e1-4, q=e2-4e1+10-2z,
    W=e3-4e2+(10-2z)e1+12z-20,
    E3=e4-(6+2z)e2+(20+4z)e1+3z^2+6z-45,
    E2=e5-(1+z)^2*p-(4+4z)*q, E1=e6-(1+z)^2*q,
    s=v1+v2, S4=v1+v2+v3+v4, K=E3-S4*W,
    Z=E1-s*E2,
    alpha=e3(v1,v2,v3,v4)-s*e2(v4,v5,v6,v7),
    B_joint=v1*v2-s^2.

The imported coefficient relations give `W>=0`, `K>=0`. The joint lemma gives

    Y_joint=Z-W*alpha-K*B_joint+W^2/2>=0.                            (J)

## 3. Algebraic dual constants and stationarity

For grouped variables u,v,z, evaluate W,E3,Z at the spectrum `(v,v,u,u,u,u,u)`; denote the resulting polynomials by Wg, Eg, Zg. At the algebraic root `(U,V,z_*)`, choose constants a,b by

    [ partial_u Wg  partial_u Eg ] [a] = -[partial_u Zg],
    [ partial_v Wg  partial_v Eg ] [b]    [partial_v Zg].             (D)

The checker encloses this two-by-two determinant away from zero on the full root box, so a,b are well-defined real algebraic constants. They are treated as CONSTANTS when differentiating the dual in v and z.

Define

    F(v,z)=Z(v,z)+a*W(v,z)+b*E3(v,z)-E3(v,z)^2.                    (F)

At `(v_*,z_*)`, the root equations imply W=E3=Z=0, so F=0. The first seven partial derivatives vanish EXACTLY: F is symmetric within the first two variables and within the last five; its two grouped derivatives are zero by (D), and the derivative of `-E3^2` vanishes because E3=0. Thus `grad_v F(v_*,z_*)=0`. This is an algebraic argument, not a small floating residual.

## 4. Positivity comparison and strict local maximum

A direct identity, using `E3=K+S4*W`, is

    F = Y_joint + lambda*W + mu*K,
    lambda=a+alpha+b*S4-W/2-S4*E3,    mu=b+B_joint-E3.               (C)

The exact interval certificate proves on a rational box containing ALL of (N) and `z in [z_*,z_*+delta]`:

    3576/1000 < lambda < 3605/1000,
    3610/1000 < mu < 3615/1000,
    -20834/1000 < partial_z F < -20667/1000,
    Hessian_v F is strictly negative definite.                    (I)

The displayed coarse inequalities are conservative rational enclosures of the certificate's full exact bounds. Hence any feasible G satisfies `F>=0` by (J), (C), W>=0 and K>=0.

For a fixed v in (N), strict concavity in v at z=z_* and the exact stationary value give `F(v,z_*)<=0`, with equality only when v=v_* (Taylor's integral remainder along the segment to v_*). Because `partial_z F<0`, every z>z_* in the stated interval satisfies `F(v,z)<F(v,z_*)<=0`, contradiction. At z=z_*, feasibility forces equality, hence v=v_*. This proves the theorem.

## 5. Exact certificate mechanism and actual run

Checker `frontier-20261029-ph7-v4-local-spectral-optimality-check.py`, **190LF/9123B**, SHA256 `6eed9b486726dcb79a8ad8d57c4106aa312c354df7cc7989c5887dd7a121813b`:

1. Standard-library Fraction interval arithmetic, including a second-order automatic differentiation implementation; elementary symmetric functions built by the usual descending-degree recurrence.
2. Bounds a,b by the explicit two-by-two Cramer formulas over the imported root box; e.g. `-13356/1000<a<-13349/1000`, `6868/1000<b<6872/1000`.
3. Uses interval variables for the seven spectral coordinates and z and interval constants for a,b. The rational superset has the first two coordinates centered at V0 with radius `10^-7+rho`, the next five at U0 with the same radius, z in `[z0-10^-7,z0+10^-7+delta]`. It does not assume the unknown algebraic root equals its rational center.
4. Computes the exact rational central matrix `B0=-Hessian_v F` at the rational center and point values of a,b, its positive unit-LDL factorization, and `R=L^{-T}`. It checks `R^T B0 R=diag(d)` exactly. Then interval arithmetic bounds `R^T(-Hessian_v F)R`; every diagonal lower bound exceeds the sum of the other absolute upper bounds. The minimum dominance margin is greater than `6745/1000`, proving positive definiteness throughout the rational box by strict diagonal dominance and congruence.

Actual successful invocation (before changing only the default radius literals to the same successful values and correcting a docstring space):

    python3 frontier-20261029-ph7-v4-local-spectral-optimality-check.py 1/1000000 1/1000000
    PASS exact local dual: rho= 1/1000000 delta_z= 1/1000000
    lambda>0, mu>0, F_z<0, uniform negative v-Hessian (rational LDL congruence)

Certificate `frontier-20261029-ph7-v4-local-spectral-optimality-certificate-v1.json`, **161LF/32064B**, SHA256 `d2d1b3e0a1e83059ff8416eaac19ff281a56999bd07fe7e1979f0809b1d5407f`, stores full exact endpoint intervals, positive LDL pivots, rational congruence matrix and all seven dominance margins. It refuses overwrite. The checker checks the pinned root-certificate hash before using its documented root box. It does not replay root existence and is not an independent review of the joint lemma.

Separately in the retained owner kernel, exact SymPy expansion verified identity (C) and both grouped stationarity Cramer identities. An independently differentiated full symbolic seven-variable Hessian at the rational center matched the certificate's rational `R^T(-H)R=diag(d)` exactly. This cross-check validates the central AD Hessian, not the uniform interval enclosure or the imported root existence.

Process transparency: an earlier attempt at rho=delta=10^-4 failed its interval diagonal-dominance assertion; no result was promoted from that attempt. The final neighborhood is 10^-6. Narrowing it changes the actual theorem locality, explicitly stated in Section 1; no global claim is inferred from the local numerical optimizer. The exact intervals above were rounded OUTWARD using Fraction integer floor/ceiling only.

## 6. Remaining mathematical gap

This establishes a topology-unrestricted LOCAL spectral obstruction near the adopted attaining endpoint. The remaining original supremum question is GLOBAL: exclude distant symmetrized spectra for ratios just above z_*, or construct a genuinely better PH7 realization. No complement cover or global supremum equality is delivered by this packet. Frozen f180 sources and the parked 0.825 variant are unchanged.

END — a strict local all-topology spectral maximum at the adopted v4 endpoint; no global-optimality claim.
