# HMZ, Lean and local math continuation

Date: **2026-10-14 PT**. **The universal book problem is not solved. LKTS(57) and LKTS(87) are also not constructed.** This package preserves a real frozen HMZ attempt, useful kernel-checked conditional mathematics, one genuinely new construction search, and their explicit limits.

## What was proved and what was not

`Formal.lean` has faithful finite definitions of triples, pairs, STS, parallel class, resolution, KTS and LKTS. `Kirkman.FullGoal` is exactly existence of LKTS(6t+3) for every integer t>=1, with no symmetry restriction. It is **defined, not proved**.

The25 claimed theorems, their plain-English statements, complete hypotheses, actual axioms and contribution classification are in [`claims.json`](claims.json). The principal results are:

| Lean theorem | Actual conclusion | Remaining input |
|---|---|---|
| `Kirkman.resolved_rows_sound` | Exact-one pair columns and exact-one(class,point) columns produce a genuine resolved STS, including uniqueness and disjoint classes | Actual selected rows satisfying those columns |
| `Kirkman.development_sound` | Mixed invariant fixed constituents and translated free bases form a block-disjoint exact cover of all triples with the required number of resolved systems | Resolved seeds, fixed-set invariance, free-base transversality, orbit ownership and the explicit generic action conditions |
| `Kirkman.translation_triple_free` | Translation on three n-point layers acts freely on genuine triples when gcd(3,n)=1 | No design existence input; nonzero n and coprimality |
| `Kirkman.c19_development_sound` | The17+19+19 construction on Fin57 is sound | The actual compatible17 fixed KTSs and two resolved transversal bases |
| `Kirkman.c29_development_sound` | The27+29+29 construction on Fin87 is sound | The actual compatible27 fixed KTSs and two resolved transversal bases |

The concrete corollaries prove their own translation laws, orbit-fiber completeness, freeness and constituent counts. They do not assume a developed LKTS as a hypothesis. Freeness follows by summing the coordinates of the three actual points: translation adds3g, and the invertibility of3 implies equal translates have equal shifts. No seed package is supplied. The contributions are **new formalizations of standard exact-cover and development reasoning**, not claimed new existence mathematics.

**Still outside the kernel:** the actual16 retained KTSs, the replacement's orbit-level starter/ABC encoding, its AAA bound and AP obstruction, and the concrete57/87 seed packages. `resolved_rows_sound` covers concrete pair/class rows; it is not a proof of the replacement's different quotient encoding. The negative control exercises a pair column, not every hypothesis of the development theorem.

## Actual released-system16 attempt

The original17-packing is preserved. The new model retains zero-based systems0–15 and jointly models an invariant resolved replacement plus two free STS pair covers over **1,092 triple-orbits**. No new replacement was greedily solved and frozen first. Its replacement AAA count ranges over every admissible value4–9.

- **61,948 Boolean variables**, **4,425 exact-one columns**, plus two linear constraints.
- Orbit allocation, if solved:28 replacement orbits plus532 orbits in each free base.
- One CP-SAT9.15.6755 call, seed19161014, **two workers**,480-second pair-cover cap within600-second total limit.
- Observed solver time **480.009102s**, total480.775230s;5,365,856 branches and626,858 conflicts.
- **UNKNOWN, no candidate.** Resolution and full-certificate checks were not reached. No candidate was blocked. No infeasibility proof or proof trace exists.
- A pre-solver pybind negative-index crash is separately retained, not counted as another solve. It was corrected using a nonnegative constraint index.

Exact sources, model, rows, input snapshots and hashes: [`evidence/joint57/`](evidence/joint57/). The solver-free complete row/column audit passed: [`evidence/joint-model-audit.json`](evidence/joint-model-audit.json). Mathematical encoding and the conditional87 analysis: [`progress.md`](progress.md). The completed historical portfolio and known-case searches were not rerun.

At87 the27-fixed-plus-two-free C29 pattern has compatible aggregate counts; no27-packing or two free bases were constructed and no87 solver run is claimed.

## Actual HMZ provenance and verdict

| Item | Observed value |
|---|---|
| Frozen scratch repository | `scratch/ai4s-math-hmz-20261014/kirkman/` |
| Baseline commit | `a0d6e7b38c054b3d00b76a94292675af94e540dd` |
| Runtime revision | `3d3e21b0da89ef5f6247cd7b3f88ad178fbac94a` |
| Official flowverse revision | `2c37d06df3e356807adb93b5a9fdca170a5d0be8` |
| Worker / reviewer | `codex/gpt-6.1-sol:max` / `claude/claude-opus-5-5:max`, unchanged shared pairing |
| Wrapper limit / measured wall |3600s /3600.377910s |
| Process result |143, watchdog SIGTERM |
| Structured completed reviews |Three, all **done:false**; fourth review interrupted |
| Terminal epic / resume |`ended how:"stopped"` / `ok:false` |
| Frozen TASK/checker/acceptance |All three hashes unchanged |
| RLAR acceptance |**No** |

The final completed review independently compiled the25-theorem source, inspected its statements and axioms, checked the semantic broken-column rejection, and accepted the model/provenance while correctly rejecting full completion. The actual verdict is in [`hmz/reviewer-verdicts.json`](hmz/reviewer-verdicts.json), extracted with source line numbers from the preserved wrapper log; it is not an invented summary verdict. [`hmz/terminal-summary.json`](hmz/terminal-summary.json) records no remaining command-line-path-matching process after termination and states the limitation of that process inspection.

Raw evidence: [`hmz/process.json`](hmz/process.json), [`hmz/wrapper.log`](hmz/wrapper.log), [`hmz/20261014T192203.406Z-02528d-epic.jsonl`](hmz/20261014T192203.406Z-02528d-epic.jsonl), [`hmz/20261014T192203.406Z-02528d-resume.jsonl`](hmz/20261014T192203.406Z-02528d-resume.jsonl). Full-access HMZ on this Mac is **not an OS sandbox**. There was no nested HMZ or separate reviewer invocation.

## Lean evidence and rejection control

Runtime: Lean4.34.1 with the existing cached Mathlib project at `scratch/rh-quasi-lean-2026-10-07/lean`, used read-only. Nine explicit Mathlib imports, no OAI imports or corpus rebuilds. All25 actual `#print`/`#print axioms` reports list only **propext, Classical.choice, Quot.sound**.

- Corrected final `python3 verify.py --partial`: **exit0**; [`verification-partial.json`](verification-partial.json).
- Full frozen `python3 verify.py`: **exit1**, solely because the original universal goal remains unproved; [`verification-full.json`](verification-full.json). This is the intended honest full-goal gate, not a Lean failure.
- `NegativeControl.lean` contains the positive source verbatim followed by two selected triples{0,1,2} and{0,1,3} on Fin9. Both cover pair{0,1}; Lean rejects the claimed unique selected row because ordinary `decide` evaluates the proposition to **false**. See [`NegativeControl.verification.log`](NegativeControl.verification.log), not merely its nonzero exit.
- An earlier control failed for missing decidability, so its initial mechanical PASS was explicitly rejected and archived under `evidence/verification-pre-control-fix/`. It is not used as acceptance evidence.
- Actor snapshots/logs and their original absolute paths are retained unchanged. Root `progress.md`, `references.md` and the frozen task describe that original scratch run. No Comparator, nanoda or adversarial-sandbox acceptance is claimed.

## Independent supplementary observation

[`linear-relaxation.md`](linear-relaxation.md) proves a written uniform fractional-feasibility lemma: with k fixed systems and v-2-k=rp, assign weight1/(rp) to every unnormalized free pair placement, or1/(rp(v-1)/2) to every unnormalized resolved placement. Actual pair/point incidence counts make every constraint sum exactly1. For the checked57 complement the weights are1/38 and1/1,064.

[`check_fractional.py`](check_fractional.py) evaluates this finite witness with exact rational arithmetic, checks the original packing and released-system split using the existing independent verifier, and rejects denominator37. Its receipt is [`fractional-receipt.json`](fractional-receipt.json). This is **not Lean-certified**, not a new novelty claim, not an integral construction, and not a statement that the symmetry-pruned solver polytope is feasible. It explains why the unnormalized basic continuous relaxation alone cannot certify impossibility.

## Reproduction without restarting search

From this directory:

```sh
sh reproduce.sh lean
sh reproduce.sh partial
sh reproduce.sh full    # expected exit1 while the universal goal is unsolved
sh reproduce.sh audit-joint
python3 check_fractional.py --output /tmp/kirkman-fractional-new.json
```

`lean` is exactly `/Users/jinleic/.elan/bin/lake env lean /ABS/PATH/TO/Formal.lean` from the cached-runtime directory. `partial` and `full` regenerate local audit logs; original final actor logs remain under `evidence/verification-partial-action-final/`. The fractional checker refuses to overwrite an existing receipt. Search is intentionally excluded from the reproduction wrapper; `joint_search.py` also refuses to overwrite the saved attempt. The source/hash integration receipt binds copied artifacts and the final supplementary check without pretending that a byte-identical copy is a new mathematical verification.

## Remaining mathematical obstruction

The57 route still needs one replacement invariant resolved KTS and **two integral orbit-transversal STS bases with genuine resolutions**, disjoint from the16 retained systems and jointly covering all1,092 remaining orbits. The87 route needs its entire27+29+29 seed package. A full solution needs a construction or proof/counterexample for **all** t>=1, not just those cases. None of these objects follows from the conditional Lean theorems, the compatible aggregate counts, the fractional witness, or the bounded UNKNOWN result.
