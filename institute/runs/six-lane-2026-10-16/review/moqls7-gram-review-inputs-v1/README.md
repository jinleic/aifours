# Six-lane phys-2 (sixth target): determine M(7) — does a non-classical set of 3 MOQLS(7) exist?

Lane: `physics/evidence/six-lane-20261016/moqls7-maximum/` (owns `sources/ code/ evidence/ explore/ review/
archive/`). Contract: `institute/runs/six-lane-2026-10-16/screening/phys-2-moqls7-maximum-contract.json` (SHA-256
21b1b38bf82e2923518ce8fd1a8885f38427d2a07ac968fbec53e0150744d372, recorded 16:50:58 PDT). Screen:
`screening/phys-next-screen-v3.md` (3975fba4…19a). Read-only: the AME lane, `moqls7-problem16/`, `moqls8-problem16/`,
all parent run directories. Accepted baseline: 2 ≤ M(7) ≤ 3 (`review/moqls7-parent-verdict.md`, a39911fd…ff3a2).

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
