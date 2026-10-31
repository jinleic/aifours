# info-6: universal dual-enumerator consequences and the exact remaining implication

Owner **InfoBalancedNL242-2-2**, same original slot. The actual pre-body ACK was written at native observation **2026-10-27T17:13:30-0700 PDT**, before opening the three newly released inputs or doing mathematics. Native `/bin/date` before this output: **2026-10-27T17:16:09-0700 PDT**. **NEW WRITTEN AUTHOR RESULT; UNREVIEWED AND UNADOPTED.** Every claim below applies simultaneously to **every** solution of the complete released enumerator constraints. No distribution, code, function, small case, state, boundary instance or numerical probe was selected; no numerical LP/CAS, solver, enumeration or scientific executable was used.

## 1. Setup and result

Let nonnegative integer A_t, −7≤t≤7, count the nonzero codewords of weight 128+t, and let the nonnegative integers D_j, 0≤j≤256, obey **all** released dual identities. Retain simultaneously

    Σ A_t=511,     Σ t A_t=128,     Σ t² A_t=16384,
    Σ_{t odd} A_t=256,    Σ_{t even} A_t=255,
    A_{−7}+A_7≥92,
    512 D_j=binom(256,j)+Σ_t A_t K_j(128+t),
    D₁=D₂=D₂₅₆=0,      5163≤D₃≤5760,                         (1)

for every j, with K_j as the released binomial sum. These remain necessary conditions on a full actual code, not sufficient conditions for one.

The complete system necessarily also has

    5296 ≤ D₃ ≤ 5594,      30 ≤ D₂₅₄ ≤ 71,     0 ≤ D₂₅₅ ≤ 11,  (2)

and the **signed odd-weight congruence**

    (A₃−A₋₃) + 5(A₅−A₋₅) + 14(A₇−A₋₇) ≡ 0  (mod 8).         (3)

These are universal consequences, not a claim that the full system is feasible or infeasible. The proof uses the stated numeric constraints only; no separate actual-code closure or extra structural assumption is substituted for them.

## 2. All-index complement identity and high dual indices

For every w and j, complementing a j-subset of the 256 coordinates gives

    K_{256−j}(w)=(−1)^w K_j(w).                                 (4)

Indeed the complement contains w−i ones when the original subset contains i, so its character sign changes by (−1)^w. From the binomial definition, or from the same elementary expansion,

    K₁(128+t)=−2t,       K₂(128+t)=2t²−128,
    K₃(128+t)=(−4t³+766t)/3.                                   (5)

For completeness, let F(z)=(1−z)^w(1+z)^{256−w}=Σ_j K_j(w)z^j. Direct differentiation gives (1−z²)F'(z)=[256−2w−256z]F(z). Comparing z^j coefficients yields (j+1)K_{j+1}=(256−2w)K_j−(257−j)K_{j−1}, with K₀=1 and K₁=256−2w. Substitution at j=1 and j=2 proves all of (5). No enumerator table is imported.

Write O_r=Σ_{t odd}t^r A_t and E_r=Σ_{t even}t^r A_t. Then E₁+O₁=128 and E₂+O₂=16384. Applying (4)–(5) at j=1,2 and using the two parity counts gives the exact identities

    O₁=128 D₂₅₅,       O₂=128(128−D₂₅₄).                       (6)

For example, 512D₂₅₅=256−2(E₁−O₁)=4O₁; and 512D₂₅₄=32640+2(E₂−O₂)−128(255−256)=65536−4O₂. In particular O₂ is a multiple of 128.

Since the 255 even t values have |t|≤6, E₂≤36·255, hence O₂≥7204. Since the 256 odd t values have |t|≤7, O₂≤49·256=12544. The multiples-of-128 condition in (6) sharpens this to 7296≤O₂≤12544 and therefore 30≤D₂₅₄≤71.

For d=D₂₅₅, Cauchy's inequality applied separately to the two parity classes gives

    (128d)²/256 + (128−128d)²/255 ≤ 16384.

Equivalently 511d²−512d−65024≤0. If d≥12 then

    511d²−512d−65024=(d−12)(511d+5620)+2416>0,

contrary to that inequality. Since D₂₅₅ is a nonnegative integer, 0≤D₂₅₅≤11. This is a universal algebraic bound, not an evaluated code or selected parameter.

## 3. Signed odd-weight congruence

Taking the difference of the j=3 and j=253 identities and using (4)–(5) yields

    768(D₃−D₂₅₃)=−4O₃+766O₁.

Substitute O₁=128D₂₅₅ and rearrange:

    O₃−O₁ = 192(127D₂₅₅−D₃+D₂₅₃).                             (7)

For odd |t|≤7, t³−t is zero at |t|=1 and is respectively ±24, ±120, ±336 at |t|=3,5,7. Divide (7) by 24 to obtain (3). The calculation covers both signs and every odd weight simultaneously; it does not choose a weight distribution.

## 4. Stronger D₃ interval from nonnegative polynomials

Define the polynomials, nonnegative for every real t∈[−7,7],

    P(t)=(7−t)(t+7)² =343+49t−7t²−t³,
    Q(t)=(7+t)(t−7)² =343−49t−7t²+t³.

For each **even** allowed t, |t|≤6. Moreover

    P(t)−13=(t+6)(55−t−t²)≥0,
    Q(t)−13=(6−t)(55+t−t²)≥0,

because |t|≤6 implies t²±t≤42. All other contributions to both sums are nonnegative. Since there are exactly 255 even-weight nonzero words,

    Σ_t A_t P(t)≥13·255,      Σ_t A_t Q(t)≥13·255.

Putting M₃=Σ t³A_t and substituting the three released moments gives

    Σ A_t P(t)=66857−M₃,      Σ A_t Q(t)=54313+M₃,
    −50998 ≤ M₃ ≤ 63542.                                        (8)

The released exact relation M₃=2²¹−384D₃ and integrality now yield 5296≤D₃≤5594, proving the first part of (2). This tightens the prior necessary D₃ interval only; it does not establish any code.

## 5. Exact gap and provenance

The displayed deductions use some consequences of the **complete simultaneous** constraints and preserve all 15 counts and all j; they do not discard any j, original rank/weight or `(24,24,2)` alternative. Their individual integer intervals are nonempty, so this derivation does not itself yield a contradiction. It does **not** prove that these intervals can be attained together, nor exhibit a satisfying distribution. The precise unresolved implication is whether all 15 nonnegative counts and all 257 nonnegative dual counts can satisfy (1) simultaneously. Even a complete proof that this numerical constraint system is consistent would not construct a code, its 256 distinct nonzero columns, or an original Boolean witness. A universal contradiction to (1), combined with the exact reviewed code-equivalence gate at its proper acceptance level, would exclude the original target; neither has been established here.

Before this output the native SHA-256/LF pins were verified: original packet `info-6-full-walsh-packet-v1.md` `a9931cf5a12f174c232e6ad50fba993e5cd01ee9d4ab13dcfe0bd35dc69d3d37` 35 LF; source `walsh-projective-code-equivalence-v1.md` `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb` 50 LF; source-gate return `review-w81-info-6-projective-code-source-gate-v1.md` `cd924d090ef17822010b68223af6c5445d068a8a2cc483ff34465723316edef8` 189 LF; ACK `dual-enumerator-prebody-ack-v1.json` `9d4776d632f485b2ee3234385ac213d64f8617bfa89fdc64acdd29358fe6584b` 17 LF. The w81 return reconstructed its frozen claims with 0F/0M/0m but expressly did **not** certify method noninfluence; only the released enumerator statements are used here.

No half-split/sector or canonical transform, truth-degree/ANF, Gate-I, post052 route, post054 selected diagnostic, L1, held source or consumer was used. Both owner PROCESS MAJORs, L1 quarantine, every prior STOP/HOLD/ZERO, mandatory w44/count-direction corrections, N4 UNKNOWN and auxiliary214 STOP persist. No witness, no-go, novelty, independent-model, human, formal/kernel or executable claim is made.
