# F559 — WRITTEN review of the whole actual AME4455 exclusion

**Reviewer gate:** ReviewF559AmeTwins  
**Disposition:** **SUPPORTED at the exact stated written-mathematical scope; not parent adoption.**  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Overall correctness:** correct  
**Confidence:** 0.97

The frozen candidate supplies a self-contained contradiction for one common complex tensor with three unitary balanced flattenings, support \(48\), exactly \(24\) modulus-one entries, and residual alphabet sizes \((4,4,5,5)\). I reconstructed Sections 2–10, including the full-slice saturation step, both four-party twin exclusions, all six rounding projections, and the final direct common-\(P\) contradiction. The primary exclusion does not depend on Euler–Tarry or another external no-OLS theorem.

## 1. Frozen bindings, coverage, and execution boundary

The following measurements are **parent-attributed**, from the supplied live-metadata record and frozen controls, not child-executed hashes or clocks.

| Artifact | Parent-supplied SHA-256 | Parent-supplied size |
|---|---|---|
| F559 manifest | `78574e45f3517a89ce2f5dbfb405f9e2372d435367e25d91925d6184c3cf3a39` | 7616 bytes; 119 LF |
| F559 freeze receipt | `5de35d5a9d377b7af91405b084edfbc597ef8f7d393b7f335479cc5ce20c349e` | 1948 bytes; 47 LF |
| F559 literal packet | `ca604c97df433a59c5ba026236ea7a6f3681e13ed39c24b30860b6543e4ff010` | 43496 bytes; 892 LF |
| S1: complete f539 candidate | `454a52525b65308d262a181673cb4d43c546347bda338ff47393c89140a62c2e` | 30738 bytes; 858 LF; packet logical lines 1–859 |
| S2: prior regular-subregime disposition | `562a98778d37a4cea3a9bdead0eaad467ee02323932a9b000f21b5a50baf2160` | 6643 bytes; 31 LF |

The supplied parent clock was **2026-10-30T13:16:27-0700 PDT**. It is not asserted to be my native start or completion time.

Before opening the mathematical packet, I read the complete manifest, freeze receipt, parent metadata supply, and all twelve listed permission/status controls, including their endings. I then sent the required **direct pre-body ACK to Main**.

After that ACK, I read the entire literal packet in consecutive exact raw windows of at most twenty LF: \(1\!-\!20,21\!-\!40,\ldots,861\!-\!880,881\!-\!892\). This included S1’s final logical line 859 and S2’s final line 31. Mathematical reconstruction began only after that complete reading.

No source links, sibling reviews, author code, held mathematical payloads, or excluded diagnostic records were followed. Quarantine records were used only for permissions and status; their episodes and consumers remained NONINPUT.

**Scientific code prepared or executed:** none / **NOT RUN**.  
**New privately chosen mathematical instances, parameters, graphs, \(P/E\) fixtures, or probes:** none.  
**External-model CLI, builds, tests, lint, formatters, Git operations, installation, deletion, credentials, or infrastructure changes:** not performed.  
**Working-tree writes and child-native clock/hash commands:** not performed. This complete body is returned for parent materialization.

## 2. Exact reviewed theorem

The reviewed statement is nonexistence of a single tensor
\[
U\in(\mathbb C^6)^{\otimes4}
\]
satisfying all of:

1. \(U^{12\mid34},U^{13\mid24},U^{14\mid23}\) are unitary;
2. \(|\operatorname{supp}U|=48\);
3. exactly \(24\) entries have modulus one;
4. for the residual support \(E\), its coordinate alphabets have sizes \((4,4,5,5)\).

The proof permits arbitrary nonzero complex residual amplitudes. No no-distance-one assumption, equal-modulus assumption, real-sign restriction, independently chosen pair graphs, or separately chosen maximal supports is imported.

All line references below are the packet’s **S1 logical source lines**, unless explicitly marked S2.

## 3. Claim-by-claim reconstruction

### 3.1 Actual common-\(P,E\) interface — SUPPORTED

**Source:** S1 lines 43–109.

Unitarity bounds every entry’s modulus by one. A modulus-one entry exhausts its row and column in every balanced flattening. Thus the \(24\) such entries have injective projections onto each of the six physical pairs.

Removing their rows and columns leaves a \(12\times12\) residual unitary containing exactly \(24\) nonzero entries. A singleton residual row or column would have a modulus-one entry, contrary to its being residual. Every residual row and column therefore has exactly two entries.

Consequently, each actual residual pair projection \(R_{ij}\) has size twelve and every used pair has exactly two \(E\)-extensions. The same maximal support \(P\) projects injectively onto its complement:
\[
\pi_{ij}(P)=[6]^2\setminus R_{ij}.
\]

For a residual symbol \(a\) at party \(i\), its number of residual neighbors at every partner party is
\[
r_i(a)=6-p_i(a),
\]
and its residual slice contains \(2r_i(a)\) words. Hence \(\sum_a r_i(a)=12\). Degree one would force its two residual words to have identical values at all other coordinates, so \(r_i(a)\ge2\).

Finally, two residual rows sharing one column must share their second column: otherwise their inner product has exactly one nonzero term. The residual flattenings therefore decompose into six full nonzero \(2\times2\) unitary blocks.

These conclusions concern the **same tensor and same supports throughout**.

### 3.2 Moment identity, degree bounds, and unique exception — SUPPORTED

**Source:** S1 lines 113–186.

The maximal-position and maximal-pair counts are respectively
\[
\sum_{w\in P}k(w)=60,\qquad
\sum_{w\in P}\binom{k(w)}2=49.
\]
Since
\[
\binom{k}{2}-2k+3
\]
takes the values \(3,1,0,0,1\) for the five possible internal-position counts, the stated identity follows:
\[
3n_0+n_1+n_4=1.
\]

Thus \(n_0=0\), and the one-internal and four-internal regimes are both covered by the argument.

For a fixed internal symbol, counting the other internal coordinates in its maximal words gives the stated equations
\[
\tau+2f-\sigma=8-2r
\]
at a four-symbol party and
\[
\tau+2f-\sigma=7-2r
\]
at a five-symbol party. Because \(\sigma\le1\) and \(\tau,f\ge0\), degrees exceeding four are impossible.

Together with the degree sum and lower bound, this gives exactly the listed possible profiles. A degree-four symbol at a five-symbol party forces \(\sigma=1\). Two different five-symbol parties cannot both obtain this requirement from the single possible one-internal maximal word, since such a word has only one internal position. The “at most one exceptional five-party profile” restriction is therefore justified.

### 3.3 Full-slice twin saturation — SUPPORTED

**Source:** S1 lines 190–259.

Let \(T=V_a\cap V_{a'}\ne\varnothing\). For each other coordinate \(j\), the actual \(ij\mid kl\) block closure forces the partner of every triple in \(T\), under equality of its \(j\)-coordinate, to remain in \(T\).

These are three perfect matchings. Two of their edges cannot coincide: two triples sharing two coordinates, together with their copies at \(a,a'\), would give four extensions of a physical pair. Thus their union is simple and cubic.

Actual row orthogonality supplies
\[
z_v+z_{v'}=0,\qquad
z_v=U_{a,v}\overline{U_{a',v}}\ne0
\]
on every matching edge. An odd cycle would force a nonzero \(z_v\) to equal its negative. The graph is therefore bipartite. Simplicity and degree three require at least three vertices in each part, hence at least six vertices in total.

Since slices have at most eight words, the overlap has size six or eight. The decisive saturation argument is valid: if a slice had eight words but only six in \(T\), each coordinate would already have three values fully used twice within \(T\). Its remaining two triples would both have to use the fourth value at every coordinate, making them identical. That is impossible in a support set.

It follows that
\[
V_a=V_{a'},\qquad r_i(a)=r_i(a')\in\{3,4\}.
\]

This proves full saturation, not merely a large intersection. It also justifies:

- no distance-one pair can vary through a low symbol;
- twin pairs at one coordinate have disjoint symbol pairs;
- a twin component exhausts all words through its two symbols;
- twin components at different coordinates are word-disjoint.

For the last assertion, a word and its two different single-coordinate flips would otherwise give three extensions of the physical pair on the remaining coordinates.

### 3.4 Low-to-low pair lemma and arbitrary-complex obstruction — SUPPORTED

**Source:** S1 lines 263–349.

The proof’s explicit normalized case \(0000,1100\) correctly represents two extensions of a low-to-low pair that differ at both complementary coordinates.

Each low slice has four words and gives a balanced two-pair partition at each remaining coordinate. In the first low slice, the partitions at parties \(1,2\) separate the two displayed words, whereas the party-\(4\) partition joins them. Thus the only possibilities are:

- all three partitions distinct; or
- equal party-\(1\) and party-\(2\) partitions, different from party \(4\).

The second possibility yields a distance-one pair varying through the fixed low party-\(4\) symbol, excluded by full-slice saturation. The symmetric low slice has the same restriction.

The two slices consequently force the six displayed words. Applying actual \(13\mid24\) block closure forces \(1111\) and \(0011\). These are precisely the eight displayed even-parity binary words. For any choice of two coordinate positions, fixing their two values leaves exactly two even-parity completions. Hence these words already exhaust their used physical pairs at **all six projections**, and the displayed matrices are closed blocks of the actual tensor.

For a nonzero complex unitary block, row orthogonality requires
\[
\arg u-\arg v-\arg w+\arg x\equiv\pi\pmod{2\pi}.
\]
The three actual cuts in the candidate therefore give
\[
X-Y\equiv\pi,\quad X-Z\equiv\pi,\quad Y-Z\equiv\pi.
\]
The first minus the second plus the third has left side zero and right side \(\pi\), a contradiction modulo \(2\pi\).

This uses arbitrary complex phases and nonzero amplitudes, not a restriction to real signs. The original two extensions must therefore differ at exactly one complementary coordinate, where the saturation lemma supplies a full twin pair.

### 3.5 Isolation and exclusion of every four-party twin — SUPPORTED

**Source:** S1 lines 353–412.

**Isolation across coordinates.** A twin at a four-symbol party exhausts all words through its two symbols. A twin component at another coordinate must avoid them by component disjointness, but needs at least three neighbors at that four-symbol party. Only two residual symbols remain. This is impossible.

**Two twins at the same four-symbol party.** Their repeated degrees sum to twelve, so both pairs have degree three. At either five-symbol party, every neighbor set is a union of these twin pairs. Its degrees are therefore two or four; five such positive degrees summing to twelve force \((4,2,2,2,2)\). This would make both five-symbol parties exceptional, contradicting the unique-exception restriction.

Thus a four-party twin, if present, would be the tensor’s sole twin pair.

**Degree-four case.** The remaining two symbols at its party are low. At either five-symbol party, the omitted symbol from the twins’ common four-element neighbor set can meet only those two low symbols; it too is low. The resulting low-to-low edge requires a complementary twin, contradicting isolation.

**Degree-three case.** At the other four-symbol party, the omitted symbol \(b\) can meet only the two remaining symbols \(u,v\), so \(b\) is low. At each five-symbol party, the two symbols omitted by the twins are likewise low and adjacent to both \(u,v\).

A low neighbor of \(b\) at either five-symbol party would force either a prohibited other-coordinate twin or the unique twin \(a,a'\), although \(b\) meets neither \(a\) nor \(a'\). Thus both neighbors of \(b\) at each five-symbol party must be high. Both five-symbol parties are ordinary.

Each of \(u,v\) already meets the two omitted low symbols at each five-symbol party and must also have a high neighbor because \((u,b)\), respectively \((v,b)\), is used. Their degrees are at least three and sum to six, so both are three. Each then has only one high neighbor at each remaining party. The two extensions of \((u,b)\) would consequently coincide, contradicting multiplicity two.

This argument does **not** prematurely assume the remaining degrees are three. It derives that fact before using uniqueness of the high neighbors.

Therefore no distance-one pair varies at either four-symbol party, for any listed profile.

### 3.6 Forced five-party graph and four-party profiles — SUPPORTED

**Source:** S1 lines 416–513.

A low-to-low edge in \(R_{34}\) would require a four-party twin and is therefore impossible. An exceptional five-symbol party has only one high symbol, insufficient to provide two distinct neighbors for an opposite low symbol. Both five-symbol parties are ordinary.

Each low symbol then meets both opposite high symbols, exhausting the high degrees:
\[
R_{34}=(L_3\times H_4)\sqcup(H_3\times L_4).
\]

Counting the same residual words in these two sectors gives
\[
x_i(a)=|N_{i4}(a)\cap H_4|,
\qquad
y_i(a)=|N_{i4}(a)\cap L_4|,
\qquad r_i(a)=x_i(a)+y_i(a).
\]

In a low party-\(3\) slice, equality of partitions \(1=4\) or \(2=4\) would produce a prohibited four-party distance-one pair; complete equality would already produce duplicate words. In either remaining partition type, every party-\(i\) neighbor meets both high party-\(4\) values. Hence \(x_i(a)>0\) implies \(x_i(a)=2\). The symmetric argument gives \(y_i(a)>0\Rightarrow y_i(a)=2\).

The sums of both functions are six. Each therefore vanishes on exactly one of the four symbols, and those zero symbols must differ because every residual degree is positive. This yields the distinct symbols \(a_i^X,a_i^Y\), forces both profiles to \((4,4,2,2)\), and proves
\[
N_{i3}(h)=A_i\setminus\{a_i^X\},\qquad
N_{i4}(k)=A_i\setminus\{a_i^Y\}.
\]

No regular-only inequality has been extended to a nonregular slice here.

### 3.7 Forced five-party twins — SUPPORTED

**Source:** S1 lines 517–556.

The low symbol \(a_1^Y\) has low party-\(4\) neighbors. For such a pair, the low-to-low lemma forces a twin at party \(2\) or \(3\). Party \(2\) is excluded, and the sector decomposition places both party-\(3\) values in \(H_3\). Thus the two high party-\(3\) symbols are saturated degree-three twins. The symmetric argument forces the high party-\(4\) twins.

Their two actual components cover \(E\), are disjoint, and each contains twelve words. Each common six-triple slice has a simple cubic bipartite equality graph, hence \(K_{3,3}\). Projection of that slice onto any two of its three coordinates is injective, since otherwise its twin copies would violate physical-pair multiplicity.

### 3.8 Same-\(P,E\) rounding and all six consuming projections — SUPPORTED

**Source:** S1 lines 560–631.

For each actual twin component, selecting the twin label by a bipartition of its equality graph retains one word per triple.

- A pair not containing the twin coordinate has a unique triple and therefore retains exactly one twin copy.
- A pair containing the twin coordinate uses the two triples on an equality-matching edge. Opposite bipartition classes select each twin label once.

The consuming-side dispatch is correct at every physical pair:

| Pair | \(C_3\to F_3\) | \(C_4\to F_4\) |
|---|---|---|
| \(12\) | Injective triple projection \(12\) | Injective triple projection \(12\) |
| \(13\) | Party-\(1\) equality edge | Injective triple projection \(13\) |
| \(14\) | Injective triple projection \(14\) | Party-\(1\) equality edge |
| \(23\) | Party-\(2\) equality edge | Injective triple projection \(23\) |
| \(24\) | Injective triple projection \(24\) | Party-\(2\) equality edge |
| \(34\) | Party-\(4\) equality edge | Party-\(3\) equality edge |

Every used pair already occurs twice within its original component, so the two components cannot share a projected pair without giving four extensions in \(E\). Thus their rounded union \(F\) projects bijectively onto each \(R_{ij}\).

The unchanged \(P\) projects onto the complementary pairs. Consequently \(Q=P\sqcup F\) has thirty-six words and is bijective at all six projections, proving the stated OA reduction. This is a support-selection conclusion; no unproved assertion that the retained amplitudes remain a unitary tensor is required.

### 3.9 Direct common-\(P\) contradiction — SUPPORTED

**Source:** S1 lines 635–704.

This endpoint already follows from Sections 2–7; the rounding and external classical theorem are unnecessary.

Fix party \(1\), with distinct \(a_X,a_Y\). For every \(h\in H_3\), its maximal party-\(1\) partners are
\[
O_1\cup\{a_X\};
\]
for every \(k\in H_4\), they are
\[
O_1\cup\{a_Y\}.
\]
Therefore a maximal word using \((h,k)\in H_3\times H_4\) must have party-\(1\) value in their intersection, namely \(O_1\).

For fixed \(h\), there are exactly three maximal words. Their party-\(4\) values are the two values of \(H_4\) and \(o_4\); their party-\(1\) values are the two values of \(O_1\) and \(a_X\). The two words using \(H_4\) must use distinct values of \(O_1\), by maximal \(13\)-pair injectivity. The remaining word therefore uses \((a_X,o_4)\) at pair \(14\).

Both distinct values \(h\in H_3\) force such a word. They are distinct words with the same \(14\)-pair, contradicting maximal pair injectivity.

This closes the remaining \((D_2,D_2)\) case inside the **same actual \(P\)**.

## 4. Imports and unreviewed matters

**No remaining unpaid mathematical import was identified for the stated whole-\(4455\) theorem.** Its load-bearing steps are reconstructed above from the stated tensor hypotheses, elementary unitary orthogonality, finite counting, and the graph arguments given in the candidate.

S2 was read completely. Its prior adopted scope is only exclusion of the both-four-parties-regular subregime. I did not use its finite-run account or linked reviews as fresh verification, nor promote that disposition itself to whole-\(4455\) authority.

**Optional external theorem: INCONCLUSIVE as an independently reconstructed source proof in this review.** I did not follow or reconstruct the Euler–Tarry/Betten sources in Section 11. They are not needed for the reviewed primary contradiction.

Author execution and access-history statements remain the author’s disclosures; this review does not independently certify unobserved history or cognition.

## 5. Final scope and verdict

**SUPPORTED:** the complete written exclusion of the actual \(q=(4,4,5,5)\), support-\(48\), exactly-\(24\)-maximal-entry stratum, for arbitrary complex residual amplitudes and both maximal-word regimes.

**REFUTED claims:** none identified.

**Not established by this return:** other residual alphabets, other maximal-entry counts, a universal support-\(48\) exclusion, \(N\ge49\), the global AME support minimum, novelty or priority, independent-model-family review, human review, kernel verification, or parent adoption.

**Overall correctness: correct.** No mathematical defect requiring repair was identified in the frozen candidate. The direct common-\(P\) endpoint closes the stated theorem without an external no-OLS premise; the six-projection rounding is separately supported. **Confidence: 0.97.**