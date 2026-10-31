# F576 WRITTEN review: global half-value competitor threshold

**Verdict: SUPPORTED at the new necessary-band scope.**  
**Findings at that scope: 0 FATAL / 0 MAJOR / 0 MINOR.**

The frozen candidate correctly establishes the unique algebraic half-value threshold \(\gamma\), its stated isolating interval, and the stronger **conditional necessary** band
\[
\gamma<m\le\beta.
\]
This does not establish actual cutoff-two existence, sufficiency of that interval, or unconditional original attainment/localization.

This is the complete review body for parent materialization as this wave’s `review-v1.md`. No working-tree file was written under the read-only runtime restriction.

## 1. Inputs, read coverage, and method

Before reading the mathematical packet, I read the complete manifest, freeze receipt, parent-supplied live metadata, and all twelve listed status-only controls through their endings. I then sent Main a direct administrative pre-body ACK.

I subsequently read **every packet LF 1–818**, in consecutive ordered exact-raw windows of at most twenty LF. The final window was LF 801–818. This included:

- **S1:** all 776 logical lines of the fresh author candidate, including its final assurance and limitation statements.
- **S2:** all 40 logical lines of the adopted necessary-band disposition, including its evidence qualifications and final unpaid-boundary statement.

Binding metadata supplied by parent:

- Manifest SHA256: `411a577260f500a42cfc3e1bce8ee2542c9f13ce8314db847f63be803fa1aa84`.
- Receipt SHA256: `a6a781949463640cfc1e06f3515cface82bccbca23e345d94173c1520e365227`.
- Packet SHA256: `6730aaf860ba610df4b4effd87ebcd36d31a234a595954f874abc704d466411a`.
- Parent-observed metadata clock: `2026-10-30T13:39:14-0700 PDT`.

These are **parent observations**, not my independently executed hashes, a child-native start/completion clock, or evidence of continuous supervision.

All mathematical checking below is written algebra from the frozen packet. I used no scientific execution, CAS, interpreter, solver, enumeration, numerical integration, or new selected parameter/geometry instance. The rational evaluations concern only instances explicitly prescribed in S1. I did not follow scientific links, read author code or sibling returns, or use held episodes or their consumers. Author chronology and no-execution statements are not independently certified by this review.

## 2. Exact imports and acceptance boundary

The retained model and named imports are:

1. The normalized full geometric law
   \[
   \Pr(G=k)=(1-b)b^k,\qquad m=\frac b{1-b},
   \]
   with the stated moments and complete all-diamond objectives in S1 LF 35–79.

2. The retained admissibility of the canonical all-diamond family, with radius \(t\ge0\), complete quantities
   \[
   Z_t=2M_2(t),\qquad N_t=\frac23M_4(t),
   \]
   and positive denominator at the competitors used here. This is a **retained canonical-model/feasibility import**, not a new reconstruction of an omitted original-law definition. S2 LF 3 and 25 preserve the canonical qualification and explicitly corroborate the full-law competitor at \(t=1/2\).

3. The conditional actual-attainment/reduction setting: an original global minimum \(V\) is attained and obeys \(1/2<V\le2\), under the named retained imports. This premise is not established afresh.

4. The previously adopted statements
   \[
   \frac7{100}<\alpha<\frac3{40},\qquad m\le\beta,\qquad
   \frac{13}{40}<\beta<\frac{33}{100},
   \]
   and the necessary endpoint classification at \(m=\beta\), exactly as stated in S2 LF 9–21.

No linked proof, prior computational result, historical reviewer body, or original/book source correspondence was imported beyond those stated scopes. In particular, the upper obstruction \(\beta\) is a **named prior import**, not a new result of this gate.

## 3. Per-claim dispositions

| Claim | Source LF | Disposition |
|---|---|---|
| Complete normalized moments, quotient, and half-value quartic identity | S1 35–109, 382–389 | **SUPPORTED** in the retained model |
| Two positive critical points, local minimum in \((1/2,3/5)\), and global minimum classification | S1 171–225 | **SUPPORTED** |
| Strict parameter monotonicity and continuous strictly increasing minimum | S1 230–251 | **SUPPORTED** |
| Exact opposite signs at the prescribed \(m_-\), \(m_+\), \(t_0\) | S1 255–328 | **SUPPORTED** |
| Unique isolated pair, global nonnegativity, and double-root factorization at \(\gamma\) | S1 113–135, 330–357 | **SUPPORTED** |
| Strict strengthening \(\alpha<223/3000<\gamma\) | S1 359–377 | **SUPPORTED** |
| Actual feasible-competitor exclusion and \(\gamma<m\le\beta\) | S1 380–422 | **SUPPORTED**, conditional on the exact retained feasibility/actual-value imports |
| Transformation to the stated \(b\)-bounds | S1 143–165 | **SUPPORTED** |
| Entire fixed-scalar canonical-strip certificate | S1 424–669 | **INCONCLUSIVE in this gate; outside complementary reconstructed scope**, as detailed below |
| Noncircular sufficiency implication, conditional on the strip certificate and independent attainment/localization | S1 671–755 | **SUPPORTED as a conditional implication only** |
| Original-regime existence anywhere in the interval | S1 7, 734–757, 774 | **NOT PROVED**, consistently with the candidate |

There is no REFUTED mathematical claim at the reconstructed necessary-band scope.

## 4. Written reconstruction of the threshold

### 4.1 Full objective and quartic

The stated normalized geometric moments give
\[
M_2(t)=t^2+2mt+m+2m^2
\]
and
\[
M_4(t)=t^4+4mt^3+6(m+2m^2)t^2
 +4(m+6m^2+6m^3)t
 +m+14m^2+36m^3+24m^4.
\]

Subtracting \((3/2)M_2\) gives exactly
\[
\begin{aligned}
K_m(t)={}&t^4+4mt^3+
 \left(6m+12m^2-\frac32\right)t^2\\
&+(m+24m^2+24m^3)t
 +24m^4+36m^3+11m^2-\frac m2.
\end{aligned}
\]

Thus
\[
N_t-\frac12Z_t=\frac23K_m(t),
\qquad
R_t(m)-\frac12=\frac{K_m(t)}{3M_2(t)}.
\]

These identities retain the **complete normalized geometric tail**. No additional factor \(1-b\) belongs outside these expectations.

### 4.2 Critical-point structure

Let
\[
I=\left[\frac7{100},\frac3{40}\right].
\]
The derivatives are
\[
K_m'(t)=4t^3+12mt^2+(12T_2-3)t
 +m+24m^2+24m^3,
\]
\[
K_m''(t)=12t^2+24mt+12T_2-3.
\]

On \(I\), \(K_m''(0)<0\), while
\[
K_m'''(t)=24t+24m>0\qquad(t\ge0).
\]
Consequently \(K_m'\) decreases to one minimum and then increases. The prescribed signs check as
\[
K_m'(0)>0,
\]
\[
K_m'(1/2)=-1+10m+36m^2+24m^3
 \le-\frac{299}{8000}<0,
\]
and
\[
K_m'(3/5)\ge\frac{17099}{125000}>0.
\]

Therefore there are exactly two positive critical points: a local maximum before \(1/2\), and a unique local minimum
\[
s(m)\in(1/2,3/5).
\]
The only global-minimum candidates on \(t\ge0\) are \(0\) and \(s(m)\), and
\[
K_m(0)=m\left(-\frac12+11m+36m^2+24m^3\right)>0.
\]

One can also resolve the endpoint comparison throughout \(I\), without an additional selected instance:
\[
K_m(1/2)-K_m(0)
 =12m^3+15m^2+\frac52m-\frac5{16}
 \le-\frac{569}{16000}<0,
\]
using the already prescribed upper endpoint \(m=3/40\). Since the function is still decreasing at \(1/2\), the local minimum at \(s(m)\) is the **unique global minimum** throughout \(I\).

### 4.3 Strict parameter monotonicity

Direct differentiation gives
\[
\begin{aligned}
\partial_mK_m(t)={}&4t^3+(6+24m)t^2
 +(1+48m+72m^2)t\\
&-\frac12+22m+108m^2+96m^3.
\end{aligned}
\]

For \(m\ge7/100\) and \(t\ge0\), all nonconstant coefficients are positive, and the constant term is at least
\[
-\frac12+22\frac7{100}=\frac{26}{25}.
\]
Thus the claimed strict positivity is valid.

In particular, for
\[
f(m)=\min_{1/2\le t\le3/5}K_m(t),
\]
compactness gives continuity, and the uniform derivative bound gives, for \(m_2>m_1\) in \(I\),
\[
f(m_2)\ge f(m_1)+\frac{26}{25}(m_2-m_1)>f(m_1).
\]
This proves strict increase without assuming differentiability of a minimizing selection.

### 4.4 Prescribed exact sign certificates

At the prescribed
\[
t_0=\frac{21}{40},
\]
written substitution reduces the quartic and its derivative to
\[
K_m(t_0)
 =24m^4+\frac{243}{5}m^3+\frac{10763}{400}m^2
 +\frac{36121}{16000}m-\frac{863919}{2560000},
\]
\[
K_m'(t_0)
 =24m^3+\frac{183}{5}m^2+\frac{4243}{400}m
 -\frac{15939}{16000}.
\]

These give the stated identities:
\[
K_{223/3000}(t_0)
 =-\frac{23195458191}{81000000000000}<0,
\]
\[
K_{119/1600}(t_0)
 =\frac{63277144}{6553600000000}
 >\frac{19}{2000000},
\]
\[
K_{119/1600}'(t_0)
 =\frac{20796776}{4096000000},
\qquad
0<K_{119/1600}'(t_0)<\frac{13}{2500}.
\]

On the whole interval \(1/2\le t\le3/5\),
\[
K_{119/1600}''(t)
 \ge24\frac{119}{1600}\left(1+\frac{119}{1600}\right)
 =\frac{4909464}{2560000}>\frac{19}{10}.
\]
The strong-convexity lower bound therefore implies
\[
K_{119/1600}(t)>
\frac{19}{2000000}
-\frac{(13/2500)^2}{2(19/10)}
=\frac{453}{190000000}>0.
\]

Hence
\[
f(223/3000)<0<f(119/1600).
\]
Continuity and strict increase yield exactly one
\[
\frac{223}{3000}<\gamma<\frac{119}{1600}
\]
with \(f(\gamma)=0\). The critical-point classification gives exactly one corresponding
\[
s_\gamma\in(1/2,3/5).
\]

### 4.5 Global nonnegativity and factorization

At \(m=\gamma\), the endpoint is positive and the unique local/global minimum is zero. Therefore
\[
K_\gamma(t)\ge0\qquad(t\ge0),
\]
with equality only at \(s_\gamma\).

The monic quartic has a double root at \(s_\gamma\), so
\[
K_\gamma(t)
 =(t-s_\gamma)^2
 \left[t^2+(4\gamma+2s_\gamma)t+w_\gamma\right],
\qquad
w_\gamma=\frac{K_\gamma(0)}{s_\gamma^2}>0.
\]
The residual quadratic is strictly positive for \(t\ge0\). This supplies the stated explicit global certificate and excludes any additional nonnegative zero.

### 4.6 Improvement over \(\alpha\)

For the previously adopted polynomial
\[
L(m)=384m^4+768m^3+416m^2+32m-5,
\]
its derivative is positive on \(m\ge0\). Written substitution at the prescribed lower isolating point gives
\[
L(223/3000)
 =\frac{357360169344}{81000000000000}>0.
\]
Since \(L(\alpha)=0\),
\[
\alpha<\frac{223}{3000}<\gamma.
\]
This is a strict improvement, not a relabeling of the prior lower endpoint.

## 5. Consuming-side actual-value argument

The threshold is passed to the actual optimization through a **feasible full objective**, not through a stationary-root interpretation.

For \(0<m\le\alpha\), the already admitted competitor \(t=1/2\) satisfies
\[
K_m(1/2)=\frac{L(m)}{16}\le0.
\]

For \(\alpha<m\le\gamma\), the adopted \(\alpha>7/100\) makes strict parameter monotonicity applicable, and
\[
K_m(s_\gamma)\le K_\gamma(s_\gamma)=0.
\]

In both cases, the retained admissible all-diamond competitor has finite complete numerator and positive complete denominator, so
\[
R_t(m)\le\frac12.
\]
An attained **global** actual minimum must therefore satisfy
\[
V\le R_t(m)\le\frac12,
\]
contradicting the assumed actual cutoff-two condition \(V>1/2\).

This proves
\[
m>\gamma.
\]
Combining it with the exact prior upper import gives
\[
\boxed{\gamma<m\le\beta}.
\]

The consumer distinction is essential:

- At \(m=\gamma\), the constructed competitor has value exactly \(1/2\); it is not thereby proved to be an original global optimizer.
- For \(m>\gamma\), every all-diamond competitor has value greater than \(1/2\), by strict parameter monotonicity. This does **not** exclude a different original competitor of value at most \(1/2\).
- Neither statement proves original attainment or existence of the actual regime.

Finally, \(m\mapsto m/(1+m)\) is strictly increasing, so
\[
\boxed{
\frac{\gamma}{1+\gamma}<b
\le\frac{\beta}{1+\beta}<\frac{33}{133}
}.
\]
The explicit weaker lower consequence is correctly
\[
\boxed{\frac{223}{3223}<b<\frac{33}{133}}.
\]

## 6. Separate treatment of the later strip and sufficiency statements

### Fixed-scalar strip certificate

The complete author body was read, but this gate does **not** independently accept the entire strip theorem in S1 LF 424–669.

The displayed algebra is compatible with its conclusion. In particular:

- \(Q^*-1/2+y^2>0\).
- On the stated strip, \(c\ge1/2\), and
  \[
  d_{1/2}(2c-y,y)\ge d_{1/2}(c,c)
  =D(c)-1/2>0
  \]
  on the displayed negative-part integration range.
- Conditional on the stated complete clipped-value identity, its negative-part integral vanishes and its remaining terms give \(h_c>0\).
- Differentiating the displayed implicit equation for \(q\) gives
  \[
  q'=-\frac{2a+m}{m+2q},
  \]
  and consequently the displayed rounded-branch formula gives
  \[
  F_R'(a)=m(2a+1+2m)+2q(2a+m)>0.
  \]

However, independent reconstruction of the whole canonical minimization and its lower-face branch would require accepting or reconstructing the retained projection and complete derivative identities, including the meanings/sign properties of the \(L,A,B\) terms used in S1 LF 643–649. Those complete model definitions are not supplied in this frozen packet, and scientific source following is forbidden.

Accordingly, the **entire strip certificate is INCONCLUSIVE in this complementary gate**, not REFUTED and not counted as a candidate defect. No blanket acceptance of S1 follows from the supported quartic argument.

### Conditional sufficiency frontier

The logical implication in S1 LF 720–734 is correctly noncircular **if** the strip certificate is independently established:

- At \(m\in[3/10,\beta]\), the imported monotonicity of \(P_m\) and \(P_\beta(t_\beta)=0\) give a feasible complete-law competitor with \(R_{t_\beta}(m)\le2\), strictly below \(2\) for \(m<\beta\).
- Independent attainment/localization of a global optimizer into the stated strip, together with the strip’s fixed-scalar positivity, would give \(V>1/2\).
- Only after those inequalities are obtained does the prior actual-endpoint necessity theorem apply at \(m=\beta\).

Pointwise strip positivity cannot replace attainment or control excluded competitors. The author explicitly leaves those prerequisites unpaid in S1 LF 734–757. Thus the conditional implication is supported, while actual existence remains **NOT PROVED**.

## 7. Final disposition

**Accepted scope of this WRITTEN gate:** the unique global quartic half-value threshold, its prescribed rational isolation and factorization, strict improvement over \(\alpha\), and the resulting necessary parameter band under the exact retained feasibility/actual-attainment imports.

**Not accepted by this gate:** the entire strip theorem, unconditional original attainment/localization, sufficiency of the necessary interval, original-regime existence, all-epsilon value, source equivalence, novelty, independent-family/human/kernel verification, or any rehabilitation of held material.

**Overall correctness: correct at the reconstructed necessary-band scope.**

**Explanation:** The complete normalized competitor objective, global quartic analysis, exact sign certificates, and actual-value consumer establish \(\gamma<m\le\beta\) with the stated strict lower endpoint. The later strip theorem is outside this gate’s reconstructed acceptance scope, and its use remains conditional; no actual-regime existence conclusion is justified or claimed.

**Confidence: 0.98 for the reconstructed necessary-band result.**