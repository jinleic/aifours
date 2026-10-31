# f119 review — "Source-independent finite and uniform joint-budget theorem" (author candidate v1)

**Kind:** INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW (manifest `f119-privacy-uniform-joint-budget`, schema 1).
**Reviewer:** same-harness Claude Code session (model id `anthropic/claude-fable-5-1`), no author contact, no web, no external/paid model, no Git, no deletion, no held mathematical outcomes used.
**Pre-write clock (observed, `/bin/date`):** `2026-10-29T02:54:00Z` = `Wed Oct 28 19:54:00 PDT 2026`.

## 0. Bindings (verified by the reviewer)

| item | path | SHA-256 | bytes / LF |
|---|---|---|---|
| manifest | `review-waves/f119-privacy-uniform-joint-budget/manifest-v1.json` | `d99311e516485267b0f36ba0c12a919f97cfc0e013c51f7f40f46a4c64cd8583` | 1855 B (verified 02:38:30Z) |
| sole input | `information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-explicit-uniform-budget-theorem-v1.md` | `f020dab0002911f8222182725ba123da2b25f4b62102bd84ac0282f4496e75cc` | 5675 B, 82 LF, trailing `\n` (verified 02:38:38Z; matches manifest exactly) |
| reviewer control script | `reviewer-f119-controls-v1.py` | `e6323db62dd59a9050f32bf9a0313b3f69c13b411640af07412432d37f2e80a5` | 22333 B, 399 lines |
| reviewer control output | `reviewer-f119-controls-output-v1.txt` | `775dae78e046f8f010d3066dbf3b6ca14832d0e1204af92a98b8907c67577762` | 13801 B, 142 LF |

Read order: manifest (whole), then the input, complete and verbatim (`:raw`, all 82 lines). Nothing else was read as mathematical input. The candidate cites an earlier frozen file `frontier-20261028-all-ratio-joint-budget-inversion-v1.md` (SHA `7fc5ce61…`); it is **not** a declared input, I did **not** open it, and this review makes **no** statement about it or about the candidate's "strengthens and replaces" sentence.

Control run receipt: `/bin/date` before `2026-10-29T02:52:12Z`; in-script `start_utc=2026-10-29T02:52:16.417902+00:00`, `end_utc=2026-10-29T02:52:35.085832+00:00`; `/bin/date` after `02:52:36Z`; Python 3.14.3, macOS arm64, mpmath 1.4.1 (Section 10 only); exit code 0; the script prints its own source SHA (`e6323db6…`, equal to the table) into the output; `fail_count=0`, `VERDICT_OF_CONTROLS=ALL_PASS`. The script was written from my own reconstruction; no author code exists in the inputs and none was executed.

## 1. Verdict

**No FATAL. No MAJOR.** Six **MINOR** expository/scope items (§7), none of which affects the truth of the finite inequalities (2), (3) or the uniform relative estimate (4)–(5).

What I independently proved (full reconstruction §§2–5, with my own explicit constants replacing every "sufficiently small/large" in the candidate):

> **Explicit form of (4).** Let `eta := ell + ell^2/j`. For every `(j, ell)` with `ell <= 1/150` and `eta <= 1/8`, and for **every** `r = j/ell > 0`,
>
> `(1 - 7 eta)^3 * ell^3 F(r)  <=  b_max(j, ell)  <=  ell^3 F(r) / (1 - 1.5 ell)  <=  ell^3 F(r) (1 + 2 ell)`,
>
> hence `|b_max(j,ell) / (ell^3 F(r)) - 1| <= 21 eta` and `eps_min = 3 log(1/ell) - log F(r) + O(eta)` with `|O(eta)| <= 2*21 eta` once `21 eta <= 1/2`.

This is a **pointwise** inequality in `(j, ell)`: no sequence, subsequence, order of limits or continuity of `r` enters. Arbitrary oscillation of `r` (including `r -> 0` with `r >> ell`, `r` crossing `1/6` in either direction or sitting exactly at `1/6`, and `r -> infinity`) is therefore covered automatically. The candidate's (2) and (3) are exact finite necessary conditions valid without any asymptotic hypothesis (my §3), and (3) in fact holds for **all** `r` (§3.8).

Conditional scope of this verdict: the class exactly as reconstructed in §2 (closed `l1` unit diamond `D` in `R^2`, all-Borel/all-shift multiplicative privacy with parameter `b = e^(-eps)`, Euclidean second moment `J`, `l1` first moment `L`). Not claimed and not verified: an exact finite-`b` optimiser, sharpness of the `ell^2/j` term in the true `b_max`, or anything outside the regime `eta <= eta_0`.

## 2. Setting as reconstructed (the candidate never states the dimension — see M1)

`D = {x in R^2 : ||x||_1 <= 1}`, closed, `|D| = 2`, `D = -D`. A Borel probability law `mu` is **b-private** iff `mu(A + v) >= b mu(A)` for every Borel `A` and every `v in D` (equivalently `P(x+Z in A) <= e^eps P(y+Z in A)` whenever `||x-y||_1 <= 1`). `J = E|X|_2^2`, `L = E||X||_1`, `b_max(j, ell) = sup{ b : some b-private law has J <= j, L <= ell }`. All constants in the candidate are the `R^2` values: `int_D |x|^2 = 2/3`, `int_D ||x||_1 = 4/3`, `|tD| = 2t^2`, `int_{tD} ||x||_1 = 4t^3/3`, `int_{tD} |x|^2 = 2t^4/3` (each recomputed by me: e.g. `int_D x_1^2 = 2 int_0^1 x^2 * 2(1-x) dx = 1/3`).

## 3. Upper bounds — density/floor dual reconstructed from scratch

**3.1 Absolute continuity.** If `|A| = 0`, then `2 mu(A) <= b^-1 int_D mu(A+v) dv = b^-1 int |D ∩ (x - A)| dmu(x) = 0`. So `mu << Leb`; let `p` be a density.

**3.2 All-point representative and boundedness** (asserted, not proved, in the candidate; here is the proof). Put `p^(x) := liminf_{e->0} mu(x + eD) / (2 e^2)`.
(i) `x + eD ⊂ B(x, e)` and `|eD| = (2/pi)|B(x,e)|`, so the family shrinks nicely and Lebesgue differentiation gives `p^ = p` a.e.
(ii) Privacy with `A = x + eD` gives `mu(x + v + eD) >= b mu(x + eD)` for **every** `e > 0`, hence `p^(x + v) >= b p^(x)` for **every** `x` and **every** `v in D`.
(iii) Averaging the inequality `mu(x+eD) <= b^-1 mu(x+v+eD)` over `v in D`: `2 mu(x+eD) <= b^-1 int |D ∩ (y - x - eD)| dmu(y) <= b^-1 * 2e^2`, so `p^ <= 1/(2b)` everywhere; `M := ess sup p = sup p^ <= 1/(2b) < infinity`. Also `p^ <= M` everywhere (each average is `<= M`).

**3.3 Near-peak diamond.** For `eta in (0,1)`, `{p^ > (1-eta)M}` has positive measure (otherwise `ess sup p <= (1-eta)M`), so pick `x0` in it; by (ii) `p^ >= (1-eta) b M` on all of `x0 + D`, hence `p >= (1-eta) b M` a.e. on `x0 + D`.

**3.4 Floor by even convexity.** `phi(x) = |x|^2 + kappa ||x||_1` is even and convex, so `phi(x0+u) + phi(x0-u) >= 2 phi(u)`; since `D = -D`, `int_{x0+D} phi = int_D phi(x0+u) du = (1/2) int_D [phi(x0+u) + phi(x0-u)] du >= int_D phi = 2/3 + 4 kappa/3 = d = (2+4kappa)/3`.

**3.5 Capped-density weak duality — (6).** Write `p = p1 + p2`, `p1 = (1-eta) b M 1_{x0+D}`, so `0 <= p2 <= M` a.e. and `int p2 = 1 - 2(1-eta) b M =: m2 >= 0`. Then `int phi p1 >= (1-eta) b M d`, and for **any** `T >= 0`:
`int phi p2 = T m2 + int (phi - T) p2 >= T m2 - int (T - phi)_+ p2 >= T m2 - M G(T)`, `G(T) = int (T - phi)_+ dx`.
Adding: `J + kappa L >= T + M[(1-eta) b (d - 2T) - G(T)]`. This is (6), exactly as written, for every `T >= 0`, every `eta in (0,1)`, with the cap `M` legitimately applied to `p2` (the candidate's "residual density has cap M").

**3.6 The root B.** Let `eta -> 0`: `J + kappa L >= T + M[b(d-2T) - G(T)]` for all `T >= 0`. `psi(T) := G(T) + 2bT` is continuous, strictly increasing, `psi(0) = 0`, `psi(T) -> infinity`, so there is a unique `B > 0` with `psi(B) = bd`; at `T = B` the bracket vanishes and `J + kappa L >= B` independently of the unknown `M`. (Choosing `T = B` is the right move: for `T > B` the bracket is negative, for `T < B` it is positive but `M` has no useful lower bound.)

**3.7 Finite inequality.** If the law is feasible, `H := j + kappa ell >= J + kappa L >= B`, so `psi(H) >= psi(B) = bd`, i.e. `b(d - 2H) <= G(H)`. Containment (`|x|^2 >= 0`): `G(H) <= int (H - kappa ||x||_1)_+ dx = int_0^{H/kappa} (H - kappa t) 4t dt = 2H^3/(3 kappa^2)`. If `H < d/2 = (1+2kappa)/3`:
`b <= (2H^3/(3kappa^2)) / ((2+4kappa)/3 - 2H) = H^3 / [kappa^2 (1 + 2kappa - 3H)]`. **Verified.**

**3.8 Pure l1 cost — (3).** Same chain with `phi = ||x||_1`: floor `4/3`, `G(T) = 2T^3/3` exactly, `L >= B`; `ell >= B` gives `2 ell^3/3 + 2b ell >= 4b/3`, i.e. `b <= ell^3/(2 - 3 ell)` for `ell < 2/3`, **for every r** (J is never used). The candidate states it only for `r >= 1/6` (M4).

**3.9 The kappa substitution — (2).** `kappa = 2r/(1-6r) > 0` iff `r < 1/6`. `H = ell (r + kappa) = 3 ell r (1-2r)/(1-6r)`, `1 + 2kappa = (1-2r)/(1-6r)`. Hence `H/(1+2kappa) = 3 r ell = 3j` and `H^3/[kappa^2(1+2kappa)] = 27 r^3 (1-2r)^3 (1-6r)^{-3} * (1-6r)^3 / (4 r^2 (1-2r)) * ell^3 = (27/4) r (1-2r)^2 ell^3 = ell^3 F(r)`. Both are identities of rational functions of `r` (after clearing denominators, polynomial identities of degree `<= 6`; controls §2 check 40 rational points × 3 values of `ell`, more than enough to prove them). `H < (1+2kappa)/3 <=> 3j < 1/3 <=> j < 1/9`. Substituting, `b <= ell^3 F(r) / (1 - 9j)`. **Verified**, including the candidate's remark that nothing singular is hidden as `r -> 0` (both identities are exact for every `r in (0,1/6)`).
Remark (M5): `kappa*` is the stationary point of the leading-order bound `g(kappa) = (r+kappa)^3/(kappa^2(1+2kappa))` (`d log g/d kappa = 0 <=> kappa(1-6r) = 2r`) and `g(kappa*) = F(r)`; for `r >= 1/6` no positive stationary point exists and `g -> 1/2` as `kappa -> infinity`, matching (3). Optimality of `kappa*` is not load-bearing: the lower bound below matches whatever `kappa` gives.

## 4. The private diamond-shell laws

**4.1 Exact shell-index privacy.** `k(x) = min{k >= 0 : x in (a+k)D} = ceil((||x||_1 - a)_+)`. For `v in D`, `| ||x+v||_1 - ||x||_1 | <= 1`, so `|k(x+v) - k(x)| <= 1` for **all** `x, v`. With `p = b^{k}/Z`, `p(y+v) >= b p(y)` pointwise, hence `mu(A+v) = int_A p(y+v) dy >= b mu(A)` for **every** Borel `A` and **every** `v in D`. A genuine member of the class for every `a > 0`, `b in (0,1)`. (Controls §4 exercise the index inequality on a rational grid and show a half-width shell index fails it — the check has teeth.)

**4.2 Geometric moment sums — (7).** With `A_k = |(a+k)D| = 2(a+k)^2`, `Z = sum_k b^k (A_k - A_{k-1}) = (1-b) sum_k b^k A_k` (Abel summation; convergent for `b < 1`), and likewise with `4(a+k)^3/3`, `2(a+k)^4/3`. So `L = (2/3) S_3/S_2`, `J = (1/3) S_4/S_2`, `S_n := sum_{k>=0} b^k (a+k)^n`. Closed forms: `sum_k k^i b^k = N_i(b)/(1-b)^{i+1}`, `N_1 = b`, `N_2 = b(1+b)`, `N_3 = b(1+4b+b^2)`, `N_4 = b(1+11b+11b^2+b^3)`, obtained from `N_{i+1} = b[(1-b)N_i' + (i+1)N_i]` (termwise differentiation); controls §3 derive these polynomials exactly, bracket the closed forms by exact partial sums with an independent tail bound, and confirm the Abel identity for `Z` against the direct shell-area series. **(7) verified.**

**4.3 Lemma E — explicit version of (8), including the relative error in J as b/a^3 -> 0.**
For `0 < a <= 1/100` and `0 < b <= a^3/2` (so `b <= 1/2`):
- tails: `T_n := sum_{k>=2} b^k (a+k)^n <= b^2 sum_{m>=0} 2^{-m} (m+3)^n`, i.e. `T_2 <= 36 b^2`, `T_3 <= 188 b^2`, `T_4 <= 1164 b^2` (values of `sum 2^{-m} m^i`: 2, 2, 6, 26, 150);
- `S_2/a^2 in [1, 1 + 0.52 a]` (`(b/a^2)(1+a)^2 <= 0.5101 a`, `36 b^2/a^2 <= 9 a^4`);
- `S_3/(a^3 + b) in [1, 1 + 3.04 a]` (`(1+a)^3 - 1 <= 3.0301 a`, `188 b <= 94 a^3 <= 0.0094 a`);
- `S_4/b in [1 + a^4/b, 1 + a^4/b + 4.12 a]` (`(1+a)^4 - 1 <= 4.0605 a`, `1164 b <= 582 a^3 <= 0.0582 a`).
Therefore, **uniformly in** `b/a^3 in (0, 1/2]`:
`L in (2/3)(a + b/a^2) * [1 - 0.52 a, 1 + 3.04 a]`,
`J in (b/(3a^2)) * [(1 + a^4/b)/(1 + 0.52 a), 1 + a^4/b + 4.12 a]`, equivalently `J = ((b + a^4)/(3a^2)) (1 + theta)`, `theta in [-0.52 a, 4.12 a]`.
This is the candidate's (8) with constants. The `a^4/b` term is **not** an artefact: as `b/a^2 -> 0` the mass of the inner diamond `aD` tends to 1 and its own second moment `a^2/3` enters `J` additively, so `J - b/(3a^2) ≈ a^2/3` and the relative error is exactly of order `a^4/b`. Controls §7 (exact rationals, `a = 1/100`, `b/a^3` from `1/2` down to `1e-10`) show the residual after removing `a^4/b` stays inside `[-0.52a, 4.12a]` throughout (observed values `0.0345` … `4.05e-10`). The candidate's error term `O(a + a^4/b)` is therefore correct and, in its relative form, sharp; the uniform claim is exactly what makes the `r -> 0` regime work (§5.1).

## 5. Matching constructions — uniform absolute constants and the gamma slack

Put `eta = ell + ell^2/j`, `K = 7`, `gamma = 1 - 7 eta`, and assume `ell <= 1/150`, `eta <= 1/8` (so `gamma >= 1/8 > 0`).

**5.1 Case 0 < r < 1/6 — (9).** `a = gamma (3/2)(1-2r) ell <= 1.5 ell <= 1/100`, `b = gamma^3 ell^3 F(r)`. Exact identities (my recomputation): `b/a^2 = 3 gamma j`, `b/a^3 = 2r/(1-2r) < 1/2` (so Lemma E applies), `a^4/b = gamma (3/4)(1-2r)^2 ell^2/j <= (3/4) ell^2/j`. Lemma E:
`L <= (2/3)(a + 3 gamma j)(1 + 3.04 a) = gamma [(1-2r) ell + 2j](1 + 3.04 a) = gamma ell (1 + 3.04 a) <= (1 - 7eta)(1 + 4.56 ell) ell <= ell`, using `(1-x)(1+y) <= 1` when `y <= x` and `eta >= ell`.
`J <= (b/(3a^2))(1 + a^4/b + 4.12 a) <= gamma j (1 + (3/4) ell^2/j + 6.18 ell) <= (1 - 7 eta)(1 + 6.18 eta) j <= j`.
Both budgets hold (the candidate's "the chosen K makes both inequalities strict": `K = 7` gives `<=`; any `K > 6.18` gives strict). So `b_max >= (1-7eta)^3 ell^3 F(r) >= (1 - 21 eta) ell^3 F(r)`.

**5.2 Case r >= 1/6.** `a = gamma ell <= 1/100`, `b = a^3/2` (`b/a^2 = a/2`, `a^4/b = 2a`). Lemma E: `L <= a(1 + 3.04 a) <= ell` for `K >= 3.04`; `J <= (a/6)(1 + 6.12 a) = (gamma ell/6)(1 + 6.12 ell) <= gamma j (1 + 6.12 eta) <= j` for `K >= 6.12`, using `j >= ell/6`. So again `b_max >= (1-7eta)^3 ell^3 F(r)`.

**5.3 Upper side.** For `r < 1/6`: `j < ell/6 < 1/9`, so (2) applies and `1/(1-9j) <= 1/(1 - 1.5 ell)`. For `r >= 1/6`: (3) gives `ell^3/(2 - 3 ell) = (ell^3/2)/(1 - 1.5 ell)`. In both cases `b_max <= ell^3 F(r)/(1 - 1.5 ell) <= ell^3 F(r)(1 + 2 ell)` for `ell <= 1/6`.

**5.4 Explicit theorem** (as in §1): `1 - 21 eta <= b_max/(ell^3 F(r)) <= 1 + 2 ell <= 1 + 2 eta` for all `(j, ell)` with `ell <= 1/150`, `eta <= 1/8`, all `r > 0`. The candidate's (4), (5) and (11) follow, with universal constants over all `r > 0` in the explicit regime. Note the error is **asymmetric**: the upper side loses only `O(ell)`, the lower side `O(ell + ell^2/j)`; the symmetric `O(eta)` of the candidate is correct, and whether the true `b_max` really carries an `ell^2/j`-order correction is neither claimed nor decided here (M6).

**5.5 Crossing r = 1/6 and oscillation — no hidden order of limits.** Everything in 5.1–5.3 is a bound for one fixed pair `(j, ell)`, with constants that do not depend on `r`; the two branches are selected by the value of `r` for that pair alone. Hence for a sequence `(j_n, ell_n)` with `ell_n -> 0`, `ell_n^2/j_n -> 0`, the two-sided bound holds termwise as soon as `ell_n <= 1/150` and `eta_n <= 1/8`, however `r_n` behaves (tiny, huge, oscillating across `1/6`, equal to `1/6`). No continuity of `F` is used (it is continuous at `1/6` anyway: `(27/4)(1/6)(2/3)^2 = 1/2`), and the two constructions even coincide in the limit `r -> 1/6-` (`a -> gamma ell`, `b/a^3 -> 1/2`). The candidate's claim "require neither subsequences nor previously claimed mixed-objective optimality" is correct. Controls §6 run exact rational adversarial sequences: `r -> 0` with `ell^2/j = 10^-m` (m = 2..6) and the regime edge `r = 1e-9`, `ell = 1e-10` (`eta = 0.1`); `r = 1/6 ± 10^-m` with `ell = 10^-m` (m = 3..7); `r = 1/6` exactly; and an oscillating cycle `{10^-m, 1/6 - 10^-m, 1/6, 1/6 + 10^-m, 1000, 10^-m}` for `ell = 10^-2m`, m = 3..5. In every case the constructed law is exactly feasible (`J <= j`, `L <= ell` in rational arithmetic), `b <= a^3/2`, Lemma E's explicit interval holds, `1 - gamma^3 <= 21 eta`, and the upper gap `<= 2 ell`. The ratio (constructed `b`)/(bound) runs from `0.80` at `eta = 0.0101` to `0.99999998` at `eta = 7e-10`, and along sequence A `(1 - b/upper)/eta -> 21.000` (the loss is exactly my `(1-7eta)^3` slack, as predicted).

## 6. Controls — what was run once and what it shows

All sections exact (`fractions.Fraction`) unless stated; receipt in §0.

| § | control | outcome |
|---|---|---|
| 1 | `F(1/24)=121/512`, `F(1/12)=25/64`, `F(1/9)=49/108`, `F(1/6)=1/2`; left value at `1/6` equals `1/2` | PASS (exact) |
| 2 | `H/(1+2kappa)=3j`, `H^3/(kappa^2(1+2kappa))=ell^3F(r)` at 40 rationals × 3 `ell`; `g(kappa*)=F(r)`, `g>=F(r)` at perturbed `kappa`; `H<(1+2kappa)/3 <=> j<1/9` at `j = 1/9 ± 1e-9, 1/9` | PASS |
| 3 | Eulerian numerators derived by exact polynomial recurrence equal `[0,1],[0,1,1],[0,1,4,1],[0,1,11,11,1]`; `(1+m)^4 <= 1000(4/3)^m` (m<=100, decreasing for m>=13) giving the independent tail bound `3000 b^{K+1}(a+K+1)^4`; closed forms inside `[P_K, P_K + tail]` at 6 `(a,b)` × n = 2,3,4; direct shell-area series brackets `2(1-b)S_2` | PASS |
| 4 | shell index `|k(x+v)-k(x)|<=1` on 43² grid × 61 diamond shifts; **negative**: half-width index violates it | PASS / expected violation found |
| 5 | finite (2) and (3) at the laws' own exact `(J,L)` for 80 shell laws (9 / 29 applicable) and all same-`b` two-shell mixtures at weights 1/4,1/2,3/4 (53 / 332 applicable); max `b/bound(2)` on grid 0.4958 | PASS, zero violations |
| 6 | explicit `K=7` construction on sequences A, A-edge, B, C, `r=1/6`, D (34 cases): exact feasibility, Lemma E interval, `1-gamma^3<=21eta`, upper gap `<=2ell`, `b<=a^3/2`; rate `(1-b/upper)/eta -> 21` | PASS all 34 |
| 7 | `J` relative error at `a=1/100`, `b/a^3 in {1/2,1/10,1e-2,1e-4,1e-6,1e-10}`: residual after removing `a^4/b` within `[-0.52a, 4.12a]` | PASS |
| 8 | scope boundary `j = ell^2` (`eta > 1`): the `gamma = 1` shell has `J/j = 1.7530, 1.7503, 1.75003` (infeasible, as the `a^4/b ≈ 3/4` term predicts); (2) still holds for that genuine law at its own `(J,L)` | PASS (theorem makes no claim there; (2) unviolated) |
| 9 | **negative** controls: a `0.98×` tightened (2) is violated by a genuine feasible law at `eta ≈ 1e-5` (`b/fake = 1.0202`); the non-private uniform law on `aD` with pretended `b = a^3` is rejected by (2) (`bound = 9.8e-9` vs `1e-6`); a mutated Eulerian polynomial fails the partial-sum bracket | PASS (all three mutations detected) |
| 10 | mpmath 60 dps, **numeric control only**: exact mixed `G_kappa(T)` (first-quadrant disc region) reproduces `pi T^2/2` as `kappa -> 0` (rel 3e-25) and `2T^3/(3kappa^2)` as `T/kappa^2 -> 0` (rel 1e-8); containment at 9 `(T,kappa)`; on 5 shell laws × `kappa in {0.1,1,10}` the dual consequences `b(d-2H) <= G_kappa(H)` and `J + kappa L >= B` (B by 200-step bisection) hold; along the `K=7` construction at `r=1/50`, `G(H)/(b(d-2H)) - 1 ≈ 0.11 eta` (`0.00375, 5.5e-4, 5.6e-5, 5.6e-6` for `ell = 1e-3..1e-6`) | PASS; dual (6) consistent and nearly tight even with the exact (non-contained) `G` |

Nothing in these controls is a proof; the proofs are §§3–5. The controls would have refuted the candidate if (a) any genuine private law violated (2)/(3) at its own `(J, L)`, (b) the explicit construction failed a budget, or (c) the exact dual consequence failed for any `(law, kappa)` — none occurred, and the negative controls show each check detects a planted defect.

## 7. Findings

- **M1 (MINOR, presentation).** The ambient dimension (`R^2`) is never stated; every constant (`d = (2+4kappa)/3`, `4/3`, `2T^3/3`, (7)) is dimension-specific. One sentence fixes it.
- **M2 (MINOR, gap in exposition, closable).** §2 of the candidate asserts "the all-point density representative … is bounded" without proof. Absolute continuity, existence of a representative satisfying the all-point inequality `p^(x+v) >= b p^(x)` for every `x, v in D`, and `M <= 1/(2b)` are needed and are proved in my §3.1–3.2 (Lebesgue differentiation along shrinking diamonds + averaging over `D`). Nothing else is missing from the dual argument.
- **M3 (MINOR, explicitness).** "small a", "sufficiently large absolute K", "eventually", and "universal over all r>0 in this regime" are never quantified, so the regime in which the universal constants are claimed is undefined in the text. Supplied here: `a <= 1/100`, `K = 7`, regime `ell <= 1/150`, `eta <= 1/8`, constants `21 eta` (lower) and `2 ell` (upper); verified exactly in 34 cases.
- **M4 (MINOR, understatement).** (3) is proved for every `r` (its derivation never uses `J`) but is stated "if r >= 1/6". Harmless; stating it for all `r` would also make clear that (2) and (3) are both available for `r < 1/6`.
- **M5 (MINOR, wording).** "exact optimizing weight kappa = 2r/(1-6r)" — `kappa*` minimises the leading-order bound `(r+kappa)^3/(kappa^2(1+2kappa))`, not necessarily the finite bound `H^3/(kappa^2(1+2kappa-3H))`. Not load-bearing (the lower bound matches), but the adjective invites misreading.
- **M6 (MINOR, statement form / scope).** (4)–(5) are phrased as limit statements ("if ell->0 and ell^2/j->0 … O(…)"), whereas the proof delivers a pointwise explicit inequality; the pointwise form should be the theorem (it is what makes "possibly nonconvergent r" automatic). Relatedly, the error is asymmetric (upper `O(ell)`, lower `O(ell + ell^2/j)`); the text should say that sharpness of the `ell^2/j` term for the true `b_max` is not established. Outside the regime (`ell^2/j` bounded away from 0) the lower construction genuinely fails (controls §8: `J/j ≈ 1.75` at `j = ell^2`), so the hypothesis is used, not decorative.

No defect was found in (1), (2), (3), (6), (7), (8), (9), (10), (11), the rational sample values, or the `r = 1/6` crossing. The candidate's own disclaimers (not formal, not reviewed, not an exact finite-`b` optimum, not a novelty claim) are consistent with what the text proves.

## 8. Limitations of this review

Same-harness review: not human review, not an independent model family, not a kernel/formal check, and no novelty assessment (no literature was consulted, by assignment). The exact controls cover finitely many rational points; the uniform statements rest on the written proofs in §§3–5, which I reconstructed independently but which have not been machine-checked. The high-precision §10 control is numeric (mpmath quadrature + bisection) and is reported as consistency, not proof. I did not read the earlier frozen file the candidate references and make no claim about dependence chains between the two files. No author contact occurred; no artifact outside this review directory was created or modified (the local scratch copy of the script used for a one-line cosmetic edit before placement is session-scoped and not part of the record).

**Post-write note:** the pre-write clock at the top is the last clock observed before this file was composed; the placement clock is recorded by the parent's filesystem timestamps and in my hand-off message, not retyped here.
