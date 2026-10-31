# Additive resolution of the stretched-block construction exception

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:38:12 PDT 2026**. This is a new WRITTEN candidate, not a reviewer verdict. Mandatory fatal before-source `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. No withdrawn f111 adoption or historical actual-block/floor implication is reused.

## 1. Stronger independent opposite-rotation lemma

Let W be a dihedral word with F=3p−2 reflections and exactly p odd maximal constant runs in its cyclic **reflection-only projection**, where p is an odd prime. No distinctness or AP condition is imposed on their labels; additional even projected runs are allowed. Suppose one entire odd projected run consists of the actual consecutive segment

`σ_c ρ_u (σ_c)^(2m) ρ_(−u)`,  m>=1.  (1)

Then W has an original-order identity subsequence of exactly2p occurrences.

**Proof.** Omit the initial σ_c. Select the two opposite rotations, select all 2m c-reflections between them, and select `floor(length/2)` pairs of equal reflections in every OTHER projected run. The equal-pair capacity across all projected runs is `(3p−2−p)/2=p−1`; (1) contributes exactly m of those pairs. Thus precisely `2+2(p−1)=2p` occurrences are selected. Cut immediately before ρ_u: the c-pairs lie between the rotations and multiply to 1, and all later equal pairs multiply to 1 after unselected rotations are skipped. The product is `ρ_u ρ_(−u)=1`. A cyclic reordering to the original increasing word order preserves identity. QED.

The selected positions are actual full-word occurrences, and “entire” refers to one projected run, not the historical actual rotation-separated `o_F/e_F` blocks. No assumption about other rotation values is needed.

## 2. Prospective removal of the prior construction exception

`frontier-20261028-olson-stretched-fourblock-selector-v1.md`, SHA256 `ef44c034b01a924d0930f26e6c95b70972af31f9666340a06457ff40bc261e7f`, proved its stated projection-only selector outside the explicitly named q=r=0, u+v=0, u!=0, AP-aligned configuration. In that configuration, h is odd and the entire odd projected run is exactly (1), with `m=(h+1)/2`; the lemma above pays it without using the AP alignment or any third rotation.

Consequently the following is a **new joint written candidate**: under the original ef44 hypotheses—F=3p−2, exactly p distinct-label odd projected runs, and ACTUAL segment `σ_c ρ_u σ_c (σ_c)^h ρ_v` within one such run—the identity-2p selector exists for EVERY h,u,v. The named ef44 proof is an essential input for all nonexceptional cases and must be read and independently reconstructed in FULL after this addendum; no earlier review is transferred. The source ef44 remains unchanged, and its original narrower statement was accurate when written.

The narrower independent third-boundary candidate `frontier-20261028-olson-exception-third-rotation-selector-v1.md`, SHA256 `140f678172dd80e09495fbfc23bdc0d0023104020ee1474232d336cdb0ec7d1c`, is now logically unnecessary for covering this exception; it is not a prerequisite for §1 or the joint candidate. No old review or claimed defect is inferred from that redundancy.

This still does not prove that an arbitrary L_RES word has p distinct-label odd projected runs or the actual segment, or establish any full OLD/SEL/IPGEN/GS/DS3 failure, full ordered Olson, an L_RES counterexample, novelty, formal verification, or review acceptance.

## 3. Exact bounded checks for the formerly excluded case

`frontier-20261028-olson-opposite-rotation-exception-experiment.py`, SHA256 `557f1b0a3e56c6cada85d400f11a2d6c28be3908042681f0b5f0a1c2f3829291`, generated 500 original zero-free singleton-gap words at p=3,5,7,11,13, including 250 with one EVEN projected run. These examples specifically satisfy the former AP-aligned exception and set EVERY other rotation equal to −u, so no non−u third-rotation condition is used. Data SHA256 `3cc2dda49d2dc6957471f0175125469866ff7dc0c04dc468fe8d580a8a6ec67b` is in `frontier-20261028-olson-opposite-rotation-exception-results.json`.

Separately written `frontier-20261028-olson-opposite-rotation-exception-checker.py`, SHA256 `a3c15c4f079f4b7b0b2ac73c4033a010f5754af07542a21058f14e2c111fcc22`, imported no producer; `frontier-20261028-olson-opposite-rotation-exception-check-results.json`, SHA256 `8635404fb9dcd44896c70c30905f004f75bf559bf1d49fe58e187e4a6558be6c`, records `PASS_INDEPENDENT_OPPOSITE_ROTATION_SELECTOR`. The checker reconstructed actual rotation positions, central run, projected parity profile, p−1 equal pairs and each original product; selected-first-reflection and changed-second-rotation mutations were rejected. These examples are AP-aligned; the lemma itself does not need that condition. The 1000 earlier nonexceptional examples are separately pinned in ef44. Bounded same-model checks are not a disjoint review, formal verification, or a proof of the universal problem.

**END — additive exception resolution; joint scope still conditional on explicit projection and actual-segment hypotheses.**
