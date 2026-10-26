# Six defects are impossible at full polar rank

Observed before creation: **2026-10-23T14:25:59-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN PROOF**, with no independent reconstruction, scientific execution, kernel acceptance or novelty clearance.

This is the same unrestricted balanced242 problem. In combination with the earlier sparse-defect and four/five-defect candidates, it gives **a>=7 for both surviving rank-eight types**. It does not exclude either entire type or solve the balanced maximum. The rank2/4/6 types retain the earlier candidate a>=4 only.

## 1. Common reconstruction and the correction on an affine span

Use the full-rank decomposition proved in `four-five-defect-rank8-proof-v1.md` (SHA256 `f6f1dc1f16d322025307cb748fa973522d8fe55af2503c2e98f1aa7fff744aa3`). Here `chi=(-1)^D`, D has nonsingular polar form B, A is the signed defect support, delta has values±1 on A and0 outside, and

`S=F+C`,

`F(y)=(-1)^k 2^(5-k) sum_{|I| even}(-3)^(|I|/2) epsilon_I chi(y+u_I)`,

`C(y)=(-1)^(k+1)2^(9-k) sum_{|I| odd}(-3)^((|I|-1)/2) epsilon_I 1_{y=u_I}`.     (1)

Let `L=u_0+K` be the affine span of A, dimension d. The ratio F/chi is constant on cosets of `K-perp_B`; C is supported in L. Outside L, S=F has magnitude20 or28. Therefore, if `K-perp_B` is not contained in K, no such fiber lies wholly in L and `|F|<=28` everywhere. This also holds whenever d<=3 by fiber cardinality.

There is a second exact formula useful for collisions:

`C=H_8 phi(H_8 delta)`.                                   (2)

To see it, write z=H_8 delta and `Q=W_D/16 in {±1}`. The sine addition formula gives

`phi(Q-z)=Q cos(2 pi z/3)+(1/2)phi(z)`;

then apply `S=2H_8 phi(Q-z)`. The first term is exactly F from (1), and the second is (2).

Choose coordinates on K. If `r(v)=delta(u_0+v)`, with v in F_2^d, the affine support factor and character orthogonality yield

`C(u_0+v)=2^(8-d) H_d phi(H_d r)(v)`,                    (3)

and C=0 outside L. This follows because `H_8 delta` is an affine character times the lift of `H_d r`, and phi is odd. No enumeration is used.

## 2. Affine dimension3

Six distinct points cannot have affine dimension below3. At d=3, F has magnitude<=28 everywhere. At a defect, `|C|<=|S|+|F|<=12+28=40`; at another point, `|C|<=56`. Equation (3) makes all C values multiples of32. Thus all have absolute value<=32.

Put `b=phi(H_3 r) in {0,±1}`. Then `H_3 b` has every entry in `{0,±1}`. Parseval gives

`8 sum b^2 = sum (H_3 b)^2 <=8`,

so b has support at most1. It cannot be zero: H_3 is invertible modulo3 and r is nonzero modulo3. If b has support1, its transform is nonzero modulo3 at every one of the eight coordinates. But

`H_3 b = H_3^2 r =8r (mod3)`,

which would force r to have support all8 points, not6. Contradiction.

The same argument shows a broader auxiliary fact: a proper nonempty defect subset of an affine three-flat cannot occur when the F-fiber argument applies.

## 3. A six-point ternary-Hadamard table on a four-space

At d=4, write `r:F_2^4 -> {0,±1}` with six support points of affine span4, and put

`J(r)=H_4 phi(H_4 r)`.

The five-dimensional space of even subsets of the six points maps onto their four-dimensional direction space. Its one-dimensional kernel has a unique nonempty relation P, of size4 or6. Put `e=product_{u in P}r(u)`.

The following table holds **at the support points**:

| relation | sign e | J(r) on P | J(r) on A outside P |
|---|---|---|---|
| size6 | +1 | `-5r` | none |
| size6 | -1 | `4r` | none |
| size4 | +1 | `r` | `-5r` |
| size4 | -1 | `-2r` | `4r` |

Here the size4 relation is an affine plane. The proof is written below; the table is not imported from a finite run.

### Proof of the table

The operation J commutes with invertible affine input changes and with multiplication by an affine sign character, since H turns translations/modulations into modulations/translations and phi is odd. Affine sign characters on six affinely spanning points have restriction rank5, and their unique binary restriction relation is P. Therefore e=+1 is precisely the case in which the signs can be normalized to all+1; e=-1 is the other sign coset.

**Size6, e=+1.** The product of the six signed character summands of H_4 r is+1. Its values are therefore±6 or±2. Affine spanning permits exactly one coefficient of magnitude6, say `6sigma` at x_0; the others have magnitude2. Hence

`phi(H_4 r)=-(H_4 r)/2+3sigma 1_{x_0}`,

`J(r)=-8r+3sigma(-1)^(x_0.v)`.

At every support point, alignment at x_0 gives `r(v)=sigma(-1)^(x_0.v)`, so J=-5r there. This formula also describes J off the support.

**Size6, e=-1.** The six summands have negative product, so H_4 r takes only0,±4. Thus `phi(H_4 r)=(H_4 r)/4`, and J=4r everywhere.

**Size4, e=+1.** Normalize r to the indicator of

`{0,e_1,e_2,e_1+e_2,e_3,e_4}`,

with P the first four points. Its transform is

`z(x)=(1+(-1)^x_1)(1+(-1)^x_2)+(-1)^x_3+(-1)^x_4`.

The exceptional coefficients to the rule phi(z)=-z/2 are z=6 at0 and z=4 at e_3,e_4. Consequently

`J(r)=-8r+3[1+(-1)^v_3+(-1)^v_4]`.

It equals r on P and -5r at the other two support points. Equivariance restores all sign patterns with e=+1.

**Size4, e=-1.** No transform coefficient can have magnitude6 because all six summands aligning would give positive product on P. Thus z=H_4 r belongs to0,±2,±4, on which

`phi(z)=(z^3-12z)/16`.

The product/convolution identity gives

`J(r)=r*r*r-12r=4r+6 sum_{I:|I|=3}r_I 1_{u_I}`,

where * is ordinary unnormalized group convolution. In r*r*r the repeated-index terms contribute `(1+3(6-1))r=16r`, and each distinct unordered triple has six orders. At a point j in P there is exactly one coincident triple, P minus j, whose sign is `e r(j)=-r(j)`. At either other support point there is no coincident triple; another one would give a second even relation. This gives -2r on P and4r elsewhere.

All table cases are now proved.

## 4. Affine dimension4, not Lagrangian

If K is not Lagrangian, `K-perp_B` is not contained in K (both have dimension4), so `|F|<=28` everywhere. At each of the six defects, equation (3) then requires

`16 |J(r)|=|C|<=40`, hence `|J(r)|<=2`.

Every row of the table has a support point where |J| is4 or5. This is impossible.

## 5. Affine dimension4, Lagrangian

Now `K=K-perp_B`. The ratio F/chi is a common constant c on L, and D restricts affinely to L. Define the gauged signed support

`r(v)=chi(u_0+v) delta(u_0+v)`.

Because this multiplication is an affine sign character on L, equation (3) and equivariance give

`T(u_0+v)=chi S=c+16J(r)(v)`.

At each defect the *definition* of its sign fixes the small value exactly:

`T=-4-8r` (r=+1 means T=-12; r=-1 means T=4).              (4)

Apply the table to r:

- Size6,e=-1: equation (4) with J=4r forces `c=-4-72r` at all six points. Hence all six r would be equal, contradicting their product e=-1.
- Size4,e=-1: on the four-point relation, J=-2r forces `c=-4+24r`. Again all four signs must agree, whose product is+1, contradicting e=-1.
- Size4,e=+1: on P, J=r forces `c=-4-24r`, so c is20 or-28. At the other two points, J=-5r would force `c=-4+72r`, one of68 or-76. The sets are disjoint.
- Size6,e=+1: J=-5r forces `c=-4+72r`. If the support signs are mixed this is impossible. If they are all a common sign r_0, the aligning affine character in the proof of the table is constant r_0 on all of L, since the support affinely spans L. Off the support the same formula makes J=3r_0. Then `T=c+48r_0=-4+120r_0`, equal to116 or-124, not20 or-28 as required there.

This eliminates every Lagrangian dimension4 case.

## 6. Affine dimension5

Six points with affine dimension5 have distinct odd-subset sums, all32 of them. At a five-subset sum outside A, equation (1) gives the unique correction±72.

If `K-perp_B` is not contained in K, all fibers meet the outside of L, so `|F|<=28` everywhere. The five-subset sum then gives `|S|>=72-28=44`, impossible.

It remains that K is coisotropic: `R=K-perp_B` is a three-space contained in K. On L the ratio F/chi is constant on each R-coset. Those four fibers are indexed by the affine quotient `L/R`, of dimension2; call their constants c_v.

At a singleton defect u_i the correction is exactly `-8epsilon_i`. With `r_i=chi(u_i)epsilon_i`, equation (4) therefore gives

`c_{v_i}-8r_i=-4-8r_i`, hence `c_{v_i}=-4`.                (5)

Let `U=sum_{i=1}^6 u_i`, an even-subset sum and thus an element of K. The six five-subset points are u_i+U. They are outside A and have correction±72, so their corresponding constants belong to

`{-28+72,-28-72,20+72,20-72}={44,-100,92,-52}`,

none equal to-4.

Consequently, if `P={v_i}` is the set of singleton fiber labels and v_U is the quotient image of U, the equal-sized sets P and `P+v_U` must be disjoint. But the six points affinely span L, so their images affinely span the two-dimensional quotient: |P|>=3. Two subsets of size at least3 cannot be disjoint in a four-element quotient. Contradiction.

This exhausts affine dimensions3,4,5 and proves that exactly six defects are impossible at polar rank8.

## 7. Actual boundary

Combining the three pinned candidate proofs gives a>=7 in either full-rank type. No execution, old solver restart or finite-certificate replay has occurred. The method still does not exclude a>=7 or solve the original target. In particular, seven affinely independent defects can span a six-space whose coisotropic fibers number16; the singleton/five-subset disjoint-translate pigeonhole used above is no longer automatic. At lower affine dimensions new even-relation kernels and signed-support collisions must be treated. Those are genuinely new mathematical cases, not justification for treating partial coverage as global.

This is an immutable written snapshot. Correctness awaits actual separate reconstruction and parent checking. Novelty, formal proof and significance are unestablished; the best demonstrated balanced value remains240.
