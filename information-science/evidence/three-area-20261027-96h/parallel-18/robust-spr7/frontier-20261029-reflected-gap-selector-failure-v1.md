# An exact counterexample to the reflected-gap selector

Owner InfoSPR7-2, info-2. Actual native clock observed before writing: **Thu Oct 29 17:34:17 PDT 2026**. **WRITTEN countermechanism with WRITTEN-checked-in-kernel exact rational evidence**, not independently reviewed, parent-adopted, formally verified or novelty-cleared. It excludes one natural data-dependent selector formula, not the general selector LP or SPR synthesis.

## 1. The failed formula

For the mixed-band pattern \(a<t_1<t_2<b<t_3<t_4<c<t_5<d\), the rule
\[
\theta_{\rm ref}=\frac{c-(t_3+t_4)/2}{c-b},\qquad
\xi=(1-\theta_{\rm ref})t_3+\theta_{\rm ref}t_4,\qquad
F(t)=(-t)(\xi-t)(d-t) \tag{1}
\]
is a plausible reflected-gap choice: it moves toward \(t_4\) when both middle nodes approach \(b\), and toward \(t_3\) when they approach \(c\). It is **not** a universal raywise selector, even on an all-seven-width Hurwitz box.

## 2. Exact eligible box and atom ray

Use odd extrema
\[
O_-=-(t-1)(t-33/5)(t-83/5),\qquad
O_+=-(t-11/10)(t-61/10)(t-171/10),
\]
whose positive independent odd intervals are
\[
a_1\in[2739/25,114741/1000],\quad
 a_3\in[12983/100,3319/25],\quad
 a_5\in[121/5,243/10].
\]
The odd-root bands are \([1,11/10],[61/10,33/5],[83/5,171/10]\). Take even interval endpoints, in \((a_0,a_2,a_4,a_6)\) order,
\[
\ell=(6/125,2993/100,633/40,249/250),\qquad
u=(7549/500,7397/125,15827/1000,251/250). \tag{2}
\]
All seven widths are positive. The six even-envelope sign margins at the odd-band endpoints are
\[
1/1000,\ 3/500000,\ 16863/500000,\ 1272177/125000,\
84556337/125000,\ 424471043/500000,
\]
all strictly positive; Hermite–Biehler and independent parity mixing therefore make the **entire** septic box Hurwitz.

Take the five-node tuple
\[
(t_1,t_2,t_3,t_4,t_5)=(41/40,109/100,111/100,23/20,131/20).
\]
Rule (1) gives \(\theta_{\rm ref}=497/500\) and \(\xi=3593/3125\). Choose the Y ray supported at \((t_1,t_2,t_4,t_5)\), odd components \((O_-,O_+,O_+,O_+)\), even components \((E_+,E_+,E_-,E_-)\), and compactified infinity weight 1. These are actual parity corners. Their positive uncompactified finite weights are
\[
\left(\frac{163840000000}{16364863697},\frac{50000000000000}{930856658823},
\frac{320000000}{58835403},\frac{1600000000}{44171428366611}\right).
\]
The four odd moments cancel exactly with infinity. The corresponding even values are
\[
-393459/16000000,\quad-1436273/125000000,\quad
-12150699/250000,\quad4620921/500000.
\]
The aggregate even pairing with the prescribed \(F\) is
\[
-\frac{37948472389931876}{134654917150723416890625}<0. \tag{3}
\]
Thus this actual four-node circuit defeats (1).

For this same box and ray, the pairing is affine and strictly increasing in \(\theta\), with zero at
\[
\theta_* =\frac{26692855371867607021363}{26853979132819104478438}
>\frac{497}{500}. \tag{4}
\]
A different Vieta vertex, with roots \((0,c,d)\), has strictly positive pairing
\(3537821467941254213348/430035663555204525\). Therefore this is **not** a weak no-go and does not refute a common numerator.

## 3. Assurance and boundary

The six stable-box sign margins, positivity of the finite weights, four zero odd moments, pairing (3), threshold (4), and the positive alternative vertex were computed using exact integers and Python `fractions.Fraction` on one Eval host. The root-band stability and affine interpolation deductions are written mathematics. No independent review, formal proof, parent adoption or novelty clearance is claimed.

This result blocks only the explicit reflected-gap rule (1). It does not show that a different data-dependent \(\theta\), the exact 16-ray selector LP in `frontier-20261029-direct-mixed-band-uniform-selector-lp-v1.md` (SHA-256 `b5380caec863a2c4e807db1aab912ee3aed2bc37fe72d2d0382d7b1262c4f36e`), another numerator family, or unrestricted synthesis fails. Process ancestry includes `owner-incidental-held-source-search-display-v1.json`, SHA-256 `dfb30abdebfc8785870e14fdba5d4e55574ded5fafef86647db1eb74d8abd724`; no clean-cognition claim is made.
