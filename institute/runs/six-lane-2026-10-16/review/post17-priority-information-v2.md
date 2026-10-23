# Post-17:00 PDT information-science status/priority refresh (v2)

**v2 supersedes [v1](post17-priority-information-v1.md)** (26,764 bytes, sha256 `8f371dc71a0a2d02e3d51b505c6b3da907e0f011722b3e37859930335621bbec`, retained unmodified). It makes the three record corrections listed in §11. No finding, verdict, source or retrieval changed, and no new retrieval was made for v2.

Author: worker `Post17PriorityInfo` (read-only public-source refresh). Plan: [post17-priority-refresh-plan-v1.json](post17-priority-refresh-plan-v1.json), `information_science` items. This is an update check against the existing baselines, not a repeat literature audit. No novelty or priority is inferred from a miss. No correctness acceptance is added or strengthened. No science was run: no solver, checker, interpreter, build, test, clone or download. Nothing was contacted or published.

## 0. Time base and method

- Host clock is `/bin/date` (PDT). Pre-17 work was local file reads only. Immediately after the 16:56:54 stamp, the prepared source list was sent to Main. At 17:00:09 `/bin/date` confirmed the release time, and Main's release message ("proceed once own /bin/date confirms >=17:00") arrived during window W1. No web read happened before 17:00:09.
- Live retrievals ran from 17:00:09 to 17:09:31 PDT on 2026-10-18. Per-request times were not logged, so each source is dated by the `/bin/date` stamps that bracket its window:
  - W1 17:00:09–17:03:12
  - W2 17:03:12–17:04:17
  - W3 17:04:17–17:05:29
  - W4 17:05:29–17:06:41
  - W5 17:06:41–17:07:29
  - W6 17:07:29–17:09:31
- Tooling: the built-in `read`/`grep` HTTP GETs of public pages and APIs (GitHub, DataCite, Crossref, OpenAlex, ORCID, arXiv abs/search HTML). No `web_search` prose was used as evidence. The arXiv export API returned HTTP 429 in W1, so the arXiv HTML abs and search pages were used instead.
- Baselines (local): [cfr27-priority-scout-v1](cfr27-priority-scout-v1.md), [info-2-cfr21-priority-screen-v1](../screening/info-2-cfr21-priority-screen-v1.md), [cdf-k5-priority-audit](cdf-k5-priority-audit.md), [point-cyclic88](point-cyclic88-priority-audit.md), [point-cyclic100](point-cyclic100-priority-audit.md), [table200](point-cyclic-table200-priority-audit.md), [btd12-15](btd12-15-priority-audit.md), [btd14-28](btd14-28-priority-screen-v1.md), [info-prior-gap-audit-v1](info-prior-gap-audit-v1.md), [info-1-pa19-post-result-priority-v1](../screening/info-1-pa19-post-result-priority-v1.md), [cpcw addendum](cpcw-priority-addendum-v1.md), [L(12,3) addendum](cover12-3-priority-addendum-v1.md), and [final-report-draft-v3](final-report-draft-v3.md) rows 43–61, 97, 99, 111 and 113.

## 1. Bottom line per target group

| Group | Baseline status | Post-17 finding | Change | Bounded verdict |
|---|---|---|---|---|
| CFR(5,27) (cyclic Z₂₇) | NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR | No newer equivalent object (6-row cyclic Z₂₇ DM, 4 MOO(Z₂₇), CFR(5,27)) found | None | NONE-FOUND-IN-SCOPE (unchanged); priority unresolved |
| CFR(6,21) (cyclic Z₂₁) | OPEN; lane closed with no candidate | No construction, nonexistence or N(21)≥6 claim found | None | OPEN-IN-SCOPE (unchanged) |
| Six cyclic (v,5,1) DFs | No earlier construction located; priority unresolved | No new citer or construction. MainCDF data page now HTTP 404 (new access gap) | None (access gap added) | Priority unresolved (unchanged) |
| Point-cyclic 2-(88,4,1) (+8p, written only) | NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR | TZ 2026 still has 0 citations and no update relation. No newer equivalent | None | Unchanged |
| Point-cyclic 100 / table to 200 | DERIVED-OPEN; no prior found | No new source. One non-equivalent 4-RGDD preprint seen | None | DERIVED-OPEN (unchanged) |
| Four BTDs | NOVELTY-UNCLEAR; (14,18) partial prior from 1996; (14,28) priority not established | CPro1, Rosin and Handbook-update sources unchanged; no new BTD item | None | Unchanged |
| PA(19,8,6) | UNDECIDED | No public existence/nonexistence or A₆(8,7) claim. Colbourn–Ling hole retried, still blocked | None | UNDECIDED (unchanged) |
| CPCW 8 codes; L(12,3)=36 | PRIOR-CLAIM (correct; confirmations) | Vos and Raval records still findable, unmodified | None | PRIOR-CLAIM retained |
| BRD(26,…), SW(25,16), CFR(4,33) | Stale (witness verified, not gates) | ACCP 2011 has no update relation; Long record findable; Sage `DM_33_6_1` present | None | Stale retained |

No contradictory primary evidence was found, and no new equivalent result was found, so no urgent message to the parent was needed. Every group keeps its prior scope and all of its old access holes, except where this report says a hole was retried.

## 2. Shared sources (one CPro1, Handbook, Sage and Rosin check serves CFR, BTD and PA19)

| Source (URL) | Version/date seen | Read scope | Window | Finding |
|---|---|---|---|---|
| [CPro1 commits API](https://api.github.com/repos/Constructive-Codes/CPro1/commits?per_page=5) | HEAD `827f02b4048fc96a6b79f0970c87ca5a54f31f40`, 2026-06-03T16:22:34Z; parents `801e86a` (2026-02-06) and `a4e7a6e` (2025-12-03) | metadata | W1 | **Unchanged** from every baseline pin |
| [CPro1 CFR problem_def.py (main)](https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/circular-florentine-rectangle/problem_def.py) | at HEAD 827f02b | full file | W1 | "OPEN_INSTANCES = [[6,21],[5,25],[5,27],[4,33]]". Definition text is unchanged ("Steps to the right" is taken circularly) |
| [CPro1 BTD problem_def.py](https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/balanced-ternary-design/problem_def.py) | at HEAD | full file | W1 | `OPEN_INSTANCES` begins "[[14,18,7,1,9,7,4],[12,15,6,2,10,8,6]" and contains "[12,20,4,3,10,6,4]". (14,28;…) is absent, as at baseline (that instance comes from Rosin Table 1) |
| [CPro1 PA problem_def.py](https://raw.githubusercontent.com/Constructive-Codes/CPro1/main/CPro1/design_definitions/packing-array/problem_def.py) | at HEAD | full file | W1 | "OPEN_INSTANCES = [[32,5,6], [24,7,6], [26,10,8], [23,11,8]]" |
| [CPro1 designs/packing-array @827f02b](https://api.github.com/repos/Constructive-Codes/CPro1/contents/designs/packing-array?ref=827f02b4048fc96a6b79f0970c87ca5a54f31f40) | 827f02b | listing | W3 | `result-18-8-6-seed1000.txt` present; no 19-8-6 file |
| [arXiv 2501.17725](https://arxiv.org/abs/2501.17725) (Rosin) | still **v1**, 29 Jan 2025 15:57:43 UTC | abstract + history | W1 | No new version |
| [arXiv 2505.23881](https://arxiv.org/abs/2505.23881) (Rosin) | still **v1**, 29 May 2025 17:45:50 UTC | abstract + history | W1 | No new version |
| [constructive.codes](https://constructive-codes.github.io/index.html) | newest item "March 2, 2026" (constant-weight codes) | full page | W4 | No CFR, BTD or PA update |
| Dinitz Handbook "New results" [Part VI](https://site.uvm.edu/jdinitz/index.php?rest_route=/wp/v2/pages/413) / [Part III](https://site.uvm.edu/jdinitz/index.php?rest_route=/wp/v2/pages/389) | WordPress `modified` 2021-07-26T15:57:15 / 15:55:48 | REST metadata only (bodies not re-read) | W1 / W4 | Unchanged since baseline reads |
| [Sage `database.py` commits](https://api.github.com/repos/sagemath/sage/commits?path=src/sage/combinat/designs/database.py&per_page=2) | newest `cd5739da` (2026-10-13T21:27:15Z), "Move module bibliographies into the shared RST reference database"; previous `1fd3a298` (2025-09-02) | metadata | W1 | **Version change** from the baseline's "unchanged since 1fd3a298" (the prior-gap pin was f9ebdea5, 2026-10-07). The content check below shows the relevant entries unchanged |
| [Sage develop `database.py` (raw)](https://raw.githubusercontent.com/sagemath/sage/develop/src/sage/combinat/designs/database.py) | develop at read time | targeted grep of full file | W1, W5 | "(21 ,1) : (6 ,DM_21_6_1)," and "(33 ,1) : (6 ,DM_33_6_1),". No (27,1) DM key. k=5 DF keys seen: 121, 141, 161, 201, 221; none of 321/501/621/681/801/901 |

## 3. CFR(5,27) and CFR(6,21) — fixed cyclic Zₙ

Scope reminder from the baselines: CFR(r,n) ⇔ (Zₙ, r+1; 1) difference matrix over the **cyclic** group ⇔ r−1 mutually orthogonal normalized orthomorphisms of Zₙ. Field and noncyclic constructions do not count: GF(27) = Z₃³, Z₉×Z₃, and noncyclic order-21 groups. [INFERENCE] The baseline bridge runs CFR(6,21) ⇒ 6 MOLS(21) in one direction only, so a MOLS-only N(21)≥6 claim would not decide CFR(6,21).

| Source | Version/date | Read scope | Window | Applicability / finding |
|---|---|---|---|---|
| [DataCite "circular florentine"](https://api.datacite.org/dois?query=%22circular+florentine%22&sort=-created&page%5Bsize%5D=25) | total **3**; newest created 2026-08-07T03:58:59Z | titles/metadata | W2 | Identical to the baseline count and newest record: "Certify v0.5.0: an explicit 5x25 circular Florentine rectangle establishing F_c(25) >= 5" (n=25 only) |
| DataCite combined sweep, `created ≥ 2026-10-16T00:00Z` (florentine, orthomorphism(s), difference matri(x/ces), difference famil(y/ies), cyclically resolvable, point-cyclic, ternary design(s), packing array(s), Kirkman, CPro1, "Handbook of Combinatorial Designs", optical orthogonal, Latin squares) | total **12** | titles | W2 | None on-topic. Hits: Kirkman as a surname (4); loops of order 7 (Shah, created 2026-10-18T13:53:25Z); a Latin-square critical-set Lean record (Bean, 2026-10-16T05:39:14Z); unrelated datasets |
| DataCite design-term sweep, `created ≥ 2026-10-16` ("mutually orthogonal", MOLS, balanced ternary, cyclic difference, Steiner, resolvable, orthogonal array, weighing matri(x/ces), covering sequence, cyclically permutable, Bhaskar Rao, combinatorial/block design) | total **117**; page 1 (100 newest) read | titles | W2 | No CFR, DM or MOLS(21/27) claim. Design-adjacent items only: a (51,18,4)-covering (2026-10-17T18:48:49Z) and a resolvable 4-GDD preprint (§5). Page 2 (17 older records) **not read** |
| DataCite creator sweep, `created ≥ 2026-10-16` (Kirtchakov, Raval, Sadhu, Gippini, Ferudun, Nowicki; "Long, Griffin"; "Vos, Reynout") | page 1, newest 2026-10-18T23:48:54Z | titles | W2 | No CFR, DM, CDF, BTD, PA or point-cyclic item. Topics: convex geometry, Hadamard ideal, covering-number DRAT certificates, FJSPLib and others |
| arXiv search ["Florentine"](https://arxiv.org/search/?query=Florentine&searchtype=all&order=-announced_date_first&size=25) | 31 results; 25 newest read | titles + snippets | W4 | Newest on-topic is still 2602.06045 (generalized quasi-Florentine rectangles; generic). Nothing on Z₂₁ or Z₂₇ |
| arXiv search ["orthomorphism"](https://arxiv.org/search/?query=orthomorphism&searchtype=all&order=-announced_date_first&size=25) | 32 results | titles + snippets | W3 | Newest is 2607.21521 (LKTS via "cubic orthomorphism"). No MOO(Z₂₁) or MOO(Z₂₇) result |
| arXiv search ["difference matrix" OR "difference matrices"](https://arxiv.org/search/?query=%22difference+matrix%22+OR+%22difference+matrices%22&searchtype=all&order=-announced_date_first&size=25) | 243 results; 25 newest | titles + snippets | W4 | None are combinatorial DMs over Zₙ |
| [OpenAlex title/abstract sweep since 2026-10-01](https://api.openalex.org/works?filter=from_publication_date:2026-10-01,title_and_abstract.search:(florentine%20OR%20orthomorphism%20OR%20orthomorphisms%20OR%20%22difference%20matrix%22%20OR%20%22difference%20matrices%22%20OR%20%22difference%20family%22%20OR%20%22difference%20families%22%20OR%20%22cyclically%20resolvable%22%20OR%20%22point-cyclic%22%20OR%20%22ternary%20design%22%20OR%20%22ternary%20designs%22%20OR%20%22packing%20array%22%20OR%20%22Kirkman%20school%22)&per-page=50&sort=publication_date:desc) | count **19** | titles | W3 | Only design hit: TZ 2026 (§5). No CFR item |
| [05oz/certify commits](https://api.github.com/repos/05oz/certify/commits?per_page=3) (Kirtchakov) | HEAD `3159a74`, 2026-08-19T03:11:57Z | metadata | W3 | Unchanged; no CFR(5,27) or CFR(6,21) |

**CFR(5,27) verdict: NONE-FOUND-IN-SCOPE, unchanged; NOVELTY-UNCLEAR; priority unresolved.** The verification count must stay as recorded in [cfr27-parent-verdict.md](cfr27-parent-verdict.md) §"Verification-count clarification" (2026-10-17 18:32:45 PDT):
- there are **three separately authored definition-level checkers**: the parent checker, Codex's own verifier and the Claude-authored checker;
- the other routes are CPro1's upstream predicate, the byte-identical producer rebuild and the group-action/conversion audit;
- these are **not six independent checkers**, and the result is not Lean-checked.

Access holes were not retried and remain open:
- Handbook VI.62 Table 62.27 (n=27 entry), VI.17 and III.3; the recorded value F_c(27)=4 is itself an inference;
- Song 2000 and the Song 1991 thesis;
- Abel–Ge 2005 and Ge 2005 bodies; Abel–Finizio–Ge–Greig 2006 Table 1;
- Evans 2018 Ch. 8/13 and Evans 2007; Wanless 2004;
- the IEEE papers Zhang–Helleseth and Song–Song; Zhang–Feng–Wang 2022; the JCD 2026 covering-schemes paper;
- the Zenodo API.

**CFR(6,21) verdict: OPEN-IN-SCOPE, unchanged.** No public 7-row cyclic Z₂₁ DM, 5 MOO(Z₂₁), 5 MODCLS(21), N(21)≥6 or nonexistence claim was found in this scope. The frozen gate (a raw 7-row DM or a complete unrestricted nonexistence proof) remains unmet. Restricted-family UNSAT and lemma L3 (parent incidence derivation, internal review only) are not the gate. Carried holes: Nazarok 1991, Handbook VI.62 and III.3.50, Evans 2018 Ch. 13, Wanless 2004, Song 2000, Lampio 2011, and Zenodo full texts.

## 4. Six cyclic (v,5,1) difference families (v = 321, 501, 621, 681, 801, 901; cyclic Z_v)

| Source | Version/date | Read scope | Window | Finding |
|---|---|---|---|---|
| [OpenAlex ACF 2004 (W2072456991)](https://api.openalex.org/works/doi:10.1016/j.dam.2003.12.005) | `cited_by_count` **24**; `updated_date` 2026-09-29 | metadata | W2 | Same 24 citers as the baseline count; no new OpenAlex-indexed citer |
| [Topalova ORCID works](https://pub.orcid.org/v3.0/0000-0003-3821-4672/works) | record last modified 2026-10-18T00:04:53Z | titles/dates | W4 | Newest group is TZ 2026 (Axioms 15:762); the 2026-10-18 change is an MDPI-sourced duplicate of that DOI. Earlier items are Axioms 15(9):679, MEM 2026, Mathematics 14(4):687 and Axioms 15(1):35. No new (v,5,1) item |
| [Baicheva–Topalova CDF page](http://moi.math.bas.bg/~tsonka/MainCDF.htm) and `~tsonka/` | — | failed | W2 | **HTTP 404 (new access gap**; the baseline read it 2026-10-16). Not evidence of any status change |
| arXiv search ["difference families" OR "difference family"](https://arxiv.org/search/?query=%22difference+families%22+OR+%22difference+family%22&searchtype=all&order=-announced_date_first&size=25) | 898 results; 25 newest | titles + snippets | W4 | No cyclic (v,5,1) item. 2610.15826 ((λ,μ)-fold factorizations; v2 dated 14 Oct 2026) and 2609.29202 (geometric DFs) are different objects (snippet level) |
| [arXiv 2510.20446](https://arxiv.org/abs/2510.20446) (Liu–Feng–Wang–Zhang) | still **v1**, 23 Oct 2025 | abstract + history | W5 | Main theorem is about (v,4,λ) perfect DFs. Perfect-DF statements do not construct cyclic DFs |
| [arXiv 2610.10973](https://arxiv.org/abs/2610.10973) (Chee) | still **v1**, 7 Oct 2026 | abstract + history | W5 | Asymptotic only: "the Johnson bound is asymptotically attained at all lengths by optical orthogonal codes" |
| Sage develop `database.py` (§2) | — | grep | W5 | None of the six orders among the k=5 DF keys |
| DataCite sweeps (§3) | `created ≥ 2026-10-16` | titles | W2 | No difference-family record for these orders |
| Access-hole retry: [Bado, DataCite 10.13140/rg.2.2.13518.01601](https://api.datacite.org/dois/10.13140/rg.2.2.13518.01601) | created 2026-08-16T18:46:21Z | metadata only | W3 | Title "Difference families and pairwise balanced designs"; no abstract; body unread. Hole **narrowed to metadata, not closed** |
| Access-hole retry: [Heseleva et al., DataCite 10.5281/zenodo.23325540](https://api.datacite.org/dois/10.5281/zenodo.23325540) | created 2026-10-12T20:34:13Z | metadata + abstract | W3 | Supplementary material for "Maximum packings with block size five admitting a block-equitable 2-colouring", a different object (coloured packings). Files unread |

**Verdict: unchanged.** The bounded audits found no earlier construction for any of the six orders, and priority is unresolved. ACF 2004 Theorem 14 remains imported and not re-verified. Handbook VI.16, the 1996 Remark 4.10.18 and the paywalled OOC/whist bodies remain unread.

## 5. Point-cyclic 2-(88,4,1), 2-(100,4,1) and the v≡4 (mod 12), 100<v≤200 table (cyclic Z_v)

| Source | Version/date | Read scope | Window | Finding |
|---|---|---|---|---|
| [Crossref 10.3390/axioms15100762](https://api.crossref.org/works/10.3390/axioms15100762) (Topalova–Zhelezova 2026) | indexed 2026-10-15; `is-referenced-by-count` **0**; `"relation": {}` | metadata + abstract | W2 | No correction or update relation. Abstract: "Before the present study, v=64 was the smallest v for which neither theoretical nor constructive results on the existence of point-cyclic resolutions of 2-(v,4,1) designs were known." The 88 "smallest undetermined" statement (p.11) is from the baseline full-text read; not re-read |
| [OpenAlex W7221679325](https://api.openalex.org/works/doi:10.3390/axioms15100762) | `cited_by_count` **0**; updated 2026-10-15 | metadata | W2 | No citer |
| ORCID [Topalova](https://pub.orcid.org/v3.0/0000-0003-3821-4672/works) / [Zhelezova](https://pub.orcid.org/v3.0/0000-0002-9669-6916/works) | both last modified 2026-10-18T00:04Z (MDPI duplicate of TZ 2026) | titles/dates | W4 / W6 | No newer work by either author |
| [DataCite 10.5281/zenodo.13771464](https://api.datacite.org/dois/10.5281/zenodo.13771464) (Baicheva–Topalova 2024 dataset) | updated 2024-09-25; no new version | metadata + description | W3 | Still "All cyclic 2-(v,4,1) designs for v=40, 52, 64, 76, 88: d_4_1.zip", plus a partial backtrack for 100≤v≤160. These are underlying cyclic designs; no resolution claim. Zip files unread |
| arXiv search ["cyclically resolvable" OR "point-cyclic" OR "cyclic resolution"](https://arxiv.org/search/?query=%22cyclically+resolvable%22+OR+%22point-cyclic%22+OR+%22cyclic+resolution%22&searchtype=all&order=-announced_date_first&size=25) | **6** results | titles + snippets | W4 | None about designs |
| [DataCite 10.5281/zenodo.23454357](https://api.datacite.org/dois/10.5281/zenodo.23454357) ("kai", created 2026-10-18T15:19:16Z, submitted to DCC) | "submitted manuscript, 18 October 2026" | metadata + abstract | W4 | Verbatim abstract (superscripts flattened in the DataCite text): "We construct resolvable group divisible designs with block size four and groups of size two, 4-RGDDs, of types 246, 294, 2100, 2118, 2130, 2202 and 2214". The title reads these as 2^u, u ∈ {46, 94, 100, 118, 130, 202, 214}. **Not equivalent** at definition level: a 4-GDD of type 2^u does not cover pairs inside its groups, so it is not a 2-(v,4,1) design, and no point-cyclic resolution is claimed |

**Verdicts (unchanged):**
- **88:** NONE-FOUND-IN-SCOPE; NOVELTY-UNCLEAR. The 8p corollary is written only, and only v=88 is Lean-replayed (single kernel).
- **100, 112, 136, 160, 196:** DERIVED-OPEN with no prior found. 100 is still not an explicitly named open case.
- **Imported entries:** nonexistence at 124 and 172 (GMJ 1997) and existence at 148 (Lam–Miao 1999 body unread) are unchanged. 184 is decided only by the round's written corollary.
- **Group scope:** Z₄×Z₅² or C₄⊕G constructions are not point-cyclic on Z_v.
- **Carried holes:** Lam–Miao 1999 and 2001 bodies, Fuji-Hara–Miao–Shinohara 2002, Mishima–Jimbo 1997, the Mishima thesis, the Handbook 2nd edition, and the published (non-preprint) GMJ, MJ and LMM versions.

## 6. Four BTD instances

Post-17 sources (all are grouped shared checks from §2, plus):
- [arXiv search "ternary design(s)" OR "packing array(s)"](https://arxiv.org/search/?query=%22ternary+design%22+OR+%22ternary+designs%22+OR+%22packing+array%22+OR+%22packing+arrays%22&searchtype=all&order=-announced_date_first&size=25) (49 results, 25 newest, W4). The only design-theory hits are Rosin's 2025 papers; the rest are physics "packed arrays".
- DataCite design and topic sweeps since 2026-10-16 (W2): no balanced-ternary item.
- OpenAlex sweep (W3): none.
- CPro1 HEAD is unchanged, so `designs/balanced-ternary-design/` is the same tree the baseline read at 827f02b. [INFERENCE] This follows from commit identity; the folder was not re-listed.

| Instance | Accepted claim (local) | Post-17 | Verdict |
|---|---|---|---|
| BTD(12,15;6,2,10;8,6) | nonexistence (Connor-type proof + Lean replay) | Still in CPro1 `OPEN_INSTANCES`; Rosin still v1; no new source | NOVELTY-UNCLEAR, unchanged |
| BTD(14,18;7,1,9;7,4) | nonexistence (same method; one contribution with (12,15)) | Same | NOVELTY-UNCLEAR; the **partial prior** stays: the 1996 table left only b₂=14 open (Kunkle–Sarvate; Chawathe–Sarvate ms) |
| BTD(12,20;4,3,10;6,4) | nonexistence (computer-assisted, 3,073 DRAT; not Lean) | Same | NOVELTY-UNCLEAR, unchanged |
| BTD(14,28;8,3,14;7,6) | existence (explicit witness; not Lean) | Rosin Table 1 source still v1; CPro1 results unchanged | Priority not established, unchanged |

Carried holes, not retried: Handbook 2nd ed. VI.2, the Greig 2003 body and Greig's unpublished table, the Chawathe–Sarvate manuscript, Billington–Robinson 1983, the Sinha 1992 and Sarvate 1990 scans, and the OpenReview workshop PDF.

## 7. PA(19,8,6) — latest exact existence status

- **Local status (restated, unchanged): UNDECIDED.**
  - The **151 lane-original undecided cases** remain open (ms06 86, ms09 65).
  - The measured M2H coverage is two **separate** views, never merged: v6_3 direct pilot **3/5,424** and v6_4 split pilot **1/5,424**.
  - **No pruning counts from GPS1/GPS2 are accepted**: applied-list and orbit coverage are INCONCLUSIVE.
  - The PA18 witness is a lower bound only. The LRAT-only route was withdrawn. Native expansion is not authorized.
  - A₆(8,7) ∈ {18, 19} remains undetermined.
- **Equivalents checked (definition level, from the baseline):** PA(19,8,6) ⇔ A₆(8,7) ≥ 19. A KSP(19), equivalently a KPD({3,4*},19), with 8 classes ⇒ PA(19,8,6) (the E0 column profile only). CKPD, KPD({3,4**}) and KPD({3,5*}) are not equivalent.

| Source | Version/date | Read scope | Window | Finding |
|---|---|---|---|---|
| CPro1 PA definition and results (§2) | HEAD 827f02b | full file / listing | W1, W3 | No (19,8,6) instance or result; the 18-8-6 result is present |
| Rosin 2501.17725 / 2505.23881 (§2) | v1 / v1 | abstract + history | W1 | No new version |
| [arXiv 2608.01606](https://arxiv.org/abs/2608.01606) (Sadhu) | still **v2**, 8 Aug 2026 12:06:57 UTC | abstract + history | W1 | "Hence pa(5;6) = pa(6;6) = 31." These are other cells; nothing on (8;6) |
| arXiv search (§6) and DataCite sweeps (§3) | since 2026-10-16 | titles + snippets | W2, W4 | No packing-array, Kirkman-school or orthogonal-partial-Latin item on (8,6) |
| Access-hole retry: Colbourn–Ling 1999, [doi:10.1016/s0012-365x(99)00015-1](https://doi.org/10.1016/s0012-365x(99)00015-1) | Crossref shows an Elsevier open-archive licence from 2013-07-17 | [Crossref metadata](https://api.crossref.org/works?query.bibliographic=Kirkman+school+project+designs+Colbourn+Ling&rows=3) (W4); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0012365X99000151) **403**; [Elsevier API](https://api.elsevier.com/content/article/PII:S0012365X99000151?httpAccept=text/plain) **400** (W5) | W4–W5 | **Hole persists**: the v=19 KSP/KPD status is still unread. Cao–Du 2004 was not retried |

**Verdict: no public construction or nonexistence claim for PA(19,8,6), and no A₆(8,7) claim, found in scope.** Status is UNDECIDED, unchanged.

## 8. Prior-claim and stale items — non-reset check

| Item | Source re-read post-17 | Window | Finding | Status |
|---|---|---|---|---|
| 8 optimal CPCW codes | [DataCite 10.5281/zenodo.22076107](https://api.datacite.org/dois/10.5281/zenodo.22076107) (Vos) | W2 | `state` findable, `isActive` true; registered and updated 2026-08-24T17:43:47Z; `IsVersionOf` 10.5281/zenodo.22068088. Abstract: "We present explicit optimal binary cyclically permutable constant-weight codes for all nine parameter cases identified as unresolved by Baicheva and Topalova" | **PRIOR-CLAIM retained**; ours is an independent confirmation. The (163,5,1) ancillary result is still not folded in |
| L(12,3)=36 | [DataCite 10.5281/zenodo.22639692](https://api.datacite.org/dois/10.5281/zenodo.22639692) (Raval v0.1.0) | W2 | Findable; updated 2026-09-07T09:15:28Z. Abstract: "Technical report, exhaustive-search software, and source-bound evidence establishing L(12,3) = 36." | **PRIOR-CLAIM retained** |
| SW(25,16) | [DataCite 10.5281/zenodo.23404962](https://api.datacite.org/dois/10.5281/zenodo.23404962) (Long) | W3 | Findable; updated 2026-10-15T20:42:34Z. Abstract: "We exhibit symmetric weighing matrices SW(25,16), SW(27,16) and SW(29,16)" | **Stale retained**; Long's matrices are still unverified by us |
| BRD(26,130,25,5,4) | [Crossref 10.1007/s10623-010-9477-6](https://api.crossref.org/works/10.1007/s10623-010-9477-6) (ACCP 2011) | W4 | `"relation": {}` (no update or retraction relation); `is-referenced-by-count` 6. The abstract was not re-read | **Stale retained** |
| CFR(4,33) | Sage develop `database.py` (§2) | W1 | "(33 ,1) : (6 ,DM_33_6_1)," still present | **Stale retained** |

## 9. Access limits

- **New in this refresh:**
  - Baicheva–Topalova `MainCDF.htm` and the `~tsonka/` homepage return HTTP 404.
  - The arXiv export API returned 429 (the HTML pages were used instead).
  - The DataCite design-term sweep page 2 (17 older records) was not read.
  - Crossref single-work `select` returned 400 (refetched without `select`).
  - OpenAlex was queried without a key (shared budget).
- **Retried, not closed:**
  - Colbourn–Ling 1999 (ScienceDirect 403, Elsevier API 400).
  - Bado RG preprint (metadata only).
  - Heseleva et al. files (metadata only).
- **Carried unchanged, not retried:** every hole listed in the baselines of §§3–7. Zenodo file and API access was not attempted. Semantic Scholar, Google Scholar, MathSciNet and CNKI were not used.

## 10. Deviations and limits of this record

- Per-request clock times were not captured; windows W1–W6 are bracketed by `/bin/date`.
- The nine pre-release `/bin/date` calls ran without an explicit `TMPDIR` (`date` writes no temp files). They were at 16:55:05, 16:56:26, 16:56:45, 16:56:54, 16:57:21, 16:57:33, 16:58:15, 16:58:39 and 16:58:49.
- Later shell calls set `TMPDIR` to a run-local path that was never created. No directory or temp file was created.
- A single `/bin/sleep 70` background timer, not a loop, ran from about 16:58:59 to 17:00:09 so the worker could block until release. The start time is derived from the 70.17 s wall time.
- "Unchanged" means the same version, count or content in the fields actually read. It is not a claim that the unread bodies are unchanged.
- No correctness verdict was re-opened or strengthened. All 22 gate rows remain locally accepted at their stated scopes; none is human-peer-reviewed or proven novel. A shared mechanism is not multiple contributions.

## 11. Corrections relative to v1 (v1 retained unmodified)

1. §10 said "five pre-release `/bin/date` calls". The correct count is **nine**; the timestamps are listed in §10.
2. §0 said the source list was sent "At 16:56:54". It was sent **immediately after** the 16:56:54 stamp.
3. In §5, the v1 quote of the 4-RGDD abstract silently rendered "2^46, 2^94, 2^100". v2 quotes the DataCite text verbatim ("246, 294, 2100", superscripts flattened) and gives the reading from the record's title separately.
