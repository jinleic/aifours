# Squared-cycle defect circulation: an all-array bridge and a sharp free-Z₃ dichotomy

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 13:42:25 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** Sections 1–3 apply to every unrestricted T2(11), including every asymmetric one. Sections 4–6 apply to any actual free cyclic Z₂ or Z₃ symmetry of its circular extension, without assuming that the full automorphism group is cyclic or that the extension is 2-perfect. Inputs: the literal T1/T2 definitions and elementary finite counting, permutations, group actions and modular arithmetic only. The relevant Z₃ collision bound is re-proved below. No Z₄ argument, old computation/UNKNOWN, f187 material, held episode, external source, arithmetic kernel, solver, scientific program or model is an input. No formal/kernel, human, independent-model, novelty or parent-adoption claim.

## 1. Actual rows and their circular successor matrices

Let A be any T2(11): eleven permutation rows on S={0,…,10}, with all 110 directed distance-one events and all 99 directed distance-two events distinct. Set V=S∪{∞}. In every T1 array each symbol is first in exactly one row and last in exactly one row, by incoming/outgoing adjacency counting. Write the first-to-last permutation as E; it has no fixed point.

Insert ∞ between the end and beginning of each actual row, making eleven directed Hamiltonian 12-cycles. Let P_i be the permutation matrix of the successor map of cycle i, with rows indexed by sources and columns by targets. Then

Σ_i P_i = J−I.                                             (1)

In particular these are actual Hamiltonian permutations, not independently selected row/column marginals. Let

B = Σ_i P_i²,            W = B−(J−I).                       (2)

Each P_i² is also a permutation matrix. Thus B has every row and column sum 11; its diagonal is zero because the square of a 12-cycle fixes no point. Hence W is integer-valued, diagonal zero, with every row and column sum zero, and every W_xy≥−1. The entry B_xy counts the actual cyclic two-step events from x to y, including events through ∞.

## 2. Exact cut-boundary formula, without symmetry

Let M be the set of missing linear distance-two pairs in S×S. It has 11 elements, all off diagonal. Let C={(last(R),first(R)): R an actual row}; C also has 11 distinct off-diagonal pairs, since first and last symbols separately permute S. Put

p_x=#{rows with x penultimate},    s_x=#{rows with x second},
z_p=#{x:p_x=0},                   z_s=#{x:s_x=0},
δ=|C\M|=|M\C|.                                            (3)

For x,y∈S, x≠y, the cyclic two-step events split into the linear events and the closing pairs. For x∈S, the events x→∞ are counted by p_x and the events ∞→x by s_x. Therefore the **entire** W matrix is

W_xy = 1_C(x,y)−1_M(x,y)       (x,y∈S, x≠y),
W_x∞ = p_x−1,                  W_∞x = s_x−1,                 (4)
W_xx = W_∞∞ = 0.

Define the total cyclic two-step excess F=Σ_{x≠y} max(B_xy−1,0). Since Σ_x p_x=Σ_x s_x=11, their total excesses are z_p and z_s, respectively. Formula (4) gives the **exact actual-row identity**

F = δ+z_p+z_s.                                             (5)

The number of cyclic ordered pairs absent altogether is also F: B has 132 events on 132 ordered pairs. Moreover z_p≤δ and z_s≤δ. For example, p_x=0 means no missing linear pair has source x, while the unique pair of C with source x necessarily lies in C\M; the s argument is the target analogue.

In particular, the earlier three-looking circular-completion requirements collapse to one **equivalence**:

C=M  ⇔  F=0  ⇔  the circular extension is 2-perfect.        (6)

When C=M, the missing-pair graph has one outgoing and one incoming edge at each symbol because C is a permutation graph, so the second and penultimate columns are automatically permutations. No circular completion is assumed for a general T2(11).

## 3. A signed bipartite circulation for the asymmetric case

Form a bipartite directed multigraph with a source copy R_x and a target copy C_y of each x,y∈V. For W_xy<0 draw −W_xy edges R_x→C_y; for W_xy>0 draw W_xy edges C_y→R_x. Row and column sums zero make this multigraph balanced at every vertex. Positive and negative supports are disjoint, so it has no directed 2-cycle. Every nonempty balanced finite directed multigraph decomposes into directed cycles, each now of length at least four.

Consequently for **every** original T2(11), with or without an automorphism,

F=0  or  F≥2.                                               (7)

If F=2, the whole signed support is exactly one directed four-cycle: two unit surplus cells and two unit missing cells form the opposite corners of a 2×2 rectangle. This is an actual square-of-successors circulation, not the earlier B-versus-M Latin-completion condition; no label symmetry, column Latin property or selected support pattern is required. Conversely, such a rectangle satisfying only zero margins is not asserted to be realizable by Hamiltonian cycles.

Also, if δ=1, write M=C−{(a,b)}+{(c,d)} with the two pairs distinct. The row/column margins imply z_p=1 exactly when a≠c, and z_s=1 exactly when b≠d. At least one changes, so (5) gives F∈{2,3}. This is useful below and makes no claim that δ=1 occurs in a real T2 array.

## 4. Orbit-type jump conservation for free Z₂ and Z₃

Suppose a cyclic group ⟨g⟩ of order q∈{2,3} preserves the actual D and acts freely on V. Put r=12/q and label V=Z_q×{0,…,r−1}, with g(t,a)=(t+1,a) and ∞=(0,0). The pair type of ((t,a),(t+d,b)) is λ=(a,b,d), omitting (a,a,0). It represents q concrete ordered pairs. Because D is g-invariant, all pairs of one type have the same two-step multiplicity μ_λ; write w_λ=μ_λ−1.

At every actual vertex exactly eleven two-step events start and eleven end. Subtracting the baseline of one for each of its eleven possible targets/sources yields the **type-layer balances**

Σ_{b,d} w_(a,b,d)=0,       Σ_{a,d} w_(a,b,d)=0.            (8)

Let S be the sum of the increments d over every pair type. For q=2,r=6 and q=3,r=4,

S=r²·q(q−1)/2 ≡0 (mod q).                                  (9)

To compare distances, take one g-orbit of cycles. If its cycle stabilizer has order s, the first L=12/s positions are a period up to a group translation: x_{j+L}=g^t x_j. The successive coordinate jumps d_j are therefore L-periodic, and its two-step jumps sum to twice its one-step jumps modulo q. The L period representatives account for the **full multiplicity** of each D2 type in that cycle orbit, even when D2 types repeat; the D1 types, across all cycle orbits, occur exactly once. Summing gives

Σ_λ μ_λ d_λ = 2S,       hence  Σ_λ w_λ d_λ = S = 0 (mod q). (10)

Let P=Σ_λ max(w_λ,0). Because the number of two-step events equals the number of directed pairs, P also counts missing types and F=qP. If P=1, there is one type of surplus +1 and one of deficit −1. The two balances (8) force them to have the same source and target layers; (10) forces the same increment d. They would therefore be the same type, impossible. Thus

**P=0 or P≥2** for either free Z₂ or free Z₃.             (11)

For q=2 this already improves (7): F is either zero or at least four. Combining (5), (11), and the δ=1 observation in §3 shows that **δ≠1** for any such free-involution extension: δ=1 would give F=2 or 3, whereas F is even and not 2. The Z₂ class remains open.

## 5. Free Z₃: prove at most two surplus types

Let O={∞,g∞,g²∞}. Every cut at a point of O is isomorphic to the original T2 cut. Therefore for any two distinct cyclic two-step events with the same ordered endpoints, O lies in the union of their four vertices.

No three consecutive vertices of a cycle can all lie in O. Such a triple has the form (x,g^a x,g^(2a)x), a=1 or 2. Translating it by g^a gives a second triple sharing its second directed arc and forcing the unique cycle containing that arc to close after three vertices, impossible for a Hamiltonian 12-cycle.

Thus repeated two-step pairs have exactly one endpoint in O; their two distinct middles are the other two O-points, and their multiplicity is exactly two. For a fixed source x∈O, two different repeated targets would force the unique arc x→gx to have two successors. Hence at most one repeated **type** goes O→V\O. The predecessor argument gives at most one repeated type V\O→O. Accordingly P≤2. With (11),

P∈{0,2},    F=3P∈{0,6}.                                   (12)

This is a new restriction on the entire actual cycle system: the previously allowed scalar excess 3 cannot occur. It does not assert that either remaining value is realizable.

## 6. Exact original-row dichotomy for the free Z₃ class

A repeated type O→V\O contains three concrete repeated ordered pairs: one starts at ∞, and the other two have both endpoints in S. Therefore it contributes one repeated second-column symbol and two members of C\M. Similarly a repeated type V\O→O contributes one repeated penultimate-column symbol and two members of C\M. By §5 there is at most one of each, so (12) gives exactly two alternatives:

**Perfect branch.** F=0; p_x=s_x=1 for every x, δ=0 and C=M. The circular extension is 2-perfect.

**Six-defect branch.** F=6; there is exactly one repeated type in each crossing orientation; δ=4 and |C∩M|=7. In the penultimate column there is exactly one symbol of multiplicity two, exactly one omitted symbol and nine symbols of multiplicity one. The same holds independently for the second column. Both doubled symbols lie outside O.

There is an additional exact arrangement constraint in the six-defect branch. Let the two repeated types be (0,A,d₊) and (B,0,e₊), where A,B are nonzero layer labels. There are exactly two missing types, since positive and negative type deviations have the same total 2. Their source-layer multiset is {0,B}, and their target-layer multiset is {A,0}, by (8). Therefore their ordered layer pairs are either

- **crossing:** (0,A) and (B,0); or
- **switched:** (0,0) and (B,A).                              (13)

In both cases their two increments must sum to d₊+e₊ modulo 3 by (10). In the crossing case each missing type differs in increment from the repeated type on the same ordered layer pair; the two increment changes are opposites. The omitted penultimate and second symbols are both outside O, each in the same g-orbit as the doubled symbol in its own column. In the switched case the missing (0,0,d), d≠0, gives the omitted penultimate and second symbols as the two **different** points of O\{∞}. In particular, one omitted symbol cannot lie inside O while the other lies outside.

All of these restrictions are necessary for **every** original T2(11) whose extension admits the stated free Z₃ action. None is a construction or a blanket exclusion of that class.

## 7. Exact remaining gap

The matrix identity and circulation (1)–(7) apply equally to asymmetric arrays. The Z₂ gap (11) and Z₃ perfect/six-defect dichotomy (12)–(13) leave real unresolved branches: no proof here forces or forbids a 2-perfect extension, the six-defect boundary pattern, a free involution, an order-six group, or a completely asymmetric extension. No Hamiltonian family satisfying any branch is constructed. **T2(11) remains OPEN.** No earlier Z₄ timeout is used or reclassified.
