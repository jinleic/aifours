# Level-six (4,4,6) entire-source large-row cone — exact candidate

**MathKacMoody-2 / math-3.** Native observation before this additive write: **Wed Oct 28 18:31:04 PDT 2026**. This is a NEW exploratory, exact-program-assisted candidate outside the registered level-four target and outside the candidate F5/B5 level-five band. Its separately authored replay is CURRENTLY RUNNING, not yet returned; full independent scientific review, parent adoption, human/formal/kernel/novelty/priority gates are all pending.

## 1. Exact claimed region — not all level six

For any integers `r,s>=6` and every allowed FULL complex Cartan realization of the original `A(r,s)`, let `S=G_C/J` be the actual original Serre quotient and

\[
P=\ker(f_1)\cap\ker(f_2)\subset S_{(4,4,6)}.
\]

Set `t=(r+s)/2`, `d=(r-s)/2`. At the unreviewed source/PBW and exact leading-matrix inputs below, the candidate is that the ENTIRE original map

\[
D_3:P_{(4,4,6)}\longrightarrow S_{(4,4,5)}
\]

is injective whenever the explicit exact inequality

\[
t>C\left(\frac{13655}{27}|d|+\frac{114599}{81}\right)\tag{1}
\]

holds, where

\[
C=\frac{162^2\,161!\,(37184/27)^{161}}{\Delta},\qquad
\Delta=527253154492450281362499347901675627491900331462363707491032596767530614784000000000000000000000000000000000000000000000000000>0.\tag{2}
\]

No numerical rounding or optimizer output is involved. For every fixed integral difference `r-s`, sufficiently large integers r,s satisfy (1), so this is a genuine unbounded cone of parameters, albeit with a deliberately very conservative constant. It does NOT settle the entire r,s>=6 quadrant, any other level-six type, B6, F6, all-level Serre, the whole book problem, novelty or priority. The source degree `(4,4,6)` has total height14 and is not the level-five invariant quotient.

## 2. Entire actual source and exact local pencil

The necessary UNREVIEWED full-Cartan/positive-presentation/PBW inputs are `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`. They give the actual positive source after the repeated-1/2 relations as `n_+(sl3) semidirect FreeLie(M)` for the actual adjoint eight M, including every full-Cartan direction. Each remaining node-3 Serre seed has level `r+1` or `s+1`. Since `r,s>=6`, **both entire node-3 ideals vanish in levels<=6**. Therefore BOTH the whole level-six source and the whole level-five target here are the corresponding free-Levi spaces. This statement is limited to this parameter region and does not infer any global Serre equality.

At `(4,4,6)`, the horizontal weight is `(-2,-2)`, a 27-type lowest weight. The exact program constructs all 1116 free-Lie Lyndon words in this fixed degree, applies both complete horizontal lowerings, and finds their entire joint kernel has dimension 162. A separate exact character calculation gives the same dimension: for the eight weights of M, the Witt formula is

\[
\operatorname{ch}L_6(M)=\tfrac16(\chi^6-\psi_2(\chi)^3-\psi_3(\chi)^2+\psi_6(\chi)),
\]

and the six-term `sl3` lowest-weight coefficient is `m(4,4)-m(3,4)-m(4,3)+m(2,3)+m(3,2)-m(2,2)=162`. Here `m(a,b)` is the corresponding coefficient of that character. This is ordinary Witt/Weyl representation theory plus exact integer coefficient arithmetic, not an independent formal proof.

For the same actual eight letters, use the full original local bracket

    [f3,m_j]=(-h3,-r e1,-s e2,-(r+s)e12,-s e12,0,0,0)_j,
    [h3,m_j]=(2-r a_j-s b_j)m_j,

and ordinary Jacobi on every full source vector. The resulting matrix is exactly affine in r,s. Let `E=D(0,0)`, `L=D(1,1)-D(0,0)` and `K=D(1,0)-D(0,1)` **as formal coefficient extractions in that polynomial identity**, not as physical parameter assumptions. Then

\[
D(r,s)=tL+dK+E.
\]

The recorded 162×162 target-word minor of L has the exact positive determinant `Delta` in (2). Its entrywise maxima are

    max|L_ij|=37184/27,   max|K_ij|=13655/27,   max|E_ij|=114599/81.

The complete 1116 source words, 162 rational kernel vectors, 162 target word pivots and ALL 26244 triples `(L_ij,K_ij,E_ij)` are in the pinned JSON. The local determinant is on the entire joint lowest source, not a selected few input vectors. No positivity or invariant form for the full nonsymmetrizable algebra is assumed.

## 3. Written cofactor inequality

Let `n=162` and `M=37184/27`. Every cofactor of the selected leading matrix has absolute value at most `(n-1)! M^(n-1)` by the Leibniz formula. Hence

\[
\|L^{-1}\|_\infty\le n(n-1)!M^{n-1}/\Delta.
\]

The perturbation satisfies

\[
\|dK+E\|_\infty\le n\left(|d|\,13655/27+114599/81\right).
\]

Thus (1) is exactly the strict sufficient condition

\[
\|L^{-1}(dK+E)/t\|_\infty<1.
\]

The geometric-series/maximum-coordinate argument makes `tI+L^-1(dK+E)` invertible over C, so `tL+dK+E` has a nonzero 162×162 minor and original D3 is injective on ALL of P. The condition is an explicit bound, not an optimal cone or a point-sampled assertion. No prior coefficient table or prior rank result is a premise.

## 4. Exact evidence and pending separate replay

`frontier-20261028-level6-446-leading-map-cone.py`, 78LF SHA `6afcb48e764b80dd687838a11c87a6cc51639b27ddfc75796e3a19052f520829`, generated the full source, entire horizontal kernel, formal-affine coefficient matrices, rank and row-cleared exact Bareiss determinant. Its **222265LF/3804504B** data `frontier-20261028-level6-446-leading-map-cone-v1.json` SHA `606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed` contains every coefficient and target pivot. Actual command returned `full source 1116 horizontal kernel 162` and `DONE LEADING_INJECTIVE_COFAC_CONE leading rank 162 of 162`, followed by native **Wed Oct 28 18:30:26 PDT 2026**. All mathematics is integer/Fraction.

A separately authored verifier `frontier-20261028-level6-446-leading-map-independent-replay.py`, 71LF SHA `4f473fe6c549888e5972333a7e94cf624ddb931d64ea16deaf2644fdcb89ae26`, is **still running as of the prewrite observation**. It is intended to rebuild the lowest multiplicity using Witt/Weyl coefficients, verify every source vector and entry with separate matrix-unit/tree-Jacobi code, and recompute the determinant via Fraction Gaussian elimination. Its mere launch grants NO verification credit; any later result must be a separate additive receipt. Even a PASS would remain same-owner/local-code, not independent-model/human/formal verification.

## 5. Exposure and history

During an earlier broad search for the level-five coordinate boundary, a status description of an older cone-style approach was incidentally displayed. No exact wall clock was recorded for that search. This is prior methodological exposure, not a blind/cognition-independence claim. The held underlying guide is NOT an accepted premise and was not read for this calculation; the new local bracket, source basis, leading matrix, determinant and cofactor constant above were freshly constructed and checked by the explicitly pinned new program. Prior ZERO/STOP/HOLD and process findings remain unchanged, and no old conclusion or priority is authenticated.

**END — exact full-source level-six cone candidate; independent replay and full scientific review still pending.**
