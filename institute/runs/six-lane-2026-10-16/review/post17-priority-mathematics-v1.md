# Post-17:00 PDT primary-source status/priority refresh — mathematics slice (v1)

Writer: read-only subagent `Post17PriorityMath`. Exclusive new file; no computation, downloads, code, external contact, publication or edits elsewhere. Bibliographic refresh only; no correctness acceptance or strengthening.

## Gate and retrieval clock

- Local preparation only before the gate; prepared source list sent to Main at `/bin/date` 2026-10-18T16:57:29-0700; no web read before the gate.
- Gate: `/bin/date` **2026-10-18T17:02:08-0700** (≥17:00:00 PDT). Main's IRC, received after that stamp: "Your observed17:02:08 satisfies the gate."
- Every web retrieval below falls inside one batch bounded by `/bin/date` stamps taken immediately before and after it:
  - **B1** 17:02:08–17:03:01
  - **B2** 17:03:01–17:03:50
  - **B3** 17:03:50–17:05:04
  - **B4** 17:05:04–17:06:08
  - **B5** 17:06:08–17:07:38
  - **B6** 17:07:38–17:08:18
- Baseline (prior records, not re-derived): [ME3 screen](../screening/math-1-me3-post-candidate-priority-v1.json), [Sun k6 screen](../screening/math-1-sun-coset6-post-candidate-priority-v1.md), [Sun k7 precheck](../screening/math-1-sun-coset7-priority-precheck-v1.md), [Sun k5 spot-check](../screening/math-1-sun-coset5-parent-primary-spotcheck-v1.json), [PH comparison v2](phase-type-complex3-priority-parent-comparison-v2.md), [Olson scout](olson-par-priority-scout-v1.md) with the K01/S1(g)/ROT-KP/ROT-ZR verdicts, [LKTS audit](lkts57-87-priority-audit.md), [RDSQS52 audit](rdsqs52-priority-audit.md), [mcDSQS38 audit](mcdsqs38-priority-audit.md), [gcDCQS20 audit](gcdcqs20-priority-audit.md), [gcDCQS32 scout](gcdcqs32-priority-scout-v1.md), [§4(3) scout](tz43-priority-scout-v1.md), [plan](post17-priority-refresh-plan-v1.json), and the [final-report draft v3](final-report-draft-v3.md) rows 27–35, 57, 68–84 and 105–123.

## Global limits (apply to every group)

1. **The Sunday-evening arXiv mailing was not visible in this window.** math.PR/new, math.CO/new and math.GR/new (B1/B2) and math.CO/new again (B5) all read "Showing new listings for Friday, 16 October 2026". math.CO/recent (B6) listed its newest mailing as "Fri, 16 Oct 2026". Anything not announced by the 16 Oct mailing is outside this refresh unless a search index already held it. **The post-17:00 arXiv re-screen therefore does not include a Monday 19 Oct mailing.** A later bibliographic-only listing check would be needed to cover it.
2. The arXiv export API returned HTTP 429 for `au:Zhou_Junling` and `au:Tan_Yuli` (B2). The arXiv web author search was used instead (B3) and succeeded. arXiv search covers metadata (titles, abstracts, comments), not full text.
3. Not used: Google Scholar, Semantic Scholar, MathSciNet, CNKI, the Zenodo API and new zbMATH queries. No paywalled body was re-attempted. Every earlier access hole remains open unless this report says it is closed.
4. `NONE_FOUND_IN_BOUNDED_REFRESH` means that the listed sources show no new equivalent, contradiction, prior claim or status change. It is not evidence of novelty or priority, and it does not support "first".

**Escalations: none.** No new equivalent theorem, contradiction, prior claim or counterexample was located for any named group, so nothing was sent to the parent as a source-level conflict.

## Summary

| Group | Refresh verdict | Retained prior status | Change |
|---|---|---|---|
| ME(≤3) minimum SCV | NONE_FOUND_IN_BOUNDED_REFRESH | NONE_FOUND_IN_BOUNDED_POST_CANDIDATE_SCOPE; NOVELTY-UNCLEAR | None. Latest versions are unchanged; the Monday mailing was not visible. |
| Sun k=6 / k=7 / k=5 | NONE_FOUND_IN_BOUNDED_REFRESH | k6: PARTIAL_OVERLAP_FOUND, NOVELTY-UNCLEAR. k7: OPEN, partial only. k5: PRIOR-CLAIM | None |
| PH three-pole, a>c>0, b>0 | NONE_FOUND_IN_BOUNDED_REFRESH | NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR, with the Mocanu and Verbeken–Ginis attributions | None |
| Olson K01 / S1(g) / ROT-KP / ROT-ZR | NONE_FOUND_IN_BOUNDED_REFRESH | Partial scopes only; no priority claim | None |
| LKTS57/87, RDSQS52, mcDSQS38, gcDCQS20/32, §4(3) | NONE_FOUND_IN_BOUNDED_REFRESH (each) | As in the gate rows | Metadata only: KKW is now journal-published, and the KKW dataset has 1 version |

## A. ME(≤3) minimum SCV (highest priority)

**Matched target (unchanged).** Every continuous matrix-exponential law of order ≤3, with no sign structure on α or A, has SCV ≥ v_cos. Here v_cos is the exact minimum over e^{−t}(1−cos(ωt−φ)), not the rounded 0.200902. Equality holds in D1, and the inequality is strict on every D2 cone. The claim is for order ≤3 only, not arbitrary order; ME(n) for n≥4 remains open.

| Batch | Source | Version / date seen | Read scope | Quote (≤40 words) | Matched comparison |
|---|---|---|---|---|---|
| B1, B4 | Battagliola–Peralta, [arXiv:2609.14612](https://arxiv.org/abs/2609.14612) | v1, 2026-09-13. The [v2 URL](https://arxiv.org/abs/2609.14612v2) returned HTTP 404, so only v1 exists. | abstract | "The enlargement leaves the infimum unchanged from that of the classical cosine-squared construction." | Adjacent family: common-damping harmonic densities at general order N, with a numerical two-parameter search. The abstract gives no global D2 bound and no certified order-3 bound. No change. |
| B1 | Battagliola–Peralta, [arXiv:2608.29143](https://arxiv.org/abs/2608.29143) | v1 only, 2026-08-29 08:41:52 UTC | abstract | "gives the kernel a Laplace transform with a single repeated real pole" | Single repeated real pole only, not full ME(3). No change. |
| B1 | Battagliola–Peralta, [arXiv:2604.26304](https://arxiv.org/abs/2604.26304) | v1 only, 2026-04-29 05:09:01 UTC | abstract | "an explicit family of concentrated matrix-exponential densities for the unit delay" | Asymptotic construction, not an order-3 optimum. No change. |
| B1 | [arXiv API au:Peralta_Oscar](https://export.arxiv.org/api/query?search_query=au:Peralta_Oscar&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending), 10 newest | 2609.14612v1, 2608.29143v1, 2607.24533v1, 2605.15395v1, 2604.26304v1, 2604.08889v1, 2603.28047v1, 2603.26003v1, 2507.15637v2, 2506.23685v1 | ID list (the feed returned untitled entries) | — | The top entry is unchanged since the 05:35 screen. Titles of the older IDs were not re-read. |
| B1 | [arXiv API au:Battagliola_Maria](https://export.arxiv.org/api/query?search_query=au:Battagliola_Maria&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending), 10 newest | Newest: 2609.14612v1, 2608.29143v1, 2607.24533v1, 2607.19043v1, 2604.26304v1 | ID list | — | The top entry is unchanged. |
| B3 | [arXiv search "matrix-exponential" "coefficient of variation"](https://arxiv.org/search/?query=%22matrix-exponential%22+%22coefficient+of+variation%22&searchtype=all&order=-announced_date_first&size=25) | 3 hits: 2609.14612; 2608.06414 (Luzon, two-phase PH queues, v2 2026-08-10); 1901.08627 (2019) | result snippets | — | No new ME(3) result. |
| B1 | [math.PR/new](https://arxiv.org/list/math.PR/new) | Friday 16 Oct 2026 listing, 68 entries | All titles and abstracts, plus a grep for phase-type, matrix-exponential, coefficient of variation, concentrated, Erlang and SCV | — | No relevant entry. The only "matrix exponential" hit is an unrelated diffusion-sampling replacement. |

**Verdict A: NONE_FOUND_IN_BOUNDED_REFRESH.** Status retained: NONE_FOUND_IN_BOUNDED_POST_CANDIDATE_SCOPE; NOVELTY-UNCLEAR. The 05:35 observation that the abstract lookup and author feeds still list v1 still held at B1 and B4.

Not covered: the Monday mailing. Also unread, as in the baseline: the Horváth–Telek 2024 book (Ch. 4), Bladt–Nielsen 2017, Fackrell 2003 and Bean–Fackrell–Taylor 2008. The OpenAlex citers of HSTZ were not re-run.

## B. Sun's disjoint-coset conjecture: k=6 (gate), k=7 (open), k=5 (prior claim)

**Matched target.** Pairwise disjoint left cosets of finite-index subgroups of **any** group, with subgroups allowed to coincide, force some pairwise index gcd ≥k. The gate is k=6; k=7 is open with partial results only.

Adjacent, not matched:
- integer-only results (O'Bryant k≤20; Fornal–Sun);
- the Herzog–Schönheim conjecture;
- coset covers;
- Ginosar's transfer question.

| Batch | Source | Version / date seen | Read scope | Quote (≤40 words) | Matched comparison |
|---|---|---|---|---|---|
| B2 | Sun, [MathOverflow Q316709](https://mathoverflow.net/questions/316709), via Stack Exchange API | asked 2018-12-02; score 9; **0 answers** | full question text | "In 2010, Zhu Gong … confirmed the conjecture for k=5 (again with G a general group). Since 2010, there is no further progress on the conjecture." | Status testimony unchanged. The API output does not show a last-edit time (access limit; the baseline recorded 2026-01-05). |
| B2 | Menon, [arXiv:2608.15873](https://arxiv.org/abs/2608.15873) | v1 only, 2026-08-16 17:49:51 UTC; ancillary verify-counterexample.g not opened | abstract | "(6,6,6,10,15) is A_5-harmonic but not Z-harmonic" | A transfer counterexample, not a gcd theorem. The baseline argument that it is not a k=7 counterexample stands. No change. |
| B2 | Margolis–Schnabel, [arXiv:1803.03569](https://arxiv.org/abs/1803.03569) | v1 only, 2018-03-09 | abstract | "pairwise trivially intersecting cosets and n ≤ 4 then [G:U_1],...,[G:U_n] are harmonic integers" | Partial overlap: Cor. 3.9, from the baseline full-text read, is retained. No change. |
| B4 | Garonzi–Margolis, [arXiv:2509.25118](https://arxiv.org/abs/2509.25118) | v2 (2026-05-05) is the latest | abstract | "We prove this conjecture for simple groups and for symmetric groups." | Herzog–Schönheim, a different conjecture. No change. |
| B4 | Fornal–Sun, [arXiv:2607.24655](https://arxiv.org/abs/2607.24655) | v1 only, 2026-07-27 | abstract | "Consider k pairwise disjoint residue classes a_i (mod m_i)." | Integer residue classes and an asymptotic bound; no statement about groups. No change. |
| B6 | Sambale, [arXiv:2609.09052](https://arxiv.org/abs/2609.09052) | v1 only, 2026-09-08 | abstract | "every subgroup occurring in an irredundant cover of an arbitrary group by n cosets has index at most 2^{n−1}" | About covers, not the gcd conjecture. No change. |
| B3 | [PPL057](https://prizeproblems.org/problems/057/) | "Checked 2026.07.27"; "Open since 2004" | full page | — | Listing unchanged; a status lead only. |
| B3, B4 | arXiv search ["disjoint cosets"](https://arxiv.org/search/?query=%22disjoint+cosets%22&searchtype=all&order=-announced_date_first&size=25) (4 hits; newest 2608.15873) and ["coset partition"](https://arxiv.org/search/?query=%22coset+partition%22&searchtype=all&order=-announced_date_first&size=25) (13 hits; newest 2609.29951 in cs.LG, then 2609.03184 on Cayley-graph colourings) | — | result snippets | — | No group claim for any k≥6. |
| B2 | [math.GR/new](https://arxiv.org/list/math.GR/new) | Friday 16 Oct 2026 listing, 28 entries | titles and abstracts, plus a term grep | — | No relevant entry. |
| B3 | DataCite query (including "disjoint cosets") | Newest relevant registration: 10.48550/arxiv.2608.15873 (2026-08-18) | metadata | — | No new record. |

**Verdict B: NONE_FOUND_IN_BOUNDED_REFRESH for k=6 and k=7.**
- **k=6 retained:** PARTIAL_OVERLAP_FOUND (M–S Cor. 3.9 covers some patterns); no prior general-group k=6 claim located; NOVELTY-UNCLEAR.
- **k=7 retained:** OPEN, with partial reductions only; no general-group claim or counterexample for k≥7 located.
- **k=5 stays PRIOR-CLAIM.** Sun reports Gong's confirmation, dated 2009 in one primary source and 2010 in the other. Gong's proof or thesis is still neither located nor read. This refresh neither verifies nor refutes it.

Holes retained: the Sun homepage and Progress.pdf (not re-read this time), Sun's 2021 book, Gong's thesis, CNKI and Zhihu, Scholar, and the Monday mailing.

## C. PH three-pole sharp order (Commault–Mocanu 2003 Conjecture 1, scope a>c>0, b>0)

**Matched target.** For a>c>0, b>0, the transform c(a²+b²)/[(s+c)((s+a)²+b²)] has minimal PH order exactly n* = min{n≥3 : b ≤ (a−c)·cot(π/n)}. This is not the general minimal-PH question, and it covers neither zero-rate limits nor other numerators.

| Batch | Source | Version / date seen | Read scope | Quote (≤40 words) | Matched comparison |
|---|---|---|---|---|---|
| B2 | Mocanu 1999 thesis, [HAL tel-05023365](https://hal.science/tel-05023365) | "tel-05023365 , version 1 (07-04-2025)"; "Last modification on : Monday, October 27, 2025"; one file, these_mocanu-a4.pdf (1.03 Mo) | record page and abstract | "la preuve du fait que toute distribution de type phase accepte une telle représentation" | Still v1. The PDF was not re-downloaded (downloads are out of scope). The parent's 01:48 read is retained unchanged: Theorem 50 gives the n*+1 baseline, and Lemma 51/Eq. 4.13 covers every boundary β = cot(π/n). |
| B2 | Verbeken–Ginis, [arXiv:2606.10143](https://arxiv.org/abs/2606.10143) | v2 (2026-09-14 09:21:39 UTC) is the latest; v1 2026-06-08 | abstract and history | "For every n≥3, we determine the union of the spectra of row-stochastic matrices supported on a directed n-cycle with self-loops and strictly positive cycle edges." | Same version the parent read. The cycle-angle spectral mechanism stays attributed to them. The abstract states no input/exit vectors and no transfer-function realization. No change. |
| B3, B4 | arXiv search ["phase-type" "minimal order"](https://arxiv.org/search/?query=%22phase-type%22+%22minimal+order%22&searchtype=all&order=-announced_date_first&size=25) (0 hits) and ["positive realization" "phase-type"](https://arxiv.org/search/?query=%22positive+realization%22+%22phase-type%22&searchtype=all&order=-announced_date_first&size=25) (0 hits) | — | — | — | Search misses only. |
| B1 | math.PR/new (Friday 16 Oct) | — | scanned | — | Nothing relevant. The math.OC, eess.SY and math.RA listings were not scanned. |

**Verdict C: NONE_FOUND_IN_BOUNDED_REFRESH.** Status retained: NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR.

Prior work, all retained:
- Mocanu 1999 gives n*+1 (Theorem 50) and every boundary case (Lemma 51/Eq. 4.13).
- Verbeken–Ginis 2026 publish the cycle-angle mechanism.
- n*=3 is CM2003 Theorem 14 (Commault–Chemla).
- The lower bound is Dmitriev–Dynkin.

The only possible contribution is the off-boundary n* realization and the assembled all-n theorem.

Holes retained: the POSTA chapter body, the O'Cinneide 1999 body, the Benvenuti–Farina 1999 primary text, Kim 2012/2013/2015, the 2024 Wiley book, and Scholar/CNKI.

## D. Ordered Olson partial scopes (math-2): K01, S1(g) with S1(d)/ZX, ROT-KP, ROT-ZR

**Matched scopes.** These are written partial theorems for D_2p, p≥5 prime, each valid only at the scope of its verdict:
- K01: o_F≤p−1 and F−o_F≥2p−4;
- S1(g): 3o_F≤2p+1 under the stated δ* conditions;
- ROT-KP: o_F≤p and F−o_F≥2p−4;
- ROT-ZR: the stated terminal ranges.

None of them gives full INV*(p), general dihedral ordered Olson, or **any all-groups claim**. The verdicts make no priority or novelty claim.

| Batch | Source | Version / date seen | Read scope | Quote (≤40 words) | Matched comparison |
|---|---|---|---|---|---|
| B2 | [Open Problem Garden, Olson's Conjecture](https://openproblemgarden.org/op/olsons_conjecture) | posted 2007-03-10 by mdevos; no comments shown, only an "add new comment" link | full page | "Apart from Olson's result, there appears to be very little known about this problem." | Unchanged. |
| B2, B4 | Godara–Joshi–Mazumdar, [arXiv:2407.01148](https://arxiv.org/abs/2407.01148) | Abstract read via the arXiv API (v1 2024-07-01). The [v3 URL](https://arxiv.org/abs/2407.01148v3) returned HTTP 404, so the baseline v2 (2025-11-23) is still the latest; the v2 page was not re-read. | abstract | "there exist 1 ≤ i_1 < i_2 < ⋯ < i_m ≤ k such that g_{i_1}g_{i_2}⋯g_{i_m}=1" | This is an ordered Davenport constant over subsequences of any length, not the length-\|G\| ordered Olson problem for D_2p. No change. |
| B3, B4 | arXiv search ["Olson's conjecture"](https://arxiv.org/search/?query=%22Olson%27s+conjecture%22&searchtype=all&order=-announced_date_first&size=25) (1 hit, astro-ph/0211518, unrelated) and "Olson dihedral" (0 hits) | — | — | — | Search misses only. |
| B2 | [math.CO/new](https://arxiv.org/list/math.CO/new) | Friday 16 Oct 2026 listing, 87 entries | titles and abstracts, plus a term grep | [2610.21577](https://arxiv.org/abs/2610.21577): "zero-sum subsequence of length k exp(G)" (abelian, rank 3). Replacement [2609.29878v4](https://arxiv.org/abs/2609.29878): "sup_{r(G)=r}(D(G)−D*(G))=∞ for every fixed r≥5" | 2610.21577 is abelian and unordered; it was already listed in §6 of the baseline scout. 2609.29878 concerns abelian groups of rank ≥5. The Olson import D(C_p⊕C_{2p})=3p−1 is a rank-2 statement, and this abstract does not contradict it [INFERENCE from the stated rank range]. No conflict. |
| B2 | math.GR/new | Friday 16 Oct listing | scanned | — | No relevant entry. |
| B3 | [DataCite query](https://api.datacite.org/dois?query=%22Olson%27s%20conjecture%22%20OR%20mcDSQS%20OR%20RDSQS%20OR%20gcDCQS%20OR%20%22disjoint%20cosets%22&sort=-created&page[size]=10&fields[dois]=titles,created,doi) | 8 records in total; none relevant to ordered Olson | metadata | — | No change. |

**Verdict D: NONE_FOUND_IN_BOUNDED_REFRESH.** The baseline finding is retained: no located ordered-Olson theorem covers D_2p or any class containing it. The partial scopes are unchanged, and no all-groups claim is made.

Holes retained: Gao–Lu 2008, Yuster 1988, Caro 1996, the Olson 1976 body, Grynkiewicz's book, the Zenodo API, Scholar/CNKI and the Monday mailing. The OPG-155 GitHub repository was not rechecked.

## E. Design results (math-1): LKTS(57/87), RDSQS(52), mcDSQS(38), gcDCQS(20⁴:0), gcDCQS(32⁴:0), Tan–Zhou §4(3)

**Matched objects (unchanged).** The exact finite objects in the gate rows. The imported families are written consequences, not certificates.

**Shared Tan–Zhou sources.** Each was fetched once and serves all five Tan–Zhou-linked results.

| Batch | Source | Version / date seen | Read scope | Quote (≤40 words) | Bearing |
|---|---|---|---|---|---|
| B2 | Tan–Zhou, [arXiv:2503.11934](https://arxiv.org/abs/2503.11934) | **v1 only**, Sat 15 Mar 2025 00:56:13 UTC | abstract and history | "an RDSQS(2^{2m+1}+2) and an mcDSQS(2·9^m+2) are proved to exist" | No new version, so the §4(1)–(3) wording is still the v1 text read earlier. The journal §4 is paywalled and was not re-attempted. |
| B2 | [Crossref 10.1007/s10623-025-01677-x](https://api.crossref.org/works/10.1007/s10623-025-01677-x) | is-referenced-by-count **1**; reference-count 24; indexed 2026-06-03T05:24:32Z | metadata | — | Citer count unchanged. |
| B2 | [OpenAlex cites:W4411559024](https://api.openalex.org/works?filter=cites:W4411559024&select=id,display_name,publication_date,doi) | count **1**: W7163175683, the Tilings paper (DCC, 2026-06-01, 10.1007/s10623-026-01853-7) | metadata | — | No new citer. |
| B2 | Tan–Zhou Tilings, [arXiv:2512.22754](https://arxiv.org/abs/2512.22754) | v1 only, 2025-12-28 | abstract and history | — | Unchanged. |
| B3 | arXiv author search: [Zhou, Junling](https://arxiv.org/search/?query=Zhou%2C+Junling&searchtype=author&order=-announced_date_first&size=25) (18 hits; newest 2604.23558, 2026-04-26) and [Tan, Yuli](https://arxiv.org/search/?query=Tan%2C+Yuli&searchtype=author&order=-announced_date_first&size=25) (4 hits; newest 2602.16319) | — | result lists | — | No new SQS, mcDSQS, gcDCQS, RDSQS or LKTS item. |

**Result-specific sources.**

| Batch | Source | Version / date seen | Read scope | Quote (≤40 words) | Bearing |
|---|---|---|---|---|---|
| B2 | Wang, [arXiv:2607.21521](https://arxiv.org/abs/2607.21521) | **v1 only**, Thu 23 Jul 2026 17:04:04 UTC | abstract and history | "The construction yields, in particular, LKTSs of orders 93, 177, 219, 261, and 303." | Still the latest status source located for LKTS57/87. Its §4 statement that 57 and 87 are the remaining exceptions below 200 comes from the baseline full-text read. |
| B2 | [OpenAlex cites:W7170252291](https://api.openalex.org/works?filter=cites:W7170252291&select=id,display_name,publication_date,doi) (Wang) | count **0** | metadata | — | No citer. |
| B3 | [arXiv search Kirkman](https://arxiv.org/search/?query=Kirkman&searchtype=all&order=-announced_date_first&size=25) | 123 hits; newest relevant is 2607.21521 | snippets | — | No LKTS item after Wang. |
| B3 | Shi–Xia–Krotov, [arXiv:2212.00048](https://arxiv.org/abs/2212.00048) | v2 (2023-07-31) is the latest; JCTA 200 (2023) 105790 | abstract and history | — | The baseline Conjectures 1–2 are unchanged. |
| B3 | Kiermaier–Krčadinac–Wassermann, [arXiv:2509.23483](https://arxiv.org/abs/2509.23483) | v1 only (2025-09-27). The abs page **now shows a journal reference: Designs, Codes and Cryptography 94 (2026), article 157, DOI 10.1007/s10623-026-01888-w**. | abstract and history | "we establish the existence of rotational Steiner quadruple systems on 46 and 92 points" | A metadata change, not recorded in the baseline audit. The abstract makes no colouring or resolvability claim. **New access hole:** the journal body was not read, so an added colouring statement cannot be excluded. The mcDSQS38 prior-object caveat (record 143) is retained. |
| B5 | [DataCite 10.5281/zenodo.17153237](https://api.datacite.org/dois/10.5281/zenodo.17153237) (concept DOI of the KKW dataset) | versionCount **1** (10.5281/zenodo.17153238 only); updated 2025-09-30 | metadata | — | **Closes, at metadata level, the baseline hole** that later versions of the KKW dataset were unchecked: no later version is registered. |
| B3 | [arXiv search "Steiner quadruple"](https://arxiv.org/search/?query=%22Steiner+quadruple%22&searchtype=all&order=-announced_date_first&size=25) | 27 hits; newest 2609.31783 (Betti numbers), then 2606.03299 (signed Johnson graphs), then 2509.23483 | snippets | — | No item on colourings or derived designs. |
| B4 | [arXiv search "minimum colorable"](https://arxiv.org/search/?query=%22minimum+colorable%22&searchtype=all&order=-announced_date_first&size=25) | 38 hits; only 2503.11934 is relevant | snippets | — | No new mcDSQS item. |
| B2, B5, B6 | math.CO/new, and [math.CO/recent](https://arxiv.org/list/math.CO/recent?skip=0&show=25) (newest mailing Fri 16 Oct) | — | titles and abstracts, plus a grep for Kirkman, Steiner, quadruple, triple system, large set, candelabra and resolvable | — | No design item. |
| B3 | DataCite topic query (above) | Relevant: 2503.11934 (registered 2025-03-18) and 2210.06214 (2022-10-13) only | metadata | — | No new record. The search listing shows Liu–Lei 2210.06214 v2 (2023-02-11) as its latest version. |

**Per-result verdicts.** Every result below is NONE_FOUND_IN_BOUNDED_REFRESH, and each keeps its gate-row qualification:
- **LKTS(57), LKTS(87):** no earlier construction located; NOVELTY-UNCLEAR. The below-200 spectrum keeps its stated evidence levels: order 147 has the weakest access, and orders 93/177 rest on Wang's unrefereed v1.
- **RDSQS(52):** NOVELTY-UNCLEAR. The journal §4 and the Yuan–Kang, Xu–Ji and Chang–Zhou bodies remain holes.
- **mcDSQS(38):** the prior object is retained, and the colourings remain the claimed contribution. New hole: the body of the KKW journal version.
- **gcDCQS(20⁴:0):** NOVELTY-UNCLEAR.
- **gcDCQS(32⁴:0):** NONE-FOUND-IN-SCOPE (bounded). Chang–Zheng–Zhou 2019, Chang–Zhou 2013 and the journal §4 remain unread.
- **Tan–Zhou §4(3):** NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR. CZZ pp. 1416–1431 remain unread.

## Changes relative to the baseline

1. No status change, contradiction, new equivalent or new prior claim in any named group.
2. KKW (arXiv:2509.23483) now carries a DCC 94 (2026) art. 157 journal reference. This adds an unread journal-body hole for the mcDSQS38 prior-object comparison and changes no verdict. The KKW dataset concept DOI has exactly one version; this closes one metadata hole.
3. The ME(≤3) post-17:00 arXiv re-screen ran, but it could see listings only through the Friday 16 Oct mailing.

**Not claimed:** novelty, priority, "first", correctness acceptance or any strengthening of a result. No earlier access hole is removed except the KKW dataset-version metadata hole above.
