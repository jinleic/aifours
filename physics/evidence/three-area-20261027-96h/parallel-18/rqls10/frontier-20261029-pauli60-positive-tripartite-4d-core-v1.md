# A 4D parity core compatible with the QLS10 context tripartition

**EXACT-CHECKED PARTIAL CONSTRUCTION, AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: **Thu Oct 29 00:49:25 PDT 2026**. This is NOT a 1RQLS10 construction: the complementary 6D rays and the remaining 25 cells have not been constructed.

## Actual finite witness

Use the exact Gaussian-integer rays numbered as in [Waegell–Aravind, Table1](https://arxiv.org/html/1109.1299v2#S2.T1). The following fifteen four-ray ONBs form three groups of five:

```text
R0 = {5,8,50,52}      R1 = {6,7,45,48}
R2 = {14,16,33,35}    R3 = {38,40,57,59}
R4 = {43,44,53,55}

C0 = {5,7,34,36}      C1 = {13,16,39,40}
C2 = {14,15,53,54}    C3 = {41,44,51,52}
C4 = {45,47,59,60}

T0 = {6,8,13,15}      T1 = {33,36,57,60}
T2 = {34,35,41,43}    T3 = {38,39,50,51}
T4 = {47,48,54,55}
```

They use exactly 30 pairwise distinct rays, each exactly twice; any two bases share at most one ray; and no two bases in the same R, C or T group share a ray. Hence the base-intersection graph embeds into `K_(5,5,5)` and each context has degree4. The other 45 edges of that complete tripartite graph form a 6-regular complementary incidence graph. The exact shared-ray matrices are in `frontier-20261029-pauli60-tripartite-core-independent-v1.json` SHA **ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd**.

This is a POSITIVE partial counterexample to overgeneralizing the previous 40-ray Petersen obstruction: these rays belong to the full 60-ray source, not to the one 40-ray subsystem excluded in `frontier-20261029-pauli40-petersen-parity-core-obstruction-v1.md` SHA **b066c15d9a8922653f6b7e61ddc3024ff7a8c67d35b59ca46fc7049bee8ec453**. It confirms the 4D tripartite parity-core premise is physically realizable. It does not establish that any complementary 6D realization exists.

## Evidence and exact remaining gap

`frontier-20261029-pauli60-tripartite-core-search-v1.py` SHA **40baaa1a7d25e32c12aa9117707422bb3159a697da1d076dcba9f36ec7cd3561**, result SHA **8fb98404025a8fcd521554cd0b9eced293bb9b84488ba970797b6a9174fcbeca**, regenerates the full source's 105 orthogonal 4-bases by exact Gaussian arithmetic, then finds a SAT 15-basis/3-color model. The SAT solver is used only as a search tool.

A separately transcribed original-vector checker `frontier-20261029-pauli60-tripartite-core-independent-v1.py` SHA **518d6444fdd71214c5ef0a6d6d5b2ce0f1b076c79982af478cde39eabd048e8c**, result SHA **ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd**, checks the actual30 vectors' 435 distinct-ray pairs, all90 within-base orthogonalities, every 0/2 incidence, every same-family disjointness and every shared-ray multiplicity. Normalizations are inferred exactly from positive integer squared norms.

To obtain a full 75-ray parity core, the 45 complementary edges need DISTINCT rays in C6 such that each of the15 vertices has a 6D ONB. The resulting 6D sector cannot itself split orthogonally into nontrivial sectors, by the even-rank/no-rank2 parity argument. One must then realize the remaining25 cells and ALL 30 original 10D row/column/transversal ONBs, with 100 pairwise distinct rays. Neither the 6D complement nor that extension is supplied here.

Source transcription and independent replay require outside review; this is not formal verification or a novelty claim. The result does not settle the unrestricted target.
