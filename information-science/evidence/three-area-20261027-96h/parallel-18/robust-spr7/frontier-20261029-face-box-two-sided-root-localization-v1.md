# Two independent atom measures force a common numerator root off both Vieta faces

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 18:18:52 PDT 2026**. **WRITTEN candidate with WRITTEN-checked-in-kernel exact rational finite certificates**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. This is a nonvacuous structural statement about one explicit solvable box, not a universal septic verdict.

## 1. Result and named box

Use the all-seven-positive-width all-Hurwitz septic box in `frontier-20261029-pattern-c-entire-vieta-face-failure-v1.md`, SHA-256 `6ab23593f984a52e0585cb0c3d53edb629a2b2f891047f8eedabf73598b5bbf9`. Its first odd-band upper endpoint is \(b=21/20\), and its second odd-band lower endpoint is \(c=221/20\), so \(c-b=10\). The explicit common monic numerator and whole-half-line exact evidence are in `frontier-20261029-pattern-c-face-box-common-numerator-v1.md`, SHA-256 `82c4427dff213aa1b69d015c53b20300829e11de12a83e737c68fd6143c6311c`.

**Theorem.** Normalize any common exact-degree-seven SPR numerator so its positive \(s^6\) coefficient is 1, and let \(x_2\) be the middle positive root of its even part. Then
\[
\boxed{\frac{21}{20}+\frac{10}{10001}
<x_2<\frac{221}{20}-\frac{10}{45001}.} \tag{1}
\]
The known common numerator has \(x_2=2\), so this is not a vacuous condition. The upper bound is from the original five-atom measure; the new lower bound is supplied by a **different** seven-finite-atom measure below.

## 2. The opposite-face positive atom measure

Number the four actual parity corners as
\((E_-,O_-),(E_-,O_+),(E_+,O_-),(E_+,O_+)\), with indices 0,1,2,3. Take the following positive uncompactified finite atoms:
\[
\begin{array}{c|c|l}
t&\text{corner}&\text{weight}\\\hline
51/50&2&4015855900970183/37973372538528000\\
26/25&3&6901716941257183/27526194023328000\\
11/10&1&8740548914377783/1434393363150000000\\
11051/1000&0&2108596929980920000/1938953146413556637634879\\
17&0&409/10000000000\\
22&2&1729/1000000000\\
23&2&441/10000000000.
\end{array} \tag{2}
\]
Give compactified infinity weight 1. All finite atoms are actual corners of the same interval box, and
\[
\sum_iw_it_iO_i(t_i)(-t_i)^r+\mathbf1_{r=3}=0,\qquad r=0,1,2,3. \tag{3}
\]
The finite weights in the compactified convention are \(w_i(1+t_i)^7\).

For \(x_1\in\{0,1\}\), \(x_2\in\{b,c\}\), and \(x_3\in\{241/20,441/20\}\), define its weighted even vertex pairing
\[
H(x_1,x_2,x_3)=\sum_iw_iE_i(t_i)(x_1-t_i)(x_2-t_i)(x_3-t_i). \tag{4}
\]
All eight exact rational sums are frozen in `frontier-20261029-face-box-opposite-odd-measure-frozen-v1.json`, SHA-256 `09a093ffa80fd0a48c92dc15c0c5c6a5131d8519c714cc94f1cb96c034a433d7`. The four on the \(x_2=b\) face are each **strictly below** \(-3/50\); those on the \(x_2=c\) face are each strictly between 10 and 600. Multi-affinity extends these bounds across the complete two faces.

## 3. Deriving the lower bound and compatibility

For a common numerator, strict positivity at each actual atom and at compactified infinity, together with the odd cancellation (3), forces \(H(x_1,x_2,x_3)>0\). Write \(\theta=(x_2-b)/(c-b)\). Since
\[
H(x_1,x_2,x_3)<-\frac{3}{50}(1-\theta)+600\theta,
\]
positivity implies \(\theta>1/10001\), hence \(x_2>b+10/10001\). The upper bound in (1) is independently derived from the earlier measure in the named common-numerator packet. These two measures exclude opposite faces but **cannot** be combined into an unrestricted no-go: the explicit common numerator proves the actual box has one.

As an exact consistency check, at the normalized even roots \((1/2,2,20)\) of that numerator, the weighted even pairings for **both** opposite-face measures are strictly greater than 1. These are separate measures with separately normalized positive weights; no common scaling comparison is inferred.

## 4. Assurance and limits

All seven finite weights, four zero odd moments, eight new vertex pairings, the rational face bounds and the two positive interior pairings were computed with exact Python `fractions.Fraction`/integer arithmetic in one Eval host. Root interlacing, face interpolation and the common-numerator implication are written deductions. The known numerator's whole-half-line positivity uses the named compactified Bernstein/Sturm evidence, not this finite atom calculation. No independent scientific review, formal proof, parent adoption or novelty clearance occurred. The root bounds apply only to the displayed box; the original arbitrary-box synthesis-or-obstruction verdict remains **OPEN**. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
