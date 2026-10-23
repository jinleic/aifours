# x1-written disposition v1 — target withdrawn BEFORE derivation (no scope, no proof, no claim)

- **Written:** `/bin/date` read at 2026-10-19T16:23:09-0700, immediately before this exclusive write. Owner SunM13MixedFibres, slot math-1.
- **Target withdrawn:** `RUN/control/mathematics-slot-transition-sun-X1-written-20261019-1615-v1.json`, sha256
  18397f87e0dade910398c5ab9c4c8ddab099e3ca745cbc63a9100594fd082ac2 (first `/bin/date` of this slice: 2026-10-19T16:15:23-0700).
  RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.
- **Reason:** X1 already has a CORRECTNESS-ACCEPTED written, computation-free exclusion,
  `RUN/review/x1-written-parent-verdict-v1.md` (sha256 84d7d8abef60fad092713fbf9530abba03ce0d269eb24a0494ac8d2729d40c4c, recorded
  2026-10-19T01:31:33-0700), so the target's purpose (removing load-bearing StageA computation for K5.3) was already met.
  I reported this to Main; Main then instructed (IRC received after my 16:22:39 `/bin/date` read; exact time unknown):
  do NOT proceed with a second X1 derivation; preserve any written scope as withdrawn-before-derivation; disclose the
  proof-summary exposure; no new X1 writes except disposition/checkpoint.
- **State of this directory:** created empty at about 16:22:39 (that `/bin/date` read immediately followed the mkdir check).
  **No scope file, derivation, proof, package or claim was ever written here**; this file is the only content. Nothing
  in this directory is a mathematical result, candidate or premise.

## Exposure disclosure (everything read or thought for this target)
1. `RUN/review/x1-written-parent-verdict-v1.md` lines 1-29, including its proof-structure summary (line 24: gcds 3/3/6,
   orientation choice alpha_(d1d2)=1, fibre counting with the exclusive fibre removed, D-triangle tau bounds, Step-4
   indicator families) and its overlays (lines 19-20: pairwise left-fibre bound; 1 <= alpha <= g-1).
2. `RUN/review/sun7-stageA-K53-parent-verdict-v1.md` lines 1-24 (sha256 0927a0d445b52f166e7cacdb2ddeb1eb57674b712227dcd0ba76537bf10c822b);
   `RUN/review/sun7-priority-parent-note-v7.md` (sha256 705985d5ec4fecacd24eb2a4a9a4bdf2d9f8c1b83e44b4ba57b2f1a8007c7c40), on parent request.
3. Menon, arXiv:2608.15873v1 HTML (on parent request): abstract; section 1 including Lemma 1.1 (= Margolis-Schnabel
   Lemma 4.6, the alpha table); section 2 (finite-core reduction, alpha definition, product formula, Lemma 2.1); start of
   Theorem 3.1; the tail of the proof of Proposition 4.1; Theorem 4.2 statement and the first lines of its proof;
   sections 5-6, references, appendix. The statement and proof start of Proposition 4.1 were not read.
4. Hashed but NOT read: `RUN/review/x1-written-parent-candidate-v1.md` (09948b0c…25af),
   `RUN/review/x1-written-parent-candidate-v1-clarification-v1.md` (49f956b2…c0a9), the Codex/Claude review files.
5. Unwritten pre-freeze sketch, recorded here only for disclosure: from the pairwise fibre bound, at a D-vertex
   alpha_(d1d2)=1 forces alpha(d,c)=1 for all c; at a C-vertex all-alpha=1 is impossible; with alpha_(d1d2)=1 each C-edge
   alpha lies in {1,3,5} with the prime dividing r1*r2. Not checked, not a claim, not continued.

## Governance
Written mathematics only; no computation, solver, model call, nested agent or source import. The parent-owned K7-NF and
K7 A2 candidates and their reviews are unaffected. Next: park and await the parent's replacement full-Sun(7) composition target.
