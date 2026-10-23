# Random 7-regular graph colouring: parent verdict

## Result and exact scope

**For the uniformly random 7-regular graph G_{n,7} (n even, n → ∞), χ(G_{n,7}) = 4 asymptotically almost surely.**

This closes the {4, 5} window that Kemkes–Pérez-Giménez–Wormald (KPW, Adv. Math. 2010, Theorem 1) leave at d = 7. It is a reviewed **written proof** that imports published theorems (KPW §§2–4 and Theorem 10, Wormald's small-subgraph-conditioning Theorem 4.1, Achlioptas–Naor's second-moment analysis, the Molloy–Reed first-moment criterion). It is not a Lean formalization. It says nothing about d = 8: the same inequality fails there (control C2 of the proof).

[Frozen target](../screening/phys-2-random7reg-colour-contract.json). The target is **DERIVED-OPEN**: its open status comes from KPW's {4, 5} window and Ayre–Coja-Oghlan–Greenhill's Table 1 (d₄,smm = 6), not from a source that explicitly names χ(G_{n,7}) as an open problem. It is therefore not counted as an explicitly-named gate.

## Frozen proof

[Final r2 proof](chi7-parent-inputs-r2/PROOF_CHI7.r2.md), SHA-256:

`f157337d864cb122247d5c9ec3c73e2d12efb5786c837404efbeafa1b6afb6a5`

[r2 manifest](chi7-parent-inputs-r2/manifest.json); [reviewed r1 and sources](chi7-parent-inputs-v1/manifest.json) (r1 `8a79ba3c…906c`, unchanged). [Complete r1→r2 diff](chi7-parent-inputs-r2/r1-to-r2.diff).

## Mathematical bridge

1. **Upper bound, χ ≤ 4.** KPW's balanced-colouring second moment plus small subgraph conditioning. An audit of every use of KPW's hypothesis d < 2(k−1) log(k−1) in §§2–4 shows that it enters only through (H1) k² − 2k − d + 2 > 0 (here 3 > 0), (H2) a global quadratic decay of φ on the Birkhoff polytope, and the trivial consequence k ≥ 3. (H2) at (k, d) = (4, 7) follows from the per-row entropy inequality D(p‖U₄) ≥ (3/2) log 3 · (Σp² − 1/4), the k = 4 case of Achlioptas–Naor's display (12), which gives decay constant C₇ = (3/8) log 3 − 7/18 > 0.
2. **n ≡ 2 (mod 4).** KPW Theorem 10 with ℓ = 7 distinguished edges whose endpoints induce a perfect matching. r2 makes the conditioning exact: on the event that v₁, v₂ are at distance ≥ 4 and lie in no triangle, the reduced structure is uniform, because the reduction map is exactly C(14,7)-to-one onto the Theorem 10 space.
3. **Lower bound, χ ≥ 4.** The published Molloy–Reed criterion at q = 3, d = 7: 9·(2/3)⁷ = 128/243 < 1. A computer-assisted first-moment maximization is a cross-check only.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Parent exact arithmetic | log 3 ∈ (13/12, 11/10) and C₇ ∈ (5/288, 17/720), so the decay constant is positive ([receipt](chi7-parent-arithmetic-v1.json)) | Checks the decisive constant, not the analytic chain |
| Worker verifier replay by parent | `verify_rigorous.py` output byte-identical ([replay](chi7-parent-verify-replay-v1/)) | Replay, not a second implementation |
| Codex CLI `gpt-6.1-sol`, hostile review of r1 | ACCEPT-WITH-FIXES, one minor, no fatal/major; independently checks the entropy proof, KPW dependency chain, SSC, the rational-log certificate and the degree-eight obstruction ([note](chi7-codex-hostile-review-v1.note.md)) | Model review, not peer review |
| Claude CLI `claude-opus-5-5`, complete review of r1 | ACCEPT-WITH-FIXES, seven minors, no fatal/major; its own audit of KPW §§1–4 agrees ([note](chi7-claude-complete-review-v1.note.md)). Its line-offset finding came from the parent's prompt rendering ([addendum](chi7-claude-source-visibility-addendum.json)) | Model review, not peer review |
| Parent source reads | KPW Theorem 10 and its full proof, Wormald Theorem 4.1 with its conclusion, Achlioptas–Naor display (12), Nir–Pérez-Giménez Theorems 1.2/3.1 | Pinned layouts in [v1 sources](chi7-parent-inputs-v1/manifest.json) and [r2 pin](chi7-parent-inputs-r2/manifest.json) |
| Parent final-delta review | All ten findings dispositioned and applied in r2; the parent re-derived the C(14,7)-to-one conditioning and the Molloy–Reed and 5 log 3 < 6 arithmetic ([dispositions](chi7-review-dispositions.json)) | r2 itself was not re-reviewed by a model; no computation changed |

## Trust, priority and significance

- The proof inherits KPW's correctness, including Theorem 10, whose proof KPW only sketch. The audit shows only (H1)/(H2) carry the d-dependence.
- [Priority audit](chi7-priority-audit.md): no source found stating χ(G_{n,7}) = 4 for the uniform model. The sharper constant is **prior work**: Achlioptas–Naor display (12), and Nir–Pérez-Giménez (arXiv:2109.13347v1) Theorem 1.2, which proves k-colourability for d < ℓ_k (ℓ₄ ≈ 7.416) for random lifts of loopless regular multigraphs and calls the extension to loops, which would give the uniform model, only "conceivable". A miss is not novelty.
- Calibrated significance: a corollary-level transfer of a published constant into KPW's uniform-model argument. It settles one degree; it is not a new threshold or method.

## Status

**FRONTIER: CORRECTNESS-ACCEPTED — reviewed written proof relying on published machinery; DERIVED-OPEN target, NOVELTY-UNCLEAR (constant prior). phys-2's χ(G_{n,7}) target is resolved (2026-10-17 PT); it is not counted as an explicitly-named gate.**

No commit, push, publication or external contact was authorized.
