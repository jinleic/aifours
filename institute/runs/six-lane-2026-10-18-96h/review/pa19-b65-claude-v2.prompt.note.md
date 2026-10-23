# Hostile review: PA19 ms09 b65 whole fixed-skeleton exclusion (`proof-v1.md`)

**Target:** `/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19/continuations/ms09-b65-completion/proof-v1.md`. I treated parent erratum `a53cc298…` as governing scope.

**Method:** I re-derived every step by hand from the four hypotheses at `proof-v1.md:9-16`. I used no tools, file reads, hashes, computation or edits. I did not rely on the e7 dossier, its Codex PASS, erratum fc48075b or Theorems A/B.

**Verdict:** The theorem is correct, and the written proof is complete for the whole class.

**Counts:** FATAL 0 · MAJOR 0 · MINOR 4. All four MINOR findings are textual. None changes a quantifier or an implication.

## 1. Claim-by-claim

| Lines | Claim | Independent re-derivation | Verdict |
|---|---|---|---|
| 38-43 | Exact pair cover; non-quad blocks are T-disjoint | 5·(6+15) + 3·(12+9+1) = 171 = C(19,2). Rows sharing c already met in Q_c. | PASS |
| 47-62 | Pattern table; empty rows lie in 2 quads + 1 triple and no pair; the 3 pair blocks have nonempty, T-disjoint ends | 10+t P0 partners gives n_3+2n_4 = 5−t and n_2+n_3+n_4 = 3. The solutions are exactly those tabled. | PASS |
| 66-90 | Exactly one of C3, C0, Q4, Q1, T2 occurs | ΣC(eps,2) = 21. There are seven parts with fixed sums (7×5, 14, 7) and minima (2×5, 10, 0), so the total excess of 1 sits in one part. Then m_2+3m_3 = 3; quad cost = 9 + ½Σd²; a triple cost of 1 means one 2 and no 3. | PASS |
| 94-100 | I(r) = 7; the only rescues are C0's 0-triple and Q1's 1-quad | Otherwise a private pair endpoint has four P0 triples ≥1 and two quads ≥2. C3's 3-triple and Q4's 4-quad are all-empty. | PASS |
| 106-112 | g has pattern (2,0,1) and pairs with p_3, p_4; H_C = g + 3 empties; g's col-3 and col-4 triples each hold 2 empties | Under (1,2,0), I(g) ≤ 2+2+1+1 = 6 outside T2, and T2 leaves g's private partner unrescued. Under (2,0,1), 7 ≤ 2+2+3 and the bound is tight. | PASS |
| 116-126 | Category Q1; L_C = {p_0,p_3,p_4,e_0}; eps(L_A) = eps(L_B) = 2; H_A = H_B = 3; every C-triple has 1 empty | C0 would put p_3, p_4 together in one 0-triple and also in L_C. For p_3, 7 ≥ 4+1+2 is tight. The leftover quad multiset is {3,3}. The 7−3−1 = 3 remaining empties go into three C-triples of capacity 1. | PASS |
| 130-140 | p_1, p_2 have pattern (0,2,1); p_i ∈ L_A, p_j ∈ L_B; p_i's B-triple and p_j's A-triple have no empty; every P0 triple of p_3, p_4, p_i, p_j has occupancy 1 | A C-pair endpoint would need L_C, but its C-block is the pair. A high quad gives I ≥ 3+1+4. From 7 = 2+1+x+y with y ≥ 4, x = 0 and y = 4. | PASS |
| 144-155 | The edge graph is simple; e_0's other quad is high; u ∈ H_A | e_0 cannot be in L_A or L_B (it would meet p_4 or p_3 twice). The A-quads hold 5 empties = e_0 + V + one U_E row. If u ∈ L_A, then H_A contains e_0 and two rows of V, and any 2+2 split of {e_0}∪V joins two of them. | PASS |
| 157-172 | Quad table; column of each empty row's triple | U_E∖{u} and {v',v''} each split across the B-quads, so H_B's third empty is v. Degrees are 3,2,3,2,3,1, and all edges are distinct. Triples lie in columns B,B,A,A,C,C,C. | PASS |
| 174-181 | M has the 10 listed edges; (G) | 11 of the 21 pairs agree in P1 (3+1+3+1+3). Of the 3 perfect matchings of {e_0,v,v',v''}, only {e_0v', vv''} avoids P1. | PASS |
| 187-210 | f = 5 − deg_M; S(p_3), S(p_4), S(p_i); (J) | deg_M = 4,2,2,3,2,3,4 (Σ = 20 = 5·2·2); Σf = 15 = 5·3. Each S is E minus the row's P1 empty partners. p_i's C-triple empty lies in V∖{v',v''} = {v}. | PASS |
| 214-220 | O ↔ E bijection | See §2 | PASS |
| 224-248 | tau_1 = {p_3,p_i,w_4} with w_4 ∈ {u,u'}; w_3 ≠ e_0; {p_i,p_j,e_0} ∈ O; c_j = v'; {w_3,w_4} = {u,u'} | p_3's unmet nonempty T-disjoint rows are exactly b_0,b_1,b_2,p_i, and each b_k ∈ Q_4. e_0 lies in exactly one O triple. v lies in one C-block. Disjointness forces w_3 to be the other member of {u,u'}. | PASS |
| 252-266 | Contradiction in P0 column 4 | See §2 | PASS |
| 270-272 | Non-use statements | Confirmed: no AT2, Petersen, orbit list, solver, placement list or Theorem A/B is used. | PASS (wording issue: MINOR-4) |

Every fact family in the brief is re-derived inside the file:
- pair cover: `:38-43`
- row patterns: `:47-62`
- occupancy categories: `:66-90`
- empty incidence and private rescue: `:94-100`
- four-row matching (the erratum's replacement for the Petersen bound): `:155`, `:179`
- b65 normal form: `:106-140`
- high/low quads: `:116-126`
- actual-empty graph: `:144-181`
- occupancy-1 triple counts: `:187-196`
- shared triples and the e_0 constraint: `:224-246`

## 2. Targeted audits

**O ↔ E bijection (`:214-220`).** The argument needs four facts, and each holds:
- Under Q1 every P0 triple has occupancy 1 or 2. Each M-edge is realised in exactly one occupancy-2 triple, and distinct occurrences of w have distinct partners. So f(w) is exact.
- All P0 triples of p_3 and of p_4 have occupancy 1 (`:120`). They therefore carry S(p_3) and S(p_4) bijectively.
- T_3 and T_4 are disjoint because p_3 and p_4 already meet in L_C. Hence |O| = 15 − 8 = 7.
- Recomputed indicator values: e_0 1−0−0, u 3−1−1, u' 3−1−1, u'' 2−0−1, v 3−1−1, v' 2−1−0, v'' 1−0−0. Every result is 1.

Each later use of the bijection (`:232`, `:237-240`, `:254`, `:256`) compares O triples already shown to be distinct.

**Column-4 contradiction (`:252-264`).**
1. Under Q1, column 4 consists of Q_4, two occupancy-2 triples and three occupancy-1 triples.
2. tau_1 is forced because every b_k lies in Q_4.
3. Let tau_2 be p_j's column-4 block. It is an occupancy-1 triple (j ≠ 4; `:140`). It differs from tau_1, which is full. It contains neither p_3 (in tau_1) nor p_4 (in Q_4), so it is in O and carries one of {e_0, v, w_4}.
   - It cannot carry e_0, because e_0's unique O triple contains p_i, and p_i is in tau_1.
   - It cannot carry w_4, which is in tau_1.
   - So tau_2 carries v.
4. tau_3 contains none of p_3, p_4, p_i, p_j. It is therefore an O triple outside the five through p_i or p_j, which carry {e_0,u,u',u'',v}. So tau_3 carries v' or v''.
5. g's column-4 triple has occupancy 2 (`:112`). By (G) it is either {g,e_0,v'} or {g,v,v''}. v ∈ tau_2 rules out the second, so it is {g,e_0,v'}, and tau_3 carries v''.
6. The last occupancy-2 triple must then take {u,u',u''}∖{w_4}. Both rows lie in H_C, so they would agree a second time.

The argument is uniform in w_4, in the (G) order and in the choice of i/j. A side check, not used by the proof: {p_i,p_j,e_0} is forced into column 0, and nothing in the proof contradicts this.

**Retained choices.**
- Both orders of {i,j} = {1,2} survive to `:266`. The leftover transposition (1 2) is never used.
- w_4 is carried symbolically through (6) and `:262`.
- The (G) order across columns 3 and 4 is decided at `:258`, not assumed.
- c_j is derived at `:232`, not chosen.
- Never fixed and never needed: the column of {p_i,p_j,e_0}; which particular triple holds an empty row beyond the forced cases (`:144` is fc48075b-compliant); the nonempty members of H_A, H_B and the C-pair; any a_k/b_k placement.
- The labels u, u', u'', v, v', v'' are definite descriptions, so the "permute E" allowance is never invoked.

**Symmetries.**
- `:108` reads A, B, C off each array. This is a definition, not a reduction.
- `:122`, σ ∈ Sym{0,1,2}: maps Q_k to Q_σ(k), fixes Q_3 and Q_4, and fixes g, p_3, p_4, E and the P1 columns. It therefore preserves A/B/C, H_C and L_C.
- `:148-153`, (3 4)(A B) with a_k↔b_k and p_3↔p_4: swaps Q_3↔Q_4 and the two g-pairs, and fixes H_C, L_C, p_0 and E. It commutes with the σ normalisation.
- Both symmetries lie in Aut(type list) = Sym{0,1,2} × Sym{3,4}, which has order 12. That matches V's `aut: 12`, which I did not rely on. Both are permitted by `scope-v1.md:17`.

**Erratum a53cc298.** With the Petersen item withdrawn, the proof needs exactly two four-row matching facts, and both are proved inline:
- `:155`: any 2+2 split of a 4-set joins two of any three specified rows.
- `:179`: explicit listing of the three perfect matchings of {e_0,v,v',v''}.

No step uses a Petersen, girth or AT2 fact.

## 3. MINOR findings and minimal repairs

1. **`proof-v1.md:122`.** The S3 step does not state the full induced map that `scope-v1.md:17` requires.
   - Repair: "σ sends P0 column k to σ(k) and a_k, b_k, p_k to a_σ(k), b_σ(k), p_σ(k); it fixes g, p_3, p_4, every empty row, columns 3 and 4 and every P1 column; Q_k maps to Q_σ(k), so A/B/C, H_C and L_C are preserved."
   - The same repair applies to `bindings-and-import-map-v1.md:64`.
2. **`proof-v1.md:148-153`, together with `:130-134`.** The swap is invoked after i and j were named. It exchanges H_A↔H_B and L_A↔L_B, and hence i↔j. That it fixes E is left implicit.
   - Repair: "The map fixes E and sends the normalised class to itself; §2 holds for the image with i, j re-read from it (equivalently, apply it before §2.3). Both orders remain."
   - The same repair applies to `bindings-and-import-map-v1.md:65`.
3. **`proof-v1.md:10,20` (binding wording).** The hypothesis fixes the size-4 class, while the encoder (`source-E-membership-v1.txt:23`) and the scope at `:14` fix the symbol-0 class. Line 20 calls the class "exact".
   - The needed direction holds: |Q_c| = 4 and the profile has a single 4. So every array with the encoder semantics lies in the theorem's class.
   - Repair: replace "exact class" with "contains every b65 encoder-semantics array (equal up to per-column symbol renaming and P1 column order)".
4. **`proof-v1.md:108,270` against `scope-v1.md:17`.** Line 270 lists "P1 column naming" as a normalisation, but the scope permits no free P1 permutation. It is in fact a definition, so nothing illegitimate happens.
   - Repair: "A, B, C are defined from each array; the only symmetry reductions are σ and (3 4)(A B)."

Uncounted nits:
- `:86` uses triple capacity (occupancy ≤ 3) without saying so.
- `:179`'s "In particular" should cite `:112` and `:155` rather than the preceding sentence.
- `:204` could cite `:146` for the fact that the C-triple empties are exactly V.

## 4. Scope of this verdict

- **Theorem correctness:** PASS (0/0/4). Applying the repairs changes no implication.
- **Source binding (only what the packet itself allows me to check):**
  - Consistent:
    - The S excerpt, `proof-v1.md:22`, theorem item 4 and V's `skeleton_types`/`skeleton_empty` all have identical content.
    - The header gives 5× (4,3,3,3,3,3), 3× (4,4,3,3,3,2) and c0 = 5.
    - The encoder excerpt gives all five degrees as 3, hence one p_c per index, 7 empty rows, and symbol-0 class = Q_c.
    - By hand count, the displayed entry is 82 bytes (= 4503 − 4421) and the header is 433 bytes, assuming no trailing LF.
    - The excerpt line counts and the scope's line anchors (4789; 4958-4961) agree.
  - **Not verified** (this needs byte or hash reads, which the brief excludes):
    - every SHA256 value
    - that the excerpts sit at the stated offsets
    - that this is S's zero-based entry 65
    - that V's entry sits under the ms09 key (the excerpt shows only the tag and path strings)
    - the encoder's profile and agreement clauses, and its caller
  - These affect which ledger item gets closed, not whether the theorem is true.
- **Status:** This is still a candidate. The review changes no ledger or count. The v10 counts (70/59/129) remain the parent's pre-result snapshot, and the both-family gate still applies.
- **Runtime admission:** Not addressed. The global HOLD and all UNKNOWN/STOP markers are unchanged.
- **Novelty:** Not assessed, and none is claimed. PA(19,8,6) remains UNDECIDED.
