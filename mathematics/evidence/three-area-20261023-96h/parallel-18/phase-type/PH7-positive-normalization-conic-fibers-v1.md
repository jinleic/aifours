# PH7 at8/9: exact positive-normalization reduction to common-block conic fibers

Actual returned `/bin/date` before this freeze: **Sun Oct 25 04:13:32 PDT 2026**. MathResearch96h, math-1. This packet was derived in WRITING after the parent withdrew the eval-arithmetic exception. No new scientific interpreter, arithmetic/enumeration, replay or solver was run for it. `resumption-arithmetic-authorization-addendum-v1.md` remains mandatory for the earlier computation-supported packets; none is rerun here.

## 1. Purpose and actual advance

The complete shared-block system at8/9 has nonlinearly coupled PH row/exit ties. They cannot simply be discarded. They CAN instead be recovered by a proved positive normalization, leaving a finite-dimensional LINEAR conic problem once the principal blocks and raw boundaries are fixed.

This packet gives that exact equivalence for the FULL union of shared-block cases. It does not assume two Erlang blocks, fix their rates, exclude feedback r,D,f, localize hidden eigenvectors, or replace actual numerator factors by independent positive polynomials. It is a new exact representation, **not an8/9 feasibility verdict**. The outer search over actual common principal blocks remains unproved.

Scientific imports, at their existing written boundaries:

- The unrestricted dominator theorem `PH7-dominator-normal-form-v1.md`, SHA256 `5e259982c3fe8f762acc0546080aa87afec405e0cbc34b00afc460f01b39f846`.
- The common-block determinant/numerator identities `PH7-dominator-shared-block-identities-v1.md`, SHA256 `941ea246ba96e00e820021733b0d716e79cc103807a86f97ee5b31dfabf5b969`.
- B6, `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, excluding all PH orders≤6 when z>1/2. The only use of B6 below is to remove zero coordinates from an otherwise nonnegative normalization vector.

No novelty claim: positive diagonal normalization and finite conic separation are classical tools. The new scope is their exact composition with this actual seven-state shared-block system.

## 2. Positive-realization normalization, including zero coordinates

Let M be a finite Hurwitz Metzler matrix, beta≥0 a row and gamma≥0 a column. Suppose

`beta(sI-M)^(-1)gamma=H(s)` and `H(0)=1`.

Set `h=(-M)^(-1)gamma≥0`, using the positive semigroup integral. Let S be the indices with h_i>0.

An index is in S exactly when it reaches a positive gamma coordinate by a directed nonnegative off-diagonal path, including a path of length0. This follows directly from the series for `exp((M+Lambda I)t)` after choosing Lambda to make its entries nonnegative: a positive path gives a positive semigroup entry for every positive t, and absence of every path gives zero for all powers and thus the integral.

Consequently there is NO positive transition from an index outside S into S. After permutation, M has block form

```
M=[ M_SS      M_S,out
     0        M_out,out ],     gamma=(gamma_S,0)^T.
```

Its full transfer is exactly `beta_S(sI-M_SS)^(-1)gamma_S`. The principal block M_SS is Hurwitz Metzler; h_S is strictly positive and satisfies

`M_SS h_S=-gamma_S`.

With Δ_S=diag(h_S), define

`T_S=Δ_S^(-1)M_SS Δ_S`,

`alpha_S=beta_S Δ_S`,

`omega_S=Δ_S^(-1)gamma_S`.

Then `T_S1=-omega_S≤0`, alpha_S≥0 and

`alpha_S1=beta h=H(0)=1`.

Similarity preserves the transfer, so this is a PH representation with |S| states. This is an explicit proof that trimming zero normalization coordinates is valid; it does not suppose the raw positive realization was already a Markov chain.

For the frozen target z=8/9, B6 forces |S|≥7. Therefore any SEVEN-state raw positive realization of H has S equal to the entire state set and h>0 automatically. Positive normalization then produces a literal seven-state PH pair without needing to impose nonlinear row sums on the raw coefficients. Conversely every PH7 is already such a raw realization. Thus, at this target, the two seven-state existence questions are exactly equivalent.

The reduction is equally valid for any z>1/2 at the same B6 import. No claim is made that h>0 follows without the lower-order exclusion for arbitrary H.

## 3. Outer data remain actual blocks and actual boundaries

Keep c,d>0, a=c+d, z=8/9 and

`D5(s)=(s+c)((s+a)²+b²)²`, `K=D5(0)`.

Fix m,n≥1 with m+n=6. Choose the following OUTER data:

- actual real Hurwitz Metzler blocks A (m-by-m), F (n-by-n);
- actual nonnegative columns b∈R^m, gamma_S∈R^n;
- actual nonnegative rows beta_R∈R^m, t^T∈R^n.

Define, FROM THOSE SAME ENTRIES,

```
a_R=det(sI-A),       a_S=det(sI-F),
v(s)=adj(sI-A)b,     w(s)=t^T adj(sI-F),
N_R(s)=beta_R v(s),  N_S(s)=w(s) gamma_S.
```

Require the ACTUAL product to satisfy

`N_R(s)N_S(s)=K Q(s)`,                                   (N)

where Q is a real monic Hurwitz quadratic. Its discriminant is unrestricted. The fixed product must have degree2. This is not an independently chosen scalar factorization: beta_R, b, t, gamma_S, A,F occur literally in N_R,N_S. An overall positive scaling of gamma_S can arrange the leading coefficient K when the unscaled product has positive leading coefficient; it does not change its roots or manufacture a missing numerator.

Write `Q(s)=s²+p s+q`. Hurwitz means p,q>0. The normal-form degree allocations remain complete and unchanged. In particular a nonreal pair must lie wholly in one of the actual degree2 numerator factors; that still does not put its eigenvectors or eigenvalues in a principal block.

No PH row tie is imposed on these RAW outer data. Section2 supplies the missing ties after an actual stable common matrix has been found, so their removal is an equivalence proved below, not a relaxation.

## 4. Inner feasibility is one exact finitely generated cone

For these fixed outer data, form the common matrix

```
M=[ A     b       0
    r^T  -lambda  t^T
    D     f       F ],
beta=(beta_R,0,0),   gamma=(0,0,gamma_S)^T,
```

where r,f,D are the INNER unknown actual nonnegative entries.

The degree-six coefficient of `det(sI-M)` fixes lambda; no extra diagonal variable is needed. Since the degree-four coefficient of D5 is `c+4a`, trace equality gives

`lambda=c+4a+p+tr(A)+tr(F)`.                              (L)

Require this value to be positive. Then define the ONE fixed residual polynomial

`R(s)=(s+lambda)a_R(s)a_S(s)-D5(s)Q(s)`.

The monic degree-seven terms cancel; equation(L) cancels degree six. Thus R has degree at most5. Define the following finite list of actual polynomial generators:

```
g_(r,j)(s)=a_S(s) v_j(s),                j=1,...,m,
g_(f,k)(s)=a_R(s) w_k(s),                k=1,...,n,
g_(D,k,j)(s)=w_k(s) v_j(s),              k=1,...,n, j=1,...,m.
```

They have degree at most5,5,4, respectively. The full characteristic identity is EXACTLY

`R = sum_j r_j g_(r,j) + sum_k f_k g_(f,k)
       + sum_(k,j) D_(k,j) g_(D,k,j)`.                    (C)

All coefficients multiply the same entries appearing in M. Consequently inner feasibility is precisely membership of the coefficient vector of R in the finitely generated cone of these coefficient vectors in R^6. It is a simultaneous all-coefficient equality, not six separately chosen polynomial signs. There is no assumed independence of the earlier W,V,U path sums.

The numerator identity for M is the unchanged product (N), regardless of the inner feedback entries. Thus a solution of (C) gives

`det(sI-M)=D5Q`,  `beta adj(sI-M) gamma=KQ`.

All roots of D5Q are strictly stable, so M is Hurwitz. It is Metzler by actual nonnegative entries. Its transfer is exactly H. Section2 and B6 give h>0 and the normalized seven-state PH pair with literal row/exit ties. This proves SUFFICIENCY of the conic fiber.

For NECESSITY, start with any actual PH7. The imported dominator theorem supplies this block form, with its actual beta=alpha and gamma=omega. Its principal blocks are Hurwitz Metzler; the imported shared identities give (N), (L) and (C). Its actual outer data therefore belong to one of these fibers. Hence the FULL UNION over the actual outer choices and all m+n=6 is equivalent to unrestricted PH7 existence at8/9.

This argument neither omits backwards D nor assumes a free exit vector in a PH matrix: gamma is free ONLY at the raw-positive level, and the PH exit is subsequently `diag(h)^(-1)gamma=-T1`.

## 5. Exact dual alternative and what the new slice certificate proves

For fixed outer data, finite-dimensional conic separation gives the exact alternative:

1. (C) has nonnegative coefficients, hence a raw positive realization and therefore PH7; or
2. there is a real linear functional ell on degree≤5 polynomials with

`ell(g_(r,j))≥0`, `ell(g_(f,k))≥0`, `ell(g_(D,k,j))≥0`,

but `ell(R)<0`.

A finitely generated cone is closed, so this is genuine separation, not a limit/exhaustion assumption. If all outer entries are rational, the fiber is a rational linear system and a nonempty fiber has a rational solution; an empty fiber admits a rational separating functional. This standard rational-polyhedral statement does NOT imply that the full OUTER problem can be restricted to rational data: an admissible outer point could require algebraic or other real entries.

The displayed functional in `PH7-eight-ninths-feasibility-verdict-v1.md` (with its sign reversed to match the convention here) is exactly such a dual certificate for ONE fixed outer principal-block family. Its remarkable cancellation of both hidden coefficients does not make it uniform over general A,F. This explains both its real force and its precise limitation without treating failed numerical slices as evidence of universal infeasibility.

## 6. Exact first unproved step and execution boundary

The unresolved8/9 question is now a union of exact conic fibers indexed by actual nonnegative boundaries and actual principal Metzler blocks. The unsolved step is whether ANY admissible outer data make the fiber nonempty, or whether a separator can be proved uniformly for ALL admissible outer data and complete degree allocations. No such outer witness or uniform separation is supplied.

No interpreter or finite enumeration was run to evaluate these fibers after the parent's correction. No new GO is presumed. A future proposed computational fiber study would need its own exact source/input pins and named HOLD-compliant admission; this written reduction does not authorize one. The current new band and point-slice certificate retain their mandatory provenance addendum and candidate status. The full point minimum remains{7,8}, not exact8, and no formal, human, cross-vendor or novelty acceptance is asserted.
