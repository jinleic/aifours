# Exact finite-local geometry for the N50/t26 and t28 frontiers

**Status: prospective GENERAL AUTHOR candidate; both new verifiers are UNRUN.** This is neither a computational result nor a parent disposition. The written arguments and expected finite classifications below need independent mathematical and complete source review. They concern local necessities of one actual tensor and do not enumerate global P/E supports, establish an AME witness, or establish a global exclusion or minimum. The source bundle is self-contained, standard-library only, and is not old or sibling code.

## 1. Quantifiers, actual object, and conditional interfaces

Fix `t` equal to 26 or 28. Suppose there is **one** normalized complex AME(4,6) tensor in a fixed product basis, `U=6ψ`, with exactly 50 nonzeros and exactly `t` entries of modulus one. `P` denotes its `t` saturated words and `E` its `50−t` other nonzero words. Every assertion about a pair system, slice, missing word, matrix entry, amplitude, or phase below refers to these very same four physical alphabets and this one `U`.

A saturated entry exhausts its row and column in each unitary flattening. Thus every one of the six physical pair projections has `t` singleton P cells and `L=36−t` E cells; P and E cells are disjoint, and each E cell has at least two E extensions. For an E symbol `x` at party `i`, write `d_i(x)` for its number of E partners at any other party (the number is independent of that party because the same P words supply `6−d_i(x)` partners), `s_i(x)` for its E occurrences, and `h_i(x)=s_i(x)−2d_i(x)`. Since `d_i(x)=1` would fix all other coordinates and yield at most one E word, `d_i(x)≥2`. Counting the actual words gives

```
Σ_x d_i(x)=L,              Σ_x h_i(x)=50−t−2L=t−22,       h_i(x)≥0.
```

Consequently `q_i=|Q_i|≤L/2`, where `Q_i` is the actual E alphabet. For t26, `L=10`, `Σh=4`, `q_i≤5`; for t28, `L=8`, `Σh=6`, `q_i≤4`. Every used `i,j` pair additionally obeys `q_i q_j≥L`.

**Named conditional import — t26 low-excess cut structure.** The t26-specific per-pair alternatives used by the mask and q5 checks are the actual-unitary support lemma stated in packet S1 §1 and parent disposition S3: each residual cut consists of either two 3-by-3-minus-one plus two 2-by-2 components, or one connected 4-by-4/12-entry component plus three 2-by-2 components. In particular each physical pair system has either four multiplicity-three E lines or two multiplicity-four E lines, all other E lines having multiplicity two. S1 supplies the order-four degree argument, but the complete earlier low-excess source bodies invoked there are not in this packet. Their use remains an explicit import, not a newly established source identity or a claim that a local mask alone is sufficient.

**Named conditional import — t28 cut structure.** The t28 q4/common-hole interface assumes the actual-unitary alternative stated in packet S4 and reconstructed in S2 §2: every residual cut is (F) two full 3-by-3 plus one 2-by-2, or (B) one 4-by-4/14-entry component plus two 2-by-2 components. S4's reduction itself cites previous low-excess facts whose complete source bodies are not present here. The order-eight portion of the old f812 run was incomplete; no f812 source was opened, no f812 order-eight search is repeated, and its partial search is not treated as a zero count. The statements below that need F/B are conditional on this named interface and on their displayed actual-object arguments.

## 2. All binary three-cube slices: a common local strengthening

Let `d_i(x)=2`. Its neighbors at each of the other three parties form actual two-symbol alphabets. Its E slice is a set `S⊂{0,1}³` of `4+h_i(x)` distinct vertices. In each of the three physical pair systems the two rows with fixed `x` and a fixed value of the varying bit are actual unit-norm rows of `U`; they cannot have exactly one common nonzero column. These are not three independently selected slices.

* `h=0`: four vertices. The code retains every support satisfying the two-extension and no-singleton-overlap necessities; it does not declare every retained slice realizable.
* `h=1`: five vertices are impossible. Both rows on each axis must have sizes 2 and 3; their intersection is nonempty and cannot be a singleton, so the induced cube has at least two edges per axis, at least six. Deleting three vertices removes at least `3·3−2=7` edges because any three cube vertices induce at most two edges; at most five of the twelve remain.
* `h=2`: the six vertices are the cube minus a distinct pair of missing words. **Their Hamming distance must be exactly two**, for either t26 or t28, under the actual-row assumptions above. There are 12 missing pairs of distance one, 12 of distance two, and four of distance three. For distance one an entire fiber over two coordinates is absent. The four squared-modulus fiber sums form a 2-by-2 table with both row sums and both column sums one, so opposite sums agree; the opposite fiber would also vanish, contradicting the six nonzeros. For distance three, relabel the missing words `000,111` and the six nonzero coefficients at `001,010,011,100,101,110` by `a,b,c,d,e,f`. The three actual row inner products give

  ```
  a conjugate(e) = −b conjugate(f),
  a conjugate(c) = −d conjugate(f),
  b conjugate(c) = −d conjugate(e).
  ```

  Multiplying the first and third and dividing by the second, using only nonzero entries, yields `b conjugate(e)=−b conjugate(e)`. Equivalently the three unit-phase equation rows have an odd integral dependency. This strengthens the packet S1 distance-two-or-three statement to distance two on its actual t26 high slices; it is a new **written candidate**, not an executed finite result or an adopted theorem.
* `h=3` and `h=4`: the seven- and eight-vertex masks pass these particular line/overlap filters. This does **not** establish arbitrary-phase realizability or common-tensor completion.

The distance-two slice, with entries in binary order

```
(0, 1/√2, −1/√2, 0, 1/2, 1/2, 1/2, −1/2),
```

has the three required pairs of unit-norm orthogonal rows by exact arithmetic in `Z[√2]` after scaling by two. It is a **local slice only**, not an AME tensor or even a full three-cut completion. The first verifier is designed to visit all 256 masks, classify by `h` and, for six vertices, missing-pair distance and exact rejection reason; its expected counts are not claimed as observed execution.

## 3. Exact q and P moments; all degree types

Let `n_k` count the actual P words having exactly `k` coordinates inside their respective actual E alphabets, and let `q=(q_1,…,q_4)`. Counting the same P words, party incidences, and pair incidences yields

```
Σ_{k=0}^4 n_k = t,
Σ k n_k = 6Σ_i q_i − 4L,
Σ C(k,2)n_k = Σ_{i<j}q_i q_j − 6L,
n_0+n_3+3n_4 = t − (6Σ_i q_i−4L)
                     + (Σ_{i<j}q_i q_j−6L).
```

All `n_k` are nonnegative integers. The first source iterates every sorted `q_i` from two through `L/2`, applies pair capacity and the elementary P-incidence bounds, and obtains **every** nonnegative moment solution by choosing `n_3,n_4` and solving the other three linear equations. This is an arithmetic relaxation: it does not assert that any profile admits even one actual P set. In particular the following written profiles are useful anchors; order is `(n_0,n_1,n_2,n_3,n_4)`:

| t | sorted q | all moment-possible profiles |
|---|---|---|
| 26 | 3444 | `(0,2,24,0,0)` |
| 26 | 3445 | `(0,1,20,5,0)`, `(0,0,23,2,1)` |
| 26 | 4444 | `(0,2,18,6,0)`, `(0,1,21,3,1)`, `(0,0,24,0,2)` |
| 26 | 4445 | `(0,2,12,12,0)`, `(0,1,15,9,1)`, `(0,0,18,6,2)` |

These rows do not replace the program's other capacity-eligible q profiles. In particular 3444 is moment-possible, not excluded by a negative moment. Its further same-P incidence contradiction is the separate argument in S1 §5: the two one-inside P words are both inside the q3 party, and for a q4 symbol of degree `d` the three words pairing it to that party's outside symbols would require `3=2(4−d)`. Conversely, any use of the packet's final t26 alphabet list also depends on its other same-tensor arguments, not merely these moments.

All sorted t26 degree types are `(5,5)` for q2; `(2,3,5),(2,4,4),(3,3,4)` for q3; `(2,2,2,4),(2,2,3,3)` for q4; and `(2,2,2,2,2)` for q5. For t28 they are `(4,4)` for q2, `(2,2,4),(2,3,3)` for q3, and `(2,2,2,2)` for q4. Degrees must also fit **all** other actual E alphabets; a single pair graph does not enforce that coupling. For a t26 q5 symbol, `d=2` and `h∈{0,2,3,4}`, so the q5 surplus partitions are `(4,0,0,0,0)` and `(2,2,0,0,0)`. For t28 q4, the unordered surplus partitions before the common-hole argument are `(4,2,0,0)`, `(3,3,0,0)`, `(2,2,2,0)`. The t28 profiles 3333 and 3334 have respectively `n_0+n_3+3n_4=−6,−3`, and therefore no moment solution.

## 4. t26 order-four masks and q5 pair graphs

For an actual order-four/12-entry support, a unitary's distinct rows or columns cannot meet in one nonzero. A degree-two row in a connected component of order greater than two has twin column neighbors, and two such rows have disjoint neighbor pairs; the transposed statements also hold. The first source visits all `C(16,4)=1820` labeled four-zero masks, records **all** row/column degree types and first necessary-filter rejection reasons, and expects the 96 surviving masks to split as follows:

* 24 with `3333/3333`: the four holes form a permutation matrix;
* 36 with `2244/3333` and 36 with its transpose. The two low rows have disjoint pairs; their positions and their first pair have `C(4,2)·C(4,2)=36` labeled choices.

The counts are a proposed exact classification plus written counting, **not a reported run**. These graph necessities are not a characterization of simultaneous three-cut realizability.

For t26 with a q5 party, every vertex on that side has degree two. Give each E edge the surplus `w=multiplicity−2∈{0,1,2}`. The first source exhausts q5-versus-q5 two-regular graphs for the two canonical q5 surplus profiles `(4,0,0,0,0)` and `(2,2,0,0,0)`. Its positive-weight enumeration is exhaustive because a vertex with h zero cannot touch any positive-weight edge. For two q5 parties the possible high-weight arrays are: no array for `(4)/(4)`; `[2 2]` and its transpose for `(4)/(2,2)`; and, for `(2,2)/(2,2)`, either all four entries one or the two diagonal entries two, up to high-symbol relabeling. A displayed zero is **zero surplus**, not necessarily an absent E edge. These are only local pair conditions: the `(4)/(2,2)` class is not asserted to extend to one tensor.

The second, independently self-contained new source completes the bounded q5-versus-q3 and q5-versus-q4 pair cases. It visits all `3⁵` and `6⁵` labeled row-neighbor tuples respectively, retains all partner degree sequences with degrees at least two, and enumerates every allowed row surplus assignment. It separately accounts for the t26 per-pair spectrum and for the independently derived impossibility `d=2,h=1`, recording partner **paired** `(degree,surplus)` types. Fixing the q5 surplus positions is without loss under row relabeling: the factors are 5 for a unique h4 symbol and 10 for two h2 symbols. The full q5-versus-q5 case is in the first source. Neither source silently drops q3/q4 partner types because of a different party's unverified alphabet, and neither claims these local graphs have an actual four-party extension.

## 5. t28 q4 X/Y graphs and the common-hole condition

Assume the t28 F/B interface in §1. For a q4 party, all four degrees equal two. The h2 slice has distance-two missing pair by §2; in the unique axis where the missing vertices agree its two rows have sizes 2 and 4, and in the other axes the two rows have sizes 3 and 3 with nonidentical, intersecting neighborhoods. Thus every actual cut is B and the two missing physical words are the two internal zero cells of that 4-by-4 component. An h3 slice similarly gives one actual internal missing word in every cut. Distinct h2 symbols of one party cannot supply the same two words, so `(2,2,2,0)` is excluded **conditional on that actual common-hole interface**. Denote the other types `X=(4,2,0,0)` and `Y=(3,3,0,0)`, high symbols first.

For each pair of q4 parties, every vertex has degree two and the edge weight is 0, 1, or 2. An X h4 vertex has two weight-two neighbors; a Y h3 vertex has weights one and two and therefore meets both opposite high symbols. In X/X, the two actual h2 symbols determine the same two physical holes; those holes agree in both q4 coordinates, so their common pair value is a multiplicity-two E line in the B core. Its edge must exist and have weight zero. This **extra actual common-hole condition**, not degree two alone, eliminates X/X graphs with an h2-to-low edge. Up to relabeling equal-h Y symbols the high-high surplus arrays are

```
X/X [[2,2],[2,0]]     X/Y [[2,2],[1,1]]
Y/X [[2,1],[2,1]]     Y/Y [[2,1],[1,2]] or [[1,2],[2,1]].
```

The remaining two low vertices on either side form a low-low `K₂,₂` and no high-low edge exists. The first source enumerates all `6⁴` labeled row-neighbor tuples, the 90 two-regular graphs among them, and all nonnegative bounded weights, explicitly counts X/X candidates rejected **only** by the common-hole condition, and checks all four ordered X/Y cases. These are proposed necessary-graph calculations; no verifier output is claimed.

For context, the route from this local result to a contradiction must still use the **same** tensor. The four low-low pair values have eight E extensions total. In the actual q4/q4 cut they are the two external 2-by-2 blocks; in the complementary system no outside E word uses their columns. Every other pair system contains at least one low coordinate and also has multiplicity two with no outside extension. Therefore the same eight-word set has four pair values each repeated twice in **all six** physical systems. This closed-subsystem inference is conditional on the actual component locations, especially the common-hole X/X row; it is not a statement that an abstract degree-two row is automatically external.

## 6. All binary eight-word pair-balanced supports and odd phase dependencies

Let `L⊂{0,1}⁴` have eight distinct words, and suppose **for each of the six coordinate pairs**, each of the four binary pair values has exactly two extensions in `L`. Put `f=1_L`, `g=2f−1`, and write the signs as `±1` variables. The size and all pair balances kill Fourier degrees 0, 1 and 2, so

```
g = χ_{1234}(a_0+a_1x_1+a_2x_2+a_3x_3+a_4x_4).
```

Pointwise `g²=1` forces `a_0a_i=0`, `a_i a_j=0` for `i≠j`, and `a_0²+Σa_i²=1`. Thus exactly one coefficient is ±1. The only possibilities are a parity constraint on three specified bits with the fourth free (four coordinate choices and two parities, eight supports) or parity on all four bits (two supports). This is an exact classification of 8-word 2-balanced **supports**, not a global P/E classification.

For the three-bit parity support write words `(a,b,a⊕b,d)` and `r_ab` for the unit-phase ratio of its d=1 and d=0 entries. The actual two-term row orthogonalities give `r_01=−r_10`, `r_00=−r_10`, and `r_00=−r_01`. On phase-angle rows their coefficients `(1,−1,1)` sum to an **integer zero row** while their coefficient sum is odd. For four-bit parity let the first three bits label the words and set `A=z_000 z_111`, `B=z_001 z_110`, `C=z_010 z_101` for unit phases. Three actual two-term equations are `A=−B`, `A=−C`, `B=−C`; their phase rows again have the exact integer dependency `(1,−1,1)`. Positive moduli need not be equal: two nonzero terms summing to zero have opposite unit phases. No equality of the unnormalized complex products is being assumed.

For any phase equation matrix `M`, an integer vector `y` with `yᵀM=0` and odd `Σy_i` obstructs `Mθ=(1/2)1` in `(R/Z)^m`. A dependency merely modulo two is **not** enough; the one-row matrix `[2]` and vector `[1]` is the built-in intended-reason control. The first source is designed to inspect all `C(16,8)=12870` supports, test each of the six actual pair projections, derive all actual two-term phase rows, and emit a concrete signed three-row integer dependency for each of the 10 expected balanced supports, including all eight sign orientations of the chosen equations. No such output has been generated here.

## 7. New source bundle, controls, bounds, and execution gate

Both new files are in this wave, require only the Python standard library, make no file writes or network/subprocess calls, and are **UNRUN and UNCOMPILED**. The parent provided these metadata-only hashes; I did not independently compute them:

| source | bytes / LF | parent-supplied SHA-256 | scope |
|---|---:|---|---|
| `finite-local-geometry-v1.py` | 29,955 / 726 | `8c323037ecb6fbe57f0381d0f004958934b19540e544bac98acf444de1a4819a` | cube, moments/degree types, t26 order4, t28 q4 X/Y, all 8-word supports/phases, q5/q5, local Gram fixtures |
| `finite-q5-q3-q4-pairs-v1.py` | 8,314 / 206 | `f490808e1b9108146c48ff4afb84f7469416544cdf9d52ce11225173d9525f4a` | remaining q5/q3 and q5/q4 weighted local pair cases |

The first source uses exact integer, `Z[√2]`, and `Z[ω]` arithmetic for the displayed six-vertex slice, the packet's disjoint-hole M and same-row-hole R matrices, a 3-by-3-minus-one matrix, both order-four t26 degree types, H2, and F3. Row Grams and zero counts are the local assertions. Such matrices and slices are labeled **local, not AME**. Targeted controls request exact reasons for one-overlap, zero-fiber norm, odd phase, three separate P moments, a one-overlap mask mutation, weighted row surplus, absent X/X common hole, pair imbalance, non-integral/mod-two-only or even dependency, and an off-diagonal Gram mutation. The companion has positive and intended-reason controls for q5 pair nonedges, row surplus, mixed t26 spectrum, and an h1/degree2 partner. A wrong reason is a control failure. No control is reported as passing before execution.

Each process has a 39-second internal **cooperative** monotonic deadline, nonthrowing SIGINT/SIGTERM latch, guarded enumeration, flushed JSONL stage/partial records, and terminal `INCOMPLETE`/`FAILED`/`FAILED_EXCEPTION` with nonzero exit. Completion is explicitly named local necessities only. The timer is not a hard real-time guarantee between guards or under an abruptly killed/broken output stream. Before **each** prospective execution, the parent must read its complete actual source, pin the actual source and interpreter, specify exactly what is authorized and audited, issue a separate one-shot GO, and enforce an outer bound of at most 55 seconds. The two source files require two separately authorized executions; no claim is made that their combined wall time is bounded by 55 seconds. A timeout, missing terminal status, failed reason control, or partial count is not COMPLETE.

## 8. Coverage, access sequence, and limits

Before reading any mathematical packet body I read the complete current manifest, freeze receipt, final binding, parent live metadata, actual dispatch receipt, and all 23 listed control files. The controls were status/permission only: the method-restoration and addendum-2 controls; L1, privacy, Gram, AME-compression and PH-report quarantines; f439, f444, f448, f508, f513, f586, f602, f596, f653, f654, f659, f660, f662 quarantine controls; occupancy omission, prerun design-correction, and f826/f832 ACK-transport controls. An initially collapsed administrative presentation was recovered by complete raw reads. I wrote `prebody-ack-v1.md` and **directly delivered** the ACK to Main before opening the packet body. The path was absent in the immediately preceding complete wave-directory listing and this worker is the sole designated writer; the write API did not expose a kernel `O_EXCL` option, so I do not claim an independently certified atomic exclusive create.

After both acknowledgments, I read the sole ordered literal packet completely and serially in raw windows `1–20, 21–40, …, 381–400, 401–407`, including its last line. The windows displayed below 30,000 bytes, with no observed clipping; their exact byte sizes were not independently instrumented. No clipping recovery was needed for the packet. Parent-supplied packet metadata: 72,606 bytes, 407 LF, SHA-256 `89b5515fbb78cf530d1803446872aa09663d4f6cb88589e5dee5e3117ec42c9e`. The complete original source bodies rendered in it were S1 f826 LF1–163 (`b826085181355b587d96df2825c7ef5fb1b9ffc13ff9531818f640d39a392fa8`), S2 f827 LF1–145 (`c78020e48e7ca16159cf74debcb25cc2b747be06b4c371230142298c1ea95814`), S3 t25/t27 disposition LF1–33 (`9dcffb913663a29d438d53354e44aaacff0ba7cd0c5b37d4b803ea98936af336`), S4 excess6/t28 cut disposition LF1–23 (`f84c4b2eba89f99b693fa1c9fdfd5b4ef90eb5e6f7d9c5a99ca7373cc11fd0dc`), and S5 t22 phase-criterion disposition LF1–21 (`85878560f5fb5cb5b60893aa774b1f961322f8ea10c79aef792c93264e8cd8f9`). These SHA values are supplied administrative pins, not my independently recomputed hashes or original-source-identity certification.

No linked scientific source, held episode body, held proof/method/selection/planning/verification/reporting/confidence/downstream consumer, old code, sibling output, network, external model, scientific execution, code test, compilation, solver, child subprocess, build, lint, formatter, Git or deletion was used. Hash requests to Main were metadata only and were not execution authorizations. The only scientific inputs were the five rendered packet bodies; §1 explicitly names any missing load-bearing imports. No human, model-family, formal/kernel, independent-review, publication-priority, source-identity, global P/E enumeration, AME feasibility, global support lower bound, or parent-adoption claim is made. Further corrections must be additive and must not overwrite these files.
