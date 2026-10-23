# Sun k7: written twin-block and twin-pair subgroup lemmas

Recorded at 2026-10-18T15:10:18-07:00.

**CORRECTNESS-ACCEPTED with the following repairs:** L6 as used, the L5 coset decomposition at subfamily sizes2–5, K7-BLOCK(a)–(d), K7-PAIR(i)–(iii), and P1–P3. These exclude specified subfamilies of K7, not K7 itself. **K7 remains OPEN.** This is not authorization for a generic FH certificate rule or a finite enumeration.

## Frozen sources and independent reviews

- [K7-BLOCK](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/K7-block-lemma-v1.md), SHA256 `93c3cd1f2d0d41b332dc460aab33a6945e77b68202eb9e27f48b58dbd3129db3`.
- [K7-PAIR](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/K7-pair-lemma-v1.md), SHA256 `77ce8b1bd0ad2803fd3d13d09aac03456b60f887b4dd2801e7e0bfcb85b88c3d`.
- [Codex](sun-coset7-k7-blockpair-codex-v1.note.md), SHA256 `35612df43fa80891faac53ab2a9de995de696c9dcc3cd63ae6a9c326b6f86fe8`: L6/BLOCK(a–d)/PAIR(i,ii)/P1 ACCEPT; PAIR(iii),P2,P3 AWF. One MAJOR P2 scope gap plus an inherited COV/Q specification issue, and MINOR import range; no fatal mathematical defect.
- [Claude](sun-coset7-k7-blockpair-claude-v1.note.md), SHA256 `62e142cd7627a8daf7a86240f1c621aad974f9a8e2d46bb4fd5622180c1e0f10`: same mathematical outcomes, 0 FATAL/MAJOR, six MINOR, one advisory and cosmetic findings. Coverage summaries INCONCLUSIVE without companion-lemma acceptance.
- Companion premises are now the exact statements in [the structure verdict](sun-coset7-k7-structure-parent-verdict-v1.md), including the X1 family convention and COV overlay. Both original source files stay unchanged.

## Accepted statements

In class K7, n_i=6r_i with pairwise coprime r_i. U denotes unmarked vertices (n_i=6w_i), M the marked vertices; a twin block is a full α=1 equivalence class inside U.

**BLOCK.** For a twin block B with s≥3, every distinct j,k∈B has U_jU_k=W_B, one subgroup of index6 independent of the pair. The s cosets g_jW_B are distinct and no outside coset g_vU_v meets any of them. Each outsider meets exactly α_vB of the remaining6−s W_B-cosets, hence α_vB≤6−s. Their fibre indices are λ_v=n_vα_vB/6 and obey Sun(t),2≤t≤4. Consequently s≥4 is impossible; s=3 is also impossible when M=∅.

**PAIR.** For a twin pair B={j,k}, W=⟨U_j,U_k⟩ has index m∈{3,6}. If m=3 every outside α_vB lies in{2,4}. If m=6, U_jU_k=W; g_jW and g_kW are distinct, exclusive pair cosets. Every outsider meets α_vB of the other four cosets, with λ_v=n_vα_vB/6 and Sun(t),2≤t≤5, in each fibre.

**P1.** In Q23 with at least two2-classes, every twin pair has m=6 (an outside α=3 rules out m=3).

**P2 (all Q23, including the single2-class).** When M=∅, a Q23 configuration has only singleton twin blocks. The missing single-class branch is repaired below.

**P3.** When M=∅ and every outside α_vB∈{2,4}, at least three outsiders of any twin pair have α_vB=4. This applies to Q24 and the all-2 single-class pattern. In the m=6 branch the stronger conclusion k_4=3 also holds, now explicitly importing accepted Sun(5).

## Parent derivation and repairs

**L6.** X=U_vU_j=U_vU_k is right-invariant under W and left-invariant under U_v, so U_vW=X. Its measure α_vj/6<1 gives W≠G. Since U_j,U_k≤W, m divides6; U_jU_k⊆W gives α_jk/6≤1/m; and [U_v:U_v∩W]=mα_vj/6. No normality.

**L5.** For x∈g_lU_l∩gH, the intersection is x(U_l∩H). Translate by g⁻¹ to obtain disjoint left cosets inside H, of index λ_l=n_lt_l/[G:H]. Every relevant t-piece subfamily obeys accepted Sun(t). This proof needs no least-order frame.

**BLOCK.** A third twin forces m/6 to be a positive integer with m|6, hence m=6. Equal cardinalities give U_jU_k=W. Pairs sharing a vertex give nested index6 subgroups and therefore one common W_B. A block vertex has fibre index w_j, coprime to each outsider's α_vB r_v; Sun(2) forbids their sharing a W_B-coset. Count incidences in the remainder:
- s≥6: no room for seven cosets or the outsider.
- s=5: the two outsiders must be marked with α=1 and coprime fibre indices in the only residual coset, impossible.
- s=4: all local pair gcds≤2, hence capacity≤2 per residual coset. Zero/one marked outsider exceeds total capacity4. With two/three marked outsiders, every feasible incidence placement would require two distinct vertices to carry marker2, impossible.
- s=3,M=∅: outside t-values are2 or3; mixed pairs cannot coexist. A3-piece uses all three residual cosets and forces four such pieces together; otherwise eight2-incidences exceed capacity6.

**PAIR.** If m=2, all outside α=3 and all seven t=1, giving seven pieces in two fibres whose pair gcds equal3; Sun(4) contradicts pigeonhole. If m=3, integrality forces even α≤5, hence{2,4}. If m=6, set equality and Sun(2) prove exclusivity directly; this is not an application of BLOCK's s≥3 theorem to s=2. Up to five outsiders may share a fibre.

**P2 repair (Codex MAJOR / Claude N2).** BLOCK eliminates sizes≥3. For a twin pair in Q23, if m=3 then PAIR(ii) and Q23 force every outside α=2; all seven vertices have t=1,λ=2w. Sun(3) gives at most two pieces in each of three fibres, contradicting7>6. Thus m=6 even in the one2-class case. Now t∈{2,3} outside; with separate capacities2 and3, incidence counting gives5=k_2+k_3≤c_2+c_3≤4. This proves the full stated P2.

**P3/import repair.** Light indices are2w, heavy indices4w. Any triple with two lights is forbidden by Sun(3). At m=3, k_4=0,1,2 respectively yield too many lights, all three fibres blocked by light pairs, or two blocked fibres leaving too few for heavy vertices. At m=6, k_4=0 exceeds light capacity8; k_4=1 or2 leaves at most one light per fibre, below required incidences. Hence k_4≥3 using Sun(3) only. For the additional m=6 conclusion, accepted **Sun(5)** rules out five pieces whose largest pair gcd is4, excluding k_4=4 or5. Declare2≤|T|≤5; the original import list ending at4 was insufficient.

## Remaining review findings

- Explicitly discharge addendum A4: TWIN supplies product-set equality; every possible subgroup index m is handled; domains are actual cosets of W; only imported Sun(t),t≤5, is used. This is written FH-type subgroup reasoning, not a claim that L5/L6 were already on the executable active-rule list. The present verdict accepts these scoped uses and L6's proof, not a generic FH checker.
- TWIN(c) can be dropped from the dependency list: integrality with1≤α≤5 suffices here. TWIN(b,d) remain necessary.
- BLOCK(c)'s t≤6 wording is harmless because it has at most four outsiders; use t≤4 there and t≤5 for PAIR.
- L0.6 is not identified with a Chinese remainder theorem; rename marker products to avoid collision with subgroup index m; write the5-valuation h_i.
- Coverage summaries require the separately accepted Q/Q5/COV statements and X1 convention. Include single-class Q23 among the residual abstract patterns; no claim that an abstract lift satisfies the added subgroup conditions automatically.
- Claude's proposed exclusion of s=3,|M|=1 is not promoted. General marked size3 cases, marked twin-pair cases beyond the stated conclusions and realizability of surviving patterns remain open.

## Verification boundary

Both reviews and the parent derivation are written mathematics. Imports include Sun(2), Zhu's Sun(3)/(4), locally accepted Sun(5), and the accepted K7 structure at precise scope. No fresh enumeration, machine-checking, Lean, human review or priority claim. No process launch is authorized.
