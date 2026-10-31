# The odd-q 4+4+2 transversal pattern is impossible

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 20:43:45 PDT 2026**. This is an additive successor to `frontier-20261028-odd105-quotient-classes-v1.md` SHA **334ad2097c9d11b66fcac1b6843f85591dfdd45d6af8c72cbe8394ebf05eb643**. It imports its Lam–Leung low-weight classification and the named universal q5 no-transversal certificate; all other steps here are elementary written linear algebra. No prior file was altered.

## Claim

For odd q with 5|q, a Fourier-product QLS10 transversal CANNOT have LOW column-class partition `4+4+2`. Consequently, under the named imports, the only unexcluded class-size patterns are

```text
4+2+2+2    or    2+2+2+2+2.
```

Together with the earlier odd-q filter this concerns the remaining odd multiples of105. It is not a no-go for those two residual patterns or for the original arbitrary 1-RQLS10.

## 1. Quotient and half-graph setup

Assume a transversal and 4+4+2 classes. The earlier packet proves every size4 class has a nonconstant quotient profile with a common 5/5 coordinate support, and all size4 supports agree up to complement: call them S and S^c. It also proves that every row quotient with one row in S and one in S^c is HIGH: at least9 distinct mu_q/mu5 values, hence at most one repetition among ten entries.

Within a size4 column class, the quotient pattern of any S/S^c row pair lists that class's four quotient-profile values, up to a common factor. At most one of the two size4 classes can have a repeated profile, and any repetition is exactly one double. Consequently, one size4 class B has four DISTINCT profiles, while the other class A has either four distinct profiles or exactly one double plus two singleton profiles. Let the size2 class be C.

Any two distinct B columns have their two G-quotient values on S and S^c, five terms on each. A five-term zero sum at odd q must be one regular5-gon, hence occupy one G coset. Therefore any zero five-half for a B pair is exactly S or S^c. The physical transversal induces a perfect matching on the zero half graph. Matching occurs only inside LOW classes, so at least one B edge is present and the matching half E equals S or S^c. The two columns of C must match each other. Taking S as the chosen half, B's four columns are pairwise orthogonal there, and C's two columns are orthogonal there.

Every cross-class column pair is HIGH, hence has at most two terms in any G coset and NO zero five-term half. In particular, **every A–C half inner product on S is nonzero**. Within A, a singleton-profile column is orthogonal on S to all other three A columns, by the LOW two-pentagon decomposition. At least one such singleton exists.

## 2. A five-dimensional frame obstruction

Restrict K to S and divide each column by sqrt(5). Write the resulting 5×4, 5×4 and 5×2 blocks as A,B,C. Every column is a flat unit vector. The B and C columns are orthonormal within their own blocks, and K row orthogonality gives

`A A† + B B† + C C† = 2 I_5`.                                      (1)

Let b be a unit normal to the four B columns, and let P_C=C C†. Then `B B†=I-bb†`, so

`A A† = I + bb† - P_C`.                                              (2)

Let a0 be a singleton-profile A column. It is orthogonal to the other three A columns, so `A A† a0=a0`. Equation (2) gives

`b (b†a0) = P_C a0`.

If b is not in col(C), the two sides lie in subspaces with trivial intersection; both vanish. Then a0 is orthogonal to both C columns, contradicting the required nonzero A–C half inner products. Thus b lies in col(C). As C is an orthonormal 2-frame, `P_C-bb†` is a rank-one orthogonal projector. Equation (2) makes `A A†` a rank-four orthogonal projector. Since A has four columns, their Gram matrix A†A has four eigenvalues1: **A's four columns are orthonormal**.

Now let a be a unit normal to A. Equation (1) becomes `P_C=aa†+bb†`. Since P_C is a rank-two orthogonal projector and a,b are unit, a and b are orthogonal; C spans their two-plane. The diagonal of `I-aa†=AA†` is4/5 because A's four columns are flat, so a is flat; similarly b is flat.

**Flat two-plane lemma.** If a,b are flat orthonormal vectors in C^5, any flat vector in span{a,b} is proportional to a or b. Indeed let `x_t=b_t/a_t`; all |x_t|=1, and orthogonality says `sum_t x_t=0`. The five x_t cannot have only one or two distinct values, because an odd number of unit vectors taking at most two values cannot sum to zero. For a flat `u=alpha*a+beta*b`, the values `Re(conj(alpha)*beta*x_t)` must be constant. A line intersects the unit circle in at most two points, so at least three distinct x_t force `conj(alpha)*beta=0`.

Both C columns are flat and form an orthonormal basis of span{a,b}; one is therefore proportional to a. It is orthogonal to every A column, again contradicting the nonzero A–C half inner products. Hence 4+4+2 is impossible.

## 3. Scope and evidence boundary

All five-dimensional frame and flat-two-plane steps are written, not a formal kernel proof. The implication from a transversal to the half graph, the LOW/HIGH quotient profile dichotomy, support classification, and the imported q5 no-T base require independent full review as named in the predecessor. This eliminates one of three previously admissible class patterns and leaves two, with no claim that either occurs, is resolvable, or exhausts non-Fourier QLS10.
