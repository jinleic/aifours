# phys-p0422 continuation (2026-10-15 PT): certified random 4-SAT / 5-SAT UNSAT bounds 9.9325 and 21.1175

Owner-authorized continuation of the immutable epoch-2 package
`institute/runs/hard-2026-10-15/problems/phys-p0422/attack-e2` (snapshot sha256 `9056545…88da`). The old
snapshots, records and navigation are unchanged. This directory's `formal/` subtree belongs to a
separate formalization lane. Nothing here writes to it or depends on it.

## 1. Result

| | k = 4 | k = 5 |
|---|---|---|
| **New certified density (this package)** | **3973/400 = 9.9325** | **8447/400 = 21.1175** |
| Epoch-2 certified density (same method) | 249/25 = 9.96 | 1057/50 = 21.14 |
| Classical one-flip bound (Kirousis et al. 1998; Dubois–Boufkhad 1997): root of `(1-2^-k)^a [2-exp(-ka/(2^k-1))] = 1` | 10.22455… (tabulated 10.23) | 21.32280… (tabulated 21.33) |
| Method floor, floating exploration (optimized laws, T = 1024) | ≈ 9.932389 | ≈ 21.117262 |
| Cavity/SP prediction, Mertens–Mézard–Zecchina (2006), Table 1 | 9.931 | 21.117 |
| MMZ Fig. 4 regression (K = 4 only) | 9.9324 | — |

**Claim (written proof + certified premises).** For `k = 4` and every `alpha >= 9.9325`, and for
`k = 5` and every `alpha >= 21.1175`, take a random formula on `n` variables with `floor(alpha n)` independent clauses. Each
clause uses `k` distinct uniformly chosen variables and independent fair signs. The formula is
unsatisfiable with probability tending to 1. Explicitly, `P[SAT] <= exp(-n/1,271,360,000,000,000)` for
`n >= 10,170,880,000,000,000` (k = 4) and `P[SAT] <= exp(-n/2,703,040,000,000,000)` for
`n >= 21,624,320,000,000,000` (k = 5). These cutoffs are coarse sufficient constants for the asymptotic
statement, not finite-size predictions.

The new values improve the epoch-2 package by 0.0275 and 0.0225. They lie 1.1e-4 and 2.4e-4 above the
numerically estimated floor of this functional. Further law tweaking can therefore gain at most about
1e-4 and is not claim-changing. Both values stay above the cavity tripwires 9.931 and 21.117. No law
was certified at or below a tripwire.

### Verification levels, stated separately

1. **Certificate (numerical premises), established.** The rigorous outward-rounded rational
   enclosures `Psi_512 <= -1/200000` and `512·exp(-20) <= 1/400000` hold for both headline rows. Two new
   implementations in this package compute them by different algorithms (A: product laws, binary
   grid, reduced Taylor exponential plus squaring; B: exact rational moments, decimal grid, direct
   alternating Taylor). They agree on all 20 printed decimals:
   k = 4 `[-0.00000599415877186445, -0.00000599415877186444]`, k = 5 `[-0.00000683568324447069, -0.00000683568324447068]`.
   The parent's separately written 768-bit checker passed all four trial rows, and its upper bounds match to its 18
   printed decimals. Its receipt is `institute/review/continuation-20261015/sat-independent-improved-bounds.json`,
   sha256 `8509a0ec…d281`, checker sha256 `2bf5c852…72b1f3`, and its input sha256 `1cdc03c2…0913e` equals this
   package's `certificates/trials.json`. For the same laws at `T = 128`, the two epoch-2 checkers
   (read-only snapshot code) reproduce the enclosures exactly.
2. **Full proof: written, not formally verified, not peer reviewed.** The full proof is the analytic bridge
   in `notes/PROOF.md` §§1–8 together with those premises. The bridge is the epoch-2 argument. It was audited by
   the parent in epoch 1, passed by two referee passes, and judged "correct" with high trust by an adversarial
   Opus review (`institute/review/continuation-20261015/physics-adversarial-review.json`). The fixes
   requested there have been applied (§5 below).
3. **Separate kernel-checked result.** [`formal/`](formal/README.md) proves the general-arity
   criterion and whp unsatisfiability at **9.934 (k = 4)** and **21.123 (k = 5)**, using the
   six-atom `T = 128` rows, as well as the old endpoints. The final imported closure passed a
   fresh lean4checker replay (exit 0; 1178 s). The stronger `T = 512` headline rows here are
   **not** kernel-certified. The formal development proves convergence, not this written proof's
   exponential rate or explicit finite-n constants; its Comparator has documented macOS trust limits.
4. **Related 3-SAT refinement.** The [`k3-extension/`](k3-extension/README.md) package certifies
   **4.26679** with `T = 1024`, improving the explicit 4.268 endpoint in Vorobyev's preprint.
   Its parent-written 1536-bit checker confirms the certificate and rejects same-law controls.
   The separate Lean development kernel-checks **4.26718** through bounded certificate chunks,
   with a final fresh imported-closure replay under 4 GiB. These are numerical and formal
   instantiations of the same established method, not an exact threshold or an established global record.

### Attribution: no new method

The method is the zero-temperature Franz–Leone replica/cavity interpolation bound. Franz–Leone (2003)
proved it for even arity. Lelarge–Oulamara (2018) condition (4) admits odd arity with nonnegative
factors. The proof follows the integer-cost, y-reweighted energetic interpolation and
exact-rational certificate style of Vorobyev (arXiv:2610.10599, k = 3), extended to general `k`.
Achlioptas–Menchaca-Méndez (2012) is an earlier energetic interpolation for unsatisfiability. The
infinite-`T` functional is the survey-propagation zero-energy complexity evaluated at a trial law.
The [primary-source ledger](../../../institute/review/continuation-20261015/physics-prior-art.json)
and [independent live audit](../../../institute/review/continuation-20261015/physics-novelty-live-review.md)
find prior upper-bound claims near the cavity predictions, including Chatterjee et al.
(arXiv:2506.01359v2, Section 2.6), and earlier general-k Lean material in OpenAI's math collection.
Thus this is explicit numerical certification within an established framework, not discovery of a
new upper-bound principle or the first k>=4 formalization. No earlier certification of these exact
endpoints was located in the checked sources; priority and global best-known status remain unresolved.

## 2. Exact assumptions (premises) of the claim

* **Analytic bridge (written proof):** `notes/PROOF.md` (A)–(Q). It needs `k >= 2`, a finitely supported
  rational law in `[0,1)`, integer `T >= 1`, `y > 0`, and `n >= 1`, with `n >= k` only for the distinct-variable
  transfer. (E) needs iid uniform clause indices, which is why the auxiliary model has repeated variables. (K) needs a Poisson
  site count, which is why the proof Poissonizes first. Concentration uses McDiarmid's bounded-differences inequality.
* **Numerical premises:** the two certified rows of `certificates/trials.json`, sha256
  `1cdc03c232078cac29906c0156bfdf7658b40fbe80fe1d0577dbcfc87000913e`.
* **Not premises:** the floating exploration, the population dynamics, the MMZ values and the
  satisfiable-region searches. These only guided or sanity-checked the work.

## 3. Commands, return codes, timing

All commands run from this directory with Python 3.14.3 (`/opt/homebrew/bin/python3`), standard
library only. Only the exploration and control scripts use numpy and mpmath.

| command | expected | observed |
|---|---|---|
| `python3 code/certify_a.py --trials certificates/trials.json` | exit 0 | 0; 1.3 s for 4 rows |
| `python3 code/certify_b.py --trials certificates/trials.json` | exit 0 | 0; 26.5 s for 4 rows |
| `python3 code/transfer_constants.py` | exit 0 | 0; prints c0, c, N0 and the P[SAT] rates |
| `python3 code/finite_audit.py` / `--break-comparison` | 0 / 1 | 0 (2×1080 comparisons, 2×1,203,048 insertions) / 1 |
| `python3 code/replay.py --with-epoch2` (everything below, 41 commands) | exit 0 | 0; **all expectations met, 413.7 s**; receipt `logs/replay.json` |
| `python3 code/control_lowdensity.py --T 256 --starts 3 --cases k5,k4,k2 --out controls/lowdensity-optimisation-T256-final.json` | exit 0 | 0; 331.5 s; no negative Psi found (§4) |
| same replay inside a copy of `handoff/` (`scratch/handoff-replay-copy/`) | exit 0 | 0; 41/41 expectations met, 412.0 s; the bundle is self-contained |

`replay.py` records the argv, return code, expected code, elapsed time and log sha256 of every
command. It also checks A/B enclosure agreement, the gap between the two endpoints (0 at 20 decimals), and that every
negative control's rigorous lower bound is positive. The epoch-2 producer `certify.py` needs
`python3 -X int_max_str_digits=0`. Without that flag, Python 3.14's integer-to-string limit stops its result
printing. The arithmetic is unaffected. At `T = 512` its fixed 384-bit grid is too coarse, so it rejects
(upper bound +1.4e-6). This fail-safe rejection is a precision limit, not a disagreement.

## 4. Discriminating controls (all observed as expected)

**Same-law marginal-density controls.** The certified laws are kept and only `alpha` (or `T`) is changed.
Both certifiers reject every row, and their rigorous lower bound is positive, so the law provably cannot
certify there:

| law, T | alpha | role | Psi_T enclosure (lower ≥) |
|---|---|---|---|
| L4, 512 | 9.9323 | just below this law's crossing ≈ 9.93239 | +0.000004899000 |
| L4, 512 | 9.931 | cavity tripwire | +0.000075701422 |
| L4, 512 | 7.9 | below Achlioptas–Peres SAT bound 7.91 | +0.102801274425 |
| L4, 128 | 9.9325 | headline density with T = 128 | +0.000026669126 |
| L5, 512 | 21.1172 | just below this law's crossing ≈ 21.117263 | +0.000001819446 |
| L5, 512 | 21.117 | cavity tripwire | +0.000007589507 |
| L5, 512 | 18.7 | below Achlioptas–Peres SAT bound 18.79 | +0.068035215993 |
| L5, 128 | 21.1175 | headline density with T = 128 | +0.000146130416 |

**External-truth controls** (`certificates/reference-trials.json`). For k = 2, the 2-SAT threshold is
proved to be 1. A one-atom law certifies `Psi_128 <= -1.435e-4` at alpha = 1.1, and both certifiers reject the same law at
0.95 with lower bound +4.105e-4. For k = 3, the epoch-2 reference input (Vorobyev's law at 4.268) gives
`[-0.00001120254523842976, -0.00001120254523842975]`. That interval contains the value the adversarial reviewer quotes
as published, −0.000011202545238429759.

**Satisfiable-region optimisation.** The theorem implies `Psi_T >= 0` for every law at alpha = 7.9 (k = 4),
18.7 (k = 5) and 0.95 (k = 2). Each case ran BFGS (`T = 256`) from 36 random starts, with atom floors 0, 0.05 and 0.2,
plus a warm start from the certified law. No negative value was found. The minima were:

| case | floor 0 | floor 0.05 | floor 0.2 |
|---|---|---|---|
| k = 4, 7.9 | 4.5e-45 | 1.44e-4 | 0.0237 |
| k = 5, 18.7 | 0.0 | 2.33e-5 | 0.0187 |
| k = 2, 0.95 | 5.0e-19 | 2.17e-4 | 0.0071 |

Unconstrained runs collapse toward the trivial law (Psi → 0⁺). At k = 5, 18.7, several runs, and the warm
start, stop at a nontrivial stationary law with Psi ≈ +0.0669. This matches the positive SP complexity
expected between MMZ's alpha_d ≈ 16.12 and alpha_c ≈ 21.117. Results are in
`controls/lowdensity-optimisation-T256-final.json`. This is floating sanity evidence only.

**Tamper controls.** Both certifiers return exit 1 for `epsilon` above the margin and for `y = 15` (the finite-y
gate), and exit 2 for non-normalized masses and for an atom equal to 1. Gating still works under `python3 -O`,
because no `assert` is used (`logs/python-O-gating.txt`).

**Finite audit** (`code/finite_audit.py`). This is the epoch-2 audit ported with explicit raises, and its log
is regenerated (the epoch-2 top-level log was stale). It adds a second configuration, ρ = (δ_1/5+δ_1/2+δ_4/5)/3 with
t = 1/3. Both configurations pass, and the sign mutation inside `check_system` is rejected.

## 5. Changes relative to epoch 2 (each audited; see `notes/PROOF.md` §11)

* New six-atom laws, `T = 512`, `epsilon = 1/200000`, `y = 20`. The analytic statement is unchanged.
* §7 now cites McDiarmid and gives the conditional-Hoeffding argument with predictable endpoints.
* (E) and (K) now flag their essential modelling hypotheses.
* §8 adds the moment identities (R2)–(R4) used by certifier B, with proofs.
* Gating in every new checker uses explicit exceptions and exit codes instead of `assert`.
* There are new discriminating controls (§4). The finite-audit log was regenerated.

## 6. Exploration record (not premises)

Exploration used a floating optimizer. It evaluated the functional exactly in fixed point (2T+192 bits)
with an adjoint gradient (`code/explore_moments.py`, `explore_search.py`). Zero crossings of optimized laws:

| T | 128 | 256 | 512 | 1024 |
|---|---|---|---|---|
| k = 4 (m = 6) | 9.932961 | 9.932416 | 9.932390 | 9.932389 |
| k = 5 (m = 6) | 21.122040 | 21.117361 | 21.117263 | 21.117262 |

At `T = 128`, three to eight atoms give the same crossing to 1e-7, so `T`, not support size, drove the
gain over epoch 2. Quantized SP population-dynamics fixed points (`code/explore_popdyn.py`, 64 atoms)
cross at 9.932421 and 21.117423 at `T = 256`, which agrees with the optimizer. The k = 4 floor 9.93239 is above MMZ Table 1's 9.931. It coincides with
MMZ's own Fig. 4 regression value 9.9324 (`sources/mmz-cs0309020-*-excerpt.txt`; the PDF sha256 is
`4b4d08a0…6a9f`). Neither MMZ number is a certified threshold. Both are physics estimates, and that
discrepancy is preserved here, not resolved. Seeds for any requeue are in `seeds/`.

## 7. FRONTIER decision

**FRONTIER: NOVELTY-UNCLEAR / PROOF-OBLIGATION for the strongest formal endpoints.**
The certified constants lie about 1e-4 (k = 4) and 2.4e-4 (k = 5) above the best floating
values found with optimized six-atom laws at `T = 1024`. Those values are **not proved global
floors**; richer laws are not excluded. [INFERENCE] More tuning of this same family has little
quantitative headroom, so the continuation does not repeat it. A certificate crossing a cavity
tripwire would require an error investigation, not automatic promotion.

1. The general-arity Lean criterion and improved `T = 128` endpoints are complete in `formal/`.
   Kernel certification of the `T = 512` headline would need a memory-bounded arithmetic
   representation; the attempted monolithic proof exceeded its watchdog. No such theorem is claimed.
2. Close the remaining explicit-constant priority holes, or obtain human expert review. The method
   and its expected small-k upper-bound location are already prior art.

## 8. Limitations

* The written proof is not formally verified or peer reviewed. A formula-level error common to all
  checkers would not be caught by arithmetic agreement. Its exactness rests on the derivation, the k = 2
  and k = 3 external checks, and the reviews.
* The finite-n constants are astronomically weak. The theorem is asymptotic.
* Novelty is unknown. The method is prior art, and only the constants may be new.
* The floor estimates and MMZ comparisons are floating exploration, not certified statements.

## 9. Layout

`notes/PROOF.md`: self-contained proof and enclosure obligations. `code/`: certifiers A/B, the transfer
constants, the finite audit, the replay, the controls and the exploration tools (`explore_*`). `certificates/`: trials,
reference trials, A/B results and constants. `controls/`: same-law, tamper and satisfiable-region
controls. `logs/`: per-command logs and the `replay.json` receipt. `seeds/`: exploration laws and population
laws for any requeue. `sources/`: the MMZ excerpts. `scratch/`: raw exploration outputs (population
`.npy` files and optimizer logs). `handoff/`: compact, hash-pinned integration bundle.
`result.json`: machine-readable summary. Superseded but kept: `logs/control-lowdensity-T256.txt` (first launch,
which hit a syntax error, then a partial run that was stopped) and `controls/lowdensity-optimisation-k2-T256.json` (an earlier k = 2 run). The
final run above supersedes both.
