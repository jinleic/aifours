# v35-D — determinant-only review of the displayed six-by-six Kac pencil

Reviewer **MathSun8-2 / math-6**. Actual preceding clock: **Sun Oct 25 05:03:13 PDT 2026** (`/bin/date`). **Strict WRITTEN work only.** No scientific interpreter/eval/arithmetic program, enumeration, symbolic program, solver or replay was used. Metadata clocks/hashes/source reads only. The v32-G review was delivered first; no prior assigned review is dropped.

## 1. Verdict: full determinant gate NOT_RECONSTRUCTED

**The requested full determinant identity and all-quadrant sign are NOT_RECONSTRUCTED by this return. This is a MAJOR unresolved acceptance/reconstruction gate, not an established counterexample or an identified wrong author coefficient.** I do not label the copied positive triangle PASS and do not infer full rank from a specialization.

Independently reconstructed below:

- The zero constant term.
- An exact determinant-preserving column reduction whose entire distinguished column is linear in u,v and has no constant part.
- The exact two degree-one determinant coefficients, including their signs and magnitude, through a traceable five-by-five/four-by-four/three-by-three cofactor calculation.
- An exact coefficient-grouping identity specifying the remaining finite obligations without relying on a historical program.
- The scalar identity det(2M)=64 det(M), but NOT the full assertion det(2M)=-2799360P.

**Still NOT_RECONSTRUCTED: all25 coefficients of total degrees2–6.** Section5 lists them individually. Consequently no proof here that the displayed pencil is nonsingular throughout r,s≥2, and no D3/invariant quotient acceptance follows.

Mathematical counterfindings: no FATAL error, wrong arithmetic coefficient or wrong source normalization is established. The MAJOR is the unclosed LOAD-BEARING determinant reconstruction; it is not silently converted into a no-defect full verdict. The column-to-actual-D3 gate is outside this assignment entirely.

## 2. Scope, exposure, complete coverage and pins

This is the explicitly disclosed SAME-DOMAIN substitution: math reviewer / math author, supplied proof, not blind or independent-family review. Other reviewers own the independent source/detector column slices. I treat the displayed matrix as GIVEN, as required, and make no claim that its36 affine entries actually equal D3 source images.

Use **F** for `level5-full-invariant-quotient-v1.md` and **J** for `level5-full-invariant-arithmetic-v1.json`. All144LF of F and64LF of J were read through the complete mandatory222-line literal packet; no truncated proof line was left unread. Exact v35-D entry, metadata receipt and parentv7 were read before the ACK/body reconstruction.

Fresh hashes:

- F: `a539f8b96afa6314367db190ae38bbd9c2f33afc517c2e96f5eb7a7d731129aa`.
- J: `6a22a92ae52d82b6dd86488ed713170efa747ad6858722750da9788ed9a4c85b`.
- Literal packet: `9191ea7c80ae16820ef137d1a724e8f71b8173d07fa8b7b749dd1ca79ceb156e`.

Line references below are ORIGINAL SOURCE lines. Source matrix is F102–107/J28–33; parameter substitution F113–115/J35; claimed determinant triangle F119–132/J36–53. The historical kernel booleans and copied triangle are NOT proof premises. Parentv7 withdraws their executable-verification/retroactive-admission credit.

## 3. Exact column reduction and the constant term

Let C_j denote column j of the displayed M(a,b,c), with

    a=1+(u+v)/2, b=(u-v)/2, c=-(u+v).

Replace column2 by

    K=2C_1+C_2-3C_4.

Adding the other columns to column2 preserves the determinant. Direct affine subtraction from the GIVEN matrix gives

    K=[18b+9c;
       -30b-9c;
       -30b-27c;
       -24b-21c;
        24b+15c;
        42b-27c].

After substitution this is exactly

    K=3u*k_u+3v*k_v,
    k_u=(0,-2,4,3,-1,16)^T,
    k_v=(-6,8,14,11,-9,2)^T.

For example the first entry is9(2b+c)=-18v, and the fourth is-3(8b+7c)=9u+33v; all six follow by the same literal subtraction. Therefore the determinant's constant term is zero, independently of the copied table. This is a formal polynomial expansion at u=v=0, not a claimed r=s=1 theorem in the r,s≥2 assignment domain.

At that origin M=A, where A=3A0 and

    A0=
    [ 0 -9 -27 -3 -3 -27;
     -6  3 -15 -3 -7  12;
      3 12  21  6  7  33;
      0  9   9  3  2   3;
      0 -12 -9 -4 -2  -3;
      3 12  21  6  3  27].

The reduced column2 is zero because 2A0[:,1]+A0[:,2]-3A0[:,4]=0. A left null vector is

    ell=(6,2,-1,48,36,5)^T.

This can be verified by six short column dot products. To derive it rather than guess it, write the left null equations: l3+l6=2l2, l4=3l1-3l2+l5, l5=6l1, 4l3=7l2-3l1, and2l3=6l1-19l2. They give l1=3l2, l3=-l2/2, l6=5l2/2, l5=18l2, l4=24l2, yielding the displayed primitive vector at l2=2.

## 4. Exact degree-one terms and their scale

### 4.1 One cofactor fixes the complete cofactor vector

Delete row3 and column2 of A0. Its five-by-five minor is

    B=
    [ 0 -27 -3 -3 -27;
     -6 -15 -3 -7  12;
      0   9  3  2   3;
      0  -9 -4 -2  -3;
      3  21  6  3  27].

Replace row2 by row2+2row5, giving (0,27,9,-1,66). Expansion in column1 leaves three times the four-by-four determinant

    D=
    [-27 -3 -3 -27;
      27  9 -1  66;
       9  3  2   3;
      -9 -4 -2  -3].

Replace row1 by row1+row2 and row4 by row4+row3. Row4 becomes (0,-1,0,0). Thus

    det D=-det[0 -4 39; 27 -1 66; 9 2 3]
         =-[4(81-594)+39(54+9)]
         =-405,
    det B=3*(-405)=-1215.

The row3/column2 cofactor sign is minus, so the corresponding A0 cofactor is+1215. Scaling five retained rows by3 gives the A cofactor+3^5*1215=295245. In particular rank A is exactly five: its determinant is zero and this five-minor is nonzero.

The cofactor vector of the replaced column2 lies in the one-dimensional left kernel. Since ell3=-1, it is

    cof_2(A)=-295245*ell.

The replacement of column2 has not changed its cofactors, which use only the other five columns.

### 4.2 Both linear coefficients

Because K has zero constant part, the entire degree-one determinant comes from K's linear part and the other columns' constant parts. The two dot products are

    ell^T k_u= -4-4+144-36+80=180,
    ell^T k_v= -36+16-14+528-324+10=180.

Therefore

    [det M]_degree1
      =-295245*3*180*(u+v)
      =-159432300*(u+v)
      =-43740*3645*(u+v).

Thus BOTH displayed degree-one coefficients and their common scale agree with the source, by an actual written determinant derivation. This does NOT establish the higher-degree identity merely by fixing a scale at one point.

The separate scaling identity det(2M)=2^6 det M is immediate by row scaling, and64*43740=2799360. It does not supply any of the missing higher-degree coefficients.

## 5. Exact all-coefficient grouping, and the25 unclosed obligations

Write the GIVEN pencil as

    M(u,v)=A+uU+vV,
    U=(M_a+M_b-2M_c)/2,
    V=(M_a-M_b-2M_c)/2,

where M_a,M_b,M_c are the three literal coefficient matrices in F102–107. The distinguished column is replaced as in §3; all other five columns remain their original A_j+uU_j+vV_j. Let O={1,3,4,5,6}.

For disjoint S,T⊂O, let D_k(S,T) be the six-by-six determinant with column2 equal k and, at each other column j, U_j if j∈S, V_j if j∈T, and A_j otherwise, in the ORIGINAL column order. Multilinearity gives the EXACT polynomial coefficient formula

    [u^p v^q]det M
      =3*sum_(S,T disjoint, |S|=p-1, |T|=q) D_(k_u)(S,T)
       +3*sum_(S,T disjoint, |S|=p, |T|=q-1) D_(k_v)(S,T).

An impossible negative cardinality gives an empty sum. This is a traceable reduction to specified rational/integer determinants, not an executable calculation and not a completed evaluation of those sums. It proves the constant term vanishes and that total degree is at most six; §4 evaluates exactly its p+q=1 cases.

The following higher-degree EVALUATIONS remain **NOT_RECONSTRUCTED**, with source-normalized coefficients listed solely to specify the exact unmet equalities, NOT as verified positive results:

| Degree | Monomials, in decreasing u-degree | Source's claimed coefficients of P; ALL unverified here |
|---|---|---|
|2|u²,uv,v²|17496;38718;18306|
|3|u³,u²v,uv²,v³|33561;114804;118341;36774|
|4|u⁴,u³v,u²v²,uv³,v⁴|32184;148365;239004;158895;36972|
|5|u⁵,u⁴v,u³v²,u²v³,uv⁴,v⁵|15438;89052;195747;202992;99540;18621|
|6|u⁶,u⁵v,u⁴v²,u³v³,u²v⁴,uv⁵,v⁶|2964;20414;56828;80639;61380;23913;3762|

For each entry the literal unclosed obligation is that its coefficient-grouping sum above equals **-43740 times that number**. These are25 distinct missing scalar identities, not an unspecified “some arithmetic remains.” No alternative full-quadrant factorization or sign certificate was established here. The rational row/column reduction in §§3–4 does not justify importing any of these copied values.

## 6. FATAL/MAJOR/MINOR and composition consequences

- **Constant/affine reconstruction:** 0F/0M/0m at the exactly displayed zero/degree-one scope.
- **Full determinant, zero/scale plus all27 nonconstant coefficients:** **NOT_RECONSTRUCTED; MAJOR load-bearing acceptance gap** because25 coefficients remain unproved by this review. No FATAL contradiction or wrong coefficient has been demonstrated.
- **Uniform sign for every r,s≥2:** **NOT_RECONSTRUCTED**, since neither the full polynomial identity nor an alternative exact all-quadrant sign argument is supplied.
- **Pencil equals actual D3 source images:** OUT OF SCOPE, no verdict. The disjoint v35-A/B/C source/detector slices cannot be replaced by this determinant review, even if its determinant gate were later closed.
- **Full invariant/actual3→5 quotient:** NOT accepted by this return. It requires all four actual gates and parent composition. Positive copied coefficients, J's boolean checks and the single r=s=2 determinant do not discharge them.

Source execution descriptions F5,F132/J47–54 remain subject to parentv7; no unadmitted program output is retroactively admitted or replayed. This return does not claim mathematical falsity merely because it cannot supply the missing full written evaluation. It preserves the exact unresolved gate for a future written derivation. No source/author/shared file was changed, no scientific execution was launched, and no formal/kernel, human, cross-vendor, independent-family or novelty acceptance is implied.
