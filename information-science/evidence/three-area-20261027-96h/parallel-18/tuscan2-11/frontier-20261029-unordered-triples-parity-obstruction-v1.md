# An asymmetric obstruction from unordered triples and boundary parity

Owner **InfoRecursiveMDS18-2**, information-science slot **info-4**. Actual `/bin/date` before writing: **Thu Oct 29 13:53:14 PDT 2026**.

**NEW author-WRITTEN candidate, unreviewed.** This applies to **every** original unrestricted T2(11), including every asymmetric array. It is a conditional no-go for entire classes of actual candidate arrays, not a proof that every array is excluded and not a construction. Its only inputs are the original T1/T2 definitions and elementary finite graph/counting facts, all proved where used. No circular-extension theorem, f225 candidate/review, Z₃/Z₄ condition, held episode, solver, search, scientific program, arithmetic kernel, selected example, external source or model is an input. No formal/kernel, human, independent-model, novelty or parent-adoption claim.

## 1. Actual triple supports have multiplicity at most two

Let A be any T1(11) array on S, |S|=11: eleven permutation rows, with each directed adjacency a→b for a≠b occurring once. Its 99 consecutive **oriented triple events** are the windows (x_j,x_{j+1},x_{j+2}), for j=0,…,8 in each row. A support is the corresponding unordered 3-subset of S. Let μ(U) count triple events with support U.

**Lemma 1.** For every U, μ(U)≤2. If μ(U)=2, the two oriented events lie in different actual rows and have disjoint sets of directed adjacency arcs.

**Proof.** Consider two distinct triple events on the same support {a,b,c}. If they shared a directed arc x→y, uniqueness of that adjacency would put it in one actual row. They cannot use x→y in the same position of two different triple windows. If one used it as the first arc and the other as the second, that row would contain z,x,y,z with the third symbol z repeated, contrary to the row being a permutation. Hence their adjacency arc sets are disjoint.

Take one triple to be (a,b,c), whose arcs are ab,bc. The only other triples on {a,b,c} with disjoint arcs are (a,c,b), (b,a,c) and (c,b,a). The two still-unused arcs after adding each are, respectively, {ba,ca} (same target), {ca,cb} (same source), or {ac,ca} (a 2-cycle). None is a directed length-two path on three distinct vertices. A third triple is therefore impossible. Two distinct windows in one permutation row cannot have the same 3-support, because any later window introduces a vertex not present in the earlier one. ∎

Let H₁ be the set of supports occurring once and H₂ the set occurring twice. Then

|H₁|+2|H₂|=99.                                            (1)

In particular |H₁| is odd and at least one. The doubles H₂ are distinct 3-subsets, not assumed to be independent or edge-disjoint.

## 2. The boundary–missing graph as an actual triangle boundary

Now suppose A is **T2(11)**. Let M be the set of missing directed distance-two pairs; exactly 11 of the 110 directed pairs are missing. Define the multiset L of the 22 directed **boundary adjacencies**: the first adjacency and the last adjacency of each actual row. A directed adjacency appears at most once in L because it occurs in only one row and a length-11 row has different first and last arcs.

For an unordered pair {a,b}, let

l_ab = #{a→b,b→a} that belong to L,          0≤l_ab≤2,
m_ab = #{a→b,b→a} that belong to M,          0≤m_ab≤2.      (2)

Form the simple undirected graph Γ on S by including {a,b} exactly when l_ab+m_ab is odd. Equivalently, Γ is the mod-2 symmetric difference of the undirected boundary-adjacency multigraph and the undirected missing-pair multigraph.

**Theorem 2.** Γ is exactly the symmetric difference over F₂ of the three edges of every actual singleton triple U∈H₁. Consequently Γ is Eulerian and has an **odd** number of edges. In particular Γ is not bipartite and contains an odd cycle.

**Proof.** Fix {a,b}. Each directed adjacency a→b (and separately b→a) belongs to two consecutive triple windows if it is interior to its row, or one if it is the first or last arc. Thus these two directed adjacencies contribute 4−l_ab triple events containing {a,b} as an adjacent pair.

As an outer pair of a triple, {a,b} contributes 2−m_ab events: T2 allows each directed distance-two pair at most once, and m_ab counts the missing orientations. Every triple containing {a,b} uses it in exactly one of these two roles, so its total support multiplicity is

Σ_{U⊇{a,b}} μ(U) = 6−l_ab−m_ab.                           (3)

Reducing (3) modulo 2 removes all double supports and shows that Γ has edge {a,b} iff an odd number of H₁ triples contain it. So Γ is the F₂ sum of the triangles U∈H₁.

Each triangle has degree 2 at each of its vertices; hence every vertex of Γ has even degree. Also |E(Γ)|≡3|H₁|≡|H₁|≡99≡1 (mod 2). An even-degree finite graph decomposes into edge-disjoint cycles; if all cycles were even, it would have an even number of edges. Thus Γ has an odd cycle and cannot be bipartite. ∎

**Direct exclusion test.** For any ACTUAL T1(11) candidate, construct its boundary multiset L and its missing distance-two set M from its rows. If the resulting Γ is bipartite, that candidate is **not** T2(11). This is a universal necessary condition: no row-symmetry or circulant hypothesis is imposed. Whether any particular T1(11) candidate has bipartite Γ is not claimed here.

## 3. A quantitative odd-girth constraint from the actual singleton supports

Let g_odd be the length of a shortest odd cycle of Γ. By Theorem 2 it exists, and 3≤g_odd≤11.

**Theorem 3.** Every actual T2(11) satisfies

|H₁| ≥ g_odd−2,          |H₂| ≤ (101−g_odd)/2.              (4)

**Proof.** Make an auxiliary graph whose vertices are the singleton supports U∈H₁, joining two supports when they share an unordered pair. In one connected component with t supports, order its triples along a spanning tree. The first uses three symbols; every later triple shares a pair with an earlier triple, so introduces at most one additional symbol. Hence all its triples together use at most t+2 symbols.

Different auxiliary components cannot contain the same unordered pair, so their triangle boundaries are edge-disjoint and their union is Γ. Since |E(Γ)| is odd, some component has a boundary with an odd number of edges. Its boundary graph has even degrees, so it contains an odd cycle of length at least g_odd. All vertices of that cycle occur among this component's symbols. Therefore g_odd≤t+2≤|H₁|+2. The bound on H₂ follows from (1). ∎

For example, triangle-free Γ forces |H₁|≥3 and |H₂|≤48; odd-girth 11 forces |H₁|≥9 and |H₂|≤45. These are **necessary actual-row conditions**, not assertions that any such graph or hypergraph is realizable.

## 4. A vertex-wise parity filter

For each symbol x, let s_x be its number of occurrences in the second column and p_x its number in the penultimate column. Each symbol is first once and last once. It appears in one triple when at either endpoint, two when second or penultimate, and three at the seven interior positions. Hence

#{U∈H₁:x∈U}+2#{U∈H₂:x∈U}=29−s_x−p_x.             (5)

In particular, every x with s_x+p_x even belongs to an odd, hence positive, number of singleton supports. Let K be the number of such x. Since Σ_x(s_x+p_x)=22, K is odd. Each singleton support contains three vertices, so

|H₁| ≥ the least odd integer ≥ ceil(K/3).                    (6)

For example, if both the second and penultimate columns happen to be permutations, K=11 and necessarily |H₁|≥5. This is a conditional implication for original arrays, not a claim that those columns must be permutations. Combine (4) and (6) by taking their maximum.

## 5. Exact residual and assurance

**WRITTEN:** multiplicity at most two for all T1(11) triple supports; the exact co-degree identity (3); the all-array T2(11) parity-graph and odd-cycle obstruction; and the actual-singleton-support bounds (4)–(6).

**NOT proved:** that every original T1(11) array has bipartite Γ, that any particular Γ or H₁/H₂ system satisfies all row-realization constraints, or that this obstruction excludes every asymmetric T2(11). No finite diagnostic was executed, and no conjectural parity pattern was promoted. The original T2(11) witness-or-universal-no-go question remains **OPEN**.
