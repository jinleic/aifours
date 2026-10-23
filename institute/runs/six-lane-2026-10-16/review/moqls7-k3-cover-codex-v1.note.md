DISPOSITION: ACCEPT-WITH-FIXES

This disposition concerns Q1–Q4. **Separate Q5 draft judgement: ACCEPT-WITH-FIXES, as conditional mathematics only.** No activation is authorised.

All copied-file SHA-256 values computed with `shasum -a 256` match `manifest.json`, including the six specified pins. References below are snapshot-relative paths with LF-based, one-based line numbers.

**FATAL**

None found in the reviewed constructions under their stated heavy-triple hypotheses.

**MAJOR**

1. **The lex artifact does not bind the original cube metadata as required.**  
   `lane/review/AMENDMENT-3.r1.md:46` requires binding both the original cube CNF SHA and metadata. `lane/code/k3_lex.py:128` records the source CNF SHA, wrappers and generators, but never reads or hashes the source metadata. The resulting `lane/explore/k3lex/A_C311.meta.json:4` likewise lacks that binding. Hashing the lex metadata in its screen receipt does not supply the missing upstream link.

   **Correction:** add a supplementary provenance record binding the source cube metadata SHA, `3b2ab04f…a0f4d9ed`, to the existing cube and lex CNF hashes. Future wrapper revisions should record and validate that source metadata explicitly. Preserve the frozen artifacts and their historical hashes.

2. **The draft’s activation contract needs explicit acceptance and heaviness dependencies.**  
   `lane/review/drafts/AMENDMENT-4.md:8` assumes the two original cube CNFs are UNSAT; its gate at line 50 requires successful certificates, while line 59 defers parent acceptance of the composition until an unrestricted theorem verdict. This does not explicitly require parent acceptance of the two upstream exclusions before activating the cuts.

   The mathematical transport also needs **every square heavy on every own row/column line**, rather than merely a heavy occurrence at the selected point. For application to arbitrary surviving K3 configurations, that domain comes from the minimality bridge and therefore requires K1 **and K2**. `lane/review/GRAM-ENCODING.r2.md:61` states this correctly; `lane/review/AMENDMENT-2.r1.md:5` also names both prerequisites. AMENDMENT-3 inherits them through the frozen cubes without restating them, and the certificate receipts only say whole-bridge acceptance is separate.

   **Correction:** add an explicit dependency statement to the draft and final integration record: accepted upstream C321/C411 exclusions; reviewed encoder soundness; all-line G4; and, when deriving G4 for unrestricted K3, accepted K1 and K2. K2 remains pending here. G6 itself needs neither exclusion once its singleton and G1/G2 hypotheses hold.

**MINOR**

1. **C411 preserves the complete cube-constrained domain, not the bare `--sym` unit set.**  
   `lane/code/k3_lex.py:33` includes columns (3,4), while `lane/review/AMENDMENT-3.r1.md:20` broadly says the operations preserve all G1–G5 conditions. The swap sends the required `g_1(p,(0,3))` unit to `g_1(p,(0,4))`; the latter is not a bare-base symmetry unit.

   **Correction:** state that preservation is for the projection of **base ∧ complete cube**. C411 makes all four columns 1–4 positive, so the transformed pattern still satisfies every original symmetry unit. This repairs the explanation without changing the comparator.

2. **The variable-order description overstates the B runtime check.**  
   `lane/review/AMENDMENT-2.r1.md:43` says the wrapper reads each encoder’s actual order and confirms agreement. A does expose its map and is compared at `lane/code/k3_cubes.py:115`. B supplies no map: line 126 checks only the variable-count lower bound.

   **Correction:** describe B’s agreement as established by static inspection of the pinned allocation, or add an explicit map comparison in a future wrapper revision. The present indices are correct; the discrepancy is between the described assurance and the implemented check.

The following checks support those findings and the disposition.

**Q1 — Cover.** At `lane/code/k3_cubes.py:19`, `CUBES` agrees exactly with the amendment table. Reading columns 1–6 in order, the three squares’ signed unit strings are:

| Cube | Square 1 | Square 2 | Square 3 |
|---|---|---|---|
| C311 | `+++---` | `---+--` | `----+-` |
| C321 | `+++---` | `---++-` | `-----+` |
| C411 | `++++--` | `----+-` | `-----+` |

The loop at line 75 emits all eighteen signs, including every negative literal.

Row 0 is an ONB, so unit norm makes each support nonempty. Its column-0 coefficient vanishes by column orthogonality. At Boolean level, the ordered G3 transition from row 1 to row 0 supplies the corresponding nonempty-neighbour clause. G5 makes the three supports pairwise disjoint, and the symmetry units supply `{1,2,3} ⊆ S_1`.

Hand enumeration of labels at columns `(4,5,6)`, with `0=unused` and `a=square a`, gives exactly:

- C311: `023, 032, 203, 230, 302, 320`;
- C321: `223, 232, 233, 322, 323, 332`;
- C411: `123, 132, 213, 231, 312, 321`.

These are three disjoint six-element orbits. A valid triple must contain labels 2 and 3; its third label is 0, 1, 2 or 3, producing exactly those cases. The extra square-1 coordinate in C411 is included. Two extra square-1 coordinates would leave insufficient room for both other nonempty supports, so `|S_1|≥5` is impossible.

`coverage()` uses this label convention correctly. Its `3-a` at `lane/code/k3_cubes.py:44` exchanges zero-based indices 1 and 2, leaving 0 fixed.

The residual operations preserve the whole projected base semantics: non-collinearity/G1; G2 over all fourteen lines; G3 over ordered line pairs; and G5. They fix square 1 and row 0, so preserve the exceptional omitted G4 constraint and the three replacing units; all other G4 obligations permute among themselves. Auxiliary values can be reconstructed.

The initial `--sym` normalization is valid for every triple satisfying all-line heaviness: choose a heavy witness on a row, send that row to 0 and the witness’s row to 1, then send its column to 0 and three neighbours to columns 1–3. Their columns differ from the witness’s column. This establishes the WLOG stated at `lane/review/GRAM-ENCODING.r2.md:89` within the required heavy domain.

**Q2 — Singleton G6.** The vector argument at `lane/review/AMENDMENT-2.r1.md:31` is sound: a singleton expansion makes the two unit vectors scalar multiples with scalar of modulus one. Rescaling either argument preserves whether every other inner product vanishes; arbitrary entry phases cause no difficulty.

The Boolean derivation at `lane/review/G6-G2-DERIVATION.r1.md:8` also covers the boundary cases:

- For `t` on row 0, both sides vanish by the cube and G1.
- Off row 0, the common-neighbour count for `p,t` is exactly `g(q,t)`.
- If `t` is collinear with `q`, that count is zero, forcing `g(p,t)=0`.
- If `t` is collinear with `p`, its Gram predicate is false; the exactly-one branch therefore forbids `g(q,t)=1`.
- If both predicates are absent, both sides are already false.

For A, the clauses at `lane/code/gram_enc.py:83` define the AND auxiliaries exactly. With the singleton units, only the `q` contribution can survive. The clauses at lines 96 and 99 become the two equality implications. When the left predicate is absent, the collinear branch forbids the sole common neighbour.

For B, `counter2` implements
`n1 ↔ a1∨x` and `n2 ↔ a2∨(a1∧x)`, including the initial false second bit. Thus its final bits mean exactly “at least one” and “at least two.” The collinear `(-s1,s2)` clause at `lane/code/gram_encB.py:151` forbids exactly one. Its latent one-item/`None` problem is unreachable here: in a row/column frame, two off-line points leave at least five structurally eligible common-neighbour positions.

`cube_clauses` handles all four availability cases correctly: neither present gives nothing; exactly one present gives its negation; both present give two implications. Skipping `p,q` avoids confusing diagonal constants, which are one, with absent off-diagonal predicates.

Among the remaining 47 points, 2 are collinear with both anchors, 10 with only each anchor, and 25 with neither. Hence each singleton contributes `10+10+2·25=70` clauses. Totals are 158, 88 and 158, matching the metadata and desk blocks.

Each square has `49·36/2=882` predicates. The wrapper, A and B all allocate square first, then row-major earlier point and later point, excluding equal-row/equal-column pairs. B allocates no auxiliaries before completing this prefix. Therefore static reading establishes index equality for all 2646 variables. In particular,
`g_a(p,(0,k))` has index `882(a−1)+36k+1`, agreeing with the desk’s displayed unit indices.

**Q3 — Lex leaders.** The generators listed in `lane/code/k3_lex.py:25` match AMENDMENT-3. Row/column permutations preserve non-collinearity and are invertible, so `image()` is a predicate bijection. Each generator fixes the anchor, preserves all eighteen cube signs and preserves the exceptional square-1/row-0 G4 location. The combined column/square swaps exchange the two singleton identities where appropriate. G6 is preserved directly and also follows from the preserved G1/G2-plus-cube conditions. The C411 qualification above is essential.

The action convention is valid. With `perm[v]=σ(v)`, the comparator uses `Y_v=X_{σ(v)}`. This is realized by pulling back the actual configuration:
`ψ′_{a,(i,j)}=ψ_{π(a),(ρ(i),κ(j))}`.
All current generators are involutions, so pushforward and pullback coincide for them; involutivity is not required for the orbit argument.

At `lane/code/k3_lex.py:54`, every equal comparison pair forces the next prefix true while the preceding prefix is true. Consequently the first unequal pair cannot be `(1,0)`. Conversely, if the first unequal pair is `(0,1)`, choose all subsequent prefixes false; if every pair is equal, choose every prefix true. This proves existential equivalence to `X≤lexY`.

The proof does not assume distinct variables across positions, so reversed pairs such as `(x,y)` followed by `(y,x)` cause no problem. Identical positions can be removed. No auxiliary is needed after the last pair. Numbering starts above the complete cube CNF’s `nv` and advances across generators.

For a simple row or column swap, each square has `C(5,2)·7·6=420` fixed predicates, hence 1386 moved predicates overall. For a combined column/square swap, only square 1 contributes those 420 fixed predicates, giving 2226 moved predicates. A comparator with `m` moved positions adds `3m−2` clauses and `m−1` auxiliaries. Thus C311 adds
`6·4156+6676=31612` clauses and
`6·1385+2225=10535` auxiliaries, producing header `107513 / 659168`. The metadata and desk excerpt agree.

A lex-minimal member of the orbit under the **single group generated by all generators** satisfies every comparator simultaneously. Base auxiliaries can be reconstructed from that pattern. No equality `X=T(X)` is imposed.

**Q4 — Composition and receipts.** `lane/code/k3_cubes.py:124` replaces only the header, copies the complete base body and appends cube/G6 clauses without new variables. `lane/code/k3_lex.py:123` similarly preserves the cube body and appends fresh comparator clauses.

The A base has 627398 clauses; the additions give 627486 for C321 and 627556 for C311/C411, with 96978 variables. The B headers likewise match additions of 88 or 158 clauses. The desk excerpts show the expected boundary between copied and appended clauses, including lex auxiliary 96979.

The certificate driver regenerates through the frozen wrapper and compares the CNF SHA to the screen receipt before invoking the pipeline (`lane/code/k3_cube_certify_r2.py:49`). The copied C321/C411 receipts bind the expected input hashes, metadata, screen receipts, code and logs. Their checker logs report the correct formula sizes and exact `s VERIFIED` at lines 41 and 62 respectively; receipts report rc20/rc0 and no safety stop.

These establish consistent **producer records**, not independent proof replay. The copied texts do not identify those records as parent-accepted exclusions. The C311 lex receipt remains `UNKNOWN safety stop`.

No unsupported four-square weight lemma enters these steps. `lane/review/LEMMAS.md:26` derives the required three-square disjoint-support bound directly.

**Q5 — Conditional draft mathematics.** The transport at `lane/review/drafts/AMENDMENT-4.md:18` works with the following explicit maps. Transpose first for a column frame. Then choose `ρ(frame row)=0`, `ρ(row(p))=1`, and `κ(column(p))=0`. Relabel the implicated squares `(a,b,c)` as `(1,2,3)`.

For `(4,1,1)`, map the four neighbours to columns 1–4 and the two singleton neighbours to 5 and 6. For `(3,2,1)`, map the supports to 1–3, 4–5 and 6. Nonemptiness and disjointness exhaust all six available coordinates in either case, establishing every negative literal as well as every positive literal. Both images satisfy the three `--sym` units. Every other required G4 witness transports from the all-line heavy configuration; the omitted square-1/row-0 obligation is supplied by those units. G6 then follows as before.

The arithmetic is correct: `w_a≥1`, disjointness gives sum at most six, `w_a≥4` forces `(4,1,1)`, and `w_a≥3,w_b≥2` forces `(3,2,1)`. Conditional on the two exclusions, the stated cuts follow. Every occurrence with any weight at least three is then `(3,1,1)`; lighter occurrences remain possible.

The direct clause count is exactly
`14·42·3·C(6,4)=26460` and
`14·42·6·C(6,3)·C(3,2)=211680`,
totalling 238140 without auxiliaries. Clauses are distinct: their edges identify the common centre and frame, while square-labelled multiplicities identify the selected subsets and ordered square roles. Four-literal and five-literal families cannot coincide. “Overlap impossible by G5” correctly refers to simultaneous truth of the selected positive literals when the subsets overlap.

These conclusions concern own **row/column frames**. All-ONB G4 does not extend the transported exclusions to arbitrary ONBs. Classical-symbol frames require a separate transport argument. Arbitrary non-minimal configurations cannot be included through an unproved heaviness assumption.

The complete cut family is preserved by the AMENDMENT-3 group: its operations merely permute frames, points, squares and subsets. Lex orbit coverage therefore remains valid after adding all these cuts.

Final use requires accepted upstream exclusions and bridge prerequisites, reviewed transport and cover lemmas, a frozen cut implementation with exact bindings, and separate certification of the precise strengthened C311 input, including lex clauses if used. The old C321/C411 receipts supply upstream premises; they do not certify that new input.

| Q1..Q5 | Status | One-line reason |
|---|---|---|
| Q1 | SOUND | Eighteen assignments form exactly the three claimed residual orbits. |
| Q2 | REQUIRES-FIXES | G6 and indices are sound; B’s validation description exceeds its runtime check. |
| Q3 | REQUIRES-FIXES | Lex construction is sound; qualify C411 preservation by the complete cube. |
| Q4 | REQUIRES-FIXES | Composition is sound; source metadata binding and dependency documentation need completion. |
| Q5 | REQUIRES-FIXES | Transport and counts are conditionally sound; acceptance/domain gates need strengthening. |

Scope: I read only the snapshot, including its review texts, six code files, controls, metadata, receipts, logs, parent verdict and desk excerpts. I ran no interpreter, solver, compiler or network operation, made no changes and did not delegate. The omitted CNFs, streamed proofs, transport implementation and independent parent replays could not be checked here.