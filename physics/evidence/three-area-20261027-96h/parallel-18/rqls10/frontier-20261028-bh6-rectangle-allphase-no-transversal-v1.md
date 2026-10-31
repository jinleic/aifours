# Every single-rectangle affine deformation of BH(10,6) has no transversal

**CATALOG-CONDITIONAL, COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at independent replay: **Wed Oct 28 19:53:50 PDT 2026**. This generalizes the ONE-family continuous no-go `frontier-20261028-q18-affine-allphase-no-transversal-v1.md` SHA **80f4b9164c4b3da8a43e207a3c50bd624e096259452281ea7f4c6800ae37f2fd**. It excludes a broad but still restricted actual-vector family, NOT all QLS10s or all BH(10,18)s.

## 1. Statement

Take ANY `H in BH(10,6)`, ANY subsets R of its rows and C of its columns such that

`K_(t,c)(z)=H_(t,c) z^[t in R and c in C]`

is a complex Hadamard for EVERY unit z. Then, for EVERY unit complex z, EVERY K-row ordering, arbitrary row/column phases and column permutations, the Fourier-product QLS `psi_(r,c)(t)=zeta10^(r t)K_(t,c)(z)/sqrt(10)` has **NO orthogonal transversal**, even with repeated rays. Degenerate empty/full R or C are just row/column phase gauges of H and are covered by the base q6 no-T result.

The ALL-H quantifier and the z in mu6 endpoint use the prior published 34-class monomial classification [Lampio–Östergård–Szöllősi, Theorem4.1/Table2](https://arxiv.org/html/1707.02287v1), and the unreviewed q6 certificate result `frontier-20261028-all-bh10-6-product-no-transversal-v1.md` SHA **ae707c663690643c541edea9c54927672d48b9d561b4477a484e2d8bbb85b3de**. The prior catalog classification was NOT regenerated. Independent review of it and every new finite caller is needed.

## 2. Exact enumeration of EVERY rectangle

For a nontrivial column subset C, build a graph on H rows, joining r,s iff their inner product restricted to C is nonzero. The Hadamard deformation exists for all unit z iff R is a union of connected components: cross-R row inner products are `z*A+B` and vanish identically iff their C-restricted sum A is zero (full H orthogonality then forces B=0).

Replacing R by its complement is equivalent to replacing z by z^-1 plus a column phase; replacing C by its complement is equivalent to z^-1 plus a row phase. Therefore WLOG both R and C contain index0; all nontrivial rectangles are covered up to these harmless gauges/inversion.

For the 34 literal catalog representatives, `frontier-20261028-bh6-rectangle-families-v1.py` SHA **35c32b12634e996fd139f0740c721b83b678a1293c729d13ab6c7ee1791a2044** enumerates component unions and records exactly **104** normalized rectangle families in JSON SHA **6973fcdd8cfc3bba2d67c075e51a63f4a6bd1eaa34d75e5c1d53961c69f6de71**. The independently written verifier below enumerates ALL normalized R masks directly for each C mask and verifies set equality with those104; it also verifies every source H's row orthogonality exactly.

## 3. Complete unit-circle half-edge sieve

For each family, each of252 source-row subsets E and each of45 K-column pairs, the necessary even-half zero is a Laurent polynomial

`A_- z^-1+A_0+A_+ z` over Z[zeta6].

A transversal must induce a perfect matching of the corresponding ten-column half graph, as in the q6 packet. The two exact, independently written scans `frontier-20261028-bh6-rectangle-unitroots-v1.py` SHA **65457cd0a4d0432c85040d4d7bab033866dcb1c6d004f0b911fd38438069303b** (reciprocal-resultant arithmetic) and `frontier-20261028-bh6-rectangles-independent-v1.py` SHA **5442e02b1dca995e9df7b140286f596dae4e3365b9393deaaf39bde2a2d02d6a** (exact polynomial gcd in Q(zeta6)) examine **104*252*45=1179360** literal half-polynomials. The independent output JSON SHA is **ce2880673eeef05acd0a91a08e631d348226239c31844f1dd842fbd2242a586c**. Both establish for ALL104 families:

1. for EACH E, the graph made only from identically zero half-polynomials has NO perfect matching;
2. any unit-circle zero of a NONidentity half-polynomial belongs to mu6.

The independent scan counts **85472 identity**, **928368 with no unit-circle zero**, and **165520 with unit zeros only in mu6**, totaling1179360. For a quadratic sharing its reciprocal-conjugate factor it also checks the discriminant/root case, rather than assuming every zero resultant is harmless. All counts and gcd tests use exact integer/Fraction arithmetic, not the prior floating triage.

For z outside mu6, only identity edges are present and no E graph has a perfect matching, so there is NO transversal. For z in mu6, K(z) is itself BH(10,6), so the prior all-q6 no-transversal theorem applies. Hadamard monomial equivalence sends rectangles to rectangles; the row/column gauges and complement normalization above preserve the physical conclusion. This proves the stated all-phase result conditional on the stated catalog/base import.

## 4. Limits

This covers one independent rectangle parameter at a time; products of multiple phase rectangles, arbitrary binary/nonbinary masks not known to be affine, other base Hadamards, arbitrary continuous K and nonproduct QLSs remain open. The exhaustive finite programs and the source classification need independent review; no target 1-RQLS, unrestricted no-go, formal proof or novelty claim is asserted.
