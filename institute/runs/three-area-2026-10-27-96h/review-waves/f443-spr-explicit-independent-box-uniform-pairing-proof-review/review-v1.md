# f443 — Independent written review of the explicit septic-box construction

**Role:** WRITTEN ONLY  
**Disposition proposed to parent:** Scoped written support; no automatic adoption.  
**Findings:** **0 FATAL / 0 MAJOR / 0 MINOR** within the frozen mathematical scope.

The construction proves a common strictly positive-real numerator for the stated actual independent coefficient boxes, including the positive-width enlargement in all seven nonleading coefficients. It does **not** prove common-SPR synthesis for every all-Hurwitz septic interval box.

## 1. Reviewed inputs and process boundary

The reviewed wave is:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f443-spr-explicit-independent-box-uniform-pairing-proof-review/`

Binding metadata, **attributed to the parent’s supplied observation rather than reviewer execution**:

- Manifest SHA256: `0dd92d6be0fe2148740c7b62b654ffb1a4c390b908fafa3122b48dca7ee956fc`
- Freeze-receipt SHA256: `fde30f372dd48f4006dd90061e49213e5c1d9c46499dd56e63e9de5091f4ad9c`
- Literal-packet SHA256: `8817fbcfcb9df7933ea4e5bc06096f3b6592ac0ea51086e611c2748b3441509e`
- Parent metadata observation: `2026-10-30T11:31:28-0700 PDT`

I completely read the manifest, freeze receipt, dispatch receipt, parent metadata supply, and all eight required status-only controls before reading the mathematical packet. I sent the administrative pre-body ACK directly to the parent. A subsequent administrative correction qualified manually transcribed receipt end-line counts; it did not change the complete-through-EOF reading assertion or introduce mathematical work.

I then read the **entire literal packet, LF1–519, consecutively in raw windows of at most 20 LF**, including both source endings, before reconstruction. No elision was encountered.

Mathematical coverage was:

- **S1:** Author candidate, whole-file SHA256 `904626d4371b26e5a007313d186ff8bdbc89827df68dd2a76d480c32659f87d8`, **selected LF1–475 only**. The author program and subsequent material were excluded.
- **S2:** Actual-box boundary disposition, SHA256 `c01abb40d552fb72954ba0918166a80fcf2eeddb5938cb06d25da8a1ad14d6b7`, **complete LF1–42**.

All reasoning below is formal-parameter reconstruction. No newly chosen mathematical instance, private diagnostic, scientific execution, CAS, interpreter, enumeration, finite replay, author program, sibling return, external source-follow, or held mathematical payload was used.

In particular, the entire F439 mathematical episode and all its consumers remained **HELD/ZERO/NONINPUT**, as did the other declared held episodes and consumers. Their status controls supplied exclusions, not mathematical premises.

This is the complete review body for parent materialization. No working-tree file was created.

## 2. Exact theorem under review

Define

\[
F(t)=\left(\frac12-t\right)(2-t)(4-t)
=4-11t+\frac{13}{2}t^2-t^3
\]

and

\[
G(t)=(1-t)(3-t)(5-t)
=15-23t+9t^2-t^3.
\]

The proposed fixed numerator is

\[
q(s)=F(-s^2)+sG(-s^2)
=s^7+s^6+9s^5+\frac{13}{2}s^4+23s^3+11s^2+15s+4.
\]

The core box \(B_0\) consists of

\[
a(s)=s^7+s^6+a_5s^5+\frac{13}{2}s^4+a_3s^3+11s^2+a_1s+a_0,
\]

with independent intervals

\[
a_0\in[3,5],\qquad
a_1\in[1197/80,15],\qquad
a_3\in[23,467/20],\qquad
a_5\in[179/20,9].
\]

Put

\[
m=\frac{65}{4096},\qquad
\gamma=\frac{m}{7^6},\qquad
\varepsilon_*=\frac{\gamma}{38}.
\]

For \(0\le\varepsilon\le\varepsilon_*\), the enlarged box \(B_\varepsilon\) independently enlarges each nonleading coefficient interval by \(\varepsilon\), including the three core fixed coefficients:

\[
\begin{aligned}
a_0&\in[3-\varepsilon,5+\varepsilon],\\
a_1&\in[1197/80-\varepsilon,15+\varepsilon],\\
a_2&\in[11-\varepsilon,11+\varepsilon],\\
a_3&\in[23-\varepsilon,467/20+\varepsilon],\\
a_4&\in[13/2-\varepsilon,13/2+\varepsilon],\\
a_5&\in[179/20-\varepsilon,9+\varepsilon],\\
a_6&\in[1-\varepsilon,1+\varepsilon].
\end{aligned}
\]

The leading coefficient stays exactly one.

**Reviewed conclusion:** Every member of every such \(B_\varepsilon\) is strictly Hurwitz, and the same \(q\) satisfies

\[
F(t)E_a(t)+tG(t)O_a(t)
\ge \frac{\gamma}{2}(1+t)^6>0
\quad(t\ge0),
\]

where \(a(i\omega)=E_a(\omega^2)+i\omega O_a(\omega^2)\). Consequently \(q/a\) is an equal-degree SPR transfer function for every member.

## 3. Claim-by-claim reconstruction

### C1. The endpoint cubics are actual independent-box envelopes

**SUPPORTED — S1 LF19–49, LF106–126.**

For a core member,

\[
E_a(t)=a_0-11t+\frac{13}{2}t^2-t^3
      =F(t)+c,\qquad c=a_0-4\in[-1,1],
\]

and

\[
O_a(t)=a_1-a_3t+a_5t^2-t^3.
\]

For every \(t\ge0\), coefficient independence makes the actual minimizing odd endpoint

\[
L(t)=\frac{1197}{80}-\frac{467}{20}t+\frac{179}{20}t^2-t^3
=\left(\frac{19}{20}-t\right)\left(\frac72-t\right)\left(\frac92-t\right),
\]

and the actual maximizing endpoint \(U(t)=G(t)\). In particular,

\[
L(t)\le O_a(t)\le U(t)
\]

holds simultaneously for every actual independent coefficient choice. The same endpoint coefficient choices attain these envelopes throughout \(t\ge0\).

The factorization of \(L\) is consistent with:

\[
\frac{19}{20}+\frac72+\frac92=\frac{179}{20},
\]

\[
\frac{19}{20}\left(\frac72+\frac92\right)+\frac72\frac92
=\frac{467}{20},
\]

and constant term \(1197/80\). Thus

\[
U-L=\frac3{80}+\frac7{20}t+\frac1{20}t^2>0.
\]

These are actual box endpoints, not an abstract pair of cubics whose simultaneous coefficient feasibility has been assumed.

The earlier actual box recorded in S2 LF27–28 is contained in \(B_0\): only its constant interval changes, from \([15/4,17/4]\) to \([3,5]\). No missing source is needed for that containment.

### C2. Every core denominator is strictly Hurwitz

**SUPPORTED, with the named classical Hermite–Biehler import — S1 LF129–166.**

Set the source’s fixed root markers

\[
(a,b,c_1,d,e,f)
=\left(\frac{19}{20},1,3,\frac72,\frac92,5\right).
\]

The endpoint envelope signs give an actual odd root in each closed interval

\[
[a,b],\qquad[c_1,d],\qquad[e,f].
\]

For example, \(O_a(a)\ge L(a)=0\) and \(O_a(b)\le U(b)=0\); the corresponding opposite endpoint inequalities hold on the other two bands. The intervals are disjoint. A cubic therefore has exactly one root in each, with all three roots distinct and simple.

The even-part bounds on the complete closed odd bands are:

\[
F\le-\frac{27}{20}\quad\text{on }[19/20,1],
\]

\[
F\ge\frac94\quad\text{on }[3,7/2],
\]

\[
F\le-5\quad\text{on }[9/2,5].
\]

The first and third follow from nonnegative factor bounds. For the middle band, \(F''=13-6t<0\), and the already specified endpoints give \(F(3)=5/2\) and \(F(7/2)=9/4\).

Consequently, every \(E_a=F+c\), \(|c|\le1\), is strictly negative, positive and negative, respectively, on those complete bands. Since \(E_a(0)=a_0\ge3\), it has a root in each open gap

\[
(0,19/20),\qquad(1,3),\qquad(7/2,9/2).
\]

Again degree three exhausts the root count and proves simplicity. Thus, writing the even roots as \(\alpha_j\) and odd roots as \(\beta_j\),

\[
0<\alpha_1<\beta_1<\alpha_2<\beta_2<\alpha_3<\beta_3
\]

for **every** independent core coefficient choice.

The orientation is the Hurwitz orientation: both parity cubics have leading coefficient \(-1\), and \(E_a(0)>0\), \(O_a(0)>0\). All original polynomial coefficients are positive, also giving the source’s positive real-point orientation.

The exact imported classical HB implication is: for these real parity polynomials with positive simple roots in this alternating order and this orientation, \(E_a(-s^2)+sO_a(-s^2)\) is strictly Hurwitz. The candidate satisfies its hypotheses uniformly. This is not a corner-sampling argument.

The displayed \(q\) belongs to \(B_0\), so the same argument proves \(q\) strictly Hurwitz.

### C3. All seven frequency cases have the claimed positive bounds

**SUPPORTED — S1 LF170–358.**

For every core member,

\[
P_a(t)=F(t)E_a(t)+tU(t)O_a(t),
\]

and

\[
F E_a\ge F^2-|F|\ge-\frac14.
\]

The last inequality is the universal square inequality
\((|F|-1/2)^2\ge0\).

The only bands where \(L\) and \(U\) have opposite signs are

\[
J_1=[19/20,1],\quad
J_2=[3,7/2],\quad
J_3=[9/2,5].
\]

Outside their union, \(UO_a\ge0\). The three separate even-root neighborhoods are

\[
I_1=[1/4,3/4],\quad
I_2=[3/2,5/2],\quad
I_3=[15/4,17/4].
\]

The following checks are interval-wide bounds, not selected-frequency tests.

**First even-root neighborhood.** On \(I_1\), factorwise minima give

\[
U\ge\frac{153}{64}>2,\qquad
L\ge\frac{33}{16}>2.
\]

Thus \(tUO_a\ge1\), giving \(P_a\ge3/4\).

**Second even-root neighborhood.** On \(I_2\), \(O_a\le U<0\), so \(UO_a\ge U^2\), and

\[
|U|=(t-1)(3-t)(5-t)\ge\frac58.
\]

Therefore \(tUO_a\ge75/128\), giving \(P_a\ge43/128\).

**Third even-root neighborhood.** On \(I_3\),

\[
L=(t-19/20)(t-7/2)(9/2-t)\ge\frac7{40}>\frac18,
\]

\[
U=(t-1)(t-3)(5-t)\ge\frac{99}{64}>1.
\]

It follows that \(tUO_a\ge15/32\), giving \(P_a\ge7/32\).

**First odd band.** On \(J_1\), \(L\le0\le U\), with

\[
U\le\frac{3321}{8000}<\frac12,\qquad
|L|\le\frac{3621}{8000}<\frac12.
\]

Since \(O_a\ge L\) and \(t\le1\), this gives \(tUO_a\ge-1/4\). Also \(|F|\ge27/20\), hence

\[
F E_a\ge\frac{27}{20}\frac7{20}=\frac{189}{400}.
\]

The claimed \(P_a\ge89/400\) follows.

**Middle odd band.** On \(J_2\), the product is exactly

\[
U|L|=(t-1)(5-t)(t-19/20)(9/2-t)(t-3)(7/2-t).
\]

Its three grouped bounds are

\[
(t-1)(5-t)\le4,
\]

\[
(t-19/20)(9/2-t)\le\frac{123}{40},
\]

\[
(t-3)(7/2-t)\le\frac1{16}.
\]

The middle product is decreasing throughout this interval because its derivative is \(109/20-2t<0\). Together with \(t\le7/2\), these prove

\[
tUO_a\ge-\frac{861}{320}.
\]

The even contribution is at least \(45/16=900/320\), leaving exactly \(39/320\).

**Last odd band.** On \(J_3\),

\[
U|L|=(t-1)(t-3)(t-19/20)(t-7/2)(5-t)(t-9/2).
\]

The source’s factor bounds yield

\[
tU|L|
\le5\cdot4\cdot2\cdot\frac{81}{20}\cdot\frac32\cdot\frac1{16}
=\frac{243}{16}.
\]

Since \(|F|\ge5\), the even contribution is at least \(20\). Thus \(P_a\ge77/16\).

**Remaining frequencies.** Outside the \(I_j\), the four closed pieces have lower bounds

\[
\begin{array}{c|c}
\text{Piece}&|F|\text{ lower bound}\\ \hline
[0,1/4]&105/64\\
[3/4,3/2]&65/64\\
[5/2,15/4]&91/64\\
[17/4,\infty)&135/64.
\end{array}
\]

The exterior pieces follow from factorwise monotonic bounds. On the second piece, \((-F)''=6t-13<0\); on the third, \(F''=13-6t<0\). Their endpoint minima give the displayed bounds.

For the remainder **outside the odd bands as well**, \(UO_a\ge0\), so

\[
P_a\ge\frac{65}{64}\left(\frac{65}{64}-1\right)
=\frac{65}{4096}.
\]

That restriction matters: the complement table overlaps odd bands, but the proof does not apply the nonnegative odd-product assertion inside those bands. They have already received their separate bounds.

The resulting seven-case bounds are

\[
\frac34,\quad\frac{43}{128},\quad\frac7{32},\quad
\frac{89}{400},\quad\frac{39}{320},\quad\frac{77}{16},\quad
\frac{65}{4096}.
\]

Their minimum is \(m=65/4096\). All cases apply on closed endpoints; overlaps cause no inconsistency. The complement includes zero and the unbounded tail. There is no uncovered frequency.

### C4. The normalized global margin is valid

**SUPPORTED — S1 LF366–398.**

For \(t\ge6\), \(O_a\le U<0\) and

\[
|U|=(t-1)(t-3)(t-5)\ge\frac5{72}t^3.
\]

The even contribution is nonnegative there, giving

\[
P_a(t)\ge\frac{25}{5184}t^7.
\]

Also,

\[
(1+t)^6\le(7/6)^6t^6<3t^6,
\]

where \(7^6<3\cdot6^6\). Therefore

\[
\frac{P_a(t)}{(1+t)^6}\ge\frac{25}{2592}.
\]

For \(0\le t\le6\), the already proved \(P_a\ge m\) gives

\[
P_a(t)\ge\frac{m}{7^6}(1+t)^6.
\]

Since \(25/2592>m/7^6\), both ranges establish

\[
P_a(t)\ge\gamma(1+t)^6
\]

for every core member and every \(t\ge0\). The joining endpoint is covered by both arguments.

### C5. The enlargement genuinely permits independent variation in all seven coefficients

**SUPPORTED — S1 LF403–449.**

Coordinatewise projection onto the core intervals gives, for every actual enlarged member,

\[
a=a_*+\delta a,\qquad a_*\in B_0,\qquad
|\delta a_j|\le\varepsilon\ (0\le j\le6),\qquad\delta a_7=0.
\]

This representation imposes no coefficient correlation.

The perturbation parities are

\[
\delta E=\delta a_0-\delta a_2t+\delta a_4t^2-\delta a_6t^3,
\]

\[
\delta O=\delta a_1-\delta a_3t+\delta a_5t^2.
\]

Thus

\[
|\delta E|\le\varepsilon(1+t)^3,\qquad
|\delta O|\le\varepsilon(1+t)^2.
\]

The stated coefficient comparisons also hold:

\[
|F|\le4(1+t)^3,\qquad |G|\le15(1+t)^3.
\]

Consequently,

\[
|F\delta E+tG\delta O|
\le4\varepsilon(1+t)^6+15\varepsilon t(1+t)^5
\le19\varepsilon(1+t)^6.
\]

Combining this with C4 proves

\[
F E_a+tG O_a
\ge(\gamma-19\varepsilon)(1+t)^6
\ge\frac{\gamma}{2}(1+t)^6>0
\]

because \(\varepsilon\le\gamma/38\).

The radius is conservative but valid. For every positive allowed \(\varepsilon\), all seven nonleading coefficient intervals have positive width. At \(\varepsilon=0\), the statement correctly reduces to the four-dimensional core.

### C6. Stability persists along the complete enlargement path

**SUPPORTED — S1 LF451–463.**

For an arbitrary enlarged member, the path

\[
a_\lambda=a_*+\lambda\delta a,\qquad0\le\lambda\le1,
\]

satisfies the same positive pairing bound throughout.

An imaginary-axis zero would force that pairing to vanish: for nonzero \(\omega\), both \(E_{a_\lambda}(\omega^2)\) and \(O_{a_\lambda}(\omega^2)\) would vanish; at zero, its even part would vanish. Both contradict strict positivity.

The path is monic, fixed-degree and coefficient-bounded, so a uniform Cauchy root bound prevents escape through infinity. Continuity of polynomial roots then makes the number of roots in each open half-plane invariant while the imaginary axis remains root-free.

The initial member is strictly Hurwitz by C2. Hence every final enlarged member is strictly Hurwitz. This proves stability for every coefficient choice, not only for corners.

### C7. The positive pairing produces the claimed common SPR numerator

**SUPPORTED — S1 LF465–472.**

For every real frequency,

\[
\operatorname{Re}\frac{q(i\omega)}{a(i\omega)}
=
\frac{F(t)E_a(t)+tG(t)O_a(t)}
     {E_a(t)^2+tO_a(t)^2}>0,\qquad t=\omega^2.
\]

The denominator is nonzero by C6, and the numerator is positive by C5. Both polynomials are monic septics, so the ratio tends to one at infinite frequency.

Thus the construction pays both denominator stability and strict frequency positivity; it does not infer stability merely from an inequality away from possible poles. With the standard stable, real-rational, equal-degree SPR convention used in the packet, the conclusion follows.

Every nonempty independent subbox inherits the result because all preceding inequalities are pointwise for every member of the containing box.

### C8. The fixed even roots remain interior, and all actual zero-odd-moment combinations have positive pairing

**SUPPORTED by reconstruction from S1 LF79–100 and LF403–472, using S2’s actual-box conventions.**

For the core box, the source’s root locations immediately give

\[
0<\frac12<a<b<2<c_1<d<4<e<f.
\]

The three fixed test roots therefore lie strictly inside the common intervals \([0,a]\), \([b,c_1]\), \([d,e]\).

The enlarged-box claim can also be paid without assuming that its odd endpoint roots stay at their old values. Use only the three fixed roots of \(F\) already specified in the source. At each such root \(\tau\), the positive pairing becomes

\[
\tau G(\tau)O_a(\tau)>0.
\]

The signs of \(G\) at the three fixed roots are positive, negative and positive, respectively. Therefore **every** enlarged odd cubic has those same alternating signs there. Its leading term is \(-t^3\), so it has exactly one simple root in each interval

\[
(1/2,2),\qquad(2,4),\qquad(4,\infty).
\]

The actual enlarged endpoint envelopes are

\[
L_\varepsilon=L-\varepsilon(1+t+t^2),\qquad
U_\varepsilon=U+\varepsilon(1+t+t^2),
\]

and \(L_\varepsilon<U_\varepsilon\) on \(t\ge0\). Write their roots, in the packet’s convention, as \((a_\varepsilon,d_\varepsilon,e_\varepsilon)\) and \((b_\varepsilon,c_\varepsilon,f_\varepsilon)\). Their signs and strict envelope inequality imply

\[
\frac12<a_\varepsilon<b_\varepsilon<2
<c_\varepsilon<d_\varepsilon<4
<e_\varepsilon<f_\varepsilon.
\]

This proves the claimed strict interior placement for the enlarged boxes too.

For the cone claim, take any nonzero finite positive combination of **actual** atoms, with frequencies \(t_i\ge0\), actual member parities \(E_i,O_i\), weights \(\mu_i\ge0\), and the four vanishing odd numerator-coordinate sums:

\[
\sum_i\mu_i t_i^{k+1}O_i(t_i)=0,\qquad k=0,1,2,3.
\]

Since \(G\) is cubic, these equations imply

\[
\sum_i\mu_i t_iG(t_i)O_i(t_i)=0.
\]

Hence

\[
\begin{aligned}
\sum_i\mu_iF(t_i)E_i(t_i)
&=\sum_i\mu_i\bigl(F(t_i)E_i(t_i)+t_iG(t_i)O_i(t_i)\bigr)\\
&\ge\frac{\gamma}{2}\sum_i\mu_i(1+t_i)^6>0.
\end{aligned}
\]

This argument covers every such actual combination, without selecting an R5 orientation or discarding degenerate cases. In particular it covers actual R4 rays, both actual R5 orientations, zero-odd singletons and same-frequency cancellation rays.

No independent classification of extreme rays is needed for this implication, and no claim about additional, unspecified closure constructions is being added.

## 4. Imports, exclusions and acceptance gates

### Mathematical imports retained

1. **Classical Hermite–Biehler:** Used only at the precise parity-root and orientation scope stated in C2. Its hypotheses were reconstructed for every core member.
2. **Elementary root continuity and a Cauchy root bound:** Used for the fixed-degree monic coefficient path in C6.
3. **The stable equal-degree SPR convention:** Used after strict Hurwitz stability, positive real-frequency pairing and the positive limit at infinity have all been established.

The HB link appearing in S2 was **not followed**. This review does not claim new primary-source authentication, complete external-paper coverage, or external formal-proof replay.

### What S2 did and did not supply

S2 supplied the previously recorded actual-box coefficients and the actual boundary-root/cone conventions. Its reported prior review findings, finite-check results, author-check execution, exact fixed-test fraction and linked artifacts were **not replayed or used as verification evidence for this candidate**.

The present proof does not depend on that fixed-test failure. It constructs a different, interior-root common test and directly proves its all-member, all-frequency positive pairing.

### Paid within this WRITTEN duty

- Actual coefficient independence and feasibility of the envelopes.
- Every core odd root and strict even/odd interlacing.
- The named HB orientation.
- Every frequency case, rational lower bound, overlap and endpoint.
- The unbounded tail and normalized margin.
- The \(19\varepsilon\) perturbation bound and \(\gamma/38\) radius.
- All-member enlarged-box stability.
- Equal-degree SPR positivity.
- Interior test-root placement and positive pairings on the stated actual finite cone combinations.

### Unpaid or outside this duty

- Independent scientific execution or finite-check replay.
- Author-program review.
- Public-source authenticity and novelty.
- Independent-family, human or formal-kernel verification.
- Parent adoption and original-target acceptance.
- A universal theorem for arbitrary all-Hurwitz septic boxes.
- An eight-strict-negative obstruction or nonexistence certificate.

**Code and argv:** Not applicable to this WRITTEN assignment. No scientific checker was authored or run, and the author’s excluded program was not inspected. No paid API, model CLI, installation, network research, build, test, lint or formatter was invoked.

## 5. Verdict

**FATAL: 0. MAJOR: 0. MINOR: 0.**

The frozen explicit-box construction is supported at its stated scope, with the named classical HB import retained. Its decisive feature is an actual uniform positive pairing for the entire independent box, followed by a quantitative seven-coefficient perturbation argument and a complete no-crossing stability proof.

This is a scoped same-harness written review, **not** self-adoption, independent-family verification, kernel certification, novelty clearance, or closure of the arbitrary-box original target.

**overall_correctness:** correct  
**explanation:** The explicit core-box and seven-coefficient enlargement theorem survives formal reconstruction, including all frequency cases, strict stability, and the actual cone-pairing consequences. No mathematical defect was found within the frozen scope; broader synthesis and external acceptance gates remain unclaimed.  
**confidence:** 0.97