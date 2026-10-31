# info-6 frontier: exact affine-energy exclusion of a second formal family

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:50:09-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**. This excludes one specified structural family, not all four-zero spectra or the unrestricted original target.

## All-variable subclass and first failing condition

Let f:F₂⁹→{0,1} be balanced with full Walsh peak≤28, write `k=W_f/4`, and choose dual coordinates such that the XOR T of the one-support is e₈. For x=(x₀,…,x₇)∈F₂⁸ suppose simultaneously

    k(x,0)/2 ≡ q(x)=x₀x₁+x₂x₃+x₄x₅                 (mod 2),
    1_{|k(x,1)|∈{1,7}} = P(x)=1−1_{x₀=1,x₂=0,x₄=0}.       (1)

**No such f exists.** This holds for *every* choice of the signed k magnitudes in the respective q/P classes. It does not assume a particular histogram, position of zeros, odd-half sign function, or the rest of the earlier formal placement.

The first failing class is the already adopted **affine energy congruence**: any affine frequency 5-flat F must have `Σ_{a∈F} k(a)²≡0 (mod 16)`. For the two functions in (1), the flat

    F = {a∈F₂⁹ : a₀=a₁=a₆=a₇=1}

instead has squared energy congruent to **8 mod 16**, independently of all remaining magnitude choices. Thus it is incompatible with the Boolean inverse and the exact autocorrelation caller. In particular, the entire fixed-q/P family containing `frontier-20261028-four-zero-coupled-placement-result.json` is excluded; the result is stronger than merely rejecting that one formal table.

## Flat count and residue

F has 32 points: 16 on each parity half. On the even half its four fixed coordinates give `q=1+x₂x₃+x₄x₅`, which equals one at 10 of the 16 choices of x₂,…,x₅. There k is even and |k|≤7: if q=1 then k²≡4 mod16; if q=0 then k²≡0 mod16.

On the odd half, P=0 precisely for x₂=x₄=0, leaving x₃,x₅ free; this happens at four points. At those four points |k| is 3 or 5, so k²≡9 mod16. At the other twelve, |k| is 1 or 7, so k²≡1 mod16. Consequently

    Σ_{a∈F} k(a)² ≡ 10·4 + 4·9 + 12·1 = 88 ≡ 8  (mod 16).      (2)

This is a symbolic category count, not a numerical assertion about one chosen table.

## Self-contained affine-energy caller

Let U be the four-dimensional spatial span of e₀,e₁,e₆,e₇, and let λ be the all-one character on U. F is the set of frequencies restricting to λ. For each of the 32 cosets C=x_C+U, let

    v_C = Σ_{u∈U} (−1)^{f(x_C+u)} (−1)^{λ·u}.

Each v_C is even. Orthogonality on the quotient V/U gives

    Σ_{a∈F} W_f(a)² = 32 Σ_C v_C²,
    Σ_{a∈F} k(a)² = 2 Σ_C v_C².                                  (3)

Because f is balanced, every W_f(a) is divisible by 4. For any a₀∈F, `W_f(a₀)=Σ_C (−1)^{a₀·x_C}v_C`. The signs do not change an even number modulo 4, so `Σ_C v_C≡0 (mod 4)`. Thus an even number of the v_C/2 are odd, and `Σ_C v_C²≡0 (mod 8)`. Equation (3) proves the required mod-16 energy congruence, contradicting (2). ∎

## Evidence and limits

The independent finite checker confirms the 10/4 counts and the pinned placement's actual flat energy 984≡8 mod16. As a positive control it uses a real balanced NL240 table and independently checks equation (3), by direct character sums and spatial-coset sums, on all 16 frequency cosets for this U. A targeted category mutation removes the mod-16 failure. These checks do not replace the all-variable proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-affine-energy-flat-check.py` | `0fe4407d2e181791448bed5132ebe6a4d7b40b5c6e92ab975822b84841c727af` | 52 |
| `frontier-20261028-affine-energy-flat-check-result.json` | `7fed6f73350cf61d11403cca1323e108bc435b2e61802ec5706bedeb49f93aba` | 30 |
| `frontier-20261028-four-zero-coupled-placement-result.json` | `ba99cc035f8cc8bbbcb9edfc99d9068263e93bdb93dfa9e368b2219f1e223c0f` | 674 |
| `frontier-20261028-even-odd-quadratic-coupling-v1.md` | `30a9d8ec35a9a6d25da2e84caa172d5d019733a49f36b3d5767c75834e5b9c6f` | 63 |

No actual balanced NL242 witness or unrestricted contradiction follows. **END.**
