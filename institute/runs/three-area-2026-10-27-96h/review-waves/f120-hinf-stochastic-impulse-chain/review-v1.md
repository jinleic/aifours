# f120 review-v1 — stochastic impulse-chain necessary lower bound (INDEPENDENT_SAME_HARNESS_SCIENTIFIC_REVIEW)

Reviewer: same-harness subagent (Claude, omp). Observed clock before this write: 2026-10-29T02:59:14Z (2026-10-28T19:59:14-0700 PDT).
Manifest: `review-waves/f120-hinf-stochastic-impulse-chain/manifest-v1.json`, live SHA256 `9f7742ffda70f4e77332992cf7467a34df79d56637aec7bf0668c7dddb0dead8` (matches assignment), verified 2026-10-29T02:38:36Z.
Authority read: `contract-addendum-2-frontier-first-owner-direction-v1.json` (14 LF, procedural only).

This review is same-harness: it is not human, independent-model-family, kernel/formal, or novelty clearance. Everything below is my own reconstruction from the six frozen inputs; the repaired proof in §4 is mine and has not been read by any other family.

## 0. Verdict (summary)

| Item | Candidate claim | Status after review |
|---|---|---|
| (2) LF28: `gamma1, gamma2 >= sup_{a!=0} L(a)/||a||` for every fixed law in the registered class, all real matrices, `T>h>=0`, `S=T-h>0`, scalar Brownian driver | lower bound via pulse family | **TRUE** — complete written proof reconstructed in §4 (same-harness). Author's own text proves it only up to the stochastic limit step (LF43), which is a correct *sketch*, not a proof: **MAJOR as written, repaired here.** |
| (3) LF49-51: if some unit top singular vector `a*` of `B_n` has `O G_j(a*) != 0` for some `j`, then `L(a*) > delta = ||B_n||`, hence `gamma1, gamma2 > delta` | strict gap | **TRUE**; proof §5 (and the condition can be weakened — Prop. 5.2; exact counter-instance NC3 where `OG=0` but the gap persists). |
| §5 LF57-61: `h=0, T=1, dx = w dW, z = w + x`: `L(1) = E sqrt(1+xi^2) > 1 = delta` | h=0 physical counterexample to threshold equality | **TRUE and exact**: `L(1) = e^{1/4}[K_0(1/4)+K_1(1/4)]/(2 sqrt(2 pi)) = 1.35453080648131530205…` (closed form derived §6.1, three independent numerical routes agree to 1e-17); strict `>1` proved analytically; finite-ε mechanism verified exactly (§6.1). |
| Source 3 (E1 state-sup bound, imported) | `E||z|| <= C_up E||w||` for E1 inputs | Reconstructed and **correct** (§3.1), including the L1 Hilbert martingale inequality with constant 8 and both localizations. Not load-bearing for the candidate's deterministic-pulse argument (F6). |
| Source 4 (delay-chain pulse algebra, imported) | `gamma1, gamma2 >= ||B_n||` | Reconstructed and **correct** (§3.2); exact `B_2^T B_2 = [[2,-1],[-1,2]]` check reproduced with Fractions. |

Overall classification: **MAJOR (proof incompleteness at LF43, repaired in this review; no FATAL; no false statement found).** The theorem statements (2), (3) and §5 are, to my checking, true with the exact scope in §8. Adoption should bind the repair (§4) together with the candidate, and the repair itself still needs the parent's hand check and the second configured family; my saying it is complete is same-harness evidence only.

Boundary notice: during the review Main informed me that a later source-owner "flow/stable-convergence addendum" exists outside manifest-v1. I did not open it, and nothing from it is used; this verdict is for the frozen six-input scope only.

## 1. Inputs read in declared order, whole-file verification (live `shasum -a 256`, `wc -c`, LF count, 2026-10-29T02:38:49Z)

| # | role | path (repo-relative to `/Users/jinleic/repos/aifours/`) | SHA256 | bytes | LF | match |
|---|---|---|---|---|---|---|
| 1 | literal expectation criterion | `institute/runs/three-area-2026-10-27-96h/written-releases/info-3-literal-criterion-definitions-v1.md` | `891ab168…633fad` | 2000 | 29 | yes |
| 2 | registered linear preview class | `…/written-releases/info-3-linear-preview-class-definitions-v1.md` | `9b72aca5…9151cd` | 1087 | 11 | yes |
| 3 | all-matrix E1 state-sup bound | `information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-all-matrix-preview-explicit-e1-gain-bound.txt` | `7130be25…0eb21` | 7650 | 112 | yes |
| 4 | finite delay-chain lower bound | `…/frontier-20261028-all-matrix-delay-chain-literal-gain-lower-bound.txt` | `8f0ac328…288011` | 5360 | 73 | yes |
| 5 | **candidate** | `…/frontier-20261028-stochastic-impulse-chain-gain-lower-bound.txt` | `c165f2df…093f76` | 7327 | 67 | yes |
| 6 | author MC diagnostic (read only; never executed/imported) | `…/frontier-20261028-stochastic-impulse-lower-check.py` | `102e4cc6…2970f` | 1374 | 34 | yes |

All six were read completely with `:raw` line selectors (no context bleed). Full hashes are in the manifest and were reproduced digit-for-digit by the live run.

Notation (candidate LF9-13): `P=A+BK, Q=A0+B0K, O=D0+D1K, E0=D1L0, Eh=D1Lh, G0=B0L0, Gh=B0Lh`; additionally from Source 3: `F0=BL0, Fh=BLh+C, F(r)=BH(r), G(r)=B0H(r), E(r)=D1H(r)`. Closed loop: `dx=(Px+f)dt+(Qx+g)dW, z=Ox+o` with `f=F0 w_t+Fh w_{t-h}+∫_0^h F(r)w_{t-r}dr`, likewise `g`, `o`. Criterion (input 1, LF16): `E||z||_{L2[0,T]} / E||w||_{L2[0,S]} < gamma`, expectation OUTSIDE the path norm, `S=T-h`. For deterministic `w`, `E||w|| = ||w||`, so one pulse family bounds both `gamma1` (E1 sup) and `gamma2` (E2 sup).

## 2. What the assignment asked me to attack, and where each item lands

| attack point | result | where |
|---|---|---|
| deleted-increment independence / time change | correct: off-window increments form `B_{c_ε(t)}` with `B` a Brownian motion independent of all `xi_j^ε` (jointly Gaussian, zero covariance); the time change is handled exactly, not asymptotically, by a measure-preserving clock | §4 Step 4 |
| convergence of noncommuting linear Itô flows with impulse marks | no commutativity needed; L2 continuity of `Φ_t Ψ_s` in the jump time `s` (`Ψ=Φ^{-1}`), moments of fundamental matrices | §4 Step 6 |
| L2 remainder estimates | written out with the uniform-in-ε second-moment bound; all `O(ε)` in `L2(Ω)` | §4 Steps 1, 3, 5 |
| distributed `H` terms | Young `L2*L1`: `||K*w_ε||_{L2} <= ||K||_{L2[0,h]} ||w_ε||_{L1} = O(sqrt ε)` for `K∈{F,G,E}`; on-window lag argument of Source 4 also verified | §3.2, §4 Step 2 |
| uniform integrability | not needed: the repair gives `L1` convergence to equal-law copies; only finite second moments are used | §4 Step 7 |
| impulse times at endpoints / `h=0` | `t_0=0` (jump = initial post-pulse state), `t_n = nh < T` strictly, `nh+ε <= T` iff `ε <= S-(n-1)h`; `h=0` is one window, taps combined per input 2 | §3.2, §4 Step 8 |
| strict observation `OG_j != 0` | correct; actually gives energy `>0` a.s., not just w.p.p.; weakened to `P(alpha_j>0)>0` with `alpha_j=∫_{t_j}^T||OΦ(r,t_j)G_j||²dr`; exact `OG=0` gap example NC3 | §5 |
| ratio is `E||z||/E||w||`, not RMS | respected throughout; Jensen gives `L(a) <= sqrt(c²+tr M)` (the RMS impulse functional), strict unless the energy is a.s. constant | §6 |
| deterministic E2 pulses sufficient for the bound, not for sharp gain/synthesis | yes; exact control D1 (`dx=w dt, z=x+w`): impulse bound 1, actual ratio of `w≡1` is `sqrt(7/3)=1.5275…`; NC2: `sup_a L(a)/||a|| = delta` although `gamma=delta` is infeasible by attained equality | §6.3 |

## 3. Reconstruction of the two imported dependencies

### 3.1 Source 3 — explicit E1 state-sup bound (LF1-112). Verdict: correct.

**(5) L1 martingale inequality, constant 8 (LF62-77).** Let `M` be a continuous `R^d`-valued local martingale, `M_0=0`, `M*=sup_{t<=T}||M_t||`, `[M]` the scalar bracket. Fix `λ>0`; `τ=inf{t: ||M_t||>=λ}`, `σ=inf{t>=τ: ||M_t-M_τ||>=λ}`, `v=inf{t: [M]_t>λ²/4}` (strict exceedance; see remark). Put `N_t=M_{t∧σ∧v}-M_{t∧τ∧v}`. `N` is a continuous local martingale with `N≡0` on `{τ>T}` for `t<=T`, and `[N]_T <= [M]_{v}-[M]_{τ∧v} <= λ²/4`, so `N` is an L2-bounded martingale with `E||N_T||² = E[N]_T <= (λ²/4) P(τ<=T) = (λ²/4) P(M*>=λ)`. On `A={M*>2λ, [M]_T<=λ²/4}`: by continuity `τ<T`; at the time where `||M||>2λ`, `||M-M_τ||>λ`, so `σ<=T`; and `[M]_σ<=λ²/4` gives `σ<=v`; hence `||N_T||=||M_σ-M_τ||=λ` on `A`, and `λ² P(A) <= E||N_T||²`. Therefore `P(M*>2λ) <= P(sqrt([M]_T)>λ/2) + (1/4)P(M*>=λ)`. Integrating `dλ` on `(0,∞)`: `(1/2)E M* <= 2 E sqrt([M]_T) + (1/4) E M*`; if `E M*<∞` this is `E M* <= 8 E sqrt([M]_T)`. Localization exactly as the source says (LF77): stop at `ρ_K=inf{t:[M]_t>=K}`; then `M^{ρ_K}` is L2-bounded, Doob gives `E (M^{ρ_K})* < ∞`, the inequality holds for `M^{ρ_K}`, and `K↑∞` with monotone convergence (`ρ_K↑∞` a.s. because `[M]_T<∞` a.s.) gives (5) for `M`. No `E[M]_T<∞` is used. ✔ Remarks (non-blocking): the source's "first time [M] reaches λ²/4" should be read as strict exceedance (or note that `{λ: P([M]_T=λ²/4)>0}` is countable); the `>=`/`>` choices in `τ` are immaterial after integration. The inequality applies to the needed stochastic integrals because they are continuous local martingales after the state stopping.

**(6) Block recurrence (LF79-101).** With `t_i=min(iδ,T)`, `Z_i=sup_{t<=t_i}||x_t||`, state stopped at `τ_R=inf{t:||x_t||>=R}` so `Z_i^R<=R`: on block `i`, `sup_{block}||x_t|| <= ||x_{t_{i-1}}|| + ||P||δ Z_i + sqrt(δ)||f||_{L2} + M*_block` with `M_t=∫_{t_{i-1}}^{t} 1_{s<=τ_R}(Qx+g)dW`; by (5), `E M*_block <= 8E sqrt(∫_block||Qx+g||²) <= 8||Q||sqrt(δ) E Z_i + 8 E||g||_{L2}`. Using (2) of the source (`||f||_2<=a_d||w||_2`, `||g||_2<=a_s||w||_2`, `||o||_2<=a_o||w||_2` — all pathwise Minkowski/Young, valid because `∫_0^h||H||dr <= sqrt(h)||H||_{L2}<∞` and the zero extension gives `||w(·-h)||_{L2[0,T]}=||w||_{L2[0,S]}`): `E Z_i^R <= E Z_{i-1}^R + α E Z_i^R + A_block E||w||_2`, `α=||P||δ+8||Q||sqrt δ <= 1/2`, `A_block = sqrt(δ)a_d+8a_s`. Since `E Z_i^R <= R < ∞` the subtraction is legitimate: `E Z_i^R <= (1-α)^{-1}[E Z_{i-1}^R + A_block E||w||_2]`, and summing with `Z_0=0`: `E Z_N^R <= A_block E||w||_2 Σ_{k=1}^N (1-α)^{-k} = A_block R(α,N) E||w||_2` with `R(α,N)=((1-α)^{-N}-1)/α` (`=N` at `α=0`) — I checked the geometric identity `Σ_{k=1}^N r^k = (r^N-1)/α` for `r=(1-α)^{-1}`. `R↑∞`: the linear SDE with pathwise-L2 progressive forcing has a global strong solution (variation of constants with the fundamental matrix), so `τ_R↑∞` and monotone convergence gives (6). Then `E||z||_2 <= ||O||sqrt(T) E Z_N + a_o E||w||_2 <= C_up E||w||_2` (LF97-100) with `C_up` exactly as in (4). ✔ The worked `δ` choice gives `α<=1/4+1/4`. ✔ The E1-not-E2 test input `exp(W_t²/3)` claims (LF108) are correct Gaussian-tail facts (`E e^{aW_t²}=(1-2at)^{-1/2}` for `2at<1`, `=∞` otherwise, so `E||w||²_2=∞` from `t>=3/4`; `E exp((sup|W|)²/3)<∞` by reflection since `1/3<1/2`). The source's sampled numbers (LF106: `C_up≈3.16e19`, ratio `0.402`) were not re-run and are not evidence of anything, as the source says.

Role for f120: Source 4 and the candidate only need *some* finite uniform state bound for deterministic pulses; for deterministic `f,g` the standard E2 estimate (Lemma 4.1 below) already supplies `E sup||x||² <= C(||f||²_2+||g||²_2)`, so the E1 machinery is not load-bearing here (F6). It is nevertheless correct.

### 3.2 Source 4 — finite delay-chain pulse algebra (LF1-73). Verdict: correct (§§1-2, 4 load-bearing; §3 checked, not load-bearing).

Pulses `w_ε = ε^{-1/2} a_j` on `[jh, jh+ε]`, `0<=j<n`, `n=ceil(S/h)`, `ε<h/2`, `ε<S-(n-1)h`. Geometry: `t_{n-1}+ε <= S` and `t_n+ε <= T` are both the same condition `ε <= S-(n-1)h = T-nh` (I verified `nh<S+h=T` and `(n-1)h<S`); windows are disjoint for `ε<h`. `||w_ε||_2=||a||` exactly. On output window `j` (`0<=j<=n`): `w_ε(t)=ε^{-1/2}a_j`, `w_ε(t-h)=ε^{-1/2}a_{j-1}` (`a_{-1}=a_n=0`), so the direct atoms equal `ε^{-1/2}D_j`, `D_j=E0a_j+Eh a_{j-1}`, with exact window path norm `sqrt(Σ_j||D_j||²)=||B_n a||`. Kernel on windows: for `t` in window `j`, `w_ε(t-r)!=0` forces `r∈[(j-k)h-ε,(j-k)h+ε]∩[0,h]`, i.e. `r∈[0,ε]∪[h-ε,h]` when `ε<h/2`; Minkowski gives `||∫E(r)w_ε(·-r)dr||_{L2(windows)} <= [∫_0^ε||E||+∫_{h-ε}^h||E||]·||a|| → 0` (absolute continuity). State on windows: `E||Ox||_{L2(windows)} <= ||O||sqrt((n+1)ε)·E sup||x|| → 0`. Reverse triangle on the windows and `E||z||_{L2[0,T]} >= E||z||_{L2(windows)}`: `liminf_ε E||z(w_ε)||/||a|| >= ||B_n a||/||a||`; strictness `gamma > ratio` for every `ε` yields `gamma >= ||B_n||` (equality not excluded — correctly left open). At `h=0` the two atoms coincide: `||E0+Eh||`. ✔ Exact check LF63-69: `B_2=[[1,0],[-1,1],[0,-1]]`, `B_2^TB_2=[[2,-1],[-1,2]]`, eigenvalues 3,1 — reproduced exactly with Fractions in my run (instance S2, field `BtB_exact`). ✔ §3 (small-delay limit `max_θ||E0+e^{iθ}Eh||`, Parseval upper bound and phased test vectors) is consistent with my own derivation but is not used by f120.

## 4. Complete written proof of (2) — repair of the stochastic limit step (candidate LF34-45)

Fix the law, `h>0` (for `h=0` see Step 8), `a=(a_0,…,a_{n-1})`, `n=ceil(S/h)`, `t_j=jh`, windows `I_j^ε=[t_j,t_j+ε]`, `s_j=t_j+ε`, `0<=j<=n`, `ε<h/2`, `ε<S-(n-1)h`. Write `Win=∪_{j=0}^n I_j^ε`, `Off=[0,T]\Win`, `κ_ε=||w_ε||_{L1}=sqrt(ε)Σ_j||a_j||`, and define the kernel forcings `k_f=F*w_ε`, `k_g=G*w_ε`, `k_o=E*w_ε` (convolutions over `[0,h]` with zero-extended `w_ε`). Then, by Young (`||K*w||_{L2} <= ||K||_{L2[0,h]}||w||_{L1}`, which only needs `H∈L2`):

 (4.0) `||k_f||_{L2[0,T]} <= ||F||_{L2}κ_ε`, `||k_g||_{L2} <= ||G||_{L2}κ_ε`, `||k_o||_{L2} <= ||E||_{L2}κ_ε`, all `O(sqrt ε)` deterministic.

On `I_j^ε`: `f=ε^{-1/2}F_j+k_f`, `g=ε^{-1/2}G_j+k_g`, `o=ε^{-1/2}D_j+k_o`, with `F_j=F0a_j+Fh a_{j-1}`, `G_j=G0a_j+Gh a_{j-1}`, `D_j=E0a_j+Eh a_{j-1}`. On `Off`: `f=k_f`, `g=k_g`, `o=k_o` (both taps vanish off the union of output windows). Put `c=||B_n a||=sqrt(Σ_j||D_j||²)` and `ξ_j^ε=ε^{-1/2}(W_{s_j}-W_{t_j})`, i.i.d. `N(0,1)` (disjoint windows).

**Lemma 4.1 (uniform second moment; standard).** For deterministic `f,g∈L2[0,T]`, the strong solution of `dx=(Px+f)dt+(Qx+g)dW`, `x_0=0`, satisfies `E sup_{t<=T}||x_t||² <= C_0 (||f||²_{L2}+||g||²_{L2})` with `C_0=C_0(P,Q,T)`; with an `F_s`-measurable square-integrable initial value `x_s` on `[s,T]`: `E sup_{[s,T]}||x||² <= C_0'(E||x_s||²+||f||²_{L2}+||g||²_{L2})`. Proof: `||x_t||² <= 3||x_s||²+3||∫_s^t(Px+f)||²+3||∫_s^t(Qx+g)dW||²`; `E sup` of the drift term `<= 6T(||P||²∫E sup||x||² + ||f||²)`, of the martingale term `<= 24(||Q||²∫E sup||x||² + ||g||²)` (Doob L2, after the usual localization/Fatou, moments being finite by the variation-of-constants formula); Gronwall. ∎ Applied to `x_ε` with (4.0) and `||f_ε||_2<=a_d||a||`, `||g_ε||_2<=a_s||a||` (Source 3 (2)):

 (4.1) `m := sup_{ε} E sup_{t<=T}||x_ε(t)||² <= C_0(a_d²+a_s²)||a||² < ∞.`

**Step 2 (output on windows).** `z_ε=Ox_ε+ε^{-1/2}D_j+k_o` on `I_j^ε`, and `||ε^{-1/2}D_j||_{L2(I_j^ε)}=||D_j||`, so by the triangle inequality in `L2(Win)`:

 (4.2) `| ||z_ε||_{L2(Win)} - c | <= ||Ox_ε||_{L2(Win)}+||k_o||_{L2(Win)} <= ||O||sqrt((n+1)ε) sup||x_ε|| + ||E||_{L2}κ_ε`, whose expectation is `O(sqrt ε)` by (4.1).

On `Off`: `z_ε=Ox_ε+k_o`, so

 (4.3) `| ||z_ε||_{L2(Off)} - ||Ox_ε||_{L2(Off)} | <= ||E||_{L2}κ_ε`.

**Step 3 (in-window increment).** For each `j`,
 `x_ε(s_j)-x_ε(t_j) = G_jξ_j^ε + R_j^ε`, `R_j^ε := ∫_{I_j}Px_ε dt + sqrt(ε)F_j + ∫_{I_j}k_f dt + ∫_{I_j}Qx_ε dW + ∫_{I_j}k_g dW`,
and, using Itô isometry for the last two terms and (4.0), (4.1),

 (4.4) `E||R_j^ε||² <= 5[ ||P||²ε² m + ε||F_j||² + ε||F||²_{L2}κ_ε² + ||Q||²ε m + ||G||²_{L2}κ_ε² ] = O(ε).`

(This is the candidate's LF41 sentence "the actual state increment equals `G_j ξ_j^ε` plus an L2 error tending to zero", now with the explicit bound; "O(sqrt ε)" and "O(ε)" for the `Qx`, `Px` parts are `||Q||sqrt(εm)` and `||P||ε sqrt m` in `L2(Ω)`.)

**Step 4 (deleted increments: an exact time change and an independent Brownian motion).** Let `c_ε(t)=t-|[0,t]∩Win|` (the paused clock), `T̄=c_ε(T)=T-(n+1)ε`, and `V_t=∫_0^t 1_{Off}(s)dW_s`. `V` is a continuous Gaussian martingale with deterministic bracket `c_ε(t)`, constant on each window; `B_r := V_{c_ε^{-1}(r)}` (right-continuous inverse) is a standard Brownian motion on `[0,T̄]` with `V_t=B_{c_ε(t)}`. The family `(B, ξ_0^ε,…,ξ_n^ε)` is jointly Gaussian (all are L2 limits of linear combinations of increments of `W`) and `Cov(B_r, ξ_j^ε)=ε^{-1/2}∫ 1_{Off}1_{I_j^ε}=0`, hence `B` is independent of `(ξ_j^ε)_j`. (This is the candidate's LF43 claim, made exact: the clock is not "approximately `t`", it is a measure-preserving bijection `Off → [0,T̄)` up to endpoints, with `c_ε(t)=t-(j+1)ε` on the off-interval `J_j=[s_j,t_{j+1})`, `J_n=[s_n,T]`.)

Let `Φ` be the fundamental matrix of `dΦ=PΦ dr+QΦ dB_r`, `Φ_0=I`, and `Ψ=Φ^{-1}` (which solves `dΨ=Ψ(Q²-P)dr-ΨQ dB`). For jump times `τ=(τ_0,…,τ_n)⊂[0,T]` and marks `G_jξ_j^ε` define the cadlag impulse process

 `X^{(τ)}_r = Σ_{j=0}^n 1_{r>=τ_j} Φ_rΨ_{τ_j}G_jξ_j^ε`,

which between jumps solves `dX=PXdr+QXdB` and jumps by `G_jξ_j^ε` at `τ_j`. Two instances:
 • `X̄ := X^{(r^ε)}` with `r_j^ε := c_ε(t_j)=c_ε(s_j)=jh-jε` on `[0,T̄]` (the comparison process), and
 • `X^{a,ε} := X^{(t)}` with `t_j=jh` on `[0,T]`. Because `B ⊥ (ξ^ε_j)` and the `ξ^ε_j` are i.i.d. `N(0,1)`, **`X^{a,ε}` has exactly the law of the candidate's `X^a` for every `ε`**, so `Y^ε := sqrt(c²+∫_0^T||OX^{a,ε}_r||²dr)` satisfies `E Y^ε = L(a)` for every `ε`.

On `J_j` put `X̂_t := X̄_{c_ε(t)}`. Since `B_{c_ε(t)}-B_{c_ε(s_j)}=W_t-W_{s_j}` on `J_j`, `X̂` solves `dX̂=PX̂dt+QX̂dW_t` on `J_j`, with `X̂(s_j)=X̄_{r_j^ε}=X̄_{r_j^ε-}+G_jξ_j^ε` and `X̄_{r_j^ε-}=lim_{t↑t_j}X̂_t` (`=0` for `j=0`). Also `||OX̂||²_{L2(Off)}=∫_0^{T̄}||OX̄_r||²dr` exactly (change of variables `r=c_ε(t)`).

**Step 5 (off-window error recursion).** Let `e=x_ε-X̂` on `Off`. On `J_j`, `de=(Pe+k_f)dt+(Qe+k_g)dW` (atoms vanish off windows), with `e(s_j)=e(t_j-)+R_j^ε` where `e(t_j-)=lim_{t↑t_j}e(t)` (`:=0` for `j=0`) — this is Step 3 together with `X̂(s_j)-X̂(t_j-)=G_jξ_j^ε`. Lemma 4.1 (second form) gives `E sup_{J_j}||e||² <= C_0'(E||e(s_j)||²+||k_f||²_2+||k_g||²_2) <= C_0'(2E sup_{J_{j-1}}||e||²+2E||R_j^ε||²+(||F||²_2+||G||²_2)κ_ε²)`. Induction over `j=0..n` (n fixed, `ε→0`), with (4.4) and (4.0):

 (4.5) `E||e||²_{L2(Off)} <= T·max_j E sup_{J_j}||e||² = O(ε).`

(This is the candidate's LF41 "Between windows, ordinary linear SDE L2 stability shows that the state is close in L2(Ω×time) to the homogeneous impulse process with the same pulse normals" — but with the comparison process now specified: it is `X̂`, driven by the deleted-increment Brownian motion and jumping at window ends, not a process driven by the full-clock `W` jumping at `t_j`, which would not even be adapted (F2).)

**Step 6 (jump-time and horizon continuity; noncommuting `P,Q` allowed).** Standard moment facts for constant-coefficient linear SDEs: `sup_{r<=T}(E||Φ_r||⁴+E||Ψ_r||⁴)<∞` and `E||Ψ_τ-Ψ_σ||⁴ <= C_1|τ-σ|²` (Gronwall + BDG(4) for `∫ΨQ dB`). Since `ξ_j^ε ⊥ (Φ,Ψ)` with `E(ξ_j^ε)²=1`,
 `E∫_0^{T̄}||O(X̄_r-X^{a,ε}_r)||²dr <= 2(n+1)||O||² Σ_j ||G_j||² [ ∫_0^T E||Φ_r(Ψ_{r_j^ε}-Ψ_{t_j})||²dr + ∫_{r_j^ε}^{t_j} E||Φ_rΨ_{t_j}||²dr ]`
 `<= C_2 Σ_j |t_j-r_j^ε| = C_2 ε Σ_j j → 0`,
using Cauchy–Schwarz `E||Φ_r(Ψ_τ-Ψ_σ)||² <= (E||Φ_r||⁴)^{1/2}(E||Ψ_τ-Ψ_σ||⁴)^{1/2}`. Likewise `E∫_{T̄}^T||OX^{a,ε}_r||²dr <= (n+1)ε·sup_r E||OX^{a,ε}_r||² → 0`. No commutation of `P` and `Q` is used anywhere; the Doss–Sussmann transform mentioned at LF43 is an alternative route, not needed (F3).

**Step 7 (assembly: L1 convergence to an equal-law copy).** Let `Y_ε := ||z_ε||_{L2[0,T]} = sqrt(||z_ε||²_{L2(Win)}+||z_ε||²_{L2(Off)})`. Since the Euclidean norm on `R²` is 1-Lipschitz, `|sqrt(u²+v²)-sqrt(u'²+v'²)| <= |u-u'|+|v-v'|` for nonnegative arguments, so

 `E|Y_ε - Y^ε| <= E| ||z_ε||_{L2(Win)} - c | + E| ||z_ε||_{L2(Off)} - ||OX^{a,ε}||_{L2[0,T]} |`
 `<= (4.2) + (4.3) + ||O||·E||e||_{L2(Off)} + ||O||·E||X̄-X^{a,ε}||_{L2[0,T̄]} + E||OX^{a,ε}||_{L2[T̄,T]}`
 `→ 0`

by (4.2)–(4.5) and Step 6 (each `E||·||_{L2}` is bounded by the square root of the second moment). Hence `E||z_ε||_{L2[0,T]} = E Y_ε → E Y^ε = L(a)`. In particular the **limit** exists (not only a liminf). Neither convergence in distribution nor uniform integrability is needed, which disposes of the LF43/LF45 route by a stronger statement.

**Step 8 (conclusion; `h=0`).** `||w_ε||_{L2[0,S]}=||a||` deterministically, so `E||z_ε||/E||w_ε|| → L(a)/||a||`. The strict criterion requires `gamma > E||z_ε||/E||w_ε||` for every `ε`; letting `ε→0`, `gamma >= L(a)/||a||`; the pulses are deterministic, hence admissible in both the E1 and the E2 classes, so this holds for `gamma1` and `gamma2`; take `sup_{a!=0}`. For `h=0` the law uses the combined taps (input 2); one window `[0,ε]`, `D=(E0+Eh)a`, `G=(G0+Gh)a`, `n=0` in the notation above, and Steps 1–7 go through verbatim with one impulse at `0` (the post-pulse state `Gξ_0^ε` is the impulse initial value; `t_0=0<T`). `L(a)<∞` since `E∫||OX^a||² <∞`. ∎ (2)

Consistency check against Source 3: `L(a)/||a|| <= gamma <= C_up`; in the scalar example `C_up = a_o+||O||sqrt(T)[sqrt(δ)a_d+8a_s]R(0,1) = 1+8 = 9 >= 1.3545`. ✔

## 5. The strict gap (3) and its natural weakening

**5.1 Candidate's statement (LF49-51), proof.** Let `a*` be a unit vector with `||B_n a*||=||B_n||=δ`, and suppose `OG_j(a*) != 0` for some `j`. `t_j<T` for all `j<=n` (because `nh<T`). The impulse process is right-continuous on `[t_j,t_{j+1})` with `X_{t_j}=X_{t_j-}+G_jξ_j`, `ξ_j ⊥ F_{t_j-}=σ(B_{·∧t_j},ξ_0,…,ξ_{j-1})`. `⟨OG_j, OX_{t_j}⟩ = ⟨OG_j,OX_{t_j-}⟩+||OG_j||²ξ_j`, which conditionally on `F_{t_j-}` is a nondegenerate Gaussian and vanishes with probability 0; so `OX_{t_j}!=0` a.s., and by right-continuity `||OX_t||>0` on `[t_j,t_j+η)` for a random `η>0`, giving `∫_0^T||OX||²dt>0` **almost surely** (the candidate's "with positive probability", LF49, is correct but weaker than what holds). Since `sqrt(δ²+y)>δ` for `y>0`: `L(a*)=E sqrt(δ²+∫||OX^{a*}||²) > δ`, hence `sup_a L(a)/||a|| >= L(a*) > δ` and `gamma1,gamma2 > δ` by (2). If `B_n=0` (`δ=0`) every unit vector is a top singular vector and the same argument gives `gamma>0`. ∎

**5.2 Proposition (weakened sufficient condition).** Let `α_j := ∫_{t_j}^T ||OΦ(r,t_j)G_j(a*)||²dr` (`Φ(r,s)=Φ_rΨ_s`). If `P(α_j>0)>0` for some `j`, then `L(a*)>δ`. Proof: conditionally on `(B,(ξ_k)_{k!=j})`, `∫_0^T||OX||²` is the quadratic polynomial `α_jξ_j²+βξ_j+γ'` in the independent continuous variable `ξ_j`; on `{α_j>0}` it has at most two zeros, so the energy is positive a.s. on `{α_j>0}`; conclude as in 5.1. ∎ Special cases: `OG_j!=0 ⇒ α_j>0` a.s. (5.1). For `Q=0`, `α_j=∫_0^{T-t_j}||Oe^{Pu}G_j||²du` is deterministic and positive iff `G_j` is not in the unobservable subspace of `(O,P)`, i.e. iff `OP^kG_j!=0` for some `k>=0`. Exact instance NC3 (§6.3): `O=[1,0]`, `P=[[0,1],[0,0]]`, `G=(0,1)^T`, `E=1`, `h=0`, `T=1`: `OG=0` (the candidate's hypothesis fails) but `Oe^{Pt}G=t`, `α=1/3`, `L=E sqrt(1+ξ²/3)=1.14112048634926815…>1=δ`.

The condition remains sufficient, not necessary, and says nothing about the actual gain (§6.3).

## 6. Exact scalar and matrix checks (my own run; no author code, no Monte Carlo)

Script `reviewer-f120-impulse-chain-exact-checks-v1.py` (SHA256 `0e7528ec11690ce61220f98a9cf367d75e834f0340a9070d6dd9ddd5f1205174`, 18085 B), bound run in this directory: `/bin/date` before `2026-10-29T02:56:53Z`, after `2026-10-29T02:57:03Z`, python 3.14.3, mpmath 1.4.1, numpy 2.4.3, macOS arm64; output `reviewer-f120-impulse-chain-exact-checks-v1-output.json` (SHA256 `0b2388f837ed2cd8918a62689f1bdf2e2ade2ae427e62707238e67541f987cfa`, 23942 B). Method: for closed loops with `Q=0`, `∫_0^T||OX^a||²dt = ξ^T M ξ` with `M_{jk}=∫_{max(t_j,t_k)}^T (Oe^{P(t-t_j)}G_j)^T(Oe^{P(t-t_k)}G_k)dt` computed EXACTLY in Fractions (`P=0` or nilpotent `P`), `c²=||B_n a||²` exact, and
 `L(a) = (2 sqrt π)^{-1} ∫_0^∞ s^{-3/2} [1 - e^{-s c²} det(I+2sM)^{-1/2}] ds`
(from `sqrt y=(2 sqrt π)^{-1}∫_0^∞(1-e^{-sy})s^{-3/2}ds` and the χ² mgf; `det(I+2sM)` exact polynomial), evaluated by 30-digit tanh–sinh quadrature; rank-1 cases cross-checked against the closed form `E sqrt(c²+λξ²)=sqrt(λ)k²e^{k²/4}[K_0(k²/4)+K_1(k²/4)]/(2 sqrt(2π))`, `k²=c²/λ` (derived by `x=k sinh u`), and against direct Gaussian quadrature. Agreement across the three routes: `<= 9e-18` in every rank-1 instance (maximum `8.99e-18`, NC2 `a=(3,1)`).

### 6.1 Candidate §5 scalar example (S1): exact
- `L(1)=E sqrt(1+ξ²) = e^{1/4}[K_0(1/4)+K_1(1/4)]/(2 sqrt(2π)) = 1.354530806481315302053117…` (s-integral `1.3545308064813152979…`, direct quadrature identical to the closed form). Author's floating quadrature `1.3545308064813155` agrees to 15 digits. Author's simple lower bound `1+(sqrt2-1)erfc(1/sqrt2)=1.13143431584031363765…` ✔ (`>1`). Jensen cap `sqrt2`.
- Finite-ε mechanism, exactly: `x_t=ε^{-1/2}W_{t∧ε}`, so `||z_ε||² = ∫_0^1(1+sqrt(ε)B_s)²ds + (1-ε)B_1²` with `B_s=W_{εs}/sqrt ε` a standard BM; pathwise `→ 1+B_1²`, dominated, so `E||z_ε||→L(1)` with no limit theory at all — a direct exact confirmation of the mechanism of §4 in this instance. Exact identity `E||z_ε||²=2-ε/2`. Rigorous Cauchy–Schwarz lower bound `E||z_ε|| >= E sqrt((1+sqrt(ε)I)²+(1-ε)ξ²)`, `I=∫_0^1B=ξ/2+η/sqrt12`:

| ε | rigorous lower bound (GH 300 / nested mpmath) | author MC (LF63) | MC − bound | `sqrt(E||z_ε||²)` |
|---|---|---|---|---|
| 0.1 | 1.3310427677 / 1.33104276770437 | 1.3342143979 | +0.0032 | 1.3964 |
| 0.04 | 1.3452409951 / 1.3452409950653 | 1.3444025317 | −0.0008 | 1.4071 |
| 0.01 | 1.3522210227 / 1.35222102267151 | 1.3492549984 | −0.0030 | 1.4124 |

Two of the author's sampled values lie *below* rigorous lower bounds; with `sd(||z_ε||)≈0.41` and 30000 paths the MC standard error is `≈0.0024`, so this is ordinary sampling error, but it confirms that the LF63 numbers carry no evidential weight (F7). Nothing in the candidate relies on them.

### 6.2 Chains with `h>0` (exact algebra + 1-D integral)
- S2 (Source 4's instance, `h=1, T=5/2, n=2, E0=1, Eh=-1, O=1, G0=1, Gh=0, P=Q=0`): `B_2^TB_2=[[2,-1],[-1,2]]` exact; `δ=sqrt3`. Top direction `a=(1,-1)`: `D=(1,-2,1)`, `c²=6`, `G=(1,-1,0)`, `M=[[5/2,-3/2,0],[-3/2,3/2,0],[0,0,0]]`, `L(a)/||a|| = 2.18410369310628… > sqrt3 = 1.7320508…` (strict gap (3) holds; `OG_0,OG_1!=0`). Other directions: `(1,1)`: 1.6261 (atom 1.0); `(1,0)`: 2.0120 (atom 1.4142); `(0,1)`: 1.8116 (atom 1.4142). All satisfy `c/||a|| <= L/||a|| <= sqrt(c²+tr M)/||a||`.
- S3 (matrix taps, `p=q=2`, state dim 2, `E0=I, Eh=J=[[0,1],[1,0]], G0=diag(1,0), Gh=0, O=I, P=Q=0, h=1, T=5/2`): `B_2^TB_2=[[2I,J],[J,2I]]` exact, eigenvalues `{3,3,1,1}`, top vectors `(v,Jv)`. `a=(1,0,0,1)`: `c²=6`, `M=diag(5/2,0,0)`, ratio `2.02890112361140870… > sqrt3`; `a=(0,1,1,0)`: `M=diag(0,3/2,0)` (the gap now comes from the *second* impulse at `t_1=1<T`), ratio `1.92137351100062622… > sqrt3`; `a=(1,0,0,-1)` (non-top): ratio 1.4227 vs atom 1.0.

### 6.3 Negative controls
- NC1 (`O=0`): `L(a)=c` exactly; formula returns `sqrt6` to `7e-18` — the s-integral reduces correctly when the state is invisible.
- NC2 (`p=2, h=0, T=1, E=[1,0], G=[0,1], O=1, P=Q=0`): `L(a)=E sqrt(a_1²+a_2²ξ²) <= ||a||` by Jensen, equality only at `a*=(1,0)` where `OGa*=0`. Values: `(1,0)`: 1.0000; `(3,1)`: 0.99785; `(1,1)`: 0.95780; `(1,3)`: 0.85700; `(0,1)`: `sqrt(2/π)=0.79788456080286535…` (exact check of the formula at `c=0`). So `sup_a L(a)/||a|| = δ = 1`: the impulse functional gives **no** strict gap here, although `gamma=1` is in fact infeasible for the strict criterion (`w=(1,0)1_{[0,1]}` gives `z≡1`, ratio exactly 1). The candidate's (3) is correctly stated as sufficient only; neither bound decides the `gamma=δ` endpoint in general.
- NC3 (`OG=0`, dynamics-visible): `M=[[1/3]]` exact, `L=1.14112048634926815 > 1`: the strict gap can hold when the candidate's hypothesis fails (Prop. 5.2).
- D1 (drift channel, deterministic: `dx=w dt, z=x+w, h=0, T=1`): `G=0` so `L(a)=|a|`, `δ=1`; the constant input `w≡1` gives `||z||²=∫_0^1(1+t)²dt=7/3` exactly, ratio `sqrt(7/3)=1.52752523165…`. The pulse family deliberately annihilates drift forcing (`sqrt(ε)F_j→0`), so the impulse bound is blind to drift energy: it is not the gain and must not be read as "sharp".

## 7. Findings (severity, anchor, status)

- **F1 — MAJOR (repaired here).** LF43: "Standard continuity of finite-dimensional linear Itô flows … gives convergence of the physical outside-window state output to `O X^a` in L2-time distribution, with uniform second moments" and LF45 "Thus … `lim E||z(w_ε)||/||w_ε|| = L(a)/||a||`". This is the first unproved step: no comparison process is constructed on a common space, no error recursion across the `n+1` windows is given, no continuity estimate in the jump times/horizon is stated, and the distribution-plus-UI route is asserted rather than derived. Statement is TRUE; §4 supplies a complete argument (L1 coupling, Steps 4–7). The candidate should be adopted only together with §4 or an equivalent written repair, and §4 needs its own check (same-harness here).
- **F2 — MINOR (subsumed by F1).** LF41 "close in L2(Ω×time) to the homogeneous impulse process with the same pulse normals": the object is unspecified; the literal reading (full-clock `W`, jumps at `t_j`) is not adapted and does not have the law of `X^a`. The correct object is `X̂` of §4 Step 4 (paused-clock Brownian motion, jumps at window ends).
- **F3 — MINOR (wording).** LF43 "equivalently the one-Brownian Doss–Sussmann ODE transform": an alternative device, not an equivalent statement; §4 uses none of it, and `P,Q` need not commute.
- **F4 — MINOR (wording/strengthening).** LF49: energy is positive almost surely under the stated hypothesis, not merely with positive probability; the hypothesis can be weakened to `P(α_j>0)>0` (Prop. 5.2, NC3). Conclusion unchanged.
- **F5 — MINOR (editorial).** Sections are numbered 1, 3, 4, 5, 6 (LF5, LF32, LF47, LF55, LF65): there is no section 2 and no displayed equation (1).
- **F6 — MINOR (provenance).** The import of the E1 state-sup bound (Source 3, LF3/LF67) is not load-bearing for the deterministic-pulse argument: Lemma 4.1 (which LF41 itself invokes as "standard linear SDE E2 estimates") suffices. Source 3 is correct regardless (§3.1).
- **F7 — INFO.** LF63 Monte Carlo values at `ε=0.04, 0.01` lie 0.0008 and 0.0030 below rigorous finite-ε lower bounds (§6.1) — within ~2 MC standard errors; diagnostic only, as the candidate itself says.
- **F8 — INFO.** LF61/63 analytic numbers (`1+(sqrt2-1)P(|ξ|>=1)=1.13143431584…`, quadrature `1.35453080648131…`) are correct; closed form in §6.1.
- No FATAL finding. No false mathematical statement found in the candidate's LF1-67.

## 8. Exact scope of what is and is not established (conditional and uniformity scope)

Established (by the candidate's deterministic parts + §4 + §5, same-harness): for EVERY fixed law `u=Kx+L0w_t+Lh w_{t-h}+∫_0^hH(r)w_{t-r}dr` with arbitrary fixed real `K,L0,Lh`, `H∈L2[0,h]`, every finite real plant `(A,B,C,A0,B0,D0,D1)`, one scalar Brownian motion, zero state/history, zero-extended input, finite `T>h>=0` with `S=T-h>0`, and the literal criterion `E||z||_{L2[0,T]}/E||w||_{L2[0,S]}<gamma`:
 (i) `gamma1 >= sup_{a!=0}L(a)/||a||` and `gamma2 >= sup_{a!=0}L(a)/||a||`, with `L(a)` the candidate's impulse functional on the `h`-lattice pulse family (`h=0`: one impulse, combined taps);
 (ii) if some unit top singular vector `a*` of `B_n` has `P(α_j(a*)>0)>0` for some `j` (in particular `OG_j(a*)!=0`), then `gamma1,gamma2>||B_n||`, so `gamma=||B_n||` is infeasible for the strict criterion;
 (iii) the `h=0` scalar law `u=w`, `B0=D1=D0=1` (others 0), `T=1` has `gamma1,gamma2 >= L(1)=1.35453080648131530205…>1=δ`.
Uniformity: (i)–(iii) are pointwise in the law and the horizon; the constants in §4 depend on `(P,Q,T,n,a,||F||_{L2},||G||_{L2},||E||_{L2})` but only their finiteness is used; no uniformity in `h→0`, `T→∞`, or over laws is claimed.

NOT established (and not claimed by the candidate): the actual gains `gamma1,gamma2`; sharpness of `sup_a L(a)/||a||` (D1 shows the gap to the true gain can be large; NC2 shows the impulse bound can be blind to an attained equality); the `gamma=δ` endpoint when (ii) fails; any controller synthesis or necessity statement; E1/E2 strict transfer at the actual gain; several Brownian drivers; infinite horizon; the behaviour of `L` under `h→0`. Pulses at non-lattice times or with more than one pulse per lattice slot would give (weakly) larger lower bounds — a remark, not a result. All numerics in §6 are illustrations of magnitudes; the inequalities themselves are proved in §§4–5 and in the exact algebra, not by the numbers.

## 9. Process disclosures and artifacts

- Inputs: read in manifest order with `:raw`; nothing outside the six inputs, the manifest and the authority addendum was read for this review; the later source-owner addendum named by Main was NOT opened.
- No author contact, no web search, no external model/paid API, no Git, no deletion, no publication, no infrastructure change, no repository test/lint/build suites.
- The author's `.py` (input 6) was read, never executed or imported; my script shares no code with it.
- Draft debugging: one draft execution of an earlier version of my script from `/tmp/f120-draft-checks.py` at 2026-10-29T02:52:37Z (it exposed a numpy `hermegauss(400)` overflow, fixed by using 200/300 nodes plus an independent nested-mpmath cross-check, and prompted adding control D1). A `cp` probe file `/tmp/f120-write-probe.txt` (6 B) exists; `rm` is blocked by tool policy, so both `/tmp` files remain (outside the review directory). Nothing was overwritten in the review directory (refuse-overwrite `test ! -e` before every copy; the output JSON was opened with mode `x`).
- Artifacts in this directory (all new, uniquely prefixed): `review-v1.md` (this file), `reviewer-f120-impulse-chain-exact-checks-v1.py`, `reviewer-f120-impulse-chain-exact-checks-v1-output.json`, `reviewer-f120-run-receipt-v1.json` (hashes/clocks binding, written after this file).
