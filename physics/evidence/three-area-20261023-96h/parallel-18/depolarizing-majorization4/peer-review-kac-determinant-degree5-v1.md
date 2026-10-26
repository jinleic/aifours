# v41-B — degree-five determinant reduction; six numeric equalities remain NOT_RECONSTRUCTED

Actual `/bin/date` before creation: **Sun Oct 25 05:59:58 PDT 2026**. Reviewer PhysicsDepol4-2. Strict WRITTEN reconstruction and metadata only; HOLD and parent erratumv8 binding. No scientific program/eval/interpreter, arithmetic or symbolic program, enumeration, replay, solver, CLI, nested agent or GO.

## 1. Exact verdict — do not compose this as a degree-five PASS

**All SIX requested numerical degree-five coefficient equalities remain NOT_RECONSTRUCTED.** A MAJOR load-bearing acceptance gate is still open. No wrong author coefficient or mathematical counterexample is established.

This return derives an exact smaller bordered-pencil/cofactor expression for the whole degree-five part, including its scale and all six coefficient groups. It does NOT evaluate the remaining five quartic-minor coefficients and six cubic-contraction groups needed to obtain the six claimed integers. A formula specifying a finite calculation is not mislabeled as having performed that calculation.

- **Reconstructed reduction/scale:**0 FATAL /0 MAJOR /0 MINOR at the exact partial algebra below.
- **Assigned six numerical degree-five identities:** NOT_RECONSTRUCTED; **one MAJOR acceptance gap covering six individually listed obligations**.
- **Author coefficient falsity:** not demonstrated.
- No degree4/6, full determinant, all-quadrant sign or actual D3/quotient acceptance.

## 2. Pins, complete literal coverage and exposure

Source **F**: `mathematics/evidence/three-area-20261023-96h/parallel-18/kac-moody/level5-full-invariant-quotient-v1.md`, complete LF1–144, SHA256 `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`.

Source **R**: `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/peer-review-kac-R1-determinant-completion-v1.md`, complete LF1–273, SHA256 `5504702ef807bdd3e3767aac8cd134edbf1c138a888770d495185fb8b62d1159`.

The mandatory431-line literal packet `peer-review-wave-v41-kac-determinant-degree5-sources-v1.md`, SHA256 `19854bf4775694ea67f8ba4adca7771e4bcaffdd77d8f49475cde07d4b7ce058`, was read completely in three windows; all144+273 source lines were read, no truncated source line left unread.

Manifest observed SHA256 `cd45439a2c5171a355e66dc75aca29a7d100f784837cb4affbc2b8c3ded732bf`. Receipt observed SHA256 `8d477259c3dd08f474ebcbe405a8b1847b843160fee766d97bd58169da2cd2e0`, read completely. Source/packet pins match metadata. Parent receipt asserts literal equality; reviewer did not regenerate the packet.

Parentv8 was read FIRST, complete LF1–37, SHA256 `52408180ac48dec69d2144ea0dee07acf08f0739f65a8cdb2b007656243527e9`. Its withdrawal of premature parent acceptance and all prior HOLD/v7 qualifications are retained. Pinning a prior review does not make its body or its remaining coefficient evaluations accepted.

`peer-review-kac-determinant-degree5-ack-v1.json` was written before the proof body/new derivation. It discloses prior reading of F and its target triangle during v35-B. My previous columnS3/S4 derivation is NOT a premise for the GIVEN-pencil calculation here. R's degree1–3 outputs are exposure, not proof of any degree5 term. No v41-A/C result or historical interpreter boolean is imported.

Line references below mean original F/R source lines.

## 3. Normalize the GIVEN pencil and prove the minor scale

Take the matrix F102–107 as GIVEN. Set

`N=M/3=aA+bB+cC`, `D=det N`, so `det M=729D`.

Replace column2 by column2+2column1−3column4; the determinant is unchanged. Directly from the displayed coefficients the distinguished column is `b k_b+c k_c`, where

`k_b=(6,-10,-10,-8,8,14)^T`,

`k_c=(3,-3,-9,-7,5,-9)^T`.

Let O=(1,3,4,5,6), using ONE-based matrix indices. The constant minor on rows(1,2,4,5,6) and columnsO is

`E=[[0,-27,-3,-3,-27],`

`   [-6,-15,-3,-7,12],`

`   [0,9,3,2,3],`

`   [0,-9,-4,-2,-3],`

`   [3,21,6,3,27]]`.

Here is a written evaluation of det E, rather than assuming its copied value. Add its third row to its fourth; that row becomes(0,0,−1,0,0). Expanding there gives the four-minor

`[[0,-27,-3,-27],[-6,-15,-7,12],[0,9,2,3],[3,21,3,27]]`.

Expansion in its first column is6 times

`det[[-27,-3,-27],[9,2,3],[21,3,27]]=-270`

minus3 times

`det[[-27,-3,-27],[-15,-7,12],[9,2,3]]=-135`.

Thus det E=6(−270)−3(−135)=−1215, in particular E is genuinely invertible.

Let `ell=(6,2,-1,48,36,5)^T`. Multiplication in the GIVEN matrices gives

`ell^T A=0`, `ell^T k_b=0`, `ell^T k_c=-180`.

For example the constant O-column dot products are respectively

`-12-3+15=0`,

`-162-30-21+432-324+105=0`,

`-18-6-6+144-144+30=0`,

`-18-14-7+96-72+15=0`,

`-162+24-33+144-108+135=0`.

The corresponding five B/C row contractions are

`r_b=(12,-204,-36,-24,24)`,

`r_c=(-102,-210,-18,-24,-36)`.

For instance the B first-column dot is36−16+7−160+120+25=12, and the C first-column dot is6+6−192+108−30=−102. Each remaining dot uses the same explicit ell and respective GIVEN column; these are ordinary five-coordinate restrictions, not null vectors inferred from sampled determinants.

The actual derivative minors read directly from the GIVEN B/C are

`E_b=[[6,15,3,5,21],`

`     [-8,-17,-3,-5,-20],`

`     [-10/3,-19/3,-1/3,2/3,3],`

`     [10/3,1/3,-2/3,-2,-5],`

`     [5,5,-4/3,-1,-5]]`,

`E_c=[[0,9,1,0,18],`

`     [3,6,1,4,-12],`

`     [-4,-13,-2,-2,0],`

`     [3,12,7/3,2,-2],`

`     [-6,-18,-3,-2,-12]]`.

Define the fully specified rational matrices `T_b=E^-1 E_b`, `T_c=E^-1 E_c`. This definition, with the explicit nonsingular E, is enough for the exact reduction; it is NOT a claim that all subsequent higher trace products have been evaluated. It avoids assuming that a prior displayed table of T_b/T_c products is a proof of the new coefficients.

## 4. Exact bordered pencil and two explicit right vectors

The vectors

`h_b=(68/9,4/9,0,-6,0)^T`,

`h_c=(118/9,77/9,2,-38,-14/3)^T`

satisfy `E h_b=(k_b)_O` and `E h_c=(k_c)_O`. To display the full small checks, the five row products for h_b are

`-12+18=6`, `-52+42=-10`, `4-12=-8`, `-4+12=8`, `32-18=14`.

For h_c they are

`-231-6+114+126=3`,

`-207-6+266-56=-3`,

`77+6-76-14=-7`,

`-77-8+76+14=5`,

`219+12-114-126=-9`.

Reorder rows as(1,2,4,5,6,3) and columns as(O,2). The row permutation has sign−1, the column permutation sign+1. Replace the last row by ell's row combination; its coefficient of the old last row is−1. These two signs cancel. Finally multiply the top five rows by E^-1. Therefore

`D=det(E) det H=-1215 det H`,

where the literal normalized bordered pencil is

`H=[[a I5+bT_b+cT_c,  b h_b+c h_c],`

`   [b r_b+c r_c,              -180c]]`.             (BORDER)

For Q=aI5+bT_b+cT_c, r=br_b+cr_c and h=bh_b+ch_c, the polynomial block determinant identity gives

`D=218700 c det Q+1215 r adj(Q)h`.                     (BD)

This identity is polynomial and holds even at singular Q; no inverse of a parameter-dependent matrix is assumed. It follows by Laplace expansion of the bordered determinant. Its scale to the original matrix is exact:

`det M=729D=-885735 det H`.

This is only a normalization/reduction, not the target determinant triangle.

## 5. Extract JUST homogeneous degree five after the shift

Use F115's substitution and put

`a_h=(u+v)/2`, `b_h=(u-v)/2`, `c_h=-(u+v)`.

Because D is homogeneous of degree6 in(a,b,c), the degree-five part after `a=1+a_h,b=b_h,c=c_h` is exactly

`D_5(u,v)=(partial D/partial a)(a_h,b_h,c_h)`.          (SHIFT)

One way to verify the factor is to insert a formal scale t: `D(1+t a_h,t b_h,t c_h)=t^6 D(a_h+t^-1,b_h,c_h)`. The coefficient of t5 is the FIRST a derivative, with no factorial or extra six. This is exact coefficient extraction, not evaluation at finitely many sample u,v values.

For a five-matrix L, let e_j(L) be the elementary characteristic coefficient (sum of its j-principal minors). Then

`partial_a det(aI+T)=e4(aI+T)`,

`partial_a adj(aI+T)=J3(aI+T)`,

`J3(L)=e3(L)I-e2(L)L+e1(L)L²-L³`.                     (ADJ)

The second identity follows by differentiating `adj L=L4-e1 L3+e2 L2-e3 L+e4 I` and using `partial_a e_j=(6-j)e_(j-1)` for a five-matrix. Combining terms leaves exactly(ADJ), including the−L3 term. Both statements are polynomial, hence include singular L.

Define

`L=u L_u+v L_v`,

`L_u=E^-1(E/2+E_b/2-E_c)`,

`L_v=E^-1(E/2-E_b/2-E_c)`.

The row/column data in the same physical homogeneous substitution become

`r=u r_u+v r_v`,

`r_u=(108,108,0,12,48)`,

`r_v=(96,312,36,36,24)`,

`h=u h_u+v h_v`,

`h_u=(-28/3,-25/3,-2,35,14/3)^T`,

`h_v=(-152/9,-79/9,-2,41,14/3)^T`.

They are simply r_b/2−r_c,−r_b/2−r_c and the corresponding h combinations; the inverse E has already been confined to the explicitly specified L matrices.

Equations(BD),(SHIFT),(ADJ) now prove the exact whole degree-five expression

`D_5=218700 c_h e4(L)+1215 r J3(L)h`.                 (D5)

Consequently its target-normalized polynomial is

`P_5^actual:=-(detM)_5/43740=-D_5/60`

` =3645(u+v)e4(L)-(81/4) r J3(L)h`.                  (P5)

This is a complete exact cofactor GROUPING derived from the GIVEN pencil. It is not a derivation of the six advertised numeric values until the remaining explicit expressions are evaluated.

## 6. All six remaining coefficient groups, individually identified

Write

`e4(L)=sum_(j=0)^4 E_j u^(4-j)v^j`,

`J3(L)=sum_(j=0)^3 J_j u^(3-j)v^j`,

with E_j=0 outside0..4 and J_j=0 outside0..3. All are determined by the explicit E,E_b,E_c; e4 is the sum of the five four-by-four principal minors, and J3 is the displayed cubic matrix polynomial.

Let

`W_j=r_u J_j h_u+r_v J_(j-1) h_u`

`       +r_u J_(j-1) h_v+r_v J_(j-2) h_v`.

There is no commutativity shortcut between the matrices: both mixed row/matrix/column orders remain. The six normalized degree-five coefficient identities are EXACTLY

`C_j=3645(E_j+E_(j-1))-(81/4)W_j`, j=0,...,5.          (GROUP)

Explicitly their finite cofactor groups are

|monomial|actual expression from the GIVEN pencil|source target, NOT established here|
|---|---|---|
|u5|`3645 E0-(81/4) r_u J0 h_u`|15438|
|u4v|`3645(E1+E0)-(81/4)(r_u J1 h_u+r_v J0 h_u+r_u J0 h_v)`|89052|
|u3v2|`3645(E2+E1)-(81/4)(r_u J2 h_u+r_v J1 h_u+r_u J1 h_v+r_v J0 h_v)`|195747|
|u2v3|`3645(E3+E2)-(81/4)(r_u J3 h_u+r_v J2 h_u+r_u J2 h_v+r_v J1 h_v)`|202992|
|uv4|`3645(E4+E3)-(81/4)(r_v J3 h_u+r_u J3 h_v+r_v J2 h_v)`|99540|
|v5|`3645 E4-(81/4) r_v J3 h_v`|18621|

**Unfinished scalar evaluations:** the five numbers E0,...,E4 and the six aggregate contractions W0,...,W5 have not been reconstructed to final rational values in this return. Merely writing them as a determinant/minor recurrence, or copying R's lower-order trace products, does not close these evaluations. No inference from the rightmost target column of this table is permitted.

Thus the individual obligations remaining are

- `[u5]det M=-43740*15438`: **NOT_RECONSTRUCTED**;
- `[u4v]det M=-43740*89052`: **NOT_RECONSTRUCTED**;
- `[u3v2]det M=-43740*195747`: **NOT_RECONSTRUCTED**;
- `[u2v3]det M=-43740*202992`: **NOT_RECONSTRUCTED**;
- `[uv4]det M=-43740*99540`: **NOT_RECONSTRUCTED**;
- `[v5]det M=-43740*18621`: **NOT_RECONSTRUCTED**.

These are source F129 and R260, not new measured numbers. The previous degree1–3 reconstruction cannot supply the missing e4/minor and cubic-contraction evaluations by headline or continuity. Neither a sampled univariate determinant nor six evaluated sample points was used.

## 7. FATAL/MAJOR/MINOR and exact acceptance boundary

### MAJOR-G1 — six degree-five numeric identities not yet reconstructed

- **Source claims:** F117–132, especially F129; R255–263 explicitly lists this row as unclosed.
- **Evidence:** §§3–6 derive a genuine bordered/cofactor reduction with exact normalization, but its eleven aggregate coefficient evaluations are still open. No target equality in the six-row table has been proved by the reduction alone.
- **Classification:** load-bearing ACCEPTANCE GAP, not evidence that an author coefficient is wrong. It is consistent with R's own NOT_RECONSTRUCTED verdict and parentv8.
- **Required closure:** evaluate the specified cofactor groups in writing or provide a complete alternative independent degree-five coefficient derivation. Until then, do not count v41-B as six new supported coefficients or compose it into a full determinant PASS.

No FATAL contradiction or additional MINOR defect was established in the reconstructed reduction. Historical unadmitted arithmetic supplies no verification credit and was not rerun.

## 8. Explicit exclusions

- No numerical degree-five target accepted; all six remain open above.
- No degree4/6 coefficient verdict, full determinant identity, positive-quadrant sign or determinant nonvanishing proof.
- No assertion that the GIVEN pencil equals the original D3 images. My separate v35-B column report is not used to infer this determinant or the other column gates.
- No full invariant source basis, actual3-to5 quotient, other primitive-map rank, F5, H13 or Serre theorem acceptance.
- No formal/kernel, executable/finite-certificate, human, cross-vendor, independent-family or novelty acceptance.

**Disposition:** PARTIAL WRITTEN reduction only, with all six assigned numeric obligations explicitly NOT_RECONSTRUCTED. Parentv8's withdrawn blanket promotion is not reinstated by a new algebraic representation.
