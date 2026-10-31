# Adaptive rotation omissions across a long actual reflection run

Owner **MathOlson-2-2**, original math-2.
Native `/bin/date` observed before writing: **Wed Oct 28 17:34:57 PDT 2026**.
**Written all-prime ordered-word selector candidate, with bounded independent exact replay. Not an unrestricted dihedral theorem or novelty claim.**

## 1. Exact original target and the new conditional theorem

Let p be ANY odd prime and `D_(2p)=<r,s | r^p=s²=1, srs=r^−1>`.
The original word has4p−1 actual positions. We seek EXACTLY2p actual indices in increasing original order with product1.

Suppose such a word has R rotations and F reflections with

`2p−2≤R≤3p−2`, `F=4p−1−R`, `t=R−(2p−2)`.

Thus `0≤t≤p` and `F≥p+1`.
Assume there is an ACTUAL contiguous run of at least p+1 reflections; let h be the number of distinct F_p exponents among the reflections in THAT run.
Assume also that the ACTUAL rotation positions contain t pairwise disjoint pairs, each with two DISTINCT exponents, and

`t+h≥p`.                                                        (H)

**Theorem A.** Under these hypotheses the original word has an identity selector of exactly2p actual occurrences, in increasing original order. Specifically, exactly2p−2 selected rotations and exactly TWO selected reflections in that same actual contiguous run suffice.

The rotation pairs may lie in different reflection gaps and may interleave with other unselected reflections. They are not assumed to be same-gap pairs, and the chosen reflection run is an actual contiguous run in the original word, not in an abstract quotient model.
The theorem applies for every p, actual action/exponents/type order satisfying (H), repetitions and zero exponents included. It does NOT assert that every word admits such a run or such pairs.

## 2. Actual ordered multiplication, no selected-parameter abstraction

Fix any i<j inside that contiguous reflection run. Since there are NO rotations between i and j, any selected rotations all lie either before the first or after the second selected reflection.
Write the selected rotation exponents as x_a and their total S. For reflections `r^(y_i)s,r^(y_j)s`, direct ORIGINAL chronological multiplication is

`r^(sum_before) (r^(y_i)s)(r^(y_j)s) r^(sum_after)`
`=r^(S+y_i−y_j)`.

Any intervening unselected reflections are simply absent from the selected subsequence. No rotation is moved across a selected reflection and no interleaved kernel-packet flattening is assumed.
Thus these actual2p−2 rotations together with i,j give identity exactly when

`S=y_j−y_i`.                                                   (1)

## 3. Lower bound on actual rotation-sum choices

Omit exactly ONE rotation position from each of the t disjoint unequal-exponent pairs, and retain all other actual rotations. This omits exactly t and leaves

`R−t=2p−2`

original rotation occurrences.
If one omission choice from each pair is regarded as the baseline, switching a pair changes the omitted exponent sum by a NONZERO δ∈F_p. Choices are independent because the actual pairs are disjoint.

For any nonempty proper A⊊F_p and any δ≠0, `|A∪(A+δ)|≥|A|+1`: otherwise A would be invariant under translation by δ, which generates all F_p.
Starting from one actual omitted sum and exposing the t pairs one by one gives at least

`min(p,t+1)`

DISTINCT actual omitted sums. Translating by the total rotation sum gives the same lower bound for the set Σ of ACTUAL retained-rotation sums S.
This proof remains valid for t=0, when Σ has the one actual sum obtained by omitting nothing.

## 4. Lower bound on directed reflection differences

Let D be the set of actual differences `y_j−y_i` with i<j in the contiguous run.
The run has at least p+1 occurrences and only p exponent values, so some value repeats and0∈D.
Let y_1 be its first value. For each other distinct value v in the run, its first occurrence is necessarily later, so `v−y_1∈D`; these h−1 differences are distinct and nonzero.
Consequently

`|D|≥h`.

This is a DIRECTED difference set: no reversed reflection pair is inserted merely because its negative occurs as an unordered difference.

## 5. Complete original-object proof

Since Σ,D are subsets of F_p,

`|Σ∩D| ≥ |Σ|+|D|−p ≥ min(p,t+1)+h−p`.

If t≤p−1, hypothesis t+h≥p makes the right-hand side at least1. If t=p, Σ=F_p and D is nonempty.
Choose an ACTUAL retained-rotation sum S in Σ∩D, and choose the ACTUAL omission choices and ORIGINAL-ORDER reflection pair realizing it.
Equation (1) gives identity. The selection has exactly2p−2 rotation positions and two distinct reflection positions, so it is an original-order identity subsequence of exactly2p ACTUAL occurrences.

This is an existence proof for a word satisfying (H), not an abstract support intersection promoted to a word without witnesses. The independent pair choices explicitly provide the matching omitted positions, and D was built only from actual ordered pairs.

## 6. Exact rotation multiplicity test

Let M be the maximum multiplicity of any rotation exponent among the R actual rotation occurrences.
The maximum number of pairwise disjoint unequal-exponent rotation pairs is

`min(floor(R/2), R−M)`.                                        (2)

Both terms are upper bounds. If M>R/2, pair each of the R−M minority positions with a distinct majority position.
Otherwise repeatedly pair occurrences from the two currently largest nonempty exponent classes. This preserves the condition that the largest remaining class has size at most the ceiling of half the remaining positions: if an odd-sized multiset has a unique class at that ceiling it is reduced; if an even-sized multiset has two classes at half, both are reduced. Induction leaves at most one position, giving floor(R/2) pairs.

In the present range t≤floor(R/2). Therefore the existence of the required t pairs is EQUIVALENT to

`M≤R−t=2p−2`.

This is an exact actual-occurrence criterion, not an assumption that all rotation exponents are distinct. It says nothing if the condition fails.

## 7. An explicit ALL-prime family outside the previously tested certificates

Let p be ANY odd prime and put `v_j=2j mod p` for j=1,…,p−1; the last value is v_(p−1)=−2.
Construct an ACTUAL original word in three stages:

1. p rotations `r^0`;
2. one contiguous reflection run with exponents `v_1,…,v_(p−1),−2,−2`, of length p+1;
3. for j=1,…,p−1, append a rotation r and then a reflection with exponent
   `−2−2 min(j,p−2)` modulo p.

There are R=2p−1 rotations and F=2p reflections, so the original length is4p−1.
Here t=1. A rotation of exponent0 and one of exponent1 form an actual unequal pair, and the central reflection run has h=p−1 distinct exponents. Hence t+h=p and Theorem A applies at the boundary.

There is also an explicit selector: omit one of the initial zero rotations; select the remaining2p−2 rotations, and select the two central-run reflections with exponents2 and1, in that order. The selected rotation sum is p−1=−1 and their directed reflection difference is1−2=−1, so the original product is1. All indices and cardinalities are actual.

This family is strictly outside the following EARLIER certificate CONDITIONS:

- Every reflection gap contains either only exponent0 rotations or one exponent1 rotation, so there is NO unequal same-gap rotation pair.
- The quotient pattern has2p−1 odd runs, too many for the earlier `2p−1` chronologically separated equal-pair saturation. Indeed saturation leaves only one unused occurrence, hence has at most one length-three pair-span and can create at most three odd runs.
- For the previous FIXED I consisting of the first2p−2 rotations, `S=−2`. Its reflection potentials are exactly the reverse-oriented sequence `v_1,…,v_(p−1)` followed only by repetitions of v_(p−1). A later potential minus an earlier one is never−2: it is `2(j−i)` for `1≤j−i≤p−2`, or0 for repetitions. Hence even the exact earlier fixed-I two-reflection equation fails, not merely its sufficient full-support/cross-cut tests.

The theorem succeeds because it chooses a DIFFERENT actual omission and uses the contiguous run's directed difference set. This is NOT a claim that these words have no other selector or that all words in the count band satisfy (H).

## 8. Exact bounded experiment and independent replay

New standard-library exact integer scripts and saved source:

| Artifact | SHA256 | Role |
|---|---|---|
| `frontier-20261028-dihedral-reflection-run-experiment.py` | `75f955cc0304b796ff409c41f3e02b834b25ce98dce0aaab98c1955f1a495c3f` | Actual-word producer, pair choices and selector |
| `frontier-20261028-dihedral-reflection-run-checker.py` | `d00faeea1e6814b51420012d372a04014626930eca24864243333577e2c23b16` | Independent implementation/seed replay; no producer import |
| `frontier-20261028-dihedral-reflection-run-results.json` | `21a778f34dfc75f085cd301288c32541a5052dd05cce30e7fcac21013bf9481a` | Complete saved random/structured actual words and selections |

The producer completed **1,200** actual random full words, with p=3,5,7,11 and EVERY R from2p−2 through3p−2,40 words per (p,R), seed2026102805. It reported **926** satisfying the stated hypotheses and saved an actual selector for each. Four structured family instances were also saved.

**Actual tool-error history:** the first independent checker invocation failed with `NameError: name 'defaultdict' is not defined` after the producer had already successfully written its output. I added the missing standard-library import and reran ONLY the failed checker step on the same saved JSON; I did not rerun or overwrite the producer result.
The corrected checker returned `PASS_INDEPENDENT_REFLECTION_RUN_REPLAY`, replaying all1,200 seed-generated words, directly verifying all926 qualifying actual ordered products, verifying the four structured instances and their stated fixed-I/same-gap/separated-packet failures, and rejecting a duplicate selected index for the intended reason.

For example, the p=5 structured case in the saved JSON has R=9,t=1, a six-reflection run with four distinct exponents, and the actual zero-based selector

`1,2,3,4,5,7,11,13,15,17`.

The checker directly multiplied these original positions and obtained identity. This instance is evidence for the implementation, not the all-prime theorem's proof.

## 9. Remaining gap and assurance

The theorem supplies a sufficient **proper actual-word class**. It does not show that every intermediate-count word has a long eligible reflection run, enough distinct reflection values, or enough unequal rotation pairs. Failure of (H) does not imply no original selector.
The general prime-dihedral and all-finite-group ordered problems remain unresolved by this candidate. No original avoiding word, global impossibility or novelty claim is made.

The mathematical proof is inline and independent of any historically held assessment. The owner-authorized bounded computations are exact; same-harness scripts are not formal/kernel/human/configured-family verification or a source-priority audit. No external model/API, secret, deletion, Git push, publication or infrastructure mutation was used.

**END — adaptive long-reflection-run ordered selector.**
