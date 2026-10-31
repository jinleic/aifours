# A strictly wider level-six 125-type ratio cone via a mixed left test

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:23:12 PDT 2026**. This is an UNREVIEWED exact-program-assisted strengthening of `frontier-20261028-level6-226-full-target-ratio-cone-candidate-v1.md`, SHA `6e8049679de3cd2d78f390edf0393d0abf31e6a0e65d531356f0d3a47bafb7d3`, and its exact-endpoint addendum SHA `d15e30f600e8e4c3aba81f3968c767947c7cdb8291f00a6f3b70119106e6599e`. Neither earlier file is edited. No parent/formal/kernel, independent-model/human, novelty or priority verdict is conferred.

## 1. Exact enlarged region

For every integer `r,s>=6` and every allowed FULL complex Cartan realization of the original A(r,s), the same named unreviewed source/PBW and exact-code inputs imply that the ENTIRE actual map

\[
D_3:P_{(2,2,6)}\longrightarrow S_{(2,2,5)}
\]

is injective whenever

\[
r+s-12\ \ge\ \frac{217}{50}|r-s|.\tag{1}
\]

Equality is INCLUDED. This is a broader ratio cone than the prior `9/2` cone and also broader than the prior **exact optimal coefficient for the particular left test `L^T`**, whose eigenvalue endpoint is strictly greater than `449/100`. For example, every integer `q>=1` gives

    r=6+269q,  s=6+169q,
    r+s-12=438q,  |r-s|=100q.

The new condition holds because `438q>=434q`, while the old sharp L-left criterion fails because its threshold is strictly greater than `449q`. This is an explicit symbolic infinite family showing strict extension on the actual integer lattice; it is not an assertion of an optimal cone, whole-quadrant injectivity, F6/B6, all-level Serre, arbitrary GCM, novelty or priority.

## 2. The full-target mixed-left forms

Use the previously independently reconstructed full 235-row/34-source pencil

\[
D=A+xB+yC=A+mL+dK,\quad L=B+C,\quad K=B-C,\quad
x=r-6,\ y=s-6,\ m=(x+y)/2,\ d=(x-y)/2.
\]

Set the NEW auxiliary left test `X=L+A/50`. Define

\[
H_0^X=X^TA+A^TX,\quad H_L^X=X^TL+L^TX,\quad
H_K^X=X^TK+K^TX,\quad \lambda=217/50.
\]

The old exact certificate/replay proved `H0=L^TA+A^TL` and `HL=2L^TL` strictly positive definite. Therefore

\[
H_0^X=H_0+\tfrac1{25}A^TA\succ0,\qquad
H_L^X=H_L+\tfrac1{50}H_0\succ0.\tag{2}
\]

The new exact producer verifies BOTH rational matrices `lambda H_L^X ± H_K^X` have 34 strictly positive LDL pivots. A separately authored replay independently reconstructs both entire matrices from ALL 235 actual target rows and verifies their **68 exact positive leading principal determinants** via integer Bareiss. These are symmetric rational coordinate forms; they are not a claimed invariant or contravariant positive form on the nonsymmetrizable Lie algebra.

## 3. All-variable proof, equality included

For a nonzero complex source vector z,

\[
2\Re((Xz)^*Dz)=z^*\bigl(H_0^X+mH_L^X+dH_K^X\bigr)z.
\]

Condition (1) is exactly `m>=lambda |d|`. For either sign of d,

\[
mH_L^X+dH_K^X=(m-\lambda|d|)H_L^X
 +|d|(\lambda H_L^X\pm H_K^X)\succeq0.
\]

By (2), the baseline `H0^X` is strictly positive, so the whole right side is positive even on the boundary. If `Dz=0` the left side is zero, contradiction. The full target word host is faithful at the named PBW/free-Levi input, and r,s>=6 ensures both actual node-3 seed ideals vanish through level6. This proves entire-source injectivity at exactly the stated inputs and region.

The earlier `L^T` algebraic endpoint remains EXACTLY sharp **for that earlier specific left test's two PSD slope constraints**; it is not contradicted by changing X. The earlier failed `A^T`-left PSD shortcut remains failed. No positive invariant form on the original nonsymmetrizable Lie algebra and no `D^*D` identity is assumed.

## 4. Exact receipts and observed failure history

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-226-mixed-left-cone-certificate.py` | 42 | `4d6ad518ff8c954f3d177f1822700073dc8aebb7159100fec7842f90c65fad94` |
| `frontier-20261028-level6-226-mixed-left-cone-certificate-v1.json` | 3769 | `3e2ccacbcc8ee5a16c79a6db53ee23536ed1e1b01b9ef2cef43ba0951610a533` |
| `frontier-20261028-level6-226-mixed-left-cone-independent-replay.py` | 43 | `3c91b3d0c9c585ace4b7d0a69da8b00d0ac872f877c2425a532eb47ba79f7ace` |
| `frontier-20261028-level6-226-mixed-left-cone-independent-replay-v1.json` | 87 | `3b4e5422bf9a75dbedd351f2070e4d21cffb6d1e545f876275cbe1c73825678c` |

The producer returned `PASS X=L+A/50, lambda=217/50: both 34x34 slope forms have positive LDL pivots` at **19:22:46 PDT**. The separately authored replay returned `PASS ... direct full-target construction and 68 positive exact Sylvester minors` at **19:23:12 PDT 2026-10-28**. Both use integer/Fraction and share some generic local helpers; this is not formal or independent-vendor review.

Two earlier exploratory Python Eval cells failed at **parse time** because of unmatched brackets; neither executed, wrote output files or constituted a numerical result. The corrected exploratory cells were followed by the separately saved exact producer and independent replay above. The original 235-row/source/tree-Jacobi replay, the old sharp-L-left lower witness, the named PBW/source inputs and the s>=6 ideal-absence proof remain essential. The earlier incidental older cone-status methodological exposure and all prior ZERO/STOP/HOLD/process findings persist; no old held guide is a premise.

**END — strictly wider mixed-left 125-type ratio cone, exact conditional candidate pending review.**
