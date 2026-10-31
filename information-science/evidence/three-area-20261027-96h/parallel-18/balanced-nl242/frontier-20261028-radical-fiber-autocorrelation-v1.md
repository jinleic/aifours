# info-6 frontier: radical-fiber mod-8 rigidity and an autocorrelation exclusion

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T21:08:59-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**. The general fiber rigidity and the numerical histogram exclusion below have written proofs with independent finite controls; no unrestricted no-go, actual target witness, novelty or formal/kernel acceptance is claimed.

## General radical-fiber rigidity

Let f:F₂⁹→{0,1} be any balanced Boolean function with T≠0 and exactly four frequencies in `Z₈={a:k(a)≡0 mod8}`, k=W_f/4. The written reduction `frontier-20261028-four-zero-rank6-only-v1.md`, SHA-256 `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37`, 43 LF, forces q=k/2 mod2 on K=T^⊥ to have rank six and R=rad(q)=Z₈. There is then a linear functional λ:R→F₂ such that for **all** a∈K and r∈R,

    k(a+r) ≡ k(a)+4 λ(r) q(a)  (mod 8).                                    (1)

This statement itself does not require the peak bound. If in addition `max|W_f|≤28`, set `m=A₋₂+A₆`. The q-one set has 112 or 144 points. If λ is nonzero, every radical fiber over q=1 contains two `(k/2)≡1` and two `(k/2)≡3` values, so m is respectively **56 or 72**. Thus a noncentral m forces λ=0 and makes k mod8 constant on every radical coset in K.

## Written proof of (1)

Choose K=F₂⁶_x⊕R with radical coordinates (r₁,r₂). Since q vanishes on R, it descends to a nondegenerate six-variable quadratic. Take either canonical Arf representative q and an integer degree-two lift g₀ of it, as in `frontier-20261028-four-zero-rank6-mod8-census-v1.md`, SHA-256 `b30fdd9449d92cf349aedb3ae6c2c355b11bf54d15027025c0fcac232f073a4f`, 69 LF. The one-support moment expansion gives

    k(x,r)/2 ≡ g₀(x)+2h(x,r) (mod 4),
    h=h₀(x)+r₁h₁(x)+r₂h₂(x)+r₁r₂h₁₂(x),                                  (2)

where deg h≤3, so deg h₁,deg h₂≤2 and deg h₁₂≤1. On q(x)=0, the condition Z₈=R requires k/2=0 mod4 for x=0 and k/2=2 mod4 for x≠0. Thus the value of h on that set is independent of r, and h₁,h₂,h₁₂ vanish on every zero of q.

An elementary lemma now applies: if p on F₂⁶ has degree≤2 and vanishes wherever a nondegenerate q vanishes, then p=0 or p=q. Indeed supp(p)⊆{q=1}; q has weight 28 or 36. If p and q+p are both nonzero, their supports partition supp(q). A nonzero six-variable quadratic has weight in `{16,24,28,32,36,40,48,64}`; no two such weights sum to 28 or 36. Hence one is zero. A degree≤1 p cannot equal the rank-six q, so it must vanish. Consequently h₁,h₂ are each 0 or q and h₁₂=0. Equation (2) gives (1), with λ determined by those two choices. ∎

## Exact autocorrelation exclusion of the surviving formal model

The formal four-zero histogram in `frontier-20261028-four-zero-mod8-counts-result.json`, SHA-256 `4f2c667037511d35ae9aada921f3361c3812274fa06639e9024a10ebcc20b1ea`, 288 LF, has q-zero count 112 and m=108, not the central value 72. Hence λ=0. Its 144 q-one frequencies all have |k|=6: 36 equal −6 and 108 equal +6. Since their residues uniquely determine these signed values and k mod8 is constant on radical cosets, each of the 36 q-one fibers is constant ±6.

Choose any nonzero r∈R. The radical fiber itself contributes zero to `R(r)=Σ_a k(a)k(a+r)`. Each q-one fiber contributes `4·36=144`, for 5,184 total. The remaining 27 q-zero nonradical fibers contain only ±4 and each contributes at least −64. Therefore the even-half contribution is at least

    36·144 − 27·64 = 3,456.                                                 (3)

Its odd-half Q has rank six and weight 144, so its radical linear term is zero: Q is constant along r. The model's odd values in each Q class are exactly:

| Q class | Signed values | Minimum unordered pair-product sum |
|---:|---|---:|
| 0 | 84 copies of −7; 28 of +5 | 392 |
| 1 | 20 copies of −5; 40 of −1; 84 of +7 | −392 |

For any pairing of a fixed sorted multiset, pairing smallest with largest minimizes the sum of products: for a≤b≤c≤d, both other pairings exceed or equal `ad+bc`. Applied in each Q class, the total **ordered** odd-half autocorrelation is at least `2(392−392)=0`. Thus (3) gives `R(r)≥3,456`, contradicting the exact Boolean autocorrelation caller `R(r)=0` for r≠0. This excludes every actual placement of this histogram, not all four-zero histograms. ∎

## Controls and pins

The separate control exhausts all 4,194,304 six-variable quadratic polynomials and finds exactly 0 and q supported on each canonical q-one set; it also independently computes both pairing minima by dynamic programming. Two independently implemented 131,072-solution mod-8 censuses additionally check that all 40 m=108 relaxation solutions have 27 all-residue-3 and nine all-residue-1 radical fibers. Those finite censuses corroborate, but are not premises of, the written fiber lemma.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-radical-fiber-check.py` | `a7ad873c202382111ed218552de9675bb639aa8cdd1dac71ad4d9e5678b9a8e4` | 60 |
| `frontier-20261028-radical-fiber-check-result.json` | `271ba7933430e2d32999afd816a1055d48e926e02061cc7e6b52cacb60d5f6e7` | 15 |
| `frontier-20261028-mod8-extreme-shape.py` | `10ff675d978872f523f599584b9b1e8fd46d488f7a2be2730ae36d5a17dfd5ef` | 60 |
| `frontier-20261028-mod8-extreme-shape-result.json` | `6a9938ecddfd825be38bd4910ba48867e4bf5962bdd52553dfcf047d0714eeaa` | 296 |
| `frontier-20261028-mod8-extreme-independent.cpp` | `bd571a1c4df0e2dbc5404b533b5ce54a24df1aaae7ca191fb4af0ad8af4efcf7` | 47 |
| `frontier-20261028-mod8-extreme-independent-result.json` | `47002af347e3d2a9a037645d3ccbb1021976286c75d70903b5d49d6c076c2ccc` | 8 |
| `frontier-20261028-four-zero-mod8-counts-result.json` | `4f2c667037511d35ae9aada921f3361c3812274fa06639e9024a10ebcc20b1ea` | 288 |
| `frontier-20261028-four-zero-rank6-only-v1.md` | `3e6e7572808e287da2ac3d2fb175efd1878ae52e83fa0a5864290aa3a5fc1f37` | 43 |

All written results remain author-owned and unreviewed. The original balanced witness-or-unrestricted-exclusion problem remains unresolved. **END.**
