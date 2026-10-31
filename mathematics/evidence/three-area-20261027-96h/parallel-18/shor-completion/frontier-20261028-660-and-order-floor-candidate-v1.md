# Shor completion: independent order-660 exclusion and a candidate 1980 floor

Owner **MathShor-2**, math-5. Native clock of the exact finite check: **Wed Oct 28 19:37:31 PDT 2026**.
**HIGH-CONSEQUENCE CANDIDATE: written mathematics plus exact bounded integer checks; unreviewed, not formally verified, not novelty-cleared and not an all-order noncompletion result.**

## 1. Claims and explicit dependency

For the literal Shor code, the independent border/gcd argument below gives the following candidate necessary condition on the actual pure-a order n of any finite UD factor-complete extension:

    660 divides n  OR  2310 divides n.                          (1)

The same argument and finite checks exclude **n=660**. Together with the separate, unreviewed order-1320 no-go candidate in `frontier-20261028-1320-border-no-go-candidate-v1.md`, they imply the **candidate floor `n>=1980`**. This floor is CONDITIONAL on successful review of that order-1320 candidate and of the present argument; it is not presented as an adopted result. The original all-order completion problem remains OPEN.

The general same-D border factorization and Sands' divisor-difference criterion are classical; the particular necessary forms used here were reconstructed from actual codewords and cyclic Fourier identities in the cited order-1320 predecessor. No historical held output is accepted as a premise.

## 2. All-order divisibility from the old anchors

Any such D has a direct border tiling `P+Q=Z_n` with old heads `A={0,3,8,11} subset P` and old tails `Y={0,1,7,13,14} subset Q`. The difference1 occurs in Q. By Sands gcd-class disjointness, every nonzero old P-difference has gcd with n different from1. The differences3,5,8,11 occur in P, so

    2*3*5*11=330 divides n.

If `v_2(n)=1` and 7 does not divide n, the old P-difference8 and old Q-difference14 both have gcd2 with n, again impossible. Therefore either 4 divides n or7 divides n. Together with `330|n` this proves (1). This does not assert the stronger unconditional claim `660|n`.

The positive integers below1980 in the union in (1) are only660 and1320. Thus excluding those two specific orders yields the stated candidate floor.

## 3. Exhaustive cardinality setup at n=660

Suppose n=660 and let P,Q be the same hypothetical D's direct border factors. The seven-head predecessor gives `|P|>=7` by explicit anchor collision/coverage identities. At n660 the old-anchor gcd screen has exactly42 candidate P-residues, so `|P|<=42`. Divisibility `|P||Q|=660` leaves exactly

    |P| in {10,11,12,15,20,22,30,33}.                         (2)

Here the old P- and Q-difference gcd classes are respectively

    G_A={3,4,5,11},    G_Y={1,2,6,12}.                         (3)

For primes3,5,11, each appearing only once in660, the side whose cardinality is divisible by that prime is uniform modulo it. The exact screened P-residue table has only6 candidates in mod3 class1 and only2 in mod5 class2. Hence 3-uniform size33 is impossible; 5-uniform sizes15,20,30 are impossible. Size11 is impossible since mod11-uniform P of size11 would contain both0 and11 in a class whose capacity is1. We treat the remaining10,12,22 separately.

## 4. Size10: an 18-slot contradiction

If `|P|=10`, it is uniform modulo5 and must take both screened candidates in each of classes2 and4:

    class2={132,407},     class4={264,539}.

The first pair has gcd55, and `gcd(132-0,660)=132`, so Q must avoid classes55 and132 as well as G_A. The old-anchor Q-candidate screen under these restrictions contains no residue4 modulo6. Q has size66 and is uniform modulo3, so it must contain22 elements congruent1 mod3; all are odd.

If two such elements share their `(mod11,mod4)` slot, their difference is a nonzero multiple of132 and has gcd132 with660. At most one may occupy each slot. The exact screened set has only18 available such slots, contradiction.

## 5. Size12: a six-pair matching

If `|P|=12`, then Q has odd size55. All `Phi_2,Phi_4` must divide the P-mask, so P is uniform modulo4, with3 elements in each class. The old-anchor P-screen has exactly three in each of classes1 and2:

    class1={33,253,473},    class2={198,418,638}.

These six forced heads contain differences of gcd55,165,220, which Q must avoid in addition to G_A. The resulting screened Q-candidates in mod11 classes0 and3 are

    {0} union L,  L={44,110,264,374,594,627},
    {14} union R, R={47,80,300,410,564,630}.

Q is uniform modulo11 with5 elements in each class; since it contains the anchors0 and14, it must select4 from L and4 from R. But the six disjoint pairs

    (110,47), (264,80), (594,410),
    (627,564), (374,630), (44,300)

all have difference gcd3 or4, forbidden in Q. Eight chosen endpoints across six disjoint pairs force one forbidden pair. So size12 is impossible.

## 6. Size22: tail outside-class shortage

If `|P|=22`, P is uniform modulo11 with2 elements in each class. The screened mod11 class1 is exactly `{188,243}`, forcing both and hence a P-difference gcd55. Q must avoid55 as well as G_A.

Q has size30 and is uniform mod5 and mod3: it contains6 tails in each mod5 class and20 tails not congruent1 modulo3. Under the anchor screen with gcd55 additionally forbidden, there is **no** tail congruent1 modulo3 in mod5 classes0 or4; their12 required tails therefore all count among those20. Outside these two mod5 classes the same screen contains only two tails not congruent1 modulo3, namely47 and627, so it cannot provide the other8. Size22 is impossible.

## 7. Exact finite check, pins and limits

`frontier-20261028-660-border-exclusion-check.py`, SHA256 `3d93de9d4968b8ab36606d4128d7d5f424ac79376390ced8213351aff98ddde4` (41 LF, 2253 bytes), reconstructs both old gcd class sets and candidate screens, verifies every stated residue count and forced head list, the18-slot bound, all six matching gcds, and the two-element outside-class list. Its actual output reports all checks passing. The finite computation uses exact integer arithmetic only and is not formal verification.

The `|P|>=7` predecessor is `frontier-20261028-seven-head-border-obstruction-v1.md`, SHA256 `713afb914e2781c8367e31726c298bc158c2c5b61176277c2d219762dfd96e24`. The separate order-1320 candidate on which the numerical floor depends is SHA256 `52aeaff132fb0e59f9c735054b017df9471e543035ba0bfea1d3dcd04385869e`.

The candidate theorem and floor require disjoint scientific reconstruction of the classical border premise, gcd-class criterion, prime-uniformity, finite script and the entire separate order-1320 dependency. No peer, human, independent-model-family, formal or novelty acceptance is claimed.

**END OF ORDER-660 AND 1980-FLOOR CANDIDATE.**
