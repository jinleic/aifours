# Mathematical progress and remaining gaps

The universal book assertion is **not solved**. No counterexample is proved. LKTS(57) and LKTS(87) remain separate unsolved target cases unless a fully resolved certificate passes the existing independent full checker. No independent reviewer acceptance is claimed by this actor. The enclosing sanctioned HMZ reviewer must return `done:false` while the universal goal remains unproved.

## Actual formal result

`Formal.lean` uses genuine finite three-subsets of Fin v, genuine finite unordered pairs, exact pair coverage, exact point partitions, explicit class disjointness, exact class union, and an LKTS with exactly v-2 constituents and all triples covered. `Kirkman.FullGoal` keeps the original t>=1 universal statement without any group restriction; it is defined, not proved.

Two substantive results are proved:

1. `Kirkman.resolved_rows_sound`: selected rows whose pair columns and (class,point) columns are exact-one columns determine a resolved STS. The proof first derives selected-row uniqueness for each actual block from exact pair coverage and the existence of a two-subset in every triple. It then proves actual point partitions, disjoint block classes, and exact union. This matches the concrete pair-placement and resolution interfaces rather than hiding KTS validity in a certificate field.
2. `Kirkman.development_sound`: invariant resolved constituents plus free resolved transversal bases develop to an LKTS under explicit orbit-fiber, orbit-invariance, freeness, and unique-orbit-owner hypotheses. The theorem proves constituent block-disjointness and equality of their union with all triples. Relabeling of pair coverage and complete resolutions is proved internally. Its input does not assume the developed family is already disjoint or already covers all triples. `Kirkman.lkts_fin` transfers the resulting finite index set to exactly Fin(v-2).

These are new formalizations of standard exact-cover/development reasoning, not new existence mathematics. Every auxiliary named theorem is listed separately in `claims.json`, with its actual assumptions, partial scope and permitted transitive axioms. A conditional soundness theorem does not supply any of the missing bases.

The theorem requires invariance of fixed block sets; it does not require their chosen resolutions to be invariant. The concrete replacement model does impose that stronger resolution symmetry. Every free base still needs its own genuine resolution.

The main development theorem applies to sizes(17,2,19) for the released57 route (16 retained plus a replacement), and(27,2,29) for the surviving87 route. Those are applications conditional on finding the complete resolved seed packages and verifying the action hypotheses, not currently checked instantiations.

## Released constituent: exact joint model

The read-only frozen17-packing was hash-checked and all constituents independently expanded. Zero-based system16 was released;0..15 are retained. Their448 occupied orbits leave1092, of types:

| Triple type | Available orbits |
|---|---:|
| AAA | 89 |
| AAB | 786 |
| ABC | 217 |

Every pair orbit has39 available incidences, counted with multiplicity. In particular, AP triples contribute their repeated pair-orbit incidences separately. There are27 AP orbits, none admissible for the invariant replacement, so all must be assigned to the two free bases.

The replacement reuses `c19_search.fixed_model` starter placements and fixed ABC seeds. To generate all row types its constructor is called with u=5, then the **local returned model's** final u equality is broadened to4<=u<=9. This permits every feasible aggregate starter count. Indeed, within-layer pair coverage gives3u+w=27, while the starter's19 blocks giveu+w+z=19, so w=27-3u andz=2u-8. Nonnegativity gives precisely4<=u<=9. No replacement is solved or frozen first.

Replacement rows:20452 (19 placements for each of1065 admissible available orbits, plus217 fixed ABC seed rows). Free rows:41496=1092*19*2. Every free row means one concrete translated block in one of two free STS bases. The entire model has61948 Boolean variables. Its4425 exact-one constraints are:

- 57 replacement starter point columns;
- 84 replacement pair-orbit columns;
- 1092 **joint** orbit columns, coupling replacement rows and both free-base placements;
- 3192 concrete pair columns (1596 in each free base).

Two further linear constraints bound replacement u in[4,9] and normalize an obligatory-free AP orbit to canonical shift0 in base0, giving4427 total constraints. The anchor is lossless by base interchange followed by translation of base0; the fixed replacement uses a full orbit and hence does not interfere. No further ordering of the two base completions of{0,1} is imposed.

The joint orbit columns have degrees38 for27 AP orbits,57 for848 other non-ABC orbits, and58 for217 ABC orbits. Each concrete free-base pair column has degree39; each replacement point column has degree1065. `audit_joint.py` checked every row and every actual exported column, including both linear domains, against the saved input and independent full19-shift conventions. Its audit is solver-free and does not certify a negative answer.

Any satisfying replacement uses28 whole triple orbits: each selected row supplies3 distinct pair-orbit incidences, so the84 exact pair-orbit columns force28 rows, all with distinct orbit ids. The57 starter point columns force19 starter blocks; the remaining9 rows are fixed ABC class seeds. Each free pair cover has532 blocks, since its1596 concrete pairs are partitioned into three per block. The orbit columns consequently allocate28+532+532=1092. All pair coverage and class validity are independently rechecked on a positive candidate.

If the replacement has starter AAA countu, the two free bases together must use89-u AAA orbits,759+3u AAB orbits and216-2u ABC orbits. These are compatible inventory identities, not a structural contradiction and not an existence proof. A simple pair-orbit capacity deficit is absent: the replacement removes one of the39 incidences in every pair orbit, leaving38 for the two bases. Higher-order compatibility, concrete shifts, and resolutions remain essential.

## One bounded construction attempt

Command, from this repository:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONFAULTHANDLER=1 UV_CACHE_DIR=/tmp/lkts-uv-cache \
  uv run --offline --with ortools==9.15.6755 python joint_search.py \
  --seconds 600 --pair-seconds 480 --threads 2 --seed 19161014
```

Only one pair-cover solve is authorized by the script; it performs no retry, no candidate blocking, and no greedy replacement solve. A satisfying assignment is preserved before two unrestricted resolution calls, whose caps share the remaining600-second overall allowance. A negative resolution verdict is preserved as solver-reported; an UNKNOWN verdict is not described as nonresolvability. The complete55-system certificate is created only if both genuine resolutions are found, and is then passed to the existing `check_lkts.py`.

The call ended normally with **UNKNOWN** after480.009102 solver seconds (480.775230 total wall seconds), using2 workers,5365856 branches and626858 conflicts. No pair-cover candidate was found; both unrestricted resolution stages and the full-certificate checker were therefore **not reached**. No candidate was blocked. This is not infeasibility of the released slice or of any larger target. Exact receipt: `evidence/joint57/result.json`; command stdout/stderr: `evidence/joint-command-fixed.log`. The instance was saved before solving:

- `evidence/joint57/input-packing17.json`, `retained16.json`, `released-system16.json`;
- `inventory.json`, `rows.json`, `model.pbtxt`, `manifest.json`;
- model SHA256 `bf462e329e881c58329fed6e13cfd3a312d8217ab14b516ec9cc436298e3d399`;
- rows SHA256 `3930a97ef6ae621fb1c01096b0935e4fc9604fd2c2a1bbdbbff4e0102edd951e`;
- exact source snapshots, source hashes, solver parameters and `pair.log`;
- `evidence/joint-model-audit.json` and its log (PASS).

The previous7200-second portfolio and known small-case searches were not run. This bounded attempt never exhausts the joint model merely by timing out.

## Order87 structural compatibility

Only the27-fixed plus two-free29-orbit pattern is considered. Its129 pair orbits each need85 constituent incidences. The27 invariant resolved constituents would consume one incidence each, leaving58 for the two free bases. Its3655 triple orbits split into27*43=1161 fixed orbits and2*1247=2494 free-base orbits. All42 AP orbits must occur in the free bases.

For each fixed starter,3A+B=42 andA+B+C=29 imply C=2A-13. For each layer,3A_i+S_i=14 and the point partition give T_i=3A_i+1-C, so0<=A_i<=4 and7<=A<=12. Across27 constituents the minimum189 admissible AAA orbits is within the336 available. Thus these necessary aggregate conditions are compatible; no contradiction or seed package is proved. The same formal development criterion would verify the final triple partition once the actual27 resolved fixed constituents and two resolved free bases were supplied. No87 search or certificate is claimed here.

## Trust, negative control, and workflow errors

The Lean runtime is4.34.1. Successful incremental elaboration is recorded in `evidence/lean-iteration-02.log` and `lean-iteration-03.log`; the latter contains all11 theorem statements and all11 axiom reports. Each has only `propext`, `Classical.choice`, `Quot.sound`. No nonstandard proof escape, OAI import, dependency update, corpus rebuild, or Comparator/nanoda replay was used.

`NegativeControl.lean` is the complete self-contained formal source followed by a broken pair column: two selected rows{0,1,2} and{0,1,3} both contain pair{0,1} on Fin9. It tries to prove exact-one coverage for that actual pair. Rejection must be a mathematical failure of uniqueness under ordinary `decide`; the full logs are retained by the frozen verifier. This does not purport to check a valid small LKTS case.

Two implementation errors are preserved transparently:

- The initial `cat` wrote a new `Formal.lean` in the cached runtime cwd while the intended compile path was in scratch. That compile failed with “no such file”; log `lean-iteration-01.log`. The new file was moved into this owned repository immediately. No tracked cached `Formal.lean` existed, and no such file remains there. No tracked runtime, Mathlib or OAI source was edited.
- The first model build crashed **before solver invocation** because OR-Tools9.15's pybind repeated-constraint accessor segfaulted on index-1. A solver-free diagnostic isolates that line. The corrected builder uses the nonnegative indexlen-1. Historical inputs/source are in `joint57-build-failed/`; crash code139 and zero solver calls are recorded in `joint-build-failure.json`. This is not a mathematical failure, an UNSAT answer, or a second search attempt.

The first partial-gate invocation returned0 mechanically, but semantic inspection found that the negative control failed to synthesize decidability for ExistsUnique instead of disproving the corrupt column. That receipt is explicitly not accepted as a meaningful control; its exact source/logs are preserved in `evidence/verification-pre-control-fix/`. The control now unfolds ExistsUnique before ordinary `decide`. Necessary incremental elaboration (`evidence/negative-control-iteration-01.log`) rejects the concrete exact-one proposition as **false**, with no syntax or instance-synthesis error. This correction does not change Formal.lean, the theorem claims or the frozen checker.

Final frozen verification is run once per prescribed mode for the corrected final sources. `--partial` can accept only partial source/Lean/control evidence; the ordinary gate must fail while `full_goal_solved:false`. Full semantic acceptance belongs to the enclosing actual HMZ reviewer, not the Python gate. TASK.md, ACCEPTANCE.md, verify.py and the baseline commit remain unchanged. No new commit, nested HMZ, separate reviewer, subagent, external message or paid infrastructure was used.

## Exact remaining step

For this57 route, find the jointly compatible invariant replacement and two orbit-transversal STS bases, then supply genuine unrestricted resolutions for both bases. The current theorem can then prove the development sound, but a concrete input certificate and kernel-checked action/instance facts would still be required for a kernel-checked target construction. A Python positive check alone is not represented as a Lean certificate.

For87, the full27+29+29 resolved seed package is missing. For the original book goal, a universal construction or a genuine counterexample is missing; settling one of57/87 would still leave that universal goal unproved. No timeout is evidence of infeasibility.

## Final observed verification

- Corrected-source `python3 verify.py --partial`: exit0; `verification-partial.json` records all11 observed permitted-axiom reports, successful kernel elaboration, and the meaningful rejection control. Its exact logs are also retained under `evidence/verification-partial-final/` before the ordinary gate recompiles the same sources.
- `python3 verify.py`: exit1, with the sole error “The universal original goal remains unsolved; partial evidence is not RLAR acceptance.” Source/Lean/control evidence passed within that full invocation. `verification-full.json` and `evidence/verify-full-command.log` preserve the actual result.
- Final negative-control log: Lean reports ordinary `decide` proved the concrete exact-one selected-row proposition **false**. It is not a syntax failure, missing instance or unrelated arithmetic assertion.
- TASK.md, ACCEPTANCE.md and verify.py hash-match the frozen baseline. The baseline commit remains `a0d6e7b38c054b3d00b76a94292675af94e540dd`; no further commit was made. Reference/helper/packing hashes are unchanged.
- The construction process exited0, with solver status UNKNOWN; a current process-table check found no remaining joint_search.py Python/uv process. Exact process receipt: `evidence/construction-process.json`.
- Full goal solved:false; target57 solved:false; target87 solved:false. The actual enclosing HMZ reviewer/journal is controlled by the owner; this actor did not launch, substitute or fabricate a reviewer verdict. Full RLAR acceptance is not met and the reviewer must return done:false for the unresolved original theorem.
