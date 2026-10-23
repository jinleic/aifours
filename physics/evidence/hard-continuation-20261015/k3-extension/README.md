# k = 3 extension: random 3-SAT is unsatisfiable w.h.p. at density 426679/100000 = 4.26679

This is a parent-requested extension (2026-10-16 PT) of the k = 4/5 package in `..`. The same
analytic bridge (`../notes/PROOF.md`) and the same two certifiers are applied to k = 3. The aim is to
test whether this pipeline beats Vorobyev's 4.268 (arXiv:2610.10599v1, endpoint 1067/250). This directory
is the only addition. No existing file in `..` was modified, including the k = 4/5 headline artifacts,
`../handoff/` and `../formal/`. The old snapshots and records were not modified either.

## 1. Result and exact claim scope

**Claim (written proof + certified premises).** Take a random 3-CNF on `n` variables with
`m = floor(alpha n)` independent clauses, each on 3 distinct uniformly chosen variables with
independent fair signs. For every `alpha >= 426679/100000 = 4.26679` it is unsatisfiable with
probability tending to 1. Explicitly, `P[SAT] <= exp(-n / 218,459,648,000,000,000)` for every
`n >= 1,747,677,184,000,000,000` (`certificates/constants.json`). This cutoff is a coarse sufficient
constant for the asymptotic statement, not a finite-size prediction.

| quantity | value |
|---|---|
| certified density (headline, T = 1024) | **426679/100000 = 4.26679** |
| certified density (secondary, same law, T = 512) | 10667/2500 = 4.2668 |
| Vorobyev (2026), same method, k = 3, T = 128 | 1067/250 = 4.268 (ours is lower by 0.00121) |
| empirical floor of the family (optimised 6-atom law, T = 1024; floating) | 4.2667853 |
| estimated T → ∞ floor (tail extrapolation; floating) | ≈ 4.266784 |
| Mertens–Mézard–Zecchina (2006) cavity estimate, eq. (43) | 4.26675 ± 0.00015 (±2σ) |
| parent tripwire | 4.2667; the certified density is 9e-5 above it |

**What is and is not claimed.** The strongest density uses the written analytic bridge and
certified numerical premises. It is not an exact threshold, a priority claim, or a new method.
The separate [Lean development](../formal/README.md) now kernel-checks the general-arity
criterion and the compatibility endpoints **4.2672 and 4.26718**; **4.26679 itself is not a
kernel theorem**, and the explicit exponential rate above remains a written result. None of
this work has human peer review.

The method is Vorobyev's, with Franz–Leone, Lelarge–Oulamara and Achlioptas–Menchaca-Méndez
as predecessors. The gain over 4.268 comes from a richer trial law and larger truncation.
The [parent priority comparison](../../../../institute/review/continuation-20261015/sat-k3-priority-check.json)
records earlier upper-bound claims near the cavity prediction, including Chatterjee et al.,
arXiv:2506.01359v2 Section 2.6. No global best-known or first-certification claim is made.
This paragraph incorporates the later formal-lane handoff; the numerical replay below remains
the 42-command run recorded at delivery.
The comparison is in a matched model. Vorobyev's §1 samples clauses independently, each on three distinct
uniform variables with fair negations, and allows repeated clauses. His theorem uses
`floor(1067 n/250)` clauses (staged reader `institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2/selection-inputs/literature/vorobyev-2026.reader.md`,
lines 44–46 and 971–975). Our model is the same. His transfer to distinct variables goes by conditioning
plus Chebyshev; ours goes by a resampling coupling plus McDiarmid. Both are written in the respective proofs.

**Verification levels, separately.**
1. *Certificate, established.* Certifiers A and B (byte copies of `../code/certify_a.py` and
   `../code/certify_b.py`, sha256 identical) give the same outward-rounded enclosures for both rows:

   | row | alpha | T | y | epsilon | Psi_T enclosure, A = B (20 d.p.) | margin `-(upper)-epsilon` | `T e^-y` upper |
   |---|---|---|---|---|---|---|---|
   | k3_T1024 | 426679/100000 | 1024 | 24 | 3/10000000 | [-0.00000043063105228493, -0.00000043063105228492] | 1.306e-7 | 3.866e-8 ≤ ε/2 = 1.5e-7 |
   | k3_T512 | 10667/2500 | 512 | 22 | 3/5000000 | [-0.00000067389244849371, -0.00000067389244849370] | 7.39e-8 | 1.428e-7 ≤ ε/2 = 3e-7 |

   The parent's separately written checker confirms both rows at 1536 bits, with
   upper bounds −0.000000430631052284 (T = 1024) and −0.000000673892448493 (T = 512). It also
   rejects its own same-law controls 4.26678@T1024 (+4.95e-7), 4.26679@T512 (+2.51e-7) and 4.2667@T512 (+8.58e-6).
   Receipts: `institute/review/continuation-20261015/sat-independent-k3-1536.json` (sha256 `925a3f29…9fb7`,
   input sha256 `88b6a0de…ab422`, which is this `certificates/trials.json`) and `sat-independent-k3-controls-1536.json`
   (sha256 `58ce2f81…1768`). The checker is `sat_independent_certificate.py`, sha256 `de819df7…6530`. At its earlier
   default of 768 bits it passed the T = 512 row but returned an upper bound of only −2.84e-7 > −ε for T = 1024,
   which fails the gate. That outcome is a fail-safe precision limit, not a disagreement (§5).
2. *Strongest full proof: written.* `../notes/PROOF.md` Sections 1–8 supplies the analytic bridge
   and exponential rate for the headline, together with these premises.
3. *Separate formalization.* `../formal/` proves the general-arity criterion and the `T = 128`
   3-SAT endpoints below. Its chunked 4.26718 theorem passed Comparator and a fresh imported-closure
   lean4checker replay (exit 0, 919 s), all under 4 GiB per process. The `T = 1024` headline
   and `T = 256` compatibility row are not formally certified.

**Compat rows for kernel checking** (`certificates/compat-trials.json`, requested for the formal lane).
These rows are kept separate so that the pinned `trials.json` is unchanged. Each row has
`T exp(-y) <= epsilon/2` and records `u` = max rate. Certifiers A and B and the epoch-2 checkers (T = 128 rows)
certify them. Each row has its own just-below rejection control in `controls/compat-same-law-controls.json`.

| row | law | alpha | T | y | epsilon | u | Psi_T upper (A = B) | control just below |
|---|---|---|---|---|---|---|---|---|
| k3_T128_compat_4.26718 | six atoms, re-optimised at T = 128 (crossing ≈ 4.2671729) | 213359/50000 = 4.26718 | 128 | 21 | 1/2000000 | 239949/250000 | −0.00000065367071717346 | 4.26717 → Psi ≥ +2.65e-7 |
| k3_T128_compat_4.2672 | same | 2667/625 = 4.2672 | 128 | 20 | 1/500000 | 239949/250000 | −0.00000249181636449635 | 4.2671 → Psi ≥ +6.7e-6 |
| k3_T256_compat_4.26685 | six atoms, optimised at T = 256 (crossing ≈ 4.2668455) | 85337/20000 = 4.26685 | 256 | 22 | 3/10000000 | 488033/500000 | −0.00000041840942969574 | 4.26684 → Psi ≥ +5.06e-7 |

Each row certifies the written theorem at its own density, below Vorobyev's 4.268.
The two `T = 128` rows now also have kernel-checked endpoint theorems in `../formal/`.
The `T = 256` row remains numerical-only; its monolithic kernel attempt stopped under a memory cap.

## 2. The analytic bridge covers k = 3 with no k-specific gap

Each step of `../notes/PROOF.md` holds for every integer `k >= 2`. At `k = 3`:

* **(C) insertion and the forced-literal product.** These are independent of k: integer costs, and
  universal quantifiers commute with the conjunction of 3 literal indicators.
* **(D)–(E).** Here `Q = R_2 R_3`. With old rows fixed, `E_new[W_C^h] = <B_h^3>_h`,
  `E_new[W_S^h] = <B_h>_h C_h^2` and `E_new[W_D^h] = C_h^3`. These need the 3 seeds to be iid with
  **independent uniform indices**, which the auxiliary repeated-variable model provides. Distinct
  variables enter only in §6.
* **(F) Lelarge–Oulamara nonnegativity for odd k.** `B^3 - 3BC^2 + 2C^3 = (B-C)^2 (B+2C) >= 0` for
  `B, C >= 0`, and here `B_h, C_h ∈ [0,1]`. No even-arity or signed-overlap hypothesis is used.
* **(G)–(I).** `f(K+1,L) + 2f(K,L) <= 3f(K,L+1) - 2d_y`. `N ~ Poisson(3 alpha n)` is thinned with
  probability 1/3 to `Poisson(alpha n)`, and the constant is `-2 alpha n d_y`.
* **(J)–(M).** The site count `L ~ Poisson(3 alpha n)` gives independent `Poisson(lambda)` marked counts with
  `lambda = 3 alpha / 2`. (K) needs this Poisson count, and §4 supplies it. Then `M_i = exp(lambda(nu_i - 1))`
  with `nu_i = E(1 - R_2 R_3)^i`, and the signed truncation (L) holds for every `T >= 1`.
* **(N)–(P).** The Poisson-to-fixed-count loss is `sqrt(alpha n) + 1`, the resampling loss is
  `alpha binom(3,2) = 3 alpha`, and `N0 = ceil(max(3, 16 alpha/c0^2, 4(1+3 alpha)/c0))`.
* **(Q).** McDiarmid's inequality with predictable Doob endpoints, as in `../notes/PROOF.md` §7, gives
  `P[SAT] <= exp(-2c^2 n/alpha)`. Monotonicity in the clause count extends this to larger densities.
* **Consistency checks.** For k = 3 the functional reduces to Vorobyev's eqs. (16) and (20) (adversarial
  review, `institute/review/continuation-20261015/physics-adversarial-review.json`). Both certifiers
  reproduce his published cross-check value (§4). The epoch-2 finite audit (`../code/finite_audit.py`)
  already includes k = 3.

## 3. Search and empirical floor (floating exploration, not premises)

The search used BFGS on atom locations and weights. Psi_T was evaluated exactly in fixed point
(2T + 192 bits) with an adjoint gradient (`code/explore_moments.py`, `code/explore_search.py`), alternating
with a secant solve for the zero crossing. Starts were Vorobyev's law and atom-split spreads of the
optimised law (`scratch/chain_m*.sh`, `scratch/opt_k3_*`). Zero crossings in alpha:

| T | Vorobyev law | m = 3 | m = 4 | m = 6 | m = 8 |
|---|---|---|---|---|---|
| 128 | 4.2678754 | 4.2672004 | 4.2671733 | 4.2671729 | 4.2671729 |
| 256 | 4.2677031 | — | 4.2668465 | 4.2668455 | 4.2668455 |
| 512 | 4.2676843 | — | 4.2667942 | 4.2667927 | 4.2667927 |
| 1024 | — | — | 4.2667871 | **4.2667853** | 4.2667854 |

* Support size stops mattering by m = 6. The truncation T is what drives the gain over Vorobyev:
  his own law already crosses at 4.26768 when T = 512.
* For k = 3, `mu_j` decays roughly like `j^-1.57`. The site-sum tail beyond T = 1024 is about 8e-8, and
  `dPsi/dalpha ≈ -0.0925`, so the T → ∞ floor is about 9e-7 lower, ≈ 4.266784.
* As a cross-check, a 64-atom quantisation of an SP population-dynamics fixed point (`code/explore_popdyn.py`,
  alpha = 4.2668, 200000 population, 200 sweeps) crosses at 4.2672366 (T = 128) and 4.2668662 (T = 256).
  These values lie just above the optimised laws.
* Rounding the T = 1024 six-atom law to denominators dividing 10^6 moves its crossing by 2e-11, to
  4.26678534640. The same rational law crosses at 4.2667927 when T = 512.
* **Tripwire check.** The floor, 4.2667853, is 8.5e-5 above the tripwire 4.2667 and lies within MMZ's ±2σ band
  [4.2666, 4.2669]. No law came near the tripwire. The variational principle makes the floor an upper
  estimate of the SAT threshold. Its exact relation to the 1RSB value is not established here.
* **Wall time.** Optimisation ran from about 00:32 to 00:55:27 PT, roughly 23 minutes, judging by the
  `scratch/` file times. At most four single-threaded processes ran at once: three optimisation chains
  plus either the population-dynamics run or the kernel. Exploration memory was not instrumented.
  Certifier memory at T = 1024 was measured with `/usr/bin/time -l`: peak RSS 26.7 MB for A (1.6 s) and 57.0 MB for B
  (131.6 s) (`notes/rss-certify-{a,b}-T1024.txt`). The rest of the ~2 h budget was not used,
  because the floor had converged to about 1e-6 and no further search could change the claim materially.

**Choice of the certified density.** Any `alpha` above this law's crossing, 4.26678535, is certifiable in
principle with smaller ε and larger y. The headline takes the smallest point of the 1e-5 grid at
which `|Psi_1024| >= 1e-7`, which is 4.26679. The secondary row takes the smallest grid point at
T = 512, which is 4.2668.

## 4. Controls (observed outcomes are in `logs/replay.json`)

* **Vorobyev control.** His law `P(R=1/20)=1/4, P(R=2/5)=1/2, P(R=17/20)=1/4` at 1067/250 with T = 128,
  y = 20 and ε = 1/100000 is in `certificates/vorobyev-control.json`. Both certifiers certify it with
  enclosure `[-0.00001120254523842976, -0.00001120254523842975]`. That interval contains the paper's
  cross-check value `-0.000011202545238429759`.
* **Same-law density controls** (`controls/same-law-controls.json`). Both certifiers must exit 1 with a
  rigorous lower bound `Psi > 0`. In the final run, every row was rejected by both A and B, and the two
  lower bounds were identical:

  | row | alpha | T | role | rigorous lower bound on Psi_T |
  |---|---|---|---|---|
  | k3_T1024_at_4.26629 | 426629/100000 | 1024 | certified density − 0.0005 | +4.583541e-5 |
  | k3_T1024_at_4.2667_tripwire | 42667/10000 | 1024 | tripwire | +7.897635e-6 |
  | k3_T512_at_4.2663 | 42663/10000 | 512 | secondary density − 0.0005 | +4.559152e-5 |
  | k3_T512_at_4.2667_tripwire | 42667/10000 | 512 | tripwire | +8.579601e-6 |
  | k3_T512_at_4.26679 | 426679/100000 | 512 | headline density at T = 512: truncation alone defeats it | +2.514661e-7 |
  | k3_T128_compat_at_4.26717 | 426717/100000 | 128 | compat row 4.26718, 1e-5 below (`controls/compat-same-law-controls.json`) | +2.653991e-7 |
  | k3_T128_compat_at_4.2671 | 42671/10000 | 128 | compat row 4.2672, 1e-4 below | +6.698831e-6 |
  | k3_T256_compat_at_4.26684 | 426684/100000 | 256 | compat row 4.26685, 1e-5 below | +5.057093e-7 |

* **Tamper controls** (`controls/tamper-controls.json`). With ε = 5e-7, above the margin, both certifiers
  must exit 1. With y = 20 the finite-y gate fails, and they must exit 1. With masses summing to
  1 + 1e-6, or with an atom equal to 1, they must exit 2.
* **python -O gating.** One same-law control and one tamper row are rerun under `python3 -O` and must
  still exit 1. The certifiers contain no `assert`.
* **Epoch-2 checkers** (`--with-epoch2`; immutable snapshot code, read-only). Both certified the two
  T = 128 compat rows. `independent_check.py` gave [−653670717174, −653670717173]·10^-18 for the 4.26718 row.
  `certify.py`, with its coarser 384-bit, 220-squaring grid, gave
  [−0.000000653670799694, −0.000000653670713431], which still contains ours. The same `certify.py` *rejected*
  k3_T1024, as required: its fixed grid is too coarse for the 2^1024 cancellation, and it reported upper bound
  +2.04e-5. A precision-starved implementation therefore fails safe.

## 5. Working precision at T = 1024, and why clipping cannot hide precision loss

`mu_j = sum_i (-1)^i binom(j,i) M_i` cancels by up to a factor `2^j`, about 10^308 at j = 1024. An interval
difference table enlarges input widths by at most `sum_i binom(j,i) = 2^j`. The working precision must
therefore exceed about 1024 bits (308 digits) plus the target accuracy:

* **Certifier A:** binary grid of `P = T + 192 + 8m` bits, which is 1264 bits for T = 1024, m = 6. Each
  `M_i` is computed at `P + 160` working bits (64 exact halvings, an alternating Taylor series, 64 outward
  squarings) and then rounded outward to `P` bits. So `width(M_i)` is a few units of `2^-P`, and
  `width(mu_j) <= 2^j · max_i width(M_i) ≈ 2^(1024-1264) ≈ 10^-72`.
* **Certifier B:** decimal grid of `D = floor((T+220)·0.30103) + 10` digits, which is 384 digits for T = 1024.
  `exp(-a)` is computed with `floor((floor(a)+1)·0.4343) + 12` extra guard digits. So `width(mu_j) <= 2^1024 · 10^-383 ≈ 10^-75`.
* **Measured.** `code/precision_report.py` reruns both certifiers' own code paths and records the exact
  widths in `certificates/precision.json`. It requires every `mu_j` enclosure and the final `Psi_T`
  enclosure to have width below 1e-40. Measured at T = 1024: A (1264 bits) has max width(mu_j) = 10^-72.03 and
  width(Psi) = 10^-55.17, the latter limited by A's 192-bit clause-log grid. B (384 digits) has max width(mu_j) = 10^-75.74
  and width(Psi) = 10^-59.22. At T = 512: A 752 bits, 10^-72.03; B 230 digits, 10^-75.87. All widths are far below the
  margins of about 1e-7.
* **Clipping is sound and fail-safe.** The only clips are `max(0, ·)` and `min(1, ·)` on enclosures of
  quantities proved to lie in [0,1]: `exp(-a)`, `nu_i`, `M_i` and `mu_j = E(1-A)^j` (`../notes/PROOF.md` (K), (R4)).
  The site term uses `sum max(0, mu_lo)^2/j <= sum mu_j^2/j`. If precision were lost, `mu_lo` would drop
  toward 0 and the term would vanish. That raises the upper bound on Psi, so the gate fails, never falsely passes.
  Symmetrically, the clip `min(1, mu_hi)` can only lower the rigorous lower bound used by the rejection controls.
  The parent's 768-bit run, which fails to confirm T = 1024, and the 384-bit epoch-2 producer's rejection
  are both observed instances of this fail-safe behaviour.

## 6. Replay (one command), recorded runs and files

    cd physics/evidence/hard-continuation-20261015/k3-extension
    python3 code/replay_k3.py --with-epoch2   # exit 0 iff every expectation holds; writes logs/replay.json and SHA256SUMS

The replay uses Python 3.14.3 and the standard library only. Exploration also needs numpy and mpmath.
`--with-epoch2` reads the immutable epoch-2 checkers. Without the flag, the replay is self-contained.

* **First run** (before the compat rows, the precision report and the epoch-2 steps were added; superseded and kept
  in `logs-replay1-superseded/`): 27 commands, all expectations met, 1229.7 s.
* **Final run** (launched 2026-10-16 01:16:54 PT): `python3 code/replay_k3.py --with-epoch2` printed
  **ALL EXPECTATIONS MET: 42 commands, 1502.7 s**. The script exits 0 exactly in that case. The A/B endpoint gap was 0 at 20 decimals for all 5 certified rows.
  The receipt is `logs/replay.json`, with stdout in `logs/replay-stdout.txt`. The replay ran single-threaded;
  B's peak RSS at T = 1024 is 57 MB.
* `SHA256SUMS` was regenerated after `README.md` and `result.json` were final. It covers every file in this
  directory except itself and `code/__pycache__/`. `replay_k3.py` writes a narrower list that excludes
  `scratch/` and `logs-replay1-superseded/`.

Layout:
* `certificates/trials.json`: the two headline rows. Its sha256 is pinned by the parent receipts, so do not edit it.
* `certificates/compat-trials.json`: the T = 128 and T = 256 rows for kernel checking.
* `certificates/{,compat-}results_{a,b}.json`: the full enclosures.
* `certificates/{,compat-}constants.json`: the transfer constants.
* `certificates/precision.json`: the working-precision report.
* `certificates/vorobyev-control.json`: the Vorobyev control row.
* `controls/`: the same-law, compat same-law and tamper controls.
* `logs/`: per-command logs with argv, return code and elapsed time, plus `replay.json` and `replay-stdout.txt`.
* `code/`: the certifiers, transfer script and explorers (byte copies of `../code/`), plus `precision_report.py` and `replay_k3.py`.
* `scratch/`: raw exploration output, which is not load-bearing.
* `result.json`: the machine-readable summary.
* `SHA256SUMS`: the final package list includes `scratch/` and `logs-replay1-superseded/`; it excludes itself and Python caches. The replay script's generated list is narrower, as noted above.

**JSON layout used for the parent's independent checker.** It is identical to `../certificates/trials.json`:
`{"description": str, "trials": [{"name": str, "k": int, "alpha": "p/q", "rates": ["p/q", ...],
"weights": ["p/q", ...], "T": int, "epsilon": "p/q", "y": int, "role": str}]}`. Each rate lies in
`[0,1)`, the weights are nonnegative and sum to exactly 1, and the atoms are listed in increasing order.
The compat rows add `"u": "p/q"`, the max rate.

## 7. FRONTIER

**NOVELTY-UNCLEAR / PROOF-OBLIGATION for the strongest formal endpoint.** The certified
4.26679 is within about 5e-6 of the best `T = 1024` floating value found in this trial family.
That is an observed optimization result, **not a proved global floor**. The general-arity
criterion and 4.26718 compatibility endpoint are now formally checked. A kernel certificate
for 4.26679, human expert review, or a closed exact-constant priority comparison could change
the remaining claim status. More tuning of the same family is not scheduled.
