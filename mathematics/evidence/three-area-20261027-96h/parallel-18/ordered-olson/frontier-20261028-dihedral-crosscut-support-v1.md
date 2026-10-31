# Dihedral frontier — a strict cross-cut improvement to the actual two-reflection selector

Owner **MathOlson-2-2**, original math-2 slot.
Actual native `/bin/date` before this write: **Wed Oct 28 17:22:57 PDT 2026**.
**Written all-prime word-class candidate, with bounded independent exact checks. Not a full dihedral or all-finite-group solution, and not novelty-cleared.**

## 1. Exact original setup

Let p be ANY odd prime and `D_(2p)=<r,s | r^p=s²=1, srs=r^−1>`.
The original word has4p−1 actual positions; the desired selector has EXACTLY2p of those positions in increasing order, with product1.

Suppose the ACTUAL word has at least2p−2 rotations. Fix ANY actual set I of exactly2p−2 of them, with exponents x_a∈F_p, and put

`S=∑_(a∈I)x_a`.

List all its reflection occurrences in original order as i_1<⋯<i_F, with reflection i_j equal to `r^(y_j)s`. Their ACTUAL I-dependent potentials are

`z_j=y_j+2∑_(a∈I, a<i_j)x_a`.

For a cut after reflection c, with1≤c<F, define

`A={z_j:1≤j≤c}`, `B={z_j:c<j≤F}`.

These are supports of the SAME actual word with one fixed actual rotation set, not freely fitted left/right arrays. The cut is in reflection occurrence order; rotations may appear anywhere in the original word.
No F≥p+1 assumption is needed for the cross-cut theorem itself; it is automatically available in the earlier count envelope when R≤3p−2.

## 2. Exact actual-product identity

For any a≤c<b, select the SAME rotation set I and the two actual reflections i_a<i_b.
Let the selected-rotation exponent sums before, between and after those reflections be U,V,W respectively.
Direct chronological multiplication gives

`r^U (r^(y_a)s) r^V (r^(y_b)s) r^W`
`=r^(U+y_a−V−y_b+W)`
`=r^(S+z_a−z_b)`.

Thus the selected2p ACTUAL original occurrences have identity product IFF

`z_b−z_a=S`.                                                    (1)

No rotations are reordered: the second reflection changes the sign back, and the actual prefix difference pays precisely the middle segment. Repeated/zero exponents and empty segments are permitted.

## 3. Cross-cut intersection theorem and selector count

**Theorem A.** If

`|A|+|B|>p`,                                                   (2)

then the original word has an increasing-index identity selector of exactly2p actual occurrences: use I and two reflections on opposite sides of the given cut.
More precisely, the number of DISTINCT cross-cut reflection pairs satisfying (1) is at least

`|A|+|B|−p`.

**Proof.** Translate the second support by−S. Both `A` and `B−S` are subsets of F_p. The elementary union bound gives

`|A∩(B−S)|≥|A|+|B|−p`.

For each v in this intersection, choose an ACTUAL left reflection with z=v and an ACTUAL right reflection with z=v+S. Its two positions have the required original order, and (1) gives identity.
Different v values give different reflection pairs and hence different2p-index selectors with the SAME I. ∎

The condition does not require the TOTAL potential support to be all F_p, does not require S=0, and does not invoke any unproved permutation or kernel-product flattening.

If a_v and b_v are the actual numbers of left/right reflections with potential v, the EXACT number of valid cross-cut pairs is

`C_cut=∑_(v∈F_p) a_v b_(v+S)`.

This also counts distinct selectors for this fixed I/cut. The lower bound uses only support cardinalities; multiplicity can improve it. No averaging over hypothetical words is used.

## 4. The support threshold is sharp for a prescribed cut

For ANY fixed δ∈F_p and ANY nonempty proper A⊊F_p, put

`B=δ+(F_p\A)`.

Then `|A|+|B|=p` and `A∩(B−δ)=∅`, so no cross-cut potential pair has difference δ.
The strict `>p` in Theorem A cannot be weakened to `≥p` using only those two support sizes.

This is also realizable by ACTUAL original dihedral words. Take R=2p−2, F=2p+1, place all reflections first in two groups with supports A,B and arbitrary repetitions to fill F, then put all rotations after them with total exponent δ.
For the necessarily fixed set I of all rotations, the prefix sums at every reflection are zero, so the desired actual potentials are exactly their chosen exponents.
There is no qualifying reflection pair ACROSS THAT CUT. This realization does not assert that the same word has no pair within one side, no alternative selector, or no original Olson solution.
For the special case S=0, separate pigeonhole arguments may still work; equality sharpness here concerns the stated cross-cut implication only.

## 5. An all-prime strict improvement beyond BOTH earlier sufficient classes

Let p be ANY odd prime, put h=(p−1)/2 and `T={0,1,…,h}⊊F_p`.
Construct an ACTUAL word with F=2p reflections and R=2p−1 rotations, strictly alternating in quotient type, beginning and ending with a reflection. All rotations equal r.
Choose I as the FIRST2p−2 rotations, so `S=−2 mod p`, nonzero.

For j=0,…,p−1 set `t_j=j mod(h+1)`. Prescribe the2p reflection potentials as

`t_0,…,t_(p−1), t_0,…,t_(p−1)`.

This has support exactly T on EACH side of the cut after p reflections. Define each actual reflection exponent by

`y_j=z_j−2 min(j,2p−2) mod p`, for j=0,…,2p−1,

because the selected rotations before reflection j are exactly `min(j,2p−2)`.
This is a complete actual group word, not an arbitrary potential vector assumed realizable.

Both cut supports equal T and

`|A|+|B|=2(h+1)=p+1>p`.

Theorem A gives an actual2p-occurrence identity selector.
At the SAME fixed I, S is nonzero and total potential support is PROPER, so the previous `S=0 or full-potential-support` criterion does not apply.
The quotient word is strictly alternating with4p−1 singleton runs. Any equal-type pair spans at least3 positions, so at most `floor((4p−1)/3)<2p−1` chronologically separated pairs exist. Thus the previously saturated-separated-pair criterion does not apply either.

An explicit pair exists without invoking only counting: for p=3 take the left value0 and right value1; for p≥5 take left value2 and right value0. Their right-minus-left difference is `−2=S` modulo p. Both labels occur on the stated sides.
Combining those actual reflection positions with I gives exactly2p original occurrences and identity product by (1).

This proves an all-prime FAMILY of actual original words covered by the new cut criterion outside BOTH named earlier sufficient conditions. It does NOT claim those words have no OTHER certificate, or that every alternating word is covered.

## 6. Bounded actual computation and independent replay

All programs use only standard-library exact integer modular arithmetic; no floating point, external model or third-party package is involved.

| Artifact | SHA256 | Scope |
|---|---|---|
| `frontier-20261028-dihedral-crosscut-support-experiment.py` | `66ba34fb4f9db541b962f658c462454c885b7b9556674063258c7a9f07f3073c` | Same seeded actual-word corpus, all cuts |
| `frontier-20261028-dihedral-crosscut-support-checker.py` | `b36a92014ce672259da0ff21a96b1d8f4e9f8a0a401274e8b62072745f3cf4ab` | Independent seed replay and direct ordered group products; imports no producer code |
| `frontier-20261028-dihedral-crosscut-support-results.json` | `0364ceb6fe88cf3f02750b6b0681071f0f0100a44fc419ca67e563eb64e759bc` | Complete saved bounded data and actual witnesses |
| `frontier-20261028-alternating-crosscut-check.py` | `19dddb2ce61a0af03c920a4588346f407dc94d17ebccb0c27821f0482df53680` | Direct full-word checks of the all-prime family at bounded primes |
| `frontier-20261028-alternating-crosscut-results.json` | `a0187c002c4bf3c0a12c49ee137959980785fdc2993edc63263608142c81173b` | Saved alternating words/indices/results |

The first bounded run replayed the same deterministic seed2026102802 on1,440 actual words, p=3,5,7 and every R from2p−2 through3p−2,80 words per (p,R).
It reported **1,159** sampled words with a cross-cut certificate, including **519** whose SAME fixed I had nonzero S and proper total potential support, so the previous two simple sufficient conditions did not apply at that I.
These are bounded counts in a deliberately chosen corpus, not estimates of a general probability and not original conjecture verification.

The independent checker replayed all1,440 words, checked the exact support-intersection lower bound for EVERY cut, and directly multiplied **40,400** cross-cut candidate products in original index order, with multiplicity across different cuts.
It returned `PASS_INDEPENDENT_CROSSCUT_REPLAY` with the same result SHA. A deliberately duplicated selected rotation was detected by the result comparison.

The separate alternating-family checker directly validated p=3,5,7,11,13: actual word length4p−1, proper potential support, nonzero S, cross-cut selector of length2p, direct identity product and failure of saturated separated-pair count. It returned `PASS_ALTERNATING_STRICT_IMPROVEMENT`.
Those five instances check only the displayed finite family specializations; the written all-prime proof is §5. The standalone family checker is not a third independent model-family review.

## 7. Remaining original gap and verification ceiling

Theorem A is a real stronger sufficient criterion for a fixed actual I. It does NOT prove that every dihedral word has a suitable I and cut.
The equality-support counterexample concerns a prescribed cut only; it is not an original avoiding word or an all-method obstruction.
The original odd-prime dihedral question and full all-finite-group ordered Olson conjecture remain unresolved by this packet; no global open/closed or priority determination is inferred from a bounded search.

The work is independently derived from the group law and finite set intersection. Previously quarantined results are not accepted as premises or retroactively rehabilitated.
The latest owner directive permits the bounded local scientific computations; no external model/paid API, secret, deletion, Git push, publication or infrastructure mutation was used.
Written proofs and same-harness exact scripts are not formal/kernel/human/cross-family or novelty acceptance.

**END — actual cross-cut selector, sharp threshold, and an all-prime strict-improvement family.**
