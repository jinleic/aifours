# AMENDMENT-4 parent header correction and driver hold

Recorded 2026-10-18T02:43:24-07:00. This addendum corrects the [parent disposition](moqls7-amendment4-parent-disposition-v1.md), original SHA `3c9373c0ca7a8a98d9af3b2288b04076cad421e65ce645638ab151b850694e44`, without changing it.

## Header correction

The disposition's decision5 and the earlier desk summary mislabeled **strengthened** clause counts as input counts. Parent read the first line of each actual pinned input:

| Formula | Variables | Input clauses | After238140 cuts |
|---|---:|---:|---:|
| A original C311 |96978|627556|865696|
| A lex C311 |107513|659168|897308|
| B original C311 |461370|1629802|1867942|

The worker r1 appender/delta uses the correct input and output counts. It must not be changed to the mistaken parent input counts. Hashes remain the source of truth.

## Source-review HOLD, not a launch GO

Parent inspected the complete selected portions of `code/k3_cuts_certify_r1.py` (SHA `0e978302559f73b115ca2b7df4e67c5e99731a53c43c64e706ffb438a3d70b5a`) and related declarations. Concrete blockers sent to the worker:
1. Lines388–390 use text universal-newline conversion, CR→LF and strip(); exact output acceptance must instead read bytes, remove only CR and compare the untrimmed status line. Record the solver line as well. Whitespace mutation controls are required.
2. Encoder-B generation at247–249 uses unguarded subprocess.run before native supervision, and generator r2 has the same child pattern. A in-process preparation is also outside the watcher. Whole-stage generation/preparation needs bounded RSS/time/floor/owned-child supervision before production.
3. There is no parent SIGTERM handler for solver/checker children. Inherited stop_children raises after30s on survivors; capacity cannot be released to another pipeline while an owned child survives. Hold/quarantine and report rather than orphaning or using SIGKILL.
4. Main's exist_ok=True output-directory creation is not the run's exclusive-directory discipline. Preserve old attempts, use exclusively created route outputs. Draft retirement is unnecessary; preserve the originals.

Proposed3600s solver/7200s checker/7320s wall limits are approved in principle, not execution. A new corrected version, source review and passing pre-solve controls remain prerequisites. The two reviewed mathematical families and A+B scientific standard are unchanged. These are source findings, not observations of failed production or evidence of any cap excursion.
