# Five-variable gluing inequality versus all subset substitutions of named families

**Status: WRITTEN with two independent-structure exact enumeration checks; scientific and source-theorem review pending.** This strengthens the **scope** of `frontier-20261028-fivevar-family-separation-v1.md` (SHA-256 `82a56e0c8775eca1e37f547be4e4b519ce9a56cd42f882f6af412e4b367a8774`) using a different separating point. It does not claim full literature novelty, entropy realizability, or an improved R-minus guessing-number bound.

## Separating point and precise conclusion

The five-variable universal gluing inequality `Psi>=0` is given in `frontier-20261028-five-variable-gluing-inequality-v1.md` (SHA-256 `ef9cb87907bd255d75f4154a11fe5471072e8959e622376bea6469ad60462df4`). In subset-mask order `C,R,H,P,Q`, the following integer vector is a Shannon polymatroid with `Psi=-13`:

```
 0–7:   0 34 35 53 32 48 51 53
 8–15: 25 43 46 62 57 57 62 62
16–23: 32 49 45 62 47 62 60 62
24–31: 47 53 56 62 62 62 62 62
```

It satisfies all 85 elemental Shannon inequalities. In addition, it satisfies all the following, with **arbitrary subset-valued role substitutions, including overlaps and empty sets, into these five variables**:

1. The entire named universally valid `F_n` family for every positive integer `n`; an arbitrary extra outer conditioning can be absorbed into its conditioning set.
2. The entire pinned Csirmaz–Csirmaz (2026) Theorem 1 family for every finite downward-closed staircase and every outer conditioning subset `W`.
3. The entire pinned 2026 Theorem 2 family for every positive integer `k` and every outer conditioning subset `W`.

Consequently the five-variable coefficient vector `Psi` is not a finite nonnegative conic combination of elemental Shannon inequalities and those three named families under those subset-valued substitutions: the listed point evaluates every generator nonnegatively but evaluates `Psi` negatively. This is **not** a statement about other published inequalities, arbitrary deterministic functions not expressible as subset unions, extra auxiliary-variable derivations/projections, or full literature novelty. The source paper's separate completeness conjecture is not addressed.

## Exact finite coverage of the infinite families

For `F_n`, two differently batched exact scanners checked all `17,301,504` choices of arbitrary subset-valued `A,B,C,D,Z` modulo the valid `A/B` symmetry, including empty and overlapping roles. Both use exact integer minimization over **all positive n** and give minimum twice-slack zero.

For the two 2026 families, the scans range over every outer conditioning subset `W`. Conditional entropy is the contraction `h_W(S)=h(S union W)-h(W)`, so components of any role inside `W` are redundant. The five roles `A,B,C,D,Z` can therefore be enumerated as arbitrary subsets of the complement of `W`; this covers all overlapping original role/conditioning assignments without repeating equivalent ones. The scanners checked:

* **20,277,625** Theorem 1 substitutions modulo `A/B` exchange. Fourteen have a negative inner coefficient, forming 12 distinct integer profiles; exact negative-cell order-ideal minimization over every finite staircase has minimum zero.
* **39,135,393** ordered Theorem 2 substitutions. Exact integer quadratic or first-difference minimization over every positive `k` has minimum twice-slack zero.

Both scans include effective-empty roles. Theorem 1's count is `sum_w binom(5,w) q_w(q_w+1)q_w^3/2`, and Theorem 2's count is `33^5`, where `q_w=2^(5-w)`. The earlier disjoint-only separator in the predecessor failed an overlapping source-Theorem-2 instance; that earlier warning remains correct for its different witness. The new vector above was separately checked against the stronger scopes.

## Evidence and limitations

* Vector `frontier-20261028-fivevar-family-separator-witness-v3.json` SHA-256 `c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842`.
* Independent point/85-Shannon verifier `frontier-20261028-fivevar-family-separator-v3-independent.py` SHA-256 `aeaa1a7e2b595ac65dac6c70b7421e8bbd52e288d459e0a917134adf610b378d`, receipt SHA-256 `85f5aa3792670298a1ae7db529a700f622ee8fb22264e425d01db15efdaa4286`; it also checks the disjoint families and rejects two mutations.
* `F_n` complete-subset producer receipt SHA-256 `54df78921d643e6c12af681fd3b1e62c2af90f717ca1677ff7d05ffd7c3dbbb3`; independent first-difference replay receipt SHA-256 `e61b244657bf26b3ce0dcdf3de62a22c1ea5d6c2ce0f20bc232be2b435d48dae`.
* Two 2026-family complete-overlap scanners: `frontier-20261028-fivevar-separator-v3-all-overlap-source.py` SHA-256 `3403a97fb1bfc48dc863e73cea4abf4f99d2fc77b6a0aedcb3a33e80d0625ccc`, receipt `85e2333ed704c47e46797c431904f72da84a8958e15a3653e65efcde4a3f2b3d`; independently structured `frontier-20261028-fivevar-separator-v3-all-overlap-source-independent.py` SHA-256 `bd5cd840416226ef266b960d9a723556b6abd60fbc9f7e9dd6ceb60658e5178a`, receipt `dc3ef05ec8b720f532e6167944e0cdc3ea99cb65a8bba246d9481815d49d21e6`. They use different loop/vectorization splits and quadratic versus first-difference / diagonal-cell minima.
* The 2026 publisher source and the theorem formulas are pinned in `frontier-20261028-five-variable-source-screen-v1.md` (SHA-256 `e8d1910e7cd2024b5a03c9cc6688fcf529ea3d75345b95033e3c801b1ec4e9cd`). Its source theorem proof and the present gluing proof have not been cross-model or proof-assistant reviewed.

The `Psi` original-graph disjoint-family scan remains an LP-only no-improvement result, not a proof that the source primal is a real entropy law. The original scientific target remains open.
