# Direct P7 exclusion for simple groups with at most seven cofactor primes

**Status: WRITTEN, source-conditional, UNREVIEWED.** Let S be a finite nonabelian simple group. If 7 does not divide |S|, or if the integer |S|/7 has at most seven distinct prime divisors, then S admits no **eight pairwise disjoint left cosets** whose subgroup indices have all pairwise gcds exactly 7. This is the direct P7 condition stated in the earlier source cited below; it is not the false assertion that seven subgroup indices of gcd 7 cannot exist. As a separate conditional consequence, if Sun7(S) holds, then Sun8(S) holds for these groups. No infinitude, all-simple, arbitrary-group, novelty, human/formal verification or adoption claim is made.

## 1. Exact source and prior-work boundary

Read in order the complete pre-source overlays `frontier-20261028-alternating-pre-source-arithmetic-correction-v1.json` SHA `6c8f85cf6e22d12026398fe87895e62d773edee701e2f96e82c69ff8cb33d793`, `frontier-20261028-alternating-repeated-unit-fatal-pre-source-v1.json` SHA `bdd6149cf483173cc54a804a4fc468b87fc52087a0d4cff40fb323dcfa018d04`, and `frontier-20261028-alternating-p7-cardinality-addendum-v1.json` SHA `6a9572f4da51f18657bccc1747206648e2ec0d41da16fc7b96f8cf6445748218`. Seven distinct index-7 subgroups do exist in A7 and GL3(2); the false no-seven-index claim remains withdrawn.

- The **definition** of P7 as eight disjoint left cosets with indices 7a_i and pairwise-coprime a_i is §3 of `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/reduction-and-generation-v1.md`, SHA `fa0497ae15bd3c765e05123996e4a94bd8038f2be1488b08dc7111f2fd7602c6`. Its Theorem R8 is earlier work, not a new discovery. Section 5 below independently rechecks its short local Sun7-to-R8 implication at written scope; the historical proof and dependency DAG are not revalidated here.
- Classification of simple groups with an index-7 subgroup is imported from the unreviewed written deduction in `frontier-20261028-simple-index-seven-criterion-v1.md` SHA `01ce8d5fcddecd3941489b92f62ff3a780d214410a3ea044250f238cb063af61`: Jones, arXiv:1209.5169v1, Theorem 1.2(k=0), implies they are A7 or GL3(2). Jones's exact statement and primary bytes are pinned in `frontier-20261028-jones-k0-source-v1.json` SHA `ce6d3b4a032bf9fe04446c87a538d09e012142ef4fbc1e29853a31c29769130a`. The source says its proof uses CFSG; it was not replayed.
- The **GL3(2)** exceptional case imports the self-contained but unreviewed written Fano-plane Sun8 candidate `frontier-20261028-gl32-sun8-geometric-v1.md` SHA `d7c18486c27d7f50d792d57c6ed493f4ceb19c4a8df0c2ff041a59e3ff1c4da0`. This is a proof input, not an adopted theorem. The A7 exceptional case is written separately below. Classical simplicity of A6 and elementary group, Sylow and finite-index facts are also inputs.

No old R8 or normal-section result is presented as a new discovery. The author's nonblind incidental cross-topic display was disclosed separately and is not used. No earlier source, hold or review is changed.

## 2. Nonexceptional simple groups

Assume S has no subgroup of index 7 and suppose for contradiction that eight proper-subgroup indices m_i have every pairwise gcd 7. They can be written m_i=7a_i with pairwise-coprime positive a_i. Since there is no index-7 subgroup, **all a_i>1**; this explicit hypothesis is essential because pairwise-coprime units may repeat. By Lagrange each a_i divides |S|/7, and each has a prime divisor which cannot divide any other a_j. Hence |S|/7 has at least eight distinct prime divisors, contrary to the hypothesis. Coset disjointness is not needed in this nonexceptional case. If 7 does not divide |S| no such index can occur at all.

By the named Jones-based deduction, only S≅A7 or S≅GL3(2) can have an index-7 subgroup. The GL3(2) geometric input excludes even the stronger eight-coset Sun8 counterconfiguration; it still has seven index-7 cosets which partition the group. The next section excludes direct P7 for A7 without assuming Sun7 or using a finite subgroup enumeration.

## 3. The A7 exception

Let G=A7. Its order is 2520=7·360, and 360=2³·3²·5. Suppose eight pairwise disjoint cosets have indices 7a_i with the a_i pairwise coprime. We first show that at most two a_i exceed 1.

If three nonunit a_i existed, their nonempty prime supports would be disjoint subsets of {2,3,5}, so one a_i would be a power of 2. Since it divides 360, that power is 2,4 or 8. There are no A7 subgroups of indices 14,28 or 56: for such a subgroup H, its order 360/a_i is not divisible by 7, so H is intransitive on seven points. An orbit of size u≤3 has a set stabilizer of index binomial(7,u), which must divide 7a_i. For u=2 or 3 this introduces a factor 3 or 5, so u=1 and H lies in a point stabilizer A6 with relative index a_i. The simple group A6 has no subgroup of index 2 or 4 because a faithful coset action would embed it in S2 or S4. It has no subgroup of index 8 either: such a subgroup would have order 45, its number of Sylow-5 subgroups divides 9 and is 1 mod 5, and hence it would normalize a C5. The normalizer of a 5-cycle subgroup in S6 has order 20 and contains an odd permutation, so its intersection with A6 has order 10, which cannot contain a group of order 45.

Thus at least six a_i equal 1. Seven disjoint index-7 cosets cover G, so there cannot be seven together with an eighth. If there are exactly six, every index-7 subgroup H has order 360 and is intransitive on seven points. An orbit of size u≤3 gives binomial(7,u)|7, forcing u=1; H is the corresponding A6 point stabilizer. Each index-7 coset is an event g(p)=q. Since A7 realizes any compatible two-point map, disjoint events share one source or one target; six mutually disjoint events form a star and their complement is one more index-7 coset. Invert all sets first if needed to obtain a left-coset partition. The remaining two cosets are contained in that last coset. Translating it to its subgroup gives two relative subgroup indices a,a' which are coprime, so the relative cosets intersect. This contradiction excludes P7 in A7.

For the coprime-index fact used here, if [K:H] and [K:J] are coprime, then [K:H∩J] is a multiple of their product but at most their product; hence HJ=K and every left H-coset meets every left J-coset. The same elementary fact applies to the translated cosets in a fixed larger coset.

## 4. Direct result and exact limitations

Combining the nonexceptional cofactor bound with the two explicitly treated index-7 exceptions gives the stated direct P7 exclusion. The condition counts **all** distinct primes of |S|/7, including 7 itself if 7² divides |S|. When the count is 8 or larger, the argument gives no conclusion. The existence of seven index-7 cosets in A7 and GL3(2) is consistent with this result: those seven partition the group, so they cannot be extended by an eighth disjoint coset.

## 5. Optional Sun7-to-Sun8 composition

Assume locally Sun7(S): every seven pairwise disjoint cosets in S have a pair of indices with gcd at least 7. Suppose eight disjoint cosets violate Sun8, so all their pairwise index gcds are at most 7; none is 1 by the coprime-index fact. Every seven-subfamily has a pair with gcd exactly 7. Let A be the set of labels whose index is divisible by 7. Every seven-subfamily contains at least two A-labels, so |A|≥3.

If A is proper, take any label j outside A. For every i in A, the indices i and j share a prime in {2,3,5}. Such a prime cannot be shared by two different A-labels, because those two indices also share 7 and would have gcd at least 14. Thus |A|≤3; consequently |A|=3, with the three shared primes 2,3,5. Every outside index must then be divisible by 30. There are five outside labels, two of which have gcd at least 30, contradiction. Hence all eight indices are divisible by 7 and all pairwise gcds equal 7: this is the previously established R8 implication, rechecked here without any claim of new credit. Section 4 excludes it.

The earlier arbitrary-group Sun7 statement was accepted only as a named same-harness written composition in `institute/runs/six-lane-2026-10-18-96h/review/sun7-complete-written-composition-parent-verdict-v1.md`, SHA `94abd506aec9879e294a5eb84129794af0c7ac78917b091d2f2c113d665c34f2`, with its final-report and ledger errata; its full proof DAG is not independently replayed here. Thus any unconditional-looking Sun8 consequence using that statement is conditional on precisely that earlier interface, the named Jones source, and the unreviewed GL3(2) written proof.

## 6. Review obligation

A disjoint attack must verify the Jones k=0 degree-7 case split, the A7 index-14/28/56 obstruction and six-star argument, the complete GL3(2) Fano proof, the cofactor count including possible 7², and the locally stated Sun7-to-R8 implication. Source proof, novelty and all other simple families remain unreplayed/open; no old process finding is rehabilitated.
