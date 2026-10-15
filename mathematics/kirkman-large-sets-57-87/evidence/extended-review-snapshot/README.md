# Large sets of Kirkman triple systems: orders 57 and 87

## Source

- Book: *10000 Selected Problems in Sciences: Mathematics* (Science Press, 2009).
- Problem: **柯克曼三元系大集的存在性问题 / Existence Problem of Large Sets of Kirkman Triple Systems**.
- Author: **常彦勋 (Yanxun Chang)**, Beijing Jiaotong University.
- Book pages **428–429**, PDF pages **444–445**. Exact extracted text: [`sources/book-excerpt.txt`](sources/book-excerpt.txt).
- The book asks for all orders `v=6t+3`, **t≥1**, and says 21 was its smallest unsettled order. The degenerate order 3 also satisfies the definition below and is admitted by the checker, but is not part of the book's t≥1 quantifier.

## Problem

On the labelled point set `X={0,…,v−1}`, an STS(v) is a set of unordered 3-element subsets in which every unordered pair of points occurs exactly once. A parallel class partitions X into triples. A KTS(v) is an STS(v) together with a partition of its blocks into `(v−1)/2` parallel classes. An LKTS(v) consists of **v−2** pairwise block-disjoint KTS(v)s; equivalently, their blocks partition all `binom(v,3)` triples. Resolutions may differ independently between constituents; no compatibility beyond disjoint blocks is required.

The **book's full question** is existence for every `v≡3 (mod 6)`, v≥9. The **two finite targets of this investigation** are LKTS(57) and LKTS(87). Search restrictions (cyclic development and, in some runs, a reflection) are not part of the problem.

## Status as of 2026-10-14

### (a) Verbatim book question and faithful translation

> 对于任意 v = 6t + 3, t ⩾ 1, 是否存在 v 阶柯克曼三元系大集？

**Translation:** “For every v=6t+3 with integer t≥1, does a large set of Kirkman triple systems of order v exist?” The source is book p.428 / PDF p.444, `sources/book-excerpt.txt`, lines24–25. This is a **universal existence question**. Constructing57 or87 would settle a new case, **not solve the book's question**.

### (b) Dated primary attestation and current-status search

**Current status: uncertified-open.** The latest located primary attestation is Chen Wang, [arXiv:2607.21521](https://arxiv.org/abs/2607.21521), dated **2026-07-23**. After defining LKTS with the same resolvability and disjointness conditions, §1 says that the existence problem “remains far from settled”; §4 explicitly identifies57 and87 as the two possible exceptions below200 and smallest remaining orders. This attests the book-wide problem and the two cases as unresolved **in that source at that date**. It is not a formal certification that no later resolution exists.

The **2026-10-14 search log is labelled “no resolution found; not proof of openness”**: [`sources/status-search-20261014.md`](sources/status-search-20261014.md). It includes arXiv/journal searches and works citing the key sources. OpenAlex returned zero indexed works citing Wang2026 and20 citing Chang–Zhou2013; the latter list includes Liu–Lei2023, Xu–Ji2024, Tan–Zhou2025, and a June2026 coding-theory article whose primary abstract was inspected. Index coverage and inaccessible bodies remain explicit limitations.

Parent-reported **openai/math corpus screen**: no matching family was found in the local clone at `adc7f1241` or in the remote listing checked **2026-10-14**. That screen was not replayed by this worker and is not proof of open status.

The book's smallest case21 was solved by Zhou–Chang, together with39, using multiplier automorphism groups: [DOI10.1007/s10623-009-9325-8](https://link.springer.com/article/10.1007/s10623-009-9325-8), online2009-09-16 / journal2010. Wang's broader below200 spectrum is a source statement, not independently replayed here; the original-body access caveat for Xu–Ji's family explaining147 remains in `sources/recursion-notes.md` §2.3.

### (c) Fully specified statements attacked

For each fixed **v∈{57,87}**, let `X={0,…,v−1}`. Seek families `P[i,j]⊆binom(X,3)`, with `0≤i≤v−3`, `0≤j≤(v−3)/2`, such that: (1) each `P[i,j]` partitionsX; (2) for eachi every pair ofX belongs to exactly one block of `⋃j P[i,j]`; and (3) every triple ofX belongs to exactly one `P[i,j]` over all i,j. Blocks are unordered three-element subsets, with no multiplicity. This is the unrestricted finite target, not the universal book assertion.

The model restrictions are fixed separately: cyclic development on `Z_(v−2)` plus two individually fixed infinities; sampled rainbow infinity matchings followed by finite-triple exact cover and unrestricted resolution; `C_19` acting on three19-point orbits with prescribed constituent-orbit patterns; and, for57, regular development by `F_55=C_11⋊C_5` plus two fixed infinities. The nonabelian multiplication is `(x,y)(x',y')=(x+3^y x' mod11,y+y' mod5)`. A negative result in one model is not a negative result for the unrestricted target. The extended solver parameters and modeling choices were recorded before the runs in [`sources/extended-search-protocol.md`](sources/extended-search-protocol.md).

The initial portfolio produced verified9/15 certificates and restricted proofs but no target certificate. The explicitly requested multi-hour continuation is being recorded separately; no running search is counted as a completed result.

## State of the art

### Direct constructions

“Development action” and “automorphism of one resolved base KTS” are different notions. Only actions actually supported by opened evidence are stated below. `[UNVERIFIED]` identifies missing historical method details rather than filling them with guesses.

| Orders v | Construction and action supported by the sources | Opened evidence |
|---|---|---|
| 9 | Classical existence; this directory independently reproduces a `Z_7` development with two fixed points. No claim about the original 1850 automorphism group. | Wang Table 1, [2607.21521](https://arxiv.org/abs/2607.21521); `evidence/cyclic9.txt` |
| 15 | Denniston's one-base transversal KTS, developed by `Z_13` with two fixed points. | Denniston [DOI 10.1016/0012-365X(74)90004-1](https://doi.org/10.1016/0012-365X(74)90004-1) metadata; full base classes in Wang–Shi [1307.3019](https://arxiv.org/abs/1307.3019), §4 |
| 33 | Schreiber, recorded 1974; exact original method/group `[UNVERIFIED]` in this investigation. | Wang Table 1 |
| 51,75,105,129 | Denniston, 1979; original construction/group details `[UNVERIFIED]` here. | Wang Table 1; bibliographic volume entry, not a reproduced construction |
| 201,369 | Chang–Ge: finite-field Y–Z partition construction, additive translations on `GF(q)` with q=199,367; multiplicative primitive elements g=3,6 organize the resolution. This is not a claim that the whole multiplier group fixes one resolution. | `sources/chang-ge-1999.pdf`, pp.309–311; [primary PDF](https://combinatorialpress.com/article/ars/Volume%2051/volume-51-paper-29.pdf); Wang Table 1 |
| 273 | Ge: the same Y–Z-partition method, q=271, primitive g=6, θ=19. | `sources/ge-2004.pdf`, Lemmas 2.3/3.1; [primary PDF](https://combinatorialpress.com/article/jcmcc/Volume%20049/vol-049-paper%2015.pdf) |
| 21,39 | Multiplier automorphism groups; the generators and base schedules were **not retrieved**, not proved non-public. | Zhou–Chang primary abstract, [DOI 10.1007/s10623-009-9325-8](https://link.springer.com/article/10.1007/s10623-009-9325-8) |
| 69,141,165,213,285,309,333 | Zheng–Chang–Zhou: `(q−1,3,{2,3},2)` disjoint difference families on exponent group `Z_(q−1)`, relative to `{0,(q−1)/3,2(q−1)/3}`, q=v−2. The opened appendix gives explicit finite-field data, not a complete base-automorphism specification. | [DOI 10.1007/s10623-016-0197-4](https://link.springer.com/article/10.1007/s10623-016-0197-4), abstract and appendix; online 2016, journal 2017 |
| 123,195,291,339 | `(q−1,3,{2,3},1)` difference families over `Z_(q−1)`, with q=121,193,289,337. | [DOI 10.1007/s10623-016-0315-3](https://link.springer.com/article/10.1007/s10623-016-0315-3), Appendix 1 |
| 111,159,183,231,279 | Two starter parallel classes over finite fields with q=109,157,181,229,277. | Same paper, Appendix 2 |
| 381 | Relative `(378,3,{2,3},2)` difference family, q=379. | Same paper, Appendix 3 |

In the “prime power sizes” paper the prime-power parameter is **q=v−2**, not necessarily the point order v. For the targets, `55=5·11` and `85=5·17` are not prime powers, and neither is a product of prime powers each congruent to 1 modulo 6. Thus the stated finite-field recipes do not apply. This does not prove that arbitrary ring/nonlinear constructions are impossible.

### Recursive constructions and their parameter barriers

Full hypotheses, source-access limitations, and arithmetic proofs are in [`sources/recursion-notes.md`](sources/recursion-notes.md). The following is a summary, not an invented unrestricted product theorem.

| Result | Actual input/output | Why it does not give 57 or 87 |
|---|---|---|
| Denniston tripling | `TKTS(v)+LKTS(v) ⇒ LKTS(3v)`; TKTS has a regular point action. Ge 2004 Lemma 2.2 states this explicitly. | Would need inadmissible KTS orders 19 or 29. |
| Lei product, 2002 | `LKTS(v)+TKTS(v)+LR(u) ⇒ LKTS(uv)`; LR(u) contains KTS(u)s with extra coupling. | Both u and v must be divisible by 3; these outputs are divisible by 9. Neither target is. Original theorem body was not retrieved; exact statement is from its indexed abstract, with LR definition checked in later primary text. |
| Zhang–Zhu, 2002/2003 | TRISQs remove the transitive-KTS assumption from tripling/product; the LR ingredient is not removed. | The same order obstructions remain. The historical weakening is explicitly confirmed in opened Wang–Shi and Liu–Lei introductions; original bodies were inaccessible. [DOIs 10.1016/S0012-365X(01)00178-9](https://doi.org/10.1016/S0012-365X(01)00178-9), [10.1016/S0012-365X(02)00766-5](https://doi.org/10.1016/S0012-365X(02)00766-5). |
| Wang–Shi | For prime-power `q≡1 mod6`, `LKTS(q+2) ⇒ LKTS(q^n+2)`, n≥2; in particular 171,345,363. | 55 and 85 are squarefree with two prime factors, so neither equals q^n. [1307.3019](https://arxiv.org/abs/1307.3019), Theorem 2.1. |
| Xu–Ji, 2021 | `LKTS(2^(2n+1)+1)` via special resolvable SQSs; first nontrivial orders 9,33,129. | 56 and 86 are not powers of 2. [DOI 10.1016/j.disc.2021.112373](https://doi.org/10.1016/j.disc.2021.112373); theorem attribution independently visible in Liu–Lei. Its additional indexed-abstract family `6·5^m(4·5^n+1)±3` explains 147 and also misses both targets; original-body verification of this additional family is `[UNVERIFIED]`. |
| Liu–Lei, 2023 | `RDSQS*(t) ⇒ RDSQS(4t)`; `RDSQS(u+1) ⇒ LKTS(3u)`. | RDSQS(u+1) requires `u≡3 mod6`, so outputs are 9 mod18. Targets would require impossible RDSQS(20)/RDSQS(30). A parameter 57 in their Theorem 4.4 gives **171**, not 57. [2210.06214](https://arxiv.org/abs/2210.06214), [DOI 10.1007/s10623-023-01221-9](https://link.springer.com/article/10.1007/s10623-023-01221-9). |
| Xu–Ji, 2024 | Special overlarge sets `OLKTS⁺(u)` replace RDSQS(u+1) in the implication to LKTS(3u). | Still needs admissible KTS order u; cannot use 19 or 29. [DOI 10.1007/s10623-024-01386-x](https://link.springer.com/article/10.1007/s10623-024-01386-x), opened abstract. |
| Tan–Zhou, 2025 | `RDSQS(2^(2n+1)+2)`, hence `LKTS(3·2^(2n+1)+3)`. | Again divisible by 9. [2503.11934](https://arxiv.org/abs/2503.11934), Theorem 3.2/Corollary 3.3. |
| Wang, 2026 | `LKTS(q+2)+CO(q) ⇒ LKTS(7q+2)`; CO exists when q is a product of prime powers each 1 mod6. Gives **93,177,219,261,303**. | Neither 55 nor 85 is divisible by 7. [2607.21521](https://arxiv.org/abs/2607.21521), Theorem 3.6/Corollaries 3.7–3.8. |

The Chang–Zhou 2013 survey [DOI 10.1016/j.jcta.2012.12.001](https://doi.org/10.1016/j.jcta.2012.12.001) was identified and its metadata opened, but full text remained blocked despite publisher/API/browser alternatives. No unseen theorem or group is attributed to it. Downloaded papers and saved publisher abstracts/appendices are in `sources/`; the literature scout's raw output and corrected overstatements are preserved in `evidence/literature-scout*.txt`.

## Attack

### Independent checker and successful known-case reproductions

[`work/check_lkts.py`](work/check_lkts.py) is standard-library-only and assumes **no automorphism group**. It checks point ranges, three distinct points per block, exact partitions in all parallel classes, exact pair coverage in every constituent, disjoint block sets, and explicit equality of the union with all triples.

Certificate format: `LKTS v`, then `KTS i`, `CLASS j`, and one integer triple per line; ids start at zero, with `#` comments allowed.

| Certificate | How obtained | Verified result |
|---|---|---|
| `evidence/cyclic9.txt` | Unhinted cyclic exact-cover search | 7 systems, 4 classes/system, 12 blocks/system, all **84** triples |
| `evidence/cyclic15.txt` | Unhinted cyclic exact-cover search, **196.928 s** solver time | 13 systems, 7 classes/system, 35 blocks/system, all **455** triples |
| `evidence/denniston15.txt` | Explicit published `Z_13+2` base schedule, expanded by `work/reproduce_denniston15.py`; table also corroborated by Wang–Shi §4 | Same complete LKTS(15) checks |

Each certificate has a `.check.json` receipt with certificate and checker SHA256. The checker also passed **23 positive/adversarial cases**, including repeated points/blocks/pairs, missing constituents/classes, foreign classes, duplicate constituents, invalid headers, and a valid relabelling; see `evidence/checker-mutations.json`. The independent referee counted all three certificates separately and replayed the mutation cases.

### Exact-cover encodings and finite search portfolio

[`work/search_cyclic.py`](work/search_cyclic.py) searches for one resolved KTS on `Z_(v−2)∪{∞₁,∞₂}` containing one representative of every translation orbit of triples. These orbits all have length v−2, so its translates would be a complete LKTS. Exact-cover columns enforce pairs, translation orbits, and `(class,point)` incidences. Translation fixes `{0,∞₁,∞₂}`; labelling classes by the infinity-1 block's unsigned difference removes class-permutation symmetry **without further restricting the cyclic model**.

[`work/search_multiplier.py`](work/search_multiplier.py) additionally bundles placements under a specified scalar multiplier, including its forced action on those class labels. `--reflection` in the first script instead uses negation swapping the infinities and fixing every class. These are concrete restricted attacks, not claims that the unrestricted problem is easy.

All **initial** target runs below had a **600-second solver limit**. The table records observed solver wall time; model construction and shutdown add to total runtime. **UNKNOWN is a timeout/incomplete search, not UNSAT.** No negative solver proof trace was exported; INFEASIBLE is solver-reported unless independently covered by a written proof. The separately preregistered extended portfolio uses7200-second overall limits.

| v | Extra base-resolution symmetry | Boolean rows | Threads | Solver seconds | Actual solver status | Receipt |
|---|---|---:|---:|---:|---|---|
| 57 | None beyond cyclic development | 776,161 | 4 | 600.152 | UNKNOWN | `evidence/cyclic57.json` |
| 57 | Negation swaps infinities, all classes fixed | 348,040 | 8 | 601.468 | UNKNOWN | `evidence/reflection57.json` |
| 57 | Multiplier 12, order 4 | 127,821 | 4 | 4.739 | INFEASIBLE | `evidence/multiplier57-a12.json` |
| 57 | Multiplier 32, order 4 | 128,701 | 4 | 0.191 | INFEASIBLE | `evidence/multiplier57-a32.json` |
| 57 | Multiplier 34, order 2 | 264,683 | 1 | 600.013 | UNKNOWN | `evidence/multiplier57-a34.json` |
| 87 | None beyond cyclic development | 4,400,621 | 2 | 600.382 | UNKNOWN | `evidence/cyclic87.json` |
| 87 | Multiplier 4, order 4 | 955,805 | 4 | 1.073 | INFEASIBLE | `evidence/multiplier87-a4.json` |
| 87 | Multiplier 33, order 4 | 777,798 | 4 | 1.428 | INFEASIBLE | `evidence/multiplier87-a33.json` |
| 87 | Multiplier 69, order 2 | 1,581,885 | 4 | 600.493 | UNKNOWN | `evidence/multiplier87-a69.json` |

The initial ledger [`evidence/search-summary.json`](evidence/search-summary.json) records **16 runs: 4 OPTIMAL, 6 INFEASIBLE, 6 UNKNOWN**, with **3507.749 aggregate solver-wall seconds** (parallel runs overlap; this is not elapsed session time or CPU time). Additional initial runs positively validated reflection/multiplier encodings at9, ruled out two stricter models at15, and attempted order21 with multiplier7 for300 seconds (**UNKNOWN**, no LKTS(21) reproduction claimed). Every run preserves command arguments, instance/source hashes, version, seed, limit, observed runtime, and log. Peak initial configured solver concurrency was16 workers; the extended portfolio has a separate resource allocation.

`Z_5×Z_11` and `Z_5×Z_17` are isomorphic to `Z_55` and `Z_85`; using their CRT coordinates with the same regular action is not a new independent search space.

### Stronger mathematical conclusions from the failed symmetry route

The complete written arguments are in [`proof.md`](proof.md). In particular:

1. **Fixed-point divisibility.** If an involution preserves a KTS(v) and its chosen resolution, and has f fixed points and c fixed parallel classes, then `2cf=f²−2f+v`; hence **f divides v**.
2. **All nonidentity scalar multipliers are excluded** in the cyclic base models at both targets, when both infinities are individually fixed and the chosen base resolution is invariant. The involutions modulo 55 have f=7,13,3; modulo 85 they have f=7,19,3. Divisibility excludes the first two; infinity-fixing negation is excluded by repeated finite pairs. Even-order multipliers reduce to these; the remaining order-5 case modulo 55 would partition seven fixed points into triples.
3. Negation **swapping** infinities at 87 is impossible already for the STS: the one-fixed-point involution gives the odd parity obstruction `binom(43,2)=903`. This does not exclude the corresponding order-57 model.
4. For the alternative action of `C_19` on three 19-point orbits at 57, an invariant **resolved** large set must have **17 or 36** fixed constituents, never 55. Its other constituents form one or two free 19-orbits. No search of those mixed-constituent cases was completed here.

Item 2 is a mathematical exclusion stronger than the two UNKNOWN multiplier runs; their logged statuses remain UNKNOWN. It does **not** exclude arbitrary cyclic LKTSs, multipliers preserving blocks without an invariant resolution, or noncyclic constructions. No novelty is claimed for these lemmas. `work/screen_symmetries.py` checks all **104 units** of the two rings and records the applicable obstruction; only identity survives.

### Recursive attacks actually attempted

Detailed definitions, counts, proofs, and missing compatibility conditions are in [`sources/recursion-notes.md`](sources/recursion-notes.md), §§3–5.

- **57=4·15−3:** a frame of type `14^4` filled with four KTS(15)s sharing one point gives a single KTS(57), but keeping those four holes fixed permits at most **13** disjoint systems and omits all `∞AB` and `AAB` triples. A precise sufficient replacement is **13 compatible frames of type `14^4` plus 42 compatible frames of type `2^28`**, using an explicit cross-group 1-factorization. Each latter frame needs **364 AAB and 140 ABC** triples. The simultaneous global triple partition, not individual-frame existence, is unproved.
- **87=4·21+3:** an ordinary frame of type `21^4` is impossible (21/2 missing-group classes); an STS(24,3) is impossible (outside-point replication 23/2); synchronizing four KTS(21) resolutions repeats the stem triple. An exact alternative deletes a three-point stem and asks for **three coupled matching arrays over 85 colors**, followed by compatible triangle decompositions/resolutions of the residual graphs on 84 points. One color needs 1120 pure-outside triangles, the other 84 need 1121 each. The matching compatibility and globally disjoint triangle resolutions remain unconstructed.

These are genuine failed routes and precise unresolved auxiliary objects, not new unconditional `4v±3` recursions.

### Reproduction

Run from this directory. Recorded searches used Python **3.12.12**, OR-Tools **9.15.6755**; checker-only runs need the Python standard library. No global package install is required. New replay logs below go to `/tmp`, leaving original receipts intact.

```sh
python3 work/check_lkts.py evidence/cyclic9.txt
python3 work/check_lkts.py evidence/cyclic15.txt
python3 work/check_lkts.py evidence/denniston15.txt
python3 work/test_checker.py
python3 work/screen_symmetries.py
python3 work/summarize_runs.py
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools==9.15.6755 python work/search_cyclic.py --v 57 --seconds 600 --threads 4 --output /tmp/lkts-replay/cyclic57
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools==9.15.6755 python work/search_cyclic.py --v 87 --seconds 600 --threads 2 --output /tmp/lkts-replay/cyclic87
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools==9.15.6755 python work/search_multiplier.py --v 57 --multiplier 32 --seconds 600 --threads 4 --output /tmp/lkts-replay/multiplier57-a32
```

Each other run is reproduced by its receipt's arguments with the same version pin. Multiworker search trajectories/timings may vary; mathematical certificates and the finite arithmetic screen are deterministic. The independent referee commands/prompts are saved under `work/run_review.py` and `evidence/*review*`.

## Claims

| Claim | Status | Evidence path |
|---|---|---|
| The book's 21 case is settled in Zhou–Chang, while Wang July 2026 reports 57/87 as remaining | PROVED | Source statements: `sources/book-excerpt.txt`, `sources/zhou-chang-2010-publisher.txt`, `sources/wang-2607.21521.txt`; not proof of exhaustive current literature coverage |
| Explicit LKTS(9) and two explicit LKTS(15) certificates satisfy the full definition | COMPUTED+VERIFIED | `evidence/cyclic9.txt`, `cyclic15.txt`, `denniston15.txt`; respective `.check.json`; `independent-review.md` |
| Checker accepts valid relabellings and rejects the tested corruptions | COMPUTED+VERIFIED | `evidence/checker-mutations.json`, 23 cases |
| Cyclic exact-cover and multiplier quotient encodings are exact within their stated models | PROVED | `proof.md` §1; `work/search_cyclic.py`, `search_multiplier.py`; independent code review |
| A nonidentity scalar multiplier can preserve the base resolution of the specified cyclic LKTS(57)/(87) | REFUTED | `proof.md` §§2,7–8; finite arithmetic in `evidence/symmetry-screen.json` |
| The 104-unit arithmetic classification | COMPUTED+VERIFIED | `work/screen_symmetries.py`, `evidence/symmetry-screen.json` |
| One-fixed-point involution at order 87 | REFUTED | `proof.md` §4; parity argument |
| Three 19-cycles with all 55 constituents and their resolutions fixed | REFUTED | `proof.md` §5 |
| Fixed four-hole filling alone produces either target large set | REFUTED | `sources/recursion-notes.md` §§4–5 |
| The specified compatible frame package for 57 would suffice | PROVED | `sources/recursion-notes.md` §4; existence of that package is OPEN |
| The specified coupled matching/triangle-resolution package for 87 would suffice | PROVED | `sources/recursion-notes.md` §5.4; existence of that package is OPEN |
| Unrestricted cyclic LKTS(57), cyclic LKTS(87), and the reflection-resolved model at 57 | OPEN | `evidence/cyclic57.json`, `cyclic87.json`, `reflection57.json`: UNKNOWN |
| LKTS(57); LKTS(87); the book's universal existence conjecture | OPEN | No target certificate or complete universal proof |

## Independent review

- **First referee:** registry-selected Codex **gpt-6.1-sol, max**, read-only/ephemeral; observed identity in `evidence/review-stderr.log`. Verdict **correct**, no errors found. It verified the pinned nine inputs, independently counted all three small certificates, replayed all 23 mutation cases in memory, audited both encodings, and checked the original six proof sections. Output: [`evidence/independent-review.md`](evidence/independent-review.md); prompt, hashes, and receipt are adjacent.
- The exact proof snapshot reviewed in that first round is retained as `evidence/proof-reviewed-original.md`; its SHA256 matches the original `proof.md` entry in `evidence/review-inputs.json`. Later §§7–8 strengthen rather than alter those arguments.
- **Second referee:** the same registry-selected Codex model/effort, read-only/ephemeral, returned **correct-with-fixes** on the stronger fixed-point-divisibility/all-multiplier theorem and the auxiliary-design reductions. All corrections were applied: use the unique infinity-pair block `{r,∞₁,∞₂}` rather than silently assuming r=0; state that divisibility is not established from block-set invariance alone; restrict the fixed-subsystem bound to w≥3; explicitly require complete edge/triangle assignment and point-disjoint complements in the order-87 resolutions. It confirmed the group enumeration, all frame inventories, and both sufficient auxiliary packages. Output: [`evidence/addendum-review.md`](evidence/addendum-review.md); resolution record: [`evidence/review-resolutions.md`](evidence/review-resolutions.md).
- The literature scout's “not public/not online” claims were narrowed to **not retrieved**, and two actually accessible older PDFs were obtained and opened. No unseen automorphism generators or inaccessible theorem bodies are asserted.
- No unresolved objection remains from the two completed referees. They did not independently certify negative CP-SAT logs or the full literature spectrum. The new extended encodings/claims will receive a focused review before their final handoff; the earlier process-exit statement applies only to the completed initial portfolio.

## Next steps

The highest-value next finite action is **not another nontrivial multiplier-invariant-resolution search**: that entire model is excluded. Keep the cyclic exact-cover model with no extra base multiplier, and replace its class-indexed Boolean expansion with a staged infinity-matching/finite-triple exact cover plus resolution constraints; benchmark the exact encoding against the stored 9/15 certificates before allocating a longer target run.

An independent noncyclic action route is to encode `C_19` on `Z_19×{0,1,2}` with **36 fixed constituents plus one free 19-orbit**, or **17 fixed plus two free 19-orbits**. Do not incorrectly force all 55 constituents to be invariant. For the recursion route, the exact first missing object is the compatible **13+42 frame package** in `sources/recursion-notes.md` §4, not merely another ordinary Kirkman frame.

The initial bounded portfolio is complete; the parent explicitly requested and authorized a multi-hour continuation. Its runs and new mathematical reductions are tracked separately. No running or incomplete phase is reported as a completed search, and the unrestricted existence goal remains unresolved absent a verified target certificate.

