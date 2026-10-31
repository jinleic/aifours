# No transversal in the BH(10,12) Fourier-product family

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay: **Wed Oct 28 19:40:58 PDT 2026**. This is a NONuniform, ALL-L restricted-family result, stronger than a maximality obstruction; it does not settle general QLS10.

## 1. Claim and explicit import

For ANY `K in BH(10,12)`, including arbitrary Hadamard row/column phases or permutations, the Fourier-product QLS

`psi_(r,c)(t)=zeta10^(r t) K_(t,c)/sqrt(10)`

has **NO orthogonal transversal**, even when repeated rays are allowed. The ALL-K claim imports the 577-class monomial-equivalence classification in Lampio, Östergård and Szöllősi, [Orderly generation of Butson Hadamard matrices](https://arxiv.org/html/1707.02287v1), Theorem4.1/Table2, and its [electronic supplement](https://wiki.aalto.fi/spaces/Butson/pages/120482304/Matrices+up+to+monomial+equivalence). The literal 577-line BH1 file used here is `frontier-20261028-aalto-bh10-12-catalog-v1.txt`, SHA **057e48f4b23cd96923aff9b8b8e791341e124a3a539ab652b78e8feafb8dd354**. Its rows and columns, q and exponent bytes are validated; the prior catalog completeness search is NOT independently regenerated.

Hadamard row phases are common coordinate unitaries, column phases are cell phases, column permutations relabel cells, and all row permutations are covered by the explicit enumeration. Arbitrary additional phase gauges are therefore also allowed.

## 2. Sieve and symmetry normalization

For a putative transversal, pair its cells in rows r,r+5. Their ten K columns must form a perfect matching in the graph whose c,d edge means the sum of `conjugate(K_(t,c))*K_(t,d)` over the five K rows E at even physical coordinates is zero. Full K-column orthogonality plus opposite-row vector orthogonality proves this necessary condition. E and its complement give the same graph.

Exact independent scans check all `577*252` subsets and all45 K-column orthogonalities for every representative. `frontier-20261028-aalto-halfgraph-census-v1.py` SHA **10a5ca121f1f9395bbcc3292d426b1c63d5a5f76fc3fa74961943ff076187d16** uses cyclotomic reduction/bitmask matching. The independent certificate replay below uses a Q(i,zeta3) basis and recursive set matching. Both find **330** matching half-subsets on60 representatives; the remaining517 representatives cannot have a transversal in ANY row order.

Cyclic shifting of the physical coordinate index swaps E/complement when needed and then puts source row0 at even physical coordinate0, producing only a common coordinate permutation and row-dependent cell phases. Exactly165 normalized E subsets remain; each has `4!*5!=2880` physical row orders, i.e. **475200** orders. These are ALL matching halves, including cases whose rays repeat; no maximality or nonparallel filter is used.

Any transversal can be shifted by a common diagonal unitary in its row index until its column0 cell lies in row0. Thus each of the 475200 cases needs only rule out transversals containing `(row0,column0)`.

## 3. Complete replayable no-transversal certificates

`frontier-20261028-aalto-q12-certificate-v1.py`, SHA **1d14bd20f913f03c1f8143fbad46df36ff65b5357e44e17c619c7fe5c98e0df1**, produces `frontier-20261028-aalto-q12-certificate-v1.json`, SHA **bd697d51e119d5562512e92250cb0b59ac8a449ba7e22fddab5fe3d2354b6f16**. For each normalized row order it contains either:

- one row r for which NO column d!=0 is orthogonal to `(0,0)`, or
- a finite branch tree listing every still-available column at a chosen unassigned row and, recursively, an actual empty-row obstruction at every leaf.

The producer uses exact integer reduction modulo Phi60. It records **472584 root-empty orders**, **2616 branched orders**, and **6168 branch-tree nodes**. A separate C++ Phi60 MRV search SHA **0f323685f97ac79904ba2730854cc70a14cc91551e71c21620a0c69e4a4be244** independently scanned ALL165 halves/475200 orders and observed the same aggregate counts with no transversal. It uses the unfiltered all-half input SHA **e6b64c3048a1d94f1e761c8cdcfd714a850d4aa75f6d3fccf7efc61d8110bfdb**.

An independently written replay, `frontier-20261028-aalto-q12-certificate-replay-v1.py` SHA **e02766673d0b2af44decbf9822b1ffd36b1cb467883bca572ed68260c8fada3b**, rebuilds the 577 half-graph census directly from the raw catalog, checks that all165 certificate halves exactly match the normalized survivors, and reconstructs every lexicographic row order. For root digits it checks all9 candidate inner products are nonzero; for every branch node it independently computes ALL columns actually compatible with the assigned cells and verifies exact equality with the certificate's child list, with an empty compatible set at every leaf. Its exact field representation is different from Phi60: `zeta60=i³*zeta3²*zeta5³`, with the 16-element product basis of the linearly disjoint cyclotomic fields Q(i),Q(zeta3),Q(zeta5). Its result SHA is **40bdcef6280a0ee516ea84b3ff5cc0916cf5f4d1f826005f0d5d055800852db5** and reports

```text
577 validated BH matrices; 330 matching halves; 165 normalized halves
475200 orders; 472584 root-empty; 2616 branched; 6168 checked tree nodes
PASS independent exact Q(i,zeta3,zeta5) replay
```

No floating arithmetic or timeout supplies the claim. The root digits and every branch tree are retained, allowing a reviewer to replay actual leaf coverage rather than trust aggregate solver output.

## 4. Remaining scope

The finite certificate and replay cover the provided 577 matrices and every physical K-row ordering via the stated symmetries; the published prior classification supplies the ALL-BH(10,12) import. It does NOT rule out K of other phase orders, arbitrary complex Hadamards, other physical constructions or nonproduct QLS10. Independent mathematical/code review, source-classification verification, and novelty assessment remain pending. No original target witness or unrestricted impossibility is claimed.
