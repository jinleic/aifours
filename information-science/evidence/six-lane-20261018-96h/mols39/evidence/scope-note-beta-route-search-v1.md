# Scope note — slice "beta-route extension search package" (2026-10-19T07:52:21-0700, ContinueCFR21)

Parent IRC of about 07:5x offered two options, one to be chosen, written only, with no execution and no search run.
CHOSEN: option (a). Frozen before any derivation.

## Question (exact; R1 base eabe1fc4... with E1 74bc52ca... and E2 88a43699..., accepted as an existence
## equivalence by the parent verdict /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-R1-parent-verdict-v1.md (dc66a8b5...))
Anchor D = the exact raw Sage DM_39_6_1 (sha256 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a), 6 x 39
over Z_39. The question: does there exist f : columns -> Z_39 with D_x - f a bijection for x = 0..5? We normalise
f(column 0) = 0. This loses nothing, because f + t is again an extension, and column 0 of the anchor is the zero
column. By corrected R1 this is equivalent to the beta-route question: a new mod-13 row g with every b_x - g 3-to-1
(b = D mod 13), followed by a mod-3 lift. It is currently UNKNOWN: v1 T2 and v2 T6 stopped incomplete at 270-282 s,
and T6 explored 8,081,408 nodes.

## Deliverable of this slice (WRITTEN ONLY; success criteria)
SC1. This scope note is frozen before any derivation.
SC2. A frozen source package:
  - a normative problem/format specification;
  - the beta-route producer: stage 1 is a mod-q multiplicity exact cover with supply pruning; stage 2 is an exact
    GF(3) lift per stage-1 solution, by fibre-sum elimination plus enumeration plus a rainbow test. It is generic in
    n = 3q (q % 3 != 0) and in the number of base rows. It splits the search into deterministic static chunks by
    the values of fixed split columns, with exact coverage accounting.
  - an INDEPENDENT second exhaustive search, authored by a separate subagent from the definition only, by a
    different method (joint Z_n exact cover). It must not read the producer.
  - preregistered controls with mathematically known answers;
  - an expectation gate built on the v3 certificate-review lessons: actual artifacts, strict JSON, typed equality,
    audited prefix, claim unevaluated until the end;
  - a run plan with one exact parent GO per job.
  The package must fit the narrowed supervisor contract (/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/rqls10-supervisor-v10-scope-parent-decision-v1.json, sha256 e441d8585228c2976700cba2c3397acfa1e544bc3dfe7af919205581572af22b): single-process children with no
  fork, exec, subprocess or multiprocessing; stdlib only; exact declared outputs; result.json last; GO entrypoints of
  the v2 design; no human-readable timestamps produced by children.
SC3. Projections:
  - exact RAM upper bounds per job, by formula from (n, q, k) and evaluated for every planned input;
  - exact per-node work bounds in elementary updates;
  - the one measured fact, a lower bound on the anchor's joint tree: more than 8,081,408 nodes, from the v2 engine
    at about 2.9e4 nodes/s in CPython;
  - a preregistered, deterministic, INFORMATIONAL calibration job (seeded Knuth estimator) whose output is never
    evidence and only informs a later parent decision.
  Total work for the anchor is UNKNOWN until calibration, and the package says so explicitly.
SC4. Controls with known answers:
  - the 2-row DMs over Z_6 and Z_12 have no one-row extension (no complete mapping of a cyclic group of even order;
    classical), so the expected solution set is empty;
  - Sage DM_21_6_1 minus its last row (5 rows over Z_21): the deleted row, normalised, must be among the
    solutions, and both programs must report identical solution sets;
  - the Singer-type (57,8;1)-DM minus one row, in the single static chunk that contains the deleted row: that row
    must be found ("planted chunk");
  - invalid inputs (not a DM, wrong pin) must be rejected for the intended reason.
SC5. Claim boundaries are stated:
  - nothing is claimed from writing;
  - a future COMPLETE run on which both independent programs agree gives a scoped result on the exact anchor only;
  - any extension found is a 6-MOLS(39) CANDIDATE and triggers the candidate protocol (stop, pin, checkers A/B/C,
    parent).
Abort criterion: if a design that meets the narrowed contract cannot be written (for example because it needs a
subprocess or compiled code), the package reports this instead of being shipped.
No anchor job is requested in this slice. Requesting one needs the calibration result and a separate parent decision.

## Why not option (b) (no derivation attempted beyond these checks)
No obstruction is visible:
- Theorem A, L3 and Proposition C exclude only specific mod-3 shapes of the new row.
- Power-sum identities (sum of (D_x - f)^j over the columns is the same for every x) give polynomial conditions of
  growing degree. These are equivalent to bijectivity only at full degree, which is the search itself.
- The character-orthogonality and dimension counts allow up to 39 rows.
- The G6 action shows only that any normalised extensions come in free G6-orbits of size 6, given T1/T3/T4 and the
  twisted reduction. This is a divisibility statement, not a nonexistence one.
[HEURISTIC] The expected number of normalised extensions of a fixed 6-row DM over Z_39 is about
39^38 * (39!/39^39)^6 ~ 1e-34.
