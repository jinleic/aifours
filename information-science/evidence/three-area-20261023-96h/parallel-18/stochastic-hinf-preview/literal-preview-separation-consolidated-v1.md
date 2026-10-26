# Literal stochastic H-infinity preview: consolidated horizon-dependent separation manuscript

**InfoHinfPreview, info-3. WRITTEN CANDIDATE ONLY.** Actual returned clock before creation: **Sun Oct 25 05:16:23 PDT 2026** (`/bin/date`). This is the requested **ONE consolidation**, after completing and returning v31-A, v32-C and v35-A, rather than a fourth standalone same-target increment.

This manuscript consolidates the three resumed primary packets, preserves their exact horizon/controller scopes, and adds one quantitative written Gaussian-gap argument leading to **one** precisely bounded next attack: a rational enclosure of one deterministic Sturm–Liouville eigenvalue. No scientific interpreter, arithmetic/symbolic program, enumeration, replay, solver or simulation was used for this consolidation or its new written argument.

## 0. Mandatory assurance correction and source fidelity

Parent erratumv7 and `permission-withdrawal-addendum-v1.json` are mandatory. The parent's checkpoint026 exception for scientific eval arithmetic was erroneous and withdrawn. The earlier four actual eval submissions are preserved and disclosed: three successful arithmetic cells and one first-line failed optional Sympy import. They have **no executable-verification, finite-certificate or retroactive-admission credit**. The now-withdrawn permission came from the parent, not an owner refusal of instructions. No scientific computation has been performed by this owner since receipt of the correction.

Accordingly this consolidation is **written mathematics**, not WRITTEN_CHECKED_IN_KERNEL, formal proof, independent-model review or parent acceptance. Displayed rational identities are written algebraic claims; earlier interpreter output is not their verification. All source snapshots remain unchanged. Fresh metadata-only source hashes matched the existing pins:

| Source in this root | SHA-256 |
|---|---|
| `proof-general-parameter-separation-v1.md` | `58777c6e1b7b83766d0a969cfd0dbca4b41729577de732ece5dd2a1ad861d575` |
| `proof-short-horizon-conditioning-v1.md` | `67c606ea9115e3a5f563b60892d2f7d706337bd7cc6aa68b7d49c62f1f8a84c8` |
| `proof-short-horizon-strict-gap-and-opposite-family-v1.md` | `c21d32783c9301c8db726ca896105056001912128d37324123b901790ad98c04` |
| `permission-withdrawal-addendum-v1.json` | `0fe2dc5d8fb20c1ae9a3bc7b26271c98a0a659878410d2f67acb77231f8c2cb1` |
| older comparison packet `proof-v1.md` | `895a36cdc42565aa7b7b6fd4279a34aba6b3bb7f0c8918d14e49d59b72f5635c` |
| saved Geiss–Scheutzow primary PDF | `0d8c9c63e68a3b68ad59def132640b3f9c3432c91aa76283d690b1e9f8bb13ce` |

The older comparison packet's scoped review history remains its own history, recorded in the round's `preview-full-packet-parent-v1.md`. It does not supply independent acceptance of any new statement here. The old reverse-separation packet still travels with its mandatory algebra addendum; no frozen equality is silently repaired by this successor.

## 1. Literal target and consolidated scope ledger

The actual book images at printed674–675 define the pathwise time-L2 norm and then put expectation **outside** it. Write

$$N_1(v;I)=E\left(\int_I|v_t|^2dt\right)^{1/2},\qquad
N_2(v;I)=\left(E\int_I|v_t|^2dt\right)^{1/2}.$$

Use the openly disclosed precision conventions of `selection-v1.md`: zero initial state/history, progressive disturbances with finite expected squared energy, strong nonanticipative well-posedness and local pathwise square integrability of realized controls. A finite horizon counts output on `[0,T]` and input **exactly on `[0,T-h]`**. Infinite input/output intervals are `[0,infinity)`.

The full unsolved synthesis target remains

$$\exists F:\ \sup_{w\ne0}{N_1(z_{F,w})\over N_1(w)}<\gamma$$

for general constant-matrix plant data and the book's state/preview-window information. No general N&S theorem is claimed.

The consolidated results are:

| Regime/result | Exact delivered scope |
|---|---|
| Long/infinite separation | A rational algebraic screen on general cascade parameters certifies mean-square feasibility but **all-controller literal infeasibility** at the same gamma; constructive rational members exist for every positive rational h,gamma, on the infinite horizon and a supplied sufficiently long finite horizon. |
| Short horizon `h<T<=2h` | For the zero law the full-adapted literal gain reduces legitimately to a deterministic-input Gaussian norm and is **strictly below** its mean-square gain. |
| Opposite short-horizon separation | For every positive rational h,T,gamma with `h<T<=2h`, rational output/control scales exist making the zero law literal-feasible but **every controller** mean-square-infeasible at gamma. This first existence statement is nonconstructive. |
| NEW quantitative bridge | Under tame damping/filtering, an explicit uniform relative Gaussian gap and a rational spectral-bracket certificate reduce coefficient extraction to one ground-eigenvalue enclosure. No enclosure has been executed or claimed. |

The two directions compare separately stated plants/horizons. No assertion that a single plant at one gamma has contradictory feasibility properties, or that either finite-horizon converse holds on the infinite horizon, is made.

## 2. One actual constant-matrix cascade and its control-cost exclusion

All families use

$$
\begin{aligned}
 df_t&=\kappa[-f_t+c w(t-h)]dt,\\
 dy_t&=(-\varepsilon y_t+b u_t)dt+(\sigma f_t+\beta u_t)dW_t,\\
 z_t&=(d y_t,r u_t)^T.
\end{aligned}                                                     \tag{2.1}
$$

Here epsilon,kappa,h,r are positive, `c*sigma*d != 0`, and b,beta may be chosen nonzero to retain effective drift AND diffusion actuation. Negative-time disturbance history is zero. In book notation,

```
A=diag(-kappa,-epsilon), B=(0,b)^T, C=(kappa*c,0)^T,
A0=[[0,0],[sigma,0]], B0=(0,beta)^T,
D0=[[0,d],[0,0]], D1=(0,r)^T.
```

The actual r*u output has full positive control penalty. With u0 and zero input, the positive storage

$$V_0={\sigma^2+1\over2\kappa}f^2+y^2$$

satisfies

$$\frac{d}{dt}EV_0=-Ef^2-2\varepsilon Ey^2
\le-\min\{2\kappa/(\sigma^2+1),2\varepsilon\}\,EV_0.$$

Thus every exhibited zero law is internally exponentially mean-square stable.

For a realized progressive control, irrespective of the law producing it,

$$d y=d y^0+S_d u,$$

$$S_d u(t)=d b\int_0^t e^{-\varepsilon(t-s)}u_sds
       +d\beta\int_0^t e^{-\varepsilon(t-s)}u_s dW_s.$$

Choose U>0 with `2epsilon*U^2>=1` and put

$$\overline M=|d|\left({|b|\over\varepsilon}+|\beta|U\right).$$

Deterministic convolution, Itô isometry and Tonelli give

$$N_2(S_d u)\le\overline M N_2(u).                            \tag{2.2}$$

For the literal control bound the named non-elementary import is Geiss–Scheutzow, [arXiv:2101.10884v2 Theorem2.2](https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2), at `p=1/2`. Accumulated output/input energies of this causal linear map are nonnegative nondecreasing adapted continuous processes; the input energy is predictable. Stopping the INPUT at each bounded stopping time preserves its earlier output, and discarding its later nonnegative output gives the required energy domination from (2.2). Applying the same argument on an initial event gives the theorem's conditional domination. Hence

$$N_1(S_d u)\le\sqrt2\,\overline M N_1(u).                   \tag{2.3}$$

For finite N1 controls with infinite N2, stop accumulated control energy at n, apply the square-energy bound and use local uniqueness/causality and Fatou. On each finite-total-energy path, sufficiently large stops change nothing. For finite time extend the realized control by zero only as input to S_d; the actual feedback law is not extended, reset or given energy-history information.

Consequently every controller with finite output norm obeys

$$N_1(d y^0)\le\sqrt{1+2\overline M^2/r^2}\,N_1(z),           \tag{2.4}$$

$$N_2(d y^0)\le\sqrt{1+\overline M^2/r^2}\,N_2(z).           \tag{2.5}$$

The separate r*u channel supplies the needed finite control norm; infinite output already fails. Triangle plus two-dimensional Cauchy–Schwarz proves both inequalities. These exclusions allow the enlarged class of all progressive realized controls, including nonlinear/nonstationary history dependence and preview pre-action, not just linear feedback.

## 3. A common square-root deficit identity

If `X>=0`, `E X=1` and its third moment is finite, put

$$v=E(X-1)^2,\qquad w=E[(X-1)^2(X+1)].$$

When w>0,

$$1-E\sqrt X\ge{v^2\over4w}.                                \tag{3.1}$$

Indeed `E sqrt(X)=1-(1/2)E(sqrt(X)-1)^2`. Also

$$E(\sqrt X-1)^2
=E{(X-1)^2\over(\sqrt X+1)^2}
\ge\tfrac12 E{(X-1)^2\over X+1}
\ge\tfrac12{v^2\over w}.$$

The last step is Cauchy–Schwarz. This written identity drives both the stopped-input denominator and the new Gaussian output gap; it does not substitute one random denominator for another.

## 4. General rational long/infinite separation screen

Define

$$H^2={(c\sigma d)^2\over2\varepsilon},\qquad q_0={103\over108},
\qquad E_0={p+q\over a}$$

for positive certificate parameters a,p,q,rho,eta,gamma, and require

$$\kappa p^2\ge1,\quad q^2\ge2h,\quad2\varepsilon U^2\ge1,$$

$$2\overline M^2<r^2\rho(2+\rho),\qquad H^2<\eta^2<\gamma^2.  \tag{4.1}$$

For infinite time set

$$Q_\infty=1-\varepsilon a^2-E_0.$$

Require `Q_infinity>0` and

$$H^2Q_\infty^2>\gamma^2q_0^2(1+\rho)^2.                    \tag{4.2}$$

For finite time choose R>0, integer m>=1, require

$$T-h\ge a^2R,\qquad2\varepsilon(T-a^2R)\ge m,$$

and set

$$Q_T=(1-2^{-m})(1-\varepsilon a^2-5/(3R^2))-E_0.$$

Require `Q_T>0` and

$$H^2Q_T^2>\gamma^2q_0^2(1+\rho)^2.                         \tag{4.3}$$

These are rational algebraic conditions when the data are rational. In particular epsilon need not be the reciprocal of twice a rational square; H is never numerically evaluated in checking the squared conditions.

### 4.1 Exact stopped-input denominator

For Brownian exit time tau from `(-1,1)` starting at0,

$$E\tau=1,\quad E\tau^2=5/3,\quad E\tau^3=61/15.$$

A written derivation uses the bounded nonnegative polynomials

$$\mu_1=1-x^2,\quad\mu_2=(5-6x^2+x^4)/3,\quad
\mu_3=(61-75x^2+15x^4-x^6)/15,$$

with `mu_j''/2=-j*mu_(j-1)` and zero boundary values. Stop Dynkin first at `tau wedge t`; mu1 proves finite exit expectation and a.s. exit. Bounded convergence removes the terminal term. Inductively the strong Markov property and Tonelli identify the remaining integrals with exit moments, without assuming them finite in advance. Nonnegativity follows from `(1-x^2)(5-x^2)` and `(1-x^2)(61-14x^2+x^4)` for the latter polynomials.

In (3.1), X=tau has `v=2/3`, `w=12/5`, giving `E sqrt(tau)<=103/108`. By Brownian scaling, for `tau_a=inf{t:|W_t|=a}`,

$$E\tau_a=a^2,\qquad E\tau_a^2=5a^4/3,\qquad
E\sqrt{\tau_a}\le a q_0.$$

Use the single controller-independent input `w=1_(t<tau_a)` in infinite time; on finite input interval L=T-h use `w=1_(t<tau_a wedge L)`. In both cases `0<N1(w)<=a q0` and expected squared input energy is finite.

### 4.2 Actual OU endpoint, delay and filter

For the ideal comparison `Z_t=integral_0^t exp[-epsilon(t-s)]w_s dW_s`, integration by parts with stopped Brownian M gives

$$Z_t=M_t-\varepsilon\int_0^t e^{-\varepsilon(t-s)}M_sds.$$

At the genuine exit, `|M|<=a` and `|M_tau_a|=a`, so

$$|Z_{\tau_a}|\ge a e^{-\varepsilon\tau_a}
                  \ge a(1-\varepsilon\tau_a).$$

After exit the ideal response decays deterministically. Averaging its exact infinite tail therefore gives

$$N_1(Z)\ge{a\over\sqrt{2\varepsilon}}(1-\varepsilon a^2).$$

For finite time restrict to `tau_a<=a^2 R<=L`. Markov's inequality at the second moment loses at most `5/(3R^2)` in event probability, while the endpoint average loses only `epsilon*a^2`, not `epsilon*a^2 R`. The COUNTED tail factor is at least `1-2^-m`, because `2epsilon(T-a^2 R)>=m`, e>2 and `sqrt(1-t)>=1-t`. Hence

$$N_1(Z;[0,T])\ge{a\over\sqrt{2\varepsilon}}
 (1-2^{-m})(1-\varepsilon a^2-5/(3R^2)).$$

The actual first state is c times the first-order filter of the delayed input. For a unit step of any stopped duration theta, its rise/tail identity is

$$\int_0^\infty|f/c-w(.-h)|^2dt=(1-e^{-\kappa\theta})/\kappa.$$

The delayed and unshifted steps differ on a set of length at most2h. Thus `N2(f/c-w)<=p+q`. Itô isometry bounds the actual performance-output error from `d*sigma*c*Z` by `H(p+q)`. In finite time the extended error is only an UPPER estimate, then restricted to the counted output; no infinite tail is inserted into the lower bound.

Therefore

$$N_1(d y^0)\ge H a Q,$$

where Q is the appropriate positive Q_infinity or Q_T. Combining with (2.4) and (4.1) proves, for EVERY controller,

$$G_1(F)\ge {HQ\over q_0(1+\rho)}>\gamma.                   \tag{4.4}$$

### 4.3 Genuine mean-square feasibility and strict storage

The deterministic low-pass kernel has L1 mass1, so its pathwise squared-energy contraction and Itô isometry give `G2(u=0)<=H<eta<gamma` for all progressive square-energy disturbances. Internal stability was proved in section2.

There is a strict quadratic certificate with

$$\alpha=\eta^2-H^2>0,\qquad
P=\operatorname{diag}\left(\eta^2/(\kappa c^2),
                    (\eta^2+H^2)/(2c^2\sigma^2)\right).$$

For `Cv=(kappa*c,0)^T`, `N=[[0,0],[sigma,0]]`, `Z=(0,d)`, the bounded-real matrix has exact quadratic form

$$
(f,y,v)\begin{pmatrix}A^TP+PA+N^TPN+Z^TZ&PC_v\\C_v^TP&-\eta^2\end{pmatrix}(f,y,v)^T
=-{\alpha\over2c^2}f^2-{\varepsilon\alpha\over c^2\sigma^2}y^2
 -\eta^2(v-f/c)^2.
$$

All weights are positive, and the zero set is only the origin. Itô retains the sigma-squared correction and the actual martingale. Bounded state/input-energy stopping, expectation, Fatou and monotone convergence give the true mean-square inequality. The finite delayed input equality is exactly `integral_0^T v^2=integral_0^(T-h)w^2`. No Riccati theorem has been imported or contradicted.

### 4.4 Constructive rational family for every positive h,gamma

Choose a>0 with `a^2>=2^17 h`; for rational h,gamma, `a=512*(1+h)` is one rational choice. Set

$$
\begin{gathered}
c=\sigma=b=\beta=1,\quad\varepsilon=1/(512a^2),\quad\kappa=(512/a)^2,\\
d=4\gamma/(65a),\quad p=q=a/256,\quad U=17a,\quad\rho=1/128,
\quad\eta=129\gamma/130,\\
\overline M=d(512a^2+17a),\quad r=16\overline M,\quad
R=32,\quad m=8,\quad T=2080a^2.
\end{gathered}
$$

Then `H=64*gamma/65`, the control slack after division by r-squared is `129/16384`, and

$$\eta^2-H^2={257\over16900}\gamma^2,\qquad
\gamma^2-\eta^2={259\over16900}\gamma^2.$$

The finite input endpoint is beyond32a-squared and its tail exponent is8. The written rational level comparisons are

$$Q_\infty={507\over512},\quad Q_T={258137\over262144},\quad
{\gamma\over H}q_0(1+\rho)={287885\over294912},$$

with respective positive differences4147/294912 and20153/2359296. Thus

$$\inf_FG_2(F)\le{64\over65}\gamma<\gamma,$$

$$\inf_FG_1(F)\ge{22464\over22145}\gamma>\gamma\quad(T=\infty),$$

$$\inf_FG_1(F)\ge{2323233\over2303080}\gamma>\gamma
\quad(T=2080a^2).$$

These are bounds, not exact optimal gains. The finite theorem supplies T rather than accepting every preassigned T>h. All positive-preview, actuation and stability conditions remain present.

## 5. Short-horizon conditioning and an exact compact operator

Now let `h<T<=2h`, L=T-h, and take base output scale `d=1`. For deterministic phi define Rphi as the random zero-law y path and

$$
(A_L\phi)(t)={\sigma\kappa c\over\sqrt{2\varepsilon}}
\sqrt{1-e^{-2\varepsilon(L-t)}}\int_0^t e^{-\kappa(t-s)}\phi(s)ds.
$$

Itô isometry/Tonelli, valid even for progressive random w, gives

$$E\|y^0\|_{L^2(0,T)}^2=E\|A_L w\|_{L^2(0,L)}^2.$$

Thus `G2(0)=m=||A_L||` for every h,T, not only the short regime. A_L is nonzero and Hilbert–Schmidt. Its squared norm is the largest eigenvalue of the positive compact integral operator with kernel

$$K(s,t)={(\sigma\kappa c)^2\over2\varepsilon}
\int_{\max(s,t)}^L(1-e^{-2\varepsilon(L-v)})e^{-\kappa(2v-s-t)}dv.$$

For short time, the ENTIRE random input on `[0,L]` is measurable at F_L before any output noise starts at h. Future Brownian increments are independent of it. With `J(phi)=E||Rphi||`, conditioning gives

$$E[\|y^0\|\mid F_L]=J(w).$$

J is continuous because `|J(phi)-J(psi)|<=||A_L(phi-psi)||`. Therefore the conditional identity follows first for simple L2-valued F_L variables, then by square-mean approximation. No anticipative approximant is asserted as an admissible input before L.

It follows, preserving the RANDOM denominator, that

$$G_1(0)=\ell=\sup_{\|\phi\|\le1}J(\phi)\le m.$$

This conditioning would be invalid when L>h, where the complete input can depend on some output increments. It is not blanket Jensen on an adapted-input ratio.

### Strictness, not just a weak inequality

A maximizing sequence for J in the Hilbert unit ball has a weakly convergent subsequence phi_n to phi_*. Compactness of A_L gives `||A_L(phi_n-phi_*)||->0`, hence the random responses converge in `L2(Omega;L2(time))`. Thus J attains its positive maximum at phi_*, of norm1.

For deterministic phi_*, the response is a nonzero centered Gaussian Hilbert variable. Its norm cannot be a.s. constant: a nonzero Gaussian scalar projection would otherwise be bounded, contradicting its unbounded Gaussian support. Strict Cauchy–Schwarz therefore gives

$$0<\ell=E\|R\phi_*\|<\big(E\|R\phi_*\|^2\big)^{1/2}
\le m.                                                        \tag{5.1}$$

Pointwise strict Jensen alone would not justify a strict inequality of suprema; compact attainment is the necessary extra step.

## 6. Opposite all-controller separation on every prescribed rational short horizon

Fix any positive rational h,T,gamma with `h<T<=2h`, rational positive epsilon,kappa, and nonzero rational c,sigma,b,beta. Let ell<m be the base `d=1` norms above. Choose rational

$$\gamma/m<d<\gamma/\ell.$$

Choose rational U with `2epsilon U^2>=1`, set `Mbar=d(|b|/epsilon+|beta|U)`, and choose rational r sufficiently large that

$$r^2(d^2m^2-\gamma^2)>\gamma^2\overline M^2.                \tag{6.1}$$

These choices exist by rational density and the Archimedean property. The zero law has literal gain d*ell<gamma. But (2.5) gives, for every actual controller,

$$G_2(F)\ge {dm\over\sqrt{1+(\overline M/r)^2}}>\gamma.$$

Controls of infinite mean-square output already fail; otherwise the penalty forces finite N2(u), legitimizing (2.2). All preview pre-action is charged in the realized S_d map. A deterministic maximizing input for the compact mean-square operator supplies the same lower bound against every controller.

Thus rational plants exist on EVERY prescribed rational short horizon/level with literal feasibility but all-controller mean-square infeasibility. The existence choices above are nonconstructive in their unevaluated ell,m endpoints. No explicit evaluated numerical d,r is supplied by this theorem. Both actuation channels can be nonzero and internal stability of u0 holds as before.

The long-horizon screen cannot incorrectly claim the reverse direction here. If T<=2h, its finite conditions imply `a^2R<=h` and `E0>=sqrt(2R)`. For R>=1/2 this makes E0>=1 and Q_T<0; for R<1/2 the tail-probability term alone makes its parenthesis negative. Thus its required positive Q_T is impossible in the short regime, consistent with the conditioning theorem.

## 7. NEW quantitative Gaussian bridge inside this consolidation

This section is new WRITTEN reasoning, not an interpreter calculation.

For a centered Gaussian Hilbert variable Y with covariance C and `q=Tr(C)>0`, put

$$s_2={\operatorname{Tr}(C^2)\over q^2},\qquad
s_3={\operatorname{Tr}(C^3)\over q^3}.$$

Diagonalizing the positive trace-class covariance and using independent normal coordinates gives

$$E(\|Y\|^2/q)^2=1+2s_2,$$

$$E(\|Y\|^2/q)^3=1+6s_2+8s_3.$$

The scalar Gaussian moments1,3,15 follow by integration by parts; finite-coordinate truncations and monotone convergence give these formulas in Hilbert space. Applying (3.1) to `X=||Y||^2/q` yields

$$E\|Y\|\le\sqrt q\left(1-{s_2^2\over4s_2+8s_3}\right)
\le\sqrt q(1-s_2/12),                                      \tag{7.1}$$

because nonnegative covariance eigenvalues normalized by q give `s3<=s2`. This is quantitative; it does not assume finite Gaussian rank.

Assume now

$$\kappa L\le1/2,\qquad\varepsilon L\le1/4.                 \tag{7.2}$$

For any deterministic unit input phi, let `v(t)=E y(t)^2` on active time `[0,L]`, with base `d=1`, and write

$$B=\sigma^2\kappa^2c^2L^2.$$

Cauchy–Schwarz on the filtered input and Itô isometry give `0<=v(t)<=B`. Hence `q=integral v<=BL`. The OU covariance is

$$C(s,t)=e^{-\varepsilon(t-s)}v(s)\quad(s\le t).$$

As `e^-2epsilon L>=1/2`, its squared Hilbert–Schmidt norm satisfies

$$\operatorname{Tr}(C^2)
=2\int_0^L\int_s^L e^{-2\varepsilon(t-s)}v(s)^2dtds
\ge\int_0^L(L-s)v(s)^2ds.$$

Set `tau=q/(2B)<=L/2`. The terminal interval of length tau has v-mass at most q/2, leaving at least q/2 in `[0,L-tau]`. Weighted Cauchy–Schwarz there gives

$$\operatorname{Tr}(C^2)\ge\tau\,{(q/2)^2\over L}
={q^3\over8BL}.                                             \tag{7.3}$$

For the unit reference input `phi=1/sqrt(L)`, the filter obeys

$$|f(t)|={|c|\over\sqrt L}(1-e^{-\kappa t})
\ge {|c|\kappa t\over2\sqrt L}.$$

Together with the OU exponential lower bound this gives

$$v(t)\ge{\sigma^2c^2\kappa^2 t^3\over24L},\qquad
q_{\rm ref}\ge{\sigma^2c^2\kappa^2L^3\over96}={BL\over96}.$$

Thus `m^2>=BL/96`. If a unit input has `q>=m^2/2`, (7.3) gives

$$s_2\ge q/(8BL)\ge1/1536.$$

By (7.1), its literal response is at most `m*(1-1/18432)`. If instead `q<m^2/2`, its literal response is below `m/sqrt(2)`, which is smaller than that same bound. Therefore the full adapted short-horizon literal gain satisfies the explicit uniform separation

$$\boxed{\ell\le(1-\delta)m,\qquad\delta=1/18432}            \tag{7.4}$$

whenever (7.2) holds. The small constant is a conservative written margin, not optimal. The near-maximal-q split is essential: no uniform effective covariance rank is asserted for arbitrarily tiny output responses.

## 8. ONE consolidated next attack: a deterministic eigenvalue enclosure

The new quantitative gap removes the need to evaluate ell in order to extract explicit rational coefficients. It is enough to obtain positive rational spectral bounds

$$m_-\le m\le m_+,\qquad(1-\delta)m_+<m_-.                  \tag{8.1}$$

Then choose the rational midpoint d of

$$\left(\gamma/m_-,\ \gamma/[(1-\delta)m_+]\right).$$

It guarantees `d*ell<gamma<d*m_-`. With rational Mbar, set

$$A=d^2m_-^2-\gamma^2>0,\qquad B_*=\gamma^2\overline M^2,
\qquad r=1+B_*/A.$$

All coefficients are rational, and the written identity

$$r^2A=A+2B_*+B_*^2/A>B_*$$

proves the all-controller mean-square exclusion. Thus (8.1) is a single concrete spectral obligation, not another full stochastic search.

There is an exact one-dimensional boundary-value representation for m. Put `W(t)=1-e^-2epsilon(L-t)` and substitute

$$F(t)=\int_0^t e^{-\kappa(t-s)}\phi(s)ds,
\qquad\phi=F'+\kappa F,\quad F(0)=0.$$

Then

$$m^2={\sigma^2\kappa^2c^2\over2\varepsilon}\,
\sup_{F\ne0,F(0)=0}{\int_0^L W F^2\over
\int_0^L(F'^2+\kappa^2F^2)+\kappa F(L)^2}.$$

Equivalently, if lambda1 is the smallest weighted Rayleigh eigenvalue,

$$-F''+\kappa^2F=\lambda W F,\quad F(0)=0,\quad
F'(L)+\kappa F(L)=0,$$

then

$$m^2={\sigma^2\kappa^2c^2\over2\varepsilon\lambda_1}.        \tag{8.2}$$

The terminal Robin term follows from the actual cross term in `integral(F'+kappa F)^2`; replacing it by a Dirichlet endpoint would change the problem. The weighted compact Rayleigh principle supplies attainment. This is a fixed-law mean-square spectral identity, not full literal synthesis.

For a universal rational dimensionless base choose `c=sigma=b=beta=1`, `kappa=1/(2L)`, `epsilon=1/(4L)`. With x=t/L the SINGLE remaining enclosure problem is the ground value Lambda1 of

$$-F_{xx}+\tfrac14F=\Lambda(1-e^{-(1-x)/2})F,
\quad F(0)=0,\quad F_x(1)+\tfrac12F(1)=0,$$

and `m^2=L/(2Lambda1)`. Rational upper/lower bounds tight enough to imply (8.1) would give explicit rational d,r through the formulas above. This is the **one next attack**; no additional branch or fourth incremental note is proposed before consolidation review.

**Not performed:** no Lambda enclosure, numerical eigensolve, interval interpreter, arithmetic replay or coefficient witness has been computed. Any future scientific execution needs a separate exact source/input-pinned named GO under HOLDv2. Written interval/comparison reasoning may continue without such execution. The exact unresolved spectral enclosure is not labelled completed.

## 9. Consolidated non-claims and review interfaces

Independent written reconstruction is needed for the long-family proof, the conditioning/compact Gaussian gap, and especially the NEW quantitative covariance inequalities (7.1)–(7.4) and the exact Robin spectral normalization. No author self-label supplies that gate.

The original broad target remains open: general prescribed-gamma N&S synthesis, arbitrary nonlinear/nonsmooth/nonstationary law structure, arbitrary preassigned horizons beyond the proven families, exact optimal gains, sharp constants and novelty. The old infinite stationary-linear reverse comparison and Fréchet tangent bridge keep their own restricted scopes; they do not provide same-level nonlinear synthesis or remove these gaps.

The only non-elementary probability transfer import is the explicitly named Geiss–Scheutzow theorem. Other imports are ordinary Brownian calculus/strong Markov/scaling, conditional expectation in separable L2, Hilbert compactness/spectral theory and Gaussian coordinates. No preview Riccati theorem is imported as if it solved the literal objective.

**Parkable state:** one manuscript now contains the two scoped feasibility directions, the horizon boundary, a quantitative coefficient-extraction bridge and exactly one remaining spectral attack. All old pins and mandatory permission qualifications are preserved. No formal, executable, cross-vendor/human, novelty or full-book solution is claimed; the deadline and global scientific-launch HOLD are unchanged.
