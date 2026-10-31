# info-6 frontier: quartic coupling between even Walsh magnitudes and odd peak/unit support

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T18:52:58-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**; no unrestricted exclusion, realization, novelty or formal-verification claim.

## Universal necessary condition

For every balanced f:F₂⁹→{0,1} with `max|W_f|≤28`, let `k=W_f/4` and T be the one-support XOR. By the explicit proof in `frontier-20261028-even-half-four-zero-obstruction-v1.md` (SHA-256 `7344078fb115eb47f9d5e3c731a63d16567cb09d23af4868810c5d45ef38f8c4`, 59 LF), T≠0 and `K=T^⊥` has dimension 8. Choose a₀ outside K and define

    q(x) = k(x)/2 mod 2,
    P(x) = 1_{|k(a₀+x)|∈{1,7}},                           x∈K.

The even-half q is quadratic; let its alternating polar be `B(u,v)=q(u+v)+q(u)+q(v)`. Then **P has degree at most four**, and for every four independent directions v₁,…,v₄ in K and every x∈K,

    Δ_{v₁}Δ_{v₂}Δ_{v₃}Δ_{v₄} P(x)
      = B(v₁,v₂)B(v₃,v₄)+B(v₁,v₃)B(v₂,v₄)+B(v₁,v₄)B(v₂,v₃).      (1)

Thus the full quartic part of P is the Pfaffian 4-form of B. In particular P has degree exactly four when rank(B)≥4, and at most three when rank(B)≤2.

A count consequence is worth isolating. Let Z count all zero Walsh coefficients, F count all magnitude-16 coefficients, and `N= #{a:|W_f(a)|∈{4,28}}=wt(P)`. Then

    N ≡ 2 (mod 4) if Z+F ∈ {120,136};
    N ≡ 0 (mod 4) otherwise.                                                (2)

The possible Z+F values and the rank-eight characterization are the quadratic-weight classification proved in `frontier-20261028-even-odd-quadratic-coupling-v1.md` (SHA-256 `30a9d8ec35a9a6d25da2e84caa172d5d019733a49f36b3d5767c75834e5b9c6f`, 63 LF). Equation (2) is necessary only and does not decide the original problem.

## Mixed-flat energy proof

Fix any 4-dimensional subspace L≤K. Let A=x+L be an arbitrary even-half affine 4-flat and B₀=a₀+y+L an arbitrary odd-half affine 4-flat parallel to it. Their union is one affine frequency 5-flat. The affine-energy caller, reproved in `frontier-20261028-coupled-family-affine-energy-obstruction-v1.md` (SHA-256 `775ad16e5485ee524f47be864737d3c5fb6fe04a6dc4fe1c29e47052b6bd875a`, 54 LF), says the sum of k² on that union is divisible by 16.

For a∈A, k is even and |k|≤7, hence `k²≡4q(a) (mod 16)`. On B₀, k is odd: P=1 gives |k|=1 or 7 and square 1 mod16, while P=0 gives |k|=3 or 5 and square 9 mod16. Since each half-flat has 16 points, the energy congruence becomes

    Σ_{a∈A} q(a) − 2 Σ_{a∈B₀} P(a−a₀) ≡ 0 (mod 4).                     (3)

The restriction of q to A is a quadratic on four variables. Its number of ones is 2 modulo 4 exactly when its polar on L has rank four, and is 0 modulo 4 for ranks zero or two. This follows immediately by putting its alternating polar in symplectic normal form; the four-variable weights are 6/10 in rank four, 4/8/12 in rank two, and 0/8/16 in rank zero. Therefore (3) says the parity of P on **every** odd affine 4-flat with direction L equals 1 precisely when B|_L is nondegenerate.

For any ordered basis v₁,…,v₄ of L this nondegeneracy indicator is the Pfaffian on the right of (1); over F₂ every invertible basis change has determinant one. The parity sum over x+L is exactly the fourth additive derivative of P. This proves (1). The right side is independent of x, so every fifth coordinate derivative vanishes, proving deg P≤4; the quartic coefficient on any four coordinate variables is the corresponding Pfaffian. ∎

The second formal placement in the earlier family has polar rank six but P of degree three, so (1) excludes the **whole** fixed-q/P family. This is the all-directions explanation of its explicit affine 5-flat energy failure; it remains only a subclass exclusion.

## Proof of the mod-4 count consequence

Use symplectic coordinates for B of rank 2r. The quartic part forced by (1) is

    P₄ = Σ_{1≤i<j≤r} x_i y_i x_j y_j.

For a Boolean polynomial in eight variables of degree≤4, expand its XOR of monomials as an integer sum. Modulo four, every single-monomial weight vanishes; any term involving at least three monomials has coefficient divisible by four; and a two-monomial term survives only when both are disjoint degree-four monomials whose union contains all eight variables. Therefore `wt(P) mod 4` is −2 times the parity of the number of disjoint pairs among its degree-four monomials.

For r≤3 every two monomials in P₄ share a symplectic pair, so there are no disjoint pairs and `wt(P)≡0 (mod 4)`. For r=4 there are exactly three disjoint complementary pairs, so `wt(P)≡−6≡2 (mod 4)`. Weight is invariant under the invertible coordinate change. The quadratic classification gives rank eight exactly for Z+F=120 or 136, which proves (2). ∎

## Finite controls and pins

An independent finite checker exhausted all 2,048 four-variable quadratic/affine forms and verified their weight modulo four against polar rank. It also sampled 125 eight-variable P polynomials with the forced quartic at ranks 0,2,4,6,8, checked 8,750 coordinate 4-flat parities, confirmed the weight congruence at each rank, and rejected a quartic mutation. These checks supplement but do not replace the all-variable proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-quartic-coupling-check.py` | `ae3acc554bc4046059110f24ccd1e8a64d321ebacb2019f073b2bcb7d748e648` | 79 |
| `frontier-20261028-quartic-coupling-check-result.json` | `c0c1d4e6d3f5610f08eed5c86a5575e8bdf2846779351d0874dbb4599d5cdd63` | 33 |
| `frontier-20261028-coupled-family-affine-energy-obstruction-v1.md` | `775ad16e5485ee524f47be864737d3c5fb6fe04a6dc4fe1c29e47052b6bd875a` | 54 |
| `frontier-20261028-even-odd-quadratic-coupling-v1.md` | `30a9d8ec35a9a6d25da2e84caa172d5d019733a49f36b3d5767c75834e5b9c6f` | 63 |

The original balanced witness-or-unrestricted-exclusion question remains unresolved by these conditions. **END.**
