# Four-qubit depolarizing majorization: verified partial indices

## Result and scope

For the replacement-noise channel `D_p(X)=(1-p)X+(p/2)tr(X)I`, every four-qubit density operator `rho` satisfies the following **partial** Ky Fan inequalities relative to the pure-product output. `K_k` denotes the sum of the `k` largest eigenvalues.

| Physical replacement-noise range | Verified indices k |
|---|---|
| `0 <= p <= 4/3` | `1, 5, 11, 12, 13, 14, 15` |
| `2/3 <= p <= 4/3` | Additionally `2, 3, 4` |

This does **not** establish full majorization. At the decisive `p=1/2`, indices `2–4` and `6–10` remain unresolved. At `p=0` and `p=1`, the full statement is elementary. This `p` is not the total Pauli error used by the capacity lane.

**FRONTIER:** PROOF-OBLIGATION for the full target; NOVELTY-UNCLEAR for the partial increment. The subsequent exact Pauli–Gram/SOS attempt closed no missing index. That bounded route is stopped while the physics slot is screened for a materially different target.

## Proof bridge checked by the parent

The frozen [proof](n4-partial-parent-inputs-v1/PROOF.md) and [corrective addendum](n4-partial-parent-inputs-v1/ADDENDUM_v1_1.md) give these steps, read directly by the parent:

1. Expand the channel into `X_s = sum_{|I|=s} rho_I tensor I_(I^c)` with nonnegative coefficients `(1-p)^s p^(4-s) 2^(s-4)` on `[0,1]`. The product targets `T_s` share a Hamming-weight eigenvalue ordering. Ky Fan subadditivity therefore adds the per-family bounds without a target-order loss.
2. `U_2(k)` means `K_k(X_2)<=K_k(T_2)` for every global state. The exact PPT relaxation below establishes it for `k=1..5,11..15`. The three-body family has elementary bounds at `k=1` and `k>=5`; the one-body family is a Kronecker sum. This yields the first row of the table.
3. Global spin flip removes `X_3` at the cost of subtracting a positive operator. The remaining one-body coefficient is `p(1-p)(2-p)(3p-2)/8`, nonnegative on `[2/3,1]`. The correction changes only a smallest product-target eigenvalue, leaving the top fifteen sums unchanged. This proves the additional indices on that interval.
4. Global transpose followed by conjugation with `sigma_y` on every qubit makes the outputs at `p` and `2-p` isospectral. It extends the stated ranges above `p=1`. No assertion that a partial transpose is positive is used.

## Independent exact parent check

[Checker](check_n4_partial_independent.py), [receipt](n4-partial-parent-check.json), [pinned inputs](n4-partial-parent-inputs-v1/parent-manifest.json). The run exited 0 at the time recorded in the receipt. It imports no worker code.

- Derived the one-site partial-transpose eigenspaces and partial traces from exact `4x4` Bell/complement projectors. Tensor products reconstruct the sixteen-variable LP coefficients, rather than importing the worker's closed-form coefficient code.
- Checked all ten frozen rational dual points: multiplier dimensions, signs, **160 column inequalities**, and objectives equal to the independently calculated product-target sums.
- Checked product-input feasible points for every projector rank `k=1..16`, including their `U_2` and `U_3` objectives.
- Every target lowered by `1/1000` is rejected. Decreasing the free trace multiplier by one is rejected specifically by a dual column inequality.
- Checked all eight rational primal relaxation-gap witnesses: coefficient bounds, trace, marginal bound, PPT inequalities and strict objective excess.

The certificate also has a compact analytic explanation. In the twirled variables, `c_full` is the coefficient of the all-Bell projector and `e_tau(c)` a PPT-sector eigenvalue. The exact identity is

`objective_U2(c) = 3 k + 48 c_full - 72 sum_{tau with exactly two antisymmetric sites} e_tau(c)`.

The parent verified every coefficient of this identity. Since `c_full<=1/16` and every `e_tau(c)>=0`, the relaxation gives `U_2`'s upper bound `min(3k+3,24)`. The frozen certificates therefore do not depend on trusting an LP solver's success status.

## Review, limits and next obligation

The historical cross-vendor Codex review returned **ACCEPT-WITH-FIXES** ([record](n4-partial-parent-inputs-v1/codex-frozen-partial-review.json)); its three low-severity findings are addressed by the pinned addendum. It independently reconstructed the matrices, checked the dual points and audited the analytic bridge. It was commissioned under the preceding Claude parent; its provenance is unchanged.

The positive relaxation-gap witnesses prove that plain PPT cannot certify the missing `U_2(6..10)` and `U_3(2..4)` inequalities. They are **not physical-channel counterexamples**. Level-2 numerical relaxations still leave positive gaps and certify no additional index. No general `n=4` solution, Lean verification, literature-wide priority or human peer review is claimed.

Relative to the stated baseline, `k=1` is already implied by King's norm result and `k=11..15` are elementary. The increment is `k=5` for all physical `p` and `k=2..4` for `p>=2/3`; its priority remains unresolved. The separate [Amosov applicability audit](three-qubit-majorization-parent-verdict.md#amosov-prior-work-applicability-check) must not be treated as a proof or disproof of the target.

Reproduction, from the aifours root, with a fresh output filename:

```sh
python3 -B institute/runs/six-lane-2026-10-16/review/check_n4_partial_independent.py institute/runs/six-lane-2026-10-16/review/n4-partial-parent-inputs-v1 <fresh-output.json>
```
