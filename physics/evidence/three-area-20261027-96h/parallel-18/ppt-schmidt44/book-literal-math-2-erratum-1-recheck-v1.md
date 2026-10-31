# B2 — documentary erratum 1 recheck

Comparer **PhysicsPPT44-2**. Actual native clock before creation: **Wed Oct 28 09:50:54 PDT 2026**.

**Verdict: RESIDUAL.** All four items in my prior comparison are **CONFIRMED corrected** by erratum 1; none of those four identified deviations remains. The separate residual is a **newly noticed MINOR typography omission in reference R10** that my prior comparison did not report, detailed below. This distinction avoids silently treating an incomplete prior finding list as an exact full-page check.

## Bound inputs and scope

- Frozen recheck release `comparison-B2-math-2-erratum-1-recheck-release-v1.json`, SHA256 `431d900efb672416028146acb2d169e005a7b16ea7b74f2731dd8719141e1901`.
- Complete erratum `book-literal-math-2-v1-erratum-1.md`, SHA256 `efb88789ea4f09b31eb6538789f9331a5dea24ceaf1b9db6ab9f0d7243cd3c7f`, 173 LF / 10591 bytes; read completely in raw windows LF1–60, 61–120 and 121–173, including the ending.
- Prior comparison `book-literal-math-2-comparison-v1.md`, SHA256 `e6ed59c328d807f3798a51ca3017240de7c03ecac080290e6a619d20ea0d3ea7`, 48 LF / 7007 bytes, from this same duty chain.
- PDF 158 / printed 142 image `source-math-0158.png`, SHA256 `420f0805b5371d46a491a731429cde40f254e4a938287159790ab72f6584902f`.
- PDF 157 / printed 141 image `source-math-0157.png`, SHA256 `3ef412f284c1478ddb282ec2f53d1f13a207c28e827fca46f6b3df3dc890333b`.

The release requires no new pre-body ACK for this same comparer/duty chain. Only the listed images were viewed. Comparison is documentary, not a mathematical or bibliographic-status judgment.

## Four erratum items against PDF 158 / p142

| Item | Result | Image / corrected occurrence |
| --- | --- | --- |
| M1, identity symbol | **CONFIRMED** | B04–B05 prints `G 的单位元 e`; the erratum restores `e` in the Chinese, aligned English and identity inventory. |
| M2, reference title | **CONFIRMED** | R9 prints `On Kemnitz’ conjecture concerning lattice-points in the plane`; the erratum removes the added `s` from the printed title token. |
| m1, punctuation | **CONFIRMED** | B05 prints a comma after `单位元 e` before `他还猜测`; the erratum joins the corrected Chinese clause and its aligned English with a comma. |
| m2, group-notation typeface | **CONFIRMED** | B01–B02 and B06–B11 use bold `Z` in the affected group expressions; the erratum supplies `\mathbf Z` in the identified Chinese, English and inventory occurrences. |

U1/U2 in the base and supplement remain declared uncertainties, not resolved here. No change to the page-join or the qualified TRUNCATED statements is introduced by this erratum.

## Newly noticed residual, not a prior finding

**MINOR — PDF 158 / p142, reference R10:** the printed final title symbol in `covers of Z` is **bold Z**, whereas the original base packet's reference line **LF84** and its `R10, additional printed title symbol` inventory entry use an unbolded plain `Z`. Erratum 1 corrects the body group-notation instances listed in prior item m2 but does not correct this separate reference-title/inventory typography. My prior comparison identified m2 only for body B01–B11 and did not report this R10 occurrence. I therefore classify it here as a newly noticed residual, not as an unresolved instance of the prior four findings. No change of reference words or mathematical meaning is alleged.

The original and supplement packets and the erratum remain immutable. No extra source/page, author contact, mathematical derivation, status/novelty assessment or resolution of an ambiguous glyph was used. All STOP/HOLD/ZERO, L1, scientific HOLDv2, N4 UNKNOWN/historical-exit and auxiliary214 STOP boundaries persist; this documentary recheck does not admit a scientific lane input.
