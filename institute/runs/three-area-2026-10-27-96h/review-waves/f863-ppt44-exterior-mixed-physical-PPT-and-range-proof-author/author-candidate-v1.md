# Author candidate: physical PPT, universal product-range obstruction, and an explicit mixed exterior

**Status and scope.** This is a fresh written GENERAL AUTHOR reconstruction of the displayed objects in the frozen packet, not a parent disposition, independent-family, human, formal/kernel, or novelty acceptance. It proves the physical PPT and entanglement statements for *every* finite complex three-coordinate filter below, and exact Schmidt number 2 in the explicit sufficient residual/scalar regions. It constructs nonempty strict mixed exterior points for every admissible source pair, including separately a `q=1` point with three nonzero coordinates and arbitrary phases. It does not assert that every such filter has Schmidt number 2, any SN3 detector conclusion, arbitrary fourth filter coordinate, or a global PPT44 result.

## 1. Objects and quantified conclusions

Write `ij=|i>_A tensor |j>_B` and `[v]=v v†`. Let `s,r` be real with

    s>1,  r>1,  (s−1)(r−1)>=4.                                  (1)

On `C^4 tensor C^5`, let

    A=00+11+22,   B=01+12,   D=10−21,
    Q=[A]+[B]+[D]+s([02+34]+[32]+[04])
                       +r([20+33]+[23]+[30]).                    (2)

For arbitrary finite `alpha,beta,gamma` in `C`, put `w=(alpha,beta,gamma,0)^T`, `K=[I_4 | w]`, and

    F=02+3w,  H=0w,  G=32,  P=30,  J=20+33,
    R=(I tensor K)Q(I tensor K)†
     =[A]+[B]+[D]+s[F]+s[H]+s[G]+r[P]+r[J]+r[23].              (3)

Here `3w=alpha 30+beta 31+gamma 32` and `0w=alpha 00+beta 01+gamma 02`; these are ket coefficients, not their conjugates. Put

    n=|alpha|²+|beta|²+|gamma|²,
    T=7+4(s+r),             Z=7+2s(1+n)+4r.                     (4)

Then `Q/T` is a state, `K/sqrt(1+n)` is a physical Bob Kraus contraction, the success probability is `p=Z/((1+n)T)` with `0<p<1`, and the conditional state is `R/Z`. For *all* finite `alpha,beta,gamma`, this state is PPT, has both local marginal ranks equal to 4, and is entangled, hence has Schmidt number at least 2. No nonzero-filter-coordinate condition is used for these facts.

For the SN2 upper bound additionally suppose `beta != 0`. Let `a=|alpha|²`, `x=|gamma|²`, `y=|beta|²`, and

    q=x/s+a/(r+s)
      + { [1+x+x²+a(1+x)]/s + a(x+a)/r }/y.                    (5)

Every `q<=1`, including equality, gives exact SN2 via the actual positive decomposition in section 4. More generally the explicitly defined `M>=0` condition there also suffices; `q<=1` is only a sufficient scalar test, not asserted necessary for this `M`, for SN2, or for physical PPT. The construction dividing by `beta` says nothing about the SN2 upper bound at `beta=0`; the universal PPT, full-support, and lower-bound statements remain valid there, including `w=0`.

## 2. Actual partial transpose, signs, and physical normalization

Take partial transpose on Bob in the computational basis. Direct expansion of (2) yields the following orthogonal direct sum on all 20 basis vectors:

* scalar blocks `1,1,s,r` on `00,22,34,33`, respectively;
* `[[1,1],[1,1]]` on `(01,10)` and `(12,21)`;
* `s[[1,1],[1,1]]` on `(04,32)` and `r[[1,1],[1,1]]` on `(23,30)`;
* on `(11,02,20)`, in this order,

          N = [[1,  1, −1],
               [1,  s,  1],
               [−1, 1,  r]];                                     (6)

* zero on `03,13,14,24,31`.

For example, the `11,02` entry `+1` comes from `[01+12]`, the `11,20` entry `−1` comes from `[10−21]`, and the `02,20` entry `+1` comes from `[00+11+22]`. Likewise `[02+34]` and `[20+33]` generate the positive off-diagonal entries in the `(04,32)` and `(23,30)` blocks. This accounts for every basis vector and fixes the signs rather than importing a block claim.

The Schur complement of the first entry of `N` is

    [[s−1, 2], [2, r−1]].                                        (7)

It is PSD under (1), including `(s−1)(r−1)=4`; all other displayed blocks are PSD. Conversely, for real `s,r>0`, `N>=0` forces `s−1>=0`, `r−1>=0` and their product at least 4, hence actually `s,r>1`: thus (1) is exactly the PPT condition for this *input Q* within that positive-parameter domain. No necessity statement for the filtered output outside (1) follows.

For arbitrary complex `K`, the actual output partial transpose is

    R^Gamma_B=(I tensor conjugate(K)) Q^Gamma_B
                       (I tensor conjugate(K))† >= 0.             (8)

This follows term-by-term from `(K X K†)^T=conjugate(K) X^T K^T`; replacing `conjugate(K)` by `K` is generally incorrect. Positivity of `R` itself follows from (3), independently of the transpose argument.

The norms of the input summands give `tr Q=3+2+2+4s+4r=T`. In (3), `||F||²=1+n`, `||H||²=n`, `||G||²=||P||²=||23||²=1`, and `||J||²=2`, giving `tr R=Z`. Since `K K†=I_4+w w†`, its largest eigenvalue is `1+n` even when `w=0`; hence the stated scaling makes `K†K/(1+n)<=I_5`. The success probability is strictly between zero and one because

    (1+n)T−Z=2s+(7+2s+4r)n>0.                                  (9)

For the local supports, the reduced operators contributed by `[A]` are `diag(1,1,1,0)` on each side. Those from `r[J]` are `r diag(0,0,1,1)` on Alice and `r diag(1,0,0,1)` on Bob. All other summands are positive; thus each unnormalized marginal dominates a positive definite diagonal matrix. Both have rank 4, including at `w=0`; division by `Z>0` does not change ranks.

## 3. Universal actual-range product obstruction

Since all coefficients in (3) are strictly positive and the summands are rank-one PSD, `range R` is exactly the span of the nine displayed kets. Every vector in that range has an actual coefficient matrix, in row/column order 0,1,2,3, of the form

    [[a0+alpha h, b+beta h, c+gamma h, 0],
     [d,          a0,       b,         0],
     [e,         −d,        a0,        k],
     [f+alpha c,  beta c,   g+gamma c, e]],                       (10)

for complex `a0,b,c,d,e,f,g,h,k`. This parametrization remains valid if columns of the spanning family happen to be dependent; in particular its `(1,1)` entry is always `a0`.

A nonzero product vector has matrix rank one, so all its `2 x 2` minors vanish. In zero-based row/column notation the minors on `(1,2;1,2)`, `(1,2;0,2)`, and `(1,3;1,3)` are respectively

    m1=a0²+bd,      m2=a0 d−be,      m3=a0 e,
    a0² m1−a0 b m2−b² m3 = a0^4.                                 (11)

The identity is a polynomial identity over `C`, with no conjugation or nonzero-parameter assumption. Thus every product vector in `range R` has `a0=0` and vanishing physical `11` coefficient. On the other hand `R_(11,11)=1`, supplied by `[A]`, for every finite `w`.

Indeed, if `R` had a positive separable decomposition, each product ket in it would lie in `range R`: for every `u in ker R`, positivity of each summand and `<u,Ru>=0` force `u` orthogonal to each summand vector. Equation (11) would make every product ket's `11` coefficient zero, contrary to `R_(11,11)=1`. Thus `R/Z` is entangled and has SN>=2 throughout the physical family. This range argument does not prove SN3.

## 4. Independent upper decomposition with complex coefficients

Define `kappa=r/(r+s)`, `eta=s/(r+s)`; then `kappa+eta=1`. For `beta!=0`, set

    X1=(H−gamma F+gamma² G+alpha gamma P)/beta,
    X2=gamma G+kappa alpha P,
    X3=alpha(F−gamma G−alpha P)/beta,
    X4=−eta alpha G.                                             (12)

The actual ket cancellations are

    X1=(alpha/beta)00+01−gamma 31,
    X3=(alpha/beta)02+alpha 31.                                   (13)

For each sixth root `z` of unity let

    V_z=A+z D+z^(−1)X1+z^(−2)X2+z^(−3)X3+z^(−4)X4.           (14)

Its actual coefficient rows are

    (1+(alpha/beta)z^−1, z^−1, (alpha/beta)z^−3, 0),
    (z,                    1,    0,                0),
    (0,                   −z,    1,                0),
    (kappa alpha z^−2, alpha z^−3−gamma z^−1,
                         gamma z^−2−eta alpha z^−4, 0).

The first row is `(z^−1+(alpha/beta)z^−2)` times the second plus `(alpha/beta)z^−3` times the third. The fourth is `kappa alpha z^−3` times the second plus `(gamma z^−2−eta alpha z^−4)` times the third. Hence every `V_z` has Schmidt rank at most 2 for all complex phases. The exponents `0,1,−1,−2,−3,−4` are distinct mod 6, so exact character orthogonality, not numerical sampling, gives

    (1/6) sum_(z^6=1) [V_z]=[A]+[D]+sum_(j=1)^4 [Xj].         (15)

Let `C:C^4 -> C^4 tensor C^4` have columns `(F,H,G,P)`, define `Lambda=diag(s,s,s,r)`, and take the complex coordinate columns

    t1=(-gamma,1,gamma²,alpha gamma)^T/beta,
    t2=(0,0,gamma,kappa alpha)^T,
    t3=(alpha/beta)(1,0,−gamma,−alpha)^T,
    t4=(0,0,−eta alpha,0)^T,
    M=Lambda−sum_j t_j t_j†.                                     (16)

The dagger is essential; no ket coefficient in (12) or (16) is replaced with its conjugate. Since `Xj=C t_j`, direct substitution into (3) and (15) gives the actual-operator identity

    R=(1/6)sum_(z^6=1)[V_z]+[B]+r[J]+r[23]+C M C†.              (17)

If `M>=0`, its Hermitian square root gives `C M C†=sum_(i=1)^4 [C M^(1/2)e_i]`. Each of these kets is supported on Alice rows 0 and 3, so has Schmidt rank at most 2. The kets `B,J,23` have ranks 2,2,1. Thus (17) is a finite positive rank-at-most-2 decomposition even when `M` is singular, and together with section 3 proves exact SN2.

Writing `W` for the matrix with columns `Lambda^(−1/2)t_j`, the explicit exact residual criterion is

    M>=0  iff  I−W W†>=0  iff  I−W† W>=0.                        (18)

The second equivalence follows because `W W†` and `W† W` have the same nonzero eigenvalues, including multiplicity. Direct squared-norm expansion yields

    sum_j ||Lambda^(−1/2)t_j||²=q,
    kappa²/r+eta²/s=1/(r+s).                                     (19)

For every `v in C^4`, weighted Cauchy–Schwarz gives

    v† M v >= (1−q) v† Lambda v.                                  (20)

Therefore `q<=1` suffices, including `q=1`; no limit, numerical detector or negative-residual argument is used.

A boundary check independent of the scalar estimate: if `alpha=0`, `0<=x<s` and `y>0`, then `t3=t4=0` and `Lambda−t2 t2†=diag(s,s,s−x,r)>0`. The rank-one criterion applied to `t1` gives `M>=0` exactly when

    y >= (1+x)/s + x²/(s−x).                                    (21)

This includes `x=0` and equality. For `x>=s` the `G,G` diagonal of this particular `M` is `s−x−x²/y<0`; this rules out only this residual, not another decomposition or SN2. The beta-zero locus is not covered by (12)–(21).

## 5. A nonempty open mixed exterior for every source pair, and its q=1 boundary

Fix *any* `s,r` satisfying (1). For any complex `alpha` with `a<r+s`, choose any nonzero complex `gamma` satisfying

    delta := x/s+a/(r+s) < 1.                                    (22)

Such a choice exists because one may take `0<x<s(1−a/(r+s))`. Let

    D0=[1+x+x²+a(1+x)]/s+a(x+a)/r > 0.

For any `beta` of arbitrary phase and finite squared modulus

    y > max{ D0/(1−delta), s[1−x/(s−1)], 0 },                  (23)

we have `q=delta+D0/y<1`, `beta gamma!=0`, and

    y/s+x/(s−1)>1.                                               (24)

Thus these actual states lie outside the ellipsoid named in frozen source S2 and, because `beta` and `gamma` are both nonzero, outside both its stated coordinate lines. Their SN is exactly 2 by (17) and section 3. For each fixed source pair the strict inequalities and nonzero conditions define a nonempty open subset of `C^3`; they also define a relatively open set over the admissible `(s,r)` domain. Alpha may be chosen nonzero, and no phase is restricted.

The scalar boundary is not omitted. A fully explicit `q=1` strict-exterior witness exists for **every** pair (1): choose moduli

    x=s/2,        a=(r+s)/4,        y=4 D0,                      (25)

where `D0` is evaluated at these `a,x`, and choose arbitrary phases for all three nonzero coordinates. Then `delta=1/2+1/4=3/4` and `q=3/4+D0/(4D0)=1`. To see exterior strictness without a numerical detector, put `Dbase=(1+x+x²)/s`. Since `a>0`, `D0>Dbase`, hence `y=4D0>2Dbase`; at `x=s/2`, the smaller choice `2Dbase=2/s+1+s/2` already gives

    (2Dbase)/s+x/(s−1)
       =1+1/[2(s−1)]+1/s+2/s² > 1.                              (26)

Thus (25) lies strictly outside the old ellipsoid and both coordinate lines, with all three coordinates nonzero. Increasing `y` strictly while retaining the phases gives `q<1`; by continuity there is an open mixed neighborhood. The `q=1` point itself is a boundary witness for the scalar certificate, not a claim that the equality hypersurface is open in `C^3`.

## 6. Concrete actual member by written identities

Take `s=r=3`, `(alpha,beta,gamma)=(1,3,1)`. The source Schur complement is `[[2,2],[2,2]]>=0`, so source PPT holds on the equality boundary. Here `a=x=1`, `y=9`, and

    q=1/3+1/6+(7/3)/9=41/54<1,
    y/s+x/(s−1)=3+1/2=7/2>1.                                   (27)

The actual columns (16) and `Lambda` are

    t1=(-1,1,1,1)^T/3,      t2=(0,0,1,1/2)^T,
    t3=(1,0,−1,−1)^T/3,     t4=(0,0,−1/2,0)^T,
    Lambda=3 I_4.

Their total squared norm is `4/9+5/4+1/3+1/4=41/18`; consequently (20) gives `M >= (13/18) I_4`. Formula (17), with these actual kets and the positive square root of this `M`, is an explicit exact positive SN<=2 decomposition; section 3 gives SN>=2. All three filter coordinates are nonzero, so the member is also outside both coordinate lines.

Here `n=11`, `T=31`, `Z=91`; the physical Kraus operator is `K/sqrt(12)` and its exact success probability is `91/372`. As an additional actual-object identity, the unnormalized Alice and Bob marginals, respectively, are

    [[38,0,0,3],              [[14,18, 6,0],
     [0,3,0,0],                [18,57,18,0],
     [0,0,8,0],                [ 6,18,14,0],
     [3,0,0,42]],              [ 0, 0, 0,6]],                    (28)

both with trace 91; divide each by 91 for the normalized state. Their full rank also follows from the general positive diagonal lower bounds in section 2, so no numerical eigenvalue calculation is needed.

## 7. Import boundary, reading, and process declaration

* The two complete mathematical inputs were read only as the single literal packet part in order, with raw windows LF `1–20, 21–40, 41–60, 61–80, 81–100, 101–120, 121–140, 141–160, 161–180, 181–200, 201–220, 221–240, 241–250`, including its ending. These contain complete S1 LF 1–191 and S2 LF 1–49. The parent-supplied packet size is 25,182 bytes, below 30,000 bytes even for the entire part, so each window was below that limit. No packet-body output was clipped; no clipping recovery was necessary. No source link was followed.
* Parent-supplied SHA-256 pins, not independently recomputed here: packet `113313a395f04d445919344cebf5da0ef74e7005bef656445a5bcd1d514f6101`; S1 `c5843b30d17031648d961d78c3da96f5c8fbf4509cdc7b8ca58bf9b97db4d352`; S2 `3f15a273f2c1d64aa1b54ff296c24133fb4c0b7245ec456e484f765f164eccf3`. The parent metadata's match assertions are administrative, not my independent hash, mathematical, or provenance certification.
* Before any packet-body read or mathematical reasoning I read the complete manifest, freeze receipt, final binding, parent live metadata, actual dispatch receipt, and all 22 listed status controls; wrote the previously absent local `prebody-ack-v1.md`; and sent the direct PREBODY ACK to Main. Initial administrative structured displays elided entries, so I recovered each entire administrative file using raw reads before the ACK. Controls were used only for permissions/status, never as mathematical inputs. Generic memory and procedural skills were also read as instructions, not premises.
* All genuinely held episodes and all their proof/method/selection/planning/verification/reporting/confidence/downstream consumers remained NONINPUT. No unlisted body, network, external model, scientific code execution, test, solver, compilation, child subprocess, child agent, or verifier source was used; hence there is no prepared code hash. No claim of private-cognition certification is made.
* The statement that the original `4 x 5` parent has SN3 appears in S2 but its prior underlying linked proof/source body is not in the packet and was not opened. It is a **named conditional import** if one describes these outputs as an SN3-to-SN2 physical transition; this candidate does not independently prove parent SN3. Nothing here asserts literature priority, unrestricted all-filter coverage, original-target closure, or family/human/formal acceptance. Parent disposition and independent review remain separate.
