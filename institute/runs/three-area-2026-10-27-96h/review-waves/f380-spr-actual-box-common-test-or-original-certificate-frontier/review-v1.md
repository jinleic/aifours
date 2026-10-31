# author-candidate-v1.md

## Actual septic boxes: boundary-root obstruction and an exact negative actual-member R5 witness

**Status: AUTHOR CANDIDATE — UNREVIEWED.** The written proofs and finite rational construction below require separate review and parent disposition. No adoption, novelty, independent-family, human, or formal/kernel certification is claimed.

**Original-target status:** The universal common-SPR synthesis problem remains unresolved here. This manuscript supplies the manifest’s **falsified-premise alternative**: an exact obstruction to extending the normalized boundary-root test
\[
F_{\partial}(t)=-t(b-t)(e-t)
\]
to all actual-box ray configurations. It is not another moment-only W1 counterexample.

The obstruction genuinely uses uncertainty in both parities. When the even coefficient box has positive width, its actual minimizing envelope switches between two different even polynomials at a boundary root of \(F\). This produces a negative actual R5 pairing. In particular, completing additional inequalities for the same boundary-root ansatz cannot establish the required all-ray condition.

### Results and assurance boundaries

| Item | Result | Status |
|---|---|---|
| Uniform theorem | A common \(F\) controlling all actual R5 rays cannot have \(x=a\), \(y=b,c\), or \(z=d,e\), when both parities have positive uncertainty | Written proof below; unreviewed |
| Actual coefficient box | Explicit independent four-dimensional monic septic box; **every** member is strictly Hurwitz | Written all-parameter HB proof below |
| Finite witness | Five positive actual-corner atoms forming a positive-first R5 ray, with the actual piecewise \(E_F\), satisfy \(\sum_i\mu_iE_F(u_i)F_{\partial}(u_i)<-7874\) | Exact written rational certificate; unreviewed |
| All eight coordinates | Signs are \((-,0,+,0,-,0,+,0)\) | Written proof below; **not** a strict-negative SPR obstruction |
| Reproducibility | Complete standard-library verifier supplied below | **NOTRUN** |
| Full synthesis | No common numerator constructed for every eligible box | Not proved |
| Full counterexample | No actual aggregate with all eight coordinates strictly negative | Not obtained |

No project files were written. This is the complete body for parent materialization.

---

## 1. Exact model and imported boundaries

Let
\[
K=\left\{a(s)=s^7+\sum_{j=0}^{6}a_js^j:\ell_j\le a_j\le u_j\right\}
\]
be a nonempty compact independent coefficient box, every member of which is strictly Hurwitz.

At \(t=\omega^2>0\), write
\[
a(i\omega)=E_a(t)+i\omega O_a(t),
\]
where
\[
E_a(t)=a_0-a_2t+a_4t^2-a_6t^3,\qquad
O_a(t)=a_1-a_3t+a_5t^2-t^3.
\]

The actual parity envelopes are
\[
\begin{aligned}
E_-(t)&=\ell_0-u_2t+\ell_4t^2-u_6t^3,\\
E_+(t)&=u_0-\ell_2t+u_4t^2-\ell_6t^3,\\
O_-(t)&=\ell_1-u_3t+\ell_5t^2-t^3,\\
O_+(t)&=u_1-\ell_3t+u_5t^2-t^3.
\end{aligned}
\]
Each combination \((E_\sigma,O_\tau)\) is an actual corner member.

For nondegenerate odd uncertainty, use the frozen actual-box interface
\[
O_-=(a-t)(d-t)(e-t),\qquad
O_+=(b-t)(c-t)(f-t),
\]
with
\[
0<a<b<c<d<e<f.
\]
Every actual even polynomial is negative, positive, negative on the respective closed odd bands
\[
[a,b],\quad[c,d],\quad[e,f].
\]

For one fixed triple
\[
(x,y,z)\in[0,a]\times[b,c]\times[d,e],
\qquad
F(t)=(x-t)(y-t)(z-t),
\]
the actual minimizing even choice is
\[
E_F(t)=
\begin{cases}
E_-(t),&F(t)\ge0,\\
E_+(t),&F(t)<0.
\end{cases}
\]
The same \(F\) is fixed before all ray quantifiers.

The raw row is
\[
r(a,t)=
(E,tO,-tE,-t^2O,t^2E,t^3O,-t^3E,-t^4O).
\]

For five distinct ordered nodes and
\[
H(t)=\prod_{i=1}^{5}(t-u_i),
\]
an R5 ray has weights
\[
\mu_i=\frac{\varepsilon}{u_iO_iH'(u_i)}>0,
\]
where \(\varepsilon=+1\) corresponds to odd signs \(+,-,+,-,+\), and \(\varepsilon=-1\) to \(-,+,-,+,-\). Its four signed odd moments vanish.

These actual-envelope and ray interfaces are imported from frozen S1/S2. The six-frequency sparsification and the earlier moment-only example are not premises of the new obstruction.

---

## 2. Uniform boundary-root obstruction

### Theorem

Assume that at least one odd coefficient interval and at least one even coefficient interval have positive width. Fix
\[
F(t)=(x-t)(y-t)(z-t)
\]
with the closed root placements above.

If
\[
x=a,\qquad y\in\{b,c\},\qquad\text{or}\qquad z\in\{d,e\},
\]
then there exists a feasible actual-endpoint R5 ray, using the actual piecewise \(E_F\), for which
\[
\sum_i\mu_iE_F(u_i)F(u_i)<0.
\]

Consequently, a fixed \(F\) satisfying **all** actual R5 inequalities must obey
\[
\boxed{x\in[0,a),\qquad y\in(b,c),\qquad z\in(d,e).}
\]
This is necessary, not sufficient. The possibility \(x=0\) is not excluded.

### Proof: the local envelope cusp

Positive even uncertainty gives
\[
\Delta E(t):=E_+(t)-E_-(t)
=(u_0-\ell_0)+(u_2-\ell_2)t+(u_4-\ell_4)t^2+(u_6-\ell_6)t^3>0
\]
for every \(t>0\).

Suppose a simple root \(r>0\) of \(F\) is also a simple root of an actual odd endpoint \(O_*\). Retain two adjacent nodes
\[
r-h,\qquad r+h
\]
using this same endpoint \(O_*\), and three other fixed nodes \(v_1,v_2,v_3\). Choose their actual odd endpoint signs so that all five nodes form one of the two R5 orientations.

Put
\[
A(t)=\prod_{k=1}^{3}(t-v_k).
\]
The derivatives of the five-node polynomial at the paired nodes are
\[
H'(r-h)=-2hA(r-h),\qquad H'(r+h)=2hA(r+h).
\]

On the two sides of \(r\), define
\[
C(t)=\frac{E_F(t)F(t)}{tO_*(t)}.
\]
The quotient \(F/(tO_*)\) has the finite limit
\[
\frac{F'(r)}{rO_*'(r)}.
\]

Write \(E_L,E_R\) for the even envelopes selected immediately to the left and right of \(r\). Because \(E_F\) is the actual minimizing envelope,
\[
E_R(r)-E_L(r)=-\operatorname{sgn}(F'(r))\,\Delta E(r).
\]

The paired contribution is
\[
P_h=\frac{\varepsilon}{2h}
\left(\frac{C(r+h)}{A(r+h)}-\frac{C(r-h)}{A(r-h)}\right).
\]

Positivity of the R5 weights implies
\[
\frac{\varepsilon}{A(r)}
=\frac{\operatorname{sgn}(O_*'(r))}{|A(r)|}.
\]
Therefore
\[
\boxed{
\lim_{h\downarrow0}2hP_h
=-\frac{|F'(r)|\,\Delta E(r)}
{r\,|O_*'(r)|\,|A(r)|}<0.
}
\]

The other three contributions have finite limits: their nodes remain distinct from \(r\), and their chosen odd values are nonzero. Thus the entire actual R5 pairing tends to \(-\infty\). It is negative for all sufficiently small positive \(h\).

### Feasible actual R5 supports

The required alternating supports exist in every eligible box. The following table gives complete choices; all unpaired nodes are fixed before taking sufficiently small \(h\).

| Boundary root | Paired endpoint and positions | Other three actual odd choices | Orientation |
|---|---|---|---|
| \(r=a\) | \(u_1=a-h,u_2=a+h\), both \(O_-\) | \(u_3\in(a,b):O_+\); \(u_4\in(b,c):O_+\); \(u_5\in(c,d):O_+\) | \(+,-,+,-,+\) |
| \(r=b\) | \(u_3=b-h,u_4=b+h\), both \(O_+\) | Ordered \(u_1,u_2\in(a,b)\), using \(O_+,O_-\); \(u_5\in(c,d):O_+\) | \(+,-,+,-,+\) |
| \(r=c\) | \(u_1=c-h,u_2=c+h\), both \(O_+\) | \(u_3\in(c,d):O_-\); \(u_4\in(d,e):O_-\); \(u_5\in(e,f):O_-\) | \(-,+,-,+,-\) |
| \(r=d\) | \(u_1=d-h,u_2=d+h\), both \(O_-\) | Ordered \(u_3,u_4\in(e,f)\), using \(O_-,O_+\); \(u_5>f:O_+\) | \(-,+,-,+,-\) |
| \(r=e\) | \(u_3=e-h,u_4=e+h\), both \(O_-\) | \(u_1\in(0,a):O_+\); \(u_2\in(b,c):O_+\); \(u_5\in(e,f):O_+\) | \(+,-,+,-,+\) |

These signs follow directly from the two actual factorizations. All denominators in the R5 weights are nonzero.

This proves the theorem. ∎

### Quantifiers and relevance

The result is
\[
\forall K\ \forall F\text{ with a listed boundary root}\ 
\exists\text{ an actual negative R5 ray}.
\]
It is **not** a claim that one ray defeats every admissible \(F\).

In particular, whenever both parities have positive uncertainty,
\[
F_{\partial}(t)=-t(b-t)(e-t)
\]
cannot satisfy the actual all-ray condition. This falsifies the premise needed to extend the normalized W1 ansatz unchanged to the full actual-box synthesis route. It does not falsify the existence of a different, interior-root common \(F\).

The mechanism vanishes when the even parity is fixed, because then \(\Delta E=0\). It is therefore not supplied by the previous fixed-even moment-only example.

---

## 3. An explicit independent all-Hurwitz septic box

Consider the actual coefficient box
\[
\begin{aligned}
a(s)={}&s^7+s^6+a_5s^5+\frac{13}{2}s^4+a_3s^3+11s^2+a_1s+a_0,\\
a_0&\in[15/4,17/4],\\
a_1&\in[1197/80,15],\\
a_3&\in[23,467/20],\\
a_5&\in[179/20,9].
\end{aligned}
\]
These four intervals vary independently; the remaining intervals are degenerate.

Its even endpoints are
\[
E_\pm(t)=E_0(t)\pm\frac14,\qquad
E_0(t)=\left(\frac12-t\right)(2-t)(4-t).
\]
Its odd endpoints are
\[
\begin{aligned}
O_-(t)
&=\left(\frac{19}{20}-t\right)
\left(\frac72-t\right)
\left(\frac92-t\right)\\
&=\frac{1197}{80}-\frac{467}{20}t+\frac{179}{20}t^2-t^3,\\
O_+(t)
&=(1-t)(3-t)(5-t)\\
&=15-23t+9t^2-t^3.
\end{aligned}
\]
Their difference is
\[
O_+(t)-O_-(t)=\frac3{80}+\frac7{20}t+\frac1{20}t^2>0.
\]

Thus
\[
(a,b,c,d,e,f)=
\left(\frac{19}{20},1,3,\frac72,\frac92,5\right).
\]

### All-member Hurwitz proof

Every actual odd polynomial lies pointwise between \(O_-\) and \(O_+\). At the six endpoint roots, these bounds force at least one root in each of
\[
[a,b],\qquad[c,d],\qquad[e,f].
\]
Since the polynomial is cubic, there is exactly one simple root in each band.

For every actual even polynomial, the following worst-case bounds hold:

| \(t\) | Envelope giving the required bound | Value |
|---|---|---:|
| \(0\) | \(E_-(0)\) | \(15/4>0\) |
| \(a=19/20\) | \(E_+(a)\) | \(-9529/8000<0\) |
| \(b=1\) | \(E_+(b)\) | \(-5/4<0\) |
| \(c=3\) | \(E_-(c)\) | \(9/4>0\) |
| \(d=7/2\) | \(E_-(d)\) | \(2>0\) |
| \(e=9/2\) | \(E_+(e)\) | \(-19/4<0\) |
| \(f=5\) | \(E_+(f)\) | \(-53/4<0\) |

Hence every actual even cubic has exactly one simple root in each of
\[
(0,a),\qquad(b,c),\qquad(d,e).
\]

The actual even and odd roots therefore strictly interlace in the Hurwitz orientation for **every independent coefficient choice**. All coefficients are positive. Equivalently, the additional orientation condition in the classical Hermite–Biehler theorem is positive at the real point \(s=1\), where both parity polynomials have positive values.

The classical Hermite–Biehler theorem consequently proves that every member of this entire coefficient box is strictly Hurwitz. No numerical root calculation is used.

---

## 4. The boundary test fails even weak synthesis

Fix the single allowed triple
\[
(x,y,z)=\left(0,1,\frac92\right),
\]
so
\[
F_{\partial}(t)
=-t(1-t)\left(\frac92-t\right)
=-\frac92t+\frac{11}{2}t^2-t^3.
\]

There is no real odd test polynomial \(G\) for which
\[
F_{\partial}(t)E_a(t)+tG(t)O_a(t)\ge0
\]
holds for every actual member and every \(t>0\).

Indeed, at \(t=1\),
\[
F_{\partial}(1)=O_+(1)=0.
\]
For each of the two actual members \((E_\pm,O_+)\), nonnegativity near this interior zero requires the derivative to vanish. But
\[
F_{\partial}'(1)=\frac72,\quad O_+'(1)=-8,\quad
E_+(1)=-\frac54,\quad E_-(1)=-\frac74.
\]
The two derivative equations respectively require
\[
G(1)=-\frac{35}{64},
\qquad
G(1)=-\frac{49}{64},
\]
which are incompatible.

This rules out even a weak common separator with this fixed even part. The next section gives a finite actual R5 certificate of the same failure, without relying on this derivative argument.

---

## 5. Exact five-node actual-member witness

Set
\[
h=\frac1{10000},
\]
and choose
\[
(u_1,u_2,u_3,u_4,u_5)=
\left(\frac12,\frac{39}{40},1-h,1+h,\frac72\right).
\]

Use these actual parity corners:

| Node | Even endpoint | Odd endpoint | Odd sign |
|---|---|---|---|
| \(u_1=1/2\) | \(E_+\) | \(O_+\) | \(+\) |
| \(u_2=39/40\) | \(E_+\) | \(O_-\) | \(-\) |
| \(u_3=1-h\) | \(E_+\) | \(O_+\) | \(+\) |
| \(u_4=1+h\) | \(E_-\) | \(O_+\) | \(-\) |
| \(u_5=7/2\) | \(E_-\) | \(O_+\) | \(+\) |

These even endpoints are exactly the actual piecewise \(E_{F_{\partial}}\): \(F_{\partial}<0\) at the first three nodes and \(F_{\partial}>0\) at the last two.

Although \(u_5\) is a root of the **unused** endpoint \(O_-\), its chosen value is
\[
O_+(7/2)=15/8>0.
\]
No chosen odd value is zero.

Let
\[
H(t)=\prod_{i=1}^{5}(t-u_i),\qquad
\mu_i=\frac1{u_iO_iH'(u_i)}.
\]
The signs of \(H'(u_i)\) are \(+,-,+,-,+\), matching the chosen odd signs, so every \(\mu_i>0\).

Lagrange interpolation gives
\[
\sum_i\frac{u_i^r}{H'(u_i)}=0,\qquad r=0,1,2,3.
\]
Therefore all four signed odd coordinates vanish exactly:
\[
\sum_i\mu_i(-1)^ru_i^{r+1}O_i=0.
\]

Every atom is an actual corner of the one all-Hurwitz independent box in Section 3.

---

## 6. Exact negative scalar pairing

Write
\[
L=\sum_i\mu_iE_{F_{\partial}}(u_i)F_{\partial}(u_i).
\]

For nodes using \(O_+\), cancellation of the factor \(1-t\) gives
\[
C_\pm(t)
:=\frac{E_\pm(t)F_{\partial}(t)}{tO_+(t)}
=-\frac{E_\pm(t)(9/2-t)}{(3-t)(5-t)}.
\]

Define
\[
D(t)=\left(t-\frac12\right)
\left(t-\frac{39}{40}\right)
\left(\frac72-t\right).
\]
Then
\[
H'(u_3)=2hD(u_3),\qquad
H'(u_4)=-2hD(u_4),
\]
and the paired contribution is
\[
L_{34}=\frac1{2h}
\left(\frac{C_+(u_3)}{D(u_3)}
-\frac{C_-(u_4)}{D(u_4)}\right).
\]

### Bounds for the paired nodes

Using \(999/1000<u_3<1<u_4<1001/1000\), direct rational product bounds give
\[
0<C_+(u_3)<\frac35,\qquad C_-(u_4)>\frac7{10}.
\]

For example,
\[
-E_+(u_3)
<\frac12\frac{1001}{1000}\frac{3001}{1000}-\frac14
<\frac{13}{10},
\]
while \(9/2-u_3<18/5\) and \((3-u_3)(5-u_3)>8\). Thus
\[
C_+(u_3)<\frac{117}{200}<\frac35.
\]
Similarly,
\[
-E_-(u_4)>
\frac12\frac{999}{1000}\frac{2999}{1000}+\frac14
>\frac{17}{10},
\]
and hence
\[
C_-(u_4)>
\frac{(17/10)(17/5)}8=\frac{289}{400}>\frac7{10}.
\]

Also,
\[
\begin{aligned}
D(u_3)&>
\frac{49}{100}\frac{31}{1250}\frac52>\frac3{100},\\
D(u_4)&<
\frac{501}{1000}\frac{63}{2500}\frac52<\frac4{125}.
\end{aligned}
\]
Since \(1/(2h)=5000\),
\[
L_{34}
<5000\left(20-\frac{175}{8}\right)
=-9375.
\]

### Remaining three nodes

At \(u_1\),
\[
\frac{E_+(u_1)F_{\partial}(u_1)}{u_1O_+(u_1)}
=-\frac4{45},
\]
and \(H'(u_1)>0\). Its contribution is negative.

At \(u_2=39/40\),
\[
E_+(u_2)=-\frac{78259}{64000},\qquad
O_-(u_2)=-\frac{14241}{64000}.
\]
Moreover,
\[
\frac{|F_{\partial}(u_2)|}{u_2}=\frac{141}{1600}<\frac9{100}.
\]
Thus
\[
\left|\frac{E_+(u_2)F_{\partial}(u_2)}{u_2O_-(u_2)}\right|
<\frac9{10}.
\]
The derivative magnitude satisfies
\[
|H'(u_2)|
>
\frac{47}{100}\frac3{125}\frac1{40}\frac52
=\frac{705}{1000000}>\frac3{5000}.
\]
Its positive contribution is therefore less than \(1500\).

At \(u_5\),
\[
\frac{E_-(u_5)F_{\partial}(u_5)}{u_5O_+(u_5)}=\frac83,
\qquad H'(u_5)>30.
\]
Its positive contribution is less than \(1\).

Combining all five contributions proves the exact rational bound
\[
\boxed{L<-9375+1500+1=-7874<0.}
\]

This is a negative **actual-envelope R5 pairing**, not just a failure of a decomposition assertion about odd moments.

---

## 7. All eight aggregate coordinates

For \(r=0,1,2,3\), put
\[
U_r=\sum_i\mu_i u_i^rE_i.
\]
The only positive even values occur at \(u_1,u_5\):
\[
E_+(u_1)=\frac14,\qquad E_-(u_5)=2.
\]
The other three chosen even values are negative.

For all four values of \(r\), the positive contribution at \(u_1\) is less than \(1\). Indeed,
\[
H'(u_1)=\frac{19}{40}\left(\frac14-h^2\right)3>\frac6{25},
\qquad u_1O_+(u_1)=\frac{45}{16}>\frac52,
\]
so \(\mu_1<5/3\).

At \(u_5\), \(\mu_5<1/180\), and
\[
\mu_5u_5^rE_-(u_5)
<\frac{2(7/2)^3}{180}
=\frac{343}{720}<1.
\]

At \(u_3\),
\[
\mu_3>5000000,\qquad u_3^r>\frac12,\qquad -E_+(u_3)>1.
\]
For the first inequality, use
\[
u_3<1,\qquad O_+(u_3)<\frac1{1000},\qquad
H'(u_3)=2hD(u_3)<\frac1{5000}.
\]
This one negative contribution exceeds \(2500000\) in magnitude. Consequently,
\[
U_r<0\qquad(r=0,1,2,3).
\]

Together with the four exact zero odd moments, the complete raw aggregate has signs
\[
\boxed{(-,\ 0,\ +,\ 0,\ -,\ 0,\ +,\ 0).}
\]

In particular:

- it is **not** an eight-strict-negative certificate;
- it does not refute common-SPR feasibility of this box;
- it does refute the all-ray premise for the **fixed**
  \(F_{\partial}\).

The negative scalar pairing is consistent with these mixed even signs:
\[
L=\frac92M_2+\frac{11}{2}M_4+M_6,
\]
where \(M_j\) denotes coordinate \(j\) indexed from zero.

---

## 8. Complete reproducibility source — NOTRUN

The following is the complete source for `boundary-r5-verifier-v1.py`. It uses only Python’s standard library, performs no file/network/subprocess operations, and checks the fixed rational object directly.

**Execution status: NOTRUN.** My role permits no scientific interpreter execution. No stdout, exit status, timing measurement, or computational PASS is claimed.

Parent argv after materializing the source: `python3 -B boundary-r5-verifier-v1.py`

BEGIN SOURCE: boundary-r5-verifier-v1.py

from fractions import Fraction as Q

def need(condition, reason):
    if not condition:
        raise ValueError(reason)

def product(values):
    result = Q(1)
    for value in values:
        result *= value
    return result

def sign(value):
    return (value > 0) - (value < 0)

def roots_coefficients(roots):
    coefficients = [Q(1)]
    for root in roots:
        updated = [Q(0)] * (len(coefficients) + 1)
        for j, value in enumerate(coefficients):
            updated[j] += root * value
            updated[j + 1] -= value
        coefficients = updated
    return tuple(coefficients)

e0_coeff = roots_coefficients((Q(1, 2), Q(2), Q(4)))
om_coeff = roots_coefficients((Q(19, 20), Q(7, 2), Q(9, 2)))
op_coeff = roots_coefficients((Q(1), Q(3), Q(5)))

need(e0_coeff == (Q(4), Q(-11), Q(13, 2), Q(-1)), "even expansion")
need(
    om_coeff == (Q(1197, 80), Q(-467, 20), Q(179, 20), Q(-1)),
    "odd minus expansion",
)
need(op_coeff == (Q(15), Q(-23), Q(9), Q(-1)), "odd plus expansion")
need(
    tuple(p - m for p, m in zip(op_coeff, om_coeff))
    == (Q(3, 80), Q(7, 20), Q(1, 20), Q(0)),
    "actual odd width polynomial",
)

def even(t, endpoint):
    return (Q(1, 2) - t) * (2 - t) * (4 - t) + Q(endpoint, 4)

def odd(t, endpoint):
    if endpoint == 1:
        return (1 - t) * (3 - t) * (5 - t)
    if endpoint == -1:
        return (Q(19, 20) - t) * (Q(7, 2) - t) * (Q(9, 2) - t)
    raise ValueError("odd endpoint label")

def test_f(t):
    return -t * (1 - t) * (Q(9, 2) - t)

hb_nodes = (Q(19, 20), Q(1), Q(3), Q(7, 2), Q(9, 2), Q(5))
hb_signs = (-1, -1, 1, 1, -1, -1)
for t, wanted in zip(hb_nodes, hb_signs):
    for endpoint in (-1, 1):
        need(sign(even(t, endpoint)) == wanted, "uniform even HB sign")
need(even(Q(0), -1) == Q(15, 4), "positive even constant")

intervals = (
    (Q(15, 4), Q(17, 4)),
    (Q(1197, 80), Q(15)),
    (Q(11), Q(11)),
    (Q(23), Q(467, 20)),
    (Q(13, 2), Q(13, 2)),
    (Q(179, 20), Q(9)),
    (Q(1), Q(1)),
    (Q(1), Q(1)),
)

def actual_coefficients(e_endpoint, o_endpoint):
    oc = op_coeff if o_endpoint == 1 else om_coeff
    return (
        Q(4) + Q(e_endpoint, 4), oc[0], Q(11), -oc[1],
        Q(13, 2), oc[2], Q(1), Q(1),
    )

h = Q(1, 10000)
nodes = (Q(1, 2), Q(39, 40), 1 - h, 1 + h, Q(7, 2))
e_labels = (1, 1, 1, -1, -1)
o_labels = (1, -1, 1, 1, 1)
need(all(nodes[i] < nodes[i + 1] for i in range(4)), "node order")

evens = []
odds = []
for t, et, ot in zip(nodes, e_labels, o_labels):
    coefficients = actual_coefficients(et, ot)
    need(
        all(lo <= c <= hi for c, (lo, hi) in zip(coefficients, intervals)),
        "actual coefficient membership",
    )
    ep = sum(((-1) ** r) * coefficients[2 * r] * t ** r for r in range(4))
    op = sum(((-1) ** r) * coefficients[2 * r + 1] * t ** r for r in range(4))
    need(ep == even(t, et), "direct even parity")
    need(op == odd(t, ot), "direct odd parity")
    need(et == (-1 if test_f(t) >= 0 else 1), "piecewise actual even envelope")
    evens.append(ep)
    odds.append(op)

need(tuple(map(sign, odds)) == (1, -1, 1, -1, 1), "R5 odd orientation")
derivatives = tuple(
    product(t - v for j, v in enumerate(nodes) if j != i)
    for i, t in enumerate(nodes)
)
weights = tuple(
    1 / (t * o * derivative)
    for t, o, derivative in zip(nodes, odds, derivatives)
)
need(all(w > 0 for w in weights), "positive actual R5 weights")

for r in range(4):
    need(
        sum(t ** r / derivative for t, derivative in zip(nodes, derivatives)) == 0,
        "Lagrange annihilation",
    )
need(
    sum(t ** 4 / derivative for t, derivative in zip(nodes, derivatives)) == 1,
    "Lagrange normalization",
)

rows = tuple(
    (e, t * o, -t * e, -t ** 2 * o,
     t ** 2 * e, t ** 3 * o, -t ** 3 * e, -t ** 4 * o)
    for t, e, o in zip(nodes, evens, odds)
)
aggregate = tuple(
    sum(w * row[j] for w, row in zip(weights, rows))
    for j in range(8)
)
need(
    tuple(map(sign, aggregate)) == (-1, 0, 1, 0, -1, 0, 1, 0),
    "all eight aggregate signs",
)

parts = tuple(
    w * e * test_f(t) for w, e, t in zip(weights, evens, nodes)
)
pairing = sum(parts)
coefficient_pairing = (
    Q(9, 2) * aggregate[2] + Q(11, 2) * aggregate[4] + aggregate[6]
)
need(pairing == coefficient_pairing, "raw-coordinate pairing identity")

def c_value(t, endpoint):
    return -even(t, endpoint) * (Q(9, 2) - t) / ((3 - t) * (5 - t))

def d_value(t):
    return (t - Q(1, 2)) * (t - Q(39, 40)) * (Q(7, 2) - t)

need(0 < c_value(nodes[2], 1) < Q(3, 5), "left local quotient bound")
need(c_value(nodes[3], -1) > Q(7, 10), "right local quotient bound")
need(d_value(nodes[2]) > Q(3, 100), "left derivative factor bound")
need(d_value(nodes[3]) < Q(4, 125), "right derivative factor bound")
need(parts[2] + parts[3] < -9375, "negative paired contribution")
need(parts[0] < 0, "first contribution sign")
need(0 < parts[1] < 1500, "second contribution bound")
need(0 < parts[4] < 1, "fifth contribution bound")
need(pairing < -7874, "negative actual-envelope R5 pairing")

for j, value in enumerate(aggregate):
    print("aggregate[" + str(j) + "]=" + str(value))
for i, value in enumerate(weights):
    print("weight[" + str(i + 1) + "]=" + str(value))
print("fixed_F_pairing=" + str(pairing))
print("finite_actual_R5_check=PASS")
print("scope=fixed boundary F only; not an eight-strict-negative SPR certificate")

END SOURCE

This source checks the endpoint sign data used by the written uniform Hurwitz proof. Its finite execution alone would not replace the proof that those signs cover every member of the independent box.

---

## 9. Public sources and prior-public boundary

The load-bearing classical external import is the Hermite–Biehler criterion:

- Olga Holtz, **“Hermite–Biehler, Routh–Hurwitz, and total positivity,”** Theorem 1. The full public HTML body, including the theorem, proofs, and ending, was read:  
  https://arxiv.org/html/math/0512591v1

Two further primary-source records were inspected for scope:

- Xu et al., **“Robust Strictly Positive Real Synthesis for Sixth-Order Interval Polynomial Families,”** v2:  
  https://arxiv.org/html/2609.26541v2  
  The full reader body and appendices were read. Its theorem concerns degree six, not the septic problem. Its fixed-even construction and its stated formal verification are prior-public claims, not new results of this manuscript. No Lean source or kernel replay was performed here.

- Long Wang, **“Robust Strictly Positive Real Synthesis for Polynomial Families of Arbitrary Order,”** arXiv abstract:  
  https://arxiv.org/abs/math/0211012  
  Only the abstract was read. Its stated two-polynomial convex-combination result is not imported as a theorem for independent coefficient boxes.

An initially mistyped arXiv request, `math/0512595`, returned an unrelated orthogonal-group volume abstract. It was not used. The correct Holtz paper was then located by search and read.

The finite example intentionally reuses the simple even baseline
\[
(1/2-t)(2-t)(4-t)
\]
already present in frozen S2. Neither that polynomial nor the classical interlacing argument is advertised as new science. The new candidate claim is the actual-envelope boundary obstruction and its explicit negative actual R5 realization. Priority and novelty remain unassessed.

---

## 10. Read and execution receipt

Before deriving the new mathematics, I read:

1. The complete f380 manifest and freeze receipt.
2. All seven permission/status controls named in `controls_before_body`, through their endings.
3. The complete parent-supplied live metadata record.
4. The ordered literal packet in consecutive raw windows:
   **1–190, 191–390, 391–590, 591–790, 791–1003**, through its actual ending.

That packet supplied complete S1, complete S2 through its logical line 923, and complete S3 through line 31. No linked held scientific payload or held consumer was opened.

Bindings supplied and confirmed by the parent metadata—not by child hash execution—were:

- Manifest: `c5a22a2f0cfe0926e6ac8b8ae39a5fbe284e41333e76a89cf2f60266af4d147d`
- Freeze receipt: `041b80509d139c1a4afec19ab07fa3013a89f8f6465c5b0acf84971fc1cd5b8b`
- Literal packet: `6f35115f2508f4bb7fce4155f4ac3d5e5aceb1ece4c397f717c4830bbc44200b`

Parent-native clock observations received were **10:13:02 PDT** and **10:23:44 PDT** on the assigned date. These are parent metadata observations, not my native start, derivation, execution, completion, or file-creation times.

The chronology after the complete frozen input read was: public-source inspection; written boundary-cusp derivation; selection of rational actual endpoint polynomials; written all-member Hurwitz and finite-pairing bounds; preparation of the unexecuted verifier. A substantive author checkpoint reporting this result and its limits was delivered to the parent.

Scientific interpreter/CAS/solver executions: **zero**. Numerical root tests, random searches, and optimization runs: **zero**. No project write, build, lint, formatter, installation, deletion, credential/provider change, external-model CLI, commit/push, or infrastructure mutation occurred.

---

## 11. Exact remaining obligations

The universal original target is still unpaid. Specifically:

1. The boundary exclusion does not construct an interior-root triple controlling every actual R4 and both R5 orientations.
2. It does not establish that any eligible box lacks every possible common \(F\).
3. The displayed finite ray has zero odd moments and mixed even signs; it cannot be promoted into an all-eight-strict-negative certificate.
4. No passage from a weak separator to a strict common SPR numerator is proved.
5. The proposed verifier has not been executed, and neither its source nor the manuscript has received disjoint review.

Zero-odd singleton and same-frequency cancellation rays remain part of the original cone. They have not been discarded or divided by. One negative R5 ray suffices to defeat this fixed boundary test; it says nothing adverse about those other rays or about an alternative common \(F\).

**Author conclusion:** The normalized boundary-root route cannot be completed merely by adding more W1 vertex inequalities. With actual positive even uncertainty, its fixed \(F_{\partial}\) fails an actual required R5 inequality—uniformly by the cusp theorem and explicitly by the rational all-Hurwitz-box witness above. Any successful construction through the frozen three-root reduction must change the root selection into the required interiors and still discharge all ray and strictness obligations.