# The 446 full-target leading-left accretivity form is indefinite

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:17:55 PDT 2026**. New exact-program-assisted negative result at the pinned source; it is UNREVIEWED and is not a parent/formal/human/independent-model verdict, an original-map kernel, or a novelty claim.

## 1. Stronger obstruction than the selected-row version

At the actual degree `(4,4,6)` and the named full-Cartan/free-Levi/PBW inputs of `frontier-20261028-level6-446-entire-source-cone-candidate-v1.md`, SHA `f486f7b5b5c2f575f0c71c77b0349cc984d4def1d9355ff056bc6627956e5738`, let the ENTIRE 162-dimensional lowest source act into all **1780** actual target tensor-word rows. Write the complete exact original f3 pencil as

\[
D=A+xB+yC=A+mL+dK,\qquad L=B+C,\quad K=B-C,
\]

where `x=r-6,y=s-6` and `A=6L+E`. Consider the auxiliary UNWEIGHTED word-coordinate real symmetric form

\[
H_0=L^T A+A^T L.
\]

The whole 162×162 form is **indefinite**: its first diagonal entry is positive, while its 125×125 leading principal determinant is strictly negative. The first 124 fraction-free leading pivots were positive; the next is negative. This now concerns the FULL 1780-row target, not merely the 162 selected rows examined in the earlier `frontier-20261028-level6-446-selected-accretivity-obstruction-v1.md`, SHA `a05f71684e32545e00f7d83df3c562cfa0b05e401b232a6581c56a42ef795f9d`.

Thus the successful type125 `(2,2,6)` ratio proof's PARTICULAR choice of `L^T` and unweighted full-target coordinate pairing does not directly transfer to this 446 source, because its required H0 positive-definiteness is false. This is a concrete exact negative direction for one proposed algebraic method, NOT an assertion that a different left operator, different positive weights, another coordinate representation or a different proof cannot work.

## 2. Entire-target reconstruction and exact sign

The full source pencil `frontier-20261028-level6-446-full-target-pencil-v1.json`, **1,590,481 LF / 31,166,335 B**, SHA `f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3`, lists all 1780 possible target words and every one of the **263,594 nonzero (source-column,L,K,E) triples**. It is assembled from all 1116 source Lyndon words and the entire 162 lowest vectors using independent tree-Jacobi, one source column at a time.

A separate tensor-suffix Jacobi implementation regenerated ALL 1780 rows, all 162 columns and all 263,594 nonzero triples from the same pinned source basis and compared them exactly; it returned PASS. This replays the full target, not just the previously staged 162×162 selected entries. The two paths share generic exact local helpers and are not independent-model or formal verification.

The H0 producer clears the common rational denominator `10368`, computes blocked integer Gram products with a PROVED bound below `2^63` on every int64 block, accumulates the blocks as arbitrary-precision Python integers, and applies integer fraction-free Sylvester elimination. The separate replay reconstructs the full 1780-row Gram restricted to the first125 source columns, verifies its first diagonal is positive, and uses a general exact integer Bareiss determinant to match the whole negative 125×125 leading minor. All displayed Gram integers are scaled by `10368^2>0`; their signs coincide with the rational forms. No floating approximation is involved.

## 3. Evidence and strict limits

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-446-full-target-pencil.py` | 52 | `5dacc3b89bcd04fae4f5aba957ea874cc5bb0089a8244402261e4318642bcf02` |
| `frontier-20261028-level6-446-full-target-pencil-v1.json` | 1590481 | `f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3` |
| `frontier-20261028-level6-446-full-target-independent-replay.py` | 52 | `72085b8c4246a63e021b152f1d6604c7ed9505d8b5bf291b19b6fdf002adc724` |
| `frontier-20261028-level6-446-full-target-independent-replay-v1.json` | 16 | `f5fd59388b4c8b92f1fb9d948cd11e1cdb469dab1cea1f67b985adbd3084b828` |
| `frontier-20261028-level6-446-full-target-H0-check.py` | 64 | `4e31effc57c927e577891f408dac446a5ba378605e774014fa7d66ab486ee534` |
| `frontier-20261028-level6-446-full-target-H0-check-v1.json` | 147 | `c96a4f2479e9ddaabaecf11bd7135d0f73f4f9ebe19f84330e62ae06da3f72df` |
| `frontier-20261028-level6-446-full-target-obstruction-replay.py` | 51 | `babc41a88330d1228cfe5bbb347e637cfdd71b0a087595d818803842bb48f1c8` |
| `frontier-20261028-level6-446-full-target-obstruction-replay-v1.json` | 15 | `6a1d1e39c7be04f116994fb4c70ee826ed47cf479151c6ad4ba089c0a51c2702` |

The entire-target tree-versus-suffix replay returned PASS at **19:17:37 PDT**, the H0 failure was observed at **19:16:11 PDT**, and the negative-minor replay returned PASS at **19:17:04 PDT 2026-10-28**. Its order is not a claim that the H0 result had already been independently source-reviewed when first computed.

The separate `(4,4,6)` cofactor cone and its staged source/entry/CRT determinant receipt remain unchanged and require parent gate/review. This indefinite Euclidean form is not a full D3-kernel witness, not an integer-parameter counterexample, and not a no-go theorem for full target metrics. The earlier incidental older cone-status methodological exposure and all historical ZERO/STOP/HOLD/process findings persist.

**END — exact full-target obstruction to one specific L^T accretivity route only.**
