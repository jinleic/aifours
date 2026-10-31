# Addendum 1 — sharp noncrossing/centrality coupling and complete index-two packet existence

Owner **MathOlson-2-2**, same successor math-2.
Actual `/bin/date` before writing: **Tue Oct 27 14:56:46 PDT 2026**.
**NEW WRITTEN candidate.** The complete198LF `prerequisite-derivation-v1.md`, SHA256 `1d374d8c6984a31641d7fa5a4058e2f3dbc4965acf3308c74cfd4b80641c67dc`, remains immutable and unadopted.
This is a genuine next all-variable step in the SAME S1 release, not new source permission or a blanket restart.

## 1. Inputs and exact question

Inputs are the COMPLETE frozen S1/S2 packet SHA256 `02114e86e30a8619d32d9a00de5c0ba71445210f68a39e80382f8cdc46cbf788`, read AFTER the actual14:46:50 pre-body ACK, and ordinary group/finite-order/induction facts. The relevant calculations are fully restated here, not imported from an unseen review or old proof.
No old candidate, held formula, primary-source page, Dimitrov/Mohar source, selection guide or scientific program is used.
Prior exposure and every STOP/HOLD/ZERO outside the narrow release persist; no clean-history or independent-cognition assertion.

The original assertion O(G) still means EVERY word of length2|G|−1 has an ORIGINAL-order identity subsequence of EXACTLY|G| actual occurrences. This addendum does NOT prove it for arbitrary G.

Let U be a finite set of selected original indices in its inherited order, partitioned into nonempty packets. Each packet's product is its own inherited-order product. List packets by their FIRST occurrence.
The partition is **noncrossing** if there are no r<s<t<u with r,t in one packet and s,u in a different packet.
A packet may contain another packet's entire interval; this is nesting, not crossing.
Chronological separation is the stronger case in which no packet interval contains or overlaps another packet interval.
All interval statements are in the selected ordered set U. Unselected original positions do not enter its product, and their labels are never changed.

Two logically different hypotheses must not be confused:

- every packet product is individually1;
- packet products lie in a subgroup K and ONLY their aggregate product, in first-occurrence order, is1.

The following theorems give different, sharp answers.

## 2. An interval packet exists in every noncrossing partition

**Lemma 1.** A nonempty noncrossing partition has a packet that is an interval in the selected order. Removing that packet leaves a noncrossing partition.

**Proof.** Choose a packet with smallest inclusive endpoint span. A singleton is already an interval.
Otherwise, if an intervening position belonged to a different packet B, noncrossing forces ALL of B between the chosen endpoints: an inside and outside B endpoint would alternate with the chosen packet's endpoints.
B would then have a strictly smaller span, a contradiction.
Hence the chosen packet contains every selected position in its span.
Removing positions cannot introduce an alternating four-endpoint pattern, proving the second assertion. ∎

This lemma is about actual ordered incidence, not arbitrary free coefficient data.

## 3. Exact criterion when EACH packet is individually product-one

**Theorem 2.** For a FIXED group G and a FIXED finite packet partition, the following implication holds for EVERY assignment of G-elements to its actual labels:

`every packet product = 1  ==>  chronological union product = 1`

IFF either G is abelian or the partition is noncrossing.

**Sufficiency, noncrossing.** Use Lemma1. An interval packet contributes a consecutive factor1 to the selected chronological product and can be removed without changing that product.
Induct on the number of packets. The empty product is1; singletons cause no difficulty.
Every packet is removed by its own actual product1, not by reordering an individual letter.

**Sufficiency, abelian.** In an abelian group one may collect letters by packet, giving the product of the packet products, hence1.

**Necessity for a nonabelian G.** If the partition crosses, take r<s<t<u in packets A,B,A,B respectively. For arbitrary noncommuting a,b∈G, assign a,a^-1 to r,t and b,b^-1 to s,u, and identities to ALL other labels.
Every packet has product1, but the chronological union has product `a b a^-1 b^-1 ≠ 1`.
This is a universal symbolic family for every nonabelian G, not a selected numerical/group-table trial. ∎

Thus unconditional concatenation transparency from v1 is stronger than needed for individual identity packets: nesting is allowed under individual identity, whereas crossing is the exact universal obstruction.
This is not a statement that every crossed ACTUAL assignment fails; it characterizes validity for ALL assignments.

## 4. Exact criterion when ONLY the aggregate kernel product is1

For a subgroup K≤G define the property of a fixed partition:

> For EVERY assignment with every packet product in K and their first-occurrence-ordered aggregate product1, the chronological union product is1.

**Theorem 3 — complete incidence classification.**

1. If G is abelian, the property holds for every partition and every K.
2. If the partition is chronologically separated, the property holds for every G,K.
3. If the partition crosses and G is nonabelian, the property fails for every K, even K={1}.
4. If the partition is noncrossing but has a genuine nesting, the property holds IFF K⊆Z(G).

These regimes exhaust the possibilities: a noncrossing partition without nesting has disjoint packet intervals and is separated in first-occurrence order.

**Cases1–3.** Cases1–2 are immediate from their products. The crossed assignment in Theorem2 has all packet products1∈K and aggregate1, so proves case3.

**Centrality suffices in case4.** More strongly, if EVERY actual packet product lies in Z(G), the chronological union product equals the product of all packet products in ANY order.
Use an interval packet B from Lemma1. Writing the chronological product as P_left b_B P_right, centrality allows moving b_B outside without changing the product of the remaining actual positions.
Induction removes all packets. Central packet products commute, so the result agrees with first-occurrence order as well.
In particular K⊆Z(G) suffices; the stronger actual-word condition that only the PARTICULAR packet products are central also suffices even if K itself is not central.

**Centrality is necessary for a fixed nested pattern.** Let A be an outer packet and B a packet strictly between its endpoints. If K is not central, choose arbitrary x∈K and a∈G with ax≠xa.
Assign a to A's first endpoint and a^-1x to its last endpoint; assign x^-1 to ONE occurrence in B; assign identity to every other label.
The packet products are x for A, x^-1 for B, and1 otherwise. Their first-occurrence order puts A before B, so their aggregate is1.
The chronological union product is `a x^-1 a^-1 x ≠ 1`.
Thus the property forces every x∈K to commute with every a∈G, which is exactly K⊆Z(G). ∎

Theorem3 requires no normality as an algebraic result. Normality is required only when K is used as a quotient kernel.
It proves that “noncrossing repairs disjoint quotient extraction” is itself incomplete in a noncentral extension: noncrossing suffices for INDIVIDUAL packet identities, not for a kernel theorem producing only aggregate identity.
No full group assertion is negated by this incidence classification.

## 5. Paid original-object transport with central ACTUAL packet values

Let G have a normal subgroup K, k=|K|, m=|G/K|, n=km, and let w be ANY actual word of length2n−1.
Assume:

- O(K);
- a disjoint NONCROSSING family of2k−1 packets, each of EXACTLY m actual original occurrences and quotient product1;
- EVERY packet's ACTUAL G-product is central in G.

The packet products lie in K, so O(K) gives k packets with aggregate product1 in their first-occurrence order.
A subfamily of a noncrossing family is noncrossing.
The actual packet products remain central. Theorem3's stronger value-specific statement therefore makes their chronological union product1.
Their union has EXACTLY km=n distinct original occurrences and is a valid original-order selector.

This is a STRICT weakening of the separated-packet prerequisite: genuine nesting is allowed. It is a true coupling lemma with an exact original-word caller, not a bare encoding.
K⊆Z(G) is a sufficient source-wide hypothesis for the central-value condition, but it is not necessary for a particular word/family.
Conversely, noncrossing incidence plus membership of packet products in a general K alone cannot justify this caller, by Theorem3's necessary centrality result.

No theorem here supplies such central-valued packets for every word or proves O(K) in general.
For k=1 the aggregate chooses one packet; for m=1 each packet is a singleton. The caller reduces to the corresponding trivial identity/previous O(K) assertion and remains valid.

## 6. Complete noncrossing quotient-pair existence at index2

**Theorem 4.** EVERY word of ODD length2r+1 over a two-letter alphabet has a noncrossing equal-letter pair partition of all but ONE actual position.

**Proof by induction on r.** For r=0 leave the only position unmatched.
If two adjacent letters agree, pair them, remove their two positions and apply induction to the remaining odd word. Restoring an adjacent pair cannot cross any recursively chosen pair.
If there is no adjacent equality, the word alternates. Pair position i with2r+2−i for i=1,…,r and leave the centre r+1 unmatched.
The mirrored positions have the same parity because their sum2r+2 is even; hence their letters agree. These pairs are nested, so noncrossing.
These cases cover ALL two-letter words, with no enumeration. ∎

Apply this to the actual quotient word of ANY index-two extension G/K at the FULL original length4k−1.
There are EXACTLY2k−1 noncrossing pairs, with equal quotient letters and hence quotient identity products; exactly one original occurrence is unused.
Thus the index-two quotient has NO packet-EXISTENCE obstruction once noncrossing replaces separation.
The remaining defect is exactly the value/action coupling exposed by Theorem3, not absence of a pairing.
This sharpens v1's obstruction rather than merely repeating it.

If K is central and O(K) holds, Theorem4 plus the caller in §5 proves O(G) for this entire extension class.
Such G is actually abelian: writing elements as z h^ε with z∈K and ε∈{0,1}, the central factors and powers of h commute.
Accordingly this special closure is a classical commutative region, NOT a new nonabelian class or a new unrestricted Olson solution.
The substantive new boundary supplied here is the exact separation/noncrossing/centrality distinction and the original-object coupling needed outside that region.

## 7. Full-length noncrossing failure caller when K is noncentral

The nested counterassignment is not confined to a short surrogate word.
Let G be ANY nonabelian index-two extension with |G|=2k, k≥3. Its index-two subgroup K is not central, since central K and cyclic quotient would make G abelian.
Choose arbitrary x∈K,a∈G with ax≠xa.
Use an actual word of length4k−1 whose first four letters are

`a, x^-1, 1, a^-1 x`,

and all remaining letters are identities.
Let B1={1,4}, B2={2,3}, and B_j={2j−1,2j} for3≤j≤2k−1.
This is a NONCROSSING family of2k−1 pairs, with packet products x,x^-1,1,…,1 in K.
The first k packet products multiply to1.
Their chronological union has EXACTLY2k=n original occurrences but product `a x^-1 a^-1 x ≠ 1`.
Thus neither correct cardinality, quotient products nor noncrossing incidence repairs the missing noncentral coupling.
The original word itself has4k−4 identity letters and hence an immediate correct n-occurrence identity selector. It is NOT an avoiding word.
Again this refutes automatic flattening of the specified legitimate kernel choice, not the existence of some other jointly chosen certificate.

## 8. Exact all-variable forest formula — the coupling a replacement must retain

For a general noncrossing family, consider an outer packet with actual letters a1,…,a_l.
Its consecutive internal gaps contain complete forests of nested packets. Let Y_j be the ACTUAL chronological product in gap j, and p_j=a1…a_j.
The product of the entire outer interval is EXACTLY

`( product_(j=1..l−1) p_j Y_j p_j^-1 ) · (a1…a_l)`,

where the displayed product over j is in increasing order.
Multiplication telescopes to `a1 Y1 a2 Y2 … a_(l−1)Y_(l−1)a_l`; this is an identity for EVERY group, including l=1 with an empty gap product.

If every packet product is in a normal K, induction makes every Y_j and the outer-interval product belong to K, because conjugates of K remain in K.
But the formula retains conjugations by ACTUAL outer prefixes. Membership in K does not erase them.
Central actual packet products make interval removal transparent as already proved; individual product-one packets make each nested forest1 by Theorem2.
With only an aggregate kernel identity, neither simplification is justified.

For a selected subfamily, outer packets that are NOT selected contribute NO letters to its chronological union. Its forest and actual conjugating prefixes must therefore be formed from the SELECTED family, not frozen from the full family and reused unchanged.
This is an essential selection/coupling dependence, not a degree datum or a freely assigned label.
No claim is made that this exact formula by itself solves the coupled kernel selection problem.

## 9. Scope, original gap and continuation

Paid here: sharp classification for individual packet identities; sharp incidence/centrality classification for aggregate kernel identities; a valid central-ACTUAL-value noncrossing transport lemma with exact n-occurrence caller; complete index-two noncrossing pair existence; and full original-length failure families showing why noncentral coupling cannot be dropped.
These are full written mathematical claims, not hash-only, encoding-only or selected-trial observations.
They might be familiar elementary facts; no novelty/priority/current-literature claim is made.

Still missing: for arbitrary original words in noncentral extensions, a JOINT selection/packet mechanism paying the actual conjugation dependence, or an entirely different proof/actual avoiding word. Ordinary O(K) is insufficient as an automatic uncoupled certificate. The universal all-finite-group O(G) target and the original prime-dihedral actual-word bridge remain unresolved.

Next genuinely admitted step is to test a precisely universal statement about FIXED noncrossing matchings and action-sensitive kernel selection, using the actual forest formula and maintaining original length/cardinality; no selected arithmetic or old source is needed or authorized. If an essential input/method separation cannot be established, that branch must STOP with the exact prerequisite.

All source/provenance/import/assurance limits of v1 remain: only the current S1/S2 and explicitly ordinary group/induction/counting facts; no fresh book-image authentication, old source/candidate/held guidance or scientific program. Same-harness WRITTEN, not Main adoption/formal/kernel/human/configured-family/executable/novelty acceptance.
Every STOP/HOLD/ZERO outside the narrow release, N4UNKNOWN historical actual child exitUNESTABLISHED, aux214STOP and all process findings persist. Same18/new exclusive root/append-only/science deadline2026-10-31T21:23:27.000Z/target20min substantive cadence and honest gaps remain.

**END OF COMPLETE NONCROSSING/CENTRALITY ADDENDUM.**
