# A paid common-controller finite/infinite synthesis interchange under weak compactness

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:36:26 PDT 2026**. Admitted structural/convexity/horizon work, not the stopped diffusion-annihilating-controller route. No new source, program, chosen state/probe or controller realization. The compactness hypothesis below is EXPLICITLY NOT established for the unrestricted original design class.

## 1. All matrices, same actual law and the missing premise

Fix all compatible real original matrices, positive dimensions, h>=0, zero state/history, canonical progressive E2 inputs and ONE feedback K. The design variable is the bound deterministic stationary feedforward triple R=(L0,Lh,H), H in L2([0,h]); at h=0 use the combined tap without a kernel.

Let H_design be the real Hilbert space of these matrix/kernel coefficients, with finite-matrix Frobenius inner products and the kernel L2 inner product. Choose a NONEMPTY WEAKLY COMPACT subset C of this space. For example, a norm-closed bounded convex coefficient/kernel set has that property by ordinary Hilbert weak compactness. The full unrestricted design space is not assumed to have it.

For each b>h, g_b(R) is the ACTUAL finite-horizon literal progressive gain. The infinite g_infinity(R) uses the explicitly local-square-integrable-control comparison interpretation and same-law physical caller of `causal-padded-horizon-literal-gain-identity-v1.md`, SHA `ed6817c1c00e81549e75e31e68c524ad22ea8ac6cdd087a734399dd9982ad72d` (UNREVIEWED). Extra original infinite-horizon control-energy/stability eligibility is not inferred and must be separately verified if required.

**Theorem.**

1. For any s>=0, `for EVERY b>h there EXISTS R_b in C with g_b(R_b)<=s` iff `there EXISTS ONE R_* in C with g_infinity(R_*)<=s`.
2. In the extended reals,

   **min_(R in C) g_infinity(R) = sup_(b>h) min_(R in C) g_b(R).** (V)

   When that value is finite, an actual parameter R_* attaining it exists in the same original-information law class.
3. Infinite uniform-strict synthesis at gamma>0 is equivalent to existence of a COMMON kappa<gamma such that every finite b has an R_b in C with g_b(R_b)<=kappa. Merely g_b(R_b)<gamma separately for each b does not pay that common-margin premise.

No minimax/controller quantifier is interchanged without the explicitly proved weak closure/compactness and the actual-law caller below. The theorem is conditional on a design-set property, not a general original N&S condition or a numerical synthesis method.

## 2. Actual finite-horizon parameter map is affine and E2-continuous

Fix ANY finite b and one original admitted progressive E2 input w on [0,b-h]. At fixed K the original closed-loop homogeneous matrices P=A+BK, Q=A0+B0K and output N=D0+D1K do not depend on R. The forcing BRw/B0Rw and direct D1Rw depend linearly on R, with physical Cw(t-h) unchanged. Strong linear-SDE uniqueness/linearity therefore makes R->Z_R(w) an affine actual-output map.

For a parameter difference Delta R, the deterministic preview bound gives

`||Delta R w||_E2[0,b] <= c_h ||Delta R||_H_design ||w||_E2[0,b-h]`,

where finite c_h follows by Cauchy-Schwarz from the two matrix taps and the L2 kernel (and c_0=1 with the combined-tap convention). The allowed linear-SDE/isometry estimate with fixed P,Q then bounds the actual output difference in the Hilbert space Y_b=L2(Omega x [0,b];R^q) by a finite constant times ||Delta R||_H_design. Thus the map is affine, bounded and weakly continuous between these two Hilbert spaces for this fixed actual input.

This conclusion uses only per-input E2 estimates, not the pending NR-GAIN theorem that a global literal operator bound exists. No deterministic-input average is promoted to an adapted input; w was an arbitrary actual progressive input throughout.

## 3. Weak lower semicontinuity is paid in the right topology

The functional J(Z)=E||Z||_[0,b] is convex and continuous in the Y_b Hilbert norm: `|J(Z)-J(Z')|<=E||Z-Z'||<=||Z-Z'||_Y_b`. Its norm-sublevel sets are therefore norm-closed convex subsets of a Hilbert space, hence weakly closed.

The precise ordinary Hilbert fact used here can be proved by nearest-point projection: if a point lies outside a closed convex subset, its displacement from the nearest point strictly separates it by a continuous linear inner product; those inner products are weakly continuous. Thus the set is weakly closed. No mixed-norm dual/adjoint/risk representation is imported.

Combining that fact with the actual affine weakly continuous output map shows, for every fixed nonzero w, that

`R -> E||Z_R(w)|| / E||w||`

is weakly lower semicontinuous. The full gain g_b is the supremum over ALL those original progressive inputs, so its sublevel set is an intersection of weakly closed sets. Hence g_b is weakly lower semicontinuous, even when extended-valued. In particular it attains its minimum on the nonempty weakly compact set C; if all values are infinity that is only an extended-value statement, not a useful finite controller.

## 4. Nested finite feasibility sets have one actual common law

For a fixed R, g_b is nondecreasing in b. Indeed embed any shorter-window input into a longer finite problem by zero extension; the actual response prefix is unchanged by causality/uniqueness, the full output norm can only increase and the denominator is identical. The input/domain/window difference is paid explicitly, not inferred from a limit of laws.

Choose any cofinal sequence b_n>h increasing to infinity. If every finite problem admits g_b<=s on C, select R_n in C feasible at b_n. By weak compactness (the design Hilbert space is separable), pass to a weakly convergent subsequence with limit R_* in C. For any fixed m, all sufficiently late n satisfy

`g_(b_m)(R_n)<=g_(b_n)(R_n)<=s`.

Weak lower semicontinuity gives g_(b_m)(R_*)<=s. The same law is therefore feasible on every b_m and, by horizon monotonicity, every finite b. The paid actual padded-horizon identity gives g_infinity(R_*)<=s. Conversely any one infinite law with that bound is feasible at every finite horizon by zero extension.

The weak-limit parameter is a real matrix/kernel triple in C, hence defines ONE deterministic stationary original-information controller. Its actual strong solution at each finite horizon is the same uniquely defined affine parameter caller of section 2; the infinite response is the consistent local strong solution. No virtual states, randomized policy selection or input-dependent controller has been substituted. This is the forward/converse actual-object synthesis caller.

## 5. Value identity, attainment and strictness

Put a_n=min_C g_(b_n), a=sup_n a_n. The minima exist as above and a_n is nondecreasing. The elementary weak inequality gives `inf_C g_infinity>=a`. If a is finite, the preceding argument with s=a supplies one R_* with g_infinity(R_*)<=a, proving equality and attainment. If a=infinity, every fixed R has g_infinity(R)>=a_n for every n, hence g_infinity(R)=infinity; no finite controller is inferred. This proves (V) in every extended-value case.

For strict gamma, an actual infinite gain below gamma supplies a single kappa<gamma bounding its gain on every finite horizon. Conversely a common kappa with the finite-controller existence property supplies one common infinite law by section 4. This proves item 3 without exchanging a horizon-dependent strict margin for a uniform one.

The current exact nonzero scalar two-tap family makes that distinction real even with C a SINGLETON (therefore weakly compact): every finite-horizon gain is strictly below gamma=M=|j0|+|jh|, but their supremum and the infinite gain equal M. Infinite uniform strictness fails. This current author-only physical example is not a claim that some other law is impossible. No generic pointwise-strict horizon interchange is asserted.

## 6. Exact missing premise for the unrestricted original problem

The theorem does not prove that finite-horizon feasible designs have a uniform coefficient/kernel norm bound or any weakly compact admissible selection. It does not restrict the unrestricted original class silently to C. Without that premise, controllers may escape every such set and the common-law argument has no justified limit. If K is allowed to vary arbitrarily, actual-output affinity/weak closure also needs separate proof; the theorem fixes K rather than borrowing the invalid joint-control-affinity extension.

If an infinite admissibility convention requires global expected-control energy, internal EMS or another nonlocal property, that law eligibility/closure must be part of the admitted design set and separately paid; local strong well-posedness alone does not establish it. The original book's unformalized technical conventions and the general nonlinear/controller-domain bridge remain unresolved.

Named ordinary facts and uses: allowed finite-horizon linear-SDE uniqueness/linearity/isometry bounds, the explicit bounded preview formula, ordinary Hilbert projection/weak compactness, weak continuity of bounded linear maps, and the previously reconstructed causal padded-horizon identity. No new source, mixed-norm dual guide, Riccati/storage/Gramian, excluded realization or direct diffusion-annihilating controller route is used. No scientific program/CAS/enumeration, selected state/control probe, external model/nested agent or stronger verification occurs. All old STOP/HOLD/ZERO/process findings, N4 UNKNOWN and aux214 STOP persist; written only, with no peer/parent, formal/kernel, executable, human/configured-family or novelty acceptance.
