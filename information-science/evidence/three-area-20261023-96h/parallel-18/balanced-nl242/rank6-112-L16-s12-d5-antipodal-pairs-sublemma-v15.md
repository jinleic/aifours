# Balanced NL242 (3,112), L=16, s=12, d=5: six forced pairs and the m=24 3+3 split

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T09:58:18-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** Conditional on v11–v14 and their author-only dependencies, this derives necessary structure in all remaining (a2), (a3), and distinct-inactivity (a4) cases. It does not exclude any of them. Hand algebra only; no scientific program, numerical probe, independent review, formal/kernel check or novelty claim.

## Claim

Translate the affine 5-flat Π so that its direction space is W≅F₂⁵. There is a uniquely determined nonzero r∈W such that Σ is a disjoint union of six pairs {x,x+r}; on every pair g₀(x)g₀(x+r) has the same sign.

In each forced m=24 single-carrier slice of v14, exactly three pairs have g_η(x)g_η(x+r)=+1 and three have product −1. For either group of three pairs, their representative differences span a 2-space in W/⟨r⟩, and these two 2-spaces are complementary. This is a necessary condition only.

## Proof: six canonical pairs

By v13 the zero-slice transform is supported on six distinct classes ζ₁,…,ζ₆, with values 8εᵢ. Fourier inversion on W gives

    g₀ 1_Σ = (1/4) Σᵢ εᵢχ_{ζᵢ}.

At every point the sum on the right is 0 or ±4. Its six signs therefore have an odd number of negatives. It follows for every x that their product is −1, whence Σᵢζᵢ=0 and ∏ᵢεᵢ=−1. The five distinct nonzero differences ζᵢ+ζ₆, i≤5, sum to zero. They have rank at most four, and not at most three: five distinct nonzero points in a 3-space with sum zero would leave two distinct nonzero points whose sum is zero, since the sum of all seven nonzero points is zero. Thus these differences span a 4-space and have a unique nonzero annihilator r in W.

For x∈Σ, put qᵢ(x)=g₀(x)εᵢχ_{ζᵢ}(x). The six qᵢ have sum 4, so exactly one is −1. Moreover Σ_{x∈Σ}qᵢ(x)=εᵢΨ₀(ζᵢ)=8: precisely two points have qᵢ=−1. If x,y are those two, every qᵢ(x)=qᵢ(y), so every ζᵢ+ζⱼ annihilates x+y. As x≠y, x+y=r. This partitions Σ into exactly six r-pairs. Finally qᵢ(x+r)=qᵢ(x) for all i, so g₀(x+r)/g₀(x)=χ_{ζᵢ}(r), independent of i and x. ∎

## Proof: every m=24 slice has three pairs of each sign

For the slice of interest, let Ψ be the signed transform of its 12 active points in Σ. v14 gives Ψ=±2 at 24 classes and ±6 at the other eight; let N be the latter eight and S its complement. Write

    C(v)=Σ_{x∈W} g_η(x)g_η(x+v),  F(v)=Σ_{ζ∈S} χ_ζ(v),

where g_η is extended by zero off Σ. Since Ψ²=4+32·1_N, Fourier inversion yields, for every v≠0,

    C(v)=Σ_{ζ∈N}χ_ζ(v)=−F(v).                                    (1)

In (a2)/(a3), p is the only outside coset; in p's inactive slice every p+v is zero, and the pure-coset slice lemma gives F(v)∈{0,±4} for v≠0. In distinct-inactivity (a4), v12 gives k=2 on all 30 pure outside cosets, hence the same bound for v≠0,δ:=p+p′. At the remaining p′ coset, its two small entries have the same slice character and the other two the opposite character, so υ_η(p′)∈{0,±6}; the single-carrier formula υ_η(p′)=3ε_pF(δ) gives F(δ)∈{0,±2}. Parseval gives Σ_vF(v)²=32·24 and F(0)=24. All other nonzero terms have squares divisible by 16, so F(δ)² is divisible by 16 too; consequently F(δ)=0. Thus in all three variants

    F(v)∈{0,±4} for every nonzero v∈W.                             (2)

Let Pᵢ=g_η(xᵢ)g_η(xᵢ+r) be the six pair products. Their product is Γ_η=−1 by v14, so an odd number are negative. Therefore C(r)=2ΣᵢPᵢ is in {−8,0,8}. Equations (1)–(2) force C(r)=0: exactly three Pᵢ are positive and three negative. In particular N has four frequencies with χ(r)=+1 and four with χ(r)=−1. ∎

## Proof: complementary pair-triple directions

On the frequency half χ(r)=+1, only the three positive-product pairs contribute to Ψ; on χ(r)=−1, only the three negative-product pairs do. In either half Ψ/2 is the sum of three signed characters. Its magnitude is 3 exactly when those three signs agree. The two equality conditions, together with the specified value of χ(r), define the corresponding four-point part N_± of N. Since it has exactly four points, those conditions are independent and N_± is an affine 2-flat.

Let H_±⊆W be the 3-space annihilating the direction of N_±. Equivalently it is spanned by r and the two differences between representatives of the corresponding three pairs. The transform of each N_± has magnitude 4 precisely on H_± and vanishes outside. If H_+∩H_− contained some v outside ⟨r⟩, then at exactly one of v and v+r their two transform contributions would agree, giving |Σ_{ζ∈N}χ_ζ|=8 at a nonzero point. This contradicts (1)–(2). Hence H_+∩H_−=⟨r⟩. Modulo r the two pair-triple difference spaces are 2-dimensional, disjoint, and jointly span W/⟨r⟩. ∎

## Dependencies and limits

The argument uses the six-character author candidate `rank6-112-L16-s12-d5-six-character-structure-v13.md` (SHA-256 `59fdd87fc77e24c2b426a017d98b6ebf33063d4ad06520ccd1d2964cfcb8ab9c`), the m=24 sign sublemma `rank6-112-L16-s12-d5-m24-sign-sublemma-v14.md` (SHA-256 `7b5425d179cec99b8690dae641cf4e009c65722d2c49fd1eebe30003a1ca0fd7`), the reductions in `rank6-112-L16-s12-d5-partial-v11.md` and `rank6-112-L16-s12-d5-variants-v12.md`, and the exact admitted cuts cited by those files. All are unreviewed premises except the specifically identified admitted cuts.

The remaining three L16 s=12/d=5 variants and s=15,16 remain OPEN. Neither the original witness-or-unrestricted-exclusion question nor (24,24,2) is resolved. Novelty UNCLEARED; no method-clean or continuous-work assurance; HOLD and all prior findings, errata and NONINPUTs remain binding.
