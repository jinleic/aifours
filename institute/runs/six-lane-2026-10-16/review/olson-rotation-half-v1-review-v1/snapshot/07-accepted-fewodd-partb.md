# Olson (D_2p) — parent verdict v1 addendum: parts (b) of INV*-FEW and OLSON-FEW (2026-10-18T08:40:55-07:00)

Extends [olson-fewodd-parent-verdict-v1.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-fewodd-parent-verdict-v1.md) (`375c534c3254ed5fe1a5ba0bcae6c86c65ca19529997f9fd322e03eb53d717a8`). **Disposition: CORRECTNESS-ACCEPTED (partial result, not a gate)** for parts (b), now that Lemma SHgen-E is accepted by both CLI families.

## Statements accepted (every prime p ≥ 5)
- **INV*-FEW (b).** Every avoider w of length 4p − 2 with 5·o_F(w) ≤ 2p + 4 satisfies INV*.
- **OLSON-FEW (b).** Every word of length 4p − 1 over D_2p with 5·o_F(w) ≤ 2p + 4 has an identity 2p-subword in increasing index order. Ranges: o_F ≤ 5 at p = 11, 6 at p = 13, 8 at p = 19, 10 at p = 23, about 2p/5 in general (together with part (a): o_F ≤ 3 for p ≥ 5, ≤ 4 for p ≥ 7).

## Chain and evidence (texts of record: current errata versions)
- **Theorem SHgen** [proof-SHgen-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-SHgen-v3.md) `fcbd5a972fdfe64f8b4c1798aef64d75375c334595bae6d400902e04546feb5e` (wording errata of v2 `8fde88c0…d239`): Codex round B ACCEPT ([note](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-roundB-codex-v1.note.md) `b589f97813eb8c6879b6ea4f0f131047be39077a5de853c96b2951545fbbc966`); Claude ACCEPT ([engine review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-engine-claude-v1.note.md) `1f5ebe39e9a88c8a45d8188ed4609112a83b27e58aa8eb175aedc65a4d32290a`).
- **Theorem ROT-FEW and Lemma MULT** [proof-ROT-few-v4.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-few-v4.md) `abd3973cd606fe3acc4d534edba13c45e8bbd3764129eaf1f5ca8c7993b7b521` (wording errata of v3): Codex round B ACCEPT (conditional on SHgen); Claude ACCEPT (every sequence lemma re-derived).
- **Reduction ROT-FEW-E with Lemma SHgen-E** [proof-ROT-few-E-v4.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-few-E-v4.md) `ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f`: Codex round C ACCEPT (v2; checked the expanded word and o_F(u°(h)) = k ≤ p with SHgen-v2 in the packet); Claude ACCEPT for SHgen-E against the SHgen-v3 text and ACCEPT-WITH-FIXES for the file ([targeted review](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-shgenE-targeted-claude-v1.note.md) `6d8257bdb566dc14c03e8068228f30d0d18aa942a36ff44e9df377b980a33def`), MINORs n1–n6 applied in v4. The parent read the v3→v4 diff: wording, citations, and one explicit scope restriction (n2) — SHgen-E now assumes REFL(p) only for words with o_F ≤ k, which REFL-few-odd supplies when k ≤ p; every actual call has k ≤ (2p + 4)/5 ≤ p.
- **INV*-FEW v3 / OLSON-FEW v3** as in verdict v1, with Claude's chain review (m1–m5 applied) and Codex ACCEPT on OLSON-FEW v2.
- Imports at their accepted scopes: REFL-few-odd, ROT-o2/o3/o4, GRX, PM*, K1/K2, Davenport-alpha, EGZ, RGR-LONG.

## Boundaries
- Not full INV*(p) or ordered Olson for D_2p: avoiders with 5·o_F > 2p + 4 (beyond the part (a) ranges) are open.
- KAPPA01 v4 (`416f40ee1ae6e3daae152ecec7d224d17aff506b5476ba91620f5babc833fa91`) and ELT0-FEW v3 are reviewed but not needed for these statements and are not separately accepted here.
- The p = 5, o_F = 4 finite verification remains in independent parent replay; until accepted, part (a) at p = 5 stays at o_F ≤ 3 (part (b) at p = 5 gives 5·o_F ≤ 14, i.e. o_F ≤ 2).
