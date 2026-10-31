# An exact infinite-horizon literal endpoint distinction in the original tap family

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 16:24:12 PDT 2026**. Continued non-construction structural work under the original supplied finite/infinite-horizon question. The direct diffusion-annihilating-controller branch remains STOPPED by `e84b09ba...`; no such controller or excluded guide is used. This is an exact fixed-law characterization and strictness obstruction, not existential general synthesis.

## 1. Precisely bounded infinite-horizon physical comparison

Use the original plant family B=C=B0=0, arbitrary compatible finite A,A0,D0, zero initial state/history, and the same deterministic stationary endpoint law

`u=Kx+L0 w(t)+Lh w(t-h)`, `H=0`.

Strong uniqueness on each finite interval gives the actual state x=0 for all t>=0, with no finite-time explosion; no infinite-horizon stability claim for nonzero states is needed. The ORIGINAL output is

`z(t)=J0 w(t)+Jh w(t-h)`, `J0=D1L0`, `Jh=D1Lh`.

For finite h>=0, define the comparison input domain to be all canonical progressively measurable w with `E integral_0^infinity |w|^2<infinity` and `0<E||w||<infinity`, with zero negative-time extension. Controls and outputs are globally E2 by the bounded endpoint shifts. This verifies the actual infinite-horizon caller for THIS family; no blanket infinite-horizon admissibility of the full finite-horizon S1 class is asserted.

The criterion is the original form `E||z||_L2[0,infinity) / E||w||_L2[0,infinity)`, not RMS. Both deterministic and progressive gain suprema are taken on the same respective domains. The infinite-horizon alternative itself is supplied in the admitted literal problem; no other source is imported.

## 2. All-matrix exact gain

For h>0 put

`M=max_(theta in [0,2pi]) ||J0+exp(i theta)Jh||`.

**Theorem A.** `G_prog=G_det=M`, independent of the positive delay h. At h=0 both gains are instead `||J0+Jh||`.

To prove this, decompose almost every t>=0 as r+jh, 0<r<h, j>=0. Time-domain L2 is the integral over r of the square-summable one-sided chain. On each chain the actual map is

`y_0=J0v_0`, `y_j=Jh v_(j-1)+J0v_j`, `j>=1`.

For finite chains, finite-polynomial orthogonality gives squared output norm at most M^2 times input norm, exactly as in the current all-matrix finite-chain calculation. Finite chains are dense in the square-summable space, and direct shifts are bounded, so the bound extends to every chain and, by nonnegative time-fiber integration, to the entire infinite time operator.

Conversely take any finite N-block real input chain and multiply it by any unit L2 residue function on (0,h). It is an actual deterministic finite-energy input on [0,Nh]. Its full output includes the final delayed block and realizes the same B_N as the finite-chain theorem. The proven all-matrix limit `||B_N|| -> M` gives the matching lower supremum. For completeness that limit uses only the finite polynomial upper bound and plane-wave chains whose N-1 interior output blocks give `liminf ||B_N||>=||(J0+exp(i theta)Jh)e||` for every theta/unit e. Real and complex norms of a real finite matrix coincide, so all physical near-maximizers may be real.

Thus the deterministic time operator has norm M. Its pathwise bound transfers by expectation to ALL progressive E2 inputs, and the deterministic near-maximizers supply the converse. This proves the literal stochastic equality without requiring independence of w and W. At h=0 both taps coincide and the sum matrix gives the stated norm directly.

This proof does not claim that the infinite operator norm is attained. That missing point is precisely the next strictness issue.

## 3. Scalar nonattainment for EVERY nonzero input

Let now j0,jh be real scalars, h>0 and j0*jh!=0. Put `m=|j0|+|jh|>0`. Theorem A gives gain m. Nevertheless

**||j0 w+jh S_h w|| < m||w|| for EVERY nonzero w in L2[0,infinity).** (S)

Here S_h is the zero-extended shift, an isometry on this one-sided space. Equality in the triangle inequality for the real Hilbert space would require `S_h w=sign(j0 jh) w`, because the two vectors have the same unscaled norm. On [0,h), S_h w=0, hence w=0 there; shifting that identity repeatedly gives w=0 on every successive interval, a contradiction. Thus equality is impossible for any nonzero input, proving (S).

For ANY actual progressive E2 disturbance with positive literal norm, apply (S) to its L2 sample paths. The nonnegative gap `m||w||-||z||` is strictly positive on the positive-probability event of a nonzero path and is bounded by the integrable m||w||. Its expectation is therefore positive:

**E||z|| / E||w|| < m for EVERY admitted nonzero disturbance.** (P)

The argument does not require an input-independent strict margin, and no norm-attaining random input is fabricated.

## 4. Matching analytic near-maximizers and complete scalar gamma thresholds

The supremum m is still exact. Let s=sign(j0 jh), choose any unit scalar phi in L2(0,h), and use the whole finite-support input family

`w_N(r+jh)=s^j phi(r)/sqrt(N)`, `j=0,...,N-1`,

zero on other chain blocks. Its norm is one, and its squared output norm is

`j0^2+jh^2+2|j0 jh|(N-1)/N -> m^2`.

These are all-N symbolic actual deterministic inputs, not a selected sample or executed frequency search. In particular every prescribed gamma<m is violated by some actual member, while gamma=m obeys (P).

Therefore for the given fixed scalar law and h>0:

- If j0*jh!=0, pointwise-strict literal feasibility holds EXACTLY for **gamma>=m**, whereas uniform-strict feasibility holds EXACTLY for **gamma>m**.
- If exactly one tap is nonzero, the output map is a scaled isometry; each nonzero input attains its gain m, so both strict conventions require **gamma>m**.
- If both taps are zero, the output is zero and both conventions hold for every prescribed gamma>0.

At h=0 the output is `(j0+jh)w`, and both conventions require **gamma>|j0+jh|** (with the zero-output case again valid for every gamma>0). The original problem prescribes gamma>0; no zero-threshold convention is invented.

For a finite horizon T>h, the complete tap-chain norm is attained by the actual block/residue input, so pointwise strictness at its finite-horizon operator norm fails. The infinite-horizon endpoint behavior above is therefore an exact actual-object distinction, not an inference from b->infinity without an attainment check.

## 5. What this obstruction changes and does not change

This proves that replacing the printed all-input strict inequality by a common strict margin below the gain supremum can change feasibility, even in a fully explicit original-information fixed-law family and with no stochastic state-response difficulty. It also gives a source-clean infinite-horizon norm/attainment caller for the previously derived finite-chain representation. It does not decide which convention the book intended; the three-page audit found that common-margin quantifier not explicitly specified there.

No assertion is made about a different controller's optimum, arbitrary nonlinear full-information F, the general noisy-state plant, stability/internal EMS, general N&S synthesis, matrix-valued endpoint norm attainment or novel status. The all-matrix gain formula and scalar endpoint classification are separately scoped. Every construction retains the original state, controller pattern and output; no performance output is changed and no policy is synthesized from the stopped annihilation route.

Named facts: ordinary endpoint-shift isometry and equality condition in the Hilbert triangle inequality, exact finite polynomial/time-fiber integration, real-versus-complex finite matrix norms, original linear-SDE zero-state uniqueness, elementary monotone/dense L2 limits and strict positivity of expectations. No new source, BDG/energy/storage guide, selected numeric/control/boundary probe, program, external model, nested agent or old proof is used. All process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP and source-render/copyright limitations persist; written only, with no peer/parent, formal/kernel, executable, human/configured-family or novelty acceptance.
