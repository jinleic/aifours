# Degree-eight curve obstruction to the primitive-Hermitian real-fibre certificate

Before-creation clock observed: **2026-10-23T13:38:06-07:00**. Active target: P24 under `selection-v2.md`. **CANDIDATE / NOVELTY_UNCLEAR; written reasoning only.** No scientific program, solver or symbolic-algebra execution occurred. This theorem eliminates the first specific real-avoidance representation, not P24 and not every degree-eight curve.

## 1. The actual missing compatibility issue

The ambient real bivector space Lambda^2 R^6 has dimension 15. In the complex identification R^6=C^3, primitive real (1,1) forms correspond to trace-free Hermitian 3x3 matrices, a real space of dimension 8. Every nonzero such form has real rank at least 4: unitary diagonalization gives a real 2-form sum_j lambda_j dx_j wedge dy_j with real rank twice the number of nonzero eigenvalues; trace zero excludes exactly one nonzero eigenvalue. Thus any subspace of these primitive forms has no nonzero real simple bivector.

A seven-dimensional subspace S of this class would be an attractive common kernel for the first eight pole-polynomial coefficient functionals: a real z^8 fibre would require a real decomposable point in that kernel. But the coefficient forms must arise from an actual polynomial decomposable curve. The theorem below proves that at degree eight this entire primitive-Hermitian certificate class forces a base locus, even without restricting to the balanced monic chart.

## 2. Exact algebraic statement

Let V(z) be a 2x6 real polynomial matrix. Suppose:

- its two rows are linearly independent at z=0;
- the maximum degree of its 2x2 minors is exactly 8.

Group the six real coordinates of its rows into three complex coordinates, obtaining polynomial vectors v(z),w(z) in C[z]^3. A bar on a polynomial below means coefficientwise complex conjugation; it does **not** conjugate the variable z. Define the Hermitian-matrix polynomial

    H(z)=(i/2)[v(z) w(z)^* - w(z) v(z)^*],                 (1)

where * means coefficient-conjugate transpose. Every coefficient of H is Hermitian and tr(BH(z)) is a real polynomial for Hermitian B.

Let H_0(3) be the real space of trace-free Hermitian 3x3 matrices. Assume there is a real seven-dimensional subspace S of H_0(3) such that

    tr(BH(z)) is divisible by z^8 for every B in S.          (2)

### Theorem

Under these hypotheses, there exists a fixed real subspace U of R^6 of dimension at most 4 containing both rows of V(z) for every real z, **or** V already has a constant nonzero row after a real unimodular polynomial row operation. In either case a fixed real rank-4 L exists for which

    det[V(z);L] is identically zero.                       (3)

Consequently V is degenerate even over the reals, and a fortiori fails the complex non-degeneracy required by P24.

In particular, **no valid non-degenerate degree-eight P24 candidate can have its first eight coefficient-kernel constraints certified by a seven-dimensional primitive-Hermitian subspace**, for any fixed orthogonal complex structure on R^6.

The conclusion is an all-curve obstruction within the named certificate class, not a finite search exclusion, a statement that every real-avoidance kernel is Hermitian, or a proof of generic stabilizability.

## 3. Polynomial row reduction preserves the hypothesis

First reduce the polynomial row degrees without changing their wedge. Suppose the row degrees are a>=b and their real leading coefficient vectors are dependent. Subtract an appropriate real multiple of z^(a-b) times the lower-degree row from the higher-degree row. This is a polynomial row operation of determinant 1 and strictly lowers the sum of degrees. Repeat until the leading row coefficients are independent; generic row independence prevents a zero row. The process terminates because the degree sum is a nonnegative integer.

The wedge of the rows is unchanged throughout. At termination, independent leading coefficients make its degree equal to the sum of row degrees. Since its coordinates are exactly the 2x2 minors, the resulting degrees a,b satisfy

    a+b=8.                                                 (4)

For real polynomial row operations H transforms by their determinant, just like the real alternating bivector: the coefficients multiplying v v^* and w w^* cancel, and the cross terms scale by the 2x2 determinant. Thus H itself is unchanged for these determinant-1 operations. Condition (2) and row rank at zero are preserved. Existence of an L satisfying (3) is also invariant under the operations.

If one reduced row has degree zero, it is a fixed nonzero real vector lying in every row plane. Any real four-plane containing that vector makes the stacked determinant vanish identically. This is the theorem's constant-row alternative.

Henceforth assume both reduced degrees are positive. Then

    1<=a,b<=7.                                             (5)

No external polynomial-minimal-basis theorem is needed for this reduction.

## 4. What a seven-dimensional annihilator actually forces

Put H0=H(0). Since the two original real rows at zero are independent, H0 is nonzero. Indeed, H0=0 would imply v0 w0^*=w0 v0^*, which forces w0 to be a **real** multiple of v0, contradicting real independence. Also rank_C(H0)<=2, so H0 cannot be a nonzero multiple of I_3.

Thus the primitive projection

    P(H0)=H0-(tr H0/3)I_3

is nonzero. The constant coefficient of (2) gives

    S subset {B in H_0(3): tr(BH0)=0}.

The right side has dimension 7, so equality holds. In the nine-dimensional real space of Hermitian matrices, the orthogonal complement of S is exactly span_R{I_3,H0}. Consequently (2) is equivalent to the following jet constraint:

    H(z)=alpha(z)I_3+beta(z)H0  modulo z^8,                 (6)

for real scalar polynomials alpha,beta, where modulo z^8 means equality of coefficients of degrees 0 through 7. We need only this necessary constraint, not any converse about realizability of H.

There are two cases according to the complex linear dependence of v0,w0.

## 5. Complex-independent initial rows force a fixed real four-space

Suppose v0,w0 are independent over C. Choose a constant unitary coordinate change so their complex span is the first two coordinate directions. Then v_3(0)=w_3(0)=0 and H0 has zero third row and column. Equation (6) implies

    H_31(z)=H_32(z)=0 modulo z^8.

Using (1), this says

    v_3(z) bar(w_j)(z)-w_3(z) bar(v_j)(z)=0 modulo z^8,
    j=1,2.                                                (7)

The 2x2 coefficient matrix in the unknowns v_3,w_3 has at z=0 the columns bar(w0),-bar(v0) restricted to their first two entries. It is invertible because v0,w0 are C-independent. It therefore has an inverse over C[[z]], the formal power-series ring: its determinant has nonzero constant term and is a unit. Equations (7) force

    v_3,w_3 divisible by z^8 in C[[z]].

Both are polynomials of degree at most 7 by (5), so they vanish identically. Thus both rows stay in the fixed C^2, which is a fixed real four-space. Choosing L to span that space proves (3).

This argument shows why a pointwise real-rank-avoidance subspace cannot simply be prescribed as the eight coefficient constraints: the jet compatibility already removes the unused complex direction.

## 6. Complex-dependent initial rows: the remaining possible escape also degenerates

Suppose v0,w0 are C-dependent but R-independent. First interchange the reduced rows if necessary so that deg v<=deg w. A degree-preserving constant real triangular row change and a constant unitary coordinate change put

    v0=e_1, w0=i e_1,
    H0=E_11.                                               (8)

To justify the row normalization, write w0=(A+iB)v0 with B!=0, subtract A times the lower-degree first row from the second and divide the second by B, then scale and rotate the common vector to e_1. Because deg v<=deg w and their reduced leading coefficients are independent, this triangular operation preserves both row degrees and their sum 8; equal degrees cause no cancellation of the independent leading vectors. Scaling and the ambient unitary change also preserve those degrees. The constant row change only multiplies H by a nonzero real constant, so the span condition (6) is preserved.

Write v_perp=(v_2,v_3), w_perp=(w_2,w_3). If both vanish identically, the rows stay in the fixed complex line and (3) follows immediately. Otherwise let k>=1 be the smallest vanishing order at zero among their nonzero components. By (5), k<=7.

The cross-block entries H_21,H_31 vanish modulo z^8 by (6). In their coefficient of degree k, use bar(w_1)(0)=-i and bar(v_1)(0)=1. If u is the degree-k coefficient of v_perp and v is that of w_perp, the equation is

    -i u-v=0.

Thus u is nonzero, both perpendicular vectors start at the same order k, and

    v_perp=z^k u+O(z^(k+1)),
    w_perp=-i z^k u+O(z^(k+1)).                            (9)

The lower 2x2 block of H therefore has coefficient

    -u u^*  at degree 2k.                                 (10)

If 2k<8, equation (6), whose H0 has zero lower block, requires this coefficient to be a scalar multiple of I_2. But -u u^* has rank one and is nonzero, while a scalar multiple of I_2 has rank zero or two. This is impossible. Therefore k>=4.

Both rows have perpendicular components starting at k, so their degrees each are >=4. Equation (4) then forces a=b=4 and k=4. There are no higher coefficients in those perpendicular vectors, so (9) is exact:

    v_perp=z^4 u,  w_perp=-i z^4 u.                        (11)

For every real z both rows lie in the fixed complex span of e_1 and u, of complex dimension at most two. Its real dimension is at most four. A real four-plane containing it supplies L and proves (3). QED.

## 7. Binding to the P24 coefficient-kernel route

For a Hermitian B, tr(BH(v,w)) is a real alternating bilinear form in the underlying real vectors v,w. In a unitary eigenbasis of B, the associated real two-form has coefficients lambda_j on dx_j wedge dy_j. Thus trace-free Hermitian B are precisely the primitive-Hermitian two-form certificate class described in Section 1.

For V's row-wedge p(z), annihilation by the first eight coefficient functionals of any B in S is exactly (2). A proposed degree-eight curve whose first-coefficient kernel contains such an S therefore satisfies the theorem. A valid Q(2,6) candidate has row rank 2 at zero: otherwise every minor would have factor z. Hence the row-rank hypothesis is automatic for the intended basepoint-free target, not an added generic assumption.

All unimodular row reductions and constant changes above preserve degeneracy, so the obstruction is not confined to one row basis or to the initially preferred balanced chart. It applies to every degree-eight polynomial row curve satisfying this particular primitive-Hermitian kernel condition.

## 8. Consequence and next exact missing ingredient

This closes the first proposed Hermitian-kernel ansatz negatively: its appealing seven-dimensional real-simple-form avoidance is **incompatible with non-degenerate degree-eight curve jets**. The actual obstruction is the formal-unit equation in the noncomplex initial-plane case and the rank-one lower-block coefficient at order 2k in the complex-plane case. No random search or small extra enumeration was needed.

P24 remains **OPEN / not decided here**. The result does not exclude non-Hermitian seven-dimensional real-avoidance kernels, different exact certificate types, or a universal positive theorem. The next representation must leave the trace-free-Hermitian kernel class, not merely tune its coefficients, rotate the complex structure, or change the polynomial row-degree split. The primitive-Hermitian class is excluded by the theorem for all those choices.

Correctness needs a parent and independent written reconstruction of the full argument, especially the coefficientwise conjugation convention, row-reduction invariance, rank-one leading block and relation to the Plucker coefficient kernel. Scientific priority is unestablished; formal-jet and polynomial-basis ideas are classical. The source-control finding remains internal only, and no compute/CLI/contact permission is inferred.
