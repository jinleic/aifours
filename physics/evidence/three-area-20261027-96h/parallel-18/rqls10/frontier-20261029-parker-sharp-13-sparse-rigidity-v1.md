# Parker resolution: a sharp 13-ray bound for globally two-sparse arrays

**WRITTEN + EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:34:47 PDT 2026**. This solves a strict structural subproblem for ONE fixed resolution; it does not settle unrestricted 1RQLS10.

## Claim

For the literal Parker resolution L in `frontier-20261028-parker-13ray-result-v1.json` SHA **0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5**, every 1-resolvable QLS10 that is globally support≤2 in SOME common orthonormal basis has at most **13 distinct rays**. The bound is attained by the exact 13-ray witness `frontier-20261028-exact-switch-grow-result-v1.json` SHA **2023d098dc9c81b437b698601ed8709161794b7434934f83abc2f4219a6dcb6e**.

Moreover, there is an uncomputed positive neighborhood of the entire set of classical arrays with this L in which every exact resolved QLS has at most13 rays, with NO sparsity assumption in that local statement.

## 1. All classical mates: exact graph dichotomy

The all-mates census `frontier-20261029-parker-all-mates-no-disjoint-pair-switches-v1.md` SHA **0386f669eb8f8e53db0acea8c6255f7761e5b5425f15b06ce290aed1a80ac5a5** enumerates all1272 L-transversals, all311214 disjoint pairs, and all162 pairs whose three-context two-color graph is disconnected. Every graph has components of 6 and14 cells. No two disconnected pairs on four mutually disjoint transversals exist. Any two compatible disconnected edges sharing one transversal form a triangle, and all24 compatible triangles have their short components in the SAME 3×3 block, rows7–9/columns7–9.

New exact-cover certificates show the remaining extension facts:

- Each of the **126** disconnected pairs outside this core cannot extend to any classical orthogonal mate.
- Each of the **36** core pairs can extend, but EVERY extension contains a third core transversal forming the triangle. Concrete completions for all36 are included.

`frontier-20261029-parker-trade-extendibility-v1.py` SHA **c05d1398cad2828cfffb9850d32e08cd5ffc23d64aceb453d8afc24bd6665ce4**, result SHA **8f842a9bea5aa79ab62116274a9e4252dcd7e64bb754d3406cea2b55d574b229**, writes all completion-failure trees and core witnesses. `frontier-20261029-parker-trade-extendibility-replay-v1.py` SHA **71d8540ea00f296cef5fcb115b43151c8e53cc1ab3307b3f4bd831d937be0950**, result SHA **4cdbcba92d331610a060ccc3cabc7f6c56d97d7e433e7e346e3cff6939d31cd0**, independently uses the DSU transversal census and replays all **29370** literal failure-tree nodes and all36 mate witnesses. Thus every classical mate A has either no disconnected pair graph, or EXACTLY the three pair graphs of its core three colors; a fourth edge would be disjoint from one edge of the triangle, which the exhaustive census forbids.

## 2. Local classification at EVERY classical mate

If all pair graphs are connected, the local rigidity theorem `frontier-20261028-classical-rigidity-and-search-v1.md` SHA **3dc1eea8fdb47c04c39dea1d0a8a85122680db29b3d8c3fdea6c7ce05f712f24** gives only classical arrays locally.

Otherwise there are exactly three disconnected pair graphs, each with two components. Gauge the first row to the standard basis and fix each other cell's phase by a positive reference-color coordinate. The standard linearized pair-graph equations then give one free complex variable for the short component of each core color pair and no other free variables: the first-row component is fixed by the gauge. Thus the exact real tangent space has dimension6. Independently, applying an arbitrary U(3) only to the nine block cells preserves all30 bases; modulo its three local column phases this is a genuine smooth 6-real-dimensional family, and its tangent supplies those six directions.

Select a maximal independent set of the original real-analytic constraint equations. The implicit function theorem gives a 6-dimensional local manifold containing every feasible gauge-fixed array. The 6-dimensional explicit block family has the same tangent, so the inverse function theorem makes it locally open in that manifold. Hence every feasible array near this classical mate is in that embedded-U(3) family: it has at most the ten exterior color rays plus three block rays, i.e. **at most13**. This is the same nonlinear argument as in the independently checked specific-seed local theorem `frontier-20261028-parker13-local-completeness-v1.md`; here the graph census extends the conclusion to EVERY classical mate.

The finite union of all classical U(10)×cell-phase orbits for this fixed L is compact. A finite subcover of these local neighborhoods supplies a uniform positive (uncomputed) epsilon near that entire classical set, proving the local statement.

## 3. Global two-sparse bound and sharpness

Given any globally 2-sparse resolved QLS with L, the analytic classicalization path in `frontier-20261029-sparse-resolution-classicalization-rigidity-v1.md` SHA **e08ae1bc19c3ea8d4c9a4c49a12120a08c671fb6408a9ad6ca9bd6d36c1b0823** connects it through exact resolved QLSs to a classical mate A. For small positive parameter, §2 puts the path in A's local rigid or embedded-U3 family. The projective minors asserting that all exterior occurrences of each A-color are equal rays, and that each core block color's three occurrences are equal rays, therefore vanish on an open parameter interval. They are real analytic along the path, hence vanish all the way to the original array. Thus its rays form at most ten exterior classes plus three core classes. In the rigid case all ten A-color classes persist and the array is classical. The conclusion is global ONLY under the 2-sparse hypothesis.

The exact 13-ray witness is 2-sparse after a change of basis in the original core span. In terms of its original core basis e7,e8,e9, set

`f7=(4e7-3e8)/5`, `f8=(3e7+4e8)/5`, `f9=e9`.

Its three new rays are `f7`, `(3f8-4f9)/5`, `(4f8+3f9)/5` (up to phases); the three exterior core rays e7,e8,e9 have support at most2 in the f basis. All other exterior rays are unchanged basis vectors. Hence the previously checked actual 13-ray array attains the bound while satisfying global 2-sparsity.

The census, exact-cover trees, tangent dimension, IFT family argument, analytic-continuation caller, witness basis change and source transcription require independent full review. This is not formal verification, external-model review or a novelty claim; nonsparse solutions and other resolution L remain open.
