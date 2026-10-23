# Sun k7: classes K5.2* and KII excluded; four classes remain open

Recorded at 2026-10-18T14:48:49-07:00.

**CORRECTNESS-ACCEPTED: no configuration of the residual classes K5.2\* (with the D2′ case) or KII exists.** This holds under the parent-accepted written reduction and active rules ([written verdict](sun-coset7-written-parent-verdict-v1.md), SHA256 `73a25ba6b2848e5412de4c8fac667c7bbd899cf22b165f0fed5db29f3eea9f35`), with its mandatory overlay. **No Sun(7) theorem follows.** K7, K6.2\*, K6.3 and K5.3 remain OPEN. K5.3 additionally awaits the separate Stage A (X1) independent check.

## Evidence chain

1. **Producer certificates.** Stage B exploratory run [receipt](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/evidence/stageB-RECEIPT.md), SHA256 `e044a4eba6decd3c34222e577628993f762a51b67cc63e61853f97db7ca9e074`. Engine `e7b4f039…288d`, 10 output files. The producer counts are never premises.
2. **Independent checker.** The SunK7StageBVerify agent wrote a standard-library checker from the definitions only, without reading producer code ([receipt](sun-coset7-stageB-independent-v1/receipt-v1.json), SHA256 `9b16a50551ff816d92519d09a2cd1dfd83e682c9fb57888485416ad5b4112aef`). For checker v2 (`f4af3f7c…7b54`):
   - it enumerated the universes two ways;
   - it re-walked the full α tree from every orbit representative;
   - it verified every T, K-partial and VFC closure and every RPLP leaf for every q, in exact arithmetic;
   - it passed 11 preregistered corruption controls.

   K52 gave 3,600 labelled tuples in 171 orbits and 0 leaves. KII gave 924 labelled tuples in 132 orbits and 1,584 leaves in 528 orbits, each matched to one verified RPLP line. Both had 0 survivors.

   Checker v1 rejected a float in producer metadata (a checker fault); v2 changed only that. The checker's v1 result is retained.
3. **Cross-family static code audit.** [Codex](sun-coset7-stageB-checker-codex-v1.note.md), SHA256 `2605b1a6afa4be8de40ef491d4906439e03b39600c3aea67815b91d9e5044bd9`, found the implication "COMPLETE_VALID ⇒ class excluded under the accepted rules" **SOUND**, with 0 FATAL/MAJOR:
   - universe SOUND, with K52 deliberately overcovering K5.2\* (it includes the D2′ case);
   - symmetry SOUND;
   - walk and closures SOUND;
   - leaves and RPLP SOUND;
   - parsing SOUND-WITH-FIXES.

   It confirmed the KII universe matches the README class. Its residual uncertainty was genuine execution and anchoring, which items 4 and 5 resolve.
4. **Parent anchoring check.** For all 10 producer outputs, the lane original, the checker's pinned copy, the manifest entry and the receipt hash are identical. Both the checker and manifest (`8f7a198d…1524`) hashes match the receipt.
5. **Parent re-execution.** The parent ran the frozen checker v2 itself, one process at a time, admitted at 14,511,247,360 free bytes ([replay receipt](sun-coset7-stageB-parent-replay-v1/replay-receipt.json), SHA256 `533113137250e4f7bd0e7de2b6342fd4ae328e8d7a7aa5a4e963f93025efa423`).
   - K52: exit 0, COMPLETE_VALID.
   - KII: exit 0, COMPLETE_VALID, 26.4 s, 129.7 MB RSS.

   Both results equal the agent's result files in every field except run metadata.

## Findings disposition

- **Codex MINOR (extra lines are reported, not enforced).** Its padding example is a non-reached orbit carrying a valid but irrelevant certificate. It cannot replace a missing required orbit, and every reached orbit was verified. It is accepted as harmless under the overlay's F-2 sufficient-coverage reading.
- **Codex MINOR (failed run.json parsing gives INCOMPLETE).** This is a false-negative path only and did not occur.
- **Codex MINOR (manifest not checked against a trusted digest).** Closed by parent items 4 and 5.
- **Untested corruptions.** These include same-count wrong-orbit substitution, duplicate keys or leaves, floats, truncated gzip, forged signature binding, and isolated empty-S or hereditary failures. They are noted. The static audit found the corresponding code paths fail closed. They are not tested facts.
- **Process MAJOR F-1 remains.** CERT-FORMAT (13:38:43) and the RPLP addendum (14:00:41) postdate the Stage B start (13:37:15). This acceptance rests on the accepted written rules, the independent full re-walk and the parent re-execution, not on preregistration. The deviation is permanent and is reported.

## Scope and limits

- **Imports.** The result imports everything the written verdict imports: Sun(2)–Sun(6) as accepted, Prop 4.5 scope, and CAP. FH, L5 and L6 are not used.
- **Trust.** It trusts CPython 3.14, the OS and the hardware.
- **Independence.** One checker implementation exists. It was statically reviewed by a second model family and re-executed by the parent. No second independent checker, Lean proof or human review exists.
- **Priority.** No priority, novelty or significance claim is made.
- **Classes still OPEN:** K7 (written structural candidates under review), K6.2\* and K6.3 (Stage C held; no run), K5.3 (awaiting the Stage A X1 check).
