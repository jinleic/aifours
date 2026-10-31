# The mutual-M-to-endpoint bridge: E-2-cycle dictionary, cross-witness rectangles, and the exact open core

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Fri Oct 30 04:01:25 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** The bounded deliverable on the mutual-M-to-endpoint-cycle bridge, per Main's direction. It assumes no conjecture (in particular not k₀ ≤ #E-transpositions), uses no selected array and no computation of any kind. All statements are all-variable over every T2(11). Named import at its adopted scope: f292 disposition `info-4-tuscan-adjacency-row-closing-derangements-parent-v1.md` (SHA `72d60805…35c5`), items 1 and 3 (adjacency-row bridge; closing-pair derangement criterion, with ρ, ψ, π_c as defined there and re-derived where used). No formal/kernel, human, independent-model, novelty or parent-adoption claim.

## 1. Dictionary for E-2-cycles

Call {x,y} an **E-2-cycle** when E(y) = x and E(x) = y (rows x and y end with each other). Equivalently, both (x,y) and (y,x) are closing pairs.

**Theorem 1 (all T2(11)).** For an E-2-cycle {x,y}, put T = S∖{x,y} (nine symbols). Both closing-pair correspondences are permutations of the SAME set T:
- π_y = ψ_{x,y}|_T and π_x = ψ_{y,x}|_T.
Then:
- (x,y) ∈ M ⟺ π_y is a derangement of T;
- (y,x) ∈ M ⟺ π_x is a derangement of T;
- {x,y} is a **mutual** M-pair ⟺ **π_x and π_y are both derangements**.

*Proof.* Each direction is the adopted closing-pair criterion applied to the corresponding closing pair; both closing pairs of an E-2-cycle delete the same two symbols x,y from the domain/codomain. ∎

So mutual membership on an E-2-cycle is governed by a *pair of derangement conditions on one common nine-point set* — a genuinely two-sided object, unlike the single-π criterion for general closing pairs. Derangements of nine points exist in both signs and with varied cycle structure, so no local (correspondence-level) obstruction exists; realizability by an actual array is not addressed.

## 2. Cross-witness rectangles: the fixed points of the composite

**Theorem 2 (all T2(11)).** Let {x,y} be an E-2-cycle. For b ∈ T, (π_x∘π_y)(b) = b holds iff there exist a symbol b₁ ∈ T and two **distinct** rows R₁ ≠ R₂ such that

R₁ contains the adjacencies x→b and b₁→y;  R₂ contains y→b₁ and b→x.      (∗)

Consequently, when {x,y} is mutual, b₁ ≠ b automatically, and the fixed points of π_x∘π_y are exactly the first components of these **cross-witness rectangles**.

*Proof.* π_y(b) = b₁ means ρ(b₁,y) = ρ(x,b): the two adjacencies lie in one row R₁. π_x(b₁) = b means ρ(b,x) = ρ(y,b₁): row R₂. If R₁ = R₂, that row would contain both x→b and b→x, which forces x and b to occupy positions i = j+1 and j = i+1 simultaneously — impossible. The rest is composition. ∎

These rectangles are a new structural object binding the two directions of a mutual pair through the row layer; the number of them is the fixed-point count of a permutation composite, unconstrained by derangement-ness of the factors alone.

## 3. The exact open core of the conjecture

The conjecture k₀ ≤ #{E-2-cycles} decomposes exactly (no bound assumed):

k₀ = (mutual pairs lying on E-2-cycles) + (mutual pairs lying off E-2-cycles),

and the first summand is **trivially** ≤ #{E-2-cycles}, since an E-2-cycle carries at most one mutual pair — itself. Hence:

> the conjecture is **equivalent** to: *every mutual M-pair of a T2(11) is an E-2-cycle.*

What is proved here governs only the on-cycle case (Theorems 1–2). For the off-cycle case — a mutual pair {x,y} with E(x) ≠ y or E(y) ≠ x — the two correspondences ψ_{x,y}, ψ_{y,x} are fixed-point-free bijections between **different** (n−2)-subsets (the b₀/c₀ exchange of the adopted bridge), and correspondence theory alone permits every configuration: a fixed-point-free bijection between two 9-sets exists unless they are equal singletons. **No mechanism currently links mutual M-membership to E's cycle structure**; that is the precise gap. Pinned-square diagnostics (T2(4), T2(6): mutual pairs = E-2-cycles exactly, via M = C; T2(8), T2(21): k₀ = 0) are consistent with the conjecture but provenance-confounded and are not premises.

## 4. Residual

Theorems 1–2 are proved; the off-cycle core is open and stated as such. Nothing is realized or excluded — no branch, no boundary type, no mixed column case; the conjecture remains a conjecture. No witness, no no-go: **unrestricted T2(11) remains OPEN.**
