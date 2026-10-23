# K7-M-empty-status-v1: status of class K7 when no vertex is marked (M = ∅), and what remains uncovered when M ≠ ∅

- **Freeze record:** host-clock time and sha256 in `evidence/k7-m-empty-status-v1.sha256`.
- **Nature:** a status summary, as the parent requested. It adds no new lemma and involves no computation.
- **K7 stays OPEN.** Every exclusion listed is written, and none is a premise until the parent issues a verdict.
- **Family convention:** that of K7-structure-erratum-v1 X1.
  - Q5: every β = 5.
  - Q23: every β ∈ {2, 3}, **including** a single 2-class (all β = 2) and b = 1.
  - Q24: every β ∈ {2, 4} with at least one β = 4.

## 0. Files and review state

| file | sha256 | review state, as last relayed |
|---|---|---|
| `K7-structure-v1.md` | f4534c07c556557c9113c6db6106f081486316e326c6d92db3f069d5fc539fc1 | Codex: TRI, U, TWIN and Q5 ACCEPT; K7-Q and K7-COV ACCEPT-WITH-FIXES. Claude pending; parent verdict pending. |
| `K7-structure-erratum-v1.md` | f8642cb6d18877df1d4ba76c5cbe098dae6c274161f00b404abc30f76ce97138 | Will be dispositioned with the K7-structure verdict |
| `K7-block-lemma-v1.md` | 93c3cd1f2d0d41b332dc460aab33a6945e77b68202eb9e27f48b58dbd3129db3 | Codex review running (packet `review/sun-coset7-k7-blockpair-review-v1`). L6 (XE) is [NEW] and in scope. |
| `K7-pair-lemma-v1.md` | 77ce8b1bd0ad2803fd3d13d09aac03456b60f887b4dd2801e7e0bfcb85b88c3d | Same packet |
| `K7-unmarked-lemmas-v1.md` | ca80d7e5884de3831e35c1fcd69214abaef0c74d18bdd4108937094f41a3f242 | Queued, to follow the block/pair review |
| `K7-enumeration-spec-v1.md` | e5aa176b599b1fa21513bb2acaa126c8ef3863123cde2b8c7bf573fb0607795f | Specification only. It uses the opposite family convention (see erratum S1). |

## 1. M = ∅: which lemma excludes which reduced family

Setting: all seven vertices are unmarked (n_i = 6w_i), so U = V. The reduced data are a twin partition of V together with one quotient family, per K7-COV with erratum X2.

| # | reduced family (M = ∅) | excluded by (file, clause) | depends on |
|---|---|---|---|
| E1 | some twin block of size ≥ 4 (including b = 1, all seven twins) | K7-block-lemma-v1, K7-BLOCK (d)1 | K7-TWIN(d); L6; L5 with Sun(2)–Sun(4) in W_B |
| E2 | some twin block of size 3 | K7-block-lemma-v1, K7-BLOCK (d)2 (case M = ∅) | as E1 |
| E3 | Q5 (all β = 5) | K7-structure-v1 §5, K7-Q5 (\|U\| = 7 ≥ 5). Also reproved by K7-unmarked-lemmas-v1, K7-HIGH. | VFC-count; K7-Q |
| E4 | Q23 with at least two 2-classes | K7-unmarked-lemmas-v1, Theorem K7-Q23U | K7-pair-lemma-v1 P2 (uses P1, K7-PAIR (i) and (iii), and E2); K7-CLASS (L4 lower bound, L6, Sun(4) in an index-2 subgroup); K7-HIGH (VFC-count) |
| E5 | Q23 with a single 2-class (all β = 2) that contains a twin pair | K7-pair-lemma-v1: the proof of P3 applied with k_4 = 0 (both m = 3 and m = 6 fail; m = 2 fails by K7-PAIR (i)); recorded in erratum S1 | K7-PAIR (i)–(iii); L5 |

After E1–E5, two families remain open when M = ∅: O1 and O2 of §2.

## 2. M = ∅: the remaining open patterns

### O1: the all-2 pattern on seven unmarked singletons (every α = 2)

**VFC at a vertex.** At any vertex v the admissible values are q_vj ∈ {1, 2, 3, 4}. By a hand computation (unreviewed, not machine-checked), VFC-count at v refutes every q-vector **except** those whose multiset is one of:

  (4,4,4,2,2,1), (4,4,4,2,2,2), (4,4,4,4,2,1), (4,4,4,4,2,2), (4,4,4,4,4,2).

Example: for (4,4,4,4,4,2), the best weights give 5.5/6 < 1.

**Not computed:** whether RPLP-k7, P or K at each vertex refutes these vectors. O1 is OPEN.

### O2: family Q24 with M = ∅

These are 2/4 colourings of the pairs of twin blocks, with at least one 4, subject to:
- every block has size ≤ 2 (E1, E2);
- every twin pair B has at least three outside vertices with β(B, ·) = 4 (K7-pair-lemma-v1, P3);
- every vertex has a neighbour with α ≤ 2, either a twin or a block at β = 2 (K7-unmarked-lemmas-v1, the corollary of K7-HIGH).

The family is finite. It has not been enumerated or counted. O2 is OPEN.

## 3. M ≠ ∅ (one to three marked vertices): what is covered and what is not

**Structure that holds for every marking** (K7-structure-v1 with erratum):
- K7-TRI: markings enter only through d_v(r).
- K7-TWIN (a)–(d), on the unmarked set U.
- K7-Q: the trichotomy on U's blocks.
- K7-COV: the reduced data and the lift obligation, with X2 (VFC in the hypothesis) and X3 (the marking data fixed in the orbit criterion).

**Exclusions that hold for every marking:**

| exclusion | source | condition |
|---|---|---|
| twin blocks of size ≥ 4 | K7-BLOCK (d)1 | any M |
| Q5 when \|U\| ≥ 5 | K7-Q5 | \|M\| ≤ 2 |

**Structural, but excluding no pattern:**
- K7-BLOCK (a)–(c) for size-3 blocks: α_vB ≤ 3, exclusive cosets of W_B, and F-packing.
- K7-PAIR (i)–(iii) and P1: in Q23 with at least two classes, every twin pair has m = 6.

**Uncovered when M ≠ ∅. No written exclusion exists for any of:**
- the marked rows a_{zB} and the marked–marked values α_{zz′}, which are subject only to the d-relaxed triangle tables (K7-TRI) and the rules on the lift;
- size-3 twin blocks;
- Q23 and Q24 with markers;
- Q5 with |U| = 4, which needs three marked vertices, one per marker.

## 4. Not claimed

- No K7 exclusion: K7 is OPEN for both M = ∅ and M ≠ ∅.
- No count of reduced data. No enumeration. No compute.
- The archived, unsubmitted draft `archive/qsym-lemma-v1.unsubmitted-draft.md` (268605e0…ddcd; see `archive/MANIFEST-v1.md`) is not a premise of anything here.
