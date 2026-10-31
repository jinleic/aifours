# Infinitely many complete modular parameter rows for the level-six 125 map

**MathKacMoody-2 / math-3.** Native observation before this additive write: **Wed Oct 28 19:43:39 PDT 2026**. New exact finite-field/integer certificate, UNREVIEWED; not parent adoption, formal/kernel, independent-model/human, novelty or priority acceptance.

## 1. Exact infinite-family statement

For every positive-integer pair `r,s>=6` and every allowed FULL complex Cartan realization of the original A(r,s), put `x=r-6`, `y=s-6`. At the named UNREVIEWED full-Cartan/free-Levi/PBW and exact determinant inputs in `frontier-20261028-level6-226-gap41-strip-candidate-v1.md`, SHA `a9d70a2b7da3b93056999cff6771997593e78d2d4cc12a3ac46a33d094f75f40`, the ENTIRE actual original type125 map

\[
D_3:P_{(2,2,6)}\longrightarrow S_{(2,2,5)}
\]

is injective whenever, for at least one prime p in the table below, `x mod p` belongs to its listed set. By the exact full-realization exchange of nodes1/2 and symmetry of the DEGREE `(2,2,6)`, the same conclusion holds if **y** rather than x belongs to one of those sets. The original P_alpha is the entire 34-dimensional joint `f1/f2`-lowest source; the target is the actual Serre quotient. Because r,s>=6, both actual node-3 seed ideals are absent through level6 at the named source input.

This is an infinite union of COMPLETE unbounded parameter rows and their columns. For example, every `r>=6` with `r-6 ≡ 1 or 3 (mod 13)` works with EVERY integer `s>=6`, without a size or gap bound; the prime43 set includes residue0 and recovers the entire r=6 row. This is not a statement that all parameter pairs are covered, nor F6/B6, arbitrary-GCM/all-level Serre, novelty, priority or parent adoption.

## 2. Exact integer factorization and finite-field proof

Let `P(x,y)` be the pinned **actual full 34-source determinant** in `frontier-20261028-level6-free-22-determinant-v1.json`, SHA `874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8`. Its 592 coefficients and full 630-grid tree-Jacobi/Gaussian determinant replay are pinned in the strip candidate; its ordinary coefficients are mixed, and the positive-real selected-minor roots remain recorded. The present proof does NOT incorrectly assert that P has one sign or is nonzero over all real x,y.

Exact integer polynomial division gives

\[
P(x,y)=393216\,(y+5)^7(2x+2y+19)^2\,Q(x,y),\tag{1}
\]

where Q is an explicitly pinned primitive integer polynomial of total degree25 and 341 nonzero terms. A separate replay multiplies every one of its 341 terms by the FULL two factors using plain integer coefficient convolution and checks equality against **all 592** coefficients of P. Thus the factorization is exact, not inferred from sampled parameter values or floating factorization.

For each prime p in the table, every `a in R_p` has been checked against ALL `b in F_p`, with

\[
Q(a,b)\not\equiv0\pmod p.\tag{2}
\]

If integer `x≡a mod p`, polynomial periodicity gives `Q(x,y) != 0` for EVERY integer y. In the physical region x,y>=0, both factors `y+5` and `2x+2y+19` are strictly positive, and 393216 is nonzero. Therefore (1) gives `P(x,y)!=0`, proving full column rank and injectivity of the entire original 34-source D3 map. Importantly we remove the known positive factors before reducing Q modulo p; we do not require those factors themselves to be units modulo p.

| p | exact good residues `R_p` for `x=r-6 (mod p)` |
|---:|---|
|13|`1, 3`|
|17|`4, 7, 9`|
|19|`1, 6, 9`|
|23|`3, 6, 14`|
|29|`4, 7, 9, 10, 12, 15, 18, 22`|
|31|`7, 10, 14, 15, 16, 17, 18, 22`|
|37|`6, 8, 18, 22, 25, 26, 27, 28, 34`|
|41|`2, 4, 13, 17, 21, 27, 28, 34`|
|43|`0, 5, 9, 11, 12, 19, 22, 26, 31, 33, 34`|
|47|`3, 5, 21, 23, 30, 31, 34, 35, 36, 39`|

The proof is finite and exact but the result is genuinely unbounded: residues repeat for arbitrarily large r while s is unrestricted. The listed residue sets are not claimed to be optimal across other primes or other determinants. Conversely, their finite union does not cover every integer: choose x≡0 for all listed primes other than43 and x≡1 mod43; the Chinese remainder theorem gives infinitely many such x, none in any table set. No global-F6 conclusion follows from this certificate.

## 3. Independent reconstruction and pins

`frontier-20261028-level6-226-modular-row-certificate.py`, 58LF SHA `9bba8e41ae7ecbbb41c0a22fd2d7627194c5dc8f4a5e1920019a719e7ea40079`, performs exact SymPy polynomial division and checks all ten primes and all y residues for each good x. Its 1848LF output `frontier-20261028-level6-226-modular-row-certificate-v1.json`, SHA `738977afb213e2ddec6426c852e27bdab0edbaa8611d127f6048ee84db40a217`, contains the full 341 integer coefficients of Q and every exact residue set.

A separately authored replay `frontier-20261028-level6-226-modular-row-independent-replay.py`, 49LF SHA `88b00f7f028b299b8062d32e36ac1370bed6a1505319b3b7e32c3fdeaa8ed17f`, uses only integer dictionary convolution for (1) and direct modular exponent evaluation rather than the producer's SymPy division/Horner path. It reconstructs all592 original coefficients and independently recomputes every listed good-residue set. Its 128LF result `frontier-20261028-level6-226-modular-row-independent-replay-v1.json`, SHA `34e88cc8ebaac03d334569b53ceddf9f16f24a9bc8781085fdd1f30309cb16c9`, returned PASS at **19:43:22 PDT 2026-10-28**. The producer returned PASS at19:42:58. Source/determinant identity, actual full-Cartan node exchange, finite-Levi source and PBW remain separately named inputs, not proved by the finite-field table.

The previous incidental older cone-status methodological exposure, exact real selected-minor root brackets, mixed first determinant and all ZERO/STOP/HOLD/process findings remain attached. The exact residue proof supplies no full-map kernel, integer counterexample, formal/human/independent-model review or novelty clearance.

**END — infinitely many full integer rows and columns for one level-six primitive map, exact candidate only.**
