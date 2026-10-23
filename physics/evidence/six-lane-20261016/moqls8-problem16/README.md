# phys-1 lane: Ball–Simoens Problem 16 at n = 8 (is every set of 5 MOQLS(8) classical?)

Frozen contract: institute/runs/six-lane-2026-10-16/screening/phys-1-moqls8-problem16-contract.json (05:16:00 PDT).
Sources (copies of the pinned files): sources/quantum-latin-2607.12933v2.pdf (2d60d45f…21afe),
sources/1406.3681v2.pdf (Egan–Wanless, f01b494f…7e0), text extractions alongside.

## 0. Frozen protocol (written 2026-10-17 ~05:40 PDT, before any n = 8 computation)

Conventions: rows, columns, symbols, coordinates 0..7; row 0 is the reference row; standard form w.r.t. row 0
(Ψ_s(0,j) = |j⟩); supp/weight w.r.t. the computational basis; definitions of QLS, orthogonality, classical sets as
in the n = 7 lane (source §2.2–2.3).

Route to a positive answer (each step written or certified):
- (W8) Off row 0 the five supports at a cell are pairwise disjoint subsets of [8]∖{j}: Σ_s w_s ≤ 7, so every weight is
  ≤ 3; a weight-3 entry forces weight 1 in the other four squares (supports partition [8]∖{j}); at most two weight-2
  entries share a cell.
- (A8) If all weights are ≤ 2 (row-0 frame), the set is classical. Planned written proof WITHOUT any MOLS
  classification: for a distinguished square Ψ1 apply Lemma 10 to the other four first (Ψ1 becomes an ONB on the
  lines of 6 classes: rows, columns, 4 classical squares), then to Ψ1; the cells with support exactly {a,b} meet
  every line of these 6 classes in 0 or 2 cells (Lemma 3) and lie in the 16 cells where the classical replacement of
  Ψ1 is a or b; each a-cell is joined to 6 distinct b-cells of 8, so this bipartite graph is connected (two a-cells
  share ≥ 4 neighbours); the row-0 cell (0,a) has weight 1, so no weight-2 entry exists. (General form: n − 3
  squares, 2(n − 2) > n.)
- Reduction: S′ := Lemma 10 applied to every square without a weight-3 entry; m := number of squares with a
  weight-3 entry; m ≥ 1 by (A8); class K_m = m quantum + (5 − m) classical squares, every quantum square with a
  weight-3 entry in the row-0 frame (P4). S′ need not be isotopic to S.
- (B8) = class K1: the 4 classical squares are 4-MOLS(8); Egan–Wanless Table 6 (n = 8, k = 4: one paratopism class;
  the linear set c + a·r, a ∈ 4 distinct nonzero elements of GF(8), is a representative) identifies their 6-net with
  six direction classes of AG(2,8). PGL(2,8) is 3-transitive on the 9 directions and the stabilizer of a 3-set acts
  regularly on its 6-point complement, so one FIXED instance (AG 6-net, frame = a line of one class) covers K1. Char 2
  breaks the n = 7 linear-class argument (|A(q) ∩ A(q′)| ∈ {0, 2}); K1 is decided by SAT unless a written proof is
  found.
- K2..K5: GENERIC encodings (classical squares as MOLS(8) variables, first row identity), conditions (P1)–(P4) as in
  the n = 7 lane (README §2 there) with 8 in place of 7, plus (SB2_8) at cell (1,0): Ψ1's weight-3 entry at (1,0);
  classical symbols 1, …, 5 − m there; S1(1,0) = the three smallest remaining coordinates; one singleton each for
  Ψ2..Ψm (forced: 3 + (m − 1) + (5 − m) = 7); encoder A additionally sorts rows 2..7 by the first classical square's
  column 0.
- Decision rule: K1..K5 all UNSAT (two independently written encoders = the n = 7 encoders A and B generalized to
  order 8, two solvers, DRAT checked by drat-trim) ⇒ every set of 5 MOQLS(8) is classical. Any SAT ⇒ decode the
  pattern, run the direct checker, then attempt exact unitary completion (a SAT pattern is NOT a counterexample).
- Route to a negative answer: an explicit exact non-classical set of 5 MOQLS(8), checked by two exact checkers.

Controls (contract): Theorem 5 for 6 MOQLS(8) (written: weights ≤ 2 automatically; (A8) argument with 7 classes);
the complete classical set of 7 MOLS(8) certified classical (8 rays per square); a non-classical MOQLS(8) pair from
the source's construction certified non-classical (> 8 rays) by two exact checkers; relaxed SAT controls (classical
configurations accepted by each encoder); fixed-pattern mutation controls; solver errors/timeouts fail closed.

## 1. Compute and disk plan (frozen)
- ≤ 4 CPU processes, ≤ 8 GiB RSS, chunks ≤ 3 h, checkpoints ≤ 30 min.
- Disk: free space on the volume at lane creation was 52 GB (95 % used). Lane cap 10 GiB in total. Exploratory and
  first solves: NO proof output. Proof runs only for instances already solved UNSAT, with binary DRAT streamed
  through zstd (proof.drat.zst; checked through a pipe/FIFO into drat-trim), and a size watchdog that STOPS the
  solver if the compressed proof exceeds 3 GiB (the partial file is kept). Nothing is ever deleted or moved out of
  the lane; if the cap would be exceeded, runs are stopped and the parent is asked.

## 2. All-frames Gram-pattern formulation (written 06:3x PDT; NOTE: its first exploratory run, GA-K5, started at
06:31:06, minutes BEFORE this text was written; the specification below is exactly code/gram_a.py at that time)
Variables g_s(p,q) = [⟨Ψ_s(p),Ψ_s(q)⟩ ≠ 0] for quantum squares, all pairs of cells. Necessary conditions:
G1 zero on common lines; G2 (Prop 1) no pair nonzero in two squares; G3 for any two fixed lines (rows/columns, and
classical lines in FIXED mode) the overlap pattern is the support of a unitary (nonempty rows/columns; no two rows or
columns sharing exactly one entry); G4 for a fixed line l and p, q ∉ l: |{a ∈ l : g(a,p) ∧ g(a,q)}| = 1 ⇒ g(p,q) = 1
(single Parseval term) and = 0 ⇒ g(p,q) = 0 (Parseval); P4 in frame row 0; SB2 as in §0 via g_s((0,k),(1,0)).
Every condition is implied by the configuration's actual inner products (canonical assignment), so UNSAT of a K_m
instance is sound. It is at least as strong as the single-frame (P1)–(P4) encoding (row 0 is one of its frames).
Validation so far (evidence/gram_dev_v1): the exact Gram patterns of the genuine n = 8 Theorem-6 pair (Z2×Z4) and
the n = 7 Corollary-7 pair pass a direct evaluator (code/gram_check.py, 0 violations) and are SAT as fixed patterns.
Status: exploratory until a second independent implementation and controls exist.

### §2 addendum (written 07:35 PDT (host clock), after the 07:04 G5 runs were launched; the code at launch is recorded by SHA in
the run directories)
- G5 (same ray): if in the frame of a row/column l the support of q is exactly {a}, then Ψ_s(q) ∝ Ψ_s(a) and
  g_s(p,q) = g_s(p,a) for every other point p. Necessary (equal rays have equal overlap patterns).
- (P4-all-rows) for class K_m it is legitimate to require a weight-3 entry of EVERY quantum square in EVERY row frame
  once A8 and the classes K_1..K_{m−1} are excluded: if a quantum square had none in frame r, Lemma 10 in frame r
  turns it classical and leaves m − 1 non-classical squares in a row-r standard form, i.e. a member of K_{m′} with
  m′ < m (after the same reduction in frame r) or a set to which A8 applies. Row permutations make every frame
  equivalent to row 0. Used so far only for K2 (needs A8 and K1 = ∅ only).
- Second implementation: code/gram_b.py (GB) implements G1–G5, P4 (row 0 or all rows), SB2 independently.

## 3. Amendment (frozen 2026-10-17, host time printed below, BEFORE any fixed-net K2 SAT run): K2 by the 39 E–W nets
- Data: Egan–Wanless species representatives of 3-MOLS(8) (their data page, ref. [36] of arXiv:1406.3681v2,
  http://users.monash.edu.au/~iwanless/data/MOLS/, returned HTTP 503 on 2026-10-17); Wayback Machine captures:
  maxMOLS8.3.txt (20191225120510; SHA-1/base32 AEUWGV6W…54XZ = CDX digest) and nmaxMOLS8.3.txt (20191225172426;
  SBV375NG…YESS), plus format notes LSformat.html, stored in sources/ew_data/. 38 maximal + 1 non-maximal species =
  39 = E–W Table 6 (n = 8, k = 3, paratopism column). Completeness of the catalogue is an imported (computer) claim.
- Local consistency checks (code/ew_nets*.py → evidence/k2_fixed/): Latin + mutual orthogonality of all 39 triples;
  no fourth orthogonal square for the 38 maximal ones and one for the non-maximal one (SAT); pairwise
  non-isomorphism via invariants (intercalates, transversal counts of all 3- and 4-class subnets, common
  transversals, cycle types, extendability) and a direct VF2++ incidence-graph test for any pair those invariants
  do not separate.
- Reduction: for a K2 configuration S′, its 5-net (rows, columns, 3 classical symbol classes) is net-isomorphic
  (paratopic) to one representative R_k; by the regridding Lemma R (review/PROOF_N8_PARTIAL.md) the quantum squares
  transport to R_k's gridding as ONBs on all 40 lines, still mutually orthogonal (the set of 64 tensor products is
  unchanged by re-indexing points) and non-classical (ray count unchanged). By A8 and K1 = ∅ (applied after
  regridding with the frame's class as rows), BOTH quantum squares have a weight-3 entry in the frame of EVERY line;
  in particular in R_k's row 0. Hence the FIXED instance FK2(R_k) — classical squares R_k (symbols relabelled so that
  row 0 is 0..7), two quantum squares with (P1)–(P4) in the row-0 frame — must be SAT. All 39 UNSAT ⇒ K2 = ∅.
- Encoders: code/enc8_a2.py and code/enc8_b2.py (enc8_a/b plus --squares for explicit fixed classical squares;
  clause families unchanged). Pilot first (measured: 2 nets, both encoders), then all 39; proofs through
  code/proof_run.py (zstd, watchdog); fail-closed; timeouts are UNKNOWN.

## 4. Amendment (frozen before any K3 run; host time printed below): K3 by the 2165 E–W 2-MOLS(8) nets
- Data: Wayback copies of maxMOLS8.2.txt (2127 maximal species; SHA-1/base32 IAJ7HVHB…7K3P = CDX digest, identical
  in captures 2016–2025) and nmaxMOLS8.2.txt (38 non-maximal; CW3S3KKP…VWRK); 2165 = E–W Table 6 (n = 8, k = 2).
- Checks: Latin + orthogonality of every pair; a third orthogonal square exists exactly for the 38 non-maximal
  (exact SAT, streamed); nauty certificates of the 4-net incidence graphs pairwise distinct.
- Reduction: in K3 every quantum square has a weight-3 entry in the frame of EVERY line of the 4-net (regrid with the
  frame's class as rows; the frame-ℓ reduction leaves m_ℓ non-classical squares with m_ℓ ≥ 1 by A8, ≠ 1 by K1 = ∅,
  ≠ 2 by K2 = ∅, and m_ℓ = 3 forces all three to have weight-3 entries). Hence one row-0-frame FIXED instance per
  net: classical squares = the pair (row 0 = 0..7), three quantum squares with (P1)–(P4); all UNSAT ⇒ K3 = ∅.
- Storage plan (disk): CNFs are not stored (deterministic regeneration by code/run_fixed_k3.py from the encoders and
  the squares; SHA-256 of the exact DIMACS recorded); encoder A8r2 instances solved with CaDiCaL and their DRAT proofs
  stored zstd-compressed and checked by drat-trim (CNF streamed through a reusable lane FIFO, proof from stdin);
  encoder B8r2 instances solved with kissat without proofs (status + CNF SHA-256). Pilot (measured) before the batch;
  stop before the lane exceeds 10 GiB.

## 5. Amendment (frozen before any K4/K5 minimal-case encoding; host time printed below): minimal counterexamples
- Suppose a non-classical set of 5 MOQLS(8) exists and choose one, S, with the smallest number m* of non-classical
  squares. By K1 = ∅ (analytic lemma K1-AG with the E–W Table 6 bridge, or the FIXED K1 certificate) m* ≥ 2.
- Minimality ⇒ ALL-FRAMES P4: for every line ℓ of the net of S (rows, columns, classical symbol lines) every
  non-classical square of S has a weight-3 entry in the ℓ-frame. Otherwise regrid with ℓ's class as rows and ℓ as row
  0 (Lemma R), apply Lemma 10 in that frame to the square lacking weight-3 entries (its weights are ≤ 3 by W8, hence
  ≤ 2): the result is a set of 5 MOQLS(8) with m* − 1 ≥ 1 non-classical squares — contradicting minimality.
  This is a statement about MINIMAL counterexamples only; it is not claimed that every set with m non-classical
  squares satisfies all-frames P4.
- Encodings "K_m-minimal": the K_m generic encoding plus P4 for every quantum square in every row frame and every
  column frame (frames of the variable classical lines are omitted, which only weakens the instance). An UNSAT
  K_m-minimal instance excludes m* = m. Results are labelled MINIMAL-counterexample exclusions; the theorem follows
  once K1 and every K_m-minimal (m = 2..5) are excluded and accepted (K2, K3 are excluded through the fixed-net
  route of §3/§4, whose all-frames P4 justification is the special case of this argument).
- Instances: K4-minimal (GA r2: --quantum 1234 --ngeneric 1 --p4 1234 --p4-all-rows --p4-all-cols --sb2 --g5) and
  K5-minimal (GA r2: --quantum 12345 --ngeneric 0 --p4 12345 --p4-all-rows --p4-all-cols --sb2 --g5 --rowlex);
  proof-free exploratory solves first (≤ 3 h), then certificates and the second implementation GB.

## 6. Amendment (frozen before any K4 cube-and-conquer run; host time printed below): K4-minimal by CnC — PILOT
- Base CNF F = evidence/kmin_v1/GA2_K4min.cnf, SHA-256 89082e605090d747ea0af351f4f3287ce29bd219542bc8ab6effa083d2f6296e,
  411712 vars, 4726836 clauses, generated by code/gram_a_r2.py (SHA-256 7dfdf885…c028) with
  `--order 8 --mode generic --quantum 1234 --ngeneric 1 --p4 1234 --p4-all-rows --p4-all-cols --sb2 --g5`.
- Active constraint families and their justification: Latin/standard-form/row-sort constraints on the one classical
  square L (L(0,j) = j; rows 2..7 sorted so that L(i,0) = i — a permutation of rows 2..7, lossless after SB2);
  G1 (zero Gram entries on rows, columns and the variable L-lines), G2 (Prop 1 between the 4 quantum squares), G3
  (necessary unitary-pattern conditions for every pair of row/column lines), G4 (Parseval: single shared frame point ⇒
  nonzero; none ⇒ zero; row/column frames), G5 (same ray: frame support {a} ⇒ identical overlap pattern with a),
  README §2 + addendum; P4 for every quantum square in EVERY row and column frame — valid for a minimal counterexample
  (README §5; K1–K3 are excluded anyway); SB2 at cell (1,0) (README §0: L(1,0) = 1, row-0-frame overlaps of (1,0):
  Ψ1 → {2,3,4}, Ψ2 → {5}, Ψ3 → {6}, Ψ4 → {7}). The generic GA/G5/SB2 soundness is to be reviewed by the parent before
  any full batch.
- Cubes: march_cu (env/cnc, SHA-256 f2ba6de7…d85e, built from github.com/marijnheule/CnC commit 705b60c) run on F with
  a static depth -d D, cubes written to the lane (iCNF lines "a l1 … lk 0", order as emitted; file SHA-256 recorded).
  Overlapping cubes are allowed. Completeness of the split is CHECKED, not assumed: the cover formula
  F ∧ (¬c_1) ∧ … ∧ (¬c_K) (one clause per cube) must be UNSAT with a verified proof; then every assignment of F lies in
  some cube.
- Per cube: CNF bytes = header (V, C + |c|) + F's clause bytes + one unit clause per cube literal, SHA-256 recorded,
  streamed to CaDiCaL; its binary DRAT streamed into drat-trim (proof from stdin, -i); strict status = solver exit 20 AND
  "s VERIFIED" without "NOT VERIFIED"; anything else (SAT, timeout, cap) is UNKNOWN (code/cert_stream.py; replay
  receipt per cube; no proofs stored in the pilot).
- PILOT (≤ 15 min wall, ≤ 4 CPU including the running K5-minimal solve): march with a small depth, a handful of cubes
  and the cover formula with short limits; report projected runtime/resources before any batch.

## 7. Amendment (frozen before the K4 run; host time printed below): K4-minimal with the classical square as a
## weight-1 Gram square — ONE proof-free solve, exploratory only (parent decision 13:1x)
- Encoding code/gram_a_r3.py (GA r3 = GA r2 + --weight1): five Gram-pattern squares on the 2-net of rows and columns;
  square 5 is the classical square L, constrained to weight exactly 1 at every off-row-0 cell (at most one nonzero
  overlap with row 0; at least one is implied by G3). Soundness: a classical square in standard form has weight 1
  off row 0 and Gram pattern g_5(p,q) = [L(p) = L(q)]; as a QLS it satisfies G2–G5 like any square, and Prop 1/G2
  between square 5 and the Q's is exactly "Q is an ONB on the L-lines" at the pattern level. No one-hot L variables.
- P4 on squares 1–4 in every row frame and every column frame (minimal counterexample, README §5); none on square 5.
- SB2 for K4 (written soundness): in a K4-minimal configuration in row-0 standard form, by (α) rows 1..7 and (β) column
  permutations with relabelling, move a weight-3 entry of Q1 to (1,0); L(1,0) ≠ 0 is sent to 1 by σ fixing 0; the
  allowed coordinates at (1,0) are then {2,…,7}: Q1 takes three and Q2, Q3, Q4 one each (W8, disjointness), so σ fixing
  0, 1 makes S1(1,0) = {2,3,4}, S2(1,0) = {5}, S3(1,0) = {6}, S4(1,0) = {7}; finally (α) on rows 2..7 sorts L's column 0
  (it contains {2,…,7} there), i.e. g_5((0,i),(i,0)) = 1 for i = 2..7. Each step fixes what the earlier ones set.
- G1 (rows/columns), G2, G3 and G4 over row/column lines, G5 as in §2. No row lex-leader (the row sort replaces it).
- Run: `--order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 1234 --p4-all-rows --p4-all-cols --sb2 --g5
  --weight1 5`, CaDiCaL proof-free, 1 CPU, native limit ≤ 3 h. Result label: EXPLORATORY (not acceptable as proof).
- Relaxed positive control (13:14:12–13:14:22): same encoding without P4/SB2 (--p4 none) SAT in 1.4 s
  (evidence/ga_r3_dev_v1).

## 8. Amendment (frozen before any K5 split run; host time printed below): certifiable split of the unconditional K5
- Base CNF F = evidence/gram_dev_v1/GA5L_K5_sb2.cnf, SHA-256 6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b
  (509915 vars, 5740230 clauses), regenerable with code/gram_a.py (SHA-256 bf1aada1…d05a, unchanged since generation)
  `--order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex`. Constraints: G1–G5 over
  rows/columns, P4 for all five squares in the ROW-0 frame only (unconditional: the reduction gives it for every
  non-classical set with m = 5, no minimality used), SB2 (K5) and the row lex-leader; the parent reviews generic
  G5/SB2/rowlex soundness before any full run.
- Split (coverage by construction): declared variable set V = the seven Gram literals g_1((0,k),(2,0)), k = 1..7
  (DIMACS variables 57, 106, 155, 204, 253, 302, 351 for k = 1..7; g_1((0,0),(2,0)) is the constant 0, same column).
  Cubes = ALL 2^7 = 128 complete assignments of V, cube b (0 ≤ b < 128) setting variable of coordinate k to bit
  k−1 of b; the disjunction of all complete assignments of V is a tautology, so every model of F lies in exactly one
  cube. Cube file evidence/k5_split_v1/cubes_V7.icnf (hash recorded); no cube is dropped (unit-propagation-refuted
  cubes are solved like the others and have trivial proofs).
- Per cube: CNF = F + one unit clause per cube literal (header V, C + 7), bytes hashed and streamed (lane FIFO) into
  CaDiCaL 3.0.1 (`-t` native limit) writing binary DRAT into a FIFO → zstd -3 → retained proof file (size measured;
  watchdog stops the solver if the compressed proof exceeds the per-cube cap ⇒ UNKNOWN); then `zstd -dc PROOF |
  drat-trim CNF -i -t T` with the cube CNF streamed again through a FIFO, under /usr/bin/time -l (RSS measured; RSS must
  stay ≤ 6 GiB); strict verdict: solver exit 20 AND a line equal to "s VERIFIED" after stripping "\r" AND no
  "NOT VERIFIED". Anything else = UNKNOWN.
- PILOT: 6 cubes (b with supports {1}, {4}, {1,2}, {4,5}, {1,4}, {2,3,4}), each solver limit 900 s, per-cube proof cap
  300 MB compressed, ≤ 2 CPUs for the split (the K4 solve uses the third). Report solve time, proof size, drat-trim
  time and RSS per cube and the projected CPU-h for 128 cubes; go/no-go by the parent.

## 8.1 Amendment (frozen before any re-split run; host time printed below): refinement of UNKNOWN K5 cubes with
## STREAMED, non-retained DRAT certification (parent approval 14:4x)
- Leaves. Depth 1 = the 128 frozen cubes of §8 (V1 = g_1((0,k),(2,0)), DIMACS 57,106,155,204,253,302,351). A leaf of
  depth d that is not certified is refined ONLY by the full product with the pre-declared list V_{d+1}: its 128
  children are c ∧ a for all complete assignments a of V_{d+1} (child index b sets V_{d+1}[k] to bit k of b). Their
  disjunction is c, so by induction the terminal leaves always cover the whole base CNF. No leaf is ever dropped;
  certified = solver UNSAT + strict checker verdict; anything else = UNKNOWN (refined at the next depth or reported).
- Pre-declared lists (base CNF variables, coordinates k = 1..7):
  V2 = g_1((0,k),(3,0)) = 64,113,162,211,260,309,358;   V3 = g_1((0,k),(4,0)) = 71,120,169,218,267,316,365;
  V4 = g_1((0,k),(5,0)) = 78,127,176,225,274,323,372;  V5 = g_1((0,k),(6,0)) = 85,134,183,232,281,330,379;
  V6 = g_1((0,k),(7,0)) = 92,141,190,239,288,337,386;  V7 = g_2((0,k),(2,0)) = 1625,1674,1723,1772,1821,1870,1919;
  V8 = g_2((0,k),(3,0)) = 1632,1681,1730,1779,1828,1877,1926. (Ids read from evidence/gram_dev_v1/GA5L_K5_sb2.map.json.)
  Children that repeat a literal or contain complementary literals are still emitted as written (the latter are
  trivially UNSAT and are certified like any other leaf).
- Pipeline (code/k5_resplit.py): leaf CNF = base + one unit per literal (header nv, C + |lits|; bytes hashed), streamed
  by FIFO to CaDiCaL 3.0.1 (`-q -t 900`, default seed) writing binary DRAT to a FIFO; the engine hashes the proof
  stream (SHA-256 + bytes) while relaying it into drat-trim (pinned d834b649…; `CNF-FIFO -i -t 20000`, proof on
  stdin). Nothing is stored except logs and receipts. One pipeline at a time (≤ 2 busy CPU processes). Guards:
  aggregate RSS (engine + solver + checker, sampled every 2 s) > 6 GiB → SIGTERM to solver and checker, bounded wait,
  whole leaf UNKNOWN; before each leaf: filesystem free ≥ 12,000,000,000 bytes and lane ≤ 9.5 GiB, else stop with a
  receipt. Strict verdict: both processes exited by themselves (no guard trip), solver code 20 with
  "s UNSATISFIABLE", checker code 0 with a line equal to "s VERIFIED" after stripping "\r", no "s NOT VERIFIED",
  no relay error.
- Receipt per leaf (RESULTS.jsonl): id, ancestor id, depth, complete literal list, CNF SHA-256 + vars + clause count,
  solver argv/returncode/status lines (binary path, SHA-256, version and seed in META), proof-stream SHA-256 and
  bytes, checker argv/returncode/status lines (binary SHA in META), relay errors, guard trip, self-exit, aggregate
  peak RSS, seconds, verdict. Streamed checks are WORKER checks; the parent replays every non-retained leaf.
- Order: after the §8 batch ends, run depth 2 for the depth-1 UNKNOWN cubes (in increasing cube index), then depth 3
  for depth-2 UNKNOWN leaves, etc.; checkpoints ≤ 30 min; report before going beyond depth 4.
frozen §8.1 at 2026-10-17 14:44:41 PDT

## 8.2 Amendment (Codex audit 14:5x fixes 1–2; frozen before any strict root run or depth-2 run; host time below)
- Old §8 root records (k5_split_v1/pilot and k5_split_v1/all RESULTS.jsonl, written by k5_split.py / k5_split_r2.py)
  are WORKER evidence only. code/k5_root_reclassify.py evaluates every condition of the strict conjunction from the
  recorded fields (solver exit 20, "s UNSATISFIABLE", no cap stop, compression and decompression exit 0, complete CNF
  feeds, checker exit 0, "s VERIFIED" without "s NOT VERIFIED"); any absent field ⇒ UNKNOWN. Output
  k5_split_v1/ROOT_RECLASSIFY_v1.json; no old record is modified.
- Cover ledger: code/k5_cover.py (init / ingest / refine / validate; validator controls k5_split_v1/ledger/
  COVER_CONTROLS_v1.json, 26/26 pass). Versions k5_split_v1/ledger/LEDGER.vNNN.json are new files, each binding its
  predecessor's SHA-256; every leaf ever created is kept with id, depth, index, ancestor, complete literals, state
  (UNSTARTED / CERTIFIED / UNKNOWN / REFINED) and receipt (file + SHA-256 of the exact line). Validation recomputes
  each leaf-CNF SHA from the base CNF and checks base SHA, frozen chain V1..V8, unique ids, the 128 roots, exact
  128-child families with the declared lists, ancestry, and CERTIFIED ⇔ strict receipt. Complete ⇔ no problem and
  every terminal leaf CERTIFIED.
- Roots: ledger v001 = 128 roots UNSTARTED; worker records that are not UNSAT (900 s timeouts) are ingested as
  UNKNOWN (an UNKNOWN never certifies anything); worker-POSITIVE roots stay UNSTARTED and get their first strict
  decision by code/k5_leafrun.py (certify() of code/k5_resplit.py SHA 4aed8e43…7069, unchanged: -q -t 900, streamed
  non-retained, strict conjunction, 6 GiB aggregate RSS guard, disk floor 12e9, lane ≤ 9.5 GiB). For these roots the
  retained §8 proof is bound informationally (SHA of its decompressed bytes vs the streamed proof SHA; the old
  file SHA must equal the old receipt's). A root whose strict run fails is UNKNOWN and is refined like the others.
- Runner: validates the ledger before starting; resumes only on receipts matching full identity (id, depth, index,
  ancestor, literals, base SHA, leaf-CNF SHA); duplicates/mismatches abort. Ingest of strict receipts aborts on
  identity mismatch or two receipts for one leaf.
- Order: §8 batch ends (its records are worker evidence) → reclassify → ledger v001 init, v002 worker-root ingest,
  validate → strict depth-1 runs → ingest, validate → refine all UNKNOWN terminal leaves → validate → depth-2 strict
  runs → … ; validation before every refinement and run; report before depth > 4. Resource rules as in §8.1.
- K4: no claim beyond CNF necessity (soundness note r2 §1–§5) until a §9 base, declared split lists and ledger exist.
frozen §8.2 at 2026-10-17 15:07:51 PDT

## 9. Amendment (frozen before any K4 split run; host time below): certified split of the K4 weight-1 base
- Base F4 = evidence/k4_w1_v1/GA3_K4w1.cnf, SHA-256 7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7
  (513184 vars, 5833793 clauses), command and line→family map in review/K4K5_ENCODING_SOUNDNESS.r3.md §3.2;
  regenerated byte-equal in memory 15:13 (code/regen_hash_k4.py → evidence/k4_split_v1/REGEN_RECEIPT.json: 64 P4
  at-least-one clauses = squares 1–4 × 8 rows + 8 columns, 0 lexeq variables; K5-SB2 inactive). Soundness: r3 §0(b),
  §4–§6 (CNF necessity, all-frames P4 via F3).
- Split (same design as §8/§8.1, coverage by construction): roots = all 128 complete assignments of
  V1 = g_1((0,k),(2,0)), k = 1..7 (DIMACS 57,106,155,204,253,302,351); refinement only by the full products over
  V2..V8 of §8.1 (same DIMACS ids; evidence/k4_split_v1/CHAIN_CHECK.json confirms all eight lists name the intended
  variables in GA3_K4w1.map.json). g_1((0,2),(2,0)) is forced ⊥ (G2 with the unit g_5((0,2),(2,0)) = ⊤, L(2,0) = 2),
  so the 64 roots with bit 1 set are expected to be trivially UNSAT; they stay in the cover and are certified like
  any leaf.
- Pipeline and records: code/k4_leafrun.py = code/k5_leafrun.py unchanged with the K4 constants of code/k4_cover.py
  (ledger/validator logic of code/k5_cover.py unchanged; base SHA, directory evidence/k4_split_v1, schema
  k4-cover-ledger/1); certify() of code/k5_resplit.py (4aed8e43…7069): streamed, non-retained, strict conjunction,
  -q -t 900, aggregate RSS guard 6 GiB, free ≥ 12e9, lane ≤ 9.5 GiB, one pipeline; versioned ledger, validation before
  every run/refinement; exact-identity resume.
- PILOT (6 roots, ≤ 900 s each; strict, streamed): c016 {5}, c032 {6}, c048 {5,6} (the K5-hard pattern: Q1(2,0) inside
  the singleton coordinates) and the seeded sample random.Random(20261017).sample(61 bit-1-clear roots other than
  16, 32, 48, 3) = c037 {1,3,6}, c001 {1}, c061 {1,3,4,5,6}. Report per-root verdict, time and RSS and a projection;
  parent go/no-go before the remaining 122 roots. Scheduling relative to the K5 refinement: as decided by the parent.
frozen §9 at 2026-10-17 15:16:01 PDT

### Addendum 2026-10-17 15:5x PDT (parent clarification; no earlier text changed)
The parent's 15:4x wording "preserve all terminal leaf proofs" is clarified by the parent: the 14:4x approval stands —
new depth-2 and K4 leaves may be streamed NON-retained, with full CNF / literal / toolchain / strict-predicate /
proof-stream hashes and an exact recipe for independent parent re-solve + check; EXISTING retained proofs and all
terminal receipts / UNKNOWN frontier records are preserved; no cap increase, no cleanup or deletion. The 122 retained
root proofs are listed in evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1.{json,sha256}.

## 9.1 Amendment (frozen; NOT IN FORCE until the parent's both-CLI review and GO(b)): K4 orbit reduction
- Verified CNF automorphisms of F4 (evidence/k4_split_v1/AUTOMORPHISM_S3_567_r2.json, d688277f…357c; checker
  code/k4_automorphism_r2.py ae9bcbb4…708f; exact sorted-int32 clause equality, group S3 of order 6, controls as
  intended). Math note and ledger contract: review/K4_ORBIT_REDUCTION.r1.md (SHA-256 89e8c52e351c02671663caab7d2989008ddbf4c1c26a0e065b9bfa06cd7d7286).
- Until GO(b): no K4 leaf is orbit-certified, no K4 production run; the K4 ledger stays at v001 + pilot receipts.
frozen §9.1 at 2026-10-17 17:04:48 PDT

### 9.1 addendum r2 (frozen; still NOT IN FORCE until the parent's GO(b))
Superseding r1 for certification use: review/K4_ORBIT_REDUCTION.r2.md (SHA-256 c99d31440c4a88d8761d55d18b2bf0efef52b74792a1930c6289adebd3f79cc7) — pinned permutation arrays
(evidence/k4_split_v1/auto_r3/PERM_g1.i32le 8b09da43…5b2a, PERM_g2.i32le e0a2bc4c…cfd3), two independent exact checks
(code/k4_automorphism_r3.py → auto_r3/RECEIPT.json c7154dc3…3ff8; code/k4_auto_secondpath.py →
auto_r3/SECONDPATH_RECEIPT.json 2990e216…1275), path-literal ledger contract implemented by code/k4_orbit_r2.py
(SHA-256 09d7af13c10d36b400e709650e19e77b923fc31035e6fdd73499af942dfda289; in-memory controls 14/14 PASS). No K4 leaf is orbit-certified and no K4 production run happens before GO(b).
frozen 9.1-r2 at 2026-10-17 17:28:18 PDT

### 9.1 addendum r3 (frozen; still NOT IN FORCE until the parent's GO(b))
Validator implementation superseded by code/k4_orbit_r3.py (single-buffer binding: each pinned artifact read once,
hashed and deserialised from that same buffer; contract unchanged from review/K4_ORBIT_REDUCTION.r2.md §3); control
suite code/k4_orbit_controls_r3.py → evidence/k4_split_v1/auto_r3/ORBIT_VALIDATOR_CONTROLS_r3.json (25/25 PASS, incl.
replace-between-reads regressions R1–R4 and the missing r2 regressions N1–N6). Replay dependency closure (sources,
fixtures, arrays, receipts, external name table): evidence/k4_split_v1/auto_r3/DEPENDENCY_CLOSURE_r3.sha256
(`shasum -a 256 -c` from the lane root: 16/16 OK). Interpreter: depolarizing/env Python 3.13.9 (NumPy 2.5.4 for path A only).
frozen 9.1-r3 at 2026-10-17 17:44:57 PDT

### Results-log entry: amendment RETRY-ONCE frozen (parent approval 18:3x PDT)
review/AMENDMENT_RETRY_ONCE.md SHA-256 507be52839cb153a26414cdf3ecc6d8d3def252a3fa78e9eca4b0389fd9ac371; code/k5_resplit_r2.py SHA-256 90b6f5928058db04315534640dba556486a969441009f0e680f5de0873558484; code/leaf_retry.py SHA-256 5a82b49b62ecce6d3c1a2dc68ec4619c7faa113ed42bc7bd2ddb5efe2378ffa7.
frozen RETRY-ONCE at 2026-10-17 18:32:30 PDT

### Proposed K5 residual normal form (frozen for review, not yet authorised for computation)
2026-10-17 19:59 PDT: `review/K5_RESIDUAL_NORMAL_FORM.r1.md`, SHA-256
`c2c77c471218760a2beeb0ca105e04958689730447f48437b9cc8c815f333d3a`, proves a candidate vector-level reduction:
the 122 accepted root exclusions plus only c064/c096 exclusions would suffice for K5. It restores ROWLEX after a
residual coordinate/square permutation; it does not claim a syntactic CNF automorphism or alter the original cover.
Finite support-order controls: `evidence/k5_split_v1/NORMAL_FORM_BIT_CONTROLS_v1.json`, SHA-256
`a85a0609ace1ef55af8834b351ac73c61bec790d7c02122c65bd50dc56599edd` (32736 families,192384 family/permutation checks,
224 A-meeting support checks; two intentionally wrong leftmost choices rejected). No root is dropped before approval.

### Stronger K5 normal-form candidate r2 (frozen for review; original cover unchanged)
2026-10-17 21:30 PDT: `review/K5_RESIDUAL_NORMAL_FORM.r2.md`, SHA-256
`1a3a47cf939e55fc125b4b70e1e171af6ca28f895a6cdfe4e61b47e8ebb8ca7f`, adds an ONB projection lemma proving a
pure-B vector exists without any root-certificate import. Thus c064/c096/c112 cover genuine normalised K5 vectors;
only c112's already accepted root proof is needed to reduce the unresolved cases to c064/c096. No arbitrary CNF
model transfer is claimed. New finite controls cover only the30 additional min-weight3 support families (180
permutation checks,112 mixed-A checks), reusing rather than repeating the pinned r1 controls:
`NORMAL_FORM_K3_CONTROLS_v2.json`, SHA-256 `dfe2fceaf4d7c715f10d1cc62e731beddc7d9a1a05d597edea8bfa6a49dd7726`.

## 10. Approved exploratory H3 pilot (frozen 2026-10-17 22:42 PDT, before generator/run)
Parent approval22:38: `HALL3_PATTERN_NECESSITY.r1.md` (068d30e5…b17f) may be piloted on the unchanged K5 hard
leaf after controls. Generator/runner `code/h3_pilot.py`, SHA-256
`7aa7bfb2577506859ac88f52702b2f36a16f3cf7261aa674ecfefb6750efd383`.
It generates235200 raw row0-H3 clause candidates (constant-folded emitted count recorded), no auxiliary variables;
streams every CNF because the base137664569B already exceeds100MB retention cap; no duplicate CNF/proof is stored.
Before the ONE proof-free CaDiCaL600s pilot: H3-only J3x2⊕J2x3⊕I3 fixed pattern must be UNSAT; the binding's
AG(2,8) positive configuration must be SAT under base+H3 minus exactly5P4-ALO clauses and7Q1-SB2 units plus
all7840fixed Gram units (same strong relaxation); its returned model is checked against every retained clause.
Control inputs come from parent `K5.bind.json`, SHA-256 `0a1be0504563b9d41f8a10f8cc3493b63a8489d03b61c327e744fccf23494ce7`.
Per-launch free floor12e9 and per-process-pipeline6GiB guard, ≤2busy processes, native limits; no further1800s
retries after this pilot pending parent decision. H3 certificate cutover still needs both static reviews and replay.

## 11. Approved full-column template certificates (frozen 2026-10-17 23:23 PDT before solver use)
Proof candidate `review/K5_COLUMN0_TEMPLATE_COVER.r1.md` SHA-256
`1ae1c81d5c2982ecf23b7a3f881e79786576bbed21efc456ba5b427b53907d9a`:16 genuine-vector templates,3covered by the
accepted c112 root and13remaining; no Boolean-cover claim. Parent23:0x approved all13 restricted strict runs,
after finite controls and the current c064 boundary. No H3/new encoder/variables: oldF+42units per case.

Finite support enumeration (nauty genbg2.9.3, binary63822426…15f83, recorded exactargs):26593 connected
colour-isomorphism classes through part sizes8, independently filtered for both pair-overlap rules and3-in2D
rank; exactly the five claimed component types, no outside component. Labelled full-square counts for n0..8:
1,1,3,25,298,4770,111770,3367910,122467800. Result
`evidence/k5_template_component_control_v2/RESULT.json` SHA3aa58aa8…72ba; v1's first-graph parser NameError
is preserved as an incomplete attempt (corrected lexical spacing; no completed enumeration was repeated).
Additional direct3x3/4x4 controls find25/298 patterns; all43290 labelled chosen-column patterns canonicalise under
S3(A)xS4(B) to exactly the16 table orbits. Manifest `evidence/k5_column_templates_v1/MANIFEST.json`,
SHA `f77c061947aa64d1107736d27723373ccc9e02633dd099c1a58cf9d77a2c0b71`, pins all16cases/13run unit lists and CNF hashes.

Runner `code/run_k5_column_templates.py` SHA `99e19533ed997901b65090578fac5a2c08cea0e4f3b3ca7f0de8af2081be5081`
uses the same strict streamed pipeline (`k5_resplit_r2.py`90b6f592…8484); solver900s, checker<=3600s,
aggregate6GiB, no retry, bounded10400s chunk with explicit resume. Every case checks the NEW12.2e9 launch floor;
projected retained growth<10MB, no CNF/proof snapshots. Separate `k5_column_template_runs_v1` ledger versions
store restricted STRICT_UNSAT/UNKNOWN/UNSTARTED states and full unit identity. They never modify the original
cover ledger or assert K5 excluded; genuine-vector coverage remains conditional on both reviews and parent disposition.

## 12. Approved unified one-P4 route (bridge frozen 2026-10-17 23:34 PDT before any weakened CNF generation)
Parent approved preparation and, AFTER the13 old-F templates, all16 weakened-F template runs. Bridge
`review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md`, SHA `c391a67ab7cb468c2500dd4fc0d565fa4e104b97777a5bab668ed5fdc82ebbb3`.
Exact deletion manifest `evidence/UNIFIED_ONE_P4_DELETIONS_v1.json`,
SHA `4509b3e7f26f75d63e35f1c3f8d57fcf33ad019c3ab4e19ada0f8372d991e3a6`, deletes only zero-based clause indices
5735297,5736866,5738435,5740004 (P4-ALO squares2–5); keeps Q1 index5733728 and all other bytes in order.
All five56-flag source lines were checked against the full name table; exact line hashes/index conventions
are frozen. F_one has509915variables,5740226baseclauses; with each template42units,5740268clauses.

A8 authority is parent `moqls8-k1k2-parent-verdict.md` SHA919daeac…a8f9, Proofoutline1/line13, read-and-bound
proof lineage/line9 and CORRECTNESS-ACCEPTED/line36. Its contrapositive plus W8 puts some weight3 entry in Q1;
the explicit common row/column+coordinate moves and ROWLEX restore the allowed normal form. Other four
squares may be classical; their retained w3 implications admit all-false flags. The component/template theorem
uses only Q1weight3 and the aligned five-square degree bound, not their P4 or reduced-K5 status.

All16 cases MUST run (including three c112 ones: the stronger old certificate is not transferable).
Same strict streamed pipeline900s/case, no retry, separate formula/ledger, fresh12.2e9+growth gate.
No claim about Problem16n8 before both bridge/template reviews, complete certificates and parent replay/disposition.
No next cover root after the authorised current c064/13/16 sequence without a new decision.

### One-P4 preparation producer pin (2026-10-17 23:41 PDT, before generation)
`code/n8_one_p4_formula.py` SHA `61eda23ce7174e7cee77ee873ff06e5f22a2beaf0c197b8282f41dc8ddded400`
checks the frozen source/deletion/bridge hashes, verifies all five source ALO lines, removes only the four
authorised ranges and updates the header. It prepares16 in-memory formulas/JSON recipes, never stores CNF bytes.
Fresh preparation floor13.534GB>=12.2GB; projected retained manifest/recipe growth<=100KB. Actual solving waits
for completion of all13 strong-F case attempts.

### Static-review repair link (2026-10-17 23:39 PDT)
`review/K5_SEMANTIC_REVIEW_REPAIRS.r1.md` SHA `413951379f248a87e02b52dfb942fb131f25524557c35adf9c54f68981b31022`
addresses NF1–4,TPL1–4,IMP1–4 and inactiveH3_1–3 without rewriting originals or changing a clause/unit/case.
`evidence/K5_SEMANTIC_REPAIR_LINK_v1.json` binds the unchanged instance manifest to those repairs/imports.
Parent semantic disposition and independent certificate replay are still required.

### Prepared unified formula/consumer (no execution yet)
F_one was regenerated only in memory after the bridge freeze: base SHA
`374d6fb46ab2a1f7a77bdf6699aa67792c126b2e2dcdf65ad37074be9fc5eeb9`,5740226clauses.
`evidence/n8_one_p4_templates_v1/MANIFEST.json` SHA
`355b33801640e39ab86946c51ab58c9c843370083ca896dd6d8ee5b09e90fc74` pins all16 leaves (5740268clauses each).
`BASE_RECIPE.json` SHA `264288f8aa3d9b10f4bae5d051d5b711e76e95dcaefd13dadc84f821adfa0c18` binds the exact
four removals/Q1 keep. No weakened CNF file exists.
`code/run_n8_one_p4_templates.py` SHA `268e743b76c9a8d8699f28ef3cab6b1100b720ef0e76a5b5b97123237563fba8`
requires all13 strong-F case attempts first; it uses a separate16case ledger and the same strict pipeline,
900s/no retry, fresh12.2e9 gate. The current shared-disk deferral prevents any new solver execution.

### Unified review repair and observed generation evidence (2026-10-18 00:07 PDT)
`review/N8_UNIFIED_REVIEW_REPAIRS.r1.md` SHA `e0f3c860aaa81dd7b8214aabb84f5094fcaf425a6a17a01159d3aa779a9d1704`
closes all7bridge/3manifest minors without changing frozen originals. It states property-form T16 for any aligned
five-set with Q1weight3, explicit support-set Sym(A)xSym(B)/square action, exact flag assignments, observed generation
versus earlier obligations, source imports and all remaining acceptance gates. No reduced-K5/13case/c112 import for F_one.
`verify_one_p4_deletion.py` SHA825c3cd7…3016 actually ran a second-path line comparison at00:04:
all5740230 source LF-only/non-comment clauses,4deleted hashes,Q1keep, every5740226retained clause byte/in-order,
all5ALO name domains and16unit/leaf hashes checked. Receipt `BYTE_FILTER_VERIFICATION_v1.json`
SHA `65aafe0ad577645036c6cc15e4f4705f0bb19a4f5e8eed2867954da8d761cc88`, all_pass=true.
`evidence/N8_UNIFIED_SEMANTIC_REPAIR_LINK_v1.json` links that evidence, overlay and unchanged16instance manifest.
These are identity/math-review repairs only, not a refutation or parent target disposition.

### Parent conditional mathematical/input disposition (2026-10-18 01:40 PDT)
Parent `moqls8-unified-parent-disposition-v1.md` SHA
`29d17f380416045f73cd4e4b6923e55316bed8a62a45dd6310235cb239f8eaeb` conditionally accepts property-formT16,
the canonical extension and one-P4 reduction, NOT an n8 theorem. Independent parent streaming binding
`moqls8-one-p4-parent-binding-v1/RESULT.json` SHA
`65311ab0b3109412383b47113b36c6a4b3d74f8132fc334cb2f5194b480928b0` closes actual source/deletion/table/672unit/16hash
bindings without producer imports. Its scope narrows the worker byte verifier: retained-line comparisons were
independent, but its hash routines reused the producer; the new parent implementation supplies independent hashes.

`N8_PARENT_CONDITIONAL_DISPOSITION_LINK_v1.json` preserves F3/F5 scope and the F4 provenance limit. The inherited
worker records planned CNFhash, relay proofhash/bytes and feed errors, not separately MEASURED delivered hashes
for both solver/checker CNF feeds. No measured values are fabricated. Current outcomes are
**producer candidates / LEGACY-worker-strict**, not full-F4. Raw stored logs and precomputed input pins are retained.
Every counted final refutation requires the parent's measured-feed re-solve/replay receipt, exactCR-only log
predicate, controls and final full-composition disposition. Inputs/queue remain unchanged; all16cases required.

## 13. Static F_one refinement design (2026-10-18 02:18 PDT, NOT LAUNCHED)
Parent-requested `review/N8-FONE-REFINE.r1.md` SHA
`768225351af1d5f595ab36546d0203e1d6df0fa313278e0264263d51d72982f1` and JSON
`fa0a68ac0c0b026eac981adfe62dca4130a63efd0976b79f6bf0d941a4da7003` preregister a3-bit Q2 A-support split:
g_2((0,c),(2,0)),c1..3,IDs1625/1674/1723 (first3V7). Static GMAP lookup verifies all16 templates'42unit lists
are disjoint from the selected IDs; no child formula generated/solved. Eight full sign-pattern children,45units,
5740271clauses; no pruning/newencoder/H3. Proposed future300s/900s native limits and stop atL1 UNKNOWN, no retry.
Full measured-feed NEW wrapper+controls,parent review and a NEW launch go are prerequisites. Resource forecasts
explicitly include10MB/child80MB/family,12.2e9+growth/9.5GiB gates,6GiB pipeline and3h chunks; no wide-batch promise.
The CURRENT sixteen-case queue remains900s/case with unchanged inputs and its legacy-producer status qualification.

## 14. Completed F_one producer pass and frozen two-level design (2026-10-18)
The unchanged16-case pass is complete:12 **producer candidates / LEGACY-worker-strict**, UNKNOWN
`P1-B1,P1-B2,P1-B3,P1-B5`; no unstarted/SAT. Source RESULTS SHA
`bcfeb441f49971e4c8241fbccdfec99a41c274e8b8af4261d17796ac4327ac19`; finalv017 SHA
`40d8e7e77dcef85d7ab49281dd4befb9435bbec251b2844d2f64b8a978432fac`.
Parent separately accepted first10 direct leaves (P0-B1..B6,P1-B4/B6,P2-C1/C2) in
`moqls8-fone-first10-parent-verdict-v1.md` SHA
`61130625a144ae8e88e1f3c8cddd22798477808b0673ac5d246d9b8215b983e4`.
P2-C3/C4 parent replay is pending; four P1 cases remain open. Never relabel the legacy12 as parent counts.

Frozen `review/N8-FONE-REFINE.r2.md` SHA
`1d912616e037aa877f1e76d1ac36c2cab5aa0c439b57ade8a6da869b99c72d5a`, JSON
`bf9f71937d7fcc98fceb26b3aaf05505d8df68bdc5005fe90b61c9fb74422d1a`, supersedes the historical r1:
L1 IDs1625/1674/1723 and L2 IDs1632/1681/1730, fixed for all16 templates; all8 sign patterns each level.
L1 UNKNOWN creates all8 L2 children; noL3/retry. Original42units stay first; L1/L2 have45/48units and
5740271/5740274clauses, no new variables/encoder/H3. One family shares10400active-s and80MB retention,
not reset per subdivision/resume. Only parent separately measured solver/checker feeds and strict proof replay
can count refutations; a new worker measured-feed wrapper is NOT required by the parent r2 approval.

`review/N8-FONE-REFINE-DELTA.r2a.json` SHA
`eb9edb517d1a7ba9db6730cf38fc9f5f58bbe7229f9807f204350c81a4729823` links exact virtual wire diffs,
source pins, static controls185c9fd0…3600a, actual-source16 binding and targeted admission controls.
The static suite checks16root hashes,1152potential byte images and16384exact Boolean partition cases;
its five wire mutations, three model corruptions and two capacity negatives are separate control sets.
It is producer-side data verification, NOT a parent measured-feed refutation or lifecycle validation.

## 15. Operational lifecycle HOLD (host checkpoint 2026-10-18 03:36 PDT)
Parent data-plane source review passed, but controller5ef65aa8…acf76 must NOT launch native work:
raw-PID signal/reap races, exception-path ownership and unguarded preparation/directory reuse require correction.
No refinement native child has launched. The intended correction is a pinned, validated external owned-group
supervisor, read-only from the phys-2 lane only after Main approves reuse; failed supervisorr2 is not used.
All old records and source/data controls are retained unchanged and do not certify stop/exception safety.

Parent admission7ff6aa67…e206 reserves ONE P1-B1 family, not all future families, and is revoked by the
specified immutable release marker. Every later family needs a new capacity reservation even if its scientific
schedule was approved. Source review alone does not admit a native pipeline. Whole-invocation ownership,
shared8GiB/4native capacity, own6GiB, fresh12.2e9+growth,9.5GiB lane data and deadline gates all remain binding.
There is still NO Problem16 n8 theorem, full16 proof closure, K4/K5 cover claim or novelty/priority claim.

## 16. Corrected lifecycle and admitted P1-B1 pilot (host prelaunch 2026-10-18 04:22 PDT)
This supersedes the operational HOLD of §15 only for the approved, pinned integration and ONE leased family.
`review/N8-FONE-LIFECYCLE-INTEGRATION.r3.json` SHA
`08ab430bb51f6ecae49c3899a20a4021575a73e200a95348f6322cf89d8b3bab` and control plan
`f609625e4d6b3c7bf6bd80283274f7977edcddf53a38640a6e1c4a8baf7b8513` were source-reviewed PASS by Main.
The outer adapter uses the read-only absolute phys2 supervisor0ee8f394…83ec4d public API; it holds the
capacity flock through owned-group cleanup/quarantine and post-qualification. Its worker contains no raw-PID
or self-SIGTERM code. Every preparation/native path is inside that supervised group. New directories are
exclusive --init-root/--init-family; later --reuse-family requires recorded identities and FIFO types.
Unexpected shared/release stops use a tiny immutable request file, never rediscovered PID signals.

`evidence/n8_refine_r3_static_controls_v1/RESULT.json` SHA
`cad9069e95e40989739f791b92c796c4c7c33d63ec221856ba317e73bc5d35cf` PASS covers the frozen STATIC
AST/metadata/directory/stop-channel/qualification/cap plan. It launched no process-group/native command and
does not replace the separately observed phys2 lifecycle controls3c77be50…99de.

Main additionally requires an x-created receipt immediately before EVERY invocation, re-hashing every packet
source and the supervisor. Static preflight425d2631…7620 and first-pilot preflight21486fcc…e144 each matched
all11 hashes and the unreleased7ff6 lease. No new invocations after17:30PDT. The first P1-B1 call began with
--init-root --init-family; later calls use --reuse-family, one child per call. No result is implied by launch.
Only outer completed_cleanly can qualify a producer candidate; closure requires every terminal outer flag.
All measured-feed/refutation counts remain PARENT-only, all16 original target obligations remain, and no
other family has a resource lease. The P1 monomial-column note is a separate unreviewed proposal, not a CNF
or ledger amendment.

## 17. Correct fail-closed stop; staged non-setuid RSS fix (2026-10-18 04:54 PDT)
The first P1-B1.L1.000 invocation is **UNKNOWN**, not a refutation. Pinned supervisor0ee8f394…83ec4d
reported an EPERM basic-info probe after9.679s; saved cleanup reports successful owned-group SIGTERM,
no survivors and no killpg error. Outer receipt2b1e92e6…1ec5, ledger295da85e…53a0 and quarantine
`evidence/N8_FONE_REFINE_R3_QUARANTINE.json` SHA
`c5f76542ff09bbac3a4ea75a4ed2eb22787feb07a60388e8b87354d2f34c1081` are preserved.
Parent disposition `moqls8-refine-r3-quarantine-disposition-v1.md` SHA
`2cdf49b1d03374323c89bac62fba6c7c09aa6856c47db120d7e124aac0217681` forbids rerun under those sources.

The verified static cause is the setuid-root /bin/ps helper used in two worker paths. It is NOT safe to ignore
EPERM or call it a zombie. New `code/k5_resplit_r3.py` SHA
`00435386034f9b1e60bbdf21d113ded9947cf2455c7b5f679e1734ed86bae3e9` changes only the RSS implementation:
its certify() source bytes remain25ef2728…cfba, identical to90b6. `darwin_process_metrics.py` reads the
pinned supervisor's real libproc data; shared selection uses audited non-setuid/non-setgid /usr/bin/pgrep,
not ps/top/lsof, and unknown probes still raise. Every resolved remaining executable was privilege-audited.

`review/N8-NOSETUID-INTEGRATION.r4.json` SHA
`cb1fd7174fdb293a1de9b336b56b65cd194038d8f90de789bc919a49b83d35ff` and control plan
`d6a33e6685c11280d6dc4c5264fb42bd645904e583563ce87ef74870f67d3a17` are staged for source review.
No r4 static control, non-native smoke or native leaf has run. Required order: parent source PASS,
static PASS, ONE supervised NON-native RSS-path smoke with zero observed unknown probes, then a separate
parent message naming the exact quarantine file/SHA for MOVE with a manifest, and a new native GO.
Code never clears quarantine. A proposed new source epoch preserves the old ledger read-only, carries its
9.704317s and REFINE state/all8L2, and continues atL1.001; it does not retry the uncertain000 leaf.
All original n8 mathematical and parent measured-feed obligations remain open.

## 18. Validated RSS fix, named retirement and v4 continuation (2026-10-18 05:12 PDT)
Parent source PASS of cb1fd717…35ff was followed by static PASS
`e2e1e2a2169504e8717a5942d00d9336bb927904f54c6c95a789f7b9c0ab3676` and ONE supervised NON-native smoke
`90df761c8508c32642805dafa40651dff6cc5273aa602f014d5698278ce033d8`. The latter exercised six NEW-R
RSS/shared snapshots on self plus a sleeping Python child: cleanrc0, zero observed unknown probes, no smoke
quarantine; no Cadi/DT/certify. Productionc5f765 quarantine was preserved during validation.

Parent then named its exact retirement by MOVE. It now resides at
`archive/n8-r3-quarantine-20261018/N8_FONE_REFINE_R3_QUARANTINE.json`, same1177bytes/SHAc5f76542…1081.
`archive/MANIFEST.md` SHA99980add…54c2 and `evidence/N8_R3_QUARANTINE_MOVE_RECEIPT.v1.json`
SHAdfa11728…5efc record the no-survivor evidence, smoke, collisions, reason and idle-only rollback. No deletion.
They explicitly record the creation-only deviation: `code/run_n8_fone_refine.py` changed at the SAME path
8598808d…f9d4→7d28ecbe…f0b3b; it was NOT a new filename. Exact r3 source bytes are x-preserved in that archive.
All active code is now frozen; any further fix needs a separately versioned path and new review.

The parent authorised ONLY P1-B1 continuation in `refine_v4` under lease7ff6, explicitly importing the old
295da85e…53a0 ledger READ-ONLY, carrying9.704317334108055active seconds/previous retention and preserving
L1.000REFINED/all8L2. It startsL1.001, never retries000. Fresh preflight7a5d7bde…adef1 matched all12source/
plan/audit/supervisor and5executable/mode pins before the first v4 call. One child per call; no other family/L3.
Every later call needs a new full gate; no new invocations after17:30PDT; quarantine/SAT/uncertainty stops.

Disk attribution and recurrence are UNESTABLISHED: observed free-space/snapshot changes do not prove a
TimeMachine/Syncthing cause or a reliable≈12e9 thinning trigger. No host configuration/deletion was performed.
All fresh/in-flight floor rules remain binding. The monomial-column proposals remain separate/unreviewed,
with no strengthened CNF or accepted ledger cutover. There is still no n8 theorem or full16 proof closure.

## 19. Parent-only strengthened route and frozen assembly (2026-10-18)
The producer pilot is STOPPED/QUARANTINED. L1.001 was a cleanly observed timeout/UNKNOWN; L1.002 triggered
a distinct ZERO-resident probe and correctly stopped. New quarantine5ac17d24…9e75 persists; no zero-as-death
reinterpretation or retry. The immutable parent release721c0eda…9050 ENDED lease7ff6. Producer native processes
are absent and no producer solve is planned on the six stronger inputs.

All12 direct leaves are now separately parent-accepted exact UNSAT (P0-B1..B6,P1-B4/B6,P2-C1..C4), by the
first-ten verdict and `moqls8-fone-direct12-parent-verdict-v1.md`. Four P1 source formulas still require closure.
The Boolean model-existence normal form has Codex ACCEPT-WITH-FIXES(0fatal/major,1minor); x-created
`P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md` SHA8ae0ac01…9e8f supplies the explicit K33 degree-premise repair.
Parent finitee075aff8…cbc2 passed local/ID/stabilizer/clause checks; Claude and parent coverage acceptance
remain pending. Six planned formula hashes are in `P1_MONOMIAL_FORMULA_HASHES.r2.json` SHAe04557a4…b709;
generator08b67cef…c352 wrote no CNF and invoked no solver. Parent N8StrengthenedReplay alone owns their
independent binding and measured-feed native certification. Planned hashes are never measured-feed receipts.

`review/N8_ASSEMBLY.r1.md` SHA
`8c9cf1c2cc079e2bfdbab8bd6e0a2c9a79268a534fb4043f9ad1028820fea986` and link registry
`2b727fde73816970724ff560c8384ed1ce3293caec36c3ce5e5d449686e21798` freeze the exact statements/files/SHAs
and accepted/PENDING status of the whole chain: unified reduction with conditions, genuine16-leaf cover,
direct12, four-to-six Boolean normal form, exact six inputs, and conditional n8 conclusion. They claim NO
unconditional n8 theorem, whole-base F_one UNSAT, result for alln or novelty. Parent must close all remaining
reviews/binding/refutations and issue a final full-composition disposition.

The separate no-fork metrics proposal is `N8-NOFORK-INTEGRATION.r5.json` a6d6cdb9…dd75 with narrow diff
71e4d780…ec98 and validation plan51809df6…f73a. It uses NEW versioned paths, in-process libproc UID enumeration/
KERN_PROCARGS2 and allocated-block walking, unchanged strict0ee supervisor and no grace/retry/zero-ignore.
It is source-only/unrun, not permission to revive a producer solve or retire the current quarantine.

## 20. Protocol qualification correction and independent GB gate
MANDATORY addendum `review/N8_ASSEMBLY_QUALIFICATION_CORRECTION.r1.md` SHA
`8bfd2dee4b7471d5187732d318c4c392467512fc42b2e24f085c7261baf28d4f` supersedes any reading of §19 or
assemblyr1 that the existing GA native receipts are fully protocol-complete. Parent correctiona4b51119…7b70
states proof-stream SHA256 was not recorded and discarded streams cannot be backfilled. Direct12/P1-B1.M2
native verification observations stand, but their final-gate evidence is PROOF_DIGEST_MISSING/QUALIFICATION_INCOMPLETE.
Fresh conforming evidence or a separately explicit authorised exception is needed; none is granted here.

The frozen contract also requires two independently written encodings for every exhaustive step. A new
source-only GB counterpart is `review/GB_ONE_P4_SOURCE_PACKAGE.r1.json` eccf887a…58a6:
`code/gb_one_p4_r1.py`952c761c…d88c, necessity/differencesnotee4dd33f4…03ed, preregfreeze1c350ced…20ce.
It calls untouched GB4b593e55…eae0 with order8/Q12345/ngen0/P4onlyQ1/SB2/G5 and NO ROWLEX; appends the same
semantic42units and126M_sclauses through GB OWNnames. Planned outputs are16+6formula hashes and an own-name
mapping, no CNF/solver. The relaxed classical control explicitly drops1P4ALO+7Q1SB2units for evaluation only;
no unrelaxed heavy-classical SAT is claimed. Exact heavythreshold component controls are also required.

Full GB generation remains NOT RUN pending natural-boundary RSS coordination with N8StrengthenedReplay
and Main permission. Its RAM sink is hard-capped1GiB/oneCPU; Python counts in the same8GiB lane aggregate.
Source preparation, hashes, component checks or future status-only results do not by themselves close the
independent-encoding/proof-certification gate. There is still no unconditional n8 theorem or novelty claim.

### 20.1 Static r2 freeze and admission order (07:18 PDT)
NEW `review/GB_ONE_P4_SOURCE_PACKAGE.r2.json` SHA
`b90b42cc6517af4d0d14aab6c19dc32a1ed67bbe56e90a7aca615d68df25bdf7` pins generator
`code/gb_one_p4_r2.py` SHA5ca7c0da…e262, necessityr2b9b4a595…2365, freeze3a2a521b…2d67 and
diff90f0222b…fc8c. Original r1 is preserved. The r2 changes tighten source-exact component controls
(prefix widths0–8, signed/constants/aliases, G3/G4/P4 rules, wrong thresholds) and add fixed inverse samples;
formula flags and emission/header/unit/M_s byte conventions are unchanged.
`review/GB_ONE_P4_CONVENTIONS.r1.md` SHA50a5bf4a…7b37 spells out those conventions and labels its inverse
examples as source-derived predictions, not yet measurements of a generated table.

The required sequence is parent N8GBParentBinding FIRST, adapter SECOND, independent hash comparison THIRD.
No concurrent generation, no parent-GB-hash read/adaptation, and any mismatch must remain a reported mismatch.
Neither r2 controls nor full GB generation has run. A parent desk's idle acknowledgment or recovered free
space alone does not grant this adapter admission.

Parent's07:16 disk report attributes the observed bulk growth to a separate Claude Code session outside
this run (`review/disk-decline-cause-observation-v1.md` in the PARENT review directory). This is parent-reported
attribution, not a new lane experiment; the earlier TimeMachine/Syncthing attribution remains unsupported.
This lane neither touches that session nor deletes/thins/reconfigures anything. The native launch gate remains
fresh12.2e9B plus projected growth, with in-flight12e9B floor. Native jobs≥60min additionally require≥13.5e9B
and no>300MB drop over5min. Per the07:17 clarification, static source/proof/receipt writes≤16MiB per action may
proceed below the launch gate; this never bypasses frozen code gates or authorises an encoder/native run.

Parent subsequently reported disk recovery and allowed each desk to resume only under its existing gates;
this does not change the adapter's sequencing HOLD. New science ends17:30PDT and all native work17:57PDT.
No lane watcher is active. For any newly authorised metadata watcher, the parent monitor is now
`institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0722-to-1810.jsonl` (10s cadence).
The earlier `disk-monitor-v1-20261018T0700.jsonl` ends10:58:43; a frozen consumer must refuse stale data,
not infer free space, relabel an UNKNOWN or create a retry storm. No frozen code is amended by this notice.


### 20.2 GB input identity, assembly r2 and GB timing probe (07:46–08:00 PDT)
After the parent GB binder finished, the parent admitted the lane adapter. Frozen `code/gb_one_p4_r2.py`
5ca7c0da…e262 ran unchanged at 07:46:20: rc0, 15.16s, peak RSS393379840B, no CNF, no solver.
Its manifest is `evidence/GB_ONE_P4_MANIFEST.r2.json` 4daf8fcf…680d. Own hashes
`evidence/GB_ONE_P4_OWN_HASHES.r2.json` 9781c877…943f were x-created BEFORE the parent GBBINDING was read.
Comparison `evidence/GB_ONE_P4_PARENT_COMPARISON.r2.json` df3fb6e6…b651 found ALL22 MATCH in SHA, bytes and
headers against parent GBBINDING d917203d…c673. This is input identity only.

`review/N8_ASSEMBLY.r2.md` SHA `ba97fce38ff3f97a72f374f8ab084775a47cc6def7223e5f6177c52fced0a41c` and registry
`review/N8_ASSEMBLY_LINKS.r2.json` eb7786b9…e060 apply Claude m1–m11 and Codex M1. They add the two parent
obligations: proof-digest provenance for all18 replays, and the GB second encoding. r1 is untouched. Assembly
r2 claims no theorem.

GB worker timing probe (parent request, not qualified). Probe r1 (b4c6ca46…b483) ran GB P1-B4 with kissat4.0.4,
relayed its proof stream (SHA and byte count recorded) and checked it with parent drat-trim a46c0c71:
- kissat rc20, s UNSATISFIABLE in24.9s;
- proof307290350B, sha cebf2feb…06b5;
- drat-trim rc0, s VERIFIED in186.0s;
- peak aggregate RSS3.68GB.

r1's frozen any-WARNING criterion marked P1-B4 FAIL because of375334 benign duplicate-literal normalisation
lines, so r1 stopped before P0-B3. Versioned r2 (1cb44062…806e) hashes the raw checker stream and counts those
lines; it launched at07:59:50 with a hard stop at08:56.

Probe r2 (worker evidence, not parent-qualified; summary b84717ff…1734) passed both GB leaves:
- **P1-B4:** PASS in184.7s, peak aggregate RSS3.69GB.
- **P0-B3:** PASS in683.3s, peak aggregate RSS5.38GB. Kissat took296.8s; the proof was765641068B
  (d4fed564…f65d) with24.2M lemmas; drat-trim reported s VERIFIED after682.8s.

Compared with GA, these pipelines are37× (P1-B4) and4.7× (P0-B3) slower. Kissat congruence/substitution
lemmas dominate the proof size. A rough two-point estimate puts the12 GB direct leaves at about1.45h run
sequentially; the six GB strengthened inputs would likely take many hours. Whether GB can close by17:57 is
the parent's decision. None of this is qualifying evidence. It closes no gate and supports no n8 claim.

### 20.3 GB direct leaves — worker production (parent decision b9886e24…09ec)
The parent authorised the twelve GB direct leaves only: sequential, shortest-first, at most 6GiB per pipeline, and
counting the GA desk's reservation against an 11GiB lane. Protocol versions:
- **r3** (619cc455…6e07): first production version.
- **r4** (80d731fe…80c0): no GB launch while a GA desk driver is alive.
- **r5** (9833abfc…a37e): race-free HOLD markers.
- **r6** (89fa8959…7032): staged transport. Kissat runs alone and its proof is collected into RAM; drat-trim then
  runs alone on that proof.

r3–r5 used concurrent transport. r6 is approved for the remaining five items. Each diff was sent to the parent
before use.

Worker results so far (concurrent transport). All are PASS with exact rc20/s UNSATISFIABLE and rc0/s VERIFIED,
measured feeds, proof SHA and bytes, raw-stream hashes, and duplicate-literal count 375334:

| Leaf | Wall (s) | Peak aggregate RSS |
|---|---|---|
| P1-B4 | 184.0 | 3.69GB |
| P0-B4 | 185.1 | 3.69GB |
| P0-B5 | 183.1 | 3.68GB |
| P0-B6 | 441.8 | 5.94GB |
| P1-B6 | 412.5 | 5.39GB |
| P2-C4 | 277.5 | 5.50GB |
| P2-C3 | 268.2 | 6.08GB |

The r4 attempt at P0-B1 is STOPPED_UNKNOWN: a hold-boundary SIGTERM arrived 0.5s after it launched. It remains
UNKNOWN; r6 will run a new attempt. Remaining items: P0-B1, P0-B2, P0-B3, P2-C2 and P2-C1. These are
worker results, not parent-qualified evidence. GB strengthened counterparts are not authorised until the
twelve are done and the GB NF bridge `review/GB_NF_GENUINE_BRIDGE.r1.md` (1a352d36…504b, UNREVIEWED) is accepted.

### 20.4 Assembly r3, GB reviews and current hold (09:30 PDT)
`review/N8_ASSEMBLY.r3.md` SHA `64d5d06b77f611c00ede71a8826102734e3d09a39e3028b761c24edbb8710345` supersedes r2,
which is preserved; the exact diff is `review/N8_ASSEMBLY.r2-to-r3.diff` 28497a38…5f50. The registry is
`review/N8_ASSEMBLY_LINKS.r3.json` 83eed664…64ac: 80 files rehashed, and every r1 entry is identical in r1/r2/r3.
r3 applies the ten Claude r2-delta MINORs; the Codex r2 delta was ACCEPT 0/0/0. It records these parent decisions:
- A7 is confirmed by NF erratum-1 da050a74…87c2.
- A single §7 certification predicate binds all36 counted replays: GA 12+6 and GB 12+6.
- A10 has three parts: parent acceptance of the GB necessity note; parent acceptance of the genuine bridge; and
  18 counted GB parent replays. The22 GB hashes are input identities only.
- No worker-only PASS substitutes for a parent replay.

GB review status:
- **Codex:** necessity ACCEPT; bridge ACCEPT-WITH-FIXES.
- **Claude:** ACCEPT-WITH-FIXES, 0/0/6+6.
- **Errata:** x-created `review/GB_REVIEW_ERRATUM.r1.md` 7b51788c…1c4e and `review/GB_REVIEW_ERRATUM.r2.md`
  a2d3b9b3…407d.
- **Parent acceptance:** pending.

GB worker runs are HELD under parent HOLD-2: 8/12 direct PASS as worker evidence, four remaining. The parent's
GA formula batch was interrupted at09:25:51 by an external SIGTERM of unestablished cause. This lane had nothing
running at that time. There is still no n8 theorem.

On parent instruction, the four remaining worker GB items (P0-B2, P0-B3, P2-C2, P2-C1) are stood down; marker
`evidence/gb_direct_v6/hold/STANDDOWN-1.json`. This lane runs no further worker native solver or checker, even
after a RELEASE. All M8 native capacity now goes first to parent GA replays, then to counted parent GB replays.

Static handoff `review/GB_R6_PARENT_HANDOFF.r1.md` 0870f26c…dc1b documents the frozen staged r6 pipeline for a
parent-owned replay. It gives the API with file:line references, how to supply independently bound bytes
(including the six strengthened ids), the receipt fields and criteria, and the required changes.

An optional, unreviewed contingency is `review/P1_PAIR_REFINEMENT_OPTION.r1.md`. It uses pair orbits, because P1-B3
and P1-B5 each have at least two permutation squares. Nothing has been generated for it, and it changes no amendment.
