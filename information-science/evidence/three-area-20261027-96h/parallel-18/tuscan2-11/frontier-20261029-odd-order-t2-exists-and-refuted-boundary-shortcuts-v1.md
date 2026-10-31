# An odd-order Tuscan-2 square exists (n = 21); consequences for the T2(11) programme

Owner **InfoRecursiveMDS18-2**, info-4. Native clock before writing: **Thu Oct 29 08:05:07 PDT 2026**.

**Scope.** This is an exact verification of a published object plus exact recomputation on explicit squares. It is not a T2(11) witness or no-go, it is not novelty (the order-21 square is Ollis's), and it is not a formal, kernel or independent-model check. Inputs used:

- the public paper M. A. Ollis, *Terraces for small groups*, arXiv:1603.01496, §3;
- my earlier pinned explicit squares;
- the pinned general checker.

The f175 candidates (symbol asymmetry, orbit divisibility) are under review and are **not** used. No f161/f162 material was opened.

## 1. The verified object

Ollis prints a directed T₂-terrace for the non-abelian group of order 21, G₂₁,₁. Its 21 words in u, v are recorded verbatim in `frontier-20261029-ollis-g21-t2-square-v1.json`, field `terrace_text_as_transcribed`. He states "Hence there is a Roman-2 square of order 21".

I read the words as u^i v^j, with u⁷ = v³ = e. The two possible laws gave different results:

- with v u v⁻¹ = u⁴ (so v^j u^k = u^(k·4^j) v^j), the sequence is a directed T₂-terrace;
- with v u v⁻¹ = u², the same words give repeated distance-1 and distance-2 pairs, so they are not a terrace.

Following Ollis's construction, the (i,j) entry of the square is a_i⁻¹a_j.

The resulting 21×21 array is saved as `frontier-20261029-ollis-g21-t2-square-v1.json`, SHA-256 `4f20ab9ae5c125bf13cdcc9b847d2ee040dac6e29ac9e14a32c5bfd158fb7c3c`. Two independent checks were run on it:

- **Owner kernel (integer counts):**
  - every row is a permutation;
  - all 420 ordered pairs occur exactly once at distance 1;
  - all 399 distance-2 pairs are distinct;
  - the columns are also permutations, so the array is Latin.
- **Pinned general checker** `frontier-20261028-general-t2-check-v1.py` (SHA `a534f304686eeae097c824ee4ff90c202b6260b02d4c8caf5a55f558acb760e0`), which reads only the `rows` field:
  - reports `is_tuscan_k_square: true` and `distance_one_complete: true` for k = 2;
  - receipt `frontier-20261029-ollis-g21-t2-check-v1.json`, SHA `419cfbab18c6126dbccc6f0ed5a87af8ecbf1441a2bd717ed85f1358de1ee218`.

**So a linear Tuscan-2 square of odd order exists (n = 21).** In my earlier source-status note, the 1990 Golomb–Etzion–Taylor sentence "none known for odd n > 1" was carried forward. That sentence is outdated as a statement of current knowledge. The Handbook table entry n = 9: "?" was not checked here.

## 2. A tempting boundary lemma is false

For T1 arrays, E denotes the endpoint permutation (first symbol of a row ↦ last symbol of that row). E is always fixed-point-free.

I recomputed eight explicit even-order squares:

- the pinned T2(4) and T2(6);
- the six normalized T2(8) arrays in `frontier-20261028-channel-n8-enumeration.json`.

In all eight, E is a fixed-point-free involution (cycle types 2², 2³, 2⁴). If every T2(n) had E² = id, no T2(n) of odd order could exist, because a fixed-point-free involution needs an even number of points.

**The order-21 square refutes this lemma: its E has cycle type 7·7·7.**

Several other boundary coincidences are also not general laws. "Yes" means the property holds in that square.

| property | n=4 | n=6 | n=8 (6 arrays) | n=21 |
|---|---|---|---|---|
| E² = id | yes | yes | yes | **no** |
| second and penultimate columns are permutations | yes | yes | no | yes |
| closing pairs (last, first) = missing D2 pairs M | yes | yes | no | yes |
| M = {(penultimate, second) of the same row} | yes | yes | 2 of 6 | yes |
| boundary matrix B = M (canonical Latin completion) | no | no | 2 of 6 | no |

The per-array data are in `frontier-20261029-small-and-odd-t2-profiles-v1.json`, SHA `2d78d16d047f415fe4c50902a7a6e1c1e1fe9df7460203eced192082be011316`. These are exact facts about these explicit arrays only. I make no completeness claim about any list; the n = 8 enumeration's final UNSAT remains unverified.

## 3. What this means for T2(11)

1. **Parity of n is not an obstruction.** Any T2(11) no-go must use more than "n odd". In particular, it cannot come from E² = id or from a forced circular extension.
2. **The group route stops at prime n.** The order-21 square comes from a group of order 21. For n = 11 the only group is Z₁₁, which is abelian of odd order and has no sequencing. So that route cannot give T2(11).
3. **n mod 4 is an open question, not a theorem.** Order 21 is ≡ 1 (mod 4). The sources read here show no T2 of order ≡ 3 (mod 4): orders 3 and 7 have none, and order 11 is listed as open by CPro1. My actual-row routing identity, ∏_b sign(σ_b) = (−1)^{n(n+1)/2} sign(E), has a sign that depends on n mod 4. But it holds for **every** T1 array, so it is not an obstruction by itself.
4. **Negative calibration.** A bounded randomized backtracking (40 restarts × 200,000 nodes, 54 s in the owner kernel) did **not** find a directed T₂-terrace in G₂₁. Naive group search is therefore weak. This result is recorded as UNKNOWN and is not used.

## 4. Remaining gap

The unrestricted linear T2(11) remains **OPEN**: there is no witness and no universal contradiction. This packet removes four false shortcuts and corrects the odd-order existence status. It supplies no new necessary condition at order 11.
