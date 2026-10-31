# Addendum 9 — actual suffix-conjugator coupling and a bounded number of relative commutators

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 15:58:55 PDT 2026**.
**NEW WRITTEN all-group conditional coupling candidate; not adopted, an unrestricted solution or a novelty claim.**

## 1. Genuinely separate input branch and source controls

This is ordinary ordered-word/noncrossing incidence work inside the SAME admitted S1 scope, continued after Main's complete parent qualification of the public-image display.
The ONLY scientific inputs are the original finite-group ordered assertion in the frozen42LF S1/S2 packet SHA256 `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788`, group associativity/inverses/conjugation and finite ordered-partition induction.
All load-bearing identities are proved below.
There is NO finite-field polynomial, p-group theorem, public-paper bound, group algebra/augmentation ideal, representation or external source in this proof.
No claim or confidence from A5/A6, their prior classification or the displayed public-paper preliminary context is used to select or justify this step.

Dimitrov proof/method and the prospective group-algebra branch remain STOPPED; all out-of-scope displayed source/method/selection/confidence consumers are NONINPUT.
A5/A6 existence remains PRIOR/REPRODUCTION, not discovery headroom. This file neither compares their proofs to the paper nor applies any paper formula.
Prior exposure is not erased; this is a complete declared elementary input chain, not a clean-cognition or independent-noninfluence certificate.
No extra source or page was opened.

The original O(G) is EVERY actual word of length2n−1 in every finite group G of order n, with an ORIGINAL-order identity selection of EXACTLY n actual occurrences.
The result below supplies an exact actual-product coupling for a specified noncrossing certificate. It does NOT make such certificates WLOG or prove one exists for every original word.

## 2. Actual forest and canonical conjugators

Let U be ANY finite ordered set of actual selected occurrence labels, partitioned into nonempty packets in a noncrossing manner.
Noncrossing means no r<s<t<u alternate between two different packets.
List packets B_1,…,B_t by their FIRST occurrence and let b_i be each packet's OWN inherited-order product of its actual G-letters.
Let T be the chronological product over all U.

The interval spans of noncrossing packets are disjoint or nested. Any packet lying inside another lies wholly in ONE gap between consecutive occurrences of that outer packet; otherwise their endpoints alternate.
This gives a forest: root packets have no containing packet; immediate children occur in gaps of their immediate parent. Let r be the number of roots.
Different roots are ordered by their disjoint chronological spans.
The packet first-occurrence order is exactly the forest preorder: outer packet, then the gap forests from left to right, then the next root.
These assertions include singleton packets and empty gaps.

For packet A with OWN letters a_1,…,a_l, define its ACTUAL suffix after gap j by

`s_(A,j)=a_(j+1)…a_l`, for1≤j<l.

These are products of ACTUAL letters of A ONLY; they do not include nested packets.
Set g_A=1 for each root.
If B is an immediate child in gap j of A, define recursively

`g_B=g_A s_(A,j)^-1`.

Thus every g_B is a fixed product of actual inverse suffixes along its ancestor chain, in the displayed order. No arbitrary group coefficient, held formula or independently assigned label replaces those products.

## 3. Exact first-occurrence factorization, every group

**Theorem A.** For EVERY assignment of ACTUAL G-elements to U and EVERY such noncrossing partition,

`T = product_(i=1..t, first-occurrence order) g_i b_i g_i^-1`.

No centrality or commutativity hypothesis is required.

**Proof.** For a packet A, let Y_j be the ACTUAL chronological product of the full nested forest in its j-th gap.
Its entire interval product is

`a_1 Y_1 a_2 Y_2 … a_(l−1)Y_(l−1)a_l`.

Writing b_A=a_1…a_l gives the exact identity

`interval(A)=b_A product_(j=1..l−1, increasing) s_(A,j)^-1 Y_j s_(A,j)`.

Successive suffix cancellations prove it: after the first factor one has a_1Y_1a_2…a_l; after the next, a_1Y_1a_2Y_2a_3…a_l; and so on. With l=1 the product is empty and the identity is immediate.
Each Y_j is the ordered product of its child intervals. Conjugation distributes over those products.
Induction on the number of packets therefore gives their first-occurrence factorization, with child conjugators exactly g_A s_(A,j)^-1.
At a root g_A=1; multiplying the disjoint root intervals in their actual order gives the stated global identity. The empty partition has both sides1. ∎

This pays the actual conjugating words and their order; it is stronger than saying merely that the product lies in a normal subgroup.
It does not identify individual packet products with the interval products containing them.

## 4. Exact defect factorization and at most t−r relative commutators

Now suppose K is a normal subgroup of G and every b_i lies in K.
Put

`B_i=b_1…b_i`, with `B_0=1`,
`c_i=g_i b_i g_i^-1 b_i^-1`.

**Theorem B.** The SAME actual chronological product satisfies

`T = [ product_(i=1..t) B_(i−1) c_i B_(i−1)^-1 ] · B_t`.

The displayed product is in increasing first-occurrence order. Its nonidentity factors number at most t−r, and each is a SINGLE actual relative commutator of an element of G with an element of K.

**Proof.** TheoremA writes T as `(c_1b_1)…(c_tb_t)`.
An elementary induction moving each new c_i to the left of the accumulated b-prefix gives

`(c_1b_1)…(c_tb_t) = c_1 (b_1c_2b_1^-1) … (B_(t−1)c_tB_(t−1)^-1) B_t`.

This is exactly the formula.
For a root packet g_i=1, so c_i=1; there are r such factors.
For ANY i let u_i=B_(i−1)g_iB_(i−1)^-1 and v_i=B_(i−1)b_iB_(i−1)^-1.
Since B_(i−1),b_i∈K, v_i∈K. Its correction factor is exactly

`u_i v_i u_i^-1 v_i^-1`.

Thus it is ONE relative commutator, not an unbounded unspecified element of [G,K]. At most the t−r nonroot packets can contribute. ∎

This is an upper bound, not a claim that its t−r factors are always independent, always nontrivial or universally minimal for every G.
For separated packets r=t and the correction is empty, recovering literal chronological transparency.
For a single nesting one genuinely nontrivial correction is possible: actual outer letters a,a^-1x and inner product x^-1 give `a x^-1 a^-1x`, which is nonidentity whenever a does not commute with x∈K. Thus a uniform zero-factor bound for all nested patterns would be false.
No finite instance or numerical group table was tested to establish either statement.

## 5. A strictly value-sensitive sufficient coupling and exact converse

Assume the ACTUAL aggregate kernel product B_t is1.
Then TheoremB gives the exact iff:

`chronological original product is1`

IFF

`product_i B_(i−1)c_iB_(i−1)^-1 =1`.

In particular it SUFFICES that, for every NONROOT selected packet B_i, its ACTUAL b_i commutes with its ACTUAL suffix-chain conjugator g_i.
Root packet products may be completely noncentral.
The subgroup K itself need not be central, and the individual nonroot packet products need not commute with all of G.
This is a weaker, occurrence-sensitive sufficient condition than imposing K⊆Z(G) or requiring all packet products central.
The condition is NOT asserted necessary: nontrivial correction factors can cancel in their exact displayed order.
The full correction-product equation, not separate vanishing of each factor, is the exact converse.

An important simple subcase is that every NONROOT packet has product1 while root products, in order, have product1; then all corrections vanish without any centrality assumption.
This is a valid actual-value implication, not a claim such packet values can always be found in an arbitrary word.

## 6. Original-cardinality caller, with ALL missing existence premises explicit

Let G have order n and w be an ACTUAL original word of length2n−1.
Suppose a given selected set U has EXACTLY n actual occurrences and a given noncrossing packet partition with packet products in a normal K.
If B_t=1 and the exact correction product of TheoremB is1, then the chronological product on U is1. Hence U is a genuine original-order n-occurrence selector.
Conversely, for THIS same data with B_t=1, a genuine selector forces that correction product1 by TheoremB.
Neither direction changes the word, duplicates an occurrence, reorders its selected product or replaces n by a quotient cardinality.

For a family of m-occurrence quotient-identity packets with |K|=k and n=km, any chosen k-packet subfamily has n actual occurrences. One must form its INDUCED selected forest and suffix conjugators, then apply the theorem.
If an outer packet from the full family is NOT selected, its letters contribute NO conjugation to the selected product. Reusing the full family's ancestor suffixes would be a false caller.
Thus both the root count and the actual g_i depend on the SELECTED subfamily.
This explicitly retains the joint incidence/action dependence; it is not a fixed-label kernel-zero model.

The original problem still needs EXISTENCE, for EVERY original word, of a selector/certificate satisfying the coupled equations, or a different genuine proof/actual avoiding word.
Noncrossing packet representation is not asserted WLOG: previously derived actual selector-completeness obstructions are not withdrawn. No reduction from every arbitrary original selector to this packet model is supplied.
This conditional all-group coupling theorem is therefore real additional structure, not an unrestricted Olson theorem or an existence claim hidden inside notation.

## 7. Exact scientific delta and assurance

The delta beyond normal-closure control is an ACTUAL canonical first-occurrence conjugator factorization, an explicit product of at most t−r relative commutators, and a weaker value-sensitive sufficient condition with a precise original-order iff caller.
Everything is universally quantified over G, actual letters, packet sizes and noncrossing forests, including empty/singleton/separated/nested degenerate cases.
It may be elementary/previously known; novelty, SOTA and priority are not claimed.
No p-group existence prior, paper quantitative theorem or source-method headline is needed for the proof.

This file needs its own separately frozen full mathematics AND dependency/application review before adoption. It does not enlarge an existing wave or inherit a no-defect verdict.
All earlier files remain immutable. The full all-finite-group original and the old odd-prime dihedral actual-word bridge remain unresolved.
The prospective group-algebra/augmentation route and every affected Dimitrov source/proof/method line remain STOPPED. Extra displayed context and ALL consuming method/selection/confidence remain NONINPUT.
Other old STOP/HOLD/ZERO outside S1, nine held formulas/consumers, v214-A/threshold/v227, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and process findings persist.
No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numeric/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/publication/contact/infrastructure action or timer/heartbeat loop.
WRITTEN/same harness, not formal/kernel/human/configured-family/executable/novelty acceptance. Same18/new exclusive append-only root/actual20min substantive cadence with honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE ACTUAL SUFFIX-DEFECT COUPLING.**
