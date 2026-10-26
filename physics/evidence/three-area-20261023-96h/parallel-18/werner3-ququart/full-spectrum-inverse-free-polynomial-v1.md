# Full-spectrum return after v30-A: an inverse-free integer polynomial target

Observed `/bin/date` before this return packet: **Sun Oct 25 04:34:52 PDT 2026**. Owner PhysicsResearch96h. The assigned v30-A review was completed first in `peer-review-ph7-nonuniform-band-conic-v1.md`, SHA256 `589654952d0268e5b43e356acae34c492dda14945543ab5bbe23f464a425bf18`.

**WRITTEN candidate at exact representation/witness-completeness scope; final sign NOT_PROVED.** No scientific arithmetic interpreter, eval, symbolic program, enumeration, replay, solver, model CLI or nested agent was used for this packet. All derivations below are written algebra. Parent erratum v7 and the owned `resumption-arithmetic-authority-addendum-v1.json` remain mandatory; earlier unadmitted outputs are not premises.

## 1. Why this is a different representation of the same target

The first return packet `full-spectrum-pair-condensation-v1.md`, SHA256 `1a814168eec30b5a8698b669fceae33145862f58c1b380d0f6b679caecf8fe98`, reduced p12 inversion to positive two-by-two edge metrics and four-row cores. Its final coupled six-matrix inequality is still open. Another variant obtained by dropping its signed row update or a positive square would not answer the assignment.

Here the actual ENTIRE joint p12/q6 form is instead homogenized into ONE integer-coefficient symmetric polynomial matrix. There are NO matrix inverses or square roots in the new target. The representation is exact over the full spectrum domain, not merely sufficient. It also gives a complete INTEGER negative-witness formulation and an equivalent set of eighteen symmetric polynomial inequalities. Neither positive polynomial coefficients nor a finite search bound is assumed or computed.

Named imports remain the full generic operator identities G1-G12, the two mandatory generic addenda including the complete S_c, the literal full raw q matrix from `all-reference-four-residuals-v1.md` R5-R7, and the p-only Hodge/strictness result. Their SHA256 pins and parent v17/v24 boundaries are listed in the pair-condensation packet Section1. G13 and bare-lift contractivity remain FALSE certificates and are not used. The present polynomial construction does not require the pair-condensation's four-row inverse formula as a premise; it uses only its directly derived H,B,A joint entries, restated below through their cleared form.

## 2. Homogeneous variables and one everywhere-positive denominator

Choose arbitrary y_i>=0, not all zero, and set

```
s=sum_i y_i,
x_i=y_i/s,
delta_i=s-y_i,
a_ij=delta_i+delta_j=2s-y_i-y_j,
W3=e3(delta),
R4=product_i delta_i,
J6=product_(i<j) a_ij,
kappa=8 s^4 W3 J6.                                        (H1)
```

For the interior y_i>0 the physical quantities are

```
d_i=delta_i/s,
d_ij=a_ij/(2s),
r=R4/(s W3),
W=W3/s^3.                                                 (H2)
```

These are algebraic identities: `sum_i 1/d_i=s W3/R4` when all delta_i>0.

The common denominator kappa is STRICTLY POSITIVE on the entire nonzero closed nonnegative orthant. Indeed s>0 and `a_ij>=s>0`. If at least two y_i are positive, every delta_i>0. At a one-coordinate ray the other three delta's equal s, so W3 still has a positive term s^3. Thus W3>0 and kappa>0, including product-reference rays. This is not a denominator whose zero set could hide a negative target value.

## 3. The full eighteen-by-eighteen integer polynomial matrix

Use twelve ordered p coordinates t_ij (i!=j) and six unordered q coordinates v_{ij}. Write the direct full joint matrix as

```
J(x)=[[H(x),B(x)],[B(x)^T,A(x)]].
```

All q-plus directions and the full raw energy A, including every shared-edge coefficient, are retained. Define

```
P(y)=kappa(y) J(y/s).                                      (H3)
```

The following explicit entries show, WITHOUT an inverse or a computation, that P is a symmetric matrix with INTEGER polynomial entries, homogeneous of degree13. Put

```
L_i=s R4-W3 delta_i y_i.
```

The p block entries are

```
(P_H)_(ij,ij)=8 J6[W3 delta_i^2 y_i y_j+L_i y_j^2],
(P_H)_(ij,it)=8 J6 L_i y_j y_t       (i,j,t distinct),
(P_H)_(ij,ji)=8 J6 s R4 y_i y_j.                           (H4)
```

All other p entries are zero apart from the symmetric counterparts. The p/q cross block is

```
(P_B)_(ij,{i,j})=-4 W3 J6 delta_i y_i y_j(s+delta_i-y_j),
(P_B)_(ij,{i,t})= 4 W3 J6 delta_i y_i y_j y_t
                                           (i,j,t distinct),
(P_B)_(ij,e)=0 if e is not incident to i.                    (H5)
```

For complementary pairs {i,j}, {k,l}, the raw q block is

```
(P_A)_({i,j},{i,j})
 =J6 y_i y_j a_ij^2(6W3-s a_ij a_kl),
(P_A)_({i,j},{i,t})
 =-2W3 (J6/a_jt)y_i y_j y_t a_ij a_it,
(P_A)_(e,f)=0 if e,f are disjoint.                          (H6)
```

Here `J6/a_jt` means the PRODUCT of the other five a factors, so it is an integer polynomial, not a variable denominator. Every displayed block is homogeneous of degree13: for example H4's bracket has degree7 and J6 degree6, while the shared-edge expression in H6 has degrees3+5+3+2. No matrix sign is inferred from the signs of these individual scalar entries.

For completeness, substitution of H2 into the original radical-free raw diagonal gives

```
A_ee
 =y_i y_j a_ij^2(6W3-s a_ij a_kl)/(8s^4W3),
```

and the shared-edge term gives

```
A_({i,j},{i,t})
 =-y_i y_j y_t a_ij a_it/(4s^4 a_jt).
```

Multiplication by kappa is exactly H6. Thus this is the original Qraw, not the R0 diagonal or a commutator-free approximation. H4/H5 follow in the same way from

```
H_(ij,ij)=d_i^2 x_i x_j+(r-d_i x_i)x_j^2,
H_(ij,it)=(r-d_i x_i)x_jx_t,
H_(ij,ji)=r x_i x_j,
B_(ij,{i,j})=-d_i x_i x_j(1+d_i-x_j)/2,
B_(ij,{i,t})=d_i x_i x_j x_t/2.
```

These are the exact variance/swap/cross identities, not finite interpolations.

## 4. Exact equivalence with the full E_full sign

For positive y, the old p chart is

```
T_ij=t_ij (i!=j),
T_ii=-(sum_(j!=i)x_j t_ij)/x_i,
Z_ij=c_i c_j T_ij,
c_i=sqrt(x_i).
```

It is bijective onto every complex Zc=0. The q chart is

```
U_ij=sqrt(2)c_i c_j v_ij, U_ii=0, U^T=U.
```

It covers every complex symmetric zero-diagonal U. Therefore

```
(t,v)^dagger J(x)(t,v)
 =<Z,rho'Z>+2Re<Z,h_c(U)>+Qraw(U).                          (H7)
```

The positive interior q pivot A is the ENTIRE raw pivot `M+C^dagger C+2S_c`. Its minimization gives exactly the old E_full,c(Z), not E_strong. Consequently

```
E_full,c(Z)>=0 for every positive spectrum and all Zc=0
 iff J(x)>=0 for every positive normalized x
 iff P(y)>=0 for every y_i>0.                              (H8)
```

Since P is a polynomial matrix, positivity on the positive orthant is equivalent to positivity on the CLOSED nonnegative orthant, by continuity (P(0)=0). This closure statement concerns the polynomial matrix; it does NOT claim that the divided p coordinate chart is invertible at a sparse reference. Returning a uniform positive-interior result to physical sparse matrices would still use the established full physical continuity/range interface, never a boundary inverse or pseudoinverse-continuity assumption.

## 5. Complete integer negative-witness formulation

There is a useful exact consequence of H8:

**The full generic E_full inequality is false if and only if there exist positive INTEGERS y_1,...,y_4 and an INTEGER real eighteen-vector u such that**

```
u^T P(y)u<0.                                              (H9)
```

Proof of the nontrivial direction: a false full sign yields a negative value of the actual joint form at some positive real spectrum and some complex (t,v). P is real, so the complex quadratic is the sum of its real and imaginary parts' real quadratics; at least one real vector is negative. Strict negativity persists on an open neighborhood by continuity of the polynomial entries. Approximate both the positive y and that real vector by rational vectors inside this open neighborhood. Clear their denominators separately. The homogeneity `P(a y)=a^13 P(y)` and quadratic scaling by the positive square of the vector denominator preserve strict negativity. This produces the stated integer witness. There is NO bound on these integers and no enumeration was run.

Conversely an H9 witness is a literal negative full joint value because kappa>0. Its p component cannot be zero, as the raw q pivot A is positive. Minimizing the q component then gives a negative E_full at its nonzero p component. The exact separating spectrum is the rational normalized vector `x_i=y_i/s`, with algebraic Schmidt amplitudes `c_i=sqrt(y_i/s)` and the full p/q tests reconstructed by H7.

This is an exact witness-completeness statement for the ORIGINAL route sign. It does not give an actual witness, a finite exhaustive bound, an admission for a search, or a rank<=2 Werner coefficient operator. A route counterexample would still require a separate physical W4 bridge.

## 6. Eighteen exact symmetric polynomial inequalities, not leading minors

Define integer polynomials C_k(y) by

```
det(t I18+P(y))
 =t^18+C_1(y)t^17+...+C_18(y).                             (H10)
```

Then for every fixed real y,

```
P(y)>=0 iff C_k(y)>=0 for ALL k=1,...,18.                   (H11)
```

Indeed a positive semidefinite matrix has nonnegative eigenvalues, hence nonnegative elementary symmetric functions. Conversely, if all these coefficients are nonnegative, the polynomial in H10 is strictly positive for every t>0 because its leading term is positive. A negative eigenvalue lambda of the real symmetric P would make it vanish at t=-lambda>0, contradiction. Zero eigenvalues cause no problem. This is NOT the incorrect assertion that only the eighteen LEADING principal minors suffice for arbitrary non-strict PSD.

Each C_k has integer coefficients and is homogeneous of degree13k. Relabeling the four Schmidt coordinates simply permutes the twelve ordered-p and six unordered-q coordinates of P. Thus C_k is a SYMMETRIC polynomial in the four y_i. By the fundamental theorem of symmetric polynomials it may equivalently be written in the four elementary symmetric functions, but those variables retain their actual nonnegative-root feasibility constraints.

Alternatively, sort the y_i and set

```
y_1=g_1+g_2+g_3+g_4,
y_2=g_2+g_3+g_4,
y_3=g_3+g_4,
y_4=g_4,
```

with g_i>=0. Every nonnegative spectrum is a permutation of one such point. Thus H8 is exactly the simultaneous nonnegativity of the eighteen substituted integer polynomials C_k(g) on the nonnegative gap orthant. No coefficient array has been generated, and it is NOT claimed that these polynomials have nonnegative monomial coefficients or a sum-of-squares decomposition.

## 7. What is and is not advanced

The new written representation is genuinely inverse-free and faithful to the complete target. It gives either (a) an all-orthant matrix/polynomial proof obligation, with eighteen exact symmetric coefficient signs, or (b) a complete integer separating-witness obligation. It does not choose another reference family, reuse a false certificate, discard compatibility or suppress the full raw correction.

**Still NOT_PROVED:** P(y)>=0 uniformly, equivalently E_full/generic Z_up. No negative integer tuple or separating spectrum is delivered. The other three canonical signs, the full asymmetric co-Choi route and W4 remain NOT_PROVED. The G13 and bare-lift obstructions remain only false-certificate obstructions.

This is a written, unreviewed representation theorem and exact next frontier, not a completed uniform-sign proof or mathematical exhaustion. No finite certificate, computational positivity claim, formal/kernel proof, external review or novelty acceptance follows. Any future coefficient generation, integer search or arithmetic verification requires a separate source/input-pinned named GO under the still-binding HOLD; none is requested or implied by these formulas.
