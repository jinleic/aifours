# Balanced NL242 (3,112), L=16, s=12, d=5: variant (a2) excluded

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:04:38-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This claims exclusion of the entire previously defined (a2) variant, conditional on the source-separated v205 chain through v16. It is not a whole-L16, whole-type, witness, unrestricted-exclusion, formal/kernel or novelty result. The proof is exact all-variable hand reasoning, with no selected numerical probe or scientific execution.

## Premises

In (a2) there is one balanced coset p outside Π and two double-valued Σ-cosets y,z. In the p-active m=20 slice η, both y,z are inactive and all ten other Σ-cosets are active with signs ±1. Let A=Σ\{y,z}, Ψ its class transform, and N={ζ:3|Ψ(ζ)}. For v in Π's direction W, let F(v)=Σ_{ζ∉N}χ_ζ(v). As p is the sole outside coset and vanishes in its inactive slice, the single-carrier formula and the pure-coset slice lemma give

    F(v)∈{0,±4} for every v∈W\{0}.                              (1)

By v16, Ψ has exactly eight values 0, twelve ±2, eight ±4 and four ±6; in particular |Ψ|≤6 and |N|=12. By v15/v16, Σ consists of six r-pairs whose six labels in W/⟨r⟩ form an affine six-point circuit: any five are affinely independent and the sum of all six labels is zero. On a nonzero v, Σ_{ζ∈N}χ_ζ(v)=−F(v). We show each possible location of y,z violates (1).

## Case I: y,z are the same r-pair

The ten active points form five complete pairs. Let k of the five have positive sign product in η. In the half of classes with χ(r)=+1, Ψ is twice a sum of k signed characters; in the other half it is twice a sum of 5−k signed characters. If either group has at least four pairs, its signs can all agree in some class: those at most five pair labels are affinely independent. This would give |Ψ|≥8, contrary to v16. Thus the groups have sizes two and three.

Let x₁,x₂ be representatives of the two-pair group and v=x₁+x₂. Then v is neither 0 nor r. In that group's r-half, N consists exactly of the eight classes where the two signed character terms are opposite, so the N-transform at v has magnitude 8. In the other r-half, N consists of the four classes where the three terms of the three-pair group agree. Their transform at v is zero: otherwise v modulo r would belong to the span of the two differences within that triple, hence equal a difference of two of its labels, producing a forbidden four-label relation with x₁,x₂. Therefore |Σ_Nχ(v)|=8, contradicting (1).

## Case II: y,z are in distinct r-pairs

There are four complete active pairs and one surviving point in each of two other pairs. Choose representatives x₁,…,x₆, using the surviving point for each incomplete pair. For a class ζ write sᵢ(ζ)=aᵢχ_ζ(xᵢ), where aᵢ is its active sign at xᵢ. The quotient labels form a six-point circuit, so their representative sum lies in ⟨r⟩. Hence, in either fixed χ(r)-half, ∏ᵢsᵢ is a constant κ∈{±1}. Moreover, modulo simultaneous reversal of all six signs, every sign pattern with that product is realized: the five relative characters have exactly the single circuit relation and rank four. Simultaneous reversal does not change |Ψ| or membership in N.

If k of the four complete pairs have product +1, then in one r-half Ψ is twice the sum of those k signed terms plus the two singleton terms, and in the other half it is twice the sum of the remaining 4−k terms plus the same singleton terms.

- If a half contains four complete pairs, then either its constant κ=+1, in which case the pattern with all six signs equal gives |Ψ|=10, or κ=−1, in which case the four pair signs can agree and the singleton signs be opposite, giving |Ψ|=8. Both patterns have the required product and are realized.
- If a half contains three complete pairs, take its three pair signs and both singleton signs equal, and choose the sixth sign to give the required product. This gives |Ψ|=8.

Both contradict |Ψ|≤6. Therefore exactly two complete pairs contribute in each half. Relabel them so the + half uses pairs 1,2 and the − half uses 3,4; 5,6 are singleton points.

On the + half, Ψ=2(s₁+s₂)+s₅+s₆. Its six classes in N split into:

- four classes with s₁=−s₂ and s₅=−s₆, where Ψ=0;
- two classes with s₁=s₂=s₅=s₆, where |Ψ|=6.

The counts follow from the independent two or three pairwise-character equations on four distinct circuit labels. Set v=x₁+x₂ and u=a₁a₂. On these six classes the sum of χ(v)=s₁s₂/u is therefore −2/u.

On the − half, Ψ=2(s₃+s₄)+s₅+s₆. For every class in N, the same two alternatives imply (s₃s₄)(s₅s₆)=+1. The product of all six sᵢ is a constant κ₋ in this half, so s₁s₂=κ₋ throughout its six N-classes. Their contribution to the N-transform at v is therefore 6κ₋/u. Adding the halves gives

    Σ_Nχ(v)   = (−2+6κ₋)/u,
    Σ_Nχ(v+r) = (−2−6κ₋)/u.

Exactly one of these two magnitudes is 8. Both v and v+r are nonzero, since x₁,x₂ are in distinct r-pairs. This contradicts (1). ∎

## Exact status

Conditional on the entire cited author chain, **(a2) is excluded**. The remaining L16 cases are (a3), distinct-inactivity (a4), s=15 and s=16. The prior L≥16 at (3,112) and L≥12 at (3,144) remain author-only; neither floor is independently reviewed. No whole residue type or original target is excluded, and the original witness-or-unrestricted-exclusion and (24,24,2) gaps remain open.

Dependencies include `rank6-112-L16-s12-d5-pair-circuit-and-a2-sublemma-v16.md` SHA-256 `664f9ef3d9237c0862ca493f16b0b54550e188d29d6fcc29072047dfd4ffbfab`, 47 LF; v15 SHA-256 `10b9867ec2c76ed19c83a0023733996cd46cde9b950c5d9239866babbb15b0eb`, 49 LF; and the v11–v14 chain and exact admitted cuts cited there. Earlier errata, pre-pin corrections, HOLD, N4 UNKNOWN, aux214 STOP, and all HELD/ZERO/NONINPUT restrictions remain binding. Novelty UNCLEARED.
