# Shor completion: four remaining border sizes at order 1320

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Wed Oct 28 19:15:15 PDT 2026**.
**Conditional written deductions with exact finite gcd/identity checks; not an exclusion of n=1320, a full completion/no-go, a formal proof or novelty clearance.**

## 1. Result and imports

Assume a finite UD factor-complete extension D of the original Shor code has actual pure-a order1320. Its same-code direct border factorization has old anchors

    A={0,3,8,11} subset P,   Y={0,1,7,13,14} subset Q.

The predecessor `frontier-20261028-1320-divisor-class-obstruction-v1.md` reconstructs the necessary direction of Sands' divisor-class theorem, verifies `|P|<=80, |Q|<=130`, and reduces `|P|` to

    {12,15,20,22,24,30,33,40,44,55,60,66}.                    (1)

Using the exact local residue counts and four-pair witnesses below, (1) further reduces to

    |P| in {12,20,24,44},    |Q| in {110,66,55,30},           (2)
    |P|>=12,  |Q|>=30.

All four pairs remain open here. In particular this packet does **not** exclude n=1320.

## 2. Necessary prime balance and individual candidate sets

Because the primes3,5,11 each divide1320 to the first power, exactly one of |P| and |Q| is divisible by each. At the corresponding primitive prime-th root, the other mask polynomial cannot vanish because its value at1 is prime-coprime. Thus the divisible side vanishes and is uniform modulo that prime. This is the elementary cyclotomic prime-balance deduction already reconstructed in the border predecessor.

Let `G_A={3,5,8,11}`, `G_Y={1,2,6,12}` be the gcd classes of old head/tail differences. Write `C_P` for all residues individually compatible with A against `G_Y`, and `C_Q` for all residues individually compatible with Y against `G_A`. Every actual P is contained in C_P and every actual Q in C_Q; any two P residues also avoid G_Y, and any two Q residues avoid G_A.

Exact integer enumeration and pair checks in the pinned §6 script give:

* `C_P` has exactly12 residues congruent to1 modulo3:
  `88,253,256,415,418,583,748,913,916,1075,1078,1243`.
* Four disjoint pairs `(88,916),(256,748),(253,415),(583,1075)` each have gcd-difference in G_Y. Thus P has at most8 elements in this mod3 class.
* `C_P` has exactly6 residues congruent to2 modulo5: `132,407,792,872,987,1067`.

If 3 divides |P|, prime balance makes each mod3 class size |P|/3; therefore sizes30,33,60,66 are impossible because they require at least10 in the first class. If 5 divides |P|, mod5 class2 has size |P|/5; therefore sizes40 and55 are impossible because they require8 and11 respectively. Size60 was already eliminated.

## 3. Excluding `|P|=15`

Here P is uniform modulo3 and modulo5: it needs5 elements congruent1 modulo3 and3 elements in each mod5 class. The old heads3,8 already occupy two of the three places in class3 modulo5, so at most ONE new head can have that mod5 residue.

Among the 12 listed mod3=1 candidates, only `256,415,916,1075` are outside mod5 class3. Therefore five selected elements would require all four of these plus one of the other eight. But each of those eight conflicts by a G_Y gcd class with at least one of the four:

| candidate in mod5 class3 | conflicting forced candidate |
|---|---:|
| 88 | 916 |
| 253 | 415 |
| 418 | 256 |
| 583 | 1075 |
| 748 | 256 |
| 913 | 415 |
| 1078 | 256 |
| 1243 | 415 |

This contradicts divisor-class disjointness. So `|P|!=15`.

## 4. Excluding `|P|=22`

Now `|Q|=60`. Since3 and5 do not divide22, Q must be uniform modulo3 and5: exactly20 tails per mod3 class and12 per mod5 class.

Exact finite screening of C_Q establishes that no candidate is `4 mod6`. For each `r in {1,2,3}`, among candidates `q==r mod5` there are exactly10 with `q mod3 != 1`, of which exactly4 are odd. Four disjoint pairs among those10 have gcd-difference5, so a valid Q can contain at most6 of them. The pairs are:

| r mod5 | four gcd-5 conflict pairs |
|---|---|
| 1 | (891,386), (971,276), (561,716), (641,1266) |
| 2 | (627,722), (707,282), (47,612), (1287,1052) |
| 3 | (363,68), (443,618), (693,1058), (773,948) |

Fix one such r. Of its required12 Q-elements at least6 are `1 mod3`. All these are odd, since class4 mod6 is absent. If they all had the same residue modulo11 there could be at most4 of them: fixed residues modulo5,6,11 identify a single class modulo330, with exactly four representatives modulo1320. Thus at least two have distinct mod11 residues.

A selected **even** element in the same mod5 class but not `1 mod3` would have gcd-difference exactly5 with at least one of those two odd `1 mod3` elements: their difference is odd, nonzero mod3 and mod11, and zero mod5. That is forbidden. Therefore all selected elements not `1 mod3` in this mod5 class must be among the four odd candidates, so at least8 of its12 elements are `1 mod3`.

For r=1,2,3 this forces at least24 Q-elements `1 mod3`, contradicting uniform mod3 count20. Hence `|P|!=22`; together with §§2–3 this proves (2).

## 5. Same-code multib consequence

Since (2) gives `|P|>=12, |Q|>=30`, the already written graded tradeoffs imply: if the number `N_out` of actual one-b atoms with heads outside A is `<264`, D must contain at least8 distinct new-head atoms `a^i b^k` with `k>=2`; if the number `N_Y` of actual one-b atoms with tails outside Y is `<220`, D must contain at least25 distinct new-tail atoms `b^l a^j` with `l>=2`. If both strict inequalities hold, these are at least33 distinct atoms: any overlap would be a pure `b^k` with k>=2, forbidden because b itself is an atom. This is a conditional necessity, not an existence claim.

## 6. Independent finite checks and limits

`frontier-20261028-1320-prime-residue-check.py`, SHA256 `fd5bb126e37396ec73681954c9e67205ed8c1ffaa4b8e62d8cf454612181068d` (32 LF, 1753 bytes), enumerates both compatibility sets, checks the two P capacity bounds and all eight P15 blocking edges, confirms that C_Q has no4 mod6, and checks all three Q22 candidate counts and 12 listed gcd-5 edges. Its actual result was PASS for each asserted count/certificate. The check is finite exact integer arithmetic, not a general SAT or formal proof.

The initial 12-size reduction relies on its separately pinned divisor-packing certificate; general Sands divisor disjointness is a named classical import with a written independent proof in that predecessor. The present derivation has not been independently reviewed or novelty screened. The original finite UD factor-completion problem remains OPEN.

**END OF FOUR-SIZE ORDER-1320 REDUCTION.**
