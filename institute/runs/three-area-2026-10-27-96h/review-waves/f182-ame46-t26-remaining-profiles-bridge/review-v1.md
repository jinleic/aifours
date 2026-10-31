# Independent same-harness review v1: f182-ame46-t26-remaining-profiles-bridge

Reviewer **ReviewF182AME46T26** (same-harness subagent). Native clock observed immediately before composing this file: `Thu Oct 29 09:02:47 PDT 2026`. This is not an exact completion time.

This is a same-harness review. It is not human review, independent-model-family review, formal or kernel verification, or novelty clearance. No author program was imported or executed. No held, f161, f162 or quarantined material, sibling review, Git, deletion, publication, external model or author contact was used.

## 0. Verdict

**Counts: 0 FATAL / 0 MAJOR / 2 MINOR. No in-scope claim is INCONCLUSIVE.**

| claim | verdict | dependency |
|---|---|---|
| (3,4,4,4) is impossible under H (§4) | Sound, no findings | H only: unitarity of the three flattenings and t=26. No import. |
| (2,5,5,5) impossible | Sound, no findings | (I1), via §5 → (M)/(O) → (G5) → (S2) |
| (3,5,5,5) impossible | Sound, no findings | (I1), via §5 → (M)/(O) → (G5) → (S2) |
| (4,5,5,5) impossible | Sound, no findings | (I1), via §5 → (M)/(O) → (G5) → (S2) |
| (5,5,5,5) impossible | Sound, no findings | (I1), via §5 → (M)/(O) → (G5) → (S2) |
| (4,4,4,5) impossible | Sound, no findings | (I1), via (M)/(O) → (G4) → (S3)/(S4) |
| (3,4,4,5) impossible | Sound, no findings | (I1), via (M)/(O) → cap (D3) → (S4) |
| (4,4,5,5) impossible | Sound, no findings | (I1), via (M)/(O) → (G4)/(G5) → (S1)/(S3)/(S4) |
| (3,4,5,5) impossible | Sound, no findings | (I1), via (M)/(O) → (G5) → (S5) + cap (D3) |
| §3 derivation of degree multisets | MINOR m1, presentation only | none |
| §8 exact controls (1/210/2580/2040 families; ranks; pair counts; zero triples) | Independently reproduced; MINOR m2, presentation only | Same normal form as §§5–6, hence (I1) |
| §1 "Combined consequence" (no AME(4,6) with support 46) | **NOT REVIEWED** (outside the manifest scope). Not composed or supported here. | (I2), f141, f113 |

Claim C therefore holds as stated, conditional on (I1). It inherits the boundaries of the adopted disposition: same-harness written support, and the unreplayed classical no-OLS(6) (Tarry) import. For the eight size-5 profiles the import is load-bearing. Without it the fibres can be cylinders, (M) fails (§4.4 control N2), and the stated reduction does not apply.

## 1. Manifest, inputs and actual source order

The manifest SHA-256 `c7168cafea342576daf582d48d907cdf127591e8f6ae24f4aef55758259bb0aa` (4,817 B) matched the assigned value. I checked it before reading the manifest, then read the manifest in full.

All six inputs matched their pins on full SHA-256, bytes, LF count and final LF. The verification command printed the clock `Thu Oct 29 08:32:46 PDT 2026`. Every recorded control run re-verified the same seven pins (`pins.*` checks, all pass).

| # | input (role) | SHA-256 | bytes | LF |
|---|---|---|---:|---:|
| 1 | `dispositions/physics-6-n46-no-hamming-one-parent-v1.md` (adopted no-H1; scope-only import) | `262a5a09…8baac0` | 5552 | 25 |
| 2 | `…/frontier-20261029-n46-t26-remaining-profiles-bridge-v1.md` (TARGET) | `b5b592d1…8913bb` | 14477 | 180 |
| 3 | `…-check-v2.py` (author checker; read/hash only) | `83afb6b2…a83911` | 6755 | 184 |
| 4 | `…-check-v2.json` (author receipt) | `856b1a87…093a23` | 3207 | 197 |
| 5 | `…-check-v1.py` (author checker; read/hash only) | `69838b8d…736440` | 11937 | 284 |
| 6 | `…-check-v1.json` (author receipt) | `03604b9f…2275db` | 9559 | 688 |

The full digests are in the pins of `reviewer-f182-independent-control-v1.py` and in every `reviewer-f182-control-out-*-v1.json`.

**Actual order.**

1. Manifest hash, then the full manifest.
2. Hash, byte and LF verification of all six inputs.
3. Complete reads in declared order:
   - disposition: 25/25 LF;
   - candidate: 180/180 LF;
   - v2.py: 184/184 LF;
   - v2.json: 197/197 LF;
   - v1.py: 284/284 LF;
   - v1.json: 688/688 LF, in two consecutive ranges, 1–300 then 301–688.

No mandatory errata or overlays exist in this manifest.

All reads finished before any mathematical reconstruction. The next clock, from an environment check, was 08:40:56. The control was then built in this order:

- in-memory prototyping in a Python kernel;
- control authoring after the 08:54:14 clock;
- five no-write debug runs, 08:55:53–08:57:44;
- the recorded runner, 08:57:58–08:58:49.

**Not opened.** The f141 and f113 dispositions, the §9 earlier packets, the f127 review and receipts linked from the disposition, and any other file outside the manifest.

## 2. Scope

**Reviewed:**

- Claim C: under H, every profile other than (4,4,4,4) is impossible.
- The written proof in §§2–7 and the load-bearing list in §10.
- The computational claims of §8.

**Import (I1)** is used scope-only. I checked that its hypotheses and conclusion match the candidate's usage; I did not re-review the lemma.

- **Disposition statement.** For a normalized complex AME(4,6) state in a product basis with support N=46 and exactly t=26 coefficients of modulus 1/6, no two of the remaining 20 positions E differ in exactly one coordinate. This holds "independently of the four-alphabet condition", conditional on no-OLS(6).
- **Candidate's H.** The candidate's hypothesis H is the same hypothesis, so the import applies to every profile.

**Not reviewed:**

- **§1 combined consequence.** The manifest forbids composing an N=46 exclusion with f127/f141/f113. Nothing here supports that composition.
- **Author-run metadata.** The v2 run time (29.3 s) and v1's "3000 directly built supports" cannot be checked without running author code. I do not rely on them.

## 3. Independent reconstruction of the load-bearing steps

### 3.1 (R1) and residual structure (§2)

For every 2|2 cut, `6ψ` reshaped as a 36×36 matrix is unitary, because the two-party marginals are I/36. An entry of modulus 1/6 becomes modulus 1, so it is the only nonzero entry in its row and its column. The 26 P entries therefore occupy 26 distinct rows and 26 distinct columns, and those rows and columns contain nothing else.

The 10 non-P rows have all their mass on the 10 non-P columns. Hence the 10×10 restriction V has orthonormal rows, so it is unitary. A row of V with a single nonzero would carry a modulus-1 entry, which would be a P entry. So every row and column of V has at least 2 nonzeros. With 20 entries, each has exactly 2.

Each pair {i,j} indexes the rows or the columns of exactly one cut. Hence (R1): 26 cells carry exactly one P word and no E word, and 10 cells carry exactly two E words and no P word. ✔

### 3.2 Local degrees and profiles (§3)

All extensions of an E-carried cell `(a,y)` lie in `E_a`, so `|E_a| = 2|π_j(E_a)|` for every j≠i. Hence d(a) does not depend on j. ✔

- **(D1).** If d=1, the two words of `E_a` agree everywhere. ✔
- **(D2).** Σd = 10. ✔
- **(D3).** `d(a) = |π_j(E_a)| ≤ r_j`. ✔
- **(D4).** `r_i r_j ≥ |π_ij(E)| = 10`, and `r_i ≤ 5` follows from (D1) and (D2). ✔

Ten sorted profiles remain. The control checks this two ways:

- pairwise products ≥ 10 over sizes 2..5;
- independently, over sizes 1..6, requiring per-party feasibility of a degree multiset under (D1)–(D3).

Both give exactly the candidate's ten profiles.

The degree multisets are:

- size 5: all 2;
- size 4: X=(2,2,2,4) or Y=(2,2,3,3);
- size 3 under the global cap 5: (2,3,5), (2,4,4), (3,3,4);
- size 2: (5,5).

See MINOR m1 on the attribution of these lists.

### 3.3 (3,4,4,4) — no import (§4)

By (R1) on (i,j), the P words active at i biject with the P-carried cells `(a,y)` with `a∈R_i`. There are `6r_i − 10` of them. Similarly, `r_i r_j − 10` P words are active at both i and j.

For (3,4,4,4) the two sums are:

- `Σk = 8 + 3·14 = 50`;
- `ΣC(k,2) = 3·2 + 3·6 = 24`.

Hence `Σ(k − C(k,2)) = 26 = |P|`. The summand values are `(0,1,1,0,−2)` for k = 0..4, so every P word has k∈{1,2}.

At a size-4 party i, 14 P words are active at i, and `(12−10)+(16−10)+(16−10) = 14` are active at i and at exactly one other party. So no P word is active at i alone.

For `a∈R_i`, exactly `6−d(a)` P words have `x_i=a`, and `r_j−d(a)` of them are also active at j. The number active at i alone is therefore `(6−d) − (11−3d) = 2d−5`. This would have to equal 0, which is impossible for an integer d. At d=2 the count is −1, already a contradiction.

The argument is complete and uses only (R1). ✔

The recorded control re-derives:

- the unique activity vector (0,2,24,0,0), over all 27,405 compositions of 26 into 5 parts;
- the counts 14/14/0;
- `2d−5 ∉ {0}` for d = 0..10;
- that the (D3) cap forces Y at the size-4 parties, giving d∈{2,3} and values −1, +1.

### 3.4 Parity fibres — the only use of (I1) (§5)

If d(a)=2, then `E_a` is four distinct words. In each other coordinate it takes two values, each exactly twice, so after relabeling it is a balanced 4-subset of `{0,1}^3`.

The control enumerates all 70 four-subsets of the cube:

- exactly 8 are balanced;
- exactly 2 of those are distance-one-free, and these are exactly the two parity classes;
- the other 6 are exactly the cylinders `{x_j=x_k}` and `{x_j≠x_k}`.

Each cylinder contains a pair differing only in the free coordinate. Such a pair consists of two E words with equal `x_i=a` that differ in exactly one coordinate, which (I1) forbids. Each parity class projects bijectively onto every coordinate pair. Each cylinder fails bijectivity exactly on its own pair. ✔

**Precise use of (I1).** Only the instance "no two E words with the same value at a size-5 party A differ in exactly one other coordinate" is used.

### 3.5 Incidence algebra (§6)

**(M).** E is the disjoint union of the five parity fibres `E_g`. Each fibre contributes exactly one word to every cell of `π_j(E_g)×π_k(E_g)`, so the multiplicity of (b,c) is `Σ_g U_j[g,b]U_k[g,c] = (U_j^T U_k)_{bc}` as an integer. ✔

This needs every A-fibre to have d=2, which holds exactly because `r_A=5`. The column weight of `U_j` at b equals `|π_A(E_b)| = d(b)`. ✔

**(O).** By (R1), every cell carries 0 or 2 E words, so all entries lie in {0,2}, and `U_j^T U_k=0` over F₂. As a consistency check, the entries sum to `Σ_g 2·2 = 20`, so exactly ten entries equal 2. ✔

**Multigraph facts.** Over F₂, the edge-vertex incidence matrix has rank `r − c`, and `ker U^T` is the cycle space. ✔

- **(G5).** A loopless 2-regular graph on 5 vertices is C5 (rank 4, `ker = {0,1}`) or C2 + C3 (rank 3, `ker = {0,p,q,1}`, with `p+q=1`). ✔
- **(G4), X.** A component avoiding the degree-4 vertex is a C2 or a triangle on degree-2 vertices. That leaves v at most one neighbor, of degree 2, so X is connected and has rank 3. ✔
- **(G4), Y.** Components need even degree sum and at least 2 vertices. So Y is connected (rank 3) or splits {3,3}+{2,2}, a triple edge plus a double edge, of rank 2 with columns `q′,q′,p′,p′` and `p′+q′=1`. ✔

Every one of these facts was also checked exhaustively over the families (`lemmaG.exhaustive_structure_facts`, 0 violations). That covers:

- rank = r − c, cross-checked by row rank and kernel size;
- 1440 C5 and 600 C2+C3 with the stated kernels;
- X always connected and of rank 3;
- rank-2 Y exactly of the stated shape, with 1 in the span;
- all size-3 families connected, of rank 2.

**Lemma S.**

- **(S1).** `col(U_k) ⊆ ker(U_j^T)`, which is the Sylvester inequality with product 0. ✔
- **(S2)** and **(S3).** Each is a rank-sum violation. ✔
- **(S4).** A rank-2 Y puts 1 in the span. Every column of the partner is then orthogonal to 1, so it has even weight, but Y has two weight-3 columns. ✔
- **(S5).** The rank sum 5 forces C2+C3 with a rank-2 Y. Every partner column then lies in `{p,q,1}`, of weights 2, 3 and 5. ✔

The control checked these exhaustively over all F₂-orthogonal pairs of the families:

- 0 rank-sum violations;
- 0 pairs of two size-5 matrices;
- 0 pairs of X with X or Y with Y;
- every (4,5) pair is a rank-2 Y with columns {q,q,p,p} against a C2+C3;
- every (3,5) pair has size-3 columns {p,q,1}.

### 3.6 The eight profiles (§7)

Each case follows by hand:

- **At least three 5's.** Two size-5 partners, so (S2).
- **(4,4,4,5).** Two of the three size-4 partners share a type, so (S3) or (S4).
- **(3,4,4,5).** The cap is 3, so both size-4 partners are Y, and (S4) applies.
- **(4,4,5,5).** The two size-4 partners have different types, so one is X of rank 3, and `3+3>5`.
- **(3,4,5,5).** (S5) on (B,C) puts D's columns in {p,q,1}. The cap `r_C=4` excludes weight 5, so D's multiset is (2,4,4) or (3,3,4), which needs a weight-4 column.

All are correct. ✔

### 3.7 Exact dependency on the no-H1 import

| profile | uses (I1)? | where | other inputs |
|---|---|---|---|
| (3,4,4,4) | **no** | — | H → (R1) only |
| (2,5,5,5), (3,5,5,5), (4,5,5,5), (5,5,5,5) | yes | §5 parity of all five A-fibres → (M)/(O) | (G5), (S2) |
| (4,4,4,5) | yes | same | (G4), (S3), (S4) |
| (3,4,4,5) | yes | same | (D3) cap, (S4) |
| (4,4,5,5) | yes | same | (G4), (G5), (S1), (S3), (S4) |
| (3,4,5,5) | yes | same | (G5), (S5), (D3) cap |

(I1) is itself conditional on the classical no-OLS(6) theorem, recorded in the disposition as an unreplayed import, and carries that disposition's same-harness status. Composing it with other records is the parent's job.

## 4. Reviewer-authored exact control

### 4.1 Design

`reviewer-f182-independent-control-v1.py` was written from the candidate's normal form. I had read the author checkers beforehand, as the manifest requires, so the control is an independent implementation, not clean-room. Method 1 shares the author's column-set reduction idea. Method 2 and the BLAS triple count are different algorithms.

It runs the following components:

- **Labeled families.** All 5-tuples of 2-subsets of `{0..r−1}`, keeping column weight ≥2, for r=2..5.
- **F₂ structure.** Rank by my own elimination, components by union-find, kernel by brute force over F₂^5.
- **Pair compatibility, Method 1.** Pure Python over distinct column sets, with a 32×32 overlap table.
- **Pair compatibility, Method 2.** numpy, labeled: (M) applied literally, accumulating each fibre's four cells and testing multiplicities. The two methods must agree on all labeled pairs.
- **Triple counts.**
  - Method 1: pure Python, group level.
  - Method 2: float64 BLAS, `Σ A12 ∘ (A13 A23^T)`, exact because all integers are below 2^53.
- **Relaxations, F₂ lemma checks, cap analysis.**
- **(M) on built supports.** 3000 seeded supports with parity fibres, plus a cylinder negative.
- **§4 activity arithmetic** for all 10 profiles.
- **Author receipts.** Both JSON receipts parsed in full by my own code and compared leaf by leaf.

`reviewer-f182-control-runner-v1.py` runs one unmutated case and four mutation cases as separate one-shot processes. Each has a 120 s subprocess timeout, alongside an in-script SIGALRM cap at 120 s. It writes exclusive-create outputs and checks each case against the expectations written into the runner before any recorded run. Those expectations were informed by in-memory prototyping, so they were declared ahead of the recorded runs but are not blind predictions.

### 4.2 Recorded runs

Python 3.14.3, numpy 2.4.3. Control SHA-256 `69f6c2db016076f265a9f0a8d3f97eee23cf8422ed0a21dcd429c807adc54d83`. The runner exited 0 with `all_as_predeclared: true`.

| case | clock before → after (PDT) | exit | elapsed s | checks failed | output SHA-256 |
|---|---|---:|---:|---|---|
| none | 08:57:58 → 08:58:07 | 0 | 8.719 | none (80/80 pass) | `b02383b2…341597533` |
| rule-le2 | 08:58:07 → 08:58:21 | 3 | 14.745 | the 8 `triples.zero.*`, `pairs-hand.{3_5,4_5,5_5}`, and both author-receipt comparisons | `8cba8b8e…dfb2f691` |
| drop-pair-23 | 08:58:21 → 08:58:30 | 3 | 8.578 | `triples.zero.*` for the 6 profiles with nonzero relaxed counts, and both author-receipt comparisons. (3,4,5,5) and (5,5,5,5) stay 0. | `63b9621f…dfb8802` |
| wrong-expected-family | 08:58:30 → 08:58:39 | 3 | 9.035 | exactly `families.size.r4` | `5a576883…a199ed19b` |
| cylinder-fibre | 08:58:39 → 08:58:49 | 3 | 10.256 | exactly the (M) positive check. All 3000 supports fail for the reason {intra-fibre Hamming-1, (M) mismatch on the cylinder's own pair}. | `e3433792…abad07213` |

No cap was hit, so no result is UNKNOWN.

### 4.3 Results of the unmutated run

| r | families | degree types | F₂ ranks |
|---|---:|---|---|
| 2 | 1 | (5,5): 1 | rank 1: 1 |
| 3 | 210 | (2,3,5): 60, (2,4,4): 60, (3,3,4): 90 | rank 2: 210 |
| 4 | 2580 | X: 720, Y: 1860 | rank 2: 60, rank 3: 2520 |
| 5 | 2040 | all 2: 2040 | rank 3: 600, rank 4: 1440 |

**{0,2}-compatible labeled pairs.** Methods 1 and 2 agree on every labeled pair:

| pair | count |
|---|---:|
| (2,5) | 2040 |
| (3,4) | 9720 |
| (3,5) | 3600 |
| (4,4) | 8640 |
| (4,5) | 3600 |
| (5,5) | 0 |

Three of these were also derived by hand and checked:

- (3,5) = (4,5) = 600·6;
- (2,5) = 2040;
- (5,5) = 0.

**Type breakdown of the compatible pairs.**

- (4,4): only X (rank 3) with rank-2 Y, 4320 in each order.
- (4,5): only rank-2 Y with C2+C3.
- (3,5): only size-3 type (2,3,5) with C2+C3.
- (3,4): only Y, never X, with size-3 types (2,4,4) or (3,3,4).

**Triples satisfying all three conditions: 0 for all eight profiles, by both methods.**

| profile | pairs 12 / 13 / 23 | triples |
|---|---|---:|
| 2,5,5,5 | 2040 / 2040 / 0 | 0 |
| 3,4,4,5 | 9720 / 9720 / 8640 | 0 |
| 3,4,5,5 | 9720 / 3600 / 3600 | 0 |
| 3,5,5,5 | 3600 / 3600 / 0 | 0 |
| 4,4,4,5 | 8640 / 8640 / 8640 | 0 |
| 4,4,5,5 | 8640 / 3600 / 3600 | 0 |
| 4,5,5,5 | 3600 / 3600 / 0 | 0 |
| 5,5,5,5 | 0 / 0 / 0 | 0 |

**Relaxed triple counts** (partners sorted ascending; one pair condition dropped):

| profile | drop (2,3) | drop (1,3) | drop (1,2) | rule ≤2 |
|---|---:|---:|---:|---:|
| 2,5,5,5 | 4161600 | 0 | 0 | 4161600 |
| 3,4,4,5 | 693360 | 77760 | 77760 | 1762560 |
| 3,4,5,5 | 0 | 64800 | 21600 | 59486400 |
| 3,5,5,5 | 216000 | 0 | 0 | 873936000 |
| 4,4,4,5 | 336960 | 336960 | 336960 | 1770543360 |
| 4,4,5,5 | 259200 | 259200 | 21600 | 6105067200 |
| 4,5,5,5 | 216000 | 0 | 0 | 10736928000 |
| 5,5,5,5 | 0 | 0 | 0 | 8489664000 |

- The drop-(2,3) column equals author v1's `control_without_CD_condition_triples` for every profile, and Methods 1 and 2 agree on it.
- The F₂-only relaxation, which keeps evenness but drops the integer {0,2} refinement and applies no caps, still gives **0 triples** for all eight profiles.

**(M) on built supports.** All 3000 seeded supports built from parity fibres satisfy (M) exactly, including zero cells, and have A-pair multiplicity 2. All 1000 supports with a cylinder fibre fail for exactly the intended reason.

**Activity moments.**

- (3,4,4,4): unique activity vector (0,2,24,0,0).
- (4,4,4,4): 3 solutions, so counting alone does not exclude it (positive control).
- (2,5,5,5): no solutions (see O1).

### 4.4 Positive and intended-reason negative cases

**Positive cases:**

- **P1.** The drop-(2,3) relaxation finds triples in six profiles, so the triple counters can see solutions.
- **P2.** 3000 parity-fibre supports satisfy (M).
- **P3.** (4,4,4,4) is not excluded by the §4 counting.
- **P4.** Every (3,5)-compatible pair has size-3 columns exactly {p,q,1}, as (S5) predicts.

**Negative cases, each failing for its intended reason:**

- **N1.** The six cube cylinders each contain a distance-one pair and are non-bijective on their own pair. This is where (I1) is needed.
- **N2.** A cylinder fibre breaks (M) on exactly its own pair, both in-run (1000/1000) and as the process-level case `cylinder-fibre`.
- **N3.** Replacing {0,2} by ≤2 admits triples in all eight profiles, both in-run and as the process case `rule-le2`. Evenness of the (R1) multiplicities is what excludes the profiles.
- **N4.** Dropping one pair condition (process case `drop-pair-23`) breaks the zero result exactly where predicted.
- **N5.** A planted wrong family expectation is caught alone.
- **N6.** The comparator self-test reports a planted one-leaf change in v2 as exactly one mismatch.

### 4.5 Author receipts parsed in full (data only, not evidence)

**v2: 117 leaves.**

- 115 match my values exactly, with matching value types.
- 2 are narrative strings (`methods`, `scope`).
- 0 mismatches, 0 author-only leaves, 0 reviewer-only leaves.

**v1: 372 leaves.**

- 357 match. Allowed degree lists were compared order-insensitively.
- 1 narrative string (`scope`).
- 1 author-run sample count (`direct_support_cross_checks`=3000), which cannot be verified.
- 13 leaves of order-dependent example histograms (`control_example_CD_multiplicities`). Each example sums to 20 words and is achievable among the drop-(2,3) relaxed triples of its profile.
- 0 mismatches.

## 5. Findings

**m1 (MINOR, §3 presentation).** §3 says "By (D1) and (D2), the degree multisets are: …". But (D1)+(D2) also admit size-3 (2,2,6) and size-2 (2,8), (3,7), (4,6). These are excluded only by (D3) together with `r_j≤5`. Similarly, (D4) attributes `2≤r_i≤5` to `|π_ij(E)|=10`, but the upper bound comes from (D1)+(D2).

No conclusion is affected. (3,4,5,5) re-derives the size-3 list with entries in [2,4], and no step uses the size-2 list. Suggested fix: cite (D1)–(D4) and name (2,2,6) as cap-excluded.

**m2 (MINOR, §8 presentation).** The §8 table's B/C/D are the partner sizes of the size-5 party in ascending order. §7 uses different letters for (3,4,5,5), and §8 does not state its convention. In (3,4,5,5), "the 3600 BD pairs include degree-5 size-3 columns equal to 1" understates the fact: **all** 3600 have size-3 type (2,3,5) with columns exactly {p,q,1}.

In the uncapped enumeration these pairs are removed by the size-3/size-4 condition, because the only (3,4)-compatible size-3 types are (2,4,4) and (3,3,4). That is the enumeration's analogue of (D3), not a use of (D3). Suggested fix: state the naming convention and the "all".

No FATAL or MAJOR issue was found in §§2–8.

## 6. Observations (reviewer-derived, outside the candidate, no verdict impact)

**O1. (2,5,5,5) has an import-free exclusion.** The §4 moment count applies directly: `Σk = 62` and `ΣC(k,2) = 45`. These give:

- `n1 + n2 − 2n4 = 17`;
- `n0 + n3 + 3n4 = 9`;
- `n2 = 45 − 3n3 − 6n4 ≥ 18 + 3n4`;

while `n1 ≥ 0` forces `n2 ≤ 17 + 2n4`. So `n4 ≤ −1`, a contradiction. The recorded run confirms the solution set is empty. If adopted after its own review, this would remove the (I1) dependency for that one profile. The candidate does not claim it.

**O2. F₂ plus degrees suffice.** The F₂-only relaxation already yields zero triples without caps. This matches the written proof, which uses only F₂ orthogonality and degrees, and it shows that the enumeration does not need the stronger integer {0,2} refinement.

## 7. Deviations and limits

- **Independence.** The control was authored after the mandated reading of the author checkers. Method 1's column-set reduction is conceptually close to the author's bitmask method. Method 2, the BLAS triple count, the compositions-based activity enumeration and the leaf-level receipt comparison are different algorithms.
- **Pre-run activity.**
  - In-memory prototypes ran in a Python kernel and wrote nothing.
  - Five `--no-write` debug runs of the finalized control (one unmutated, four mutations) gave the same outcomes as the recorded runs and wrote nothing.
  - I also imported my own control as a module in the kernel to inspect intermediate data; this wrote no files and no bytecode.
  - The runner's expectations were written after the in-memory prototypes and the first debug run, but before the mutation debug runs and the recorded runs.
- **File mode.** The write tool set the executable bit on my two `.py` files automatically.
- **(M) coverage.** The exhaustive part of (M) is the local cube statement plus disjoint additivity. The 3000/1000 built supports are a seeded sample.
- **§4 coverage.** The control checks only the arithmetic of §4. The unitarity reduction (R1) is verified by hand (§3.1).
- **Not rerun.** Author programs were not run, so author-run times and samples are unverified.
- **Same harness.** The model and harness may be the same as the author's.

## 8. Files created by this reviewer (this directory only)

| file | SHA-256 |
|---|---|
| `reviewer-f182-independent-control-v1.py` | `69f6c2db016076f265a9f0a8d3f97eee23cf8422ed0a21dcd429c807adc54d83` |
| `reviewer-f182-control-runner-v1.py` | `1c6dfe3e93ab739feb214d4cf4eac6c90830695eb1b4c8b7cce0759fcc2504f2` |
| `reviewer-f182-control-run-receipt-v1.json` | `a3292b8fc618d865c50d56e6df2e627f7d86970f252af57c0fea135cd93029d4` |
| `reviewer-f182-control-out-none-v1.json` | `b02383b246ac1d2a21328b5ef81c5922c9090b89d59b6d015a6f601341597533` |
| `reviewer-f182-control-out-rule-le2-v1.json` | `8cba8b8ee3c215b3054baf4c6aa3d1b2d4af253af5073d403dd77eeedfb2f691` |
| `reviewer-f182-control-out-drop-pair-23-v1.json` | `63b9621fd1515d7e8a9ec09d8ec9d9659d5988b97a21d6d9949e20579ece8802` |
| `reviewer-f182-control-out-wrong-expected-family-v1.json` | `5a576883a61e83f90508332ac67c315899f5ab1e303b03becc45bc5a199ed19b` |
| `reviewer-f182-control-out-cylinder-fibre-v1.json` | `e3433792eebf8c280988d369c35f6c79d4f7ffd5d75656901e179a0abad07213` |
| `review-v1.md` | this file; its SHA-256 is reported separately |
