# No transversal in the BH(10,10) Fourier-product family

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay: **Wed Oct 28 20:32:13 PDT 2026**. This is a strictly stronger successor to `frontier-20261028-all-bh10-10-product-obstruction-v1.md` SHA **9ffd6cb15029caeb5c976109df9e2ed8f8d9142dc0677b875476545dea74d02a**: it also checks all branches with repeated rays. No prior bytes are altered.

## 1. Exact claim and imported completeness

For ANY `K in BH(10,10)`, any K-row ordering, row/column phases and column permutations, the actual Fourier-product QLS

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`

has **NO orthogonal transversal**, without any maximal-cardinality or uniform-overlap premise. Therefore it has no 1-resolution for ANY L. The ALL-K statement imports the 51-class q-root monomial classification of [Lampio–Östergård–Szöllősi, Theorem4.1/Table2](https://arxiv.org/html/1707.02287v1) and its [Aalto supplement](https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence). Its literal 51-line input is SHA **3275d1f074dc3ac1bf82479755efb1f385361778ca35f85783a55be6cb4d0c55**. The prior classification's completeness was NOT independently regenerated; both new exact programs validate all51 literal matrices directly.

## 2. Exact exhaustive reduction

For any putative transversal, pairing its cells in rows r and r+5 gives a perfect matching on the K columns with zero inner-product sums over the even-coordinate K-row half E. K-column orthogonality supplies the same zero condition on the complement. Exhaustive checks on all51*252 halves give **56** matching subsets, hence **28** E/complement pairs.

A cyclic physical-coordinate shift exchanges E with its complement if needed and places source row0 at coordinate0, costing only a common coordinate unitary and cell phases. Exactly `4!*5!=2880` row orders remain for each of the28 normalized halves: **80640** orders. Any candidate transversal can be shifted in physical row index by a common diagonal unitary until its column0 cell is at row0. This is the only transversal normalization.

## 3. Complete leaf certificate and independent replay

`frontier-20261028-aalto-q10-certificate-v1.py`, SHA **c84a30afd286458971356745c870644cc1534a3e5ca3d87839939576b9aa7186**, produces `frontier-20261028-aalto-q10-certificate-v1.json`, SHA **feb5d1aba23ab02c98dbe2356a6cbde6fc92b6620c4ec7e114358d62f80dff4a**. Each of the80640 orders has either a root row with NO orthogonal different-column choice from `(0,0)`, or a branch tree with EVERY compatible column and an empty-choice witness at each leaf. No character-ratio or duplicate-ray case is skipped. It records

```text
21792 root-empty orders; 58848 branched orders; 197714 tree nodes.
```

Independent `frontier-20261028-aalto-q10-certificate-replay-v1.py`, SHA **e141a133cfbe306f7deb345de8b5d2a1862a29115375ffe35035be3f0788498c**, regenerates all51 Hadamard checks and all252 half graphs each, verifies the exact28 normalized halves, reconstructs every row order, and checks each root digit and branch node's COMPLETE set of compatible columns. It represents roots independently using `zeta10=-zeta5^3` in the four-dimensional Q(zeta5) basis rather than the producer's Phi10 polynomial division. Its result SHA **1281de0202ffd9ac58de7ccf54db0a670583f23a277601b01b909648dc455aee** reports the exact counts above and PASS. A third C++ all-half MRV search SHA **37465dc7d6c138e6f0ae0e03f1eb5700ee86d0b816b8f03bb7d0b4b71ed32a40** found the same counts independently. No floating arithmetic or timeout is a premise.

## 4. Scope

The finite certificates cover the supplied51 representatives, all row orders and all transversals via the stated callers; the prior classification supplies ALL BH(10,10). This result does not cover q18 or general complex Hadamards, other product constructions or nonproduct QLS10. Independent code/math/source review, original target resolution and novelty clearance remain pending.
