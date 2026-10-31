# An all-odd reflection-projection band for the R=p+1 word

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:40:35 PDT 2026**. NEW conditional-on-named-input **WRITTEN candidate**, not independently reviewed or a complete ordered Olson proof. Mandatory source order starts with `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`; the historical actual block counters are never replaced by projection counters.

## 1. All-prime band statement

Let p be an odd prime. Let W have F=3p−2 actual reflections and at least p+1 actual rotations, with at most one rotation in each cyclic gap between consecutive reflections. No nonzero or rotation-value assumption is imposed. If the cyclic reflection-only projection of W has exactly p maximal constant runs and ALL of these runs have odd length, then W has an original-order identity selector of exactly2p actual occurrences.

This addresses the named R=p+1 count band (indeed at least p+1), only for the explicit PROJECTION condition. It does NOT assume or conclude any value of historical actual `o_F` or `e_F`, nor any OLD/SEL/IPGEN/GS/DS3 failure. No f111 proof, review or floor claim is imported.

## 2. Proof with exact named inputs

There are `(F−p)/2=p−1` disjoint equal-reflection pairs in the cyclic projection, with one spare reflection in each odd projected run.

If two different odd projected runs have the same exponent, select one spare from each and all p−1 pairs. Every pair is an identity subproduct, and after their deletion the two remaining reflections have the same exponent and multiply to 1. This selects `2+2(p−1)=2p` reflections in their original order. No rotations are needed.

Otherwise all p odd-run exponents are distinct, hence they comprise F_p. Assign each occupied actual rotation gap to the projected run containing the reflection immediately BEFORE the gap, including a run's boundary gap after its last reflection. The runs partition all reflection gaps. Since singleton gaps make the at least p+1 rotations occupy at least p+1 different gaps, one of the p odd projected runs is assigned at least two occupied gaps. Take the FIRST TWO in that run's linear cyclic order. The first cannot follow the run's final reflection, and therefore its next reflection has the same exponent c. There is no intervening occupied gap between these first two gaps, so the ACTUAL word contains a consecutive segment

`σ_c ρ_u σ_c (σ_c)^h ρ_v`

within that odd projected run. Apply the joint written selector candidate from the MANDATORY ADDITIVE exception resolution `frontier-20261028-olson-stretched-fourblock-exception-resolution-v1.md`, SHA256 `4c13a273997c6a02c97ab9b4b45bd36a80c5ebe0751c59450770ba33b76a58ac`, together with its full named input `frontier-20261028-olson-stretched-fourblock-selector-v1.md`, SHA256 `ef44c034b01a924d0930f26e6c95b70972af31f9666340a06457ff40bc261e7f`. Their paired parity proof pays every h,u,v and gives an original-order 2p selector. Those inputs are unreviewed candidates, not a verdict; an independent review must read 4c13 before the COMPLETE ef44 and must reconstruct both. QED conditional on that named joint input.

As a separate elementary observation, if the projection has at most p−2 odd runs, regardless of even projected runs, `(F−o_π)/2>=p` equal pairs alone give a reflection-only 2p selector. Thus the following current open projection strata remain: `o_π=p` with at least one EVEN projected run, and `o_π>=p+2`. This is not a classification by actual full-word block counts.

## 3. Bounded actual-word evidence and limits

New `frontier-20261028-olson-repeated-odd-projection-experiment.py`, SHA256 `27444cf51d59efd5931c4d99ac0904eb7df8e169346f08cc666146bcbe5a4cce`, produced 400 words p=5,7,11,13 with repeated odd projected-run labels, singleton gaps and reflection-only selectors; data SHA256 `acd2fb36c55a6e1502b1d4695b51bd52ce29627e04ca964de8fb29106ff67ebe`. Independent `frontier-20261028-olson-repeated-odd-projection-checker.py`, SHA256 `baf6d8aad1c88197c20ded264b54c42c1ccf7ca08f4edcdea90a01efa6dd8817`, returned PASS in result SHA256 `50b4689e2036180dcde30bb3ee512eb639135e2f1a8b33c6a7b0dd8f3c5d7f62`.

A separately written pooled checker `frontier-20261028-olson-all-odd-projection-band-checker.py`, SHA256 `0b9dedfabdb62278549447136e9700fce24ebcb37a33c16f37ec708a70ad5083`, read the 1000 previous nonexceptional stretched fixtures (data SHA256 `1914ad08678cef0a806bf3a43c96ff0ea6bd0ef5a8271ee7d277de857c5f6dd4`), the 500 former exception fixtures (SHA256 `3cc2dda49d2dc6957471f0175125469866ff7dc0c04dc468fe8d580a8a6ec67b`, excluding their 250 with an even projected run), and the 400 new repeated-label fixtures. Result `frontier-20261028-olson-all-odd-projection-band-check-results.json`, SHA256 `c642b26bd9415fddd0385548215faa354785e755780899c4e55b590ca9566ae2`, records `PASS_INDEPENDENT_ALL_ODD_PROJECTION_BAND` for 1650 original-word witnesses: 1250 distinct and 400 repeated odd-label cases. It independently checked counts, actual singleton gaps, odd-projection profile, the occupied-gap pigeonhole, original-index products, and two mutation controls. This is finite same-model evidence, not review, formal verification, novelty clearance or a proof of the full lower branch.

**END — all-odd PROJECTION band candidate; other projection strata remain open.**
