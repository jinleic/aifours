# An all-gamma obstruction to one projected far-axis left test

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 19:29:03 PDT 2026**. Exact same-owner algebraic computation, UNREVIEWED; not an original-map kernel, a global no-go theorem, a parent/formal/human/independent-model verdict or a novelty claim.

## 1. The proposed left-test family and the negative result

Use the previously independently replayed full actual 235-target-row/34-source level-six `(2,2,6)` pencil `D=A+xB+yC`, at the exact full-Cartan/free-Levi/PBW inputs in `frontier-20261028-level6-226-full-target-ratio-cone-candidate-v1.md` SHA `6e8049679de3cd2d78f390edf0393d0abf31e6a0e65d531356f0d3a47bafb7d3`. Here `C` is the ORIGINAL s-slope, not a Cartan matrix or arbitrary choice.

Let `Pi_C` be orthogonal projection in the unweighted real tensor-word coordinate space onto the entire image of C, and let

\[
U=(I-\Pi_C)A,\qquad X_\gamma=C+\gamma U.
\]

This is an auxiliary Euclidean left test. It has the appealing property `C^T U=0`, hence `X_gamma^T C+C^T X_gamma=2C^TC` is positive semidefinite for every real gamma. One might hope to choose gamma so that the baseline `X_gamma^T A+A^T X_gamma` is positive definite, then use it for a far-s-axis cone. **That whole scalar-gamma strategy fails** for this exact source pencil.

The exact full-target ranks are

\[
\operatorname{rank}C=33,\quad \operatorname{rank}[C\ A]=43,\quad \operatorname{rank}U=10.
\]

The pinned data give an explicit nonzero rational source vector v such that `Uv=0` (equivalently `Av in im C`) and

\[
v^T(C^TA+A^TC)v=
-8221052732291973821490633426807013629288835015629916322996652704480377632253162206060143175030325888/
578957176550099804963191170448063919481649772139975222662664107361636329377555148689354940094227<0.
\]

Consequently for EVERY real gamma,

\[
v^T(X_\gamma^TA+A^TX_\gamma)v
=v^T(C^TA+A^TC)v<0.
\]

No member of this entire scalar family has a positive-semidefinite baseline form. This is an exact ALL-gamma result, not a finite list of failed gamma samples.

## 2. How the actual witness is checked

The producer chooses 33 independent actual C columns `C_J`, constructs the exact rational projection `Pi_C=C_J(C_J^TC_J)^(-1)C_J^T`, then forms U and a rational basis of `ker U`. A negative Schur-complement direction of the compression of `C^TA+A^TC` gives the full 34-coordinate rational vector v. The producer checks every entry of `Uv=0` and the exact negative value.

The independent replay uses a separately implemented rational span routine to check `rank C=33` and `rank[C A]=43`; it verifies the listed 33 C columns are independent. It computes Av and Cv directly from ALL 235 target rows, independently solves the 33×33 rational Gram system, confirms `Av` is exactly in `im C`, and recomputes `2(Cv)^T Av` as the same strictly negative rational. It does not trust the first script's nullspace output without checking the explicit vector. All code uses exact Q/SymPy rational arithmetic; shared local source helpers mean this is not formal or independent-vendor verification.

## 3. Evidence and strict nonclaims

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-226-projected-axis-obstruction.py` | 44 | `b9865fd83ff771c6bb7cc4c7aa67838ebf800159ceddf7620a41b9f0853750ae` |
| `frontier-20261028-level6-226-projected-axis-obstruction-v1.json` | 88 | `18529b04f981ab96393fca4c048c187ee0528e5c2777f2b0b16d440a8ca70e87` |
| `frontier-20261028-level6-226-projected-axis-obstruction-replay.py` | 42 | `b36ecd2dfa1d8638bcc23579a820bfabb561ffe8b3162a55c13d7f011e437094` |
| `frontier-20261028-level6-226-projected-axis-obstruction-replay-v1.json` | 14 | `f26630bc8888c2833ae144088149df7c7bd2fa6fe6f0e8559a041d1b18b866f8` |

The actual producer returned PASS at **19:28:28 PDT** and the independently authored rational replay returned PASS at **19:29:03 PDT 2026-10-28**. The source ratio certificate and its full tree-Jacobi/235-row replay remain load-bearing.

This negative quadratic vector is NOT a zero of `D=A+xB+yC`, a non-Serre vector, a counterexample at any integer r,s, an obstruction to arbitrary left operators or target weights, or a denial of the proved-at-named-inputs gap/ratio cone candidates. It excludes only `C+gamma(I-Pi_C)A` as a strict-baseline-positive certificate for ANY real gamma. Prior incidental older cone-status exposure and all ZERO/STOP/HOLD/process qualifications remain unchanged.

**END — exact no-gamma result for one projected far-axis test, not a kernel claim.**
