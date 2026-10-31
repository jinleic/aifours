# Physical equalities and actual corrected-coordinate binding for d4

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 18:24:05 PDT 2026. This independently checks the **actual** d4 equality metadata, the physical factor order, common compression modules across the two signed marginal parts, and all 329 corrected lambda coordinates. It closes a physical-source dependency separate from the full identity and multiplier PSD; it is not parent, human/family, formal/Lean, or source-wide acceptance.

## 1. Written original-object equalities

The original same-pair lift has unit a,b and `Tr_H |a><a|=I_Q/2`, where V=H⊗Q. Let `Y31=|aaab><aaab|`, `Y22=|aabb><aabb|`, `Y13=|bbba><bbba|` on four **complete V replicas**.

- **Stiefel:** at any a-replica r, tracing H_r and applying the source's auxiliary contrast yields

  `2 Tr_(H_r)Y − I_(Q_r)⊗Tr_(V_r)Y = 0`.

  Indeed the relevant factors are `2(I_Q/2)` and `I_Q·||a||²`; all other replicas are spectators. The three actual groups use slot0 of Y31, slot0 of Y22, and slot3 of Y13, all a slots. The prior exact local-basis audit independently checked the source's dual auxiliary operator `2V_p−I_slot⊗Tr_slot(V_p)` and all 648 used equality compression/permutation contractions.

- **aab:** delete replica2 from Y31 and Y22, and keep `(0,1,3)` in each. The deleted a or b is unit, so both yield the SAME physical `|aab><aab|` in the SAME order.
- **abb:** delete replica1 from Y22, keeping `(0,2,3)`, and from Y13, keeping **`(3,0,2)`**. Both give the SAME physical `|abb><abb|`; the differing physical order is indispensable.

These equalities hold for the original arbitrary complex same-pair vectors, including rank-one/degenerate C, and are preserved by the **same** local twirl, site symmetrization and conjugation. Their components may be contracted by any common fixed matrices; coefficient signs on the final exact zero relations are unrestricted.

## 2. Every actual equality group and corrected coordinate

The independent checker `frontier-20261028-d4-physical-equality-source-check.py`, SHA256 `077737ece6d3953daee00187ef4ea203046d97aab59d0dd86211b72e87f94e6f`, reads the hash-pinned actual source data and corrected rational data through the pinned owner source parser, without executing author `ep3core.py` or the author verifier. It derives each family's letter word, deleted slot, surviving order, sign and actual compressed dimensions; all four local specifications must refer to the **same whole-replica slot/order**.

Critically, for each of the two marginal groups it also checks the two parts have the **same actual compression module keys at all four factors**, not merely the same dimensions. With the same physical surviving operator and identical compression, each paired compressed coordinate really is the same; shape equality alone would not prove that fact. The resulting equality-coordinate axis lengths—sums of squared module-column counts, not individual matrix dimensions—are `(6,6,6,5)` for both marginal groups and `(6,6,6,14)` for each Stiefel group. All 329 corrected lambda index tuples were checked against **every** associated signed part, not only the first:

| Group | Corrected lambda coordinates | Physical binding |
|---|---:|---|
| stiefel31 | 104 | family31, a slot0 |
| stiefel22 | 106 | family22, a slot0 |
| stiefel13 | 15 | family13, a slot3 |
| aab | 51 | `aaab` del2 order013 vs `aabb` del2 order013; same actual modules |
| abb | 53 | `aabb` del1 order023 vs `bbba` del1 order302; same actual modules |

Actual `python3 frontier-20261028-d4-physical-equality-source-check.py` returned **PASS in 0.292 s**, no invalid lambda coordinates. Receipt SHA256 `608f6453b9e05b8303fe09a4b561e71371f6a8eaa325fe04f3f2e5fbe5707e85`. Four deliberate in-memory faults were detected: wrong abb order, Stiefel applied to a b slot, equal rather than opposite marginal signs, and an out-of-range lambda coordinate.

## 3. Equal-shape compression is not enough: actual fault control

The separate `frontier-20261028-d4-equality-compression-fault-check.py`, SHA256 `83bdd36805d5009a2a1809d778b79f44379e5bf3d5eac126ac93d33a322df86c`, replaced one actual abb auxiliary compression in memory with a **synthetic different 8×1 matrix of the same shape**. The binding check rejected it specifically because the two marginal parts no longer used the same modules; result SHA256 `3d17aad6deecd637eba6f796f778c79c66f6118f1a83a6a68d7bc4604d299150`, **PASS**. This is a guard-sensitivity test, not a physical counterexample. Exact equality of the actual module keys is stronger than necessary if two differently keyed modules happen to be mathematically identical, but the actual data satisfy it, so no such equivalence assumption is needed.

Chronology: the first attempted construction looked for a *different already-present* auxiliary module of the same shape for the actual abb key and found none; it exited without a result. The final separate test used the explicitly synthetic same-shape mutation above and detected the intended mismatch. Neither attempt changed source or corrected data.

## 4. Remaining dependencies

The written physical equalities above are supported by the actual data binding and the separately run literal local-value checks, but they do not themselves prove the complete corrected functional identity, source-span coverage, positivity of the 1237 saved multipliers, the original partial-trace objective, or q3. Those remain the separately pinned complete Gram bridge, finite commutant/canonical orbit, global exact/CRT, saved-data PSD and original-lift evidence. This does not validate `gram2` or other dimensions, the source's all-d theorem, physical distillability, new priority, formal/human/family review or parent adoption. Historical held material is not a premise.
