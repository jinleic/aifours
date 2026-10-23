# Finite mathematics replacement screen — 2026-10-16 PT

Read-only scout report; screening evidence, not proof of openness or novelty.

**Recommendation: RDSQS(52) is the strongest target. The two alternatives are mcDSQS(38) and RoSQS(56).** All three were open in their latest primary sources, I found no claim of a solution, and none appears in openai/math or EulerSolve. A search miss is not proof of novelty. I edited no files and ran no solvers or builds.

## Summary
- **Main target, RDSQS(52).** This is a Steiner quadruple system on 52 points whose derived triple system at every point is resolvable, i.e. is a Kirkman triple system.
  - Tan–Zhou (2025) name it as the smallest unknown order.
  - Their December 2025 paper still lists the matching exceptions 51, 69 and 75. That makes RDSQS(52), RDSQS(70) and RDSQS(76) the only gaps up to 100; my own recomputation of the known families gives the same three.
  - It fits the LKTS method exactly: build the quadruple system under a prescribed group with Kramer–Mesner, then solve for resolutions with SAT. Unlike LKTS, the resolution problems at different points are independent of each other.
- **Side finding for the LKTS(57)/LKTS(87) priority audit.** Tan–Zhou's arXiv:2512.22754v1 (28 Dec 2025), Theorem 2.8(1), lists LKTS exceptions a ∈ {57, 87, 93} below 100.
  - This is a second primary statement, before October 2026, that 57 and 87 were open.
  - The existing dossier only had the paywalled publisher abstract of this paper (`status-search-20261014.md:43`).
  - LKTS(57) and LKTS(87) from math-1, plus Wang's LKTS(93), remove all three exceptions [INFERENCE, using the paper's tripling assumption].

## Files
- `/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`
  - :128-134 — definition of mcDSQS; mcDSQS(20) was the only one known before this paper.
  - :176-189 — Theorem 1.3 and Corollary 1.4, the alphabet-size equivalence used below.
  - :869-902 — their RDCQS(8⁴:2), found by computer search under ⟨(0…31)(a,b)⟩, which gives RDSQS(34).
  - :1092-1117 — the open-problems section.
- `.../sources/liu-lei-2210.06214.txt`
  - :177-236 — RDSQS(22) and RDSQS(40).
  - :258-265 — RDSQS*(28) on Z7×Z4.
  - :449-465 — the product lemma, the known families, the FDH list, and Theorem 4.4.
- `.../sources/wang-2607.21521.txt:63-71,490-513,558` — Wang cites Tan–Zhou; nothing there on RDSQS(52).
- `.../sources/status-search-20261014.md:42-46` — earlier screen; the tilings paper's body was not read.
- `institute/runs/six-lane-2026-10-16/{outcomes.md,contract.json,review/lkts57-87-priority-audit.md}`

## How the pieces connect
- An RDSQS(v+1) gives an overlarge set OLKTS(v). It also gives LKTS(3v) (Tan–Zhou Theorem 1.1).
- Tripling turns RDSQS(n+1) into RDSQS(3n+1). The product rule combines RDSQS(u+1) and RDSQS(v+1) into RDSQS(uv+1).
- Alphabet-size equivalence (Shi–Xia–Krotov Theorem 5, quoted as Tan–Zhou Theorem 1.3): q0′(3,4,n) = min over SQS(n) of max χ′(derived) + 1. Here q0′ is the smallest alphabet size for which a diameter-perfect code with these parameters exists, and χ′ is the chromatic index.
- Search pipeline: Kramer–Mesner for the SQS under a group G, then SAT resolution for each point-orbit representative, then an explicit certificate, then three separately written verifiers.

## Report

### 1. Strongest target: RDSQS(52)
- **Exact statement.** There exists a set X with |X| = 52 and a family B of 5525 four-element subsets such that:
  - every one of the 22,100 three-subsets lies in exactly one block, and
  - for every x ∈ X, the 425 triples {B∖{x} : x ∈ B} on X∖{x} split into 25 parallel classes of 17 disjoint triples.
  - One quadruple system must work for all 52 points.
  - Equivalent form: q0′(3,4,52) = 26. Each STS(51) needs at least 25 colours, with equality exactly when it is resolvable.
- **Open attestation.** Tan–Zhou, [arXiv:2503.11934v1](https://arxiv.org/abs/2503.11934) (15 Mar 2025), §4 "Summary and open problems", item (1), PDF page 19:
  > "Find more examples of mcDSQS(v)s, for example, an mcDSQS(38) and an RDSQS(52) (the smallest unknown mcDSQS(6n + 2)s and the smallest unknown RDSQS(6n + 4)s, respectively)."
  - Later statement by the same authors, [arXiv:2512.22754v1](https://arxiv.org/pdf/2512.22754) (28 Dec 2025), Theorem 2.8, page 6:
  > "For any positive integer a ≡ 3 (mod 6) and a < 100, there exist (1) an LKTS(3^m · a) if a ∉ {57, 87, 93} and (2) an OLKTS(3^m · a) if a ∉ {51, 69, 75}."
  - The authors say this theorem comes from combining tripling with the known small RDSQS orders.
- **Latest version, citations, equivalents.**
  - arXiv: version 1 only, checked today. The journal version is DCC 93:4117–4140 (online 2025-06-23) and is paywalled, so its open-problems wording is unverified.
  - Citations found: the two Tan–Zhou 2025–2026 follow-ups (tilings; one-factorizations of multipartite graphs), the Etzion–Tan–Zhou mixed-Steiner paper, and Wang 2026. None of them constructs RDSQS(52).
  - arXiv search for "RDSQS" returns 2 hits. OpenAlex full-text search for "resolvable derived designs" since mid-2024 returns 2 hits. A Zenodo record from 2025-12-30 that mentions resolvable quadruple systems is science fiction ("Dyson swarm") with no certificate.
  - Known families, checked one by one; none reaches 52:
    - Liu–Lei Theorem 4.4 products: 51 = 3·17, and 17 is not a product of family members.
    - Tan–Zhou's 2^(2m+1)+2: gives 34, 130.
    - Zhou–Chang's 2q+2 family needs q ≡ 7 (mod 12); q = 25 fails.
    - FDH RDSQS(2p) only for p ∈ {23, 29, 41, 47, 53, 59, 71, 83}.
    - RDSQS(4v) would need RDSQS*(13), which cannot exist.
  - RDSQS(52) implies OLKTS(51), but not the converse. Whether OLKTS(51) is already known by another route is unchecked: Xu–Ji 2022 returned 403 and Xu–Ji 2024 (OLKTS+) is paywalled.
  - LKTS(153) follows, but it is already known, so there is no LKTS gain.
  - Corpus screens: openai/math remote CONTENTS (719 manuscripts) and the EulerSolve listing have no hits for quadruple, Kirkman, derived, overlarge or diameter-perfect.
- **Known results nearby.**
  - RDSQS exists for v ∈ {4, 10, 16, 22, 28, 34, 40, 46, 58, 64, 82, 88, 94, 100}. The only gaps up to 100 are 52, 70 and 76 (my derivation, matching the exceptions 51, 69, 75).
  - No nonexistence result is known for any v ≡ 4 (mod 6).
  - Computer constructions in this literature: RDSQS(22), RDSQS*(28), RDCQS(8⁴:2) under a cyclic group, and the FDH orders.
  - Kiermaier–Krčadinac–Wassermann (DCC 2026) say only v = 94 is undecided for cyclic SQS below 100. So existence of a cyclic SQS(52) is decided, but I did not open Feng–Chang 2011 Theorem 4.6 to see which way.
- **Certificate and verification.**
  - Certificate: the 5525 quadruples, then for each x in 0..51 the 25 classes of 17 triples (22,100 triple lines in total), plus a compact seed that expands to the exact bytes.
  - Three independent checkers (parent standard-library script, Codex in-memory, Claude-written), each checking:
    - all 22,100 triples are covered exactly once;
    - for every x, the classes contain exactly the derived triples at x, there are 25 classes, and each class partitions X∖{x}.
  - Each checker's mutation controls should be reported separately. Suggested mutations: a point swapped inside a block, a duplicated block, a triple moved between classes, a wrong x label, and a missing resolution.
  - A finite Lean existence proof is optional, as for LKTS.
- **Symmetry groups and tractability.** The arithmetic below is my own derivation.
  - **(A) Cyclic group Z52.**
    - 425 triple orbits.
    - Quadruple orbits: 5200 of length 52, 12 of length 26, 1 of length 13.
    - Counting forces the orbit of {0,13,26,39} and an even number b of half-length orbits, with 2a + b = 212.
    - Only one resolution problem remains: the derived design at 0, with 10,625 placement variables.
    - Optional extra symmetries: the multipliers 3 (order 6) or −1.
  - **(B) Rotational Z51 ∪ {∞}.** Two resolution problems.
  - **(C) 2q+2 template with q = 25.**
    - Points F25×{0,1} ∪ {∞0, ∞1}, group {x ↦ ax + b : a ∈ C ≤ F25*}.
    - When C ≠ 1, the blocks through {∞0, ∞1} are forced to be {∞0, ∞1, (x,0), (x,1)}.
    - It mirrors both Zhou–Chang's 2q+2 family and the G903 action that produced LKTS(87). 76 = 2·37 + 2 fits the same template.
  - [INFERENCE] tractability:
    - Building the quadruple system is routine at this size; Kiermaier–Krčadinac–Wassermann constructed at least 1535 SQS(50) and a rotational SQS(92) this way.
    - Each resolution problem is about the size of the LKTS(57) resolution model (12,628 variables), and there is no coupling between points.
    - The unknown is how often a group-invariant STS(51) is resolvable.
- **First bounded experiment** (≤2 hours, ≤4 workers).
  - Calibration on known orders:
    - template (C) at v = 16 (q = 7) and v = 40 (q = 19);
    - templates (A)/(B) at v = 22, 28 and 34.
  - Main run at v = 52: sample up to 100 cyclic SQS(52) solutions with recorded seeds, each with a 120-second resolution cap.
  - Any resolved derived design gives RDSQS(52) after verification. That closes the named open case, removes the a = 51 exceptions from Tan–Zhou's Theorems 2.8(2) and 4.11(2), and settles q0′(3,4,52) = 26.
  - If no cyclic SQS(52) exists in the encoding, switch to template (C).
  - UNKNOWN results change nothing.
- **Risks.**
  - Novelty: the posing group (Zhou's group) does computer searches and could have unpublished work. Chinese theses and journals are not searchable from here, and both DCC versions are paywalled.
  - Correctness: verifying only orbit representatives. The certificate should contain all 52 resolutions explicitly.

### 2. Alternative: mcDSQS(38)
- **Exact statement.** An SQS(38) (2109 blocks) such that for every x, the derived STS(37) (222 triples) splits into 19 partial parallel classes. Equivalent: q0′(3,4,38) = 20.
- **Attestation.** The same Tan–Zhou §4(1) quote; same version, citation and corpus checks as above.
- **Known results nearby.** mcDSQS(20) (Shi–Xia–Krotov 2023); mcDSQS(26), mcDSQS(32) and the 2·9^m+2 family (Tan–Zhou Theorems 3.9 and 3.10). No nonexistence results.
- **Search route.** Two routes:
  - A public dataset ([Zenodo 17153238](https://doi.org/10.5281/zenodo.17153238)) contains at least 1547 SQS(38). Test each SQS(38) for 19-colourings (4218-variable SAT per point).
  - Alternatively, build SQS(38) under Z38 or Z37 ∪ {∞}.
  - [INFERENCE] The share of STS(37) that are 19-colourable is unknown.
- **First experiment** (≤1.5 hours).
  - Main run: screen about 200 of the dataset SQS(38) at all 38 points.
  - Positive control: the dataset's SQS(20)s.
  - Negative control: 7-colourings of STS(13), which must come back UNSAT.
- **Risks.**
  - Novelty: the dataset has been public since September 2025; if the answer is an existing SQS(38), the result carries less weight.
  - Correctness: classes must be truly disjoint, and there must be exactly 19.

### 3. Alternative: RoSQS(56)
- **Exact statement.** An SQS on Z55 ∪ {∞} invariant under x ↦ x+1: 9 block orbits through ∞ and 117 full orbits.
- **Attestation.** Kiermaier–Krčadinac–Wassermann, [DCC 94:157](https://link.springer.com/article/10.1007/s10623-026-01888-w) (2026-07-07, open access), §2:
  > "For RoSQS(v) designs, there were seven open values below 100, namely v=46, 56, 70, 82, 86, 92, and 98 [30, Table I]. We succeeded to construct rotational designs RoSQS(46) and RoSQS(92)."
  - Same in arXiv 2509.23483v1 and on [Krčadinac's page](https://web.math.pmf.unizg.hr/~krcko/results/steiner3.html). OpenAlex shows no citing works.
- **Related results.** RoSQS(v) implies an optimal (v−1, 4, 2) optical orthogonal code (one direction only). RoSQS(10) is impossible because there is no cyclic STS(9). The same team tried cyclic SQS(94) and could neither build nor rule it out.
- **Why it is attractive.** The group is fixed by the definition. So one exact cover over Z55 (504 rows, about 6678 columns) decides the question either way. A verified DRAT/LRAT proof of UNSAT, from an independently audited encoding, would prove nonexistence.
- **Risk.** The team that built 46 and 92 is silent about 56. [INFERENCE] Their two-stage extension method may have failed there, and a joint model is the materially different approach.
- **First experiment** (≤2 hours).
  - Calibration: reproduce RoSQS(46) under Z45.
  - Main runs: Z55 with the order-5 multiplier 36 (36⁵ ≡ 1 mod 55), then Z55 alone.

### Screened, not recommended
- **S(3,5,41), S(3,6,46), S(3,5,50) and cyclic SQS(94):** the 2026 expert searches failed.
- **gcDCQS(20⁴:0), gcDCQS(32⁴:0), gcDCQS(18⁴:2)+FDGDD (Tan–Zhou §4(2)–(3)):** these would give infinite families, but they are 80–128-point objects with layered colouring conditions and a higher risk of getting the specification wrong.
- **Resolvable (45,5,1) design, (51,6,1) design, S(4,5,21):** famous or failed decades-long searches.
- **2-GHD₃(7,18;1):** settled by Östergård (DCC 2025).
- **OLKTS(69), OLKTS(75):** covered by RDSQS(70) and RDSQS(76) under the main target.
- **Lei 2004 finite list of auxiliary designs:** not a single bounded target.

### Access holes
- Paywalled: the DCC versions of Tan–Zhou 2025 and 2026, Xu–Ji 2022 and 2024, and Feng–Chang 2011 Theorem 4.6.
- arXiv API returned 429, so I used arXiv web search instead.
- Not searched: Google Scholar, Semantic Scholar, CNKI and theses.
