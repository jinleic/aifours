# f419 WRITTEN review — complete return

**Disposition: RETURN FOR ONE ADDITIVE CORRECTION — 0 FATAL / 1 MAJOR / 0 MINOR.**

The calibration identities, quantitative positive penalty, active-core endpoint comparison and actual-edge right derivative are supported at the conditional scope specified below. One additional assertion is false: the coupling-penalty difference has a universal nonpositive sign, rather than an undetermined sign.

## Scope, inputs and process

The reviewed candidate is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f400-privacy-cutoff2-scalar-uniqueness-original-frontier/review-v1.md`

All source-line references below use the packet’s **S1–S4 source LF labels**, not packet-display line numbers.

I read the complete manifest, freeze receipt, dispatch receipt, parent metadata and all seven status-only controls before sending the administrative pre-body ACK. I then read the entire literal packet in ordered raw windows of at most 20 LF: packet LF 1–940 in consecutive 20-line windows, followed by 941–955. This included S1 through its LF 698 ending, S2 through LF 49, S3 through LF 38 and S4 through LF 168. Focused rereads followed the complete read. The independent-snapshot-review skill was also read as administrative guidance, after the packet and before derivation; no external-model review was launched.

The following are **parent-attributed metadata**, not child-executed hashes or a child-native start/completion clock:

- Manifest SHA256: `334d4aee75420d44576e1f23085998e59f51a03f851a9192c56c8ea71a1b4ac6`.
- Freeze-receipt SHA256: `011056abcbf3e93aa0923bd06e3a5cd6d6359e6478e83aa71ee7b7873e888332`.
- Packet SHA256: `6aea55ed41918188eee3a3b2fc1d92ff4234e4a391fdd0b85083d1ee4b575ebd`.
- Parent observation: `2026-10-30T10:56:06-0700 PDT`.

The private auxiliary privacy episode and every consumer, PHv8/cp116, AMEt28 and the other held episodes were **NONINPUT**. No excluded links, sibling returns, author code or external scientific sources were opened. No selected mathematical instance, scientific executable, CAS, solver, enumeration or replay was used. A read-only `git diff` restricted to the candidate path returned no output; the scientific review is bound to the frozen packet, not to an inferred Git change history.

No repository review file was written under this read-only role. This is the full body for parent materialization.

## Findings

### M1 — State the endpoint coupling-penalty difference as nonpositive

**Priority:** 2  
**Confidence:** 0.98  
**File:** `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f400-privacy-cutoff2-scalar-uniqueness-original-frontier/review-v1.md`  
**Line start–end:** 498–498

For the stated ordering \(c\ge u\), the defined penalty satisfies \(P(a,c;\lambda)\le P(a,u;\lambda)\) for every fixed admissible \(a,b,\lambda\), so its difference cannot have both signs. Raising \(d\) increases the independent tail clip \(q_d\), while every coupling threshold is below the tail upper bound; consequently the conditional excess tail cost, and then its minimum over the unchanged first-core box, are nonincreasing in \(d\). The corner excess is nonincreasing for the same reason. Replace the “need not have a fixed sign” assertion by \(P(a,c;\lambda)-P(a,u;\lambda)\le0\), while retaining the separate, correct qualification that this alone does not determine the sign of the full endpoint difference or establish edge dominance. A complete all-variable proof appears in §4 below.

This does not invalidate equations (5.4), (5.7), (6.2), or the conditional shared-core-slack exclusion. It requires correction before accepting the complete endpoint-sign discussion.

## 1. Exact imports and quantified boundary

I use the following imports only at their frozen scopes:

1. **S4 LF 43–53, 75–111:** the full \(N=2\) functional, corrected pointwise minimization, canonical feasibility, unique fixed-scalar value zero \(\rho\), and attained conditional reduction
   \[
   V=\min_{a\ge0,\ c\ge a+1/2}\rho(a,c).
   \]
   This is not the rejected unrestricted two-equation P3 characterization.

2. **S4 LF 95:** actual-optimizer positivity \(a>0\) and the pruning consequence \(c<a+1\), retaining the full standing hypothesis
   \[
   \frac12<V\le2.
   \]

3. **S2 LF 21–41:** exact both-endpoint bookkeeping and the old edge derivative **only on its declared all-upper-face stratum**.

4. **S3 LF 7–30:** necessary normal-cone conditions, with one common Clarke subgradient and the stated compatible-extension or relative-convention qualification. No exact Clarke implicit or integral-selection equality is imported.

5. **S1 §3:** the proposed active-core theorem supplies, **conditionally for this disjoint gate**,
   \[
   V<Q_*:=v+(1+m)^2,
   \qquad r(y)<1.
   \]
   Its competitor and polynomial-certificate proof is not independently certified by this §§4–6 review. Acceptance of that import remains a separate gate.

Thus the actual-optimizer conclusions below quantify over every \(b\in(0,1)\) **for which the assumed actual regime and optimizer exist**. They do not establish that such a regime occurs.

The general independent-box identities in §5 of the candidate have a wider algebraic scope: fixed \(b\in(0,1)\), \(a\ge0\), \(d\ge u=a+1/2\), and fixed finite \(\lambda\), using the displayed clipped-root convention. They do not require \(d\) to be an optimizer.

## 2. Cubic identity, weights and full calibration — SUPPORTED

### 2.1 Exact cubic remainder

Write \(g_y(t)=\psi_1(t,y;\lambda)\). Its coordinate-dependent terms are
\[
g_y(t)=\frac{t^3}{3}+mt^2+(y^2-\lambda+T_2)t+\text{constant in }t,
\]
and
\[
g_y'(s)=s^2+2ms+y^2-\lambda+T_2
       =d_1(s,y),
\]
because \(T_2=m^2+v\).

Setting \(\Delta=t-s\), direct symbolic expansion gives
\[
g_y(t)-g_y(s)
=d_1(s,y)\Delta+(s+m)\Delta^2+\frac{\Delta^3}{3}.
\]
Equivalently,
\[
g_y(t)-g_y(s)
=d_1(s,y)(t-s)
 +(t-s)^2\left(\frac{t+2s}{3}+m\right)
=\mathcal B_y(t,s).
\]

This verifies **S1 LF 335–347** exactly. There is no missing factor in the remainder.

If \(s\) minimizes \(g_y\) over an interval containing \(t\), the first-order variational inequality gives
\[
d_1(s,y)(t-s)\ge0.
\]
For \(t,s\ge0\),
\[
\frac{t+2s}{3}+m\ge m>0.
\]
Therefore \(\mathcal B_y(t,s)\ge0\), with equality exactly when \(t=s\). This covers lower faces, upper faces, stationary-root ties and singleton boxes.

The analogous expansion
\[
\psi_0(t,y)-\psi_0(s,y)
=d_0(s,y)(t-s)+(t-s)^2\frac{t+2s}{3}
\]
also holds. Although its quadratic coefficient has no added \(m\), it is strictly positive whenever \(t,s\ge0\) and \(t\ne s\). Hence no fixed-profile nonuniqueness exception appears at a tie.

### 2.2 Why the pooled-core coefficient is \(8\), not \(8b\)

For fixed height, define
\[
W_y(x)=(1-b)\psi_0(x,y)+b\psi_1(x+1,y).
\]
The imported pooled identity gives
\[
W_y'(x)=d_1(x,y).
\]
Consequently
\[
W_y(x)-W_y(f_a)=\mathcal B_y(x,f_a),
\]
without an additional factor \(b\).

For \(F_1=x+1+D\),
\[
\psi_1(x+1+D,y)-\psi_1(x+1,y)
=d_1(x+1,y)D+(x+1+m)D^2+\frac{D^3}{3}.
\]
This is precisely \(\Gamma_y(x,D)\).

Thus:

- the pooled first-core difference has weight \(8\);
- the additional shared-core slack cost has weight \(8b\);
- corner and far-tail differences each have weight \(8b\).

These are the weights in (4.5), **S1 LF 387–400**.

### 2.3 Feasibility, blocks and constants

Under the conditional active-core bounds, fix
\[
a>0,\qquad u\le d<a+1,\qquad \lambda=V<Q_*.
\]
For any first-core coordinate \(x\in[a,2a-y]\),
\[
d<a+1\le x+1\le2a+1-y\le2d-y.
\]
Since \(d_1(z,y)>0\) for \(z\ge1\), the tail’s conditional minimum is \(z=x+1\). Minimizing \(W_y\) then gives \(f_a\).

The remaining blocks are exactly:

- shared core: \(0\le y\le a\);
- corner: \(a\le y\le u\), with bounds \([\max(d,2u-y),2d-y]\);
- far tail: \(u\le y\le d\), with bounds \([d,2d-y]\).

On a selected root branch, the derivative is \(-y/(r+m)\). In the pooled core the selected coordinate is at least \(a\ge y\); in either tail block it is at least \(d\ge y\). Constant and upper-face branches have slopes \(0\) and \(-1\). The joins are continuous: at \(a\) both profiles give the tail value \(a+1\), at \(u\) the effective corner floor becomes \(d\), and at \(d\) the tail box collapses to \(d\). Thus the pointwise minimizers are canonical profiles, not merely unconstrained pointwise selections.

Subtracting the two full functionals at the **same** \(d\) cancels exactly the common term \(bC(d;V)\). The result is
\[
\begin{aligned}
H_V(F_0,F_1;a,d)-h(a,d;V)
={}&8\int_0^a\mathcal B_y(x,f_a)\,dy\\
&+8b\int_0^a\Gamma_y(x,D)\,dy\\
&+8b\int_a^u\mathcal B_y(F_1,\phi_d)\,dy\\
&+8b\int_u^d\mathcal B_y(F_1,p_d)\,dy.
\end{aligned}
\]
Every range and weight in (4.5) is correct. At \(d=u\) the last interval has zero length; the corner interval does not disappear.

### 2.4 Strictness and the exact slack lower bound

Put \(\delta=Q_*-V>0\). For \(x\ge a>0\),
\[
d_1(x+1,y)\ge d_1(1,y)=\delta+y^2.
\]
Therefore, for \(D\ge0\),
\[
\Gamma_y(x,D)\ge\delta D.
\]
All other calibration terms are nonnegative, so
\[
H_V-h(a,d;V)
\ge8b\delta\int_0^a(F_1-F_0-1)\,dy.
\]

Equality in the full calibration requires the selected coordinate in every positive-length block and \(D=0\) throughout the shared core. Continuity extends almost-everywhere equality to the canonical profiles themselves. Strict slack at even a shared endpoint has a positive-length one-sided neighborhood of positive slack, because \(a>0\). It therefore makes the displayed integral strictly positive.

At an actual minimizing scalar pair, \(h(a,c;V)=0\) and \(Z>0\), so such a profile has ratio strictly larger than \(V\). This is a valid conditional exclusion of **all** shared-core slack, including face branches. No scalar stationarity or sufficiency assertion is used.

## 3. Independent-box penalty and both-endpoint subtraction — SUPPORTED

The corrected two-line core rule in **S1 LF 423–438** has the proper scope. If the independent pair is infeasible, \(q_d<p_0+1\), then
\[
d-1<p_0\le2a-y,
\]
so the active interval is nonempty. The rule requires only this implication, not its converse.

The independent-box minimizers \(p_0,q_d\) minimize their respective integrands on the same boxes containing \(x_d,z_d\). Likewise, \(\phi_d\) and \(q_d\) lie in the same tail box in the corner. Their normal terms are consequently nonnegative. This proves \(P\ge0\) in (5.2), with all three components retained.

Direct subtraction of the full functional gives
\[
h(a,d;\lambda)=h_{\rm ind}(a,d;\lambda)+P(a,d;\lambda).
\]
At fixed \(a,\lambda\), the first-core term of \(h_{\rm ind}\) is independent of \(d\). Splitting the tail integral at \(u\) yields exactly
\[
\begin{aligned}
h(a,c;\lambda)-h(a,u;\lambda)
={}&b[C(c;\lambda)-C(u;\lambda)]\\
&+8b\int_u^c\psi_1(q_c,y;\lambda)\,dy\\
&+8b\int_0^u[\psi_1(q_c,y;\lambda)-\psi_1(q_u,y;\lambda)]\,dy\\
&+P(a,c;\lambda)-P(a,u;\lambda).
\end{aligned}
\]

Expanding the last difference produces precisely:

- \(8(1-b)\) times the first-core difference on \([0,a]\);
- \(8b\) times the **two-endpoint** tail-core correction on \([0,a]\);
- \(8b\) times the **two-endpoint** corner correction on \([a,u]\).

The deterministic difference \(b[C(c)-C(u)]\) remains. No tail-core correction is lost by treating only one endpoint. Equation (5.4) is correct.

## 4. Complete proof of the sign correction — REFUTES S1 LF 498

This proof is all-variable; it uses no selected instance.

Fix \(a,b,\lambda\) and a height \(y\in[0,u]\). Let
\[
U_d=2d-y,\qquad q_d=\operatorname{clip}(r(y),[d,U_d]).
\]
Both box endpoints increase with \(d\), so \(q_d\) is nondecreasing in \(d\). The function \(g_y=\psi_1(\,\cdot\,,y;\lambda)\) is nondecreasing on \([r(y),\infty)\), including when its nonnegative minimizer is \(r(y)=0\).

For a fixed threshold \(t\le U_d\), define the conditional excess
\[
E_d(t)=g_y(\max(q_d,t))-g_y(q_d).
\]

For two ordered parameters \(d_1\le d_2\), with the threshold admissible at both:

- If \(q_{d_1}\ge t\), then \(q_{d_2}\ge t\), and both excesses are zero.
- If \(q_{d_1}<t\), then \(q_{d_1}<U_{d_1}\), so it is not an upper-face projection. Hence
  \[
  q_{d_1}=\max(d_1,r(y))\ge r(y).
  \]
  Increasing \(q_d\) toward \(t\) increases \(g_y(q_d)\) and decreases \(g_y(t)-g_y(q_d)\); after \(q_d\) reaches \(t\), the excess is zero.

Thus \(E_d(t)\) is nonincreasing in \(d\).

For a shared-core height, put \(A=2a-y\). Since \(d\ge u\),
\[
U_d\ge A+1.
\]
Every threshold \(x+1\), \(x\in[a,A]\), is therefore admissible. Conditional minimization over the tail gives \(z=\max(q_d,x+1)\). The pointwise core penalty is consequently
\[
\kappa_d(y)=
\min_{x\in[a,A]}
\left\{
(1-b)[\psi_0(x,y)-\psi_0(p_0,y)]
+bE_d(x+1)
\right\}.
\]
For every fixed \(x\), the expression is nonincreasing in \(d\). Its minimum over the unchanged box is also nonincreasing.

For a corner height, take \(t=2u-y\). Again \(t\le U_d\), and
\[
\phi_d=\max(q_d,t).
\]
The pointwise corner penalty is exactly \(E_d(t)\), also nonincreasing.

The corrected fixed-height minimizers are canonical by the imported reduction, so these pointwise penalties integrate to the \(P\) actually defined in (5.2):
\[
P(a,d;\lambda)
=8\int_0^a\kappa_d(y)\,dy
 +8b\int_a^u E_d(2u-y)\,dy.
\]
Therefore
\[
\boxed{P(a,c;\lambda)-P(a,u;\lambda)\le0\qquad(c\ge u).}
\]

This proof includes clipping, ties, singleton first-core boxes at \(a=0\), and arbitrary finite fixed \(\lambda\) under the displayed root convention. It does not require the actual regime or an optimizer.

The correction does **not** determine the sign of the other terms in (5.4). Global edge dominance remains unproved.

## 5. Quantitative positive penalty and active-core comparison — SUPPORTED

### 5.1 Both penalties are strictly positive

At an actual pair, the conditional imports give \(a>0\), \(c<a+1\) and \(r(0)<1\). For each \(d\in\{c,u\}\),
\[
q_d(y)\le\max(d,r(0)),
\qquad
\varepsilon_d=a+1-\max(d,r(0))>0.
\]
The actual clipped joint core satisfies
\[
z_d=f_a+1\ge a+1,
\]
hence
\[
z_d-q_d\ge\varepsilon_d.
\]

Because \(q_d\) minimizes the independent tail integrand on its box and \(z_d\) belongs to that box,
\[
\mathcal B_y(z_d,q_d)
\ge m(z_d-q_d)^2
\ge m\varepsilon_d^2.
\]
Retaining just this nonnegative part of (5.2) gives
\[
\boxed{P(a,d;V)\ge8bam\varepsilon_d^2>0,\qquad d=c,u.}
\]

The clipping bound is valid whether \(q_d\) selects its lower face, root or upper face. No claim that \((a,u)\) itself is an optimizing pair is needed. Its penalty is positive because the same \(a,V\) satisfy the conditional strip bounds.

There is no circular existence argument: this statement begins with an actual optimizer as a hypothesis. It does not construct one.

### 5.2 Coupled-core cancellation is different from independent slack

For \(d=c,u\), the coupled core is the same pair \((f_a,f_a+1)\), so its complete weighted contribution cancels in subtraction. At \(d=u\), the corner box is the singleton \(2u-y\), and the far-tail interval is empty. Therefore
\[
\begin{aligned}
\frac{h(a,c;V)-h(a,u;V)}b
={}&C(c;V)-C(u;V)\\
&+8\int_a^u
[\psi_1(\phi_c,y;V)-\psi_1(2u-y,y;V)]\,dy\\
&+8\int_u^c\psi_1(p_c,y;V)\,dy.
\end{aligned}
\]
This verifies (5.7).

The two positive independent-box penalties are **not** being set to zero. Their bookkeeping combines with the independent tail-core difference to give the identical **coupled** core cancellation. The manuscript distinguishes these mechanisms correctly.

## 6. Clip frontiers, normals and actual-edge derivative — SUPPORTED

### 6.1 Clips and necessary conditions

The integrand derivative
\[
d_1(t,y)=(t+m)^2+v+y^2-V
\]
is strictly increasing on \(t\ge0\). Its signs at the actual lower and upper bounds give exactly the lower/root/upper classification (6.1). At equality the adjacent formulas select the same coordinate. A singleton interval remains a singleton regardless of derivative sign.

The scalar conditions quoted in §6.1 agree with S3:

- positive-\(a\) interior: \(h_a=h_c=0\);
- positive-\(a\) edge: \(h_a+h_c=0,\ h_c\ge0\);
- vertex: \(h_a+h_c\ge0,\ h_c\ge0\);
- \(a=0,c>1/2\): \(h_c=0,\ h_a\ge0\).

At a kink, these remain a necessary inclusion using **one common** \(g\in\partial_C h\), under the imported subdifferential convention. They are not sufficiency conditions, exact interchange formulas or a replacement for scalar comparison.

### 6.2 Derivative with all contributions retained

Fix an actual positive-\(a\) edge and differentiate in \(c\) while holding \(a,b,V\) fixed. Thus \(u=a+1/2\) is fixed during this derivative.

For sufficiently small right increments, \(c<a+1\), so the coupled core remains independent of \(c\).

The deterministic derivative is
\[
C'(u;V)=8uT_2+\frac{16}{3}T_3-8mV.
\]

For the newly added interval \([u,c]\), the clipped coordinate lies between \(c\) and \(2c-y\), so it converges uniformly to \(u\) as the interval collapses. Its derivative contribution is
\[
8\psi_1(u,u;V)=8uT_2+16mu^2.
\]
The cubic and \(V\)-terms cancel exactly at this diagonal endpoint.

For a fixed \(y\in(a,u)\), put \(k=2u-y\). At \(c=u\), the corner box is \([k,k]\). For sufficiently small right increments its lower floor remains \(k\), and its upper endpoint moves at speed two. Therefore its optimized cost derivative is
\[
2\min\{0,d_1(k,y)\}.
\]
This includes the tie \(d_1(k,y)=0\), whose first-order contribution is zero.

To justify integration, for \(c=u+t\),
\[
k\le\phi_{u+t}(y)\le k+2t.
\]
On this finite interval and a fixed small parameter neighborhood, \(\psi_1\) has a bounded coordinate derivative. The cost difference quotient is therefore bounded uniformly in \(y,t\). Dominated convergence applies. The changing-floor layer near \(y=u\) is covered by the same bound; its endpoint value does not create an omitted positive-measure term.

Combining these contributions gives
\[
\boxed{
\begin{aligned}
\frac1b\partial_c^+h(a,u;V)
={}&16uT_2+16mu^2+\frac{16}{3}T_3-8mV\\
&+16\int_a^u
\min\{0,(2u-y+m)^2+v+y^2-V\}\,dy .
\end{aligned}}
\]
Thus (6.2), **S1 LF 614–646**, is supported. No exact Clarke differentiation is needed.

### 6.3 Comparison with f305 only on its own stratum

On f305’s stratum
\[
(E):\quad \lambda\ge v+(2u+m)^2,
\]
the independent tail selects its upper face throughout \([0,u]\). Its shared-core part then moves as well, so the face integral is over **\([0,u]\)**, not merely \([a,u]\). Direct integration gives
\[
\int_0^u d_1(2u-y,y)\,dy
=\frac83u^3+3mu^2+(T_2-\lambda)u.
\]
Adding sixteen times this integral to \(C'(u)+8\psi_1(u,u)\) yields
\[
\frac{16}{3}T_3+32uT_2+64mu^2
+\frac{128}{3}u^3-(16u+8m)\lambda,
\]
exactly S2 LF 37.

This is a separate stratum calculation. Under the conditional actual bounds \(a>0\) and \(V<Q_*\), stratum \((E)\) cannot hold, because
\[
v+(2u+m)^2>v+(1+m)^2=Q_*.
\]
The old expression therefore cannot be transplanted to the actual binding-core branch. The manuscript’s general formula correctly retains the corner minimum rule and excludes a spurious shared-core motion.

A negative actual-edge right derivative excludes a local minimum. A nonnegative derivative is only necessary; no uniform sign or global edge-uniqueness conclusion has been established.

## 7. Claimwise outcome and remaining gates

| Claim | Outcome |
|---|---|
| Cubic identities (4.1)–(4.2), including strict equality at ties | **SUPPORTED** |
| Full calibration (4.5), weights \(8,8b,8b,8b\), all block ranges and same-\(d\) constant cancellation | **SUPPORTED, conditional on the active-core imports** |
| Exact lower bound (4.6) and exclusion of continuous shared-core slack | **SUPPORTED at that conditional scope** |
| General corrected box rule, \(P\ge0\), and identities (5.3)–(5.4) | **SUPPORTED** |
| “\(P(c)-P(u)\) need not have a fixed sign” | **REFUTED — M1; it is nonpositive** |
| Quantitative bound (5.6), including positivity of both endpoint penalties | **SUPPORTED, conditional** |
| Active coupled-core comparison (5.7) | **SUPPORTED, conditional** |
| Clip ties and necessary scalar normals | **SUPPORTED at the imported necessary-condition scope** |
| Actual-edge derivative (6.2), moving endpoint, constants and bounded integration | **SUPPORTED, conditional** |
| Global sign of the full endpoint difference or actual-edge derivative | **INCONCLUSIVE / NOT PROVED** |
| Actual-regime existence, scalar-pair uniqueness, global value formula | **NOT PROVED** |

The candidate remains subject to separate parent disposition. This return supplies a same-harness written reconstruction of the assigned §§4–6 claims; it does not accept the §3 active-core import independently, establish original-target completion, or supply independent-family, human, formal/kernel, source-equivalence, priority or novelty assurance. No finite executable verification was performed.

**Overall correctness:** incorrect.

**Explanation:** The assigned calibration, endpoint identities and actual-edge derivative are supported at their explicit conditional scopes, but S1 LF 498 incorrectly leaves the coupling-penalty difference unsigned: it is always nonpositive for \(c\ge u\). An additive correction resolves this finding without establishing global edge dominance or scalar uniqueness.

**Confidence:** 0.97.