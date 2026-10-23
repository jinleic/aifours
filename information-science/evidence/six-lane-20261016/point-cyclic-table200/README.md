# Lane info-2: point-cyclic resolvability of 2-(v,4,1) designs, v = 4 (mod 12), 100 < v <= 200

Owner: worker `InfoCyclic100`. Contract (read-only):
`institute/runs/six-lane-2026-10-16/screening/info-2-point-cyclic-table200-contract.json` (recorded
2026-10-17T04:10:32-07:00). Lane opened 2026-10-17 04:16:44 PDT (host clock, `notes/lane-opened.txt`). Deadline
2026-10-18 18:31:43 PDT. Prior lanes (`point-cyclic88`, `point-cyclic100`), review files and sources are read-only;
files from them are copied, never moved.

Status label (contract): DERIVED-OPEN table completion. Topalova-Zhelezova (Axioms 15 (2026) 762, p.11) name only 88 as
the smallest undetermined order; no source names the larger orders verbatim. This round settled 88 (no) and 100 (yes).
A completed table would extend the source's frontier statement. It is not an explicitly named open target. No novelty,
priority or "first" claim is made anywhere in this lane.

File discipline (contract): no file is deleted or moved. Every script writes only into fresh output paths, refuses to
overwrite, and has no automatic cleanup (no temporary directories, no removal calls).

## 1. Frozen contract (written 2026-10-17 04:16-04:40 PDT, BEFORE any block search in this lane)

### 1.1 Exact target, per order
For each v in {112, 124, 136, 148, 160, 172, 184, 196} there is one separate finite claim: does there exist a 2-(v,4,1)
design together with a resolution that has an automorphism permuting the points in one v-cycle (TZ Definition 5; binding
as in the reviewed 88/100 lanes)? Possible outcomes per order:
* EXISTS: a full certificate (all blocks and classes) passes the direct checker, with a seed and a producer replay.
* NONEXISTENT: a decisive theorem whose hypotheses are checked, or a complete written proof, or a certified exhaustive
  search over a proved-complete reduction with two implementations.
* UNKNOWN: anything else. Restricted misses, timeouts and type-restricted searches are UNKNOWN, never nonexistence.

### 1.2 Reduction used (proved in `GENERAL-REDUCTION.md`, written before any search; untrusted until parent review)
The v = 100 reduction is generalized to every v = 4n, v = 4 (mod 12):
* Theorem A' (necessity): a point-cyclic resolution, labelled so that sigma = +1, is determined by a type (t, K) and
  base blocks.
  * t is the length of the unique class orbit with short blocks: t | n and t = 1 (mod 4). t = 1 is T1, t = n is T2,
    otherwise T3.
  * K is a multiset of divisors k of n with 4k <= n (class orbits of length 4k without short blocks).
  * (E): t + 4 sum(K) = r.
  * The base blocks satisfy the residue partition conditions (R1)/(R2) and the difference condition (D).
* Theorem C' (sufficiency): the converse construction.
* Corollary E: n | lcm({t} u {4k}).

`code/type_table.py` enumerates the admissible types (receipt `evidence/type-table-200.{txt,json}`, run 04:2x before
any search).

### 1.3 Sources and exact quotes (text layers by `pdftotext -layout`; line breaks and hyphenation normalized)
* [TZ] Topalova-Zhelezova, Axioms 15 (2026) 762. Local copy `../point-cyclic88/sources/axioms-15-00762.pdf` (SHA-256
  d5170670…9608); text layer `sources/tz2026-axioms-15-00762.layout.txt` (SHA-256 c9a3f526…9693).
  * TZ-GMJ (p.2): "An important necessary condition says that if a 2-(v,k,1) design possesses point-cyclic resolutions
    and v/k is a prime number, then v/k ≡ 1 (mod k(k − 1)) [5]."
  * TZ-LM (p.2): "The main existence result for cyclically resolvable Steiner 2-designs with block size 4 is derived in
    [6]. It states that there exist cyclically resolvable 2-(v,4,1) designs for v = 4q, where q is a product of primes
    of the form 12s + 1, and s is odd."
  * TZ-CONV (p.2): "In the present paper, when we talk about cyclically resolvable designs, we mean designs with
    point-cyclic resolutions."
  * TZ-OPEN (p.11): "That is why v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v, 4, 1)
    designs has not yet been determined."
* [GMJ] Genma-Mishima-Jimbo, J. Combin. Des. 5 (1997) 177-187, Gifu author preprint `sources/gmj1997-preprint-a0801798.pdf`
  (SHA-256 0963ccc0…3f11; Wayback URL in the 88 priority audit). The published version may differ.
  * GMJ-DEF (p.2): "If a resolvable design has a non-trivial automorphism σ of order v = |V| which preserves the
    resolution, that is, if R^σ = {R_1^σ, ..., R_r^σ} = R holds, then it is called cyclically resolvable with respect
    to σ ... In this paper, we shall treat a Steiner 2-design which is cyclic with respect to an automorphism
    σ : i ↦ i + 1 (mod v) and which is also cyclically resolvable with respect to the same automorphism σ."
    With σ = +1 on Z_v this is TZ's point-cyclic resolution, and TZ cite it as [5].
  * GMJ-2.1 (p.3): "Theorem 2.1 When v is a prime, if a cyclically resolvable cyclic (kv, k, 1)-BIB design exists, then
    v ≡ 1 (mod k(k − 1)) holds." (GMJ's v is our n.)
  * GMJ-3.4/3.5 (pp.10-11), recursive constructions: "Corollary 3.4 Let u_i ≡ 1 (mod k(k − 1)) for i = 1, ..., n and
    u_2, u_3, ..., u_n be primes. If there are cyclically resolvable cyclic (ku_i, k, 1)-BIB designs for any i, then
    there exists a cyclically resolvable cyclic (ku_1u_2···u_n, k, 1)-BIB design with properties (P1) and (P2)."
    "Corollary 3.5 Let u be prime such that u ≡ 1 (mod k(k − 1)). Then the existence of a cyclically resolvable cyclic
    (ku, k, 1)-BIB design implies the existence of a cyclically resolvable cyclic (ku^m, k, 1)-BIB design with
    properties (P1) and (P2) for any integer m." Theorem 3.2 (p.8) needs two such designs and a difference matrix.
* [MJ] Mishima-Jimbo, Discrete Math. 211 (2000) 135-152, Gifu author preprint `sources/mj2000-preprint-a0801873.pdf`
  (SHA-256 24f26261…771d), restating Mishima-Jimbo 1997 (Congr. Numer. 123, not read).
  * MJ-4.1 (p.13): "Lemma 4.1 If there exists a CRCB(kuv, k, 1) of type (T3) such that its regular short block orbit is
    arranged in a v × u array, then uv ≡ 1 mod k − 1 and v ≡ 1 mod k hold."
  * MJ-4.2 (p.13): "Lemma 4.2 If a CRCB(kv, k, 1) of type (T2) exists, then v ≡ 1 mod k(k − 1) holds."
  * MJ-4.3 (p.14): "Theorem 4.3 Let u be relatively prime to w. If there are (i) a CRCB(kuv, k, 1) of type (T3) such
    that its regular short block orbit is arranged in a v × u array, (ii) a DM(w, k + 1, 1) and (iii) a CRCB(kw, k, 1)
    of type (T2) such that each length of resolution orbits not containing any block from its regular short block
    orbit is relatively prime to uv, then there exists a CRCB(kuvw, k, 1) of type (T3), in which its single regular
    short block orbit is arranged in a vw × u array."
  * MJ-4.4 (p.15): "Corollary 4.4 If there are (i) a CRCB(kv, k, 1) of type (T2), (ii) a DM(w, k + 1, 1) and (iii) a
    CRCB(kw, k, 1) of type (T2) such that each length of resolution orbits not containing any block from its regular
    short block orbit is relatively prime to v, then there exists a CRCB(kvw, k, 1) of type (T2)."
* [LMM] Lam-Miao-Mishima, J. Statist. Plann. Inference 95 (2001) 245-256, Gifu author preprint (copy of the text layer
  `sources/lmm2001-preprint.layout.txt`; PDF `../point-cyclic100/sources/lmm2001-preprint-a0801799.pdf`, SHA-256
  3c5f0740…7826), quoting Mishima-Jimbo 1997:
  * LMM-2.1 (p.4): "Lemma 2.1. Let v = p^α for a prime number p and assume that p is relatively prime to k. Then there
    does not exist any CRCS(2, k, kv) of type (T1)."
* [8p] This round's reviewed theorem, `../point-cyclic88/PROOF.md` (r2), Section 6, and parent verdict
  `review/point-cyclic88-parent-verdict.md`: "Corollary (same proof). For every prime p = 11 (mod 12), no 2-(8p,4,1)
  design has a point-cyclic resolution." Written proof with Claude ACCEPT and Codex ACCEPT; v = 88 itself is
  Lean-checked.
* Access holes (unchanged from the 88/100 audits): the Lam-Miao 1999 full text [TZ ref. 6] (publisher 403; known only
  through TZ-LM and its zbMATH review), Mishima-Jimbo 1997 [Congr. Numer. 123], Kageyama-Miao 1996, the Handbook of
  Combinatorial Designs (2nd ed.), Chang-Miao 2002, and other paywalled bodies. A missing family is not proof of
  openness; any of these may already settle a table entry.

### 1.4 Status table (BEFORE any search; T = theorem read here, R = own reduction of `GENERAL-REDUCTION.md`)
| v | n = v/4 | decided by a checked theorem? | own type analysis (Theorem A', Corollary E) | status entering the search |
|---|---|---|---|---|
| 112 | 28 = 2^2·7 | No. GMJ-2.1 needs n prime. LMM-2.1 needs n a prime power. TZ-LM needs n a product of primes 12s+1. MJ-4.3/4.4 and GMJ-3.4/3.5 build only T2/T3 designs, and T1 is forced here | T2 impossible (n = 0 mod 4). T3 impossible (no divisor t = 1 mod 4 with 1 < t < 28). T1 forced with K = {7,2} or {7,1,1}: class orbit lengths 1, 28, 8 or 1, 28, 4, 4 | OPEN |
| 124 | 31 prime | **Yes: NONEXISTENT** by GMJ-2.1 (= TZ-GMJ): n = 31 prime and 31 = 7 (mod 12) | no admissible type (agrees) | decided |
| 136 | 34 = 2·17 | No. The 8p theorem needs p = 11 (mod 12), and 17 = 5. GMJ-2.1 and LMM-2.1 do not apply (34 is neither a prime nor a prime power). MJ-4.1 allows T3 (u = 2, v = 17). MJ-4.3 would need a CRCB(68,4,1) of type T2, which MJ-4.2/GMJ-2.1 exclude (17 is not 1 mod 12) | T1 excluded (lcm of {4,8} is not a multiple of 34). T3 forced with t = 17 (O_S: 17 classes with 2 short blocks each); K in {2,2,2,1}, {2,2,1,1,1}, {2,1,1,1,1,1}, {1^7} | OPEN |
| 148 | 37 prime | **Yes: EXISTS** by the Lam-Miao family (TZ-LM; 37 = 12·3+1 with s = 3 odd). Primary [6] not read; quoted by TZ | T2 forced, K = {1,1,1}: 9 X blocks and 3 Y blocks (seed format of the v = 100 lane with q = 37) | decided (cited); an explicit certificate is planned as a check |
| 160 | 40 = 2^3·5 | No. GMJ-2.1 and LMM-2.1 do not apply. Lam-Miao: 5 is not of the form 12s+1. MJ-4.3 with u = 8 and vw = 5 needs a T2 or T3 ingredient at 20 or 32 points, and no 2-(20,4,1) or 2-(32,4,1) design exists (20, 32 are not 1 or 4 mod 12) | T2 impossible (n = 0 mod 4). T1: 12 types. T3 with t = 5: 27 types (list in `evidence/type-table-200.txt`) | OPEN |
| 172 | 43 prime | **Yes: NONEXISTENT** by GMJ-2.1: 43 = 7 (mod 12) | no admissible type (agrees) | decided |
| 184 | 46 = 2·23 | **Yes: NONEXISTENT** by the 8p theorem: 184 = 8·23 with 23 = 11 (mod 12) | no admissible type (agrees) | decided |
| 196 | 49 = 7^2 | No. Lam-Miao: 7 is not 12s+1. LMM-2.1 excludes only T1 (7^2, gcd(7,4) = 1). MJ-4.2 allows T2 (49 = 1 mod 12). GMJ-3.4/3.5 and MJ-4.4 would need a design at 28 = 4·7, impossible by GMJ-2.1. MJ-4.3 produces only T3 designs, and T3 is impossible at 196 (no t = 1 mod 4 with 1 < t < 49 divides 49) | T1 excluded (lcm of {4,28} is not a multiple of 49; also LMM-2.1). T3 impossible (7 = 3 mod 4). T2 forced, K = {1,1,1,1}: 12 X blocks with residues mod 49 partitioning Z_49 \ {0}, and 4 transversals mod 4 | OPEN |

Here "decided" means decided by a theorem whose quoted hypotheses are checked above. The cited theorems were read in
author preprints or through TZ's quotation, as recorded. Our own reduction (R) reproduces every nonexistence entry
independently, but it is unreviewed. It is a consistency check, not the basis of these entries.

### 1.5 Representations (frozen)
* Seed format `PC-SEED v` (strict):
  * line 1 `PC-SEED v`, then `SHORT t`;
  * (t-1)/4 lines `X a b c d`;
  * then for each k of K, in nonincreasing order of k: a line `GROUP k` followed by k lines `Y a b c d`;
  * integers in [0, v), each block line strictly ascending, single spaces, final newline, nothing else.
* Expander `code/pc_expand_general.py` (stdlib): checks t | n, t = 1 (mod 4), k | n, (R1), (R2) and (D) directly in Z_v.
  It builds R(t, K, X, Y) of Theorem C' and writes the strict `POINT-CYCLIC-RESOLUTION v 4 r n` certificate: blocks
  sorted inside classes, classes sorted, class indices 0..r-1. It does not decide acceptance.
* Direct checker `code/pc_check.py`: a byte-identical copy of `../point-cyclic100/code/pc_check.py` (SHA-256
  8b29ab30…18d5), which is general in v and independent of any base-block structure. Acceptance per order: PASS of
  this checker on the full certificate, seed SHA-256, producer replay and expansion replay byte-identical, mutation
  controls rejected. The parent supplies further independent checkers.
* R1 search (`code/pc_tabu.c`, C, deterministic per seed via splitmix64; wall clock only for limits): a tabu search for
  one type (t, K).
  * State: for each group (the O_S group with modulus t > 1, and one group per k with modulus 4k), every residue of the
    group (Z_t \ {0}, or Z_{4k}) has a block label (4 residues per block, so (R1)/(R2) hold by construction) and a
    height j in [0, v/modulus). The point is residue + modulus·j.
  * Cost: sum over difference classes {d, -d} of Z_v (d != 0) of max(0, count - cap), with cap 0 for d in H = <n> and
    1 otherwise. Cost 0 <=> (D).
  * Moves: change one height; exchange two residues between two blocks of one group (heights travel, or stay in
    place); exchange the heights of two residues of one block. Best non-tabu move with aspiration, and random
    perturbation after a stall.
  * R1 imposes no normalization; it is a heuristic, and misses are UNKNOWN.
* R2 (only if needed): an exact solver over the same reduction with written normalizations. It is not written yet; its
  representation and normalizations will be frozen here before it is run.

### 1.6 Controls (before any claim)
* Positive search controls, which must be found: v = 52 (t = 13, K = {1}), v = 64 (t = 1, K = {4,1}), v = 100 (t = 25,
  K = {1,1}). Each found certificate must pass `pc_check.py`, and its class orbit lengths must match the type.
* Negative search controls, which must NOT be found within 60 s: v = 16 (t = 1, K = {1}) and v = 40 (t = 5, K = {2} and
  {1,1}). Both have admissible types but no point-cyclic resolution (no cyclic 2-(16,4,1) design exists; TZ state that
  52 is the smallest order). A miss calibrates nothing about nonexistence; a find would reveal a bug.
* Expander/checker: the published v = 52 (LMM Appendix A) and v = 64 (TZ pp.6-7) data and the accepted v = 100 seed,
  converted to `PC-SEED`, must expand to PASS certificates. Seed and certificate mutations must fail.

### 1.7 Stop rules and resources
* At most 4 concurrent processes and 8 GiB; host-clock checkpoints in Section 3 every 30 min or less; chunks of at most
  3 h.
* Chunk 1:
  * controls;
  * 196: up to 4 seeds × 30 min;
  * 148: up to 2 seeds × 10 min (explicit check of the cited existence);
  * 112: both types, up to 2 seeds × 30 min each;
  * 136: all four types, 1 seed × 30 min each;
  * 160: types in this order, 1 seed × 15 min each:
    * T3 t=5: K = {10,2}, {10,1,1}, {8,4}, {2^6};
    * T1: K = {10,2,1}, {10,1,1,1}, {8,5}, {5,5,2,1};
    * then the remaining 31 types in the order of `evidence/type-table-200.txt`.
* An order stops at its first seed whose expansion passes `pc_check.py`. No abundance runs.
* Every candidate is reported to Main immediately, with SHA-256 values.
* Orders without a certificate after chunk 1: write the R2 representation into this README first, then decide.

## 2. Status
Status 2026-10-17 05:50 PDT, per order. Each order is a separate finite claim. Existence entries rest on the raw
certificates alone (direct checking of every pair, every class and the +1 action), NOT on the unreviewed general
reduction of `GENERAL-REDUCTION.md`, which only guided the search.

| v | status | basis | evidence |
|---|---|---|---|
| 112 | EXISTS | lane certificate. Parent definition-first verification PASS (three independent checkers, own seed expansion byte-identical, semantic mutations rejected) | type T1, K = {7,1,1}; `certs/v112/pc112_t1.{seed,cert}`; producer replay `evidence/replay/v112-r1` REPLAY_PASS |
| 124 | NONEXISTENT | published prior theorem: Genma-Mishima-Jimbo 1997, Theorem 2.1 (n = 31 prime, 31 = 7 mod 12); read in the author preprint; hypotheses checked | Section 1.4 |
| 136 | EXISTS | lane certificate; parent verification PASS as for 112 | type T3, t = 17, K = {1^7}; `certs/v136/pc136_t3.{seed,cert}`; replay `evidence/replay/v136-r1` REPLAY_PASS |
| 148 | EXISTS (cited) | published prior theorem: the Lam-Miao 1999 family (37 = 12·3+1, s = 3 odd), as quoted by Topalova-Zhelezova 2026; the Lam-Miao body was NOT read; no lane certificate (the explicit check was stopped at Main's direction) | Section 1.4 |
| 160 | EXISTS | lane certificate; parent verification PASS as for 112 | type T3, t = 5, K = {10,2}; `certs/v160/pc160_t3.{seed,cert}`; replay `evidence/replay/v160-r1` REPLAY_PASS |
| 172 | NONEXISTENT | published prior theorem: GMJ 1997, Theorem 2.1 (n = 43 prime, 43 = 7 mod 12) | Section 1.4 |
| 184 | NONEXISTENT | OUR written 8p corollary of this round (`../point-cyclic88/PROOF.md` r2, Section 6; Claude ACCEPT and Codex ACCEPT on the 88 proof and corollary). This is NOT published prior art | Section 1.4 |
| 196 | EXISTS | lane certificate; parent verification PASS (Main 05:4x: three independent routes, own seed expansion byte-identical, three semantic mutations rejected) | type T2, t = 49, K = {1^4}; `certs/v196/pc196_t2.{seed,cert}`; replay `evidence/replay/v196-r1` REPLAY_PASS |

* Novelty and priority: the parent's bounded priority scout (PcTablePriority) found no earlier point-cyclic
  construction or exclusion for 112, 136, 160 or 196. That is a bounded miss with access holes: the Lam-Miao 1999 body,
  Fuji-Hara-Miao-Shinohara 2002, theses and the Handbook were not read, and they matter most at 196. No novelty or
  priority claim is made.
* The apparent Chang-Miao 2002 reference may be mis-attributed. Results on 1-rotational designs, or on
  class-transitive cyclic actions, are NOT point-cyclic results in the source's sense (TZ Definition 5, TZ-CONV).
* Wording (Main, 04:39): "OPEN" in Section 1.4 means "not decided by any theorem read here". The source status of
  these orders stays DERIVED-OPEN / access-limited.
* The Lean existence package for 112, 136, 160 and 196 is in Section 2.4. Main asked for no further searches or
  samples without a newly frozen parent target.

### 2.1 R1b representation (frozen 2026-10-17 04:52 PDT, before its first run)
`code/pc_tabu2.c` is a byte copy of `code/pc_tabu.c` (the pinned producer of the 112, 136 and 160 witnesses, which
stays unchanged) with two edits: a header comment, and a FOCUSED neighborhood. Each iteration evaluates only the moves
that change at least one residue lying in a pair whose difference class is over capacity: M1 on such residues; M2/M3
pairs containing one; M4 pairs containing one. State, cost, move types, tabu rules, aspiration, perturbation, output
format and exclusive file creation are unchanged; it is again a heuristic, and its misses are UNKNOWN. Source
SHA-256 15f5574a…3215, `bin/pc_tabu2` (cc -O2). Planned use: v = 196 only (Main: continue only 160/196), first a
speed comparison on the v = 100 control (seeds 1-3), then up to 4 × 30 min of v = 196 as part of the remaining chunk-1
budget for 196 (4 seeds × 30 min in total for R1 and R1b together, extended only with a written reason).

### 2.2 R1c representation (frozen 2026-10-17 05:18 PDT, before its first v = 196 run)
`code/t2_sat.py` (SHA-256 below in the log) encodes the T2 type (t = q = n, K = {1^((q-1)/12)}) as CNF for kissat 4.0.4.
It uses CRT coordinates (height x mod 4, residue x mod q):
* one-hot block and height variables for the X residues, with at most 4 residues per block;
* one-hot residues for the Y points at heights 0..3;
* equivalence-defined "same block" and "height difference" variables, X/Y candidate literals per difference class,
  and an exactly-one constraint per class;
* the short difference is forbidden in Y pairs.

This is exactly (R1), (R2) with k = 1, and (D) of GENERAL-REDUCTION.md for the T2 type. The normalizations below lose
no solution.
* N1: in each X block, the smallest residue has height 0. Adding q·c to a block keeps its residues, shifts its heights by
  c (since q = 1 mod 4) and keeps its orbit.
* N2: X blocks are ordered by their smallest residues (relabelling).
* N3: every Y block has its height-0 point at residue 0. Adding 4c keeps the heights; 4c runs through all residues mod
  q, and the orbit is unchanged.
* N4: Y blocks are ordered by the residue of their height-1 point, strictly (relabelling; these residues differ by (D)).

Decoding: the model is turned into a PC-SEED (`t2_sat.py decode`). Acceptance as always: expansion and
`pc_check.py`. Calibration (05:17): q = 13 SAT in 0.4 s and q = 25 SAT in 28 s; both decoded seeds expand to PASS
certificates (`runs/r1c-dev/check/`). Planned: one kissat process on q = 49, time limit 3600 s, seed 1. A SAT answer is
a candidate. An UNSAT answer would NOT be used for any nonexistence claim without a separate certified-proof plan (DRAT
checking and review of the encoding and normalizations), to be frozen here first. UNKNOWN on timeout.

### 2.3 R1d representation (frozen 2026-10-17 05:30 PDT, before its first run)
`code/t2_twostage.c` (SHA-256 1667f1ef…15c9, `bin/t2_twostage`, cc -O2) is a two-stage search for the T2 type at
v = 4q. It uses CRT coordinates, and the difference classes are {(d,e), (-d,-e)} with e != 0. A Y block (one point per
height) covers no class with d = 0, exactly 2 classes with d = 2 and exactly 4 classes with d = 1, 3. Hence the X
blocks must cover all classes with d = 0, exactly (q-1)/2 - 2C classes with d = 2, and no class twice.
* Stage 1: a tabu search over the X group only (residue partition by construction, heights mod 4; moves and tabu rules
  as in R1). The cost is the collisions, plus the uncovered d = 0 classes, plus |#X pairs with d = 2 - ((q-1)/2 - 2C)|.
* Stage 2: when stage 1 reaches cost 0, an exact and complete search for the C Y blocks.
  * Each Y block is normalized (N3 of 2.2) to residue 0 at height 0, i.e. (0, b, c, d) at heights 0..3.
  * It covers the d = 1 classes of b, c - b, d - c and -d, and the d = 2 classes of c and d - b.
  * Every candidate inside the uncovered classes is enumerated, and an exact cover is sought by backtracking.
  * On failure, stage 1 continues after a random perturbation.

A heuristic overall; misses are UNKNOWN. Planned: calibration on q = 13 and q = 25, then up to 2 processes × 60 min on
q = 49.

### 2.4 Lean existence package (`lean-kernel/`, final form `PCTableKernelR2/`)
Requested by Main: a combined Lean pass for 112, 136, 160 and 196 that reuses the accepted generic proof.
* Reuse:
  * `PC100Kernel/Target.lean` (definitions only) and `PC100Kernel/Check.lean` (Boolean checker `certCheck`,
    data-independent `sound_of_check`, cycle lemmas) are byte copies of the accepted v = 100 package. `replay.py`
    checks their SHA-256 against `../point-cyclic100/lean-kernel/manifest.json`.
  * `lean_env.sh`, `build_module.sh` and `lean_source_scan.py` are byte copies too.
* New per order, generated from one template:
  * `gen_lean.py` writes `Data<v>.lean`: the pinned raw certificate verbatim, preceded by
    `set_option maxRecDepth 16384 in` (an elaborator resource limit).
  * `gen_cert.py` writes `Cert<v>.lean`, which evaluates `certCheck` in four kernel declarations (range, pairs, classes,
    shift) and derives `PC100.Target v`, `PC100.TargetShift v` and `PC100.TargetCounts v`. It also writes `Audit.lean`.
  * `gen_controls.py` writes `Controls.lean`, which is not used by any root:
    * at every order, a point swap between disjoint blocks of classes 0 and 1: `certCheck` false and
      `¬ IsDesign241`;
    * at 112, the relabel 1<->2: range, pairs and classes pass, shift fails, and the block set is not shift-invariant.
  * `gen_controls.py` also writes `ControlFail.lean`, which must fail to build.
* Roots (`PCTable.Audit`), each with axioms {propext, Classical.choice, Quot.sound} only: `root<v> : PC100.Target v`,
  `root<v>_shift : PC100.TargetShift v`, `root<v>_counts : PC100.TargetCounts v` and
  `root<v>_cycleType : (PC100.shift v).cycleType = {v}`, for v = 112, 136, 160, 196.
* Binding (`audit_binding.py`, stdlib): BINDING_AUDIT_PASS. It checks literal = certificate, the Theorem C' expansion of
  every seed byte-identical to its certificate, the Lean objects equal to the certificates' blocks and classes, and that
  5 corruptions are rejected for the intended reasons.
* `manifest.json` SHA-256 1f15f540625ed8e83ccda8cf8d2698d61e47e50c5864b99bd4e3f8a62d156897. Clean replay
  `replay-worker/result.json` (SHA-256 7afaf1fdc9759c0c915e6223bce01dbe71051e5c10ab3020c87bae32eda7595c):
  REBUILD_AND_FRESH_KERNEL_REPLAY_PASS, 05:45:24-05:53:21.
  * Generated modules regenerated byte-identically; source scan clean; audit log byte-identical to the pinned expected
    output; ControlFail fails as required.
  * leanchecker --fresh: Audit 175 s / 5.3 GB; Controls 187 s / 5.4 GB.
  * Peak build RSS: Cert196 at 5.3 GB. One Lean process at a time.
* Trust limits: lean and leanchecker come from one toolchain (not Comparator). The raw-file and seed bindings are the
  external stdlib audit, not Lean theorems.
* Superseded drafts, kept and not part of the package:
  * `PCTable/`: the 160 literal failed with maximum recursion depth;
  * `PCTableKernel/`: a doc comment placed before `set_option ... in` is a parse error.

  Their partial build outputs are under `build/`, `logs/`, `build-final/` and `logs-final/`. The log-truncation
  incident is recorded in Section 3.

## 3. Log (host clock, PDT)
- 04:16:44 lane created; GMJ 1997 and MJ 2000 author preprints fetched from the Wayback URLs of the 88 priority audit
  (`sources/`, SHA-256 above); TZ and LMM text layers copied from `../point-cyclic100/sources/` (byte-identical).
- 04:2x `code/type_table.py` run (`evidence/type-table-200.{txt,json}`); `GENERAL-REDUCTION.md` and this frozen section
  written; no block search run before this point.
- 04:19-04:24 type table run at 04:19 (file mtime), reduction and freeze written; freeze receipts 04:24:00 and 04:24:18
  (`notes/freeze-receipt.txt`; the second one repairs an edit that had misplaced the 196 row before any search). The
  two "04:2x" labels above are these times.
- 04:24-04:27 tooling: `code/pc_expand_general.py`; `code/pc_check.py` (byte copy, SHA-256 8b29ab30…18d5);
  `code/cert_to_seed.py`; `code/pc_tabu.c` (SHA-256 b9f0bf98…ae35, `bin/pc_tabu` cc -O2). Round trip
  certificate -> seed -> expansion is byte-identical for the accepted v = 100 certificate (971f…), the TZ v = 64
  certificate (d8c1…, type T1 K = {4,1}) and all six LMM v = 52 certificates (`controls/roundtrip-v1/`).
- 04:26:59-04:29:26 positive search controls (`runs/controls-r1/`): v = 52 (t = 13, K = {1}) and v = 64 (t = 1,
  K = {4,1}) found by seeds 1-3 in < 0.1 s each; v = 100 (t = 25, K = {1,1}) found by seeds 1-3 in 77, 3 and 66 s.
  All 9 expand to certificates that pass `pc_check.py` with the expected class orbit lengths
  (`controls/search-positive-r1/check-receipt.json`).
- 04:29:35-04:30:35 negative search controls, 60 s each, no find (as required): v = 16 (t = 1, K = {1}), v = 40
  (t = 5, K = {2}) and v = 40 (t = 5, K = {1,1}); best costs 1, 1, 1.
- 04:30:4x chunk 1 started (`runs/chunk1/`, 4 processes, 1800 s each): v = 196 seeds 1-2 (t = 49, K = {1,1,1,1});
  v = 112 type K = {7,2} seed 1 and type K = {7,1,1} seed 1.
- 04:30:58-04:31:45 v = 112, type K = {7,1,1}, seed 1: FOUND at iteration 1595892 (47 s). Expansion PASS
  (`runs/check-v112-r1/`), class orbits 1, 4, 4, 28. Pinned at 04:32:01: `certs/v112/pc112_t1.{seed,cert}` (SHA-256
  9836c503…d4b1 and 96265b66…440d). The K = {7,2} run was stopped at 04:32:01 by the stop rule (best cost 1).
  Main was notified at 04:32.
- 04:32:19-04:32:46 v = 136, type t = 17 with K = {1^7}, seed 1: FOUND in 24 s. A concurrently started run with
  K = {2,2,2,1} also FOUND, in 27 s. Both expansions PASS (`runs/check-v136-r1/`). The first one is pinned at 04:33:10:
  `certs/v136/pc136_t3.{seed,cert}` (SHA-256 7f505783…da5b and 61874100…5c56). The other is kept only under `runs/`.
  Main was notified at 04:33.
- 04:33:24 v = 148 (positive check, t = 37, K = {1,1,1}) and v = 160 (t = 5, K = {10,2}) started. At 04:39 Main asked to
  continue only 160/196 and the 112/136 replays, so the 148 run was stopped at 04:39:33 (best cost 1, about 370 s).
  148 therefore stays decided by the cited Lam-Miao theorem only, with no lane certificate.
- 04:39:38-04:40:50 producer replays (`evidence/replay/v112-r1`, `v136-r1`): fresh `cc -O2` build of `code/pc_tabu.c`;
  seed and certificate byte-identical; checker PASS (REPLAY_PASS for both).
- 04:41 scheduling deviation, recorded: the 160 types are tried with types that have many k = 1 groups first (here
  t = 5, K = {2,1^10}). The reason is that such types were found fastest at 112 and 136, while t = 5, K = {10,2}
  showed no find after 5 min. The frozen list of types and the time per type are unchanged; only the order changes.
- 04:43:24 v = 160, type t = 5, K = {10,2}, seed 1: FOUND at iteration 10414711 (600 s). Expansion PASS, class orbits
  5, 8, 40 (`runs/check-v160-r1/`). Pinned: `certs/v160/pc160_t3.{seed,cert}` (SHA-256 d81b4af2…19f7 and
  8928dd9b…a923). Main was notified at 04:43.
- The parallel run t = 5, K = {2,1^10} stopped at 04:43:40 with best cost 8 throughout. This agrees with a counting
  obstruction for that type, recorded here as an observation and not used for any claim. Differences divisible by 4
  outside H number 36. Transversals give none, the X block gives at most 12, and the k = 2 group gives at most 8.
- 04:43:44-04:53:45 v = 160 producer replay (`evidence/replay/v160-r1`): REPLAY_PASS (seed and certificate
  byte-identical, iteration 10414711).
- 04:44 v = 196 seed 3 (R1) started; 04:52 R1b frozen (Section 2.1).
- 04:53:51-04:54:44 R1b calibration (`runs/r1b-calib/`): v = 100 seeds 1-3 found in 2, 14 and 20 s; v = 136 type
  {1^7} seeds 1-2 found in 10 and 6 s. That is about 3× more iterations per second than R1.
- 04:54:5x v = 196 R1b seed 1 started (`runs/chunk1b/`). Checkpoint 04:55: v = 196 R1 seeds 1-3 are at best cost 1;
  CPU use is 4 processes.
- 05:00:58 v = 196 R1 seeds 1 and 2 ended without a find (1800 s each, best cost 1, about 20.4M iterations each).
- 05:01:03-05:01:06 mutation controls (`controls/mutations-v{112,136,160}/mutations-report.json`): all as intended for
  the three certificates. Point change and point swap gave FAIL D2; block move FAIL R1; duplicate FAIL D1; non-affine
  relabeling FAIL C1; affine relabelings (3x+7, x+1, -x) PASS; 7 format corruptions FAIL F. On K_6 the cyclic
  factorization gave PASS and the non-cyclic one FAIL C2. Three seed mutations were refused by the expander.
- 05:01 budget extension for v = 196, with reason: 196 is the only order of the table left undecided, and R1b is about
  3× faster per iteration. R1b seeds 2 and 3 get 30 min each (`runs/chunk1b/`), in addition to R1 seeds 1-3 and R1b
  seed 1.
- 05:13:56 v = 196 R1 seed 3 ended without a find (1800 s, best cost 1). R1b seeds 1-3 were at best cost 1 at 05:14
  (about 29.5k iterations per second).
- 05:16-05:17 R1c (`code/t2_sat.py`, SHA-256 f0b76b6a…92e9) written and calibrated. q = 13 gave SAT in 0.4 s and q = 25
  SAT in 28 s; the decoded seeds expand to PASS certificates (`runs/r1c-dev/check/check-receipt.json`). R1c frozen
  (Section 2.2) at 05:17:47. The README insertion was made with a one-off scripted text replacement rather than the
  editor; no other text was changed.
- 05:18 kissat on q = 49 started (`runs/r1c-196/`; CNF SHA-256 f27b8ab1…3c4a: 23200 variables, 234535 clauses; seed 1,
  --time=3600). CPU: R1b seeds 1-3 plus kissat, 4 processes.
- 05:24:50 and 05:31:24 v = 196 R1b seeds 1-3 ended without a find (1800 s each, about 52M iterations each, best
  cost 1). 05:25 kissat `--sat --seed=2` on q = 49 started (`runs/r1c-196/q49-sat-s2.*`, --time=3500).
- 05:30 R1d frozen (Section 2.3). 05:31:29-05:31:34 R1d calibration (`runs/r1d-calib/`): q = 13 seeds 1-3 found in
  0.01-0.02 s; q = 25 seeds 1-3 found in 2.4, 0.4 and 1.0 s, after 2950, 479 and 1274 stage-1 hits. All 6 seeds expand
  to PASS certificates (`runs/r1d-calib/check/check-receipt.json`).
- 05:32 R1d on q = 49 seeds 1-2 started (`runs/r1d-196/`, 3500 s each). CPU: 2 × R1d and 2 × kissat. Checkpoint 05:32:
  196 still has no certificate; 112, 136 and 160 are pinned and replayed.
- 05:31:41-05:34:45 v = 196, R1d seed 1: FOUND in 184 s, after 55490 stage-1 hits; on average 81.6 stage-2
  candidates per hit. Expansion PASS, class orbits 49, 4, 4, 4, 4 (`runs/check-v196-r1/`). Pinned at 05:34:55 as
  `certs/v196/pc196_t2.{seed,cert}` (SHA-256 27095204…6d26 and 0828bf23…d8db5).
- 05:34:55 the siblings were stopped by the stop rule, and their outputs are preserved:
  - R1d seed 2;
  - kissat seed 1 (R1c), after 17 min;
  - kissat --sat seed 2, after 9 min.

  Both kissat runs gave no answer, which is UNKNOWN. Main was notified at 05:35.
- 05:35:09-05:35:11 mutation controls for v = 196 (`controls/mutations-v196/`): all as intended.
- 05:35:15 v = 196 producer replay started (`evidence/replay/v196-r1`, `code/replay_twostage.py`).
- 05:36 Lean preparation (`lean-kernel/`):
  - generic modules `PC100Kernel/{Target,Check}.lean` and the scripts `lean_env.sh`, `build_module.sh`,
    `lean_source_scan.py`, copied byte-identically from `../point-cyclic100/lean-kernel/` (SHA-256 checked against its
    manifest);
  - `gen_lean.py` and `gen_cert.py` generate `PCTable/Data{112,136,160,196}.lean`, `Cert{112,136,160,196}.lean` and
    `AuditAll.lean`, all from one template;
  - `PCTable/Audit.lean` (generated at 05:33 for 112/136/160 only) is kept; the combined roots are in `AuditAll.lean`;
  - a fresh regeneration of all four Data modules (`scratch/regen-check/`) is byte-identical.

  Builds started (one Lean process).
- 05:38:33-05:38:42 INCIDENT, recorded: a rebuild started into the default log directory truncated the draft build
  logs `lean-kernel/logs/Data112.build.{log,time}` before it was stopped at 05:38:42. The draft Data112 build record
  (from the 05:36 tool output) was: 2.61 s real, 1969586176 bytes maximum RSS, exit 0, empty log. No other file was
  touched: the draft oleans under `lean-kernel/build/PCTable/` are intact, and that run had produced no
  `build/PCTableKernel/` output. From now on every Lean build uses fresh `PC100_BUILD`/`PC100_LOGS` directories.
- 05:38:34 v = 196 producer replay (`evidence/replay/v196-r1`): REPLAY_PASS. Seed and certificate byte-identical;
  stage-1 hits 55490 as in the original run.
- 05:37:09 the draft `PCTable/Data160.lean` failed to elaborate (maximum recursion depth on the 2120-block literal). The
  final package is regenerated into `lean-kernel/PCTableKernel/`:
  - every literal is preceded by `set_option maxRecDepth 16384 in` (an elaborator resource limit, not a proof
    setting);
  - `certCheck` is evaluated in four kernel declarations per order (range, pairs, classes, shift) and assembled by
    `simp only [certCheck, Bool.and_eq_true]`.

  `PCTable/` stays on disk as the superseded draft; it is not part of the final package.
- 05:4x Main (IRC): all four existence orders now have parent definition-first verification. The next step is the
  combined Lean package and replay receipts, not more searches.
- 05:39-05:41 `lean-kernel/PCTableKernel/` (first regeneration) did not parse: in `Data112`, `set_option ... in` came
  after a doc comment. Fixed generators wrote `lean-kernel/PCTableKernelR2/` at 05:42, the final package.
- 05:43:12-05:45:08 worker build into fresh `build-r2/` and `logs-r2/`: all modules PASS, and ControlFail fails as
  required. 05:45:20 `lean-kernel/manifest.json` written. 05:45:24-05:53:21 clean replay `lean-kernel/replay-worker/`:
  REBUILD_AND_FRESH_KERNEL_REPLAY_PASS (Section 2.4). Main was notified at 05:53.
- 05:50 the status table was rewritten at Main's request: it now separates published prior theorems (GMJ 1997; Lam-Miao
  1999, cited only), our own 8p corollary (184) and the lane certificates. Existence rests on the raw certificates.
- 05:54:07 README final for this cycle; lane manifest evidence/MANIFEST.sha256 generated next (last write of the cycle).
