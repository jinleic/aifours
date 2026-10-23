# External sources used by the K1 corollary note (desk fetch; static reviewers cannot access the PDFs)

Fetched read-only into memory by the delegated parent delta check on 2026-10-17 PDT with `source_fetch.py`
(sha256 396a2f31204e98feaae399ae02fb87b37150b4a264a03f69687c68862a1984c4). Text was extracted with
`pdftotext 26.04.0` from stdin; no PDF or text copy was written. The receipt `source_fetch.receipt.json` in this
directory records URL, HTTP status, byte count and SHA-256 of each PDF and short verbatim anchors (each at most 40
whitespace tokens). The extraction renders "≠" as "6=" or "̸=" and "∉" as "∈ /". Everything below that is not an
anchor is a desk paraphrase; treat it as a paraphrase.

| key | arXiv PDF | bytes | sha256 |
|---|---|---|---|
| ZC | Zhang–Cao, Resolvable quantum Latin squares with maximal cardinality, 2608.29201v2 | 226010 | dc525efe0fbde64d8c67972af91b761eac7b0710270b14fc0e43a3434b18ac43 |
| HL | Huang–Li, The Existence of Diagonal Quantum Latin Squares with Maximum Cardinality, 2606.27758v1 | 471299 | dc0264f5ef2c2678de118500ee9c26554394b9d19f3da2dd8e182f84961b8c63 |
| BS36 | Ball–Simoens, Thirty-six quantum officers are entangled, 2603.02334v1 | 414766 | 66e43b924f8e2af79f8401f1b4008ec719c3695a388ebd4728d3e8b634a7ebcd |

## ZC (paraphrase plus receipt anchors)
- Section 1: a QLS(v) is "classical" if all entries are computational-basis vectors. Two unit vectors are identical
  iff they differ by a real phase e^{iθ}. The cardinality c is the number of distinct vectors in the array,
  v ≤ c ≤ v², "non-classical" means c > v, and maximal cardinality means c = v². A transversal is v cells in
  distinct rows and columns whose vectors form an ONB.
- Definition 1.1 (t-RQLS(v)): t families, each of v mutually disjoint transversals, such that any transversal of
  one family meets any transversal of a different family in exactly one cell (anchors `ZC_def_1_1_*`).
- After Definition 1.1, ZC states that Huang–Li's pandiagonal QLS of odd order v is a 2-RQLS(v)
  (anchor `ZC_HL_pandiagonal_is_2RQLS`). Theorem 1.2(3), attributed to Huang–Li, says a maximal-cardinality
  2-RQLS(v) exists for gcd(v,6)=1, v ∉ {5,7,11} (anchor `ZC_thm_1_2_3`).
- Definition 2.1: A and B are orthogonal iff {|a_ij> ⊗ |b_ij>} is an ONB of H_v ⊗ H_v. This is the same product-vector
  orthogonality as Ball–Simoens.
- Lemma 2.2 (anchor `ZC_lemma_2_2_statement`, verbatim): "A is a t-RQLS(v) if and only if there exist t classical
  QLS(v)s, B0, ..., Bt−1, such that A, B0, ..., Bt−1 form a (t + 1)-MOQLS(v)." Its printed proof defines
  |b^(r)_ij> = |k> for (i,j) in T^(r)_k and proves both directions.
- Section 5 (Concluding remarks): maximal-cardinality 2-RQLS(v) is known only for gcd(v,6)=1 with v ∉ {5,7,11},
  or v = n² with n ≥ 6. Existence for the remaining orders is left to be determined
  (anchor `ZC_s5_2RQLS_remaining`).

## HL (paraphrase plus receipt anchors)
- Introduction: cardinality is the number of vectors distinct up to a global phase, and MCQLS(n) means c = n²
  (anchor `HL_cardinality_def`). A transversal of a QLS(n) is n cells with no two in the same row or column whose
  vectors form an ONB (anchor `HL_transversal_def`). PQLS(n) is defined in anchor `HL_PQLS_def`, quoted verbatim:
  "if its main diagonal, anti-diagonal, and all broken diagonals in both directions are each a transversal".
  MCPQLS(n) is a PQLS(n) of maximum cardinality.
- Theorem 2.15: an MCPQLS(v) exists if gcd(·,6)=1 and v ∉ {5,7,11} (anchor `HL_thm_2_15`). Section 5 is titled
  "Conclusion" and contains anchor `HL_s5_MCPQLS7_undetermined`: MCPQLS(5) does not exist, while the existence of
  MCPQLS(7), MCPQLS(11) and MCPQLS(n) with gcd(n,6) ≠ 1 "remains to be determined".

## BS36 (paraphrase plus receipt anchors)
- Section 4.2 is titled "Checking twelve cases" (anchor `BS36_s4_2_heading`). Its Lemma 21 (anchor
  `BS36_lemma_21`) states that 2 MOQLS(6) exist iff some Latin square graph on 6 × 6 vertices has a complement with
  an orthonormal representation in C^6. The preceding Theorem 20 lets one of the two squares be assumed classical.
