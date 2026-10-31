# Original-array orbit multiplicities: deletion-gcd obstruction and a forced singleton at order 11

Owner **InfoRecursiveMDS18-2**, info-4. Actual native clock observed before writing: **Wed Oct 28 22:21:58 PDT 2026**.

**NEW author-WRITTEN candidate; unreviewed.** This is a universal obstruction for every original unrestricted T1(11), hence every original T2(11), under EVERY cyclic symbol labelling. It is not a search restricted to symmetric arrays. No mathematical program, numerical example, solver, certificate outcome, external theorem or held material is used. No formal/kernel, independent-model, novelty or parent-adoption claim.

**Inputs:** original T1 definition, elementary integer divisibility, and the half-orbit theorem of `frontier-20261028-prime-translate-intersection-rigidity-v1.md` (SHA `ac9bea314ad9b2ab178499ce16ed47d63fbfd506a11b2077c7a11a670581493e`), whose proof is recalled below.

## 1. Actual-row difference accounting

Let A be ANY T1(p) array, with p an odd prime. Fix ANY p-cycle g of the symbols and label symbols by Z/pZ so that g is addition of 1. Partition the actual p rows of A according to their orbits under g in the space of ALL permutation rows. Suppose r orbits meet A, with positive intersection sizes m_1,…,m_r summing to p. Choose a base row R_i in each such orbit. The actual shifts in an orbit need not be consecutive, nor a whole group orbit. No invariance of A is assumed.

For each nonzero e∈Z/pZ, let k_i(e) be the number of adjacent pairs in R_i with difference e. Every translate of R_i has exactly k_i(e) such pairs. Across A there are exactly p arcs with difference e, namely (x,x+e) for x∈Z/pZ, and T1 uses each exactly once. Therefore

sum_i m_i k_i(e) = p             for EVERY nonzero e.      (1)
sum_(e≠0) k_i(e) = p−1           for EVERY i.              (2)

All k_i(e) are nonnegative integers. Crucially, no permutation row R_i can have k_i(e)=1 for every nonzero e: summing those p−1 differences gives zero, whereas telescoping along R_i gives last(R_i)−first(R_i)≠0.

Thus if ANY condition forces one k_i(e) to be positive for all e, equation (2) forces it to be identically 1 and yields a contradiction. The following divisibility test does exactly that.

## 2. General deletion-gcd obstruction

**Theorem A.** In every actual-row partition of §1 with r≥2,

gcd(m_j : j≠i) = 1              for EVERY i.               (3)

**Proof.** Put d=gcd(m_j:j≠i). If d>1, then d≤p−1 and d does not divide the prime p. If k_i(e)=0, the left side of (1) is divisible by d, contradicting (1). Hence k_i(e)≥1 for every one of the p−1 nonzero e. Equation (2) makes every one equal 1, contradicting the last paragraph of §1. ∎

This is stronger than requiring only gcd(m_1,…,m_r)=1. Deleting ANY one multiplicity must still leave gcd 1. It is a necessary condition from common actual rows, not a claim that arbitrary integer solutions of (1)–(3) are realizable.

## 3. Universal order-eleven consequences

The half-orbit theorem gives m_i≤5 at p=11. Recall its elementary argument: if at least six translates of R_i occur, their shift-index difference set is all Z/11Z; then no adjacent difference of R_i can repeat, giving the impossible all-differences-once row of §1.

### At least four occupied row orbits

One or two occupied orbits cannot contain eleven rows when each has at most five. With exactly three, the complete sorted list of multiplicity partitions of 11 is

(5,5,1), (5,4,2), (5,3,3), (4,4,3).

Every one violates (3): delete, respectively, the multiplicity 1, 5, 5 or 3; the gcd of the remaining multiplicities is respectively 5, 2, 3 or 4. Thus:

**Every T1(11) occupies at least FOUR distinct permutation-row orbits under EVERY 11-cycle of the symbols.**

In particular no construction from arbitrary shift subsets of only three base permutation rows can realize an original T1(11), even when the subsets are not closed, not consecutive and not equally sized. This excludes an entire construction representation without imposing any symmetry on the original array.

### Exactly four orbits: only three multiplicity patterns remain

All sorted four-part partitions of 11 with parts at most five are

(5,4,1,1), (5,3,2,1), (5,2,2,2), (4,4,2,1),
(4,3,3,1), (4,3,2,2), (3,3,3,2).

Condition (3) excludes (5,2,2,2), (4,4,2,1), (4,3,2,2) and (3,3,3,2): delete respectively 5, 1, 3 and 2, leaving gcd 2, 2, 2 and 3. Hence any original array with exactly four occupied orbits must have one of

**(5,4,1,1), (5,3,2,1), (4,3,3,1).**                       (4)

These are residual multiplicity patterns, not completed or excluded original arrays.

### A singleton row orbit is unavoidable for every 11-cycle

**Theorem B.** For EVERY T1(11) and EVERY 11-cycle g, some actual row R has no other g-translate among the actual rows of A.

**Proof.** Suppose all m_i≥2. The preceding result gives r≥4, while summing to 11 gives r≤5. If r=4, every surviving pattern in (4) contains a 1, contradiction. If r=5, the only partition into five parts ≥2 is (3,2,2,2,2). Deleting 3 leaves gcd 2, violating (3). There is no r≥6 without a singleton because six parts ≥2 sum to at least 12. ∎

Thus an original T2(11) is not merely globally asymmetric under a regular cyclic symbol action: for every such action, at least one of its actual rows is isolated from all its nontrivial translates, and its whole actual row set needs at least four distinct translate classes.

## 4. Scope and remaining gap

**WRITTEN universal:** equations (1)–(2), deletion-gcd condition (3) for every odd-prime T1(p), and the at-least-four-orbits, three exact four-orbit residual patterns and forced-singleton conclusions at p=11. All statements apply a fortiori to every unrestricted original T2(11).

**OPEN:** Whether the multiplicity patterns (4), or configurations with five or more occupied orbits and a singleton, support a T2(11). Difference-count conditions do not themselves construct Hamiltonian rows or enforce the full distance-two requirement. No claim is made that every original array must have only four orbits. No native search or small-order extrapolation was used. The unrestricted T2(11) existence/no-go target remains **OPEN**, with no support-9 or novelty promotion.
