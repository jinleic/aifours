# Where symmetry can still hide in a T2(11): automorphisms of the circular extension act freely

Owner **InfoRecursiveMDS18-2**, info-4. Native clock before writing: **Thu Oct 29 08:17:49 PDT 2026**.

**NEW author-WRITTEN candidate, unreviewed.** All arguments are written and quantified over every unrestricted linear T2(11) array. No computation is used. The only lemma needed is re-proved inline (§1), so the f175 review is not treated as returned. One step (§3, case |H| = 12) cites my earlier circular-regular packet. That citation is conditional: the packet is author-written, and its returned review required the corrections in its erratum. No formal, independent-model or novelty claim is made.

## 0. Setting: every T1(11) is a vertex-deletion of a Hamiltonian decomposition of K₁₂*

Let A be any T1(11) array on the symbol set S, |S| = 11. Its rows are R_s = (s, x₁, …, x₁₀), indexed by first symbol. Add a new vertex ∞ and put V = S ∪ {∞}. Each row becomes the directed Hamiltonian cycle C_s = (∞, s, x₁, …, x₁₀) on V.

The eleven cycles D = {C_s} use every ordered pair of distinct vertices of V exactly once:

- pairs inside S, by the T1 property;
- the pair (∞, s), in C_s only;
- the pair (x, ∞), in the unique row ending in x.

So D is a Hamiltonian decomposition of the complete digraph K₁₂*.

Conversely, take any Hamiltonian decomposition D of K₁₂* (eleven directed Hamiltonian cycles) and any vertex u. Cutting every cycle at u gives a T1(11) array A_u on V∖{u}: the row of a cycle C is C read from the vertex after u.

**Automorphisms.** An automorphism of D is a permutation h of V that maps every cycle of D, with its direction, to a cycle of D. Since h(D) = D, the map h sends each row of A_u position-wise to a row of A_{h(u)}. So A_u ≅ A_{h(u)}.

## 1. Lemma (T1 asymmetry at prime order, proved here)

For an odd prime p, the only permutation g of the symbols of a T1(p) array that maps every row to a row is the identity.

*Proof.* Suppose g ≠ id. Some power h of g has prime order ℓ.

- If h maps some row R to itself, then h fixes every symbol of R. Every symbol lies in R, so h = id, a contradiction.
- So ⟨h⟩ acts freely on the p rows, and ℓ divides p. Hence ℓ = p, h is a p-cycle on the symbols, and the rows form one orbit R, hR, …, h^{p−1}R.

Label the symbols by Z/p so that h acts as +1. For a nonzero e, the p arcs (x, x+e) each occur exactly once. The orbit of R contributes p·k(e) of them, where k(e) is the number of adjacent differences of R equal to e. So k(e) = 1 for every e ≠ 0.

The p−1 adjacent differences of R are then all the nonzero residues, and their sum is 0 mod p. Telescoping, the same sum equals last(R) − first(R) ≠ 0. This is a contradiction. ∎

## 2. Theorem A: every automorphism of D is fixed-point-free

Let p be an odd prime and D any Hamiltonian decomposition of K_{p+1}*. Then every nontrivial automorphism of D fixes no vertex. So Aut(D) acts freely on the p+1 vertices, and |Aut(D)| divides p+1.

*Proof.* Let h ∈ Aut(D) fix a vertex u. By §0, h maps the rows of A_u, cut at h(u) = u, position-wise to rows of A_u. So h restricted to V∖{u} is a symbol automorphism of the T1(p) array A_u. By §1 it is the identity, so h = id. A free action splits V into orbits of size |Aut(D)|. ∎

For p = 11 this says: **every automorphism group of a Hamiltonian decomposition of K₁₂* has order 1, 2, 3, 4, 6 or 12, and acts without fixed points.** This holds for every decomposition, not only those coming from T2(11).

## 3. Theorem B: what a symmetric extension of a T2(11) must look like

Let A be a T2(11) with circular extension D, as in §0 with ∞. Put H = Aut(D) and let O = H·∞ be the orbit of ∞, so |O| = |H|.

A *2-step event* of D is a consecutive triple (x, y, z) in a cycle of D. Two distinct events with the same ordered ends (x, z) have different middles y ≠ y': equal middles would repeat the arc x→y. Call such a pair a *coincidence*.

1. **Every image is again T2.** For every h ∈ H, A_{h(∞)} ≅ A is a T2(11).
2. **Coincidences contain the whole orbit.** For every coincidence {(x,y,z), (x,y',z)}, the set O lies inside {x, y, y', z}.

   *Proof.* Fix u ∈ O. The events of D that avoid u are exactly the distance-2 events of A_u. If both events of the coincidence avoided u, A_u would repeat the distance-2 pair (x, z), contradicting item 1. So u ∈ {x, y, y', z} for every u ∈ O. ∎
3. **Five or more automorphisms force 2-perfection.** If |H| ≥ 5, D has no coincidence at all, because |{x,y,y',z}| ≤ 4. Then every ordered pair occurs exactly once at cyclic distance 1 and exactly once at cyclic distance 2. That is, D is a circular Tuscan-2 11×12 array: 132 events on 132 ordered pairs.

   By Theorem A this happens only for |H| ∈ {6, 12}. For |H| = 12 the action is regular. A regular action is excluded by `frontier-20261028-circular-regular-obstruction-v1.md` (SHA `72af4fbaec5ac9bfd019327373ce0a7ced5e8d36f4c6dcba23feec1c92e76026`) as corrected by its erratum (SHA `6e64aa10ef915a0475cf06324761b4db074fc9789ff9fcd3bee93f577b981c2c`, odd n ≥ 3, p = 2 transfer step). This exclusion is conditional on that packet.
4. **Cases |H| ∈ {2, 3, 4}.** D need not be 2-perfect, but every coincidence lies on a vertex set containing the whole orbit O, of size 2, 3 or 4. For |H| = 4 each coincidence has vertex set exactly O.

## 4. Consequences for the T2(11) programme

By §1, A itself has no symbol symmetry. In contrast, every explicit T2 square examined in this round has nontrivial symbol automorphisms: orders 4, 6 and 8 by `frontier-20261028-small-t2-symmetry-check-v1.json`, and order 21 through its group G₂₁. So the symmetric patterns behind those examples cannot occur in a T2(11). Theorems A and B show the only remaining way to use symmetry: an automorphism group of the 12-point extension D that **moves ∞** and acts freely. The possibilities are exactly:

| \|Aut(D)\| | structure of D | status |
|---|---|---|
| 1 | general | the unrestricted problem |
| 2, 3, 4 | coincidences confined to vertex sets containing the orbit of ∞ | new symmetric classes; not 2-perfect in general; never searched in this round |
| 6 | 2-perfect circular array with a free group (Z₆ or S₃) on 12 points | open |
| 12 | 2-perfect with a regular group | excluded, conditionally (§3, item 3) |

**Comparison with earlier bounded runs.** Earlier unverified SAT runs required full 2-perfection with a fixed-point-free involution or element of order 3. They do not cover the classes |Aut(D)| ∈ {2, 3, 4} with coincidences. Those runs are not inputs here.

## 5. Remaining gap

These are necessary conditions and a classification of where symmetry can occur. No case except |H| = 12 is excluded, and no T2(11) is constructed. The unrestricted T2(11) problem remains **OPEN**. A bounded search in the classes |Aut(D)| ∈ {2, 3} would be a natural next computation, but it needs a frozen request and parent authorization. None was started.
