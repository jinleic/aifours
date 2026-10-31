# Exact finite-chain tap norm and a sharper literal necessary condition

**WRITTEN AUTHOR CANDIDATE — UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 15:30:30 PDT 2026**. A substantive all-length coupling refinement of `direct-preview-tap-literal-necessary-bound-v1.md`, SHA-256 `4d3dd07200d15f3a2c96107d329db8e3abad72b4e205e199b5065256a542f259`; originals are unchanged. No source, scientific program, chosen numeric case, hidden controller method or stronger assurance is introduced.

## 1. Original-object statement

Keep the ENTIRE bound linear preview law and original plant, all real compatible matrices, finite T>h>0, S=T-h, zero state/history, canonical progressive E2 disturbances and original literal norms. Set

`J0=D1 L0`, `Jh=D1 Lh`, `N=ceil(S/h)>=1`.

Define the finite block matrix B_N from N input blocks in R^p to N+1 output blocks in R^q by

`y_0=J0 v_0`,

`y_j=Jh v_(j-1)+J0 v_j`, `j=1,...,N-1`,

`y_N=Jh v_(N-1)`.

**Theorem.** For every such fixed law and plant,

**G_prog >= G_det >= ||B_N||.**                               (1)

The quantity ||B_N|| is the EXACT norm and exact essential norm of the original direct-feedthrough operator `J0 w(t)+Jh w(t-h)` between the stated time intervals. Dynamic-state and L2-kernel mean-output contributions are compact and cannot reduce the lower bound (1). Thus it improves the preceding stacked two-tap bound, recovered at N=1. There is no truncation to a selected chain length: N is the full horizon/preview ratio for the actual problem.

Uniform-strict feasibility requires gamma>||B_N||. From pointwise-strict feasibility alone one can deduce only gamma>=||B_N||; equality needs a separate caller and is NOT generically excluded by an essential-norm argument.

## 2. Exact decomposition into ALL delay chains

Represent almost every t>=0 uniquely as t=r+jh, with r in (0,h) and an integer j>=0. Lebesgue integration is exactly integration over r followed by the finite sum of all relevant j. This gives an isometry from time-domain L2 functions to their variable-length delay-chain fibers; no point evaluation on an arbitrary L2 equivalence class is used beyond these a.e. representatives.

Put `ell=S-(N-1)h`, so `0<ell<=h`. For r in (0,ell), the input has exactly N chain entries j=0,...,N-1, and output has N+1 entries through j=N. On this entire positive-measure residue interval the direct operator is exactly B_N. If ell<h, residues r in (ell,h) have N-1 input entries and N output entries, giving B_(N-1). For N=1 the latter input fiber is empty and its output is zero. Boundary residues have zero time measure and are not mistaken for positive-measure extra chains.

Appending a zero input block embeds B_(N-1) isometrically in B_N (with one extra zero final output block), so `||B_(N-1)||<=||B_N||`. It follows at once that the complete direct operator has norm at most ||B_N||.

For the reverse inequality let e=(e_0,...,e_(N-1)) be any unit maximizing vector for the finite matrix B_N. Let phi be any unit scalar L2 function supported in (0,ell), and define the actual deterministic input by

`w(r+jh)=e_j phi(r)`, `r in (0,ell)`, `j=0,...,N-1`,

with zero values on all other input fibers. Its norm is one and its direct output norm is exactly ||B_N||. Hence the direct operator norm is precisely ||B_N||. This includes the case B_N=0 directly.

## 3. Compact terms and the ACTUAL stochastic caller

For deterministic v, the actual E2 state/control of every bound law has the paid mean-output identity

`M v=N_out integral_0^t exp(P(t-s))[B Rv(s)+C v(s-h)]ds + D1 Rv(t)`,

`P=A+BK`, `N_out=D0+D1K`.

Here E2 control is guaranteed by the finite-horizon linear-SDE theorem and the explicit bounded preview operator; therefore the Itô integral has zero mean. It is not assumed for an arbitrary local-only controller. The actual criterion satisfies `E||z_v||>=||M v||`.

As established directly in the preceding packet, the finite-horizon Volterra drift-state part is compact, its composition with the bounded input/preview operators is compact, and the direct L2-kernel part is compact. Thus

`M = (J0 E0+Jh Eh) + K_compact`.

Choose an orthonormal sequence phi_k in L2(0,ell), and use the SAME maximizing block vector e from section 2 to build the full actual inputs w_k. They are an orthonormal sequence in the original input space and are weakly null. Their direct output norms are all ||B_N||, while compactness gives `K_compact w_k->0` strongly. Consequently `liminf ||M w_k||>=||B_N||`. The actual Jensen inequality and the supremum over ALL deterministic disturbances prove (1).

More generally, the same sequence proves that subtracting ANY compact operator from the direct operator leaves norm at least ||B_N||. The zero compact operator gives the converse, proving the claimed essential norm. This auxiliary operator-theoretic statement does not replace the original stochastic output or criterion.

## 4. Scalar closed form, every sign and every length

When J0=j0 and Jh=jh are real scalars,

**||B_N|| = sqrt(j0^2+jh^2+2|j0 jh| cos(pi/(N+1))).**           (2)

Indeed B_N transpose times B_N has constant diagonal j0^2+jh^2 and off-diagonal j0 jh. The N vectors with entries `sin(l k pi/(N+1))`, l=1,...,N, satisfy its eigenvalue equation by the sine addition identity, with eigenvalues `j0^2+jh^2+2j0 jh cos(k pi/(N+1))`. The largest is the displayed value squared, including either sign of j0 jh and the zero-product case. This is an all-N symbolic diagonalization, not a calculated finite example or selected scalar state.

For N=1, cos(pi/2)=0 and (2) reduces exactly to the earlier stacked norm. As h becomes small at fixed T, N grows; the separate h=0 problem has coincident tap j0+jh and is NOT obtained by silently substituting h=0 in the chain decomposition. No continuity-in-h theorem is asserted.

## 5. Sharpness as a universal tap-only lower condition

The bound is sharp when only the given tap matrices are known: use original physical plants with B=C=B0=0, zero initial state, arbitrary A,A0,D0, take H=0 and the prescribed endpoint gains. Their actual state remains zero, so the ORIGINAL output is exactly the direct operator above. Every progressive input is mapped samplewise by that deterministic operator, hence its literal gain equals its deterministic operator norm, ||B_N||, with a deterministic norm-attaining input from section 2.

This is an entire symbolic physical structural family, not a selected numerical test. It proves that no larger universal lower constant depending on the tap matrices alone can be inferred. It does not determine the gain of a different noisy/dynamic plant or prove sufficiency of this condition for synthesis.

## 6. Boundaries and residuals

All matrix ranks/signs, zero tap products, any integer N>=1 and the exact S/h integer boundaries are covered. At an exact integer S/h, ell=h, and the positive-measure chains have N entries; an extra entry at residue zero is a measure-zero artifact. At h=0 use the previously proved combined endpoint bound, not B_N. T<=h lies outside the adopted nonzero-input definition.

This supplies a genuine horizon/preview-coupled finite matrix necessary bound, rather than separately feasible endpoint magnitudes. It does not compute the complete stochastic literal gain, remove the compact mean term, settle pointwise equality endpoints or optimize over controllers. General original synthesis, infinite horizon and source-book equivalence remain OPEN/NR. No claimed witness, solver, operator sampling, model CLI, held guide or stopped controller/storage route is used.

Ordinary facts used are exact time-fiber integration, finite matrix norm attainment, the compact-kernel/actual-mean caller fully reconstructed in the preceding source, weak-null orthonormal L2 sequences and the displayed elementary tridiagonal eigenvectors. All written-source/assurance limitations, late-ACK PROCESS MINOR and STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP persist; no peer/parent adoption, formal/kernel, human/configured-family, executable or novelty claim.
