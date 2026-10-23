# K3 encoder instantiation (H3, Link 7): written proof r1 (phys-2, lane moqls7-maximum)

Written 2026-10-18 from 07:18 PDT (host clock) at the parent's request. This is a static source reading for the
parent composition review (AMENDMENT-4 disposition decision 8; AMENDMENT-4.r4 §1 H3 and §8; K3-COMPOSITION.r3
Link 7). Frozen by `cp -n` from `review/drafts/K3-H3-INSTANTIATION.r1.md` and never rewritten.

**No claim.** This note proves a lemma about the pinned encoder sources. It accepts no certificate, changes no
status and makes no statement about K3 or M(7). Nothing was executed to write it.

Paths: `L/` = `physics/evidence/six-lane-20261016/moqls7-maximum/`; `R/` = `institute/runs/six-lane-2026-10-16/review/`.
Line numbers refer to the pinned files below.

## 0. Bindings

| File | SHA-256 |
|---|---|
| `L/code/gram_enc.py` (encoder A) | b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833 |
| `L/code/gram_encB.py` (encoder B) | c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45 |
| `L/code/k3_cubes.py` (cube and G6 block) | 70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550 |
| `L/code/k3_lex.py` (lex block, A route) | 2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10 |
| `L/review/GRAM-ENCODING.r2.md` (Gram-G1…G5, G4) | c6c506a7d1ecba15b2e31393b0da4caa248db5c9227f512c0df9ea5bd07ad6c7 |
| `L/review/LEMMAS.md` (C0, Lemma 10, G4) | 4bddc9d422cf989bb9bfdf4f09de72742ea2d423b9a082f8fd76263ba1c850c9 |
| `L/review/G6-G2-DERIVATION.r1.md` | 8790e9e1af45d4b49e397a06fc4b8dbd70742278698c55561e03f0904f07e791 |
| `L/review/AMENDMENT-4.r4.md` | 75ac7aece0f050160bf147be91eec906ab99e68294bf9f70feb453b9bcbd9a91 |
| `L/review/K3-COMPOSITION.r3.md` | b85daed48b15ebcc69ea2c8cdd54899911ce8565f9ceebe67a36cbdb01726aed |
| `L/evidence/k3cubes/bmap_oracle_r1.json` | 6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c |

Static audits already covering this ground: Codex `R/moqls7-k3-composition-r1-codex-v1.note.md` (5a68a20d…47bf,
Link 7 ACCEPT-WITH-FIXES) and Claude `R/moqls7-k3-composition-r2-claude-v1.note.md` (786f3438…78e1, Link 7
ACCEPT-WITH-FIXES, m7/m8). This note writes their per-family reasoning out as one proof, with the fixes applied.

## 1. Statement

**Lemma H3.** Let (Ψ1, Ψ2, Ψ3) be a K3 triple of mutually orthogonal QLS(7) in which every square is heavy on each
of its 14 own row/column lines (Link 3). Suppose it is normalised by `--sym` (Link 5) and then, by the residual
normalisation of Link 6, into one canonical cube C ∈ {C311, C321, C411}. For non-collinear cells p ≠ q set
g_a(p, q) := [⟨ψ_{a,p}, ψ_{a,q}⟩ ≠ 0]. Then:

1. There are values of the auxiliary variables of encoder A such that every clause of the base CNF
   `gram_enc.build(3, None, True, True, None)` holds (§3).
2. There are values of the auxiliary variables of encoder B such that every clause of the base CNF of
   `gram_encB.py --squares 3 --heavy --sym` holds (§4).
3. Every clause of the cube block `k3_cubes.cube_clauses(vmap, C)` holds: the 18 signed units and the G6 equalities
   (§5).
4. For C = C311 on the A route, let X* be the lexicographically least Gram pattern in the H_311-orbit of the
   configuration's pattern. X* is the Gram pattern of a K3 triple normalised into C311, so items 1 and 3 apply to it.
   With prefix auxiliaries set to "equal so far", it also satisfies the AMENDMENT-3 lex block of `k3_lex` (§6).
5. Under G1–G2 (and Links 3 and 7), the cut block holds for the configuration and for X* (§7; Link 10).

Hence every K3 triple, so normalised, satisfies the cube input (base ∧ cube ∧ G6) of its cube under both encoders,
and for C311 it also satisfies the strengthened A lex input (through X*) and the strengthened B input.

## 2. Common facts

- **F1 (variables).** With L absent, the ONB lines are the 7 rows and 7 columns (`gram_enc.py:55`, no symbol lines
  since L is None; `gram_encB.py:101-104` without `--net-L`, collinear pairs at 105–110). Both encoders create a g
  variable exactly for each square and each unordered non-collinear pair (`gram_enc.py:58-71`;
  `gram_encB.py:113-118`): 3 · 882 = 2646 variables. A collinear pair has no variable; the code treats it as the
  constant false (`gram_enc.py:72-73`, `gram_encB.py:120-123`). That is Gram-G1: distinct cells on a common ONB line
  are orthogonal.
- **F2 (shared order).** Both allocate the g variables first, in the order square, earlier cell, later cell (cells
  row-major), skipping collinear pairs. This is also `k3_cubes.variable_map()` (`k3_cubes.py:58-68`). For A it is
  asserted at run time (`k3_cubes.py:112-115`); for B it is established by the runtime oracle (0 of 2646 variables
  differ; K3-ERRATA E1).
- **F3 (production-domain sizes; Claude m7).** Let ℓ be an own line and p ∉ ℓ. Exactly one cell of ℓ is collinear
  with p (the cell of ℓ in p's column if ℓ is a row, in p's row if ℓ is a column). So p has exactly 6 possible
  neighbours on ℓ. Consequently:
  - for two cells p, q ∉ ℓ, the possible common neighbours on ℓ number 6 (same excluded cell) or 5;
  - for distinct lines ℓ1, ℓ2 and r ∈ ℓ1 ∖ ℓ2, the possible neighbours of r in ℓ2 ∖ ℓ1 number exactly 6 (if the
    lines meet in s, then s ∈ ℓ1 is collinear with r and is excluded anyway; otherwise one cell of ℓ2 is collinear
    with r);
  - every own line has 42 off-line points, each with 6 possible neighbours.
  This agrees with `GRAM-ENCODING.r2.md` lines 141–147.
- **F4 (images are K3 triples).** Row and column permutations, transposition (applied to all three squares at once)
  and relabelling of the squares keep the QLS axioms and pairwise orthogonality. As cell permutations they leave each
  square's ray set unchanged, hence its individual non-classicality (`LEMMAS.md` lines 9–11). So every normalised or
  transformed configuration used below is again a K3 triple, and G4 holds for it (Link 3).

## 3. Encoder A: `gram_enc.build(3, None, True, True, None)`

Auxiliary values: each h := g(p, r) ∧ g(q, r); each guard w_{a,ℓ,p} := [p has at least three neighbours on ℓ].

| Family | Lines | Clause meaning | Why it holds |
|---|---|---|---|
| h definitions | 75–86 (clauses 83–85) | h ↔ g(p,r) ∧ g(q,r); h is created only when both g exist, else the product is the constant false | definition, with h set to the conjunction |
| G2, count 0 | 96 | (∨ h_r) ∨ ¬g(p,q) | Expanding in the ONB of ℓ, G(p,q) = Σ_{r∈ℓ} conj(G(r,p)) G(r,q). With no nonzero term, G(p,q) = 0 (Gram-G2). |
| G2, count 1 | 97–99 | ¬h_r ∨ (∨_{s≠r} h_s) ∨ g(p,q); g(p,q) omitted when p, q are collinear | A single nonzero term gives G(p,q) ≠ 0 (Gram-G2). If p, q are collinear, G(p,q) = 0 by G1, so a count of exactly one is impossible; the clause without g(p,q) says exactly that. Once each h equals its defining conjunction, these clauses hold by frame consistency (Codex F3). |
| G3 cover | 100–106 | ∨_{q ∈ ℓ2∖ℓ1} g(r,q) for r ∈ ℓ1∖ℓ2 | U[r,q] = ⟨ψ_r, ψ_q⟩ is the unitary change of basis between the ONBs of ℓ1 and ℓ2. Row r has norm 1; its entries at the meet point and at the cell collinear with r vanish by G1 (F3). So r has a neighbour among the listed q (Gram-G3). |
| G3 singleton | 107–114 | ¬g(r,q) ∨ (∨ rest) ∨ ¬g(r2,q) | If q is r's only neighbour, |U[r,q]| = 1, so column q has no other nonzero entry: g(r2,q) = 0 for r2 ∈ ℓ1∖ℓ2, r2 ≠ r (Gram-G3). |
| G5 | 115–118 | ¬g_a(p,q) ∨ ¬g_b(p,q), a < b | ⟨ψ_{a,p}⊗ψ_{b,p}, ψ_{a,q}⊗ψ_{b,q}⟩ = G_a(p,q) G_b(p,q) = 0 for p ≠ q by orthogonality of Ψ_a and Ψ_b (Gram-G5). |
| `--sym` units | 123–126 | g_1((1,0),(0,k)) for k = 1, 2, 3; this replaces the G4 clause of (square 1, row 0) | Link 5 normalisation. The residual normalisation of Link 6 fixes square 1, rows 0–1 and columns 0–3, so the units survive it. |
| G4 guards | 45–51, 127–136 | for every other (square, line) and each of the 42 off-line points: w → at least 3 of the 6 possible neighbours (15 clauses, one per 4-subset) | A 4-subset of six literals contains a true literal for every 4-subset iff at least three literals are true. With w as defined, each clause holds. |
| G4 disjunction | 137 | ∨ w over the 42 points | Link 3: each own line has an off-line point with at least three neighbours, so some w is true. |

Families not emitted: no symbol lines (L is None); `fix` is None, so lines 138–147 add nothing.
Degenerate branches are unreachable by F3: `at_least` with t > n (line 48) needs fewer than 3 candidates; the G3
clause at line 106 would be empty only with no candidate; the disjunction at line 137 would be empty only if no
point had 3 candidates. Guard count: 41 (square, line) pairs × 42 points = 1,722 guards, consistent with `--sym`
removing exactly the guards of (square 1, row 0) (AMENDMENT-4.r4:362–363 overstates the guard set; r3 §5, m8).

## 4. Encoder B: `gram_encB.py --squares 3 --heavy --sym`

Auxiliary values: each product m := g(p,r) ∧ g(q,r); every register of `counter2` its true prefix threshold
("at least 1" / "at least 2" among the items so far); every register c[i][k] of `counter_ge3` its true prefix
threshold "at least k among the first i items", and its output t := [at least 3 of the items].

| Family | Lines | Clause meaning | Why it holds |
|---|---|---|---|
| products | 126–135 (clauses 134) | m ↔ g(p,r) ∧ g(q,r) | definition |
| `counter2` | 41–57 | full equivalences n1 ↔ a1 ∨ x, n2 ↔ a2 ∨ (a1 ∧ x) | The true prefix thresholds satisfy exactly these recurrences (Codex: A′1 = A1 ∨ x, A′2 = A2 ∨ (A1 ∧ x)). |
| G2 | 136–157 | none → ¬g(p,q) (153); exactly one → g(p,q) (157); collinear p, q: ¬s1 ∨ s2 (151) | As for A (Gram-G2, and G1 for the collinear case). |
| G3 | 158–183 | c1 (172); c2 ∨ ¬g(r,q) ∨ ¬g(r2,q) (183) | As for A (Gram-G3): c1 is "at least one neighbour"; with fewer than two neighbours, a neighbour q of r is not a neighbour of any other r2. |
| G5 | 184–187 | ¬g_s(p,q) ∨ ¬g_t(p,q), s < t | Gram-G5. |
| `--sym` units | 191–194 | g_1((1,0),(0,k)), k = 1, 2, 3, replacing that line's G4 clause | as for A |
| `counter_ge3` | 60–89 | one-directional implications v → prev[k] ∨ (x ∧ prev[k−1]) with the base cases, and t → prev[3] (88) | True prefix thresholds satisfy each implication: at least k among the first i items means at least k among the first i−1, or the i-th item is true and at least k−1 among the first i−1. The first item's k = 2, 3 registers are forced false, which is their true value. |
| G4 disjunction | 195–202 | ∨ t over the 42 off-line points | Link 3, as for A. |

Families not emitted: no `--net-L`, no `--fix-json` (lines 203–215 add nothing).
Degenerate branches are unreachable by F3: `counter2` returns (None, None) only for no items (line 44), giving the
branch at line 148; s2 = None (one item) would make lines 151 and 155 malformed; line 169 emits an empty clause only
with no candidate; `counter_ge3` forces t false only with fewer than three items (lines 63–65). In production the G2
lists have 5–6 items, the G3 lists 6 candidates and the G4 lists 6 candidates, so none of these branches is reached.

## 5. Cube block and G6 (`k3_cubes.cube_clauses`, lines 70–99)

- **Units (line 79).** For a = 1, 2, 3 and k = 1, …, 6, the unit g_a((1,0),(0,k)) or its negation, according to
  whether k ∈ S_a. The cell (0,0) is collinear with (1,0) and has no variable (G1; K3-ERRATA E4). After the residual
  normalisation of Link 6 the configuration's supports at (1,0) on row 0 are exactly (S_1, S_2, S_3) of C, so all 18
  units hold.
- **G6 (lines 83–98).** For each singleton S_a = {k}, with q = (0,k) and every t ∉ {(1,0), q}: g_a((1,0),t) =
  g_a(q,t), written as two clauses, or as one negative unit when exactly one side is a collinear constant (lines
  94, 96), and skipped when both are. These hold: by `G6-G2-DERIVATION.r1.md` they follow from Gram-G1/G2 and the
  cube units (with the K3-ERRATA E5 wording for the collinear case); equivalently, ψ_{a,(1,0)} is a unit-modulus
  multiple of ψ_{a,q} (AMENDMENT-2.r1 §2). Squares with G6: C311 squares 2 and 3; C321 square 3; C411 squares 2 and 3.
- **Prefix.** The cube CNF is the base text followed by these clauses, with the header's clause count increased and
  the variable count unchanged (`k3_cubes.py:124-132`). So item 3 of the lemma, with items 1–2, gives every clause of
  the cube input. Header arithmetic (parent header erratum effec3db…b148; Claude audit cross-check) agrees: the C311
  and C411 blocks add 158 clauses and the C321 block 88.

## 6. Lex block, A route only (`k3_lex.py`)

- For each of the seven C311 generators (AMENDMENT-3.r1 §1; `k3_lex.py:118-121`), `lex_clauses` (lines 55–69)
  appends the comparator X ≤lex X∘σ with fresh prefix variables, skipping positions with σ(v) = v.
- The comparator lemma of K3-COMPOSITION.r3 Link 11 shows that, for any length, the clauses are satisfiable in the
  prefix variables iff X ≤lex X∘σ, with the witness e_i := [x_k = y_k for all k < i].
- X* is the least element of the finite H_311-orbit of the configuration's Gram pattern, so X* ≤lex X*∘σ for every
  generator σ. By K3-ERRATA E3 each orbit element is the Gram pattern of the configuration moved by an element of
  H_311, which is again a K3 triple (F4) normalised into C311: every C311 generator fixes rows 0–1, column 0 and the
  set of columns {1, 2, 3}, and its combined operation exchanges (square 2, column 4) with (square 3, column 5) while
  fixing column 6. So X* satisfies items 1 and 3, and the lex block with the prefix values above.

## 7. Cuts

The cut block has no auxiliaries; every literal is a negative g literal (AMENDMENT-4.r4 §4(i)). Under G1–G2 and Links
3 and 7, Link 10 (transport) shows that every K3 configuration satisfies every cut clause. This applies to the
normalised configuration (B route) and to the configuration whose pattern is X* (A route). So the strengthened
inputs, base ∧ cube ∧ G6 ∧ cuts (B, header 461370/1867942) and base ∧ cube ∧ G6 ∧ lex ∧ cuts (A, header
107513/897308), are satisfied.

## 8. Conclusion and limits

Lemma H3 holds: every clause family emitted for the exact K3 base instantiation and its cube, G6, lex and cut blocks
is either a necessary condition of the normalised K3 triple (Gram-G1…G5, G4, `--sym`, cube units, G6, and the cuts
under G1–G2) or a definition whose auxiliary has the canonical value given above. No emitted clause can exclude a
genuine K3 configuration normalised as stated.

Limits:
- This is a static reading of the pinned sources. That the certified CNF bytes are exactly these encoders' output
  rests on the regeneration hashes (parent A-cube replays regenerated with the pinned functions; producer drivers
  regenerate in memory and assert the pinned SHAs) and, for B's variable map, on the runtime oracle.
- It imports Links 3, 5, 6 and 10 as stated in K3-COMPOSITION.r3, and Gram-G1…G5 as accepted with K2.
- Acceptance of H3 is the parent's (decision 8). This note changes no status.
