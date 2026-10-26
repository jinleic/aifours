# Checkpoint 007 — asymmetric W4 domination closes every nonzero charge and the fixed block

Before-creation clock observed: **2026-10-23T14:51:46-07:00**. Owner: physics-1 / PhysicsResearch96h. Status: **CANDIDATE written proof**, pending distinct reconstruction. No scientific program, solver, symbolic engine, finite replay or new GO was used.

## 1. Exact conclusion and remaining obstruction

For `eta_t=Omega_A+t Omega_B`, A={0,1}, B={2,3}, all t>=0, this packet proves in writing:

1. On **all160 nonzero-central-charge dimensions**, `C_B-S_eta>=0` and `3C_B+S_eta>0`. The upper-sign kernel there is exactly the eight reference-input directions with mixed output group.
2. On the **fixed eight-dimensional charge-zero subspace**, `C_B-S_eta>=0` and `3C_B+S_eta>=0`; the latter is strict for t>0. The upper bound uses checkpoint003, with the t=0 extension by continuity.

Thus the sharper asymmetric criterion from checkpoint006 is closed in writing on **168 of256 dimensions for every angle**. The precise residual is the **88-dimensional nonfixed part of central charge zero**, for both asymmetric signs. This does not establish the full asymmetric inequality, full symmetric GS, a whole biseparable W4 class, or unrestricted W4. All new sector closures remain unreviewed CANDIDATES.

The original book connection, exact full64x64 rank<=2 target, prior-source boundaries and novelty uncertainty remain unchanged. The quartic from checkpoint006 characterizes the stronger symmetric fixed plus sign; its failures are not failures of the asymmetric criterion proved here.

## 2. The complete remaining low charge+1 block

The64-dimensional charge+1 space has two group patterns. Checkpoint005 already closed their two higher subspaces, of dimension16 each. The remaining32 dimensions have an external A index alpha and external negative B index beta, with a common eight-vector multiplicity basis. Define, summing a in A and b in B,

`x1=sum_b |alpha,b,b,beta>`,

`x2=sum_b |alpha,beta,b,b>`,

`y1=sum_b |b,b,alpha,beta>`,

`y2=sum_b |b,beta,alpha,b>`,

`u1=sum_a |a,a,alpha,beta>`,

`u2=sum_a |alpha,a,a,beta>`,

`v1=sum_a |a,beta,alpha,a>`,

`v2=sum_a |alpha,beta,a,a>`.

The fixed external pair (alpha,beta) has four possible values. Their sectors are mutually orthogonal. Within each eight-vector basis the Gram matrix is the direct sum of four copies of `[[2,1],[1,2]]`, on the pairs(x1,x2),(y1,y2),(u1,u2),(v1,v2). Its maximum eigenvalue is3, and it is positive definite. Equivariance gives the same eight-dimensional form for each external pair. These vectors exhaust the lower fundamental copies, not just a chosen trial subspace.

Set

`s=t^2`, `a=1+2s`, `b=2+s`, `c=3(1+s)/2`,

`k=1/a`, `l=s/b`, `B2=[[1,2],[2,1]]`, `D2=diag(3,-1)`, `E2=diag(-1,1)`.

In the order(x1,x2,y1,y2 | u1,u2,v1,v2), the C_B form is block diagonal, with both4x4 blocks

`(3/2)[[I2,-I2/2],[-I2/2,I2]]`.

The full S_eta form is `[[S_I,W],[W^T,S_II]]`, where

`S_I=[[B2/(4c),(3l/4)E2],[(3l/4)E2,(3s/(4c))D2]]`,

`S_II=[[(3/(4c))D2,(3k/4)E2],[(3k/4)E2,s B2/(4c)]]`,

and the entire cross block is

`W=[[ -3t/(2b), -3t/(4b), t/c, t/(2c)],`

`   [          0,          0, t/(2c), t/(4c)],`

`   [   9t/(4c),          0, -3t/(2a), 0],`

`   [          0,          0, -3t/(4a), 0]]`.

All entries are quadratic-form entries in the stated nonorthogonal basis. No inverse-Gram action matrix is being mistaken for a form.

### Physical derivation of the table

The full reference-inverse rank-one correction is supported only in charge zero, as proved in checkpoint005. Therefore using D^-1 on the present nonzero-charge sector is an exact cancellation, not a truncation of A_eta^-1. The retained D^-1 still has its a,b,c group values and all eta terms.

For any labels r,s,u,v, the exact raw vector is

`L_rs†|uv>=delta_(rs)c_r|uv>-(c_s/2)delta_(ru)|sv>-(c_r/2)delta_(sv)|ur>+(1/4)delta_(ru)delta_(sv)eta`.

The reversed bilinear is `<L_(column input)†(row output),D^-1 L_(row input)†(column output)>`, summed over the internal labels in the displayed vectors. Checkpoint005's operators I,T,P1,K12,K21 give S_I upon multiplying by the two-contraction Gram matrix. Group/physical-factor interchange gives S_II.

For independent reconstructions of representative new cross entries:

- x1,v1: each of the four(a,b) contractions is `t/(4c)`, giving t/c.
- x1,u2: only a=alpha remains; the two BB terms and the eta term sum to `-t/b+t/(4b)=-3t/(4b)`.
- y1,u1: the two contraction sums each contribute `1+1/2`, giving `9t/(4c)`.
- x2,u1: the BB diagonal sum is `-t/(2b)+2t/(4b)=0`, and the a sum preserves zero.
- y1,u2 and y2,u2 contain respectively the zero sums `sum_a(delta_(a,alpha)-1/2)=0` and the product of that sum with its B analogue.

The same raw formula specifies all16 cross entries above, including their signs. The persistent kernel gives a further exact identity across both patterns:

`K=u1+t y1=eta_input tensor |alpha,beta>_output`,

`(C_B-S_eta)K=0`.

For example, the x1 row reads `-3t/(2b)+t*(-3l/4)=-3t/4`, and the v1 row reads `-3k/4+t*(-3t/(2a))=-3/4`, precisely the respective C_B entries. The table retains these exact reference couplings.

## 3. Full upper bound on the low charge-one block

Because K has coefficient1 on u1, `(K,x1,x2,y1,y2,u2,v1,v2)` is an invertible basis change even at t=0. The minus form has an exact zero K block, with all cross entries zero by Hermiticity. It remains to prove strict positivity on the seven displayed remaining vectors.

The y1 pivot equals `9/(4c)>0` and connects only to x1 and v1, with entries `-3/(2b)` and `3t/(2a)`. Eliminate it. Then eliminate the positive y2,u2 pivots

`d_y=(3+4s)/[2(1+s)]`, `d_u=(4+3s)/[2(1+s)]`.

The final4x4 form, in order(x1,x2,v1,v2), has diagonals

`delta1=3/2-1/[6(1+s)]-3(1+s)(16+15s)/[8 b^2(4+3s)]`,

`delta2=3/2-1/[6(1+s)]-9(1+s)^3/[2 b^2(3+4s)]`,

`delta3=3/2-s/[6(1+s)]-3s(1+s)(15+16s)/[8 a^2(3+4s)]`,

`delta4=3/2-s/[6(1+s)]-9(1+s)^3/[2 a^2(4+3s)]`.

Its six off-diagonal entries are

`h12=-1/(2c)`, `h34=-s/(2c)`, `h24=-t/(4c)`,

`h13=t(s-1)^2/[4cab]`,

`h14=t[-1/(2c)+c^2/(ab(4+3s))]`,

`h23=t[-1/(2c)+c^2/(ab(3+4s))]`.

For example, the h13 identity uses `c^2-ab=(s-1)^2/4`; the y1 elimination changes `-t/c` into that nonnegative expression. Thus the small cross signs are not guessed from a numerical matrix.

### Diagonal lower bounds by positive polynomial numerators

For all s>=0, delta1>1/2. Multiplying delta1-1/2 by its positive denominator `24(1+s)b^2(4+3s)` gives

`176+521s+578s^2+309s^3+72s^4>0`.

The reciprocal identity `delta3(s)=delta1(1/s)` gives delta3>1/2 for s>0, and the t=0 limit is positive too.

For all s>=0, delta2>1/3. Multiplying delta2-1/3 by `6(1+s)b^2(3+4s)` gives

`45+144s+148s^2+49s^3+s^4>0`.

Consequently delta4>1/3 by `delta4(s)=delta2(1/s)` and continuity at0. On the smaller range0<=s<=1 we have the stronger delta2>1/2: the numerator for that comparison is

`33+104s+101s^2+26s^3-3s^4`

`>=33+104s+101s^2+23s^3>0`.

### Small cross bounds and strict diagonal dominance

Since `ab>=2(s-1)^2`,

`|h13|<=t/[12(1+s)]<=1/24`.

For h14,h23 their numerators over the common positive form `12(1+s)ab(4+3s)` or `12(1+s)ab(3+4s)` are respectively

`t*(-5-23s-11s^2+3s^3)`,

`t*(3-11s-23s^2-5s^3)`.

The absolute coefficient bounds are dominated termwise by

`ab(4+3s)=8+26s+23s^2+6s^3`,

`ab(3+4s)=6+23s+26s^2+8s^3`.

Hence both absolute entries are at most `t/[12(1+s)]<=1/24`.

For0<=s<=1, the other entries satisfy `|h12|<=1/3`, `|h34|<=1/6`, `|h24|<=1/12`. The row off-diagonal sums are therefore at most

`5/12`, `11/24`, `1/4`, `7/24`.

The respective diagonal bounds are `1/2,1/2,1/2,1/3`. All four differences are strictly positive, at least `1/12,1/24,1/4,1/24`. The elementary inequality `2|z_i z_j|<=|z_i|^2+|z_j|^2` proves positivity also for arbitrary complex coefficients; no real-vector restriction is imposed.

This proves strict positivity of the full seven-vector remainder on0<=s<=1. Group interchange followed by physical-factor interchange maps the full block at t to the block at1/t, with only a nonzero scalar change in the reference. S_eta is invariant under that scalar change. Therefore the same conclusion holds for every finite t>=0. Its exact minus kernel is just K for each external pair.

Physical-factor interchange supplies charge-1. With checkpoint005's strictly positive higher subspaces, the entire128-dimensional charge±1 upper bound is now closed, with precisely four reference kernels per charge. Checkpoint004 supplies the other32 nonzero-charge dimensions and has no kernel.

## 4. Strict lower bound3C_B+S_eta on the same low block

The same raw8x8 table gives a much shorter proof of the asymmetric lower bound. It suffices again to take0<=s<=1 and use reciprocity. The following parameter bounds are elementary:

`k>=1/3`, `l<=1/3`, `t/b<=1/3`, `t/c<=1/3`,

`1/(2c)<=1/3`, `s/(2c)<=1/6`, `t/(4c)<=1/12`,

`t/a<=16/45`.

The last bound follows from `16a-45t=32t^2-45t+16>0`, whose discriminant is-23. It avoids a floating-point square-root bound.

For the form of3C_B+S_eta, these yield the following full row estimates in the eight-vector basis:

| Row | Diagonal lower bound | Sum of absolute off-diagonal entries, upper bound |
|---|---|---|
| x1 | 9/2 | 49/12 |
| x2 | 9/2 | 17/6 |
| y1 | 9/2 | 227/60 |
| y2 | 17/4 | 151/60 |
| u1 | 9/2 | 17/4 |
| u2 | 4 | 9/4 |
| v1 | 9/2 | 67/15 |
| v2 | 9/2 | 29/12 |

For the tightest v1 row, group its y1/y2 couplings together: their sum is `9t/(4a)<=4/5`. The remaining bounds are3 from u1 and2/3 from v2,x1,x2. Thus its total is67/15 and its margin is exactly1/30. Every other row has a larger positive margin.

Diagonal dominance therefore gives the coefficient form at least `I/30`. The basis Gram matrix is at most3I, so this is the physical operator bound

**`3C_B+S_eta >= I/90`**

on all64 low charge±1 dimensions, uniformly in t>=0. No basis-conditioning gap is hidden in this conversion. Reciprocity is unitary and permutes these contraction bases, so the constant is unchanged for t>1.

On the higher charge±1 dimensions, checkpoint005 gives `C_B+S_eta>=I/4`; adding2C_B and using `C_B>=I/4` gives the strict lower bound3I/4 for3C_B+S_eta. On the extremal charges, checkpoint004 likewise gives at least5I/8. This closes the asymmetric lower bound on **all160 nonzero-charge dimensions**.

## 5. The fixed eight-dimensional asymmetric lower bound for every angle

This section uses the exact fixed-space matrices of checkpoint006, not its quartic sign conclusion. Work first with t>0. Put `p=kl`, `L=k+l`, `g=-2t/(1+s)`, and retain its2x2 blocks T,E,J and its matrix R after eliminating T.

For3C_B+S_eta, eliminate the positive reference block4K2 and the positive z_minus scalar. In the same basis `(p_A,p_B,V_A,V_B,z)`, the resulting5x5 form has blocks

`[[T3,E,-4g*1],[E,J+(9/2)I,g*1],[-4g*1^T,g*1^T,14+3L]]`,

where

`T3=[[28l+38p,10p],[10p,28k+38p]]/[3(1-p)]`.

This follows directly from `(lambda+1)C_B-(C_B-S_eta)` with lambda=3: V_A,V_B have zero C pairing with the reference vectors, C(V,V)=9I/4, and the reference Schur term has coefficient4 rather than2. In particular the changed p-z entry is-4g.

Both T3 and T3-T are positive definite. Explicitly,

`det T3=616p/[3(1-p)]`,

`T3-T=(3/(1-p))[[2l+3p,p],[p,2k+3p]]`,

whose unscaled determinant is `10p(1-p)>0`. Hence `T3^-1<=T^-1`.

After eliminating T3, the V block R3 consequently satisfies

`R3=J+(9/2)I-E^T T3^-1 E >= R+(9/2)I`.

Checkpoint006 gives the diagonal f(k),f(l) of R. For0<=x<=1,

`f(x)+1/2`

`=(1-x)[231+387x+513x^2-171x^3]/[70(1+x)^2]>=0`.

Its off-diagonal absolute value is `6p(5+39p)/[35(1-p)]<=1/5`, because this positive expression increases up to p=1/9. Therefore `R>=-(7/10)I`, and

`R3>=(19/5)I`.

The remaining z pivot and its V coupling admit particularly short exact identities. Direct inversion gives

`T3^-1=(1/308)[[14/l+19,-5],[-5,14/k+19]]`,

`1^T T3^-1 1=(1-p)/(22p)`,

`E^T T3^-1 1=((3k-1)/11,(3l-1)/11)^T`.

Thus after the T3 elimination,

`Z3=14+3L-16g^2*1^T T3^-1 1=90/11+3L>=112/11`,

`q3=(g/11)(7+12k,7+12l)^T`.

Because `g^2<=1`, `k+l<=1`, and `k^2+l^2<=1`,

`||q3||^2<=(98+168+144)/121=410/121`.

The final Schur complement is bounded below by

`R3-q3 q3^T/Z3`

`>=[19/5-205/616]I=(10679/3080)I>0`.

All eliminated blocks are positive; the z_minus scalar equals `18-2h>=15` with h=3L/2. Hence3C_B+S_eta is strictly positive on the full fixed eight for t>0. Continuity of the physical matrix, whose reference inverse exists also at t=0, gives the stated nonnegative endpoint without making a singular basis change at0. No stronger endpoint kernel/equality assertion is needed here.

Combining this with checkpoint003's upper bound closes both asymmetric signs on those eight dimensions for all t>=0.

## 6. Exact next residual, without an auxiliary/physical conflation

The charge dimensions are16,64,96,64,16. This packet closes both asymmetric signs on the160 nonzero-charge dimensions and the fixed8 inside charge zero. The remaining **88** charge-zero dimensions decompose into nontrivial U(2)xU(2) representations and still require physical raw-block derivation and positivity. The persistent reference kernel predicts six further charge-zero nonfixed kernel directions, but that prediction is not used as a positivity proof.

If those88 dimensions also satisfy the two asymmetric inequalities, checkpoint006's one-site spectrum argument will supply a genuine W4 reference-ray theorem for the entire two-equal-pairs family, including angles where symmetric GS fails. Until then no such global theorem is claimed. This continues one W4 problem, not an additional slot or a collection of independently accepted discoveries.
