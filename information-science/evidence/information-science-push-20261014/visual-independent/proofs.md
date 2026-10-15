# Independent finite visual-cryptography decisions

Date: 2026-10-14 PT. This directory was developed from the task's access structures and probability model, without reading `ai4s/visual-cryptography-optimality/` or `ai4s/evidence/`. It is a new derivation, not a replay of their certificates. The result concerns arbitrary probability distributions, not only single basis-matrix pairs.

## Reproduce

From any working directory:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-visual-cryptography-optimality/venv/bin/python /Users/jinleic/jinleic-workspace/scratch/ai4s-visual-independent-20261014/run_all.py
```

The command compiles the small C++ orbit enumerator, regenerates the six decisions and their certificates, finds the two positive-control basis pairs, constructs the expected-count counterexample, and runs a separate certificate-only checker. It writes `results.json` and `verification.json`. It does not install packages, access the network, invoke Git, or read another project's proof artifacts. NumPy and SciPy were checked to be present in the prescribed Python environment. BLAS and HiGHS are explicitly single-threaded; the driver runs jobs sequentially and records peak process memory.

`results.json` is the canonical result and includes candidate counts, all branch counts, the actual nonzero integer certificate terms, timings, exact-check results, and hashes of the files used. `case*_decision.json` contains the full proof trees. `expected_count_control.json` contains the compact rational counterexample. The earlier `relaxed_*` scripts and `case0_*` universes are discovery artifacts, not inputs to the reproduction command or grounds for the six negative decisions.

## 1. Model and orbit reduction

Participants 1 through 5 are bits 0 through 4. A column is an integer from 0 through 31. For a sorted length-m tuple A of columns, define

- `weight(Q,A) = #{c in A : c & Q != 0}`;
- `projection(F,A) = sorted(c & F for c in A)`.

All supersets of a stated minimal qualified set are qualified; all other subsets, including the empty set, are forbidden. All qualified sets, not just minimal ones, are used for contrast.

Apply a uniformly random common column permutation independently on each encoding. This preserves every OR weight and preserves equality of each forbidden observer's ordered-matrix distribution. Conditional on a column multiset, the resulting full matrix is uniform over its distinct column orderings. Its F-projection is uniform over the distinct orderings of the projected multiset. Thus two symmetrized distributions have the same ordered F-view exactly when their distributions on complete projected multisets agree. Consequently, searching distributions over column multisets loses no scheme and introduces no spurious scheme.

There are exactly C(m+31,m) column multisets. A recursive nondecreasing-column enumeration visits each exactly once: the first column is chosen in 0..31 and every later column is chosen between its predecessor and 31. This is the standard unique sorted representative of each multiset; no participant symmetry reduction is used.

## 2. Maximal forbidden sets suffice

Every forbidden F is contained in an inclusion-maximal forbidden G. The F-projected multiset is the deterministic image of the G-projected multiset under masking by F. Equality of G-projection distributions therefore implies equality for F. Checking all maximal forbidden sets is sufficient. Conversely, every maximal forbidden set is forbidden, so using it in any necessary condition is legitimate. The positive-control checker explicitly checks *all* forbidden sets.

## 3. White-orbit zero-column filter

The full participant set U=31 is qualified in every instance. If a white-support orbit W contained no zero column, `weight(U,W)=m`, while every black matrix has weight at most m. This contradicts black weight at least white weight plus one. Every white-support orbit must therefore contain column zero.

Every sorted orbit containing zero is enumerated uniquely by fixing its first entry to zero and choosing the remaining m-1 entries nondecreasingly. Its count is C(m+30,m-1). No restriction on the number of additional zero columns is imposed.

## 4. Necessary black-orbit coverage filter

Fix a black-support orbit B, a qualified Q, and a maximal forbidden F. Since B has positive probability, its full F-projection event has positive black probability. Security forces positive white probability on the same event, so some white-support orbit W has the same projected multiset.

The set Q intersect F is contained in F, hence

`weight(Q intersect F,W) = weight(Q intersect F,B)`.

Monotonicity of OR stacking and contrast give

`weight(Q,B) >= weight(Q,W)+1 >= weight(Q intersect F,B)+1`.

The difference on the two ends is exactly the number of columns c of B satisfying

`c & Q != 0` and `c & (Q & F) == 0`.

At least one such column must occur. For each pair (Q,F), the enumerator constructs the 32-bit set of allowed column values and requires the orbit's set of present values to intersect it.

Duplicate obligations can be merged. If an obligation contains another obligation as a subset, meeting the smaller one already meets the larger one, so retaining only inclusion-minimal obligations is equivalent to retaining all of them. Multiplicity does not matter for this particular existence test; it remains part of every orbit and projection elsewhere.

This filter crucially uses a positive-probability *whole projection event*. Equality of expected column counts does not justify the matching W. Accordingly, the expected-count control does not use this filter.

## 5. Preliminary white projection filter

After the necessary black filter, for each maximal forbidden F, retain the signatures `projection(F,B)` of all surviving black orbits. A white orbit whose F-signature does not occur cannot be in a scheme: its positive white event probability would require a positive black event probability. This argument uses only a superset of all possible black-support orbits, so it is safe before any contrast-compatible matching is imposed.

## 6. Iterated support pruning

For current white candidates S0 and black candidates S1, call W and B compatible when

`weight(Q,B) > weight(Q,W)` for every qualified Q.

For every maximal forbidden F, mark a candidate if it has at least one opposite-color candidate that is compatible and has the same complete F-projection. Delete a candidate if it is unmarked for at least one F. Each round is synchronous; the recorded per-F matching counts and resulting counts describe the whole round.

**Safety proof.** Suppose a genuine scheme's positive supports are contained in S0 and S1. For any support orbit and forbidden F, security supplies an opposite-color support orbit with the same projection, as in Section 4. Every white-support/black-support pair of the scheme is compatible by the stated contrast requirement. Thus each true support orbit is marked for every F and survives the round. Induction proves that no sequence of these deletions can remove a genuine support orbit. A fixed point is only a necessary condition, not a proof of existence. If either color becomes empty, no pair of normalized probability distributions exists.

## 7. Exhaustive integer-threshold branching

For any nonempty genuine white and black supports and qualified Q, set

`t_Q = 1 + max_W weight(Q,W)`.

Integral weights and strict all-pairs contrast imply `1 <= t_Q <= m` and

`weight(Q,W) < t_Q <= weight(Q,B)`

for every support W and B. Conversely, these inequalities imply contrast at Q. Hence branching over every integer t in 1..m, retaining white weights below t and black weights at least t, covers every possible scheme. An empty child is impossible. Children with exactly identical candidate sets can be merged without changing the covered possibilities.

A split is needed only if some current white/black pair conflicts at a qualified Q. For such a Q, every nonempty child removes at least one candidate: otherwise all current candidates would already be separated at t. The finite search therefore cannot descend forever. The implementation records all m threshold counts, including discarded empty cases, and the certificate-only checker checks the coverage.

For case 5 at m=7 the successful run needs only one split, at mask 7 = participants {1,2,3}. Thresholds 1,2,3 have empty white sets; the surviving thresholds are 4,5,6,7. Threshold 4 is killed by support pruning. Each of thresholds 5,6,7 has an integer separating functional after pruning. No symmetry assumption on the different qualified-set thresholds is made.

## 8. Full-projection feasibility and exact separation

For an orbit A, let phi(A) have one coordinate for each pair (F,p), with F maximal forbidden and p a complete projected multiset: its value is 1 if `projection(F,A)=p`, otherwise 0. Equality of expected phi is *exactly* equality of the complete projected-multiset distributions; it is not equality of expected column counts.

For finite candidate lists, security and normalization have the rational linear formulation

`sum_W a_W phi(W) = sum_B b_B phi(B)`,

`sum_W a_W = sum_B b_B = 1`, with all coefficients nonnegative.

It is a necessary relaxation even when the candidate sets still contain cross-color contrast conflicts. If all remaining cross-color pairs are compatible, it is also sufficient. A feasible rational solution at such a leaf is a scheme; its distribution and contrast are checked exactly before acceptance. Rational feasibility is enough because this is a rational polytope.

A negative leaf is certified by an integer functional

`L(A) = constant + sum_(F,p) coefficient(F,p) * 1[projection(F,A)=p]`

with `L(W) >= 1` on *every* surviving white orbit and `L(B) <= 0` on *every* surviving black orbit. Security would imply `E_white L = E_black L`; normalization preserves the common constant. The displayed inequalities instead imply `E_white L >= 1 > 0 >= E_black L`, a contradiction for arbitrary real probabilities.

SciPy/HiGHS is used only to discover a candidate functional. Its coefficients are scaled and rounded, the additive constant is adjusted using the exact black maximum, and the resulting integer coefficients are checked using Python unbounded integers on every surviving orbit. A floating infeasibility status alone is never a negative certificate. Inability to reconstruct an exact certificate causes an error, not a NO verdict. The separate checker parses the serialized terms and recomputes the projected tuples and inequalities without calling an LP optimizer.

## 9. Six full-model decisions

The following counts are structural, not floating solver results. Counts after the preliminary filters and after root support pruning are written as (white,black).

| Case | m | All orbits | White orbits with zero | Black coverage survivors | Preliminary survivors | Root pruning survivors | Final reason |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 5 | 376,992 | 52,360 | 66 | (624,66) | (0,0) | Empty support |
| 2 | 6 | 2,324,784 | 376,992 | 1,053 | (5788,1053) | (0,71) | Empty white support |
| 3 | 5 | 376,992 | 52,360 | 3 | (24,3) | (0,0) | Empty support |
| 4 | 6 | 2,324,784 | 376,992 | 144 | (3148,144) | (54,44) | Integer projection-event separator |
| 5 | 6 | 2,324,784 | 376,992 | 854 | (1103,854) | (0,15) | Empty white support |
| 5 | 7 | 12,620,256 | 2,324,784 | 14,482 | (42201,14482) | (1895,1284) | Exhaustive threshold split and exact leaf proofs |

All six verdicts are **NO**. These agree with the claims under test. The full nonzero certificate terms, their minima/maxima, and their orbit coverage counts are in `results.json` and the decision files. No bound on support size, probability denominator, or use of a single basis pair was used for these negative results.

## 10. Positive controls under full security

For case 1 at m=6 and case 5 at m=8, `witness_search.py` solves an integer column-count formulation for a single white/black basis pair. This is a construction search, not a substitute for the arbitrary-distribution impossibility proof. Uniformly permuting the columns of each basis matrix yields distributions on ordered matrices.

Before reporting a witness, both the constructor and the separate checker verify in exact arithmetic:

1. Both column multisets have length m and use masks 0..31.
2. Their complete projected multisets are identical for *every forbidden F*.
3. Black OR weight exceeds white OR weight for *every qualified Q*.

The constructed columns are recorded in `basis_controls.json`. For example, the independent search found case 1 at m=6 with white `[0,0,15,15,22,24]` and black `[3,5,8,14,18,28]`, and case 5 at m=8 with white `[0,2,7,11,19,29,30,30]` and black `[1,3,6,10,18,28,31,31]`. A solver version may return a different exactly verified pair.

## 11. Expected-count relaxation changes a verdict

Case 5 at m=7 is **YES** if only security is weakened to equality of expected projected column counts, while retaining the original all-support contrast requirement. This is an explicit counterexample, not an inference from an LP status.

Let P be the six two-element subsets of participants {2,3,4,5}, encoded as masks `{6,10,12,18,20,24}`. The following probabilities refer to complete column multisets; each can subsequently be uniformly permuted.

White distribution (8 orbits):

- For each p in P, `[0,0,1|p,1|p,1|p,1|p,1|p]`, probability 1/10 each.
- `[0,0,31,31,31,31,31]`, probability 1/10.
- `[0,0,30,30,30,30,30]`, probability 3/10.

Black distribution (3 orbits):

- `[0,1,1,1,1,1,1]`, probability 1/4.
- `[0,31,31,31,31,31,31]`, probability 1/4.
- `[6,10,12,18,20,24,31]`, probability 1/2.

Every white orbit has weight 5 at every qualified set. The first two black orbits have weight 6 at every qualified set. In the third black orbit, a minimal qualified set (participant 1 plus two leaves) misses exactly one leaf-pair column and has weight 6; every larger qualified set has weight 7. Thus **every** black/white support pair meets the original contrast requirement.

The expected black-minus-white column counts are:

- -3/2 at column 0 and +3/2 at column 1;
- +1/2 at every p in P and -1/2 at every `1|p`;
- -3/2 at column 30 and +3/2 at column 31;
- zero elsewhere.

Every forbidden set is either a subset of the leaves, or participant 1 together with at most one leaf. For a leaf-only set, each displayed leader-bit pair has identical projection and cancels. For participant 1 and a fixed leaf, three of the six p contain that leaf and three do not; their projected contributions cancel the 0/1 and 30/31 contributions exactly. Smaller forbidden sets follow by projection. Expected projected column counts therefore agree for every forbidden observer.

Full-distribution security fails already for the forbidden singleton {1}. The probability that all seven of participant 1's entries are white is 3/10 under the white secret and 0 under the black secret. Equal expected row weight (7/2 on both sides) plainly does not repair this leak. `expected_control.py` constructs this distribution, and exact `Fraction` arithmetic checks normalization, all forbidden expected counts, and every all-support contrast inequality.

## 12. Trust boundary and scope

These are finite mathematical certificates checked by ordinary integer/rational computation. They are not Lean/kernel certificates and do not claim a uniform solution for arbitrary numbers of participants. The remaining trusted implementation consists of the stated finite enumeration, Python/NumPy integer operations, and the C++ compiler/runtime. The detached checker uses a different projection representation and a different compatibility-loop organization from the search. Its negative conclusions rely on serialized exact terms and exhaustive branch coverage, not on floating LP tolerances. The positive and relaxed controls test both sides of the model distinction explicitly.
