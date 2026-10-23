# Imported results: exact statements, source locations, and where each is used

Line numbers refer to the lane's text extractions: `sources/2607.12933v2.raw.txt` (from the pinned PDF,
SHA-256 2d60d45f…21afe) and `sources/1406.3681v2.layout.txt` (from `sources/1406.3681v2.pdf`, SHA-256 f01b494f…).
"Not consulted" means that the original paper was not opened in this lane; the statement is quoted from the
citing source or is standard.

## I1. Lemma 10 of Ball–Simoens (original: [2, Lemma 13] = Ball–Simoens, "Thirty-six quantum officers are
entangled", arXiv:2603.02334, not consulted)
- Statement (raw.txt:342–344): "If Ψ is a quantum Latin square without entries of weight three or more, then there
  exists a classical quantum Latin square Ψ′ such that whenever Ψ and Φ are orthogonal, Ψ′ and Φ are orthogonal as
  well."
- Properties of the construction, read off from the proof (raw.txt:345–356) and used explicitly: Ψ′ arises by
  finitely many steps; each step picks a support {a,b} and applies one unitary U acting on span{|a⟩,|b⟩} (fixing the
  other basis vectors) to every entry whose support is exactly {a,b}. Hence (i) supp Ψ′(c) ⊆ supp Ψ(c) for every
  cell c; (ii) weight-1 entries, in particular the first row of a standard form, are unchanged up to phase;
  (iii) weights refer to the same fixed basis (the standard-form basis of the reference row).
- Used in: PROOF_PARTIAL Theorem A step 1; Theorem C (passage S → S′, and inside each frame); the definition of the
  classes K2/K3/K4 (README §2: every non-classical square of S′ has a weight-3 entry in the reduction frame).

## I2. Theorem 9 = Shrikhande 1961 ([12]: S. S. Shrikhande, "A note on mutually orthogonal Latin squares",
Sankhyā A 23(2) (1961) 115–116; not consulted)
- Statement as quoted (raw.txt:339–341): "A set of n − 3 MOLS(n) can be extended to a set of n − 1 MOLS(n) if
  n ≠ 4. In particular, a set of n − 2 MOLS(n) can be extended to a set of n − 1 MOLS(n)."
- Used in: Theorem A step 2 (4 MOLS(7) → 6 MOLS(7)); the Theorem-5 control (5 MOLS(7) → 6 MOLS(7)).

## I3. Bose 1938 (R. C. Bose, Sankhyā 3 (1938) 323–338; standard, not consulted)
- Statement used: n − 1 MOLS(n) together with rows and columns are the n + 1 parallel classes of an affine plane of
  order n (and conversely).
- Used in: Theorem A step 2; Theorem B step 2.

## I4. Hall 1953 (M. Hall Jr., Proc. Amer. Math. Soc. 4 (1953) 912–916, uniqueness of the projective plane of
order 7 (57 points); not consulted — bibliographic details from memory, to be checked by the reviewer)
- Statement used: every projective plane of order 7 is PG(2,7). Consequence: every affine plane of order 7 is
  AG(2,7) (an affine plane completes uniquely to a projective plane; PGL(3,7) is transitive on lines).
- Used in: Theorem A step 2 (identifies the completed net with AG(2,7), so Fact (C) applies); Theorem B step 2
  (identifies the 5-net with five classes of AG(2,7), so Fact (L) applies).

## I5. Egan–Wanless 2016 (J. Egan, I. M. Wanless, "Enumeration of MOLS of small order", Math. Comp. 85 (2016)
799–824; arXiv:1406.3681v2 — computer classification, not re-verified)
- Table 5 "Number of reduced sets of k-maxMOLS(n)" (layout.txt:699–721): for n = 7 the only rows are k = 1
  (16765350 reduced sets), k = 2 (341880 reduced sets; 17 isotopism, 11 trisotopism, 5 paratopism classes) and
  k = 6 (120). Table 7 (reduced lists of k-maxMOLS(n), layout.txt:782–804) has the same n = 7 rows (k = 2: 5
  paratopism classes). Table 6 (all reduced sets, layout.txt:742–776): n = 7, k = 2: 342480 reduced sets, 7
  paratopism classes; k = 3: 1200 reduced sets, one class; Table 9 (layout.txt:812) classifies "the 5 sets of
  2-maxMOLS(7)".
- Statement used: there is no maximal set of 3, 4 or 5 MOLS(7); hence every set of 3 MOLS(7) extends to a complete
  set of 6 MOLS(7).
- Used in: Theorem B step 2 ONLY. Answer to the parent's sub-question (i): yes, the classical pair in class K2 can
  be non-extendable — by Table 5, 341880 of the 342480 reduced 2-MOLS(7) are maximal (5 species). The K2 analysis
  does not use this classification: its GENERIC encoding ranges over all pairs of MOLS(7) in standard form.

## Internal computational facts (two implementations each; not imports)
- Fact (C) (Theorem A step 3) and Fact (L) (Theorem B step 3): `code/impl1_incidence.py`, `code/impl2_chart.py`,
  outputs `evidence/impl1.json`, `evidence/impl2.json`.
