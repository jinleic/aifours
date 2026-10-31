# f59 — universal one-copy inequality and partial-core separation

Reviewer **InfoSPR7-2**, author **InfoGuessingRminus-2**. Actual `/bin/date` immediately before writing: **Wed Oct 28 17:51:43 PDT 2026**. The full ordered assignment is SHA256 `a317b737e90e5da56ceaa8810113cb8e641cfa64c386799f9a27a669ef9dacaa`. The complete candidate is SHA `1d5cb24c9dfb38248bdc8d32ead3818288f77b8cc8494501ee03963ce7d92d27`; full addendum 2 is `eab2a42b99840a6f6845da1256b207e6c60cae14ea2febd3fb961dc4dd453956`. The complete 1,416-LF certificate JSON and 274,210-LF frozen point JSON were read as complete byte strings and parsed, with hashes `ae9d207260ef0855f84c9ab3ab6f7d62128562db5ad051a0337bf9ccac6e6498` and `97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec`, respectively.

## Verdict

**FATAL 0 / MAJOR 0 / MINOR 1.** The 36-term inequality is reconstructed for **every finite joint law**; the exact certificate, negative point value, restricted all-order-F separation and no-one-copy-extension caller are independently checked at the stated scope. It is not a new guessing-number bound or an entropic counterexample.

**MINOR M1 — full-source redundancy is known, not merely a possibility.** Candidate line 18 says L *may* be redundant in the full source-copy LP; its proposed next question at line 53 is ambiguous about which “copy/FD relaxation” would be strengthened. Every one of the 33 CMIs is an elemental inequality on the source's **eleven-variable first copy branch**, and all 15 equalities are first-branch conditional-copy equalities. The displayed certificate therefore proves that L is **already implied by the full source-copy LP**, independently of objective, finite numerical output or the F-family. If that full LP includes its original-entropy graph-symmetry equalities as in the cited source, each graph-automorphism image of L has the same value as L and is implied as well. Adding L and those images to that same full LP cannot strengthen it or lower its optimum. Adding L to the weaker, explicitly partial-coordinate core remains a valid new cut and does separate this point; any other stronger relaxation or changed copy mechanism needs its own analysis. This is a sharpened future-work boundary, not a defect in the candidate's actual inequality or its partial-relaxation separation.

## 1. Exact universal certificate

The reviewer independently wrote `frontier-review-f59-one-copy-kernel-v1.py`, SHA `2b81150d9a0220e2796f6c5f63d55c1a3181581d442ddcd91bed3ae85e9632d8`. It executes finite `fractions.Fraction` and integer-mask arithmetic inside the Python Eval kernel, imports no author checker or optimizer, and binds the complete certificate and frozen point by SHA. It reconstructs the announced L vector separately, not from the certificate's claimed `original_entropy_coefficients` field.

The 48 selected entries have 48 distinct row indices and divide as follows:

- **33 CMIs**, each reconstructed from its actual `i,j,Z` metadata with distinct vertices, Z disjoint from the two singleton indices, and exact entropy vector `H(Zi)+H(Zj)-H(Zij)-H(Z)`; H(empty)=0. Every CMI multiplier is strictly positive. After division by 276, the only multipliers are 1 and 2.
- **14 copy-marginal equalities** `H(S,b)-H(S,b'0)=0`, up to orientation, with each actual context S a subset of `Y={a,d,e,f,g,h,i,j}`. Their multipliers may have either sign.
- **One copy-independence equality**, up to sign, `I(b'0;b,c|Y)=0`, equivalent to the candidate's `I(b'0;all originals|Y)=0`. Its multiplier is unrestricted.

The exact weighted vector has **zero at every mask containing auxiliary bit 10**. Its remaining **36** original-mask coefficients, after division by 276, equal the candidate's literal displayed L term by term, including the coefficients `3,5,-4`. The raw weighted vector also matches the separately serialized coefficient vector. Consequently L is a nonnegative linear combination of 33 CMIs and zero-valued copy equalities, and L>=0 follows for arbitrary finite variables. No R-minus graph, FD, cap, symmetry, feasible-point entropy law, solver status or numerical LP optimum is used for this universal inequality.

### Copy identities for arbitrary finite laws

For any original joint distribution, for each Y-value of positive probability choose the conditional distribution of b given Y and draw b'0 from that kernel independently of the original ten-variable tuple conditional on Y. Assign arbitrary kernels on Y-null values. The new joint law preserves the entire old marginal, `(Y,b'0)` has the same distribution as `(Y,b)`, and b'0 is conditionally independent of `(b,c)` (indeed the entire old tuple) given Y. Marginalizing `(Y,b)` and `(Y,b'0)` gives every `H(S,b)=H(S,b'0)` for S subset Y; conditional independence gives the one four-term equality. All variables and kernels are finite, so no conditional-density regularity beyond this construction is required. This pays every equality used by the 48-row certificate, including signs and zero-probability conditioning values.

The independent in-memory controls rejected: a negative CMI multiplier as `NEGATIVE_CMI_WEIGHT`; a sign-corrupted CMI term as `CMI_TERMS`; a modified copy marginal as `COPY_EQUALITY`; and a missing row as `ROW_COUNT`. They leave the source bytes unchanged. These controls exercise four targeted checks only and are not an exhaustive mutation proof.

## 2. Exact point separation and extension boundary

The reviewer directly evaluated the **literal** 36-term L against the parsed frozen original coordinates, obtaining exactly `L(h)=-1/276`; the raw certificate vector evaluates to `-1`. Its original full-set coordinate is exactly `1847/276`. The independent f39 review `frontier-review-f39-rminus-all-order-copy-obstruction-v1.md`, SHA `3d2b548b970c1df08f83a4e133adcb33713c61ea9b7ddb82aab2593e9d74a774`, separately checked the same SHA-pinned point's original Shannon/FD/cap/symmetry rows, certificate-core/partial-copy rows, and all **13,729,980** disjoint nonempty A–D substitutions modulo A/B swap for **all** n>=1 by exact integer quadratic minimization. The f39 empty-block proof pays the remaining disjoint cases. Thus the point is a legitimate witness that this *specific partial relaxation* plus all stated disjoint-block F_n cuts does not imply L>=0. It is not a probability distribution or original guessing strategy.

The point cannot have **any** first-branch copy extension satisfying all elemental Shannon and actual copy equalities while retaining its ten-variable base profile: the 48 valid rows would force L>=0, contradicting the fixed `-1/276`. This is stronger than merely ruling out the particular saved auxiliary assignment. It still says nothing about a different original-variable profile, a new full-LP primal, or the true guessing number.

I independently reconstructed the distinct addendum-2 obstruction to the **saved auxiliary assignment** in the second branch. With `S={a,b,c,d,e,g,h}` and `U=H(S,d'1,f)`, the fixed coordinates are

`H(S)=871/138`, `H(S,d'1)=0`, `H(S,f)=1847/276`,
`H(S,d'1,e'1)=0`, `H(S,d'1,e'1,f)=2057/276`;

U itself is not stored. The two elemental CMIs in the addendum force `U<=35/92` and `U>=2057/276`, an exact contradiction gap `488/69`. A separate reviewer enumeration of immediate nested known-coordinate pairs gave the addendum's `(checked,negative)` counts `(6554,0),(9758,5),(14782,18)` for the first, second and third source branches. These checks confirm the saved assignment's nonextendibility; the universal L argument above separately rules out even a differently chosen first-copy extension of the same base profile.

## 3. Evidence and limits

Exact replay receipt `frontier-review-f59-one-copy-replay-v1.json` has SHA `6906efd6291c58eb5fad35782951f9a09dfb9ccf6c76380c56643093b2110b78`. The f39 source graph and first-copy transcription come from the previously reviewed pinned article/Annex C sources; the universal inequality itself uses only the explicitly stated Y/copy construction and exact certificate, not that graph. Author-provided floating solver statuses and author-produced check results were not used as independent evidence and were not rerun.

The partial-coordinate point is neither entropic nor a source-LP feasible primal. The all-order comparison is only for **disjoint original-vertex blocks**; no conclusion is made about all known information inequalities or other copy constructions. The calculation does not improve the published upper bound, determine whether the source LP attains it, decide the exact guessing number, or establish novelty/priority. This is same-harness independent code and written reconstruction, not formal-kernel, independent human or configured-model review; no external-model/paid API, native scientific subprocess, publication, Git or deletion occurred.

**END OF REVIEW.**
