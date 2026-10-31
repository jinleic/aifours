# info-6 frontier: four Walsh zeros force rank six, with zero plane equal to the radical

Owner **InfoBalancedNL242-2-2**. Native `/bin/date` observed before writing: **2026-10-28T20:18:44-0700 PDT**. **UNREVIEWED AUTHOR CANDIDATE**. This is an all-variable proper reduction, not a proof that the four-zero case is impossible, an actual Boolean witness, a novelty claim, or formal verification.

## Statement

Let f:F₂⁹→{0,1} be balanced, put k=W_f/4, assume its one-support XOR T is nonzero, and use the quadratic `q=k/2 mod2` on K=T^⊥ with polar B. Define `Z₈={a∈K:k(a)≡0 mod8}`. Then

> **If |Z₈|=4, rank(B)=6 and Z₈=rad(B).**

This statement does not require a Walsh peak bound. For a balanced peak≤28 target, Z₈ is exactly its Walsh-zero set; therefore exactly four Walsh zeros force rank six, with those four frequencies exactly the polar radical. As q vanishes on the radical, its zero set in K has size 112 or 144, so the count of magnitude-16 Walsh coefficients is respectively **108 or 140**. No existence of either branch is asserted.

The preceding `frontier-20261028-four-zero-radical-reduction-v1.md`, SHA-256 `89ca5480f9c4375cc0a82b313fd66c554941bfc7856bdea3e326935a94eeb229`, 63 LF, already proves that |Z₈|=4 makes it a linear 2-plane, that rad(B)⊆Z₈, and that rank(B)≥6, with equality forcing Z₈=rad(B). It remains to rule out rank eight.

## Full-rank contradiction

Assume rank(B)=8. For every z∈Z₈, q(z)=0; since Z₈ is a linear plane, its two generators have B-pairing zero. Thus Z₈ is a totally singular, in particular totally isotropic, 2-plane. Extend a basis of it to a symplectic basis

    Z₈=span(e₁,e₂),     B(e_i,f_j)=δ_ij,     B(e_i,e_j)=B(f_i,f_j)=0.

For completeness, choose dual partners f₁,f₂, make their mutual pairing zero by a basis adjustment, and extend the resulting nondegenerate 4-space by two further hyperbolic pairs. Let

    D=span(f₁,f₂,e₃),       L=D^{⊥_B}.

D is totally isotropic of dimension three. Hence L has dimension five, its restricted radical is exactly D, and `rank(B|L)=2`. Also L∩Z₈={0}: pairing a nonzero element of span(e₁,e₂) with f₁ or f₂ is nonzero.

For every affine coset A of L, q|A is a five-variable quadratic of polar rank two; its number of ones is 8, 16, or 24, always divisible by eight. Fix any odd coset B₀ of L in the other Walsh half. For each even coset A, the union A∪B₀ is an affine frequency 6-flat; the balanced affine-energy identity gives its scaled squared energy divisible by 32. As derived explicitly in the preceding paper,

    Σ_{a∈A} k(a)² ≡ 16 [ (Σ_A q)/4 + |A∩Z₈| ] (mod 32).                  (1)

The odd part is fixed as A varies, and `(Σ_A q)/4` is even for every A. Therefore the parity of |A∩Z₈| must be the same for all eight cosets of L. But L∩Z₈={0}, so the four elements of Z₈ lie in four distinct cosets: four parities are one and the other four are zero. Contradiction. Thus rank eight is impossible, and the predecessor's rank-six equality proves the theorem. ∎

## Finite control and limits

The separate checker instantiates a rank-eight symplectic space, a totally singular 2-plane, the isotropic 3-space D and the constructed L. It checks rank(B|L)=2, all eight quadratic coset counts are divisible by eight, and their formal even-half energy residues split into four zeros and four sixteens modulo 32. This is a concrete control of the construction, not a substitute for the basis-independent proof or a disjoint review.

| File | SHA-256 | LF |
|---|---|---:|
| `frontier-20261028-fourzero-fullrank-check.py` | `269713d57f556f99b8fc8f85512e06f121c5bb716fbfb5cf93e82d805233d161` | 56 |
| `frontier-20261028-fourzero-fullrank-check-result.json` | `e056c534fb3ccff7b789bde7a18cd12ba77570d0585f9c0fb6bcf6c031c32b8e` | 75 |
| `frontier-20261028-four-zero-radical-reduction-v1.md` | `89ca5480f9c4375cc0a82b313fd66c554941bfc7856bdea3e326935a94eeb229` | 63 |

Neither the rank-six four-zero branch nor the original unrestricted witness-or-exclusion question is resolved. **END.**
