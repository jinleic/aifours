# Balanced NL242 (3,112), L=16, s=12, d=4: direct distinct-inactivity exclusion

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T10:59:43-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This is a same-author alternative to the distinct-inactivity argument of v10, not an independent review. It uses the v9 reductions and the v32 zero-slice derivation, but avoids the second-moment/Cauchy bound. No scientific program, selected-state probe, accepted floor, witness, formal/kernel or novelty claim.

## 1. One single-carrier slice controls every Σ-row

In v9's distinct-inactivity case all twelve Σ-cosets are single; in any single-carrier slice η, m=12 on the 16 Π-dual classes. Write Γ_η=∏_Σg_η and J for the unnormalised four-character transform below.

If Γ_η=+1, Parseval gives Ψ∈{0,±4}, so φ(Ψ)=Ψ/4 and affine-class pairing gives υ_η=8g_η on Σ, as in v34.

If Γ_η=−1, Parseval gives twelve Ψ of magnitude 2 and four of magnitude 6. Let N be the four |Ψ|=6 frequencies and let ε=Ψ/6 on N. Then

    φ(Ψ)=−Ψ/2+3ε·1_N,    υ_η(x)=−16g_η(x)+6J(x)  on Π,
    J(x)=Σ_{ζ∈N} ε(ζ)χ_ζ(x).                                     (1)

For a Σ-coset with one small entry, its T-row gives υ_η/g_η∈{−10,−4,2,8}. Since J is a sum of four signs, (1) forces J/g_η∈{2,4} on each of the twelve points; in particular J has at least twelve nonzero values.

Four distinct frequencies are either affinely independent, or an affine plane. In the first case a signed four-character sum has exactly ten nonzero values on F₂⁴; in the plane case its sign product +1 gives four nonzero values, while product −1 gives magnitude 2 everywhere. Thus N must be a negative-sign plane, J/g_η=2 on every Σ point, and υ_η=−4g_η there.

## 2. The Π-class contribution is at most 160

Write 𝒢(x)=c_x·Walsh(σ1_Z)(x), s_x=υ₀(x), and use the census

    c_xs_x=4−(3/2)𝒢(x)+c_xĥ₀(x)/2.                              (2)

By v32, ĥ₀=4g₀ on Σ and equals −12εχ_{ζ*} on the four points C=Π\Σ. For x∈Σ put e=c_xg₀(x)∈{±1}. Its one small T-entry is −4−8e; write the three large entries −4+24ε_j and B=Σε_j. Then c_xs_x=−2−e+3B.

- In the Γ_η=+1 case, υ_η=8g_η forces the three ε_j to be e,−e,−e, so B=−e.
- In the Γ_η=−1 case, υ_η=−4g_η forces e(ε_same−ε_opp,1−ε_opp,2)=−1, hence B is either 3e or −e.

Substitution in (2) gives 𝒢(x)=4+2e−2B∈{0,8} on every x∈Σ. Each x∈C is pure. If k of its four entries are −28 and q=c_xεχ_{ζ*}(x)∈{±1}, then (2) and c_xs_x=10−6k give 𝒢(x)=4(k−1−q)≤16. Therefore

    Σ_{x∈Π}𝒢(x)≤12·8+4·16=160.                                 (3)

## 3. The other classes force at least 192 on Π

v9/v10 give 𝒢=4 on the two outside-carrier classes, including p,p′, so those 32 cosets contribute 128. In the remaining outside class, 12 pure cosets have k=2 and 𝒢=4; the four others are monochromatic with 𝒢∈{−4,12}, giving at most 96. Since N₀=52 by v32, the first moment is Σ_all 𝒢=8N₀=416. Hence the Π-class must contribute at least 416−128−96=192, contradicting (3). ∎

## Limits and dependencies

This excludes only v9's d=4 distinct-inactivity subcase at author-candidate level; the same-inactivity case still depends on v9. Uses `rank6-112-L16-s12-d4-partial-v9.md` SHA-256 `b489d713eb9473bf224931096afadb3394db74290145f97ca94f99948ca84bcf`, 69 LF; `rank6-112-L16-s12-d4-exclusion-v10.md` SHA-256 `c52b0f6512cf05bf35e745c2d2628fde22c1c6e7cf34bc8d024cbffeace67e62`, 47 LF; `rank6-112-L16-s12-d4-zero-slice-derivation-v32.md` SHA-256 `0478ceadc45b2c799c2e9b24acca48c99458e117cc4d4019c8064f6b2ea1d9c0`, 33 LF; and their stated source cuts. No independent review, whole-type exclusion, original witness, unrestricted exclusion, (24,24,2) closure or novelty follows. All findings including the v10 precision finding, v263 early-stop deviation, HOLD, N4 UNKNOWN, aux214 STOP and HELD/ZERO/NONINPUT remain binding.
