# info-6 frontier: a kernel-direction autocorrelation bound for one formal histogram

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` before writing: **2026-10-28T21:53:09-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**, deliberately separate from any general four-zero exclusion or solver result. The displayed histogram is formal and no Boolean target is claimed.

## Statement

Assume the original balanced peak≤28 four-zero Boolean hypotheses and the normalized radical notation of `frontier-20261028-fourzero-phase-consolidated-v1.md`, SHA-256 `8c6afc0d19a9707089c5aebf1240f21ef69b1418a2c7009fcaa650712fc5707a`, 154 LF: `ρ=0`, `λ≠0`, and R is the zero radical. Let `r₀` be the unique nonzero element of ker λ. Then the odd-half peak/unit indicator `P=1_{|k|∈{1,7}}` satisfies **D_{r₀}P affine**.

For the exact signed count vector pinned in `frontier-20261028-four-zero-directed-10.json`, SHA-256 `0557b2b6fc27994c3169b5387f9243c29e54b420e9c9c7dc3eab15a56bb9338c`, 516 LF, these necessary conditions give the all-placement bound

    C_k(r₀)=Σ_a k(a)k(a+r₀) ≥ 2,016 > 0.                                    (1)

This contradicts the Boolean caller for this **one histogram**. It does not by itself exclude all four-zero histograms; no solver status is used in the proof.

## Why the derivative is affine

Choose a₀ outside the even half K and for x∈K define

    g(x)=k(x)/2 mod4,       u(x)=(k(a₀+x)−1)/2 mod4.

Since λ(r₀)=0, g(x+r₀)=g(x). Since ρ=0, `u(x+r₀)−u(x)` is always even. For M the one-support and `m(x)=#{v∈M:a₀·v=1, x·v=1}`, the integer parity identity gives

    u(x)−g(x) ≡ (k(a₀)−1)/2 − m(x)  (mod4).

As x varies, m modulo four is a squarefree Z/4 polynomial with linear terms and **even** quadratic coefficients; its third additive differences vanish modulo four. The derivative of u−g in direction r₀ is even, and half of that derivative has vanishing second differences modulo two, so it is affine. Adding two modulo four toggles the predicate `u∈{0,3}`, which is precisely P. Hence D_{r₀}P is affine.

An affine Boolean function on eight variables has weight 0,128, or 256. Here wt(P)=160; the constant-one derivative would force wt(P)=128 and is impossible. Therefore `I=Σ_{a∈H}P(a)P(a+r₀)` is either 160 or 96.

## Exact even and odd lower bounds

On the even half r₀ preserves q-zero and both mod-8 q-one residue classes. The histogram's nonzero values in these classes are

    q=0:  56×(−4), 52×(+4);
    q=1, k/2≡1: 53×(−6), 19×(+2);
    q=1, k/2≡3:  1×(−2), 71×(+6).

The four zeros pair within R and contribute zero. Pairing the smallest value with the largest minimizes the pair-product sum; applying it independently gives ordered lower bounds −1,600, +768 and +2,496, so the even-half contribution is at least **1,664**.

On the odd half Q is r₀-invariant. Choose the baseline coefficient `−7,+5,+7,−5` in the four classes `(Q,P)=(0,1),(0,0),(1,1),(1,0)` respectively. Its ordered autocorrelation is

    144I−12,800 ≥ 1,024,

because I is 96 or 160. The actual histogram differs from that baseline at exactly six positions: one `−7→+1`, two `+5→−3`, and three `−5→+3`. Each change is ±8 and alters the ordered autocorrelation by at most `2·8·7=112`, even when another exception is its partner. Hence the odd contribution is at least `1,024−6·112=352`, proving (1). ∎

## Controls and pins

The finite control independently computes the three even pair minima by dynamic programming, verifies the P-intersection calculation on a formal mod-8-consistent P, and plants a non-affine derivative mutation. These checks do not replace the all-variable proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-kernel-phase-check.py` | `a585ec994eafd70d2de72666768fb87eed807fc725c78117637e51ffabe8a8ab` | 54 |
| `frontier-20261028-kernel-phase-check-result.json` | `b6358604d72d9b7da14111768616041f351883c880874b4d6e7d4236d6395638` | 14 |
| `frontier-20261028-fourzero-mod8-P-search-result.json` | `f00d5f21d9c69f6768fa7aeb42b474d141a0b8ebf9cda3faa45285c91dd8d587` | 18 |
| `frontier-20261028-four-zero-directed-10.json` | `0557b2b6fc27994c3169b5387f9243c29e54b420e9c9c7dc3eab15a56bb9338c` | 516 |
| `frontier-20261028-fourzero-phase-consolidated-v1.md` | `8c6afc0d19a9707089c5aebf1240f21ef69b1418a2c7009fcaa650712fc5707a` | 154 |

No global four-zero or unrestricted exclusion follows from this histogram-specific bound. **END.**
