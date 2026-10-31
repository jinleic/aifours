# Orthogonal-array subdesign obstruction for order-10 resolvable QLS constructions

**NEW WRITTEN AUTHOR CANDIDATE, unreviewed.** Native `/bin/date` immediately before writing: **Wed Oct 28 17:27:03 PDT 2026**. The theorem below is an exact UNIVERSAL combinatorial obstruction to a specific classical-incidence/local-subarray construction route. It is NOT a no-go for general QLS10, an assertion about overlapping surgeries or other resolutions, or a novelty claim.

## 1. Precise theorem

Write OA(n) for a set of n² four-coordinate tuples, each coordinate taking n values, such that projection to ANY two coordinate positions is a bijection onto all ordered pairs. Such an OA is precisely the four-coordinate record `(row,column, A-symbol,L-label)` of two orthogonal Latin squares A,L, but the proof is entirely in the tuple definition.

A **proper OA(k) subarray** is a subset of k² ambient tuples using k symbols in each coordinate and having the same two-coordinate bijection property; k<n. It corresponds to two orthogonal k×k Latin subsquares on selected coordinate alphabets, not to an arbitrary k×k submatrix.

**Theorem A.** Every proper OA(k) subarray of OA(n) satisfies `n>=3k`.

**Theorem B.** For EVERY integer k>=2, any two OA(k) subarrays of OA(3k+1) share at least one ambient tuple. In particular, NO OA(10) contains TWO disjoint OA(3) subarrays.

No result about maximal-cardinality quantum arrays follows by dropping the premise that a construction starts from such a classical OA or by assuming every quantum array has an embedded classical OA.

## 2. Single-subarray bound: full proof

Let P be a proper OA(k), and let S_i be its k-symbol alphabet in coordinate i, i=1,2,3,4. Any ambient tuple outside P has at most ONE coordinate in its corresponding S_i: if it had two, that coordinate pair is already attained by exactly one tuple of P, and the ambient OA's pair-uniqueness forces equality with that P tuple.

For a fixed coordinate i, every symbol occurs n times in OA(n), so `k(n-k)` outside tuples have their i-coordinate in S_i. Since an outside tuple can be counted for at most one i, these four sets are disjoint. Thus

`4k(n-k) <= n²-k²=(n-k)(n+k)`.

Because k<n, cancel n-k>0 to obtain `4k<=n+k`, i.e. **n>=3k**. No symmetry, numerical example or literature theorem is used.

A single proper embedded subarray rotated by a k×k unitary, leaving the other cells in their standard-basis rays, can introduce at most k new rays. Each original color appears n times, only k in the subarray, so all n old rays still occur. At n=10 Theorem A gives k<=3, hence this SINGLE-pocket unitary construction yields at most13 rays. The exact Parker OA(3)/Householder example reaches13, so this limited bound is attained within the scheme. This is not a bound for arbitrary sequences of overlapping/noncommuting transformations or arbitrary QLS.

## 3. Two-disjoint-subarray theorem: complete counting proof

Let P and Q be DISJOINT OA(k) subarrays of OA(n), with alphabets S_i and T_i of size k in each of four coordinates. Put `t_i=|S_i intersect T_i|`. At most ONE t_i can be positive: if t_i,t_j>0 for i!=j, choose shared symbols in those two positions. P and Q each contain a tuple with that pair, but ambient pair-uniqueness makes the two tuples equal, contrary to disjointness. Let t be the unique nonzero intersection size, or0 if none. Always `0<=t<=k`.

Let X be the `n²-2k²` ambient tuples outside P union Q. For each x in X define a(x) as the number of positions where x_i∈S_i, and b(x) analogously for T_i. The same uniqueness argument used in §2 gives `a,b∈{0,1}`. Define A={x∈X:a=1}, B={x∈X:b=1}, I=|A intersect B| and J=the number of points in A intersect B whose one S- and one T-membership are in the SAME coordinate.

**First count.** Outside P there are `4k(n-k)` coordinate-memberships in its four alphabets. Among the tuples of Q, exactly kt memberships lie in S (each shared symbol appears k times within Q); disjointness/at-most-one-overlap means they are counted once. Hence

`|A|=|B|=4k(n-k)-kt`.                                          (3.1)

**Cross count.** For ordered distinct coordinate positions (i,j), the number of ambient tuples with x_i∈S_i and x_j∈T_j is k². There are12 ordered pairs, giving12k². Within P, every shared-coordinate occurrence in the T alphabet gives3 choices of i!=j, totaling3kt; similarly Q contributes3kt. Outside P union Q, a point with a=b=1 contributes1 if the S/T memberships are in different coordinates and0 if in the same one. Thus

`I-J=12k²-6kt`.                                                  (3.2)

A shared symbol in the single overlapping coordinate occurs n times in the ambient OA, k times in P and k times in disjoint Q. The remaining `n-2k` occurrences lie in X and have both memberships in that SAME coordinate. There are t such symbols, and no other shared-coordinate locations. Therefore

`J=t(n-2k)`,  `I=12k²+t(n-8k)`.                                (3.3)

These are exact SAME-array counts, not independent bounds on overlapping categories. In particular both the A-only count and neither-count are nonnegative:

`|A|-I=4kn-16k²+t(7k-n) >=0`,

`|X\(A union B)|=n²-8kn+18k²+t(n-6k) >=0`.                    (3.4)

Now put n=3k+1, k>=2. The first inequality becomes

`-4k(k-1)+(4k-1)t>=0`.

If t<=k-1 its left side is at most `-(k-1)<0`; hence t>=k. Since t<=k, **t=k**. The second inequality then becomes

`3k²-2k+1-(3k-1)k=1-k<0`,

a contradiction. This proves Theorem B for ALL k>=2. All cases of shared coordinate alphabets, including no shared coordinate or full overlap on one coordinate, were covered. No restricted OLS table, solver output or finite enumeration is needed for the proof.

For the original n=10,k=3, the two necessary nonnegative counts are explicitly `-24+11t` and `22-8t`; t=0,1,2,3 makes at least one negative. This is an all-array consequence of the proof, not a claim that arbitrary 100-ray QLS have classical subarrays.

## 4. Actual independent checks and bounded construction search

The exact finite census `frontier-20261028-suboa-census-v1.py`, SHA256 **4d451e9e2bd554d59ab589e538123e9067f7fadf402e7592f5ea9f33e400a5f8**, verifies each complete input OA and enumerates all row/column triples in FOUR source-backed tables. Actual result `frontier-20261028-suboa-census-result-v1.json`, SHA256 **360743b7afacf4937791c033202c1823be7841a8c8368ef209b849de608c73bb**:

```text
Weisner1963-Fig1 OA3 pockets 0 disjoint pairs 0
Weisner1963-Fig2 OA3 pockets 0 disjoint pairs 0
Weisner1963-Fig3-inferred00 OA3 pockets 0 disjoint pairs 0
Parker1959-section3 OA3 pockets 1 disjoint pairs 0
  rows [7,8,9], columns [7,8,9], colors [7,8,9], labels [7,8,9]
shared-axis intersection 0: A-only -24, neither 22
shared-axis intersection 1: A-only -13, neither 14
shared-axis intersection 2: A-only -2, neither 6
shared-axis intersection 3: A-only 9, neither -2
```

Weisner Fig.3's first cell was OMITTED by the source text extractor; 00 was inferred from its remaining first-row Latin symbols and then the entire inferred table was independently verified. It is not represented as directly transcribed from the rendered page. The four-table census is a check/examples ONLY; it is NOT an exhaustive classification of all OLS(10) pairs. The universal theorem is §3's written counting proof.

The constructive array `frontier-20261028-parker-13ray-result-v1.json` SHA **0108335bbbe2d35214761904172490bbbed6976d59dd19748aaa7843276dc9e5** is checked by the separately written original-vector checker SHA **40f201ed11f598afada8091ac59b7fe5865b7d75acd5bf5764b4024550a4ed47**: 100/100 norms and all30 basis orthogonalities exactly; 10 actual transversal labels; 13 rays and387 parallel cell pairs. It is an exact proper-cardinality object, NOT the 100-ray goal.

**SMT model caution.** `frontier-20261028-two-pocket-smt-v1.py` SHA **b31ee3b9bf51823ef610e53b95f74f0867f8d5e6b67a480cf0b2b9ec301bcd2b**, output `frontier-20261028-two-pocket-smt-result-v1.json` SHA **29aa9d148e27ede6996e7eaccf5489546fdfecdd68127f7eacc492bdc266a567**, returned `unsat` for two normalized trial configurations. BOTH models also accidentally force `A[0,3]=A[3,3]=3`, violating column-Latinness independently of the desired pocket condition. Therefore those solver outcomes are **INVALID as independent evidence for the general subarray theorem or a global obstruction**. The broken ansatz and its bytes are preserved; Theorem B was derived separately in §3. This explicit failure is not relabeled as a successful all-instance proof.

## 5. Exact scope and next step

Theorem B shows that the tempting plan “find two disjoint OA(3) pockets in a classical OLS(10), rotate them independently and obtain at least16 rays” cannot work. It does NOT exclude overlapping OA(3) pockets, closed pair switches which are not whole subarrays, differently shaped local trades, nonclassical incidences, nonlocal components or arbitrary exact arrays. Nor does the exact13-ray object/locally complete neighborhood settle existence or nonexistence of100 rays. The next meaningful route must escape the proved classical-disjoint-pocket and local-reference obstructions while retaining SAME-array row/column/transversal Gram constraints.

Written proof, the literal source-table transcription and finite checks require independent review before adoption. No held prior outcome is a premise; no external model, secrets, deletion, publication or infrastructure action. The original 10×10/100 pairwise-nonparallel-ray target remains OPEN.

**END — universal restricted-construction obstruction; no global QLS10 conclusion.**
