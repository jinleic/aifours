# Support 45: a two-case obstruction using the recorded t≤28 disposition

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 13:48:05 PDT 2026`; this is not an asserted completion time. **WRITTEN author candidate**, not independently reviewed, adopted, formally verified or novelty-cleared. No numerical solver or certificate is a premise.

## 1. Claim, input and provenance

Let ψ be a normalized complex AME(4,6) state in any one product basis. Let N be the number of nonzero coefficients and let t count those of modulus 1/6. **Claim:** if t≤28, then N≠45.

The sole imported scientific input for applying this to all AME(4,6) states is item 3 of `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-ame46-support-47-excluded-and-at-most-28-maximal-coefficients-composition-parent-v1.md`, SHA-256 `4101ae2cdb08aa2c9238b680359dc2793bcccfc3af672fbb92be9dd460a41003`. It records t≤28 for every such state at the same-harness boundary, inheriting the f113 classical no-OLS(6) import and its prior t≤30 provenance. This packet does not reprove those imports.

This is a shorter successor route to the separately unadopted author candidate `frontier-20261028-n45-direct-unitary-exclusion-v1.md`, SHA-256 `29e966ae999aef3f7d852153aec677325ad4571b909e6733b9ec70c62fe8378b`. That earlier packet used the then-recorded t≤29 bound and also had to treat t=29. The newly recorded t≤28 input removes that third case. The author had prior exposure to the earlier proof; this is not a blind or novelty claim. The earlier packet is not a premise here: both residual-unitary facts are proved below.

No statement about N=46, the pending f222 union audit, the f182 disposition, or any withdrawn certificate-dependent candidate is assumed. No v203/v124 held material is used. This packet asserts no adopted global lower bound and gives no witness.

## 2. One actual residual unitary

For every 2|2 bipartition, the flattening `U=6ψ` is a 36×36 complex unitary. A modulus-1/6 coefficient gives a modulus-one entry of U. That entry exhausts the squared norm of its row and its column, so it is their sole nonzero. The t maximal entries occupy distinct rows and distinct columns. Let E be the other nonzero positions, and put `n=36−t`. After removing the singleton rows and columns, the remaining n×n block V is unitary and has exactly `|E|=N−t` nonzeros. Every row and column of V has at least two nonzeros: a unitary line with a single nonzero would have modulus one and therefore would have been removed as a maximal entry.

In particular `N=t+|E|≥t+2n=72−t`. If N=45, then t≥27; with the recorded t≤28 input, the only possibilities are:

| t | n | |E| | excess `|E|−2n` |
|---:|---:|---:|---:|
| 27 | 9 | 18 | 0 |
| 28 | 8 | 17 | 1 |

The same tensor and the same P,E partition work in all three cuts. The contradictions below already hold for **any one** of its cuts; no independently selected marginal is substituted.

## 3. Zero excess forces an even dimension

For a complex unitary, two distinct rows cannot share exactly one nonzero column: their inner product would be a single nonzero product.

If V has exactly 2n nonzeros, every row and every column has degree exactly two. Take any row with support {c,d}. Column c has exactly one other nonzero, in a distinct row. That row must also contain d, by the no-single-overlap observation, and has degree two, so its support is exactly {c,d}. Neither column has any further nonzero. Thus the rows partition into pairs with identical supports; n is even.

At t=27 the residual is 9×9 with 18 nonzeros. Its dimension is odd, contradiction.

## 4. Excess one is impossible

Suppose instead that V has 2n+1 nonzeros and all lines have degree at least two. Exactly one row R has degree three; every other row has degree two. Name R's three columns a,b,c. Each of them has at least one further nonzero because every column has degree at least two. Any degree-two row meeting R must meet it in at least two columns, by the no-single-overlap observation, so its support is one of {a,b}, {a,c}, {b,c}.

All three columns a,b,c must be covered by such rows, so at least two distinct supports from that list must occur. Any two distinct two-subsets of {a,b,c} intersect in exactly one column. The corresponding degree-two rows would share exactly one nonzero column, contradicting their orthogonality. Therefore excess one is impossible.

At t=28 the residual is 8×8 with 17 nonzeros, contradiction.

## 5. Exact conclusion and review boundary

Both permitted t cases are impossible, proving the stated N=45 obstruction conditional on the recorded t≤28 input. The unitary argument itself is elementary and uses no no-OLS theorem; the application to every AME(4,6) state inherits the input's stated no-OLS(6) and prior-t≤30 boundaries. Nothing here decides N=46, establishes a new adopted global bound, identifies the exact minimum, or establishes priority. Independent review should check the singleton deletion and the two elementary row-support arguments.
