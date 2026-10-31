# Three zero-net reflection pairs in the type-I subclass

Owner **MathOlson-2-2**. Native `/bin/date` immediately before this write: **Wed Oct 28 18:46:38 PDT 2026**. A **WRITTEN sufficient-condition candidate**, with actual bounded checks below; no independent review, full type-I theorem, formal proof or novelty claim.

## 1. The actual-word theorem

Let p be ANY odd prime and a∈F_p nonzero. Let W be an actual original-order `D_(2p)` word of length4p−1 with exactly `2p−1` rotations `r^a`, `p−3` rotations `r^(−a)` and p+3 arbitrary reflections. At a reflection i let Q_i be the INTEGER count of +a rotations before i minus the count of −a rotations before i.

If there are SIX actual reflection positions

`i_1<j_1<i_2<j_2<i_3<j_3`

such that `Q_(j_t)−Q_(i_t)=0` for t=1,2,3, then W has an original-order identity subsequence of exactly2p occurrences. The pairs must be chronologically separated, but their reflections need not be adjacent in W and their exponents are arbitrary.

## 2. Exact two-reflection alternative

For ANY specified pair with Q-difference zero, the actual signed rotation multiset still contains `2p−1` values +a and `p−3` values −a. Selecting exactly `2p−2` actual rotations can include any q of the signed −a values, `0<=q<=p−3`; the selected signed sum is

`−2(1+q)a`.

These p−2 distinct sums are **all field elements except 0 and 2a**. Thus if the actual directed reflection difference `y_j−y_i` is outside `{0,2a}`, the pair and an actual choice of `2p−2` rotations immediately select identity.

For the rest of the proof, assume each of the three actual pairs has directed difference either 0 or 2a. This is an exact residual for these pairs, not a presumed equality of their exponents.

## 3. Four/six-reflection choices

For any collection of two or three of the chronologically separated zero-net pairs, take all their reflection endpoints. The intervals where a selected rotation changes sign are disjoint and each has net Q-increment zero. Consequently the signed rotation multiset remains exactly `2p−1` occurrences of +a and `p−3` of −a, and its total is `T_0=2a`.

If the selected pairs contain r directed differences equal to 2a, their reflection contribution is `−2r a`; the product with ALL rotations has exponent `2(1−r)a`. The following actual omission choices leave precisely2p occurrences and preserve zero exponent.

* **Mixed pair types:** If one of the three differences is 0 and another 2a, select one pair of each (four reflections). Their all-rotation exponent is zero. Omit p actual signed +a rotations, of sum `p a=0`; this leaves `2p−4` rotations plus four reflections.
* **All three differences zero:** Select all three pairs (six reflections), and omit p+2 actual signed +a rotations, of sum `2a`. This is possible because `2p−1>=p+2` for p>=3. The remaining `2p−6` rotations plus six reflections have identity product.
* **All three differences 2a, p>=5:** Select any two pairs. Their all-rotation exponent is −2a. Omit p−1 actual signed +a rotations and one actual signed −a rotation, whose sum is `(p−2)a=−2a`; the negative rotation exists because p−3>=1. The remaining rotations plus four reflections select identity.
* **All three differences 2a, p=3:** Select all six reflections and no rotations. Their reflection exponent is `−6a=0` in F_3 and their parity is even; the six actual occurrences already have length2p and identity product.

At every branch the sign and omission computation refers to the ORIGINAL word and the actual chosen reflection positions. Other unselected reflections do not affect selected-word parity. This proves §1.

## 4. Remaining gap

The theorem is conditional on finding three chronologically separated Q-zero pairs. It does NOT claim every type-I word has them. In particular it does not settle the entire R=3p−4 band or L_RES. It is compatible with the separate all-prime family in which six reflections are genuinely minimal; it makes no unproved statement about the minimal number for any other word.

## 5. Actual exact checks

`frontier-20261028-dihedral-type1-zero-triplets-experiment.py`, SHA256 `963604aa52f6b48f5754783db75a0a65b9b8f7af64073fd34c6c2d215dbc0d68`, generated `frontier-20261028-dihedral-type1-zero-triplets-results.json`, SHA256 `71309c2d7549a1ebeaf8e5f7820327fcc2a8faabb9eb4c6dc741a309f144a5dd`. It tried 100 random layouts at each p=3,5,7,11,13; layouts without three qualifying pairs were SKIPPED, not solved (83,51,20,3,1 respectively). For each qualifying layout it additionally assigned three representative pair-difference patterns to exercise all branches.

Separately written `frontier-20261028-dihedral-type1-zero-triplets-checker.py`, SHA256 `1a7815e59ead582fbfcec835356dac1a060044a9b16b316543fb8532bc1f8745`, imported no producer code and returned `PASS_INDEPENDENT_ZERO_TRIPLETS_CHECK`; output `frontier-20261028-dihedral-type1-zero-triplets-check-results.json`, SHA256 `0c3da28b328e252f4bc7a1425efd6a82fe903e2b0d13716ec005b834fcd71c51`. It reconstructed all 1,368 qualifying full original words and their three separated INTEGER-prefix-zero pairs, checked actual signed omissions and counts, and directly multiplied every distinct-index original selector. Observed branches: 328 random/two; 9 random/four-mixed; 3 random/four-all-two; 2 random/six; and forced 342/four-mixed, 325/four-all-two, 359/six. Three intentional duplicate-index, overlapping-pair and duplicate-omission mutations were rejected for their intended reasons.

These checks are bounded and do not establish the written theorem for all words, formal proof, human/cross-family review or novelty.

**END — exact zero-net triplet theorem and residual.**
