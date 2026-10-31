# The published order-eight example is not a cyclic Fourier product

**EXACT-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Wed Oct 28 21:24:41 PDT 2026**. This tests the actual published even-order example as a possible counterexample to the Fourier-product question; it is NOT a general no-go for order8 or any even order.

## 1. Primary source and exact original-object checks

[Zhang–Cao, Example 2.4](https://arxiv.org/html/2608.29201v2#S2.Thmtheorem4) presents a maximal-cardinality 1-RQLS(8). Its complete example-table HTML fragment, transcribed directly from the source, is `frontier-20261028-zhang-cao-example24-source-v1.html` SHA **b10e87e1ac59e5fa4f7c6703d034eb61cb9e91c77209417adc3481e9d54211cc**. The exact parser/checker `frontier-20261028-source8-covariance-check-v1.py` SHA **504e7521ec91d932f8f29adf3711ad76c8a85d5d3d184a4779903c7eb2c8ec9f** decodes all64 source expressions in the integer basis `1,zeta8,zeta8²,zeta8³` with common denominator2; the stated sqrt2 coefficients use `sqrt2=zeta8-zeta8³`. Result SHA **a06dcd30a57b1e88fa6eda421e592071d2c3655936169af124ddeca4ddb5554a** records exact checks of64 unit norms, 224 row Gram pairs,224 column Gram pairs,224 Gram pairs across all eight published XOR-labelled transversals, and all2016 ray pairs distinct. These checks reconstruct the source's stated object, not a new target10 witness.

## 2. Necessary covariance invariant

If an array is a cyclic Fourier product, perhaps after ONE row permutation, ONE column permutation, a common unitary, and arbitrary individual cell phases, some global unitary U cyclically maps each row's labelled rays to the next row's labelled rays. Therefore, for a suitable eight-cycle of the rows, all eight directed matrices

`G_(r,s)[c,d]=|<v_(r,c),v_(s,d)>|²`

on consecutive row pairs must be IDENTICAL. Individual phases cancel from these squared magnitudes; one global column permutation relabels both indices of EVERY G equally and cannot create equality of unequal matrices. A common unitary also cancels. This invariant is necessary, not sufficient, for a cyclic Fourier representation.

For the primary source array, exact field arithmetic finds five distinct directed Gram-block values. Their directed-edge classes have sizes `16,16,8,8,8`: each 16-edge class is a disjoint union of two bidirected K_(2,2) graphs on four vertices each, and each 8-edge class is four bidirected single edges. EVERY monochromatic component has at most four rows. Hence there is no invariant eight-cycle and no possible cyclic Fourier-product representation under the stated isotopies.

The same calculation after transposing the entire array gives the identical five edge-class structures and again no eight-cycle. Thus transposing rows/columns does not turn this particular example into a Fourier product either. This does not authorize arbitrary independent relabelling within individual rows or columns, which changes the QLS incidence and is NOT an isotopy assumed here.

## 3. Boundary

The published example establishes that general even-order maximal 1-RQLSs exist, but this exact invariant shows it does **not** furnish an even-order cyclic-Fourier-product transversal. Other order8 examples and unrestricted K may behave differently; n>=8 even existence remains unsettled by this check. The source parser, field operations, original constraints and covariance implication need independent review before adoption.
