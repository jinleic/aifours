# Additive MINOR qualification: feedback-fiber extension is not joint control affinity

Actual native prewrite observation: **Tue Oct 27 16:31:25 PDT 2026**. Owner InfoHinfPreview-2. This is a new immutable additive clarification, not an edit to the reviewed source `fixed-feedback-preview-literal-convexity-v1.md`, SHA `1127ad2e08baeb152fc9e3f258fb69d71ef41c0d1ec2be4f63e0bc648b3e046d`.

## Trigger and exact affected claim

Main reports the w55 return as **PARTIAL: 0 FATAL / 0 MAJOR / 1 MINOR**, with the S7 feedback-fiber extension requiring that it not imply joint control affinity, and with NR-GAIN separately unpaid/pending w65. I have not opened the w55 review body or inferred a full-scope acceptance from that report. The reported finding is retained, not re-run or dismissed.

The source theorem item 3 begins “The conclusion extends to joint pairs (K,R) restricted to any affine feedback slice on which BK, B0K and D1K are all fixed.” Read that extension prospectively as referring to **state/output affinity, literal gain convexity and the stated feasible-set conclusions ONLY**. It must NOT extend item 1's actual-control affinity to simultaneous changes in K and R.

## Correct exact identities

For K FIXED and arbitrary R1,R2, the source's actual state, control AND original output affine identities remain as stated.

For simultaneous pairs (K1,R1),(K2,R2) on a fixed (BK,B0K,D1K) fiber, set `Klambda=lambda K1+(1-lambda)K2`, `Rlambda=lambda R1+(1-lambda)R2`. For the same actual progressive input and Brownian motion the state/output identities are

`Xlambda=lambda X1+(1-lambda)X2`,

`zlambda=lambda z1+(1-lambda)z2`.

But the actual ORIGINAL control is

`ulambda=Klambda Xlambda+Rlambda w`,

and satisfies the precise difference formula

`lambda u1+(1-lambda)u2-ulambda`

`=lambda(1-lambda)(K1-K2)(X1-X2)`.

This vector need not be zero, even on the fiber. Its B, B0 and D1 images ARE zero under the fiber assumptions, which is exactly why the ORIGINAL physical state/output affinity and literal convexity survive. No claim of joint control affinity is made. With identical R, the states coincide and the special same-R control identity may hold; that special case does not imply the general joint statement.

Admissibility of ulambda follows from its own finite-horizon linear-SDE/E2 caller as one bound original-information law, not from representing its control as the convex combination of the other controls.

## Status and limits

This supplies an explicit author remedy to the one reported MINOR; only Main's complete-read disposition can adopt/pay it. The original reviewed return and source bytes remain unchanged. NR-GAIN for global literal finiteness/continuity is NOT paid here and remains tied to the separate source under w65. No finite/continuous conclusion is upgraded merely by this correction.

The self-contained fixed-K convexity and the properly scoped fiber state/output/gain conclusions require no general-controller averaging or stopped realization route. This addendum does not claim arbitrary-feedback convexity, general N&S synthesis, independent reconstruction, source-book equivalence, formal/kernel/executable/human/configured-family/novelty acceptance or cure of any old process finding. The direct diffusion-annihilating controller branch remains NOT ADMITTED; all STOP/HOLD/ZERO/N4 UNKNOWN/aux214 STOP limits persist.
