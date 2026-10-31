# Shor completion: an even-tail P15 obstruction at order 2640

Owner **MathShor-2**, math-5. Actual clock of independent finite replay: **Wed Oct 28 20:38:48 PDT 2026**.
**Conditional necessary-border reduction with two separately implemented exact finite checks. No order2640 exclusion, all-order noncompletion, formal/peer/cross-family acceptance or novelty claim.**

## 1. Branch and forced partial heads

Suppose a finite UD factor-complete extension of the literal Shor code has actual pure-a order2640 and same-code direct border factors `|P|=15, |Q|=176`, with old anchors `A={0,3,8,11}` and `Y={0,1,7,13,14}`. Q is EVEN. The classical actual-border and Sands gcd-disjointness theorems were independently reconstructed in earlier packets.

P is uniform modulo3 and5, requiring5 heads in mod3 class1 and3 heads in each mod5 class. Old heads3,8 already occupy two positions in mod5 class3, so at most ONE of the five mod3-class1 heads may lie in mod5 class3. The old-anchor head screen has24 candidates in the class:8 outside mod5 class3,16 inside.

Exactly184 of the possible five-element partial sets satisfy that allocation and all old-tail gcd restrictions. Joining each to the four old heads yields20 distinct gcd-class sets H. Every actual P in this branch induces one of these184 partial sets.

## 2. Tail quotas and complete finite partition

Q has size176 and P is odd, so Q is uniform modulo16 with11 tails per class. P is coprime to11, so Q is also uniform modulo11 with16 tails per class. For each partial-head H, Q must avoid H by Sands and remain compatible with all old tails.

Among the184 partial sets, 78 leave fewer than11 individually admissible Q-candidates in some mod16 class. The remaining106 induce9 distinct H-sets. For EACH H, an exact include/exclude search retaining all mod16 and mod11 quotas finds no Q-selection. This exhausts the partial-head partition and excludes P15/Q176 at the stated written/finite-check scope.

## 3. Independent replay, positive control and limits

| Artifact | SHA256 | LF / bytes |
|---|---|---|
| `frontier-20261028-2640-even-p15-check.py` | 2e9b0c5eab4c88138cee387391938fd5b1b5858b4cd9401af25cd7a71a46577e | 64 / 3970 |
| `frontier-20261028-2640-even-p15-replay.py` | d53c108c091cbbc5040bba855f622e3c984cbf9935e85a50e280ba6a1b2ca6f8 | 54 / 2586 |

The producer tests all 5-subsets and uses bitsets. The separately written replay splits the candidates into `5 of 8 outside` or `4 of 8 outside plus 1 of 16 inside`, uses a set-based search with a different branch order, and reproduces the counts `184 / 20 / 78 / 106 / 9`. Maximum quota nodes were67 and53 respectively. The producer also directly verifies a literal 176-element Q-only set meeting all stated prime-power quotas and old-anchor gcd restrictions when partial-head H restrictions are omitted. This is a positive relaxation control, NOT a border factorization.

Together with the preceding even-tail sieve and P10 obstruction, the necessary even-Q P-sizes at order2640 are now

    {12,20,22,24,30,33,40,44,55,88}.

All ten remain open. Neither the pending odd-Q theorem nor any unreviewed solver timeout is used. The original finite UD factor-completion problem remains OPEN.

**END OF ORDER-2640 EVEN P15 OBSTRUCTION.**
