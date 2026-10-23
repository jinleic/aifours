# Priority/status audit: Díaz et al. 2009 Maximum Hypothesis (χ(G_{n,5}) = 3)

All web sources were accessed on 2026-10-17. The audit was read-only: no files were changed and no one was contacted. This screen checks priority only. It does not check the certificate's correctness.

## Summary
- **(a) Has the Maximum Hypothesis been proved, rigorously or by computer?** No proof was found in the bounded screen. Every author who describes the result accurately calls it conditional: Kemkes 2008, Coja-Oghlan–Efthymiou–Hetterich (CEH) 2013, and Ayre–Coja-Oghlan–Greenhill (ACG) arXiv v3/v4 in 2019/2021.
  - **Three sources overstate the result.** Zdeborová–Krzakala 2007 cites "rigorous results". Moore's arXiv v3 (2015) says it "showed … w.h.p.". ACG v1 and v2 (2018-12 and 2019-05) say "a computer-assisted proof yields χ(G(n,5)) = 3".
  - **ACG corrected its own wording in v3** (2019-06-26) to "if a certain optimisation problem attains its maximum … numerical evidence".
- **(b) Has χ(G_{n,5}) = 3 been proved by another method?** None found.
  - Proven bounds are {3,4} (Shi–Wormald; also Kemkes–Pérez-Giménez–Wormald (KPW) Theorem 1).
  - CEH covers large k only. ACG gives lower bounds only.
  - Achlioptas–Moore report (unpublished) that a second-moment argument over balanced 3-colourings cannot work for d=5, even with positive probability.
- **(c) Has the hypothesis been refuted, or the conditional proof found flawed?** Nothing found.
  - The physics predictions (Krzakala–Pagnani–Weigt (KPW04) 2004, Zdeborová–Krzakala (ZK) 2007, ACG (1.7)) all predict χ=3.
  - ZK flags q=3, d=5 as replica-symmetric (RS) **marginal/critical**: c_RS^reg(3)=5.
- **ESA 2005 is the one unresolved priority risk.** Díaz–Grammatikopoulos–Kaporis–Kirousis–Pérez–Sotiropoulos (ESA 2005) has an abstract that reads as unconditional, claiming 3-colourability with positive probability. The full text is paywalled.
  - Kemkes 2008 describes that result as conditional on the same maximum.
  - [INFERENCE] JGT 2009 still calls it a "Hypothesis", which suggests the authors did not regard the ESA computer-aided verification as rigorous. The JGT preprint thanks Grammatikopoulos and Sotiropoulos for the "computer-aided verifications".
- **The closest technique precedent is Shmalo, arXiv 2607.11010 (2026-07-13, unrefereed).** It uses Arb ball arithmetic plus convex duality to certify the global numerical conditions behind the Ising-perceptron capacity bounds. Its design matches the candidate's: certified sweeps over the bulk plus a concavity argument at the maximiser.

## Files
- `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random5reg-colour/README.md:1-95` — frozen contract; §1.4 baseline; candidate log.
- `…/CLAIM.md:205-206` — the lane's novelty caveat.
- `…/sources/diaz2009-3col-preprint.layout.txt` — the Díaz et al. preprint:
  - :6-17 abstract
  - :26 "preliminary version … appeared in [6]"
  - :74-76 the open question
  - :159-165 Hypothesis 1.1 and Theorem 1.1
  - :1841-1851 concavity "numerically confirmed" and the grid
  - :1901-1904 acknowledgement of the computer-aided verifications
  - :1925-1927 reference [6], ESA 2005
- `…/sources/acg-1812.09691v4.txt:68-70` — ACG v4 status sentence (p. 2).
- `…/sources/eulersolve-opg-37656-paper.txt:17,37-44,420-425` and `…/eulersolve-opg-37656.html` — the K5-lift paper (different model) and the EulerSolve paper listing.

## Architecture
1. ESA 2005 claimed the positive-probability result.
2. Kemkes–Wormald CORR 2005-22 and the Kemkes 2008 thesis strengthened it to a.a.s. under the Maximum Hypothesis.
3. JGT 2009 published that version.
4. Later papers cite JGT 2009 (CEH, KPW Advances, Moore, Díaz–Mitsche, ACG, Ben-Shimon–Krivelevich).

The physics line (KPW04, ZK 2007, ACG (1.7)) supplies the prediction. The technique precedents are separate: the Ising perceptron (Huang 2024, Shmalo 2026) and the conditional result in Kemkes's thesis that became the unconditional KPW Advances 2010 theorem.

## Report

### (i) Sources and d=5/q=3 verdicts
| # | Source (version read) | Date | Verbatim quote (≤40 words) | Location | Verdict |
|---|---|---|---|---|---|
| 1 | Díaz et al. JGT 61:157–191 (preprint read; published abstract via Crossref/zbMATH) | 2009 | "Hypothesis 1.1 (Maximum Hypothesis) The four-variable function F (n) has a unique global maximum over its domain at the point (1/9, 1/9, 1/9, 1/9)." / "Theorem 1.1 Under the Maximum Hypothesis, the chromatic number of Gn,5 is a.a.s. 3." | p. 4, layout:159-165 | Conditional |
| 1b | same | 2009 | "The above results leave the main outstanding open question on the chromatic number of low-degree random regular graphs as follows: is the chromatic number of a 5-regular graph a.a.s. 3?" | p. 2, layout:74-76 | Open before the paper |
| 2 | ESA 2005, LNCS 3669:215–225 (abstract only) | 2005 | "We show that uniformly random 5-regular graphs of n vertices are 3-colorable with probability that is positive independently of n." | Springer abstract | Positive probability only, not a.a.s.; rigor unknown |
| 3 | Kemkes PhD thesis, Waterloo (UWSpace PDF) | 2008-09-23 | "Díaz and others [12] have shown that χ(G_{n,5}) = 3 with probability bounded away from 0, provided a certain four-variable function has a unique maximum at a given point in a bounded domain." | Ch. 1, text line 200 ([12] = ESA 2005); Thm 24, p. 52 | Conditional |
| 4 | Shi–Wormald, CPC 16:459–494 (Crossref abstract) | 2007 | "…is a.a.s. restricted to a range of two integer values: {3, 4} for d = 5" | abstract | {3,4} proven |
| 5 | Achlioptas–Moore, RANDOM 2004 (arXiv cond-mat/0407278v1) | 2004-07-11 | "Krząkała, Pagnani and Weigt [8] have conjectured that a random 5-regular graph is w.h.p. 3-colorable. The authors (unpublished) have shown that applying the second moment method to the number of balanced 3-colorings cannot establish this fact" | §7, p. 11 | Open; plain balanced-colouring route fails |
| 6 | Krzakala–Pagnani–Weigt, PRE 70 (cond-mat/0403725v2) | 2004-07-28 | "q = 3, c = 5 \| COL 1RSB \| 0.279 \| 0.037 \| 0.688"; "Both cases are in the COL phase which implies Σ(e = 0) ≥ 0." | stability table (text lines 256-261); §VII.A | Physics prediction: χ=3 |
| 7 | Zdeborová–Krzakala, PRE 76 (arXiv 0704.1269, latest version) | 2007 | "Indeed the 5-regular graphs are 3-colorable [31] (and rigorous results in [13, 14]) and exactly critical since c^reg_RS(3) = 5" | §III, p. 7 ([13] = CORR 2005-22, [14] = ESA 2005) | Prediction χ=3; the "rigorous" wording overstates |
| 8 | KPW, arXiv 0812.2937v1 (the only arXiv version) | 2008-12-15 | "In particular it provides an alternate proof of the results of Shi and Wormald [19, 20] that a.a.s. χ(G_{n,4}) = 3 and χ(G_{n,6}) = 4." | §1, p. 2 | Theorem 1 gives {3,4} for d=5. The Advances 2010 body could not be read; its Crossref references include Díaz et al. |
| 9 | CEH, arXiv 1308.4287v1 (the only version; JCTB body not read) | 2013-08-20 | "…[25] proved that if a certain four-dimensional optimization problem … attains its maximum at a particular point, then χ(G(n, 5)) = 3 w.h.p. Thus, determining χ(G(n, 5)) remains an open problem." | §1.3, pp. 3-4 | Open / conditional |
| 10 | Moore, arXiv 1502.07591v3 (AIHPD version not read) | 2015-03-04 | "another application [23] showed that random 5-regular graphs are 3-colorable with high probability." | §3, text line 65 ([23] = Díaz et al.) | Mischaracterisation |
| 11 | ACG arXiv v1 and v2 | 2018-12-23 / 2019-05-30 | "For the random regular graph a computer-assisted proof yields χ(G(n, 5)) = 3 w.h.p. [17]" | p. 1 | Mischaracterisation, corrected in v3 |
| 12 | ACG arXiv v3 and v4 (Combinatorica 42:617–658 body not read) | 2019-06-26 / 2021-10-19 | "Diaz, Kaporis, Kemkes, Kirousis, Pérez and Wormald [18] showed that χ(G(n, 5)) = 3 w.h.p. if a certain optimisation problem attains its maximum at a specific point, for which they provided numerical evidence." | v4 §1.1, p. 2 | Conditional; the cavity prediction (1.7) with Table 1 d_3=6 implies χ=3 |
| 13 | Frieze–Karoński book (Frieze website PDF, undated) | — | "Shi and Wormald [932], [933] consider the chromatic number of G_{n,r} for small r. In particular they show that w.h.p. χ(G_{n,4}) = 3." | p. 229 | No d=5 statement |

Screened with no d=5 mention:
- Kunisky–Yu 2404.17012
- Bandeira et al. 2008.12237
- Conneryd et al. 2503.17022
- Bennett–Frieze 2301.00085
- 2509.08531 (bisection and max-cut of 5-regular graphs, 2025)
- Janzer–Janzer 2304.12260
- Bapst et al. 1404.5513
- 1611.00814 and 1411.0610 (identified by ID only)
- Harangi 2204.01353v4
- 2009.10483v2
- Nir–Pérez-Giménez 2109.13347v1
- the live EulerSolve paper index

**JGT 2009 published version vs the 2009-10-20 preprint.**
- The published abstract (Crossref and zbMATH) matches the preprint apart from Wiley spelling edits: "provided a certain four‐variable function has a unique maximum at a given point in a bounded domain".
- The 17-item reference list on zbMATH matches the preprint's numbering: [6] ESA 2005, [17] Wormald 1999.
- The Hypothesis 1.1 and Theorem 1.1 text in the published body could not be compared, because Wiley returned 403.

### (ii) Latest dated attestation of open/conditional status
- **Latest read:** ACG arXiv v4, submitted 2021-10-19 (row 12).
- **Latest overall:** the Combinatorica version, online 2021-10-26, issue dated October 2022. Its body is paywalled. Its Springer reference list still contains item 18, Díaz et al. [INFERENCE] The corrected sentence most likely survived.
- **Latest explicit "remains an open problem":** CEH arXiv v1, 2013-08-20.
- None of the 2022–2026 sources checked restates the status either way.

### (iii) Earlier equivalent result
None found. Scope of the search:
- OpenAlex `cites:W4238782258`: 5 works.
- zbMATH "cited in": 5 documents.
- Crossref is-referenced-by: 4.
- OpenAlex `cites:` for ESA 2005: 6 works.
- OpenAlex full-text searches: "locally rainbow"; "random 5-regular" for 2016–2026; "chromatic number"+"5-regular"+"numerical" for 2019–2026.
- arXiv API metadata queries: 5-regular combined with colour terms; "random regular" combined with chromatic/colouring terms.
- Version histories for ACG, CEH, KPW and Moore (DataCite).
- About 15 web searches.
- The Kemkes thesis, the Frieze–Karoński book, and the live EulerSolve index.

ESA 2005's positive-probability claim is the only possible partial precedent. It is weaker than a.a.s. and its rigor is unverified.

### (iv) Access holes
- **Bodies not readable:**
  - JGT 2009 (Wiley 403)
  - ESA 2005 (Springer paywall; the preview PDF could not be converted)
  - KPW Advances 2010 and CEH JCTB 2016 (Elsevier 403)
  - ACG Combinatorica 2022 (paywall)
  - Moore AIHPD (EMS 404)
  - Díaz–Mitsche, Comput. Sci. Rev. 2010
  - Yilun Shang, Disc. Math. 2025
- **PDF text extraction failed:** Waterloo CORR 2005-22 (Kemkes–Wormald) and CORR 2004-24.
- **Citation indices:** the Semantic Scholar API rejected every URL form I tried; Google Scholar returned 403. A search snippet gives Google Scholar "Cited by 11", so about 6 citing items were not enumerated.
- **Not located or read:** Ben-Shimon–Krivelevich 2009, the theses of Hetterich and Pérez-Giménez, MathOverflow answer 265746, and Zenodo (API 403).

### Technique precedents (item 4)
- **Shmalo 2026 (arXiv 2607.11010v1):** "Previous work established matching conditional lower and upper bounds, subject respectively to a one-variable global sign condition of Ding--Sun and a two-variable global sign condition of Huang. We rigorously verify both conditions using Arb ball arithmetic." Also: "Convex duality and certified adaptive sweeps control its bulk, while a ray-concavity argument treats the degenerate maximizer." This is the same proof architecture as the candidate, in a lower-dimensional problem.
- **Huang 2024 (arXiv 2404.18902v2):** "Claim 2.6 is verified numerically for κ = 0 using rigorous interval arithmetic" (§2, p. 11), done with python-flint. The global maximum, Condition 1.3, is left as an assumption.
- **Aubin–Perkins–Zdeborová (arXiv 1901.00314):** "a proof, subject to a numerical hypothesis, of a formula for the storage capacity" (§I).
- **Galanis–Štefankovič–Vigoda (arXiv 1305.2902v3):** "For odd q, we are unable to establish whether the dominant phases are supported on vectors with two or three different entries" (§1.2.3). This is an analytic open case, not computer-assisted.
- **Kemkes thesis to KPW Advances 2010:** the thesis result "provided a certain second moment condition holds" later became an unconditional analytic theorem.
- **EulerSolve OPG-37656 (2026-10-17, unrefereed, AI-assisted):** proves the unique global maximum analytically for degree-4 lifts of K5. Different model; nothing from it is used.

### (v) Significance
- **If the certificate survives hostile review,** it turns a 2009 conditional theorem into an unconditional one. That closes the question Díaz et al. called "the main outstanding open question" for low-degree random regular graphs, and that CEH 2013 listed as open.
- **What changes:**
  - The q=3 picture becomes complete: χ=3 for d≤5 and >3 for d≥6. The d=3 case comes from Brooks' theorem; the d=4 case from Shi–Wormald.
  - It confirms the 1RSB cavity prediction at the point ZK call RS-marginal.
  - [INFERENCE] It also removes the confusion that ACG v1/v2, Moore and ZK created by implying the result was already proved.
- **Who would care:** researchers on random graph colouring and random constraint-satisfaction problems (the Wormald and Coja-Oghlan groups, Greenhill), and statistical physicists working on q-colouring.
- **Calibration:**
  - The reduction and the conditional theorem belong to Díaz et al.
  - The certified-numerics method closely follows Huang 2024 and Shmalo 2026.
  - I would classify it as a potentially substantive specialist resolution of an explicit open problem, not a new method.
  - Its value also depends on the paper's own steps that do not use the hypothesis: the Lemma 5.7 rank, the Lemma 5.8 Hessian, and §6.
- **Before any priority wording:** read the ESA 2005 full text.
