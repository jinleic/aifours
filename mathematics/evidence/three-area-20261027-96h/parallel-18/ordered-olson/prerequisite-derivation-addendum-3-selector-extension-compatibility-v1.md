# Addendum 3 — exact selector/quotient-matching compatibility, not automatic completeness

Owner **MathOlson-2-2**, successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 15:04:20 PDT 2026**.
**NEW all-variable WRITTEN candidate under the SAME narrowly frozen S1 definition-first release.**

## 1. Inputs and why this is a different failed implication

Only the COMPLETE current S1/S2 packet, SHA256 `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788`, and explicitly elementary order/counting/group/induction facts are inputs.
Its whole42LF was read after actual14:46:50 pre-body ACK. No old source/proof/review/held formula, selected control, program or external source is used. All prior contacts and STOP/HOLD/ZERO histories survive; no clean-cognition or novelty claim.

The immutable preceding candidates are v1, noncrossing/centrality addendum1 and fixed-matching addendum2, with the pins in checkpoint002. Nothing here edits or adopts them.
Their relevant combinatorial arguments are restated where needed.

The full original target O(G) is EVERY actual length2n−1 word in EVERY finite group G of order n, with an ORIGINAL-order identity selection of EXACTLY n actual occurrences.
This manuscript does not prove or refute O(G). It pays an exact quotient-incidence input a proposed packet transport must additionally satisfy.

Two stronger implications must not be smuggled in:

- every ACTUAL identity selector can be partitioned into noncrossing quotient-identity pairs;
- every such partial pair partition can be extended to the full2k−1-pair quotient certificate with one unused occurrence.

The first is false; the second has a precise extra face condition, proved below.

## 2. Exact all-variable test for an EVEN binary word

Let c1,…,c_(2r) be ANY binary word, ci∈{0,1}. Define the INTEGER alternating balance

`D(c)=sum_(j=1..2r) (-1)^(j−1)c_j`.

The signs use ranks in THIS selected word, not the parity of its original ambient occurrence indices. No reduction modulo a group order, field characteristic or cardinality is performed.

**Theorem A.** The word has a noncrossing perfect matching of equal letters IFF D(c)=0.

**Necessity.** Every nonempty noncrossing pair partition has an interval pair: choose an innermost pair, whose interior cannot contain an endpoint paired outside without a crossing. Equivalently the minimal-span proof in addendum1 applies.
An interval pair consists of adjacent equal letters in the current selected word.
Deleting two equal adjacent letters cancels their two alternating contributions, and shifts every later rank by2, so D is unchanged.
Inductively deleting all pairs yields the empty word with D=0.

**Sufficiency.** Delete adjacent equal letters as a mathematical induction, never a program/table execution.
D is unchanged by each deletion, and the remaining word has even length.
If the terminal word were nonempty, it would alternate and have length2s for s≥1.
Its D equals−s if it starts with0, and+s if it starts with1, which is nonzero in the INTEGERS.
Thus D=0 forces the terminal word empty.
Restoring the successive adjacent pairs gives a noncrossing equal-letter matching: an adjacent pair cannot cross a matching on its remaining ordered positions. ∎

The empty even word has D=0 and its empty matching, so no degenerate case is omitted.
This is an exact classification, not only a necessary parity count.

For a quotient C2 word, product identity requires only an EVEN number of1 letters. D=0 is stronger: it requires the numbers of1 letters at odd and even selected ranks to be equal.
The original group product-one condition therefore cannot be replaced by D=0 without a proof.
The next all-parameter actual-word family refutes the converse.

## 3. An original identity selector can fail the test for EVERY noncrossing packet family

Let G be ANY finite group with a normal index-two subgroup K of EVEN order k≥2, so n=2k.
Choose ANY h∉K.
Take an actual n-occurrence word S equal to k/2 repetitions of

`1, h, 1, h^-1`.

Each four-letter piece has product1 in its original order, so the whole S has product1 and has EXACTLY n=2k occurrences.
Its binary quotient word is k/2 repetitions of0,1,0,1.
Every odd selected rank has bit0 and every even selected rank bit1; hence its integer D is−k, not0.
By TheoremA, NO noncrossing equal-quotient-letter perfect matching exists on these selected positions.

Embed S as the first n actual occurrences of a FULL original word by appending n−1 identities. The full word has2n−1=4k−1 occurrences.
Thus S is a genuine correct original n-occurrence selector, not a shorter surrogate.
Yet S cannot be the union of k packets from ANY noncrossing quotient-pair family: such a subfamily would itself give the forbidden matching on S.

This is a universal family for every such G,K,h and even k, not an evaluated finite example.
The full word is not avoiding: the displayed S already proves otherwise, and the added identities give other possibilities as well.
It does not show that no OTHER selector of the word can have a compatible matching.
It proves only that encoding an arbitrary already-existing selector by a noncrossing packet certificate is NOT a valid converse.

For odd k this particular four-letter repetition construction is not asserted; for the trivial kernel it is not needed. TheoremA itself holds for all even binary lengths without a group hypothesis.

## 4. Exact extension test for a FIXED partial matching in an odd ambient word

Let W be ANY binary word of odd length, and let P be a fixed noncrossing equal-letter matching on some EVEN selected set U. Thus all positions of U are already matched in P; they are not available to a complement pair.
We ask whether P extends to a noncrossing equal-letter matching of ALL ambient positions except ONE, without changing its fixed pairs.

Draw each fixed pair as an interval. For an unselected position v, record the set of fixed intervals whose interiors contain v.
Because P is noncrossing, those containing intervals form a chain. They are determined by the deepest containing interval, or by the exterior if there is none.
Call this containing-chain label the **face** of v. Different disconnected stretches with the same label belong to the same face; fixed child intervals between them are ignored when listing that face's remaining letters.
For each face F, list its unselected letters in their inherited order as W_F.
An empty face word is permitted and has even length with D=0.

**Lemma B — no mixing between faces.** A new pair of complement positions crosses no fixed P interval IFF its endpoints have the SAME face label.

**Proof.** If exactly one endpoint lies inside some fixed interval, the endpoints alternate with that interval's endpoints, so there is a crossing.
If both endpoints lie in exactly the same containing intervals, then for each fixed interval they are both inside, both outside on one side, or on opposite sides enclosing the entire interval. None is a crossing.
The containing chains coincide exactly when the face labels coincide. ∎

**Theorem C — necessary and sufficient extension criterion.** Such an extension exists IFF:

1. EXACTLY ONE face word has odd length;
2. EVERY even face word has integer alternating balance D=0.

There is no further letter restriction on the one odd face.

**Necessity.** By LemmaB every complement pair lies in one face. Exactly one globally unmatched position therefore requires exactly one odd face, while every other face is even and perfectly matched.
The restriction of a noncrossing completion to each face remains noncrossing, so TheoremA gives D=0 for every even face.
The complement has odd cardinality because the ambient word is odd and U even, so one cannot instead have zero odd faces.

**Sufficiency.** Match every even face word by TheoremA.
For the one odd face, EVERY binary word of odd length admits equal-letter noncrossing pairs leaving one position: induct on length, removing adjacent equal pairs when present; if none exists, the word alternates and mirror-equal positions pair around its unique centre.
Every new pair is compatible with all fixed pairs by LemmaB.
Completions in different faces also cannot cross: disjoint fixed-interval subtrees are separated, while a pair in an ancestor face either encloses a child fixed interval entirely or avoids it, so it cannot alternate with a pair confined inside that child face.
Within each face the constructed matching is noncrossing by construction.
Thus all completions together with P give the required full matching, with exactly the one unmatched position in the odd face. ∎

This classifies the exact extra gap/face compatibility. Merely having a noncrossing matching on the proposed selector does NOT automatically pay extendibility.
In particular more than one odd face, or any nonzero D in an even face, is a precise obstruction to extension of that FIXED partial certificate, not a counterexample to the original group problem.

## 5. Full original-object caller and what quotient compatibility does NOT pay

For ANY actual word of length4k−1 in an index-two G/K, and ANY proposed n=2k-occurrence selector S:

- S can have its own noncrossing quotient-pair matching only if its SELECTED-rank D is0, and that condition is sufficient for such a partial quotient matching;
- for a GIVEN such partial matching P on S, extension to a full2k−1-pair quotient family with one unused occurrence is exactly TheoremC's face criterion;
- if a full family has S as a union of k of its pairs, then the induced partial matching satisfies BOTH tests necessarily.

These statements retain the actual original position labels; no gap is filled by a new source element and no original occurrence is duplicated.
TheoremC uses quotient letters only. It does NOT prove the chronological G-product of S is1, nor the aggregate product of its packet products is1 in K.
Both algebraic conditions are additional, distinct from incidence/quotient matching.

Even starting with an ACTUAL chronological product-one S does not in general give aggregate kernel product-one for its nested packets.
To see the precise reverse-coupling failure, take ANY normal K and arbitrary x∈K,a∈G with ax≠xa. Use nested packets A at first/last and B at the middle two positions of

`a, a^-1 x^-1 a, 1, a^-1 x`.

The chronological product is1 by direct cancellation.
The packet products are x and a^-1 x^-1 a, both in K by normality, but their first-occurrence aggregate
`x a^-1 x^-1 a`
is nonidentity.
This is an all-variable local algebraic counterfamily, not a claim of an original avoiding word or a new necessary law for all selectors.
Together with the forward failure in addendum1, it prevents silently identifying the two product-one predicates in EITHER direction.

Consequently the full normal-transport plan still needs a JOINT all-word theorem paying:
actual original cardinality/order, quotient pair incidence, matching extension where required, aggregate kernel identity if invoking O(K), AND the actual conjugation coupling.
The original conjecture supplies none of these stronger certificate properties merely by its name, and this candidate does not assert their joint existence for every original word.

## 6. Exact scientific delta, open step and limits

This manuscript supplies two exact all-variable equivalences (even-word matchability and fixed-partial extension), an actual full-length family disproving completeness for arbitrary original selectors, and an explicit reverse algebraic coupling failure.
These are sharper failed implications/coupling criteria, not an implementation, selected numeric trial, architecture enumeration or formal coefficient restatement.
They may be standard elementary combinatorics/group identities; novelty and primary-source attribution are unestablished and not claimed.

The remaining missing theorem is EXISTENCE of a successful JOINT actual-word certificate at the original2n−1/n threshold, or a different unrestricted proof or actual avoiding word. Its proof is not supplied by any of these conditional/equivalence statements.
No full group class beyond the stated conditional commutative boundary is newly claimed, and no prime-dihedral intermediate actual-word selector is promoted.

No new source has been opened. All preceding candidates remain immutable and unadopted until complete source/peer/parent review. Every old STOP/HOLD/ZERO outside current S1, all nine held-formula and consuming-guide restrictions, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and process findings persist.
Only current admitted literal definitions and elementary written facts were used; no new book-image/source equivalence or independent-family/formal/kernel/human/executable/novelty acceptance.
No interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/typechecker, selected numerical/control/state/boundary/decimal probe, nested agent/modelCLI/paidAPI, Git/delete/contact/publication/infrastructure action or timer/heartbeat loop.
Same18/new exclusive root/append-only/actual20min substantive cadence with honest gaps/science ends2026-10-31T21:23:27.000Z.

**END OF COMPLETE SELECTOR-EXTENSION COMPATIBILITY ADDENDUM.**
