# v42-C — complete written homogeneous degree-six determinant

Observed `/bin/date` before creation: **Sun Oct 25 06:31:07 PDT 2026**. Reviewer `InfoRecursiveMDS18-2`; author `MathKacMoody`.

## 1. Verdict and boundaries

**ALL FIVE remaining mixed identities are reconstructed in writing.** The complete homogeneous degree-six determinant of the GIVEN pencil is

`-43740*(2964u^6+20414u^5v+56828u^4v^2+80639u^3v^3`
`                  +61380u^2v^4+23913uv^5+3762v^6)`.

**0 FATAL / 0 MAJOR / 0 MINOR mathematical defects found at this given-pencil degree-six scope.** No scalar in this assigned slice remains NOT_RECONSTRUCTED. The proof is the actual polynomial elimination, reduced3x3cofactors and evaluated coefficient groups below, not another unevaluated multinomial definition or endpoint interpolation.

No degree1–5, whole determinant, source-image, full108-scalar composition, invariant injectivity or actual3-to5 acceptance is inferred by this return. The prior endpoint review remains immutable and correct about its earlier five open mixed obligations. Parent errata v7/v8 remain binding.

**WRITTEN ONLY:** no scientific interpreter/eval, arithmetic program, symbolic program, enumeration program, sampled determinant, certificate replay, solver, CLI delegate or nested agent. Only metadata clocks/hashes and ordinary source reads were performed. The calculations below are handwritten rational polynomial operations. No historical unadmitted arithmetic receives credit.

## 2. Complete sources, pins and supplied-proof exposure

Manifest observed SHA-256 `5a6c96653bdd223e31c7d1cd4ff9cf353856363eed43b9363e603d2da3d35159`.

The complete830-line mandatory literal packet was read raw in ranges1–180,181–355,356–535,536–710,711–830. All declared source LF were read; no truncation or omitted body remains:

|Label|Source|Complete LF|Observed SHA-256|
|---|---|---|---|
|S1|`level5-full-invariant-quotient-v1.md`|1–144|`a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`|
|S2|own `peer-review-kac-determinant-degree6-v1.md`|1–252|`3684ce9c093564ef5e92940fa6be39119576d423a86b84eb1d957010b9c9ecd0`|
|S3|`peer-review-kac-determinant-degree4-v1.md`|1–419|`dc3faec7e7405710b9afd8f9ab5af5c4a9d030a217c849d567f892c11a3e24b4`|

Literal packet hash observed: `6f43633a56656763dfc85bd6dc5a0e68569fc9b64e662f1a522ca7462caa8b60`, matching the metadata receipt. Parentv8, exact entry including its untruncated scope, and receipt were read before the exposureACK/body.

I authored S2's explicit U,V and endpoint reductions. Its five mixed targets were known but unproved. S3 is new supplied-proof exposure and is fully read; its inverse/cofactor products are NOT numerical premises of the alternative elimination below. I do not call this a blind reconstruction or independent rediscovery of S3's trace products. The new proof instead starts directly from the GIVEN pencil S1LF102–107 and performs a different homogeneous polynomial elimination. Same-harness written supplied-proof review is not cross-vendor/human/formal/novelty acceptance.

## 3. Formal homogeneous reduction — no sampling

Let U,V be the integer coefficient matrices of S2LF45–59, so the assigned highest part is `det(uU+vV)`. Put T=u+v,d=u-v. At top degree only, a=T/2,b=d/2,c=-T=-2a.

Define the formal one-variable matrix

`H(t)=M(a=1,b=t,c=-2)=(U+V)+t(U-V)`.

This is dehomogenization of a HOMOGENEOUS matrix pencil, not evaluating the shifted determinant at sample points. Explicitly:

```
H(t)=
[18t,       -63+9t,  -135+45t, -15+9t,  -9+15t,  -189+63t;
 -36-24t,    45-9t,   -81-51t, -15-9t, -45-15t,   108-60t;
 45-21t,     36+24t,   99-21t,  24+4t,  33-3t,    171+3t;
 24-10t,     57-7t,   105-19t,  21-t,   18+2t,      9+9t;
 -18+10t,   -72-2t,   -99+t,   -26-2t, -18-6t,      3-15t;
 45+15t,     72,      171+15t,  36-4t,  21-3t,    153-15t].
```

Every operation below is over Q[t], dividing only by NONZERO CONSTANTS. Hence there are no exceptional variable pivots to discard. At the end, homogenization establishes an identity in Q[a,b], including a=0 by polynomial identity, not a limiting assertion about selected physical parameters.

## 4. First constant pivot: six dimensions to five

Set R2<-R2+R1 and R5<-R5+R4. Set C3<-C3-C1 and C6<-C6+C1/2. The new row2 is

`(-36-6t,-18,-180,-30,-54,-99)`.

Clear every entry except its column2 entry-18 using

```
C1 <- C1-(2+t/3)C2,
C3 <- C3-10C2,
C4 <- C4-(5/3)C2,
C5 <- C5-3C2,
C6 <- C6-(11/2)C2.
```

All these column additions preserve the determinant, even with polynomial multipliers. Expanding at row2/column2 gives

`det H=-18 det B5`.

The remaining row labels are(1,3,4,5,6) and column labels(1,3,4,5,6). Name their columns X,Y,Z,W,Q respectively. For an unchanged remaining row with ORIGINAL H entries o1,...,o6,

```
X=o1-(2+t/3)o2,
Y=o3-o1-10o2,
Z=o4-(5/3)o2,
W=o5-3o2,
Q=o6+o1/2-(11/2)o2.
```

Replace Y by Y-6Z; equivalently Y=o3-o1-6o4. The special row5, which is the sum of original rows4/5, is now

`(36+23t+3t^2, 30, 20+12t, 45+23t, (195+87t)/2)`.

Thus the second pivot is the CONSTANT30 in row4/column2 of B5.

## 5. Second constant pivot and a fully displayed four-matrix

Let h=Y/30 for each of the other four rows(1,3,4,6). They are

`(-45-27t)/30`, `(-90-24t)/30`,
`(-45-3t)/30`, `(-90+24t)/30`.

Eliminate the special row using the constant30 pivot. Its cofactor sign is positive. Thus

`det H=-540 det B4`,

where B4 has columns X,Z,W,Q after subtracting h times the corresponding special-row entries.

Now perform the following column changes ON B4:

```
X' = X-(t/4+3/2)Z,
Z' = Z,
L  = 23Z-12W,
N  = 4Q-(29/2)Z.
```

This column transformation has determinant-48. Its special-row values before elimination are6,20+12t,-80,100. Therefore the new four-matrix entries, for each remaining original row, can be calculated directly as

```
X'=o1-(3/2+t/4)o4+(1/2+t/12)o2-Y/5,
Z'=o4-(5/3)o2-(2/3+2t/5)Y,
L=23o4-12o5-(7/3)o2+(8/3)Y,
N=4o6+2o1-(29/2)o4+(13/6)o2-(10/3)Y.
```

Scale these columns by60,15,3,3, respectively. Their product is8100. The resulting integer-polynomial matrix C is

```
[774t-90t^2,          1800+450t+162t^2,      -630-198t, -1575+801t;
 2700-792t+60t^2,      360+240t+144t^2,      -504+24t,   2412+132t;
 1800-714t-20t^2,     -660+460t+18t^2,         42-116t,   159+76t;
 2700+792t+60t^2,     -360+240t-144t^2,        504+24t,   1908-156t].
```

For example its first entry is

`60*(18t)-(90+15t)*(-15+9t)+(30+5t)*(-63+9t)-12*(-45-27t)`
`=774t-90t^2`.

Its second-row second entry is

`15*(24+4t)-25*(36+24t)-(10+6t)*(-90-24t)`
`=360+240t+144t^2`.

The other entries follow from the same explicitly displayed original-row formulas, so no unseen minor evaluation is used.

The complete scale is

`det H=(45/4)det(X',Z',L,N)=det C/720`.

Factor9 from C's row1,12 from row2,12 from row4. Their product is1296, giving

`det H=(9/5)det D4`,

```
D4=
[86t-10t^2,        200+50t+18t^2,  -70-22t, -175+89t;
 225-66t+5t^2,      30+20t+12t^2,  -42+2t,   201+11t;
 1800-714t-20t^2,  -660+460t+18t^2, 42-116t, 159+76t;
 225+66t+5t^2,     -30+20t-12t^2,   42+2t,   159-13t].
```

This is the promised actual polynomial reduction, not a definition of an unevaluated coefficient sum.

## 6. Third CONSTANT pivot and a three-by-three determinant

Set row4<-row4-row2 in D4 and factor6 from it. Denote the new row4 by

`F=(22t,-10-4t^2,14,-7-4t)`.

Call this matrix E4. Then `det H=(54/5)det E4`.

Using the OLD row1 of E4, first set

`R3 <- R3-2R1-(9/2)F`,

then set

`R1 <- R1+2R2+(21/2)F`.

Multiply rows1 and3 by2. These are constant row additions followed by total row scaling4. The resulting matrix G4 is

```
[900+370t,         310+180t,      -14-36t,  307+138t;
 225-66t+5t^2,      30+20t+12t^2, -42+2t,   201+11t;
 3600-1970t,      -2030+720t,      238-144t,1081-168t;
 22t,              -10-4t^2,       14,       -7-4t].
```

The scale is `det H=(27/10)det G4`.

Set C2<-11C2+2tC1, multiplying the determinant by11. The last row's column2 becomes the CONSTANT-110. Its column3 is14. Clear the other three last-row entries by

```
C1 <- 14C1-22tC3,
C2 <- 14C2+110C3,
C4 <- 14C4+(7+4t)C3.
```

These operations multiply that determinant by14^3. Expansion at row4/column3 has NEGATIVE cofactor sign and pivot14. Hence, for the three-matrix K3 remaining on rows1–3 and columns1,2,4,

`det H=-27 det K3/21560`,

where

```
K3=
[12600+5488t+792t^2,  46200+48960t+10360t^2,   4200+1624t-144t^2;
 3150+26t^2,          9600t+140t^3,             2520+8t^2;
 50400-32816t+3168t^2,-286440+195840t-55160t^2,16800-2408t-576t^2].
```

For example K3's middle second-column entry is obtained from

`14*(11*(30+20t+12t^2)+2t*(225-66t+5t^2))+110*(-42+2t)`
`=9600t+140t^3`.

This displays the cancellation responsible for the cubic rather than concealing a variable pivot.

Factor8 from rows1 and3,2 from row2, and5 from column2. The total factor is640. The reduced matrix L3 has rows

```
[A,B,C],
[D,2tE,4F0],
[G,J,I],
```

with

```
A=1575+686t+99t^2,       B=1155+1224t+259t^2,
C=525+203t-18t^2,
D=1575+13t^2,           E=480+7t^2, F0=315+t^2,
G=6300-4102t+396t^2,    J=-7161+4896t-1379t^2,
I=2100-301t-72t^2.
```

Thus `det H=-(432/539)det L3`.

Subtract4row1 from row3. The latter becomes

`(-6846t,-11781-2415t^2,-1113t)`
`=-21*(326t,561+115t^2,53t)`.

Factoring-21 gives the final THREE-BY-THREE polynomial matrix

```
J3=
[A, B, C;
 D, 2tE, 4F0;
 326t, 561+115t^2, 53t],
```

and the complete sign/scale is

`det H=(1296/77)det J3`.                                  (1)

All three pivot values(-18,30,14) are nonzero constants; the remaining factors are the explicitly displayed constant row/column scalings. No polynomial root has been excluded.

## 7. Evaluate the WHOLE three-by-three cofactor polynomial

Set z=t^2. The three cofactor brackets in J3 are:

```
(2tE)*(53t)-4F0*(561+115t^2)
 =106z*(480+7z)-4*(315+z)*(561+115z)
 =-706860-96264z+282z^2,

D*(53t)-4F0*(326t)
 =t*(53*(1575+13z)-1304*(315+z))
 =-t*(327285+615z),

D*(561+115t^2)-(2tE)*(326t)
 =(1575+13z)*(561+115z)-652z*(480+7z)
 =883575-124542z-3069z^2.
```

Consequently the COMPLETE determinant, with its middle cofactor minus sign retained, is

`det J3=A*(-706860-96264t^2+282t^4)`
`       +t*B*(327285+615t^2)`
`       +C*(883575-124542t^2-3069t^4)`.

The following evaluated coefficient groups show EVERY multiplication contributing to the sextic. No target coefficient is used to solve for a group:

|power of t|A times first bracket|tB times middle bracket|C times third bracket|SUM|
|---|---:|---:|---:|---:|
|0|-1113304500|0|463876875|-649427625|
|1|-484905960|378014175|179365725|72473940|
|2|-221594940|400596840|-81288900|97713000|
|3|-66037104|85477140|-25282026|-5841990|
|4|-9085986|752760|630531|-7702695|
|5|193452|159285|-623007|-270270|
|6|27918|0|55242|83160|

For example the degree2 first group is `-99*706860-1575*96264=-221594940`; its middle group is `1224*327285=400596840`; its final group is `-18*883575-525*124542=-81288900`. The degree4 first/final groups are `-99*96264+1575*282=-9085986` and `18*124542-525*3069=630531`. Thus the mixed terms have actual arithmetic, not an unevaluated multinomial representation.

Every SUM is divisible by77. Dividing gives

`det J3/77=-8434125+941220t+1269000t^2-75870t^3`
`                         -100035t^4-3510t^5+1080t^6`.

Combining with(1),

`det M(1,t,-2)=1296*(-8434125+941220t+1269000t^2`
`                         -75870t^3-100035t^4-3510t^5+1080t^6)`.  (2)

This is an identity of polynomials in t, not a fit from sample determinants.

## 8. Restore homogeneity and explicitly evaluate all mixed u/v scalars

Since the matrix M is linear in(a,b,c), the determinant is homogeneous degree six. Equation(2) therefore proves

`det M(a,b,-2a)=1296*(-8434125a^6+941220a^5b+1269000a^4b^2`
` -75870a^3b^3-100035a^2b^4-3510ab^5+1080b^6)`.

Initially this follows in the rational-function field by t=b/a; multiplication by a^6 yields a polynomial identity. Hence it is valid also at a=0, with no omitted exceptional parameter set.

Now put a=T/2,b=d/2. Define the normalized highest part by `F6=-det(uU+vV)/43740`, without assuming it equals the author's target. Since1296/64=81/4 and43740/(81/4)=2160, simplifying by135 gives

`16F6=62475T^6-6972T^5d-9400T^4d^2+562T^3d^3`
`                       +741T^2d^4+26Td^5-8d^6`.          (3)

For T=u+v,d=u-v the complete coefficient rows, ordered by decreasing u degree, are

```
T6:    1, 6,15,20,15, 6, 1
T5d:   1, 4, 5, 0,-5,-4,-1
T4d2:  1, 2,-1,-4,-1, 2, 1
T3d3:  1, 0,-3, 0, 3, 0,-1
T2d4:  1,-2,-1, 4,-1,-2, 1
Td5:   1,-4, 5, 0,-5, 4,-1
d6:    1,-6,15,-20,15,-6, 1.
```

The five previously missing scalar evaluations are consequently:

```
16[u5v]F6=374850-27888-18800-1482-104+48=326624,

16[u4v2]F6=937125-34860+9400-1686-741+130-120=909248,

16[u3v3]F6=1249500+37600+2964+160=1290224,

16[u2v4]F6=937125+34860+9400+1686-741-130-120=982080,

16[uv5]F6=374850+27888-18800-1482+104+48=382608.
```

Dividing by16 gives **20414,56828,80639,61380,23913**, respectively. The two pure coefficients are also recovered from the SAME polynomial:

`16[u6]F6=62475-6972-9400+562+741+26-8=47424`,

`16[v6]F6=62475+6972-9400-562+741-26-8=60192`,

giving2964 and3762. They agree with the separate endpoint reductions in S2, but were not used as interpolation conditions.

Restoring the original determinant normalization yields exactly

`det(uU+vV)=-43740*(2964u^6+20414u^5v+56828u^4v^2`
`                    +80639u^3v^3+61380u^2v^4+23913uv^5+3762v^6)`.

No coefficient in the assigned homogeneous degree-six slice remains uncomputed.

## 9. FATAL/MAJOR/MINOR and composition boundary

- **All seven given-pencil degree-six coefficients:** reconstructed by the displayed polynomial elimination/cofactor groups.0F/0M/0m; no discrepancy against S1LF130.
- **Own five mixed obligations from S2:** CLOSED in WRITTEN reconstruction; their earlier NOT_RECONSTRUCTED history remains preserved.
- **Degree1–5/full determinant/all-quadrant sign:** not a new verdict of this return. S3's degree-four data were read as supplied exposure, not silently promoted or reused as an independent result of this proof.
- **Actual D3 column identity, full108-scalar parent composition, invariant source-basis/injectivity and actual3-to5 quotient:** separate gates; no headline promotion under parentv8.
- **Other seven primitive maps, generalF5, H13/B4 authentication, broad Serre problem, formal/human/cross-vendor/novelty acceptance:** not claimed.

This closes only the assigned written degree-six determinant gate, with explicit constant pivots and polynomial homogenization. It grants no scientific execution permission and no retrospective credit to historical unadmitted arithmetic. All author/shared/pinned files and earlier review returns are unchanged.
