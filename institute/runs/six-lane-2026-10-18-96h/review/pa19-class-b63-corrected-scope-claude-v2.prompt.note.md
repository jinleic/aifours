# Second-family review: PA19 ms09 class extension and b63 reduction

**Governing, read first.** Parent erratum v2 controls this review, and erratum v1 still applies in full. In particular:
- The 59 rows and the total of 129 refer to frozen v10. Current v11 has 70 + 58 = 128.
- H1/H2 covers only b65 among the 59 rows and adds no count.
- "Corroboration" for b59 has shared provenance. It does not imply an independent author, independent discovery, a closure or any gain.
- There is no duplicate b65 credit.
- The opaque 59-case check binds hashes and literal V case IDs only.
- The theorem is mathematical. It says nothing about whether S or V is complete.
- b63 stays PARTIAL, and the original fallback stays UNFULFILLED.
- The three procedural/delivery MAJORs are permanent.

**Method.** I worked from the text only: no tool calls, code, enumeration, tests or assertions. I re-derived every step by hand. I did not recompute any SHA256, and cannot.

## Verdict

| Claim level | Verdict | Math FATAL/MAJOR/MINOR | Non-mathematical |
|---|---|---|---|
| (a) Class theorem: H1∧H2 ⇒ no array | **PASS as written** | 0/0/0 | 1 MINOR binding (LF13); LF151 wording governed by v2; 1 nit |
| (b) The 59 applicability decisions | **PASS** | 0/0/0 | 1 MINOR binding (LF3); hash and completeness limits as stated in v2 |
| (c) b63 B1–B9 and the six families | **PASS as a necessary reduction only; b63 NOT excluded** | 0/0/2 | 2 nits |
| Procedure and delivery | **3 MAJOR, permanent** | — | — |

**Whole-case gain: none.**

## (a) `class-theorem-v1.md`

**Section 1, general facts (all verified)**
- **§1.1 (LF28):** 5·21 + 3·22 = 171 = C(19,2), so every pair of rows agrees exactly once. Rows sharing a P0 triple are T-disjoint: a common index d ≠ c would give a second agreement in Q_d.
- **§1.2 (LF31):** n4 − n2 = 2 − t, and all nine row patterns are correct.
- **§1.3 (LF34–44):** The minimum costs are 2 per P0 column, 10 for the P1 quads and 0 for the P1 triples, so the excess is 1. The m_j analysis and the identity Σd = 2, cost = 9 + ½Σd² give exactly the five categories C3, C0, Q4, Q1 and T2.
- **§1.4 (LF47–53):** I(r) = 7 holds. For L1, outside the rescue blocks I ≥ 4 + 4. L2 holds. L3 is tight at 2 + 2 + 3.

**Section 2, Steps A–G (LF57–85): all hold**
- Two privates of the same type cannot share the rescue block.
- C0 is impossible because p3 and p4 would meet both in R* and in L_C.
- The Step F count gives 2 + m = 4. That forces 5 privates, Σdeg = 15, n = 7, and six 2-types of the form {k,w}. This is b65 up to relabelling, with every degree equal to 3.

**Symmetries (all valid)**
- Relabelling P is allowed.
- S₃ on {0,1,2} preserves both the list and the normal form.
- The map 3↔4, a↔b, p3↔p4, A↔B swaps L_A↔L_B and H_A↔H_B, fixes H_C, L_C, U_E and e0, and swaps i↔j. Both values of i are retained.

**Section 3 (LF91–114): verified**
- The A-quad count is 3 + 1 + x = 5, so x = 1.
- u ∉ L_A, by pigeonhole on g's two occupancy-2 triples.
- The table is consistent: occupancies 3, 2, 3, 2, 3, 1; each empty row lies in exactly two quads; the quad graph is simple.
- There are 11 pairs that agree in P1, so M has exactly the 10 listed edges.
- The unique perfect matching is {e0v′, vv″}.

**Section 4 (LF118–147): verified**
- deg_M = (4,2,2,3,2,3,4) and f = (1,3,3,2,3,2,1), with Σf = 15.
- The S-sets are correct, and all seven O-counts equal 1.
- τ₁ is correct and w4 ∈ {u, u′}.
- The triple {p_i, p_j, e0} is forced, c_j = v′, and w3 = w̄4.
- In column 4: τ₂ carries v, g's triple is {g, e0, v′}, and τ₃ carries v″. The remaining occupancy-2 triple then lies inside U_E ⊂ H_C, which is a contradiction. This holds for both values of i.

**Observation (not a defect).** After Section 2 the class adds nothing beyond b65 up to relabelling. Every other H-list is refuted inside §§1–2; for example, b59 fails at E3.

**Findings**
- **MINOR (binding, not mathematical)** at `class-theorem-v1.md:13`: "This is exactly the ms09 skeleton semantics."
  - The pinned E lines 3–8 and 77–99 show only three things: the row order, the P0 symbol-0 memberships Q_c, and the profile list.
  - They do not show the at-most-one-agreement constraint or the symbol-cardinality constraints.
  - `interface-map-v1.md:16` states the narrower, correct scope.
  - Repair (by erratum): align LF13 with that line, and mark the definition-to-encoder bridge as parent metadata that is not part of the theorem.
- **MINOR (wording), already repaired by parent v2; I concur** at `class-theorem-v1.md:151`: "independent corroboration."
  - b59 has types {012, 034, 13, 14, 23, 24} with e = 7, degrees (2,3,3,3,3) and six privates, so 6 + 6 + 7 = 19.
  - b59 satisfies H and is refuted at E3. That is corroboration only.
- **nit** at `class-theorem-v1.md:151`: "the list is exactly b65's" should read "b65's up to a permutation of P." The parenthetical list of contradiction types is illustrative, not exhaustive; for example, a 2-type meeting g twice is ruled out by §1.1.

## (b) `case-table-v1.md` and metadata

**Checked by hand against the embedded S text**
- All 59 quoted entries at `entry-range-hash-metadata-v1.txt:4-62` match the S entries at those indices.
- **Byte ranges:** I recomputed all 71 entry lengths using 23 + 3·Σ|type| + 2·#types, with a 433-byte header and 2-byte separators. All 59 ranges match. Entry 70 ends at byte 4975, and the closing `]}` brings the total to 4977, the stated file size.
- **e values:** all match S. H1 fails for exactly 55 cases, with e between 1 and 6.
- **The four e = 7 cases:**
  - b63 fails H2, because {3,4} is listed.
  - b66 and b68 fail H2, because they have no 3-type.
  - b65 satisfies H.
  - So "H covers no further undecided case" is correct.
- **V line numbers:** all 59 equal the lines in `v10-binding-lines-v1.txt:4-121`.
- **Selection rule (`scope-v1.md:20`): applied correctly; it selects b63.**
  - b63 has Δ = 2. Δ is even for two 7-type lists, and Δ = 0 is excluded because the degree sequences differ: (2,3,3,3,4) against all 3s.
  - b66 and b68 have Δ = 3: 1 for g plus at least 2 extra 2-types. The bound is attained because each contains a K₃,₂.

**Binding limits (not mathematical; consistent with v1 §6 and v2)**
- I verified no SHA256 values.
- The line excerpt proves that the 59 IDs are members of the list. It does not prove the list contains no others.

**Findings**
- **MINOR (binding)** at `case-table-v1.md:3`: "The e value read from S equals each V entry `skeleton_empty`."
  - The packet embeds no `skeleton_empty` lines, so this cannot be checked.
  - Repair: embed those 59 lines, or mark the sentence as unverified.
- `case-table-v1.md:69` ("independent corroboration") is governed by v2, as in (a).

## (c) `b63-reduction-v1.md` and the worker's clock erratum

**Verified**
- **Case data (LF8):**
  - Degrees are (2,3,3,3,4). The privates are p0, p0′, p1, p2 and p3, with no p4, so 7 + 5 + 7 = 19. The quads are correct.
  - The list's automorphism group under relabelling P is exactly {id, 1↔2}. Indices 0 and 4 are fixed by degree. g is the only 3-type, which fixes {1,2} and therefore 3. So the stated symmetries are complete and used correctly.
- **B1 and B2.**
  - G1 gives category T2, the pair {g,z}, and τ′ = {g, p3, ε}.
  - G2 gives the pairs {g,p3} and {g,z}, with category C0 or Q1.
- **B3.**
  - On {04, 13, 14, 23, 24}, the T-disjointness graph is the path 24–13–04–23–14.
  - Its 2-matchings are exactly the three listed, and 1↔2 swaps the last two.
  - The tightness argument for p3 is correct.
- **B4 and B5.**
  - c* ≠ 3, and eps(L_B) = eps(L_C) = 2.
  - For c* = 0, 1 and 4, the R* lists are exactly the T-disjoint pairs that avoid both c* and 3. The c* = 2 list is the 1↔2 image.
- **B6, B7 and B8.**
  - Each C-triple has occupancy 1.
  - The C-pair consists of two 2-types.
  - r1 and r2 are privates of different types.
  - The occupancy bounds for s1 and s2 are tight.
  - {K_B, K_z, K′_A} have occupancies {3,3,2}.
- **B9.**
  - The only nonempty row in K′_A must be a C-pair row, because the s-quads have occupancy 2.
  - [e0 ∈ A] + #U_A = 3. With B8, this gives e0 ∈ A and #U_A = 2.
  - f(e0) = 1, which forces the triple {s1, s2, e0}. Then y ∈ K_B and e0 ∈ K_z, and x's B-triple contains e0.
  - Up to swapping vb↔vc, the table is K_z = {z, e0, u1, va}, K′_A = {x, u2, vb, vc}, and B-quads {va, vb} and {vc, u3}.
  - g's triples are {g, e0, vb} and {g, va, vc}, the only admissible split.
  - If L_B contains {va, vb}, then f(u3) = 2. p3, z, x and s_L must all meet u3 in those two triples, which forces {p3, x, u3} and {s_L, z, u3}, with x ∈ {04, 14, 24}.
- **§2 case tree:**

  | Family | Branch |
  |---|---|
  | 1–2 | G1 |
  | 3 | G2-C0 |
  | 4 | G2-Q1-(a), K_B = 2 |
  | 5 | G2-Q1-(a), K_B = 3: either e0 ∈ A with one U row in A, or e0 ∈ K_B with two |
  | 6 | G2-Q1-(b) |

  The six families are exhaustive as **necessary** families. None is excluded and none is realized, so this list supports no nonexistence claim.

**Findings**
- **MINOR (confirmed; repaired by parent v1 §1)** at `b63-reduction-v1.md:34`: "p3's partner" should read "p3." g is in the B-pair, not in a B-quad.
- **MINOR (new; a gap in justification, but the conclusion holds)** at `b63-reduction-v1.md:34`: "z and x have all P0 triples of occupancy 1 (… their other P1 triple occupancy 1)."
  - At that point, the occupancy of x's B-triple has not been established.
  - I(x) = 7 alone would also allow a B-triple of occupancy 0 with P0 occupancies (2,1,1).
  - Repair: "Since eps(L_B) = eps(K_B) = 2, the three B-triples carry 3 empties, at most one each in Q1, so each carries exactly one."
- **nit** at `b63-reduction-v1.md:34`: f(w) = eps(Q_w) + eps(Q′_w) − 3 equals 4.1's 5 − deg_M(w), because deg_M(w) = 8 − eps(Q_w) − eps(Q′_w). Say so in the text.
- **nit** at `b63-reduction-v1.md:38`: families 1–2 should state that both assignments of the pairs to columns B and C are covered. Family 1's two assignments are equivalent under 1↔2; family 2's are not.

## Procedural and delivery findings: 3 MAJOR, permanent, independently confirmed

1. **Derivation before the freeze.**
   - `scope-v1.md:3` says the freeze came "before any written derivation in this directory." The transition rule is stronger: "Freeze scope + exposure BEFORE derivation."
   - `scope-v1.md:24` shows that the class-reduction sketch, the full applicability screening, the byte-range work and the metric ties all came before the freeze. So the selection rule was frozen with its outcome already known.
   - Disclosure does not cure this. It is not preregistration.
2. **Estimated timestamp.**
   - The time "18:03:00" at `b63-reduction-v1.md:3` was not read from `/bin/date`.
   - It is later than the worker erratum's 17:49:54 and the interface map's 17:50:45, so it cannot be an observed clock reading. The observed window is 17:43:22–17:49:11.
   - The violation stands.
3. **Unmet fallback.**
   - Once H covered no further case, the transition required a complete written exclusion of the nearest case. `b63-reduction-v1.md:36-43` delivers only a partial reduction, so the target is UNFULFILLED.
   - Later results F4/F5 (parent metadata, which I did not review) leave families 1, 2, 3 and 6 open. They do not redefine the target.

## Count and gain

No whole-case gain follows.
- Among the v10 cases, the theorem covers only b65. b65 is already excluded separately in v11, so there is no duplicate credit.
- b59 was already closed, so the theorem only corroborates it.
- b63, b66 and b68 remain open as whole cases.
- The current count stays at 128 (70 ms06 + 58 ms09), and PA(19,8,6) remains UNDECIDED.
- No novelty, human, Lean or runtime claim is made.

**Governing, read last.** Erratum v2 and erratum v1 still control. The mathematical PASS on (a)–(c) does not upgrade b63 beyond PARTIAL. It does not fulfil the original fallback, does not erase the three MAJORs, and grants no count credit.
