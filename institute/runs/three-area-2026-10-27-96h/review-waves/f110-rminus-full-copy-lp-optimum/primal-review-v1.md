# Independent review: R-minus three-branch primal

**Recorded native clock immediately before writing:** 2026-10-28T19:31:20-0700 PDT. Main exact run: 19:30:01–19:30:02 PDT; supplemental corruption controls completed 19:30:58 PDT, 2026-10-28.

## Verdict and finding

**VALID, for the specified primal feasibility claim. FATAL 0 / MAJOR 0 / MINOR 1.** The four frozen profiles define an exact rational point of the stated three-branch Shannon/copy LP at `h(a,...,j)=1847/276`. The point also satisfies all stated disjoint-original-variable `F_n` constraints for all positive integers `n`. This establishes the **primal direction**: the optimum of that stated LP, with or without these extra constraints, is at least `1847/276`.

**MINOR — incorrect source attribution.** Candidate `frontier-20261028-full-source-lp-optimum-v1.md`, Exact LP scope, says the publisher's Remark 3.8 states that cross-branch Shannon inequalities were omitted; the manifest's scope likewise attributes the omission to that remark. In the actual publisher PDF, printed p. 566, Remark 3.8 instead contrasts prior use of non-Shannon inequalities with copy-lemma constraints. The specified separation is supported by Theorem 5.2 item 2, printed p. 571, which explicitly lists three separate elemental-variable sets. Replace the incorrect Remark 3.8 attribution with that item; this citation error does not change the checked primal or the explicitly restricted LP. The native-page image `primal-remark-page14.png` retains the visual evidence.

**Upper bound and completeness boundary.** I did not replay the 1,920-row publisher dual, its row extraction or its equality to `1847/276`; those are separate imports/review duties. The exact-optimum conclusion is conditional on that upper-bound certificate. This review does not establish an actual probability distribution, an almost-entropic extension, a guessing-number lower bound, a new upper bound, a priority claim, or a formal proof. It does not establish or refute any mixed cross-branch Shannon inequality: the four inputs do not provide coordinates such as `h(b'0,d'1)`. In particular, a globally feasible 17-variable polymatroid is **not** established.

## Frozen input binding and read order

The manifest was read first and has SHA-256 `36bfb4303c5f2c3c1851b8f2bd6141fa2b19e29a1e8d516d67e561b55f811978`, 4,903 bytes and 83 LF. The three mathematical Markdown inputs were read completely in manifest order; each of the four JSON profiles was consumed and parsed completely in order; and the three checker source texts were then read completely, not imported or executed. All ten declared full SHA-256/byte/LF triples matched, both at intake and in the executable receipt:

| Order / role | SHA-256 | bytes | LF |
|---|---|---:|---:|
| source audit | `d0b494122660394b46d8ce647ed17e2f890c1f3ccf393cd4e44ccc48e87dcaf6` | 10,044 | 81 |
| all-order written input | `76d83e14a011baaa2de3a17d8f6d8a28474094bf8a8a4bd5829f14bb5c40230b` | 9,786 | 132 |
| full-LP candidate | `08af469a09689dcdf40b07bbb086c851349141f582b92714b92d5a7eef63fcdd` | 8,558 | 69 |
| original/base profile | `aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651` | 674,589 | 48,278 |
| branch 1 auxiliary | `1898339bb4ba63c53dbda6dff9603f82414f29645543631bc21d82d752941e37` | 162,159 | 11,360 |
| branch 2 auxiliary | `09981982317f1659a9a291dbbc416f77d2ac8a91eac818191048cb0ac9cd7a87` | 1,219,031 | 84,072 |
| branch 3 auxiliary | `fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0` | 1,202,939 | 84,066 |
| combined author checker | `ce96cd7148526942125c01875a749c6b6bf93e863f7ad8e4a851022a29aeaf3d` | 7,182 | 108 |
| all-order author driver | `92627e854b17b4971a430eac14d8c13fbd05988a28025e592e12b183feb62b68` | 624 | 11 |
| all-order author helper | `d4268fd6db3b4573462f04b19253b345d94e81295405a7acf7d1e3f68976210a` | 7,609 | 149 |

The executable additionally rejects duplicate JSON keys, repeated or unknown coordinate labels, duplicate entropy subsets and malformed rational strings. It compares the full expected subset universe, not only its size. The parser uses Python `Fraction`; all branch row checks use exact integers at each branch's common denominator.

## Source graph identity and copy specification

I directly fetched the publisher's public [article PDF](https://www.kybernetika.cz/content/2024/5/553/paper.pdf), SHA-256 `373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8`, equal to the hash cited by the source audit. Figure 2 on printed p. 570 was visually inspected. I independently assigned its ten visible labels to node centres, extracted its 21 black vector strokes via `pdftocairo`, subdivided the inner triangle at the three visible intermediate vertices, and compared the resulting 26 edges with the graph used for the FD checks. The vector extraction corroborates the transcription; it is not a formal verification of renderer fidelity or the visually assigned labels.

Using `a,...,j` for vertices `1,...,10`, the checked graph's neighbour sets are:

| Vertex | Neighbours | Vertex | Neighbours |
|---|---|---|---|
| 1 | 2, 3, 4, 5, 6, 7 | 6 | 1, 5, 7, 8, 9 |
| 2 | 1, 3, 7, 9, 10 | 7 | 1, 2, 6, 8, 10 |
| 3 | 1, 2, 4, 8, 9 | 8 | 3, 4, 6, 7, 9, 10 |
| 4 | 1, 3, 5, 8, 10 | 9 | 2, 3, 5, 6, 8 |
| 5 | 1, 4, 6, 9, 10 | 10 | 2, 4, 5, 7, 8 |

Thus `3–4` is present and `9–10` absent. The source Appendix B generators `(1 8)(2 10 5 9)(3 7 4 6)` and `(2 5)(3 6)(4 7)` preserve these edges, generate a group of order 8, and exhaust the graph automorphisms in an exact scan of all 80,640 degree-preserving vertex permutations. The symmetry rows checked below are the seven nonidentity group elements on every nonempty original subset.

Theorem 5.2 and the certificate naming in the frozen audit identify the following separate branches. In each step, the new tuple matches **every** nonempty subtuple jointly with **every** subset of the stated base, and its conditional-independence relation is checked against the entire previous branch outside the base, including the copied original tuple:

1. Originals plus `b'0`: copy `b` over `adefghij`.
2. Originals plus `d'1,e'1,g'2`: copy `(d,e)` over `abcfghi`; then copy `g` over `abcd,e'1,fhi`, with past originals plus `d'1,e'1`.
3. Originals plus `f'3,g'3,h'4`: copy `(f,g)` over `abcdehij`; then copy `h` over `abcdef,f'3,ij`, with past originals plus `f'3,g'3`.

## Exact primal execution

The auxiliary files contain auxiliary coordinates only: the common original coordinates are inserted from the single frozen base profile into **each** constructed branch, then independently compared as rationals across all 1,023 masks and three branches, for **3,069 comparisons**. This is not a claim that three independently supplied original profiles were present. The union has 1,023 common original plus 1,024, 7,168 and 7,168 branch-only coordinates, exactly **16,383** distinct nonempty coordinates. The three per-branch full arrays have 2,047, 8,191 and 8,191 nonempty coordinates.

| Exact check | Branch 1 | Branch 2 | Branch 3 |
|---|---:|---:|---:|
| branch variables | 11 | 13 | 13 |
| exact integer denominator | 32,430,000 | 324,300,000 | 32,430,000 |
| elemental conditional entropies | 11 | 13 | 13 |
| elemental conditional mutual informations | 28,160 | 159,744 | 159,744 |
| **total elemental inequalities** | **28,171** | **159,757** | **159,757** |
| copy-subset equalities, step 1 / step 2 | 256 / — | 384 / 256 | 768 / 512 |
| copy-independence equalities | 1 | 2 | 2 |
| **total copy equalities** | **257** | **642** | **1,282** |
| original graph FD equalities | 10 | 10 | 10 |
| original singleton caps | 10 | 10 | 10 |
| nonidentity original symmetry equalities | 7,161 | 7,161 | 7,161 |

Overall, 347,685 elemental inequalities and 2,181 copy equalities were checked. Every minimum elemental slack was zero, never negative. All original singleton values are exactly `1`; the common objective is `1847/276`, and the balance expression is `1847/276 - 20/3 = 7/276`.

The frozen base file has **4,397** coordinates, but only its **1,023 original** values participate in this primal. Its old auxiliary overlaps differ from the new profiles at **4/302**, **243/1,070**, and **460/2,002** positions in branches 1, 2 and 3, respectively. This is not an extension of that earlier 4,397-coordinate partial point.

## All positive orders for disjoint original blocks

The separately authored C++ scanner assigns each of the ten original vertices recursively to one of `A,B,C,D,Z,unused`, enumerating all `6^10` assignments and retaining exactly **13,729,980** with nonempty `A,B,C,D` and `A<B` as bitmasks. That count agrees with inclusion–exclusion and uses the symmetry under exchanging `A,B`. It uses original entropy numerators at scale **25,944** and exact wide integer arithmetic.

Writing `c=a-δ`, the checked slack is `F_n=a+n c+n(n+1)d/2`. For `d=0`, negative `c` is rejected and otherwise `n=1` minimizes the slack. For `d>0`, the scanner uses the first difference `F_(n+1)-F_n=c+(n+1)d` to select an integer minimizer, rather than executing the author's vectorized quadratic-vertex checker. All 13,729,980 minima were nonnegative; the minimum twice-scaled slack was 0 and the largest first minimizer encountered was 22. The 1,325,888 linear cases include 139,010 flat cases.

If A or B is empty the expression is a nonnegative sum of original CMIs; if C is empty it is `I(A;B|Z)+n I(A;B|D,Z)`; if D is empty, `δ=0`. Therefore the original elemental checks cover these omitted empty cases too. This establishes feasibility against the stated original-variable family, not independent verification of the cited written proof that the family is universally valid.

## Corruption controls and execution evidence

The primary run deliberately corrupted each branch's monotonicity, an auxiliary-containing elemental CMI, a copy-subset marginal, a copy-independence entropy and the original projection; every one of these 15 controls was rejected with its intended error category. Separate original cap, graph FD, symmetry, objective and duplicate-coordinate mutations were also rejected for their intended reasons: **20 intended-reason controls total**. The family scanner separately rejected synthetic negative linear slope and negative finite minimum with their respective intended reasons and accepted its positive scalar control.

Eight further executed controls targeted both second copies and both joint two-variable copies. In each of branches 2 and 3, a corrupted second-copy singleton, its `a`-conditioned subset, and its full-past independence entropy were rejected specifically at **copy step 2**; corrupting the first copied joint pair was rejected specifically at **step 1, joint selection 3**. All eight expected reason, step and subset assertions passed. Full details, including the affected masks and observed errors, are in the two receipts; no input profile was modified.

Commands executed in this review directory:

```
clang++ -std=c++17 -O2 -Wall -Wextra -Werror primal-family.cpp -o primal-family
python3 -B primal-verify.py
python3 -B primal-second-step-controls.py
```

| Own artifact | SHA-256 |
|---|---|
| `primal-verify.py` | `fb9ced37ccbd4037d68e5f9d65af42911a3da12b9c3a258f114e95286d7e958c` |
| `primal-family.cpp` | `31eedc26680cd9488a1e5089caea062ecfa5700726a64283c18b0608ffa1592d` |
| compiled `primal-family` | `e1619a7883ff5d4bfb816089c284a48b94bb36c7bdf53f1d05bbf893398d6971` |
| `primal-receipt-v1.json` | `f889d765e7fa2f562bf1c82f24b0d3d48290138253c976d01075893006f075a2` |
| `primal-second-step-controls.py` | `2a7f682e5328d125b35dee827bcdb43f844d5653b0cc62512112bbf5f6c4cc35` |
| `primal-second-step-receipt-v1.json` | `9c6394b402629fb0b583a860ac42c08b0ec8270892a46d1a3d9ba26c5c7176bf` |
| `primal-graph-page18.svg` | `64142da3b73659d5085c072df2b01810d1b455b9f1149a3b30cb19e96402f9b7` |
| `primal-graph-page18.png` | `59595d9626759ea42ed533734cc3d1f14ed5eb6566d7cfbc4cc50ff86677e3df` |
| `primal-remark-page14.png` | `4f556a63a2b319227ccfa84de0952d0c21adfc2cf2ee3d9c67c95ae0159358c9` |

**Imports and independence:** The verifier uses only the Python standard library, the separately authored C++ scanner and the directly fetched public publisher PDF. The supplemental control script imports only this review's own verifier. No author code, solver, author-generated receipt or external model was executed as proof. Source construction and the definition of the `F_n` constraints are imported from the frozen written inputs and publisher; the dual remains a separate dependency. These are same-harness computational checks, not an independent-family, human, proof-assistant/kernel, or novelty review.
