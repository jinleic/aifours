# Olson lane: incremental theorem applicability and credit note v3

Recorded at 2026-10-19T07:30:14-0700. Supplements v2 and the separate new-cell scout. Correctness remains governed by the exact parent verdicts, not this literature screen.

**No major or matched-SOTA improvement certified.** CT/CTgen are classical scaffolding; LS-lin is a restricted proof-method transfer with a lane-specific multiplier-pinning step. BASE1's classification may already be corollary-level. The newly reviewed LS+ chain would give a sharp partial band, not full LS+/STAB or ordered Olson.

## Evidence

- [Incremental scout](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-delta-applicability-scout-v4.json) `f790678a82dfbbc3e8548d1127c03fa8b2b1c3e6a2304227f6267a7f60d5d2b3`: 18 findings, five newly read primary sources and targeted re-reading of earlier pinned sources. Derived implications are **[INFERENCE]**; access holes are retained.
- Parent read the author-hosted [DeVos–Goddyn–Mohar preprint](https://www.sfu.ca/~mohar/Reprints/2009/BM09_AM220_DeVos_KneserAdditionTh.pdf), front matter and printed introduction pages1–3 (PDF pages2–4), including Corollary1.5 and the immediately following complement-sum remark. The PDF identifies itself as March2007 preprint; the journal version was not read. Extraction drops several ell/sum glyphs, so exact formula reconstruction remains labelled below.
- At G=C_p, a nonempty proper fixed-length subsum set has trivial stabilizer. The Corollary1.5 bound and complement identity give CT's truncated-multiplicity inequality directly **[INFERENCE from the read statement, consistent with the accepted CT proof]**. CTgen then adds pigeonhole and even involution deletion, as already checked in its correctness verdict. Neither is treated as a new theorem for priority purposes.

| Lane result | Source-level comparison | Calibrated status |
|---|---|---|
| CT / CTgen | DGM Cor1.5 + complement identity; elementary deletion/pigeonhole | Classical scaffolding, not a novelty claim |
| LS+ at e=2 | DGM + Savchev–Chen2007 index-one/greedy structure + CF arithmetic | Routine assembly; alternative elimination of SLZ3 remains [INFERENCE] |
| LS-lin p>=6e-10 | Savchev–Chen2008 proof-method transfer through zero-free core and first-crossing steps | Not a direct theorem corollary; the multiplier pinning and no-wrap bounds are the lane-specific restrictions |
| BASE1 p congruent to1 mod3 | Zeng–Yuan2011 factorization route identified by scout | Corollary-level identification remains [INFERENCE], because full text is inaccessible; BASE1+ still needs non-extension/SLZ3 |
| LS+ chain p>=10e-13 | Sharp 3kappa+1 band if all new text/errata accepted; classical tools apply in a wider region | Modest partial bound; no matched published comparator or major delta established; no new LS cells |

## Research lever, not a new accepted premise

The current bottleneck is multiplier/translation pinning. Savchev–Chen normal forms permit affine normalization; (ZP_kappa) does not permit arbitrary translation without changing its forbidden sums. Do not silently use that extra symmetry.

A distinct small-cell route is p congruent to2 mod3, kappa=(2p+2)/3, including (17,12) and (23,16). The scout suggests decomposing a shortest long zero-sum of length2p+2 into two or three atoms and using Zeng–Yuan's multi-atom results **[INFERENCE]**. Their full hypotheses must be read or reproved before import. This is not an extension of the accepted p congruent to1 BASE1 theorem.

## Limits

- The external index-one theorem remains an imported theorem; this screen does not replay its proof or replace the correctness boundary.
- Zeng–Yuan2011 full text and Savchev–Chen JNT2017 full text remain inaccessible; summary/slides cannot certify a hidden hypothesis. No access controls were bypassed.
- The general SC2008 statement at n=2p has a length mismatch and is vacuous here; only the audited proof-method comparison is used. At n=p after an EGZ split it supplies a normal form, not the missing pinning conclusion.
- A search miss is not novelty. Do not describe an extra-hypothesis bound as beating an unmatched weaker-hypothesis baseline.
- Full LS, LS+, STAB, INV* and ordered Olson remain **OPEN**. Accepted sequence cells are exactly those in [the delta verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-STAB-delta-parent-verdict-v1.md); later LS+ chain acceptance needs its own final erratum/verdict.
