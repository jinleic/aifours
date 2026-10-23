# Depolarizing capacity candidate: parent verification state

**Status: CANDIDATE.** An explicit 2000-qubit rank-two symmetric input is reported to have rigorously enclosed coherent information

`1.1288547919e-8 <= I_c(rho*, N_(1/5)^(tensor 2000)) <= 1.1436444146e-8` **bits**,

for `N_p(rho)=(1-p)rho+(p/3)(X rho X+Y rho Y+Z rho Z)`. If the certificate gate closes, monotonicity and LSD give `Q(N_p) > 0` for every `0 <= p <= 1/5`. Total-error convention: the matched rigorous prior point is `0.194868`.

It is **not yet accepted as a certified theorem.** Remaining blockers are a provenance-bound final certificate run under the revised code, explicit rejection controls for record mutations in the combining step, and an exposition revision incorporating the reviewer fixes. A reproduction, model review and a search miss are not human peer review or priority certification.

## Independent evidence

| Gate | Result | Artifact |
|---|---|---|
| Exact sector/channel bridge | Independent Claude Opus 5.5 maximum-effort proof review: **ACCEPT-WITH-FIXES**, no mathematical error. Required fixes: normalize the kept and flag blocks by `1-epsilon`, explicitly retain off-diagonal reference blocks, state the exact flag identity, residue/support condition, intertwiner/cloning details and AFW hypotheses. | `depolarizing-sector-bridge-review.note.md`, receipt alongside |
| Independent numerical reproduction | A separate singlet-embedding, nonnegative-kernel float64 implementation, built before reading worker code, gives `1.14134071e-8` bits at `p=1/5`: inside the claimed interval. All 220 per-sector values fall inside the worker's per-sector intervals. Same-state controls at `p=201/1000` and `p=1/4` are negative. Small-M brute-force agreement covers 216 cases. | `depolarizing-parent-reproduction/README.md`, `evidence/SUMMARY.json` |
| Primitive arithmetic spot audit | 15,000 exact-Fraction checks of double-double primitive operations stay inside allowed error. | `depolarizing-dd-parent-check.json` |
| Worker hostile review | Codex `gpt-6.1-sol` maximum effort: ACCEPT-WITH-FIXES, no fatal issue; text fixes recorded in `PROOFS_v2.md`. | `physics/evidence/six-lane-20261016/depolarizing/review/` |

The float reproduction cannot certify the sign: binary64 rounding is not enclosed. Its value matters as an independent implementation that would expose many modelling and indexing errors. The empirical error estimate is below `5e-14` bits; the closest interval endpoint is more than 460 times farther away.

## Provenance and limits

- The `TOTAL.json` witness hash is canonical JSON, not raw file bytes. The raw witness file SHA-256 is `4ced4ed9...`; both identities must be recorded separately.
- The combine step used a sector-tail cutoff near `1e-13`, not its code default `1e-30`. Omitted mass is bounded rigorously, but the setting must be recorded in the final certificate.
- The current combining program trusts producer sector records. Record-integrity gates and mutations must reject changed witness or code hashes, wrong `M,p,D`, duplicates, omitted sectors without an explicit omitted-mass bound, inverted intervals and altered contributions.
- Matched prior work: rigorous `0.194868` (Krohn-Grimberghe, arXiv:2608.15870v2); higher asymptotic Gaussian-limit claim `0.2029161` without a finite witness (Ahmed et al., arXiv:2609.39747v2). The present value exceeds the first only if certified and remains below the second.
- No commit, publication, external contact or novelty claim.
