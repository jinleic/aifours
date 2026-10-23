# Balanced ternary designs (12,15) and exploratory (14,18): bounded priority audit

Recorded 2026-10-17 08:57:03 PDT. Read-only scout `BtdPriority`; search misses are not novelty. The complementary-minor/Gram method is classical; any contribution concerns the finite cases.

---

I found no published construction or nonexistence proof for BTD(12,15;6,2,10;8,6), and none for BTD(14,18;7,1,9;7,4). No general necessary condition I could check excludes either one. The newest sources that list both as open are Rosin's January 2025 paper (latest version is still v1, checked 2026‑10‑17) and his CPro1 repository. Neither is in the solved list of the May 2025 paper. The Gram-matrix argument is a known method: Connor (1952) proved the same perfect-square fact for block designs. A search miss is not proof of novelty.

## (a) Where each instance is listed as open
- **Rosin, arXiv:2501.17725v1**, Table 1, BTD block (https://arxiv.org/html/2501.17725v1). The columns are "Open instances (V,B;p1,p2,R;K,L) | [Greig (2002)] | CPro1". The rows read "(14,18;7,1,9;7,4)? | | |" and "(12,15;6,2,10;8,6)? | | |", both blank. For comparison, "(12,26;3,5,13;6,5)? | Doesn't Exist |".
  - Caption: "the smallest open instances from the Handbook are listed, along with progress on these published elsewhere in the literature."
  - Scope: "(or a proof that none exists, but in this paper we are limited to seeking solutions that construct the design)."
  - The Greig reference is cited as "Constructions using balanced n-ary designs. In Designs, pages 227–274. Springer, 2002". Crossref has it as DOI 10.1007/978-1-4613-0245-2_9, pp. 227–254, 2003.
- **Rosin, arXiv:2505.23881v1**, Table 1(a): "Open instances from 2006 Handbook, that were solved and found to exist by CPro1." The BTDs listed are (17,17;8,2,12;12,8), (14,21;6,3,12;8,6), (12,16;4,4,12;9,8), (16,16;7,3,13;13,10), (12,21;4,5,14;8,8), (16,22;9,1,11;8,5) and (21,21;12,1,14;14,9). Neither target is there.
- **CPro1 repository** (https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/balanced-ternary-design/problem_def.py): `OPEN_INSTANCES` starts with `[14,18,7,1,9,7,4],[12,15,6,2,10,8,6]`. `designs/balanced-ternary-design/` holds result files only for the 7 solved instances. The last BTD commit is 2025‑05‑29. A failed search by CPro1 is not evidence of nonexistence.
- **Kaski–Östergård data page** (https://users.ics.aalto.fi/pkaski/btd.html), numbered by Billington–Robinson 1983 and Kunkle–Sarvate 1996:
  - "76 | 31 | 12 | 15 | 6 | 2 | 10 | 8 | 6" (our 12-point case)
  - "43 | 15 | 14 | 18 | 7 | 1 | 9 | 7 | 4" (the 14-point case)
  - Both rows have empty enumeration columns. The zbMATH review (Zbl 1037.05008) gives the scope: "enumerate all but 12 of the 155 possible design classes with V≤10, B≤30, and R≤15". Both instances have V > 10, so they were outside it.
- **Dinitz "New results" pages.** The page for Part VI of the 2nd edition (last edited 10/18/2019) has no entry for chapter VI.2 (balanced ternary designs). The 1st-edition page (Wayback snapshot 2008‑10‑13) says: "Page 233, Table 2.2. Kunkle, Sarvate and Greig have pointed out several errors in Table IV.2.2 … unpublished work by Greig … For an updated version of the table, contact greig@sfu.ca."
- **Handbook status overall.** Of Rosin's 13 listed instances, these remain open after May 2025: (14,18;7,1,9;7,4), (12,15;6,2,10;8,6), (12,20;4,3,10;6,4) and (14,28;8,3,14;7,6). [INFERENCE] Rosin's list is not exhaustive: (21,21;…) appears only in the May paper.

## (b) Construction or nonexistence statements found
None for either instance.
- **Greig chapter, abstract only:** "We settle several open existence cases for BTDs". Per Rosin's blank cells, he did not settle these two. [INFERENCE: I could not read the chapter.]
- **arXiv API**, `abs:"ternary designs" OR ti:"ternary design" OR abs:"balanced n-ary"`: totalResults = 2, both Rosin papers (2026‑10‑17).
- **OpenAlex:** both Rosin papers have cited_by_count 0. The Greig chapter is cited only by Abel–Bluskov–Greig 2004 and Francel–Hurd 2008. A full-text search for "balanced ternary design" since 2024 returns 6 unrelated works.
- **zbMATH:** all 66 "balanced ternary" titles (1975–2025) checked, plus the citers of BR 1983 (7), Billington 1984 (13), Billington 1989 (9) and the Greig chapter (1). None addresses either instance.
- **Rosin, later:** the Dec 2025 NeurIPS MATH‑AI abstract, constructive.codes (newest posts 2026‑03), arXiv:2603.00174 (no "ternary" match), CPro1 GitHub issues and commits — none mention these instances.
- **Exact-string web searches** for "12,15;6,2,10;8,6" and "14,18;7,1,9;7,4" (and spaced variants), and MathOverflow/Math.StackExchange: no relevant hits.
- **Other queries:**
  - Handbook VI.2 and Dinitz pages
  - Greig chapter
  - Billington–Robinson 1983
  - BTD with Hasse–Minkowski / Bruck–Ryser–Chowla
  - Connor and n-ary block intersections
  - McCarthy (r,λ)-designs
  - CPro1 follow-ups 2025–2026

## (c) General necessary conditions
Neither instance is excluded by any condition I could check.
- **Basic parameter identities pass** (my arithmetic):
  - (12,15): 12·10 = 15·8; 6·11 = 66 = 6·7 + 4·6; N Nᵀ = 8I + 6J; B − V = 3.
  - (14,18): 14·9 = 18·7; 4·13 = 52 = 7·6 + 2·5; N Nᵀ = 7I + 4J; B − V = 4.
  - Fisher-type B ≥ V holds. The symmetric-design (Bruck–Ryser–Chowla type) condition does not apply because B ≠ V.
- **Kunkle–Sarvate 1995** (https://kunklet.people.charleston.edu/93_01.pdf), bounds on the number of blocks containing a repeated point: 6 ≤ b₂ ≤ 15 and 5 ≤ b₂ ≤ 14 respectively. Their parity lemma applies only when "K equal 4 or 5".
- **Billington–Robinson 1983** has "theorems dealing with the necessary parametric requirements" (zbMATH review), but I could not read their content. [INFERENCE] Since the Handbook (2006) and Rosin (2025) still list both as open, those conditions did not exclude them.
- **Rational quadratic-form conditions give nothing here.** [INFERENCE: every positive definite rational form in n variables is a sum of n+3 rational squares, so Hasse–Minkowski obstructions vanish once B − V ≥ 3.]
- **The Gram argument is Connor's method.** Connor, Ann. Math. Statist. 23 (1952) 57–71, as summarised in the zbMATH review (Zbl 0046.36102): "|C_t| ≥ 0 bei t<b−v … bei t=b−v gilt: |N₁N₁'| ist ein volles Quadrat". In English: the determinant is non-negative for t < b − v, and a perfect square when t = b − v. Connor used this to kill BIBDs (21,28,8,6,2) and (36,45,10,8,2). McCarthy–Vanstone (1979) extended the method to (r,λ)-designs.
  - [INFERENCE] The proof only uses N Nᵀ = aI + ΛJ, so it carries over to BTDs unchanged. The internal "3×3 principal minors of H are squares" lemma is Connor's t = b − v case. I found no published BTD application of it.
  - The parent's H for (14,18) checks out: H = 63I − 9MᵀM + 28J. A column with t twos has diagonal 28 − 18t, and t ≥ 2 would make it negative. So 14 columns have diagonal 10 and 4 have diagonal 28, with trace 252 = 63·4.
  - For (12,15), the diagonal is 24 − 10t with t ≤ 2.
  - Both cases share one mechanism, so they are one contribution: a new application of a classical method, not a new method.

## (d) Access holes
- **Handbook 2nd ed. VI.2 (Hurd–Sarvate) text was not read.** The Google Books API returned 429 and archive.org search-inside returned 403. The Handbook's "?" marks are known to me only through Rosin.
- **Greig chapter:** paywalled; the free Springer preview PDF would not convert.
- **Older papers not online:** Billington–Robinson 1983 and Greig–Sarvate 1998 appear in Combinatorial Press listings without PDFs. Billington 1984/1989 were seen only as zbMATH reviews.
- **Kaski–Östergård full text:** ScienceDirect returned 403; I used the zbMATH review and the authors' data page.
- **Blocked or failed sources:**
  - OpenReview workshop PDF (bot check)
  - ADS (405)
  - Semantic Scholar (reader could not parse the URL)
  - Donovan thesis on UQ eSpace (403)
  - Dinitz errata page (401)
  - University of Wollongong repository (bot block)
  - The 2nd-edition "new results" page for Part VI was read via REST API and a 2013 Wayback snapshot; the BTD section is absent in both.

## (e) [INFERENCE] items and what would overturn them
| Claim | Falsified by |
|---|---|
| Greig did not settle either instance | A result for these in the Greig chapter (pp. 227–254) |
| Hasse–Minkowski is vacuous for B − V ≥ 3 | A published rational obstruction for B = V+3 or V+4 |
| Connor's theorem transfers verbatim to BTDs | An integrality step needing binary entries |
| Billington–Robinson 1983 conditions did not exclude them | Its necessary-conditions section excluding class #76 or #43 |
| Remaining-open list | A Handbook VI.2 or 2025–26 update |

My only computations were arithmetic on parameters; I did not check either internal proof.
