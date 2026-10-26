# Static admission audit — independent Kac level-four consumer v1

Reviewer PhysicsPPT44 under `peer-review-wave-eighteen-v6.json`. Clock actually observed during the full read: **2026-10-23T15:45:31-07:00**. Completion clock actually observed before this output: **2026-10-23T15:57:07-07:00**. This is a temporary static reconstruction, not a new problem owner. P44's normalizedN4 remains **HOLD/notGO**.

## 1. Verdict and exact observed pins

**HOLD — 0 FATAL / 2 MAJOR / 1 MINOR. Do not execute v1 under a new GO until the blocking bootstrap/settlement defects are repaired in new numbered owner snapshots and re-reviewed.** No substantive mathematical defect was identified in the definition-first reconstruction routes at their stated shared-model/import boundaries. That is a static assessment, **not** evidence that any certificate or mutation has run successfully.

All three assigned hashes were observed and match:

| Complete body read | Observed SHA-256 |
|---|---|
| `guessing-rminus/kac_level4_definitions_v1.py`, all557lines | `21819efb0f8564adbd408ff0d507262f3e5f624a40263d718c1f36f20b94e4de` |
| `guessing-rminus/kac_level4_consumer_v1.py`, all462lines | `ced9033e4bd2d72f94a55ee3e7d5c34235229431fb3647a725a235adc0bd6f62` |
| `guessing-rminus/kac-level4-independent-admission-v1.json`, complete | `58de281b6c6fd99b8e03687faa525129af0d8a1e24cd2aa2e26a7da0efa718ac` |

The first two roots in this table are under `information-science/evidence/three-area-20261023-96h/parallel-18/`. The other complete reads were:

- reconstruction plan119lines, SHA `6ebee70416cea5b20cc39f1ca5b5c8aea05a27c7f6eb5777f70c5f39f01494de`;
- complete input-pin JSON inventory, SHA `1872d5e87dbafcf3e4cf28705963a5b0cb3a0950b271bb6364ed12d83f6ef9da`;
- actual canonical model91lines, SHA `9ab6cbf7bd3b39e17714e64e314452362ba5525d6bb152a8e7e6d36f6acec18b`;
- certificate-to-band interface73lines, including an extra untruncated read of line25, SHA `c1a2efb271a44b76d8fcdf5dbb214f891e7f0b945f5088ee33d2b99bb122a3ca`;
- actual band candidate169lines, SHA `8b2fd9b4f2b4935e703689efd227ee96392053696b3bdded3e91e5921a9dfb73`;
- complete producer437lines for exposure/independence comparison **only**, SHA `af9e001f44c518eb56ffd7649926fe57625045a49c2ebd6b3954cbdb8a13874f`;
- complete preparation-boundary JSON; selected actual `(1,4,3,3)` fixture fields/tensor/image/minor contents through Read selectors.

The last four mathematical sources are in the mathematics `parallel-18/kac-moody/` root. I did **not** manually validate all64 certificate bodies or recompute all66 input-file hashes, and did not freshly accept the historical lower-level/invariant/full-band DAG. Current manifest/source identities and the consumer design were audited; actual stage2 is still unperformed.

Parent supplied the same bootstrap/settlement/resource observations during this audit; I independently traced their actual lines and consequences. This is not blind or cross-vendor review.

## 2. Blocking findings

### MAJOR M1 — the core is imported and trusted before its pin is checked

**Locations:** consumer19,49–50,407–419; particularly19 versus417–419.

`import kac_level4_definitions_v1 as m` executes before argument parsing and before all source/core/interpreter comparisons. Moreover the later bootstrap comparisons call consumer `require`, which delegates into this **already loaded** `m.require`. The recorded core digest is computed from `HERE/'kac_level4_definitions_v1.py'`, not from a bound loaded module origin or the verified source bytes actually executed.

Consequences:

1. A changed core can execute import-time behavior before a mismatch is reported; no scientific deadline or signal setup covers this import.
2. The pin checks themselves rely on code from the not-yet-authenticated core.
3. Hashing a sibling pathname is not an attestation of `m.__file__`, import hooks, or any cached bytecode that normal import may have consumed. `-B` prevents bytecode writes, not all bytecode reads.

This fails the explicitly requested **before-import/use** binding. It is not fixed merely by noting that the currently read core is benign or by recording its digest later. A parent prelaunch metadata check is useful but does not make this bootstrap ordering true.

**Required new-version repair:** use a trusted stdlib-only bootstrap with explicit non-assert pin comparisons before loading the core. Resolve/bind the exact core origin and load the exact verified bytes rather than an unrestricted pre-check import/cache path. Only then delegate mathematical gates into it. Preserve v1; the InfoGuessing owner must create new numbered sources/request pins. No import or tamper experiment was performed in this review.

### MAJOR M2 — claiming the output precedes the protected initialization/settlement region

**Locations:** consumer398–419 and447–456; exclusive mkdir401, deadline/guard/handlers402–406, identity/hash reads407–412, launch-write413–415, protected try only416.

After the program successfully creates a new exclusive output directory, several fallible operations remain outside the try/finally that writes settlement. Examples are reading source/core/interpreter bytes and opening/writing launch.json. An OSError there escapes without the promised settlement. There is also a setup window after claiming the directory but before installing the signal handlers.

This does not turn a completed mathematical rejection into PASS, but it breaks the requested reliable lifecycle and leaves an owned partial output with no final status. Existing-output refusal is a different case: the consumer must not write a settlement into somebody else's existing directory merely to satisfy this requirement.

**Required new-version repair:** complete trusted bootstrap metadata before claiming an output where possible; protect all fallible post-claim initialization and body work with a settlement path whose minimal state is already defined. Install the nonthrowing cooperative handlers early enough to cover that region. Explicitly distinguish launch refusal/no-owned-output from an owned incomplete run, and surface a final write failure to the parent wrapper rather than calling it a settled success. No deletion, overwrite or hard-kill mechanism is requested.

## 3. Minor finding and non-passing runtime limits

### MINOR m1 — resource rationale describes an explicit block split that is not implemented

**Locations:** admission `resource_basis`; core315–320 and84–112; plan113.

The request says the unshuffle matrices are split by letter multiset into blocks of at most24 words. The actual code constructs one constraints dictionary over the entire requested weighted word space and calls one `LinearSpan`, which calls the whole sparse Gauss–Jordan routine. There is no explicit block-partition/solve loop.

There **is** a valid mathematical block-sparsity fact: each unshuffle row stays within a fixed letter multiset, and elimination cannot couple distinct such components. That supports limited row support, but does not make traversal, allocation, or runtime identical to an implemented blockwise solve.

**Repair:** qualify the estimate as one block-sparse weighted solve, or actually implement and re-review a new blockwise version if that claim is needed. No mathematical redesign is necessary just to correct the resource description. The proposed1GiB is already honestly labeled an estimate, not a measured/hard-enforced peak; this review does not establish or refute that estimate.

Other runtime boundaries remain unverified:

- Input lengths/totals are checked after `read_bytes`; they are not a hard pre-allocation bound against an oversized changed file. Hashes still precede JSON-derived mathematics. Do not describe the byte-reading path or informational RSS as a hard memory sandbox.
- The stdlib process has no subprocess/network/solver API, and its exact current tensor degrees/minor sizes are finite. That is not a measured600-second completion guarantee.
- After installation, the signal handler only sets STOP. First and repeated signals are idempotent, do not throw into serialization, and mathematical guards convert the flag/deadline into INCOMPLETE. This is a good design property, subject to M2's initialization gap. Native I/O, filesystem failure or external forced termination cannot be represented as a successful settled run without the actual receipt.

## 4. Mathematical independence and whole-space reconstruction

The design is genuinely different from re-importing/re-running the producer, within explicit shared definitions:

1. **Alphabet/model:** core155–171 and221–266 derive positive lifts `(v,u,w,p,q,x,y,z)=(E31,-E32,E21,H1,-H2,-2E12,2E23,2E13)`. The old/new maps are inverse permutations with compensating scalings. Matrix-unit Kronecker-delta commutators replace the producer's dense3by3 helper; coordinate reconstruction and defining Levi identities are actual proposed gates.
2. **Entire primitive tensor space:** core181–202 and289–323 form all reduced unshuffle equations, including multiplicities of repeated letters. In characteristic zero their kernel is the entire free Lie subspace. This is an explicit PBW primitive theorem import, not an inference from exported dimensions.
3. **Source and target bases:** level4 uses every homogeneous canonical symmetric-wedge image with its bracket trees; level3 uses standard Lyndon bracketing with the longest proper Lyndon suffix. Independence and equality with the complete coproduct-kernel dimension are separately required. The canonical F-isomorphism is a read mathematical interface, not simply a saved source-dimension assumption.
4. **Raw generation is separate:** the producer uses all right-normed/Dynkin words and producer spans; this core does not invoke them. It shares the eight-dimensional elimination interpretation and certificate serialization, which are necessary exposed mathematical inputs. It is not a new proof of positive elimination from the original3-generator presentation.

If a basis or completeness gate fails in a future run, the run rejects; static reasoning alone is not evidence that those gates pass on all64 cases.

## 5. Whole ideals, actual quotient-lowest kernel and original row

**Whole ideals:** core325–362 and429–461 generate the literal original seeds `(ad v)^q(E_jv)`, verify they are nonzero/lowest, and take their positive Levi orbits. For a lowest seed, PBW reordering makes the full Levi span equal to that positive orbit. Truncation at a,b<=3 is justified here because every raising increases these coordinates and all added V-leaf degrees are nonnegative; no path above the box contributes back to a requested source, target or lowered parent.

The code explicitly generates every contribution of both rows to

`T3=[V,Q2]+Q3`, `T4=[V,[V,Q2]]+[V,Q3]+Q4`.

A possible `[L2,Q2]` contribution is included by Jacobi in the iterated V bracket term. Row4+ contributes no level<=4 seed. No unknown row1 ideal intersection is assumed zero; whole spans are reconstructed and supplied ideal rows must be independent and span-equal to them (consumer159–172).

**Actual quotient-lowest:** core463–489 forms both lowering maps from the whole free source into the two actual parent quotients. It checks that the whole source ideal maps into those parent ideals, then computes kernel dimension minus source-ideal dimension. That is the correct quotient-kernel formula and does not depend computationally on producer free-lowest lifting. The supplied representatives are separately free-lowest, independent modulo the whole source ideal, and must have exactly this dimension (consumer196–210). Thus successful execution would not silently check only a narrower chosen free slice.

**Original D3:** core364–420 retains h3 as an independent actor. Its leaf table is

`Dv=-h3`, `Du=-r e1`, `Dw=-s e2`,
`Dp=-s[e1,e2]`, `Dq=r[e1,e2]`, `Dx=Dy=Dz=0`.

These signs agree with the positive lifts and the printed original row. On another factor of full degree(a,b,k), h3 acts by `2k-ra-sb`, exactly the three slots `(2k,-a,-b)` in the code. No singular-A(1,1) identification of h3 with a Levi Cartan is made. Bracket recursion uses the proper opposite sign for a level-zero actor on the right. This differs from producer associative actor-to-the-right deletion.

Terminal cancellation is an actual scalar first-variation gate on every supplied source-ideal/primitive tensor, not a silently discarded residual. Whole source-ideal D3 stability is checked coefficientwise in each cell. `affine_cell` substitutes r/s=1,2,3 or4+X/4+Y correctly, retaining the variable slots rather than just evaluating the point4.

## 6. Faithful quotient coordinates and complete polynomial determinant

Consumer217–264 transforms the **whole** independently reconstructed target ideal into the serialized alphabet, computes its lexicographic RREF, and requires every supplied image to have zero pivot coordinates. The independently rebuilt raw original-row images are reduced by that same faithful quotient projection and compared exactly. This avoids a raw-coordinate-minor test on arbitrary quotient lifts.

Selected rows are distinct valid degree-three words outside the target-ideal pivots. Source columns remain in their actual supplied order. Every affine entry is built from the three reconstructed slots. Core499–557 uses full bivariate Bareiss elimination, tracks row-swap orientation, and checks every nonconstant polynomial division by exact long division to zero remainder. The polynomial ordering is lexicographic on exponent pairs; fixed cells prohibit spurious variables. The full result is compared with the supplied determinant, then the oriented constant must be positive and every oriented coefficient nonnegative. This proves the required uniform nonvanishing condition **if the consumer completes**, not merely at sampled parameter values. Empty source uses determinant1.

No determinant, rank, kernel, ideal equality or coefficient identity was computed by this reviewer.

## 7. All15 mutation paths inspected, not executed

The actual selected fixture has cell[1,4], degree[3,3,4],37 source-ideal rows,8 target-ideal rows,4 primitive representatives, a nonempty first affine component and a nonempty determinant. These fields were read from the real input, not guessed. They establish the nonempty preconditions for the chosen pop/first-entry mutations.

| Mutation | Actual path and required rejection |
|---|---|
|1. Alter first primitive coefficient | `validate_record -> parse_tensor -> coproduct`, `SOURCE_TENSOR_COPRODUCT`; adding one nonzero word to a Lie tensor changes its reduced coproduct |
|2. Remove source-ideal basis row | `validate_record -> same_ideal`, `IDEAL_SPAN` after a genuine independent row is omitted |
|3. Remove target-ideal basis row | Same complete-span path, `IDEAL_SPAN` |
|4. Double a nonzero affine component | Preserves degree/Lie/normal-form linear conditions, then differs from rebuilt raw image, `RAW_ORIGINAL_ROW` |
|5. Swap actual r/s lowering slots | Reconstructs with `swap_original_row=True` in the nonsymmetric cell; whole-ideal stability/image equality must give `RAW_ORIGINAL_ROW`, not merely a changed status field |
|6. Alter determinant coefficient | Full Bareiss equality, `DETERMINANT_IDENTITY` |
|7. Flip orientation | Polynomial remains unchanged, positive oriented constant fails, `DETERMINANT_POSITIVITY` |
|8. Change category4 marker to3 | Actual field gate, `SCHEMA`; whole open-cell semantics are additionally enforced by raw affine reconstruction |
|9. Omit a degree | Actual exhaustive record set, `COVERAGE_MISSING` |
|10. Omit a whole cell | Same exhaustive set gate, `COVERAGE_MISSING` |
|11. Duplicate a degree | Actual duplicate-key detection, `COVERAGE_DUPLICATE` |
|12. Duplicate a cell | Same actual coverage path, `COVERAGE_DUPLICATE` |
|13. Truncate artifact | Actual `parse_json` on truncated pinned-format bytes, `MALFORMED_JSON` |
|14. Duplicate JSON key | Actual object-pairs hook, `DUPLICATE_JSON_KEYS` |
|15. One-byte same-length tamper | Actual `pinned_bytes`, `INPUT_HASH`, before JSON mathematics |

`expect_rejection` accepts only the exact expected ConsumerError code; a survivor or unrelated typed error fails the control, and an unrelated Python exception becomes ERROR, not a passed mutation. I have not observed any of these outcomes. In particular the transposed-row mutant is an actual raw reconstruction mutation, but its eventual named rejection must still be observed rather than claimed from this static table.

## 8. Strict coverage, optimized execution and lifecycle boundary

`EXPECTED` is exactly16 row cells times4 degrees. The manifest lists64 certificates plus launch/settlement; its own observed digest matches the hardcoded pin. The code refuses unlisted/missing files, symlinks and duplicate inventory entries; binds every size/hash before parsing certificate mathematics; checks settlement status/coverage; and compares each filename key with its body. Record field sets, integer-vs-bool distinctions, canonical nonzero Fraction encodings, ordered unique tensor/polynomial terms, degree/parameter supports and minor schemas have actual explicit gates.

The consumer/core contain no correctness assertions or `__debug__` branches. Their explicit errors remain active under `-OO`; removal of the parser description docstring changes no mathematical gate. The producer's assertion-based generation controls are not imported or counted as the independent consumer's controls.

Fresh output uses exclusive creation and checked-record names. Complete status requires64 actual checks,15 actual controls and exact final coverage. Stop/deadline outcomes are INCOMPLETE; other failures are REJECTED/ERROR; exit0 is reserved for the complete status. Informational native RSS units are disclosed, not enforced. These good static properties do not cure M1/M2 or demonstrate runtime completion.

## 9. Exact admission conclusion

The proposed definition-first mathematical routes meet the intended **scope and algorithmic independence design**, conditional on the exposed characteristic-zero PBW/positive-elimination/Levi interfaces. They are not a narrower determinant-only consumer. However, **v1 is not statically ready for execution** because of M1 and M2; m1 requires a resource-description correction or an actually reviewed implementation change.

Repairs belong to InfoGuessingRminus in new numbered source/request versions, never edits to these reviewed snapshots. A later actual stage2 run requires a new named GO and fresh resources. Even successful stage2 would establish only the64 finite certificate premises. The inherited boundary/level-three/invariant/full-realization composition remains stage3, and no full family band, formal proof, novelty, all-height Serre conjecture or full book solution is accepted by this review.

Only source/format reads, clock and SHA metadata were performed. No module import, compilation, smoke test, arithmetic program, solver, certificate replay, CLI or nested agent occurred. Own normalizedN4 remains HOLD/notGO.
