# Additive author correction: the cutoff-two coupling penalty is nonincreasing

**Status: PARENT-AUTHORED CORRECTION, NOT YET ADOPTED.** Native observation before composition: 2026-10-30T11:14:30-0700 PDT. The frozen [f400 manuscript](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f400-privacy-cutoff2-scalar-uniqueness-original-frontier/review-v1.md) line498 and the corresponding sentence in [f418](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f418-privacy-cutoff2-uniform-active-core-proof-review/review-v1.md) are false: the difference of endpoint coupling penalties does have a fixed sign. [f419](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f419-privacy-cutoff2-calibration-and-both-endpoint-proof-review/review-v1.md) returns **0 FATAL / 1 MAJOR / 0 MINOR**, with a complete all-variable proof. That original finding remains permanently recorded; neither frozen source is edited or retrospectively labeled correct.

## Correct statement

For every fixed b∈(0,1), a>=0, u=a+1/2, real finite lambda and d>=u, with the corrected canonical pointwise profiles and P defined by f400§5, P(a,d;lambda) is nonnegative and NONINCREASING in d. In particular P(a,c;lambda)−P(a,u;lambda)<=0 whenever c>=u. This is not the sign of the FULL endpoint difference; it proves neither edge dominance, scalar uniqueness, an actual cutoff2 regime nor a global value formula.

## Universal proof, including upper-face and zero-root cases

At a fixed height y∈[0,u], write g=psi1(.,y;lambda), r its nonnegative-root convention, U_d=2d−y and q_d=clip(r,[d,U_d]). Both endpoints increase with d, so q_d is nondecreasing. For a threshold t<=U_d, put E_d(t)=g(max(q_d,t))−g(q_d). If q_d>=t then E=0. If q_d<t, q_d is NOT an upper-face clip, since t<=U_d, hence q_d=max(d,r)>=r; g is nondecreasing from r upward. Increasing d therefore decreases E until it reaches0. This argument explicitly covers a degenerate box, clipping ties and r=0 (including negative radicands); it does not assume that g increases below r.

On a shared-core height, the independent first-core minimizer p0 and its box [a,A], A=2a−y, do not depend on d. Since U_d>=A+1, every t=x+1 is admissible. The core penalty is the minimum over that UNCHANGED box of

(1−b)[psi0(x,y;lambda)−psi0(p0,y;lambda)]+b E_d(x+1).

Every fixed-x expression is nonincreasing in d, so its minimum is also nonincreasing. On the corner [a,u], the threshold t=2u−y<=U_d gives the penalty E_d(t), likewise nonincreasing. Integrating over the unchanged core/corner intervals gives exactly P=8integral_core kappa_d+8b integral_corner E_d, so P is nonincreasing. No far-tail coupling penalty is added; the uncoupled far-tail minimum is already in h_ind.

## Preserved science and acceptance boundary

The f400 competitor, strict V<Q*, whole shared-core binding, full calibration, both-endpoint identities and actual-edge derivative are NOT withdrawn by this localized correction; their own gates remain separate. f418's claim of0F/0M/0m does not certify its repeated incorrect endpoint-sign sentence. Parent has completely read the full f400,537logical f418 and454logical f419 returns and independently reconstructed the conditional excess proof; no new selected diagnostic, held auxiliary privacy episode or scientific execution was used for this correction. A fresh written correction gate and existing independent finite algebra gate remain required before parent adoption. No held episode or consumer is rehabilitated.
