# f373 — Written review of the paired-repetition Class B theorem

**overall_correctness:** correct  
**confidence:** 0.98  
**explanation:** The assigned Class B theorem is supported by an independent written reconstruction: the encoded physical map is exact, the necessary logical two-qubit comparison follows from a directly derived two-level calculation, and the four output blocks admit a finite global unitary-orbit ensemble. The second exact example, its maximizing complex projector, and its separation from the convex hull of Class A also check.

**Findings:** none — **0 FATAL / 0 MAJOR / 0 MINOR** within this assigned mathematical slice.

This is a **same-harness written review**, not a parent adoption, independent-model-family review, human review, formal/kernel proof, novelty determination, or whole-target acceptance. The upstream candidate’s recorded **AUTHOR / UNREVIEWED** status is not silently changed by this return.

The full source packet was read, including its ending. The disposition below covers **Class B, its permitted physical transformations and finite convex mixtures, its all-\(2|2\)-separable inclusion, the required logical \(m=2\) comparison, and the second exact example**. It does not independently dispose the entire Class A argument at all other active-qubit counts or the first example’s separate layer-trace calculations.

## 1. Reviewed statement and source bindings

The principal source is:

- **S1:** `review-waves/f363-depolarizing-common-projector-slack-frontier/review-v1.md`
- SHA-256: `a9b558665da012bfff67d56f520cc4d8fe44864e8bec4e8b43dc532344e8d915`
- 24,211 bytes; 690 LF characters; 691 logical lines, including its unterminated final line.

Important locations are:

| Claim | S1 logical LF |
|---|---:|
| Class B definition and unrestricted logical density | 30–39 |
| Unitary-orbit and all-projector assertions | 43–59 |
| Common-projector and block-assembly facts | 123–137 |
| Two-level calculation supplying the needed \(m=2\) step | 143–246 |
| Exact encoded pair map | 274–321 |
| Logical comparisons | 323–353 |
| EE/EO/OE/OO blocks and assembly | 355–391 |
| All-\(2|2\)-separable inclusion | 393 |
| Physical parameter range and reflection | 395–431 |
| Second four-coefficient example | 563–622 |
| Explicit exclusions | 635–645 |

For clarity, let \(\mathcal B_{\mathrm{hull}}\) denote the finite convex hull of all Class B states after the allowed component-dependent physical local basis changes and physical-qubit pairings. The theorem established by this review is:

For
\[
\Phi_p(X)=(1-p)X+\frac p2\operatorname{Tr}(X)I,\qquad
\Lambda_p=\Phi_p^{\otimes4},
\]
every physical \(p\in[0,4/3]\), and every
\(\rho\in\mathcal B_{\mathrm{hull}}\), set
\[
t=|1-p|,\quad a=\frac{1+t}{2},\quad b=\frac{1-t}{2},\quad
D_t=\operatorname{diag}(a,b)^{\otimes4}.
\]
There exists a finite ensemble of sixteen-dimensional unitaries such that
\[
\Lambda_p(\rho)=\sum_j w_jU_jD_tU_j^\dagger,\qquad
w_j\ge0,\qquad \sum_jw_j=1.
\]
Consequently, for every complex orthogonal rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}(Q\Lambda_p(\rho))\le K_k(D_t),
\qquad k=1,\ldots,16.
\]

The ensemble may depend on \(\rho,p\), but it is independent of \(Q\). This does **not** assert a single input-independent random-unitary postprocessing channel.

## 2. Exact one-pair physical map — SUPPORTED

First work on the positive Bloch branch:
\[
\mathcal D_t=\Phi_{1-t},\qquad 0\le t\le1.
\]
Its elementary action is
\[
\mathcal D_t(|0\rangle\langle0|)=\operatorname{diag}(a,b),\qquad
\mathcal D_t(|1\rangle\langle1|)=\operatorname{diag}(b,a),
\]
and
\[
\mathcal D_t(|0\rangle\langle1|)=t|0\rangle\langle1|.
\]

Use the encoding
\[
V|0\rangle=|00\rangle,\qquad V|1\rangle=|11\rangle,
\]
and physical subspaces
\[
E=\operatorname{span}\{|00\rangle,|11\rangle\},\qquad
O=\operatorname{span}\{|01\rangle,|10\rangle\}.
\]

For an arbitrary logical matrix \(X=(X_{ij})\), direct application to its four matrix units gives
\[
\mathcal D_t^{\otimes2}(VXV^\dagger)
=
\begin{pmatrix}
a^2X_{00}+b^2X_{11}&t^2X_{01}\\
t^2X_{10}&b^2X_{00}+a^2X_{11}
\end{pmatrix}_{E}
\oplus
ab\,\operatorname{Tr}(X)I_{O}.
\]
There are no \(E\)-to-\(O\) entries, and there are no off-diagonal entries within \(O\).

Define
\[
h=a^2+b^2=\frac{1+t^2}{2},\qquad
\ell=ab=\frac{1-t^2}{4},\qquad
\gamma=\frac th=\frac{2t}{1+t^2}.
\]
Then
\[
h>0,\qquad h+2\ell=1,\qquad 0\le\gamma\le1,
\]
the last inequality following from \(2t\le1+t^2\).

Let
\[
\mathcal Z_t(X)=\frac{1+t}{2}X+\frac{1-t}{2}ZXZ,
\qquad F=\mathcal Z_t\circ\mathcal D_\gamma.
\]
The diagonal coefficients satisfy
\[
\frac{h(1+\gamma)}2=a^2,\qquad
\frac{h(1-\gamma)}2=b^2,
\]
and the off-diagonal multiplier is
\[
ht\gamma=t^2.
\]
Therefore the exact map is
\[
\boxed{
\mathcal D_t^{\otimes2}(VXV^\dagger)
=
hF(X)\big|_E\ \oplus\
\ell\operatorname{Tr}(X)I_2\big|_O.
}
\]

This is a linear, entrywise identity, not a spectral estimate or an erasure surrogate. It verifies S1 LF274–321, including the dephasing parameter, all factors of \(h,\ell,\gamma\), and the odd-block multiplicity.

## 3. Independent derivation of the needed logical \(m=2\) comparison — SUPPORTED

This reconstruction does **not** import a pending sibling review.

Use a general depolarizing parameter \(r\in[0,1]\), and write
\[
c=\frac{1+r}{2},\qquad e=\frac{1-r}{2},\qquad
d_r=\operatorname{diag}(c,e).
\]

For a Schmidt-form pure state
\[
|s\rangle=\sqrt u\,|00\rangle+
e^{i\theta}\sqrt{1-u}\,|11\rangle,
\qquad 0\le u\le1,
\]
the output under \(\mathcal D_r^{\otimes2}\), in the decomposition
\(\{00,11\}\oplus\{01,10\}\), is
\[
H_E\oplus ce I_2,
\]
where
\[
H_E=
\begin{pmatrix}
uc^2+(1-u)e^2&
r^2\sqrt{u(1-u)}e^{-i\theta}\\
r^2\sqrt{u(1-u)}e^{i\theta}&
(1-u)c^2+ue^2
\end{pmatrix}.
\]
The corresponding reference blocks of \(d_r\otimes d_r\) are
\[
\operatorname{diag}(c^2,e^2)\oplus ceI_2.
\]

Put \(z=2u-1\). Since \(c+e=1\) and \(c-e=r\),
\[
c^2-e^2=r.
\]
The eigenvalues of \(H_E\) are
\[
\frac{c^2+e^2}{2}\pm G,
\]
with
\[
(2G)^2=z^2r^2+(1-z^2)r^4
\le r^2=(c^2-e^2)^2.
\]
Thus, when \(r>0\),
\[
q=\frac12+\frac Gr\in[1/2,1].
\]
Choose a unitary \(T\) whose first column is a larger-eigenvalue eigenvector of \(H_E\). Then
\[
H_E=
T\left[
q\operatorname{diag}(c^2,e^2)
+(1-q)X\operatorname{diag}(c^2,e^2)X
\right]T^\dagger.
\]
Extending \(T\) and \(TX\) by the identity on the odd subspace gives a **two-term unitary-orbit ensemble for the complete logical two-qubit output**.

At \(r=0\), both output and reference are \(I_4/4\), so no division is needed. At \(r=1\), the same construction remains valid with zero reference eigenvalues.

Now let the logical input be an arbitrary complex pure state. Its Schmidt decomposition supplies local logical unitaries reducing it to the displayed form. Covariance of \(\mathcal D_r\), directly from its definition, transports the two-term ensemble back to that state. This does not restrict the original state or its output eigenvectors to real amplitudes.

Finally, a mixed logical density has a finite spectral decomposition. Averaging these pure-state ensembles proves
\[
\boxed{
\mathcal D_r^{\otimes2}(\omega)
\in\operatorname{conv}\{U(d_r\otimes d_r)U^\dagger\}
}
\]
for every complex logical two-qubit density \(\omega\).

This supplies the load-bearing comparison used at S1 LF337–353 without assuming a four-qubit global theorem.

### Applying the comparison to \(F\)

For the physical pair map, take \(r=\gamma\), so
\[
d=d_\gamma
=\operatorname{diag}\left(\frac{1+\gamma}{2},
                         \frac{1-\gamma}{2}\right)
=\operatorname{diag}(a^2/h,b^2/h).
\]

For every one-qubit density \(\eta\), spectral decomposition and covariance give
\[
\mathcal D_\gamma(\eta)
\in\operatorname{conv}\{UdU^\dagger\}.
\]
Applying \(\mathcal Z_t\), already an explicit two-term unitary mixture, gives
\[
\boxed{F(\eta)\in\operatorname{conv}\{UdU^\dagger\}.}
\]

Likewise, applying the four-term random-unitary map
\(\mathcal Z_t^{\otimes2}\) to the preceding two-qubit comparison gives
\[
\boxed{
(F\otimes F)(\omega)
\in\operatorname{conv}\{U(d\otimes d)U^\dagger\}.
}
\]

Importantly, this argument uses covariance of **\(\mathcal D_\gamma\)** before applying dephasing. It does not assume the generally false statement that \(F\) is covariant under arbitrary logical basis changes.

All mixtures are finite. One possible bound is at most 32 ensemble terms for the two-qubit comparison after spectral mixing and dephasing, and at most four for each one-qubit comparison. No such bound is needed for the inequality, but finiteness is explicit.

## 4. Four actual blocks, reference blocks and global assembly — SUPPORTED

Encode an arbitrary complex logical density:
\[
\rho=(V\otimes V)\omega(V\otimes V)^\dagger.
\]
Let \(\omega_A,\omega_B\) be its logical marginals. Tensoring the exact one-pair map gives:

| Physical block | Actual output | Product-reference block | Trace of either block |
|---|---|---|---:|
| \(EE\) | \(h^2(F\otimes F)(\omega)\) | \(h^2d\otimes d\) | \(h^2\) |
| \(EO\) | \(h\ell F(\omega_A)\otimes I_2\) | \(h\ell d\otimes I_2\) | \(2h\ell\) |
| \(OE\) | \(h\ell I_2\otimes F(\omega_B)\) | \(h\ell I_2\otimes d\) | \(2h\ell\) |
| \(OO\) | \(\ell^2 I_4\) | \(\ell^2 I_4\) | \(4\ell^2\) |

The mixed blocks follow from applying the trace map to the other logical factor; they do not assume \(\omega\) is a product state. Their total trace is
\[
h^2+4h\ell+4\ell^2=(h+2\ell)^2=1.
\]

The reference table follows directly from the one-pair reference
\[
\operatorname{diag}(a,b)^{\otimes2}
=
h d\big|_E\oplus \ell I_2\big|_O.
\]
Thus both the actual and reference tables in S1 LF355–386 have the correct block placement, marginals, coefficients and traces.

### Explicit finite global assembly

Write finite block comparisons as
\[
A_{EE}=\sum_\mu r_\mu U_\mu D_{EE}U_\mu^\dagger,
\]
\[
F(\omega_A)=\sum_\nu s_\nu V_\nu dV_\nu^\dagger,\qquad
F(\omega_B)=\sum_\xi v_\xi W_\xi dW_\xi^\dagger,
\]
where each probability list sums to one.

On the physical direct sum \(EE\oplus EO\oplus OE\oplus OO\), define
\[
\mathcal U_{\mu\nu\xi}
=
U_\mu\oplus(V_\nu\otimes I_2)
\oplus(I_2\otimes W_\xi)\oplus I_4,
\]
with probability \(r_\mu s_\nu v_\xi\). These are whole-space unitaries, and
\[
\Lambda_{1-t}(\rho)
=
\sum_{\mu,\nu,\xi}
r_\mu s_\nu v_\xi\,
\mathcal U_{\mu\nu\xi}D_t\mathcal U_{\mu\nu\xi}^\dagger.
\]

This establishes the required global ensemble. The independent choice of block unitaries is a construction of the ensemble; it is not an independence assumption about the input’s logical correlations.

**Unequal traces cause no problem:** the comparison uses the unnormalized block matrices themselves, with matching trace within each block.

**Zero blocks cause no problem:** at \(\ell=0\), the \(EO,OE,OO\) blocks are zero on both sides and their unitaries can be chosen arbitrarily. No division by \(\ell\) or by a block trace occurs.

At \(t=0\),
\[
h=\tfrac12,\quad \ell=\tfrac14,\quad \gamma=0,
\]
and every physical four-dimensional block is \(I_4/16\). At \(t=1\),
\[
h=1,\quad\ell=0,\quad\gamma=1,
\]
so only \(EE\) remains, with its already established finite ensemble. Rank drops and spectral degeneracies therefore do not leave a missing case.

## 5. Physical bases, pairings, mixtures and separability — SUPPORTED

### Physical local bases and pair permutations

The channel definition gives physical local-unitary covariance:
\[
\Lambda_p(L\rho L^\dagger)=L\Lambda_p(\rho)L^\dagger,
\qquad L=L_1\otimes L_2\otimes L_3\otimes L_4.
\]
Because all four tensor factors are the same channel, it also commutes with physical-qubit permutations.

Consequently, a Class B state in any permitted physical product basis and any physical pairing has a unitary-orbit ensemble relative to the same \(D_t\): conjugating the output merely left-multiplies the ensemble unitaries.

For a finite convex decomposition at fixed \(p\), multiply each component’s ensemble weights by its decomposition weight and take the union. This covers mixed decompositions whose physical bases and pair partitions differ between components. There is no requirement of one common physical basis across the mixture.

### Inclusion of every \(2|2\)-separable state

For a fixed balanced physical partition, a separable state has a finite convex decomposition into products of two-qubit densities. Spectrally decompose those densities to obtain products
\[
|\alpha\rangle\langle\alpha|\otimes
|\beta\rangle\langle\beta|
\]
of two-qubit pure states.

Schmidt-decompose each physical pair separately:
\[
|\alpha\rangle=
\sqrt{x}\,|e_0f_0\rangle+
\sqrt{1-x}\,|e_1f_1\rangle,
\]
with an analogous expression for \(|\beta\rangle\). Each component is therefore supported on the tensor product of two locally transformed repetition subspaces. It is a permitted Class B component.

If separability is defined using a closed convex hull, finite-dimensional Carathéodory supplies an equivalent finite decomposition; no infinite-ensemble limit is needed here.

This proves:

- inclusion of every state separable across each fixed \(2|2\) partition;
- inclusion of finite mixtures whose balanced partitions differ between components;
- inclusion of arbitrary mixed and logically entangled densities on a fixed paired-repetition support.

It does **not** establish coverage of all \(1|3\)-separable states, all biseparable states, or all four-qubit densities. No such enlargement is adopted.

## 6. Full physical range and arbitrary complex projectors — SUPPORTED

For \(q=1-p\), the one-qubit channel has Pauli-mixture weights
\[
\frac{1+3q}{4}\quad\text{for }I,\qquad
\frac{1-q}{4}\quad\text{for each of }X,Y,Z.
\]
They are nonnegative exactly when
\[
-\frac13\le q\le1,
\]
equivalently \(0\le p\le4/3\).

The preceding construction covers \(p=1-t\), \(0\le t\le1\).

For the negative branch, let
\[
W=Y^{\otimes4},\qquad S(A)=WA^TW.
\]
Full transpose followed by spin flip changes Pauli weight \(w\) by \((-1)^w\), hence
\[
\Lambda_{1+t}(\rho)=S(\Lambda_{1-t}(\rho)).
\]
For the physical negative branch, \(0\le t\le1/3\).

Because \(D_t\) is real diagonal,
\[
S(UD_tU^\dagger)
=(W\overline U)D_t(W\overline U)^\dagger.
\]
Thus the finite ensemble itself transports to the negative branch.

For an arbitrary complex Hermitian orthogonal projector \(Q\), define
\[
Q'=WQ^TW.
\]
Since \(W^T=W\), this is again a rank-\(k\) Hermitian orthogonal projector and
\[
\operatorname{Tr}(QS(A))=\operatorname{Tr}(Q'A).
\]
This is **full transposition**, not partial transposition. Neither the density nor the consuming projector is assumed real.

On the negative branch, the literal product-input output has its one-qubit diagonal entries reversed relative to \(D_t\); it is a fixed unitary conjugate of \(D_t\), so the reference spectrum and unitary orbit are unchanged.

### Same-\(Q\), all-index conclusion

For any established ensemble and one fixed rank-\(k\) projector \(Q\),
\[
\operatorname{Tr}(Q\Lambda_p(\rho))
=
\sum_jw_j\operatorname{Tr}(U_j^\dagger Q U_jD_t)
\le K_k(D_t).
\]
In a diagonal basis of \(D_t\), the diagonal entries of each conjugated projector lie in \([0,1]\) and sum to \(k\). Their weighted sum is at most the sum of the \(k\) largest diagonal eigenvalues.

This proves all Ky Fan inequalities and full output majorization on the reviewed Class B hull. It does not assume coincident maximizing projectors for separate Pauli layers or separate blocks.

### Actual joint-layer consequence on this class

With the source’s definitions
\[
\rho=\frac1{16}(I+C_1+C_2+C_3+C_4),\qquad
\widetilde\rho=W\rho^TW,
\]
\[
\alpha=\frac{t^3(1+t)}2,\qquad
\beta=\frac{t^3(1-t)}2,\qquad
B=\alpha\rho-\beta\widetilde\rho,
\]
one has \(\alpha-\beta=t^4\) and \(\alpha+\beta=t^3\). Comparing Pauli coefficients gives
\[
\Lambda_{1-t}(\rho)=
B+\frac{1-t^4}{16}I+
\frac{t-t^3}{16}C_1+
\frac{t^2-t^4}{16}C_2.
\]

Also
\[
16R_3=16(a^4+2a^3b)=3+8t+6t^2-t^4.
\]
For every fixed complex rank-three \(Q\), the reviewed majorization bound therefore implies
\[
16\operatorname{Tr}(QB)
+(t-t^3)\operatorname{Tr}(QC_1)
+(t^2-t^4)\operatorname{Tr}(QC_2)
\le8t+6t^2+2t^4.
\]
This is the source’s actual same-\(Q\) inequality on the reviewed class. On the negative branch it is applied using \(Q'\) above. No unrestricted joint-slack premise or held one-erasure/L1 result enters.

## 7. Second exact four-coefficient example — SUPPORTED

The source-provided example is
\[
|\phi\rangle=\frac{3|00\rangle+i|11\rangle}{\sqrt{10}},
\qquad
|\psi\rangle=|\phi\rangle_{12}\otimes|\phi\rangle_{34},
\qquad p=\frac12.
\]
It is an author-provided claim being audited, not a newly selected reviewer probe.

Its four physical coefficients are
\[
|\psi\rangle=
\frac9{10}|0000\rangle+
\frac{3i}{10}|0011\rangle+
\frac{3i}{10}|1100\rangle-
\frac1{10}|1111\rangle,
\]
whose squared magnitudes sum to one. It is a Class B pure state.

### Exact pair output

Here
\[
t=\frac12,\quad a=\frac34,\quad b=\frac14,\quad
h=\frac58,\quad\ell=\frac3{16},\quad\gamma=\frac45.
\]
Applying the exact one-pair map gives
\[
\sigma_E=
\begin{pmatrix}
41/80&-3i/40\\
3i/40&9/80
\end{pmatrix},
\qquad
\sigma_O=\frac3{16}I_2.
\]
The complete pair output is \(\sigma=\sigma_E\oplus\sigma_O\), with unit trace.

Put \(w=\sqrt{73}\). The even block is
\[
\sigma_E=\frac{25I+16Z+6Y}{80},
\]
so its eigenvalues are
\[
L_\pm=\frac{25\pm2w}{80}.
\]
The pair spectrum is therefore
\[
L_+,\quad \ell,\quad\ell,\quad L_-,
\qquad \ell=\frac3{16}.
\]
Since \(8<w<9\),
\[
L_+>\ell>L_->0.
\]

### Complete four-qubit spectrum and its leading terms

The actual four-qubit output is exactly \(\sigma\otimes\sigma\). Its spectrum, including multiplicities and in decreasing order, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
L_+^2&1\\
L_+\ell&4\\
L_+L_-&2\\
\ell^2&4\\
\ell L_-&4\\
L_-^2&1
\end{array}
\]
For the only additional ordering comparison not immediate from
\(L_+>\ell>L_->0\),
\[
L_+L_-=\frac{333}{6400}>
\frac{225}{6400}=\ell^2.
\]
The multiplicities sum to sixteen, and the eigenvalue sum is
\((L_++2\ell+L_-)^2=1\).

Consequently,
\[
K_3=L_+^2+2L_+\ell
=\frac{1667+160\sqrt{73}}{6400}.
\]
The product reference has
\[
R_3=\frac{135}{256}=\frac{3375}{6400},
\]
hence
\[
\boxed{
R_3-K_3=\frac{427-40\sqrt{73}}{1600}>0.
}
\]
Indeed \(\sqrt{73}<9\) makes the numerator larger than \(67\). These agree with S1 LF599–605.

### Maximizing complex projector

Define
\[
|\zeta\rangle=
\sqrt{\frac{w+8}{2w}}\,|00\rangle+
i\sqrt{\frac{w-8}{2w}}\,|11\rangle.
\]
It is normalized and has logical Bloch coordinates
\[
\langle Z\rangle=\frac8w,\qquad
\langle Y\rangle=\frac3w.
\]
Thus it is the positive eigenvector of \(8Z+3Y\), and
\[
\sigma|\zeta\rangle=L_+|\zeta\rangle.
\]

The three vectors
\[
|\zeta\rangle\otimes|\zeta\rangle,\qquad
|\zeta\rangle\otimes|01\rangle,\qquad
|01\rangle\otimes|\zeta\rangle
\]
are orthonormal eigenvectors of the complete actual output, with eigenvalues
\[
L_+^2,\qquad L_+\ell,\qquad L_+\ell.
\]
Their orthogonal span therefore gives an actual maximizing complex rank-three projector, exactly as claimed at S1 LF607–620. The degeneracy of \(L_+\ell\) does not invalidate choosing these two of its four eigenvectors.

### Strict enlargement beyond the Class A hull

Across the physical cut \(13|24\), the coefficient matrix is diagonal, up to phases, with nonzero singular values
\[
\frac9{10},\quad\frac3{10},\quad
\frac3{10},\quad\frac1{10}.
\]
Thus the Schmidt rank is four.

Every pure state with at most two coefficients in a physical product basis has Schmidt rank at most two across every physical cut: each of its two terms is a product across that cut. Local basis changes cannot increase the rank of that two-term representation.

Therefore this example is not Class A in any permitted physical product basis. Since it is pure, it also cannot be a convex mixture of distinct Class A pure states: positivity forces every nonzero component of a decomposition of a rank-one density to have the same one-dimensional support.

Accordingly, **adding Class B strictly enlarges the Class A convex hull**. This does not assert the different statement that Class B by itself contains every Class A state.

Each one-qubit marginal of this example has Bloch radius \(4/5\), so
\[
s=\sum_i r_i^2=\frac{64}{25}>\frac14.
\]
It is outside the supplied low-polarization pure sector and, by purity, outside that sector’s pure-state convex hull. Also \(p=1/2\) is outside the supplied all-density window around complete depolarization. These comparisons do not claim nonmembership in every other earlier regional class.

## 8. Per-claim disposition and exact import boundary

| Claim | Disposition | Source and boundary |
|---|---|---|
| Exact encoded pair map, including \(h,\ell,\gamma\) and dephasing | **SUPPORTED** | S1 LF274–321; reconstructed entrywise |
| Required pure logical \(m=2\) comparison | **SUPPORTED** | S1 LF143–246, 337–353; independently derived above, no sibling import |
| Arbitrary complex logical density and logical marginals | **SUPPORTED** | S1 LF323–353; finite spectral mixing plus explicit random-unitary dephasing |
| EE/EO/OE/OO actual/reference blocks and trace factors | **SUPPORTED** | S1 LF355–386; reconstructed from the exact map |
| Finite global ensemble with unequal traces and zero blocks | **SUPPORTED** | S1 LF137, 389; explicit product-probability/direct-sum construction |
| Physical local bases, physical pairings and mixed decompositions | **SUPPORTED** | S1 LF30–39, 391; covariance and finite averaging |
| Every \(2|2\)-separable state | **SUPPORTED** | S1 LF393; componentwise spectral and physical-pair Schmidt decompositions |
| Physical \(p\)-range, reflection and arbitrary complex \(Q\) | **SUPPORTED** | S1 LF395–431; Pauli probabilities and full-transpose transport |
| All-index majorization and actual same-\(Q\) consequence on the reviewed Class B hull | **SUPPORTED** | S1 LF43–59, 85–117, 123–137; ensemble certificate |
| Second example’s output, full spectrum, maximizing \(Q\), gap and strict Class A-hull separation | **SUPPORTED** | S1 LF563–622; exact reconstruction above |
| Full Class A proof at all other \(m\), and first example’s separate layer traces | **INCONCLUSIVE in this disposition / outside assigned slice** | Complete source context was read; no blanket clearance is inferred |
| Unrestricted all-\(\rho\), all-biseparable or original whole-target theorem | **INCONCLUSIVE / not established** | Explicitly excluded by S1 LF635–645; neither proved nor refuted here |
| Independent confirmation of the author’s historical execution/read chronology | **INCONCLUSIVE** | S1 LF647–691 is author reporting, not independently observed execution evidence |

No reviewed mathematical claim was refuted.

### Mathematical imports actually used

1. Finite-dimensional Hermitian spectral decomposition.
2. Schmidt decomposition for complex bipartite pure states.
3. Finite-dimensional Carathéodory only if separability is defined via a closed convex hull.
4. Elementary tensor algebra, matrix-unit channel action, Pauli algebra and full-transpose trace identities.

The logical two-qubit comparison, block-assembly construction and projector trace bound were derived here rather than imported as unproved scientific premises.

The other supplied sources were read at their stated comparison scopes:

- **S2**, SHA `b8587c7aef665460e042c3f87295e0fc9062c201ab2d43150d89faa1259073c1`: low-polarization pure-state sector and its specified convex hull; not unrestricted majorization.
- **S3**, SHA `774cbb0f053c2b5c6400320a6c3bfdb919ec1e3df09ddf5884508e54cccb3f6c`: prior regional and small-\(t\) results, only after applying the mandatory Class H scope erratum. Class H requires its moment hypothesis as well as its spin-flip condition; \(p=1\) is complete depolarization, not identity.
- **S4**, SHA `cdda493b043002b208d8f92b7da352d2f165f6e03c07481a439b596be7b8b38d`: selected global prefixes \(k\in\{5,6,10,11\}\), not full majorization.

Their historical executions, reviewer outcomes and linked artifacts were not replayed or used as a substitute for the present derivation. No linked old-held payload, sibling outcome, author code, or original-book authenticity claim is a premise.

## 9. Unpaid gates and final scientific boundary

The supported result is a constructive theorem for the actual physical channel on the reviewed Class B hull. It includes all logical densities on paired-repetition support and every \(2|2\)-separable state, with component-dependent physical bases and pairings allowed.

It does **not** establish:

- unrestricted four-qubit \(k_3\);
- unrestricted all-index majorization;
- coverage of all biseparable states;
- arbitrary mixed-state membership from small local Bloch radii;
- a universal four-qubit one-erasure/L1 or joint-slack premise;
- novelty, priority, original-book/source authenticity;
- independent-family, human or formal/kernel assurance.

No scientific executable, CAS, selected new mathematical instance, solver, enumeration, finite diagnostic, or scientific replay was used in this WRITTEN duty. The displayed exact source examples were audited as permitted author claims, not reclassified as author-method violations.

**Final assigned-slice disposition: SUPPORTED, with no mathematical findings. Parent adoption remains separate.**

---

## Materialization target: `f373-depolarizing-paired-repetition-full-majorization-proof-review/reviewer-process-v1.md`

# f373 — Reviewer process and metadata record

## Assignment and actual role

- **Role:** WRITTEN proof review.
- **Actual runtime model:** `anthropic/claude-fable-5-1`, as supplied by the session.
- **Assurance:** same-harness only.
- **Round cutoff:** `2026-10-31T21:23:27Z`, unchanged.
- **Write status:** no working-tree file was written. The complete review and this process body are returned directly for parent materialization. No alternate-filesystem working-tree bypass was used.

## Frozen assignment bindings

Wave root:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f373-depolarizing-paired-repetition-full-majorization-proof-review/`

| Artifact | SHA-256 | Bytes / LF |
|---|---|---:|
| `manifest-v1.json` | `5ed7bf333d309f17abc7415160f89bd67dd13d955c0cdbd27000b3cdf053c366` | 6998 / 121 |
| `freeze-receipt-v1.json` | `eb60f76183ad8df404f4bfda619cefc18dc3ed81f713cf2750eac50a45702a6d` | 2965 / 73 |
| `literal-packet-v1.md` | `5cf65a768c3a55f055393caefdb77f6d3bb17082f9cc9dc991e2ceae3bb8a888` | 48862 / 790 |

These live hash/byte/LF checks were **supplied by the parent**, not executed by this reviewer. The complete parent record was read from `parent-live-metadata-supply-v1.json`; its parent-native observation is `2026-10-30T09:54:48-0700 PDT`. It reports matching pins for all assigned artifacts, controls and inputs.

## Controls and pre-body acknowledgement

Before mathematical packet reads, I read the complete manifest, freeze receipt and all eight named controls:

1. `contract-addendum-2-frontier-first-owner-direction-v1.json`
2. `parent-L1-selected-diagnostic-release-quarantine-v1.json`
3. `parent-written-duty-execution-and-reporting-deviations-20261030-v1.json`
4. `prospective-author-method-scope-restoration-20261030-v1.json`
5. `dispositions/physics-2-depolarizing-k3-class-H-scope-erratum-v1.json`
6. `parent-ame-held-compression-claim-consumer-quarantine-v1.json`
7. `parent-core-gram-auxiliary-operator-diagnostic-quarantine-v1.json`
8. `parent-privacy-auxiliary-parameter-diagnostic-quarantine-v1.json`

The Class H erratum was read before the affected S3 disposition.

The following direct administrative ACK was delivered to `Main` before opening the mathematical packet:

> f373 WRITTEN pre-body ACK: I have read the complete manifest and freeze receipt plus all eight controls, including the mandatory ClassH scope erratum, before opening the mathematical packet. I will read the entire ordered literal packet raw in <=20-LF windows through its ending before deriving; reconstruct ClassB and logical m2 independently; use no sibling/old-held payload, selected probe, scientific executable, or external-model CLI. Source-provided author examples will be audited as claims, not classified as unauthorized author activity. This role is read-only: I will return full materializable review/process bodies if wave writes are unavailable. Native start/completion have not been invented.

The controls were status/permission inputs only. No excluded mathematical payload was followed.

## Complete packet coverage and chronology

The entire packet was read using raw windows no longer than twenty LF:

- `1–20`, `21–40`, and so on through `761–780`;
- the final request `781–800` returned the actual ending at packet LF790.

The windows were requested in consecutive ascending groups, with independent calls within groups issued concurrently. This records complete coverage, not a claim of serialized native completion order for concurrent calls.

Coverage included, in packet order:

- S1 logical LF1–691, including its final status line;
- S2 LF1–38;
- S3 LF1–22;
- S4 LF1–37, including the packet ending.

All packet reads completed before mathematical derivation. No elided mathematical fragment remains unrecovered.

No out-of-manifest reviewer body or sibling outcome was opened. Historical review descriptions already present in the required S2–S4 text were read as part of the packet, not adopted as scientific verification of the present candidate.

## Actual clock observations and substantive checkpoint

The reviewer executed only metadata clock commands, using `/bin/date -u`:

| Observation | Reviewer-native output | Meaning |
|---|---|---|
| Initial packet-read batch | `2026-10-30T16:54:47Z` | Clock observation in that concurrent batch; not an asserted task start |
| Substantive checkpoint | `2026-10-30T16:58:23Z` | Clock observed after the complete read and principal reconstruction |
| Final pre-delivery observation | `2026-10-30T17:00:37Z` | Observation before composing the delivered result; not an exact completion timestamp |

The parent’s `09:54:48-0700 PDT` observation is attributed separately to the parent.

At the substantive checkpoint, a direct record was delivered to `Main` stating the following completed mathematical work:

- the entrywise \(E/O\) map and the factors \(h,\ell,\gamma\);
- the independent logical \(m=2\) gap comparison
  \[
  (2G)^2=(2u-1)^2r^2+4u(1-u)r^4\le r^2;
  \]
- extension by spectral mixing and random-unitary dephasing;
- all four block traces and direct-sum assembly without block normalization;
- the second example’s pair spectrum, top-three tensor sum and complex maximizing projector.

The full scientific derivation is included in `review-v1.md` above; this process record does not substitute an IRC summary for the review body.

No thirty-minute active-work checkpoint interval elapsed between the recorded observations.

## Methods, exclusions and delivery

Actual scientific method was written matrix algebra, spectral/Schmidt decomposition, finite ensemble construction and exact auditing of the source-provided example.

Not performed:

- scientific interpreter/CAS/solver execution;
- privately or publicly selected new mathematical instances;
- scientific enumeration, experiments or replay;
- author-code execution;
- builds, tests, lint or formatters;
- external-model CLI, paid/heavy/remote work, installation;
- deletion, credential/provider changes, commit, push or publication.

No original source snapshot was edited. Agent messages were administrative acknowledgement and the required substantive checkpoint, not scientific filesystem writes.

The prospective author-method restoration was honored: earlier general-author fresh examples were permitted. The review did not treat them as violations. Historical genuinely held outputs and all their mathematical, method, selection and confidence consumers remained NONINPUT.

No claim is made about independently observing the author’s historical execution, cognitive isolation, exact private derivation times, original-book authenticity, novelty, or continuous supervision outside the recorded interval.

**Delivery:** complete materializable review and process bodies returned directly. No mathematical blocker or finding remains in the assigned Class B slice; parent disposition and every explicitly excluded assurance gate remain separate.