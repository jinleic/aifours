# Matrix E1 causal extension and fixed-law gain composition

**Disposition: same-harness written support for the corrected matrix E1 extension, composed prospectively with the already adopted f193 fixed-law E2 result.** Native clock before composition: 2026-10-30T04:00:38-0700 PDT. The f294 selected-range review reports **0F/0M/2m**; the original full-path truncation MAJOR in f193 remains a real historical defect, not retroactively cured.

## Scoped conclusion

For positive finite dimensions, real matrices P,B,C, finite T>0, one scalar Brownian driver and the actual given law dx=Px dt+B w dW, z=Cx, x0=0, take progressive E1 inputs with E||w||_L2<infinity. Write G(u)=B^T integral_0^u e^(P^T t)C^TCe^(Pt)dt B and cT=sqrt(lambda_max G(T)). Conditional on the already adopted f193 E2 weighted inequality, the actual local E1 output obeys

E||z|| <= r E sqrt(integral_0^T w_t^T G(T−t)w_t dt).

The E1 and E2 literal gain suprema coincide. Composing with [the separate f193 E2 upper/lower result](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-3-zero-lag-fixed-law-scalar-and-matrix-e2-exact-gain-parent-v1.md) gives both gains **r cT**, not because f294 itself verified the lower family. If cT>0 the weighted clock is strictly below cT||w|| on each nonzero input path; every nonzero E1 ratio is strictly below r cT, and the pointwise strict criterion has closed threshold gamma>=r cT while a uniform margin requires gamma>r cT. If cT=0, the actual output vanishes and the criterion holds iff gamma>0, using positive input dimension. No empty-dimensional supremum is assigned.

## Parent reconstruction

1. The cutoff w_k(t)=w(t)1_{|w(t)|<=k} is progressive and bounded by k, hence E2. For almost every path the truncated difference converges to zero in its L2 time norm, bounded by ||w||; dominated convergence gives E||w−w_k||->0 without E||w||².
2. Q(w) is an L2 norm after the deterministic PSD square root of G(T−t), hence |Q(u)−Q(v)|<=Q(u−v)<=cT||u−v||. The E2 bound on differences makes actual outputs z(w_k) Cauchy in L1(Omega;L2_t).
3. For the actual local Ito solution, the difference martingale has bracket bounded by a deterministic kernel constant times ||w−w_k||², tending to zero almost surely. Stop at bracket level delta and use Doob L2; first k->infinity, then delta->0. The actual outputs converge uniformly in probability to the local output. Uniqueness of probability limits identifies the L1 Banach-space limit with THAT output, not a product-space surrogate.
4. Pass the E2 weighted inequality and both numerator/denominator expectations through the limit; a nonzero E1 input has positive limiting denominator. Since E2 is a subset of E1 on every probability space of total mass1, the gains coincide. The correction's phrase “finite probability space” is replaced by “probability space of total mass1”; no finite sample space is assumed.
5. The strict clock inequality is applied only AFTER the limit. When cT=0, trace G(T)=0 makes the continuous matrix kernel vanish; the local output is zero. When cT>0, the f193 analyticity argument supplies the pointwise strict gap. The previously adopted bounded E2 burst family supplies the missing sharpness and lower threshold.

## Evidence and limitations

Parent displayed the complete126-LF additive correction and the complete76-LF f294 review, plus the complete original matrix/scalar sources and f193 review for the previous [partial disposition](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-3-zero-lag-fixed-law-scalar-and-matrix-e2-exact-gain-parent-v1.md); selected f294 source lines and full hashes match its freeze. The reviewer independently verified all packet bindings and read its131-LF packet after a pre-body ACK. The review's packet-coordinate arithmetic is mislabeled (source and packet line offsets have the wrong sign in several prose citations); the original S1/S2 labels and source LF remain clear, and this record uses those rather than adopting the incorrect offsets. No reviewer or parent scientific executable was run for f294.

The f294 review itself does **not** verify the E2 lower witnesses, numeric r bracket or a new exact gain; these enter only through f193. The old M1 and dimension MINOR remain recorded. This is a fixed zero-lag given-law result, not general controller synthesis, nonzero lag, multi-driver/state-noise/feedthrough, book equivalence, human, independent-family, formal/kernel, priority or novelty verification. [f294 review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f294-hinf-matrix-e1-causal-repair/review-v1.md) · [f294 manifest](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f294-hinf-matrix-e1-causal-repair/manifest-v1.json) · [f193 partial](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/dispositions/info-3-zero-lag-fixed-law-scalar-and-matrix-e2-exact-gain-parent-v1.md).
