# Shor completion: two remaining border sizes at order 1320

Owner **MathShor-2**, math-5. Actual clock of independent finite replay: **Wed Oct 28 19:23:09 PDT 2026**.
**Conditional written reduction with two independently implemented exact finite counts; not an order-1320 exclusion, unrestricted no-go, formal proof or novelty clearance.**

## 1. Result

For a hypothetical finite UD factor-complete extension of the original Shor code with actual pure-a order1320, the same-code direct border factorization must satisfy

    (|P|,|Q|) in {(24,55),(44,30)}.                            (1)

The preceding `frontier-20261028-1320-three-border-sizes-v1.md` gave `(20,66),(24,55),(44,30)`. Here we exclude `(20,66)` because both P and Q would have a difference with gcd264 against1320, contrary to the independently reconstructed necessary direction of the classical Sands divisor-class theorem. The two remaining pairs are NOT asserted feasible; n=1320 remains OPEN.

## 2. Why P must use gcd class264

If `|P|=20`, 5 divides |P| and not |Q|, so the elementary prime-balance argument forces four P-elements in EACH residue class modulo5. The old-anchor candidate screen from the divisor-class predecessor gives exactly these six candidates in class2 and six in class4:

    class2: 132,407,792,872,987,1067
    class4: 264,344,459,539,924,1199.

The following are six disjoint cross-class pairs, each with gcd-difference exactly264:

    (132,924), (407,1199), (792,264),
    (872,344), (987,459), (1067,539).

Selecting four from each six-set selects eight endpoints from six pairs, so P necessarily selects both endpoints of at least one. Thus gcd264 occurs among P differences. These literal lists and all six gcd values were checked by the pinned finite program below.

## 3. Why Q must also use gcd class264

Suppose instead that Q avoids gcd264. From `|Q|=66`, prime balance forces exactly6 Q-elements in each class modulo11 and exactly22 Q-elements congruent1 modulo3. The old-anchor gcd screen C_Q contains no residue4 modulo6, so every Q-element congruent1 modulo3 is odd.

Under the no264 assumption, two distinct `1 mod3` Q-elements cannot share `(mod11,mod8)`: they would differ by a nonzero multiple of264=8*3*11, whose gcd with1320=264*5 is exactly264. Thus there are at most four such elements in any fixed mod11 class. In each of the mod11 classes1,2,7, six Q-elements are required, so each class has **at least two** elements not congruent1 modulo3.

The exact old-anchor candidate screen has ten such non-1 elements in each of these three mod11 classes. Any actual Q therefore admits a six-element seed, choosing two from each list: `C(10,2)^3=91,125` possibilities. The following is a RELAXED finite necessary test, so rejecting every seed is enough:

1. Reject a seed if its elements or old anchors have a gcd difference in `{3,5,8,11,264}`. Exactly1,143 seeds remain.
2. Partition all individually compatible `1 mod3` candidates into their44 possible `(mod11,mod8)` slots. A slot is open if at least one candidate in it avoids those forbidden gcd classes against the seed. Ignore any further conflicts, including possible slot-candidate conflicts against old anchors in class264; this can only increase the number of open slots. For1,089 seeds fewer than22 slots are open, impossible.
3. For each of the remaining54 seeds, at least one required mod11 class cannot supply six total elements: even if every open `1 mod3` slot is occupied, the seed plus ALL individually seed/anchor-compatible remaining non-1 candidates in that class is still insufficient. This test ignores mutual conflicts among those extra candidates, again only relaxing the requirement. There are zero residual seeds.

Thus any Q satisfying its actual anchor, cardinality and prime-balance requirements must use gcd264. This contradicts §2 and Sands disjointness.

## 4. Exact independent counts and consequences

The bitset implementation `frontier-20261028-1320-forced-264-check.py`, SHA256 `7dcf4ce407c2e13178db3e774d7c4518aca6364687f208011aba49c6ef79a6a3` (53 LF, 2931 bytes), reported `91,125 / 1,143 / 1,089 / 54 / 0` for seeds, compatible seeds, slot rejections, quota rejections and residuals. It also checks the P matching.

The independently written set-based implementation `frontier-20261028-1320-forced-264-replay.py`, SHA256 `f9f237d6c1da97124992aba49fd05b73774f0140fc4e7ebc19bb9ad2dc19d640` (36 LF, 2030 bytes), reconstructs the Q candidate screen, compatibility relation and slots and returned exactly the same five counts. Neither program is a formal proof or independent-model-family review.

From (1), `|P|>=24` and `|Q|>=30`. The previously written same-D graded bounds therefore say that `N_out<264` forces at least20 actual multi-b suffix-border atoms and `N_Y<220` forces at least25 actual multi-b prefix-border atoms; if both strict inequalities hold, these are at least45 distinct multi-b atoms. No completion is constructed.

## 5. Scope

All prime balance, actual border factorization and gcd-class disjointness premises are explicitly named and established in the preceding packets, with Sands' theorem and the classical border theorem credited as prior. The finite count is exact, nonvacuous (`1,143` compatible seeds) and checked by two different same-harness implementations, but has not been peer-reviewed, formally verified, independently model-family reviewed or novelty screened. The original finite UD factor-completion problem remains OPEN.

**END OF TWO-SIZE ORDER-1320 REDUCTION.**
