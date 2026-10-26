# All-reference obligation — exact kernel deflations and complete zero-charge raw form

Before-creation clock observed: **2026-10-23T16:06:44-07:00**. Owner: PhysicsResearch96h. Intermediate written research checkpoint, **not** a completed all-reference theorem or isolated acceptance request. No scientific execution occurred. The proposed assay and its lifecycle-only successor remain UNEXECUTED without a fresh named GO.

The target remains BOTH asymmetric signs for EVERY nonzero two-ququart eta, or an exact failure of this sufficient route. It has not been replaced by the supported paired class or a small neighborhood. This checkpoint gives exact larger-block representations; it does not infer their positivity from known kernels.

## 1. Notation and a common denominator

Retain normalized nonnegative Schmidt amplitudes c_i, `x_i=c_i^2`, `sum_i x_i=1`, and for Schmidt rank>=2

`d_ij=1-(x_i+x_j)/2`, `d_i=1-x_i`, `q_i=x_i/d_i`,

`z=sum_i q_i`, `r=1/(4+z)`, `h_i=c_i/d_i`.

The full reference inverse is diagonal1/d_ij off the diagonal-pair subspace and has the4x4 diagonal-pair block

`G=diag(1/d_i)-r h h^T`.

This is the restriction of the FULL inverse, not the inverse of an unaccounted compression. Rank-one probability vertices are treated by actual physical continuity or the known product-reference argument, never by substituting divergent q_i. All zero/repeated values of rank>=2 already satisfy these formulas without a problem.

There is a useful denominator independent of how the four labels are paired:

`W=(4+z) product_i(1-x_i)=1+2e2(x)-e3(x)`.

For any partition into two pairs, put `T=x_i+x_j`, `m=x_i x_j`, `n=x_k x_l`. Then equivalently

`W=1+2T(1-T)+(1+T)m+(2-T)n`.

Consequently the scalar quantity from checkpoint001 has the regular form

`E_ij=[2+T(1-T)]/(4W)-1/4`.

In particular this expression, as well as W, remains regular at rank-one vertices by continuity. It also shows why treating the denominator separately for different pairs would obscure an exact identity.

For four distinct labels,

`E_ac-E_ad=-(x_a-x_b)(x_c-x_d)/(4W)`.

This controls the actual asymmetry of the four-dimensional table; it is not zero at a generic reference.

## 2. A conditional lower-bound reduction on the4x4 blocks

For the4x4 C4,S4 of checkpoint001 let `T=x_a+x_b`,

`a0=T/[4(2-T)]`, `b0=(1-T)/[4(1+T)]`,

`Eavg=(E_ac+E_ad)/2`.

The physical swap inverse is

`C4^-1=(16/9)(I+F13/2)(I+F24/2)`.

Multiplying its four permutation terms with S4 gives

`Tr(C4^-1 S4)=(16/9)[2(a0+b0)-Eavg]`.

Here `a0+b0>=1/6`, since

`a0+b0-1/6=(2T-1)^2/[6(2-T)(1+T)]`,

and Eavg<=1/4 by checkpoint001's pair-sum bound. Thus the trace is at least4/27.

**Conditional implication only:** if C4-S4>=0 is proved, its normalized deficit is PSD of dimension4 and has trace at most `4-4/27`. It follows immediately that

`3C4+S4>=(4/27)C4>0`.

Thus the outstanding four-dimensional universal obligation can be reduced to its **upper** sign. This does not prove that upper sign; entry bounds or the trace alone cannot do so.

## 3. Complete coordinate system for a12-dimensional nonzero weight

Fix distinct a,b and write the weight `e_a-e_b`. The four diagonal-input coordinate vectors are

`Q_i=|i,i,a,b>`, i=0,1,2,3.

A complementary eight-vector coordinate basis consists of

`P_j=|a,b,j,j>`, j=0,1,2,3,

and, for each j outside{a,b},

`R_j=|a,j,j,b>`, `T_j=|j,b,a,j>`.

These twelve vectors are distinct orthonormal computational vectors. The usual sixteen contraction names have four duplicates (`R_a=Q_a`, `R_b=P_b`, `T_a=P_a`, `T_b=Q_b`); none is counted twice here.

Define diagonal entries and a vector

`tau_i=1-(delta_(ia)+delta_(ib))/2`, `A=diag(tau_i)`, `f=A c`,

`d=d_ab=c^T A c`.

Direct physical contraction of the two off-diagonal output indices gives the EXACT Q block

`C_QQ=A`, `S_QQ=f f^T/d`,

so

`D_QQ=A-f f^T/d`, where D=C_B-S_eta.

It is a positive rank-three form, with exactly the known vector c as its kernel. This calculation is independent of any desired sign on the rest of the block: `L_ii†|ab>=c_i tau_i|ab>`, and the full inverse on|ab> is1/d because that vector is off the diagonal-pair subspace.

### All Q-to-rest upper couplings

For each P_j let

`nu=z/4-(q_a+q_b)/2`,

`sigma_j=1-2delta_(ja)-2delta_(jb)`,

`kappa_j=[sigma_j/4-r nu]/d_j`.

Then the upper coupling column is

`D_Q,Pj=kappa_j(e_j-c_j c)`.

For j outside{a,b}, write `A_(jb)=diag(1-(delta_(ij)+delta_(ib))/2)` and define A_(aj) analogously. The other columns are

`D_Q,Rj=-(1/2)e_j+[c_j/(2d_jb)] A_(jb)c`,

`D_Q,Tj=-(1/2)e_j+[c_j/(2d_aj)] A_(aj)c`.

Each column is orthogonal to c. For P this is immediate from c^T c=1. For R,T it follows from `sum_i x_i tau_i(pair)=d_(pair)`. These are explicit physical formulas, not couplings invented from the kernel.

For example `L_ab†|ab>=eta/4-(c_a|aa>+c_b|bb>)/2`, whose full-inverse diagonal coefficient at j is `h_j[sigma_j/4-r nu]`. Inserting `L_ii†|jj>=c_i(1-delta_(ij))|jj>+delta_(ij)eta/4` and the actual C swap entry gives precisely the P column above. The R,T columns have off-diagonal intermediate vectors, so their H correction is exactly zero for that contraction; no generic mixed-input correction has been discarded elsewhere.

### Exact upper Schur deflation, including the zero mode

Let B be the full4x8 matrix of these Q-to-rest columns. Since `c^T B=0`,

`D_QQ A^-1 B=B`.

Therefore completing the square with the Q variables gives the exact equivalence

`D>=0 iff D_rest-B^T A^-1 B>=0`.

The eliminated Q form has its one persistent reference kernel; it is not inverted as a nonsingular4x4 matrix. This reduces the generic12-dimensional upper problem to an explicit **eight-dimensional residual** once the remaining raw entries are written.

### Exact lower Schur deflation

For the lower form, `3C+S=4C-D`, its Q block is

`M_QQ=3A+f f^T/d>0`,

with exact inverse

`M_QQ^-1=(1/3)A^-1-c c^T/(12d)`.

Its Q-to-rest block is `H=4C_Q,rest-B`. Hence lower positivity is exactly equivalent to

`(3C+S)_rest-H^T[(1/3)A^-1-c c^T/(12d)]H>=0`.

The known C_Q,rest entries are `sigma_j e_j/4` on P_j and `-e_j/2` on R_j,T_j. Both signs have therefore been reduced without dropping the reference coupling, and without requiring equality of any Schmidt coefficients. **Neither eight-dimensional residual has yet been proved PSD.**

## 4. Complete zero-charge raw form

The28-dimensional zero space has an orthonormal coordinate basis

`p(i,j)=|i,i,j,j>`, all16 ordered pairs,

`q(a,b)=|a,b,b,a>`, all12 ordered a!=b.

For diagonal-pair vectors e_j set

`v_j=eta_diag/4-c_j e_j`,

`W_i^j=c_i(1-delta_(ij))e_j+delta_(ij)eta_diag/4`.

Here eta_diag is the four-component vector c. The FULL p-p raw co-Choi entries are

`S_(p(i,j),p(k,l))=(W_k^j)^T G W_i^l`.

For p-q, with a!=b,

`S_(p(i,j),q(a,b))`

`=-[c_i tau_i(ab)/(2d_ab)]*(c_b delta_(ja)+c_a delta_(jb))`,

where `tau_i(ab)=1-(delta_(ia)+delta_(ib))/2`.

The q-q entries are completely specified by the following disjoint cases:

- diagonal: `S_(q(a,b),q(a,b))=0`;
- reversed edge: `S_(q(a,b),q(b,a))=E_ab`;
- for a,b,t all distinct: `S_(q(a,b),q(b,t))=c_a c_t/(4d_at)`;
- for a,b,t all distinct: `S_(q(a,b),q(t,a))=c_b c_t/(4d_bt)`;
- all other entries: zero.

Hermitian symmetry supplies the reversed entries consistently. The nonzero chain cases come from one negative matrix-unit term on each side. The reversed case is the same full-inverse norm as the scalar form E_ab. The diagonal case vanishes because `L_ab†|ba>=0`. Thus this is a complete generic physical table, not a numerical sparse pattern.

The C form on p has diagonal1 for i!=j, diagonal1/4 for i=j, and off-diagonal1/4 only between p(i,j),p(j,i). On q it has diagonal1 and off-diagonal1/4 only between q(a,b),q(b,a). The p-q entry is

`C_(p(i,j),q(a,b))=-(delta_(ib)delta_(ja)+delta_(ia)delta_(jb))/2`.

These formulas, together with G, define every entry of the28-dimensional forms.

## 5. Reference-kernel quotient for the zero-block upper sign

The four known zero-block kernels are

`K_j=sum_i c_i p(i,j)=eta_input tensor |jj>_output`.

They follow from the physical reference identity before any positivity assumption. Since D is Hermitian, its quadratic form can be studied on their orthogonal complement. Write the p coefficients as a4x4 matrix Z=(z_ij); the complement condition is

`c^T Z=0`.

Let `V_ij=v_i^T G v_j`. Expanding the p-p table under this constraint cancels its first three outer-product terms and leaves

`S_pp[Z]=sum_(i,j) V_ij conjugate(z_ji) z_ij`,

`V_ij=delta_(ij)q_i+r[z/4-q_i-q_j-q_i q_j]`.

Consequently on this constrained p space the upper p-p part has

- coefficient1 on every off-diagonal `|z_ij|^2`;
- the opposite-pair coefficient `1/4-V_ij=r/(d_i d_j)` for i!=j;
- diagonal coefficient `1/4-V_ii=r/d_i^2-q_i`.

The last quantity need not be nonnegative separately; its coordinate is constrained by c^T Z=0. It cannot be treated as a free negative witness or silently deleted.

The p-to-q upper coupling can be written as a linear functional of Z. For a!=b,

`G_ab(Z)=-(z_ba+z_ab)/2`

`        -[x_a z_ab+x_b z_ba+c_a c_b(z_aa+z_bb)]/(4d_ab)`.

The full mixed term is `2Re sum_(a!=b) conjugate(G_ab(Z))*w_ab`, where w_ab are q coefficients. The upper q-q matrix is obtained from Section4: diagonal1, reversed coefficient1/4-E_ab, and the negative of the displayed chain coefficients. This is an exact24-dimensional upper quotient representation after the four known kernels are removed. Its sign is **unproved**.

## 6. Lower zero-block Schur complement retains those reference directions

The lower form does NOT vanish on K_j, so removing their coordinates as if they were upper zero modes would be wrong. In the K basis its C block is the actual reference diagonal-pair matrix

`C_KK=A_diag=diag(d_i)+c c^T/4`, `C_KK^-1=G`.

On an upper-orthogonal-complement vector (Z,w), the C pairing with K is the four-component vector

`g=(1/4)Z c-diag(c)diag(Z)-(1/2)(W+W^T)c`,

where W is the off-diagonal matrix with entries w_ab and zero diagonal. This follows directly from the three C entry classes in Section4 and c^T Z=0.

Because the upper difference vanishes on K, the lower block on K is4A_diag with cross4g. Its exact Schur complement is therefore

`(3C+S)_rest-4 g†G g`,

or equivalently

`4(C_rest-g†G g)-D_rest`.

This is the remaining lower24-dimensional quotient, with the actual reference couplings retained. No inverse of a rank-deficient upper block is used.

## 7. Literal scientific residual

All normalized amplitudes, including zero/repeated coefficients, remain in scope. The product-reference vertices are known directly; rank>=2 formulas above have a nonsingular full inverse. The universal route is still NOT PROVED and no exact failure has been found in written work.

The current exact remaining tasks are: the generic4x4 upper sign (its lower sign then follows from Section2), the two explicit eight-dimensional Schur residuals for every12-weight block, and the two zero-charge24-dimensional quotient forms. This is a change of analytical representation of the SAME target, not a smaller target or an empirical conclusion. Any separately admitted finite assay may locate an exact route obstruction but cannot replace these all-parameter proof obligations.
