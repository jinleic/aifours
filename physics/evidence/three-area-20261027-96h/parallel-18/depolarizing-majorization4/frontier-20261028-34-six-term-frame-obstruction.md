# Six-term genuinely entangled witness against the third-frame-eigenvalue shortcut

This is a simpler **separate exact witness to the same auxiliary falsification** as `frontier-20261028-32-complex-third-frame-obstruction.md`; the earlier complex witness remains unchanged. It disproves \(\lambda_3(F(\rho))\le2\), where \(F(\rho)=\sum_{i,a}\sigma_i^a\rho\sigma_i^a\). It is **not** an original-channel counterexample and does not refute the still-unproved \(\|F(\rho)\|_{(3)}\le8\). No novelty, formal or independent-family acceptance is claimed.

## Physical state, actual rank-three subspace and full frame spectrum

Take
\[
|\psi\rangle=\frac13\bigl(2|0000\rangle+|0101\rangle+|0110\rangle
+|1001\rangle+|1010\rangle+|1111\rangle\bigr),\qquad \rho=|\psi\rangle\langle\psi|.
\]
It is normalized. The exact coefficient-matrix ranks across the four one-versus-three cuts are `(2,2,2,2)` and across the three two-versus-two cuts with the first party on the left are `(3,4,4)`. Thus it is genuinely multipartite entangled, not a product or relaxed negative block.

In computational-basis even/odd parity order, exact Pauli conjugation gives two independent parity blocks. The nonzero even blocks of \(9F(\rho)\) are
\[
\begin{pmatrix}16&-8\\-8&4\end{pmatrix},\qquad
\begin{pmatrix}4&-4\\-4&4\end{pmatrix},\qquad
\begin{pmatrix}4&-4\\-4&4\end{pmatrix},
\]
with two additional zero directions. The odd block consists of two copies of
\[
M=\begin{pmatrix}12&4&6&6\\4&12&6&6\\6&6&6&4\\6&6&4&6\end{pmatrix}
\]
divided by9. On \((1,-1,0,0)\) and \((0,0,1,-1)\), \(M\) has eigenvalues8 and2. On the two-dimensional symmetric subspace \((a,a,b,b)\), its matrix is \(\left(\begin{smallmatrix}16&12\\12&10\end{smallmatrix}\right)\), with eigenvalues \(13\pm3\sqrt{17}\). Therefore
\[
\operatorname{spec}F(\rho)=
\left(\frac{13+3\sqrt{17}}9\right)^{(2)},\quad
\left(\frac{20}9\right)^{(1)},\quad
\left(\frac89\right)^{(4)},\quad
\left(\frac29\right)^{(2)},\quad
\left(\frac{13-3\sqrt{17}}9\right)^{(2)},\quad 0^{(5)}.
\]
The displayed order is descending. In particular,
\[
 \lambda_3(F)=\frac{20}9>2,\qquad
 \|F(\rho)\|_{(3)}=\frac{46+6\sqrt{17}}9<8.
\]
The strict last inequality follows from \(\sqrt{17}<13/3\); it does not establish that inequality for other inputs.

An explicit actual rank-three projector can be formed from the three pairwise orthogonal vectors
\[
\begin{aligned}
w_0&=-2|0000\rangle+|1111\rangle,\\
w_1&=3(|0001\rangle+|0010\rangle)+2(|0111\rangle+|1011\rangle),\\
w_2&=3(|0100\rangle+|1000\rangle)+2(|1101\rangle+|1110\rangle),
\end{aligned}
\]
with squared norms5,26,26. Put \(P=\sum_{j=0}^2|w_j\rangle\langle w_j|/\|w_j\|^2\). The exact compressed matrix \(W^\dagger(F-2I)W\), \(W=(w_0,w_1,w_2)\), is diagonal with entries \(10/9,188/9,188/9\), so the third frame eigenvalue exceeds2 by min–max. Direct exact multiplication gives \(\operatorname{Tr}[PF]=916/117\). This physical real projector is a valid complex-space rank-three projector; no relaxation is used.

## Original-channel check and limits

At each physical \(p=2/3,4/3\), the exact checker independently compares the full original Pauli Kraus mixture with sequential local partial traces, and verifies 16 positive exact LDL pivots both for the output and for \((13/100)I-\Lambda_p(\rho)\). Therefore the output is physical and its top-three eigenvalue sum is strictly less than \(39/100<32/81\), the exact product-reference top3. The rigorous margin is strictly greater than \(41/8100\). The **same specified** \(P\) has exact original-channel trace `12836/47385` at \(2/3\) and `10181/47385` at \(4/3\). NumPy's observed top three at \(2/3\) were approximately `(0.12540917996177292,0.08779149519890266,0.08779149519890259)`, sum `0.30099217035957815`; these decimals are not the exact bound.

## Evidence

`frontier-20261028-33-simple-frame-witness.py`, SHA256 `09bf7cadefdfe1c3638b27b5ca79d21de5ff62dc1bb644b9c74061b3fee993b3`, ran as `env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B ...` from the repo root and exited0. It uses the previously pinned exact Gaussian-rational helpers and verifies the input purity, all seven representative cut ranks, all entries of the two parity blocks, the displayed compressed matrix and actual projector, and both exact original-channel LDL certificates; NumPy is used only for labelled decimal eigenvalues. Native clock after pin **Wed Oct 28 17:50:19 PDT 2026**. The finite code and written block decomposition do not resolve the general first/second-erasure inequalities or the original full k3 problem.
