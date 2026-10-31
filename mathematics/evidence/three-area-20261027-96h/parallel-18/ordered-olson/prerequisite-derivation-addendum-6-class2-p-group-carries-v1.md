# Addendum 6 — full original-order Olson selectors for ALL finite class-two p-groups, with power carries paid

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 15:26:05 PDT 2026**.
**NEW complete WRITTEN candidate theorem. Not reviewed/adopted, formal/kernel checked or novelty-cleared.**

## 1. Exact scope and input boundary

**Theorem A.** For ANY prime p and ANY finite p-group G with `[G,G]⊆Z(G)`, put n=|G|.
For EVERY actual word a_1,…,a_(2n−1) in G, the number A of n-element ORIGINAL index subsets whose product IN INCREASING INDEX ORDER is identity satisfies

`A ≡ 1 (mod p)`.

In particular every such word has an ORIGINAL-order identity subsequence of EXACTLY n actual occurrences.
The trivial group is included with its unique selector.

This is the FULL original2n−1/n assertion for the stated entire group class, including arbitrary prime-power exponent, arbitrary identity/repeated letters and every actual type/order pattern.
It is NOT a WLOG model of arbitrary finite groups and does not settle mixed-prime groups, higher nilpotency class or the original unrestricted question.
In particular it does not silently cover the old odd-prime dihedral intermediate route.

Only the COMPLETE current S1/S2 definition-first packet SHA256 `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788`, read after the actual14:46:50 exposure ACK, and explicitly elementary group/finite-polynomial facts are inputs.
All specialized group, power-carry, digit and zero-count bridges are proved below. No external group-structure, Chevalley–Warning, group-algebra/Jennings theorem or paper proof is imported.
The earlier prime-exponent A5 candidate is preserved, but neither its verdict nor its source body is needed as a premise of this standalone proof.
Prior group/polynomial exposure survives; no blind/clean-cognition/non-influence certificate or novelty/priority claim.

## 2. Elementary cyclic decomposition of finite abelian p-groups

We first prove the only group-structure input needed for the centre and central quotient.

**Lemma B.** Every finite abelian p-group is a direct product of cyclic groups of p-power order.

**Proof.** Write it additively. For a nontrivial A choose a of MAXIMAL order p^e. All element orders are p-powers dividing that maximum, so p^e annihilates A.
Start with the homomorphism χ:<a>→C_(p^e) sending a to1.
Suppose χ is defined on a subgroup H containing a, and choose b outside H.
The coset b+H has order p^r for some1≤r≤e; thus h0=p^r b∈H and p^(e−r)h0=0.
It follows that p^(e−r)χ(h0)=0 in C_(p^e), so χ(h0) is a multiple of p^r. Choose y with p^r y=χ(h0).
Define on H+<b>

`χ'(h+j b)=χ(h)+j y`.

For well-definedness, any difference j−j' with (j−j')b∈H is a multiple p^r t. The compensating H difference is−t h0, and its χ value cancels p^r t y.
Thus χ' is a homomorphism extending χ. Its domain strictly grows, so finitely many such extensions reach A.
Now χ(a)=1, and every x splits as `χ(x)a + (x−χ(x)a)`, the second term in kerχ.
The intersection <a>∩kerχ is trivial, so `A=<a>⊕kerχ`.
Induct on |A| for the smaller kernel. The trivial group is an empty product. ∎

The only ordinary order fact used is that the order of an element/coset divides the order of its finite group, obtained by the partition into cosets of its cyclic subgroup.
No classification source or selected group table was consulted.

## 3. Actual central normal form and its indispensable carry data

Let Z=Z(G). Both Z and G/Z are finite abelian p-groups: the latter is abelian because `[G,G]⊆Z`.
Apply LemmaB to obtain ACTUAL decompositions

`G/Z ≅ product_(i=1..d) C_(q_i)`, with `q_i=p^(a_i)`,
`Z ≅ product_(j=1..c) C_(r_j)`, with `r_j=p^(e_j)`.

Only nontrivial factors are listed. Empty products are allowed.
Let Q=product_i q_i, R=product_j r_j. Then n=QR=p^m, with m=sum_i a_i+sum_j e_j.
Choose ANY actual lifts h_i of the quotient generators and actual central generators z_j for the displayed cyclic factors.
Every actual element has a UNIQUE expression

`h_1^(α_1)…h_d^(α_d) z_1^(β_1)…z_c^(β_c)`,

with INTEGER representatives0≤α_i<q_i and0≤β_j<r_j.
This follows first from its actual quotient coordinates and then from the unique remaining central coordinates.

Unlike the exponent-p case, we do NOT assume h_i^(q_i)=1.
Define the ACTUAL central coefficients θ and κ by

`h_i^(q_i)=product_j z_j^(θ_(ij))`,
`[h_i,h_l]=product_j z_j^(κ_(il,j))`,

with `[x,y]=x^-1y^-1xy` and nonnegative representatives modulo r_j.
These data come from the given G; they are NOT freely assigned coefficients claimed realizable.
The first equation is legitimate because h_i has quotient order q_i. The second uses class at most2.
Central commutator swaps give, by ordinary induction,

`h_i^u h_l^v=h_l^v h_i^u [h_i,h_l]^(uv)`.

All actual noncentral powers may be kept UNREDUCED as integers until the final identity test. This avoids silently deleting central power carries.

For the actual input letter a_v, denote its above integer coordinates by α_(vi),β_(vj).
For a Boolean support vector z_v∈{0,1}, collecting the selected letters IN THEIR ORIGINAL ORDER gives exactly

`product_(v selected, increasing) a_v = h_1^(S_1)…h_d^(S_d) z_1^(T_1)…z_c^(T_c)`,

where

`S_i(z)=sum_v α_(vi) z_v`,

`T_j(z)=sum_v β_(vj)z_v + sum_(u<v) sum_(i>l) κ_(il,j) α_(ui)α_(vl) z_u z_v`.

The strict u<v is the actual occurrence order; sorting BASIS generators accounts for it through the exact central commutators. No selected letter is reordered without paying those terms.
Coefficients are nonnegative integers. Using representatives modulo r_j changes only a multiple of the central order, hence not the displayed group element.

By quotient uniqueness, this product is identity IFF:

1. EVERY q_i divides S_i;
2. for EVERY j, r_j divides

`U_j = T_j + sum_i θ_(ij)(S_i/q_i)`.

The quotients in condition2 are used ONLY after condition1. Then h_i^(S_i)=(h_i^(q_i))^(S_i/q_i) is genuinely central.
These two conditions pay ALL power carries and central commutator coupling.

## 4. Remove conditional division without losing equivalence

If d>0 put q=max_i q_i=p^a. Since all q_i are powers of the SAME p, q/q_i is an INTEGER.
If d=0 put q=1,a=0. Then G is abelian and the quadratic commutator term is absent.
For every central coordinate define the INTEGER polynomial

`F_j(z)=q T_j(z)+sum_i θ_(ij)(q/q_i)S_i(z)`.

Whenever the quotient conditions q_i|S_i hold, this is exactly q U_j.
Thus the actual identity conditions are EQUIVALENT to

`q_i|S_i for all i`, AND `q r_j|F_j for all j`.

Under the first conditions, F_j is already divisible by q=p^a. Therefore the lower a base-p digits of F_j vanish AUTOMATICALLY; only digits a,…,a+e_j−1 must be additionally constrained.
This logical order is essential. We do NOT assume those lower digits vanish for unrelated supports or divide an arbitrary field variable by q_i.

Every quadratic coefficient of F_j is divisible by q. If q=1, there are NO quadratic terms at all because d=0.
These actual coefficient divisibilities will supply the sharp degree budget; an unrestricted quadratic-polynomial estimate would be too crude.

## 5. Digit polynomials for INTEGER linear/quadratic activation sums

**Lemma C.** Let H(z)=sum_A c_A z_A be an integer polynomial with nonnegative coefficients, where `z_A=product_(v∈A)z_v` is a Boolean activation monomial. Define over F_p

`P_H(T,z)=product_A [1+z_A((1+T)^(c_A)−1)]`.

Terms with c_A=0 may be omitted. At any Boolean support,

`P_H(T,z)=(1+T)^(H(z))`.

Consequently the polynomial `Δ_l(H)(z)=coefficient_(T^(p^l)) P_H(T,z)` evaluates to the l-th base-p digit of the INTEGER H(z), reduced modulo p.

**Proof of the digit statement.** For any nonnegative integer w with digits w_b,

`(1+T)^w=product_b (1+T^(p^b))^(w_b)` in F_p[T].

The coefficient of T^(p^l) is w_l: the total lower-digit degree is at most p^l−1, and higher factors cannot contribute. This proves the claim with w=H(z). ∎

This is a symbolic universally defined polynomial; no coefficients, fields or support sets are generated/enumerated by a program.
It is valid even when H(z) is much larger than a group order.

### Degree control paid by actual divisibilities

For a positive coefficient c divisible by p^b,

`(1+T)^c=(1+T^(p^b))^(c/p^b)` in F_p[T],

so every positive T-degree in that factor is at least p^b.
An activated factor contributes degree |A| in z.
If in EVERY factor |A| is at most its minimum possible positive T-degree, then a coefficient of T^w in the product has z-degree at most w: in any contributing term the activated z-degrees sum to at most its T-degrees, which sum to w.
Repeated z variables or cancellation can only lower degree; no squarefree-top shortcut is being used.

For each S_i only LINEAR activations occur; their minimum positive T-degree is at least1. Hence

`deg_z Δ_l(S_i) ≤ p^l`.

For F_j the linear activations again satisfy this condition. A quadratic activation has coefficient divisible by q, so its positive T-degrees are at least q.
When q≥2, its activation degree2 is at most q. When q=1 there is no quadratic activation.
Therefore in ALL cases

`deg_z Δ_(a+l)(F_j) ≤ p^(a+l)=q p^l`.

This is the key carry-correct estimate. It uses the ACTUAL q-divisibility of the quadratic coefficients, not an unproved generic low-degree coordinate ansatz.

## 6. Boolean supports, exact n cardinality and the complete equations

Let L=2n−1. Introduce field variables t_1,…,t_L and set z_v=t_v^(p−1), which is0 or1.
For completeness, Fermat's identity follows by multiplying the nonzero field elements after their permutation by any nonzero scalar; cancellation gives u^(p−1)=1.
Let w=sum_v z_v as an INTEGER, namely the number of nonzero t_v.
Impose ALL equations:

- digits0,…,m−1 of w vanish;
- digits0,…,a_i−1 of each S_i vanish;
- digits a,…,a+e_j−1 of each F_j vanish.

Use the Δ polynomials of §5, with H=w for the first family.
The first family means p^m=n divides w; since0≤w≤2n−1, it means EXACTLY w=0 or w=n.
The second family means q_i|S_i.
Given that, §4 proves the third family means q r_j|F_j, equivalently the actual central conditions U_j=0 modulo r_j.
Hence a field point satisfies ALL equations IFF its support is empty OR is an ACTUAL n-occurrence identity selection in ORIGINAL ORDER.
There is no relaxation, arbitrary coefficient assignment or one-way-only status implication in this equivalence.

## 7. Complete degree budget, all exponents and all primes

Substituting z_v=t_v^(p−1) multiplies the z-degree bounds by p−1.
The cardinality equations therefore have total degree cost

`sum_(l=0..m−1) (p−1)p^l = n−1`.

The quotient equations have total cost at most

`sum_i sum_(l=0..a_i−1)(p−1)p^l = sum_i(q_i−1)`.

The central equations have total cost at most

`sum_j sum_(l=0..e_j−1)(p−1)q p^l = q sum_j(r_j−1)`.

For any list of positive integers, expanding product_i[1+(q_i−1)] gives

`sum_i(q_i−1) ≤ Q−1`.

Similarly `sum_j(r_j−1)≤R−1`. Empty lists give0≤0.
Also q≤Q, including the convention q=Q=1 when d=0.
Thus the total GROUP-coordinate degree cost is at most

`(Q−1)+q(R−1) ≤ (Q−1)+Q(R−1)=QR−1=n−1`.

Adding the exact-cardinality cost gives

`sum of degrees of ALL equations ≤ 2n−2 < 2n−1=L`.

No small-prime, exponent, vector-dimension or nonabelian exception is suppressed in this inequality. In particular characteristic2 and arbitrary central power carries are included.
This strict inequality is the substantive gain from the weighted digit construction, not an evaluated numerical boundary.

## 8. Elementary zero-count lemma and the actual selector count

For polynomials f_r in L variables over F_p with sum deg(f_r)<L, the common-zero count C is divisible by p.
Here is a complete proof rather than an external import.
The polynomial `product_r(1−f_r(t)^(p−1))` is their common-zero indicator over F_p and has degree less than L(p−1).
Every monomial therefore has SOME variable exponent e<p−1.
If e=0, its complete sum over that variable is p=0 in F_p.
If0<e<p−1, the degree-e polynomial X^e−1 cannot vanish on all p−1 nonzero scalars. Choose one scalar u with u^e≠1; scaling the summation variable proves its power sum0.
Every monomial's full field sum is therefore0. The indicator sum is the common-zero count modulo p, proving C≡0.
The polynomial root bound used here is the elementary repeated-linear-factor bound.
Zero equations can be omitted and never increase the degree budget.
No finite-field sum is executed or tabulated; these are universal written identities.

Apply the lemma with the complete degree budget of §7.
Exactly ONE common zero has empty support: all t_v=0.
Each actual original n-index identity selector has EXACTLY(p−1)^n field realizations, choosing its nonzero coordinates independently.
By §6 these are ALL other common zeros. Therefore

`C=1+A(p−1)^n`.

For odd p, n=p^m is odd and `(p−1)^n≡−1 modp`.
For p=2, `(p−1)^n=1≡−1 mod2` as well.
Consequently C≡0 gives `A≡1 modp`, so A≥1.
This proves TheoremA at the full original word/order/cardinality scope.

For n=1, the group is trivial and the single index is the unique selector, with A=1. One may instead observe that the equation families are empty and the same one-variable field count equals p. No special false denominator or absent central factor is used.

## 9. BOTH actual-object directions and noncommutative coupling audit

**Field solution to original object:** the cardinality digits force support0 or EXACTLY n. For a nonempty support, quotient digits and the carry-correct central digits are exactly the unique ACTUAL group normal-form identity conditions. The support indices are read in their ORIGINAL increasing order, as fixed in the u<v commutator terms. No letters or cardinality change.

**Original object to field solutions:** any actual n-index original-order identity selection satisfies every digit condition, and all independent nonzero t_v choices yield those same Boolean activations. This gives the exact count equality, not a loose necessary condition.

**No uncoupled transport:** no quotient packet family is flattened. Actual commutator terms AND h_i^(q_i) central power carries are retained in the same full word. In particular the exponent-p assumption of the earlier candidate is NOT smuggled into this extension.
No old formal degree/even-pointmass interpolant, free Hessian, prescribed array, selected parameter or protected source is used.

Repeats, identity entries, zero coordinate coefficients, vanished commutators, trivial quotient, arbitrary centre factor counts and all characteristic2 cases are permitted. Polynomial cancellations only help the proved upper-degree bounds.
The normal-coordinate bases are arbitrary ACTUAL cyclic decompositions, not a special symmetry/ansatz.

## 10. Exact scientific delta and remaining original problem

The preceding positive candidate covered prime exponent. This manuscript supplies the missing central-power-carry and weighted-digit argument and proves the FULL original ordered assertion for EVERY finite class-at-most-two p-group of ANY exponent, with the same selector-count congruence.
It is a real positive proper-GROUP-CLASS theorem candidate, not an outer word-count range, isolated finite example, source encoding or formal feasibility relaxation.
The theorem and proof may be known; novelty/priority/current literature are not cleared or asserted.

Groups with mixed prime divisors, arbitrary nilpotency class or arbitrary finite groups remain outside this theorem. Neither conditional quotient transport nor the new group-class result is asserted WLOG.
The original all-finite-group ordered Olson problem and the old odd-prime dihedral actual-word residual remain unresolved by this manuscript.
No actual avoiding word or unrestricted no-go is claimed.

This complete new candidate needs a separately frozen full mathematics AND dependency/application/carry audit and Main's complete source AND return reads before adoption. Do NOT enlarge any already frozen A5 review silently.
The degree-bounded digit helper, full normal-coordinate construction and BOTH support directions are load-bearing and must not be replaced by a source hash or the earlier exponent-p verdict.

## 11. Controls and provenance

The only named ordinary facts used are group axioms/quotients/coset cardinality, basic finite cyclic arithmetic, normality/central commutator swaps, finite induction, binomial/Frobenius identities, integer base-p digits, polynomial root bound and elementary finite counting. Cyclic decomposition, digit degrees, zero count and all specialized applications are proved above.
No original-paper proof, advanced group-coordinate theorem, nilpotent-group algebra result or computational output is a premise.
Prior exposure is not erased and the supplied page-image transcription is not freshly authenticated here.

All older files remain immutable/unadopted at their exact gates. Every STOP/HOLD/ZERO outside the narrow S1 release, nine held formulas/consumers, v214-A/threshold/v227, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and old process findings persist.
No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or timer/heartbeat loop.
WRITTEN/same harness, not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/new exclusive append-only root/actual substantive20min cadence and honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE CARRY-CORRECT CLASS-TWO p-GROUP SELECTOR PROOF.**
