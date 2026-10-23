**RDSQS(52) audit: no earlier construction or impossibility proof located; the problem was still open as of 2025–2026**

Before 2026‑10‑17, the screen found no construction of an RDSQS(52) and no proof that one cannot exist. A search miss does not establish novelty.

## Summary

- **Latest explicit open statement.** Tan–Zhou, arXiv:2503.11934v1 (15 Mar 2025; the only arXiv version), §4(1), PDF p.19, call RDSQS(52) "the smallest unknown RDSQS(6n+4)". The journal version was revised after the preprint, and its §4 wording is paywalled and unverified.
- **Later implicit statement by the same authors.** arXiv:2512.22754v1 (28 Dec 2025, only version), Theorem 2.8(2), still excludes a ∈ {51, 69, 75}. The authors say this theorem is not a complete list: it only combines tripling with known small orders.
- **Wider conjecture.** Shi–Xia–Krotov (JCTA 2023) conjecture that an RDSQS(n) exists for every n ≡ 4 (mod 6).
- **Known orders up to 100**, recomputed from the stated families: 4, 10, 16, 22, 28, 34, 40, 46, 58, 64, 82, 88, 94, 100. The gaps are exactly 52, 70 and 76, matching the excluded 51, 69, 75. No source states this list word for word, and none names 70 or 76 as open.
- **Why recursion cannot reach the gaps.** 51 = 3·17, 69 = 3·23 and 75 = 3·5². None can be written as a product of factors that are all ≡ 3 (mod 6). So no product or tripling construction reaches them; they need a direct construction.

## Files

- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`
  - :78-89 — definitions of derived design and RDSQS(v); Theorem 1.1; the condition v ≡ 4 (mod 6).
  - :128-134 — mcDSQS equals RDSQS when v ≡ 4 (mod 6).
  - :176-189 — Theorem 1.3 and Corollary 1.4 (the alphabet-size results).
  - :891-907 — Theorem 3.2 (the RDSQS(2^(2m+1)+2) family, including 34) and Lemma 3.4 (cyclic computer construction).
  - :1094-1117 — the open-problems section.
- `.../sources/liu-lei-2210.06214.txt`
  - :58-68 — where the RDSQS notion is attributed; their Theorem 1.1.
  - :184 — RDSQS(22).
  - :229-236 — RDSQS(3·7^n+1), RDSQS(3·13^n+1); RDSQS(40) attributed to their ref [22].
  - :243 — definition of RDSQS*(v).
  - :449-461 — Lemmas 4.1–4.3 and Theorem 4.4.
- `.../sources/wang-2607.21521.txt:54-71,558-559` — Table 1 of direct LKTS constructions (51, 75: Denniston 1979; 69: Zheng–Chang–Zhou 2016); citation of Tan–Zhou.
- `.../sources/xu-ji-2024-publisher.txt:111` — OLKTS⁺ abstract.
- `.../sources/tan-zhou-2026-tilings-publisher.txt:207-211,323,361,393,405,413-417` — the published reference list keeps every Theorem 2.8 citation under the same numbers.
- `institute/runs/six-lane-2026-10-16/screening/math-finite-target-screen.md:5-101` — earlier parent screen. Its conclusions agree with this audit; corrections are listed at the end.

## Architecture

- **RDSQS(v+1) → OLKTS(v).** This follows directly from the definitions; the proof is in section C.
- **RDSQS(v+1) → LKTS(3v).** Tan–Zhou Theorem 1.1, citing Chang–Zhou 2013 and Yuan–Kang 2008. Xu–Ji 2024 show a weaker object, OLKTS⁺(v), gives the same result.
- **Products.** An RDSQS(u+1) and an RDSQS(v+1) give an RDSQS(uv+1) (Liu–Lei Lemma 4.1). Taking u = 3, i.e. the trivial RDSQS(4), gives tripling: RDSQS(v+1) → RDSQS(3^m·v+1) → OLKTS(3^m·v).
- **Codes.** By Shi–Xia–Krotov Theorem 5 (Tan–Zhou Theorem 1.3), q₀′(3,4,n) = min over SQS(n) of max χ′(derived STS) + 1. Here q₀′ is the smallest alphabet size for the diameter-perfect codes in question, and χ′ is the chromatic index. So an RDSQS(n) gives q₀′(3,4,n) = n/2.
- **Tilings.** An OLKTS(n) with n ≡ 9 (mod 12) gives a TOC₃(n+1,5,3), a tiling by optimal ternary constant-weight codes (tilings Corollary 4.10(2)).
- **2-resolvable SQS ⇒ RDSQS** (stated by Shi–Xia–Krotov and Liu–Lei).

## Report

### A. Sources table

All checked 2026‑10‑17.

| # | Source | Version/date | Quote (≤40 words) | Location | Verdict for v=52 |
|---|---|---|---|---|---|
| 1 | Tan–Zhou, [arXiv:2503.11934](https://arxiv.org/abs/2503.11934v1) | v1 only: submitted 2025‑03‑15T00:56Z. DataCite lists only v1 (metadata updated 03‑18). `/abs/…v2` returns HTTP 404. | "Find more examples of mcDSQS(v)s, for example, an mcDSQS(38) and an RDSQS(52) (the smallest unknown mcDSQS(6n + 2)s and the smallest unknown RDSQS(6n + 4)s, respectively)." | §4(1), PDF p.19 | **Explicitly open** (latest explicit) |
| 2 | Same paper, [DCC 93:4117–4140](https://doi.org/10.1007/s10623-025-01677-x) | Received 2025‑01‑24, revised 05‑28, accepted 06‑13, online 06‑23, issue Oct 2025 | Abstract: "an RDSQS(2^{2m+1}+2) and an mcDSQS(2·9^m+2) are proved to exist" | Springer abstract page. Reference list is the arXiv list minus Hartman 1994. | No claim visible; body paywalled, §4 unverified |
| 3 | Tan–Zhou, [arXiv:2512.22754v1](https://arxiv.org/pdf/2512.22754v1) (tilings paper) | v1 only, 2025‑12‑28 | "For any positive integer a ≡ 3 (mod 6) and a < 100, there exist (1) an LKTS(3^m · a) if a ∉ {57, 87, 93} and (2) an OLKTS(3^m · a) if a ∉ {51, 69, 75}." | Theorem 2.8, §2.2, p.6 | **Implicitly open.** Scope caveat in the same paper: "we omit a comprehensive list of the results about LKTSs and OLKTSs" |
| 4 | Same paper, [DCC 94, art. 124](https://doi.org/10.1007/s10623-026-01853-7) | Online 2026‑06‑02 | — | All nine Theorem 2.8 citations kept under the same numbers | No claim visible. [INFERENCE] Theorem 2.8 retained. |
| 5 | Shi–Xia–Krotov, [arXiv:2212.00048v2](https://arxiv.org/pdf/2212.00048v2); JCTA 200 (2023) 105790 | v2 2023‑07‑31 | "Conjecture 1. If n ≡ 4 mod 6, then there is an SQS(n) such that all its derived STS are resolvable." / "Up to now, we only know that the conjecture is true for n = 10 and in the cases when 2-resolvable SQS(n) are known to exist" | §5, p.21. Keevash remark in §4.1, p.13. | General conjecture; 52 not in their known list. Their list omits the RDSQS orders from the LKTS literature. |
| 6 | Liu–Lei, [arXiv:2210.06214v2](https://arxiv.org/pdf/2210.06214v2); DCC 91 (2023) | 2023‑02‑12 | "Then there exists an RDSQS(v + 1) and an LKTS(3v) where v is the product of some elements in L." | Theorem 4.4, p.9 | The families miss 52 (my derivation, section B) |
| 7 | Xu–Ji, [DCC 92:2267–2285](https://doi.org/10.1007/s10623-024-01386-x) | Received 2022‑09‑26, online 2024‑04‑05 | "an RDSQS(v+1) is reduced to an overlarge set of Kirkman triple systems of order v with an additional property (OLKTS+(v)), which plays the same role in constructing an LKTS(3v) as an RDSQS(v+1)." | Abstract | No RDSQS(52) in abstract; body paywalled |
| 8 | Wang, [arXiv:2607.21521v1](https://arxiv.org/abs/2607.21521v1) | 2026‑07‑23 | Table 1 row: "51, 75, 105, 129 Denniston [4] 1979" | Table 1; ref [16] | No RDSQS(52) statement. LKTS(51) and LKTS(75) are known. |
| 9 | Yuan–Kang, [Acta Math. Sin. 25:419–434](https://doi.org/10.1007/s10114-008-6615-4) | Online 2009‑02‑18 | "There exists an OLKTS(6u + 3) for u = 2^{2n−1} − 1, 7^n, 31^n, 127^n, 4^r 25^s, where n ≥ 1, r + s ≥ 1." | Abstract. Superscripts are flattened on the page; this is my reading. | No RDSQS(52). Includes **OLKTS(153)** (u=25); excludes 51, 69, 75 (u = 8, 11, 12). |
| 10 | Yuan–Kang, Discrete Math. 309 (2009) 975–981 | — | "under certain conditions, an OLKTS of order v can be used to produce an OLKTS of order 3v" | [zbMATH review by Colbourn](https://zbmath.org/?q=an:1162.05009); body blocked (403) | Shows OLKTS-only tripling is conditional |
| 11 | Yuan–Kang, Discrete Math. 310 (2010) 2119–2125 | — | "some new existence results of OLKTS(v) with a special properties are obtained" | [zbMATH summary](https://zbmath.org/?q=an:1219.05020); body blocked | Cited as the source of RDSQS tripling (tilings ref [61]) and of the product rule (Liu–Lei ref [23]) |
| 12 | Yuan–Kang, [DCC 48:35–42](https://doi.org/10.1007/s10623-008-9168-8) | 2008 | "we give a new construction for LKTS(6v + 3) via OLKTS(2v + 1) with a special property" | Abstract | Earliest root of the RDSQS ⇒ LKTS link; no 52 |
| 13 | Chang–Zhou, JCTA 120 (2013) 649–670 | — | Liu–Lei (p.2) say the RDSQS notion is used in [4] (this survey), with the LKTS application restated from Yuan–Kang 2008. | [zbMATH summary](https://zbmath.org/?q=an:1259.05024); body blocked | Unknown. [INFERENCE] none here, since Zhou later called 52 unknown. |
| 14 | Chang–Zheng–Zhou, DCC 87 (2019) | — | "There exists an RDSQS(2v) for v ∈ {23, 29, 41, 47, 53, 59, 71, 83}." | Via Liu–Lei Lemma 4.3 | 52 would need v = 26: not listed |
| 15 | Tilings Theorem 2.7 (Baker 1976; Teirlinck 1994) | Dec 2025 | "There exists a 2-resolvable SQS(n) if n = 4^m or n = 2p^m + 2 with p ∈ {7, 31, 127} for any positive integer m." | p.5 | For 52, p^m = 25: not covered |
| 16 | Kiermaier–Krčadinac–Wassermann arXiv:2509.23483v1; Rosin arXiv:2505.23881v1; Etzion–Tan–Zhou arXiv:2510.24132v1; Tan–Zhou–Etzion arXiv:2602.16319v1; Liu–Feng Zenodo 10.5281/zenodo.22852801 (2026‑09‑20) | 2025–26 | — | Text searches; Zenodo item is metadata only | No RDSQS content |

### B. Known RDSQS orders (latest statements, recomputed)

What the latest sources actually state:
- **Tan–Zhou 2025:** their new family RDSQS(2^(2m+1)+2), and 52 as the smallest unknown. Together these imply every order below 52 is known: {4, 10, 16, 22, 28, 34, 40, 46}.
- **Liu–Lei Theorem 4.4:** RDSQS(v+1) whenever v is a product of elements of
  L = {7·4^n − 1 : n ≥ 1} ∪ {3·7^n} ∪ {3·13^n} ∪ {4^m·25^n − 1 : m ≥ 1} ∪ {4·7^n − 1} ∪ {2q^n + 1 : q ≡ 7 (mod 12), q a prime power} ∪ {45, 57, 81, 93, 105, 117, 141, 165}.

Order-by-order check up to 100 (my recomputation):

| v | Source |
|---|---|
| 4, 10 | Trivial; SQS(10) (Tan–Zhou proof of Theorem 3.2) |
| 16, 64 | 2-resolvable Boolean SQS (Baker); also 63 ∈ L |
| 22 | Liu–Lei Lemma 2.5 |
| 28 | Liu–Lei Theorem 3.3; also 27 = 3·9 |
| 34 | Tan–Zhou Theorem 3.2 |
| 40 | 39 = 2·19+1 ∈ L |
| 46 | 45 = 3·15; also CZZ with v = 23 |
| 58, 94 | CZZ with v = 29, 47 |
| 82 | 81 = 3⁴ |
| 88 | 87 = 2·43+1 |
| 100 | 2·7²+2 (2-resolvable), or 99 ∈ L |
| **52, 70, 76** | **Gaps** |

The gaps are also missed by every other route:
- 4v route: needs an RDSQS*(13) or RDSQS*(19), which cannot exist (an SQS of odd order does not exist); 70 is not divisible by 4.
- FDH doubling: no CZZ entry for v = 26, 35 or 38.
- 2-resolvable: would need p^m = 25 or 37 with p ∈ {7, 31, 127}; and 70 ≡ 10 (mod 12) cannot be 2-resolvable at all.

The tilings exceptions 51, 69, 75 match these gaps exactly. [INFERENCE] the tilings paper used the same set of known orders.

### C. Your scope item (1): where RDSQS ⇒ OLKTS is stated, and tripling

- **No numbered theorem found** in any text I could open.
  - Tilings §2.2, p.6, states it uncited: "An RDSQS(n + 1) is a Steiner quadruple system SQS(n+1) whose derived designs are resolvable at all points, meaning that an RDSQS(n+1) gives an OLKTS(n). A tripling construction states that an RDSQS(n+1) yields an RDSQS(3n+1) [61]."
  - Xu–Ji 2024 state it in the stronger OLKTS⁺ form.
  - The likely original sources (Yuan–Kang 2008/2010, Chang–Zhou 2013) are blocked, so their theorem numbers are unverified.
- **Hypotheses: none beyond the definition.** In an SQS(v+1) on X, each triple T lies in exactly one block B, so T belongs to exactly one derived design B_x, namely x = B∖T. Hence the B_x for x ∈ X partition all triples of X, and each B_x is a KTS(v) by assumption. That is an OLKTS(v).
- **Tripling: yes.** Liu–Lei Lemma 4.1 ("If there exists an RDSQS(u + 1) and an RDSQS(v + 1), then there exists an RDSQS(uv + 1)") with u = 3 gives RDSQS(3^m·v+1), hence OLKTS(3^m·v) for every m ≥ 0. That is the shape of tilings Theorem 2.8(2).
- **Caution:** tripling an OLKTS directly works only "under certain conditions" (Yuan–Kang 2009). An OLKTS(51) alone is therefore not known to give OLKTS(153).

### D. Your scope item (2): 70/76 and OLKTS(51/69/75)

- **RDSQS(70) and RDSQS(76):** not stated open anywhere I found. They appear only implicitly, through tilings Theorem 2.8(2) and Theorem 4.11 ("a TOC₃(3^m a + 1, 5, 3) if a ∉ {51, 69, 75}"), and generically through the Shi–Xia–Krotov conjecture.
  - The 14-order list you gave is not stated verbatim anywhere. It is derivable as in section B.
  - 52 and 76 are ≡ 4 (mod 12). Keevash's theory, as reported by Shi–Xia–Krotov, covers only "n large enough" in that class: "for given w and n large enough, 2-resolvable S(3, w, n) systems exist if some divisibility conditions are satisfied. In particular, for w = 4, those conditions are equivalent to n ≡ 4 mod 12." I did not check the theorem in [Keevash 2018](https://arxiv.org/abs/1802.05900) myself.
- **OLKTS(51), OLKTS(69), OLKTS(75):** no source I could open shows any of them known.
  - Yuan–Kang 2009's family misses them, but it does claim OLKTS(153). So tilings Theorem 2.8(2) is not a full status list, and the m = 1 case for a = 51 may already be known.
  - Xu–Ji 2022 ("new infinite families of … overlarge sets"), Xu–Ji 2024, Zhou–Chang 2014 ("A new result on overlarge sets … is also produced") and Chang–Zhou 2013 could not be read, so other routes are not ruled out.
  - Yuan–Kang 2009 also reduce the whole OLKTS spectrum to a finite list of small designs. That reduction is conditional.

### E. Earlier equivalent and search scope

None found within this scope:
- **arXiv API:**
  - `all:RDSQS` (2 hits); `mcDSQS` / "minimum colorable".
  - Kirkman, "quadruple systems" and "diameter perfect", each since 2025‑03.
  - Author searches: Zhou Junling (18), Lei Jianguo / Ji Lijun (2).
- **Full-text searches:** 2512.22754, 2212.00048, 2509.23483, 2505.23881, 2510.24132, 2602.16319, plus the local Tan–Zhou, Liu–Lei, Wang and Wang–Shi texts.
- **OpenAlex:**
  - `cites:W4411559024` → 1 (the tilings journal paper).
  - Papers since 2023‑06 citing 8 core RDSQS/OLKTS works → 7.
  - Full text "resolvable derived designs" → 6.
  - Full text RDSQS → 93 (3 relevant).
  - Titles with "quadruple systems" or Kirkman since 2024.
  - Yuli Tan's works (6).
- **Citation and version databases:** Crossref (cited-by count 1; Springer shows "2 Citations", the second unidentified); OpenCitations 0; DataCite.
- **zbMATH:** 10 entries.
- **Springer abstract pages:** 7.
- **web_search:** 4 queries, used as leads only.

### F. Access holes

- **Springer paywall:** Tan–Zhou journal body; tilings journal body; Xu–Ji 2024; CZZ 2019; Yuan–Kang 2008 and 2009 bodies.
- **ScienceDirect/Elsevier (403):** Chang–Zhou 2013; Yuan–Kang 2009 and 2010; Zhou–Chang 2014; Xu–Ji 2021 and 2022. The open-access PDF links also return 403.
- **Semantic Scholar:** the reader rejected the API URLs.
- **Other blocks:** IA Scholar asks for an anti-bot check (not bypassed); CORE and the Zenodo API return 403.
- **Not searched:** Google Scholar, MathSciNet, CNKI or Chinese theses (e.g. the Yuan 2007 dissertation and Beijing Jiaotong theses), the CRC Handbook.
- **Residual risk:** possible unpublished or thesis work by the Tan–Zhou group.

### G. Calibrated significance

"Major" here means one of: a new method, a long-standing prominent problem, a large gain over the state of the art, or a broad consequence.

- **RDSQS(52) is a short specialist answer to an explicit 2025 open question. It is not major.** If the certificate verifies:
  - It is the smallest open case of Tan–Zhou §4(1) and of the Shi–Xia–Krotov conjecture.
  - [INFERENCE] 52 has only been the smallest open order since Tan–Zhou constructed RDSQS(34) in 2025.
  - It is equivalent to q₀′(3,4,52) = 26 (Corollary 1.4(2), with the converse following from Theorem 1.3).
  - It gives OLKTS(51) and, via tripling, OLKTS(3^m·51). The m = 1 case may already be known from Yuan–Kang 2009.
  - It gives TOC₃(3^m·51+1, 5, 3) for odd m.
  - By the product rule it gives further RDSQS orders such as 154, 460 and 766. These are not covered by any family I located.
  - It gives no LKTS gain: LKTS(51) is known (Denniston 1979), so LKTS(153) follows by tripling.
  - The method matches the source's own technique: Tan–Zhou Lemma 3.4: "We construct a cyclic mcDSQS(v) on Zv for v = 26, 32; the base blocks and the resolutions are listed in Appendix B."
- **Your exploratory RDSQS(76), if verified,** would give the same kind of result:
  - q₀′(3,4,76) = 38.
  - OLKTS(75) and OLKTS(3^m·75), including OLKTS(225), which is not in Yuan–Kang 2009's family.
  - TOC₃(226, 5, 3).
  - No LKTS gain (LKTS(75) is known from Denniston 1979).

### H. Corrections to the earlier parent screen

- 2510.24132 and 2602.16319 show no citation of Tan–Zhou 2025 in their extracted text.
- Shi–Xia–Krotov's 2023 conjecture is an additional, generic open statement that the screen missed.
- Yuan–Kang 2009's OLKTS(153) means tilings Theorem 2.8(2) should not be read as saying OLKTS(153) is open.

**Checks you may want to run:** if anyone gets institutional access, read Tan–Zhou journal §4, Xu–Ji 2022 and 2024, and the Yuan–Kang 2009 bodies. Those are the remaining places where an earlier result could be hiding.
