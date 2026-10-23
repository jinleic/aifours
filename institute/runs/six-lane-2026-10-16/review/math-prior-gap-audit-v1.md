# MathPriorGapAudit report (verbatim, read-only scout)

Recorded 2026-10-17 15:17:21 PDT. Leads only until parent-read; the parent directly read the DataCite records for Vos (10.5281/zenodo.22076107) and Raval (10.5281/zenodo.22639692) and exactly checked all nine Vos codes and the L(12,3) witness coverage.

No earlier claim found for any of the eight targets. I searched the new surfaces you listed and found nothing that constructs LKTS(57), LKTS(87), RDSQS(52), the 19-colourings for mcDSQS(38), gcDCQS(20⁴:0), mcDSQS(80) or the mcDSQS(5·4ⁿ) family. No published theorem or code database covers those exact parameters or colouring/resolution requirements either. Mathematical correctness is not in question. Not finding a claim does not make these results new: NOVELTY-UNCLEAR stays as it is.

**Timing:** I have no host clock. API timestamps put the run around 2026-10-17 21:30–22:10 UTC: DataCite returned a record registered at 2026-10-17T21:33:31Z, and zbMATH reported 2026-10-17T22:05:29Z.

**mcDSQS(80) filename:** there is no separate verdict file. It is covered in `review/gcdcqs20-parent-verdict.md`, plus `mcdsqs80-codex-verify-v1.*` and the `mcdsqs80-parent-*` folders. The other gcDCQS files are `gcdcqs20-parent-verdict.md`, `gcdcqs20-lean-parent-verdict.md` and `gcdcqs20-priority-audit.md`.

## Outcome table

| Target (definition taken from the verdicts) | Earlier claim found | Exact URL / version / date | What I read | Applicability | Access limits | Ledger correction |
|---|---|---|---|---|---|---|
| **LKTS(57)**: all triples of a 57-set split into 55 KTS(57) | NONE-FOUND-IN-SCOPE. Nearest object: Topalova–Zhelezova classify single cyclically resolvable STS(57), not a large set | [doi:10.3390/math13020212](https://doi.org/10.3390/math13020212), 2025-01-10. Only citing work: [Axioms 15:762](https://doi.org/10.3390/axioms15100762), 2026-10-13, on 2-(64,4,1) designs | Abstract (from OpenAlex): "There are 2,353,310 cyclic STS(57)s. We establish that 155,966 of them are cyclically resolvable yielding 3,638,984 point-cyclic resolutions" | A classification of single KTS(57). It makes no claim about pairwise disjoint KTS(57) | MDPI page returned 403; the abstract came via OpenAlex | None required |
| **LKTS(87)** | NONE-FOUND-IN-SCOPE | Same searches as LKTS(57) | Same | No family or database reaches 87 | Same | None required |
| **All admissible orders below 200** (combined with Wang's survey) | No earlier aggregate claim. Wang lists 57 and 87 as the only exceptions | Wang [arXiv:2607.21521v1](https://arxiv.org/abs/2607.21521v1) is still v1 (arXiv API, today); local copy lines 487–491 | "Combining Table 1, Denniston's tripling construction, the construction of Wang and Shi [18], the family obtained by Xu and Ji [19], and Corollary 3.8, an LKTS(v) is known to exist for every v < 200" | Order 147 is reachable only through the second Xu–Ji 2021 family; none of Wang's other listed routes gives it. New support: zbMATH 1467.05022 review (Horák): "a LKTS(v) has been constructed for two infinite classes of v." | The paper's body is still unread. Crossref shows an Elsevier open-archive licence for it from 2025-06-01, but ScienceDirect returns 403 to the scout | Recommended: change the 147 caveat to say the body is free to read (open archive) but was blocked to the scout, and that zbMATH confirms "two infinite classes" without giving the formula |
| **RDSQS(52)**: SQS(52) whose derived STS(51) is resolvable at every point | NONE-FOUND-IN-SCOPE. Near-objects that do not match: (1) Meng–Gao–Wu DRSQS, (2) arbitrary SQS(52) (Sage/LJCR), (3) Liu–Feng symmetric cyclic SQS, (4) Dobson et al. CQS(52²) | DRSQS: [doi:10.1007/s10623-024-01356-3](https://doi.org/10.1007/s10623-024-01356-3), 2024. Liu–Feng: [Zenodo 22852801](https://doi.org/10.5281/zenodo.22852801), 2026-09-20. Dobson et al.: [Zenodo 16902245](https://doi.org/10.5281/zenodo.16902245), 2025-08-21 | DRSQS abstract: "If a Steiner quadruple system has two mutually orthogonal resolutions, the design is called doubly resolvable." Liu–Feng file is integer computations for lemmas. Dobson et al.: "M-cyclic CQS(g²) for g = 20,28,40,44,52" | DRSQS concerns two orthogonal resolutions of the whole SQS, not derived designs; its recursion cannot give 52. Sage and LJCR give arbitrary SQS(52). Dobson et al.'s object has 2g = 104 points. The Kiermaier–Krčadinac–Wassermann (KKW) tables stop at v ≤ 50 | The Tan–Zhou journal version and the Tilings journal version are paywalled (Springer page reports no access) | None required |
| **mcDSQS(38)** (the 19-colourings; the SQS(38) itself is already disclosed as KKW record 143) | NONE-FOUND for the colourings. Another public SQS(38), Sage's `_SQS38`, carries no colouring claim | Sage develop branch, `steiner_quadruple_systems.py` blob aa3355dc…; KKW dataset concept [Zenodo 17153237](https://doi.org/10.5281/zenodo.17153237); [KKW in DCC 94:157](https://doi.org/10.1007/s10623-026-01888-w), 2026-07-07, open access | Sage code: `_SQS38` is commented "From the La Jolla Covering Repository". DataCite: KKW versionCount 1, metadata updated 2025-09-30. KKW full text: no colouring, chromatic-index or resolvability terms | No colourings anywhere. Each derived design's 12¹⁸6 colouring profile matches the Hanani triple system definition [INFERENCE: definition recalled, not re-read]; a full-text search for "Hanani triple" found nothing relevant | I did not test whether the LJCR/Sage SQS(38) is isomorphic to the certificate; the gate does not depend on it | Recommended: close the "later KKW versions not checked" hole (only one version exists) |
| **gcDCQS(20⁴:0)**: 4 groups of 20, empty stem, good colourings (40 classes, 10 hole-free) | NONE-FOUND-IN-SCOPE. Nearest object: Dobson et al. CQS(40²) on 80 points | Same Zenodo 16902245 | Dataset description only | Two groups rather than four, no colourings, so not the target. A CQS is not an H-design | Zenodo pages 403. OpenAlex full-text search does not even match "gcDCQS" in Tan–Zhou, so that index cannot test this target | None required |
| **mcDSQS(80)** | NONE-FOUND-IN-SCOPE | Sage `steiner_quadruple_system` builds an arbitrary SQS(80) only | Sage catalog and module | No colouring claim. Searching "diameter perfect" (the q′₀(3,4,80) = 41 form) found nothing. KKW covers v ≤ 50 only | Same | None required |
| **mcDSQS(5·4ⁿ), n ≥ 3** | NONE-FOUND-IN-SCOPE | — | — | No other theorem gives these orders. The family's priority depends entirely on gcDCQS(20⁴:0) | — | None required |

## Surfaces checked (all found nothing relevant)

- **DataCite**, all clients and Zenodo only:
  - Griffin Long and "agent-afk": only the SW(25,16) record family.
  - "Kirkman" since 2025 (78 hits); large set or overlarge plus triple systems (18); acronym queries.
  - Zenodo design terms since 2025-06 (350); STS/SQS/large-set terms since 2026-08; SAT and prescribed-automorphism notes since 2026-06.
  - There are many recent AI-agent combinatorics notes on Zenodo (for example z(32;2) = 189 and C(16,5,3) ≥ 62). None touches these targets.
- **OpenAlex full text:** large sets of Kirkman, disjoint KTS, double resolvability, overlarge, mcDSQS, RDSQS, Steiner quadruple, derived designs, candelabra quadruple, Hanani triple, 2-resolvable, diameter perfect. Also Ji's and Zhou's journal output since 2025.
- **zbMATH Open API:** Kirkman titles 2023–2026 (6 records) and quadruple titles 2025–2026 (17).
- **Other indexes:** HAL; Crossref posted-content preprints (SSRN, OSF, Research Square, Preprints.org and similar).
- **Code and tables:**
  - The Sage catalog has no large sets and no derived-design resolution or colouring code. It carries the TODO "Implement DerivedDesign".
  - CPro1 lists 23 design families, none relevant.
  - Krčadinac's table covers v ≤ 50 plus rotational SQS(46) and SQS(92).
- **GitHub:**
  - griffinwork40's math repos are D21-Kissing and Shannon capacity only.
  - openai/math HEAD is still `1581d4c` (2026-10-12).
  - Repository searches returned only astronomy hits.
- **Web leads only:** Chinese-language searches and exact-string searches.

Earlier screens listed some Elsevier sources as 403. Chang–Zhou 2013 is free to read under Elsevier's open archive from 2017-04-01, Xu–Ji 2021 from 2025-06-01 and Xu–Ji 2022 from 2026-09-01. The 403 is a bot block, which I did not try to get around. Opening Xu–Ji 2021 in a normal browser would close the order-147 hole.

Out of scope, not assessed: the Axioms paper on point-cyclic resolutions of 2-(64,4,1) designs (2026-10-13) may matter for the info-2 point-cyclic lane.

```json
{
  "scope": "new-surface priority audit; read-only; no proof reruns",
  "timestamp": "no host clock; API-observed 2026-10-17 ~21:33Z-22:05Z",
  "targets": [
    {"target": "LKTS(57)", "outcome": "NONE-FOUND-IN-SCOPE",
     "near_objects_not_matching": ["Topalova-Zhelezova 2025 cyclically resolvable STS(57) classification, doi:10.3390/math13020212", "Sage kirkman_triple_system (single KTS)"],
     "ledger_correction": "none required"},
    {"target": "LKTS(87)", "outcome": "NONE-FOUND-IN-SCOPE", "ledger_correction": "none required"},
    {"target": "all admissible v<200 corollary", "outcome": "NO EARLIER AGGREGATE CLAIM FOUND",
     "premise_note": "147 needs the second Xu-Ji 2021 family; zbMATH 1467.05022 review: 'two infinite classes of v'; body open-archive since 2025-06-01 but 403 to scout",
     "ledger_correction": "recommended: refine the 147 caveat"},
    {"target": "RDSQS(52)", "outcome": "NONE-FOUND-IN-SCOPE",
     "near_objects_not_matching": ["DRSQS (Meng-Gao-Wu 2024, orthogonal resolutions)", "arbitrary SQS(52) in Sage/LJCR", "Liu-Feng symmetric cyclic SQS (Zenodo 22852801)", "Dobson et al. CQS(52^2) on 104 points (Zenodo 16902245)"],
     "ledger_correction": "none required"},
    {"target": "mcDSQS(38) colourings", "outcome": "NONE-FOUND-IN-SCOPE",
     "near_objects_not_matching": ["KKW record 143 (already disclosed)", "Sage _SQS38 from LJCR, no colourings, isomorphism untested"],
     "ledger_correction": "recommended: KKW concept DOI 17153237 has versionCount 1; close the access hole"},
    {"target": "gcDCQS(20^4:0)", "outcome": "NONE-FOUND-IN-SCOPE",
     "near_objects_not_matching": ["Dobson et al. CQS(40^2) on 80 points, two groups, no colourings"],
     "ledger_correction": "none required"},
    {"target": "mcDSQS(80)", "outcome": "NONE-FOUND-IN-SCOPE", "ledger_correction": "none required"},
    {"target": "mcDSQS(5*4^n), n>=3", "outcome": "NONE-FOUND-IN-SCOPE",
     "note": "priority depends entirely on gcDCQS(20^4:0)", "ledger_correction": "none required"}
  ],
  "access_limits": ["Zenodo pages/files 403", "ScienceDirect 403 on open-archive/bronze bodies (Xu-Ji 2021, Chang-Zhou 2013)", "Springer paywall: Tan-Zhou 2025 and Tilings 2026 bodies", "MDPI 403", "Semantic Scholar tool failure", "Crossref 429 once", "OpenAlex full text misses the token gcDCQS", "CNKI, MathSciNet, Google Scholar not searched"],
  "writes": "none"
}
```
