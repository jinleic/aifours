# gcDCQS(20^4:0): bounded priority audit

Recorded 2026-10-17 07:32:17 PDT. Read-only scout `GcdcqsPriority`; a search miss is not novelty. Raw scout report follows.

---

# Status audit: Tan & Zhou, arXiv:2503.11934, Section 4 problem (2)

## Summary
- **Versions.** arXiv has only v1, with no journal-ref. The paper was published in Des. Codes Cryptogr. 93(10) (2025) 4117–4140, DOI 10.1007/s10623-025-01677-x. The journal text is paywalled, so I could not read its Section 4.
- **Problem (2).** I found no construction or announcement of a gcDCQS(20⁴:0), a gcDCQS(32⁴:0), an mcDSQS(80), an mcDSQS(320), or the family mcDSQS(5·4ⁿ) in any source I checked. A search miss does not establish novelty.
- **Reference [16].** It is Shi–Xia–Krotov, JCTA 200 (2023) 105790. It shows explicitly that the derived STS(19) of Phelps' cyclic SQS(20) II.A.1 can be split into 10 colour classes (χ′ = 10).
- **Coverage.** The paper's families do not include 80 or 320.

## Report

### (a) Versions and journal publication
- **arXiv** (https://arxiv.org/abs/2503.11934):
  - Submission history: "[v1] Sat, 15 Mar 2025 00:56:13 UTC (24 KB)". No other version.
  - Comments: "25 pages". No journal-ref field. The only DOI is the arXiv one, 10.48550/arXiv.2503.11934.
  - arxiv.gg says "Latest revision 2025-03-18". arXiv's own history shows only v1. [INFERENCE] The arxiv.gg date is probably a metadata update, not a new version.
- **Journal** (https://link.springer.com/article/10.1007/s10623-025-01677-x, Crossref, OpenAlex W4411559024):
  - Des. Codes Cryptogr. 93, issue 10, pp. 4117–4140.
  - "Received: 24 January 2025 · Revised: 28 May 2025 · Accepted: 13 June 2025 · Published: 23 June 2025 · Issue date: October 2025". "Communicated by L. Teirlinck."
  - Closed access (OpenAlex `oa_status: closed`).
- **What I could compare in the journal version:**
  - The abstract is identical to arXiv except "motivated from" became "motivated by".
  - The journal has 24 references; arXiv has 25. The dropped one is arXiv [8] (Hartman 1994), which does not appear to be cited in the arXiv body text.
  - The references behind Corollary 2.6 are still there: Xu–Bao–Ji 2020 (2-RSQS\*) and Ji–Yin 2010 (RDTD).
  - The appendices shown on the Springer page still cover Lemma 3.1 (CQS(8⁴:2)), "An mcDSQS(26) and an mcDSQS(32)", and Lemma 3.6.
  - [INFERENCE] Corollary 2.6 and the open problems probably survived, but I did not verify the journal's Section 4.
- **arXiv v1, Section 4, quoted exactly:**
  - "(1) Find more examples of mcDSQS(v)s, for example, an mcDSQS(38) and an RDSQS(52) (the smallest unknown mcDSQS(6n + 2)s and the smallest unknown RDSQS(6n + 4)s, respectively)."
  - "(2) Find a gcDCQS(v⁴ : 0) for v = 20, 32. Apply Corollary 2.6. If a gcDCQS(20⁴: 0) exists, then there exists an mcDSQS(5 · 4ⁿ) for any integer n ≥ 3. In the same way, the existence of a gcDCQS(32⁴: 0) will yield an mcDSQS(2^{2n+1}) for any integer n ≥ 4."
  - Introduction: "we only have one known mcDSQS(6n + 2) with n ≥ 2, that is, an mcDSQS(20) [16]."

### (b) Constructions resolving problem (2): not found
**Citing works (complete list found):**
- OpenAlex `cites:W4411559024` returns one work: Tan & Zhou, "Tilings of H_q(n,w) with optimal (n,d,w)_q-codes", DCC 94 (2026) art. 124, arXiv:2512.22754.
  - It cites the 2025 paper only in its Theorem 2.8, on RDSQS/LKTS of small orders.
  - Its full text contains no mcDSQS, gcDCQS or "minimum colorable", apart from the reference title.
- Springer/Dimensions shows "2 Citations" but does not list them. OpenCitations returned an empty list.
- OpenAlex full-text search for "minimum colorable derived" also finds Chen Wang, arXiv:2607.21521. It cites Tan–Zhou [16] only as a source of non-product LKTS constructions. [INFERENCE] This is probably Dimensions' second citation.

**Author output checked:**
- arXiv `au:Tan_Yuli`: 2602.16319, 2512.22754, 2510.24132, 2503.11934.
- arXiv `au:Zhou_Junling`: 2604.23558, 2603.12761, 2602.16319, 2512.22754, 2510.24132, 2501.07928, plus earlier papers.
- I grepped the full text of 2510.24132 and 2602.16319: no match. The other abstracts are off-topic.
- Zhou's faculty page (http://faculty.bjtu.edu.cn/5999) lists publications through two 2026 items. Its only mcDSQS item is the DCC 2025 paper.

**arXiv metadata searches (posts after March 2025; none relevant):**
- all:"Steiner quadruple": 2609.31783, 2606.03299, 2509.23483 (also grepped), 2509.06663, 2505.23881, 2504.16632.
- all:candelabra: only 2109.14140.
- "chromatic index" AND Steiner: 2503.11934 is the newest hit.
- all:"diameter perfect": 2608.14437, 2607.21037, 2605.09617.

**Other database queries:**
- Crossref, journal articles from 2025-03-01 with "Steiner quadruple" in the title: nothing relevant.
- OpenAlex citers of Shi–Xia–Krotov (5): only Tan–Zhou is about mcDSQS.

**Web searches:**
- The exact title.
- "gcDCQS" candelabra; "mcDSQS".
- `"RDSQS(52)" OR "mcDSQS(38)" OR "gcDCQS(20" OR "mcDSQS(80)"`: zero relevant hits.
- SQS(80) with chromatic index; Hanani-derived SQS.
- Chinese-language searches for a BJTU thesis: no thesis found.

**Inaccessible:** Semantic Scholar (the tool rejected every URL form), Google Scholar (HTTP 403), CNKI (not tried).

### (c) Reference [16]
- **Citation:** M. Shi, Y. Xia, D.S. Krotov, "A family of diameter perfect constant-weight codes from Steiner systems", J. Combin. Theory Ser. A 200 (2023) 105790, DOI 10.1016/j.jcta.2023.105790. arXiv:2212.00048: v1 30 Nov 2022, v2 31 Jul 2023, the accepted version.
- **What it proves (v2, Proposition 3):** "The values q₀′(3,4,14) and q₀′(3,4,20) equal 9 and 11, respectively."
  - The proof takes "the cyclic SQS(20) (II.A.1) from [27]", which is Phelps, Ann. Discrete Math. 7 (1980) 277–300.
  - It notes that "Because of the cyclicity, all derived STS are isomorphic", and lists a partition of the derived STS(19) "into 10 cells with mutually disjoint blocks".
  - The lower bound is "χ(S′) ≥ ⌈57/6⌉ = 10". So χ′ = 10: every derived design is minimum colourable, and the system is an mcDSQS(20).
  - Tan–Zhou's Lemma 3.4 relies on exactly this: "Shi et al. show that the cyclic SQS(20) constructed in [14] is an mcDSQS(20)."
- **Its Conjecture 2:** "If 20 ≤ n ≡ 2 mod 6, then there is an SQS(n) such that all its derived STS have chromatic number n/2". This is the general mcDSQS existence conjecture.

### (d) The paper's family theorems; are 80 and 320 covered?
- **Known orders in the paper:**
  - Lemma 3.4: "There exists an mcDSQS(v) for v = 20, 26, 32." The 26 and 32 systems are cyclic and found by computer.
  - Theorem 3.9: "There exists an mcDSQS(2 · 9ⁿ + 2) for any positive integer n." This gives 20, 164, 1460, …
  - Theorem 3.2 covers RDSQS(2^{2n+1}+2), which are orders ≡ 4 (mod 6) and so irrelevant here.
  - Theorem 3.10(2) settles the code question only for n ∈ {2·9ᵐ+2 : m ≥ 1} ∪ {26, 32}.
- **Neither 80 nor 320 is covered.** 2·9ᵐ+2 = 80 would need 9ᵐ = 39, and 320 would need 9ᵐ = 159. The paper itself calls 38 the smallest unknown order.
- **The recursive results problem (2) relies on:**
  - Corollary 2.6: "Let m ≡ 4, 8 (mod 12). If there exist a gcDCQS(m⁴ : 0) and an mcDSQS(m), then there exists an mcDSQS(m · 4ⁿ) for any integer n ≥ 2."
  - It uses Construction 2.4 together with Theorem 2.5: a 2-RSQS\*(4ⁿ) exists for n ≥ 2, and an RDTD(3,4,m) exists when "gcd(m,4) ≠ 2 and gcd(m,18) ≠ 3". I checked the ≠ signs in the HTML version; the PDF extraction drops them. Both conditions hold for m = 20 and m = 32.
  - With m = 20, the corollary gives 20·4ⁿ for n ≥ 2, i.e. 320, 1280, …, which matches "5·4ⁿ, n ≥ 3".

### (e) Inferences
- **[INFERENCE] 80 also follows.** Construction 2.1 says: "If there exist a gcDCQS(gⁿ: s), an mcDSQS(g+s) and a gcDSQS(g+s, s), then there exists an mcDSQS(gn+s)." Take g = 20, n = 4, s = 0.
  - With an empty hole, a gcDSQS(20,0) is just an mcDSQS(20). Corollary 2.6's own proof fills holes with mcDSQS(m) alone, which supports this reading.
  - So a verified gcDCQS(20⁴:0) plus Phelps' mcDSQS(20) would also give an mcDSQS(80), the n = 2 case that problem (2) does not mention. Likewise, a gcDCQS(32⁴:0) would give an mcDSQS(128).
- **[INFERENCE] Colour counts.** By the paper's (1.1), χ′(79) = 40 and χ′(319) = 160. So mcDSQS(80) requires every derived STS(79) to be 40-colourable.
- **[INFERENCE] Code consequence.** By Corollary 1.4, an mcDSQS(80) would settle q₀′(3,4,80) = 41. That would also be a new case of Shi–Xia–Krotov's Conjecture 2, since none was found in the sources checked.
- **[INFERENCE] Same authors, later paper.** The Tilings paper (posted December 2025, published June 2026) does not mention gcDCQS or mcDSQS. That is weak evidence the authors had not announced either object by then; it is not evidence that none exists.

## Sources
- https://arxiv.org/abs/2503.11934, plus the v1 PDF and HTML: abs metadata; Corollary 2.6, Theorem 2.5, Constructions 2.1 and 2.4, Lemma 3.4, Theorems 3.2, 3.9, 3.10; Section 4; references.
- https://link.springer.com/article/10.1007/s10623-025-01677-x, its /metrics page, and https://api.crossref.org/works/10.1007/s10623-025-01677-x: journal metadata, dates, reference list, appendices, citation count.
- https://api.openalex.org/works?filter=cites:W4411559024: the one citing work.
- https://arxiv.org/pdf/2212.00048v2, around Proposition 3 and Conjecture 2: reference [16].
- https://arxiv.org/pdf/2512.22754 (Theorem 2.8 and its reference [50]) and https://arxiv.org/pdf/2607.21521 (introduction and its reference [16]): the two citing works.

**How the pieces connect:** a gcDCQS(m⁴:0) becomes a gcDCQS(m^{4ⁿ}:0) via Construction 2.4, using a 2-RSQS\*(4ⁿ) and an RDTD(3,4,m). Filling its holes with an mcDSQS(m) via Construction 2.1 gives an mcDSQS(m·4ⁿ). The only verified mcDSQS(20) input is Phelps' cyclic SQS(20), shown to qualify in [16].
