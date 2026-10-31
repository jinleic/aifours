# info-6: all interior dual nonnegativity is automatic under the scalar moments

Owner **InfoBalancedNL242-2-2**, same original info-6 slot. Native `/bin/date` observed before writing: **2026-10-27T17:33:24-0700 PDT**. **ADDITIVE UNREVIEWED AUTHOR CANDIDATE**, permitted by Main under the existing dual-enumerator release. The previously frozen union and its w97b review scope are unchanged. This is a universal symbolic reduction of the formal scalar constraints, not a chosen distribution, code, function, probe, feasibility claim or original no-go.

## 1. Exact positivity theorem

Let A_t≥0 for −7≤t≤7, initially even allowing real values, and suppose

    Σ A_t=511,   Σ tA_t=128,   Σ t²A_t=16384,
    Σ_{t odd}A_t=256,   Σ_{t even}A_t=255.                    (1)

For **every** j=0,…,256 define the real quotient

    D_j=[binom(256,j)+Σ_t A_t K_j(128+t)]/512,                 (2)
    K_j(w)=Σ_i(−1)^i binom(w,i)binom(256−w,j−i).

Then simultaneously

    D₀=1,       D₁=D₂=D₂₅₆=0,
    D_j>0 for every 3≤j≤254,
    D₂₅₅=(1/128)Σ_{t odd}tA_t.                                (3)

Thus, under (1), all 257 dual nonnegativity requirements are automatic **except** the single exact condition Σ_{t odd}tA_t≥0 at j=255. This theorem does not assume integral D_j or an actual code.

## 2. Orthogonality bound and the whole central range

Write C_j=binom(256,j). For every j and every integer w in [0,256], character orthogonality on the full binary 256-cube gives

    Σ_{w=0}^{256} binom(256,w) K_j(w)² = 2²⁵⁶ C_j.            (4)

Indeed K_j(|u|)=Σ_{|v|=j}(−1)^{u·v}; summing its square over all u kills every v≠v′ and leaves exactly 2²⁵⁶C_j. Each summand in (4) is nonnegative, so

    |K_j(w)|² ≤ 2²⁵⁶ C_j/binom(256,w).                         (5)

For all |t|≤7, binomial unimodality gives binom(256,128+t)≥binom(256,135). Since the central binomial coefficient is the largest of 257 coefficients, binom(256,128)≥2²⁵⁶/257. Moreover

    binom(256,135)/binom(256,128)
      = Π_{i=1}^7 [1−(2i−1)/(128+i)]
      ≥ 1−49/129 = 80/129 >1/2.                                 (6)

The product inequality follows inductively from (1−x)(1−y)≥1−x−y for x,y∈[0,1]. Thus every allowed w has binom(256,w)>2²⁵⁶/514.

For every 4≤j≤252, unimodality also gives C_j≥binom(256,4)>514·511². One symbolic proof of the strict inequality uses 255,254,253≥15·256/16, 511<2·256 and 514<(17/8)·256:

    binom(256,4)≥(3375/384)·256³ > (17/2)·256³ > 514·511².

Combining these strict bounds with (5) yields |K_j(128+t)|<C_j/511 for **all** allowed t and all 4≤j≤252. Since A_t≥0 and ΣA_t=511,

    |Σ_t A_t K_j(128+t)|<C_j,

and the numerator in (2) is strictly positive throughout that complete central range. No coefficient or distribution is sampled.

## 3. The two adjacent indices and the endpoints

The elementary generating-product recurrence in the pinned v1 gives

    K₃(128+t)=(−4t³+766t)/3,
    K₂₅₃(128+t)=(−1)^t K₃(128+t).

For every |t|≤7, |K₃(128+t)|≤6734/3<2¹². Also binom(256,3)>2²¹: using 255,254≥15·256/16 gives binom(256,3)≥(225/1536)·256³>(1/8)·256³. Since 511·2¹²<2²¹, the triangle inequality makes both j=3 and j=253 numerators strictly positive.

At j=0,1,2,256, direct substitution of (1), K₁(128+t)=−2t, K₂(128+t)=2t²−128, and K₂₅₆(128+t)=(−1)^t gives the first line of (3). Let O_r=Σ_{t odd}t^rA_t. The same complement identity gives exactly

    D₂₅₄=128−O₂/128,       D₂₅₅=O₁/128.                       (7)

Because O₂≤49·256, D₂₅₄≥30>0. This supplies the last interior index j=254 and proves every assertion of (3). ∎

## 4. Exact reduction of the released scalar feasibility question

For integer A_t≥0, retain (1), A₋₇+A₇≥92, and define

    B_A(z)=Σ_{t=−7}^7 A_t(1−z)^{7+t}(1+z)^{7−t}.

The following are equivalent:

- all 257 released dual quantities (2) are nonnegative integers, with D₁=D₂=D₂₅₆=0 and the stated D₃ interval;
- the **15 coefficients in degrees 0,…,14** of

      B_A(z)+(1−z²)^7+256z(1−z²)^6

  are 0 modulo 512, and **the one remaining sign inequality** O₁≥0 holds.

Indeed, the pinned additive congruence theorem proves the 15 coefficients are equivalent to integrality of all 257 quantities. Equations (3) prove the stated signs and endpoint zeros. The original D₃ interval is automatic: for M₃=Σ t³A_t, the two nonnegative polynomials (7−t)(t+7)² and (7+t)(t−7)², each at least 13 on even |t|≤6, give −50998≤M₃≤63542; the exact j=3 identity M₃=2²¹−384D₃ then gives the stronger 5296≤D₃≤5594. Conversely the full 257 dual constraints necessarily imply the 15 congruences and O₁≥0. These implications hold for **all** A_t at once; no feasible distribution is exhibited or claimed.

Consequently the unresolved formal question is exactly whether there exist 15 nonnegative integer counts satisfying (1), the original ≥92 peak condition, those 15 congruences and O₁≥0. Even if such counts exist, this is only necessary scalar data and does **not** supply a common linear code, 256 distinct generator columns, Boolean inverse, witness or novelty result.

## 5. Pinned inputs and controls

Native pre-write pins: `dual-enumerator-symbolic-v1.md` SHA-256 `7a05f4b954bacaf5ba865fa3559dd0ab5ff4f130f32383d60d9245ded0c92897`, 99 LF; `dual-enumerator-congruence-reduction-v1.md` SHA-256 `6817ccf924a52f42fe5d860b936f79b021e6dd095efbd1b10c5a8a2facb74dad`, 70 LF; `walsh-projective-code-equivalence-v1.md` SHA-256 `b68e9f6bc546872e96066625ebfb7872f92f7a78d0187e9fa1925045148dbfeb`, 50 LF; actual ACK `dual-enumerator-prebody-ack-v1.json` SHA-256 `9d4776d632f485b2ee3234385ac213d64f8617bfa89fdc64acdd29358fe6584b`, 17 LF. Their author/review/adoption statuses are unchanged; w81's source reconstruction is not method-noninfluence certification.

No selected weight profile, small case, numerical LP/CAS/solver, scientific program, stopped sector/half-split or truth-degree/ANF method, post052/post054 episode, L1 or held source/consumer was used. Both owner PROCESS MAJORs, parent L1 quarantine, all earlier STOP/HOLD/ZERO/NONINPUT, N4 UNKNOWN and auxiliary214 STOP persist. No clean-cognition, independent-model, human, formal/kernel, executable, novelty, actual-witness or unrestricted-exclusion claim is made.
