# An all-frequency NECESSARY bound for the original infinite literal gain

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Last actual native prewrite observation: **Tue Oct 27 17:13:36 PDT 2026**. This is a given-law class-level obstruction, not a stochastic transfer-function equivalence, controller construction or RMS replacement. It uses the current author mean-tail source `mean-tail-moment-obstruction-infinite-literal-gain-v1.md`, SHA `95a2c5559ab84b93054445c98c23e54d28aec5fc04aa9a2466dc15d4a1cba89e`, itself pending review. No new source or scientific execution.

## 1. Full original matrix/law and the mean-tail boundary

Keep all compatible real original matrices, positive dimensions, finite h>=0, zero state/history, ONE bound deterministic stationary linear preview law and canonical progressive globally E2 disturbances in the explicit local-control infinite comparison. Stricter law eligibility, if required, is separate; all necessary bounds apply in particular to any law meeting it.

Write

`P=A+BK`, `Q=A0+B0K`, `O=D0+D1K`,

`R(s)=L0+exp(-sh)Lh+integral_0^h H(r)exp(-sr)dr`.

At h=0 use the combined tap and no kernel. Define Pi_+ and M_h exactly as in the pinned mean-tail source:

`M_h=B L0+exp(-Ph)(B Lh+C)+integral_0^h exp(-Pr)B H(r)dr`.

If any finite condition `O P^j Pi_+ M_h=0`, j=0,...,n-1, fails, that source gives an ACTUAL compact deterministic input family with infinite original literal ratio. The present bounded-mean analysis assumes all of those conditions hold. It does not solve them for gains or infer that they suffice for stochastic feasibility.

## 2. The actual deterministic-MEAN frequency function, including canceled poles

The paid finite-prefix E2 control makes the actual Itô term zero-mean for deterministic inputs. The mean-output map is the ordinary causal convolution with direct atoms

`J0=D1L0`, `Jh=D1Lh`,

and the L1 regular kernel k(t) reconstructed in the mean-tail source. Its head is finite-window integrable; its tail is `O exp(Pt)M_h`, whose nonstable observed component vanishes under the finite conditions. Thus the function

`T_mean(omega)=J0+exp(-i omega h)Jh+integral_0^infinity k(t)exp(-i omega t)dt`

is defined and continuous for EVERY real omega, even when P has unobservable/canceled imaginary-axis eigenvalues.

For i omega outside the finite spectrum of P it equals the exact original-coupling formula

**T_mean(omega)=O(i omega I-P)^(-1)[B R(i omega)+C exp(-i omega h)]+D1R(i omega).** (F)

No full stochastic transfer function is asserted. To justify (F) without illegitimately transforming an unstable state term separately, first integrate the COMPLETE finite kernel head/tail through a finite b>h. Ordinary finite-interval integration gives the state part

`O(sI-P)^(-1)[B R(s)+C exp(-sh)]`

`- O(sI-P)^(-1)exp((P-sI)b)M_h`.

The finite conditions kill the observed nonstable component of the last term: the resolvent is a polynomial in P up to a scalar factor at every noneigenvalue, by Cayley-Hamilton. The remaining stable component tends to zero. Adding the direct atoms/kernel proves (F) on the real frequency line. At an excluded eigenfrequency use the CONTINUOUS kernel-defined value above, not omission of that frequency or an undefined inverse. No pole, Jordan or zero-frequency case is silently discarded.

## 3. Exact norm of the MEAN channel and ACTUAL real input caller

Put `sigma_mean=sup_(omega real)||T_mean(omega)||<infinity`. The causal deterministic mean channel has L2 operator norm exactly sigma_mean.

Upper bound: zero-extend any input to the real line and apply unitary L2 Plancherel plus the bounded Fourier multiplier of the L1 kernel/direct shifts. Restriction to the causal half-line loses nothing for zero-negative-time input.

For the converse fix ANY real omega0 and any complex unit input vector e. Use the analytic compact-input family

`v_L(t)=exp(i omega0 t)e/sqrt(L)` on [0,L], zero elsewhere.

Its Fourier energy has total mass one and concentrates at omega0 as L increases: outside any positive frequency radius, the elementary bound on the finite exponential integral gives vanishing tail mass; inside, bounded continuity of T_mean gives convergence. Thus its mean-output/input norm ratio tends to `|T_mean(omega0)e|`. This is a universal proof in omega0,e,L, not a selected frequency/rank/control probe or an executed transform.

All physical inputs may be REAL. The real convolution operator's norm on complexification equals its real norm, since for v=x+i y both input and output squared norms split into the real/imaginary sums. At least one nonzero real component therefore has ratio at least the complex ratio. These real components are ACTUAL deterministic compactly supported E2 disturbances, not formal Fourier profiles or inputs to a different controller. Taking all omega0/e gives the reverse norm bound.

For each such actual deterministic input, the original output satisfies the finite-prefix expectation triangle inequality. Monotone prefix limits give

`E||z(v)||_[0,infinity) >= ||E z(v)||_[0,infinity)`.

Hence the ORIGINAL criterion obeys

**G_prog,infinity >= G_det,infinity >= sigma_mean.**          (N)

No independence between input and Brownian motion, RMS gain, private policy choice or expected-control upgrade outside the bound linear class has been used.

## 4. Explicit high-frequency endpoint obstruction, all matrices

The L2 finite-window H is L1, and its Fourier integral tends to zero as |omega| increases: approximate H in L1 by step matrices, whose elementary interval integrals decay, and bound the transform error uniformly by the L1 error. Also `(i omega I-P)^(-1)=O(1/|omega|)` by its finite Neumann expansion/bound beyond ||P||. R(i omega) stays bounded.

Consequently

`T_mean(omega)=J0+exp(-i omega h)Jh+o(1)`.

For h>0 the phase runs around the full unit circle along symbolic unbounded frequency sequences. Therefore

**limsup_(|omega|->infinity)||T_mean(omega)|| = max_(|z|=1)||J0+zJh||.** (T)

For h=0 the limit is instead ||D1(L0+Lh)||. Combining (N) and (T) gives a whole-original-matrix infinite tap obstruction without assuming the dynamic mean contribution can cancel all high-frequency inputs. No numerical frequency, small case or boundary value is tested.

## 5. Precise prescribed-gamma consequences and limits

For any GIVEN law, uniform-strict original literal feasibility requires both the finite nonstable mean-tail conditions AND `sigma_mean<gamma`; in particular its high-frequency endpoint quantity in (T) must be below gamma. Pointwise-strict feasibility for every individual input gives only the deducible nonstrict condition `sigma_mean<=gamma`. Equality need not supply a violating input; no endpoint norm-attainment inference is fabricated.

If sigma_mean>gamma, the universal real compact wave-family proof above supplies an actual deterministic input whose mean ratio, and hence actual literal ratio, exceeds gamma. If the finite tail test fails, an actual ratio is infinity. Conversely, passing these tests proves ONLY that no such deterministic-mean obstruction was found. It says nothing sufficient about stochastic fluctuations, a sharper actual gain, global-control/EMS eligibility or existential general synthesis.

Q is unrestricted and remains in the physical state/mean-caller integrability argument, but does not enter this first moment. The criterion is not treated as equivalent to the deterministic mean problem: the supported progressive-versus-deterministic gap already warns against such a promotion. Every matrix rank, repeated/canceled pole, h=0/h>0, zero output or feedforward degeneracy is included at its stated branch.

## 6. Import and control boundary

Mathematical inputs are the explicitly pinned current mean-tail theorem/physical kernel, ordinary deterministic finite integration/Cayley-Hamilton, standard L2 Plancherel/multiplier facts and the displayed real compact-input approximation, plus finite-prefix strong linear-SDE/isometry zero mean. No new source, source-page method, original historical audit claim, Riccati/storage/Gramian or stopped realization/diffusion-annihilating controller construction is used. No gain is computed by sampling a frequency or choosing a matrix instance.

All old late-ACK/cadence/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and source-render/copyright/parent physics-2 L1 quarantine controls persist. The author import and this paper remain UNREVIEWED; no parent/peer, formal/kernel, executable, human/configured-family, novelty or general-target completion is claimed.
