# Author candidate v1 — Arbitrary three-qubit depolarizing majorization and the full four-qubit \(1|3\)-separable extension

**Status: AUTHOR / PROOF CANDIDATE / NOT INDEPENDENTLY ACCEPTED.**

**Materialization:** This is the complete body for `author-candidate-v1.md` in the assigned F463 wave. No repository file was written. No scientific program, solver, CAS, build, test, or numerical experiment was executed.

## 1. Claimed result and exact scope

Let
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]
and define
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2}.
\]
For a Hermitian matrix \(X\), write \(K_k(X)\) for the sum of its \(k\) largest eigenvalues.

### Theorem A — Every complex three-qubit input

For every three-qubit density operator \(\rho\), every physical \(p\), every \(k=1,\ldots,8\), and every complex orthogonal rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes3}(\rho)\right]
\le K_k\!\left(\Phi_p^{\otimes3}(\rho)\right)
\le K_k\!\left(\operatorname{diag}(a,b)^{\otimes3}\right).
\tag{1}
\]

There is **no parity, reality, Schmidt-basis, permutation-symmetry, or local-unitary-normal-form restriction** on \(\rho\).

### Theorem B — Every four-qubit \(1|3\)-separable input

For every four-qubit state separable across any specified single-qubit-versus-three-qubit cut,
\[
\Phi_p^{\otimes4}(\rho)\prec
\operatorname{diag}(a,b)^{\otimes4}.
\tag{2}
\]
The same holds for the convex hull over all four choices of the single-qubit side.

Thus every complex rank-\(k\) projector on the full sixteen-dimensional space obeys the corresponding product-reference prefix bound. In particular, for \(k=3\),
\[
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
\le a^4+2a^3b.
\tag{3}
\]

These are claimed mathematical conclusions of the proof below, not parent dispositions or independent verification results. The unrestricted four-qubit theorem remains unproved here.

---

## 2. Input audit, chronology, and methods

### Frozen-input coverage

Before deriving the argument below, I read:

1. The manifest, freeze receipt, parent live-metadata supply, and dispatch receipt.
2. All ten status/permission controls listed in the manifest, including the F439/F444/F448 quarantines.
3. The complete ordered literal packet, in successive ranges \(1\!-\!180\), \(181\!-\!370\), \(371\!-\!570\), \(571\!-\!755\), and \(756\!-\!832\):
   - S1: lines \(1\!-\!41\);
   - S2: logical lines \(1\!-\!711\), including its ending;
   - S3: lines \(1\!-\!15\);
   - S4: lines \(1\!-\!21\);
   - S5: lines \(1\!-\!42\).

The manifest and receipt pins supplied for this assignment are:

- Manifest: `27ce89c6da03e57eb79f50f745de93db6fc615d1f8ed871fabc3479b15853baf`.
- Receipt: `8c02870311df95afbfc1bfc8b6d33fe52e2eb3ff293f36e609ea104a02805c75`.
- Literal packet, according to the parent metadata supply: `082d4d2c44ea839d19b84aba9ec384ad32471afc38db44d5267db6d81b44dd05`.

The clock, byte counts, LF counts, hash observations, and assertion that the assigned pins match are **parent-attributed metadata**. I did not independently execute hashing or obtain a child-native clock observation.

### Scientific chronology

After completing the ordered packet, I developed the spin-flip and paired-projection argument in Sections 4–6 using written algebra. I subsequently read the introduction through Theorem 4/Remark 5 and the discussion of the public Song–Wang–Tomamichel–Fang paper cited in Section 11. A bounded web search also returned a generated search summary; that summary supplies no proof premise or independent verification.

The exact selected state in Section 9 was chosen during this GENERAL AUTHOR duty. It is an authorized fresh written example, not an imported WRITTEN-review diagnostic.

### Method boundaries

- No held scientific payload or held consumer was opened as a research input.
- The quarantine records were used for status and exclusions only.
- No sibling research return or author program was imported.
- No scientific executable, package installation, external-model CLI, paid/heavy/remote computation, or filesystem-write bypass was used.
- There are **no program outputs, execution results, or computational verification claims** in this return.
- Numerical fractions in Section 9 are written exact arithmetic, with the inputs and derivation displayed.
- This return supplies a proof candidate, not a clean-cognition certificate, novelty determination, independent-family review, human review, or formal/kernel proof.

---

## 3. Spectral facts used

For Hermitian \(X\),
\[
K_k(X)=\max_{\substack{Q=Q^\dagger=Q^2\\ \operatorname{rank}Q=k}}
\operatorname{Tr}(QX).
\tag{4}
\]
Consequently:

1. \(K_k\) is convex.
2. \(K_k(X+Y)\le K_k(X)+K_k(Y)\).
3. If every \(X_s\prec D\), then every convex combination \(\sum_s w_sX_s\prec D\), provided the traces agree.

These statements apply to arbitrary complex projectors.

The argument below will bound each term of the **actual channel expansion for the same fixed \(Q\)**. The reference terms have a common decreasing eigenvalue order, so their prefix bounds add exactly to the desired reference—not to a larger relaxation.

---

## 4. Actual marginal sums and the three-qubit spin flip

For a three-qubit density \(\rho\), define the unnormalized lifted marginal sums
\[
H_1(\rho)=
\rho_A\otimes I_B\otimes I_C+
I_A\otimes\rho_B\otimes I_C+
I_A\otimes I_B\otimes\rho_C,
\tag{5}
\]
and
\[
H_2(\rho)=
\rho_{AB}\otimes I_C+
\rho_{AC}\otimes I_B+
I_A\otimes\rho_{BC},
\tag{6}
\]
where every term occupies its indicated physical tensor factors.

Both sums are positive, and
\[
\operatorname{Tr}H_1=12,\qquad
\operatorname{Tr}H_2=6.
\tag{7}
\]

Let \(Y\) be the Pauli \(Y\) matrix, let \(\mathcal K\) denote computational-basis complex conjugation, and put
\[
\Theta=Y^{\otimes3}\mathcal K.
\tag{8}
\]
This antiunitary satisfies
\[
\Theta^2=-I.
\tag{9}
\]
For Hermitian \(X\), write
\[
\widetilde X=\Theta X\Theta^{-1}
=Y^{\otimes3}X^T Y^{\otimes3}.
\tag{10}
\]

The one-qubit identity
\[
YX^TY=\operatorname{Tr}(X)I-X
\tag{11}
\]
gives, by tensor expansion,
\[
\widetilde\rho
=I_8-H_1(\rho)+H_2(\rho)-\rho.
\tag{12}
\]

This identity retains the complete input state, including every complex cross-parity coherence.

### Pure-input consequence

Suppose now that
\[
\rho=|\psi\rangle\langle\psi|.
\]
Because \(\Theta^2=-I\), the vectors \(\psi\) and \(\Theta\psi\) are orthogonal. For completeness, antiunitarity gives
\[
\langle\Theta\psi,\Theta^2\psi\rangle
=\langle\Theta\psi,\psi\rangle,
\]
whereas \(\Theta^2\psi=-\psi\) makes the left-hand side the negative of the right-hand side.

Therefore
\[
P=\rho+\widetilde\rho
\tag{13}
\]
is an orthogonal rank-two projector, and
\[
\widetilde P=P.
\tag{14}
\]

Rearranging (12),
\[
H_2=P+H_1-I.
\tag{15}
\]
Also,
\[
\widetilde H_1=3I-H_1,
\tag{16}
\]
since each one-qubit density is sent to its complementary density while identity factors remain identities.

Applying the spin flip to (15) and adding yields the central exact coupling:
\[
\boxed{H_2+\widetilde H_2=I+2P.}
\tag{17}
\]

The positivity of both summands follows from the actual marginal construction and positivity preservation by the full spin flip.

---

## 5. The two-body marginal-sum majorant

### Lemma

For every pure complex three-qubit input,
\[
H_2(\rho)\prec
L_2:=\operatorname{diag}(3,1,1,1,0,0,0,0).
\tag{18}
\]

### Proof

Set
\[
G=I+2P,\qquad
Z=G^{-1/2}H_2G^{-1/2}.
\tag{19}
\]
The matrix \(G\) is strictly positive: its eigenvalues are \(3\) on \(\operatorname{ran}P\) and \(1\) on its orthogonal complement. It is invariant under \(\Theta\).

Equation (17) consequently implies
\[
Z+\widetilde Z=I.
\tag{20}
\]
Since both terms are positive,
\[
0\le Z\le I.
\tag{21}
\]

#### 5.1 Paired spectral decomposition of \(Z\)

If \(Zu=\lambda u\), then (20) gives
\[
Z(\Theta u)=(1-\lambda)\Theta u.
\tag{22}
\]

An orthonormal eigenbasis can therefore be chosen as
\[
u_1,\Theta u_1,\ldots,u_4,\Theta u_4,
\]
with
\[
Z=\sum_{i=1}^4
\left[
\lambda_i|u_i\rangle\langle u_i|
+(1-\lambda_i)|\Theta u_i\rangle\langle\Theta u_i|
\right],
\qquad 0\le\lambda_i\le1.
\tag{23}
\]

For eigenvalues different from \(1/2\), pair the two complementary eigenspaces using \(\Theta\). The \(1/2\)-eigenspace is \(\Theta\)-invariant; it admits orthonormal pairs \(u,\Theta u\) because \(\Theta^2=-I\). This also proves that its dimension is even.

For each binary choice \(s=(s_1,\ldots,s_4)\), let \(\Pi_s\) select exactly one vector from each pair. Thus \(\Pi_s\) is an orthogonal rank-four projector and
\[
\widetilde\Pi_s=I-\Pi_s.
\tag{24}
\]

Give this choice weight
\[
w_s=\prod_{i=1}^4
\begin{cases}
\lambda_i,&s_i=0,\\
1-\lambda_i,&s_i=1.
\end{cases}
\tag{25}
\]
These nonnegative weights sum to one, including when some \(\lambda_i\) are \(0\) or \(1\). Equation (23) becomes
\[
Z=\sum_s w_s\Pi_s.
\tag{26}
\]
Hence
\[
H_2=\sum_s w_s X_s,\qquad
X_s=G^{1/2}\Pi_sG^{1/2}.
\tag{27}
\]

#### 5.2 Spectrum of each \(X_s\)

Because \(P\) is invariant under \(\Theta\), while \(\widetilde\Pi_s=I-\Pi_s\),
\[
\operatorname{Tr}(P\Pi_s)
=\operatorname{Tr}(P\widetilde\Pi_s)
=2-\operatorname{Tr}(P\Pi_s).
\tag{28}
\]
Here the trace is real; antiunitary conjugation conjugates a trace, and the trace of the product of two Hermitian matrices is real.

Therefore
\[
\operatorname{Tr}(P\Pi_s)=1.
\tag{29}
\]

The compression
\[
\Pi_sP\Pi_s\big|_{\operatorname{ran}\Pi_s}
\]
is positive, has rank at most two, and has trace one. Its four eigenvalues are consequently
\[
\eta,\ 1-\eta,\ 0,\ 0
\qquad\text{for some }0\le\eta\le1.
\tag{30}
\]

The four nonzero eigenvalues of \(X_s\) are the eigenvalues of the compression of \(G\) to \(\operatorname{ran}\Pi_s\). Thus its full spectrum is
\[
\left(
1+2\eta,\ 3-2\eta,\ 1,\ 1,\ 0,\ 0,\ 0,\ 0
\right),
\tag{31}
\]
up to decreasing rearrangement.

Its largest eigenvalue is at most \(3\). Its top-two sum is \(4\), its top-three sum is \(5\), and its total trace is \(6\). Thus
\[
X_s\prec L_2.
\tag{32}
\]

Finally, (27) and convexity of every \(K_k\) prove (18). ∎

### Mixed-input extension

The map \(\rho\mapsto H_2(\rho)\) is linear. Spectrally decomposing any mixed \(\rho\) into pure states and applying convexity gives
\[
\boxed{H_2(\rho)\prec L_2}
\tag{33}
\]
for every three-qubit density.

The pure-state rank-two coupling was essential to the proof. No analogous assertion was assumed for freely chosen matrices with only matching global and marginal spectra.

---

## 6. The one-body marginal-sum majorant

For every three-qubit density,
\[
H_1(\rho)\prec
L_1:=\operatorname{diag}(3,2,2,2,1,1,1,0).
\tag{34}
\]

Here is a direct mixed-unitary proof.

Diagonalize each one-qubit marginal:
\[
\rho_i=V_i
\operatorname{diag}(q_i,1-q_i)V_i^\dagger,
\qquad 0\le q_i\le1.
\tag{35}
\]
Let
\[
L_1^{\mathrm{comp}}
=|0\rangle\langle0|_A\otimes I_{BC}
+|0\rangle\langle0|_B\otimes I_{AC}
+|0\rangle\langle0|_C\otimes I_{AB}.
\tag{36}
\]
Its spectrum is precisely that in (34).

Independently choose a bit \(s_i\), with probabilities \(q_i\) for \(s_i=0\) and \(1-q_i\) for \(s_i=1\), and put
\[
U_s=\bigotimes_{i=A,B,C}V_iX^{s_i}.
\tag{37}
\]
Averaging the conjugates \(U_sL_1^{\mathrm{comp}}U_s^\dagger\) gives exactly \(H_1(\rho)\). Therefore \(H_1\) is a convex combination of unitary conjugates of \(L_1^{\mathrm{comp}}\), proving (34).

This argument permits arbitrary complex marginal eigenbases and does not require their compatibility with a pure-state normal form.

---

## 7. Proof of all eight three-qubit prefixes

First consider the nonnegative-parameter channel
\[
T_t(X)=tX+b\,\operatorname{Tr}(X)I,
\qquad b=\frac{1-t}{2},\quad 0\le t\le1.
\tag{38}
\]

Its actual three-qubit tensor expansion is
\[
\boxed{
T_t^{\otimes3}(\rho)
=t^3\rho+t^2b\,H_2(\rho)+tb^2\,H_1(\rho)+b^3I_8.
}
\tag{39}
\]

For any fixed complex rank-\(k\) projector \(Q\), \(k\ge1\),
\[
\begin{aligned}
\operatorname{Tr}\!\left[QT_t^{\otimes3}(\rho)\right]
&=t^3\operatorname{Tr}(Q\rho)
+t^2b\,\operatorname{Tr}(QH_2)
+tb^2\,\operatorname{Tr}(QH_1)+kb^3\\
&\le t^3+t^2b\,K_k(L_2)+tb^2\,K_k(L_1)+kb^3.
\end{aligned}
\tag{40}
\]

All coefficients are nonnegative.

The relevant prefix sums are:

| \(k\) | \(K_k(L_2)\) | \(K_k(L_1)\) |
|---:|---:|---:|
| 1 | 3 | 3 |
| 2 | 4 | 5 |
| 3 | 5 | 7 |
| 4 | 6 | 9 |
| 5 | 6 | 10 |
| 6 | 6 | 11 |
| 7 | 6 | 12 |
| 8 | 6 | 12 |

To identify the right-hand side of (40), apply the same expansion to \(|000\rangle\langle000|\). Order the computational basis by Hamming weight.

The four reference coefficient matrices are then diagonal in a common decreasing order:

- \(|000\rangle\langle000|\): eigenvalues \((1,0,\ldots,0)\);
- its two-body marginal sum: \((3,1,1,1,0,0,0,0)\);
- its one-body marginal sum: \((3,2,2,2,1,1,1,0)\);
- \(I_8\).

Their positively weighted sum is
\[
\operatorname{diag}(a,b)^{\otimes3},
\qquad a=t+b=\frac{1+t}{2}.
\tag{41}
\]

Indeed, the values on Hamming weights \(0,1,2,3\) are respectively
\[
\begin{aligned}
&t^3+3t^2b+3tb^2+b^3=a^3,\\
&t^2b+2tb^2+b^3=a^2b,\\
&tb^2+b^3=ab^2,\\
&b^3.
\end{aligned}
\tag{42}
\]

Consequently, the right-hand side of (40) is **exactly**
\[
K_k\!\left(\operatorname{diag}(a,b)^{\otimes3}\right).
\tag{43}
\]

Writing \(u=a^3\), \(d=a^2b\), \(c=ab^2\), and \(\ell=b^3\), the eight bounds are therefore
\[
u,\quad u+d,\quad u+2d,\quad u+3d,\quad
u+3d+c,\quad u+3d+2c,\quad u+3d+3c,\quad1.
\tag{44}
\]

This establishes every prefix for every density \(\rho\).

### Why no incompatible-maximizer shortcut occurs

Equation (40) uses the same actual \(Q\) throughout. Uniform termwise bounds are legitimate upper bounds for that \(Q\), whether or not they can be attained together. Their sum has the required value because the **reference coefficient matrices** are co-ordered. No simultaneous attainment by the actual input is asserted or required.

There is no parity pinching, and no cross-parity block is discarded.

### Endpoints

No division by \(t\), \(b\), a population, an eigenvalue gap, or a marginal eigenvalue occurs.

- At \(t=0\), (39) gives \(I_8/8\).
- At \(t=1\), the reference is pure and (40) reduces to \(\operatorname{Tr}(Q\rho)\le1\).
- The normalizing matrix \(G=I+2P\) always has eigenvalues \(1\) and \(3\), so its inverse square root is harmless.

---

## 8. Full physical interval, including \(p>1\)

Write \(s=1-p\). The physical interval is
\[
-\frac13\le s\le1,
\tag{45}
\]
as follows from the Pauli-channel probabilities
\[
q_I=\frac{1+3s}{4},
\qquad q_X=q_Y=q_Z=\frac{1-s}{4}.
\tag{46}
\]

For one qubit, let
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X.
\tag{47}
\]
Then
\[
T_{-t}=\mathcal J\circ T_t.
\tag{48}
\]
For every \(n\),
\[
T_{-t}^{\otimes n}(\rho)
=W_n\,[T_t^{\otimes n}(\rho)]^T W_n,
\qquad W_n=Y^{\otimes n}.
\tag{49}
\]

This is full transpose, so the two outputs have identical spectra.

For a complex orthogonal projector \(Q\),
\[
\operatorname{Tr}\!\left[QT_{-t}^{\otimes n}(\rho)\right]
=
\operatorname{Tr}\!\left[Q'T_t^{\otimes n}(\rho)\right],
\qquad
Q'=W_nQ^TW_n.
\tag{50}
\]
The transported \(Q'\) is again an orthogonal projector of the same rank. The two signs from \(W_n^T=(-1)^nW_n\) cancel in deriving (50), including for odd \(n\).

The physical negative branch needs only \(0\le t\le1/3\), already covered by Section 7. The pure one-qubit product reference has eigenvalues \(a,b\), possibly exchanged. Its tensor-power spectrum is therefore the reference used above.

This completes the proof of Theorem A.

---

## 9. An exact genuinely cross-parity example outside every local-parity sector

Consider the normalized pure state
\[
|\psi_*\rangle
=\frac{|000\rangle+|001\rangle+|010\rangle+|100\rangle}{2}.
\tag{51}
\]

It has nonzero coherences between the even vector \(|000\rangle\) and the three odd vectors. More strongly, it is **not** a parity eigenstate in any physical local bases.

### 9.1 Excluding every local-parity representation

Each one-qubit marginal is
\[
m=
\begin{pmatrix}
3/4&1/4\\
1/4&1/4
\end{pmatrix}
=\frac12\left(I+\frac{X+Z}{2}\right).
\tag{52}
\]
Its eigenvalues are
\[
\frac{1\pm1/\sqrt2}{2},
\tag{53}
\]
so it is nondegenerate.

If a pure state is an eigenvector of \(A_1\otimes A_2\otimes A_3\), where each \(A_i\) is a traceless Hermitian one-qubit unitary, then each \(A_i\) commutes with the corresponding marginal. Equation (52) therefore forces
\[
A_i=\pm H,\qquad H=\frac{X+Z}{\sqrt2}.
\tag{54}
\]

However,
\[
\langle\psi_*|H^{\otimes3}|\psi_*\rangle
=\frac{5}{4\sqrt2},
\qquad
\left|\frac{5}{4\sqrt2}\right|^2=\frac{25}{32}<1.
\tag{55}
\]
To obtain (55), sum the Hadamard matrix signs on
\[
S=\{000,001,010,100\}.
\]
The \(000\) row contributes \(4\), and each of the other three rows contributes \(2\), for a total of \(10\); the normalization is \(4\sqrt8\).

Changing the signs in (54) changes only the overall sign of (55). Thus \(\psi_*\) cannot be a local-parity eigenstate.

Because a positive convex combination equal to a rank-one density must have every positive-weight component supported on that same ray, \(|\psi_*\rangle\langle\psi_*|\) is also outside the convex hull of all local-basis parity-preserving densities.

Theorem A therefore covers genuinely unpaid cross-parity inputs, rather than merely re-expressing the adopted parity sector.

### 9.2 Exact written physical-channel expectation

This is an exact written calculation, **not an executed finite check**.

At
\[
p=\frac14,\qquad t=\frac34,\qquad b=\frac18,
\tag{56}
\]
take the same actual rank-one projector
\[
Q_*=|\psi_*\rangle\langle\psi_*|.
\]

Equation (52) gives
\[
\operatorname{Tr}(m^2)=\frac34.
\tag{57}
\]
Purity of the full input makes each complementary two-qubit marginal have the same nonzero spectrum as its single-qubit marginal. Hence
\[
\operatorname{Tr}(Q_*H_1)
=\operatorname{Tr}(Q_*H_2)=\frac94.
\tag{58}
\]

Using the actual expansion (39),
\[
\begin{aligned}
\operatorname{Tr}\!\left[
Q_*T_{3/4}^{\otimes3}(Q_*)
\right]
&=t^3+\frac94(t^2b+tb^2)+b^3\\
&=\frac{623}{1024}
<\frac{686}{1024}
=\left(\frac78\right)^3.
\end{aligned}
\tag{59}
\]

This is an actual state/channel/projector expectation. It is not asserted to be the largest output eigenvalue and does not replace the universal prefix proof.

Arbitrary complex local-unitary images of this example are also covered.

---

## 10. Proof of the full four-qubit \(1|3\)-separable consequence

For every one-qubit density \(\sigma\), its channel output has ordered eigenvalues
\[
\frac{1+tr}{2},\qquad\frac{1-tr}{2},
\qquad 0\le r\le1,
\tag{60}
\]
so
\[
\Phi_p(\sigma)\prec D_{1,t}:=\operatorname{diag}(a,b).
\tag{61}
\]

We use positive tensor preservation of majorization. Here is a direct proof.

If \(X\prec X_0\) and \(Y\prec Y_0\) are positive matrices, diagonalize \(X\), with eigenvalues \(x_i\ge0\). Then
\[
K_k(X\otimes Y)
=
\max_{\substack{0\le k_i\le\dim Y\\\sum_i k_i=k}}
\sum_i x_iK_{k_i}(Y)
\le K_k(X\otimes Y_0).
\tag{62}
\]
Now diagonalize \(Y_0\) and apply the same argument to \(X\prec X_0\). Thus
\[
X\otimes Y\prec X_0\otimes Y_0.
\tag{63}
\]

For an arbitrary three-qubit density \(\tau\), Theorem A and (61) therefore imply
\[
\Phi_p(\sigma)\otimes\Phi_p^{\otimes3}(\tau)
\prec D_{1,t}\otimes D_{3,t}
=D_{4,t}.
\tag{64}
\]

If a four-qubit state is \(1|3\)-separable,
\[
\rho=\sum_j w_j\,\sigma_j\otimes\tau_j,
\tag{65}
\]
then for the same fixed complex rank-\(k\) projector \(Q\),
\[
\begin{aligned}
\operatorname{Tr}\!\left[Q\Phi_p^{\otimes4}(\rho)\right]
&=\sum_jw_j
\operatorname{Tr}\!\left[
Q\bigl(\Phi_p(\sigma_j)\otimes\Phi_p^{\otimes3}(\tau_j)\bigr)
\right]\\
&\le\sum_jw_j K_k(D_{4,t})\\
&=K_k(D_{4,t}).
\end{aligned}
\tag{66}
\]

Physical qubit permutations are unitary conjugations. The same argument consequently permits a different spectator position in each convex-mixture component.

The ordered reference eigenvalues are
\[
a^4,\quad
a^3b\ \text{(four copies)},\quad
a^2b^2\ \text{(six copies)},\quad
ab^3\ \text{(four copies)},\quad
b^4,
\tag{67}
\]
which establishes every one of the sixteen prefixes and (3).

No claim is made that there is an input-independent postprocessing channel.

---

## 11. Relation to the frozen inputs and public literature

### What supplies the missing coupling

The adopted parity proof used explicit parity blocks and a coupled deficit estimate. The present argument does not discard the cross-parity block or assume a local-parity normal form.

Instead, it uses the actual pure-state identity
\[
H_2+\widetilde H_2=I+2(\rho+\widetilde\rho),
\tag{68}
\]
where \(\rho+\widetilde\rho\) is an invariant rank-two projection. This is a constraint on marginal sums arising from the **same actual input**.

The weakened tensorization countermodel in S4 is not used as a physical channel input or as a theorem counterexample. Global and marginal spectral bounds alone do not supply (68). The present proof therefore does not invoke the insufficient implication diagnosed there.

The one-leg ancillary theorem in S3 is also not being iterated. The proof works directly with the actual three-leg tensor expansion.

### Public-source qualification

The read portions of [Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1](https://arxiv.org/html/2609.37240v1) state:

- the general exact output-majorization relation as a conjecture in Equation (2);
- an asymptotic approximate-majorization theorem;
- an exact shifted-log-determinant ordering in Theorem 4;
- in the discussion, full majorization in general as an open direction.

Those statements are context, not premises in Sections 4–8. The proof here does not replace exact prefixes by norm inequalities, determinant ordering, or approximation.

No exhaustive priority audit was conducted. The earlier stronger printed claims noted in the frozen packet retain their existing source/proof qualifications. **No first-result, novelty, or journal-source-equivalence claim is made.**

---

## 12. Exact conclusions, nonconclusions, and remaining acceptance gates

### Mathematical conclusions claimed by this candidate

1. All eight exact output prefixes for every arbitrary complex three-qubit density.
2. The complete physical parameter interval \(0\le p\le4/3\), including all endpoints.
3. Arbitrary complex consuming projectors, with correct full-transpose transport on the negative branch.
4. All sixteen prefixes for every four-qubit \(1|3\)-separable state, including the convex hull over varying single-qubit cuts.
5. Coverage genuinely beyond local-parity inputs, witnessed by the exact state in (51).

### Not established here

- Unrestricted four-qubit majorization, including genuinely four-party-entangled inputs.
- The unrestricted four-qubit \(k=3\) target.
- General blocklength \(n\), general local dimension \(d\), or tensorization with an arbitrary auxiliary channel.
- The full older group-channel propositions or their iteration.
- An independent finite verification, interval-certified computation, human review, independent-family review, or formal/kernel proof.
- Novelty, priority, or equivalence to an uninspected journal proof.

The load-bearing new acceptance obligation is a disjoint reconstruction of the paired-projection lemma and its use in the co-ordered coefficient expansion. Parent disposition is still required.

**Completed deliverable:** a self-contained written proof candidate for unrestricted complex three-qubit depolarizing-output majorization, its actual four-qubit \(1|3\)-separable tensor/mixture consequence, and an exact non-parity-LU physical example. All scientific execution remains **NOT RUN**; all genuine held episodes and consumers remain **NONINPUT**.