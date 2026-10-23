# Olson cycles 5–6 — parent delta check (2026-10-17 PT)

Scope: the review-fix revisions frozen by OlsonRunCount5 after the CLI reviews of [c5](olson-c5-codex-review-v1.note.md) / [c5 Claude](olson-c5-claude-review-v1.note.md) and [c6](olson-c6-codex-review-v1.note.md) / [c6 Claude](olson-c6-claude-review-v1.note.md). The parent compared each revision with its reviewed predecessor by full `diff`; no recomputation was needed.

| Revision | Predecessor | Delta found by the parent | Disposition |
|---|---|---|---|
| `c6/c5-fixes/proof-SEED-r3.md` `474396f2…936e` | c5 `proof-SEED-r2.md` `f04c3bbf…3f91` (Codex ACCEPT, Claude ACCEPT-WITH-FIXES) | Version header; labels (0.1)/(0.2) renamed (ARC)/(CLAIM) with every reference updated; the empty-Z sentence (S1); the IND* special-case sentence restricted (S3); an exact hypothesis ledger replacing Remark (1) (S4); explicit c4→c5 revision citations and the DOB(p) definition (S9); the mutation-control sentence (S10). No theorem statement, hypothesis or proof step changed | Accepted as wording-only; closes Claude c6 target (3), which lacked the predecessor in its packet |
| `c6/c5-fixes/proof-Cplus-r2.md` `00e850cf…48bd3` | c5 `proof-Cplus-r1.md` `d5a1ba78…f4a` | C1 computer-assisted status of Corollary HYP; C2 relaxed-system wording citing the parent raw ordered-product smoke; C3 reconciliation; C4 weakening of (ii+) to n_ev,al ≤ 2(k − kB − 2B) + n_pr − 1 via integrality (|X_o| ≥ 2Δ + s0, s0 ≥ ½ ⇒ |X_o| ≥ 2Δ + 1) | C4 verified by the parent and accepted by both c6 reviews; theorem slightly strengthened |
| `c6/proof-SEEDB-r3.md` `93620654…d62b` | `c6/proof-SEEDB-r2.md` `616e0c4d…c6e4` (both reviews ACCEPT-WITH-FIXES, no mathematical error) | Codex rounding and Claude F3 (integer anti-seed caps and exact y-parity gains); F1 exact open-class accounting; F2 a new written Claim E′ deriving the six exceptional classes, citing Part A, labelled [W+F]; F4–F8 wording; region renamed RB | Accepted. The parent re-derived Claim E′'s case analysis (p = 17: B = 4, kB = 7; p = 13: (6,2), (7,2), (5,3); p = 11: (4,2), (5,2); (13;5,2) is not exceptional because its second inequality holds with equality). Lemmas TS, IS, SL, SCW-B, C0, Theorem SEED-B and Claim E are unchanged |

**Resulting accepted partial statements.**
- Theorem SEED with W-ALL: no word of W(p, kB) is an avoider for every prime p ≥ 5 and every 1 ≤ kB ≤ p − 4. This closes both DOB(p) ends of the B = 1 all-single-letter family.
- Theorem C+: an (H)-conditional extension. Corollary HYP covers the seven sample words with computer-certified hypotheses.
- Theorem SEED-B: every all-single-letter word with B ≥ 2 anti runs at any positions, kB ≥ 1 and 2B + kB ≤ p − 2 has an identity 2p-subword, for every prime p ≥ 19. At p = 11, 13 and 17 this holds except for six classes whose exclusion is computer-assisted only.

**Still open in RUNS item (iii):** all words with excess; all-single-letter classes with B ≥ 2 and 2B + kB ≥ p − 1. On the PAR side, the reviewed MIX_low partial result leaves R***. No PAR, RUNS, INV* or full dihedral ordered-Olson theorem follows. The parent's raw ordered-product check is finite smoke only.
