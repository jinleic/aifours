# info-6: simultaneous energy congruences on every affine frequency partition

Owner **InfoBalancedNL242-2-2**, same info-6 slot. Actual `/bin/date` observed before this write: **2026-10-27T14:51:47-0700 PDT**. **NEW WRITTEN AUTHOR CANDIDATE, UNREVIEWED AND UNADOPTED.** This extends the all-hyperplane necessary coupling without selecting a subspace or object. It is not a witness, unrestricted exclusion, rank/type exclusion, numerical improvement, formal/kernel or novelty result. No scientific program, selected-state probe or external-model review was used.

## Claim

For every balanced f:F₂⁹→{0,1}, let W be its actual Walsh transform and k=W/4. For every spatial subspace T≤F₂⁹ of dimension r with 1≤r≤8, and every two characters λ,μ of T, put

    E_λ := Σ_{a:a|_T=λ} k(a)².

The **same actual array** simultaneously satisfies

    E_λ ≡ 0 (mod 2^{8−r}),
    E_λ ≡ E_μ (mod 2^{9−r}).                                    (1)

The first congruence at r=8 is understood modulo 1. At r=1 this contains the previous all-hyperplane energy bound; at other r it couples every affine partition of the frequency space, including partitions with zero frequency. This is necessary only, not a sufficiency theorem.

## Proof

Let M={x:f(x)=1}, so |M|=256. Partition the source space into affine T-cosets C=x_C+T. For every λ∈T* define

    S_{C,λ}=Σ_{t∈T} (-1)^{f(x_C+t)+λ(t)},    u_{C,λ}=S_{C,λ}/2.

The u are integers because T has even size. Character orthogonality on the frequency coset gives the exact all-block relation

    E_λ = 2^{5−r}Σ_C S_{C,λ}² = 2^{7−r}Σ_C u_{C,λ}².             (2)

This also holds for r=8, when the coefficient is 1/2; the expression is then integral because the left side is a sum of integer squares. Choices of x_C affect signs but not squares.

Write n_C=|M∩C| and J_T=#{C:n_C is odd}. Since Σ_C n_C=256, J_T is even. For nonzero λ,

    u_{C,λ}=−Σ_{t∈T} f(x_C+t)(−1)^{λ(t)} ≡ n_C (mod 2).

For λ=0, u_{C,0}=2^{r−1}−n_C. Its parity is n_C for r≥2; for r=1 it is the opposite parity. There are 256 source cosets when r=1, and 256−J_T≡J_T (mod 4) because J_T is even. Hence, for **every** λ,

    Σ_C u_{C,λ}² ≡ J_T (mod 4),   J_T≡0 (mod 2).                  (3)

Combining (2)–(3) gives (1). For r=8 divide the congruence of the two sums by 2; their evenness makes the resulting mod-2 statement valid. For r=1 both E-values are multiples of 128 and agree modulo 256, consistently strengthening the separate half-energy divisibility. No orientation, origin, T or frequency coset is selected. ∎

## Exact scope and residual

An abstract magnitude array violating any one of the simultaneously quantified congruences cannot be the squared Walsh array of an actual balanced Boolean function. The family may be used as a **necessary** filter without assigning phase signs, but no selected profile has been tested, no particular forbidden rank/weight has been chosen, and no claim is made that the filters alone imply the 512 Boolean inverse bits. The exact common-array autocorrelation and caller remain as in `prerequisite-derivation-v1.md`, SHA-256 `075f61ffe1b5cfb000bb3bbda9ddd7fefea04e27806f19bedd9c5a2318fa3df9`, 87 LF.

The unrestricted open step is still an actual balanced peak-28 witness or an exclusion covering **all** arrays that satisfy the coupled conditions. The parent-supplied definitions are not independently certified against the book; full-scope written review, human, formal/kernel, executable and novelty gates remain unperformed. Prior authored exposure and every S1 HELD/ZERO/NONINPUT, STOP/HOLD, N4 UNKNOWN and aux214 STOP remain binding.
