# F501 WRITTEN review: complete-competitor lower exclusion

**Verdict at the assigned lower-exclusion scope: SUPPORTED, conditional on the named canonical-reduction and actual-attainment imports.**

**New findings: 0 FATAL / 0 MAJOR / 0 MINOR.** The historical f419 penalty-sign **1 MAJOR** and the frozen erroneous f400/f418 assertions remain unchanged. This review neither clears them retrospectively nor uses their unsigned penalty claim.

## 1. Read order, provenance, and execution boundary

Before reading the mathematical packet, I completely read:

- `manifest-v1.json`, lines 1–120;
- `freeze-receipt-v1.json`, through its ending;
- `parent-live-metadata-supply-v1.json`, through its ending;
- all ten `controls_before_body`, through their endings, as status-only controls.

I then sent Main a direct administrative pre-body ACK. Only afterward did I read the complete literal packet, raw and in order, in the windows 1–20, 21–40, continuing in consecutive windows of at most 20 LF through 541–560, then 561–573. This includes the candidate’s ending at source-labelled S1 line 471 and the complete S2 and S3 endings. The reconstruction below followed that complete read.

The assigned F501 pins are:

- Manifest: `3c086ca477ac8c6fbce70ff46c502d11cce2aefb292e874fd0f75271a74a1cd3`.
- Freeze receipt: `8eb855a488afe690d0833123fe5acf2f2e55849381635c02fb525dfed395956a`.
- Literal packet: `c92029922f6d85d79b7376be5b6346bd47bd45ff1858afe5bb91cc9f9becde9c`.

Their matching hashes, byte/LF counts, and the clock `2026-10-30T12:27:03-0700 PDT` are **parent-supplied observations**, not my own hashing, native start time, or execution evidence.

**Scientific execution: NOTRUN, as required by the WRITTEN role.** No scientific code, CAS, interpreter, solver, enumeration, numerical integration, build, test, lint, or formatter was run. The calculations below are written identities. I used no new selected mathematical instance: the numerical substitutions are the manuscript’s competitor \(t=1/2\) and its prescribed lower-root bracket endpoints \(7/100\) and \(3/40\).

No linked author code, sibling review, external mathematical source, or held scientific payload was opened. All quarantined episodes and their consumers—including f439, f444, f448 and the privacy auxiliary-parameter episode—remain **HELD/ZERO/NONINPUT**. Their status records supply no mathematical premise or confidence evidence.

The tool interface does not provide working-tree file writing. No repository file was created or changed; this is the complete review body for parent materialization, without a write bypass.

## 2. Exact scope and imports

This gate reviews S1 §4, source-labelled lines 133–180: the genuine canonical competitor, its complete normalized objective, the polynomial \(L\), the bracket for \(\alpha\), and the strict necessary lower exclusion.

The load-bearing imported facts are:

1. **Canonical optimization and actual attainment.** S2 lines 7–16 supply the corrected canonical fixed-scalar reduction, positive denominator, unique signed-value zero, and an attained actual cutoff-two value
   \[
   \frac12<V\le2,\qquad
   V=\min_{a\ge0,\ c\ge a+1/2}\rho(a,c).
   \]
   These remain named conditional imports, not newly proved original-regime facts.

2. **Complete diamond-edge calibration.** S2 lines 49–53 give the full normalized edge value, including geometric tails:
   \[
   e(a;\lambda)
   =\frac23M_4(2a)-2\lambda M_2(2a)
   -\text{the explicitly retained core improvement}.
   \]
   The first two terms are the complete all-diamond comparison value, not a core-only surrogate.

3. **Normalization and corrected accounting.** S3 lines 7–19 retain the geometric normalization, deterministic constant, and complete tail accounting. In particular, the geometric expectation is not to be multiplied by an additional external \(1-b\).

The lower proof does **not** require the upper-bound quartic certificate, rounded-branch monotonicity, the proposed \(\beta\)-endpoint classification, or the synthetic example in S2 line 55. It also does not use a sign for the full endpoint difference or infer global edge dominance from the corrected penalty monotonicity statement.

## 3. The supplied competitor is admissible independently of stationarity

The manuscript selects
\[
t=\frac12,\qquad a=\frac14,\qquad c=\frac34=a+\frac12.
\]

This scalar pair belongs to the retained canonical domain \(a\ge0,\ c\ge a+1/2\). Its diamond core is the upper-face profile \(F_0(y)=2a-y\); the next diamond has radius \(2c=2a+1\), and subsequent radii are \(t+k\). These are the compatible diamond profiles occurring in the imported complete edge calibration.

Crucially, feasibility does not require this selected profile to solve the fixed-scalar projection, the scalar stationarity equations, or the original optimization. The argument uses its objective as an **upper comparison for a global minimum**. It does not assert that the competitor is itself an actual optimizer.

Thus S1 lines 151–155 provide the correct kind of comparison object for the claimed lower exclusion.

## 4. Reconstruction of the complete normalized objective

For a formal diamond radius \(s\), the area and quadratic-moment contributions underlying the imported calibration are
\[
A(s)=2s^2,\qquad B(s)=\frac23s^4.
\]
For example, the full quadratic moment is
\[
4\int_0^s
\left(\frac{(s-y)^3}{3}+y^2(s-y)\right)\,dy
=\frac23s^4.
\]

With
\[
\Pr(G=k)=(1-b)b^k,\qquad
M_j(t)=\mathbb E(G+t)^j,
\]
the complete diamond sequence consequently gives
\[
\begin{aligned}
Z_t
&=(1-b)\sum_{k\ge0}b^k\,2(t+k)^2
=2M_2(t),\\
N_t
&=(1-b)\sum_{k\ge0}b^k\,\frac23(t+k)^4
=\frac23M_4(t).
\end{aligned}
\]

Equivalently, its complete signed value is
\[
H_\lambda(C_t)
=\frac23M_4(t)-2\lambda M_2(t),
\]
in agreement with S2 lines 49–53. This agreement concerns evaluation of the diamond competitor; it does not require the clipped fixed-scalar minimizer to remain on the diamond branch.

Therefore
\[
R_t(m)=\frac{N_t}{Z_t}
=\frac{M_4(t)}{3M_2(t)}.
\]

The factor \(1-b\) is already inside the distribution of \(G\). No deterministic constant or geometric tail is removed, and no extra \(1-b\) is appended.

**Assessment of S1 lines 135–149: SUPPORTED.**

## 5. Reconstruction of the moments and \(L(m)\)

Write \(m=b/(1-b)>0\). The geometric falling-factorial identities give
\[
\mathbb E(G)_{\underline j}=j!m^j
\]
for the moment orders used in the manuscript. Expanding ordinary powers yields
\[
\begin{aligned}
\mathbb EG&=m,\\
T_2=\mathbb EG^2&=m+2m^2,\\
T_3=\mathbb EG^3&=m+6m^2+6m^3,\\
T_4=\mathbb EG^4&=m+14m^2+36m^3+24m^4.
\end{aligned}
\]

Hence
\[
\begin{aligned}
M_2(t)&=t^2+2mt+T_2,\\
M_4(t)&=t^4+4mt^3+6T_2t^2+4T_3t+T_4.
\end{aligned}
\]

At the manuscript-supplied \(t=1/2\), these become
\[
M_2(1/2)=\frac14+2m+2m^2>0
\]
and
\[
M_4(1/2)
=\frac1{16}+5m+29m^2+48m^3+24m^4.
\]

Subtracting the correct threshold multiple gives
\[
\begin{aligned}
M_4(1/2)-\frac32M_2(1/2)
&=24m^4+48m^3+26m^2+2m-\frac5{16}\\
&=\frac1{16}
\left(384m^4+768m^3+416m^2+32m-5\right).
\end{aligned}
\]

Thus the claimed polynomial
\[
L(m)=384m^4+768m^3+416m^2+32m-5
\]
has the stated coefficients. More explicitly,
\[
R_{1/2}(m)-\frac12
=\frac{L(m)}{48M_2(1/2)}.
\]
The denominator is strictly positive, so the sign comparison is valid without an exceptional zero-denominator case.

**Assessment of S1 lines 159–169: SUPPORTED.**

## 6. Unique positive root and prescribed exact brackets

The derivative is
\[
L'(m)=1536m^3+2304m^2+832m+32>0
\qquad(m\ge0).
\]
Thus \(L\) is strictly increasing on the entire nonnegative domain.

The prescribed endpoint evaluations can be checked by clearing denominators:
\[
\begin{aligned}
100^4L(7/100)
={}&384\cdot7^4
+768\cdot7^3\cdot100
+416\cdot7^2\cdot100^2\\
&+32\cdot7\cdot100^3-5\cdot100^4\\
={}&-44\,895\,616,
\end{aligned}
\]
so
\[
L(7/100)=-\frac{350747}{781250}<0.
\]

Similarly,
\[
\begin{aligned}
40^4L(3/40)
={}&384\cdot3^4
+768\cdot3^3\cdot40
+416\cdot3^2\cdot40^2\\
&+32\cdot3\cdot40^3-5\cdot40^4\\
={}&194\,944,
\end{aligned}
\]
and therefore
\[
L(3/40)=\frac{1523}{20000}>0.
\]

Continuity gives a zero between these positive endpoints, and strict monotonicity makes it the unique positive zero. Consequently,
\[
\frac7{100}<\alpha<\frac3{40},
\]
with
\[
L(m)<0\quad(0<m<\alpha),\qquad L(\alpha)=0.
\]

**Assessment of S1 lines 171–175 and the lower-root definition in lines 74–80: SUPPORTED.**

## 7. Global comparison and the strict lower endpoint

Suppose an attained actual cutoff-two optimizer, under the named imports, had \(0<m\le\alpha\). The feasible complete competitor above would satisfy
\[
R_{1/2}(m)\le\frac12.
\]

By global minimality in the retained canonical problem,
\[
V\le R_{1/2}(m)\le\frac12.
\]
This contradicts the imported strict actual-cutoff-two condition \(V>1/2\). Therefore
\[
\boxed{m>\alpha}.
\]

The exclusion includes \(m=\alpha\): at that endpoint the competitor has quotient exactly \(1/2\), which still contradicts \(V>1/2\). The strictness is therefore justified, rather than inferred from a merely non-strict polynomial sign.

This is a global comparison argument with a genuine admissible competitor. It is not stationarity sufficiency, an inference from a selected local root, or an existence argument.

**Assessment of S1 lines 177–180 and line 456: SUPPORTED, conditional on the stated imports.**

## 8. Conversion to \(b\) and separation from the upper-bound gate

For positive parameters,
\[
\frac{x}{1+x}-\frac{y}{1+y}
=\frac{x-y}{(1+x)(1+y)}.
\]
Thus \(m>\alpha\) is equivalent to
\[
\boxed{b>\frac{\alpha}{1+\alpha}}.
\]
Since \(\alpha>7/100\), it also implies the weaker explicit necessary bound
\[
\boxed{b>\frac7{107}}.
\]

If the separate upper-bound gate establishes the candidate’s \(m\le\beta\), then the combination is exactly
\[
\alpha<m\le\beta
\quad\Longrightarrow\quad
\frac{\alpha}{1+\alpha}<b\le\frac{\beta}{1+\beta}.
\]
The lower endpoint is strict; the proposed algebraic upper endpoint remains non-strict. Conditional additionally on the separately established \(\beta<33/100\),
\[
\frac{\beta}{1+\beta}<\frac{33}{133}.
\]
Accordingly, the displayed weaker consequence
\[
\frac7{107}<b<\frac{33}{133}
\]
has the correct endpoint directions.

**Assessment of S1 lines 107–123: SUPPORTED as an algebraic consequence of the lower theorem reviewed here plus the independently established upper theorem.** This is not independent support from F501 for the upper theorem itself.

The existence and uniqueness of \(\beta\), its quartic certificate, coverage of the rounded branch, and the claimed endpoint conditions \(V=2\), \(a=s(\beta)/2\), and diamond-branch selection are **not adjudicated by this lower-exclusion gate**. Their status here is **INCONCLUSIVE / OUTSIDE ASSIGNED RECONSTRUCTION**, not refuted.

## 9. Findings and acceptance boundary

**Current mathematical findings: none — 0 FATAL / 0 MAJOR / 0 MINOR at the assigned F501 scope.**

The supported new statement is:

> Under the named corrected canonical reduction, complete normalized objective, and attained actual cutoff-two hypothesis \(V>1/2\), the manuscript’s feasible all-diamond competitor proves the necessary condition
> \[
> m>\alpha,\qquad
> b>\frac{\alpha}{1+\alpha}>\frac7{107},
> \]
> where \(\alpha\) is the unique positive zero of \(L\) and \(7/100<\alpha<3/40\).

This review does **not** establish:

- actual cutoff-two attainment at any parameter;
- sufficiency or nonemptiness of the actual regime;
- the separate upper exclusion or its endpoint classification;
- a global value formula or an all-\(\epsilon\) formula;
- unreduced-law uniqueness or original book/source equivalence;
- novelty, priority, human review, independent-family review, or formal-kernel acceptance.

The historical penalty-sign MAJOR remains permanent. No held episode or consumer is rehabilitated.

**Overall correctness:** correct.

**Explanation:** At the assigned lower-exclusion scope, the competitor is admissible, its complete normalized numerator and denominator give the stated polynomial, both exact bracket evaluations are correct, and global minimality supplies the claimed strict contradiction. The combined \(b\)-bounds are correct only conditional on the separately reviewed upper theorem; no regime-existence claim follows.

**Confidence:** 0.99 at this explicitly conditional lower-exclusion scope.