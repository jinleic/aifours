# Full all-noise original k3 for the complementary-W five-code: written candidate

**HIGH-CONSEQUENCE AUTHOR-WRITTEN CANDIDATE — NOT ADOPTED.** Let `|bar i>` be the four-bit word with a single zero at site i. For every complex normalized pure state in

\[
\mathcal C=\operatorname{span}\{|0000\rangle,|\bar1\rangle,|\bar2\rangle,|\bar3\rangle,|\bar4\rangle\},\tag{1}
\]

and every physical noise `0<=p<=4/3`, the written argument below gives the ORIGINAL four-qubit k3 comparison against a pure product input, for every actual complex rank-three projector. It extends by fixed-projector affinity to every mixed density supported on this code, physical local-unitary/permutation images, and their actual convex hull. There is **no** cutoff on the vacuum weight, individual amplitudes or phases. This is not unrestricted global k3, full majorization, novelty, formal/kernel/human/stronger-family acceptance, or a cure of historical process findings; it requires complete disjoint written review.

This five-code is vacuum plus **three** excitations; it is not assumed to be the previously supported vacuum-plus-**single**-excitation code. Applying global bit flip produces the full-weight word plus single excitations, not vacuum plus singles. A concrete GME input outside several earlier named families and outside the previous moment-limited regions appears in §6.

## 1. Actual-state coordinates and sufficient layer interface

Write, after one harmless global phase,

\[
|\psi\rangle=a|0000\rangle+\sum_{i=1}^4g_i|\bar i\rangle,
\qquad a\ge0,\quad A=a^2,\quad w_i=|g_i|^2,\quad B=\sum_iw_i,\quad A+B=1.
\tag{2}
\]

All terms of distinct support differ in at least two bit positions, so each actual one-qubit marginal is diagonal, with probability `B-w_i` for `|1>`. This is true for arbitrary complex phases. Define

\[
F(\rho)=\sum_{i,a=x,y,z}\sigma_i^a\rho\sigma_i^a,\quad
H_1(\rho)=\sum_i I_{\bar i}\otimes\rho_i,\quad
\widetilde\rho=Y^{\otimes4}\rho^TY^{\otimes4}.
\]

The following exact actual-input bounds, proved in §§2–4, are enough:

\[
K_3(F(\rho))\le8,\qquad
K_3(H_1(\rho)+\widetilde\rho)\le10.\tag{3}
\]

Indeed, for the SAME actual rank-three Q, the physical erasure identities

\[
T_1=\rho+F/4,\qquad
4T_2=H_1+\rho+\widetilde\rho+F/2-I
\]

give `Tr QT1<=1+8/4=3` and `4 Tr QT2<=10+1+4-3=12`. Also `Tr Qrho<=1`, `Tr QT3<=5/4`, and `Tr QT4=3/16`. For `0<=p<=1`, multiplying the same-Q bounds by the nonnegative erasure coefficients gives the fixed product-reference layer sequence `(1,3,3,5/4,3/16)` and hence the original product top3. The three-erasure bound is direct: its eigenvalues are `(4+sum_i +/- r_i)/16`, so the top-three sum is `(12+r1+r2+3r3+3r4)/16<=5/4` for sorted local radii. The exact full-transpose spin-flip identity then carries the comparison to `1<=p<=4/3`; it is not a partial transpose. This proof never combines state-dependent bounds from different Qs.

## 2. Exact three-block Pauli frame for ALL complex amplitudes

The elementary local Pauli twirl gives, for computational matrix units `|x><y|` with Hamming distance d,

\[
F(|x\rangle\langle y|)=(4-2d)|x\rangle\langle y|
 +2\sum_{i:x_i=y_i}|x\oplus e_i\rangle\langle y\oplus e_i|.\tag{4}
\]

Consequently `F(rho)` is block diagonal on the three indicated, mutually orthogonal excitation sectors: weights `(0,3)`, weights `(1,4)`, and weight `2`. Put `g=(g_1,...,g_4)^T`, `D=diag(w_i)` and `m=max_i w_i`. In the ordered basis `|0>,|bar1>,...,|bar4>`,

\[
F_0=\begin{pmatrix}4A&-2a g^\dagger\\-2a g&4D\end{pmatrix},
\qquad\operatorname{Tr}F_0=4.\tag{5}
\]

In the basis `|e1>,...,|e4>,|1111>`, the weight `(1,4)` block is

\[
F_1=\begin{pmatrix}2A I_4&2a\overline g\\2a\overline g^\dagger&2B\end{pmatrix},
\quad\operatorname{spec}F_1=\{2,(2A)^{\times3},0\}.
\tag{6}
\]

For the six weight-two words `|bar{ij}>` and a 6-by-4 matrix V with `V_{(ij),i}=g_j`, `V_{(ij),j}=g_i` and other entries zero,

\[
F_2=2VV^\dagger,\quad V^\dagger V=G=B I_4+g g^\dagger-2D,
\quad \operatorname{Tr}F_2=6B.\tag{7}
\]

The nonzero spectra of `VV^dagger` and G agree; zero amplitudes create no division. For all complex g, a 2-by-2 Rayleigh bound on (5) gives

\[
\lambda_1(F_0)\le L_0:=2(A+m)+2\sqrt{(A-m)^2+AB}.\tag{8}
\]

Because `G=B I+(g g^dagger-2D)`, the rank-one-positive matrix `H=g g^dagger-2D` has at most one positive eigenvalue. In fact

\[
\lambda_1(H)\le\frac43(B-m).\tag{9}
\]

If `B=m`, H is nonpositive. Otherwise let `d=B-m>0`. If its top eigenvalue h is positive, the rank-one secular equation is `sum_i w_i/(h+2w_i)=1`, with zero weights omitted. The function `x/(h+2x)` is concave and increasing in x. At `h0=4d/3`, the three nonmaximal terms sum to at most `d/(h0+2d/3)=1/2`, while the maximal term is at most `1/2`. Since the secular sum decreases in h, `h<=h0`. This proves (9) without assuming a normal form for g or dropping phases.

It follows that

\[
\lambda_1(F_2)\le(14B-8m)/3,\quad
K_2(F_2)\le(20B-8m)/3,\quad
K_3(F_2)\le6B.\tag{10}
\]

The first two also give the simpler respective bounds `4B` and `6B` since `m>=B/4`. The total F0 trace gives `K2(F0),K3(F0)<=4`.

## 3. All rank allocations give the full frame bound

The only allocations needing the coupled bound L0 rather than just a block trace are `(one from F0, one from F1, one from F2)` and `(one from F0, none from F1, two from F2)`. Both are bounded by 8. Specifically,

\[
L_0+2+(14B-8m)/3\le8,\qquad
L_0+(20B-8m)/3\le8.\tag{11}
\]

For the first, it suffices to show

\[
\sqrt{(A-m)^2+AB}\le(6-4B+m)/3.
\]

The right side is positive. Nine times the squared difference is

\[
P_1=27-39B+16B^2+(30-26B)m-8m^2.
\]

It is concave in `m in [B/4,B]`; its endpoints are

\[
P_1(B,B)=9(1-B)(2B+3),\quad
P_1(B,B/4)=\tfrac92(6-7B+2B^2),
\]

both nonnegative for `0<=B<=1`. For the second inequality, the positive right side is `(9-7B+m)/3`; nine times the squared difference is

\[
P_2=72-117B+49B^2+(36-32B)m-8m^2,
\]

whose concave-m endpoints are `9(1-B)(8-B)` and `(9/2)(4-3B)^2`. Thus (11) includes both boundary equalities and all intermediate B,m.

All other total-rank-three block allocations are bounded directly: `K3(F0)<=4`; `K2(F0)+K1(F1)<=6`; `K2(F0)+K1(F2)<=4+4B<=8`; `K1(F0)+K2(F1)<=4+2+2A<=8`; `K3(F1)<=2+4A<=6`; `K2(F1)+K1(F2)<=2+2A+4B<=6`; `K1(F1)+K2(F2)<=2+6B<=8`; and `K3(F2)<=6B<=6`. Together with (11), these exhaust every distribution of three eigenvalues among the three actual blocks, proving

\[
K_3(F(\rho))\le8\quad\text{for every state in (1)}.\tag{12}
\]

No individual-eigenvalue bound `lambda2(F)<=2` or `lambda3(F)<=2` is used; such assertions are false for other actual states.

## 4. The full spin-flip bound for ALL vacuum weights

For every pure four-qubit state, `H1(sigma)>=2sigma` by the four local-Schmidt-rank-two bounds. With `sigma=tilde rho`,

\[
H_1(\rho)+\widetilde\rho=4I-[H_1(\sigma)-\sigma],
\]

so its largest eigenvalue is at most 4. If the sum `s` of sigma's **actual local minority probabilities** is at least 1, its second eigenvalue is at most 3: `H1(sigma)-I>=0`, and subtracting the rank-one sigma creates at most one negative eigenvalue. The same is true for a product input.

For `0<s<1`, use the actual sigma majority eigenbasis and write `P_x` for the SAME state's computational probabilities. The pure-qubit marginal polygon guarantees that the positive-sector denominators below are nonnegative and that any zero denominator carries zero probability. A one-negative-pivot Schur complement, fully described in the consolidated packet `frontier-20261028-121-consolidated-physical-k3.md` §3, gives the exact criterion

\[
\lambda_2(H_1(\rho)+\widetilde\rho)\le3
\iff
\sum_{x\ne1111}\frac{P_x}{3-s-\sum_{i:x_i=1}r_i}
\le1+\frac{P_{1111}}{1-s},\tag{13}
\]

where zero denominators with zero numerator are omitted and `r_i=1-2p_i` in that actual majority basis. We verify (13) in all remaining cases from the special support (2).

For the physical basis bookkeeping, first conjugate `sigma=tilde rho` by `X^tensor4`. The exact identity `X^tensor4 sigma X^tensor4=Z^tensor4 conjugate(rho) Z^tensor4` shows that the resulting computational probabilities are those of the original rho, with unchanged local bit-one probabilities `B-w_i`; conjugation only changes phases. We then apply X on exactly those sites where `B-w_i>1/2`. These are actual local unitaries on sigma, not a new independently chosen distribution.

First suppose `0<B<1/3`. All original minority probabilities are `B-w_i<1/2`, so after the common spin-flip/majority-axis rotation the support remains weight 0 plus weight 3. It has `s=3B`, `P0=A`, `P_bar_i=w_i`, `P1111=0`, and the left side of (13) is

\[
\frac{A}{3A}+\sum_i\frac{w_i}{B+2w_i}
=\frac13+\sum_i\frac{w_i}{B+2w_i}\le1.\tag{14}
\]

The last inequality is Jensen for the concave function `x/(1+2x)` applied to `w_i/B`, whose sum is one; it remains valid if some weights vanish.

For `1/3<=B<=2/3`, the minority-probability sum is at least one. Indeed each local bit-one probability is `B-w_i`, and `min(x,1-x)` is concave. The sum of the four minima, as a function of `w` on the simplex `w_i>=0,sum w_i=B`, is concave and hence at least its value at a vertex `(B,0,0,0)`, namely `3 min(B,1-B)>=1`. Therefore the preceding rank-one inertia argument applies, including all ties `B-w_i=1/2`.

Finally let `2/3<B<=1`. If `s>=1` or `s=0` we are already done. Otherwise `0<s<1` and the pure marginal polygon makes all actual minority axes nondegenerate. Let h be the number of sites where the original bit-one probability `B-w_i` exceeds one half, so those sites are physically flipped to their majority basis. `h=0` would imply `B<=2/3`; for `h=1,2,4`, respectively,

\[
s=B+1+2\sum_{\rm flipped}w_i\ge1,\quad
s=2-B+2\sum_{\rm flipped}w_i\ge1,\quad
s=4-3B\ge1.
\]

Hence only `h=3` is possible. Let i be the unique unflipped site, `m=w_i`, `d=B-m`. After those three physical flips, the SAME state's probabilities have support `P0=m`, `P_{ij}=w_j` for `j!=i`, and `P_bar_i=A=1-B`; there are no weight-one or weight-four entries. The actual minorities are `p_i=d`, `p_j=A+w_j`, and `s=3A+2d<1`. The denominator at zero is `3-s=B+2m`, at `|ij>` is `B+2w_j`, and at `|bar i>` is `3A`. Thus (13)'s left side is

\[
\mathbf1_{A>0}/3+\sum_{k=1}^4\frac{w_k}{B+2w_k}\le1.
\tag{15}
\]

When `A=0` the zero numerator/denominator term is omitted, and the sum is at most `2/3`; when B=0 the input is product. Every equality/tie and `s=1` endpoint was handled separately. Therefore `lambda2(H1+tilde rho)<=3` and `K3(H1+tilde rho)<=10` for the entire complex code, establishing the second part of (3).

## 5. Original all-p and mixed/LU hull conclusion

Sections 2–4 prove both actual same-input bounds in (3). The exact erasure, full-transpose mirror and same-Q affine steps in §1 prove the stated original comparison for every pure vector in the five-code and all `0<=p<=4/3`. Every density supported on the code is a finite convex combination of such pure vectors; fix the same actual Q while averaging. Local channel covariance permits all physical local-unitary and site-permutation images, and the same fixed-Q argument covers their convex hull. This is the complete stated family, not a truncated parameter chart, a numerical extrapolation or global four-qubit majorization.

## 6. Exact physical diagnostic beyond the previous moment regions

`frontier-20261028-122-complementary-w-check.py`, SHA256 `fb8bbafb5fb6a088c22ea0c5ceee148fc625b062e3c03d31cb242e32ff328e43`, ran `python3 -B` with single-threaded BLAS, exit0. Exact Fraction/Gaussian-rational arithmetic checks the entire three-block identity (5)–(7) for five actual pure inputs including complex phases, `B=0`, `B=1`, and a high-B three-flip case. Finite examples do **not** prove the uniform block/allocation/Jensen argument.

For the explicit GME input

\[
(5|0000\rangle+2|0111\rangle+|1011\rangle+|1101\rangle+|1110\rangle)/\sqrt{32},
\]

the program verifies seven cut ranks `2,2,2,2,3,3,3`, local radii `(13/16,5/8,5/8,5/8)`, `S=469/256`, and `C=0`; hence `4S=469/64>64/9`. It is outside the moment-limited 120/118 regions, has unequal radii and thus is outside 114, and its nondegenerate Z marginals with mixed support parity exclude the named PAR/paired-parity family. Unequal radii exclude LU-symmetric states; a rank-three 2|2 cut excludes the general-W single-excitation LU family. Its `(1,2)|(3,4)` Schmidt squared values are `25/32,5/32,2/32,0`, so product overlap is at most `25/32<124/125`, outside the named old near-product region. Other prior F2/covariance/regional tests are not assessed; there is no exhaustive novelty claim.

For this exact state, LDL/inertia bounds certify the auxiliary frame top3 below `17/5+201/100+8/5=701/100<8`. At `p=2/3` and `4/3`, exact sequential/Pauli channel matrices agree, LDL gives `lambda1<17/100`, inertia `(15,1,0)` gives `lambda2<9/100`, and true original top3 is `<7/20<32/81`, with certified gap `73/1620`; the same actual test projector has exact trace `1/3`. These are finite diagnostics, not the all-p proof. Native evidence-pin clock `Wed Oct 28 21:43:11 PDT 2026`.

A disjoint review must reconstruct **every** coefficient and complex conjugation in (4)–(7), the secular/Jensen and rank-allocation bounds (including zero weights), the actual local-basis/h3-flip harmonic cases and boundary endpoints, and the common-Q/erasure/physical-reflection/mixed-hull application. All previous process and quarantine dispositions remain unchanged.
