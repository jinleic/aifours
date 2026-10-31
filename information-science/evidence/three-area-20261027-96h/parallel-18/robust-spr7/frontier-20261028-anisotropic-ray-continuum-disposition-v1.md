# Exact continuum disposition for a nested anisotropic septic-box ray

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 19:02:26 PDT 2026**. **WRITTEN-checked-in-kernel candidate; not independently reviewed or adopted.** This disposes a continuum of one explicitly named box ray, not the general septic synthesis question.

## Exact result

Use the base rational endpoints `l,u` listed in the full `frontier-20261028-bounded-exact-search-and-symmetric-ray-barrier-v1.md`, SHA256 `65c7cf0ac40b45a243e0cbcd037a71305acba3f1b4c10582aefd3f6811301864`. For a real r>=0, define one monic independent box A(r) around the same midpoint: for coefficient indices j=0,...,5 its half-width is `r*(u_j-l_j)/2`, while for j=6 its half-width is fixed at `(u_6-l_6)/4`. These are actual independent closed intervals; the s^6 width is always positive and the others may collapse at r=0.

Import the COMPLETE exact constructive result `frontier-20261028-boundary-box-new-numerator-open-family-v1.md`, SHA256 `816e6aab6c5b68e111e7c001251e2358ff891f71e94b6e98f6116e4ce5d16dd0`. It proves that A(679/640) is all-member Hurwitz and gives one explicit rational b_B which is SPR against EVERY member and EVERY finite real frequency, with an exact positive margin. It remains a same-harness candidate, not automatically adopted.

Then:

- For EVERY real `0<=r<=679/640`, A(r) is eligible and the SAME b_B is a common exact-degree-seven numerator, because `A(r) subset A(679/640)`.
- For EVERY real `r>=17/16`, A(r) is ineligible: it contains the non-Hurwitz actual corner displayed below.
- The exact residual on THIS ray is `679/640 < r < 17/16`, of width `1/640`; no claim is made there or for other box directions.

The first bullet also covers every closed independent subbox of A(679/640), including boxes with arbitrary different midpoints and degenerate coefficients. It is not an original all-box solution.

## Exact instability witness

At `r=17/16`, the actual `(E_+,O_-)` corner has ascending coefficients

`(146903/32000, 68631/6400, 378373/16000, 692013/16000,`
` 359529/32000, 104257/8000, 2207/2000, 1)`.

Its fifth leading Hurwitz determinant, for the usual monic seventh-degree Hurwitz matrix, is exactly

`D_5 = -509025067848337572697/524288000000000000000 <0`.

Strict Hurwitz stability requires D_5>0, so this actual polynomial is non-Hurwitz. All A(r) for r>=17/16 contain A(17/16) because every changing half-width increases while the sixth-index half-width stays fixed. Hence they contain this very same non-Hurwitz polynomial and cannot satisfy the original all-member Hurwitz prerequisite.

The owner computed the determinant in the Python Eval kernel by integer Bareiss elimination after multiplying the coefficient vector by 32000: the scaled fifth minor was `-32577604342293604652608`. A separately structured rational Gaussian determinant calculation gave the displayed D_5 and exactly matched the scaled value divided by `32000^5`. The exact bounded stability-bracketing source is `frontier-20261028-anisotropic-boundary-bracket-kernel-v1.py`, SHA256 `61b7fee215ed49bd3dc8177ddce3841f833a2ffcf88db7919449a9c2cc552024`.

## Scope

The positive conclusion is conditional on the entire named full-frequency base proof and its independent same-harness root/leaf replay; the determinant is an exact kernel calculation, not an independent human or formal verification. The unnamed residual interval is not a certificate failure, a counterexample, or a claim that b_B necessarily fails there. No original universal result, actual no-numerator box, novelty, numerical optimum or altered historical process status is claimed.

**END.**
