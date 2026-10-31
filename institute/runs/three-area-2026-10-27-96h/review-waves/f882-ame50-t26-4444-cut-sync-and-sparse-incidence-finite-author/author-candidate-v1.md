# F882 author candidate: exact finite scrutiny of q=4444 cut synchronization and single-F sparse incidence

**Prospective GENERAL AUTHOR candidate. Nonblind, same harness. Not a parent disposition.** This document contains: written finite lemmas, written alternative routes for two steps of S2, a precise conditional finite model, and one new standalone stdlib verifier, `finite-4444-sync-sparse-v3.py`, which is **UNRUN**. Every verifier outcome below is labelled as a **written prediction**. None is an observed result. Earlier files v1 and v2 are **UNRUN and SUPERSEDED** (see §7). Running v3 requires a full parent source read and a separate one-shot GO.

## 0. Object, quantifiers and what is claimed

Fix **one** normalized complex four-party tensor ψ in **one** product orthonormal basis. Put `U=6ψ`. Assume:

- all three balanced 36×36 flattenings of U are unitary;
- the support has 50 words;
- exactly 26 support words have modulus one (the set P);
- the other 24 words (the set E) use E-alphabets of sizes (4,4,4,4).

Throughout, P and E are the **same** sets in all six pair systems and all three cuts. Amplitudes are arbitrary nonzero complex numbers. I do not assume a phase ansatz, real entries, independent cut realizability, a global t bound, or a no-OLS theorem.

Claims made here:

1. **(W1, written)** A synchronization identity and an exact classification of the high binary support Ω, under the imported T/T cut interface. Both directions are written out in §2.
2. **(W2, written)** Two elementary routes inside S2 §4b. The X/X sparse case dies by multiplicity counting alone, without the closed binary box. Case II dies without using S2's degree list (7). See §3.4–§3.5.
3. **(W3, written)** The four-bit star propagation is an orientation lemma on K4. See §4.
4. **(V, prepared, UNRUN)** A bounded exact verifier. It replays W1 by exhaustion over all 2^16 masks and all 1,820 four-word sets. It also replays the entire single-F sparse model of S2 §4b with explicit pair multiplicities, degrees and saturated one-overlap, plus controls and reason mutants. See §5.

I do **not** claim any of the following:

- a global E/P enumeration or a phase or amplitude solution;
- AME(4,6) feasibility or infeasibility;
- a complete t=26 or N=50 exclusion;
- a family, human or formal acceptance, or publication priority.

## 1. Conditional imports (named, not re-proved here)

The following come from S2 (with S3/S4 restating parts of them). They are **imports**, and the finite model is conditional on them.

- **I1 (actual-unitary cut interface, S2 §1).** Each residual 10×10 cut support is one of two types:
  - X: two 3×3-minus-one components plus two full 2×2 components;
  - Y: one connected 4×4 component with 12 entries plus three full 2×2 components.

  Pair systems are T (four E values of multiplicity 3, six of multiplicity 2) or F (two of multiplicity 4, eight of multiplicity 2). F/F never occurs. In F/T, the two F rows are full on the four T-high columns, and the two other component rows have disjoint complementary two-element supports partitioning those columns. In T/T, X has its four high rows and four high columns split 2+2 between its two 3×3-minus-one components, whose unique zero is at the low-row/low-column position. Y's high block is all 16 positions minus a permutation.
- **I2 (surplus classification, S2 §3).** Every party has exactly two high symbols `H_i` of surplus two, and two low E-symbols of surplus zero. In T, the four multiplicity-3 values are exactly `H_i×H_j`. In F, the two multiplicity-4 values form a matching between `H_i` and `H_j`. Also d≥2, Σd=10, and degree is independent of the partner party (S2 (1)).
- **I3 (degree-two/surplus-two slice lemma, S2 §2 (3)).** A high symbol of degree two has exactly one incident F pair. Hence a high symbol all of whose pair systems are T has degree 3.
- **I4 (S2 §4a).** At most one F pair. This is used only to delimit the coverage in §6; it is not modelled.
- **I5 (S2 §5b, star-form lemma (10)).** This is the low-row star form in each cut for four-bit parity Ω. Only the subsequent propagation step is modelled (§4).

Also used: actual row/column orthogonality forbids two **complete** rows (or columns) of one pair system from meeting in exactly one nonzero (S2 §1, S3 §1). Here "complete" means the row has reached its exact final multiplicity.

## 2. W1: synchronization and the high binary support

Assume no F pair, so all six pair systems are T (S2 §5 setting). Encode each `H_i` as {0,1} and define

```
Ω = E ∩ (H_A×H_B×H_C×H_D) ⊂ {0,1}^4.
```

### 2.1 Ω is the high block of every cut

Fix a cut ij|kl. By I2, the four multiplicity-3 rows are exactly the values `H_i×H_j`, and the four multiplicity-3 columns are exactly `H_k×H_l`. The other rows and columns have multiplicity 2.

- In type X, the lines of degree three are exactly the two high rows and two high columns of each 3×3-minus-one component. Full 2×2 blocks have only degree-two lines. Hence the restriction of the support to high rows × high columns is
  ```
  R_1×C_1 ⊔ R_2×C_2,   R_1⊔R_2 = H_i×H_j,   C_1⊔C_2 = H_k×H_l,   |R_t|=|C_t|=2.     (2.1)
  ```
  This is 8 entries.
- In type Y with T/T, the 12-entry component has degrees 3333 on both sides. Its lines are exactly the high lines, and the high restriction is 16 positions minus a permutation (12 entries).

An E word lies in that high restriction **iff** all four coordinates are high, i.e. iff it lies in Ω. So for each cut c,

```
|Ω| = 8  if cut c is X,     |Ω| = 12  if cut c is Y.                                   (2.2)
```

Ω is one set, the same in all three cuts. Hence **all three cuts have the same type**. Mixed X/Y is impossible for one actual tensor. If each cut were allowed its own independent mask (the "drop common tensor" mutant), then an X mask in one cut and a Y mask in another would both exist, but they would be different sets of sizes 8 and 12. The verifier counts this explicitly (§5).

**Boundary.** F/T cuts are excluded from this section by hypothesis. The single-F case is §3, and two or more F pairs are I4.

### 2.2 All three cuts X ⟺ Ω is one of exactly ten parity sets

(⇒) Under (2.1), each high row and each high column has exactly two Ω entries. So every one of the six pair projections of Ω takes each of its four values exactly twice. Put `F=2·1_Ω−1` on `{±1}^4`. Then:

- `ΣF = 2·8−16 = 0`;
- each `Σ_x F(x)x_i = 2Σ_{Ω}x_i = 0`;
- each `Σ_x F(x)x_ix_j = 2Σ_{Ω}x_ix_j = 0`, because each pair projection is balanced.

By S2's identity `F=x_Ax_Bx_Cx_D(c_0+Σc_ix_i)` and `F²=1`, exactly one coefficient is ±1. So Ω is one of:

- `{x: x_i⊕x_j⊕x_k = e}`: 4 choices of the triple × 2 values of e = 8 sets; or
- `{x: Σx = e (mod 2)}`: 2 sets.

That is 10 sets in total.

(⇐) Each of the ten sets is X in every cut.

- Four-bit parity: in cut ij|kl, row `(x_i,x_j)` is supported exactly on the two columns with `x_k⊕x_l = e⊕x_i⊕x_j`. Rows of equal `x_i⊕x_j` share a column pair, and the two pairs are complementary.
- Three-bit parity on i,j,k with l free:
  - in ij|kl, row (x_i,x_j) has `x_k` fixed and `x_l` free;
  - in ik|jl, row (x_i,x_k) has `x_j` fixed and `x_l` free;
  - in il|jk, row (x_i,x_l) has `x_j⊕x_k = e⊕x_i`.

  In each case the rows with equal key share a complementary column pair, which is form (2.1).

So the set of masks that are X in all three cuts is **exactly** these ten. This is a two-direction identity, not only a necessary filter.

**Written counting predictions for the verifier table** (hand counts, used as cross-checks):

- In one fixed cut, the number of X-type masks is 3 (row pairings) × 3 (column pairings) × 2 (matchings) = **18**.
- In one fixed cut, the number of Y-type masks is 4! = **24**.
- No mask has both an X and a Y cut.

### 2.3 All three cuts Y is impossible

If every cut is Y, let `Z=Ω^c` (four words). In each cut, Z is a permutation in the high block. So **all six** pair projections of Z are bijective onto {0,1}².

Label Z by its (x_A,x_B) values. Bijectivity of AC and BC forces `x_C = x_A⊕x_B⊕e`. Likewise `x_D = x_A⊕x_B⊕f`. Then the CD projection takes only two values, which is a contradiction. This is S2's four-word argument.

The verifier checks it independently by exhausting all 1,820 four-subsets of {0,1}^4: predicted zero have six bijective projections. It also checks that no 12-mask is Y in all three cuts. Hence |Ω|=8 and Ω is one of the ten sets in §2.2.

## 3. Single-F sparse incidence: exact model and W2

### 3.1 Normal form (conditional on I1–I3)

Let AB be the unique F pair and use symbols {0,1}=high and {2,3}=low at every party. The F rows are `(0,0),(1,1)` (the matching; without loss of generality). Since only AB is F, AC, AD, BC, BD and CD are all T. By I3, the high C and D symbols have degree 3. By Σd=10 and d≥2, the low C and D symbols have degree 2.

The AB|CD cut is F/T of type Y. Its 12-entry component consists of:

- the two F rows, each full on the four high CD values (8 words);
- two further distinct AB rows r, r' from the 14 other AB values;
- their two-element supports, which partition the four high CD values: axis-C `{c fixed}`, axis-D `{d fixed}`, or diagonal, in either order.

This gives **91 × 3 × 2 = 546 core assignments**. Rows are typed X (high/high), Y (high A, low B), Z (low A, high B) and W (low/low).

### 3.2 The other twelve E words are forced into 4 + 4 + 4

The ten CD E values are as follows.

- The four high-high values have multiplicity 3 and lie entirely in the core: 2 words from the F rows plus 1 from the sparse partition.
- A high C symbol c has D-neighbors both high D symbols plus exactly one low symbol `δ_c`. The value `(c,δ_c)` has multiplicity 2. Likewise each high D symbol d has a unique low C partner `γ_d`.
- The low D symbols have total degree 4 at C. The high C symbols take 2 of those edges, so exactly **two** low-low CD values remain, each of multiplicity 2.

So E consists of: the 12 core words, plus 2 words at each of the four contexts `(c,δ_c)` and `(γ_d,d)`, plus 4 low-low words. That totals 24, so no other word exists.

### 3.3 Context identity

Take a high C symbol c, with s(c)=2·3+2=8. Its six high-D words are exactly the core words with C=c. Its two remaining words both have D=δ_c, so they must have distinct AB values.

c has A-neighbors 0, 1 (each with multiplicity 3, since T high-high) and exactly one low λ (with multiplicity 2). So the A-multiset of the two words is

```
{3,3,2,0 at 0,1,λ,λ'} − (A-counts in the core slice at c),                              (3.1)
```

and the same holds for B. Both differences must be nonnegative and sum to 2. The same identity holds for a high D symbol. This is S2's matching rule (8), derived here without first restricting to the residual pairs (6).

### 3.4 W2a: X/X dies by counting alone

S2 shows that the partition is diagonal. In X/X (rows (0,1),(1,0), the off-matching ones), every high c meets one word of each sparse row. Its core slice therefore has A-counts 3,3 at the two high A symbols and B-counts 3,3 at the two high B symbols. By (3.1), **both** remaining words at c are `(λ_c, μ_c, c, δ_c)`, i.e. the same word, which is a contradiction.

S2 instead uses the closed binary box (4). That route is also valid in this case: every high row is complete inside the box. The counting route needs no Pauli or spin-flip identity. The verifier reports the X/X core both as `closed_box` and as a context-stage rejection, and it **does not** use the box to reject anything.

### 3.5 W2b: Case II without the degree list (7)

Take residual II, `(a_0,β),(α,b_1)` = (0,2),(2,1). By (3.1), each of the four contexts uses

- `M_0 = {(1,0),(2,2)}`, or
- `M_1 = {(1,2),(2,0)}`.

Each AB value of `M_0` and `M_1` has capacity 2. So each matching is used exactly twice, giving **C(4,2)=6** assignments. After these 20 words, eight AB E values are complete:

- F: (0,0), (1,1);
- sparse: (0,2), (2,1);
- matchings: (1,0), (2,2), (1,2), (2,0).

The four low-low words must therefore add exactly two new AB values, each with multiplicity 2. Current AB degrees:

- A: (2,3,3,0);
- B: (3,2,3,0).

The symbols α'=3 and β'=3 each need degree ≥2 (S2 (1)). Two new edges can achieve that only if both edges are (3,3), which is impossible because they must be distinct. This holds for **every** allowed degree multiset (2224 or 2233), not just (7).

Case I is as in S2. `(α,β)=(2,2)` already has its two words, so `M_0` is impossible. Then `M_1` used four times gives (1,2) multiplicity 4 > 2.

### 3.6 What the model encodes and what it omits

**Encoded constraints:**

- exact pair-line capacities: F 4, other AB 2, T high-high 3, other 2;
- the C/D degree bounds (≤3 high, ≤2 low) during search;
- at the end:
  - every pair system has 10 values with exact multiplicities and all required high values;
  - every symbol has equal degree at all three partners, in [2,4];
  - C/D degrees are exactly 3/2;
  - occurrences s = 2d+2 (high) or 2d (low);
  - AB degree multisets are in {2224, 2233};
- the saturated one-overlap rule at every node and at the end;
- final cut shapes: AB|CD must be Y, and the other two cuts must each be X or Y.

**Not encoded:**

- the closed-box lemma (counted only);
- phases and amplitudes beyond the one-overlap consequence;
- P words;
- the I3 lemma itself (only its consequence, C/D high degree 3, is used);
- the low-row structure of the other two cuts beyond their shapes.

## 4. W3: four-bit star propagation

Under I5, each of the six pairs `ij` places its star's low endpoint at i or j. If any pair places it at i, then every pair incident to i places it at i.

Suppose AB places it at A. Then AC and AD do too. If BC places it at B, then AB must be at B; if at C, then AC must be at C. Both are contradictions. So no orientation of K4's six edges satisfies this rule. The verifier checks all 2^6 = 64 orientations and predicts 0. The drop-propagation mutant admits all 64.

## 5. The prepared verifier (UNRUN)

**File** `finite-4444-sync-sparse-v3.py`, in this wave directory:

| Property | Value |
|---|---|
| Size | 24,434 bytes (as reported by the write tool) |
| Lines | 583 LF (from a read display of its ending) |
| SHA-256 | **not computed by the author**: a hashing subprocess was avoided under the no-child-subprocess rule. The parent must bind a live hash before any GO. |
| Dependencies | stdlib only (`collections`, `itertools`, `json`, `signal`, `sys`, `time`) |
| I/O | no input or output files; JSON status lines on stdout, flushed per line |
| Deadline | internal 39 s (SIGALRM plus a monotonic guard); parent outer limit ≤55 s |
| Exit codes | 0 = main checks complete and all agree; 3 = main complete with a disagreement; 124 = main incomplete; 1 = error |

The final drop-one-overlap pipeline mutant runs after the main status. It is diagnostic only and reports its own completion, timeout or error status.

**Phases and predictions.** These are the written predictions, encoded as `expected`:

1. **high_support.** Visits all 65,536 masks × 3 cuts.
   - The set of three-cut-X masks equals the ten parity masks: True.
   - Three-cut-Y masks: 0.
   - Six-pair-bijective four-sets among 1,820: 0.
   - Masks with both an X and a Y cut: 0.
   - Drop-common-tensor mutant: independent X and Y masks exist (True).
   - It emits the full size/type table. Hand predictions: 18 X and 24 Y in each single cut.
2. **controls.**
   - A synthetic 24-word X cut graph is recognised as X, and a synthetic Y graph as Y.
   - Deleting one word gives `other`.
   - The case-II core's context options at c=0 equal exactly `{M_0, M_1}`.
   - The X/X diagonal core is a closed box but has **no** context option (W2a).
   - A Y/Y fixture `(0,2),(1,2)` with diagonal supports is accepted without one-overlap and rejected with it. The witness is two complete AC rows meeting once, as in S2.
3. **I_II_matching.** Expected values: case I, 0 capacity-surviving assignments; case II, 6; degree completions, 0 under the general multisets (W2b) and 0 under (7).
4. **four_bit_star.** 0 propagated orientations out of 64.
5. **single_F_sparse.** Expected values: 546 core assignments; 0 strict survivor completions; 0 closed-box-core survivors. For each type/partition label it also reports:
   - the core census under four rule sets (multiplicity only; +CD degree; +one-overlap; all);
   - rejection reasons by stage;
   - high-boundary nodes reached;
   - pair/degree completions.
6. **mutant_drop_one_overlap_pipeline.** The same search with one-overlap removed both in pruning and at the end. No written prediction is made. It measures which supports satisfy every encoded multiplicity, degree and cut-shape constraint except one-overlap. Any 24-word completion it finds also exercises the final-stage functions.

A disagreement would mean either a verifier defect or a defect in the written step named by that check. Neither is presumed. Timeout output is never a PASS.

## 6. Coverage of the written chain

| Written step (S2) | Status here |
|---|---|
| §1 cut interface, T/F alternatives, component masks | Import I1 |
| (1) degree/surplus sums; (2) | Import I2 / not needed |
| (3) degree-two/surplus-two slice | Import I3, used as C/D high degree 3 |
| Closed binary box (4) | Not used to reject; X/X instead by W2a |
| §3 surplus partitions; (5) exclusion of (4) | Import I2 |
| §4a ≤1 F | Import I4 (not modelled) |
| §4b axis exclusion, X/Y/Z/W cases, (6)–(8), cases I/II | Modelled exhaustively (546 cores) and written W2 |
| §5 synchronization, Y no-OLS, parity classification | Modelled exhaustively and written W1 |
| §5a three-coordinate parity | **Not modelled** (written only in S2) |
| §5b star form (10) | Import I5; propagation modelled (W3) |

Overall coverage is as follows:

- zero-F case: W1 plus W3, conditional on I1, I2, I5 and the unmodelled §5a;
- one-F case: the full sparse model, conditional on I1–I3;
- two or more F pairs: I4 only.

Even if every prediction is confirmed, this would replay **necessary** local support constraints of S2's proof route. It is not a global enumeration of P/E supports.

## 7. Limits, process and read declarations

**Limits.**

- No verifier was run, so §5 contains predictions only.
- Model coverage is conditional on I1–I5, and S2 §5a is untouched.
- No P incidence (S3's profiles), no amplitude or phase system (S3 §8), and no AME existence or nonexistence is decided.
- The W1–W3 written arguments are author claims awaiting independent checking.

**Superseded files, both UNRUN.**

- `finite-4444-sync-sparse-v1.py` (21,038 B, 519 LF) is superseded for four reasons:
  - it used `int.bit_count` (Python ≥3.10 only);
  - its matching test hard-coded (7);
  - assertion failures aborted later phases;
  - it used the closed box to reject.
- `finite-4444-sync-sparse-v2.py` (21,855 B, 534 LF) is superseded because it lacked controls and the pipeline mutant.

Neither file was edited after writing, and neither was executed. The write tool automatically set the executable bit on all three `.py` files. This is a tool side effect; nothing was executed.

**Order and reads.**

1. Administrative reads, completed before any packet body or mathematics:
   - manifest, freeze receipt, final binding, metadata, and the actual dispatch receipt (already present; it names this agent and wave);
   - all 22 manifest-listed status-only controls, read raw and in full after collapsed initial displays.
2. Wrote `prebody-ack-v1.md`.
3. Sent a direct prebody ACK to Main; delivery was confirmed.
4. Read the sole packet part in raw windows 1–20, 21–40, …, 401–420, 421–434, including its ending. Every display was below 30,000 bytes, and no clipping was observed or needed recovery.

That read covered S1 LF 1–3, S2 1–182, S3 1–172, S4 1–22 and S5 1–33, all complete bodies. Links inside S4/S5 were not followed. No held episode or consumer, peer output, old code or unlisted file was opened.

**Execution and tools.** No network, external model, code execution, tests, compilation, scientific evaluation, solver, child subprocess, Git, deletion or formatter was used. The only operations were tool-level reads and writes, plus one message to Main.

**Discarded turn.** One of my earlier turns exceeded the runtime output limit, and the runtime discarded it together with its planned tool calls. No file or message from it exists. I disclose it as a process event only.

**Hashes.** Hashes are not recomputed here. Administrative pins are not correctness or source-identity certification.

Corrections must be new additive files. Parent disposition is separate.
