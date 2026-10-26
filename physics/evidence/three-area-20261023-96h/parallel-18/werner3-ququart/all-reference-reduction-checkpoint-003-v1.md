# All-reference obligation — a universal Cauchy kernel and zero-block12-dimensional residuals

Before-creation clock observed: **2026-10-23T16:20:48-07:00**. Owner: PhysicsResearch96h. Intermediate **unreviewed written research checkpoint**, not a completed all-reference theorem. The single admitted fixed-reference assay has been executed by the parent and consumed; it found no failure among its seven references. None of the universal assertions below is inferred from those finite outputs, and no new scientific execution occurred.

The target remains all nonzero eta, both asymmetric signs, including all zero/repeated Schmidt coefficients. The precise frontier at the end is generic4 upper, generic nonzero-weight8 residuals for both signs, and zero-weight12 residuals for both signs. This is another analytical representation of the same target, not a restricted positive region.

## 1. A bounded Cauchy-kernel matrix

Use normalized amplitudes c_i>=0, x_i=c_i^2, sum x_i=1 and d_i=1-x_i. First assume Schmidt rank>=2 so d_i>0. Define the real symmetric4x4 matrix K by

`K_ii=0`,

`K_ij=c_i c_j/[2(d_i+d_j)]=c_i c_j/(4d_ij)` for i!=j.

**Claim: `||K||<=1/4`.**

Define another matrix

`N_ij=2c_i c_j sqrt(d_i d_j)/(d_i+d_j)`.

It is a Gram matrix: use the real L2[0,infinity) functions `sqrt(2)c_i sqrt(d_i) exp(-d_i t)`. Their inner products are exactly N_ij. Hence N>=0, and `Tr N=sum_i x_i=1`, so N<=I. Congruence by diag(1/sqrt(d_i)) gives

`diag(1/d_i)-[2c_i c_j/(d_i+d_j)]_(ij)>=0`.

Its diagonal is1 and its off-diagonal is-4K_ij. Therefore **I-4K>=0**, proving lambda_max(K)<=1/4. Since K has nonnegative entries, for every complex v,

`|v†Kv|<=|v|^T K|v|<=(1/4)||v||^2`.

This also bounds its negative spectrum, proving the norm claim. At a product probability vertex K is directly zero; the off-diagonal formula is continuous there, so the same bound holds without inserting a divergent diagonal inverse.

This is a written positive-Gram/trace proof, not a matrix-eigenvalue sample or numerical bound.

## 2. Exact symmetric/antisymmetric split of the zero-charge q space

Checkpoint002's zero-charge coordinates are p(i,j)=|iijj> and q(a,b)=|abba>, a!=b. The p-q entries of BOTH C_B and S_eta are unchanged when q(a,b) is replaced by q(b,a). Its q-q table also commutes with that reversal. Thus the six-dimensional antisymmetric space

`q^-_(ab)=[q(a,b)-q(b,a)]/sqrt(2)`, a<b,

is a genuine reducing subspace, with no p coupling. The symmetric six-dimensional space uses q^+ with the plus sign.

On q^- the physical C form is `(3/4)I`. On q^+ it is `(5/4)I`. Associate q coefficients with off-diagonal4x4 matrices W, antisymmetric or symmetric as appropriate; the Hilbert-Schmidt norm equals the physical coefficient norm in these normalized bases.

Let E be the diagonal pair operator with entries E_ab from checkpoint001. It satisfies `0<=E<=I/4`. Let L_K act on matrices by

`L_K(W)=K W+W K`.

Its Hilbert-Schmidt operator norm is at most2||K||<=1/2. From the complete q-q physical table,

`S_-=-E-L_K` on antisymmetric W,

`S_+=E+Pi_offdiag L_K Pi_offdiag` on symmetric off-diagonal W.

The signs follow directly from W_ba=±W_ab in the reversed-edge and two chain terms. For antisymmetric W the anticommutator automatically remains antisymmetric with zero diagonal; for the symmetric space the explicit orthogonal projection is retained.

Consequently

`-(3/4)I<=S_-<=(1/2)I`,

`-(1/2)I<=S_+<=(3/4)I`.

Thus the ENTIRE q^- reducing subspace has

`C_- - S_->=I/4`, `3C_-+S_->=(3/2)I`.

The q^+ principal upper block is also uniformly positive:

`D_q=C_+-S_+>=I/2`, and `D_q<=(7/4)I`.

The q^+ subspace itself still couples to p; its positive principal block is not a proof of positivity of their combined block.

## 3. Reference-direction Schur subtraction on q^+

The four reference directions K_j=sum_i c_i p(i,j) are orthonormal, and their C block is

`A=diag(d_i)+c c^T/4>0`.

Let B be the4x6 C coupling from those reference directions to q^+. Its column for a<b is

`B_(ab)=-(c_b e_a+c_a e_b)/sqrt(2)`.

Therefore

`B B^T=(1/2)diag(1-2x_i)+(1/2)c c^T`.

A useful universal bound is **BB^T<=(3/4)A**. Indeed,

`(3/4)A-BB^T=[4diag(1+x_i)-5c c^T]/16`.

For every v, weighted Cauchy-Schwarz gives

`|c^T v|^2 <=[sum_i x_i/(1+x_i)]*[sum_i(1+x_i)|v_i|^2]`.

The scalar function x/(1+x) is concave, so its four-term sum at total mass1 is at most4/5. This proves the displayed matrix inequality, without a pure-state sampling assumption. Equivalently

`B^T A^-1 B<=(3/4)I`,

and the Schur complement of C on q^+ after the reference directions is at least

`C_q,Schur=(5/4)I-B^T A^-1 B>=I/2`.

For the upper difference D=C_B-S_eta the reference directions are exact zero modes, so their removal leaves D_q unchanged. For the lower form `3C_B+S_eta=4C_B-D`, the q^+ block AFTER eliminating the positive4A reference block is

`4 C_q,Schur-D_q`.

Using the bounds above, it is at least

`4*(1/2)I-(7/4)I=I/4`.

This is the required strict positivity of the q^+ pivot in the **lower Schur complement**. Positivity of its unsubtracted principal block alone would not have justified this elimination.

The argument remains valid at rank-one references: A itself remains positive and B is regular; the Cauchy-K bounds extend as explained. No inverse of a vanishing d_i is substituted at that endpoint.

## 4. The resulting exact12-dimensional zero-block obligations

The original zero block has28 dimensions. The reducing q^- part removes6 with both signs proved above. The remaining22 consist of p16 and q^+6.

For the upper sign, remove the four known reference kernels from p16, leaving its12-dimensional constraint space `c^T Z=0`. On that space let D_p be checkpoint002's explicit p quadratic form and F its coupling to normalized q^+. Then the exact remaining upper condition is

**`D_p-F† D_q^-1 F>=0`.**

The inverse exists because D_q>=I/2. This is a12-dimensional form, not a24-dimensional one.

For the lower sign, first eliminate4A on the reference directions as in checkpoint002. Call the resulting p/q^+ block R. Section3 proves `R_qq>=I/4`, so the exact remaining lower condition is

**`R_pp-R_pq R_qq^-1 R_qp>=0`.**

Again this is12-dimensional. All reference cross couplings are retained before the second elimination. The two12-dimensional signs remain **UNPROVED**; bounding their individual pivots does not settle their Schur remainders.

## 5. Current literal residual and scope control

The all-reference sufficient route remains NOT PROVED, and no exact failure has been found. The finite assay is only finite evidence and is not reused as a universal premise.

The exact remaining written obligations are now:

- generic four-dimensional upper form from checkpoint001; its lower sign follows conditionally from checkpoint002's relative trace;
- the two eight-dimensional Schur residuals in each12-weight block, with full generic mixed-input inverse corrections;
- the two12-dimensional zero-weight remainders in Section4.

All endpoints and all four Schmidt coefficients remain in scope. No extra sampling, root search, CAS, model CLI or nested agent has been authorized or run. The purpose of this checkpoint is the explicit Gram/Schur reduction of the SAME universal target, not another sector counted as an independent discovery or a completed theorem.
