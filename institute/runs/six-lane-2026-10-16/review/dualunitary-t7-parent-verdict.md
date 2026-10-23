# Two-qutrit 2-unitaries are isolated among dual and T-dual gates: parent verdict

## Result

Let D and T be the sets of two-qutrit dual-unitary and T-dual-unitary gates in U(9), with the reshuffling and partial-transpose conventions of the source survey. Let O9 = {(v1⊗v2)P9(v3⊗v4) : vi ∈ U(3)} be the local-unitary orbit of the source permutation P9.

**Theorem (qualitative).** O9 is relatively open in D and in T, so it is a connected component of each ([corrected proof r3](dualunitary-parent-inputs-r3/PROOF.md), SHA-256 `ac24c12f…be67`).

**Proposition (quantitative).** Every dual or T-dual gate outside O9 has Frobenius distance at least 1 from O9; here ‖P9‖_F = 3 ([addendum v2](dualunitary-radius-addendum-v2.md), `66fb5f23…e36c`). This independently reproves the qualitative theorem with explicit radius 1.

**Corollary (imports Rather–Ramadas–Kodiyalam–Lakshminarayan, arXiv:2212.06737v2, Theorem 1: every order-9 2-unitary lies in O9).** No non-2-unitary dual or T-dual gate lies within Frobenius distance 1 of the 2-unitary set. The entangling power satisfies sup{e_p(U) : U ∈ D, U not 2-unitary} < 1, and likewise for T. No value of this entangling-power gap is claimed.

**Answer to T7 at d = 3** (Rajchel-Mieldzioć et al., arXiv:2508.04777v3, 25 Jun 2026, p.21; the gap's "rigorous existence … is yet to be established", p.9):
- Literal reading: trivially yes, through local-unitary images of P9.
- Non-trivial reading: **no**. No non-2-unitary dual or T-dual gate comes arbitrarily close to P9 or to the 2-unitary set.

The other-dimensions part of T7 and the 15/16 conjecture are not addressed. The d = 4 control, below, is not isolated.

## Verification

| Gate | Result | Artifact |
|---|---|---|
| Primary statement | Parent read T7, the isolation/gap passage and the uniqueness statement in the pinned survey PDF, and read [44] Theorem 1 | [contract](../screening/phys-1-dualunitary-t7-contract.json) |
| Worker exact certificates | Two worker implementations, matrix and four-party pictures. Constraint rank 129 for dual and T-dual systems (129×129 minor det 512); tangent rank 33 (minor −27); kernel bases cross-checked with 0 violations | [pinned inputs](dualunitary-parent-inputs-v1/pin-receipt.json) |
| Parent definition-first ranks | Integer Jacobians built directly from matrix entries, with no worker imports: ranks 129, tangent 33, J·T = 0 for both systems. The repeated-cut control gives kernel 81. At d = 4 the kernel is 136 against tangent 61, and a verified transverse enphasing direction raises tangent rank to 62 | [receipt](dualunitary-parent-check-v1.json), [checker](check_dualunitary_independent.py) |
| Parent spectral identity | Frobenius-weighted Gram matrix G satisfies G(G−2I)(G−6I)(G−8I) = 0 exactly; spectrum 0^33 2^48 6^48 8^33 for both systems | [receipt](dualunitary-radius-parent-check-v1.json), [checker](check_dualunitary_radius.py) |
| Read-only proof review | ACCEPT-WITH-FIXES; one formal group-action fix | [audit](dualunitary-proof-audit.md) |
| Claude hostile review (qualitative) | ACCEPT-WITH-FIXES: three minor justification gaps and four cosmetic items, no critical or major defect. All required fixes applied in r3 | [review](dualunitary-t7-hostile-review.note.md), [dispositions](dualunitary-review-dispositions.json) |
| Claude hostile review (radius) | **ACCEPT**: weights, six-cycle multiplicities, nearest-orbit normality and the global remainder bound were re-derived by hand. Clarity edits applied in v2 | [review](dualunitary-radius-hostile-review.note.md), [dispositions](dualunitary-radius-review-dispositions.json) |
| Codex cross-vendor review (r3 and v2) | **ACCEPT**, no fatal, major or minor findings. Its own in-memory computations reproduced the cut dictionary, the 12 free orbits, ranks 129/33, the Gram spectrum {0:33, 2:48, 6:48, 8:33}, the exact annihilating polynomial and every parent receipt field. SWAP and the identity are at distance exactly √12 from O9; random dual and T-dual examples were consistent with the radius | [final message](dualunitary-codex-review-v1/final.md), [prompt](dualunitary-codex-review-v1/prompt.txt) |

The worker, the parent and the Claude reviewers are all Claude models. The Codex review is cross-vendor to all of them. The finite algebra was checked by three independently written programs plus the Codex in-memory recomputation; the nonlinear arguments by three independent mathematical reviews.

## Priority and significance

A bounded audit ([report](dualunitary-priority-audit.md)) found no earlier proof of isolation of O9 in D or T, and no proof of the gap. The survey authors still call the gap's existence unestablished in June 2026. The thesis cited as [62] was not readable behind a bot challenge.

**Main credit issue.** Geng, arXiv:2211.15776v3 (Dec 2022, unrefereed), Propositions 6–7, already computes numerically that the pairwise linearized unitarity conditions at an OLS(3) perfect tensor have the same 33-dimensional kernel ([pinned PDF](geng-2211.15776v3.pdf), `c9fed0d1…2d9d`). Combined with the 33-dimensional orbit noted in [44] and the regular-value lemma, the qualitative theorem is close to a corollary. Geng instead drew the opposite conclusion in his Theorem 10, which conflicts with [44] Theorem 1. Any write-up must cite Geng's computation and the numerical gap observations (PRL 2020, PRR 2021).

What this adds beyond that:
- an exact hand proof through the perfect tetracode;
- exact rank and spectral certificates;
- the published-uniqueness corollary;
- the explicit Frobenius radius 1.

**Significance:** modest specialist result. It is a short rigorous answer to the non-trivial d = 3 reading of an explicit 2025–26 review question, with an explicit isolation radius. It gives no explicit e_p gap and covers no other dimension.

**FRONTIER:** CORRECTNESS-ACCEPTED, with parent exact certificates, the corrected proof, an ACCEPT radius review, an ACCEPT-WITH-FIXES qualitative review whose fixes are applied, and a Codex cross-vendor ACCEPT of both. NOVELTY: no earlier equivalent located in the bounded screen, but the core linear computation is in Geng 2022; NOVELTY-UNCLEAR. **The frozen phys-1 T7 (d = 3) target gate is met** (2026-10-17 PT).


**Attribution addendum (2026-10-17 15:19:38 PDT, appended; text above unchanged):** a new-surface audit found a method precedent or general theorem that this verdict did not cite; see [physics-priority-addendum-v1.md](physics-priority-addendum-v1.md). No correctness change.
