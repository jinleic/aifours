# All four published isolated order-eight classes: no Fourier transversal

**PRIMARY-SOURCE-CONDITIONAL, RATIONAL-INTERVAL AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 22:18:46 PDT 2026**. The four isolated classes listed in [Valtonen §3.2](https://arxiv.org/html/2505.22947v1#S3.SS2) are `A_8A, A_8B, V_8A, V_8B`. Their cyclic Fourier products have NO orthogonal transversal under any source-row order, row/column gauges and column relabellings, regardless of repeated rays. This is NOT an all-order8 or universal-even theorem.

## 1. The A pair

The source's A_8A and its conjugate A_8B are excluded by the exact field/halfgraph packet `frontier-20261028-isolated-a8a-nonbutson-no-transversal-v1.md` SHA **cec28eca986f9a33bb8d77c196315cfc918a0133067fcb1a948fb60d766f0a18**: 35 normalized halfgraphs each have an isolated vertex or two leaves sharing a neighbor, independently rechecked in Z[i,sqrt2]. Its gauge-invariant cross-ratio argument places that class outside all finite Butson monomial classes.

## 2. The V pair and exact source assumption

The source defines V_8B=V_8(a,b,c) and V_8A=V_8B†, with explicit unit algebraic phases given by Proposition3.1. We use that proposition as the NAMED IMPORT that the stated matrix is a complex Hadamard; our interval enclosures merely contain all expected zero/full norm values and are NOT by themselves a proof of equality. Source-row/column permutations and unit gauges preserve the no-T statement after quantifying all source-row orderings.

For V_8B, and separately for its transpose, an exact outward interval computation considers ALL70 four-row halves. For each half and each of28 column pairs, it retains an edge whenever the real AND imaginary half-inner-product enclosures both contain0; all other edges are rigorously nonzero and excluded. Every one of the140 retained-edge graphs has at most TWO edges. A perfect matching of eight vertices would require four, so none exists. Thus no transversal exists by pairing physical rows r and r+4 and using the source Hadamard column orthogonality. The transpose result plus global conjugation and physical row reflection covers V_8A=V_8B†.

## 3. Integer enclosures and independent replay

`frontier-20261028-isolated-v8-interval-halfgraphs-v1.py` SHA **d5f4364c8cd02ca706d6963183f3768fe2995d7a1ef0fb20d1000e9d6cd426ae**, certificate SHA **d26cf655ad67c077c0617166369e661e3ad8993e5bcabc5109aa9d070207add1**, uses integer endpoints divided by 10^60, outward-rounded +,−,*,/, and integer `isqrt` for square roots; it never uses floats. The trigonometric constants in the source are enclosed via positive nested-square-root identities for cos(pi/16), sin(pi/16), cos(3pi/16) and cos(pi/8). For EACH orientation the retained-edge histogram over70 halves is

```text
0 possible edges: 50 halves; 1 possible edge: 16; 2 possible edges: 4.
```

A separately written replay `frontier-20261028-isolated-v8-fraction-replay-v1.py` SHA **4dc2b95e9864fd9b2a7157de5696436425c2479dbc6e4b35d8df36ef80feedf3**, result SHA **a1e78837fd7b7e1af863cc7cbe09190e944087cab7c3e41242fec126570cf012**, uses exact Fraction interval endpoints and independently rounded square-root bounds at denominator10^45. It checks all140 distinct halves, at most two unexcluded edges each, and certifies **3872** other halfgraph edges nonzero. Thus uncertainty is conservative: no actual zero edge was discarded if the enclosures and transcription are correct. The two algorithms share source formulas and the named Hadamard import; they are not an external-model review.

## 4. Scope

The source list's completeness is only for the four currently listed isolated examples; other 8×8 complex Hadamards and non-affine families remain. The source proposition, root/angle transcription, rigorous enclosure rules, matching caller and both programs require independent review. There is no conclusion about arbitrary even-order Fourier products or the original unrestricted 1-RQLS10 problem.
