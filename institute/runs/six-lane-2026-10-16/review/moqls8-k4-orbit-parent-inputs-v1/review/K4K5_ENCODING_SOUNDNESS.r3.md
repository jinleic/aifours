# Problem 16 at n = 8, classes K4 and K5: soundness of the Gram-pattern base CNFs, symmetry breaking, P4 frames and
# splitting — revision r3 (supersedes r2 for audit purposes; r1/r2 unchanged; model-authored)

Changes from r2: fixes for Codex review v1 (minor 3) and Claude review v1 (M1–M3, m1–m10): complete line→family maps
with square and frame sets; explicit index domains (self-pairs); exact P4 frame sets and clause counts; K4 claims
limited to CNF necessity until README §9 declares a K4 split; full hashes and command lines; trust list.
Keys: KK = review/PROOF_K1_K2.r2.md, K3 = review/PROOF_K3.r2.md, BS = Ball–Simoens arXiv:2607.12933v2.

## 0. What is claimed
(a) K5 bridge: every set in the reduced class K5 (§1), after the lossless moves of §5, yields a canonical assignment
satisfying every clause of the K5 base CNF, and it lies in exactly one leaf of the README §8/§8.1/§8.2 split.
It does NOT use F3. (b) K4: CNF necessity only — every K4 set yields a canonical assignment satisfying every clause of
GA3_K4w1.cnf; it uses F3 (hence the accepted K1–K3 certificates and E–W counts). Leaf-level K4 claims wait for §9.
No exclusion of K4 or K5 is claimed here.

## 1. Classes, reduction, F3
Let S be a set of 5 MOQLS(8) in row-0 standard form (per-square unitaries, BS LF 113 (iii)). S′ := Lemma 10 applied to
each square of S with no entry of weight ≥ 3 (W8: all weights ≤ 3). The untouched squares (those with a weight-3
entry) have ≥ 9 rays (KK LF 14–17), the treated ones are classical, so m(S′) := #untouched = #non-classical(S′) ≤
#non-classical(S). K_m := {S′ : m(S′) = m}; K5 and K4 are REDUCED classes. A set with five non-classical squares may
reduce into K4 (or K3…); only A8 + K1 = … = K5 = ∅ together cover every non-classical set (m9).
F3 (used only for K4): no set of 5 MOQLS(8) has exactly 1, 2 or 3 non-classical squares — the conjunction of KK LF 8
(exactly one or two) and K3 LF 9 (exactly three), both already quantified over all sets. Equivalently: restandardise T,
reduce; 1 ≤ m(T′) ≤ #nc(T) ≤ 3 (m(T′) ≥ 1 by A8), and K_{m(T′)} = ∅ (m1).

## 2. Variables, constants and index domains (M3, C2, C3, m10)
g(s,p,q) (gram_a.py 127–138; r3 130–141): ⊤ if p = q (so a shared cell of two lines gives U[c0][c0] = ⊤); ⊥ if p ≠ q
share a row or a column; otherwise ONE variable keyed ("g", s, min(p,q), max(p,q)) — one per square and unordered pair
of distinct cells. Canonical value g = [⟨Ψ_s(p),Ψ_s(q)⟩ ≠ 0]; it is ⊤ for p = q and ⊥ on common lines (ONBs).
CNF.add (gram_a.py 51–61): drops clauses containing ⊤, drops ⊥ literals, RAISES on an empty clause — no empty clause can
be emitted. AND(name, a, b) (63–76): constant operands fold (⊥ → ⊥, ⊤ → other operand); otherwise a memoised variable
v with v ⇔ a ∧ b (3 clauses). Memo keys always contain the square s and determine the operand set:
b3 = ("b3", s, x, y, z) ≡ g_s(x,z) ∧ g_s(y,z); c4 = ("c4", s, a, p, q) (p,q sorted) ≡ g_s(a,p) ∧ g_s(a,q);
u5 = ("u5", s, l[0], l[1], q, a) ⇔ "the l-frame support of q is exactly {a}" (full equivalence: u ⇒ ov_a, u ⇒ ¬ov_b
for b ≠ a, and ov_a ∧ ∧_{b≠a} ¬ov_b ⇒ u; clauses with a constant ⊥ overlap fold away);
w3 = ("w3", s, r, p) (gram_a) / ("w3", s, ℓ[0], ℓ[1], p) (r3), ONE-WAY: w3 ⇒ weight ≥ 3; lexeq ("lexeq", i, k),
square 1 only, full equivalence. No counters and no other auxiliaries exist.
Domains: G3 over unordered pairs of distinct lines among the 8 rows and 8 columns (parallel or intersecting; the shared
cell's entry is ⊤); G4 over a line l and unordered pairs p ≠ q with p, q ∉ l; G5 over q ∉ l, a ∈ l with g(a,q) not
constant ⊥, p ∉ {q, a}; P4 flags at cells p ∉ ℓ.

## 3. Line → family maps
### 3.1 gram_a.py (SHA-256 bf1aada12a04e7a0054c1e30c681dc81f32ba90c221d84dc982097d4cf14d05a), K5 base command
`python -B gram_a.py --order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex --cnf
../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --map ../evidence/gram_dev_v1/GA5L_K5_sb2.map.json` (cwd code/; Python 3.13.9)
→ SHA-256 6ecb77a779170635830c4c7c488c3e0eb434ee249fb2b1c81dc2625c4183469b, 509915 vars, 5740230 clauses.
| lines | content | active for K5 | squares / lines / frames |
|---|---|---|---|
| 1–25 | docstring, imports | — | — |
| 28–36 | gmul8 (GF(8) slopes) | no (fixed mode only) | — |
| 39–80 | CNF class (var/add/AND), neg | helpers | — |
| 83–98 | setup: cells, CL = [] (ngeneric 0), lin, L | CL empty | — |
| 100–125 | generic classical-square constraints | no (CL empty) | — |
| 127–138 | g() | yes | §2 |
| 140–149 | G1 on classical lines | no (CL empty) | — |
| 150–153 | G2 | yes | all 10 pairs of squares 1–5, all distinct cell pairs |
| 154–163 | fixg (controls) | no | — |
| 164–170 | lines = 8 rows + 8 columns | yes | (classical lines only in fixed mode) |
| 172–177 | helper "not exactly one" | yes | — |
| 179–190 | G3 (+ b3) | yes | squares 1–5; all 120 pairs of the 16 lines |
| 191–206 | G4 (+ c4) | yes | squares 1–5; 16 lines; p ≠ q ∉ l |
| 207–232 | G5 (+ u5) | yes (--g5) | squares 1–5; 16 lines |
| 233–247 | P4 (+ w3) | yes | squares 1–5; frames {row 0} only (no --p4-all-rows) → exactly 5 at-least-one clauses |
| 248–270 | ROWLEX (+ lexeq) | yes (--rowlex) | square 1, column 0, pairs (i, i+1), 2 ≤ i ≤ 6 |
| 271–281 | K5 SB2 units | yes (--sb2) | (1,0): squares 1–5 ↦ {1,2,3},{4},{5},{6},{7} |
| 285–318 | main: parse, write "p cnf" + clauses, map/meta | — | — |
### 3.2 gram_a_r3.py (SHA-256 40622a6f7809a7ebc3974d40e9353af691c9f4d34d588a6506df1379b7d4fdbb), K4 base command
`python -B gram_a_r3.py --order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 1234 --p4-all-rows --p4-all-cols
--sb2 --g5 --weight1 5 --cnf ../evidence/k4_w1_v1/GA3_K4w1.cnf --map ../evidence/k4_w1_v1/GA3_K4w1.map.json`
→ SHA-256 7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7, 513184 vars, 5833793 clauses.
| lines | content | active for K4 | squares / lines / frames |
|---|---|---|---|
| 1–29 | docstring, imports | — | — |
| 30–82 | gmul8, CNF class, neg | helpers | — |
| 85–101 | setup (CL = []) | CL empty | — |
| 103–128 | generic classical constraints | no | — |
| 130–141 | g() | yes | §2 |
| 143–152 | G1 classical lines | no | — |
| 153–156 | G2 | yes | all 10 pairs of squares 1–5 (square 5 = L included) |
| 157–166 | fixg | no | — |
| 167–180 | lines (16), helper | yes | — |
| 182–193 | G3 | yes | squares 1–5 |
| 194–209 | G4 | yes | squares 1–5 |
| 210–235 | G5 | yes | squares 1–5 |
| 236–252 | P4 | yes | squares 1–4 ONLY (--p4 1234); frames: 8 rows + 8 columns → 64 at-least-one clauses |
| 253–275 | ROWLEX | NO (--rowlex absent) | — |
| 276–285 | weight1 | yes | square 5: at most one nonzero row-0 overlap at each of the 56 off-row-0 cells |
| 286–300 | K4 SB2 + row sort | yes (sb2 ∧ weight1) | g_5((0,k),(1,0)) = [k = 1]; squares 1–4 at (1,0) ↦ {2,3,4},{5},{6},{7}; g_5((0,i),(i,0)) = ⊤, i = 2..7 |
| 301–311 | K5 SB2 | NO (guard `sb2 and not weight1`) | — |
| 315–350 | main | — | — |
Hence (M1): the K4 CNF has no K5-SB2 unit, no lexeq variable/clause, and no P4 for square 5. The parent's emitted-CNF
family counts (task Moqls8EncoderBinding) are the check of record.

## 4. Validity of each family for every QLS (unchanged mathematics of r2 §3, with domains of §2)
G2: Prop 1 (tensor inner product factorises). G3: U = [⟨Ψ(a),Ψ(b)⟩] between two ONBs is unitary: nonempty rows and
columns; a single nonzero term cannot make UU* or U*U vanish off the diagonal (Lemma 2). G4: Parseval in the ONB of l;
only "one term ⇒ ≠ 0" and "no term ⇒ 0" are used (cancellation of ≥ 2 terms is never excluded). G5: singleton frame
support ⇒ Ψ(q) = λΨ(a), |λ| = 1. P4 gadget (m5): for each flag the 8 overlaps g_s(a,p), a ∈ ℓ (the one on p's own
column/row is ⊥), and the 28 explicit clauses ¬w ∨ ∨_{k∈K} ov_k over the 6-subsets K: satisfiable with w = ⊤ iff ≤ 5
zeros iff weight ≥ 3. weight1: a classical square in standard form is Ψ(p) = phase·|L(p)⟩ — exactly one nonzero
row-0 overlap (the clause encodes only "at most one"; nonemptiness is G3).

## 5. Lossless moves (vectors are moved first; auxiliaries take defining values afterwards; no CNF symmetry assumed)
(α) a common permutation of rows 1..7; (β) a common column permutation σ with P_σ|k⟩ = |σ(k)⟩ on every vector (keeps
row-0 standard form); (γ) per-square unitaries; (τ) transposition — NOT a BS isotopy (BS LF 107–113), but it maps a set
of 5 MOQLS(8) to a set of 5 MOQLS(8) with the same per-square ray counts (all that F3 and W8 need) (m2, m8).
K5 SB2: a weight-3 entry of Ψ1 to (1,0) by (α), (β); at (1,0) the five supports avoid 0 (rule #2), are pairwise disjoint
(G2/rule #3 with q = (0,k)), nonempty, |S1| = 3 ⇒ 3 + 1+1+1+1 = 7: a partition of {1..7}; σ fixing 0 ↦ {1,2,3},{4},
{5},{6},{7}. ROWLEX (m6): then (α) on rows 2..7 sorts v_i = (g_1((0,k),(i,0)))_{k=0..7}, k = 0 most significant,
non-decreasing, constraints on pairs (i, i+1), 2 ≤ i ≤ 6, chain start e_{−1} = ⊤. Rows 0 and 1 are not included
(widening to (1,2) would be unsound: v_1 = 01110000).
K4 SB2 + sort: a weight-3 entry of Q1 to (1,0); supports of Q1 (3), Q2–Q4 (≥ 1 each) and L ({L(1,0)}) partition
{1..7}; σ fixing 0 ↦ L(1,0) = 1, {2,3,4},{5},{6},{7}; then (α) on rows 2..7 makes L(i,0) = i. This consumes the row
freedom, so the K4 CNF has no ROWLEX (M1 ii).

## 6. P4 frame sets (M2)
K5: frames {row 0}, squares 1–5, exactly 5 at-least-one clauses: each square of a K5 set is untouched, i.e. has a
weight-3 entry in row 0's frame — by DEFINITION of the reduced class; no other frame is asserted (another frame would
make K5 conditional on K4 = ∅). K5 is F3-independent.
K4: frames = all 8 rows and all 8 columns, squares Q1–Q4. For a K4 set and a line ℓ: apply (τ) if ℓ is a column, (α)
to bring ℓ to row 0, (γ) to restandardise; ℓ-frame weights become computational weights; if some Q_s had no weight-3
entry there, its weights are ≤ 2 (W8) and Lemma 10 makes Q_s classical, leaving exactly three non-classical squares
(the other Q's keep ≥ 9 rays; L, Q_s′ classical) — contradicting F3. No minimality and no Lemma R are used (m2).

## 7. Splitting
K5: README §8 (V1), §8.1 (V2..V8, full 128-assignment products, streamed strict certification), §8.2 (strict
reclassification of old root records, versioned cover ledger with validator code/k5_cover.py, ledger-driven strict
runner). For any 7-tuple of literals ∨_a ∧_i x_i^{a_i} ≡ ⊤ (repeated or fixed variables only create contradictory or
duplicate leaves), so by induction the leaves cover the base; the canonical assignment lies in exactly one leaf.
K4: no split declared yet (§9 pending) — no leaf-level claim (Codex minor 3, Claude m7).

## 8. Trust list (m8)
Imported: BS §2.2–2.4 definitions and rules #2/#3; BS Lemma 10 (printed proof re-checked, including the
same-or-disjoint step). Written, reviewed: Prop 1, Lemma 2, W8, A8, KK LF 14–17 (classical ⇔ 8 rays; a weight-3 entry ⇒
≥ 9 rays), the reduction, the transposition symmetry (τ). K4 additionally inherits, through F3, the K1–K3 certificates
and the E–W catalogue counts (39, 2165) as parent-accepted. K5 does not. Machine facts are only DRAT verifications
of hash-bound leaf CNFs (solver correctness not trusted).
