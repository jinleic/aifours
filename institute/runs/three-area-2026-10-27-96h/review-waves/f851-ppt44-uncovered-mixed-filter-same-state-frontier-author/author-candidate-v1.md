# Author candidate: an exterior mixed-filter SN2 region

**Status.** Fresh, written GENERAL AUTHOR candidate for the exact displayed state and filter. The positive decomposition below is proposed for independent reconstruction and parent disposition; it is not a family, human, formal/kernel or publication/novelty acceptance. It strictly extends the particular ellipsoid/coordinate-line union in the frozen packet. It does not close the remaining mixed region or the global PPT44 question. No numerical detector or negative residual is used as evidence of Schmidt number 3.

## 1. Exact objects and quantified result

Write `ij` for `|i>_A tensor |j>_B` and `[v]=v v†`. For arbitrary real `s>1`, `r>1` with `(s−1)(r−1)>=4`, define the actual 4×5 positive operator

    Q = [00+11+22] + [01+12] + [10−21]
        + s([02+34]+[32]+[04])
        + r([20+33]+[23]+[30]).

For arbitrary finite complex `alpha,beta,gamma`, put `w=(alpha,beta,gamma,0)^T`, `K_w=[I_4 | w]`, and

    R_w=(I tensor K_w) Q (I tensor K_w)†,
    A=00+11+22,       B=01+12,       D=10−21,
    F=02+3w,          H=0w,           G=32,
    P=30,             J=20+33.

Thus, with `3w=alpha 30+beta 31+gamma 32` and `0w=alpha 00+beta 01+gamma 02`, the actual output is

    R_w = [A]+[B]+[D]+s[F]+s[H]+s[G]+r[P]+r[J]+r[23].       (1)

Let `a=|alpha|²`, `x=|gamma|²`, `y=|beta|²`, and, for `y>0`, define

    q = x/s + a/(r+s)
        + { [1+x+x²+a(1+x)]/s + a(x+a)/r }/y.             (2)

**Candidate theorem.** For every such `s,r` and every finite complex `alpha,beta,gamma` with `beta != 0` and `q<=1`, the *actual normalized physical output* has exact Schmidt number 2 and is PPT. Equality `q=1` is included. There are no restrictions on the complex phases. More generally, the exact positive-semidefinite condition on a displayed 4×4 matrix in (7), which can hold even when `q>1`, is also sufficient and yields the same explicit decomposition. Neither condition is asserted necessary for SN2.

This is an actual enlargement, not merely a reformulation of the frozen union: impose additionally `gamma != 0` and

    y/s+x/(s−1)>1.                                          (3)

These points are outside the retained ellipsoid and, because both `beta` and `gamma` are nonzero, outside both coordinate lines. For every admissible `s,r`, every finite complex `alpha` with `a<r+s`, and every nonzero complex `gamma` with

    x/s+a/(r+s)<1,                                          (4)

there are arbitrarily large *finite* `|beta|` and arbitrary beta phase satisfying both (2) and (3). In fact it suffices to take

    y > max( [ [1+x+x²+a(1+x)]/s + a(x+a)/r ]
             /[1−x/s−a/(r+s)],
             s[1−x/(s−1)], 0 ).                             (5)

All denominators in (5) are then strictly positive where used. This proves a nonempty open mixed exterior for every source-region pair `s,r`, with genuinely complex three-coordinate filters allowed; it does **not** assert coverage for every finite alpha, beta and gamma.

## 2. Rank-two character construction

Let `kappa=r/(r+s)` and `eta=s/(r+s)`, so `kappa+eta=1`. For `beta != 0` put

    X1 = (H−gamma F+gamma² G+alpha gamma P)/beta,
    X2 = gamma G+kappa alpha P,
    X3 = alpha(F−gamma G−alpha P)/beta,
    X4 = −eta alpha G.                                      (6)

Every `Xj` is supported on Alice rows 0 and 3. The complex coefficients in (6) are as written; they are not conjugated in a ket. The useful actual-vector cancellations are

    X1 = (alpha/beta)00 + 01 − gamma 31,
    X3 = (alpha/beta)02 + alpha 31.

For each of the six sixth roots of unity `z`, define

    V_z = A+zD+z^(−1)X1+z^(−2)X2+z^(−3)X3+z^(−4)X4.

In the output computational bases its coefficient matrix is

    ( 1+(alpha/beta)z^−1,   z^−1,               (alpha/beta)z^−3,             0 )
    ( z,                     1,                   0,                            0 )
    ( 0,                    −z,                   1,                            0 )
    ( kappa alpha z^−2,      alpha z^−3−gamma z^−1, gamma z^−2−eta alpha z^−4, 0 ).

The first row is `(z^−1+(alpha/beta)z^−2)` times the second row plus `(alpha/beta)z^−3` times the third. The fourth is `kappa alpha z^−3` times the second row plus `(gamma z^−2−eta alpha z^−4)` times the third. Thus every `V_z` has complex matrix/Schmidt rank at most 2. This remains true for arbitrary complex phases and all six roots, including `z=1`.

The exponents `0,1,−1,−2,−3,−4` are pairwise distinct modulo 6, so character orthogonality gives the exact identity

    (1/6) sum_(z^6=1) [V_z]
       = [A]+[D]+[X1]+[X2]+[X3]+[X4].                     (6a)

No root is sampled numerically; the displayed finite algebraic average is exact.

## 3. Positive residual and an explicit finite decomposition

Let `C` denote the linear map from `C^4` whose columns are the four actual bipartite kets `(F,H,G,P)`. Define the coordinate columns

    t1 = (−gamma, 1, gamma², alpha gamma)^T / beta,
    t2 = (0, 0, gamma, kappa alpha)^T,
    t3 = (alpha/beta)(1, 0, −gamma, −alpha)^T,
    t4 = (0, 0, −eta alpha, 0)^T,
    Lambda = diag(s,s,s,r),
    M = Lambda − sum_(j=1)^4 t_j t_j†.                      (7)

These are complex outer products: in particular `t_j t_j†`, not `t_j t_j^T`. Equation (6) says `Xj=C t_j`. Consequently (1) and (6a) give the exact actual-object residual identity

    R_w = (1/6) sum_(z^6=1) [V_z]
          + [B] + r[J] + r[23] + C M C†.                   (8)

Whenever `M>=0`, let `M^(1/2)` be its unique positive Hermitian square root and set

    Psi_i = C M^(1/2) e_i,    i=1,2,3,4.

Then `C M C†=sum_i [Psi_i]`; each `Psi_i` is supported only in Alice rows 0 and 3 and therefore has Schmidt rank at most 2. Also `B` and `J` have rank 2 and `23` has rank 1. Thus (8), with those four explicit square-root columns, is a finite positive rank-at-most-2 decomposition of the actual `R_w`, including when `M` is singular. All coefficients are nonnegative. This is a construction, not a claim that a nonpositive residual would prove SN3.

For an equivalent exact test of this *particular* residual, form the 4×4 matrix `W` with columns `Lambda^(−1/2)t_j`. Since `s,r>0`,

    M>=0  iff  I_4−W W†>=0  iff  I_4−W† W>=0.             (9)

The second test is a finite Hermitian PSD condition with all entries explicitly determined by (7), valid for arbitrary complex coordinates. It may certify more than (2).

For the simpler closed scalar region, direct calculation gives

    sum_j ||Lambda^(−1/2)t_j||²
       = x/s + a/(r+s)
         + { [1+x+x²+a(1+x)]/s + a(x+a)/r }/y = q.        (10)

The `a/(r+s)` term uses `kappa²/r+eta²/s=1/(r+s)`. For every complex column `v`, Cauchy–Schwarz gives

    v† M v >= (1−q) v† Lambda v.

Thus `q<=1` proves `M>=0`, including equality. Division by beta is the only parameter division beyond strictly positive `s,r,r+s`; `beta=0` is not covered by this construction and is not silently obtained by taking a limit.

**Sharper explicit alpha-zero mixed subregion.** When `alpha=0`, the terms `t3,t4` vanish. For `0<=x<s` and `y>0`, subtracting `t2 t2†` first leaves `diag(s,s,s−x,r)`. The rank-one Schur-complement criterion shows that this particular `M` is PSD exactly when

    y >= (1+x)/s + x²/(s−x).                               (11)

For `x>=s` with `x>0`, this `M` is not PSD, since its G-diagonal entry is `s−x−x²/y<0`; this says nothing about another decomposition. Condition (11) can be combined with `x>0` and (3), yielding another explicit genuine mixed exterior. Its equality boundary and `x=0` limit are included. This special case supplements, rather than replaces, the arbitrary-complex-alpha theorem above.

## 4. PPT, physical normalization and lower bound

The PPT claim can be reconstructed directly from the displayed `Q`, without importing the source's linked proof. Partial transpose on Bob gives a direct sum of:

* scalar blocks `1,1,s,r` on `00,22,34,33`;
* all-ones 2×2 blocks with coefficients `1,1,s,r` on `(01,10)`, `(12,21)`, `(04,32)`, `(23,30)`;
* the block, in order `(11,02,20)`,

      N = [[1, 1,−1], [1,s,1], [−1,1,r]];

* a zero block on `03,13,14,24,31`.

Taking the Schur complement of `N_11=1` gives `[[s−1,2],[2,r−1]]`, which is PSD exactly under the stated source-region inequality and `s,r>1`. Hence `Q^Gamma_B>=0`. For a complex filter the required identity is

    R_w^Gamma_B=(I tensor conjugate(K_w)) Q^Gamma_B
                 (I tensor conjugate(K_w))† >= 0,

not the generally wrong identity with unconjugated `K_w`. The output is positive by construction. This establishes the filtered PPT statement in the specified region, not an iff classification outside it.

The trace of the input and actual output is

    T=tr Q=7+4(s+r),
    n=|alpha|²+|beta|²+|gamma|²,
    Z_w=tr R_w=7+2s(1+n)+4r.

`K_w K_w†=I_4+w w†` has largest eigenvalue `1+n`. Thus the physical Kraus contraction is `K_w/sqrt(1+n)`, and, on input `Q/T`, its success probability and conditional output are

    p=Z_w/((1+n)T),       rho_w=R_w/Z_w.

They are well-defined and strictly positive for all finite `w`; indeed `(1+n)T−Z_w=2s+(7+2s+4r)n>0`, so `p<1`. The decomposition (8), divided by `Z_w`, is the physical state's positive SN2 decomposition. Both local supports have rank 4: `[A]` supplies local levels 0,1,2, while the positive `[J]` term supplies level 3 on each side.

For the lower bound, every vector in `range R_w` has a coefficient matrix of the following form for some complex `a0,b,c,d,e,f,g,h,k`:

    ( a0+alpha h,  b+beta h, c+gamma h, 0 )
    ( d,           a0,        b,         0 )
    ( e,          −d,         a0,        k )
    ( f+alpha c,   beta c,    g+gamma c, e ).

For a product vector its minors

    m1=a0²+bd,    m2=a0 d−be,    m3=a0 e

all vanish: they use rows/columns `(1,2;1,2)`, `(1,2;0,2)` and `(1,3;1,3)` respectively, in zero-based indices. The identity

    a0² m1−a0 b m2−b² m3=a0^4

therefore forces `a0=0` over the complex numbers, so every product vector in the range has zero `11` coefficient. But `(R_w)_(11,11)=1`. In any positive separable decomposition, every summand must lie in `range R_w` because each is orthogonal to `ker R_w`; hence such a decomposition is impossible. This proves SN>=2 for all finite `w`. Combining it with (8) proves **exact SN2** in the stated new region.

The displayed source states that the original 4×5 parent has SN3. That historical source-boundary assertion is not needed for the above filtered-output theorem and is not independently proved here; the linked underlying source bodies were not opened. If describing this as an SN3-to-SN2 physical transition, the parent SN3 claim remains a named conditional import from the frozen packet.

## 5. Concrete mixed, three-coordinate, exterior physical member

Take `s=r=3` and `(alpha,beta,gamma)=(1,3,1)`. Then `(s−1)(r−1)=4`, `a=x=1`, `y=9`, and

    q = 1/3+1/6+(7/3)/9 = 41/54 < 1,
    |beta|²/s+|gamma|²/(s−1) = 9/3+1/2 = 7/2 > 1.

Both beta and gamma are nonzero, and alpha is also nonzero, so the member is outside all three retained certificates. Formula (8) gives its exact positive rank-2 decomposition, not a numerical test. Its actual `n=11`, `T=31`, `Z_w=91`, physical Kraus operator `K_w/sqrt(12)`, and exact success probability is `91/372`. The PPT input condition here is at equality; the output is still PPT and exactly SN2 by the preceding proof.

## 6. Scope, read declaration, and process limits

* Before any source-body access or mathematical reasoning, I read the manifest, freeze receipt, final pre-dispatch binding, parent live metadata supply, actual dispatch receipt, and all 22 manifest-listed controls as status/permissions only. The fresh `prebody-ack-v1.md` was written and a direct PREBODY ACK was delivered to Main before any body access. The first f660 control read used an incorrect plural directory name and returned not found; I then read the correct manifest-listed singular path completely. Initial automatically elided administrative displays were recovered with complete raw reads. No held-body mathematical content was used.
* I read the sole literal packet part completely, serially, in raw windows LF `1–20`, `21–40`, and `41–55`, including the ending. The parent-provided part size was 9,872 bytes, so each raw display was below 30,000 bytes; there was no clipped body content to recover. It contains all of S1 logical LF `1–49`. Parent-supplied part SHA-256 is `ef521768b512655d3a60d6c73022517f968b1bc8ab83d19a3057dd8b44b950d1`; S1 SHA-256 is `3f15a273f2c1d64aa1b54ff296c24133fb4c0b7245ec456e484f765f164eccf3`. These are supplied metadata, not hashes independently computed by me. No listed or unlisted source link was followed.
* All genuine held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers are NONINPUT. Generic memory summary and procedural skills were read as instructions, not mathematical premises. No scientific execution, test, solver, compilation, network, external model, child subprocess or child agent was used. No verifier/source code was prepared, hence no code hash. I do not assert clean-cognition certification or independent family review.
* The theorem addresses only the specified `Q`, kernel/filter family and its output, with the explicit parameter conditions above. In particular it does not prove an SN3 detector, all-alpha/all-beta/all-gamma coverage, arbitrary fourth-component filters, all-filter classification, global PPT44 closure, literature novelty, or independent acceptance. Outside the exhibited sufficient regions and the packet's retained certificates, the status remains open here.
