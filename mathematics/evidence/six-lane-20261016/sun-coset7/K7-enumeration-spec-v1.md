# K7-enumeration-spec-v1: the reduced-data enumeration for K7 and its lift-soundness obligation (specification only)

- **Freeze record:** host-clock time and sha256 in `evidence/k7-enumeration-spec-v1.sha256`.
- **Scope:** this is a specification. It contains no counts, no code and no executed script. It authorises no run: any implementation and any execution need a parent GO.
- **Status:** unreviewed. K7 stays OPEN.
- **Premises (none is accepted yet):**
  - `K7-structure-v1.md` (f4534c07…9fc1): K7-TRI, K7-U, K7-TWIN, K7-Q, K7-Q5 and K7-COV. It is under both-family review, in packet `review/sun-coset7-k7-structure-review-v1`.
  - Optionally `K7-block-lemma-v1.md` (93c3cd1f…29db3): K7-BLOCK, which is unreviewed. It is used **only** in the conditional pruning layer of §5. The base specification does not depend on it.
  - The rules: rules-k7-v1, rules-k7-addendum-v1, rules-k7-erratum-v1; certificate formats CERT-FORMAT-k7-v1 and CERT-FORMAT-k7-addendum-v1.

## 1. The reduced datum D

A reduced datum D = (Mk, Π, Q, A, N) has five components.

**1.1 Marking data Mk.** Mk is a set partition π of a marker set P ⊆ {2, 3, 5}.
- Each part of π is the marker set of one marked vertex, so |M| = |π| ∈ {0,1,2,3}.
- Each marked vertex z also carries capped excesses: ε_2(z) ∈ {1,2,3} if 2 is in its part, ε_3(z) = 1 if 3 is, and ε_5(z) ∈ {1,2} if 5 is.
- Its capped profile is (1 + ε_2, 1 + ε_3, ε_5), with absent markers read as 0. Under the caps (4,2,2) this means e ∈ {2,3,4}, f = 2 and g ∈ {1,2} for the respective markers.
- Every unmarked vertex has profile (1,1,0).
- **Vertex order:** marked vertices first, ordered by the smallest marker in their part; then U.

**1.2 Twin partition Π.**
- **Allowed sizes:** an integer partition (s_1 ≥ s_2 ≥ … ≥ s_b) of |U| = 7 − |M|, with every s_i ≥ 1.
- **Placement:** blocks are labelled 1..b in this order and occupy consecutive vertex positions in U.

**1.3 Quotient data Q.** Q is exactly one of the following, so that every pattern falls into exactly one family.
- **Q24:** a map β from block pairs {i, i′} (i < i′) to {2, 4}. It includes the all-2 map and the case b = 1, where there are no pairs.
- **Q23:** a set partition of {1..b} into **at least two** 2-classes, with β = 2 inside a class and β = 3 between classes. The all-2 case belongs to Q24.
- **Q5:** allowed only when |U| = 4 and |M| = 3, by K7-Q5. Then every s_i = 1 (b = 4) and β ≡ 5. With |M| = 3 and P = {2,3,5}, π is necessarily the partition into singletons.

**1.4 Marked rows A.** For each z ∈ M and each block i, a_{z,i} ∈ {1,…,5}, with a_{z,i} ≤ 4 whenever s_i ≥ 2 (by K7-TWIN(c)).

**1.5 Marked–marked values N.** α_{zz′} ∈ {1,…,5} for every pair z ≠ z′ in M.

## 2. The lift L(D): a full 7-vertex K7 pattern

- **Profiles:** as in 1.1.
- **Gcds:** g_xy = 6 for all pairs.
- **α values:**

| pair | α_xy |
|---|---|
| x, y in the same block | 1 |
| x ∈ block i, y ∈ block i′, i ≠ i′ | β(i, i′) |
| z ∈ M, x ∈ block i | a_{z,i} |
| z, z′ ∈ M | α_{zz′} |

- **Admissibility check:** L(D) is a pattern of the K7 universe, i.e. every profile is admissible and every capped pairwise gcd equals 6. An implementation **must** recheck this by recomputing gcds from profiles; it may not assume it.

## 3. Lift-soundness obligation (mandatory)

**3.1 What a closure needs.** A datum D is CLOSED only by a certificate valid **on L(D) itself**, using one of these rules, applied to the full 7-vertex pattern with the d-relaxed quantities of K7-TRI. Equivalently, the general formulas of rules-k7-v1 with the K7 profiles.
- **T:** any of the 35 triangles of L(D), including triangles inside U.
- **K:** L2/L3 with K1, at any vertex.
- **VFC:** Corollary VFC-count at any vertex, for every admissible q.
- **P:** Ppair or PB.
- **RPLP-k7:** rules-k7-addendum-v1 §A1 with erratum W2, at any vertex, for every admissible q.

The certificate formats are CERT-FORMAT-k7-v1 §3 with CERT-FORMAT-k7-addendum-v1, in exact rationals.

**3.2 What is never allowed.** No rule may be evaluated on the quotient, the block structure or the reduced datum in place of L(D). FH is UNUSED. No rule outside 3.1 may close a datum without a new frozen text and a parent GO.

**3.3 Survivors.** A datum whose lift survives every rule is a SURVIVOR. It is listed exactly, as D together with L(D) in canonical form. It is not a counterexample.

**3.4 Partial pruning.** The enumeration may be organised as a tree over the components of D, for example Mk, then Π, then Q, then A, then N. It may prune a partial datum only under the deletion conditions of CERT-FORMAT-k7-v1 §2:
- T: only on triangles all of whose three α values are already fixed;
- VFC: only on the fixed edges of a star, with every admissible q refuted;
- K: only for sets S whose pairs and apex edges are all fixed.

The prune certificate must name the fixed sub-pattern it uses.

## 4. Symmetry: orbit representatives

**The group.** The stabiliser of the lifted profile tuple is Sym(U) × {id_M}, because distinct marked vertices have distinct marker sets. Two data D and D′ give equivalent lifts iff there is a size-preserving bijection σ of blocks with all three of:
- β′(σi, σi′) = β(i, i′), or the corresponding 2-class partition for Q23;
- a′_{z,σi} = a_{z,i};
- N′ = N.

**What an implementation must do.**
1. Enumerate at least one datum per such orbit. Every orbit must be represented.
2. Either (a) evaluate duplicates as well, or (b) deduplicate by an **exact** canonical form. The reference choice is the lexicographically smallest α-code of L(D), in a fixed edge order, over all permutations of U, as in CERT-FORMAT-k7-v1 §2.
3. A checker recomputes canonical forms itself.

**Orbit coverage.** Orbit coverage itself must be argued or replayed. The reference argument: enumerate all labelled data (all block labellings consistent with the non-increasing sizes, all Q, A, N), then deduplicate by the exact canonical form of the lift.

## 5. Conditional pruning layer (only if K7-BLOCK is accepted; otherwise ignore this section)

If the parent accepts K7-BLOCK, an implementation may additionally skip:
- every Π with some s_i ≥ 4;
- every Π with some s_i = 3 when M = ∅;
- for a block i with s_i = 3, every Q with β(i, i′) = 4 for some i′ ≠ i (K7-BLOCK(b) applied to unmarked outside vertices);
- for a block i with s_i = 3, every A with a_{z,i} = 4 for some z ∈ M (K7-BLOCK(b) applied to marked outside vertices).

Each skip must be recorded with the clause of K7-BLOCK used. A run that uses this layer has K7-BLOCK as an additional premise of any conclusion.

## 6. Coverage statement (what a successful run would show)

**Hypotheses.**
- (i) The premises of the header are accepted.
- (ii) Every orbit of §4 is represented.
- (iii) Every represented datum is CLOSED by a certificate valid under §3.
- (iv) An independently written checker replays (ii) and (iii) from definitions.

**Conclusion.** Under these hypotheses, no K7 configuration exists in any group. The reason: by K7-COV, every K7 configuration has a pattern equal to L(D) for some datum D in the domain of §1. Its Q5 restriction rests on K7-Q5, which uses VFC.

If the §5 layer is used, K7-BLOCK joins the premises.

A run that stops early, or that leaves survivors, is UNKNOWN for K7, with the exact list of unclosed orbits. It is never a partial exclusion of K7 as a whole.

## 7. Required outputs of a future run (none produced here)

- The generation parameters.
- The list of orbit representatives, as canonical lift codes.
- For each representative, the rule, the witness and the vertex, or SURVIVE.
- The prune certificates for any partial-tree closures.
- A run record (status, stop reason, completed-datum frontier) under the guard and launcher conventions then authorised.
