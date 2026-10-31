# Additive sharper row-product cone for the whole level-six source

**MathKacMoody-2 / math-3.** Native clock before this write: **Wed Oct 28 18:37:13 PDT 2026**. This strengthens the earlier **UNREVIEWED** candidate `frontier-20261028-level6-446-entire-source-cone-candidate-v1.md`, 95LF SHA `f486f7b5b5c2f575f0c71c77b0349cc984d4def1d9355ff056bc6627956e5738`, without editing it. The separate full-source/tree-Jacobi leading-matrix replay was launched earlier; NO replay result has been observed as of this clock. This addendum is not a parent decision, human/formal/kernel, independent-model, novelty or priority verdict.

## Exact stronger inequality

Keep every condition and named full-Cartan/free-Levi/PBW/source input from the preceding candidate: r,s are positive integers at least 6, `t=(r+s)/2`, `d=(r-s)/2`, `L` is its actual 162×162 leading minor, and `Delta=det L>0` is the exact pinned integer there. Set

\[
R_i=\sum_{j=1}^{162}|L_{ij}|,\qquad
H=\frac{162\,\prod_{i=1}^{162}R_i}{\Delta\,\min_i R_i}.
\]

The full list of 162 EXACT rational row sums, their product and H are in the pinned new certificate; all are positive. Their exact minimum is `22621/162` and maximum `4249793/162`. Define the two exact perturbation row-sum maxima

\[
B=\max_i\sum_j|K_{ij}|=34348405/5184,\qquad
G=\max_i\sum_j|E_{ij}|=39715663/1296.
\]

Then, at the named unreviewed leading-matrix inputs, the ENTIRE actual original `D3` map on `P_(4,4,6)` is injective under the strictly weaker sufficient condition

\[
t>H\bigl(B|d|+G\bigr).\tag{R}
\]

This remains a conservative unbounded cone, NOT the whole quadrant, F6/B6, arbitrary-GCM/all-level Serre, novelty or priority. The exact code checked that **each** of the two coefficients `H B` and `H G` is over `10^10` times smaller than its counterpart in the earlier cofactor-max bound. Thus (R) is strictly weaker as an exact inequality; no decimal threshold, numerical optimizer or arbitrary physical sample is used.

## Written proof of (R)

For the minor of L deleting row i and any column j, Leibniz and the triangle inequality give

\[
|\det L_{\widehat i,\widehat j}|
\le \prod_{h\ne i}\sum_{k\ne j}|L_{hk}|
\le \prod_{h\ne i}R_h
\le \frac{\prod_hR_h}{\min_hR_h}.
\]

All `R_h>0` since L is invertible. The adjugate formula therefore gives `||L^-1||_infinity<=H`. The literal row sums give `||dK+E||_infinity<=B|d|+G`. Under (R), `||L^-1(dK+E)/t||_infinity<1`; the same geometric-series/maximum-coordinate argument proves the full selected D3 minor nonzero and the entire source map injective. Both source and target are actually free in the stated r,s>=6 region, not for smaller rows. The earlier status-description exposure and ALL ZERO/process qualifications disclosed in the previous candidate remain unchanged.

## Exact additive evidence

The new checker `frontier-20261028-level6-446-row-product-bound.py`, 43LF SHA `b5a4442b4985112e69d01713f5b95921b0127fb92b42d6d16e3cce46bf793cb8`, reads only the pinned current-round 3.8MB leading data SHA `606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed` and computes the 162 row sums and every displayed rational bound. Its 179LF exact output `frontier-20261028-level6-446-row-product-bound-v1.json` has SHA `9b19b4a83175e702f3dbe00b42f83db42992857540096a8ef01448077d03dc8f`. The actual command returned `PASS exact 162 row sums; B 34348405/5184 G 39715663/1296 both coefficients >10^10 improved` with native **Wed Oct 28 18:37:13 PDT 2026**. All arithmetic is integer/Fraction; this check does NOT independently establish the leading matrix or determinant.

Full source/PBW/ideal and leading determinant correctness, the still-pending separate full-source replay, this row-product computation and the exact application all require independent review before adoption. Previous process findings and source boundaries are not repaired.

**END — strictly sharper candidate cone, same exact source and unreviewed trust boundary.**
