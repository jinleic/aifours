# A nonempty open shape family defeating the seven-generator span

**Status: WRITTEN candidate with WRITTEN-checked-in-kernel exact boundary evidence; author result, not parent adoption.** There is a nonempty open subset of the feasible nine-parameter five-contact boundary family such that every sufficiently near-boundary strictly stable radial interval box has **no** common SPR numerator in the real span of its four parity endpoints and the first three midpoint derivatives. This is an open-shape obstruction to that seven-dimensional construction, not an unrestricted no-go theorem.

## Boundary conflict

Use the five-contact parameterization and radial boxes of `frontier-20261028-generic-five-contact-span-rigidity-v1.md`. At the explicit strictly feasible shape
\[
(t_1,t_2,t_3,t_4,t_5)=\left(1,\frac32,100,101,2000\right),\quad
u=\frac1{20},\quad v=2001,\quad\alpha=1,\quad\beta=\frac{1001}{1000},
\]
let \(G\) be the seven boundary generators consisting of the four actual parity endpoints and \(Dm,D^2m,D^3m\), where \(m\) is the boundary midpoint. The independent checker verifies \(G\) has rank 7, and the five actual corner/contact tangent rows form a matrix \(T\) of rank 5.

The two-dimensional tangent nullspace has explicit generator-span polynomials \(U,V\), frozen exactly, with leading coefficients \(U_7=1,V_7=0\). For any tangent-nullspace polynomial \(b=yU+xV\), let \(P_1,P_2\) be its pairings with the actual boundary corner \(a_{--}\) at squared frequencies \(1/3\) and \(4093/3\), respectively. The checker computes exact rational coefficients
\[
P_i=A_i y+B_i x,\qquad B_1>0>B_2,\qquad
A_1B_2-A_2B_1>0.
\]
Consequently the positive combination with weights \((-B_2,B_1)\) is
\[
(-B_2)P_1+B_1P_2=-(A_1B_2-A_2B_1)y.
\]
If \(y>0\), this is strictly negative, so both pairings cannot be nonnegative. If \(y=0\), their nonnegativity forces \(x=0\), hence \(b=0\). Thus no **nonzero** boundary-span polynomial with nonnegative leading coefficient can satisfy the five tangencies and both nonnegative pairings.

## Near-boundary and open-shape conclusion

Suppose a sequence of strictly stable radial boxes of this shape had common numerators in their own seven-generator spans with \(\rho_n\uparrow1\). Normalize their coefficient norms to one by positive scalars and pass to a convergent subsequence. The leading coefficients of equal-degree common numerators are positive, so the limit has nonnegative leading coefficient. Rank 7 of the boundary generators implies bounded generator coordinates and places the nonzero limit in the boundary span. Continuity gives nonnegative boundary pairings. At each positive-frequency contact the actual boundary denominator vanishes, so its nonnegative pairing has zero derivative. Hence the limit lies in \(\ker T\), contradicting the two-row argument. Therefore some \(\rho_0<1\) excludes the seven-generator span for all \(\rho_0<\rho<1\). The alternating marker signs prove these radial boxes strictly Hurwitz.

Rank, leading-coordinate normalization, and the three strict two-row signs are continuous in the shape parameters. They therefore persist on a nonempty open neighborhood of the displayed shape in the feasible nine-parameter domain; the same compactness argument applies shape by shape. No density claim is made. The companion `frontier-20261029-seven-dimensional-span-obstruction-open-v1.md` supplies an **actual** \(\rho=1-10^{-8}\) box, an independent eight-positive-atom annihilator, and a separately verified unrestricted common numerator. The present generic-shape argument does not claim unrestricted synthesis for every nearby shape.

Frozen exact boundary generators, nullspace vectors, rank minors and pairings: `frontier-20261029-seven-dimensional-boundary-conflict-frozen-v1.json`, SHA-256 `a7bb7609a5fdfe05a8821363e8f6a498b286c3068759fcd77f24466760a8afa5`. Independent factor, monomial-derivative and determinant checker `frontier-20261029-seven-dimensional-boundary-conflict-independent-kernel-v1.py`, SHA-256 `cda68521a63c56eb06c5b2fb6b790fe2f36c2176064dc52b7498a7e3ea9fcfe8`; receipt `frontier-20261029-seven-dimensional-boundary-conflict-independent-result-v1.json`, SHA-256 `86d54ea79c451d070d0507c439b2cace4d237fc2d732f08869d61d130d7cca65`. The actual-box companion is SHA-256 `5693a3a172c2d696471718084a755d4ce984cc3edf2fc1946b6e38ee1f9f561f`.

Finite identities use exact integers and `fractions.Fraction` on one Python Eval host. Compactness, continuity and sign-band stability are written mathematics. No formal proof, cross-vendor review, novelty clearance, arbitrary-box verdict, or all-numerator negative certificate is claimed.
