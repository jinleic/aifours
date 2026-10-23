# rules-k6-v2: the hereditary Sun condition (addendum to rules-k6-v1)

**Freeze and status.**
- The host-clock freeze record is in `evidence/freeze-v2.sha256`.
- `rules-k6-v1.md` (3b135fea…b187) stays frozen and unchanged.
- "[NEW]" means only "written in this lane"; it is not a novelty claim.

## L9. Hereditary Sun condition [NEW]

**Statement.** Take the setting of rules-k6-v1 L5 (F2) or L7 (R4′). Let C be a left coset of H in (F2), or a right coset of U_v in (R4′). Let S_C be the set of vertices whose pieces lie in C, with local indices λ_l in (F2) or d_l = q_lr_l in (R4′). Then for **every** subset T ⊆ S_C with |T| ≥ 2, some pair in T has gcd ≥ |T|.

**Proof.**
1. **The pieces of T are pairwise disjoint.** The pieces of all of S_C are pairwise disjoint, so in particular the pieces indexed by T are.
2. **Move them into the subgroup.**
   - In (F2): left-translate by z⁻¹, where z ∈ C. This gives pairwise disjoint left cosets in H of the subgroups U_l∩H.
   - In (R4′): right-translate by w⁻¹, where w ∈ C, and then invert. This gives pairwise disjoint left cosets in U_v of subgroups of index d_l.

   The translation steps are those of rules-k6-v1 L5 and of sun-coset5 proof-v4 §5 (R5′).
3. **Apply Sun(|T|).** Apply Sun's statement for k = |T| inside H, or inside U_v, using the inputs of rules-k6-v1 §0:
   - |T| = 2: L0.6.
   - |T| ∈ {3, 4}: Zhu Theorem 1.1.
   - |T| = 5: Sun(5). This rests on sun-coset5 proof-v4, a stated dependence.
   - |T| = 6: this can occur only in (F2), because in (R4′) S_C contains at most 5 vertices. Here use the minimality of G, since H is proper.

   So some pair of T has gcd ≥ |T|. ∎

**Effect on the rules.**

| Rule | Change |
|---|---|
| (F2) in FH5 | An assignment is rejected if the condition fails for **some** subset T of the vertices meeting a coset. rules-k6-v1 tested only T = S_C. |
| RLP (rules-k6-v1 L7) | A support S is **allowed** only if every subset T ⊆ S with \|T\| ≥ 2 has a pair with maxgcd ≥ \|T\|. |

The allowed family is therefore closed under taking subsets. The "maximal sets suffice" step and the soundness argument for maxgcd go through unchanged. A smaller allowed family can only raise LPmin, and the new condition is valid for every instance, so every RLP kill remains sound.

**Engine.** `code/core56_engine_v2.py` is `core56_engine_v1.py` with exactly two functions changed:
- `lp_min`: its allowed-support test becomes the hereditary condition;
- `fibre5_feasible`: its coset test becomes the hereditary condition.

The exact diff is in `evidence/engine-v1-to-v2.diff`. Everything else is unchanged: the enumeration, the T pruning, the canonical forms, K, P, M1/M2 and the E5 loop.
