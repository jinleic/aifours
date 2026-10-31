# Original four-qubit k3 for every density when |1−p| <= 1/142

Owner PhysicsDepol4-2, physics-2. Actual native clock before composition: **Thu Oct 29 09:44:13 PDT 2026**.

**HIGH-CONSEQUENCE AUTHOR-WRITTEN CANDIDATE — full-scope disjoint review and parent disposition required.** This is a new theorem candidate, not an adoption of its own proof. It enlarges the all-density radius from the f172-adopted 1/200 to 1/142 by a stronger far-region estimate and a new explicit uniform perturbation budget. It does not solve unrestricted original k3. The R-positivity and one-erasure conjectures in 174/178 are **not premises**.

## 1. Literal theorem and inherited algebra

Let `Phi_p(X)=(1-p)X+(p/2)Tr(X)I`, `Lambda_p=Phi_p^tensor4`, and `R3(t)=a^4+2a^3 b`, `a=(1+t)/2`, `b=(1-t)/2`.

**Candidate theorem.** For every four-qubit density rho, every complex orthogonal rank-three projector Q, and every physical p satisfying

`|1-p|<=1/142`, equivalently `141/142<=p<=143/142`,

`Tr(Q Lambda_p(rho)) <= K3(Lambda_p(rho)) <= R3(|1-p|)`. (A)

This interval is near **complete depolarization**, not near the identity channel.

The load-bearing algebra reused here is the corrected 121 composite:

- `frontier-20261028-121-consolidated-physical-k3.md`, SHA256 `91643ea8965e0e423f2b5010a18e967ddfaeb4c0f78a175ba6509dd9f2e5c36b`, with mandatory errata 125/127/128/130/133 and the parent reflection note;
- its exact common-Q reflection (6), Pauli certificate (14), closest-product gauge (15), raw Hessian blocks (16)–(20), and normalized conjugation identities (22),(25),(26);
- the explicit bridge and weight-share normalization in additive packet 177, SHA256 `a092c605b188cadafa5784eee5ab794524d7fee934f400b7964bde48f4511b70`;
- fresh f172 review, SHA256 `f34242e40d0b649851fbead9981b1e805ecbdd061c6ae31d9b83f86edeaf1b8f`, reconstructing that algebra at the old interval. Its acceptance at 1/200 does **not** itself authorize substitution of 1/142. Every interval-dependent estimate used below is re-established explicitly.

The matrix-unit identities (16)–(20) are algebraic identities for 0<t<1, with the corrected weight-three factor `V_(e_i,1111)=bt^3 conjugate(g_i)`. Their weight-two PSD argument uses t<=1/2. These domains all contain the new interval. No numerical interpolation or old code output is a premise.

## 2. A stronger far-region estimate

For a pure psi, let m be its largest squared overlap with a product vector, eta^2=1-m, and let r_1<=r_2<=r_3<=r_4 be its local Bloch radii. Define

`S=sum r_i^2`, `L=r_1+r_2+3r_3+3r_4`, `delta=8-L`.

The majority-axis product vector and the union bound imply

`eta^2 <= (1/2)sum_i(1-r_i) <= delta/2`. (B)

Write d_i=1-r_i>=0. Since `delta=d_1+d_2+3d_3+3d_4>=sum d_i`,

`S=4-2sum d_i+sum d_i^2 >=4-2delta`.

Consequently the remainder coefficient in 121 Eq.(14) satisfies

`sqrt(39(15-S))-5 <= sqrt(429+78delta)-5`. (C)

This replaces the old universal upper bound 20 by a value below 16 at the tube boundary. Set

`c=1/142`, `r=19/80`, `delta_0=2r^2=361/3200`.

For fixed 0<t<=c define `f_t(d)=d-t(sqrt(429+78d)-5)`. For d>=delta_0,

`f_t(d)-f_t(delta_0)=(d-delta_0)[1-78t/(sqrt(429+78d)+sqrt(429+78delta_0))] >=0`,

because both square roots exceed 20 and `1-39c/20=2801/2840>0`. Moreover

`429+78delta_0 = 441-5121/1600 <441`,

`delta_0-16c=31/227200>0`.

Thus eta>=r implies delta>=delta_0 and

`delta-t(sqrt(39(15-S))-5) >= f_t(delta_0) > delta_0-16c=31/227200`. (D)

The old Pauli certificate (14), valid at all nonnegative t in this domain, therefore proves (A) strictly for every pure input with eta>=r, with the explicit lower gap `31t/3635200`. Neither a local-purity cutoff nor a chosen physical state is substituted for the original all-density quantifier.

## 3. Strengthen the normalized Hessian margin to four

In the closest-product gauge (15), v has norm one and support on excitation weights 2,3,4. Let A,M be the raw second-order blocks (16). Write `A=sum w_h A_h`, `M=sum w_h M_h`, with `w_h=||v_h||^2`, `sum w_h=1`, and normalized nonzero components; the convention is made explicit in 177.

For 0<t<=c:

- Weight two: (17) gives `K2(M_2)<=0` because `K=t Gamma+(1-2t)diag(n)>=0` and `Tr K=2(1-t)`. Also

  `a^2(1-t^2)-1/4 = t(2-2t^2-t^3)/4 >=0`.

  Hence `A_2+K2(M_2)<=-t/4`.
- Weight three: (19) has negative magnitude at least `t(15/32)(1-c)>t/4`, since D3<=1 and its displayed polynomial is at least 15. Exactly `(15/32)(1-c)-1/4=979/4544>0`.
- Weight four: (20) has negative magnitude at least `t(1-2c^6)>t/4` since D4>=1/2. The scalar slack is positive, namely `3074406814103/4099209085472`.

Ky Fan subadditivity therefore gives the uniform all-direction bound

`A+K2(M) <= -t/4`. (E)

This is not obtained by evaluating (17)–(20) at finitely many v. It holds on the entire complex normal sphere. After normalization, `(16/t)(A+K2(M))<=-4`.

## 4. All-variable perturbation budget at the new radius

Use the same normalized map `H_t(X)=[16 Lambda_(1-t)(X)-Tr(X)I]/t`, polynomially extended at t=0. For t>0 write

`H=D+h V_H+eta^2 W_H`, `h=eta sqrt(1-eta^2)`.

The reference gaps satisfy

`d_0-d_1=2(1+t)^3>=2`,

`d_1-d_2=2(1+t)^2(1-t)>=2`,

since `1-t-t^2>0` throughout 0<t<=c. The extreme reference eigenvalues give

`||D||<=4+6c+4c^2+c^3<81/20`.

The same Pauli Parseval argument, now retaining the explicit t dependence, gives

`||V_H||_F^2<=512t^2`, `||W_H-W_0||_F^2<=512t^2`.

Indeed the two traceless input operators have Frobenius norm squared two, the degree-one Pauli part vanishes for V_H, and it is exactly W_0 for W_H. All remaining Pauli weights are at least two. Since

`(4/25)^2-512c^2=656/3150625>0`,

we may take the rational uniform bounds

`v=4/25`, `s=2/25`, `w=204/25`, `b_*=1/25`, `q=41/5`, `o=21/5`.

Here v bounds the two Frobenius quantities, s bounds the anti-Hermitian generator S, and the gap division gives `||S||_F<=||V_H||_F/2<s`. As in 177, put

`B=[V_H,S]+(1/2)[[D,S],S]`, `Qcal=W_H+B`.

Then

`||B||_F <3vs=24/625 <b_*`,

`||W_H|| <8+v=w`,

`||Qcal|| <w+3vs=5124/625<q`,

`||off Qcal|| <4+v+3vs=2624/625<o`. (F)

The last estimate uses the compression of the transverse one-body field of v to excitation weights at most two. It is an actual off-block estimate, not the norm of a separately chosen projector or Hamiltonian.

### Cubic remainder

For eta<=r and h<=eta, `2h||S||<2rs=19/500`, so

`exp(2h||S||)<=1/(1-19/500)=500/481<26/25`.

Three Taylor errors arise from D at order three, h V_H at order two, and eta^2 W_H at order one. With `d=81/20` their total eta^3 coefficient is bounded by

`(26/25)[d(2s)^3/6+v(2s)^2/2+w(2s)] =2661776/1953125 <137/100=:e`.

Hence the exact conjugation satisfies

`exp(-hS)H exp(hS)=D+h V_diag+eta^2 Qcal-eta^4 B+Remainder`,

`||Remainder||<e eta^3`. (G)

The `-eta^4 B` term is retained. There is no division by eta in (G), and no t=0 use of the normalized map is needed.

### Block separations and the leading-block bridge

Let `H_*=D+h V_diag+eta^2 Qcal` and set `g=199/200`. Equations (F) give

`||H_*-D||<r v+r^2 q`.

Both actual separations exceed g because

`2-2(r v+r^2 q)-g=63/16000>0`. (H)

The exact diagonal block identities are `Qcal_00=(16/t)A`, `Qcal_wt1=(16/t)M`. Their complete derivation, including the half-double-commutator and scale c^2/c=c, is in 177 §2. Neither V_H nor S has a within-leading-block contribution. These are algebraic identities; no bound is transferred by just rescaling a review headline.

Apply the PSD block comparison (26) successively to weight zero and weight one, using the same g and the off-block bound o. The normalized leading trace margin (E) yields

`K3(H_*) <= K3(D)-4eta^2 + (3o^2/g)eta^4`.

Restoring the two terms omitted from H_* costs at most `3e eta^3+3b_* eta^4`. The entire adverse coefficient divided by eta^2 is therefore at most

`3e r+3b_* r^2+(3o^2/g)r^2 =126815937/31840000`.

It is strictly below four, with

`4-126815937/31840000 =544063/31840000 >16/2000`. (I)

Thus every pure input with 0<eta<=r and every 0<t<=c obeys

`R3(t)-K3(Lambda_(1-t)(rho)) >= t eta^2/2000`. (J)

Every constant in (E)–(J) is independent of v and Q. The weight-one block may be degenerate. The matrix comparison and Weyl bounds operate on the whole blocks and require no choice of individual eigenvectors within that block.

## 5. Endpoints, mixed inputs and reflected interval

The tube eta<=r and the far region eta>=r cover every pure input and overlap at eta=r. The eta=0 case is a pure product and has the reference output spectrum. At t=0 the channel output is exactly I/16, so every rank-three projector has trace 3/16; none of the normalized formulas is used by division at that endpoint.

For a mixed input fix the same actual complex rank-three Q and average the pure-input bound over a finite spectral decomposition. This proves (A) for `141/142<=p<=1`. The exact identity (6) moves Q to `Y^tensor4 Q^T Y^tensor4` and p to 2-p, preserving rank, the input, and t. It therefore proves (A) also for `1<=p<=143/142` and **no farther** from this theorem. No claim about p=4/3 follows.

## 6. Exact finite arithmetic exercised and verification boundary

The following positive rational slacks were evaluated using fractions.Fraction in the retained Python kernel:

| Constraint | Exact positive slack |
|---|---:|
| v^2−512c^2 | 656/3150625 |
| 81/20−(4+6c+4c^2+c^3) | 108057/14316440 |
| b_*−3vs | 1/625 |
| q−(w+3vs) | 1/625 |
| o−(4+v+3vs) | 1/625 |
| 26/25−1/(1−2rs) | 6/12025 |
| e−the displayed cubic coefficient | 56021/7812500 |
| 2−2(rv+r^2q)−g | 63/16000 |
| residual in (I), minus 16/2000 | 289343/31840000 |
| 2r^2−16c | 31/227200 |
| 441−(429+78delta_0) | 5121/1600 |
| 1−39c/20 | 2801/2840 |

These finite constant checks are not the universal proof. The proof uses the written all-direction Hessian formulas, Parseval estimates, far-region inequalities, and block comparison above. Full fresh review must verify their applicability on the new domain, especially the factor four in (E), the off-block compression in (F), the 121→177 bridge, and the monotonic far bound (D).

No original-k3 result outside this new window or the earlier explicitly supported regional classes is asserted. No R positivity, one-erasure bound, other prefix, full majorization, novelty, formal/kernel or cross-family acceptance follows. Frozen reviewed bytes remain unchanged; the old source-order, cadence and quarantine histories are not repaired by this new proof candidate.
