# A k3 spectral nonimplication at every nontrivial physical noise

**WRITTEN abstract-spectrum result, NOT a channel-output counterexample.** At every physical parameter `0<=p<=4/3` with `0<|1-p|<1`, there is an explicit positive, normalized, decreasing vector `x` whose k3 prefix strictly exceeds the actual pure-product reference spectrum `y`, while all **other** prefixes, every Schatten-z comparison `1<=z<=infinity`, and every positive shifted log-determinant comparison hold in the required direction. No realization of x by a physical input is claimed. Hence even these combined exact scalar spectral constraints do not, alone, imply k3 at **any** nontrivial parameter. At the excluded endpoints `p=0` and `p=1`, this construction degenerates to x=y.

This is the continuous-noise successor of the concrete rational obstruction `frontier-20261028-102-all-spectral-constraints-obstruction.md`, SHA256 `98c0b83769f0bd98e7e77003bde0e2f1dcf75668707e7fc293ee58e7a40c75ba`, which contains the complete continuous Schatten-exponent proof. Neither result is independently reviewed or a novelty or process-cleanness claim.

## 1. Explicit construction and all prefixes

Put

\[
t=|1-p|,\quad a=(1+t)/2,\quad b=(1-t)/2,\quad
A=a^4,\quad Q=a^3b,\quad R=a^2b^2,\quad
\epsilon=(Q-R)/10>0.
\]

The exact product-reference vector is

\[
y=(A,Q^{\times4},R^{\times6},(ab^3)^{\times4},b^4),
\]

and set

\[
x=(A-3\epsilon,(Q+2\epsilon)^{\times2},
 (Q-\epsilon)^{\times2},R+\epsilon,R^{\times5},
 (ab^3)^{\times4},b^4).\tag{1}
\]

Because `A-Q=a^3 t >= a^2 b t=Q-R=10 epsilon`, the vector x is positive and sorted: in particular `A-3epsilon>Q+2epsilon` and `Q-epsilon>R+epsilon`. It has trace one. Its 16 upper-prefix differences relative to y are

\[
(-3\epsilon,-\epsilon,+\epsilon,0,-\epsilon,0^{\times11}),\tag{2}
\]

so the only violated prefix is k3. This remains true arbitrarily close to either trivial endpoint, with the positive excess tending to zero.

## 2. All shifted log determinants, for every noise and shift

Interpolate with `s in [0,epsilon]`, using the changed entries

\[
A_s=A-3s,\quad Q_+=Q+2s,\quad Q_-=Q-s,\quad R_+=R+s.
\]

For any shift `u>=0`, the derivative of the logarithm of the altered six-factor product is

\[
\begin{aligned}
D_u(s)={}&3\left(\frac1{u+Q_+}-\frac1{u+A_s}\right)\\
&+\left(\frac1{u+Q_+}+\frac1{u+R_+}-\frac2{u+Q_-}\right).
\end{aligned}\tag{3}
\]

The first line is strictly positive because `A-Q>=10epsilon>=5s`. In the second line, `Q-R>=10epsilon>=5s` implies `(Q_++R_+)/2<=Q_-`; the function `v -> 1/(u+v)` is convex and decreasing on positive v, so Jensen makes the second line nonnegative. All entries remain positive. Integrating (3) proves

\[
\prod_j(u+x_j)>\prod_j(u+y_j),\quad
\log\det(uI+\operatorname{diag}x)>
\log\det(uI+\operatorname{diag}y)
\quad(u\ge0).\tag{4}
\]

This matches the direction of the public shifted-logdet output theorem but is proved here directly for abstract x, not imported from that theorem.

## 3. Every Schatten exponent

For every `s in [0,epsilon]`, the numerical-level hypotheses of the full proof in packet 102 are satisfied:

\[
\begin{aligned}
&A-3s\ge Q+2s\ge Q-s\ge R+s>0,\\
&Q-R\ge5s,\quad 3(A-Q)\ge18s,\quad
3A-2Q-R\ge20s.
\end{aligned}\tag{5}
\]

Indeed `Q-R=10epsilon`, `A-Q>=10epsilon`, and `3A-2Q-R=3(A-Q)+(Q-R)>=40epsilon`. The derivative of the z-power sum along (1) is therefore nonpositive for every `z in [1,2]` by the concave Jensen step in 102 §3, and for every `z>=2` by the explicitly established five-coordinate weak-majorization/convex-power step there. All entries being positive, integration gives

\[
\sum_jx_j^z\le\sum_jy_j^z\quad(z\ge1),
\qquad \max_jx_j<\max_jy_j.\tag{6}
\]

Thus all finite and infinity Schatten norms satisfy the reference comparison. Equation (6) is a continuous-exponent result, not a finite grid.

## 4. Exact finite checks and precise boundary

`frontier-20261028-103-general-spectral-check.py`, SHA256 `8b0128f80a13f76dde1f3fe83d01ca8c19f9a96bd47f4450bca47a4b279b0dae`, ran with `python3 -B`, exit0. Exact Fraction arithmetic checked vector normalization/ordering and (2), endpoint conditions (5), and positivity of every coefficient in the altered shifted-determinant difference at five rational values `t=1/1000,1/200,1/3,9/10,999/1000`. These examples are not the all-t proof: the parameter-uniform written inequalities and Jensen arguments in §§1–3 provide that scope. Native checker-pin clock `Wed Oct 28 20:27:01 PDT 2026`.

The input-independent spectral data at issue are very strong: this countermodel satisfies **every original index except k3**, the complete Schatten family, and the full shifted-logdet family at the same chosen parameter. It does not assert any local marginals, Pauli covariance, common rank-three projector/state, or physical output realization. It therefore identifies a necessary missing physical ingredient and does not falsify original k3, the separate conditional small-noise candidates, or any accepted older result.
