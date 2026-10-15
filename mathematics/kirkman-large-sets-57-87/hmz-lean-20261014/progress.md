# Mathematical progress and remaining gaps

The universal book assertion is **not solved**. No counterexample is proved. LKTS(57) and LKTS(87) remain separate unsolved target cases unless a fully resolved certificate passes the existing independent full checker. No independent reviewer acceptance is claimed by this actor. The enclosing sanctioned HMZ reviewer must return `done:false` while the universal goal remains unproved.

## Actual formal result

`Formal.lean` uses genuine finite three-subsets of Fin v, genuine finite unordered pairs, exact pair coverage, exact point partitions, explicit class disjointness, exact class union, and an LKTS with exactly v-2 constituents and all triples covered. `Kirkman.FullGoal` keeps the original t>=1 universal statement without any group restriction; it is defined, not proved.

Two substantive results are proved:

1. `Kirkman.resolved_rows_sound`: selected rows whose pair columns and (class,point) columns are exact-one columns determine a resolved STS. The proof first derives selected-row uniqueness for each actual block from exact pair coverage and the existence of a two-subset in every triple. It then proves actual point partitions, disjoint block classes, and exact union. This matches the concrete pair-placement and resolution interfaces rather than hiding KTS validity in a certificate field.
2. `Kirkman.development_sound`: invariant resolved constituents plus free resolved transversal bases develop to an LKTS under explicit orbit-fiber, orbit-invariance, freeness, and unique-orbit-owner hypotheses. The theorem proves constituent block-disjointness and equality of their union with all triples. Relabeling of pair coverage and complete resolutions is proved internally. Its input does not assume the developed family is already disjoint or already covers all triples. `Kirkman.lkts_fin` transfers the resulting finite index set to exactly Fin(v-2).

These are new formalizations of standard exact-cover/development reasoning, not new existence mathematics. Every auxiliary named theorem is listed separately in `claims.json`, with its actual assumptions, partial scope and permitted transitive axioms. A conditional soundness theorem does not supply any of the missing bases.

The theorem requires invariance of fixed block sets; it does not require their chosen resolutions to be invariant. The concrete replacement model does impose that stronger resolution symmetry. Every free base still needs its own genuine resolution.

The main development theorem applies to sizes(17,2,19) for the released57 route (16 retained plus a replacement), and(27,2,29) for the surviving87 route. The added `c19_development_sound` and `c29_development_sound` now discharge the concrete action hypotheses and constituent counts in Lean. Both applications remain conditional on finding the missing complete resolved seed packages.

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

1. **Universal acceptance:** prove `Kirkman.FullGoal` or supply a genuine counterexample to the universal assertion for every t>=1, v=6t+3. FullGoal is defined, not proved. Only settling this original statement can satisfy full acceptance; even a57 or87 construction would leave the universal goal open.

2. **Concrete certificate instantiation:** no concrete system has been proved `IsKTS` in Lean, including the16 retained systems in `evidence/joint57/retained16.json`. Neither concrete development corollary has had its seed-package hypotheses instantiated. A future certificate needs a kernel-checkable Boolean checker using permitted kernel reduction, with soundness into genuine `IsKTS`, fixed-block invariance, base transversality and orbit ownership. The kernel-proved concrete action/count facts are available; the actual certificate and its seed facts are not. For57, the replacement plus two orbit-transversal bases and genuine resolutions remain missing. For87, the entire27+29+29 resolved seed package remains missing.

3. **Model structure not yet formalized:** the AP-orbit obstruction for translation-invariant STSs, the replacement starter bound4<=u<=9, and the order87 starter bound7<=A<=12 remain Python assertions and/or hand derivations rather than Lean theorems. In particular, the AP obstruction justifies the27 orbits forced to the free bases and the chosen symmetry anchor, but that justification has not been kernel-checked in this development. The action freeness theorem does not itself prove these structural statements.

4. **Negative-control coverage:** the existing semantic rejection tests the pair-column hypothesis of `resolved_rows_sound` only. It does not test the development criterion itself. A future meaningful control could supply a concrete false variant demonstrating the necessity of transversality or free translation, but no such instance is currently formalized or claimed.

No timeout is evidence of infeasibility. All three solved flags remainfalse and full acceptance requires reviewer **done:false** while the universal goal remains unproved.

## Initial round verification, before the concrete-action extension

The exact initial sources, claims, receipts and logs are preserved in `evidence/pre-concrete-action/`. The root receipts will describe the latest final sources. This initial round is the evidence independently confirmed by the reviewer; no prior model or reference verification was rerun.

- Corrected-source `python3 verify.py --partial`: exit0; `verification-partial.json` records all11 observed permitted-axiom reports, successful kernel elaboration, and the meaningful rejection control. Its exact logs are also retained under `evidence/verification-partial-final/` before the ordinary gate recompiles the same sources.
- `python3 verify.py`: exit1, with the sole error “The universal original goal remains unsolved; partial evidence is not RLAR acceptance.” Source/Lean/control evidence passed within that full invocation. `verification-full.json` and `evidence/verify-full-command.log` preserve the actual result.
- Final negative-control log: Lean reports ordinary `decide` proved the concrete exact-one selected-row proposition **false**. It is not a syntax failure, missing instance or unrelated arithmetic assertion.
- TASK.md, ACCEPTANCE.md and verify.py hash-match the frozen baseline. The baseline commit remains `a0d6e7b38c054b3d00b76a94292675af94e540dd`; no further commit was made. Reference/helper/packing hashes are unchanged.
- The construction process exited0, with solver status UNKNOWN; a current process-table check found no remaining joint_search.py Python/uv process. Exact process receipt: `evidence/construction-process.json`.
- Full goal solved:false; target57 solved:false; target87 solved:false. The actual enclosing HMZ reviewer/journal is controlled by the owner; this actor did not launch, substitute or fabricate a reviewer verdict. Full RLAR acceptance is not met and the reviewer must return done:false for the unresolved original theorem.

## Reviewer-directed concrete action extension

The reviewer returned **not done** and confirmed the original11-theorem development, the meaningful control and the one bounded model attempt. This continuation does not rerun any solver, known-case search, packing check, model audit or literature screen. All solved flags remainfalse. It addresses the concrete action and count gap only.

`pointEncoding n` is an explicit equivalence `(Fin3 x ZMod n) ≃ Fin(3*n)`, for nonzero n. `pointEncoding_val` proves that the label is exactly `n*layer + coord.val`. `translation n g` is the coordinate permutation `(layer,coord) -> (layer,coord+g)` conjugated through that encoding. `translation_encoding` and `translation_val` prove both the coordinate description and the precise numeric formula `n*layer + ((coord.val+g.val) mod n)`. Identity and composition are proved for both points and actual unordered finite triples.

The key is the actual orbit set `translationOrbit n b = {c | exists g, translate(g,b)=c}`. `translationOrbit_invariant` proves hkey. `translationOrbit_fiber` proves hfiber by observing that c belongs to its own orbit under the zero shift; equality of orbit sets supplies the desired translate. No choice of canonical representative and no enumeration of all triples is required.

For freeness, `coordinateSum_translation` proves that summing the coordinates of the three points in ZMod n increases by exactly3*g under a shiftg. Thus equal translates by g,h give3*g=3*h. `translation_triple_free` cancels3 using `ZMod.isUnit_iff_coprime` under `Nat.Coprime 3 n`. This needs no layer case split and no prime hypothesis; coprimality suffices. It applies to19 and29 with ordinary kernel-checked `decide` proofs of those two numerical coprimality facts. These are scalar facts, not small-case design searches.

The general `development_sound` is strengthened by weakening its ownership premise to

```lean
∀ b : Triple v, ∃! i : F ⊕ A, key b ∈ ownerOrbits key fixed base i
```

Only attained labels must have owners. This resolves the codomain-surjectivity issue for the concrete orbit-set key, whose codomain contains many sets that are not orbits. Both uniqueness and global coverage use this weaker premise directly; no hidden surjectivity hypothesis is added.

`c19_development_sound` specializes the action to Fin57,17 fixed constituents and2 bases, and proves17+2*19=55 internally. `c29_development_sound` specializes to Fin87,27 fixed constituents and2 bases, proving27+2*29=85 internally. Their only hypotheses are:

- the supplied fixed constituents and bases are genuine resolved KTSs;
- fixed block sets are invariant under the concrete translations;
- each base contains at most one triple in each concrete translation orbit;
- every actual triple's orbit has exactly one input owner.

There are no action, orbit-fiber, freeness, primality or count hypotheses left in these two corollaries. Fixed chosen resolutions need not be invariant for these formal corollaries; the existing replacement search model imposes that stronger restriction. The result still does not construct any missing seed package or kernel-check the historical Python packing as a Lean certificate.

This is a new formalization of standard cyclic-action and finite-sum reasoning. It is not a new LKTS existence theorem. The formal source now has25 claimed theorems. All25 statement prints and all25 transitive axiom reports succeed in `evidence/lean-action-iteration-03.log`, using only `propext`, `Classical.choice`, `Quot.sound`. Initial elaboration errors and full output are preserved in `lean-action-iteration-01.log`; corrected iterations02 and03 succeed. The optional deprecated Set membership simp lemma was replaced by `Set.mem_ofPred_eq`.

`NegativeControl.lean` has the updated Formal.lean verbatim as its prefix, followed by the exact previously accepted broken-pair-column control. No new rejection mechanism or proof escape is introduced. `claims.json` lists all25 declarations as PARTIAL, with the strengthened ownership premise and explicit concrete corollary assumptions. The frozen checker and baseline files are untouched; no commit is made.

Current extension source hashes before final verification:

- `Formal.lean`: `a39613c93506390e52b75b4fb355d6a0d69160ea2f8a3bfe5e0ebd30ff3f2dee`
- `NegativeControl.lean`: `c84db30d282daacb457e8b4677833eb752768861a641892e84ccde7007096dbd`
- `claims.json`: `a9166d26fbd39562ca2c92b4ab6c5f8ba9289fed62d6b31eba58a9e6a303bed8`

## Final verification of the concrete-action extension

After the last Formal.lean/NegativeControl.lean/claims.json edit, each prescribed mode was run exactly once for this extension:

- `python3 verify.py --partial`: **exit0**,25 actual statement/axiom reports, positive elaboration and meaningful broken-column rejection. Root receipt `verification-partial.json`; command log `evidence/verify-partial-action-command.log`; its Lean/control logs are preserved separately in `evidence/verification-partial-action-final/`.
- `python3 verify.py`: **exit1**, with the sole error “The universal original goal remains unsolved; partial evidence is not RLAR acceptance.” The full invocation passed the source/Lean/negative-control evidence checks. Root receipt `verification-full.json`; command log `evidence/verify-full-action-command.log`; full Lean and control logs `AcceptanceAudit.verification.log`, `NegativeControl.verification.log`.
- All25 claimed theorems have only `[propext, Classical.choice, Quot.sound]` in the successful actual reports. The control fails because its concrete exact-one pair-column assertion is false. Its exact original semantic mechanism is retained.
- All three solved flags remainfalse. No additional solver, model solve, known-case search, independent reviewer, subagent, nested HMZ, commit or external message was launched in this continuation. The previous single480-second UNKNOWN remains the only released57 solver attempt.
- The enclosing reviewer's completed baseline/packing/model/reference checks were not rerun. TASK.md, ACCEPTANCE.md and verify.py were not edited. New source hashes match the latest receipts; the independently confirmed original round is archived under `evidence/pre-concrete-action/`.

The concrete action/orbit/count gap is closed. Actual seed-package certificates for57/87, and a universal construction or counterexample, remain missing. These new conditional formalizations do not change the required reviewer verdict **done:false** for the frozen full task.

## Final archival cleanup after independent review

The reviewer independently confirmed the25-theorem source, semantic control, both gate outcomes, faithful joint model and provenance. That confirmation still requires **done:false** for the original universal task. This cleanup introduces no mathematical claim and does not repeat those checks.

The stale, unreferenced root drafts were moved, without deletion or content changes:

- `action-claims.fragment` -> `evidence/drafts/action-claims.fragment`;
- `concrete-action.fragment` -> `evidence/drafts/concrete-action.fragment`.

The latter contains an earlier point-encoding proof and is historical drafting material, not an imported or claimed Lean source. `references.md` now distinguishes the live arXiv abstract-page fetches from the target's saved literature/status dossier. The exact remaining mathematical and formal gaps are recorded above under “Exact remaining step”.

Formal.lean, NegativeControl.lean and claims.json remain byte-identical to the independently confirmed versions, so their matching verification receipts are retained without rerunning Lean or either gate. TASK.md, ACCEPTANCE.md and verify.py were not edited. No solver, search, known-case replay, process launch for review, subagent or commit was performed. `evidence/artifact-sha256.json` was regenerated after the moves and these documentation edits.
