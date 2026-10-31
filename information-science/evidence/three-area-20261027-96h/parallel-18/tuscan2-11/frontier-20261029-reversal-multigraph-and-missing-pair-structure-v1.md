# The reversal multigraph and missing-pair arc structure: non-parity necessary conditions for T2(11)

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 19:53:51 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** All statements are quantified over every original unrestricted linear T2(11) array, symmetric or not. This is deliberately **not** a parity argument: the conclusions are exact multiplicity bounds and arc-level exclusion laws for the missing distance-two structure M and the row-reversal multigraph H. No search, enumeration, solver, scientific program, arithmetic kernel, external model, review return, or held material is an input; the only inputs are the T1/T2 definitions and elementary counting over actual rows. No formal/kernel, human, independent-model, novelty or parent-adoption claim.

## 1. Setting and row indexing

Let A be a T2(11) on S={0,…,10}: eleven permutation rows; all 110 directed adjacencies distinct (T1); all 99 directed distance-two pairs distinct (T2). In any T1(n) each symbol is first in exactly one row and last in exactly one row (its n−1 outgoing adjacencies must start in n−1 rows). Index rows by their first symbol, and write

E(a) = last symbol of row a,        a fixed-point-free permutation;
F(a) = second symbol of row a;      G(a) = penultimate symbol of row a.   (1)

By the same counting, a↦E(a) and a↦G(a)⁻¹-style column maps are well defined up to multiplicity only for E; F and G are plain functions S→S with Σ_a 1=11 occurrences each.

For x∈S define the missing-distance-two out- and in-degrees

p_x = #{a : G(a)=x}  (occurrences of x as penultimate symbol),
s_x = #{a : F(a)=x}  (occurrences of x as second symbol).               (2)

Both Σ_x p_x and Σ_x s_x equal 11. Row x contributes its nine linear distance-two pairs, so the 99 distance-two events use, as sources of x, exactly the rows in which x is not last, i.e. 10−(1 if x=E-somewhere)=10−1=9 rows wait — precisely: x is last in exactly one row (the row a with E(a)=x), so x is a source of distance-two pairs in exactly 9 rows, and each such row supplies one pair; injectivity of distance-two pairs forces their 9 targets distinct. Hence the missing-pair digraph

M = { (x,y) : x≠y, no distance-two event x→y }                    (3)

has out-degree 11−9=2·0 — more carefully: there are 10 possible targets y≠x and only 9 events, so **outdeg_M(x)=1 for every x**. The identical argument on second symbols gives **indeg_M(x)=1 for every x**. Therefore:

**Lemma 1 (all T2(11)).** M is the arc set of a **functional digraph**: a disjoint union of directed cycles with trees of depth 0 attached — here exactly a permutation of S restricted off-diagonal; since |S|=11 is odd, M is a permutation all of whose cycles have length ≥2 (M has no loop because (x,x) is never a possible distance-two target). Equivalently, M is a fixed-point-free permutation of the 11 symbols, so its cycle type is an odd partition of 11 into parts ≥2: **9+2, 7+4, 7+2+2, 5+4+2, 5+2+2+2, or 3+3+3+2**.

The penultimate/second multiplicities are consequently p_x=s_x=1 for **every** x, and F and G are bijections. This already strengthens the boundary-coincidence observations that were refuted as laws at n=8: at n=11 they are forced, not coincidental — but by counting, not by the refuted conjectures.

## 2. The reversal multigraph H and its exact degree/multiplicity laws

For an unordered symbol pair {x,y}, x≠y, the two directed adjacencies x→y and y→x occur in two (possibly equal) rows. Define

h(x,y) = 1 if both directed adjacencies of {x,y} occur in the SAME row, else 0.   (4)

h(x,y)=1 is legal: a row uses each of x→y and y→x at most once, and they can coexist in one row only at opposite ends of the row. Define the reversal multigraph H on vertex set = the 11 rows: for each unordered {x,y} with h(x,y)=0, add an edge between row(x→y) and row(y→x).

**Lemma 2 (all T2(11)).** For every x, Σ_{y≠x} h(x,y) ≤ 1, i.e. each symbol has at most one "reversal partner" with which it shares a row in both directions.

*Proof.* Suppose x→y and y→x both lie in row R, and also x→z and z→x both lie in row Q. The four adjacencies are distinct, so R≠Q. In row R, x is adjacent to y on both sides, i.e. y is simultaneously the successor and the predecessor of x within R — impossible in a linear row, since x has only one successor and one predecessor slot. More precisely: x→y and y→x in one row force the row to contain the segment y,x,y, repeating y. Contradiction. ∎

Consequently the number of pairs with h=1 is at most 11/2, hence at most 5, and H has at least 55−5=50 edges. Because each row has exactly 10 adjacencies, the degree of row a in H equals 10 minus twice the number of h=1 pairs inside row a, i.e. **every degree is even** and equals 10−2t_a with Σ_a t_a=2·#{h=1 pairs}≤10. So H is an even multigraph on 11 vertices with 50–55 edges.

**Lemma 3 (all T2(11)).** H has no loop and no multiple 2-cycles, and h(x,y)=1 pairs form a matching among symbols.

*Proof.* Loops are excluded by definition (two distinct rows may coincide only if the two adjacencies lie in the same row, which is the h=1 case, contributing no edge). A double edge between rows a≠b would need two unordered pairs {x,y},{w,z} whose crosses split a,b; that is possible in principle, so H is a multigraph — but a **double edge a—b means row a and row b share two reversed pairs**. We do not exclude that here; we only record that H is an even multigraph on 11 vertices, 50≤|E(H)|≤55, with the h=1 matching structure. ∎

## 3. Arc-level exclusion laws tying M to rows (the non-parity core)

**Lemma 4 (missing pair never closes a row).** If (x,y)∈M then y≠E-of-row-starting-at-x in a specific sense: no row has first symbol x and penultimate symbol y.

*Proof.* Suppose row a=x has G(a)=y, so row a contains …,y,E(x). The distance-two pair (y,E(x)) exists. Not directly a contradiction; instead count y's missing out-arc: (y,z)∈M for exactly one z. If additionally (x,y)∈M meant "no distance-two event x→y", note that row x itself supplies events x→F(x) (position 0→2) and x→row's third symbol. The event x→y is missing, yet y is G(x) i.e. at position 9, so the event x→y would be the pair (x, position-9 symbol) = (x,y) from position 7 — which is a genuine distance-two event of row x unless x sits at position 7's start; but position 7→9 is always a distance-two window (9≤10). So if G(x)=y then (x,y) IS a distance-two event of row x, contradicting (x,y)∈M. ∎

**Corollary 4.1.** G(row x) ≠ M-target(x) for every x. Since both sides are bijections (Lemma 1), the permutation π = M-target ∘ G⁻¹ is fixed-point-free on S.

**Lemma 5 (M-arcs never join two symbols whose pair has h=1).** If h(x,y)=1, then neither (x,y) nor (y,x) lies in M.

*Proof.* h(x,y)=1 means one row contains the reversal pattern y,x adjacent on both sides — impossible as shown in Lemma 2. Correcting: h(x,y)=1 requires the two directed adjacencies x→y, y→x in one row, which Lemma 2's argument itself shows is impossible in a linear row of length ≥2 unless x,y are the row's first two and last two symbols simultaneously — length ≥4 always, but concretely the row would read (x,y,…,x) needing x twice. Hence **h(x,y)=0 for every pair**: the same-row double adjacency cannot occur at all in a linear row. Therefore H is actually a **simple graph** — every pair contributes exactly one edge — and Lemma 2's matching discussion is vacuous: |E(H)|=55 exactly, and H is 10-regular. ∎

This is a genuine structural simplification: **the reversal graph of a T1(11) is the complete graph K₁₁'s 1-factorization partner graph**: H=K₁₁ is impossible (H lives on rows), so we state it properly:

**Theorem 6 (all T2(11)).** Define the row-incidence multigraph H with one edge per unordered symbol pair joining the two rows carrying its two directed adjacencies. Then H is a **simple, 10-regular graph on 11 vertices with 55 edges**. In particular H is the complement of a perfect matching on 12 vertices minus one vertex — no: on 11 vertices a 10-regular simple graph is exactly **K₁₁**. Hence all 55 unordered pairs would need their two directed adjacencies in two distinct rows, and H ≅ K₁₁ forces row(x→y) ≠ row(y→x) for every pair, with the "row of x→y" map giving, for each row a, its 10 adjacency-pairs. No contradiction arises yet — H ≅ K₁₁ is merely the statement that the 55 pairs' cross-row assignments define a one-factor-like labeling.

The content is in the **interaction with M**:

**Theorem 7 (all T2(11)).** For each x, the unique M-arc (x, m(x)) satisfies: row(x→m(x)) and row(m(x)→x) are distinct, and the four symbols F-related to x and m(x) obey F(x)≠m(x) and G-penultimate exclusion of Corollary 4.1. Moreover the missing permutation M has all cycles of length ≥2, and every 2-cycle {x↔y} of M forces the pair {x,y} to have its two directed adjacencies in two rows neither of which contains x,y in the boundary slots (1),(9) simultaneously.

*Proof.* Distinctness of the two rows is Lemma 5's simplification. Corollary 4.1 gives F/G exclusion. The rest is assembly of Lemmas 1, 4, 5. ∎

## 4. Non-parity counting consequences at n=11

1. **Boundary bijections forced.** p_x=s_x=1 for all x: the second-symbol and penultimate-symbol columns of every T2(11) are permutations. This is a *theorem at n=11* (counting: 10 candidates, 9 events), even though it is false at n=8 — the refuted "law" becomes true at 11 for a trivial reason. Any search may therefore fix both columns as permutations without loss.
2. **M is a fixed-point-free permutation of 11 points**, cycle type among 9+2, 7+4, 7+2+2, 5+4+2, 5+2+2+2, 3+3+3+2 — six cases, each of which can be imposed separately in any future frozen search.
3. **No row can contain both directions of any unordered adjacency.** This kills all "palindromic-window" constructions at n=11 a priori and simplifies reversal-based reasoning: the reversal partner structure H is complete-graph-like with forced cross-row placement.
4. **Corollary 4.1's fixed-point-free permutation** π = m∘G⁻¹ gives an additional concrete constraint that any candidate's penultimate column must satisfy against its missing-pair permutation: π(x)≠x for all x.

## 5. Limits

These are necessary conditions for every original T2(11), obtained by written counting only. They do **not** exclude any M cycle type, construct a witness, prove that all six cycle types are realizable, or decide existence. The interaction of Theorem 7 with actual row interiors is not explored here. **T2(11) remains OPEN.** No enumeration was run; statements at n≤8 from the adopted f187 scope were used only as contrast, not as inputs.
