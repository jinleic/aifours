# RDSQS(52) — six-lane round 2026-10-16 (math-1, second target)

Lane owner: worker `MathKirkman`. Frozen contract:
`institute/runs/six-lane-2026-10-16/screening/math-1-rdsqs52-contract.json`
(recorded 2026-10-16T22:41:21-07:00). The previous math-1 lane
`../kirkman57/` is preserved unchanged.

## 0. Headline (2026-10-17, host clock)

**An explicit RDSQS(52) was constructed and independently checked** (candidate; not peer
reviewed; priority audit and hostile review by the parent pending). Certificate
`evidence/rdsqs52-z52m23/rdsqs52_z52_m23.txt`, sha256
`7ae0a828b5af08b4bd9b423564981d85e3703886553638024fdc812f564989a6` (5525 blocks; all 52
resolutions explicit). Checks: lane Python checker PASS, lane C checker PASS, parent's
independent definition-first checker VALID, 15/15 intended-reason mutations (both lane
checkers), exact symmetry audit PASS, byte-exact regeneration from a 6 KB seed, byte-exact
re-run of the search. Construction: cyclic SQS(52) invariant under Z52⋊⟨23⟩ (⟨23⟩=⟨9⟩×⟨−1⟩,
order 6), derived design at 0 resolved ⟨23⟩-invariantly, translated to all points
(`sources/construction-z52m23.md`). Representation R1 (frozen first), experiment family E3.

## 1. Frozen target (written 2026-10-16 ≈22:45 PDT, before any search)

Find a set B of 4-subsets ("blocks") of X={0,…,51} such that

1. every one of the C(52,3)=22,100 three-subsets of X lies in exactly one block
   (so |B|=5,525: B is an SQS(52)); and
2. for **every** x∈X the derived design `B_x={b∖{x} : x∈b∈B}` (425 triples on
   X∖{x}, an STS(51)) has a resolution: a partition into 25 classes of 17
   pairwise disjoint triples.

Success = an explicit labelled certificate listing all 5,525 blocks **and all 52
resolutions explicitly**, accepted by a direct definition-based checker that
assumes no symmetry. Even when symmetry is used in the search, the certificate
contains every resolution. A cyclic-only non-find, UNSAT under a prescribed
group, or a timeout is **not** nonexistence of RDSQS(52).

## 2. Primary status

* Tan–Zhou, arXiv:2503.11934v1 (2025-03-15), §4(1): "Find more examples of
  mcDSQS(v)s, for example, an mcDSQS(38) and an RDSQS(52) (the smallest unknown
  mcDSQS(6n + 2)s and the smallest unknown RDSQS(6n + 4)s, respectively)."
  Read-only cache `../../../kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`
  (sha256 `df52a8f1…c8164`) lines 1108–1110; definition of derived design and RDSQS at lines 78–82.
* Parent screen (`institute/runs/six-lane-2026-10-16/screening/math-finite-target-screen.md`):
  Tan–Zhou arXiv:2512.22754v1 Thm 2.8 still lists OLKTS exceptions 51, 69, 75;
  no solution claim found in arXiv, OpenAlex, openai/math, EulerSolve, Zenodo.
  Not reopened by this lane yet; to be rechecked before any promotion.
* Known families (Liu–Lei 2023 Thm 4.4 / Lemma 4.2, Tan–Zhou 2025, FDH) do not
  reach 52 = 51+1 (51 = 3·17; 17 not a product of family elements; 25≢7 mod 12).

## 3. Baseline

SQS(52) exists (Hanani). RDSQS(v) is known for v∈{4,10,16,22,28,34,40,46,58,…};
52 is the smallest open order. The open increment is simultaneous
resolvability of all 52 derived STS(51), not SQS existence.

## 4. Frozen representation and attack protocol

**R1 (frozen first):** cyclic group G=Z52 acting by translation (optionally
extended by a multiplier subgroup M≤U(52), each M a separately recorded
experiment). Kramer–Mesner: columns = G-orbits of triples, rows = G-orbits of
4-sets that cover every triple of the triple-orbits they meet exactly once
(independently enumerated; counts recomputed, not taken from the scout).
Derived design at 0: SAT resolution with 25 classes, lossless class labelling
by the 25 triples through one fixed point; optional M-invariant class
structures. Resolutions at x are the translates by x of the resolution at 0;
the certificate writes all 52 explicitly.

**Experiments (in order; each with recorded seeds, CNF hashes, caps):**

* E0: orbit inventory at v=52 and KM satisfiability (cyclic).
* E1 calibration (same code): cyclic pipeline at known orders v=10, 22, 28, 34, 40
  (and v=16 KM only); fraction of sampled SQS whose derived design at 0 resolves
  within the cap.
* E2 main: up to 100 cyclic SQS(52) samples (kissat seeds 0…99 with blocking
  clauses), resolution cap 120 s each, ≤4 parallel workers.
* E3: multiplier-extended groups (M = ⟨−1⟩, ⟨25⟩, ⟨29⟩, …), invariant or
  unrestricted resolutions; each recorded separately.
* If R1 is concretely blocked (KM UNSAT or no resolvable derived design within
  the frozen budget), freeze a new representation (rotational Z51∪{∞}, or
  F25×{0,1}∪{∞0,∞1} with x↦ax+b) in this README **before** searching it.

**Checker and controls (before E2):** `code/check_rdsqs.py` (stdlib, direct
definition). Positive controls: trivial RDSQS(4), RDSQS(22) transcribed from
Liu–Lei (arXiv 2210.06214 Lemma 2.5, published data), pipeline-found
certificates at known orders. Intended-reason mutations: triple coverage,
per-point resolution, missing-point completeness, plus duplicated block,
wrong point label, triple moved between classes, non-derived triple.

**Resources:** ≤4 CPU workers, ≤8 GiB RSS target, outputs/checkpoints at least
every 30 min, first cycle ≤2 h (deadline of the round: 2026-10-18 18:31:43 PDT).
No monolithic CNF dumps beyond per-run models (each < 20 MB).

### R2 — frozen 2026-10-16 before 23:58:54 PDT (mtime of the first R2 run summary), after the R1 evidence in §5

**Why R1 is concretely blocked (as a decision procedure, not as mathematics):**
the frozen E2 decision step (unrestricted anchored resolution SAT, 120 s) fails
on *known-resolvable* designs of this size — two randomly relabelled
constituents of the verified LKTS(57) gave UNKNOWN after 300 s each
(`code/kts57_calibration.py`, `code/runs/kts51_calib/`). So E2 UNKNOWNs carry no
information, and the cyclic pipeline reproduced no known RDSQS at v=22, 28, 34
(E1). The symmetric E3 variant (Z52⋊⟨9⟩, R=⟨9⟩) gave 24/24 UNKNOWN at 120 s.

**R2 (parent-proposed, adopted):** classical doubling of a cyclic SQS(26) on Y=Z26:
points (y,i)∈Y×F2 (encoded y+26i); blocks (i) the 8 even-parity lifts of every
SQS(26) block, (ii) `{(x,0),(x,1),(y,0),(y,1)}` for every pair {x,y} (8·650+325=5525).
Z26×Z2 acts regularly, so one derived STS(51) (at (0,0)) is resolved and transported.
That derived design contains the derived STS(25) of the SQS(26) on layer 0, which
forces every parallel class to have exactly 4 internal and 13 cross triples.
Multipliers M≤U(26) of the SQS(26) fix (0,0); resolutions are sought invariant
under R≤M with the class structure forced by the R-orbits of triples through the
anchor (0,1) (`code/doubling_pipeline.py`, `code/mult_pipeline.py:sym_model`).
Calibration first at a known order: Y=20 (v=40, RDSQS(40) known), then Y=26 with
M ∈ {⟨7⟩ (order 12), ⟨5⟩ (4), ⟨9⟩ (3), ⟨25⟩ (2), ⟨17⟩, ⟨23⟩ (6), trivial}.
Caps: ≤4 workers, resolution cap 120–600 s per model, KM(26) samples by kissat seeds
with blocking clauses; checkpoints ≤30 min. A non-find is restricted to R2.
Source-family check: the 2u doubling is not among the RDSQS families listed by
Liu–Lei Thm 4.4 / Tan–Zhou §3 for 52 (screen §1); no claim that doubling-based
RDSQS constructions are new.

### Resolution-engine calibration (2026-10-17, output mtimes 00:16–00:30 PDT, parent-approved ≤60 min)

Inputs: three randomly relabelled constituents of the verified LKTS(57) (known
resolvable STS(57)) and Liu–Lei's derived STS(21) (`code/dump_designs.py`,
`code/runs/engine_calib/`). Results on the known-resolvable STS(57) `kts57_sys0`:
kissat default/`--sat`/`--unsat`/`--plain` UNKNOWN at 300 s; CP-SAT 9.15
(AllDifferent per point, 4 workers) UNKNOWN at 300 s; TabuCol-style local search
(`code/tabures.c`, 20M iterations) best cost 35. All engines solve Liu–Lei's STS(21)
(kissat 0.04 s, CP-SAT 0.11 s, tabu 68k iterations). **Conclusion: no generic
resolution engine decides resolvability at this size in minutes; resolutions must
come from symmetric models with a large class-symmetry group R (as in LKTS(57)/(87),
where |R|≥9 made models solvable in seconds).**

### R3 — frozen 2026-10-17 at ≈00:31 PDT host clock (parent-proposed), before any R3 search

Points F_q×{0,1}∪{∞0,∞1} (id x+q·j, ∞0=2q, ∞1=2q+1), v=2q+2. G generated by the
translations and the multiplications x↦cx (c in a subgroup C≤F_q*), acting
identically on both copies and fixing ∞0, ∞1; optional copy/infinity swap σ and
(q=25) Frobenius. KM over G-orbits; resolutions at the point-orbit
representatives ∞0 (stabilizer ⊇ F_q⋊C) and (0,0) (stabilizer ⊇ C), each sought
invariant under a chosen subgroup R of the stabilizer, class structure forced by
the R-orbits of triples through an R-fixed anchor; transport by G.
Calibration at known orders q=7 (v=16), q=13 (v=28, q≡1 mod 12 like 25), q=19
(v=40), then q=25 (v=52) for C of orders 24, 12, 8, 6, 4, 3, 2. Caps as before;
UNSAT/UNKNOWN are scoped to R3 with the stated C, σ, R.

### R3γ — frozen 2026-10-17 ≈01:22 PDT host clock, before any R3γ search

R3 at q=25 with C=⟨ω⟩ (order 3) and swap σ (the only C allowed by KM, see §5),
plus a **local** symmetry γ imposed on the derived design D at (0,0) only (γ need
not extend to the SQS): γ fixes ∞0, ∞1, (0,1), commutes with ω, has order 3, permutes
the 16 ω-cycles of F25*×{0,1} with m three-cycles (cycle maps ω-equivariant, shifts
summing to 0 mod 3) and acts on each fixed cycle as ω^k. Every element of
R=⟨ω,γ⟩≅C3×C3 must have a fixed set of size 3, 9, 15 or 21 in D (sub-STS orders);
with m=4 this holds iff the twists of the 4 fixed cycles take each value an even
number of times; m=2 / m=0 analogously (counts even, ≤6). Implementation: for every
3-subset t of D's points, x[orbit(t∪{(0,0)})] ⟺ x[orbit(γt∪{(0,0)})] added to the KM
CNF (a forced false where the orbit is not a valid row). Resolution at (0,0)
R-invariant (anchor ∞0), at ∞0 translation-invariant; transport by G. Random γ from
seeded generators; each γ recorded. A non-find is scoped to R3γ with the recorded γ.

## 5. Results log

Times are file mtimes (PDT) unless marked "host clock".

| Completed | Experiment | Outcome |
|---|---|---|
| 10-16 22:47:22 | E0 Z52 inventory (`code/runs/e0_inventory_v52.json`) | 425 triple orbits; quad orbits 5200×52, 12×26, 1×13; 24 AP rows invalid; scout counts confirmed |
| 10-16 22:47:59 / 22:48:36 | checker + controls; RDSQS(22) mutations | Liu–Lei RDSQS(22), RDSQS(4) PASS; 15/15 mutations as intended |
| 10-16 22:47–23:33 | E1 cyclic calibration (`code/runs/e1_cyclic_v*`) | v=10 found; v=16 KM UNSAT; v=22 8/8 UNSAT (then 400/400 non-resolvable D0, `e1_enum22`); v=28 3 UNSAT/5 UNKNOWN; v=34 8 UNKNOWN; v=40 KM UNKNOWN 600 s |
| 10-16 23:34:25 | KM probes Z52⋊⟨9⟩,⟨25⟩,⟨−1⟩ | SAT ≤2.5 s |
| 10-16 23:58:05 | E3 Z52⋊⟨9⟩, R=⟨9⟩ | 24/24 UNKNOWN at 120 s |
| 10-16 23:51:55 | KTS(57) calibration (plain SAT) | known-resolvable STS(57): UNKNOWN at 300 s ×2 |
| 10-16 23:58:54 – 10-17 00:16:03 | R2 doubling batches | R∋−1: UNSAT (Lemma R2-a, `sources/model-lemmas.md`); R=⟨9⟩ UNKNOWN; Y=20 plain UNKNOWN |
| 10-17 00:08:26 | plain cyclic KM v=52 | UNKNOWN at 600 s |
| 10-17 00:16–00:30 | engine calibration | kissat presets, CP-SAT, TabuCol fail on known STS(57) |
| 10-17 00:18:40 | PSL(2,25)-family KM probes | all no rows / UNSAT |
| 10-17 00:3x–00:5x | R3 calibration and q=25 batch | RDSQS(16) (q=7) and RDSQS(40) (q=19, C9) reproduced; q=25: even C KM UNSAT, C3 finite point UNKNOWN (also 4×1500 s) |
| 10-17 01:1x–01:3x | R3γ scan, independent-copy and twisted PSL probes | 450 γ: KM UNSAT; probes UNSAT |
| 10-17 01:3x–01:5x | PartialCol / LNS engines; C3 calibration at v=40 | fail on known STS(57); C3 model of known-resolvable v=40 design: SAT 34 s / UNKNOWN 600 s, C9: 0.05 s |
| 10-17 ≈01:5x | multiplier-subgroup sweep (`code/runs/e0_km52/mult_sweep.json`) | KM SAT for orders 2,3,4,6,12 groups avoiding 27; UNSAT/UNKNOWN for groups with 27 |
| 10-17 ≈02:0x | E3 with R ∋ 25 (orders 4, 6, 12) | 12/12 UNSAT each (models restricted to those R) |
| 10-17 02:07 | **E3 Z52⋊⟨23⟩, R=⟨23⟩, anchor 26** (`code/runs/e3c_v52_m23_r23/`) | **12/12 SAT (0.05–3.3 s), 12/12 certificates PASS**; sample 0 pinned |
| 10-17 02:1x | C checker, mutations, seed/expander, symmetry audit, search replay | all PASS / byte-identical |
| 10-17 02:30:05 | control: Z52⋊⟨−1⟩, R=⟨−1⟩ only (order 2) (`code/runs/e3c_v52_m51_r51/`) | 11 UNKNOWN, 1 UNSAT at 120 s — ⟨−1⟩ alone not enough for the solver |
| 10-17 02:30:07 | control: Z52⋊⟨7⟩ (order 12), R=⟨25⟩ (`code/runs/e3c_v52_m7_r25/`) | 12/12 UNSAT (another R∋25 model) |

Stopped cooperatively at 02:08: the R3 long batch (`code/runs/r3q25_c3_sw_long2`, partial).
Restricted-model UNSAT/UNKNOWN results above are scoped to their models; none is a
nonexistence statement.

## 6. Exploratory extension (parent-approved ≤30 min probe; NOT promoted)

Host-clock window ≈02:13–02:27 PDT 2026-10-17. Same pipeline (`code/mult_pipeline.py`).

* **RDSQS(76):** Z76⋊⟨3⟩ (⟨3⟩ of order 18, contains −1 and order-9 multipliers), anchor 38,
  class orbits [1,9,9,9,9]: 6/6 KM samples resolved (0.05–0.95 s), 6/6 certificates PASS.
  Pinned exploratory copy `evidence/exploratory-ext/rdsqs76_z76_m3_sample0.txt`
  (sha256 `2f75b37c0439aa9f9c57861505a2e865997dd02249349b708880916d477a75aa`); seed
  `rdsqs76_z76_m3_sample0_seed.json` (byte-exact via `code/expand_rdsqs_seed.py`); both lane
  checkers PASS (C build for v≤128: `code/check_rdsqs_v128.c`); symmetry audit PASS; 15/15
  mutations as intended (`mutations76/`; first run preserved as `mutations76_wrong_c_binary/`,
  which used the 64-point C build). Orbit data `rdsqs76_orbit_description.{json,md}`.
* **RDSQS(70):** Z70⋊⟨59⟩ (order 6, same shape as 52) KM UNKNOWN at 600 s; KM probes:
  ⟨29⟩, ⟨57⟩, ⟨9⟩, ⟨3⟩ UNSAT (all contain the involution 29 fixing 14 points), ⟨11⟩ and ⟨−1⟩
  UNKNOWN at 120 s (`code/runs/ext_km70/`). No RDSQS(70) found; scoped to these models.
* Open status of 70/76: see `sources/ext-70-76-status.md` (no lane-read source names them
  explicitly; inference from Tan–Zhou arXiv:2512.22754v1 Thm 2.8(2) via the parent screen).
