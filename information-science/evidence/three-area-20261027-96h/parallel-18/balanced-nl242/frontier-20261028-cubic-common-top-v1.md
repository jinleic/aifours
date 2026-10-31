# info-6 frontier: corrected cubic coset congruence

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T02:32:32-0700**. **UNREVIEWED AUTHOR CANDIDATE**, additive after the mandatory cubic-divisibility withdrawal. It does not use the false claim that every six-variable cubic has weight divisible by 8. It depends on the pinned unreviewed rank-two profile/cubic inputs and on the parent-adopted E₂+2O₃ congruence through the corrected parity paper. It is not a target witness, unrestricted no-go, novelty, disjoint review or formal verification.

## Statement

For any actual balanced f:F₂⁹→F₂ with `T≠0`, peak≤28 and rank-two even polar B, let R be the six-dimensional radical, `g=(W/8 mod4)` on the even frequency half, `q=g mod2`, Z the Walsh-zero count, and

    G₃=#{a∈T⊥:q(a)=1, g(a)=3}.

Then each of the three q-one R-cosets contains a number of g=3 positions congruent to `Z mod4`. Consequently

    G₃≡Z (mod4);    Z≡0 (mod4);    G₃≡0 (mod4).                 (1)

No divisor-eight claim is made. An additional odd-half corollary, conditional on the unreviewed quartic-coupling candidate, is that `h=1_{|W/4|∈{3,5}}` is cubic and its four R-coset weights are equal modulo4; their total is divisible by 8, but **need not be divisible by 16**. The latter algebraic statement alone does not rule out any of the corrected 23 unsigned profiles.

## Correct six-variable lemma

If p and p′ are Boolean polynomials of degree≤3 on F₂⁶ with the same homogeneous cubic part, then their weights are congruent modulo4. Their difference d=p⊕p′ has degree≤2. Every degree≤2 Boolean polynomial on F₂⁶ has weight divisible by 4: in the XOR inclusion-exclusion expansion, a single monomial contributes a multiple of 16, a product of two contributes a multiple of 8, and all remaining terms carry coefficient divisible by 4. Also `Σ pd` is even because pd has degree≤5<6. Hence

    wt(p′)−wt(p)=wt(d)−2Σ pd ≡0 (mod4).                          (2)

This proof is compatible with the actual cubic weight-14 counterexample: it only compares polynomials with the **same** top cubic part.

## Even-half application

The rank-two predecessor gives q-zero count 64, so q vanishes exactly on R. The singular-cubic predecessor gives an integer quadratic lift g₀ of q and a Boolean cubic t on K such that `g=g₀+2t mod4`. On any R-coset g₀ has constant parity. In its six radical coordinates, after subtracting an appropriate constant and dividing the even-valued part by 2, g₀ contributes a Boolean polynomial of degree≤2.

On R, `H=1_{g=0}=1−t−(g₀/2) mod2` is the Walsh-zero indicator, so wt(H)=Z and H has the same cubic part as t|R. On any q-one coset, `1_{g=3}` differs from t restricted to that coset only by a quadratic and a constant. The four restrictions of the **same global cubic t** to parallel R-cosets have the same six-variable cubic part. Applying (2), each q-one residue indicator has weight congruent to Z modulo4. The corrected parity predecessor proves Z≡0 mod4; hence each of those weights, and their sum G₃, is divisible by 4. ∎

For the odd-half corollary, rank two makes the quartic Pfaffian part vanish; the unreviewed quartic paper gives h degree≤3. Its four parallel R-slices have the same cubic part, hence equal weights modulo4 by (2). Every six-variable cubic has even weight, so the common residue is 0 or 2. Their total is therefore 0 or 8 modulo16, i.e. divisible by 8. No claim that it is divisible by 16 follows. ∎

## Intended-reason control and limitations

The checker constructs a degree-three six-variable zero indicator with **Z=12**, not divisible by8, and a single explicit even-half array with rank-two q/z64, cubic mod8 lift, first sum128, squared energy `64·118`, E₂=6 and g=3 coset weights `(52,52,12)`, all 0 modulo4. Its E₂ is compatible with an odd n₃; no odd half or Boolean inverse is supplied. This is a formal **NON-WITNESS**, not evidence of a target at Z=12. It demonstrates that the corrected proof does not silently reintroduce the false divisor-eight assumption.

The preceding withdrawal remains mandatory and immutable. The new lemma, its Boolean callers, and the profile/cubic inputs need disjoint full-scope review. All target existence or unrestricted exclusion remains open.

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-cubic-common-top-check.py` | `efd555d50ca5ee9f4b2a25a4aa18c3d05ec1b6d945dbb9f75f873c373c880c26` | 50 | corrected cubic control |
| `frontier-20261028-cubic-common-top-check-result.json` | `39b30c322e339528414ddaad87380b7b5709fd00cbcd09f47d96e565d6b4e536` | 292 | formal Z12 even-half NON-WITNESS |
| `frontier-20261028-cubic-divisibility-withdrawal-v1.md` | `7b6596b4e5cad5aaeb4dc109baaa07dc8e685dfa696ae5abc0af632d21de705c` | 33 | mandatory withdrawal |
| `frontier-20261028-rank2-corrected-parity-v1.md` | `c2a0b51ab918289c9db73b1196c59d5d9c209c7a783c3045296010d3d90f3b2b` | 44 | unreviewed Z congruence predecessor |
| `frontier-20261028-singular-cubic-zero-v1.md` | `6fba1086e8beefa0101f28c5c4c4c3243be2fc583d18328f6271ac6695e961fe` | 70 | unreviewed cubic predecessor |

**END.**
