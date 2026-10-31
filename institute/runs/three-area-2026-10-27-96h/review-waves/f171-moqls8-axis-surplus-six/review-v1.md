# f171 review: in a four-MOQLS(8), every active coordinate costs at least six surplus units

- **Wave:** `f171-moqls8-axis-surplus-six`. Manifest `manifest-v1.json`: SHA-256 `f678d5de6fbe6cc7de7ccf9e7002036485070f0f776845d2decc695a71ad8bce`, 2795 B, verified before reading.
- **Reviewer:** ReviewF171AxisSurplus, a same-harness task agent.
- **Clock:** native `/bin/date` observed before composing this file was **2026-10-29T07:53:40-0700 PDT**. This is not an asserted file-creation time.

**Overall result: 0 FATAL / 0 MAJOR / 2 MINOR.**
- Every load-bearing mathematical claim is **WRITTEN_SUPPORTED**, at same-harness level.
- I reconstructed every embedded proof case independently by hand.
- Every finite claim (case lists, graph enumerations, tables, rank and moment inequalities) was reproduced by my own exact code, with no discrepancies.
- **The C10 and C4+C6 exclusions were reconstructed by hand only.** No actual-vector instance and no classical-mate control exists in this review for either configuration.
- This review is not human review, not independent-model-family review, not formal/kernel verification, and not a novelty or priority assessment.
- Author status language ("PASS", "excluded", etc.) was not used as evidence.

## 1. Read chronology, scope and edits

All clocks are `/bin/date`, 2026-10-29, PDT.

| Clock | Event |
|---|---|
| 06:54:16 | Verified the manifest's SHA-256 and byte count, then read it raw in full. |
| after 06:54:16, before 07:07:49 | Verified both inputs (SHA-256, bytes, LF), then read each raw in full in the declared order. (1) `dispositions/physics-4-moqls8-no-degree-two-mixed-graph-parent-v1.md`: `09c55d17704561ae4037ad86ec5c19e8b028741a100fa09617be68a2601ce1c8`, 5742 B, 19 LF. Used as scope-only context. (2) `physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261028-axis-surplus6-self-contained-v1.md`: `4534db97ff45e79ea1d909ad77e6b42d7753d5f9dc93e7ea86ba9765a0bb1a1c`, 27117 B, 170 LF. All three values matched the manifest. |
| 07:07:49 | Checked local Python 3.14.3. sympy is absent, so all exact arithmetic was hand-written (int / Fraction / Gaussian pairs). |
| 07:15:52 | The wave directory held only the manifest. I then created `rv171-controls.py`. |
| 07:15:52 to 07:39:42 | Debugged my own script in memory: I `exec`'d the file in the eval kernel with bytecode writing disabled. The debug runs wrote no files and are **not evidence**. I made two edits before the final run: (a) rewrote control R to use triangle enumeration with isomorphism reduction, plus an all-labelled mod-p determinant pass; (b) added the helper self-test (control 0) and its call in `main`. |
| 07:39:42 to 07:40:15 | **Single final run** of `python3 -B rv171-controls.py` with `PYTHONDONTWRITEBYTECODE=1`. Script SHA-256 was identical immediately before and after the run. The results file was created exclusively (mode `x`). 89 checks, 0 failures. I then parsed the whole results file with my own code. |
| after 07:40:15 | Parent capacity pause. I sent a status-only report and did no computation. |
| 07:47 to 07:53 | The parent placed `parent-capacity-resume-v1.json` in this directory (1162 B, SHA-256 `41cf072c36b8cb086f06eb9a3fef1a979ad52757ed9bd2d9e172124d794e0f25`). I hashed it as metadata only; I did not open its content. On resume I did no new computation; I only re-read my own results JSON to quote values. |

Scope notes:
- No errata, overlays or withdrawals were declared, and there is no certificate JSON among the inputs.
- **Not read:**
  - the original author artifacts cited by hash inside the candidate (`665c0f6433b9…`, `9b7790ec7cbe…`). I reviewed their text as embedded and did **not** check its byte identity with those hashes;
  - the f133 review, the parent spot check, and the four candidates linked from the disposition;
  - any other file.
- During this duty, Main sent two status-only notices about the f162 and f161 holds. **I accessed no f161 or f162 material.**

## 2. Reconstructed definitions

**Ordinary QLS(8) and four-MOQLS(8).**
- An ordinary QLS(8) is an 8×8 array of unit vectors in C^8 whose rows and columns are orthonormal bases.
- Four arrays Q, R, S, T form a four-MOQLS(8) when, for every pair (M, N), the 64 same-cell products M_x⊗N_x form an ONB of C^8⊗C^8.
- Equivalently, `<M_x,M_y><N_x,N_y>=0` for all distinct cells x≠y.

**Standardisation.** Fix a common row r0. Apply a local unitary to each member so that M_(r0,c)=e_c^(M) in that member's own basis. Product orthogonality is invariant under U_M⊗U_N. Bases of different members are never identified.

**Selected cell and weights.**
- x0 = (r0, a).
- For member Q and coordinate a, set W_rc = |<e_a, Q_rc>|².

**Support graph.** This is the bipartite row/column graph of the nonzero entries of W outside x0. Its nontrivial components have k rows and k columns and N cells.

**Surplus.** σ_a = |support| − 7 = Σ(N_i − k_i), summed over the nontrivial components.

**Mixed cell, active coordinate, completeness.**
- A cell is mixed when its ray is not collinear with any e_c.
- Coordinate a is active in Q when some mixed Q ray has a nonzero a-coefficient.
- A "local ray complete" means e_a^(M) occurs, up to phase, exactly once in every row and every column of M.

## 3. Verdicts per claim, with hand reconstruction

The "mates used" column records how many of Q's three mates each written exclusion actually uses. This is my observation; it matters for the tightness controls in §5.

| ID | Claim (candidate location) | Verdict | Mates used | Exact controls |
|---|---|---|---|---|
| S1 | Channel structure: the off-row 7×7 block is doubly stochastic; components are balanced; a degree-one vertex means a light singleton; min degree 2; σ = Σ(N−k); active ⇔ σ>0 (Setup; inner App. "definitions") | WRITTEN_SUPPORTED | 0 | P, F, K |
| S2 | 21-unit budget: the four members' off-row a-supports are pairwise disjoint on the 49-cell board | WRITTEN_SUPPORTED | all | F (three-family), K (GF(8)) |
| S3 | Surplus case lists: σ=2, 3, 4 (three cases), 5 (four types: two need new arguments) | WRITTEN_SUPPORTED | – | P |
| A1 | A sole 2×2 component is impossible with one mate, in any order n (inner App.) | WRITTEN_SUPPORTED | 1 | K1 |
| A2 | A sole 3×3 component, N=6..9, is impossible with three mates: K4-free bound, table, N=6 equality (inner App.) | WRITTEN_SUPPORTED | 3 | G, T, M |
| A3 | σ≥4 | WRITTEN_SUPPORTED | – | P |
| B1 | Sole C8: two-plane propagation, 4-ray ONB classes, disjoint transition supports (App. A §1) | WRITTEN_SUPPORTED | 3 | G, F |
| B2 | Two 2×2 components: all plane/basis cases (App. A §2) | WRITTEN_SUPPORTED | 3 if same basis, else 1 | X, K2, K3, K4 |
| B3 | Channel-rank inequality (1), frame-moment bound (2), N=10..16 table (App. A §3) | WRITTEN_SUPPORTED | 3 | G, T, M |
| B4 | N=9 equality case: Turán uniqueness, five partitions, no repeated pair, Bessel equality, BB^T, rank 9 (App. A §4) | WRITTEN_SUPPORTED | 3 | T, R |
| B5 | σ≥5; a sole 4-row component is impossible for every N=8..16 | WRITTEN_SUPPORTED | – | P, M |
| C1 | Cycle two-plane lemma: the rays of a cycle component alternate p ⟂ q in one plane containing e_a (main) | WRITTEN_SUPPORTED | 0 | F (instance) |
| C2 | Light-cell pigeonhole: one common basis on k rows forces k≤4 (main) | WRITTEN_SUPPORTED (see m2) | 3 | F (k=4 slack case) |
| C3 | A sole C10 (σ=5, k=5) is impossible (main) | WRITTEN_SUPPORTED, **hand only** | 3 | none (P only lists the type) |
| C4 | C4+C6 (σ=5) is impossible in all three plane/basis cases (main) | WRITTEN_SUPPORTED, **hand only** | 3 if same basis, else 1 | X covers only the generic cross-Gram lemma |
| C5 | Every active coordinate has σ_a≥6 | WRITTEN_SUPPORTED | – | P |
| C6 | At most three members are active at any selected-row coordinate; some member has its local a-ray complete | WRITTEN_SUPPORTED | all | K (GF(8), trivial instance) |

The scope and non-claim statements (no four-family construction, classicality, q1–q4, M(8), A10/A11, novelty, or five-family transfer) are consistent with what is proved. They need no verdict.

### Reconstruction notes, one step per load-bearing claim

**S1.**
- Row and column ONBs give every row and column sum of W equal to ||e_a||² = 1.
- Row r0 gives W_(r0,c) = δ_ca, so column a vanishes off x0, and all support other than x0 lies in the 7×7 block.
- Summing over a component gives #rows = #cols.
- A degree-one row has entry 1. Its column then has no other support, so the component is a singleton with Q ∝ e_a.
- Hence nontrivial components have N≥2k and contribute N−k≥k.
- A cell with W=1 would be a singleton. So cells of nontrivial components have 0<W<1: they are mixed and use a. Conversely, a mixed ray using a has 0<W<1. So active ⇔ σ_a>0.

**S2.** For y≠x0 and M≠N, `<e_a^(M),M_y><e_a^(N),N_y>=0`. So at most one member has a nonzero a-coefficient at y. This gives Σ_M(7+σ_(M,a)) ≤ 49.

**S3.** Components must satisfy 2k≤N≤k², Σk≤7 and Σ(N−k)=σ. Control P confirms the candidate's lists exactly:

| σ | Possible channel types |
|---|---|
| 1 | none |
| 2 | sole (2,4) |
| 3 | sole (3,6) |
| 4 | sole (4,8); sole (3,7); (2,4)+(2,4) |
| 5 | sole (3,8); sole (4,9); sole (5,10); (2,4)+(3,6) |

- N=2k forces a 2-regular graph. So (2,4)=C4, (3,6)=C6, (4,8)=C8 and (5,10)=C10.
- Of the σ=5 types, the candidate's "only two possible graphs" are the two that Appendix A does not already exclude.

**A1.**
- The n−2 singleton cells carry mutually orthonormal R rays. These are orthogonal to the four component R rays, because those cells have nonzero Q overlap with e_a.
- So the component R rays lie in a 2-space, and opposite component cells have collinear R rays.
- By Q⊗R, opposite Q rays are therefore orthogonal. The four component Q rays become orthonormal with total a-weight 2 > 1, contradicting Bessel.

**A2.**
- W_M has dimension 3, so every mate's orthogonality graph is K4-free.
- Adjacent pairs are orthogonal in all three mates; every pair is orthogonal in at least two of three, by the mate-pair products. So the total edge count is ≥ 2·C(N,2)+A.
- The K4-free bound floor(N²/3) holds by:
  - deleting a triangle (each outside vertex has ≤2 neighbours in it; identity 3+2(N−3)+floor((N−3)²/3) = floor(N²/3));
  - Mantel's bound N²/4 for triangle-free graphs, via Cauchy–Schwarz.
- The comparison is 36/36, 52/48, 70/63 and 90/81 for N=6..9.
- At N=6 equality forces exactly one nonzero mate per non-adjacent pair. Q⊗M then makes all six Q rays orthonormal, with a-weight 3 > 1.
- The candidate's K6-minus-matching remark is true (control T) but not needed.

**B1.**
- Each C8 line has exactly two support cells, and the line ONB gives e_a = c₁Q_y + c₂Q_y' with c₁c₂≠0.
- The shared mixed ray is not ∝ e_a, so adjacent line planes coincide. This gives one plane P ∋ e_a, with rays alternating p, q, one of each per line.
- Four singleton rows (including r0) put the component M rays in a 4-space W. Each 4-cell class with collinear Q rays gives 4 orthonormal M rays, an ONB of W.
- The p→q transition is a 4×4 unitary. Each p cell's row neighbour and column neighbour are two distinct q cells, so each transition row has two forced zeros.
- Different mates have disjoint transition supports. Three mates would need three of the two remaining positions in a row.

**B2.**
- (i) Same plane and same projective basis: the combined 4-cell classes are ONBs of W, and the B1 pigeonhole applies (each p cell is adjacent to two q cells of its own block).
- (ii) Same plane, different basis: all four cross overlaps are nonzero, since a zero cross overlap inside a 2-plane forces the same basis.
- (iii) Different planes: P1∩P2 = span(e_a).
  - G = U1*U2 has ||G||≤1, and Gβ = U1*e_a has norm 1 for e_a = U2β. So ||G|| = 1.
  - A zero row or column would make a basis ray orthogonal to the other plane, which contains e_a.
  - Two zeros on one diagonal make G diagonal or anti-diagonal with an entry of modulus 1. That forces a ray into span(e_a), so it would not be mixed.
  - So G has at most one zero.
- In (ii) and (iii) there are therefore at least three orthogonalities between the 2-spans A, B and C, D inside the 4-space W.
- Relabel within blocks, and swap the blocks if needed, to get A⟂C, A⟂D, B⟂D. Then C = D = A^⊥∩W and B = A.
- The block-1 transition is 2×2 and identically zero (both entries are row/column neighbours), yet both classes are ONBs of A. Contradiction.
- The "up to relabeling" is justified.

**B3.**
- With 4 singleton rows, dim W_M = 4 and the mate graphs are K5-free.
- Adjacent pairs (A of them) and Q-non-orthogonal pairs (H of them; disjoint from the adjacent pairs, because adjacent Q rays are orthogonal) are orthogonal in all three mates. Every other pair is orthogonal in at least two. This gives (1).
- The K5-free bound holds by deleting a K4 (identity 6+3(N−4)+floor(3(N−4)²/8) = floor(3N²/8)), with the no-K4 branch handled by floor(N²/3) ≤ floor(3N²/8).
- For (2), take S = Σ|Q_x⟩⟨Q_x|. Then ⟨e_a,Se_a⟩ = 4, tr S = N, and tr S² ≥ 16+(N−4)²/7 by Cauchy–Schwarz on the other seven diagonal entries. Also tr S² = N + 2Σ|⟨Q_x,Q_y⟩|² ≤ N + 2H.
- A_min follows from convexity of the balanced degree profile.

**B4.**
- At N=9 the profiles (3,2,2,2) are forced, A=12 and H≥⌈37/7⌉=6. Then LHS = RHS = 90, so every mate graph has exactly 30 edges.
- The direct uniqueness proof holds:
  - the K4-free bound is 27, so a K4 exists;
  - equality in 6+15+9 forces the outside graph to be K5−e, with each outside vertex missing exactly one clique vertex;
  - adjacent outside vertices miss different labels (otherwise a K5 appears);
  - the label multiplicities are therefore (2,1,1,1), which gives K_{3,2,2,2}.
- In the 4-space, each part is orthogonal to a 3-dimensional span formed by one ray from each of the other parts. So each part is a collinear class.
- This yields five (3,2,2,2) partitions: rows, columns, and the R, S, T classes. No pair of cells shares two blocks:
  - a row and a column meet in one cell;
  - within a line, mate rays are orthogonal, but within a class they are collinear;
  - two classes would violate the two mates' product ONB.
- Block weights:
  - rows and columns weigh 1;
  - each mate block's Q rays are orthonormal by Q⊗M, so the block weighs ≤1 by Bessel;
  - each mate's four blocks sum to 4, so every block weighs exactly 1.
- Bessel equality then gives e_a = Σ_{x∈β}⟨Q_x,e_a⟩Q_x for all 20 blocks, i.e. CDB = e_a 1^T.
- BB^T = 5I+(J−I)−Adj(H0) = 4I+J−Adj(H0). Since deg H0 ≤ 3, λ_max(Adj H0) ≤ 3 and BB^T is positive definite.
- So rank B = 9, rank(CD) ≤ 1, and all nine Q rays would be collinear. That is impossible, because each component row contains two orthogonal rays.

**C1.** The B1 propagation applies to any cycle component, since every incident line has exactly two support cells.

**C2.**
- On k rows, all component rays lie in {p, q}, with one of each per row (see m2).
- There are 8−k singleton rows, whose M rays are orthonormal and orthogonal to the component M rays. The p class gives k orthonormal M rays, so it spans the complement W_M.
- Since ⟨p,q⟩=0 with p_a q_a≠0, some b≠a has p_b q_b≠0.
- Q_(r0,b) = e_b overlaps every component ray. So M_(r0,b) is orthogonal to W_M and lies in the singleton span.
- M_(r0,b) is orthogonal to M_x0, because both are in row r0. So it overlaps some other singleton cell z; there are 7−k choices.
- Two mates cannot share z, because their product ONB covers the cell pair ((r0,b), z). Hence 3 ≤ 7−k.
- Observation: p_b≠0 alone suffices, because the p class already spans W_M.

**C3 (hand only).** A single cycle gives one plane and alternating p, q. With k=5 the C2 count leaves 7−5 = 2 cells for three mates.

**C4 (hand only).**
- With 3 singleton rows, W is 5-dimensional. The C4 classes give 2-spans A and B; the C6 classes give 3-spans C and D.
- Same plane and same basis: the C2 count applies on 5 rows.
- Same plane, different basis: all four cross overlaps are nonzero.
- Different planes: at most one zero, as in B2(iii).
- At least three orthogonalities remain. Relabelling within sides is enough, since the two sides have different dimensions: the missing edge, if any, can always be named B–C. This gives A⟂C, A⟂D, B⟂D.
- Then C = D = A^⊥∩W (3-dimensional) and B = A. The zero C4 transition contradicts both C4 classes being ONBs of A.

**C5, C6.**
- σ∈{1,…,5} is impossible, so σ≥6.
- Four active members would need ≥24 > 21 units.
- An inactive member has σ=0, so all its a-components are singletons. Together with x0, e_a^(M) then occurs exactly once in each row and column.

## 4. Findings

- **m1 (MINOR, notation).** Several symbols are overloaded:
  - "e_a" is both the coordinate vector and the support count (σ_a = e_a − 7, inner App.);
  - "S" is both a mate and the frame operator (§3);
  - "A" is both the adjacency-pair count and a mate span (§2);
  - "H" is the Q-overlap pair count, while "H_0" is a graph.

  There is no logical effect.
- **m2 (MINOR, unstated immediate step).** The light-cell pigeonhole ("all nontrivial a-components together use the same ray pair p,q and occupy k rows ... the two k-ray mate classes") silently needs exactly one p cell and one q cell per component row. This follows from the facts that a line ONB holds at most one ray collinear with p and at most one collinear with q, and that every component line has ≥2 support cells. Both applications (C10, and coincident-basis C4+C6) are cycles anyway. The claim is not affected.
- **No FATAL or MAJOR finding.**
  - No missing σ≤5 case.
  - Every "without loss of generality" or "up to relabeling" (B2, C4, the deletions in B3/B4, "an ONB beginning with e_a") is justified as shown in §3.
- **Non-defect observations.**
  - (i) §3 states t_4(N) = floor(3N²/8) as an identity, but its induction proves only the upper bound, and only the upper bound is used. The identity is nevertheless true for N≤60 (control T).
  - (ii) Several sub-cases need fewer than three mates (A1; non-coincident B2 and C4).
  - (iii) The theorem leaves σ=6 open. Control P lists 8 σ=6 types.

## 5. Exact controls and receipts

**Files and run:**
- Script `rv171-controls.py`: 50682 B, SHA-256 `5d076ca1511ec5e291cc0162a38a2c63003fb200eac33ecc21554bc1feef80af`, hashed immediately before and after the run.
- Results `rv171-controls-results.json`: 27620 B, 1735 LF, SHA-256 `8585dd2542d328a5ba479d7feffaab4b909b7efd4b0af54c40e923dfe040d39f`.
- Run window: 07:39:42 to 07:40:15 PDT, wall time 33.6 s.
- Python 3.14.3, run with `-B`. No cache or temporary files were written.
- Results: **89 checks, 74 positive and 15 negative, all OK**.
- The script imports no author code. "Negative" checks are cases that fail, or are shown impossible, for the intended reason.

| Control | Result |
|---|---|
| 0 self-test | `solve_exact`, `rank_exact`, `det_exact`, `det_mod_p` and `conn_mindeg2` are correct on known positive and negative inputs. |
| P partitions | σ lists exactly as in §3 (S3). σ=6: 8 types. **Negative:** allowing tree components (N=2k−1) would admit σ=1 (a sole (2,3)), so the degree-one lemma is load-bearing. Among 5×5 2-regular graphs, 2040 in total and 1440 connected: every (5,10) channel is a Hamiltonian C10. |
| G support graphs | 3×3, N=6..9: counts 6/18/9/1, with A forced to 6/10/14/18. 4×4, N=8: 72 graphs, all C8. 4×4, N=9: 816 graphs, both profiles (3,2,2,2), A=12. 4×4 true minimum A for N=10..16: 16/20/24/30/36/42/48. This equals the balanced formula and the candidate table. |
| T Turán | t_3 = floor(N²/3) and t_4 = floor(3N²/8) for N≤60. Both induction identities hold. Brute force gives ex(N,K4) for N=4..8 and ex(N,K5) for N=5..9. Caro–Wei bounds exceed s−1 for K4 up to N=9 and K5 up to N=16. **Exactly 1260 labelled 30-edge K5-free graphs on 9 vertices, all K_{3,2,2,2}** (complement K3+3K2). 6 vertices, 12 edges, K4-free: exactly 15 graphs, all K6 minus a perfect matching. **Negatives:** no 31-edge K5-free graph on 9 vertices; K_{3,2,2,2} minus an edge (29 edges) is K5-free but not complete multipartite. |
| M tables | 4×4 rows reproduced exactly (A, H, t_4, LHS, RHS): N=10 16,6,37,112,111; N=11 20,6,45,136,135; N=12 24,7,54,163,162; N=13 30,8,63,194,189; N=14 36,9,73,227,219; N=15 42,10,84,262,252; N=16 48,11,96,299,288. N=9: 90=90. 3×3 table reproduced. **Negative:** N=8 gives 70 ≤ 72, so (1) alone does not exclude C8 and §1 is needed. |
| R N=9 rank | 816 labelled graphs fall into 3 isomorphism classes (orbits 576/144/96). There are 219/220/526 pentads per graph (rows, columns and three mate partitions), **208,320 labelled pentads** in total. Over all labelled pentads: H0 has exactly 6 edges, max degree ≤3, and det(BB^T) ≢ 0 mod 2^31−1, so rank B = 9. On one representative per class (965 pentads), exact rational checks: BB^T = 4I+J−Adj(H0), rank B = 9, det(BB^T) > 0 (minimum 759375). The triangle enumeration agrees with a naive enumeration. **Negatives:** if two points shared all blocks, rank B < 9; setting T:=R gives an off-diagonal 2 in BB^T. **Observation:** B^T w = 1 is inconsistent for all 965 representative pentads. Given the block-weight lemma, this is a second, purely linear contradiction route; the candidate does not use it. |
| X cross-Gram | Gaussian-rational examples in C³. Different planes with exactly one zero, and det(GG*−I) = 0, so ‖G‖ = 1 and "at least three nonzero" is tight. Same plane, same basis: two zeros on one diagonal. Same plane, different basis: no zeros. Generic different planes: no zeros. Real-parameter polynomial identities show that double diagonal or anti-diagonal zeros with c≠±1 force an a-coefficient to vanish, or a ray ∝ e_a. **Negative:** with equal planes the double zero is realised, so plane distinctness is the operative premise. |
| F three-family | Q is built from the Z4×Z2 Cayley table: on the odd rows and columns, the C8 of symbols a=(1,0), b=(2,0) is replaced by e_a±e_b. It is an exact QLS with σ_a = σ_b = 4 (a sole (4,8)); every other coordinate is inactive. 128 Q-orthogonal transversals and 832 classical mates (complete enumeration). An orthogonal pair R, S gives an **exact three-MOQLS(8)**: every pair's 2016 cell-pair products vanish, and the a-supports are disjoint. §1 mechanism: each p cell has 2 adjacent q cells, and R and S use the two free q cells, disjointly. **Negative:** no class is compatible with both R and S. Over all 16 ordered orthogonal classical-mate pairs, there is no third mate. Light-cell count at k=4: 3 singletons, and R and S use distinct ones, so k=4 gives no contradiction. |
| K Z2^3 members | K0, classical: has classical mates. This search was capped at the first solution and is used for existence only. K1, sole 2×2: **0** classical mates (192 classes, exhaustive). K2, two 2×2 with the same basis: 4096 mates and 128 ordered orthogonal pairs, **no third**. K3, same plane with the e_a±i·e_b basis: **0** mates. K4, different planes: **0** mates. The GF(8) four-MOQLS(8) checks exactly, with every coordinate inactive: a trivial positive instance of C6. |

Classical-mate searches look only at mates made of standard basis vectors. They are consistency checks of special cases, not evidence for arbitrary complex mates; those claims rest on the written arguments reconstructed in §3. No solver was used. Every completed search was exhaustive, except K0, whose cap counts only as existence.

## 6. Exact dependency list

**Imports, pinned data, catalogues, numerical solvers:** none. The candidate is self-contained, with Appendix A embedded. The cited original-artifact hashes are historical, and nothing depends on them.

**Definitions:**
- ordinary complex QLS(8);
- four-MOQLS(8) via pairwise same-cell tensor-product ONBs, so Q has exactly three mutually orthogonal mates;
- independent standardisation at a common row.

**Conditional premises:** none beyond these definitions.

**Elementary results used:**
- ONB expansion; Bessel's inequality and its equality case; Cauchy–Schwarz; dimension counting;
- unitary transition matrices;
- ‖U1*U2‖ ≤ 1 for isometries;
- λ_max(Adj) ≤ max degree;
- Mantel and the K4/K5-free Turán bounds, all proved inline;
- uniqueness of the 30-edge K5-free 9-vertex graph, proved inline and confirmed exhaustively.

**Adopted disposition:** used only as scope context; it is not a premise.

## 7. Deviations and limitations

**Deviations:**
- in-memory debug runs before the final run;
- two script edits before the final run;
- metadata-only hashing of the parent-placed resume file.

Nothing was written outside this directory, no cache or temporary files were created, and nothing was deleted. I used no web search, external model or API, Git, or author contact.

**Limitations:**
- **C10 and C4+C6 were checked by hand only, with no actual-vector instance.** Group-based order-8 squares yield symbol-pair cycles of length 4, 8 or 16 only, and I attempted no other construction.
- Brute-force Turán checks stop at N=9 for K5 and N=8 for K4. Beyond that, the bounds rest on the verified induction identities, Turán-graph counts and the Caro–Wei arithmetic.
- The exact rational N=9 checks cover one representative per isomorphism class. Invariance covers the rest, and the labelled set additionally received the mod-p determinant and H0 checks.
- I did not check that the embedded appendices are byte-identical to their cited hashes.
- The result is a necessary condition only. No four-family existence or non-existence, classicality, q1–q4, M(8), A10/A11, novelty or five-family transfer is assessed.

## 8. Summary

All 17 load-bearing claims are WRITTEN_SUPPORTED, with 0 FATAL, 0 MAJOR and 2 MINOR findings. I found no missing case and no unjustified "without loss of generality". The claims cover:
- the channel lemmas and the 21-unit budget;
- the complete σ≤5 case list;
- the σ≥4 appendix (sole 2×2 with one mate; sole 3×3, N=6..9, with three mates);
- the σ≥5 appendix: C8 two-plane propagation with disjoint transition supports; all two-2×2 plane/basis cases; inequality (1) and the frame-moment bound (2) for N=10..16; the N=9 equality case through Turán uniqueness, five partitions, Bessel equality and incidence rank 9;
- the main-text cycle two-plane lemma, the light-cell pigeonhole, and the C10 and C4+C6 exclusions;
- σ≥6, and the conclusion that at every selected-row coordinate at least one member has its local ray complete.

The two MINOR findings are notation overload and one unstated but immediate one-p/one-q-per-row step in the light-cell pigeonhole. Every finite claim was reproduced exactly by my own independently authored code (89 checks, 0 failures). An exact three-MOQLS(8) with an active C8 member shows that the three-mate hypothesis in the C8 argument is essential. Exhaustive classical-mate searches agree with every sub-case exclusion they can test. The C10 and C4+C6 exclusions are supported by hand reconstruction only, with no actual-vector instance. This is same-harness review only. It is not human, independent-model-family, formal/kernel or novelty verification, and it asserts nothing about the existence of four-families, M(8), A10/A11 or priority.
