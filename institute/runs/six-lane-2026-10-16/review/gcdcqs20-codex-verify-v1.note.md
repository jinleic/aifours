RESULT: VALID

Both SHA-256 hashes match their supplied pins. An independent in-memory verifier passed both inputs; no excluded checker or claimant code was accessed.

For **each input**, all 100,289 non-comment lines were consumed. Verified:

- Four disjoint groups, exactly `0–19`, `20–39`, `40–59`, `60–79`.
- 19,400 distinct valid blocks; none contains three group mates.
- Coverage equals the explicitly constructed set of 77,600 eligible triples, each exactly once; no group triple occurs.
- Exactly one section per point. Each lists its exact 970 derived triples once, partitioned into 40 nonempty classes of disjoint triples avoiding that point.
- Exactly ten hole-free classes at every point.

At **every point in both inputs**, class sizes are **10 once, 20 nine times, 26 thirty times**. The ten hole-free classes have sizes 10 once and 20 nine times.

| Input | Block pattern 2+2 | 2+1+1 | 1+1+1+1 |
|---|---:|---:|---:|
| A | 5,640 | 11,520 | 2,240 |
| B | 5,760 | 11,280 | 2,360 |

From [(1.1)](/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt:110) and the [gcSTS definition](/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt:211), since \(79\equiv1\pmod6\),
\[
r=\chi'(79)=(79+1)/2=40,\qquad s=40-(79-19)/2=10.
\]
“At least \(s\)” gives the same requirement here. Each of the 19 hole points occurs in \(60/2=30\) triples, giving 570 hole incidences. If \(k\) classes are hole-free, disjointness implies
\[
570\le19(40-k),\quad\text{hence }k\le10.
\]
More than ten is impossible.

For **A**, exhaustive testing of all 480 requested maps found precisely
\[
\sigma\in A_4,\qquad c\in\mathbb Z_{20}.
\]
Thus the stabiliser **within this family** is \(A_4\times C_{20}\), of order **240**, acting transitively on all 80 points.

All eight in-memory corruption controls were rejected as intended:

| Corruption to A | Rejection |
|---|---|
| Swap 20 and 21 between two blocks, preserving block count and group patterns | Four eligible triples uncovered |
| Move `(22,42,62)` at point 0 from class 0 to 1 | Intersecting triples |
| Move `(6,34,72)` from class 10 to 0, retaining disjointness and all derived triples | Only nine hole-free classes |
| Drop one colouring triple | 969 derived triples |
| Replace a block with another existing block | Duplicate block |
| Change `COLOURS` to 39 | Incorrect colour count |
| Change `HOLEFREE` to 9 | Incorrect hole-free parameter |
| Append non-comment garbage | Invalid trailing line |

No material definition gap remains: the source permits **partial** parallel classes, so the size-10 class is allowed; the empty stem makes its stem-point condition vacuous. These checks establish the requested gcDCQS\((20^4:0)\) property.

The inputs are **different designs by block-set equality**: they share 360 blocks, with 19,040 blocks exclusive to each.