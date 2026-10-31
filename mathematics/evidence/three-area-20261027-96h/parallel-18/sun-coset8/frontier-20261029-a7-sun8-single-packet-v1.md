# Sun8 in A7: a self-contained small-simple-group packet

Actual `/bin/date` immediately before this new body: **Thu Oct 29 09:28:13 PDT 2026**. Owner: **MathSun8-2**, math-6. **WRITTEN, with separate author-run exact finite corroboration; UNREVIEWED, UNADOPTED.**

## 0. Exact statement, source order and scope

**Theorem.** For every eight nonempty pairwise-disjoint left cosets g_i H_i in G=A7, there are distinct i,j such that gcd([G:H_i],[G:H_j])≥8. The subgroups may repeat; they need not be maximal or conjugate. No covering hypothesis is imposed.

This proves the eight-coset Sun8 assertion for this one finite simple group. In particular there is no eight-disjoint-coset family with all 28 pairwise index gcds exactly 7. It does **not** exclude seven gcd-7 indices, seven distinct index-7 subgroups or seven disjoint index-7 cosets: those all occur. It is not a theorem for all alternating groups, all simple groups or arbitrary groups.

Read the three complete mandatory overlays, in this order, before any affected antecedent or this successor:

1. `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json`, SHA256 `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`;
2. `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json`, SHA256 `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`;
3. `frontier-20261028-alternating-p7-cardinality-addendum-v1.json`, SHA256 `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`.

All relative filenames here are in this owner's exclusive new-window root. The owner's wide-search preview frontier `frontier-20261028-sun-wide-search-preview-frontier-v1.json`, SHA256 `4ca6a3bb90795334dcd5783463863efe3b194facf1ed92f58f14f44e8689a2e6`, is cited status-only. Every displayed snippet stays NONINPUT. No such snippet is used, reconstructed or searched for.

The author previously wrote A7 material in `frontier-20261028-simple-seven-prime-support-v1.md` (SHA256 `815c9e2374a96858f7bfd609aca9f592f293fb14a1822e774333dc41c4eb2faf`, §3) and `frontier-20261028-alternating-small-written-sun8-v1.md` (SHA256 `cb2c2ae804915798e5545cb4be9432677caac012d5f67f82b114967ba732b6647`, §4). They explain the author's nonblind prior context, not proof premises. This is one consolidated packet for the A7 obligation, not a newly discovered group family or an extra count of a known result. No old review is transferred.

The proof below imports only elementary finite-group/permutation facts: Lagrange, Cauchy, Sylow, orbit-stabilizer and simplicity of A_n for n≥5. The last is the standard elementary alternating-group simplicity theorem, not CFSG. No maximal-subgroup classification, Sun7, R8, descent, Jones, Jordan, Nagura or Lie-type result is used. The written proof does not depend on a computer search.

## 1. Two coset facts

**Lemma 1 (coprime indices).** If U,V≤F are subgroups of a finite group and gcd([F:U],[F:V])=1, then every left coset of U meets every left coset of V.

Let a=[F:U], b=[F:V] and c=[F:U∩V]. Both a and b divide c, while |UV|≤|F| gives c≤ab. Coprimality forces c=ab, whence |UV|=|F| and UV=F. For any x,y∈F, write x^{-1}y=uv with u∈U,v∈V. Then xu=yv^{-1} lies in xU∩yV. Thus disjoint cosets have index gcd at least 2. This argument assumes no normality.

**Lemma 2 (cosets inside one coset).** If yK⊆xL, then K≤L and x^{-1}yK is a left coset of K in L. Indeed x^{-1}y∈L, since y∈yK; multiplying the inclusion x^{-1}yK⊆L by (x^{-1}y)^{-1}∈L gives K≤L. If [F:L]=7 and [F:K]=7a, then [L:K]=a. Simultaneous left translation preserves disjointness.

## 2. Elementary subgroup restrictions in A7

We have |A7|=2520=2^3·3^2·5·7.

**Lemma 3.** There is no subgroup of order 45 in A7.

For a group K of order 45, its Sylow-5 count divides 9 and is 1 modulo 5, hence is 1. Its Sylow-3 count divides 5 and is 1 modulo 3, hence is also 1. The two normal Sylow subgroups commute because their commutator lies in their intersection. An element of order 3 from the Sylow-3 subgroup commutes with an element of order 5, producing an element of order 15. A permutation on seven points cannot have order 15: it would need disjoint cycles of lengths 3 and 5 (or a cycle of length divisible by 15). Thus K does not embed in A7.

**Lemma 4.** There is no subgroup of A7 of order 180 or 90; equivalently there is no subgroup of index 14 or 28. Along with Lemma 3, there is no subgroup of index 7·2^a for a=1,2,3.

Let K have order 180 or 90. Since 7 does not divide |K|, it is not transitive on seven points. If it fixes a point, K≤A6. The respective indices inside A6 are 2 and 4. The coset action would inject the simple group A6 into S2 or S4, impossible since |A6|=360 is larger than both orders. If K fixes no point, its orbit partition is 5+2, 4+3 or 3+2+2. The respective setwise stabilizers inside A7 have orders (5!·2!)/2=120, (4!·3!)/2=72 and (3!·2!·2!)/2=12. Neither 180 nor 90 divides any of these orders. The order-45 case is Lemma 3 and corresponds to index 56.

**Lemma 5.** No proper subgroup K<A7 has order divisible by 35.

Let P be a Sylow-7 subgroup of K. A 7-cycle's normalizer in S7 consists of the affine maps t↦ut+v on F7, of order 42. A primitive multiplier u induces an odd 6-cycle on the six nonzero points, whereas translations are even. Thus N_{A7}(P) has order 21. A7 has 720 seven-cycles and therefore 120 Sylow-7 subgroups. Write h=|K| and t=|N_K(P)|. Then t∈{7,21}, n_7(K)=h/t≤120 and h/t≡1 modulo 7. Also h divides 2520 and 35 divides h.

These integer restrictions give the following complete possibilities: for t=7, h=105 or 840; for t=21, h=315 or 2520. To check the list directly, put d=h/t: for t=7 it is a divisor of 360, a multiple of 5, at most 120 and 1 modulo 7, hence d=15 or 120; for t=21 it is a divisor of 120 with the same conditions, again d=15 or 120. Since K is proper, h=2520 is excluded. The order-840 case has index 3 and would inject simple A7 into S3, impossible.

If h=105, n_7(K)=15 contributes 90 nonidentity elements of order 7. The Sylow-5 count is 1 or 21; the latter would contribute another 84 nonidentity elements of order 5, exceeding |K|. Thus its Sylow-5 subgroup Q is normal. P acts trivially on Q≅C5, since |Aut(C5)|=4 and |P|=7. Their commuting product contains an element of order 35, impossible on seven points.

If h=315, K contains a 7-cycle and is transitive. Its point stabilizer has order 315/7=45, contradicting Lemma 3. All cases are excluded.

**Lemma 6.** Every proper subgroup of A7 has index at least 7, and every index-7 subgroup is a natural point stabilizer.

A subgroup of index m≤6 would give a nontrivial coset action of simple A7 and hence an injection into S_m. But 7 divides |A7| and not m!, impossible. If H has index 7, its order is 360, not divisible by 7, so it is intransitive. If it had no fixed point, the three orbit partitions and orders 120,72,12 from Lemma 4 could not contain it. Hence it fixes a point and, by order equality, is that point's full stabilizer.

## 3. Six index-7 cosets leave one index-7 coset

Put Ω={1,…,7} and P(x,y)={g∈A7:g(x)=y}. By Lemma 6 these are exactly the index-7 left cosets. For two distinct such events, disjointness holds exactly when they have the same source x and different targets, or the same target y and different sources. If both sources and both targets are distinct, extend the prescribed two-point bijection to a permutation; if it is odd, compose with a transposition on two of the other five source points, fixing the two prescribed images. Thus an even extension exists.

Every family of at least three pairwise-disjoint P(x,y) events has a common source or a common target. Indeed if two share a source and different targets, any event disjoint from both must share that source, because it cannot have both different targets. The target version is symmetric. Such a family has at most seven members. For six members with a common source x, the complement is P(x,y_0) for the remaining target; with a common target y, it is P(x_0,y) for the remaining source. In particular the complement of any six disjoint index-7 cosets is itself an index-7 coset.

## 4. Proof of the theorem

Assume eight pairwise-disjoint cosets have all pairwise index gcds at most 7. All subgroups are proper. Write their indices n_i.

First suppose none of the n_i is 7. Then each n_i>7 by Lemma 6 and divides 2520. Every such index has at least one of these five prime pairs in its support:

{2,5}, {3,5}, {2,7}, {3,7}, {5,7}.

Otherwise its support is contained in {2,3}, {5} or {7}. The last two allow only indices 5 or 7, not greater than 7. An index supported on {2,3} leaves a subgroup order divisible by 35, impossible by Lemma 5. Two indices containing the same displayed prime pair have gcd at least 10, contradicting the assumed bound. Their nonempty sets of displayed pairs must therefore be disjoint, permitting at most five indices, not eight. Thus at least one index is 7.

Every other coset must then also have index divisible by 7: an index prime to 7 would force intersection with this coset by Lemma 1. Write n_i=7a_i. The a_i are pairwise coprime divisors of 360. Repeated a_i=1 are explicitly allowed. Since 360 has only the three prime divisors 2,3,5, there are at most three nonunit a_i. If there were three, their nonempty disjoint prime supports would each be a singleton, so one a_i would be 2,4 or 8. Lemma 4 excludes all three corresponding indices. Thus there are at most two nonunit a_i, and at least six indices equal 7.

Seven index-7 cosets would already have total size 7·360=2520, leaving no room for an eighth nonempty disjoint coset. Consequently there are exactly six index-7 cosets. By §3 their complement is xL, where [A7:L]=7. Both remaining cosets lie in xL. By Lemma 2, after the same translation they become disjoint left cosets of subgroups of L, with indices a and b. But gcd(a,b)=1, contradicting Lemma 1 inside L. This proves the theorem. □

**Seven-coset boundary.** For a fixed target y, the seven events P(x,y), x∈Ω, are disjoint and partition A7. Their underlying point stabilizers are distinct, each index is 7 and every pairwise index gcd is 7. The theorem does not erase this boundary or rehabilitate the withdrawn seven-index claim.

## 5. Separate finite corroboration and exact computational boundary

Checker: `frontier-20261029-small-simple-sun8-check-v1.py`, SHA256 `7e36d8e9d55fdfee253cd82a7c3ed8de4cc6b9fd0d89e1bb480d4891cc7e772d`, 287 LF / 12782 bytes. Receipt: `frontier-20261029-small-simple-sun8-check-receipt-v1.json`, SHA256 `4ffb680ef6e14673f7c9e491e0acee94f191cc379dd37d27680b38ab3e2c7cb5`. The single completed run lay between native observations 09:24:08 and 09:25:39 PDT. It used existing NumPy and integer permutation/matrix arithmetic in the author's Python eval kernel, not a solver or external model.

For A7 it computed 2520 elements, 40 subgroup conjugacy classes, 3786 subgroups and 49 index-7 cosets. It enumerated exactly eight feasible eight-index multisets after the elementary disjointness constraints, each of shape (7,7,7,7,7,7,u,v), with (u,v) equal to (21,35), (21,70), (21,140), (21,280), (35,42), (35,126), (35,252) or (35,504). It checked all 98 unordered six-families of disjoint index-7 cosets; every complement is another index-7 coset. The representative order-360 stabilizer has 501 subgroups and no pair of proper subgroups with coprime indices. Thus the reduced exhaustive check also excludes the eight-coset counterconfiguration.

The subgroup enumeration is complete by a generating-list induction, not by assuming a published lattice: start with the trivial subgroup and every cyclic subgroup. For each conjugacy-class representative H and each cyclic subgroup C not contained in H, compute the finite monoid/subgroup generated by H and C, and insert every conjugate whenever its class is new. Any subgroup generated by g_1,…,g_r is reached up to conjugacy by this operation and induction on r. Every stored subgroup's identity, inverse and multiplication closure is checked. All conjugates are expanded, so actual cosets are not replaced by order labels.

This is a **reduction-based exhaustive check**, not a direct scan of every eight-coset subset. It uses the two proved coset lemmas from §1. At the final two-coset stage it checks actual products of all coprime-index subgroup pairs inside representatives of the index-7 stabilizer classes, if such pairs exist. It assumes neither the star description nor the subgroup restrictions in §§2–3; instead it enumerates and checks their relevant finite consequences directly.

Positive controls: the actual seven index-7 cosets partition A7; eight cosets of an index-15 subgroup are accepted when the gcd cap is relaxed to 15. Targeted mutations reject a duplicate coset for `COSET_OVERLAP`, a wrong index for `SIZE_INDEX_MISMATCH`, and the relaxed eight-coset family under cap 7 for `INDEX_GCD_EXCEEDS_CAP`. These are author controls, not another independent implementation.

## 6. Review and nonclaims

A reviewer should reconstruct the elementary subgroup restrictions, especially the Sylow-7 normalizer/count argument and the order-45 obstruction; the prime-pair count; repeated unit cofactors; all index-7 subgroup/coset claims; and the exact subcoset caller into L. The finite checker is corroboration, not a premise of the written proof. No subgroup classification or Sun7/R8 interface is hidden in this packet.

No independent-model-family or human review, Lean/kernel proof, source-priority search, mathematical novelty clearance, parent adoption or arbitrary-group conclusion is claimed. The 09:18 owner cadence PROCESS MAJOR remains as recorded in `checkpoint-20261029-0918-small-simple-work-and-cadence-gap-v1.json`; earlier generic timed-out searches supplied no exclusion evidence. Every prior process finding, quarantine, immutable source and review remains unchanged. The conditional assembly is still UNREVIEWED and is not promoted by this author packet.
