# Status search — 2026-10-14

**Verdict: no resolution found; not proof of openness. Current-status label: uncertified-open.** This log concerns both the book-wide universal assertion and the selected finite cases57/87. A construction at either finite order would be partial progress on the book's question, not its full solution.

## Exact question and latest primary attestation

Book p.428 / PDF444, `book-excerpt.txt` lines24–25:

> 对于任意 v = 6t + 3, t ⩾ 1, 是否存在 v 阶柯克曼三元系大集？

Faithful English: For every v=6t+3 with integer t≥1, does a large set of Kirkman triple systems of orderv exist?

Chen Wang, **2026-07-23**, [arXiv:2607.21521](https://arxiv.org/abs/2607.21521): definitions in§1 agree with the book; §1 states that the corresponding LKTS existence problem “remains far from settled.” Section4 records57 and87 as the smallest remaining cases and the only possible exceptions below200. Full primary PDF/text opened and saved. This is a dated primary attestation, not a proof that a later resolution is absent.

The book's specific earliest case21 is solved by Zhou–Chang, [DOI10.1007/s10623-009-9325-8](https://link.springer.com/article/10.1007/s10623-009-9325-8), online2009-09-16 / journal2010, whose opened primary abstract also constructs39.

## Search scope and later citing works

Searches actually issued included:

- `site:arxiv.org "Kirkman" "large" after:2026-07-23 before:2026-10-15`;
- `"LKTS(57)" OR "LKTS(87)" OR "LKTS (57)" OR "LKTS (87)"`;
- `"large sets of Kirkman" 2026 2025`;
- exact article-title searches for the Chang–Zhou survey, Liu–Lei2023, Xu–Ji2021/2024, and Zheng–Chang–Zhou2016/2017;
- the literature scout additionally reports arXiv API queries sorted by date and a Crossref Kirkman-title search; its exact report and corrections are preserved in `../evidence/literature-scout.txt` and `literature-scout-corrections.txt`. That report is discovery evidence, not a substitute for the primary pages opened by the integration owner.

The latest relevant arXiv result located was Wang2026. No later resolution of57,87 or the universal question was found.

### Citation-index checks performed on2026-10-14

1. OpenAlex identifies Wang2026 as `W7170252291`, publication_date2026-07-23, DOI10.48550/arxiv.2607.21521. The explicit citing-works query returned **0 indexed works**:
   `https://api.openalex.org/works?filter=cites:W7170252291&per-page=100&select=id,title,publication_date,doi`
   Raw response: `status-20261014-wang-citing.json`.
2. OpenAlex identifies Chang–Zhou's survey as `W1993518998`, DOI10.1016/j.jcta.2012.12.001. The explicit citing-works query returned **20 indexed works**, all on one page:
   `https://api.openalex.org/works?filter=cites:W1993518998&per-page=100&sort=publication_date:desc&select=id,title,publication_date,doi`
   Raw complete list: `status-20261014-survey-citing.json`.
3. A Semantic Scholar API URL was attempted through the reader; the reader failed to extract its arXiv identifier. This is an access/tool failure, not a zero-citation result.

The recent survey-citing works examined include:

| Work | Dated primary record | What was actually opened / relevance |
|---|---|---|
| Tan–Zhou, *Tilings of H_q(n,w) with optimal(n,d,w)_q-codes* | **2026-06-02**, DOI10.1007/s10623-026-01853-7 | Primary publisher abstract and references, saved as `tan-zhou-2026-tilings-publisher.txt`. Its abstract announces coding-space tilings, including complete binary weight-three tiling spectra; it does not assert an LKTS57/87 or the universal LKTS result. The full subscription body was not available, so no claim about every hidden theorem is made. |
| Tan–Zhou, minimum-colorable derived designs | **2025-06-23** journal, DOI10.1007/s10623-025-01677-x; arXiv2503.11934 | Full author preprint opened; RDSQS-to-LKTS family retains the factor3 and misses57/87. |
| Xu–Ji, *Special overlarge sets of Kirkman triple systems* | **2024-04-05**, DOI10.1007/s10623-024-01386-x | Primary abstract opened; OLKTS⁺ replaces RDSQS in the implication toLKTS(3v), notLKTS(v). |
| Liu–Lei, *More results on large sets of Kirkman triple systems* | **2023-04-29**, DOI10.1007/s10623-023-01221-9; arXiv2210.06214 | Full preprint and primary abstract opened; exact theorem hypotheses recorded in recursion-notes.md. |
| Xu–Ji, *New results on LR-designs and OLKTSs* | **2022**, DOI10.1016/j.disc.2022.112948 | DOI metadata opened; mathematical body not recovered. Not claimed to have been fully audited. |
| Xu–Ji, orders2^(2n+1)+1 | **2021**, DOI10.1016/j.disc.2021.112373 | DOI metadata and later primary attribution opened; original body blocked. Indexed extra-family statement explaining147 remains explicitly source-limited. |
| Zheng–Chang–Zhou, direct constructions / prime-power sizes | online**2016**, journal**2017**, DOIs10.1007/s10623-016-0197-4 and10.1007/s10623-016-0315-3 | Primary abstracts and appendices opened and saved. |
| Zhou–Chang, *A new result on Sylvester's problem* | **2014**, DOI10.1016/j.disc.2014.04.022 | DOI metadata opened; original body not recovered. No unseen theorem is asserted. |

OpenAlex's June1 date for the2026 tiling paper differs from the publisher's June2 online date; the primary publisher date is used above. OpenAlex citation indexing is incomplete/lagged: notably its survey-citing list need not include every actual reference such as Wang's newer preprint. A zero indexed citing-work count is not evidence that no newer relevant work exists.

## openai/math corpus screen

Parent-reported observation, supplied in the review instruction: no matching family was found in the local openai/math clone at **adc7f1241** or in the remote listing checked **2026-10-14**. This worker did not replay that corpus search. The absence of a family in that corpus is not a mathematical nonexistence or open-status proof.

## Access limitations and conclusion

Chang–Zhou2013 survey metadata were readable but its full mathematical body was blocked by publisher/API/browser access failures. Several older direct-construction details and the original Xu–Ji2021 extra-family statement were not independently primary-body verified. These gaps are not filled by invented citations or guessed group generators.

The record supports: **the latest opened primary source attests the universal problem and57/87 as unresolved in July2026; the October14 search found no resolution.** It does not certify contemporary openness, unrestricted nonexistence, or the completeness of the literature search.
