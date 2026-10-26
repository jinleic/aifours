# Unrestricted endpoint-cut defect theorem and a six-triple orbit obstruction v1

Clock actually observed before creation: **2026-10-23T15:15:32-0700**. Status **CANDIDATE / WRITTEN ONLY / PARTIAL FOR T2(11) / NOVELTY_UNCLEAR**. This continues the unrestricted written defect line. It does not assume a group-developed source, target Latin columns, a1-factor missing graph, or one-point deletion from a12×12 Tuscan-2 source.

The full T2(11) target is not solved. The new conclusions concern all add-zero/cutting orbits and an explicit published Tuscan-1(11) input. They are not an unrestricted nonexistence proof. No solver, CNF generator, scientific arithmetic program or executable certificate check ran. Native operations used here were source download/OCR and metadata only.

## 1. Primary source and exact objects

The source access gap for the original cutting methods has been closed by opening the author's own PDFs:

- Etzion–Golomb–Taylor, *Tuscan-K squares*, Advances in Applied Mathematics10(1989),164–174: [author PDF](https://etzion.net.technion.ac.il/files/2016/02/P12.pdf), retained SHA-256 `72473afe80e20df799a171d12c7a550a443b43234d08cc6e22b0df0a1f315ea9`. OCR/source images for pp.164–165 and170–174 were read. Its Q1 concerns circular Tuscan-2 arrays and Q2 the broader odd Tuscan-2 squares. These are not equivalent questions.
- Etzion, *Hamiltonian decomposition of K_n^*, patterns with distinct differences, and Tuscan squares*, Discrete Mathematics91(1991),259–276: [author PDF](https://etzion.net.technion.ac.il/files/2016/02/P17.pdf), retained SHA-256 `7583bd2c67d6577a125462301b734dd3969c6d51f4c425b6f7c1270f58346a64`. Definitions, Cutting Method, Add Zero Transformation, and Example2 on printed p.265 were read. The actual p.265 image was opened, not trusted solely to OCR.

The primary Add Zero Transformation adjoins a new common symbol to each row, cyclically shifts each augmented row to put some common symbol first, then removes that common symbol. The cutting constructions and the existence of Tuscan-1(11) are classical. This manuscript claims no novelty for those ingredients. The bounded-fault descriptions below are reconstructed in writing; their priority is not certified.

Let Ω have N=n+1 symbols, N≥4. Let C consist of N−1 directed Hamilton cycles on Ω in which each ordered pair of distinct symbols is an edge exactly once. Equivalently it is a circular Tuscan-1 array of shape `(N−1)×N`.

For t∈Ω, cut every cycle at t and delete t, without joining its two neighbors: the remaining row starts just after t and ends just before it. Denote this linear n×n array by B_t. It is always Tuscan-1: every finite adjacent pair not involving t survives exactly once. The question is which t make B_t Tuscan-2.

For an ordered pair a≠b in Ω define

`W_(a,b)={c∈Ω\{a,b}: some cycle contains the consecutive triple (a,c,b)}`,

and `μ_(a,b)=|W_(a,b)|`.

There cannot be two occurrences with the same center c, because that would repeat the circular edge a→c. Thus W is a set, not a multiset disguised as one.

## 2. Exact root-intersection theorem

For every pair with μ≥2 define a fault set

`F_(a,b)={a,b}∪W_(a,b)` if μ=2,

`F_(a,b)={a,b}` if μ≥3.

No set is imposed when μ≤1.

**Theorem1.** The complete set of t for which B_t is Tuscan-2 is exactly

`V = intersection_(a≠b, μ_(a,b)≥2) F_(a,b)`,

with the empty intersection interpreted as Ω.

*Proof.* If t=a or t=b, the ordered pair does not belong to the remaining alphabet and imposes no condition. Otherwise an occurrence `(a,c,b)` survives as a linear distance2 event exactly when c≠t. Cutting at t creates no new distance2 event and removes at most the one occurrence centered at t. Hence the remaining multiplicity is exactly

`μ_(a,b)−1_(t∈W_(a,b))`.

For μ≤1 it is automatically≤1; for μ=2 it is≤1 exactly when t∈W; for μ≥3 it cannot be≤1 unless t is an endpoint. Intersect over the pairs. All retained rows are permutations and adjacency is already complete, so this is also sufficient. ∎

**Corollary2 (root-count gap).** Either every one of the N roots works, or at most4 work. If any μ≥3, at most2 work. In particular **five good add-zero roots force all N roots to be good** when N≥5.

*Proof.* If there is a fault, its set has size≤4, and if it is a high-multiplicity fault its set has size2. If there is no fault, every root works. ∎

**Corollary3 (bounded failure certificate).** If no root works, this can be certified by at most five ordered-pair fault constraints. If a μ≥3 fault is available, at most three suffice.

*Proof.* Start with one fault set F of size at most4. Since the full intersection is empty, for each t∈F choose one further fault excluding t. Those at most1+|F| constraints already have empty intersection. Starting from a2-element high-fault set improves the bound to3. A μ=2 constraint is supported by two distinct-center triples; a high fault is supported by any three distinct-center triples. For a failure certificate these witness triples suffice—no assertion about unlisted multiplicities is needed. ∎

In particular, two high faults with disjoint endpoint sets already rule out every root using only **six explicit triples**. Three high faults forming a triangle of endpoint pairs also suffice, even though their endpoint sets intersect pairwise.

## 3. Full relation to the unrestricted missing-distance2 graph

Now suppose a particular B_t actually is Tuscan-2 on X=Ω\{t}. Let M be its0/1 missing-distance2 matrix. Let E be the permutation matrix of the ordered closing arcs `(last symbol of a row, first symbol of that row)`. Starts and ends are each permutations, so E has one1 per row and column and no diagonal1.

For finite a,b∈X,

`μ_(a,b) = 1−M_(a,b)+E_(a,b)`.  (1)

Indeed the ordinary distance2 events give `1−M`, while the only additional circular distance2 event on finite endpoints is the path `last→t→first`, exactly E.

For pairs involving the added root,

`μ_(t,b)=#{rows with second symbol b}`,

`μ_(a,t)=#{rows with penultimate symbol a}`.  (2)

These multiplicities may exceed1; they are not silently replaced by Latin-column assumptions.

**Corollary4.** For a known good root t, all N roots work if and only if **M=E**. If M≠E, at most4 roots work (including t).

*Proof.* With no circular faults every μ equals1: there are N(N−1) circular distance2 events, equal to the number of ordered distinct pairs. Equation(1) then gives M=E. Conversely M=E gives μ=1 on finite pairs. The degree identities for M make each second/penultimate multiplicity1, so(2) gives μ=1 on the other pairs as well. The root-count gap applies if M≠E. ∎

Thus a generic Tuscan-2 square is NOT automatically a circular Tuscan-2 array; that stronger condition is precisely M=E after adjoining a root. The older circular-array→orthogonal-Latin-square theorem cannot be applied to an arbitrary Tuscan-2 square without this bridge.

A useful sharper consequence of(2): if two different symbols occur at least three times in the second column, t is the **only** good root. The same holds for two high penultimate multiplicities, or one high second and one high penultimate multiplicity at distinct symbols. For any alternative finite root, the relevant high-fault endpoint sets `{t,b}` would have to share that finite root.

### Add-zero iteration is not a larger hidden search space

Starting with B_t and adjoining a fresh common symbol recovers exactly the same circular cycles C, with t renamed as the fresh symbol. Therefore any finite sequence of Add Zero Transformations merely chooses another root of C up to symbol relabeling. Row permutations and global reversal do not change whether a good root exists. The root-intersection theorem controls the entire add-zero equivalence orbit, not just a one-step test.

## 4. Exact characterization of Tuscan-1-preserving row rotations

A second unrestricted endpoint fact bounds a different move. Let A be ANY Tuscan-1 square of order n≥3, with its rows kept labeled. Close each row into a directed n-cycle D_r. Write e_r for its closing arc `(last,first)`. These n arcs are distinct. In the original A, e_r occurs as an ordinary adjacent edge in exactly one other row f(r); necessarily f(r)≠r.

Consider arbitrary independent cyclic rotations of the rows, without reversing their directions. Such a rotation is determined by which edge q_r of D_r is cut.

**Theorem5.** The rotations retain the Tuscan-1 property exactly when the choices are obtained by selecting a union S of directed cycles of the functional graph `r↦f(r)`:

- if r∉S, cut its original closing edge e_r;
- if r∈S, transfer the cut of e_r to its original occurrence in row f(r).

There are exactly `2^c` labeled cut states, where c is the number of directed cycles of f. Since f has no fixed point, `c≤floor(n/2)`. In particular a Tuscan-1(11) square has **at most32** such labeled rotations, not11^11 independent feasible choices. Different states may become equivalent after row/symbol relabeling; no inequivalent-class count is claimed.

*Proof.* A nonclosing arc appears in exactly one D_r, so cutting it would destroy coverage; every cut must be a member of `{e_r}`. Each e_r appears twice among the closed cycles, once as its own added closing edge and once in row f(r). Exactly one occurrence must be cut. Let S comprise those r whose original occurrence in row f(r), rather than own closing occurrence, is cut. The number of cuts received by row k is

`1_(k∉S)+#{r∈S:f(r)=k}`.

It must equal1. Thus f maps S into S and has exactly one predecessor in S for every point of S. On this finite set f is a permutation, so S is a union of its directed cycles; no tree vertex can be selected. Conversely any such union gives exactly one cut per row and per closing arc. Each cut determines the linear row uniquely. ∎

The set of closing arcs remains E after every such Tuscan-1-preserving rotation. Distance2 is not automatic. If `B_r(q)` is the two-element set of cyclic distance2 events crossing cut q in D_r, then changing from original cut e_r to q removes the events in `B_r(q)\B_r(e_r)` from the old linear array and adds those in `B_r(e_r)\B_r(q)`. For an originally Tuscan-2 square, the new square is Tuscan-2 exactly when all added events are distinct and disjoint from the surviving old events. Equivalently its signed defect vector is the original defect plus the boundary-change vector and has only0/1 entries. This couples endpoint moves to actual distance2 events; a degree-feasible missing graph alone is insufficient.

## 5. Concrete primary order11 input and its written authentication

The exact Example2 array from Etzion1991 p.265 is retained as

`sources/etzion-example2-tuscan1-11.table`, SHA-256 **`a50fc2994053f669973f91b61ed64824d30afe390527e74d62e9e6beee6f1a20`**.

The printed star is relabeled0; printed1through10 keep their values. Rows1through11 are in their printed order. This is an old **Tuscan-1** square, not a new T2 witness. The actual image `sources/etzion-P17-middle-07.png` was opened to authenticate every row used below.

Here is also a self-contained written binding of the input to the classical construction, rather than trusting an OCR table as a theorem. Over F11, the multiplication rows `(a,2a,...,10a)` for a=1,...,10 cover every ordered distinct nonzero pair once: its row is a=v−u and its column is k=u/a, which is neither0 nor10. Shifting each row to the column order `(6,7,8,9,10,1,2,3,4,5)` removes all pairs `(5a,6a)` and adds `(10a,a)`. Both collections enumerate all ordered opposite pairs once, so Tuscan-1 coverage is retained. Adjoin star0 and close each row; its first/last-column permutations supply all arcs to/from0, giving a Hamilton-cycle decomposition on11 symbols.

The source's shift pattern is

`P=(0,8,9,7,10,6,1,5,2,4,3)`.

Its ten edges belong respectively to source rows

`5,1,9,3,7,6,4,8,2,10`.

For the finite edges, the row is their nonzero difference modulo11; `0→8` belongs to row5. These are ten different rows. Cutting one such edge in each cycle gives ten paths; adding P as the eleventh path restores precisely the removed edges. This proves the displayed array's Tuscan-1 property in writing. All of this is classical baseline reconstruction, not a new construction claimed by this round.

## 6. Entire published add-zero orbit excluded by six triples

Adjoin the new symbol **11** (distinct from the source's0/star) and close each row of the published A. In these twelve-symbol cycles, the following six triples occur:

| Ordered endpoints | Three distinct centers | Literal triples and source rows |
|---|---|---|
|11→2|10,6,3|`(11,10,2)` in row3; `(11,6,2)` in row7; `(11,3,2)` in row10|
|1→5|3,6,11|`(1,3,5)` in row2; `(1,6,5)` in row5; `(1,11,5)` across the end/start of row4|

The first three are visible because those rows start `(10,2)`, `(6,2)` and `(3,2)`. The last circular triple uses row4's last symbol1 and first symbol5. The centers are distinct in each row of the certificate.

Both endpoint pairs have circular distance2 multiplicity at least3. Any root yielding T2 would therefore have to belong to both `{11,2}` and `{1,5}`, which are disjoint. **No root works.** This excludes the entire iterated Add Zero orbit of the published Example2, with a six-triple certificate and no exhaustive search.

This is not a claim that the published example was intended to solve T2(11). It is a precise obstruction to trying to obtain a new T2(11) from that explicit Tuscan-1 input by its classical orbit operation.

## 7. The only nontrivial Tuscan-1-preserving rotation also fails

For the published A, its closing arcs in row order are

`8→9, 2→4, 7→10, 1→5, 0→8, 6→1, 10→6, 5→2, 9→7, 4→3, 3→0`.

The first ten all occur in the eleventh row P. The last arc3→0 occurs in row5. Thus

`f(r)=11 for1≤r≤10`, and `f(11)=5`.

The only directed cycle is `(5,11)`. Theorem5 leaves exactly two labeled Tuscan-1 rotation states. The nontrivial state changes only

`row5 → (0,8,2,7,1,6,5,10,4,9,3)`,

`row11 → (8,9,7,10,6,1,5,2,4,3,0)`.

The same six triples in §6 still occur: rows3,7,10,2,4 are unchanged, and the internal triple `(1,6,5)` remains in the rotated row5. Hence this second state also has no good add-zero root.

Consequently no T2(11) can be obtained by **one arbitrary Tuscan-1-preserving batch of row rotations of this particular published array, followed by any finite number of Add Zero Transformations, row/symbol relabelings and global reversals**. Arbitrary alternation of new row-rotation batches at other add-zero roots is NOT covered; neither are other Tuscan-1 inputs. Those exclusions must not be silently expanded.

## 8. Calibration, feasibility and remaining mathematical ingredient

The T2(4) array already expanded in `unrestricted-defect-interface-v1.md` has missing arcs exactly equal to its four closing arcs. Corollary4 therefore gives all five good roots, agreeing with the classical circular order5 construction. This is a written positive calibration; no program has replayed it.

The new useful unrestricted constraints are the exact local fault-intersection criterion, the5-fault failure certificate, the five-good-roots rigidity threshold, and the at-most32 Tuscan-1 rotation states at11. They still act on one circular/path decomposition at a time. A full negative answer would require a reason **every** Hamilton-cycle decomposition of K12^* has empty good-root intersection; a full positive answer would require one decomposition with a nonempty intersection and the resulting literal121 entries. Neither is established here.

The stage1 encoding request is **PREPARE / NOT_ADMITTED / NOT_RUN**, as directed by the parent. Small CNF generation or hashing is not evidence that a47k-variable solver run can settle this instance in the remaining window. No such feasibility assertion is made. The present packet supplies actual written structural exclusions rather than counting protocol construction as a scientific result. Separate parent and actual in-harness reconstruction are pending, and priority remains unclear.
