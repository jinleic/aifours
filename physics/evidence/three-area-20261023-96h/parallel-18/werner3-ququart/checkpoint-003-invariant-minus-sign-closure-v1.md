# Checkpoint 003 — the entire invariant minus sign is positive for every two-pair angle

Before-creation clock observed: **2026-10-23T14:18:32-07:00**. Slot physics-1. Status: **CANDIDATE written proof**, dependent on the explicitly reconstructed raw matrix table of checkpoint002, not independently checked yet. No scientific program, symbolic engine, finite parameter assay or new execution was used.

## 1. Exact conclusion and scope

For `eta_t=Omega_A+t Omega_B`, every t>0, the restriction of `C_B-S_eta` to the full eight-dimensional U(2)×U(2) fixed subspace is PSD and has **exactly** the two reference-input kernel directions K_A,K_B from checkpoint002. It is strictly positive on the remaining six directions.

Thus the invariant minus sign imposes **no additional angular cutoff** in this family. The invariant plus sign and the remaining248-dimensional complement remain unresolved. This is not full GS positivity, not an exact global angular criterion and not unrestricted W4.

The dependency is `checkpoint-002-eight-dimensional-angular-compression-v1.md`, SHA `47a24185bbf5f1a1de7fbe64f4ec585feda2b488b1e68b53c11fe35c7ad21ecf`. All calculations below are explicit rational identities and inequalities for its displayed5×5 minus form.

## 2. Parameters and a simplifying identity

Retain

`s=t^2`, `k=1/(1+2s)`, `l=s/(2+s)`, `p=kl`,

`L=k+l=1-3p`, `r=1/[4+2L]`, `g=-2t/(1+s)`.

For every finite t>0, k,l,p are positive, `0<p<=1/9`, and

`g^2=8p/(1-p)`.

The upper bound on p follows from `9s<=(1+2s)(2+s)`, equivalent to `2(s-1)^2>=0`.

Replace q_A,q_B by

`r_A=q_A-p_A/2`, `r_B=q_B-p_B/2`.

This is an invertible change of basis in the five-dimensional remainder. Directly from checkpoint002's raw S table,

`S(r_A,r_A)=S(r_B,r_B)=3L/8-(3r/4)(k-l)^2`.

Using `(k-l)^2=L^2-4p`,

`3L/8-(3r/4)(k-l)^2`

`=(3/8)[L-(L^2-4p)/(L+2)]`

`=(3/4)(L+2p)/(L+2)=1/4`.

The last equality is exact because L=1-3p. The off-diagonal r_A,r_B entry is zero. No parameter sampling is used to infer this constant.

Other simplified entries are

`S(p_A,p_A)=1/3+8k/[3(1-p)]`,

`S(p_B,p_B)=1/3+8l/[3(1-p)]`,

`S(p_A,p_B)=-8p/[3(1-p)]`,

`S(p_A,r_A)=-3k`, `S(p_B,r_B)=-3l`,

`S(p_A,r_B)=S(p_B,r_A)=0`,

`S(r_A,z_plus)=S(r_B,z_plus)=-g`,

`S(p_A,z_plus)=S(p_B,z_plus)=2g`, `S(z_plus,z_plus)=3L`.

For example `(9k+l)/2-r(3k+l)^2` simplifies to `(2p+8k+L)/(L+2)=1/3+8k/[3(1-p)]`. These identities expose the cancellation of the rank-one inverse term rather than hiding it in a determinant.

## 3. Exact block form of the minus matrix

Order the basis as `(p_A,p_B,r_A,r_B,z_plus)`. The p-p block of `C_B-S_eta` is

`P=(8/[3(1-p)]) [[l+2p,p],[p,k+2p]]`.

Its determinant is `64p/[3(1-p)]>0`, because

`(l+2p)(k+2p)-p^2=p(1+2L+3p)=3p(1-p)`.

Its inverse is particularly simple:

`P^-1=(1/8)[[1/l+2,-1],[-1,1/k+2]]`.

The cross block from p-p to r-r is

`A=-3 diag(1-k,1-l)`,

the p-p to z_plus column is `-2g(1,1)^T`, the r-r block is5I_2, the r-r to z_plus column is `g(1,1)^T`, and the z_plus diagonal is `10-3L`. These are the complete entries of the five-dimensional form after the basis change. In particular its r-r diagonal is `21/4-1/4=5`.

It remains to prove positivity of its Schur complement after the positive p-p block P is eliminated.

## 4. Schur complement with all factors retained

The relation `k+l+3kl=1` gives

`1-k=l(1+3k)`, `1-l=k(1+3l)`,

`(1-k)(1-l)=4p`.

The resulting Schur complement on `(r_A,r_B,z_plus)` is

`[[R,b],[b^T,z0]]`,

where

`R=[[ (9(1+k)^2+4)/8, (9/2)p ],`

`   [ (9/2)p, (9(1+l)^2+4)/8 ]]`,

`b=-(g/2)(1+3k,1+3l)^T`,

`z0=3(1+3p)`.

Here are independent simplifications of its entries:

- The first R diagonal is `5-(9/8)(1-k)^2(1/l+2)`. Since `(1+3k)(1+2l)=3+k`, this equals `5-(9/8)(1-k)(3+k)=(13+18k+9k^2)/8`, as displayed.
- The R off-diagonal is `+(9/8)(1-k)(1-l)=(9/2)p`; the minus sign in P^-1 is load-bearing.
- `P^-1(1,1)^T=(1/8)(1/l+1,1/k+1)^T`. Multiplying by1-k or1-l gives `(1+k)/4` or `(1+l)/4`, respectively. Thus the residual cross column is `g[1-(3/2)(1+k)]` and its l analogue, exactly b.
- `(1,1)P^-1(1,1)^T=(L+2p)/(8p)=(1-p)/(8p)`. Therefore the removed z contribution is `4g^2·(1-p)/(8p)=4`, leaving `10-3L-4=3(1+3p)`.

These verifications rule out losing a factor of two in the two p-z cross terms.

## 5. Uniform elementary positivity bounds

Every R diagonal is at least13/8. Its positive off-diagonal is at most1/2 because p<=1/9. Consequently

`R >= (9/8)I_2`, `||R^-1||<=8/9`.

The squared norm of b is

`||b||^2=(g^2/4)[(1+3k)^2+(1+3l)^2]`

`        =2p(17-90p+81p^2)/(1-p)`.

It is at most two throughout0<=p<=1/9. Indeed the desired inequality reduces to

`81p^3-90p^2+18p-1<=0`,

and its exact factorization is

`(9p-1)(9p^2-9p+1)<=0`.

The first factor is nonpositive, while the second is positive on this interval: it decreases there to1/9. Thus

`b^T R^-1 b <= (8/9)||b||^2<=16/9`.

Since z0>=3, the final Schur pivot is at least

`z0-b^T R^-1 b>=3-16/9=11/9>0`.

Both Schur eliminations are therefore strict for t>0. This proves that the entire five-dimensional minus remainder is positive definite for every t>0, with no numerical root or polynomial-positivity oracle.

## 6. Restoring the complete invariant sector and the unresolved part

Checkpoint002's separated z_minus direction has value `6+2h>0`. Its two reference directions K_A,K_B are exact zeros. Together with the positive five-dimensional remainder just proved, the full eight-dimensional invariant minus form is PSD with exactly those two kernel directions. At t=0 the basis change using1/t is not used; the original maps have a continuous limit, which gives PSD by closure, but additional kernel directions may appear. No uniform strict kernel claim is made at that endpoint.

This establishes a completed half of the invariant angular obligation: **only the invariant plus form can create an angular cutoff within this fixed subspace**. The plus form is still the explicit `C5+S5-2R_cross^T K2^-1R_cross` of checkpoint002, not simply C5+S5. Its exact sign interval and all nontrivial representation sectors of the full co-Choi space remain the next bounded written obligations.

The quartic negative tests of checkpoint001 are plus-sign failures and remain consistent. None of these co-Choi conclusions is an admissible rank-two negative W4 witness. This is one progressing primary route, not additional solved-problem/discovery counts, and no new scientific execution is admitted.
