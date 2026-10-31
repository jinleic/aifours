# Balanced NL242 (3,112), L=16, s=12, d=5: the forced m=24 slices have negative sign product

Owner: InfoBalancedNL242-2, info-6; continuation handle InfoBalancedNL242-2-2. Native `/bin/date` observed before this write: 2026-10-27T09:53:43-0700 PDT.

**WRITTEN AUTHOR CANDIDATE, NOT REVIEWED OR ADOPTED.** This is a proper sublemma conditional on the preceding author-only v205 chain; it is not an exclusion of any of the remaining variants. It uses handwritten algebra only. No interpreter, numerical search, solver, replay, model CLI, nested agent or new GO is used. No formal, kernel, novelty, witness, whole-type or unrestricted-exclusion claim follows.

## Scope and premises

Work only in the surviving v12/v13 cases: (a2), (a3), and (a4) with distinct inactive slices. The v11/v12 reductions identify, respectively, one m=24 p-active slice in (a2)/(a3), or both single-carrier slices in (a4). In any such slice exactly the 12 points of Σ in the affine 5-flat Π are active inside Π, and there is exactly one active balanced coset p outside Π. In (a2), two of those Σ-cosets have two same-sign small values and are both active; all other Σ-cosets have one. In (a3)/(a4), all 12 are single. The reduced slice signs g_η(x) are ±1 on Σ, including at the active double cosets. Write Γ_η := ∏_{x∈Σ} g_η(x).

The slice-zero structure v13 gives ĥ_0(x)=−8g_0(x) on Σ. Write c_x=(−1)^{D̄(x)}, s_x=υ_0(x), and denote v13's moment function by 𝒢(x). The census is

    c_x s_x = 4 − (3/2)𝒢(x) − 4 c_x g_0(x)       (x∈Σ).

The v11/v13 moments on Π, with γ=𝒢/4, are

    (a2),(a3):  Σ_Π γ = 80−4a,  Σ_Π γ² = 176−8a,  a∈{3,4};
    (a4):       Σ_Π γ = 72,      Σ_Π γ² = 176.

These are used as **author-only premises**, not as newly accepted results.

## Claim

In every such m=24 slice, Γ_η=−1. Consequently its 32 quotient-class sums Ψ_η are ±2 at exactly 24 classes and ±6 at exactly 8 classes. No claim is made about the other slice signs, the number of surviving configurations, or complete exclusion.

## Proof

Suppose Γ_η=+1. Since Σ has 12 points and their XOR is zero, all class sums are multiples of 4. Parseval gives Σ_classes Ψ²=384. The 24 classes not divisible by 3 have magnitudes 4 or 8; the other classes have magnitude 0 or 12. Thus

    384 = 16·24 + 48 n_8 + 144 n_12,

so n_8=n_12=0 and every Ψ is 0 or ±4. For centred reduction φ modulo 3, φ(Ψ)=Ψ/4.

Pair the two dual points over each class, using the linear normal ω of Π. On Π the outside p-character changes sign while the Σ-characters have the same common affine factor. The identity φ(z+1)+φ(z−1)=−φ(z), and u_η=−φ(Ψ+g_η(p)χ_p), give for x∈Π

    υ_η(x) = Σ_classes φ(Ψ(ζ)) χ_x(ζ) = 8 g_η(x)  if x∈Σ,
                                                    0  if x∉Σ.

Here arbitrary class representatives are used consistently; their affine common factors cancel in the product. The last equality is character orthogonality on Π's direction space. The sign of the active p term is immaterial to the paired identity.

We next show that each Σ-coset has 𝒢(x)=4. Put e=+1 for a −12 small T-value and e=−1 for a +4 small T-value, so a small entry is −4−8e and its δ sign is e c_x. Each large entry is −4+24ε with ε∈{±1}. Let t be the slice character at a small entry.

* **One small entry.** Then g_0=e c_x and g_η=e c_x t. Of the other three slice characters, one equals t and two equal −t. The equation 8c_xυ_η=64e t forces ε_same−ε_opp,1−ε_opp,2=3e, so the three large signs are e,−e,−e. Hence c_x s_x=−2−4e. Substitution in the census with c_x g_0=e gives 𝒢(x)=4.
* **Two same-sign small entries active in η.** Their characters both equal t and the two large entries have character −t. Centred reduction gives g_0=−e c_x and g_η=−e c_x t. The equation 8c_xυ_η=−64e t forces the sum of the two large signs to be 2e. Hence c_x s_x=−2+4e. Substitution in the census with c_x g_0=−e again gives 𝒢(x)=4.

There are exactly 12 points in Σ, so γ=1 at all 12. Applying Cauchy–Schwarz to the other 20 points of Π contradicts each of the prior moment pairs:

    (a2)/(a3), a=3: 56² = 3136 > 20·140 = 2800;
    (a2)/(a3), a=4: 52² = 2704 > 20·132 = 2640;
    (a4):           60² = 3600 > 20·164 = 3280.

Thus Γ_η≠+1, and therefore Γ_η=−1. For Γ_η=−1, the class sums are ±2, ±6 or ±10. Exactly 24 are not divisible by 3. Parseval is saturated by 24·2²+8·6²=384, so no magnitude 10 occurs and the asserted multiplicities follow. ∎

## Exact dependency and status

- `rank6-112-L16-s12-d5-partial-v11.md`, SHA-256 `d45cd94578572aea26bd035f5e18893de08230e48675e0a47c54c2302b77fc47`, 67 LF.
- `rank6-112-L16-s12-d5-variants-v12.md`, SHA-256 `7aac4fe052ed17aea9b3b41ce4354115f6f17edface0be1ac93bdff720890b7f`, 55 LF.
- `rank6-112-L16-s12-d5-six-character-structure-v13.md`, SHA-256 `59fdd87fc77e24c2b426a017d98b6ebf33063d4ad06520ccd1d2964cfcb8ab9c`, 40 LF.
- `rank6-112-L14-s12-exclusion-v3.md`, SHA-256 `3a29e8171f3b8eb7b2fc8f51ace4ae0df92d8f9c80b04f49c381fe2dbda2d62b`, 87 LF; only its m=24 class arithmetic and slice notation are used here.
- `rank6-lifted-floors-consolidated-proof-v1.md`, SHA-256 `6c5ce361f12e0335c5dbfc49f783bb5f926a7575e04bfd929a851d6aaf55b929`, 214 LF; its admitted S0017 (3), (6), ordinary character orthogonality, and author-only census/moment derivations are used at the cuts stated therein.

All source-chain assumptions remain subject to entire independent review. The s=12/d=5 variants remain open, as do s=15 and s=16. The original witness-or-unrestricted-exclusion problem and (24,24,2) gap remain open. HELD/ZERO/NONINPUT cuts and all prior findings remain binding; novelty is UNCLEARED.
