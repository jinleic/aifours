# Literal preview gain: a causal transfer bound and an infinite-horizon obstruction

**CANDIDATE — written derivation, not independently accepted.** InfoHinfPreview, slot info-3. Frozen against `selection-v1.md`. This is a partial attack on the book's continuous-time, expectation-of-pathwise-L2 criterion, not a replacement by a quadratic objective. No scientific program or numerical experiment was run. All constants below are symbolic; none is claimed optimal.

## 1. Scope, information and notation

Let `W` be Brownian motion with its completed natural filtration, optionally enlarged by independent initial randomization. Future Brownian increments remain independent of the present. The input class contains **all progressively measurable** `w` with finite `E integral |w|^2`. Set

\[
 N_1(f;I)=\mathbb E\big(\int_I|f_t|^2dt\big)^{1/2},\qquad
 N_2(f;I)=\big(\mathbb E\int_I|f_t|^2dt\big)^{1/2}.
\]

The plant remains

\[
 dx_t=(Ax_t+Bu_t+Cw_{t-h})dt+(A_0x_t+B_0u_t)dW_t,
 \quad z_t=D_0x_t+D_1u_t,
 \quad x_0=0,\quad h\ge0.                                      \tag{1}
\]

Negative-time disturbance history is zero. On a finite horizon `[0,T]`, inputs are zero outside `[0,T-h]`; on the infinite horizon their interval is `[0,infinity)`. All gain statements use the indicated horizon, not a limiting substitution of a finite-horizon estimate. Every actual controller is nonanticipative, strongly well posed and zero-preserving. In particular, stopping an input at a stopping time leaves its closed-loop output unchanged before that stopping time. This is strong causality, not access to future Brownian increments. Extra controller randomness is kept fixed between stopped and unstopped trajectories.

`G_p(F)` denotes the induced `N_p` gain of a **fixed** controller `F`, taking the supremum over all nonzero inputs in the preceding square-integrable adapted class. A finite zero-state gain alone does not assert internal stability from arbitrary nonzero initial data.

There are three distinct conclusions:

1. A **causal transfer theorem**, for any fixed strongly causal law, converts a genuine mean-square gain bound into a literal bound with factor `sqrt(2)`, not with factor1.
2. A **reverse infinite-horizon theorem**, for a specified stationary linear preview-controller class, gives `G_2 <= sqrt(3) G_1`. It proves equivalence of finiteness, not equal attenuation levels and not equivalence for arbitrary nonlinear controllers.
3. A **scalar fixed-feedback classification** and an explicit deterministic nonnegative input family give an infinite-horizon literal-gain obstruction beyond the old finite-horizon gamma6 separation.

## 2. A source-checked import, not a new probability inequality

The only non-elementary norm inequality imported is Geiss–Scheutzow, *Sharpness of Lenglart's domination inequality and a sharp monotone version*, arXiv:2101.10884v2 (2021), **Theorem2.2**:

<https://arxiv.org/html/2101.10884v2#S2.Thmtheorem2>.

Its actual hypotheses and conclusion were read: `X,G` are nonnegative, nondecreasing, adapted, right-continuous; `G` is predictable; for every bounded stopping time `tau`,

\[
 \mathbb E[X_\tau\mid\mathcal F_0]
 \le \mathbb E[G_\tau\mid\mathcal F_0].
\]

Then for `0<p<1`,

\[
 \mathbb E X_\infty^p\le p^{-p}\mathbb E G_\infty^p.             \tag{2}
\]

At `p=1/2` its multiplicative constant is `sqrt(2)`. The more familiar general Lenglart bound has the worse constant `p^{-p}/(1-p)`; using that instead would give `2 sqrt(2)`. We use the **monotone** theorem because accumulated input/output energies are monotone. Neither theorem says that two induced norms are equal. The probability inequality and its sharpness are prior art, not this round's discovery.

## 3. Causal mean-square-to-literal transfer

**Theorem A.** Fix a finite or infinite horizon with the input counting convention in §1. Suppose a strongly causal, event-local, zero-preserving controller has a uniform bound

\[
 \mathbb E\int|z_w|^2\le g^2\mathbb E\int|w|^2                 \tag{3}
\]

for every adapted square-integrable input. Then, on the **same horizon and same adapted class**,

\[
 N_1(z_w)\le\sqrt2\,g\,N_1(w),\qquad G_1(F)\le\sqrt2\,G_2(F). \tag{4}
\]

Consequently a controller whose genuinely established mean-square gain is less than `gamma/sqrt(2)` satisfies the book's strict literal criterion at `gamma`. This is a sufficient route, not an N&S characterization at a prescribed `gamma`.

*Proof.* Write `L=T-h` on a finite horizon and `L=infinity` otherwise; extend output energy constantly beyond `T` when `T` is finite. For a fixed input let

\[
 X_t=\int_0^{t\wedge T}|z_w(s)|^2ds,
 \qquad G_t=g^2\int_0^{t\wedge L}|w(s)|^2ds.                   \tag{5}
\]

Both are adapted, continuous and nondecreasing, and `G` is predictable. If `tau` is a bounded stopping time, define the **admissible stopped input**

\[
 w^\tau_s=w_s\,1_{\{s\le\tau\}},\quad 0\le s\le L.
\]

The indicator is progressively measurable and its endpoint is immaterial for time integrals. Strong causality gives `z_(w^tau)=z_w` up to `tau wedge T`. It does not claim equality after stopping and does not reset any controller state. Therefore (3) gives

\[
 \mathbb E X_\tau
 \le\mathbb E\int_0^T|z_{w^\tau}(s)|^2ds
 \le g^2\mathbb E\int_0^{\tau\wedge L}|w(s)|^2ds
 =\mathbb E G_\tau.                                          \tag{6}
\]

For the conditional version, apply precisely the same argument to `1_A w^tau`, for every `A in F_0`. On `A` it has the required stopped output and on the complement it has zero output by event locality and zero preservation. Thus `E[1_A X_tau] <= E[1_A G_tau]`, which is the conditional domination in (2). Apply (2) with `p=1/2` to (5), obtaining (4). If only `G_2(F)` is given, apply the argument at each `g>G_2(F)` and let `g` decrease to that value. QED.

**Larger-input extension.** If the closed loop is locally well posed for pathwise-L2 inputs, (4) also extends to all adapted `w` with `N1(w)<infinity`. Stop `w` when its accumulated squared energy first reaches `b`. Each stopped input has mean-square energy at most `b`; apply (4). On each sample path with finite total input energy, all sufficiently large `b` leave the input and the complete output unchanged. Fatou then proves the extension, since `N1(w^b)<=N1(w)`. This extension is a separate claim and is not needed for the square-integrable-input theorem.

**Why this is not Jensen.** The key is (6), quantified over stopping times and using the same adapted disturbance class. Jensen on output alone does not compare the random input denominators. No same-level implication `G1<=G2` has been established.

## 4. A direct printed-criterion sufficient synthesis certificate

This corollary imports **no Riccati theorem**. Choose constant state feedback `u=Kx` (permitted by the book's window information, though it ignores available preview), and put

\[
 A_K=A+BK,\quad N_K=A_0+B_0K,\quad Z_K=D_0+D_1K.
\]

Suppose `P=P^T>0`, `g>0`, `epsilon>0` satisfy

\[
 \begin{pmatrix}
 A_K^TP+PA_K+N_K^TPN_K+Z_K^TZ_K & PC\\
 C^TP & -g^2I
 \end{pmatrix}
 \preceq-\begin{pmatrix}\epsilon I&0\\0&0\end{pmatrix}.       \tag{7}
\]

Then for **every fixed `h>=0`**, on either counted horizon,

\[
 G_1(K)\le\sqrt2\,g.                                         \tag{8}
\]

Indeed, Itô's formula for `V=x^TPx` gives, with `v_t=w_(t-h)`,

\[
 dV+\big(|z|^2+\epsilon|x|^2-g^2|v|^2\big)dt
 \le 2x^TPN_Kx\,dW.                                         \tag{9}
\]

Stop when state and input energy are bounded; on those stops the stochastic integral has expectation zero. Its integrand squared is bounded by a constant times the fourth power of the bounded state, so it is integrable on bounded time intervals. Drop the nonnegative terminal storage, pass through localization by Fatou, and then increase the deterministic terminal time if necessary. The shifted input obeys `integral_0^T|v|^2=integral_0^(T-h)|w|^2` in finite time and equality of full energies in infinite time. This proves (3), and Theorem A proves (8). For `w=0`, (9) also gives exponential mean-square decay: `d E V/dt <= -(epsilon/lambda_max(P)) E V`. Thus this sufficient certificate supplies internal stability, not only zero-state gain.

For any prescribed `gamma`, (7) with `sqrt(2)g<gamma` is therefore an explicit sufficient controller/certificate for the **printed** problem. It is generally conservative, is not necessary, and uses no claim that the old advanced Riccati equation is correct for the printed norm. It is a direct consequence of a quadratic storage calculation plus classical monotone Lenglart, not a claimed novel Riccati solution.

## 5. Reverse comparison without resetting the plant

Here the horizon is **infinite**. Fix a deterministic, time-homogeneous linear controller of the concrete book-information form

\[
 u_t=Kx_t+\sum_{j=1}^mJ_jw(t-r_j)
               +\int_0^h H(r)w(t-r)dr,
 \quad 0\le r_j\le h,\quad H\in L^2([0,h]).                 \tag{10}
\]

All taps, matrices and the kernel are fixed; zero histories are used. The same Brownian motion drives the full plant. This includes static state feedback and genuine finite-window preview feedforward; it is **not** every nonlinear/history-dependent law from the book. We work on canonical Wiener space; independent initial randomization does not enlarge the mean-square operator norm, by conditioning on its seed. Finite-time input-output continuity and second-moment finiteness follow from the linear SDE with bounded coefficients and finite-window bounded input terms. These facts do not require infinite-horizon stability.

**Theorem B.** For every fixed controller (10), with gains in the extended nonnegative reals,

\[
 \frac1{\sqrt3}G_2(F)\le G_1(F)\le\sqrt2\,G_2(F).             \tag{11}
\]

In particular, its infinite-horizon literal gain is finite **if and only if** its mean-square gain is finite. This is not equality of levels, is not a finite-horizon theorem, and does not assert internal stability of unobservable modes.

*Elementary Hilbert-sign inequality.* For finitely many vectors `v_i` in a real Hilbert space and independent formal signs `eta_i=+/-1`, let `S=sum eta_i v_i`, `V=sum ||v_i||^2`. Expanding the second and fourth moments gives

\[
 \mathbb E_\eta\|S\|^2=V,\qquad
 \mathbb E_\eta\|S\|^4
 =V^2+4\sum_{i<j}\langle v_i,v_j\rangle^2\le3V^2.            \tag{12}
\]

Hölder applied to `||S||^(2/3) ||S||^(4/3)` yields

\[
 V\le(\mathbb E_\eta\|S\|)^{2/3}
       (\mathbb E_\eta\|S\|^4)^{1/3},
 \quad\text{hence}\quad
 \mathbb E_\eta\|S\|\ge\sqrt{V/3}.                          \tag{13}
\]

The constant `1/sqrt(3)` is deliberately elementary and not asserted sharp.

*Proof of the lower bound.* Start with any nonzero adapted Brownian-functional template input `v`, supported on `[0,S]`, and observe its zero-state response through a finite time `L>S+h`. Put

\[
 X=\int_0^S|v_t|^2dt,\quad
 Y=\int_0^L|z_v(t)|^2dt,\quad 0<\mathbb EX<\infty.            \tag{14}
\]

`EY` is finite by finite-time linear-SDE estimates. In each block `I_i=[iL,(i+1)L]`, use the same progressively measurable template functional, now driven by **that block's Brownian increment path** `W_(iL+t)-W_(iL)`. Denote the input copy by `v_i`, supported in `[iL,iL+S]`, and the full zero-state component output, on the actual common Brownian path, by `y_i`. Before `iL` this component has zero input/state/output. Its output energy on `I_i`, called `Y_i`, has the law of `Y`, and these `Y_i` are independent. Likewise its input energy is `X_i` with the law of `X`. Independence here concerns the local block energies, **not the complete overlapping output tails**.

For any **deterministic** sign vector `eta` of length `n`, let `w_eta=sum_(i=0)^(n-1) eta_i v_i`. Its input supports are disjoint; it is adapted and has finite mean-square energy. Linearity under the common Brownian motion gives exactly

\[
 z_{w_\eta}=\sum_i\eta_i y_i.                                \tag{15}
\]

The physical plant is never reset. Its old state and every output tail are present in (15). Apply (13), conditional on the Brownian path, in the Hilbert space `L2([0,nL];R^p)`. Since `sum_i ||y_i||_(0,nL)^2 >= sum_i Y_i`,

\[
 2^{-n}\sum_\eta N_1(z_{w_\eta};[0,nL])
 \ge\frac1{\sqrt3}\mathbb E\sqrt{\sum_iY_i}.                 \tag{16}
\]

Every sign vector has the **same** input norm `E sqrt(sum_i X_i) <= sqrt(n EX)`. If `G1(F)` is finite, its defining inequality, averaged over these finitely many deterministic sign inputs, and (16) imply

\[
 G_1(F)\ge\frac{\mathbb E\sqrt{n^{-1}\sum_iY_i}}
                  {\sqrt{3\mathbb EX}}.                    \tag{17}
\]

There is no requirement that signs be supplied by a new random source or chosen in response to future noise; averaging proves that an admissible deterministic sign pattern exists. No sign enumeration was executed.

For completeness, the only averaging limit needed can be proved without an ergodic theorem. For fixed `M>0`, the independent variables `Y_i wedge M` have common mean `mu_M=E(Y wedge M)` and variance at most `M^2`. Chebyshev gives, for `0<delta<mu_M`,

\[
 \mathbb E\sqrt{n^{-1}\sum_iY_i}
 \ge\sqrt{\mu_M-\delta}\left(1-\frac{M^2}{n\delta^2}\right).
                                                                  \tag{18}
\]

Take `n->infinity`, then `delta->0`, then `M->infinity`; monotone convergence yields `liminf >=sqrt(EY)`. Thus (17) gives

\[
 G_1(F)\ge\frac1{\sqrt3}\sqrt{\mathbb EY/\mathbb EX}.        \tag{19}
\]

Finally, the supremum of the right-hand template ratios is the full infinite-horizon mean-square gain. To see the nontrivial direction, fix any square-integrable adapted input `w` and an output observation time `R`. Truncate the input at `R`; by causality its output up to `R` is unchanged, its total input energy is no larger, and it is a template with `S=R`, observed through any `L>R+h`. Consequently the template supremum bounds `N2(z_w;[0,R])/N2(w;[0,infinity))`. Let `R` increase and use monotone convergence, then take the input supremum. Equation(19) proves the lower half of (11), including `G2=infinity`. The upper half is Theorem A. QED.

**Synthesis meaning and exact limit.** Let `g_p^lin` be the infimum of `Gp(F)` over the **same** class(10). Then

\[
 g_2^{lin}/\sqrt3\le g_1^{lin}\le\sqrt2\,g_2^{lin}.           \tag{20}
\]

Thus existence of *some finite attenuation level* is equivalent within this class. At a specified `gamma`, only sufficient/exclusion bands follow. Nonlinear controllers, time-varying feedback and arbitrary controller memory do not satisfy the superposition argument; no general synthesis necessity is inferred for them.

## 6. A fully quantified scalar infinite-horizon obstruction

Consider a scalar state with effective scalar feedback fixed at `u=kx`,

\[
 dx_t=[a_kx_t+c w(t-h)]dt+\sigma_kx_t dW_t,\qquad z_t=d_kx_t,
\]

where `a_k=a+bk`, `sigma_k=sigma+beta k`, `d_k=D0+D1 k` is a nonzero output vector, and `c!=0`. Set

\[
 q_k=2a_k+\sigma_k^2.                                       \tag{21}
\]

**Corollary C.** For this fixed feedback and every fixed finite `h>=0`,

\[
 G_1(k)<\infty\quad\Longleftrightarrow\quad q_k<0.            \tag{22}
\]

If `q_k<0`, a concrete (not optimal) bound is

\[
 G_1(k)\le {2\sqrt2\,|c|\,|d_k|\over -q_k}.                 \tag{23}
\]

If `q_k>=0`, then **for each finite number `Gamma` there is a deterministic, nonnegative-up-to-the-sign-of-c, compactly supported finite-energy input with literal output/input ratio greater than `Gamma`**. This impossibility is stronger than failure for a single pulse or one finite horizon, but remains a fixed-feedback result.

*Proof of sufficiency.* Write `kappa=-q_k>0`. Itô gives `d E x^2/dt=-kappa E x^2+2c E(xv)`, `v=w(t-h)`. The elementary square inequality gives `2|c xv| <= (kappa/2)x^2+(2c^2/kappa)v^2`. Integrate, localize, and drop the nonnegative terminal second moment to obtain

\[
 \mathbb E\int_0^\infty|d_kx|^2
 \le{4c^2|d_k|^2\over\kappa^2}\mathbb E\int_0^\infty|w|^2.
\]

Theorem A proves(23). This proof covers **all adapted inputs**, not only deterministic ones.

*Deterministic-input proof of necessity, avoiding any controller reset or norm substitution.* Absorb `c`'s sign into the input. A single unit pulse of duration1, after arrival at the plant, has positive zero-state response `p(t)` solving

`dp=(a_k p+|c| 1_[0,1])dt+sigma_k p dW`, `p(0)=0`.

The stochastic exponential is strictly positive, hence `p(1)>0` almost surely. Its second moment `m=E p(1)^2` is finite and strictly positive. After time1 the forcing is zero and independence of future increments gives

\[
 \mathbb E p(t)^2=m\,e^{q_k(t-1)},\qquad t\ge1.               \tag{24}
\]

For a block of length `L>h+1`, let its isolated pulse start in input time0, so it reaches the state at time `h`. The expected output energy through the block obeys

\[
 \mathbb EY_L\ge |d_k|^2m\int_0^{L-h-1}e^{q_k r}dr.           \tag{25}
\]

The right side tends to infinity with `L` when `q_k>=0`, including the boundary `q_k=0`.

Now use the **actual** deterministic input

\[
 w_{n,L}(t)=\operatorname{sgn}(c)
                \sum_{i=0}^{n-1}1_{[iL,iL+1]}(t).           \tag{26}
\]

Its norm is exactly `N1(w_(n,L))=sqrt(n)`; it is in the stipulated adapted mean-square-input class. Every component state response is nonnegative. On its own block the full state is therefore at least that block's isolated pulse response, despite all earlier tails remaining present. The local block energies `Y_(L,i)` are independent copies of `Y_L`, so

\[
 {N_1(z_{w_{n,L}})\over N_1(w_{n,L})}
 \ge \mathbb E\sqrt{n^{-1}\sum_{i=0}^{n-1}Y_{L,i}}.           \tag{27}
\]

Use the explicit finite-`n` bound(18), with `Y_L` in place of `Y`. Given `Gamma`, first choose `L` so (25) is greater than `Gamma^2`; next choose `M` with `mu_M>Gamma^2`, then `delta` with `sqrt(mu_M-delta)>Gamma`; finally choose an integer

\[
 n>{M^2\over\delta^2\,[1-\Gamma/\sqrt{\mu_M-\delta}]}.        \tag{28}
\]

Equations(18),(27) now make the ratio strictly greater than `Gamma`. These are literal `E sqrt(energy)` inequalities for actual finite-energy inputs. No physical reset, stochastic simulator, numerical search or unrestricted mean-square replacement is used. QED.

**What is counterintuitive, and what is not claimed.** When `a_k<0<=q_k`, the expected pathwise-L2 norm of the stochastic exponential after one pulse is finite: split time into unit blocks, use `E Phi(j,0)=e^(a_k j)` and Cauchy–Schwarz inside a block to bound the expected total norm by

\[
 \frac{\sqrt{\int_0^1e^{q_k r}dr}}{1-e^{a_k}}<\infty.
\]

The forced pulse has finite expected amplitude at its end and independent future noise, so its entire output also has finite `N1`. More generally the old finite-support convolution argument applies. Yet(26)–(28) show the **infinite-horizon induced gain is infinite**. Thus finite expected output for every individual compact input, or a finite one-pulse norm, is not a finite-gain certificate. The previous gamma6 example did not establish this infinite-horizon statement, and it is not being reused as the new result.

If actuation is absent (`B=B0=0`) and `z=(x,r u)` with `r>0`, then `u=0` is pathwise optimal and the no-go for `q>=0` is an **all-controller** no-go, even allowing arbitrary adapted preview controls. This is a transparent uncontrollable subcase, not a result for effective general actuation. For nonzero `b` or `beta`, Corollary C classifies each fixed `k` only; it does not exclude better preview/nonlinear laws.

## 7. Current source audit and acceptance boundary

* Book printed pp674–676: actual images read; pathwise norm, expectations, continuous-time model, preview window and both horizons confirmed.
* Wang–Zhang–Chen–Yu2014 DOI10.11918/j.issn.0367-6234.2014.07.017: actual6-page primary PDF retrieved into `sources/wang-2014.pdf` and read. Page102 equations(1)–(5) give continuous time, **B0=0**, finite horizon, and **expected squared norm** plus terminal penalty in(4). Page103 Theorem1 gives sufficiency from bounded coupled equations(21)–(24); it does not give literal-norm necessity. No theorem from it is imported here.
* Wang–Fu–Zhang2020 author manuscript: p2 Hilbert norm and p3 equations(2.1),(2.4) confirm discrete time, finite horizon, mean square. Its inertia/Riccati theorem is **not imported**.
* Geiss–Scheutzow2021 Theorem2.2: genuine primary import checked in§2, with the actual stopping-time and predictability hypotheses verified in§3. Its probability theorem is already known. Section5's elementary sign and averaging arguments are written out and do not import a hidden Riccati result, BDG constant or ergodic theorem.
* Local and remote `openai/math` catalogue screens are in `selection-v1.md`; no matched preview/Riccati claim was located. This is a bounded screen, not priority certification.

**Correctness:** candidate pending separate reconstruction and full parent read. **Import trust:** explicit classical monotone Lenglart theorem plus ordinary Itô/strong linear-SDE well-posedness, Hölder, Chebyshev and monotone/Fatou integration. **Scope:** same printed criterion; finite/infinite upper transfer; infinite stationary-linear reverse comparison; fixed scalar-law complete finiteness classification. **Novelty:** UNCLEAR; the upper transfer is a classical extrapolation application, not new probability theory. No first/best-known/solved-book claim. **Significance:** a rigorous finite-gain bridge and a horizon-sensitive no-go prevent misuse of the finite-horizon separation, but leave general optimal-level synthesis open.

The exact remaining problem is **necessary and sufficient literal synthesis at a prescribed gamma for the book's full controller class**, with both finite and infinite horizons and nonzero control-dependent noise. Neither the factor bounds nor the scalar subcase settles it. No scientific executable, independent-model CLI, kernel proof, external expert review or publication has occurred.
