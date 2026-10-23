# Post-17:00 PDT physics primary-source status/priority refresh v1

Recorded 2026-10-18T17:22:47-07:00 (/bin/date, host clock) by read-only task agent `Post17PriorityPhysics`. The first post-gate /bin/date read 17:00:11. Live retrievals counted here ran from 17:00:22 to 17:22:41 PDT; exact /bin/date brackets are in the log below. Pre-17:00 work (16:55:09–16:58) read local run files only and sent Main a source list. None of it is evidence here.

Scope: the physics items of `review/post17-priority-refresh-plan-v1.json`. This is an update check against the existing baselines: `screening/phys-2-moqls7-M7-post-candidate-priority-v2.md`, `review/moqls7-k1-priority-scout-v1.md`, `screening/phys-2-rqls10-priority-audit-v1.md`, `review/physics-priority-addendum-v1.md` and the colour, χ8, dual-unitary, qutrit-sharp, AME and depolarizing audits, plus rows 36–42, 87–91 and 107–110 of `review/final-report-draft-v3.md`. It is not a repeat audit.

Constraints observed:
- Public pages only. No computation, contact or publication.
- No correctness acceptance or strengthening.
- No files saved by this agent. The harness URL-grep tool keeps transient fetch text in its own session cache (`~/.omp/agent/sessions/…/url-search/`), outside RUN.

## Bottom line

- **No escalation.** No newly found full-equivalence result, withdrawn source or changed source version in any assigned group. Each group below is a bounded NO-CHANGE with access gaps. A miss is not novelty, and no "first" is claimed.
- **All baseline versions are unchanged.** Every baseline primary version re-checked is still the latest: [Ball–Simoens 2607.12933v2](https://arxiv.org/abs/2607.12933v2), [Huang–Li 2606.27758v1](https://arxiv.org/abs/2606.27758v1), [Zhang–Cao 2608.29201v2](https://arxiv.org/abs/2608.29201v2), and the colour, dual-unitary, AME and depolarizing sources listed below.
- **The open statements the gates cite are still present.** The open-problem statements cited by the K1 corollaries, M(7)=2 and RQLS(10) rows are still in the latest texts. The quotes are below.
- **Main access gap: the new arXiv mailing was not public.** The Sunday 20:00 EDT mailing (the listing dated Monday 19 Oct 2026) had not appeared at any check from 17:02:47 to 17:22:41 PDT. `arxiv.org/list/{math.CO,quant-ph}/new` still read "Showing new listings for Friday, 16 October 2026".
  - [arXiv status](https://status.arxiv.org/) showed all services Up.
  - The [availability page](https://info.arxiv.org/help/availability.html) lists no 2026 holiday on 18 or 19 Oct.
  - [arxiv.org/localtime](https://arxiv.org/localtime) read "Sun, 18 Oct 2026 20:15 EDT".
  - **Consequence:** the scheduled same-day announcement refresh, including the M(7)=2 row's "PENDING", is **not completed** by this report.

## Retrieval log (PDT; /bin/date brackets; individual fetches inside a bracket are not separately timed)

| Window | Retrievals | Observation |
|---|---|---|
| 17:00:22–17:01:14 | arXiv abs pages for 2607.12933 and 2606.27758; 2608.29201 through the reader's arXiv-API path; export API `id_list` for 10 IDs | Latest: 2607.12933v2, 2606.27758v1, 2608.29201v2, 2603.02334v1, 2507.20154v1, 2609.24653v1, 2609.29070v1, 2609.09695v1, 2607.19969v2, 2610.17170v1 |
| 17:01:14–17:01:58 | Targeted full-text passages: Ball–Simoens v2 HTML; Huang–Li v1 PDF; Zhang–Cao v2 HTML and PDF | See A and B |
| 17:01:58–17:02:47 | Export-API search "quantum Latin" (HTTP 429). [DataCite "quantum Latin"](https://api.datacite.org/dois?query=%22quantum%20Latin%22&sort=-created) sorted by newest | 36 records, unchanged. Newest is 10.48550/arxiv.2610.17170, created 2026-10-14T07:26:10Z |
| 17:02:47–17:03:23 | Keyword scan of `/list/{math.CO,quant-ph,math.PR}/new`; RSS for math.CO | Friday 16 Oct listing (87, 154 and 68 entries); no target item. RSS empty; lastBuildDate Sun 18 Oct 04:00:07 UTC |
| 17:03:23–17:04:00 | arXiv abs version histories for 15 IDs (groups C–E) | All unchanged; versions are listed below |
| 17:04:00–17:04:34 | DataCite: Ferudun DOI and concept DOI; random-regular colouring; Ferudun newest and topic queries; AME, dual-unitary and entangling-power query | No new matched record |
| 17:04:34–17:04:48 | DataCite: AfAME record; depolarizing query; math.CO/new header | No matched claim; listing still Friday |
| 17:04:48–17:05:32 | Pandya v1 PDF; Ahmed v2 (PDF gave no extractable match, then abs, then HTML); review 2508.04777v3 PDF | Statements unchanged |
| 17:05:32–17:06:30 | arXiv /search: "quantum Latin" (28 results; newest 2610.17170, submitted 12 Oct 2026). Dual-unitary or entangling power (268 results); abstracts of the two newest. Three further searches returned HTTP 429 | No new matched item |
| 17:06:30–17:06:45 | OpenAlex full text, three queries; quant-ph/new header | No new matched item; listing still Friday |
| 17:06:45–17:07:23 | INSPIRE `refersto` query (not parsed; unusable). [INSPIRE record 3180352](https://inspirehep.net/api/arxiv/2607.12933). Semantic Scholar URL rejected by the tool | Ball–Simoens citation_count = 1, unchanged |
| 17:07:23–17:07:52 | Simoens and Ball home pages; math.CO/new header | Home pages not usable; listing still Friday |
| 17:07:52–17:08:57 | Huang–Li Thm 4.1; Zhang–Cao 2609.24653 abs; DataCite Ferudun page 2 and wildcard query; DataCite Krohn-Grimberghe; GitHub commit lists for the Pandya and Bruzda repos | Unchanged |
| 17:08:57–17:10:30 | quant-ph/new header; DataCite wildcard random-regular query; Crossref ×3 (Ball–Simoens query HTTP 429) | No new item |
| 17:10:30–17:11:01 | abs pages for 1406.3681, 2109.13347 and 1308.4287; math.CO/new header | Unchanged; listing still Friday |
| 17:11:01–17:15:27 | Keyword scan of the full quant-ph Friday listing (154 entries, including cross-lists and replacements) | Two incidental, off-target hits only: DFE under depolarizing noise, and "coherent information" in a Bell-nonlocality paper |
| 17:15:27–17:15:35 | quant-ph/new and math.CO/new headers | Friday |
| 17:15:35–17:21:00 | arXiv availability page, status page and localtime | See Bottom line |
| 17:21:00–17:22:41 | math.CO/new and quant-ph/new (`show=1500` gave HTTP 400; `show=25` pages fetched) | Friday 16 Oct |

Peer observations, not this agent's reads:
- `Post17PriorityMath`: math.CO/recent showed newest mailing "Fri, 16 Oct 2026" at 17:07:38–17:08:18, and arxiv.org/search worked for them at 17:03:50–17:06:08.
- `Post17PriorityInfo`: arxiv.org/search returned 200 at 17:04:17–17:06:41.

## A. M(7)=2, every four MOQLS(7), and K1 corollaries (n=8 carried)

**Matched run claims (final-report rows 38, 39 and 42; K1 verdict):**
- Every three MOQLS(7) are classical. With the prior non-classical pair this gives M(7)=2; the earlier step was that every four are classical.
- K1: no MOQLS(7) triple has exactly one non-classical square.
- Hence every 2-RQLS(7) and every PQLS(7) has cardinality 7, so no MCPQLS(7) and no maximal-cardinality 2-RQLS(7) exist.

| Source (latest version, date) | Read scope (post-17) | Decisive text (≤40 words) | Comparison |
|---|---|---|---|
| [Ball–Simoens 2607.12933v2](https://arxiv.org/html/2607.12933v2). v1 Tue 14 Jul 2026 16:05:20 UTC; v2 Mon 27 Jul 2026 07:40:44 UTC; comment "Correction of Theorem 6"; no v3 | Abs page and history; HTML v2 targeted passages: M(n) definition, Corollary 7, Table 2, Problems 16–17 | Table 2 row: "M(n) \| 0 \| 0 \| 1 \| 1 \| 1 \| 2-4 \| 2-5 \| 3-6 \| 2-7 …" (n=2…10). Problem 16 still ends "…MOQLS(n), n≠4, necessarily classical?" | Still states M(7) as 2–4, M(8) as 2–5 and M(10) as 2–7, and Problem 16 remains posed. No triple or four-set exclusion and no K1. **No change.** |
| [Huang–Li 2606.27758v1](https://arxiv.org/pdf/2606.27758v1), submitted Fri 26 Jun 2026 06:36:51 UTC (only version) | Abs page; PDF targeted passages: Thm 2.15, Thm 4.1 and Remark 4.2, §5 (Thm 5.1 head, the MCPQLS sentence, Thm 5.2 and its remark) | "…the existence of MCPQLS(7), MCPQLS(11), and MCPQLS(n) with gcd(n,6) ≠ 1 remains to be determined." Also: "Theorem 5.2 There exists a non-classical 2-MOQLS(7)." | MCPQLS(7) is still listed as open, neither withdrawn nor answered. Thm 5.2 is the prior lower-bound pair. **No change.** |
| [Zhang–Cao 2608.29201v2](https://arxiv.org/html/2608.29201v2); the export API lists v2 as latest (v2 date not re-observed) | API feed; HTML and PDF v2 targeted passages: abstract, Thm 1.3, Lemma 2.2 heading, §4 table, §5 | §5: "the known result at present are gcd(v, 6) = 1 and v ∉ {5, 7, 11} or v = n² … It remains to determine the existence of maximal-cardinality 2-RQLS(v)s for the remaining orders." | Maximal-cardinality 2-RQLS(7) is still open in the source. The Lemma 2.2 reformulation, which is prior art, is still present. **No change.** |
| [Ball–Simoens 2603.02334v1](https://arxiv.org/abs/2603.02334) (2 Mar 2026), [Han et al. 2507.20154v1](https://arxiv.org/abs/2507.20154) (27 Jul 2025), 2609.24653v1, 2609.29070v1, 2609.09695v1, 2607.19969v2, 2610.17170v1, [Egan–Wanless 1406.3681v2](https://arxiv.org/abs/1406.3681) (13 Oct 2014, imported classification) | Version metadata only | — | No new versions. |
| Freshness: [DataCite](https://api.datacite.org/dois?query=%22quantum%20Latin%22&sort=-created) (36, newest 2026-10-14); [arXiv search](https://arxiv.org/search/?query=%22quantum+Latin%22&searchtype=all&order=-announced_date_first) (28, newest 2610.17170); OpenAlex full text since 2026-10-01 (6 hits); Friday 16 Oct listings; INSPIRE citation count 1 | Metadata, titles and abstracts | — | No new quantum-Latin record after 2610.17170. |

**Verdict A: bounded NO-CHANGE; NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR retained.**
- The cited open-problem statements are unchanged in the latest versions.
- The M(7)≥2 pair (Huang–Li Thm 5.2; Ball–Simoens Cor. 7) and the net reformulation (Zhang–Cao Lemma 2.2; Ball–Simoens 2603.02334 Lemma 21) remain prior work.
- **Same-day announcement refresh still PENDING:** the Monday 19 Oct mailing was not public at the read times.

**n=8, carried:**
- Ball–Simoens v2 Table 2 still reads M(8) "2-5"; no new source was found.
- The run's Problem 16 at n=8 remains **OPEN**, with GA 16/18 and GB 1/18 qualified, as in final-report row 107. This was carried, not re-derived.
- K1, K2, K3 and 122/128 K5 roots are partial inputs. No priority screen turns them into a proof.

## B. Maximal-cardinality 1-RQLS(10)

**Matched target:** 100 pairwise nonparallel unit vectors in C¹⁰ forming a QLS(10) with ten transversal ONBs that partition the cells. The run's status is **UNKNOWN**: no result, so there is no priority question.

| Source | Read scope | Decisive text | Comparison |
|---|---|---|---|
| Zhang–Cao 2608.29201v2 Thm 1.3 and §5 | HTML/PDF targeted | "It remains to determine whether a maximal-cardinality 1-RQLS(v) exists for v ∈ {10, 14, 18, 22, …, 94}" (17-order exception list; Thm 1.3 excludes the same set) | Order 10 is still open in the latest version. |
| Huang–Li 2606.27758v1 Thm 4.1 | PDF targeted | Idempotent MCQLS(v) exists "except possibly when v ∈ {6, 8, 10, 12, 14, 18, 20, 24, 26, 30, 32, 38, 62}" | A different object, but 10 is unresolved there too. |
| [Zhang–Cao 2609.24653v1](https://arxiv.org/abs/2609.24653) | Abstract | "…a symmetric idempotent quantum Latin square with maximal cardinality of order 4k+2 for all k≥1." | PARTIAL_OVERLAP carried from the v1 audit: a symmetric square, not a 100-ray resolution. The ray bound was not re-read. |
| Ball–Simoens v2 Table 2; Lv–Zhang–Cao 2609.29070v1 | Table row; version only | M(10) "2-7" | No order-10 resolution. |

**Verdict B: NO-CHANGE.** The target is still open in the latest primary sources, and no external resolution was found in scope.

## C. Maximum Hypothesis; χ(G_{n,8})=4 and χ(G_{n,12})=5; T7; sharp 15/16

**C1 Maximum Hypothesis.** The run claims F(n)<F(n*) on the pinned preprint's Δ, which gives χ(G_{n,5})=3 a.a.s. through the imported Theorem 1.1.
- **Versions unchanged:** [ACG 1812.09691v4](https://arxiv.org/abs/1812.09691) (v4 Tue 19 Oct 2021 12:42:15 UTC; four versions); [KPW 0812.2937v1](https://arxiv.org/abs/0812.2937) (15 Dec 2008, only version); [COEH 1308.4287v1](https://arxiv.org/abs/1308.4287) (only version).
- **Freshness screens:** no record states the Maximum Hypothesis or χ(G_{n,5})=3.
  - DataCite "random regular" with colour\*/color\*/chromatic: 86 hits, none relevant after 2026-09-16.
  - OpenAlex full text "random regular" + "chromatic number" since 2026-09-01: 18 hits, titles only.
  - Ferudun wildcard topic query: newest match 2026-10-17T16:01:32Z, off-topic.
- **Not re-read:** the Díaz preprint and JGT body (pinned 2009 source) and the ESA 2005 body. ESA 2005 stays the unresolved priority risk.
- **Verdict: NO-CHANGE.**

**C2 χ8/χ12.** These are DERIVED-OPEN targets, counted only under the new-theorem clause.
- **Versions unchanged:** KPW v1 (window source), ACG v4, and [Nir–Pérez-Giménez 2109.13347v1](https://arxiv.org/abs/2109.13347) (lifts only).
- **Ferudun method-precedent record unchanged:** [DataCite 10.5281/zenodo.23430098](https://api.datacite.org/dois/10.5281/zenodo.23430098), version 1.0. Created 2026-10-17T04:20:57Z, registered and updated 04:20:58Z. Its concept DOI 10.5281/zenodo.23430097 has versionCount 1.
- **Abstract read:** "This is an unrefereed, AI-assisted preprint with reproducible exact checks, not independent or formal verification, and makes no absolute priority claim."
- No later Ferudun or EulerSolve colouring record was found: 689 Ferudun records, newest 2026-10-18T23:48:54Z, off-topic.
- **Verdict: NO-CHANGE.**
  - The method precedent is retained. Method novelty stays narrowed to the hypercontractive row inequality.
  - Theorem priority stays unresolved.

**C3 T7.** The run claims O₉ is a connected component of the two-qutrit dual and T-dual gates, with radius 1.
- **Survey still poses T7:** [review 2508.04777v3](https://arxiv.org/abs/2508.04777) (v3 Thu 25 Jun 2026 11:57:52 UTC; J. ref. Rep. Prog. Phys. 89 057601 (2026)). Its PDF text still asks: "(T7). Are there dual/T-dual gates in U(9) arbitrarily close to the 2-unitary permutation matrix P₉ related to the state AME(4,3)?"
- **Versions unchanged:**
  - [Geng 2211.15776v3](https://arxiv.org/abs/2211.15776) (6 Dec 2022).
  - [Nicoară math/0404301v1](https://arxiv.org/abs/math/0404301) (16 Apr 2004, only version).
  - [Rather–Ramadas–Kodiyalam–Lakshminarayan 2212.06737v2](https://arxiv.org/abs/2212.06737) (14 Sep 2023; PRA 108, 032412).
  - [Pahari 2607.00210v2](https://arxiv.org/abs/2607.00210) (4 Jul 2026).
- **No new dual-unitary result on the target.**
  - The newest arXiv dual-unitary/entangling-power hits, 2610.06791 (scattering entanglement power) and 2610.06754 (projected ensembles in dual-unitary circuits), are off-target at abstract level.
  - DataCite has no record after 2026-10-14.
- **Verdict: NO-CHANGE.** Retained: the Geng 2022 core-computation overlap, and the near-implication by Nicoară's Theorem 3.4, whose convention mapping is still unchecked.

**C4 Sharp 15/16.**
- The review v3 text is unchanged: "The dual unitary U_s(2π/3) is an orthogonal matrix with entangling power 15/16 = 0.9375 which is likely to be the highest possible value for dual unitaries that are not 2-unitary."
- The Rather thesis was not re-fetched.
- **Verdict: NO-CHANGE.**

## D. AME(4,6) support

**Matched run claim:** every AME(4,6) state has at least 48 nonzero coefficients in every product ONB.
- Pandya's upper bound of 60 is imported, not re-reviewed.
- The frozen gate needs an exact state with support ≤59 or a complete proof of support ≥60.
- The case (24,0) at s=48 is UNKNOWN.

**Sources:**
- **[Pandya 2610.16673v1](https://arxiv.org/pdf/2610.16673v1)** (Mon 12 Oct 2026 12:20:27 UTC, only version). PDF targeted text:
  - "an explicit real AME(4,6) state with 60 non-zero coefficients, the sparsest AME(4,6) state we know of"
  - "Whether the gap between 38 and 60 can be closed is open."
  - Repository [real-ame46](https://github.com/palashpandya/real-ame46) HEAD is still `215fd885` (2026-10-13T11:50:15Z).
- **Bruzda and Hontarenko–Życzkowski:** [Bruzda 2610.16882v1](https://arxiv.org/abs/2610.16882) (repository [AME_4_6](https://github.com/matrix-toolbox/AME_4_6) HEAD still `eaa668f7`, 2026-10-14T19:51:14Z) and [Hontarenko–Życzkowski 2610.17170v1](https://arxiv.org/abs/2610.17170) are unchanged.
- **Newer DataCite records:**
  - DataCite AME/dual-unitary/entangling-power: no AME(4,6) record after 2026-10-14.
  - [AfAME, zenodo.23068891](https://api.datacite.org/dois/10.5281/zenodo.23068891) (2026-09-30, software). Its abstract describes quadratic-phase finite-field search and makes no AME(4,6) support claim (abstract only).
  - OpenAlex since 2026-10-01: nothing new.

**Verdict D: NO-CHANGE.**
- No external AME(4,6) state with ≤59 nonzero coefficients and no external lower bound above 38 were located in scope. This is not a novelty statement.
- The range 48 ≤ s_min ≤ 60 stands, with the upper bound imported.
- The gate is unmet in both directions.

## E. Depolarizing capacity (scope only; not a gate)

**Matched run claim:** Q(N_p)>0 for 0≤p≤1/5, from a certified M=2000 witness.
- **[Ahmed et al. 2609.39747v2](https://arxiv.org/html/2609.39747v2)** (v2 Thu 1 Oct 2026 16:48:34 UTC, latest). HTML text still reads: "We therefore conclude from our work that p_th ≥ 0.2029161."
- **[Krohn-Grimberghe 2608.15870v2](https://arxiv.org/abs/2608.15870)** (Tue 18 Aug 2026; comment says "certified bound unchanged") is latest. Their DataCite records show nothing newer on depolarizing; the newest is 2026-09-25, off-topic.
- **[Khanian–Leung–Smith 2610.02176v1](https://arxiv.org/abs/2610.02176)** is unchanged.
- **DataCite and OpenAlex since early October:** no new threshold claim; titles only.

**Verdict E: NO-CHANGE.**
- The run's 1/5 stays above Krohn-Grimberghe's certified 0.194868 and below Ahmed's prior-claimed 0.2029161, whose numerical premise the prior audit found uncertified.
- It is not counted as a gate, and no priority is claimed.

## Prior-claimed results versus unresolved priority (physics slice)

- **Prior work, not the run's:**
  - The M(7)≥2 pairs and the net reformulation.
  - Pandya's 38 and 60 bounds.
  - Ahmed's claimed 0.2029161 and Krohn-Grimberghe's certified 0.194868.
  - The Ferudun method precedent, Geng's core computation and Nicoară's general theorem.
- **Priority unresolved (NOVELTY-UNCLEAR):** M(7)=2 and the four-set step; the K1 corollaries; the Maximum Hypothesis proof; the χ8/χ12 theorems; the T7 exact check, radius 1 and T-dual case; 15/16; and AME s≥48.
- No physics item here is PRIOR-CLAIM.

## Access gaps

1. **Monday 19 Oct arXiv mailing not public** through 17:22:41 PDT, so the decisive new batch is uncovered.
2. **Rate limits and refusals:**
   - The arXiv export-API search returned HTTP 429 at 17:01:58–17:02:47.
   - arXiv /search returned HTTP 429 for the random-regular, AME(4,6)/officers and depolarizing queries at 17:05:32–17:06:30. DataCite and OpenAlex metadata, which lag (OpenAlex's newest arXiv item seen is dated 2026-10-14), were the substitute.
   - Crossref returned 429 for the Ball–Simoens journal-version query. Crossref's top three bibliographic matches for Huang–Li and Zhang–Cao were other papers.
3. **Citation and catalogue gaps:**
   - Semantic Scholar was rejected by the tool, and the INSPIRE `refersto` query was unusable.
   - Zenodo pages and files were not opened (DataCite only), and GitHub code search was not used.
   - Author home pages were not usefully read.
4. **Extraction gap:** Ahmed v2 PDF extraction returned no matches, so HTML v2 was used.
5. **Version-date gap:** the Zhang–Cao v2 submission date was not re-observed.
6. **Bodies not re-read here:** the journal versions (PRL 137 050202 and its Correction, Rep. Prog. Phys., PRA, JGT), ESA 2005, the Díaz preprint, the Rather and Musto theses, the Krohn-Grimberghe artifacts, Han et al., Lv–Zhang–Cao, Geng and Nicoară.
7. **Indexes not searched:** Google Scholar, MathSciNet, zbMATH, CNKI and arXiv full text. Earlier screens' holes stay open unless a direct read above closed them; none did.
