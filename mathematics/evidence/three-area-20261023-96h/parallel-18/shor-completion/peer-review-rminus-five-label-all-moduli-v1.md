# Review v89-A — the specified four-syndrome R-minus family, ALL slot moduli

Reviewer owner MathShor / MathShor-2. Actual preceding `/bin/date`: `Sun Oct 25 14:35:33 PDT 2026` (an earlier-observation bound for this write).

## 0. Verdict and exact scope

**0 FATAL / 0 MAJOR / 0 MINOR** at the supplied complete scope.

For EVERY integer slot modulus m>=2 and EVERY arbitrary original-FD subset A of the FOUR specified nonzero syndrome classes, the two constructions (one for m>=3, a DIFFERENT one for m=2) give ONE fixed translation map Phi on all four classes, independent of A, whose restriction to A injects into the ACTUAL baseline removal union R(A). Hence no valid baseline replacement using these four classes and arbitrary actual deletion sets can gain words.

This is the ONE specified literal family, not arbitrary four nonzero syndromes. No older ANY3 verdict is a premise. All30 slots, all26 edges/full neighborhoods, both complete arrays, all ten syndromes and all ten pair comparisons were reconstructed below. No prime-field, linear-subset, full-coset, disjoint-fiber or cardinality-relaxation premise is used.

The original arbitrary-four-family/global problem, T300, and any global guessing-number improvement remain unproved. Slot modulus2 means physical alphabet size8, not physical binary alphabet2. This review is same-harness, same-family written work, not formal/kernel, executable, configured-family, human or novelty acceptance.

## 1. Frozen binding, reading order and exposure

- Manifest `peer-review-wave-eighteen-v89.json`: SHA-256 `49c39b97ed5e86a5da0d62ab80926bebcf444c8e0a1108b8d51affbca47cd600`. Read raw LF1–141, the common rules and COMPLETE v89-A entry.
- Receipt `peer-review-wave-eighteen-v89-packet-receipt-v1.json`: SHA-256 `7f3b9c1335650fa27ba249876ab5711458622559705341e243cc58d7d2f80dca`, read raw LF1–50.
- Own primary checkpoint `primary-continuation-20261025-102319-checkpoint-10-v1.json`, SHA-256 `44d3fdd83a3d7ead4a50799790ac40e8bcbba677133ad6c0c560decfd0cb7135`, actual clock14:31:10, written before any v89 proof reading. It retains the full Shor gap and H* withdrawal.
- Exposure ACK `peer-review-rminus-five-label-all-moduli-ack-v1.json`, SHA-256 `12b14775d62fb11a2748ff9c5a91a164e05ab166021f7a773a86d7ef2375bfe6`, actual clock14:32:18, written BEFORE proofbody.

Mandatory direct reads: v9 raw1–35 FIRST, v10 raw1–31 SECOND, v11 raw1–40 THIRD, then assignment/receipt and ACK. Corrections remain binding and are not backdated.

**Source exposure:** fresh to this guessing-number/syndrome proof family, to my knowledge. Earlier NL242/privacy reviews are different mathematics, not source or verdict credit here. The parent/manifest headlines were exposed. No other review of these candidates, no later critical-pair/forest/star body, and no earlier ANY3 proof body was read.

The single literal part `peer-review-wave-v89-v89-A-part1-v1.md`, SHA-256 `dfe9478a0d333eb4d67235162db2b550364103be2e0d8044aba8382e08798bc9`, 43,767 bytes,521LF, was read RAW at1–130,131–265,266–395,396–521 including the ending. No truncation remained.

| Source | Original LF read | SHA-256 |
|---|---|---|
|S1/v9|1–35 COMPLETE|b7c92143cda18c88c7c56017859ab3c7f08fa92ef3d00fd85ba29f41ac258034|
|S2/v10|1–31 COMPLETE|d61acbf77fefa3a8d55d0cf74e9ebe0b680edb28d273f5b22255d09cbd66aa62|
|S3/v11|1–40 COMPLETE|3ce29e3c49d4789106431978152ffab28a3d14402a748ec3828c825f31c4d9e7|
|S4, m>=3 construction|1–213 COMPLETE|11cfe556730bf64851e925a8ee5ae0dd2f14ac5c4dc05746e00f30224b6aa54b|
|S5, all-moduli/m2 addendum|1–144 COMPLETE|6cba0629c0de586bb313b12e83e39aaae5a4d3cb0ffb78153c6231afab5ac1b2|
|S6, ANY3 parent context|1–25 COMPLETE|08e6ddd52fe748d5f19400ac41f51de456008bacf826e93036c39f37be225b9c|

## 2. The actual26-edge graph, ten triangles and30 slots

The26 edges are exactly

    12 13 14 15 16 17 23 27 29 2-10 34 38 39
    45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10.

Expanding them gives ALL original neighborhoods:

|v|N_v|
|---|---|
|1|2,3,4,5,6,7|
|2|1,3,7,9,10|
|3|1,2,4,8,9|
|4|1,3,5,8,10|
|5|1,4,6,9,10|
|6|1,5,7,8,9|
|7|1,2,6,8,10|
|8|3,4,6,7,9,10|
|9|2,3,5,6,8|
|10|2,4,5,7,8|

The degrees sum to52, so no edge was dropped or added. In particular the EXTRA edge34 (not a side of the ten chosen triangles) is included in BOTH N3 and N4. It is respected in the comparisons below; no reduction to the triangle-edge subgraph occurs.

The triangles are

    T1=123, T2=145, T3=167, T4=239, T5=(2,7,10),
    T6=389, T7=(4,5,10), T8=(4,8,10), T9=569, T10=678.

Each triangle's three sides occur in the edge list. Each vertex has EXACTLY three incident chosen triangles:

|v|Full symbol slot order|
|---|---|
|1|T1,T2,T3|
|2|T1,T4,T5|
|3|T1,T4,T6|
|4|T2,T7,T8|
|5|T2,T7,T9|
|6|T3,T9,T10|
|7|T3,T5,T10|
|8|T6,T8,T10|
|9|T4,T6,T9|
|10|T5,T7,T8|

Thus there are30 distinct slots, three per physical symbol. The physical alphabet is Z_m^3. The constraints sum the three distinct slots of each triangle. C_eta is attainable for every eta: assign two triangle slots freely and determine the third. In particular C_0 has m^20 words; that is a baseline count, not an optimality claim.

## 3. Literal syndrome family and distinctness for every m

In T1,...,T10 order the four rows are

    eta1=(0,0,0,0,1,1,0,1,1,2),
    eta2=(0,1,1,0,1,0,1,2,1,1),
    eta3=(1,0,1,1,1,2,0,0,1,1),
    eta4=(2,2,2,0,1,0,0,0,1,0).

All are nonzero modulo every m>=2 because T5=1. All are mutually distinct even at m2: compare pairs12 at T2,13 at T1,14 at T6,23 at T1,24 at T7,34 at T4. Every listed difference is1 or-1. Hence the class index used by Phi is unique for all m>=2, without relying on2 remaining nonzero.

## 4. Complete m>=3 array and all ten syndrome computations

Use component letters A,...,J for T1,...,T10 ONLY. Vertices1,7,8,9 are0 on ALL five representatives. The six other physical symbols, each in its FULL order from §2, are

|label|2 (A,D,E)|3 (A,D,F)|4 (B,G,H)|5 (B,G,I)|6 (C,I,J)|10 (E,G,H)|
|---|---|---|---|---|---|---|
|0|000|000|000|000|000|000|
|1|(0,0,1)|(0,0,1)|(0,0,2)|000|(0,1,2)|(0,0,-1)|
|2|(0,0,1)|000|(0,0,2)|(1,1,0)|(1,1,1)|000|
|3|(0,0,1)|(1,1,2)|(0,0,2)|000|(1,1,1)|(0,0,-2)|
|4|(2,0,1)|000|(2,0,0)|000|(2,1,0)|000|

Here000 means the full zero triple, not an omitted coordinate. All entries are reduced modulo the SAME m.

I recomputed every triangle value from these slots:

|T|Actual nonzero-coordinate sum|labels1,2,3,4|
|---|---|---|
|T1|2A+3A|(0,0,1,2)|
|T2|4B+5B|(0,1,0,2)|
|T3|6C|(0,1,1,2)|
|T4|2D+3D|(0,0,1,0)|
|T5|2E+10E|(1,1,1,1)|
|T6|3F|(1,0,2,0)|
|T7|4G+5G+10G|(0,1,0,0)|
|T8|4H+10H|(1,2,0,0)|
|T9|5I+6I|(1,1,1,1)|
|T10|6J|(2,1,1,0)|

The T8 integer cancellations are2-1=1 and2-2=0. Reading a label column gives its EXACT eta, not merely the support of the syndrome. No multiplication inverse is used, so composite moduli are included.

## 5. All ten m>=3 comparisons, on that SAME array

For the six pairs among S={0,1,3,4}, every full N6 symbol is0: N6={1,5,7,8,9}, and vertex5 is0 on exactly these S rows. The own6 triples are

    0:000, 1:(0,1,2), 3:(1,1,1), 4:(2,1,0).

For12 and23, full N3 observations agree on rows1,2,3: vertices1,8,9 are0, vertex2 is(0,0,1), and vertex4 is(0,0,2). This includes the observation at4 from the extra edge34. Own3 triples are(0,0,1),000,(1,1,2).

For02 and24, every full N2 symbol is0 on rows0,2,4: N2={1,3,7,9,10}. Own2 triples are000,(0,0,1),(2,0,1).

Thus the complete ten-pair table is

|pair|witness|One nonzero own-component difference|
|---|---|---|
|01|6|I=1|
|03|6|I=1|
|04|6|I=1|
|13|6|C=1|
|14|6|C=2|
|34|6|C=1|
|12|3|F=1|
|23|3|A=1|
|02|2|E=1|
|24|2|A=2|

Every1 is nonzero for all m>=2; every2 is nonzero for every m>=3, prime OR composite. These are exactly the guards needed here. The palette{2,3,6} includes original edge23, so this is not a section that assumes independent witness vertices.

**Historical m2 failure retained.** In this old array, own2 for rows2/4 becomes the same triple(0,0,1), and own6 for rows1/4 becomes the same triple(0,1,0). Hence assigned24 and14 comparisons can fail at m2. This is a construction failure only, not no-globalSECTION or no-Hall evidence.

## 6. The DIFFERENT m2 array and exact original reduced rows

Reduce the SAME four eta rows modulo2:

    eta1=(0,0,0,0,1,1,0,1,1,0),
    eta2=(0,1,1,0,1,0,1,0,1,1),
    eta3=(1,0,1,1,1,0,0,0,1,1),
    eta4=(0,0,0,0,1,0,0,0,1,0).

The new representatives are0 at vertices2,3,5,6,8,10. The other symbols are

|label|1 (T1,T2,T3)|4 (T2,T7,T8)|7 (T3,T5,T10)|9 (T4,T6,T9)|
|---|---|---|---|---|
|0|000|000|000|000|
|1|000|(0,0,1)|(0,1,0)|(0,1,1)|
|2|(0,1,1)|(0,1,0)|(0,1,1)|(0,0,1)|
|3|(1,0,1)|000|(0,1,1)|(1,0,1)|
|4|(0,1,1)|(1,0,0)|(1,1,0)|(0,0,1)|

I recomputed ALL ten syndrome sums:

|T|Actual sum, other slots zero|labels1,2,3,4 in Z2|
|---|---|---|
|T1|1T1|(0,0,1,0)|
|T2|1T2+4T2|(0,1,0,0)|
|T3|1T3+7T3|(0,1,1,0)|
|T4|9T4|(0,0,1,0)|
|T5|7T5|(1,1,1,1)|
|T6|9T6|(1,0,0,0)|
|T7|4T7|(0,1,0,0)|
|T8|4T8|(1,0,0,0)|
|T9|9T9|(1,1,1,1)|
|T10|7T10|(0,1,1,0)|

In row4 the two cancellations T2/T3 are both1+1=0 in Z2. These are exactly the original reduced syndromes, not substituted all-one controls or a relabeled family.

## 7. All ten m2 comparisons; actual d9 collision and24 exception

Here N9={2,3,5,6,8} is0 on ALL FIVE rows. The actual own9/d9 values are

    0:000,
    1:(0,1,1),
    2:(0,0,1),
    3:(1,0,1),
    4:(0,0,1).

Thus every pair except24 is witnessed at9. Explicitly those nine pairs are01,02,03,04,12,13,14,23,34. Their own9 triples differ, while EVERY full observed neighbor symbol agrees.

For24, the actual row difference is

    (b4-b2)_4=(1,1,0),
    (b4-b2)_7=(1,0,1),
    zero at every other physical vertex.

In particular the full N4={1,3,5,8,10} symbols agree and the own4 symbol differs. The extra edge34 is respected because the relative3 symbol is0. Vertices4/7 are indeed nonadjacent in the ORIGINAL graph. The syndrome difference has exactly T2,T3,T7,T10 nonzero, matching the two displayed relative physical tuples. No edge was deleted or physical-neighbor equality weakened.

All ten comparisons therefore belong to this ONE shared m2 array. They are not obtained by transplanting selected rows from the m>=3 array.

## 8. Original decoder and EXACT actual-removal iff

For every vertex v and each of its three triangles, the other two corners are original neighbors of v. Define f_v^0 on the FULL neighbor tuple by putting in each slot minus the sum of the two corresponding other-corner slots. Extra graph neighbors may be ignored by this decoder, but may NOT be ignored in a confusion comparison.

For c in C_m,

    c_v=f_v^0(c_Nv).

For x in C_eta,

    x_v=f_v^0(x_Nv)+d_v(eta),

where d_v is the tuple of the three incident syndrome entries from §2. This uses addition in Z_m only. It proves baseline FD at all ten vertices, for every m.

If c in C_m and x in C_eta agree on the entire N_v observation, their own-symbol difference is EXACTLY d_v(eta). Hence their cross-pair is confusing at v if and only if that ACTUAL tuple is nonzero. Consequently

    R(A) = union_(x in A) union_(v:d_v(eta(x))!=0)
             {c in C_m : c_Nv=x_Nv}

is precisely the compulsory baseline removal union, not a projection cardinality or an assigned partition of fibers.

For actual deletions D subset C_m:

    (C_m minus D) union A is FD
      iff A is FD and R(A) subset D.

Necessity selects any surviving baseline word in the displayed conflict fiber. Sufficiency covers within-baseline, within-A and ALL cross-pairs at ALL vertices; a zero d_v gives no own mismatch at that vertex. Empty fibers and overlapping fibers cause no gap.

## 9. ONE Phi inside the actual union, and nonlinear simultaneous injectivity

For fixed m choose the appropriate shared array and set

    Phi(x)=x-b_i for x in C_etai, i=1,2,3,4.

The distinct syndrome rows make the label unique. The exact syndrome computation puts Phi(x) in the ACTUAL C_m, not an isomorphic abstract output space.

### Actual removal membership

For m>=3 the baseline witnesses are

|i|v_(0i)|b_i,Nv|b_i,v=d_v(etai)|
|---|---|---|---|
|1|6|full zero|(0,1,2)|
|2|2|full zero|(0,0,1)|
|3|6|full zero|(1,1,1)|
|4|6|full zero|(2,1,0)|

For m2, choose9 for ALL four labels, with the four nonzero d9 tuples of §7. Since b_i,Nv=0 and f_v^0(0)=0, each selected d_v equals the actual nonzero own tuple. Therefore

    Phi(x)_Nv=x_Nv,
    Phi(x) in the actual removal fiber of THAT SAME x and v.

So Phi(A) subset R(A) with no assumptions on disjointness or relative sizes of removal fibers.

### Injectivity

Translation is injective within a class, over every Z_m including composites. For different classes i,j, a collision Phi(x)=Phi(y) implies

    x-y=b_i-b_j.

At the already-fixed pair witness in §5 or §7, this gives equality of EVERY full original neighbor symbol but a nonzero own difference. That violates FD of A. Thus the restriction is injective on ANY FD-consistent subset, even if its selections are nonlinear, empty/partial in some classes, or coordinated across all four.

This does not assert injectivity on the unrestricted union of the full classes. That would be false and is not used.

Hence |A|=|Phi(A)|<=|R(A)|. For valid deletions R(A) subset D, and all four nonzero classes are disjoint from C_m, so

    |(C_m minus D) union A|=|C_m|-|D|+|A|<=|C_m|.

This is the claimed family-wide no-gain statement with actual deletions.

## 10. Boundaries, named inputs and assurance

**All-modulus union.** m>=3 and m2 exhaust all m>=2. Only the representatives/witness palette change; the graph, physical slot structure, original reduced syndrome family, FD definition, removal union and original objective remain the same. m2 is physical alphabet8, NOT an alphabet2 guessing statement.

**No hidden transitive proof needed for this scope.** S4 names older interface files at LF211, but the graph/slots, exact arrays, all comparisons, decoder, removal iff and injection were supplied and reconstructed here. S6's older ANY3 author/review bodies were not in this packet and were not read; its verdict is not used to accept the new four-row family. The historical global interval20/3..1847/276, T300, original book/source/novelty assertions and any positive finite witness certification are NOT_RECONSTRUCTED and are not premises of this no-gain proof.

**Remaining original gap.** Arbitrary four nonzero syndromes for all m, arbitrary larger class families/global optimum, or a positive-gain FD trade with its exact removal set. Sections for different selected families cannot be pasted without a new simultaneous proof. General Hall expansion is not equivalent to existence of this translation section.

**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.** The old m2 failure is retained honestly and the new addendum is prospective. No unadmitted arithmetic, no later critical-pair/forest/star theorem, and no executable or triple-witness acceptance has been imported.

This is SAME-HARNESS, SAME-FAMILY, different-domain WRITTEN reconstruction, not formal/kernel, configured-family, human, executable, SOTA or novelty acceptance. Only source reads, metadata and written finite algebra were used; no arithmetic interpreter/program, enumeration, solver, replay, build/lint/test/formatter, nested agent or new GO. Source/author/shared/pinned files are unchanged. The full original Shor primary resumes only after this bounded review is actually returned to the parent.
