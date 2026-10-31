# Author candidate: all-prefix physical channel proof for the phase-locked Dicke–cat–vacuum family

**Status and scope.** Fresh written author reconstruction, not an independent review, parent disposition, formal-kernel proof, human or model-family acceptance, or literature-priority claim. The result below is only for the explicitly quantified family. In particular it is not a theorem for all high-defect four-qubit states. Its all-prefix channel proof does not use the unprovided body of the invariant-sector theorem linked by packet S2. The exact H2 analysis yields a strengthened strict gap through rank 15, not just through rank 11. All claimed mathematics is written here for a subsequent disjoint check.

## 1. Statement, variables, and the exact gap

Let
\[
D=\frac1{\sqrt6}\sum_{|x|=2}|x\rangle,\quad
 y=\frac{|0000\rangle+|1111\rangle}{\sqrt2},\quad v=|0000\rangle,
\]
\[
 \frac16\le C\le\frac13,\quad 0\le q\le\frac18,\quad
 c=\sqrt{\frac{1+C}{2}},\quad s=\sqrt{\frac{1-C}{2}},\quad
 \psi=cD+is y,\quad P=|v\rangle\langle v|,
\]
\[
 X=(1-q)|\psi\rangle\langle\psi|+qP,\qquad
 \rho=UXU^\dagger,\quad U=U_1\otimes U_2\otimes U_3\otimes U_4,\quad U_i\in U(2).
\]
Here and below every inequality includes the stated endpoints. For the actual physical qubit depolarizing channel
\[
 \Phi_p(A)=(1-p)A+\frac p2\operatorname{Tr}(A)I,\qquad 0\le p\le\frac43,
\]
put \(t=|1-p|\), \(b=(1-t)/2\), and
\[
 D_t=\operatorname{diag}\bigl((1+t)/2,(1-t)/2\bigr)^{\otimes4}.
\]
For an Hermitian matrix \(A\), write \(K_k(A)=\sum_{i=1}^k\lambda_i^\downarrow(A)\), \(1\le k\le16\). For every such \(C,q,U,p\), every integer \(k\in\{1,\ldots,16\}\), and every **one actual complex Hermitian rank-\(k\) projector** \(Q\),
\[
 \operatorname{Tr}[Q\Phi_p^{\otimes4}(\rho)]\le K_k(D_t)-(1-q)\,d_k(C)\,t^2b^2. \tag{1}
\]
The exact pure-H2 reference gap used in (1) is
\[
 d_k(C)=\begin{cases}
 k+3-\frac{k+1}{2}C,&1\le k\le3,\\
 k+3-(5-k)C,&4\le k\le5,\\
 k+3-\frac{(k-5)(4+C)}3,&6\le k\le8,\\
 k-1-C-(k-8)(\frac43-\frac C6),&9\le k\le11,\\
 10-C-(k-8)(\frac43-\frac C6),&12\le k\le14,\\
 16-k,&15\le k\le16.
 \end{cases} \tag{2}
\]
Every \(d_k(C)>0\) for \(1\le k\le15\), while \(d_{16}=0\). In particular, the coarser bounds in S1 are recovered: \(d_k\ge3\) for \(k\le5\), \(d_k\ge5\) for \(6\le k\le11\); additionally \(d_k\ge1\) for \(12\le k\le15\). Thus the output spectrum is majorized by the physical product reference in all 16 prefixes, strictly in every proper prefix whenever \(0<t<1\). Section 6 gives all output-prefix equality boundaries, including \(p=0,1,4/3\).

## 2. Actual one-, two-, and three-qubit partial traces

Write \(\omega=|\psi\rangle\langle\psi|\). Permutation symmetry means the following are the actual marginals for each subset of the indicated cardinality, with the corresponding qubit labels restored. Define
\[
 a=\frac{c^2}{6}+\frac{s^2}{2}=\frac{2-C}{6},\qquad r=\frac{c^2}{3}=\frac{1+C}{6}.
\]
The one- and two-body marginals are
\[
 \omega_1=I/2,\qquad
 \omega_2=\begin{pmatrix}a&0&0&0\\0&r&r&0\\0&r&r&0\\0&0&0&a\end{pmatrix}
 \quad(00,01,10,11). \tag{3}
\]
For the cross term, the one-body partial trace of \(|y\rangle\langle D|\) vanishes and the two-body one is
\[
 \operatorname{Tr}_{\overline{ij}}|y\rangle\langle D|
 =\frac{|00\rangle\langle11|+|11\rangle\langle00|}{\sqrt{12}},
\]
which is Hermitian. Hence the two cross terms of \(cD+is y\) cancel at two bodies; this cancellation depends on the actual phase, not an independently chosen marginal. For the mixed physical input,
\[
 X_1=\begin{pmatrix}(1+q)/2&0\\0&(1-q)/2\end{pmatrix},\qquad
 X_2=(1-q)\omega_2+q|00\rangle\langle00|. \tag{4}
\]

Let \(|D_3^h\rangle\) denote the normalized symmetric three-qubit weight-\(h\) ket. Explicitly decomposing the four-qubit ket across the traced qubit gives
\[
 |\psi\rangle=\frac1{\sqrt2}\left[
 (c|D_3^2\rangle+is|000\rangle)|0\rangle+
 (c|D_3^1\rangle+is|111\rangle)|1\rangle\right].
\]
The two displayed three-qubit vectors are orthonormal. In the basis \((|000\rangle,|D_3^1\rangle,|D_3^2\rangle,|111\rangle)\), extended by zero to the remaining four dimensions,
\[
 \omega_3=\frac12\begin{pmatrix}
 s^2&0&isc&0\\
 0&c^2&0&-isc\\
 -isc&0&c^2&0\\
 0&isc&0&s^2
 \end{pmatrix},\qquad
 X_3=(1-q)\omega_3+q|000\rangle\langle000|. \tag{5}
\]
In particular \(\operatorname{spec}(\omega_3)=(1/2,1/2,0^{\times6})\). The imaginary entries in (5) are not discarded.

## 3. Exact H2 spin spectra, all prefixes, and mixed ordering

For a density \(A\) define the actual embedded marginal sums
\[
 H_j(A)=\sum_{|S|=j}\operatorname{Tr}_{S^c}(A)\otimes I_{S^c},\qquad
 H_0(A)=I,\quad H_4(A)=A.
\]
Let \(J_\alpha=\frac12\sum_i\sigma_\alpha^{(i)}\) and let \(J_z|0\rangle=|0\rangle/2\) on each qubit. From (3), summing the actual two-qubit Pauli coefficients yields
\[
 H_2(DD^\dagger)=I+\frac13J^2-\frac12J_z^2,\qquad
 H_2(yy^\dagger)=I+\frac12J_z^2, \tag{6}
\]
\[
 H_2(\omega)=I+\frac{1+C}{6}J^2-\frac C2J_z^2,\qquad
 H_2(P)=I+\frac32J_z+\frac12J_z^2. \tag{7}
\]
For example, the \(D\) pair correlations are \((T_{xx},T_{yy},T_{zz})=(2/3,2/3,-1/3)\), and \(\sum_{i<j}\sigma_\alpha^{(i)}\sigma_\alpha^{(j)}=2J_\alpha^2-2I\); this proves the first identity rather than invoking an invariant-sector result. The second follows similarly from the \(y\) pair state. The product formula follows from its eigenvalue \(\binom{2+m}{2}\) on the \(J_z=m\) weight space.

Pairing the first two and the last two spins gives \((0\oplus1)\otimes(0\oplus1)=2\cdot0\oplus3\cdot1\oplus1\cdot2\). Thus \(m=-j,\ldots,j\), with multiplicity \(\mu_0=2,\mu_1=3,\mu_2=1\). The two operators in (6) have these simultaneous eigenvalues:

| \(j\) | \(m\) | \(H_2(DD^\dagger)\) | \(H_2(yy^\dagger)\) |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 1 | 0 | 5/3 | 1 |
| 1 | \(\pm1\) | 7/6 | 3/2 |
| 2 | 0 | 3 | 1 |
| 2 | \(\pm1\) | 5/2 | 3/2 |
| 2 | \(\pm2\) | 1 | 3 |

On the entire \(C\)-interval the **ordered** spectrum of \(H_2(\omega)\) is
\[
 \bigl(2+C,\ (2+C/2)^{\times2},\ (2-C)^{\times2},\
 ((4+C)/3)^{\times3},\ (4/3-C/6)^{\times6},\ 1^{\times2}\bigr). \tag{8}
\]
For example \(2-C-(4+C)/3=(2-4C)/3>0\), so no hidden branch crossing has been omitted. The product layer has ordered spectrum
\[
 (6,3^{\times4},1^{\times6},0^{\times5}),\quad
 R_k:=K_k(H_2(P))=\begin{cases}3k+3&1\le k\le5,\\k+13&6\le k\le11,\\24&12\le k\le16.\end{cases} \tag{9}
\]
Subtracting the prefix sums of (8) from (9) gives exactly the six branches in (2), including the \(k=16\) trace equality. These formulas directly verify each of the sixteen prefixes and their stated lower bounds.

For completeness the **actual mixed** \(H_2(X)\) is also diagonal in the same \((j,m)\) basis, with every eigenvalue
\[
 L_{jm}=1+\frac{(1-q)(1+C)}6j(j+1)
       +\frac{q-(1-q)C}{2}m^2+\frac{3q}{2}m, \tag{10}
\]
occurring \(\mu_j\) times. Its ordering can change as \((C,q)\) varies. An exact formula for every mixed prefix, valid even on all crossing surfaces, is
\[
 K_k(H_2(X))=
 \min_{\theta\in\{L_{jm}:j=0,1,2,\,-j\le m\le j\}}
 \left[k\theta+\sum_{j=0}^2\mu_j\sum_{m=-j}^j(L_{jm}-\theta)_+\right]. \tag{11}
\]
Consequently the exact mixed H2 gap is \(R_k\) minus (11). To see (11), order the 16 values with multiplicities: for a threshold between the \(k\)-th and \((k+1)\)-st values the displayed expression is their first-\(k\) sum, and every other threshold gives at least that sum. A threshold equal to a listed eigenvalue always suffices. This is a finite exact formula, not an assertion that one fixed ordering works in the whole box.

Further, for the actual \(X\), Ky Fan's variational principle and linearity give
\[
 R_k-K_k(H_2(X))\ge(1-q)[R_k-K_k(H_2(\omega))]=(1-q)d_k(C). \tag{12}
\]
Here \(K_k(A)=\max_{\mathrm{rank}\,Q=k}\operatorname{Tr}(QA)\): in an eigenbasis the diagonal projector weights lie in \([0,1]\) and sum to \(k\), so their maximum is the first-\(k\) eigenvalue sum. No invariant-sector input is needed for (6)–(12).

## 4. Actual H3 trace-square and layer comparison

Let \(A_i=\omega_{\bar i}\otimes I_i\) and \(B_i=P_{\bar i}\otimes I_i\). Equations (3) and (5) yield
\[
 \operatorname{Tr}\omega_2^2=2a^2+4r^2=\frac13+\frac{C^2}{6},\quad
 \operatorname{Tr}A_i^2=2\operatorname{Tr}\omega_3^2=1,\quad
 \operatorname{Tr}A_iA_j=\operatorname{Tr}\omega_2^2\ (i\ne j).
\]
The last identity is the physical partial-trace identity on the two qubits common to the embedded triples. Therefore
\[
 \operatorname{Tr}H_3(\omega)^2=4+12\operatorname{Tr}\omega_2^2=8+2C^2\le\frac{74}{9}. \tag{13}
\]
The corresponding **actual mixture** moment is also explicit. For equal indices,
\(\operatorname{Tr}A_iB_i=2\langle000|\omega_3|000\rangle=s^2\); for unequal indices, \(\operatorname{Tr}A_iB_j=\langle00|\omega_2|00\rangle=a\). Thus
\[
 \operatorname{Tr}[H_3(\omega)H_3(P)]=4s^2+12a=6-4C,
 \quad \operatorname{Tr}H_3(P)^2=20,
\]
\[
 \operatorname{Tr}H_3(X)^2=(1-q)^2(8+2C^2)+2q(1-q)(6-4C)+20q^2. \tag{14}
\]
This is not the square of a convexly averaged bound or a collection of independently selected marginals.

\(H_3(P)\) has spectrum \((4,1^{\times4},0^{\times11})\), hence prefixes \(4,5,6,7,8,\ldots,8\). Each \(A_i\) is positive and at most \(I/2\), so \(K_1(H_3(\omega))\le2\). For \(k=2,3,4\), Cauchy–Schwarz and (13) give
\[
 K_2\le\sqrt{148}/3<5,\quad
 K_3\le\sqrt{74/3}<6,\quad
 K_4\le\sqrt{296}/3<7.
\]
All later prefixes are at most \(\operatorname{Tr}H_3(\omega)=8\). Thus \(H_3(\omega)\prec H_3(P)\). Also \(H_1(\omega)=2I\prec H_1(P)\), since both traces are 32, and \(\omega\) and \(P\) are both rank-one densities. The \(H_0\) layers coincide. Every one of these statements refers to the actual state, not separately optimized local objects.

## 5. One common projector and all physical retentions

For \(0\le t\le1\), \(\Phi_{1-t}(A)=tA+b\operatorname{Tr}(A)I\). Expanding its four actual factors gives
\[
 \Phi_{1-t}^{\otimes4}(X)=\sum_{j=0}^4 t^j b^{4-j}H_j(X). \tag{15}
\]
If a computational basis word has weight \(h\), then the product reference layer \(H_j(P)\) has eigenvalue \(\binom{4-h}{j}\), understood as zero outside its natural range. All five layers have a common decreasing order by \(h\), so their weighted sum is exactly
\[
 \sum_jt^jb^{4-j}H_j(P)=D_t,\qquad
 K_k(D_t)=\sum_jt^jb^{4-j}K_k(H_j(P)). \tag{16}
\]

Fix a **single** arbitrary complex rank-\(k\) projector \(Q\). For every layer, using \(H_j(X)=(1-q)H_j(\omega)+qH_j(P)\) and the same \(Q\),
\[
 \operatorname{Tr}[QH_j(X)]\le(1-q)K_k(H_j(\omega))+qK_k(H_j(P))\le K_k(H_j(P)).
\]
For \(j=2\), (2) improves this inequality by \((1-q)d_k(C)\). Multiplying by the nonnegative coefficients in (15) and using (16) proves (1) for positive retention. Bounding several terms by their separate Ky Fan maxima is legitimate for this one \(Q\); the proof does **not** claim that their optimizers coincide. Coordering is used only for the actual product reference, where it gives equality, not for the input's different marginals.

For negative retention set \(Y_4=Y^{\otimes4}\). The identity \(YA^TY=\operatorname{Tr}(A)I-A\), valid for every complex \(2\times2\) matrix, gives
\[
 \Phi_{1+t}^{\otimes4}(X)=Y_4[\Phi_{1-t}^{\otimes4}(X)]^TY_4. \tag{17}
\]
The transpose is the **full four-qubit transpose**, not a partial transpose. Consequently
\[
 \operatorname{Tr}[Q\Phi_{1+t}^{\otimes4}(X)]
 =\operatorname{Tr}[(Y_4Q^TY_4)\Phi_{1-t}^{\otimes4}(X)]. \tag{18}
\]
Even for complex \(Q\), \(Y_4Q^TY_4\) is one Hermitian rank-\(k\) projector, used unchanged in every layer and both mixture components. Physical negative retention corresponds exactly to \(0\le t\le1/3\); (1) follows from the positive-retention calculation with this transported projector.

Finally, every local unitary preserves the physical expansion: \(H_j(UXU^\dagger)=UH_j(X)U^\dagger\), and \(\Phi_p^{\otimes4}(UXU^\dagger)=U\Phi_p^{\otimes4}(X)U^\dagger\). Thus a projector consuming \(\rho\) is transported to \(U^\dagger QU\), with no assumption of a common local normal form. This holds for all \(U_i\in U(2)\), all endpoints and both retention signs.

## 6. Exact output equality boundaries

For \(0<t<1\), (1) and \(q\le1/8\) give strict inequality between output and reference for every \(k=1,\ldots,15\). Rank 16 is always equality because both outputs have trace one. Thus this strictness includes \(p=4/3\), where \(t=b=1/3\) and each proper-prefix gap is at least \((1-q)d_k(C)/81\). At \(p=1\), \(t=0\) and both matrices are exactly \(I/16\), so every prefix is equality.

At \(p=0\), the output is \(\rho\) and \(D_1=P\). The nonzero eigenvalues of \(X\), counting the vanishing second eigenvalue at \(q=0\), are
\[
 \lambda_\pm=\frac{1\pm\sqrt{1-q(1-q)(3+C)}}2. \tag{19}
\]
Indeed \(|\langle v|\psi\rangle|^2=s^2/2=(1-C)/4\), giving the rank-two determinant \(q(1-q)(3+C)/4\). If \(q=0\), both the output and reference are rank one and every prefix is equality. If \(0<q\le1/8\), the output has rank two, so the first-prefix gap is \(1-\lambda_+>0\) and prefixes \(k\ge2\) are equal. These cases, \(p=1\), the strict interior statement above, and rank 16 exhaust output-prefix equality possibilities in the quantified family. The endpoint values \(C=1/6,1/3\) and \(q=0,1/8\) require no limiting argument; (2), (10), and the physical projector proof include them literally.

## 7. Defect, genuine entanglement, and comparison limits

Let \(\Theta_4=Y_4K\), where \(K\) is full computational-basis complex conjugation, and \(\widetilde X=Y_4X^TY_4\). With \(z=(|0000\rangle-|1111\rangle)/\sqrt2\), the actual defect \(\Delta=(X-\widetilde X)/2\) in the orthonormal basis \((D,y,z)\), with zero on its complement, is
\[
 \begin{pmatrix}0&-i(1-q)cs&0\\i(1-q)cs&0&q/2\\0&q/2&0\end{pmatrix}.
\]
Its nonzero eigenvalues are \(\pm\sqrt{(1-q)^2c^2s^2+q^2/4}\), giving the exact physical trace-norm defect
\[
 d^2:=\|\Delta\|_1^2=q^2+(1-q)^2(1-C^2)\ge\frac{401}{576}>\frac3{13}. \tag{20}
\]
For the minimum use \(1-C^2\ge8/9\); \(q^2+(8/9)(1-q)^2\) decreases on \([0,1/8]\), and at the endpoint it equals \(401/576\). For \(q=0\), \(\eta=|\langle\psi|\Theta_4\psi\rangle|^2=C^2\in[1/36,1/9]<55/72\). Thus the numerical sufficient thresholds described in S2 do not cover these inputs: at \(q>0\) the input has rank two and the pure-input criterion is inapplicable. No conclusion is drawn here about exclusion from the convex hull of S2's entire pure sufficient region.

For a stronger, separately defined hull statement, let \(\mathcal H\) be the convex hull of all pure biseparable rays, all pure \(\eta=0\) rays and all pure \(\eta=1\) rays. Every spin-flip-invariant mixed state belongs to it, because an antiunitary involution admits a fixed real orthonormal basis and its invariant density is real symmetric in that basis. This enlarged hull contains the specific classes named in S2, conditional only on those classes having the stated biseparable/\(\eta\)-class definitions; it does not assert their channel property.

To show \(X\notin\mathcal H\), set \(W=\operatorname{span}\{\psi,v\}\). For any \(A\ne0\), the ket \(A\psi+Bv\) is entangled across every 1|3 cut: its two coefficient rows have disjoint three-bit weight supports \(\{0,2\}\) and \(\{1,3\}\), and their Dicke terms are both nonzero. Across every 2|2 cut, its rows/columns split into a nonzero \((01,10)\) block and a separate \((00,11)\) block with nonzero off-diagonal \(Ac/\sqrt6\); hence the coefficient matrix has rank at least two. Consequently the only biseparable ray in \(W\) is \(v\).

The only other \(\eta=1\) and \(\eta=0\) rays in \(W\), up to scalar, are respectively
\[
 x_I=\psi-i\sqrt2\,s\,v,\qquad x_N=\psi+i\frac C{\sqrt2s}v.
\]
For the first, equality in \(|\langle x|\Theta_4x\rangle|\le\|x\|^2\) forces \(\Theta_4x\) proportional to \(x\), and the \((D,y,z)\) coefficients uniquely give the displayed ray. For the second, the exact bilinear form is
\[
 (A\psi+Bv)^TY_4(A\psi+Bv)=A^2C+i\sqrt2\,ABs,
\]
so its only non-\(v\) zero is \(x_N\). All denominators are nonzero in the closed parameter box.

If \(X\in\mathcal H\), positivity forces every constituent ray into \(\operatorname{range}X\subseteq W\). In the linearly independent coordinate basis \((\psi,v)\), absorb normalizations into nonnegative \(\alpha,\beta,\gamma\) and compare
\[
 X=\alpha|x_I\rangle\langle x_I|+\beta|x_N\rangle\langle x_N|+\gamma|v\rangle\langle v|.
\]
The three coordinate equations give
\[
 \alpha+\beta=1-q,\quad \alpha\sqrt2s=\beta C/(\sqrt2s),\quad
 q=\alpha(2s^2)+\beta C^2/(2s^2)+\gamma=(1-q)C+\gamma.
\]
But \(q/(1-q)\le1/7<1/6\le C\), contradiction. This argument includes \(q=0\), where the actual support is only \(\mathbb C\psi\). Thus every family member is genuinely four-party entangled and lies outside this enlarged hull. Local unitaries preserve biseparability and \(\eta\), and satisfy \(\widetilde{UXU^\dagger}=U\widetilde XU^\dagger\); hence (20) and the hull conclusion hold for every allowed \(U\).

## 8. Import boundaries and read/process declaration

* Literal scientific input was exactly part 01, in ordered raw windows 1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–260, and 261–276, including its ending. Parent-supplied whole-part size is 27,230 bytes, so each window is below 30,000 bytes; no packet clipping was displayed. The packet contains the complete rendered S1 LF 1–219 and S2 LF 1–47. Parent-supplied SHA-256 pins are part `5cc20c2d1bd4ccc8ae95dc40dfce934e9dc9aae66147352a651cade9b7ceb826`, S1 `098435386c86deeb036faa455fe17ca43ae613fc25a2cc62060a4cbb6b63fcd2`, and S2 `4d9f3d97723cafe956eaf7c151506249e08c246bb35b59436fe64b015558eaff`; these are supplied metadata, not hashes independently recomputed here.
* Before any packet-body reading or target reasoning I read the manifest, freeze receipt, final binding, parent-live metadata, actual dispatch receipt, and all 22 manifest-listed status-only controls, wrote `prebody-ack-v1.md`, and sent the direct prebody acknowledgement to Main. Initial non-raw administrative displays elided blocks; full raw administrative rereads recovered them before the acknowledgement. A separately displayed general memory summary clipped long advisory lines and was not used as mathematical input. Required skills were procedural context only.
* The linked invariant-sector theorem body in S2 was not supplied and was not opened. S2 itself identifies that import as load-bearing for its general small-defect H2 argument; its prior-region/hull naming and historical review descriptions are comparison metadata here, not premises silently used in (1)–(19). Any separate claim about that linked theorem or the earlier classes' channel properties remains conditional on those unprovided bodies. Elementary finite-dimensional variational, Cauchy–Schwarz, trace and angular-momentum identities used above are explicitly stated/derived at the needed interface.
* No source links were followed, no genuine held episode or any proof/method/selection/planning/verification/reporting/confidence/downstream consumer was used, and no scientific program, subprocess, solver, test, compilation, network or external model was run. No verifier source was prepared, so there is no prepared-code hash. This author candidate is not itself a disjoint check or parent disposition.
