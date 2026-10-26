# Addendum v2 — the reverse separation also holds on an explicit finite horizon

Observed before creation: **2026-10-23T14:31:14-0700**, `/bin/date '+%Y-%m-%dT%H:%M:%S%z'`. Author: InfoHinfPreview. **CANDIDATE, pending separate and parent written checks.** No scientific execution.

Read with immutable `proof-reverse-feasibility-separation-v1.md`, SHA256 **33a3e60e43ef8e83f4351824fc708467728243a54846fda349350cabae10bb0f**, and its operative algebra-correction `proof-reverse-feasibility-separation-addendum-v1.md`, SHA256 **11922c3123990af68d812ab3d8a26dfe9449f6ee5868b3478986355ead1d36d8**. This addendum strengthens the horizon coverage; it does not alter the earlier bytes or pretend the extension was already asserted there.

## Exact additional theorem

For the **same** constant matrices, positive preview `h=2^-29`, effective `B=B0=(0,1)^T`, full-rank control penalty `r=2^43`, `epsilon=2^-29`, `kappa=2^28`, `g=16384`, `delta=1/2048` and `gamma=16386`, set

\[
 R=2^{14},\qquad T=R+8/\varepsilon=2^{14}+2^{32},
 \qquad L=T-h.
\]

On the literal finite horizon with output counted on `[0,T]` and input counted **exactly on `[0,T-h]=[0,L]`**:

* `u=0` has mean-square induced gain at most16384, strictly less than gamma, for **every adapted square-integrable disturbance** on the counted interval.
* Every well-posed nonanticipative adapted controller has printed induced gain **strictly greater than gamma**, including all controllers allowed to use the full preview window and pre-action.

Thus the reverse feasibility separation is not solely an infinite-horizon phenomenon.

## 1. Admissible finite-window test disturbance

Use the same Brownian exit time `tau=inf{t>=0:|W_t|=1}`, but truncate it at the actual counted input endpoint:

\[
 w^{(L)}_t=1_{\{0\le t<\tau\wedge L\}}.
\]

It is progressively measurable, supported on `[0,L]`, and

\[
 N_2(w^{(L)})^2=\mathbb E(\tau\wedge L)\le1,
 \qquad
 0<N_1(w^{(L)})=\mathbb E\sqrt{\tau\wedge L}
 \le\mathbb E\sqrt\tau<1-\delta.
\]

There is no input on the uncounted terminal preview interval `(T-h,T]`. The plant receives the actual delayed signal `w^(L)(t-h)`, whose support ends at or before `T`.

The mean-square upper bound follows immediately by extending this input by zero outside `[0,L]`, applying the infinite-horizon contraction/isometry estimate in the original proof, and discarding the nonnegative output energy after `T`. This proves a uniform bound at the correct finite-horizon denominator, not merely a bound for the one test signal.

## 2. The OU anchor loses only an explicit terminal tail

Let

\[
 M^{(L)}_t=W_{t\wedge\tau\wedge L},\qquad
 Z^{(L)}_t=\int_0^t e^{-\varepsilon(t-s)}w^{(L)}_s\,dW_s.
\]

On the event `tau<=R` (which lies inside the input window because `R<L`), the process has stopped at the genuine boundary, `|M^(L)_tau|=1`, and the same integration-by-parts argument gives

`|Z^(L)_tau|>=1-epsilon R=1-delta/16`.

After `tau` its diffusion forcing is zero. Its **counted** output energy on `[tau,T]` is exactly

\[
 |Z^{(L)}_\tau|^2\int_\tau^T e^{-2\varepsilon(t-\tau)}dt
 =g^2|Z^{(L)}_\tau|^2(1-e^{-2\varepsilon(T-\tau)}).
\]

Because `2epsilon(T-R)=16` and `e>2`,

`e^(-2epsilon(T-tau))<=e^-16<2^-16<delta/16`

on that event. Also `sqrt(1-x)>=1-x` for `0<=x<=1`. Hence

\[
 \begin{aligned}
 N_1(Z^{(L)};[0,T])
 &\ge g(1-\delta/16)(1-\delta/16)\mathbb P(\tau\le R)\\
 &\ge g(1-\delta/16)^2(1-\delta/8)\\
 &\ge g(1-\delta/4).
 \end{aligned}
\]

The last inequality follows by multiplying nonnegative factors: their three losses sum to `delta/16+delta/16+delta/8=delta/4`, and the product is at least one minus that sum. No infinite tail is being inserted into the finite output norm.

## 3. Positive-delay/filter and control errors remain uniformly bounded

The input `w^(L)` is again a single stopped step, of pathwise duration `tau wedge L`. Therefore the earlier exact low-pass calculation and delayed-interval symmetric-difference bound hold with that duration:

`integral_0^infinity |f^(L)-w^(L)(.-h)|^2 <=1/kappa`,

`integral_0^infinity |w^(L)(.-h)-w^(L)|^2 <=2h`.

Extend the zero-control response beyond `T` only as a **comparison estimate**. Itô isometry on the extended error and then restriction to the counted interval give

\[
 N_1(d^{(L)}-Z^{(L)};[0,T])
 \le g(\kappa^{-1/2}+\sqrt{2h})=g\delta/4.
\]

Together with the counted OU anchor this yields

\[
 N_1(d^{(L)};[0,T])\ge g(1-\delta/2)=16380.
\]

For an arbitrary actual control on `[0,T]`, extend its realized input by zero after `T` when estimating the **linear control-only map** `S`. This is not an extension of the feedback law, not an assumption of future control inactivity in the original problem, and not a controller reset. Causality ensures the extended control-only response agrees on `[0,T]`. The infinite-horizon bound thus implies

`N1(Su;[0,T])<=M N1(u;[0,T])`, `M<2^31`.

This also covers finite `N1(u)` with infinite second moment through the already stated energy-stop/Fatou extension. If the output norm is infinite the controller already fails; otherwise the `r*u` channel guarantees the required finite `N1(u)`.

Exactly the original triangle/Cauchy estimate now gives, entirely in the **counted finite** output norm,

\[
 {N_1(z;[0,T])\over N_1(w^{(L)};[0,L])}
 >g{1-\delta/2\over(1-\delta)(1+\delta/8)}
 >g(1+\delta/4)=16386.
\]

The final algebra is the corrected positive identity in additive v1. This excludes every controller, including time-varying horizon-aware laws and preview pre-action.

## Consequence and limits

The same rational plant therefore supplies reverse same-gamma **controller-existence** separations on both the infinite horizon and this explicitly stated finite horizon. Combined with the preserved earlier finite-horizon gamma6 example, the two objectives have no unqualified implication in **either direction even within the finite-horizon regime**. This last consequence compares two different plants/horizons; it does not claim one plant exhibits both directions at one level.

The original manuscript's statement that it did not prove a finite-horizon reverse example was accurate for that earlier snapshot and is superseded **only on this point** by the present additive proof. General prescribed-gamma N&S synthesis, exact optimal gains, novelty, formal verification and expert acceptance remain unresolved/unperformed. The large finite horizon is a mathematical certificate parameter, not an engineering recommendation.
