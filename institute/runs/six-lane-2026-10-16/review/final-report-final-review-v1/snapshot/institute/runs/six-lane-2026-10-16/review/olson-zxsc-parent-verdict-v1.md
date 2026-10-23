# Olson rotation: SC0 and ZX-SC, parent verdict v1

Recorded at 2026-10-18T13:33:13-07:00.

**CORRECTNESS-ACCEPTED with the mandatory overlay below.** Written partial results relative to the stated classical and parent-accepted imports. No full ROT(p), INV*(p), dihedral ordered Olson or all-groups theorem. No novelty, Lean or human-review claim.

## Frozen texts and reviews

- [ZX-SC v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-ZXSC-v1.md), SHA256 `15958303cffafae29f656f9ab0db0f26df9872415396d19097c07310b92dbb1a`.
- [Codex review](olson-rotation-zxsc-v1-codex-v1.note.md), SHA256 `c3bb6017eab75034f4cb2ef2581af29f6e440600bb1441e4413433c9e56f253c`: SC0, ROT-ZX-SC, INV*-ZX-SC and OLSON-ZX-SC ACCEPT; ZX-SC ACCEPT-WITH-FIXES; 0 FATAL/MAJOR, 1 MINOR. All eight snapshot hashes matched.
- [Claude review](olson-rotation-zxsc-v1-claude-v1.note.md), SHA256 `ebf38a80e9a9ef91a8ae99c690be4f8374fc9120325adebc9b3387b77d8ea715`: SC0 ACCEPT; remaining four statements ACCEPT-WITH-FIXES; 0 FATAL/MAJOR, 8 MINOR.
- [ZX/S1(c) verdict](olson-zx-s1c-parent-verdict-v1.md) and [index-one source record](olson-index-one-primary-statement-parent-v1.md) retain their exact scopes. The index-one theorem is used here over **C_(2p), at length ≥ p+2**, not merely the C_p, length p−1 instance used by S1(d). The recorded general statement covers this instance; its original proof was not read.

## Exact statements accepted

1. **SC0.** For prime p ≥ 5, every zero-sum-free sequence S over C_(2p) of length t ≥ p+1 has a generator g and positive integer coefficients a_i with S = (a_1g)…(a_tg) and Σa_i ≤ 2p−1. If S consists of odd elements, every a_i is odd.
2. **ZX-SC.** Let k, κ be integers, 1 ≤ k ≤ (4p+1)/5, 0 ≤ κ ≤ k−1, 2κ+k ≤ 2p−1, and either κ(k−1) < p or 3(k−1) ≤ 2p−1. If Y consists of 2p+2κ−k odd elements of C_(2p) and every zero-sum has length ≤ 2κ, choose a longest zero-sum Z and the SC0 generator g for Y−Z. Then cost_g(Y) ≤ e = k−1−2κ+|Z| ≤ k−1, every signed odd coefficient satisfies |b_g| ≤ k, positive terms of Z equal g, and E+N = cost_g(Y), using the accepted ZX definitions.
3. **ROT-ZX-SC.** For a length-(4p−2) avoider, if some normal form produced by the accepted process has 2 ≤ k ≤ (4p−1)/5 and κ̂ ∈ {0,1}, the original rotations lie in one nonzero pair {ρ_c,ρ_−c}. The separate k=1 branch is K1.
4. **INV*-ZX-SC.** For every prime p ≥ 5, every length-(4p−2) avoider with **5o_F ≤ 4p−1 and F−o_F ≥ 2p−4** satisfies INV*.
5. **OLSON-ZX-SC.** For every prime p ≥ 5, every length-(4p−1) word over D_(2p) meeting the same two inequalities has an identity 2p-subword in increasing original index order.

Here o_F counts odd maximal cyclic constant reflection blocks; F counts reflections. These are sufficient classes, with no existence assertion for avoiders realizing them. The uniform range beyond 3o_F ≤ 2p+1 is empty for p=5,7; examples are p=11, o_F=8, F≥26; p=13, o_F=10, F≥32; p=19, o_F=14 or15, F≥o_F+34; p=29, o_F=20,…,23, F≥o_F+54.

## Independent parent derivation

The parent read SC0/ZX-SC and re-derived the changed estimates, then read the accepted ZX Steps A–G directly to check every substituted interface.

- **SC0:** s=ΣS is nonzero. Any proper zero-sum in S·(−s) must contain the appended occurrence; its complementary subsequence inside S has sum zero, forcing that complement empty, a contradiction. Thus S·(−s) is minimal of length ≥p+2. Index one supplies positive coefficients summing ord(a); ord(a)>p and ord(a) divides 2p, hence ord(a)=2p. Removing the appended positive coefficient leaves sum ≤2p−1. Odd terms require odd coefficients relative to an odd generator.
- **A′:** D(C_(2p)) gives L≤2p−1, whereas |Z|≤2κ gives L≥2p−k. Integer k≤floor((4p+1)/5)≤p−1 ensures L≥p+1. With e=2p−1−L and e′=W′−L≤e, the number q of nonunit coefficients is ≤e′/2, so m≥L−e′/2 and a_i≤e′+1. Now 5L≥5(2p−k)≥6p−1 is exactly 3e≤2L−2, giving a_i≤m. Also e′<L implies q<m, hence g has the unique largest multiplicity. Odd a_i≤k≤p−1 imply a_i≤p−2. Unit weights and a_i≤m give complete subset weights [0,W′]; SC0 gives W′≤2p−1. W′≥L>p suffices for ZX Step C.
- **B–D:** longest-Z maximality gives |Q|≤|U| whenever U⊆Z and Q⊆Y−Z have equal sums. For positive b≥3, b≤p<W′ supplies a Q of size≥2, contradicting |U|=1. Thus positive Z terms are g. For negative coefficient −β, β≤p−2 independently gives 2p−β≥p+2. Were that weight available in Y−Z, the same singleton exchange would contradict maximality. Thus β≤e−e′. No MULT or old 3k hypothesis is needed in these steps.
- **E:** write Z=g^r T and σ=Σ_Tβ=r+2pt; 2κ<2p implies t≥0. Under 3(k−1)≤2p−1, 2m−2p+1≥2p−1−2e−e′≥e−e′, so the prefix sums of β hit [2p−m,m]. Exchanging that prefix and its complement separately gives 2p≤|Z|<2p. Under the other alternative, σ≤2κ(k−1)<2p immediately forces t=0. Therefore σ=r in both cases.
- **F–G:** a completion of weight 2p−r would force 2p≤|Z|+e′≤2κ+k−1≤2p−2. Hence W′≤2p−1−r and cost=e′+r≤e. Coefficients on Y−Z, positive Z terms and negative terms have absolute values ≤k,1,k−1 respectively; E+N=cost.
- **Word consequences:** κ̂∈{0,1} and 2≤k≤(4p−1)/5 imply every ZX-SC hypothesis. GRX gives (ZP), and integer-domain S1(a) already gives (S1). Integer k≤floor((4p−1)/5)≤p−2 excludes zero rotations. SHgen(H): 2H=2p−2−2κ̂≥2p−4≥k−1≥E. SHgen(K): η≤(k−1)/2 and a_max≤k give 2p−η−a_max−1≥(4p−3k−1)/2≥k. SHgen-E expansions preserve k and the block/empty-run representation; its base words have length4p−2, rotations in a nonzero pair and o_F=k≤p, discharging restricted REFL throughout.
- **Uniform/deletion:** κ(w)≤1 iff F−o_F≥2p−4. Normal form gives κ̂≤κ(w), and GRX gives κ̂≥0 for k≥2. Original-word REFL uses o_F≤(4p−1)/5≤p. The accepted ordered deletion ledger gives (o−1,F−1) or (o or o−2,F), preserving both inequalities. Case1 follows from o≤(4p−1)/5≤2p−3 and its framed equal-pair argument.

## Mandatory overlay and disposition

1. **Integrality** (Codex MINOR, Claude m1): replace the false real inequality (4p+1)/5≤p−1 at p=5 with floor((4p+1)/5)≤p−1. For the theorem use floor((4p−1)/5)≤p−2. At p=5: lemma k≤4, theorem k≤3; p=7: k≤5.
2. **Step E substitution** (m2): explicitly use 3e≤3(k−1)≤2p−1 and 2κ<2p from the new assumptions, not the old 3k≤2p+1 justification. Its window chain requires exactly 3e≤2p−1.
3. **Statement completeness** (m3): include positive Z terms=g and E+N=cost, proved in Steps C/G. D(C_(2p)) supplies e≥0 before SC0.
4. **κ̂≥0 and k=1** (m4): GRX supplies nonnegativity for k≥2; K1 includes the nonzero-pair assertion for k=1.
5. **SHgen-E** (m5): the explicit caller discharge is above; use the generalized [ZS v2 overlay V3](olson-zs-v2-parent-verdict-v1.md).
6. **Imports** (m6): list D(C_(2p)), the general index-one theorem at n=2p, S1(a), normal form/GRX/PM*/K1/DAV, SHgen/SHgen-E, restricted REFL, RGR-LONG and the OLSON case structure with overlay8. These imported proofs are not newly certified.
7. **Deletion inequalities** (m7): o≤(4p−1)/5≤2p−3 and 5o′≤5o≤4p−1.
8. **Scope** (m8): “outside every earlier uniform range,” not “no earlier file covers”: existential terminal criteria can already handle some large-o words. At 3k=2p+2 the second ZX-SC alternative holds for larger κ; the present word theorem does not claim that extension. Any residual requires all admissible normal forms to remain uncovered. The new uniform band is empty at p=5,7.

Claude's final suggestion using η+a_max≤E+2 is **unreviewed and not adopted** here. No finite aid or experimental search result is a premise. This verdict supersedes the candidate's UNREVIEWED labels only at the precise statements above.
