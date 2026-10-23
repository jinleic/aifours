# Constructive zero-sum tripling — parent acceptance, 2026-10-18T01:11:53-07:00

**CORRECTNESS-ACCEPTED as an auxiliary construction for the already-closed Tan–Zhou §4(3) result. No new gate, new infinite family or novelty claim.**

1. Every finite 3-regular 3-partite 3-uniform hypergraph (indexed edges allowed), after its zero-sum Z3 blow-up with any fixed sum s, splits into nine perfect matchings.
2. Consequently, every H(5,6,4,3), inflated by the zero-sum TD(3,4,3), has explicit Kirkman frames at all 90 points and is an FDGDD(3,4,5{18}).
3. The new [certificate](tz43-tripling-parent-v1/fdgdd_5_18_konig_tripled.txt), SHA `5442b8c71612f9e021bdb990ea8931cf0919514bf4685f70d59dd80ce804ff12`, is VALID by three separately authored checker implementations. It replaces only the frame-SAT construction step, not the SAT-derived master H(5,6,4,3).

## Mathematical check

Accepted text: [lemma-v2.md](tz43-tripling-parent-v1/lemma-v2.md), SHA `3ad31c7bcaf89fb4a1e785e330a4566e7207c0a2b7d6ee4244d76ce926f1d511`. The parent read §§0–2 and the application: Hall's theorem decomposes the cubic incidence bipartite graph into three perfect matchings. This proves the needed König consequence; **Hall's theorem itself is imported, not proved in that note**.

At a lifted third-part vertex (c,z), the required label P forces

    u(c,e) = s − z − P1 − P2 mod 3.

The incidence colours at c are exactly 0,1,2, so one and only one incident edge supplies the lift; the other two coordinates are then forced. At either other part, the first or second label coordinate gives the analogous unique edge. All lift indices have one label, proving partition as well as coverage. For a 3-GDD of type 6^4, pair counts give each missing-group family degree g/2=3. At a derived point (p,β), apply the lemma with s=−β to each of its four families. This proves frames, not block resolution or RDGDD. No assertion extends to g=4,8 or arbitrary g.

## Verification

- The original accepted witness `3e22f502…a998` remains unchanged. The parent independently compared the first 14,588 LF lines (header/groups/blocks): byte-identical. Both witnesses have 14,580 blocks; only the chosen frames differ.
- The desk's own deterministic construction uses 120 cubic incidence colourings and produces 3,240 classes (36 per point, 18 triples each). The independent parent checker and Claude prompt-only checker both accept the written bytes. The desk's v2 matrix contains 52/52 expected results, including intended frame, sum-constant and duplication mutations, under Python 3.9.6/3.14.3 normal/optimized modes. These are two implementations, not 52 independent routes. [Receipt](tz43-tripling-parent-v1/receipt-v2.json), SHA `8ecd6f4163271978b1633089e7e99237a2105237946abca6bbde49b67eb217a4`.
- **Third implementation, executed by this parent:** recovered the exact Codex-authored verifier source from the original `tz43-codex-verify-v1.stderr.txt` LF513–1012, decoded its two shell quoting layers, and selected its unchanged parsing/verification definitions using the AST. No worker/checker code was imported. The new positive and all four retained mutations produced their preregistered categories (5/5), in 3.203 seconds. [Receipt](tz43-tripling-codex-replay-v1/RESULT.json), SHA `9b0b2dc3206ffac12e198eb0a55f09833718ee0327be6b04c4916eba9ca05cbf`. This is parent execution of preserved Codex-authored code, **not a new Codex CLI verification call**. Source, extraction rule, hashes and pre-execution input pins are retained beside it.

## Reviews and dispositions

Codex gpt-6.1-sol: ACCEPT, no findings. Claude claude-opus-5-5: ACCEPT-WITH-FIXES, 10 MINOR, no MAJOR/FATAL. [Disposition map](tz43-tripling-parent-v1/dispositions-v1.md), SHA `7f6ec5fd20ccaa62d404fd8f375f91412e92f0c0a954b4297ecc858f65140f8d`.

The three mathematical repairs make edge indices explicit, spell out third-part containment, and derive the counts 72/540. The remaining changes add binding, reparsing and fresh-output protections or correct wording. No accepted statement or certificate byte changed. The v2 files were not re-reviewed by the CLIs; the parent reads and accepts the mathematical delta, and the third checker independently validates the final certificate and its four controls.

## Limits

No novelty screen was commissioned for this lemma; it is a short consequence of Hall/König and may be folklore. This construction does not change the gcDCQS ingredient, the mcDSQS74 object or the imported higher-order family. The original §4(3) gate remains based on its previously checked objects. No Lean formalization or human peer review is claimed. The desk receipt's assumed parent-model-family labels were not independently verified; checker authorship here is stated by artifact, not inferred from the current parent model.
