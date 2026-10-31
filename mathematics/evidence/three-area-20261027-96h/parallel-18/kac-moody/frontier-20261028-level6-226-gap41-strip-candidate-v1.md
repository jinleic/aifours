# Level-six (2,2,6) entire-source |r−s|≤41 strip — exact candidate

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 18:48:41 PDT 2026**. This is a NEW unreviewed exact-program-assisted improvement over the separately pinned near-diagonal cofactor cone. It is not a parent disposition, formal/kernel, independent-model/human, novelty or priority verdict.

## 1. Entire actual source and exact new region

For EVERY pair of integers `r,s>=6` with `|r-s|<=41`, and every allowed FULL complex Cartan realization C of the original A(r,s), the candidate is that the entire original D3 map

\[
D_3:P_{(2,2,6)}\longrightarrow S_{(2,2,5)},\qquad
P=\ker f_1\cap\ker f_2\subset S_{(2,2,6)},\quad S=G_C/J,
\]

is injective at the named full-Cartan/free-Levi/PBW and exact-code inputs below. Its actual type125 lowest multiplicity source has dimension34. This strip gives ALL sizes within the finite gap, not only the astronomically large t allowed by the previous cofactor bound. It remains a strict region: no whole r,s>=6 quadrant, other level-six type, F6/B6, arbitrary-GCM/all-level Serre, novelty or priority claim follows.

The previous `frontier-20261028-level6-226-entire-source-cone-candidate-v1.md`, 70LF SHA `e85ae127d0ea3e552dfd5785f9934371650a902cfbf3ab5ba3baf5d9ca0eb9ea`, proved a separate conservative near-diagonal large-t cone at its unreviewed exact source/leading-matrix inputs; the strip and that cone may be unioned **only at those inputs**. Their source description, all historical findings and methodological exposure qualifications are unchanged.

## 2. Source and complete selected determinant

Use the separately written UNREVIEWED full-Cartan/positive-presentation/PBW inputs `frontier-20261028-fixed-levi-level1-independent-v1.md` SHA `a001ed19bce6feda024d8cd4d1fc5267cee2c7349133589bf471090b9a87699a` and `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` SHA `e5ca9ebf34e87a7a37a804330000904375b5bf691aa79cf1601d40f2b483354f`. For r,s>=6, both node-3 Serre seed modules have level at least seven, so the WHOLE original level-six source and level-five target really are the free-Levi spaces. All extra full-Cartan directions remain represented by the actual local h3 action.

The complete degree `(2,2,6)` has 74 Lyndon source words and horizontal rank40, hence 34 full lowest vectors. Their actual f3 table is the original row/ordinary Jacobi table in the previous source, and its selected 34×34 target-word minor is the complete bivariate polynomial `P(x,y)` with

    x=r-6,  y=s-6,  total degree(P)<=34.

P has **592 nonzero coefficients with mixed signs**, 133 positive and459 negative. We do NOT assert its coefficients have a common sign or that it is nonzero on the entire quadrant. The full 592 coefficients, all 74 source words, 34 actual lowest vectors and every affine matrix entry are pinned below. A separate independent replay reconstructs the matrix via tree Jacobi and checks the WHOLE polynomial against exact Fraction-Gaussian determinants at ALL 630 points `(i,j)` with `i+j<=34`. The affine determinant degree bound and unisolvent triangular interpolation grid prove the complete polynomial identity, not merely 630 parameter samples.

## 3. Exact closed-gap sign proof

First suppose `s>=r>=6`, and write `v=r-6>=0`, `g=s-r in [0,41]`, so `x=v,y=v+g`. Group the complete *mixed* polynomial as

\[
P(v,v+g)=\sum_{j=0}^{34} f_j(g)v^j.
\]

Every one of the 35 polynomials `f_j` is explicitly formed by exact binomial expansion. For `m_j=deg f_j`, define

\[
Q_j(z)=(1+z)^{m_j}f_j\!\left(\frac{41z}{1+z}\right).
\]

The new exact certificate lists **all 620 nonzero coefficients** of these 35 polynomials and verifies that EVERY coefficient is strictly negative. For `0<=g<41`, choose `z=g/(41-g)>=0`; all `Q_j(z)<0`, hence `f_j(g)<0`. At the INCLUDED endpoint `g=41`, the leading coefficient of `Q_j` is exactly `f_j(41)` and is also strictly negative. Therefore every term `f_j(g)v^j` is nonpositive and the j=0 term is strictly negative, so `P(v,v+g)<0` for all real `v>=0` and `0<=g<=41`.

Thus this entire 34-source D3 map is injective for all ORIGINAL integer `6<=r<=s` with `s-r<=41`. Exchange nodes1/2, their full Cartan columns/rows and parameters. Degree `(2,2,6)` is fixed by the exchange, so its actual full source/target map for the swapped pair is canonically isomorphic. This gives the full symmetric region `r,s>=6, |r-s|<=41`. **No symmetry of the selected determinant P is assumed**; the second half is obtained from the actual algebra isomorphism.

## 4. Why this is NOT a whole-quadrant determinant proof

The same exact polynomial has

    P(0,0) = -603138104964912067285615430860800000000000000,
    [x^27]P(x,0) = 4217288785920000000 > 0,
    [y^30]P(0,y) = 2071650631680000 > 0.

Each axis polynomial is therefore negative at0 and tends to +infinity; the real intermediate-value theorem gives a positive real zero of THIS SELECTED MINOR on each axis. This is a concrete obstruction to using this one determinant as a global real-quadrant nonvanishing certificate. It is **not** a zero of the full D3 map, a non-Serre element, an integer-parameter witness, a contradiction to the strip (the physical-node exchange can use different target rows), or a proof about other minors. The previously recorded bounded400 one-row alternate search remains exactly a bounded search; no global impossibility is inferred.

## 5. Exact source, independent replay and sign-certificate pins

| Owner-root artifact | LF | SHA-256 |
|---|---:|---|
| `frontier-20261028-level6-free-22-pencil-v1.json` | 6561 | `b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc` |
| `frontier-20261028-level6-free-22-determinant-v1.json` | 2982 | `874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8` |
| `frontier-20261028-level6-free-type-determinant-independent-replay.py` | 60 | `a7ec63e2d3102b08816f9c5c2eb859bf09647eaeb07822c8eb56cc81de19ccf0` |
| `frontier-20261028-level6-free-22-determinant-independent-replay-v1.json` | 18 | `ca69a9d938e1353287e72c89c1fce31601a171ea67f404d928d352605a02e48f` |
| `frontier-20261028-level6-226-gap41-sign-certificate.py` | 57 | `4a9b8f2af6cca4f0919b2dc8d9052176d34b4aed138476de12d8ed51d46b75f1` |
| `frontier-20261028-level6-226-gap41-sign-certificate-v1.json` | 854 | `998c3acbfbe956542fa16f95cf0506af29db0fd51401eec59d89a0b7b8eeb35d` |
| source pencil producer `frontier-20261028-level6-free-type-pencil.py` | 49 | `7bfff385efe2819f6c627fe3a7ed476ead71487cc6ff920dafbab355a8614e76` |
| polynomial producer `frontier-20261028-level6-free-type-determinant.py` | 33 | `8d168126cea3a1df08cb0f0d54836eacf1d65378f5203b83ba9ac3f178ef4c64` |
| separate tree engine `frontier-20261028-levi-critical-independent-replay.py` | 263 | `4b79f8cb58e34a28fdd9c046e3cc91d4619c971bbc8d5c6e059ff1c54e79bae6` |

The independent full-polynomial replay actually returned `PASS level6 (2, 2, 6) source 74 lowest 34 grid 630 terms 592` at **18:48:33 PDT**. The sign checker returned `PASS closed gap<=41: 35 coefficient functions, 620 strictly negative transformed terms; both selected-minor real axis roots` at **18:48:41 PDT 2026-10-28**. It uses exact integer/Fraction only. Both are independently authored same-owner computation paths with shared generic helpers, not human/formal/independent-model verification. The earlier older-cone status-description exposure is explicitly disclosed in the 125-cone candidate and remains attached; no held guide is a premise.

The exact 41 bound is a proved bound for this coefficient certificate, not a statement of maximality of the true feasible region. Independent scientific/source/code review and parent decision are pending.

**END — entire actual type125 map on the exact |r−s|≤41 strip, candidate only.**
