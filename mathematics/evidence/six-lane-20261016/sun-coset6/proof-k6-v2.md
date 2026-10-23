# proof-k6-v2: candidate proof composition for Sun's disjoint-coset conjecture at k = 6 (CONDITIONAL; supersedes proof-k6-v1)

**Freeze record.** Host-clock time and sha256 are in `evidence/proof-k6-v2.sha256`.

**Status.** Candidate proof, written in this lane. It is computer-assisted and has not been checked in Lean. No k = 6 theorem, no gate and no novelty is claimed. The final parent verdict decides.

**Changes from proof-k6-v1 (b8ac51a1…ecd6).** This version only re-cites:
- `rules-k6-erratum-v1.md` and `rules-k6-erratum-v2.md`;
- `CERT-FORMAT-k6-v2.md`;
- the accepted Core(5) record.

The engine, the certificates and every rule predicate are unchanged.

## Components

| component | file(s) | status |
|---|---|---|
| R0, R1(6) (Sun(6) ⟺ Core5(6)) | README §2; erratum-v1 E1; erratum-v2 F2 | Codex ACCEPT (rules-v1 review); parent re-derived by hand |
| Core(5) input | `R/sun-coset5-parent-verdict-v1.md` (2cf02436…5301), binding sun-coset5 proof-v4 and rules-v1-erratum-v3 | CORRECTNESS-ACCEPTED (not a gate for an open target; a prior unpublished claim by Z. Gong exists) |
| Prop 4.5 | sun-coset5 proof-v4 §2 | accepted with the Core(5) record |
| T, K, P, F, H5, RLP, M1/M2 | rules-k6-v1 with erratum-v1 | Codex and Claude: ACCEPT or ACCEPT-WITH-FIXES, with the fixes recorded in erratum-v1 |
| L9 hereditary Sun | rules-k6-v2; proof-k6-lemmas-v1 §1 | Codex delta: ACCEPT; Claude delta: pending |
| L10 XE | rules-k6-v3; proof-k6-lemmas-v1 §2 | Codex delta: ACCEPT |
| L11 N2-6 | rules-k6-v3; proof-k6-lemmas-v1 §3; **erratum-v2 F1** (corrected E3 test and τ table) | Codex delta: ACCEPT-WITH-FIXES, fixed in erratum-v2 |
| L12 RPLP | rules-k6-v3; proof-k6-lemmas-v1 §4 | Codex delta: ACCEPT |
| Certificate format | `CERT-FORMAT-k6-v2.md` (26b1dbcc…854c), with explicit PB rounding and the N26 test | Codex delta: ACCEPT-WITH-FIXES, fixed in v2 |
| Certificates | `evidence/engine-v3-core56/` (hashes in `evidence/engine-v3-run.sha256`) | see below |

## Proof composition

1. **Reduction to a finite group.** By R0, G may be taken finite.
2. **Minimal counterexample.** Suppose Sun(6) fails, and let G be a counterexample of minimal order. By R1(6), which holds group by group, G carries a Core5(6) configuration.
3. **What each rule may assume.**
   - Sun(k) for k ≤ 4 holds in every group (Zhu Theorem 1.1, L0.6).
   - Sun(5) holds in every group (the accepted Core(5) record).
   - Sun(6) holds in every proper subgroup of G. It is used only inside an FH5 fibre of a proper subgroup H < G, when 6 vertices meet one H-coset (erratum-v1 E4).
4. **Reduction to finitely many patterns.** Each configuration gives a pattern (α ∈ {1,2,3,4}^15, with markers E2/class, E3, E5). Up to S6, the pattern is a labelling of one of the 8 types in CERT-FORMAT §1.
   - Labellings containing a T-forbidden triangle are impossible (rules-k6-v1 L1).
   - Every other labelling is one of 1,575,031 T-consistent leaves, forming 61,124 stabiliser orbits.
5. **One certificate per orbit.** Every orbit carries a certificate. The counts are:

   | rule | orbits | proved by |
   |---|---|---|
   | K | 55,159 | |
   | RLP | 5,513 | exact duals for every admissible q |
   | FH5 | 134 | all 7 placements of E5 |
   | N26 | 108 | |
   | PB | 55 | |
   | RPLP | 155 | exact dual or Farkas vector for every admissible q |

   There is no SURVIVE line. Each certificate is valid for every admissible τ (M1) and for every r carrying the given markers (M2, using the saturation argument of erratum-v1 E5).
6. **Conclusion, conditional.** If the parent's final verdict accepts the certificate replay and the v2/v3 lemma reviews, then no Core5(6) configuration exists. Hence Sun(6) holds for every group.

## Verification status (at the time of writing)

**Parent checks, reported by the parent over IRC; the parent holds the record.**
- All 1,575,031 labelled leaves were checked independently.
- The coverage of the 61,124 orbits was checked exactly.
- Every K, RLP, PB, N26 and RPLP witness was checked.
- A separate FH5 replay passed 134 out of 134.

**Still pending.**
- The separate-author full checker is still running.
- The Claude review of the v2/v3 changes is pending.

**Lane self-check.** `code/core56_checkB_v1.py` was a same-author self-check applying the v2 rules only. On parent instruction it was stopped cooperatively with SIGTERM at 12:02:48 PDT. Its outcome is UNKNOWN; the stop receipt is `evidence/checkB-v1-run1-STOP-RECEIPT.json`. Before the stop, it had finished 4 of the 8 types, and its leaf counts matched the engine's. It is not acceptance evidence.

**Not done.**
- Lean.
- A post-result priority audit, which the parent will run.

**Claims made.** Nothing is published. Neither "first" nor "novel" is claimed.
