# F538 author-candidate-v1.md

## A sharp half-value competitor threshold, a stronger necessary parameter band, and the remaining global sufficiency bridge

**Status: UNREVIEWED AUTHOR CANDIDATE.** This return gives a strictly stronger necessary lower bound for the original attained cutoff-two regime, using complete feasible objectives rather than synthetic stationary-root evidence. It also gives a fixed-scalar certificate on the canonical pruned strip and identifies precisely what is still needed for an original-regime existence theorem.

**Original actual cutoff-two existence remains NOT PROVED.** No claim of source equivalence, unconditional original attainment/pruning, novelty, independent-family review, human verification, or formal-kernel acceptance is made.

## 1. Inputs, chronology, and execution boundary

Before reading the scientific packet, I completed the manifest, freeze receipt, parent-supplied live metadata, dispatch receipt, and every named permission/status control through its ending. I then sent Main a direct pre-body ACK.

After that ACK, I read the entire literal packet in consecutive, ordered raw windows of at most twenty lines, from packet LF 1 through LF 574; the final window was LF 561–574. This included the complete endings of:

- S1: the adopted necessary-band disposition, logical lines 1–40.
- S2: the complete F486 author body, logical lines 1–471.
- S3: the adopted scalar-edge/complete-value disposition, logical lines 1–61.

All new mathematical work below followed that complete packet read.

The binding pins are:

- Manifest: `7b296a86e498101c5569fa2b5e350c99c4a295af9ffa2639f6be1629c7a4d798`.
- Freeze receipt: `95c32a0089d4a78d6997a42c52f6a7e89df46a935bdbb1a33d2c66b0eae56b67`.
- Literal packet: `10cafec6f0a016f3841db86e703280457d7601cf63a1dbb61aae232efbb7f422`.

The matching pins, byte/LF observations, and clock `2026-10-30T12:50:40-0700 PDT` are **parent-supplied observations**, not independently computed child hashes, a child-native start time, or evidence of continuous child supervision.

No scientific program, CAS, solver, numerical integration, test, build, or formatter was run. The rational identities below are written algebra, not fabricated computational output. No external source, linked scientific body, sibling return, or held scientific payload/consumer was opened. All historical held episodes and their consumers remain NONINPUT.

No candidate file was written under the read-only runtime restriction. This is the complete body for Main’s materialization.

## 2. Exact retained model and assurance boundary

Put

\[
m=\frac{b}{1-b},\qquad b=\frac{m}{1+m},\qquad v=m(1+m),
\]

and define

\[
\begin{aligned}
T_2&=m+2m^2,\\
T_3&=m+6m^2+6m^3,\\
T_4&=m+14m^2+36m^3+24m^4,\\
\kappa&=\frac13+2v,\qquad Q^*=1+3m+2m^2.
\end{aligned}
\]

Let \(G\) have the normalized geometric law

\[
\Pr(G=k)=(1-b)b^k,\qquad k=0,1,\ldots,
\]

and write \(M_j(t)=\mathbb E(G+t)^j\). In particular,

\[
\begin{aligned}
M_2(t)&=t^2+2mt+T_2,\\
M_4(t)&=t^4+4mt^3+6T_2t^2+4T_3t+T_4.
\end{aligned}
\]

The retained feasible all-diamond canonical profile with initial radius \(t\ge0\) has the **complete** quantities

\[
Z_t=2M_2(t)>0,\qquad N_t=\frac23M_4(t),
\]

and therefore quotient

\[
R_t(m)=\frac{M_4(t)}{3M_2(t)}.
\]

These expressions include the geometric tails and deterministic normalization. No additional external factor \(1-b\) is applied to an already normalized expectation.

For statements about the original actual optimum, I retain exactly the named canonical-reduction and attainment qualifications of S1–S3. In particular, a conditional necessary-bound theorem is not an unconditional existence theorem.

The existing upper obstruction remains the adopted number \(\beta\), characterized in S1–S2 by the global quartic

\[
P_m(t)=M_4(t)-6M_2(t)
\]

and its positive local-minimum critical point. The existing disposition gives

\[
\frac{13}{40}<\beta<\frac{33}{100}
\]

and the necessary upper bound \(m\le\beta\). It does not establish attainment at \(\beta\).

## 3. New necessary-bound theorem

Define

\[
\boxed{
\begin{aligned}
K_m(t)
&:=M_4(t)-\frac32M_2(t)\\
&=t^4+4mt^3+
\left(6m+12m^2-\frac32\right)t^2\\
&\quad +(m+24m^2+24m^3)t
+24m^4+36m^3+11m^2-\frac m2.
\end{aligned}}
\]

There is a unique pair \((\gamma,s_\gamma)\) satisfying

\[
K_\gamma(s_\gamma)=0,\qquad
\partial_tK_\gamma(s_\gamma)=0,
\]

with

\[
\boxed{
\frac{223}{3000}<\gamma<\frac{119}{1600}},
\qquad
\boxed{\frac12<s_\gamma<\frac35}.
\]

For this \(\gamma\),

\[
K_\gamma(t)\ge0\qquad(t\ge0),
\]

with equality only at \(t=s_\gamma\).

Consequently, under the original actual-attainment/reduction imports, every attained actual cutoff-two optimum obeys the strictly stronger necessary band

\[
\boxed{\gamma<m\le\beta}.
\]

Equivalently,

\[
\boxed{
\frac{\gamma}{1+\gamma}<b
\le\frac{\beta}{1+\beta}<\frac{33}{133}}.
\]

An explicit, slightly weaker consequence is

\[
\boxed{\frac{223}{3223}<b<\frac{33}{133}}.
\]

The previous lower threshold \(\alpha\) satisfies

\[
\boxed{
\alpha<\frac{223}{3000}<\gamma
<\frac{119}{1600}<\frac3{40}}.
\]

Thus this is a genuine strengthening of the adopted necessary set, not a renaming of its lower endpoint.

## 4. Proof of the new threshold

### 4.1 Critical-point classification

Work first on

\[
I=\left[\frac7{100},\frac3{40}\right].
\]

The relevant derivatives are

\[
\begin{aligned}
K_m'(t)
&=4t^3+12mt^2+(12T_2-3)t
+m+24m^2+24m^3,\\
K_m''(t)
&=12t^2+24mt+12T_2-3.
\end{aligned}
\]

For \(m\in I\), \(K_m''(0)<0\), while \(K_m''\) is strictly increasing on \(t\ge0\) and tends to \(+\infty\). Hence \(K_m'\) first decreases and then increases.

Moreover,

\[
K_m'(0)=m+24m^2+24m^3>0,
\]

and

\[
K_m'(1/2)
=-1+10m+36m^2+24m^3
\le-\frac{299}{8000}<0.
\]

At the other endpoint,

\[
K_m'(3/5)
\ge K_{7/100}'(3/5)
=\frac{17099}{125000}>0.
\]

Thus \(K_m\) has exactly two positive critical points: a local maximum before \(1/2\), and a unique local minimum

\[
s(m)\in(1/2,3/5).
\]

The global minimum on \(t\ge0\) is therefore either \(K_m(0)\) or \(K_m(s(m))\).

The endpoint value is positive throughout \(I\), because

\[
K_m(0)
=m\left(-\frac12+11m+36m^2+24m^3\right)>0.
\]

### 4.2 Strict parameter monotonicity

For every \(m\ge7/100\) and \(t\ge0\),

\[
\begin{aligned}
\partial_mK_m(t)
={}&4t^3+(6+24m)t^2\\
&+(1+48m+72m^2)t\\
&-\frac12+22m+108m^2+96m^3
>0.
\end{aligned}
\]

In fact its constant term is already at least \(26/25\).

It follows that

\[
f(m):=\min_{1/2\le t\le3/5}K_m(t)
=K_m(s(m))
\]

is continuous and strictly increasing on \(I\). This conclusion concerns the complete feasible competitor objective; \(f\) is not being identified with the original optimum.

### 4.3 Exact opposite signs

Put

\[
m_-=\frac{223}{3000},\qquad
m_+=\frac{119}{1600},\qquad
t_0=\frac{21}{40}.
\]

Direct polynomial substitution gives

\[
K_{m_-}(t_0)
=-\frac{23195458191}{81000000000000}<0.
\]

Therefore \(f(m_-)<0\).

For the upper sign, the corresponding exact identities are

\[
K_{m_+}(t_0)
=\frac{63277144}{6553600000000}
>\frac{19}{2000000},
\]

and

\[
K_{m_+}'(t_0)
=\frac{20796776}{4096000000},
\qquad
0<K_{m_+}'(t_0)<\frac{13}{2500}.
\]

On the entire interval \(1/2\le t\le3/5\),

\[
K_{m_+}''(t)
\ge K_{m_+}''(1/2)
=24m_+(1+m_+)
=\frac{4909464}{2560000}
>\frac{19}{10}.
\]

The strong-convexity inequality therefore yields, for every such \(t\),

\[
K_{m_+}(t)
\ge K_{m_+}(t_0)
+K_{m_+}'(t_0)(t-t_0)
+\frac{19}{20}(t-t_0)^2.
\]

Minimizing the right-hand quadratic over the real line gives

\[
\begin{aligned}
K_{m_+}(t)
&>
\frac{19}{2000000}
-\frac{(13/2500)^2}{2(19/10)}\\
&=\frac{453}{190000000}>0.
\end{aligned}
\]

Hence \(f(m_+)>0\).

Continuity and strict monotonicity prove that there is exactly one

\[
\gamma\in(m_-,m_+)
\]

with \(f(\gamma)=0\).

### 4.4 Global certificate at \(\gamma\)

The critical-point classification gives

\[
\min_{t\ge0}K_\gamma(t)
=\min\{K_\gamma(0),f(\gamma)\}=0.
\]

Its unique zero is \(s_\gamma=s(\gamma)\).

There is also a useful exact factorization certificate. Since \(s_\gamma\) is a double root,

\[
K_\gamma(t)
=(t-s_\gamma)^2
\left(t^2+(4\gamma+2s_\gamma)t+w_\gamma\right),
\]

where

\[
w_\gamma=\frac{K_\gamma(0)}{s_\gamma^2}>0.
\]

The second factor is strictly positive for \(t\ge0\), making the nonnegativity and unique-zero conclusion explicit.

The pair \((\gamma,s_\gamma)\) is specified by rational polynomial equations and isolating intervals. No numerical root approximation is used.

### 4.5 Strict improvement over \(\alpha\)

Recall

\[
L(m)=384m^4+768m^3+416m^2+32m-5,
\]

with unique positive zero \(\alpha\). At the lower isolating point,

\[
L(223/3000)
=\frac{357360169344}{81000000000000}>0.
\]

Since \(L\) is strictly increasing on \(m\ge0\),

\[
\alpha<\frac{223}{3000}<\gamma.
\]

## 5. Why this excludes actual parameters

For every complete all-diamond competitor,

\[
R_t(m)-\frac12
=\frac{K_m(t)}{3M_2(t)}.
\]

The denominator is positive.

If \(m\le\alpha\), the already feasible competitor \(t=1/2\) satisfies

\[
K_m(1/2)=\frac{L(m)}{16}\le0,
\]

so its quotient is at most \(1/2\).

If \(\alpha<m\le\gamma\), then \(m>7/100\). Strict parameter monotonicity gives

\[
K_m(s_\gamma)\le
K_\gamma(s_\gamma)=0.
\]

Thus the feasible competitor of radius \(s_\gamma\) again has quotient at most \(1/2\), with strict inequality when \(m<\gamma\).

Global minimality would consequently imply

\[
V\le\frac12.
\]

This contradicts the actual cutoff-two hypothesis \(V>1/2\). Therefore

\[
\boxed{m>\gamma}.
\]

Combining this with the adopted upper obstruction gives \(\gamma<m\le\beta\).

This proof requires neither treating a stationary root as an original value nor assuming that a candidate is globally optimal. It uses an explicit feasible full-law competitor to contradict the required global minimum.

## 6. Additional analytic certificate on the canonical pruned strip

This section is a **new author lemma in the corrected fixed-scalar canonical model**. It is not an unconditional pruning theorem for the original problem.

Let

\[
\mathcal S
=\{(a,c):a\ge0,\ a+\tfrac12\le c<a+1\},
\]

and let \(h(a,c;\lambda)\) denote the complete fixed-scalar minimum of \(N-\lambda Z\) over the canonical profiles with these scalar parameters.

At the fixed scalar

\[
\lambda_0=\frac12,
\]

the following certificate holds:

- At \(m=\gamma\), \(h(a,c;\lambda_0)\ge0\) throughout \(\mathcal S\), with equality only at the all-diamond edge pair
  \[
  a=s_\gamma/2,\qquad c=a+\frac12.
  \]
- For every \(m>\gamma\), \(h(a,c;\lambda_0)>0\) throughout \(\mathcal S\).

The argument below checks applicability at the fixed scalar rather than presupposing an actual cutoff-two optimizer.

### 6.1 Binding core and the \(c\)-direction

The retained slack-removal estimate is strictly positive because

\[
Q^*-\lambda_0+y^2>0.
\]

Within \(\mathcal S\), setting \(F_1=F_0+1\) respects the core bounds: \(F_0\ge a\) gives \(F_0+1\ge a+1>c\), and \(F_0\le2a-y\) gives \(F_0+1\le2a+1-y\). Thus the same fixed-scalar projection is applicable without assuming \(\lambda_0=V\).

Write

\[
d_\lambda(z,y)=(z+m)^2+v+y^2-\lambda,
\qquad
D(x)=2x^2+2mx+T_2,
\]

and \(s=2a+1-c\). The complete clipped-value derivative identity is

\[
\frac{h_c}{8b}
=D_0(c)
+\int_s^c[d_\lambda(c,y)]_+\,dy
-2\int_a^c[-d_\lambda(2c-y,y)]_+\,dy,
\]

where

\[
\begin{aligned}
D_0(c)
&=2cT_2+2mc^2+\frac23T_3-m\lambda\\
&=m(D(c)-\lambda)+2cv+
\frac{2m}{3}+3m^2+2m^3.
\end{aligned}
\]

For every \(c\ge1/2\),

\[
D(c)\ge D(1/2)=\frac12+2v>\lambda_0.
\]

Furthermore, \(y\mapsto d_{\lambda_0}(2c-y,y)\) decreases on \(y\le c\), so

\[
d_{\lambda_0}(2c-y,y)
\ge d_{\lambda_0}(c,c)
=D(c)-\lambda_0>0.
\]

The negative-part integral vanishes, while \(D_0(c)>0\). Hence

\[
\boxed{h_c(a,c;\lambda_0)>0\quad\text{throughout }\mathcal S}.
\]

Thus the fixed-scalar strip minimum lies on \(c=a+1/2\). This is a statement about the explicitly defined strip, not permission to discard its complement.

### 6.2 The entire no-lower-face edge

Set

\[
e(a)=h(a,a+1/2;\lambda_0),\qquad
R(a)=4a^2+4ma+T_2.
\]

When \(T_2<\lambda_0\), define \(a_R<a_D\) by

\[
R(a_R)=\lambda_0,\qquad D(a_D)=\lambda_0.
\]

For \(0\le a\le a_R\), the core is all-upper and

\[
e(a)=\frac23K_m(2a).
\]

For \(a_R<a<a_D\), define \(q\in(0,a)\) by

\[
\lambda_0=D(a)+2mq+2q^2.
\]

The complete rounded-core value is

\[
\begin{aligned}
e(a)
={}&\frac23M_4(2a)-2\lambda_0M_2(2a)\\
&-8\int_0^{a-q}(U-r)^2
\left(\frac{U+2r}{3}+m\right)\,dy,
\end{aligned}
\]

where

\[
U=2a-y,\qquad
r=\sqrt{\lambda_0-v-y^2}-m.
\]

Thus neither the geometric tail nor the rounded-core gain is dropped.

Its exact derivative is

\[
\frac{e'(a)}{16}
=F_R(a)
=m\left[a^2+(1+2m)a+\kappa-\frac14\right]
-mq^2-\frac43q^3,
\]

with

\[
F_R'(a)
=m(2a+1+2m)+2q(2a+m)>0.
\]

At the all-upper join \(q=a_R\),

\[
F_R(a_R)=J_m(a_R),
\]

where

\[
J_m(a)
=m\left[(1+2m)a+\frac1{12}+2v\right]-\frac43a^3.
\]

For \(m\ge7/100\),

\[
R(3/10)
\ge R_{7/100}(3/10)
=\frac{2619}{5000}>\frac12,
\]

so \(0\le a_R<3/10\).

For fixed \(a\ge0\),

\[
\partial_mJ_m(a)
=(1+4m)a+\frac1{12}+4m+6m^2>0.
\]

The function \(J_{7/100}(a)\) is concave on \([0,3/10]\). Its endpoint values are

\[
J_{7/100}(0)=\frac{24479}{1500000},
\qquad
J_{7/100}(3/10)=\frac{6389}{1500000}.
\]

Therefore

\[
\boxed{
F_R(a_R)\ge\frac{6389}{1500000}>0}.
\]

The entire rounded branch is strictly increasing. It cannot undercut its all-upper joining value.

At \(m=\gamma\), that joining value is strictly positive. Indeed \(2a_R\in(1/2,3/5)\), and

\[
K_\gamma'(2a_R)=12F_R(a_R)>0
\]

places the join strictly after the unique local minimum \(s_\gamma\). Thus the unique zero occurs on the genuine all-upper branch, before rounding starts.

### 6.3 The lower-face edge and boundary cases

If \(D(a)\ge\lambda_0\), then

\[
d_{\lambda_0}(2a-y,y)
\ge D(a)-\lambda_0\ge0
\qquad(0\le y\le a),
\]

so the negative core integral \(A\) vanishes.

The retained complete derivative identity

\[
\frac{h_a}{16}=\frac L2-A+bB
\]

then gives \(h_a\ge0\), while §6.1 gives \(h_c>0\). Consequently,

\[
e'(a)=h_a+h_c>0
\]

throughout the lower-face region.

If \(T_2\ge\lambda_0\), this region begins at \(a=0\). The empty-core edge has

\[
e(0)=\frac23K_m(0)>0
\]

for \(m\ge\gamma\).

The joining cases \(D(a)=\lambda_0\), \(q=a\), and \(q=0\) are covered by the matching clipped-value formulas. The case \(a=0\) uses the right edge derivative; no infeasible negative-\(a\) direction is invoked.

Combining these cases with the strict \(c\)-direction proves the strip certificate.

**Its limitation is essential:** pointwise positivity on this strip is not, by itself, unconditional original attainment or a uniform lower bound over excluded canonical/noncanonical competitors.

## 7. A noncircular sufficiency frontier

The new strip certificate can be combined with the existing complete upper competitor without pretending that the global consumer has been paid.

Let

\[
t_\beta=s(\beta)
\]

be the adopted minimizer defining \(\beta\). Then

\[
P_\beta(t_\beta)=0.
\]

The adopted strict parameter monotonicity of \(P_m(t)\) on \(m\ge3/10,\ t\ge0\) implies

\[
P_m(t_\beta)\le0
\qquad
\left(\frac3{10}\le m\le\beta\right),
\]

strictly when \(m<\beta\).

Because

\[
N_{t_\beta}-2Z_{t_\beta}
=\frac23P_m(t_\beta),
\]

this is an actual feasible complete-law upper competitor:

\[
R_{t_\beta}(m)\le2.
\]

On the other hand, \(m\ge3/10>\gamma\), so §6 establishes

\[
N-\frac12Z>0
\]

for every canonical profile whose scalar pair lies in \(\mathcal S\).

It follows that the following is a genuine conditional sufficiency criterion:

> For a parameter \(m\in[3/10,\beta]\), if the original-to-canonical reduction is applicable and a global minimum is attained with a representative in \(\mathcal S\), **without presupposing \(V>1/2\)**, then that minimum satisfies
> \[
> \frac12<V\le2.
> \]
> For \(m<\beta\), the displayed competitor gives \(V<2\). At \(m=\beta\), the adopted endpoint necessity theorem then forces
> \[
> V=2,\qquad
> a=t_\beta/2,\qquad
> c=a+\frac12,
> \]
> with the stated all-diamond canonical profile.

This implication does not assume the conclusion \(V>1/2\) in order to derive it: the lower inequality comes from the fixed-scalar strip certificate, and the upper inequality comes from a feasible full-law competitor.

**The prerequisite is not established here.** The existing positivity/pruning statements are qualified by an attained actual cutoff-two hypothesis. They cannot be reused circularly to prove that very hypothesis.

## 8. Exact first unpaid global consumer

The first unpaid bridge is:

\[
\boxed{
\begin{gathered}
\text{Establish global attainment and localization into }\mathcal S\\
\text{for the relevant original/canonical optimization,}\\
\text{without assuming in advance that }V>1/2.
\end{gathered}}
\]

In particular, the present argument does not discard:

- canonical scalar pairs with \(c\ge a+1\);
- competitors outside the retained canonical reduction;
- minimizing sequences for which the required attainment/localization has not been established.

A result restricted to stationary edge candidates, a truncated-tail calculation, or a numerical plot would not pay this consumer. Nor would applying the already conditional actual-optimizer pruning conclusion before establishing its cutoff-two premise.

Original/book source correspondence remains a separate unpaid boundary.

## 9. Delivered result and limits

The new necessary obstruction is

\[
\boxed{
\alpha<
\frac{223}{3000}<\gamma<
\frac{119}{1600}<\frac3{40},
\qquad
\gamma<m\le\beta}.
\]

It is supported by complete feasible geometric-tail objectives, a global quartic classification, exact rational sign certificates, and a positive-denominator comparison with the required actual value.

The additional fixed-scalar analysis covers all clipping branches and boundaries on the explicitly stated pruned strip. It provides a concrete conditional sufficiency frontier for \(m\in[3/10,\beta]\), but **does not establish original-regime existence anywhere in that interval**.

No scientific execution occurred. No synthetic scalar root is asserted to be the actual original value. No historical penalty-sign finding, held episode, or held consumer is rehabilitated. Disjoint checking and parent disposition have not yet occurred.