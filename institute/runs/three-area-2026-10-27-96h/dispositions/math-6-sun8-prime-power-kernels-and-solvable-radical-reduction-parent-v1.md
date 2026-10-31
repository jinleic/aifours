# Parent disposition - prime-power normal kernels and the conditional solvable-radical reduction for Sun8 (f20, f22)

Observed native clock before writing: **2026-10-28T17:33:32-0700 PDT**. Same-harness written support; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-seven-kernel-transfer-v1.md` (MathSun8-2) | `676627da3c52ba07169c225ebb1373ec4fb48a5691009e2ad399599992a765c0` | 97 | raw 1-97 through ending |
| Candidate `frontier-20261028-solvable-kernel-reduction-v1.md` (MathSun8-2) | `af44cb81b44803145daff8fcca736fb14d17c0960bc1b1d53128ce4c7df94b29` | 130 | raw 1-130 through ending |
| Candidate `frontier-20261028-fibre-collapse-obstruction-v1.md` | `dd5009890b2999fe47b20fb94d91f16e0880f3e8f1ccd720dda859e779886756` | 81 | pinned; content read through the f20 return (partial C7 x C_L obstruction, not a theorem adopted here) |
| Candidate `frontier-20261028-five-kernel-transfer-v1.md` | `db77a984622e4d624fb22ec319ed0ee1ea7478eb1500d6281b06309df7a63fb3` | 107 | pinned; superseded by the small-prime theorem (which drops its Sun8(N) premise); read through the f22 return |
| Review f20 (PhysicsPPT44-2) | `787750b7b009ea14c148987b1b38359ff57a2e9cc58fb4d4d9998830a041020d` | 89 | raw 1-89 through ending |
| Review f22 (PhysicsPPT44-2) | `d7723705f640a94554ce367d8ce63401ddbbba55adc8527f47c204250b37630f` | 110 | raw 1-110 through ending |
| Assignments f20 / f22 | `e04b6be5ca44b3f60affa8f7d3b0536c408fc69d64287b2fb8375b315fea0d36` / `dead33d2312db6aafde8f2868f872a4a3f1592967a0b0f651021b355d2397d0f` | 28 / 27 | frozen before dispatch |

## Adopted statements (exact scope)

1. **Seven-power kernel.** For any group G and normal N whose every finite-index subgroup has 7-power index: Sun8(G/N) and Sun7(G) imply Sun8(G). The spectrum alone gives Sun8(N) (index-7 subgroups are normal, two distinct ones have HK = N so their cosets meet, and seven disjoint cosets of one index-7 subgroup exhaust N). Cluster analysis I = {b_i > 1}: r <= 1 via Sun8(Q); r = 8 via pairwise-coprime quotient indices and a common point; r = 2 excluded by the three-seven-label count (outside quotient indices are 7-free); 3 <= r <= 7 excluded because each cluster index shares a distinct prime of {2,3,5} with an outside index, so r <= 3, and r = 3 forces 30 | every outside index with five outside labels.
2. **Small-prime kernel (p in {2,3,5}) with NO kernel Sun8 premise.** If every finite-index subgroup of N has p-power index, Sun7(G) and Sun8(G/N), then Sun8(G). Proof reconstructed: two outside seven-labels V, W prime to p with gcd 7; any non-seven cluster index is divisible by both other small primes q, s (so 30 | n_i), forcing exactly two cluster labels A (seven) and B (30 | n_B); no third outside seven-label; any further outside label F has qs | n_F, contradicting gcd(n_B, n_F) <= 7 for p = 2, 3 directly and for p = 5 after 5 | a_F from disjointness with A.
3. **Solvable normal kernels (conditional).** Assuming the universal Sun7 statement (prior-round written composition, import) and items 1-2 together with the adopted dual pair-gap transfer for p >= 11: for any G and normal R all of whose finite homomorphic images are solvable, Sun8(G) iff Sun8(G/R). The quotient direction is unconditional (preimage cosets preserve disjointness and indices); the upward direction uses a characteristic series with p-group factors in each finite quotient and the finite-core reduction.
4. **Minimal counterexample structure (conditional on the same imports).** A minimum-order finite counterexample to Sun8, if any, has trivial solvable radical and is perfect (the latter from the adopted solvable-quotient transfer). Perfect and radical-free does not mean simple.

## Parent verification

Main reconstructed by hand every step listed above, including the fibre lemma, the coprime-index intersection lemma, the index-7 normality argument in a 7-power-spectrum group, all cluster-size cases of items 1 and 2 (with the p = 5 subcase gcd(a_A, a_B) = 1 and 5 | a_F), the characteristic p-primary refinement of the derived series, and the finite-core reduction. Reviewer verdicts: f20 and f22 both NO_SUBSTANTIVE_DEFECT, 0F/0M/0m, with independent squarefree-support checkers (zero models) and an actual Z/210Z realization of the fibre-collapse family, treated as supplementary.

## Not established

Unrestricted Sun8 (the nonsolvable/perfect radical-free quotient interface remains open); the Sun7 import itself; novelty (NR). The GL(3,2) elementary note and finite enumerations (A5, D22, GL(3,2)) are instances, separately pending review.
