# Exact M(7) = 2: final parent K3 composition and gate verdict v2

Recorded at 2026-10-18T13:22:39-07:00.

**v2 is a typographic restatement of [v1](moqls7-M7-equals2-parent-gate-verdict-v1.md)** (SHA256 `bd5d993008eb07cd634c57712893b1e9c07334928c9fd4ae13d6bc290c2ee813`, recorded 2026-10-18T13:00:17-07:00, retained unchanged). v1 lost many inter-word spaces. v2 restores them and rewords one chronological phrase so it cannot be read as a priority claim. No decision, hash, count, scope, caveat or disposition differs from v1.

## Decision and exact scope

**GATE MET for the frozen phys-2 M(7) target. CORRECTNESS-ACCEPTED, computer-assisted: M(7) = 2.** Every set of three mutually orthogonal quantum Latin squares of order 7 is classical, and a non-classical orthogonal pair exists. The statement allows **arbitrary complex unit vectors**, with product-vector orthogonality and the source's set-isotopy convention: independent unitaries per square and simultaneous row/column permutations.

This is not nonexistence of classical triples (they exist), not a bound on the ray count of one QLS, not a result about entangled Latin arrangements, and not M(n) for all n. No Lean proof, human peer review or novelty claim.

This is the final **decision 8** composition disposition under the [AMENDMENT-4 parent decisions](moqls7-amendment4-parent-disposition-v1.md). The formerly pending Links 3, 7, 10, 11 and 14 are accepted at the reconciled scopes below. The A+B standard is fully retained.

## Text and final reviews

- [K3-COMPOSITION r5](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/composition/K3-COMPOSITION.r5.md), SHA256 `7ed11c72a563cfea617e8d2ee3578e1db26ec02d5094fdd610398fbb80b5eecf`, read with this verdict's overlay. Its frozen pending/conditional statuses are superseded only by this final decision.
- [Exact r4→r5 diff](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k3-B-cube-parent-replay-v1/composition/K3-COMPOSITION.r4-to-r5.diff), SHA256 `61b7c88cf235ca4403ddf6aedf0c585a85118088b06866bf7e00bfa425dd06d8`.
- [Codex final review](moqls7-k3-composition-r5-final-codex-v1.note.md), SHA256 `f65cbd2f9eca8fef815f30b47d2e8449f86ebe630b979eb640ba9c1984db5fd6`: **COMPLETE-COMPOSITION ACCEPT**, 0 FATAL/MAJOR/new MINOR.
- [Claude final review](moqls7-k3-composition-r5-final-claude-v1.note.md), SHA256 `cdf97163ebe4fdd46e3c7d02928b3294e054e1447906cdd53330ac7c5a732291`: **COMPLETE-COMPOSITION ACCEPT-WITH-FIXES**, 0 FATAL/MAJOR, 7 documentation/import MINORs, all disposed below.

Both final reviews explicitly conclude that the accepted components plus the reviewed bridge establish K3 and M(7) = 2. Their reads were static; they did not run solvers. The finite outcomes are the parent's recorded replays.

## Six exact K3 formula facts

All are parent-accepted UNSAT, with solver self-exit 20, checker self-exit 0, and exact singleton status lines after CR removal only.

| Formula | SHA256 | Variables / clauses | Authority |
|---|---|---:|---|
| A_C321 | `d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388` | 96,978 / 627,486 | [G1](moqls7-k3-G1-parent-verdict-v1.md), [A-side replay](moqls7-k3-A-cubes-parent-verdict-v1.md) |
| B_C321 | `8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6` | 461,370 / 1,629,732 | [G1](moqls7-k3-G1-parent-verdict-v1.md), B_C321-a3 |
| A_C411 | `2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2` | 96,978 / 627,556 | [G2](moqls7-k3-G2-parent-verdict-v1.md), [A-side replay](moqls7-k3-A-cubes-parent-verdict-v1.md) |
| B_C411 | `01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8` | 461,370 / 1,629,802 | [G2](moqls7-k3-G2-parent-verdict-v1.md), B_C411-p3 |
| A lex C311+cuts | `18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e` | 107,513 / 897,308 | [A-cut verdict](moqls7-k3-A-C311cuts-parent-verdict-v1.md) |
| B C311+cuts | `ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a` | 461,370 / 1,867,942 | [B-cut verdict](moqls7-k3-B-C311cuts-parent-verdict-v1.md), [raw audit](moqls7-B-C311cuts-parent-audit-v1.json) |

The C321/C411 gates contain neither cuts nor lex blocks. The C311 facts use the exact 238,140-clause derived cut block `05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd`. A additionally uses the **seven C311-specific generators**, not another cube's group or all 22 generators.

The final B-cut pipeline ended 12:05:22 PDT. Its raw audit verifies all 43 assembled conditions and 39 grouped parent predicates, including complete measured 38,353,647-byte feeds, input/source/native pins and clean owned-process settlement. Its checker consumed 842,063,946 proof bytes; the A-cut checker consumed 705,539,296 bytes. No interrupted or disarmed attempt contributes.

## Parent derivation of the complete bridge

The parent read the full definitions and basis-free replacement argument, r5's cover/cut/lex/composition interfaces, the accepted H3/G1/G2/A-cut/B-cut verdicts, and both final audits. The key implications were independently re-derived:

1. **C0 and minimality.** Separate per-square unitaries straighten each individually classical member in its existing cells, preserving tensor-product orthogonality, so a set is classical iff every member is classical. If a K3 square were light in some orthonormal basis, selectively rotating all weight-2 entries on a chosen 2-coordinate support preserves every pre-existing zero inner product: an orthogonal entry outside the support must have disjoint support, because a single-coordinate overlap cannot cancel. At least one weight-2 entry disappears and none is created. Iterating classicalizes that square and preserves both partners simultaneously. The new square is distinct from both partners; otherwise a QLS would be orthogonal to itself, which needs 49 orthogonal vectors in C^7. This produces a forbidden K2 triple. Therefore every K3 member is heavy in every orthonormal basis, giving G4 on all 14 own lines, not only in one chosen frame.
2. **Normalization and three cubes.** Choose a heavy own line and an off-line point, then apply `--sym` and the separate residual column/square normalization. All 3 support sets are then nonempty and pairwise disjoint in the 6 coordinates outside the meet point, and the first contains 3 fixed coordinates. The only types are (3,1,1), (3,2,1) and (4,1,1), giving the 18 assignments covered by the 3 signed cubes. No new forced-weight-3 lemma from the older four-square problem is substituted.
3. **Encoder instantiation.** Both bases express the stated necessary Gram conditions, with collinear predicates false. A's product auxiliaries and B's product/threshold auxiliaries receive their actual conjunction/prefix-threshold values. The G2/G3/G4 lists have 5 or 6 candidates, so malformed empty/None branches are unreachable. Own-line heaviness gives the guards; singleton supports give G6. The runtime B-map oracle and the reviewed allocation order bind the same 2,646 g variables. The [H3 verdict](moqls7-k3-h3-parent-verdict-v1.md) is now applied with its hypotheses supplied by the normalized K3 configuration.
4. **The uncut gates imply the cuts, without circularity.** In any own frame, each square's neighbour count is positive and the 3 sets are disjoint in 6 coordinates. A count ≥ 4 forces (4,1,1); counts ≥ 3 and ≥ 2 force (3,2,1). Transposition and row/column/square permutations carry those local types to the exact uncut gate inputs, preserving individual ray sets and heaviness on the image, so G1/G2 exclude them. The uniform family has 14·42·3·C(6,4) = 26,460 at-most-3 clauses and 14·42·6·C(6,3)·C(3,2) = 211,680 mixed clauses; their sum is 238,140. These are derived K3 consequences under K1/K2/G1/G2, not unconditional QLS axioms.
5. **Existential lex representative.** The C311-specific group preserves the base, cube and cut conditions, so every orbit member is again a K3 configuration. A finite orbit has a lex minimum satisfying all 7 generator comparisons. For arbitrary comparator length, prefix variables set to "all prior positions agree" satisfy the emitted clauses when the lex order holds; conversely, the first 1→0 difference contradicts its forced-true prefix. No involution assumption or bounded-length truth-table premise is used; auxiliaries may be reconstructed. Thus **some** C311 representative satisfies A's strengthened input, and the original normalized configuration satisfies B's input.
6. **Closure.** C321 contradicts G1, C411 contradicts G2, and C311 contradicts the two accepted strengthened UNSAT facts. This proves K3. With the accepted K1/K2, every triple is classical. Any non-classical t-set with t ≥ 3 contains a non-classical member by C0; that member and 2 distinct partners form a non-classical triple, which is impossible. Hence M(7) ≤ 2.

## Lower bound: exact check

The prior Fourier construction uses f = (0,6,5,1,3,4,2), Psi_ij(x) = ω^(i·f(x)+j·x)/√7 and Phi_ij = |4i+j⟩. The parent wrote [an independent exact checker](check_m7_published_pair_parent_v1.py), SHA256 `3737822396d07fa7297d597ff1fa230f533cf2929ee7467d07844dbb03d0e7b2`, using the minimal polynomial 1+X+…+X^6 of ω_7, with no floating-point zero tests. [Result](moqls7-published-pair-parent-check-v1.json), SHA256 `1980a137dac1f9076b9ff4d50f2f70e0a0a7ccf5a77081c530dcf2c062deb849`: all 1,176 distinct cell pairs checked; both QLS valid and mutually orthogonal; 49 distinct Psi rays, hence non-classical. Replacing Phi's multiplier 4 by 2 fails orthogonality, and an affine f gives only 7 rays and is correctly classical. Thus M(7) ≥ 2 is independently corroborated. This construction is prior work, not a contribution of this run.

## Final MINOR finding dispositions

1. **Anticipatory statuses** (Claude m1): Links 3, 7, 10, 11 and 14 are accepted by this verdict. G1's earlier "accepted" wording is read through this final reconciliation, not as earlier authority.
2. **Implementation premises** (m2): the [hash-bound implementation index](moqls7-final-implementation-premises-v1.json) lists the original cut-family source, the regeneration/appender drivers, cut controls, encoders and lex metadata. Fidelity of the block to its mathematically derived family, and its serialization/appending, are reviewed trusted implementation premises. The parent-source lineage includes the [v11 static GO](m7-launch-v11-codex-v1.note.md), SHA256 `d7ed4c3a078ba765e735b262a29488bcc60ec1256e82243b926454c8abe8c61a`, which checks B's exact composition; the [v12 static GO](m7-launch-v12-codex-v1.note.md), SHA256 `e1e6f94c35019c5e7715e9c8aa7c5f3802b0663003aff265dd1fefcc0e4e6be7`, which checks A's exact composition; and the [v14 parent source GO](m7-v14-known-zombie-parent-source-go-v1.json), SHA256 `4e675c166726bc9ffd92d22108ed912352c70f07df333cfae3bea46fa29e623d`. These are scoped source/changeset reviews. They do not claim that every historical producer activation event is independently authenticated in this final snapshot.
3. **Generator identity** (m3): the header alone cannot identify H311. It is bound by the actual C311 generator source, lex metadata `7bef0b78…190d` and the signed-unit preservation evidence, not merely by the counts 10,535 auxiliaries / 31,612 clauses.
4. **Identical quiet logs** (m4): a 16-byte solver log whose exact bytes are `s UNSATISFIABLE` plus a newline hashes identically across many runs. Run identity comes from bound receipts and driver inputs, not from the common log hash or equal proof byte counts.
5. **PRODUCER label** (m5): r5 Link 13's older paragraph means "producer result, evidence only"; the parent B-cut verdict and this final composition status govern acceptance.
6. **Old A attempts** (m6): r8/r9 producer attempts remain non-contributing. Link 12 rests on A_C311cuts-p2; no missing old producer PASS is silently inferred.
7. **C0/control limits** (m7): subset closure uses the source's per-square-unitary convention and distinct partners. Classical AG(2,7) cut checks are near-vacuous because the local weights are 1. The semantic evidence is the structural cut proof, the C1 local coverage and the AMENDMENT reviews, not a nonexistent genuine K3 positive.

All 12 prior composition MINORs (Codex 3, Claude 9) remain closed by r5's fix maps. The empty-log templates are false and remain frozen; the actual B-cut raw logs are 16/478 bytes and the A-cut raw logs 16/475 bytes. A's 466-byte field is CR-normalized, not raw. The first B-cut parent audit's object/scalar schema failure is retained; correcting gate.rss_cap.value did not rerun science.

## Inherited evidence limits, not upgraded

**K2 provenance caveat, verbatim:** "35 classes (0-33, 35) have no script-hash-observed parent replay for either encoder; their acceptance rests on receipt content, hash-bound native logs (exact status, matching parse dims), regenerated CNF = producer r4 CNF, and A+B producer+parent verification; same-dims different-formula substitution excluded only by the edit-log account." No backfilled hash or concealment rerun is claimed.

The 26 matched controls followed K2 production; other hash-bound controls were reused. No genuine K3 positive control is possible without refuting the theorem, so the explicit component-level ruling remains. No parent-authored third encoder exists. Classification inputs enter through the accepted K1/K2 and Egan–Wanless; those literature premises remain imports.

**M7 proof streams are not retained or digested.** Parent replay means freshly re-solving the exact CNF and checking that stream, not identical producer proof bytes; re-checking the old stream is unavailable. The existing M7 exact-CNF protocol permits this; n8's stricter proof-digest protocol is not applied retroactively. CaDiCaL and kissat are untrusted producers; drat-trim, CPython, the compiler, OS, hardware and the reviewed serialization are trusted. No Lean, Comparator, independent formal kernel or human review.

## Priority and significance

The [fresh exact-M7 primary comparison](../screening/phys-2-moqls7-M7-post-candidate-priority-v2.md), SHA256 `6138411f55adbe79ddc02aa0bdf4fbbb5f270f68e8562835013812c6d5b673a6`, found no earlier M(7) = 2 and no order-7 triple construction or exclusion within its bounded scope. It covers current primary papers, all 36 DataCite quantum Latin records, arXiv, citers and authors, with explicit access holes. This is not a novelty or priority proof. A same-day final announcement refresh remains scheduled.

Scientific delta: the inspected Ball–Simoens preprint states 2 ≤ M(7) ≤ 4. Earlier in this run the upper bound was lowered to 3 (every four MOQLS(7) are classical); this verdict lowers it to 2, which determines M(7) exactly. This is a substantive specialist result in quantum combinatorics within the same order-7 programme, not a physical capacity claim or a claim about all orders. Publication and contact remain unauthorized.
