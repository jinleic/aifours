# Independent review: all-BH(10,5) Fourier-product obstruction

Native `/bin/date` observed immediately before preparing this review: **2026-10-28T18:28:57-0700 PDT**. The successful replay began at **2026-10-28T18:27:55-0700 PDT**, and the checker's native clock observation before creating its receipt was **2026-10-28T18:27:58-0700 PDT**.

## Disposition and scope

**FATAL 0; MAJOR 0; MINOR 0.** The complete independent finite replay and the written mathematical reduction support the stated **no orthogonal transversal** theorem for the specific Fourier10 × BH(10,5) product arrays, including the stated phase gauges, common unitary, cell phases and physical row/column relabelings. Consequently there is no Latin-incidence 1-resolution in which each symbol class is an orthogonal transversal. This is an independent same-harness scientific review, not a parent acceptance, a human or external-model review, a formal-kernel proof, or a priority determination.

The computational result is **complete over the specified finite normalized half-frame superset**, not a sample. Universality over all admissible K and all five-row halves follows from the mathematical normalization and necessary-condition argument below, not from enumerating or classifying all BH matrices. The result does **not** exclude arbitrary complex Hadamards, other product constructions, or arbitrary/general QLS10 and does not establish universal BH equivalence. The source's ancillary claim about a previously constructed maximal 100-ray example and the historical outputs of the author's cited programs were not independently checked and are not premises here.

## Frozen inputs and independent artifacts

The manifest was read first, then the complete 105-LF proof, then the entire 612,365-byte one-line JSON certificate; the certificate was fully UTF-8 decoded, strictly parsed, and all its records examined.

| Item | Bytes | SHA-256 |
|---|---:|---|
| `manifest-v1.json` | 1,921 | `f36d49b3d25ce08534a3081f7c491af09ee5a08b0c73e01c12ed6ed83fa2ca46` |
| Pinned `frontier-20261028-all-bh10-5-product-obstruction-v1.md` | 11,149 | `44776a4da92b9b50cc9b8710bdd7b7dc7b2119dbb7c3beebf4aa909969885678` |
| Pinned `frontier-20261028-bh10-structural-cert-v1.json` | 612,365 | `67bc6f39a6d2bbd6a3c181dc4a7e5baaa7e5406b4ad8a50eb997b44e41197eb2` |
| `independent-check-v1.py` | 23,139 | `0b64bd7e3b0ee6527b201a4307cca016754516c31d1a5aab4f34058a3157f809` |
| `receipt-v1.json` | see receipt | `e131fa267ed4edf0992064dc8d493923a1e8a1d217f82a29a37d38175123a011` |

The checker uses only Python's standard library, reads the frozen proof/certificate, and neither reads, imports, nor executes an author checker or producer. It verifies the manifest and both complete input hashes/lengths, rejects duplicate JSON keys, regenerates the finite objects, verifies every witness and also independently runs a perfect-matching DP on every eligible graph. The successful command was `python3 -B independent-check-v1.py` under Python **3.14.3**; it exclusively created the receipt after all checks and controls passed. A first `/usr/bin/python3 -B` invocation used system Python **3.9.6** and failed at `int.bit_count()` before creating any receipt. Use Python **3.10+**; a later reproduction must use a fresh output directory containing the same manifest and checker, since an existing receipt is not overwritten.

## Physical caller, all gauges and all halves

Write a gauged admissible K as `K[t,c] = alpha[t] beta[c] omega^a[t,c]`, where `|alpha|=|beta|=1` and `omega` is a primitive fifth root. Even for arbitrary, not necessarily fifth-root, `alpha` and `beta`, the `alpha` factors give one common diagonal unitary on every vector and `beta[c]` gives a cell phase shared within physical column `c`; both preserve the orthogonality of any cell collection. Thus it suffices to work with the fifth-root matrix. A common arbitrary unitary, arbitrary cell phases, and permutations of physical rows or columns likewise preserve both orthogonality and the property of meeting each row and column once.

For actual normalized vectors `psi_(r,c)(t) = zeta10^(r t) K[t,c]/sqrt(10)`, fixed `c` gives a Fourier orthonormal basis and fixed `r` gives a K orthonormal basis. More generally the numerator of the physical inner product is

`sum_t zeta10^((s-r)t) conjugate(K[t,c]) K[t,d]`.

Suppose a transversal exists. Its ten different physical row labels contain the five opposite pairs `(r,r+5)`, `r=0,...,4`, and its ten physical columns are all different. Therefore those five opposite-row pairs partition all ten K-column labels into five disjoint pairs. For each such distinct pair `c,d`, let E be the five even Fourier coordinates and O its complement. Since `zeta10^5 = -1`, column orthogonality and the actual opposite-row inner product respectively give

`S_E(c,d) + S_O(c,d) = 0`, and `10 <psi_(r,c),psi_(r+5,d)> = S_E(c,d) - S_O(c,d) = 0`.

Thus `S_E(c,d)=0`. The graph `Gamma_E` with an edge exactly for this zero half-sum must consequently have a perfect matching. This is a necessary condition only; neither a matching nor the stated extension filter alone constructs a transversal. The proof actually considers **every** 5-subset E of the K rows, hence in particular the actual even-coordinate E for every K, including any K with permuted rows. Reordering rows of a half for the graph argument is a combinatorial relabeling, not an unproved assertion that arbitrary Fourier-coordinate permutations preserve the entire physical array.

For a sum of five fifth roots, the integer count polynomial of degree at most four vanishes at `omega` iff it is a multiple of `Phi_5=1+X+X^2+X^3+X^4`; with five terms the five counts are therefore all one. With ten terms they are all two. This justifies the exact integer half-edge and full-row orthogonality predicates; no floating-point phase comparisons or BH classification are used.

## Complete normalization and finite reduction

Take any admissible K and any E. Choose **any ordered pair** `p,q` of distinct rows in E and **any** pivot column `c0`. After removing the arbitrary phases as above, let the fifth-root exponents be `a[t,c]` and set

`b[t,c] = a[t,c] - a[t,c0] - a[p,c] + a[p,c0] (mod 5)`.

The p-row and c0-column are zero. Row orthogonality makes the q-row contain each residue exactly twice; since its pivot is zero, a permutation of the remaining columns puts it at `(0,0,1,1,2,2,3,3,4,4)`. This dephasing changes each half-column difference only by a c,d-dependent constant independent of t; row gauges cancel. Hence it relabels the graph without altering its edges. Arbitrary orders within the equal-residue pairs are also only column relabelings.

Every remaining normalized row starts in zero, contains each symbol twice, and has balanced difference from the canonical second row. Orthogonality prevents duplicate rows; the first and second rows themselves are excluded from the candidates. The three other rows of E form a triangle in the candidate compatibility graph. The five actual rows outside E are five **distinct** additional candidates adjacent to all three vertices. Thus at least five common neighbors is necessary, even though those five neighbors need not form a clique in the checked superset. This proves coverage for every K, E, choice of p, q, c0, and permitted gauge/permutation without assuming that any two BH matrices are equivalent.

The independently implemented row generator assigned positions to the second zero and the four pairs of nonzero residues: `9 * C(8,2) * C(6,2) * C(4,2) = 22,680`. It sorted the surviving rows lexicographically to bind certificate indices. The checker then exhaustively found:

| Complete object | Count |
|---|---:|
| Balanced dephased rows before second-row filter | 22,680 |
| Candidate rows | 1,075 |
| Compatibility edges | 26,715 |
| All unordered triangles | 53,065 |
| Triangles with at least five common candidate neighbors | 16,064 |
| Certificate records, exact set equality and no duplicates | 16,064 |
| Independently checked isolated-vertex witnesses | 16,000 |
| Independently checked odd-cut witnesses | 64 |
| Independent matching-DP rejections | 16,064 |

The isolated-vertex histogram across **all** eligible graphs was 12,800 with one isolate, 3,200 with two isolates, and 64 with none. Every odd-cut record was checked for a nonempty proper odd set and for **every** edge leaving it; a separate full-record count found that all 64 supplied sets have exactly five vertices. An isolate cannot be matched. A perfect matching of an odd-cardinality set would require at least one edge leaving it; these cuts have none. Every certificate entry was checked against a freshly constructed half-column graph, and every eligible triangle was covered exactly once. The independently computed DP also found no perfect matching in any of the 16,064 graphs.

## Controls and explicit coverage limitations

- The checker rejected, for their intended reasons, a removed certificate record, duplicate record, unexpected triple, repeated or boolean triple index, unknown record field, duplicate JSON key, out-of-range or nonisolated reported isolate, even or repeated-vertex cut, and an odd cut containing a crossing edge. The receipt records each exact reason; these are in-memory mutations, not altered source files.
- In a reconstructed genuine BH example, for `E=(0,1,2,3,4)`, columns 2 and 4 are **not** adjacent under the conjugate/difference predicate but become adjacent under the erroneous addition predicate. For columns 0 and 1, the correct `S_E-S_O` is nonzero whereas the erroneous `S_E+S_O` is zero. These distinguish both conjugation and opposite-Fourier signs.
- A separately checked 5-by-10 half-frame has five orthogonal rows, five duplicated column signatures and an actual five-edge matching `(0,1),(2,3),(4,5),(6,7),(8,9)`. Once normalized it has candidate triple `(0,25,50)` with **zero** common candidate neighbors. This positive matching control demonstrates why half-frame matching without the five-outside-row condition does not supply a full BH witness.
- The checker independently found one full BH matrix by an eight-clique search and directly checked all 45 row pairs and all 45 column pairs. For that **one** example it checked all 252 halves, all `252*5*4*10 = 50,400` ordered first-row/second-row/pivot dephasings, that all five actual outside rows were common neighbors, and the relabeled graph against the corresponding certified graph. One deterministic fifth-root row/column gauge was tested for every half; arbitrary complex gauges are handled by the written algebra above, not exhaustively sampled.
- In exact `Z[X]/Phi_10(X)` arithmetic, this same example passed 900 actual physical row/column basis-pair inner products and 56,700 opposite-row inner products across all 252 half-coordinate arrangements, 45 distinct column pairs, and five opposite row pairs. These physical numeric controls are **sampled in K**, whereas the half-frame enumeration and certificate checks above are complete and the caller/normalization is a general proof.

No author checker output, external source, held proof premise, external model, paid API, or classification theorem was required.
