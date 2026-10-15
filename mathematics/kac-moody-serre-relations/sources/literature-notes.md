# Primary literature and status ledger

Search date: 2026-10-14 (PT). **No resolution found is not proof of openness.** `../README.md` is the status authority. This ledger distinguishes direct parent reading, read-only scout findings, and unavailable material. All saved source hashes are in `../evidence/source-downloads.json`.

## Exact question versus naming conventions

The book, excerpt lines 12–34, defines g(A) by quotienting the preliminary Chevalley/Cartan algebra by the maximal ideal tau with tau intersect h=0, then asks whether Serre relations generate tau for every GCM. Marquis and Williams instead often denote the **Serre quotient** by g(A). Their GK-simplicity statements must be read with that convention. Simply observing that a paper defines a Kac–Moody algebra by Serre relations does not prove the book conjecture.

The book's reference [1] is Humphreys's 1972 finite-dimensional textbook; it is not used here as proof of the general symmetrizable infinite-dimensional theorem. The original Gabber–Kac paper is *On defining relations of certain infinite-dimensional Lie algebras*, Bull. AMS 5(2) (1981), 185–189, DOI **10.1090/S0273-0979-1981-14940-5**, confirmed against publisher-deposited Crossref metadata and the 2024 GHS primary reference list. A search summary supplied a different DOI; that summary was rejected. Original AMS full text was blocked, so no claim of reading that proof is made.

## Open-status sources, newest posting distinguished from newest text

### Rousseau: 2025 posting of older text

- [arXiv:2508.08728](https://arxiv.org/abs/2508.08728), posted 2025-08-12; DOI [10.24033/bsmf.2724](https://doi.org/10.24033/bsmf.2724), *Bull. SMF* 144 (2016), 613–692.
- Opened parent: abstract and full PDF. Saved `rousseau-2025-repost.pdf/.txt`.
- The PDF title page explicitly says **12 Mai 2015** and its abstract mentions an erratum. Therefore the 2025 upload is not treated as a fresh 2025 assessment of openness.
- §6.5, PDF p.54; `.txt:3286-3305`: “En caractéristique 0, g_k est GK-simple dans le cas symétrisable (et même conjecturalement dans tous les cas).” Translation: in characteristic zero it is GK-simple in the symmetrizable case, and conjecturally in all cases.
- The same passage warns that characteristic-zero GK-simplicity does not automatically imply its positive-characteristic counterpart. This supports keeping modular diagnostic failures separate from the book's characteristic-zero problem.

### Marquis 2023: later fresh open-question discussion

- [arXiv:2309.02508](https://arxiv.org/abs/2309.02508), *Minicourse on Kac-Moody groups*, 2023-09-05.
- Opened parent: abstract and full PDF. Saved `marquis-minicourse-2023.pdf/.txt`.
- §6 “Open questions”, §6.2, printed p.11; `.txt:621-636`: Question 6.3 asks when the maximal group is GK-simple. For characteristic zero, the text then says: “For A non-necessarily symmetrisable, this is equivalent to proving the Gabber–Kac simplicity Theorem 0.2 for A.”
- This is an equivalent formulation with a precisely stated characteristic distinction. It does not solve the arbitrary-matrix Lie problem.

### Williams 2022: most explicit modern statement of the exact two-quotient problem

- Robert Theodore Williams Jr., *Commutator Formulas in Groups of Kac-Moody Type*, University of Virginia thesis, title page August 2022, DOI [10.18130/t9v1-vz61](https://doi.org/10.18130/t9v1-vz61).
- Opened parent: full PDF via [stable public download](https://libraetd.lib.virginia.edu/public_view/gx41mj85m/download?file=1_Williams_Robert_2022_PHD.pdf). Saved `williams-thesis-2022.pdf/.txt`.
- Printed p.49 / PDF p.55; `.txt:2079-2098` explicitly defines Kac's maximal-ideal quotient and the Serre quotient and says: “They coincide in (at least) the case that A is a symmetrizable matrix ... but it is not known if they always coincide or if there is a GCM A for which they do not.”
- Proposition 6.1.4 also supplies the preliminary triangular decomposition, free positive/negative subalgebras, Chevalley involution, and maximal ideal splitting. This is direct support for the computation's setup, not just an open-status citation.
- The initially indexed `/downloads/ns064727m?...` endpoint returned only a JavaScript shell. The alternate public-view endpoint was found by the scout and independently opened/downloaded by the parent. Only the successful PDF is counted.

### Marquis 2019: exact characteristic-zero open statement and an important false lead

- [arXiv:1509.01976](https://arxiv.org/abs/1509.01976), journal DOI [10.5802/aif.3301](https://doi.org/10.5802/aif.3301), *Ann. Inst. Fourier* 69(6), 2519–2576; online 2019-10-29.
- Parent opened full author PDF and publisher metadata; `marquis-2015.pdf/.txt` is the retained arXiv source, despite the filename's submission year.
- Printed p.2523; `.txt:150-165`: in characteristic zero the group question is equivalent to the Lie Gabber–Kac theorem, and “when A is not symmetrisable, this latter problem remains, decades after it was first considered, completely open.” Footnote `.txt:194` specifies the Serre-defined convention.
- §2.2 gives the two-stage construction; its sign convention for f differs from the book's convention, so the computational proof fixes the book's signs explicitly.
- Proposition C and §2.7 positive-characteristic examples are **not** counterexamples over C. The rank-two examples there are symmetrizable as matrices; the different field is decisive.

## Recent broader theory and the module question

### Gorelik–Hinich–Serganova 2024

- *Root groupoid and related Lie superalgebras*, **Annals of Representation Theory**, not Annales de l'Institut Fourier; 1(4) (2024), 465–516, DOI [10.5802/art.13](https://doi.org/10.5802/art.13), published 2024-10-08.
- Parent opened full PDF and publisher record. Saved `gorelik-hinich-serganova.pdf/.txt`.
- §1.1.3 explicitly distinguishes the classical maximal-ideal and Serre constructions and states agreement in the symmetrizable case. Its statement that root-algebra classification is open even for Lie algebras is broader than the book's exact conjecture; it is supporting context, not a substitute for Williams's precise quotation.
- The equality theorem at printed p.468 leaves out the indefinite nonsymmetrizable case. The gl(1|1), sl(n|n), sq(n) and nonsymmetrizable affine **super** exceptions must not be presented as ordinary-Lie counterexamples.

### Kumar / Heckenberger–Kolb

- Heckenberger–Kolb, [arXiv:math/0605460](https://arxiv.org/abs/math/0605460), journal DOI [10.1007/s00031-007-0059-2](https://doi.org/10.1007/s00031-007-0059-2).
- Parent opened abstract and full PDF; saved `heckenberger-kolb-2006.pdf/.txt`.
- Theorem 3.2 cites Kumar's BGG exactness theorem for the complex ending in the **maximal integrable quotient V(mu)**. The same p.6 explicitly states that it is not known whether V(mu) is simple for arbitrary Kac–Moody Lie algebras (`.txt:225-262`). Therefore Kumar's geometric exactness does not resolve the defining-relations conjecture.
- The scout read Mathieu's 1988 *Astérisque* text and identified an implication from simplicity of all standard highest-weight modules to GK-simplicity (Lemme 115), but did not verify a converse. The book itself calls the conjectures closely related; its “or equivalently” connects module irreducibility with complete reducibility in category O, not explicitly with Conjecture 1.
- A Zhang–Lu 2010 Chinese article's partially accessible abstract suggested an equivalence for canonical algebras, but its decisive final phrase was available only in a search snippet. **[UNVERIFIED]**; no theorem is imported from it.
- Dhillon–Khare, [arXiv:1606.09640](https://arxiv.org/abs/1606.09640): parent opened abstract; scout read the author PDF. It distinguishes weight sets from weight multiplicities of simple modules. This is not a solution to equality of the two Lie-algebra quotients.

### Fang's quantum specialization is not a classical counterexample

- **Xin Fang**, [arXiv:1303.5994](https://arxiv.org/abs/1303.5994), *Non-symmetrizable quantum groups: defining ideals and specialization*. The pre-screen attribution to Berenstein–Greenstein was incorrect.
- Parent opened full PDF and abstract; saved `fang-2013.pdf/.txt`.
- Its Nichols-algebra relations and specialization difficulties are a different issue. The scout inspected Example 2 and noted that the displayed (ad f_3)^3 f_1 is not the classical Serre relation when c_31=-3, whose exponent is 4. No characteristic-zero extra classical relation is thereby established.

## Works citing Marquis 2019: explicit coverage audit

The read-only scout queried OpenAlex on 2026-10-14 and found three records for two distinct papers citing DOI 10.5802/aif.3301. This index is incomplete and the counts are not a literature census. Parent subsequently opened both arXiv abstracts; the scout keyword-searched their PDFs but did not fully referee them.

1. **Paula Harring and Ralf Köhl**, *Fundamental groups of split real Kac-Moody groups and generalized real flag manifolds*, [arXiv:1905.13444](https://arxiv.org/abs/1905.13444), journal DOI [10.1007/s00031-022-09719-7](https://doi.org/10.1007/s00031-022-09719-7), 2022. Abstract: topology/fundamental groups, with a result also applying in the nonsymmetrizable two-spherical situation. This is not Serre-ideal equality. The scout found “Gabber” only in the Marquis reference entry.
2. **Inna Capdeboscq, Katerina Hristova, Dmitriy Rumynin**, *Cocompact Lattices in Locally Pro-p-complete Rank 2 Kac-Moody Groups*, [arXiv:1807.07929](https://arxiv.org/abs/1807.07929), journal DOI [10.1070/SM9311](https://doi.org/10.1070/SM9311), 2020. Abstract: locally pro-p group lattices and covolume, not the characteristic-zero defining ideal. The third OpenAlex record is the Russian original, DOI [10.4213/sm9311](https://doi.org/10.4213/sm9311), not a third independent paper.

No current all-height nonsymmetrizable result was found by this citing-work screen. It is explicitly limited by indexed coverage and the stated reading depth.

## Special cases and search limitations

- Every rank-two GCM is symmetrizable; tree-shaped diagrams are symmetrizable by diagonal-ratio propagation. Non-symmetrizable matrices require unbalanced cycles. The rank-three inputs here satisfy that obstruction explicitly.
- Hyperbolic diagram classification includes nonsymmetrizable diagrams. Classification is not a defining-ideal theorem; no such all-height theorem was found in the opened works.
- The present coefficient-one comparison theorem and finite computations are in `../proof.md` and evidence/. They are not mislabeled published SOTA or all-height resolutions; novelty was not established.
- Parent's openai/math / Sra screen is recorded as parent-reported negative catalog evidence at commit adc7f1241, not as proof of openness.
- Unavailable or only partially read: original Gabber–Kac AMS proof, Kumar 1990 scan and 2002 book, Marquis 2018 book, and the Zellhofer thesis whose endpoint returned HTML. No missing passage is fabricated.

Search queries combined Gabber–Kac, nonsymmetrizable, Serre/maximal ideal, rank three, hyperbolic, off-diagonal products, Kumar, BGG, integrable highest-weight modules, and Chinese formulations, including post-2019 filters. The dossier retains the conservative current label **uncertified-open**, while accurately recording the positive dated primary assertions that the exact question was open.
