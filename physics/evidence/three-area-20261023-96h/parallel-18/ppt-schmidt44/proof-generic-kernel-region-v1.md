# A simultaneous mixed-kernel region still has Schmidt number at most two

Observed immediately before freezing: **2026-10-23T14:50:10-07:00**. Author PhysicsPPT44, physics-3. **CANDIDATE — complete written argument; separate reconstruction and parent acceptance pending.** No scientific executable, finite numerical check, solver or formal kernel was used.

This addresses the slot's actual remaining generic-kernel mechanism. It excludes a full multi-parameter region, **not all filters, all PPT states, or P44**. It is not another one-point compression paper or a claimed discovery.

## 1. Exact family and achieved quantifiers

In `C^4_A tensor C^4_B`, write `P(y)=|y><y|` for an unnormalized vector, and let

`a=00+11+22`, `b=01+12`, `c=10-21`,
`e=20+33`, `f=30`, `g=32`, `j=23`.

For an arbitrary complex vector `x=(x0,x1,x2,x3)`, set

`d_x=02+|3> tensor x`, `h_x=|0> tensor x`,

`R_x=P(a)+P(b)+P(c)+3P(d_x)+3P(e)`
`       +3P(f)+3P(g)+3P(j)+3P(h_x)`.

Its trace is `25+6||x||^2>0`; define `rho_x=R_x/(25+6||x||^2)`.

This is the exact local-filter image of the already frozen Krebs–Gachechiladze4by5 input R45 under

`B_x|r>=|r>` for r=0,1,2,3, and `B_x|4>=x`.

Thus positivity/PPT are inherited by local congruence. This chart covers all rank4 Bob filters whose first four column images are linearly independent, up to an invertible output filter; it does not cover every chart by itself. Provenance is Theorem5/Fig.1/Eqs.(10)–(11) of [2509.07086v1](https://arxiv.org/html/2509.07086v1), captured raw SHA-256 `115f3102fc7f3c9be9992cbb130633da40d729b6f3c353338de0153770ea5070`.

**Theorem.** For **every complex** x satisfying

`L:=|x0|+|x1|+|x2| <= 1/3`,
`|x3|^2 <= 8/3`,                                                    (R)

one has `SN(rho_x)<=2`. Consequently no universally two-block-positive W can have `Tr(W rho_x)<0` on this region.

The theorem permits all four coordinates to be simultaneously nonzero. For example `x=(1/12,1/12,1/12,1)` is strictly inside (R). The initially proposed exploratory input `x=(1,1,1,1)` is **not covered**, since its L equals3. No conclusion about that state is inferred.

## 2. Explicit Schmidt-rank-two family

Let z,w range independently over the complex unit circle, each with normalized uniform angular measure. Define

`D(z,w)=z^2(w+x2)+z*x1-x0`,
`J(w)=x3/(w+x2)`.

Under (R), uniformly in z,w,

`|w+x2|>=1-|x2|>=2/3`,
`|D(z,w)|>=1-(|x0|+|x1|+|x2|)>=2/3`.                               (1)

No denominator below vanishes. Put

`psi(z,w)=a+z*c+(w/D)d_x+w*f+(w^2/D)g+(1/D)h_x+J(w)j`.             (2)

Its coefficient-matrix rows are

```
r0 = (1+x0/D, x1/D, (w+x2)/D, x3/D),
r1 = (z,      1,        0,        0),
r2 = (0,     -z,        1,     J(w)),
r3 = (w+x0*w/D, x1*w/D, w*(w+x2)/D, x3*w/D).
```

They satisfy the exact identities

`r0 = [(z(w+x2)+x1)/D] r1 + [(w+x2)/D] r2`,
`r3 = w*r0`.                                                       (3)

For the first coordinate in the first identity use

`z[z(w+x2)+x1]=D+x0`;

for the final coordinate use `(w+x2)J(w)=x3`. The other coordinates are immediate. Hence every matrix in (2) has rank at most two, for arbitrary complex x obeying (1), not merely real parameters.

## 3. Exact orthogonality of the coefficient groups

All averages below are exact circle integrals, not finite-point testing. They follow from uniformly convergent geometric series and the identity that the angular average of a nonconstant integer character is zero.

For fixed w, the expansion

`1/D = [z^(-2)/(w+x2)]`
`       * sum_{n>=0} [-(z*x1-x0)/(z^2(w+x2))]^n`                    (4)

converges uniformly on the two-torus. Indeed

`|(z*x1-x0)/(z^2(w+x2))|`
` <= (|x1|+|x0|)/(1-|x2|) <= 1/2 <1`.

Every z-exponent in (4) is strictly negative, at most minus2. Therefore, for each w, the three coefficients

`q=(q_h,q_d,q_g)=(1/D,w/D,w^2/D)`                                  (5)

have zero z-average, and their inner products with the coefficient z also average to zero. They are likewise orthogonal in the joint average to the coefficients1,w,J(w), since the latter do not depend on z.

The remaining coefficients1,z,w,J(w) are pairwise orthogonal in average. The only non-immediate pair is w versus J(w). Since |x2|<1,

`J(w)=x3 sum_{n>=0}(-x2)^n w^(-n-1)`.

It has zero mean; and

`w*conj(J(w))=conj(x3)*w^2/(1+conj(x2)*w)`

also has zero mean. Independence of z handles pairs containing z. Finally

`E |J(w)|^2 = |x3|^2/(1-|x2|^2) =: m`,

by summing the squared orthogonal Fourier coefficients. Condition (R) implies

`m <= (8/3)/(1-1/9)=3`.                                           (6)

No claim of orthogonality **within** the three corner coefficients q is needed.

## 4. Matrix bound for the corner covariance

Let F be the16by3 matrix with columns `(h_x,d_x,g)`, and put

`K=E[q q^*]`.

Every column of F is supported on Alice's two-dimensional subspace `span{|0>,|3>}`. Thus every positive operator of the form `F M F^*` has Schmidt number at most two whenever M>=0.

For arbitrary eta in C3, (1) and orthogonality of `1,w,w^2` give

`eta^* K eta`
` = E |conj(eta_h)+conj(eta_d)w+conj(eta_g)w^2|^2 / |D|^2`
` <= (9/4) E_w |conj(eta_h)+conj(eta_d)w+conj(eta_g)w^2|^2`
` = (9/4)||eta||^2`.

Hence

`0<=K<=(9/4)I3`, and `3I3-K>=(3/4)I3>=0`.                         (7)

The bound does not require evaluating the entries of K, assuming an unproved independence, or asserting a polynomial identity from samples.

## 5. Positive decomposition of the whole state

Let

`A=E P(psi(z,w))`.

Section3 removes exactly the off-diagonal groups needed for

`A=P(a)+P(c)+P(f)+m P(j)+F K F^*`.                                 (8)

Subtracting (8) from the defining state gives the exact identity

`R_x = A + P(b)+3P(e)+2P(f)+(3-m)P(j)+F(3I3-K)F^*`.                 (9)

Every residual term is positive and has Schmidt number at most two:

- b and e each have two product terms;
- f and j are product vectors;
- `3-m>=0` by (6);
- the final positive term is supported on only two Alice dimensions by Section4.

The average A also has Schmidt number at most two because every explicitly specified vector (2) has Schmidt rank at most two. For completeness, the continuous average causes no closure gap: (1) uniformly bounds the vector norms, so Riemann sums converge to A; the normalized rank-at-most-two projector set is compact, and its convex hull is compact in the finite-dimensional trace-one Hermitian space. Thus the Schmidt-number-two cone is closed at the finite-trace operator A. Equivalently, finite-dimensional Caratheodory converts the normalized average to a finite convex decomposition with at most256 pure terms. This is an existence implication of a classical theorem, not an explicit table of256 numerical vectors or a scientific enumeration.

Dividing (9) by the positive trace proves the theorem. Linearity then forbids a negative expectation for every two-block-positive W.

## 6. Why this is genuine generic-kernel coverage, and its limit

The earlier auxiliary-only and coordinate-core merging proofs did not permit simultaneous generic x0,x1,x2 components. Here all coordinates may vary complexly and simultaneously within the explicit region (R). The rank-two family (2) adapts to all of them through one denominator, while (7) absorbs the non-diagonal corner covariance in a positive two-Alice-dimensional block. Treating that covariance as diagonal would have been unjustified; it is bounded as a matrix instead.

This is still only a **sufficient SN2 region of a restricted construction family**. It does not settle the high-mixing residual, every4by5-to4by4 filter, or every4by4 PPT state. The constants1/3 and8/3 are conservative sufficient values, not claimed optimal. Positivity/PPT of the family alone is not evidence of SN3 anywhere outside (R).

The source's local-extension input is an existing baseline. The analytic ingredients here are elementary coefficient-matrix rank, Fourier orthogonality, a covariance norm estimate, and finite-dimensional cone closure. No priority claim is made; this packet has not undergone literature-wide comparison or separate reconstruction. Correctness, scope, source trust, novelty and significance remain distinct.

### Verification state

- Complete author-written symbolic/analytic proof; **CANDIDATE**.
- No scientific execution, Python arithmetic, finite phase replay, solver, formal kernel, modelCLI or human review.
- Parent and a distinct in-harness reconstruction of these pinned bytes remain required before promotion.
- The all-finite-N bare-Bose-lift obstruction is a different, coherent witness-method barrier, not a substitute for this state-family argument or for unrestricted P44.
