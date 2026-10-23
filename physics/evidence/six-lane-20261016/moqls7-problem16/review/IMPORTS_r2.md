# Imports, revision r2 (2026-10-17 PDT) — supersedes IMPORTS.md (pinned, unchanged)

Line numbers: `sources/2607.12933v2.raw.txt`, `sources/1406.3681v2.layout.txt` (lane extractions of the pinned PDFs).

## I1. Ball–Simoens Lemma 10 — used through its printed proof (raw.txt:342–356); verified, not trusted
Statement (raw.txt:342–344): a QLS without entries of weight ≥ 3 has a classical replacement Ψ′ orthogonal to every
square orthogonal to Ψ. Construction (raw.txt:349–352): pick a support {a,b}; apply one unitary U on span{|a⟩,|b⟩}
(fixing the other basis vectors) to every entry whose support is exactly {a,b}; repeat.
Same-or-disjoint step (unstated in the source; F6): if supp Ψ(c) = {a,b}, Ψ(c′) ⊥ Ψ(c) and |supp Ψ(c′)| ≤ 2, then
|supp Ψ(c′) ∩ {a,b}| ≠ 1 (Lemma 2: a single common coordinate gives a nonzero inner product), so supp Ψ(c′) = {a,b}
or is disjoint from {a,b}. This holds for ANY orthogonal pair of the square. Consequences: each row/column is either
untouched or mapped entirely by U (still a QLS); N(Ψ′) ⊆ N(Ψ), so orthogonality to every other square persists in any
order of application; supports only shrink; weight-1 entries (in particular all of row 0) are literally UNCHANGED
(not merely up to phase).

## I2. Egan–Wanless 2016 (Math. Comp. 85, 799–824; arXiv:1406.3681v2) — trusted computer classification
- Table 5 "Number of reduced sets of k-maxMOLS(n)" (layout.txt:699–721; F10 — Table 5, not Table 7, throughout):
  for n = 7 only k = 1, 2 (341880 reduced sets; 17/11/5 classes) and 6 (120) occur; the table covers all
  1 ≤ k < n ≤ 9, so there are no maximal 3-, 4-, 5-MOLS(7).
- Table 6 "Number of reduced sets of k-MOLS(n)" (layout.txt:742–776; includes non-maximal sets per §6,
  layout.txt:732–738): n = 7, k = 3 and k = 4 each form ONE paratopism class (Section 2, layout.txt:121–150: paratopy
  = equivalence of the orthogonal array (r, c, L1, …, Lk) under row, column and within-column symbol permutations,
  i.e. isomorphism of the corresponding nets). With the explicit linear representatives L_a(r,c) = c + a·r
  (a = 1..k) this gives: every 3-MOLS(7) yields a 5-net isomorphic to five direction classes of AG(2,7), every
  4-MOLS(7) a 6-net isomorphic to six (parent bridge: review/moqls7-parent-classification-bridge-v1.md). Paratopy is
  used only on classical incidence nets, never as a quantum isotopy.
- Used in: Theorem A (6-net model, then Fact C) and Theorem B (5-net model, then Fact L).

## I3. Redundant classical route (not needed given I2; originals NOT read)
Shrikhande 1961 (Sankhyā A 23, 115–116; quoted as source Theorem 9, raw.txt:339–341); Bose 1938 (Sankhyā 3,
323–338); M. Hall Jr. 1953 (Proc. AMS 4, 912–916) on the uniqueness of the projective plane of order 7, together with
its 1954 Correction — import boundary: neither the 1953 paper nor the 1954 correction was read in this lane.

## I4. Source definitions and Corollary 7
Ball–Simoens v2 (pinned): QLS/MOQLS/classical definitions (§2.2–2.3), rules #1–#3 (§2.4), Corollary 7 and Example 15
(lower bound M(7) ≥ 2).

## Written lemmas (model-authored, reviewed): Prop 1, Lemmas 2–4, Theorems A, B (PROOF_PARTIAL), Lemma P, (SB2)
(PROOF_CANDIDATE_r2 §2–§3), Facts C and L (two lane implementations: evidence/impl1.json, impl2.json; analytic
proofs by the parent).
