# ORIGINAL r1 WHOLE35star — complete s10 integer-lifting nonsingularity certificate

Owner MathKacMoody-2. Preceding verbatim returned metadata clock: **Sun Oct 25 14:54:16 PDT 2026** (`/bin/date`). WRITTEN integer/modular algebra only, NOT an executed replay or formal/kernel check. No scientific interpreter/program/CAS/enumeration/solver/replay/compile/CLI/GO was used. Fresh full reconstruction remains required.

## 1. Exact complete matrix and finite control

Use ALL corrected ACTUAL11 columns in `level5-r1-grade3-35star-matrix-columns-v2.json`, SHA256 `a9d648c0b586247424877bbdfc609ab72339d8d2da99b3ea261cddb667e0f012`, with mandatory K31 correction SHA256 `cd26a23ac2436c4a0d4bd79690b3e985541551cca883ee11bee9961655a01b20`. Basis is(F_A,G_A,F_B,G_B,f_A,f_B,f_C,g_A,g_B,g_C,g_D).

Write N(s)=s(s+2)L3=s^2 C+s D+E, C=13I-A. Set

    H=39I-A-B,
    M=N(10)/9=156I-10A-B=H+9C.                                  (1.1)

The aim is WHOLE11x11 nonsingularity. A singular reduction modulo3 below is NOT an original kernel; the higher lifting obstruction is essential.

## 2. Complete reduction H modulo3 and its exact one-dimensional nullspaces

Directly from the pinned integer A/B columns,

    Hbar=[
      [1,2,0,1,1,2,1,1,0,2,0],
      [1,2,1,2,2,2,2,0,0,0,1],
      [0,0,2,1,0,0,2,0,0,0,0],
      [0,0,2,0,0,0,1,0,0,0,0],
      [1,1,0,1,0,2,0,0,0,0,1],
      [2,0,0,1,0,0,2,2,0,1,2],
      [0,0,0,0,0,0,1,0,0,0,0],
      [0,0,0,0,2,0,0,0,2,2,2],
      [0,2,2,2,1,2,0,1,1,2,0],
      [0,0,0,0,0,0,0,0,0,1,0],
      [2,2,1,2,0,1,0,2,2,2,2]
    ].

Rows7/10 first give x7=x10=0; rows4/3 then give x3=x4=0. In variables(a,b,c,d,e,f,g)=(x1,x2,x5,x6,x8,x9,x11), the remaining seven equations are the COMPLETE matrix

    [[1,2,1,2,1,0,0],
     [1,2,2,2,0,0,1],
     [1,1,0,2,0,0,1],
     [2,0,0,0,2,0,2],
     [0,0,2,0,0,2,2],
     [0,2,1,2,1,1,0],
     [2,2,0,1,2,2,2]].

For transparency, row2-row1 gives c=e-g; row3-row2 gives b=c; dividing row4 by2 gives a=-e-g; row5 gives f=-e. Row1 then gives g=2d, while row6 gives d0 and thus g0. Row7 is consistent. Hence the ONLY homogeneous solutions are

    (a,b,c,d,e,f,g)=(2e,e,e,0,e,2e,0).

Therefore Hbar has EXACT rank10 and right nullspace spanned by

    v=(2,1,0,0,1,0,0,1,2,0,0)^T.                               (2.1)

Direct multiplication also gives the nonzero left null vector

    u=(2,1,2,1,2,0,0,1,0,2,2)^T,
    u^T Hbar=0.                                                (2.2)

Rank10 makes that left nullspace one-dimensional too. This rank proof is a written full-system solution, not a selected minor.

## 3. Exact integer lifts and all needed products

Choose the INTEGER vector

    v1=(0,0,1,1,0,0,1,0,1,1,1)^T,
    w=v+3v1=(2,1,3,3,1,0,3,1,5,3,3)^T.                        (3.1)

The exact integer products, obtained by substituting the pinned columns, are

    Hv=(123,36,-33,9,57,-45,60,36,105,-57,27)^T,
    Hv1=(1,-3,32,60,14,-39,82,-12,64,19,54)^T.

Consequently

    Hv/3=(41,12,-11,3,19,-15,20,12,35,-19,9)^T,
    Hw/9=(14,3,7,21,11,-18,34,0,33,0,21)^T.                    (3.2)

In particular Hbar*v1=-(Hv/3) modulo3, so w is a genuine second lift with Hw divisible by9 in EVERY coordinate. Pairing the displayed INTEGER vectors with u gives

    u^T(Hv/3)=105=0 mod3,
    u^T(Hw/9)=130=1 mod3.                                     (3.3)

The remaining correction is also explicit:

    Cv=(0,1,0,0,0,1,0,2,0,0,0)^T mod3,
    u^T Cv=1+2=0 mod3.                                       (3.4)

No floating point, determinant program or p-adic implementation supplies these identities. All data for their independent written reconstruction are literal above and in the pinned A/B table.

## 4. Elementary contradiction excluding ANY nonzero rational kernel

Assume M is singular over Q. Choose a nonzero INTEGER kernel vector x primitive at3 by clearing denominators and dividing its common power of3. Since Mbar=Hbar has rank10, its nonzero reduction is alpha*v, alpha1or2. Multiplying x by the appropriate integer unit at3 lets us assume x=v+3y.

Reduce Mx0 modulo9. Because M=H+9C,

    Hbar*y=-(Hv/3) mod3.

The complete rank/nullspace result in §2 and the particular lift v1 imply y=v1+beta*v+3z for integers beta,z. Thus

    x=w+3beta*v+9z.                                           (4.1)

Now pair Mx with u and divide by9. Every displayed term is an INTEGER: Mw is coordinatewise divisible by9; Mv by3. Equations(3.3),(3.4) give

    u^T Mv/3=u^T Hv/3+3u^T Cv=0 mod3,
    u^T Mw/9=u^T Hw/9+u^T Cw=1+u^T Cv=1 mod3,
    u^T Mz=0 mod3.

The last equality follows from u^T Hbar0 and Mbar=Hbar. Substitute(4.1):

    0=u^T Mx/9=1+beta*0+0=1 mod3,

a contradiction. Therefore M has NO nonzero rational kernel and is nonsingular. Since it is an integer matrix, this is equivalent to nonzero determinant over R/C as well. Hence N(10)=9M and the WHOLE s10 creator are nonsingular.

This proves a complete fixed-parameter control despite the singular first reduction. It does NOT mistake a rank-deficient modular matrix for an actual kernel, assume a simple root, or suppress a remaining lift. The original quotient implication still uses the full source/local/ideal chain; no stronger mathematical acceptance or process repair is inferred.
