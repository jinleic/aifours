# Literature reading ledger

Snapshot: 2026-10-14, America/Los_Angeles. This is a source ledger; `../README.md` is the target's status authority. Search summaries were used only to find sources, not as proof. Download URLs, failures, file sizes, and SHA-256 hashes are in `../evidence/source-downloads.json`.

## Load-bearing sources actually opened

1. **Book excerpt**, `book-excerpt.txt`, extracted with `pdftotext -layout -f 551 -l 552` from the user-supplied PDF. Printed pages 535–536, author Yang Xiaoguang (杨晓光). It poses Heuberger's converse and lists weighted l1, l2, infinity, and Hamming distances. Its reference [1] has incorrect journal/year/volume metadata; use *Operations Research* 49(5), 771–783 (2001), DOI 10.1287/opre.49.5.771.10607, rather than silently repeat the book's 2000/35 entry.

2. **Heuberger (2004)**, DOI [10.1023/B:JOCO.0000038914.26975.9b](https://doi.org/10.1023/B%3AJOCO.0000038914.26975.9b). Full author manuscript opened and saved as `heuberger-2004.pdf` / `.txt`; publisher record also opened. This manuscript is 27 PDF pages, not the 33-page typeset journal layout. Section 2.1, equations (2.1)–(2.2), permits F_g subsets of R^n, a fixed general f(c,x), supplied feasible targets, and lower/upper bounds on modified costs. The objective need not be c·x. Section 5, item 1, author-PDF page 23, asks (verbatim, line breaks normalized):

   > Consider the following “inverse” question: Given an optimization problem (2.1) with a polynomially solvable inverse problem (2.2) (for all c and x̂). What does this imply for the complexity of the original problem (2.1)? Does it necessarily belong to P?

   Local anchors: `heuberger-2004.txt:91-133` (model), `:1250-1256` (question and coNP remark), `:1151-1168` (center-location discussion). The short wording in Section 2.1 is: “If the inverse problem is polynomially solvable, does this also hold for the original problem?” His following coNP argument concerns certification of global optimality and tacitly needs appropriate nonempty/attainment/encoding hypotheses for forward decision complements; it does not make arbitrary infeasibility certificates available.

3. **Schulz (2009)**, DOI [10.1007/978-3-540-76796-1_19](https://doi.org/10.1007/978-3-540-76796-1_19), chapter pp.399–428. Full MIT author manuscript and publisher record opened. Saved `schulz-2009.pdf` / `.txt`, publisher metadata `schulz-metadata.json`.
   - Assumption 1: all integer cost vectors on a fixed feasible set remain instances (`.txt:107-109`).
   - Assumption 2: a feasible point is explicitly known (`.txt:172-176`).
   - Inverse definition and footnote 4: l1 or l-infinity (`.txt:204-225`).
   - Theorem 1: all 15 tasks, including inverse, forward, and optimality verification, are oracle-polynomial equivalent (`.txt:275-281`).
   - Lemma 19: verification to augmentation; Lemma 5: augmentation to optimization by bit scaling. These are the sources of our main proof, not a new discovery.
   This source decisively resolves the standard known-start linear binary reading, even though later broad surveys still use open-problem wording.

4. **Huang (2005)**, DOI [10.1007/11496199_45](https://doi.org/10.1007/11496199_45). Opened publisher abstract, saved HTML `huang-2005.html`. It explicitly says the inverse knapsack algorithm and fixed-number-of-constraints integer-programming inverse algorithm are **pseudo-polynomial**. Full paid chapter was not obtained. Therefore this is not evidence of bit-polynomial inverse algorithms for NP-hard forward problems. Bulut–Ralphs independently describes the same result in its previous-work section.

5. **Berg–Hempel (2008)**, DOI [10.1007/978-0-387-09680-3_5](https://doi.org/10.1007/978-0-387-09680-3_5). The IFIP host timed out twice; the publisher's freely available full PDF worked and is saved as `berg-hempel-2008.pdf` / `.txt`. Introduction and Definition 1 describe a different inverse problem: given an explicit set of certificates Pi, find/decide existence of an input x whose verifier accepts exactly Pi. It is **not** nearest-cost modification making a supplied feasible solution optimal. Its polynomial-hierarchy results do not answer Heuberger's optimization question.

6. **Bulut–Ralphs (2021)**, DOI [10.1137/20M1377369](https://doi.org/10.1137/20M1377369), arXiv [2104.09002](https://arxiv.org/abs/2104.09002). Full author report, last revised November 18, 2021, opened and saved as `bulut-ralphs-2021.pdf` / `.txt`. It proves coNP-completeness of inverse-MILP primal-bound verification, NP-completeness of dual-bound verification, and DP-completeness of exact-optimal-value verification. **Important model caveat:** Section 1 expressly does not require x0 in S; it works with S+=S union {x0}. Its general equivalence therefore cannot be transferred blindly to a promised-feasible-target oracle. The dummy-closure theorem in our proof makes a corresponding assumption explicit. Relevant local anchors: `.txt:844-914` (decision formulations), `:918-936` (target may be infeasible in S).

7. **Guan–Pardalos–Zhang (2025)**, DOI [10.1007/978-3-031-91175-0_1](https://doi.org/10.1007/978-3-031-91175-0_1), first online July 25, 2025. Publisher abstract and references opened; saved `guan-pardalos-zhang-2025.html`. The abstract explicitly says: “We question whether an inverse problem of an NP-hard problem can be polynomially solvable, an unresolved challenge.” **Only the public abstract/references were available**, not the chapter's full formulation/discussion. This supports reporting its broad question as described by that publication, not asserting that every restricted version remained open in 2025. It cites Bulut–Ralphs. Its publicly shown reference list did not supply the missing distinction as a replacement for reading Schulz's actual theorem.

8. **Bérczi–Mendoza-Cadena–Varga (2025 journal / 2023 preprint)**, DOI [10.1007/s11590-024-02183-0](https://doi.org/10.1007/s11590-024-02183-0), arXiv [2302.13411](https://arxiv.org/abs/2302.13411). Full arXiv PDF and abstract opened, saved `berczi-mendoza-varga.pdf` / `.txt`; final publisher article also opened and saved as `berczi-mendoza-varga-journal-2025.pdf` / `.txt`.
   - Weighted bottleneck-Hamming: O(n) forward-oracle calls for the Newton-type algorithm (preprint Theorem 4), improved to O(log n) calls by the final journal version's binary-search algorithm (Section 1.3); strongly polynomial if the forward oracle is strongly polynomial.
   - Weighted l-infinity: a pseudo-polynomial Newton-type algorithm, strongly polynomial in the unit-weight case, conditional on a matching forward oracle. This does not erase the older weakly polynomial LP/ellipsoid algorithm for rational weights.
   - Theorem 14: exact weighted-infinity min-max characterization, including multiple cost vectors; our Proposition L is its single-cost unconstrained form, independently reproved.
   - The norm is bottleneck Hamming, not sum-Hamming. Changing one word changes the problem.

9. **Ley–Merkert (2025)**, DOI [10.1007/s10898-025-01529-x](https://doi.org/10.1007/s10898-025-01529-x). Full open-access article opened and PDF saved `ley-merkert-2025.pdf` / `.txt`. With only weight increases, partial inverse shortest path on a DAG and partial inverse assignment are NP-complete even with a single required edge/arc. This concerns *partial* targets and the opposite forward-P/inverse-hard direction; it is not a counterexample to inverse-P => forward-P.

10. **Cai–Yang–Zhang (1999)**, DOI [10.1023/A:1008360312607](https://doi.org/10.1023/A%3A1008360312607). Publisher abstract opened and saved `cai-yang-zhang-1999.html`: forward center location is polynomial, inverse is NP-hard. Heuberger Section 4.18 additionally specifies sign-constrained single-object unit-l1 inverse minmax center location, all vertex demands 1. The book's stronger adjective “strongly” is **[UNVERIFIED] from the primary full proof** because the original article was not obtained. We report only the primary abstract's NP-hardness, which suffices here.

## Requested source with incomplete access

**Demange–Monnot**, *An Introduction to Inverse Combinatorial Problems*, DOI [10.1002/9781119005353.ch17](https://doi.org/10.1002/9781119005353.ch17), July 10, 2014, pp.547–586. The publisher URL and both 2014/earlier-edition PDF endpoints returned HTTP 403. Publisher-deposited Crossref metadata was opened and saved in `demange-monnot-metadata.json`, confirming title/authors/date/DOI but providing no abstract. Search located no accessible author manuscript. **[UNVERIFIED]** whether this chapter resolves or qualifies the converse. No theorem or open-status claim is attributed to its unseen contents.

**Ahuja–Orlin (2001)**, DOI [10.1287/opre.49.5.771.10607](https://doi.org/10.1287/opre.49.5.771.10607). The publisher returned 403, the indexed CiteSeer mirror 404; Orlin's author publication list confirms the correct journal metadata. MIT DSpace record [1721.1/2696](https://hdl.handle.net/1721.1/2696) for the 1998 working paper opened, but its PDF download returned 429. We rely on the fully opened Heuberger Theorem 3.3 and Schulz Lemma 4 for the theorem itself, not an invented reading of the inaccessible journal PDF.

## Rejected claimed resolution

**Siming Huang (2021 preprint)**, [arXiv:2103.15337](https://arxiv.org/abs/2103.15337), full PDF opened and saved `huang-2021.pdf` / `.txt`. Its abstract claims to resolve Heuberger and prove coNP=NP. Two concrete defects prevent using it as a resolution:

- Section 2 constructs inverse **KKT-point** problems for nonconvex QP, not global-optimum inverse problems. KKT stationarity is not sufficient for global optimality in that setting.
- Its Theorem 4.4 defines P2 as “all feasible solutions ... are not the KKT points” but then infers P2 in NP merely from polynomial checking of a given x0 and the existence of many feasible points (`huang-2021.txt:367-377`). This replaces a universal statement by checking one candidate; it supplies no polynomial certificate for the universal assertion. The number of candidates being exponential makes the inference worse, not valid.

We reject this argument, not assert the negation NP!=coNP. In particular, the unrelated open status of P versus NP would not itself refute an NP=coNP claim.

## Search limits and reproducibility

Searches used exact question fragments, Heuberger + complexity, NP-hard-forward/P-inverse, Demange–Monnot, weighted Hamming, partial inverse problems, and post-2024 references. The result is a scoped literature check, not an exhaustive proof of absence of any 2026 publication. The strongest positive status finding is the explicit 2009 theorem, verified in the full primary manuscript. The strongest recent broad-open wording is the 2025 publisher abstract. The remaining no-initial-point formulation is marked unresolved **in this dossier**, not falsely certified as a formally established open problem of the entire literature.

All successful PDF sources can be re-extracted with `pdftotext -layout sources/NAME.pdf sources/NAME.txt`. Reproduction commands for the mathematical checks are in `../README.md`.
