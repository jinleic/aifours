# F486 author candidate: necessary parameter bounds from the complete cutoff-two objective

**Status: UNREVIEWED AUTHOR CANDIDATE — written proof, not an existence theorem.**

The result below excludes two genuine parameter classes of the original canonical optimization, conditional on the named reduction and attainment imports. In particular, it strengthens the imported necessary condition \(b<1/3\) to
\[
\boxed{b<\frac{33}{133}},
\]
and gives a sharper implicitly algebraic upper bound, together with a necessary lower bound. These are full-objective exclusions, not assertions that stationary roots are actual optimizers.

## 1. Provenance, chronology, and execution boundary

Before opening the scientific packet, I completely read the manifest, freeze receipt, parent-supplied live metadata, and all ten named permission/status controls through their endings, then sent Main a direct pre-body ACK. I subsequently read the literal packet in the ordered raw windows
\[
1\!-\!20,\ 21\!-\!40,\ 41\!-\!60,\ 61\!-\!80,\ 81\!-\!100,\ 
101\!-\!120,\ 121\!-\!140,\ 141\!-\!160,\ 161\!-\!180.
\]
All new mathematical work below followed that complete read. The dispatch receipt was read afterward as metadata only.

The assigned pins are:

- Manifest: `133e5dc1474cba817b50a7c62a48029135f94222bba2af60ad4a52b554e23cb0`.
- Freeze receipt: `b3fd08bb93c6d276fe60092bcbb5dad9f753e4e28c4e66e0be06be45409f46d0`.
- Literal packet: `5f450e675170087de14c896456d5945ecf03124a119f69a6a6a9d82e3835f75e`.

The matching hashes, byte/LF counts, and clock `2026-10-30T12:17:35-0700 PDT` are **parent observations supplied in `parent-live-metadata-supply-v1.json`**, not my own hashing, scientific execution, or native start time.

The scientific inputs used are exactly the packet’s S1–S3:

1. `info-1-actual-cutoff2-scalar-edge-uniqueness-and-full-value-parent-v1.md`, complete LF 1–61, SHA `4179e3691a8050e64432044bfb928c273086537a3755fbd5b5d4f9c790af3330`.
2. `info-1-actual-cutoff2-binding-core-and-corrected-penalty-parent-v1.md`, complete LF 1–39, SHA `4880cff7e5d64e615aad22c013a591f6fd8b835f7d7991fa8e3ac34cb2a54b06`.
3. `info-1-cutoff2-penalty-sign-correction-parent-outcome-v1.json`, complete LF 1–78, SHA `80ccc5132d9efd6785b58d7ab275c7ee988275304debde570338a846acc4bf23`.

No linked author/reviewer body, external source, sibling scientific return, or held payload/consumer was opened. The historical penalty-sign error remains intact; no unsigned penalty-difference assertion is used.

**Scientific execution: NOTRUN.** No program, CAS, solver, test, build, or numerical integration was run. The rational calculations below are written algebra. No executable code or computational result is claimed. No repository file was written; this is the complete candidate body for Main’s materialization.

## 2. Exact imported scope

Put
\[
m=\frac{b}{1-b},\qquad b=\frac{m}{1+m},\qquad v=m(1+m),
\]
and
\[
\begin{aligned}
T_2&=m+2m^2,\\
T_3&=m+6m^2+6m^3,\\
T_4&=m+14m^2+36m^3+24m^4,\\
\kappa&=\frac13+2v,\qquad Q^*=1+3m+2m^2.
\end{aligned}
\]

The theorem retains the following named imports from S1–S2:

- The corrected canonical fixed-scalar reduction, with positive denominator \(Z\), full signed objective \(H_\lambda=N-\lambda Z\), and its unique signed-value zero.
- An **attained actual** optimum \(V\) satisfying
  \[
  \frac12<V\le2.
  \]
- The actual-optimizer positivity and pruning conclusions.
- Their adopted consequences that every such optimizer satisfies
  \[
  a>0,\qquad c=a+\frac12,\qquad
  D(a):=2a^2+2ma+T_2<V,
  \]
  and necessarily \(m<1/2\).
- The complete geometric-tail normalization and cubic calibration, including the deterministic constant, rather than a core-only surrogate.

These imports are not reproved here and are not asserted unconditionally for every \(b\). In particular, nothing below supplies the missing attainment or original-source equivalence theorem.

## 3. New necessary-bound theorem

Define
\[
L(m)=384m^4+768m^3+416m^2+32m-5.
\]
Let \(\alpha\) be its unique positive zero. Then
\[
\frac7{100}<\alpha<\frac3{40}.
\]

For the upper bound, define
\[
\begin{aligned}
P_m(t)
={}&t^4+4mt^3+(6m+12m^2-6)t^2\\
&+(-8m+24m^2+24m^3)t\\
&+24m^4+36m^3+2m^2-5m.
\end{aligned}
\]

For each \(m\in[3/10,1/3]\), let \(s(m)\) be the unique local-minimum critical point of \(P_m\) in \((1/2,1)\). Equivalently, it is the root in that interval of
\[
s^3+3ms^2+(3m+6m^2-3)s-2m+6m^2+6m^3=0.
\]

There is a unique
\[
\boxed{\beta\in\left(\frac{13}{40},\frac{33}{100}\right)}
\]
such that
\[
P_\beta(s(\beta))=0.
\]

**Claim.** Under the imports in §2, every attained actual cutoff-two optimizer satisfies
\[
\boxed{\alpha<m\le\beta}.
\]
Consequently,
\[
\boxed{
\frac{\alpha}{1+\alpha}<b\le\frac{\beta}{1+\beta}
<\frac{33}{133}.
}
\]

Thus, in particular,
\[
\frac7{107}<b<\frac{33}{133}
\]
is necessary, though substantially less precise than the algebraic bounds.

At the possible upper endpoint \(m=\beta\), actual attainment additionally forces
\[
V=2,\qquad a=\frac{s(\beta)}2,\qquad c=a+\frac12,
\]
and the edge core is strictly on the all-upper, diamond branch.

This does **not** assert that the upper endpoint, or any interior parameter, actually attains the original optimum.

## 4. Complete normalized competitor and the lower exclusion

Let \(G\) have the geometric law
\[
\Pr(G=k)=(1-b)b^k,\qquad k=0,1,\ldots,
\]
and write \(M_j(t)=\mathbb E(G+t)^j\).

The all-diamond canonical competitor with initial diamond radius \(t\) and subsequent radii \(t+k\) has the complete folded quantities
\[
Z_t=2M_2(t)>0,\qquad N_t=\frac23M_4(t).
\]
Its quotient is therefore
\[
R_t(m)=\frac{M_4(t)}{3M_2(t)}.
\]
There is no additional factor \(1-b\) outside these geometric expectations.

Take the actual feasible competitor \(t=1/2\), corresponding to
\[
a=\frac14,\qquad c=\frac34.
\]
This is a competitor in the retained canonical model, not an auxiliary stationary example.

Using
\[
\begin{aligned}
M_2(t)&=t^2+2mt+T_2,\\
M_4(t)&=t^4+4mt^3+6T_2t^2+4T_3t+T_4,
\end{aligned}
\]
gives
\[
M_4(1/2)-\frac32M_2(1/2)
=24m^4+48m^3+26m^2+2m-\frac5{16}
=\frac{L(m)}{16}.
\]

Since \(L'(m)>0\) for \(m\ge0\), \(L\) has exactly one positive zero. The endpoint signs are
\[
L(7/100)=-\frac{350747}{781250}<0,\qquad
L(3/40)=\frac{1523}{20000}>0.
\]

If \(m\le\alpha\), then this complete competitor has \(R_{1/2}(m)\le1/2\). Global minimality would imply \(V\le1/2\), contradicting the imported actual-cutoff-two condition. Hence
\[
m>\alpha.
\]

## 5. Exact global quartic certificate defining \(\beta\)

### 5.1 Critical-point classification

For \(m\in[3/10,1/3]\),
\[
P_m''(t)=12t^2+24mt+12(T_2-1).
\]
Here \(T_2<1\), and \(P_m''\) is strictly increasing on \(t\ge0\), from a negative value to \(+\infty\). Consequently, \(P_m'\) first decreases and then increases.

Moreover,
\[
\begin{aligned}
P_m'(0)&\ge\frac{51}{125}>0,\\
P_m'(1/2)&=24m^3+36m^2+m-\frac{11}{2}
\le-\frac5{18}<0,\\
P_m'(1)&\ge\frac{221}{125}>0.
\end{aligned}
\]
Thus \(P_m\) has exactly two positive critical points: one local maximum in \((0,1/2)\), and exactly one local minimum \(s(m)\in(1/2,1)\).

Its global minimum on \(t\ge0\) is therefore either \(P_m(0)\) or \(P_m(s(m))\).

### 5.2 Strict monotonicity in the physical parameter

At \(m=3/10\),
\[
\partial_mP_m(t)
=4t^3+\frac{66}{5}t^2+\frac{322}{25}t+\frac{1064}{125}>0
\quad(t\ge0).
\]
Also
\[
\partial_m^2P_m(t)
=24t^2+(48+144m)t+4+216m+288m^2>0
\]
for \(t\ge0,\ m\ge3/10\).

Hence \(P_m(t)\) is strictly increasing in \(m\), uniformly on \(t\ge0\). In particular,
\[
f(m):=P_m(s(m))
=\min_{1/2\le t\le1}P_m(t)
\]
is continuous and strictly increasing on \([3/10,1/3]\).

### 5.3 Opposite exact signs

The identity obtained by putting \(u=m-1/3\) is
\[
P_m(t)=\frac{W(t)}{27}+uJ(t)+u^2B(t)+u^3C(t)+24u^4,
\]
where
\[
\begin{aligned}
W(t)&=27t^4+36t^3-72t^2+24t+5,\\
J(t)&=4t^3+14t^2+16t+\frac{107}{9},\\
B(t)&=12t^2+48t+54,\\
C(t)&=24t+68.
\end{aligned}
\]

At the lower bracket,
\[
P_{13/40}(2/3)
=-\frac{1508857}{25920000}<0,
\]
so \(f(13/40)<0\).

For the upper bracket, the degree-four Bernstein coefficients of \(W\), with each interval affinely mapped to \([0,1]\), are:

| Interval | Bernstein coefficients |
|---|---|
| \([0,1/2]\) | \(5,\ 8,\ 8,\ 49/8,\ 83/16\) |
| \([1/2,1]\) | \(83/16,\ 17/4,\ 17/4,\ 8,\ 20\) |

The Bernstein basis is nonnegative and sums to one. Therefore
\[
W(t)\ge\frac{17}{4}\qquad(0\le t\le1).
\]

At \(m=33/100\), \(u=-1/300\). On \(0\le t\le1\),
\[
J(t)\le\frac{413}{9},\qquad B(t)\ge0,\qquad C(t)\le92,
\]
and hence
\[
\begin{aligned}
P_{33/100}(t)
&\ge \frac{17}{108}-\frac{413}{2700}
-\frac{92}{27000000}\\
&=\frac{29977}{6750000}>0.
\end{aligned}
\]
In particular, \(f(33/100)>0\).

Continuity and strict monotonicity now prove the stated existence and uniqueness of \(\beta\).

### 5.4 Positivity over every \(t\ge0\), not merely near the critical root

At the lower bracket,
\[
P_{13/40}(0)=\frac{28743}{320000}>0.
\]
Parameter monotonicity gives \(P_\beta(0)>0\). The critical-point classification and \(f(\beta)=0\) therefore show
\[
P_\beta(t)\ge0\quad(t\ge0),
\]
with exactly one zero, namely \(t=s(\beta)\).

Strict parameter monotonicity then gives the global certificate
\[
\boxed{P_m(t)>0\quad\text{for every }t\ge0\text{ whenever }m>\beta.}
\]

This is a global quartic statement, not selection of a favorable local root.

## 6. Why the quartic excludes the rounded core as well

The preceding quartic describes the all-upper branch. To obtain an actual-optimization exclusion, the other possible clipping branch must also be covered.

Suppose an actual optimizer has \(m\ge\beta\). The imported necessary bound gives \(m<1/2\); thus
\[
\frac3{10}<m<\frac12.
\]
In this range,
\[
T_2<1,\qquad Q^*>2.
\]

Let
\[
R(a)=4a^2+4ma+T_2,
\]
and define \(a_R,a_D>0\) uniquely by
\[
R(a_R)=2,\qquad D(a_D)=2.
\]
Then
\[
a_R<a_D,\qquad \frac14<a_R<\frac12.
\]
Indeed, \(R(1/4)<2\) for \(m<1/2\), while \(R(1/2)=Q^*>2\).

The actual scalar obeys \(D(a)<V\le2\), so \(a<a_D\).

### 6.1 The complete fixed-scalar objective at \(\lambda=2\)

Write \(e_2(a)=h(a,a+1/2;2)\).

The active-core projection remains legitimate at this fixed scalar, not because \(2\) is presumed to be the actual value, but because
\[
Q^*-2>0.
\]
The slack-tail derivative is bounded below by \(Q^*-2+y^2>0\); thus slack is removed. The remaining pooled core derivative is
\[
d(x,y)=(x+m)^2+v+y^2-2.
\]
Its strictly convex primitive has derivative \(d\), so the minimizing core is
\[
F_0(y)=\operatorname{clip}\!\left(
\sqrt{2-v-y^2}-m,\ [a,2a-y]\right),
\qquad F_1=F_0+1.
\]

Because \(D(a)<2\), the lower face is inactive throughout the shared core. The free profile has slope in \([-1,0]\), joins the upper face continuously, and joins the fixed edge corner. Thus this is the global canonical fixed-scalar projection supplied by the retained reduction, not an inadmissible independent-height perturbation.

For completeness, put
\[
U=2a-y,\qquad r=\sqrt{2-v-y^2}-m,
\]
and let \(q>0\) solve
\[
2=D(a)+2mq+2q^2,\qquad \tau=\min(a,q).
\]
The full value is
\[
\begin{aligned}
e_2(a)
={}&\frac23M_4(2a)-4M_2(2a)\\
&-8\int_0^{a-\tau}(U-r)^2
\left(\frac{U+2r}{3}+m\right)\,dy.
\end{aligned}
\]
The first line retains the complete geometric tails and normalization. The integral is exactly the pooled cubic improvement, using
\[
\psi(U,y)-\psi(r,y)
=(U-r)^2\left(\frac{U+2r}{3}+m\right).
\]
No tail constant has been discarded.

### 6.2 All-upper branch

For \(0\le a\le a_R\), the integral vanishes, and
\[
\boxed{e_2(a)=\frac23P_m(2a).}
\]

### 6.3 Rounded branch is strictly increasing

For \(a_R<a<a_D\), \(0<q<a\). Exact differentiation of the same complete value gives
\[
\frac{e_2'(a)}{16}
=F_R(a)
=m\!\left[a^2+(1+2m)a+\kappa-1\right]
-mq^2-\frac43q^3.
\]
Implicit differentiation yields
\[
q_a=-\frac{2a+m}{m+2q},
\]
and therefore
\[
F_R'(a)
=m(2a+1+2m)+2q(2a+m)>0.
\]

At the joining point \(q=a_R\), use \(2=R(a_R)\) to obtain
\[
F_R(a_R)
=m\!\left(\frac13+\frac32m+m^2\right)
+ma_R-2ma_R^2-\frac43a_R^3.
\]
Since \(0<a_R<1/2\),
\[
\begin{aligned}
F_R(a_R)
&\ge m\!\left(\frac13+\frac32m+m^2\right)-\frac16\\
&\ge\frac{131}{500}-\frac16
=\frac{143}{1500}>0.
\end{aligned}
\]

Thus \(e_2\) is strictly increasing throughout the rounded interval. It cannot obtain a lower value there than at its all-upper joining point.

## 7. Contradiction with actual attainment; endpoint identification

Let \(\sigma\) be the assumed actual optimizing profile at its actual scalar \(a\). Since
\[
H_V(\sigma)=0,\qquad Z(\sigma)>0,
\]
the same admissible profile satisfies
\[
H_2(\sigma)=-(2-V)Z(\sigma)\le0.
\]
Fixed-scalar minimization consequently implies
\[
\boxed{e_2(a)\le0.}
\]

If \(m>\beta\), §5 gives \(P_m(t)>0\) for every \(t\ge0\). Therefore \(e_2(a)>0\) throughout the all-upper interval. Section 6 shows that it remains strictly positive on the rounded interval. This covers every possible actual \(a<a_D\), contradicting \(e_2(a)\le0\).

Hence
\[
m\le\beta.
\]

At \(m=\beta\), the all-upper value is nonnegative and has its unique zero at \(a=s(\beta)/2\). This zero lies strictly before \(a_R\): the minimum satisfies \(s(\beta)\in(1/2,1)\), while
\[
P_\beta'(2a_R)=12F_R(a_R)>0,\qquad 2a_R>\frac12.
\]
The critical-point classification therefore gives \(s(\beta)<2a_R\). In particular, the rounded joining value is strictly positive.

Thus actual attainment at \(m=\beta\) forces
\[
a=\frac{s(\beta)}2,\qquad c=a+\frac12.
\]
If \(V<2\), the displayed inequality would strengthen to \(e_2(a)<0\), impossible. Hence \(V=2\). Since \(a<a_R\), the core is strictly on the diamond branch.

This proves all claims in §3.

## 8. Exact achievement and remaining original obligations

**Established here as an unreviewed written candidate:**

- A genuine normalized canonical competitor excludes \(m\le\alpha\).
- A global polynomial certificate, together with the complete rounded-core objective, excludes every \(m>\beta\).
- The possible upper endpoint has a necessary value and clipping classification.
- The explicit consequence is \(b<33/133\), improving the imported \(b<1/3\).

**Not established:**

- Actual attained cutoff-two optimization at any parameter.
- Sufficiency anywhere in the necessary band \(\alpha<m\le\beta\).
- Global comparison against every canonical competitor for an existence claim.
- The actual value or clipping branch throughout that band.
- Unconditional attainment/pruning, an all-\(\epsilon\) formula, unreduced-law uniqueness, original book/source equivalence, or novelty/priority.

The interval between the necessary bounds is nonempty as an algebraic interval; **that is not evidence that the actual regime is nonempty**.

No human, independent-family, formal-kernel, or new independent-check acceptance is claimed. The candidate requires disjoint checking and parent disposition before adoption.