# Equal-marginal spin-flip bound and a physical all-noise k3 region

**HIGH-CONSEQUENCE WRITTEN AUTHOR CANDIDATE — NOT ADOPTED.** For every pure four-qubit state whose four one-qubit Bloch radii are equal to `r`, the written proof below proposes the nontrivial actual-state bound

\[
\lambda_2\!\left(H_1(\rho)+\widetilde\rho\right)\le3,
\quad H_1(\rho)=\sum_i I_{\bar i}\otimes\rho_i.\tag{1}
\]

Combining this with an exact Pauli-frame second-moment criterion proves original k3 for the explicit pure-state region

\[
r_1=r_2=r_3=r_4=r,\qquad
16r^2+8C\le256/39,
\quad C=|\langle\psi|Y^{\otimes4}\overline\psi\rangle|^2,\tag{2}
\]

and for its actual convex hull, all physical noise, and every complex rank-three test projector. Equal radii are a restriction on the **input**; no claim is made that arbitrary states can be made equal-radius by physical local unitaries. This does not prove global k3, even on the full equal-radius set without (2). The proof is ordinary written algebra, uses no old held result or external theorem beyond finite-dimensional Schmidt/Schur/Ky Fan/Cauchy facts, and needs complete disjoint written review; no novelty, formal/kernel/human/stronger-family acceptance or process-history cure is claimed.

## 1. Basic notation and a universal norm bound

Write `rho=|psi><psi|`, `tilde rho=Y^tensor4 rho^T Y^tensor4`, and `M(rho)=H1(rho)-rho`. For any local qubit i, pure-state Schmidt rank is at most two, so

\[
I_{\bar i}\otimes\rho_i\ge\rho/2.
\]

One proof is to apply the inverse square root of `rho_i` on its support: the resulting Schmidt vector has squared norm at most two. The zero-Schmidt coefficient is handled on its support. Summing gives `H1(rho)>=2rho`, hence `M(rho)>=0`. Full spin flip sends each one-qubit marginal to `I-rho_i`, so

\[
H_1(\rho)+\widetilde\rho=4I-M(\widetilde\rho).
\tag{3}
\]

The spin-flipped state is pure and has exactly the same local Bloch radii. Therefore `lambda_1(H1(rho)+tilde rho)<=4` for every pure rho; the argument below proves its second eigenvalue at most 3 when the local radii are equal.

## 2. The equal-marginal second-eigenvalue argument

It is enough by (3) to prove that for every equal-radius pure `sigma`, the second **smallest** eigenvalue of `M(sigma)` is at least one. Independently rotate its local bases so each marginal has majority `1-q` and minority `q`, `0<=q<=1/2`. Put `s=4q`, and define

\[
D=H_1(\sigma),\qquad P_h=\sum_{|x|=h}|\langle x|\psi\rangle|^2.
\]

The actual probabilities obey `sum_h P_h=1` and `sum_h h P_h=s`; no independence assumption is made. On the weight-h computational sector,

\[
D- I=(3-s,\;2-s/2,\;1,\;s/2,\;s-1)_h.\tag{4}
\]

If `s>=1`, `D-I>=0`, and subtracting the one-dimensional projection sigma creates at most one negative eigenvalue; this gives the desired second-eigenvalue bound. If `s=0`, all local marginals are pure, sigma is a product, and the bound is direct. Now assume `0<s<1`. In (4) exactly the weight-four direction has a negative diagonal value; the other 15 directions form a positive definite block.

Taking the Schur complement of that one negative entry in `D-I-sigma`, the positive block is PSD exactly when

\[
W:=\frac{P_0}{3-s}+\frac{P_1}{2-s/2}+P_2+\frac{2P_3}{s}
\le1+\frac{P_4}{1-s}.\tag{5}
\]

For completeness, the negative scalar block is `-(1-s+P4)`, and the surviving rank-one coefficient is `(1-s)/(1-s+P4)`. Thus (5) follows from the rank-one PSD criterion, without dividing by a zero endpoint.

Set `K=(2-s)/(s(3-s))`, `a1=1/(2-s/2)-1/(3-s)`, `a2=1-1/(3-s)`. Using BOTH `sum P_h=1` and `sum h P_h=s`, one obtains the exact identity

\[
\begin{aligned}
W-1-\frac{P_4}{1-s}
={}&(a_1-K)P_1+(a_2-2K)P_2\\
&-\left(\frac1{3-s}+\frac1{1-s}+4K\right)P_4.
\end{aligned}\tag{6}
\]

Every term on the right is nonpositive: `a1=K s/(4-s)<=K` and `a2=sK<=2K`. Thus (5) holds, `M(sigma)-I` has at most one negative eigenvalue, and `lambda_2^up(M(sigma))>=1`. Formula (3) then proves (1). In fact the scalar argument only uses actual equal marginals and the total Hamming-weight moment; it does not choose independently optimized marginals or phases.

A useful exact tightness family has only weight 0 and weight 3 support, equal weight-3 probabilities and `0<s<1`; in (6), `P1=P2=P4=0`. These can be actual GME states, so the second-eigenvalue bound cannot be sharpened to a strict inequality on all entangled inputs.

## 3. A separately certified frame criterion and original k3

Let `F(rho)=sum_(i,a) sigma_i^a rho sigma_i^a`. For every pure four-qubit rho,

\[
\operatorname{Tr}F=12,\qquad
\operatorname{Tr}F^2=16+4\sum_i r_i^2+8C.\tag{7}
\]

For clarity, here is the finite-dimensional derivation. Let `A_j` be the sum of squared Pauli expectations of weight j. Pure three-site/one-site complementary marginal purities give `A3=12+A1-2A2`, global purity gives `A4=3-2A1+A2`, and the full spin-flip overlap gives `16C=1-A1+A2-A3+A4`. Hence `A2=2+A1+4C`. The 12-by-12 local-Pauli Gram matrix has diagonal-site squared Frobenius sum `12+2A1` and cross-site sum `2A2`; its nonzero eigenvalues equal those of F. This yields (7), including all complex amplitudes.

Let `x=K3(F)`. By Cauchy–Schwarz on the largest three and remaining thirteen eigenvalues,

\[
\operatorname{Tr}F^2\ge x^2/3+(12-x)^2/13.
\]

The right side is increasing for `x>=9/4`, and every PSD 16-by-16 F of trace 12 has `K3(F)>=9/4`. At `x=8` its value is `880/39`. Thus, if (2) holds,

\[
\operatorname{Tr}F^2=16+16r^2+8C\le880/39
\quad\Longrightarrow\quad K_3(F)\le8.\tag{8}
\]

For any SAME actual rank-three Q, (1), the universal `lambda1<=4`, and (8) give

\[
\operatorname{Tr}Q(H_1(\rho)+\widetilde\rho)\le10,
\qquad\operatorname{Tr}(QF)\le8.
\]

Use `T_m(rho)=sum_|S|=m E_S(rho)` with `E_i` the normalized erasure. Pauli twirl and full spin flip give the exact input-side identities

\[
T_1=\rho+F/4,\qquad
4T_2=H_1+\rho+\widetilde\rho+F/2-I.
\]

Thus `Tr Q T1<=3` and `4 Tr Q T2<=10+1+4-3=12`, with the SAME rho,Q. The unconditional other layer bounds are `Tr Qrho<=1`, `Tr QT3<=5/4` and `Tr QT4=3/16`. Multiplying them by the nonnegative physical erasure coefficients for `0<=p<=1` gives the exact product-reference top3 expression. Full-transpose global spin flip extends to `1<=p<=4/3`. Fix Q when averaging finite convex decompositions; this proves the stated actual convex-hull class, not a nonlinear condition on mixed-state marginals.

## 4. Exact nonproduct equality in (1) and finite evidence

`frontier-20261028-113-equal-marginal-check.py`, SHA256 `5074896e58a0581b3ef827502535017916035bc230459922b0e2fbe70fcb7a95`, ran under `python3 -B`, single-threaded BLAS, exit0. Exact Fraction/Gaussian-rational matrix arithmetic checks the physical state

\[
|\psi\rangle=(3|0000\rangle+|0111\rangle+|1011\rangle
+|1101\rangle+|1110\rangle)/\sqrt{13},
\]

its seven Schmidt-cut ranks `2,2,2,2,3,3,3`, each local minority probability `3/13`, `r=7/13`, and `C=0`. Exact rational Gaussian ranks give the **full** spectrum

\[
\operatorname{spec}(H_1+\widetilde\rho)=
(40/13)^{(1)},3^{(1)},(33/13)^{(3)},2^{(6)},(19/13)^{(5)}.
\]

Thus `lambda2=3` exactly at a GME input. The exact frame square is `Tr F^2=3488/169<880/39`, so this example lies in (2). At original `p=2/3` and `4/3`, independent exact sequential/Pauli channel matrices agree; exact LDL certifies positivity and `lambda1<3/20`, exact inertia `(15,1,0)` certifies `lambda2<17/200`, and hence top3 `<8/25<32/81`, with gap `152/2025`. The named same actual rank-three projector was checked as well. These finite checks are not the universal proof. The first exploratory execution exposed an integer-to-float construction bug and a subsequent missing helper attribute; both were corrected before this pinned exact successful run, with no earlier mathematical result inferred from the failed checks. Native checker-pin clock `Wed Oct 28 21:15:54 PDT 2026`.

The all-variable original problem remains outside (2), as does a proof of the frame inequality on the entire equal-radius set. Disjoint review should check the Schur sign, scalar identity (6), pure Pauli-sector identities, same-Q erasure coefficients, endpoint and mixed-state/negative-shrink extensions in full; no prior gate is transferred.
