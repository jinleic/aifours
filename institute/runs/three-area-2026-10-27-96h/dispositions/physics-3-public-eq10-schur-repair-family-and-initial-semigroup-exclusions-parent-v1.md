# Public 4x4 Eq10 detector route: exact repair-family and small-time exclusions

**Disposition: scoped same-harness written support plus independent exact complex finite corroboration.** Native observation before composition: 2026-10-30T10:59:51-0700 PDT. Disjoint f391/f392 reviews each report **0 FATAL / 0 MAJOR / 0 MINOR**. The original 4x4 PPT Schmidt-number>=3 witness or unrestricted no-go remains open. No publication priority, novelty or claim that the public paper's ordinary-positivity result is false is made.

## Literal public map and true rank-two violation

Let Phi be [vom Ende–Khatri–Denisov arXiv:2508.21348v2 Eq.(10)](https://arxiv.org/html/2508.21348v2#S4.E10), with the paper's unnormalized Choi convention. Its Choi block on span{|34>,|43>} is (1/3)[[0,1],[1,1]]. The actual Schmidt-rank2 vector |34>−|43> has quadratic form −1/3, so this particular seed is NOT 2-positive. This does not refute ordinary (1-)positivity; the source itself describes ordinary positivity as numerically supported, not proved. Its general workflow requires an already k-positive seed.

## Entire affine repair family

For every lambda>=0, real delta and arbitrary COMPLEX Hermitian S>=0, put

Psi=lambda Phi+delta Delta+M_S,  Delta(X)=Tr(X)I4, M_S(X)=S∘X.

With r=(sqrt5−1)/6, the following are equivalent:

**Psi is 2-positive iff Psi is completely positive iff delta>=lambda r.**

Necessity uses a normalized rank2 eigenvector of the 2x2 Choi block with eigenvalue delta−lambda r, on which every Schur addition vanishes. At that threshold all other scalar Choi blocks are nonnegative, while the diagonal-correlated block delta I+(lambda/3)(J4−E34−E43)+S is PSD: its base spectrum is 0,1,(3±sqrt17)/2 and r>(sqrt17−3)/6. Equality, lambda=0, negative delta and singular complex S are covered. Every rank2-positive member is thus PSD as a Choi matrix and cannot pair negatively with ANY PSD state. Invertible local congruences preserve this exclusion; singular filters and non-Schur CP additions are NOT covered.

## Specified semigroup intervals

Let L_K(X)=KX+XK†+Psi(X), with arbitrary complex K. If delta>=lambda r, the semigroup exp(tL_K) is CP for every t>=0 by the finite-dimensional Lie–Trotter formula. If delta<lambda r, put A=lambda r−delta>0 and M=2||K||op+lambda+4|delta|+max_i S_ii. The same rank2 vector is orthogonal to Omega, so its first derivative from KX+XK† vanishes and its total derivative is −A. The Frobenius/Choi reshuffle bound and exponential remainder give a strict rank2-negative expectation for every

0<t<=min{1/M, A/(12M²)}.

Here M>0 under the below-threshold hypothesis. This is an initial interval depending on K, not a common bound over unbounded K or a no-go for all later times.

For the original Phi and K=0, put u=t/3. The actual Choi pair block has off-diagonal sinh(u) and determinant

[(exp(4u)−4)sinh²(u)−sin²(u)]/4 < 0

for 0<t<=3 log(2)/2, including its endpoint. An explicit vector sinh(u)|34>−p_-(u)|43> has Schmidt rank2, with p_->=u²>0, and its quadratic form is p_- times that determinant. This exact longer interval covers only the stated unshifted trajectory; no claim about arbitrary later times follows.

## Verification and remaining gates

[Author](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f382-ppt44-original-two-positive-detector-or-state-frontier/review-v1.md) · [Repair-family written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f391-ppt-eq10-entire-cp-schur-repair-family-proof-review/review-v1.md) · [Semigroup written review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f392-ppt-eq10-semigroup-initial-interval-proof-review/review-v1.md) · [Bounded primary Eq10/workflow excerpt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/source-screens/f382-public-equation10-and-workflow-reader-excerpt-v1.md). Parent displayed the full824-line author,598-line f391,741-line f392 and860-line f393 bodies, reconstructed the complex Choi blocks, exact threshold, full-transpose indices, nonnormal K remainder and K0 population orientation, and checked frozen pins. The independently authored [Gaussian-rational verifier](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f393-ppt-eq10-independent-exact-map-finite-check/independent-eq10-gaussian-rational-check-v1.py) was parent-run ONCE: exit0,14 selected offset/complex-Schur cases including singular and full-rank S, genuine nonreal rank2 quadratic −1/375, complete complex-K Choi drift/sign checks, all13 full Taylor coefficient matrices and5 intended scientific mutations rejected. [Actual receipt](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f393-ppt-eq10-independent-exact-map-finite-check/parent-independent-finite-run-v1-receipt.json). The author checker was also separately parent-run, exit0, but is not independent evidence. Taylor coefficients and finite cases do not prove the uniform family or analytic time interval; those are carried by the written proof. Child execution was NOTRUN.

No actual 4x4 PPT/SN3 state–detector pair, all-4x4 no-go, higher-hierarchy impossibility, ordinary-positivity refutation, source-wide literature or novelty result follows. Same-harness only; no human/independent-family/formal-kernel/original-target acceptance.
