# An actual-projector region for the rank-three spin-flip inequality

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** This packet proves the second operator target from `frontier-20261028-106-physical-rank3-dual-obstruction.md`, namely `H1(Q)+tilde Q<=10I`, for an explicit, nontrivial **region of actual complex rank-three projectors**. It does not prove that operator bound for all Q, does not prove the separate frame bound `F(Q)<=8I`, and does not close global original k3. An explicit physical projector outside all stated cases is supplied in §4; its being outside is not a violation. No novelty, formal/human/stronger-family acceptance, or process-history cure is claimed.

## 1. Statement and exact dual equivalence

For an actual rank-three orthogonal Q, independently rotate the four local bases to write each marginal as

\[
\operatorname{Tr}_{\bar i}Q=\tfrac32I+\tfrac{m_i}{2}Z_i,
\quad m_i\ge0,\quad S=\sum_i m_i.
\]

These rotations are physical local unitaries; if an `m_i=0`, any axis may be chosen at that site. The trace variational principle gives `S<=8`, because the top three eigenvalues of `sum_i Z_i` are `4,2,2`. Put `c=(S-6)/2` when `S>6`.

**Claim.** Each of the following conditions implies the actual operator inequality

\[
H_1(Q)+\widetilde Q\le10I,\qquad
H_1(Q)-Q\ge2I,\tag{1}
\]

where `H1(Q)=sum_i I_bar_i tensor Tr_bar_i Q` and `tilde Q=Y^tensor4 Q^T Y^tensor4`:

1. `S<=6`;
2. `6<S<=8` and `min_i m_i>=3c/2`;
3. in one such rotated local basis, the range of Q is contained in the span of the computational words of Hamming weight at most two.

At `S=8`, condition 3 automatically holds and the inequality follows regardless of condition 2. Full spin flip carries the first inequality in (1) into the second, because `tilde(H1(Q))=12I-H1(Q)` and spin flip is a positive involution. Thus either form is sufficient for the other; no partial transpose is used.

## 2. Proof for the scalar region

In the rotated basis,

\[
D:=H_1(Q)-2I=4I+\tfrac12\sum_i m_i Z_i.
\]

If `S<=6`, then `D>=I>=Q` and (1) is immediate. Assume `6<S<=8`; then `0<c<=1`. Set `E=|1111><1111|` and `q=Tr(QE)`. If `min_i m_i>=3c/2`, the diagonal value of D at `E` is `1-c`, whereas every other diagonal value is at least `1-c+3c/2=1+c/2`. Consequently

\[
D-Q\ge(I-Q)-cE+\tfrac c2(I-E).\tag{2}
\]

Let `N=sum_i(I-Z_i)/2` and `E0=|0000><0000|`. The exact diagonal inequality `N>=I-E0+3E` and `Tr Q=3` give

\[
3-c=\operatorname{Tr}(QN)
\ge3-\operatorname{Tr}(QE0)+3q\ge2+3q,
\quad q\le(1-c)/3.\tag{3}
\]

The right side of (2) is PSD. To see this, on the span of `e=|1111>` and `Qe`, Q has the usual projection matrix with diagonal `q,1-q` and off-diagonal magnitude `sqrt(q(1-q))`. The two diagonal entries of the right side of (2) are `1-q-c` and `q+c/2`; its determinant is

\[
\frac c2[(1-c)-3q]\ge0.
\]

Both diagonals are nonnegative under (3). The orthogonal complement is invariant under Q and E and has `(I-Q)+(c/2)I>=0`. The `q=0` and `c=1` endpoints follow directly from the same inequality; no inverse or division by `1-c` is used. Thus `D-Q>=0`, proving (1) in condition 2.

## 3. Proof for local low-weight support and S=8

Suppose the range of Q lies in the locally rotated subspace of Hamming weight at most two. For any pair of distinct sites,

\[
m_i+m_j=\operatorname{Tr}[Q(Z_i+Z_j)]\le6,
\]

since the rank-three top trace of `Zi+Zj` is `2+2+2`. If `S>6`, the diagonal value of D on a word with one-set T of size at most two is

\[
4+S/2-\sum_{i\in T}m_i\ge S/2-2>1.
\]

If `S<=6`, D is already at least I. Thus in either case `D>=I` on the weight-at-most-two subspace; on its orthogonal complement `Q=0` and D is positive because `S<=8`. Hence `D-Q>=0` on the whole physical Hilbert space.

At `S=8`, equality in the rank-three Ky Fan bound forces Q to contain the unique weight-zero top vector and to have its other two dimensions inside the weight-one eigenspace of `sum_i Zi`; consequently condition 3 applies. No all-projector extension follows from this boundary case.

## 4. Exact covered and uncovered physical projectors

`frontier-20261028-111-spinflip-region-check.py`, SHA256 `7938b6f0219b6afcf4b30534474640688283b5e6cca239181dc79bc13ef2f671`, ran with `python3 -B` and single-threaded BLAS, exit0. It constructs the actual rank-three projector

\[
Q_{\rm in}=\operatorname{proj}\operatorname{span}\left\{
(12|0000\rangle+5|1111\rangle)/13,\ |0001\rangle,\ |0010\rangle\right\}.
\]

Its exact positive local magnitudes are `(457,457,119,119)/169`; `S=1152/169`, `c=69/169`, `m_min-3c/2=31/338>0`, and `q=25/169<(1-c)/3`. Exact Gaussian-rational LDL gives all 16 positive pivots for the projector lemma in (2) and for `H1(Q_in)-Q_in-2I`. It also gives all 16 positive pivots of `8I-F(Q_in)`. Therefore BOTH sufficient targets of 106 hold for this specific actual Q, and the common-Q erasure calculation there proves the original k3 dual comparison for `Q_in` at **every** physical noise and every input. As a separate finite check, exact Pauli/sequential outputs agree and `(3/8)I-Phi_p^tensor4(Q_in)` has 16 positive LDL pivots at `p=2/3,4/3`, below the product `32/81`.

The same program constructs a different actual rank-three Q outside the present proof region:

\[
Q_{\rm out}=\operatorname{proj}\operatorname{span}\left\{
(24|0001\rangle+7|1110\rangle)/25,\ |0000\rangle,\
(|0011\rangle+|0100\rangle)/\sqrt2\right\}.
\]

Its local axes are nondegenerate with magnitudes `(1777,1152,1152,98)/625`; `S=4179/625>6`, `c=429/1250`, and `m_min<3c/2`. It has exact weight-three occupation `49/625`, so it is not covered by condition 3 in its unique local eigenbases. The program nevertheless certifies `H1(Q_out)-Q_out-2I>0` by 16 positive exact LDL pivots. Thus this is a **coverage boundary**, not a counterexample to (1), and it shows no false global conclusion is being drawn. Native checker-pin clock `Wed Oct 28 21:08:22 PDT 2026`.

The true global task remains the second target (1) beyond these physical regions together with the separate first frame target, or a genuine original-channel counterexample. The fixed-minority global strengthening in packet 110 is already exactly false and is not used here.
