# Sub-lane cfr21: CFR(6,21) = (Z_21, 7; 1) difference matrix (worker InfoCFR27Lift)

Append-only README. Opened 2026-10-17 18:32:04 PDT (notes/lane-opened.txt) on the parent's instruction
(IRC 2026-10-17 ~18:2x PDT): PREPARE ONLY -- amendment draft, encoders, calibration runs of at most 5 min each on at
most 2 busy processes; NO substantial search and no claims until the parent issues a go. Contract context: the original
info-2 contract (../sources/contract-info-2-cfr33.json, "Same-lane alternates ... CFR(5,27), then CFR(6,21)") and
institute/runs/six-lane-2026-10-16/screening/info-2-cfr27-contract.json ("same-lane alternate CFR(6,21) only after
decision ... and an exact-group prior-art screen"); the parent runs that screen. Round deadline 2026-10-18 18:31:43 PDT.

## 1. Amendment DRAFT (written 2026-10-17 18:46:18 PDT; becomes frozen, unchanged, when the parent's go is appended)

### 1.1 Object and acceptance predicate
* CFR(6,21): 6 x 21 array, rows permutations of Z_21, all 6*21*20 = 2520 ordered distance events distinct. Equivalent to
  a (Z_21, 7; 1)-DM over the CYCLIC group (../notes/facts-v1.md E2); 7 DM rows; normal form rows 0, id, f_1..f_5.
* Witness = a 6 x 21 cfr-raw-v1 file written with exclusive create, sha256 recorded, that passes
  code/cfr_check_events_c21v1.py RAW 6 21 (CHECK_A PASS, 2520 distinct events) AND code/cfr_check_posdiff_c21v1.py RAW 6 21
  (CHECK_B PASS) -- both byte-identical copies of the cfr33 checkers -- then code/witness_gate_c21v1.py RAW 6 21 OUTDIR
  (all mutation expectations), its 7-row DM form passes code/dm_check_c21v1.py DM 7 21, the claimed symmetry passes
  code/audit_group_invariance_c21v1.py with an invalid-permutation control, and the producer replays byte-identically.
* On a candidate: SIGTERM every lane process, bounded wait <= 120 s (no SIGKILL), run the gates above, pin
  spec/model/binary/command/stdout, message the parent immediately, start nothing until the parent answers.
  A restricted exhaustion or a heuristic miss is never a gate and never "nonexistence of CFR(6,21)".

### 1.2 Representations and models (priority order)
(A) Symmetric DM-orbit models, exact cover over whole G-orbits (bin/dmorbit_xc_c21v1, copy of the cfr27 engine that
    produced the CFR(5,27) witnesses; changes listed in its header). G ranges over the UNTWISTED subgroups of
    Z_21^* x S_7 with 2 <= |G| <= 84, up to S_7-conjugacy, containing no dead element (notes/facts-c21-v1.md C2: E3,
    E3b, G1), as listed by bin/groups_enum_c21v1 in specs/groups-v1/n21-k7-ord2to84.jsonl (65 classes; orders
    2:6, 3:2, 4:3, 6:14, 7:1, 12:8, 14:5, 21:3, 28:2, 42:15, 84:6). Twists: H^1 classes from code/twist_h1_c21v1.py
    (specs/groups-v1/h1/; 101 classes in total; nontrivial only for 6 groups, H^1 = GF(7)).
    Runs: every class untwisted in modes zero and nozero (zero covers every G-invariant DM with a G-fixed column,
    ../notes/facts-v7.md F5); every nontrivial twist class in mode nozero. Order: |G| descending; per run internal
    deadline 1800 s for |G| >= 6, 10800 s (root split if needed) for |G| <= 4; a run that hits the 3 GB memory cap is
    UNKNOWN. A solution of any model stops everything (1.1).
(B) Per-row multiplier models (facts-c21-v1 C3: only K = <8> and K = <20> = odd are possible besides K = 1):
    bin/keq_clique_c21v1 (new; enumerate all K-equivariant normalised orthomorphisms, process R1-orbit representatives
    f_1, exact L2 per f_1, 4-cliques in L2). Odd model also by bin/cfr_odd_search_c21v1 (byte-identical copy of the
    cfr27 v7 engine, f1file mode over the same representatives) as an independent second program.
(C) Deferred (only if (A) and (B) finish): CRT lift Z_21 = Z_3 x Z_7 -- a (Z_7, 7; 3)-DM pattern plus a GF(3) lift
    (for each row pair and each Z_7-difference the three Z_3-differences must be distinct: sum = 0 mod 3 and not all
    equal; 147 linear equations), the analogue of the cfr27 3-adic lift engine; and order-3/2 groups by root splitting.

### 1.3 Wording
A finished model is a RESTRICTED result: "no (Z_21,7;1)-DM invariant under G (with/without a G-fixed column), program X
only". Cross-checks: per-row models by two programs (B); group models by one program plus the calibration evidence of
section 2 (and the Python cross-check where n is small enough). No statement about CFR(6,21) itself unless a witness
passes 1.1.

### 1.4 Resources and stop rules
After the go: <= 4 busy lane processes (or the parent's limit), <= 8 GiB RSS in total (xc MEMCAP 3e9 bytes per
process, at most 2 xc processes at a time), host free floor 12,000,000,000 bytes checked before every launch, chunks
<= 3 h, detached launches through code/run_cmd_c21v1.py / run_seq_c21v1.py with exclusive records, no SIGKILL /
Popen.kill / subprocess timeouts, no foreground calls in eval cells beyond a few seconds, checkpoints here at least every
30 min with host-clock times, everything stopped by SIGTERM at 2026-10-18 18:20 PDT at the latest.

## 2. Preparation log (appended as it happens)
* 18:32 code copies (notes/copies-c21v1.txt: source and copy sha256; modified copies: dmorbit_xc_c21v1.c,
  witness_gate_c21v1.py). New programs: keq_clique_c21v1.c, groups_enum_c21v1.c, twist_h1_c21v1.py.
* Calibrations (each <= 280 s, <= 2 processes; all records under calib/; every positive output passed checkers A and B):
  - bin/dmorbit_xc_c21v1 (sha256 005ca0b8…3a70): P21 (Sage DM_21_6_1 shape, n = 21, k = 6) count 96 COMPLETE and
    `all` count 2016, both equal to the cfr27 engines; n = 7, k = 7, <(1,7-cycle)>: zero 1, all 7; n = 13, k = 7,
    <(1,(1 2 3 4 5 6))>: zero 4 (positive), nozero 0; negatives n = 9, k = 7 (no (Z_9,7;1)-DM, kmax(Z_9) = 3) with
    <(1,6-cycle)> and <(1,7-cycle)>, zero/nozero/all: 0 COMPLETE each. Per-row cross-check against keq_clique (next
    item; a G-invariant DM with the zero column <-> a K-model normal form, so count_xc = (kk-3)! * count_keq_all):
    n = 13, kk = 5, K = <12>: 4260 = 2 * 2130; n = 11, kk = 6, K = <10>: 3024 = 6 * 504; n = 13, kk = 6, K = <3>
    (not odd): 12960 = 6 * 2160 -- all equal. n = 13, kk = 7 odd: xc 34,929 after 280 s (INCOMPLETE, 58% of the root)
    against the predicted 24 * 2520 = 60,480 (consistent, not a full check).
  - bin/keq_clique_c21v1 (ab1744b3…580b): positives n = 7 kk = 7 odd, n = 13 kk = 7 odd, n = 25 kk = 6 K = <7>
    (Kirtchakov's model) found; n = 9 kk = 4 odd EXHAUSTED (all 21 maps / 2 reps, count 0). n = 27 kk = 5 odd stopped
    by SIGTERM at 141 s: the level-1 store had reached 41,450,019 maps and ~1 GB RSS (the odd model at n = 27 is too
    large for this engine; harmless here, noted as a limit).
  - Model sizes at n = 21 (kk = 3 runs = level-1 enumeration only, no clique search): K = <8>: 2,527 maps, 108
    R1-orbit representatives; K = <20> (odd): 656,771 maps, 18,399 representatives (first L2: 86 maps, 0.06 s).
    The independent Python generator code/gen_odd_reps_c21v1.py (plain DFS, explicit orbits) gives the same numbers
    for n = 9 (21/2), 13 (319/19) and 21 (656,771/18,399); its n = 21 representative file is
    calib/oddreps-v1/odd-reps-n21.txt (sha256 9bf9bca3…f104), input of the second odd-model program.
  - bin/cfr_odd_search_c21v1 (copy of v7): f1file over the n = 13 representatives finds a CFR(6,13) (positive); n = 9
    R = 3: none (negative). (A checker run with the wrong row count 5 was correctly rejected by both checkers.)
  - bin/groups_enum_c21v1 (55c0ca6f…580b... see notes/hashes-prep-c21v1.txt): n = 27, k = 6, order 6 reproduces the
    hand classification (facts-c21-v1 C2). n = 21, k = 6, order 5: 1 class (the P21 shape). n = 21, k = 7, orders
    2..84: 65 classes with G1 (108 without); specs/groups-v1/n21-k7-ord2to84.jsonl (sha256 2fa193b5…ee8).
  - code/twist_h1_c21v1.py: equals the brute-force class counts on 11 groups (facts-c21-v1 C4); for the 65 groups:
    101 classes, nontrivial (H^1 = GF(7), 6 nontrivial classes each) only for g03 <(1,7-cycle)>, g13 <(8,7-cycle)>,
    g45 (42), g50 (21), g54 (42), g56 (14). The 6 nontrivial classes of each are permuted transitively by global
    multipliers (t -> lambda t), so they are expected to give identical results (all are run anyway).
  - Planted: Sage DM_55_7_1 rebuilt from the pinned source (code/sage_dm55_expand_c21v1.py) is a (Z_55,7;1)-DM
    invariant under <(1,(0 1 2 3 4 5))> with orbits [1, 6 x 9]; two invalid controls are not invariant
    (calib/planted-v1/). So the 6-cycle-plus-fixed-row shape hosts a known 7-row cyclic DM.
* 101 compiled models (65 untwisted + 36 twisted): specs/groups-v1/models-v1/ (index.json sha256 b8833082…1ee8).
  Prepared, NOT launched: runs/prepared-v1/jobs-{A1a,A1b,A2,A3,B1,B2}.json (118 + 36 + 12 xc runs, keq <8> and odd,
  v7 odd). Hashes of everything prepared: notes/hashes-prep-c21v1.txt.

## 3. Checkpoint 2026-10-17 18:52:31 PDT (clock read by `date`)
Preparation complete; nothing of this sub-lane is running; disk free 17.0 GB. No search for CFR(6,21) has been run:
the only n = 21, k = 7 computations were the group enumeration, the H^1 linear algebra and the model compilation.
The level-1 map counts above (kk = 3) list the f_1 candidates and never look for a 7-row DM.
Waiting for the parent's go (and any change of limits). On the go: append the go message and time here, freeze
section 1 unchanged (record its sha256), launch B1 and A1a/A1b first (<= 4 processes, <= 2 xc processes at a time).
Erratum (appended 18:54 PDT): three abbreviated hashes in section 2 were mixed up. Full values (notes/hashes-prep-c21v1.txt):
bin/keq_clique_c21v1 ab1744b3671523e5758acc1d74859503527aff560b0fedc00eb4a8a8a2a0cfa1; bin/groups_enum_c21v1
55c0ca6f4f063d22fb3bea812602dc262640cdbf9350df0ab99f7c0c55e07c6a; specs/groups-v1/n21-k7-ord2to84.jsonl
2fa193b58d22f897626f3978ef7a7cbe7ee96b989ac77917f9414d6d844c580b.
(Time correction: the erratum line was typed with "18:54" before the clock was read; `date` right after it gave
2026-10-17 18:53:07 PDT. Logged in notes/deviations-c21.log.)

## 4. Checkpoint 2026-10-17 18:54:51 PDT (clock read by `date`) -- preparation finished, idle until the parent's go
* code/candidate_gate_c21v1.py (sha256 44cf7486…991b): one-shot lane gate for a candidate (DM mode: dm_check ->
  dm_to_cfr -> checkers A and B -> witness_gate -> group-action audit with the control (1, swap rows 0 and 1); CFR
  mode: A, B, witness_gate). Tested on the cfr27 T10 DM with its spec: PASS; the same DM with two entries of row 3
  swapped: FAIL; the T10 DM with the wrong symmetry spec (S3a): FAIL (the audit rejects it); the keq CFR(6,13): PASS
  (calib/gate-v1/*/receipt.json).
* Third program at k = 7 (Python cross-check code/dmorbit_xcheck_c21v1.py, orbit materialisation): n = 7,
  <(1,7-cycle)>, zero + 6 fixed columns: 1 solution, 13 valid orbits (xc: 1 and 13 options in `all` mode); n = 9,
  zero + 1 fixed + 1 free orbit: 0 solutions, 61 valid orbits (xc: 0 and 61) (calib/pyxcheck-v1/).
* Nothing of this sub-lane is running. No CFR(6,21) search has been started; no claims.

## 5. GO received -- section 1 FROZEN (appended 2026-10-17 19:02:00 PDT, clock read by `date`)
Parent IRC (transition39): GO for CFR(6,21); parent freeze 2026-10-17T18:59:22-07:00; contract
institute/runs/six-lane-2026-10-16/screening/info-2-cfr21-contract.json (sha256 498efb754ef0ca1caccd76217bacd69a6f720a998ee0a1ebc56c5b5b9ed61e81,
checked 19:01:48); screen screening/info-2-cfr21-priority-screen-v1.md (9a41f26df48985e1cfc502838fa113e65f5feb9ff6b9c0d6a058a83f56d48c13,
checked). Section 1 (from "## 1. Amendment DRAFT" up to before "## 2. Preparation log", 4181 bytes) has sha256
82a79368b0c59984f6dde8ca6fd49e8da51e3aa69667c4ad9e4c2376df11eecc, recomputed here and equal to the parent's value; README
sha256 before this append 72cf5ca3e3b0c029dff2e43559410ddb438d97218e54cc47dcc674141c6966c1 (= contract
worker_protocol_pin). Section 1 is frozen from now on. Parent conditions recorded: first a <= 15 min assay of the
untwisted Frobenius group C7 x| C3 (rows i -> i+1, i -> 2i, entry multiplier 4 and 16), single column orbit of size
21 (the scout formula is an unreviewed lead: derive and calibrate it); then the frozen A/B queue. Limits unchanged
(<= 4 busy, <= 8 GiB, <= 10 GiB new data, <= 2 xc processes with 3e9-byte cap, floor 12e9, chunks <= 3 h, checkpoints
<= 30 min); compilers with TMPDIR inside the lane; stop by 2026-10-18 18:20 PDT. Scout lemmas/heuristics are not
pruning theorems; restricted exhaustion is not unrestricted nonexistence.

## 6. Addendum ADD-1 -- FROZEN 2026-10-17 19:03:42 PDT (clock read by `date`), before any production run
Changed priority (parent GO condition): a cheap assay runs BEFORE the frozen queue.
* Assay (i), new independent program code/frob21_orbit_c21v1.c (compiled with TMPDIR=cfr21/tmp-cc): the family of
  (Z_21,7;1)-DMs whose 21 columns are ONE orbit of the untwisted Frobenius group G_mu = <(1, x -> x+1), (mu, x -> 2x)>
  on the row indices Z_7, mu in {4, 16} (parent) and also mu = 1 (cheap). Derivation of the exact condition:
  notes/facts-c21-v2.md D1 (the scout formula is the mu = 4 case up to sign). Each mu: first `selftest` (100,000
  random v: every row-pair difference multiset of the expanded array equals the formula T(b - a); T(2d) = mu T(d);
  T(-d) = -T(d); reduced and direct tests agree), then `search` over all 21^6 base columns with v_0 = 0; every passing v
  is expanded and checked on all 21 row pairs; the first is written as runs/assay-v1/frob-mu<mu>.dmraw.
* Assay (ii), already compiled models (no new engine): bin/dmorbit_xc_c21v1 on g49 (= G_4), g50 (= G_16) and g36
  (mu = 1, conjugate labelling), modes nozero then zero, `first`, internal deadline 600 s each. These runs contain the
  single-orbit family (any orbit structure) and are the same six runs as in the frozen A1 lists; those six entries are
  removed from the queue afterwards (new list files runs/prepared-v1/jobs-A1a-v2.json, jobs-A1b-v2.json = v1 minus
  them), so nothing is searched twice. Twisted g50 classes stay in A2.
* Then the frozen queue: B1 (keq <8>, then keq odd) and B2 (v7 odd) on one process each, A1a-v2 and A1b-v2 on the two
  xc slots; afterwards A2, then A3. Output directories runs/A-out, runs/B-out exist before launch (a solution file
  must be creatable). Budget for the assay: <= 15 min wall in total.
* A passing assay vector stops everything (section 1.1 stop rule) and goes through code/candidate_gate_c21v1.py.

## 7. Checkpoint 2026-10-17 19:05:15 PDT (clock read by `date`) -- assay done (no witness), frozen queue launched
Assay (ADD-1), wall 19:04:11-19:04:38 PDT, all RESTRICTED results:
* (i) bin/frob21_orbit_c21v1 (sha256 177ae578…e174, source 04e41141…768d): selftest PASS for mu = 4, 16, 1 (100,000
  random base columns each: every row-pair difference multiset equals T(b - a), T(2d) = mu T(d), T(-d) = -T(d), reduced
  and direct tests agree). Search over all 85,766,121 base columns (v_0 = 0): 0 passing for mu = 4, 0 for mu = 16, 0
  for mu = 1 (runs/assay-v1/runs-i/). So no (Z_21,7;1)-DM is a single regular orbit of an untwisted Frobenius group
  C7 x| C3 with entry multiplier 4, 16 or 1 (this program only).
* (ii) dmorbit_xc_c21v1 on g49 (G_4), g50 (G_16), g36 (mu = 1): EXHAUSTED-RESTRICTED in modes nozero and zero (4.3-4.5 s
  each; options g49 248/158, g50 168/90, g36 2/2; no valid orbit of size 21 in any of them, matching (i)); so no
  (Z_21,7;1)-DM is invariant under these three untwisted groups at all (any orbit structure; xc program only).
  Two independent programs agree on the single-orbit part.
* Queue launched 19:05:09 PDT (4 processes): B1 (keq K = <8>, then keq odd), B2 (v7 odd over the 18,399 R1
  representatives), A1a-v2 and A1b-v2 (= v1 lists minus the six assay runs above: runs/prepared-v1/jobs-A1a-v2.json
  4551c34c…, jobs-A1b-v2.json 4f93a7ca…; 56 runs each). Disk free 18.5 GB at launch.

## 8. ADD-2 FROZEN 2026-10-17 19:18:03 PDT (clock read during note creation), before its production use
This changes priorities/time slices, not the frozen target or acceptance predicate.
* The remaining g01 zero run has only orbit-size3 options and20 columns left after the zero column; 20 cannot be a
  sum of3s. Versioned solver bin/dmorbit_xc_c21v2 (sha256 0c7187f4cbad97fd43034f7da7e4f2b5477836dcaa271f7d28e39b0fb5c222d6)
  adds ONLY this general exact necessary condition: unbounded coin reachability of the remaining column count using
  the sizes of the generated valid options. Failure rules out a cover; success proves nothing. No scout/multiplier
  heuristic is used. Calibrated counts unchanged: P21 96; n13k5 odd4260; n7k7 cyclic1; n13k7 6cycle4; n9k7 6cycle0.
  The old g01 zero probe is retained as UNKNOWN after SIGTERM; rerun g01 zero with the new guard.
* g06 order3 is not projected to finish (nozero:1 of1,441,314 root branches after>300s). Cap each zero/nozero probe
  at600s, then retain UNKNOWN and continue the still-unrun A2/A3 queue. This is not an exhaustion claim.
* Skip A3's pure per-row cases g09 and g18 already covered by B (g09 also has hand proof P1 in facts-c21-v2.md).
  Give the other A3 models600s initial chunks; increase effort later only if observed branch rates justify it.
* New representation C21-CRT1, exact derivation and families frozen in notes/crt-experiment-v1.md. Code:
  crt3_lift_c21v1.py (4b0c51152fb32a3f877738a130362b6192f158de04e756f2bbb2a45a1982eaf0) and
  crt3_affine_sample_c21v1.py (99b71aaf1a19d508ebd206a9ec87f0cbf307e02c608ff9b4f3ade1d782e695ab).
  For a (Z7,7;3) pattern, solve147 homogeneous equations overF3 in120 gauge-fixed alpha variables, then exact
  linear-nonzero constraints. A basis of the inequality image reduces the search to binary1/2 coordinates;
  every lift is checked on all21 row pairs overZ21. No SAT. Calibration: pinned cyclic Sage21k6 and33k6 reductions
  lift; Z3 k3 positive, k4 negative; repeated-field7 k7 negative; damaged beta multiplicity rejected.
  After B and the bounded A1 probes finish, allow one CRT sampler CPU alongside A2/A3 (rather than waiting for every
  expensive A3 probe). Seeds21001 onward,1800s initial chunks,2s per pattern; subsequent chunks <=10800s.
  Sample three affine-field-block families exactly as recorded in the note. Any per-pattern timeout is UNKNOWN;
  sampling is never exhaustion of the pattern family or of CFR(6,21). Standard candidate stop/gate rule applies.

## 9. ADD-3 FROZEN 2026-10-17 19:26:56 PDT (clock read at calibration launch), before target use
An independent exact representation for the still-UNKNOWN g06 model, not a new broad exclusion:
* code/cycle3_pair_c21v1.c, bin/cycle3_pair_c21v1 SHA256
  51b12d8010fe125dfad6bc9793ad36b44813f788fe46f8065ff27e91aebc53ed.
  Derivation in notes/cycle3-representation-v1.md. For symmetry
  (mu,(1 2 3)(4 5 6)), fix row0=0 and row1=t. The rows are exactly
  0,t,mu*h^2,mu^2*h,g,mu*g(h^2),mu^2*g(h), with h^3=id.
  Enumerate h by DLX on its fixed-point/3-cycle partition, requiring t-mu*h^2(t) bijective; then exact g search
  with five permutation constraints (listed in the note), followed by a direct all21-pair check.
  Modes fixed (h0=g0=0, covers all group-fixed-column cases by row translation) and free (h has no fixed point).
* Calibration: four prime-order positives (n7 mu1/2, n13 mu1/3) pass DM/event/position-difference/action checks.
  The n13 positives pass the full mutation gate. At n7 the frozen mutation generator raises IndexError for its
  hard-coded symbol index7; those full gates FAIL and are retained, with the exact boundary limitation documented.
  Known-negative n9 mu4 fixed/free both exhaust with zero h. Independent Python brute permutations reproduce the
  hcounts: n7 mu1 fixed2, n7 mu2 fixed2, n9 mu4 fixed0/free0; checks every top-submatrix row pair as well.
* Target: n21 mu4 (=g06), first hcount fixed/free (<=120s each), then first-solution fixed/free (600s initial chunks).
  This runs on one CPU alongside existing work and remains a RESTRICTED model. Timeout is UNKNOWN.
* New queue runner code/run_seq_c21v2.py stops its queue on exit10, writes an exclusive candidate marker and exits10.
  Known-prime-positive control confirms the second queued job is not started. New searches use tool-supervised
  jobs (without a tool-cell deadline) so candidate/termination output is delivered automatically; other owned
  queues are still stopped cooperatively by this worker on a target candidate.

## 10. ADD-4 FROZEN 2026-10-17 19:32:42 PDT (clock read while writing model note), before target use
* Order2 nozero cases are impossible by parity: after excluding G-fixed columns all orbits have size2, which cannot
  sum to21. Proof in notes/order2-parity-v1.md. Do not spend a huge option-enumeration pass on these four residual
  nozero cases; keep the four fixed-column A3 probes at600s (runs/prepared-v1/jobs-A3-zero-add4.json).
* Independent SAT representation for g15 only, derived in notes/sat-g15-v1.md. Zero/id rows are fixed by the generator,
  so the normal-form relation is f_j(13x)=13*f_sigma(j)(x), sigma=(1,3,2,5,4). Input runs/sat-g15-v1/g15.spec.json,
  SHA256430c8bf640371cd1bacc34cb3987f0d470a530347c7b27059791a3cf366923c7. No extra heuristic restriction.
  Byte-identical copied encoder94daf614…09e2, decodercd348155…fe3, native-limit runner101f421b…2e7ca.
  Calibration: unplanted CFR6,7 SAT and planted Kirtchakov CFR5,25 SAT decode correctly and pass A/B; plant is
  byte-identical. CFR3,9 UNSAT proof passes pinned DRAT-trim, while an empty-clause proof on the SAT positive is NOT
  VERIFIED (calib/sat-v1/). First g15 production: kissat seed1,1800s native limit, no proof file. SAT is decoded and
  gated; UNSAT without a certificate remains only a solver claim. Never unrestricted nonexistence.
  Uses one available CPU alongside CRT, cycle3 and one xc probe, total at most4 busy.

## 11. Checkpoint 2026-10-17 19:35:22 PDT (clock read while recording the independent g15 argument)
Target CFR(6,21) is still UNKNOWN; no target candidate.
* B closed: odd model exhausted by two independently written engines over the same18,399 representatives.
  Both report exactly1,708,200 L2 neighbours and10,034 edges, no required clique. v7 finished180.85s, every
  representative explicitly exhausted with no overflow/time limit; keq finished900.96s. K=<8> exhausts with L2
  empty for all108 reps and also has written proof P1. These are only per-row multiplier models.
* A1/A2 closed as bounded work: all58 untwisted groups of order>=3 OTHER THAN g06 exhaust in both modes; all36
  nontrivial twist classes exhaust (one xc implementation only). g06 nozero retained UNKNOWN after634s
  (planned600s probe; actual stop documented in notes/probe-stop-add2.json), zero UNKNOWN at600s. g01 zero's old
  208s UNKNOWN probe was superseded by the exact orbit-size obstruction (20 remaining columns, only size3
  options). Raw receipts and aggregate hashes: notes/checkpoint-A-B-v1.json.
* Dedicated g06 cycle3 representation (ADD-3), structured exact CRT/F3 sampler seed21001 (ADD-2), and fixed-column
  A3 probes (ADD-4) are now running under supervised jobs. No progress of those still-running jobs is claimed here.
* g15 normal-form SAT CNF has2963 variables,174,996 clauses, SHA fea22a706538588b33cc980f435eaf5eac6aa9acd2c19168bb0766aaa0bf2b50.
  kissat seed1 returns UNSAT in0.043s; a second run with DRAT returns UNSAT in0.041s. Proof checking is next; until
  checked this is only a restricted solver claim. Independent explanation is in notes/pair-fixedpoint-obstruction-v1.md:
  an individually fixed row pair forces3 fixed columns (Fix13), while a swapped pair forces7 (Fix8), impossible.
  This argument is specific about the multiplier and pair action; it does not exclude g10/g16.
* Four target-computation CPUs at most: cycle3, CRT, one xc, plus brief proof/checker work. Last recorded shared
  free space17.64GB; no new native processes are launched below the12GB floor. No unrestricted nonexistence claim.

## 12. ADD-5 FROZEN 2026-10-17 19:45:06 PDT (clock read at queue creation), before target use
Replace the slow residual generic A3 probes with an independent exact involution representation, not a heuristic cut.
* code/involution_pair_c21v1.c (b99573acce6f0876954190935831458b8e5353c17b49c1ed873512a23031d6f8),
  binary SHA256 f8caa8c94a6066d0ef1b1fb7401d5a9f90256ecebf2de63002fe5c873de8a43e.
  Full derivation in notes/involution-representation-v1.md. For generator (mu,(1 2)(3 4)(5 6)), row0 fixed, use rows
  0,t,mu*h,g,mu*g(h),j,mu*j(h), h^2=id. Enumerate all h with t-mu*h bijective; enumerate g with four permutation
  conditions, then test every pair g,j with the two exact cross-pair conditions. Unit-conjugate h representatives
  and swapping paired rows are valid existence symmetries, proved in the note. Store cap/deadline -> UNKNOWN.
* Controls: prime7 and13 positives found for mu1 and-1; n9 mu1/-1 exhaust with no g. The independent Python
  permutation check reproduces hcounts3,1,9,1, respectively. Both n13 controls pass the complete definition,
  mutation and claimed-action gates. Calibration evidence under calib/involution-v1/.
* Target multipliers13,8,1 correspond to g16,g10,g00. First hcount for each (120s limit), then first-solution
  chunks600s each, ordered13,8,1. One CPU. Native candidate output is checked on all21 DM pairs before writing.
  Stop the generic A3 driver cooperatively and retain its partial/UNKNOWN records; no overwritten attempts.
* g15 now CERTIFIED-RESTRICTED-UNSAT: regenerated CNF byte hash matches, DRAT-trim prints exact s VERIFIED.
  Proof246,980 bytes, SHA baa1563006583741617ce033cf4bc7528e6027d5fe21242405e2e9cfe5040616.
  Full receipt runs/sat-g15-v1/certificate-v1.json includes checker pin, soundness control and independent
  fixed/swapped-pair proof. No unrestricted conclusion follows.

## 13. ADD-6 FROZEN 2026-10-17 19:52:43 PDT (clock read when pinning script), before production use
Replace repeated random coverage of the small common-slope CRT subfamily with a finite deterministic scan:
* code/crt3_common_exhaust_c21v1.py SHA2878d8b7928afcc2630fe7850a39e2bc0c9fadf6704a8e4a866ee78338081677.
  Exact family is family2 of C21-CRT1: beta_i(0,c)=i*c and beta_i(t,c)=i*c+u_t*(i^2-i)+v_t*(i^3-i) mod7,
  t=1,2, (u1,v1,u2,v2) inF7^4. All2401 coefficient tuples give distinct beta patterns (checked at start).
  Enumerate lexicographic indices0..2400; each uses the already calibrated exact CRT/F3 solver, max10s per pattern,
  native chunk1800s. Preserve UNKNOWN pattern inputs; only a complete scan with no timeouts supports a restricted
  single-program exhaustion claim (independent cross-check still required). A candidate stops immediately.
  Calibration first index0 matches the known repeated-field negative: rank42, kernel78, no lift.
* Dedicated g06 v1 results are UNKNOWN, not exclusions: complete h enumeration counts468,198 fixed-mode h and
  841,428 free-mode h;600s g-searches processed416 and6 h, respectively, without a target candidate.
  Consider symmetry reduction/stronger exact g enumeration before extending those timings; no narrowed result is
  rebranded as unrestricted.

## 14. ADD-7 FROZEN 2026-10-17 20:02:49 PDT (clock read at timeout-resolution receipt), before verifier use
Independent certificate cross-check of the finite common-slope CRT family, not a change of search target:
* The Gaussian/F3 program settled all2401 patterns in156.10s, no timeouts or lifts
  (runs/crt3-common-all-v1/record.json). This is still single-program restricted evidence.
* New direct CNF verifier code/crt3_direct_sat_check_c21v2.py
  SHA69b548f5ae620880333d5e81886a9f2703e008988ab6cb6a04319af8ba68b6a9.
  It reconstructs beta independently, uses one-hot alpha and pair-difference variables with direct all-different
  triples; NO Gaussian elimination, projected forms or binary-image reduction. UNSAT requires exact s VERIFIED
  from the pinned DRAT checker; SAT is decoded and tested over all21 DM row pairs.
  Calibration: unplanted cyclic21k6 recovered; planted known cyclic33k6 alpha recovered; Z3 k4 negative has a
  verified DRAT proof; an empty-clause proof on the SAT21 control is rejected. Old v1 unplanted33 control hit its
  native8MiB proof cap and remains UNKNOWN; failed directory retained, no cap raised, completed21 control reused.
* First verification pilot: common-family indices0..31,300s global, native20s solver/checker per case,8MiB native
  file cap, shared disk floor plus64MiB margin, cumulative new data cap3GiB. Preserve every CNF/proof/log. On limits,
  retain UNKNOWN; extend only if observed cost supports it. Certified subsets are not whole-family certificates.

## 15. Checkpoint 2026-10-17 20:02:49 PDT (same clock reading)
No target witness. Initial CRT sampler finished43,628 draws in1800.03s,43,465 individually exhausted and163 timeouts.
The162 common-family timeouts are now resolved by the full2401-pattern scan; the remaining last-index43627 timeout
was replayed alone and exhausted in0.0304s. Thus no unresolved lift among those sampled patterns; this is sampling,
not exhaustion of general CRT matrices. Exact resolution receipt: notes/crt-sample-resolution-v1.json.
Only the dedicated involution native queue remains from the earlier target jobs; new independent certificate work
uses at most one additional CPU. Two code-only delegates are preparing exact affine reductions for g06 and a
full/non-odd permutation neighbourhood seeded by the known six-row cyclic21 designs; they must not build or run.
Both are integrated/calibrated here only after they return, and no production begins without another dated freeze.

## 16. Certificate range extension FROZEN 2026-10-17 20:04:08 PDT (clock read at measured-cost receipt)
The independent direct-CNF pilot certifies all32 cases0..31 by DRAT, no UNKNOWN, in1.443s and3,014,274 bytes.
Measured linear projection for the remaining2369 cases is~107s/~223MB [INFERENCE, not a promised outcome].
Under ADD-7's conditional extension, verify indices32..2400 with900s global limit, the same20s per-native limit,
8MiB per-file cap,3GiB range-data cap and12GB disk floor plus64MiB margin. No limits are raised.
Only combining settled receipts covering all2401 indices without UNKNOWN supports a whole-family certificate;
otherwise preserve certified subsets and unverified cases separately. Receipt notes/crt-proof-pilot-v1.json.

## 17. Checkpoint and certificate continuation, 2026-10-17 20:20:57 PDT (clock read at calibration queue creation)
No CFR(6,21) witness. Dedicated involution v1 also timed out in each600s first-solution probe: mu13 processed277 h,
mu8 processed23 h, mu1 processed9 h, none yielded the two compatible g maps. Independent top-H counts complete:
255,633 /1,507,077 /188,181 respectively. These are top-subproblem counts, NOT seven-row exclusions.
An exact nested AlgorithmX implementation for g is being calibrated before further target use.

Direct CRT certificate extension took898.18s and~1.53GB (not the pilot's linear projection): indices32..2264 settled,
2176 certified,57 UNKNOWN. Of those57,56 hit the unchanged8MiB native proof cap; one reached a native limit near the
global deadline. With the prefix there are2208 independently certified patterns, not a whole-family certificate.
Continue ONLY the unattempted tail2265..2400 with300s global, same20s native and8MiB file caps. Preserve all earlier
failed/proof-limited cases; do not rerun certified inputs or raise resource caps. A different calibrated prover may
be tried later on the57 unresolved cases, with its own controls and dated freeze. Primary F3 evidence for all2401
remains separate from this partial certificate. Last free-space observation15.83GB clears the12GB floor.

## 18. ADD-8 FROZEN 2026-10-17 20:24:25 PDT (clock read at target queue creation), before target use
Same three residual involution models, stronger EXACT implementation:
* code/involution_pair_c21v2.c SHA36457219c216b8672599ff9c5dc97a57b972ff0db1036fb948868a9ace257719;
  binary4d41e4b4e882069af28742b7ae97e9793307e3ded93f1ad8733e21570634fcb5.
  g assignments are now a second AlgorithmX matrix over orbit markers and all four permutation-value families;
  mathematically identical to v1 masks. All actual target outputs still get the independent all-pair check.
  h representatives also allow shifting by an h-fixed point before unit conjugation, with g/j translations
  preserving the generator; exact proof in notes/involution-representation-v2.md.
* Independent Python brute permutations reproduce full H counts, affine H representative counts, complete V sets
  and compatible V-pair counts at n7/n9. Both n13 positives pass the entire candidate gate (calib/involution-v2/).
* Target first-solution chunks1800s per mu13/8/1 (g16/g10/g00), initially mu13 andmu8 in parallel, mu1 on a free CPU
  as limits permit. No more than four busy native CPUs overall, and room retained for parent-owned calibration.
  If a model finishes, its result is only restricted; a timeout is UNKNOWN. All v1 attempts remain unchanged.

## 19. ADD-9 FROZEN 2026-10-17 20:33:50 PDT (clock read at queue creation), before affine-cycle production
Both code-only delegates have returned; all build/calibration was done by this worker afterwards.
* code/cycle3_pair_c21v2.c SHA9382212c4e7a2b5a61d90faa8cdc6b0413044ea3e8e07e0c65b253bfaa826e5b;
  binary7d081cf94cfcc328741d8e85a6c12823db8497ae4470bb6f995179ed224cc768.
  Exact affine h conjugation and free-mode g0=0 gauge are proved in the header, not inferred from a heuristic.
  Independent Python entrywise checks reject four intentionally wrong transformation formulas; all small prime
  and Z9 exhaustive H/model checks, old positive transports and native logs agree. Native target H totals remain
  468,198 fixed /841,428 free; affine representatives are12,831 /3,339 (calib/cycle3-v2/independent-controls.json,
  all_as_expected true). Three prime13 positives pass full definition/mutation/action gates.
* Target g06 mu4: free then fixed,600s initial chunks, one CPU, runs/cycle3-v2/jobs.json. Limits/overflow remain
  UNKNOWN; this changes only the exact representation and existence quotient, not the symmetry family.

## 20. ADD-10 FROZEN 2026-10-17 20:34:18 PDT (clock read at calibration acceptance), before non-odd production
New finite first-row neighbourhood, with NO assumed automorphism of the whole target:
* Expand all96 known P21 six-row DMs, normalize every ordered row pair (p,q), collect their four other maps,
  then quotient by R1 (unit conjugation, A(f)=f(-x)+x, inverse). All1,440 DM row pairs,2,880 normal forms and11,520
  occurrences were checked directly. Inventory/R1 closure has360 distinct maps and six representatives
  (two size36 orbits, four size72), explicit provenance in specs/full-seeds-v1/p21-detail.json.
  Input specs/full-seeds-v1/p21-r1-reps-n21.txt
  SHA50585e11b3e9d063b4b242fc2f82db2c4a1789b48f6058da5fca696fa3656329.
* code/cfr_perm_search_c21v1.c SHAe2bcdb7478d186776d233354b7971410e50b40e698d7bdc78791539f57432eb7;
  binaryf9d6e55e58db6f677da16fe18392ab9b2f7139a31e560d570b66a299ffa87e8b.
  This uses all20 nonzero points and ordinary residues, not odd half-maps. For each fixed f1 enumerate full L2 and
  seek a4-clique. L2/adjacency allocations are bounded below1GiB; any cap is UNKNOWN with exhausted0.
* Controls: prime7/13 CFR6 positives; all225 normalized Z9 orthomorphisms have L2 empty (full, not odd enumeration).
  Tiny-store and tiny-edge controls fail closed with overflow1/exhausted0. Malformed half-map and identity inputs
  reject. Prime13 full gate passes. The Kirtchakov first-row extension control produces CFR3,25 and passes its
  full gate (this is a subset-sized control, NOT a claimed production recovery of the full CFR5,25).
* Target: N21,R6, seed argument1, f1file over all six representatives, native10800s limit, one CPU. Deterministic
  f1file enumeration. Any completed negative applies only to normalized targets having an f-row in this finite
  R1 family (up to the stated equivalences). A general asymmetric target outside it is untouched.

## 21. Checkpoint 2026-10-17 20:38:44 PDT (clock read while pinning the remaining proof cases)
Still no CFR(6,21) witness. Current four native search CPUs: involution v2 mu13, involution v2 mu8, affine-cycle v2
mu4 free/fixed queue, and full non-odd six-seed neighbourhood. All are bounded and tool-supervised; no interim
progress from those running jobs is claimed. Involution v2 mu1 is prepared but waits for a free CPU.

Independent CRT certificates now cover2343 of2401 explicit common-slope patterns. All2401 were attempted by the
direct CNF route;58 remain uncertified (mostly unchanged8MiB proof-file limits), while the separate exact F3 solver
settled all2401 negatively. Do not call this a fully certified family exclusion. Only those58 original CNF hashes
are listed for a later different-prover retry in notes/crt3-unresolved-request-v3.json. No cap increase or rerun of
certified cases is allowed. Source code for a CaDiCaL continuation is prepared, but its prover controls must pass
before use and it will wait for a free CPU. Last free space15.34GB; floor remains12GB.

## 22. ADD-11 FROZEN 2026-10-17 20:49:20 PDT (clock read at target queue creation), before verifier use
The six non-odd P21 first-row representatives all finished in the bitmask engine (371.36s, no overflow/timeouts).
Their neighbour/edge counts are19084/23,19282/14,19209/6,18974/8,19145/13,19064/20, no4-clique.
This remains one-program restricted evidence until checked independently.

New independent checker code/full_seed_crosscheck_c21v1.c
SHA57c3b1180809bb54e1f2eb6ff313753340be7db64067ce9b9905b96b61ae9d34,
binary045db7952fa306f19f1f6ba2766975f971a8e065dd8eb79a45602e1105cf017a.
Adapted from the separately written K-equivariant engine with K={1}, it reads only the fixed inventory, uses
point-MRV mask enumeration rather than the primary class-item bitmask DFS, and builds/checks the full graph.
Controls agree exactly with the primary engine on prime7 graph4 vertices/6 edges and prime13 graph348/630;
both produce valid CFR6 positives, prime13 full gate passes, and all225 Z9 first maps have L2 empty.
Malformed and identity inputs reject. Memory caps and deadlines fail UNKNOWN; no unconstrained model conclusion.
Run N21,DM rows7, same six-row input file, native10800s, first-solution mode, one CPU. It can still produce a
directly checked candidate if the primary result was wrong. Target symmetry is not assumed.

## 23. Checkpoint and ADD-12 FROZEN 2026-10-17 21:33:41 PDT (host clock read before new production)
No CFR6,21 candidate. The independent point-MRV checker has now completed all six baseline P21 first-row
representatives in2345.79s, no timeout/cap. It independently matches every primary L2 vertex/edge count:
19084/23,19282/14,19209/6,18974/8,19145/13,19064/20; total114758/84, no4-clique.
Thus this finite first-row family has an independent exact restricted exclusion, not an unrestricted result.
Both completed outputs and the input/producer/checker hashes are retained; no completed target search is rerun.

Checkpoint deviation C21-D4 is recorded in notes/deviations-c21.log: the interval after ADD-11 exceeded30min
while a supervised verifier completed. It is not backdated away. The new code/run_seq_c21v3.py, SHA
3fc7a3e14703923e34444159884f1df53ede14a2512434891ac4a7f91151dcd1, preserves the exact child commands and
candidate-stop protocol, adds actual host-clock heartbeat.jsonl at most300s apart, and forwards SIGTERM at the
frozen18:20 PDT stop time or disk floor. A2s native wait produced periodic1s calibration heartbeats, the known
prime7 positive stopped its queue with exit10, and the subsequent test job was not started. No target candidate
is implied by this calibration. Future long queues use this version. Last free space14,251,294,720 bytes.

ADD-12a: resume the already frozen INV-v2 mu1 probe, unchanged native1800s, one CPU, with the checkpoint runner.
The settled mu8/mu13 probes and C3-v2 free/fixed probes remain UNKNOWN, not exclusions; all old jobs are settled.

ADD-12b: alternative direct-CRT prover controls passed at21:30:25. Code/crt3_direct_sat_check_c21v3.py SHA
29f06c10df113eee989f2419d8e84995f570ada13ae711e0b6905670f237de74 uses CaDiCaL seed1 (solver SHA
601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa) and the pinned DRAT checker.
New controls: unplanted Sage21k6 SAT, planted Sage33k6 SAT, Z3k4 UNSAT with DRAT verification, and rejection of an
empty-clause proof on a SAT input. Retry only the58 unresolved original CNFs listed in
notes/crt3-unresolved-request-v3.json, requiring exact regenerated-CNF SHA equality. One CPU, native20s per
solver/checker, wall allowance1800s, unchanged8MiB per proof/3GiB range cap and12GB floor plus64MiB margin.
No previously certified input is rerun. A partial retry remains partial; combine all receipts before any full
finite-family certification claim. The exact F3 result and the independent CNF route remain distinct evidence.

ADD-12c: next finite non-odd first-row family is the COMPLETE one3-value-trade inventory just generated from the
360 pinned baseline maps. For each triple of domain points, rotate the three values in both directions and keep
exactly those preserving the three differences with identity; subtract the new f(0), then quotient by the same
calibrated R1 operations.957600 proposals yield2808 valid occurrences and50 new R1 classes, none reusing the
six excluded baseline classes. Input specs/three-trades-v1/new-trade-R1-reps.txt SHA
d30506be45c9ce0d7feb30de341e90a018880abc90c6a19872c085e4fe76f1a3; generator SHA
b81736e9c602daace1b2d42c313247c0d8620767a8fa36a1cd2c0ea5872690aa; provenance retained.
Run only these50 inputs in the already calibrated full/non-odd engine, no target symmetry, CFR rows6/N21,
native10800s, one CPU; stop on candidate, cap/timeouts UNKNOWN. At most4 busy processes including the above,
aggregate8GiB/data10GiB/floor12GB unchanged. This covers only that finite family. Any newly exhausted inputs
need the independent point-MRV cross-check before they are called independently excluded.


## 24. ADD-13 FROZEN 2026-10-17 21:41:58 PDT (host clock read before finite-pattern certificate reduction)
CaDiCaL retry finished all58 previously uncertified inputs in218.92s:41 additional DRAT certificates,
17 still UNKNOWN at the unchanged file cap. Thus2384/2401 direct certificates are available; no whole-family
certificate claim yet. Both target search queues (INV-v2 mu1 and50 trade first maps) continue unchanged.
Free space13,834,625,024 bytes; no cap is raised and no more proof-file retries are planned here.

Instead prepare explicit validity-preserving DM equivalence certificates from each remaining beta pattern to
an already DRAT-certified pattern. This is verification of the same finite family, not a new target search.
Write U=(0,u1,u2),V=(0,v1,v2). For a,l nonzero and b in F7, and a permutation s of the three blocks, put
dU_t=U_s(t)-U_s(0), dV_t=V_s(t)-V_s(0). The transformed parameters are
u'_t=l*a^2*(dU_t+3*b*dV_t), v'_t=l*a^3*dV_t.
Derivation: permute rows i -> a*i+b, subtract row b columnwise, permute blocks, subtract each new row's value
at the new column0, and multiply entries by a unit L of Z21 with L mod7=l and L mod3=1. These standard
DM-validity-preserving operations induce a common affine permutation of c separately in each7-column block.
They preserve cyclic Z21 DM existence; no CFR row-isotopy claim is made.

The certificate producer must emit explicit7-row/21-column permutations, multiplier and row constants.
A separate table-level verifier (not reusing the parameter transformation) must reconstruct both beta tables,
check every one of147 equalities modulo7 under those operations, check the anchor's exact CNF/proof/checker
receipt hashes and stripped exact s VERIFIED, and reject an invalid column permutation control. The proof
anchors plus these explicit implications may cover the residual17; missing coverage remains UNKNOWN.
At most one additional CPU, native preparation/verification allowance300s, negligible extra data; all lane caps
unchanged. The primary exact F3 exhaustion and DRAT-plus-equivalence evidence must be reported separately.


## 25. ADD-14 FROZEN 2026-10-17 22:03:01 PDT (clock read before certificate production)
For a stronger, smaller audit dependency, the explicit-equivalence producer will map ALL2401 patterns to a
small selected subset of already DRAT-certified anchors, not merely map the residual17. Select anchors from
the complete finite parameter-action images, preferring smaller retained proofs; the separate verifier does
not trust those orbit labels and must check every literal7x21 table implication and exact coverage.
Only the selected anchor CNFs are regenerated to bind the stated beta tables to the pinned proofs. Native SAT
and proof checks are not rerun. The unchanged300s bounds/data caps apply.
Producer code/crt3_equivalence_cert_c21v1.py SHA
08e7895c77b3db8984db1f7074229f956d3fc6e747613df7a267dcd7e8e00e35;
table auditor code/crt3_equivalence_audit_c21v1.py SHA
102418159933ccbf0d1ba1959bf3f39b56749e88b03b07ebd88ec2599ee8485d.
The control swaps two nonzero column images while retaining a valid permutation, and must fail the beta
identity itself, not merely parser validation. Actual anchor count and coverage are not asserted before audit.

## 26. ADD-15 FROZEN 2026-10-17 22:03:01 PDT (same host-clock read, before new fixed-action SAT search)
New exact representation of the already selected involution groups: fix the COLUMN involution h in canonical
form, leave the first nonzero row a free permutation (do not force both h canonical and that row identity).
For paired rows F,mu*F(h), d=F-mu*F(h) satisfies d(h)=-mu*d. Since d is a permutation, h has exactly
gcd(mu+1,21) fixed columns:1,3,7 for mu1,8,13. Common column relabelling makes h fix0..f-1 and swap consecutive
remaining points. A group-fixed row translation at fixed column0 permits every F(0)=0. Thus this representation
is complete for each restricted pure involution action, with no assumed extra symmetry.

Use3 primary permutations F,G,J; twin rows are virtual, not independent variables. Require the3 within-pair
differences and, for every pair of primaries, F-G and F-mu*G(h) to be permutations. These9 conditions imply
the other pair differences by h and unit multiplication; every decoded candidate is checked on all21 pairs.
CNF has5292 variables and, with zero gauges plus the optional exact unit anchor, at most188437 clauses atN21.
The unit anchor F(f)=1 is permitted because phi(21)=12>f: some unit value lies on a nonfixed column; a
centralizer permutation of h and a common unit entry multiplication put that value at f and make it1.
No heuristic/lex pruning is used. This is a fixed-column-action encoding, not the variable-H outer enumeration.

Source code/fixed_involution_cnf_c21v1.py SHA
a48309148696e4951e5b558d83b2e69e64243a308faf05f09b5e3b05328ec9fd.
Before production: unplanted prime7/13 paired positives; full known CFR4,27 odd and Kirtchakov CFR5,25 plus
Sage21 DM6 as explicitly PLANTED no-action base controls; unplanted Z9 DM4 negative with DRAT/checker control.
Planted controls are calibration, not solver recovery claims. Any failed calibration remains retained and
blocks this new producer. Main integration runs controls after both disjoint source-preparation tasks land.

Then initial native1800s SAT probes mu8,mu1,mu13, seed1, at most one such solver until aggregate RSS is measured.
Search WITHOUT a proof file to avoid an8MiB proof cap terminating a potentially productive search. An UNSAT
solver claim alone remains uncertified; a separate proof run or independent exact agreement is required.
Use a versioned supervisor with cooperative SIGTERM,2.5GiB child RSS stop threshold,8MiB native stdout/proof
cap, host-clock heartbeat, shared12GB floor and the frozen worker stop time; other lane caps remain unchanged.
On SAT decode/check the complete raw7x21 DM and stop its queue with exit10; stop all other owned searches and
run the existing DM/CFR gate before notifying the parent. Last free space14,236,049,408 bytes.


## 27. Checkpoint and ADD-16 FROZEN 2026-10-17 22:29:30 PDT (host clock read before new production)
No CFR6,21 candidate. All old native searches and the new calibration queues have settled. The50 three-trade
first-row cases all exhausted in3078.96s with963360 neighbours,406 edges and no4-clique; this is still primary
one-program evidence until their independent point-MRV cross-check finishes.
The finite-CRT equivalence attempt correctly did NOT pass its audit:9 anchored parameter orbits cover2389
patterns, but the12-pattern orbit with seed364 has no retained DRAT anchor. The auditor refused the incomplete
producer. Both failed-attempt artifacts remain unchanged; no full-family certificate claim is made.

New C3-v3 source26bcb778a83979382166c2a44ad11d8737c68b291728fce8716d10c7873b0ddb,
binary130d2b70ac203e311ff3dc926152be3358680bf9f79169d1837addc31f344c07, independent Python checker
db6753496064c95f08eb9ed493cfed4852299965f13f9322ca05a48718fdb79a:
59 native control runs plus the independently authored definition-based Python control passed, including
n7/n9/n13 counts, g-set count/FNV checks, affine classes, full21-pair equivalence and deterministic skip logs.
FNV agreement is a64-bit checksum, not a byte-exact set certificate. N21 H counts reproduce
fixed468198/12831 classes and free841428/3339 classes. All three prime13 positive full DM/CFR/action gates pass.
Run BOTH N21 mu4 modes from SKIP0, native5400s each, separate one-CPU queues, same row-action generator
(4,(1 2 3)(4 5 6)). No old partial prefix is assumed. G search is now nested5-map DLX, not the v2 orbit-MRV
search. Completed ranges are [SKIP,SKIP+hcompleted); resume only at the printed resume value. Restricted
completion still needs independent exact cross-check before certification. No unrestricted conclusion.

INV-v3 source0a79403b37edeec18006a4e9d0e4a7dca8947a7a0a21b87ada5a3ece827d00a6,
binary895779e2413f4c1ef282a17202e8908c93a4f0f15f2c7fe1308a3426dd5259eb:14 native positive/negative/resume/
invalid-skip/timeout controls have exact expected return codes; an interrupted current H reports hcompleted0.
Both prime13 positive full gates pass. Continue mu13 with native5400s and SKIP1983: the old v2 run reached
canonical1984 before its deadline, so only the strictly earlier1983 H are omitted; its last H is deliberately
redone. New hcompleted is the last actually completed canonical index, not a count including the assumed
prefix. Preserve the old timed-out receipt and require the union of ranges for any later model completion.
The mu1-v2 probe also settled UNKNOWN at1800.001s, canonical42; it is not resumed by this queue.

Use the fourth CPU for independent verification of the50 trade inputs, in five disjoint10-line chunks listed
with hashes in runs/three-trades-crosscheck-v1/partition.json. Each native chunk5400s; deadlines/caps remain
UNKNOWN, not exclusions. The already calibrated point-MRV engine returns10 on a candidate, so the checkpoint
runner stops the remaining queue. All four queues use run_seq_c21v3 host-clock heartbeat logs and cooperative
SIGTERM. Total busy processes<=4, RSS8GiB/data10GiB/floor12GB, <=3h native chunks unchanged. Last free
space14,054,432,768 bytes. Build commands/source hashes are pinned in calib/integration-v3-build-manifest.json.


## 28. Parent disk-policy cutover, recorded 2026-10-17 23:25:51 PDT (host-clock read)
The parent's22:38 and23:17 notices supersede earlier launch plans:
* Before EVERY new solver/checker/enumerator/compile/reviewer stage, take a fresh shared free-space check.
  It must show at least12,200,000,000 bytes AND fit projected retained growth; the physical floor stays12GB.
* If that check fails, record UNKNOWN/deferred, report ONCE to the parent, then wait rather than poll.
* In-flight stages may finish, writing only small receipts. No new proof files; existing pre-notice artifacts
  are preserved unchanged because deletion/thinning/unlink-style compression is forbidden.
* Regenerate future CNFs in RAM; never retain duplicate CNF copies. No new snapshot/copy larger than10MB;
  review snapshots are text-only. New verification tasks have at most1GiB retained growth.
The first post-notice check at23:24:21 showed15,034,437,632 bytes, so no deferral was reported. This is not
permission to reuse that reading: every later launch is checked again. The already-launched independent
checker compile finished; no new native SAT stage has run. The old multi-part trade-verifier queue was
cooperatively SIGTERMed at23:25:51 after its exact command/PID were validated, so it cannot start another
chunk under its obsolete12.064GB launch guard. The two single-job C3 searches may finish.
Receipt: notes/trade-verifier-policy-pause-v1.json. No SIGKILL, deletion, thinning or proof compression.

The mu13 INV-v3 suffix finished in1043.123s: H255633, canonical3145, hcompleted3145, no timeout/overflow/pair.
Together with the pinned completed prefix1..1983 this exhausts this ONE involution model in the original
enumerator. It is not yet independently certified and says nothing unrestricted about CFR6,21.
The50 trade inputs have only primary exhaustion until the paused independent verifier's completed prefix
is reconciled. The earlier six baseline inputs remain independently cross-checked.

## 29. ADD-17 FROZEN (clock read 2026-10-17 23:25:51 PDT), conditional on completed review and calibration
Extend the fixed-column-action representation to two row3-cycles. For each primary F use the virtual triple
F(t),mu*F(h^2(t)),mu^2*F(h(t)); use one within-triple difference per primary and all three cross-triple
differences. All other differences follow by the action. The first nonzero row remains FREE, not identity.
For N21,mu4, h^3=id implies its fixed count is0 mod3; injectivity of (1-mu)F on fixed columns bounds it by7.
Thus the three canonical column actions with0,3,6 fixed points cover this restricted pure row action.
Only PRIMARY F(0)=0 is gauged in free mode: subtract a group-fixed (a,mu*a,mu^2*a) vector. Virtual entries at
column0 are generally nonzero, and the decoder must not require an all-zero column there.

Exact centralizer normalization: sort the first primary on fixed columns; cyclically rotate each nonfixed
h-orbit so its minimum first-primary value is first; sort those orbit minima. This never reverses a3-cycle.
These common column permutations commute with h and preserve all primary-zero gauges. For fixed count>0,
the optional unit anchor is compatible with this ordering under the earlier phi(N)>fixed-count premise.
No scout clique heuristic or unproved pruning is used. Each result remains restricted to its stated action.

Encoder code/fixed_rowcycle_cnf_c21v1.py SHA
2d508f682d3f38f5e6be2c06942416845e7a84196c983a2df8e97a7b85a4e6ee.
Its bounded private memory interface emits one read-only CNF buffer and no CNF/proof files. All decoded
candidates get every row-pair test, the explicit column action and column-multiset audit before raw output;
this is NOT a CFR row-isotopy claim. Three C3 fixed-count target models are planned, initially native1800s,
one solver until RSS is measured, per-call retained growth<=16MiB. No target production before calibration.

The independent static reviewer found no mathematical defect in the paired model or this C3/gauge/centralizer
extension. It did find supervisor lifecycle bugs: ordinary bounded waiting was fixed in v2, but a failed
stream close could still bypass the unreaped-child guard. Therefore supervisor v1/v2 and the current v4
queue prototype remain UNRUN and NOT production-ready; a new version must preserve guard exits even when
cleanup/logging fails, apply the12.2GB minimum before every Popen, and halt queued work on any guard failure.
Review receipts are preserved; no failed static-review attempt is overwritten or presented as accepted.

Calibration plan is pinned in calib/rowcycle-memory-v1/controls-plan.json: unplanted paired/C3 prime7/13,
full planted odd CFR4,27 and Kirtchakov CFR5,25 plus the known P21 six-row DM, an actual FREE-action N21 DM4
fixture, Z9 DM4 known-negative checks in both native solvers, and a lower-RSS SIGTERM guard control.
The free fixture has a literal H seed/column permutation and was directly checked on all six row pairs.
It is a calibration witness below the existing baseline, not a new CFR6,21 candidate.
Four disjoint calibration chunks have a whole-task hard retained bound256MiB; no CNF or proof is retained.
No new DRAT-negative claim is allowed merely from an UNSAT solver line. The new disk rule supersedes the
earlier plan to retain calibration proof files; use prior exact negative controls and independent agreement.

## 30. ADD-18 FROZEN (same clock read), before independent GF3 checker target use
Separately authored code/crt3_graycheck_c21v1.c SHA
5c3719fa85dfb2969a19bd1087d74ae07c7d9296c735d3dac90723c359e1a411
was prepared without reading/importing the primary lift program or its results, per its author's report.
It derives the exact F3 equalities/nonzero forms directly from beta triples, uses independent GF3 elimination
with algebraic self-checks, and completely enumerates nonzero inequality coordinates by sparse Gray code.
Ranks above26 or a native bound remain UNKNOWN; any found lift is reconstructed and checked on every DM pair.
No per-assignment allocation, SAT, floating point or retained proof is used. Static data is about481KiB.
The source was compiled with lane TMPDIR, -O3 -std=c11 -Wall -Wextra -Wpedantic; controls are still pending.

Before target use require Q1/K2,K3 complete counts against independent brute force; Q1/K4,K7 negatives;
Sage-structure P21 DM6 mod7 and the pinned Sage33 DM6 mod11 positives; rank-cap and malformed-input controls,
and row/column/row-translation metamorphic agreement. Then check the one explicit common-polynomial beta
pattern (u1,v1,u2,v2)=(1,0,3,0), index364, at Q7,K7, initially native600s, one CPU, tiny retained output.
On a candidate use the SAME existing raw-DM/CFR gate and parent notification policy. A complete zero result
would independently cross-check only this beta pattern, not unrestricted CFR6,21. Any extension through
explicit beta-equivalence tables still needs its own completed audit; the earlier incomplete v1 audit remains
failed, and no duplicate anchor CNF will be regenerated onto disk.


## 31. Owner release, then resource pause — checkpoint 2026-10-17 23:52:37 PDT
Parent23:26: the owner keeps the12GB physical floor and lets lanes throttle; no deletion or snapshot thinning.
Every resumed stage needs a FRESH check showing12.2GB PLUS its projected retained growth. Frozen old-guard
runners are used only ONE STAGE per outer check, never as an unchecked multi-stage queue.
The paused trade verifier settled after SIGTERM:8/10 first-chunk inputs reported complete,153285 neighbours/
65 edges/no clique; its current ninth input and all later chunks remain unfinished. No completed prefix is
discarded, and no claim for all50 independent checks is made.

Observed independent Gray controls so far: Q1/K2 and K3 complete with2 gauged lifts and raw-count expressions
2*3^4 and2*3^5; Q1/K4 completes all4 sign assignments with zero. The known P21 six-row input lifts at
assignment28/64 in FIRST mode, so this is not a complete count. External definition gates and the other
controls are still pending. The seed364 target has NOT been run.

At23:47:17 the next stage was DEFERRED: free12,172,886,016 bytes, below the required12,201,048,576
(12.2GB+1MiB). This is NOT a claimed breach of the12GB physical floor. The parent was notified once;
no new stage or manual free-space poll followed. In-flight single-stage guards still monitor their own
physical floor. Only small checkpoint/review receipts were written. Waiting for parent resource clearance.
Exact checkpoint: notes/resource-pause-234717-v1.json; failed gate: logs/floor-launch-v3-0007.json.

Supervisor v3 SHA4c65bd8d1b90b36bbd8827472b3b91ec53cef4030511eace54ec3555eba78351
received READY for the prior I/O-lifecycle finding by static re-review only. It creates no CNF/proof files
and requires12.2GB+16MiB before launch. This is NOT runtime/calibration acceptance; all native SAT production
remains unstarted. Archived v1/v2/v4 prototypes and old command plans must not be invoked.


## 32. Continuation after parent23:54 release; source preparation recorded 2026-10-18 00:42:14 PDT
Parent restored continuation under a fresh12.2GB PLUS projected-growth gate for each stage. The failed23:47
launch was not silently retried: it remained deferred until that release. No deletion or thinning.
C3-v3 first chunks ended UNKNOWN at5400s: free completed[0,704) of3339 canonical H; fixed completed[0,1095)
of12831. Neither mode is exhausted. The free mode resumes exactly at704 in a new5400s chunk; fixed remains
paused at1095. The completed mu13 involution model and prior completed symmetry/CRT assays are not rerun.
The independent trade verifier completed the interrupted tail2; first10 are now reported complete, while
the next previously unstarted10-input chunk runs as ONE stage behind its fresh outer gate.

The v3 RAM-only producer recovered unplanted paired prime7 (mu1 and6), paired prime13 (mu12), and C3 prime7
(mu2) positives, with definition/action checks and no retained CNF/proof. Its Kissat invocation instead failed
before solving: installed Kissat treats '-' as a literal input path. The failed attempt is retained UNKNOWN,
not a timeout/UNSAT claim. Installed --help says to omit DIMACS for stdin. Version4 changes ONLY that argument
contract and the CLI documentation; the encoder, decoder, safety limits and stop paths are unchanged.
The corrected prime13/mu1 Kissat attempt recovered a verified DM and used the identical CNF SHA as the failed
attempt. No completed CaDiCaL calibration was repeated. Correct callers: controls-plan-v3.json; unsafe/unrun
old plans and run_seq_c21v4.py remain archival, not launch paths.

Seed-intake control and lifted-seed intake both found no new first-row classes; the recovered P21 DM was in
fact byte-identical to the old control. That redundant metadata-only intake is recorded as a deviation; no
neighbourhood or symmetry search was repeated from it. Future digest-identical inputs are not reprocessed.

## 33. ADD-19 FROZEN before catalogue generation or novel-CRT production
Chosen novel family: beta_i(t,c)=i*c+f_t(i) mod7, i,c in F7, t=0,1,2, with f0=0 and each offset f1,f2 zero
at i=0,1. Lift freely in F3 to a cyclic Z21 DM7. This assumes a three-parallel-line quotient only, not a
row automorphism; it is NOT the unrestricted CFR6,21 problem.
Necessary exact ARC condition: f1,f2,f1-f2 each have at most3 points on any affine line, since four rows
with the same projected difference between two columns cannot receive four distinct F3 digits. All7^5
normalized functions are covered, not sampled. Native consumer independently checks catalogue completeness.

Use the exact252-action row/entry normalization and S3 block rebasing specified, with derivations and the
plain-text ABI, in notes/offset-arcs-protocol-v1.txt. First-offset orbit minima, complete stabilizers and
six block orders give deterministic pair representatives. These are proved validity-preserving DM operations,
not scout heuristics or CFR row-isotopy claims. Every decoded witness still needs all actual mod21 differences.

Exclude the ENTIRE completed P23 polynomial2/3 subspace pair family, invariant under these operations.
Also exclude any admissible completed common-slope sampler input justified by replayed INPUT metadata,
never by rerunning the old solver. Unjustified exclusions become explicit holes, not fabricated history.
Thus production explores novel offsets outside the earlier2401-pattern assay; that completed assay is not
repeated merely to obtain another negative. The seed364 independent-verifier target remains unrun for now;
no full-family certification claim is made from its missing check.

Disjoint code-only preparations: gen_offset_arcs_c21v1.py and crt3_offset_batch_c21v2.c. No generation, build or
test occurs in those workers. Main integrates only after both land. Catalogue<=8MiB, text only; no giant
case/action table, per-case process/input file, proof or CNF copy. Initial generation<=600s; initial batch
native1800s (later bounded chunks only by a newly recorded decision), rank cap26. Per-stage retained growth
<=16MiB, fresh12.2GB+growth gate, all lane CPU/RSS/data/3h ceilings unchanged.
Partially processed case resumes at the SAME deterministic key; any cap or time-limited case stays UNKNOWN
and is preserved. A completed selected-family scan is restricted one-program evidence until independently
checked, never unrestricted nonexistence. Candidate acceptance remains the pinned raw7x21 DM SHA, both copied
CFR checkers, position-difference route/DM bridge, cooperative stop, and immediate parent notification.


## 34. Checkpoint 2026-10-18 01:04:59 PDT (host clock read; an initially typed unread01:07 label was corrected)
No CFR6,21 candidate. Running: C3-v3 free resume from canonical704 (5400s chunk); independent trade verifier
part2 (inputs11-20, 5400s); offset-batch source preparation (code only). C3 fixed stays paused at1095.

Versioned queue runner code/run_seq_c21v5.py SHA
cc4b385ac7c1c4ce2939d9252cb303be101b90f1a2924dbfeb3e55f299b238be is v3 plus a FRESH12.2e9+job-growth gate
immediately before every child; failure writes deferred-job.json, exits75, launches nothing further.
Exit10 stops the queue unless --calibration-continue is given; child guard exits70/74/75 always halt.
Self-tests (calib/run-seq-v5-selftest): forced deferral after one job, default candidate stop, explicit
calibration continuation and guard halt all produced the expected exit codes/record counts.

Producer calibration (calib/integration-v4-queue/expectations.json and interpretation.json):
* RAM-only SAT v4 recovered planted FREE-action N21 DM4, planted full odd CFR4,27, Kirtchakov CFR5,25 and the
  P21 six-row DM, plus unplanted C3 prime13, prime7 without centralizer ordering, and all earlier positives.
  No CNF/proof retained; largest observed solver maxrss in calibration was22,183,936 bytes.
* The lower-RSS stop control was SIGTERMed for the intended RSS reason, verdict UNKNOWN.
* Base-mode Z9 DM4 negatives returned UNKNOWN at300s in BOTH solvers. Base mode deliberately leaves the
  whole column symmetry unbroken, so this was an inadequate negative-control design. It is recorded as a
  failed control, not as soundness evidence. Symmetry-broken replacements (C3 N9 DM4 f0/f3, paired N9 DM7)
  plus an unplanted N21 free C3 DM4 positive are now running before any target production.
* New Gray-checker outputs: column reversal, row swap and row translation all reproduced the forward
  Sage33 ranks/complete count; the corrupted-multiplicity input was rejected exit2 for that exact reason.
* Full candidate gates passed for P21-from-Gray, Sage33-from-Gray and all prime13 SAT outputs. Prime7
  outputs pass DM, both CFR checkers and action audit, but the generic mutation helper crashes because it
  swaps column7 (needs n>=8). That is a gate-tool size limitation, not a mathematical gate failure.
Free space at the last launch gate was15,881,555,968 bytes (logs/floor-launch-v3-0029.json).
Replacement controls then finished: C3 N9 DM4 f0/f3 and paired N9 DM7 were UNSAT exit20 (uncertified solver
claims, consistent with Z9 having no DM4); unplanted N21 C3 DM4 f0, f3 and f6 were SAT with directly
verified DMs. Production remains a separately frozen step below.


## 35. ADD-20 FROZEN 2026-10-18 01:04:59 PDT (same host-clock read), before restricted SAT production
Only still-unsettled pure row-action models are targeted; completed groups are not rerun.
* g10: paired (1 2)(3 4)(5 6), mu8, forced fixed count3, canonical columns + unit anchor.
* g00: paired, mu1, forced fixed count1, canonical columns + unit anchor.
* g06: (1 2 3)(4 5 6), mu4, fixed counts0 (canonical columns) and3,6 (canonical columns + unit anchor).
These five fixed-column-action models jointly cover exactly the same restricted actions as the unfinished exact
INV mu8/mu1 and C3 free/fixed runs, with a free first row and no other pruning (sections26,29).
g16/mu13 is already exhausted by the exact enumerator and is NOT rerun here.
Runs: runs/rowcycle-sat-v1/jobs-*.json, encoder2d508f68…a4e6ee, supervisor v4
1d2af356c7c5c09573da7dcc63c29b956736d5f63dbbc4534829755089f1246d, queue v5 above.
CaDiCaL seed1, native1800s initial chunks, at most two such solvers at once, <=16MiB retained each,
RSS stop2.5GiB per child. No CNF/proof retained. SAT => decoded, directly checked DM, queue stop, all
other owned searches cooperatively stopped, full candidate gate, immediate parent notification.
UNSAT => uncertified restricted solver claim only; a certifying proof run may follow ONLY with a separate
disk-gated decision. UNKNOWN never becomes an exclusion. Calibration data: sections34 and calib/*queue*.


## 36. ADD-21 FROZEN 2026-10-18 01:08:56 PDT (queue-end host clock), before novel offset-family production
Integration of ADD-19 (code-only preparations landed01:06): batch source
360e1f1e61d045a4d164022b6914314508fe37f5c07348f4a00c9af96ba6657e built with no compiler output;
generator ae59b04d16700b1113e6458356980e6b3696bae1857e2121a327ecdfb6da5e86 completed in0.50s.
Catalogue runs/offset-arcs-catalog-v1/catalog.txt SHA0d5f4b7665c28e74eb5fb6f656dd7ec274e841508e54ec22916c1a70bafa99ef:
8868 ARC functions of16807 normalized,46 G-orbits, S116, E0 (sampler replay found no admissible
completed identity-slope draw; exclusion status COMPLETE). Independent C validation passed all checks and
enumerated exactly27184 production pair cases; P23 cases excluded7; keys accounted78641424/78641424.
To free a CPU for this, the restricted-certification trade verifier was cooperatively paused at01:06:15
(notes/trade-verifier-priority-pause-v2.json); its completed inputs remain, the interrupted one is redone later.
Calibration (calib/offset-arcs-v1): v2 scalar mode reproduced v1 keys/exit codes on all seven fixtures with
byte-identical witnesses; eight catalogue mutations rejected for their intended reasons; first and last case
keys agree with v1 on extracted beta; two block-order/action transforms keep the canonical key and v1
invariants; single-key trace equals range trace; split chunks sum to the same counts/checksums; wall stop,
rank-cap0 registry and existing-output refusal behave as specified. Typical case: ineq_rank6-12,0.002s.
Production: ONE batch over [0,end), wall1800s, rank cap26, no per-case limit, one CPU, registry only.
Exit10 => stop other owned searches, full candidate gate, parent notice. Exit20 => restricted ONE-program
family zero (independent cross-check needed). Exit30 => UNKNOWN keys retained. Never unrestricted.


## 37. Result + ADD-22 FROZEN 2026-10-18 01:10:35 PDT (batch-end host clock)
Offset-arc production COMPLETE in48.14s: all27184 canonical cases ZERO, no UNKNOWN registry line, keys
78641424/78641424 accounted, case_keys_checksum equal to validate. Ranks: ineq6 for27034 cases,12/18/24 for
the rest. This is a restricted ONE-program exclusion of the common-parallel-line CRT family only.
Structural diagnostic: the known P21 six-row Z21 DM has NO partition of its21 columns into three
(Z7,6;1) blocks mod7 (exhaustive pure-Python check). So block-decomposable CRT families, including this one
and the earlier common-slope/affine families, do not even contain the known six-row structure.

New finite first-row family: DMs containing a LINEAR row triple {0,x,ax}. After normalizing that triple's
first two rows to0,id, f1(x)=ax with a,a-1 units of Z21. Exact R1+translation classes are {2,11,20}
and {5,17}; neither occurs in the56 previously searched first-row classes, and the known P21 DM6 contains no
linear triple (all120 ordered triples checked). Search f1=2x and f1=5x in the calibrated full/non-odd
primary engine (rows6,N21, native10800s, no target symmetry), then the independent point-MRV checker.
A linear sub-DM has at most3 rows here (all slopes must differ mod3), so this is the maximal linear case.
One CPU, queue v5, retained growth<=2MiB. Exhaustion is restricted to this first-row family only.


## 38. Checkpoint 2026-10-18 01:29:00 PDT (host clock) — linear-triple result and a hand lemma
Both full-permutation engines report L2 = EMPTY for f1=2x and f1=5x (primary127.01s, no cap/timeout;
independent point-MRV821.30s, EXHAUSTED-RESTRICTED). So not even a FOUR-row Z21 DM contains a linear triple.
Hand proof (Lemma L3, recorded for review, mod-3 counting only): normalize rows0,r1,r2 with
r2 = 2r1 + const (mod3). For a fourth row g, let n(u,v) = #{columns: r1=u, g=v (mod3)}. Row sums are7
(r1 balanced), column sums7 (g balanced), v-u sums7 (g-r1 balanced), v+u sums7 (g-r2 balanced). These are
all four parallel classes of AG(2,3). Summing the four lines through a point p gives3n(p)+21 = 28, so
n(p)=7/3, not an integer. Hence in ANY (Z21,4;1)-DM no three rows have a columnwise-constant sum mod3.
The linear triple {0,x,ax} with a=2 mod3 is the special case. Two-program agreement plus this argument; no
literature-priority or novelty claim.

Verification launched immediately before this note (01:29, disk gate logs/floor-launch-v3-0037.json):
code/offset_family_crosscheck_c21v1.py SHA7b19929f8980690b18998035219e03504fc4b185db423792280b164e16958320
independently re-enumerates ARC offsets, the252 actions and six rebasings with numpy, compares case count and
splitmix key checksum to the C batch, and solves every selected beta with the separately written primary
crt3_lift_c21v1 solver (10s per pattern, wall7200s). A completed zero is two-program restricted evidence;
UNKNOWN keys stay UNKNOWN. The record is written after launch here, a minor protocol-order deviation.
Free space at gate15.6e9 bytes. Running: C3 free exact, SAT g10/g06-f3, this cross-check (4 busy).


## 39. Checkpoint 2026-10-18 01:44:39 PDT (host clock) and ADD-23 FROZEN before per-H production
Offset-arc family now has TWO-PROGRAM restricted agreement: the independent numpy selector reproduced
N8868, 46 first representatives, exactly27184 cases, 7 P23 exclusions and the same splitmix key checksum
0x1e4772e135464f95; the separately written primary lift solver returned EXHAUSTED-PATTERN for all27184
(847.45s, no UNKNOWN). Still only this restricted common-parallel-line CRT family.

First1800s SAT chunks for g10 (paired mu8 f3) and g06 (C3 f3) ended UNKNOWN by CaDiCaL's native time limit
(signal14 exit, no status line); peak RSS269-320MB. g06 f6 and the hcount/g00 queue are running.

ADD-23: complete the same three restricted models by exact H enumeration plus one tiny SAT call per H.
cycle3_pair_c21v4.c (280a13e5…b074) and involution_pair_c21v4.c (280f7993…a0f) add only an hlist mode
printing every canonical column action in the calibrated deterministic order (unknown run modes now rejected).
code/hsat_driver_c21v1.py (d0312aaf…cf1f) encodes, for one fixed H, ALL21 row pairs directly: one-hot unknown
primary values with g(0)=j(0)=0 gauges, at-most-one constraints for known/unknown differences, and a one-hot
difference table with forward links for every unknown/unknown pair. No pruning beyond the enumerators'
documented normal form and affine-canonical H. CNFs stay in RAM; one native CaDiCaL child at a time, -t per H.
SAT is decoded and checked on all21 pairs before exclusive output. UNSAT is an uncertified claim per H;
timeouts are an UNKNOWN registry. Calibration now running (calib/hsat-v1): hlist counts must equal earlier
hcounts; every n13 cycle3 H must be SAT exactly when the v3 gcount line has count>0; involution prime7/13
positives and Z9 negatives must behave as known. Only after that: production on g06 fixed/free and g10/g00.
The C3 free exact run (v3, resume from704) continues to its native end; it is not resumed further.


## 40. Per-H calibration ACCEPTED (queue ended 01:45:39 PDT); production launched under ADD-23
Both v4 enumerators built with no compiler output. hlist counts equal the earlier hcounts: C3 N21 fixed
12831 (all468198 h), free3339 (841428), n13 mu1/3/9 fixed15 each. New involution totals: N21 mu8 42007
canonical H (of1507077), mu1 15715 (of188181). For each n13 C3 multiplier, the per-H SAT verdict set equals
exactly the set of canonical indices whose independent v3 gcount line has count>0 ({0,5,14}, {0,5,9},
{7,8,11}), with identical h arrays. Involution prime13 mu1/mu12: the first SAT H equals the v3 first-mode
solution's h; prime7 positives SAT; Z9 mu1/mu8 all UNSAT. Every SAT DM was decoded and checked on all pairs.
Typical per-H wall0.01-0.05s at these sizes. Inputs/hashes: runs/hsat-v1/inputs.json.
Production order: g06 fixed (launched), then g06 free, g10 mu8, g00 mu1 as CPUs free; per-H native600s,
chunk wall10800s. Model results remain restricted; UNSAT counts are uncertified per-H solver claims.


## 41. Checkpoint + ADD-24 FROZEN 2026-10-18 02:40:37 PDT (host clock at launch)
Measured costs changed the plan. Per-H SAT (driver v1/v2, both solvers agree on all small calibrations):
g06 fixed ~21-24s/H and free ~41s/H with CaDiCaL (Kissat slower); involution g10 H exceeded600s per H.
The exact v3 DLX is faster (fixed4.9s/H, free7.7s/H). Per-H SAT runs were cooperatively stopped
(notes/hsat-stop-v1.json); their completed175 fixed and68 free indices (all UNSAT claims) lie inside the v3
exact completed prefixes and are retained as an independent second-method sample, not as new coverage.
The whole-model1800s SAT chunks for g06 f6 and g00 were stopped early (notes/whole-sat-early-stop-v1.json),
UNKNOWN. g10 and g00 completion is NOT feasible by these methods before18:20 (42007 and15715 canonical H at
>=9s and >=43s per H). They remain UNKNOWN restricted models; no claim.

code/cycle3_pair_c21v5.c (0e994e9a…dfd2) = v4 + exclusive END canonical index. Calibration (calib/cycle3-v5):
gcount over [2,9) at n13 mu3 reproduces the v3 hg lines exactly; first [1,5) exhausts (exit22,hcompleted4);
[1,6) finds the known positive at index5; mu1 finds index7; END<=SKIP rejected; N21 fixed [1085,1095)
exhausts in53s (5.3s/H), consistent with v3. ADD-24: complete g06 by disjoint exact ranges, native10800s each:
fixed [1095,3295),[3295,5495),[5495,7695) and free [1401,2801) now; afterwards fixed [7695,9895),
[9895,12095),[12095,12831) and free [2801,3339), plus resumes from printed resume indices. Coverage claim only
from the union of COMPLETED ranges with v3's completed prefixes [0,1095) fixed and [0,1401) free.
Restricted model only; a single exact program (v2/v3/v5 lineage) plus sampled per-H SAT cross-check.


## 42. ADD-25 and ADD-26 FROZEN by 2026-10-18 02:45:27 PDT (host clock read right after writing; an unread "02:48" label was corrected; no launch yet)
ADD-25 (cheap independent cross-check of the earlier2401-pattern P23 assay): code/offset_p23_canonical_c21v1.py
recomputes, from the protocol definitions only, the canonical offset pairs with BOTH offsets in P23 (the pairs the
offset batch excluded, expected7) and writes their7x21 beta; the separately written Gray checker v1 then runs on
each (count mode, rank cap26). Coverage of all P23 patterns follows from the same proved actions/rebasings.
This adds a second exact algebraic program to the primary F3 scan and the2384 DRAT receipts; the incomplete
equivalence audit remains failed and is not reused. Launch only when a CPU frees, behind a fresh gate.

ADD-26 (new finite first-row family, unrestricted completions): DMs containing a row triple (0,id,f) where f is a
multiplier-equivariant orthomorphism, f(mx)=m f(x) for m in {2,4,8}. Exact enumeration: 49, 6975 and2527 such
normalized maps; 12, 161 and32 classes under R1+point translation; minus the58 known classes (6 baseline, 50
trade, 2 linear) leaves179 new classes (input specs/equivariant-triples-v1/f1-equivariant-new-classes.txt, SHA in
its record.json). Run them in the calibrated primary full-permutation engine (rows6, N21, native10800s per chunk)
on CPUs left free by short g06 ranges; split into disjoint line chunks, stop on candidate. Independent point-MRV
cross-check only if time remains; otherwise this stays one-program restricted evidence.


## 43. Checkpoint 2026-10-18 04:10:37 PDT — physical-floor stop, all work deferred
Shared free space fell to11,938,119,680-11,938,824,192 bytes (<12GB floor). The v5 queue heartbeats
cooperatively SIGTERMed all four g06 range chunks at04:10:37 (no SIGKILL); all four printed final UNKNOWN
receipts with exact completed ranges: fixed [1095,2213), [3295,4340), [5495,6539); free [1401,2112).
Cumulative exact g06 coverage: fixed [0,2213) U [3295,4340) U [5495,6539) = 4302 of12831 canonical H;
free [0,2112) of3339. No CFR6,21 candidate. Zero native children now; the parent was notified once;
no relaunch or free-space polling until the parent's release. Receipt notes/floor-stop-041037-v1.json.
Pending after release: resume g06 at the printed indices, ADD-25 P23 Gray cross-check, ADD-26 equivariant family.

Trade-family independent cross-check status (read-only comparison at the stop): inputs1-10 (part1 + tail)
and inputs11-14 (part2, paused at input15) reproduce the primary per-input neighbour/edge counts exactly, no
4-clique. Inputs15-50 have primary-only exhaustion. Resume rule: restart part2 at its input5 (line15).


## 44. Consolidated status at the floor stop (all RESTRICTED; no CFR6,21 candidate; no unrestricted claim)
| Family / model | Result | Independence |
|---|---|---|
| 6 baseline P21 first-row classes, any completion | no4-clique (114758/84) | two engines, exact count agreement |
| 50 one-trade first-row classes | no4-clique (963360/406) | primary all50; independent14/50 agree |
| linear row triple {0,x,ax} (2 classes) | L2 empty: not even a DM4 | two engines + hand Lemma L3 (mod-3 count) |
| offset-arc common-parallel-line CRT family | 27184 canonical cases, all zero lifts | C Gray batch + independent numpy selector/primary solver, same count/checksum |
| common-slope P23 subfamily (2401 patterns) | zero lifts | primary F3 all; DRAT2384/2401; Gray check pending (ADD-25) |
| g16 involution mu13 | exhausted | one exact program (prefix+suffix receipts) |
| g06 C3 mu4 | UNKNOWN: fixed4302/12831, free2112/3339 exact; no solution so far | exact DLX; per-H SAT sample agrees |
| g10 mu8, g00 mu1 involutions | UNKNOWN (42007/15715 canonical H; infeasible this round) | — |
| 179 new multiplier-equivariant triple classes (ADD-26) | frozen, not run | — |
Lemma L3 (for review): in any (Z_n,4;1)-DM with 3|n and 9∤n, no three rows have columnwise-constant sum mod3
(four parallel classes of AG(2,3) would force a point weight n/9). Exact resume jobs: runs/resume-after-floor-v1/plan.json.


## 45. Parent release (free14.97e9 at04:14) — four gated lanes resumed 2026-10-18 04:17:35 PDT
Parent instructions: resume runs/resume-after-floor-v1/plan.json in priority order; fresh >=12.2e9+growth gate
before EACH stage (run_seq_c21v5 does this per child); floor trips stay UNKNOWN; resume only from printed
indices; no reruns of completed ranges; restricted wording; Lemma L3 unreviewed; checkpoint by06:30 PDT;
no new science after17:30 PDT. Four sequential lanes (runs/resume-after-floor-v2/layout.json):
A: fixed [2213,3295) -> fixed [9395,11095) -> ADD-26 0-45 -> trade part4
B: fixed [4340,5495) -> fixed [11095,12831) -> ADD-26 45-90 -> trade part5
C: fixed [6539,7695) -> fixed [7695,9395) -> ADD-26 90-135 -> trade part3
D: free [2112,3339) -> ADD-25 (code/p23_gray_stage_c21v1.py) -> ADD-26 135-179 -> trade part2 lines5-10
Deviation (boundaries only): fixed [7695,12831) re-chunked to <=1736 H per native10800s chunk instead of the
plan's2200-H chunks, which would exceed the native limit. The new ranges plus completed ranges tile [0,12831)
and [0,3339) exactly (checked). Any candidate halts its lane; the others are then stopped cooperatively.


## 46. Lemma L3 internal review recorded (after04:18:37 PDT gate; receipt notes/lemma-L3-review-v1.json)
notes/lemma-L3-v1.txt was checked step by step by an internal read-only reviewer agent: verdict CORRECT, no findings
(normalisation, balance, AG(2,3) incidence, N(p)=n/9, linear-triple corollary, k>=4 extension, n=9/27 remark).
This is an internal same-harness review, not an external or cross-vendor one; it executed no computations. As a
separate consistency check, all16170 enumerated canonical C3 4-row Z21 DMs (rows0,t,4h^2,16h) contain no
constant-sum triple mod3. L3 prunes only50/42007 (g10) and45/15715 (g00) canonical involution H, so it does not
make those restricted models feasible. Elementary; may well be known; no priority claim.


## 47. Checkpoint 2026-10-18 05:32:54 PDT (host clock)
No CFR6,21 candidate. All four lanes are on their first g06 range (A fixed [2213,3295), B fixed [4340,5495),
C fixed [6539,7695), D free [2112,3339)); no job has ended yet; latest heartbeats05:32:35, free25.2e9 bytes,
no stop. Parent note (later): causes and recurrence of the free-space dips are UNESTABLISHED; this log makes no
attribution. Next checkpoint when the first lane job ends or within30 minutes, whichever is first.


## 48. Checkpoint 2026-10-18 06:03:37 PDT (host clock)
No CFR6,21 candidate. Completed exact g06 fixed ranges (exit22, hcompleted = range length, no timeout):
[2213,3295) 5587.4s, [4340,5495) 5962.6s, [6539,7695) 5923.3s. Cumulative fixed coverage is now exactly
[0,7695) of12831: [0,2213)+[2213,3295)+[3295,4340)+[4340,5495)+[5495,6539)+[6539,7695), all completed ranges.
Lanes A/B/C are on fixed [9395,11095), [11095,12831), [7695,9395); D free [2112,3339) at canonical2945
(833 completed this chunk). Free space at06:02:35 heartbeats18.44e9 bytes.


## 49. Checkpoint 2026-10-18 06:34:57 PDT (host clock)
No candidate. A fixed [9395,11095): 511 done (resume9906); B fixed [11095,12831): 439 (resume11534);
C fixed [7695,9395): 450 (resume8145); D free [2112,3339): 1081 (resume3193). All ~5.1-5.2s/H fixed and
7.6s/H free, so each range should complete inside its native10800s limit. Heartbeats06:32:35, free17.10e9.


## 50. Checkpoint 2026-10-18 07:05:11 PDT — brief sub-floor dip not sampled
Parent07:02 notice: free ~12.44e9 and falling (cause unidentified); hold new launches. My reply07:02:46: no
bulk writers (resume run tree247,966 B; progress text only). Parent07:05: free fell below12e9 at ~07:04:1x
(11.84e9 seen by another desk) and recovered to14.5e9 at07:04:23; lanes may continue under their gates.
My queue heartbeats run every300s (07:02:35 saw12.43e9; next07:07:35), so this ~10s dip was NOT observed and
no in-flight child was stopped; no launch occurred during the dip. Recorded as a monitoring-granularity limit,
not as a stop. Lane D results: free [2112,3339) completed in9339.2s (exit21, hcompleted1227, hcanonical3339 =
model total, no timeout). With v3 [0,1401) and v5 [1401,2112), the g06 FREE mode is now EXHAUSTED over all3339
canonical H (restricted; one exact program lineage plus the68-index per-H SAT sample). ADD-25 finished: all7
canonical P23 offset pairs ZERO_FOR_THIS_BETA in the separately written Gray checker (exit20, 4.4s), so the
P23 sub-family now has two exact algebraic programs (plus2384/2401 DRAT receipts). D then started ADD-26
chunk135-179 at06:53:18 (heartbeat child-start; gate logged at launch). A/B/C continue fixed ranges (858/795/799).


## 51. Parent07:16-07:17 rules recorded (free near12.0e9; consumer identified OUTSIDE this run by the parent)
New launches: fresh >=12.2e9+growth; LONG jobs (>=60 min) additionally need >=13.5e9 and no >300MB drop in5 min.
Small static writes (notes/receipts/freezes, <=16MiB per action) may proceed. No deletion, thinning or config change.
Lane consequence: my frozen v5 queues A/B/C would auto-launch trade parts3/4/5 (~65 min each, LONG) after their
ADD-26 chunks, without the extra stability test. To comply without editing frozen code, I will cooperatively
SIGTERM runners A/B/C while their (short, ~47 min) ADD-26 chunks run, record each stopped chunk UNKNOWN with its
completed f1 lines, and later relaunch only the unfinished ADD-26 lines as short single-job queues, and the trade
inputs as <=5-input (~33 min) chunks, each behind a fresh gate. In-flight g06 ranges are NOT stopped. Lane D's
next job (trade part2 lines5-10, ~39 min) is short and stays queued. Results ledger: notes/results-ledger-v1.json.


## 52. ADD-27 FROZEN after parent07:19 release (static freeze; nothing launched by this section)
Free rose to ~189.5e9 at07:17 (parent). New science stops17:30, native work must end by17:57 PDT; my frozen
runners' own stop is18:20, so every chunk will be sized/launched to end before17:57.
ADD-27: second multiplier family, same exact method as ADD-26. f(13x)=13f(x) (13 == 1 mod3, -1 mod7): 90207
normalized equivariant orthomorphisms, 892 R1+translation classes; excluding the58 known and179 ADD-26 classes
leaves871 new classes (specs/equivariant13-triples-v1/record.json with input/chunk SHA-256). Run in the same
primary full-permutation engine as22 disjoint chunks of <=40 classes (~41 min each: SHORT), after ADD-26 and the
trade cross-check, one-program restricted evidence. Trade inputs21-50 become six5-input chunks (~33 min each).
All future jobs are therefore <60 min; the long-job stability rule is avoided rather than relied upon.


## 53. g06 COMPLETE (restricted) + lane restructuring, checkpoint 2026-10-18 08:26:25 PDT
Final g06 fixed ranges: [7695,9395) 8704s exit22, [9395,11095) 8740s exit22, [11095,12831) 8879s exit21
(hcompleted1736, hcanonical12831 = model total); none timed out/overflowed. Fixed mode coverage is the exact
tiling [0,12831): v3 [0,1095) + v5 [1095,2213),[2213,3295),[3295,4340),[4340,5495),[5495,6539),[6539,7695),
[7695,9395),[9395,11095),[11095,12831). Free mode [0,3339) (section50). RESULT: no (Z21,7;1)-DM is invariant
under the pure row action g06 = (4,(1 2 3)(4 5 6)), in either column-action mode, per this ONE exact program
lineage (v2 h-enumeration/affine canonicalization, v3/v5 nested5-map DLX), with per-H SAT agreement on a
175+68-index sample. Restricted symmetry model only; not independently re-enumerated in full.
ADD-26 chunk135-179 finished (44/44 inputs exhausted, no overflow/timeout, 3148.77s). Trade inputs15-20
(lane D) agree exactly with the primary counts, so trade inputs1-20 now have independent agreement.
At08:25:04/08:25:41 runners A, C, B were SIGTERMed inside their ADD-26 chunks (notes/lane-stop-long-rule-v1/v2.json)
so they could not auto-launch LONG trade parts; completed f1 lines kept: chunk0-45 lines1-8, chunk90-135
lines1-3, chunk45-90 none (each interrupted f1 is redone). New short-job lanes runs/after-g06-v3 (layout.json):
E/F launched08:26 (ADD-26 remainders, trade5-input chunks, ADD-27 chunks); G/H to follow, staggered.


## 54. Checkpoint 2026-10-18 08:57:22 PDT (host clock)
No candidate. Lanes E/F/G/H (launched08:26:25-08:26:44) on their first jobs: ADD-26 remainders 8-45, 93-135,
45-90 and trade part4b; no job ended yet; heartbeats08:56, free ~179.4e9, no stop/deferral.
Results ledger updated: notes/results-ledger-v2.json (supersedes v1).


## 55. Parent-requested checkpoint inventory (x-created 2026-10-18 09:11:37 PDT, the file's own clock field)
notes/checkpoint-inventory-v1.json (SHA256 21de235581971fbc9706c9f14417c548ffd11e1ed6c47fd9fa5176219205faea):
exhausted vs unfinished domains, no candidate, active runner/child PIDs, source and result SHA-256 values,
next bounded step. It keeps restricted exhaustion separate from the still-OPEN unrestricted CFR(6,21).
No run was stopped to produce it.


## 56. External simultaneous SIGTERM at 09:25:51 PDT; ADD-26 COMPLETE; relaunch 09:27:22-09:27:32
All four after-g06-v3 runners received SIGTERM within0.1s at09:25:51 (stop_reason "owned SIGTERM/SIGINT
forwarding"), together with loss of my eval-kernel state; the parent reports the same instant for several of its
own jobs, cause NOT ESTABLISHED. I did not send it. Each runner forwarded SIGTERM and recorded its child; no SIGKILL.
Completed before the stop (verified per input, no overflow/timeout, no 4-clique "deep0"):
ADD-26 remainders8-44 (37 inputs,2293.42s), 93-134 (42,2600.60s), 45-89 (45,3075.92s). With chunk135-179 and the
earlier completed lines0-7 and90-92, ALL179 ADD-26 classes are exhausted: no (Z21,7;1)-DM contains a row triple
(0,id,f) with f equivariant under x->2x, 4x or 8x (up to the proved R1+translation equivalence); one program.
Trade independent checks completed: part4b (inputs36-40, exit20); partial (UNKNOWN, interrupted): part3a inputs21-23
done, part3b26-27, part4a31, part5a41-44; all completed inputs equal the primary counts. So inputs1-23, 26-27, 31,
36-44 are now independently confirmed; remaining24-25, 28-30, 32-35, 45-50.
Relaunched as NEW runs (runs/after-stop-v4/layout.json), lanes I-L, each behind a fresh statvfs gate
(logs/floor-launch-v4-*.json): remaining trade inputs (4 short chunks) then the22 ADD-27 chunks (<=41 min each).
The eval kernel was re-initialised from scratch; no state was inferred from the transcript.


## 57. Checkpoint 2026-10-18 10:02:02 PDT (host clock)
No candidate. Trade remainders t24-25, t28-30, t32-35 finished exit20 and equal the primary per-input counts;
lane L runs t45-50. Lanes I/J/K now run ADD-27 chunks0-40, 40-80, 80-120. Heartbeats09:57, free ~149.9e9,
no stop/deferral/guard. Results ledger v3 (ADD-26 complete): notes/results-ledger-v3.json. Parent incident
request answered: I sent no signal in09:25:45-09:26:00; observed interruptions are listed in section56.


## 58. Checkpoint 2026-10-18 10:32:40 PDT — trade family now two-program; ADD-27 80/871
t45-50 finished (exit20, 2321s) equal to the primary counts. All50 one-trade first-row classes are now
independently confirmed by the point-MRV engine (inputs1-23, 24-25, 26-27, 28-30, 31, 32-35, 36-40, 41-44,
45-50 across runs three-trades-crosscheck-v1/v2, resume-after-floor-v2, after-g06-v3, after-stop-v4), with
identical per-input neighbour/edge counts and no4-clique: a TWO-PROGRAM restricted exhaustion.
ADD-27 chunks0-40 (2484.07s) and40-80 (2478.52s): 40/40 inputs each exhausted, no overflow/timeout, deep0.
Running: I add27-160-200, J add27-200-240, K add27-80-120, L add27-120-160; heartbeats10:32, free ~147.7e9.


## 59. ADD-28 FROZEN (static; not launched until ADD-27 lanes free CPUs)
Deterministic sample cross-check of the one-program ADD-26/ADD-27 exhaustions with the independent point-MRV
engine: ADD-26 classes0,6,12,... (30 classes) and ADD-27 classes0,22,44,... (40 classes), in14 chunks of <=5
classes (specs/sample-crosscheck-v1/record.json with SHA-256s). Acceptance per input: identical L2 neighbour and
edge counts to the primary engine and no4-clique; any mismatch is reported, not averaged away. This is sample
agreement only: it does not turn the unsampled classes into two-program results. Short jobs, fresh gates,
no launch after17:30, native end by17:57.


## 60. Checkpoint 2026-10-18 11:04:52 PDT (host clock)
No candidate. ADD-27: 200 of871 classes exhausted so far (every finished chunk 40/40 inputs, no overflow/timeout,
deep0); lanes on chunks320-360, 200-240, 240-280, 280-320. Heartbeats11:02-11:03; free119.4-122.7e9 (falling
from147.7e9 at10:32; my lane's outputs are KB-scale; no attribution). No stop/deferral/guard/candidate.


## 61. Checkpoint 2026-10-18 11:35:22 PDT (host clock)
No candidate. ADD-27: 280/871 classes exhausted (all finished chunks verified). Lanes on chunks320-360, 360-400,
400-440, 280-320. Free87.8e9 at11:32 heartbeats (falling ~1e9/min; not from this lane, no attribution).
If the floor is reached the queue guards stop cooperatively; interrupted chunks stay UNKNOWN and resume by line.


## 62. Checkpoint 2026-10-18 11:56:16 PDT (host clock; parent status request answered)
No candidate of any kind. ADD-27: 400/871 classes exhausted. Owned runners (pid=pgid) I60240, J60241, K60287,
L60288 with cfr_perm_search_c21v1 children39297, 43048, 44389, 30316 (same pgid). Expected ADD-27 end ~13:55,
then ADD-28 sample cross-check to ~16:00; no launch after17:29, all native work ends before17:57.


## 63. Checkpoint 2026-10-18 12:26:58 PDT (host clock)
No candidate. ADD-27: 520/871 classes exhausted (all finished chunks verified). Lanes on chunks640-680,
520-560, 560-600, 600-640. Free58.8e9 at12:26:09 (lane I heartbeat), 74.5-75.1e9 at12:22; still falling,
no attribution; no stop/deferral/guard.


## 64. Checkpoint 2026-10-18 12:57:48 PDT (host clock)
No candidate. ADD-27: 600/871 classes exhausted. Lanes on chunks640-680, 680-720, 720-760, 600-640.
Free29.38e9 at12:57 heartbeats, falling ~1e9/min (external; no attribution). If the gate/floor trips, the
queue guards defer or stop cooperatively; such items are recorded UNKNOWN and resumed by line after release.


## 65. Checkpoint 2026-10-18 13:24:04 PDT (host clock)
No candidate. ADD-27: 760/871 classes exhausted; lane K finished its five chunks; I/J/L run800-840, 840-871,
760-800. ADD-28 lane M (sample chunks0,4,8,12) launched13:24:04 on K's CPU behind a fresh gate (free26.44e9);
lanes N/O/P start as I/J/L finish (runs/sample-crosscheck-v1/layout.json).


## 66. ADD-27 COMPLETE 2026-10-18 13:52:16 PDT; ADD-28 admissions (checkpoint 13:52:26)
All22 ADD-27 chunks finished; all871 new multiplier-13 classes exhausted (each chunk: every input exhausted, no
overflow/timeout, deep0; totals L2 17,633,194 neighbours, 10,336 edges). RESULT (restricted, one program): no
(Z21,7;1)-DM contains a row triple (0,id,f) with f(13x)=13f(x), up to the proved R1+translation equivalence.
With ADD-26, every multiplier-equivariant triple family except the odd one (m=20, far larger) is excluded.
ADD-28 admitted lanes (short chunks, fresh statvfs gate each; logs/floor-launch-v4-0104..0106.json):
M 13:24:04 (26.42e9), N 13:40:01 (25.65e9), O 13:48:42 (23.02e9). Lane P NOT_STARTED: free19.90e9 at13:52:26
and falling fast; no stacking, no automatic retry. Parent tranche message sent once.


## 67. Checkpoint 2026-10-18 14:13:25 PDT (host clock)
Parent notice: its monitor saw11.985e9 at14:07:50 (<12e9) and14.99e9 at14:11:51. My lane heartbeats did not
sample that breach (M14:09:05 saw12.73e9; N minimum12.50e9; O14:08:42 saw13.55e9), so no in-flight child was
stopped; recorded as a monitoring-granularity limit, not a stop. N's next chunk launched14:13:09 behind its own
fresh gate (free14.96e9). ADD-28 first results: add26-sample-0-5 (classes0,6,12,18,24) and add26-sample-5-10
(30,...,54): exit20, per-input L2/edge counts EQUAL the primary engine, no4-clique. Lane P stays NOT_STARTED.


## 68. Floor stop observed 2026-10-18 14:20:01 PDT (lane N heartbeat)
Lane N's heartbeat read free11,900,555,264 B (<12e9) and cooperatively stopped add26-sample-25-30 after412s
(SIGTERM forwarded, child-end logged). Its first class (ADD-26 index150) completed and equals the primary counts;
classes156,162,168,174 are UNKNOWN (not started/unfinished). Lane N ended; parent notified once; no retry.
M (add26-sample-20-25) and O (add26-sample-10-15) remain in flight under their own guards. P NOT_STARTED.


## 69. Floor stop observed 2026-10-18 15:23:42 PDT (lane O heartbeat)
Lane O read free11,543,990,272 B (<12e9) and cooperatively stopped add27-sample-20-25 after1822s: ADD-27
classes440,462,484,506 completed and equal the primary counts; class528 UNKNOWN. Lane O ended; no retry.
Completed before: add26-sample-10-15 and add27-sample-0-5 (all equal). M continues add27-sample-30-35 under its
guard (launched15:01:53 with free14.23e9 at its own gate). Lane P NOT_STARTED; N's add27-sample-15-20/35-40 NOT_STARTED.


## 70. Closeout — /bin/date 2026-10-18T15:24:31-0700; final summary notes/final-summary-v2.json
Lane M was floor-stopped at15:24:05 (11.52e9) inside add27-sample-30-35: ADD-27 classes660,682,704 equal the
primary counts; 726,748 UNKNOWN. No owned native process remains (ps on all recorded runner PIDs, 15:24:10).
No further launches: the parent forbids sample extensions/retries without a separate GO, and no launch is allowed
at/after17:29.
Final summary (create-only): notes/final-summary-v2.json SHA256
53f5ac427c59e0142dacd2081a28ad37a2961f91f613307060e170074da6b629 (v2 supersedes v1
637394eef7eb89dc24cbf00ce6c11449fcdec45e6b9ee4e060f5681b81c7d3c7 only to drop a never-created receipt path).
It lists every result, guard and stop receipt with SHA-256; exact ADD-28 boundaries (ADD-26 sample: 21 equal,
4 UNKNOWN, 5 NOT_STARTED; ADD-27 sample: 17 equal, 3 UNKNOWN, 20 NOT_STARTED; 0 mismatches); the process census
(59 heartbeat-logged queues, 200 child intervals, peak4 concurrent); the admission census (61 outer gate receipts,
1 denied, 0 deferred-job files); and all deviations, including the disclosed re-chunking of trade parts3-5.
CFR(6,21) itself remains OPEN here: no candidate, and no unrestricted nonexistence claim.

