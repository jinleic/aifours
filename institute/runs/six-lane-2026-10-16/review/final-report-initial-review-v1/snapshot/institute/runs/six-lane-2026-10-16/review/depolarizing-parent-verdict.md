# Depolarizing capacity: parent verdict

## Status: CERTIFIED (computer-assisted, stated trust base)

For `N_p(rho)=(1-p)rho+(p/3)(X rho X+Y rho Y+Z rho Z)` and the hash-bound 2000-qubit input `rho*` (rank two, real, mod-3 Dicke comb on `Sym^2000`), the provenance-bound v3 run gives

`1.1373755593447965e-8 <= I_c(rho*, N_(1/5)^(tensor 2000)) <= 1.1432769065159199e-8` **bits**.

By monotonicity of the depolarizing family under composition (data processing) and LSD, `Q(N_p) >= 5.68e-12` per channel use for **every** `0 <= p <= 1/5`. The same state certifies **negative** coherent information at `p=201/1000`; this says nothing about `Q` there.

Trust base: IEEE-754 binary64 round-to-nearest without FMA contraction in the numpy build, FLINT/Arb and python-flint, and the cited theorems (Schur–Weyl, LSD, data processing, Araki–Lieb, Winter's continuity lemma, Ostrowski, Gershgorin, Ky Fan). The proof is computer-assisted with one rigorous implementation; there is no second interval implementation, no formal verification and no human peer review.

## Evidence

| Gate | Result | Artifact |
|---|---|---|
| Provenance-bound certificate run (v3) | Witness raw SHA `4ced4ed9…`, canonical-JSON SHA `43117f99…`, cert.py `81d50d97…`, dd.py `cbfb39f4…` bound into every one of 220 sector records; `ptail=1e-13`, `pitail=1e-40`, `D=440`; classification POS | `physics/evidence/six-lane-20261016/depolarizing/evidence/cert/v3/` (`p1_5_TOTAL.json`, `PROVENANCE.json`) |
| Replay | All 220 sectors recomputed one at a time reproduce every record field (worker replay with the same code; reproducibility, not independence) | `p1_5_full_replay_SUMMARY.json` |
| Combine-step controls | 17/17 mutations give the intended named outcome (altered amplitude, wrong code hashes, wrong `M/p/D/ptail`, duplicates, omissions, inverted/NaN intervals, unselected sector); consistent shifts caught by replay | `mutation_tests.json` |
| Cross-vendor hostile review of the revised proof and the certified code | Claude Opus 5.5 (max): **ACCEPT-WITH-FIXES**, no fatal error. Major M1 (witness premises unchecked) discharged by the parent; minor items are an upper-endpoint-only rounding margin, documentation and tooling | [`depolarizing-v3-hostile-review.note.md`](depolarizing-v3-hostile-review.note.md), [dispositions](depolarizing-v3-review-dispositions.json) |
| M1 discharge | Parent exact check of the hash-bound witness: `k=3`, residues `{0,1}` distinct, all 201 nonzero amplitudes in their classes, `K=300 <= M=2000`, real | [`depolarizing-witness-m1-parent-check.json`](depolarizing-witness-m1-parent-check.json) |
| Earlier bridge review | Claude Opus 5.5: ACCEPT-WITH-FIXES on the exact sector/channel bridge; fixes folded into PROOFS v4 | [`depolarizing-sector-bridge-review.note.md`](depolarizing-sector-bridge-review.note.md) |
| Independent numerical reproduction | Parent float64 implementation written before reading worker code: `1.14134071e-8` bits, inside the v3 interval, all 220 per-sector values inside; same-state controls negative at `p=201/1000` and `p=1/4` | [`depolarizing-parent-reproduction/README.md`](depolarizing-parent-reproduction/README.md) |
| Primitive arithmetic audit | 15,000 exact-Fraction checks of double-double primitives within the stated error | [`depolarizing-dd-parent-check.json`](depolarizing-dd-parent-check.json) |
| Worker reviews | Codex `gpt-6.1-sol` re-review of v3: ACCEPT-WITH-FIXES (minor tooling); same-vendor to the current parent | lane `review/codex-rereview-v3.receipt.json` |

## Priority and significance

In the audited primary sources, the prior explicit certified finite witness reaches total-error `p=0.194868` (Krohn-Grimberghe, [arXiv:2608.15870v2](https://arxiv.org/abs/2608.15870v2)). Our certificate extends that **certified finite-witness** point by `0.005132` to `1/5`, including every smaller p by data processing.

Ahmed et al. ([arXiv:2609.39747v2](https://arxiv.org/abs/2609.39747v2)) claim the stronger threshold `0.2029161`. Their analytic Theorem 6 gives an explicit fixed-cutoff coherent-information convergence bound; no mathematical error was found in the scoped [primary-source audit](depolarizing-asymptotic-priority-audit.md), which is not formal verification. The headline value also uses an approximately `1e-12` positive Gaussian-channel coherent information. The audit located no published amplitudes for that state, stated numerical precision/error bound or interval certificate. Parent read the load-bearing numerical passage at source lines 331–384. Thus the numerical premise is **uncertified in the checked public material**, not disproved. Lack of a finite M alone is not a flaw: if that positive premise holds, convergence already implies positivity at `p=1/5` and above.

Our finite certificate does not use Theorem 6 or its numerical values, but it does follow the same mod-3 Dicke-comb ansatz, Gaussian-limit search route and exact sector decomposition (re-derived here). It is an explicit finite realization and a rigorous-sign upgrade on `(0.194868,1/5]`, not a threshold beyond the stronger claim or a new construction paradigm. **Significance: modest specialist improvement.** No global-priority or "first" claim; the primary audit has stated read-scope and access limits.

**FRONTIER:** DELIVERY-READY as a scoped computer-assisted certificate; a major breakthrough is not established. The distinction between a sound-looking analytic theorem and its uncertified numerical premise does not by itself change that significance assessment. The worker is running a headroom assay above `0.2029161` and documentation/tooling fixes that preserve the hash-bound certified code.
