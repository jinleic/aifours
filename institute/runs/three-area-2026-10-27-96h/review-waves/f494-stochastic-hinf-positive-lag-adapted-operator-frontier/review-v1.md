# author-candidate-v1.md — F494 positive-lag stochastic gain

**Status: AUTHOR CANDIDATE.** This return establishes a causal E1 extension, exact zero cases, a deterministic Gaussian variational characterization, an exact reduction to that characterization when \(T/2\le \tau<T\), and genuine adapted lower witnesses when \(T>2\tau\). It does **not** establish a closed-form general positive-lag gain, nonattainment of its actual supremum, or controller synthesis.

**Materialization:** Complete body returned here for Main. No repository file was written.

## 1. Binding, chronology, and execution limits

The assigned wave is `f494-stochastic-hinf-positive-lag-adapted-operator-frontier`.

- Manifest: `c7aa13f9a350693a4db0f17e5a7d39ec4776d60d86995a93914f6548e914d758`.
- Freeze receipt: `7bc193052ee9828b5708bbb026efdbd5b98f21b4cb51c3cda8b1196b2d36d5b1`.
- Literal packet: `f38936f704f3afe228c7ecca29853650f6251896f9421e6dd8197128c9d0b01d`.

These bindings, byte/LF counts, and the clock `2026-10-30T12:22:49-0700 PDT` are **parent-supplied observations**, not child-executed hashing or a child-native start time.

I read the manifest, receipt, parent metadata supply, and all declared status/permission controls through their endings before sending the direct pre-body ACK. I then read the entire 119-LF literal packet in ordered raw windows 1–20, 21–40, 41–60, 61–80, 81–100, and 101–119 before the mathematical work below. The ACK’s metadata-supply endpoint label “104” was a transcription error: the pre-ACK read included the closing brace at LF105.

All held scientific payloads and their consumers remain NONINPUT. Their controls were read only for status and permissions.

**Scientific execution: NOTRUN.** No scientific program, numerical calculation, test, solver, external-model CLI, or public-source search was executed. The results below are written mathematical arguments. No executable code or numerical output is offered as evidence.

## 2. Exact law and admissibility

Let \(n,m,p\ge1\), and let

\[
P\in\mathbb R^{n\times n},\qquad
B\in\mathbb R^{n\times m},\qquad
C\in\mathbb R^{p\times n}.
\]

Fix \(T>0\) and \(\tau>0\). Let \(W\) be one real Brownian motion relative to a usual filtration \((\mathcal F_t)\). In particular, future Brownian increments are independent of \(\mathcal F_t\).

Consider exactly

\[
dx_t=Px_t\,dt+B w_{t-\tau}\,dW_t,\qquad
x_0=0,\qquad z_t=Cx_t,
\]

with **zero input prehistory**

\[
w_s=0\quad\text{for }s<0.
\]

On \([0,T]\), inputs are \(\mathbb R^m\)-valued progressive processes. Write

\[
\|w\|_T=\left(\int_0^T |w_s|^2\,ds\right)^{1/2}.
\]

The two domains are

\[
\mathcal E_1=\{w:\mathbb E\|w\|_T<\infty\},\qquad
\mathcal E_2=\{w:\mathbb E\|w\|_T^2<\infty\}.
\]

A nonzero input means \(0<\mathbb E\|w\|_T<\infty\). The literal gain is

\[
L_\tau=
\sup_{w\in\mathcal E_1,\;w\ne0}
\frac{\mathbb E\|z(w)\|_T}{\mathbb E\|w\|_T}.
\]

The expectation is outside each path norm. This is not an RMS criterion.

Set

\[
H=(T-\tau)_+,\qquad
G(u)=B^\top\int_0^u e^{P^\top v}C^\top C e^{Pv}\,dv\,B,
\qquad
c_H=\sqrt{\lambda_{\max}G(H)}.
\]

Only \(w|_{[0,H]}\) can affect the output. Setting the unused input tail to zero leaves the numerator unchanged and cannot increase the denominator.

### Frozen analytic import

The general upper bounds involving \(r\) below use the frozen S2 E2 weighted inequality for the actual zero-lag law:

\[
\mathbb E\|z(v)\|_T
\le
r\,\mathbb E
\left(\int_0^T v_t^\top G(T-t)v_t\,dt\right)^{1/2}
\]

for progressive E2 inputs \(v\). Here \(r\) is the unique positive zero of

\[
g(y)=e^{y^2/2}-y\int_0^y e^{s^2/2}\,ds.
\]

This is an explicitly retained import, not a new verification of its Bellman/generalized-Itô proof. Since \(g\) decreases on \((0,\infty)\), \(g(1)>0\), and \(g(y)\le1-y^2/2\), one has \(r>1\).

The positive-lag sharpness question is **not** included in that import.

## 3. Why an unrestricted zero-lag sharpness argument is invalid

For \(0<\tau<T\), put

\[
\beta_u=W_{\tau+u}-W_\tau,\qquad 0\le u\le H.
\]

Then

\[
y_u:=z_{\tau+u}
=
\int_0^u C e^{P(u-s)}B w_s\,d\beta_s.
\]

Although \(\beta\) is Brownian relative to \(\mathcal G_u=\mathcal F_{\tau+u}\), the admissible coefficient \(w_s\) must remain \(\mathcal F_s\)-measurable. It is not an arbitrary \(\mathcal G_s\)-adapted coefficient.

For example, a coefficient chosen using \(\beta_s=W_{\tau+s}-W_\tau\) generally requires information unavailable at input time \(s\). Thus the shifted formula permits importing a zero-lag **upper inequality**, but not an unrestricted zero-lag **lower witness**.

The long-lag result below proves that the distinction changes the actual gain.

## 4. Causal E1 extension and general bounds

### Proposition 1 — Local E1 solution, weighted bound, and equality of E1/E2 suprema

For the stated law, every E1 input has its actual local Itô solution, its output belongs to \(L^1(\Omega;L^2[0,T])\), and

\[
\mathbb E\|z(w)\|_T
\le r\,\mathbb E Q_H(w),
\]

where

\[
Q_H(w)=
\left(\int_0^H w_s^\top G(H-s)w_s\,ds\right)^{1/2}.
\]

Moreover, the E1 and E2 literal gain suprema coincide.

#### Proof

Use the pointwise progressive cutoffs

\[
w^{(k)}_s=w_s\,\mathbf1_{\{|w_s|\le k\}}.
\]

These are progressive and E2. For almost every path,

\[
\|w-w^{(k)}\|_T\longrightarrow0,
\qquad
\|w-w^{(k)}\|_T\le\|w\|_T.
\]

Therefore

\[
\mathbb E\|w-w^{(k)}\|_T\longrightarrow0.
\]

For two cutoff inputs, the imported E2 inequality, applied to their delayed difference, gives

\[
\mathbb E\|z(w^{(k)})-z(w^{(\ell)})\|_T
\le
r c_H\,\mathbb E\|w^{(k)}-w^{(\ell)}\|_T.
\]

Thus their outputs are Cauchy in \(L^1(\Omega;L^2[0,T])\).

This limit must still be identified with the **actual** local solution. Write

\[
x_t=e^{Pt}M_t,\qquad
M_t=\int_\tau^t e^{-Pr}B w_{r-\tau}\,dW_r,
\]

with the integral zero for \(t\le\tau\). The trace bracket of \(M-M^{(k)}\) at \(T\) is bounded by

\[
K\int_0^H |w_s-w^{(k)}_s|^2\,ds
\longrightarrow0
\quad\text{almost surely},
\]

for a finite deterministic \(K\). Stop the difference martingale when this bracket reaches \(\delta\). Doob’s inequality gives, for \(\eta>0\),

\[
\mathbb P\!\left(\sup_{t\le T}|M_t-M^{(k)}_t|>\eta\right)
\le
\mathbb P(A_T^{(k)}>\delta)+\frac{4\delta}{\eta^2}.
\]

First let \(k\to\infty\), then \(\delta\downarrow0\). Hence the actual cutoff solutions converge uniformly in probability to the actual local solution. Uniqueness of probability limits identifies the Banach-space limit with its output.

Finally,

\[
|Q_H(u)-Q_H(v)|\le c_H\|u-v\|_T.
\]

Passing to the limit proves the E1 inequality. For every nonzero E1 input, both numerator and denominator of its cutoff ratios converge to the actual ratio. Hence its ratio is bounded by the E2 supremum. The reverse inclusion follows from \(\mathcal E_2\subset\mathcal E_1\). ∎

No full-path-norm indicator is used.

### Proposition 2 — Strictness of the \(r c_H\) upper bound

If \(H>0\) and \(c_H>0\), every nonzero E1 input satisfies

\[
\mathbb E\|z(w)\|_T
<
r c_H\,\mathbb E\|w\|_T.
\]

#### Proof

For every \(s\in(0,H]\) and nonzero \(a\),

\[
a^\top G(H-s)a<c_H^2|a|^2.
\]

Otherwise equality in

\[
G(H-s)\preceq G(H)\preceq c_H^2 I
\]

would imply

\[
\int_{H-s}^H |Ce^{Pv}Ba|^2\,dv=0.
\]

The analytic function \(v\mapsto Ce^{Pv}Ba\) would vanish identically, contradicting \(a^\top G(H)a=c_H^2|a|^2>0\).

Consequently, on every path with nonzero input norm,

\[
Q_H(w)<c_H\|w\|_T.
\]

Unused-tail energy also makes this inequality strict. Taking expectations and applying Proposition 1 proves the claim. ∎

**Important limitation:** this proves that no nonzero input attains the upper bound \(r c_H\). It does **not** prove nonattainment of the actual supremum \(L_\tau\), because sharpness of that upper bound has not been established.

## 5. Exact zero cases and history dependence

### Proposition 3 — Complete zero classification

With zero prehistory:

1. If \(\tau\ge T\), then \(z=0\) and \(L_\tau=0\).
2. If \(0<\tau<T\), then
   \[
   L_\tau=0
   \quad\Longleftrightarrow\quad
   c_H=0
   \quad\Longleftrightarrow\quad
   CP^kB=0,\quad k=0,\ldots,n-1.
   \]

At \(\tau=T\), the possible value of the integrand at the single terminal time has no Itô-integral contribution.

For \(H>0\), \(G(H)=0\) is equivalent to \(Ce^{Pv}B=0\) throughout an interval, hence everywhere by analyticity. Taylor expansion and Cayley–Hamilton give the finite matrix criterion. Conversely, if \(c_H>0\), the burst construction in §6 gives a positive gain. ∎

### Nonzero prehistory is a different problem

Suppose a fixed admissible prehistory \(h\) on \([-\tau,0)\) is supplied but is **not charged** in the input denominator. Write

\[
z(w)=z^h+z^w.
\]

If \(0<\mathbb E\|z^h\|_T<\infty\), choose any fixed nonzero admissible \(u\) and put \(w=\varepsilon u\). Then

\[
\mathbb E\|z(\varepsilon u)\|_T
\ge
\mathbb E\|z^h\|_T-\varepsilon\mathbb E\|z^u\|_T,
\]

while the denominator tends to zero. The gain is infinite.

Thus “zero prehistory,” “uncharged prescribed history,” and “history included in the norm” cannot be interchanged. The finite-gain statements in this return use zero prehistory.

## 6. Deterministic bursts and a compact Gaussian optimization

Assume \(H>0\). Let

\[
\mathcal H=L^2([0,H];\mathbb R^p),
\]

and define the deterministic impulse operator

\[
(F_s a)(u)
=
\mathbf1_{\{u\ge s\}}Ce^{P(u-s)}Ba.
\]

It satisfies

\[
\|F_s a\|_{\mathcal H}^2=a^\top G(H-s)a.
\]

The map \(s\mapsto F_s\) is continuous in operator norm. The changing support contributes an \(O(|s-s'|)\) term to the squared norm difference, and the exponential kernel is uniformly continuous on the remaining compact region.

### 6.1 Single-burst lower limit

Let \(|a|=1\) be a top eigenvector of \(G(H)\), and choose

\[
w_s^{(\delta)}
=
\delta^{-1/2}a\,\mathbf1_{[0,\delta]}(s),
\qquad 0<\delta<H.
\]

This input is deterministic, progressive, E2, and has path norm one. Its shifted output converges in \(L^2(\Omega;\mathcal H)\) to \(F_0a\,Z\), with \(Z\sim N(0,1)\). Indeed, the squared error is

\[
\frac1\delta\int_0^\delta
\|(F_s-F_0)a\|_{\mathcal H}^2\,ds\longrightarrow0.
\]

Writing \(\kappa=\mathbb E|Z|=\sqrt{2/\pi}\), this proves

\[
L_\tau\ge \kappa c_H.
\]

The comparison vector \(F_0a\,Z\) is only an output-limit device. It is not used as an anticipative input.

### 6.2 Exact deterministic-input gain

Let

\[
K=[0,H]\times S^{m-1}.
\]

For a probability measure \(\mu\) on \(K\), define

\[
Q_\mu
=
\int_K (F_s a)\otimes(F_s a)\,d\mu(s,a),
\]

and let \(Z_\mu\) be a centered \(\mathcal H\)-valued Gaussian with covariance \(Q_\mu\). Set

\[
J(\mu)=\mathbb E\|Z_\mu\|_{\mathcal H},
\qquad
D_H=\max_{\mu\in\mathcal P(K)}J(\mu).
\]

Then \(D_H\) is exactly the supremum over deterministic L2 inputs of the literal expected-path-norm ratio.

To see this, a deterministic nonzero profile \(v\) defines the probability measure

\[
\mu_v(ds,da)
=
\frac{|v_s|^2\,ds}{\|v\|_{L^2}^2}
\,\delta_{v_s/|v_s|}(da),
\]

with zero values ignored. Its normalized output covariance is \(Q_{\mu_v}\).

Conversely, every finite atomic measure is approximated by deterministic narrow, disjoint input bursts with the corresponding energy masses and directions. Repeated atom times are approximated by nearby distinct times. General probability measures are approximated by finite atomic measures.

The maximum exists. Here are the relevant continuity details:

- \(\{F_s a:(s,a)\in K\}\) is compact in \(\mathcal H\).
- For every \(\varepsilon>0\), it is uniformly within \(\varepsilon\) of a finite-dimensional subspace \(V\).
- Consequently,
  \[
  \mathbb E\|(I-\Pi_V)Z_\mu\|^2\le\varepsilon^2
  \]
  uniformly in \(\mu\).
- The finite-dimensional covariance entries depend continuously on \(\mu\) in the weak topology, as does the corresponding Gaussian expected norm.
- Therefore \(J\) is a uniform limit of continuous finite-dimensional functions.

Weak compactness of probability measures on the compact space \(K\) gives a maximizer. These standard Hilbert-Gaussian and compactness facts are the analytic inputs for this variational characterization.

### 6.3 Strict deterministic bounds

If \(c_H>0\), then

\[
\boxed{\kappa c_H<D_H<c_H.}
\]

For the upper inequality,

\[
J(\mu)^2\le\mathbb E\|Z_\mu\|^2
=\operatorname{tr}Q_\mu\le c_H^2.
\]

If the compact maximum equaled \(c_H>0\), equality in Jensen would require a nonzero Gaussian vector to have constant norm almost surely. This is impossible: a nonzero one-dimensional Gaussian projection is unbounded. Hence \(D_H<c_H\).

For the strict lower inequality, let \(a\) be the top vector above, \(f=F_0a\), and choose \(s\in(0,H)\), \(g=F_sa\). These vectors are nonzero and noncollinear: \(g\) vanishes on \([0,s)\), whereas analyticity prevents \(f\) from vanishing throughout that interval.

Write \(f=c_H e_1\) and \(g=\alpha e_1+\beta e_2\), with \(\beta\ne0\). For the two-atom measure with masses \(1-\theta,\theta\), its Gaussian expected norm equals

\[
j(\theta)
=
\mathbb E
\sqrt{(1-\theta)c_H^2X^2
+\theta(\alpha X+\beta Y)^2},
\]

where \(X,Y\) are independent standard normals. At zero,

\[
j'(0+)
=
\mathbb E
\frac{(\alpha X+\beta Y)^2-c_H^2X^2}
     {2c_H|X|}
=+\infty.
\]

The positive divergence is supplied by \(\beta^2Y^2/|X|\); the negative part is integrable. The difference quotients are bounded below by \(-c_H|X|\), so the one-sided expectation limit is justified by monotone convergence after adding this integrable bound.

Thus \(j(\theta)>j(0)=\kappa c_H\) for sufficiently small positive \(\theta\). Approximating the two atoms by actual deterministic bursts proves the strict lower bound.

In particular, the single Gaussian impulse is a valid lower witness but is **not** sharp.

## 7. Exact long-lag reduction

### Theorem 4 — \(T/2\le\tau<T\)

If \(H=T-\tau\le\tau\), then

\[
\boxed{L_\tau=D_H.}
\]

Consequently, when \(c_H>0\),

\[
\boxed{\sqrt{2/\pi}\,c_H<L_\tau<c_H<r c_H.}
\]

#### Proof

The entire active input profile \(w|_{[0,H]}\) is \(\mathcal F_\tau\)-measurable. Brownian increments after \(\tau\) are independent of \(\mathcal F_\tau\).

Conditional on \(\mathcal F_\tau\), the active profile is therefore fixed, and the shifted output is a centered Gaussian with covariance

\[
\int_0^H (F_s w_s)\otimes(F_s w_s)\,ds.
\]

Thus

\[
\mathbb E[\|z(w)\|_T\mid\mathcal F_\tau]
\le
D_H\left(\int_0^H |w_s|^2\,ds\right)^{1/2}.
\]

For E1 inputs, the conditional statement follows by the same progressive cutoffs, or directly by the conditional deterministic Gaussian construction. Taking expectations proves \(L_\tau\le D_H\). Deterministic profiles are admissible and approach \(D_H\), proving the reverse inequality. ∎

This includes the endpoint \(T=2\tau\). A value at the common endpoint does not create an interval in which the controller can react to the first applied noise.

### Explicit falsification of a zero-lag transfer

For the actual scalar subcase \(P=0,\ B=C=1\), one has \(c_H=\sqrt H\). Therefore, whenever \(T/2\le\tau<T\),

\[
\sqrt{2/\pi}\sqrt H
<
L_\tau
<
\sqrt H
<
r\sqrt H.
\]

Hence the proposed carryover \(L_\tau=r c_{T-\tau}\) is false, already within this scalar subcase. The general matrix long-lag theorem above, not this example alone, is the substantive result.

The variational formula evaluates the stochastic optimization exactly in terms of a compact deterministic Gaussian optimization. It does **not** supply a closed-form evaluation of that remaining optimization.

## 8. Genuine adapted lower bursts

For shorter lag, a valid lower family can use observed applied noise, but its physical timing must be retained.

Let \(N\ge1\) satisfy

\[
N\tau<T.
\]

Choose \(\delta>0\) with \(N\tau+N\delta<T\), and define

\[
s_j=(j-1)(\tau+\delta),\qquad t_j=s_j+\tau.
\]

Let

\[
Z_j=\frac{W_{t_j+\delta}-W_{t_j}}{\sqrt\delta}.
\]

These are independent standard normals. Choose bounded Borel functions

\[
a_j=h_j(Z_1,\ldots,Z_{j-1})\in\mathbb R^m,
\]

and set

\[
w_s^{(\delta)}
=
\sum_{j=1}^N
\delta^{-1/2}a_j\,\mathbf1_{[s_j,s_j+\delta]}(s).
\]

This is genuinely admissible because

\[
t_{j-1}+\delta=s_j.
\]

All prior \(Z_i\) have been observed by the time \(a_j\) is selected. The amplitudes are held constant during their input bursts; no future applied increment is used.

The path input norm is exactly

\[
\|w^{(\delta)}\|_T
=
\left(\sum_{j=1}^N|a_j|^2\right)^{1/2}.
\]

As \(\delta\downarrow0\), the output expected norm converges to that of

\[
Y=\sum_{j=1}^N
F_{(j-1)\tau}
h_j(Z_1,\ldots,Z_{j-1})Z_j.
\]

The proof uses Hilbert-space Itô isometry on the disjoint applied-noise intervals and continuity of \(F_s\). Boundedness of the \(h_j\) makes the error tend to zero in \(L^2(\Omega;\mathcal H)\).

Therefore every such family supplies the rigorous lower bound

\[
L_\tau\ge
\frac{
\mathbb E\left\|
\sum_{j=1}^N
F_{(j-1)\tau}
h_j(Z_{<j})Z_j
\right\|_{\mathcal H}
}{
\mathbb E\left(\sum_{j=1}^N|h_j(Z_{<j})|^2\right)^{1/2}
},
\]

provided the denominator is positive.

For example, when \(T>2\tau\), the choices

\[
h_1=v_1,\qquad
h_2(Z_1)=v_2\,\mathbf1_{\{|Z_1|\le b\}},
\]

with \(v_1,v_2\ne0\), \(b>0\), give a nonconstant causal response to the first applied-noise observation.

These are genuine adapted witnesses. No optimization or numerical value of their finite-dimensional Gaussian integrals is claimed. They do not establish that the general upper bound \(r c_H\) is sharp.

## 9. Lag endpoints and regularity

The gain is nonincreasing in \(\tau\).

Indeed, if \(0\le\tau_1<\tau_2\), put \(d=\tau_2-\tau_1\) and, after removing an unused tail, transform a \(\tau_2\)-input into

\[
\widetilde w_s=
\begin{cases}
0,&s<d,\\
w_{s-d},&s\ge d.
\end{cases}
\]

This is adapted, preserves its input norm, and satisfies

\[
\widetilde w_{t-\tau_1}=w_{t-\tau_2}.
\]

It produces exactly the same output. Hence \(L_{\tau_1}\ge L_{\tau_2}\).

For a fixed E1 input, zero-extended time translation is continuous in \(L^1(\Omega;L^2)\). The imported zero-lag bound applied to the difference of two delayed inputs therefore makes the actual output continuous in the delay. Together with monotonicity, this proves right continuity of \(L_\tau\).

At the endpoints:

\[
\lim_{\tau\uparrow T}L_\tau=0,
\]

because \(L_\tau\le r c_{T-\tau}\to0\).

At \(\tau=0\), the frozen zero-lag result gives \(L_0=r c_T\). Approximating a fixed nearly sharp zero-lag input by its delayed versions proves

\[
\lim_{\tau\downarrow0}L_\tau=r c_T.
\]

In particular, if \(c_T>0\), then for all sufficiently small positive \(\tau\),

\[
L_\tau>c_{T-\tau}>D_{T-\tau}.
\]

Thus genuine adaptation improves on all deterministic profiles for sufficiently small lag. This is an existence statement, not a computed lag cutoff.

## 10. Strict feasibility, uniform margins, and nonattainment

Define strict pointwise feasibility by

\[
\mathbb E\|z(w)\|_T
<
\gamma\,\mathbb E\|w\|_T
\quad\text{for every nonzero admissible }w.
\]

For the actual gain \(L_\tau\):

- If \(\gamma>L_\tau\), strict pointwise feasibility holds.
- If \(\gamma<L_\tau\), it fails.
- If \(\gamma=L_\tau\), it holds **if and only if** the actual supremum is not attained.
- A uniform positive margin holds **if and only if** \(\gamma>L_\tau\).

The proved specializations are:

1. **Zero-output cases:** \(L_\tau=0\), every nonzero ratio equals zero, and strict feasibility holds exactly when \(\gamma>0\). It fails at \(\gamma=0\).

2. **General nonzero positive-lag case:**
   \[
   \sqrt{2/\pi}\,c_H<L_\tau\le r c_H.
   \]
   Therefore \(\gamma\le\sqrt{2/\pi}\,c_H\) fails. The endpoint \(\gamma=r c_H\) is pointwise strictly feasible by Proposition 2. A uniform margin at that endpoint is not established in general.

3. **Long-lag nonzero case:**
   \[
   L_\tau=D_H<c_H.
   \]
   In particular, \(\gamma=c_H\), and hence \(\gamma=r c_H\), has a uniform positive margin.

4. **Actual critical endpoint in the long-lag case:** feasibility at \(\gamma=D_H\) reduces to whether a maximizing measure for \(J\) is represented by an actual deterministic L2 energy profile. Random adapted profiles cannot create attainment unless such a deterministic profile exists: an attaining random input would have to attain the conditional deterministic bound on its nonzero paths and have no wasted input-tail energy.

That last optimizer-representation question is not settled here. Accordingly, **nonattainment of the actual positive-lag gain remains unpaid**, including in the long-lag regime.

For distinction only: the E2 **RMS** gain is exactly \(c_H\), by Itô isometry and deterministic narrow bursts. Its positive-value supremum is not attained because \(G(H-s)\prec c_H^2I\) for \(s>0\). This does not determine the literal gain above.

## 11. Relation to the original source and controller synthesis

The frozen S3 parent observation records that the inspected source pages display a stochastic plant, regulated output, controller arguments, and the strict expected-path-norm ratio. It also records that the full filtration, initial/history, and universal-disturbance conventions are not explicitly supplied in those inspected pages.

The present theorem concerns exactly the **given law**

\[
dx_t=Px_t\,dt+B w_{t-\tau}\,dW_t,\qquad z_t=Cx_t,
\]

under the explicit zero-history and filtration assumptions in §2. The packet does not display enough coefficient-level plant/controller equations to establish that this law is the original source’s general controlled system or an equivalent closed loop.

No controller has been constructed. No claim is made about general state noise, multiple Brownian drivers, feedthrough, a disturbance-preview synthesis problem, or the infinite horizon. Therefore this is a **conditional given-law result**, not closure of the printed controller-synthesis problem.

## 12. Precisely unpaid steps

The remaining obligations are:

1. Evaluate the actual adapted gain for \(0<\tau<T/2\), beyond the proved bounds and causal lower family.
2. Evaluate the compact deterministic optimization \(D_H\), rather than merely characterize it.
3. Determine whether its maximizing covariance measures are representable by actual L2 profiles; this controls attainment and the strict critical endpoint in the long-lag case.
4. Determine attainment and the critical strict endpoint for the general short-lag adapted problem.
5. Supply an actual controller-synthesis formulation and solution, with a coefficient-level source match and explicit information/history assumptions.
6. Obtain a disjoint mathematical check and parent disposition of this candidate.

**Evidence boundary:** The \(r\)-weighted inequality and zero-lag exact gain enter only through frozen S1/S2. S3 supplies only its stated page-limited source observation. No new public-source, novelty, current-openness, independent-family, human, formal/kernel, or scientific-execution credit is claimed.