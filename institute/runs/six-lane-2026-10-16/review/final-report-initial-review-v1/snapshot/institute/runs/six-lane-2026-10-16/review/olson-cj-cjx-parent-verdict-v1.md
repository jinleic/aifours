# Olson reflection: B0S-CJ and its strengthened range — parent verdict v1

Recorded at 2026-10-18T10:51:53-07:00.

**CORRECTNESS-ACCEPTED, written partial theorems, with the mandatory corrections below.** Not full REFL(p), INV*(p), ordered Olson, a breakthrough gate, or a novelty claim. No Lean verification.

## Exact setting and accepted scope
Let p≥5 be prime, and let w be a word of length4p−2 over D_2p. Its R≥1 rotations are all equal to one nonidentity rotation, normalized to ρ1 (B=0); F≥1. Every maximal constant reflection block has odd length, and empty intervening rotation runs must be genuine (the adjacent reflection values differ). Let k be the number of these blocks, H=(F−k)/2, κ=p−1−H≥1, and Δ=k−p−κ−1=p+κ−1−R.

For a proper cyclic interval S=[a,b] of runs let O(S)=[b+1,a−1], and m be rotation mass. S is heavy if m(S)≥2Δ−1. It is admissible if m(O(S))≥2Δ−1 and either O(S) has one run, or it has a run x other than its last run for which both m([b+1,x+1]) and m([x,a−1]) are at least2Δ−1. Prefixes/suffixes here are in the linear order of O(S), not a second traversal of the cycle.

- **B0S-CJ:** if R≥4κ+1 and either Δ≤0 or there are two disjoint heavy admissible intervals, w has an increasing-index identity2p-subword.
- **Strengthened B0S-CJ triple-prime:** the same conclusion holds under R≥4κ−4 **and** 2κ≤p−1. Both conditions are retained.
- **Corollary1, corrected:** a partition of the cycle into three **nonempty** consecutive arcs, each of mass≥2Δ−1, supplies two disjoint heavy admissible intervals.
- **Corollary2:** under the respective R hypothesis, there is no avoider if Δ≤1 or p≥κ+5Δ−5. The sufficient shortcut is 4Δ≤2κ+7 under R≥4κ+1, but only 4Δ≤2κ+2 under the strengthened hypothesis. The p≤23 conclusion of the original corollary does **not** transfer wholesale to the strengthened version.

These statements apply to the specified B=0 setting only. RES_<(p) consequences import its accepted normalization into that setting. They do not normalize arbitrary rotations.

## Texts and reviews
- [B0S-CJ r2](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-B0SCJ-r2.md), SHA256 `f90c8b53cfeea9b909266be0b27c3e15a39b400c721cba70af49538dbf92c0ed`.
- [Strengthened r4](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-B0SCJx-r4.md), SHA256 `f2779c243289713b5e8b34a4206379d7054ff8cc8e0b0479893f1d44e189843d`.
- [Base B0S++ r5](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-B0SPP-r5.md), SHA256 `d388d3910ef12aa59c3a12878c578edf1608b444342fb99cc417f271a2a6bd64`, at the imported sections/scopes used by those texts.
- [Codex](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-b0scjx-r3-codex-v1.note.md), SHA256 `c9654ea3dc63c501245d05bb1535938f159edc8810b23eb50c59e80b6c5a4363`: accepts the original CJ and strengthened r3 mathematics with MINOR fixes. The supplied r2/r4 apply those fixes.
- [Claude](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-cj-cjx-corrected-claude-v1.note.md), SHA256 `188e60c6d02c7ba95b41e3cc3b9e651e2cdcd4ae5f43844302b610280dbdd865`: re-derived CJ, the constructive contradiction and strengthened inequalities; 0 FATAL/MAJOR. CJ overall and strengthened theorem ACCEPT-WITH-FIXES. Four numbered MINORs are disposed below.
- [Review snapshot](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-cj-cjx-corrected-review-v1/manifest.json), SHA256 `15e004d49db068d56cc379e7fc99ee2f7d740bb06bddbd4e49a4889349c26111`.

## Mandatory corrections and disposition
Read the immutable texts through this overlay; no certificate or scientific output is changed.

1. **Original Corollary2, p≤23.** Replace the parameter-enumeration justification by this written argument. A violating triple satisfies 3κ+2+Δ≤p≤κ+5Δ−6, so4Δ≥2κ+8. With Δ≤κ−1, this forces κ≥6. Ifκ=6 then Δ=5 and p=25, not prime. Ifκ≥7 then Δ≥6 and p≥29. Thus no such triple has prime p≤23. RES_<(p)'s accepted B=0 setting is an explicit import; k≤p falls into the Δ≤1 branch.
2. **Corollary1.** Insert “nonempty” before “consecutive arcs.” For Δ≥1 positivity already forces nonemptiness; the explicit word is needed in the degenerate Δ≤0 statement.
3. **Strengthened proof, greedy step.** Apply 2|P′|+2≤Φ(P′)≤2κ to P′, yielding |P′|≤κ−1 and hence |P|≤κ after adding one run. Properness also follows from P⊆Z⊊[k]. The omitted possibility of the added run bordering the same interval on both sides would make P=[k], so P⊆Z excludes it. Thus the +1/0/−1 interval-count trichotomy used by the increment lemma is complete.
4. **Strengthened Δ≤0 branch.** Use item5's SIGMA-2P argument followed by item6's rechecked constructive contradiction, not an invocation of the original B0S++ theorem with its stronger R hypothesis. Item7's import list includes those two steps as well as C1/C2/F1/F2.
5. **Remaining notation/status notes.** In CJ's x* argument, “[x*+2,a−1]” means the part of O after x*+1 (empty at the endpoint). For the (29,7,6) remark, the |O|=1 case is impossible since its mass≤1<11. The k=1 example precedes the trivial R≥2p cut and illustrates the common Δ≤0 branch only. Strengthened r4 references to CJ-r1 are read through CJ-r2's errata. Historical “r3/UNREVIEWED” headers do not override the r4 pin and this verdict. The parity observation δ_P≤R is sufficient for L3; no stronger assertion is required.

## Parent checks and trust boundary
Parent read the corrected statements, LemmaCJ and its two outward-growth chains, the complement calculation J=c(X)+c(X^c)≥2J, and the exact C2/greedy bounds against the base definitions. H0's conversion of a selected interval pattern to an ordered identity subword, P0, and the earlier constructive cases retain the scoped imports recorded in the reviewed texts. Both reviewers independently checked the written mathematics; agreement is not a formal-kernel proof.

An additional [exact-integer boundary smoke](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-cj-exact-window-parent-smoke-v1.json), SHA256 `8509bb13bc41c8544e0741bfe81ef5c6693363e0face7a91685cfe30ca685aca`, checked1,103,989 mass triples for primes5..31, including19,386 at R=4κ−4: zero A′ failures and zero B′ failures among1,097,614 applicable triples. This finite aid is **not a premise** of the universal theorems.

Still open: the numerical-condition failures with no separately verified heavy-interval condition; excluded edge cells κ=(p+1)/2, R∈{2p−2,2p−1}; deep IIIa/IIIb below the strengthened range; and B≥1 beyond the accepted small-k regime. No census result is promoted by this verdict.
