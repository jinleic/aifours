# K62-M3R parent commentary and transcription erratum v1

Recorded at 2026-10-19T11:55:07-0700. Read after immutable K62-M3R-v2 `af2b965bf69b252e266064aff5b201b16757bcb76af152d7eee8c89ee77888b3` and review package `b0baf77dc9db360f65149670ea047080ce925949d3576743ddb07175b2e11d3a`. Disposes Codex review `9f244c93334da6f6267255213745d1f8fda8f0e3a2d56fde7095980473b833e8`: no FATAL/MAJOR, five MINOR findings. The load-bearing Lemma A/C, RR, W6, R2N and corollary statements are unchanged. Corollary6.2 remains conditional on pending MK. Original target R1X/R2X remains unproved. Each Old span occurs exactly once in the proof.

## m1 displayed failed certificate

Old:
````text
for an R2-row with i*-entry 2 the allowed sets are
  pairs and {u, i*, d}, and the best feasible value is 11/2 < 6 (e.g. 1/2 on entries 2 and on d), so LFC (d) gives nothing.
````

New:
````text
for an R2-row with i*-entry 2, entry-1 labels are isolated and allowed sets include empty sets, singletons, eligible pairs and {u, i*, d}. The displayed certificate has weight 1 on entries 1, 1/2 on entries 2 and on d, and 0 on i*: its value is (4-a)+a+3/2=11/2<6, so this particular certificate gives no contradiction. No optimality assertion is needed here.
````

## m2 sufficient contradiction targets

Old:
````text
Equivalent targets suggested by R2N: a lower bound E > n_t / 12 for the empty fibres at t, or the exclusion of
  tau_y'({d, i*, e}) = 3 (that is, Phi_e(Phi_d cap Phi_(i*)) = Phi_ePhi_d in the y'-configuration) together with an R2-row.
````

New:
````text
Sufficient contradiction targets suggested by R2N: prove E > n_t / 12 for EVERY R2-instance y, or prove that NO R2-instance y admits ANY e in O' with tau_y'({d, i*, e}) = 3 (equivalently, Phi_e(Phi_d cap Phi_(i*)) = Phi_ePhi_d in the y'-configuration). No unrestricted-row characterization or unconditional empty-fibre lower bound is asserted.
````

## m3 withdrawn ancillary mutation

Old:
````text
(4) in R2N (ii) allow the 4-sets {u, u', i*, d}: with f_4 such
  fibres the identity becomes f_3 + 2 f_4 - f_1 = n_t / 6 + 2E, and since f_3 + f_4 <= n_t / 3 the bound weakens to E <= n_t / 4.
````

New:
````text
(4) WITHDRAWN: merely allowing the 4-sets {u, u', i*, d} in a hereditary allowed-set system also allows triples {u, u', d}, so f_3+f_4<=n_t/3 is no longer justified. No weakened bound E<=n_t/4 is claimed. The original R2N count, using the actual allowed-set restrictions, is unchanged.
````

## m4 limits of attempted subgroup route

Old:
````text
(5) The subgroup route W6 closes m = 3 but at m = 6 gives
  no contradiction from Sun(2), Sun(3) inside W alone.
````

New:
````text
(5) The particular subgroup argument recorded in W6 closes m = 3 and stops at its displayed m = 6 structure. This is not a theorem that every possible use of Sun(2)/Sun(3) inside W fails.
````

## m5 divisibility transcription

Old:
````text
m divides n_a and n_b, hence
g_ab = 6.
````

New:
````text
m divides gcd(n_a, n_b) =
g_ab = 6.
````

## Scope notes

The discussion of MK's structural route in section7(b)(4) is diagnostic commentary on a particular attempted route, not an imported theorem beyond the explicitly conditional Corollary6.2. The review-package line19 phrase "the residual ... reduces to R2 alone" is conditional on MK's pending classification; RR itself is unconditional relative to accepted imports. The package's description of the earlier draft mutation correction is historical: mutation(4) of v2 is now withdrawn too. No counterfactual n_t/4 theorem survives this overlay.
