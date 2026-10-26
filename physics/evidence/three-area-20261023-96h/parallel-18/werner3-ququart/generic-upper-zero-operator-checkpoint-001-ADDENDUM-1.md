# Generic operator attack addendum1: the separate Korn estimate is false; retain the compatibility penalty

Actual clock observed before writing: **2026-10-24T06:03:42-07:00**, `/bin/date -Iseconds`. Owner PhysicsResearch96h.

**NEW CANDIDATE hand obstruction and generic operator continuation.** No scientific program, numerical experiment, arithmetic interpreter, CAS, import, compilation/test, model CLI or nested agent was used. This is not a new launch request.

Consume the immutable `generic-upper-zero-operator-checkpoint-001-v1.md`, SHA256 **`249c1becd5e89ff08a3badebaab8234f3e89d7cb7879430e8e9152eabff18a7e`**. Its G13 was clearly labeled an UNPROVED sufficient estimate, not an accepted premise. The result here is an attack outcome, not a repair to an asserted proof of G13. Its G1–G12 identities and exact original-target boundary are not altered.

## 1. A genuinely full-spectrum counterexample to G13

Choose the normalized, strictly positive, four-DISTINCT Schmidt squares

```
(x1,x2,x3,x4)=(872,125,1,2)/1000,
c_i=sqrt(x_i), Q=I-cc^T,
Z=|1><Qe3|, so Zc=0.
```

The notation is output row/input column: Z has only its first output row, equal to `(Qe3)^T`. Thus it is an admissible p-quotient test. It is not a64x64 rank-two Werner coefficient witness.

For this test, the actual row and swap terms are exactly

```
<Z,B'Z>=d1^2 d3-d1 x1 x3=d1(x2+x4),
<Z,F_Q Z>=x1 x3.
```

Only edges1j contribute to the off-diagonal subtraction in G13. Therefore its exact value is

```
P_c(Z)=(d1/2)(x2+x4)+r x1 x3
       -d1^2[d3^2/(4g13)+x3 x2/(4g12)+x3 x4/(4g14)].  (A1)
```

Every symbol here is the literal generic operator from G12/G13; no symmetry reduction or replacement inverse was made.

A short strict rational upper bound suffices to prove negativity. Here

```
d1=16/125, x2+x4=127/1000, d3=999/1000,
r<d1,
(d1/2)(x2+x4)=127/15625,
r x1 x3<d1 x3=2/15625.
```

Also

```
4g13=2(d1+d3)-(d1-d3)^2
     =1495359/1000000 <3/2,
d3^2=998001/1000000>99/100.
```

Discarding the OTHER TWO nonnegative subtractions in (A1) gives the valid upper bound

```
P_c(Z)<129/15625-d1^2(99/100)/(3/2)
      =129/15625-(33/50)(256/15625)
      =-999/390625 <0.                         (A2)
```

Thus **G13 is FALSE**, with a fully specified positive, full-rank, four-distinct reference and an exact algebraic p test. This is an upper bound on its negative value, not a fabricated exact equality or a sampled float.

It refutes ONLY the sufficient estimate obtained by dropping the two nonnegative compatibility squares in G12. It does NOT refute the stronger R0 comparison G7, the exact Z_up sign, the full route, or W4. No q test was supplied that makes the entire physical joint form negative. The square centers are different and generally cannot vanish simultaneously.

## 2. The exact generic compatibility operator

Retain G12 instead of dropping its positive squares. Its notation is

```
Gamma(T)=sum_(i;j<t)gamma_(i;jt)|T_ij-T_it|^2,
gamma_(i;jt)=d_i x_i x_j x_t/2,
m_ij=x_i x_j g_ij>0,
e_ij=x_i x_j(d_i T_ij+d_j T_ji),
a_ij=e_ij/(sqrt(2)m_ij),
delta_ij=a_ij-sqrt(2)T_ij.
```

T is the directed p array Z_ij/(c_i c_j), with every row weighted sum zero. The mass center a is a symmetric edge array; delta is generally directed.

Introduce the actual weighted row-difference operator C from UNDIRECTED edge6 to row-difference12:

```
(Cy)_(i;jt)=sqrt(gamma_(i;jt))(y_ij-y_it).
```

Let `d_delta` be the same weighted row differences of the directed delta. This symbol is a12-vector, not the reference diagonal d_i. Let M be the positive diagonal six-matrix with entries m_ij. The minimum of the two squares in G12 is exactly

```
Penalty_c(T)
 =min_(y in C6) (||Cy+d_delta||^2+y^dagger M y)/2
 =(1/2)d_delta^dagger[I+C M^(-1)C^dagger]^(-1)d_delta.    (A3)
```

Indeed set y=z-a in G12, expand, and eliminate the positive pivot `M+C^dagger C`. The equivalent inverse identity

```
I-C(M+C^dagger C)^(-1)C^dagger
 =[I+C M^(-1)C^dagger]^(-1)
```

follows by multiplication. It is not a pointwise numerical inversion or a singular endpoint claim.

Consequently the generic stronger R0 comparison is exactly equivalent to

```
P_c(Z)+Penalty_c(T)>=0 for every Zc=0,          (A4)
```

NOT to the false standalone P_c>=0. This returns a NONNEGATIVE compatibility correction for arbitrary full spectra, rather than special-casing the counterexample in Section1.

## 3. Uniform graph bound for that positive correction

The weighted line-graph degree at edge ij is

```
Degree_ij
 =sum_(t!=i,j)[gamma_(i;jt)+gamma_(j;it)]
 =x_i x_j d_ij(2d_ij-1).
```

This satisfies the exact scalar bound

```
Degree_ij<=m_ij.                              (A5)
```

To verify it, put u=d_ij. The physical inequalities give `1/2<=u<=1` and `|d_i-d_j|<=2(1-u)`. Thus

```
g_ij-u(2u-1)
 =2u(1-u)-(d_i-d_j)^2/4
 >=(1-u)(3u-1)>=0.
```

For every undirected y, the elementary difference estimate now gives

```
||Cy||^2<=2sum_edges Degree_ij|y_ij|^2
         <=2y^dagger M y.
```

Hence `C M^(-1)C^dagger<=2I` on the twelve row-difference coordinates, and (A3) proves the whole generic lower bound

```
Penalty_c(T)>=||d_delta||^2/6
             =Gamma(delta)/6.                 (A6)
```

No extremal reference or selected parameter family is used in this certificate. All complex y and directed delta are included. The exact A3 correction is kept if this coarser lower bound is insufficient.

## 4. The three genuine circulation modes are not lost

Let H_circ be the orthogonal projection onto ker(C^dagger) in row-difference12. The inverse in A3 acts as the identity on this kernel. Therefore the stronger bound is

```
Penalty_c(T)
 >=(1/2)||H_circ d_delta||^2
   +(1/6)||(I-H_circ)d_delta||^2.              (A7)
```

Because a is an undirected edge array,

```
H_circ d_delta=-sqrt(2) H_circ d_T,
```

where d_T denotes the weighted row differences of the directed T. Thus the irreducible circulation part is not an artifact of the chosen mass center.

The general directed row-difference image has dimension8: each of four rows has three off-diagonal values modulo one row constant. The connected line-graph image ran C has dimension5, since its only undirected kernel is the constant edge array. It lies inside that8-dimensional image. Hence the physically relevant orthogonal circulation complement has dimension3, not an uncontrolled12-dimensional remainder.

Its exact compatibility test is also concrete. H_circ d_T=0 iff there is an undirected edge array z such that

```
T_ij-z_ij=lambda_i for each directed off-diagonal entry.
```

Symmetry of z then gives `T_ij-T_ji=lambda_i-lambda_j`, equivalently zero circulation of this antisymmetric edge array on every triangle of K4. Conversely that gradient condition constructs such a z by subtracting the row constants. This is a generic weighted-graph/Hodge obstruction; it is NOT assumed automatically true for an arbitrary p test.

Mass-center gradient incompatibility still remains even when these three curls vanish. Accordingly no argument discards either term of A7 or claims the circulation correction alone proves A4.

## 5. Operative frontier after the obstruction

The current operator mechanism is the FULL identity

```
minimum stronger joint energy=P_c(Z)+Penalty_c(T),
```

with the exact positive correction A3 and proved lower bounds A6/A7. A possible further sufficient estimate is

```
P_c(Z)+Gamma(delta)/6>=0,
```

but it is **UNPROVED**, not a new premise or a replacement of A4. If it fails, retain A3/A7 rather than labeling the R0 or Z_up target false. If the R0 comparison itself fails, retain the entire positive Qraw-R0 remainder of the previously written-supported packet.

The original generic upper-zero-six question and all other final-sign/W4 boundaries are unchanged. This addendum supplies a checkable FULL-SPECTRUM obstruction to one overly strong operator estimate and a genuinely coupled replacement mechanism; it does not supply a selected-family theorem or a negative physical Werner witness. These new written claims require actual independent reconstruction before any promotion.
