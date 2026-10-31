# author-candidate-v1.md — Actual cutoff-two scalar classification

**F438 GENERAL AUTHOR candidate — UNREVIEWED.**  
**Complete manuscript for Main materialization; no repository file was written.**

## Result

Conditional on the frozen actual-cutoff-two variational reduction, positivity and pruning imports, this manuscript proves:

1. **Every actual optimizer lies on the scalar edge**
   \[
   \boxed{c=a+\tfrac12.}
   \]
2. **The actual positive scalar pair is unique.**
3. The remaining actual core has exactly two possible clipping patterns: an entirely upper-face core, or one free-root block followed by one upper-face block. There is no lower-face block of positive length.
4. Every actual optimizer satisfies the stronger necessary value bound
   \[
   \boxed{
   V>2v+2^{1/3}\bigl[v(1+2m)\bigr]^{2/3}>2T_2,
   }
   \]
   and consequently
   \[
   \boxed{m<\tfrac12,\qquad b<\tfrac13.}
   \]
5. At the actual edge, the vertical normal is strictly active:
   \[
   \boxed{\partial_c^+h(a,a+\tfrac12;V)>0.}
   \]

These are **new author claims requiring independent reconstruction and parent disposition**. They are not an acceptance of this manuscript, an existence theorem for the actual regime, or a closed all-parameter value formula.

---

## 1. Frozen scope and actual methods

Assignment:

`f438-privacy-actual-cutoff2-binding-core-scalar-classification-frontier`

Parent-attributed bindings:

- Manifest SHA256: `4cf97447f5ba8094381ccca28e70b5a307769e88b69af2b8bcb54d9f9628a9a5`.
- Freeze-receipt SHA256: `98ca0b3155b214b5c92f8f3c9ade3b19651cd96136d749515980100ee4a7062d`.
- Literal-packet SHA256: `45c5e1dbf8b2f2c2e8a64075a9ebc29d1139e83790da92d193f88da45dd8155c`.

The supplied observation `2026-10-30T11:15:12-0700 PDT` and the reported hash/byte/LF matches belong to **Main’s metadata supply**, not to child-executed hashing or a child-native start/completion clock.

### Reads and chronology

I read memory/protocol guidance, the complete manifest, freeze receipt, parent live metadata and dispatch receipt, and all seven permission/status controls before the mathematical packet. I then read the complete 1799-LF packet in order:

\[
1\!-\!120,\ 121\!-\!240,\ldots,\ 1561\!-\!1680,\ 1681\!-\!1799.
\]

This included all source endings: S1 through logical line 698, S2 through 537, S3 through 454, S4 through 21, S5 through 49 and S6 through 38. A focused reread of the complete functional followed the derivation.

Mathematics began after the complete packet read. Methods were written algebra and fresh selected mathematical examples. The exact worked example offered as evidence appears in §10. No scientific executable, interpreter, CAS, numerical search, solver, enumeration, replay, external-model CLI, build, test, lint or formatter was run. Thus there is **no executed scientific argv, program output or finite-check receipt** to report. Arithmetic below is written derivation, not fabricated tool output.

The held privacy auxiliary episode and every consumer, held CORE material, AME held material and PHv8/cp116 remained **NONINPUT**. No excluded scientific link, current sibling return or external scientific source was opened. Status controls supplied permissions and exclusions only. This is an access/method disclosure, not a cognitive-isolation certificate.

The governing tool role is read-only. This full body is returned for materialization rather than using a file-write or execution bypass.

---

## 2. Mathematical object and imports

Put
\[
0<b<1,\qquad m=\frac b{1-b},\qquad v=m(1+m),
\]
and let
\[
\Pr(G=j)=(1-b)b^j,\qquad j\ge0.
\]
Write \(T_k=\mathbb EG^k\). In particular,
\[
T_2=m+2m^2,\qquad
T_3=m+6m^2+6m^3,
\]
\[
T_4=m+14m^2+36m^3+24m^4.
\]

The scalar domain is
\[
K=\{(a,c):a\ge0,\ c\ge u:=a+\tfrac12\}.
\]

For a profile \(F\) with diagonal parameter \(t\), define
\[
A(F)=8\int_0^t(F-y)\,dy,
\]
\[
Q(F)=8\int_0^t
\left(\frac{F^3}{3}+y^2F-\frac{4y^3}{3}\right)dy,
\qquad
B(F)=8\int_0^t(F^2+y^2)\,dy.
\]

The complete denominator and numerator are
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

Define
\[
\psi_0(x,y;\lambda)
=\frac{x^3}{3}+(y^2-\lambda)x-\frac{4y^3}{3}+\lambda y,
\]
\[
\psi_1(z,y;\lambda)
=\psi_0(z,y;\lambda)+m(z^2+y^2)+T_2z,
\]
and
\[
C(c;\lambda)
=4c^2T_2+\frac{16}{3}cT_3+\frac23T_4
-\lambda(8cm+2T_2).
\]

Then the **full**, rather than truncated, signed functional is
\[
H_\lambda=N-\lambda Z
=8(1-b)\int_0^a\psi_0(F_0,y;\lambda)\,dy
+8b\int_0^c\psi_1(F_1,y;\lambda)\,dy
+bC(c;\lambda).
\tag{2.1}
\]

Its tail-coordinate derivative is
\[
d_\lambda(z,y)
:=\partial_z\psi_1(z,y;\lambda)
=(z+m)^2+v+y^2-\lambda.
\tag{2.2}
\]
The everywhere-defined nonnegative-root convention is
\[
r_\lambda(y)
=\max\{0,\sqrt{\max(\lambda-v-y^2,0)}-m\}.
\tag{2.3}
\]

### Exact upstream imports

The following remain imports at their frozen scopes:

- Corrected, canonically feasible, unique fixed-scalar profile minimization.
- The unique value zero \(\rho(a,c)\) of the minimized signed functional \(h(a,c;\lambda)\).
- Under the **actual-cutoff-two hypothesis**
  \[
  \frac12<V\le2,
  \]
  the attained reduction
  \[
  V=\min_K\rho(a,c).
  \]
  Hence
  \[
  h(a,c;V)\ge0\quad\text{on }K,
  \]
  and an actual optimizing pair has \(h(a,c;V)=0\).
- Actual-optimizer positivity \(a>0\) and the pruning consequence
  \[
  u\le c<a+1.
  \]
  For \(c>u\), the imported pruning argument additionally gives \(2c^2\le V\).

No rejected two-equation P3 sufficiency, exact Clarke interchange or ordinary-directional/Clarke equivalence is imported.

### Reconstructing the active-core reduction used below

The feasible vertex diamond comparison gives
\[
V\le J_\diamond:=\frac{T_4}{3T_2}.
\]
Put
\[
Q_*=1+3m+2m^2.
\]
For \(0<m\le1/3\),
\[
Q_*-J_\diamond
=\frac{2+m-12m^2-12m^3}{3(1+2m)}>0,
\]
because its numerator is at least
\[
2-\frac{12}{9}-\frac{12}{27}=\frac29>0.
\]
For \(m\ge1/3\),
\[
Q_*\ge\frac{20}{9}>2\ge V.
\]
Consequently,
\[
\boxed{V<Q_*}.
\tag{2.4}
\]

Thus \(r_V(y)<1\), and \(d_V(z,y)>0\) for \(z\ge1\). In the actual scalar strip \(u\le c<a+1\), the smallest feasible shared-core tail coordinate conditional on \(x\) is \(x+1>1\). It is therefore the unique conditional minimum.

Writing
\[
\kappa:=\frac13+2v,
\]
direct expansion gives the useful identity
\[
(1-b)\psi_0(x,y;\lambda)+b\psi_1(x+1,y;\lambda)
=\psi_1(x,y;\lambda)+b(\kappa-\lambda).
\tag{2.5}
\]
In particular, its derivative in \(x\) is \(d_\lambda(x,y)\).

Hence, at \(\lambda=V\),
\[
F_0(y)=f_a(y):=\operatorname{clip}(r_V(y),[a,2a-y]),
\]
\[
F_1(y)=f_a(y)+1,\qquad 0\le y\le a.
\tag{2.6}
\]

For \(a\le y\le c\), the remaining tail can be written as one clipped expression:
\[
F_1(y)=
\operatorname{clip}
\left(
r_V(y),
[\max(c,2a+1-y),\,2c-y]
\right).
\tag{2.7}
\]

These selections are canonical: selected free roots have slope
\[
-\frac{y}{r_V(y)+m}\in[-1,0],
\]
because the selected coordinate is at least \(y\); the other branches have slope \(0\) or \(-1\). The joins at \(a\), \(u\) and \(c\) agree. In particular, \(f_a(a)=a\), the tail starts at \(a+1\), and ends at \(c\).

The later proof works with the **coupled profiles (2.6)–(2.7)**, not with an incorrectly unpenalized independent-tail substitution.

---

## 3. Preserved correction: the coupling penalty is nonincreasing

The false sentence at f400 line 498 and its f418 repetition remain false frozen assertions. The f419 MAJOR is not withdrawn or silently repaired.

For fixed admissible \(a,b,\lambda\),
\[
\boxed{P(a,c;\lambda)-P(a,u;\lambda)\le0\qquad(c\ge u).}
\tag{3.1}
\]

Here is the complete mechanism needed for that correction.

At a fixed height, let \(g=\psi_1(\,\cdot\,,y;\lambda)\),
\[
q_d=\operatorname{clip}(r_\lambda(y),[d,2d-y]).
\]
The clip \(q_d\) is nondecreasing in \(d\). For any threshold \(t\le2d-y\), put
\[
E_d(t)=g(\max(q_d,t))-g(q_d).
\]
If \(q_d\ge t\), this excess is zero. If \(q_d<t\), it cannot be an upper-face projection; hence \(q_d\ge r_\lambda(y)\). On that range \(g\) is nondecreasing, so increasing \(q_d\) decreases the excess until it vanishes. Thus \(E_d(t)\) is nonincreasing.

In the shared core, every threshold \(x+1\), \(x\in[a,2a-y]\), is admissible because
\[
2d-y\ge2a+1-y.
\]
The pointwise core penalty is the minimum over this **unchanged** \(x\)-box of
\[
(1-b)\bigl[\psi_0(x,y)-\psi_0(p_0,y)\bigr]+bE_d(x+1),
\]
where \(p_0\) is the independent first-core minimizer. Each fixed-\(x\) expression is nonincreasing in \(d\), and so is its minimum. On the corner, the threshold is \(2u-y\), giving the same conclusion. Integrating gives (3.1), including upper-face clips, zero roots and ties.

This correction **alone does not sign the full endpoint difference**. The edge theorem below instead excludes every possible interior local minimum.

---

## 4. Main theorem

### Theorem — conditional actual scalar classification

Assume the upstream imports in §2 and the existence of an actual-cutoff-two optimizer with \(1/2<V\le2\). Then:

1. Every actual optimizer satisfies
   \[
   c=u=a+\tfrac12.
   \]
2. Every actual optimizer satisfies
   \[
   V>D(a):=2a^2+2ma+T_2.
   \tag{4.1}
   \]
3. For the fixed actual \(b,V\), there is exactly one positive scalar \(a\) that can be an actual optimizer. Thus the actual scalar pair is unique.
4. Its core has exactly one of the two patterns in §8.
5. The necessary actual-regime bounds are
   \[
   V>2v+2^{1/3}[v(1+2m)]^{2/3}>2T_2,
   \]
   and therefore \(m<1/2\), \(b<1/3\).
6. Its edge normal satisfies
   \[
   \partial_c^+h(a,u;V)>0.
   \]

The theorem does not assert that an actual regime exists for any particular \(b\).

---

## 5. Direct scalar derivative formulas

For this section fix \(\lambda=V\), and abbreviate \(d=d_V\). Put
\[
k(y)=2a+1-y,\qquad s=2a+1-c.
\]
In the actual strip,
\[
a<s\le u\le c.
\]
The tail lower bound is \(k(y)\) on \([a,s]\), and \(c\) on \([s,c]\).

Write \([x]_+=\max(x,0)\), and define
\[
A(a)=\int_0^a[-d(2a-y,y)]_+\,dy,
\]
\[
L(a)=\int_0^a[d(a,y)]_+\,dy,
\]
\[
B(a,c)=\int_a^s[d(k(y),y)]_+\,dy.
\]

Direct differentiation of the clipped value gives
\[
\boxed{
\frac{h_a}{16}=\frac12L(a)-A(a)+bB(a,c).
}
\tag{5.1}
\]
At the scalar edge, this denotes the derivative obtained from the feasible fixed-\(c\), decreasing-\(a\) side.

For the other scalar, define
\[
D_0(c)=2cT_2+2mc^2+\frac23T_3-mV.
\]
Then
\[
\boxed{
\frac{h_c}{8b}
=
D_0(c)
+\int_s^c[d(c,y)]_+\,dy
-2\int_a^c[-d(2c-y,y)]_+\,dy.
}
\tag{5.2}
\]
At \(c=u\), (5.2) is the right derivative.

### Why these formulas retain all terms

- In (5.1), the core lower-face speed is one and the upper-face speed is two.
- The tail floor \(k\) has \(a\)-speed two.
- The moving shared-core endpoint cancels exactly:
  \[
  8\bigl[(1-b)\psi_0(a,a)+b\psi_1(a+1,a)\bigr]
  -8b\psi_1(a+1,a)=0.
  \]
- In (5.2), the tail lower-face speed is one and upper-face speed is two.
- The moving diagonal endpoint contributes
  \[
  \psi_1(c,c)=2mc^2+T_2c.
  \]
- The deterministic derivative contributes
  \[
  \frac{C'(c)}8=cT_2+\frac23T_3-mV.
  \]
  Their sum is precisely \(D_0(c)\).

At an interior scalar point, the clipping ties have measure zero, and at a root tie the coordinate derivative of the integrand vanishes. Bounded difference quotients on the finite intervals therefore justify the displayed differentiations. Moving interfaces have equal values on their two sides. At the scalar edge, the same argument uses the appropriate one-sided opening of the box.

No Clarke integral-selection identity is used.

### Immediate exclusion of a lower-face core

The quadratic
\[
(2a-y+m)^2+y^2+v
\]
is decreasing on \(0\le y\le a\), with minimum \(D(a)\). Hence, if \(V\le D(a)\), then \(A(a)=0\).

Also \(B(a,c)>0\): its interval has positive length, and at its initial endpoint
\[
k(a)=a+1>1,\qquad d(k(a),a)>0
\]
by \(V<Q_*\). Equation (5.1) then gives \(h_a>0\). A small feasible decrease of \(a\), with \(c\) fixed, strictly decreases \(h\), contradicting actual minimality.

Therefore every actual optimizer satisfies (4.1). In particular, \(L(a)=0\), and the actual core has no lower-face block of positive length.

---

## 6. Excluding the whole scalar-interior branch

Suppose an actual optimizer had \(c>u\).

### Case I: \(V\le D(c)\)

The upper-face integral in (5.2) vanishes, because its threshold has minimum \(D(c)\) at \(y=c\). Moreover,
\[
D_0(c)
=
m(D(c)-V)+2cv+K_m,
\]
where
\[
K_m:=\frac23T_3-mT_2
=\frac23m+3m^2+2m^3>0.
\]
Thus \(h_c>0\), contradicting interior stationarity.

### Case II: \(V>D(c)\)

Since \(V\le2\) and \(c>u>1/2\), this case implies
\[
m<\frac12,\qquad c<1,\qquad 0<a<\frac12.
\tag{6.1}
\]

Define the upper-face core threshold
\[
R(a):=(2a+m)^2+v=4a^2+4ma+T_2.
\]
A direct subtraction gives
\[
D(u)-R(a)
=\frac12+m+2a(1-a-m)>0
\]
under (6.1). Consequently,
\[
V>D(c)>D(u)>R(a).
\]
The entire first core is therefore upper-face:
\[
f_a(y)=2a-y.
\]

The function \(d(k(y),y)\) is positive at \(y=a\), negative at \(y=u\), and strictly decreasing on \([a,u]\). Let its unique zero be \(a+\ell\), where
\[
0<\ell<\frac12.
\]
At \(y=s\), its value is less than \(D(c)-V<0\), so this zero lies before \(s\). Thus
\[
A=a(V-T_2)-3ma^2-\frac83a^3,
\tag{6.2}
\]
\[
B=(1+m)\ell^2-\frac43\ell^3.
\tag{6.3}
\]

At an interior stationary point, \(h_a=0\), so
\[
A=bB.
\tag{6.4}
\]

But \(V>D(u)\) gives
\[
A>
a\left(\frac12+m\right)
+a^2\left(2-m-\frac23a\right)
>
a\left(\frac12+m\right),
\]
while
\[
bB<\frac m4.
\]
Consequently,
\[
a<\frac{m}{2+4m}<\frac18.
\tag{6.5}
\]

Now differentiate (5.1) once more in \(a\), keeping \(c,V\) fixed. The corner root is simple; its boundary term vanishes. Directly,
\[
B_a=2(2a+1+m)\ell,
\]
and hence
\[
\frac{h_{aa}}{16}
=
-V+T_2+6ma+8a^2
+2b(2a+1+m)\ell.
\]
Using \(V>D(u)\) and \(\ell<1/2\),
\[
\frac{h_{aa}}{16}
<
6a^2+(4m-2+2b)a-\frac12.
\]
Since \(m<1/2\), \(b<1/3\) and \(a<1/8\),
\[
\frac{h_{aa}}{16}
<
\frac{6}{64}+\frac1{12}-\frac12
=
-\frac{31}{96}<0.
\tag{6.6}
\]

Thus every possible interior stationary point in Case II has a strictly descending second-order fixed-\(c\) direction. It cannot be a local minimum.

Both cases are excluded. Therefore
\[
\boxed{c=u.}
\]

### Strictness of the actual edge normal

At the edge, Case I already gives \(h_c^+>0\).

In Case II, suppose \(h_c^+=0\). The edge tangent condition gives \(h_a=0\) as well. The same calculation (6.2)–(6.6) applies from the feasible decreasing-\(a\) side: the corner zero lies strictly before \(s=c=u\). A fixed-\(c\), negative-\(a\) displacement then lowers \(h\) to second order, contradicting minimality.

Hence every actual optimizer satisfies
\[
\boxed{h_c^+>0,\qquad h_a=-h_c^+<0,\qquad h_a+h_c^+=0.}
\tag{6.7}
\]

In particular, the old scalar-interior system \(h_a=h_c=0\) does not characterize the actual optimizer.

---

## 7. Edge derivative and uniqueness of the positive scalar

Set
\[
e(a;\lambda):=h(a,a+\tfrac12;\lambda),
\]
holding \(b\) fixed.

Actual optimizers have \(V>D(a)\). Work initially on the corresponding no-lower-face interval
\[
0<a<\beta_\lambda,
\]
where
\[
\beta_\lambda
=\frac{\sqrt{m^2+2(\lambda-T_2)}-m}{2}.
\]

The full edge derivative, obtained from (2.1), is
\[
\boxed{
\frac{e_a(a;\lambda)}{16}
=
m\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right]
-A(a;\lambda).
}
\tag{7.1}
\]

For completeness, before simplification the corner and endpoint terms are
\[
\frac{e_a}{16}
=
-A
+b\int_a^u d_\lambda(2u-y,y)\,dy
+\frac b2D_0(u).
\]
Their sum simplifies exactly to (7.1). The deterministic tail constant and moving diagonal endpoint have not disappeared.

Define
\[
F(a;\lambda):=\frac{e_a(a;\lambda)}{16},
\]
and
\[
\alpha_\lambda
=\frac{\sqrt{m^2+\lambda-T_2}-m}{2}.
\]
Then \(R(\alpha_\lambda)=\lambda\), and
\[
0<\alpha_\lambda<\beta_\lambda.
\]

### 7.1 Entirely upper-face core: \(0<a\le\alpha_\lambda\)

Here
\[
A=a(\lambda-T_2)-3ma^2-\frac83a^3,
\]
so
\[
\boxed{
F(a;\lambda)
=
G(a;\lambda)
:=
\frac83a^3+4ma^2+(2T_2-\lambda)a
+m\left(\kappa-\frac{\lambda}{2}\right).
}
\tag{7.2}
\]
Its derivatives are
\[
G_a=8a^2+8ma+2T_2-\lambda,
\qquad
G_{aa}=16a+8m>0.
\tag{7.3}
\]
At the clipping frontier,
\[
G_a(\alpha_\lambda;\lambda)=\lambda>0.
\tag{7.4}
\]

### 7.2 Free-root then upper-face core: \(\alpha_\lambda<a<\beta_\lambda\)

Let
\[
q=q(a,\lambda)
=\frac{\sqrt{m^2+2(\lambda-D(a))}-m}{2}.
\]
Then \(0<q<a\), and
\[
\lambda-D(a)=2mq+2q^2.
\]
The upper-face block has length \(q\), and
\[
A=mq^2+\frac43q^3.
\]
Therefore
\[
F(a;\lambda)
=
m\left[a^2+(1+2m)a+\kappa-\frac{\lambda}{2}\right]
-mq^2-\frac43q^3.
\tag{7.5}
\]

Differentiating the defining equation for \(q\),
\[
q_a=-\frac{2a+m}{2q+m}.
\]
It follows that
\[
\boxed{
F_a
=
m(2a+1+2m)+2q(2a+m)>0.
}
\tag{7.6}
\]
The values and first derivatives in (7.2) and (7.5) agree at \(q=a\); their common first derivative there is \(\lambda\).

### 7.3 Why \(V>2T_2\)

If \(T_2<\lambda\le2T_2\), then \(G_a\ge0\), while
\[
G(0;\lambda)
=
m\left(\kappa-\frac{\lambda}{2}\right)
\ge m(\kappa-T_2)
=m\left(m+\frac13\right)>0.
\]
After the clipping frontier, (7.6) keeps \(F\) increasing. Thus \(e_a>0\) throughout the no-lower-face interval, and no actual positive edge minimum exists.

The earlier necessary inequality \(V>D(a)>T_2\) excludes \(\lambda\le T_2\). Hence
\[
\boxed{V>2T_2.}
\tag{7.7}
\]

### 7.4 Exactly one positive local-minimum root

For \(\lambda>2T_2\), define
\[
\theta_\lambda
=
\frac{\sqrt{m^2+(\lambda-2T_2)/2}-m}{2}.
\]
Equation (7.3) shows that
\[
0<\theta_\lambda<\alpha_\lambda,
\]
and that \(F\) is:

- strictly decreasing on \((0,\theta_\lambda)\);
- strictly increasing on \((\theta_\lambda,\alpha_\lambda]\);
- strictly increasing on \((\alpha_\lambda,\beta_\lambda)\).

Moreover,
\[
\lim_{a\uparrow\beta_\lambda}F(a;\lambda)
=
m\left[(1+m)\beta_\lambda+\kappa-\frac{T_2}{2}\right]>0.
\tag{7.8}
\]

A zero on the decreasing branch is a local maximum of \(e\), not a local minimum. A zero at \(\theta_\lambda\) is not a local minimum either: if the minimum value of \(F\) is zero, \(e_a\) is positive on both sides.

Therefore a positive local minimum requires
\[
F(\theta_\lambda;\lambda)<0,
\]
and then there is **exactly one** qualifying root
\[
a_+(\lambda)\in(\theta_\lambda,\beta_\lambda),
\qquad F_a(a_+;\lambda)>0.
\tag{7.9}
\]

Every actual optimizer has the same \(b,V\), lies on the edge, and is a positive local minimum of \(e(\,\cdot\,;V)\). Thus all actual optimizers have the same \(a=a_+(V)\), and hence the same \(c=a+1/2\).

This proves actual scalar-pair uniqueness.

Fixed-scalar profile uniqueness then fixes the canonical profile pair at those scalars. This is not a separate theorem about every unreduced law or representation.

### 7.5 Sharper necessary actual-regime bound

Put
\[
w:=v(1+2m).
\]
At the turning point,
\[
2\theta_\lambda+m=\sqrt{\lambda/2-v}.
\]
Substitution into (7.2) gives
\[
F(\theta_\lambda;\lambda)
=
\frac13w-\frac23(\lambda/2-v)^{3/2}.
\]
The necessary strict inequality in (7.9) is therefore equivalent to
\[
\boxed{
\lambda>2v+2^{1/3}w^{2/3}.
}
\tag{7.10}
\]

Since \(w=m+3m^2+2m^3>2m^3\), the right-hand side of (7.10) exceeds
\[
2v+2m^2=2T_2.
\]
Together with \(V\le2\), this yields
\[
T_2<1,\qquad (2m-1)(m+1)<0,
\]
so
\[
\boxed{m<\tfrac12,\qquad b<\tfrac13.}
\]

These are necessary bounds, not a characterization of the entire actual-regime parameter interval.

---

## 8. Complete surviving actual clipping stratification

Every actual optimizer has
\[
c=u,\qquad D(a)<V,
\]
and
\[
F_1(y)=2u-y\qquad(a\le y\le u).
\]
There is no far-tail interval between \(u\) and \(c\).

The shared core has exactly the following two possibilities.

### Branch D: entirely upper-face core

If
\[
V\ge R(a)=4a^2+4ma+T_2,
\]
then
\[
F_0(y)=2a-y,\qquad
F_1(y)=2a+1-y,\qquad 0\le y\le a.
\]
At equality the free root touches the upper face at \(y=0\); it does not create another profile.

### Branch R: free root followed by upper face

If
\[
D(a)<V<R(a),
\]
let
\[
q=\frac{\sqrt{m^2+2(V-D(a))}-m}{2}\in(0,a).
\]
Then
\[
F_0(y)=
\begin{cases}
\sqrt{V-v-y^2}-m,&0\le y\le a-q,\\[2mm]
2a-y,&a-q\le y\le a,
\end{cases}
\]
and
\[
F_1(y)=F_0(y)+1.
\]

The lower-face alternative \(V\le D(a)\) has been excluded by a feasible scalar descent. The scalar-interior branch has been excluded by §6. Thus the table above covers every remaining actual clipping geometry, including its tie frontier.

---

## 9. The full value-zero condition, not stationarity alone

The preceding uniqueness proof uses actual global minimality. It must not be converted into an assertion that an arbitrary stationary candidate is globally optimal.

Here is the explicit full value equation that an actual candidate must also satisfy.

Set \(t=2a\), and define
\[
M_j(t):=\mathbb E(G+t)^j.
\]
Thus
\[
M_1=t+m,\qquad M_2=t^2+2mt+T_2,
\]
\[
M_3=t^3+3mt^2+3T_2t+T_3,
\]
\[
M_4=t^4+4mt^3+6T_2t^2+4T_3t+T_4.
\]

The all-diamond edge competitor has complete signed value
\[
H_{\rm diam}(t;\lambda)
=\frac23M_4(t)-2\lambda M_2(t).
\tag{9.1}
\]
This includes the whole geometric tail.

For a no-lower-face edge profile, put \(\tau=\min(a,q)\), where \(q\) is as above. On the root block define
\[
U(y)=2a-y,\qquad r(y)=\sqrt{\lambda-v-y^2}-m.
\]
The exact full edge value is
\[
\boxed{
e(a;\lambda)
=
\frac23M_4(2a)-2\lambda M_2(2a)
-8\int_0^{a-\tau}
(U-r)^2\left(\frac{U+2r}{3}+m\right)dy.
}
\tag{9.2}
\]

Indeed, the coupled-core identity (2.5) makes the core cost difference exactly the difference of \(\psi_1\) values. On the selected root,
\[
d_\lambda(r,y)=0,
\]
so the cubic remainder is precisely the integrand in (9.2). No tail constant or endpoint contribution is removed.

An actual optimizer must satisfy all of:

- the full value equation \(e(a;V)=0\);
- the qualifying root condition \(F(a;V)=0\), \(a>\theta_V\);
- the strict vertical condition \(h_c^+>0\);
- the standing actual-cutoff-two imports.

For Branch D these two equalities reduce to
\[
\boxed{
V=\frac{M_4(t)}{3M_2(t)}
=\frac{2M_3(t)}{3M_1(t)}.
}
\tag{9.3}
\]
For Branch R, the integral in (9.2) remains essential.

Conditional on actual existence, the attained scalar minimum can consequently be reduced to the edge:
\[
V=\min_{a\ge0}\rho(a,a+\tfrac12).
\]
This is a conditional one-dimensional reduction, **not** a closed explicit value formula or a sufficiency theorem for arbitrary solutions of (9.2)–(9.3).

---

## 10. Exact nonvacuity example for the candidate equations

This is a **fresh chosen written example**, not an executable calculation and not an assertion that the chosen \(b\) has been proved to lie in the original actual regime.

Take
\[
m=\frac1{10},\qquad b=\frac1{11}.
\]
Then
\[
T_2=\frac3{25},\qquad T_3=\frac{83}{500},
\qquad T_4=\frac{174}{625}.
\]

For a diamond edge, eliminating \(\lambda\) between the two equalities in (9.3) gives
\[
2M_3(t)M_2(t)-M_4(t)M_1(t)=0.
\]
At this \(m\), multiply the left side by \(250\) to obtain
\[
p(t)=250t^5+125t^4+80t^3-47t^2-48t+3.
\]

Exact endpoint evaluations give
\[
p\left(\frac{11}{20}\right)=-\frac{147}{512}<0,
\qquad
p\left(\frac35\right)=\frac{51}{5}>0.
\]
Also
\[
p'\left(\frac12\right)=\frac{845}{8}>0,
\]
and, for \(t\ge1/2\),
\[
p''(t)=5000t^3+1500t^2+480t-94>0.
\]
Hence there is exactly one root
\[
t_0\in\left(\frac{11}{20},\frac35\right).
\]

Define
\[
a_0=\frac{t_0}{2},\qquad
c_0=a_0+\frac12,\qquad
\lambda_0=\frac{M_4(t_0)}{3M_2(t_0)}.
\]

The root equation implies the second equality in (9.3), so both the **full value-zero equation** and the edge stationarity equation hold exactly.

Monotonicity of the positive-coefficient moment polynomials gives
\[
\frac59<\lambda_0<\frac{256}{355}<\frac34.
\]
Thus
\[
\frac12<\lambda_0<2.
\]

Furthermore,
\[
2M_3-3M_1M_2
=
-t^3-\frac3{10}t^2+\frac3{10}t+\frac{37}{125}.
\]
This expression is decreasing on the displayed interval and equals \(19/125>0\) at \(t=3/5\). Therefore
\[
\lambda_0>M_2(t_0)=R(a_0).
\]
The clipped core is genuinely in Branch D, so its fixed-scalar minimized value is exactly the diamond value used above.

Since \(c_0>31/40\),
\[
D(c_0)>2\left(\frac{31}{40}\right)^2>1>\lambda_0,
\]
and §6 Case I gives a strictly positive vertical normal.

Finally,
\[
F_a(a_0;\lambda_0)
=
2t_0^2+\frac25t_0+\frac6{25}-\lambda_0
>
\frac{213}{200}-\frac34
=
\frac{63}{200}>0.
\]
Thus this is a nondegenerate positive edge local-minimum candidate, with a strict vertical normal, full signed value zero, and value in the numerical range \(1/2<\lambda_0\le2\).

**What this example does not prove:** it does not prove global minimality over \(K\), equality \(\lambda_0=V\) for the original problem, actual-regime existence at \(b=1/11\), or a maximal transition threshold. It demonstrates that the derived candidate equations and clipping inequalities are not formally empty, without substituting a synthetic value for an established actual one.

---

## 11. Conclusions and assurance boundary

### New author results supplied

At the stated conditional scope, the manuscript supplies full written proofs of:

- exclusion of every scalar-interior actual optimizer;
- edge necessity \(c=a+1/2\);
- exclusion of a positive-length lower-face core;
- uniqueness of the positive actual scalar pair;
- the complete two-branch actual clipping classification;
- strict positivity of the actual edge normal;
- the necessary value bound
  \[
  V>2v+2^{1/3}[v(1+2m)]^{2/3};
  \]
- the complete value-zero equation, including the rounded-core gain and entire geometric tail.

The argument does **not** assert a uniform sign for
\[
h(a,c;V)-h(a,u;V)
\]
at arbitrary scalar pairs. Instead, it excludes interior minima through a direct first-derivative/negative-curvature dichotomy.

The coupling-penalty correction remains
\[
P(a,c;\lambda)-P(a,u;\lambda)\le0.
\]
The frozen f400/f418 incorrect unsigned assertions and the f419 MAJOR remain part of the record.

### Not established

- Existence of an original actual-cutoff-two regime for any specific parameter.
- The exact or maximal parameter interval of that regime.
- Which of Branch D or Branch R is selected throughout that interval.
- A closed global value formula or all-epsilon formula.
- Uniqueness outside the adopted canonical reduction.
- Source/book equivalence, priority or novelty.
- Human, independent-model-family, formal/kernel or finite-execution verification.

### Verification attribution

All new work here is **author-written mathematics**. No scientific program was run and no numerical result is claimed as observed execution.

Before adoption, the load-bearing independent reconstruction should check in particular:

1. Both scalar derivative formulas (5.1)–(5.2), including their endpoint terms.
2. The uniform negative-curvature estimate (6.6), including the edge one-sided extension used for strict normality.
3. The free/upper transition formulas and the strict unimodality argument in §7.
4. The full value identity (9.2) and the exact nonvacuity arithmetic.

**Status: AUTHOR CANDIDATE / UNREVIEWED. This return is not automatic parent adoption or original-target acceptance.**