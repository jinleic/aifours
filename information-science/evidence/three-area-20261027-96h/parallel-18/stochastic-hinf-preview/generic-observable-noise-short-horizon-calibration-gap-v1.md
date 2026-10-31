# A generic observable input-noise obstruction to deterministic calibration

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** Actual native prewrite observation: **Tue Oct 27 17:25:51 PDT 2026**. Given-law, all-matrix class-level obstruction; no controller is constructed or chosen to annihilate noise. The proof is independent of NR-GAIN/BDG and uses only strong linear-SDE/isometry facts, their explicit E2 perturbation estimate, and an analytic stopped-Brownian family. No selected diagnostic or new source.

## 1. Original law, algebraic condition and exact horizon quantifiers

Fix arbitrary compatible real original matrices, positive dimensions and an ALREADY GIVEN deterministic stationary current-tap law

`u(t)=Kx(t)+Lw(t)`.

It is in the bound full-information preview class for every h>=0 (left tap/kernel zero); at h=0 L can be the combined endpoint tap, so every bound h=0 law has this form. Use zero state/history, canonical progressive E2 inputs specified on [0,T-h], zero elsewhere INCLUDING (T-h,T], and the original output `z=D0x+D1u`.

Define the actual closed-loop matrices

`P=A+BK`, `Q=A0+B0K`, `O=D0+D1K`, `G=B0L`,

`J=D1L`, `M=O G`.

Assume ONLY the two exact algebraic conditions

**J=0 and M!=0.**                                            (A)

The instantaneous control-noise channel is therefore OBSERVABLE and active, not annihilated. P,Q,B,C are otherwise unrestricted. No stability, rank or noise-smallness hypothesis is imposed.

Fix ANY preview fraction theta in [0,1). For each T>0 set `h=theta T`, `S=(1-theta)T`. Matrices/K/L stay unchanged as T varies. At theta>0 this is a family of positive-preview problems, NOT a claim that a fixed nonzero h permits T to decrease to zero.

**Theorem.** For every such fixed matrix/law/theta tuple, there exists T0>0 such that for EVERY 0<T<T0 the actual literal gains obey

**G_prog(T,theta T) > G_det(T,theta T).**                     (G)

A legal adaptive E2 input has ratio above an explicit upper bound covering EVERY deterministic L2 input. Both use the SAME original law/plant/output at that T,h. At theta=0 this is an algebraic generic sufficient condition for short-time deterministic calibration failure across the entire original h=0 linear class.

## 2. Scalar Brownian ingredients, all parameters and no numerical value

For any radius r>0 let tau_r be first exit of standard Brownian motion from (-r,r). The stopped-indicator integral identity, derived from the Itô simple-predictable construction/isometry, gives `E(t min tau_r)=E|W_(t min tau_r)|^2<=r^2`. Monotone/bounded convergence and path continuity imply E tau_r=r^2. The stopping time is nonconstant (a deterministic exit time would contradict the nonatomic Gaussian marginal), so `0<E sqrt(tau_r)/r<1` by strict Cauchy-Schwarz.

Brownian scaling here is derived directly from its definition: `W_(b^2 t)/b` has continuous paths, independent centered Gaussian increments of variance equal to the time increment. Consequently tau_r has the distribution of r^2 times the exit time at any common normalized radius, and

`rho:=E sqrt(tau_r)/r`

is the SAME number for every r>0, with 0<rho<1. No radius or value is selected/evaluated as a diagnostic.

For the given theta choose ANY positive dimensionless a satisfying

`eta:=1-rho-a^2/(1-theta)-rho a>0`.                           (B)

The set of such a is nonempty because the two subtractions tend to zero with a, while 1-rho>0. Let xi be tau_a min (1-theta) for a standard Brownian motion and define the exact unevaluated constants

`m=E sqrt(xi)>0`, `v=E xi`, `R_stop=sqrt(v)/m<infinity`.

All are ordinary analytic constants for the entire parameter family, not chosen boundary/frequency/state tests.

## 3. Reference integrator: deterministic upper and actual adaptive lower

Use the auxiliary operator on the SAME input/Brownian motion

`X0_t=G integral_0^t w_s dW_s`, `Y_t=O X0_t=M integral_0^t w_s dW_s`.

It is a comparison operator only; it is not substituted for the original plant/output in the theorem. For EVERY deterministic input on [0,S], Itô isometry/Tonelli and Cauchy-Schwarz give

`E||Y||_[0,T] <= sqrt(T)||M|| ||w||_[0,S]`.                   (U0)

Choose any real unit maximizing vector e of the finite matrix M. For EVERY amplitude q>0 use the actual progressive family

`w_(T,q)(t)=q e 1_(0<=t<S) 1_(t<sigma_T)`,

`sigma_T=inf{t>=0:|W_t|=a sqrt(T)}`.

It has positive finite E2 input energy. The law is unchanged: the disturbance uses its own stopping rule, not a new controller or private information. Scaling W_(Ts)/sqrt(T) shows exactly

`E||w_(T,q)||=q sqrt(T)m`,

`||w_(T,q)||_E2=q sqrt(T)sqrt(v)`,

so its E2-to-literal input norm factor is the FIXED finite R_stop, independent of T and q.

For this input, Y is q M e times the actual Brownian path stopped at sigma_T min S. On {sigma_T<=S}, that path has magnitude a sqrt(T) after exit. The inequalities `sqrt(T)<=sqrt(r)+sqrt((T-r)_+)` and `P(sigma_T>S)<=a^2/(1-theta)` therefore give

`E||Y|| >= q||M|| a T [1-rho a-a^2/(1-theta)]`.

Also `E sqrt(sigma_T min S)<=E sqrt(sigma_T)=rho a sqrt(T)`. With (B) the positive lower bound yields

**E||Y||/E||w_(T,q)|| >= ||M||sqrt(T)[1+eta/rho].**           (L0)

This is an actual adapted-input inequality for an ENTIRE symbolic family, not graph singularity, a RMS criterion or a single sampled case.

## 4. All-coupling E2 error for the ORIGINAL physical law

The actual state satisfies

`dX=[P X+B Lw+Cw(t-h)]dt+[Q X+G w]dW`, `z=O X`,

where J=0 was used ONLY in the original output expression. Let `f=||BL||+||C||`; the drift-input operator norm is at most f by zero extension/shift contraction. All finite-T states/controls/outputs are uniquely strong, E2 and nonexplosive by the permitted linear-SDE theorem.

For clarity the needed elementary E2 estimate for `dV=(PV+f0)dt+(QV+g0)dW`, V0=0, is

`||V||_E2[0,T] <= 2sqrt(T)exp(2T[T||P||^2+||Q||^2]) sqrt(T||f0||_E2^2+||g0||_E2^2)`.

It follows from the integral equation, squared four-term Cauchy inequality, Itô isometry and the elementary integral Gronwall bound. No first-moment/NR-GAIN import or martingale maximal inequality is used.

The difference X-X0 has original homogeneous P,Q, drift forcing `P X0+BLw+Cw(t-h)` and diffusion forcing `Q X0`. Since `||X0||_E2<=sqrt(T)||G||||w||_E2`, substitution in that E2 estimate gives the UNIFORM actual-output bound

`||z-Y||_E2[0,T] <= epsilon(T)||w||_E2[0,S]`,

`epsilon(T)=2T||O||exp(2T[T||P||^2+||Q||^2])`

`             * sqrt((f+||P||sqrt(T)||G||)^2+||Q||^2||G||^2)`.

Thus epsilon(T)=O(T) and epsilon(T)/sqrt(T)->0 for the fixed matrix tuple. Every B,C,Q and state/output coupling is retained in this bound; no approximate reference dynamics is asserted identical to the original response.

## 5. Paid actual ratio comparison and strict gap

For EVERY deterministic input, its E2 norm equals its deterministic L2 norm. The triangle inequality, (U0) and the error bound imply

`G_det(T,h) <= U(T):=||M||sqrt(T)+epsilon(T)`.

For the ACTUAL adapted family w_(T,q), Cauchy-Schwarz converts the error ONLY using its proven R_stop, not a false uniform E2/L1 norm equivalence. Equations (L0) and the error bound give

`E||z(w_(T,q))||/E||w_(T,q)||`

`>= L(T):=||M||sqrt(T)[1+eta/rho]-epsilon(T)R_stop`.

Consequently

`L(T)-U(T)=||M||eta sqrt(T)/rho-epsilon(T)(1+R_stop)>0`

for EVERY sufficiently small T>0. This proves (G). Each exhibited ratio is finite by actual E2 well-posedness and its denominator is positive. No exact value or finiteness of the progressive supremum is required. For any prescribed threshold strictly between U(T) and L(T), deterministic-input testing passes THIS fixed law while one legal progressive disturbance fails its ORIGINAL literal criterion.

## 6. Degeneracies, scope and control boundary

M!=0 supplies a real maximizing direction and a positive strict-gap coefficient; if it fails no gap is claimed. J=0 is a hypothesis on the GIVEN law, not an equation solved to design it. No conclusion is made for J!=0, arbitrary left/kernel tap laws at positive h, fixed nonzero h with T tending to zero, or optimized synthesis over all controllers. At theta=0 the combined h=0 tap gives the full released linear class; theta>0 is explicitly the current-tap subset with h proportional to T. Every matrix rank/sign, feedback K, arbitrary Q including nonzero values and all q>0/a satisfying (B) are included.

This extends an isolated physical family into an all-matrix algebraic short-time obstruction, not a general N&S synthesis theorem. It is independent of pending NR-GAIN and does not rely on a historical book-audit assertion. No controller is constructed to remove diffusion; the observable noise channel is REQUIRED nonzero. The original regulated output is never replaced by Y: all final inequalities use the explicit actual error and the same actual law.

Only strong linear-SDE/isometry/linearity facts, deterministic matrix/norm inequalities, Brownian defining Gaussian scaling/continuity and the displayed stopping/moment arguments are used. No optional-stopping/BDG source, old guide, source-page method, parent physics-2 L1 material, Riccati/storage/Gramian or stopped realization is imported. No scientific interpreter/CAS/enumeration, chosen diagnostic/frequency/state/control probe, external model or nested agent occurred. Every process/STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP/source-render/copyright limit persists; written only, no parent/peer/formal/kernel/executable/human/configured-family/novelty acceptance.
