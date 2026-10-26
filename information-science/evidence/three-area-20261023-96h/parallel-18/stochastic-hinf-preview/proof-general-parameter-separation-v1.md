# A rational general-parameter separating family for the literal preview criterion

Owner: **InfoHinfPreview**, slot **info-3**. Actual clock observed before creation: **Sun Oct 25 03:56:18 PDT 2026** (`/bin/date`).

**Status: WRITTEN, with the specifically listed rational/polynomial identities WRITTEN-checked-in-kernel.** This is the assignment's **separating-family** acceptance route, not a general necessary-and-sufficient synthesis theorem. The stochastic argument is written mathematics, not proof-assistant/kernel certification. New independent reconstruction, parent disposition and novelty clearance have not been performed for this packet.

All older pinned packets and corrections remain unchanged. In particular, the old reverse-separation manuscript still requires its algebra addendum; this standalone successor does not silently repair or expand an old review verdict.

## 1. Consequential advance and exact target

The earlier reviewed packet supplies one rational cascade at gamma16386 and its particular finite horizon. Here there is instead:

1. A finite list of **rational algebraic inequalities in general cascade coefficients** that certifies mean-square feasibility together with **all-controller literal infeasibility**, including a strict quadratic storage matrix.
2. A constructive member for **every prescribed positive rational preview length h and attenuation gamma** on the infinite horizon, and on an explicitly supplied finite horizon with the correct input endpoint T-h.
3. A new exit-time moment representation, giving `E sqrt(tau) <= 103/108`, and a directly averaged OU endpoint anchor. These replace the old tiny Gaussian-event deficit and its rare-event anchor cutoff. This is not an additional enumeration of the old example.
4. Exact rational margins and general storage/exit-polynomial coefficient identities checked inside this agent's own eval kernel; no native scientific process, simulation, solver, external model or package installation.

The source is the actual printed criterion, not its square-energy replacement. The actual images at printed674–675, `information-science/stochastic-hinf-preview-control/sources/book/pdfpage-0695.png` and `pdfpage-0696.png`, were opened in this resumption. They define the pathwise L2 norm, place expectation **outside** that norm, print the state/window information, and request finite and infinite horizons.

Use, on the indicated interval I,

$$N_1(v;I)=E\left(\int_I |v_t|^2dt\right)^{1/2},\qquad
N_2(v;I)=\left(E\int_I |v_t|^2dt\right)^{1/2}.$$

The precise disturbance/admissibility interpretation is inherited openly from `selection-v1.md`: zero initial state and negative-time disturbance history; all progressively measurable disturbances with finite expected squared input energy; well-posed nonanticipative zero-preserving controllers. These are disclosed interpretations of omissions in the book, not verbatim book quantifiers. Finite output is counted on `[0,T]`, input exactly on `[0,T-h]`; infinite input/output are counted on `[0,infinity)`.

An impossibility result below allows **any realized progressively measurable control**, with locally pathwise square-integrable control and a strong nonexplosive closed-loop solution, even if the law is nonlinear, nonstationary, history-dependent or uses the whole Brownian past. This is an enlargement of the printed controller class and therefore a valid exclusion of it. The feasible mean-square controller `u=0` actually has the printed state/window form.

## 2. General-coefficient, rationally checkable theorem

Consider the two-state, one-control constant-matrix plant

$$
\begin{aligned}
 df_t&=\kappa[-f_t+c\,w(t-h)]dt,\\
 dy_t&=(-\varepsilon y_t+b u_t)dt+(\sigma f_t+\beta u_t)dW_t,\\
 z_t&=(d y_t,r u_t)^T,\qquad f_0=y_0=0.
\end{aligned}                                                    \tag{1}
$$

Here `epsilon,kappa,h,r>0`, `c*sigma*d != 0`; take `b*beta != 0` to retain effective drift AND diffusion actuation. Signs of the latter five nonzero coefficients are unrestricted. In book notation,

```
A  = diag(-kappa,-epsilon),       B  = (0,b)^T,
C  = (kappa*c,0)^T,              A0 = [[0,0],[sigma,0]],
B0 = (0,beta)^T,                 D0 = [[0,d],[0,0]],
D1 = (0,r)^T.
```

In particular `D1^T D1=r^2>0` and `D1^T D0=0`; the actuator is not an unused extra state.

Choose positive real certificate parameters `a,p,q,U,rho,eta,gamma`. All plant and certificate data MAY be rational. Define

$$
 q_0={103\over108},\qquad
 H^2={(c\sigma d)^2\over2\varepsilon},\qquad
 E_0={p+q\over a},\qquad
 \overline M=|d|\left({|b|\over\varepsilon}+|\beta|U\right).
                                                               \tag{2}
$$

Here H denotes the positive square root only in the proof; no square root need be evaluated to check the conditions. Require the **common conditions**

$$
\begin{gathered}
 \kappa p^2\ge1,\qquad q^2\ge2h,\qquad 2\varepsilon U^2\ge1,\\
 2\overline M^2<r^2\rho(2+\rho),\qquad
 H^2<\eta^2<\gamma^2. 
\end{gathered}                                                    \tag{C}
$$

For an infinite horizon put

$$Q_\infty=1-\varepsilon a^2-E_0.$$

Require

$$Q_\infty>0,\qquad
 H^2 Q_\infty^2>\gamma^2 q_0^2(1+\rho)^2.                    \tag{I}
$$

For a finite horizon choose `R>0` and an integer `m>=1`, and require

$$
 T-h\ge a^2R,\qquad 2\varepsilon(T-a^2R)\ge m.                \tag{F0}
$$

Put

$$Q_T=(1-2^{-m})\left(1-\varepsilon a^2-{5\over3R^2}\right)-E_0.$$

Require

$$Q_T>0,\qquad
 H^2 Q_T^2>\gamma^2 q_0^2(1+\rho)^2.                         \tag{F1}
$$

**Theorem SF.** Under (C), the zero controller is exponentially internally mean-square stable, has `G2 <= H < eta < gamma`, and has the strict mean-square quadratic certificate in section6. If also (I) holds, **every admissible controller has infinite-horizon literal gain greater than gamma**. If (F0)–(F1) hold, the same assertion holds on the stated finite horizon with input counted exactly on `[0,T-h]`.

More quantitatively, for the appropriate horizon and every such controller,

$$G_1(F)\ \ge\ {H Q\over q_0(1+\rho)}>\gamma,                \tag{3}$$

where `Q=Q_infinity` or `Q_T`. The supremum already has this lower bound from a **single controller-independent adapted disturbance** specified below.

For fixed integer m these are finite algebraic inequalities: absolute values can be replaced by fixed signs or sign cases, and all remaining denominators are positive. In particular rational inputs give exact rational admission tests, even for general rational epsilon: there is **no** requirement that `1/(2epsilon)` be a rational square. The conditions certify a counterexample property on this family; they are **not** advertised as necessary conditions for literal solvability of arbitrary plants.

## 3. A self-contained rational exit-time denominator certificate

Let B be standard Brownian motion started at x in `(-1,1)` and let tau be its first exit from that interval. Consider

$$
\begin{aligned}
 \mu_0(x)&=1,\\
 \mu_1(x)&=1-x^2,\\
 \mu_2(x)&=(5-6x^2+x^4)/3,\\
 \mu_3(x)&=(61-75x^2+15x^4-x^6)/15.
\end{aligned}                                                     \tag{4}
$$

For `j=1,2,3` they satisfy

$$\tfrac12\mu_j''=-j\mu_{j-1},\qquad \mu_j(-1)=\mu_j(1)=0.$$

They are nonnegative and bounded on `[-1,1]`. Explicitly,

$$\mu_2={(1-x^2)(5-x^2)\over3},\qquad
\mu_3={(1-x^2)(61-14x^2+x^4)\over15};$$

the second factor in the latter is positive there. Applying Itô/Dynkin first at `tau wedge t` for mu1 gives `E(tau wedge t)<=mu1(x)`, hence tau is finite a.s. Letting t increase, bounded convergence at the exit boundary gives `E_x tau=mu1(x)`.

For j2 and j3 the same stopped identities and bounded convergence give

$$\mu_j(x)=j E_x\int_0^\tau\mu_{j-1}(B_s)ds.$$

Inductively, the Brownian strong Markov property identifies the integrand with the conditional `(j-1)`st remaining-exit-time moment on `s<tau`. Tonelli and

$$\tau^j=j\int_0^\tau(\tau-s)^{j-1}ds$$

give `E_x tau^j=mu_j(x)`, including finiteness. Thus, at x0,

$$E\tau=1,\qquad E\tau^2=5/3,\qquad E\tau^3=61/15.             \tag{5}$$

No unjustified unbounded optional-stopping or prior moment-finiteness assumption is needed.

Set `A=tau-1`. Then

$$E A^2=2/3,\qquad E[A^2(\tau+1)]=12/5.$$

Cauchy–Schwarz therefore yields

$$E{A^2\over\tau+1}\ \ge\ {(E A^2)^2\over E[A^2(\tau+1)]}={5\over27}.$$

Since `(sqrt(t)+1)^2 <= 2(t+1)`,

$$E(\sqrt\tau-1)^2
 =E{A^2\over(\sqrt\tau+1)^2}\ge {5\over54}.$$

Finally `E tau=1` gives the exact identity

$$E\sqrt\tau=1-\tfrac12 E(\sqrt\tau-1)^2\le {103\over108}=q_0. \tag{6}$$

This is a useful rational bound, not an assertion of the exact value of `E sqrt(tau)` or an optimal moment certificate.

For the actual driving Brownian motion W, let

$$\tau_a=\inf\{t\ge0:|W_t|=a\}.$$

Brownian scaling gives

$$E\tau_a=a^2,\quad E\tau_a^2=5a^4/3,\quad
E\sqrt{\tau_a}\le a q_0.                                     \tag{7}$$

Use `w_t=1_(t<tau_a)` in infinite time, and `w_t=1_(t<tau_a wedge L)` in finite time, where **L=T-h**. Both are progressive and have finite mean-square input energy. The finite denominator only decreases on truncation. In either case

$$0<N_1(w)\le a q_0.$$

These are adapted, not deterministic, test disturbances. The distinction is indispensable.

## 4. Directly averaged OU anchor and the actual delay/filter error

### 4.1 Infinite-time lower anchor without a cutoff event

For the untruncated test disturbance define the comparison process

$$Z_t=\int_0^t e^{-\varepsilon(t-s)}w_s\,dW_s,\qquad
M_t=W_{t\wedge\tau_a}.$$

This is only a comparison process, **not the plant**. Integration by parts gives

$$Z_t=M_t-\varepsilon\int_0^t e^{-\varepsilon(t-s)}M_sds.$$

At tau_a, `|M_tau_a|=a` and `|M_s|<=a`. In fact

$$|Z_{\tau_a}|\ge a e^{-\varepsilon\tau_a}
                  \ge a(1-\varepsilon\tau_a).$$

After tau_a there is no diffusion forcing, so the exact tail norm is `|Z_tau_a|/sqrt(2epsilon)`. Consequently

$$N_1(Z)\ge {a\over\sqrt{2\varepsilon}}(1-\varepsilon a^2).    \tag{8}$$

The decisive change from the old packet is to **average the stopped endpoint directly** using `E tau_a=a^2`. There is no Markov cutoff R or `epsilon*R` loss in (8).

### 4.2 Counted finite-time lower anchor

For the finite truncated input use the corresponding Z. On the event `tau_a<=a^2 R`, condition (F0) puts the genuine exit inside the counted input interval. The counted tail from tau_a to T has norm

$$ {|Z_{\tau_a}|\over\sqrt{2\varepsilon}}
       \sqrt{1-e^{-2\varepsilon(T-\tau_a)}}.$$

Because `2epsilon(T-a^2 R)>=m`, `e>2`, and `sqrt(1-t)>=1-t` on `[0,1]`, its square-root factor is at least `1-2^-m`. Also (7) and Markov's inequality at the **second** moment give

$$P(\tau_a>a^2R)\le {5\over3R^2}.$$

The endpoint estimate and `E tau_a=a^2` therefore imply

$$
\begin{aligned}
 E[|Z_{\tau_a}|1_{\{\tau_a\le a^2R\}}]
 &\ge a P(\tau_a\le a^2R)
       -a\varepsilon E[\tau_a1_{\{\tau_a\le a^2R\}}]\\
 &\ge a\left(1-{5\over3R^2}-\varepsilon a^2\right).
\end{aligned}
$$

Thus, entirely inside the **counted finite output interval**,

$$N_1(Z;[0,T])\ge {a\over\sqrt{2\varepsilon}}(1-2^{-m})
       \left(1-\varepsilon a^2-{5\over3R^2}\right).            \tag{9}$$

There is no hidden infinite output tail in (9), and no input on the uncounted interval `(T-h,T]`.

### 4.3 Returning to the actual plant

Write `F=f/c` and `v=w(.-h)`. For either test signal its duration theta is tau_a or `tau_a wedge L`. The shifted and unshifted unit steps have symmetric difference of length at most2h, pathwise. The actual first-order filter has the exact rise/tail identity

$$\int_0^\infty |F_t-v_t|^2dt={1-e^{-\kappa\theta}\over\kappa}
                                                    \le1/\kappa.$$

Indeed the rise and tail terms are `(1-e^-2kappa*theta)/(2kappa)` and `(1-e^-kappa*theta)^2/(2kappa)`. Their sum is the displayed expression. Minkowski in the product L2 space and (C) give

$$N_2(F-w)\le\kappa^{-1/2}+\sqrt{2h}\le p+q.                 \tag{10}$$

For `u=0`, the actual performance state is the OU convolution driven in diffusion by `sigma*c*F`. Itô isometry/Tonelli show that the performance-output difference from `d*sigma*c*Z` has

$$N_1(d y^0-d\sigma c Z)\le N_2(d y^0-d\sigma c Z)
                                \le H(p+q).                  \tag{11}$$

For finite time the full extended error is used only for an **upper** estimate and then restricted to `[0,T]`. Combining (8) or (9) with (11) gives the actual uncontrolled-output bound

$$N_1(d y^0)\ge H a Q.                                       \tag{12}$$

Thus strictly positive preview and finite-rate filtering are explicitly paid for; neither was silently set to zero or infinity.

## 5. Why every admissible controller is excluded

Treat the **realized** adapted control as an input to a linear equation. Irrespective of how it was chosen,

$$d y=d y^0+\mathcal S u,$$

where

$$\mathcal S u(t)=d b\int_0^t e^{-\varepsilon(t-s)}u_sds
              +d\beta\int_0^t e^{-\varepsilon(t-s)}u_s dW_s.$$

Deterministic convolution and Itô isometry give, for every adapted square-energy input,

$$N_2(\mathcal S u)\le |d|\left({|b|\over\varepsilon}
                 +{|\beta|\over\sqrt{2\varepsilon}}\right)N_2(u)
                   \le\overline M N_2(u).                    \tag{13}$$

The only non-elementary norm import is Geiss–Scheutzow, *Sharpness of Lenglart's domination inequality and a sharp monotone version*, [arXiv:2101.10884v2, Theorem2.2](https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2). Its actual statement was re-read in the saved primary PDF this resumption. For nonnegative nondecreasing adapted right-continuous X,G, predictable G, and conditional domination at **every bounded stopping time**, it gives `E X_infinity^(1/2) <= sqrt(2) E G_infinity^(1/2)`.

Here apply it to accumulated output energy of S and `G_t=overlineM^2 integral_0^t u^2`. For each bounded stopping time, stopping the **input** preserves the earlier output; discarding its later nonnegative output and using (13) supplies the required domination. Multiplication by an initial event gives its conditional form because S is linear, causal, event-local and zero-preserving. Therefore

$$N_1(\mathcal S u)\le\sqrt2\,\overline M N_1(u).             \tag{14}$$

No sharp BDG constant or Riccati theorem is imported. The older `proof-v1.md` TheoremA is the same classical transfer interface; (13)–(14) spell out its application here rather than inheriting a review verdict.

Crucially (14) also holds when `N1(u)<infinity` but `N2(u)=infinity`: stop u when its accumulated squared energy reaches n, apply (14) to that square-energy input, and use local uniqueness/causality and Fatou as n increases. On every path of finite total control energy, sufficiently large stops do not alter the entire path. For finite time, extend the realized u by zero after T only as an input to S; causality preserves S through T. This neither extends nor resets the feedback law and supplies no energy-history information to it.

If `N1(z)=infinity` the controller already fails. Otherwise the separate `r*u` channel forces finite `N1(u)`, so (14) is available for **all** controls under consideration. For pathwise time norms X and U, triangle and two-dimensional Cauchy–Schwarz give

$$
\begin{aligned}
 N_1(d y^0)&\le N_1(d y)+\sqrt2\,\overline M N_1(u)\\
 &\le \sqrt{1+2\overline M^2/r^2}\,
          E\sqrt{\|d y\|_2^2+r^2\|u\|_2^2}\\
 &\le (1+\rho)N_1(z).
\end{aligned}                                                    \tag{15}
$$

The last step is exactly the control inequality in (C). Combining (12), (15), and the actual **random-denominator** bound `N1(w)<=a q0` proves (3). Positivity of Q makes the squared rational separation inequality equivalent to the needed strict level comparison. The test disturbance is the same for every controller. This proves TheoremSF's literal exclusions, without stationarity, differentiability, linear-feedback optimality or a physical reset.

## 6. Mean-square feasibility, internal stability, and a strict matrix certificate

For `u=0`, the deterministic low-pass kernel has L1 mass1, so Jensen/Tonelli gives the pathwise contraction `integral F^2 <= integral w^2`, including the actual delay. Itô isometry then gives

$$N_2(d y^0)^2=H^2 E\int_0^\infty F_t^2dt\le H^2 N_2(w)^2.$$

This holds for **all** adapted square-energy disturbances, not just the exit-time test. For finite time use zero extension of w and discard later nonnegative output. Hence `G2(u=0)<=H<eta<gamma` on both specified regimes.

For arbitrary homogeneous initial states choose

$$V_0={\sigma^2+1\over2\kappa}f^2+y^2.$$

Its expectation satisfies

$$ {d\over dt}E V_0=-E f^2-2\varepsilon E y^2
 \le-\min\left\{{2\kappa\over\sigma^2+1},2\varepsilon\right\}E V_0.$$

Thus the exhibited controller is exponentially internally mean-square stable. No unobservable unstable mode is being excused by zero-state gain.

There is also a direct **strict bounded-real storage matrix** at eta, for every general coefficient set satisfying (C). Put

$$\alpha=\eta^2-H^2>0,\qquad
 P=\operatorname{diag}\left({\eta^2\over\kappa c^2},
                     {\eta^2+H^2\over2c^2\sigma^2}\right)>0.$$

For `Cv=(kappa*c,0)^T`, `N=[[0,0],[sigma,0]]`, `Z=(0,d)`, the complete matrix is

$$\mathcal B=\begin{pmatrix}
 A^TP+PA+N^TPN+Z^TZ&PC_v\\ C_v^TP&-\eta^2
 \end{pmatrix}.$$

Its exact quadratic form is

$$
 (f,y,v)\mathcal B(f,y,v)^T
 =-{\alpha\over2c^2}f^2
  -{\varepsilon\alpha\over c^2\sigma^2}y^2
  -\eta^2(v-f/c)^2.                                         \tag{16}
$$

Every displayed weight is strictly positive and the joint zero set is only the origin, so `Bcal<0` on the full state/input space. This identity was checked as a general rational-function coefficient identity in-kernel, not merely at a sample matrix.

Itô for `V=x^T P x` retains the correction `py*sigma^2*f^2` and the martingale `2*py*sigma*f*y dW`. Its drift plus `d^2*y^2-eta^2*v^2` is exactly (16). Bounded state/input-energy stopping, taking expectation, discarding nonnegative storage, Fatou and monotone convergence give the genuine mean-square energy inequality at eta. The finite delayed input identity is **exactly** `integral_0^T v^2=integral_0^(T-h) w^2`. No old preview Riccati theorem is consumed.

Thus these are instances where an explicit **strict quadratic mean-square certificate at eta<gamma exists**, yet no admissible controller attains the printed criterion at gamma. The usual mean-square bounded-real theory is not refuted; the same-level substitution of objectives is.

## 7. An explicit family for arbitrary prescribed positive h and gamma

Fix any `h>0`, `gamma>0`. Choose any `a>0` with

$$a^2\ge2^{17}h.$$ 

For positive rational h,gamma, all data below can be rational: for example `a=512*(1+h)` always satisfies that inequality. Set

$$
\begin{gathered}
 c=\sigma=b=\beta=1,\qquad
 \varepsilon={1\over512a^2},\qquad \kappa=(512/a)^2,\\
 d={4\gamma\over65a},\quad p=q=a/256,\quad U=17a,\quad
 \rho=1/128,\quad \eta=129\gamma/130,\\
 \overline M=d(512a^2+17a),\qquad r=16\overline M,\\
 R=32,\qquad m=8,\qquad T=2080a^2.
\end{gathered}                                                     \tag{17}
$$

Then

$$H=64\gamma/65,\quad
 \kappa p^2=4,\quad 2\varepsilon U^2=289/256,\quad E_0=1/128.$$

The control slack, after division by `r^2`, is exactly

$$\rho(2+\rho)-{2\over16^2}={129\over16384}>0.$$

Also

$$\eta^2-H^2={257\over16900}\gamma^2>0,\qquad
\gamma^2-\eta^2={259\over16900}\gamma^2>0.$$

The finite tail exponent is exactly8. The counted input endpoint is beyond `32a^2` because `h<=2^-17*a^2`. The two lower-anchor quantities and the common level threshold are

$$Q_\infty={507\over512},\qquad
Q_T={258137\over262144},\qquad
{\gamma\over H}q_0(1+\rho)={287885\over294912}.$$

Their exact positive margins are

$$Q_\infty-{\gamma\over H}q_0(1+\rho)={4147\over294912}>0,$$

$$Q_T-{\gamma\over H}q_0(1+\rho)={20153\over2359296}>0.$$

Consequently this single constructive family satisfies

$$\inf_F G_2(F)\le {64\over65}\gamma<\gamma,$$

whereas, allowing even the enlarged all-adapted controller class,

$$\inf_F G_1(F)\ge {22464\over22145}\gamma>\gamma
\quad\hbox{on the infinite horizon},$$

$$\inf_F G_1(F)\ge {2323233\over2303080}\gamma>\gamma
\quad\hbox{on the finite horizon }T=2080a^2.                   \tag{18}$$

These are bounds, not exact optimal gains. The finite claim supplies a horizon; it does **not** assert separation on every preassigned short T>h. Positive h, both effective actuation channels, adapted disturbances, full control penalty, and internal stability are present throughout.

A small exact canonical member is

```
a=1, h=1/262144, gamma=1,
epsilon=1/512, kappa=262144,
c=sigma=b=beta=1, d=4/65, r=33856/65,
eta=129/130, T=2080.
```

This is not merely the old plant's output normalization: the denominator certificate, endpoint averaging, general free-coefficient rational screen, coefficient-dependent strict storage, and explicit h/gamma construction have all been proved above. Moreover the general screen in section2 allows nonzero b,beta,c,sigma,d and epsilon,kappa to vary independently while preserving its strict margins. With slack in the auxiliary bounds and finite endpoint/tail inequalities it describes open parameter neighborhoods, not a single exceptional equality point.

## 8. Verification boundary, provenance, and exact remaining gap

The companion `family-rational-verification-v1.json` records the actual in-kernel arithmetic. Specifically checked:

- The three Brownian generator polynomial identities and all six boundary values, plus their displayed nonnegativity factorizations.
- The exact Fraction arithmetic yielding `5/108`, `103/108`, the two Q values, all level/control margins, and the two fractions in (18).
- The four coefficients `f^2,y^2,f*v,v^2` in the **general** identity (16), by sparse multivariate polynomial numerator/denominator arithmetic over `fractions.Fraction`.
- The elementary low-pass integration cancellation as a formal polynomial identity.
- Every rational hypothesis for the canonical member, and three nontrivial prescribed h/gamma pairs using `a=512*(1+h)`.

A first attempt to import sympy returned `ModuleNotFoundError`. Nothing after that first import ran in that cell; no package was installed. The successful checks used Fraction-based exact sparse algebra, with known-true square/product controls. No float, numerical solver, Brownian sample, launched native scientific program, background job, external-model CLI, nested agent, git operation, deletion or publication was used.

These checks certify **only the named algebra and finite rational inequalities**. They do not machine-check Itô/Dynkin, Brownian strong Markov/scaling, conditional stopping-time domination, stochastic well-posedness, Fatou/localization, controller quantifiers or the written theorem as a whole. The classical imports are ordinary Brownian stochastic calculus/strong Markov/scaling and integration, plus the explicitly source-read Geiss–Scheutzow Theorem2.2. No Riccati characterization, sharp probability constant, prior novelty claim or formal proof is smuggled in.

Prior scope remains in the immutable `proof-v1.md`, reverse-separation packet with its three addenda, and nonlinear tangent packet. Their actual review history is recorded in `institute/runs/three-area-2026-10-23-96h/preview-full-packet-parent-v1.md` and the PhysicsResearch96h cross-domain return. That scoped mean-square substitute and those written checks remain scoped; the present successor has not inherited their independent-review or parent-acceptance labels.

**Assignment deliverable:** an exact general-parameter separating family with rational in-kernel verification, including arbitrary positive prescribed h and gamma and both stated horizon regimes. **Not delivered/remaining scientific gap:** a necessary-and-sufficient literal synthesis criterion for an arbitrary constant-matrix plant and prescribed horizon/level, exact optimal gain even for this cascade, every preassigned finite horizon, nonsmooth/nonstationary optimal-law structure, sharp norm constants, novelty or publication acceptance. No full-book solution is claimed. The packet is parkable without any scientific launch, and the global HOLD remains binding.
