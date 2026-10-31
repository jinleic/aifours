# info-6 frontier: rank-two cubic residue divisibility

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-29T02:01:17-0700**. **UNREVIEWED AUTHOR CANDIDATE**, conditional on the pinned unreviewed rank-two parity/profile and singular-cubic inputs. This is not a labelled Boolean witness, unrestricted exclusion, disjoint review, novelty claim, or formal verification.

## Claim

For an actual balanced nine-variable f with `T≠0`, peak≤28 and even polar rank two, let `g=k/2 mod4` on the even half, `q=g mod2`, and

    G₃=#{a:q(a)=1, g(a)=3},   G₁=192−G₃.

Then **G₃ and G₁ are multiples of 8**. More precisely, the numerical ranges below are necessary according to the indicated first moment `s_even=Σ_{T⊥} k∈{0,128}`:

| D | Z | s_even=0: possible G₃ | s_even=128: possible G₃ |
|---:|---:|---|---|
| 12 | 8 | 72,80,88,96,104,112,120 | 88,96,104,112,120,128 |
| 12 | 16 | 80,88,96,104,112 | 88,96,104,112,120 |
| 12 | 24 | 88,96,104 | 96,104,112,120 |
| 16 | 8 | 80,88,96,104,112 | 88,96,104,112,120,128 |
| 16 | 16 | 80,88,96,104,112 | 96,104,112,120 |
| 20 | 8 | 80,88,96,104,112 | 88,96,104,112,120 |

Each list is a **coarse necessary set** from first moment, energy, and divisibility; no claim is made that every listed value can be placed in a Boolean spectrum. Neither rank two nor the original target is excluded.

## Proof

The rank-two predecessor gives z=64, so the zero set of q is exactly its six-dimensional radical R; the other three R-cosets comprise the 192 q-one positions. The singular-cubic predecessor derives `g=g₀+2h mod4`, where g₀ is an integer quadratic lift of q and h is a Boolean polynomial of degree≤3 on K.

On a fixed R-coset `a₀+R` with q=1, the restricted integer lift g₀ has constant odd parity. Let `c=g₀(a₀) mod4`, so c is 1 or 3. Then `g₀−c` has even values on R, and its reduced multilinear polynomial modulo 4 has even coefficients. Dividing those coefficients by two gives a Boolean polynomial of degree≤2 on R. Accordingly `1_{g=3}=h+(g₀−c)/2+(3−c)/2 mod2` on this coset has degree≤3. Its weight is divisible by 8 by the inclusion-exclusion proof in the zero-divisibility predecessor. Summing the three cosets gives G₃≡0 mod8; G₁=192−G₃ is likewise divisible by 8.

Let E₂ be the number of even coefficients with magnitude 2 after division by four; the parity-profile predecessor fixes it for each D/Z pair. Among the G₃ points let L be the number taking k=−2 instead of +6; the other E₂−L low-magnitude points occur in the G₁ residue class, taking +2 instead of −6. If P of the `64−Z` nonzero q-zero positions take +4, then

    s_even = 6(2G₃−192)+8(E₂−2L)+4(2P−(64−Z)),
    max(0,E₂−G₁)≤L≤min(E₂,G₃),  0≤P≤64−Z.                    (1)

Enumerating (1) with G₃∈{0,8,…,192} and s_even=0 or128 gives precisely the displayed coarse sets; the pinned checker lists every value. ∎

## Sharpness control and limits

The checker constructs an explicit **even-half-only formal non-witness** with q rank two/z64, eight zeros, a degree-three mod8 correction, `G₃=120,G₁=72`, even first sum128 and even squared energy7808=64·122. Its 256 values are in the receipt. It has no supplied odd half, no verified 511 correlations and no Boolean inverse, so it is not a target witness. It demonstrates that the endpoint G₃=120 in the final row is attainable by the listed even-half filters, not by the full target.

A preliminary exploratory sampling cell accidentally used a q array from a different coordinate system; that sampling output was discarded and is not an input to this packet. The pinned control recomputes q/g from its own explicit coordinates. All new conclusions and predecessor inputs require disjoint review; the original witness-or-exclusion gap remains.

| File in this directory | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-rank2-cubic-residue-check.py` | `2c74a9bc36432cbf6192c34b530488a2c79136d598ce47c66881d09e045e5306` | 51 | residue/positive-control checker |
| `frontier-20261028-rank2-cubic-residue-check-result.json` | `6d943bdb32e8256b28673c21a204c6b98cb6cdee16c93b7d77184f3d7a5d254f` | 404 | even-half NON-WITNESS receipt |
| `frontier-20261028-rank2-parity-profile-v1.md` | `a2f2fdc481efa967f5e61d95cc72c8aea19efd10a72c43c877eb8dc16316b1ab` | 42 | unreviewed profile predecessor |
| `frontier-20261028-singular-cubic-zero-v1.md` | `6fba1086e8beefa0101f28c5c4c4c3243be2fc583d18328f6271ac6695e961fe` | 70 | unreviewed cubic predecessor |

**END.**
