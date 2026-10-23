# Tan–Zhou §4(3) pre-freeze priority screen and gcDCQS(32) addendum (scout Gcdcqs32Priority, delivered 2026-10-17 ~16:0x PDT; server stamps 22:59–23:00Z)

Verbatim scout report follows. Bounded screen only; a miss is not novelty.

**Outcome: NONE-FOUND-IN-SCOPE.** I found no earlier gcDCQS(32⁴:0), and no earlier mcDSQS(2^{2n+1}) of order 128 or more. The result also does not follow from published work. Only I1 is classical. I could not find I2, gcDCQS(8⁴:0), anywhere. I could not find I3, FDH(5,8,4,3), either, but the main paper where it could appear (Chang–Zheng–Zhou 2019) is paywalled and I could not read it. A miss is not novelty.

One trivial route is closed. The Boolean SQS(2^{2n+1}) is **not** an mcDSQS: by Meszka's theorem its derived designs PG(2n,2) need 2^{2n}+2 colours, two more than χ′.

## Evidence: prior-claim sweeps
| # | Source / query | Result | Quote or datum (URL, version/date) |
|---|---|---|---|
| 1 | Tan–Zhou arXiv:2503.11934 | Only v1 exists (DataCite version 1, registered 2025-03-18T03:33:02Z) | "Find a gcDCQS(v⁴ : 0) for v = 20, 32. Apply Corollary 2.6. … the existence of a gcDCQS(32⁴ : 0) will yield an mcDSQS(2^{2n+1}) for any integer n ≥ 4." (v1 §4(2); https://arxiv.org/abs/2503.11934v1) |
| 2 | Same paper, introduction | Known mcDSQS(6n+2) at the time | "we only have one known mcDSQS(6n + 2) with n ≥ 2, that is, an mcDSQS(20) [16]." (v1) |
| 3 | Journal version, DCC 93(10):4117–4140, online 2025-06-23 | Body paywalled. Springer shows "2 Citations"; Crossref is-referenced-by-count is 1. | https://doi.org/10.1007/s10623-025-01677-x |
| 4 | Citers of Tan–Zhou | OpenAlex `cites:W4411559024` gives 1 work: Tan–Zhou, *Tilings*, DCC 94 (2026) #124, arXiv 2512.22754. In its text, FDH 2019 appears only in the reference list. The arXiv record W6891900342 has 0 citers. zbMATH (Zbl 1575.05024) and MaRDI each list 1 citer. | — |
| 5 | Wang arXiv:2607.21521v1 (2026-07-23); probably Springer's second citer [INFERENCE] | Cites Tan–Zhou only as a source of large-set (LKTS) constructions | "designs and related structures were obtained by Xu and Ji [19], Liu and Lei [11], and Tan and Zhou [16]." |
| 6 | Authors' later output | OpenAlex: Tan 6 works, Zhou 8 since 2025-03. Zhou's faculty page (faculty.bjtu.edu.cn/5999) lists two 2026 items. No gcDCQS or mcDSQS follow-up. The lane's copy of the arXiv TeX source contains no hidden mention of FDGDD(3,4,5{8}) or gcDCQS(8⁴:0) (grep). | — |
| 7 | DataCite full-text queries | `"candelabra quadruple"`: 0 hits. `gcDCQS OR mcDSQS OR RDSQS OR RDCQS`: 2 (Tan–Zhou, Liu–Lei 2022). Minimum colorable/colourable: Tan–Zhou plus 2 unrelated. `"Steiner quadruple"` on Zenodo: nothing on colourings (Liu–Feng, BJTU, symmetric cyclic SQS data 2026-09-20; a nonsense "Dyson swarm" record 2025-12-30; Kiermaier–Krčadinac–Wassermann data 2025-09-18). Chromatic index, Kirkman frame, triple-system colouring, "diameter perfect", Hanani-type phrasings, and Zenodo Steiner colouring 2025–26: nothing relevant. | — |
| 8 | Zenodo record families, via DataCite creator search | Vos 32 records, Long 6, Raval 34, Kirtchakov 20, Ferudun 628 (newest 2026-10-17T22:00:30Z). Titles grepped: none on SQS, candelabra or STS colourings. | — |
| 9 | OpenAlex full-text | "candelabra quadruple": 21 hits, newest DCC 2026-05 (constant-composition codes), none on colourings. "mcDSQS": Tan–Zhou only. "gcDCQS" and "FDGDD": nothing relevant. "chromatic index" + "Steiner quadruple" since 2023: Tan–Zhou only. Shi–Xia–Krotov's 5 citers: none build mcDSQS(2^k). | — |
| 10 | arXiv API | 60 newest math.CO abstracts matching Steiner triple, Steiner quadruple, Kirkman, candelabra or quadruple system, back to 2022. Nothing on colourings of derived designs after 2503.11934. | — |
| 11 | Boolean route | Meszka's theorem as stated by Xu–Feng, Theorem 1.2: "For any even integer n ⩾ 4, χ′(PG(n,2)) = [n 1]₂ + 3". So χ′(PG(4,2)) = 18 > 16 and χ′(PG(6,2)) = 66 > 64. | arXiv 2206.00900v2 (2023-06-25); Meszka, JCD 21 (2013) 531–540 |

## Evidence: were the ingredients published?
The source's own route is Construction 2.3: "Suppose that there exists a 1-FG(3, (K1, K), gn) of type gⁿ … If there exist a gcDCQS(mk1 : s) … and an FDGDD(3, 4, k{m}) …, then there exists a gcDCQS((mg)ⁿ : s)."

| Ingredient | Status | Evidence |
|---|---|---|
| I1: 1-FG(3,({4},{5}),16) of type 4⁴ | **Classical** | Witt 1938: S(3,5,17) is unique (Kiermaier–Krčadinac–Wassermann table, v=17, k=5, 68 blocks, 1 design, "Möb(4)"; https://web.math.pmf.unizg.hr/~krcko/results/steiner3.html). Tan–Zhou Lemma 3.8: "There exists an RDS(3, q + 1, qⁿ + 1)…". Their proof of Construction 2.2 notes the RDS gives a "1-fan S(3, ({k}, {k+1}), n)". [INFERENCE] Taking one parallel class of AG(2,4) as the groups gives type 4⁴. Adding a point to the lines turns any such design into an S(3,5,17), so the lane's I1 is the classical one. I did not see the type-4⁴ step stated explicitly anywhere I could read. |
| I2: gcDCQS(8⁴:0) | **Not found** | The notion was only defined in 2025 (Tan–Zhou, good-colourable STS definition, lines 211–215). Their lemmas give RDCQS(8⁴:2), 1cDCQS(2⁹:2), 2cDCQS(2⁹:2), RDGDD(3,4,10{2}) and mcDSQS(20, 26, 32), but no gcDCQS(8⁴:0). Hand check of their cyclic mcDSQS(32) (Appendix B, via the lane's transcription): only the base block {0,8,16,24} lies inside a coset of ⟨4⟩. That gives 2 blocks per coset, where a sub-SQS(8) needs 14, so it does not yield a CQS(8⁴:0) with those groups. |
| I3: FDGDD(3,4,5{8}) = FDH(5,8,4,3) | **Not found; publication not ruled out** | Chang–Zheng–Zhou abstract: "direct constructions for FDH(v, 2, 4, 3)s are displayed by using automorphism groups" (DCC 87, online 2018-08-21). Liu–Lei cite that paper only for "an RDSQS(2v) for v ∈ {23, 29, 41, 47, 53, 59, 71, 83}" (arXiv 2210.06214v2). Zhang–Ge 2013 (DCC 69:65–76): for n = 5, H(g⁵) "exists whenever g is even, g [≠] 2 and g [≢] 10, 26 (mod 48)", so FDH(5,2,4,3) cannot exist. [INFERENCE, hand check] Inflating an FDH(5,4,4,3) to group size 8 needs an RDTD(3,4,2). Tan–Zhou's existence theorem requires gcd(m,4) ≠ 2, and the Latin square of order 2 has no parallel class, so none exists. Teirlinck's 3-frames F(3,4,n{2}) have group size 2 only. Tan–Zhou §4(3) still asks: "Construct a gcDCQS(18⁴ : 2) and an FDGDD(3, 4, 5{18})…". |

Derivability fails at I2 even if the Chang–Zheng–Zhou paper turns out to contain I3. [INFERENCE] The authors posed §4(2) while holding their own Construction 2.3, which weakly suggests they had neither I2 nor I3.

## Access holes
- **Chang–Zheng–Zhou, DCC 2019**, the main hole: body paywalled; only the abstract and references were read. FDH(5,8,4,3), or a recursion producing it, could be inside.
- **Chang–Zhou, JCTA 2013**: open archive, but ScienceDirect and its PDF return HTTP 403, and the Elsevier API returns 400 without a key. Its Lemma 5.14 context and any explicit type-4⁴ fan lemma are unread.
- **Tan–Zhou journal version §4**: paywalled. Its abstract on zbMATH and Springer lists no new mcDSQS families.
- **Citers on ScienceDirect** (Xu–Ji 2021 and 2022) return 403; Xu–Ji 2024 is paywalled; I read only zbMATH summaries.
- **Mills 1990** was not read; the H(g⁵) facts come from Zhang–Ge's summary.
- **Search tools**: the Zenodo API and search pages return 403, so Zenodo was covered through DataCite metadata only, not file contents. Semantic Scholar URLs are rejected by the tool. Google Scholar and CNKI were not reachable, so theses are unchecked. OpenAlex full text covers only abstracts for recent paywalled papers (searching "gcDCQS" does not even return Tan–Zhou), and one request hit HTTP 429. The arXiv API searches abstracts only.
- **Clock**: I have no shell or clock tool and could not read the host clock. The only timestamps are server-side: arXiv feeds stamped 2026-10-17T22:35:52Z–22:37:34Z, and the newest DataCite record seen was created 22:00:30Z. The certificate was assembled at 15:22:46 PDT (22:22:46Z) per the lane README. Records registered after about 22:3xZ are outside this screen.

## Recommended wording
"Tan and Zhou (arXiv:2503.11934v1, §4(2), 2025) asked for a gcDCQS(32⁴:0). We give an explicit one, checked against the definition by independent checkers. It comes from their Construction 2.3 with (m,g,n,s) = (8,4,4,0), using the classical fan design from the inversive plane of order 4 and two computer-found ingredients: a gcDCQS(8⁴:0) and an FDH(5,8,4,3) with Kirkman frames at every point. A bounded screen on 2026-10-17 found no earlier construction of these objects, or of an mcDSQS(2^{2n+1}) for 2n+1 ≥ 7. The full texts of Chang–Zheng–Zhou (2019) and Chang–Zhou (2013) were not accessible."

Do not write "first", "new FDH", or "Boolean SQS works".

## Files read
- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt:24-33,99-132,204-247,285-293,444-447,680-693,866-1116,1120-1128`
- `/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups/README.md` (E10 rows), `sources/construction-2.3-transcription.md`, `sources/tz_appb_mcdsqs32.json`, `sources/e11/arxiv-2503.11934v1-mcDSQS-0314.tex` (grep only)
- `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/gcdcqs20-priority-audit.md`
- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/wang-2607.21521.txt:42-71,558`

```json
{"outcome":"NONE-FOUND-IN-SCOPE","target":"gcDCQS(32^4:0); consequence mcDSQS(2^{2n+1}), n>=4 (also mcDSQS(128) via Construction 2.1 [INFERENCE])",
"prior_claims_found":[],
"derivable_from_published":{"value":false,"I1":"classical (Witt 1938 S(3,5,17), unique per KKW table; Tan-Zhou Lemma 3.8 + 1-fan remark; type-4^4 step [INFERENCE, routine])","I2_gcDCQS_8^4_0":"no source located; concept introduced 2025; Tan-Zhou App. B mcDSQS(32) has no sub-SQS(8) on cosets of <4> (hand check)","I3_FDH_5_8_4_3":"no source located; CZZ 2019 abstract: direct constructions only g=2; H(2^5) excluded (Zhang-Ge 2013 summary of Mills/Ji); RDTD(3,4,2) inflation impossible [INFERENCE]; body paywalled"},
"boolean_route":"excluded: chi'(PG(n,2)) = 2^n+2 for even n>=4 (Meszka 2013 via Xu-Feng arXiv 2206.00900v2 Thm 1.2)",
"citers":{"openalex_cites_W4411559024":1,"arxiv_record_W6891900342":0,"crossref_is_referenced_by":1,"zbmath":1,"springer_display":2},
"datacite":{"candelabra_quadruple":0,"gcDCQS_mcDSQS_RDSQS_RDCQS":2,"named_families":{"Vos":32,"Long":6,"Raval":34,"Kirtchakov":20,"Ferudun":628},"relevant_hits_beyond_Tan_Zhou":0,"newest_record_seen":"2026-10-17T22:00:30Z"},
"access_holes":["Chang-Zheng-Zhou DCC 2019 body (paywall)","Chang-Zhou JCTA 2013 (ScienceDirect 403, Elsevier API 400)","Tan-Zhou DCC journal Section 4 (paywall)","Xu-Ji 2021/2022 (403), Xu-Ji 2024 (paywall)","Zenodo API and search 403 (DataCite metadata only)","Semantic Scholar rejected; Google Scholar and CNKI not reached","OpenAlex full text abstract-only for recent paywalled works; one HTTP 429","Mills 1990 not read","no host clock; server stamps 2026-10-17T22:35:52Z-22:37:34Z"],
"significance":"specialist answer to an explicit 2025 question via the source's own Construction 2.3; any novelty rests on ingredients I2 and I3",
"counterpoints":["CZZ 2019 may contain FDH(5,8,4,3)","an unindexed thesis or note may contain gcDCQS(8^4:0)","journal Section 4 may differ from arXiv v1"],
"new_vs_prior_gcdcqs20_audit":["Boolean/Meszka exclusion","I1 uniqueness via KKW table","I3 context: CZZ abstract, H(g^5), 3-frames, RDTD(3,4,2)","Zenodo family sweep and DataCite full-text queries for this target","citer counts unchanged (1)"]}
```
