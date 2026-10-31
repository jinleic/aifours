# Werner upper zero — the entire base forcing in closed form: a vertex-potential (Woodbury) identity and an explicit inverse-free sufficient certificate

PhysicsResearch96h-2 / physics-1. **WRITTEN OWNER-CANDIDATE; not parent-read, reviewed, adopted or checked in any kernel.** Actual `/bin/date` immediately before creation: **Mon Oct 26 05:23:33 PDT 2026**.

Chronology (disclosed, not cured): after the separate checkpoint040 (04:49:47) and before Main's later instruction arrived, I resumed primary reading and derived the post-040 leads recorded in ACK041 (`6d40a6b98e1f2e85c98ac972be5fcd485ee461ac813125e458c4971f990dfb17`, 04:58:21, sent before any further primary work). Everything below was derived after ACK041, except the post-040 leads that ACK041 lists, which are labeled as such there. The pre-v111-receipt mass/force derivation (inventory correction `fa4eac2bb889d43f9cc5c6e61d85d217b306d718852e49fe62e5c15ac87f9bf4`) is NOT used here.

All algebra below is WRITTEN in exact symbols and fractions. No scientific interpreter, calculator, Eval, CAS, program, LP, enumeration, solver, replay, CLI, nested agent or GO was used. All own and parent process findings and the HOLD remain.

## 0. Result and its limits

For EVERY positive normalized four-Schmidt spectrum and EVERY complex p test Z with Zc=0 (all twelve complex directions: skew A3, output C3, symmetric T6, with all couplings), the base forcing `F_c(Z)=j_c(Z)^dagger K_c^-1 j_c(Z)` has the exact closed form (Theorem C)

`F_c(Z)=sup over alpha in C^4 of [ sum_edges x_i x_j theta_ij |phi_ij(Z)/2+alpha_i+alpha_j|^2 - sum_i (2x_i/d_i)|alpha_i|^2 ]`,

with `theta_ij=1/(d_ij(1+d_ij))`. Consequently:

- the strong comparison G7 is EQUIVALENT to positivity of one explicit (12+4)-dimensional Hermitian form (Corollary C1), with no six-edge inverse;
- an explicit inverse-free p-side inequality (Corollary C2, for any positive vertex weight vector s with positive ϖ^s, in particular s=1 for EVERY spectrum) is SUFFICIENT for G7, hence for E_full≥0, because `K_full>=K_c`.

**Nothing here proves G7, E_full≥0, Z_up≥0, the other three canonical signs or unrestricted W4.** The equal-spectrum numbers in §6 are written diagnostics of the certificate's sharpness only, not a selected-family result. G13 and the bare dual lift remain FALSE and are not used.

## 1. Imports (named, not re-proved here)

- Generic operator identities G1–G8: `generic-upper-zero-operator-checkpoint-001-v1.md`, SHA256 `249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`. These are (G3) the six-edge kernel K_c, (G4) I<=K_c<=3I, (G5) the forcing j_c, (G6) the joint minimization, and (G8) the ground-state expansion with w_ij=c_i c_j d_ij, m_ij=x_i x_j g_ij, g_ij=d_ij-(d_i-d_j)^2/4 and gamma_(i;jt). Parent wave-v24 support covers G1–G12 at its stated scope; the FALSE-G13 correction `1b0e9a523810b5fb29cfa3c53ad287112d19803dc8110913d1b1f975817e6eb5` is respected.
- `K_full>=K_c` (the exact raw kernel adds a positive remainder): addendum-2 `ef401cddef2d596c1b3bbd53bbfac3f05a48f53c3d43cf3f61c6b242b78cda64` and the v7 full-raw identity `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`. Owner candidates; the implication G7 ⇒ E_full≥0 inherits exactly these imports.

Off-diagonal entry check of gamma: `(K_c)_(ij,it)=-d_i c_j c_t/(2d_ij d_it)` times `w_ij w_it` equals `-d_i x_i x_j x_t/2`. Hence

`gamma_(i;jt)=d_i x_i x_j x_t/2`,                                  (1)

which has PRODUCT form in j,t at each vertex i. Everything below rests on this.

## 2. Notation

All c_i>0 with Σc_i²=1. Set x_i=c_i², d_i=1-x_i, d_ij=(d_i+d_j)/2, r=1/Σ(1/d_k), Q=I-cc^T, M=QZQ. For Z in H={Zc=0} put T_ij=Z_ij/(c_i c_j) for i!=j. Write

- `Tbar_i=Σ_(k!=i) x_k T_ik/d_i` and `Delta_ij=T_ij-Tbar_i`;
- `psi_ij=d_i(1+d_i)T_ij-d_i^2 Tbar_i=d_i Tbar_i+d_i(1+d_i)Delta_ij`;
- `phi_ij=psi_ij+psi_ji`.

Since Zc=0 forces Z_ii=-d_i Tbar_i, (G5) reads `j_ij=c_i c_j phi_ij/(d_i+d_j)`. For a complex edge vector sigma, `(R sigma)_i=Σ_(j!=i) x_j sigma_ij`.

## 3. Lemma A — the base kernel is edge-diagonal minus a vertex-sum term

In the ground-state coordinates F_e=sqrt(2) w_e sigma_e,

`(1/2)F^dagger K_c F = Q_K(sigma)`,
`Q_K(sigma)=Σ_edges x_i x_j d_ij(1+d_ij)|sigma_ij|^2 - Σ_i (d_i x_i/2)|(R sigma)_i|^2`.    (A)

*Proof.* By (G8), `(1/2)F^dagger K_c F=Σ_e m_e|sigma_e|^2+Σ_i Σ_(j<t) gamma_(i;jt)|sigma_ij-sigma_it|^2`. Weights x_j summing to d_i over j!=i give the weighted variance identity

`Σ_(j<t) x_j x_t|a_j-a_t|^2 = d_i Σ_j x_j|a_j|^2 - |Σ_j x_j a_j|^2`.

By (1), the vertex-i Laplacian is `(d_i x_i/2)[d_iΣ_j x_j|sigma_ij|^2-|(R sigma)_i|^2]`. Summing over vertices, each edge receives `x_i x_j(d_i^2+d_j^2)/2`. Finally `g_ij+(d_i^2+d_j^2)/2=d_ij+d_ij^2`, because `(d_i-d_j)^2=2(d_i^2+d_j^2)-4d_ij^2`. ∎

Equal-spectrum check (x=1/4): the right side of (A) is `(36/512)I-(3/512)Adj` on the octahedral edge graph. Its values 3/64, 9/128 and 21/256 on 1_6, E0 and E_{-2} are `(9/256)×(4/3, 2, 7/3)`, which are exactly the K_c eigenvalues times w².

## 4. Lemma B — the joint form

With F as in Lemma A, the joint quadratic of (G6) equals

`Phi(Z,sigma)=P(Z)-Re Σ_edges x_i x_j conj(phi_ij) sigma_ij + Q_K(sigma)`,  `P(Z)=<Z,rho'Z>`.    (B)

*Proof.* `sqrt(2) Re(j^dagger F)=2Re Σ_e conj(j_e) w_e sigma_e`, and `conj(j_e) w_e = x_i x_j conj(phi_e)/2`. ∎

The forcing is VERTEX-LOCAL: `Σ_e x_i x_j conj(phi_e)sigma_e=Σ_i x_i Σ_(j!=i) x_j conj(psi_ij)sigma_ij`, and psi_ij depends only on row i. The constraint `Σ_j x_j Delta_ij=0` splits the vertex-i term exactly into `x_i d_i conj(Tbar_i)(R sigma)_i` (row mean against vertex sum) plus `x_i d_i(1+d_i)Σ_j x_j conj(Delta_ij)(sigma_ij-sigmā_i)` (deviations against deviations).

The p energy is `P=Σ_i d_i x_i Σ_(j<t) x_j x_t|T_ij-T_it|^2 + r<M,M^T>` (generic G9 plus the N term). Its row weight `d_i x_i x_j x_t` is EXACTLY `2 gamma_(i;jt)`. The ONLY non-vertex-local term in (B) is `r<M,M^T>`.

## 5. Theorem C — closed form of the entire base forcing

Let `D_K=diag_e(x_i x_j d_ij(1+d_ij))`, `Lambda=diag(d_i x_i/2)`, and

`W=Lambda^-1-R D_K^-1 R^dagger`, i.e. `W_ii=(1/x_i)(2/d_i-Σ_(k!=i)x_k theta_ik)`, `W_ik=-theta_ik`.

Then W>0 and, for every Z in H,

`F_c(Z)=(1/4)Σ_e x_i x_j theta_e|phi_e|^2+(1/4)h^dagger W^-1 h`,  `h_i=Σ_(j!=i)x_j theta_ij phi_ij`,     (C)

`F_c(Z)=sup_(alpha in C^4)[Σ_e x_i x_j theta_e|phi_e/2+alpha_i+alpha_j|^2-Σ_i(2x_i/d_i)|alpha_i|^2]`.  (C')

*Proof.*

1. By (B) and Lemma A, `F_c=sup_sigma[Re<f,sigma>-sigma^dagger K_sigma sigma]` with `f_e=x_i x_j phi_e` and `K_sigma=D_K-R^dagger Lambda R`. K_sigma>0 because K_c>=I, so the Schur complement W of D_K in `[[D_K,R^dagger],[R,Lambda^-1]]` is positive.
2. Woodbury gives `K_sigma^-1=D_K^-1+D_K^-1 R^dagger W^-1 R D_K^-1`, hence (C), since `(R D_K^-1 f)_i=Σ_j x_j theta_ij phi_ij`.
3. For (C'), write `sigma^dagger R^dagger Lambda R sigma=sup_b[2Re(b^dagger Lambda R sigma)-b^dagger Lambda b]` and exchange the two suprema.
4. The inner supremum in sigma equals `(1/4)Σ_e x_i x_j theta_e|phi_e+d_i b_i+d_j b_j|^2`, since `(2R^dagger Lambda b)_e=x_i x_j(d_i b_i+d_j b_j)` and `D_K,e=x_i x_j/theta_e`.
5. Put alpha_i=d_i b_i/2; then `b^dagger Lambda b=Σ_i(2x_i/d_i)|alpha_i|^2`.
6. The supremum over alpha is finite exactly because W>0. Its alpha-quadratic part is `Σ(2x_i/d_i)|alpha_i|^2-Σ_e x_i x_j theta_e|alpha_i+alpha_j|^2=(Xalpha)^dagger W(Xalpha)`. This holds because `x_i W_ii+Σ_k x_k theta_ik=2/d_i`, so all cross terms cancel exactly. ∎

Equal-spectrum cross-check on K_B (Z=-diag(z)Q, so phi_e=d_i z_i+d_j z_j): (C) gives `F_c=||z||^2/64+(7/512)|Σz|^2`. This is identical to the direct eigen-decomposition, whose relative forces are 1/6 on Σz=0 and 1/2 on constant z.

**Corollary C1 (exact equivalence).** G7 holds at c iff for all Z in H and alpha in C^4

`P(Z)+Σ_i(2x_i/d_i)|alpha_i|^2 >= Σ_e x_i x_j theta_e|phi_e(Z)/2+alpha_i+alpha_j|^2`.     (C1)

**Corollary C2 (explicit inverse-free sufficient certificate).**

1. For any positive s in R^4 and nonnegative symmetric Θ, `diag((Θs)_i/s_i)-Θ` is PSD. Conjugating by diag(s) turns it into a weighted graph Laplacian with weights `s_i s_k theta_ik`.
2. Hence `W>=diag(ϖ^s)` with `ϖ^s_i=W_ii-Σ_k theta_ik s_k/s_i`. If ϖ^s>0, then `W^-1<=diag(1/ϖ^s)`.
3. Then G7, and therefore E_full>=0, follows from the p-side inequality

`P(Z) >= (1/4)Σ_e x_i x_j theta_e|phi_e(Z)|^2 + (1/4)Σ_i |h_i(Z)|^2/ϖ^s_i`  for all Z in H.   (C2)

4. **s=1 is admissible for EVERY positive spectrum.** We have `ϖ^1_i=(1/x_i)[2/d_i-Σ_(k!=i)(x_i+x_k)theta_ik]`. Since `d_ik=1-(x_i+x_k)/2>=1/2`, `theta_ik<=4/3`. Then `Σ_k(x_i+x_k)theta_ik<=(4/3)(3x_i+d_i)=4-(8/3)d_i`. Finally `4-(8/3)d_i<2/d_i`, because `(8/3)d_i^2-4d_i+2` has discriminant `16-64/3<0`. ∎

Both sides of (C2) are explicit. The right side involves no inverse.

## 6. Equal-spectrum sharpness diagnostic (written, not a result)

At x=1/4, `K_c=2I-(1/6)Adj` has eigenvalues 4/3 (1_6), 2 (E0, three-dimensional) and 7/3 (E_{-2}, two-dimensional). There A3, C3, T2^0 (symmetric zero-diagonal, Zc=0) and K_B are mutually rho'-orthogonal, and Z_up is additive over them.

- A3: forcing 0.
- C3: G = 4/3 on E0.
- K_B: G = 1/3 on E0 (Σz=0) and 2/3 on 1_6.
- T2^0: G = 49/24 on E_{-2}.
- Strong Z_up eigenvalues: 1/3, 2/3 and 7/24. Relative margins: 1/6, 1/2 and 1/8.

The tightest direction is T2^0.

Here `W=(16/21)(12I-J)` and `ϖ^1=128/21`. The s=1 bound is exact on constants and on ker R, and inflates W^-1 by 3/2 on 1^⊥. In kernel units this turns K_c into `K'=(14/15)K_c` on E0 and leaves it unchanged on 1_6 and E_{-2}. Certificate (C2) therefore still holds at this spectrum, with relative margins 3/28, 1/2 and 1/8.

## 7. Sector formulas that the certificate exposes

- **Row-variance/q-Laplacian matching.** Completing the deviation square vertex by vertex is exact:
  `d_i^2 x_i Σ_j x_j[|Delta_ij|^2-Re conj(Delta_ij)rho_ij+|rho_ij|^2/2]=d_i^2 x_iΣ_j x_j[|Delta_ij-rho_ij/2|^2+|rho_ij|^2/4]`.
  The full deviation forcing, however, carries `d_i(1+d_i)`. If each ordered pair is bounded by AM-GM against its row energy, then per EDGE on ker R the shortfall against the available q energy is EXACTLY `x_i x_j(1-d_i d_j)/2|sigma_e|^2`. This must come from `r<M,M^T>`, which is nonnegative on the nine-dimensional mixed space S={QZQ symmetric} and negative only on A3.
- **K_B.** `G_K(sigma)=(1/(4r))b^dagger Gamma^-1 b` with `b_i=x_i d_i(R sigma)_i` and `Gamma=Q∘Q=diag(d_i^2-x_i^2)+xx^T`. The K_B forcing sees only vertex sums.
- **T2^0.** `T2^0={Y_e=c_i c_j eta_e: eta in ker R}`, `P=Σ_e x_i x_j(d_i^2+d_j^2+2r)|eta_e|^2`, `phi_e=kappa_e eta_e` with `kappa_e=d_i(1+d_i)+d_j(1+d_j)`. On ker R, `nu_e=theta_e kappa_e=2+(d_i-d_j)^2 theta_e/2`. Theorem C gives EXACTLY

  `P-F_c = Σ_e x_i x_j eps_e|eta_e|^2 - (1/4)h^dagger W^-1 h`,
  `eps_e = 2r - d_ij(x_i+x_j)/2 - (d_i-d_j)^4 theta_e/16`,
  `h_i = (1/2)Σ_j x_j (d_i-d_j)^2 theta_ij eta_ij`.

  The kernel ker R is `{eta_e=t_(a(e))/(x_i x_j): t_1+t_2+t_3=0}`, where a(e) is the perfect matching containing e. T2^0 forcing domination is therefore EXACTLY a 2×2 Hermitian inequality on Σt=0.
  - Equal spectrum: h=0 and eps=3/16, so the relative margin is 1/8.
  - Written leading-order diagnostic as c->e_1 (not a proof). On triangle edges `eps≈5ε^2`; on spoke edges `eps≈-1/3`. On ker R the spoke amplitudes are suppressed, giving `Σ x_i x_j eps|eta|^2≈(14/3)ε^-2 Σ|t_a|^2`, while the W term is `≈(1/6)ε^-2Σ|t_a|^2`, so the leading coefficient is 9/2>0. Edge-by-edge positivity is FALSE there (spoke eps<0); amplitude suppression is essential.

## 8. Exact remaining gap

NOT proved:

- (C1) or (C2) for all spectra, hence neither G7, E_full>=0, Z_up>=0 nor P11.
- Domination on the 2×2 T2^0 sector beyond the two diagnostic points.
- The A3/S coupling (the mixed9 Schur residual).
- The other three canonical signs and unrestricted W4.

No negative spectrum or physical witness is supplied. The full kernel K_full also admits a Woodbury structure, since every weighted triangle Laplacian has a product form with radical vertex weights, but this is not developed here and is not needed for sufficiency.

**Next written step:** prove (C2) on the whole nine-dimensional S, where `r<M,M^T>=r||M||^2>=0`, and then control the A3 coupling. Alternatively, prove the explicit 2×2 T2^0 inequality uniformly, using matching coordinates and the ϖ bound.

## 9. Assurance

Same-harness owner-written exact algebra only; not reviewed, formal, kernel, executable, configured-family, cross-vendor, human or novelty accepted. Original cutoff 2026-10-27T11:05:38-07:00 and deadline 12:35:38 unchanged; no park or round closeout.
