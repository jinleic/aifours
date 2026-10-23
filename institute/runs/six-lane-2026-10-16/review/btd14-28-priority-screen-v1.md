# BTD(14,28;8,3,14;7,6) bounded priority screen (scout report, verbatim)

Recorded 2026-10-17 12:28:32 PDT from the read-only scout `Btd1428Priority` (task agent). Verbatim copy of its final report; claims marked by the scout as unverified or inherited remain so.

I found no published construction or nonexistence proof for BTD(14,28;8,3,14;7,6) (class #234 in Billington–Robinson 1983, entry #121 in the 1996 Handbook). The strongest new evidence is the 1996 Handbook table itself, read from the author-hosted copy: it lists no known design for these parameters. A miss is not proof of novelty; three key sources were unreadable (see `blocked_sources`).

```json
{
  "summary": "No published construction or nonexistence proof for BTD(14,28;8,3,14;7,6) was found in any source read on 2026-10-17. This extends the parent audit in five ways. (1) Kunkle–Sarvate's 1996 Handbook (1st ed.) table, author-hosted copy, lists it as #121 (= Billington–Robinson class #234) with known b₂'s 'none' and open b₂'s '14..28', so no design was known in 1996. (2) That table cites Sinha 1992 and Dillon–Wertheimer 1985 only on other rows. (3) Rosin arXiv:2501.17725 is still v1. Its HTML Table 1 shows blank Greig and CPro1 cells for this instance, and the paper says CPro1's code was tested on every Table 1 instance. (4) Neither Rosin's May 2025 paper nor CPro1 HEAD (2026-06-03) has a result for it; the BTD results folder last changed 2025-05-29. (5) Dinitz's Handbook-update pages have no entry for it. The 1st-edition page (2005) does record unpublished Greig improvements to the BTD table, contents unknown. Forward citations and 2024–2026 BTD searches found nothing relevant. The 2006 Handbook VI.2 text, the body of Greig's 2003 chapter and Greig's unpublished table could not be read.",
  "read_scope": {
    "full_text_read": [
      "Kunkle–Sarvate 1996 Handbook (1st ed.) section, author copy dated 'last changed: Sept 25, 96' (section.pdf)",
      "Kunkle–Sarvate JCMCC 22 (1996), preprint copy (94_10.pdf)",
      "Kunkle–Sarvate Ars Combin. 40 (1995), preprint copy (93_01.pdf, about first 300 of 383 lines)",
      "Rosin 2501.17725v1 HTML Table 1 and §3 text",
      "Rosin 2505.23881v1 (pinned PDF text): Table 1(a), §§3–4, references",
      "Francel–Hurd AJC 42 (2008), pinned: definitions and lemmas",
      "Srivastav–Srivastav 2026 preprint, Research Square v1 (pp. 1–17 read in full; rest grepped)",
      "arXiv 2605.12421 and 2607.16069 (grepped for 'ternary'/'Rosin')"
    ],
    "data_or_listing_pages_read": [
      "Kaski–Östergård BTD data page (all rows)",
      "CPro1 GitHub tree at HEAD and at tag v1.0; commits for the BTD folders; READMEs; problem_def.py",
      "constructive.codes homepage",
      "Dinitz 2nd-ed. Part VI 'new results' page (via WordPress REST)",
      "Dinitz 1st-ed. Part IV 'new results' page (Wayback, 2008-12-12)",
      "Handbook 2nd-ed. table of contents (HTW Berlin PDF)"
    ],
    "abstract_or_review_only": [
      "Greig 2003 chapter (Springer landing page; zbMATH Zbl 1056.05017)",
      "Billington–Robinson 1983 (Zbl 0534.05010)",
      "Dillon–Wertheimer 1985 (Zbl 0628.05007)",
      "Sinha 1992 (Zbl 0771.05015; Combinatorial Press abstract)",
      "Sarvate 1990 (Zbl 0703.05013; Cambridge abstract)",
      "Sarvate–Seberry 1993 (Zbl 0764.62062)",
      "Comm. Stat. 2026 residual-effect ternary designs (Zbl 08209314)"
    ],
    "title_or_metadata_only": [
      "OpenAlex citing works 2602.16807 and the 2026-09-29 Zenodo deletion-code dataset",
      "MDPI Mathematics 2026 nested-designs paper",
      "Crossref and zbMATH title lists"
    ],
    "inherited_from_parent_not_rechecked": [
      "arXiv API abs/ti search: totalResults = 2",
      "zbMATH 66-title BTD sweep (1975–2025)",
      "Kaski–Östergård scope quote (V≤10) from the zbMATH review",
      "CPro1 GitHub issues"
    ]
  },
  "findings": [
    {
      "claim": "The 1996 CRC Handbook BTD/BPTD table lists (14,28;8,3,14;7,6) as entry #121 (Billington–Robinson #234). No BPTD, and hence no BTD, was known for any b₂; every b₂ in 14..28 was open; no reference is given.",
      "quote": "Col. 10 shows the values of b₂ for which existence is in question. … 121 (234) | 14 28 | 8 3 | 14 7 | 6 none | 14.. 28",
      "url": "https://kunklet.people.charleston.edu/section.pdf",
      "source": "T. Kunkle & D.G. Sarvate, 'Balanced (Part) Ternary Designs', CRC Handbook of Combinatorial Designs (1st ed.) pp. 233–238; author-hosted copy",
      "date_version": "Copy marked 'last changed: Sept 25, 96'; published 1996. May differ from print (see Dinitz errata finding).",
      "verified": "yes — full table read",
      "stance": "supports-open"
    },
    {
      "claim": "The 1996 table already includes Sinha 1992 and Dillon–Wertheimer 1985. Sinha [8] is cited only on rows #107 (18,42;…) and #130 (16,28;6,4,14;8,6); Dillon–Wertheimer [5] only on #73 and #164. Neither is cited on #121. [INFERENCE] Sinha's 'two new designs' are #107 and #130, not the target.",
      "quote": "[8] K. Sinha, A construction of balanced ternary designs, Ars Combin., 33 (1992) … 107 (209)|18 42|12 1|14 6|4 6|7.. 18|[8] … 130 (245)|16 28|6 4|14 8|6 16|17.. 28|[8]",
      "url": "https://kunklet.people.charleston.edu/section.pdf",
      "source": "Kunkle–Sarvate 1996 table, reference column",
      "date_version": "1996",
      "verified": "yes for the citations; identity of Sinha's designs is [INFERENCE] (Sinha PDF is an unreadable image scan)",
      "stance": "nuance"
    },
    {
      "claim": "Kunkle–Sarvate JCMCC 1996, Appendix B, lists every table entry their results apply to or settle. #121 is not in any of the lists.",
      "quote": "Disregarding redundancies, here are the designs from the BPTD table [8] to which results in either this or our earlier paper [7] applies.",
      "url": "https://kunklet.people.charleston.edu/94_10.pdf",
      "source": "T. Kunkle & D.G. Sarvate, 'Balanced part ternary designs: some new results', J. Combin. Math. Combin. Comput. 22 (1996), preprint copy",
      "date_version": "1996",
      "verified": "yes — full text read",
      "stance": "supports-open"
    },
    {
      "claim": "On the Kaski–Östergård enumeration page the target is row 234 / KS 121 with empty enumeration columns. Their classification did not cover it (V=14 is outside the V≤10 scope recorded by the parent).",
      "quote": "234 | 121 | 14 | 28 | 8 | 3 | 14 | 7 | 6 | (Nd, Ns, |Aut(D)|, b2 blank)",
      "url": "https://users.ics.aalto.fi/pkaski/btd.html",
      "source": "Kaski & Östergård, data page for 'Enumeration of Balanced Ternary Designs', Discrete Appl. Math. 138 (2004)",
      "date_version": "page read 2026-10-17",
      "verified": "yes (row); scope quote inherited from parent",
      "stance": "nuance"
    },
    {
      "claim": "Dinitz's 1st-edition errata say the BTD table had errors, mostly in V=K rows (the target has V≠K). They also say unpublished Greig work improved the table, available only from Greig. Its contents are unknown, so this is an unverifiable priority risk.",
      "quote": "most of which are inconsistencies for V=K designs. Recent work, including unpublished work by Greig, has resulted in a number of improvements to the table. For an updated version of the table, contact greig@sfu.ca.",
      "url": "https://web.archive.org/web/20081212105122id_/http://www.emba.uvm.edu/~dinitz/newresults.part4.1.html",
      "source": "J. Dinitz, 'New Results in Part IV', CRC Handbook 1st ed.",
      "date_version": "Page 'Last edited on 6/10/05'; Wayback capture 2008-12-12",
      "verified": "yes",
      "stance": "nuance"
    },
    {
      "claim": "Greig's 2003 chapter settled several open BTD cases. Only the abstract is accessible, so which cases is unknown first-hand; Rosin attributes three of them to Greig, not the target.",
      "quote": "We settle several open existence cases for BTDs (including both suitable and unsuitable designs for our construction), and provide a number of suitable BnDs.",
      "url": "https://link.springer.com/chapter/10.1007/978-1-4613-0245-2_9",
      "source": "M. Greig, 'Constructions Using Balanced n-ary Designs', Designs 2002 (MAIA 563), pp. 227–254; zbMATH review Zbl 1056.05017 is generic",
      "date_version": "2003",
      "verified": "abstract only",
      "stance": "nuance"
    },
    {
      "claim": "Rosin's Table 1 lists the target among the Handbook's smallest open BTD instances, with both the Greig (2002) column and the CPro1 column blank. Neighbouring rows show Greig 'Exists' entries. arXiv API and DataCite both show v1 as the latest version.",
      "quote": "Open instances (V,B;p1,p2,R;K,L) | Greig (2002) | CPro1 … (12,28;10,2,14;6,6)? | Exists | … (14,28;8,3,14;7,6)? | | | (18,18;2,6,14;14,10)? | Exists |",
      "url": "https://arxiv.org/html/2501.17725v1",
      "source": "C.D. Rosin, arXiv:2501.17725, Table 1 (Handbook chapter VI.2 per its Table 2)",
      "date_version": "v1, 2025-01-29; still latest on 2026-10-17",
      "verified": "yes (HTML table; matches pinned layout line 105)",
      "stance": "supports-open"
    },
    {
      "claim": "Rosin states CPro1's generated code was tested on every smallest Handbook open instance in Tables 1–2, so CPro1 (Jan 2025) attempted the target and failed. A failed heuristic search is not evidence of nonexistence.",
      "quote": "we extend by testing the generated code on adjacent open instances, including all of the smallest open instances from the Handbook shown in Tables 1 and 2.",
      "url": "https://arxiv.org/html/2501.17725v1",
      "source": "Rosin arXiv:2501.17725v1, §3 (experimental protocol)",
      "date_version": "v1, 2025-01-29",
      "verified": "yes (statement); run logs not public",
      "stance": "supports-open"
    },
    {
      "claim": "Rosin's May 2025 paper lists seven Handbook BTD instances solved by CPro1; the target is not among them.",
      "quote": "(17,17;8,2,12;12,8) (14,21;6,3,12;8,6) (12,16;4,4,12;9,8) (16,16;7,3,13;13,10) (12,21;4,5,14;8,8) (16,22;9,1,11;8,5) (21,21;12,1,14;14,9) … Open instances from 2006 Handbook, that were solved and found to exist by CPro1.",
      "url": "https://arxiv.org/pdf/2505.23881v1",
      "source": "C.D. Rosin, arXiv:2505.23881, Table 1(a) (pinned layout lines 130–142)",
      "date_version": "v1, 2025-05-29; still latest (arXiv API)",
      "verified": "yes",
      "stance": "supports-open"
    },
    {
      "claim": "CPro1 repo at HEAD 827f02b (2026-06-03) has BTD result files only for 12-16, 12-21, 14-21, 16-16, 16-22, 17-17 and 21-21; there is no 14-28 file, at HEAD or at tag v1.0. The BTD results folder last changed 2025-05-29. OPEN_INSTANCES (initial run) omits the target; the README says later extension runs covered the paper's Table 1.",
      "quote": "problem_def.py has the OPEN_INSTANCES from the initial run, which yielded initial successful results. After that, extension runs were done that included the additional open instances listed in Table 1 of the paper.",
      "url": "https://github.com/Constructive-Codes/CPro1/tree/827f02b4048fc96a6b79f0970c87ca5a54f31f40/designs/balanced-ternary-design",
      "source": "CPro1 GitHub (git tree API, commits API, CPro1/design_definitions/balanced-ternary-design/README.md)",
      "date_version": "HEAD 2026-06-03; BTD results commit 5b26b1a (2025-05-29)",
      "verified": "yes",
      "stance": "supports-open"
    },
    {
      "claim": "Rosin's results page announces no BTD results after May 2025. Its newest item is 2026-03-02 (constant-weight codes), and it describes the NeurIPS 2025 workshop paper as a summary of the two preprints.",
      "quote": "This is an updated brief workshop paper that summarizes the results in the preprints below.",
      "url": "https://constructive-codes.github.io/index.html",
      "source": "constructive.codes (C.D. Rosin)",
      "date_version": "feed updated 2026-03-03",
      "verified": "yes",
      "stance": "supports-open"
    },
    {
      "claim": "The Handbook 2nd-ed. update page for Part VI has no entry for VI.2, Balanced Ternary Designs (pp. 330–332). Its first entry is p. 335 (VI.3).",
      "quote": "Last edited 10/18/2019 … Page 335, Theorem 3.14: A PBTD(9) has been constructed by M. Araya and N. Tokihisa.",
      "url": "https://site.uvm.edu/jdinitz/index.php?rest_route=/wp/v2/pages/413",
      "source": "J. Dinitz, 'New results in Part VI' (Handbook 2nd ed.)",
      "date_version": "text 'Last edited 10/18/2019'; WordPress modified 2021-07-26",
      "verified": "yes",
      "stance": "supports-open"
    },
    {
      "claim": "Handbook 2nd ed. chapter VI.2 is 'Balanced Ternary Designs' by Hurd & Sarvate, pp. 330–332. Its text was not accessible.",
      "quote": "2 Balanced Ternary Designs SPENCER P. HURD, DINESH G. SARVATE 330 3 Balanced Tournament Designs ESTHER R. LAMKEN 333",
      "url": "https://sisis.rz.htw-berlin.de/inh2007/12355378.pdf",
      "source": "Handbook of Combinatorial Designs, 2nd ed., table of contents",
      "date_version": "2006/2007 edition",
      "verified": "yes (TOC only)",
      "stance": "nuance"
    },
    {
      "claim": "OpenAlex forward citations of both Rosin preprints return one work, an unrelated deletion-code dataset; the cached cited_by_count fields still read 0. A full-text search for the workshop title finds three citing works (2603.00174, 2602.16807, 2607.16069), none about BTDs; 2607.16069 has no 'ternary' match. DataCite citationCount for 2501.17725 is 0.",
      "quote": "\"count\": 1 … \"display_name\": \"A binary two-deletion-correcting code of length 16 with 216 codewords\"",
      "url": "https://api.openalex.org/works?filter=cites:W4406975762|W4414855602",
      "source": "OpenAlex API; DataCite API",
      "date_version": "queried 2026-10-17",
      "verified": "yes",
      "stance": "supports-open"
    },
    {
      "claim": "zbMATH shows no 2008–2026 paper on BTD existence for this case. The keyword 'balanced ternary design' returns four papers, none relevant. A '\"balanced ternary\"' search for 2015–2026 returns Rosin's two papers plus unrelated or statistical items. Billington's ternary-titled papers end in 1993, so the updated list Kunkle–Sarvate expected from her was not found.",
      "quote": "Found 4 Documents … Monadic balanced ternary designs … Packed and monadic balanced ternary designs with common reductions … Nested balanced ternary designs and Bhaskar Rao designs … Some series of partially balanced ternary designs",
      "url": "https://zbmath.org/?q=ut%3A%22balanced+ternary+design%22+py%3A2008-2026",
      "source": "zbMATH Open",
      "date_version": "queried 2026-10-17",
      "verified": "yes (titles/reviews only)",
      "stance": "supports-open"
    },
    {
      "claim": "Related but different object: packed BTDs (Francel–Hurd). The target is not packed, because a packed design needs B = ρ₁V = 112 ≠ 28 and ρ₂ = Nρ₁ = 24 ≠ 3. Their constructions therefore do not apply.",
      "quote": "A BTD with odd block size K = 2N + 1 is said to be packed if every block in the design is packed. … (a) B = ρ1 V, (b) ρ2 = Nρ1",
      "url": "https://ajc.maths.uq.edu.au/download/42/ajc_v42_p003.pdf",
      "source": "M.A. Francel & S.P. Hurd, Australas. J. Combin. 42 (2008) 3–19",
      "date_version": "2008",
      "verified": "definitions yes; arithmetic is mine",
      "stance": "nuance"
    },
    {
      "claim": "Related but different object: the multiset-space construction gives ternary designs only when s = 2 ≥ (k+1)/2, i.e. block size k ≤ 3, and its block counts are binomial. It cannot give K=7, B=28.",
      "quote": "Let v ≥ k ≥ 2 and s ≥ (k + 1)/2 (the regime in which pairwise balance is preserved by Proposition 3.1).",
      "url": "https://www.researchsquare.com/article/rs-8595082/v1",
      "source": "S.K. Srivastav & A. Srivastav, 'Construction of Balanced n-ary Designs via Complete Multiset Spaces' (preprint)",
      "date_version": "v1, 2026-04-21",
      "verified": "yes",
      "stance": "nuance"
    },
    {
      "claim": "Classical families checked against the target do not produce it [INFERENCE: my arithmetic]. Kunkle–Sarvate 1995 Thm 2.1 and Results 1.5–1.7 need K even or K ∈ {V, V−1}; here K=7, V=14. Sarvate 1990's main family puts the same number of doubled elements in every block; the target has 42/28 = 1.5 per block.",
      "quote": "If there exists a BIBD with parameters (V, b₁, ρ₁, K, λ₁) and a BIBD with parameters (V, b₂, ρ₂, K/2, λ₂), then one can construct a BPTD",
      "url": "https://kunklet.people.charleston.edu/93_01.pdf",
      "source": "Kunkle–Sarvate, Ars Combin. 40 (1995); Sarvate, J. Austral. Math. Soc. A 48 (1990), zbMATH review Zbl 0703.05013 ('equal numbers of elements occur twice in all blocks')",
      "date_version": "1995 / 1990",
      "verified": "text and review yes; applicability is [INFERENCE]",
      "stance": "nuance"
    },
    {
      "claim": "Related instances, kept separate: (12,28;10,2,14;6,6) and (18,18;2,6,14;14,10) exist and (12,26;3,5,13;6,5) does not, all per Greig via Rosin; all three were open in 1996 (#113, #147, #99). (14,21;6,3,12;8,6) exists (CPro1, Jan 2025). (21,21;12,1,14;14,9) exists (CPro1, May 2025). (14,18;7,1,9;7,4) is still open. (14,28;4,4,12;6,4), same V and B, was already known to exist in 1996 (#77, known b₂ = 28).",
      "quote": "77 (160)|14 28|4 4|12 6|4 28|19.. 27 … 113 (223)|12 28|10 2|14 6|6 none|8.. 24 … 147 (266)|18 18|2 6|14 14|10 none|18",
      "url": "https://kunklet.people.charleston.edu/section.pdf",
      "source": "Kunkle–Sarvate 1996 table; Rosin 2501.17725v1 Table 1; Rosin 2505.23881v1 Table 1(a)",
      "date_version": "1996 / 2025",
      "verified": "yes",
      "stance": "nuance"
    }
  ],
  "open_status_assessment": "Best-supported status: existence was undecided in the published literature through at least May 2025, and no later resolution was found through 2026-10-17. Evidence chain: 1996, no design known (Kunkle–Sarvate #121, read directly). 2003, Greig did not settle it (per Rosin's blank cell; not read directly). 2006, the Handbook still marks it '?' (per Rosin; not read directly). 2019, no Handbook VI.2 update (read directly). Jan and May 2025, open, and CPro1 attempted it without success (read directly). 2025–2026, no forward citation, repo result or zbMATH/OpenAlex/Crossref item addresses it (read directly). Remaining priority risk is low-to-moderate, concentrated in: (a) the body of Greig's 2003 chapter; (b) Greig's unpublished updated BTD table, offered by email in 2005; (c) the 2006 Handbook VI.2 text and its references; (d) unindexed theses or conference notes. Several general constructions do not reach this instance [INFERENCE: my arithmetic]. Splitting the design into two smaller BTDs/BIBDs on the same 14 points with K=7 is impossible: each part needs B_i ≥ 14 by the rank (Fisher) argument, forcing B_i = 14 and R_i = 7; then 13Λ_i = 42 − 2ρ₂ forces ρ₂ = 8 and ρ₁ = 7 − 16 < 0. Consistency check the parent can run on the witness: its b₂ (blocks containing a doubled element) must lie in [14, 28] by Kunkle–Sarvate (3.2).",
  "blocked_sources": [
    "Handbook 2nd ed. VI.2 (Hurd–Sarvate, pp. 330–332): archive.org search-inside returned HTTP 403 (item is lending-restricted); Google Books API returned 429 twice; Google Books in-book search redirected to google.com/sorry (429). Not bypassed.",
    "Greig 2003 chapter (doi:10.1007/978-1-4613-0245-2_9): Springer paywall; the free preview PDF downloads as binary and text conversion failed (unsupported format). OpenCitations returned no citations.",
    "Sinha 1992 (Ars Combin. 33, CC-BY PDF on combinatorialpress.com): image-only scan, no text layer, and no OCR tool available.",
    "Sarvate 1990 (J. Austral. Math. Soc. A 48, free PDF on Cambridge Core): image-only scan, text extraction failed.",
    "Sarvate–Seberry 1993 (JSPI 34): the UOW repository copy is behind an AWS WAF bot challenge; ScienceDirect not attempted (paywall).",
    "Rosin, NeurIPS 2025 MATH-AI workshop paper (OpenReview WlXSZiqcbH): OpenReview browser-verification page via api2.",
    "Semantic Scholar API: the reader tool could not parse any of three URL forms (tool-side failure), so S2 forward citations were not obtained.",
    "Zenodo records API: HTTP 403.",
    "Not online, so only zbMATH reviews were read or nothing attempted: Billington–Robinson 1983, Billington 1984/1989, Dillon–Wertheimer 1985, Francel–Sarvate 1991 (Util. Math. 39), Chawathe–Sarvate 'Improved entries…' (unpublished manuscript; no zbMATH record), Greig's unpublished updated table."
  ],
  "unverified_or_dropped": [
    "Unverified: that the 2006 Handbook VI.2 marks the target '?'. Known only through Rosin 2025.",
    "Unverified: that Greig 2003 does not settle the target. Known only through Rosin's blank cell; the chapter body is unread.",
    "[INFERENCE] Sinha 1992's two new designs are 1996-table rows #107 and #130 (the only rows citing [8]), not the target.",
    "Unverified: that the published 1st-ed. print table matches the author-hosted copy dated Sept 25, 96. Dinitz says the print table's errors were mostly in V=K rows.",
    "Unverified: what CPro1 actually ran on the target (run logs not public). Only the protocol statement and the absent result file were checked.",
    "Discrepancy: OpenAlex cited_by_count = 0 for both Rosin papers, while its cites: filter returns one work.",
    "Dropped as unrelated after reading: arXiv 2605.12421 (CSP solver benchmark; no 'ternary' or 'Rosin'); arXiv 2607.16069 (complex weighing matrices; no 'ternary'); Srivastav–Srivastav 2026 (not applicable to K=7); Comm. Stat. 2026 'Ternary designs enabling efficient estimation of residual effects' (statistical residual-effect designs).",
    "Dropped at title level only: arXiv 2602.16807 (hypercube slicing), 2603.00174 (constant-weight codes; parent found no 'ternary'), MDPI Mathematics 2026 nested designs, Crossref 'Ternary Matrices over B3…' and the response-surface 'Modified Slope Rotatability for Balanced Ternary Designs…'.",
    "Inherited from the parent audit, not re-run: arXiv API search (2 results), zbMATH 66-title sweep, CPro1 GitHub issues, Kaski–Östergård scope quote."
  ],
  "recommended_wording": "BTD(14,28;8,3,14;7,6) (Billington–Robinson 1983 class #234; Kunkle–Sarvate 1996 entry #121). In the 1996 CRC Handbook BPTD table no design with these parameters was known, and every b₂ from 14 to 28 was listed as open. Rosin (arXiv:2501.17725v1, Table 1) lists it among the Handbook's smallest open BTD instances, with no resolution reported from Greig (2003) or from CPro1 (January and May 2025). A bounded search on 2026-10-17 (scope in the audit) found no published construction or nonexistence proof. The 2006 Handbook chapter VI.2, the body of Greig's 2003 chapter and Greig's unpublished updated table were not accessible, so priority is not established. Do not use 'first' or 'new'. Before any external claim, read Handbook 2nd ed. pp. 330–332 and Greig 2003 pp. 227–254 through a library; contacting Greig about his table needs owner approval."
}
```
