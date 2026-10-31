# Werner upper zero — complete raw-entry admission proof for the v24 universal Kirchhoff bound

Owner PhysicsResearch96h-2 / physics-1. Actual `/bin/date` before creation: **Mon Oct 26 10:31:12 PDT 2026**.
**WRITTEN OWNER-CANDIDATE, UNREVIEWED/UNADOPTED.** Additive companion to ENTIRE127LF v24, SHA256 `6e39e1e30e8c7ffdbf032c84ed940f3086f73370aa459afa8cbf5246c446a0fc`. It reconstructs the complete source-specific positivity/factorization/forcing admission needed to apply that theorem. The v24 file remains unchanged at its original stated input cut; this LATER joint proof does not backdate its review, source coverage or acceptance.
Prospective authority is Main v65 after ACTUAL v133 RETURN and NEW whole064 ACK WRITTEN/SENT/Main complete read. All older process/source-probe/held-lead findings and ZERO guidance remain, without source laundering or a provenance-cure assertion. Only all-variable original raw-entry algebra is used.

## 1. Exact result and source provenance, not an extra discovery count

For ALL positive c_i with sum_i c_i^2=1 and ALL complex Z with Zc=0, the ACTUAL raw six-edge kernel and forcing satisfy EVERY positive-matrix hypothesis of v24 Theorem1. Consequently the full raw forcing obeys v24(K1)–(K11) and the original energy obeys v24(K12)–(K13), without leaving an unsupplied specialized positive-mass/factorization input in THIS NEW joint manuscript.
The actual original sign E_full>=0, its p-side domination, the other three full canonical signs and unrestricted W4 are STILL NOT PROVED. This is a complete application proof for a forcing bound, not a new sign certificate or another claimed discovery of old mass positivity.
Actual sources used here: COMPLETE original v1_354LF; COMPLETE original source017_205LF; COMPLETE v20_130LF; COMPLETE v22_152LF; now COMPLETE v7_211LF in raw1–170/171–211, including endings. v7 is `werner-upper-zero-consolidated-v7-full-raw-ground-state.md`, SHA256 `31f993aa031d4affc156f08bfe58ec289eb10d287f2351da0be4938eccb49d08`.
Sections2–3 below reconstruct the OLD v7 positive-mass argument from its actual formulas, and §§4–5 reconstruct the OLD v22 factorization/Schur/supersolution. They are not new independent result counts. v7's compatible-square residual, its boundary-region discussion, false G13/bare-lift history or any historical numerical probe is NOT a premise of this proof. The new quantitative result remains the complete v24 coherent/variance contraction, now with its entire operator-leaf application written out.

## 2. Literal raw operators and the exact ground-state row sum

Let `x_i=c_i^2`, `d_i=1-x_i`, `d_ij=(d_i+d_j)/2`, `W=e3(d)>0`. For unordered edges e=ij, let `w_ij=c_i c_j d_ij>0`. The ACTUAL full raw kernel is DEFINED by

`(K_full)_(ij,ij)=3-2d_ij d_kl/W`,
`(K_full)_(ij,it)=-c_j c_t/(2d_jt)`,

and zero on disjoint edges, where k,l complement i,j. Set `K_F=diag(w)K_full diag(w)`. Its shared-edge off-diagonal entries are

`(K_F)_(ij,it)=-gammaF_(i;jt)`,
`gammaF_(i;jt)=x_i x_j x_t d_ij d_it/(2d_jt)>0`.

Let mF_ij be the ROW SUM of K_F at edge ij. Direct substitution, retaining every adjacent edge, gives

`mF_ij=x_i x_j gF_ij`,
`gF_ij=d_ij^2(3-2d_ij d_kl/W)`
`        -(d_ij/2)sum_(t!=i,j) x_t(d_it/d_jt+d_jt/d_it)`.  (A1)

For every complex sigma on all SIX edges, collecting each shared pair once gives the EXACT expansion

`sigma^*K_F sigma=sum_e mF_e|sigma_e|^2`
` +sum_i sum_(j<t;j,t!=i) gammaF_(i;jt)|sigma_ij-sigma_it|^2`.  (A2)

No positivity of the masses or raw kernel is assumed in deriving (A1)–(A2). In particular positivity of a matrix alone would not prove positive row sums.
For an auxiliary algebraic comparison define K_c by the explicit entries

`(K_c)_(ij,ij)=1+d_i d_j/d_ij^2`,
`(K_c)_(ij,it)=-d_i c_j c_t/(2d_ij d_it)`.

Its weighted row sum divided by x_i x_j is

`d_ij^2+d_i d_j-d_ij(1-x_i-x_j)`
`=d_ij-(d_i-d_j)^2/4=:g_ij`,  (A3)

because 1-x_i-x_j=2d_ij-1. This uses only these displayed entries, not a separate theorem that K_c is positive or that K_full>=K_c.

## 3. Complete all-variable positive-mass proof, paying signed shared rows

Fix an ARBITRARY edge ij and put `Delta=d_i-d_j`, `S=d_i+d_j`; k,l are its complementary indices. The weighted matrix `A=diag(w)(K_full-K_c)diag(w)` has shared entry

`A_(ij,it)=-x_i x_j x_t(d_i-d_j)(d_i-d_t)/(8d_jt)`.

Indeed the coefficient difference is `(x_i x_j x_t/2)[d_i-d_ij d_it/d_jt]`, and the bracket is `-(d_i-d_j)(d_i-d_t)/(4d_jt)`. Its diagonal divided by x_i x_j is

`2d_ij^2(1/2-d_ij d_kl/W)+Delta^2/4`.

Summing BOTH shared entries through every outside t, the cancellation

`(d_i-d_t)/d_jt-(d_j-d_t)/d_it`
`=2(d_i-d_j)(d_i+d_j)/[(d_i+d_t)(d_j+d_t)]`

therefore gives the exact row identity

`gF_ij-g_ij=S^2[2W-S(3-S)]/(8W)`
` +(Delta^2/4)[1-S sum_(t!=i,j) x_t/((d_i+d_t)(d_j+d_t))]`.  (A4)

Here d_kl=(3-S)/2 because sum_i d_i=3. The second bracket is NOT asserted nonnegative; its possible negative contribution is paid explicitly next.
Write `T=x_i+x_j=2-S`, `h=x_i x_j`, `v=x_k x_l`. These are ALL-variable abbreviations, not selected parameters or a source restriction: positivity and normalization give0<T<1 for every edge. The outside sum is1-T, while `d_i d_j=1-T+h>=1-T`. Hence

`S sum_outside x_t/[(d_i+d_t)(d_j+d_t)]<=S`,

so that bracket is at least `1-S=-(1-T)`. Also Delta^2=(x_i-x_j)^2<=T^2.
The elementary symmetric identity W=1+2e2(x)-e3(x) gives

`W=1+2T(1-T)+(1+T)h+(2-T)v`,
`2W-S(3-S)=3T(1-T)+2(1+T)h+2(2-T)v`.  (A5)

For clarity, e2(x)=h+v+T(1-T) and e3(x)=h(1-T)+vT, which prove the first identity directly; the second follows by S=2-T. Elementary AM–GM gives h<=T^2/4 and v<=(1-T)^2/4, yielding

`W<=3/2+3T(1-T)/4`.

Therefore the exact factorization

`3S^2-2WT>=3(2-T)^2-2T[3/2+3T(1-T)/4]`
`=(3/2)(1-T)(T+4)(2-T)>0`  (A6)

holds on the ENTIRE positive source domain. Combining these bounds with the SIGNED row identity(A4),

`gF_ij-g_ij>=3S^2 T(1-T)/(8W)-T^2(1-T)/4`
`=T(1-T)[3S^2-2WT]/(8W)`
`>=3T(1-T)^2(T+4)(2-T)/(16W)>0`.  (A7)

Finally set u=d_ij. Then1/2<u<1 and |d_i-d_j|<=x_i+x_j=2(1-u). From(A3),

`g_ij>=u-(1-u)^2>=1/4`,

where the last difference is exactly `(u-1/2)(5/2-u)>=0`. It follows that

`mF_ij>x_i x_j g_ij>=x_i x_j/4>0`  (A8)

for EVERY edge and EVERY positive normalized spectrum. This is a complete symbolic proof from the literal raw entries. No sampled instance, boundary/limit evaluation, numerical magnitude, entrywise inverse order, dropped commutator row or generic PSD-to-row-sum inference was used.
Equation(A2) with(A8) proves K_F>0 immediately; because w_e>0, it also proves K_full>0. Thus positivity of the actual raw kernel is reconstructed here rather than imported from K_full>=K_c.

## 4. Complete rational four-vertex factorization and positive Schur matrix

For each vertex i with neighbors j,k,l, define

`Pi_i=d_jk d_jl d_kl`,
`a_(i;j)=x_j d_ij/(d_jk d_jl)`,
`lambda_i=x_i Pi_i/2`, `A_i=sum_(j!=i) a_(i;j)`.

All these quantities are positive rational functions of the ENTIRE source spectrum. Define the4-by6 matrix R by `(R sigma)_i=sum_(j!=i) a_(i;j)sigma_ij`, Lambda=diag(lambda_i), and

`beta_ij=mF_ij+lambda_i A_i a_(i;j)+lambda_j A_j a_(j;i)>0`, `D=diag(beta_e)`.

For distinct j,k neighbors of i, direct cancellation gives

`lambda_i a_(i;j)a_(i;k)=x_i x_j x_k d_ij d_ik/(2d_jk)=gammaF_(i;jk)`.

Using the full complex weighted-variance identity at each vertex,

`sum_(j<k) a_(i;j)a_(i;k)|sigma_ij-sigma_ik|^2`
`=A_i sum_j a_(i;j)|sigma_ij|^2-|sum_j a_(i;j)sigma_ij|^2`,

equation(A2) becomes exactly

`K_F=D-R^*Lambda R`.  (A9)

This retains every raw shared edge and diagonal term. Consider the Hermitian block matrix with diagonal blocks D,Lambda^-1 and off-diagonal blocks R^*,R. Its Schur complement at Lambda^-1 is K_F>0. Since Lambda^-1>0, the whole block is positive definite; its other Schur complement is

`Omega=Lambda^-1-R D^-1R^*>0`.  (A10)

The off-diagonal entry at vertices i,j is `-a_(i;j)a_(j;i)/beta_ij=-theta_ij<0`, because their unique common edge is ij. All SIX vertex conductances are present; no zero/constant source mode is artificially removed.
Put `s_i=lambda_i A_i>0`. Entrywise in edge space,

`(R^*s)_e=beta_e-mF_e`.

Consequently, with `eta=R(mF/beta)`,

`Omega s=Lambda^-1s-RD^-1R^*s`
`=A-R(1-mF/beta)=R(mF/beta)=eta>0`.  (A11)

Here R1=A and every summand in eta is positive by(A8). Thus omega_i=eta_i/s_i>0. This supplies ALL positive s,eta,theta/Omegas=eta hypotheses of v24, without a vertex-vector search or a separate unproved supersolution assertion.

## 5. Complete forcing normalization and application to ALL original p tests

For ALL complex Zc=0, set T_ij=Z_ij/(c_i c_j) for i!=j and `Tbar_i=sum_(j!=i)x_jT_ij/d_i`, so Z_ii=-d_i Tbar_i. Define

`psi_ij=d_i(1+d_i)T_ij-d_i^2 Tbar_i`,
`phi_ij=psi_ij+psi_ji`, `f_ij=x_i x_j phi_ij`.

The literal original forcing is

`j_ij=[d_i(1+d_i)Z_ij+d_j(1+d_j)Z_ji`
`       +c_i c_j(d_i Z_ii+d_j Z_jj)]/(d_i+d_j)`.

Substitution gives `w_ij j_ij=f_ij/2`. Therefore, for the ACTUAL full forcing,

`j^*K_full^-1j=(1/4)f^*K_F^-1f`.  (A12)

Ordinary block inversion of(A9)–(A10) gives

`K_F^-1=D^-1+D^-1R^*Omega^-1R D^-1`.

Thus with h=R D^-1f,

`F_full(Z)=(1/4)sum_e |f_e|^2/beta_e+(1/4)h^*Omega^-1h`.  (A13)

Every step applies to all12 complex source directions and all6 complex forcing directions. No selected source sector, matched row constraint, reality/symmetry hypothesis on Z, or discarded p/q mixed term has been introduced.
Equations(A8)–(A13) now admit the ENTIRE v24 Theorem1 proof directly: take its u_i=s_i eta_i, U=sum u_i, ell_ij=theta_ij s_i s_j, kappa=min Uell_ij/(u_i u_j), xi=sum s_i h_i and V=sum|h_i|^2/omega_i-|xi|^2/U. Its exact coherent-mode/three-potential decomposition, strict variance contraction and improved original energy lower bound therefore follow for every positive spectrum and ALL Zc=0. The v24 proof is REQUIRED IN FULL, not presumed accepted by this application.
The original p energy is still the literal `P(Z)=<Z,rho'Z>` from v1/v20, with the complete D0^2Z-D0diag(Z_ii)Q+rQZ^TQ operator. No lower p estimate replaces it in the application. E_full=P-F_full is the operator leaf being bounded; this proof supplies neither P>=F_full nor any rank<=2 W4 bridge.

## 6. Current union, exact unpaid step and assurance

This is an ADDITIVE full source-admission companion, not a silent edit to v24 or the old v7/v22 files. New current proof union is THIS complete companion PLUS ENTIRE127LF v24, with cp066's whole-source matrix interface if that application form is consumed. At this union every specialized mass/factorization/positive-pivot/supersolution/forcing edge needed for the new bound is proved from the printed literal raw entries. Ordinary exact algebra, finite Hermitian Schur complements/block inversion and weighted-Laplacian inequalities remain conventional background, not formal/kernel proofs.
The original physical co-Choi/raw-leaf derivation and W4 matching-reference bridge retain their actual older named boundaries; this algebraic operator-leaf proof does not authenticate or widen them. All historical source-probe/held-lead and process qualifications remain mandatory; complete displayed proof is not a global counterfactual provenance cure.
The first unpaid leaf step is STILL the complete p-side comparison in v24(K12), equivalently v20N_full/v22F4/originalv1C4. Even the improved whole-source sufficient matrix S_kappa in cp066 is UNPROVED. Coherent exactness, positive masses/pivots and strict graph gain are not original sign closure; the genuine A/C mixed comparison and the other three full signs/W4 remain unpaid. No failure/success at a selected state, control, boundary/limit or region is asserted.
No identity was machine-checked. No scientific interpreter/calculator/Eval/CAS/program/enumeration/solver/replay/build/test/CLI/nested agent/new GO, chosen numeric/state/control/boundary/limit/magnitude/decimal probe or withdrawn-guidance conversion. All algebra is all-variable original-source reconstruction. Same18/OWN/HOLD/N4 UNKNOWN/historical exit unestablished/auxiliary214 STOP/ALL findings/ZERO credit, cutoff2026-10-27T11:05:38-07:00, deadline12:35:38, actual<=30min substantive checkpoints and no early final park remain.
