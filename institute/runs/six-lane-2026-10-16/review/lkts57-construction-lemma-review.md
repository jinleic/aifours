# Independent construction-lemma audit

Reviewer: read-only `LKTS57LemmaReview` agent. Scope: frozen `lkts57-construction-snapshot-v1/automorphism-lemmas.md`, SHA-256 `184ba0ab5532f39c08396d986c274b2f323c0079ca36130ea11d69228cc29263`, and faithful finite definitions in `PriorFormal.lean`. Source inspection and mathematical derivation only: no solver or verifier was run by this reviewer, no novelty verdict or human peer review.

**Verdict: ACCEPT-WITH-FIXES.** Lemmas 0–5 and the prime-order necessary restrictions are sound apart from the trivial-Sylow qualification. The G513 resolution-pruning application is conditional on action facts missing from the text. These defects do not affect the independently verified raw LKTS(57) certificate.

## Required fixes

1. **Lines 90–95: missing action premises for Corollary 5a.** The text must define R, K, gamma and their point actions; establish preservation of the chosen resolution and cyclic layer order; and justify the block-orbit decomposition. Either supply these facts for the eight old models or state only a conditional obstruction. UNKNOWN solver outcomes are not infeasibility certificates.
2. **Lines 34–35: trivial Sylow 2-subgroups.** Replace the unconditional unique-involution assertion with: every **nontrivial** Sylow 2-subgroup has a unique involution; every Sylow 2-subgroup is cyclic, possibly trivial, or generalized quaternion. Odd-order automorphism groups have a trivial Sylow 2-subgroup with no involution.
3. **Dependency disclosure:** excluding fixed-set size 7 in the prime-order enumeration imports nonexistence of LSTS(7), not proved in this note. “Possible” fixed-set sizes 9 and 21 mean not excluded by the count, not constructed.

## Accepted arguments

- Unique pair completion gives fixed-point closure of an STS. For a proper fixed subsystem F, pick a outside F; its blocks through each x in F need distinct third points outside F and a, proving `v >= 2|F|+1`.
- For a prime-order automorphism with f>=3 fixed points, all triples of F lie in invariant constituents; each invariant constituent contributes `f(f-1)/6` such triples, giving exactly f-2 invariant constituents and `p | v-f`.
- For an involution with f>=3, the f fixed triples through one transposition pair force at least f invariant constituents, contradicting f-2. Thus f=1. The unique invariant constituent and centralizer arguments then follow.
- The order-3 block congruence and listed necessary prime-divisor restrictions are correct under the stated/imported premises.
- The orientation congruence is valid for any partition of three equal layers into triples; no STS property is needed. With 19 exclusively two-layer blocks, positive and negative counts are both 2 modulo 3.

## Conditional Corollary 5a proof

If R acts on a genuine resolution and a parallel class C has a regular orbit, then C contains at most one representative of each block orbit. Indeed, b and rb in C imply rb in both C and rC; resolution disjointness forces rC=C, and regularity forces r=1. The same argument makes block stabilizers trivial. Thus C meets exactly 19 regular block orbits.

For the asserted class pattern `1+3*9`, suppose additionally `R is C9`, its order-3 subgroup fixes exactly one point per layer, and R preserves the chosen resolution. That subgroup has exactly one fixed class. Its three fixed points and 18 point-cycle triples lie in the unique invariant constituent and must form that fixed class. Therefore the fixed class has no two-layer blocks.

If the remaining blocks consist of exactly 57 regular two-layer R-orbits, the three base classes exhaust them. Their positive-orbit counts are each 2 modulo 3, hence total 0 modulo 3 and between 6 and 51. This cannot equal 0, 19, 38 or 57, the asserted possible positive totals. The conditional contradiction is sound. Application to particular UNKNOWN models still needs the action/orbit hypotheses verified independently.

## Disposition

The parent sent all required fixes to `MathKirkman`, the sole owner of the construction source, before its seed-package freeze. The separate parent action audit confirms G513 on the actual constituent block sets, but explicitly finds that it does not preserve every chosen resolution. The raw-certificate existence theorem requires no automorphism or invariant-resolution hypothesis. Full reviewer transcript: `agent://LKTS57LemmaReview`.
