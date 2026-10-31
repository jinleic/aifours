# Uniform active-core theorem for the actual cutoff-two problem

**F400 author candidate v1 — UNREVIEWED.**

This manuscript proves a uniform exclusion of the **entire shared-core-slack optimizer branch, including box-face branches**. It does **not** prove scalar-pair uniqueness or a global value formula.

Complete manuscript supplied for parent materialization; session copy: `local://author-f400-privacy-cutoff2-candidate-v1.md`.

## 1. Frozen scope, actual reads, and methods

Assignment: `f400-privacy-cutoff2-scalar-uniqueness-original-frontier`.

Parent-supplied bindings:

- Manifest SHA256: `3e53845e8b344a5ae2a737d1b9dfca81406842eaabcd93074e84ad7aa50650f6`.
- Freeze-receipt SHA256: `f579c150316ce648320ee99ab59f31f9869bcd995311219650396982fc19ab25`.
- Literal-packet SHA256: `ab36689ba3fba09018df31a3c18ef6ba79333b6906fdaed0b997c3b81370a550`.

These are **parent-attributed metadata**, not independently executed child hashes. The supplied clock `2026-10-30T10:37:10-0700 PDT` belongs to the parent observation, not a child-native start or completion.

Actual read order: mandatory memory and relevant protocol skills; full manifest, receipt, parent metadata and dispatch receipt; all seven status/permission controls; input/method acknowledgement; then the complete ordered 273-LF scientific packet, displayed as LF 1–105, 106–190 and 191–273. Scientific reasoning began after that complete packet read. No linked held scientific body, held diagnostic payload, sibling current outcome or external scientific source was opened. Status-only controls were not mathematical premises. This reports actual access, not cognitive isolation.

All mathematics below was derived in writing. **No scientific executable, numerical search, CAS, random example, model CLI, build, lint or formatter was run.** The current bash role does not permit scientific execution or native clock/hash commands. Repository writes are unavailable through the supplied write tool; this full body is returned for parent materialization. There is no experiment code or numerical output to attribute.

The mathematical imports are exactly the frozen packet:

- **S2 and S4:** corrected fixed-scalar profile minimization and attained implicit variational reduction.
- **S4 LF 95:** actual-optimizer positivity and pruning consequences.
- **S1:** both-endpoint difference accounting, including the edge tail-core correction.
- **S3:** necessary normal-cone conditions only, using one common Clarke subgradient at a kink.

No rejected stationarity sufficiency or exact Clarke interchange is used.

## 2. Actual object and complete signed functional

Let
\[
0<b<1,\qquad m=\frac b{1-b}>0,\qquad v=m(1+m),
\]
and let \(G\) have distribution
\[
\Pr(G=j)=(1-b)b^j,\qquad j\ge0.
\]
Write \(T_k=\mathbb E G^k\). The needed moments are
\[
T_2=m+2m^2=m^2+v,
\]
\[
T_3=m+6m^2+6m^3,
\qquad
T_4=m+14m^2+36m^3+24m^4.
\]
Indeed, near zero,
\[
\mathbb E(1+t)^G=(1-mt)^{-1},
\]
so the \(k\)th factorial moment is \(k!m^k\); expanding ordinary powers gives these identities.

Retain the full actual-cutoff-two hypothesis:
\[
\frac12<V\le2.
\]

The scalar domain is
\[
K=\{(a,c):a\ge0,\ c\ge u:=a+\tfrac12\}.
\]
Canonical profiles satisfy
\[
a\le F_0(y)\le2a-y\qquad(0\le y\le a),
\]
\[
c\le F_1(y)\le2c-y\qquad(0\le y\le c),
\]
with the adopted continuous, nonincreasing, 1-Lipschitz conventions and coupling
\[
F_1(y)\ge F_0(y)+1\qquad(0\le y\le a),
\]
\[
F_1(y)\ge2a+1-y\qquad(a\le y\le u).
\]

For a profile \(F\) with diagonal parameter \(t\), put
\[
A(F)=8\int_0^t(F-y)\,dy,
\]
\[
Q(F)=8\int_0^t
\left(\frac{F^3}{3}+y^2F-\frac{4y^3}{3}\right)dy,
\qquad
B(F)=8\int_0^t(F^2+y^2)\,dy.
\]

The complete N=2 denominator and numerator are
\[
Z=(1-b)A(F_0)+b\{A(F_1)+8cm+2T_2\},
\]
\[
N=(1-b)Q(F_0)+b\left\{
Q(F_1)+mB(F_1)
+(A(F_1)+8c^2)T_2+\frac{16}{3}cT_3+\frac23T_4
\right\}.
\]
In particular,
\[
Z\ge2bT_2>0.
\]

These are the imported f273 tail formulas with every profile integral displayed. Directly, for diamond expansion radius \(r\), the sector profile is \(F(y)+r\) on \(0\le y\le t\), followed by \(2t+r-y\) on \(t\le y\le t+r/2\). Integration gives
\[
A(C+rD)=A(C)+8tr+2r^2,
\]
\[
Q(C+rD)=Q(C)+B(C)r+(A(C)+8t^2)r^2
+\frac{16}{3}tr^3+\frac23r^4.
\]
Thus the constants below include the complete tail and endpoint contributions.

Define
\[
\psi_0(x,y;\lambda)
=\frac{x^3}{3}+(y^2-\lambda)x-\frac{4y^3}{3}+\lambda y,
\]
\[
\psi_1(z,y;\lambda)
=\psi_0(z,y;\lambda)+m(z^2+y^2)+T_2z,
\]
\[
C(d;\lambda)
=4d^2T_2+\frac{16}{3}dT_3+\frac23T_4
-\lambda(8dm+2T_2).
\]

The full signed functional is exactly
\[
\boxed{
\begin{aligned}
H_\lambda(F_0,F_1;a,c)
&=N-\lambda Z\\
&=8(1-b)\int_0^a\psi_0(F_0,y;\lambda)\,dy\\
&\quad+8b\int_0^c\psi_1(F_1,y;\lambda)\,dy
+bC(c;\lambda).
\end{aligned}}
\tag{2.1}
\]

Its profile-coordinate derivatives are
\[
d_0(x,y)=x^2+y^2-\lambda,
\qquad
d_1(z,y)=(z+m)^2+v+y^2-\lambda.
\tag{2.2}
\]

An everywhere-defined clipped-root convention is
\[
r_0(y)=\sqrt{\max(\lambda-y^2,0)},
\]
\[
r(y)=\max\left\{0,\sqrt{\max(\lambda-v-y^2,0)}-m\right\}.
\tag{2.3}
\]
On nonnegative boxes these give the source projections, including when no nonnegative stationary root exists.

Let \(h(a,c;\lambda)\) be the minimum of \(H_\lambda\) over the adopted feasible profiles at those scalars. The frozen reduction supplies a unique zero \(\rho(a,c)\) and, under the actual-cutoff-two hypothesis,
\[
V=\min_{(a,c)\in K}\rho(a,c),
\tag{2.4}
\]
with attainment. Consequently, every feasible phase has \(H_V\ge0\), and every actual minimizing pair has
\[
h(a,c;V)=0.
\]

## 3. Uniform theorem: the entire shared-core-slack branch is absent

### Theorem

For **every** \(b\in(0,1)\) for which an actual-cutoff-two optimizer with \(1/2<V\le2\) exists, **every** such optimizer satisfies:

1. \(a>0\) and \(u\le c<a+1\).
2. With
   \[
   Q_*:=v+(1+m)^2=1+3m+2m^2,
   \]
   one has
   \[
   V<Q_*,
   \]
   hence \(r(y)<1\) for every \(y\ge0\).
3. Throughout the entire shared core,
   \[
   \boxed{
   F_0(y)=f_a(y):=\operatorname{clip}(r(y),[a,2a-y]),
   \qquad F_1(y)=f_a(y)+1
   \quad(0\le y\le a).
   }
   \tag{3.1}
   \]
4. No optimizer belongs to any branch with \(F_1>F_0+1\) at even one shared height. This excludes box-face slack as well as free-free slack. Neither \(S_{\rm pair}\) nor \(S_{\rm both}\) from S1 contains an actual optimizer.

This conclusion is uniform over all actual parameters and all remaining scalar edge/interior and clipping/kink patterns.

### Proof, step 1: actual scalar corridor

The positivity \(a>0\) is an explicit frozen actual-optimizer import, not inferred from stationarity.

At the edge \(c=u\), clearly \(c<a+1\). If \(c>u\), its diagonal endpoint \((c,c)\) lies outside \(C_0+D\). The imported pruning inclusion
\[
C_1\subset(C_0+D)\cup\overline B(\sqrt V)
\]
therefore gives
\[
2c^2\le V\le2.
\]
Thus \(c\le1<a+1\). Every actual minimizing pair lies in
\[
a>0,\qquad u\le c<a+1.
\]

### Proof, step 2: complete feasible comparison

Use the feasible scalar vertex
\[
(a,c)=(0,\tfrac12),\qquad C_0=\{0\},\quad C_1=D.
\]
Its first core has zero area. Its complete tail consists of diamonds \((G+1)D\), with the required outer weight \(b\).

A radius-\(s\) diamond has area \(2s^2\) and moment \(2s^4/3\). Moreover,
\[
b\,\mathbb E(G+1)^k=T_k\qquad(k>0).
\]
Therefore this competitor has
\[
Z_\diamond=2T_2,\qquad
N_\diamond=\frac23T_4,\qquad
J_\diamond=\frac{T_4}{3T_2}.
\tag{3.2}
\]
In signed form, with all constants included,
\[
\boxed{
H_\lambda(\{0\},D;0,\tfrac12)
=\frac23T_4-2\lambda T_2
=2T_2(J_\diamond-\lambda).
}
\tag{3.3}
\]

This degenerate-prefix phase is an allowed competitor in (2.4). It is not asserted to be an actual optimizer or to have a genuine two-prefix cutoff. Hence
\[
V\le J_\diamond,\qquad V\le2.
\]

The strict comparison
\[
\min\{2,J_\diamond\}<Q_*
\]
has an exact positive certificate on the entire half-line \(m>0\). Put \(t=2/7\). For \(0<m\le t\),
\[
Q_*-J_\diamond
=\frac{2+m-12m^2-12m^3}{3(1+2m)},
\]
and
\[
\boxed{
2+m-12m^2-12m^3
=\frac{352}{343}
+(t-m)\left(12m^2+\frac{108}{7}m+\frac{167}{49}\right)>0.
}
\tag{3.4}
\]
For \(m\ge t\),
\[
\boxed{
Q_*-2
=\frac1{49}+(m-t)\left(2m+\frac{25}{7}\right)>0.
}
\tag{3.5}
\]

Both are literal polynomial identities. Thus \(V<Q_*\) for every \(m>0\). Equivalently, \(V\ge Q_*\) either contradicts \(V\le2\) through (3.5), or makes the complete feasible signed value (3.3) strictly negative through (3.4), contradicting global minimality.

This comparison includes the zero first-core term, entire geometric tail, outer weight and normalization—not merely a corner threshold.

Set
\[
\delta:=Q_*-V>0.
\tag{3.6}
\]
For every \(z\ge1\),
\[
d_1(z,y)\ge d_1(1,y)=\delta+y^2>0.
\tag{3.7}
\]
The bound \(r(y)<1\) follows from (2.3).

### Proof, step 3: box-face and free shared-core slack are excluded

Fix an actual scalar pair and shared height. Any feasible core coordinate \(x\) satisfies \(x\ge a\), so
\[
c<a+1\le x+1.
\]
Also,
\[
x+1\le2a+1-y\le2c-y.
\]
Thus its smallest feasible tail coordinate is exactly \(x+1\). By (3.7), the tail integrand is strictly increasing for
\[
z\ge x+1>1.
\]
Its unique conditional minimum is therefore \(z=x+1\), without a free-root or box-face exception.

On this active line, the adopted pooled identity gives
\[
\begin{aligned}
\frac{d}{dx}\{(1-b)\psi_0(x,y)+b\psi_1(x+1,y)\}
&=(1-b)d_0(x,y)+bd_1(x+1,y)\\
&=d_1(x,y).
\end{aligned}
\tag{3.8}
\]
The second derivative is \(2(x+m)>0\). Projecting its nonnegative root onto \([a,2a-y]\) gives (3.1).

These profiles are canonically feasible, not merely pointwise minimizers. On a selected root branch,
\[
r'=-\frac{y}{r+m},
\]
and \(r\ge a\ge y\) in the first core, so the slope lies in \([-1,0]\). Constant and upper-face branches have slopes \(0\) and \(-1\). The tail clips below join continuously at \(a,u,c\) and have the same slope bounds. At \(a\), \(f_a(a)=a\) and the corner floor equals \(a+1\); at \(u\), the additional corner floor is no larger than \(c\).

The next section proves strictness uniformly, including all ties. ∎

## 4. Exact nonnegative calibration over every core and tail block

For \(s,t\ge0\), define
\[
\mathcal B_y(t,s)
=d_1(s,y)(t-s)
+(t-s)^2\left(\frac{t+2s}{3}+m\right).
\tag{4.1}
\]
The cubic identity
\[
\psi_1(t,y)-\psi_1(s,y)=\mathcal B_y(t,s)
\tag{4.2}
\]
is exact.

If \(s\) minimizes the integrand on the same interval containing \(t\), its normal term
\[
d_1(s,y)(t-s)
\]
is nonnegative. Hence \(\mathcal B_y(t,s)\ge0\), with equality only for \(t=s\), including lower faces, upper faces and root ties.

Fix
\[
a>0,\qquad u\le d<a+1,\qquad \lambda=V<Q_*.
\]
Define
\[
L_d(y)=\max(d,2u-y),\qquad U_d(y)=2d-y,
\]
\[
\phi_d(y)=\operatorname{clip}(r(y),[L_d(y),U_d(y)])
\qquad(a\le y\le u),
\]
\[
p_d(y)=\operatorname{clip}(r(y),[d,2d-y])
\qquad(u\le y\le d).
\tag{4.3}
\]
The corrected minimizer is \((f_a,f_a+1)\) in the shared core, \(\phi_d\) in the corner block and \(p_d\) in the far tail.

For any other feasible canonical profiles at these scalars, write
\[
x(y)=F_0(y),\qquad
D(y)=F_1(y)-F_0(y)-1\ge0
\qquad(0\le y\le a),
\]
and put
\[
\Gamma_y(x,D)
=d_1(x+1,y)D+(x+1+m)D^2+\frac{D^3}{3}.
\tag{4.4}
\]

The complete calibration is
\[
\boxed{
\begin{aligned}
H_V(F_0,F_1;a,d)-h(a,d;V)
={}&8\int_0^a\mathcal B_y(x,f_a)\,dy\\
&+8b\int_0^a\Gamma_y(x,D)\,dy\\
&+8b\int_a^u\mathcal B_y(F_1,\phi_d)\,dy\\
&+8b\int_u^d\mathcal B_y(F_1,p_d)\,dy.
\end{aligned}}
\tag{4.5}
\]

To verify its first two terms, replace \(F_1=x+1+D\) by \(x+1\). The exact cost difference is \(b\Gamma_y(x,D)\) by cubic expansion. The remaining weighted core difference equals \(\mathcal B_y(x,f_a)\) by (3.8). The corner and far-tail terms follow directly from (4.2). Equation (2.1) has the same deterministic term \(bC(d;V)\) on both sides: it cancels exactly rather than being omitted. Every block has its actual integration limits.

Every term in (4.5) is nonnegative. Moreover, (3.7) yields
\[
\boxed{
H_V(F_0,F_1;a,d)-h(a,d;V)
\ge8b\delta\int_0^a(F_1-F_0-1)\,dy.
}
\tag{4.6}
\]

Equality in (4.5) holds exactly for the corrected profiles in every block. Since canonical profiles are continuous and \(a>0\), strict shared-core slack at any height gives a strictly positive integral in (4.6). At an actual minimizing pair \(h=0\), so
\[
N-VZ>0,
\]
and, because \(Z>0\), the ratio is strictly larger than \(V\).

Thus (4.5)–(4.6) exclude the entire shared-core-slack optimizer branch, not merely a stationary free-free configuration. They apply separately at **both endpoints** \(d=c\) and \(d=u\), including collapse of the last interval at \(d=u\).

## 5. Exact comparison of both scalar endpoints

The following general identity precedes the active-core restriction and records every correction.

For arbitrary \(a\ge0,d\ge u\), let
\[
p_0(y)=\operatorname{clip}(r_0(y),[a,2a-y]),
\qquad
q_d(y)=\operatorname{clip}(r(y),[d,2d-y]).
\]
Let \((x_d,z_d)\) be the corrected joint core minimizer. Explicitly:

- If \(q_d\ge p_0+1\), it is \((p_0,q_d)\).
- Otherwise,
  \[
  x_d=\operatorname{clip}(r,[\max(a,d-1),2a-y]),
  \qquad z_d=x_d+1.
  \]

The active interval is nonempty whenever the independent feasibility test fails; no converse is asserted. The corner minimizer is \(\phi_d\) from (4.3), and the far-tail minimizer is \(q_d\).

Define
\[
\begin{aligned}
\mathcal B_y^0(t,s)
&=d_0(s,y)(t-s)+(t-s)^2\frac{t+2s}{3}\\
&=\psi_0(t,y)-\psi_0(s,y).
\end{aligned}
\tag{5.1}
\]
The independent-box value is
\[
\begin{aligned}
h_{\rm ind}(a,d;\lambda)
={}&8(1-b)\int_0^a\psi_0(p_0,y)\,dy\\
&+8b\int_0^d\psi_1(q_d,y)\,dy+bC(d;\lambda).
\end{aligned}
\]
Its complete coupling penalty is
\[
\boxed{
\begin{aligned}
P(a,d;\lambda)
={}&8\int_0^a\left\{
(1-b)\mathcal B_y^0(x_d,p_0)
+b\mathcal B_y(z_d,q_d)
\right\}dy\\
&+8b\int_a^u\mathcal B_y(\phi_d,q_d)\,dy
\ \ge0.
\end{aligned}}
\tag{5.2}
\]
All roots and derivatives here use this section’s displayed \(\lambda\). Each normal term is nonnegative because its comparison point minimizes the independent box. Strict convexity handles root/face ties.

Direct substitution into (2.1) gives
\[
h(a,d;\lambda)=h_{\rm ind}(a,d;\lambda)+P(a,d;\lambda).
\tag{5.3}
\]
Therefore,
\[
\boxed{
\begin{aligned}
h(a,c;\lambda)-h(a,u;\lambda)
={}&b\{C(c;\lambda)-C(u;\lambda)\}\\
&+8b\int_u^c\psi_1(q_c,y;\lambda)\,dy\\
&+8b\int_0^u
[\psi_1(q_c,y;\lambda)-\psi_1(q_u,y;\lambda)]\,dy\\
&+P(a,c;\lambda)-P(a,u;\lambda).
\end{aligned}}
\tag{5.4}
\]

Expanding the last line gives exactly the three f305 corrections:

- C0 difference, weight \(8(1-b)\), range \([0,a]\);
- tail-core difference, weight \(8b\), range \([0,a]\);
- corner difference, weight \(8b\), range \([a,u]\);

each evaluated at **both** endpoints. No deterministic tail term or moving limit is suppressed. Although each \(P\) is nonnegative, their difference need not have a fixed sign. Equation (5.4) does not establish global edge dominance.

### Actual optimizers have a strictly positive independent-box penalty

At an actual minimizing pair,
\[
r(y)\le r(0)<1,\qquad c<a+1.
\]
Consequently,
\[
q_c(y)\le\max(c,r(0))<a+1\le p_0(y)+1
\qquad(0\le y\le a).
\tag{5.5}
\]
The independent feasibility test fails strictly at **every** shared height. Hence \(S_{\rm pair}\), and therefore \(S_{\rm both}\), contains no actual optimizer. Their frozen conditional descriptions as synthetic strata are unchanged.

The penalty is quantitatively nonzero. Put
\[
\varepsilon_d=a+1-\max(d,r(0))>0
\qquad(d=c,u).
\]
Since \(z_d=f_a+1\ge a+1\), \(q_d\le a+1-\varepsilon_d\), and the quadratic coefficient in \(\mathcal B_y\) is at least \(m\), (5.2) gives
\[
\boxed{
P(a,d;V)\ge8bam\,\varepsilon_d^2>0
\qquad(d=c,u).
}
\tag{5.6}
\]
Thus neither endpoint penalty may be set to zero in an actual-optimizer argument.

### Actual active-core endpoint comparison

There is nevertheless a different exact simplification: the two **coupled** core profiles are identical, so their entire core values cancel. Keeping the complete constants,
\[
\boxed{
\begin{aligned}
\frac{h(a,c;V)-h(a,u;V)}b
={}&C(c;V)-C(u;V)\\
&+8\int_a^u
[\psi_1(\phi_c,y;V)-\psi_1(2u-y,y;V)]\,dy\\
&+8\int_u^c\psi_1(p_c,y;V)\,dy.
\end{aligned}}
\tag{5.7}
\]
At the edge, \(\phi_u=2u-y\).

The cancellation in (5.7) comes from **binding, identical coupled cores**, not independent core/tail slack. This is why substituting the independent-tail difference without its endpoint penalties would be wrong.

No sign of (5.7) is asserted.

## 6. Actual scalar geometries and clip frontiers

The branch exclusion is independent of scalar stationarity, so it remains valid across every remaining scalar or clipping geometry.

### 6.1 Scalar geometries

**Actual smooth interior.** Here
\[
a>0,\qquad u<c<a+1,
\]
with the imported additional \(c\le1\). Necessary conditions remain
\[
h_a=h_c=0
\]
at \(\lambda=V\). The active-core theorem holds throughout this branch but does not make stationarity sufficient.

**Actual smooth edge.** Here
\[
a>0,\qquad c=u.
\]
Necessary conditions remain
\[
h_a+h_c=0,\qquad h_c\ge0.
\]
The shared core has form (3.1), and the corner interval is the fixed upper face \(2u-y\).

**Vertex and the rest of \(a=0\).** These remain legitimate competitors in \(K\), including the comparison used above. They are excluded as actual-cutoff-two optimizers by the imported positivity \(a>0\), not a reversed-sign cone or an unsupported derivative claim. Without that import, the vertex conditions are
\[
h_c\ge0,\qquad h_a+h_c\ge0,
\]
and on \(a=0,c>1/2\),
\[
h_c=0,\qquad h_a\ge0.
\]

**Scalar or clip kinks.** Retain only
\[
0\in\partial_C h+N_K,
\]
using **one and the same** \(g\in\partial_C h\) in the applicable row. No exact Clarke implicit or integral-selection formula is asserted.

### 6.2 Complete pointwise clip classification

Let \([L,U]\) be the actual bounds of the block:

- pooled core: \([a,2a-y]\);
- corner: \([\max(c,2u-y),2c-y]\);
- far tail: \([c,2c-y]\).

Its selected coordinate is
\[
L\quad\text{if }V\le(L+m)^2+v+y^2,
\]
\[
r(y)\quad\text{if }
(L+m)^2+v+y^2<V<(U+m)^2+v+y^2,
\]
\[
U\quad\text{if }V\ge(U+m)^2+v+y^2.
\tag{6.1}
\]
Ties give the same coordinate and do not destroy fixed-scalar uniqueness. If \(L=U\), the coordinate is that singleton.

These are actual parameter inequalities, not a grid classification. In the shared core, the tail is always the selected coordinate plus one; there is no additional independent/slack case.

### 6.3 Actual-edge right derivative, including its endpoint

For completeness, the exact right derivative at an actual edge is
\[
\boxed{
\begin{aligned}
\frac1b\partial_c^+h(a,u;V)
={}&16uT_2+16mu^2+\frac{16}{3}T_3-8mV\\
&+16\int_a^u
\min\{0,(2u-y+m)^2+v+y^2-V\}\,dy.
\end{aligned}}
\tag{6.2}
\]

This does **not** apply S1’s all-upper-face formula outside its stratum. Derive it directly from (5.7):

- Keep
  \[
  C'(u)=8uT_2+\frac{16}{3}T_3-8mV.
  \]
- Keep the newly added far-tail endpoint
  \[
  8\psi_1(u,u)=8uT_2+16mu^2.
  \]
- For fixed \(y\in(a,u)\), the edge corner equals its floor and upper face \(2u-y\). Increasing \(c\) leaves the floor fixed and opens the upper face at speed two. Its contribution is
  \[
  2\min\{0,d_1(2u-y,y)\}.
  \]
  At a derivative tie the contribution is zero.
- Bounded difference quotients on this finite interval justify integration; the single endpoint contributes no positive-measure tie term.
- The shared core contributes zero because (3.1) is independent of \(c\) throughout a right neighborhood inside \(c<a+1\).

A negative value in (6.2) excludes that edge as a local minimum. Nonnegative is only necessary. No uniform sign, entire-edge exclusion or scalar uniqueness follows here.

## 7. Completed result, residual target, and separate gates

### Completed author result

Conditional on the frozen actual-cutoff-two imports, this manuscript proves
\[
V<v+(1+m)^2,
\]
the exact binding relation
\[
F_1=F_0+1
\]
at every shared height, and exclusion of **every shared-core-slack optimizer branch**, including branches whose independent minima lie on box faces.

The proof includes:

- a complete feasible competitor and normalization;
- exact positive polynomial certificates covering every \(m>0\);
- a nonnegative full-core/full-tail calibration, (4.5)–(4.6);
- complete corrections at both scalar endpoints, (5.4);
- the correct actual active-core endpoint comparison, (5.7).

It uses no selected-parameter experiment or derivative-sign extrapolation.

### Negative conclusions and precise residual

The following remain **NOT PROVED**:

1. Existence or parameter range of the actual regime \(1/2<V\le2\).
2. Which remaining scalar edge/interior or clip configurations globally minimize.
3. A uniform sign of (5.7) or (6.2).
4. Uniqueness of \((a,c)\), or law uniqueness beyond fixed-scalar profile uniqueness.
5. A closed global value formula, original small-epsilon result, maximal transition threshold or all-epsilon formulas.
6. Book/source equivalence, priority or novelty.

The first unproved scalar bridge is concrete: compare the remaining **binding-core** scalar candidates using (5.7), their value-zero condition and the correct scalar normals. A global comparison controlling its potentially signed corner and added-height terms is still needed. Stationarity alone is not that comparison.

### Attribution and required verification

The variational reduction, actual positivity/pruning and normal geometry are attributed to the frozen f273/f280/f305 packet at the stated scopes. The geometric-moment calculation and cubic remainder identities are elementary derivations displayed here. No public source was consulted; no external literature comparison or novelty search is claimed.

Separate gates still required:

- Independently assigned full written reconstruction of all load-bearing claims, including the degenerate-prefix competitor and normalization.
- Check of both positive polynomial certificates.
- Check of the all-block calibration and both-endpoint subtraction.
- Parent disposition at this exact quantified scope.

Any finite arithmetic replay is a separate check, **not already performed by this author**.

**Current status: AUTHOR / UNREVIEWED. No human, independent-family, formal/kernel, original-target or novelty assurance is claimed.**