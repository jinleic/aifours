# An exact physical harmonic criterion for the spin-flip dual and original k3

**HIGH-CONSEQUENCE WRITTEN AUTHOR CANDIDATE — NOT ADOPTED.** For arbitrary pure four-qubit inputs, §2 gives an exact necessary-and-sufficient **finite scalar criterion** for the strengthened physical spectral condition `lambda_2(H1(rho)+tilde rho)<=3`. It uses the one actual input's local eigenbases and amplitudes, not freely selected marginals. In conjunction with the frame moment condition `4S+8C<=64/9`, it yields original all-noise k3 on a fully specified pure-input region and its actual convex hull. A concrete unequal-marginal GME input outside both new regions 114 and 118 is supplied. The scalar inequality is **not** proved for all physical inputs, and its failure would disprove only this strengthened spectral route, not automatically original k3. No novelty, independent-family/human/formal acceptance, or process-history cure is asserted.

## 1. Exact physical data

Let `rho=|psi><psi|`, `sigma=tilde rho=Y^tensor4 rho^T Y^tensor4`, and let `r_i` be the actual local Bloch radii; `S=sum_i r_i^2`, `C=Tr(rho sigma)`. Diagonalize each one-qubit marginal of sigma so its majority eigenvector is `|0>` and its minority eigenvalue is

\[
p_i=(1-r_i)/2,\qquad s=\sum_i p_i.
\]

In this product eigenbasis write `P_x=|<x|sigma_vector>|^2`. These amplitudes and all four marginals arise from the **same physical pure state**. For `0<s<1`, all axes are nondegenerate: the pure-state marginal polygon `p_i<=sum_(j!=i)p_j` gives `p_i<=s/2<1/2`.

For `x!=1111`, define

\[
a_x=3-s-\sum_{i:x_i=1}(1-2p_i).
\tag{1}
\]

These are the actual diagonal entries of `H1(sigma)-I` in the stated eigenbasis. For weight 0,1,2 they are strictly positive when `s<1`; at weight 3, for the word missing i, `a_x=s-2p_i>=0`. If any such denominator is zero, its actual `P_x` is zero as well. Indeed, across i|rest, the largest eigenvalue of the complementary marginal is `1-p_i`, so the probability all other three sites are majority is at most `1-p_i`. If `p_i=sum_(j!=i)p_j`, equality holds in the three-event union bound; hence the probability that two or more other sites are minority is zero, including the displayed weight-three word. No `0/0` occurs.

## 2. The exact scalar iff

Define

\[
W(\rho)=\sum_{\substack{x\ne1111\\a_x>0}}\frac{P_x}{a_x},
\qquad q_4=P_{1111}.
\tag{2}
\]

For `0<s<1`,

\[
\boxed{\lambda_2\bigl(H_1(\rho)+\widetilde\rho\bigr)\le3
\quad\Longleftrightarrow\quad
W(\rho)\le1+\frac{q_4}{1-s}.}\tag{3}
\]

To see this, set `D=H1(sigma)` and `M=D-sigma`. Full spin flip gives `H1(rho)+tilde rho=4I-M`. In the actual local eigenbasis, `D-I` has one strictly negative diagonal entry `s-1` at `1111` and all other entries nonnegative by the pure marginal polygon. The `1111` pivot of `M-I` is `-(1-s+q4)<0`. Eliminating this pivot leaves the positive diagonal block, minus

\[
\frac{1-s}{1-s+q_4}\,|\sigma_{\perp}\rangle\langle\sigma_{\perp}|.
\]

Its zero-diagonal directions have zero sigma amplitude by §1. On the strictly positive support, the rank-one Schur/PSD criterion gives exactly (3), with a Moore–Penrose interpretation on the zero directions. Thus the iff includes true polygon-boundary degeneracies without undefined inverses. For `s>=1`, `D-I>=0` and one rank-one subtraction creates at most one negative eigenvalue, so `lambda2<=3` holds automatically. At `s=0` the state is product and the bound holds directly.

For reference, the elementary proof of the polygon inequality is: the probability that any of the other three local bits is minority is at least `p_i` because the complementary marginal's largest eigenvalue is `1-p_i`, and at most the sum of those three minority probabilities. This also establishes the equality condition just used. The iff does NOT assert the harmonic inequality is universally true; its general physical validity remains a precise open problem.

## 3. Exact k3 sufficient region

For every pure state, each local Schmidt rank is at most two, so `H1(sigma)>=2sigma` and `H1(rho)+tilde rho=4I-[H1(sigma)-sigma]` has largest eigenvalue at most four. If either `s>=1`, `s=0`, or the actual harmonic inequality in (3) holds, its second and third largest eigenvalues are at most three, hence its top-three trace against every actual rank-three Q is at most ten.

Separately, the pure Pauli frame `F(rho)=sum_(i,a) sigma_i^a rho sigma_i^a` has trace 12, rank at most 12, and `Tr F^2=16+4S+8C` by the written Pauli-sector identity in 114 §3. If

\[
4S+8C\le64/9,\tag{4}
\]

Cauchy–Schwarz on the top three and at most nine other nonzero frame eigenvalues implies `K3(F)<=8`: the lower bound `x^2/3+(12-x)^2/9` at `x=8` is `208/9`. The actual common-Q spin-flip/erasure identities then give `Tr Q T1<=3`, `Tr Q T2<=3`; together with the exact product coefficient bounds for T0,T3,T4, the ORIGINAL k3 comparison follows for every physical p. Full transpose/spin flip covers `p>1`, and same-Q affine averaging covers the actual convex hull. This general criterion includes all of the 118 low-Bloch-sum region and, under the weaker rank-12 frame threshold, the equal-radius criterion in 114. It is not an all-state solution.

## 4. Exact unequal-radii GME point beyond both earlier input regions

Take

\[
|\psi\rangle=(4|0000\rangle+|0011\rangle+|1101\rangle+2|1110\rangle)/\sqrt{22}.
\]

Its local radii are `(6,6,6,9)/11`, with sum `27/11>2` and not all equal, so it is outside the input scopes of both 118 and 114. It has `S=189/121`, `C=0`, and `4S=756/121<64/9`. For sigma's actual majority axes, `s=17/22`, `q4=0`, and the only nonzero terms in (2) give

\[
W=(16/22)/(49/22)+(1/22)/(19/22)
 +(1/22)/(7/22)+(4/22)/(13/22)
=10042/12103<1.
\]

Thus the candidate proves original k3 for this actual state at all physical p, conditional on full written review. Its exact Schmidt-cut ranks are `2,2,2,2,2,4,4`, so it is GME. Its unique local axes are Z and its support mixes parity, excluding product-Pauli parity and paired-parity LU families; unequal radii exclude symmetric LU states; the rank-4 two-versus-two cut excludes LU vacuum-plus-single-excitation states; and its `(1,2)|(3,4)` maximum squared Schmidt coefficient `17/22` bounds product overlap below `124/125`. Other older covariance/regional tests are not assessed, and no exhaustive novelty claim is made.

## 5. Executed exact physical check and limits

`frontier-20261028-119-harmonic-dual-check.py`, SHA256 `985b3e44bfcad4887fdf1b44796c7110bfcc2211a5d15acece53c7ef606aa589`, ran with `python3 -B`, single-threaded BLAS, exit0. Exact Fraction/Gaussian-rational arithmetic constructs actual rho and sigma, performs the physical product-basis rotation for sigma, verifies the nondegenerate marginals and all cut ranks, all denominators and the exact harmonic sum, and `Tr F^2=2692/121<208/9`. It checks the exact pair marginal giving the overlap bound. At `p=2/3,4/3`, exact Pauli/sequential original channel matrices agree; exact LDL certifies `lambda1<4/25` and exact inertia `(15,1,0)` certifies `lambda2<9/100`, so actual top3 `<17/50<32/81` with gap `223/4050`. The same actual rank-three projector and its reflected partner give trace `7/22`. These finite checks do not prove the general scalar inequality or all-input k3. Native checker-pin clock `Wed Oct 28 21:24:54 PDT 2026`.

A disjoint review must reconstruct the physical polygon/zero-support boundary, full two-way Schur inertia, all amplitudes in sigma's **actual** local eigenbasis, Pauli rank/moment, same-Q erasure and exact mirror/convex bridges. The original unrestricted k3 question remains open.
