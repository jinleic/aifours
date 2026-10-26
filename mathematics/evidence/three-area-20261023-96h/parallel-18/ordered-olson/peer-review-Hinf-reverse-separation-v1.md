# Priority written reconstruction — reverse H-infinity feasibility separation

Observed before exclusive creation: **2026-10-23T14:36:18-0700 PDT**. Reviewer MathOlson-2, primary math-2. Parent-assigned bounded review; only this named review file is written. This is a separate in-harness reconstruction from the supplied proof, not a blind, cross-vendor, human or formal review. No scientific executable or external-model CLI was used.

## One three-file candidate, exact independently observed pins

All three assigned files were read completely and are reviewed TOGETHER:

| File under `information-science/evidence/three-area-20261023-96h/parallel-18/stochastic-hinf-preview/` | Observed SHA256 |
|---|---|
| `proof-reverse-feasibility-separation-v1.md` | `33a3e60e43ef8e83f4351824fc708467728243a54846fda349350cabae10bb0f` |
| `proof-reverse-feasibility-separation-addendum-v1.md` | `11922c3123990af68d812ab3d8a26dfe9449f6ee5868b3478986355ead1d36d8` |
| `proof-reverse-feasibility-separation-addendum-v2.md` | `889ac912ab3dcd4ae6cd551f2b97739e80e53a512fa2c00aed6149d3880bfe3f` |

These match the assigned pins; no source bytes were changed. The additive v1 is the OPERATIVE algebra correction, and additive v2 supplies the finite-horizon extension. Reviewing the base alone would retain an invalid coefficient equality and miss the later scope extension.

Read the complete current selection and continuation freeze. Read the used causal-transfer dependency `proof-v1.md` sections1–3, including the larger-input localization extension, observed SHA256 `895a36cdc42565aa7b7b6fd4279a34aba6b3bb7f0c8918d14e49d59b72f5635c`. Its later reverse-comparison/scalar results are NOT needed or imported into this review. Read actual book page images `.../stochastic-hinf-preview-control/sources/book/pdfpage-0695.png` and `pdfpage-0696.png`: the model is continuous-time with constant matrices, and equation(3) indeed puts the expectations OUTSIDE the pathwise L2 norms. Finite and infinite horizons are both requested.

Freshly read the primary statement of [Geiss–Scheutzow2021v2 Theorem2.2](https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2). It requires nonnegative nondecreasing adapted right-continuous X,G, predictable G, and conditional domination at every bounded stopping time; its constant is p^(-p), hence sqrt2 at p=1/2. This theorem is the explicit classical import; its proof/optimality is not newly certified here.

## Verdict

**No substantive defect found in the combined candidate at the stated admissibility and source boundary. Unresolved findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The checked claim is an exact SAME-LEVEL SEPARATION, not a same-level transfer theorem: at gamma16386 the stated plant has an internally mean-square-stable mean-square feasible controller, yet every adapted admissible controller fails the printed criterion, on infinity and on the explicit finite horizon. Full necessary-and-sufficient synthesis and novelty remain unestablished. Parent acceptance is separate.

The false base coefficient3/16 in its equation following(24) was author-corrected BEFORE this review to11/32 in additive v1. I independently reconstruct that corrected identity below; this is an already repaired source issue, not a new unresolved finding or a clean pass of the uncorrected base.

## Reconstruction

### 1. Exact norms, effective model and all-adapted mean-square bound

Base lines19–56 define the two-state plant and admissibility. Matrices(3) give df=kappa(-f+w(t-h))dt and dy=(-epsilon y+u)dt+(f+u)dW, with z=(y,r u). Thus B and B0 both directly enter the PERFORMANCE state y; the argument does not hide actuation in an unused state. D1^T D1=r²>0 and the performance/control output channels are separate.

With u=0 the actual low-pass kernel has L1 mass1. Pathwise Jensen/Tonelli gives ||f||_L2<=||w(.-h)||_L2=||w||_L2, with negative history zero. This does not require deterministic w. The filter/delay preserves adaptedness, so Itô isometry and Tonelli give

    E integral_0^infinity d_t²dt
      =(1/(2epsilon)) E integral_0^infinity f_s²ds
      <=g² E integral_0^infinity w_s²ds,

where epsilon=2^-29 and g=1/sqrt(2epsilon)=2^14=16384. The upper bound is uniform over ALL progressive square-integrable disturbances. It is strictly below gamma16386.

For arbitrary initial homogeneous states with w=0, u=0 gives

    d E(f²+y²)/dt=-(2kappa-1)E f²-2epsilon E y²
                <=-2epsilon E(f²+y²),

since 2kappa-1>=2epsilon. This proves internal exponential mean-square stability, not just a zero-state gain statement. The controller u=0 is within the actual book information form.

### 2. Stopped Brownian input and the strict denominator gap

Base lines109–152 take tau as the first exit of W from(-1,1), and w=1_(t<tau). This is progressively measurable, not anticipating. For finite t, M_t=W_(t∧tau) is bounded by1 and Itô isometry gives E(t∧tau)=E M_t²<=1. Monotone convergence yields E tau<=1 and hence tau<infinity almost surely; Brownian continuity then gives |W_tau|=1. Dominated convergence of M_t² proves E tau=1 exactly.

The event W_(1/2)>=1 forces an exit by1/2. On x in[3/2,2], e^(-x²/2)/sqrt(2pi)>1/27 from e<3 and pi<4, and the interval has length1/2. Thus P(tau<=1/2)>1/54. The exact identity

    (1+t)/2-sqrt(t)=(sqrt(t)-1)²/2

with E tau=1 implies E sqrt(tau)=1-(1/2)E(sqrt(tau)-1)². On the stated event the square exceeds1/16 because1/sqrt2<3/4. Therefore

    E sqrt(tau)<1-1/1728<1-1/2048=1-delta.

The input has N2(w)=1 but N1(w)<1-delta. This is a fixed admissible disturbance for every controller, not a controller-dependent deterministic-input replacement.

### 3. OU lower anchor and actual positive-preview/filter error

For the ideal comparison Z_t=integral_0^t exp(-epsilon(t-s))w_s dW_s, integration by parts gives Z_t=M_t-epsilon integral_0^t exp(-epsilon(t-s))M_sds. At tau, |Z_tau|>=1-epsilon tau. After tau its forcing stops and the remaining infinite path energy is exactly g²|Z_tau|². On tau<=R=2^14, epsilon R=delta/16 and P(tau<=R)>=1-1/R=1-delta/8, so

    N1(Z)>=g(1-delta/16)(1-delta/8)>=g(1-delta/4).

The comparison is not silently substituted for the actual plant. Actual v=w(.-h) is the step on[h,h+tau], so its symmetric difference with w has length2min(h,tau)<=2h pathwise. The displayed low-pass solution has squared error relative to v equal to

    (1-e^(-2kappa tau))/(2kappa)
      +(1-e^(-kappa tau))²/(2kappa)
      =(1-e^(-kappa tau))/kappa<=1/kappa.

These calculations are valid pathwise for random tau and preserve adaptedness. Consequently N2(f-w)<=kappa^(-1/2)+sqrt(2h)=2^-13=delta/4. Isometry on the difference OU convolution then gives N1(d-Z)<=N2(d-Z)<=g delta/4=2. Hence N1(d)>=g(1-delta/2)=16380 for the ACTUAL delayed/filtered zero-control response. The strictly positive h was explicitly paid for.

### 4. The all-controller lower bound, including N1-only controls

For ANY realized adapted control, however nonlinear/history-dependent its generating rule, the linear plant equation decomposes pathwise as y=d+Su, with

    Su=deterministic stable convolution of u
        +stable Itô convolution of u.

This includes all preview pre-action: neither control nor plant is reset. The deterministic convolution has pathwise-L2 gain epsilon^-1, the stochastic convolution mean-square gain g. Minkowski gives N2(Su)<=(epsilon^-1+g)N2(u) uniformly over adapted L2 controls.

For completeness, the used transfer is valid for S. Set accumulated output/input energies X_t and G_t=M2² integral_0^t u². They are continuous, nonnegative and increasing, and G is predictable. Stopping u at ANY bounded stopping time leaves S-output unchanged up to that time; its full N2 bound therefore dominates E X_tau by E G_tau. Multiplying stopped inputs by events in F0 proves the conditional version, since S is linear/event-local/zero-preserving. These are the actual hypotheses of the freshly read monotone Lenglart theorem, giving

    N1(Su)<=sqrt2(epsilon^-1+g)N1(u)=M N1(u), M<2^31.

Finite N1(u) with infinite N2(u) is NOT excluded. Stop u at accumulated energy b, apply the preceding bound to the L2 stopped input, and use local pathwise uniqueness plus Fatou. On every sample path with finite total control energy, sufficiently large b leaves the whole input/output unchanged. This verifies the stated extension for S.

If N1(z)=infinity the attempted controller fails. Otherwise the separate r u channel forces N1(u)<infinity, so the extension applies. Put X=||y||_L2 and U=||u||_L2, pathwise. Triangle and weighted two-dimensional Cauchy–Schwarz give

    N1(d)<=E(X+MU)<=sqrt(1+(M/r)²)N1(z)=c_* N1(z).

Because r=2^43 and M<2^31, c_*<1+2^-24<1+delta/8. These estimates cover ALL realized adapted histories, not merely static gains or mean-square-finite controllers. In particular a controller using the full Brownian past is covered, a larger information class than required for the book.

### 5. Exact gamma margin and operative correction

Combining the fixed test input's N1(w)<1-delta with N1(d)>=g(1-delta/2) and c_*<1+delta/8 gives every controller

    N1(z)/N1(w)>g(1-delta/2)/((1-delta)(1+delta/8)).

The corrected additive-v1 algebra is

    (1-delta)(1+delta/8)(1+delta/4)
      =1-5delta/8-11delta²/32-delta³/32,

so its difference from1-delta/2 is delta/8+11delta²/32+delta³/32>0. Thus the ratio is strictly greater than g(1+delta/4)=16386. The base3/16 equality is not used. Strict positivity of the input norm and the denominator follows from tau>0 almost surely and0<delta<1.

### 6. Explicit finite counted horizon — additive v2

The extension uses T=R+8/epsilon=2^14+2^32 and counted input endpoint L=T-h. The stopped input is w^L=1_(0<=t<tau∧L), progressive and zero outside[0,L]; its N2 squared is E(tau∧L)<=1 and its N1 remains below1-delta. There is no hidden input on(T-h,T].

On tau<=R<L the stopped Brownian anchor reaches the genuine boundary, and after tau it decays. Its COUNTED energy is

    g² |Z_tau|²(1-e^(-2epsilon(T-tau))).

Here2epsilon(T-R)=16. Thus the tail factor is at most e^-16<2^-16<delta/16. Using sqrt(1-x)>=1-x, the finite output norm is bounded below by

    g(1-delta/16)²(1-delta/8)>=g(1-delta/4).

The three losses sum exactly delta/4. Restricting the already bounded full-horizon delay/filter error can only decrease its N1 norm, so the counted actual d^L still has N1>=16380. Extending a realized control by zero AFTER T for the linear-map estimate S changes no output on[0,T] by causality; it does not extend/reset the original feedback law. The same N1-localization and control-cost argument then proves the strict ratio>16386 on the correctly counted finite intervals. The u=0 mean-square upper bound for EVERY adapted counted input follows by zero extension and discarding the nonnegative output tail. No infinite tail is inserted into the finite performance norm.

## Comparison with the old gamma6 baseline and limits

Read the old `information-science/stochastic-hinf-preview-control/work/literal_continuation.md` definitions and L2 statement/proof ranges through its lower-bound certificate. At h=1,T=5, input interval[0,4], its effective-control constant-matrix example has literal feasibility at gamma6 for all adapted inputs but no mean-square feasible controller at that level. Its u=0 is not infinite-horizon internally mean-square stable. That is the OPPOSITE implication, and is not re-counted here.

The current packet supplies mean-square feasibility but printed infeasibility at gamma16386, with positive preview, B0!=0, direct drift control of y, and an internally stable exhibited law, on infinity and on one explicit finite horizon. Together the two DIFFERENT examples obstruct unqualified same-gamma substitution in either direction within the finite-horizon regime; this does not mean one plant/horizon displays both directions, does not identify either optimal gain, and does not contradict the factor-sqrt2 transfer.

General printed necessary-and-sufficient synthesis, sharp constants and novelty remain unresolved. The stopped-Brownian Jensen-gap mechanism and Lenglart theorem are classical. This review establishes no priority, human/formal acceptance or transitive certification of unrelated Riccati theory. The assigned bounded review is returned; I resume ordered Olson as my ONE primary problem.
