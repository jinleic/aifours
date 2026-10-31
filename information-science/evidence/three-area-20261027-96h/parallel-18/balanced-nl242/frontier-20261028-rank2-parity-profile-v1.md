# info-6 frontier: rank-two parity-refined magnitude profiles

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T01:50:53-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This uses the parent-adopted `E₂+2O₃≡0 mod4` constraint at its exact written-support scope, plus pinned unreviewed rank-two profile/zero-divisibility predecessors. It is not a witness, unrestricted exclusion, independent review, novelty claim or formal verification.

## Statement

Under the original balanced f:F₂⁹→F₂, `T≠0` and peak≤28 hypotheses, suppose the even polar B has rank two. Let `E_j` count even-half coefficients with `|W/4|=j`, let `n_j` count odd-half coefficients with `|W/4|=j`, put `D=n₁+n₃`, and let Z be the Walsh-zero count. Then the following are necessary:

| D | m | possible Z | possible n₁ | n₇ |
|---:|---:|---|---|---|
| 12 | 118 | 8,16,24 | 2,8 | 110,112 |
| 16 | 120 | 8,16 | 4,10,16 | 108,110,112 |
| 20 | 122 | 8 | 0,6,12,18 | 104,106,108,110 |

Here m counts agreeing unordered T-pairs. In all cases n₁ and n₃ are even and the number of magnitude-28 coefficients satisfies `104≤n₇≤112`. For a given row, all combinations of the listed Z and n₁ are left as **necessary options**, not asserted realizable. The table does not exclude rank two, rank four, rank six, rank eight, or the original target.

## Proof

The unreviewed profile predecessor gives the three D/m pairs, z=64 and the corresponding odd-energy profiles. The unreviewed zero-divisibility paper gives positive `Z≡0 mod8` and the listed upper bounds. Even-half squared energy is exactly 64m; at q=0, nonzero k has magnitude 4, and at q=1 k has magnitude 2 or 6. Therefore

    64m=16(64−Z)+4E₂+36(192−E₂),
    E₂=(7936−16Z−64m)/32.                                       (1)

For all six listed `(D,m,Z)` combinations, E₂ is a nonnegative multiple of four: respectively 8,4,0; 4,0; and 0. The parent-adopted necessary congruence

    E₂+2n₃≡0 (mod 4)                                             (2)

therefore makes n₃ even; D is even, so n₁ is even. Substitute this parity into the pinned profile lists, or directly use `8(m−60)=6n₁+5n₃+3n₅`, `n₁+n₃=D`, and `n₁+n₃+n₅+n₇=256`. The 33-LF checker enumerates the 16 resulting `(D,m,Z,n₁,n₃,n₅,n₇)` profiles and confirms the table and extrema. ∎

## Boundary and verification

All 16 are **formal unsigned magnitude profiles**, not codes, labelled spectra, witnesses or no-go proofs. The finite enumeration verifies only the displayed elementary arithmetic. The parent-adopted congruence does not promote the new conclusions: all inherited author-only rank/zero inputs and this proof require disjoint review. Other ranks and the unrestricted witness-or-exclusion gap remain.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-parity-profile-check.py` | `73a358035d016e81fb724c2b623c3f941a8421a0ff1493cafb0d9130018cea43` | 33 | bounded integer checker |
| `frontier-20261028-rank2-parity-profile-check-result.json` | `4187c01b696222cd92f0801ccc6c34f16285553fd05d0c7038460c3f2091d059` | 197 | formal unsigned profiles |
| `frontier-20261028-rank2-zero-divisibility-v1.md` | `0f84a22a93b37690b7d6d0f24e5142f6a18c2ed6cb5b973357f753395b509a4d` | 36 | unreviewed zero predecessor |
| `frontier-20261028-lowrank-valid-profile-v1.md` | `910d3b68e5e25d13b10b7843b5716edffbdbe82203c01f70b2351bb4faa8ceac` | 63 | unreviewed profile predecessor |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted written caller |

**END.**
