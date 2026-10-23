I'm recommending a packing-array question for info-1 (candidate 1 below), but only if a 15-minute literature check comes back clean. The other two candidates are a quick-win difference family that needs only one search (candidate 2) and the point-cyclic case after 88 (candidate 3). I ran no searches or solvers. The counting bounds, the T2 structure and the heuristic odds below are my own hand derivations, labelled [INFERENCE] where they appear.

## Candidate 1 — Packing array PA(19,8,6), i.e. the optimal 6-ary code A₆(8,7)

This is a new sub-area (codes / packing arrays), not a cyclic difference family.

| Field | Content |
|---|---|
| Exact claim | Decide whether a PA(19,8,6) exists: a 19×8 array over {0..5} in which every pair of columns contains each ordered symbol pair at most once. Equivalently, a 6-ary code of length 8 with 19 codewords where any two codewords agree in at most one position. Same-lane follow-ups: PA(25,11,8) (best known 24, bound 25) and PA(29 or 30,12,9) (best known 28, bound 30). |
| Latest open quote | Rosin, CPro1, arXiv:2501.17725v1 (29 Jan 2025), Table 1, PDF p.2. Row "(8, 6): 19 ≥ N ≥ 12 \| N ≥ 17 \| N ≥ 18". Caption: "For each combinatorial design problem, the smallest open instances from the Handbook are listed, along with progress on these published elsewhere in the literature." The later version arXiv:2505.23881v1 (29 May 2025), Table 1(a), lists (18,8,6) and (24,11,8) as solved, but not 19 or 25. |
| Baseline | Best known N=18 (CPro1); upper bound 19 (Handbook). By pair counting, N=20 needs 192 coincident row pairs but only 190 exist, so N ≤ 19. At N=19 the slack is only 3 [INFERENCE], so almost every pair of rows agrees exactly once. If every column has symbol counts (4,3,3,3,3,3), the array is a resolvable packing of 19 points into 8 classes, each one 4-block plus five 3-blocks. That is a Kirkman school project / KPD({3,4*},19) design [INFERENCE]. |
| Certificate and verification | Existence: the 19×8 array itself; check all 28 column pairs; a Lean `decide` proof is trivial. Nonexistence: a SAT encoding with written-out symmetry breaking and a soundness argument, an LRAT proof checked by cake_lpr, plus an independent second method (orderly generation over column types or a different encoder/solver). |
| Initial 2-h experiment | (1) Build the verifier and controls, using CPro1's published PA(18,8,6) from its GitHub repo as a positive control. (2) Run a CaDiCaL/kissat SAT model with proof logging on 1 CPU for 60 min, on the full PA(19,8,6) and on the all-(4,3⁵) subcase separately. Alongside it, run tabu search with 4 seeds for 30 min. **Decision value:** SAT settles the maximum at 19; certified UNSAT settles it at 18. Either way the Handbook entry is closed. |
| Nonexistence risk | Unknown to moderate. CPro1 failing to reach 19 is weak evidence against existence. Both outcomes are decisive if proved. |
| Crowding / priority risk | Moderate. CPro1 (Rosin, Jan/May/Dec 2025, still active in 2026) covers the construction side; the nonexistence side is not crowded. **Kill check before freezing:** if KSP(19) or KSP(25) is already published, PA(19,8,6) or PA(25,11,8) exists and the table entry is stale. Sources to read (paywalled for me): Colbourn–Ling, Disc. Math. 203 (1999) 49–60 (zbMATH: "nearly completely cover" v ≡ 1 mod 6); Cao–Du, Disc. Math. 281 (2004) 83–95 ("improve the existence results on KPD({3,s*},v) for s=4,5"); Phillips–Wallis–Rees 1998; Stevens–Mendelsohn, TCS 2004. |
| Physics/math overlap | None with physics. The design-theory overlap is only through the KSP link; the object is a code, and KPDs are also used for (2,w) threshold schemes. |

## Candidate 2 — (31⁶,7,1) difference family over GF(31⁶)

| Field | Content |
|---|---|
| Exact claim | Construct a (q,7,1) difference family in (GF(q),+), q = 31⁶ = 887,503,681: 21,131,040 base blocks of size 7 whose differences cover each nonzero element exactly once. |
| Latest open quote | Hetman–Baicheva–Topalova, J. Algebra Comb. Discrete Appl. 13(1) (2026), §1, PDF p.4 (the same sentence the 211 contract cites): "a (q,7,1) CDF exists for any prime power q ≡ 1 (mod 42) except for q = 43, possibly for q = 127 (nonexistence proved in [5]), 211, 31^6, and primes q ∈ [261239791, 1.236597·10^13]". Local pinned copy: `cdf-k5/sources/hetman-baicheva-topalova-2026-jacodesmath-389.pdf`. |
| Baseline | 31⁶ is a possible exception in Chen–Wei–Zhu (JCD 2002). I checked q ≡ 1 (mod 42), and that (−3)^((q−1)/14) = 1 because −3 has order 15 in F₃₁. So 31⁶ falls inside the paper's gap range and fails its special-construction condition, which is consistent with it being listed [INFERENCE about their method]. |
| Certificate and verification | Wilson-type certificate: an irreducible degree-6 polynomial f, a primitive element g (q−1 = 2⁶·3²·5·7²·19·331), and one block B whose 21 differences lie in 21 distinct cosets of the index-21 subgroup. The full family is {g^(21j)·B : 0 ≤ j < 21,131,040}. Independent check: regenerate all 887,503,680 differences into a 111 MB bitset, with two separate implementations. |
| Initial 2-h experiment | Implement GF(31⁶) arithmetic and a randomized backtracking search over B (an estimated ~10⁵ coset tests [INFERENCE]), then the brute-force verifier. **Decision value:** closes one listed exception within about an hour; the rest of the prime gap stays open. |
| Nonexistence risk | Very low; the heuristic count of valid blocks is about 10³⁷ [INFERENCE]. |
| Crowding / priority risk | Low crowding. Prior art is unchecked: forward citations of Chen–Wei–Zhu, the Abel–Buratti Handbook chapter, and Buratti–Pasotti FFA 2009. HBT writes "CDF"; for q = 31⁶ the original theorem is over GF(q). A cyclic family on Z₈₈₇₅₀₃₆₈₁ would be a different, harder question. |
| Physics/math overlap | None with physics. The information link is weak (a non-cyclic difference family giving S(2,7,q) and constant-weight codes). Significance is modest; it is a sibling of the current 211 target. |

## Candidate 3 — Point-cyclic resolution of a 2-(100,4,1) design

| Field | Content |
|---|---|
| Exact claim | Construct (or rule out) a cyclic 2-(100,4,1) design with a resolution invariant under the 100-cycle. |
| Latest open status | Derived, not stated verbatim. Topalova–Zhelezova, Axioms 15(10):762 (13 Oct 2026), §7, p.11: "That is why v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1) designs has not yet been determined." Our run has now settled 88. The next v ≡ 4 (mod 12) is 100. Known results I checked leave it undetermined: the Lam–Miao family needs primes of the form 12s+1, and 25 = 5² is not covered; Mishima–Jimbo 2000 Corollary 4.4 and Theorem 4.3 would need a CRCB(20,4,1), which does not exist (I read the preprint); the info-2 table shows 100 not excluded. |
| Baseline | Type T1 (short orbit as one class) is excluded by the Mishima–Jimbo 1997 lemma (v/k = 5², gcd(5,4) = 1). Types T2 and T3 pass Mishima–Jimbo 2000 Lemmas 4.1 and 4.2. For T2 the structure is forced [INFERENCE]: one orbit of 25 classes fixed by ⟨25⟩, and two orbits of 4 classes fixed by ⟨4⟩. That reduces to an exact-cover search for 8 base blocks covering Z₁₀₀∖{0,25,50,75}: 6 blocks with distinct residues mod 25 whose translated residue sets partition Z₂₅∖{0}, plus 2 blocks containing all four residues mod 4. |
| Certificate and verification | The base blocks plus the T2 rule. Check the 96 differences, the 825 blocks, all 33 classes as partitions, and invariance under +1. A Lean `decide` proof works as it did for 88 and the CDFs. |
| Initial 2-h experiment | Adapt the info-2 CDF exact-cover code to the T2 model. Use v=52, also a T2 order with class orbits of 4 and 13, as a positive control. Search for 60 min; if it misses, try a T3 model with a 5×5 arrangement. **Decision value:** settles the smallest undetermined order after 88. Follow-ups 112 (T1 forced), 136, 160 and 196 could complete the table for v ≤ 200. |
| Nonexistence risk | Low; the heuristic count of T2 solutions is well above 1 [INFERENCE]. |
| Crowding / priority risk | Moderate. The Sofia group is moving up this sequence. Chang–Miao 2002 and the Handbook are unread. The work overlaps info-2's 88 lane, so assign ownership explicitly. |
| Physics/math overlap | None. Information link: LDPC codes and optimal (33,100,32)₂₅ equidistant codes. |

## Recommendation

Freeze **candidate 1** for info-1 after the 15-minute KSP/KPD check. It is the only option that is explicitly open in a recent primary source, is in a new sub-area, and gets a decisive answer either way (19 or 18). Its exact SAT/proof route is also the side the LLM construction searches never covered.
- If the check shows KSP(19) or KSP(25) is already published, switch info-1 to **candidate 2**: it is explicit, quick, and from the same source as 211.
- Give **candidate 3** to info-2, which has the 88 machinery and is idle after the CPCW lengths; it has the best odds of the three but is only derived-open.

## Dropped leads

- **(163,5,1) optimal CPCW code:** already found by info-2 at 02:23 PDT (`cpcw-optimal/README.md` §4).
- **(183,5,1), (184,5,1):** marked "?" ("nothing is known") in Baicheva–Topalova 2026 Table 1, but outside that paper's v ≤ 181 scope. Seconds of work with info-2's tools; offer as an info-2 add-on, not a frozen target.
- **Baicheva–Yoveva–Topalova 2026 (k(k−1)s+2, k, 1) codes:** no list of specific undecided lengths; "yes" in its Table 1 only means the necessary conditions hold.
- **Hetman–Baicheva–Topalova 2026 open problem:** it is about classification, not existence.
- **General S(2,k,v), k ≥ 6:** design theory and long-standing hard cases.
- **Modular Golomb rulers:** determined for k ≤ 15 (Gordon, arXiv:2408.16721v3).
- **Gordon's (61,30,14,30) almost difference set:** the quadratic residues mod 61 appear to realize it [INFERENCE], so not a valid target.
- **Buratti–Stinson 2-regular OOCs:** no explicit open list, and no 2024–2026 restatement found.
- **Optimal (v,4,1) OOCs:** solved; v=25 is a determined exception.
- **Perfect difference families, k=4:** solved (arXiv:2510.20446).
- **Variable-weight {3,4,5} geometric difference families:** completed (arXiv:2609.29202).
- **Additive quaternary codes, dimensions 3.5 and 4:** completed (Kurz, May 2026).
- **Odd binary Z-complementary pairs:** lengths ≤ 49 settled; 51 and above not stated open.
- **Conflict-avoiding codes, SEDFs, functional batch/PIR codes:** no finite stated open case.
- **NMDS maximum lengths:** latest open table found is from 2006.
- **LCD/self-dual tables, covering arrays, covering sequences, deletion codes:** either record-improvement only, crowded, or both.
- **Weighing matrices W(n,16), n ∈ {25,27,29}:** Hadamard-adjacent and already swept by LLM search.
- **RBIBD(45,5,1):** no 2024–2026 open statement located.
- **Quantum codes (((11,K,4)), AME, quantum MDS):** overlap with the physics lanes.

## Local files used

- `institute/runs/six-lane-2026-10-16/{transitions.json, outcomes.md, checkpoints.md, screening/*.md, screening/info-1-cdf211-contract.json}`
- `information-science/evidence/six-lane-20261016/cpcw-optimal/{README.md, notes/table3-163/NOTE.md, sources/axioms-15-00035.layout.txt, sources/axioms-15-00679.layout.txt}`
- `.../point-cyclic88/{sources/axioms-15-00762.pdf, evidence/general-table-2000.txt}`
- `institute/runs/six-lane-2026-10-16/review/point-cyclic88-priority-audit.md`
- `.../cdf-k5/sources/hetman-baicheva-topalova-2026-jacodesmath-389.pdf`
