# All-reference obligation — complete12-weight table and seven-dimensional residuals

Before-creation clock observed: **2026-10-23T16:38:17-07:00**. PhysicsResearch96h. Intermediate unreviewed written checkpoint, not a completed universal candidate. No new scientific execution. The fixed-reference GO is consumed; the proposed universal polynomial certificate has no GO yet.

The target is still BOTH asymmetric signs for all nonzero eta, not a smaller reference family. This packet completes the generic physical12-dimensional table and reduces both its signs to seven-dimensional residuals. The zero-block12-dimensional residuals and generic4 upper sign remain open.

## 1. Notation and orthonormal coordinates

Use normalized amplitudes c_i>=0, x_i=c_i^2, sum x_i=1. Retain

`d_ij=1-(x_i+x_j)/2`, `d_i=1-x_i`, `q_i=x_i/d_i`,

`z=sum q_i`, `r=1/(4+z)`.

The q_i formulas are used for Schmidt rank>=2; the actual physical matrices extend continuously to the product vertices and are handled there without divergent substitutions.

Fix a!=b and let O={j,k} be the two remaining labels. The complete orthonormal coordinate basis of weight e_a-e_b is

`Q_i=|iiab>`, all four i,

`P_i=|abii>`, all four i,

`R_j=|ajj b>`, `T_j=|jba j>`, j in O.

Spaces or commas in the last strings are separators only: R_j has slots(a,j,j,b), T_j has(j,b,a,j). These are exactly twelve distinct computational vectors.

Put

`tau_i=1-(delta_(ia)+delta_(ib))/2`, `A=diag(tau_i)`,

`d=d_ab=c^T A c`, `f=A c`, `v=c_b e_a+c_a e_b`,

`sigma_i=1-2delta_(ia)-2delta_(ib)`.

The exact reference kernel is `K=sum_i c_i Q_i=eta_input tensor |ab>_output`, of norm1. It follows from the direct reference identity, not from an assumed sign.

## 2. The entire C form

Its nonzero blocks, beyond symmetric counterparts, are

`C_QQ=C_PP=A`,

`C_Q,Pi=(sigma_i/4)e_i`,

`C_Q,Rj=C_Q,Tj=C_P,Rj=C_P,Tj=-(1/2)e_j`, j in O,

`C_(R,T)=[[I2,I2/4],[I2/4,I2]]`.

There are no further entries. For i=a,b these formulas give the actual2x2 blocks with diagonal1/2 and cross-1/4; for the two spectators they give the actual4x4 swap blocks. No contraction-basis Gram matrix is involved.

## 3. The entire S form, with full generic inverse correction

The Q blocks from checkpoint002 are

`S_QQ=f f^T/d`,

`S_Q,Pi=C_Q,Pi-G_Pi`,

`G_Pi=kappa_i(e_i-c_i c)`,

`kappa_i=[sigma_i/4-r nu]/d_i`, `nu=z/4-(q_a+q_b)/2`.

For j in O let `A_(uv)=diag(1-(delta_(iu)+delta_(iv))/2)`. Then

`S_Q,Rj=C_Q,Rj-G_Rj`,

`G_Rj=-(1/2)e_j+[c_j/(2d_jb)]A_(jb)c`,

`S_Q,Tj=C_Q,Tj-G_Tj`,

`G_Tj=-(1/2)e_j+[c_j/(2d_aj)]A_(aj)c`.

Every G column is orthogonal to c. The quantities involving r are retained, not replaced by the paired mixed-input cancellation.

The newly completed remaining blocks are

`S_PP=v v^T/(4d)`,

`S_(Pi,Rj)=[c_a c_j delta_(ia)+x_a delta_(ij)]/(4d_aj)`,

`S_(Pi,Tj)=[c_b c_j delta_(ib)+x_b delta_(ij)]/(4d_bj)`.

Finally define

`beta=[(q_j+q_k+q_j q_k)-(q_a+q_b+q_a q_b)]/[4(4+z)]`,

`k0=c_j c_k/(4d_jk)`, `B=[[beta,k0],[k0,beta]]`.

The full R/T block is

`S_(R,T)=[[0,B],[B,0]]`.

All displayed entries specify the complete generic12-dimensional S; nothing remains to be inferred from a kernel or an old numerical assay.

### Direct physical derivations of the new blocks

The universal adjoint vector is

`L_uv†|pq>=delta_(uv)c_u|pq>-(c_v/2)delta_(up)|vq>-(c_u/2)delta_(vq)|pu>+(1/4)delta_(up)delta_(vq)eta`.

For P_i the input is always(a,b), so `L_ab†|ii>` vanishes except at i=a,b, where it is respectively `-c_b|ba>/2` and `-c_a|ba>/2`. The full inverse on|ba> is1/d, proving S_PP.

For P_i,R_j, the two surviving possibilities are i=a and i=j. They give intermediate|ja> with coefficients(c_j/2,c_a/2) or(c_a/2,c_a/2), hence the stated c_a c_j and x_a entries divided by4d_aj. The T analogue is obtained with|bj>. These intermediate vectors are genuinely off diagonal, so their inverse correction is zero for this contraction for an exact reason.

The R-R and T-T entries vanish directly. For distinct spectator labels j,k, the R_j,T_k contraction is `c_j c_k/(4d_jk)`. For j=k, its two diagonal intermediate vectors are

`eta/4-(c_b|bb>+c_j|jj>)/2`,

`eta/4-(c_a|aa>+c_j|jj>)/2`.

Their D-inverse product minus the FULL rank-one correction is exactly beta, the same regular rational expression already derived for the two-dimensional phase blocks. Interchanging j,k leaves beta unchanged. These computations recover the full R/T form without deleting generic nu terms.

## 4. Uniform R/T principal bounds

Checkpoint001 gives `|beta|<=1/4`. Also `0<=k0<=1/4`, either from the Cauchy-kernel lemma in checkpoint003 or directly from arithmetic-geometric mean and x_j+x_k<=1. Thus `||B||<=1/2`.

In the normalized R±T directions, the upper form D=C-S has the two2x2 principal blocks

`D_+=(5/4)I-B>=3I/4`,

`D_-=(3/4)I+B>=I/4`.

The raw lower principal blocks are

`(3C+S)_+=(15/4)I+B>=13I/4`,

`(3C+S)_-=(9/4)I-B>=7I/4`.

These are principal-block bounds only; R/T still couples to P and to the Q complement, so they do not close the12-dimensional matrix.

## 5. Lower R/T pivot AFTER the reference Schur subtraction

For the lower form, deleting K would be wrong. Its actual positive block is4d, since D vanishes on K. The C pairing from K to R_j and T_j is exactly `-c_j/2`. Thus only the normalized R+T block couples to K, with vector `-c_O/sqrt(2)`.

After eliminating4d the plus principal block becomes

`(15/4)I+B-2c_O c_O^T/d`.

Here `||c_O||^2=1-T`, where `T=x_a+x_b` and d=(2-T)/2. Therefore

`||2c_O c_O^T/d||=4(1-T)/(2-T)<=2`,

and the subtracted plus block is still at least

`(15/4)I-(1/2)I-2I=(5/4)I`.

The minus block is unaffected and remains at least7I/4. Hence the lower R/T block **after the reference elimination**, not merely before it, is strictly positive with bound5I/4.

The upper reference kernel has zero cross-form with all other directions, so removing it does not alter the upper R/T principal blocks. Both subsequent R/T eliminations are therefore legitimate.

## 6. Exact seven-dimensional residual obligations

Choose the orthogonal complement c^T Q=0 in the Q space. Together with P4 it has dimension3+4=7. The known Q reference direction has been kept as an upper zero and eliminated with its true4d lower coupling.

- For the **upper** form, first remove its K kernel. The R/T block is positive, so its exact Schur complement on `(Q_perp,P)` is a seven-dimensional form. Its nonnegativity is equivalent to the full12-weight upper inequality.
- For the **lower** form, first eliminate4d on K, then its proven positive R/T block. The resulting seven-dimensional Schur form on the same `(Q_perp,P)` space is exactly equivalent to full12-weight lower positivity.

Every raw block and pivot needed to write these two residuals is given above. Neither seven-dimensional sign is yet proved. This representation improves the earlier eight-dimensional residual without restricting c or hiding a missing reference cross term.

## 7. Literal frontier

The all-reference sufficient route remains NOT PROVED; no exact route failure is known. The finite assay was positive only on its listed references and supplies no universal premise.

The active written residual is now generic4 upper (with its lower sign conditional on the upper), both seven-dimensional nonzero-weight residuals, and both zero-weight12-dimensional residuals. All normalized four-coefficient references remain included; product-reference vertices are handled by the known direct argument/physical continuity, not a division by a vanishing d_i. No new sampling or symbolic execution has been authorized by this checkpoint.
