# Author candidate — actual high-defect four-qubit matrices and exact finite verifier

**Status: AUTHOR CANDIDATE; prepared source UNRUN.** The written derivations below concern the specific family and quantifiers stated here. They are not a parent disposition, independent family/human review, formal-kernel verification, publication-priority claim, or a theorem about arbitrary four-qubit states. The source is a new standalone exact checker; its intended checks are not reported as results. Parent must fully read and audit it, freeze its actual bytes, and issue a separate one-shot GO before any execution. Nothing in this candidate authorizes execution.

## 1. Precise scope

Take the packet's phase-locked family at **C = 1/3**, with **q in {0, 1/8}**, and define

\[
D=6^{-1/2}\!\sum_{|x|=2}|x\rangle,\quad
 y=(|0000\rangle+|1111\rangle)/\sqrt2,\quad
 \psi=\sqrt{2/3}\,D+i\sqrt{1/3}\,y,\quad v=|0000\rangle.
\]

Let \(X_q=(1-q)|\psi\rangle\langle\psi|+q|v\rangle\langle v|\), and \(\rho_q=U X_q U^\dagger\) for **every** local \(U=U_1\otimes\cdots\otimes U_4\), \(U_j\in U(2)\). For each physical \(p\in[0,4/3]\), put \(t=|1-p|\), \(b=(1-t)/2\), and
\(D_t=\operatorname{diag}((1+t)/2,b)^{\otimes4}\). The written argument in §§3–5 gives, for **every** complex orthogonal rank-\(k\) projector \(Q\) on the actual four-qubit space and \(k=1,\ldots,16\),

\[
\operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho_q)]\le K_k(D_t),\qquad
\Phi_p(A)=(1-p)A+\tfrac p2\operatorname{Tr}(A)I.
\]

For \(1\le k\le11\) it gives the stronger bound with subtraction
\((1-q)g_k t^2b^2\), where \(g_k=3\) for \(1\le k\le5\) and \(g_k=5\) for \(6\le k\le11\). This is an author-derived **family-specific** result, not the unrestricted high-defect spectrum theorem. The checker is much narrower: two q values, two explicitly selected frames, five p values and one nested set of sixteen actual complex projectors, plus the separately constructed mutant witnesses. Its finite checks would not establish the universal quantifiers.

The two frames prepared in source are the identity and
\[
U_* = \begin{pmatrix}3/5&4i/5\\4i/5&3/5\end{pmatrix}
\otimes\begin{pmatrix}3/5&4/5\\-4/5&3/5\end{pmatrix}
\otimes\begin{pmatrix}1&0\\0&i\end{pmatrix}\otimes I_2.
\]
Each factor is exactly unitary. The finite p set is \(\{0,1/2,2/3,1,4/3\}\); it includes both channel endpoints, zero retention, positive retention, and the physical negative-retention endpoint. C = 1/3 and both q values are endpoints of the packet's larger parameter box; no finite check of C = 1/6 or of other C is claimed here.

## 2. Actual 16×16 states and every one-, two- and three-body marginal

Put \(r=\sqrt6/6\). In the computational basis indexed by four-bit strings, the **complete entrywise definition** of the physical vector is
\[
\psi_x=\begin{cases}ir,&|x|\in\{0,4\},\\1/3,&|x|=2,\\0,&|x|\in\{1,3\}.\end{cases}
\quad (X_q)_{xy}=(1-q)\psi_x\overline{\psi_y}+q\,\mathbf1_{x=0}\mathbf1_{y=0}.
\]
Its rotated entry is \((\rho_q)_{xy}=\sum_{z,w}U_{xz}(X_q)_{zw}\overline{U_{yw}}\), with \(U_{xz}=\prod_i(U_i)_{x_i z_i}\). These formulas fix **all 256 entries**, including complex coherences; the source constructs the rotated vectors and their physical outer products, not an abstract spectrum or independently prescribed marginals. The pure vector has norm one, and \(v\) and \(\psi\) are linearly independent. Thus \(X_0\) has rank one and \(X_{1/8}\) rank two.

For the unrotated \(X_q\), the same-state physical partial traces, in the natural computational bases, are as follows. For every singleton,
\[
(X_q)_i=(1-q)I_2/2+q|0\rangle\langle0|.
\]
For every pair,
\[
(X_q)_{ij}=(1-q)\begin{pmatrix}
5/18&0&0&0\\0&2/9&2/9&0\\0&2/9&2/9&0\\0&0&0&5/18
\end{pmatrix}+q|00\rangle\langle00|.
\]
The pure pair purity is \(2(5/18)^2+4(2/9)^2=19/54\). For every triple, the complete 8×8 matrix is
\[
(X_q)_{ijk}=(1-q)(aa^\dagger+bb^\dagger)+q|000\rangle\langle000|,
\]
where
\[
a=ir|000\rangle+(|011\rangle+|101\rangle+|110\rangle)/3,\quad
b=(|001\rangle+|010\rangle+|100\rangle)/3+ir|111\rangle.
\]
The vectors \(a,b\) have orthogonal supports and squared norm 1/2 each. These formulas follow directly by grouping the original vector by the traced qubit; permutation symmetry covers every choice of subset. For arbitrary local U, each marginal is conjugated by the tensor product of the U factors **on that same subset**. The source separately constructs all 4 singletons, 6 pairs and 4 triples from each actual 16×16 density, and the H layers by re-embedding them on their original qubits.

## 3. Written H1, H2 and H3 identities, inequalities and rank witness

For \(H_j(X)=\sum_{|S|=j}\operatorname{Tr}_{S^c}X\otimes I_{S^c}\), \(H_0=I\), \(H_4=X\), physical partial tracing gives \(H_1(|\psi\rangle\langle\psi|)=2I\). Writing \(J_\alpha=\tfrac12\sum_i\sigma_\alpha^{(i)}\), direct use of the pair matrix gives
\[
H_2(|\psi\rangle\langle\psi|)=I+\tfrac29J^2-\tfrac16J_z^2. \tag{1}
\]
For the elementary four-spin decomposition \(2\cdot j=0\oplus3\cdot j=1\oplus1\cdot j=2\), its eigenvalues, with multiplicities, are
\[
1^{\times2},\quad(13/9)^{\times3},\quad(23/18)^{\times6},\quad
7/3,\quad(13/6)^{\times2},\quad(5/3)^{\times2}.
\]
Consequently \(I\le H_2(|\psi\rangle\langle\psi|)\le3I\) and \(\operatorname{Tr}H_2=24\). The actual product layer is diagonal with eigenvalue \(\binom{4-h}{2}\) on Hamming weight h; its spectrum is \((6,3^{\times4},1^{\times6},0^{\times5})\). Its first five prefixes are \(3k+3\), its next six are \(k+13\), and the rest are 24. The pure H2 prefixes are bounded by \(3k\), \(k+8\), and 24 respectively; hence the announced gaps 3 and 5. Linearity gives for the **same actual mixture**
\[
(1-q)I\le H_2(X_q)\le(3+3q)I,\qquad \operatorname{Tr}H_2(X_q)=24. \tag{2}
\]
The displayed bounds are \([I,3I]\) at q=0 and \([(7/8)I,(27/8)I]\) at q=1/8. The code prepares direct exact PSD tests on unrotated matrices and checks local-unitary covariance of the actual pure and product layers, rather than assigning these bounds to unrelated reductions.

For \(A_i=\psi_{\overline i}\otimes I_i\), \(\operatorname{Tr}A_i^2=1\), and, for distinct i,j, \(\operatorname{Tr}(A_iA_j)=19/54\). Therefore
\[
\operatorname{Tr}H_3(\psi\psi^\dagger)=8,\qquad
\operatorname{Tr}H_3(\psi\psi^\dagger)^2=4+12(19/54)=74/9. \tag{3}
\]
Also \(\operatorname{Tr}H_3(P)^2=20\) and the **actual cross term** is \(\operatorname{Tr}[H_3(\psi\psi^\dagger)H_3(P)]=14/3\). For the latter, \(H_3(P)\) is diagonal with values 4 at weight 0, 1 at weight 1 and 0 otherwise; the corresponding pure-layer diagonal entries are 2/3 and 1/2. Hence
\[
\operatorname{Tr}H_3(X_q)=8,\quad
\operatorname{Tr}H_3(X_q)^2=(74-64q+170q^2)/9
=\begin{cases}74/9,&q=0,\\2197/288,&q=1/8.\end{cases} \tag{4}
\]
Each triple marginal is a density, so each embedded term lies between 0 and I; consequently \(0\le H_3(X_q)\le4I\). These are actual physical matrices, not a separately optimized moment model.

An independent, explicit finite rank witness for the **pure** H3 is
\[
H_3(\psi\psi^\dagger)=2|\psi\rangle\langle\psi|
+\tfrac12\sum_{i=1}^4\sum_{\alpha=x,y,z}
|\sigma_\alpha^{(i)}\psi\rangle\langle\sigma_\alpha^{(i)}\psi|,
\qquad \operatorname{rank}H_3(\psi\psi^\dagger)\le13. \tag{5}
\]
It follows from the one-qubit Pauli twirl, and the source constructs all thirteen actual vectors and compares their outer-product sum to the partial-trace H3. **No rank-13 assertion is made for the q=1/8 mixed H3.** For the pure H3, the rank-1 prefix is at most 4; Cauchy–Schwarz and (3) give for k=2,3,4 that \(K_k^2\le k(74/9)<(k+3)^2\); all later prefixes are at most trace 8. This is majorization by the product H3 spectrum \((4,1^{\times4},0^{\times11})\). The mixed-layer bound follows by actual linearity and the same projector, not by extending the pure rank bound to mixed inputs.

## 4. Exact defect and genuine entanglement

Define \(\widetilde X=Y^{\otimes4}X^T Y^{\otimes4}\), \(\Delta=(X-\widetilde X)/2\), and \(d=\|\Delta\|_1\). In the orthonormal basis \((D,y,z)\), \(z=(|0000\rangle-|1111\rangle)/\sqrt2\), and zero on its orthogonal complement,
\[
\Delta=\begin{pmatrix}
0&-i(1-q)\sqrt2/3&0\\
i(1-q)\sqrt2/3&0&q/2\\0&q/2&0
\end{pmatrix}.
\]
Thus the **exact physical spectrum identity** is
\[
\Delta^3=\tfrac{d^2}{4}\Delta,\quad
\operatorname{spec}(\Delta)=\{+d/2,-d/2,0^{\times14}\},\quad
\operatorname{Tr}\Delta^2=d^2/2,\quad
 d^2=q^2+\tfrac89(1-q)^2. \tag{6}
\]
The two actual values are \(d^2=8/9\) and \(401/576\), and the nonzero eigenvalues are respectively \(\pm\sqrt2/3\) and \(\pm\sqrt{401}/48\). The checker constructs the actual 16×16 spin-flipped density and verifies the exact Hermiticity, zero trace, rank two and squared trace in (6); these imply the spectrum and cubic identity by elementary Hermitian rank-two linear algebra. Eigenvalue square roots need not themselves lie in \(\mathbb Q(i,\sqrt6)\). Local spin flip transforms by conjugation under U because \(Y U_i^*Y=(\det U_i)^*U_i\).

There is also a direct finite polynomial GME witness for the range, not a numerical entanglement estimate. Put \(W=\operatorname{span}\{\psi,v\}\). For every one-versus-three cut, choose the two single-qubit row strings 0,1 and triple column strings 001,011. For each of the three representative two-versus-two cuts, use row strings 00,01 and column strings 10,11. In all seven cuts the corresponding 2×2 minor of the coefficient matrix of \(a\psi+bv\) is exactly
\[
-\frac{a^2}{9}, \tag{7}
\]
with zero \(ab\) and \(b^2\) coefficients. Thus every range vector with \(a\ne0\) is entangled across every cut; the only biseparable ray in W is v. Positivity forces all pure constituents of a convex decomposition to lie in the density's range, so neither selected state is biseparable. Local U preserves cut Schmidt ranks. The code's seven exact polynomial coefficient checks implement (7).

For the optional larger-hull separation, the actual bilinear identity is
\[
(a\psi+bv)^T Y^{\otimes4}(a\psi+bv)
=\frac{a^2}{3}+\frac{i\sqrt6}{3}ab. \tag{8}
\]
The only eta-zero rays in W are v and \(x_N=\psi+i\sqrt6\,v/6\); the only eta-one ray with nonzero psi coefficient is \(x_I=\psi-i\sqrt6\,v/3\), which is fixed by the spin-flip antiunitary. The eta-one uniqueness uses the equality condition in Cauchy–Schwarz, after fixing the phase by the nonzero real Dicke coefficient. If \(X_q\) were a mixture of pure biseparable, eta-zero or eta-one states, range inclusion would restrict its constituents to these rays. In the independent basis \((\psi,v)\), nonnegative unnormalized weights \(\alpha,\beta,\gamma\) on \(x_I,x_N,v\) would satisfy \(\alpha+\beta=1-q\), \(\beta=2\alpha\), and \(q=\alpha+\gamma=(1-q)/3+\gamma\). Both selected q values violate \(q\ge(1-q)/3\). Hence these states lie outside that explicitly defined enlarged hull as well. The source prepares exact checks of the bilinear coefficients, the two named rays and the strict obstruction; the general uniqueness/range argument just given is written reasoning, not a claim of exhaustive computational algebra.

The pure state has eta \(1/9\), and the mixed state is rank two. Both displayed d² values exceed 3/13. The comparison with the historical mixed/pure sufficient regions and the old named classes is conditional on the **actual** meanings and scopes recorded in packet S2/S1; neither historical threshold's original proof nor any linked invariant-sector theorem body was opened or silently imported. The present layer proof does not require that unavailable theorem.

## 5. One actual projector, physical negative retention and boundary cases

For positive retention, the expansion of the **same** actual density is
\[
\Phi_{1-t}^{\otimes4}(X_q)=\sum_{j=0}^4t^j b^{4-j}H_j(X_q).
\]
Fix one Q. Apply its expectation to every term, use the pure H1/H2/H3/H4 bounds and the linear mixture with \(P=vv^\dagger\), and use the coordered product Hamming-weight layers only for the product comparator. Their weighted sum is exactly \(D_t\), not the sum of unrelated optimized states. The actual H2 gap is \((1-q)g_k\) for k≤11. The physical local-unitary statement follows by conjugating both the output and the one physical Q.

For negative retention, \(0<t\le1/3\), use the **full** four-qubit transpose:
\[
\Phi_{1+t}^{\otimes4}(X)=F[\Phi_{1-t}^{\otimes4}(X)]^TF,\quad
\operatorname{Tr}[Q\Phi_{1+t}^{\otimes4}(X)]
=\operatorname{Tr}[(FQ^TF)\Phi_{1-t}^{\otimes4}(X)],\quad F=Y^{\otimes4}.
\]
The same single transported \(FQ^TF\) is used for every layer. At p=0 the reference is rank one and the gap term vanishes; at p=1 all outputs are \(I/16\); at p=4/3, \(t=b=1/3\), and the k≤11 gap is \((1-q)g_k/81>0\). At k=16 both traces are exactly one. None of these endpoint statements depends on excluding q=0 or q=1/8.

The prepared source uses a genuine physical nested projector family \(Q_k=W P_k W\), with \(w_j=1+i(j\bmod3)\), \(w^\dagger w=41\), \(W=I-2ww^\dagger/41\), and \(P_k\) the first-k computational projector. W is Hermitian and unitary, so each actual Q_k is complex and has rank k. It constructs the literal matrices, checks their trace/Hermiticity and W²=I, and compares the fast same-Q expectation formula with literal \(\operatorname{Tr}(Q_kH_2)\). For the four selected physical densities at the five p values, the intended exact checks compare these same physical Q_k with all five actual layers and the coordered reference, including full-transpose negative retention. This finite set does not replace the all-Q written reasoning.

## 6. Exact reason-specific mutant design

* **Wrong projector transpose.** For the q=1/8 rotated state, the local first-qubit Y expectation after the positive-retention t=1/3 channel is exactly \(1/25\): the pure singleton contributes zero, the vacuum's first local Bloch-Y component is 24/25, and \((1/3)(1/8)(24/25)=1/25\). Thus the positive output has a non-real off-diagonal entry. The source selects one such pair i<j, forms \(R=(|i\rangle+i|j\rangle)(\langle i|-i\langle j|)/2\), and takes the actual negative-output projector \(Q=FR^TF\). The correct transported expectation is \(\operatorname{Tr}(R\,\mathrm{out}_+)\), while omitting the transpose gives \(\operatorname{Tr}(R^T\mathrm{out}_+)\); these differ because the selected entry is non-real. It separately checks the full actual channel matrix identity and same transported Q across layers.
* **Spin flip and moment.** On that same complex state, \(F\rho F\ne F\rho^TF\), so a spin flip omitting the full transpose is a distinct rejected mutant. For the pure state, the moment-coefficient mutant \(8+C^2=73/9\) differs from the actual \(74/9\) by exactly \(1/9\); this targets the missing factor 2, not a floating residual.
* **Changing Q between layers.** For the q=1/8 rotated density at t=1/2, use \(Q_v=|Uv\rangle\langle Uv|\) on all layers except H1 and substitute \(Q_w=|U1111\rangle\langle U1111|\) for H1. Their H1 expectations differ by \(4q=1/2\), so the one-Q physical expectation minus this false layer sum is exactly \((1/2)(1/4)^3(1/2)=1/256\). This mutation diagnoses incompatible projectors; it is not asserted to be a channel counterexample.

These are precise intended exact checks and written identities, **not observed checker output**.

## 7. Source, execution boundary, imports and read/process declaration

* New source: `fourqubit-high-defect-physical-exact-v1.py`, standalone Python ≥3.10 stdlib, integer-coefficient \(\mathbb Q(i,\sqrt6)\), exact sign decisions and no numerical tolerance. Parent supplied the following **administrative-only** metadata in direct response: SHA-256 `5f722df64060b8b2130317c599b932adce053d6eb8e5a3c9a0fac30749dbcc1a`; 27,015 bytes; 760 LF. This is not an independent source audit, execution, GO, correctness or pass claim. The source has not been run, imported, compiled or tested. It uses a 36-second cooperative internal deadline and returns INCOMPLETE when a guard observes it; an authorized parent launcher must independently enforce outer wall ≤55 seconds. Scheduling/one-operation latency is not falsely represented as a hard internal kill.
* Before mathematical body or reasoning I read, in full, the manifest, freeze receipt, final pre-dispatch binding, parent-live metadata, actual dispatch receipt, and all 22 manifest-listed controls **as status/permissions only**. The initial non-raw administrative displays elided JSON blocks; complete raw rereads recovered them. I wrote `prebody-ack-v1.md` and directly delivered the prebody ACK to Main before opening the packet. Mandatory memory-summary display clipped long lines; it was procedural/non-mathematical and not a load-bearing input. Written-math and research-round skills supplied process context only.
* I then read the single complete literal packet part serially in raw windows **1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, 261–276**, including both source endings. The complete part is parent-supplied 27,230 bytes, so every display was below 30,000 bytes; no packet clipping was displayed and no body recovery was needed. Parent-supplied packet SHA-256 is `5cc20c2d1bd4ccc8ae95dc40dfce934e9dc9aae66147352a651cade9b7ceb826`; S1 complete LF 1–219 is pinned `098435386c86deeb036faa455fe17ca43ae613fc25a2cc62060a4cbb6b63fcd2`, S2 complete LF 1–47 is pinned `4d9f3d97723cafe956eaf7c151506249e08c246bb35b59436fe64b015558eaff`. These are supplied metadata, not independently recomputed verification.
* All genuine held episodes and all their method/selection/proof/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. I did not open linked source bodies, old code, sibling work or unlisted mathematical source, use network/external models, run scientific code, tests, compilation, solvers or child subprocesses, or modify any frozen/previous candidate. No execution result, external-model/family/human acceptance, global theorem, source equivalence or literature-wide novelty is asserted. Parent full-source reading, any separate GO, independent review and parent disposition remain distinct future actions.
