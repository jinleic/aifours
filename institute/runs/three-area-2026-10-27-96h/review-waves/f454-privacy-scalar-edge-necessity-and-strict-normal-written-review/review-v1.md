# F454 WRITTEN review — scalar-edge necessity and strict normal

**Assigned-scope result: SUPPORTED, conditional on the stated upstream imports.**  
**Candidate findings at this scope: 0 FATAL / 0 MAJOR / 0 MINOR.**  
This is a written-review return, not parent adoption or acceptance of the complete F438 manuscript.

## 1. Binding, chronology and methods

Wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f454-privacy-scalar-edge-necessity-and-strict-normal-written-review/`

Parent-supplied bindings:

- Manifest: `9a10c592d82cc0061317be7384dfb96683ff08394d741e0a779def4445f91334`
- Freeze receipt: `429e9ca45d6bd8805b93031a0eef7c4e38f286bfdda6f3565537383bdad57dc2`
- Literal packet: `f68394e5c4157c2dfeaa4dd8be4ade1c47c874700c169be5f06dc3cb1a5f7dcf`

The clock `2026-10-30T11:39:34-0700 PDT`, hash matches, byte counts and LF observations are **parent-attributed metadata**, not child-native execution, start or completion observations.

I read the complete manifest, freeze receipt, dispatch receipt, parent metadata supply and every listed status-only control before sending the direct administrative pre-body ACK. I then read the entire 1128-LF literal packet, in order, in contiguous raw windows of at most 20 LF, including its final window 1121–1128. This covered:

- S1: all logical source lines 1–1049;
- S2: lines 1–39;
- S3: lines 1–38.

Mathematical reconstruction began only after that complete packet read.

**Administrative correction:** The ACK described the parent metadata file as ending at LF104; its closing brace is at logical line105. The actual pre-ACK read included the complete 101–120 window and therefore already included that brace. I sent an additive correction to Main. This was a reviewer metadata-label transcription error, not an omitted ending, late ACK or candidate mathematical defect.

Methods were formal-parameter written algebra and differentiation. I did not instantiate a new mathematical example, privately or publicly, and did not use §10’s author example as a diagnostic. No scientific executable, code, interpreter, CAS, solver, enumeration, replay, author program, external model, build, test, lint or formatter was used. There is therefore no scientific argv, executed output or finite-check PASS to report.

F439, F444, F448, the held privacy auxiliary episode, held CORE material, held AME material and held PHv8/cp116 material and their consumers remained **HELD/ZERO/NONINPUT**. Only their designated status controls were read. No excluded scientific link, sibling review or new scientific source was opened.

The governing role is read-only. This complete body is returned for parent materialization; no repository write or write bypass was attempted.

## 2. Exact review scope and imports

The assigned claims are:

1. The complete signed functional and scalar derivatives, including all tail weights, pooled constants, moving endpoints and one-sided edge terms.
2. The necessary inequality \(V>D(a)\).
3. Exclusion of every scalar-interior actual optimizer.
4. Strict positivity of the actual edge normal.

The following remain **conditional upstream imports**, not newly proved here:

- \(b\in(0,1)\), \(m=b/(1-b)>0\);
- the corrected canonical feasible-profile reduction and its unique fixed-scalar minimizing profiles;
- an attained actual-cutoff-two reduction with
  \[
  \frac12<V\le2,\qquad V=\min_K\rho(a,c);
  \]
- equivalently at this \(V\),
  \[
  h(a,c;V)\ge0\quad((a,c)\in K),
  \]
  with equality at an actual optimizing pair;
- actual-optimizer positivity and pruning:
  \[
  a>0,\qquad u:=a+\tfrac12\le c<a+1;
  \]
- the feasible diamond comparison \(V\le T_4/(3T_2)\);
- S2’s already-scoped whole-core binding and corrected penalty statements.

The positivity import excludes \(a=0\) from the actual optimizer considered here; this review does not derive vertex exclusion afresh. Likewise, \(c<a+1\) is retained at its pruning-import scope, not silently proved from the derivative argument.

No exact Clarke interchange, stationarity sufficiency, ordinary-directional/Clarke equivalence or original-source equivalence is assumed.

## 3. Per-claim disposition

| Claim | Source location | Result |
|---|---|---|
| Full \(N,Z,H_\lambda\), tail derivative and pooled constant | S1:91–153, 214–252 | **SUPPORTED**, as identities for the displayed conditional object |
| Scalar derivative formulas (5.1)–(5.2), including edge meanings | S1:323–394 | **SUPPORTED** |
| Every actual optimizer satisfies \(V>D(a)\) | S1:396–410 | **SUPPORTED** |
| Interior Case I has \(h_c>0\) | S1:418–431 | **SUPPORTED** |
| Interior Case II has a feasible negative-curvature direction at every stationary point | S1:433–524 | **SUPPORTED** |
| Every actual optimizer lies on \(c=a+\tfrac12\) | S1:526–528 | **SUPPORTED**, conditional on the imports |
| Every actual edge optimizer has \(h_c^+>0\) | S1:531–543 | **SUPPORTED**, by the one-sided argument below |
| Scalar uniqueness, sharper value bound, full value equation and example | S1:547–994 | **INCONCLUSIVE in this review: outside the assigned audit**, not refuted |
| Actual-regime existence or a uniform endpoint-difference sign | S1:319, 1016–1036 | **Not established and not claimed by this review** |

## 4. Full-functional reconstruction

Write
\[
v=m(1+m),\qquad
T_2=m+2m^2=m^2+v,
\]
with \(T_3,T_4\) as in S1.

From the displayed definitions of \(A,Q,B,N,Z\),
\[
H_\lambda=N-\lambda Z
\]
has core term
\[
8(1-b)\int_0^a\psi_0(F_0,y;\lambda)\,dy
\]
and tail term
\[
8b\int_0^c\psi_1(F_1,y;\lambda)\,dy+bC(c;\lambda).
\]

In particular, the contribution \(T_2A(F_1)\) is
\[
8T_2\int_0^c(F_1-y)\,dy.
\]
Its \(-8T_2\int_0^c y\,dy=-4c^2T_2\) combines with the displayed deterministic \(8c^2T_2\), leaving
\[
C(c;\lambda)
=
4c^2T_2+\frac{16}{3}cT_3+\frac23T_4
-\lambda(8cm+2T_2).
\]
Thus the \(4c^2T_2\) in \(C\) is correct; no tail contribution was omitted.

The remaining integrand derivative is
\[
d_\lambda(z,y)
=
z^2+2mz+T_2+y^2-\lambda
=
(z+m)^2+v+y^2-\lambda,
\]
and
\[
\partial_zd_\lambda=2(z+m)>0\qquad(z\ge0).
\]
This gives the stated nonnegative-root convention, including a nonpositive radicand or a root clipped to zero.

The denominator bound
\[
Z\ge2bT_2>0
\]
also retains its stated full-functional meaning.

### Active core and pooled constant

The manuscript’s strict bound \(V<Q_*\), with
\[
Q_*=1+3m+2m^2,
\]
follows from the displayed diamond comparison and its two formal parameter ranges:

- for \(0<m\le1/3\),
  \[
  Q_*-\frac{T_4}{3T_2}
  =
  \frac{2+m-12m^2-12m^3}{3(1+2m)}>0;
  \]
- for \(m\ge1/3\), \(Q_*\ge20/9>2\ge V\).

Consequently \(d_V(z,y)>0\) whenever \(z\ge1\). In the actual strip, for every admissible core \(x\),
\[
x+1\ge a+1>c,\qquad
x+1\le2a+1-y\le2c-y.
\]
Thus \(x+1\) is the feasible conditional tail minimum.

Using \(b(1+m)=m\), direct coefficient cancellation gives
\[
(1-b)\psi_0(x,y;\lambda)+b\psi_1(x+1,y;\lambda)
=
\psi_1(x,y;\lambda)+b(\kappa-\lambda),
\]
where
\[
\kappa=\frac13+2v.
\]
The constant \(b(\kappa-\lambda)\) is retained below, including in the moving-endpoint calculation.

Hence, at the fixed \(\lambda=V\),
\[
F_0=f_a=\operatorname{clip}(r_V,[a,2a-y]),\qquad F_1=f_a+1
\]
on the shared core, and
\[
F_1(y)=\operatorname{clip}
\bigl(r_V(y),[\max(c,2a+1-y),\,2c-y]\bigr)
\]
on \([a,c]\).

These selections are canonical. A selected positive root has slope
\[
-\frac{y}{r_V(y)+m}\in[-1,0],
\]
because its selected coordinate is at least \(y\). The other branches have slope \(0\) or \(-1\). The endpoint values agree: \(f_a(a)=a\), the tail starts at \(a+1\), and it ends at \(c\). The split at the changing floor also has equal values on both sides.

## 5. Reconstruction of both scalar derivatives

Fix \(b,V\), and put
\[
k(y)=2a+1-y,\qquad s=2a+1-c.
\]
In the actual strip,
\[
a<s\le u\le c.
\]
Define
\[
A=\int_0^a[-d_V(2a-y,y)]_+\,dy,
\]
\[
L=\int_0^a[d_V(a,y)]_+\,dy,
\]
\[
B=\int_a^s[d_V(k(y),y)]_+\,dy.
\]

### The \(a\)-derivative

The core lower face has speed one and contributes \(L\). Its upper face has speed two and contributes \(-2A\). On the tail interval where the floor is \(k\), that floor has speed two and contributes \(2bB\).

The moving shared endpoint cancels exactly. In the original form this is
\[
(1-b)\psi_0(a,a)+b\psi_1(a+1,a)-b\psi_1(a+1,a)=0,
\]
because \(\psi_0(a,a)=0\).

Equivalently, in pooled form the cancellation is
\[
\psi_1(a,a)+b(\kappa-V)-b\psi_1(a+1,a)=0.
\]
This explicitly retains the derivative of the pooled constant; it is not discarded.

Therefore
\[
\boxed{\frac{h_a}{16}=\frac12L-A+bB.}
\]
At \(c=u\), this is the partial derivative obtained from feasible decreasing \(a\) at fixed \(c\).

### The \(c\)-derivative

The lower tail face \(c\), on \([s,c]\), has speed one. The upper tail face \(2c-y\) has speed two. Their contributions are
\[
\int_s^c[d_V(c,y)]_+\,dy
-
2\int_a^c[-d_V(2c-y,y)]_+\,dy.
\]

The moving diagonal endpoint contributes
\[
\psi_1(c,c)=2mc^2+T_2c.
\]
The deterministic term contributes
\[
\frac{C'(c;V)}8=cT_2+\frac23T_3-mV.
\]
Their sum is
\[
D_0(c)=2cT_2+2mc^2+\frac23T_3-mV.
\]

Thus
\[
\boxed{
\frac{h_c}{8b}
=
D_0(c)
+\int_s^c[d_V(c,y)]_+\,dy
-2\int_a^c[-d_V(2c-y,y)]_+\,dy.
}
\]
At \(c=u\), this is the right derivative.

The moving split \(s\) contributes no residual endpoint term because its two profile formulas have the same value there. The same principle handles the other moving joins.

These first-derivative formulas do not require differentiating a singular square root. They use polynomial positive/negative parts. At a root/face tie the coordinate derivative is zero; collapsed diagonal boxes occur only at the endpoint. Bounded difference quotients on the finite intervals and the matching interface values justify differentiation, including the indicated one-sided edge limits.

## 6. Necessary exclusion of a lower-face core

Let
\[
D(t)=2t^2+2mt+T_2.
\]
On \(0\le y\le a\),
\[
q_a(y):=(2a-y+m)^2+v+y^2
\]
satisfies
\[
q_a'(y)=4y-4a-2m<0,\qquad q_a(a)=D(a).
\]
Therefore \(V\le D(a)\) would imply \(A=0\).

But \(s-a=a+1-c>0\), and
\[
d_V(k(a),a)=d_V(a+1,a)>0
\]
by \(V<Q_*\). Continuity then gives \(B>0\). Hence the derivative formula yields \(h_a>0\).

A sufficiently small decrease of \(a\) at fixed \(c\) remains feasible: \(a\) remains positive, \(c\ge a+\tfrac12\) is preserved, and the strict margin \(c<a+1\) persists. This displacement decreases \(h\), contradicting actual minimality.

Consequently,
\[
\boxed{V>D(a).}
\]
Moreover,
\[
d_V(a,y)\le d_V(a,a)=D(a)-V<0
\]
on the core, so \(L=0\). A positive-length lower-face core is excluded.

## 7. Exclusion of every scalar-interior optimizer

Suppose an actual optimizer has \(c>u\).

### Case I: \(V\le D(c)\)

On \([a,c]\), the upper-face threshold
\[
(2c-y+m)^2+v+y^2
\]
is decreasing and has minimum \(D(c)\) at \(y=c\). Therefore the negative-part integral in \(h_c\) vanishes.

Also,
\[
D_0(c)
=
m(D(c)-V)+2cv+K_m,
\]
where
\[
K_m=\frac23T_3-mT_2
=\frac23m+3m^2+2m^3>0.
\]
The remaining integral in \(h_c\) is nonnegative. Thus
\[
h_c>0,
\]
contradicting stationarity at an interior minimum.

### Case II: \(V>D(c)\)

Since \(c>u>1/2\) and \(V\le2\), the inequality implies
\[
m<\frac12,\qquad c<1,\qquad 0<a<\frac12.
\]
Indeed \(m\ge1/2\) would force \(D(c)>2\), while \(D(c)>2c^2\) forces \(c<1\).

Put
\[
R(a)=4a^2+4ma+T_2.
\]
Then
\[
D(u)-R(a)=\frac12+m+2a(1-a-m)>0.
\]
Since \(D\) is strictly increasing,
\[
V>D(c)>D(u)>R(a).
\]
The core is therefore strictly upper-face throughout:
\[
f_a(y)=2a-y.
\]

#### Corner root and exact integrals

The corner function
\[
g(y)=d_V(k(y),y)
\]
is positive at \(a\), negative at \(u\), and strictly decreasing on \([a,u]\), because
\[
g'(y)=4y-2(2a+1+m)\le-2m<0.
\]
It has one simple zero \(y=a+\ell\), with \(0<\ell<1/2\).

At \(y=s\),
\[
g(s)=d_V(c,s)<D(c)-V<0,
\]
so
\[
a+\ell<s.
\]
Thus neither the upper endpoint \(s\) nor its speed contributes to differentiating \(B\) locally.

Direct integration gives
\[
A=a(V-T_2)-3ma^2-\frac83a^3.
\]
Writing \(y=a+t\), the corner polynomial has the form
\[
g(a+t)=C_*-2(1+m)t+2t^2,
\]
with its zero imposing
\[
C_*=2(1+m)\ell-2\ell^2.
\]
Therefore
\[
B=(1+m)\ell^2-\frac43\ell^3.
\]

At an interior stationary point, \(L=0\) and \(h_a=0\), so
\[
A=bB.
\]
But \(V>D(u)\) gives
\[
A>
a\Bigl(\frac12+m\Bigr)
+a^2\Bigl(2-m-\frac23a\Bigr)
>
a\Bigl(\frac12+m\Bigr),
\]
whereas
\[
bB<b(1+m)\ell^2<\frac m4.
\]
Consequently,
\[
\boxed{a<\frac{m}{2+4m}<\frac18.}
\]

#### Implicit-root derivative and curvature

At fixed \(c,V\), differentiation of the corner-root equation gives
\[
\ell_a=\frac{2a+1+m}{1+m-2\ell}.
\]
Its denominator is positive. Since
\[
\frac{d}{d\ell}
\left((1+m)\ell^2-\frac43\ell^3\right)
=
2\ell(1+m-2\ell),
\]
we obtain
\[
\boxed{B_a=2(2a+1+m)\ell.}
\]

Thus
\[
\frac{h_{aa}}{16}
=
-V+T_2+6ma+8a^2
+2b(2a+1+m)\ell.
\]
Using \(V>D(u)\), \(\ell<1/2\) and \(b(1+m)=m\),
\[
\frac{h_{aa}}{16}
<
6a^2+(4m-2+2b)a-\frac12.
\]
Now \(m<1/2\), \(b<1/3\), \(a<1/8\), and hence
\[
\frac{h_{aa}}{16}
<
\frac6{64}+\frac1{12}-\frac12
=
\boxed{-\frac{31}{96}<0}.
\]

At a scalar-interior point, sufficiently small changes of either sign in \(a\) at fixed \(c\) remain feasible. Therefore this strictly negative second derivative at a stationary point contradicts local minimality.

Both cases are excluded. Accordingly,
\[
\boxed{c=a+\tfrac12}
\]
for every actual optimizer at the stated conditional scope.

## 8. Strictness of the actual edge normal

Now take an actual optimizer on \(c=u\).

The feasible upward vertical ray gives
\[
h_c^+\ge0.
\]
Because \(a>0\), both directions along the edge are feasible, so the ordinary edge derivative is zero.

Here the equality between the edge derivative and the sum of partial derivatives can be checked directly, without a Clarke chain rule. On the edge, the tail is \(k(y)=2u-y\). Its tangential coordinate speed is two regardless of the sign of \(d_V(k(y),y)\). Using
\[
[d]_+-[-d]_+=d,
\]
the two scalar formulas give
\[
\frac{h_a+h_c^+}{8}
=
L-2A
+2b\int_a^u d_V(2u-y,y)\,dy
+bD_0(u).
\]
Direct edge differentiation gives this same expression. Hence
\[
h_a+h_c^+=0.
\]

If \(V\le D(u)\), Case I already proves \(h_c^+>0\).

Otherwise \(V>D(u)\). Suppose \(h_c^+=0\). Then \(h_a=0\), and all the Case II calculations apply:

- \(m<1/2\), \(a<1/2\);
- \(V>D(u)>R(a)\), so the core is strictly upper-face;
- the simple corner root lies strictly before \(s=c=u\);
- \(A=bB\), giving \(a<1/8\);
- the feasible-side second derivative satisfies
  \[
  h_{aa}/16<-31/96.
  \]

The strict root/interface gaps persist under a sufficiently small decrease of \(a\) at fixed \(c\). Therefore the same smooth formula applies on that feasible side. With \(h_a=0\),
\[
h(a-\varepsilon,c;V)
=
h(a,c;V)
+\frac{\varepsilon^2}{2}h_{aa}
+o(\varepsilon^2)
<
h(a,c;V)
\]
for sufficiently small positive formal \(\varepsilon\).

This contradicts actual minimality. Thus
\[
\boxed{h_c^+>0,\qquad h_a=-h_c^+<0,\qquad h_a+h_c^+=0.}
\]

This proves the claimed strict normal at actual optimizers. It does not prove a uniform sign of the edge derivative at arbitrary scalar pairs.

## 9. Findings, retained history and assurance ceiling

### New candidate findings

**0 FATAL / 0 MAJOR / 0 MINOR** within the explicitly assigned derivative, interior-exclusion and strict-normal scope.

The edge continuation requires replacing the interior chain \(D(c)>D(u)\) by equality \(D(c)=D(u)\); the proof still has the necessary strict inequality \(V>D(u)\). Likewise, at the edge \(g(s)=D(c)-V<0\), rather than being strictly less than \(D(c)-V\). These are valid specializations of the argument, not defects.

### Retained historical finding

The old f400/f418 unsigned penalty assertion remains incorrect, and the historical f419 **1 MAJOR** remains recorded. This review neither erases nor retroactively clears it. The retained corrected statement is
\[
P(a,c;\lambda)-P(a,u;\lambda)\le0.
\]
That statement alone does not determine the sign of the full endpoint difference.

### Boundaries

This review does **not** establish:

- actual-regime existence for any parameter;
- scalar uniqueness or the later §7 value bounds;
- the §9 full-value formula or §10 example arithmetic;
- sufficiency of arbitrary stationary/value-zero candidate equations;
- uniform global edge dominance;
- uniqueness of every unreduced law or representation;
- source/book equivalence, priority or novelty;
- human, independent-model-family, formal/kernel or finite-execution verification.

The complete F438 manuscript remains an author candidate requiring the other independently assigned gates and parent disposition.

**overall_correctness: correct**

**explanation:** The assigned scalar-derivative, interior-exclusion and strict-edge-normal arguments reconstruct correctly at the stated conditional actual-cutoff-two scope. All deterministic, pooled and moving-endpoint terms are retained, and the edge conclusion follows from a feasible one-sided second-order descent rather than a Clarke interchange or stationarity-sufficiency claim. This verdict does not adopt the manuscript’s unassigned uniqueness, value or existence claims.

**confidence: 0.97**