# F455 — WRITTEN review: conditional scalar uniqueness, clipping and value

**Overall correctness:** correct within the conditional scope stated below.  
**Explanation:** The scalar-edge exclusion, strict normality, uniqueness argument, clipping transitions and full value equation withstand written reconstruction. The assigned example satisfies the candidate equations, but neither it nor this review establishes actual-regime existence or global optimality.  
**Confidence:** 0.96.

**New findings:** **0 FATAL / 0 MAJOR / 0 MINOR.**  
**Historical finding retained:** the earlier **1 MAJOR** concerning the unsigned coupling-penalty assertion remains unchanged; this review does not retrospectively clear f400 or f418.

**Disposition:** scoped written support, returned for Main’s materialization. No repository file was written, and no parent adoption, original-target acceptance, independent-family review, human review, kernel verification or novelty judgment is asserted.

## 1. Binding, chronology and methods

The reviewed wave is:

`f455-privacy-conditional-scalar-uniqueness-clipping-and-value-written-review`

The following bindings and observation are **parent-attributed metadata**, not hashes or clocks executed by this reviewer:

- Manifest SHA256: `8215c1212e7e6fe8e93537fb96ce615754d473df80c19c12bebc310e5d7a9bdb`.
- Freeze-receipt SHA256: `373cbc0cb01add89e60f959add9fca8c87e2d24d2afccd9dce4ea554de0e0a40`.
- Literal-packet SHA256: `55a676c8ff4fa8a26a95c1de49104dfd7be1565ae71d56b8e08863eca76fb8e9`.
- Parent observation: `2026-10-30T11:39:34-0700 PDT`.

Before mathematical packet access, I completely read the manifest, freeze receipt, parent metadata supply and all ten listed status-only controls, including their endings. I then sent Main an administrative **WRITTEN pre-body ACK** expressly accepting the method and exclusion boundaries.

After that ACK, I read the complete literal packet in consecutive raw windows of at most 20 LF:

\[
1\!-\!20,\ 21\!-\!40,\ldots,\ 1141\!-\!1160,\ 1161\!-\!1168.
\]

One mistyped path for window 641–660 returned “not found”; I corrected the path and read that exact window before continuing. No source-body portion was skipped or elided. Coverage includes:

- **S1:** complete author body through logical line 1049; parent metadata records 1048 LF.
- **S2:** complete disposition through line 39.
- **S3:** complete correction outcome through line 78.

Mathematical reconstruction began only after the complete packet read.

Methods were written algebra with formal parameters, plus written checking of the **explicitly assigned author example** \(m=1/10\) and its stated quintic-root interval and endpoints. No additional chosen mathematical instance was introduced. No scientific program, interpreter, CAS, solver, enumeration, replay, author program, external-model CLI, build, test, lint or formatter was run. Consequently, there is **no scientific argv, executed output or finite-check receipt** to report.

No linked prior-review body, sibling return, new scientific source or excluded scientific payload was opened. F439/F444/F448 and all their consumers, the held privacy auxiliary episode, CORE material, AME material and PHv8/cp116 remained **HELD/ZERO/NONINPUT**. Controls supplied status and exclusions only. This is an access-and-method disclosure, not a cognition certificate.

## 2. Exact mathematical scope and imports

The following remain imports rather than newly established original-problem facts:

1. The corrected canonical fixed-scalar minimization framework, including fixed-scalar profile uniqueness, the complete signed functional \(h(a,c;\lambda)\), its positive denominator and its unique value zero \(\rho(a,c)\).
2. The **actual-cutoff-two hypothesis** and attained reduction
   \[
   \frac12<V\le2,\qquad V=\min_{(a,c)\in K}\rho(a,c),
   \qquad K=\{a\ge0,\ c\ge a+\tfrac12\}.
   \]
   In particular, \(h(a,c;V)\ge0\) throughout \(K\), with equality at an actual optimizer.
3. Actual-optimizer positivity and pruning:
   \[
   a>0,\qquad a+\tfrac12\le c<a+1,
   \]
   together with the stated interior pruning implication.
4. The feasible diamond comparison and the adopted whole-binding-core/canonical-profile scope recorded in S2. S2 does **not** prepay edge necessity, scalar-pair uniqueness, strict normality or a global value theorem.
5. The corrected penalty statement, at its exact universal scope:
   \[
   P(a,c;\lambda)-P(a,a+\tfrac12;\lambda)\le0.
   \]
   This statement alone does not sign the full endpoint difference.

I do not import rejected P3 sufficiency, an exact Clarke interchange, ordinary-directional/Clarke equivalence, or any original-source equivalence.

In the reconstruction below, edge identities concern \(\lambda=V\), or the same fixed-scalar active-core framework where its hypotheses hold. They are not assertions about \(h\) for unrestricted \(\lambda\) after the active-core hypotheses fail.

## 3. Edge necessity and strict normality are reconstructed, not prepaid

**Status: SUPPORTED, conditionally.**  
**Locations:** S1 lines 183–252, 323–543; S2 lines 7–31.

### 3.1 Active-core calibration

With \(m=b/(1-b)>0\), \(v=m(1+m)\) and \(Q_*=1+3m+2m^2\), the author’s diamond comparison gives \(V<Q_*\).

For \(0<m\le1/3\),

\[
Q_*-\frac{T_4}{3T_2}
=\frac{2+m-12m^2-12m^3}{3(1+2m)}>0,
\]

using the displayed positive lower bound on the numerator. For \(m\ge1/3\), \(Q_*\ge20/9>2\ge V\).

Thus \(d_V(z,y)>0\) for \(z\ge1\), and the conditional minimum in the shared core is \(F_1=F_0+1\). Direct expansion also confirms

\[
(1-b)\psi_0(x,y;\lambda)+b\psi_1(x+1,y;\lambda)
=\psi_1(x,y;\lambda)+b(\kappa-\lambda),
\quad \kappa=\frac13+2v.
\]

The weights combine to one in the remaining core cost. This is important both for the scalar derivatives and for the factor 8 in the later rounded-core gain.

### 3.2 Both scalar derivative formulas retain their endpoint terms

Writing \(u=a+1/2\), \(s=2a+1-c\) and \(k(y)=2a+1-y\), direct clipped-value differentiation yields

\[
\frac{h_a}{16}=\frac12L-A+bB,
\]

where

\[
A=\int_0^a[-d_V(2a-y,y)]_+\,dy,\quad
L=\int_0^a[d_V(a,y)]_+\,dy,\quad
B=\int_a^s[d_V(k(y),y)]_+\,dy.
\]

The moving endpoint at \(y=a\) cancels because the two descriptions have the same value there and \(\psi_0(a,a)=0\). Lower- and upper-face speeds are respectively one and two.

The other derivative is

\[
\frac{h_c}{8b}
=D_0(c)+\int_s^c[d_V(c,y)]_+\,dy
-2\int_a^c[-d_V(2c-y,y)]_+\,dy,
\]

with

\[
D_0(c)=2cT_2+2mc^2+\frac23T_3-mV.
\]

Specifically, the moving diagonal endpoint contributes

\[
\psi_1(c,c)=2mc^2+T_2c,
\]

and the deterministic term contributes

\[
\frac{C'(c)}8=cT_2+\frac23T_3-mV.
\]

Their sum is exactly \(D_0(c)\). At \(c=u\), the second formula is the right derivative.

The relevant interface values match. At root ties the coordinate derivative vanishes, and the remaining ties are isolated. Consequently, these derivatives do not require the rejected Clarke-selection identities.

### 3.3 Exclusion of a lower-face core

Let

\[
D(a)=2a^2+2ma+T_2.
\]

The upper-face threshold \((2a-y+m)^2+y^2+v\) decreases on \([0,a]\), with minimum \(D(a)\). If \(V\le D(a)\), then \(A=0\).

Meanwhile \(B>0\): \(s>a\) follows from \(c<a+1\), and at its initial endpoint the selected floor is \(a+1>1\), where the coordinate derivative is strictly positive. Hence \(h_a>0\), and a small feasible decrease of \(a\) at fixed \(c\) lowers \(h\).

Therefore every actual optimizer satisfies

\[
V>D(a).
\]

This also gives \(L=0\), excluding any positive-length lower-face core.

### 3.4 Exclusion of every scalar-interior minimum

Suppose \(c>u\).

If \(V\le D(c)\), the upper-face negative-part integral in \(h_c\) vanishes, while

\[
D_0(c)
=m(D(c)-V)+2cv+K_m,\qquad
K_m=\frac23m+3m^2+2m^3>0.
\]

Thus \(h_c>0\), contradicting interior minimality.

If \(V>D(c)\), then \(V\le2\) and \(c>1/2\) imply

\[
m<\frac12,\qquad c<1,\qquad a<\frac12.
\]

The exact subtraction

\[
D(u)-R(a)=\frac12+m+2a(1-a-m)>0,
\quad R(a)=4a^2+4ma+T_2,
\]

shows \(V>R(a)\); the whole core is upper-face.

The corner derivative decreases strictly from a positive value at \(a\) to a negative value before \(s\). Writing its zero as \(a+\ell\), one has \(0<\ell<1/2\) and

\[
A=a(V-T_2)-3ma^2-\frac83a^3,\qquad
B=(1+m)\ell^2-\frac43\ell^3.
\]

At stationarity \(A=bB\). The author’s estimates reconstruct as

\[
A>a\Bigl(\frac12+m\Bigr),\qquad
bB<\frac m4,
\]

so

\[
a<\frac{m}{2+4m}<\frac18.
\]

The simple corner root gives

\[
B_a=2(2a+1+m)\ell.
\]

Therefore

\[
\frac{h_{aa}}{16}
=-V+T_2+6ma+8a^2+2b(2a+1+m)\ell
<6a^2+(4m-2+2b)a-\frac12
<-\frac{31}{96}.
\]

The constants and inequality directions agree with the manuscript. A stationary point in this second case has a descending fixed-\(c\) second-order direction and cannot be a local minimum.

Thus every actual optimizer has

\[
\boxed{c=a+\frac12}.
\]

### 3.5 Strict vertical normal

At an actual edge minimum, the right normal derivative is nonnegative and the edge tangential derivative is zero.

The first case above already makes \(h_c^+>0\). In the second case, if \(h_c^+=0\), the tangent condition also gives \(h_a=0\). The corner root remains strictly before the collapsed endpoint, so the same negative-curvature calculation applies from the feasible decreasing-\(a\) side. It contradicts local minimality.

Hence

\[
\boxed{h_c^+>0,\qquad h_a=-h_c^+<0,\qquad h_a+h_c^+=0}.
\]

This is not the obsolete scalar-interior stationarity system \(h_a=h_c=0\).

## 4. Edge derivative, transitions and uniqueness

**Status: SUPPORTED, conditionally.**  
**Locations:** S1 lines 547–731.

Set \(e(a;\lambda)=h(a,a+1/2;\lambda)\). On the no-lower-face interval \(0<a<\beta_\lambda\),

\[
\beta_\lambda
=\frac{\sqrt{m^2+2(\lambda-T_2)}-m}{2},
\]

the full derivative is

\[
\boxed{
F(a;\lambda):=\frac{e_a}{16}
=m\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right]-A(a;\lambda).
}
\]

Before simplification, the corner and endpoint contribution is

\[
b\int_a^u d_\lambda(2u-y,y)\,dy+\frac b2D_0(u).
\]

Evaluating this expression gives the displayed polynomial term exactly. No deterministic-tail or moving-endpoint term is omitted.

### Upper-face branch

For

\[
0<a\le\alpha_\lambda,\qquad
\alpha_\lambda=\frac{\sqrt{m^2+\lambda-T_2}-m}{2},
\]

one obtains

\[
A=a(\lambda-T_2)-3ma^2-\frac83a^3
\]

and therefore

\[
F=G=\frac83a^3+4ma^2+(2T_2-\lambda)a
+m\left(\kappa-\frac{\lambda}{2}\right).
\]

The derivatives are

\[
G_a=8a^2+8ma+2T_2-\lambda,\qquad
G_{aa}=16a+8m>0.
\]

At \(R(\alpha_\lambda)=\lambda\), this gives \(G_a(\alpha_\lambda)=\lambda\).

### Free/upper branch

For \(\alpha_\lambda<a<\beta_\lambda\), define

\[
q=\frac{\sqrt{m^2+2(\lambda-D(a))}-m}{2}.
\]

Then

\[
0<q<a,\qquad \lambda-D(a)=2mq+2q^2,
\]

and integration over the upper-face block gives

\[
A=mq^2+\frac43q^3.
\]

Consequently,

\[
F=m\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right]
-mq^2-\frac43q^3.
\]

Differentiating the defining equation,

\[
q_a=-\frac{2a+m}{2q+m},
\]

so

\[
\boxed{F_a=m(2a+1+2m)+2q(2a+m)>0.}
\]

At \(q=a\), both \(F\) values agree, and both first derivatives equal \(\lambda\). Thus the clipping frontier does not create a derivative discontinuity or an additional candidate.

### Domains and qualifying-root argument

For \(\lambda>T_2\),

\[
0<\alpha_\lambda<\beta_\lambda.
\]

If \(T_2<\lambda\le2T_2\), \(G_a\ge0\) and

\[
G(0;\lambda)\ge m(\kappa-T_2)
=m\left(m+\frac13\right)>0.
\]

The free/upper branch continues strictly increasingly. Combined with the already established \(V>D(a)>T_2\), this proves the necessary condition \(V>2T_2\).

For \(\lambda>2T_2\),

\[
\theta_\lambda
=\frac{\sqrt{m^2+(\lambda-2T_2)/2}-m}{2}
\]

satisfies \(0<\theta_\lambda<\alpha_\lambda\). The function \(F\) decreases strictly before \(\theta_\lambda\), then increases strictly through both remaining branches. Its terminal limit is

\[
\lim_{a\uparrow\beta_\lambda}F(a;\lambda)
=m\left[(1+m)\beta_\lambda+\kappa-\frac{T_2}{2}\right]>0.
\]

A decreasing-branch zero is a local maximum of \(e\), not a minimum. If \(F(\theta_\lambda)=0\), \(e_a\) is positive on both sides, so that turning-point zero is not a local minimum either.

Accordingly, a positive local minimum requires \(F(\theta_\lambda)<0\), and there is then exactly one qualifying root on

\[
(\theta_\lambda,\beta_\lambda),
\]

with \(F_a>0\).

Every actual optimizer shares the same actual \(b,V\) and must supply such a qualifying root. Therefore there is **at most one qualifying positive scalar**, and actual attainment supplies its existence. The claimed **actual scalar-pair uniqueness follows conditionally**. This does not establish existence for a chosen \(b\), or uniqueness of every unreduced law or representation.

## 5. Sharper necessary value bound

**Status: SUPPORTED, conditionally.**  
**Locations:** S1 lines 733–770.

Put \(w=v(1+2m)\) and \(t=2a+m\). The upper-face cubic can be written

\[
G=\frac{t^3}{3}+\left(v-\frac{\lambda}{2}\right)t+\frac w3.
\]

At the turning point, \(t^2=\lambda/2-v\), giving exactly

\[
F(\theta_\lambda;\lambda)
=\frac w3-\frac23(\lambda/2-v)^{3/2}.
\]

Thus the necessary strict negativity is equivalent to

\[
\boxed{\lambda>2v+2^{1/3}w^{2/3}.}
\]

Because \(w>2m^3\), this lower bound strictly exceeds \(2v+2m^2=2T_2\). With \(V\le2\), it follows that

\[
T_2<1,\qquad (2m-1)(m+1)<0,
\]

hence

\[
\boxed{m<\frac12,\qquad b<\frac13.}
\]

These remain necessary conditions, not a sufficient characterization or an actual-regime existence interval.

## 6. Complete surviving clipping geometry

**Status: SUPPORTED, conditionally.**  
**Locations:** S1 lines 774–824.

At every actual optimizer, \(c=u\), \(V>D(a)\), and the remaining tail is forced to

\[
F_1(y)=2u-y,\qquad a\le y\le u.
\]

There is no interval between \(u\) and \(c\).

The core alternatives are exhaustive:

- **D:** If \(V\ge R(a)\), then
  \[
  F_0(y)=2a-y,\qquad F_1(y)=2a+1-y.
  \]
  At equality, the root touches the upper face only at \(y=0\); this is the same canonical profile, not another branch.

- **R:** If \(D(a)<V<R(a)\), the \(q\) above satisfies \(0<q<a\), and
  \[
  F_0(y)=
  \begin{cases}
  \sqrt{V-v-y^2}-m,&0\le y\le a-q,\\
  2a-y,&a-q\le y\le a,
  \end{cases}
  \qquad F_1=F_0+1.
  \]

The interface equation is exactly the defining equation for \(q\). Values match there; selected root slopes lie in \([-1,0]\), and the remaining branches have slope \(-1\). The shared endpoint and tail joins agree. The lower-face alternative was excluded by feasible descent, rather than omitted from the table.

## 7. Full value-zero equation

**Status: SUPPORTED as an exact conditional value identity and necessary equation; not a global sufficiency theorem.**  
**Locations:** S1 lines 828–900.

For the diamond profile of diagonal parameter \(d\),

\[
A=8d^2,\qquad B=\frac{64}{3}d^3,\qquad Q=\frac{32}{3}d^4.
\]

Substitution into the complete \(N,Z\), followed by the geometric one-step decomposition, gives

\[
Z_{\rm diam}=2M_2(2a),\qquad
N_{\rm diam}=\frac23M_4(2a).
\]

Thus

\[
H_{\rm diam}(2a;\lambda)
=\frac23M_4(2a)-2\lambda M_2(2a)
\]

contains the **entire geometric tail**.

On the free-root core block, let \(U=2a-y\) and \(r=\sqrt{\lambda-v-y^2}-m\). Since \(d_\lambda(r,y)=0\),

\[
\psi_1(U,y;\lambda)-\psi_1(r,y;\lambda)
=(U-r)^2\left(\frac{U+2r}{3}+m\right).
\]

The pooled-core identity makes its coefficient 8, not \(8b\). With \(\tau=\min(a,q)\),

\[
\boxed{
e(a;\lambda)=
\frac23M_4(2a)-2\lambda M_2(2a)
-8\int_0^{a-\tau}
(U-r)^2\left(\frac{U+2r}{3}+m\right)\,dy.
}
\]

For D, \(\tau=a\) and the gain vanishes. For R, the gain is essential.

On D, the **two separate equations** \(e=0\) and \(e_a=0\) give

\[
\boxed{\lambda=\frac{M_4(t)}{3M_2(t)}
=\frac{2M_3(t)}{3M_1(t)},\qquad t=2a.}
\]

Stationarity alone is not value zero. These equations are necessary for actual optimizers; arbitrary solutions are not thereby proved globally optimal.

Conditional on actual attainment and the edge theorem, the one-dimensional minimum representation follows. It is not a closed global value formula.

## 8. Assigned nonvacuity example

**Status: SUPPORTED as the stated local candidate example only.**  
**Locations:** S1 lines 904–994.

For the assigned \(m=1/10\), \(b=1/11\), the stated moments are correct:

\[
T_2=\frac3{25},\qquad T_3=\frac{83}{500},\qquad T_4=\frac{174}{625}.
\]

Expanding the elimination equation gives

\[
250(2M_3M_2-M_4M_1)
=250t^5+125t^4+80t^3-47t^2-48t+3.
\]

Written arithmetic confirms the author’s endpoint values

\[
p(11/20)=-147/512,\qquad p(3/5)=51/5,
\]

and

\[
p'(1/2)=845/8.
\]

The displayed \(p''\) is positive on \(t\ge1/2\), so the asserted root \(t_0\in(11/20,3/5)\) is unique in that interval.

For the assigned endpoints,

\[
M_2(11/20)=\frac{213}{400},\quad
M_2(3/5)=\frac35,\quad
M_4(11/20)=\frac{163113}{160000}>1,\quad
M_4(3/5)=\frac{144}{125}.
\]

These give the claimed bounds

\[
\frac59<\lambda_0<\frac{256}{355}<\frac34,
\]

so \(1/2<\lambda_0<2\).

The identity

\[
2M_3-3M_1M_2
=-t^3-\frac3{10}t^2+\frac3{10}t+\frac{37}{125}
\]

is correct. It decreases over the stated interval and equals \(19/125>0\) at its upper endpoint. Hence

\[
\lambda_0>M_2(t_0)=R(a_0),
\]

placing the candidate strictly in D. Also \(\lambda_0<Q_*\), so the active-core calculation used here is valid independently of an assertion that \(\lambda_0\) is the original actual value.

The quintic equation supplies both full value zero and edge stationarity. The stated \(c_0>31/40\) gives \(D(c_0)>1>\lambda_0\), and the reconstructed first case yields a strictly positive vertical derivative. Finally,

\[
F_a(a_0;\lambda_0)
=2t_0^2+\frac25t_0+\frac6{25}-\lambda_0
>\frac{213}{200}-\frac34
=\frac{63}{200}>0.
\]

Thus the example is a nondegenerate positive edge local-minimum candidate with full signed value zero and strict normality.

It does **not** establish global minimality over \(K\), \(\lambda_0=V\) for the original problem, or actual-regime existence at \(b=1/11\).

## 9. Final scoped assessment

| Claim | Assessment |
|---|---|
| \(V>D(a)\), excluding a positive-length lower-face core | **SUPPORTED conditionally** |
| Every actual optimizer has \(c=a+1/2\) | **SUPPORTED conditionally**, independently reconstructed here |
| Strict actual edge normal | **SUPPORTED conditionally**, including its one-sided curvature argument |
| Exact edge derivative and all constants in the two formulas | **SUPPORTED at the active-core scope** |
| Value and first-derivative matching at \(q=a\) | **SUPPORTED** |
| At most one qualifying positive scalar for fixed actual \(b,V\) | **SUPPORTED** |
| Unique actual scalar pair under actual attainment | **SUPPORTED conditionally** |
| Complete D/R clipping classification, including the tie | **SUPPORTED conditionally** |
| Sharper necessary value bound | **SUPPORTED conditionally** |
| Full value identity, rounded-core gain and geometric tail | **SUPPORTED** |
| Assigned quintic-root candidate example | **SUPPORTED at its expressly local scope** |
| Actual-regime existence, global sufficiency, global value formula, unreduced-law uniqueness, source equivalence or novelty | **NOT ESTABLISHED; not claimed by this review** |

No new mathematical defect was found in the assigned scope. The old penalty-sign MAJOR remains historical and uncured retrospectively; corrected penalty monotonicity does not itself imply global edge dominance.

**Final boundary:** this is a complete same-harness WRITTEN reconstruction, not automatic adoption or a broader assurance claim.