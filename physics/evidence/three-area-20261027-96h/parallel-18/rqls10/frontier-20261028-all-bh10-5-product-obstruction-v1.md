# No transversal in any Fourier10 × BH(10,5) product array

**NEW COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` before writing: **Wed Oct 28 18:19:37 PDT 2026**. The written normalization/physical caller and the complete finite certificate below together give an exact ALL-BH(10,5), ALL-L obstruction for one NONuniform construction family. Independent reviewer replay and mathematical review are required before adoption. This is NOT an unrestricted QLS10 no-go, not a classification of BH matrices, and not a novelty claim.

## 1. Theorem and precise target scope

Let zeta10 be a primitive tenth root, and let K be **ANY** 10×10 complex Hadamard matrix whose entries are fifth roots of unity, or become fifth roots after arbitrary row/column phase gauges. Define 100 ACTUAL vectors

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`, for r,c,t∈Z10.        (1)

Allow arbitrary common unitary, cell phases, and row/column relabellings. **Claim:** this array has NO orthogonal transversal, so it has NO 1-resolution by ANY Latin incidence L. No maximal-cardinality or uniform-overlap assumption is required. The statement ranges over ALL K in BH(10,5), not just the previously checked published B10 or its equivalence class.

The proof is a finite exhaustive argument on a superset of possible half-frames, with a replayable individual no-matching certificate for every eligible half-frame. It does NOT cover K with other phase orders, an arbitrary complex Hadamard K, a different product formula, or an arbitrary 1-resolvable QLS10.

## 2. Why any transversal forces a five-column-pair matching

The columns of K are orthogonal with squared norm10. In the actual product array (1), each column is a Fourier ONB and each row is a K ONB. Given ANY putative transversal, pair its cells in opposite rows `r,r+5`. Because the transversal meets every physical column once, these five row pairs partition the TEN distinct K-column labels into five disjoint pairs.

Let E be the five K-row indices occupying even Fourier-coordinate positions; its complement O occupies odd positions. For any paired physical columns c,d, set

`S_E(c,d)=sum_(t in E) conjugate(K_(t,c))K_(t,d)`, and similarly S_O.

K-column orthogonality gives `S_E+S_O=0`; orthogonality of the two opposite-row physical vectors gives `S_E-S_O=0`. Hence `S_E=0`. Arbitrary K row phases cancel and column phases factor out, so the condition is invariant under phase gauges. E may be ANY 5-subset of K rows because an arbitrary K row permutation may be present.

For fifth roots, a sum of five such roots is zero iff each root occurs exactly once: the degree-at-most4 integer count polynomial must be a multiple of `Phi5=1+X+X²+X³+X⁴`, with total coefficient sum5. Thus define Gamma_E on the ten K columns by joining c,d iff their FIVE phase differences across E contain each residue0,...,4 exactly once. The putative transversal forces **a perfect matching** of Gamma_E. Proving no possible BH K/E has such a matching is a sufficient obstruction; no claim is made that an arbitrary matching would satisfy the other transversal inner products.

## 3. Exhaustive normalized BH half-frame reduction

Given ANY BH(10,5) K and ANY candidate E, choose an arbitrary row of E as the first row and another row of E as the second. Fifth-root row/column phase multiplications dephase the first row and first column to zero exponents. They preserve all half-graph zero tests (row phases cancel and column phases are common factors). The second row is orthogonal to the first, so among its ten entries every residue appears exactly twice. Its first entry is0; permuting the other nine columns puts it in the canonical form

`second=(0,0,1,1,2,2,3,3,4,4)`.

Column permutation only relabels Gamma_E. This normalization is WLOG for EVERY pair (K,E), not an ansatz or a restriction to the published B10.

Every other dephased row starts with0, has every residue twice (orthogonal to the zero first row), and is also balanced in its pointwise difference with `second`. The remaining9 positions are a permutation of the multiset `{0,1,1,2,2,3,3,4,4}`, giving exactly

`9!/(2!)^4 = 22680`

candidate rows before the second-row filter. Independent complete generation gives exactly1075 after the filter. Put an edge between two candidates when their pointwise difference is balanced, i.e. when the two corresponding fifth-root rows are orthogonal. The resulting graph has26715 edges.

A possible E contains the first row, `second`, and ANY THREE mutually compatible candidate rows: an unordered triangle of this graph. Moreover the other FIVE rows of the putative full BH matrix must be five DISTINCT candidates adjacent to all three selected rows. Therefore any extendible E is among triangles with at least FIVE common candidate neighbors. This is only a NECESSARY condition: we do NOT assume the common neighbors form a mutually compatible five-clique or that such a half-frame extends. Filtering by it makes the set checked a SUPERSET of all true BH half-frames.

## 4. Complete independent finite certificate

A first C++ search `frontier-20261028-bh10-clique-search-v1.cpp`, SHA **0cf7d89b95b57baf736e1ffcf6f6d692875d0c38dde6945186ac488cbbe545b9**, result SHA **91cfba03e68dabf077487787bbd6264e4f3ec664aa0ecaeb74a0bcef8af5c362**, independently generated the balanced rows, the full compatibility graph and every triangle. Actual bounded output was

```text
candidate_rows 1075 compatibility_edges 26715
triangles 53065 common5 16064 halfmatch 0 extension_nodes 0
found 0 timed_out 0
```

The algorithm finishes the whole triangle loop, not a random sample; it applies the necessary >=5-common-neighbor condition, then checks for a Gamma_E perfect matching. The reported `extension_nodes 0` means no half-frame with a matching survived, not that a five-row completion search was falsely claimed exhaustive.

A different implementation `frontier-20261028-bh10-half-independent-v1.py`, SHA **a1225322091753cc2d50dab645392c15aa5a9456565df686dcf72ba85fb65208**, independently deduplicates all9! permutations, uses Python integer bitsets, and computes Gamma_E matchings by bitmask dynamic programming. Its output JSON SHA is **c2ec32ec4cd261ec0e357e060decd1175608c2c6f68bf5a4bd7b2777cebeed1**. Actual complete run:

```text
independent row candidates 1075 compatibility edges 26715
triples 53065 common5 16064 halfmatch 0 isolates {0:64, 1:12800, 2:3200} timed_out False
```

For an auditable per-half-frame certificate, `frontier-20261028-bh10-structural-cert-v1.py` SHA **4f79cfad9d08e846f9ae0711ef770220d90a2eb58a75dd20704ed84942d2d95f** produces `frontier-20261028-bh10-structural-cert-v1.json`, **612365 bytes**, SHA **67bc6f39a6d2bbd6a3c181dc4a7e5baaa7e5406b4ad8a50eb997b44e41197eb2**. Each of its16064 eligible triples has a simple no-perfect-matching witness:

```text
12800 graphs: an isolated column (one isolated total)
 3200 graphs: an isolated column (two isolated total)
   64 graphs: a five-vertex odd subset with no edges to its complement
```

An isolated vertex, or any odd subset with no edge leaving it, plainly forbids a perfect matching. `frontier-20261028-bh10-certificate-replay-v1.py`, SHA **4a9dda035c105fe6479ea2c44e8092aaaccda2ee812de25c5c69a7a85aa0c935**, imports NO producer code: it recursively generates all22680 balanced tails, reconstructs the1075 candidates and26715 compatibility edges, enumerates all53065 triangles, independently verifies the16064 eligible triples are covered exactly ONCE, and checks every reported isolated vertex or odd cut against freshly computed fifth-root difference counts. Actual output:

```text
PASS independent recursive 22680 balanced-row generation; 1075 candidates; 26715 edges
PASS all53065 triangles; exactly16064 eligible triples covered once
PASS each eligible graph has independently verified isolated vertex or odd cut
consequence needs written BH normalization/physical transversal caller
```

The final line is essential: the code's exact finite output alone is NOT the theorem. Sections2–3 pay the full quantifiers, WLOG normalization, >=5-common-neighbor necessity and original physical caller. The independent checker does not use floating arithmetic or the author's previously checked particular B10 matching result.

## 5. Sanity boundary: a valid half-frame can still fail extension

A separate bounded Z3 model without the >=5-neighbor extension criterion produced the exact 5×10 half-frame

```text
0000000000
0121230434
0242410313
0313140242
0434320121
```

Independent exact checker `frontier-20261028-bh5-half-frame-check-v1.py`, SHA **1b7f9ed773e03037973851e0792c5d6376d618d26d3f5d6d1243f2baaf67c736**, verified its five mutually orthogonal rows and five designated orthogonal column pairs, but found only FIVE distinct half-column signatures, each repeated twice. Thus a half-frame matching alone is NOT a full BH witness.

In fact a full fifth-root BH(10,5) cannot have ANY two projectively parallel columns on a 5-row half. If their half inner product has modulus5, full column orthogonality forces the complementary five unit terms to sum to the opposite complex number of modulus5. Equality in the triangle inequality forces each complementary term to be the exact negative of the half ratio. After cancelling allowed row/column gauges, this would require −1 to be a fifth root, impossible. This also illustrates why the >=5 actual outside-row requirement in §3 cannot be dropped.

A distinct-half-column Z3 search returned **unknown (30-second timeout)**; it is neither a proof nor a counterexample. The complete exact graph certificate in §4, not this solver, proves the stated no-matching theorem. The earlier isolated B10 product nevertheless gives a fully verified maximal-cardinality QLS(10) with100 distinct rays, but it has no transversal by this result; its exponent certificate `frontier-20261028-butson-maximal-qls-result-v1.json` SHA **c809119bffef2c66ea67ad47b3b7b7d3b25be2cf60fd27aeae80b3c9f155f93d** and independent original-definition verifier SHA **7edaa590daf5fac745016096f60304aaa42c91c52db365c8370aab133be341bc** remain only a NON-resolvable partial object.

## 6. Remaining original gap

No assumption that every BH(10,5) is equivalent to one published matrix was made; indeed an overbroad external search synopsis asserting a universal equivalence was rejected. The result is universal over BH(10,5) only within formula (1). It does not exclude product arrays with other phase alphabets or arbitrary complex Hadamard K, multiple noncommuting row bases, nonuniform/general QLS, or any other resolution geometry. No actual 1-resolvable 100-ray array or unrestricted no-go is produced.

The complete finite certificate and independent replay are exact integer calculations, not a formal proof, human review, external-model review, or novelty clearance. Main must arrange a full independent scientific review before adoption. No held historic proof was accepted merely by chronology and no source, process or authorization record was retroactively changed.

**END — ALL-BH(10,5) Fourier-product family has no orthogonal transversal; general QLS10 remains OPEN.**
