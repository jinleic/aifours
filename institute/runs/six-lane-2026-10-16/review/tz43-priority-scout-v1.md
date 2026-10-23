<!-- Parent transcription 2026-10-17T23:04:45-07:00 of the read-only scout Tz43Priority's final report (agent://Tz43Priority; transcript history://Tz43Priority), verbatim below. The scout wrote no files and had no host clock; its time base is the server stamps it quotes. -->

NONE-FOUND-IN-SCOPE

I found no earlier gcDCQS(18⁴:2), no FDH(5,18,4,3) (= FDGDD(3,4,5{18})), no mcDSQS(74) and no mcDSQS(18·4ⁿ+2) family. Nothing I could read lets either object be derived from published work. The main hole is still open: I could read only the first page (p. 1415) of Chang–Zheng–Zhou 2019 (CZZ). A miss here is not proof of novelty.

**How the screen was run.** No files were written and no reviewer CLI was run, as the task specified. I had no shell, so there is no host clock reading. Server timestamps: arXiv API 2026-10-18T05:43:48Z to 06:01:34Z (22:43–23:01 PDT on the 17th); Springer metrics 2026-10-18 05:34:12 UTC; newest DataCite record seen 05:28:20Z. Candidate hashes are the ones recorded in the lane README (A `1382d572…282e`, B `3e22f502…a998`, mcDSQS74 ASCII v2 `1122f1f4…eb4c`); I did not recompute them.

## Evidence
| # | Source (date) | Quote (≤40 words) / datum | Bearing |
|---|---|---|---|
| 1 | CZZ, DCC 87:1415–1431, online 2018-08-21. Abstract: https://link.springer.com/article/10.1007/s10623-018-0536-8 | "Related recursive constructions are established and direct constructions for FDH(v, 2, 4, 3)s are displayed by using automorphism groups." Its definition of FDH is the same as Tan–Zhou's FDGDD. | The only direct constructions mentioned have group size 2. |
| 2 | CZZ p. 1415, Springer's free page-one preview (https://page-one.springer.com/pdf/preview/10.1007/s10623-018-0536-8), rendered through the Google Docs viewer | Received 2018-05-16, accepted 2018-08-09; keywords "Generalized frame · … · t-wise balanced design". The page holds only the abstract and the start of the introduction. | No theorems are visible. |
| 3 | CZZ citers | OpenAlex 6, zbMATH 6, Crossref 6, OpenCitations 5, Springer/Dimensions 8. They are Xu–Ji 2021/2022/2024, Liu–Lei 2023 and Tan–Zhou 2025/2026. zbMATH Zbl 1411.05037 has the abstract only. | — |
| 4 | Liu–Lei, arXiv 2210.06214v2, LF456 | "Lemma 4.3. [5] There exists an RDSQS(2v) for v ∈ {23, 29, 41, 47, 53, 59, 71, 83}." | This is their only use of CZZ. [INFERENCE] These come from FDH(v,2,4,3) with every v ≡ 2 (mod 3). |
| 5 | Tan–Zhou arXiv 2503.11934; only v1 exists (2025-03-15) | §4(3), LF1114–1116: "Construct a gcDCQS(18⁴ : 2) and an FDGDD(3, 4, 5{18}) or RDGDD(3, 4, 5{18}). By Construction 2.2 or 2.3 and Lemma 3.8, the existence of an mcDSQS(18·4ⁿ+2) would be obtained…" CZZ is cited only at LF131: "There is a large literature studying RDSQSs [2, 3, 11, 23]". | Zhou, a CZZ coauthor, still posed (B) as open in 2025. Their "smallest unknown mcDSQS(6n+2)" is 38 (LF1108–1110), so 74 was unknown to them. |
| 6 | Tan–Zhou journal version, DCC 93(10):4117–4140 (received 2025-01-24, revised 05-28, online 06-23) | The zbMATH summary (Zbl 1575.05024) matches the arXiv abstract: "an RDSQS(2^{2m+1}+2) and an mcDSQS(2·9^m+2) are proved to exist". Its 24 references are the arXiv list minus Hartman 1994. | No sign that §4(3) was answered. Cited by: Crossref 1, OpenAlex 1 (Tilings, DCC 94 #124), zbMATH 1, Springer 2, OpenCitations 0. |
| 7 | Ji, JCD 27 (2019) 75–81 (Zbl 1407.05043) | "…necessary and sufficient conditions … are m≥4, mg≡0 (mod 2), and g(m−1)(m−2)≡0 (mod 3), with a definite exception (m,g)=(5,2)." | FDH(5,2,4,3) cannot exist. |
| 8 | Ji, JCD 17 (2009) 25–35 (Zbl 1197.05023) | "for m=5, an H(5,g,4,3) exists if g is divisible by 4 or 6 [Mills 1990] … if g is even, g≠2 and g≢10,26 (mod 48)." | Plain H(6⁵) and H(18⁵) have been known since Mills 1990. Correction: the earlier screen credited this to Zhang–Ge 2013. That paper (DCC 69, Zbl 1268.05030) gives "a new existence proof for H-designs of type 2ⁿ". |
| 9 | Zhang–Ge, DCC 57 (2010); their RH paper, p. 84 | "(1, α)-resolvable, if its block set can be partitioned into α-parallel classes." Their H-frame HF(q,g,k,t) is an H-design with holes. | These constrain the block resolution, not derived Kirkman frames. Irrelevant here. |
| 10 | Muse–Phelps, JCTA 104 (2003) (Zbl 1031.05025); Teirlinck, DCC 4 (1994) | "provide a new construction of 3-frames F(3,4,n{2})" | Group size 2 only. |
| 11 | Stinson 1987, as quoted in arXiv 2404.06066v1 Thm 3.2 | "There is a Kirkman frame of type gᵘ if and only if u ⩾ 4" (plus g even, g(u−1) ≡ 0 mod 3) | KF(m³) never exists, so FDH(4,m,4,3) is impossible. |
| 12 | Tan–Zhou Thm 2.5(2), LF682–683 | "There is an RDTD(3, 4, m) for … gcd(m, 4) ≠ 2 and gcd(m, 18) ≠ 3." | m = 3 is not covered. The zero-sum RDTD(3,4,3) exists anyway (lane `fcdb4285…`). |
| 13 | Liu–Lei Lemma 2.2 | "there exists a TD(3, 4, 3) on A × Z3 … We can check that the derived design of the GDD at every point is resolvable." | The method "weight by Z₃, then compute the resolutions" is already published, for type 3⁸. |
| 14 | DataCite, single-phrase queries | mcDSQS: 1 hit (Tan–Zhou). gcDCQS: 0. "candelabra quadruple": 0. "Kirkman frame": 1 (Dukes–Lamken). FDGDD/RDGDD/RDSQS/RDCQS/LKTS: only Wang, Tan–Zhou, Liu–Lei, 1307.3019 relevant. Newest "Steiner quadruple" records: Alesandroni et al. (2026-09-29), Liu–Feng symmetric cyclic SQS (2026-09-20). | Nothing relevant. Queries combining several quoted phrases with OR returned junk, so I re-ran them one phrase at a time. |
| 15 | Zenodo creator families, through DataCite | Kirtchakov 20 records (newest 08-14), Griffin Long 6 (10-15), Vos 32 (10-10), Raval 34 (09-11), Ferudun 652 (10-18T05:28Z), Gippini Requeijo 52 (10-17T22:26Z), Sadhu (common surname; 9 title-filtered hits, none relevant). | No record on SQS, candelabra systems, H-designs or Kirkman frames. |
| 16 | arXiv | The newest math.CO listing (Fri 16 Oct 2026, 87 entries) and the past week's titles: nothing relevant. API keyword search, newest hit 2610.18666: nothing relevant. Chromatic index plus Steiner: only Tan–Zhou. | — |
| 17 | OpenAlex and GitHub | "Steiner quadruple" since 2025-03: 28 works, none relevant. "Kirkman frame(s)" since 2018: 4 works (Stinson's survey has no FDH). Shi–Xia–Krotov's 5 citers and Tan's 6 works contain no follow-up. GitHub: "mcDSQS" finds 0 repositories. | — |

## Derivability (Q4), with the exact theorems
- **Inflating a frame-derived H-design.** [INFERENCE, routine] An FDH(5,g,4,3) plus an RDTD(3,4,m) gives an FDH(5,gm,4,3). To get group size 18 with g even, g must be 2, 6 or 18.
  - g = 2 is excluded by Ji 2019.
  - g = 6 needs an FDH(5,6,4,3), and I found none. CZZ's abstract mentions only g = 2. The lane's symmetric searches for this seed were UNSAT or UNKNOWN; that is not a nonexistence proof.
  - So (B) would become derivable only if an FDH(5,6,4,3) exists in some text I could not read.
- **Inflating a plain H(6⁵).** Mills' H(6⁵) plus RDTD(3,4,3) gives only a plain H(18⁵). The frame argument needs frames in the master design. The worker's master has 1, 1, 0 and 1 perfect matchings in its four missing-group families at point 0, and no 3-class decomposition (`master-nonframe-diagnosis-v1.json`). The 36 classes at each of the 90 points were found by SAT. This step is not routine.
- **Fundamental (master-design) construction.** Blocks of size 4 would need a KF(m³), which does not exist. So the master must be an OA(3,5,h) with h·m = 18 and m even.
  - (h,m) = (9,2) fails because FDH(5,2,4,3) does not exist.
  - (3,6) fails because an OA(3,5,3) does not exist (Bush bound: an index-1 OA with s ≤ t has at most t+1 columns).
  - (1,18) is circular.
- **3-frames and H-frames.** 3-frames are known only for group size 2. H-frames are holey H-designs, a different property.
- **The RDGDD alternative.** I found no RDGDD(3,4,5{6}) or RDGDD(3,4,5{18}). The published examples are 10{2} (Tan–Zhou), and types 3⁸ and 3¹⁴ (Liu–Lei).
- **gcDCQS(18⁴:2).** The notion was defined in 2025. The lane's Lemma R (written, not reviewed) argues that no Tan–Zhou recursion produces it.
- **The family 18·4ⁿ+2.** For n ≥ 1 it does not overlap the published 2·9ᵐ+2 family, since equality would force n = 0.
- **mcDSQS orders known before this run.** Published: 20, 26, 32 and 2·9ᵐ+2. This run's 38, 62, 80 and 128 are internal and unpublished.

## Access holes
- **CZZ pp. 1416–1431.**
  - Paywalled; MathSciNet MR3947353 not read.
  - No preprint or repository copy: no arXiv version, and OpenAlex reports no repository full text.
  - Search and mirror routes failed: Google Scholar 403, CORE 403, BASE bot wall, Semantic Scholar URLs rejected by the tool, r.jina.ai 401.
  - Hao Zheng's thesis and CNKI not reached.
- **Chang–Zhou JCTA 2013.** ScienceDirect 403, Elsevier API 400. Any RDGDD or FDGDD(3,4,5{6}) lemma there is unchecked.
- **Xu–Ji 2021/2022/2024.** Read only through the citation indexes.
- **§4 of the Tan–Zhou journal version.** Paywalled.
- **Zenodo files.** Zenodo search returns 403, so only DataCite metadata was checked.
- **Records after about 06:00Z** are outside this screen.

## Significance
**Potentially substantive specialist work, not yet established.**
- The pair answers an explicitly posed open problem from 2025.
- If the parent check of the certificates and the hostile review of the Construction 2.3 + 2.1 + Lemma 3.8 bridge both pass (the bridge also needs a gcDSQS(20,2)), it gives mcDSQS(74) and an infinite mcDSQS(6n+2) family distinct from Tan–Zhou's 2·9ᵐ+2.
- The methods are standard: prescribed-automorphism search and Z₃ weighting.
- The finite objects alone are a modest extension.
- This is not a major result.

## Recommended wording (no "first")
"Tan and Zhou (arXiv:2503.11934v1 §4(3); DCC 93 (2025) 4117–4140) asked for a gcDCQS(18⁴:2) together with an FDGDD(3,4,5{18}) or RDGDD(3,4,5{18}). We give explicit certificates for a gcDCQS(18⁴:2) and an FDGDD(3,4,5{18}), i.e. an FDH(5,18,4,3) in the sense of Chang–Zheng–Zhou (2019), each checked against the definitions [parent verdict]. The FDGDD comes from inflating an H(5,6,4,3) (such designs exist by Mills 1990), which is not itself frame-derived, by the zero-sum TD(3,4,3), and then computing Kirkman frames for the inflated derived designs. A bounded screen on 17 Oct 2026 found no earlier construction of these objects, of an mcDSQS(74), or of an mcDSQS(18·4ⁿ+2) family, and no route to them from published FDH or RDGDD results. The bodies of Chang–Zheng–Zhou (2019) and Chang–Zhou (2013), and §4 of the journal version, were not accessible. Subject to the separate bridge review, Constructions 2.3 and 2.1 with Lemma 3.8 then give an mcDSQS(18·4ⁿ+2) for every n ≥ 1."

Avoid "first", "new class of FDH designs", "solves FDH(5,g)", and stating the family as proven before the bridge review.
