# C19 pair-first completion of the checked 17-packing

Date: 2026-10-14 (PT). Implementation: `work/c19_staged_completion.py`. This continuation preserves the previous C19 scripts, receipts and witnesses unchanged.

## Frozen input and exact first model

Input: `evidence/c19-17-staged.frozen-packing.json`, SHA256 `6515e4041991d0c857df9c5d5752613f8d958d4ee76296cbbc24c024b807d714`. Its 17 invariant resolved KTS(57)s occupy 476 of the 1,540 translation orbits of triples. Every runner independently expands and checks those constituents before searching.

For each of the remaining 1,064 triple-orbits, each of its 19 blocks, and each of two free bases, introduce one Boolean placement variable: **40,432 primary variables**. Exact-one constraints cover:

- every remaining triple-orbit, over both bases together (1,064 columns);
- every concrete pair separately in each base (2·1,596 columns).

There are **4,256 exact-cover columns, each with 38 candidate placements**. Consequently a satisfying assignment consists of two STS(57)s, each with 532 blocks, each transverse to triple-orbits; together they use every remaining orbit once. The 38 translated systems are block-disjoint from each other and the fixed packing. Resolvability is deliberately deferred, not assumed.

The native CNF uses the existing `search_staged.CNF` Sinz sequential encoding, rather than a second encoding convention. Before candidate blocking, the expected dimensions including the symmetry unit below are 197,904 total variables and 472,417 clauses. Every attempt saves its complete immutable CNF or model text, hash, manifest, configuration, log and previously blocked candidate witnesses.

### Preregistered modular CP-SAT encoding

Before launching any long run, the CP-SAT configuration was changed to the following equivalent encoding, supplied by the parent investigator. Each remaining orbit o has a color `c_o∈{0,1}` and shift `s_o∈{0,…,18}`: 2,128 primary decision variables, with auxiliary variables for modular expressions. Each of its three pair incidences is retained separately. If its canonical pair-orbit representative translates by t to that pair, its selected concrete pair has label `y=19c_o+((s_o+t) mod19)`.

For each of the 84 pair-orbits, **AllDifferent** on its 38 incidence labels in `{0,…,37}` forces every concrete pair once in each base. In particular, two incidences of an AP triple in the same pair-orbit must not be deduplicated: their offsets differ. The implementation checks the offset dictionary against all 19 translated blocks of every remaining triple-orbit, then asserts exactly 38 incidences in every pair-orbit.

This model is equivalent to the Boolean exact cover: an orbit's color and shift specify its unique placement; conversely every Boolean solution selects exactly those decisions. Complete pair coverage forces each base to have 532 blocks. The same anchor is imposed as `c_0=s_0=0`. No other base ordering is imposed. The native solvers retain their 40,432-primary-variable CNF. The Boolean CP encoding remains explicitly selectable with `--cp-encoding boolean`, but is not the preregistered long CP run.

## Lossless symmetry normalization

Let O be the least remaining triple-orbit. Exactly one free base contains its chosen block. Interchanging the two bases places that block in base 0. Independently translating base 0 under C19 then makes that block O's canonical representative. This preserves its STS property, its resolvability status and its selected triple-orbits. It cannot introduce shared blocks with base 1 or the fixed constituents, since their orbit sets are disjoint and the fixed block sets are invariant.

Thus the first primary variable, `(O,shift=0,base=0)`, is set true. This removes 38 equivalent choices without restricting existence for the frozen complement. **No additional ordering of the third points of the two {0,1} blocks is imposed**: base interchange has already been used. Base 1 is not independently translation-normalized in this implementation.

## Positive checks and unrestricted resolutions

Every SAT pair cover is checked by concrete pair counters and by the independent full-19-element orbit canonicalization from `c19_verify.py`. These checks do not trust the solver's auxiliary assignment. Both STSs must have exactly 532 distinct blocks, every pair once, and together exactly the remaining 1,064 triple-orbits.

For each checked STS, its 28 blocks through point 0 label its 28 resolution classes. This loses no resolution: each class contains exactly one such block. For every other block, variables allow every class whose anchor is point-disjoint. Exact-one constraints assign each block once and cover every point once in every class. This is an unrestricted resolution search for the fixed STS, with only class-permutation symmetry removed. It has 12,628 placement variables: 28 anchors plus 504 non-anchor blocks, each compatible with 25 classes.

If both resolutions are found, all 17+19+19 systems are expanded in the existing plain certificate format and passed to `work/check_lkts.py`. Only checker PASS creates the portfolio's shared verified-target stop file. Every runner watches that file and its own wall deadline, requesting cancellation of active CP-SAT/native search promptly. Current lifecycle code starts a 30-second SIGTERM grace period when cancellation occurs. A responsive native child is reaped before its handle is cleared. An unresponsive child is not force-killed without approval: its PID and incomplete cleanup are retained and reported.

## Bounds, blocking and interpretation

The native Kissat and CaDiCaL runners use one worker each. The CP-SAT runner uses two. Resolution stages replace rather than overlap a runner's pair-cover solve, so configured solver concurrency is at most **four**. Every runner has a **7,200-second overall wall deadline**, a 7,200-second maximum pair-cover call, and a 300-second maximum call per STS resolution; every call is limited by remaining overall time.

A candidate with an INFEASIBLE resolution is excluded by a clause negating its selected primary variables. The status is solver-reported; no independently checked negative proof trace is claimed. A candidate whose resolution returns UNKNOWN may also be excluded to diversify the search, but that exclusion is explicitly recorded as **heuristic**, with its witness retained. Any later exhaustive negative answer after such exclusions is not a nonexistence result. An UNKNOWN pair-cover solve does not itself block any assignment.

Even a negative first-model result pertains only to this frozen 17-packing, not every C19-invariant LKTS(57), and never to unrestricted LKTS(57).

## Commands and exact replay

Run from the target directory with OR-Tools 9.15.6755. Use new prefixes for replays; existing prefixes are refused.

```sh
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python work/c19_staged_completion.py search --packing evidence/c19-17-staged.frozen-packing.json --solver kissat --config sat --seed 1917201 --threads 1 --seconds 7200 --stop-file evidence/c19-paircover-verified.json --output evidence/c19-paircover-kissat
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python work/c19_staged_completion.py search --packing evidence/c19-17-staged.frozen-packing.json --solver cadical --config sat --seed 1917202 --threads 1 --seconds 7200 --stop-file evidence/c19-paircover-verified.json --output evidence/c19-paircover-cadical
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python work/c19_staged_completion.py search --packing evidence/c19-17-staged.frozen-packing.json --solver cpsat --cp-encoding modular --seed 1917203 --threads 2 --seconds 7200 --stop-file evidence/c19-paircover-verified.json --output evidence/c19-paircover-cpsat
```

For an individual saved attempt:

```sh
UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --offline --with ortools==9.15.6755 python work/c19_staged_completion.py replay evidence/c19-paircover-kissat-data/paircover-0000.manifest.json --output /tmp/c19-paircover-replayed.cnf
```

Replay revalidates the frozen packing, regenerates rows and columns, independently validates every previously blocked candidate, reconstructs the exact model and requires equality with the original instance SHA256. Every search snapshots this script and its imported local helpers alongside the packing and encoding. **Replay PASS authenticates reconstructed model bytes, not historical source identity:** it uses the current generator and neither authenticates the manifest's `source_hashes` nor loads the frozen sources. This permits an unrelated lifecycle-only source change without falsely rejecting a byte-identical mathematical model.

## Preliminary resolution diagnostic

An unhinted 60-second, one-worker resolution search on the first **known** fixed KTS, after forgetting its known resolution, returned UNKNOWN (60.0016 solver seconds; 12,346,650 branches). The diagnostic driver expected a positive result and therefore exited with an assertion error. This is recorded as an unresolved search, not an infeasibility result or an identified model error. The exact model, log, original source snapshot and parameters are retained in `evidence/c19-paircover-resolution-validation*`. It also warns that the deferred resolution stage may remain substantial even when a resolution is known to exist.

Without rerunning that search, the known resolution was subsequently assigned to the saved model's actual 12,628 variables. All 2,128 exact-one constraints were evaluated directly and passed; 532 variables were selected. Evidence: `c19-paircover-resolution-validation.witness-check.json`. Thus the retained instance is concretely satisfiable despite the diagnostic's UNKNOWN.

## Focused review and lifecycle correction

The focused independent review in `evidence/completion-review.md` found no mathematical encoding error. It independently checked the positive 17-packing, native model dimensions, lossless normalization, all 20,216 modular translations including AP duplicate incidences, and all 17 known resolutions against the resolution constructor.

Its operational finding was accepted without rerunning the defective behavior: early cancellation sent SIGTERM promptly but could wait nearly the original full solver cap before escalating. Current code starts grace at the first cancellation timestamp, checks the child in bounded waits, sends no SIGKILL, retains an unresponsive process handle/PID, and never reports zero remaining children when a tracked child is still alive.

`evidence/c19-paircover-lifecycle-unit.py` exercises the corrected control flow using only a virtual clock and fake child. The six cases passed: normal exit, early responsive stop, early unresponsive stop, caller retention of an unresponsive handle, caller clearing of a reaped handle, and cancellation before spawn. Cancellation at simulated t=5 now returns an unresponsive-child report at t=35, not at the original 7,200-second deadline. No real child, solver, or SIGKILL was used. Receipt: `evidence/c19-paircover-lifecycle-unit.json`.

Current source SHA256 is `1f4f0d55ff73c754fba91e8606928c1185eaf8656fe7338212e1b4264b9a4525`; the three already-running searches retain source snapshot `40e8e7b19bc7317fc473f380a9f000b7e8d7fdbac48b66e8f88962139462360f`. The mathematical models were not changed or restarted for this lifecycle correction. Their final receipts must be consulted for actual child exit and cleanup; the fake-child regression is not real-process shutdown evidence.


## Actual 7,200-second continuation results

All three preregistered runs completed. **No SAT pair cover was found**, so neither long-run candidate resolution nor full-certificate checking was reached. No candidate was blocked, heuristically or otherwise.

| Runner | Encoding | Total wall seconds | Pair-cover solver seconds | Status |
|---|---|---:|---:|---|
| Kissat 4.0.4, seed 1917201, one worker | 40,432 primary / 197,904 total CNF variables; 472,417 clauses | 7200.191 | 7199.765 | UNKNOWN |
| CaDiCaL 3.0.1, seed 1917202, one worker | Same native CNF | 7200.156 | 7199.734 | UNKNOWN |
| CP-SAT 9.15.6755, seed 1917203, two workers | 2,128 color/shift decisions; 6,400 variables including auxiliaries; 4,358 constraints | 7200.017 | 7199.683 | UNKNOWN |

Receipts are `evidence/c19-paircover-{kissat,cadical,cpsat}.json`; corresponding `-data/` directories retain exact source snapshots, packing, encoding, model, manifest and solver log. Native solvers searched model SHA256 `48a6d93b38737eb9567bdab4a2394da1e8f598452d5f8af8f2d5b5b10d607320`. The modular CP model SHA256 is `707da826500842fd3ea653f3fa98d4811d8803235bd231c822efbcebce2b0915`.

The CP run exercised 124,411,357 branches and 2,811,766 conflicts. Both native children were stopped at their wall deadlines by SIGTERM, returned `-15`, and were reaped normally; both recorded `forced_termination=false`. Thus the historical lifecycle escalation branch was not exercised. All three runners exited with zero remaining children. There is no owned solver process left running.

The conservative sum of each runner's recorded self and child peak RSS is **5,374,181,376 bytes**, below 12 GB. Configured solver concurrency was four workers; the three two-hour intervals overlapped and must not be reported as six elapsed hours.

Exact initial-model replay passed before the lifecycle correction (`c19-paircover-model-replay.json`) and again with corrected code against the historical manifests (`c19-paircover-postfix-replay.json`). Both native and modular hashes remained identical. These are model-byte and mathematical-input checks, not proof-trace certification or authentication of historical source hashes.

The earlier proposed pair-first reduction has therefore now been **implemented and exercised**, rather than left as a plan. It did not settle even this frozen packing's pair-cover problem. No global C19 exclusion, frozen-packing infeasibility, or LKTS(57) certificate follows from the three UNKNOWN results.

