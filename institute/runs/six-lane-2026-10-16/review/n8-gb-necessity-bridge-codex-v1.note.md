All ten SHA256 hashes and byte counts match the supplied values. This audit used static reads and hashes within the snapshot only.

| Component | Disposition | Findings |
|---|---|---|
| **GB NECESSITY** | **ACCEPT** | No correctness defect found |
| **GENUINE NF BRIDGE** | **ACCEPT-WITH-FIXES** | Two MINOR scope clarifications |
| **ADAPTER** | **ACCEPT-WITH-FIXES** | One MINOR documentation correction |

**No FATAL or MAJOR findings.** The repairs below clarify the written claims; they require no encoding change.

1. **MINOR — [SOURCE01:15](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-necessity-bridge-review-v1/snapshot/01-GB_NF_GENUINE_BRIDGE.r1.md:15): specify the ROWLEX domain.**  
   “The rows” leaves its range ambiguous. The accepted normalization sorts rows **2–7**, fixing rows 0 and 1.

   Exact replacement:  
   > **ROWLEX:** rows 2–7 are sorted ascending, non-strictly, by the Q1 column-0 support bits in coordinate order 0,…,7, coordinate 0 most significant, False < True, with no secondary key. Rows 0 and 1 are fixed.

2. **MINOR — [SOURCE01:17](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-necessity-bridge-review-v1/snapshot/01-GB_NF_GENUINE_BRIDGE.r1.md:17): separate sixteen-template coverage from the four-template setting.**  
   The setting restricts C to four templates, while “such a configuration … one of the sixteen” crosses that restriction.

   Exact replacement:  
   > By accepted U and T16, every genuine non-classical five-set reaches row-0 standard form, SB2 and ROWLEX with one of the sixteen templates. For the following argument, condition on its template belonging to {P1-B1, P1-B2, P1-B3, P1-B5}.

3. **MINOR — [SOURCE00:84](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/n8-gb-necessity-bridge-review-v1/snapshot/00-GB_ONE_P4_NECESSITY.r2.md:84): describe the allocator wrapper accurately.**  
   `Sink.new` is overridden at SOURCE03:116–126. Its call to `super().new(key)` preserves allocation, but saying the method is inherited is inaccurate.

   Exact replacement:  
   > `encode` is unchanged. `Sink.new` delegates allocation unchanged to the original `F.new` and adds control bookkeeping; `Sink.c` replaces clause storage with the original CLI serialization.

The GB necessity argument survives the clause audit.

- **Constants, allocation and G2:** T is allocated first and forced true. Identical-cell and collinear-cell constants have the correct signs. Unordered Gram variables represent symmetric zero/nonzero inner-product facts. With `ngen=0`, the classical branches contribute no constraints; `fixg` is absent. G2 follows directly from tensor-product orthogonality.
- **Conjunctions and counters:** `conj` is a full equivalence. `counter2` defines the two prefix thresholds, starting with both false. `atleast3` defines all three prefix thresholds, starting false and using true as the threshold-zero carry. The CNF implements
  \[
  a'_k=a_k\lor(a_{k-1}\land l).
  \]
  Empty prefixes and initial prefixes below the threshold therefore behave correctly. The equivalences remain valid for signed, repeated, complementary and constant inputs.
- **G3/G4:** G3 supplies nonempty overlaps and excludes exactly-one common support between orthogonal vectors. G4 permits either Gram value for intersection size ≥2, forces false for size 0, and true for size 1. Its two output clauses have the correct directions.
- **G5:** `single` is equivalent to exactly the selected frame coordinate being present. Both conditional Gram-equality directions express the same-ray consequence. Skipping false coordinates is safe. The omitted comparisons at `p=q` and `p=a` already follow under the singleton condition.
- **P4/SB2:** the exact call generates one row-0 P4 ALO for Q1, over its 56 off-row-0 cells. The normalized `(1,0)` support `{1,2,3}` satisfies it. SB2 assigns `{1,2,3},{4},{5},{6},{7}` correctly, including the retained coordinate-0 TRUE units. There is no P4 on squares 2–5, ROWLEX, fixed Gram data, or additional frame restriction.

Assigning actual Gram supports, actual conjunction values, actual prefix thresholds and actual singleton conditions satisfies every emitted family. This establishes the required genuine-image necessity without importing GA’s auxiliary extension.

As an independent static cross-check, counting the encoder loops gives **3,803,745 variables and 17,025,578 base clauses**. Adding 42 units gives 17,025,620 clauses; adding the strengthened tail gives 17,025,746. These agree with SOURCE08’s reported headers.

The genuine bridge is mathematically sound after the two scope repairs.

SOURCE01’s proofs of **(A)–(C)** are valid: column 0 is an ONB, its transition matrix to row 0 is unitary, and pairwise tensor-product orthogonality gives entrywise disjointness. These are exactly the premises needed for SOURCE04’s accepted **local combinatorics**. Its count bounds supply a permutation support matrix for B1/B2/B3 and at least two for B5; no phase realization or GA auxiliary argument enters that import.

The transformation
\[
Q'_{\tau(s)}(\rho(i),\sigma(j))=P_\sigma Q_s(i,j)
\]
uses common row/column permutations and allowed per-square unitary transformations. The square permutation τ merely reindexes the unordered MOQLS set; it is explicitly distinguished from the isotopy operations. It preserves row 0, column 0, SB2, Q1’s weight-three witness and permutation status. The imported stabilizer pairs preserve each Q1 mask in its final row, so they preserve the **same template** and its ROWLEX keys.

The representative argument is complete: B1/B3 are transitive on B; B2 has orbits `{4,5}` and `{6,7}`; B5 has orbits `{4}`, `{5,6}`, `{7}`, with two distinct available permutation-square labels ensuring one lies outside `{7}`. Thus the stated representatives `{2}`, `{2,4}`, `{2}`, `{2,3}` suffice.

The adapter preserves the intended formula construction.

`Sink.c` uses the original CLI serialization without filtering, sorting or deduplicating base clauses. Control evaluation changes only its separate assignment bookkeeping. Every template literal comes from semantic support membership and GB’s own table; GA unit IDs are unused. The 126 binaries cover exactly six rows and 21 coordinate pairs per row, using negative GB literals with the frozen within-clause ordering. Nonemptiness, SB2 and coordinate-0 constants make these precisely the intended singleton column-0 restriction.

The classical positive control is correctly scoped to evaluation with **one Q1 P4 ALO and seven nonconstant Q1 SB2 units relaxed**; those clauses remain in the emitted bytes. Its extension procedure fails closed on contradictions or unresolved clauses. Threshold rejection controls concern components; sign-flip controls concern byte binding. Their runtime outcomes were not verified in this static audit.

Consequently, conditional on the accepted U/T16 imports, every normalized genuine configuration yields a GB assignment, and every genuine configuration in a hard P1 template can reach one of its specified strengthened GB inputs. **UNSAT of all six would exclude those genuine configurations.** This establishes no arbitrary-GB-model transformation, solver result, proof certification, or n8 gate. SOURCE08 remains input-identity evidence only.