# A finite algebraic classification of the matrix tap endpoint

**WRITTEN AUTHOR CANDIDATE — UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:27:03 PDT 2026**. Non-construction structural continuation of `infinite-endpoint-tap-literal-gain-and-strictness-v1.md`, SHA `66512920bfa6bfc991e90196846e3032fdf7edc590160bec99d066d1d13daf30`. No new source, scientific computation, held route or controller construction is used. The explicit parent diffusion-annihilating-branch STOP and every process/HOLD/ZERO limitation remain.

## 1. Full matrix physical scope and finite condition

Keep exactly the actual infinite-horizon tap family/caller from that source: B=C=B0=0, arbitrary compatible finite A,A0,D0, zero state/history, H=0 and fixed deterministic stationary endpoint law. Thus x=0 and the ORIGINAL regulated output is

`z(t)=J0 w(t)+Jh w(t-h)`

for all canonical progressive E2 inputs on [0,infinity), with zero negative history and finite h>0. Let J0,Jh be their arbitrary real q-by-p products, and put

`H(z)=J0+z Jh`,

`M=max_(|z|=1)||H(z)||`.

The actual progressive and deterministic literal gain both equal M, as previously reconstructed with finite chains. For the nonzero case M>0 define the p-by-p Laurent polynomial matrix

`D(z)=M^2 I_p-(J0^T+z^(-1)Jh^T)(J0+z Jh)`.

On the unit circle this is Hermitian positive semidefinite. Multiplying det D(z) by z^p produces an ordinary real polynomial of degree at most 2p. “Identically zero” below is the finite polynomial identity, not vanishing at selected test frequencies.

**Theorem.** For M>0:

1. The actual time-domain tap operator attains its norm at a NONZERO real L2 input iff **det D(z) is identically zero**.
2. If the identity holds, there is a real finite-support delay-chain norm-attaining input; it is an actual deterministic E2 disturbance, not merely a formal spectral profile.
3. If the identity does not hold, EVERY nonzero real L2 input has output norm STRICTLY less than M times its input norm. Hence every nonzero canonical progressive E2 input satisfies the literal STRICT ratio at gamma=M, despite gain supremum M.

Thus the full matrix fixed-law pointwise-strict threshold is:

- det D identically zero: **gamma>M**;
- det D not identically zero: **gamma>=M**.

Uniform-strict feasibility always requires gamma>M. The prescribed gamma is positive. M=0 and h=0 are treated separately below. This is not a general synthesis test over different controllers.

## 2. Build only the L2 representation actually needed

For a one-sided square-summable chain v=(v_j), let `V(z)` be the L2 unit-circle limit of its finite polynomials `sum_(j=0)^N v_j z^j`. Elementary finite orthogonality makes the partial polynomials Cauchy with squared norm sum |v_j|^2; completeness identifies a limit. It is zero iff every coefficient is zero, by taking its individual Fourier inner products. No Hardy-space uniqueness theorem is imported.

The output chain is multiplication by H(z), because it is true for finite chains and both bounded operators pass to the L2 limit. Therefore

`M^2||v||^2-||H v||^2 = (1/(2pi)) integral V(z)^* D(z)V(z) dtheta >=0`. (1)

This identity is a chain energy calculation for the actual deterministic tap map, not an RMS replacement of the original stochastic criterion. The original time-space is the integral over residues r in (0,h) of these chains, by exact time-fiber decomposition; all functions remain a.e. time-domain L2 objects.

## 3. Nonzero determinant implies strict nonattainment

If det D is not the zero Laurent polynomial, its ordinary polynomial multiple has only finitely many unit-circle zeros. Except on that finite set, D is positive semidefinite AND invertible, hence positive definite.

For any nonzero chain its V is nonzero on a positive-measure set. Thus the nonnegative integrand in (1) is strictly positive on a positive-measure subset, giving a strictly positive integral. Every nonzero chain has norm strictly decreased relative to M.

For any nonzero time-domain w, its residue chains are nonzero on a positive-measure residue set. Integrating the nonnegative strict chain gaps yields

`||J0 w+Jh S_h w|| < M||w||`.

For an actual nonzero progressive E2 input apply this to its finite-energy sample paths. The gap is positive on the positive-probability event of nonzero input norm and bounded by the integrable M||w||. Its expectation is positive, proving the literal strict inequality at gamma=M. No claim of a common gap below M or a random norm maximizer follows.

## 4. Identically zero determinant gives an ACTUAL finite real caller

If det D is identically zero, D is singular as a matrix over the ordinary field R(z). Elementary linear algebra over that field supplies a nonzero rational vector r(z) in its kernel. Multiplying by the finitely many denominators and by a sufficient power of z gives a nonzero REAL polynomial vector

`p(z)=sum_(j=0)^N p_j z^j`, `p_j in R^p`,

satisfying `D(z)p(z)=0` as a Laurent-polynomial identity. This is an existence proof from exact finite linear algebra, not a performed elimination/CAS or a selected matrix rank case. It holds at every nonzero z by the cleared identity.

Use the finite chain v_j=p_j. Its squared input norm is positive. Substitution in (1) makes the integral zero, so its full output chain norm is exactly M times its input norm, including the final delayed output block.

To obtain the original physical disturbance, choose ANY real unit phi in L2(0,h) and set

`w(r+jh)=p_j phi(r)`, `r in (0,h)`, `j=0,...,N`,

zero on later chain blocks. It is deterministic, finite-energy and nonzero, hence an admitted progressive E2 input on the original canonical space. The ACTUAL original output is its matrix tap convolution, and time-fiber integration gives the exact norm ratio M. This proves both sufficiency and the endpoint-violation caller. No controller or altered output is constructed.

## 5. Exact threshold, necessity and every degenerate case

The known gain supremum M supplies actual deterministic near-maximizers, so any gamma<M fails regardless of the determinant case. At gamma=M, section 3 proves pointwise strictness for EVERY stochastic input in the nonidentity case, whereas section 4 supplies an actual deterministic violating input in the identity case. Above M a uniform margin holds. This proves the complete pointwise/uniform statement, not merely a one-way spectral filter.

If M=0 then H(z)=0 on the circle, hence J0=Jh=0; original output is zero and both conventions hold for every prescribed gamma>0. No gamma=0 convention is added. At h=0 the map is the memoryless matrix J0+Jh; a nonzero matrix attains its norm along a real maximizing direction, so both strict conventions require gamma>||J0+Jh||, with the zero-output case again valid for gamma>0.

All positive input/output dimensions, arbitrary real matrices, singular/rank-deficient directions and polynomial-degree drops are included. The determinant identity is not confused with D itself being zero, and a frequencywise singular direction is not independently selected at each frequency: a SINGLE real polynomial vector is produced and called back to the same actual input. That caller is the crucial distinction from a real-spectrum or pointwise-direction relaxation.

For the scalar nonzero two-tap case the determinant is not identically zero, recovering the preceding nonattainment result. With only one nonzero scalar tap the determinant is identically zero and the scaled-isometry endpoint is attained. These are symbolic consistency consequences, not numerical tests.

## 6. Remaining original-target gap and import limits

This gives an exact finite algebraic norm-attainment/strictness criterion for the entire stated matrix fixed-law physical family. It does not solve general existential stochastic preview synthesis, determine the source's unspecified uniform-margin convention, extend to arbitrary dynamic/noisy-state plants, or clear source/controller-domain equivalence. It does not authorize the stopped diffusion-annihilating controller branch.

The only ordinary facts used are finite polynomial orthogonality and L2 completeness, finite matrix positivity/norms, finitely many roots of a nonzero polynomial, elementary nullspace linear algebra over R(z), time-fiber integration and positivity of an expectation. The prior physical caller uses original zero-state linear-SDE uniqueness. No unprovided Hardy-space, spectral-factorization, storage/Gramian, realization or old guide is imported; no scientific interpreter, selected frequency/rank/state/control probe, source expansion or external model/nested agent occurred. All source-render/copyright, process, STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP boundaries persist; written only, with no peer/parent, formal/kernel, executable, human/configured-family or novelty acceptance.
