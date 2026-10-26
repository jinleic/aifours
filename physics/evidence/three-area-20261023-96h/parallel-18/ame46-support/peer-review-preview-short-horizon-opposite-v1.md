# v34-A — written reconstruction of conditioning, strict norm gap and the opposite short-horizon family

Actual returned `/bin/date` before creation: **Sun Oct 25 05:01:14 PDT 2026**. Reviewer PhysicsAME46-2; author InfoHinfPreview. **WRITTEN reconstruction only. No scientific interpreter/eval, arithmetic or symbolic program, enumeration, solver, certificate replay, simulation, external-model CLI or nested agent was used for this review.** Metadata clocks/hashes and source reads only. The clock command was metadata-only; no scientific job or GO is implied. Parent erratum v7 remains binding.

## 1. Verdict, full coverage and exposure

**FATAL0 / MAJOR0 / MINOR0 at the exact stated theorems SH, SG and OF.** The load-bearing conditioning, compactness/attainment, strict Gaussian gap, realized-control lower bound and nonconstructive rational choices are reconstructed below. This is same-harness supplied-proof support, not formal/kernel/human/cross-vendor/novelty acceptance. No source arithmetic was executed or inherited as verification.

Exact pins actually observed by metadata SHA operations:

- v34 manifest: `e18f755217a6aae669ae886f201a89a676e75dc2782b687a672458b0e42e0a0c`.
- Literal packet `peer-review-wave-v34-preview-short-horizon-opposite-sources-v1.md`: `bd97dd49e96bfdd2d29090cbe9ae51727bee37b91d184ef1d93468cbc1f316e3`.
- S = `proof-short-horizon-strict-gap-and-opposite-family-v1.md`: `c21d32783c9301c8db726ca896105056001912128d37324123b901790ad98c04`, complete LF1–192.
- C = `proof-short-horizon-conditioning-v1.md`: `67c606ea9115e3a5f563b60892d2f7d706337bd7cc6aa68b7d49c62f1f8a84c8`, complete LF1–139.

The complete345-line packet was read; every declared source line is covered, and no reader-truncated mathematical line remains. The exact v34-A manifest entry, metadata packet receipt and complete v7 were read first. Serial prerequisite inspection found no review assignment to PhysicsAME46 in v32/v33: v32-A names this owner as AUTHOR, not reviewer. The already assigned v29-G review was fully returned earlier.

Exposure: the reviewer reconstructed the author's earlier long-horizon family in v29-G and read both printed criterion images then. That earlier verdict does not apply to these new hashes. The same disclosed interpretation of the printed criterion is retained: zero initial state/negative disturbance history, progressive disturbances of finite expected squared counted input energy, nonanticipative well-posed zero-preserving controller laws. Enlarged realized-control quantifiers are checked separately below. No parent correctness verdict was supplied.

## 2. Exact mean-square Volterra identity for ALL progressive inputs — C17–90

Write L=T-h>0. With u=0 the physical delayed filter is

    f_(h+v)=kappa*c integral_0^v exp(-kappa(v-s))*w_s ds,

and the OU state is `y_t=sigma integral_h^t exp(-epsilon(t-s))*f_s dW_s`, with zero state/output before h. These formulae follow by the actual linear variation-of-constants equations, not by conditioning the disturbance on future noise. For progressive w, f_s uses w only up to s-h and is adapted. All the following integrals are square integrable by the bounded finite-interval filter and the assumed input energy.

Itô isometry first and Tonelli second give

    E integral_0^T d^2*y_t^2 dt
      =d^2*sigma^2 E integral_h^T f_s^2
           [integral_s^T exp(-2epsilon(t-s)) dt] ds
      =d^2*sigma^2/(2epsilon) E integral_h^T
           (1-exp(-2epsilon(T-s)))*f_s^2 ds.

Substitute s=h+v. This is exactly `E||A_L w||^2` for C30–33, applied PATHWISE to w as an L2(0,L)-valued variable. No independence of w from Brownian increments is used in this identity, so it is valid even for L>h.

The deterministic kernel is

    a(v,s)=d*sigma*kappa*c/sqrt(2epsilon)
           *sqrt(1-exp(-2epsilon(L-v)))
           *exp(-kappa(v-s))*1_(0<=s<=v<=L).

It is bounded on a finite triangle, hence Hilbert–Schmidt, compact and bounded. The pathwise deterministic norm inequality gives the full progressive-class upper bound `G2(0)<=||A_L||`. Every deterministic L2 input is admissible and can approach that norm, giving equality. This is not replacement of the progressive class by a smaller class without an upper bound.

Multiplying the two real kernels and integrating their common output variable v yields C85–88 exactly: the lower limit is max(s,t), the upper limit L, and the exponent is `-kappa(2v-s-t)`. Thus A_L^*A_L is the stated compact positive integral operator. Since A_L is nonzero, its positive top eigenvalue is `||A_L||^2`. The integral representation does not divide by epsilon-kappa and therefore needs no omitted equal-rate case.

The norm and the law of the response AFTER translating t=h+v (or its total counted norm) depend on L rather than absolute h. This is the correct sense of C40; no identity of unshifted time-coordinate path laws on different [0,T] intervals is needed or accepted here.

## 3. Complete progressive-input conditioning — C94–117, S54–58

Now L<=h. Progressive measurability on [0,L] and finite expected squared input energy make w a strongly F_L-measurable random element of the separable space H0=L2(0,L). In particular the ENTIRE random input path is already known at F_L. Since F_L is contained in F_h and W is Brownian relative to the filtration, all increments after h are independent of F_L. No output noise exists before h under the ZERO law.

A precise approximation verifies the conditional law instead of asserting Gaussianity for an arbitrary adapted integrand. For a simple F_L-measurable random element `w=sum_j 1_(E_j)*phi_j`, the post-h response is `sum_j 1_(E_j)*R phi_j`. Each E_j is independent of the future driving increments. Conditional on F_L its output has exactly the deterministic phi_j response law. Therefore its conditional first norm moment is J_L(w), and its conditional squared norm moment is `||A_L w||^2`.

Approximate a general w by such simple random elements in L2(Omega;H0). These approximants need NOT be admissible progressive disturbances before L; they are used only to build the post-h integral, where F_L-measurability makes them adapted. The mean-square identity supplies convergence of their outputs in L2(Omega;H1). Cauchy–Schwarz gives L1 convergence of norms and of squared norms; conditional expectation is an L1 contraction. The deterministic estimate

    |J_L(phi)-J_L(psi)|<=||A_L(phi-psi)||<=||A_L||*||phi-psi||

gives matching L1 convergence of J_L(w). Likewise the squared operator norms converge in L1. The two conditional identities in C98–99 follow.

Crucially the denominator is kept as `E||w||`, not `sqrt(E||w||^2)`. If `g_J=sup J_L(phi)/||phi||`, then

    N1(d*y)=E J_L(w)<=g_J*E||w||=g_J*N1(w).

Deterministic inputs give the reverse induced-gain inequality. Thus G1(0)=g_J for the FULL progressive class. Jensen is applied only afterwards to each deterministic response, giving `g_J<=||A_L||`. The boundary L=h is included: increments after h are independent of F_h, and the single endpoint has no stochastic-integral energy.

This argument would fail for L>h, where the full input path can encode information from increments already contributing to output. It is not a blanket Jensen comparison for arbitrary adapted input/output pairs or controlled systems.

## 4. Attainment and strict Gaussian gap BETWEEN SUPREMA — S29–94

For this section d=1. The map R:H0->L2(Omega;H1) is bounded linear, and the preceding deterministic identity is `||R phi||=||A phi||`. A is nonzero: for a nonnegative nonzero input supported strictly before L, its filtered convolution is nonzero on a positive-measure subset before L, where the terminal weight is positive. Thus m=||A||>0 and some J(phi)>0.

Let phi_n maximize J over the closed unit ball. Hilbert weak sequential compactness provides a weakly convergent subsequence with limit phi_* in that ball. A compact linear operator sends that weak convergence to strong convergence. The SAME norm identity for differences gives `R phi_n->R phi_*` in L2(Omega;H1), and hence

    |J(phi_n)-J(phi_*)|<=||A(phi_n-phi_*)||->0.

Therefore J attains its supremum ell at phi_*. Positivity implies phi_* is nonzero; if its norm were less than1, homogeneity would increase J by rescaling, a contradiction. Thus ||phi_*||=1. This is the missing uniformity mechanism that pointwise strict Jensen alone would not provide.

For deterministic phi, finite linear combinations of stochastic-integral output coordinates are centered Gaussian. Approximation in L2 gives the same property for every continuous linear functional of the H1-valued response; equivalently one can interchange a deterministic test-function integral with the square-integrable stochastic convolution. Thus Y=R phi is a centered Gaussian Hilbert random variable.

If such a Y has nonzero second moment, some coefficient along a countable orthonormal basis has positive variance. That scalar projection is a nondegenerate centered Gaussian. If ||Y|| were almost surely a finite constant, this scalar projection would be bounded by that constant, contradicting the Gaussian's unbounded support. Therefore ||Y|| is not a.s. constant. Equality in Cauchy–Schwarz between ||Y|| and1 is impossible, so

    E||Y||<sqrt(E||Y||^2).

Apply this to the NONZERO maximizing response R phi_*. It yields

    0<ell=J(phi_*)<||A phi_*||<=m.

This establishes an actual strict gap between the two suprema without evaluating either endpoint and without claiming that a pointwise gap is automatically uniform. Compactness also gives a norm-maximizing deterministic input for A, as used in the next section.

## 5. All-controller mean-square lower bound WITH pre-action — S98–147

Reintroduce b,beta nonzero, d,r positive and the actual stacked output `(d*y,r*u)`. For a fixed disturbance and the same Brownian path, linearity of the PLANT gives

    d*y=d*y0+S_d u,

with drift and diffusion convolutions exactly as S116–117. This treats the realized control as an input; it makes no assumption that the feedback law itself is linear, stationary, Markov, differentiable or resettable.

The integrals begin at0. Thus any actuation before h, including preview pre-action, is retained in S_d and charged by the positive r*u output. Zero-extending the realized u after T merely bounds this causal input/output map; it does not extend or reset the controller.

For square-energy adapted u, deterministic convolution has L2 norm at most1/epsilon, and Itô isometry followed by integrating the squared OU kernel gives at most1/sqrt(2epsilon) for the diffusion part. Triangle gives exactly the Md in S123–124 and its upper bound Mbar_d for `2epsilon U^2>=1`.

If N2(z) is infinite, mean-square attenuation already fails. Otherwise the separate r*u coordinate forces finite N2(u). Consequently this estimate applies to EVERY admissible attempted control, with no additional expected-control-energy assumption. Triangle and two-dimensional scalar Cauchy–Schwarz yield

    N2(d*y0)<=N2(d*y)+Mbar_d*N2(u)
             <=sqrt(1+(Mbar_d/r)^2)*N2(z).

For a single deterministic unit-norm maximizing input of A, the zero-control numerator is d*m. Applying the inequality to any controller's response to that SAME input proves

    G2(F)>=d*m/sqrt(1+(Mbar_d/r)^2)

uniformly over the enlarged progressive realized-control class. A norm-approaching sequence would suffice if attainment were not used. No conditioning claim is made for controlled outputs, and correlations/cancellation between control and noise were not discarded: they remain in the decomposition and are handled by triangle plus the control penalty.

## 6. Rational existence for EVERY prescribed short horizon — S151–182

Fix arbitrary positive rational h,T,gamma with h<T<=2h. The freely chosen positive rational epsilon,kappa and nonzero rational c,sigma,b,beta satisfy all base assumptions. Sections2–4 define exact positive real endpoints ell<m for this fixed base plant at d=1.

The open interval `(gamma/m,gamma/ell)` is nonempty. Rational density supplies a POSITIVE RATIONAL d inside it, so `d*ell<gamma<d*m`. No evaluated endpoint or numerical search is required to prove this existence. Positive scaling of the output gives exactly these two zero-law gains.

Choose a positive rational U, for example a sufficiently large integer, with `2epsilon U^2>=1`. Then Mbar_d is rational. The positive number Delta=(d*m)^2-gamma^2 is strictly greater than zero. Archimedeanness supplies a positive rational r, again an integer if desired, with `r^2*Delta>gamma^2*Mbar_d^2`. Dividing by the positive r^2 and rearranging gives the strict lower bound in Section5 greater than gamma. This is existence of a rational coefficient, not an evaluated witness or a finite rational certificate for the real endpoint m.

The resulting constant matrices are all rational. Both actuation channels remain nonzero, the full control penalty is positive, and u=0 has the printed state/window form with literal gain d*ell<gamma against ALL progressive square-energy disturbances. EVERY controller has mean-square gain greater than gamma, by the same deterministic test and the proved control-cost bound.

For internal stability, the homogeneous u=0 storage `[(sigma^2+1)/(2kappa)]*f^2+y^2` has expected derivative `-E f^2-2epsilon E y^2`: the sigma^2 diffusion correction cancels its matching part of the f drift. Its positive coefficients imply a strict exponential mean-square bound. No unstable hidden state is being exempted.

This proves OF at the stated nonconstructive existence scope. No explicit d,r, evaluated ell/m, eigenfunction, finite LMI or numerical member was delivered or is inferred by this review.

## 7. Consistency, findings and exact unmet obligations

The earlier screen exclusion in C121–133 also reconstructs in writing. Under L<=h, `a^2 R<=L` and `q^2>=2h` imply `E0>=q/a>=sqrt(2R)`. If R>=1/2, then E0>=1 while the anchor's prefactor/parenthesis product is strictly less than1, so QT<0. If R<1/2, its `1-epsilon a^2-5/(3R^2)` parenthesis is already negative, again giving QT<0. Thus the long-horizon screen cannot meet QT>0 here.

There is NO same-plant/same-level contradiction. The long-horizon family makes mean-square feasibility coexist with literal infeasibility for its own data/horizon. The new short-horizon family has DIFFERENT data and makes literal feasibility coexist with all-controller mean-square infeasibility. Nor does this new construction imply an infinite-horizon opposite-direction result.

No load-bearing identity above remains NOT_RECONSTRUCTED. The following are explicitly outside acceptance, rather than silently labeled PASS:

- Explicit/evaluated ell,m endpoints, a particular rational d,r witness, finite exact matrix/LMI certificate, numerical eigenfunction and quantitative gap size are NOT_EVALUATED/NOT_PROVIDED. Their absence is intentional in the assigned nonconstructive theorem scope.
- The underlying Brownian stochastic calculus, separable-Hilbert conditional-expectation framework, weak sequential compactness, compact Hilbert–Schmidt operator facts and Gaussian projection/support facts are NAMED CLASSICAL IMPORTS. They are used in the written derivation, not formally/kernel certified here.
- Arbitrary-plant necessary-and-sufficient literal synthesis, exact optimal controller gains, arbitrary-controller same-level norm transfer, sharp constants, nonlinear optimal-law structure, novelty and publication acceptance remain NOT_ESTABLISHED.
- Historical unadmitted arithmetic or booleans have ZERO verification/certificate credit and were not used to accept either new source.

**Disposition: WRITTEN_SUPPORTED for SH, SG and the stated all-controller nonconstructive rational OF family, at the disclosed admissibility interpretation and named classical imports.** Parent disposition remains separate. The owner slot, round deadline and scientific HOLD are unchanged.
