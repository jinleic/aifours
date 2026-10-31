# f49 — review of chronological crosscut and same-gap selectors

**Verdict: NO_SUBSTANTIVE_DEFECT at the two stated odd-prime, actual-word scopes.** The two proofs below use original occurrences, not freely reordered multisets. Neither theorem settles every dihedral word, the unrestricted finite-group ordered problem, novelty or priority. This is same-harness written review with separately written finite exact checks, not formal/kernel, human or configured-family review.

Actual native prewrite observation: **Wed Oct 28 17:40:19 PDT 2026**; no inferred completion or delivery timestamp.

## Bound inputs, definitions and exposure

- Assignment `institute/runs/three-area-2026-10-27-96h/review-waves/f49-olson-crosscut-and-same-gap-selectors/assignment-v1.json`, SHA256 `3a7a57e77583948518b3afe77007f786af2f6486fadca7afd166199b277f7ca0`.
- Crosscut candidate `frontier-20261028-dihedral-crosscut-support-v1.md`, SHA256 `1907b90bbc641716196b484c08e0da7f8b6f2176634d98190e87d5a86381bc34`, all 145 LF read through the ending.
- Same-gap candidate `frontier-20261028-dihedral-same-gap-pair-selector-v1.md`, SHA256 `4e53b8fa3eb8b1050a8cd5d8922edcfc363a7ad228e9e83c3c2553673c955765`, all 69 LF read through the ending. Both are in `mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/`.
- Registered dihedral route: the slot's `intake-v1.md`, SHA256 `856c96797ca53d7a96c5a01eadccb6ca5db943eabbb2a3f9a4ca4de906a5d189`, LF21–27, gives actual original-order words of length \(4p-1\) and exactly \(2p\) selected original occurrences. Its initial route is not the all-finite-group theorem. The exact separated-pair definition used for the comparison comes from `frontier-20261028-exact-binary-packet-class-v1.md`, SHA256 `2e7c1ab87fc0e5027b192140b08e53b668117a491ef8aedd627b433ea053a20e`, LF7–24: pair spans satisfy \(i_1<j_1<i_2<j_2<\cdots\), with equal quotient types at pair endpoints. The comparison below is reconstructed directly, not imported as an earlier verdict.
- I have known prior math-2 exposure, including old Olson review contacts and the later B2 source-transcription duty, as well as an earlier explicitly uncertain A9/A10/w45 exposure screen. No claim of blinding, first exposure, clean cognition, or exhaustive contact census is made. No held historical result is accepted as a mathematical premise, no historical process outcome is retroactively validated, and I did not contact the author.

## 1. Crosscut product identity and selector count

For any odd prime \(p\), work in \(D_{2p}=\langle r,s\mid r^p=s^2=1,\ srs=r^{-1}\rangle\). Fix one **actual** set \(I\) of \(2p-2\) distinct rotation positions in a \(4p-1\)-position word, and write \(S=\sum_{a\in I}x_a\pmod p\). For each reflection occurrence \(i_j\), with letter \(r^{y_j}s\), let \(z_j=y_j+2\sum_{a\in I,a<i_j}x_a\).

Choose a left reflection \(i_a\) and later right reflection \(i_b\), on opposite sides of an actual cut. Let \(U,V,W\) be the sums of the same selected rotation exponents before, between and after those reflections. Then \(S=U+V+W\), \(z_a=y_a+2U\), \(z_b=y_b+2(U+V)\), and direct use of \(sr^x=r^{-x}s\) gives
\[
r^U(r^{y_a}s)r^V(r^{y_b}s)r^W
=r^{U+y_a-V-y_b+W}
=r^{S+z_a-z_b}.
\]
All factors are in their original chronological order; the chosen reflection pair and \(I\) are disjoint. Identity is exactly \(z_b-z_a=S\). If \(A\) and \(B\) are the sets of actual left and right potentials, then
\[
|A\cap(B-S)|=|A|+|B-S|-|A\cup(B-S)|\ge |A|+|B|-p.
\]
For each value in the intersection, selecting one actual left occurrence and one actual right occurrence gives a distinct pair and therefore a distinct \(2p\)-position selector with the SAME \(I\). When \(|A|+|B|>p\), the lower bound is positive. If \(a_v,b_v\) are the actual left/right multiplicities, the exact count is \(\sum_{v\in\mathbb F_p}a_v b_{v+S}\). This pays candidate 1 LF29–67; no assumption of distinct potential values or of \(S=0\) is needed.

### Sharpness, including a positive-count example

Candidate 1 LF69–81 correctly proves that at \(|A|+|B|=p\) the crosscut conclusion can fail: for nonempty proper \(A\), arbitrary \(\delta\), and \(B=\delta+(\mathbb F_p\setminus A)\), the intersection is empty. It is an actual word: put \(2p+1\) reflections in the two groups, repeat values as needed, and put all \(2p-2\) rotations afterward with total exponent \(\delta\). The displayed cut has zero satisfying pairs. This says nothing about within-side pairs or other selectors.

The positive count lower bound is also attained in an explicit all-odd-prime actual-word family. Put \(h=(p-1)/2\), \(A=\{0,\ldots,h\}\), and \(B-\delta=(\mathbb F_p\setminus A)\cup\{0\}\). Each support has \(h+1\) values, their intersection is exactly \(\{0\}\), and \(|A|+|B|-p=1\). In the left reflection group list every value of \(A\) once and repeat the nonintersection value 1 exactly \(p\) more times; in the right group list every value of \(B\) once. The number of reflections is \(2p+1\). Append \(2p-2\) rotations of total exponent \(\delta\). Their selected prefix at every reflection is zero; the only valid crosscut pair is the unique left value0/right value\(\delta\). Thus the exact occurrence count equals the positive lower bound 1, not merely a support-intersection abstraction. This does not claim simultaneous equality for every choice of support sizes and multiplicities.

## 2. Same-gap rotation-pair selector

Assume actual \(R\ge3p-3\), \(F\ge2\), and \(p-1\) disjoint pairs of rotation positions, each pair contained in one gap between consecutive actual reflections (boundary gaps included), whose exponents differ. Fix **any** two actual reflections at \(i<j\). Each rotation outside \((i,j)\) has sign \(+1\), each inside has sign \(-1\); the selected chronological exponent is
\[
 y_i-y_j+\sum_{a\text{ retained}}\sigma_a x_a.
\]
Since a prescribed pair has no reflection between its two positions, its two positions have the same sign even if the gaps or unselected factors interleave with other choices. Its two signed exponents remain distinct modulo \(p\).

Let \(t=R-(2p-2)\ge p-1\). The \(p-1\) disjoint pairs occupy \(2(p-1)\) actual rotations, leaving exactly \(R-2(p-1)=t\) other rotations. Fix \(t-(p-1)\) omissions among those other rotations and omit one position from each pair. This makes exactly \(t\) omissions and retains exactly \(2p-2\) rotations. For each pair the difference of its two possible signed omissions is nonzero. If \(X\subsetneq\mathbb F_p\) is nonempty and \(\delta\ne0\), \(X\cup(X+\delta)\) has strictly larger size: equality would make \(X\) invariant under the generator \(\delta\) of the additive cyclic group and hence all of \(\mathbb F_p\). Starting from the fixed sum and applying the \(p-1\) actual independent binary choices, the attainable omitted sums therefore fill \(\mathbb F_p\). Choose the sum \(y_i-y_j+\sum_{a\text{ all rotations}}\sigma_a x_a\); the retained sum then cancels the two reflection exponents. The final \(2p\) distinct actual positions, sorted in the original order, multiply to identity. This reconstructs candidate 2 LF8–32, including the boundary-gap, repeated-exponent, arbitrary chosen reflections and exact-omission cases.

### Gap pair-count equivalence

For a gap of \(n\) rotations and maximum same-exponent multiplicity \(M\), no unequal pair family exceeds \(\lfloor n/2\rfloor\) or \(n-M\). If \(M>n/2\), pair each minority occurrence with a distinct majority occurrence to attain \(n-M\). Otherwise repeatedly pair the two largest remaining exponent classes. The invariant \(M\le\lceil n/2\rceil\) is preserved: for even \(n=2k\), at most two classes can have size \(k\) and all such largest classes are reduced; for odd \(n=2k+1\), a class of size \(k+1\), if present, is unique and is reduced. If no maximum is at the limit, the residual bound already holds. The process continues until at most one occurrence remains, attaining \(\lfloor n/2\rfloor\). The empty gap has value0. Since gaps are disjoint, the maximum total is
\[
\sum_g\min(\lfloor r_g/2\rfloor,r_g-M_g),
\]
and the candidate's statistic \(\ge p-1\) is exactly equivalent to its pair hypothesis, not a proof that every word meets it.

## 3. Explicit family comparisons and boundaries

For candidate 1 LF83–111, an alternating word with \(2p\) reflections and \(2p-1\) unit rotations has length \(4p-1\). With the first \(2p-2\) rotations selected, \(S=-2\ne0\). The reflection potentials can be prescribed as two copies of \(t_j=j\bmod((p+1)/2)\), because \(y_j=z_j-2\min(j,2p-2)\) supplies actual reflection exponents. Each cut side has support \(\{0,\ldots,(p-1)/2\}\), so their total support size is \(p+1\); it is still a proper subset on that fixed \(I\). For \(p=3\), values left0/right1 differ by \(-2\); for \(p\ge5\), left2/right0 do so. The selected actual indices are therefore valid. The quotient word is strictly alternating, so every equal-type pair spans at least3 positions; disjoint spans give at most \(\lfloor(4p-1)/3\rfloor<2p-1\) separated pairs. The earlier fixed-I and saturated-pair certificate conditions fail only at their stated scopes; no assertion that no alternative certificate exists is warranted.

For candidate 2 LF50–62 and \(p\ge5\), the actual word \((r,r^2)^{p-1}(s,r)^{p-1}s^3\) has \(R=3p-3\), \(F=p+2\), and length \(4p-1\). The initial gap gives the prescribed \(p-1\) disjoint unequal pairs. Choose \(r^2\) from two pairs, \(r\) from the other \(p-3\) pairs, all \(p-1\) later rotations, and two of the final three reflections: the \(2p-2\) rotations occur before these reflections and sum to \(2p\), so their ordered product followed by \(ss\) is 1. For the **different** fixed \(I\) of all initial rotations, \(S=-3\ne0\) and every reflection potential is the same, so the fixed-I zero/full-support and crosscut-size tests do not apply at that \(I\). The quotient run pattern has \(2p-1>3\) odd runs. A family of \(2p-1\) chronologically separated pairs would leave only one original position unused; all pair spans have length at least2 and at most one can have length3, which permits at most three odd runs. Thus the saturated separated-pair property also fails. This remains a comparison of named certificates, not a statement that other choices or methods cannot work.

## 4. Independently executed finite checks

Own `frontier-review-f49-olson-selector-check-v1.py`, SHA256 `4101640c025ede3388ee6807d57f2cfe2a7068a334eef3e2f5a82323b4184b73`, 263 LF/10629 bytes, imports no author code or saved results. Ran from repository root:

```
python3 -B physics/evidence/three-area-20261027-96h/parallel-18/depolarizing-majorization4/frontier-review-f49-olson-selector-check-v1.py
```

Exit0, standard-library exact modular integers and independent seed `741492026`. For \(p=3,5,7,11\), 480 random actual crosscut words were checked over **4625 cuts and 170204 direct ordered pair products** (the latter count includes repetitions across cuts); all potential identities, exact counts and intersection lower bounds held, including 2485 qualifying cuts. On another 480 actual high-rotation words, 450 met the gap-pair condition, and **7012 specified reflection pairs** were constructively solved by actual omission dynamic programming and directly multiplied in original order. These are finite samples, not all-prime proof or replay of the author's 1440-word corpus.

The checker separately brute-forced the matching maximum for **2222 exponent multisets** over alphabets of sizes3 and5, lengths0–9. It generated **1050 actual sharpness words** covering every \(\delta\) and nonempty proper \(A\) for \(p=3,5,7\); each had zero qualifying crosscut pairs. It checked the crosscut alternating family at primes3,5,7,11,13 and the same-gap family at5,7,11,13, including every specified reflection pair in each latter instance. A control with interleaved selected reflections has direct ordered product1 while the false unsigned-rotation exponent is2 mod3, so the sign convention matters.

Own `frontier-review-f49-olson-positive-sharp-check-v1.py`, SHA256 `e156cd2268f0472da216535b194e8dd75cd39b932fe39ceafdeb1446661aa683`, 38 LF/1574 bytes, imports the **reviewer's** checker, not author code. `python3 -B` on that file exited0 and directly checked the positive-count equality construction above for all \(\delta\) at \(p=3,5,7,11,13\): **39 actual words**, exactly one crosscut selector each.

## Findings and limits

- Candidate 1 LF9–81: **NO_SUBSTANTIVE_DEFECT** for actual prefix-potential identity, multiplicity count, support lower bound and its threshold sharpness; the independent positive-count equality family above is an additional check.
- Candidate 1 LF83–111: **NO_SUBSTANTIVE_DEFECT** for the all-odd-prime alternating family and the expressly fixed-I/separated-pair comparison.
- Candidate 2 LF8–48: **NO_SUBSTANTIVE_DEFECT** for the any-specified-two-reflections selector and exact gap matching criterion.
- Candidate 2 LF50–62: **NO_SUBSTANTIVE_DEFECT** for its \(p\ge5\) family and qualified comparison.
- Candidate 1's reported saved replay/corpus and candidate 2's later work were not independently opened or replayed; only the new reviewer checks above are observations. The author states no checker for candidate 2 at its own LF64–67.

Neither a finite sample nor these conditional word classes prove that the required actual pairs/cut exist in every dihedral word. No full all-finite-group theorem, avoiding word, independent-family/human/formal proof, current literature priority or novelty verdict is supplied.
