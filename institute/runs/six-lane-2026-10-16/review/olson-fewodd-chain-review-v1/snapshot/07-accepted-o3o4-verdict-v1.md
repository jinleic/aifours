# Olson rotation: ROT-o3 and ROT-o4 parent verdict v1

Parent at 2026-10-18T05:54:40-07:00. **CORRECTNESS-ACCEPTED** (partial results, not a gate) at the exact scopes below. Nothing here proves full ROT(p), INV*(p), reflection constancy or ordered Olson.

## Accepted statements

- **Theorem ROT-o3** ([proof-ROT-o3-v3.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-o3-v3.md), sha256 `9b0a37dbcb30b9f989c530d74a9106b8ea312072860fae349232492a329b9ab7`). For every **prime** p ≥ 5, every avoider of length 4p−2 over D_2p with exactly three odd maximal constant reflection blocks has all rotation letters in one set {ρ_c, ρ_−c}, c ≠ 0. With the accepted ROT-o2 ([lowodd verdict v2](olson-rotation-lowodd-parent-verdict-v2.md)), the same conclusion holds for every avoider with **at most three** odd maximal constant reflection blocks, for all primes p ≥ 5.
- **Theorem ROT-o4 and Corollary ROT-o≤4**, for primes **p ≥ 7 only**. The reviewed text is [proof-ROT-o4-v2.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-o4-v2.md) (`878fd123cf69941b0e4f0f86e0dde20ab7fb29481c61c30a4b81e8b34fa1e741`); its statement is restated in [proof-ROT-o4-v3.md](../../../../mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-o4-v3.md) (`db4eee8a5a43aee17a4bef38f79792a3488c9c7a4b8de4e6bcaa3e599550148e`). For every prime p ≥ 7:
  - every avoider of length 4p−2 over D_2p with exactly four odd maximal constant reflection blocks has all rotation letters in one {ρ_c, ρ_−c}, c ≠ 0;
  - the same holds with at most four such blocks.
- **Not accepted:** the p = 5 case of ROT-o4. Both families withheld endorsement, because it rests only on an unaudited exhaustive D10 census. v3 §5 now marks it as a separate prior finite claim pending a provenance audit.

## Reviews (two CLI families; advisory)

1. [Codex](olson-rotation-o3o4-codex-v1.note.md), `86061f1c5c9a8fa868a2c0e0584408498ba7b041336de152de2a1f24f78393d9`. ROT-o3: **ACCEPT** (p ≥ 5). ROT-o4: **ACCEPT-WITH-FIXES** for p ≥ 7, with 1 MAJOR (the p = 5 scope) and 1 MINOR (the missing fifth weight-zero multiset). INC, DEL, K2′ and K3′ were re-derived, including the p = 7, #g = 9 exception.
2. [Claude](olson-rotation-o3o4-claude-v1.note.md), `b07fef33bfcb5076388cc32dad027a4b1ba6c712c371899bcf0f575cdf5f2089` (prompt `a4ba3fe1…76b5`, no tools). ROT-o3: **ACCEPT-WITH-FIXES**, 0 FATAL/MAJOR, 9 MINOR. ROT-o4: **ACCEPT-WITH-FIXES** for p ≥ 7 with 9 MINOR; its M1 equals the Codex MAJOR. Every new lemma was re-derived independently.

Both reviews used the same seven-file snapshot (manifest `olson-rotation-o3o4-review-v1/manifest.json`). The parent re-hashed all seven snapshot files against both the manifest and the live sources: all equal.

## Parent dispositions

- **Scope MAJOR (both families):** resolved by restriction. o4-v3's diff from v2 is exactly:
  - restating the theorem and corollary for p ≥ 7;
  - moving p = 5 to an unendorsed §5;
  - listing all five weight-zero multisets and excluding g(−g)(3g)(−3g) by the preceding restriction (the Codex MINOR; Claude o4-m3).

  The parent read the full 65-line diff. No proof step for p ≥ 7 changed.
- **Prime hypothesis (Claude o3-m1):** both theorem statements quantify over primes. INC/K2′ are applied only at prime p, so stating "p prime" in those lemmas is a wording fix. Claude's Z2×Z9 example lies outside the accepted scope.
- **Davenport-alpha citation (Claude o3-m6):** the "parent erratum m4" is pinned in [RUNS verdict L57](olson-runs-parent-verdict-v1.md) (`82adbddd…9237`): N ≤ 4p−1, F ≥ 2, frame at a gap outside I. Both reviewers re-derived the interior-gap instance used here. The GR0 (d) citation is not relied on.
- **DEL statement (Claude o3-m5, o4-m1):** both reviewers checked DEL as used, for o = 3 and o = 4, on non-maximal representations. GRX, PM*, the pairs bound and Davenport-alpha do not use maximality, and o is read on the original maximal blocks.
- **Remaining MINORs** (the vacuous p = 5, e = 3 branch; the inequality chain at p = 5; normalization wording; the superset Y′ list; extraction lines; dropped one-representative remarks): wording and justification only. Both families say the conclusions stand.
- **Finite aids** (o3 §4, o4 §4): unaudited and **not premises**.

Imports, all at their accepted scopes: GRX/PM* and ROT-o2 (lowodd verdict v2), EGZ, the pairs bound, (D)/(Z1)/(Z2), and Davenport-alpha with erratum m4. No circularity was found (01 → 00 → imports). The parent ran no new finite aid for this verdict; acceptance rests on two independent CLI derivations plus the parent pin, diff and interface checks above.

Open in rotation: avoiders with ≥ 5 odd blocks (and = 4 at p = 5). The worker's later SH3±/SHm/ELT0/EXP2/SHROT files (bundle-v1 `d1abdcab…7587`, addendum SHm `ecc91a52…dadb`) are unreviewed and not covered.
