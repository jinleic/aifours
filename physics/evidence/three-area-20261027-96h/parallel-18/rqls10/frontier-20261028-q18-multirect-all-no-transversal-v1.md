# No transversal in q18 specializations of BH(10,6) multi-rectangle families

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the final independent coverage replay: **Wed Oct 28 20:09:56 PDT 2026**. This covers genuine q18 examples OUTSIDE the earlier binary-lift criterion, but is NOT a classification of BH(10,18) or a general QLS10 no-go.

## 1. Statement and important scope

Let `H in BH(10,6)` and let `M_1,...,M_s` be rectangle indicator matrices such that

`H(z)_(t,c)=H_(t,c) product_j z_j^(M_j(t,c))`

is a complex Hadamard for EVERY choice of unit phases z_j. **Claim:** if EVERY parameter z_j is an 18th root of unity, then the actual Fourier-product QLS formed from H(z) has NO orthogonal transversal, even when rays repeat, for arbitrary physical K-row ordering, row/column gauges and column permutations. The number s is unrestricted: duplicate rectangles can be combined and degenerate rectangles are gauges.

The ALL-H and rectangle-family coverage uses the 34-class BH(10,6) monomial classification [Lampio–Östergård–Szöllősi, Theorem4.1/Table2](https://arxiv.org/html/1707.02287v1), and the conditional q6 no-T theorem `frontier-20261028-all-bh10-6-product-no-transversal-v1.md` SHA **ae707c663690643c541edea9c54927672d48b9d561b4477a484e2d8bbb85b3de**. These prior imports and all new code/callers are unreviewed. The result does NOT cover non-rectangle masks, families not Hadamard for all independent phases, other q18 matrices, arbitrary phases or nonproduct QLSs.

## 2. A general binary-gauge criterion

Call a BH(10,18) exponent matrix e **binary-gaugeable** if additive row/column shifts mod3 put every e_(t,c) into `{0,1}`. Such a K always has NO Fourier-product transversal, conditional on the q6 theorem:

1. Apply the corresponding row/column zeta18 phases and write the resulting entries as `H'_(t,c) zeta18^R_(t,c)` with H' entries sixth roots and R binary.
2. Since `[Q(zeta18):Q(zeta6)]=3`, any K-column inner product is a Laurent polynomial in zeta18 of degree at most1 in each direction. Multiplying by zeta18 produces degree<=2, so the Hadamard orthogonalities at zeta18 are identities. At parameter1, H' is therefore BH(10,6).
3. `[Q(zeta18):Q(zeta30)]=3` likewise forces any physical Fourier-product transversal at zeta18 to exist at1, contradicting q6 no-T. Row/column gauges do not affect transversals.

This recognizes arbitrary binary-gaugeable q18 K directly; one need not already know the sixth-root base H'. Nonbinary means no such decomposition even after arbitrary unit row/column phases and permutations: because both sides have 18th-root entries, all row/column phases can be normalized to 18th roots up to one canceling common factor, so the F3 gauge test is complete.

As a closed-form special case, ANY sum of two rectangle masks with ANY integer coefficients is F3-binary-gaugeable. Write each term as `x_i y_i`, x_i,y_i∈{0,1}, after replacing `-x_i y_i` by `(1-x_i)y_i-y_i` and absorbing `-y_i` into a column gauge. Then adding row gauge `-x_1 x_2` and column gauge `(1-y_1)(1-y_2)` yields only 0 or1 modulo3. Its complete 9 coefficient-sign choices×16 bit cases are checked by `frontier-20261028-two-rectangle-binary-identity-v1.py` SHA **8aebb85bb2d42a398596e77400ed53f9dffecfb3385779de514845638ae987e5**. Thus ANY q18 Hadamard obtained from a sixth-root matrix by two rectangle phase factors is in the binary no-T branch, even without separately assuming a two-parameter affine family.

## 3. Exhaustive normalized rectangle specializations

The prior independent rectangle-family census `frontier-20261028-bh6-rectangles-independent-v1.py` SHA **5442e02b1dca995e9df7b140286f596dae4e3365b9393deaaf39bde2a2d02d6a** proves, for the 34 literal representatives, there are104 nontrivial normalized rectangle directions, with R and C each containing0. Complementing R or C only changes the phase sign and a row/column gauge. Every compatible multi-parameter family is a subset of these directions; compatibility is the exact vanishing of each coefficient in each row-pair Laurent polynomial.

The independently written `frontier-20261028-q18-multirect-bothsign-replay-v1.py`, SHA **225e2ec716aeec08bd923699e0ea8513892a05f145af9dec4434eb0c9ebab43a**, reconstructs EVERY subset without the producer's pruning and verifies exact compatibility. It obtains subset counts

```text
1 direction:104; 2 directions:176; 3 directions:164;
4 directions:76; 5 directions:14; larger:0.
```

For each compatible subset it enumerates ALL nonzero residues 1 or2 for each parameter, not merely one global sign, giving **3888** literal specializations. The earlier producer `frontier-20261028-q18-multirect-all-sign-v1.py` SHA **f7684f47cf30a752a80a95e7c271c1058c5215db2b267d86cda5799b00b90e73** records all gauge witnesses/exception cases in JSON SHA **ea58bac43c93c799bebee8a2d7f1b3ba4955822545fbf24478231fc810f8cf5b**. The independent replay checks set equality and EVERY row/column gauge byte: **3864** are binary-gaugeable and covered by §2; **24** are not.

For arbitrary 18th-root parameter exponents, coefficients divisible by3 are absorbed as sixth-root phase specializations into a new BH(10,6) base; simultaneous compatibility survives. Reclassifying that base by the named 34-class import, normalizing each rectangle by complement/gauge and dropping zero residual coefficients lands in the exhaustive 3888 cases. This is why the literal finite scan covers the stated conditional ALL-H family, not merely its displayed examples.

## 4. Twenty-four genuinely nonbinary q18 matrices

All24 nonbinary specializations use four rectangle directions. Their literal exponent matrices and a digit certificate for each of the `3^9=19683` normalized F3 row gauges are in `frontier-20261028-q18-nonbinary-twentyfour-v1.json`, SHA **776515e99bfc2b04ea7511ab14e971dfa4f0b8bc285df517e5cc5d47c92c11d2**. The digit identifies a column whose forbidden column shifts cover ALL three residues, proving no binary gauge exists. Each matrix has no perfect matching in ANY of its252 half graphs, so it has no Fourier-product transversal for ANY coordinate row order.

Independent `frontier-20261028-q18-nonbinary-twentyfour-replay-v1.py`, SHA **1ae8695da15fe9dc813539c9853f47bddcafe28cfaaff727ee69eb8088ec778b**, reconstructs all24 from the literal source and masks, checks all6048 half graphs in an exact `Q(zeta6)[zeta18]` basis, replays all **472392** F3 row-gauge obstruction digits, and verifies on ORIGINAL q90 vectors all100 norms,20 ONBs and4950 pairwise distinct rays for EACH identity coordinate order. Result SHA **0bdb5ed4d6bbfefea77d6ecc9c62d8e5e43d84dcb81a8e7cd2ccc20d92a3d9f7** records PASS. These are24 literal maximal QLS10 examples with no transversal; no claim is made that they are mutually inequivalent or 1-resolvable.

## 5. Remaining frontier

The theorem covers q18 specializations of the stated simultaneously affine rectangle families only. It does not cover general BH(10,18), non-rectangle masks, continuously variable multi-parameter exceptions, arbitrary complex Hadamards, nonproduct QLSs or unrestricted 1-RQLS10. The prior classification, finite coverage, algebraic-degree and physical symmetry callers all require independent review; no target witness, global impossibility or novelty clearance is claimed.
