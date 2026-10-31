# Parent disposition - Sun8 transfer through an index-three normal extension (f1)

Observed native clock before writing: **2026-10-28T17:19:51-0700 PDT**. Same-harness written support; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-c3-normal-transfer-v1.md` (MathSun8-2) | `5c9099385c75e451a60f8bebe1c133dc1da07285e504aa822799e91027e70668` | 100 | raw 1-60 and 60-100 through ending |
| Review `frontier-review-f1-sun-c3-transfer-v1.md` (PhysicsPPT44-2) | `b6906074a12a7c4c6bd9cf011ea5ade1dda529c68f47880676f703762a343fa0` | 92 | raw 1-92 through ending |
| Assignment `review-waves/f1-sun-c3-transfer/assignment-v1.json` | `1dfb9f87c82a566fca9909f3a42175ca12522b293caf64f704bd71de51a34526` | 20 | frozen before dispatch |

## Adopted statement (exact scope)

**Theorem.** For every group G and every normal subgroup N of index 3: if every eight pairwise-disjoint left cosets of finite-index subgroups of N have two indices with gcd >= 8 (`Sun_8(N)`), and every seven pairwise-disjoint left cosets of finite-index subgroups of G have two indices with gcd >= 7 (`Sun_7(G)`), then `Sun_8(G)`. Groups may be infinite; no splitting, normality of the chosen subgroups, covering or index symmetry is assumed.

**Corollary (conditional).** If G/N is a finite 3-group, `Sun_8(N)` holds and `Sun_7` holds for every intermediate group of the pulled-back central series, then `Sun_8(G)`. The universal Sun7 statement used by the author to pay those hypotheses is an explicit IMPORT (statement only, not re-proved or authenticated here).

## Parent verification

Main reconstructed every step by hand: the index formula `n_i = a_i b_i` with `a_i in {1,3}`; the actual fibre lemma (`t^{-1}(g_i U_i ∩ tN) = x(N ∩ U_i)`, an actual left coset of index `b_i`; disjoint originals give disjoint fibres at a common quotient point); the coprime-index intersection lemma via the injective diagonal map `G/(H∩K) -> G/H × G/K`; (2.1) `gcd(b_i,b_j) >= 2` whenever images meet; the Sun8(N) reduction forcing at least two proper-image labels; (2.2) `gcd(b_i,b_j) <= 2` for proper pairs; the Sun7 forcing of at least three seven-divisible original indices with at most one proper among them and an odd seven-divisible full label V; the no-proper-seven case (3 and 5 split between A and B, then `15 | n_V` and `15 | n_B` or `15 | n_A`); and the one-proper-seven case (`5 | b_B, 5 | n_V`; exactly two proper labels; `2 | n_W, 2 | b_B`; `b_A` odd and coprime to `b_B`; a third full label F is not seven-divisible, has `3 | n_F`, `2 | n_F`, `5 ∤ n_F`; then `gcd(n_F, n_V) = 1` contradicts (2.1) for two full labels). The 3-group central-series corollary is elementary (class equation).

Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m, with an independently written squarefree-support overapproximation check (zero terminal models) treated as supplementary only. Main did not run either checker; the written proof is the basis of adoption.

## Not established

Unrestricted Sun8; the Sun7 property itself (import); transfer through index-2 or mixed composition factors (separate candidates in review); any finite simple/perfect quotient case; source/book equivalence; novelty (NR). Earlier immutable quarantine/process records for this slot remain historical records and are not retrospectively certified or used as premises.
