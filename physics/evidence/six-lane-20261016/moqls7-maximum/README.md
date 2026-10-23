# Six-lane phys-2 (sixth target): determine M(7) — does a non-classical set of 3 MOQLS(7) exist?

Lane: `physics/evidence/six-lane-20261016/moqls7-maximum/` (owns `sources/ code/ evidence/ explore/ review/
archive/`). Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-moqls7-maximum-contract.json` (SHA-256
21b1b38bf82e2923518ce8fd1a8885f38427d2a07ac968fbec53e0150744d372, recorded 16:50:58 PDT). Screen:
`screening/phys-next-screen-v3.md` (3975fba4…19a). Read-only: the AME lane, `moqls7-problem16/`, `moqls8-problem16/`,
all parent run directories. Accepted baseline: 2 ≤ M(7) ≤ 3 (`review/moqls7-parent-verdict.md`, a39911fd…a3ff2).

## 0. Frozen protocol (written 2026-10-17 from 16:59:37 PDT, before any computation in this lane)

### 0.1 Sources and definitions
Pinned copies in `sources/` (SHA-256 equal to the old lane's pins):
- Ball–Simoens arXiv:2607.12933v2: PDF 2d60d45f…21afe, layout text df1d8b14…4219 (the contract's pin);
- Egan–Wanless arXiv:1406.3681v2: PDF f01b494f…27e0, layout text 4d0d009e…1965.

Definitions (Ball–Simoens §2.2–2.3, layout LF90–116; re-read for this lane):
- A QLS(7) is a 7 × 7 array of unit vectors of C^7 whose rows and columns are orthonormal bases (ONBs).
- Two QLS Ψ, Φ are orthogonal if {ψ_ij ⊗ φ_ij} is an ONB of C^7 ⊗ C^7.
- Set isotopy consists of entry phases, simultaneous row/column permutations, and a separate unitary per square.
- A set is classical if, up to isotopy, all entries lie in one fixed ONB.
- M(n) is the largest t such that a non-classical set of t MOQLS(n) exists (LF29–31).

Consequences used throughout (to be proved in `review/LEMMAS.md`):
- **(C0)** A set is classical iff every square is classical, since isotopy (iii) acts per square. A QLS(7) is
  classical iff its entries span exactly 7 projective rays. Hence a set is non-classical iff some square has more
  than 7 rays (contract wording).
- **(C1)** A QLS Ψ is orthogonal to a classical square L iff, for every symbol a, the entries of Ψ on the cells with
  L = a form an ONB.

### 0.2 Target and readings
- **Target:** does a non-classical set {Ψ1, Ψ2, Ψ3} of 3 MOQLS(7) exist (arbitrary complex entries)?
  - Positive: an exact witness, i.e. all 147 vectors in exact algebraic form, with an exact verification of the
    row/column ONBs, the three pairwise 49-element tensor ONBs and the ray count. This gives M(7) = 3.
  - Negative: an unrestricted nonexistence proof covering exactly 1, 2 or 3 non-classical squares. This gives
    M(7) = 2.
- **Case names** (contract): K1, K2, K3 = exactly 1, 2, 3 non-classical squares. With (C1):
  - **K1** ⟺ a 4-net of order 7 (two classical squares, i.e. a pair of MOLS(7), plus rows and columns) carrying an
    ONB-assignment (a unit vector at each of the 49 points, with every one of the 28 lines an ONB) that is
    non-classical. This is symmetric in the 4 parallel classes, so net isomorphism (Egan–Wanless paratopy) is the
    right equivalence: 7 classes (Table 6, k = 2), 5 of them maximal (Table 5).
  - For a maximal 4-net every ONB-assignment is non-classical, because a classical one is a 5th parallel class.
  - **K2** ⟺ a 3-net (one classical Latin square) carrying two orthogonal non-classical ONB-assignments.
  - **K3** ⟺ three mutually orthogonal non-classical QLS.
- Partial results are reported only as partial: e.g. "no K1 witness on net X in ansatz Y" is a search miss, not
  nonexistence.

### 0.3 Fresh necessary conditions (derived anew for 3 squares; nothing imported from the old 4-square proof)
- **(W)** Put every square in standard form, with row 0 equal to |0⟩, …, |6⟩. At each cell (i, j) with i ≥ 1:
  - the three supports are pairwise disjoint, by rule #3, which holds for every pair of the three squares;
  - each support avoids j, by rule #2 (column ONB);
  - so the weights w1 + w2 + w3 ≤ 6 with each wi ≥ 1, i.e. wi ≤ 4, and a weight-4 entry forces weight 1 in the
    other two squares. Weight 2 and 3 entries, and weight-2 non-classical squares, remain allowed.
- **(K1 frame)** For an ONB-assignment on a 4-net in the frame of one line ℓ (that line equal to the standard basis):
  every point p ∉ ℓ has support avoiding the 3 coordinates of the points where the other 3 lines through p meet ℓ.
  So it has at most 4 coordinates.
- **Pattern conditions** for any orthogonal pair (u, v) of vectors: their supports never meet in exactly one
  coordinate. On every ONB line, each coordinate is covered by some support; a coordinate covered exactly once forces
  that entry to have weight 1. On every line the supports form a unitary pattern.
- **Lemma 10** (Ball–Simoens, used through its printed proof): an assignment with all weights ≤ 2 in some fixed basis
  can be classicalized, preserving every orthogonality. Hence a K1 assignment on a maximal net has, in every line's
  frame, an entry of weight ≥ 3.

### 0.4 Route (frozen order; search choices are not exclusions)
**Phase A — K1 positive search.**
- A1 nets:
  - The 2 extendable classes: the harmonic and the equianharmonic 4-subnets of AG(2,7). These are to be verified
    against Egan–Wanless: |par| 2352 and 3528 give 360 + 240 = 600 = 342480 − 341880 reduced sets (Theorem 3.2).
  - The 5 maximal classes: generated in this lane, then source-bound by computing |par| for each representative and
    checking Σ 846720/|par| = 341880 (Table 5, k = 2).
- A2 searches, per net:
  - (a) numerical exploration of ONB-assignments, which is never evidence;
  - (b) structured ansätze: a Weyl–Heisenberg-equivariant fiducial unbiased to the 4 MUBs of the net's directions
    (Desarguesian nets), and automorphism-equivariant assignments;
  - (c) support-pattern SAT under §0.3 feeding exact reconstruction.
- A3: any numerical zero becomes an exact algebraic reconstruction and an exact verification (§0.5).

**Phase B — K2 and K3 positive search.** Numerical 3-MOQLS(7) search with a non-classicality requirement; the
Theorem-6/ring/orthomorphism and pandiagonal constructions as search choices only.

**Phase C — negative direction**, only if Phase A and B searches fail and time remains. A written reduction plus
pattern SAT covering K1, K2 and K3 completely, with two encodings, drat-trim-checkable proofs and the parent route.
No transfer of the old 4-square Theorems A/B/F3/P4 or forced-weight-3 claims.

### 0.5 Controls and verification
- **Exact controls:**
  - the published non-classical pair (Corollary 7 / Example 15 at q = 7: Ψ(f) with the order-3 subgroup H, plus one
    Φ(m));
  - classical triples from AG(2,7);
  - a genuinely non-classical small QLS (the 4 × 4 example of source §2.4);
  - intended mutations.
- Every necessary-condition encoding must admit all matched genuine controls before production.
- A witness checker must be exact and definition-first: row/column ONBs, 3 × 49-element tensor ONBs and the ray
  count, computed from the vectors. A second, separately written checker is required before any claim.

### 0.6 Stop rules
- Chunks are at most 3 h, with a change of representation after a calibrated concrete obstruction and no blind
  reruns.
- UNKNOWN or a timeout is never UNSAT. A numerical near-zero is never a witness.
- Any exact candidate is reported to the parent immediately with its full SHA-256, and no claim is made before
  parent verification.

### 0.7 Resources and permissions
- At most 4 busy processes, 8 GiB aggregate RSS, 10 GiB of new data, and a global free floor of 12e9 B (17.69e9 B
  free at 16:59). Chunks at most 3 h, checkpoints at most every 30 min, host-clock labels.
- Python: `../depolarizing/env/bin/python -B` (numpy, scipy, sympy) and `/usr/bin/python3` (stdlib). Also clang,
  CaDiCaL and kissat.
- Native solver limits or SIGTERM with a bounded wait only. No SIGKILL, no `subprocess.run(timeout=…)`, and no native
  children under eval deadlines.
- No deletion (retire to `archive/`), no overwriting of old evidence, no `/tmp`, no publication or contact, no Git
  mutation, no paid API, no global config.

## 1. Status (checkpoints)
- 16:59:37 lane created; sources copied, with SHAs verified equal to the pins.
- 17:20:57 the 7 classes of 4-nets of order 7 were found (`evidence/nets7_classes.json`); the orbit sums equal the
  Egan–Wanless totals.
- 17:51:49 **K1 excluded (lane result, awaiting parent verification)**: `review/K1-THEOREM.r1.md` (b702b021…8767).
  - Maximal nets: no ONB-assignment at all.
  - Harmonic net: only classical assignments.
  - Equianharmonic net: the only non-classical pattern has weight 4 everywhere off the frame line, and an exact
    7-relation phase cycle refutes it.
  - Two independent encoders were run (CaDiCaL and kissat); every DRAT proof gave `s VERIFIED` under drat-trim. The
    controls include the genuine non-classical Ψ(f) and the 4 × 4 QLS.
  - Reduction: K2 and K3 remain, with every non-classical square having an entry of weight ≥ 3.
  - Next: the K2 pattern SAT with a free classical square, then K3.
- 18:30:13 status:
  - The single-frame K2 (W3) and K3 (W3+sym) CNFs ended UNKNOWN at their 1800 s CaDiCaL caps. This is not
    evidence either way.
  - Parent steering: until parent verification finishes, the lane runs at most 2 busy processes and at most 4 GiB.
  - New frame-free encoder `code/gram_enc.py`, with Gram-support variables, consistency in every line frame, and
    the tensor ONB written exactly as edge-disjoint Gram supports. Its controls passed
    (`explore/gram/gram_controls_v1.json`).
  - Minimal-counterexample reduction: every non-classical square is heavy in every ONB basis (Lemma 10 in an
    arbitrary basis + Theorem K1). So the frame-free heavy condition holds on every own line.
  - Running: the K3 Gram CNF with heavy and sym (3600 s cap), and the main-class enumeration of Latin squares of
    order 7 (`code/ls_classes.c`, by canonical form plus cycle switching; completeness requires Σ reduced =
    16942080). The enumeration feeds per-class K2 Gram instances.
- 19:28:00: both K2 exploratory screens finished: all 147 classes UNSAT under encoder A/CaDiCaL and encoder
  B/kissat; these are not yet certified exclusions. The K3 Gram run ended UNKNOWN at 19:26:33 after 3600 seconds.
  All exploratory solvers have finished. Certification now uses the frozen driver-only delta
  `review/CERTIFY-DRIVER-DELTA.r2.json`; both encoder hashes and the Gram proof text are unchanged. The first batch
  is class 0 under both encoders, with native caps and FIFO-streamed DRAT checks, at most 2 busy processes.
- 19:33:35: first K2 class certificates passed for A and B, with exact DRAT verification and sampled aggregate RSS
  below 563 MB. Driver r2/r3 startup/transport failures were rejected and preserved; r4 is the corrected stdin
  binary-proof transport (`review/CERTIFY-DRIVER-DELTA.r4.json`). Classes 1–146 under A are certifying sequentially.
  K3 `AMENDMENT-2.r1.md` freezes three covering row-frame cubes and forced singleton same-ray identities; its
  finite coverage control passed before search (18 assignments, three disjoint orbits). K3 cube search is pending.
- 19:55:28: encoder A has 147/147 verified K2 certificates (inventory
  `evidence/gram/k2A_cert_summary_r4.json`, 31aa7eb2…dc29). Encoder B classes 0–73 have also certified;
  classes 74–146 are next. All completed runs returned exact `s VERIFIED`, rc 20/0, without a safety stop.
  K3 cube search has not overlapped this two-process pipeline.
- 20:14:20: candidate K2 exclusion has both full producer routes: 147 A and 147 B DRAT-verified UNSATs. B inventory
  `evidence/gram/k2B_cert_summary_r4.json` is ed29e3a1…20f4b. Full write-up `review/K2-THEOREM.r1.md`
  (e846e1d9…ef05b) remains pending parent bridge/classification/replay/CLI acceptance; no K3 or exact-M(7) claim.
  K3 A screening is now sequential on C311/C321/C411 with native 1800-second caps and RSS/floor guards
  (`explore/k3cubes/screenA_r1/`), after all K2 certificate pipelines ended.
- 21:18:13: saved K3 cube checkpoints: A/C311 UNKNOWN at 20:43:35 (1800-second cap); A/C321 UNSAT exploratory
  at 21:06:29 (1373.284 seconds); A/C411 is the final sequential screen. C321 is not yet certified.
  `review/G6-G2-DERIVATION.r1.md` shows the singleton equalities are already implied by G1/G2 plus cube units;
  no new encoder restriction or CNF change is introduced. The finite coverage and exact G6 control receipts are
  in `evidence/k3cubes/`.
- 21:41:14: original A cube screen completed: C311 UNKNOWN; C321 UNSAT exploratory (1373.284 s);
  C411 UNSAT exploratory (1755.924 s). The only native science job is now A/C321's regenerated binary-DRAT
  certification pipeline, with 3600-second child caps and persisted 15-minute resource checkpoints.
  New matched component controls passed 26/26 outcomes on unchanged encoders; end-to-end proof transport
  controls accepted both UNSAT streams and rejected SAT/invalid-proof/premature-writer cases while retaining
  valid SAT models. Explicit chronology and review corrections are in `review/REVIEW-CORRECTIONS.r2.json`;
  corrected proof snapshots are `K1-THEOREM.r3.md` and `GRAM-ENCODING.r2.md`.
- 22:11:46: A/C321's regenerated original cube is now producer-certified UNSAT, with rc20/0 and exact
  `s VERIFIED`. Receipt `evidence/k3cubes/cert_r2/A_C321.json` is c3a30df3…e9314; CNF is d598507d…8388.
  Pipeline time 1906.802 s, maximum sampled aggregate RSS 1275789312 bytes, no safety stop. This is one cube,
  not a K3 theorem. A/C411 certification is now the sole two-child pipeline; C311 lex search and B routes wait.
  Updated candidate K2 text is `review/K2-THEOREM.r2.md` (a73a9007…532cd), preserving all original evidence.
- 22:39:37: parent disk steering applied. Fresh observation was 13,557,416 KiB available and lane644,984 KiB
  retained; the 12e9-byte floor remains continuously guarded. A/C411 certification is still the only pipeline.
  New `K3-CERTIFICATION-DRIVER-DELTA.r3.json` requires future certificates to regenerate/hash CNFs in memory and
  certify the one existing search input, never retain duplicate CNF copies. No proof file is retained, no old
  evidence is removed, and every future launch gets a fresh floor check plus projected log/receipt growth.
- 22:43:50: at the parent's request, froze `review/K1-COROLLARY.r1.md`
  (7ded3c69…f6b6d): every 2-RQLS(7) and every pandiagonal QLS(7) is classical/cardinality7, so neither
  maximal-cardinality 2-RQLS(7) nor MCPQLS(7) exists. The note proves the harmonic-net shear and cites/acknowledges
  Zhang–Cao Lemma2.2 and Ball–Simoens Lemma21 (order6) as prior art for the reformulation. It inherits K1 status
  and makes no exact-M(7) or priority claim. Parent K2 replay desk is separate; own pipeline remains <=2 busy.
- 23:05:47: A/C411 also producer-certified UNSAT (3143.930 s, sampled peak1899347968 bytes, rc20/0,
  exact `s VERIFIED`, no safety stop). Receipt `evidence/k3cubes/cert_r2/A_C411.json` is 5f117b60…a23cf.
  C311 remains the unresolved A case; independent B cases remain. The sole solver now screens the existing
  A/C311 residual-lex CNF for1800 seconds. Fresh launch floor13040176 KiB, projected new logs/model<=10 MiB.
  New no-duplicate A/B in-memory regeneration controls passed without writing CNFs or proofs
  (`evidence/k3cubes/no_duplicate_regen_controls_r1.json`).
- Parent23:17 disk notice: NEW solver/checker/enumerator/compiler/reviewer stages are deferred under the reported
  12.16e9-byte free space, below the new12.2e9-byte launch gate. Deferral is recorded once in
  `evidence/DISK-DEFERRAL-2317.json`; no disk polling or >10 MB snapshots/copies. Only the already-in-flight
  A/C311 lex screen may finish under its existing guards, with small logs/receipt. After its outcome, await parent
  resource release; none of these resource statuses is a scientific nonexistence result.
- 23:18:55: the in-flight A/C311 residual-lex stage stopped cooperatively on its free-space floor:
  UNKNOWN safety stop,769.881 s, rc-15, sampled aggregate RSS527564800 bytes. Its completed receipt is
  `explore/k3lex/screenA_r1/A_C311.json`; no solver/checker owned by this worker remains. No new stage was
  launched and disk was not polled after the parent notice. Research is resource-blocked, not complete.
  On parent release and a fresh>=12.2e9-byte growth-qualified gate before the original deadline, the immediate
  continuation is the interrupted C311 lex screen on the existing059be616…a8c4f input, using a new output directory.
- 23:26:41: parent resource release received. Fresh outer gate14309265408 available bytes exceeds12.2e9 plus
  projected10 MiB logs/model/receipt growth (`evidence/RESUME-GATE-2326.json`). Restarted the interrupted C311
  residual-lex screen as one fresh1800-second solver on the same existing CNF, new output `screenA_r2`;
  no input/proof copy or modification of the interrupted receipt. Parent release/floor policy remains in force.
- 23:47:55: the authorized C311 lex resumption also stopped on the continuous free-space floor:
  UNKNOWN safety stop,1229.385 s, rc-15, sampled aggregate492994560 bytes. All own science processes ended;
  renewed deferral is recorded once in `evidence/DISK-DEFERRAL-2347.json`, without disk polling or a new launch.
  Both lex runs were interrupted before their1800-second caps. The prepared text-only
  `review/drafts/AMENDMENT-4.r2.md` clarifies a proof-assisted alternative from the checked C321/C411 cases;
  it is unfrozen/inactive, without a generator/control/search. Await parent resource release and launch gates.
- Parent23:56 release: K1 and both requested order7 corollaries are parent-accepted
  (`evidence/PARENT-K1-ACCEPTANCE-2356.json`); M(7) remains undecided. Prioritize direct original B/C321, then
  B/C411 certification; no identical C311 retry and no all-frame-cut activation.
- 23:58:07: froze `K3-DIRECT-B-DELTA.r4.json` and dedicated `code/k3_direct_B_r4.py`
  (bbed0b09…6631e). The B/C321 attempt uses tested in-memory regeneration, existing B cube input, fresh
  internal12.2e9-plus10MiB gates before regeneration/native launch and the controlled3600/3600 proof pipeline.
  No prior B screen is claimed or fabricated; all outcomes are retained accurately, and no CNF/proof copy is made.
- 23:59:59: direct B/C321 stopped UNKNOWN on the continuous global free-space floor after77.704 s; both
  children rc-15, no checker verdict, sampled aggregate917635072 bytes. Both fresh outer gates had passed
  (12584103936/12584140800 bytes, each>=12.2e9+10MiB). Receipt and renewed deferral are retained under
  `evidence/k3cubes/cert_B_r4/B_C321.json` and `evidence/DISK-DEFERRAL-2359.json`.
  No own science process remains; B/C411 was not launched. Await parent release, without disk polling, C311
  retry, cut activation or CNF/proof copies. No B case exclusion or exact M(7) follows.
- 00:53:26 (2026-10-18): **K2 is parent CORRECTNESS-ACCEPTED** (`moqls7-k2-parent-verdict.md`, 25ecb6ba…1242;
  accepted text K2-THEOREM.r2.md with the parent's corrections). With K1, every MOQLS(7) triple is either classical
  or has three non-classical squares; M(7) is still 2 or 3. The K3 cover disposition (fbfc0e10…f369) accepts the
  cover, G6 and lex steps with text fixes and asks for provenance sidecars; AMENDMENT-4 stays inactive.
  - (a) Runtime B-map oracle PASS: `evidence/k3cubes/bmap_oracle_r1.json` (6e2bd95e…952c), script pinned in
    `review/K3-BMAP-ORACLE.r1.json` before execution; 0 of 2646 B variables differ from A's map.
  - (b) B/C321 certification running with the oracle-gated driver `code/k3_direct_B_r5.py` (0e391cc7…e4f6).
  - (d) Sidecars `review/K3-Q4-SIDECAR.r1.json` and `review/K3-ERRATA.r1.md`. (e) Draft
    `review/drafts/AMENDMENT-4.r1.md` (not frozen, inactive). Records: `evidence/PARENT-K2-K3COVER-0046.json`.
- 01:02:35: parent-requested AMENDMENT-4 cut generator `code/k3_cuts_r1.py` (0ec92c86…1b0a), pinned before execution
  in `review/AMENDMENT-4.GENERATOR.r1.json` (4c23ec44…5dd3). Its controls PASS (`evidence/k3cubes/cuts_r1_receipt.json`,
  9cfc0e81…babbf): exactly 238140 distinct clauses in 588 groups of 45+360; C1 rejects exactly the 450 forbidden local
  assignments; classical triples 0 violations; genuine weight-5 Ψ(f) exactly (2940,0); six mutations caught;
  invariance under all 22 lex generators and transposition; A and B emissions equal (B map decoded at run time).
  Clause block SHA 05f31da4…e6dd, not written. AMENDMENT-4 stays NOT FROZEN; no C311+cuts CNF or solve.
- 01:51:04: (b) B/C321 ended **UNKNOWN** with a checker timeout (receipt `evidence/k3cubes/cert_B_r5/B_C321.json`,
  b07100e3…7614). kissat returned UNSAT (rc 20) within ~2700 s. drat-trim read the 1,065,624,962-byte streamed proof,
  started backward checking and printed `s TIMEOUT` at its 3600 s limit; its clock includes the FIFO wait for the
  solver. No exclusion is claimed. (c) B/C411 started under the same 3600/3600 rule; a checker-limit decision for any
  B retry is with the parent.
- 01:57:03: the parent authorised ONE B/C321 retry after B/C411 r5 ends, with solver 3600 s and drat-trim 7200 s,
  plus ONE B/C411 retry only if B/C411 r5 ends solely on the same checker-clock obstruction. The driver-only delta was
  frozen before launch as `review/K3-DIRECT-B-DELTA.r6.json` (5beb6009…1eb8): driver `code/k3_direct_B_r6.py`
  (24fcfea8…c44d) and transport `code/proof_stream_r2.py` (45163ed4…5605), with a wall guard of 7320 s (≤10740 s).
  CNFs, oracle, binaries and controls are pinned. CNFs, solver limit and acceptance predicate are unchanged.
- 02:32:06: the parent disposition of AMENDMENT-4.r1 (3c9373c0…4e44) found the mathematics conditionally sound, set
  an A+B standard and gave a README:91 ruling. In response, these were drafted statically for parent source review:
  - `review/drafts/AMENDMENT-4.r3.md` (1ded55bb…c366);
  - `review/drafts/K3-CUTS-CERT-DELTA.r1.json` (b211321d…ac11);
  - appender/driver `code/k3_cuts_certify_r1.py` (0e978302…0b5a);
  - generator r2 `code/k3_cuts_r2.py` (5c1c1d67…bdd9);
  - controls `code/k3_cuts_certify_controls_r1.py` (1dc761d1…0025).
  Nothing was run or frozen; C311+cuts stays inactive until the review PASSes and the controls pass.
- 02:50:07: the parent accepted the A-side exact-CNF facts for A_C321 and A_C411 (verdict 0ba3fe4f…1f97). This is A
  side only; G1/G2 still need the B side under A+B. The source review put a HOLD on draft 1, so new versions were
  written statically:
  - stage guard `code/stage_guard_r1.py` (2d945ed0…0fba);
  - driver r2 `code/k3_cuts_certify_r2.py` (5b7ab798…f0ff);
  - generator r3 `code/k3_cuts_r3.py` (e636924c…3d0d);
  - controls r2 `code/k3_cuts_certify_controls_r2.py` (c9e287d9…2ef1);
  - `review/drafts/AMENDMENT-4.r3-d2.md` (157f38c3…8291);
  - `review/drafts/K3-CUTS-CERT-DELTA.r2.json` (f3684ae1…c4f9).
  They await parent source review; nothing is frozen or launched.
- 02:51:14: B/C411 r5 ended **UNKNOWN** with the same checker-clock obstruction (`s TIMEOUT` after solver rc 20;
  receipt 1acc121b…7dfc). The authorised B/C321 r6 retry (drat-trim -t 7200) is running; the one authorised B/C411
  r6 retry follows it.
- 03:07:05: the source review kept the HOLD on the stage-guard design. It is replaced by a single-threaded
  process-group supervisor, `code/supervise_r1.py` (0755d68e…8b53). Strict probes treat unknown as a trip plus a
  quarantine; killpg is sent only while the leader is unreaped; a final completion check runs. New versions:
  - supervisor controls `code/supervise_controls_r1.py` (0f61b466…01c5);
  - driver r3 `code/k3_cuts_certify_r3.py` (7453009c…5fbe);
  - generator r4 `code/k3_cuts_r4.py` (5c19b64a…24d9);
  - controls r3 `code/k3_cuts_certify_controls_r3.py` (90634fb3…1c3f);
  - `review/drafts/AMENDMENT-4.r3-d3.md` (9633ffa9…7339);
  - `review/drafts/K3-CUTS-CERT-DELTA.r3.json` (1d728bac…8b67).
  All control outcomes are still expected results; nothing has been executed or frozen.
- 03:15:23: the parent accepted the process-group supervisor for the stated production domain but required a
  fail-closed exception path. New versions:
  - supervisor r2 `code/supervise_r2.py` (0b023e2c…8c37);
  - supervisor controls r2 (f8f71254…11ec), with S12/S13;
  - driver r4 (3ad6a4df…c038);
  - generator r5 (2b9b1189…8e87);
  - controls r4 (646798ef…07e5);
  - `review/drafts/AMENDMENT-4.r3-d4.md` (c390a8bf…034c);
  - `review/drafts/K3-CUTS-CERT-DELTA.r4.json` (9d93687e…006c).
  These await source review; all control outcomes are still expected results.
- 03:31:05: AMENDMENT-4.r3 and delta r4 were frozen, but the first control stage, supervisor controls r2, **FAILED**
  (receipt 8313d092…18a1). The cause is that on Darwin an unreaped zombie probes as ESRCH and killpg on a zombie-only
  group returns EPERM. The frozen r3/r4 package is historical failed preparation, not activated cuts. A narrow fix,
  supervisor r3 (a zombie is ESRCH while freshly listed in our group; no killpg for zombie-only groups), plus the
  version cascade, is drafted as `review/drafts/AMENDMENT-4.r4.md` (75ac7aec…9a91) and delta r5 (75f8c382…b6e2).
  It awaits source review.
- 03:35:10: control stages for AMENDMENT-4.r4 (frozen 75ac7aec…9a91, delta r5 75f8c382…b6e2) all PASSED (observed):
  - supervisor controls r3: 3c77be50…99de;
  - generator r6: 9624d612…4a24, supervisor record clean;
  - controls r5: bb9445a2…b3e3, supervisor record clean.
  Strengthened inputs: A 18583aab…2e5e and B ae3b8309…783a. A C311+cuts launch awaits a separate parent GO.
- 03:36:36: **route A C311+cuts launched** under the parent's scientific GO (route A only, once): input
  18583aab…2e5e, supervise_r3 + driver r5, frozen AMENDMENT-4.r4/delta r5, caps 3600/7200/7320 s, supervisor wall
  8400 s and rss-cap 3.5 GiB. Route B is not GO yet.
- 03:59:13: **B/C321 r6 VERIFIED_UNSAT_CASE** (producer certificate; receipt 2ffc2fa8…32ac; exact `s VERIFIED`,
  solver rc 20, checker rc 0, 4035.475 s). Parent replay and acceptance are pending. The one authorised B/C411 r6
  retry is running.
- 04:10:15: the global 12e9 free-space floor (11,999,735,808 B free) stopped **route A** (UNKNOWN; supervisor
  record f0311593…04d2, clean stop) and **B/C411 r6** (final UNKNOWN; receipt 92354254…0184) at 04:09:50. Nothing is
  excluded. Route B was not started. Holding for a parent decision.
- 04:19:47: after parent PASS and GO, delta r6 and B delta r7 were frozen, and **route A attempt 2** was launched
  (driver r6 under supervise_r3, input 18583aab…2e5e). Route B follows A. B/C411 r7 waits for the replay desk's
  slot-2 handoff.
- 04:53:46: **route A attempt 2 UNKNOWN**, stopped again by the external free-space floor (driver receipt
  06bd12b0…dab3; supervisor record 50a07ffd…fc87; clean stop). Both feeds delivered the exact input. Route B is held
  for a parent decision on disk headroom. B/C411 r7 waits for the slot-2 handoff.
- 04:59:21: headroom recovered (25.96e9 B free). **Route B** (driver r6, input ae3b8309…) and **B/C411 r7** were
  launched in slots 1 and 2. Route-A attempt-3 versions (driver r7 6485a1eb…, delta r7 draft 00844232…) are
  prepared and await PASS and a free slot 1.
- 06:09:25: **B/C411 r7 VERIFIED_UNSAT_CASE** (receipt 644b5b23…6f75; producer certificate, parent replay pending).
  Both original cubes on encoder B now have producer certificates: C321 r6 (2ffc2fa8…32ac) and C411 r7. Slot 2 is
  released. Route B C311+cuts is still checking.
- 06:10:35: **route B C311+cuts VERIFIED_UNSAT_CASE**: driver receipt 1f003634…c535 with strict flags; supervisor
  record 43d48141…e4cb, completed_cleanly true. Producer certificate; the parent replay is pending. **Route A
  attempt 3** was launched in slot 1 (driver r7, frozen delta r7 00844232…). K3 is not excluded until route A
  finishes and the parent completes its replays and composition review.
- 06:20:23: froze the K3 composition note `review/K3-COMPOSITION.r1.md` (f17fdd98…6b90b). It sets out the chain
  K1 ∧ K2 ⇒ G4 ⇒ `--sym` ⇒ three cubes ⇒ {G1, G2; transport ⇒ cuts; C311+cuts on A and B} ⇒ no K3, with the status
  of each link and the conditional M(7) = 2 consequence. It makes no claim. After route A attempt 3, slot 1 passes to
  parent replays.
- 06:30:54: the Codex audit of composition r1 returned ACCEPT-WITH-FIXES (0 FATAL, 0 MAJOR, 3 MINOR). Errata-only
  `review/K3-COMPOSITION.r2.md` (803238a6…3f9d) and its diff (a9f50998…930b) are frozen. Route A attempt 3 is still
  running.
- 07:05:34: **route A attempt 3 UNKNOWN**, stopped by the external floor at 07:04:14 (supervisor record 6cf3bd5d…0496;
  the solver had returned rc 20, and drat-trim was in backward checking with no verdict). The A side of C311+cuts
  has no certificate. Slot 1 passes to parent replays. Any route-A attempt 4 needs a path-only r8 version, a parent
  PASS and a slot.
- 07:09:00: parent PASS and GO for the path-only r8 version (delta r8 439e37ee…d3d4, driver r8 1a50f09c…7eb5).
  **Route A attempt 4** was launched in slot 1.
- 07:10:54: **route A attempt 4 UNKNOWN**, stopped by the external floor after 99 s (supervisor record
  eea33007…aec6). All four route-A C311+cuts attempts were stopped by the floor. The A side has no certificate.
  Holding for a parent decision.
- 07:11:27: errata-only `review/K3-COMPOSITION.r3.md` (b85daed4…6aed; Claude m1–m9) and its diff (844f6306…7125)
  are frozen. Both static audits (Codex 0/0/3, Claude 0/0/9) accept the conditional skeleton. The lane is idle,
  holding for a parent decision on further route-A attempts.
- 07:20:35: free space recovered to about 189.5e9 B (the consumer was an external session). After parent GO (delta r9
  76f68d34…5487) and watcher admission, **route A attempt 5** was launched in slot 1.
- 07:21:28: froze `review/K3-H3-INSTANTIATION.r1.md` (c3d8c05d…5cdc), the written proof of the encoder
  instantiation (Link 7) for the parent composition review. Route A attempt 5 is running.
- 08:19:24: **route A C311+cuts attempt 5 VERIFIED_UNSAT_CASE**: receipt 88c154b7…f37f with strict flags; supervisor
  record 2fb5e032…25b1, completed_cleanly true. All six producer certificates of the A+B standard now exist: A_C321
  and A_C411 (parent-accepted); A C311+cuts; B_C321, B_C411 and B C311+cuts. The parent replays, the G1/G2 verdicts
  and the composition review remain; K3 and M(7) are not decided. phys-2 launches nothing further; the parent desk is
  the single M7 admitter.
- 08:23:29: status-refresh `review/K3-COMPOSITION.r4.md` (152e13cb…7b3e) and its diff (57183da2…0930) are frozen.
  Link 7 (H3) is parent-accepted at conditional scope (verdict edba465a…abca7). All six producer certificates are
  listed with SHAs. Parent replays, the G1/G2 verdicts and the final composition verdict are pending.
- 11:17:10: parent verdicts accepted G1 (639fbf6b…), G2 (d41253f6…) and the exact A C311+cuts CNF (b18472b2…).
  The unfrozen composition draft `review/drafts/K3-COMPOSITION.r5.md` (0dbaefe3…2486) records them and adds the
  formula, proof-boundary, control-chronology, lower-bound and import sections. The B C311+cuts parent replay and the
  final composition verdict are pending; M(7) is not decided.
