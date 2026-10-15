# Extended constructive search protocol

Recorded 2026-10-14 before the extended runs. This continues the bounded initial portfolio, at the parent's explicit request for multi-hour attempts. A certificate for57 or87 would be a new case, not a solution of the book's universal conjecture.

## Fixed mathematical model

For each v in{57,87}, put n=v−2, pointsZ_n∪{u=n,w=n+1}, with translations fixing u,w. Seek one KTS transverse to all translation orbits of triples. There is **no nonidentity multiplier or invariant-resolution symmetry requirement** in this portfolio.

Normalize the infinity-pair block to{0,u,w}. The remaining u-blocks define a perfect matching M_u of{1,…,n−1}, as do the w-blocks M_w. Each matching uses every unsigned difference1,…,(n−1)/2 exactly once, and the two matchings are edge-disjoint. These are necessary conditions for every cyclic-transversal solution.

Stage1 samples such matching pairs with an exactly specified CP-SAT seed/variable order. Some configurations explicitly restrict M_u to the patterned matching{x,−x}; others do not. The restriction is not WLOG. Each sampled pair is saved verbatim.

Stage2 removes those matching edges fromK_n and seeks a triangle decomposition using exactly one representative from every finite translation orbit. Its exact-cover columns are all remaining finite pairs and all finite triple-orbits. It has onlyO(n³) primary Boolean variables, rather than theO(n⁴) block/class expansion of the initial portfolio. CNF uses a documented sequential at-most-one encoding plus at-least-one clauses. The same exact cover can alternatively use CP-SAT.

Stage3 resolves each candidate STS with CP-SAT: every block is used once; each class partitions allvpoints. The u-blocks canonically label the classes by unsigned difference, with class0 containing{0,u,w}. This imposes no further resolution symmetry. A successful resolution is developed into a full certificate and checked by the existing independent checker.

Candidate STSs may be skipped after a resolution time limit; such a skipped candidate is **not proved nonresolvable**. Blocking a previously sampled candidate only diversifies the portfolio; it is not a mathematical nonexistence deduction. Freezing sampled matchings also restricts the search. An exhausted or time-limited portfolio does not rule out the full cyclic model.

## Main-agent portfolio

Six configurations, each with a7200-second overall wall limit (including all three stages). Stage1 matching cap5s, each Stage2 solve cap180s, each Stage3 resolution cap90s; up to20 STS candidates per matching pair before drawing another pair. The overall deadline is authoritative. Configurations:

|v|Stage2 solver/config|seed|M_u patterned?|solver threads|
|---|---|---:|---|---:|
|57|kissat --sat|101|no|1|
|57|cadical --default|102|yes|1|
|87|kissat --sat|103|yes|1|
|87|cadical --default|104|no|1|
|57|CP-SAT|105|no|2|
|87|CP-SAT|106|no|2|

Known-case validation on9/15 occurs after implementation and before these six runs. All phase outputs are logged with instance/source hashes, parameters, caps, observed runtime and status. The generated CNF and raw large model output may live in/tmp and be overwritten between phases; saved matching/candidate data and the deterministic source/seed permit exact regeneration. Solver logs retain status/statistics; SAT variable lines are replaced by the selected primary-row certificate and a SHA256 of the complete raw output.

## Independent slices and global resources

- C19 slice: at most4 threads/12GB; fixed-constituent patterns36+19 and17+19+19 onZ19×3. Rigorous early obstructions are permitted instead of futile long runs; remaining staged search cap at least7200s.
- Alternative-group slice: at most2 threads/4GB; genuinely different actions or block-set-only automorphisms, with an actual constructive search if the reduction survives elementary obstructions.
- Main staged runs:8 solver threads total. Global configured solver concurrency at most14, leaving2 threads for one independent check after any success. Small staged models avoid the multi-million-variable class-expanded formulation; total RAM must remain below48GB. BLAS/OpenMP helper threading is limited to1.
- All original run receipts remain immutable. New artifacts use `extended-*`, `c19-*`, or `group-*` prefixes. No old UNKNOWN is relabelled UNSAT by a later theorem.
- Stop on an independently verified full certificate; otherwise finish the stated finite portfolio, save exact remaining limitations, and stop all owned processes.

## Addendum recorded before the joint-modular target run

A complementary **unfrozen** cyclic STS model was derived: one shift variable per finite triple-orbit, two infinity-edge positions per unsigned difference, and modular all-different constraints for every concrete pair-orbit. Both infinity matchings are solved jointly rather than sampled and frozen. This model has531 primary variables at57, versus the initial776,161 class-placement Booleans; the actual CP-SAT expanded representation is solver-dependent. It then seeks an unrestricted resolution of each resulting STS. Its exactness argument is in `staged-encoding.md` and implementation in `work/search_modular.py`.

After known-case validation, run order57, seed57007, **7200-second overall limit**, one solver worker, with a7200-second first-stage limit (clipped by remaining total time) and240-second resolution limits. This supplies a genuinely multi-hour single-instance configuration as well as the earlier diversified180-second frozen-matching slices. Rejected or unresolved candidate resolutions remain explicitly distinguished.

The alternative-group worker also runs the nonabelian `F_55=C_11⋊C_5` regular-development model for7200seconds with **one** extra worker; its reflection-blockset/unrestricted-resolution run retains two workers. With eight main staged workers, four C19 workers, three alternative-group workers and one modular worker, the configured solver cap is **16**, not14. The short order21 calibration finished before these extra allocations. Individual models are staged/compact and the total RAM cap remains48GB.
