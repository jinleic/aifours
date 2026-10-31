# Exact fixed-law preview-length discontinuities with unrestricted L2 disturbances

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:22:08 PDT 2026**. First substantive non-construction result after the exact parent branch STOP `e84b09baef996c0e947d70aefa46dbe7802035aabd43a9336d0a8672987a9897`. The stopped diffusion-annihilating-controller branch is not used or reconstructed. This is a class-level delay/criterion obstruction in the already bound linear class, not controller design or synthesis impossibility.

## 1. Full statement and actual physical family

Fix T>0 and the original endpoint tap matrices J0=D1L0 and Jh=D1Lh, held CONSTANT as the preview parameter varies. For each 0<h<T put S=T-h and N(h)=ceil(S/h). Let B_N be the complete block delay-chain matrix

`(B_N v)_0=J0 v_0`,

`(B_N v)_j=Jh v_(j-1)+J0 v_j`, `1<=j<=N-1`,

`(B_N v)_N=Jh v_(N-1)`.

The current author source `direct-preview-tap-chain-essential-bound-v1.md`, SHA `240ca6c4b186835b46da8978e9b551c230c3b6686cae1643a2504729d8abc76f` (UNREVIEWED), derives its exact original time-domain norm and the all-plant lower bound. The new all-matrix asymptotic and explicit continuity obstruction are proved below, not inferred from a numerical sweep.

Define the finite matrix-frequency quantity

`M = max_(theta in [0,2pi]) ||J0+exp(i theta)Jh||`.

Complexification here is only a finite matrix proof device; all physical matrices, disturbances and controls remain REAL.

**Theorem.**

1. `lim_(N->infinity)||B_N||=M`.
2. For the ORIGINAL symbolic physical family B=C=B0=0, arbitrary A,A0,D0, zero initial state/history, H=0 and the fixed law `u=Kx+L0w(t)+Lh w(t-h)`, the actual state is identically zero and

   `G_prog(h)=G_det(h)=||B_(N(h))||` for 0<h<T,

   `G_prog(0)=G_det(0)=||J0+Jh||`.

   Hence the right limit at zero is M, and the fixed-law gain is discontinuous at zero EXACTLY when `M>||J0+Jh||`.
3. For real scalar j0,jh with j0*jh!=0, there are also exact positive-preview jumps at EVERY `h_c=T/(N+1)`, N>=1: the left limit is ||B_(N+1)|| and the value/right limit is ||B_N||, strictly smaller.

These are fixed-law, moving-disturbance-interval phenomena at the literal expected-path-norm criterion. They do not prove that an optimized synthesis value is discontinuous/nonmonotone or that an admissible controller fails to exist. No initial/source convention is silently changed.

## 2. All-matrix finite-chain upper bound by elementary orthogonality

For an input chain v_0,...,v_(N-1), form the finite polynomial `V(z)=sum_j v_j z^j`. Its output polynomial is `(J0+z Jh)V(z)`. Integrating squared norms over the unit circle and using the elementary orthogonality of exp(i j theta) gives

`||B_N v||^2 = (1/(2pi)) integral_0^(2pi) ||(J0+exp(i theta)Jh)V(exp(i theta))||^2 dtheta`

`<= M^2 ||v||^2`.

This is a finite-sum Parseval calculation, not a new Fourier-source import or an executable transform. Thus ||B_N||<=M for every N, with all matrix ranks and zero products retained.

## 3. Matching all-frequency lower limit and real caller

Fix ANY theta and any complex unit vector e of the input dimension; use the analytic chain `v_j=exp(i j theta)e/sqrt(N)`. The N-1 interior output entries have squared norm `||(J0+exp(-i theta)Jh)e||^2/N` each. The two boundary squared norms are nonnegative. Consequently

`||B_N||^2 >= ((N-1)/N)||(J0+exp(-i theta)Jh)e||^2`.

For a REAL matrix B_N its operator norm over complex vectors equals that over real vectors: writing v=x+i y gives `||B_Nv||^2=||B_Nx||^2+||B_Ny||^2` and `||v||^2=||x||^2+||y||^2`. Thus this proof does not enlarge the physical disturbance domain. Compactness of the finite matrix unit sphere and unit circle supplies the maximum M; taking the lower limit and then that maximum gives liminf>=M. Combine with the previous bound to prove theorem item 1.

No frequency, matrix or chain length is selected for numerical evaluation; all theta/e/N are quantified. The same conclusion follows for zero matrices, with M=0.

## 4. Exact original time-domain and stochastic caller

For each h>0, write almost every time as r+jh with 0<r<h. If `ell=S-(N-1)h` then 0<ell<=h. Residues r in (0,ell) carry N input blocks and N+1 output blocks, so the exact tap operator is B_N. The remaining residues, if any, carry B_(N-1). Appending a zero input block embeds the latter into B_N, so the entire norm is ||B_N||. Taking a maximizing real block vector times any unit L2 function of r in (0,ell) gives an ACTUAL real deterministic norm-attaining input. Measure-zero boundary residues do not create an extra chain.

In the stated original physical family, `dx=A x dt+A0 x dW` and x0=0 imply x=0 for all inputs/laws, by the admitted strong linear-SDE uniqueness theorem. Therefore the original output is exactly

`z(t)=J0 w(t)+Jh w(t-h)`.

For every progressive E2 disturbance this is a samplewise deterministic bounded operator. Its pathwise norm bound transfers by expectation with the SAME literal input denominator. Deterministic norm-attaining inputs give the converse gain inequality. Thus both actual gains equal the time-domain operator norm. At h=0 the endpoints coincide and must sum, giving ||J0+Jh|| rather than a two-chain expression.

Since N(h) tends to infinity as h decreases to zero, item 1 proves the exact right limit. M always dominates the zero-frequency value ||J0+Jh||; equality may hold and no discontinuity is claimed then. The family has arbitrary original A,A0 and K but no state response from its zero initial state; no altered output, added realization or controller-construction branch is used.

## 5. Explicit symbolic scalar jumps, every integer boundary

The exact scalar chain norm, derived by the tridiagonal sine eigenvectors, is

`b_N=sqrt(j0^2+jh^2+2|j0 jh|cos(pi/(N+1)))`.

For j0*jh!=0, b_N is strictly increasing in the positive integer N. At `h_c=T/(N+1)`, the exact interval ratio `(T-h_c)/h_c=N`, hence N(h_c)=N. Immediately to its left the ceiling is N+1, and immediately to its right it is N. This proves the stated strict jump without a chosen boundary sample. The cause is that the extra longest-chain residue set has positive, arbitrarily small measure before the boundary and disappears at it; unrestricted L2 inputs may concentrate there with normalized norm.

At zero preview the scalar right limit is |j0|+|jh|, while the zero-preview value is |j0+jh|. Thus EVERY nonzero opposite-sign scalar pair gives a strict zero-preview discontinuity. These are whole analytic parameter families, not a tested value or a bandwidth-limited diagnostic.

As h increases toward T, the input interval remains nonempty but can shrink arbitrarily; N(h)=1 near that boundary and the tap norm is the stacked norm. At h=T there is no admitted nonzero input interval in the adopted definition, so no gain value or feasibility convention is invented there.

## 6. General-plant lower implication and exact residual

For ANY of the original dynamic/noisy plants and bound laws at each h, the previously proved essential mean-tap lower bound gives `G_prog(h)>=G_det(h)>=||B_(N(h))||`. Thus the all-matrix M is a right-liminf lower obstruction as h tends to zero whenever the tap products are held fixed. The actual h=0 gain of a general plant can exceed M due to its state/noise dynamics; no general discontinuity conclusion follows solely from that lower bound.

The failed inference is `small preview/delay change -> small operator/gain change without an input regularity assumption`. It is false for this legal unrestricted-L2 fixed-law family. Norm continuity in matrices/gains/kernel at FIXED h, proved in another current candidate, is not contradicted or improperly extended to a changing shift/interval.

General prescribed-gamma synthesis, different controller classes, alternate horizon/input conventions, infinite horizon and book-domain equivalence remain unresolved. Source-page method discussion, old C1-C3/R4/v209 guidance and all ZERO consumers are noninputs. Named mathematical facts are the displayed finite-chain orthogonality/linear algebra, real-versus-complex matrix norm identity, exact time-fiber integration, original linear-SDE uniqueness and ordinary norm inequalities. No program, selected probe, new source/model CLI, hidden method, stronger verification or novelty claim. All process/HOLD/N4 UNKNOWN/aux214 STOP limits persist.
