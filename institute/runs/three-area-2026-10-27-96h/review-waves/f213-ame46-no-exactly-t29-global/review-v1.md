# Independent same-harness review: f213, no exactly-t=29 AME(4,6)

**Disposition: 0 FATAL / 0 MAJOR / 1 MINOR; 1 INCONCLUSIVE item (author-process provenance, not the mathematical proof).** The exact-t=29 exclusion and the asserted absence of the named mathematical imports are supported by the independent written reconstruction below. The minor finding concerns an overbroad description of what the proof bounds, not the validity of the contradiction. No t≤28, global support-bound, or novelty conclusion is reviewed or adopted here.

Native clock observed before writing this review: **2026-10-29T13:16:41-0700 PDT**. This is not a claim about file creation or completion time.

## Frozen inputs, integrity, and actual sequence

The required process-memory summary was consulted before the first research artifact; it supplied no scientific premises. The first research artifact opened was this wave's `manifest-v1.json`. Its measured SHA-256 was `bc6418f37d1e885bc40212cea4cc29d2750a24b5929673c777bfbb4c77c6a51f`, matching the assigned prefix `bc6418f37d1e`. Before opening either input body, I measured both complete files, and all SHA-256, byte, and LF values matched the manifest:

| Manifest order and role | File | SHA-256 | Bytes | LF |
|---|---|---|---:|---:|
| 1, adopted context for definitions only | `institute/runs/three-area-2026-10-27-96h/dispositions/physics-6-n46-no-hamming-one-parent-v1.md` | `262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0` | 5552 | 25 |
| 2, target candidate | `physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261029-no-t29-global-v1.md` | `eaa2c9f93b782720527eb0117434a2663954735038330c09b1943bc99831dbe5` | 4589 | 58 |

After integrity measurement I reread manifest line 29 raw, then displayed **all** input bodies in manifest order and in these exact raw windows: context `1–15`, `16–25`; target `1–15`, `16–30`, `31–45`, `46–58`. All final lines were displayed before mathematical reconstruction or controls. Subsequently I consulted the procedural `independent-snapshot-review` skill, not as scientific evidence, and made a supplemental non-raw target selector `30–34` to locate the wording finding; the tool also displayed nearby and structural anchor lines. No linked body was opened. I then wrote and ran the reviewer-owned control below and wrote this review. Only the adopted context's definitions, not its N=46/t=26 claims, no-Hamming-one conclusion, enumeration, no-OLS theorem, or linked evidence, are used as premises.

## Per-claim disposition

| Claim | Verdict | Reason |
|---|---|---|
| Each pair system has 29 distinct maximal singleton cells and 7 nonmaximal cells, each with at least two E extensions | 0F/0M/0m | Follows independently from the two-party maximally mixed reductions and row norms, as reconstructed below. |
| For every local E symbol, `d_i(a)=6−m_i(a)` is independent of partner, `d_i(a)≥2`, and the degree sum is 7 | 0F/0M/0m | The complete pair partition and pair injectivity give the identity; a degree-one fiber would be a forbidden singleton E cell. |
| All four E alphabets have exactly three symbols | 0F/0M/0m | Degree sums give size at most three; a pair with a size at most two has at most `2·3<7` E cells. |
| The activity counts are 11 per party, 2 per party pair, totaling 44 and 12; `32≤29` is impossible | 0F/0M/0m | The active 3×6 and 3×3 pair cells and pair injectivity give these counts; a pointwise inequality yields the contradiction. |
| No normalized complex AME(4,6), in any product basis and irrespective of total support, has exactly 29 coefficients of modulus 1/6 | 0F/0M/0m | The contradiction uses no prescribed support cardinality or residual multiplicity upper bound. |
| The exact-t=29 proof has no mathematical dependence on no-OLS(6), no-Hamming-one, small-excess classifications, SAT, f113, or any prior author outcome | 0F/0M/0m | The complete reconstruction uses only the AME definition, elementary linear algebra, and finite counting. A separate synthetic positive incidence control even contains a distance-one E pair. This verifies the proof's dependencies, not the author's historical research process. |
| Candidate line 31 says the conclusion “did not bound any E-pair multiplicity or \|E\|” | 0F/0M/1m | Literally overbroad: the proof uses E-pair multiplicity at least 2, and its three-symbol alphabets imply a multiplicity at most 9. Clarify that no **additional a priori upper bound** or fixed residual-support cardinality is assumed. This does not affect the proof. |
| Candidate's historical statement “No held material was used” | INCONCLUSIVE | The pinned text states this, but the permitted inputs do not establish author-process provenance; no prohibited material or author communication was consulted. This is not an imported premise in the reconstruction. |
| Optional t≤28 composition, support-bound comparisons, and attribution to earlier controls | OUT OF SCOPE | Not checked or imported; their linked bodies were not read. |

## Independent written reconstruction

Let `ψ` be a normalized pure state on four six-dimensional parties, and suppose, for contradiction, that it is AME and has exactly 29 coefficients of modulus `1/6` in a chosen product basis. The defining AME condition is that every two-party reduced density matrix is `I/36`. For a pair of parties `i,j` and its complementary pair `k,l`, arrange the amplitudes into the 36×36 matrix `C` with row `(i,j)` and column `(k,l)`. Then `C C†=I/36`, so `U=6C` satisfies `U U†=I`; being square, it is unitary. The same statement holds for every pair as a row system. This uses no classification of a unitary's residual block.

A coefficient has modulus at most `1/6` because each row of `U` has squared norm 1. Let `P` be the 29 words with modulus exactly `1/6`, and let `E` be all other nonzero coefficient positions. A P entry has modulus 1 in `U`, so every other entry in its row and column is zero. Consequently distinct P words cannot agree in any chosen coordinate pair, and an E word cannot share a pair with a P word. Every one of the 36 rows of each pair system has nonzero norm, hence is represented by support. Exactly 29 cells are P-carried, one P word per cell, and the other 7 are E-carried. An E-carried row has at least two nonzero entries: if it had exactly one, its entry would have unit modulus in `U`, and that word would be in P instead. This gives the full `29P+7E` partition in **all six** coordinate-pair systems, with no hypothesis on total support.

Fix party `i`, an E symbol `a`, and another party `j`. Define `m_i(a)` as the number of P words with coordinate `i` equal to `a`; pair injectivity makes their `j` coordinates distinct. Of the six cells `(a,b)`, exactly `m_i(a)` are P-carried, and the full partition puts all remaining `6−m_i(a)` in the E projection. Thus

`d_i(a):=|{x_j : x∈E, x_i=a}|=6−m_i(a)`, independently of `j`.

Because `a` occurs in E, this degree is positive. If it were 1, the same identity for each of the other three parties would force each of those coordinates to be constant across the fiber `E_i(a)`. Four-coordinate words in a support are distinct, so the fiber would contain exactly one word, making a pair cell involving `i` a singleton E cell, impossible. Hence `d_i(a)≥2`. Summing over the distinct E symbols at `i` counts the seven E-carried `(i,j)` cells exactly once, so `Σ_a d_i(a)=7`, for every `i` and every partner `j`. Therefore each E alphabet has at most `⌊7/2⌋=3` symbols. Since every one of the six E pair projections has seven cells and each partner alphabet has size at most 3, any alphabet of size at most 2 would give at most `2·3=6` cells for a pair containing it. Thus each alphabet has size exactly 3. In fact its three degrees must be a permutation of `(2,2,3)`; this refinement is not needed for the contradiction.

Call coordinate `i` of a P word *active* when its value lies in the E alphabet at `i`, and write `k(x)` for the number of active coordinates of P word `x`. In any pair `(i,j)`, exactly `3·6=18` cells have active `i` coordinate. All seven E cells have active `i` coordinate, leaving 11 P cells; by P pair injectivity, exactly 11 P words are active at `i`. Similarly, all seven E cells lie among the `3·3=9` active/active cells, so the other two are P cells: exactly two P words are active simultaneously at `i` and `j`. Double counting gives

`Σ_{x∈P} k(x)=4·11=44`, and `Σ_{x∈P} binom(k(x),2)=6·2=12`.

For `k=0,1,2,3,4`, the values of `k−binom(k,2)` are respectively `0,1,1,0,−2`, each at most 1. Thus

`32 = 44−12 = Σ_{x∈P}[k(x)−binom(k(x),2)] ≤ |P| = 29`,

an impossibility. The chosen product basis was arbitrary. The proof is conditional only on the definition of AME and the assumed exact count of 29; it therefore excludes that count for any total support.

For the minor wording issue, in the same hypothetical setting an E pair cell has at least two extensions by the row-norm argument and at most `3·3=9` possible extensions because both complementary E alphabets have size three. These are consequences within the contradiction, not an extra imposed upper-bound hypothesis. The candidate's unqualified “did not bound any E-pair multiplicity” can therefore mislead; replace it with the narrower statement identified in the table.

## Reviewer-owned exact controls and receipts

Control source: `reviewer-controls-v1.py` in this wave, written independently without opening, importing, compiling, or running author code. Native `/bin/date` before writing the control: `2026-10-29T13:15:28-0700 PDT`. Its measured SHA-256 before execution was `d4d8e39932fc451bbd69a1006cb33bd3e4656d1790e3355c8567945383b48227`. One bounded run was invoked as `/usr/bin/python3 reviewer-controls-v1.py`, with the tool deadline set to 120 seconds. Native clock before execution: `2026-10-29T13:15:55-0700 PDT`; native clock after execution: `2026-10-29T13:15:55-0700 PDT`; captured control exit code: `0`. Both timestamps are observations at one-second precision, not a precise duration. No cap or timeout occurred.

- Positive incidence-only control: `P={(0,0,0,0)}`, `E` all 4-tuples over `0,…,5` with at most one zero. It has `|E|=1125`, all 216 pair cells correctly partitioned, E-cell extension counts 25–35, and all 72 local-symbol/partner degree identities. `E` includes `(1,1,1,1)` and `(1,1,1,2)`, a distance-one pair. This is an abstract combinatorial support, **not** an AME state or a t=29 witness.
- Intended-reason negatives: removing all E extensions of pair cell `(parties 0,1; symbols 1,1)` produces exactly that missing cell and partner degrees 5 versus 6; adding `(0,0,1,1)` produces exactly the shared P/E cell `(0,1;0,0)` and partner degrees 6 versus 5; retaining only one extension of the first cell produces exactly the targeted singleton E cell, with no missing or shared cells. The checker detected each intended fault separately.
- Degree-profile enumeration: ordered local degree lists of lengths 1 through 6, entries 2 through 6, and sum 7 had respective counts `0,4,3,0,0,0`; imposing all pair-capacity requirements left only alphabet shape `(3,3,3,3)`. Intended negatives: four symbols have minimum degree sum 8, and a 2×3 pair has only six cells. In a 3×3 pair with both ordered degree lists `(2,2,3)`, exactly two seven-cell patterns exist; placing both missing cells in one row gives row degrees `(1,3,3)` and is rejected for that reason. These checks establish necessary incidence facts, not a construction of a quantum state.
- Exhaustive activity-multiplicity control: all `C(33,4)=40,920` nonnegative 5-tuples `(c_0,…,c_4)` summing to 29 were enumerated. Of these, 669 have total activity 44, none also have pair activity 12, and one has pair activity 15. The positive relaxed arithmetic control `(0,14,15,0,0)` has total 29, activity 44 and pair activity 15; it is rejected for the target specifically because `15≠12`. The script independently checked the five pointwise values `0,1,1,0,−2`. These finite checks supplement, rather than replace, the written proof.

## Imports, remaining gap, and deviations

Mathematical premises are the definition of a normalized complex AME(4,6) state and elementary linear algebra and combinatorics. There is **no mathematical import** of no-OLS(6), no-Hamming-one, a small-excess unitary classification, SAT, solver status, author outcomes, a residual-support size, or the cited optional composition. The author-process assertion about held material remains unverified; the exact-t=29 proof's validity does not depend on that historical assertion. Nothing here determines whether t≤28, proves a support-bound improvement, or adjudicates the optional compositions.

Contract deviations: none identified. The required process-memory and procedural skill reads were not scientific evidence; no input body was read before all integrity measurements or out of manifest order, and no prohibited source was used. This is a **same-harness** review, not human review, independent-model-family review, formal/kernel verification, or novelty verification.
