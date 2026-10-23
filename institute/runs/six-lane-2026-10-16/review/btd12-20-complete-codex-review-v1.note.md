VERDICT: ACCEPT-WITH-FIXES

The frozen snapshot supports the unrestricted nonexistence claim as a computer-assisted proof under the trusted base below. I found no fatal or major failure in the mathematics, enumeration, encoding, or actual certificate coverage. The fixes concern runner behavior and reporting.

All references below are relative to the supplied snapshot.

**Minor findings**

- **The certificate runner’s aggregate exit status is not fail-closed.** `code/cert_run.py:115` returns 0 even when cases have status `UNKNOWN` or `UNSAT_UNVERIFIED`. It should require every requested case to be `CERTIFIED`. Per-case certification correctly requires exit 0 **and** a stripped line exactly equal to `s VERIFIED` (`code/cert_run.py:84`). The completed replay also enforces this condition (`code/case_split_replay.py:173`). All actual records passed, so this defect does not invalidate this result.
- **The runner documentation overstates its behavior.** `code/cert_run.py:7` says both checkers run on a decoded SAT witness; the SAT branch at `code/cert_run.py:88` only writes the witness. The promised separate summary file at `code/cert_run.py:9` is instead a final JSONL record (`code/cert_run.py:111`). Neither issue affects the stored UNSAT certificates.
- **Executable pinning has a reproducibility gap.** `code/case_split_replay.py:115` hashes manifest absolute paths, but regeneration invokes executables through `PATH` (`code/case_split_replay.py:120`; `code/e_combos.py:27`; `code/enum_crosscheck.py:45`). Controls similarly invoke `kissat` by name (`code/dcomp_controls.py:51`). Record and hash the resolved executables actually invoked, or invoke the pinned paths directly. The snapshot establishes matching outputs, but does not independently establish executable resolution.

**Mathematical completeness**

The argument in `notes/case-split-r2.md:23` is sound. Pair intersections of distinct A-supports are even, and column covers are in `{0,2,4,6}`.

Lemma T’s split argument works: under a consistent split, intersecting parts must coincide, producing a partition into pairs (`notes/case-split-r2.md:42`). In the inconsistent-split case, the three seed tetrads span the stated seven-coordinate code. Every later tetrad’s restriction lies in that **local** span’s dual. Its weight therefore forces either another e7 tetrad or one extension to e8; local e8 self-duality prevents further coordinates (`notes/case-split-r2.md:49`). There is no assumption that the whole twenty-coordinate code is self-dual.

My independent in-memory checks recovered the dual distribution `{0:1,3:7,4:7,7:1}`, all seven extensions’ self-duality and distribution `{0:1,4:14,8:1}`, and the recorded bijections to the enumerator’s tetrads.

Different adjacency components have disjoint supports. Multiplicities remain row multiplicities, including identical A-rows; their pair constraints are still imposed. Non-d components have full support on seven or eight coordinates, so at most two fit. Unused coordinates remain genuine columns requiring three D-entries (`notes/case-split-r2.md:72`, `notes/case-split-r2.md:97`). E0/E1 overlap causes harmless duplication.

**Enumeration completeness and binding**

The actual ranges are sufficient:

- E0 uses `n=4..10`, underlying simple graphs from `geng -q -d1 -D6 n 1:12`, then `multig -q -e12 -D6 -T` and the even-degree filter (`code/case_split_replay.py:119`; `code/mg_filter.py:19`). Degree sum 24 proves the lower bound; twenty coordinates prove the upper bound.
- E1 uses every `n=2..floor(remaining_columns/2)` with simple-edge lower bound `ceil(n/2)`, exact remaining edge count, and maximum degree six (`code/e_combos.py:18`). These bounds include every loopless admissible multigraph. Parallel multiplicity cannot exceed six because endpoint degree cannot exceed six. The zero-edge case explicitly supplies the empty graph.
- The `genbg` alternative uses vertex-node degrees 2–6 and edge-node degrees exactly two, without forbidding duplicate neighborhoods (`code/enum_crosscheck.py:42`). Thus it represents parallel edges and disconnected graphs.

The e-multiset search exhausts nonnegative multiplicities with total at most twelve and point degrees at most six. Its group computation tests **every tetrad**, not merely generators (`code/e_multisets.py:32`). Independently enumerating point permutations recovered group orders 168 and 1344. Expanding the stored representatives produced disjoint orbit unions of 694 and 52,060 valid vectors; independent enumeration recovered exactly those totals. Full-support totals were 505 and 47,306 vectors, represented by 17 and 187 orbits. Canonical minima and full-support metadata checked correctly.

Unordered component pairs include equal components; offsets, remaining rows/columns, and padding are correct (`code/e_combos.py:55`, `code/e_combos.py:66`). I independently reconstructed the case-list binding and checked every pattern. E0 counts are **7, 59, 312, 550, 616, 352, 173 = 2069**; E1 is **1004**.

The cross-checks have limited independence: `genbg` is a different graph encoding/generator within nauty; Burnside uses a separate recursion but shares tetrads/group construction; the E1 recount reuses the component-choice plan (`code/enum_crosscheck.py:142`). They are not independent end-to-end proofs.

**SAT equivalence and controls**

`code/dcomp_cnf.py:30` imposes exactly the required D constraints: off-A variables, row sum three, column sum `(6-a_j)/2`, and
\[
u+2z=(4-x)/2.
\]
Negative or odd residuals produce empty clauses. Identical A-rows give target zero and disjoint D-supports.

The AND clauses are biconditional (`code/btd_cnf_a.py:49`). The counter recurrence is biconditional prefix counting (`code/btd_cnf_a.py:78`), so repeated literal **positions** correctly implement weight two. Empty, zero-target, full-target, and impossible-target cases are correct for the nonnegative targets used here. Only `CNF` is imported; the other encoder’s symmetry and strengthening options are not applied.

Independent exhaustive checks covered 40 small cardinality instances, 23,864 complete assignments, and 128 AND truth cases. All passed.

Controls are substantive: they decode solver assignments and check the resulting matrices (`code/dcomp_controls.py:122`). I directly checked all six fixture matrices and six parent-decoded matrices, including preservation of A. Counting enumerates complete D-assignments and checks CNF extensions by propagation, asserting all auxiliaries are assigned (`code/dcomp_controls.py:88`); brute force separately checks matrix equations (`code/dcomp_controls.py:100`). Independent brute counts reproduced totals **12** over 27 patterns and **10** over 60 patterns, both nonvacuous.

**Certificates, replay, and limits**

The candidate SHA matches the supplied value. I verified all 39 parent fixed-file pins, all 37 manifest file hashes, and **all 6,146 actual CNF/proof hashes**, totaling **1,862,511,681 bytes**. Producer indices cover **0..3072 exactly once**, with matching unique case IDs; every record has `kissat_rc=20`, `drat_rc=0`, `verified=true`, and `CERTIFIED`.

The parent result was present and inspected once: `runs/case-split-replay-parent-r01/result.json:27` reports complete coverage, 3,073 rebuilt-equal CNFs, 3,073 verified proofs, and PASS. Its complete per-case ledger agrees. I did not rerun proofs or rebuild the target CNFs. Checker stdout is represented by receipts and the inspected acceptance logic, rather than retained raw logs. CP-SAT statuses contribute no proof authority.

The trusted base includes **nauty, Python/stdlib, the audited scripts, the C compiler/native-build chain, drat-trim, and the written mathematics**. Kissat is only a proof producer. This is not a Lean or independent-kernel proof; external tool sources, executable resolution, and build provenance were not independently re-established within this snapshot.

Procedural exception: one initial command listed the enclosing review directory; no sibling file contents were opened.