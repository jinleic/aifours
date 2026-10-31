# Author candidate v1 — Four-qubit \(H_3\) bounds and full depolarizing majorization for a coherent vacuum–\(W_4\) family

**Status: AUTHOR / WRITTEN PROOF CANDIDATE / NOT INDEPENDENTLY ACCEPTED.**

**Original unrestricted target: NOT PROVED. No physical counterexample is constructed.**

This candidate supplies:

1. An exact \(H_3\)-majorization argument for an entire coherent vacuum–\(W_4\) family, including genuinely four-partite-entangled states outside the previously adopted classes.
2. An exact \(H_2\)-majorization argument for the same family.
3. Consequently, all sixteen actual depolarizing-output prefixes for that family, arbitrary complex local-unitary images, and their finite convex mixtures, throughout the physical parameter interval.
4. A separate, unrestricted-input sufficient condition for the \(H_3\) bound, expressed through its second moment.

The unrestricted four-qubit statement remains explicitly unpaid. No layer failure or channel failure is inferred.

## 1. Materialization, provenance, and methods

This is the complete proposed body of `author-candidate-v1.md` for the assigned F480 wave. No repository file was written.

The supplied pins are:

- Manifest: `2b74a0cd425fea32d127470a0e3d6ac42401423288dc33dd78188eab6a202a48`.
- Freeze receipt: `0145a614e0c6de1aefbce311d88eeae4f10c8a8f3da436db682ca4a716d0859b`.
- Literal packet, from parent metadata: `eec5650f88a53d6aff09668bb808efe9b341790776a6acb3959e7b596026d029`.

These hashes, byte/LF counts, and the recorded clock `2026-10-30T12:13:16-0700 PDT` are **parent-attributed metadata**, not child-native hash or clock observations.

### Read chronology

Before reading the mathematical packet, I read the manifest, receipt, dispatch receipt, metadata supply, and all ten status/permission controls, including their endings. I then supplied the pre-body acknowledgment.

I read the entire literal packet in ordered raw slices of at most twenty lines, through packet line 887, including:

- S1 logical lines 1–783;
- S2 lines 1–12;
- S3 lines 1–48;
- S4 lines 1–42.

Only afterward did I develop the written algebra below. The coherent family and second-moment criterion are fresh author constructions in this duty.

### Execution and exposure boundaries

- Scientific programs, numerical experiments, CAS, solvers, builds, tests, and formatters: **NOT RUN**.
- No calculation code or scientific execution output exists for this candidate.
- One read-only `git diff` restricted to the assigned manifest, receipt, and packet returned no output. That is not a source-hash verification or mathematical check.
- No additional scientific source, sibling return, held payload, or held consumer was opened.
- All quarantine controls were used only for status and exclusions.
- F463 remains an **unreviewed candidate**; its three-qubit theorem is not a premise of the argument below.
- No independent-model, human, formal/kernel, novelty, or clean-cognition assurance is asserted.

The matrices, determinants, and inequalities below are written exact algebra, not executed verification.

## 2. Definitions and claimed state class

For a four-qubit density operator \(\rho\), define the unnormalized lifted marginal sums
\[
H_m(\rho)=
\sum_{\substack{S\subseteq\{1,2,3,4\}\\|S|=m}}
\rho_S\otimes I_{S^c},
\qquad m=1,2,3.
\]
Each marginal occupies its actual physical tensor factors. In particular,
\[
H_3(\rho)=\sum_{i=1}^4\rho_{\bar i}\otimes I_i.
\]

For Hermitian \(X\), let \(K_k(X)\) denote its top-\(k\) eigenvalue sum.

The product-input marginal-sum reference spectra are
\[
\begin{aligned}
L_3&=(4,1,1,1,1,0^{\times11}),\\
L_2&=(6,3^{\times4},1^{\times6},0^{\times5}),\\
L_1&=(4,3^{\times4},2^{\times6},1^{\times4},0).
\end{aligned}
\tag{1}
\]
Their traces are respectively \(8,24,32\).

Let
\[
|W_4\rangle=\frac{|1000\rangle+|0100\rangle+|0010\rangle+|0001\rangle}{2},
\]
and introduce the whole parameter family
\[
|\psi_q\rangle=\sqrt q\,|0000\rangle+\sqrt{1-q}\,|W_4\rangle,
\qquad 0\le q\le1.
\tag{2}
\]
Write
\[
r=1-q,\qquad u=\sqrt{qr}.
\tag{3}
\]

Arbitrary relative phases between the vacuum and the four equal-modulus single-excitation coefficients can be removed by physical local diagonal unitaries and an irrelevant global phase. The claim below therefore also covers those complex states.

### Claimed theorem

For every \(q\in[0,1]\),
\[
H_3(|\psi_q\rangle\langle\psi_q|)\prec L_3,
\qquad
H_2(|\psi_q\rangle\langle\psi_q|)\prec L_2.
\tag{4}
\]

Consequently, for every physical
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I_2,
\qquad 0\le p\le\frac43,
\]
putting
\[
t=|1-p|,\qquad a=\frac{1+t}{2},\qquad b=\frac{1-t}{2},
\]
one has
\[
\Phi_p^{\otimes4}(|\psi_q\rangle\langle\psi_q|)
\prec \operatorname{diag}(a,b)^{\otimes4}.
\tag{5}
\]

The same conclusion holds for arbitrary complex physical local-unitary images and finite convex mixtures, with \(q\) and the local unitaries allowed to vary between components.

## 3. Actual compatible marginals and an explicit block decomposition

Every marginal below comes from the single normalized pure state (2).

For an erased qubit \(i\), put
\[
|v_i\rangle=
\sqrt q\,|000\rangle+
\frac{\sqrt r}{2}\sum_{j\ne i}|e_j\rangle.
\]
Then
\[
\rho_{\bar i}=|v_i\rangle\langle v_i|
+\frac r4|000\rangle\langle000|.
\tag{6}
\]

For a retained pair \(i,j\), put
\[
|v_{ij}\rangle=
\sqrt q\,|00\rangle+
\frac{\sqrt r}{2}(|10\rangle+|01\rangle).
\]
Then
\[
\rho_{ij}=|v_{ij}\rangle\langle v_{ij}|
+\frac r2|00\rangle\langle00|.
\tag{7}
\]

These identities provide a direct entrywise route to every block used below.

### A concrete orthonormal decomposition

Let \(|D_k\rangle\) be the normalized equal superposition of the computational strings of Hamming weight \(k\).

For a unit vector \(f=(f_1,\ldots,f_4)\) satisfying \(\sum_i f_i=0\), define
\[
\begin{aligned}
|f;1\rangle&=\sum_i f_i|i\rangle,\\
|f;2\rangle&=\frac1{\sqrt2}\sum_{i<j}(f_i+f_j)|ij\rangle,\\
|f;3\rangle&=\sum_{|S|=3}\left(\sum_{i\in S}f_i\right)|S\rangle.
\end{aligned}
\tag{8}
\]
All three vectors have norm one. For example,
\[
\sum_{i<j}|f_i+f_j|^2=2\sum_i|f_i|^2
\]
when \(\sum_i f_i=0\).

Choose an orthonormal basis of the three-dimensional zero-sum space. This gives three mutually orthogonal copies of the vectors in (8).

The remaining two-dimensional weight-two space is orthogonal to \(|D_2\rangle\) and all \(|f;2\rangle\). It is the kernel of the incidence map
\[
z\longmapsto
\left(\sum_{j\ne i}z_{\{i,j\}}\right)_{i=1}^4.
\tag{9}
\]

Thus the full space decomposes into:

- the five-dimensional symmetric space spanned by \(|D_0\rangle,\ldots,|D_4\rangle\);
- three three-dimensional spaces from (8);
- the two-dimensional space (9).

The incidence maps between adjacent weight spaces have coefficients:

- \(2,\sqrt6,\sqrt6,2\) on the symmetric vectors;
- \(\sqrt2,\sqrt2\) between the three vectors in (8).

The within-weight exchange adjacency has eigenvalues:

- \(k(4-k)\) on \(|D_k\rangle\);
- \(-1,0,-1\) on \(|f;1\rangle,|f;2\rangle,|f;3\rangle\);
- \(-2\) on (9).

These facts also follow directly from the definitions. For instance, the weight-two exchange sum sends \(f_i+f_j\) to
\[
\sum_{\ell\ne i,j}\bigl[(f_i+f_\ell)+(f_j+f_\ell)\bigr]=0.
\]

## 4. Exact \(H_3\) majorization for the entire family

Substitution of (6) gives the following computational-basis entries of \(H_3\):

- Weight-zero diagonal: \(4-3r\).
- Weight-one diagonal: \(1\).
- Weight-two diagonal: \(r/2\).
- Within-weight exchange entries: \(r/2\) at weight one and \(r/4\) at weight two.
- Vacuum-to-single entries: \(3u/2\).
- Single-to-containing-pair entries: \(u/2\).
- All remaining entries vanish.

In the decomposition above, the nonzero blocks are therefore
\[
A_3=
\begin{pmatrix}
4-3r&3u&0\\
3u&1+\frac32r&\sqrt{\frac32}\,u\\
0&\sqrt{\frac32}\,u&\frac32r
\end{pmatrix}
\tag{10}
\]
on \(|D_0\rangle,|D_1\rangle,|D_2\rangle\), and three copies of
\[
B_2=
\begin{pmatrix}
1-\frac r2&u/\sqrt2\\
u/\sqrt2&r/2
\end{pmatrix}.
\tag{11}
\]
There are seven further zero eigenvalues.

Both blocks are positive because they are blocks of the actual positive marginal sum. Their traces are
\[
\operatorname{Tr}A_3=5,\qquad \operatorname{Tr}B_2=1.
\tag{12}
\]
In particular, every eigenvalue of \(B_2\) is at most one. Explicitly, they are
\[
\frac{1\pm\sqrt{1-r^2}}2.
\tag{13}
\]

For every four-qubit density, each term of \(H_3\) is at most \(I_{16}\). Hence
\[
0\le H_3\le4I_{16},
\tag{14}
\]
and consequently \(\lambda_{\max}(A_3)\le4\).

Now consider a top-\(k\) eigenvalue selection, \(1\le k\le4\). Let \(j\) selected eigenvalues come from \(A_3\).

- If \(j=0\), the selected sum is at most \(k\).
- If \(j=1\), it is at most \(4+(k-1)=k+3\).
- If \(j\ge2\), positivity and trace \(5\) of \(A_3\) bound it by
  \[
  5+(k-j)\le k+3.
  \]

Therefore
\[
K_k(H_3)\le k+3,\qquad k=1,2,3,4.
\tag{15}
\]
For \(k\ge5\), positivity and total trace \(8\) give \(K_k(H_3)\le8\). These are exactly all prefixes of \(L_3\), proving the first claim in (4).

This argument uses actual four-body compatibility. It does not replace the marginals by freely selected matrices.

## 5. Exact \(H_2\) majorization for the same family

The \(H_3\) result alone would not justify a full channel conclusion. This section supplies the separate two-body layer bound needed here.

From (7), the weight-\(k\) diagonal of \(H_2\) is
\[
q\binom{4-k}{2}+\frac{3r}{4}(4-k).
\tag{16}
\]
The within-weight exchange entry is \(r/4\). The entry between a weight-\(k\) string and a containing weight-\((k+1)\) string is
\[
\frac{3-k}{2}\,u.
\tag{17}
\]

The resulting blocks are
\[
A_4=
\begin{pmatrix}
6-3r&3u&0&0\\
3u&3&\sqrt6\,u&0\\
0&\sqrt6\,u&1+\frac32r&\sqrt{\frac32}\,u\\
0&0&\sqrt{\frac32}\,u&\frac32r
\end{pmatrix},
\tag{18}
\]
three copies of
\[
B_3=
\begin{pmatrix}
3-r&\sqrt2\,u&0\\
\sqrt2\,u&1+\frac r2&u/\sqrt2\\
0&u/\sqrt2&r/2
\end{pmatrix},
\tag{19}
\]
the scalar \(1\) on each of the two dimensions in (9), and one zero on \(|D_4\rangle\).

Their traces are
\[
\operatorname{Tr}A_4=10,\qquad \operatorname{Tr}B_3=4.
\tag{20}
\]
The total trace is \(10+3\cdot4+2=24\), as required.

### 5.1 The three-dimensional block

The leading principal minors of \(3I-B_3\) are
\[
r,\qquad \frac32r^2,\qquad \frac{r^2(16-r)}4.
\tag{21}
\]
For \(r>0\), all are positive. At \(r=0\),
\[
3I-B_3=\operatorname{diag}(0,2,3).
\]
Thus
\[
0\le B_3\le3I.
\]
Together with trace \(4\), this proves
\[
B_3\prec\operatorname{diag}(3,1,0).
\tag{22}
\]

### 5.2 The four-dimensional block

I claim
\[
A_4\prec\operatorname{diag}(6,3,1,0).
\tag{23}
\]

First, \(H_2\le6I\), since it is the sum of six lifted density operators, each at most \(I\). Hence \(\lambda_{\max}(A_4)\le6\).

To control the top-two sum, it suffices to show that at least three eigenvalues of \(A_4\) are at least one. Consider \(A_4-I\). Its successive leading principal determinants are
\[
\begin{aligned}
p_1&=5-3r,\\
p_2&=10-15r+9r^2,\\
p_3&=\frac32r(3r-2)(5-r),\\
p_4&=\frac34r^2(9r^2+9r-14).
\end{aligned}
\tag{24}
\]
The first two are strictly positive on \([0,1]\); indeed
\[
p_2=9\left(r-\frac56\right)^2+\frac{15}{4}.
\tag{25}
\]

Consequently, the upper-left two-dimensional block is positive definite. Let \(C\) be its two-dimensional Schur complement. Then
\[
C_{11}=\frac{p_3}{p_2},\qquad \det C=\frac{p_4}{p_2}.
\tag{26}
\]

If \(p_4\le0\), the real symmetric matrix \(C\) has at most one negative eigenvalue.

If \(p_4>0\), then
\[
r>\frac{\sqrt{65}-3}{6}>\frac23.
\]
Therefore \(p_3>0\), so \(C_{11}>0\) and \(\det C>0\); hence \(C\) is positive definite.

At \(r=0\), the assertion follows directly from
\[
A_4-I=\operatorname{diag}(5,2,0,-1).
\]

Thus \(A_4-I\) has at most one negative eigenvalue throughout the closed interval. At least three eigenvalues of \(A_4\) are at least one. Since \(A_4\ge0\) and has trace \(10\),
\[
K_2(A_4)\le10-1=9.
\tag{27}
\]
The top-three sum is at most \(10\), and the total is \(10\). Along with \(\lambda_{\max}(A_4)\le6\), this proves (23).

### 5.3 Assembling the blocks

Majorization is preserved under direct sums when the corresponding block traces agree. A direct proof uses the eigenvalue-allocation formula
\[
K_k\!\left(\bigoplus_j X_j\right)
=
\max_{\sum_j k_j=k}\sum_j K_{k_j}(X_j).
\tag{28}
\]

Apply (28) to (22), (23), and the unchanged scalar blocks. The resulting reference spectrum is the union of
\[
(6,3,1,0),\qquad
3\text{ copies of }(3,1,0),\qquad
(1,1),\qquad(0).
\]
Its decreasing rearrangement is exactly
\[
(6,3^{\times4},1^{\times6},0^{\times5})=L_2.
\]
This proves the second claim in (4).

## 6. From the layer bounds to every actual channel prefix

### 6.1 The one-body layer

For every four-qubit density,
\[
H_1(\rho)\prec L_1.
\tag{29}
\]

For completeness, diagonalize each one-qubit marginal as
\[
\rho_i=V_i\operatorname{diag}(z_i,1-z_i)V_i^\dagger.
\]
Start from the product-input one-body reference operator
\[
R_1=\sum_i |0\rangle\langle0|_i\otimes I_{\bar i}.
\]
Independently choose a bit \(s_i\) with probabilities \(z_i,1-z_i\), and average conjugations by
\[
U_s=\bigotimes_i V_iX^{s_i}.
\]
This average is exactly \(H_1(\rho)\). The spectrum of \(R_1\) is \(L_1\), proving (29) by convexity of every Ky Fan sum.

### 6.2 The positive branch

For \(0\le t\le1\), write
\[
T_t(X)=tX+b\,\operatorname{Tr}(X)I,\qquad b=\frac{1-t}{2}.
\]
Its actual four-use expansion is
\[
T_t^{\otimes4}(\rho)
=t^4\rho+t^3bH_3(\rho)+t^2b^2H_2(\rho)+tb^3H_1(\rho)+b^4I_{16}.
\tag{30}
\]

For \(\rho=|\psi_q\rangle\langle\psi_q|\) and the **same arbitrary complex rank-\(k\) projector \(Q\)** throughout,
\[
\begin{aligned}
\operatorname{Tr}\!\left[QT_t^{\otimes4}(\rho)\right]
\le{}&
t^4+t^3bK_k(L_3)+t^2b^2K_k(L_2)\\
&+tb^3K_k(L_1)+kb^4.
\end{aligned}
\tag{31}
\]

The right-hand side is exactly, not merely approximately,
\[
K_k\!\left(\operatorname{diag}(a,b)^{\otimes4}\right),
\qquad a=t+b.
\tag{32}
\]

To see this, evaluate (30) on \(|0000\rangle\langle0000|\) and order the basis by Hamming weight \(w\). Its coefficient matrices have entries
\[
\mathbf1_{w=0},\qquad
\binom{4-w}{3},\qquad
\binom{4-w}{2},\qquad
4-w,\qquad1,
\tag{33}
\]
respectively. They share a decreasing order. Their weighted sum has entry
\[
(t+b)^{4-w}b^w=a^{4-w}b^w.
\]
Thus their prefix sums add to the product-reference prefix in (32).

No simultaneous attainment by the actual input is assumed. Co-ordering is required only of the reference coefficient matrices.

### 6.3 The physical negative branch

For one qubit,
\[
\mathcal J(X)=YX^TY=\operatorname{Tr}(X)I-X,
\qquad T_{-t}=\mathcal J\circ T_t.
\]
Consequently, with \(W=Y^{\otimes4}\),
\[
T_{-t}^{\otimes4}(\rho)
=W[T_t^{\otimes4}(\rho)]^TW.
\tag{34}
\]
This is full transpose, not partial transpose. It preserves the output spectrum.

For the consuming projector, the transport is
\[
Q'=WQ^TW,
\tag{35}
\]
which remains an orthogonal projector of the same rank. Therefore the positive-branch bound supplies the negative branch. The physical negative branch uses \(0\le t\le1/3\), already inside the proved interval.

All endpoints are included. No division by \(t,b,q,r\), a marginal eigenvalue, or an eigenvalue gap is used.

### 6.4 Local unitaries and mixtures

Physical local-unitary covariance gives
\[
H_m(V\rho V^\dagger)=VH_m(\rho)V^\dagger
\]
and the corresponding covariance for the actual channel.

For any finite mixture of such states, linearity for a fixed \(Q\), followed by the same reference bound, proves every prefix. Different components may have different \(q\), phases, and local bases.

This completes the claimed all-prefix channel theorem on the stated family and hull.

## 7. Genuine entanglement and strict enlargement of the frozen adopted classes

For \(q<1\), the state (2) is genuinely four-partite entangled.

Across any \(1|3\) cut, its two conditional vectors are
\[
\sqrt q\,|000\rangle+\frac{\sqrt r}{2}\sum_{j\ne i}|e_j\rangle,
\qquad
\frac{\sqrt r}{2}|000\rangle.
\]
They are linearly independent when \(r>0\), so the Schmidt rank is two.

Across every \(2|2\) cut, put
\[
|w\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2}.
\]
Then
\[
|\psi_q\rangle=
\sqrt q\,|00\rangle|00\rangle+
\frac{\sqrt r}{\sqrt2}
\bigl(|w\rangle|00\rangle+|00\rangle|w\rangle\bigr).
\tag{36}
\]
The coefficient matrix in the two local bases \((|00\rangle,|w\rangle)\) has determinant \(-r/2\), so this Schmidt rank is also two.

Thus the pure state is not product across any bipartition.

### Excluding the earlier Class A/B hull

Across every paired cut, its pair reduced support is
\[
\operatorname{span}\{|00\rangle,|w\rangle\}.
\tag{37}
\]
A vector \(x|00\rangle+y|w\rangle\) has product-coordinate determinant \(-y^2/2\), so this support contains exactly one product ray.

By contrast:

- A rank-two pair support of a Class A two-coefficient physical-product-basis state contains two independent product rays.
- A rank-two repetition-encoded Class B pair support contains the two product rays of its repetition basis.

Local physical unitaries preserve product rays, and all three pairings of (2) have property (37). Thus these states are outside the earlier Class A/B pure classes.

### Excluding the adopted equal-\(W_4\) local-unitary orbit

Every one-qubit marginal of (2) is
\[
m_q=
\begin{pmatrix}
1-r/4&u/2\\
u/2&r/4
\end{pmatrix},
\qquad
\det m_q=\frac{3r^2}{16}.
\tag{38}
\]
The equal-\(W_4\) value is \(3/16\). For \(0<q<1\), these marginal spectra differ, so the state is not a local-unitary image of \(W_4\).

Finally, a positive convex mixture equal to a pure density must have every positive-weight component supported on that same ray. Therefore, for \(0<q<1\), these states are outside the convex hull of the frozen adopted Class A/B and equal-\(W_4\) classes.

Accordingly, adjoining the newly proved family would strictly enlarge that frozen all-prefix channel class, **if this author candidate is independently checked and adopted**.

This is a comparison with the specified frozen classes, not a literature novelty claim.

## 8. An unrestricted-input sufficient condition for \(H_3\)

The following result does not assume permutation symmetry, real amplitudes, or membership in the preceding family.

### Second-moment certificate

For every four-qubit density \(\rho\),
\[
\operatorname{Tr}\bigl[H_3(\rho)^2\bigr]\le\frac{160}{13}
\quad\Longrightarrow\quad
H_3(\rho)\prec L_3.
\tag{39}
\]

Indeed, \(H_3\ge0\), \(\operatorname{Tr}H_3=8\), and \(H_3\le4I\). If \(x=K_k(H_3)\), Cauchy–Schwarz on the top and remaining eigenvalues gives
\[
\operatorname{Tr}(H_3^2)
\ge\frac{x^2}{k}+\frac{(8-x)^2}{16-k}.
\tag{40}
\]
At the respective forbidden-prefix boundaries, the second-moment thresholds are
\[
\begin{array}{c|c|c}
k&x&x^2/k+(8-x)^2/(16-k)\\ \hline
2&5&92/7\\
3&6&160/13\\
4&7&37/3.
\end{array}
\tag{41}
\]
The expression in (40) increases with \(x\) above each listed boundary. Since \(160/13\) is no larger than any threshold in (41), condition (39) proves all three nontrivial intermediate prefixes. The first prefix follows from \(H_3\le4I\); prefixes from five onward follow from trace eight.

### Pure-state expression and the correct four-qubit spin flip

For a pure input, write its Pauli expansion as
\[
\rho=\frac{I+C_1+C_2+C_3+C_4}{16},
\]
and let
\[
S_j=\sum_{\operatorname{wt}(P)=j}\bigl(\operatorname{Tr}(\rho P)\bigr)^2.
\]
Define
\[
\Theta=Y^{\otimes4}\mathcal K,\qquad
\eta=\operatorname{Tr}(\rho\widetilde\rho)
=|\langle\psi|\Theta\psi\rangle|^2.
\tag{42}
\]

Here \(\Theta^2=+I\). **There is no general Kramers orthogonality assumption.**

Equality of complementary pure-state marginal purities gives
\[
S_3=12+S_1-2S_2.
\tag{43}
\]
Global purity and the spin-flip overlap then give
\[
S_4=3-2S_1+S_2,\qquad
S_2=S_1+2+4\eta.
\tag{44}
\]

The actual marginal sum is
\[
H_3=\frac{4I+3C_1+2C_2+C_3}{8}.
\]
Pauli orthogonality therefore yields
\[
\begin{aligned}
\operatorname{Tr}(H_3^2)
&=4+\frac94S_1+S_2+\frac14S_3\\
&=\boxed{8+3S_1+2\eta}.
\end{aligned}
\tag{45}
\]

Thus a sufficient condition for an arbitrary complex pure input is
\[
\boxed{3S_1+2\eta\le\frac{56}{13}.}
\tag{46}
\]

For the family (2), \(\eta=0\) follows specifically from its weight-zero/one support and its spin flip’s weight-three/four support. That is a property of this family, not of arbitrary four-qubit pure states.

The second-moment criterion and the exact family proof are separate sufficient arguments. Failure of (39) or (46) establishes neither failure of \(H_3\) majorization nor failure of the actual channel.

## 9. Prior-source qualification

The frozen Song–Chen excerpt identifies Proposition 3 of [*A counterexample to the strong spin alignment conjecture*, arXiv:2603.25410v1](https://arxiv.org/html/2603.25410v1) as a direct prior theorem for weighted compatible three-qubit two-body marginal sums. Its equal-weight specialization is precisely the three-qubit \(H_2\) majorant.

That statement is **prior, not a new result here**. Neither it nor the unreviewed F463 candidate is required by the four-qubit block proof above.

The earlier stronger Amosov claims retain the qualifications stated in the frozen inputs. This candidate neither certifies those proofs nor disproves their statements. No inaccessible-source equivalence, priority, or method-novelty claim is made.

## 10. Exact conclusions and residual obligations

### Author conclusions claimed

- Full \(H_3\) majorization for every coherent vacuum–\(W_4\) state (2).
- Full \(H_2\) majorization for the same entire family.
- All sixteen actual channel prefixes, for every physical depolarizing parameter, every arbitrary complex consuming projector, and every physical local-unitary image and finite mixture.
- A strict enlargement relative to the frozen adopted Class A/B plus equal-\(W_4\) hull.
- An unrestricted-input second-moment sufficient condition for \(H_3\), with the pure-state expression (45).

### Original unrestricted \(H_3\) residual

For an arbitrary complex pure state not covered by these sufficient arguments, the unpaid inequalities are exactly
\[
K_2(H_3)\le5,\qquad
K_3(H_3)\le6,\qquad
K_4(H_3)\le7.
\tag{47}
\]
The first prefix and all prefixes from five onward already have universal elementary bounds.

The first missing step in extending the family proof is a replacement for its permutation-symmetry block constraints for a general compatible four-qubit input. No such replacement is established here.

A proof for all pure inputs would extend to mixed inputs by linearity and Ky Fan convexity. That universal pure-state proof has not been supplied.

### Original unrestricted channel residual

Outside the enlarged state class proved here, this candidate does not establish the full channel theorem. In particular:

- A general \(H_3\) result alone would not supply the separate general \(H_2\) layer bound used by this layerwise route.
- A counterexample to either layer bound would not automatically be a counterexample to the positively weighted actual channel sum.
- No arbitrary four-qubit density/projector violation is constructed.

### Acceptance status

The load-bearing new checks are the compatible-marginal block formulas, the principal-determinant identities (21) and (24), their inertia consequences, and the co-ordered channel assembly. They require disjoint reconstruction and a parent disposition before adoption.

**Completed return:** a self-contained written author candidate for a strictly larger genuine-four-qubit all-prefix channel class, together with an unrestricted \(H_3\) sufficient condition and the literal remaining universal inequalities. Scientific execution is **NOT RUN**. The original unrestricted target remains **NOT PROVED**.

---

overall_correctness: correct

explanation: The assigned frozen-path git diff was empty, so no patch-introduced defect can be anchored and reported. This code-review field does not independently accept the mathematical author candidate above or close its unrestricted target.

confidence: 0.99