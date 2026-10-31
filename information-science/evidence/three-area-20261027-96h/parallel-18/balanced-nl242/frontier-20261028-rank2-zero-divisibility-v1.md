# info-6 frontier: rank-two zero-count divisibility

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T01:42:22-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This is an additive consequence of the pinned unreviewed low-rank profile and singular-cubic predecessors. It is a necessary-condition refinement, not an original witness, unrestricted exclusion, independent review, novelty claim, or formal verification.

## Claim

Under the original balanced nine-variable Boolean, nonzero T and peak≤28 hypotheses, if the even polar B has rank two, then all Walsh zeros lie in its six-dimensional radical and their number Z is a **positive multiple of 8**. With the previous profile `(D,m)`, the exact remaining zero-count possibilities are

| D=n₁+n₃ | agreeing T-pairs m | possible Z |
|---:|---:|---|
| 12 | 118 | 8, 16, 24 |
| 16 | 120 | 8, 16 |
| 20 | 122 | 8 |

These are necessary possibilities, not a claim that any occurs. For the D20 row, the separate unreviewed zero-plane packet gives the stronger shape of the eight zeros. No rank-two, rank-four, rank-six or rank-eight case is globally excluded here.

## Proof

The profile predecessor forces z=64. For a rank-two quadratic q with q(0)=0, this is the anisotropic quotient case: q vanishes exactly on the six-dimensional polar radical R. Every Walsh zero has q=0, hence lies in R. The singular-cubic predecessor proves its indicator `H=1_{W=0}|_R` is a nonzero Boolean polynomial of degree at most 3; it contains frequency zero.

A Boolean polynomial of degree d≥1 in n variables has weight divisible by `2^(ceil(n/d)−1)`. One short proof expands its integer 0/1 truth table as the XOR of algebraic-normal-form monomials. For any nonempty family of j monomials, the XOR inclusion-exclusion coefficient is `(-2)^(j−1)`, while their common support has size divisible by `2^max(0,n−dj)`. Each term is therefore divisible by `2^(j−1+max(0,n−dj))`, whose minimum over j≥1 is `2^(ceil(n/d)−1)`. For n=6,d=3 this divisor is 8. Thus Z is a positive multiple of 8; the elementary minimum-weight bound also gives Z≥8.

The pinned exact profile has `(D,m)=(12,118),(16,120),(20,122)`. Even-half energy gives `Z≤(7936−64m)/16`, namely 24,16,8. Intersecting each upper bound with the positive multiples of 8 gives the table. ∎

## Controls and remaining gap

The checker gives explicit degree≤3 indicators on F₂⁶, each containing the origin, of weights 8, 16, and 24, and verifies the table's integer arithmetic. These are **only polynomial sharpness controls**, not a common Walsh spectrum or Boolean target witness. The result does not establish that Z=8,16,24 is realizable under all original conditions. The necessary profile/cubic inputs and this divisor argument require disjoint review; all original witness-or-unrestricted-exclusion obligations remain.

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-zero-divisibility-check.py` | `246751570e0d99827a98541dbd88c5bc353ffb954f97ef2096c306732cb180f2` | 36 | polynomial/arithmetic controls |
| `frontier-20261028-rank2-zero-divisibility-check-result.json` | `89dd6240af8af4cf04be85079b214da60eea684ab4ee75158343fed1974734da` | 49 | control receipt |
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 | unreviewed profile predecessor |
| `frontier-20261028-singular-cubic-zero-v1.md` | `6fba1086e8beefa0101f28c5c4c4c3243be2fc583d18328f6271ac6695e961fe` | 70 | unreviewed cubic predecessor |

**END.**
