# F69 independent review: stochastic matrix preview gain gap

**Disposition: FATAL 0 / MAJOR 0 / MINOR 1 (provenance qualification below).** I reconstructed the stated all-input matrix result, including the imported elementary inequalities, and found no mathematical defect in that restricted result. This is an independent same-harness written review, not a parent adoption, human/cross-model review, formal proof, novelty assessment, or general synthesis result. The disposition is conditional on the explicitly listed standard mathematical imports and on the frozen source-bound definitions; it does not validate unpinned original-source material.

Observed clock before review creation: **2026-10-28T18:11:47-0700 PDT**. This is an observed pre-write clock, not a claimed exact file-creation time.

## Input binding and provenance finding

All three manifest inputs were read in full, in the declared order; their live SHA-256, byte counts and LF counts match the manifest. References `D`, `E`, and `M` below mean the following complete pinned files, respectively:

1. **D**, `written-releases/info-3-linear-preview-class-definitions-v1.md`, SHA256 `9b72aca5c3434827f43bc81e3fcd3cfc5f72d4ddbf4c7df3943444f10e9151cd`, 1087 bytes, 11 LF.
2. **E**, `information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-positive-two-tap-preview-causal-gain-gap.txt`, SHA256 `38cf215409528b869856e5d3e03e9ecf02a833bb1285f708be7ddde137d0a076`, 8301 bytes, 120 LF.
3. **M**, `information-science/evidence/three-area-20261027-96h/parallel-18/stochastic-hinf-preview/frontier-20261028-matrix-scalar-noise-preview-literal-gain-gap.txt`, SHA256 `0f81a9928080961daa665d5d23557874fa82866db169409c7cd140ba1aa482f8`, 10114 bytes, 115 LF.

The manifest is `manifest-v1.json`, SHA256 `46cc4e59bc1333e745816f812aa599dff00eac5aa52d86c11dd875a3dcbc3ee7`. No older verdict or held payload is imported. E's shape and weighting argument was reconstructed below, not accepted merely because E asserts it. M's finite diagnostics were neither replayed nor used to prove the theorem.

**MINOR — source provenance / breadth of the phrase “actual original” (D:3–11, M:7–19).** D identifies itself as Main's binding of the owner's proposed original-information class, in “verbatim substance,” and expressly says it supplements, rather than replaces, an earlier literal-criterion packet. That earlier packet and any book-original text are not among these pins and were not read here. The model and criterion match D exactly as described below; this review does not independently establish identity with any unpinned packet or original publication. This is not evidence of a conflict or a mathematical defect in M; retain the qualification when describing provenance.

## Exact statement and original-class match

Write `S=T-h>0`, `P=A+BK`, `b=B ell`, `g_v(t)=D exp(Pt)v`, and `G_v(x)^2=integral_0^x ||g_v(t)||^2 dt`. For finite `T>h>=0`, scalar progressive input `w` zero outside `[0,S]`, scalar Brownian motion and

```
dx = (P x + b w_t + c w_(t-h)) dt + sigma x dW,
z = D x,  x_0=0,
```

M considers `E||w||_L2[0,S]<infinity`. This is a subset of D's law with `A0=sigma I`, `B0=D1=0`, scalar disturbance, `L0=ell`, `Lh=0`, distributed kernel zero, and the same `K`. It includes every canonical progressive E2 disturbance by Cauchy–Schwarz. The criterion is the literal ratio `E||z|| / E||w||`, not root-mean-square energy nor an expectation of a pathwise ratio. Inputs in the ratio must have `E||w||>0`. The state-feedback law, horizon, zero history and input extension agree with D:5–7; no claims are made about D's other admissible laws.

For a nonzero output operator M supplies `0<epsilon<1` with

```
E||z|| <= (1-epsilon) Gamma E||w|| <= (1-epsilon) H E||w||.
```

Thus, in this fixed law and source-bound model, `0<G_det<=G_prog<Gamma<=H`, with the strict inequality uniform; `gamma=Gamma` is strictly feasible, as is any `gamma>(1-epsilon)H`. Gamma is an upper-bound construction, **not** asserted to be the true gain. When the output operator is zero, every positive gamma is strictly feasible but gamma zero is not strictly feasible for a nonzero input. No actual-gain endpoint, general controller synthesis, general multiplicative-noise matrix, B0/D1 extension, multivariate disturbance, infinite-horizon result, or E1/E2 endpoint-transfer result follows.

## Integrating factor, visibility and moments

For `nu(t,s)=exp[-sigma^2(t-s)/2+sigma(W_t-W_s)]`, the scalar noise commutes with `P`, so the linear Itô variation-of-constants solution gives the physical output column

```
K_s(t) = 1_(t>=s) nu(t,s) g_b(t-s)
       + 1_(t>=s+h) nu(t,s+h) g_c(t-s-h),
z_t = integral_0^S K_s(t) w_s ds.
```

For E1 inputs the forcing is time-integrable pathwise; localization supplies the usual solution, and the pathwise integral is well-defined. For fixed `s`, `K_s` depends only on Brownian increments after `s`; it is independent of `F_s`. Its joint measurability plus Tonelli gives the expectation steps below even without an E2 input moment.

By Cayley–Hamilton and analyticity, `v` is invisible iff `D P^j v=0` for all `0<=j<n`, equivalently `g_v` is identically zero; otherwise `G_v(x)>0` for every `x>0`. For `h>0`, an uncancellable prefix of length `h` exposes a visible `b`; if `b` is invisible, the delayed `c` is the only output column. For `h=0` the two terms share the same noise factor and combine to `g_(b+c)`. Hence M:36–41's zero conditions are exactly: both `b,c` invisible when `h>0`, or `b+c` invisible when `h=0`. The converse and positivity of the deterministic gain are justified in the last section, without assuming a maximizing input.

Let `C(s)=E||K_s||`, `Gamma^2=integral C(s)^2 ds`, `ell0(s)=||E K_s||`, and `H^2=integral E||K_s||^2 ds`, with output-time Hilbert norm. All integrals are over the stated finite horizons. In a nonzero case `ell0(s)>0` for `s<S`: the early prefix supplies it if `b` is visible; otherwise the visible remaining delayed/combined vector has positive energy on `S-s>0`. Jensen and Cauchy–Schwarz give `ell0<=C`, `0<Gamma<=H<infinity`.

The all-sign formula M:47–55 follows directly. For the late region set `v=t-s-h`, `X=nu(s+h,s)`, `Y=nu(s+h+v,s+h)`, `a=g_b(h+v)`, `d=g_c(v)`. Independent increments give `EX=1`, `EX^2=exp(sigma^2 h)`, `EY=1`, `EY^2=exp(sigma^2 v)` and

```
E||Y(Xa+d)||^2
 = exp(sigma^2 v) [ ||a+d||^2 + (exp(sigma^2 h)-1)||a||^2 ].
```

Consequently, with `s` integrated over `[0,S]`,

```
ell0(s)^2 = integral_0^h ||g_b(v)||^2 dv
          + integral_0^(S-s) ||g_b(h+v)+g_c(v)||^2 dv,
H^2 = S integral_0^h exp(sigma^2 v)||g_b(v)||^2 dv
    + integral_0^S (S-v) exp(sigma^2 v)
      [ ||g_b(h+v)+g_c(v)||^2
        +(exp(sigma^2 h)-1)||g_b(h+v)||^2 ] dv.
```

These formulas are nonnegative without a sign assumption. For `h=0` the first integral is empty and the bracket is `||g_(b+c)(v)||^2`; for `sigma=0` the variance term vanishes, as it must. Output cancellations are present in the squared sum; for nonzero noise they do not erase the additional variance term.

## Uniform constants and vector-column separation

For each nonzero case take `delta=S/8`, `I=[S/4,S/3]`, `J=[2S/3,3S/4]`, any `r0>0`, and define

```
f0=ell0/H,
b0=||f0 1_[0,delta]||_2,   bI=integral_I f0,   bJ=integral_J f0,
eta=min{bI/(2 sqrt(|I|)), bJ/(2 sqrt(|J|))},
p0=P(sup_(0<=v<=T-delta)|beta_v|<=r0)>0,
m=exp[-sigma^2 T/2-2|sigma|r0],  M=1/m.
```

For the three nonzero visibility cases the reviewed choices `(Q,P0,lambda_I,lambda_J)` are

```
h>0, b visible:    (G_b(T)+G_c(T), m G_b(min(h,S/3)), m G_b(h), m G_b(h));
h>0, b invisible:  (G_c(T), m G_c(S/3), m G_c(2S/3), m G_c(S/4));
h=0:               (G_(b+c)(T), m G_(b+c)(S/3),
                    m G_(b+c)(2S/3), m G_(b+c)(S/4)).
```

In the second and third rows the displayed visible vector is required to be visible. Put

```
xi=1-sqrt(1-P0^2/(M^2 Q^2)),
cI=lambda_I bI/2,  cJ=lambda_J bJ/2,
epsilon=min{p0^2 b0^2/[128(1+p0)^2], p0 eta^2/16,
            xi cI cJ p0^2/(8H^2)}.
```

Every factor is positive. Here `P0<=m Q<=M Q`, so the square root is real and `xi>0`; since `f0<=C/Gamma` and the latter has unit L2 norm, `b0<=1`, making the first epsilon term strictly below 1. The small-ball event is positive even at `sigma=0`; that choice merely yields a conservative constant.

On `A={sup_(delta<=t<=T)|W_t-W_delta|<=r0}`, all scalar factors `nu(t,s)` with `delta<=s<=t<=T` lie in `[m,M]`. Thus `||K_s||<=M Q`. If `s in I`, `u in J`, then `u-s>=S/3`. In the visible-`b` case, before `min(s+h,u)` the `s` column is exactly its immediate component while the `u` column is zero. This interval has length at least `min(h,S/3)` and supplies norm at least `P0`; the full initial interval `[s,s+h)` supplies `lambda_I=lambda_J=mG_b(h)` despite any later destructive cancellation. If `b` is invisible, use `[s+h,u+h)` and `g_c`; if `h=0`, use `[s,u)` and `g_(b+c)`. The stated lower bounds for the whole columns follow from `S-s>=2S/3` on I and `S-u>=S/4` on J.

Projecting the `s` column off that prefix gives the absolute, vector-valued estimate

```
|<K_s,K_u>| <= sqrt(1-P0^2/(M^2 Q^2)) ||K_s|| ||K_u||
              = (1-xi)||K_s||||K_u||.
```

Absolute value is essential: it covers vector orientation and either sign of the scalar input. This handles `h=0`, invisible `b`, opposite tap signs and later output cancellations without relying on positivity of the physical columns.

## Progressive E1 shape, future weighting and loss

Let `U=||w||`, `O=||integral K_s w_s ds||`, `R=integral |w_s| ||K_s|| ds`. Since the input is `F_s`-measurable and each full column is future-independent,

```
E R = integral C(s) E|w_s| ds <= Gamma E U,
O<=R.
```

Tonelli and the last bound show `R,O` are integrable for E1; no second moment of `w` is used. Normalize `E U=1`. Define `f=C/Gamma`; on `U>0`, set `v=|w|/U`, `e=||v-f||`, and put `e=0` on `U=0`. With `q=1-E O/Gamma>=0`, the unit-vector identity gives

```
Gamma-E R = (Gamma/2) E[U e^2],
E[U e^2] <= 2q.
```

Crucially, `U` need not be `F_delta`-measurable nor independent of the future event. Instead `Lambda=||w 1_[0,delta]|| / ||f 1_[0,delta]||` is `F_delta`-measurable. The reverse triangle inequality and weighted Cauchy–Schwarz give `E|U-Lambda|<=sqrt(2q)/b0`. Brownian independent increments then yield

```
E[U 1_A] >= p0-(1+p0)sqrt(2q)/b0.
```

If `q` is at most the first epsilon term, this is at least `7p0/8`. If `q` is at most the second, `E[U 1_(e>eta)]<=2q/eta^2<=p0/8`. With `R0=4H/p0`, Markov applied to the nonnegative integrable R gives `E[U 1_(R>R0 U)]<=E R/R0<=p0/4`. Consequently the intersection of A, `e<=eta`, and `R<=R0 U` has U-weight at least `p0/2`.

Because `f>=f0`, Cauchy–Schwarz on I and J yields, on `e<=eta`,

```
integral_I |w_s| ||K_s|| ds >= cI U,
integral_J |w_s| ||K_s|| ds >= cJ U.
```

Expanding `R^2-O^2` as a double integral, each pair contributes a nonnegative Cauchy–Schwarz deficit; the I-by-J and J-by-I pairs have at least the additional `xi` deficit even for opposite signs of `w`. Thus `R^2-O^2>=2xi cI cJ U^2`. On the weighted intersection, `R+O<=2R0 U`, so `R-O>=xi cI cJ U/R0` (the `U=0` case contributes nothing). Therefore

```
Gamma q >= E(R-O) >= xi cI cJ p0^2/(8H),
q >= xi cI cJ p0^2/(8H Gamma) >= xi cI cJ p0^2/(8H^2).
```

If either preliminary condition on q fails, q is already at least that preliminary epsilon term. This verifies all three constants and the uniform gap for every progressive E1 input; it does not assume that `U` itself is independent of the event.

## Strictly positive gain and independent exact evidence

On each Brownian-continuous sample path, the kernel is Hilbert–Schmidt. In each nonzero visibility case its exposed transfer prefix has positive time measure, so the corresponding deterministic-input operator is nonzero. Fix a countable dense family of deterministic L2 inputs. If every member mapped to zero on a path, continuity would make the operator zero, a contradiction. Hence their positive-output events cover the probability-one set of continuous paths; one fixed deterministic input has positive-probability nonzero output. The E1 bound ensures its output norm is integrable. This establishes `G_det>0` and therefore `G_prog>0`, without selecting an optimizer.

Independent analytic calculations, including an all-input bound, are saved in `exact-specializations-v1.txt`, SHA256 `d33f3e92bdf432967fa525bda5e27f0bb65a9f6aeeafc09324c88fbb1718979f`. In particular, with `P=0`, `D=1`, `b=1`, `c=-1`, `T=2`, `h=1`, `sigma=0`, the kernel is exactly `1_[s,s+1)` and `Gamma=H=1`. Its normal operator has kernel `1-|s-u|` and Hilbert–Schmidt norm `1/sqrt(2)`, giving the pathwise all-input bound `||z||<=2^(-1/4)||w||`; deterministic `w=1` gives squared output norm `2/3`. Thus in this specialization Gamma is provably not the true gain. For the same opposite taps with `sigma=1`, the late mean cancels but independent Gaussian increments give the exact `H^2=(e-1)^2`. The evidence additionally checks a partially cancelling two-output vector case and an invisible-immediate/visible-delayed case. Exact rational arithmetic cross-checked the displayed polynomial coefficients and integral constants; finite simulations were not used.

## Imports and exclusions

Imports are the scalar-noise Itô integrating factor with localization, Brownian independent increments and finite-time small-ball positivity, Gaussian exponential moments, matrix exponential analyticity and Cayley–Hamilton, Tonelli/measurable Bochner integration, Jensen, Hilbert-space Cauchy–Schwarz and separability. No earlier proof verdict, source outside the manifest, author diagnostic, author contact, external model, or numerical simulation is used as an authority for the all-input claim. This review does not certify the unpinned earlier literal-criterion packet, scientific novelty, or any of the broader endpoints excluded above.
