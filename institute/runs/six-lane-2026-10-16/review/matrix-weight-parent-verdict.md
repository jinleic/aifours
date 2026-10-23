# AMH Open Problem 1: parent verdict (state at 2026-10-16 ~20:20 PDT)

**Verdict: the stated Open Problem 1 is answered positively as posed, subject to the usual model-review and novelty limits.**
The worker's explicit table is a putative integer matrix weight enumerator for the hypothetical `[[24,0,10]]_2`
code: it satisfies Anglès Munné–Huber arXiv:2603.19901v1 Eqs. (31)–(35) with the Eq. (38) weight distribution.
This is **moment feasibility only**. It does not construct a stabilizer code, decide whether `[[24,0,10]]_2`
exists, certify further SDP-hierarchy levels, or establish novelty.

## Evidence

| Check | Result | Artifact |
|---|---|---|
| Parent independent exact verifier (stdlib only, no worker imports) | All 20,475 admissible orbits; 1616 positive integer entries; total `2^48`; every linear gate; all 169 PSD blocks with explicit rational Gram decompositions and separate reconstruction; two indefinite 2×2 controls rejected; 0.415 s | `matrix-weight-parent-verification-v1.json`, `check_matrix_weights_independent.py` |
| Coefficient comparison | 96,409 nonzero block terms: worker `alp` equals independent integer construction | parent session check recorded in transition notes |
| PSD-only negative control | Same affine family; all linear gates pass; parent checker rejects; block (3,3) weight-10 diagonal `−15685/163944` reconstructed independently | `matrix-weight-parent-psd-control.json` |
| Source/verifier audit (read-only reviewer agent) | corepoint-sufficient; Eq. (41) displayed formula has a typo, intended gamma matches the authors' public code | `matrix-weight-paper-to-verifier-review.md` |
| Cross-vendor Codex `gpt-6.1-sol`, max | **ACCEPT** for the stated integer moment-feasibility claim; no required fixes | `matrix-weight-review-codex.note.md`, `.receipt.json` |
| Same-vendor Claude Opus 5.5 checker review | ACCEPT-WITH-FIXES: no mathematical/checker-logic error; evidence-binding and labelling fixes (hash parsed bytes, reject duplicate JSON keys, cite Eqs31–35/38 not 29/41, rename status) | `matrix-weight-review.note.md` |
| Additional classical necessary constraints | Parent exact check: table also satisfies `0 <= x <= x_(i,0)` and the classical GST q-ary second PSD family (all 169 rescaled blocks), so these give no obstruction at this point. Re-run in standalone checker v1.1 (`--gst-second-family`), which also hashes the parsed bytes and rejects duplicate JSON keys; PSD-only and duplicate-key controls exit 1 | `matrix-weight-gst-second-family.json`, `matrix-weight-parent-verification-v1.1.json` |
| Priority/significance scout | No earlier explicit table located in a bounded 2026-10-16 screen; OP1 first appears in AMH v1; code open since CRSS 1997. Significance: **modest extension** | `matrix-weight-priority-audit.json` |
| Worker-commissioned Codex review | ACCEPT with informational notes | worker lane `frozen-candidate-v1/` |

Pinned input SHA-256: table `15a159af1078468defea70d4394f25d896b51d471ed8f2f59453502357fe73e1`.
Worker frozen snapshot manifest SHA-256: `3a504093b62c904047e73f783854d2b2d08a8c77e632b85386abe9d4ee156be1`.

## Calibration

- **Correctness:** strong for the finite claim: exact arithmetic, independent implementation, discriminating control, and two independent model reviews of the checker/claim boundary.
- **Priority:** pending the read-only priority scout. A search miss would not establish novelty.
- **Significance [INFERENCE]:** a complete positive answer to an explicitly stated 2026 open problem, but a narrow one. Its main consequence is negative for a proof strategy: this SDP level with integrality cannot exclude the hypothetical code. It is **not** a breakthrough on the underlying 1998 code-existence question.

The worker's additional claims (exact eight-dimensional genus-two family, pair MacWilliams identities, subspace divisibility) are outside this verdict.
