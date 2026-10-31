# f226 review: support 45 at at most 28 maximal coefficients

## Disposition and per-claim findings

**Target outcome: reconstructed at the stated conditional scope, with 0 FATAL / 0 MAJOR / 0 MINOR / 0 INCONCLUSIVE findings within that scope.** This is a same-harness written review, not an independent-model-family, human, formal/kernel, or novelty verification. The target is the implication `t≤28 ⇒ N≠45`; it is elementary once the AME flattening condition is given. Its application to every AME(4,6) state imports the adopted `t≤28` item, with its provenance; the separate `N≥46` deduction additionally imports the adopted lower-45 disposition.

| Claim | Review finding and scope |
|---|---|
| For each 2-versus-2 cut, `U=6ψ` is unitary; maximal coefficients give disjoint singleton rows/columns and a residual unitary. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE. Reconstructed below, including empty and one-dimensional residuals. |
| `N≥72−t` and, at `N=45` under `t≤28`, the two-case table. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE. Counts are per fixed state and product basis, with no substitution of a different cut or state. |
| A zero-excess residual is a disjoint union of full 2×2 unitary blocks and has even dimension. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE. The empty case is included; phases and magnitudes need not be equal. |
| A residual of excess one cannot exist. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE. The proof treats dimensions below three, repeated pairs, and rows disjoint from the distinguished row. |
| For any normalized AME(4,6) state in any product basis, `t≤28` implies `N≠45`. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE. This conditional statement needs no no-OLS import. |
| Apply the adopted item 3 to all states/bases and obtain `N≠45`. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE **as an implication from that adopted premise**. It inherits that item's classical no-OLS(6) and prior-`t≤30` provenance. The premise itself is not re-proved here. |
| Combine that exclusion with the separately adopted `N≥45` to obtain `N≥46`. | 0 FATAL / 0 MAJOR / 0 MINOR / not INCONCLUSIVE **as a separate conditional deduction from both imports**. This is not an unconditional new disposition. |
| Standalone truth/proof of the imported `t≤28`, `N≥45`, or the classical no-OLS(6) theorem. | **INCONCLUSIVE as independent proof in this review**: these are expressly scoped imports/provenance, not reconstructed here. The lower-45 record is not needed for the target implication itself. |
| `N=46`, any `N=47` composition, global `N≥48`, exact minimum, or priority/novelty. | **INCONCLUSIVE / outside this review**; no pending union, unlisted source, status report, search, or assumed witness is used. |

## Exact inputs, measurements, and actual reading sequence

The assigned manifest `f226-ame46-n45-two-case-t28/manifest-v1.json` was the first research artifact. Its measured SHA-256 was `8ed3da45796cea53d3808e4377d1d18386a5bab0aea7b4455efe022da5c8fb45`, exactly the assigned full hash. Before reading any input body, `shasum -a 256` and `wc -cl` measured all three full files; every hash, byte count, and LF count matched the manifest. `wc` counts LF bytes, and the declared final line of each input was then displayed. The manifest declares no separate mandatory-correction body. The actual source-body reads, in manifest order and exact raw windows, were:

1. `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame46-support-47-excluded-and-at-most-28-maximal-coefficients-composition-parent-v1.md`: SHA-256 `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003`, 4,423 bytes, 17 LF; raw `1–15`, `16–17`.
2. `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame46-global-support-lower45-parent-v1.md`: SHA-256 `28ffc96f2b7295dd62c7efcfe39d066ac1a77449fbf0804a67c86cbce8c8a8cc`, 8,441 bytes, 34 LF; raw `1–15`, `16–30`, `31–34`.
3. `physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261029-n45-two-case-using-adopted-t28-v1.md`: SHA-256 `429ad666e0f44b7d93219a6efb9ffdd4f3dfe4acb763f4c1fb39588e3ce10634`, 5,060 bytes, 46 LF; raw `1–15`, `16–30`, `31–45`, `46–46`.

Paths above are relative to `/Users/jinleic/repos/aifours`. Each source was displayed completely, including its ending, in windows of at most 15 lines; no mathematical analysis began before the final window. No linked-but-unlisted body was opened or used as a premise. No process deviation is known.

## Reconstruction: singleton deletion and counting

Fix one normalized AME(4,6) state and one product basis. For a fixed 2|2 cut, write its 36×36 coefficient matrix as `A`. The AME condition gives `AA†=I₃₆/36`; hence `U=6A` obeys `UU†=I₃₆`. Since `U` is square, it is unitary on both sides. The same coefficients occur once in each flattening, so `N` and `t` refer to the same state and basis in every cut. This proof needs only one cut.

Every entry of a unitary has modulus at most one. Thus the `t` tensor coefficients of modulus `1/6` are exactly the modulus-one entries of `U`. Each exhausts both its row norm and its column norm, so all other entries in that row and column vanish. Two such entries cannot share a row or column. In particular `0≤t≤36`. Independently permuting rows and columns puts these `t` singleton phases in one diagonal block and leaves an `(n×n)` block `V`, `n=36−t`; unitarity of `U` makes `V` unitary. Its nonzero count is exactly `N−t`.

A row or column of `V` cannot be empty, and if it had just one nonzero then the relevant unitary line norm would force that entry to have modulus one. That entry would already have been counted among and removed with the `t` maximal entries, a contradiction. Thus every residual row and column has degree at least two. The statement is vacuous when `n=0`; when `n=1`, unitarity would force its only entry to be maximal, so that residual cannot actually occur. Summing the row degrees gives

`N−t ≥ 2n`, hence `N ≥ t+2(36−t)=72−t`.

At equality `N=72−t`, every row and every column has degree exactly two, because each of their degree sums equals `2n`. In particular, no strict inequality is silently used in the target cases. If `N=45`, the bound gives `t≥27`; assuming `t≤28` and using integrality leaves precisely

| `t` | `n=36−t` | `N−t` | `(N−t)−2n` |
|---:|---:|---:|---:|
| 27 | 9 | 18 | 0 |
| 28 | 8 | 17 | 1 |

Without the adopted `t≤28` premise, the elementary count alone does not eliminate values above 28; the review does not import any unlisted argument to do so.

## Zero excess, including equality and degeneracies

Two different rows of a complex unitary cannot have exactly one common nonzero column: their inner product would consist of one product of two nonzero complex numbers, which cannot vanish. This conclusion does not depend on entry phases or magnitudes.

Suppose `V` has exactly `2n` nonzeros and all lines have degree at least two. For `n=0` it is the empty union of blocks. Otherwise every row and column has degree exactly two. Pick a row with support `{a,b}`. Column `a` has exactly one other nonzero, in a different row. That row shares `a` with the first and therefore must share `b` as well; because its degree is two, its support is exactly `{a,b}`. Columns `a,b` are now exhausted by those two rows, and both rows are exhausted by those columns. They are an isolated full 2×2 support block. Remove it and repeat: all rows and columns partition into such blocks. Each block is itself unitary, though its four nonzero entries need not have equal magnitudes. Consequently `n` is even. The `n=1` case is impossible independently as noted above.

This is an exact equality classification, not just an inequality: even dimensions are realizable at the one-unitary level by direct sums of `H₂=(1/√2)[[1,1],[1,−1]]`; the empty sum handles `n=0`. No such construction is claimed to be an AME tensor in all cuts. At `t=27`, `n=9` and `N−t=18=2n`, so the required odd-dimensional residual is impossible.

## One excess, including degeneracies and repeated supports

Suppose a residual unitary has `2n+1` nonzeros and every line has degree at least two. For `n=0` there is no row in which the extra nonzero can occur; for `n=1` or `n=2` no row can have three distinct columns. Otherwise the row-degree sum forces exactly one degree-three row `R`, with every other row of degree two. Let `R` have support `S={a,b,c}`.

Every column in `S` has degree at least two, so each is met by some other row. Any other row meeting `S` meets the row `R`; the no-single-overlap rule forces at least two common columns. Since that other row has degree two, its complete support must be one of `{a,b}`, `{a,c}`, `{b,c}`. Rows disjoint from `S` are irrelevant, and arbitrarily many repeated copies of one pair still cover only two elements of `S`. Covering all three columns therefore requires rows with at least two distinct such supports. Two distinct two-subsets of a three-set intersect in exactly one column, and because their full supports are those pairs, the corresponding rows have exactly one overlap. Their inner product is then one nonzero product, contradicting unitarity. Thus excess one is impossible for every dimension; the symmetric column-degree sum would likewise have a unique degree-three column but is not needed.

At `t=28`, `n=8` and `N−t=17=2n+1`, so this case is also impossible. Together the two cases prove `t≤28 ⇒ N≠45` for every state and product basis. This two-case proof itself uses only the AME flattening premise and elementary complex linear algebra, not no-OLS, a solver, or a candidate witness.

## Exact application of the adopted premises

The first declared disposition's **item 3**, and not its separate support-47 items, states that every normalized complex AME(4,6) state has `t≤28` in every product basis. Applying it to the fixed state and basis in the proof above yields the same universally quantified exclusion `N≠45`. This application is conditional on that item's stated inherited f113 provenance: classical nonexistence of two orthogonal Latin squares of order 6 and the previous `t≤30` boundary. Neither that classical theorem nor the proof chain establishing the adopted `t≤28` item was independently reconstructed here; provenance and recorded review status are not proofs supplied by this review.

The second declared disposition separately states `N≥45` for every such state and product basis at the classical no-OLS(6) import. If that lower bound and the adopted `t≤28` item are both accepted, then integrality plus `N≠45` gives **`N≥46` for every such state in every product basis**; if the set of such states is nonempty, its minimum support is therefore at least 46. This is an additional conditional composition, not part of the self-contained `t≤28 ⇒ N≠45` argument and not an independently verified replacement for either adopted premise.

The lower-45 import is genuinely needed for this deduction: at the level of one flattening alone, `I₂₈ ⊕ H₂ ⊕ H₂ ⊕ H₂ ⊕ H₂` is a 36×36 unitary with exactly 28 modulus-one entries and 44 total nonzeros. The other cuts are not checked and this is **not** an AME witness; it merely shows why the single-cut argument must not be advertised as independently proving `N≥45`. No `N=46` exclusion, pending `N=46`/`N=47` union, global `N≥48`, exact minimum, witness, or priority is assumed or concluded.

## Reviewer-owned bounded exact control

After all assigned inputs had been displayed, I wrote and ran only the reviewer-owned `reviewer-control-support-v1.py` in this wave directory; no author code was run, imported, or compiled. Its SHA-256 was `fe07756b04b973953d0757c944f6a9c823c7e768b7e2a27c4989f83c85f04f56`. The actual `/bin/date` start and end were respectively `2026-10-29T13:52:16-0700 PDT` and `2026-10-29T13:52:16-0700 PDT`; measured monotonic duration was 0.250 s, the imposed cap was 120 s, the process exited 0, and stderr was empty.

It exactly enumerated labeled row supports of degree two in dimensions `n=0,…,5`, and supports with one degree-three row fixed as row 0 by row relabeling, requiring column degree at least two and forbidding a one-column overlap between two rows. Zero-excess survivor counts in order `n=0,…,5` were `1, 0, 1, 0, 18, 0`; the one-excess survivor count was zero in every tested dimension. It also verified exactly that the integer Hadamard numerator has Gram matrix `2I₂` and accepted positive 2×2 and 4×4 block supports. Its degree-two triangle and one-excess three-row example were each rejected specifically for `single-row-overlap`; a support with insufficient column degree was rejected specifically for `column-degree-below-two`.

These are necessary-support and small-dimension checks, not a unitary-existence oracle, not an enumeration of the target dimensions 8 or 9, and not a substitute for the universal written proof. An interrupted or timed-out control would have meant UNKNOWN; this run completed normally. No other scientific control, external literature/model/API, held material, author PASS or receipt, or sibling review was used as evidence.
