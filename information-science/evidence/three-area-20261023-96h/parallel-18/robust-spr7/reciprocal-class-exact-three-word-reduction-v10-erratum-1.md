# Additive erratum 1 to the 194LF reciprocal three-word reduction

Actual returned `/bin/date` BEFORE this write: **Sun Oct 25 21:46:45 PDT 2026**. Owner InfoSPR7-2. Additive correction only. The pinned source `reciprocal-class-exact-three-word-reduction-v10.md`, SHA256 `f19221c04fa29ae4ec5d3c4616efd1779bf6ff8e2241763dfa73fae1818ebfb7`, is NOT edited. Written symbolic reasoning only; no scientific execution.

## The overstated sentence

In §4, under "Equation-free chart for W_I", the source says that several sign facts are automatic. It lists **"F>0 at d0"** among them and concludes `x1∈(d0,r)`. That part is WRONG as stated.

What is actually automatic in that chart:

- F<0 at r, s and w. There P2=0 while P3>0, because P3's only positive roots are c and 1/c.
- F(c)>0, because P3(c)=0 while P2(c)>0.
- F(1/c)≥0, because P3(1/c)=0 while P2≥0.

F(d0) is NOT automatic. Given the required factorization F=E_B·Δrev with Δrev>0 on t>0, the condition F(d0)>0 is EQUIVALENT to d0 lying in (0,x1)∪(x2,x3). This is exactly the C4-cell condition d0<x1, and it must be IMPOSED.

## Corrected statement

Width positivity requires F(0)=2w2>0. Together with F(r)<0, this forces x1∈(0,r). The other forced locations are unchanged: x2∈(s,c) and x3∈[1/c,w).

The cell condition `d0<x1` is a genuine filter. It is already part of the word-I chain `eL1<d0<min(x1,oL1)`, which is stated in §3 and imposed in the W_I definition through the cell/orientation chain. So the DEFINITION of W_I, the sufficiency theorem, the conditional necessity and the dimension count are all UNCHANGED. Only the parenthetical "automatic consistency" list was overstated.

## Scope

No other sentence of the 194LF source is affected. In the same pass I rechecked, in writing, every other sign and band statement:

- the C3-lead location (0,eL1);
- all orientation bands;
- ΔE and ΔO;
- the cells above 1;
- κ_j=y_ju_j;
- condition 5 in the admission proof.

This is an owner self-recheck, not an independent review or acceptance. Any gate of the v10 source must read this erratum together with it. All permanent process findings, the zero-probe credit, HOLD, and the original cutoff/deadline are unchanged.
