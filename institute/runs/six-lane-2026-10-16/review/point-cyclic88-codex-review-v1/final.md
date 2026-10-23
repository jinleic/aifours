VERDICT: ACCEPT

1. **MINOR (optional exposition)** — [PROOF.md, §6, lines 208–220](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/point-cyclic88-parent-inputs-r2/PROOF.md:208). The corollary is correct, but explicitly explaining the other prime congruence would clarify its boundary. Concrete fix: add: “For \(p\equiv5\pmod{12}\), \((h,m)=(8,2)\) satisfies Lemma 3 because \(8\mid 2p-2\). Thus mixed classes cannot be excluded, and the argument does not force type T1.” This addition is optional; no correction is required for correctness or completeness.

I found no FATAL or MAJOR defect and no gap invalidating either result.

The definitions match. **§0, lines 24–60:** Definition 5 explicitly requires one cycle on all points. Its “automorphism” belongs to the resolution; the preceding definition of resolution isomorphism requires preservation of classes. The source’s actual class-orbit analysis confirms this interpretation. The proof adds neither classwise fixation nor class transitivity, and does not assume that the entire automorphism group is cyclic. Definition 4’s order-\(v\) wording alone is unnecessary: the explicit single-cycle condition supplies the regular translation action.

**§2, Lemmas 1–2:** Both arguments are valid. Two common points force translated blocks to coincide. A block stabilizer acts freely on points, so its order divides four. An alleged order-two stabilizer forces the additional translation \(c-a\), contradicting that stabilizer’s specified order. Every diameter pair then forces its block to be an \(H_4\)-coset. Consequently there are exactly 22 short blocks, with differences \(22,44,66\).

**§3, Lemma 3 and Corollary 4:** All three constraints are necessary:
\[
88/h\le29,\qquad h\mid22-m,\qquad (88/h)m\le22.
\]
The last inequality counts distinct short blocks across classes disjoint **as sets of blocks**, justified because a resolution partitions the block collection. Exhausting the divisors gives exactly
\[
(h,m)=(11,0),(22,0),(88,22).
\]
Thus no mixed class exists, and the short blocks form exactly one class. This proves the source’s T1 property without importing its T2/T3 results.

**§3, Lemma 5 through §5:** Every remaining class has stabilizer order 11 or 22, and both corresponding subgroups contain translation by 8. Lemma 6 correctly uses disjointness within a class: if \(X\) contains \(x,x+d\), then \(X+d\) intersects \(X\), forcing equality. The block covering \(\{0,8\}\) is full, so this equality contradicts its trivial stabilizer. The additional count of 440 uncovered unordered pairs is also correct.

**§6, corollary:** The substitution argument is exhaustive because the divisors of \(8p\) are \(1,2,4,8,p,2p,4p,8p\). The critical congruence is \(p\equiv3\pmod4\), which excludes the mixed candidate \((8,2)\). The remaining non-short class stabilizers have orders \(p\) or \(2p\), both contain 8, and \(8<2p\) excludes a short-block difference. This establishes the infinite family independently of the finite checks.

The positive cases survive for precise reasons:

- **\(v=52\), §6 lines 200–205:** \((h,m)=(4,1)\) is allowed. The published class orbits of lengths 13 and 4 correspond respectively to classes containing one short block and classes containing none. T1 is not forced.
- **\(v=64\), §6 lines 200–225:** T1 is forced, but the admissible non-short stabilizer orders are \(4,8,16\), whose subgroups intersect in exactly \(H_4\). Its nonzero differences already occur in short blocks. The published example realizes orders 4 and 16, so there is no uncovered-difference contradiction.

Checks actually run, with commands abbreviated only by referring to the supplied file paths:

- **`shasum -a 256` on the proof and PDF:** returned respectively  
  `d6faaf1151d6397b6ebc2a7c434b7b8df9518b91ed53c3dc944a0b9c71a78358`  
  `d5170670a40e95195ac3e440121e447b998d3f775cc6bb52e1555e01b3b99608`.
- **`nl -ba` on the proof; `cat` on both supplied excerpts:** read the complete proof and both excerpts.
- **`/opt/homebrew/bin/pdftotext -layout <PDF> -`**, followed by page-selected calls using **`-f 1 -l 2`**, **`-f 3 -l 7`**, and **`-f 11 -l 11`**: verified Definitions 1–5, T1/T2/T3, the explicit positive example, and §7’s open statement.
- **`python3 -B -c` with an independent exhaustive four-subset enumeration:** examined **2,331,890** subsets; stabilizer counts were **`{1: 2330944, 2: 924, 4: 22}`**. Exactly the 22 \(H_4\)-cosets were compatible subsets with nontrivial stabilizer; exactly 22 compatible subsets contained a diameter pair.
- **`python3 -B -c` with independent integer constraint checks:** returned exactly **`[(11,0),(22,0),(88,22)]`** for \(v=88\), and **440** forbidden unordered pairs. Across all **833** admissible values \(16\le v\le10000\), the excluded set equalled the two stated prime families: **92 + 50 = 142** values.
- **`python3 -B -c` with a fresh transcription from PDF pp. 6–7:** reconstructed the 64-point example; verified **336 blocks**, **2016 pairs each once**, **21 parallel classes**, complete block partition, and preservation by translation by 1. Class orbit lengths were **`[1,4,16]`**; the common non-short class stabilizer was **`[0,16,32,48]`**.
- Publisher web fetches returned “not accessible”; source comparisons used the hash-verified local PDF. All completed Python verification programs exited **0**.