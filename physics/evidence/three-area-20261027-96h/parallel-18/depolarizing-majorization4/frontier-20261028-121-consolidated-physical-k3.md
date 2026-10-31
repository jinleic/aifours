# Consolidated four-qubit k3 physical regions and full proof dependencies

**HIGH-CONSEQUENCE AUTHOR-WRITTEN CANDIDATE — NOT ADOPTED.** This is one consolidated review packet for the current original-channel k3 work. It contains the actual common-projector erasure bridge, the complete spin-flip/harmonic input criterion (including zero denominators and equality), the rank-12 frame moment, the equal-marginal and low-Bloch-sum corollaries, the one-uniform class, a state-dependent high-noise bound, and the separate proposed all-density uniform high-noise interval with its normal-direction Hessian and finite-dimensional remainder dependencies. Nothing here asserts the unresolved unrestricted k3 inequality, full majorization, a physical counterexample, novelty, an independent-model-family/human/formal/kernel review, or a cure of any old process finding.

The parent has **separately** supported original prefixes `k=5,6,10,11` at all physical p and all densities in `institute/runs/three-area-2026-10-27-96h/dispositions/physics-2-depolarizing-balanced-rank-prefix-parent-v1.md`, SHA256 `cdda493b043002b208d8f92b7da352d2f165f6e03c07481a439b596be7b8b38d`; that disposition does not support k3 or the new regions in this packet. The historic all-BISEP k3 and other family dispositions keep their own exact named scopes and are not silently imported into the new proofs below.

## 1. Definitions and theorem scope

For a single qubit let

\[
\Phi_p(X)=(1-p)X+(p/2)\operatorname{Tr}(X)I_2,\qquad
\Lambda_p=\Phi_p^{\otimes4},\qquad 0\le p\le4/3.
\]

Write `t=|1-p|`, `a=(1+t)/2`, `b=(1-t)/2`, and let `R3(p)` be the sum of the three largest output eigenvalues at any pure product input. Ties are allowed:

\[
R_3=a^4+2a^3b,\qquad16R_3=3+8t+6t^2-t^4.\tag{1}
\]

All inequalities below mean the ORIGINAL comparison

\[
\operatorname{Tr}[Q\Lambda_p(\rho)]\le R_3(p)
\quad\text{for every actual complex rank-three }Q.\tag{2}
\]

For a pure input let `r_i` be its local Bloch radii, sorted `r1<=r2<=r3<=r4`, and set

\[
S=\sum_i r_i^2,\quad L=r_1+r_2+3r_3+3r_4,\quad
\delta=8-L,\quad C=|\langle\psi|Y^{\otimes4}\overline\psi\rangle|^2.
\]

At each fixed physical p, define the following **actual pure-input** classes:

* **P:** every pure product state.
* **U:** every pure state with all four local marginals `I/2`, without a restriction on C.
* **D_p:** every pure state with `delta >= t( sqrt(39(15-S))-5 )`.
* **H:** every pure state with `4S+8C<=64/9` and the actual spin-flip condition in §3: `s>=1`, or `s=0`, or `0<s<1` and the explicit harmonic inequality (9). Equal radii are one sufficient subcase of that harmonic condition.

The written candidate asserts (2) for every rho in the finite convex hull of `P union U union D_p union H`. Moreover, **independently**, §§7–10 propose (2) for every physical rho whenever `t<=1/200`. These are separate proof branches; neither a numerical sample nor any other prefix gate supplies their universal quantifiers. At `p=1`, every output is `I/16`, and all inputs satisfy equality in (2).

## 2. Exact same-Q erasure and reflection interfaces

For each site `E_i(X)=I_i tensor Tr_i(X)/2`, restoring factor order; put `T_m(X)=sum_|A|=m E_A(X)`. For `0<=p<=1`, these commuting positive maps give

\[
\operatorname{Tr}[Q\Lambda_p(\rho)]
=\sum_{m=0}^4(1-p)^{4-m}p^m\operatorname{Tr}[QT_m(\rho)].\tag{3}
\]

For the same product reference and fixed Q spanning `|0000>,|1000>,|0100>`, the five layer traces are `(1,3,3,5/4,3/16)`. Thus for a given actual `(rho,Q)`, the two bounds `Tr QT1<=3` and `Tr QT2<=3`, together with the following unconditional bounds, imply (2) by nonnegative coefficientwise comparison:

* `Tr Qrho<=1` and `Tr QT4=3/16`.
* For `T3=(1/8)sum_i I_bar_i tensor rho_i`, diagonalize the four local marginals. Its top-three sum is `(12+L)/16<=5/4`, with the obvious sorted radii and ties. This holds for mixed rho as well.

Define `F(X)=sum_(i,a=x,y,z) sigma_i^a X sigma_i^a`, `H1(X)=sum_i I_bar_i tensor Tr_bar_i X`, and `tilde X=Y^tensor4 X^T Y^tensor4`. Pauli twirl and FULL spin flip give, for a normalized input,

\[
T_1=\rho+F(\rho)/4,\quad
4T_2=H_1(\rho)+\rho+\widetilde\rho+F(\rho)/2-I.\tag{4}
\]

The second identity follows by expanding `tilde rho=rho-2T1+4T2-8T3+16T4`, with `8T3=H1`, `16T4=I`. Therefore if, for the SAME input,

\[
K_3(F(\rho))\le8,\qquad
K_3(H_1(\rho)+\widetilde\rho)\le10,\tag{5}
\]

then `Tr QT1<=1+8/4=3` and `4 Tr QT2<=10+1+4-3=12` for every Q. These are sufficient input-side conditions, not assumptions that separately maximizing Qs coincide.

For `1<=p<=4/3`, `p'=2-p` lies in `[2/3,1]` and

\[
\Lambda_p(X)=Y^{\otimes4}\Lambda_{p'}(X)^T Y^{\otimes4}.\tag{6}
\]

This follows from `Y X^T Y=Tr(X)I-X` at each site. It maps actual Q bijectively to `Y^tensor4 Q^T Y^tensor4`, keeps the SAME input, and preserves the product-reference spectrum. No partial-transpose positivity is used. All remaining proofs may take `0<=p<=1`, `t=1-p`, and then use (6).

## 3. Exact actual-state spin-flip criterion

Put `sigma=tilde rho`, `M(sigma)=H1(sigma)-sigma`. A local one-qubit Schmidt decomposition gives `I_bar_i tensor sigma_i>=sigma/2` even at zero Schmidt coefficients; summing four sites yields `M(sigma)>=sigma>=0`. Also

\[
H_1(\rho)+\widetilde\rho=4I-M(\sigma),\tag{7}
\]

because spin flip sends each single-qubit marginal to `I-rho_i`. Hence its largest eigenvalue is at most four. It suffices for the second inequality in (5) to show its second eigenvalue is at most three.

Diagonalize the four actual one-qubit marginals of sigma in physical local bases with majority `|0>` and minority probabilities `p_i=(1-r_i)/2`; let `s=sum_i p_i` and `P_x=|<x|sigma_vector>|^2`. If `s>=1`, `H1(sigma)-I>=0`; subtracting the rank-one sigma creates at most one strictly negative eigenvalue, so the second-smallest eigenvalue of M is at least one. If `s=0`, sigma is a pure product and the original comparison is equality by class P.

For `0<s<1`, set for `x!=1111`

\[
a_x=3-s-\sum_{i:x_i=1}(1-2p_i),\quad
W=\sum_{\substack{x\ne1111\\a_x>0}}P_x/a_x,\quad q_4=P_{1111}.\tag{8}
\]

The pure marginal polygon `p_i<=sum_(j!=i)p_j` follows because the probability all three other local bits are majority is at most `1-p_i` (the largest eigenvalue of their complementary marginal) and at least `1-sum_(j!=i)p_j` (the commuting-projector union bound). It makes every `a_x>=0`: for weights 0,1,2 they are strictly positive since `s<1`, and for the weight-three word missing i it equals `s-2p_i`. If this value is zero, equality holds in that union bound; the probability of two or more minority bits among the other three vanishes, in particular that actual `P_x=0`. Thus no `0/0` is used, and the local marginal axes are nondegenerate because `p_i<=s/2<1/2`.

The diagonal of `D-I`, `D=H1(sigma)`, has exactly one negative entry `s-1` at `1111`. In `D-I-sigma`, that pivot is `-(1-s+q4)<0`. Eliminating it leaves the nonnegative diagonal block minus `(1-s)/(1-s+q4)` times the projected rank-one sigma. On its strictly positive support, the rank-one PSD criterion gives the exact two-way equivalence

\[
\lambda_2(H_1(\rho)+\widetilde\rho)\le3
\quad\Longleftrightarrow\quad W\le1+\frac{q_4}{1-s}.\tag{9}
\]

Zero diagonal directions have zero sigma amplitude by the previous paragraph, and remain zero under the Schur complement. Equality in (9) is allowed: a zero Schur eigenvalue is not a negative eigenvalue. If (9), `s>=1`, or the product case applies, (7) gives `K3(H1+tilde rho)<=4+3+3=10`. The general physical inequality (9) is **not** claimed for all pure states.

### Equal radii: a full subcase of (9)

If all four radii are equal, the four minorities are `q=s/4`. Let `P_h=sum_|x|=h P_x`. For `0<s<1`, the positive-sector diagonal values `H1(sigma)-I` at weights `h=0,1,2,3` are `3-s, 2-s/2, 1, s/2`. The Schur condition is

\[
\frac{P_0}{3-s}+\frac{P_1}{2-s/2}+P_2+\frac{2P_3}{s}
\le1+\frac{P_4}{1-s}.\tag{10}
\]

Using the SAME actual amplitudes, `sum_h P_h=1` and `sum_h h P_h=s`. Put `K=(2-s)/(s(3-s))`, `a1=1/(2-s/2)-1/(3-s)` and `a2=1-1/(3-s)`. Substitution gives left minus right of (10) exactly

\[
(a_1-K)P_1+(a_2-2K)P_2-
\left(\frac1{3-s}+\frac1{1-s}+4K\right)P_4\le0,
\]

since `a1=K s/(4-s)<=K` and `a2=sK<=2K`. The endpoints `s=0,1` were handled above. At `P1=P2=P4=0` equality can occur, including actual GME states; no product-only saturation claim is used.

## 4. Frame moment, rank, and the H class

For pure rho, the frame is a sum of twelve rank-one Pauli-error projectors, so `rank F<=12` and `Tr F=12`. Let `A_j` be the sum of squared Pauli expectations of weight j. Complementary three-site/one-site purities, total purity and full spin flip give

\[
A_3=12+S-2A_2,\quad A_4=3-2S+A_2,\quad
16C=1-S+A_2-A_3+A_4,
\]

hence `A2=2+S+4C`. The 12-by-12 local-Pauli Gram has squared Frobenius sum `12+2S+2A2`, and shares the nonzero spectrum of F. Therefore

\[
\operatorname{Tr}F^2=16+4S+8C.\tag{11}
\]

Writing `x=K3(F)`, Cauchy–Schwarz over the three largest and at most nine remaining nonzero eigenvalues gives

\[
\operatorname{Tr}F^2\ge x^2/3+(12-x)^2/9.
\]

The right side is strictly increasing on `x>=8` and equals `208/9` at 8. Consequently the condition `4S+8C<=64/9` implies `x<=8`, including equality and ranks below 12. Combined with §3 and the SAME Q through (4)–(5), this proves class H. In particular the easy explicit subcase `sum r_i<=2` has `s>=1`; the equal-radius subcase is established without that restriction by (10).

## 5. One-uniform class U and its explicit gap

For a pure rho with all local marginals `I/2`, across each one|three split the two Schmidt coefficients are `1/sqrt2`. Thus every `E_i(rho)` has four eigenvalues `1/4`, and `Tr QT1<=4*(3/4)=3`. Also `T3=I/4`, so `Tr QT3=3/4`. With `x0=Tr Qrho` and `xt=Tr Qtilde rho`, the full spin-flip identity yields

\[
4\operatorname{Tr}QT_2= x_t-x_0+2\operatorname{Tr}QT_1+8\operatorname{Tr}QT_3-16\operatorname{Tr}QT_4
\le1+6+6-3=10.
\]

The same Q and the product layer coefficients therefore give, for `0<=p<=1`,

\[
R_3-\operatorname{Tr}[Q\Lambda_p(\rho)]\ge\tfrac12p^2(1-p).
\tag{12}
\]

By (6), the general-physical-p version uses `p'=min(p,2-p)` in (12). Equality at the endpoints and pure-product/one-uniform overlap is not presumed; mixtures of one-uniform states retain (12) by fixing Q. This independently covers all C in class U, including points not covered by the moment condition.

## 6. State-dependent class D_p

For a pure input and the SAME rank-three Q, the local-Pauli expansion gives

\[
16\operatorname{Tr}[Q\Lambda_p(\rho)]
\le3+tL+t^2\sqrt{39(15-S)}.\tag{13}
\]

Indeed the top-three sum of the commuting weight-one operator `sum_i r_i dot sigma_i` is L, including zero radii/ties. Pauli Parseval gives total nonidentity squared projector coefficients `16 Tr Q^2-(Tr Q)^2=39`, and pure-input weight-two-through-four squared coefficients `16-1-S=15-S`; Cauchy–Schwarz with `t^k<=t^2`, `k>=2`, yields the remainder. Equation (1) and `t^4<=t^2` give

\[
16[R_3-\operatorname{Tr}(Q\Lambda_p\rho)]
\ge t[\delta-t(\sqrt{39(15-S)}-5)].\tag{14}
\]

Thus class D_p gives (2), with equality cases retained. Equation (6) justifies using nonnegative t even for `p>1`; it is not an erasure expansion at negative shrinkage.

## 7. Uniform interval: closest-product gauge and exact Hessian identities

The separate candidate `t<=1/200` below is an all-density statement and needs the FULL following algebra and perturbation estimates; it is not inferred from class D_p or from finite tests. For a pure input, let `m` be its maximum squared product overlap and choose a maximizing product vector, rotating it to `|0>=|0000>`. Compactness gives a maximizer and `m>0`. Complex first-variation stationarity removes all four weight-one amplitudes. After fixing global phase,

\[
|\psi\rangle=\sqrt{1-\eta^2}|0\rangle+\eta|v\rangle,
\quad\eta^2=1-m,\quad\|v\|=1,\quad v\text{ supported on weights }2,3,4.
\tag{15}
\]

`eta=0` is a product; take it separately. For `0<t<=1/200`, define `lambda_h=a^(4-h)b^h`,

\[
V=\Lambda_{1-t}(|v\rangle\langle0|+|0\rangle\langle v|),\quad
W=\Lambda_{1-t}(|v\rangle\langle v|-|0\rangle\langle0|).
\]

The weight-zero and weight-one diagonal blocks of V vanish. With i,j in weight one and k in weights 2–4, the exact second-order blocks are

\[
A=W_{00}+\sum_k\frac{|V_{k0}|^2}{\lambda_0-\lambda_{|k|}},\quad
M_{ij}=W_{ij}+\sum_k\frac{V_{ik}V_{kj}}{\lambda_1-\lambda_{|k|}}.
\tag{16}
\]

Every denominator is positive for `0<t<1`. The six relevant product gaps and the local matrix-unit rules `|0><0| -> diag(a,b)`, `|1><1| -> diag(b,a)`, `|0><1| -> t|0><1|` give the following explicit identities. Global excitation-phase covariance makes all cross-weight contributions vanish in A and M: a weight-h direction couples the weight-one block only to virtual weight h+1, and couplings in the two sides of a virtual product must have the same h. Thus `A=sum_h A_h`, `M=sum_h M_h`, with component norms carried quadratically and `K2(sum M_h)<=sum K2(M_h)`.

* Weight 2: write `v2=sum_(i<j)c_ij|ij>`, `sum|c|^2=1`, `T_ii=0`, `T_ij=T_ji=c_ij`, `Gamma=TT^dagger`, `n_i=Gamma_ii`. Then `Tr Gamma=2`, `Gamma>=0`, and

\[
A_2=-a^2t(1-t^2),\quad
(M_2)_{ii}=-ab t(1-t^2)(1-n_i),\quad
(M_2)_{ij}=ab t^2(1+t)\Gamma_{ij}\ (i\ne j).\tag{17}
\]

Equivalently `M2=ab t(1+t)[-(1-t)I+K]`, where `K=t Gamma+(1-2t)diag(n)>=0` and `Tr K=2(1-t)`. Hence `K2(M2)<=0` and `A2+K2(M2)<=-a^2 t(1-t^2)`. For example, (17)'s A term comes from `W00=a^2b^2-a^4=-a^2t`, `V_(ij,0)=a^2t^2 c_ij`, and `lambda0-lambda2=a^2t`; its M terms follow by the same rules on the weight-three virtual block.

* Weight 3: write `v3=sum_i g_i|bar i>`, `sum|g_i|^2=1`, `D3=1-ab=(3+t^2)/4`. Then

\[
\begin{aligned}
A_3&=-atD_3+at^5/D_3,\\
M_3&=-a^2bt I-b^2t(1+t)\operatorname{diag}(|g_i|^2)
 +(t^2b^2+t^5b/D_3)\overline g\,\overline g^{\dagger}.
\end{aligned}\tag{18}
\]

Discarding the negative diagonal and bounding the positive rank-one top-two sum by its trace yields

\[
A_3+K_2(M_3)\le
-\frac{t(1-t)(15+24t+38t^2+32t^3+3t^4)}{32D_3}.
\tag{19}
\]

Here `W00=ab^3-a^4=-atD3`, `V_(bar i,0)=at^3g_i`, and `lambda0-lambda3=atD3`; (18)'s virtual weight-four block uses `V_(i,1111)=bt^3` times the corresponding g and gap `lambda1-lambda4=btD3`.

* Weight 4: put `D4=a^2+b^2=(1+t^2)/2`. The unique normal direction gives

\[
A_4=-tD_4+t^7/D_4,\quad M_4=-abtI,\quad
A_4+K_2(M_4)=-t+t^7/D_4.\tag{20}
\]

All formulas apply for complex amplitudes; complex conjugations are contained in Gamma and the displayed rank-one matrix. For `0<t<=1/200`, the weight-two margin is at least `(15/64)t` since `a^2(1-t^2)>15/64`; (19) has magnitude at least `(15/32)(1-t)t>15t/64`; and (20) has magnitude at least `(1-2t^6)t>15t/64`. Mixed-weight additivity gives

\[
A+K_2(M)\le-15t/64.\tag{21}
\]

The original exploratory `59` checker once emitted a larger weight-two constant after the invalid simplification `a-ab=at`; it was corrected before that checker was pinned. The present proof uses only (17)–(21), not that erroneous constant. The exact interpolation/polarization audit in the dependency table supports the coefficient identities but is **not** a substitute for reviewing their all-variable matrix-unit derivation, signs, or the subsequent remainder.

## 8. Uniform interval: normalized block conjugation

For trace-class X and `t>0`, define

\[
\mathcal H_t(X)=[16\Lambda_{1-t}(X)-\operatorname{Tr}(X)I]/t,
\]

which extends polynomially to t=0. For the actual input (15), put `h=eta sqrt(1-eta^2)`, `D=H_t(|0><0|)`, `V_H=H_t(|v><0|+|0><v|)`, `W_H=H_t(|v><v|-|0><0|)`. The normalization is exact:

\[
H:=\mathcal H_t(\rho)=D+hV_H+\eta^2W_H.\tag{22}
\]

The reference weight-0/weight-1/rest diagonal blocks have gaps

\[
d_0-d_1=2(1+t)^3\ge2,\qquad
d_1-d_2=2(1+t)^2(1-t)\ge2,
\]

and `||D||<5` on the stated interval. Pauli Parseval and the absence of normal weight 0/1 amplitudes give `||V_H||_F<23/200` and `||W_H-W_0||_F<23/200`, where

\[
W_0=\sum_i(\vec r_i(v)-\hat z)\cdot\vec\sigma_i,
\qquad\|W_0\|\le8,\quad\|W_H\|<163/20.
\]

Let `S1` be the anti-Hermitian divided-gap generator, zero within the three reference blocks and satisfying `V_off+[D,S1]=0`. Then `||S1||_F<=23/400`. Define

\[
B=[V_H,S_1]+\tfrac12[[D,S_1],S_1],\quad
\mathcal Q=W_H+B.
\]

The commutator and Parseval bounds yield

\[
\|B\|_F<47/1000,\qquad \|\mathcal Q\|<41/5.
\tag{23}
\]

For the actual off-block estimate, only the transverse part `G=sum_i(r_ix X_i+r_iy Y_i)` of W0 matters. The entire off-block part is exactly its compression to weights at most two, extended by zero; thus `||off W0||<=||G||<=sum_i sqrt(r_ix^2+r_iy^2)<=4`. Together with the Frobenius correction this gives

\[
\|\operatorname{off}\mathcal Q\|<21/5.\tag{24}
\]

Fix `eta<=9/40`. Taylor expansion of the first exact unitary conjugation, with `h^2=eta^2(1-eta^2)`, gives

\[
e^{-hS_1}He^{hS_1}=D+h(V_H)_{\rm diag}+\eta^2\mathcal Q-\eta^4B+R,\qquad\|R\|<\eta^3.\tag{25}
\]

Indeed `exp(2 eta ||S1||)<103/100`, and the cubic coefficient is at most

\[
\frac{103}{100}\left[
\frac{5(2s_1)^3}{6}+\frac{(23/200)(2s_1)^2}{2}
 +\frac{163}{20}(2s_1)\right]
=\frac{580473701}{600000000}<1,
\quad s_1=23/400.
\]

Let `H_*` be the first three terms on the right of (25). By (23),

\[
\|H_*-D\|\le(9/40)(23/200)+(9/40)^2(41/5)=441/1000.
\]

Both actual block separations therefore exceed `2-2(441/1000)>11/10`, including a degenerate weight-one block. If Hermitian blocks satisfy `lambda_min(A)-lambda_max(D0)>=g>0`, then

\[
\begin{bmatrix}A&B_0\\B_0^*&D_0\end{bmatrix}
\le\operatorname{diag}(A+B_0B_0^*/g,D_0+gI),
\tag{26}
\]

because the difference factors as `[B0/sqrt(g);-sqrt(g)I]` times its adjoint. The lower diagonal block is at most `lambda_min(A)I`. Apply (26) first to weight 0 versus its complement, and then inside that complement to weight 1 versus the rest. Cauchy interlacing gives `K3(H_*)<=lambda1(H_*)+K2(compression_without_weight0)`. Using the exact common-Q off-block bound (24), the rescaled leading blocks `(16/t)A,(16/t)M`, and (21),

\[
K_3(H_*)\le K_3(D)-\tfrac{15}{4}\eta^2
 +\frac{3(21/5)^2}{11/10}\eta^4.
\]

The norm difference in (25) changes K3 by at most `3eta^3+3(47/1000)eta^4`. Dividing these errors by eta² and using `eta<=9/40` gives the exact bound

\[
3(9/40)+3(47/1000)(9/40)^2+
\frac{3(21/5)^2}{11/10}(9/40)^2
=54870831/17600000<13/4.
\]

Therefore for this actual input and every actual rank-three Q,

\[
R_3-\operatorname{Tr}[Q\Lambda_{1-t}(\rho)]
\ge R_3-K_3(\Lambda_{1-t}(\rho))\ge t\eta^2/32.
\tag{27}
\]

All quoted constants and block gaps are universal over the entire complex normal sphere and all `0<t<=1/200`; no nondegeneracy of the fourfold block or independent state/projector optimizer is assumed.

## 9. Uniform interval: far states, endpoints, and mixing

For a pure input outside the tube, `eta>=9/40`. Choosing the local majority eigenvectors and applying the commuting-projector union bound gives

\[
1-m\le\tfrac12\sum_i(1-r_i)\le\delta/2,
\quad\delta\ge2\eta^2\ge81/800.
\]

The coefficient `sqrt(39(15-S))-5` in (14) is strictly below 20, since `0<=S<=4`. For `t<=1/200`, `20t<=1/10<81/800`, so the bracket in (14) is strictly positive. The tube is covered by (27), and `eta=0` is a product. At `t=0`, every output is exactly `I/16`; no formula divides by t there.

Fix the SAME actual rank-three Q and average the pure-input bound over a finite spectral decomposition of any density. Equation (6) then covers the negative-shrink physical half, including `p=4/3`. This completes the **written, unreviewed** all-density `t<=1/200` candidate, conditional on the all-variable identities and bounds explicitly displayed in §§7–8. It is not global k3 outside that interval.

## 10. Evidence, source bindings, and exact nonclaims

All named files below are relative to `physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/` unless otherwise specified. They are **immutable source bindings**, not assertions of fresh independent review or novelty:

|Dependency or evidence|SHA256|
|---|---|
|`frontier-20261028-01-spectral-mirror.md`|`4fb86d219a99daf54cbe7ab6c37a6a7fbd11c40009879d63ae135c5195cb4b1c`|
|`frontier-20261028-06-erasure-certificate.md`|`d33fa3cad8f26408e876163d975eb023821b6ab60bea8f220f82bfd1a73d5e2a`|
|`frontier-20261028-08-one-uniform-proof.md`|`980d9f111f3fb685dfec9449b8bfcb325f3761a19ec91bea0615401d7d46cb38`|
|`frontier-20261028-39-fourqubit-purity-certificate.md`|`54bf3245ed4d49d015123b8049988d6e43eb4ce4d12650c25039f24b9a6af471`|
|`frontier-20261028-42-firstorder-common-projector.md`|`c28f17e541cc994c05da80292edcb71dd8a2d4721682789591b3e65dcfca52d2`|
|`frontier-20261028-57-product-hessian-exact.py`|`647ca9ef45936094b0414d143a475fed4089dd263a3b32885221ff338d87c0ec`|
|`frontier-20261028-59-uniform-high-noise-k3.md`|`6f13422e52e6761a3d0d325df821ca78a721ea9c3ad1c8d321043bf93eeb2752`|
|`frontier-20261028-73-hessian-polynomial-audit.py`|`57626c72a11882440c26886b387c718eeb50dccce27a006c7a39ad36701c830e`|
|`frontier-20261028-74-hessian-polynomial-audit-report.md`|`6d4ce6f83845f136fa6af1b7f05a9a9ba6a6da0c680f3bb785fe31ca173900fd`|
|`frontier-20261028-75-offblock-constants-check.py`|`985ee8bb41dbc3bcfd7a75645200b8e697f2038dc85b64fc0c244ab2fd86e8d9`|
|`frontier-20261028-76-offblock-numeric-audit.py`|`e86c18787768a2da54d18ceb4e67db139077f747b65f61da8038dbc860020832`|
|`frontier-20261028-77-offblock-uniform-noise.md`|`04de53eea1187e9a890f263c954c3e05abe7c1e621817bfea24c811ca23eafb2`|
|`frontier-20261028-81-psd-hessian-uniform-noise.md`|`49019845e5ca92b1a90f8c0199c0fcc2ba37301b720117839c42b13469422760`|
|`frontier-20261028-88-normalized-tube-uniform-noise.md`|`2d7aea2d8e95b3db0e547502f7828cab496129a31b569263d0cb6a48ab8fc98c`|
|`frontier-20261028-90-extended-uniform-noise.md`|`0b84f4033848bc269ec2374fd926615f4b0d8cb20792627c9f8b9c3303479349`|
|`frontier-20261028-106-physical-rank3-dual-obstruction.md`|`b596d1dae93a3b4183d99c429bb7e9032c436ae0394d3f71cafb73ce2c4561ae`|
|`frontier-20261028-114-equal-marginal-k3.md`|`78dce15eedb3a2102d32802cb965538193a3719043dffe353016f10637f8ad72`|
|`frontier-20261028-118-low-bloch-sum-k3.md`|`ef9d0813590d08e83a5ad0563787dce03bf8e0357edbb40ac80c6c435d2fb28a`|
|`frontier-20261028-120-harmonic-dual-k3.md`|`090650198b61c252095ab99e08df77a0399b5a090e0c14b66d2d93af1dd5d30b`|
|`frontier-20261028-89-extended-noise-exact.py`|`29e416955676d36b99b6b2bf74811973fa02c317a0125a4d7e0b692e175afbe5`|
|`frontier-20261028-113-equal-marginal-check.py`|`5074896e58a0581b3ef827502535017916035bc230459922b0e2fbe70fcb7a95`|
|`frontier-20261028-115-asymmetric-equal-marginal-check.py`|`ffc16f7b089684123c08ea65ebd05ea3c46ba1a033fc8220968009640d33ed3c`|
|`frontier-20261028-117-unequal-marginal-check.py`|`3ed501c65aa7b2110f0153ab216011c8e11d7890587ffc5b7d38a0a9da9e2ad7`|
|`frontier-20261028-119-harmonic-dual-check.py`|`985b3e44bfcad4887fdf1b44796c7110bfcc2211a5d15acece53c7ef606aa589`|

The source checkers' imported local helpers are bound separately, without treating their output as a universal premise:

|Local checker helper|SHA256|
|---|---|
|`frontier-20261028-02-physical-seesaw.py`|`73d4befebd61820df000ef49c3f768844828e7cb137cb4caa5a0510337ec7587`|
|`frontier-20261028-09-exact-one-uniform-check.py`|`ca5c9fc326c1a17a4035b758757a74b8b5222081015eaa9da9928b0646b357da`|
|`frontier-20261028-12-bloch-gap-check.py`|`72c3efd28cda8e50e01021f9446e8eb6fb29102973de4b28b9ae56ef89718a87`|
|`frontier-20261028-18-anisotropic-w-check.py`|`29935ef6e2d288686a4cfcf7c3e1e6483895e00e124f2bce2a2683ea909f4a0a`|
|`frontier-20261028-26-dicke-pauli-counterexample.py`|`aefeea6ddc56b72a16a90e795232b1837830284f5e4d597088e6f2914d2e1925`|
|`frontier-20261028-31-complex-frame-counterexample.py`|`f88a31f4e283fe2a1d79f643521f0a534f17a9d3583f4073053f0bace7255a07`|
|`frontier-20261028-33-simple-frame-witness.py`|`09bf7cadefdfe1c3638b27b5ca79d21de5ff62dc1bb644b9c74061b3fee993b3`|
|`frontier-20261028-35-entangled-frame-saturation.py`|`aa72723ed285a9a2467b545ee09b2e95c24d55203dce535e5dbea903367daebb`|
|`frontier-20261028-61-perturbation-block-audit.py`|`cb1f90e74265ff58e9cd8bee27c896c578b20862f64e1b6eed56c5d4ad0aff3f`|
|`frontier-20261028-66-noise-endpoint-check.py`|`0a9468089b7677c9846db198bc3b8e18abdd744aa68235b998d5302fbcb6efcc`|
|`frontier-20261028-97-rank6-tail-check.py`|`16e3f2b3ec6572d2d1ff3c8caea863affec342db7e0bf3753b0f44e43555175f`|

The pinned source checkers actually ran under `python3 -B` with their recorded exact rational/LDL/inertia scopes. The `74` report's finite polarization/interpolation argument is expressly bounded to the displayed coefficient identities; exact sample identities, endpoint LDLs, and finite PSD checks do not establish the full all-variable harmonic, moment, Hessian, unitary, or original-channel argument by themselves. All universal content above is the WRITTEN candidate and is awaiting full disjoint review. The complete failed-checker implementation history is disclosed in 114; no failed trial is counted as proof.

Explicit exclusions: neither `F(Q)<=8I` nor `H1(Q)+tilde Q<=10I` is asserted here for every actual rank-three Q; an actual GME rank-three counterexample to a stronger projector-supported bound and another to a fixed-minority PSD shortcut are recorded in 106 and 110 without being original counterexamples. No arbitrary local spectra or independently selected projectors replace an actual joint input/Q; no prior held/withdrawn body, selected guide, numerical optimizer, generic classification, or unreviewed reviewer verdict is imported. The claimed hull is exactly the stated union, not all four-qubit states outside the uniform interval. Original k3 outside these regions and every unaddressed prefix remain open. Parent/f130’s supported `k=5,6,10,11` remains its separate, non-transferable gate. Native dependency-pin clock `Wed Oct 28 21:31:56 PDT 2026`.
