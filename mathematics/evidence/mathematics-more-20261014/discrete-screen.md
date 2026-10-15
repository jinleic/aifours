I screened all ten chapters, and none of them earns a full-resolution run. Every explicit question is either already solved, a famous conjecture the README already rules out, not precisely posed, or out of reach by computation. Two exact questions could each be settled outright, but only negatively: a single finite counterexample would refute them. I'd launch at most a cheap counterexample search, and only after a literature check. I ran no computations; the reductions below are my own derivations and nobody has reviewed them.

Line numbers below refer to `/tmp/math10000_full.txt`; PDF page = book page + 16.

## Status of every explicit book question

**Covering systems, pp. 104–106 (Sun Zhiwei)**

| Lines | Question | Status |
|---|---|---|
| 3866–3868 | Can the least modulus of a distinct-moduli covering be arbitrarily large? | **Solved, answer no** ([Hough, arXiv:1307.0874](https://arxiv.org/abs/1307.0874), Ann. Math. 2015) |
| 3885–3886 | Erdős–Selfridge: a distinct covering with all moduli > 1 must have an even modulus | Open, famous. Partial results: some modulus is divisible by 2 or 3 ([1703.02133](https://arxiv.org/abs/1703.02133)); no odd square-free covering ([1901.11465](https://arxiv.org/abs/1901.11465)); a Lean-checked bound lcm > 10000 ([2607.25628](https://arxiv.org/abs/2607.25628), seen only via search snippet) |
| 3887–3890 | A distinct-moduli covering other than {0(1)} cannot be disjoint | Solved in the book itself (Davenport–Mirsky–Newman–Rado) |
| 3895–3897 | Disjoint coverings with each modulus repeated ≤ M times: can the least modulus be arbitrarily large? | Solved, answer no (Simpson 1986, per the book) |
| 3898–3902 | Reciprocal sum → ∞ as the least modulus → ∞ | Solved (Filaseta–Ford–Konyagin–Pomerance–Yu 2007, per the book) |
| 3911–3912 | 78557 is the smallest Sierpiński number | Open. Five k remain ([prothsearch](http://prothsearch.com/sierp.html)); confirming it needs PrimeGrid-scale prime searches, refuting it needs a proof |
| 3926–3928 | Herzog–Schönheim | Open. Known for |G| < 1440 ([1803.03569](https://arxiv.org/abs/1803.03569)) and for simple and symmetric groups ([2509.25118](https://arxiv.org/abs/2509.25118)) |
| 3938–3940 | **Sun: k pairwise disjoint cosets of finite-index subgroups force gcd([G:Gᵢ],[G:Gⱼ]) ≥ k for some i < j** | **Open** (see nomination 2) |

Lines 3882–3884 only state a consequence that would follow if Erdős's problem had a positive answer; since Hough answered it negatively, this is not a separate question.

**Davenport constants, pp. 141–142 (Sun Zhiwei)**
- 5295–5300: determine D(G) from the structure of G. This is a research program, not one statement.
- 5310–5312: Olson's conjecture D(C_nʳ) = 1 + r(n−1). Open and famous. The best general result is the asymptotic D(C_nʳ) ~ rn ([1709.08033](https://arxiv.org/abs/1709.08033)).
- **5332–5334: Olson's ordered Erdős–Ginzburg–Ziv conjecture** (the n chosen terms must keep their original order, i₁ < ⋯ < iₙ). **Status not established.** Every source I found uses "product in some order" ([Gao–Li](https://cfc.nankai.edu.cn/_upload/article/files/d2/e7/02ad99784f4bbe19008160bb92ce/cad4f1ea-5d2e-46ac-99c5-e2fb33887cf7.pdf), [2603.21052](https://arxiv.org/abs/2603.21052), [2608.15568](https://arxiv.org/abs/2608.15568)), and none proves or refutes the ordered version.

**Weiss, pp. 419–420, lines 14660–14661.** Open. A 2021 paper calls it "still wide open" (search snippet, [2106.06750](https://arxiv.org/abs/2106.06750)), and I found no 2025–26 proof.

**Chvátal, pp. 422–423, line 14746.** Claimed solved in 2026 preprints:
- [Chang–Liu–Liu, 2609.19123](https://arxiv.org/abs/2609.19123)
- [Ellis–Filmus–Friedgut, 2609.28404](https://arxiv.org/abs/2609.28404), with a Lean repository (not inspected)

I'd exclude it.

**Latin transversals, pp. 430–431**
- 14966–14967: Ryser's conjecture for odd orders. Open, and already excluded in the README.
- Its parity strengthening is resolved in the book itself (lines 14968–14971): false for odd n (Parker), true for even n (Balasubramanian).
- 14973 / 14996–14997: Brualdi–Stein. Proved for sufficiently large n ([Montgomery, 2310.19779](https://arxiv.org/abs/2310.19779)). The threshold is not explicit, so the small cases cannot be finished by computation.

**List colouring, pp. 432–433.** The list colouring conjecture (15060) and the Gravier–Maffray conjecture (15065–15066) are both open ([survey 2606.31702](https://arxiv.org/abs/2606.31702); a subclass is done in [2610.16258](https://arxiv.org/abs/2610.16258)).

**Pfaffian orientations, pp. 442–443**
- Which graphs are Pfaffian (15367): the bipartite case is solved (Robertson–Seymour–Thomas and McCuaig, per the book). I found no general characterization or efficient recognition test.
- The dimer–monomer counting problems (15383–15386) are not precisely posed.

**Integer flows, pp. 446–447**
- The 5-flow (15492), 4-flow (15500–15502) and 3-flow (15509–15510) conjectures are all open.
- The weak 3-flow conjecture (15510–15512) is solved: Thomassen 2012, improved to 6-edge-connected graphs by [Lovász–Thomassen–Wu–Zhang 2013](https://www.sciencedirect.com/science/article/pii/S0095895613000506).

**Subgraph covers, pp. 448–449**
- Gallai's path conjecture (15553–15557): open; known for maximum degree ≤ 5 ([1609.06257](https://arxiv.org/abs/1609.06257)).
- Hajós' cycle conjecture (15563–15567): the book prints the weaker bound ≤ n/2. Open; verified for n ≤ 12 ([1705.08724](https://arxiv.org/abs/1705.08724)).
- Fulkerson (15574–15581): the book omits "bridgeless", so the printed statement is trivially false. Every perfect matching of a cubic graph contains every bridge, so a bridge would be covered six times. That is a transcription defect, not a result. The intended Berge–Fulkerson conjecture is open.

**Self-avoiding walks, pp. 450–452**
- An exact formula for c_n (15620–15622) is not a precise question.
- The d ≥ 5 cases are solved (Hara–Slade 1992, cited in the book).
- The d = 4 logarithmic correction is open for the true self-avoiding walk; only the weakly self-avoiding version is done ([1403.7422](https://arxiv.org/abs/1403.7422)).
- The exponents γ and ν, the SLE(8/3) scaling limit and universality (15639–15702) are all open.
- At lines 15639–15648 the book states the existence of γ for d = 2, 3 as fact; it is unproven.

## Nominations (each settles the question only if a counterexample exists)

**1. Olson's ordered EGZ conjecture (line 5334; book p. 142, PDF 158).**
- **Statement:** for every finite group G of order n and every a₁, …, a₂ₙ₋₁ in G, there are i₁ < ⋯ < iₙ with a_{i₁}⋯a_{iₙ} = e.
- **Why it is the best target:** one group plus one sequence of length 2n−1 would refute it.
- **Evidence it is tight:**
  - In S₃, the length-10 sequence r⁵s⁵ has no ordered product-one subsequence of length 6. So the ordered bound 2n−1 is already sharp there, whereas the unordered constant is only 9.
  - In D₂ₘ with m odd, r^{2m−1}s^{2m−1} does the same.
  - Adding a third element between those two blocks or at either end always creates a solution (an injectivity argument), so simple block constructions do not break the conjecture.
- **Attack:** exhaustive search over small non-abelian groups (orders 6 to about 32, then A₅). Track, for each prefix, which pairs (number of chosen terms, product) are reachable, merge equivalent states, and look for a length-2n−1 sequence that never reaches (n, e).
- **First step:** a literature check of Olson 1976 (J. Number Theory 8:52–57) and the papers citing it.
- **If the search finds nothing:** that is only finite evidence. No proof route is in sight, because the standard induction combines sub-blocks out of their original order.

**2. Sun's disjoint-coset conjecture (lines 3938–3940).**
- **Status:** confirmed open in July 2026 ([Fornal–Sun, 2607.24655](https://arxiv.org/abs/2607.24655)). Known cases:
  - integers, k ≤ 20 ([O'Bryant](https://arxiv.org/abs/math/0604347))
  - groups, k = 3, 4 ([Zhu](https://arxiv.org/abs/0807.2207))
  - k = 2 and p-groups ([Sun](http://maths.nju.edu.cn/~zwsun/conj.pdf), Conj. 5)
- **Where a counterexample could be:** the first open group case is k = 5. My derivation says a k = 5 counterexample must satisfy all of the following:
  - every index is even and pairwise gcds are 2 or 4;
  - at least three indices are divisible by 4, with pairwise gcd exactly 4, and at most one is divisible by 8;
  - at most one index is divisible by 3;
  - G is not abelian. An abelian G reduces to its Sylow 2-subgroup, where the p-group case applies.
- **Attack:** a GAP search over groups whose order fits these patterns (e.g. multiples of 420).
- **Caveat:** I expect the conjecture is true, so the chance of a hit is low. Proving k = 5 would be a partial result, not the book question. A full proof is out of reach, since the best integer result is k^(1−o(1)).

## openai/math overlap
I searched the local clone and the remote main `CONTENTS.md` (2026-10-14); neither covers any of these questions. Only adjacent results exist:
- **237:** honeycomb-lattice self-avoiding walk, exponent 3/4. Its Lean scope covers supporting finiteness, free energy and strip estimates only; it is a different lattice and does not settle Z².
- **181:** Erdős–Gallai, at most Cn cycles and edges (also [2610.07840](https://arxiv.org/abs/2610.07840)). This is weaker than Hajós.
- **113:** counting perfect matchings.
- **226:** double-dimer loops converging to CLE₄.
- **180:** Barnette; mentions Pfaffian graphs.
- **162:** Ryser's hypergraph covering conjecture, unrelated to Latin squares despite the name.

## Sources I could not read
- Olson 1976 and the Gao–Geroldinger 2006 survey are paywalled.
- For Simpson, Filaseta et al., Hara–Slade and Robertson–Seymour–Thomas I relied on the book's own statements.
- The 2607.25628 claim and the Weiss "wide open" quote come from search snippets only.
- The 2026 Chvátal proofs are unrefereed.
- Hough's bound is cited from the arXiv abstract (≤ 10¹⁸), not the published version.
- The extracted text splits fractions and formulas and drops figures; the statements are still recoverable.