# f5 — physical depolarizing mirror, three-erasure bound and one-uniform k3

Reviewer **PhysicsMOQLS8-2**, author **PhysicsDepol4-2**. Native clock before writing: **Wed Oct 28 17:16:36 PDT 2026**. This is a same-harness written reconstruction plus independent exact finite checks, not formal/kernel, configured-model-family, human, or novelty acceptance.

## 1. Actual scope, inputs and verdict

I read the COMPLETE assignment FIRST, then all189LF of the three complete candidate bodies including their endings. Native pins matched:

|Input|LF|SHA256|
|---|---:|---|
|assignment-v1.json|32|ab8da34d00ac4051ab000cbc29b828cebb09724f368eb68a6f9453aecfaf9a66|
|frontier-20261028-01-spectral-mirror.md|63|4fb86d219a99daf54cbe7ab6c37a6a7fbd11c40009879d63ae135c5195cb4b1c|
|frontier-20261028-06-erasure-certificate.md|64|d33fa3cad8f26408e876163d975eb023821b6ab60bea8f220f82bfd1a73d5e2a|
|frontier-20261028-08-one-uniform-proof.md|62|980d9f111f3fb685dfec9449b8bfcb325f3761a19ec91bea0615401d7d46cb38|

The registered original all-density/all-physical-parameter majorization question and actual complex rank3 carrier are explicitly present in `physics/.../depolarizing-majorization4/intake-v1.md` LF20–34, which I read as a scoped definition/status source, not a fresh validation of its inherited parent results. The candidate files themselves supply every other needed equation. I do not import the author's prior numerical script outputs as reviewer evidence.

**Prior contact:** I am same-track physics-4 and have earlier depolarization status/control and quantum-matrix exposure. Parent L1 and other historical findings remain historical; no quarantined payload is used as a mathematical premise. This is not blind, human, formal, or configured-family-independent review. No author contact or external-model call occurred.

**Verdict: 0 FATAL / 0 MAJOR / 0 MINOR; NO_SUBSTANTIVE_DEFECT AT EXACT STATED SCOPE.**

|Gate|Supported exact statement|Boundary|
|---|---|---|
|Mirror candidate|For all complex four-qubit operators, `Λ_p(X)=Y Λ_(2−p)(X)^T Y` when both p and2−p lie in the physical interval; in particular p∈[1,4/3]. Spectra and same-input/deterministically mapped complex projectors match.|No global k3 inequality follows merely from mirror symmetry.|
|Erasure candidate|All actual densities and complex rank3 P obey `t3≤5/4`, sharp; product-reference coefficients and the same-pair sufficient reduction are exact.|The proposed global `t1≤3,t2≤3` remain UNPROVED; they are sufficient,not necessary.|
|One-uniform candidate|For every convex mixture of pure states with ALL four local marginals I/2,every actual complex rank3 P and every physical p, the exact candidate gap holds.|Only the stated convex hull; NOT every mixed state with local marginals I/2 or every four-qubit state. No all-index majorization follows from k3 alone.|

No old held outcome is adopted or repaired by this proof review.

## 2. Physical channel, product reference and exact mirror

The single-qubit map is `Φ_p(X)=(1−p)X+(p/2)Tr(X)I`; `Λ_p=Φ_p^⊗4`. For 0≤p≤4/3 this is a physical channel: directly expand

    Φ_p(X)=(1−3p/4)X+(p/4)(X_σ X X_σ+Y_σ X Y_σ+Z_σ X Z_σ).

The four coefficients are nonnegative and sum1. This supplies the physical endpoint independently of a historical channel claim.

For EVERY complex 2×2 X, entrywise multiplication gives `σ_y X^T σ_y=Tr(X)I−X`. Write S for this complex-LINEAR map. Since Φ_(2−p) preserves the trace,

    S Φ_(2−p)(X)=Φ_p(X).

Tensor this identity and check it first on the matrix-unit tensor basis,then by complex linearity on ALL four-qubit operators. With `Y=σ_y^⊗4=Y*=Y^T` and Y²=I,

    Λ_p(X)=Y Λ_(2−p)(X)^T Y.                                    (M)

For p∈[1,4/3],p'=2−p∈[2/3,1];both are physical. A Hermitian matrix and its transpose have identical real eigenvalues, and Y-conjugation preserves them. Thus the SAME rho produces equal entire output spectra,including multiplicities/degeneracies. For any rank3 orthogonal complex P,

    Tr[P Λ_p(rho)] = Tr[(Y P^T Y) Λ_p'(rho)].

`Y P^T Y` is PSD/Hermitian/idempotent of trace/rank3, and applying the map twice returns P. It is the deterministic image of the SAME original P,not an independently optimized copy. The formula works for arbitrary X in (M),not only Hermitian states.

For a pure product input the local output eigenvalues are `a=(1+|1−p|)/2`, `b=(1−|1−p|)/2`,a≥b≥0. The three greatest products are a^4 and two copies of a³b,even when ties occur. Hence

    R3(p)=a^4+2a³b=(1+|1−p|)^3(3−|1−p|)/16.

This is mirror-invariant. Thus the original all-density k3 assertion on the physical interval reduces EXACTLY to p∈[0,1];the same holds at any Ky-Fan index. The reduction is not itself proof of that assertion.

## 3. Actual erasure layers and common product maximizer

Set `E_i(X)=I_i⊗Tr_i(X)/2`,restoring tensor positions,and `E_S=∏_(i∈S) E_i`. These maps commute and, for the SAME rho,P,

    T_m=Σ_(|S|=m) E_S(rho),   t_m=Tr(P T_m),
    Tr(PΛ_p(rho))=Σ_(m=0)^4 (1−p)^(4−m) p^m t_m.              (E)

The expansion is a binomial expansion of commuting physical site maps for 0≤p≤1,where all five scalar weights are nonnegative. It is valid algebraically for any p,but the coefficientwise comparison uses this nonnegative range.

For `rho*=|0000><0000|` and P* spanning `|0000>,|1000>,|0100>`,E_S(rho*) assigns weight2^(−m) to every computational string supported in S. Therefore its SAME projector gives

    t_m*=2^(−m)[binom(4,m)+2 binom(3,m−1)]
        = (1,3,3,5/4,3/16).

The two chosen one-bit vectors are in the product output's second-largest degenerate eigenspace for every p∈[0,1];P* is an actual common maximizer,including endpoints. This is a single consistent reference projector,not independently optimized layer values.

For arbitrary density rho and rank3 P,positivity gives t0≤1;`T4=I16/16` gives t4=3/16. The universal t3 bound is proved next. If additionally `t1≤3` AND `t2≤3` were established for ALL actual SAME pairs,comparing each coefficient in (E) would imply the global original k3 bound for 0≤p≤1;§2 then extends it to all physical p. The converse need not hold because a weighted sum can be bounded without each coefficient being bounded separately. The two stated global layer inequalities are NOT established by these candidates.

## 4. Universal, sharp t3≤5/4 — all mixed inputs and complex P

For arbitrary rho,`T3=(1/8)Σ_i rho_i⊗I_(other three)`,with each term acting on its own tensor factor. Let the local eigenvalues be `(1±r_i)/2`,0≤r_i≤1;relabel r1≤r2≤r3≤r4 solely for the calculation. A product eigenbasis diagonalizes T3,with sixteen eigenvalues

    λ_ε=(4+Σ_i ε_i r_i)/16, ε_i∈{±1}.

The all-plus value and the two single sign flips at the smallest r's give three largest eigenvalues;if some r's vanish or coincide,other choices tie but the sum is unchanged. Their sum is

    (12+r1+r2+3r3+3r4)/16 ≤ 20/16 = 5/4.

For a Hermitian matrix H and ANY rank-k orthogonal P,diagonalize H:the weights `<e_j,P e_j>` lie in[0,1] and sum k,so their weighted sum is at most the sum of the k largest eigenvalues. Hence t3≤5/4 for the actual complex P;no separate chosen marginal projector is needed. The product reference in §3 attains5/4,so it is sharp.

Equality of the upper expression to5/4 forces each r_i=1. A positive density with a pure marginal is supported on that marginal's one-dimensional local factor:the trace on its orthogonal local factor is0,so positivity forces that entire block and its cross block to vanish. Iterating over four sites gives a pure product density. This establishes the candidate's density equality implication;it does not classify all maximizing projectors.

## 5. Pure one-uniform t0,t1,t3,t4 bounds

Now assume rho is PURE and EACH single-qubit marginal is I/2,with the same arbitrary rank3 P.

- `0≤t0=Tr(P rho)≤1` and `t4=3/16`.
- Across the i versus complementary-three cut,the Schmidt coefficients are exactly1/sqrt2,1/sqrt2. Thus `rho_(bar i)` has two nonzero eigenvalues1/2; `E_i(rho)=I_i/2⊗rho_(bar i)` has four nonzero eigenvalues1/4. The rank3 variational inequality from §4 gives each trace≤3/4,therefore **t1≤3**.
- Each local rho_i=I/2,so `T3=(1/8)Σ_i rho_i⊗I_(bar i)=I16/4`,and **t3=3/4 for EVERY P**,not only an optimizer.

The Schmidt fact is the elementary equality of nonzero eigenvalues of AA* and A*A for the two reshaped coefficient matrices. It is used on an actual complex pure state;no numerical state or real-only restriction enters the proof.

## 6. Exact spin-flip identity and t2≤5/2 on the SAME pair

For any four-qubit operator X,the one-site spin flip is `S_i=2E_i−Id`. The tensor product of the four complex-LINEAR maps is `X→Y X^T Y`. Expanding the commuting product gives the ACTUAL operator identity

    Y rho^T Y = T0−2T1+4T2−8T3+16T4.                          (S)

Let `tilde rho=Y rho^T Y`. Since rho is a density,so is tilde rho;for any actual rank3 P, `0≤Tr(P tilde rho)≤1`. Trace the single identity (S) with the SAME P and solve for t2:

    4t2=Tr(P tilde rho)−t0+2t1+8t3−16t4
        ≤1+6+6−3=10.

Thus **t2≤5/2**. The negative `−t0` is bounded by0,not by an independently selected optimizer. Purity is needed for the Schmidt t1 estimate;one-uniformity gives t3 exactly. The argument does not show t2≤5/2 for every mixed state with the same local marginals.

## 7. Complete nonnegative gap, mixtures, mirror and endpoints

For a pure one-uniform rho,subtract (E) from the fixed product reference:

    R3(p)−Tr(PΛ_p(rho))
    =(1−p)^4(1−t0)+(1−p)^3p(3−t1)
      +(1−p)^2p²(3−t2)+(1−p)p³(5/4−t3)
      +p^4(3/16−t4).

Every term is nonnegative for0≤p≤1. Using t2≤5/2,t3=3/4 yields

    R3(p)−Tr(PΛ_p(rho))
      ≥ (1/2)p²(1−p)²+(1/2)p³(1−p)
      = (1/2)p²(1−p).                                        (G)

All layers involve the SAME rho,P;the product terms have one fixed reference P*. No minimum/maximum is separately moved through the sum.

For a finite convex combination of pure one-uniform inputs,apply (G) to each summand with the SAME p,P and use trace affinity. Any closed-hull version follows by continuity in finite dimensions;no different P is chosen per component. For p∈[1,4/3],apply the proven mirror (M) to the SAME rho and `P'=Y P^T Y`, then use (G) at p'=2−p. Set `s=min(p,2−p)` to get exactly

    Tr(PΛ_p(rho)) ≤ R3(p)−(1/2)s²(1−s)

throughout 0≤p≤4/3. Since this holds for EVERY actual complex rank3 P,the Ky-Fan variational characterization yields the candidate's top-three spectral bound on precisely this convex hull.

At p=0 the explicit gap is0,at p=1 it is0 and both outputs are I16/16,while at p=4/3 it is2/27>0. Every other physical p except1 has a strictly positive displayed gap. Degenerate eigenspaces cause no ambiguity in the variational statement.

## 8. Independent exact bounded checks — executed, not author output

I wrote `frontier-review-f5-depol-exact-check-v1.py` SHA256 **5de969371efd72585a6ffddf39c26ebb78e6f2252e7d652394eb3c9c730f720e** and ran, once:

    python3 -B frontier-review-f5-depol-exact-check-v1.py \
      --output frontier-review-f5-depol-exact-check-receipt-v1.json

Receipt SHA256 **8b8b5d8f68d0393d928edcfd80fc24effa806d30c1ae797a945c19766edfea6d**;actual tool result `PASS_INDEPENDENT_EXACT_SAMPLES_NOT_UNIVERSAL_PROOF`,wall time3.66s. The checker uses ONLY Python standard-library `fractions.Fraction` pairs as exact complex numbers and imports NO author program.

- Constructed a complex cycle-graph pure state,a complex GHZ pure state,and their `2/5,3/5` convex mixture. Verified both pure matrices Hermitian/idempotent/trace1 and ALL four one-qubit marginals I/2 exactly.
- Constructed one genuinely complex rank3 projector from three phase-twisted Walsh columns and verified P*=P,P²=P,TrP=3 exactly.
- Checked full spin-flip erasure OPERATOR identity on all three states;checked t0/t1/t2/t3/t4 inequalities and (G)/(M) gaps at six rational physical parameters including0,1,7/6,4/3. Observed layer traces respectively `(1/2,1,5/4,3/4,3/16)`, `(3/16,3/4,9/8,3/4,3/16)`, `(5/16,17/20,47/40,3/4,3/16)`.
- Computed the SAME product-reference erasure layers exactly `(1,3,3,5/4,3/16)`.
- Checked the mirror identity on ALL256 computational matrix units separately at p=7/6 and4/3,for **512 exact matrix-unit checks**. Both sides are complex-linear,so these finite tests cover all operators at those TWO sampled p values only. The all-p proposition is the written proof in §2.

A preliminary local environment check reported `ModuleNotFoundError: No module named 'sympy'`;the actual verifier uses only standard-library exact arithmetic and ran successfully. No package was installed. No unobserved check or formal certificate is claimed. Exact samples do not establish the universal inequality.

## 9. Remaining original target and assurance

The candidates establish only Ky-Fan k=3 on the convex hull of pure one-uniform four-qubit inputs,with the stated gap. General mixed inputs outside that hull—including possibly mixed states whose four one-qubit marginals are I/2—remain untreated by this derivation. The all-density `t1≤3,t2≤3` sufficient certificate remains open;failure of one of those layer bounds would not itself be a physical original-channel violation. A genuine violation must give one actual density,physical p and rank3 P exceeding R3;or a full proof must cover all actual pairs. No such violation/global proof is supplied.

Mirror,universal t3 and one-uniform gap proofs are separately reconstructed above,with no use of quarantined parent episode/old source as an accepted premise. This review does not reclassify or erase any historical process finding. No novelty/priority,formal/human/configured-family or global all-index majorization claim is made. Main should read the complete three source candidates and this complete return before any scoped adoption.
