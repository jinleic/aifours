# Six-lane phys-1 (third target): Ball–Simoens Problem 16 at n = 7 — are 4 MOQLS(7) necessarily classical?

Lane: `physics/evidence/six-lane-20261016/moqls7-problem16/` (owns `sources/ code/ evidence/ review/`).
Contract: `institute/runs/six-lane-2026-10-16/screening/phys-1-moqls7-problem16-contract.json` (recorded 02:03:18 PDT).
Previous phys-1 lanes (`../depolarizing/`, `../dualunitary-t7/`) are closed and preserved; nothing there is modified.

## 0. Frozen protocol (written 2026-10-17 after 02:03:46 PDT, before any computation in this lane)

### 0.1 Source and definitions (read in full: `sources/2607.12933v2.raw.txt`, PDF SHA-256 2d60d45f…21afe = parent pin)

QLS(n): n×n array of unit vectors of C^n, every row and column an ONB. Orthogonal: {ψ_ij ⊗ φ_ij} is an ONB of
C^n ⊗ C^n. Set isotopy: phases, simultaneous row/column permutations, a separate unitary per square. Classical: up to
isotopy all entries in {|1⟩,…,|n⟩}. M(n) = largest t with a non-classical set of t MOQLS(n). Standard form (rule #1):
first row of every square = |1⟩,…,|n⟩. Rules #2 (unitary patterns), #3 (zero overlap off the first row), Lemma 10
(weight ≤ 2 squares can be made classical preserving all orthogonalities and with supports shrinking), Theorem 9
(Shrikhande: n−3 MOLS(n) extend to n−1, n ≠ 4), Theorem 5 (n−2 MOQLS(n) classical), Theorem 6/Cor 7 constructions.

### 0.2 Target and readings

Problem 16 at n = 7: every set of 4 MOQLS(7) classical? Baseline 2 ≤ M(7) ≤ 4 (Cor 7 / Huang–Li; Theorem 5).
- Positive answer = complete proof; negative = exact non-classical witness (two exact checkers, ray-count invariant).
- Partial results (reportable as partial only): weight-3 exclusion, complete reductions to stated finite cases.

### 0.3 Route (frozen before computation)

1. Re-derive the weight bound (expected ≤ 3 off the reference row; weight 3 forces weight 1 in the other squares).
2. Weight ≤ 2 case: Lemma 10 + Theorem 9; test whether the final contradiction survives with two added squares;
   if the pigeonhole fails, look for a structural replacement (n = 7 specific facts allowed if cited exactly:
   uniqueness of the plane of order 7, complete-set structure).
3. Weight-3 case: first the sub-case where the other three squares are classical (orthonormal assignments on a
   5-net), then the general case; exhaustive steps only with stated reductions and two independent implementations.
4. Any finite fact used in a proof gets two independent implementations, positive and mutation controls.
5. Witness route only if a weight-3 configuration is shown realizable.

### 0.4 Controls

Theorem 5 at n = 7 must be reproduced by the same method; methods must not "prove" classicality where non-classical
objects exist (Cor 7 pair: 3-class nets; 4-class nets); mutation controls for every checker; any external
computational classification used (e.g. MOLS enumeration) is cited, not silently assumed.

### 0.5 Resources / permissions

≤ 4 CPU, ≤ 8 GiB, checkpoints ≤ 30 min, host-clock timestamps; Python `../depolarizing/env` read-only with `-B`
(stdlib only for the finite checks). No deletion, publication, external contact, paid fallback.

## 1. Log

See `evidence/LOG.md`.

## 2. Next bounded step (approved by parent 2026-10-17 ~02:26 PDT): 2 quantum + 2 classical squares — FROZEN
## representation, written at 02:2x PDT (host clock at freeze: see LOG) BEFORE any computation for this step

Class K2: 4 MOQLS(7) with Ψ3, Ψ4 classical (symbol arrays L3, L4 = a pair of MOLS(7), standard form w.r.t. row 0),
Ψ1, Ψ2 non-classical. By Theorem C (applied after relabelling which two net classes are rows/columns — the 4-net
{rows, columns, L3-lines, L4-lines} is symmetric for the constraints) both Ψ1 and Ψ2 have weight-3 entries in the
frame of ANY line of the 4-net.

**Pattern variables (row-0 frame):** S_s(c) ⊆ [7] for c = (i,j), i ≥ 1, s ∈ {1,2}; first-row cells have S = {j}.
**Necessary conditions** (each follows from Prop 1 + Lemma 2 of review/PROOF_PARTIAL.md):
- (P1) S_s(c) ≠ ∅; S_s(c) ∩ {j, L3(c), L4(c)} = ∅; S1(c) ∩ S2(c) = ∅.
- (P2) For every line M of the 4-net (7 rows, 7 columns, 7 L3-lines, 7 L4-lines, each incl. its first-row cell) and
  s = 1, 2, the 7×7 support pattern is that of a unitary matrix, so: (a) every coordinate is covered by some cell of M;
  (b) no two cells of M share exactly one coordinate; (c) no two coordinates co-occur in exactly one cell of M.
- (P3) For all pairs of distinct cells: not both |S1(c)∩S1(c′)| = 1 and |S2(c)∩S2(c′)| = 1.
- (P4) Some cell has |S1| = 3 and some cell has |S2| = 3.
- (P5) Either FIXED (L3, L4) = (j + s3·i, j + s4·i) (AG(2,7) pairs; {s3,s4} = {1,2} harmonic, {1,3} equianharmonic —
  the only two isomorphism types of extendable pairs), or GENERIC: L3, L4 arbitrary MOLS(7) in standard form, encoded
  as variables, with symmetry breaking L3(i,0) = i (i = 1..6; simultaneous permutation of rows 1..6 is an isotopy).
  GENERIC covers every pair of MOLS(7), extendable or maximal, without relying on a classification.
**Decision rule:** UNSAT of GENERIC (two independent encoders/solvers, proof-checked) ⇒ class K2 is empty.
SAT ⇒ candidate patterns: first strengthen with further necessary conditions (rank/Hall conditions on lines;
additional frames sharing L3, L4), then exact realizability only for survivors; report surviving patterns exactly.
Soundness requirement: every clause is satisfied by the canonical encoding of any real configuration (auxiliary
variables defined by full equivalences).
**Implementations:** A = `code/k2_encode_a.py` (+ CaDiCaL), B = `code/k2_encode_b.py` (independent auxiliary scheme,
+ kissat). Egan–Wanless data on maximal 2-MOLS(7) is cross-checked where feasible, but the GENERIC encoding does not
depend on it.

### §2 addendum A (frozen before the corresponding runs; host time in LOG)
- Classes K3 (3 quantum + 1 classical) and K4 (4 quantum): same conditions with the obvious changes; (P4) becomes
  "EVERY quantum square has a weight-3 entry in the row-0 frame": S′ was built by applying Lemma 10 (frame row 0) to
  each square without weight-3 entries, so the non-classical squares of S′ are exactly those with weight-3 entries.
  The same holds for K2 (both quantum squares), as already used.
- (SB2) symmetry breaking at cell (1,0), sound by: simultaneous permutation of rows 1..6; column permutations σ with
  the coordinate/symbol relabelling k ↦ σ(k) in every square (keeps the standard form); both preserve every
  condition. WLOG Ψ1 has its weight-3 entry at (1,0); the classical squares carry symbols 1, 2, … there; the
  remaining 3 + (m − 1) coordinates (m quantum squares, m + #classical = 4) are split S1(1,0) = the three smallest,
  then one singleton each for Ψ2, …, Ψm (forced: supports are disjoint, nonempty); rows 2..6 sorted so that the first
  classical square has L(i,0) = i.
- Lesson recorded: no DRAT proof output for exploratory/long runs (four UNKNOWN-run proofs reached 17.6 GB; moved to
  ~/.Trash, see evidence/MOVED_TO_TRASH_*.txt). Proofs only for runs known to finish, re-run with proof afterwards.

### §2 note (parent instruction, 2026-10-17): the ~/.Trash relocation mentioned in addendum A is a
scope/preservation deviation (see evidence/LOG.md, "SCOPE/PRESERVATION DEVIATION"); no further moves/deletions.
