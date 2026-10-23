# Cyclic (v,5,1) difference families: priority audit (read-only scout, 2026-10-16 PT)

Preserved verbatim. A search miss is not novelty.

I found no earlier construction or announced construction of a cyclic (v,5,1) difference family for any of v ∈ {321, 501, 621, 681, 801, 901}, and no nonexistence proof for any of them. The search was bounded and several sources were unreachable, so this is not a proof of novelty.

The latest primary sources still list all six as possible exceptions. The newest is Baicheva–Topalova, *Axioms*, 1 January 2026; two later papers by the same group (May and September 2026) neither restate nor touch these orders. For 501 there is one earlier claim. The 1996 CRC Handbook listed 501, 681 and 801 as known, and Abel–Costa–Finizio (2004) later said that listing was incorrect. Abel wrote both.

I edited no files and ran no solvers or model CLIs.

### Per-v status
The three names are the same object here. Since 5 ∤ v, every cyclic S(2,5,v) is strictly cyclic, and a perfect (v,5,1) OOC is the same thing as a cyclic difference family.

| v | factors | earlier construction located? | earlier claim | nonexistence claim | latest status statement |
|---|---|---|---|---|---|
| 321 | 3·107 | none | none | none | "except possibly" t=16 (HBT, online 2025-12-22; Axioms, 2026-01-01) |
| 501 | 3·167 | none | 1996 Handbook Remark 4.10.18 listed it as known; ACF 2004 says this was incorrect | none | "except possibly" t=25 (same two sources). The lane's certificate passed the parent checker (`cdf501-parent-verification-v1.json`, 2026-10-16 23:00:54 PDT) |
| 621 | 3³·23 | none | none | none | t=31, same sources |
| 681 | 3·227 | none | same 1996 listing, also called incorrect in 2004 | none | t=34, same sources |
| 801 | 3²·89 | none | same 1996 listing, also called incorrect in 2004 | none | t=40, same sources |
| 901 | 17·53 | none | none | none | t=45, same sources |

### Key evidence (verbatim quotes)
1. **Abel–Costa–Finizio**, Discrete Appl. Math. 143 (2004) 43–53, DOI 10.1016/j.dam.2003.12.005. Read from the local reader text (`…/cdf-k5/sources/abel-costa-finizio-2004-academia-107955257.reader.txt`).
   - Lines 452–453: "in Remark 4.10.18 of [1], the three values 501, 681 and 801 were incorrectly given as known." Here [1] is Abel's own 1996 Handbook chapter.
   - Line 601, Theorem 14 as extracted: "If v ≡ 1 mod 20, v 6 1001 and v ∈ {321; 501; 621; 681; 801; 901} then a cyclic (v; 5; 1) DF exists." The extraction turns "≤" into "6" and "∉" into "∈".
2. **Hetman–Baicheva–Topalova**, JACODESMATH 13(1) 111–119. Received 14 May 2025, accepted 20 Sep 2025, online 22 Dec 2025. Read the full PDF.
   - p.114: "A (20t + 1,5,1) CDF exists for 1 ≤ t ≤ 50 except possibly for t = 16,25,31,34,40,45 [2]".
   - [2] is ACF 2004. The Handbook 2nd edition is cited only "for general background".
3. **Baicheva–Topalova**, *Axioms* 15(1):35. Received 3 Dec 2025, published 1 Jan 2026. Read the full mdpi-res PDF.
   - "According to [26], a (20t + 1, 5, 1) difference family exists for 1 ≤ t ≤ 50 except possibly for t = 16, 25, 31, 34, 40, 45." [26] is ACF 2004.
   - Their own search only covered "k = 5 and v ≤ 181".
4. **Baicheva–Topalova**, MEM 55 (2026) 329–339, from the April 2026 conference, online 19 May 2026. Read the full PDF. For k = 5 their range is "90 ≤ v ≤ 123".
5. **Baicheva–Topalova CDF data page** (`moi.math.bas.bg/~tsonka/MainCDF.htm`, created 2024-10-10, last saved 2025-05-12). The only k=5 link is "(21-105,5,1)". Her home page lists "(v,5,1) CPCW codes with v ≤ 89" and "(v,5,1) optical orthogonal codes with 90 ≤ v ≤ 123".
6. **Handbook 2nd edition (2007)**, via public Open Library/Internet Archive full-text search snippets only.
   - It contains "The number N of inequivalent (v, 5, 1) difference families over Zv. V 21 25 41 45 61 65", and its bibliography cites ACF 2004.
   - The phrase queries "501 621 681", "501 681 801", "681 and 801" and "v 5 1 DF" returned no hits anywhere in the index. OCR makes this weak negative evidence only.
7. **Dinitz's "New results" page for Handbook Part VI** (last edited 10/18/2019). Its chapter-16 entries are p.397 Theorem 16.29 and p.406 Theorem 16.77; neither is about (v,5,1).
8. **Buratti–Pasotti**, DCC 56 (2010) 1–20 (abstract and zbMATH review only). It covers "a cyclic (pq, 5, 1) difference family whenever p and q are primes congruent to 11 (mod 20)", checked up to 1000. None of the six has that form.
9. **Sage** (`database.py`, develop branch, fetched 2026-10-16; commit not pinned). The only k=5 entries are (21,5,1), (45,5,1), (65,5,1), (81,5,1), (121,5,1), (141,5,1), (161,5,1), (201,5,1) and (221,5,1).
10. **Recent general status statements.**
    - Liu–Feng–Wang–Zhang, arXiv:2510.20446v1 (23 Oct 2025; JCTA 2026): "For k⩾5, the existence of (v,k,1)-CDFs is far from being settled".
    - Buratti–Muzychuk, ADAM 8 (2025) #P1.01: the cyclic spectrum is determined "only for k = 3 … and for k = 4".

### Do not conflate
- **Perfect difference families.** Kotzig–Turgeon (cited in arXiv:2510.20446): "There are no (v,k,1)-PDFs for … k=5 and v≡21 (mod 40)". This covers 501, 621 and 901, but it rules out only the special perfect (Abrham-type) families, not cyclic difference families.
- **Chee, arXiv:2610.10973v1 (7 Oct 2026).** Its result is asymptotic: "the Johnson bound is asymptotically attained…". It gives no exact codes for any specific v.
- **Known weight-5 OOC families can't reach these lengths.** This is my own arithmetic from the families listed in *Axioms* 15(1):35 §1.2 and arXiv:1911.07189v2 Thm 7.1. Their lengths are 15p, 4p, 4up, 3ˢ·5v, gv with 20 | g, 5v, 45v, 5pq and 5p², all divisible by 4 or 5. Prime-power families don't apply because none of the six is a prime power. Product constructions would need factors ≡ 1 (mod 20), and no factor here is.

### Forward citations
| work | OpenAlex | Crossref | zbMATH | found by reading reference lists |
|---|---|---|---|---|
| ACF 2004 | 24 (newest: Axioms 15(9):679, 2026-09-11; Axioms 15(1):35, 2026-01-01) | 19 | 17 (newest: HBT 2026) | HBT 2026 (missing from OpenAlex) |
| HBT 2026 | 1 (Axioms 15(10):762, 2026-10-13, about 2-(64,4,1) designs) | 1 | — | Axioms 15(1):35 [25], Axioms 15(9):679 [30], MEM 2026 [25]; so at least 4 in total |

I screened all 24 OpenAlex citers of ACF by title. I read the full text or abstract of the relevant ones: Axioms 15(1):35, Axioms 15(9):679, Axioms 15(10):762, Buratti–Pasotti, and arXiv:1911.07189. None reports any of the six orders.

### Other sources checked (all fetched 2026-10-16)
- **openai/math**: the remote `CONTENTS.md` ("719 manuscripts covering 372 result families") and the local clone's `.md` files have no difference-family, OOC, Steiner, whist or BIBD items.
- **EulerSolve** `/papers/` (291 papers): the only "Steiner" hits are Steiner trees and Steiner pedal curves.
- **Other listings**: arXiv author pages for Hetman (13 items; latest arXiv:2604.04975 is about S(2,7,·)) and Menglong Zhang (13) have nothing on k=5. Topalova's ORCID (updated 2026-10-13) and Buratti's 2024 CV have no such item either.
- **Other tables**: Krčadinac's table has only S(2,5,41/45/65); the La Jolla repository holds no difference families.
- **Searches**: OpenAlex full-text searches, a zbMATH search for "(v,5,1)" since 2005, and web searches for each specific "(v,5,1)" string turned up nothing relevant.
### Access holes
- **Handbook 2nd edition, §VI.16 (pp. 392–410):** body not read. Google Books returned 429, the Internet Archive search-inside endpoint 403, and Taylor & Francis is paywalled (Part VI DOI 10.1201/9781420010541.pt6 confirmed via Crossref). Only the snippets above were seen.
- **Handbook 1996, Remark 4.10.18:** not read; I know what it said only through ACF 2004.
- **Handbook errata page:** HTTP 401.
- **Citation indexes:** Google Scholar returned 403. The Semantic Scholar API failed in the fetch tool ("Failed to extract paper ID"). MDPI HTML returned 403, so I used the mdpi-res PDFs instead.
- **Paywalled or unopened bodies:**
  - Buratti–Pasotti 2010
  - Ma–Chang 2004/2005, Chang–Ji 2004, Tang–Yin 2002, Yin 1998
  - Park et al. (TCOMM 2013) and the other LDPC citers
  - the whist and triplewhist citers
  - Baicheva–Topalova DCC 2019
  - Yin–Yang–Li FFA 2011 (snippet only)
  - Rudasill 2014 dissertation (PDF returned 403); Travers 2004 dissertation not opened
  - Baicheva–Topalova ACCT 2014 "New perfect difference families" (not located)
- **Colbourn's ASU page:** behind Cloudflare Access.
- **Not searchable from here:** CNKI and Chinese theses, talks, private communications.
- **Index gaps:** OpenAlex citation links are incomplete, because the HBT Crossref record has 0 deposited references.

### Suggested priority wording
- **501:** "We construct a cyclic (501,5,1) difference family, equivalently a perfect (501,5,1) OOC or strictly cyclic S(2,5,501). This order is a possible exception in Abel–Costa–Finizio 2004, Theorem 14, and is still listed that way by Hetman–Baicheva–Topalova (online December 2025) and Baicheva–Topalova (January 2026). A 1996 Handbook listing of 501 as known was declared incorrect in 2004. No earlier construction was located in our bounded search."
- **321, 621, 681, 801, 901:** open in the same sources; no earlier construction or nonexistence proof located.
- **Avoid** "first" or "never constructed". The main residual risks are the unread Handbook 2nd-edition text (judging it unlikely to contain a construction is my inference: the 2025–26 papers source the exception list to ACF 2004, and Dinitz's page has no related entry), paywalled 2004–2024 OOC and whist papers, and unindexed venues.
- **Significance:** a modest specialist finite result. It removes one of the six possible exceptions up to 1001.

### Local files used
- `/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/cdf-k5/sources/abel-costa-finizio-2004-academia-107955257.reader.txt:451-453,601`
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cdf501-parent-verification-v1.json` (status VALID, certificate SHA-256 517e02fa…ab74)
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/cdf501-multiplier-parent-audit.json`
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/screening/finite-info-target-screen.md` (its "could not access" items: the data page is now read; the Handbook is only partly probed)
