# gcDCQS(32⁴:0), explicit mcDSQS(128) and the mcDSQS(2^{2n+1}) family — parent verdict

Recorded 2026-10-17 PDT (host clock; evidence receipts carry their own times).

## Result and exact scope

**A gcDCQS(32⁴:0) exists.** An explicit certificate gives a candelabra quadruple system on 128 points in four groups of 32 with empty stem, together with a good colouring of every one of the 128 derived incomplete STS(127,31). This settles the v = 32 component of Tan–Zhou's explicit question §4(2) ("Find a gcDCQS(v⁴ : 0) for v = 20, 32", arXiv:2503.11934v1, LF lines 1111–1113). The v = 20 component was settled earlier in this run ([verdict](gcdcqs20-parent-verdict.md)), so **both parts of §4(2) are now answered**. [Frozen target](../screening/math-1-gcdcqs32-contract.json): construct a gcDCQS(32⁴:0) or prove none exists, with no symmetry restriction.

Consequences, kept separate from the finite result:

- **mcDSQS(128), explicit.** Tan–Zhou Construction 2.1 (s = 0) fills the four groups with the published cyclic mcDSQS(32) of Lemma 3.4/Appendix B. The filled 128-point design is checked directly here (below), so this order does not rest on the construction's proof.
- **mcDSQS(2^{2n+1}) for every n ≥ 4.** This follows from Tan–Zhou Corollary 2.6 with m = 32 and imported published inputs (below). With the published mcDSQS(32) (n = 2) and the explicit mcDSQS(128) (n = 3), **mcDSQS(2^{2n+1}) exists for every n ≥ 2**, conditional on the imports for n ≥ 4.

## Finite witness

[Pinned input](gcdcqs32-parent-inputs-v1/manifest.json): `gcdcqs32_c23.txt`, SHA-256 `e38945b1204e78937527f17db3d87f147e47885dc160c04b6a4de49377da0f46`, 4,113,669 bytes.

It lists 80,384 distinct 4-subsets of 128 points. Every one of the 321,536 triples not inside a group lies in exactly one block, and no group triple lies in any block (block group-patterns 2+2: 20,736; 2+1+1: 53,760; 1+1+1+1: 5,888). At each point x, the 2,512 derived triples are partitioned into r = χ′(127) = 64 nonempty partial parallel classes avoiding x, exactly s = 64 − (127 − 31)/2 = 16 of which avoid the hole G(x)∖{x}. Counting forces at most 16 hole-free classes: each hole point lies in 48 derived triples and in at most one triple per class. Observed profile at every point: 42⁴⁸ 32¹² 28⁴ (an observation, not part of the definition). The source's definition requires partial, not full, parallel classes, so the size-28 hole-free classes are permitted.

## Independent verification and reproducibility

| Evidence | Observed result | Scope |
|---|---|---|
| Parent definition-first stdlib checker | PASS on the pinned bytes; explicit full triple universe, all 128 colourings; r and s derived from (v, g), not trusted from the header | [checker](check_gcdcqs_parent.py) SHA `9d3f477a…e640`, [receipt](gcdcqs32-parent-check-v1/parent-result.json) |
| Parent intended-reason controls | 23/23 fixtures rejected for the intended reason (21 data mutations, wrong order, wrong digest); fixtures retained | [receipt](gcdcqs32-parent-controls-v1/parent-result.json); script v1 crashed before writing any fixture because its first hole-free class was already full, v2 (`b71eb125…`) selects an available class |
| Codex CLI `gpt-6.1-sol`, own in-memory verifier | RESULT: VALID; all 410,249 non-comment lines consumed; r, s derived from the source; 7 intended in-memory corruptions rejected | [note](gcdcqs32-codex-verify-v1.note.md) |
| Claude CLI `claude-opus-5-5`, prompt-only generic checker from the v = 20 round, executed unchanged by the parent | 52/52 runs as expected: target under `-B` and `-O -B`, wrong digest and wrong order, and all 23 mutations in both modes | [receipt](gcdcqs32-claude-checker-run-v1/parent-run-result.json) |
| Parent assembler replay | The pinned stdlib Construction 2.3 assembler on pinned ingredients reproduces the certificate byte-identically | [pins](gcdcqs32-parent-producer-inputs-v1/pins.json), [receipt](gcdcqs32-parent-producer-replay-v1/result.json) |
| Parent ingredient checks (independent code) | I1 1-FG(3,({4},{5}),16) of type 4⁴ (16 B-lines, 48 T-blocks; all 120 pairs and 560 triples covered once) PASS; I3 FDGDD(3,4,5{8}) (1,280 transverse blocks, 5,120 transverse triples, Kirkman frames at all 40 points with 4 classes missing each other group) PASS; I2 gcDCQS(8⁴:0) PASS by the parent checker. All 10 retained ingredient mutations rejected; 9/10 with the anticipated category (the moved-triple fixture fails source-class coverage before destination disjointness), so the receipt status is CONTROL-MISMATCH | [checker](check_gcdcqs32_ingredients_parent.py), [receipt](gcdcqs32-parent-ingredient-check-v1/result.json) |
| Worker full chain | I1 and I3 re-solved (kissat seed 1), I2 re-produced, re-assembled byte-identically; 21 certificate and 10 ingredient mutations; worker-run only | worker [receipt](../../../../mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups/evidence/gcdcqs32-c23/receipt.json) `909e0d19…` |

Correctness rests on the raw certificate. It does not rest on Construction 2.3, the SAT models, the symmetry used to find I3, or any restricted-model exclusion.

## Mathematical bridge and imports

Reviews: Codex `gpt-6.1-sol` **BRIDGE-HOLDS**, no fatal/major; its one minor (no I2 mode in the claimant ingredient checker) is closed by its own in-memory I2 check and the parent's ([note](gcdcqs32-bridge-codex-review-v1.note.md)). Claude `claude-opus-5-5` on the corrected LF-line source packet: **ACCEPT-WITH-FIXES**, no fatal/major, nine wording/provenance minors, all applied in this verdict ([note](gcdcqs32-bridge-claude-review-v2.note.md)). A read-only scout bridge audit also found no gap ([report](gcdcqs32-bridge-scout-v1.md)). The first Claude bridge packet used `str.splitlines()` on a PDF extraction with 25 form feeds, so its quoted source ranges were shifted; that note is not counted for the source bridge ([erratum](gcdcqs32-bridge-excerpt-erratum-v1.json)).

1. **Definition** (LF 211–220, 256–262, 281–288). With S = ∅, condition (2) is vacuous; condition (1) is checked at all 128 points. The incomplete-STS pair conditions follow from the CQS triple conditions. χ′(127) = 64 = ⌈2667/42⌉; the elementary bound and the explicit colourings make the (1.1) import unnecessary for the finite claim.
2. **Construction 2.3** (LF 444–541), (m,g,n,s) = (8,4,4,0), K₁ = {4}, K = {5}: mgn + s = 128 and mk₁ + s = 32, both ≡ 2 (mod 6), the branch proved in the source. The assembler is faithful; the assignment of I2's twelve hole-meeting classes to y ∈ B∖{x} may be any bijection, while the I3 labels are forced by the missing group. Disjointness follows from I1's Steiner-3 property: for each pair {x,y}, the member of G ∪ B through x, y and the four T-blocks through x, y partition the remaining points. This is a reproducibility route, not the acceptance basis.
3. **Corollary 2.6 with m = 32** (LF 684–693). 32 ≡ 8 (mod 12); 4m + s = 128 ≡ 2 (mod 6); 4ᵗ ≡ 4 (mod 12). Imports, not re-proved: Theorem 2.5(1) (2-RSQS*(4ᵗ), t ≥ 2; Xu–Bao–Ji, DCC 88 (2020) Cor. 3.2), Theorem 2.5(2) (RDTD(3,4,32): gcd(32,4) = 4 ≠ 2, gcd(32,18) = 2 ≠ 3; Ji–Yin and Xu–Bao–Ji), Construction 2.4 (its proof beyond LF 572 was not audited), and Construction 2.1's ≡ 2 (mod 6) branch (LF 295–335). With s = 0, an SQS(32, 0) is an SQS(32), so gcDSQS(32, 0) = mcDSQS(32) and Lemma 3.4 supplies all fillers; the printed proof of Corollary 2.6 omits this step. Output orders 32·4ᵗ = 2^{2n+1} with n = t + 2 ≥ 4, matching LF 1113.
4. **Source remark (not used).** Corollary 2.6 also admits m = 8, but Construction 2.1 then needs a 4-colouring of the filler's derived STS(7), whose chromatic index is 7: every hole point lies in every hole-meeting class, so the filler's triples could only use the four hole-free classes. So gcDCQS(8⁴:0) alone does not give mcDSQS(8·4ᵗ) by that route; m = 32 is unaffected. The orders 8·4ᵗ = 2^{2t+3} are covered anyway, by the explicit order 128 (t = 2) and the m = 32 family (t ≥ 3).

## Explicit mcDSQS(128)

[Pinned input](mcdsqs128-parent-inputs-v1/manifest.json): `mcdsqs128_c21.txt`, SHA-256 `a97b1ae50fa8f0dc7f3bb6908e6c714fdd233eeede2607c2d16c2101380fd326`, 4,362,494 bytes; 85,344 blocks covering all 341,376 triples once; at all 128 points a 64-colouring of the derived STS(127), the minimum for every STS(127) by ⌈2667/42⌉ = 64; observed profile 42⁶⁰ 38 37 36².

| Evidence | Observed result |
|---|---|
| Parent definition-first mcDSQS checker | VALID_MCDSQS ([receipt](mcdsqs128-parent-check-v1/parent-result.json)) |
| Codex CLI own in-memory verifier | RESULT: VALID; all 435,043 non-comment lines consumed; additionally all 1,024,128 derived pair incidences; 8 intended corruptions rejected ([note](mcdsqs128-codex-verify-v1.note.md)) |
| Claude-authored generic mcDSQS checker (from the mcDSQS(38) round), parent-executed unchanged | 22/22 expected runs, including both optimization modes, the published mcDSQS(32), wrong digest/order and 7 mutations ([receipt](mcdsqs128-parent-controls-v1/parent-result.json)) |
| Parent intended-reason controls | 9/9 (7 retained mutations, wrong digest, wrong order), same receipt |
| Parent independent filling | Appendix B extracted independently from the primary text (40 base blocks, 16 classes, 155 triples), developed and directly checked as an mcDSQS(32); four-group fill regenerates every non-comment line of the order-128 certificate ([receipt](mcdsqs128-parent-fill-v2/parent-result.json)); v1 stopped at its source-anchor check before writing a certificate (form-feed line splitting; [failure record](mcdsqs128-parent-fill-v1/failure.json)) |

The finite order-128 claim rests on this direct check, not on Lemma 3.4 or Construction 2.1. It is a consequence of the gcDCQS(32⁴:0), not a separate target.

## Priority, significance and limits

- **Priority.** Bounded post-result screen: NONE-FOUND-IN-SCOPE for an earlier gcDCQS(32⁴:0) or an mcDSQS(2^{2n+1}) with 2n+1 ≥ 7 ([report](gcdcqs32-priority-scout-v1.md)). It covered DataCite full-text queries, the Zenodo record families of the AI-assisted authors met earlier in this run, OpenAlex full text and citers, arXiv sweeps, and the authors' later output. The parent's own DataCite acronym query returned only Tan–Zhou v1 and Liu–Lei v2 ([capture](gcdcqs32-priority-parent-spot-v1/datacite-summary.json)). The Boolean SQS(2^{2n+1}) is not an mcDSQS (Meszka: χ′(PG(2n,2)) = 2^{2n} + 2). I1 is classical (the type-4⁴ fan from AG(2,4), equivalent to the unique S(3,5,17)). I2 and I3 were not found in readable sources. **Access holes:** Chang–Zheng–Zhou (DCC 2019, FDH designs) and Chang–Zhou (JCTA 2013) bodies, the journal version of Tan–Zhou §4 (DCC 93(10) 2025), several ScienceDirect citers, and Zenodo file contents. A miss is not novelty; whether the result was already derivable from published ingredients is not established either way.
- **Significance.** A specialist resolution of an explicitly posed auxiliary-design case, the last open component of §4(2), activating the source's pre-computed family. The non-routine content is the ingredient pair I2 and I3 and the observation that the AG(2,4) fan with K = {5} fits at m = 8. Calibrated as a modest, short-note-scale contribution that is explicit and mechanically checkable. No new general method is claimed; the number of covered orders carries no weight. General mcDSQS existence and §4(3) remain open.
- **Limits.** No Lean proof (the comparable v = 20 replay needed about 1,014 s and 5.0 GB, so an unsharded order-128 proof would likely exceed the 8 GiB lane cap). The infinite family imports the listed theorems and constructions; only the finite inputs (gcDCQS(32⁴:0), the published mcDSQS(32) and the explicit order 128) were checked here. Corollary 1.4(1)'s coding consequence q₀′(3,4,2^{2n+1}) = 2^{2n} + 1 is a further import, not checked. Model reviews are not human peer review.
- **Process deviations (this package).** Earlier lane deviations are recorded in the lane README §4 and the [ledger](../outcomes.md): possibly unmeasured >8 GiB concurrent KM builds at 08:35, a freeze row written after launch, estimated time labels, SIGTERM stops (UNKNOWN), a tool-deadline kill, a launch race, and a 14:03–15:11 checkpoint gap. The parent's failed attempts above are retained, not relabelled.

**FRONTIER: CORRECTNESS-ACCEPTED — explicit gcDCQS(32⁴:0) checked by three independently authored routes, intended-reason controls, parent assembler and ingredient replays, and cross-family bridge reviews; explicit mcDSQS(128) likewise accepted; NOVELTY-UNCLEAR. The frozen math-1 gcDCQS(32⁴:0) gate is met (2026-10-17 PT).**

## Review-disposition clarification — 2026-10-17 PT

All review findings were **addressed**, not all requested editorial source changes applied: frozen producer/checker bytes were preserved. The exact nine-item [disposition table](gcdcqs32-review-dispositions-v1.md) records the applied/declined requests, the third-checker accept/reject counts and the scope of the unmeasured Lean-memory inference. No mathematical result or gate disposition changes.
