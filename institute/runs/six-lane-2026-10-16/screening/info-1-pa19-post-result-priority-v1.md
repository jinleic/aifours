<!-- Parent capture 2026-10-18T02:01:59-07:00 of read-only scout PA19PostPriority. Bounded screen; a miss is not novelty; correctness not assessed. -->

NONE-FOUND-IN-SCOPE — no claim of PA(19,8,6) existence or nonexistence, and no claim that A₆(8,7) is 18 or 19, turned up in this screen. The open risk is that I could not read the full texts of Colbourn–Ling 1999 and Cao–Du 2004. No prior equivalent claim was found, so no immediate notice to the parent is needed.

I made no files, ran no code and used no CLI. I give no verdict on whether the candidate is correct. Host date of the screen: 2026-10-18.

## Summary
- **Latest status on record is still open, 18 ≤ N ≤ 19.**
  - Both Rosin preprints are still v1. DataCite records only v1 and the arXiv API returns v1 as latest for both: [2501.17725](https://arxiv.org/abs/2501.17725) submitted 2025-01-29T15:57:43Z, [2505.23881](https://arxiv.org/abs/2505.23881) submitted 2025-05-29T17:45:50Z.
  - The CPro1 repo's latest commit is `827f02b` (2026-06-03T16:22:34Z), the same commit the lane pinned. `designs/packing-array/` holds `result-18-8-6-seed1000.txt` and no 19-8-6 file.
  - The December 2025 NeurIPS MATH-AI workshop version is blocked by OpenReview's browser check. The repo commit "Updated with workshop paper." (2025-12-03) added no PA(19,8,6).
- **Nearest neighbour, not equivalent.** Sadhu, [arXiv:2608.01606](https://arxiv.org/abs/2608.01606) (v1 2026-08-03T02:29Z, v2 2026-08-08T12:06Z, unrefereed), claims pa(5;6) = pa(6;6) = 31 and pa(7;6) ≤ 31. Those are other cells in the same Handbook III.3 six-symbol column. At k = 8 it gives only pa(k;6) ≤ 31, which is weaker than 19. A search of the v2 HTML found no statement about (8;6).
- **Code tables don't cover q = 6.** Brouwer's site lists tables up to "A small table of bounds for 5-ary codes." [Laaksonen–Östergård 2019](https://link.springer.com/article/10.1007/s12095-018-0302-9): "updated tables of Aq (n, d) for q ∈ {3, 4, 5}". 6 is not a prime power, so the linear-code servers don't list it either. The Handbook PA table is the only record for this cell.

## How the objects relate (no equivalence assumed without proof)
- PA(N,k,v) (Rosin/CPro1): N×k array over v symbols, each ordered pair at most once in every N×2 subarray. This is an (n = k, M = N, d = k−1) code over v symbols, so PA(19,8,6) exists ⇔ A₆(8,7) ≥ 19. "A₆(8,7) = 18" ⇔ PA(19,8,6) does not exist (the 18-row array exists, from CPro1).
- The same object appears as PAN(k;g) in the Handbook/Noritake, pa(k;6) in Sadhu, and as k−2 mutually orthogonal partial Latin squares of order v. Noritake: "PA is also called mutually orthogonal partial latin squares and has been applied to optimal disk allocation in Databases."
- A KSP(19), equivalently a KPD({3,4*},19), with 8 parallel classes is the same thing as a PA(19,8,6) whose every column has symbol counts (4,3,3,3,3,3). That is the lane's E0 case.
  - A published KSP(19) with 8 classes would mean PA(19,8,6) exists, directly contradicting the candidate.
  - Nonexistence of that KSP does **not** settle the general PA question, because columns with uneven counts remain.
- **Not equivalent:** CKPD(v) and ICKPD (v ≡ 4 mod 6); KPD({3,4\*\*},v) (two 4-blocks, v ≡ 2 mod 3); KPD({3,5\*},v); near-triangle factors (Phillips–Wallis–Rees 2001).

## Findings
| Source (date/version) | Exact quote (≤40 words) | Bearing on PA(19,8,6) |
|---|---|---|
| [zbMATH 0929.05013](https://zbmath.org/?q=an:0929.05013), Colbourn–Ling 1999 (review by Boyvalenkov) | "A Kirkman school project (KSP) design on v elements consists of the maximum admissible number of disjoint parallel classes each containing blocks of size three except possibly one of size two or four." / "completely resolve the existence problem for v ≡ 4 (mod 3) and nearly completely cover the case v ≡ 1 (mod 3)." | The "(mod 3)" is evidently a typo for mod 6 [INFERENCE]. The review does not say what happens at v = 19. |
| [zbMATH 1064.05039](https://zbmath.org/?q=an:1064.05039), Cao–Du 2004 (publisher summary) | "In this paper we improve the existence results on KPD({3,s*},v) for s=4,5." | Nothing about v = 19 in the summary. |
| Su–Wang, Ars Combin. 91 (2009), lane OCR `sources/ocr/ars91-03.txt:1-3` | "There is a KPD({3,4*},v) containing floor((v-3)/2) parallel classes for every v = 1 (mod 3) with v > 25." | Secondary summary of Černý et al., Phillips et al., Colbourn–Ling and Cao–Du. |
| [Deng–Su, AJC 42 (2008)](https://ajc.maths.uq.edu.au/pdf/42/ajc_v42_p189.pdf), Thm 1.1 | "Let v ≡ 4 (mod 6). Then there exists a CKPD(v) if and only if v ≥ 22." | So everything ≡ 4 (mod 6) from 22 up exists. Su–Wang's "v > 25" therefore leaves 7, 13, 19, 25 unasserted [INFERENCE]. That fits the open Handbook PA cells (8,6) and (11,8). Whether 19 is listed as open or as nonexistent is unknown. |
| [Noritake et al. 2014](https://doi.org/10.11309/jssst.31.1_116) (free on J-STAGE) | "We succeeded in proving the optimality of previously known upper bounds for two arrays and in obtaining improved lower bounds for five arrays." | The new results are PAN(12;8)=19, PAN(13;8)=17 and others. It cites Stardom for 17 ≤ PAN(8;6). (8,6) at 17 rows was solved; 18 and 19 are not in the solved table [INFERENCE: the Japanese body text is garbled]. |
| [Rosin 2505.23881v1](https://arxiv.org/html/2505.23881v1), Table 1 | "(24,7,6) \| (18,8,6) \| (28,10,8) \| (24,11,8) \| (32,11,9) \| (28,12,9) \| (21,14,9) \| (19,15,9)" | 18 rows solved, 19 not listed. |
| [NeurIPS 2025 workshop abstract](https://nips.cc/virtual/2025/loc/san-diego/131107) | "CPro1 successfully solves long-standing open instances for 7 of 16 combinatorial design problems selected from the 2006 Handbook of Combinatorial Designs" | No instance-level detail; PDF blocked. |
| Sadhu 2608.01606v2, §13 item 3 | "the gap is now the widest in the hexary column" (said of pa(7;6): ≤ 31, best known construction 24) | Different cells; not a prior claim on (8,6). |
| [Dinitz Handbook "New Results"](https://site.uvm.edu/jdinitz/?page_id=373), Parts II/III (last edited 9/17/2019), Part VI (10/18/2019) | — | No packing-array or Kirkman school project entries in Parts II, III or VI. |

## Recent preprint and repository screen (DataCite, OpenAlex, arXiv, GitHub)
- **Named independents:** DataCite title list for Long, Vos, Raval, Kirtchakov, M. Nowicki and Liu Zhaobo (125 records). Topic-term searches for Ferudun, Gippini and Sadhu (Ferudun has 727 records; I filtered by title keywords, not a full title list).
  - None concern packing arrays, A₆, or Kirkman packings. Sadhu is the exception noted above.
  - The same crowding pattern as in the earlier lanes shows up:
    - Long: SW(25,16), SW(27,16), SW(29,16), 2026-10-15T20:42Z.
    - Kirtchakov: F_c(25) ≥ 5, 2026-08-07.
    - Gippini: a deletion code, 2026-09-29.
    - Vos: CPCW codes.
    - Raval: L(12,3).
  - SERAPHIEL is M. Nowicki with an AI co-author, on positive matrix realizations, 2026-09-29; unrelated. Liu Zhaobo's records are in control theory; unrelated.
- **Topic searches:**
  - DataCite titles ("packing array", "Kirkman school/packing", "orthogonal partial Latin"): 6 hits, none relevant.
  - DataCite descriptions mentioning CPro1 or the Handbook, 2025–2026: 9 hits; none touch (8,6).
  - OpenAlex "packing array" since 2015: 32 hits. [Kampel et al., JCD 2023](https://doi.org/10.1002/jcd.21876) is about balanced covering arrays; its abstract gives no (8,6) parameters.
  - Citing works of Colbourn–Ling (zbMATH 8, OpenAlex 18): no title points at v = 19.
  - arXiv "packing array" search: noise only.

## Significance (separate from correctness and priority)
- I counted a result as major if it brings a new method, solves a prominent problem, beats the state of the art under matched assumptions, or has a downstream consequence.
- The candidate is none of those. It would close one Handbook III.3 cell exactly, at A₆(8,7) = PAN(8;6) = 18.
  - The 2007 Handbook range was 12–19; the 17 is Stardom 2001 and the 18 is CPro1 2025.
  - It lowers the pair-count upper bound by 1, using a certified nonexistence computation.
- It belongs to the same class as Noritake 2014 (exact cell values found by SAT) and Sadhu 2026 (exact cells from exhaustive refutation). Calibrated value: a modest specialist result.
- Side result: no KPD({3,4*},19) with 8 classes. This could resolve a possible exception in the Kirkman packing literature, or it could already be known. Which one depends on the unread Colbourn–Ling / Cao–Du text.
- An unrefereed earlier claim on (8,6) would remove gate eligibility without saying anything about correctness. None was found as of this screen.

## Access holes
- **Colbourn–Ling 1999 and Cao–Du 2004 full texts.** Both are free in Elsevier's open archive; Crossref shows Cao–Du under the open-access licence from 2013-08-22. Every route failed:
  - ScienceDirect: 403.
  - ACM Digital Library: 403.
  - CORE: 403.
  - IA Scholar: anti-bot check, not bypassed.
  - fatcat: timed out.
  - Wayback Machine API: 429.
  - Semantic Scholar API: the reader intercepted the request.
- **Other papers not read:**
  - Phillips–Wallis–Rees, JCMCC 28 (1998): no PDF found.
  - Phillips–Wallis–Rees, AJC 2001: image-only PDF; OCR would need code execution.
  - Rees–Wallis survey: paywalled.
  - Cao's 2002 thesis (in Chinese).
  - Stardom's thesis.
  - Stevens–Ling–Mendelsohn 2002: abstract seen only as search-result prose. It says its design-packing bound beats or matches Plotkin when k ≥ g+1. The 2006 Handbook and Rosin still record 19, so it apparently doesn't improve this cell [INFERENCE].
  - The Handbook III.3 table itself: seen only via Noritake's garbled copy plus the parent-verified Rosin row.
- **Zenodo API:** 403, so DataCite stood in for it.

## Parent actions
1. Get Colbourn–Ling's result for v ≡ 1 (mod 6) through a lawful browser or institutional route **before acceptance**. A published KSP(19) with 8 classes would contradict the E0 UNSAT result.
2. Just before the gate, re-run the DataCite screen, for example `https://api.datacite.org/dois?query=titles.title:("packing array" OR "Kirkman school") OR descriptions.description:("packing array" OR CPro1)&sort=-created`. Also check Sadhu's arXiv listing and the CPro1 commit log.

## Local files read
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening/info-1-packing-array19-contract.json`
- `/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19/README.md:12-27`
- `.../packing-array19/sources/ocr/ars91-03.txt:1-3`
- `.../packing-array19/sources/cpro1/COMMIT.txt`
- `.../packing-array19/sources/cpro1/CPro1_design_definitions_packing-array_problem_def.py:7-8` (OPEN_INSTANCES `[[32,5,6],[24,7,6],[26,10,8],[23,11,8]]`)
- `.../packing-array19/sources/cpro1/CPro1_design_definitions_packing-array_README.md`
