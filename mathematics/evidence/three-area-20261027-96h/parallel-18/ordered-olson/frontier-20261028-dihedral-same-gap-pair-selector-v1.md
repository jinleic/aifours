# Same-gap rotation exchanges give an actual ordered selector near the high-rotation boundary

Owner **MathOlson-2-2**, original math-2. Actual native `/bin/date` observation before this write: **Wed Oct 28 17:26:19 PDT 2026**.
**Written all-prime candidate; bounded scientific verification is not yet performed for this new statement. Not an all-word theorem or a novelty claim.**

## Exact theorem

Let p be ANY odd prime and let an ACTUAL word of length4p−1 in `D_(2p)=<r,s | r^p=s²=1,srs=r^−1>` have R rotations and F reflections.
Assume `R≥3p−3` and `F≥2`.
Split the actual rotation occurrences into their maximal gaps between consecutive reflection occurrences, including the boundary gaps before the first and after the last reflection.
Suppose these gaps contain **p−1 disjoint pairs** of rotation occurrences such that each pair lies in ONE gap and its two exponents in F_p are distinct.

Then for **ANY specified pair of actual reflection positions** i<j, one can choose exactly2p−2 ACTUAL rotations so that those two reflections and those rotations, read in the original order, multiply to1. Thus the original word has an identity selector of exactly2p occurrences.

In the original unresolved intermediate envelope `R≤3p−2`, this supplies a genuine all-prime conditional word class at `R=3p−3` and `R=3p−2`. It does NOT prove that every word there has the p−1 pairs; cases outside the condition remain open by this argument.

## Proof with actual indices and no flattening

Write every rotation as r^x and each reflection as r^y s. Fix the actual two reflections i<j.
Assign sign +1 to rotations before i or after j and −1 to rotations strictly between them. The chronological product of the fixed reflections and ANY actual chosen rotations is the rotation with exponent

`y_i−y_j + sum_(chosen rotations a) σ_a x_a`.

This follows directly from `s r^x=r^(−x)s`. Because the two occurrences in each prescribed pair have NO reflection between them at all, they have the SAME sign σ for this fixed i,j. Their signed exponents are distinct.

Put `t=R−(2p−2)`. The hypothesis gives t≥p−1. Select the p−1 disjoint unequal-exponent pairs. Exactly `R−2(p−1)=t` rotations lie outside them, so choose any `t−(p−1)` of those outside rotations as fixed omissions. From each pair omit exactly ONE of its two actual positions. The total number of omitted rotations is t, leaving exactly2p−2.

For one pair, changing which position is omitted changes the signed omitted sum by some nonzero δ∈F_p. Across the p−1 disjoint pairs, all choices are simultaneously realizable and produce a translate of the subset-sum set of p−1 nonzero increments.
For ANY nonempty proper A⊊F_p and nonzero δ, `A∪(A+δ)` has at least |A|+1 elements: otherwise A would be invariant under translation by δ, which generates all F_p. Starting with a singleton, successive pair choices thus give at least `min(p,1+(p−1))=p` attainable omitted signed sums.
The fixed omissions contribute only a constant. Hence EVERY target signed sum occurs, in particular the one making the full actual exponent zero. The retained2p−2 rotation positions together with i,j give exactly2p distinct original indices and product1.

No independence of interleaved packet products, arbitrary reordering, selected formal coefficients or equation for nonexistent occurrences is assumed.

## An exact occurrence-count version of the hypothesis

For one actual reflection gap g let r_g be its number of rotation positions, and let M_g be the largest multiplicity of a rotation exponent in that gap; put M_g=0 if the gap is empty.
The maximum number of disjoint unequal-exponent pairs in the gap is exactly

`c_g=min(floor(r_g/2), r_g−M_g)`.

Both quantities are upper bounds. If the most frequent value occurs more than half the time, pair each minority occurrence with a distinct majority occurrence, attaining r_g−M_g.
Otherwise pair two currently most frequent distinct values and repeat. The largest remaining count never exceeds the ceiling of half the remaining occurrences: if the previous maximum was exactly that ceiling it is among the two reduced values, and in the even tie case both maximal values are reduced. Induction pairs all but at most one occurrence, attaining floor(r_g/2).

Consequently the theorem's pairing hypothesis is EQUIVALENT to the exact ACTUAL gap statistic

`sum_g min(floor(r_g/2), r_g−M_g) ≥ p−1`.

This equivalence is only a restatement of the explicit pairing hypothesis; it does NOT establish that all actual words meet it.

## An all-prime family outside the previous fixed-I and saturated-pair criteria

For any prime p≥5 take the FULL actual word

`(r, r²)^(p−1), (s, r)^(p−1), s,s,s`,

where the powers denote separately labelled repetitions. It has R=3p−3, F=p+2 and length4p−1; ALL rotation exponents are nonzero.
The initial reflection gap contains p−1 disjoint unequal pairs, so the theorem applies.

It has an explicit actual selector: choose r² from two of those pairs and r from each of the other p−3 pairs, then all p−1 later r occurrences, and finally choose two s reflections from the final three consecutive s's. The selected rotations, which all precede those two reflections, sum to2p≡0; their EXACT original-order product is therefore r^0ss=1. This uses exactly2p−2 rotations and two reflections, with no reordered indices.

For comparison at the DIFFERENT fixed I consisting of the first2p−2 rotations, their sum is `3(p−1)≡−3≠0`; all reflections occur after that I and equal s, so all I-prefix potentials coincide. The earlier fixed-I zero-sum/full-support and cross-cut support>p criteria therefore do not apply at that I.
The quotient pattern has2p−1 odd runs, so the earlier saturated separated-pair criterion also does not apply. This demonstrates strict improvement over those named certificate conditions, not uniqueness of the new selector or failure of any other method.

## Verification and limits

The all-variable proof and gap matching lemma are written above. **No bounded checker has yet been run for this new candidate**; it was pinned at the requested transition to the priority f30 review. The latest owner directive permits a subsequent exact check and independent review; no numerical result is claimed here.
The original full D_(2p) problem, lower rotation bands and all-finite-group target remain unresolved. No actual avoiding word, full-band closure, publication, formal/human/configured-family verification or novelty claim is made. Historically quarantined outputs are not accepted as premises; this proof uses only the stated actual group law and elementary prime-field counting.

**END — same-gap unequal-pair original-order selector candidate.**
