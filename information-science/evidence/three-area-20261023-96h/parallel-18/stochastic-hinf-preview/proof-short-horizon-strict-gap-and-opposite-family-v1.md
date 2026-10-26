# Written-only strict Gaussian gap and an opposite all-controller family on every short horizon

Owner **InfoHinfPreview**, info-3. Actual returned clock before creation: **Sun Oct 25 04:39:51 PDT 2026** (`/bin/date`). **WRITTEN CANDIDATE**, following completion of the v31-A written algebra review. No scientific interpreter, arithmetic/symbolic program, enumeration, replay, solver or simulation was used for this note. The mandatory `permission-withdrawal-addendum-v1.json` and parent erratumv7 remain binding. Independent reconstruction and parent disposition of this new claim are **not performed**.

## 1. Progress beyond the previous conditioning boundary

`proof-short-horizon-conditioning-v1.md` established, for the fixed zero controller, that when `h<T<=2h` the literal norm is no greater than the mean-square norm. Here the inequality is proved **strict**, not just weak. Compactness prevents deterministic input sequences from making the Gaussian Jensen gap disappear at the maximizing literal input.

The strict gap then gives an **all-controller feasibility separation in the opposite direction** to the long-horizon family:

> For every prescribed positive rational h, T, gamma with h<T<=2h, there is a rational constant-matrix plant of the same two-state cascade form, with effective drift and diffusion actuation, positive preview, full control penalty and an internally mean-square-stable zero law, for which the printed literal criterion is feasible at gamma while the mean-square criterion is infeasible at gamma for every admissible controller.

This is an exact **nonconstructive written existence family**, not a new rational numeric witness or executable certificate. Its coefficient choices use a rigorously proved compact-operator norm gap and rational density; this note does not claim to evaluate the endpoint norms, to supply a finite LMI for them, or to authorize arithmetic to locate a numerical member.

## 2. Fixed-law strict gap

Fix arbitrary real constants

$$\varepsilon,\kappa,h>0,\qquad h<T\le2h,\qquad
c\sigma\ne0.$$

For the moment take base state-output coefficient `d=1` and ignore the unused control input by setting `u=0`:

$$df_t=\kappa[-f_t+c w(t-h)]dt,\qquad
dy_t=-\varepsilon y_tdt+\sigma f_t dW_t.$$

Both states start at0; negative-time disturbance history is zero. Put `L=T-h`. Inputs are all progressive w with finite expected squared energy on `[0,L]`; output is counted on `[0,T]`.

For deterministic `phi in H0=L2(0,L)` define `R phi` to be the random state-output path y in `H1=L2(0,T)`. Thus

$$R:H_0\longrightarrow L^2(\Omega;H_1)$$

is a bounded linear map. The previous note's exact Itô/Tonelli identity gives

$$\|R\phi\|_{L^2(\Omega;H_1)}=\|A\phi\|_{H_0},              \tag{1}$$

where

$$
 (A\phi)(t)={\sigma\kappa c\over\sqrt{2\varepsilon}}
      \sqrt{1-e^{-2\varepsilon(L-t)}}
      \int_0^t e^{-\kappa(t-s)}\phi(s)ds.
                                                               \tag{2}
$$

The kernel in (2) is bounded on a finite triangle, so A is compact (indeed Hilbert–Schmidt). It is nonzero, since `c*sigma != 0`, L>0, and a nonnegative nonzero input supported strictly before L gives a nonzero filtered path on a set of positive measure.

Write

$$m=\|A\|>0,\qquad
J(\phi)=E\|R\phi\|_{H_1},\qquad
\ell=\sup_{\|\phi\|\le1}J(\phi).$$

The earlier conditioning proposition, applicable because L<=h, says exactly

$$G_2(0)=m,\qquad G_1(0)=\ell.$$ 

This equality for G1 is for the **full progressive random-input class**, not a replacement of that class by deterministic inputs: the complete random input is `F_L`-measurable before any output noise starts, so conditional output norm is J evaluated at the realized input, and the random input denominator remains `E||w||`.

**Proposition SG.**

$$0<\ell<m.                                                  \tag{3}$$

### 2.1 Why the literal maximizing input exists

Take a maximizing sequence phi_n in the closed unit ball of H0. Hilbert-space weak compactness gives a subsequence weakly converging to phi_* in that ball. Compactness of A implies

$$\|A(\phi_n-\phi_*)\|\longrightarrow0.$$

By linearity and (1), this is also convergence of `R phi_n` to `R phi_*` in `L2(Omega;H1)`. Hence

$$|J(\phi_n)-J(\phi_*)|
 \le E\|R(\phi_n-\phi_*)\|
 \le\|A(\phi_n-\phi_*)\|\longrightarrow0.$$

Therefore `J(phi_*)=ell`. Nontriviality of A gives some positive J, so ell>0 and `R phi_*` is nonzero. Homogeneity then forces `||phi_*||=1`, since a smaller nonzero norm could be scaled up to increase J.

This compactness argument is essential. Pointwise strict Jensen alone would not prove a strict gap between two suprema.

### 2.2 Why every nonzero deterministic response has a strict Gaussian Jensen gap

For deterministic phi the process R phi is a centered Gaussian random variable in the separable real Hilbert space H1. This follows directly from its stochastic-convolution formula with deterministic integrand: finite linear combinations of time-integrated output coordinates are centered Gaussian, and L2 approximation gives all continuous Hilbert functionals.

A nonzero centered Gaussian H1-valued variable Y cannot have almost surely constant norm. Otherwise its constant norm would be finite, so every scalar projection would be bounded. But nonzero second moment gives at least one continuous scalar projection with positive variance; that projection is a nondegenerate real Gaussian and is not bounded. This contradiction uses only the ordinary Gaussian marginal property, not a numerical tail estimate.

Consequently, for nonzero Y, strict Cauchy–Schwarz applied to `||Y||` and1 gives

$$E\|Y\|<\big(E\|Y\|^2\big)^{1/2}.$$

Apply this to `Y=R phi_*`, which is nonzero by ell>0. Then

$$\ell=J(\phi_*)<\|A\phi_*\|\le\|A\|=m.$$

This proves (3) without computing either norm.

## 3. A general all-controller mean-square lower bound retaining pre-action

Reintroduce arbitrary nonzero drift/diffusion control coefficients b,beta, a positive state-output scale d and a positive control penalty r:

$$
\begin{aligned}
 df_t&=\kappa[-f_t+c w(t-h)]dt,\\
 dy_t&=(-\varepsilon y_t+b u_t)dt+(\sigma f_t+\beta u_t)dW_t,\\
 z_t&=(d y_t,r u_t)^T.
\end{aligned}                                                    \tag{4}
$$

Permit any progressive realized control with locally pathwise square-integrable input and a strong nonexplosive solution, including nonlinear/nonstationary arbitrary-history laws and preview pre-action. Impossibility for this enlargement implies impossibility for the printed state/window controller class.

For any fixed disturbance and the same Brownian path,

$$d y=d y^0+S_d u,$$

where y0 is the zero-control state and

$$S_d u(t)=d b\int_0^t e^{-\varepsilon(t-s)}u_sds
          +d\beta\int_0^t e^{-\varepsilon(t-s)}u_s dW_s.$$

Extend the realized u by zero after T solely as input to this linear map. Causality preserves its response through T. Deterministic convolution and Itô isometry give

$$N_2(S_d u;[0,T])\le M_d N_2(u;[0,T]),$$

$$M_d=d\left({|b|\over\varepsilon}
                       +{|\beta|\over\sqrt{2\varepsilon}}\right).$$

For a rationally describable upper bound one can choose any positive U with `2epsilon*U^2>=1` and use

$$\overline M_d=d\left({|b|\over\varepsilon}+|\beta|U\right)\ge M_d.$$

If `N2(z)=infinity`, the attempted controller already fails mean-square attenuation. Otherwise `r*u` in the actual output forces `N2(u)<infinity`, so this square-mean bound applies with no extra controller regularity. Triangle followed by scalar Cauchy–Schwarz gives

$$
\begin{aligned}
 N_2(d y^0)&\le N_2(d y)+\overline M_d N_2(u)\\
 &\le\sqrt{1+(\overline M_d/r)^2}\,
             \sqrt{N_2(d y)^2+r^2N_2(u)^2}\\
 &=\sqrt{1+(\overline M_d/r)^2}\,N_2(z).
\end{aligned}                                                    \tag{5}
$$

The actual control can act before delayed forcing arrives; all such actuation remains present in S_d and is charged in r*u. It has not been removed or reset.

The zero controller has mean-square gain d*m. Taking the supremum over disturbances in (5) therefore proves, for every actual controller F,

$$G_2(F)\ge {d m\over\sqrt{1+(\overline M_d/r)^2}}.           \tag{6}$$

In fact a single deterministic maximizing input for the compact operator A realizes the zero-law norm m and supplies this same universal lower bound against every controller. Using a sequence approaching m would also suffice; no search or explicit eigenfunction was computed.

## 4. Rational existence on any prescribed short horizon and attenuation

Now fix **any positive rational h,T,gamma with h<T<=2h**. Choose arbitrary positive rational epsilon,kappa and arbitrary nonzero rational c,sigma,b,beta. These are genuinely free base coefficients; no special relation between epsilon and kappa is required. The preceding theorem fixes exact positive real numbers ell,m satisfying ell<m.

The open interval

$$\left({\gamma\over m},{\gamma\over\ell}\right)$$

is nonempty. By density of the rationals choose a **positive rational d** in it. Thus

$$d\ell<\gamma<d m.                                        \tag{7}$$

Choose positive rational U sufficiently large that `2epsilon*U^2>=1`. Then `Mbar_d` is rational. Since `(d*m)^2-gamma^2>0`, choose a **positive rational r** sufficiently large that

$$r^2\big((d m)^2-\gamma^2\big)>\gamma^2\overline M_d^2.      \tag{8}$$

This is an ordinary Archimedean existence choice, not a performed coefficient search. It is equivalent to making the right side of (6) strictly greater than gamma.

For these rational plant matrices:

- The zero controller is of the printed state/window form and satisfies the literal criterion uniformly over all progressive square-energy disturbances, because its literal gain is `d*ell<gamma`.
- Every admissible controller has mean-square gain strictly greater than gamma by (6)–(8), so mean-square feasibility is impossible at that same level.
- b and beta are both nonzero, so the actuator genuinely affects the performance state in drift and diffusion. The separate output r*u has full positive penalty.
- The zero law is internally exponentially mean-square stable: the positive homogeneous storage

  $$V_0={\sigma^2+1\over2\kappa}f^2+y^2$$

  has derivative of its expectation `-E f^2-2epsilon E y^2`, and hence a strict exponential decay bound. No unstable unobservable mode is being hidden.

Thus:

**Theorem OF (written existence).** For every positive rational h,T,gamma with h<T<=2h, a fully rational constant-matrix plant of (4), with both effective control channels and internal mean-square stability of its exhibited law, is literal-feasible but mean-square-infeasible at gamma, under exactly the counted finite-horizon disturbance convention.

The theorem even permits any preselected rational positive damping/filter rate and nonzero rational c,sigma,b,beta; only the rational output scale and control penalty are chosen afterwards. The coefficient family is described by (7)–(8) using exact compact-operator/Gaussian-function norm endpoints. No explicit numerical d,r or finite algebraic certificate for those endpoints is supplied. This distinction is part of the delivered result, not a hidden missing implementation.

## 5. Relationship to the other packets and remaining obligations

This is the **opposite** feasibility direction from the long-horizon general-parameter family: here literal feasibility does not imply mean-square feasibility. It also explains the previous note's restriction: when h<T<=2h, the zero-law mean-square-to-literal implication holds, but the two levels are actually strictly different.

There is no claim that one fixed plant at one fixed gamma exhibits contradictory directions. The long-horizon and short-horizon constructions have their own data and horizon regimes. No infinite-horizon opposite-direction result follows from this finite compactness argument.

The non-elementary written imports are weak compactness of Hilbert unit balls, compact Hilbert–Schmidt operator properties, centered Gaussian Hilbert random variables and the ordinary unbounded support of a nondegenerate Gaussian projection. Stochastic ingredients are the already displayed deterministic-integrand Itô isometry, Brownian future-increment independence, Tonelli and conditional expectation in separable L2 spaces. The written control-cost lower bound uses no Lenglart/BDG theorem or Riccati theory. None has been formally checked here.

**Exact remaining gap:** general necessary-and-sufficient literal synthesis for arbitrary plant data and prescribed level/horizon; explicit evaluated endpoints ell,m or a finite-dimensional exact certificate for this new nonconstructive family; sharp constants, optimal nonlinear laws, and novelty. A different-domain written reconstruction is needed before any new support label. The old unadmitted arithmetic has no proof-verification credit for this written theorem, and no future arithmetic is authorized by it.
