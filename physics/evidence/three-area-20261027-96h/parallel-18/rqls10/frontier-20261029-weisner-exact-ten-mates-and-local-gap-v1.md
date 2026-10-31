# Complete classical-mate classification for one order10 resolution

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:31:46 PDT 2026**. This concerns the literal Weisner Figure1 resolution L only; no unrestricted QLS10 no-go is claimed.

## Classification

Up to a global relabeling of A-symbols, the fixed L has exactly **10** classical orthogonal mates A. The normalization is `A[0,c]=c`; rows, columns and L labels themselves remain fixed. The ten complete 10×10 A tables are recorded in `frontier-20261029-weisner-all-classical-mates-v1.json` SHA **480d68b237c071dbfe5b4cb5deafb42a11f6333ccfe9017659df1432db14afe7**. This counts exactly ten normalized mates, not necessarily ten classes after additional row/column automorphisms.

The row-group exact-cover producer `frontier-20261029-weisner-all-classical-mates-v1.py` SHA **e4d5e248bda8a30a52af2d9fea262140fbdc848c29ce67ff20a91a4d0d4fc8cc** enumerates ten disjoint transversals from the completely enumerated set of728, with 59928 search nodes. Independent `frontier-20261029-weisner-all-mates-algorithmx-v1.py` SHA **78fbc5ff620961a01762bccac1ec02db91e8d268ad9ea3ad775b3aee5e70463a**, result SHA **cc2febb794e589240abd6b0fd0b5a1e48d7cef82a2a98816b2fc130fbfc47b55**, re-enumerates L-transversals via dynamic MRV, then uses cell-driven Algorithm X (18030 nodes) and checks every original Latin and pair-orthogonality constraint. It recovers the SAME ten literal normalized tables. Both algorithms share the published L transcription, but enumerate the choices and exact cover differently.

## Consequences for quantum arrays

By the separate disconnected-trade exact-cover census in `frontier-20261029-sparse-resolution-classicalization-rigidity-v1.md` SHA **e08ae1bc19c3ea8d4c9a4c49a12120a08c671fb6408a9ad6ca9bd6d36c1b0823**, every pair graph of EVERY one of these classical mates is connected. The local rigidity theorem in `frontier-20261028-classical-rigidity-and-search-v1.md` SHA **3dc1eea8fdb47c04c39dea1d0a8a85122680db29b3d8c3fdea6c7ce05f712f24** therefore applies around each mate. The set of all classical arrays for this L is the union of the ten orbits under common U(10) and per-cell unit phases; it is compact. Consequently there is a positive, not explicitly computed epsilon such that EVERY exact 1RQLS10 with L within epsilon of this entire compact classical set is classical and has ten rays. This is a uniform existential local gap around ALL classical references of this L, not a numerical gap around all feasible arrays.

The sparse-classicalization theorem cited above yields the stronger GLOBAL statement under the extra hypothesis of a common support≤2 basis: every such resolved array is classical, hence is in one of these ten orbits. Arrays with support≥3 in every basis may exist far from the classical set; no claim is made about them or about another resolution L.

The table transcription, exact-cover completeness, orbit/local-rigidity and compactness caller require independent review. The result is not formal verification, human review or novelty clearance.
