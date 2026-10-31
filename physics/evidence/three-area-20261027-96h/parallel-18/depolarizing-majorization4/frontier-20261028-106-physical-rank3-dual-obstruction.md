# Actual rank-three dual target and a sharp physical obstruction

**WRITTEN reduction + exact physical counterexample to a stronger auxiliary operator bound, NOT an original-channel counterexample.** The original k3 comparison is equivalent to an operator bound on every actual rank-three projector. Section 1 gives a concrete sufficient pair of spin-flip/erasure inequalities; both remain **unproved**, and no global k3 claim follows. Section 2 supplies the requested explicit physical rank-three projector that violates a natural product-inspired strengthening of one of these inequalities. The input is a genuine four-partite-entangled state, not an abstract spectrum or an independently chosen collection of marginals. These are unreviewed same-harness results; no novelty, formal/human/independent-family certification or history cure is claimed.

## 1. A precise dual operator route to the actual original k3 target

Write `Phi_p(X)=(1-p)X+(p/2)Tr(X)I`, `Lambda_p=Phi_p^tensor4`, and for an actual rank-three orthogonal projector `Q` define

\[
F(Q)=\sum_{i=1}^4\sum_{a=x,y,z}\sigma_i^a Q\sigma_i^a,
\quad H_1(Q)=\sum_i I_{\bar i}\otimes\operatorname{Tr}_{\bar i}Q,
\quad \widetilde Q=Y^{\otimes4}Q^T Y^{\otimes4}.
\]

Because the channel is self-adjoint, original k3 for every physical rho is exactly

\[
\Lambda_p(Q)\le R_3(p)I_{16}\quad\text{for every actual rank-three }Q.
\tag{1}
\]

For `0<=p<=1`, put `u=1-p` and let `T_m(Q)=sum_|S|=m E_S(Q)`, where `E_i(X)=I_i tensor Tr_i(X)/2`. The following TWO **open, sufficient**, pointwise operator assertions would imply (1):

\[
\boxed{F(Q)\le8I},\qquad
\boxed{H_1(Q)+\widetilde Q\le10I}.
\tag{2}
\]

They concern the very same actual Q. Their exact significance is as follows. Pauli twirl, full spin flip, and `Tr Q=3` give

\[
\begin{aligned}
T_1(Q)&=Q+\tfrac14F(Q),\\
4T_2(Q)&=H_1(Q)+Q+\widetilde Q+\tfrac12F(Q)-3I.
\end{aligned}\tag{3}
\]

These are identities, not guesses. For the second, expand `tilde Q=Q-2T1+4T2-8T3+16T4`, use `8T3=H1` and `16T4=3I`, and substitute the first identity. If both inequalities in (2) hold, then `Q<=I` gives

\[
T_1(Q)\le3I,\qquad 4T_2(Q)\le(10+1+4-3)I=12I.
\]

The remaining layer bounds are unconditional: `T0(Q)=Q<=I`, `T4(Q)=3I/16`, and `T3(Q)=H1(Q)/8<=5I/4`. For the last, rotate the single-site marginals of Q to `3I/2+(m_i/2)Z`, `m_i>=0`. The rank-three variational bound gives `sum_i m_i<=4+2+2=8`, hence `H1(Q)<=6I+4I=10I`. Multiplying all five layer bounds by the SAME nonnegative coefficients `u^(4-m)p^m` produces

\[
\Lambda_p(Q)\le
\left[u^4+3u^3p+3u^2p^2+\tfrac54up^3+\tfrac3{16}p^4\right]I
=R_3(p)I.
\]

For `1<=p<=4/3`, the exact full-transpose spin-flip identity carries the established `2-p` bound to p. Thus a proof of BOTH actual-projector assertions in (2) would settle the full original k3 question. Neither assertion is proved here, and an auxiliary failure would not automatically refute original k3. These targets are a dual repackaging of the owner’s earlier actual-erasure reduction `frontier-20261028-06-erasure-certificate.md`, with the new explicit H1/full-spin-flip interface; no claim of a novel underlying sufficient coefficient condition is made.

## 2. Exact actual Q defeating a tempting stronger bound

The product-reference projector `Q0=span{|0000>,|0001>,|0010>}` satisfies the very convenient, **stronger** inequality

\[
F(Q_0)\le4(I+Q_0),\tag{4}
\]

and (4), if true for every Q, would immediately imply the first target `F(Q)<=8I`. But it is FALSE for an actual complex-allowed rank-three projector. Let Q be the orthogonal projection onto the following three mutually orthonormal real vectors:

\[
\begin{aligned}
u_0&=(|0000\rangle-|1111\rangle)/\sqrt2,\\
u_1&=(|0001\rangle+|0010\rangle+|0111\rangle+|1011\rangle)/2,\\
u_2&=(|0100\rangle+|1000\rangle+|1101\rangle+|1110\rangle)/2.
\end{aligned}\tag{5}
\]

Take the actual pure density `rho=|psi><psi|`, where

\[
|\psi\rangle=\frac{2|0000\rangle+|0101\rangle+|0110\rangle
+|1001\rangle+|1010\rangle+2|1111\rangle}{\sqrt{12}},
\quad
|\zeta\rangle=\frac{|0101\rangle-|0110\rangle-|1001\rangle+|1010\rangle}{2}.
\]

Direct Pauli conjugation gives the exact 16-by-16 identities

\[
Q\rho=0,\quad Q|\zeta\rangle=0,\quad
\langle\psi|\zeta\rangle=0,\quad
F(Q)=2I+6\rho-2|\zeta\rangle\langle\zeta|.\tag{6}
\]

In particular, `F(Q)|psi>=8|psi>` while `Q|psi>=0`, so

\[
[F(Q)-4(I+Q)]|\psi\rangle=4|\psi\rangle.\tag{7}
\]

The proposed universal extension of (4) is therefore violated by the **exact positive eigenvalue 4**. More generally, this same actual Q disproves `F(Q)<=8I-alpha(I-Q)` for every `alpha>0`: the left minus right has eigenvalue alpha at psi. Thus even if the still-open target `F(Q)<=8I` is true, its saturation can occur on a vector orthogonal to the projector; a product-supported correction or a positive spectral gap away from Q cannot establish it.

The vector `psi` and projector in (5) are the balanced actual frame-saturation example in the earlier author packet `frontier-20261028-38-entangled-frame-equality-family.md`; here the requested **dual operator violation** and complete dual-channel spectra are checked directly anew. The seven exact Schmidt-cut ranks of psi are `2,2,2,2,3,4,4`, so it is genuinely four-partite entangled. No historical held or withdrawn result is imported.

## 3. The ORIGINAL channel remains safe on this witness

For the same Q, direct exact arithmetic gives

\[
\begin{aligned}
\operatorname{spec}F(Q)&=8^{(1)},2^{(14)},0^{(1)},\\
\operatorname{spec}T_1(Q)&=2^{(1)},(3/2)^{(3)},(1/2)^{(11)},0^{(1)},\\
\operatorname{spec}T_2(Q)&=(7/4)^{(1)},(3/2)^{(3)},1^{(11)},(3/4)^{(1)}.
\end{aligned}\tag{8}
\]

Both open candidate bounds in (2) are safe here: `lambda_max F(Q)=8` and `lambda_max(H1(Q)+tilde Q)=7`; the same-projector `T1` and `T2` maxima are 2 and 7/4, respectively. At each actual physical `p=2/3,4/3`, the full dual channel spectrum is

\[
\operatorname{spec}\Lambda_p(Q)=
(20/81)^{(1)},(19/81)^{(3)},(14/81)^{(11)},(4/27)^{(1)}.
\]

Its maximum `20/81` is strictly less than the original reference `R3=32/81`. The same psi is the actual maximum-eigenvalue input for this Q. Hence (7) is a clean obstruction to the tempting auxiliary shortcut, **not** a counterexample to original k3 or to either target in (2).

## 4. Exact executed checks and review boundary

`frontier-20261028-105-dual-projector-obstruction-check.py`, SHA256 `3482d25fb06214b99e7b6f1d64e973a98ebe01b21c6a9b7d3829d4cb5476f6b8`, ran under `python3 -B` and single-threaded BLAS, exit0. Exact Fraction/Gaussian-rational calculations checked rho purity/trace, all seven cut ranks, Q Hermiticity/idempotence/rank, the full matrix identity (6), `Q rho=Q|zeta>=rho|zeta>=0`, `(F(Q)-4I-4Q)rho=4rho`, both identities in (3), the full spectra in (8), and the two candidate-operator maxima. The rank-3 product Q0 satisfies (4) by an exact diagonal operator check. Exact sequential local and independent Pauli channel matrices agree at both named p values; all 16 dual eigenvalue multiplicities are checked via rational Gaussian ranks. Native checker-pin clock `Wed Oct 28 20:38:41 PDT 2026`.

The new complete proof obligation is the **actual** pair of rank-three operator inequalities (2), or a physical violation of either. No inequality has been inferred from a floating spectrum, incompatible projectors, the abstract nonimplication packets, or a withdrawn historical candidate. The original global k3 target remains open.
