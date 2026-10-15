# Primary sources and exact prior-art comparison

Screened 2026-10-14 PT. Status: **Question 3 is solved by prior work.** No originality claim is made for the seven trialgebra rules, their leading terms, the normal forms, or their Schröder enumeration. The earlier scout's search miss is superseded by a direct primary-source recovery, not treated as evidence of openness.

All eight PDFs and `pdftotext -layout` text snapshots are retained in this directory. Their source URLs, byte lengths and SHA-256 hashes are in [source-downloads.json](../evidence/source-downloads.json). Relevant formulas were checked against [the book image](../source/page-099.png) and [the published lemma image](lemma-29.png), rather than inferred from damaged symbol extraction.

## Decisive matching theorem

**Fatemeh Bagherzadeh, Murray Bremner, Sara Madariaga, “Jordan trialgebras and post-Jordan algebras,” Journal of Algebra 486 (2017), 360–395.** DOI [10.1016/j.jalgebra.2017.04.022](https://doi.org/10.1016/j.jalgebra.2017.04.022); [arXiv:1611.01214](https://arxiv.org/abs/1611.01214); [author-institution PDF](https://investigacion.unirioja.es/documentos/5bbc6a21b750603269e8279e/f/6225f36b5fa07802f2a54cbc.pdf).

- **Read:** Definition 3.1, §6.1 and Lemma 6.1 (journal p. 388; PDF p. 29), plus field/operad conventions in §§1.2 and 2.1–2.3.
- **Exact match:** their `prec`, `succ`, `curlywedge` are the book's `prec`, `succ`, `dot`. Their Lemma 6.1 displays precisely the seven oriented polynomials reproduced in [proof.md §1](../proof.md#1-exact-scope-and-seven-rules), with order `curlywedge < prec < succ`. No additional higher relation is needed.
- **Noncommutative scope:** Definition 3.1 imposes the seven tridendriform identities, not commutativity. The paper distinguishes the separate commutative variety. Symmetrization of the nonsymmetric operad permits arbitrary permutations of input variables; it does not impose symmetry on any operation.
- **Source wording hazard:** the sentence immediately before Lemma 6.1 calls `curlywedge` a “commutative operation.” This conflicts with Definition 3.1 and the paper's stated operations “with no symmetry.” We do not adopt that sentence as a hypothesis. The integral critical-pair calculation independently confirms the same basis without commutativity. Likewise, we do not use the swapped relation counts in the introductory overview as an encoding authority.
- **Characteristic audit:** §1.2 uses characteristic zero unless otherwise stated. Our all-characteristic statement is supported separately by the integral, monic reduction proof, not by silently extending that convention. No division or symmetric-group semisimplicity occurs.
- **Proof detail audit:** the lemma's printed proof cites general operadic GS machinery and comparable computations rather than listing its critical reductions. This dossier supplies all fifteen symbolic reductions and a written all-arity bridge, so it does not rely only on that brief proof paragraph.

**Conclusion:** the proposed candidate is not a surviving open problem. It was explicitly answered no later than this 2017 publication (preprint submitted in November 2016). This is not a claim that this was the earliest possible source.

## All requested baseline sources

| Primary source | Passages checked | What it does and does not supply |
|---|---|---|
| Dotsenko–Khoroshkin, “Gröbner bases for operads,” [arXiv:0812.4069](https://arxiv.org/abs/0812.4069), Duke Math. J. 153 (2010), 363–396 | §3.2.1, Propositions 4–5; §3.6 diamond criterion; example sections screened | Graded path-lex admissibility and operadic GS/diamond machinery. No trialgebra-specific basis was located in this paper. Its characteristic-zero convention is not used to justify positive-characteristic conclusions. |
| Dotsenko–Khoroshkin, “Quillen homology for operads via Gröbner bases,” [arXiv:1203.5053](https://arxiv.org/abs/1203.5053) | Introduction, §1 conventions, §5.3 and Proposition 5.6 | Monomial replacement/resolutions and GS bases for Rota–Baxter operads. Not the decisive trialgebra theorem; a Rota–Baxter embedding alone is not automatically a trialgebra GS basis. |
| Loday–Ronco, “Trialgebras and families of polytopes,” [math/0205043](https://arxiv.org/abs/math/0205043), Contemp. Math. 346 (2004), 369–398 | §2.1 identities; §2.4 trees; Theorem 2.6, Lemmas 2.7–2.8 and Corollary 2.9 | Explicit free noncommutative trialgebra on `V`, with basis `T_n tensor V^(tensor n)`. `T_n` has n+1 leaves, all internal arities at least two, not merely binary trees. Arbitrary field `K`; no finite-generator restriction. This gives an independent all-arity dimension comparison, not a dimension-prefix conjecture. |
| Vallette, “Manin products, Koszul duality, Loday algebras and Deligne conjecture,” [math/0609002](https://arxiv.org/abs/math/0609002), J. reine angew. Math. 620 (2008), 105–164 | §5.7, especially Theorem 54 | Trialgebra-family Koszulness over the integers via partition-poset methods. Koszulness by itself is not an explicit GS basis, and no such implication is used here. |
| Bremner–Dotsenko, *Algebraic Operads: An Algorithmic Companion* (2016), [author-hosted final draft](https://irma.math.unistra.fr/~dotsenko/AlgebraicOperadsAnAlgorithmicCompanion.pdf) | Lemma 3.4.1.4; Proposition 3.4.1.6; §3.5.1; §3.7; Exercise 3.10 | Full path-order and nonsymmetric diamond theory, algebra normal-form translation; trialgebra basis appears as Exercise 3.10. The exercise is not evidence that the task remained research-open in 2026. The draft was fully accessible in this round. |
| Madariaga, “Gröbner–Shirshov bases for the non-symmetric operads of dendriform algebras and quadri-algebras,” [arXiv:1304.5184](https://arxiv.org/abs/1304.5184) | §1 order definition, §2.1, Theorem 1 and Remark 2 | The dialgebra half: the three defining relations form the reduced quadratic basis for `prec < succ`. Normal left growth is only `succ` over `prec`. Its own field convention is characteristic zero; its trialgebra mention is background, not a trialgebra theorem. |
| Chen–Wang, “Gröbner–Shirshov Bases and Hilbert Series of Free Dendriform Algebras,” [arXiv:1009.0185](https://arxiv.org/abs/1009.0185), Southeast Asian Bull. Math. 34 (2010), 639–650 | Definition 2.1, normal L-words, §3 Theorem 3.2 and corollary | Earlier explicit free-dialgebra GS basis as a quotient of a free L-algebra over a field `k`. It uses a different ambient/order convention; no contradiction with Madariaga's shorter operadic basis. |

## Current literature search and scope exclusions

Queries included `tridendriform Gröbner basis`, `dendriform trialgebra Groebner`, and the exact title `Jordan trialgebras and post-Jordan algebras`. The decisive result was read in its primary published PDF, not accepted from generated search summaries. In particular, a generated summary repeated the misleading word “commutative”; the direct definition and explicit reproduction resolve the ambiguity.

Do not conflate the seven-relation **dendriform trialgebra / tridendriform algebra** with the eleven-relation associative trialgebra (Trias/TriAss), or with a commutative tridendriform algebra, tridendriform family algebra, Jordan trialgebra, or post-Jordan algebra. The 2017 article's main new targets are Jordan/post-Jordan identities, but its auxiliary Lemma 6.1 exactly covers this book question.

No required source remained inaccessible in this round. The book chapter's other numbered questions are outside this dossier's conclusion.

## Read-only math/ corpus comparison

The case-insensitive vocabulary screen `tridend|dendriform|trialgebra` found no matching entries in local `math/CONTENTS.md`, `math/overview.tex`, `math/lean/docs/`, `math/lean/ComparatorChallenges/`, or `math/preprints/`. The same target vocabulary found no matches in [remote openai/math main/CONTENTS.md](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md); the remote `lean/docs` listing was also inspected.

This means only **no covering entry found by this screen**. It does not prove corpus noncoverage or mathematical openness. No mathematical theorem from `math/` is borrowed. The applicable reference is procedural: `math/lean/ComparatorChallenges/README.md` establishes the fresh-module Comparator challenge/replay interface; it does not formalize a multioperator diamond lemma. The only delivered Lean root is the explicit finite symbolic-overlap theorem, and the parent owns independent Comparator replay.
