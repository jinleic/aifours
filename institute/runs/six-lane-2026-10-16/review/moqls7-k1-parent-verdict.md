# Theorem K1 and its order-7 corollaries — parent verdict (phys-2) — 2026-10-17 23:10:53 PDT (host clock)

**Disposition: GATE MET (phys-2), via two explicitly listed open order-7 cases; M(7) itself is NOT decided.**

- **Theorem K1 — ACCEPTED (computer-assisted).** No set of three mutually orthogonal quantum Latin squares of order 7 has exactly one non-classical square. Equivalently, every ONB-assignment in C⁷ on a 4-net of order 7 is classical: the five maximal 4-nets admit none, and on both Desarguesian 4-nets every assignment uses only 7 rays.
- **Corollaries — ACCEPTED.**
  - Every 2-resolvable QLS(7) (Zhang–Cao, Definition 1.1) and every pandiagonal QLS(7) (Huang–Li) has cardinality 7.
  - Hence **no MCPQLS(7) exists**. Huang–Li, arXiv:2606.27758v1 §5: "the existence of MCPQLS(7), MCPQLS(11), and MCPQLS(n) with gcd(n,6) ≠ 1 remains to be determined".
  - Hence **no maximal-cardinality 2-RQLS(7) exists**. Zhang–Cao, arXiv:2608.29201v2 §5: the known results are "gcd(v, 6) = 1 and v ∉ {5, 7, 11} …", and the existence for the remaining orders is open.
  - The parent read both passages in the arXiv PDFs on 2026-10-17 PDT.
- **Correctness:** VERIFIED as a computer-assisted proof, five independent parent routes plus hostile reviews.
- **Priority:** NONE-FOUND-IN-SCOPE; this is a bounded screen.
- **Novelty:** UNCLEAR. The (C1)/net reformulation is prior art (Ball–Simoens arXiv:2603.02334v1 Lemma 21; Zhang–Cao Lemma 2.2); only this order-7 case is new as far as was located.
- **Significance:** a specialist result that settles two order-7 exceptions listed in 2026 preprints.
- **Status of M(7):** still 2 or 3. K2 (exactly two non-classical squares) and K3 (three) are candidates under verification, not accepted here.

## Claim documents (lane `physics/evidence/six-lane-20261016/moqls7-maximum/review/`)

| File | sha256 |
|---|---|
| K1-THEOREM.r1.md (reviewed) | `b702b021e94aafeaace754370b79a2f11c0e8bfebcfb3a3984df720d0e728767` |
| K1-THEOREM.r2.md | `98b06d226d0c53d7db53540a6760be049e6df3aaba62aefdfa69024837842f59` |
| K1-THEOREM.r3.md (accepted text) | `2d77c63719fafd1e7f7cfe2a3161931f2e90dff0976e3ee9c5083a88d076a096` |
| K1-COROLLARY.r1.md (accepted text) | `7ded3c698163c18757a21964d3552e053f1081f9fd854895054a606e56ef6b6d` |
| LEMMAS.md | `4bddc9d422cf989bb9bfdf4f09de72742ea2d423b9a082f8fd76263ba1c850c9` |

## Independent parent verification (subagent M7K1Verify; [RESULT.json](moqls7-k1-parent-check-v1/RESULT.json) `f46a741602fcc36cda6828e282063d14cb8df4bb4f3fbc81bccbb3db74396570`; the parent re-hashed all five route receipts and read the full-classification and support-enumerator C sources)

1. **Net classes.** Parent C code enumerated all 16,942,080 reduced Latin squares of order 7 together with all their transversals and orthogonal mates. It found 342,480 reduced lists of 2-MOLS(7), every one inside exactly one of the 7 listed classes and each orbit element hit exactly once.
   - |par| was recomputed by explicit automorphism counting: 126, 6, 6, 24, 48, 2352, 3528.
   - The sum matches the Egan–Wanless totals (342,480 overall; 341,880 for the maximal classes), quoted from the pinned arXiv:1406.3681v2.
   - The completeness of the class list therefore does not rest on the published totals.
2. **SAT replay.** All 14 final CNFs and 14 DRAT proofs were reproduced byte-for-byte from the pinned encoders, and the parent drat-trim gave 14/14 `s VERIFIED`.
   - Checker controls: a SAT CNF with an empty-clause proof gives NOT VERIFIED; contradictory units with a 0-byte proof give VERIFIED; four mismatched-proof controls are rejected.
   - The model sets are identical between encoders A and B (0,0,0,0,0,4,5).
3. **Third route, not SAT.** Parent backtracking enumerators in two independent search modes start from all 127 nonempty supports per point. The frame lemma emerges from F2, and they return exactly the same patterns.
4. **Phase cycle.** Exactly recomputed: the seven relations, the signed sum cancelling every phase variable, and the odd multiple of π.
5. **Controls C1–C4.** Replayed, and C1/C2 re-checked with parent code, including the genuine non-classical Ball–Simoens Ψ(f) and the 4×4 example.

## Hostile reviews

| Review | Disposition | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| Codex `gpt-6.1-sol`, whole claim ([note](moqls7-k1-review-codex-v1.note.md)) | ACCEPT-WITH-FIXES | 0 | 2 | 5 |
| Claude `claude-opus-5-5`, whole claim ([note](moqls7-k1-review-claude-v2.note.md)) | ACCEPT-WITH-FIXES | 0 | 0 | 13 |
| Codex delta r1→r3 + corollary ([note](moqls7-k1-delta-codex-v1.note.md)) | ACCEPT-WITH-FIXES | 0 | 0 | 2 |

- The two Codex MAJORs were missing drat-trim control receipts, and unsupported exploration claims (315/97/MILP minimality).
- Both are resolved in r3: the parent route-2 control receipts are cited by hash, and the exploration claims are withdrawn.
- See the [delegated delta check](moqls7-k1-delta-v1/delta-check.md) (DELTA-ACCEPT-WITH-NOTES, all 20 findings mapped). Four non-blocking wording/provenance notes remain:
  - the checker build citation;
  - attribution of the producer statuses;
  - the RESULT.json hash;
  - a frozen code comment.

## Corollary bridge (parent-checked)

- **Pandiagonal QLS(7).** Rows, columns and broken diagonals in both directions form the 4-net with slopes {∞,0,1,−1}. The affine shear (x,y)↦(x,y+x) maps it line for line onto the lane's class 5 (harmonic, slopes {∞,0,1,2}), and not onto class 6. This was checked by parent computation against the pinned class file ([spot check](moqls7-k1-corollary-parent-spot-v1.md)) and independently by the delta desk.
- **2-RQLS(7).** By Zhang–Cao Lemma 2.2 (forward direction), a 2-RQLS(7) A plus two classical squares forms a 3-MOQLS(7). If A were non-classical, that triple would contradict K1.
- **Cardinality.** A single square using 7 rays is classical, and its cardinality (distinct vectors up to global phase) is then 7. Maximal cardinality would be 49.

## Priority

- Scout M7K1Priority: NONE-FOUND-IN-SCOPE ([transcription](moqls7-k1-priority-scout-v1.md)). The field is active: the Cao group posted four 2026 preprints.
- Access holes: Semantic Scholar, Google Scholar, MathSciNet and CNKI were not checked; Zenodo API returned 403; arXiv submissions after the 2026-10-15 announcement were not public.
- Re-screen before any release.
- Suggested wording: "No QLS(7) orthogonal to two MOLS(7) is non-classical; equivalently every 2-RQLS(7) is classical. Hence every PQLS(7) is classical, and neither an MCPQLS(7) nor a maximal-cardinality 2-RQLS(7) exists. M(7) ∈ {2,3}."
- Never write "first", and never claim to determine M(7).

## Gate reasoning and limits

- **Why this meets the gate.** The run contract's gate admits "a complete solution or counterexample to an explicitly stated open target". Both corollaries answer cases explicitly listed as undetermined in primary sources, with full quantifiers (arbitrary complex unit vectors, no symmetry assumption).
- **Recorded as found after the fact.** The frozen phys-2 slot target is M(7). These two targets were recognised by the post-result priority screen; the contract already cited Huang–Li's MCPQLS(7) as a related open case. This verdict records that provenance and does not relabel M(7) as decided.
- **Remaining limits.**
  - Computer-assisted proof: it trusts the Python encoders (with two independent encoders plus a parent non-SAT enumerator), CaDiCaL/kissat only as producers, the drat-trim checker and the parent C code.
  - It is not Lean-checked.
  - There has been no human peer review.
  - The 2026 sources are unrefereed preprints.
- **Deviations recorded by the verifiers:** some non-exclusive tool writes at fresh paths, compiler temp files in the macOS per-user temp dir, a Claude review timeout (v1, preserved), and snapshot directories created with exist_ok=True below fresh roots. None of these affects the checked evidence.
