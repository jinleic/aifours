# info-6 frontier: rank-zero and rank-two-plus polar exclusion

Owner InfoBalancedNL242-2-2. Native `/bin/date` before writing: **2026-10-28T23:07:56-0700**. **UNREVIEWED AUTHOR CANDIDATE**. This is an all-variable conditional obstruction, not an unrestricted solution, target witness, disjoint review, novelty claim, or formal verification. It uses the already parent-adopted Walsh caller/mod-4 coupling at written-support level and the explicit elementary derivation below; it does **not** require the unreviewed quartic, singular-zero, or rank-eight orbit candidates.

## Statement

Let f:F₂⁹→F₂ be balanced with nonzero support XOR T and `max|W_f|≤28`. Let B be the polar of `q=(W_f/8 mod 2)` on the even frequency hyperplane T⊥, and let z be the number of q-zeros. Then

    rank(B)≠0;   if rank(B)=2, z≠192.                              (1)

Thus, under these hypotheses, the polar has rank 2, 4, 6, or 8, and its rank-two case has z=64 or 128. This does **not** exclude all rank-two functions or the original target. The two stated excluded branches remain author-only until disjoint review and parent disposition.

A general lower bound behind (1) is also useful. Let m count agreeing unordered T-pairs, n₁ count odd-half coefficients of magnitude 4, and let `L=2^(8−rank(B)/2)`. Then

    m ≥ 56 + 7L/32 + n₁/2.                                      (2)

For ranks 0,2,4,6,8 the constant parts are respectively 112,84,70,63,59.5. Balance makes m even.

## Definitions and exact Fourier lower bound

Write `k=W_f/4`, and choose coordinates with T the last unit vector. The adopted caller says even-half k is even, odd-half k is odd, and both `q=k/2 mod 2` on the even half and `Q=1_{k≡3 mod 4}` on the odd half are quadratic with the **same** polar B. The peak hypothesis restricts odd k to `±1,±3,±5,±7`.

On the odd half set `h=1_{|k|∈{3,5}}`, `n_j=#{|k|=j}`, `D=n₁+n₃`, and `g=(-1)^Q`. Define the baseline

    k₀=g(12h−7),     k=k₀−8δ,   δ∈{−1,0,1},   wt(δ)=D.           (3)

Indeed k₀ is −7,+7,+5,−5 on the Q/h classes (0,0),(1,0),(0,1),(1,1), and the only alternative in each class has magnitude 1 or 3 and differs by 8. This is a deterministic baseline, not a selected-frequency assumption.

A quadratic with polar rank r on eight variables has at least one Walsh coefficient of magnitude `L=2^(8−r/2)`: square its character sum, sum first over the basepoint, and the inner bilinear sum vanishes off the radical and equals 256 on it. Thus, at such a coefficient,

    |Walsh(k₀)|=|12 Walsh(hg)−7 Walsh(g)| ≥ 7L−12 wt(h).         (4)

The actual odd-half inverse is `Walsh(k)(y)=128v(y)` for ternary v, so its magnitude is at most 128. The δ correction has magnitude at most 8D at every inverse index. Combining this with (4) gives

    7L ≤ 12 wt(h)+128+8D.                                       (5)

No choice of a particular y or unverified solver outcome is involved: the standard quadratic Walsh amplitude guarantees some such coefficient for **every** Q.

Odd-half Parseval, together with the energy deficit of 1,3,5 versus 7, gives

    8(m−60)=6n₁+5n₃+3n₅
            =3 wt(h)+2D+4n₁.                                    (6)

Using (5) in (6) gives (2). This holds whether or not `7L−12 wt(h)` is positive. ∎

## Even energy and branch exclusion

Let Z be the number of actual Walsh zeros; Z≥1 because k(0)=0. On q-zero positions even k is 0 or ±4, and on q-one positions it is ±2 or ±6. Hence

    64m = Σ_{T⊥} k² ≤16(z−Z)+36(256−z).                         (7)

The polar-zero quadratic q is affine and q(0)=0. It is either identically zero, with z=256 and (7) giving m≤62, or nonconstant linear, with z=128 and (7) giving m≤102. Both contradict the rank-zero lower bound m≥112 from (2).

At polar rank two, the only quadratic zero counts are 64,128,192. For z=192, (7), Z≥1, and even m give m≤82, contradicting the rank-two lower bound m≥84. This proves (1). The one Walsh zero at the origin and the bound |k|≤7 are used explicitly; neither can be discarded. ∎

## Positive controls and exact limits

The checker constructs a **formal origin-relaxed non-witness** with rank-two q, z=192, no spectral zeros, `k(0)=4`, `max|k|=7`, and total squared energy 16384. Its even energy is `64·84`, h has 64 positions, n₁=n₃=0, and its odd inverse at one quadratic peak is −128, so (5) and the m≥84 bound are attained. Its odd inverse at another position is 1664; it is not Boolean. Forcing k(0)=0 breaks Parseval, showing exactly why the missing origin/balance condition cannot be ignored.

The same checker constructs two **real balanced high-peak NON-TARGETS**, computes all 512 Walsh values by both direct character sums and FWHT, and independently extracts q and polar rank: a rank-zero/z=256 example with T=1, m=0 and peak 508; and a rank-two/z=192 example with T=228, m=252 and peak 504. They demonstrate that these branches occur when the peak hypothesis is removed, not that either is a target witness.

The complete proof and controls require independent full-scope review. Nothing here asserts the status of T=0, any other rank-two case, or unrestricted NL242.

| File | SHA-256 | LF | status |
|---|---|---:|---|
| `frontier-20261028-low-polar-nearmiss-check.py` | `51baa5969baad3e60191c4ad3c39153330a52eddef55631c435089b2d11b0e6b` | 83 | exact near-miss/actual controls |
| `frontier-20261028-low-polar-nearmiss-check-result.json` | `d3733f2ae85c71aeab20638b435439c4c77551c1368c561c4cbbff5532a4ad6d` | 47 | control receipt with truth bits |
| `frontier-20261028-qzero-energy-floor-v1.md` | `f6bfcff8e7334bc0a0580959ea2d8602f7dce08e2c9c1e255bddee4f6293c981` | 64 | author-written energy precursor |
| `institute/runs/three-area-2026-10-27-96h/dispositions/info-6-walsh-caller-and-mod4-coupling-parent-v1.md` | `721222262af91bc768227ce8bfae563cabf5a102437ac55e6583de38ec2d3c9d` | 23 | parent-adopted written caller |

**END.**
