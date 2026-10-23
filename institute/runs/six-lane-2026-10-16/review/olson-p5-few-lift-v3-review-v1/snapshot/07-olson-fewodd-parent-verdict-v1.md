# Olson (D_2p) — Corollaries INV*-FEW (a) and OLSON-FEW (a): parent verdict v1 (2026-10-18T08:30:37-07:00)

**Disposition: CORRECTNESS-ACCEPTED, partial result (not a gate).** Correctness only; no novelty, priority or significance claim. Part (b) of each corollary (conditional on SHgen and Lemma SHgen-E) is NOT accepted here; it waits for a targeted check of Lemma SHgen-E against the SHgen proof text.

## Statements accepted (every prime p ≥ 5; D_2p with (v,e)(v′,e′) = (v + e v′, e e′); o_F = number of odd maximal constant reflection blocks in the maximal cyclic decomposition)
- **INV*-FEW (a).** Every avoider w of length 4p − 2 (no identity 2p-subword in increasing index order) with o_F(w) ≤ 3, or with p ≥ 7 and o_F(w) = 4, satisfies INV*: all rotations lie in one pair {ρ_c, ρ_−c}, c ≠ 0, and every maximal cyclic reflection run is constant.
- **OLSON-FEW (a).** Every word w of length 4p − 1 over D_2p with o_F(w) ≤ 3, or with p ≥ 7 and o_F(w) ≤ 4, has an identity 2p-subword in increasing index order. (Ordered Olson holds for this class of words.)

The case p = 5 with o_F = 4 is excluded here (ROT-o4 is accepted only for p ≥ 7); an independent finite verification of that case is in parent replay.

## Texts of record
[proof-OLSON-few-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-OLSON-few-v3.md) `ae151f9b38af60ba3a16b954f470b53976317fede4efddc8181fb98ce18cd66a` (errata of v2 `d19e5a301e1d2dae71dcfa0291118edaa402203e1d62e41c02c88d7c00fa27a1`), [proof-INVstar-few-v3.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-INVstar-few-v3.md) `779218b4a92c29c996172c361052d2ac9c16cbca003f49921af3713b3ca05531` (errata of v2 `e71ece9e559b29b8f9c60b40ec95d37f3e9af7d18459dc5caf05199e590dcd03`). The parent read both v2→v3 diffs: dependency lists, a cyclic-frame sentence in Case 1, a redundancy note in Case 3, and two interface conditions in (b)(i); no statement, hypothesis, range or proof step of part (a) changed.

## Evidence
- Codex `gpt-6.1-sol`: [round C](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-roundC-codex-v1.note.md) `233778ccab9efe4a5d5a346bd5a9c13797a90b969a057906cd7e5506a6a2b581` — INV*-FEW ACCEPT-WITH-FIXES (citation erratum only), OLSON-FEW v1 ACCEPT; [OLSON-FEW v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-olsonfew-v2-codex-v1.note.md) `878d6c804413823f88cfe60c151c1867988f050f01f54a560fc89419579221c7` — ACCEPT 0/0/0 (Case 1 R ≤ 2 by p equal pairs; long-odd-block deletion keeps RGR-ness equivalent and lowers o_F by one; two-rotation deletions and reconstruction; ranges; RGR-LONG lift).
- Claude `claude-opus-5-5`: [few-odd chain](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-fewodd-chain-claude-v1.note.md) `6f130cfeb4417fd708287d406418b4e199e9b3d810ec235e7ac0e6e70e0ffabc` — OLSON-FEW v2 ACCEPT-WITH-FIXES with (a) complete given REFL-few-odd; INV*-FEW v2 ACCEPT-WITH-FIXES; no FATAL/MAJOR; MINORs m1–m5 applied in the v3 errata.
- Imports, all parent-accepted at their stated scopes: ROT-o2, GRX, PM*, K1/K2 ([lowodd verdict v2](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-lowodd-parent-verdict-v2.md)); ROT-o3 (p ≥ 5) and ROT-o4 (p ≥ 7) ([o3/o4 verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-o3o4-parent-verdict-v1.md)); REFL-few-odd ([REFL-few-odd verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-refl-fewodd-parent-verdict-v1.md) `16436c07e2dc1b6b773989b2ff5d05900ea92f8e6c1d681b0c5979673688f1ca`); RGR-LONG(p) ([RUNS/RGR-LONG verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-runs-parent-verdict-v1.md)).

## Boundaries
- Not ordered Olson for D_2p in general: words with more odd blocks (o_F ≥ 4 at p = 5, o_F ≥ 5 at p ≥ 7) are not covered by (a); (b) extends the range to 5·o_F ≤ 2p + 4 only after Lemma SHgen-E is accepted.
- Not INV*(p) for all avoiders, and not the lane's all-groups ordered Olson target.
