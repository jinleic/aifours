# A 60-CMI certificate for the common-syndrome lemma

**Status: WRITTEN-CHECKED-IN-KERNEL; scientific review pending.** This is an independent shorter exact certificate for the common-selector lemma in `frontier-20261028-two-syndrome-repaired-theorem-v1.md` SHA-256 `9feb6cd50a2b376b971c2091369b5c5ad7d50e18446ce4cd3293bfc718b776b1`. The required earlier local-neighbourhood erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f` remains part of the source history. The proof below explicitly uses the corrected actual factor-component local decoder.

For a law of ten triangle-factor vertex blocks with a common selector `S` determined by each factor syndrome and with original graph FDs, the exact coefficient identity `frontier-20261028-common-syndrome-compact-dual-v1.json` SHA-256 `580416bde07e8009210f1e9cef3272c4a465f8693c35cfd67046e6bdbc6353a9` expresses

\[
\Delta=H(X_V)-\tfrac23\sum_v H(X_v)
\]

as a four-automorphism average of **60** elemental CMIs with negative rational weights and 12 equality rows. Of these 12, three are original graph FDs, two assert syndrome recovery from a graph neighbourhood, one recovery from a triangle, one recovery from all vertices, and five are conditional local-factor FDs. Their conditioning vertex masks and target vertices are

```text
467 -> 3     471 -> 6     507 -> 3     510 -> 1     511 -> 10
```

A mask uses bit `v-1` for vertex `v`. In each row the mask contains every other vertex in every triangle incident to the target; given `S`, those components uniquely determine all target components even over nonabelian finite groups. Thus all 12 rows are zero for the actual common-selector law and every CMI contribution is nonpositive. This proves `Delta<=0` under those hypotheses without a separate tensorized entropy gate, cardinality cap or LP optimality assertion.

The independent checker `frontier-20261028-common-syndrome-compact-dual-check.py` SHA-256 `8a4abd77c46d788b0043016222b3beadb157bef45a188704d8ab37c6736c6f23`, receipt SHA-256 `fe63e84172928106831f8e6062da5ad9f0d0226d40d5f466c1e863ce8790f029`, validates all signs, the five local-set containments, automorphism group, 2,047 entropy coefficients, and two negative controls exactly. It is not a proof assistant, independent scientific review, novelty clearance, or a general bound outside the theorem's support class.
