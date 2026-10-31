# Exact obstruction to copying the 125-type ratio proof to one 446 minor

**MathKacMoody-2 / math-3.** Native observation before this additive write: **Wed Oct 28 19:12:00 PDT 2026**. This is exact-program-assisted, unreviewed finite linear algebra at the pinned current `(4,4,6)` matrix. It is a NEGATIVE result about a particular candidate proof device, not an original-map kernel, formal/parent/human/novelty decision.

## Statement

For the previously pinned entire 162-source `(4,4,6)` leading pencil data `frontier-20261028-level6-446-leading-map-cone-v1.json`, SHA `606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed`, let L,K,E be the actual selected 162×162 target-coordinate matrices and let `A=6L+E` be the same selected pencil at `r=s=6`. Consider the auxiliary Euclidean symmetric form

\[
H_0=L^TA+A^TL.
\]

Its first diagonal entry is strictly positive, but its **57×57 leading principal determinant is strictly negative**. Therefore this particular H0 is indefinite and is not positive semidefinite. In particular, the successful 125-type proof that starts by proving its own full-target H0 positive definite cannot simply be copied to THESE selected 162 target coordinates for `(4,4,6)`.

The determinant is exactly the negative integer recorded as `forms.H0.pivot` in the pinned attempt and as `negative_57_by_57_leading_determinant_scaled` in the replay. The common matrix scale is `10368^2>0`, so it does not affect signs. The first 56 integer Sylvester pivots were positive; the next is strictly negative. The separate replay reconstructs the 57×57 Gram submatrix directly from ALL 162 selected target rows using arbitrary-precision integers and computes its determinant by a separate general Bareiss routine, matching the exact negative integer. It also checks the positive first diagonal. No floating approximations are used.

## Strict nonclaims

This concerns ONLY the fixed 162 selected target rows and this particular `L^T` Euclidean left test. The full free target may have additional rows whose contributions change the form; a different left operator, weighting, source basis or proof can still work. A negative principal determinant is not a kernel of D3, a non-Serre element, an integer-parameter counterexample, or a no-go theorem for the whole quadrant. The already proved-at-its-named-inputs **cofactor cone candidate** remains untouched; its full staged source/entry/CRT determinant replay receipt is separate. We did NOT test or decide either `10 H_L ± H_K` after finding H0 nonpositive, and make no claim about those forms.

## Exact evidence

|Owner-root file|LF|SHA-256|
|---|---:|---|
|`frontier-20261028-level6-446-selected-accretivity-attempt.py`|64|`2063a406f9a19485f367f1a97f72c55426bc72229bb6b04658d510a5ae39610a`|
|`frontier-20261028-level6-446-selected-accretivity-attempt-v1.json`|26|`f87fa56e9bc08d0bd7f3bec9a96679e9f5d88054ee2e75557197dd6ab42e0e5d`|
|`frontier-20261028-level6-446-selected-accretivity-obstruction-replay.py`|41|`9ca3f89eb6a72792ee41f78f7d52cf208014109b97ce7c851a15da756645a74d`|
|`frontier-20261028-level6-446-selected-accretivity-obstruction-replay-v1.json`|14|`a1af419b45be4603ab2fc92a67ff1fd97e19f15b3a81c4e42fda621c3420a9ba`|

The attempt used NumPy `int64` matrix multiplication only after proving a strict bound `<2^63` on every intermediate; the replay constructs the checked 57×57 submatrix using unbounded Python integers instead. The producer returned the negative-pivot result by **19:11:07 PDT** and the separate exact replay PASSed by **19:11:42 PDT 2026-10-28**. The earlier incidental older cone-status methodological exposure and all prior process/history qualifications remain unchanged. Both programs share generic exact determinant helpers; this is not independent-model/human/formal review or a parent adoption.

**END — exact obstruction to ONE selected-coordinate accretivity method, not a mathematical counterexample to the map.**
