# f355 — Frozen WRITTEN proof review

**Delivery:** Complete review body for parent materialization as `review-v1.md` in the assigned f355 wave. No repository file was created by this reviewer.

**overall_correctness: correct**

**explanation:** The universal actual-box equivalence, complete finite-grid odd-moment ray classification, and conditional six-frequency sparsification are supported by the written reconstruction below, using the frozen imports at their stated scopes. This verdict does **not** certify the finite arithmetic of the author’s supplied example, establish condition B for every eligible box, produce a strict-negative certificate, or construct a common strict SPR numerator.

**confidence: 0.97**

**New findings at the assigned written-proof scope: FATAL 0 / MAJOR 0 / MINOR 0.**  
There are no merge-blocking mathematical findings in that scope. The example’s finite assertions remain **INCONCLUSIVE in this review**, not refuted.

## 1. Frozen inputs and review boundary

References below use the **f355 packet’s source labels**, not the author’s earlier wave-local labels:

- **S1:** f347 candidate, SHA-256  
  `bf4af736bc4e85355cd5682ecc14ee2f00ed39f8d8d440f724bfa601f3ee7353`; complete logical lines 1–923.
- **S2:** adopted corrected six-positive-frequency lower-bound disposition, SHA-256  
  `a4f1f48c3521a8b4a5635aa861f9a5afbb9d6f6e5ea7ead79d8183be5308788b`; lines 1–34.
- **S3:** complete corrected written proof supplying the original-model and interlacing interfaces, SHA-256  
  `7bd4c0442b424f6ef01df332df5865661e7a9872e3719723553c87f21b2ea96d`; complete logical lines 1–709.

Frozen bindings:

- Manifest: `eb31496a0a745e620e839909688d4ce242e724e06732a3ebba6bbcf8eccac63d`
- Receipt: `5b9f3e62b29a43178b6ea7633d18526acb96855659f8a1ed29aa352e9229f921`
- Packet: `c0b358ec22e883a77bb57cf8deaeddf82525e6c4664659f544c6d4f0d27e2290`

The following are the only substantive imported interfaces used:

1. Strict Hurwitzness gives positive actual coefficients and the stated strict Hermite–Biehler parity interlacing.
2. Coefficient independence makes every even-/odd-envelope combination an actual member.
3. The corrected box-wide odd-root ordering and actual-even-root placements have the scope stated in S2 LF 14 and S3 LF 123–136, 164–170.
4. **Only for the six-frequency sparsification:** S2 LF 7’s adopted impossibility of a strict-negative certificate on at most five distinct positive squared frequencies, with arbitrary actual members and optional endpoint atoms.
5. Finite-dimensional convex separation and extreme-ray generation of pointed polyhedral cones.

No historical defective manuscript, finite K1/K2 computation, normalized W1 vertex result, held output, sibling return, or f356 result is a premise.

## 2. Per-claim disposition

| Claim | Disposition | Source lines |
|---|---|---|
| Raw pairing, eight-coordinate row and two signed moment vectors | **SUPPORTED** | S1 LF 20–89 |
| Compactified endpoint contributions can be removed from a strict-negative aggregate | **SUPPORTED** | S1 LF 91, 401–415; S3 LF 100 |
| Exact four-corner convexification of the row image at one fixed frequency | **SUPPORTED** | S1 LF 106–153 |
| Strict odd-band widths under nonzero odd coefficient width; strict actual-even placements | **SUPPORTED** | S1 LF 155–176; S3 LF 123–136, 164–170 |
| The cone variables are nonnegative atom weights | **SUPPORTED** | S1 LF 180–195 |
| Z singleton and P same-frequency cancellation rays | **SUPPORTED** | S1 LF 197–220, 289–296 |
| R4 formulas, positive weights and signed moment vector \(-e_k\) | **SUPPORTED** | S1 LF 222–249, 314–321 |
| Both R5 orientations and their positive annihilator weights | **SUPPORTED** | S1 LF 251–285, 323–329 |
| Completeness of Z/P/R4/R5, including the support bound and cubic separator | **SUPPORTED** | S1 LF 287–331 |
| Separation from the **open** negative orthant produces a nonzero coefficientwise nonnegative test vector | **SUPPORTED** | S1 LF 399–445 |
| The even test cannot vanish identically | **SUPPORTED** | S1 LF 447–453 |
| Band signs force a common cubic with roots in the asserted closed root box | **SUPPORTED** | S1 LF 455–497 |
| Piecewise \(E_F\) is the correct actual minimizing even envelope | **SUPPORTED** | S1 LF 335–370, 501–503, 521–534 |
| Exact quantified equivalence A iff B | **SUPPORTED** | S1 LF 372–395, 397–536 |
| An individual odd-moment ray is not an all-eight-strict-negative certificate; the lower bound does not prove arbitrary scalar ray inequalities | **SUPPORTED** | S1 LF 540–556 |
| Same-six-frequency, same-aggregate, at-most-eight-corner-atom sparsification; at least four pure groups after merging | **SUPPORTED** | S1 LF 580–612; imported S2 LF 7 |
| Supplied physical example’s exact parameters, finite substitutions, aggregate signs and finite W1-only falsification | **INCONCLUSIVE in this review’s finite-verification boundary** | S1 LF 616–830 |
| Universal fixed-even and fixed-odd class obstructions | **SUPPORTED** | S1 LF 832–844 |
| Every eligible box satisfies B; a strict-negative witness exists; or common strict SPR synthesis follows | **NOT PROVED**, correctly excluded by the candidate | S1 LF 848–874 |
| Author’s historical execution/read/process assertions | **Not independently certified here** | S1 LF 878–923 |

**REFUTED claims at the assigned universal written-proof scope: none.**

The historical six MAJOR findings discussed in S2/S3 concern the earlier manuscript. They are not new findings against this candidate.

## 3. Actual fixed-frequency corner convexification

### 3.1 Pairing and weight convention

For \(t=\omega^2>0\),

\[
a(i\omega)=E_a(t)+i\omega O_a(t),
\]

and the numerator pairing is

\[
\operatorname{Re}\bigl(b(i\omega)\overline{a(i\omega)}\bigr)
 =B_e(t)E_a(t)+tB_o(t)O_a(t).
\]

Thus S1 LF 65–69’s raw row is correct:

\[
r(a,t)=
\bigl(E_a,tO_a,-tE_a,-t^2O_a,
      t^2E_a,t^3O_a,-t^3E_a,-t^4O_a\bigr).
\]

In particular, the odd signed moments contain \(t^{r+1}O_a(t)\), not \(t^rO_a(t)\). This is why the ray weights below contain the factor \(u_i\) in their denominators.

All cone variables and certificate variables are **weights**, not the signed quantities \(w_it_iO_i\). Zero coefficients in a decomposition may be omitted; all retained certificate atoms then have positive weights.

### 3.2 Exact row image, not a four-polynomial coefficient hull

At a fixed positive \(t\), the even coefficient group has image exactly

\[
[E_-(t),E_+(t)],
\]

and the independent odd coefficient group has image exactly

\[
[O_-(t),O_+(t)].
\]

Independence makes their joint image the complete rectangle

\[
[E_-(t),E_+(t)]\times[O_-(t),O_+(t)].
\]

Every rectangle corner comes from the stated **actual coefficient-box polynomial** \(a^{\sigma\tau}\). Since the raw row is linear in the two displayed parity values, its image is exactly the convex hull of the four corner rows.

This proves S1 LF 142 without asserting that the whole coefficient box is the convex hull of four polynomials. The convex weights may depend on \(t\); the corner polynomials themselves are actual fixed members of the original box.

Degenerate even intervals cause no problem. If the even interval image collapses, the rectangle and its corner list simply have duplicates. No division by an even width is required.

### 3.3 Odd bands and actual even signs

If at least one odd coefficient interval has positive width, then

\[
O_+(t)-O_-(t)
=(u_1-\ell_1)+(u_3-\ell_3)t+(u_5-\ell_5)t^2>0
\]

for every \(t>0\).

The corrected interlacing import first gives the non-strict paired root bounds and strict gaps between the bands. A common positive root of \(O_-\) and \(O_+\) would make the displayed difference zero. Consequently all three paired widths are strict, yielding

\[
0<a<b<c<d<e<f.
\]

Every actual even polynomial has its roots strictly in

\[
(0,a),\qquad(b,c),\qquad(d,e).
\]

Its leading multiplier in the product of \((\rho_j-t)\) factors is positive. Hence every actual even polynomial is:

- strictly negative on \([a,b]\);
- strictly positive on \([c,d]\);
- strictly negative on \([e,f]\).

These statements include the band endpoints because the actual even roots lie in the intervening **open** gaps. No arbitrary-marker realization assumption is used.

## 4. Complete finite-grid odd-moment cone

Fix finite \(T\subset(0,\infty)\). Write

\[
M_r^o(w)=
\sum_{t,\tau}w_{t,\tau}(-1)^rt^{r+1}O_\tau(t),
\qquad r=0,1,2,3.
\]

The cone is

\[
\mathcal C_T=\{w\ge0:M_r^o(w)\le0\text{ for all }r\}.
\]

It is polyhedral and pointed because it lies in the nonnegative weight orthant.

### 4.1 Zero values and repeated frequencies

A zero-odd atom contributes zero to every odd constraint. Its singleton weight is an extreme ray **Z**. A feasible vector containing that atom and any other positive weight splits off a nonzero Z component, so it is not a new extreme ray.

For two nonzero endpoint atoms at one frequency:

- With the same odd sign, a sufficiently small redistribution in both directions preserves all four odd moments and nonnegative weights. This precludes extremality.
- With opposite signs, the positive cancellation vector is

  \[
  (w_-,w_+)=(O_+,-O_-).
  \]

  Subtracting a maximal feasible positive multiple leaves at least one of these two coordinates zero and preserves the odd moments. Except when the whole vector is proportional to this cancellation vector, that is a nontrivial decomposition.

Thus **P** is retained, and every other extreme ray uses distinct frequencies with nonzero odd values.

This treatment neither assumes that finite weights imply nonzero parity nor requires a generic perturbation.

### 4.2 Active-constraint dimension and the small-support exclusion

On an extreme ray’s positive support of size \(p\), the active odd equations must have nullity one. There are at most four independent such equations, so \(p\le5\).

For distinct nodes with nonzero odd values, put

\[
z_i=w_iu_iO_i.
\]

If \(p\le3\), a cubic

\[
Q(t)=\prod_{j=1}^{3}(r_j-t),\qquad r_j>0,
\]

can agree in sign with every \(z_i\): put roots in the sign-change gaps, and place any remaining roots before the first node or after the last node with the required parity. Positivity of the first node leaves room for roots before it.

The coefficient magnitudes of \(Q\) are all strictly positive and alternate in sign. Therefore

\[
\sum_i z_iQ(u_i)
\]

is a positive-coefficient combination of the four nonpositive signed moments, hence is nonpositive. On the other hand, every summand is strictly positive. This is a contradiction.

The proof applies to **non-strict** odd moment constraints, as required for the cone.

### 4.3 R4 normalization

On four distinct nodes, all four moments cannot vanish because the corresponding Vandermonde matrix is invertible. Extremality therefore requires exactly three active moments.

Let the omitted moment be \(k\), and set

\[
H_4(t)=\prod_{i=1}^4(t-u_i),\qquad
q_i=e_{3-k}(\widehat u_i).
\]

The coefficient of \(t^k\) in the Lagrange basis polynomial gives

\[
\sum_i\frac{q_i u_i^r}{H_4'(u_i)}
=(-1)^{3-k}\delta_{rk}.
\]

With

\[
w_i=\frac{q_i}{u_iO_iH_4'(u_i)},
\]

the signed odd moments are consequently

\[
M_r^o=(-1)^r(-1)^{3-k}\delta_{rk}
=-\delta_{rk}.
\]

All \(q_i\) are strictly positive, including \(q_i=e_0=1\) when applicable. The signs of \(H_4'(u_i)\) are \((-,+,-,+)\), so positive weights require exactly the stated odd sign orientation.

The three active equations have rank three on the support. These feasible normalized vectors therefore are extreme rays.

### 4.4 Both R5 orientations

For five distinct nodes, extremality requires all four odd moments to be active. Their matrix has rank four, giving

\[
w_iu_iO_i=\frac{C}{H_5'(u_i)}.
\]

The derivative signs are \((+,-,+,-,+)\). Positive weights permit:

- \(C>0\), with odd signs \((+,-,+,-,+)\);
- \(C<0\), with odd signs \((-,+,-,+,-)\).

The stated positive weights follow by normalizing \(C\) to \(+1\) or \(-1\). Lagrange annihilation makes all four moments zero. Their active nullspace has dimension one, proving extremality.

There is no basis for discarding the negative-first orientation.

### 4.5 Completeness

The preceding arguments exhaust:

- zero-odd supports;
- repeated-frequency supports;
- distinct nonzero supports of size at most three;
- support four;
- support five;
- larger supports, excluded by the active-rank bound.

Every listed feasible ray has a one-dimensional active face on its support. Pointed polyhedral generation therefore gives exactly Z, P, R4 and the two R5 orientations.

This is a finite-\(T\) cone argument. It makes no unjustified claim about extreme rays of an infinite-dimensional continuum cone.

## 5. Reconstruction of A implies B

### 5.1 Compactified endpoints and open-orthant separation

The normalization

\[
\widehat r(a,t)=\frac{r(a,t)}{(1+t)^7}
\]

has limits

\[
\widehat r(a,0)=a_0e_0,\qquad
\widehat r(a,\infty)=e_7.
\]

The latter uses the fixed monic leading coefficient. Both endpoint contributions are coordinatewise nonnegative.

The row image on \(K\times[0,\infty]\) is compact, so its finite-dimensional convex hull \(C\) is compact. If \(C\) contained a vector in the open negative orthant, its finite convex representation would yield a strict-negative finite aggregate. Removing endpoint terms only decreases coordinates. The remaining finite positive-node terms convert to raw weights by division by \((1+t)^7\), and zero weights can be omitted. They would contradict A.

Separation of \(C\) from the **open** negative orthant supplies a nonzero \(q\) with

\[
q\ge0,\qquad q\cdot \widehat r(a,t)\ge0.
\]

Indeed, a negative component of \(q\) would make its supremum on the negative orthant infinite; for a nonzero \(q\ge0\), that supremum is zero. Multiplication by the positive normalization denominator yields

\[
q\cdot r(a,t)\ge0
\]

for every actual member at every positive finite node.

This is a **weak**, coefficientwise nonnegative separator. It is not a strict separator or a common strict SPR numerator.

### 5.2 The even test is nonzero

Write

\[
F(t)=q_0-q_2t+q_4t^2-q_6t^3,\qquad
G(t)=q_1-q_3t+q_5t^2-q_7t^3.
\]

The pointwise inequality is

\[
F(t)E_a(t)+tG(t)O_a(t)\ge0.
\]

The first odd band has positive width. On arbitrary four distinct nodes in that band, the actual odd endpoints permit the R4 alternating signs. For each \(k\), the already reconstructed R4 weights have odd signed moment vector \(-e_k\). Summing those four feasible families produces four strictly negative odd moments.

If \(F=0\), nonzero \(q\ge0\) would be supported only on odd coordinates, and pairing it with that family would be strictly negative. This contradicts the separator. Therefore \(F\ne0\).

This is an all-variable reconstruction of the author’s proof construction, not a newly selected numerical case.

### 5.3 Nonpositive odd moments force band signs

For any finite weighted actual-member family with nonpositive odd signed moments,

\[
\sum_iw_iE_{a_i}(t_i)F(t_i)
\ge-\sum_{r=0}^3q_{2r+1}M_r^o
\ge0.
\]

At an interior point of any odd band, use the P cancellation with the same arbitrary actual even polynomial at both atoms. Its odd moments vanish and its total weight is \(O_+-O_->0\). Consequently

\[
E(t)F(t)\ge0.
\]

The strict actual-even signs give

\[
F\le0\text{ on }[a,b],\qquad
F\ge0\text{ on }[c,d],\qquad
F\le0\text{ on }[e,f],
\]

including endpoints by continuity.

### 5.4 The root box and coefficient degeneracies

We have \(F(0)=q_0\ge0\), degree at most three, and \(F\ne0\). Its weak sign on each positive-width band is strict away from finitely many roots.

The successive prescribed signs force roots in

\[
[0,a],\qquad[b,c],\qquad[d,e].
\]

If \(q_0=0\), the first root may be zero. Otherwise the first transition supplies a positive root no later than \(a\). The other two transitions occur between their respective signed bands.

These three intervals are disjoint. Hence the roots are distinct, the degree is exactly three, and

\[
F(t)=\kappa(x-t)(y-t)(z-t),\qquad \kappa>0.
\]

There is no room for extra roots or multiplicity. Scaling by \(\kappa\) gives the claimed normalization.

Thus possible initial degeneracies of the even separator coefficients are handled by the proof itself. In the normalized test, the three nonconstant coefficient magnitudes are strictly positive; only \(xyz\) may vanish.

### 5.5 Actual envelope and all ray inequalities

For a fixed \(F(t)\),

\[
\min_{E\in[E_-(t),E_+(t)]} E\,F(t)=E_F(t)F(t).
\]

The minimizing member is \(E_-\) when \(F\ge0\) and \(E_+\) when \(F<0\). At a zero of \(F\), either choice has the same zero product.

At each R4 or R5 node, this actual even endpoint combines independently with the specified actual odd endpoint. Applying the preceding weighted inequality gives precisely the displayed \(\mathcal R_{4,k}\) or \(\mathcal R_{5,\varepsilon}\).

The separator was obtained for the whole actual row family. The resulting \(F\) is therefore **one common test across all finite grids and all ray configurations**, not a separately chosen test for each ray.

This proves B.

## 6. Reconstruction of B implies A

Assume B and a strict-negative actual certificate.

For

\[
F(t)=(x-t)(y-t)(z-t)
=xyz-(xy+xz+yz)t+(x+y+z)t^2-t^3,
\]

the even test coefficient magnitudes are

\[
xyz,\qquad xy+xz+yz,\qquad x+y+z,\qquad1.
\]

They are nonnegative, and the last three are strictly positive because \(y,z>0\). Pairing them with the four strictly negative even aggregate coordinates gives

\[
L=\sum_i\mu_iE_{a_i}(t_i)F(t_i)<0.
\]

This remains strict when \(x=0\).

At each node, replace the actual even parity by \(E_F\). Coefficient independence preserves actual box membership, and minimization cannot increase \(L\).

Then split the actual odd value into a convex combination of the two actual odd endpoint values, retaining the same \(E_F\). This preserves:

- all four odd moments;
- the lowered even scalar pairing.

The resulting nonnegative weights lie in \(\mathcal C_T\) on the certificate’s finite frequency set. Decompose them using the complete ray list:

- **R4:** nonnegative scalar pairing by B.
- **Both R5 orientations:** nonnegative scalar pairing by B.
- **Z:** the node is an odd-envelope root, hence a band endpoint. The root-box signs of \(F\) agree weakly with the strict actual-even sign there.
- **P:** its scalar contribution is exactly

  \[
  (O_+(t)-O_-(t))E_F(t)F(t)\ge0.
  \]

  The first factor is strictly positive; the other product is nonnegative on the cancellation bands.

The lowered scalar pairing is therefore nonnegative, contradicting \(L<0\). This proves A.

There is no missing strictness step: strictness is used to obtain \(L<0\), while the cone and ray conditions correctly remain non-strict.

## 7. Exact quantifiers and limitations

For each eligible box \(K\) with at least one nonzero odd coefficient width, the proved statement is

\[
\begin{aligned}
&\text{No finite positive-weight actual-member aggregate lies in }(-\infty,0)^8\\
&\quad\Longleftrightarrow\\
&\exists(x,y,z)\in[0,a]\times[b,c]\times[d,e]\ 
  \text{such that every applicable R4 and both-orientation R5}\\
&\hspace{9em}\text{actual-endpoint scalar pairing is nonnegative.}
\end{aligned}
\]

The existential triple precedes all ray quantifiers.

The theorem does not exchange this for “each ray has some successful test.” Nor does it establish

\[
\forall K\ \exists(x,y,z)\ \forall\text{ rays}.
\]

An individual R4 ray has only one strictly negative odd moment and three zero odd moments. R5, Z and P have all four odd moments zero. None is itself an all-eight-strict-negative certificate. Thus the adopted at-most-five-frequency no-go does **not** imply arbitrary scalar ray nonnegativity.

The piecewise actual \(E_F\) also cannot be silently replaced by one normalized artificial root vertex. If \(F\) changes sign across the support, different actual even envelopes can be the minimizing choice at different nodes.

These distinctions support S1 LF 540–576 and 848–874.

## 8. Six-frequency same-aggregate sparsification

Let a hypothetical strict-negative certificate use exactly six distinct positive squared frequencies. Same-frequency original atoms may first be merged using their weighted average coefficient vector, which remains in the independent box.

Replace each fixed-frequency row by its convex combination of the four actual corner rows. This preserves the complete raw aggregate exactly and introduces no new frequency.

The aggregate is now a positive conic combination of finitely many vectors in \(\mathbb R^8\). If more than eight positive generators remain, choose a linear dependence

\[
\sum_j c_jr_j=0.
\]

Choose its sign so some \(c_j>0\), and set

\[
\lambda=\min_{c_j>0}\frac{w_j}{c_j}.
\]

Replacing \(w_j\) by \(w_j-\lambda c_j\) preserves the aggregate, keeps every coefficient nonnegative and makes at least one zero. Iteration leaves at most eight positive corner atoms. This is the conic bound of eight, not a convex bound of nine.

### Why all six original frequencies remain

Conic sparsification alone does not preserve frequency support. Here the preservation follows from exactly the adopted S2 LF 7 theorem:

If any original frequency disappeared, the remaining corner atoms could be merged at equal frequencies into actual members. The unchanged aggregate would then be a strict-negative certificate on at most five distinct positive squared frequencies, contradicting that imported no-go.

No W1-only statement or scalar ray inequality is used for this step.

### Why at least four groups are pure

Let \(n_g\ge1\) be the number of positive corner atoms in surviving frequency group \(g\). There are six groups and

\[
\sum_{g=1}^6n_g\le8,
\qquad
\sum_{g=1}^6(n_g-1)\le2.
\]

Every non-pure group consumes at least one of these two extra atoms. Hence at most two groups are mixed, and at least four contain a single actual corner atom.

After merging a group, its weight is the sum of its atom weights and its polynomial is their coefficientwise weighted average. Affinity of the raw row at that frequency preserves the complete eight-coordinate aggregate.

A singleton group is exactly an actual corner polynomial \(a^{\sigma\tau}\), not merely an artificial root-envelope vertex. Degenerate coefficient intervals can create duplicate corners, but do not weaken the bound.

This proves the proposition in its stated conditional scope. It neither proves a six-frequency witness exists nor asserts that four members of the **original**, unreplaced certificate were already corners.

## 9. Degeneracies and universal class obstructions

### All odd coefficient intervals fixed

The main equivalence explicitly excludes this case, appropriately: its proof that \(F\ne0\) uses a positive-width odd band.

The separate universal obstruction is valid. With fixed odd parity \(O\), choose the odd test \(G=O\). Its numerator coefficient magnitudes are positive, and every atom contributes

\[
tO(t)^2\ge0.
\]

An all-eight-strict-negative aggregate would pair negatively with that nonzero nonnegative test vector. Therefore no such certificate exists.

No collapsed-band denominator is needed.

### Degenerate even intervals

The main theorem permits them. Corner convexification, piecewise minimization and ray classification remain valid, including the case \(E_-=E_+\).

If the entire even parity is fixed, choosing \(F=E\) gives the universal obstruction

\[
E(t)^2\ge0.
\]

This supports S1 LF 832–844 independently of any finite example.

### Zero test values and zero odd values

They are handled at different interfaces:

- \(F(t)=0\): the minimizing even endpoint is immaterial to the scalar pairing.
- \(O_\tau(t)=0\): retain a Z ray, rather than divide by that value.
- Opposite nonzero odd endpoint signs at one frequency: retain P.
- R4/R5 divisions are only made for the explicitly nonzero odd values in those ray definitions.

Consequently neither the universal equivalence nor the sparsification needs a new genericity assumption.

## 10. Supplied example: explicit non-adoption boundary

I read the author’s entire supplied example, S1 LF 616–844, including:

- the claimed all-Hurwitz independent box;
- the six rational nodes and member parameters;
- positive weights;
- the claimed four zero odd moments;
- all eight claimed aggregate signs;
- the two-orientation five-node decomposition;
- the stated limited W1-only falsification.

I did **not** introduce another selected example, run arithmetic, read author code, or consume f356 or parent finite results.

Accordingly, the finite assertions in S1 LF 616–830 are **INCONCLUSIVE here as independently verified finite evidence**. This is a method-boundary qualification, not a finding that they are false.

Their advertised logical scope is appropriately limited:

- A counterexample satisfying only the four zero odd moments would falsify the quoted **moment-only** positive-first reduction, not a hypothetical reduction additionally assuming four strict even inequalities.
- The author expressly states that the supplied aggregate is not an all-eight-strict-negative certificate.
- No part of the universal cone proof, A iff B proof or six-frequency sparsification above depends on that example.
- The universal fixed-parity obstructions in LF 832–844 have the independent all-variable proofs given in §9.

The separate finite gate remains separate.

## 11. Original target remains unpaid

The review supports the reduction and conditional structural consequence, not the unrestricted decision.

Still unproved by this packet are:

1. Existence, for **every** eligible nondegenerate-odd box, of one common root triple satisfying all required actual R4 and both-orientation R5 inequalities.
2. An eligible box and actual positive-weight aggregate with all eight coordinates strictly negative.
3. A passage from the weak nonnegative separator to a **strict** common SPR numerator.

Even complete positivity of a restricted normalized W1 vertex table would not, by itself, discharge the omitted placements, opposite orientation, R4 constraints, actual piecewise-even minimization or common-test quantifier.

No worldwide-status, novelty, human-review, independent-family or formal/kernel conclusion is made.

## 12. Actual process and read receipt

- Read the complete manifest, complete freeze receipt and all seven specified status-only controls before the mathematical packet.
- Read the complete parent metadata supply before the pre-body ACK.
- Sent the required direct administrative pre-body ACK to Main **before** the first mathematical packet window.
- Read the complete packet in consecutive unelided raw windows of at most 20 LF: `1–20, 21–40, …, 1641–1660, 1661–1668`.
- Actual source-label coverage was S1 logical 1–923, S2 1–34, S3 logical 1–709, including every ending.
- One mistyped path failed for the intended packet window 1141–1160; the correct path was read immediately. No content was skipped.
- Began mathematical reconstruction only after the full packet ending.
- Matching live pins, byte counts and LF counts are **parent-supplied observations**, not reviewer-executed hashes.
- Parent-native clock observations received: **2026-10-30T09:06:30-0700 PDT** and **2026-10-30T09:16:29-0700 PDT**. Neither is claimed as my native start, private proof time or artifact-write time.
- Sent a substantive checkpoint after the complete read and reconstruction of the corner, separator and ray-classification interfaces.
- Reviewer scientific executions: **zero**.
- Reviewer native hash/count/date executions: **zero**.
- New selected scientific cases: **zero**.
- Author code, excluded held payloads, sibling/f356 results, scientific network requests and external-model CLIs: **not read or used**.
- No build, test, lint, formatter, installation, deletion, credential/provider change, commit/push or infrastructure operation occurred.
- No file-write bypass was attempted. This complete body is the fallback for parent materialization.

**Final scoped disposition:** **SUPPORTED** universal actual-box A iff B reduction, complete Z/P/R4/two-orientation-R5 classification, and same-six-frequency/same-aggregate sparsification with at least four pure actual corners. **Finite example independently unverified here; unrestricted certificate/synthesis target not proved.**