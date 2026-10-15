# Focused continuation review resolution

Date: 2026-10-14 (America/Los_Angeles).

## Completed review

`round2-review.md` returned **READY**. The completed CLI run exited 0; `round2-review-run.json` records the command, input digests and execution interval. Runtime headers in `round2-review.stderr.log` confirm **gpt-6.1-sol**, reasoning effort **max**, and **read-only** sandbox. The prompt restricted reads to this target and prohibited code/test execution, web access, changes and further delegation. This was an independent static review, not a second execution of the numerical checks.

The referee accepted:

- Exact equality at A_one degree (4,4,5), with free dimension 6930, Serre ideal rank 6880, both quotient dimensions 50, and descent rank 50. The first-defect inequalities extend the previously accepted height-12 result through **height 13**.
- The inverse-nonnegative deletion/band theorem and its A_one consequence at every height: **alpha_1<=3 OR alpha_2<=3 OR alpha_3<=4**.
- The purely algebraic coefficient-two theorem for the displayed A(r,s) family, for every positive integer r,s, and the higher-level detection criterion conditional on equality at the preceding level.
- Uniform rank-three equality through **height 7**, covering all 144 parameter cells at degree (3,2,2); only the explicitly certified height-8 subset, namely 211/256 cells at (4,2,2) and 235/324 at (3,3,2).
- The content-stripped determinant verification, including the 160300-term polynomial and its positive constant 512745678002234327040. Intermediate pivots need not remain nonzero at specialization: the independently checked final identity is a polynomial identity.

## Sole finding and its resolution

The reviewer found one **low-severity reporting-label issue**, not an arithmetic error: `work/round2_target_degree.py` used the JSON key `parent_modular_ranks` even for the exact-Q run.

The producer now emits **`parent_ideal_ranks`**, with the arithmetic field still recorded separately. This is a one-line reporting-only change; no arithmetic, certificate, checker or proof changed. No code caller in `work/` consumed the old key.

The original observed outputs are intentionally unchanged. Their historical `parent_modular_ranks` field denotes the ranks in their declared field, so in the Q report it means exact rational parent-ideal ranks. Before the rename, the exact executed producer was preserved as `evidence/round2_target_degree-as-run.py`; its digest is the original producer digest **119ca9512ed018906d22cc904afbdb3e2abf1f344fd1e775c284521e9ee56745**. The current final receipt binds both versions. The updated reporting-only producer was **not rerun**; the unchanged independent checker and unchanged certificates retain the exercised acceptance evidence.

## Trust boundary and unsolved scope

The new degree checker composes with the previously accepted, externally hash-pinned height-12 certificate. It reconstructs the new degree independently but does **not** recertify the entire baseline. The baseline's recorded acceptance digest binds an artifact; it is not, by itself, authentication of a past execution. The earlier observed checker run remains an explicit premise of the composed result.

Uniform height 7 similarly composes with the earlier accepted height-6 theorem and the written coefficient-one/descent/Serre/sl2 reductions. Height-8 cell counts are **per fixed degree**; they do not assert that a common family of matrices is completely settled through height 8. Failed, timed-out and unattempted cells remain gaps. The finite-field run is screening only.

The full universal characteristic-zero conjecture, all-degree equality for A_one, uniform height 8, and general higher-level injectivity are **NOT SOLVED**. No counterexample was found. Novelty is not certified. There was no Lean/kernel verification. All owned computation and review processes have finished or were explicitly stopped; no background computation remains.
