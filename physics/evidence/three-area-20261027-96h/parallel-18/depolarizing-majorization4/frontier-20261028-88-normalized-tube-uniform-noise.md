# Normalized product tube: a wider all-density k3 candidate

**HIGH-CONSEQUENCE CONDITIONAL AUTHOR CANDIDATE, NOT ADOPTED.** Conditional on the named complete predecessor Hessian and common-projector estimates below, the written argument proposes the original four-qubit k3 comparison for **all** physical densities and actual complex rank-three projectors when

\[
|1-p|\le 1/1000,\qquad 0\le p\le4/3.\tag{1}
\]

This is twelve and a half times the radius of the separate unreviewed `81` candidate, not an all-noise or all-index theorem. The algebraic/executable checks below do **not** prove the universal result; full independent review is required. No historical quarantine or process finding is cured or used as a mathematical premise.

## 1. Exact imports and the new normalization

For `0<t=1-p<=1/1000`, use

\[
\mathcal H_t(X)=[16\Lambda_{1-t}(X)-\operatorname{Tr}(X)I]/t.
\]

The imports are the complete product-gauge/Hessian/common-projector reasoning of `frontier-20261028-59-uniform-high-noise-k3.md`, SHA256 `6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`; the small-t Pauli bounds of `frontier-20261028-77-offblock-uniform-noise.md`, SHA256 `04de53eea1187e9a890f263c954c3e05abe7c1e621817bfea24c811ca23eafb2`; and the mixed-normal-direction rescaled Hessian margin of `frontier-20261028-81-psd-hessian-uniform-noise.md`, SHA256 `49019845e5ca92b1a90f8c0199c0fcc2ba37301b720117839c42b13469422760`. Each predecessor is itself an unreviewed author candidate; its import here is conditional, not a fresh review or admission.

For an arbitrary pure input choose a closest product state, rotate it to `|0>=|0000>`, and fix phase. Write

\[
|\psi\rangle=\sqrt{1-\eta^2}|0\rangle+\eta|v\rangle,
\qquad \|v\|=1,\qquad 0<\eta\le1,
\]

where `v` has no weight-0 or weight-1 computational component, and `eta^2=1-m(psi)` with `m` the maximum squared product overlap. The product case `eta=0` is exact equality. Put `h=eta sqrt(1-eta^2)`,

\[
D=\mathcal H_t(|0\rangle\langle0|),\quad
V=\mathcal H_t(|v\rangle\langle0|+|0\rangle\langle v|),\quad
W=\mathcal H_t(|v\rangle\langle v|-|0\rangle\langle0|).
\]

Unlike an expansion of an unnormalized `(|0>+epsilon v)` using a cubic normalization remainder, the normalized parameter gives the **exact** identity

\[
H:=\mathcal H_t(|\psi\rangle\langle\psi|)=D+hV+\eta^2W.\tag{2}
\]

Let the reference blocks be computational weights `0`, `1`, and `2/3/4`; the two consecutive gaps are at least `2`. The `0` and `1` compressions of `V` vanish. Let `S` be the anti-Hermitian divided-gap generator with `V_off+[D,S]=0` and zero within-block entries. Set

\[
C=[V,S]+\tfrac12[[D,S],S],\quad Q=W+C.\tag{3}
\]

The imported high-noise bounds, valid uniformly over complex normalized `v` and `0<t<=1/1000`, are

\[
\|D\|\le5,\quad\|V\|_F<23/1000,\quad \|S\|_F<3/250,
\quad\|W\|_F<17,\quad\|Q\|_F<17.\tag{4}
\]

The predecessor's actual Hessian identity and `81` PSD weight-two argument give, for the `0`-block scalar `Q_0` and `1`-block matrix `Q_1`,

\[
Q_0+K_2(Q_1)\le-15/4.\tag{5}
\]

This keeps one same actual `v` throughout; it is not derived from independent state optimizers.

## 2. New operator off-block bound

At `t=0`,

\[
W_0=\sum_i(\vec r_i(v)-\hat z)\cdot\vec\sigma_i.
\]

Its longitudinal terms are block diagonal. Let `B=sum_i(r_ix X_i+r_iy Y_i)` be its transverse part, and let `P_{<=2}` project onto weights at most two. A single spin flip changes weight by one, so the **entire** off-block part of `W_0` is precisely `P_{<=2} B P_{<=2}`, extended by zero on weights three and four. Thus

\[
\|\operatorname{off}W_0\|\le\|B\|
\le\sum_i\sqrt{r_{ix}^2+r_{iy}^2}\le4.\tag{6}
\]

Using the imported `||W-W0||_F<23/1000`, the Frobenius bounds in (4), and `||[A,B]||_F<=2||A||_F||B||_F`,

\[
\|C\|_F\le 2(23/1000)(3/250)+2(5)(3/250)^2
=249/125000<1/500,
\]

so pinching cannot increase the Frobenius norm of the correction and

\[
\|\operatorname{off}Q\|<4+23/1000+1/500<403/100.\tag{7}
\]

This is an operator-norm bound on the **actual** three-block off-diagonal, not a claim that the total `Q` has norm at most `403/100`.

## 3. First conjugation with normalization retained

Suppose `0<eta<=1/8`. Expanding the actual unitary `e^{-hS} H e^{hS}` through second order, use `h^2=eta^2(1-eta^2)` and (3):

\[
e^{-hS}He^{hS}=D+hV_{\rm diag}+\eta^2 Q-\eta^4 C+R.\tag{8}
\]

The first term in (8) has the exact cancellations shown; the remainders are controlled using `||[A,S]||<=2||A||||S||` and `exp(2 eta ||S||)<2`:

\[
\|R\|\le\eta^3\left[\frac{5(2s)^3}{3}+
 (23/1000)(2s)^2+2(17)(2s)\right]
<\frac{817}{1000}\eta^3,\quad s=3/250.\tag{9}
\]

In (9), the three terms bound respectively the cubic-and-higher part of `D`, quadratic-and-higher conjugation of `hV`, and first-and-higher conjugation of `eta^2 W`; the factor two bounds their exponential tails. Equation (8) is exact with `R` defined as the residual, and the separate `eta^4 C` accounts exactly for `h^2!=eta^2`.

Let `H_* = D+h V_diag+eta^2 Q`. By (4),

\[
\|H_*-D\|\le(1/8)(23/1000)+(1/64)17
=537/2000<27/100.\tag{10}
\]

Consequently the scalar weight-0 block is separated from the entire compression on weights `1/2/3/4` by more than `7/5`; the weight-1 block is likewise separated from the weight-`2/3/4` block by more than `7/5`. This does not assume any gap within the fourfold weight-1 block.

## 4. Interlacing replaces the second unitary rotation

We use the following elementary block estimate. If Hermitian `A,D` obey `lambda_min(A)-lambda_max(D)>=g>0`, then

\[
\begin{bmatrix}A&B\\B^*&D\end{bmatrix}
\le \operatorname{diag}(A+BB^*/g,D+gI),\tag{11}
\]

because the difference is `[[B/sqrt(g)],[-sqrt(g)I]]` times its adjoint. All eigenvalues of the second diagonal block are at most the smallest eigenvalue of `A`, so (11) and Ky Fan monotonicity give, for `j<=dim(A)`,

\[
K_j\!\left(\begin{bmatrix}A&B\\B^*&D\end{bmatrix}\right)
\le K_j(A)+j\|B\|^2/g.\tag{12}
\]

Let `C0` be the compression of `H_*` to the orthogonal complement of the weight-0 block. Cauchy interlacing gives

\[
K_3(H_*)\le\lambda_1(H_*)+K_2(C0).\tag{13}
\]

Apply (12) once to weight `0` versus `1/2/3/4`, then to weight `1` versus `2/3/4` inside `C0`. In both cases the off-block norm is at most `eta^2(403/100)` by (7). Using (5), and noting the two leading `V_diag` compressions vanish,

\[
K_3(H_*)\le K_3(D)-\frac{15}{4}\eta^2
 +\frac{3(403/100)^2}{7/5}\eta^4.\tag{14}
\]

By Weyl/Ky Fan, (8), (9), and `||C||<1/500` add at most `3(817/1000)eta^3+3eta^4/500`. For `eta<=1/8`, the resulting normalized loss divided by `eta^2` is bounded exactly by

\[
3\frac{817}{1000}\frac18+
3\frac1{500}\frac1{64}+
\frac{3(403/100)^2}{(7/5)64}
=\frac{761823}{896000}<1.\tag{15}
\]

Therefore

\[
K_3(H)\le K_3(D)-\frac{11}{4}\eta^2,
\qquad R_3(p)-K_3(\Lambda_p(\rho))
\ge\frac{11}{64}t\eta^2.\tag{16}
\]

The equality endpoint `eta=0` is the product reference; the displayed strict gap covers all nonproduct pure states in the tube. Equations (11)–(16) use actual block compressions and a single `v`, and do not assume any individual excited eigenvalue is product-bounded.

## 5. Far case, mixed states and reflection

For the same physical pure input, let sorted local Bloch radii be `r1<=r2<=r3<=r4`, `L=r1+r2+3r3+3r4`, `S=sum r_i^2`. The predecessor's union bound on the four commuting local-majority projectors gives

\[
8-L\ge2[1-m(\psi)]=2\eta^2.
\]

Its common-projector estimate gives for every actual rank-three `P`

\[
16[R_3(p)-\operatorname{Tr}(P\Lambda_p\rho)]
\ge t[(8-L)-t(\sqrt{39(15-S)}-5)].\tag{17}
\]

The bracketed square-root coefficient is strictly below `20`. If `eta>=1/8` and `t<=1/1000`, then `8-L>=1/32>1/50>=20t`; hence the original k3 gap is positive. The tube case is (16). At `t=0` every output is `I/16`. Fix the SAME actual `P` while averaging a finite pure-state decomposition to cover every mixed density. Finally use the exact global-transpose/spin-flip mirror from `frontier-20261028-01-spectral-mirror.md` to cover negative shrinkage at `p>1`. This gives (1) conditional on the explicitly named predecessor inputs.

## 6. Actual finite checks and boundaries

`frontier-20261028-87-normalized-tube-exact.py`, SHA256 `e6227036c04685e389db161fce719a7cf0c29b928e3bb2ccfe4d17e5825d5216`, ran with `python3 -B`, single-threaded BLAS, and exited zero. Python `Fraction` arithmetic checked the exact constants in (7), (9), (10), (15), the `7/5` gap, and the far comparison `1/32>1/50`. It also built the exact physical state

\[
(1500|0000\rangle+|0011\rangle+2i|0111\rangle+2|1111\rangle)/\sqrt{2250009}
\]

at both `p=999/1000` and `p=1001/1000`. Sequential local channel entries exactly equaled the independently assembled Pauli channel; exact rational Gaussian LDL certified 16 positive output pivots and `lambda1<0.0627503737`; exact inertia `(15,1,0)` of `0.0626249993 I-output` certified `lambda2<0.0626249993`. Thus the actual top-three sum is below `1880003723/10000000000`, while the product reference is `3008005999999/16000000000000`, leaving exact gap `43199/16000000000000`. One actual rank-three projector (and its reflected partner) was also checked. The printed numerical top eigenvalues are only approximate; the matrix equalities, LDL, inertia and rational inequalities above are exact finite checks for this one state and two p values, **not** proof of the universal tube theorem.

Full review must independently reconstruct the entire imported Hessian/closest-product/far-P/mirror chain AND new normalization, transverse compression, unitary remainder, both interlacing/block applications, ordering, constants and mixed-state bridge. No all-p closure, independent-family/human/formal verification, executable universal proof or novelty claim follows. Native checker-pin clock: `Wed Oct 28 19:33:22 PDT 2026`.
