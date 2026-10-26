# Tuscan-2 order11 — exact one-point deletion obstruction candidate v1

Observed clock before creation: **2026-10-23T14:22:30-0700**. Status **CANDIDATE, WRITTEN ONLY, PARTIAL FOR T2(11), NOVELTY_UNCLEAR**. No program, enumeration, solver or executable arithmetic was used. This is not an unrestricted nonexistence theorem for11. The exact unrestricted target remains `selection-v1.md`.

## 1. Purpose and source boundary

A natural construction route is to start with a known even-order Tuscan-2 square, remove one row and remove one symbol from every remaining row, then close each resulting gap. At order12, familiar group-developed Roman/Vatican constructions supply small even-order sources (Ollis2021 describes the classical quotient-triangle framework). This manuscript proves an obstruction to **every abelian group-developed source**, not just to the identity starter or one affine coefficient. It also isolates exact endpoint and group-abelianization constraints for nonabelian sources.

All arguments below are reconstructed here. No claim is made that the deletion obstruction is previously unknown; a bounded keyword screen is not a priority proof. The sum/quotient and group-development ingredients are classical. The old fact that a regular cyclic development of the TARGET odd order cannot work is not counted as this candidate: the present obstruction concerns deletion from an even-order SOURCE.

Terminology: a Tuscan-1 square of order m has m rows, each a permutation of an m-element symbol set, with each ordered distinct pair occurring once as a linear adjacent pair. A Tuscan-2 square additionally has no repeated ordered pair at linear distance2. There is no column-Latin requirement on arbitrary squares. A group-developed source IS column-Latin, but its deletion need not be; no column condition is imposed on the resulting target in the argument.

## 2. Unrestricted endpoint and missing-arc identities

**Lemma 1 (all Tuscan-2 squares).** Let A be a Tuscan-2 square of order n≥3. Every symbol occurs first in exactly one row and last in exactly one row. Exactly n ordered distinct pairs are absent at distance2. If M is the directed graph of these missing pairs, then

- `outdeg_M(a)` equals the number of rows having a in the penultimate position;
- `indeg_M(a)` equals the number of rows having a in the second position.

Consequently M need not be a permutation graph: assuming its indegrees/outdegrees equal1 would silently add an unsupported column-uniformity hypothesis.

*Proof.* A symbol a occurs once in each of n rows. Its number of outgoing adjacent occurrences is n minus its number of last-position occurrences. Complete adjacent-pair coverage makes this n−1, so it is last exactly once. The incoming argument makes it first exactly once. There are n(n−2) distance2 events, all distinct, in a universe of n(n−1) pairs, leaving n missing pairs. The number of outgoing distance2 events from a is n minus its last and penultimate multiplicities, hence `(n−1)−p_a`; complementing in the n−1 available targets gives outdegree p_a. The incoming statement is analogous. ∎

These elementary identities are a calibration, not a claimed solution or novelty. For11 they leave an11-arc defect graph with unknown, not automatically unit, degrees.

## 3. Exact deletion criterion without any group assumption

Let A be a Tuscan-2 square of order m≥4 on X. Fix a symbol s and a row r*. Delete r*, and in each other row delete its occurrence of s without permuting the other entries. The resulting square B has order m−1 on `Y=X\{s}`.

Define the following finite collections of ordered pairs, always requiring endpoints in Y:

- R1: adjacent pairs of the removed row r* which do not involve s.
- N1: for each retained row in which s is internal, the new pair `(predecessor of s, successor of s)` created by closing that gap. N1 is initially a MULTISET, not assumed distinct.
- U2: the set of all original distance2 pairs of A with endpoints in Y.
- R2: original pairs in U2 which occur in r*, together with original pairs in retained rows whose intervening symbol is s.
- N2: for each retained row, the new distance2 pairs obtained from original consecutive four-tuples `(u,s,v,w)` or `(u,v,s,w)`, namely `(u,w)`. Again N2 is initially a multiset.

**Proposition 2 (exact necessary-and-sufficient criterion).** B is Tuscan-2 if and only if

1. N1 equals R1 as a multiset;
2. all members of N2 are distinct;
3. N2 is disjoint from `U2\R2`.

*Proof.* All rows of B remain permutations of Y. Since A covers each adjacent pair once, its original adjacent pairs within Y comprise the entire ordered-pair universe on Y. Of these, only R1 are lost when removing r*: all other finite adjacent pairs survive deletion of s. Closing gaps adds exactly N1. Thus the adjacent multiset of B is `(universe\R1) ⊎ N1`, which covers exactly once precisely when(1) holds.

An original finite distance2 pair remains at distance2 after deletion unless its row was removed or its middle symbol was s. Therefore its surviving set is `U2\R2`. Deletion can create a new distance2 event only when an original length3 gap is shortened by removal of s at one of its two internal positions, exactly the four-tuples defining N2. Thus the distance2 multiset of B is `(U2\R2) ⊎ N2`. The original events were already distinct, so it has no repetitions precisely when(2)–(3) hold. There are no other events, and no wraparound is used. ∎

This criterion is a construction interface, not an existence claim. It accounts for new-new and new-old collisions separately.

## 4. Group-developed source and interior-deletion impossibility

Let G be any finite group of order m≥4 with identity1. Let

`a=(a_0,...,a_(m−1))`

be an ordering of all its elements. Form the m rows

`(g a_0,...,g a_(m−1)),   g∈G`.

Define right quotients

`d_i=a_i^(−1) a_(i+1),  0≤i≤m−2`,

`e_i=a_(i−1)^(−1) a_(i+1)=d_(i−1)d_i,  1≤i≤m−2`.

**Classical group-development criterion.** The square is Tuscan-1 exactly when the d_i enumerate `G\{1}`. It is Tuscan-2 exactly when, in addition, all e_i are distinct. They are necessarily nonidentity because a is an ordering. Indeed, an occurrence of a quotient h in the starter at a given distance develops into exactly all pairs `(u,uh)` once; two occurrences of h repeat those developed pairs. This proves the criterion, without treating the source's name as a proof.

**Theorem 3 (interior deletion never works for a group-developed T2 source).** If one row and one symbol are deleted from such a group-developed Tuscan-2 square and the result is even Tuscan-1, the deleted symbol must be at an endpoint of the deleted row.

*Proof.* Relabel every symbol by left multiplication by the inverse of the removed row's index; this makes the removed row the starter a without changing its position pattern. Write the relabeled deleted symbol as `s=a_k`. For each position i, exactly one row contains s there: its index is `g=s a_i^(−1)`.

Suppose `1≤k≤m−2`. The quotients of the removed row's finite adjacent pairs R1 are

`G\{1,d_(k−1),d_k}`.

The quotients of the new bridges N1 in retained rows are the e_i for `1≤i≤m−2`, except e_k: that one would belong to the removed row. Since the e_i are m−2 distinct members of `G\{1}`, let b be their unique omitted nonidentity element. Thus their bridge-quotient set is

`G\{1,b,e_k}`.

Proposition2(1), necessary even for Tuscan-1, forces these sets equal, so

`{b,e_k}={d_(k−1),d_k}`.

But `e_k=d_(k−1)d_k` equals neither `d_(k−1)` nor d_k: either equality would force the other nonidentity quotient to equal1 by cancellation. Contradiction. All sets have the stated sizes because the source really is Tuscan-2. No commutativity was used. ∎

## 5. Exact endpoint condition and abelian obstruction

If the deleted symbol is the last element of the removed row, reverse all rows to reduce to deletion of its first element. Reversal preserves the Tuscan properties. Having made the removed row the starter, right multiply all symbols by `a_0^(−1)` so that the starter begins at1 and the deleted symbol is1. This operation commutes with the left development. We may therefore assume

`a_0=1`, deleted row index1, deleted symbol1.

Write `v=a_(m−1)` and `u=a_(m−2)`.

**Lemma 4 (endpoint square condition).** If the deletion yields Tuscan-1, then

`u=v²` and `ord(v)>2`.

More precisely, the necessary adjacent-pair multiset equality is

`{(d_(i−1)^(−1),d_i):1≤i≤m−2}`

`= {(a_j,a_(j+1)):1≤j≤m−2}`.

*Proof.* A retained row containing1 at internal position i has index `a_i^(−1)`, and closing its gap creates precisely the pair

`(a_i^(−1)a_(i−1),a_i^(−1)a_(i+1))`

`=(d_(i−1)^(−1),d_i)`.

The finite adjacent pairs lost from the removed row are the pairs in the right-hand collection. Equality follows from Proposition2(1). The left endpoints of the new bridges enumerate

`G\{1,d_(m−2)^(−1)}`,

whereas the left endpoints of the lost pairs enumerate

`G\{1,v}`.

Their equality forces `d_(m−2)^(−1)=v`. Since `d_(m−2)=u^(−1)v`, this is `v^(−1)u=v`, so `u=v²`. If v had order1, it would equal the first starter entry; if it had order2, u would equal that entry. Either contradicts that a is an ordering. ∎

**Theorem 5 (all abelian-developed sources excluded).** For every finite abelian group G of order m≥4, deleting any one row and any one symbol from a group-developed Tuscan-2 square on G can never produce a Tuscan-1 square of order m−1. In particular it cannot produce a Tuscan-2 square. This excludes **every such abelian-developed order12 source**, irrespective of its starter, as a one-point deletion construction for T2(11).

*Proof.* Interior deletion is excluded by Theorem3. Reduce an endpoint deletion as above. Since the adjacent quotients d_i enumerate all nonidentity elements and G is abelian, their product is both

`a_0^(−1)a_(m−1)=v`

(by telescoping, which in fact does not need commutativity) and

`P=product_(g∈G) g`.

Pair each element with its inverse. The only remaining factors are the elements of the elementary abelian2-subgroup `E={g:g²=1}`. Their product has order at most2: coordinatewise, it is1 if E has size1 or size at least4, and its unique nonidentity element if E has size2. Hence v has order at most2, contradicting Lemma4. ∎

This proof needs no classification of finite abelian groups beyond the elementary involution subgroup observation. It is stronger than checking one Williams/finite-field starter, but still only excludes a deletion route, not all Tuscan11 objects.

## 6. Abelianization filter for nonabelian source groups

Let π be the projection to `G/[G,G]`. The same adjacent-quotient telescoping gives, for any possible endpoint deletion,

`π(v)=product_(g∈G) π(g)`.

Indeed the left side is the image of the ordered product of the d_i, and in the abelian quotient that product may be reordered. In addition `ord(v)>2` and the penultimate entry must equal v². These are necessary, not sufficient, conditions.

At order12 this gives the following explicitly scoped route filters using the standard presentations below:

- **A4.** Its abelianization is C3 with kernel the Klein four-group V4. Each quotient element has four preimages, so the displayed product is1. Thus v∈V4 and has order≤2, impossible. Consequently no A4-developed T2 source works by one-point deletion either. The standard fact `[A4,A4]=V4` is a named elementary group import; it is not a formal-kernel claim.
- **Dihedral group D12.** With `r^6=s²=1, srs=r^(−1)`, the commutator subgroup is `<r²>` and the abelianization is C2×C2. Each quotient coset has three elements, and their total product is1. Therefore the only remaining endpoint possibilities are `v=r²,r⁴`; the penultimate entry is the other one. This does NOT prove existence of a suitable starter or deletion.
- **Dicyclic group Dic3.** With `a^6=1, x²=a³, xax^(−1)=a^(−1)`, the commutator subgroup is `<a²>` and the abelianization is C4 generated by π(x), with π(a)=π(x)². Each quotient coset has three elements, so the product of all images is π(x)². Hence v belongs to `{a,a³,a⁵}`. Lemma4 excludes the involution a³, leaving `v=a` or `a⁵`, with penultimate v². Again this is only a necessary route filter.

No assertion that this list classifies every source or every target is needed for the theorem. Any later search over these two presentations would be a proposed bounded ansatz experiment, not an unrestricted nonexistence proof for11.

## 7. Consequence, verification boundary and next mathematical obligation

The unrestricted T2(11) target is **not solved**. We now have a complete written candidate obstruction to an entire tempting even-source deletion family, and an exact all-group interior obstruction/end condition. These results do not justify claiming that ordinary group-development is the only possible construction, that Tuscan11 must have Latin columns, or that its missing-distance2 graph is a1-factor.

A complete positive deletion candidate in a residual nonabelian group must supply an actual ordering a and pass both parts of Proposition2, then the resulting121-entry array must be checked against the original unrestricted definition independently of the group explanation. A bounded failure there is only a route failure/UNKNOWN. An unrestricted negative still needs a theorem or certified complete enumeration over all arrays.

Current checks: author written reconstruction only. Parent and a separate actual in-harness reconstruction at this exact snapshot are required before WRITTEN_CHECKED. No scientific executable, exhaustive group-starter enumeration, mutation battery, Lean, outside-model, expert or human verification occurred. A separate compute proposal, if any, must pin the actual program and exact controls before admission; this manuscript itself grants no GO.
