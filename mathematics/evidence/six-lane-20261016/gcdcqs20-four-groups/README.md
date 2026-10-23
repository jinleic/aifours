# gcDCQS(20⁴ : 0) — candelabra quadruple system with good colourable derived designs (math-1)

Lane owner: worker `MathMcDsqs38`. Frozen contract (read-only):
`institute/runs/six-lane-2026-10-16/screening/math-1-gcdcqs20-contract.json`
(recorded 2026-10-17T04:52:33-07:00). All earlier lanes are read-only; nothing in them is
executed from here (code is re-written or copied into `code/` with a no-deletion guard first).

## 1. Frozen target (written 2026-10-17 after 05:07:05 PDT host clock, before any search)

X = {(g, a) : g ∈ {0,1,2,3}, a ∈ {0,…,19}} (label 20g + a), groups G_g = {(g, a)}; empty stem.
Find a set A of 4-subsets such that

1. (CQS(20⁴ : 0), Tan–Zhou lines 256–266) every 3-subset of X not contained in one group lies
   in exactly one block and no 3-subset of a group lies in any block; hence |A| =
   (C(80,3) − 4·C(20,3))/4 = 19400 and block group-multiplicities are 2+2, 2+1+1 or 1+1+1+1;
2. (good colourable derived designs, lines 211–220 and 281–288) for **every** x ∈ G, the
   derived design D_x = {B∖{x} : x ∈ B ∈ A}, an incomplete STS(79, 19) with hole H = G∖{x}
   (970 triples; every pair not inside H covered once), is partitioned into r = χ′(79) = 40
   nonempty partial parallel classes (pairwise point-disjoint triples) of which exactly
   s = χ′(79) − (79 − 19)/2 = 10 avoid H (contain no point of G).

r = 40 is the source value χ′(79) = (79+1)/2 from (1.1), not a counting bound for the
incomplete design. Counting facts used only as sanity checks: a hole point lies in 30 triples
(so every non-avoiding class contains every hole point once and exactly 10 classes avoid H);
a non-hole point lies in 39 triples (missed by exactly one class); class sizes ≤ 26 resp. ≤ 20
(hole-avoiding), total slack 30·26 + 10·20 − 970 = 10. **No class-size profile, full-point
partition, translation invariance or group invariance is part of the target.**

Success = one explicit certificate listing the groups, all 19400 blocks and all 80 labelled
colourings, accepted by definition-first checkers that assume no symmetry. A restricted-group
UNSAT or a colouring timeout leaves the unrestricted question UNKNOWN.

## 2. Primary status (lane reading; parent priority audit separate)

Tan–Zhou arXiv:2503.11934v1 (local `../../../kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt`,
sha256 `df52a8f1…c8164`): §4(2) lines 1111–1113 "Find a gcDCQS(v⁴ : 0) for v = 20, 32. Apply
Corollary 2.6. If a gcDCQS(20⁴ : 0) exists, then there exists an mcDSQS(5·4ⁿ) for any integer
n ≥ 3." Corollary 2.6 (684–693): m ≡ 4, 8 (mod 12), a gcDCQS(m⁴ : 0) and an mcDSQS(m) give an
mcDSQS(m·4ⁿ), n ≥ 2 (via Construction 2.4 with a 2-RSQS*(4ⁿ) and an RDTD(3,4,m), Theorem 2.5,
then Construction 2.1). Bounded later-status check (2026-10-17 ≈05:00 PDT, web): queries
`"gcDCQS" candelabra quadruple system good colorable derived designs`, `Tan Zhou "minimum
colorable derived designs" … mcDSQS 320`, `"Steiner quadruple" derived designs chromatic index
"partial parallel classes" 2026 arXiv` returned only the source and its mirrors (arXiv.gg: 0
citations); no later gcDCQS(20⁴:0) located. The journal body is an access hole. A miss is not
novelty.

**Lane result (2026-10-17 07:08:04 PDT host clock): two CANDIDATE certificates; parent
verification pending (untrusted until then).** `evidence/gcdcqs20-a4c20/gcdcqs20_a4c20_e1s1.txt`
(sha256 `58b51b50…0a0ca`) and `…_e1s0.txt` (sha256 `52c13d6a…0d8`), from E8(iv) (the P10 ansatz on
the E1 A4 × C20 designs, KM samples 1 and 0). Both pass the stdlib checker (Python 3.9.6) and the
C checker; 21/21 retained mutations each fail for the intended reason; seeds expand
byte-identically with the stdlib; exact symmetry audit and producer replays in §4 and
`evidence/gcdcqs20-a4c20/producer-replay-receipt.json`. Correctness (checkers), priority (only the
bounded status check above; a search miss is not novelty) and significance (Tan–Zhou Cor. 2.6 /
§4(2) consequences, not re-proved here) are separate questions. Header caveat: both files say
"KM sample 0" — that is `pipeline2.py`'s loop index under `--rows-from`, not the E1 KM sample
(see the §4 provenance row). E10 (Construction 2.1 with s = 0) then gives an explicit
mcDSQS(80) candidate, `evidence/mcdsqs80-construction21/mcdsqs80_c21_A.txt` (sha256
`49f500c5…44a3`), also pending parent verification.

## 3. Frozen representation, controls, experiments, stop rules

**Certificate format `GCDCQS`** (plain text, `#` comments): `GCDCQS v n g` (stem empty),
`COLOURS r`, `HOLEFREE s`, `GROUPS` + n lines of g points, `BLOCKS` + 4-point lines, then for
every x `POINT x`, `CLASS j` (j = 0..r−1 in order) + 3-point lines. Checkers recompute r and s
from (1.1) and the gcSTS formula, check groups, blocks, exact coverage of the non-group triple
universe, and at every point: r nonempty PPCs listing the derived design exactly, exactly s
of them avoiding the hole. Two independent checkers (Python stdlib, C); mutation controls with
every mutated file retained.

**Controls (before E1).** C0a: gcDCQS(4⁴ : 0) from the read-only RDSQS(16)
`../rdsqs52/evidence/controls/r3_rdsqs16_q7_c3_sw_s0.txt` (sha256 `1521d8a8…1833`): find four
pairwise disjoint blocks covering the 16 points, use them as groups, delete them, and delete
the hole triple G∖{x} from the class containing it at each x (source gcSTS(15,3): r = 7,
s = 1, checked independently by the checkers). C0b: the lane pipeline (below) at g = 4 and
g = 8 (group A4 × C_g; v = 16, 32; r = 7/16, s = 1/4) — calibration only, never promoted.

**Groups (search choices only).** Generators act on (g, a): π₁ = (1 2 3) and π₂ = (0 1)(2 3)
on the group index (⟨π₁, π₂⟩ = A4), τ: a ↦ a+1 (mod 20) in every group. G0 = A4 × C20
(order 240, transitive, stabilizer of (0,0) = ⟨π₁⟩ ≅ C3 fixing G₀ pointwise).

**Pipeline.** Kramer–Mesner over G-orbits: columns = orbits of 3-subsets not inside a group
(types 2+1 and 1+1+1), rows = orbits of 4-subsets with no three points in a group whose
development covers every triple of each column it meets exactly once (from orbit sizes);
exact cover by kissat 4.0.4, samples by seeds + blocking clauses. Colouring of D_x at the
representative x = (0,0) invariant under R ≤ Stab(x) ∩ Stab(h), anchor h = (0,1) ∈ H:
classes 0..9 are the hole-avoiding classes (no hole point), the 30 triples through h are
forced, in sorted order of their R-orbits, into the representatives of the other class orbits
(lossless: each non-avoiding class contains exactly one triple through h, so its stabilizer is
that triple's stabilizer); the R-orbit structure of the 10 hole-avoiding classes is a
declared, recorded option. Each triple orbit gets exactly one placement; at most one triple
per (class, point). Colourings at other points: g(colouring at x) for the least g ∈ G with
g(x) = point (valid as G preserves A and the groups); the certificate lists all 80.

**Experiments (in order; every CNF, log and output retained in fresh directories).**
* E1: G0, KM inventory + ≤ 8 KM samples (cap 600 s each); colouring per sample with R = ⟨π₁⟩
  and hole-avoiding orbit structures [1,3,3,3], [1,1,1,1,3,3], [1¹⁰] (cap 300 s each), then
  R = 1 (cap 600 s) on the first sample.
* E2 (only after E1 is recorded; group and R options frozen here before running):
  G1 = A4 × A5 (A5 acting by conjugation on its 20 three-cycles; order 720, stabilizer C3×C3)
  and G2 = AGL(1,4) × AGL(1,4) × Z5 on F4 × (F4 × Z5) (order 720, stabilizer C3×C3); colouring
  with R = the stabilizer of (x, h) and hole-avoiding orbit structures recorded per run.
* E2b (frozen 2026-10-17 after 05:23:47 PDT host clock, before any E2b run): coordinates
  PG(1,19) = F19 ∪ {∞} (coordinate index 19 = ∞) with t: y ↦ y+1, m_k: y ↦ ky, j: y ↦ −1/y.
  KM probes (inventory + one kissat call, cap 300 s, ≤ 2 CPU): A4 × PSL(2,19) = A4 × ⟨t, m4, j⟩
  (order 41040, transitive, Stab(x,h) = C3 × C9 for x = (0,0), h = (0,∞)); V4 × PSL(2,19)
  (order 13680, transitive, Stab(x,h) = C9); A4 × (19:9) = A4 × ⟨t, m4⟩ (order 2052, point
  orbits {(i,∞)}, {(i,y)}; R = ⟨π₁, m4⟩ at both representatives (0,∞), (0,0) with anchors
  (0,0), (0,∞)); A4 × (19:3) = A4 × ⟨t, m7⟩ (order 684, same representatives, R = ⟨π₁, m7⟩).
  For every KM-SAT group: colourings at every point-orbit representative with R as stated and
  hole-avoiding orbit options recorded per run (cap 300 s each), transport per orbit.
* E2c (frozen 2026-10-17 after 05:30:43 PDT host clock, before any E2c run): all 20
  A4 × PSL(2,19)-invariant CQS (exhaustive KM enumeration, `runs/e2b/km_enum_a4psl19.json`) and
  ≤ 4 KM samples of V4 × PSL(2,19), A4 × (19:9), A4 × (19:3), coloured with smaller cyclic R
  fixing (x, h) = ((0,0), (0,∞)): ⟨m4⟩ (C9), ⟨π₁m4⟩ (C9), ⟨m4³⟩ (C3), ⟨π₁⟩ (C3); hole-avoiding
  orbit options for cyclic R of order 9: [1,9], [1,3,3,3], [1,1,1,1,3,3], [1¹⁰]; of order 3:
  [1,3,3,3], [1,1,1,1,3,3], [1¹⁰]; caps 300 s per colouring, ≤ 4 CPU.
* E3 (frozen 2026-10-17 after 05:40:54 PDT host clock, before any E3 run): unrestricted
  colourings (no symmetry) of the derived design at (0,0) of E1 KM samples 0 and 1 by TabuCol
  local search (`code/tabucol.c`: recolour one conflicting triple, tabu tenure 10 + U[0,10) +
  0.6·#conflicting; hole triples restricted to colours 10..39), seeds 1..3, cap 600 s CPU each;
  a cost-0 colouring is verified, transported by A4 × C20 and checked (`code/derived_io.py`).
* E4 (frozen 2026-10-17 after 05:41:28 PDT host clock, before any E4 run; motivated by
  `sources/obstruction-lemmas.md`): coordinates (u, c) ∈ {0..3} × {0..4} (label 5u + c),
  G = A4 × V4 × A5 and A4 × Z4 × A5 (V4 by XOR / Z4 on u, A5 on c), orders 2880 / 2880,
  transitive; x = (0,(0,4)), anchor (0,(0,3)); h₃ = (0 1 2) on c fixes k = 8 coordinates
  (allowed by Corollary F2). KM probe (≤ 2 samples, cap 300 s); colourings with
  R ∈ {⟨π₁, h₃⟩ (C3×C3; the 11 E2a options), ⟨π₁⟩, ⟨π₁h₃⟩, ⟨π₁h₃²⟩ (C3; [1,3,3,3],
  [1,1,1,1,3,3], [1¹⁰])}, caps 300 s, ≤ 4 CPU.
* E5 (frozen 2026-10-17 after 05:52:17 PDT host clock, before any E5 run): **hybrid colouring
  model** (`colour_model.hybrid`): non-avoiding classes R-invariant and anchored as before;
  the 10 hole-avoiding classes WITHOUT symmetry (a hole-free triple orbit is placed whole into a
  non-avoiding class orbit, or each of its triples individually into one of the 10 avoiding
  classes) — contains every R-invariant colouring, so no orbit-structure guess is needed.
  (a) E1 samples 0, 1 with R = ⟨π₁⟩, cap 600 s; (b) groups A4 × (C20 ⋊ ⟨m⟩), m ∈ {9, 11, 19}
  (orders 480; anchor = least fixed nonzero coordinate of m in G₀), ≤ 2 KM samples (cap 300 s),
  hybrid colourings with R = ⟨π₁, μ_m⟩ (C6) and ⟨π₁⟩, cap 600 s; ≤ 4 CPU.
* E6 (frozen 2026-10-17 after 05:56:47 PDT host clock, before any E6 run): the quadrupled
  cyclic SQS(20) Q(S) (`code/quadruple.py`: S from the Z20 Kramer–Mesner model, kissat seeds 0/1,
  first and second solution; Q(S) = even-label lifts of S's blocks minus the four group copies,
  {y}×{l, l⊕d} ∪ {z}×{m, m⊕d} for all pairs and d ≠ 0, and {y} × F4) — an A4 × C20-invariant
  CQS(20⁴:0) with extra S4 × Aut(S) symmetry; colour at (0,0) with R = ⟨π₁⟩ (hybrid model and
  anchored [1,3,3,3]), caps 900 s, ≤ 4 CPU.
* E8 (frozen 2026-10-17 after 06:11:01 PDT host clock, before any E8 run; parent direction of
  06:09): no new group-invariant KM/colouring models predicted UNSAT by Lemma F. Per-point
  colouring of fixed designs — the two quadrupled designs Q(S₀), Q(S₁) (`runs/e6/`) first, then
  E1 samples 0, 1 — by (i) CP-SAT (`code/cpsat_point.py`: AllDifferent per point, anchor-labelled
  classes; optional hole-fixing C3 with avoid structure [1,3,3,3]) and (ii) a dancing-links
  exact cover with secondary columns (`code/dlx_colour.c`). All designs here are invariant under
  the transitive A4 × C20, so one point per design decides the design (colouring transported by
  automorphisms); per-point outcomes are reported per design. Calibration first on the g = 8
  designs of C0b. Caps ≤ 900 s per run, ≤ 4 CPU; any UNSAT will be re-run by kissat with a DRAT
  proof before a design is discarded. OR-Tools: lane-local copy (`pydeps312/`) of the cp312
  wheels unpacked in the read-only rdsqs52 uv cache, run with the uv-managed CPython 3.12.12.
  (iii) kissat on the strengthened encoding (`--strengthen`: S1 every non-avoiding class
  contains every hole point; S2 every non-hole point is missed by exactly one class — both implied
  by counting, now explicit), for the hole-fixing C3 anchored and hybrid models; calibration
  first on the g = 8 designs (samples 2, 3 were UNKNOWN at 120 s), then the E6 and E1 designs.
  (iv) frozen after 06:27:16 PDT host clock, before use: optional ansatz `--profile P10`
  (parent-suggested; never a hypothesis): with [1,3,3,3], every non-avoiding class misses
  exactly one non-hole point (size 26) and the nine avoiding classes in 3-orbits cover all 60
  non-hole points (size 20), leaving the fixed avoiding class with 10 triples.
* E9 (frozen 2026-10-17 after 06:45:27 PDT host clock, before any E9 run): the quadrupled
  designs Q(S₀), Q(S₁) are invariant under S4 × C20 (AGL(2,2) on labels; verified,
  `runs/e9/q_s{0,1}_s4.json`). Colour D_x with R = S3 = ⟨π₁, φ⟩ ≤ Stab(x) ∩ Stab(h), φ the
  Frobenius ω ↔ ω² on labels (an involution fixing G₀ and G₁ pointwise; not excluded by Lemma F,
  which concerns order 3; the involution counting gives no contradiction). The orbit model is
  made correct for non-abelian R (placement condition g⁻¹·Stab(t)·g ≤ R_k per coset).
  Models: hybrid strengthened; anchored strengthened with avoid structures [1,3,6] and [1,3,3,3];
  caps 1200 s, ≤ 4 CPU; transport by S4 × C20.
* E10 (frozen 2026-10-17 after 07:30:21 PDT host clock, before any E10 construction; parent
  task of 07:30 — a construction, not a search): an explicit mcDSQS(80) by Tan–Zhou
  Construction 2.1 with g = 20, n = 4, s = 0 from certificate A
  (`evidence/gcdcqs20-a4c20/gcdcqs20_a4c20_e1s1.txt`, sha256 `58b51b50…0a0ca`).
  Input mcDSQS(20): Phelps' cyclic SQS(20) II.A.1 and the explicit 10-colouring of its derived
  STS(19) at 0 exactly as printed in Shi–Xia–Krotov arXiv:2212.00048v2, proof of Proposition 3
  (PDF pinned `sources/sxk/arXiv-2212.00048v2.pdf`, sha256 `5474c9fb…353c4`; pdftotext
  `sources/sxk/arXiv-2212.00048v2.txt` lines 667–684), transcribed to
  `sources/sxk/sxk_prop3_transcription.json`; the transcription is accepted only if the 16 base
  blocks generate an SQS(20) under Z20 and the 10 cells partition its derived STS(19) at 0 into
  partial parallel classes; colourings at a ∈ Z20 by translation (cells + a). Otherwise fall back
  to a lane SQS(20) with all 20 derived designs 10-coloured, verified separately.
  Rule: copy the SQS(20) onto every group G_i via a ↦ 20i + a (4 · 285 blocks added to the
  19400, total 20540); at x ∈ G_i the k-th hole-avoiding class P (in index order) of the
  certificate-A colouring at x is merged with the k-th SQS(20) colour class at x on G_i ∖ {x}
  (k = 0…9); the 30 other classes are kept; class indices as in certificate A. Output in the
  strict `MCDSQS` format of `mcdsqs38_g342_s0.txt` (`MCDSQS 80`, `COLOURS 40`, `BLOCKS`, 20540
  block lines, `POINT x` / `CLASS j` for x = 0…79, j = 0…39). Checks: exact copies of the mcdsqs38
  lane checkers (`code/mcdsqs/check_mcdsqs.py` stdlib, `check_mcdsqs.c`), mutation controls with
  retained files; deterministic builder replay byte-exact.

**Process stops (parent safety rule of ≈06:30).** Solvers use native limits (kissat `--time`,
CP-SAT `max_time_in_seconds`, TabuCol/DLX internal clocks); no `subprocess` timeouts. In this
lane no SIGKILL / `kill -9` was ever sent; two cooperative SIGTERMs were sent to my own
processes (05:23:45 kissat KM sample 2 of E1; 06:19:56 CP-SAT calibration s3 of E8), both
recorded in §4 as stopped, not as UNSAT.

**Stop rules.** First certificate passing both checkers → stop searching; pin; mutations; seed +
stdlib expander byte-exact; symmetry audit; producer replay; immediate SHA report to parent.
Restricted UNSAT/UNKNOWN stay scoped. Changed representations are frozen here before running.

**Resources.** ≤ 4 CPU, ≤ 8 GiB, checkpoints ≤ 30 min, first chunk ≤ 3 h (deadline of the round
2026-10-18 18:31:43 PDT). No deletion, no system temp files, no overwrites, nothing outside lane.

## 4. Results log

Times are file mtimes (PDT) unless marked "host clock".

| Completed | Experiment | Outcome |
|---|---|---|
| 10-17 ≈05:00 host clock | bounded later-status check (web, §2) | only the source and mirrors; no later gcDCQS(20⁴:0) located |
| 10-17 05:12:53 | C0a control (`code/control_from_rdsqs16.py`, `controls/c0a_gcdcqs4_from_rdsqs16.txt`, sha256 `436e71fa…79e5`) | groups = first parallel class of the RDSQS(16) {0,1,2,4},{3,5,6,14},{7,8,9,11},{10,12,13,15}; 136 blocks; Python and C checkers PASS (r = 7, s = 1 recomputed by both; profile 5⁶4) |
| 10-17 05:15:40 | C0a mutations (`controls/c0a_mutations_v2/`, all 19 mutated files retained) | 19/19 fail both checkers for the intended reason; 2 mutation types not constructible in this zero-slack certificate (isolated duplicate, Kempe swap removing the hole-avoiding class), recorded. `controls/c0a_mutations/` is an empty directory left by a first attempt that crashed before writing |
| 10-17 05:17:39 | C0b g = 4, A4 × C4, R = C3, avoid [1] (`runs/c0b/g4_a4c4_c3/`) | KM 12 cols/31 rows; 6 samples; colourings SAT for 2, UNSAT for 4 (≤ 0.01 s); both certificates pass both checkers (calibration only) |
| 10-17 05:20:01 | C0b g = 8, A4 × C8, R = C3 (`runs/c0b/g8_a4c8_c3/`) | KM 50 cols/290 rows SAT ≤ 0.01 s; avoid [1,3]: 2 SAT (2.7 s, 9.7 s; profile 10¹²7⁴; both checkers PASS), 2 UNKNOWN at 120 s; avoid [1,1,1,1]: 4/4 UNSAT ≤ 0.9 s (calibration only) |
| 10-17 05:20–05:23 | E1 KM, A4 × C20 (`runs/e1/a4c20_c3/`) | 324 columns (one of length 80), 5179 valid rows; sample 0 SAT 14.1 s, sample 1 SAT 137.9 s (after blocking sample 0); sample 2 kissat terminated by me (SIGTERM, 05:23:45 host clock, after 43.5 s) so that the pipeline proceeds to colour the two samples instead of drawing up to 8 — its record says UNKNOWN, which is NOT a solver timeout |
| 10-17 05:29–05:33:45 | E1 colourings, R = ⟨π₁⟩ (54–59k variables, 324 triple orbits) | samples 0 and 1 × all three hole-avoiding options: **6/6 UNKNOWN at 300 s**. Restricted model only |
| 10-17 05:29:24 | E2b A4 × PSL(2,19), R = ⟨π₁, m4⟩ ≅ C3 × C9 (`runs/e2b/a4psl19/`) | KM: 6 columns, 12 valid rows, SAT; derived design at (0,0): 40 R-orbits of triples; non-avoiding class orbits forced [3, 27]; 11 hole-avoiding options × 2 KM samples: **all UNSAT** (≤ 0.03 s). Restricted model only |
| 10-17 05:30:43 | exhaustive KM enumeration A4 × PSL(2,19) (`code/km_enumerate.py`, `runs/e2b/km_enum_a4psl19.json`) | exactly **20** A4 × PSL(2,19)-invariant CQS(20⁴:0) (labelled); every one uses row orbits of lengths 20, 1140, 1140, 3420, 3420, 10260 |
| 10-17 05:31:52 | E2b completion: all 20 A4 × PSL(2,19) CQS × 11 options, R = C3 × C9 (`runs/e2b/a4psl19_all20_c3c9/`) | 220/220 UNSAT; KM sample 20 UNSAT confirms the count 20 |
| 10-17 05:32:41–05:33:00 | E2c R = ⟨m4⟩ and ⟨π₁m4⟩ (C9) on all 20 (`runs/e2c/`) | 80/80 and 80/80 UNSAT (≤ 0.24 s) |
| 10-17 05:35:48–05:35:51 | E2a (`runs/e2a/`) | A4 × AGL(1,4) × Z5: **KM UNSAT** (122 columns, 1372 rows; no invariant CQS); A4 × A5: KM SAT (114 columns, 1537 rows), R = C3 × C3, 11 options × 2 samples: 22/22 UNSAT (≤ 0.2 s) |
| 10-17 05:35:29 | first launch of the E1 plain colouring (`runs/e1/a4c20_plain_s0.stdout`, 0 bytes) | the process ended before creating its run directory (detached subshell without nohup; presumably hung up with the tool shell); relaunched as `runs/e1/a4c20_plain_s0_r2` |
| 10-17 ≈05:45 host clock | proof note `sources/obstruction-lemmas.md` | **Lemma F** (order-3 ρ ∈ Stab(x) with fixed set F: χ′(F,L) ≤ #ρ-invariant classes ≤ r_L(p)+1 for non-hole p ∈ F), Corollary F1 (Fano fixed set ⇒ no ρ-invariant good colouring), F2 (a diagonal order-3 automorphism fixing k coordinates forces a sub-CQS(k⁴:0): k ∈ {5,11,17} impossible, k = 2 Fano). They prove every UNSAT of E2a/E2b/E2c and the A4 × AGL(1,4) × Z5 KM UNSAT (all restricted to those symmetry models) |
| 10-17 05:51:42 | E3 TabuCol, unrestricted (`runs/e3/`) | E1 sample 0 seeds 1, 2: best conflict cost 44, 41; sample 1 seed 1: 43 (≈ 9.8·10⁷ moves, 600 s each); no colouring |
| 10-17 05:51:43 | E1 plain kissat, R = 1, sample 0 (`runs/e1/a4c20_plain_s0_r2/`, 970 triple orbits) | UNKNOWN at 600 s |
| 10-17 05:52:15–05:52:17 | E4 (`runs/e4/`) | A4 × V4 × A5 (66 columns, 224 rows) and A4 × Z4 × A5 (66 columns, 212 rows): **KM UNSAT** — no invariant CQS (colourings not reached) |
| 10-17 05:56:42–05:56:47 | E5b KM + hybrid colourings with R = ⟨π₁, μ_m⟩ ≅ C6 (`runs/e5/a4c20m{9,11,19}_km/`) | m = 9 (μ fixes 4 coordinates): KM SAT (172 columns, 2145 rows), hybrid C6: 2/2 UNSAT (≤ 0.5 s); m = 11 (fixes 10): **KM UNSAT**; m = 19 (fixes 2): KM SAT (168 columns, 2325 rows), hybrid C6: 2/2 UNSAT (≤ 0.3 s). Restricted models only |
| 10-17 06:06:32 | E5a hybrid model, R = ⟨π₁⟩, E1 samples 0 and 1 (`runs/e5/a4c20_hyb_c3_s{0,1}/`, 66604 variables) | 2/2 UNKNOWN at 600 s |
| 10-17 06:01:05–06:01:07 | E6 construction (`runs/e6/q_s0.json`, `runs/e6/s1/q_s1.json`) | two cyclic SQS(20) from the Z20 KM (first and second solution, seed 0); both quadrupled designs Q(S) verified directly as CQS(20⁴:0) and as A4 × C20-invariant (99 and 94 KM rows) |
| 10-17 06:09:01 | E5b hybrid R = ⟨π₁⟩ on the m = 9 and m = 19 KM sample 0 designs (`runs/e5/a4c20m{9,19}_hyb_c3_s0/`) | 2/2 UNKNOWN at 600 s |
| 10-17 06:21:42 | E6 hybrid R = ⟨π₁⟩ on Q(S₀), Q(S₁) (`runs/e6/q_s{0,1}_hyb_c3/`, 324 triple orbits, 66604 variables) | 2/2 UNKNOWN at 900 s |
| 10-17 06:12–06:19:56 | E8(i) calibration: CP-SAT plain (no symmetry) on the g = 8 designs (`runs/e8/cal_g8_s{0,1,2}/`) | 3/3 UNKNOWN at 120 s (2 workers; ≈ 2.8·10⁶ conflicts each) although kissat with C3 solves s0, s1 in 2.7 s / 9.7 s; the 4th run (s3) was stopped by me (SIGTERM, 06:19:56) to keep ≤ 4 CPU, no result file |
| 10-17 06:17:31 | E8(ii) calibration: DLX exact cover on g = 8 designs s0, s1 (`runs/e8/cal_g8_s{0,1}_x0.tri`) | unsolved in 60 s each (best depth 117 of 148 triples, 11 restarts) |
| 10-17 06:22:47 | E8(iii) calibration: **strengthened** C3 [1,3] kissat on the g = 8 designs (`runs/e8/cal_g8_s*_str/`) | s0 SAT 0.074 s (was 2.7 s), s1 SAT 0.459 s (was 9.7 s), certificates written; s2, s3 UNKNOWN at 120 s (as before) |
| 10-17 ≈06:16 host clock | frozen lemma note `sources/lemma-F-frozen.md` + exact controls `sources/lemma-F-controls.json` (`code/lemma_controls.py`) | hypotheses H1–H4 stated exactly; scope = restricted symmetry only; controls C-F (g = 8, ρ = π₁, F ⊆ H, ρ-invariant PASS colouring exists), C-F1 (A4 × A5 sample 0: F is an STS(7) with one hole point, 11/11 recorded models UNSAT), C-F2 (m_ω of order 3 fixes k = 5 coordinates, KM UNSAT): all PASS |
| 10-17 06:43:08 | E8(iii) round 1: strengthened C3 on Q(S₀), Q(S₁) (`runs/e8/q_s{0,1}_str_{hyb,1333}/`; hybrid 70144 vars, [1,3,3,3] 55920 vars) | **4/4 UNKNOWN at 1200 s** |
| 10-17 06:45:27 | S4 × C20 invariance (`code/regroup_design.py`, `runs/e9/q_s{0,1}_s4.json`) | Q(S₀), Q(S₁) are S4 × C20-invariant (84 / 80 KM rows over S4 × C20); E1 sample 0 is not |
| 10-17 06:45:56–06:46:56 | E9 R = S3 = ⟨π₁, φ⟩ on Q(S₀), Q(S₁) (`runs/e9/q_s{0,1}_s3_{hyb,anch}/`, 267 triple orbits) | hybrid and anchored [1,3,6], [1,3,3,3]: **6/6 UNSAT** (≤ 0.015 s). Explained by Lemma Q (`sources/obstruction-lemmas.md`): a label involution fixes at most 2 non-avoiding classes, but S3-invariance forces 10 (every h-triple of Q(S) lies inside one group) — restricted symmetry only |
| 10-17 06:48:03–07:08:04 | E8(iv) strengthened C3 [1,3,3,3] + P10 on Q(S₀), Q(S₁), E1 samples 0, 1 (`runs/e8/{q_s0,q_s1,e1s0,e1s1}_p10/`, 56510 vars, 161579 clauses each) | Q(S₀), Q(S₁): UNKNOWN at 1200 s; **E1 sample 1: SAT 554.25 s, E1 sample 0: SAT 1127.45 s** (kissat 4.0.4 seed 1); decoded colourings verified at x = 0 (profile 10, 20⁹, 26³⁰), transported by A4 × C20; certificates `runs/e8/e1s{1,0}_p10/gcdcqs20_s0.txt` with the lane checker PASS |
| 10-17 07:08:22 | both checkers on both certificates | stdlib Python 3.9.6 PASS, C checker PASS (r = 40, s = 10 at all 80 points, 19400 blocks); stop rule applied — no new search after 07:08 |
| 10-17 07:08:57 | pinned (`cp -n`) to `evidence/gcdcqs20-a4c20/gcdcqs20_a4c20_e1s{1,0}.txt` with checker receipts | sha256 `58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca` (E1 sample 1), `52c13d6aa5f1acf8cc6ca5e0bb27894263443ce6486e4007afeea41c2c60d0f8` (E1 sample 0); reported to the parent 07:08 |
| 10-17 07:10:27 | retained mutations (`code/mutation_controls.py`; first pass `mutations_e1s1/` 20/20 with the Kempe swap not constructible for s = 10; generalized Kempe swap, `mutations_e1s1_v2/`, `mutations_e1s0/`) | 21/21 each, every mutant rejected by both checkers for the intended reason (incl. Kempe swap leaving 9 hole-avoiding classes) |
| 10-17 07:10:41 | seeds (`code/seed_tools.py make/expand/audit`, `*_seed.json`, 16 KB) | stdlib expansion byte-identical to both certificates; audit PASS (generators preserve blocks, transitive, colourings are least-element images) |
| 10-17 07:15:51 | exact symmetry audit (`code/equivariance_audit.py`, `*_equivariance-audit.json`) | G = A4 × C20 (order 240) preserves the block set and is transitive; Stab_G(0) = ⟨π₁⟩ (order 3) preserves the partition at 0 (π₁ fixes one avoiding class and permutes the other 39 in 3-cycles); for all 19200 pairs (g, y), g maps the partition at y onto the partition at g(y); class labels are preserved for 6400 pairs (labels are fixed only by the transport representatives) |
| 10-17 07:13–07:24 | provenance / header | both certificate headers read "KM sample 0": with `--rows-from` the producer `pipeline2.py` runs one loop iteration and prints its loop index i = 0 (`KM sample {i}`, also in the file name `gcdcqs20_s0.txt`). The rows came from `runs/e1/a4c20_c3/summary.json` samples 1 and 0 (`args.rows_from` in each run summary); the block sets are re-derived from those rows in the receipt. The pinned files are left unchanged |
| 10-17 07:24:16 | producer replay with the exact producer code (`runs/replay/orig_code/`, all 8 modules hash-equal to the 06:45:55 snapshot `runs/e9/code_sha256_at_launch.txt`), E1 sample 1 | kissat output identical apart from the command line; certificate byte-identical |
| 10-17 07:24:36 | decode-only replay (`pipeline2.py --model-from` the pinned kissat logs) | rebuilt colouring CNFs have the recorded sha256 (`9e75443e…`, `e4004b9f…`), the retained models satisfy them, both certificates byte-identical |
| 10-17 07:30:47 | full producer replay from scratch with the current code (`code/replay_km.py` KM seeds 0, 1 → `runs/replay/km/`; then `pipeline2.py` colourings → `runs/replay/col_e1s{1,0}_p10/`) | KM CNF sha256 and selected rows equal the E1 record for both samples (`a89f9732…`, `2b47c212…`); both certificates byte-identical |
| 10-17 07:30:21 | Shi–Xia–Krotov arXiv:2212.00048v2 pinned (`sources/sxk/`, PDF sha256 `5474c9fb81ca252a42a6560d7dd8adccd2136a86d4803554ade74d16a13353c4`, pdftotext sha256 `619909f8…77a1`); Prop. 3 data transcribed to `sources/sxk/sxk_prop3_transcription.json` | — |
| 10-17 07:33:18 | E10 builder (`code/build_mcdsqs80.py`, stdlib) | transcription accepted (285 cyclic blocks form an SQS(20); the 10 cells and their 20 translates partition every derived STS(19)); **mcDSQS(80) candidate** `evidence/mcdsqs80-construction21/mcdsqs80_c21_A.txt`, sha256 `49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3`, 20540 blocks |
| 10-17 07:33:29 | mcdsqs38 checker copies (`code/mcdsqs/check_mcdsqs.py` = sha256 `e2dc212d…`, `check_mcdsqs.c` = `7d04c404…`, binary `code/bin/check_mcdsqs_c`) | stdlib Python 3.9.6 PASS, C PASS (v = 80, 40 colours, 1027 derived triples per point; profile 26³⁷ 25 24 16 at every point); reported to the parent 07:33 |
| 10-17 07:33:54 | E10 controls | builder replay byte-identical (`runs/replay/mcdsqs80/`); 15/15 retained mutations (`evidence/mcdsqs80-construction21/mutations/`) rejected by both checkers for the intended reason; 4/4 corrupted transcriptions (`runs/replay/mcdsqs80/transcription_controls/`) rejected by the builder; receipt `evidence/mcdsqs80-construction21/mcdsqs80-receipt.json` |
| 10-17 07:44:13 | producer replay with the exact producer code (`runs/replay/orig_code/`), E1 sample 0 | kissat output identical apart from the command line; certificate byte-identical |
| 10-17 07:44:22 | receipt `evidence/gcdcqs20-a4c20/producer-replay-receipt.json` (`code/producer_receipt.py`) | block set of `…_e1s1.txt` = E1 KM sample 1 (KM seed 1, CNF `2b47c212…` = base + blocking clause of sample 0), of `…_e1s0.txt` = E1 KM sample 0 (seed 0, CNF `a89f9732…`); 8/8 replays byte-identical (decode-only, full solver current code, full solver original code, stdlib seed expansion; × 2 certificates); hashes of inputs, code and binaries |
