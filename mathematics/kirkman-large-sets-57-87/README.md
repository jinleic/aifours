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

For the cyclic model, finite labels are0,…,n−1 and the infinities are n,n+1. For C19, point(x,i) is encoded19i+x and the generator is `(x,i)↦(x+1 mod19,i)`; there are no distinguished infinities. Its fixed constituents are required to have invariant **chosen resolutions**, while free constituents are translates of arbitrarily resolved bases. For F55, finite(x,y) is encoded11y+x, the action is left multiplication, and labels55,56 are fixed infinities. These are explicit search restrictions, not extra assumptions in the book's question.

The completed work produced verified9/15 certificates and a checked **partial packing of17 disjoint resolved KTS(57)s**, covering9,044 distinct triples. A full LKTS(57) requires55 systems and29,260 triples. **No LKTS(57) or LKTS(87) certificate was found.** The partial packing is not a solution of either finite target or the universal book question; all declared finite searches have now ended.

**HMZ + Lean continuation:** [`hmz-lean-20261014/`](hmz-lean-20261014/README.md) adds25 kernel-checked partial theorems, including exact-row certificate soundness and concrete C19/C29 development criteria. The prescribed release-system16 joint model was actually attempted once:61,948 variables,4,425 exact-one columns, two workers,480.009 solver seconds, **UNKNOWN** with no candidate. The actual3600-second HMZ run retained three reviewer `done:false` verdicts and ended `how:"stopped"` (exit143), not accepted. The universal goal and both57/87 cases remain unsolved.

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

The initial proofs are in [`proof.md`](proof.md); the extended block-set and action-count proofs are in [`sources/extended-group-analysis.md`](sources/extended-group-analysis.md) and [`sources/c19-search-notes.md`](sources/c19-search-notes.md). All were independently reviewed. No novelty is claimed.

1. **Fixed-point divisibility:** if an involution preserves a KTS(v) and its chosen resolution, with f fixed points and c fixed classes, then `2cf=f²−2f+v`; hence f dividesv.
2. **Stronger block-set theorem:** at57 and87, no nonidentity scalar multiplier fixing both infinities can preserve a cyclic-transversal **STS block set**, even if its eventual resolution is unrestricted. For an involution put `m=gcd(a−1,n)`, `f=m+2`, `t=(n−m)/2`. Centering each triple by the average of its finite points proves that each fixed translation orbit contains exactlym fixed triples. The fixed-orbit count is `O=[binom(f,3)+ft]/m`, whereas an invariant STS has `B=f(f−1)/6+t` fixed blocks. Their difference `O−B=n/m−1>0` contradicts transversality. Even-order scalars reduce to an involution; the remaining order-five case at55 forces the impossible cyclic-transversal7-point fixed subsystem.
3. **Classical reverse-STS corollary:** no STS(87) has a one-fixed-point involution, since `binom(43,2)=903` is odd. This is the Doyen–Rosa/Hartman–Hoffman reverse-STS necessary condition at its full strength, not a novel cyclic-only theorem.
4. **C19 on three19-point orbits at57:** with invariant chosen resolutions of fixed constituents, the36-fixed+one-free19-orbit pattern is impossible. Each fixed KTS requires at least4 AAA triple-orbits, but only126 are admissible (27 arithmetic-progression orbits repeat pairs), and `36·4>126`. Only **17 fixed plus two free19-orbits** survive in this resolved action.
5. **C29 on three29-point orbits at87:** the analogous AP count leaves336 admissible AAA orbits, while every fixed resolved constituent needs at least7. It excludes56 or85 fixed constituents, leaving only **27 fixed plus two free29-orbits**. This is an analytic reduction, not a completed search of the surviving C29 case.

The scalar theorem strengthens the earlier invariant-resolution exclusion and supersedes the formerly conceivable “scalar block symmetry plus unrestricted resolution” workaround. It does **not** rule out arbitrary cyclic LKTSs or noncyclic constructions. The original UNKNOWN statuses are unchanged. Exact finite counts are in `evidence/group-arithmetic.json` and `evidence/c19-36-obstruction.json`.

**Remaining involutive affine ansatzes.** Write the finite action as `x↦ax+b`, where `a²=1` and `(a+1)b=0`. Since n is odd it is conjugate by translation to the scalar action; the infinity-pair block fixes the base normalization. Every nonidentity affine map fixing both infinities individually is excluded by item2. If it exchanges the infinities:

| Finite modulus | Involutive scalar choices after translation | Remaining possibility |
|---|---|---|
| 55 | a=1 fixes55 finite points (subsystem too large); a=21,34 fix5,11 (inadmissible STS orders); a=54 fixes1 | **Only negation exchanging the infinities**, or its affine conjugates, survives. Its resolution need not be invariant. |
| 85 | a=1 fixes85 (subsystem too large); a=16,69 fix5,17 (inadmissible); a=84 fixes1 (classical reverse-STS obstruction) | **None**. The affine-normalizer stabilizer of a cyclic-transversal base STS(87) is trivial. |

The kernel of the action of an affine base-automorphism group on the two infinities is trivial, so no higher-order infinity-swapping affine case is omitted. Automorphisms outside this normalizer and other development groups remain possible.

### Recursive attacks actually attempted

Detailed definitions, counts, proofs, and missing compatibility conditions are in [`sources/recursion-notes.md`](sources/recursion-notes.md), §§3–5.

- **57=4·15−3:** a frame of type `14^4` filled with four KTS(15)s sharing one point gives a single KTS(57), but keeping those four holes fixed permits at most **13** disjoint systems and omits all `∞AB` and `AAB` triples. A precise sufficient replacement is **13 compatible frames of type `14^4` plus 42 compatible frames of type `2^28`**, using an explicit cross-group 1-factorization. Each latter frame needs **364 AAB and 140 ABC** triples. The simultaneous global triple partition, not individual-frame existence, is unproved.
- **87=4·21+3:** an ordinary frame of type `21^4` is impossible (21/2 missing-group classes); an STS(24,3) is impossible (outside-point replication 23/2); synchronizing four KTS(21) resolutions repeats the stem triple. An exact alternative deletes a three-point stem and asks for **three coupled matching arrays over 85 colors**, followed by compatible triangle decompositions/resolutions of the residual graphs on 84 points. One color needs 1120 pure-outside triangles, the other 84 need 1121 each. The matching compatibility and globally disjoint triangle resolutions remain unconstructed.

These are genuine failed routes and precise unresolved auxiliary objects, not new unconditional `4v±3` recursions.
### Extended portfolio: fixed models and completed calibrations

The extended protocol is [`sources/extended-search-protocol.md`](sources/extended-search-protocol.md). Six7200-second staged cyclic configurations combine Kissat4.0.4, CaDiCaL3.0.1, and CP-SAT9.15.6755 with distinct seeds and sampled infinity matchings. Joint-modular CP configurations solve the matchings and finite-orbit shifts simultaneously, with531 primary variables at57 and1246 at87. Exactness and restrictions are proved in [`sources/staged-encoding.md`](sources/staged-encoding.md).

Completed extended portfolio:

| Model | Observed run time | Actual outcome |
|---|---:|---|
| Cyclic frozen-matchings, three configurations per target | Six runs, each7200.016–7201.744s |234 valid matching samples; every finite-STS call UNKNOWN; no candidate STS or resolution stage |
| Joint modular model at57, no frozen matchings |7200.009s|UNKNOWN; no STS candidate |
| C19, fixed starter AAA count4 |7200.134s|17 disjoint invariant resolved KTSs constructed in119.988s;1,087,824-placement frozen-complement completion UNKNOWN after7074.986 solver seconds |
| C19, fixed starter AAA count5 |7200.028s|259 valid candidates across29 restarts, maximum disjoint prefix15; completion stage not reached |
| Reflection-invariant block set at57, unrestricted resolution |7200.004s|UNKNOWN; no STS candidate |
| Nonabelian F55 starter/triangle/resolution model |7200.027s|24 verified starter pairs; all24 triangle calls UNKNOWN; no STS candidate |
| Joint modular model at87, no frozen matchings |7202.786s|UNKNOWN; no STS candidate |
| Frozen C19 packing, pair-first Kissat completion |7200.191s|UNKNOWN; no pair of STSs found, so no resolution stage |
| Same frozen packing, pair-first CaDiCaL completion |7200.156s|UNKNOWN; no pair of STSs found |
| Same frozen packing, modular CP completion |7200.017s|UNKNOWN; no pair of STSs found;124,411,357 solver-reported branches and2,811,766 conflicts |

Every row retains the full per-run receipt, model/source hashes, parameters and logs. Summed run times overlap and are not elapsed session time or CPU time. The36-fixed C19 pattern was instead eliminated by proof and exhaustive orbit inventory; it was not falsely credited with a7200-second search.

The17-packing is now also stored as **plain text** [`evidence/c19-partial17.txt`](evidence/c19-partial17.txt), explicitly headed `PACKING 57 17`, not `LKTS 57`. The independent `check_partial_packing.py` checks all class partitions, per-system pair counts, and cross-system block disjointness. Its PASS receipt records9,044 distinct blocks and `is_full_large_set:false`. A separate standard-library C19 replay checked all276 generated candidate witnesses, the AP inventory, disjoint prefixes and frozen complement (`evidence/c19-parent-replay.json`).

The pair-first continuation used40,432 native placement variables (197,904 total CNF variables,472,417 clauses), or2,128 color/shift decisions in the6,400-variable modular CP model. Its exact models and lossless orbit anchor are documented in `evidence/c19-paircover-notes.md`. All three reconstructed models matched their original SHA256s after the lifecycle correction (`evidence/c19-paircover-parent-replays.json`). No candidate pair was found, so no candidate blocking or resolution call occurred in these three runs.

Completed calibration evidence, not target constructions:

- The staged Kissat9, CaDiCaL15 and CP-SAT15 pipelines produced full independently checked certificates (`evidence/extended-validate*.txt`).
- Exact original and twice-blocked CNFs were regenerated from saved inputs and matched solver SHA256s; frozen-snapshot replays also match (`evidence/extended-cnf-replay-checks.json`, `extended-review-supplement-replay.json`).
- The joint modular model found LKTS(9). Its unhinted120-second order15 run found131 STSs, received131 resolution-INFEASIBLE reports, then timed out; no unhinted LKTS(15) discovery is claimed for that run. A separate **known-Denniston embedding** and resolution check passed (`evidence/extended-modular-embedding15.json`).
- A300-second order21 calibration sampled10 matching pairs; all ten30-second finite-STS calls returned UNKNOWN. No LKTS(21) reproduction was obtained.
- The reflection block-set pipeline independently reproduced order9. The F55 setup smoke verified starter pairs but found no target STS.

The final ledger [`evidence/extended-summary.json`](evidence/extended-summary.json) contains **15 target configurations with7200-second limits**, totaling **108,007.808 observed run-wall seconds** (about30.002 hours summed across overlapping runs, **not** elapsed session time or CPU time). All ended without a target certificate. Global configured solver concurrency was at most16; all owned processes exited or were reaped. Both final native completion children exited on SIGTERM, with no forced termination. Frozen matching/packing restrictions remain explicit, and no timeout is promoted to UNSAT.


### Reproduction

Run from this directory. Recorded searches used Python **3.12.12**, OR-Tools **9.15.6755**; checker-only runs need the Python standard library. No global package install is required. New replay logs below go to `/tmp`, leaving original receipts intact.

```sh
python3 work/check_lkts.py evidence/cyclic9.txt
python3 work/check_lkts.py evidence/cyclic15.txt
python3 work/check_lkts.py evidence/denniston15.txt
python3 work/check_partial_packing.py evidence/c19-partial17.txt --expected-systems 17
python3 work/c19_verify.py evidence/c19-36-obstruction.json evidence/c19-17-staged.json evidence/c19-17-staged-u5.json --output /tmp/c19-packing-replay-new.json
python3 work/test_checker.py
python3 work/screen_symmetries.py
python3 work/summarize_runs.py
python3 work/summarize_extended.py
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools==9.15.6755 python work/search_cyclic.py --v 57 --seconds 600 --threads 4 --output /tmp/lkts-replay/cyclic57
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools==9.15.6755 python work/search_cyclic.py --v 87 --seconds 600 --threads 2 --output /tmp/lkts-replay/cyclic87
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools==9.15.6755 python work/search_multiplier.py --v 57 --multiplier 32 --seconds 600 --threads 4 --output /tmp/lkts-replay/multiplier57-a32
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python -B work/c19_staged_completion.py replay evidence/c19-paircover-kissat-data/paircover-0000.manifest.json --output /tmp/c19-completion-replay-new.cnf
```

Use fresh output paths for replays that refuse overwrites. Each other run is reproduced by its receipt's arguments with the same version pin. Multiworker search trajectories/timings may vary; certificates and exact model-byte replays are deterministic. Native and modular frozen-completion replay results are saved in `evidence/c19-paircover-parent-replays.json`; replay authenticates model bytes, not historical source identity. The independent referee commands/prompts are saved under `work/run_review.py` and `evidence/*review*`.

## Claims

| Claim | Status | Evidence path |
|---|---|---|
| The book's 21 case is settled in Zhou–Chang, while Wang July 2026 reports 57/87 as remaining | PROVED | Source statements: `sources/book-excerpt.txt`, `sources/zhou-chang-2010-publisher.txt`, `sources/wang-2607.21521.txt`; not proof of exhaustive current literature coverage |
| Explicit LKTS(9) and two explicit LKTS(15) certificates satisfy the full definition | COMPUTED+VERIFIED | `evidence/cyclic9.txt`, `cyclic15.txt`, `denniston15.txt`; respective `.check.json`; `independent-review.md` |
| An explicit partial packing of17 disjoint resolved KTS(57)s | COMPUTED+VERIFIED | `evidence/c19-partial17.txt`, `c19-partial17.check.json`, `c19-parent-replay.json`; only17 of55 required systems |
| Checker accepts valid relabellings and rejects the tested corruptions | COMPUTED+VERIFIED | `evidence/checker-mutations.json`, 23 cases |
| Cyclic exact-cover and multiplier quotient encodings are exact within their stated models | PROVED | `proof.md` §1; `work/search_cyclic.py`, `search_multiplier.py`; independent code review |
| A nonidentity scalar/affine map fixing both infinities can preserve a cyclic-transversal STS(57)/(87) block set | REFUTED | `sources/extended-group-analysis.md` §§1–2; `evidence/group-arithmetic.json`; extended independent review |
| The 104-unit arithmetic classification and fixed-orbit counts | COMPUTED+VERIFIED | `work/group_screen.py`, `evidence/group-arithmetic.json`; independently recounted in extended review |
| Existence of an STS(87) admitting a one-fixed-point involution | REFUTED | Classical reverse-STS corollary at full strength; `proof.md` §4 |
| C19 action at57 with36 or55 fixed constituents and invariant chosen resolutions | REFUTED | `sources/c19-search-notes.md` §1; `evidence/c19-36-obstruction.json` |
| C29 action at87 with56 or85 fixed constituents and invariant chosen resolutions | REFUTED | `sources/extended-group-analysis.md` §4 |
| Staged CNF, joint-modular, C19-completion, reflection and F55 encodings are exact within their stated restrictions | PROVED | Encoding notes, frozen code, `evidence/extended-review.md`; no claim that the finite portfolios exhaust all models |
| Fixed four-hole filling alone produces either target large set | REFUTED | `sources/recursion-notes.md` §§4–5 |
| The specified compatible frame package for 57 would suffice | PROVED | `sources/recursion-notes.md` §4; existence of that package is OPEN |
| The specified coupled matching/triangle-resolution package for 87 would suffice | PROVED | `sources/recursion-notes.md` §5.4; existence of that package is OPEN |
| Faithful exact-row soundness and concrete C19/C29 mixed-development criteria | LEAN-VERIFIED, CONDITIONAL | `hmz-lean-20261014/Formal.lean`, `claims.json`;25 printed theorems, only `propext`, `Classical.choice`, `Quot.sound`; no concrete target seed package |
| Joint release-system16 construction over1,092 orbits | OPEN | `hmz-lean-20261014/evidence/joint57/result.json`: one480-second/two-worker UNKNOWN; no pair cover, resolution, or full certificate |
| Unrestricted cyclic LKTS(57), cyclic LKTS(87), and the reflection-resolved model at 57 | OPEN | `evidence/cyclic57.json`, `cyclic87.json`, `reflection57.json`: UNKNOWN |
| LKTS(57); LKTS(87); the book's universal existence conjecture | OPEN | No target certificate or complete universal proof |

## Independent review

- **First referee:** registry-selected Codex **gpt-6.1-sol, max**, read-only/ephemeral; observed identity in `evidence/review-stderr.log`. Verdict **correct**, no errors found. It verified the pinned nine inputs, independently counted all three small certificates, replayed all 23 mutation cases in memory, audited both encodings, and checked the original six proof sections. Output: [`evidence/independent-review.md`](evidence/independent-review.md); prompt, hashes, and receipt are adjacent.
- The exact proof snapshot reviewed in that first round is retained as `evidence/proof-reviewed-original.md`; its SHA256 matches the original `proof.md` entry in `evidence/review-inputs.json`. Later §§7–8 strengthen rather than alter those arguments.
- **Second referee:** the same registry-selected Codex model/effort, read-only/ephemeral, returned **correct-with-fixes** on the stronger fixed-point-divisibility/all-multiplier theorem and the auxiliary-design reductions. All corrections were applied: use the unique infinity-pair block `{r,∞₁,∞₂}` rather than silently assuming r=0; state that divisibility is not established from block-set invariance alone; restrict the fixed-subsystem bound to w≥3; explicitly require complete edge/triangle assignment and point-disjoint complements in the order-87 resolutions. It confirmed the group enumeration, all frame inventories, and both sufficient auxiliary packages. Output: [`evidence/addendum-review.md`](evidence/addendum-review.md); resolution record: [`evidence/review-resolutions.md`](evidence/review-resolutions.md).
- The literature scout's “not public/not online” claims were narrowed to **not retrieved**, and two actually accessible older PDFs were obtained and opened. No unseen automorphism generators or inaccessible theorem bodies are asserted.
- **Extended referee:** Codex **gpt-6.1-sol/max**, read-only/ephemeral, returned **correct-with-fixes**, finding no active encoding unsoundness. It accepted the stronger block-set theorem, full affine classification, C19/C29 AP obstructions, signed reflection and F55 packages, all new encodings, and Status(a)–(c). It independently reproduced the six fixed-orbit counts, C29 signatures and C19 AP counts, and counted all supplied small certificate contents. Its sole finding was missing replay/embedding inputs in the frozen snapshot. Seven inputs and original ledger entries were added under a separate supplement manifest; original37 reviewed hashes remain unchanged. Both CNF replays were then exercised from the completed snapshot by this worker. See `evidence/extended-review.md`, `extended-review-supplement.json`, and `extended-review-supplement-replay.json`. No independent execution of those two replays or the modular embedding is falsely attributed to the referee.
- **Concrete-completion referee:** Codex **gpt-6.1-sol/max** independently verified the17-system plain certificate, its exact JSON expansion and all19 translations, rejected eight corrupted in-memory certificate cases, and accepted the native/modular pair-cover equivalence, orbit anchor, and unrestricted resolution models. Verdict **correct-with-fixes**: one cancellation-grace defect was found, not a mathematical encoding error. The current controller now starts grace at cancellation, reaps before clearing its handle, never escalates to SIGKILL, and explicitly reports an unresponsive PID rather than claiming cleanup. Six virtual-clock/fake-child regressions passed both the owner and integration-worker runs; no real child or force kill was used in those tests. The live runs retain their original frozen source/model snapshots. Replay PASS is explicitly limited to reconstructed model-byte identity, not authentication of original source identity. See `evidence/completion-review.md` and `c19-paircover-lifecycle-parent.json`.

## Next steps

The exact missing object for the checked57 packing is **two resolved STS(57) bases**, each transverse to C19 triple-orbits, whose38 translates cover the1,064 remaining orbits without meeting the17 fixed constituents. The Boolean and modular pair-cover searches both timed out; they did not prove that this complement is impossible.

**Released-system16 experiment is now executed, not merely proposed:** the HMZ continuation preserved the original certificate and16 other systems, then modeled simultaneous selection of the replacement rows and two free-base pair covers over1,092 orbits. The replacement's full admissible AAA range4–9 was allowed, rather than freezing another greedy replacement. Its one bounded solve returned UNKNOWN, with no candidate. See [`hmz-lean-20261014/progress.md`](hmz-lean-20261014/progress.md) for the exact model and missing compatibility conditions. Neither this enlarged slice nor the original frozen complement is proved impossible; do not repeat the finished portfolio or refuted scalar/36-fixed models.

At87, the structurally surviving C29 pattern is **27 fixed plus two free29-orbits**; it has not been searched here. For the4v−3 recursion, the missing compatible13+42 frame package remains precisely specified in `sources/recursion-notes.md` §4. None of these remaining objects is asserted to exist.

The new Lean development criteria prove the action, exact coverage and soundness implications, not existence of the input systems. The replacement orbit-level encoding and the retained16 concrete systems have not been kernel-certified. The written fractional-incidence observation in [`hmz-lean-20261014/linear-relaxation.md`](hmz-lean-20261014/linear-relaxation.md) explains why the **unnormalized continuous** pair/class relaxation is feasible; it is not an integral construction, a Lean-certified lemma, or a statement about the symmetry-pruned solver polytope.

The declared bounded portfolio is complete and all owned processes have stopped. No target certificate or universal proof was obtained. The exact unresolved objects and executable evidence are preserved; UNKNOWN remains UNKNOWN.

