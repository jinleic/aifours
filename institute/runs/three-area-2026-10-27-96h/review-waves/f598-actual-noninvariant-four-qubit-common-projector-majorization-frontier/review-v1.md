# author-candidate-v1.md

## Four-qubit depolarizing majorization on a uniform non-spin-flip-invariant stratum

**Status: WRITTEN AUTHOR CANDIDATE.** This body gives sufficient conditions for the **actual four-qubit channel**, using one arbitrary physical complex consuming projector throughout. It does **not** close unrestricted four-qubit majorization.

The principal conclusions are:

- **Every mixed four-qubit density** with spin-flip defect
  \[
  \left\|\rho-\frac{\rho+\widetilde\rho}{2}\right\|_1^2\le \frac3{13}
  \]
  satisfies every product-reference output-majorization prefix at every physical channel parameter.
- **Every pure four-qubit density** satisfying
  \[
  \eta:=|\langle\psi|\Theta_4\psi\rangle|^2\ge\frac{55}{72}
  \]
  satisfies the same conclusion.
- These scopes contain a universal family of **genuinely four-party-entangled, non-spin-flip-invariant pure states outside the convex hull of the frozen invariant, Dicke-orbit, coherent-vacuum–W4, and biseparable classes**.

No scientific executable, numerical experiment, selected-state probe, external source follow, or repository write was performed. Disjoint review and parent disposition are **NOT_PERFORMED**.

---

## 1. Frozen inputs and actual chronology

Assignment: `f598-actual-noninvariant-four-qubit-common-projector-majorization-frontier`.

The supplied identifiers are:

- Manifest SHA-256: `9476cf69d1a87d9a9c94ab6368b5c62ac3e71ec5848e1595fa24aa5dc3ef30b4`.
- Freeze-receipt SHA-256: `3f7881fd76ff0d27c211435d9719237d6ce6818428762eccb4c2cf05e2cebe52`.
- Literal-packet SHA-256, as recorded in that receipt: `9ab666dafa7c29599022c2896777cfd0bfed3a45ef58d6d4bc2574e788509a2b`.

These are **supplied parent metadata**, not child-native hash recomputations.

I read the entire manifest, freeze receipt, parent dispatch receipt, parent live-metadata supply, and all thirteen listed permission/status controls through their endings. I then sent the required pre-body acknowledgement directly through `agent://Main`.

Only afterward did I read the scientific packet, in ordered raw chunks:

\[
1\!-\!20,\ 21\!-\!40,\ 41\!-\!60,\ 61\!-\!80,\ 81\!-\!100,\ 
101\!-\!120,\ 121\!-\!140,\ 141\!-\!151.
\]

Derivation followed completion of that read.

The scientific inputs used are exactly the packet’s complete S1–S4 bodies:

- **S1:** all mixed spin-flip-invariant four-qubit states, including the physical sharp bound \(K_4(H_3)\le6\).
- **S2:** coherent-vacuum–W4 disposition and the unrestricted pure-state \(H_3\) moment identity.
- **S3:** invariant-sector identities and the physical two-excitation Dicke state.
- **S4:** the already established biseparable scope, used only for comparison.

No linked author, reviewer, checker, source-screen, or held scientific body was opened. Every held episode and its scientific, method, selection, planning, reporting, verification, and confidence consumers remained NONINPUT. This is a documentary access account, not a cognitive-isolation certificate.

---

## 2. Precise theorem

Work on the actual physical tensor space
\[
\mathcal H=(\mathbb C^2)^{\otimes4}.
\]

Let
\[
W=Y^{\otimes4},\qquad
\widetilde\rho=W\rho^TW,\qquad
\sigma=\frac{\rho+\widetilde\rho}{2},
\]
and define
\[
d=d(\rho):=\|\rho-\sigma\|_1
          =\frac12\|\rho-\widetilde\rho\|_1.
\]

Thus \(0\le d\le1\), and \(\sigma\) is an actual spin-flip-invariant density.

Use the actual lifted marginal sums
\[
H_j(\rho)=\sum_{\substack{S\subseteq\{1,2,3,4\}\\|S|=j}}
                 \rho_S\otimes I_{S^c}.
\]

For
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]
put
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\qquad D_t=\operatorname{diag}(a,b)^{\otimes4}.
\]

### Theorem A — mixed-state defect region

For every actual four-qubit density \(\rho\),
\[
d(\rho)^2\le\frac3{13}
\quad\Longrightarrow\quad
\Phi_p^{\otimes4}(\rho)\prec D_t
\qquad\text{for every }p\in[0,4/3].
\]

All sixteen prefixes are included.

### Theorem B — larger pure-state defect region

For an actual pure density \(\rho=|\psi\rangle\langle\psi|\), define
\[
\eta=|\langle\psi|\Theta_4\psi\rangle|^2,
\qquad \Theta_4=W\mathcal K.
\]

Then
\[
\eta\ge\frac{55}{72}
\quad\Longrightarrow\quad
\Phi_p^{\otimes4}(\rho)\prec D_t
\qquad\text{for every }p\in[0,4/3].
\]

For pure inputs,
\[
d^2=1-\eta,
\]
so this is the defect condition \(d^2\le17/72\).

The conclusion also holds for every finite convex mixture of the pure states in Theorem B, by applying the result to one fixed consuming projector before taking the mixture.

These are sufficient regions, not necessary conditions.

---

## 3. Exact imported invariant interface

The nontrivial invariant-sector input is the frozen S1 physical theorem, together with the invariant identities recorded in S1/S3.

For every actual invariant density \(\sigma=\widetilde\sigma\),
\[
H_2(\sigma)=I+H_3(\sigma),\qquad
0\le H_3(\sigma)\le2I,\qquad
\operatorname{Tr}H_3(\sigma)=8,
\]
and
\[
K_4(H_3(\sigma))\le6.
\]

Consequently,
\[
K_k(H_3(\sigma))\le
\begin{cases}
2,&k=1,\\
4,&k=2,\\
6,&k=3,\\
6,&k=4,\\
8,&k\ge5.
\end{cases}
\tag{3.1}
\]

The fourth-prefix improvement from the trivial value \(8\) to \(6\) will be load-bearing for the non-invariant \(H_2\) bound below.

No independent signed SVD is applied to the real and imaginary parts of a non-invariant vector. The imported invariant theorem is used only on the actual invariant density \(\sigma\).

---

## 4. Actual even/odd Pauli identities

For each nonidentity physical Pauli string \(P\), write
\[
r_P=\operatorname{Tr}(\rho P).
\]
Define
\[
R_w=\sum_{\operatorname{wt}(P)=w}r_PP,\qquad
S_w=\sum_{\operatorname{wt}(P)=w}r_P^2.
\]

Pauli orthogonality gives
\[
\rho=\frac1{16}(I+R_1+R_2+R_3+R_4),
\]
and spin flip changes the sign of precisely the odd-weight terms. Therefore
\[
\sigma=\frac1{16}(I+R_2+R_4),\qquad
\Delta:=\rho-\sigma=\frac1{16}(R_1+R_3).
\]

Direct physical partial traces give
\[
H_1=2I+\frac12R_1,
\tag{4.1}
\]
\[
H_2=\frac14(6I+3R_1+R_2),
\tag{4.2}
\]
and
\[
H_3=\frac18(4I+3R_1+2R_2+R_3).
\tag{4.3}
\]

In particular,
\[
H_2(\rho)-H_2(\sigma)=\frac34R_1,
\tag{4.4}
\]
and
\[
H_3(\rho)-H_3(\sigma)=\frac18(3R_1+R_3).
\tag{4.5}
\]

These are identities for the same physical density and tensor positions—not independently chosen marginal operators.

---

## 5. Pure moment identity, reconstructed symbolically

For a pure four-qubit density, Pauli purity and the spin-flip overlap give
\[
S_1+S_3=8(1-\eta).
\tag{5.1}
\]

Equality of complementary marginal purities gives
\[
\sum_i\operatorname{Tr}\rho_i^2
=
\sum_{|S|=3}\operatorname{Tr}\rho_S^2,
\]
hence
\[
2S_2+S_3=12+S_1.
\tag{5.2}
\]

Solving,
\[
S_3=8-8\eta-S_1,\qquad
S_2=2+4\eta+S_1.
\tag{5.3}
\]

From (4.3) and Pauli orthogonality,
\[
\operatorname{Tr}H_3^2
=4+\frac14(9S_1+4S_2+S_3).
\]
Substitution yields
\[
\boxed{\operatorname{Tr}H_3^2=8+3S_1+2\eta.}
\tag{5.4}
\]

Thus the coefficient of \(\eta\) is established by the general physical identities, not inferred from an \(\eta=0\) sample.

For an invariant pure state, \(S_1=0\) and \(\eta=1\), so
\[
\operatorname{Tr}H_3^2=10.
\tag{5.5}
\]

Because \(\Theta_4^2=+I\), every invariant mixed density has a decomposition into \(\Theta_4\)-fixed pure vectors. Convexity of squared Hilbert–Schmidt norm therefore gives
\[
\boxed{\operatorname{Tr}H_3(\sigma)^2\le10}
\tag{5.6}
\]
for every invariant mixed \(\sigma\).

---

## 6. A mixed-state moment bound from the actual defect

Let \(\mathbf r_i\) be the Bloch vector of the actual one-qubit marginal \(\rho_i\).

Every invariant \(\sigma\) has \(\sigma_i=I/2\). Trace-norm contraction under physical partial trace gives
\[
|\mathbf r_i|
=\|\rho_i-I/2\|_1
\le\|\rho-\sigma\|_1=d.
\]
Therefore
\[
S_1=\sum_i|\mathbf r_i|^2\le4d^2.
\tag{6.1}
\]

The Hermitian matrix \(\Delta=\rho-\sigma\) is traceless and has trace norm \(d\). Its positive and negative parts each have trace \(d/2\), so
\[
\operatorname{Tr}\Delta^2\le\frac{d^2}{2}.
\]
Since \(\Delta=(R_1+R_3)/16\),
\[
S_1+S_3=16\operatorname{Tr}\Delta^2\le8d^2.
\tag{6.2}
\]

The even and odd parts in (4.3) are Hilbert–Schmidt orthogonal. Equations (4.5), (5.6), (6.1), and (6.2) imply
\[
\begin{aligned}
\operatorname{Tr}H_3(\rho)^2
&=\operatorname{Tr}H_3(\sigma)^2
  +\frac14(9S_1+S_3)\\
&\le10+\frac14\bigl(8S_1+(S_1+S_3)\bigr)\\
&\le10+10d^2.
\end{aligned}
\]

Hence, for **every actual mixed four-qubit density**,
\[
\boxed{\operatorname{Tr}H_3(\rho)^2\le10(1+d^2).}
\tag{6.3}
\]

This is the first coupling estimate: the physical odd Pauli sectors cannot be varied independently of the defect or of the even invariant density.

---

## 7. Physical rank and moment certificates for \(H_3\)

For every density,
\[
H_3\ge0,\qquad \operatorname{Tr}H_3=8,\qquad H_3\le4I.
\tag{7.1}
\]

For a pure input, the physical single-qubit Pauli identity gives
\[
H_3
=2\rho+\frac12\sum_{i=1}^4\sum_{P=X,Y,Z}P_i\rho P_i.
\tag{7.2}
\]
This is a sum of thirteen positive rank-one operators. Consequently,
\[
\operatorname{rank}H_3\le13
\qquad\text{for pure inputs.}
\tag{7.3}
\]

Now let a positive matrix \(A\) have trace \(8\) and rank at most \(r\), padding its nonzero spectrum with zeros to length \(r\). If \(s=K_k(A)\), Cauchy–Schwarz gives
\[
\operatorname{Tr}A^2
\ge\frac{s^2}{k}+\frac{(8-s)^2}{r-k}.
\tag{7.4}
\]

The expression on the right is strictly increasing past each target \(s=5,6,7\) for \(k=2,3,4\), respectively. Its boundary values are:

| Prefix | Target | \(r=16\) boundary moment | \(r=13\) boundary moment |
|---|---:|---:|---:|
| \(k=2\) | \(5\) | \(92/7\) | \(293/22\) |
| \(k=3\) | \(6\) | \(160/13\) | \(62/5\) |
| \(k=4\) | \(7\) | \(37/3\) | \(445/36\) |

The minimum in the \(r=16\) column is \(160/13\). The minimum in the \(r=13\) column is \(445/36\).

Together with (7.1), this proves
\[
\operatorname{Tr}H_3^2\le\frac{160}{13}
\quad\Longrightarrow\quad
H_3\prec L_3:=(4,1^{\times4},0^{\times11}),
\tag{7.5}
\]
and, for pure inputs,
\[
\operatorname{Tr}H_3^2\le\frac{445}{36}
\quad\Longrightarrow\quad
H_3\prec L_3.
\tag{7.6}
\]

Equality at either moment threshold is allowed.

Applying (6.3):

- If \(d^2\le3/13\), then
  \[
  \operatorname{Tr}H_3^2\le10+\frac{30}{13}=\frac{160}{13}.
  \]
- If the input is pure and \(d^2\le17/72\), then
  \[
  \operatorname{Tr}H_3^2\le10+\frac{170}{72}=\frac{445}{36}.
  \]

Thus both proposed theorem regions have the required **actual \(H_3\) majorization**.

This moment argument alone would not prove the channel theorem. The compatible \(H_2\) estimate is supplied next.

---

## 8. Compatible \(H_2\) majorization when \(d\le1/2\)

From the invariant interface,
\[
H_2(\sigma)=I+H_3(\sigma).
\]
Hence
\[
K_k(H_2(\sigma))\le
\begin{cases}
3,&k=1,\\
6,&k=2,\\
9,&k=3,\\
10,&k=4,\\
k+8,&5\le k\le10.
\end{cases}
\tag{8.1}
\]

For \(k\ge11\), positivity and \(\operatorname{Tr}H_2=24\) provide the bound \(24\).

By (4.4), the remaining operator is exactly
\[
B:=H_2(\rho)-H_2(\sigma)=\frac34R_1.
\]

Apply physical single-qubit rotations that diagonalize the four Bloch vectors. Then
\[
B=\frac34\sum_i r_iZ_i,\qquad 0\le r_i\le d.
\]

For \(d>0\), this is a convex mixture of local bit-flipped conjugates of
\[
dB_0,\qquad B_0=\frac34\sum_iZ_i.
\]
Indeed, choose the sign at site \(i\) with mean \(r_i/d\). The case \(d=0\) is immediate.

The spectrum of \(B_0\) is
\[
(3,(3/2)^{\times4},0^{\times6},(-3/2)^{\times4},-3).
\]
Its relevant prefix sums are
\[
M_1=3,\quad M_2=\frac92,\quad M_3=6,\quad
M_4=\frac{15}{2},\quad M_k=9\quad(5\le k\le10).
\tag{8.2}
\]

For one arbitrary complex rank-\(k\) orthogonal projector \(Q\),
\[
\operatorname{Tr}(QH_2(\rho))
=
\operatorname{Tr}(QH_2(\sigma))+\operatorname{Tr}(QB)
\le K_k(H_2(\sigma))+dM_k.
\tag{8.3}
\]

Compare these bounds with
\[
L_2=(6,3^{\times4},1^{\times6},0^{\times5}).
\]

| \(k\) | Bound for the actual \(K_k(H_2)\) | \(K_k(L_2)\) |
|---|---:|---:|
| 1 | \(3+3d\) | 6 |
| 2 | \(6+\frac92d\) | 9 |
| 3 | \(9+6d\) | 12 |
| 4 | \(10+\frac{15}{2}d\) | 15 |
| \(5\le k\le10\) | \(k+8+9d\) | \(k+13\) |
| \(11\le k\le16\) | 24 | 24 |

Every row is valid when \(d\le1/2\). Thus
\[
\boxed{d\le\frac12\quad\Longrightarrow\quad H_2(\rho)\prec L_2.}
\tag{8.4}
\]

Both principal regions satisfy \(d<1/2\), since
\[
\frac3{13}<\frac14,\qquad \frac{17}{72}<\frac14.
\]

The sharp invariant fourth-prefix input is essential here: replacing \(K_4(H_3(\sigma))\le6\) by the trivial bound \(8\) would not give the displayed fourth-prefix conclusion at \(d=1/2\).

---

## 9. The one-body layer

For every actual density, physical local rotations put
\[
H_1=2I+\frac12\sum_i r_iZ_i,\qquad 0\le r_i\le1.
\]

This is a convex mixture of local bit-flipped conjugates of the product-input one-body layer. Therefore
\[
H_1\prec L_1
:=(4,3^{\times4},2^{\times6},1^{\times4},0).
\tag{9.1}
\]

Also, for every density and \(k\ge1\),
\[
\operatorname{Tr}(Q\rho)\le1
\tag{9.2}
\]
for every rank-\(k\) orthogonal projector \(Q\).

---

## 10. Actual channel and one common consuming projector

On the nonnegative-retention branch,
\[
T_t(X)=tX+b\operatorname{Tr}(X)I,
\]
and the actual four-qubit expansion is
\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3+t^2b^2H_2+tb^3H_1+b^4I.
\tag{10.1}
\]

There are no additional binomial factors outside the subset sums.

Fix **one arbitrary physical complex rank-\(k\) orthogonal projector \(Q\)**. The preceding bounds give
\[
\begin{aligned}
\operatorname{Tr}\!\left(QT_t^{\otimes4}(\rho)\right)
\le{}&
t^4+t^3bK_k(L_3)+t^2b^2K_k(L_2)\\
&+tb^3K_k(L_1)+kb^4.
\end{aligned}
\tag{10.2}
\]

For the product input \(|0000\rangle\), the layers \(\rho,L_3,L_2,L_1,I\) are simultaneously diagonal and co-ordered by Hamming weight. Their weighted sum is exactly \(D_t\).

Equivalently, on a string of weight \(w\), the product \(H_j\) diagonal entry is \(\binom{4-w}{j}\), and the channel expansion sums to
\[
b^w(t+b)^{4-w}=b^wa^{4-w}.
\]

Thus the right side of (10.2) is exactly
\[
K_k(D_t),
\]
not a larger relaxed reference. Taking the supremum over the same class of physical projectors proves every prefix.

No alignment between the actual marginal-layer maximizers is assumed.

### Explicit rank-three and rank-four consumers

The argument gives the following direct inequalities for every physical rank-three \(Q\):
\[
\begin{aligned}
\operatorname{Tr}\!\left(QT_t^{\otimes4}(\rho)\right)
&\le t^4+6t^3b+(9+6d)t^2b^2+10tb^3+3b^4\\
&=K_3(D_t)-(3-6d)t^2b^2.
\end{aligned}
\tag{10.3}
\]

For every physical rank-four \(Q\),
\[
\begin{aligned}
\operatorname{Tr}\!\left(QT_t^{\otimes4}(\rho)\right)
&\le t^4+7t^3b+
       \left(10+\frac{15}{2}d\right)t^2b^2
       +13tb^3+4b^4\\
&=K_4(D_t)-
       \left(5-\frac{15}{2}d\right)t^2b^2.
\end{aligned}
\tag{10.4}
\]

These are load-bearing bounds for the **actual output and actual common projector**. In both theorem regions \(d<1/2\), so these two prefix gaps are strictly positive when \(0<t<1\).

At \(t=0\), both outputs are maximally mixed. At \(t=1\), the reference is pure and majorizes every density.

---

## 11. Physical negative-retention branch

For one qubit,
\[
Y X^T Y=\operatorname{Tr}(X)I-X.
\]
Consequently,
\[
\Phi_{1+t}^{\otimes4}(\rho)
=
W\left(T_t^{\otimes4}(\rho)\right)^TW.
\tag{11.1}
\]

This is a **full transpose**, not a partial transpose.

For an arbitrary consuming projector \(Q\), set
\[
Q'=WQ^TW.
\]
Then \(Q'\) is again a complex orthogonal projector of the same rank, and
\[
\operatorname{Tr}\!\left(
Q\,W\left(T_t^{\otimes4}(\rho)\right)^TW
\right)
=
\operatorname{Tr}\!\left(Q'T_t^{\otimes4}(\rho)\right).
\tag{11.2}
\]

Therefore the same prefix bounds apply on \(p\in[1,4/3]\). This completes Theorems A and B on the entire physical interval.

---

## 12. Relation to the requested \(x+iy\) decomposition

For a pure vector, choose its global phase so that the spin-flip overlap is real and nonnegative. Write
\[
\psi=x+iy,\qquad \Theta_4x=x,\qquad \Theta_4y=y.
\]

Then
\[
\langle x,y\rangle=0,\qquad
\|x\|^2+\|y\|^2=1,
\]
and
\[
\|x\|^2-\|y\|^2=\sqrt\eta.
\]

Hence
\[
d^2=1-\eta=4\|x\|^2\|y\|^2.
\tag{12.1}
\]

The pure theorem therefore controls the entire stratum
\[
4\|x\|^2\|y\|^2\le\frac{17}{72}.
\]

It does not assume that the same physical local rotations independently put \(x\) and \(y\) into separate signed-SVD normal forms. Their simultaneous physical compatibility is retained through the actual even/odd Pauli identities, physical marginal contraction, and the common-projector channel bounds.

---

## 13. Strict addition beyond the four named frozen classes

This section uses the frozen literal Dicke vector, but does not choose a new diagnostic vector or parameter value.

Let
\[
|D\rangle=\frac1{\sqrt6}\sum_{|z|=2}|z\rangle.
\]
It satisfies \(\Theta_4D=D\).

Let \(y\) be **any** unit vector satisfying
\[
\Theta_4y=y,\qquad \langle D,y\rangle=0.
\]
For every parameter
\[
0<\theta<\frac\pi4,\qquad
\sin^2(2\theta)\le\frac{17}{72},
\]
define
\[
\psi_{\theta,y}=\cos\theta\,D+i\sin\theta\,y.
\tag{13.1}
\]

This is a universal parameterized family, not a selected-state probe. It has
\[
\eta=\cos^2(2\theta)\in[55/72,1),
\]
so Theorem B applies.

### Genuine four-party entanglement

Across each singleton cut, the Dicke vector has Schmidt coefficients
\[
1/\sqrt2,\quad1/\sqrt2.
\]
Across each balanced cut, its nonzero Schmidt coefficients are
\[
2/\sqrt6,\quad1/\sqrt6,\quad1/\sqrt6.
\]

Thus its second Schmidt singular value is at least \(1/\sqrt6\) on every cut.

Because \(\sin^2(2\theta)\le17/72<1/4\),
\[
\theta<\frac\pi{12}.
\]
Moreover,
\[
\|\psi_{\theta,y}-D\|
=2\sin(\theta/2)
\le\theta
<\frac\pi{12}
<\frac13
<\frac1{\sqrt6}.
\]

For every cut, the operator norm of the coefficient-matrix perturbation is bounded by this vector norm. The singular-value perturbation inequality therefore leaves the second Schmidt singular value strictly positive on all seven cuts.

Every state in (13.1) is consequently genuinely four-party entangled.

### Separation from the named classes

The absolute spin-flip overlap is invariant under physical local unitaries.

- Pure invariant states and the Dicke orbit have \(\eta=1\).
- The frozen coherent-vacuum–W4 orbit has \(\eta=0\).
- The family (13.1) has \(55/72\le\eta<1\).
- Its genuine entanglement excludes every pure biseparable component.

Finally, a positive convex combination equal to a rank-one density must have every nonzero component supported on that same ray. Therefore these new pure states cannot lie in the convex hull of the four named frozen classes, including mixed invariant components.

This establishes a **strict extension relative to those classes**. It is not a literature-wide novelty claim, and it does not assert that every mixed state in the defect region is genuinely entangled.

---

## 14. Exact remaining unrestricted frontier

The unrestricted four-qubit theorem is **NOT_PROVED**.

The established new uniform regions are:

\[
\boxed{d(\rho)^2\le3/13\quad\text{for arbitrary mixed inputs},}
\]
and
\[
\boxed{\eta\ge55/72\quad\text{for pure inputs},}
\]
together with finite convex mixtures of the latter and the separately frozen prior classes.

Outside those regions:

- The general physical estimate
  \[
  \operatorname{Tr}H_3^2\le10(1+d^2)
  \]
  remains valid.
- The parameter-dependent \(H_2\) table in §8 remains valid.
- Their failure to establish the reference bounds is **not** an \(H_2\), \(H_3\), or channel counterexample.
- A global proof still requires stronger actual compatible-layer or directly weighted common-projector control. It cannot be obtained by independently optimizing incompatible \(H_2/H_3\) relaxations.
- No unrestricted ancillary tensorization, general blocklength result, or arbitrary-dimension conclusion follows.

No physical counterexample was produced.

---

## 15. Evidence and acceptance limits

All new work above is written algebra and general-variable argument. The only nontrivial previously adopted theorem imported into the new \(H_2\) step is the frozen physical invariant-sector interface, especially its sharp \(K_4(H_3)\le6\).

- Scientific programs prepared or executed: **none**.
- Numerical results claimed: **none**.
- Fresh selected vectors or parameter probes: **none**.
- Public-source follow or novelty audit: **not performed**.
- Independent written reconstruction of this candidate: **not performed**.
- Independent finite physical corroboration: **not performed**.
- Parent mathematical disposition: **not performed**.
- Human, independent-model-family, or formal-kernel verification: **not performed**.

No experiment code or execution results are omitted: there was no computational experiment. No repository file was written; this is the complete body for Main materialization.