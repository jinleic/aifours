# The entire PH7 feasibility set is closed above 1/2: an exact 8/9 endpoint dichotomy

**NEW WRITTEN CANDIDATE; not independently reviewed or parent-adopted.** MathResearch96h-2, original math-1. This extends the prospective global spectral compactness proof `frontier-20261028-ph7-global-spectral-compactness-v1.md` SHA256 `e1b9ec89f5e5f9770a2ca3b1b9ed88c3eb633102e0c94d125fc53de5d8c4b4db`. The latter's singular-resolvent proof is an essential named dependency and requires full independent review. The earlier 6-state lower is not claimed as new. No 8/9 existence or exclusion is decided here.

## 1. Main consequence for the original target

Fix any finite closed interval `[L,U]` with `1/2<L<=U`. Let Z7(L,U) be the set of z in that interval for which the ORIGINAL H has an actual PH representation with at most seven transient states, for one (equivalently, every) pair c,d>0 with `a=c+d` and `b^2=z d^2`.

**Claim.** Z7(L,U) is a compact subset of `[L,U]`. More precisely, after a canonical positive-Perron normalization and a harmless scalar gauge, all actual seven-state generator/input/exit data lie in an exact closed, bounded semialgebraic fiber described in §3.

Taking `L=7/9`, `U=8/9`, the independently checked earlier PH7 construction supplies nonemptiness. Therefore EXACTLY ONE of the following holds:

1. There is an actual PH7 realization at z=8/9; or
2. There is an epsilon>0 such that NO PH realization with at most seven states exists for any z in `(8/9-epsilon,8/9]`.

Equivalently, a sequence of actual PH7 realizations with z approaching8/9 from below would FORCE an actual endpoint realization; an unbounded-rate or disappearing-input/exit escape is impossible after normalization. This is an exact topological dichotomy, NOT a decision between its two branches. It proves no particular epsilon, no actual endpoint matrix, no minimum8, and no monotonicity of Z7.

## 2. Normalize any actual PH representation to a row generator

Let `tau=c/d>0` and `y=(s+c)/d`. The normalized target has the form

    H(s)=K_tau(z)/D_z(y),
    K_tau(z)=tau[((tau+1)^2+z)]^2,
    D_z(y)=y[(y+1)^2+z]^2.                         (TARGET)

For z>1/2, the independently supported SCC/PH structural argument says every representation using <=7 states in fact uses7, is reachable and has irreducible T. The positive Perron argument in that proof puts the spectral bound of `A=(T+cI)/d` at0. Let v>0 be its Perron right vector, V=diag(v), and define

    G=V^(-1) A V,      beta=alpha V,
    gamma=V^(-1) omega/d.

Then G is an irreducible row generator and

    beta (yI-G)^(-1) gamma = K_tau(z)/D_z(y).      (RAW)

Multiplying v by any positive scalar multiplies beta by that scalar and divides gamma by it; G and the raw transfer do not change. Since beta is nonzero and nonnegative, choose this gauge so that

    beta>=0,     beta 1=1,     gamma>=0.            (GAUGE)

The actual transfer poles force `det(yI-G)=D_z(y)Q(y)` with Q a real monic quadratic; there is no need to assume Q has distinct, real, or noncoincident roots. Comparing actual numerator polynomials yields

    beta adj(yI-G) gamma = K_tau(z) Q(y).           (NUM)

This is an identity for the SAME matrix, not a separately chosen numerator.

## 3. The compact explicit semialgebraic fiber

The preceding global spectral compactness candidate gives a compact set S(L,U) of all `(G,z)` satisfying the row-generator conditions and the actual characteristic divisibility. It also proves every member irreducible. For fixed tau>0 define F_tau(L,U) as all quadruples `(G,z,beta,gamma)` such that

* `(G,z) in S(L,U)`;
* `(GAUGE)` holds; and
* all coefficients of the polynomial identity(NUM) hold, with Q the unique monic quadratic obtained by division of the actual characteristic polynomial by D_z.

This is a closed semialgebraic set: characteristic divisibility is the explicit four polynomial residual system of the first-order source, Q's coefficients are determined polynomially by the leading characteristic coefficients and z, and(NUM) gives finitely many polynomial equalities. The beta simplex is compact. We now prove gamma is uniformly bounded and cannot disappear.

For each G in the compact S(L,U), set `R_tau(G)=(tau I-G)^(-1)`. It is entrywise STRICTLY positive because G is irreducible and its nonnegative semigroup is strictly positive for t>0. It varies continuously with G, and its row sums are `1/tau`. Hence there is an m>0, depending only on L,U,tau, with

    m <= [R_tau(G)]_ij <= 1/tau   for all G in S and all i,j.  (RESBOUND)

(The assertion is vacuous if S is empty.) Evaluating(RAW), or equivalently(NUM), at y=tau gives `beta R_tau(G) gamma=1`, because `K_tau(z)=D_z(tau)`. With beta1=1 and gamma>=0, (RESBOUND) implies

    tau <= sum_j gamma_j <= 1/m.                    (GAMMA-BOUND)

Thus F_tau(L,U) is closed and bounded, hence compact. Define `h=R_tau(G)gamma`. It obeys the uniform positive two-sided bound

    tau m <= h_i <= 1/(tau m).                      (H-BOUND)

No zero or infinite normalizer can arise at a limit.

## 4. Every fiber point is an actual PH realization

Conversely take any point of F_tau. Since G is irreducible and gamma>=0 is nonzero by(GAMMA-BOUND), h is strictly positive. Put `H=diag(h)` and

    T0=H^(-1)(G-tau I)H,
    alpha=beta H,
    omega0=H^(-1) gamma.

Because `(tau I-G)h=gamma`, we have `-T0 1=omega0>=0`; T0 is Metzler and Hurwitz, since G has spectral bound0 and tau>0. Also `alpha>=0` and `alpha1=beta h=1`. The actual transfer is(RAW), by(NUM). Finally multiply T0 and omega0 by any chosen d>0 to recover the original H with c=tau d. Thus the fiber is an exact equivalence, not just a necessary parameterization.

The argument also proves independence from tau: given any RAW transfer at tau0, multiply gamma by `K_tau(z)/K_tau0(z)` and reconstruct the above positive h at any new tau>0. The same G and z then yield an actual PH realization for that tau. The beta simplex gauge remains valid. Thus the phrase 'one or every c,d' in §1 is justified without a hidden assumption of scale invariance of the probability normalization.

## 5. Compact projection, endpoint and gap

The coordinate projection of the compact F_tau(L,U) onto z is compact, and §2–§4 identify it exactly with Z7(L,U). If a sequence `z_n in Z7` converges to a point z_c in `[L,U]`, compactness supplies a convergent subsequence of the full `(G,beta,gamma)` data; the polynomial numerator and characteristic identities survive the limit, while(H-BOUND) makes the limiting PH normalization actual. Therefore z_c itself belongs to Z7.

If 8/9 is not in the compact set, its distance to the set is strictly positive (or the set is empty), yielding the stated exclusion strip below8/9. This does not prove an exclusion strip exists: the first branch may hold. The earlier endpoint z_* is only a local spectral maximum; no inference that it is the global maximum is made.

## 6. Review boundaries

The proof depends on prospective spectral compactness, the existing SCC/Perron proof, positive irreducible Metzler resolvents, polynomial adjugates, and finite-dimensional compactness. A reviewer must reconstruct both directions of the row-generator gauge, strict and UNIFORM resolvent positivity, all-normalizer bounds, the equivalence(NUM), the tau change, and compact projection. No optimizer output, public-source characterization theorem, old held body, Lean proof or novelty clearance is a premise. No actual decision at8/9, explicit epsilon, rate bound or optimal PH order is claimed. Historic process qualifications remain.

END — either a genuine 7-state endpoint exists at8/9, or a positive-width PH<=7 exclusion strip lies below it; both branches remain open.
