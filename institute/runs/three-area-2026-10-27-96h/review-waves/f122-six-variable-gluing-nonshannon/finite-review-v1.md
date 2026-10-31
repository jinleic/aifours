# f122 independent finite witness review

**Disposition: finite Shannon-separator verification PASS.** No FATAL, MAJOR, or MINOR finding was found in the finite reconstruction and controls described below. This is one independently written, same-harness checker, **not** independent-model-family, human, formal/kernel, or novelty review. The finite vector is a Shannon polymatroid that violates the displayed linear form; it is not asserted to be entropic, nor to improve an original guessing-number bound.

## Frozen inputs and read order

The manifest was read first and its SHA-256 matched `b8bdc86c7281c3c8e1d0c6a2abdc980848e620650a8df95906cae854a6524907`. All three declared inputs were then read completely and in order, with their full SHA-256, bytes, and LF pins verified both before reading and again inside the independent execution:

| Input | SHA-256 | Bytes | LF |
|---|---|---:|---:|
| Inequality manuscript | `f5c83b572ecc2ec25a62b22e24e405a897b37152385a11a1e31f37f567a07075` | 5,518 | 62 |
| Exact witness JSON | `10aa3d5daa42b42223193b5a465aa32e5883b592a916be5d5941ee00bc5dc169` | 1,769 | 146 |
| Author checker, read only | `4b55faa53a9d3043eb4baa9d3fc497934247c37da83b0a04927854697d09fdf6` | 3,550 | 73 |

No author code was imported or executed. The verifier strict-parses the complete eight-row manuscript table: ordered consecutive mask ranges, exactly eight canonical nonnegative integers per row, variable order `B,C,R,H,P,Q`, and the printed scale. All 64 coordinates and the scale `6,900,000` match the strict JSON parse; duplicate JSON keys and coefficient masks are rejected. The manuscript's displayed exact value and the JSON's scaled value were checked separately against the independently evaluated dot product.

## Coefficient reconstruction

The checker parses the nine written conditional-mutual-information terms, verifies disjoint variables and conditioning sets, and expands each from the definition `I(X;Y|Z) = H(XZ)+H(YZ)-H(Z)-H(XYZ)`. **The JSON coefficient map is not used to form that expansion.** The resulting 16 nonzero coefficients agree exactly, mask by mask and sign by sign, with both the independently parsed manuscript expression and the JSON map:

| Mask | Set | Coefficient | Mask | Set | Coefficient |
|---:|---|---:|---:|---|---:|
| 3 | BC | -1 | 31 | BCRHP | -1 |
| 5 | BR | -1 | 33 | BQ | -1 |
| 15 | BCRH | +2 | 35 | BCQ | +1 |
| 19 | BCP | +1 | 37 | BRQ | +1 |
| 21 | BRP | +1 | 41 | BHQ | +1 |
| 23 | BCRP | -1 | 42 | CHQ | -1 |
| 25 | BHP | -1 | 46 | CRHQ | +1 |
| 27 | BCHP | +1 | 47 | BCRHQ | -2 |

All 16 masks containing **both** `P` and `Q` have coefficient zero in each representation. The nine-term expansion has eight coefficient-`+1` CMIs and the single coefficient-`-2` term `I(P;Q|B,C,R,H)`.

## Independent finite Shannon checks

All calculations below are integer arithmetic on the table numerators; slacks have common denominator `6,900,000`. The complete row-by-row slacks and their masks are retained in `finite-rows-v1.json`.

| Formulation | Rows checked | Zero slacks | Positive slacks | Smallest positive numerator |
|---|---:|---:|---:|---:|
| Elemental: 6 full-context conditional entropies and 240 elemental CMIs | 246 | 61 | 185 | 6,852 |
| All `A subseteq B` monotonicities, including equality | 729 | 114 | 615 | 130,200 |
| All ordered subset-pair submodularities `(A,B)` | 4,096 | 1,630 | 2,466 | 6,852 |

The monotonicity count includes 665 strict comparable pairs and 64 equality pairs; the submodularity count includes both orientations and equal/comparable pairs. All three formulations have minimum slack zero and no negative slack, and the normalized empty-set value is zero. These direct all-pairs formulations are independently enumerated expressions, not derived from a presumed elemental pass.

The computed linear-form numerator is exactly `-50,548`, and

`Phi(r) = -50548 / 6900000 = -12637 / 1725000 < 0`.

Consequently this point lies in the six-variable Shannon polymatroid cone and is outside the half-space `Phi >= 0`. In particular, the displayed inequality cannot be a nonnegative linear combination of the six-variable elemental Shannon inequalities. This is the precise **non-Shannon-type cone-separation** conclusion; it does not imply novelty or an entropic realization of the witness.

## Controls

There are 15 intended-reason negative checks on 13 retained distinct mutated inputs, each with a canonical-payload SHA-256 and exact observed failure in `finite-controls-v1.json`. They cover malformed/out-of-order table rows, an altered table coordinate, a wrong scale, a duplicate JSON key, nonzero empty-set value, duplicated or sign-flipped JSON coefficients, an overlapping CMI condition, an altered CMI condition, and a sign-flipped manuscript entropy term. Two vector mutations are each checked through different formulations: setting the full-set coordinate to zero is caught by both elemental and all-comparable checks; increasing the `BC` coordinate beyond `H(B)+H(C)` is caught by both elemental and all-pairs submodularity checks. Every control was rejected for its specified error, not merely by an arbitrary exception.

Two exact positive polymatroid controls, a weighted modular rank function and the uniform rank-two function, pass all three formulations and evaluate to `Phi=0`. A third, strictly positive **finite-law gluing control** uses independent fair bits `U,V,W,S,T` with

- `B=U, C=V, R=W, H=U xor W, P=S xor U`;
- `Q=S xor V` before gluing and `Q=T xor V` after gluing.

The original law has 16 equiprobable atoms and the glued law has 32. Exact rational probabilities verify equality of the `(Y,P)` and `(Y,Q)` marginals for `Y=(B,C,R,H)`, and the conditional product identity for every supported `Y,P,Q` state. All 48 entropy coordinates whose masks do not contain both auxiliary variables are preserved. Exact integer-bit entropies give `I(P;Q|Y)=1` before and `0` after, while `Phi=1` bit in both. In written order the nine CMI values are `[0,0,1,1,0,0,0,1,1]` before and `[1,0,0,0,0,0,0,0,0]` after; both satisfy the checked identity. This example exercises both auxiliary roles but is **not** a universal proof.

## Separation versus universality, closure, and novelty

The finite witness establishes only the stated Shannon-cone separation. Universal entropy validity rests on a different argument: for each supported `Y=y`, replace the original conditional joint distribution by `p(P|y)p(Q|y)`. Both `(Y,P)` and `(Y,Q)` marginals, and hence all 16 entropy terms, are preserved; in the checked CMI identity the negative term becomes zero, leaving eight nonnegative CMIs. The closure claim then follows from continuity of the finite-dimensional linear form. Neither universal validity nor closure is proved by the negative vector or by the single finite-law control alone. A complete independent proof-review disposition remains separate from this finite-witness ticket. No literature priority or novelty determination was attempted.

## Execution and retained receipts

Exactly one independently authored exact execution was run: `python3 -B finite-check-v1.py` under Python 3.14.3. The run recorded start `2026-10-28T19:53:26.808582-07:00` and completion of computation `2026-10-28T19:53:26.821459-07:00`; source SHA and output SHA values were also independently observed after the run. The complete checks and fixtures are retained next to this report:

| Artifact | SHA-256 | Purpose |
|---|---|---|
| `finite-check-v1.py` | `776f53b8e9717352d2bf7e83f574a307813eec251a632c6bbb398696546b6104` | Own exact checker; no author import or execution |
| `finite-result-v1.json` | `52066a98586b68b7998cdf979bd91fcf33cfb91b6b8174a873ec0d297f16b5b2` | Input pins, all signed coefficients, summaries, clock, output bindings |
| `finite-rows-v1.json` | `5a0e96a36d96c983f3d1f4138dd56511e36ff2979704ca9db32593eeae5fd6c1` | All 246, 729 and 4,096 exact slack rows |
| `finite-controls-v1.json` | `074c3bf70d1309ffbb1bdf1c5b529d9a00f1022f4f7ed337578210e6125524fb` | Hashed mutation payloads and reasons, positives, exact finite-law control |
