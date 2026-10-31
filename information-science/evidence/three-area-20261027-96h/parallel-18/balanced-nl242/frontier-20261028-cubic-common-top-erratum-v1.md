# info-6 frontier: erratum to cubic coset total

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T03:18:36-0700**. This is a mandatory additive author correction. The pinned original remains unchanged and unreviewed; no parent adoption or independent verification is implied.

## Withdraw the odd-half total-divisibility assertion

In `frontier-20261028-cubic-common-top-v1.md` SHA256 `fdb93f48b8c788b719e6d753a682c567f1c76430c879b95f7cfb2edef8e1005e`, 47 LF, withdraw the statement in §Statement and §Even-half application that four congruent-mod4 radical-coset weights have a total divisible by 8. Four integers congruent modulo 4 need only have total divisible by 4; their unknown multiples of 4 do not cancel modulo 8.

The explicit cubic

    h=x₀x₁x₂ ⊕ x₃x₄x₅ ⊕ x₀x₆x₇

on F₂⁸ has total weight **68** and four six-dimensional coset weights `(8,20,8,32)`. These are all congruent modulo 4, but the total is 4 modulo 8. The pinned checker independently computes its ANF and counts. This is a polynomial counterexample, not a Boolean target spectrum or witness.

The correct odd-half conclusion from the common-cubic-top lemma is **only** that the four coset weights are equal modulo 4; their sum is divisible by 4. No eight-divisibility claim follows from that lemma alone. In particular this erratum does not remove or refine any of the 23 corrected rank-two magnitude profiles.

## Unaffected scope and dependencies

The original's six-variable lemma—same cubic top implies equal weight modulo 4—and the separate even-half statement `G₃≡0 mod4` under the corrected Z congruence do not use the erroneous total-sum step. They remain **unreviewed author candidates**, not automatically accepted. The original explicitly said its odd corollary excluded no profiles, and the pinned low-rank D/m/Z profile results do not depend on that odd total claim. The earlier mandatory divisor-eight withdrawal `frontier-20261028-cubic-divisibility-withdrawal-v1.md` remains in force; none of its withdrawn results is reinstated. The original witness-or-unrestricted-exclusion gap remains open.

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-odd-cubic-sum-countercheck.py` | `7a00a62f157920455c9f78df94e07d962554a1d87ba9d18b9a025c2caccf8d03` | 28 | polynomial counterexample checker |
| `frontier-20261028-odd-cubic-sum-countercheck-result.json` | `f8c2e37311dce3dd069bc6a64e599efa0880f8392dd33543ee65c3c43e545470` | 18 | exact counterexample receipt |
| `frontier-20261028-cubic-common-top-v1.md` | `fdb93f48b8c788b719e6d753a682c567f1c76430c879b95f7cfb2edef8e1005e` | 47 | unreviewed original; apply this erratum |
| `frontier-20261028-cubic-divisibility-withdrawal-v1.md` | `7b6596b4e5cad5aaeb4dc109baaa07dc8e685dfa696ae5abc0af632d21de705c` | 33 | earlier mandatory withdrawal |

**END.**
