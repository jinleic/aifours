# Written-only horizon boundary: conditioning removes the adapted norm gap for the zero controller

Owner: **InfoHinfPreview**, info-3. Prior actual returned clock: **Sun Oct 25 04:09:59 PDT 2026** (`/bin/date`). This is a new **WRITTEN** proposition following the parent's withdrawal of the blanket eval-kernel exception. **No scientific arithmetic interpreter, symbolic computation, enumeration, certificate replay, solver or simulation was used for this note.** Ordinary written algebra is not a machine check.

Read together with `permission-withdrawal-addendum-v1.json`. The earlier general-parameter packet and arithmetic receipt remain immutable observations; their permission/verification-credit wording is qualified by that addendum. No new independent reconstruction, parent acceptance, formal verification or novelty clearance is claimed here.

## 1. Question addressed

The delivered separating family supplies its own sufficiently long finite horizon; it does not separate the two problems for every preassigned T>h. The following exact representation explains a genuine boundary, rather than merely restating that restriction:

> For the cascade's **zero controller**, if the entire counted input interval ends before delayed forcing starts, the literal gain cannot exceed that controller's mean-square gain. Random adapted disturbances do not improve its literal norm beyond deterministic disturbances in this regime.

This does not settle synthesis over other controllers. It identifies why the Brownian stopping-time mechanism used in the long-horizon family cannot be transplanted unchanged to every short horizon.

## 2. Plant and statement

Use the same constant-matrix plant, with zero data, `epsilon,kappa,h,r>0` and `c*sigma*d != 0`:

$$
 df_t=\kappa[-f_t+c w(t-h)]dt,\qquad
 dy_t=(-\varepsilon y_t+b u_t)dt+(\sigma f_t+\beta u_t)dW_t,
 \qquad z_t=(d y_t,r u_t)^T.
$$

Fix finite `T>h`, put **L=T-h**, and count input exactly on `[0,L]`. Disturbances are progressive and have finite expected squared input energy. Set `u=0`; no optimization over controllers is being inferred.

For deterministic `phi in L2(0,L)` define the bounded Volterra operator

$$
 (A_L\phi)(t)={d\sigma\kappa c\over\sqrt{2\varepsilon}}
       \sqrt{1-e^{-2\varepsilon(L-t)}}
       \int_0^t e^{-\kappa(t-s)}\phi(s)ds,
 \qquad 0\le t\le L.                                      \tag{1}
$$

Let `Y_phi` denote the zero-control performance-output process for deterministic phi on the counted output interval, and define

$$J_L(\phi)=E\|Y_\phi\|_{L^2(0,T)}.$$

Its law depends on L and phi, not on the absolute delay h: the output before h is zero and Brownian increments after h have their usual law.

**Proposition SH.**

1. For **every** h>0 and T>h, the zero controller's mean-square induced gain is exactly

   $$G_2(0)=\|A_L\|.$$

   In particular its finite-horizon mean-square gain depends on L, not separately on h.

2. If `L<=h`, equivalently `h<T<=2h`, the zero controller's literal gain is exactly

   $$G_1(0)=\sup_{\phi\ne0\text{ deterministic}}
                         {J_L(\phi)\over\|\phi\|_{L^2(0,L)}}
            \le\|A_L\|=G_2(0).                            \tag{2}$$

3. Hence, in this short-horizon regime, `G2(0)<gamma` implies `G1(0)<gamma`. A reverse separation whose exhibited mean-square feasible law is `u=0`, such as the delivered cascade family, **cannot occur there**. This does not claim a same-level implication for arbitrary nonlinear controllers or arbitrary plants.

## 3. Exact mean-square operator, without a deterministic-input substitution

For u0, the actual filtered input is

$$f_s=\kappa c\int_0^{s-h}e^{-\kappa(s-h-v)}w_vdv,
       \qquad h\le s\le T,$$

and f,y are zero before h. The state after h is

$$y_t=\sigma\int_h^t e^{-\varepsilon(t-s)}f_s\,dW_s.$$

The integrand is adapted even for random progressive w. Itô isometry and Tonelli therefore give, with no conditioning and no independence assumption on w,

$$
\begin{aligned}
 E\int_0^T d^2 y_t^2dt
 &= {d^2\sigma^2\over2\varepsilon}
       E\int_h^T(1-e^{-2\varepsilon(T-s)})f_s^2ds\\
 &=E\|A_L w\|_{L^2(0,L)}^2.                              \tag{3}
\end{aligned}
$$

Here A_L is applied pathwise to the random input equivalence class. Its kernel is bounded on a finite triangle, so it is Hilbert–Schmidt and in particular bounded. Equation (3) gives `G2(0)<=||A_L||`. Deterministic input functions are admissible, and a sequence approaching the deterministic operator norm gives the opposite inequality. No norm-attaining function needs to be assumed. This proves claim1 for the **full adapted class**.

For an alternative exact spectral representation, `A_L^* A_L` is the compact positive integral operator with kernel

$$
 K_L(s,t)={(d\sigma\kappa c)^2\over2\varepsilon}
       \int_{\max(s,t)}^L
       (1-e^{-2\varepsilon(L-v)})e^{-\kappa(2v-s-t)}dv.       \tag{4}
$$

Its largest eigenvalue is `G2(0)^2`. The integral expression deliberately avoids introducing a spurious exceptional case when epsilon equals kappa. This is an infinite-dimensional compact-operator representation for a **fixed law**, not the requested finite-dimensional general synthesis criterion.

## 4. Short-horizon conditioning is legitimate precisely because the input is already known

Now suppose L<=h. The whole random input, as an `L2(0,L)`-valued variable, is measurable with respect to `F_L`. All output noise occurs after h. Brownian increments after h are independent of `F_L`; f after h is a deterministic functional of that already known random input.

It follows that, conditionally on `F_L`, the output has exactly the law of the deterministic-input Gaussian response with input equal to the realized w path. Thus

$$E[\|d y\|_{L^2(0,T)}\mid F_L]=J_L(w),\qquad
 E[\|d y\|_{L^2(0,T)}^2\mid F_L]=\|A_L w\|^2.             \tag{5}$$

For precision, J_L is measurable: linearity, Cauchy–Schwarz and the deterministic version of (3) give

$$|J_L(\phi)-J_L(\psi)|\le\|A_L\|\,\|\phi-\psi\|.$$

The conditional identities can first be established for simple `F_L`-measurable L2-valued variables, using independent future Brownian increments, and extended by this continuity and the corresponding square-mean continuity. These approximants are used only to establish the conditional stochastic-integral law after h; no anticipative approximation is being asserted as an admissible disturbance before L.

Let

$$g_J=\sup_{\phi\ne0}{J_L(\phi)\over\|\phi\|}.$$

Taking expectation in (5) gives the literal, random-denominator bound

$$N_1(d y)=E J_L(w)\le g_J E\|w\|=g_J N_1(w).$$

Conversely deterministic inputs give `G1(0)>=g_J`. Hence equality holds. For each deterministic phi, Jensen and (3) give `J_L(phi)<=||A_L phi||`, proving (2).

This is **not** the invalid blanket Jensen comparison from the original problem. The random denominator is preserved through conditioning on the **entire input before any output noise occurs**. If L>h, that entire input contains future information relative to some output increments; (5) is no longer justified by Brownian independence. That is exactly the correlation opportunity exploited by the long-horizon adapted stopping-time construction.

## 5. Consequence for the earlier rational screen

The finite separating screen itself is consistent with this structural boundary. Its conditions include

$$a^2R\le T-h,\qquad q^2\ge2h,\qquad E_0=(p+q)/a.$$

If T<=2h, these imply

$$E_0\ge q/a\ge\sqrt{2h}/a\ge\sqrt{2R}.$$

For R>=1/2 this is at least1, so

$$Q_T=(1-2^{-m})(1-\varepsilon a^2-5/(3R^2))-E_0<0.$$

For R<1/2 the middle parenthesis is negative already, so again Q_T<0. Thus the required Q_T>0 cannot hold on this short-horizon range. This is a written inequality argument only; no parameter enumeration or interpreter check was performed.

## 6. Exact boundary of this progress

This note supplies a fixed-controller norm representation and an exact conditional-independence obstruction to extending the delivered reverse separation to every short finite horizon. It neither assumes nor proves that u0 is optimal among controllers. Effective controls may pre-act and generate output noise before h; for them the same conditioning argument need not apply. No arbitrary-controller same-gamma transfer, exact nonlinear optimum or general N&S synthesis theorem follows.

Imports are ordinary Itô isometry, Brownian independent increments, Tonelli, conditional expectation in separable L2 spaces, and elementary bounded/compact Hilbert-space operator theory. They are named mathematical imports, not formal certification or newly machine-checked results. The global scientific-launch HOLD remains binding; no new scientific computation is authorized by this written proposition.
