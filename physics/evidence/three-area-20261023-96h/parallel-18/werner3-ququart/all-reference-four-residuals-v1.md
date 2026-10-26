# Four exact remaining matrix families for the all-reference route

Before-writing clock observed: `2026-10-23T19:29:06-07:00` (`/bin/date -Iseconds`).

Status: **CANDIDATE / UNREVIEWED complete reduction specification**, not a solution of the four matrix inequalities, not a complete all-reference proof, and not unrestricted W4. No scientific program, numerical evaluation, import, compilation, solver, model CLI, or proof assistant was used.

This packet gives explicit fixed-size definitions of all four still-unproved forms. There are no unspecified cross blocks, numerical pseudoinverses, or hidden restricted reference classes. The preceding hand closures remain subject to actual independent reconstruction.

## 1. Exact candidate reduction statement

Let `Lambda(X)=Tr(X)I-X/2` on `M4`, `B=Lambda tensor Lambda`,

```
A_eta=B(|eta><eta|),
L_i=B(|i><eta|),
M_eta(E_ij)=L_i A_eta^(-1)L_j^dagger,
C_B=Jhat(B), S_eta=Jhat(M_eta),
Jhat(E)=sum_ij E_ji tensor E(E_ij).
```

The technical target is **both** `C_B-S_eta>=0` and `3C_B+S_eta>=0` for every nonzero eta in `C4 tensor C4`.

Scaling eta by a nonzero scalar does not change M_eta. Local-unitary covariance of B permits `eta=sum_i c_i|ii>` with `c_i>=0`, `sum_i c_i^2=1`. Indeed conjugating the reference by `W=U tensor V` conjugates the reversed-input co-Choi matrices by `W tensor W`; the fixed C_B has the same covariance. Thus no complex reference or test-vector quantifier is dropped.

**Candidate reduction:** using the complete sector profile and hand closures cited in Section 6, the technical target is equivalent to

```
F_up(c)>=0, F_low(c)>=0,
Z_up(c)>=0, Z_low(c)>=0                     (R1)
```

for every **strictly positive** normalized c, where the first two matrices have size four and the last two size six, and are explicitly defined below. Positivity of the entire physical matrices then extends to zero amplitudes by continuity. In particular, no boundary-singular upper-p inverse is part of the boundary assertion. Conversely the technical target implies these Schur signs wherever the stated interior pivots are positive.

This is an equivalence for the **sufficient co-Choi route**, not an equivalence with W4. Even success of all four would only establish the biseparable-reference range/co-range class supplied by that route. A negative value of one residual would disprove the route, not automatically give a rank-two Werner witness.

## 2. Common scalar quantities

Write

```
x_i=c_i^2, d_i=1-x_i,
d_ij=1-(x_i+x_j)/2,
W=1+2e2(x)-e3(x)=e3(d)>0.
```

For any distinct i,j, let `{k,l}` be its complementary pair and set

```
E_ij=[2+(x_i+x_j)(x_k+x_l)]/(4W)-1/4,
K_ij=c_i c_j/(4d_ij).
```

All are regular on the closed normalized reference simplex. Matrix transposes below are ordinary transposes in the real Schmidt coordinate basis; the PSD inequalities are Hermitian inequalities over complex vectors.

## 3. Both nonzero-charge four-dimensional forms

By label permutations it is enough to fix one ordered charged pair `a!=b`, with spectators `{j,k}`. The physical basis is

```
Q_i=|i,i,a,b>, P_i=|a,b,i,i>, i=1,...,4,
R_l=|a,l,l,b>, T_l=|l,b,a,l>, l=j,k.
```

The rest-coordinate order is `P1,P2,P3,P4,Rj,Rk,Tj,Tk`. Define

```
tau_i=1-(delta_ia+delta_ib)/2,
Tau=diag(tau_i), f=Tau c, d=d_ab=c^T Tau c,
sigma_i=1-2delta_ia-2delta_ib,
v=c_b e_a+c_a e_b,
T=x_a+x_b, m=x_a x_b, n=x_j x_k,
beta=(1-2T+m-n)/(4W).
```

The four regular kappa scalars are

```
kappa_a=-d_b(d_j+d_k)/(2W),
kappa_b=-d_a(d_j+d_k)/(2W),
kappa_j= d_k(d_a+d_b)/(2W),
kappa_k= d_j(d_a+d_b)/(2W).
```

For a pair u,v let `Tau^(uv)=diag(1-(delta_iu+delta_iv)/2)`.

### 3.1 The raw rest matrices, fully specified

Their C blocks are

```
Crest_PP=Tau,
Crest_P,Rl=Crest_P,Tl=-e_l/2,
Crest_RT=[[I2,I2/4],[I2/4,I2]].
```

Their S blocks are

```
Srest_PP=v v^T/(4d),
Srest_P,Rl=[c_a c_l e_a+x_a e_l]/(4d_al),
Srest_P,Tl=[c_b c_l e_b+x_b e_l]/(4d_bl),
Srest_RT=[[0,B2],[B2,0]],
B2=[[beta,K_jk],[K_jk,beta]].
```

Symmetric counterparts are included, and no other entries occur.

### 3.2 Exact Q-cross matrices and the fixed inverse-pairing rule

Let G be the 4-by-8 upper Q-cross matrix with columns

```
G_Pi=kappa_i(e_i-c_i c),
G_Rl=-e_l/2+c_l Tau^(lb)c/(2d_lb),
G_Tl=-e_l/2+c_l Tau^(al)c/(2d_al).
```

Let gC be the 4-by-8 C-cross matrix **after its reference correction**, with columns

```
(gC)_Pi=(sigma_i/4)(e_i-c_i f/d),
(gC)_Rl=(gC)_Tl=-e_l/2+c_l f/(2d).
```

Every column is orthogonal to c. The actual Q-complement pivot is

```
Q0=Tau-f f^T/d,
```

with kernel c and `Q0>=I/2` on `c^perp`. On orthogonal-to-c columns g,h its inverse pairing is exactly

```
g^*Q0^+h=g^*Tau^(-1)h.                      (R2)
```

Indeed `Tau^(-1)h+constant*c` solves `Q0 q=h`; the constant disappears against g. Thus no numerical pseudoinverse or square-root basis is required.

### 3.3 The actual upper and lower eight-dimensional forms

Define

```
D8=Crest-Srest-G^T Tau^(-1)G.
```

This is the upper form after removing its reference kernel and eliminating the Q complement.

The fixed Schur matrix of C after eliminating **all Q4** is C0, specified by

```
C0_PP=diag(3/8 on a,b; 15/16 on j,k),
C0_P,Rl=C0_P,Tl=-(3/8)e_l,
C0_RT=(3/4)I4.
```

Put

```
H=G-gC,
L8=4C0-D8-(4/3)H^T Tau^(-1)H.              (R3)
```

This is exactly the lower form after eliminating the true positive reference block `4d` and its Q-complement pivot `3Q0`. Formula (R3) is obtained by expanding the lower cross `4gC-G`, not by deleting a reference direction.

Partition D8 and L8 into `P4 | RT4`. The prior hand proofs give

```
R_up=(D8)_RT,RT>=I/18,
R_low=(L8)_RT,RT>=73I/72.
```

The two remaining four-dimensional matrices are therefore

```
F_up=(D8)_PP-(D8)_P,RT R_up^(-1)(D8)_RT,P,
F_low=(L8)_PP-(L8)_P,RT R_low^(-1)(L8)_RT,P. (R4)
```

These are different matrices. Their signs are **unproved**. All quantities in (R2)-(R4) are regular for every reference spectrum; the only inverses displayed in (R4) have the stated positive physical pivots.

## 4. Both zero-charge six-dimensional forms

### 4.1 Explicit sixteen-dimensional p operators

The p space is identified with `C4_input tensor C4_output` through `p(i,j)=|i,i,j,j>`. Column vectorization is `|X>>=sum_i |i> tensor X|i>`. Define

```
Omega4=sum_i |i,i>,
Pi=sum_(i!=j)|i,j><i,j|+|Omega4><Omega4|/4,
P=cc^T, A0=I-diag(x)+P/4,
J_M=Pi(P tensor A0^(-1))Pi,
Cp=Pi^Gamma, Sp=J_M^Gamma,
rho=Cp-Sp, Lp=3Cp+Sp=4Cp-rho.
```

Gamma is input partial transpose. Pi is a rank13 orthoprojection and J_M a rank4 orthoprojection. The upper p reference projector is `Pref=P tensor I4`; rho annihilates it. Checkpoint 017 proves rho positive for every reference, and strictly positive on the reference-perpendicular p12 quotient on the full positive interior. Thus

```
rho_reg=rho+Pref
```

is invertible on that interior. Checkpoint 018 proves the **full** Lp strictly positive for every normalized reference, including sparse spectra; its inverse includes the true lower reference correction automatically.

### 4.2 The six q-plus coordinates and their full q block

Use the six fixed normalized coordinates indexed by unordered pairs

```
q_plus(a,b)=[|a,b,b,a>+|b,a,a,b>]/sqrt(2), a<b.
```

Let Tq be the symmetric 6-by-6 matrix with

```
(Tq)_(ab,ab)=E_ab,
(Tq)_(ab,bt)=K_at for distinct a,b,t,
(Tq)_(ab,cd)=0 for disjoint unordered pairs.
```

The shared-label rule is independent of how each unordered pair is written. These are all entries. The raw C block here is `(5/4)I6`, so the raw upper/lower q-plus blocks are `(5/4)I6-Tq` and `(15/4)I6+Tq`.

### 4.3 Explicit p/q-plus cross columns

For each unordered pair a,b define the real symmetric matrix

```
F_ab=|a><b|+|b><a|,
v_ab=F_ab c,
f_ab=Tau^(ab)c,
d_ab=c^T f_ab.
```

The actual upper cross column, as a vectorized 4-by-4 matrix, is

```
H_ab=|[v_ab f_ab^T/d_ab-F_ab]/sqrt(2)>>.      (R5)
```

It is reference-perpendicular because the matrix inside annihilates c. The C cross column is `-|F_ab>>/sqrt(2)`. Hence the actual lower cross is

```
J_ab=-|[3F_ab+v_ab f_ab^T/d_ab]/sqrt(2)>>.    (R6)
```

In particular J_ab is **not** reference-perpendicular; its reference component must be retained. Eliminating all p16 using Lp is a compact way to retain it exactly.

Write Hq and Jq for the sixteen-by-six matrices of these columns. The two remaining six-dimensional matrices are

```
Z_up=(5/4)I6-Tq-Hq^T rho_reg^(-1)Hq,
Z_low=(15/4)I6+Tq-Jq^T Lp^(-1)Jq.          (R7)
```

The added Pref in rho_reg does not affect its upper Schur subtraction because `Pref Hq=0`. Z_low uses the entire positive p16 inverse, so it includes both the reference and p12 Schur operations. No lower reference component is discarded.

Both signs in (R7) are **unproved**. Z_up is used on the full positive interior, where its inverse is legitimate. A proof there must extend the entire physical zero matrix to sparse spectra by continuity; it must not evaluate an inverse of a boundary-singular upper p pivot. Z_low is well-defined on the closed reference simplex by strict positivity of Lp.

## 5. Why these four signs suffice, and what remains open

The exact torus-sector profile of the 256-dimensional co-Choi space consists of scalar12, two families of two-dimensional blocks (24+24), six four-dimensional blocks (24), twelve charge12 blocks (144), and one zero28 block. The dimensions sum to256. This is a decomposition, not a discovery count.

- Scalar and two-dimensional phase families have their earlier hand closures.
- Both signs of each whole four-dimensional phase block have checkpoint 009's hand closure.
- A charge12 upper block has one actual reference kernel, the positive joint Q/RT seven-pivot, and F_up. Its lower block has the actual reference4d pivot, its positive Q/RT seven-pivot, and F_low.
- In zero28, q-minus6 is reducing with the earlier positive bounds. The upper remainder has four reference kernels, p12 positive on the full interior, and Z_up. The lower p16 is strictly positive including its reference part, leaving Z_low.

All cross terms are present in (R4) and (R7). Ordinary Schur equivalence therefore gives (R1) on the interior. The physical A_eta lower bound makes every original block continuous on the compact normalized reference domain, completing the stated closed-simplex implication if all four interior signs are established.

What remains is exactly the four matrix inequalities (R4),(R7), not a final step hidden in a claimed theorem. No proof, negative direction, sample, determinant certificate, or novelty verdict for those four signs is supplied by this reduction.

## 6. Provenance and gates

The frozen source/dependency hashes through checkpoint018 are in `all-reference-working-manifest-v2.json`, SHA256 `4aad56bdfc55160c5684f7551af1ce371545ea079fbc1cedad5f9e790a20d6cc`.

Load-bearing working leaves are the full raw tables001/002/004, regular inverse005, reducing-q bounds003, full four-phase proof009, charge principal proofs015/016, and zero p principal proofs017/018. Earlier dimension reductions and alternative inverse representations remain preserved but are not independent theorems or accepted gates.

All generic-reference leaves remain **CANDIDATE / UNREVIEWED**. Prior written checking of the paired-reference theorem does not transfer. The admitted seven-reference assay is finite evidence and is not used in this reduction proof. Both polynomial requests remain author-requested HOLD; no science output from them was received or used. No proof assistant, independent model review, external acceptance, unrestricted W4 conclusion, or source/novelty clearance is claimed.
