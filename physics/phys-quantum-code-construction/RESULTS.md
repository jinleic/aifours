# Results and proof boundary

Date: **2026-10-14 PT**.

**Overall verdict: OPEN-BLOCKED.** Neither unrestricted `((7,3,3))_2` nor `((11,5,4))_2` is solved here. **PARTIAL** describes the exact restricted certifications, not successful completion of the user's still-open/not-too-hard target selection. The exclusions are **ALREADY-SOLVED** in stronger prior literature. The CWS construction class is **HEADROOM-ABSENT** for the attacked targets and further construction requires **NEEDS-NEW-REPRESENTATION**. Independent review accepted the mathematical certificates; no Discovery or priority claim is made.

## Claim ledger

| ID | Precisely established statement | Evidence label | Novelty / review disposition |
|---|---|---|---|
| C1 | A `[[7,1,3]]_2` code exists, with the explicit generators and two codewords supplied. Its distance is exactly 3. | **Certification**, **Reproduction** | Known Steane code; no improvement. Two distinct exact implementations passed; Codex accepted the claim. |
| C2 | The enhanced quantum weight-enumerator LP including shadow positivity is feasible at `(n,K,d)=(7,3,3)`, with the rational vector below. | **Certification** | Known LP limitation [P11]; explicit replay witness, not a code and not SDP feasibility. |
| C3 | No general qubit `((7,4,3))` code exists; an exact rational Farkas identity proves this from valid LP constraints. Hence `K_max(7,3) <= 3`. | **Certification**, **Reproduction** | Known upper bound, not a stronger bound. |
| C4 | If a rank-r subspace Q of a dimension-D qubit stabilizer code V has `r > D/2` and `r >= 2`, then Q cannot have larger Pauli distance than V. In particular a hypothetical `((7,3,3))_2` code cannot have five independent common Pauli stabilizers. | **Certification** by the complete argument below | Standard Hermitian compression / stabilizer argument; priority not established and not claimed. Not a full nonexistence proof. |
| C5 | No `((7,3,3))_2` CWS code exists, including degenerate CWS codes. | **Certification**, **Reproduction** | Already proved by Chuang et al. [P11]. Analytic proof and 1,044-graph finite control agree. |
| C6 | Among CWS codes whose graph-state frame is a simple undirected **circulant graph on 11 vertices**, maximum dimension at distance at least 4 is **4**. This also covers **all vertex-transitive 11-vertex graph frames**. | **Certification**, **Reproduction** | Subcase of the stronger all-CWS result of Rigby–Olivier–Jarvis [P14, §III.C]. Independent bitset and maximal-clique implementations agree; Codex accepted the local certificate. No novelty. |
| C7 | A particular `((11,4,4))_2` positive-control code is explicitly given and has distance exactly 4. | **Certification** | Reaches, but does not beat, the known dimension-four lower bound. Independent CWS and integer state-vector checks passed. |
| D1 | The considered open targets have not been demonstrated to be “not too hard.” The tested cheap construction route is exhausted. | **Empirical evidence** for the screening history plus C2/C4/C6's exact restrictions | Negative selection decision. It does not assert that the unrestricted problems are impossible or objectively intractable. |

`[P#]` references are defined with primary links in [STATUS.md](STATUS.md).

## Replay commands and observed output

From this folder, one command replays all **local computational results**, without internet or an optimization solver. It does not replay the full published CWS classification:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify.py && /Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/verify_circulant.py
```

The two component commands were run and printed:

```text
PASS: K=3 enhanced LP feasible over rationals; K=4 Farkas contradiction 0 >= 1.
PASS: Steane distance 3 by 16384-Pauli enumeration and 211 exact state-vector compressions plus a weight-3 witness.
PASS: 1044 seven-vertex graph representatives; zero CWS dimension-3 candidates (including degeneracy constraints).
PASS: 3 negative controls rejected; source snapshot hashes matched.
FULL INSTANCE: OPEN. No general rank-3 projector or nonexistence certificate is claimed.
PASS: all 32 circulant frames independently reconstructed; no K=5, and 20 K=4 frames.
PASS: ((11,4,4)) control by CWS checks and 4984 integer state-vector compressions plus weight-4 witness.
```

C4 is an analytic theorem: the command verifies its finite-code corollary's LP premise, **not** a formal proof kernel for the dimension argument. C5's universal analytic proof does not rely on the graph-atlas completeness assumption. C6's finite statement relies on complete, easily replayed enumeration of the 32 explicitly specified connection masks, not on graph-atlas data.

The generation/search commands actually run were:

```sh
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/build_lp_certificates.py
/Users/jinleic/jinleic-workspace/scratch/ai4s-venv/bin/python code/search_circulant.py
```

The first printed the rational C2 vector and C3 multipliers. SciPy/HiGHS only proposed them; `Fraction` arithmetic accepted them and an independent implementation replayed them. The second printed `32` graph frames, `4983` nonidentity errors per frame, `K=5 hits: 0`, `K=4 control hits: 20`, and `25079` target-recursion nodes. Those counts are not a global search budget or evidence of general nonexistence.

Runtime versions recorded in `results/verification.json`: Python **3.13.9**, NetworkX **3.7**. NumPy integer arrays are used only for the eleven-qubit state-vector replay; sums are bounded by 2,048 and cannot overflow signed 64-bit integers. No floating-point comparison supports a code distance or exclusion.

## 1. Exact LP barrier and upper-bound certificate (C2–C3)

Let P be a rank-K projector on n qubits. Use the standard Shor–Laflamme enumerators

`A_j = sum_{wt(E)=j} |Tr(PE)|^2`,

`B_j = sum_{wt(E)=j} Tr(PEPE)`

for Hermitian Pauli strings E. Put `a_j=A_j/K^2`, `b_j=B_j/K`. The established MacWilliams identity and shadow inequalities [P3, Eqs. (5)–(11)] give

`b_j = (K/2^n) sum_i K_j(i;n) a_i`,

`s_j = (1/2^n) sum_i (-1)^i K_j(i;n) a_i >= 0`,

where `K_j(i;n)` is the coefficient of `x^(n-j)y^j` in `(x+3y)^(n-i)(x-y)^i`.

Necessary conditions at distance at least d are:

- `a_0=1`, all `a_j>=0`;
- `b_j=a_j` for `0<=j<d`;
- `b_j>=a_j` for all remaining j;
- every `s_j>=0`.

These conditions permit degenerate codes. We do not add purity, integrality, CWS, or stabilizer restrictions to the general-code LP.

### C2: a rational feasible point at K=3

For `n=7, K=3, d=3`, take

```text
a = (1, 0, 0, 0, 7, 14, 56/3, 2)
b = (1, 0, 0, 28, 63, 126, 112, 54)
s = (1/12, 0, 7/4, 28/3, 49/4, 56, 343/12, 20).
```

Every listed condition follows by direct rational substitution. `results/lp-feasible-7-3-3.json` stores a. The independent verifier obtains the transforms by repeated polynomial multiplication, not by importing the generator's binomial Krawtchouk formula.

This settles the proposed **LP-only** route negatively: no correct infeasibility certificate for these exact constraints exists at this target. It does **not** settle the complete SDP hierarchy, stronger relaxations, or existence of a physical projector realizing this enumerator.

### C3: explicit contradiction at K=4

For n=7 define the integer linear forms

`F_j = 4 sum_i K_j(i;7) a_i - 128 a_j`,

`T_j = sum_i (-1)^i K_j(i;7) a_i`.

A distance-three code with K=4 requires `F_0=F_1=F_2=0` and `T_0,T_1>=0`. Coefficient-by-coefficient polynomial expansion gives the **identical zero linear form**

```text
0 = a_0 + 4 a_1 + a_2 + 2 a_3
    + (T_0 + T_1)/16
    - 5 F_0/128 - F_1/64 - F_2/128.
```

Substitution of the necessary constraints makes the right-hand side at least 1, a contradiction. All nonnegative multipliers and equality multipliers are in `results/lp-infeasible-7-4-3.json`. The verifier checks every coefficient is exactly zero and the normalized contradiction constant is exactly one.

If a code of dimension greater than four existed, any four-dimensional subspace would inherit every Knill–Laflamme error-detection identity. Thus C3 excludes all `K>=4`, not only exactly K=4. Together with C1 it certifies the known interval `2 <= K_max(7,3) <= 3`.

## 2. A stabilizer-parent obstruction beyond CWS (C4)

**Lemma.** Let V be a dimension-D qubit stabilizer code with D at least two, and Q a rank-r subspace of V with `2<=r<=D` and `r>D/2`. If Q detects every Pauli of weight below d, then V also detects every such Pauli. Equivalently, taking a subcode larger than half the parent cannot improve its distance.

**Proof.** Fix a Hermitian Pauli E of weight below d and let S be V's stabilizer group, with signs chosen for its common +1 eigenspace.

1. If E anticommutes with an element of S, E sends V into its orthogonal complement. Consequently its compression to V is zero: it is already detected by V.
2. If E acts as a signed stabilizer, its restriction to V is scalar: again V detects it.
3. In the remaining case E commutes with S but is not a signed element of S. It preserves V. Its restricted square is the identity. Moreover
   `Tr_V(E) = (1/|S|) sum_{g in S} Tr(Eg) = 0`,
   because no `Eg` is a scalar identity. Its +1 and -1 eigenspaces V+ and V- therefore each have dimension D/2.
4. The elementary intersection bound gives
   `dim(Q intersect V+) >= r + D/2 - D > 0`,
   and the same for V-. Choose nonzero vectors in both intersections. If the Q-compression were `c I_Q`, its expectation on the first vector forces c=1; its expectation on the second forces c=-1. This contradicts detection on Q.

Case 3 is impossible. Every low-weight E is therefore in case 1 or 2, which is exactly detection by V. QED.

An independent viewpoint is the Hermitian higher-rank numerical range [P13]: a rank-r scalar compression of a Hermitian matrix must lie between its r-th smallest and r-th largest eigenvalues. For equal ±1 multiplicities and `r>D/2`, that interval is empty. The strict inequality matters: at `r=D/2`, the span of equal superpositions of paired positive/negative eigenvectors has zero compression.

**Seven-qubit corollary.** Five independent commuting Pauli operators acting scalarly on a hypothetical rank-three code define a dimension-four stabilizer parent. (Six independent generators would already leave dimension two.) C4 would make that parent a `((7,4,3))` code, contradicting C3. Hence any hypothetical `((7,3,3))` has **at most four independent common Pauli stabilizers**. General rank-three subspaces can have zero such stabilizers; nothing here excludes them. Local unitary changes of basis also preserve the support-size error-detection condition, but this observation is not a classification of all codes.

## 3. Known CWS barrier and its independent finite control (C5)

A standard-form CWS code has orthonormal basis `Z^c |G>` for a graph state G and binary words c. Translate all words by one of them, a local Pauli operation, to assume the set contains 0. Write a Pauli up to phase as `X^x Z^z`, with induced word `e=z+Gamma*x` over F2.

- For e nonzero, error detection requires that e not be a difference of two distinct code words.
- For e zero, the Pauli acts diagonally in the graph basis. Its phases must agree on every selected word; with 0 present this requires `c dot x=0` for every c.

For three words `{0,a,b}`, distinctness makes a,b linearly independent. Their nonzero differences are exactly `{a,b,a+b}`. Adjoining `a+b` adds no new difference, and its zero-syndrome phase constraints follow by linearity. Thus the four-word linear code `{0,a,b,a+b}` has the same error-detection property and is a stabilizer code. For n=7,d=3 this contradicts C3. This is the known structure theorem of [P11], not a new result.

As a redundant exact control, `verify.py` enumerates all 1,044 seven-vertex graph representatives in NetworkX's graph atlas. For each frame it constructs every induced error of weights one and two, imposes every zero-syndrome phase constraint, and checks all pairs of nonzero admissible words. **Zero** frames admit a three-word set. **864** of the graph frames have a graph-state stabilizer of weight below three, so simply ignoring degeneracy would not have checked the same search space. The atlas is a shared external data dependency; the analytic argument above removes it from the universal theorem's proof.

## 4. Restricted reproduction: eleven-qubit symmetric graph frames (C6–C7)

### Finite contract and exhaustive reduction

The full target is `((11,5,4))_2`, which would beat the dimension-four lower bound in [P3, Table 1]. We restricted the **construction frame**, not the classical word set, to the 32 simple undirected circulant graphs

`vertices = Z/11Z`,

`edges i~j iff j-i belongs to +/-D`,

`D is any subset of {1,2,3,4,5}`.

For each graph, generate every Pauli of weights one, two, and three: `33+495+4455=4983` errors. Translate a prospective word set to contain 0. Define V to be every nonzero word that is neither an induced nonzero error nor forbidden by a zero-syndrome phase constraint. Two vertices a,b in V are adjacent exactly when their difference is not an induced nonzero error. The phase constraints are linear, so the difference automatically satisfies them.

A five-dimensional code exists in this frame **if and only if** this graph on V has a clique of size four. A larger code would contain a five-word subcode, so excluding size five excludes all larger dimensions in the same frame.

The search program exhaustively branches on increasing vertex indices, intersecting with adjacency at each step; the population-count cutoff only prunes branches with fewer vertices than still needed. It considers every prospective four-clique. The independent verifier reconstructs all error syndromes using set symmetric differences, rebuilds compatibility edges, and uses a separate maximal-clique enumeration. Neither imports the other's implementation.

### Observed exact result and mathematical consequence

- All 32 masks were checked, with no omitted connection set.
- Twelve frames have no admissible nonzero word.
- Twenty frames have 165 admissible nonzero words and compatibility-clique maximum exactly three.
- Thus no frame has K=5; twenty frames have K=4.
- `results/circulant-11-5-4.json` records all raw frame inputs, admissible words, and positive controls.
- `results/circulant-verification.json` records the independently reconstructed result.

This proves the maximum is exactly four **within this family**.

**Prior-art resolution:** [P14, §III.C] already reports the same upper bound for the entire eleven-qubit CWS class, after exhaustive LC-class searches. Its n=11 result must not be confused with the heuristic clique search explicitly used at n=12. The present computation therefore reproduces a strict subfamily of a known result. It supplies a small independently checked artifact, not a stronger theorem.

**Vertex-transitive extension.** The automorphism group of a vertex-transitive graph on 11 vertices has order divisible by 11 by orbit–stabilizer. By Cauchy's theorem it has an element of order 11. As a permutation of 11 vertices this element is an 11-cycle. Relabeling along that cycle presents the graph as one of the 32 circulant graphs above. Consequently the same bound covers every **vertex-transitive graph-state frame** on 11 vertices. It does not require that the selected codeword set itself be cyclic or transitive. It does not cover an arbitrary non-vertex-transitive frame, much less every quantum code.

### Explicit positive control and independent distance checks

The first positive frame has offsets D={1,2}. Its four word labels are

`{0, 189, 599, 746}`,

where qubit j is integer bit j. An explicit amplitude formula is

`|c> = 2^(-11/2) sum_s (-1)^(sum_{edges ij} s_i*s_j + sum_j c_j*s_j) |s>`.

Edges and all conventions are in `results/circulant-11-4-4-anchor.json`. The CWS error criterion verifies distance at least four. A second implementation builds all 2,048 integer amplitudes for each of the four vectors and checks all 4,984 Pauli compressions of weights zero through three, without floating arithmetic. The Gram matrix is `2048 I_4` before normalization. The weight-four string `XYXIIYIIIII` has a nonscalar compression, proving distance exactly four. The implementation represents Y by XZ, differing only by a global phase; scalar-versus-nonscalar and zero-versus-nonzero compression are invariant under that phase.

This code is a **positive control**, not a new parameter record. The unrestricted primary interval remains `4 <= K_max(11,4) <= 7`.

## 5. Exact blocker and next-action decision

The user asked for still-open but not-too-hard problems. This project has **not established that selection criterion**. The seven-qubit route starts behind a 2009 structural obstruction; its remaining feasible LP data lack projector realizability. The eleven-qubit assay was aimed at a genuine unrestricted gap, but the stronger 2019 CWS classification was initially missed. Both the locally tested family and the larger CWS class are already closed. The existence of simulators or fast certificate checkers is not an argument that the remaining problem is easy.

**Single most valuable next action:** derive a bounded realizability constraint for **genuinely non-CWS rank-five projectors** at `((11,5,4))_2`, beyond the weight-enumerator relaxation. No such missing lemma or promising unrestricted ansatz is established here. The earlier idea of searching non-vertex-transitive CWS frames is **withdrawn** in light of [P14]. Further CWS search and unstructured numerical restarts are not justified. This is an exact representation blocker and a negative selection decision, not a promise of a solution.

## 6. Independent review

The first hostile review ran through Codex CLI 0.162.1 using the configured **gpt-6.1-sol**, **max** effort, **read-only** sandbox; it exited 0. Prompt, report, logs and input hashes are in `review/codex-prompt.md`, `review/codex-review.md`, `review/codex-stderr.log`, and `review/invocation.json`.

- **Referee verdict:** READY as a restricted-certificate and negative-selection report; **zero findings**.
- **Disposition:** accepted the absence of mathematical objections, not an assertion of literature completeness. The reviewer independently recomputed the rational LP, Steane distance, all 32 eleven-qubit compatibility graphs and clique obstructions, and selected integer-amplitude controls; it source-audited the full eleven-qubit compression loop and graph-atlas loop. Exact details of what it did are in the unedited report.
- **Author-discovered prior-art issue, found while that frozen review ran:** [P14] gives a stronger all-CWS exclusion at n=11,d=4. Verified directly in its primary text (§III.C), then pinned the PDF. **Disposition: fixed.** C6 is now labeled Reproduction, the novelty-unclear description is removed, and further non-vertex-transitive CWS search is explicitly withdrawn. The original referee report is retained verbatim as a review of the earlier hashed snapshot; its READY verdict is not represented as review of this later literature correction.
- **Target-selection issue:** neither original nor amended assay established an easy open target. **Disposition: retained as a failure to meet that criterion**, prominently in README.md and STATUS.md. No newly solved open instance is claimed.
- **Second-pass review:** `review/codex-prior-art-review.md`, same configured model/effort and read-only sandbox, exited 0; verdict **READY-WITH-FIXES**. It checked the primary PDF hash, Table I's count of 45,144 LC classes, the reported 3,060 dimension-four cases and absence of larger codes at n=11, and the separate heuristic n=12 qualification. This was a primary-text check, not replay of those 45,144 classes.
- **Second-pass finding 1 (minor):** stale “Actual open-instance attack” heading and overly broad “every computationally load-bearing result” replay wording. **Disposition: fixed.** The heading now says “Restricted reproduction”; README.md and this file limit the command to **local computational results** and explicitly exclude replay of the complete published classification. These were wording-only changes; the numerical records and code did not change.
- **Final local replay:** the single combined verification command above was run after the source correction and printed all seven displayed PASS/OPEN lines. Six pinned primary-source snapshots were hash-verified. The final wording-only review fixes do not alter computational inputs.
