# ORIGINAL r1 WHOLE35star: written nonzero leading-matrix certificate modulo31

Owner MathKacMoody-2. Preceding verbatim returned metadata observation: **Sun Oct 25 14:35:53 PDT 2026** (`/bin/date`, completed metadata job bg_172).

**WRITTEN finite-algebra certificate CANDIDATE, NOT an executed replay or formal/kernel check.** Every elimination below was hand-derived. No scientific interpreter/program/CAS/enumeration/solver/replay/compile/CLI/GO was used. Fresh complete reconstruction is still required before acceptance.

## 1. Exact pinned actual matrix and statement

Input is the COMPLETE corrected ACTUAL11 source matrix `level5-r1-grade3-35star-matrix-columns-v2.json`, SHA256 `a9d648c0b586247424877bbdfc609ab72339d8d2da99b3ea261cddb667e0f012`. Its basis is(F_A,G_A,F_B,G_B,f_A,f_B,f_C,g_A,g_B,g_C,g_D), with the exact actual12-to11 source relation already imposed. The mandatory K31 mathematical erratum is `level5-r1-grade3-35star-K31-erratum-v1.json`, SHA256 `cd26a23ac2436c4a0d4bd79690b3e985541551cca883ee11bee9961655a01b20`. No wrong frozen assay is used standalone.

Write the actual matrix as F_y=(s^2 I+s A+B)/(s+2). The original creator numerator is

    N(s)=s(s+2)L3=s^2 C+s D+E,
    C=13I-A, D=12I+A-B, E=B-16I.

This certificate proves the INTEGER constant matrix C is NONSINGULAR. It does NOT prove N(s) nonsingular at every positive s by itself. All process/exposure/cadence overlays remain mandatory and no earlier finding is repaired.

## 2. The complete integer leading matrix

Directly taking the linear-s coefficients in the pinned columns gives

    C=[
      [21,2,2,2,4,2,0,12,9,6,4],
      [-2,25,-3,-2,-8,-13,-12,0,-6,-6,-5],
      [-15,-15,10,-7,0,3,6,0,-3,-12,-15],
      [3,3,3,30,0,12,12,0,6,6,3],
      [1,-2,0,-2,21,-1,0,-1,-1,-1,-3],
      [5,9,0,1,-24,5,-6,-16,-10,-4,-6],
      [-12,-12,-2,-1,30,15,24,30,15,6,9],
      [0,0,0,0,-1,0,0,29,-1,-1,-1],
      [3,-1,1,1,4,4,2,-4,29,2,-3],
      [6,6,-1,0,-24,-21,-10,-24,-24,9,-9],
      [-1,-1,2,1,12,9,2,12,9,6,29]
    ].

All following entries are in F31, with negative representatives retained for readability. Every pivot is a UNIT. Thus each Schur deletion preserves nonsingularity equivalently; no determinant sign bookkeeping is needed for the nonzero conclusion.

## 3. First sparse pivot and exact10x10 remainder

Use original row8,column5,pivot-1. Its equation gives x5=29x8-x9-x10-x11, hence modulo31 x5=-2x8-x9-x10-x11. Eliminate that coordinate and DELETE row8/column5, retaining the other original orders. The exact10 remainder is

    M10=[
      [21,2,2,2,2,0,4,5,2,0],
      [-2,-6,-3,-2,-13,-12,-15,2,2,3],
      [-15,-15,10,-7,3,6,0,-3,-12,-15],
      [3,3,3,-1,12,12,0,6,6,3],
      [1,-2,0,-2,-1,0,-12,9,9,7],
      [5,9,0,1,5,-6,1,14,-11,-13],
      [-12,-12,-2,-1,15,-7,1,-15,7,10],
      [3,-1,1,1,4,2,-12,-6,-2,-7],
      [6,6,-1,0,10,-10,-7,0,2,15],
      [-1,-1,2,1,9,2,-12,-3,-6,-14]
    ].

Columns here are original1,2,3,4,6,7,8,9,10,11; rows are original1,2,3,4,5,6,7,9,10,11.

For EVERY subsequent displayed step: positions refer to the CURRENT matrix. Swap the selected pivot column with its FIRST column, eliminate below/above it by row subtraction (scaling by the unit pivot inverse), then delete the pivot row and first column. Keep the relative order of other rows and the remaining swapped columns. This explicitly fixes all column orders, including nonadjacent swaps.

## 4. Unit pivots10through7

From M10 select row5,column1,pivot1. The exact remainder is

    M9=[
      [13,2,13,-8,0,8,2,-1,8],
      [-10,-3,-6,-15,-12,-8,-11,-11,-14],
      [-14,10,-6,-12,6,6,8,-1,-3],
      [9,3,5,15,12,5,10,10,13],
      [-12,0,11,10,-6,-1,0,6,14],
      [-5,-2,6,3,-7,12,0,-9,1],
      [5,1,7,7,2,-7,-2,2,3],
      [-13,-1,12,-15,-10,3,8,10,4],
      [-3,2,-1,8,2,7,6,3,-7]
    ].

Select row7,column2,pivot1, giving

    M8=[
      [3,-1,9,-4,-9,6,-5,2],
      [5,15,6,-6,2,14,-5,-5],
      [-2,-14,11,-14,14,-3,10,-2],
      [-6,15,-6,6,-5,-15,4,4],
      [-12,11,10,-6,-1,0,6,14],
      [5,-11,-14,-3,-2,-4,-5,7],
      [-8,-12,-8,-8,-4,6,12,7],
      [-13,-15,-6,-2,-10,10,-1,-13]
    ].

Select row1,column2,pivot-1, giving

    M7=[
      [-12,-14,-4,-9,11,13,-6],
      [-13,9,11,-15,6,-13,1],
      [8,5,8,15,13,-9,3],
      [-10,-15,12,-7,4,13,5],
      [3,11,10,4,-8,-12,-15],
      [-13,8,9,11,-4,10,14],
      [4,14,-4,1,13,12,-12]
    ].

All numbers are the ordinary Schur differences modulo31, not sampled floating-point pivots.

## 5. Unit pivots7through4

Select row7,column4,pivot1 in M7. The exact remainder is

    M6=[
      [-12,-9,-7,4,-3,10],
      [2,13,-15,15,12,7],
      [12,6,10,4,-3,-3],
      [-10,15,-13,2,4,14],
      [-14,-5,-13,2,2,2],
      [9,-9,5,8,2,-9]
    ].

Select row2,column1,pivot2; its inverse is16 modulo31. This gives

    M5=[
      [7,-4,1,7,-10],
      [-10,7,7,-13,-14],
      [-13,5,15,2,-13],
      [-7,6,14,-7,-11],
      [10,-5,-13,10,6]
    ].

Select row1,column3,pivot1, giving

    M4=[
      [4,3,0,-6],
      [3,6,-10,13],
      [0,-12,-12,5],
      [5,8,8,0]
    ].

For example the last operation first swaps M5 columns1/3, using pivot row(1,-4,7,7,-10); subtraction leaves exactly the four displayed rows. This specifies the otherwise easy-to-misread column order.

## 6. Final written determinant, and the exact conclusion

Select row1,column1,pivot4 in M4, inverse8 modulo31. The exact final remainder is

    M3=[[-4,-10,2],[-12,-12,5],[12,8,-8]].

Its INTEGER determinant calculation is

    -4*(96-40)+10*(96-60)+2*(-96+144)
       =-224+360+96=232=15 mod31 !=0.

Every preceding pivot was nonzero, so C is nonsingular over F31. Hence its integer determinant is NONZERO, and C is nonsingular over Q/R/C. This does not turn the written elimination into a machine-checked or independent verification; the complete data/row rules above are supplied for that future written gate.

The implication for the original family still requires the separate matrix/source/local-ideal chain. At this point the established candidate fact is exactly nonzero leading coefficient of det N(s), not all-positive-s injectivity. No process finding, actual finite boundary or stronger acceptance gate is erased.
