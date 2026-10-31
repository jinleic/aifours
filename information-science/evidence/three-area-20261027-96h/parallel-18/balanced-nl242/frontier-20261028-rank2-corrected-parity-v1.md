# info-6 frontier: corrected rank-two zero/parity profiles

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T02:24:38-0700**. **UNREVIEWED AUTHOR CANDIDATE**, additive after the pinned cubic-divisibility withdrawal. This result uses the unreviewed low-rank profile and singular-cubic minimum-support inputs, plus the parent-adopted E₂+2O₃ congruence. It does **not** use the false six-variable cubic divisor-eight lemma. No witness, unrestricted exclusion, novelty, disjoint review or formal verification is claimed.

## Corrected claim

Under the original balanced f:F₂⁹→F₂, `T≠0`, peak≤28 hypotheses, suppose B has rank two. With `D=n₁+n₃`, m the number of agreeing T-pairs, Z the total Walsh-zero count, and `E₂=#{even-half |W/4|=2}`, the following are necessary:

| D | m | possible Z | E₂ | parity of n₃ |
|---:|---:|---|---|---|
| 12 | 118 | 8,16,24 | 8,4,0 respectively | even |
| 12 | 118 | 12,20 | 6,2 respectively | odd |
| 16 | 120 | 8,16 | 4,0 respectively | even |
| 16 | 120 | 12 | 2 | odd |
| 20 | 122 | 8 | 0 | even |

In particular **Z is divisible by 4**, but no divisor-eight conclusion is asserted. Combining the exact odd-energy equations leaves 23 unsigned magnitude profiles in the pinned receipt, with `104≤n₇≤113`. These are necessary options, not codes, labelled spectra, or claims of realizability. They do not exclude rank two or the original target.

## Proof

The unreviewed profile predecessor gives q-zero count 64 and the three D/m pairs. This q is anisotropic on its rank-two quotient and vanishes exactly on its six-dimensional radical R. The unreviewed singular-cubic predecessor proves the zero indicator restricted to R has degree≤3 and contains the origin; its **minimum-support** bound gives Z≥8. This is valid independently of the false divisor-eight assertion.

At q=0 the nonzero even k values are ±4; at q=1 they are ±2 or ±6. Since even-half energy is 64m,

    32E₂ = 7936−16Z−64m.                                         (1)

The parent-adopted Walsh/mod-4 disposition gives `E₂+2n₃≡0 mod4`, so E₂ is even. For m even, (1) then implies Z is divisible by 4. It does not imply Z divisible by 8. The energy upper bound gives Z≤24,16,8 in the three cases; together with Z≥8 and Z≡0 mod4 this gives exactly the table's zero options. Formula (1) gives E₂, and the same parent congruence determines n₃ parity. The 39-LF checker enumerates those constraints and the odd-energy/magnitude identities, obtaining 23 profiles and the stated peak range. ∎

## Counterexample boundary and remaining gap

The pinned cubic-divisibility withdrawal constructs a formal even-half object with Z=14, E₂=5, `Σ_even k=128`, `Σ_even k²=64·118`, q rank two/z64, peak≤24, and a cubic mod8 correction. It is **not** a Boolean target witness and cannot satisfy the parent congruence for any n₃, because E₂ is odd. This explicitly distinguishes the false local cubic-divisor claim from the valid full-object parity constraint used above.

All claims here remain author-only pending disjoint review of this proof and the pinned predecessor scopes. The corrected table does not establish existence at Z=12 or20, nor rule out any remaining profile. The witness-or-unrestricted-exclusion target remains open.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-corrected-parity-check.py` | `b6bf5e597ce5c5bdb96ac55c837ca1b7877cfd6495317fb71f5df505b981d3c1` | 39 | corrected integer-profile checker |
| `frontier-20261028-rank2-corrected-parity-check-result.json` | `2e1686e5e48829864d704636412c3e88e5ff521b99aed08e46b7151ce8f35fd2` | 282 | corrected unsigned profiles |
| `frontier-20261028-cubic-divisibility-withdrawal-v1.md` | `7b6596b4e5cad5aaeb4dc109baaa07dc8e685dfa696ae5abc0af632d21de705c` | 33 | mandatory withdrawal |
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 | unreviewed profile predecessor |
| `frontier-20261028-singular-cubic-zero-v1.md` | `6fba1086e8beefa0101f28c5c4c4c3243be2fc583d18328f6271ac6695e961fe` | 70 | unreviewed minimum-support predecessor |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted written caller |

**END.**
