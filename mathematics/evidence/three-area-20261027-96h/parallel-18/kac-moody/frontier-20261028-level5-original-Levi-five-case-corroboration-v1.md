# Five direct original-generator versus Levi quotient cross-checks

**MathKacMoody-2 / math-3.** Native clock before this additive write: **Wed Oct 28 18:42:39 PDT 2026**. These are exact, bounded, same-owner corroborative computations, not a proof of all parameters, an independent-vendor/human/formal review, parent adoption, or a claim identifying the preliminary-G reached-target obstruction with a compressed-Levi obstruction.

## 1. Exact checked quantities

The new `frontier-20261028-level5-original-Levi-crosscheck.py` constructs the source in TWO different presentations for each fixed case. One starts from the actual three positive generators, all six literal positive Serre seeds, their whole ideal closures and the full three-lowering direct-sum target. The other uses the separately written eight-letter free-Levi engine with the entire node-3 seed ideals and actual targets. Both use exact rational sparse elimination and share generic local arithmetic helpers. For every case the program compared **all three**:

1. entire actual Serre-quotient source dimension;
2. rank of the full simultaneous `(f1,f2,f3)` map into the full quotient target direct sum;
3. dimension of its full simultaneous quotient kernel.

Every actual ideal-source derivative was checked to descend into the whole target on the direct-original side. The exact five comparisons were:

|degree|r,s|actual quotient dim|full three-lowering rank|simultaneous kernel dim|
|---|---|---:|---:|---:|
|(2,2,5)|1,2|1|1|0|
|(2,2,5)|2,3|20|20|0|
|(3,2,5)|3,2|44|44|0|
|(2,3,5)|3,4|69|69|0|
|(3,3,5)|2,4|115|115|0|

All five output `cross_representation_comparison=PASS`. These are exact finite parameter cases only; the unbounded F5 candidates still require their own full source/ideal and polynomial proofs, not interpolation from this table. The code paths share exact `Span` and bracket utilities, so the checks are not wholly independent software implementations.

## 2. Two concrete warnings against a whole s4 quotient substitution

The fresh full-source s4 cases illustrate why the 154* type exclusion in the uniform small-row proofs is necessary and why it MUST NOT be broadened to a claim about the whole quotient:

- At degree `(2,3,5)`, r3, the source model built with s5 has whole quotient dimension 72 (r3 paper's 35* row), whereas the independently built actual s4 quotient has dimension **69**. These are not equal whole spaces, even though the finite-Levi absence of type154* lets a separately checked selected primitive isotype survive.
- At degree `(3,3,5)`, r2, the source model built with s5 has whole quotient dimension 118 (r2 paper's 27 row), whereas the independently built actual s4 quotient has dimension **115**. Again, the selected type27 isotypic quotient comparison is a separate written theorem; the WHOLE quotients differ.

These are positive finite counterchecks against an illicit whole-space shortcut, not counterexamples to the selected-isotypic candidate or proofs of an unbounded map.

## 3. Actual data, pins and exact observation

|Owner-root file|LF|SHA-256|
|---|---:|---|
|`frontier-20261028-level5-original-Levi-crosscheck.py`|37|`d952ccdcb22cd580e8631f3ecfbca4dfbb6e03ab8bc5df0def814ece04bdb6cf`|
|`frontier-20261028-level5-original-Levi-22-r1-s2-v1.json`|15|`4c90ceb34eb9a2e4469446a6376f6f1af260b8bdf83f7cba07077bcc194e94be`|
|`frontier-20261028-level5-original-Levi-22-r2-s3-v1.json`|15|`d6a7ad93a7f62d29464b8054f729ca1ea710e238168298ed44eba29535426f96`|
|`frontier-20261028-level5-original-Levi-32-r3-s2-v1.json`|15|`c7d3b5dc15759abce362647de08ffc32c177076add5419e13c38f394e167459b`|
|`frontier-20261028-level5-original-Levi-23-r3-s4-v1.json`|15|`12e9cbf91690be42a779af0eb1093dee1fe9ff7f550ee72e9be6d305cb54c56d`|
|`frontier-20261028-level5-original-Levi-33-r2-s4-v1.json`|15|`988bc8a8a1ab89672297ecd5a3e73ca1f78d9917ae11fdfb3c54277344e42e27`|

The first independent comparison returned PASS by **18:20:43 PDT**. The sequential other four returned all PASS by **Wed Oct 28 18:42:28 PDT 2026**. The newly disclosed whole-space inequality is not a source error in the current F5 candidates: their stated s4 bridge is selected-isotypic, not whole-space equality. All source-isomorphism, exact code, historical process, B4/F5 and independent review boundaries remain unchanged.

**END — five exact finite cross-checks; no unbounded conclusion.**
