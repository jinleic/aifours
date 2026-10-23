# Olson: ZS and the half-range partial theorems — parent verdict v1

Recorded at 2026-10-18T11:18:04-07:00.

**CORRECTNESS-ACCEPTED at the scopes below, with the mandatory textual overlay.** A written partial theorem, not a proof of unrestricted ROT(p), INV*(p) or ordered Olson. No novelty or breakthrough-gate claim; no Lean verification.

## Exact accepted statements
For p≥5 prime, let o_F count the odd blocks in the **maximal cyclic constant reflection-block decomposition**. It is not the number of reflection runs.

- **Lemma ZS.** If1≤k≤(p+1)/2,0≤κ≤k−1 and a sequence Y of2p+2κ−k odd elements of Z_2p has no zero-sum subsequence of length in[2κ+2,2p], there is an odd generator g such that signed coefficients b∈(−p,p] have cost Σ_(b>0)(b−1)+Σ_(b<0)|b|≤k−1. Thus every|b|≤k and E+N≤k−1.
- **ROT-HALF / INV*-HALF.** Every length-(4p−2) avoider with o_F≤(p+1)/2 has all rotations in one nonzero pair {ρ_c,ρ_−c} and constant maximal cyclic reflection runs.
- **OLSON-HALF.** Every word of length4p−1 with o_F≤(p+1)/2 has an identity2p-subword in increasing original index order.
- With the separately accepted [p5/four-block result](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-p5-few-lift-parent-verdict-v1.md), the bound is **o_F≤max(4,(p+1)/2)**. This is a union, not an additional assumption. The p5,o_F4 input remains finite computer-assisted and is not a premise of the new half-range proof.

| p | Previously accepted upper bound on o_F | Accepted bound after union |
|---:|---:|---:|
|5|4|4|
|7|4|4|
|11|5|6|
|13|6|7|
|17|7|9|
|19|8|10|
|23|10|12|
|29|12|15|

## Evidence and proof audit
- [Text of record, proof-ROT-half-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-half-v1.md), SHA256 `3b8fa50e7a15eb58d215568407238e31d78468562be198035d6bf2d00641c738`.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-half-v1-codex-v1.note.md), SHA256 `e8c61273b26a7f449b80519af7fd687a784d7b921f2b53b791245da59fd2c729`: ZS, ROT-HALF, INV*-HALF and OLSON-HALF ACCEPT; one MINOR on the obstruction's scope wording.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-half-v1-claude-v1.note.md), SHA256 `1ac9c06b1c1edc1494c36d7d34f78311344e364944a5f64ef74fbf813310085b`: the same mathematics accepted, no FATAL/MAJOR; textual/citation MINORs disposed below.
- [Review manifest](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-half-v1-review-v1/manifest.json), SHA256 `b24f8455eb9d1f8747b58c2b8b8d5e36c672d3eea415db26269cc1bc7336dfeb`; both reviewers received the same pinned proof and import texts.

Parent read the nine-step proof and the MULT/SHgen hypotheses. A longest zero-sum Z has|Z|≤2κ, while its complementary zero-sum-free Y′ has lengthL≥2p−k and defecte=k−1−2κ+|Z|. MULT gives a generator and complete positive integer subset weights of Y′. A residue of a submultiset U⊆Z in the forbidden middle interval would permit **two separate** completions, for U and Z minus U, whose numerical inequalities force4k≥2p+4; their completion subsequences need not be disjoint. Balancing positive/negative weights in Z and bounding the remaining room in Y′ yield cost≤k−1. The κ0/k1 and half-boundary cases retain the strict integer inequalities.

The new cost bound supplies SHgen(H)/(K) without the old5k≤2p+4 condition. The normal-form and SHgen-E lemmas are accepted here as statements whose proofs require only their displayed hypotheses, **not** that old range: both reviewers checked their supplied proofs for this applicability. Genuine empty-run expansions preserve k/block values and use restricted REFL only on descendants with o_F≤k≤p; no full ROT/INV*/REFL is imported. Restricted REFL is then applied to the **original** word to establish reflection rigidity. Finally the accepted odd-block/rotation deletion argument preserves the needed bound and reconstructs RGR before calling RGR-LONG. No reflection constancy is lifted backwards through PM*.

## Mandatory wording overlay
The frozen v1 source is unchanged. Read it with these dispositions:
1. ZS's proof is complete **modulo MULT and Davenport D(Z_2p)=2p**; MULT is used, not replaced. κ=0 directly makes Y zero-sum-free and Z empty. Inclusion-maximal Z would suffice, although the proof selects maximal length.
2. At the normal-form κ≥0 assertion, insert: ifH≥p, GRX's all-plus pattern with zero selected rotations is already an identity selection. GRX applies also with genuine empty runs.
3. Normal-form/DAV/SHgen-E are used at their actual lemma hypotheses as checked above. Their earlier occurrence in a narrower theorem chain does not impose that theorem's5k bound on the lemmas. All SHgen-E caller obligations, especially o_F≤k≤p throughout induction, are explicitly discharged.
4. State|b|≤k≤p−2 **before** identifying SHgen's weight; x=0 would require b=±p or0 and is excluded.
5. For OLSON-HALF cite OLSON-FEW v3 lines37–46 and the accepted parent deletion argument, not an absent source as a premise.
6. The sequence example at(k,κ)=(p,p−1), Y=g^(2p−1)(3g)^(p−1), refutes extension of the cost conclusion to that **one** parameter pair under ZP (and it also satisfies V). It does not establish an obstruction throughout an interval “near p,” nor show the theorem fails outside its proved range. Additional avoidance information, for example nonconstant-sign GRX patterns, is one possible way forward. No group-word or ordered-Olson counterexample is supplied.
7. KAPPA01 remains an **unaccepted auxiliary candidate**, not an input to this verdict. No wider slice is accepted by referring to it.

## Exercised check and trust boundary
[Independent parent sequence smoke](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-half-parent-smoke-v1/RESULT-v1.json), SHA256 `7cfe1de4256c858f538a6f19ddb844bdd3cfeacc6b2f0e53522ae58529c00d0a`, source `21de5327500f701789212a178066c96d3da8542ec624a4ffec5f7066bc999ab2` and [pre-execution plan](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-half-parent-smoke-v1/PRE-EXEC-v1.json): standard-library raw residue/cardinality DP, no worker imports or symmetry quotient. All4,621 odd multisets atp5,k1..3 andκ0..k−1 were examined; all32 satisfying ZP obeyed the conclusion. Eight tight-family controls attainedk−1 and rejectedk−2; four k=p sequence obstructions satisfied ZP while exceeding the cost bound. This is a bounded aid, **not a premise** of the universal written proof.

Davenport/EGZ, MULT, GRX, PM*, K1, DAV, SHgen/SHgen-E, restricted REFL and RGR-LONG retain their stated imported mathematical foundations; ordinary written/model review is not formal-kernel verification. Priority has not been cleared. The worker's broader proof-ROT-half-v2 is a **separate unreviewed generalization**, not substituted here.

**Still open:** words/avoiders outside the union bound; full inverse normalization; unrestricted dihedral and arbitrary-group ordered Olson. No silent weakening of those targets.
