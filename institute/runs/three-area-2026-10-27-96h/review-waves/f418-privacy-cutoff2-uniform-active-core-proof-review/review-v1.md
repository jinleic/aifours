# F418 — WRITTEN review of the uniform actual-cutoff-two active-core theorem

**Verdict: SUPPORTED at the stated conditional scope.**  
**Findings: 0 FATAL / 0 MAJOR / 0 MINOR.**

The central theorem is supported: conditional on the adopted actual-cutoff-two reduction and its actual-optimizer positivity/pruning imports, every canonical actual optimizer in the full range \(1/2<V\le2\) has
\[
V<1+3m+2m^2,\qquad
F_1(y)=F_0(y)+1\quad(0\le y\le a),
\]
with the stated clipped pooled-root formula for \(F_0\). The argument excludes strict shared-core slack on box faces as well as in free-free configurations. It does not establish existence of that regime, scalar-pair uniqueness, global edge dominance or a global value formula.

This is the complete review body for parent materialization. **No repository review file was written.**

## 1. Scope, inputs and actual method

### Frozen bindings

The following bindings are **parent-supplied observations**, not hashes independently executed by this reviewer:

- Manifest: `9e8c77d618d0bfd41ee7edf01f27ec5ea463ce433cf6a30a58d692182d9b3d59`.
- Freeze receipt: `a2a5a3fa5d373dddaf102f664acd6b944f0bbeb296db863c0b47eab9d148c1b0`.
- Literal packet: `be62aea1cd2512077ec091005c9e2bcf39b80ec6b30082ac85d0b32259ec13bb`.

The clock `2026-10-30T10:56:06-0700 PDT` is attributed to the parent metadata supply. It is **not** a reviewer-native start, completion or elapsed-time observation.

All source LF references below use the frozen manifest’s identifiers:

| ID | Source | Parent-supplied SHA256 |
|---|---|---|
| S1 | F400 `review-v1.md`, “Uniform active-core theorem for the actual cutoff-two problem” | `6d907d4f950cb5ab4a1a17ad051ea061a48d7916d24547e4ff14997a46162654` |
| S2 | Adopted f273 variational-reduction disposition | `51502ed65a16c5fe43da2416ee7e2365dbc1df306d388c9b01dec966012d067c` |
| S3 | Complete f273 written review | `ffd402176e70512fa102eb75ee21011926c4a8b5e86e34eb9dd674d590ea2a35` |
| S4 | Correct normal cones and necessary Clarke-inclusion disposition | `dd4e6ff73c21b2256d78758edfb26bcf97dcb8ff39a35866685f098dbbc8c470` |

### Read order and exclusions

I read the full manifest, freeze receipt, all seven listed status-only controls and the complete parent metadata supply, then sent Main a direct administrative **pre-body ACK**. Only afterward did I read the mathematical packet.

The entire packet was read in order using exact raw windows of at most 20 LF: \(1\!-\!20,21\!-\!40,\ldots,901\!-\!920,921\!-\!922\). This included every source ending: S1 through displayed source line 698, S2 through 16, S3 through 168 and S4 through 38. No elided mathematical window remained unrecovered. Mathematical derivation began after the final packet window. The dispatch receipt was subsequently read as administrative attribution.

Mandatory memory/protocol guidance was also read; it was not used as a mathematical premise.

No held mathematical payload or linked excluded body was opened. The entire parent-private privacy auxiliary episode and its consumers, PH v8/cp116, the AME held episode and other quarantined outputs remained **NONINPUT**. No current sibling output, author program or external scientific source was consulted. This is an access/method disclosure, not a certificate of cognitive isolation.

All reconstruction below is written mathematics. **No selected new instance, scientific executable, CAS, interpreter, enumeration, replay, solver, external-model CLI, build, test, lint or formatter was run.** No code was assigned to this WRITTEN gate; no finite-check result is claimed.

## 2. Exact mathematical imports

The review uses the following imports at their existing scopes:

1. **Adopted functional and fixed-scalar profile elimination:** S2 LF 5–9; S3 LF 43–53, 75–111. These provide the corrected canonical feasible profiles, their unique fixed-scalar minimization, the unique value zero \(\rho(a,c)\), and the conditional attained reduction
   \[
   V=\min_{\substack{a\ge0\\c\ge a+1/2}}\rho(a,c).
   \]
   They do not provide scalar-pair uniqueness or unrestricted stationarity sufficiency.

2. **Actual-optimizer positivity and pruning:** S3 LF 95. Under the standing actual-cutoff-two hypothesis, \(a>0\) and
   \[
   C_1\subset(C_0+D)\cup\overline B(\sqrt V).
   \]
   These are imports, not newly proved upstream results.

3. **Pooled derivative:** S2 LF 7 and S3 LF 65–73. The variance is exactly \(v=m(1+m)\).

4. **Necessary scalar geometry:** S4 LF 7–24. Nonsmooth necessity is understood with the adopted compatible locally Lipschitz extension or precise relative convention. No exact Clarke interchange, implicit identity, sufficiency or ordinary-directional equivalence is imported.

The diamond-subclass result in S2/S3 is not needed to establish the active-core theorem.

## 3. Complete functional and geometric-tail reconstruction — SUPPORTED

**Locations:** S1 LF 36–173.

Let
\[
0<b<1,\qquad m=\frac b{1-b}>0,\qquad v=m(1+m),
\]
and
\[
\Pr(G=j)=(1-b)b^j,\quad j\ge0.
\]

Near zero,
\[
\mathbb E(1+t)^G
=\frac{1-b}{1-b(1+t)}
=\frac1{1-mt}.
\]
Thus \(\mathbb E(G)_k=k!m^k\). Expanding ordinary powers into falling factorials gives
\[
T_2=m+2m^2,\qquad
T_3=m+6m^2+6m^3,
\]
\[
T_4=m+14m^2+36m^3+24m^4.
\]
In particular \(T_2>0\).

For a canonical profile \(F\) with diagonal parameter \(t\), sector integration gives
\[
A(F)=8\int_0^t(F-y)\,dy,
\]
\[
Q(F)=8\int_0^t
\left(\frac{F^3}{3}+y^2F-\frac{4y^3}{3}\right)dy,
\qquad
B(F)=8\int_0^t(F^2+y^2)\,dy.
\]

For diamond expansion by radius \(r\), the sector profile is \(F+r\) on \([0,t]\), followed by \(2t+r-y\) on \([t,t+r/2]\). Integrating both blocks yields
\[
A(C+rD)=A(C)+8tr+2r^2,
\]
\[
Q(C+rD)=Q(C)+B(C)r+(A(C)+8t^2)r^2
+\frac{16}{3}tr^3+\frac23r^4.
\]
For example, the moment increment over the first block is
\[
B(C)r+(A(C)+4t^2)r^2+\frac83tr^3;
\]
the added triangular block contributes
\[
4t^2r^2+\frac83tr^3+\frac23r^4.
\]
Their sum gives the displayed complete expansion.

The level weights are
\[
(1-b)C_0,\qquad (1-b)b^{j+1}(C_1+jD),\quad j\ge0.
\]
Consequently the complete tail is weighted by **\(b\mathbb E\)**, not by an additional factor \(b(1-b)\) outside that expectation. Therefore
\[
Z=(1-b)A(F_0)+b\{A(F_1)+8cm+2T_2\},
\]
\[
N=(1-b)Q(F_0)+b\left\{
Q(F_1)+mB(F_1)+(A(F_1)+8c^2)T_2
+\frac{16}{3}cT_3+\frac23T_4
\right\}.
\]
In particular,
\[
Z\ge2bT_2>0.
\]

The signed functional is also correct. Writing
\[
\psi_0(x,y;\lambda)
=\frac{x^3}{3}+(y^2-\lambda)x-\frac{4y^3}{3}+\lambda y,
\]
\[
\psi_1(z,y;\lambda)
=\psi_0(z,y;\lambda)+m(z^2+y^2)+T_2z,
\]
one obtains
\[
H_\lambda=N-\lambda Z
=8(1-b)\int_0^a\psi_0(F_0,y;\lambda)\,dy
+8b\int_0^c\psi_1(F_1,y;\lambda)\,dy+bC(c;\lambda),
\]
where
\[
C(c;\lambda)
=4c^2T_2+\frac{16}{3}cT_3+\frac23T_4
-\lambda(8cm+2T_2).
\]

The coefficient \(4c^2T_2\) is not a missing half of the tail constant: expanding \(A(F_1)T_2\) supplies \(-4c^2T_2\), which combines with the original \(+8c^2T_2\).

Finally,
\[
d_0(x,y)=x^2+y^2-\lambda,\qquad
d_1(z,y)=(z+m)^2+v+y^2-\lambda,
\]
because \(m^2+v=T_2\). The nonnegative-root conventions in S1 LF 155–163 correctly handle nonexistent or nonpositive stationary roots.

## 4. Actual scalar corridor — SUPPORTED AS AN EXACT-SCOPE IMPORT

**Locations:** S1 LF 204–218; import S3 LF 95.

The positivity \(a>0\) is expressly imported.

If \(c=u=a+1/2\), then \(c<a+1\) directly. If \(c>u\), the diagonal endpoint \((c,c)\) lies outside \(C_0+D\). The imported pruning inclusion therefore puts that endpoint in \(\overline B(\sqrt V)\), yielding
\[
2c^2\le V\le2.
\]
Thus \(c\le1<a+1\). Every actual optimizer covered by these imports satisfies
\[
a>0,\qquad u\le c<a+1.
\]

This does **not** exclude \(a=0\) from the unrestricted feasible scalar domain. Its use as a competitor below is consistent with its imported exclusion only for actual optimizers under the standing hypothesis.

## 5. Degenerate-prefix competitor and universal strict bound — SUPPORTED

**Locations:** S1 LF 221–296.

### Feasibility and normalization

At
\[
(a,c)=(0,\tfrac12),\qquad C_0=\{0\},\quad C_1=D,
\]
the first profile is the singleton value \(F_0(0)=0\), while
\[
F_1(y)=1-y,\qquad 0\le y\le\tfrac12.
\]
This is continuous, nonincreasing and 1-Lipschitz. It satisfies the box, core coupling and corner floor; the corner floor equals the upper box. Hence it is an admissible competitor in the adopted domain even though it need not have a genuine actual two-prefix cutoff.

A radius-\(s\) diamond has
\[
A(sD)=2s^2,\qquad Q(sD)=\frac23s^4.
\]
The complete nonzero tail is \((G+1)D\), with outer weight \(b\). For every positive integer \(k\),
\[
b\mathbb E(G+1)^k
=(1-b)\sum_{j\ge1}b^j j^k
=T_k.
\]
It follows that
\[
Z_\diamond=2T_2,\qquad
N_\diamond=\frac23T_4,\qquad
J_\diamond=\frac{T_4}{3T_2}.
\]
Equivalently,
\[
H_\lambda(\{0\},D;0,\tfrac12)
=\frac23T_4-2\lambda T_2.
\]
There is no omitted first-core term, tail weight or normalization factor.

The attained global reduction consequently gives
\[
V\le J_\diamond.
\]
Together with the standing bound, \(V\le\min(2,J_\diamond)\).

### Polynomial certificates on the entire half-line

Set
\[
Q_*=1+3m+2m^2,\qquad t=\frac27.
\]
Direct symbolic expansion gives
\[
Q_*-J_\diamond
=\frac{2+m-12m^2-12m^3}{3(1+2m)}.
\]
The proposed numerator identity is exact:
\[
2+m-12m^2-12m^3
=\frac{352}{343}
+(t-m)\left(12m^2+\frac{108}{7}m+\frac{167}{49}\right).
\]
It is strictly positive throughout \(0<m\le t\), including \(m=t\).

The second identity is also exact:
\[
Q_*-2
=\frac1{49}+(m-t)\left(2m+\frac{25}{7}\right),
\]
and is strictly positive throughout \(m\ge t\), again including the split boundary.

Thus
\[
\min(2,J_\diamond)<Q_*\qquad\text{for every }m>0,
\]
and therefore
\[
\boxed{V<Q_*}.
\]
The excluded endpoint \(m=0\) is not used. No new selected parameter instance is needed.

Let
\[
\delta=Q_*-V>0.
\]
Then, for all \(y\ge0\) and \(z\ge1\),
\[
d_1(z,y)\ge d_1(1,y)=\delta+y^2>0.
\]
The clipped-root convention also gives
\[
r(y)=\max\{0,\sqrt{\max(V-v-y^2,0)}-m\}<1
\]
for every \(y\ge0\), including where the radicand is nonpositive.

## 6. Entire-core binding and global canonical feasibility — SUPPORTED

**Locations:** S1 LF 298–329.

Fix an actual scalar pair and a shared height \(0\le y\le a\). For every feasible core coordinate \(x\),
\[
x\ge a,\qquad c<a+1\le x+1,
\]
and
\[
x+1\le2a+1-y\le2c-y.
\]
Hence the smallest feasible tail coordinate conditional on \(x\) is exactly \(x+1\). Since \(x+1>1\), the tail integrand is strictly increasing throughout its admissible conditional range. Its unique conditional minimizer is
\[
z=x+1.
\]
This includes lower- and upper-box configurations; no free-root assumption is used.

On that active line, put
\[
\Phi_y(x)=(1-b)\psi_0(x,y;V)+b\psi_1(x+1,y;V).
\]
Using \(b(1+m)=m\) and \(T_2=m+2m^2\),
\[
\Phi_y'(x)
=(1-b)d_0(x,y)+bd_1(x+1,y)
=d_1(x,y),
\]
and
\[
\Phi_y''(x)=2(x+m)>0.
\]
Thus the unique pointwise minimizer is
\[
\boxed{
f_a(y)=\operatorname{clip}(r(y),[a,2a-y]),\qquad
F_1(y)=f_a(y)+1.
}
\]

The pointwise solution is globally admissible, not merely a collection of unrelated slice minima:

- On a selected free-root branch,
  \[
  r'(y)=-\frac{y}{r(y)+m}.
  \]
  In the core, \(r(y)\ge a\ge y\), so the slope lies in \([-1,0]\).
- Lower- and upper-face branches have slopes \(0\) and \(-1\). The clipping formulas are continuous at ties, and \(f_a(a)=a\).
- For any \(u\le d<a+1\), the corner bounds
  \[
  L_d(y)=\max(d,2u-y),\qquad U_d(y)=2d-y
  \]
  are ordered on \([a,u]\). The far-tail bounds \([d,2d-y]\) are ordered on \([u,d]\).
- At \(y=a\), \(L_d(a)=a+1\). Since \(r(a)<1<a+1\), the corner clip equals \(a+1=f_a(a)+1\).
- At \(y=u\), the corner and far-tail clips have identical bounds \([d,2d-u]\).
- At \(y=d\), both far-tail endpoints equal \(d\).
- On any selected tail-root branch, \(r(y)\ge d\ge y\), giving the same slope bound. The effective floors and upper boxes also have slopes in \([-1,0]\).

Consequently all pieces join continuously and define canonical nonincreasing 1-Lipschitz profiles, including \(d=u\), collapsed intervals and clip ties.

This construction supplies the globally feasible comparison needed to exclude slack; it does not rely on an isolated coordinate lowering that might violate a neighboring join.

## 7. Strict calibration and exclusion of slack at even one height — SUPPORTED

**Locations:** S1 LF 333–417.

For \(s,t\ge0\),
\[
\psi_1(t,y)-\psi_1(s,y)
=d_1(s,y)(t-s)
+(t-s)^2\left(\frac{t+2s}{3}+m\right)
=:\mathcal B_y(t,s).
\]
If \(s\) minimizes the same interval containing \(t\), its normal term is nonnegative. Since \(m>0\), the remainder is strictly positive when \(t\ne s\). This covers both box faces and derivative ties.

For arbitrary feasible canonical profiles at \(a>0\), \(u\le d<a+1\), write
\[
x=F_0,\qquad D=F_1-F_0-1\ge0
\]
on the core. Exact cubic expansion yields
\[
\psi_1(x+1+D,y)-\psi_1(x+1,y)
=d_1(x+1,y)D+(x+1+m)D^2+\frac{D^3}{3}
=:\Gamma_y(x,D).
\]
The pooled identity then gives the complete calibration
\[
\begin{aligned}
H_V-h(a,d;V)
={}&8\int_0^a\mathcal B_y(x,f_a)\,dy\\
&+8b\int_0^a\Gamma_y(x,D)\,dy\\
&+8b\int_a^u\mathcal B_y(F_1,\phi_d)\,dy\\
&+8b\int_u^d\mathcal B_y(F_1,p_d)\,dy.
\end{aligned}
\]
The deterministic term \(bC(d;V)\) cancels because both values use the same scalars; it has not been discarded from the functional.

All terms are nonnegative. Moreover,
\[
\boxed{
H_V-h(a,d;V)\ge8b\delta\int_0^aD(y)\,dy.
}
\]

At an actual minimizing scalar pair, \(h(a,c;V)=0\). If \(D\) is positive at any shared height, continuity and \(a>0\) make its core integral positive, including when that height is an endpoint. Therefore
\[
N-VZ>0,
\]
contradicting attainment of \(V\), since \(Z>0\).

Thus **strict slack at even one canonical shared height is excluded**. Equality in the full calibration requires the displayed corrected profiles in every positive-length block, with continuity fixing their endpoint versions.

The same calibration is valid at \(d=u\). This does not assert that \(h(a,u;V)=0\) when the actual optimizer has \(c>u\).

## 8. Independent-box strata and both-endpoint accounting — SUPPORTED

**Locations:** S1 LF 419–547.

For arbitrary feasible scalars, the corrected two-line rule agrees with the adopted fixed-box minimization:

- If the independent projections satisfy \(q_d\ge p_0+1\), they are the unique joint minimizer.
- Otherwise the minimizer binds, and its active interval is
  \[
  [\max(a,d-1),\,2a-y].
  \]
  Test failure implies this interval is nonempty; no converse is required.

Strict convexity supplies uniqueness through ties. The imported canonical-feasibility reconstruction covers the unrestricted scalar domain; the active-core proof above additionally establishes the required actual corridor directly.

Subtracting independent-box values gives exactly
\[
h=h_{\rm ind}+P.
\]
The penalty includes both shared-core coordinates and the corner block. Thus subtraction at \(c\) and \(u\) gives S1 equation (5.4), retaining:

1. \(b[C(c;\lambda)-C(u;\lambda)]\);
2. the added interval \([u,c]\);
3. the common-height tail difference over \([0,u]\);
4. **both** endpoint penalties \(P(a,c;\lambda)-P(a,u;\lambda)\).

For actual scalars, the strict pointwise gap is
\[
q_d(y)\le\max(d,r(0))<a+1\le p_0(y)+1,
\qquad 0\le y\le a,\quad d\in\{c,u\}.
\]
Hence the independent feasibility test fails at **every** shared height. This supports exclusion of \(S_{\rm pair}\) and \(S_{\rm both}\) at the feasibility meanings stated in S1; it is not an independent audit of any additional, unpasted definitions of those labels.

With
\[
\varepsilon_d=a+1-\max(d,r(0))>0,
\]
the cubic remainder gives
\[
P(a,d;V)\ge8bam\varepsilon_d^2>0.
\]
Neither endpoint penalty can therefore be set to zero in an actual-optimizer comparison. Their difference still need not have a fixed sign.

Alternatively, the **coupled** core profiles are identical at \(d=c\) and \(d=u\), so those complete core contributions cancel. Since \(\phi_u=2u-y\),
\[
\begin{aligned}
\frac{h(a,c;V)-h(a,u;V)}b
={}&C(c;V)-C(u;V)\\
&+8\int_a^u[\psi_1(\phi_c,y;V)-\psi_1(2u-y,y;V)]\,dy\\
&+8\int_u^c\psi_1(p_c,y;V)\,dy.
\end{aligned}
\]
This is the claimed equation (5.7). It establishes an exact comparison identity, **not** global edge dominance.

## 9. Scalar normals, clip frontiers and edge derivative — SUPPORTED AT NECESSARY SCOPE

**Locations:** S1 LF 549–646.

The smooth normal conditions reproduce S4 correctly:
\[
\begin{array}{c|c}
\text{Geometry}&\text{Necessary conditions}\\ \hline
a>0,\ c>u&h_a=h_c=0\\
a>0,\ c=u&h_a+h_c=0,\ h_c\ge0\\
a=0,\ c=\frac12&h_a+h_c\ge0,\ h_c\ge0\\
a=0,\ c>\frac12&h_c=0,\ h_a\ge0.
\end{array}
\]
At kinks, the inclusion uses one common subgradient and the adopted extension/relative convention. No sufficiency or rejected exact Clarke representation is needed.

For an actual block \([L,U]\), monotonicity of \(d_1\) gives precisely the three clipping cases in equation (6.1). At a threshold the adjacent expressions agree; at \(L=U\) the coordinate is the singleton. Thus no tie creates fixed-scalar profile nonuniqueness.

The right-edge derivative is also supported. Hold \(a,V\) fixed and let \(c\downarrow u\) from above within \(c<a+1\):

- The core is independent of \(c\), so contributes zero.
- The deterministic term contributes
  \[
  C'(u)=8uT_2+\frac{16}{3}T_3-8mV.
  \]
- The newly opened far-tail interval contributes
  \[
  8\psi_1(u,u)=8uT_2+16mu^2.
  \]
- For each fixed \(y\in(a,u)\), the corner floor remains \(2u-y\) initially, while the upper face opens at speed two. Its minimized-value derivative is
  \[
  2\min\{0,d_1(2u-y,y)\}.
  \]
  It is zero at a derivative tie.

The corner clips move by at most twice the scalar increment, and the integrand derivatives are bounded on the relevant finite neighborhood. This supplies bounded difference quotients for integration. The moving-floor endpoint layer does not add a first-order integral term.

Combining the terms gives
\[
\begin{aligned}
\frac1b\partial_c^+h(a,u;V)
={}&16uT_2+16mu^2+\frac{16}{3}T_3-8mV\\
&+16\int_a^u
\min\{0,(2u-y+m)^2+v+y^2-V\}\,dy,
\end{aligned}
\]
as claimed. A negative value excludes that edge as a local minimum; a nonnegative value is only necessary. No uniform sign or whole-edge exclusion follows.

## 10. Claimwise disposition and remaining gates

| Claim | Disposition |
|---|---|
| Complete \(N/Z\), geometric moments, tail weight and signed constant | **SUPPORTED** |
| Feasibility of the degenerate-prefix diamond competitor | **SUPPORTED** |
| \(Z_\diamond=2T_2\), \(N_\diamond=2T_4/3\), \(V\le J_\diamond\) | **SUPPORTED** |
| Strict polynomial cover of every \(m>0\), including the split boundary | **SUPPORTED** |
| \(V<Q_*\), \(r(y)<1\), strict tail monotonicity above one | **SUPPORTED** |
| Actual \(a>0\) and \(u\le c<a+1\) | **SUPPORTED AS IMPORTED**, with the pruning implication reconstructed |
| Unique pointwise binding core, including all box faces and ties | **SUPPORTED** |
| Global canonical feasibility and joins | **SUPPORTED** |
| Strict exclusion of slack at even one shared height | **SUPPORTED** |
| Exclusion of independent-feasible strata at their stated meanings | **SUPPORTED** |
| Full calibration, endpoint penalties and active-core subtraction | **SUPPORTED** |
| Normal conditions and right-edge derivative | **SUPPORTED AT NECESSARY SCOPE** |
| Actual-regime existence or its parameter range | **INCONCLUSIVE / NOT PROVED**, correctly excluded |
| Scalar-pair or unrestricted law uniqueness | **INCONCLUSIVE / NOT PROVED**, correctly excluded |
| Uniform endpoint-comparison sign, global edge dominance or global value formula | **INCONCLUSIVE / NOT PROVED**, correctly excluded |
| Original small-epsilon target, source/book equivalence, priority or novelty | **NOT ESTABLISHED**, correctly excluded |

The remaining scalar bridge is exactly the one identified by the author: compare the surviving binding-core scalar candidates using their value-zero conditions, valid boundary geometry and complete signed endpoint comparison. Stationarity alone does not supply that bridge.

This return provides a **same-harness written reconstruction**, not parent adoption. Separate parent disposition remains required. No independent-model-family, human, formal/kernel, finite-execution, original-target or novelty gate is claimed cleared.

## Verdict fields

**overall_correctness:** correct

**explanation:** The complete feasible competitor and strict polynomial cover establish \(V<Q_*\) uniformly under the full actual-cutoff-two hypothesis. The resulting monotonicity, globally feasible clipped profiles and exact calibration rigorously exclude every shared-core-slack optimizer branch, while the manuscript preserves the necessary distinctions from scalar uniqueness, regime existence and global value claims.

**confidence:** 0.98