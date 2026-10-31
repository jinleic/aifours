# Additive erratum: ln 64 exact gap denominator

**NUMERIC CORRECTION; original author candidate remains frozen and UNREVIEWED.** Native clock observed before this write: `Wed Oct 28 21:09:15 PDT 2026`.

## Affected pin and mandatory read order

This is an additive correction to `frontier-20261028-ln64-rational-nonradial-obstruction-v1.md`, SHA-256 `028397b5e5c5cae583f9fc69ed1efadbaeda169c729d3cb878b74b1e2cc14e01`. Its original Eq. (10) printed a denominator **10^6 too small**. Therefore the printed equality is WRONG; the frozen source bytes are unchanged. It was an author transcription error, not a reviewed proof or a retroactive change to an earlier packet.

Main's complete mandatory before-source correction is `institute/runs/three-area-2026-10-27-96h/review-waves/f145-privacy-ln64-nonradial-staircase-obstruction/parent-required-numeric-correction-v1.json`, SHA-256 `3b29787c…` as reported by Main. Its recorded read order and independently-recompute requirement apply to that review. This addendum does not replace that parent control, claim correction-compliant prior exposure, or release any historical v227/v259 duty.

## Exact replacement for Eq. (10)

The same numerator must be divided by the CORRECT denominator below:

    M4(a)/[3M2(z)]-J(P_S)
      =55892104628095766169604064637687395172793197064705238995982813
       /28589579218686463271455054512504719394059809867200000000000000000000
      >1/1000000.                                                         (10 corrected)

Main reports an exact Fraction recomputation of the cost and this corrected gap. This is also the fraction printed by the owner's earlier Fraction cell; the source-file copy lost six zero digits. The owner's earlier decimal rendering was approximately `1.954981715560335e-6`. The assertion `>10^-6` remains the parent-reported exact arithmetic result; this addendum is not a separate proof of full-D feasibility, all-staircase optimization, the optional radial bridge, or the cited source theorem.

No check was rerun merely to reconfirm Main's reported failure; the original Eq. (10) and the parent correction were read, and the previously observed owner output was used for this erratum. The later uniform-window and threshold candidates were derived separately and do not use the incorrect printed Eq. (10) as a premise; no exhaustive consumer census is claimed. No independent review, formal proof, novelty/priority conclusion, or parent acceptance of the candidate is asserted.
