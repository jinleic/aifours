# Structural continuation and the all-level obstruction

Date: 2026-10-14. The universal characteristic-zero equality is **not proved or refuted**.
This file contains a written consequence of the established dossier and an audit of
the attempted all-level induction. It is not a Lean proof of that consequence.

## A coefficient-three consequence for the fixed-column family

**Written proposition, conditional on the established dossier premises.** Let

\[
A(r,s)=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-r&-s&2\end{pmatrix},\qquad r,s\ge1.
\]

Use the full complex realization in TASK.md. Assuming the dossier's
coefficient-one theorem, coefficient-two theorem, exact lowering recurrence,
positive elimination presentation, and independently accepted uniform
rank-three height-seven theorem, equality holds in every positive degree
with \(\alpha_3\le3\). No new novelty claim is made.

The new step is a finite-Levi structural argument at level three, rather than
another Serre-ideal height computation. The height-seven premise was **read**
from the dossier; its independent checker was not rerun in this repository.

### The level-three free Lie module has no invariant vectors

Let \(V=S_1\). With the original first two rows and third column fixed,
the dossier identifies \(V\) with the adjoint module of \(\mathfrak{sl}_3\).
Before imposing the remaining relations led by node 3, the positive algebra
is \(\mathfrak n_J^+\ltimes L(V)\). Every \(S_k\) is consequently a quotient
of \(L_k(V)\), as a module for the actual finite Levi. This uses the
generator/universal-property presentation in round2-coefficient-two.md §3.1;
it does not replace the original third row.

For any characteristic-zero vector space, there is an exact sequence

\[
0\longrightarrow\Lambda^3V\xrightarrow{j}V\otimes\Lambda^2V
 \xrightarrow{b}L_3(V)\longrightarrow0,
\]

where

\[
j(x\wedge y\wedge z)=x\otimes(y\wedge z)+y\otimes(z\wedge x)
                       +z\otimes(x\wedge y),
\quad b(x\otimes(y\wedge z))=[x,[y,z]].
\]

The wedge map back to \(\Lambda^3V\) composed with \(j\) is multiplication
by 3, so \(j\) is injective. Jacobi gives \(bj=0\). The map \(b\) is
surjective because degree-three bracket words span. For \(\dim V=8\),
the dimensions are 56, 224, and \((8^3-8)/3=168\), respectively. Thus
the kernel of \(b\) is exactly the image of \(j\). These maps are Levi-equivariant.

The dossier's explicit exterior-square decomposition is

\[
\Lambda^2V\cong V\oplus M_{10}\oplus M_{10}^*,
\]

with each summand simple and with no repetitions. The adjoint module is
self-dual by its nondegenerate invariant trace form. Schur's lemma therefore
gives

\[
\dim(V\otimes\Lambda^2V)^{\mathfrak{sl}_3}
 =\dim\operatorname{Hom}_{\mathfrak{sl}_3}(V,\Lambda^2V)=1.
\]

There is a nonzero invariant alternating three-form
\(\omega(x,y,z)=\operatorname{tr}(x[y,z])\). It is alternating by trace
cyclicity and invariant by Jacobi and trace cyclicity. For example,
\(x=H_1=E_{11}-E_{22},y=E_{12},z=E_{21}\) gives value 2.
The trace form identifies this covariant three-form with a nonzero invariant
element of \(\Lambda^3V\). Its image under the injective equivariant \(j\)
spans the one-dimensional invariant space of the middle term.

All three modules are finite-dimensional modules of the complex semisimple
Levi. Complete reducibility makes the invariant functor exact here.
Consequently \(L_3(V)\) has no trivial summand. Every quotient, including
\(S_3\), also has no trivial summand. **This is a statement about invariant
vectors, not the dimension of the zero-weight space.**

### Bounding a possible level-three primitive

The previous levels have no extra ideal. If the extra ideal \(R_3\) were
nonzero, choose a nonzero homogeneous component with least total degree in
nodes 1 and 2. Its vector \(x\) is killed by \(F_1,F_2\). Write its full
multidegree as \((a,b,3)\). The genuine locally nilpotent sl2 calculation
gives

\[
2a-b-3\le0,\qquad -a+2b-3\le0.
\]

Inverting the finite A2 Cartan matrix gives \(a,b\le3\). If either is 3,
the displayed inequalities force \(a=b=3\). Then \(x\) has both Levi
Cartan weights zero. A vector killed by both Levi lowerings and of weight
\((0,0)\) generates a trivial finite-dimensional Levi module: in each sl2
string the recurrence at the last nonzero raising vector forces the string
length to be zero. Hence both raisings kill it as well. This contradicts the
absence of a trivial summand in \(S_3\).

We therefore have \(a,b\le2\), putting this alleged extra relation at total
height at most 7. The established uniform height-seven theorem excludes it.
Together with levels 0, 1 and 2 this proves the stated conditional consequence.
Negative degrees are transported by the usual Chevalley involution when
interpreting the positive result, but no full all-level equality is concluded.

This proof retains the full realization, including the extra Cartan direction
in the singular affine member \(r=s=1\). A Levi-zero weight is not identified
with degree zero of the full realization. The full rank of C remains the
reason that the homogeneous components can be selected separately.

### Small exact character corroboration

levi_character_check.py uses only integer Laurent polynomials for the fixed
adjoint A2 character. If \(X,Y\) denote the two simple-root weights, put

\[
v=2+X+Y+XY+X^{-1}+Y^{-1}+X^{-1}Y^{-1}.
\]

The degree-three exterior and free-Lie characters are

\[
\chi_{\Lambda^3V}=(v^3-3v\psi_2v+2\psi_3v)/6,
\quad \chi_{L_3(V)}=(v^3-\psi_3v)/3,
\]

and \(\chi_{L_4(V)}=(v^4-(\psi_2v)^2)/4\), where
\(\psi_dv=v(X^d,Y^d)\). The exterior formulas follow by expanding products
of eigenvalues. The free-Lie formulas follow from the graded PBW identity
and its logarithm, with Möbius inversion; they are character versions of the
dossier's Witt formula.

For a finite A2 character \(\chi\), its trivial multiplicity is the constant
coefficient of

\[
\chi(1-X^{-1})(1-Y^{-1})(1-X^{-1}Y^{-1}).
\]

This follows from multiplying the Weyl character formula by its denominator;
among dominant highest weights, only the zero highest weight contributes
to that constant coefficient. The script performs all divisions exactly,
checks nonnegative integer weight multiplicities, checks the **whole**
degree-three exact-sequence character identity, and obtains:

| Module | Dimension | Trivial multiplicity |
|---|---:|---:|
| \(V\otimes\Lambda^2V\) | 224 | 1 |
| \(\Lambda^3V\) | 56 | 1 |
| \(L_3(V)\) | 168 | 0 |
| \(L_4(V)\) | 1008 | 1 |

The script is reproducible arithmetic corroboration. It is **not** an
independent Serre checker, a computation of \(K/I\), a Lean theorem, or an
all-height theorem. The written degree-three proof above supplies its
representation-theoretic interpretation independently of its output.

## Why this induction still stops

For \(r,s\ge4\), the omitted-node positive Serre generators have levels
\(r+1,s+1\ge5\). Thus none contributes through level four, and
\(S_4=L_4(V)\). The exact character computation gives a one-dimensional
trivial Levi summand in this actual slice, situated at full degree
\((4,4,4)\). It is killed by the complementary lowerings.

The level-three argument therefore fails at level four: there is now a
nonzero vector of precisely the excluded Levi type. This vector is **not**
a counterexample. The following focused calculation detects this line with
the original omitted lowering. Complementary lowering and a Levi-weight
bound alone would not do so.

### The level-four trivial line is detected for r,s at least four

Use the matrix-model basis

\[
(b_0,\ldots,b_7)=(E_{12},E_{23},E_{13},E_{21},E_{32},E_{31},H_1,H_2)
\]

of V, and its trace-dual basis \((b^i)\). These are **vectors of the
level-one module**. In particular the last two are the positive vectors p
and -q of the dossier's model, not Cartan elements of the ambient algebra.
Construct the following rational Lie polynomial:

\[
X=\sum_{i,j,k,l=0}^7
 \operatorname{tr}((b_i b_j+b_j b_i)[b_k,b_l])
 [b^i,[b^k,[b^j,b^l]]].
\]

The tensor contracted here is invariant under the adjoint Levi action, and
the Lie bracketing is equivariant. The exact calculation also checks
invariance separately under all six named Levi generators. X is nonzero,
has full degree (4,4,4), and spans the unique trivial summand identified by
the character calculation. Its associative expansion has 208 words; the
whole expansion is saved in level4-invariant-vectors.json.

For D3, the original row gives the following level-zero leaf images:

| Model vector in V | Its actual D3 image |
|---|---|
| E12, E23, E13 | 0 |
| E21 | -s e2 |
| E32 | r e1 |
| E31 | -h3 |
| H1-model | -s [e1,e2] |
| H2-model | -r [e1,e2] |

The last four non-Cartan values are the same formulas as Dv, Du, Dw, Dp,
Dq in the dossier, with the displayed basis signs. The first three are
zero because their omitted-node descents land in absent positive A2 Levi
degrees (2,1), (1,2), (2,2); equivalently one obtains zero by continuing
the corresponding raising formulas and the A2 Serre relations. When -h3
acts on a V-vector of full degree (a,b,1), its action uses the original
weight \(-(2-ra-sb)\).

level4_invariant_check.py applies the bracket derivation rule recursively
to the displayed X. It first reproduces the established Dt1, Dt2 and Dz
formulas exactly. The resulting degree-(4,4,3) associative tensor has 37
words. In its ordered basis word E12 E23 H1-model the coefficient is

\[
\frac43(r-1).
\]

This is at least 4 for r at least 4, independently of s. Since the source
and target slices have no omitted-node Serre relation when r,s at least 4,
they are L4(V) and L3(V), respectively. The coefficient proves that D3 X
is nonzero in the actual target slice for all these parameters.

check_level4_invariant.py imports **no producer code**. It reads the saved
tensor, independently checks that its right-nested Dynkin expansion equals
four times itself (which supplies a direct bracket expression for X),
checks all six Levi actions, and computes D3 by deleting a leaf and moving
its level-zero image to the right in each associative word. It verifies
that every terminal Levi/Cartan actor cancels, then compares every affine
coefficient with the recursive result. Both an altered lowering constant
and an altered Lie-tensor coefficient are rejected. The PASS receipt is
level4-independent-check.json, with hashes of vectors and both scripts.

This is exact independent arithmetic verification of **one original-row
map**, together with its explicit Lie interpretation. It is not a Lean
formalization, a complete check of P4, or a proof of R4=0 for this family.
This single-line receipt is now complemented by the separate complete four-cell verification below.

At arbitrary level, fixed-level complete reducibility reduces the problem
to finitely many Levi-lowest lines and their multiplicity spaces. These
multiplicities grow with level; this reduction does not supply a uniform
injectivity theorem. Moreover the original omitted lowering is not generally
a Levi homomorphism, since the brackets \([f_j,f_i]\) need not vanish.

## Other all-height routes examined

1. **Transporting a symmetrizable comparison.** At level one the unchanged
   complementary rows suffice. At higher levels the positive presentation
   changes whenever an omitted-row Serre exponent enters the slice, and the
   omitted lowering already differs on \([e_j,e_i]\): its value is
   \(a_{ij}e_j\). No compatible transport at arbitrary level was obtained.
2. **A nondegenerate symmetric invariant pairing.** If such a form pairs
   each \(e_i\) nontrivially with \(f_i\), put \(q_i=B(e_i,f_i)\).
   Invariance forces \(B(h_i,h_j)=a_{ij}q_j\); symmetry gives
   \(a_{ij}q_j=a_{ji}q_i\). These equations force balanced products around
   every directed cycle. An unbalanced cycle such as \(A(2,1)\) precludes
   this form with nonzero simple-root pairings. The symmetrizable proof's
   nondegeneracy cannot be assumed for the nonsymmetrizable algebra.
3. **Finite-Levi weights alone.** They bound a primitive degree at level k
   by height \(3k\) in this family. This grows with k; the balanced interior
   \((k,k,k)\) has \(A(r,s)\alpha=(0,0,k(2-r-s))\le0\) for all k.
   The necessary primitive inequalities do not eliminate this unbounded
   region. The new level-three absence-of-invariants argument does not persist.
4. **Uniform minors or elimination.** A fixed finite matrix has an exact
   determinant identity; elimination requires checked divisions and a final
   nonvanishing argument. The audited Schur/Pfaffian identities concern a
   different matrix family and provide no all-height positivity theorem.
   No broad finite search or height-thirteen replay was launched.
5. **Induction on rank through a symmetrizable complement.** Even an
   all-level result with this extra hypothesis would not cover every GCM.
   For example a block sum of two nonsymmetrizable A(2,1) matrices has no
   single-node symmetrizable complement. Disconnected blocks could be handled
   separately, but connected diagrams with two disjoint unbalanced triangles
   linked by a symmetric edge give the same obstruction to this hypothesis.
   Any rank induction must address arbitrary nonsymmetrizable complements.
6. **Base change and finite certificates.** Exact rational spaces can be
   extended to C with the stated flatness/exactness premises. This preserves
   a certificate's scope and supplies no bound on the first possible defect.

## Exact next missing lemma

For a node i with symmetrizable complementary Levi J, retain the actual
Serre slice and original omitted row. Assuming \(R_{k-1}=0\), prove

\[
\ker\bigl(D_i|_{P_k}\bigr)=0,\qquad
P_k=\{x\in S_k:[f_j,x]=0\text{ for all }j\in J\},
\]

**for every k**, including trivial Levi summands and repeated lowest-weight
summands. For the displayed family, the complete four-cell calculation below and the preceding trivial-line calculation settle P4 when r,s are at least 4. Level four outside this regime and unbounded higher levels remain unsettled. The criterion already
established in the dossier is necessary and sufficient for that level.
Neither the coefficient-three consequence nor the formal propagation lemmas
prove its all-level injectivity. For the full universal
quantifier, one must additionally handle GCMs with no symmetrizable
single-node complement, or prove the more general statement that every
nonzero homogeneous positive vector of height at least two in the Serre
quotient is detected by some simple lowering.

No nonzero characteristic-zero extra-ideal witness, checked non-Serre
relation, or complete universal induction was obtained. Required universal
reviewer status remains **done:false**.


## Complete level-four detection for r,s at least four

**Written theorem, conditional on the established earlier-level premises.**
For A(r,s), r,s at least 4, equality holds throughout alpha_3 at most 4.
The preceding coefficient-three argument supplies R3=0. A least-Levi-degree
vector of any nonzero R4 is killed by f1,f2 and f3. Its degree (a,b,4)
satisfies 2a-b<=4 and 2b-a<=4. Inverting the finite A2 matrix gives a,b<=4.
If either is 4, both are 4, giving the invariant line already detected.
Every other admissible degree either has a+b<=3, hence height at most seven,
or is one of the four cells below. The height-seven premise excludes the
former; the following exact certificates exclude all four remaining cells.

| Degree | Primitive dimension | Free L4 dimension | Free L3 target dimension |
|---|---:|---:|---:|
| (2,2,4) | 7 | 25 | 13 |
| (3,2,4) | 6 | 36 | 13 |
| (2,3,4) | 6 | 36 | 13 |
| (3,3,4) | 8 | 65 | 18 |

level4_cells_producer.py spans each free Lie space by Dynkin images of all
appropriate words and intersects the two Levi-lowering kernels. It computes
the original D3 images by recursive brackets and selects a maximal minor on
faithful tensor-coordinate rows. After r=4+x,s=4+y, each determinant has a
nonzero constant and coefficients of one sign. Its oriented constant is,
in table order, 262828800, 2015539200, 503884800, 17631936921600. The numbers
of positive terms are 35,27,27,45. Thus every minor is nonzero on x,y>=0.

level4_cells_check.py imports no producer code. It rebuilds all Dynkin spans,
both Levi-action ranks and primitive dimensions; checks completeness and
independence of each supplied primitive basis; computes every affine image
by independent associative word deletion; and verifies target Lie-space
membership. It reconstructs the matrices and determinant polynomials by
memoized Laplace expansion, independently of the producer's subset dynamic
program. Altered lowering and determinant coefficients are rejected in each
cell, and omitted cell coverage is rejected. The exact PASS receipt is
level4-cells-independent-check.json. Full bases, images and polynomials are
in level4-cells-certificate.json. All calculations use rational arithmetic.

This proves the stated level-four consequence with its earlier premises
retained. It is not a Lean formalization or an all-level theorem for any
fixed nonsymmetrizable matrix. No counterexample candidate was found.

## Diagonal specialization

**Written lemma.** For k>=2 in the regime r,s>=k, the spaces Sk=Lk(V),
S(k-1)=L(k-1)(V) and Pk are literally independent of r,s: the remaining
omitted-node Serre exponents r+1,s+1 exceed k. The original D3(r,s) on these
fixed spaces is affine in r,s. For every integer t>=k, A(t,t) is symmetrizable
with symmetrizer (t,t,1), so Gabber-Kac gives R=0 at that specialization.

If a nonzero vector in Pk were killed by D3(t,t), take a nonzero homogeneous
component, using the full Cartan realization. It is killed by all three
simple lowerings. The exact radical recurrence puts its free-Lie
representative in K and produces a nonzero extra-ideal vector, contradicting
R=0. Equivalently its positive adjoint descendants U(n+)x form an ideal
inside the positive part: Jacobi, Cartan weights and induction give lowering
stability, as in the established radical recurrence. Thus D3(t,t) is
injective on Pk.

The ideal of maximal minors of this fixed affine matrix is therefore nonzero
for every k. Its zero locus is a proper algebraic subset and misses every
integer diagonal point (t,t) with t>=k. If Pk=0, use the empty minor 1.
A possible integer failure with r,s>=k must be off the diagonal and lie on
this proper zero locus. This proves generic full rank, not nonvanishing
throughout the entire parameter region. Level one is already covered by
coefficient-one equality; its omitted lowering lands in level zero and
Cartan, so the free-Lie target formula above is stated for k>=2.

This is not the invalid symmetrized-row comparison: in this restricted
regime no omitted-node Serre summand enters either slice. The original map
is explicitly specialized, rather than transported from an unequal row.
For a fixed matrix the lemma covers only k<=min(r,s), not all levels. The
next missing lemma is injectivity on all higher primitive multiplicity
spaces, including outside this regime; the universal quantifier also
requires arbitrary nonsymmetrizable complementary Levis. Universal status
remains done:false.
