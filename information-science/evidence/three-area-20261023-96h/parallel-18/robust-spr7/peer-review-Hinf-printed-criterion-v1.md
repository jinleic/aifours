# Bounded peer reconstruction — literal stochastic H-infinity preview candidate

Observed clock before creation: **2026-10-23T14:19:02-0700**. Reviewer: InfoSPR7 (info-2), temporarily performing the one review assigned in `peer-review-wave-eighteen-v1.json`, then returning to robust SPR. No nested agent, model CLI or executable scientific check.

## Snapshot and scope

- Complete source read: `information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/proof-v1.md`, all323 lines.
- SHA256 independently observed with `shasum -a 256`: **`895a36cdc42565aa7b7b6fd4279a34aba6b3bb7f0c8918d14e49d59b72f5635c`**, exactly the assigned pin.
- Actual selection read in full, including its uniform strict induced-gain interpretation, all-adapted square-integrable input class, information and horizon boundaries.
- Actual book page images PDF695–696 (printed674–675) read: continuous-time multiplicative-noise dynamics, pathwise L2 norm, expectation outside that norm, preview window and finite/infinite horizon distinction. No mean-square substitution is licensed by those pages.
- Actual primary [Geiss–Scheutzow, arXiv:2101.10884v2](https://arxiv.org/html/2101.10884v2), Theorem2.2 and preceding comparison read. Its constant is `p^(-p)` under nonnegative nondecreasing adapted right-continuous processes, predictable `G` and conditional domination for every bounded stopping time.

## Verdict and findings

**No FATAL, MAJOR or MINOR mathematical defect found at the explicitly stated scope.** The three main claims reconstruct as written: the causal upper transfer, the infinite stationary-linear two-sided comparison, and the scalar fixed-feedback finiteness classification with deterministic pulse-train obstruction. This is an ordinary in-harness written check with the author's proof supplied, not blind, different-model-family, external, human or proof-assistant acceptance. Parent reconstruction remains separate.

This verdict does not accept a full synthesis theorem, a sharp comparison constant, novelty, an imported Riccati theorem, or equivalence of the two gain criteria at the same prescribed gamma.

## Independent reconstruction of load-bearing steps

### 1. Causal transfer and the imported constant (source lines55–95)

For each fixed input, let `X_t` be its accumulated output energy through `t wedge T` and `G_t=g^2` times input energy through `t wedge L`. Both are continuous monotone adapted processes, and `G` is predictable. Stopping the **input**, rather than resetting any state, preserves the output only up to the stop. Its subsequent output energy is nonnegative. The assumed full-horizon square-energy inequality therefore gives `E X_tau <= E G_tau` for every bounded stopping time, precisely as required.

Multiplication of the stopped input by `1_A`, `A in F_0`, is admissible. Event locality and zero preservation give the corresponding inequality with `1_A` inserted; thus the domination is conditional on `F_0`, not merely an unconditioned estimate being substituted into a conditional theorem. The actual primary Theorem2.2 at `p=1/2` gives `E sqrt(X_infinity) <= sqrt(2) E sqrt(G_infinity)`, hence the stated `sqrt(2)g` factor. No additional square root of the constant occurs: these expectations are already `N1`.

The finite-horizon convention with output continuing through `T` but input stopping at `T-h` causes no gap; stopped-input domination still compares total nonnegative output energy to stopped input energy. The larger-input extension is correctly separate and requires its stated local pathwise well-posedness. The Jensen warning is justified.

### 2. Direct quadratic sufficient certificate (lines97–130)

Substitution of `u=Kx` into drift, diffusion and output gives exactly the blocks in (7). Itô's formula supplies the storage, output and state-penalty inequality (9). Localization makes the stopped martingale integrable; Fatou and the nonnegative storage term give the square-energy bound for all adapted inputs. The shift identity counts precisely `[0,T-h]` on finite horizons. For zero input, `|x|^2 >= V/lambda_max(P)` gives the claimed exponential mean-square decay. Thus this corollary really supplies a conservative sufficient certificate for the printed norm rather than treating the old Riccati replacement as necessary.

### 3. Independent local blocks, global tails and signed superposition (lines134–224)

For the deterministic time-homogeneous linear controller (10), replay a Brownian-functional input template using each block's independent Brownian increment path. The component starts from zero before its own block. Its **local** energy is a measurable function of that block's Brownian path and has the template law, so the local energies are independent. Its later tail need not be independent of other tails; the proof never assumes that.

Linearity of the drift and diffusion, with the same actual Brownian motion, gives global pathwise superposition for each deterministic sign vector. In the finite-observation Hilbert space, if `V=sum||y_i||^2`, direct expansion yields `E_eta||sum eta_i y_i||^4 <=3V^2` and second moment `V`. Hölder then gives the lower expected norm `sqrt(V/3)`. Since component full-observation energies dominate the local block energies, the sign average bounds the actual aggregate output below by `E sqrt(sum Y_i)/sqrt(3)`. The plant and controller are not reset. Every input sign pattern is adapted and has the same pathwise input energy because its supports are disjoint.

The Chebyshev argument for `Y_i wedge M` is valid with variance bound `M^2`; its successive limits yield `liminf E sqrt(n^(-1)sum Y_i) >=sqrt(EY)`. The denominators are bounded above by `sqrt(n EX)`, giving `G1>=sqrt(EY/EX)/sqrt(3)`. Taking templates is sufficient for the full `G2`: truncate any input at its output observation time, use causality before that time and then monotone convergence. Conditioning on any independent initial seed cannot enlarge the square-mean operator norm. The conclusion remains restricted to the same stationary linear controller class, infinite horizon and extended-real finiteness, as the source states.

### 4. Scalar no-go including q=0 (lines228–311)

With `q=2a_k+sigma_k^2<0`, the Young inequality in line254 yields `G2<=2|c||d_k|/(-q)`; applying the already checked causal transfer gives (23), with no deterministic-input restriction in this sufficient direction.

For `q>=0`, a positive unit forcing pulse has positive state at its end because the stochastic exponential is strictly positive. After forcing ends, its square mean is exactly `m exp(q(t-1))`, by independent future Brownian increments. Thus isolated-block mean output energy diverges with block length, linearly even at `q=0`. For the actual same-sign deterministic pulse train, all component scalar states are nonnegative. On each block the full output norm is therefore at least the isolated component's norm, even with all old state and tails retained. The independent local-energy average and the explicit finite-n Chebyshev inequality then produce a finite-energy input whose literal norm ratio exceeds any fixed Gamma. The choice (28) has the correct strict direction and finite positive denominator after the earlier choices of L,M,delta.

The argument proving one pulse can nevertheless have finite `N1` when `a_k<0<=q` is consistent: unit-block path norms are bounded using `E Phi(j)=exp(a_k j)` and a finite within-block second moment. It does not make the induced gain finite. The all-controller statement in line311 explicitly removes actuation and includes the state in the output; it is not silently extended to effective general actuation.

## Trust and scope boundaries retained

The ordinary Itô/linear-SDE, Hölder, Chebyshev and monotone/Fatou arguments above were reconstructed in writing. The monotone Lenglart theorem is a genuine external classical import, read at its exact primary statement; its sharpness proof was not independently rebuilt. The 2014/2020 Riccati papers are not dependencies of these arguments, and their recorded source-status characterizations were not independently re-audited in this bounded rotation. No old finite-horizon gamma6 computation was replayed.

The selection's uniform strict induced-gain formulation is an explicit interpretation of the book; the candidate does not prove same-gamma necessity/sufficiency for arbitrary laws, finite-horizon reverse comparison, nonlinear reverse comparison or internal stability from gain alone. Novelty remains UNCLEAR. This review supplies no priority or significance upgrade.
