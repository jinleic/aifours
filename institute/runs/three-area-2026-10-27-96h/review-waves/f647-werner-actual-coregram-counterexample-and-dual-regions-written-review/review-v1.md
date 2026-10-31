# f647 written review — full body for parent materialization

**Reviewed candidate:** `f643-werner-two-copy-actual-rank2-nontrivial-frontier/author-candidate-v1.md`, SHA-256 `ccaf062c7547afd3d3c618b95673d1fb9fb6cc2a0fbd2632f1ee7276e7e53121`, complete LF 1–162, as S1 in the frozen packet.

**Verdict:** The candidate’s mathematical claims are supported at their stated scopes. The supplied actual frame refutes the universal sufficient CORE-GRAM premise, **not** Q or T2. Both the actual-frame Q region and the separate physical-pair region have valid written proofs.

**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.** No candidate correction is required by this review. This is a written reconstruction, not parent adoption or machine certification.

No repository file was written under the read-only review role; this is the complete review body.

## 1. Coverage, process and exact imports

Before mathematical packet access, I read the complete manifest, freeze receipt, parent-supplied metadata, actual dispatch receipt and every listed status-only control through their endings, then sent a direct PREBODY ACK to Main.

I subsequently read the entire literal packet, LF 1–243, in ordered RAW windows of at most 20 LF, including the final line. The displayed windows had no unresolved elision. All derivations below followed that complete read.

Bindings supplied by the parent:

- Manifest: `32df0f3a247cbd6984f026d70ddf5dae55af05e85477245106cc66efdbd363f7`.
- Freeze receipt: `762228109c5c9e8a613758f8cb92ce69731e4208feda213c01ee49d608df9df7`.
- Literal packet: `00ccd1c74e03ea8f8207463722d5855f100ade8febcefd0df46346cfab39b41d`.

These are attributed as parent-supplied metadata, not independent child hash observations.

The mathematical imports were exactly:

| Packet source | Scope used |
|---|---|
| **S2**, complete LF 1–20; SHA `5c9e3f6d05d7f28cadc3c25e1b5d66a4a78b129bd53ad9c25b8ebd84946ce3f7` | Double-universal Q/T2 formulation, rank-one swap identity, previously paid dual classes, and the conditional—not unconditional—CORE-GRAM route. The relevant duality and swap arguments are reconstructed below. |
| **S3**, complete LF 1–9; SHA `2df022ab3f005756bcc194598fab8c894931269693c84df6ee834e4f2f62f65d` | Read before S4. The corrected coefficient identities are \(M=VU^\dagger\) and \(N=(U^\dagger V)^T\); the outer operation is ordinary transpose. |
| **S4**, complete LF 1–19; SHA `172a018df9db48431fdf59a3ea55fc69fadcde9738b0fbfd893f4d695dab3a8c` | Imported theorem scope for separately 2+2-reducing physical pairs. Its complete underlying source proof was not supplied or followed; it is not claimed as newly reconstructed here. |
| **S5**, complete LF 1–31; SHA `702b660be092f0fc5e7a44f0794699a6c4cf8c504f280647b1508177ac911916` | Common-local-qubit support class and the separately qualified original-projector result. The underlying equality-classification proof is not claimed as newly reconstructed here. |

All held episodes and all their consumers—including the held CORE diagnostic and f285/f289—remained NONINPUT. I did not follow source links, inspect sibling reviews or author code, introduce an additional selected example, or run scientific code, CAS, a solver, enumeration, tests, builds or external-model tools.

## 2. Per-claim dispositions

| Claim and candidate LF | Disposition | Reconstructed scope |
|---|---|---|
| Definitions, complex conjugations, rank-one bound; LF 7–32 | **SUPPORTED** | Correct sesquilinear expansions under the declared conjugate-linear-first convention. The historical displayed convention is distinguished below. |
| Actual doubly orthonormal frame and CORE-GRAM failure; LF 36–59 | **SUPPORTED** | Actual vectors in \(\mathbb C^4\otimes\mathbb C^4\), both \(p_i>0\), and the strict comparison \(900>672\). The universal CORE-GRAM premise is **REFUTED**. |
| Actual rank-two \(16\times16\) operator, marginals, \(G<0\), Q check; LF 61–77 | **SUPPORTED** | Exact matrix and arithmetic independently reconstructed in writing. Q holds strictly for this operator. |
| Non-EP, nonzero cross term and full common local supports; LF 79 | **SUPPORTED** | Applies to this actual operator, not an auxiliary compression. |
| Perturbation and nonempty open full-Schmidt frame set; LF 81–87 | **SUPPORTED** | Orthogonality, both determinant formulas and continuity argument reconstructed. |
| Entire-span sufficient region \(q_1+q_2\le2\); LF 91–104 | **SUPPORTED** | All complex coefficients and phases, not just nonnegative singular weights. The union-extension claim is supported against the explicitly imported dual classes. |
| Coefficient-dependent region and ratio \(3-2\sqrt2\); LF 106–110 | **SUPPORTED** | Sufficient conditions only, including zero and rank-one boundaries. |
| Exact determinant criterion and residual; LF 112–126 | **SUPPORTED** | Necessary and sufficient on each actual frame; globally equivalent to Q when quantified over every actual frame. |
| Hypothetical determinant violation converted to actual \(A,B\); LF 128–133 | **SUPPORTED** | The complex phase choice \(z_1=h,\ z_2=\alpha_1\) is correct. No violating frame is supplied or inferred. |
| Separate physical-pair singular-gap region; LF 137–145 | **SUPPORTED** | Derived independently from rank-one duality, without assuming global Q. |
| Explicit physical pair, numerical bound, irreducibility and open extension; LF 147–155 | **SUPPORTED** | Actual \(16\times16\) Kronecker sum; both local matrices irreducible, both squares nonnormal, strict singular-gap bound. |
| Author chronology and execution self-report; LF 159–161 | **INCONCLUSIVE as independent certification** | These are author-reported facts. This review did not independently observe the author’s private chronology or execution history. This is not a mathematical defect. |
| Unrestricted Q/T2, T3/q3, novelty, human/kernel or independent-family acceptance; LF 162 | **NOT ESTABLISHED**, consistently with the candidate | No whole-target or stronger acceptance follows from this review. |

## 3. Complex conventions and the conditional route

With the declared inner product,
\[
\langle A,B\rangle=\operatorname{Tr}(A^\dagger B),
\]
and \(c_i=\operatorname{Tr}x_i\), the cross coefficient of the trace norm is necessarily \(\overline{c_1}c_2\). Therefore
\[
G(z_1x_1+z_2x_2)
=
4p_1|z_1|^2+4p_2|z_2|^2
+2\operatorname{Re}\!\left[
\overline{z_1}z_2
(\overline{c_1}c_2-C_{12})
\right].
\]
This agrees with S1 LF 30.

In particular,
\[
h=\langle F(x_1),F(x_2)\rangle
=C_{12}-\tfrac12\overline{c_1}c_2
\]
is the upper-right entry of the Hermitian matrix representing \(q\) on the coefficient vector \((z_1,z_2)\).

The historical S2 LF 11 displays \(c_1\overline{c_2}\). I have not copied that expression as the sesquilinear coefficient for the candidate’s definitions. The candidate explicitly acknowledges the distinction at LF 32. On the supplied real frame the two products coincide, so the counterexample directly violates the historical displayed CORE-GRAM inequality as well; it does not depend on silently changing its conjugation convention.

The rank-one identity is also correct. Regrouping the two copies into their A and B factors,
\[
1+|\langle v,u\rangle|^2
-\|\operatorname{Tr}_B|u\rangle\langle v|\|_F^2
-\|\operatorname{Tr}_A|u\rangle\langle v|\|_F^2
=
\langle u\otimes v,(I-F_A)(I-F_B)u\otimes v\rangle .
\]
The swaps commute and each \(I-F\) is positive semidefinite. Hence \(p_i\ge0\), and
\[
q(x_i)=1+\tfrac12|c_i|^2-4p_i\le\tfrac32.
\]

The sufficient implication remains valid: the phase-uniform CORE-GRAM bound would make the \(G\)-matrix positive semidefinite and give \(G(R)\ge0\) for every rank-at-most-two \(R\). Since
\[
|\operatorname{Tr}R|^2\le2\|R\|_F^2,
\qquad
q(R)=\|R\|_F^2+\tfrac12|\operatorname{Tr}R|^2-G(R),
\]
this would imply Q and then T2.

**The new example falsifies that sufficient premise, not this conditional implication and not its conclusion.**

## 4. Reconstruction of the actual counterexample

Write \(r=\sqrt{101}\). The supplied vectors satisfy
\[
\|a\|^2=(16+4+4+1)/25=1,\qquad
\|v_1\|^2=(36+64+1)/101=1.
\]
The support of \(a\) is diagonal, whereas those of \(u_1,v_1\) are off-diagonal. Thus both required orthogonality relations hold. These are actual left and right singular frames.

The dyad is
\[
x_1=-\frac{
6|01\rangle\langle01|
+8|01\rangle\langle02|
+|01\rangle\langle10|
}{r}.
\]
Taking partial traces gives exactly
\[
\operatorname{Tr}_B x_1=-6E_{00}/r,\qquad
\operatorname{Tr}_A x_1=-(6E_{11}+8E_{12})/r.
\]
For \(x_2=|a\rangle\langle a|\), both marginals are
\[
\rho=\operatorname{diag}(16,4,4,1)/25,\qquad
\|\rho\|_F^2=289/625.
\]

Consequently,
\[
4p_1=1+\frac{36}{101}-\frac{136}{101}=\frac1{101},
\qquad
4p_2=2-\frac{578}{625}=\frac{672}{625},
\]
and
\[
C_{12}=-\frac{6(16+4)}{25r}
=-\frac{24}{5r},
\qquad
\overline{c_1}c_2-C_{12}=-\frac6{5r}.
\]
Both \(p_i\) are strictly positive. Nevertheless,
\[
\left|\overline{c_1}c_2-C_{12}\right|
=\frac{30}{25r}
>
\frac{4\sqrt{42}}{25r}
=4\sqrt{p_1p_2},
\]
because \(900>672\). Equivalently, the determinant of the actual \(G\)-matrix is
\[
\frac{672-900}{63125}=-\frac{228}{63125}<0.
\]
The universal sufficient CORE-GRAM premise is therefore false on actual d=4 frames.

### Actual operator and independent Q test

The operator retained for this check is the complete \(16\times16\) operator
\[
R=\frac1r\left(
|a\rangle\langle a|
-6|01\rangle\langle01|
-8|01\rangle\langle02|
-|01\rangle\langle10|
\right),
\]
not a projected or relaxed object. Its SVD weights are \(1,1/r\).

Its marginals are
\[
\operatorname{Tr}_B R
=\frac{\operatorname{diag}(-134,4,4,1)}{25r},
\]
\[
\operatorname{Tr}_A R
=\frac{\operatorname{diag}(16,-146,4,1)-200E_{12}}{25r}.
\]
Their squared norms are respectively
\[
\frac{134^2+4^2+4^2+1}{63125}
=\frac{17989}{63125},
\]
\[
\frac{16^2+146^2+4^2+1+200^2}{63125}
=\frac{61589}{63125}.
\]
Together with
\[
\|R\|_F^2=\frac{102}{101},\qquad
\operatorname{Tr}R=-\frac5r,
\]
these give
\[
G(R)=\frac{79375-79578}{63125}
=-\frac{203}{63125},
\]
but
\[
q(R)=\frac{143531}{126250}
<
\frac{255000}{126250}
=2\|R\|_F^2.
\]
The actual Q gap is
\[
2\|R\|_F^2-q(R)=\frac{111469}{126250}>0.
\]
Thus this is explicitly **not a Q counterexample**.

The range and adjoint range are respectively
\[
\operatorname{span}\{|01\rangle,a\},
\qquad
\operatorname{span}\{v_1,a\}.
\]
The \(|02\rangle\) and \(|10\rangle\) components of \(v_1\) show that these spaces differ, so \(R\) is not EP. Its trace and \(C_{12}\) are nonzero. Any common local support must contain \(a\), whose Schmidt rank is four, so both common local supports are full.

The singular values are distinct; hence an alternative SVD cannot replace this with a zero-cross-term frame. This supports the claimed strict extension of the explicitly imported easy dual classes.

## 5. Perturbation and full-Schmidt frames

For the supplied \(w\),
\[
\|w\|^2=(1+1+1+64)/67=1,\qquad
\langle a,w\rangle=(4+2+2-8)/(5\sqrt{67})=0.
\]
Its diagonal support also makes it orthogonal to \(u_1,v_1\). The perturbed frames therefore satisfy the required normalization and orthogonality exactly.

Set \(t=\epsilon/\sqrt{67}\). The coefficient matrix of \(u_1(\epsilon)\) is upper triangular apart from its already upper-triangular \(E_{01}\) entry, giving
\[
\det U_1(\epsilon)
=-\frac{8t^4}{(1+\epsilon^2)^2}.
\]
For \(v_1(\epsilon)\), expansion through the last two rows gives
\[
\det V_1(\epsilon)
=
-\frac{8t^2(t^2-6/101)}{(1+\epsilon^2)^2}.
\]
These establish the asserted full Schmidt ranks for sufficiently small nonzero \(\epsilon\), with no additional selected value required.

Strict CORE-GRAM failure, positive \(p_i\), nonzero trace and the positive Q gap are continuous conditions and persist near the original frame. A sufficiently small nonzero point on the supplied path has all four vectors full-Schmidt; full Schmidt rank is itself open. The claimed nonempty open set in the product of complex Stiefel manifolds follows.

## 6. Actual-frame Q region and exact residual

The triangle inequality and Cauchy–Schwarz give
\[
q(z_1x_1+z_2x_2)
\le
(|z_1|\sqrt{q_1}+|z_2|\sqrt{q_2})^2
\le
(q_1+q_2)(|z_1|^2+|z_2|^2).
\]
The dyads are Frobenius-orthonormal, so the last coefficient norm is exactly the squared Frobenius norm of the operator. Thus \(q_1+q_2\le2\) pays the **entire complex span**. Substituting the rank-one identities gives precisely criterion (5).

For the supplied frame,
\[
q_1=\frac{118}{101},\qquad
q_2=\frac{531}{1250},\qquad
q_1+q_2=\frac{201131}{126250}<2,
\qquad
h=-\frac9{5r}.
\]
This verifies the whole-span claim independently of the single-operator Q calculation.

For arbitrary SVD weights, the bound \(q_i\le3/2\) gives
\[
q(R)\le\tfrac32(s_1+s_2)^2.
\]
For \(s_1>0\) and \(r_s=s_2/s_1\in[0,1]\), the sufficient comparison with \(2(s_1^2+s_2^2)\) becomes
\[
r_s^2-6r_s+1\ge0,
\]
which is exactly \(r_s\le3-2\sqrt2\) on this interval. Zero and rank-one cases are valid.

The exact gap matrix is
\[
K=
\begin{pmatrix}
\alpha_1&-h\\
-\overline h&\alpha_2
\end{pmatrix},
\qquad \alpha_i=2-q_i\ge\tfrac12.
\]
Therefore Q holds for every complex coefficient vector exactly when
\[
|h|^2\le\alpha_1\alpha_2.
\]
For the supplied frame its determinant is
\[
\frac{84}{101}\frac{1969}{1250}
-\frac{81}{2525}
=\frac{80673}{63125}>0.
\]
This is a further exact confirmation that the entire span obeys Q despite failing CORE-GRAM.

### Complex-phase-correct violation construction

If an actual frame were to have \(|h|^2>\alpha_1\alpha_2\), the candidate’s choice
\[
(z_1,z_2)=(h,\alpha_1)
\]
is correct: its cross term is
\[
-2\operatorname{Re}(\overline h\,\alpha_1 h)
=-2\alpha_1|h|^2.
\]
Thus
\[
z^\dagger Kz
=\alpha_1(\alpha_1\alpha_2-|h|^2)<0.
\]
Both coefficients are nonzero, so the resulting operator has rank two.

With the actual partial traces of that operator,
\[
A=(\operatorname{Tr}_B R)_0,\qquad
B=(\operatorname{Tr}_A R)_0,
\]
one has
\[
L=q(R),\qquad
\langle R,A\otimes I+I\otimes B\rangle=q(R).
\]
Rank-two Ky Fan duality then gives
\[
S_2(X)\ge\frac{q(R)^2}{\|R\|_F^2}>2L.
\]
No conjugation or tensor-leg correction is missing.

This also reconstructs the double-universal equivalence: Q gives T2 by weighted Cauchy–Schwarz and rank-two duality; universal T2 gives Q by this choice of \(A,B\), with \(q=0\) immediate. It does **not** identify a fixed physical pair with an arbitrary fixed frame.

## 7. Independent physical-pair region and actual irreducible example

For a normalized leading singular dyad \(x\) of the actual \(X\),
\[
\sigma_1^2=|\langle x,X\rangle|^2
\le Lq(x)\le\tfrac32L.
\]
This uses only the rank-one swap bound, not unrestricted Q. Therefore
\[
\sigma_2/\sigma_1\le1/\sqrt3
\quad\Longrightarrow\quad
S_2(X)\le\tfrac43\sigma_1^2\le2L.
\]
The zero case is immediate, and the strict ratio condition defines an open set away from zero.

For the supplied \(M=D+N/10\), the complete physical operator is
\[
X=M\otimes I_4+I_4\otimes M.
\]
The diagonal \(X_0\) has one singular value 6 and fifteen singular values 2. The shift \(N\) has operator norm one, hence
\[
\|X-X_0\|_{\rm op}\le1/5.
\]
Consequently,
\[
\sigma_1(X)\ge29/5,\qquad
\sigma_2(X)\le11/5,\qquad
\frac{\sigma_2}{\sigma_1}\le\frac{11}{29}<\frac1{\sqrt3}.
\]
Also,
\[
L=2(12+3/100)=1203/50,
\]
and independently
\[
S_2(X)
\le
\left(1+\frac{121}{841}\right)\frac32L
=\frac{1443}{841}L<2L.
\]
The displayed physical-example bound is correct.

For irreducibility, the 3-eigenspace is exactly \(\operatorname{span}\{e_0\}\). An orthogonal projection commuting with \(M\) must take \(e_0\) to either zero or itself and, by Hermitian adjunction, also commute with \(M^\dagger\). The supplied cyclic chain then forces the same action on \(e_1,e_2,e_3\), so the projection is zero or identity. Thus neither local matrix admits a 2+2 reducing decomposition.

Moreover,
\[
(M^2)_{01}=(3-1)/10=1/5.
\]
Since \(M^2\) is upper triangular and not diagonal, it is nonnormal. Both squares are therefore nonnormal.

The openness argument is valid: irreducibility makes the commutator map injective on traceless Hermitian matrices; compactness of their unit sphere gives a strictly positive minimum commutator norm, preserved under small perturbations. Nonnormality of the squares and the strict singular gap also persist. This produces an open set of traceless physical pairs beyond the separately 2+2 class.

It does not establish that this example avoids S5’s maximizing-projector condition or every other known physical class; the candidate correctly makes neither claim.

## 8. Final disposition and unpaid target

The following are supported by this written reconstruction:

1. A genuine actual-frame counterexample to the universal sufficient CORE-GRAM premise, with both diagonal gaps positive.
2. An explicit actual rank-two operator with \(G(R)<0\) but a strictly satisfied Q inequality.
3. A sufficient entire-complex-span Q region, a sufficient singular-value-ratio region, and the exact frame determinant criterion.
4. A phase-correct conditional construction turning a future actual determinant violation into an actual physical T2 violation.
5. A separately proved open physical-pair region containing the supplied irreducible, both-squares-nonnormal example.

The exact original target remains
\[
S_2(A\otimes I_4+I_4\otimes B)
\le2(\|A\|_F^2+\|B\|_F^2)
\]
for **every** traceless complex \(4\times4\) pair \(A,B\). This review neither proves nor refutes it. Equivalently, the determinant inequality must still be established for every remaining actual frame; the new criterion pays all frames with \(q_1+q_2\le2\), while the candidate does not resolve all frames with \(q_1+q_2>2\).

**Overall correctness: correct.** No mathematical defect was found in the candidate at its explicitly limited scopes. The CORE-GRAM failure is a sufficient-route failure only; unrestricted Q/T2 remains unpaid.

**Confidence: 0.98**, for this written mathematical reconstruction only. No scientific execution, independent-family, human, formal/kernel or novelty acceptance is claimed.