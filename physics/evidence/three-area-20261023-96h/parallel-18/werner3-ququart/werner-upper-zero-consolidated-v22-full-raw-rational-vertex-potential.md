# Werner upper zero — rational four-vertex factorization of the ENTIRE raw kernel and an explicit positive Schur supersolution

Owner PhysicsResearch96h-2 / physics-1. Precreation `/bin/date`: **Mon Oct 26 06:45:59 PDT 2026**.

**WRITTEN OWNER-CANDIDATE; not reviewed, adopted, formal or machine-checked.** Written after the v36 whole-state qualified ACK cp050 (`f3e338e0574616bb1af4e472d46db1d97c90bb56aecd737ba9507a775bb3b172`) was written and SENT. Mandatory provenance remains v24/v29/v33/v36, cp047 B1–B3, all earlier process findings, and the HOLD. No zero-credit trial, limit evaluation, region guidance or held lead H1/H2 is used.

Method: symbolic identities and inequalities for ALL positive spectra and ALL indicated complex variables. No selected parameter instance, boundary or limit evaluation, region, threshold, interpreter, calculator, CAS, program, solver, enumeration, replay, CLI, nested agent or new GO.

## 1. Result and exact limits

The complete six-edge raw q kernel, not merely K_c, admits an edge-diagonal minus four-vertex-square factorization with coefficients rational in the spectrum variables x. Consequently its complete forcing on all twelve complex p directions has an exact four-dimensional vertex-potential formula (Theorems 1–2).

The factorization has an explicit positive Schur supersolution. It yields an inverse-free forcing upper bound valid for every spectrum, with no choice or search for a positive vertex vector (Theorem 3).

This replaces the tentative radical-factor observation in v18 §8 by displayed rational formulas for the actual K_full. It is a representation and an upper bound, NOT the missing sign proof. Neither the exact forcing nor its upper bound is shown dominated by P. Lemma N_full, E_full>=0, Z_up>=0, P11, the other three signs and unrestricted W4 remain NOT proved.

## 2. Named inputs and variables

All indices are distinct when required; each unordered edge occurs once.

- x_i=c_i^2>0, Sum_i x_i=1, d_i=1-x_i, d_ij=(d_i+d_j)/2, E3=e3(d), r=(Sum_i 1/d_i)^(-1).
- On H={Zc=0}, T_ij=Z_ij/(c_i c_j), Tbar_i=Sum_(j!=i) x_j T_ij/d_i, Z_ii=-d_i Tbar_i. Every T in C^12 corresponds to exactly one Z in H.
- P(Z)=<Z,rho'Z>, psi_ij=d_i(1+d_i)T_ij-d_i^2 Tbar_i, phi_ij=psi_ij+psi_ji, f_ij=x_i x_j phi_ij.
- w_ij=c_i c_j d_ij, F_ij=sqrt(2)w_ij sigma_ij. This is a bijective coordinate change on C^6.

Imports, with no inherited acceptance of the present packet:

1. v20 (`b5c3d36c1b8594388b28c74a12e46de5adf4feb3d85a6d81d96d494a5a2c86ea`) derives from the v1 definitions that
   `J_full(Z,sigma)=P(Z)-Re(f^dagger sigma)+sigma^dagger K_F sigma`,
   where `K_F=diag(w) K_full diag(w)` and
   `E_full(Z)=P(Z)-(1/4)f^dagger K_F^-1 f`.
2. v7 (`31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`), GFR1–GFR3, gives the exact ground-state expansion
   `sigma^dagger K_F sigma=Sum_e mF_e|sigma_e|^2+Sum_i Sum_(j<k; j,k!=i) gammaF_(i;jk)|sigma_ij-sigma_ik|^2`,
   with
   `gammaF_(i;jk)=x_i x_j x_k d_ij d_ik/(2d_jk)` and
   `mF_ij=x_i x_j[d_ij^2(3-2d_ij d_kl/E3)-(d_ij/2)Sum_(t!=i,j)x_t(d_it/d_jt+d_jt/d_it)]`.
3. Theorem 3 alone uses v7 GFR8: `mF_ij>=x_i x_j[d_ij-(d_i-d_j)^2/4]>0`. This is a named owner-written all-variable theorem, not re-proved or independently reviewed here.
4. K_full>=K_c>=I is the named positive-kernel import from the generic checkpoint, addendum-2 and v7, at their existing scope. Thus K_F is positive definite. This, not any arbitrary entrywise inverse-order assertion, is used below.

## 3. Theorem 1 — rational vertex factorization

For each vertex i, let its three neighbors be j,k,l. Define

`Pi_i=d_jk d_jl d_kl`,
`a_(i;j)=x_j d_ij/(d_jk d_jl)`,
`lambda_i=x_i Pi_i/2`,
`A_i=Sum_(j!=i) a_(i;j)`.

The expression for a_(i;j) uses the other two neighbors k,l; it is unchanged when k,l are exchanged. Every a_(i;j), lambda_i and A_i is positive and rational in x.

Let R_F be the 4-by-6 matrix with `(R_F sigma)_i=Sum_(j!=i) a_(i;j) sigma_ij`, and let Lambda_F=diag(lambda_i). For e={i,j}, set

`beta_e=mF_e+lambda_i A_i a_(i;j)+lambda_j A_j a_(j;i)`,
`D_F=diag(beta_e)`.

Then

`K_F=D_F-R_F^dagger Lambda_F R_F`.                                              (F1)

Moreover beta_e>0 for every edge, independently of whether the imported mass bound is used.

*Proof.* For distinct neighbors j,k of i with remaining neighbor l,

`lambda_i a_(i;j)a_(i;k) = (x_i d_jk d_jl d_kl/2) [x_j d_ij/(d_jk d_jl)] [x_k d_ik/(d_jk d_kl)] = gammaF_(i;jk)`.

For arbitrary complex values u_j, the weighted-variance identity gives

`Sum_(j<k) a_(i;j)a_(i;k)|u_j-u_k|^2 = A_i Sum_j a_(i;j)|u_j|^2-|Sum_j a_(i;j)u_j|^2`.

Apply this to each vertex in the imported full ground-state expansion. The diagonal coefficient accumulated at e={i,j} is precisely beta_e, while the negative square is `lambda_i |(R_F sigma)_i|^2`. This proves (F1).

Alternatively, reading the diagonal of (F1),

`beta_e=w_e^2(K_full)_ee+lambda_i a_(i;j)^2+lambda_j a_(j;i)^2>0`,

because K_full is positive definite. This also proves positivity without the mass comparison. ∎

## 4. Theorem 2 — exact forcing and vertex-potential criterion for the ORIGINAL sign

Define the real symmetric 4-by-4 matrix

`Omega_F=Lambda_F^-1-R_F D_F^-1 R_F^dagger`,

and `h_F=R_F D_F^-1 f`. Its entries are explicit rational functions:

`(Omega_F)_ii=1/lambda_i-Sum_(j!=i) a_(i;j)^2/beta_ij`,
`(Omega_F)_ij=-a_(i;j)a_(j;i)/beta_ij` for i!=j,
`(h_F)_i=Sum_(j!=i) a_(i;j) f_ij/beta_ij`.

Then Omega_F is positive definite, and the full forcing is exactly

`F_full(Z):=j(Z)^dagger K_full^-1 j(Z) = (1/4)Sum_e |f_e|^2/beta_e + (1/4)h_F^dagger Omega_F^-1 h_F`.       (F2)

Equivalently,

`F_full(Z)=sup_(b in C^4) [Sum_e |f_e/2+a_(i;j)b_i+a_(j;i)b_j|^2/beta_e-Sum_i |b_i|^2/lambda_i]`.          (F3)

Thus E_full>=0 on all of H at a spectrum iff, for every T in C^12 and every b in C^4,

`P(Z)+Sum_i |b_i|^2/lambda_i >= Sum_e |f_e/2+a_(i;j)b_i+a_(j;i)b_j|^2/beta_e`.                             (F4)

*Proof.*

1. The block matrix `[[D_F,R_F^dagger],[R_F,Lambda_F^-1]]` has Schur complement K_F at its lower diagonal block. Since Lambda_F and K_F are positive definite, the block matrix is positive definite. Its other Schur complement is Omega_F, so Omega_F>0.
2. Woodbury gives `K_F^-1=D_F^-1+D_F^-1R_F^dagger Omega_F^-1R_F D_F^-1`. Substituting in the full-forcing formula of §2 proves (F2), including its factor 1/4.
3. For (F3), use `sigma^dagger R_F^dagger Lambda_F R_F sigma = sup_b [2Re(b^dagger R_F sigma)-b^dagger Lambda_F^-1 b]` in `F_full=sup_sigma[Re(f^dagger sigma)-sigma^dagger K_F sigma]`. Both suprema range over full complex vector spaces and may be exchanged. Completing the diagonal sigma square gives (F3).
4. Taking P>=F_full for every Z proves (F4). No component of the raw q kernel or any of the twelve p directions is removed. ∎

## 5. Theorem 3 — explicit positive supersolution and inverse-free full-forcing bound

Use the positive full masses from input 3. Define, without a solve or choice,

`s_i=lambda_i A_i`,
`eta_i=Sum_(j!=i) a_(i;j)mF_ij/beta_ij`,
`omega_i=eta_i/s_i>0`.

Then

`Omega_F s=eta`,
`Omega_F>=diag(omega_i)>0`,

and therefore, for every Z in H,

`F_full(Z) <= (1/4)Sum_e |f_e|^2/beta_e + (1/4)Sum_i |(h_F)_i|^2/omega_i`.                 (F5)

All coefficients in this bound are explicit rational functions of x; its tests T are arbitrary complex variables. No numerical spectrum or optimized vertex parameter is involved.

*Proof.* At edge e={i,j},

`(R_F^dagger s)_e=lambda_i A_i a_(i;j)+lambda_j A_j a_(j;i)=beta_e-mF_e`.

Hence

`Omega_F s=Lambda_F^-1s-R_F D_F^-1 R_F^dagger s=A-R_F(1-mF/beta)=R_F(mF/beta)=eta`.

For i!=j put `theta_ij=a_(i;j)a_(j;i)/beta_ij>0`. Since omega_i=(Omega_F s)_i/s_i, the diagonal of `Omega_F-diag(omega)` is `Sum_j theta_ij s_j/s_i`, and its off-diagonal is -theta_ij. Its Hermitian quadratic form is exactly

`Sum_(i<j) theta_ij |sqrt(s_j/s_i)y_i-sqrt(s_i/s_j)y_j|^2>=0`.

This proves the matrix lower bound. Inverse order for positive definite matrices yields `Omega_F^-1<=diag(1/omega_i)`, and (F2) gives (F5). ∎

## 6. Exact remaining lemma and distinction between equivalence and sufficiency

- **Exact universal obligation:** prove (F4) for every positive spectrum and every (T,b), equivalently prove Lemma N_full from v20 for every (T,sigma). Neither has been proved.
- **Explicit sufficient obligation:** show that P dominates the right side of (F5) for every positive spectrum and every T. This would prove the original full sign, but is stronger than the exact obligation. No implication in the reverse direction is asserted.
- The other three canonical signs and unrestricted rank<=2 W4 remain open in this work.

The four-vertex formula retains the complete full-raw correction. It does not assume that a stronger K_c certificate must hold, infer a physical witness from a route direction, or claim a positivity result merely from a change of representation.

## 7. Assurance

All new equalities and the supersolution argument are written symbolic algebra. The positive-mass input is explicitly named, not independently cleared. No kernel/formal proof, review, configured-family gate, external-family review, executable validation or novelty clearance is claimed. Original cutoff 2026-10-27T11:05:38-07:00 and delivery deadline 12:35:38 remain. No park or closeout.
