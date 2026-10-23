# Olson reflection slice — Corollary REFL-few-odd: parent verdict v1 (2026-10-18T07:55:35-07:00)

**Disposition: ACCEPTED (correctness only), conditional on the parent-accepted imports it cites.** No novelty, priority or significance claim. This is a partial result toward INV*(p) / ordered Olson for D_(2p); it is not the lane's target theorem.

## Statement accepted
For prime p ≥ 5, every avoider w0 of length 4p − 2 over D_(2p) whose rotations lie in one pair {ρ_c, ρ_−c}, c ≠ 0, and whose number o_F(w0) of odd maximal CONSTANT reflection blocks (maximal cyclic constant-block decomposition) is at most p, has every maximal cyclic reflection run constant (REFL(p) on o_F ≤ p). Text of record: `mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/proof-REFL-fewodd-r4.md` sha256 `1e447754e8c7238c2a1918254f674cfb9a4889015a845517e3170087f932861d` (errata-only successor of r2 `db16274fffccde41e65025a46c4992bb3c11c26bce9bcc97f5bc3efaae65c2c6`).

## Evidence
- Codex `gpt-6.1-sol`, r2: **ACCEPT 0/0/0** twice, independently — `review/olson-refl-fewodd-r2-codex-v1.note.md` (`56e2127a625cd96ced7c4ea3cab3fbfcd0ef4e53be8be6d05a691a68a3ad4cf7`) and as SOURCE04 of round C, `review/olson-roundC-codex-v1.note.md` (`233778ccab9efe4a5d5a346bd5a9c13797a90b969a057906cd7e5506a6a2b581`). Both re-derived MON (o_F non-increasing under P1–P4 and both normalisations), avoidance preservation through SPEC/GR0/H0, the cyclic/degenerate cases and the terminal identity k = o_F ≤ p.
- Claude `claude-opus-5-5`, r2: **ACCEPT-WITH-FIXES 0/0/9**, all MINOR (citations, scope wording, interface documentation) — `review/olson-refl-fewodd-r2-claude-v1.note.md` (`a02b50736ee0665ba09a3f2cd3e8a3e38f334d9ee02147fa4e714018f1d0560a`). It re-derived MON via o_F = F − 2H and found no counterexample possible.
- Parent check of r2 → r4 (`diff`, 131 lines): errata only. All nine Claude MINORs are applied with fix maps; the statement changes only by the title word "constant" (o_F was already defined on constant blocks), and the proof is unchanged. The interface claim at the ROT-few-E call site is weakened from o_F(u°) = k to o_F(u°) ≤ k (via the merging Remark), which suffices because the corollary needs only o_F ≤ p.
- Imports, all previously parent-accepted at their stated scopes: Theorem RED and K0* (`review/olson-reflection-K0star-RED-parent-verdict-v1.md`), the small-k verdict with its errata binding (`review/olson-reflection-smallk-parent-verdict-v1.md`, `review/olson-reflection-smallk-errata-binding-v1.md`), and through them GRX, PM*, H0, Theorem P, EGZ/AR, Davenport-alpha, Lemma M0, Lemma BC, SING, KB*, CAP, KBH*, K1*, TII, QQ, B0S, MXG.

## Boundaries
- Avoiders with more than p odd constant blocks are not covered.
- Caller-side obligations (recorded in r4 Sec. 4): a caller that rebases Lemma SHgen-E on this corollary must carry k ≤ p through its induction and check condition (d) at the base word at every induction level. Codex round C found these met at the INV*-FEW(b) call site (k ≤ (2p+4)/5 ≤ p); that caller is judged in its own verdict.
