# Universal exclusion of strict five-positive-node certificates for septic boxes

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 19:06:22 PDT 2026**. **WRITTEN theorem candidate**, with a named WRITTEN-checked-in-kernel integer positivity certificate. It is not parent-adopted, independently reviewed, Lean/kernel-verified or novelty-cleared.

## 1. Result and scope

Let \(K\) be any compact independent coefficient box of monic real septic polynomials, every member strictly Hurwitz. No positive-weight aggregate of actual denominator/frequency pairing atoms at **five distinct positive squared frequencies**, even with any additional zero and/or compactified-infinity atoms, has all eight numerator-monomial coordinates strictly negative.

In fact, combining this with the named direct phase-classification/sign-variation result, any such strict-negative aggregate on an eligible box needs **at least six distinct positive frequencies**. This addresses the resumed five-node direct-certificate question. It does **not** establish a common strictly positive-real numerator for every box, exhibit an eligible no-common-numerator box, or resolve certificates with six or more frequencies. The original unrestricted septic synthesis-or-obstruction problem remains **OPEN**.

The author-written classification `frontier-20261029-strict-negative-certificate-two-band-obstruction-v1.md`, SHA-256 `33cce85c5451984a670de2ae05c921ea3a61d0c88c867c3c81a1bb94cd026783`, excludes fewer than five positive nodes and shows that five can only have phase word
\[
A=(2,1,3,2,4),\quad B=(2,1,3,5,4),\quad C=(2,4,3,5,4). \tag{1}
\]
Phase C is excluded by `frontier-20261029-universal-five-node-phase-c-exclusion-v1.md`, SHA-256 `8c0a03012e79fbdf4d713635bb03d448712e46510ea99bdfc722b01c449ef505`. Phase A is excluded by its variable-leading reciprocal transfer `frontier-20261029-universal-five-node-phase-a-reciprocal-exclusion-v1.md`, SHA-256 `7a9a14ac8cbae0b90772f8b791372fb512c5c7e7c7b18503043224b6a1944b39`. The remainder of this packet excludes phase B.

## 2. An outside-band lemma allowing variable leading coefficients

Let an independent, all-Hurwitz septic coefficient box have positive leading interval rather than necessarily fixed monicity. Write its odd root bands \([a,b],[c,d],[e,f]\), and pointwise odd envelopes
\[
O_- =\lambda_-(a-t)(d-t)(e-t),\quad
O_+=\lambda_+(b-t)(c-t)(f-t),\quad
\lambda_-\ge\lambda_+>0. \tag{2}
\]
Suppose four ordered support nodes obey
\[
a<u_1<u_2<b<u_3<c\le d<u_4<e, \tag{3}
\]
and their actual odd signs are \((- ,+,-,+)\). For every one of the four direct odd-moment interpolation rays, the even test
\[
F(t)=(-t)(c-t)(d-t) \tag{4}
\]
has strictly positive pairing, uniformly over all actual members of this box. The same is true for any nonzero positive combination of such rays. This is the precise variable-leading lemma needed below; the strict \(u_3<c\) avoids any endpoint limiting convention.

At all four nodes \(F<0\), so the actual pairing is bounded below by the even upper envelope. Its root triple lies in the three even-root gaps; multi-affinity reduces it to \(x\in\{0,a\}\), \(y\in\{b,c\}\), \(z\in\{d,e\}\). The minimizing odd endpoints are
\[
\begin{array}{c|cccc}
(y,z)&u_1&u_2&u_3&u_4\\\hline
(b,d)&O_-&O_+&O_+&O_+\\
(b,e)&O_-&O_+&O_+&O_-\\
(c,d)&O_-&O_+&O_-&O_+\\
(c,e)&O_-&O_+&O_-&O_-.
\end{array} \tag{5}
\]
These endpoint minima are valid for the actual scaled box; inside-band reciprocal odd magnitudes can be unbounded, but the corresponding even-test contributions are positive and are minimized at the maximal-magnitude endpoint.

### Unit-shape and scale argument

Temporarily remove \(\lambda_\pm\), retaining exactly the four root-shaped endpoint expressions and choices in (5). Their unit-shape pairing \(S_0\) is positive for all eight even vertices and all four interpolation rays. This follows by the written four-vertex proof in `frontier-20261029-universal-first-odd-band-five-node-exclusion-v1.md`, SHA-256 `c2ee101472efe7e7c6ba4d10e8fd3ab1c78d40f1146307f0feb126b6c59129af`, and the decreasing-weight argument in `frontier-20261029-three-strict-pattern-eight-ray-reduction-v1.md`, SHA-256 `8591da67f304472da00e7afb7bf1ddfc1c2a7970802f7c844cf8cd495ee93686`. Importantly, the selected **unit shapes need not themselves define an independent odd box**. The only place the four-vertex proof names their difference \(\Delta_0=O_+^0-O_-^0\) is \((y,z)=(b,e)\): if \(\Delta_0(u_3)\le0\), its displayed divided-difference numerator is immediately positive because \(\Delta_0(u_2)>0\); if \(\Delta_0(u_3)>0\), the same proof applies using
\[
\frac{\Delta_0(t)}{(f-t)(t-a)(d-t)}
=\frac{e-t}{f-t}+\frac{(b-t)(c-t)}{(t-a)(d-t)}, \tag{6}
\]
whose value at \(u_2\in(a,b)\) exceeds its value at \(u_3\in(b,c)\), and the strict \(h(u_3)/h(u_2)\) comparison displayed there. The remaining vertex cases use only root order and opposite odd signs at their replacement nodes. The nonincreasing elementary-symmetric ray weights preserve those signs, with the two-versus-three domination below handling \((b,d)\).

Separate the unit-shape contributions using an \(O_+\) endpoint as \(S_+\), so the actual pairing is
\[
S=\frac{S_0}{\lambda_-}+
\left(\frac1{\lambda_+}-\frac1{\lambda_-}\right)S_+. \tag{7}
\]
We also have \(S_+>0\). For \(y=c\) this is immediate from (5). For \(y=b\), the positive node-2 contribution alone exceeds the magnitude of the negative node-3 contribution. Indeed, with
\(H(t)=\prod_i(t-u_i)\), \(h(t)=(t-u_1)(u_4-t)\), and the unit odd endpoint at nodes 2 and 3,
\[
\frac{F(t)(x-t)(b-t)(z-t)}{tO_+^0(t)h(t)}
=\frac{t-x}{t-u_1}\frac{d-t}{u_4-t}\frac{z-t}{f-t}. \tag{8}
\]
All three factors are positive and nonincreasing from \(u_2\) to \(u_3\), and the first two are strict: \(x\le a<u_1\), \(d<u_4\), \(z\le e\le f\). Thus the node-2 base contribution exceeds node 3 in magnitude; the ray's elementary-symmetric multipliers satisfy \(q_2\ge q_3>0\). For \(z=d\), any additional \(O_+\) node-4 term is positive. Equation (7) is therefore strict because \(\lambda_-\ge\lambda_+\), proving the lemma.

## 3. Phase B is self-reciprocal

For a phase-B candidate, the named outside-band direct theorem already excludes the case that its third node \(t_3\le c\). In the remaining case, the phase signs force \(c<t_3<d\). Let \([p,q]\) be the box's second **even** root band. Global independent-box interlacing gives \(q<c\).

Reverse coefficients without renormalizing:
\[
a^*(s)=s^7a(1/s),\qquad b^*(s)=s^7b(1/s). \tag{9}
\]
The reciprocal family is again an independent all-Hurwitz coefficient box, with positive variable leading interval equal to the original \(a_0\) interval; it is not generally monic. Compactified pairings satisfy
\[
\frac{P_{a^*,b^*}(1/t)}{(1+1/t)^7}
=\frac{P_{a,b}(t)}{(1+t)^7}. \tag{10}
\]
Therefore positive finite atom weights are unchanged, zero and infinity swap, and reversal of the numerator monomials preserves strict negativity of every coordinate. Phase B's parity word
\[
(--),(-+),(+-),(-+),(++)
\]
is unchanged when frequencies reverse and \((E,O)\mapsto(-O,-E)\). The reciprocal second odd-root band is \([1/q,1/p]\), so its third node satisfies
\[
u_3=1/t_3<1/c<1/q. \tag{11}
\]
The reciprocal B sign pattern and interlacing place its first two nodes in the first odd band, its third strictly in the following gap, and its last two in the third even-root gap. Each of its odd-cone rays therefore satisfies (3), so the variable-leading lemma contradicts strict negativity. Phase B is excluded, completing (1).

## 4. Evidence, conditional corollary, and limits

A fully realized original phase-B box is in `frontier-20261029-pattern-b-mixed-band-selector-lp-v1.md`, SHA-256 `5b5cb29a32ea08c074375bf35c5d2a88d7cd743302099607ffa18fc84e4e49df`. For its five actual members, exact rational checks of the self-reciprocal signs and (10) are frozen in `frontier-20261029-phase-b-self-reciprocal-example-frozen-v1.json`, SHA-256 `b8e9e3483092cb903db639d32e9247501b016004e33e7f2ed501e171a236bd24`; the reciprocal leading interval is \([87/1000,87/500]\). This is a nonvacuity example, not a negative certificate.

**Conditional refinement.** If the separate author-written robustification theorem `frontier-20261029-universal-counterexample-robustification-v1.md`, SHA-256 `6c60f44465c55e786d0871bb6c1e3675557a927087259c618ced8e567353295f`, is also valid, then any original counterexample would yield a rational full-width robustly Hurwitz counterexample with a rational strict-negative certificate on **six to eight distinct positive frequencies**. That statement does not assert such a counterexample exists, nor that a search terminates in the positive case.

The phase-B scaling, sign and reciprocal arguments here are written mathematics. The phase-C first-gap import rests on eight exact integer polynomials with 225,019 positive coefficients and same-host rational point checks; the original phase classification also imports a same-host finite class enumeration. The example's five pairing identities use exact Python `fractions.Fraction` on the same Eval host. None is independent scientific review, parent adoption, formal proof or novelty clearance. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
