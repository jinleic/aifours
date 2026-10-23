# Six-lane research round — outcome ledger (state at 2026-10-16 PT)

Contract: [`contract.json`](contract.json), 48-hour authorization from 2026-10-16 18:31:43 PDT to 2026-10-18 18:31:43 PDT. Slot changes: [`transitions.json`](transitions.json). Worker checkpoints and parent status: [`checkpoints.md`](checkpoints.md). Every timestamp below comes from a tool receipt or the host clock.

## Headline

**Mathematics met the contract's breakthrough gate.** Large sets of Kirkman triple systems of orders **57** and **87** were constructed explicitly and verified independently ([verdict](review/lkts-57-87-parent-verdict.md)). Wang's 2026 survey of known constructions ([arXiv:2607.21521v1 §4](https://arxiv.org/html/2607.21521v1#S4)) named these as the only admissible orders below 200 still possibly without an LKTS. Combined with that survey, **no admissible order below 200 remains open**. That combined statement inherits the survey's premises at uneven evidence levels; order 147 is the weakest.

The universal question in the book (an LKTS of every admissible order) remains **open**. Priority is **unresolved**: the bounded literature search found no earlier construction, which does not prove novelty. There has been no human peer review, publication or Lean proof.

The contract defines a breakthrough as a complete solution of an explicitly stated open target. It requires independent parent verification, cross-vendor review and a primary-source comparison. LKTS(57) was the frozen target of the math-1 slot, and LKTS(87) is the other order Wang names. Both were checked by three separately written verifiers (parent stdlib; cross-vendor Codex `gpt-6.1-sol`; a Claude-written program), each with mutation controls. Compact seeds regenerate both certificates byte for byte. The method is an established design-theory technique: prescribed automorphism groups, Kramer–Mesner exact cover, and resolution SAT. Its contribution is the specific groups and orbit-forcing lemmas, not a new general method.

## Results by slot

| Slot | Target sequence | Best verified outcome | Verification level | Status |
|---|---|---|---|---|
| math-1 | LKTS(57), then LKTS(87) | **Both constructed**: G513=(Z19⋊Z9)×Z3 for 57; G903=Z43⋊Z21 on {∞}∪Z43×{0,1} for 87 | Exact finite certificates; three independent verifiers; mutation controls; seed byte replay; action audits; construction-lemma review ACCEPT-WITH-FIXES (fixes applied by the worker) | Breakthrough gate met for the finite targets. NOVELTY-UNCLEAR. Worker exploring a uniform v=2q+1 construction |
| math-2 | Ordered Olson EGZ conjecture | For dihedral groups D_2p: **Theorem P** covers a large class of words. A Doubling lemma, a Davenport lemma and **Theorem R** (rigid words, all p>=3) add further classes ([proof map](../../../mathematics/evidence/six-lane-20261016/olson/proof-dihedral-partial.md)) | Theorem P: worker Codex review "correct", no fixes. Other lemmas are written proofs with constructive checkers, not independently reviewed. A separate Codex note proves universal counting bounds; parent hand-check plus finite controls ([note check](review/olson-lifting-codex-parent-check.md), [controls](review/olson-note-finite-controls.json)) | PARTIAL: the residual "diverse" word class is open; no full D_2p proof yet |
| phys-1 | Depolarizing-channel quantum-capacity threshold | **Candidate**: an explicit 2000-qubit state with rigorously enclosed I_c in [1.12885e-8, 1.14364e-8] bits at p=1/5 ([verdict](review/depolarizing-parent-verdict.md)) | Exact sector-bridge review ACCEPT-WITH-FIXES (no mathematical error). Independent float reproduction gives 1.14134071e-8 bits, inside the interval, with all 220 sectors inside. Same-state sign controls are negative | CANDIDATE: provenance-bound rerun, combine-step mutation controls and revised proofs still pending. If certified, it would exceed the certified 0.194868 and stay below the claimed asymptotic 0.2029161 |
| phys-2 | ((7,3,3))_2 code → AMH Open Problem 1 → spin alignment n=3 → depolarizing majorization n=4 | (a) An integer matrix-weight table for the hypothetical [[24,0,10]]_2 **answers AMH Open Problem 1 positively** as moment feasibility ([verdict](review/matrix-weight-parent-verdict.md)). (b) **Three-qubit depolarizing-output majorization holds for every state and all physical p in [0,4/3]**, the n=3,d=2 case of SWTF arXiv:2609.37240 Eq. (2) ([verdict](review/three-qubit-majorization-parent-verdict.md)) | (a) Exact parent checker: all linear gates and 169 PSD blocks, extra classical constraints, negative controls; Codex ACCEPT. Modest extension; it does not establish that the code exists. (b) Written proof importing Song–Chen Prop. 3, plus an exact spectral reflection p↔2−p (20 exact matrix controls). Worker Codex ACCEPT-WITH-FIXES (applied); parent Claude review ACCEPT | (a) Done. (b) Priority screen running. Song–Chen's general Conjecture 2 is open. For n=4 the worker reports exact partial Ky Fan certificates (unreviewed, not parent-verified); the target is open |
| info-1 | Balanced 9-variable NL242 → exact guessing number gn(R⁻) | NL242: sign-digit identities (Claims 1–4, Cor. 5) reviewed, Claude ACCEPT-WITH-FIXES and Codex ACCEPT; **no residue type excluded**. gn(R⁻): an **exact obstruction**. A 625-word code violates all eight diamond conditional Ingleton inequalities at once, so no proof of 20/3 can rest on them alone ([parent check](review/guessing-number-fan-code-parent-check.json)) | Boolean: focused reviews plus parent finite controls ([check](review/boolean-digit-parent-check.json)). Guessing game: parent's independent exact recomputation, using the worker's graph transcription | Bounds unchanged: 20/3 ≤ gn(R⁻) ≤ 1847/276. Open |
| info-2 | Robust SPR synthesis, degree ≥ 7 | Exact structural controls. Two rational generalized-rectangle families at n=6 provably admit no nonzero closed numerator, and a strictly stable shrunken family has an exact 8-point certificate that no numerator of degree ≤ 6 works. So any proof must use the monotone coefficient-box structure ([lane](../../../information-science/evidence/six-lane-20261016/robust-spr/README.md)) | Exact rational certificates checked by the worker. These are not book counterexamples, and the parent has not replayed them | Open; adversarial box/chain-configuration work continues |

Cancelled before launch: the information-science replacement target on static output feedback. An unrefereed public note dated 2026-10-03 already claims its witness cases ([record](screening/sof-prior-art-collapse.md)). Superseded slot targets keep their evidence and dispositions in `transitions.json`; nothing was overwritten.

## What the evidence does not establish

- No universal book question is solved: neither LKTS for every admissible order, ordered Olson for all groups, the depolarizing threshold, balanced NL242 existence, gn(R⁻), nor robust SPR for every n ≥ 7.
- Model reviews are not human peer review. Search misses are not novelty. UNKNOWN or timeout outcomes and floating-point values are not certificates.
- The all-orders-below-200 LKTS corollary imports the published constructions summarized by Wang; we checked only that no listed family reaches 57 or 87.
- The three-qubit majorization proof depends on Song–Chen Proposition 3 as published, which was not re-proved.

## Next actions, by scientific value

1. Seek expert or primary-literature confirmation of LKTS(57)/LKTS(87) priority, then prepare a compact external-review package. The certificates, seeds, verifiers and construction notes already exist. Publication or contact requires owner authorization.
2. Close the depolarizing certificate gates: a provenance-bound rerun, combine-step mutation controls and revised proofs.
3. Resolve the priority of the three-qubit majorization; continue the n=4 case with a strengthened relaxation or a proved obstruction.
4. Find a uniform algebraic construction for v=2q+1, q≡7 (mod 12). This must be a proof; more finite cases do not count.
5. Close the residual diverse-word class for D_2p, with an independent review of the Doubling, Davenport and Theorem R lemmas.

## Reproduction (from `/Users/jinleic/repos/aifours`)

```sh
python3 -B institute/runs/six-lane-2026-10-16/review/check_lkts_independent.py institute/runs/six-lane-2026-10-16/review/lkts57-parent-inputs-v1/lkts57_g513.txt
python3 -B institute/runs/six-lane-2026-10-16/review/check_lkts_independent.py institute/runs/six-lane-2026-10-16/review/lkts87-parent-inputs-v1/lkts87_g903.txt
python3 -B institute/runs/six-lane-2026-10-16/review/lkts-claude-verifier-v1/checker.py 87 institute/runs/six-lane-2026-10-16/review/lkts87-parent-inputs-v1/lkts87_g903.txt 65ab29ae6d24545c4ed41c3a4ea027becdf497b6810384b728379cfd0cae273e
python3 -B institute/runs/six-lane-2026-10-16/review/check_matrix_weights_independent.py institute/runs/six-lane-2026-10-16/review/matrix-weight-parent-inputs-v1/evidence/lambda_24_0_10.json --gst-second-family
/Users/jinleic/.local/state/research-explorer/venv/bin/python -B institute/runs/six-lane-2026-10-16/review/check_qubit_depolarizing_spinflip.py
```

No commit, push, publication, external contact, deletion, paid-API fallback, global configuration change, cron or launchd job, or live-infrastructure mutation was performed. Prior engine records, attack snapshots and continuation evidence are unchanged.
