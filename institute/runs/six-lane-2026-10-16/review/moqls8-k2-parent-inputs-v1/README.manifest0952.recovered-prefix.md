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
