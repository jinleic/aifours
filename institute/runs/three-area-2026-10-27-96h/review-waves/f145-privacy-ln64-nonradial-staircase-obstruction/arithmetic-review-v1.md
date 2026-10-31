# f145 arithmetic review — corrected candidate only

Native clock observation before writing: `2026-10-28T21:12:18-0700 PDT`.

## Verdict and scope

**PASS for the specified arithmetic with the mandatory correction applied**, conditional on the candidate's stated all-layer clipped-diamond geometry and the stated staircase cost formula. On that conditional arithmetic scope, the corrected rational bound is strictly greater than `10^-6` for every `gamma` in `[0,1]`. The computation is exact, not a numerical root approximation or a finite geometric-tail truncation.

**Findings:** FATAL 0; unresolved MAJOR 0; MINOR 0 in the corrected arithmetic scope. **Original-candidate MAJOR, resolved only by the mandatory overlay:** the uncorrected Eq. (10) prints a denominator one million times too small, hence a false equality and a claimed lower bound one million times too large. The original bytes remain uncorrected; this verdict requires the source **together with** `parent-required-numeric-correction-v1.json`. The original wrong fraction also exceeds `10^-6`, so that inequality alone would not detect the error.

**INCONCLUSIVE / not assessed by this arithmetic review:** the all-`k` Minkowski-sum identity, disjointness of the four removed caps, actual measure construction, nonradiality and full-event/full-closed-diamond privacy; the unreviewed MDA26/all-radial extension; all-law/global optimality, novelty and priority. The present review cannot by itself promote the conditional arithmetic comparison to an unconditional privacy theorem. Same-harness review is not independent-family or human review, and the checker is not kernel/formal verification.

## Input binding and read order

The complete correction was read and SHA/byte/LF checked **before** the candidate. The complete candidate and then the complete primary-definitions release were read in the manifest's order; the execution rechecked these pins in that order. LF means the number of `0x0a` bytes. The source text was not modified.

| Input | SHA-256 | bytes | LF |
|---|---|---:|---:|
| `manifest-v1.json` | `8b11415d77d1cc66f4a79cf59f4ed441de8ff46436ea06ba6755944214fe6c01` | 3312 | 38 |
| `parent-required-numeric-correction-v1.json` | `3b29787c171857d35099fded30bc7d1c2bd9b957537d64b54891209a8a1197bb` | 1446 | 16 |
| `frontier-20261028-ln64-rational-nonradial-obstruction-v1.md` | `028397b5e5c5cae583f9fc69ed1efadbaeda169c729d3cb878b74b1e2cc14e01` | 7063 | 87 |
| `info-1-mda-primary-definitions-v1.md` | `25740af38e4ed3d36e925be499e7a0fa4920182989c8ba55c99811538fb03718` | 1542 | 9 |

The full paths are bound in `manifest-v1.json` and in the execution receipt. No author or sibling code was imported or executed. No public source expansion was performed.

## Independent reconstruction

Put `b=1/64`, `m=b/(1-b)=1/63`, `a=3761763123/10^10`, `z=3761763124/10^10`, and `eta=1/100`. For `Pr(N=k)=(1-b)b^k`, differentiating the geometric probability-generating function yields `E[(N)_r]=r!m^r`; independently converting factorial to ordinary moments gives

\[
\begin{aligned}
 M_1(g)&=g+\frac1{63},\\
 M_2(g)&=g^2+\frac2{63}g+\frac{65}{3969},\\
 M_4(g)&=g^4+\frac4{63}g^3+\frac{130}{1323}g^2
         +\frac{5804}{83349}g+\frac{102635}{5250987}.
\end{aligned}
\]

The checker separately evaluated the closed geometric power sums through degree four. As an explicit infinite-tail control it verified, for each `j=0,...,4`,

\[
 E N^j=\sum_{k=0}^{6}(1-b)b^k k^j
       +b^7\sum_{r=0}^{j}\binom jr7^{j-r}E N^r.
\]

Thus the displayed costs do not discard the tail.

### Derivative, roots, and the entire staircase interval

For `F(g)=M4(g)/(3 M2(g))`, direct polynomial multiplication gives

\[
 F'(g)=\frac{2P(g)}{3M_2(g)^2},\qquad
 P(g)=g^5+\frac5{63}g^4+\frac{46}{1323}g^3
 -\frac{2642}{83349}g^2-\frac{1495}{83349}g+\frac{65}{250047}.
\]

`M2` is positive on `[0,1]`. Exact evaluations in the executed receipt have signs `P(0)>0`, `P(a)<0<P(z)`, and `P(1)>0`. In particular,

\[
 P(a)=\frac{-59520815474376217149493776262534895636073379}
             {25004700000000000000000000000000000000000000000000000000},\quad
 P(z)=\frac{161638062247006216977565755367438883421347}
             {24418652343750000000000000000000000000000000000000000}.
\]

The coefficient signs in descending degree are `+,+,+,-,-,+`, giving exactly two Descartes sign changes. The intermediate value theorem gives distinct positive roots in `(0,a)` and `(a,z)`. Descartes' rule, counting multiplicity, therefore implies these are the only positive roots and each is simple. The second root `g*` is in `(a,z)`, is the local minimum, and is below `1`. Moreover `F(0)=F(1)=1579/3969`; after `g*`, `F` increases to `F(1)`. Hence `F(g*)` is the global minimum on `[0,1]`. Since both moment polynomials are strictly increasing for nonnegative arguments,

\[
 \min_{0\le g\le1}F(g)=F(g_*)>
 L:=\frac{M_4(a)}{3M_2(z)}
 =\frac{4360956031322694336838386787406708390699272667}
 {26752882574623784652679233600000000000000000000}.
\]

No conclusion about a different family of laws follows from this scalar minimization.

### Integrated cap and clipped cost

Independently integrating monomials on the full diamond gives area `2R^2` and squared-Euclidean moment `(2/3)R^4`. For one stated axis cap, direct integration gives

\[
 \int_0^\eta\int_{-u}^{u}1\,dv\,du=\eta^2,\qquad
 \int_0^\eta\int_{-u}^{u}[(R-u)^2+v^2]dv\,du
 =R^2\eta^2-\tfrac43R\eta^3+\tfrac23\eta^4.
\]

For example, the actually evaluated cap moment at `R=a` is exactly `40967880131488139387/3000000000000000000000000`. Applying the four-cap geometry **as an input assumption** and summing all geometric layers gives

\[
 Z=2M_2(a)-4\eta^2
 =\frac{67325211993630408409001}{198450000000000000000000},
\]

\[
 Q=\tfrac23M_4(a)-4\eta^2M_2(a)+\tfrac{16}{3}\eta^3M_1(a)-\tfrac83\eta^4,
 \qquad J_S=Q/Z
 =\frac{4355768046089487574226880288026708390699272667}
 {26721376640271909097532496900000000000000000000}.
\]

Under those geometry assumptions, `Q/Z` is the actual clipped shell law's cost, not a linearized approximation. As an independent uncut positive control, setting `eta=0` and `g=1/2`, then evaluating the diamond integrals against separate raw geometric-series identities, gives exactly `12549035/71140356`, equal to `M4(1/2)/(3 M2(1/2))`. The uncut zero-core series check also gives `1579/3969`.

## Corrected exact comparison

The independently recomputed **lower bound on** the gap, not the unknown exact optimal gap, is

\[
 \Delta=L-J_S=
 \frac{55892104628095766169604064637687395172793197064705238995982813}
 {28589579218686463271455054512504719394059809867200000000000000000000}.
\]

The strict comparison is certified exactly by

\[
 \Delta-10^{-6}=
 \frac{27302525409409302898149010125182675778733387197505238995982813}
 {28589579218686463271455054512504719394059809867200000000000000000000}>0.
\]

Consequently, given the geometry and staircase-cost premises, `F(g)-J_S >= F(g*)-J_S > Delta > 10^-6` for **every** `g` in `[0,1]`. The corrected bound is approximately `1.954981715560335e-6`; this decimal is orientation only, not evidence in place of the exact fractions.

## Executed positive and negative controls

* The independent `eta=0`, `g=1/2` and zero-core controls pass as above; the explicit geometric tail identities pass for degrees `0,...,4`.
* **Normalization mutation:** replacing four cap areas in the normalizer by three while retaining the four-cap density gives actual integral `67325211993630408409001/67345056993630408409001`, not `1`. It is rejected specifically for failure to normalize.
* **Denominator mutation:** the original Eq. (10) denominator is the corrected denominator divided by `10^6`. The resulting fraction is rejected specifically for failing the recomputed-gap equality; its ratio to the correct fraction is exactly `10^6`. Its still-positive `>10^-6` inequality is not a valid denominator check.
* **Bad root bracket:** `[z,z+10^-10]` has positive `P` at both endpoints and is rejected specifically because it lacks the required negative-to-positive endpoint signs.
* **Coarse but valid bracket:** `[37617/100000,37618/100000]` really does have the required signs; it is **not** rejected as an invalid bracket. Its outward comparison gives the negative exact gap `-3981815887985580532565556044482978917905451333266101/714751649496696168362456686058620160700000000000000000000`, so it is rejected only as an attempted certificate of a `>10^-6` gap. This distinction is recorded in the receipt.

## Actual run and artifact binding

* Executed command: `python3 -B arithmetic-check-v1.py`, in this review directory; process exited `0` and printed `ALL SPECIFIED ARITHMETIC CHECKS PASSED`.
* Run start `2026-10-28T21:11:29.890584-07:00`; computation complete before receipt write `2026-10-28T21:11:29.891574-07:00`, both observed from the local clock in the actual process.
* Independently written standard-library checker: `arithmetic-check-v1.py`, SHA-256 `6faf0bea3c4a2b09f081da116cbd1203b4bcb787c68c812c4538d80d4b4a0d8b` (15012 bytes, 309 LF).
* Actual machine-readable receipt: `arithmetic-receipt-v1.json`, SHA-256 `5e9c10252a295f8c40ffdb75f44e7a529b5dfe1dd190b6743525b596d8668d9a` (6793 bytes, 179 LF). It includes the verified input pins, all exact polynomial coefficients, evaluated signs, tail identities, bound, and mutation reasons/values.
