# PA19 ms09 e7 dossier: second-family written review

**Method.** I re-derived everything by hand from the packet text, against the original quantifier: all 19×8 arrays over six symbols, with exact ms09 profiles, fixed skeleton quads, and at most one agreement per row pair.
- No files were read, hashed, executed or enumerated. SHA256 values and offsets are unverified.
- The first-family approval and parent erratum v1's acceptance were not used as evidence.
- Dossier paths are relative to `information-science/evidence/six-lane-20261018-96h/pa19/continuations/ms09-e7-excess/`.

### Status (both errata applied)
- **Counts.** V9 = 132 and V10 = 129 are historical snapshots. Current parent V11 is 70 ms06 + 58 ms09 = **128**.
- **Cases.** The definitions of b63, b65, b66 and b68 are unchanged.
  - b65 was closed by a separate later full proof.
  - b63 has separate later F4/F5 exclusions, with families 1/2/3/6 still open.
  - Erratum v2 records no change for b66 or b68.
- **Premises.** Per erratum v2, neither later result is a premise of this dossier's proofs.
- **Credit.** This dossier gives zero whole-case closures and zero count credit. Its "all four (current) cases remain undecided" sentences are dated packet status, not the current frontier.

### Verdict: FATAL 0 · MAJOR 0 · MINOR 8
- m1–m3 independently confirm parent erratum v1 items #1–#3. m4–m8 are new.
- Every lemma holds as a necessary implication under the full quantifier.
- Only L23 excludes anything, and it excludes a single displayed P1 projection.
- Nothing here is a whole-case exclusion, an extension or a realizability claim. That matches the dossier's own labels.

### Per-lemma verdicts

**imports-v1.md**

| Lemma | Lines | Kind | Verdict | Independent check |
|---|---|---|---|---|
| L1 exactness and block facts | 6–8 | necessary | VALID | 5·21 + 3·22 = 171 = C(19,2). If two rows share an index d, they already agree in column d. So non-quad blocks are T-disjoint, and each quad hits distinct blocks in every other column. |
| L2 row patterns | 10–15 | necessary | VALID for t ≤ 3 | Follows from 2n4 + n3 = 5 − t with n2 + n3 + n4 = 3. See m8. |
| L3 occupancy, five categories | 18–32 | necessary (counts only) | VALID | Solved the a_i system directly. Quad pair-count 10 gives only (3,3,2,2,2,2); 11 gives only (4,2,2,2,2,2) or (3,3,3,2,2,1). P0 columns: (2,2,1,1,1), or exceptional (3,1,1,1,1) / (2,2,2,1,0). P1 triples: a single 2. |
| L4 I(r) = 7 | 35 | necessary | VALID | |
| L5 R1 | 37 | necessary | VALID | Equality also forces: in C0, the other P0 triples have eps 1 and both quads eps 2; in Q1, all P0 triples eps 1 and the other quad eps 2. |
| L6 R2 | 39 | necessary | VALID | Any P0 triple containing a nonempty row has eps ≤ 2 in every category. |
| L7 R3 | 41 | necessary | VALID | |
| L8 R4 | 43 | necessary | VALID | The two partners must also have distinct types (see m7). |

**reductions-v1.md**

| Lemma | Lines | Kind | Verdict | Independent check |
|---|---|---|---|---|
| L9 AT2 | 6–14 | necessary, any ms09 and any e | VALID | The disjointness graph on 2-subsets of 5 indices is the Petersen graph, girth 5. A 5-vertex induced subgraph has ≤ 5 edges (≤ 4 if it has a degree-3 vertex). Five rows in three triples, at most two per triple, give exactly 2 agreements per column. That needs 6 distinct edges, but at most 5 exist. |
| L10 AT2 equality case | 16 | necessary | VALID | Four vertices with girth 5 allow at most 3 edges, so the graph is a spanning tree (path or star). Each column uses one edge with distribution (2,1,1); those pairs never agree again. |
| L11 b65 forces Q1, L_C = {p0,p3,p4,e} | 19–25 | necessary | VALID | L_C is the only block containing both p3 and p4. C0 would make them agree twice. The third row's type lies in {0,1,2} and it is not g. Permuting {0,1,2} normalises it to p0. |
| L12 A/B quad eps (3,2), four extra positions | 27 | necessary | VALID | Pattern totals reconcile (Σn2 = 6, Σn4 = 24, Σn3 = 27). Bookkeeping not written out (m6). |
| L13 two C-pair orbits | 29–32 | necessary | VALID, see m2 | Under ⟨1↔2, (3↔4)(A↔B)⟩ the orbits are {a0b1, a0b2, a1b0, a2b0} and {a1b2, a2b1}. |
| L14 U paths | 34 | necessary | VALID | Orbit I edges: a1b0, a1b2, a2b0. Orbit II edges: a0b1, a2b0, a2b1. |
| L15 C-column branches | 36–38 | necessary, exhaustive | VALID | Each C-triple holds exactly one empty. AT2 equality allows only one U-edge in C, so p1 and p2 sit in different triples. Orbit I's middle edge fails because a2 and b2 both contain index 2. Six branches are listed; five are distinct up to symmetry (O1). |
| L16 b63 G1 | 45–49 | necessary | VALID | Path checked. The unmatched vertex is at position 1, 3 or 5, and 1↔2 identifies {2,4} with {1,4}. g's other triple must be {g, p3, e}, since z there would agree with g twice. |
| L17 b63 G2 | 51 | necessary | VALID | z is not in L_C because it shares index 3 with p3. A C-pair of two private rows is also excluded by R1 alone. |
| L18 b66/b68: l ≤ 2 | 56–60 | necessary | VALID | |

**rainbow-and-completion-v1.md**

| Lemma | Lines | Kind | Verdict | Independent check |
|---|---|---|---|---|
| L19 empty incidence graph | 6 | necessary | VALID, see m1 | |
| L20 matching test | 8 | necessary (conditional) | VALID | |
| L21 b65 high/low quads, zero triple | 11–23 | necessary | VALID | p1 or p2 in a high quad gives I ≥ 3 + 1 + 4 = 8. e0 is not in L_A or L_B. A-quad empties count 5 = 3 + 1 + 1, which isolates u. u in L_A breaks g's matching. Renaming A/B is harmless because every step is A/B-symmetric. |
| L22 P0 capacity, columns 3/4 | 26 | necessary | VALID | A sharpening is noted in O2. |
| L23 displayed branch | 28–36 | exclusion of one P1 projection, all empty fillings | VALID | p0 meets a0 in Q0, a1 in A, a2 in B and p3 in C. The example is redundant; see m5. |
| L24 completion criterion | 48 | equivalence | VALID | Distinct symbols per block yield an array, and every array yields its block system. |

**p0-capacity-v1.md**

| Lemma | Lines | Kind | Verdict | Independent check |
|---|---|---|---|---|
| L25 count projections | 7–11 | necessary | VALID | Nonempty count = 3 − eps. |
| L26 b66/b68 private-row constraints | 13 | necessary | VALID | Only 4 (P0) or 5 (P1) indices are available. |
| L27 T2 sole member | 15 | necessary | VALID | |
| L28 rainbow condition | 17 | necessary | VALID | |

**bindings-v1.md and excerpts**

| Lemma | Lines | Kind | Verdict |
|---|---|---|---|
| L29 case bridge | 6–36 | definition | VALID; hashes unverified |

What I could check by hand for L29:
- The header string counts to exactly 433 bytes.
- The four case excerpts are 82, 82, 87 and 87 bytes, matching their half-open ranges.
- The V9 records span 48, 48, 51 and 51 lines, matching their JSON layout.
- The gaps between records also fit: the S byte gaps (83, 94) and V line gaps (47, 52) are consistent with a seven-two-type b64 and a t3-plus-seven-two-type b67.
- V9 `skeleton_types` equal the S excerpts.
- Degrees, private rows and the 19-row totals recompute correctly.
- Q_c = {r : c ∈ member[r]} matches encoder lines 77–99.
- Note only: the tags s00050/s00052 differ from b-index 63/65, while s00066/s00068 match 66/68. Case identity rests on the type lists being equal, and they are.

### MINOR findings and minimal repairs

**m1.** `rainbow-and-completion-v1.md:6` (confirms erratum v1 #1).
- **Issue:** an empty edge determines only the P1 *column* of that row's triple, not which triple.
- **Downstream:** nothing relies on the stronger reading. Lines 17 and 21 get triple membership from quad counts and row patterns instead.
- **Repair:** use the erratum v1 #1 wording.

**m2.** `bindings-v1.md:36` and `reductions-v1.md:29,49` (confirms erratum v1 #2).
- **Issue:** the symmetry ledger omits two automorphisms the proofs use:
  - b65: (3↔4)(A↔B), i.e. a_i↔b_i and p3↔p4.
  - b63: 1↔2, i.e. p1↔p2, {1,3}↔{2,3}, {1,4}↔{2,4}.
- **Check:** both preserve the skeleton, the profiles and the normal forms in use.
- **Wording:** reductions:29's "3<->4, and swap A/B" must mean the joint map. Neither half alone preserves the normal form.
- **Repair:** erratum v1 #2, plus the word "jointly".

**m3.** Status sentences (confirms erratum v1 #3 and erratum v2).
- **Locations:** `scope-v1.md:7` ("CURRENT … v9"), `bindings-v1.md:7` ("current snapshot"), `rainbow-and-completion-v1.md:50`, the manifest `status` field, the `current_*` excerpt roles, and the packet preamble's "remain unresolved".
- **Repair:** read all of these as dated packet status. The current frontier is V11 = 128. No count credit.

**m4.** The symbol U means two different things.
- **Issue:** in `reductions-v1.md:25,34,36–38`, U is the four all-triple two-types. In `rainbow-and-completion-v1.md:11,17,19`, U is the three empties of H_C. Each file is internally consistent, but reading them together invites mistakes.
- **Repair:** rename the second one, e.g. W := H_C ∩ E.

**m5.** The displayed example (`rainbow-and-completion-v1.md:32–36`, credited at :50) is already excluded by incidence counting.
- **Issue:**
  - In the table, p1 sits in L_A (eps 2), the C-triple {23, p1} and the B-triple {24, p1}. Each of those triples has two nonempty rows, so eps 1.
  - Q1 makes every P0 column (2,2,1,1,1), so each of p1's four P0 triples has eps ≥ 1.
  - That gives I(p1) ≥ 4 + 2 + 1 + 1 = 8 before any P0 argument.
- **Root cause:** a consequence of :13 plus reductions:36 is never drawn (the same step the dossier does for p3/p4 at reductions:27). For each of p1 and p2, I = 7 forces:
  - its non-C triple to have eps 0, so it is that column's unique eps-0 triple;
  - all four of its P0 triples to have eps 1.
- **Effect:** the exclusion is still correct, but the example doesn't show the P0 filter catching anything the counts miss.
- **Repair:** state the p1/p2 equality next to :13 and mark the example "also excluded by I(p1) = 8", or replace it with a projection that satisfies every stated I-equality.

**m6.** Two correct steps are not written out.
- `reductions-v1.md:27`: why the four extra A/B quad positions are exactly p1, p2, x, y.
  - p0 is unpaired, so its pattern is (0,2,1) and its only quad is L_C.
  - All-triple rows have no quads, and g's only quad is H_C.
  - p3 and p4 sit in L_B and L_A, and both C-quads are full.
- `rainbow-and-completion-v1.md:23`: why the eps-0 triple is unique.
  - A and B each hold 5 empties in quads and none in their pair.
  - That leaves 2 empties across three triples at ≤ 1 each, so exactly one triple has eps 0.
- **Repair:** add one sentence for each.

**m7.** Wording and a sharpening.
- `reductions-v1.md:16`: "contain either endpoint … together" should read "no other block contains both endpoints of one of those edges".
- `imports-v1.md:43` (R4): add "of distinct types". Both partners lie in the rescue block, so they cannot share a quad. This is automatic for b65.

**m8.** Scope labels.
- `imports-v1.md:11–14` lists row patterns only for t ≤ 3. That covers these four cases, but general ms09 allows up to t = 5, adding (2,1,0) for t = 4 and (3,0,0) for t = 5.
- The pair count 21 and excess 1 (`imports-v1.md:18–20`) and "eight nonempty / seven empty" (`p0-capacity-v1.md:5`) hold only for e = 7.
- By contrast, AT2 and its equality case, the empty-row pattern and the empty-graph construction hold for all ms09.
- **Repair:** label the scope of each statement.

### Observations (no credit; no verdict changes)
- **O1: orbit II has a leftover symmetry.**
  - σ = (1↔2)(3↔4)(A↔B) fixes the pair {a1, b2} and preserves the normal form.
  - It maps branch (b0–a2; p1–a0, p2–b1) onto branch (b1–a0; p2–b0, p1–a2), and fixes both middle-edge bijections.
  - Orbit I's representative has trivial stabilizer, so the six branches at reductions:37–38 reduce to five. The list remains exhaustive.
- **O2: the P0 capacity lemma at :26 sharpens.**
  - In column 4, g's triple has eps 2, so the other four triples have eps (2,1,1,1) and contain one Q3 row each.
  - So p0, p1 and p2 go into the triples of three distinct Q3 rows, avoiding p_i–a_i and any earlier agreements.
  - Column 3 works the same way with Q4.

### Disposition
- Record the six files as candidate written necessary implications, with m1–m8 as overlay text; the source files stay unchanged.
- This dossier closes no case and shows no case feasible or infeasible. The later b65/b63 results do not retroactively upgrade it.
- This review is not count evidence, and makes no novelty, formal-verification or human-verification claim.
