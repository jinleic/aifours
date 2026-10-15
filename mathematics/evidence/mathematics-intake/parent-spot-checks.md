# Parent source checks — mathematics volume

Checked 2026-10-14. This file records direct checks by the parent, separately from subagent reports. It is not a proof of the five original problems or a claim of exhaustive literature coverage.

## Book provenance and scope

- Original PDF: `/Users/jinleic/Documents/中文pdf/10000个科学难题·数学卷(10000个科学难题数学编委会).pdf`.
- SHA-256, measured with `shasum -a 256`: `3c69cf2c023a37fdb9e2c7e8ccbe9b163e067884f257003c9df64ac62d092901`.
- `pdfinfo`: 568 PDF pages, Science Press first edition 2009 in the copyright page. Book page 1 is physical PDF page 17.
- Front contents extracted with `pdftotext -layout -f 9 -l 16` to `book-contents.txt` here. Counting terminal `(number)` entries gives 251 entries including the afterword at book page 553, hence 250 problem articles. The original selection inspected the contents and roughly 45 candidate sections; it did not read every article in full.
- The opening problem articles are logic and set theory. The five candidates were selected from the front table of contents and then their actual pages, not exclusively from the first five problem articles.

## Load-bearing sources opened directly

1. Chen Wang, *A new recursive construction for large sets of Kirkman triple systems*, [arXiv:2607.21521](https://arxiv.org/abs/2607.21521), July 2026. Parent opened the abstract and extracted PDF text, especially concluding remarks. It states LKTS(v) known for every admissible v below 200 with possible exceptions 57 and 87, calls these the smallest remaining cases, and suggests prescribed-automorphism search. Its wording is a dated literature statement, not proof that no subsequent construction exists. The LKTS agent checks later literature independently.
2. Andreas S. Schulz, *On the Relative Complexity of 15 Problems Related to 0/1-Integer Programming*, [author manuscript](https://web.mit.edu/schulz/www/epapers/s-2009.pdf), [DOI](https://doi.org/10.1007/978-3-540-76796-1_19). Parent opened the PDF and read Assumptions 1–2, definitions, Theorem 1 and reduction sections. Assumption 1 permits all integer costs; Assumption 2 supplies a feasible point. Theorem 1 includes forward optimization, inverse optimization under l1/linf, and optimality verification in the polynomial equivalence. Therefore that restricted reading of the book question is already solved and cannot be counted as a new solution. General nonlinear objectives and absent feasible starts are separate formulations.
3. Malliaris–Shelah, *Cofinality spectrum theorems in model theory, set theory and general topology*, [arXiv:1208.5424](https://arxiv.org/abs/1208.5424). Parent opened the primary abstract; it explicitly resolves p=t. This excludes the book's minimal tower problem from the unsolved selection.
4. Arsovski, *A proof of Snevily's conjecture*, [DOI:10.1007/s11856-011-0040-6](https://doi.org/10.1007/s11856-011-0040-6). Parent opened the publisher abstract; it states a proof for finite abelian groups of odd order. Publisher metadata says Israel J. Math. 182, 505–508 (2011), not the 505–516 page range returned by a search summary.
5. Karlin–Klein–Oveis Gharan, *A (Slightly) Improved Approximation Algorithm for Metric TSP*, [arXiv:2007.01409](https://arxiv.org/abs/2007.01409). Parent opened the primary abstract; it states a randomized (3/2−epsilon)-approximation for some epsilon>10^(-36). This settles the book's sub-1.5 approximation existence question in the randomized sense, not deterministic approximation or exact TSP.
6. Original regular-semigroup article, extracted by the agent at `../../regular-semigroup-embedding/sources/book-excerpt.txt`, read directly by parent. Book reference [2] is Szendrei, *Some open problems in the structure theory of regular semigroups*, Semigroup Forum 64 (2002), 213–223. Reference [1] is Billhardt–Hsieh, a preprint; it must not silently be replaced bibliographically by Billhardt–Szendrei (2003), even where the later theorem is relevant. Parent checked natural order, weak E-unitarity, regular/normal/seminormal-band definitions and Problem 1.
7. Santos, *A counterexample to the Hirsch conjecture*, [arXiv:1006.2814](https://arxiv.org/abs/1006.2814). The primary abstract states a 43-dimensional counterexample with 86 facets and its relation to the d-step conjecture.
8. Brenner–Monsky, *Tight closure does not commute with localization*, [DOI:10.4007/annals.2010.171.571](https://doi.org/10.4007/annals.2010.171.571). CrossRef returned title, authors, journal and publication date, but no abstract; this session did not audit the proof.
9. Adiprasito, [arXiv:1812.10454](https://arxiv.org/abs/1812.10454), and Papadakis–Petrotou, [arXiv:2012.09815](https://arxiv.org/abs/2012.09815). Parent opened both primary abstracts. The latter explicitly says it gives a second proof of McMullen's g-conjecture for simplicial spheres. No claim is made here about unrelated nonsimplicial versions.

## Access limits and non-evidence

- The search summary claiming a new n=5 Atiyah–Sutcliffe proof at Zenodo record 23142909 was not verified. Both the record and API returned HTTP 403 through `read`. It is not an established solved exclusion and is not evidence for or against the conjecture.
- The Annals HTML page for Santos returned a generic comments feed rather than the article. That response was discarded; the primary arXiv abstract was subsequently checked (item 7).
- A search result is a discovery aid, not a checked primary source. Absence of a solution in these searches is not proof that a problem remains open.

## Difficulty interpretation

The defensible criterion is **bounded setup and checkable progress**, not guaranteed low mathematical difficulty. A finite certificate can be easy to verify and still extremely hard to discover. LKTS(57/87) has a concrete construction target; M-estimation has low-dimensional proof/counterexample routes; Artin rewriting has exact critical-pair checks; Gabber–Kac has an exact degree-by-degree linear-algebra counterexample route; regular-semigroup embedding has nearby structural theorems. All remain research-risky in the surviving formulations. The independent review (`independent-review.json`, verdict ready-with-fixes) found nothing supporting a "not too hard" label; no success probability or guarantee of full resolution is asserted.

## Slot-2 replacements

1. Inverse optimization (book pp. 535–536): replaced. Schulz 2009 (item 2) covers the binary, full-linear, known-feasible-start case; the 2025 Guan–Pardalos–Zhang chapter abstract ([DOI](https://doi.org/10.1007/978-3-031-91175-0_1), opened) still calls "an inverse problem of an NP-hard problem polynomially solvable?" unresolved, but no single precise open formulation was certified.
2. Seymour's second-neighborhood conjecture (book pp. 417–418): rejected after one step. [Bai–Li–Park, arXiv:2607.18047](https://arxiv.org/abs/2607.18047) (opened; July 2026) says it remains open, but `math/lean/docs/173.md` in the local openai/math clone (read directly) scopes a Lean formalization of the full conjecture (exact distance-two neighbors, sinks allowed), with preprint dated 2026-09-23. Not re-verified with Comparator here.
3. Gabber–Kac for non-symmetrizable GCMs (book pp. 226–227): selected. Book text read directly (Conjecture 1: Serre relations define g(A) for every GCM). Open-status evidence pending primary-text verification by the target agent; Marquis, [arXiv:1509.01976](https://arxiv.org/abs/1509.01976), abstract opened, concerns the related Gabber–Kac simplicity conjecture.

## openai/math corpus screen (2026-10-14)

- Local clone `math/` at adc7f1241 (2026-10-06): 235 family docs, 722 preprint directories. Remote listing via the GitHub web page: 242 families (new: 027, 066, 075, 103, 137, 195, 301; titles read via raw.githubusercontent.com, none related) and 749 preprint directories; the GitHub REST API was rate-limited.
- Case-insensitive term scans of `lean/docs` and `preprints` (`*.md`, `*.tex`) for Kirkman/LKTS, Shirshov/Gröbner, E-unitary/orthodox, M-estimat, inverse optimization/Heuberger, Gabber/Serre relation/non-symmetrizable: every hit was in an unrelated paper (inspected by path). No family or preprint covers the five selected targets.
- The corpus does claim many other problems in this book (README "Screened out"). Sra, [arXiv:2608.29595](https://arxiv.org/abs/2608.29595) (opened; 15+ GPT-found counterexamples) was also scanned: no selected topic.
- DFP convergence (book p. 527) is answered negatively by [Liu–Wang–Wen–Zhang–Yuan, arXiv:2608.21708](https://arxiv.org/abs/2608.21708) (abstract opened; August 2026 preprint).
