# f390 independent exact finite check

**Status: AUTHOR CANDIDATE — UNREVIEWED pending parent disposition.**  
**Scientific execution: NOT RUN.** Runtime restrictions permit this review and source delivery but prohibit executing scientific code or editing files. The complete standalone checker is supplied below for parent materialization and replay.

## 1. Scope, provenance, and chronology

Reviewed the complete manifest, receipt, all seven controls, and parent metadata supply **before** opening the mathematical packet. Sent a direct pre-body acknowledgement, then read packet LF1–607 in ordered raw windows of at most 20 LF, including both selected-source endings.

Inputs:

- **Manifest:** `manifest-v1.json`, supplied SHA256 `0357c045baacfdf2abe004d312a488aff95fd1aa32a2a1c3fe21bdcdec3a0a0d`.
- **Receipt:** `freeze-receipt-v1.json`, supplied SHA256 `daa5c882e819cf83e7e067a6a00cbc25ab86fdfe18ee74b1a1dca3af9ed649b6`.
- **Packet:** `literal-packet-v1.md`, supplied SHA256 `9d3f7b76e6a41de3fa9d15fcc5f89b8428f5e3371fb1bf637a9aae2c90ecc4e3`.
- **S1:** f380 `review-v1.md`, SHA256 `2ca1e3dcad4c4032d604c53c8c1c69c5fda66ca92a71c9a76a4a24116af3ba4c`, **only LF1–578**.
- **S2:** Holtz Hermite–Biehler excerpt, SHA256 `942d2cbf6d77a7e31de13a9ea962d6fa66514ce211d6b2ee6958677d6b58cbd0`, LF1–27.

These paths are rooted at:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/`

The hashes, byte/LF counts, and clock **2026-10-30T10:34:20-0700 PDT** are **parent-supplied observations**, not independently computed child metadata or a child-native start/completion time. The deadline remains **2026-10-31T21:23:27Z**.

The controls were used for permissions and exclusions only. No held mathematical payload, authored checker, sibling outcome, PHv8/cp116 consumer, or AMEt28 route was read or used. In particular, S1 LF579–828, containing excluded material, was not opened. S2’s final line is a reader continuation notice; this was **not** a complete-paper read.

After the packet read, I independently expanded the literal polynomials, derived the finite rational tables and invariants below, and delivered a substantive checkpoint without inventing a native timestamp. No scientific program was executed, and no filesystem artifact was written. This chronology is an access/use disclosure, not a cognitive-isolation certificate.

## 2. Claimwise disposition

“SUPPORTED” below means supported by the displayed **written exact derivation**, not by an observed interpreter run or final gate acceptance.

| Claim | Disposition | Evidence and boundary |
|---|---|---|
| The specified independent box has 16 actual corners and the stated parity envelopes | **SUPPORTED** | Direct coefficient expansion and independent interval minimization; S1 LF235–264 |
| The seven stated worst-case even endpoint values are exact | **SUPPORTED** | Exact table below; S1 LF281–291 |
| Every member is strictly Hurwitz | **SUPPORTED as a written HB application** | Degree/IVT/interlacing argument below, using S2 LF13–18; its separate written-proof gate remains unpaid |
| The five atoms are actual corners and have positive R5 weights | **SUPPORTED** | Exact \(E,O,F,H'\) table below; S1 LF348–390 |
| The four signed odd coordinates vanish | **SUPPORTED** | Lagrange coefficient identity, independently reconstructed |
| The entire aggregate has signs \((-,0,+,0,-,0,+,0)\) | **SUPPORTED** | Exact aggregate representation and uniform bounds for its four even moments |
| The fixed-\(F_\partial\) scalar pairing is \(<-7874\) | **SUPPORTED** | Independent coefficient-row and factorized derivations agree algebraically |
| This is an eight-strict-negative certificate | **REFUTED** | Four coordinates are zero; coordinates 2 and 6 are positive |
| No polynomial \(G\) works with this fixed \(F_\partial\), even for weak pointwise nonnegativity | **SUPPORTED** | Incompatible derivative conditions at \(t=1\) |
| The universal boundary-root cusp argument is valid | **SUPPORTED at the reconstructed written-algebra level** | Limit and support signs checked below; not discharged by this FINITE gate |
| Other admissible \(F\) are excluded, or common-SPR feasibility of this box is refuted | **INCONCLUSIVE / not established** | The witness fixes \(F_\partial\); its quantifiers do not exclude interior-root alternatives |
| Original universal synthesis problem is solved; novelty is established | **INCONCLUSIVE / not established** | Neither synthesis nor a novelty audit is supplied |
| The executable checker and mutations passed | **INCONCLUSIVE — NOT RUN** | Complete independently written source and intended outcomes supplied below |

**Findings:** no mathematical correctness defect identified in the selected claims. **F/M/m: 0/0/0.** Execution and acceptance limitations are recorded explicitly rather than presented as mathematical findings.

## 3. Actual coefficient box and parity envelopes

The literal box is

\[
a(s)=s^7+s^6+a_5s^5+\frac{13}{2}s^4+a_3s^3+11s^2+a_1s+a_0,
\]

with four independent two-endpoint choices:

\[
a_0\in[15/4,17/4],\quad
a_1\in[1197/80,15],\quad
a_3\in[23,467/20],\quad
a_5\in[179/20,9].
\]

Therefore it has exactly \(2^4=16\) distinct corners.

Expanding the literal factors, independently of any supplied checker,

\[
E_0(t)=(1/2-t)(2-t)(4-t)
      =4-11t+\frac{13}{2}t^2-t^3,
\]
\[
E_-(t)=E_0(t)-1/4,\qquad E_+(t)=E_0(t)+1/4,
\]
\[
O_-(t)=(19/20-t)(7/2-t)(9/2-t)
      =\frac{1197}{80}-\frac{467}{20}t+\frac{179}{20}t^2-t^3,
\]
\[
O_+(t)=(1-t)(3-t)(5-t)=15-23t+9t^2-t^3.
\]

For \(t>0\), independent coefficient minimization chooses \(a_1\) low, \(a_3\) high, and \(a_5\) low for \(O_-\), with the opposite choices for \(O_+\). Thus these are actual corners, not an independent relaxation of the box.

Their difference is

\[
O_+(t)-O_-(t)=\frac3{80}+\frac7{20}t+\frac1{20}t^2>0.
\]

### Exact HB endpoint data

Let \((a,b,c,d,e,f)=(19/20,1,3,7/2,9/2,5)\).

| \(t\) | \(O_-(t)\) | \(O_+(t)\) |
|---|---:|---:|
| \(a\) | \(0\) | \(3321/8000\) |
| \(b\) | \(-7/16\) | \(0\) |
| \(c\) | \(-123/80\) | \(0\) |
| \(d\) | \(0\) | \(15/8\) |
| \(e\) | \(0\) | \(21/8\) |
| \(f\) | \(-243/80\) | \(0\) |

The worst-case even bounds are exactly:

| Point | Bound |
|---|---:|
| \(0\) | \(E_-(0)=15/4>0\) |
| \(a\) | \(E_+(a)=-9529/8000<0\) |
| \(b\) | \(E_+(b)=-5/4<0\) |
| \(c\) | \(E_-(c)=9/4>0\) |
| \(d\) | \(E_-(d)=2>0\) |
| \(e\) | \(E_+(e)=-19/4<0\) |
| \(f\) | \(E_+(f)=-53/4<0\) |

**Continuum argument, distinct from finite checks.** Every actual odd cubic is pointwise between the envelopes, so IVT gives a root in each of the disjoint closed bands \([a,b],[c,d],[e,f]\). A cubic with these three distinct roots has exactly those roots, each simple. Every actual even cubic similarly has a root in each of \((0,a),(b,c),(d,e)\), again exactly one simple root per interval. Hence the positive \(t\)-roots strictly interlace.

For \(a(s)=p(s^2)+sq(s^2)\), this produces simple real interlacing roots of \(p(-x^2)\) and \(xq(-x^2)\), including the latter’s root at zero. At \(z_0=1\),

\[
p(1)=a_0+\frac{37}{2}>0,\qquad
q(1)=a_1+a_3+a_5+1>0.
\]

Thus \(\operatorname{Re}(p(1)/q(1))>0\), supplying the additional orientation condition in the frozen [Holtz Theorem 1 excerpt](https://arxiv.org/html/math/0512591v1). This is a **written application of the named theorem**, not a conclusion from checking finitely many corners or numerical roots.

## 4. Exact finite object and all eight coordinates

Set \(h=1/10000\),

\[
(u_1,u_2,u_3,u_4,u_5)
=(1/2,39/40,9999/10000,10001/10000,7/2),
\]
\[
F(t)=-t(1-t)(9/2-t).
\]

The selected parity corners are \((+,+),(+,-),(+,+),(-,+),(-,+)\), where the first sign selects \(E\), the second \(O\).

Write \(P_i=H'(u_i)\), \(H(t)=\prod_j(t-u_j)\). Independent exact expansion gives:

| \(i\) | \(E_i\) | \(O_i\) | \(F(u_i)\) | \(P_i\) |
|---|---:|---:|---:|---:|
| 1 | \(1/4\) | \(45/8\) | \(-1\) | \(1424999943/4000000000\) |
| 2 | \(-78259/64000\) | \(-14241/64000\) | \(-5499/64000\) | \(-119935581/160000000000\) |
| 3 | \(-1249899964999/10^{12}\) | \(800060001/10^{12}\) | \(-349974999/10^{12}\) | \(62240039502/10^{16}\) |
| 4 | \(-1750099965001/10^{12}\) | \(-799940001/10^{12}\) | \(350024999/10^{12}\) | \(-62760039498/10^{16}\) |
| 5 | \(2\) | \(15/8\) | \(35/4\) | \(189374999697/4000000000\) |

All nodes are positive and strictly increasing. Both \(O_i\) and \(P_i\) have signs \(+,-,+,-,+\), so

\[
\mu_i=\frac1{u_iO_iP_i}>0.
\]

The chosen even values minimize \(E\,F(u_i)\) over the actual box: \(F<0\) at the first three nodes, requiring \(E_+\), and \(F>0\) at the last two, requiring \(E_-\).

### Exact aggregate, not only its signs

Define the following **fully specified rational expression** for \(k=0,1,2,3\):

\[
\begin{aligned}
S(k)={}&
 \frac4{45P_1}(1/2)^k
+\frac{3130360}{555399P_2}(39/40)^k\\
&-\frac{1249899964999\cdot10000}
 {9999\cdot800060001P_3}(9999/10000)^k\\
&+\frac{1750099965001\cdot10000}
 {10001\cdot799940001P_4}(10001/10000)^k
+\frac{32}{105P_5}(7/2)^k .
\end{aligned}
\]

All \(P_i\) are the literal rational constants in the table. This is an exact factored rational representation; no floating-point approximation or unknown quantity remains.

The entire raw aggregate is

\[
\boxed{M=(S(0),\,0,\,-S(1),\,0,\,S(2),\,0,\,-S(3),\,0).}
\]

To prove the odd zeros independently, interpolation of \(t^r\), \(r<4\), in the five Lagrange basis polynomials gives

\[
\sum_i \frac{u_i^r}{P_i}=0.
\]

Since \(\mu_i u_iO_i=1/P_i\), all four signed odd row coordinates vanish. The corresponding normalization at \(r=4\) is \(\sum_i u_i^4/P_i=1\).

For every \(k=0,1,2,3\), the positive contribution to \(S(k)\) at node 1 is \(<1\), and that at node 5 is \(<1\). At node 3,

\[
\mu_3>5000000,\quad u_3^k>1/2,\quad E_3<-1.
\]

The other two contributions are negative. Consequently,

\[
S(k)<2-2500000=-2499998<0.
\]

Therefore

\[
\boxed{\operatorname{sign}M=(-,0,+,0,-,0,+,0).}
\]

This is **not** an eight-strict-negative obstruction.

## 5. Scalar negativity: two independent representations

The coefficient vector of the fixed even numerator part is

\[
B=(0,0,9/2,0,11/2,0,1,0).
\]

Pairing it with the raw coefficient rows gives

\[
B\cdot r(a,t)
=-\frac92tE+\frac{11}{2}t^2E-t^3E=E\,F(t).
\]

Thus the direct coefficient-row aggregate gives

\[
L=B\cdot M=-\frac92S(1)+\frac{11}{2}S(2)-S(3).
\]

This equals \(\frac92M_2+\frac{11}{2}M_4+M_6\), with zero-based indexing.

For a separate factorized reconstruction, put \(C_i=E_iF(u_i)/(u_iO_i)\). Exact cancellation yields

\[
C_1=-4/45,\quad C_2=-78259/161600,\quad C_5=8/3,
\]
\[
C_3=\frac{1249899964999\cdot35001}
 {10^8\cdot800060001},\qquad
C_4=\frac{1750099965001\cdot34999}
 {10^8\cdot799940001}.
\]

Hence an additional exact representation of the same scalar is

\[
\boxed{
L=-\frac4{45P_1}
-\frac{78259}{161600P_2}
+\frac{C_3}{P_3}
+\frac{C_4}{P_4}
+\frac8{3P_5}.
}
\]

Let

\[
D(t)=(t-1/2)(t-39/40)(7/2-t).
\]

Then

\[
D(u_3)=31120019751/10^{12},\qquad
D(u_4)=31380019749/10^{12},
\]
\[
P_3=2hD(u_3),\qquad P_4=-2hD(u_4).
\]

The paired contribution therefore has the essential **minus** sign:

\[
L_{34}=\frac1{2h}
\left(\frac{C_3}{D(u_3)}-\frac{C_4}{D(u_4)}\right).
\]

The exact rational inequalities

\[
0<C_3<3/5,\quad C_4>7/10,\quad
D(u_3)>3/100,\quad 0<D(u_4)<4/125
\]

give \(L_{34}<-9375\). The remaining contributions satisfy

\[
L_1<0,\qquad 0<L_2<1500,\qquad 0<L_5<1.
\]

Therefore

\[
\boxed{L<-9375+1500+1=-7874.}
\]

This proves failure of the all-ray inequality for the **fixed** \(F_\partial\), using actual box members.

## 6. Derivative conflict and universal-scope boundary

At \(t=1\),

\[
F(1)=O_+(1)=0,\quad F'(1)=7/2,\quad O_+'(1)=-8,
\]
\[
E_+(1)=-5/4,\qquad E_-(1)=-7/4.
\]

If \(F E+tGO_+\) were nonnegative on a neighborhood of this interior zero for both actual even choices, its derivative there would vanish. These two equations require respectively

\[
G(1)=-35/64,\qquad G(1)=-49/64.
\]

They are incompatible. This excludes even weak nonnegativity with this fixed \(F\), and does not depend on a numerical root computation.

For the uniform cusp argument, positivity of the two paired weights implies

\[
\frac{\varepsilon}{A(r)}
=\frac{\operatorname{sgn}O_*'(r)}{|A(r)|}.
\]

The minimizing-envelope jump is
\(E_R(r)-E_L(r)=-\operatorname{sgn}F'(r)\Delta E(r)\).
Substitution yields

\[
\lim_{h\downarrow0}2hP_h
=-\frac{|F'(r)|\Delta E(r)}
 {r|O_*'(r)||A(r)|}<0.
\]

The support table in S1 LF201–205 has the stated alternating signs: the \(a,b,e\) cases have positive-first orientation, while \(c,d\) have negative-first orientation. Fixed unpaired nodes can remain separated from the paired nodes for sufficiently small \(h\). Their denominators stay nonzero and their contributions have finite limits.

This reconstructs the displayed written mechanism. **Its universal quantification, and the all-member HB conclusion, still belong to the separate written-proof gate.** A finite checker cannot discharge those continuum claims.

Neither argument excludes \(x=0\), nor an admissible interior-root choice of \(F\). No common numerator is constructed, and no actual aggregate with eight strictly negative coordinates is supplied.

## 7. Meaningful mutation controls

The checker below implements four fresh mutations. Their stated outcomes are **mathematically derived intended outcomes, not observed execution output**.

| Mutation | Preserved precondition | Intended rejection |
|---|---|---|
| Replace the odd minimum’s \(t\)-coefficient \(-467/20\) by \(-23\) | Still an actual odd corner | `ODD_ENVELOPE_MINIMUM`: at \(t=1\), mutant value \(-7/80\) differs from actual minimum \(-7/16\) by \(7/20\) |
| Use \(E_+\), rather than \(E_-\), at \(u_4\) | Every atom remains an actual corner; odd values and weights unchanged | `EVEN_POINTWISE_MINIMIZER`: objective exceeds its actual minimum by \(F(u_4)/2>0\) |
| Double \(\mu_1\) | All weights remain positive | `ODD_MOMENTS`: moment \(r=0\) becomes \(1/P_1>0\), rather than zero |
| Replace the paired subtraction by addition | Original atoms and weights unchanged | `PAIR_DECOMPOSITION_SIGN`: wrong pair exceeds direct pair by \(C_4/(hD(u_4))>0\) |

Only the named invariant exception is accepted as a mutation rejection. Deadline errors and arbitrary exceptions do not count.

## 8. Complete materializable checker

**Proposed source name:** `f390-independent-exact-finite-v1.py`  
**Argv:** `python3 -B f390-independent-exact-finite-v1.py`  
**Status:** **NOT RUN**; no stdout, exit status, runtime, or code hash is claimed.

The program uses only the standard library, embeds all scientific inputs, and performs no input-file access, networking, subprocess launch, installation, deletion, or writes. It has a cooperative 55-second guard; actual runtime is unmeasured.

To materialize the source, each line beginning `PY|` contributes exactly its suffix followed by LF. Remove only that three-character prefix. The complete source follows, without omitted sections.

PY|from fractions import Fraction as Q
PY|from itertools import product
PY|from math import prod
PY|from time import monotonic
PY|
PY|DEADLINE = monotonic() + 55.0
PY|
PY|class InvariantError(Exception):
PY|    def __init__(self, tag, detail=""):
PY|        super().__init__(tag + ": " + detail)
PY|        self.tag = tag
PY|        self.detail = detail
PY|
PY|def need(condition, tag, detail=""):
PY|    if monotonic() > DEADLINE:
PY|        raise RuntimeError("55-second cooperative deadline exceeded")
PY|    if not condition:
PY|        raise InvariantError(tag, detail)
PY|
PY|def multiply(p, q):
PY|    out = [Q(0)] * (len(p) + len(q) - 1)
PY|    for i, x in enumerate(p):
PY|        for j, y in enumerate(q):
PY|            out[i + j] += x * y
PY|    return tuple(out)
PY|
PY|def from_roots(roots):
PY|    p = (Q(1),)
PY|    for r in roots:
PY|        p = multiply(p, (r, Q(-1)))
PY|    return p
PY|
PY|def value(p, t):
PY|    out = Q(0)
PY|    for c in reversed(p):
PY|        out = out * t + c
PY|    return out
PY|
PY|def derivative_value(p, t):
PY|    return sum((k * p[k] * t ** (k - 1)
PY|                for k in range(1, len(p))), Q(0))
PY|
PY|def shifted_constant(p, delta):
PY|    return (p[0] + delta,) + p[1:]
PY|
PY|def sign(x):
PY|    return (x > 0) - (x < 0)
PY|
PY|BOUNDS = (
PY|    (Q(15, 4), Q(17, 4)),
PY|    (Q(1197, 80), Q(15)),
PY|    (Q(11), Q(11)),
PY|    (Q(23), Q(467, 20)),
PY|    (Q(13, 2), Q(13, 2)),
PY|    (Q(179, 20), Q(9)),
PY|    (Q(1), Q(1)),
PY|    (Q(1), Q(1)),
PY|)
PY|CHOICES = tuple(tuple(sorted(set(pair))) for pair in BOUNDS)
PY|CORNERS = tuple(tuple(a) for a in product(*CHOICES))
PY|need(len(CORNERS) == 16 and len(set(CORNERS)) == 16,
PY|     "ACTUAL_CORNER_COUNT")
PY|
PY|def parity_values(member, t):
PY|    even, odd = Q(0), Q(0)
PY|    for j, coefficient in enumerate(member):
PY|        term = coefficient * ((-1) ** (j // 2)) * t ** (j // 2)
PY|        if j % 2:
PY|            odd += term
PY|        else:
PY|            even += term
PY|    return even, odd
PY|
PY|def coefficient_envelopes(parity):
PY|    lower, upper = [], []
PY|    for k, j in enumerate(range(parity, 8, 2)):
PY|        lo, hi = BOUNDS[j]
PY|        s = (-1) ** k
PY|        lower.append(s * (lo if s > 0 else hi))
PY|        upper.append(s * (hi if s > 0 else lo))
PY|    return tuple(lower), tuple(upper)
PY|
PY|def corner(even_label, odd_label):
PY|    out = []
PY|    for j, (lo, hi) in enumerate(BOUNDS):
PY|        label = odd_label if j % 2 else even_label
PY|        s = (-1) ** (j // 2)
PY|        pick_high = (label == "+") if s > 0 else (label == "-")
PY|        out.append(hi if pick_high else lo)
PY|    result = tuple(out)
PY|    need(result in CORNERS, "ACTUAL_CORNER_MEMBERSHIP")
PY|    return result
PY|
PY|E_ROOTS = (Q(1, 2), Q(2), Q(4))
PY|OM_ROOTS = (Q(19, 20), Q(7, 2), Q(9, 2))
PY|OP_ROOTS = (Q(1), Q(3), Q(5))
PY|F_ROOTS = (Q(0), Q(1), Q(9, 2))
PY|E0 = from_roots(E_ROOTS)
PY|EM = shifted_constant(E0, Q(-1, 4))
PY|EP = shifted_constant(E0, Q(1, 4))
PY|OM, OP = from_roots(OM_ROOTS), from_roots(OP_ROOTS)
PY|F = from_roots(F_ROOTS)
PY|need(E0 == (Q(4), Q(-11), Q(13, 2), Q(-1)),
PY|     "EVEN_FACTOR_EXPANSION")
PY|need(coefficient_envelopes(0) == (EM, EP),
PY|     "EVEN_BOX_VS_FACTORS")
PY|need(coefficient_envelopes(1) == (OM, OP),
PY|     "ODD_BOX_VS_FACTORS")
PY|need(tuple(OP[k] - OM[k] for k in range(4)) ==
PY|     (Q(3, 80), Q(7, 20), Q(1, 20), Q(0)),
PY|     "ODD_ENVELOPE_DIFFERENCE")
PY|need(F == (Q(0), Q(-9, 2), Q(11, 2), Q(-1)),
PY|     "NUMERATOR_FACTOR_EXPANSION")
PY|
PY|a, b, c, d, e, f = (
PY|    Q(19, 20), Q(1), Q(3), Q(7, 2), Q(9, 2), Q(5)
PY|)
PY|ODD_ENDPOINTS = (
PY|    (a, Q(0), Q(3321, 8000)),
PY|    (b, Q(-7, 16), Q(0)),
PY|    (c, Q(-123, 80), Q(0)),
PY|    (d, Q(0), Q(15, 8)),
PY|    (e, Q(0), Q(21, 8)),
PY|    (f, Q(-243, 80), Q(0)),
PY|)
PY|for t, low, high in ODD_ENDPOINTS:
PY|    need((value(OM, t), value(OP, t)) == (low, high),
PY|         "ODD_ENDPOINT_EXACT_VALUE", str(t))
PY|
PY|EVEN_ENDPOINTS = (
PY|    (Q(0), EM, Q(15, 4), 1),
PY|    (a, EP, Q(-9529, 8000), -1),
PY|    (b, EP, Q(-5, 4), -1),
PY|    (c, EM, Q(9, 4), 1),
PY|    (d, EM, Q(2), 1),
PY|    (e, EP, Q(-19, 4), -1),
PY|    (f, EP, Q(-53, 4), -1),
PY|)
PY|for t, envelope, exact, required_sign in EVEN_ENDPOINTS:
PY|    need(value(envelope, t) == exact,
PY|         "EVEN_ENDPOINT_EXACT_VALUE", str(t))
PY|    for member in CORNERS:
PY|        E, O = parity_values(member, t)
PY|        need(sign(E) == required_sign,
PY|             "CORNER_HB_ENDPOINT_SIGN", str((t, member)))
PY|        need(member[0] + member[2] + member[4] + member[6] > 0,
PY|             "HB_REAL_POINT_EVEN_ORIENTATION")
PY|        need(member[1] + member[3] + member[5] + member[7] > 0,
PY|             "HB_REAL_POINT_ODD_ORIENTATION")
PY|
PY|h = Q(1, 10000)
PY|NODES = (Q(1, 2), Q(39, 40), Q(1) - h, Q(1) + h, Q(7, 2))
PY|LABELS = (("+", "+"), ("+", "-"), ("+", "+"), ("-", "+"), ("-", "+"))
PY|MEMBERS = tuple(corner(ep, op) for ep, op in LABELS)
PY|need(all(t > 0 for t in NODES) and
PY|     all(NODES[i] < NODES[i + 1] for i in range(4)),
PY|     "POSITIVE_ORDERED_DISTINCT_NODES")
PY|
PY|POINTS = tuple(sorted(set((Q(0), a, b, c, d, e, f) + NODES)))
PY|for t in POINTS:
PY|    values = tuple(parity_values(member, t) for member in CORNERS)
PY|    need(min(x[0] for x in values) == value(EM, t) and
PY|         max(x[0] for x in values) == value(EP, t),
PY|         "FINITE_EVEN_ENVELOPE", str(t))
PY|    need(min(x[1] for x in values) == value(OM, t) and
PY|         max(x[1] for x in values) == value(OP, t),
PY|         "FINITE_ODD_ENVELOPE", str(t))
PY|
PY|EO = tuple(parity_values(member, t)
PY|           for member, t in zip(MEMBERS, NODES))
PY|FV = tuple(value(F, t) for t in NODES)
PY|HP = tuple(prod((t - s for j, s in enumerate(NODES) if j != i),
PY|                start=Q(1)) for i, t in enumerate(NODES))
PY|EXPECTED = (
PY|    (Q(1, 4), Q(45, 8), Q(-1), Q(1424999943, 4000000000)),
PY|    (Q(-78259, 64000), Q(-14241, 64000), Q(-5499, 64000),
PY|     Q(-119935581, 160000000000)),
PY|    (Q(-1249899964999, 10**12), Q(800060001, 10**12),
PY|     Q(-349974999, 10**12), Q(62240039502, 10**16)),
PY|    (Q(-1750099965001, 10**12), Q(-799940001, 10**12),
PY|     Q(350024999, 10**12), Q(-62760039498, 10**16)),
PY|    (Q(2), Q(15, 8), Q(35, 4), Q(189374999697, 4000000000)),
PY|)
PY|for i, ((E, O), t, (ep, op)) in enumerate(zip(EO, NODES, LABELS)):
PY|    need((E, O, FV[i], HP[i]) == EXPECTED[i],
PY|         "EXACT_ATOM_TABLE", str(i + 1))
PY|    E_factor = prod((r - t for r in E_ROOTS), start=Q(1))
PY|    E_factor += Q(1, 4) if ep == "+" else Q(-1, 4)
PY|    roots = OP_ROOTS if op == "+" else OM_ROOTS
PY|    O_factor = prod((r - t for r in roots), start=Q(1))
PY|    need((E, O) == (E_factor, O_factor),
PY|         "RAW_COEFFICIENT_VS_FACTOR_ATOM", str(i + 1))
PY|need(tuple(sign(O) for E, O in EO) == (1, -1, 1, -1, 1),
PY|     "ODD_RAY_ORIENTATION")
PY|need(tuple(sign(x) for x in HP) == (1, -1, 1, -1, 1),
PY|     "LAGRANGE_DERIVATIVE_SIGNS")
PY|MU = tuple(1 / (t * EO[i][1] * HP[i]) for i, t in enumerate(NODES))
PY|need(all(w > 0 for w in MU), "POSITIVE_RAY_WEIGHTS")
PY|
PY|def verify_even_minimizers(members):
PY|    for i, (member, t) in enumerate(zip(members, NODES)):
PY|        need(member in CORNERS, "ACTUAL_CORNER_MEMBERSHIP", str(i + 1))
PY|        selected = parity_values(member, t)[0] * value(F, t)
PY|        minimum = min(parity_values(v, t)[0] * value(F, t)
PY|                      for v in CORNERS)
PY|        need(selected == minimum, "EVEN_POINTWISE_MINIMIZER", str(i + 1))
PY|
PY|verify_even_minimizers(MEMBERS)
PY|
PY|def verify_moments(weights):
PY|    for r in range(4):
PY|        moment = sum((weights[i] * t ** (r + 1) * EO[i][1]
PY|                      for i, t in enumerate(NODES)), Q(0))
PY|        need(moment == 0, "ODD_MOMENTS", str((r, moment)))
PY|
PY|verify_moments(MU)
PY|for r in range(5):
PY|    lagrange = sum((t ** r / HP[i] for i, t in enumerate(NODES)), Q(0))
PY|    need(lagrange == (Q(1) if r == 4 else Q(0)),
PY|         "LAGRANGE_NORMALIZATION", str(r))
PY|
PY|ROWS = []
PY|for t, (E, O) in zip(NODES, EO):
PY|    row = []
PY|    for j in range(8):
PY|        k = j // 2
PY|        row.append(((-1) ** k) * t ** (k + j % 2) *
PY|                   (O if j % 2 else E))
PY|    need(tuple(row) == (E, t*O, -t*E, -t*t*O,
PY|                        t*t*E, t**3*O, -t**3*E, -t**4*O),
PY|         "RAW_ROW_SIGN_CONVENTION")
PY|    ROWS.append(tuple(row))
PY|M = tuple(sum((MU[i] * ROWS[i][j] for i in range(5)), Q(0))
PY|          for j in range(8))
PY|U = tuple(sum((MU[i] * t**r * EO[i][0]
PY|               for i, t in enumerate(NODES)), Q(0)) for r in range(4))
PY|need(M == (U[0], Q(0), -U[1], Q(0), U[2], Q(0), -U[3], Q(0)),
PY|     "ALL_EIGHT_COORDINATES")
PY|need(tuple(sign(x) for x in M) == (-1, 0, 1, 0, -1, 0, 1, 0),
PY|     "AGGREGATE_SIGNS_NOT_EIGHT_STRICT_NEGATIVES")
PY|need(MU[0] < Q(5, 3) and MU[4] < Q(1, 180) and MU[2] > 5000000,
PY|     "EVEN_MOMENT_WEIGHT_BOUNDS")
PY|for r in range(4):
PY|    need(0 < MU[0] * NODES[0]**r * EO[0][0] < 1,
PY|         "FIRST_POSITIVE_EVEN_CONTRIBUTION", str(r))
PY|    need(0 < MU[4] * NODES[4]**r * EO[4][0] < 1,
PY|         "LAST_POSITIVE_EVEN_CONTRIBUTION", str(r))
PY|    need(MU[2] * NODES[2]**r * EO[2][0] < -2500000,
PY|         "DOMINANT_NEGATIVE_EVEN_CONTRIBUTION", str(r))
PY|    need(U[r] < -2499998, "EVEN_MOMENT_STRICT_BOUND", str(r))
PY|
PY|B = (Q(0), Q(0), Q(9, 2), Q(0), Q(11, 2), Q(0), Q(1), Q(0))
PY|CONTRIBUTIONS = tuple(MU[i] * EO[i][0] * FV[i] for i in range(5))
PY|L = sum(CONTRIBUTIONS, Q(0))
PY|for i in range(5):
PY|    need(sum((B[j] * ROWS[i][j] for j in range(8)), Q(0)) ==
PY|         EO[i][0] * FV[i], "COEFFICIENT_ROW_PAIRING", str(i + 1))
PY|need(sum((B[j] * M[j] for j in range(8)), Q(0)) == L,
PY|     "DIRECT_AGGREGATE_PAIRING")
PY|need(Q(9, 2)*M[2] + Q(11, 2)*M[4] + M[6] == L,
PY|     "EVEN_COORDINATE_PAIRING_IDENTITY")
PY|
PY|C = []
PY|for i, (t, (E, O), (ep, op)) in enumerate(zip(NODES, EO, LABELS)):
PY|    offset = Q(1, 4) if ep == "+" else Q(-1, 4)
PY|    E_factor = prod((r - t for r in E_ROOTS), start=Q(1)) + offset
PY|    if op == "+":
PY|        cancelled = -E_factor * (Q(9, 2) - t) / ((3 - t) * (5 - t))
PY|    else:
PY|        numerator = prod((r - t for r in F_ROOTS), start=Q(1))
PY|        denominator = t * prod((r - t for r in OM_ROOTS), start=Q(1))
PY|        cancelled = E_factor * numerator / denominator
PY|    need(cancelled == E * FV[i] / (t * O),
PY|         "FACTORIZED_VS_COEFFICIENT_SCALAR", str(i + 1))
PY|    C.append(cancelled)
PY|need((C[0], C[1], C[4]) == (Q(-4, 45), Q(-78259, 161600), Q(8, 3)),
PY|     "UNPAIRED_EXACT_CANCELLED_VALUES")
PY|need(sum((C[i] / HP[i] for i in range(5)), Q(0)) == L,
PY|     "FACTOR_FORMULA_TOTAL_PAIRING")
PY|
PY|def D(t):
PY|    return (t - Q(1, 2)) * (t - Q(39, 40)) * (Q(7, 2) - t)
PY|
PY|D3, D4 = D(NODES[2]), D(NODES[3])
PY|need((D3, D4) == (Q(31120019751, 10**12), Q(31380019749, 10**12)),
PY|     "PAIRED_DENOMINATORS_EXACT")
PY|need(HP[2] == 2*h*D3 and HP[3] == -2*h*D4,
PY|     "PAIRED_DERIVATIVE_SIGNS")
PY|direct_pair = CONTRIBUTIONS[2] + CONTRIBUTIONS[3]
PY|factor_pair = (C[2]/D3 - C[3]/D4) / (2*h)
PY|need(direct_pair == factor_pair, "PAIR_DECOMPOSITION_SIGN")
PY|need(0 < C[2] < Q(3, 5) and C[3] > Q(7, 10),
PY|     "PAIRED_NUMERATOR_BOUNDS")
PY|need(D3 > Q(3, 100) and 0 < D4 < Q(4, 125),
PY|     "PAIRED_DENOMINATOR_BOUNDS")
PY|need(direct_pair < -9375, "PAIRED_NEGATIVE_BOUND")
PY|need(CONTRIBUTIONS[0] < 0 and 0 < CONTRIBUTIONS[1] < 1500 and
PY|     0 < CONTRIBUTIONS[4] < 1, "UNPAIRED_CONTRIBUTION_BOUNDS")
PY|need(L < -7874, "FIXED_F_SCALAR_BOUND")
PY|
PY|dF, dO = derivative_value(F, Q(1)), derivative_value(OP, Q(1))
PY|need(value(F, Q(1)) == value(OP, Q(1)) == 0 and
PY|     (dF, dO) == (Q(7, 2), Q(-8)), "DERIVATIVE_COMMON_ZERO_DATA")
PY|g_plus = -dF * value(EP, Q(1)) / dO
PY|g_minus = -dF * value(EM, Q(1)) / dO
PY|need((g_plus, g_minus) == (Q(-35, 64), Q(-49, 64)) and
PY|     g_plus != g_minus, "INCOMPATIBLE_G_AT_ONE")
PY|
PY|CONTROL_RESULTS = []
PY|
PY|def expect_rejection(label, expected_tag, action):
PY|    try:
PY|        action()
PY|    except InvariantError as failure:
PY|        need(failure.tag == expected_tag, "WRONG_MUTATION_FAILURE",
PY|             label + ": " + failure.tag)
PY|        CONTROL_RESULTS.append((label, failure.tag, failure.detail))
PY|    else:
PY|        raise InvariantError("MUTATION_NOT_REJECTED", label)
PY|
PY|def verify_odd_minimum(candidate):
PY|    true_min = min(parity_values(v, Q(1))[1] for v in CORNERS)
PY|    need(value(candidate, Q(1)) == true_min, "ODD_ENVELOPE_MINIMUM",
PY|         "candidate=" + str(value(candidate, Q(1))) +
PY|         ", true_min=" + str(true_min))
PY|
PY|verify_odd_minimum(OM)
PY|bad_odd = list(OM)
PY|bad_odd[1] = Q(-23)
PY|bad_member = list(corner("-", "-"))
PY|bad_member[3] = Q(23)
PY|need(tuple(bad_member) in CORNERS, "MUTATION_SETUP_ODD_ACTUAL_MEMBER")
PY|need(value(tuple(bad_odd), Q(1)) ==
PY|     parity_values(tuple(bad_member), Q(1))[1] == Q(-7, 80),
PY|     "MUTATION_SETUP_ODD_VALUE")
PY|need(value(tuple(bad_odd), Q(1)) - value(OM, Q(1)) == Q(7, 20),
PY|     "MUTATION_SETUP_ODD_GAP")
PY|expect_rejection("wrong odd envelope coefficient", "ODD_ENVELOPE_MINIMUM",
PY|                 lambda: verify_odd_minimum(tuple(bad_odd)))
PY|
PY|bad_members = list(MEMBERS)
PY|bad_members[3] = corner("+", "+")
PY|need(all(v in CORNERS for v in bad_members),
PY|     "MUTATION_SETUP_STALE_EVEN_ACTUAL")
PY|need((parity_values(bad_members[3], NODES[3])[0] - EO[3][0]) * FV[3] ==
PY|     FV[3] / 2 > 0, "MUTATION_SETUP_STALE_EVEN_GAP")
PY|expect_rejection("stale actual even minimizer", "EVEN_POINTWISE_MINIMIZER",
PY|                 lambda: verify_even_minimizers(tuple(bad_members)))
PY|
PY|bad_mu = list(MU)
PY|bad_mu[0] *= 2
PY|need(all(w > 0 for w in bad_mu), "MUTATION_SETUP_POSITIVE_WEIGHTS")
PY|bad_moment = sum((bad_mu[i] * t * EO[i][1]
PY|                  for i, t in enumerate(NODES)), Q(0))
PY|need(bad_moment == 1 / HP[0] > 0, "MUTATION_SETUP_MOMENT_RESIDUAL")
PY|expect_rejection("positive weight moment corruption", "ODD_MOMENTS",
PY|                 lambda: verify_moments(tuple(bad_mu)))
PY|
PY|bad_pair = (C[2]/D3 + C[3]/D4) / (2*h)
PY|need(bad_pair - direct_pair == C[3] / (h*D4) > 0,
PY|     "MUTATION_SETUP_PAIRED_SIGN_GAP")
PY|expect_rejection(
PY|    "wrong paired sign", "PAIR_DECOMPOSITION_SIGN",
PY|    lambda: need(bad_pair == direct_pair, "PAIR_DECOMPOSITION_SIGN",
PY|                 "addition does not reconstruct the direct pair"))
PY|
PY|need(len(CONTROL_RESULTS) == 4, "CONTROL_COUNT")
PY|print("FINITE_CHECKS_PASS")
PY|print("actual_corner_count", len(CORNERS))
PY|for i in range(5):
PY|    print("atom", i + 1, "u", NODES[i],
PY|          "member", " ".join(str(x) for x in MEMBERS[i]))
PY|    print("E O F Hprime", EO[i][0], EO[i][1], FV[i], HP[i])
PY|    print("mu", MU[i], "scalar_contribution", CONTRIBUTIONS[i])
PY|for r, x in enumerate(U):
PY|    print("U", r, x)
PY|for j, x in enumerate(M):
PY|    print("M", j, x)
PY|print("aggregate_signs", tuple(sign(x) for x in M))
PY|print("L_direct", L)
PY|print("L_factorized", sum((C[i] / HP[i] for i in range(5)), Q(0)))
PY|print("paired_contribution", direct_pair)
PY|print("required_G_at_one", g_plus, g_minus)
PY|for label, tag, detail in CONTROL_RESULTS:
PY|    print("CONTROL_REJECTED", label, tag, detail)
PY|print("LIMITS: finite exact checks only; no universal HB/cusp gate,")
PY|print("novelty, other-F exclusion, or common-SPR synthesis acceptance.")

## 9. Unpaid gates and final verdict

The delivered mathematical certificate is complete in literal inputs, exact rational expressions, derivation, independently written code, and four intended-invariant controls. The remaining gates are distinct:

1. **Parent executable replay:** materialize and pin the source, run the stated argv, and retain actual output, exit status, and elapsed time. No executable PASS is claimed here.
2. **Written-proof disposition:** separately adjudicate universal cusp coverage and all-member HB applicability; finite results do not replace that review.
3. **Parent disposition:** all candidate material remains UNREVIEWED until that disposition.
4. **Novelty and original target:** no novelty conclusion, universal common-SPR synthesis theorem, or full common-SPR counterexample has been established.

No PPT-map assertion, whether ordinary positivity or 2-positivity, is part of this SPR-only freeze.

**overall_correctness:** correct  
**explanation:** The selected finite mathematical claims are supported by independent exact written derivations, including the mixed eight-coordinate aggregate and the fixed-\(F_\partial\) bound \(L<-7874\). The checker is complete but NOT RUN, and neither universal written-proof acceptance nor the original synthesis problem is discharged.  
**confidence:** 0.97