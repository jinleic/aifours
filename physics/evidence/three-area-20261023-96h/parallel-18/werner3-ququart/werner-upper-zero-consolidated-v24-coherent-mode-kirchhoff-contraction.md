# Werner upper zero — exact coherent forcing mode and a universal Kirchhoff contraction of the full-raw inverse-free bound

Owner PhysicsResearch96h-2 / physics-1. Actual `/bin/date` before creation: **Mon Oct 26 10:20:40 PDT 2026**.
**WRITTEN OWNER-CANDIDATE, not reviewed/adopted/formal/kernel-checked/novelty-cleared.** This is a full-raw forcing inequality for ALL positive normalized spectra and ALL complex Z with Zc=0, at the named owner-written input cut below. It is NOT a proof that P dominates that forcing.

## 1. Prospective authority and exact provenance cut

Actual v133-B RETURN preceded NEW whole064 ACK, SHA256 `be928f8a946ae7922a1b02edf6f5ecf83c1b00aacb3ed803305dbe950a2181b6`, which was WRITTEN and SENT before any new primary source/proof. Main actually read that whole ACK and explicitly released ORIGINAL universal primary work in `PH-post-v61-exactness-and-qualified-Shor-Werner-directions-v65.json`; its COMPLETE body was read before the present source/proof continuation. No extra ACK or silence is used as permission.
All v24/v29/v33/v36/v38/v46/v53/v56/v59 and earlier process/source-probe histories remain mandatory, including cp047 B1–B3 and the exact held-lead statuses. Entire withdrawn probes/proposed bounds/consuming guidance retain ZERO credit, not repair by symbolic rewriting. The current derivation below starts from the displayed all-variable full-raw factorization/supersolution identities in v22 and ordinary weighted-Laplacian algebra. It does not use a selected spectrum, boundary, limit, chosen parameter/control, viability comparison, old joint-skew/row-constant proposed bound or any withdrawn conclusion. This is an explicit mathematical dependency statement, not a global counterfactual provenance/cognition certificate.
Actual current source reads: COMPLETE130LF v20 and COMPLETE152LF v22, including endings, after COMPLETE v65. Cross-domain reviews are not Werner proofs and supply no correctness/import clearance here.

## 2. Inputs and the new quantitative statement

Use v22 `werner-upper-zero-consolidated-v22-full-raw-rational-vertex-potential.md`, SHA256 `0749cf9a517eee2ae732a9143dd4d078be690d29276f8c4aebf5e4df4b9b2964`, with its named inputs. For every positive normalized spectrum x_i=c_i^2, all quantities below are its explicit rational functions, without any evaluated instance:

- f=f(Z) in C^6, `f_ij=x_i x_j phi_ij`, retains the ENTIRE source forcing on H={Zc=0}, with all twelve complex off-diagonal directions.
- `K_F=D_F-R_F^* Lambda_F R_F`, `D_F=diag(beta_e)>0`, and the complete forcing is
  `F_full(Z)=j(Z)^* K_full^-1 j(Z)=(1/4)sum_e |f_e|^2/beta_e+(1/4)h^* Omega^-1 h`,
  where `Omega=Lambda_F^-1-R_F D_F^-1 R_F^* >0`, `h=R_F D_F^-1 f`.
- In v22's notation `s_i=lambda_i A_i>0`, `eta_i=sum_(j!=i) a_(i;j) mF_ij/beta_ij>0`, `omega_i=eta_i/s_i>0`, and `Omega s=eta`.
- The off-diagonal entries are `Omega_ij=-theta_ij`, with `theta_ij=a_(i;j)a_(j;i)/beta_ij>0` for ALL distinct i,j.

The Werner application inherits v22's explicit named owner-written v7 GFR8 positive-mass input `mF_e>0` and its positive-kernel/factorization inputs; they are NOT independently cleared here. The following linear-algebra theorem is proved under the displayed positivity/identity hypotheses. Thus the present application is WRITTEN at that NAMED input cut, not a new import-free or accepted Werner theorem.
Define, with no solve, choice or parameter search,

`u_i=s_i eta_i>0`, `U=sum_i u_i>0`,
`ell_ij=theta_ij s_i s_j>0`,
`kappa=min_(i<j) [U ell_ij/(u_i u_j)]>0`,
`y_i=s_i h_i`, `xi=sum_i y_i`,
`V(h)=sum_i |h_i|^2/omega_i-|xi|^2/U`.

**Theorem 1 (full-raw coherent/variance bounds).** For EVERY such spectrum and EVERY Z in H,

`D(f)+|xi|^2/(4U) <= F_full(Z)`
`<= D(f)+|xi|^2/(4U)+V(h)/[4(1+kappa)]`,  (K1)

where `D(f)=(1/4)sum_e |f_e|^2/beta_e`. Furthermore

`V(h)=sum_i u_i |h_i/eta_i-xi/U|^2 >=0`.  (K2)

Consequently the upper bound in (K1) is no larger than v22(F5), and is STRICTLY smaller whenever h is not a complex scalar multiple of eta. The coherent case h=a eta is EXACT: both sides of (K1) equal the actual full forcing, not merely a sufficient comparison.
This is an all-variable quantitative improvement of v22(F5), not an evaluated comparison of its usefulness at any spectrum. The scalar kappa is the minimum of the six symbolic edge ratios of the complete actual four-vertex graph, not a chosen numeric parameter or region threshold.

## 3. Full proof of Theorem 1

Let S_s=diag(s_i), M=diag(u_i), and let L be the weighted graph Laplacian with off-diagonal `L_ij=-ell_ij` and diagonal `L_ii=sum_(j!=i) ell_ij`. The source identity Omega s=eta gives, entry by entry,

`S_s Omega S_s=M+L`.  (K3)

Indeed its off-diagonal entries are -theta_ij s_i s_j=-ell_ij, and multiplication by the all-one vector gives S_s eta=u, determining the diagonal entries. Thus

`h^* Omega^-1 h=y^*(M+L)^-1 y`.  (K4)

The complete graph is connected because every ell_ij is positive. For arbitrary complex z, by the definition of kappa,

`z^*Lz=sum_(i<j) ell_ij |z_i-z_j|^2`
`>= (kappa/U)sum_(i<j) u_i u_j |z_i-z_j|^2`
`=kappa[sum_i u_i|z_i|^2-|sum_i u_i z_i|^2/U]`.  (K5)

The last equality is the full complex weighted-variance identity, with exactly the SAME u_i in every term. Put `v=M^(1/2)1/sqrt(U)`, so v^*v=1. Then (K5) is

`M^(-1/2) L M^(-1/2) >= kappa(I-vv^*)`.

Since L1=0, v is an EXACT null vector of this Hermitian normalized Laplacian. Its orthogonal complement is invariant, and the preceding inequality bounds the operator there below by kappa. Therefore

`[I+M^(-1/2)LM^(-1/2)]^-1`
`<= vv^*+(1/(1+kappa))(I-vv^*)`.  (K6)

This also follows directly by inverse order from `(1+kappa)I-kappa vv^*>0` and its explicit rank-one inverse. No entrywise inverse-order claim or numerical spectral estimate is used.
Applying (K6) to M^(-1/2)y gives

`y^*(M+L)^-1 y`
`<= |sum_i y_i|^2/U+(1/(1+kappa))[sum_i |y_i|^2/u_i-|sum_i y_i|^2/U]`.  (K7)

Here `|y_i|^2/u_i=|h_i|^2/omega_i` and sum_i y_i=xi. Completing the weighted scalar square gives precisely (K2), hence the upper side of (K1).
For completeness, let `y_perp=y-(xi/U)u`; then sum_i(y_perp)_i=0. Since `(M+L)1=u`, one has `(M+L)^-1u=1`, and the cross terms vanish EXACTLY. Therefore

`y^*(M+L)^-1y=|xi|^2/U+y_perp^*(M+L)^-1y_perp`.  (K8)

The residual is nonnegative because M+L>0, proving the lower side of (K1). It also satisfies `0<=y_perp^*(M+L)^-1y_perp<=V(h)/(1+kappa)` by (K7).
Equation (K2) says V(h)=0 iff every h_i/eta_i equals the same complex scalar. In that coherent case y_perp=0, so (K8) gives the exact asserted forcing. Otherwise V(h)>0 and kappa>0, so the new upper bound improves v22(F5) by the STRICT positive amount

`[kappa/(4(1+kappa))] V(h)`.  (K9)

This proves Theorem 1 for all indicated variables. No source mode or mixed term has been removed. ∎

## 4. The coherent scalar and its normalization are explicit edge expressions

The v22 definition of beta_e gives `(R_F^*s)_e=beta_e-mF_e`. Hence

`xi=s^*h=s^* R_F D_F^-1 f`
`=sum_e (1-mF_e/beta_e) f_e`.  (K10)

Likewise, using eta=R_F(mF/beta),

`U=s^*eta=sum_e [(beta_e-mF_e)mF_e/beta_e]`.  (K11)

These are rational coefficient expressions in the spectrum. No new positive vector is chosen, no vertex solve is performed and no full-raw term is discarded. In particular (K10) is an actual linear combination of the COMPLETE f(Z), not a separately chosen projected source direction.

## 5. Exact ORIGINAL residual and a strictly improved sufficient obligation

Combining (K8) with the full forcing identity gives the exact decomposition

`E_full(Z)=P(Z)-D(f)-|xi|^2/(4U)`
`          -(1/4)y_perp^*(M+L)^-1y_perp`.  (K12)

The potential residual is supported on the THREE-dimensional sum-zero forcing space `sum_i(y_perp)_i=0`; all source Z still range over the entire twelve-dimensional H. Its quadratic form is retained, not assumed nonnegative with a favorable sign or omitted. This separates ONE exactly solvable coherent potential mode from the full mixed three-potential residual without a symmetry assumption on the source.
Thus the original full sign is EQUIVALENT to domination of the ENTIRE right side of the forcing identity in (K12) by P for all positive spectra and all Z. A necessary condition is

`P(Z)>=D(f)+|xi|^2/(4U)` for ALL Z,  (NEC)

and an explicit sufficient condition is

`P(Z)>=D(f)+|xi|^2/(4U)+V(h)/[4(1+kappa)]` for ALL Z.  (SUFF)

SUFF is strictly weaker than demanding v22(F5)'s full inverse-free upper bound whenever V(h)>0, because it subtracts the proved positive gain (K9). It remains only a SUFFICIENT obligation, not an equivalence. Neither NEC nor SUFF has been proved here on the full source space; even the exact coherent-force sector requires its remaining P comparison. No selected-state success/failure is inferred.
The universal lower bound directly obtained for the original energy is

`E_full(Z)>=P(Z)-D(f)-|xi|^2/(4U)-V(h)/[4(1+kappa)]`.  (K13)

This keeps the ENTIRE raw kernel and every mixed source term through P and f(Z). The actual unpaid comparison in (K12), equivalently v20 N_full/v22F4, remains the full-target prerequisite. The honest genuine A/C obstruction recorded in cp057/v53 is not paid by this graph bound or by separate positive compressions. The other three full canonical signs and unrestricted rank<=2 W4 remain unproved.

## 6. Scope, inputs and assurance

New result: the exact coherent-mode separation (K8)/(K10)/(K11), the universal quantitative variance contraction (K1)/(K9) improving v22(F5), and the full mixed original energy bound (K13), all with complete conventional all-variable proofs and explicit source-input cut. This is not a new full sign, parameter regime, spectral instance, witness, kernel/formal proof, independent-family/human acceptance, novelty result or numerical progress claim.
The generic linear-algebra proof only assumes the displayed positive s,eta,theta and Omega s=eta, with positive Omega; its Werner application inherits the named unreviewed source factorization/positive-mass inputs from v22/v7/v20. No earlier selected probe or withdrawn bound is a premise. None of those source pins or chronology facts certifies a global unaffected provenance history.
No identity was machine-checked. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/CLI/nested agent/new GO, numeric/state/control/boundary/limit/magnitude/decimal viability probe, or frozen/shared edit. All original ownership/18/HOLD/N4 UNKNOWN/historical exit unestablished/auxiliary214 STOP/process findings/ZERO histories remain, including v46's FULL34m27s. Cutoff2026-10-27T11:05:38-07:00, delivery12:35:38, actual<=30min substantive checkpoints and no early final park remain unchanged.
