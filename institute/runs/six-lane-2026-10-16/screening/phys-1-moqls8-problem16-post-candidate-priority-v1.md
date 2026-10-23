# phys-1 post-candidate priority screen v1: every set of five MOQLS(8) is classical (Ball–Simoens Problem 16 at n = 8; M(8) ≤ 4)

- Recorded: 2026-10-18T06:40:08-07:00 (host clock). Screener: `PriorityScreensQLS`, a task subagent of the six-lane run. Literature priority only.
- Not claimed: that the result is new, priority, an exhaustive search, or correctness. Correctness is reviewed separately in the lane.
- No earlier MOQLS(8) priority screen exists in `screening/` or `review/`. The lane contract `screening/phys-1-moqls8-problem16-contract.json` gives the pre-run attestation.

## Classification
**NONE_FOUND_IN_BOUNDED_SCOPE**

- The bounded screen found no published source for the statement that every set of five MOQLS(8) is classical (M(8) ≤ 4). It found none for any other resolution of Problem 16 at n = 8, and no general theorem that implies it.
- It found no published partial result on non-classical MOQLS(8) sets of size 3, 4 or 5, either constructions or exclusions.
- No source constructs a non-classical 5-MOQLS(8). Such a construction would contradict the statement.
- The known published bounds are 2 ≤ M(8) ≤ 5:
  - Ball–Simoens v2, Table 2 and Theorem 5;
  - non-classical 2-MOQLS(8) from Han et al. Theorem 3.7 and from Zhang–Cao Example 2.4 with Lemma 2.2.

## Statement screened
- **Definitions.** These follow Ball–Simoens v2 §2.2–2.3 (PDF pp.2–3).
  - Orthogonality: product vectors ψ_ij ⊗ φ_ij form an orthonormal basis of C⁸ ⊗ C⁸.
  - Set isotopy allows phases, simultaneous row and column permutations, and a separate unitary for each square.
  - A set is classical if, up to isotopy, all its entries lie in one fixed orthonormal basis.
  - M(n) (PDF p.1): "we define M (n) as the largest value of t such that a non-classical set of t MOQLS(n) exist".
- **Statement.** Every set of 5 MOQLS(8) is classical. This is Ball–Simoens v2 PDF p.7, "Problem 16. Is a set of n − 3 MOQLS(n), n ̸= 4, necessarily classical?", at n = 8. Equivalently M(8) ≤ 4.
- **Also checked.** Partial results on non-classical MOQLS(8) sets of size 3–5.
- **Notion scope.** Product-state orthogonality only. Entangled "quantum orthogonal Latin squares" (Goyeneche et al.; AME(4,n)) and weak orthogonality are not covered.

## Primary-source status (Ball–Simoens, arXiv:2607.12933)
- **Latest version is v2.**
  - The arXiv API (06:23:36) gives v2: updated 2026-07-27T07:40:44Z, comment "Correction of Theorem 6", no journal-ref.
  - The abs page (06:31:51) lists only v1 (14 Jul 2026) and v2 (27 Jul 2026). There is no v3 that could itself settle n = 8.
- **Downloaded copy matches.** The v2 PDF downloaded at 06:28:40 has sha256 `2d60d45f…6e21afe`, identical to the pinned local copy `review/quantum-latin-2607.12933v2.pdf` (also the `local_pdf_sha256` in the lane contract).
- **Relevant content.**
  - Table 2 (PDF p.2) gives M(8) as "2-5". Table 1 (earlier bounds) gave "2-6".
  - Theorem 5 (PDF p.1, proof p.4) gives M(n) ≤ n − 3, so M(8) ≤ 5.
  - Problem 16 is still posed in v2 (PDF p.7).
  - Corollary 7 needs a proper divisor d ≠ 1 of q − 1. At q = 8, q − 1 = 7 has none [INFERENCE: arithmetic], so the paper gives no order-8 construction beyond the pair bound.
- **Author page.** Simoens' publication page (06:31:06) still lists 2607.12933 as the only QLS preprint.

## Queries run
Host clock, PDT (UTC−7). The screen ran from 06:21:54 (clock read) to 06:33:46 (last fetch); this file was composed at 2026-10-18T06:40:08-07:00. The same query set serves this screen and its companion screen, because the two statements share one literature.

### Web search (`web_search` tool)
| # | web_search query | issued (PDT) | outcome |
|---|---|---|---|
| W1 | `"mutually orthogonal quantum Latin squares" order 7 non-classical three` | 06:23:20–06:23:32 | Ball–Simoens 2607.12933, Han et al. 2507.20154v1, INSPIRE record 3180352, classical MOLS pages; no order-7 triple result |
| W2 | `Ball Simoens "Large sets of mutually orthogonal quantum Latin squares" Problem 16` | 06:23:20–06:23:32 | 2607.12933 abs/html v1, 2609.29070v1; no restatement or answer of Problem 16 |
| W3 | `"quantum Latin squares" order 8 non-classical MOQLS classical five` | 06:23:20–06:23:32 | 2607.19969v1 (cardinality), 1708.05946 (Goyeneche et al.), 2607.12933, 2608.29201, alphaXiv/INSPIRE mirrors; no order-8 set result |
| W4 | `"orthogonal quantum Latin squares" 2026 arXiv non-classical sets M(n)` | 06:23:20–06:23:32 | 2607.12933, 2507.20154v1, 2608.29201, 2609.29070v1; no M(7)/M(8) value |
| W5 | `"MOQLS(7)" OR "3-MOQLS(7)" OR "M(7)" mutually orthogonal quantum Latin squares classical` | 06:31:21–06:31:51 | 2607.12933 v1/v2, 1804.04042 (Musto–Vicary), 2609.29070, OEIS A001438 (classical MOLS); nothing on M(7) |
| W6 | `"MOQLS(8)" OR "5-MOQLS(8)" OR "M(8)" non-classical quantum Latin squares order 8` | 06:31:21–06:31:51 | 2607.12933, 2607.19969 v1/v2, 2608.29201v1, Musto–Vicary 2016 (ORA, Birmingham), 2507.20154; nothing on M(8) |
| W7 | `Simeon Ball preprints 2026 quantum Latin squares classical n-3` | 06:31:21–06:31:51 | 2607.12933, 2603.02334, New Scientist news item (order 6); no further Ball preprint on MOQLS |
| W8 | `Musto Vicary quantum Latin squares orthogonal 2025 OR 2026 new results` | 06:31:21–06:31:51 | 1804.04042v3, UCD 2022 student report, 2609.29070, 2608.29201, Zang et al. Discrete Math. 2026 (sciencedirect abstract), 2606.27758, 1504.02715; no MOQLS order-7/8 result |
| W9 | `Goyeneche OR Paczos "quantum Latin squares" 2025 2026 orthogonal genuinely quantum` | 06:31:21–06:31:51 | 2507.20154, 1708.05946, 2507.05642, INSPIRE 1963523 (Zang–Facchi–Tian), irredundant OA papers; no new Goyeneche/Paczos MOQLS work |
| W10 | `Simoens OR Ball "quantum Latin squares" talk abstract 2026 conference classical "n-3" OR "n − 3" MOQLS` | 06:33:31–06:33:46 | 2607.12933 v1/v2, phys.org news (Aug 2026, order 6), 2609.29070, 2603.02334; no talk abstract announcing an order-7/8 result |
| W11 | `"quantum Latin squares" "order 7" OR "order seven" orthogonal triple non-classical 2026` | 06:33:31–06:33:46 | Musto–Vicary 2016 (ORA), 2607.12933, Semantic Scholar page of 2507.20154, UCD 2022 report, classical MOLS(10) papers; no order-7 triple result |
| W12 | `"orthogonal quantum Latin squares" "order 8" OR "order eight" three OR four OR five non-classical construction` | 06:33:31–06:33:46 | UCD 2022 report, 2608.29201, Musto thesis (Coecke page), 2507.20154 (S2 page), 2303.15001 (quantum k-uniform states); no order-8 3/4/5-set result |

### arXiv API (export.arxiv.org)
| arXiv API `search_query` (sortBy=submittedDate desc; metadata fields only) | PDT | total | 2025+ hits returned / note |
|---|---|---|---|
| `all:"quantum Latin"` | 06:23:51 | 28 | 2610.17170v1, 2609.29070v1, 2609.24653v1, 2609.09695v1, 2608.29201v2, 2608.12607v1, 2607.19969v2, 2607.12933v2, 2607.11800v3, 2606.27758v1, 2605.15540v2, 2603.02334v1, 2601.09132v1, 2508.01972v1, 2507.20154v1, 2507.05642v1 |
| `abs:"orthogonal quantum Latin"` | 06:23:54 | 9 | 2609.29070v1, 2607.12933v2, 2603.02334v1, 2507.20154v1 |
| `all:MOQLS` | 06:23:58 | 3 | 2607.12933v2, 2507.20154v1 (2606.18111v1 is an unrelated RL paper using the acronym) |
| `all:"quantum Latin" AND cat:math.CO` | 06:24:01 | 15 | 2609.29070v1, 2609.24653v1, 2609.09695v1, 2608.29201v2, 2608.12607v1, 2607.19969v2, 2607.12933v2, 2607.11800v3, 2606.27758v1, 2605.15540v2, 2603.02334v1, 2601.09132v1, 2508.01972v1, 2507.20154v1 |
| `all:"quantum Latin" AND cat:quant-ph` | 06:24:05 | 17 | 2610.17170v1, 2607.12933v2, 2603.02334v1, 2601.09132v1, 2507.20154v1, 2507.05642v1 |
| `au:Simoens` | 06:24:08 | 522 | 20 newest shown; only 2607.12933v2 concerns QLS (others: unrelated authors/fields) |
| `au:Ball_S AND all:quantum` | 06:24:12 | 0 | — |
| `(au:Musto OR au:Vicary) AND all:Latin` | 06:24:15 | 5 | 5 hits, all pre-2025 (Musto–Vicary line) |
| `au:Goyeneche` | 06:24:19 | 47 | 2025+ items 2608.14981, 2606.05666, 2602.20275, 2601.22253, 2601.05973, 2512.11729, 2510.16117, 2507.06663: none on quantum Latin squares |
| `au:Paczos` | 06:24:22 | 11 | 2025+ items 2610.18131, 2610.07422, 2608.19333, 2506.13872: gravitational/quantum-optics topics, none on quantum Latin squares |
| `all:"quantum Sudoku"` | 06:24:26 | 2 | 2 hits, pre-2025: 2204.13008, 2106.02967 (Paczos et al., SudoQ cardinality) |
| `all:"genuinely quantum" AND all:Latin` | 06:24:29 | 1 | 1 hit, pre-2025 (2205.08842) |
| `(au:Zang_Y OR au:Tian_Z) AND all:Latin` | 06:24:33 | 0 | 0 (author-name format not matched; their papers appear under the topical queries) |
| `au:Cao_H AND all:Latin` | 06:24:36 | 0 | 0 (author-name format not matched; Cao-group papers appear under all:"quantum Latin") |
| `au:Huang_L AND all:Latin` | 06:24:40 | 0 | 0 (author-name format not matched; Huang–Li appears under all:"quantum Latin") |
| `all:"unitary pattern"` | 06:24:43 | 0 | — |
| `all:"quantum orthogonal Latin"` | 06:24:46 | 1 | 2610.17170v1 |
| `au:Zyczkowski AND all:Latin` | 06:24:50 | 5 | 5 hits; 2025+: 2610.17170v1 only |
| `au:Roberson AND all:Latin` | 06:24:53 | 1 | 1 hit: 2501.00196v2 (submitted 2024-12-31; group-invariant QLS) |
| `all:"orthogonal Latin" AND all:quantum AND all:classical` | 06:24:57 | 6 | 2610.17170v1 |
| `all:"36 officers"` | 06:25:00 | 9 | 2610.17170v1, 2504.15401v2 (order-6 entangled officers) |
| `all:"Latin square graph" AND all:orthonormal` | 06:25:17 | 0 | — |
| `all:"orthonormal representation" AND all:Latin` | 06:25:21 | 0 | — |
| `all:"quantum orthogonal arrays"` | 06:25:24 | 4 | 4 hits, all pre-2025 (incl. 2111.04055 Zang–Facchi–Tian, 1708.05946 Goyeneche et al.) |
| `all:"k-uniform states" AND all:Latin` | 06:25:28 | 4 | 2507.20154v1, 2503.02222v1 (LP bounds on k-uniform states; not MOQLS classicality) |
| `all:"quantum combinatorial designs"` | 06:25:31 | 4 | 4 hits, all pre-2025 |
| `all:"unitary error bases" AND all:Latin` | 06:25:34 | 6 | 2507.20154v1 |
| `all:"quantum Latin" AND all:orthogonal` | 06:25:43 | 13 | 2610.17170v1, 2609.29070v1, 2608.12607v1, 2607.12933v2, 2607.11800v3, 2605.15540v2, 2603.02334v1, 2507.20154v1 |
| `all:"mutually orthogonal" AND all:quantum AND all:Latin` | 06:25:47 | 16 | 2607.12933v2, 2603.02334v1, 2511.03537v3 (MUBs vs classical OLS; no MOQLS) |
| `ti:"Latin squares" AND cat:quant-ph` | 06:25:50 | 13 | 2610.17170v1, 2607.12933v2, 2601.09132v1, 2511.03537v3, 2507.20154v1, 2507.05642v1 |
| `all:"quantum Latin" AND all:"order 7"` | 06:25:54 | 0 | — |
| `all:"quantum Latin" AND all:"order 8"` | 06:25:57 | 0 | — |
| `all:"Problem 16" AND all:Latin` | 06:26:01 | 0 | — |

### Citation indexes, metadata services and direct pages
| index / endpoint | PDT | HTTP | outcome |
|---|---|---|---|
| arXiv API `id_list` = 2607.12933, 2603.02334, 2606.27758, 2507.20154, 2608.29201, 2609.29070, 2610.17170, 2609.24653, 2609.09695, 2607.19969, 2501.00196 | 06:23:36 | 200 | latest versions: 2607.12933**v2** (2026-07-27, "Correction of Theorem 6"), 2603.02334v1, 2606.27758v1, 2507.20154v1, 2608.29201v2 (2026-09-07), 2609.29070v1, 2610.17170v1, 2609.24653v1, 2609.09695v1, 2607.19969v2, 2501.00196v2; no journal-refs |
| arXiv abs page https://arxiv.org/abs/2607.12933 | 06:31:51 | 200 | submission history: v1 Tue 14 Jul 2026 16:05:20 UTC; v2 Mon 27 Jul 2026 07:40:44 UTC; no v3 |
| Semantic Scholar `paper/arXiv:2607.12933/citations` | 06:26:26 | 200 | 2 citers: 2609.29070, 2608.29201 |
| Semantic Scholar `paper/arXiv:2606.27758/citations` (Huang–Li) | 06:26:26 | 200 | 4 citers: 2609.29070, 2609.24653, 2608.29201, 2607.12933 |
| Semantic Scholar `paper/arXiv:2603.02334/citations` | 06:26:26 | 200 | 7 citers: 2610.17170, 2610.16673, 2609.29070, 2609.11796, 2608.29201, 2607.12933, 2606.27758 |
| Semantic Scholar `paper/arXiv:2507.20154/citations` | 06:26:26 | 200 | 8 citers: 2609.29070, 2608.29201, 2607.12933, 2606.27758, doi:10.1002/qute.70293, 2603.02334, 2508.04777, 2508.01972 |
| Semantic Scholar citations of 2609.29070, 2608.29201, 2609.24653 / 2610.17170 | 06:31:51 | 200 | 0 / 0 / 0 / 2 (2610.16673, 2610.16882) |
| Semantic Scholar `paper/search` "mutually orthogonal quantum Latin squares", year 2025-2026 | 06:26:26 | 429 | rate-limited; not retried |
| INSPIRE `refersto:arxiv:<id>` for 2607.12933, 2603.02334, 2606.27758, 2507.20154, 2608.29201, 2609.29070 | 06:26:25 | 200 | query syntax not honoured (returned the unfiltered default listing, total 25,159); superseded by the recid queries below |
| INSPIRE `refersto:recid:3180352` (Ball–Simoens 2607.12933) | 06:29:52 | 200 | 1 citer: 2608.29201 |
| INSPIRE `refersto:recid:2954858` (Han et al. 2507.20154) | 06:29:52 | 200 | 5 citers: 2607.12933, Zang–Zheng–Tian–Shan (Discrete Math. 2026, doi:10.1016/j.disc.2026.115126), 2603.02334, 2608.29201, 2508.04777 |
| INSPIRE `arxiv:2603.02334` / `arxiv:2606.27758` | 06:29:52 | 200 | recid 3125388 / Huang–Li not indexed |
| INSPIRE `t "quantum latin"` sort=mostrecent | 06:26:25 | 200 | 15 records; newest 2610.17170 (created 2026-10-14) |
| OpenAlex `works/doi:10.48550/arxiv.{2607.12933, 2606.27758, 2603.02334, 2507.20154, 2608.29201}`, `doi:10.1103/hxzf-nmpx` | 06:26:25 | 200 | W7168405632, W7166538768, W7133518549, W7077076767, W7204924163, W7164831508; cited_by_count 0 for all |
| OpenAlex `filter=cites:` W7168405632 / W7166538768 / W7164831508 | 06:31:51 | 200 | 0 / 0 / 0 (citation lag) |
| OpenAlex `search="quantum Latin squares"`, from 2025-01-01, by date | 06:26:26 | 200 | 43 works; MOQLS-relevant ones are all listed in the source table; items newer than the previous run screen: 2610.16882, 2610.16673 (order-6 AME), 2610.09900 (background mention only) |
| OpenAlex `search="orthogonal quantum Latin"`, from 2025-01-01 | 06:26:26 | 200 | 14 works; nothing on orders 7/8 |
| OpenAlex abstracts: doi:10.1002/jcd.70002, 10.1016/j.disc.2025.114863, 10.1002/jcd.70021, 10.1016/j.disc.2026.115126 | 06:32:06 | 200 | single-square cardinality papers; abstracts (where present) do not mention orthogonality/MOQLS |
| Crossref `works/10.1103/hxzf-nmpx`; `filter=updates:10.1103/hxzf-nmpx` | 06:26:26; 06:29:52 | 200 | PRL 137, 050202 (published 2026-07-28); `updated-by` a publisher Correction dated 2026-08-28; correction text not located |
| Crossref `query.bibliographic=Thirty-six quantum officers are entangled` | 06:26:26 | 200 | PRL article plus unrelated items |
| Crossref `query.bibliographic=quantum Latin squares`, from 2025, sort=published | 06:26:26 | 200 | 120,376 hits, newest unrelated (noise); superseded by the title query |
| Crossref `query.title=quantum Latin squares`, from 2025 (relevance) | 06:31:51 | 200 | journal QLS items: JCD 2025 (10.1002/jcd.70002), Discrete Math. 2026 (10.1016/j.disc.2025.114863, 10.1016/j.disc.2026.115126), JCD 2026 (10.1002/jcd.70021), Adv. Quantum Technol. 2026 (10.1002/qute.70293); none on MOQLS sets of order 7/8 |
| Crossref `works/10.1002/qute.70293` + OpenAlex | 06:29:52 | 200 | Zang, Zhang, Tian, Fei: orthogonal quantum Sudoku squares (pairs); closed access |
| DataCite `query="quantum latin"`, sort=-created | 06:26:26 | 200 | 36 records; newest 10.48550/arxiv.2610.17170 (created 2026-10-14T07:26:10Z); nothing newer |
| DataCite `query=MOQLS OR "orthogonal quantum Latin" OR "quantum Latin squares"` | 06:26:26 | 200 | 35 records; same newest |
| DataCite `dois/10.5287/ora-8jbg9qebo` | 06:29:53 | 200 | Musto 2019 DPhil thesis on ORA, rights "all-rights-reserved" |
| Google Scholar `"mutually orthogonal quantum Latin squares"`, as_ylo=2026 | 06:26:26 | 200 | 5 results: PRL (cited by 8), 2609.29070, 2610.16882, 2610.16673, EPJ ST essay (10.1140/epjs/s11734-026-02543-0); not blocked |
| Google Scholar `"quantum Latin squares"`, as_ylo=2026, sorted by date | 06:27:12 | 200 | 2610.17170, 2609.29070, 2609.24653, 2609.09695, 2608.29201, 2608.12607, 2607.11800 (ADS), PRL |
| Google Scholar exact title of 2607.12933 | 06:27:19 | 200 | no own record for 2607.12933 (only 2609.29070 returned), so no GS forward-citation list for it |
| Google Scholar `"quantum Latin squares" "non-classical" orthogonal`, as_ylo=2025 | 06:27:25 | 200 | PRL, 2609.29070, 2608.29201 |
| Google Scholar `MOQLS quantum Latin`, as_ylo=2025 | 06:27:32 | 200 | PRL, 2608.29201, 2609.29070 |
| Google Scholar cited-by of PRL 10.1103/hxzf-nmpx (cites=10021449075696744466) | 06:27:51; 06:32:17 | 200 | 8 citers: 2610.17170, 2609.11796, 2610.16673, 2608.01011, 2610.16882, 2608.29201, 2609.29070, 2606.27758 |
| Google Scholar exact titles of 2507.20154 and 2606.27758 | 06:32:12; 06:32:23 | 200 | no own records (returned citing works only) |
| APS abstract page journals.aps.org/prl/abstract/10.1103/hxzf-nmpx | 06:29:53 | 403 | bot wall; PRL version and its Correction not read |
| Simoens homepage https://users.ugent.be/~rnsimoen/en/{publications,talks,research} | 06:31:06 | 200 | preprints: 2607.12933 is still the only QLS preprint; QLS talks: Combinatorics 2026 (Naples, 25 May 2026, 36 officers), DMD2026 (Granada, 29 Jun 2026, "Mutually entangled quantum Latin squares"); nothing later |

## Sources opened
| # | source (version/date) | URL | access level | content checked / bearing on orders 7 and 8 |
|---|---|---|---|---|
| S1 | Ball–Simoens, *Large sets of MOQLS*, arXiv:2607.12933**v2** (27 Jul 2026; v1 14 Jul 2026) | https://arxiv.org/abs/2607.12933v2 ; PDF https://arxiv.org/pdf/2607.12933 | full text (PDF fetched 06:28:40, sha256 2d60d45fbc3e3d1d5f5d6cfec0f7040b6f362ba3d7c7b3e358d3fb02a6e21afe = local copy `review/quantum-latin-2607.12933v2.pdf`); abs page version history | M(n) definition (PDF p.1); Table 2 (p.2): M(7) "2-4", M(8) "2-5" (Table 1, earlier bounds: "2-5", "2-6"); Thm 5 (p.1, proof p.4): M(n) ≤ n − 3; Cor 7 (p.2); §4.1 Rédei remark (p.7); Problem 16 (p.7). No v3, no journal-ref |
| S2 | Ball–Simoens, *Thirty-six quantum officers are entangled*, arXiv:2603.02334v1 (2 Mar 2026); PRL 137, 050202 (2026), doi:10.1103/hxzf-nmpx, Correction 2026-08-28 (Crossref) | https://arxiv.org/abs/2603.02334 | arXiv v1 full text (keyword search + context reading); **PRL version and Correction not read** (APS HTTP 403) | "Open problem 1. Are 2 MOQLS(7) classical?" (PDF p.16; later answered by Huang–Li); non-classical pairs impossible at n = 4, 5, none at 6. Nothing on ≥ 3 squares at n = 7 or on n = 8 sets |
| S3 | Huang–Li, *The Existence of Diagonal QLS with Maximum Cardinality*, arXiv:2606.27758v1 (26 Jun 2026; latest) | https://arxiv.org/abs/2606.27758 | full text (keyword search + §5 reading) | Thm 5.2 (PDF p.28): "There exists a non-classical 2-MOQLS(7)" (MCQLS(7) A with 7 disjoint transversals + classical B); §5: "the existence of MCPQLS(7), MCPQLS(11), and MCPQLS(n) with gcd(n,6) ≠ 1 remains to be determined". No 3-MOQLS, no order-8 MOQLS sets |
| S4 | Han–Zang–Zhang–Tian, *The existence of non-classical orthogonal QLS*, arXiv:2507.20154v1 (27 Jul 2025; latest) | https://arxiv.org/abs/2507.20154 | full text (keyword search + context reading) | Lemma 1.2 (PDF p.2): existence lists for non-classical 2-, 3-, 4-MOQLS(v) all exclude E1 = {2,3,4,6,8,18,p,2p,6p} (so 7 and 8); Thm 3.7 (p.10): non-classical 2-MOQLS(v) for v ≥ 4 except possibly 4–7, with an explicit 2-MOQLS(8); Thm 3.8 (p.12): "For v ≥ 4, there exists a non-classical 3-MOQLS(v), except possibly for v ∈ {4, 5, . . . , 15}" |
| S5 | Zhang–Cao, *Resolvable QLS with maximal cardinality*, arXiv:2608.29201v2 (7 Sep 2026; latest) | https://arxiv.org/abs/2608.29201 | full text (keyword search + context reading) | Lemma 2.2 (PDF p.3): t-RQLS(v) ⇔ a QLS plus t classical QLS forming a (t+1)-MOQLS(v); Example 2.4 (p.4): maximal-cardinality 1-RQLS(8); §5 (pp.19–20): maximal-cardinality 2-RQLS(v) known only for gcd(v,6)=1, v ∉ {5,7,11}, or v = n²; "It remains to determine ... for the remaining orders" (7 and 8 included); such a 2-RQLS "yields a non-classical 3-MOQLS(v)"; "For the case t ≥ 3, we have not yet found an example of a maximal-cardinality t-RQLS(v)" |
| S6 | Lv–Zhang–Cao, *Orthogonal QLS with maximal cardinality from full-rank factorizations*, arXiv:2609.29070v1 (24 Sep 2026; latest) | https://arxiv.org/abs/2609.29070 | full text | pairs with both squares of maximal cardinality (MCOQLS); "The smallest order obtained by our constructions is 64"; open: "What is the smallest order n ≥ 2 for which an MCOQLS(n) exists?" (PDF p.11). Cites S1 only for background; no M(7)/M(8) statement |
| S7 | Zhang–Cao 2609.24653v1; Lv–Cao 2609.09695v1; Zhang–Lv–Cao 2607.19969v2; Das–Kumar 2608.12607v1; Zhang–Ji 2601.09132v1; 2508.01972v1 | arxiv.org/abs/<id> | full text, keyword search only | single-square cardinality/symmetric/hypercube papers; zero occurrences of "MOQLS" or "mutually orthogonal quantum" |
| S8 | 2607.11800v3, 2605.15540v2, 2507.05642v1 | arxiv.org/abs/<id> | arXiv metadata (title/abstract) only | single-square cardinality (order 6 / general); no MOQLS-set content in abstracts |
| S9 | Hontarenko–Życzkowski, *Fractional and quantum Latin squares: real solutions of quantum 36 officers problem*, arXiv:2610.17170v1 (12 Oct 2026) | https://arxiv.org/abs/2610.17170 | full text (keyword search + contexts) | order-6 entangled officers; cites S2 for order 6; no "order 7/8" text, no MOQLS-set classicality statement |
| S10 | Pandya 2610.16673; Bruzda 2610.16882 (both 12 Oct 2026) | arxiv.org/abs/<id> | full text, keyword search | real AME(4,6) (order 6) only; cite S2 for order 6 |
| S11 | Hontarenko–Życzkowski 2609.11796; Shi–Zhang–Zhao–Li 2608.01011 | arxiv.org/abs/<id> | full text, keyword search | AME(2q,q) and seven-party AME states; no MOQLS classicality content (the "seven" refers to parties) |
| S12 | AME review, arXiv:2508.04777 (Rep. Prog. Phys. 2026, doi:10.1088/1361-6633/ae672a) | https://arxiv.org/abs/2508.04777 | full text, keyword search | MOQLS appears only in an AME(6,p)/quantum orthogonal array identity and a citation of S4 |
| S13 | Árnadóttir–Roberson 2501.00196v2; Misawa 2610.09900; 2511.03537v3 | arxiv.org/abs/<id> | full text, keyword search | no orthogonal-QLS-set results (2610.09900 mentions QLS as background only) |
| S14 | Musto, DPhil thesis *Quantum Latin squares and quantum functions* (Oxford 2019; ORA doi:10.5287/ora-8jbg9qebo, all-rights-reserved) | https://www.cs.ox.ac.uk/people/bob.coecke/BenMustoThesis | full text PDF (fetched 06:33:46, sha256 d915c06d93498b98966934353e84968dc8cdaae84e8eae41a11d7c4eabd5eea1), processed in memory, keyword search + context reading | Thm 5.2.16 (PDF p.74): any family of MOQLS of dimension n has size at most n − 1; Example 5.2.2: a non-classical orthogonal pair; nothing on orders 7/8 or on classicality of larger sets |
| S15 | Zang–Zhang–Tian–Fei, *Genuinely quantum solutions of orthogonal Sudoku squares*, Adv. Quantum Technol. 2026, doi:10.1002/qute.70293 | https://doi.org/10.1002/qute.70293 | abstract only (Crossref/OpenAlex; OpenAlex marks it closed access) | orthogonal pairs of quantum Sudoku squares (Sudoku sizes); pairs only |
| S16 | Journal QLS papers 2025–2026: JCD doi:10.1002/jcd.70002; Discrete Math. doi:10.1016/j.disc.2025.114863; JCD doi:10.1002/jcd.70021; Discrete Math. doi:10.1016/j.disc.2026.115126 | doi.org/<doi> | abstract or title only (OpenAlex) | single-square cardinality; abstracts present do not mention orthogonality or MOQLS |
| S17 | Guo, Zenodo doi:10.5281/zenodo.22852779 (2026-09-20) | https://doi.org/10.5281/zenodo.22852779 | metadata only (DataCite/OpenAlex) | single-square cardinality spectrum at order 7; no orthogonality |
| S18 | Simoens homepage: publications, talks, research | https://users.ugent.be/~rnsimoen/en/publications | full pages | S1 is still the only QLS preprint; QLS talks end with DMD2026 (Granada, 29 Jun 2026) |
| — | **Not opened / blocked**: APS PRL page (HTTP 403); UCD 2022 report https://www.ucd.ie/mathstat/t4media/CORreport2022.pdf (HTTP 403; snippet: order-3, 2-unitary notion); EPJ ST essay doi:10.1140/epjs/s11734-026-02543-0 (GS snippet only, popular essay on order 6); phys.org / New Scientist news (secondary, order 6); Zang–Facchi–Tian 2021 J. Phys. A (predates S1, whose Table 1 summarises earlier bounds); Goyeneche et al. 2018 PRA and Paczos et al. 2106.02967 (arXiv metadata only; entangled-QOLS and SudoQ topics) | — | — | — |

## Findings
1. **Problem 16 at n = 8 is still open in the literature.**
   - It remains posed in the latest version of the source (v2). No source located restates it as answered, or answers it for any n ≥ 7.
   - The run's own n = 7 result is internal and unpublished, so it is not literature.
   - The forward citations of 2607.12933 (Semantic Scholar: 2609.29070, 2608.29201; INSPIRE: 2608.29201; OpenAlex: 0) do not mention Problem 16. The string "Problem 16" occurs only in S1 among the 22 full texts.
2. **Published range: 2 ≤ M(8) ≤ 5.**
   - Upper bound: Ball–Simoens Theorem 5.
   - Lower bound: Han et al. Theorem 3.7 (S4, PDF p.10) lists an explicit non-classical 2-MOQLS(8). Zhang–Cao Example 2.4 (S5, PDF p.4) gives a maximal-cardinality 1-RQLS(8). By their Lemma 2.2 this is a non-classical 2-MOQLS(8) with one classical square.
   - Ball–Simoens Theorem 4(2) (PDF p.1) records non-classical pairs for all n ≥ 7.
3. **Size 3: no published construction or exclusion.**
   - Han et al. Theorem 3.8 (S4, PDF p.12) leaves orders 4–15 open. Their Lemma 1.2 (PDF p.2) excludes 8 (8 ∈ E1) from its 2-, 3- and 4-set existence lists.
   - Zhang–Cao §5 (S5) leave maximal-cardinality 2-RQLS(8) undetermined. Such a 2-RQLS would give a non-classical 3-MOQLS(8).
   - Ball–Simoens Corollary 7 does not apply at q = 8.
   - The product construction (Ball–Simoens Theorem 3, from Zang–Facchi–Tian) needs two factors that each carry at least two MOQLS. For 8 = 2·4 the factor 2 carries at most one (Theorem 2) [INFERENCE].
4. **Sizes 4 and 5: neither constructed nor excluded in any source read.**
   - Han et al. Lemma 1.2(4), on non-classical 4-MOQLS, again excludes 8.
   - No source states a classicality theorem for 4- or 5-sets at order 8, for prime-power or characteristic-2 orders, or for n − 3 squares in general. The general bounds found are weaker: n − 1 squares (Musto thesis Thm 5.2.16, S14; Ball–Simoens Theorem 2) and n − 2 squares (Ball–Simoens Theorem 5).
5. **Pairs of two maximal-cardinality squares at order 8 are not addressed.** Lv–Zhang–Cao (S6) construct them only from order 64 upward and pose the smallest order as open.
6. **The rest of the 2025–2026 literature does not bear on M(8).** This covers the Musto–Vicary line, Goyeneche et al., Paczos et al., the Życzkowski group, the Cao group and the Zang–Tian group (S7–S17). It concerns single-square cardinalities, order 6, AME constructions or Sudoku pairs. The newest arXiv "quantum Latin" record is still 2610.17170v1.

## Calibrated wording if correctness is accepted
"Every set of five MOQLS(8) is classical. This resolves the n = 8 instance of Ball–Simoens Problem 16 and improves 2 ≤ M(8) ≤ 5 to 2 ≤ M(8) ≤ 4."
- Use no priority words.
- Do not write "solves Problem 16" or "determines M(8)": sizes 3 and 4 stay open.
- Recheck arXiv for a v3 of 2607.12933 after the next announcement and before any release.

## Limits
- A bounded search miss is not evidence that the statement is new, and nothing here assesses correctness.
- arXiv API searches cover metadata (titles, abstracts, comments, authors), not full text. Full-text keyword checks were run only on the 22 documents listed as "full text" above.
- Google Scholar was reachable (no CAPTCHA), but it has no own records for 2607.12933, 2507.20154 or 2606.27758, so GS forward citations exist only for the PRL paper. Semantic Scholar search returned HTTP 429 (its citation endpoints worked). INSPIRE `refersto:arxiv:` queries were not honoured; the recid route was used, and INSPIRE does not index Huang–Li. OpenAlex citation counts are 0 for every item (index lag).
- Paywalled or blocked, not read: the PRL version of S2 and its 2026-08-28 Correction (APS HTTP 403); S15 body (closed); S16 bodies; the UCD 2022 report (HTTP 403).
- Not checked: MathSciNet, zbMATH, CNKI/Wanfang (Chinese-language journals), Research Square/SSRN/Preprints.org, ResearchGate, conference abstract books (Combinatorics 2026, DMD2026), Simeon Ball's own homepage (not located), theses beyond ORA/DataCite, code repositories, private communications.
- Timing: [INFERENCE from the arXiv schedule] no arXiv announcement occurred between the previous run screen (newest DataCite arXiv record seen then: 2610.17170, created 2026-10-14) and this screen; the next announcement is Sun 2026-10-18 20:00 ET (17:00 PDT). Work submitted after Thu 2026-10-15 14:00 ET, journal-only work and unindexed work can exist. Re-screen after that announcement and before any release, including a check for a v3 of 2607.12933.
- Process deviation (disclosed): the 21 arXiv PDFs used for full-text keyword checks were cached at `/tmp/priority_screen_pdfs/` on the host, outside the permitted write directory. They were left in place (no deletion). The Musto thesis was processed in memory only. No other files were written outside `screening/`.
- Specific to this statement: the order-8 checks were metadata queries (`all:"quantum Latin" AND all:"order 8"`: 0 hits), web searches W3, W6 and W12, and full-text keyword checks for "MOQLS(8)", "QLS(8)", "M(8)" and "order 8/eight". Every order-8 hit was a pair or single-square result (S4, S5, S7). A Chinese-language or journal-only partial result on 3–5-sets at order 8 would not be visible to these routes.
