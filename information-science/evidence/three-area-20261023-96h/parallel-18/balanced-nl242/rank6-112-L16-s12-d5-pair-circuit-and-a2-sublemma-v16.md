# Balanced NL242 (3,112), L=16, s=12, d=5: canonical pair circuit and an (a2) compatibility condition

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:01:10-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** The conclusions are conditional on the author-only v205 chain through v15. They are necessary conditions, not a complete exclusion or a witness. Handwritten exact reasoning only; no selected numeric-state probe, scientific computation, review, formal/kernel or novelty claim.

## 1. Pair-circuit classification of Σ

By v15, Σ⊂Π=a+W is the disjoint union of six cosets of ⟨r⟩, r≠0. Its affine span is Π. By v7 §3, Σ has exactly 15 affine planes. Any two r-pairs form a distinct plane, giving all 15. Four distinct quotient points cannot form an affine plane in W/⟨r⟩: if they did, choose one lift from each pair and, if necessary, replace one lift by its r-mate to make their sum zero. Those four points would form a further plane, not the union of two r-pairs.

The six quotient points affinely span the 4-space W/⟨r⟩, so their affine-dependence space has dimension one. A nonzero affine relation has even size; sizes two and four are impossible. Therefore its support is all six points, whose sum is zero. Any five are affinely independent. Consequently, up to an affine change of Π, the support is exactly

    Σ = {0,e₁,e₂,e₃,e₄,e₁+e₂+e₃+e₄} × F₂,

with r the F₂-fibre direction. This is a classification of the support only; it does not classify the entire target or claim novelty. In particular, the 15 pairwise differences among the six quotient points are all distinct and exhaust the 15 nonzero quotient elements.

The complementary 2-spaces of v15 are automatic for every split of this six-point affine circuit into two triples: an intersection of their direction 2-spaces would give a forbidden four-point relation. v15's nontrivial sign statement is the forced 3+3 split.

## 2. The m=20 slice in (a2)

Let y,z be the two double-valued Σ-cosets in (a2). In the other p-active slice they are both inactive; the active inside set A=Σ\{y,z} has 10 points and τ:=ΣA=y+z≠0. Its 32 class sums Ψ split into 16 classes with Ψ≡0 (mod 4) and 16 with Ψ≡2 (mod 4), in some order. Write n_j for the number in the appropriate half with |Ψ|=j. Since m=20 and Σ Ψ²=320,

    n₄+n₈+n₂+n₁₀ = 20,
    n₂+n₆+n₁₀ = 16,
    n₄+2n₈+2n₁₀ = 8.

The last equation follows by substituting the first two into the second moment. Let S={ζ:3∤Ψ(ζ)} and F(v)=Σ_{ζ∈S}χ_ζ(v). The number of S classes in the two parity halves differs by 4+2n₈+4n₁₀, so |F(τ)|=4+2n₈+4n₁₀. At the pure outside coset p+τ, the single-carrier formula and the inactive p slice give F(τ)∈{0,±4}. Hence n₈=n₁₀=0, and the class distribution is exactly

    |Ψ|:       0   2   4   6
    multiplicity 8  12   8   4.

In particular F(τ)=±4, so p+τ is nonzero in this m=20 slice. Its pure-coset triple has at most one nonzero entry, and therefore the forced m=24 slice has F₂₄(τ)=0.

## 3. Location of y and z relative to the m=24 split

In the m=24 slice, let Pᵢ be the sign product on each r-pair. If y,z occupy the same pair then τ=r and no further positional assertion is made. Suppose they occupy different pairs i,j. By §1 their quotient difference identifies i,j uniquely, and Σ∩(Σ+τ) consists of exactly those two full pairs. The signed autocorrelation C₂₄(τ)=Σ_xg₂₄(x)g₂₄(x+τ) is then zero exactly when Pᵢ=−Pⱼ: the two cross-pair contributions cancel for opposite products, and add to ±4 for equal products. By v15 equation (1), C₂₄(τ)=−F₂₄(τ)=0. Thus

    either y,z are the two points of one r-pair,
    or they lie in two distinct r-pairs of opposite m=24 pair-product.

This is a uniform necessary compatibility condition, not a chosen-pair search and not an exclusion of (a2). ∎

## Dependencies and residual

Uses `rank6-112-L16-s8-s10-exclusion-v7.md` §3, the v11/v12 (a2) reductions, and `rank6-112-L16-s12-d5-antipodal-pairs-sublemma-v15.md` (SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`), with all its v13/v14 and exact admitted-cut dependencies. These author conclusions remain independently unreviewed and unadopted.

The same (a2), (a3), (a4) distinct-inactivity, s=15 and s=16 L16 cases remain OPEN; no witness, unrestricted exclusion, whole residue-type exclusion, (24,24,2) closure or novelty is claimed. Existing findings, early-stop disclosure, HOLD and every NONINPUT restriction remain binding.
