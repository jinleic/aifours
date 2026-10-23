# Problem 16 at n = 7 — CANDIDATE positive answer (computer-assisted)

**Claim (candidate).** Every set of 4 MOQLS(7) is classical. Hence M(7) ≤ 3, and with Corollary 7 of Ball–Simoens
(Example 15), 2 ≤ M(7) ≤ 3. Problem 16 of arXiv:2607.12933v2 ("Is a set of n − 3 MOQLS(n), n ≠ 4, necessarily
classical?") is answered YES for n = 7.

**Status.** CANDIDATE, written 2026-10-17 PDT by the lane worker; NOT independently reviewed. Ingredients:
(a) human proofs (review/PROOF_PARTIAL.md: Prop 1, Lemmas 2–4, Theorems A, B; §2 below);
(b) imported theorems (review/IMPORTS.md: Lemma 10 and its proof properties, Shrikhande, Bose, Hall 1953,
Egan–Wanless — the last used only inside Theorem B);
(c) three SAT certificates (classes K2, K3, K4), each produced by two independently written encoders and two
solvers, with DRAT proofs checked by drat-trim (status per class in §5).
The DRAT checks certify the CNF files only; the correctness of the encodings rests on §3–§4, the encoder
controls (§5.3) and the agreement of two independent encoders.

## 1. Conventions
Cells c = (i, j), i, j ∈ {0,…,6}; row 0 is the reference row. Standard form w.r.t. row 0 (rule #1): Ψ_s(0, j) = |j⟩
for every square s. The support of Ψ_s(c) is supp Ψ_s(c) = {k : ⟨k|Ψ_s(c)⟩ ≠ 0}; its weight is |supp|. A QLS in
standard form is classical iff all its entries have weight 1 (then Ψ_s(c) ∝ |L_s(c)⟩ with L_s a Latin square,
L_s(0, j) = j); mutually orthogonal classical QLS ↔ MOLS. A set is classical iff each square is.

## 2. Reduction to three finite pattern problems
Let S = {Ψ1, …, Ψ4} be a non-classical set of 4 MOQLS(7) in standard form w.r.t. row 0.
- (R1) Lemma 4: every entry off row 0 has weight ≤ 3, and at a weight-3 entry the other three squares have weight 1.
- (R2) Theorem A: not all entries have weight ≤ 2. So some square has a weight-3 entry.
- (R3) Let S′ be obtained by applying Lemma 10 (basis of row 0) to every square of S that has no weight-3 entry.
  By I1 (properties (i)–(iii)), S′ is a set of 4 MOQLS(7) still in standard form w.r.t. row 0; each modified square
  is classical; the unmodified squares are exactly those with a weight-3 entry, and they are non-classical.
  Let m ≥ 1 be their number; relabel them Ψ1, …, Ψm; the classical squares Ψ_t (t > m) have symbol arrays L_t
  forming 4 − m MOLS(7) with first row 0,1,…,6.
- (R4) Theorem B: m ≠ 1. So m ∈ {2, 3, 4}; call the class of S′ K_m.
- (R5) Lemma P (§3): the support pattern S_s(c) := supp Ψ_s(c) (s ≤ m, c off row 0) together with (L_t)_{t>m} satisfies
  (P1)–(P4). By §4, after a relabelling preserving all hypotheses, it also satisfies (SB2).
- (R6) For each m, the CNF instance encodes the existence of MOLS L_t (standard form, as variables — every pair /
  single square / none) and patterns S_s with (P1)–(P4) and (SB2). All three instances are UNSAT (§5). Contradiction.
Hence no non-classical set of 4 MOQLS(7) exists. ∎ (modulo §5 status)

## 3. Lemma P (necessary pattern conditions) with proofs
Write N for the net of lines {rows, columns, lines {c : L_t(c) = x} of each classical square}.
- (P1) S_s(c) ≠ ∅; j ∉ S_s(c) for c = (i, j), i ≥ 1; L_t(c) ∉ S_s(c) for every classical t; S_s(c) ∩ S_u(c) = ∅ for
  quantum s ≠ u. Proof: nonzero vector; Ψ_s(c) ⊥ Ψ_s(0, j) = |j⟩ (column); c and (0, L_t(c)) lie on a common L_t-line,
  and Ψ_s ⊥ Ψ_t with Ψ_t classical forces Ψ_s(c) ⊥ Ψ_s(0, L_t(c)) = |L_t(c)⟩ (Prop 1, since Ψ_t(c) ∝ Ψ_t(0, L_t(c)));
  rule #3: Ψ_s(c)⊗Ψ_u(c) ⊥ |k⟩⊗|k⟩ = Ψ_s(0,k)⊗Ψ_u(0,k) gives ⟨k|Ψ_s(c)⟩⟨k|Ψ_u(c)⟩ = 0.
- (P2) For every line M ∈ N and quantum s, the 7 vectors Ψ_s(c), c ∈ M, form an ONB (rows/columns: QLS; classical
  lines: Prop 1 as in P1). Their 7×7 coefficient matrix is unitary, so its rows and its columns are orthonormal:
  (a) every coordinate occurs in some S_s(c), c ∈ M; (b) no two cells of M share exactly one coordinate (Lemma 2 for
  rows); (c) no two coordinates co-occur in exactly one cell of M (Lemma 2 for columns).
- (P3) For quantum s ≠ u and all cells c ≠ c′: not both |S_s(c) ∩ S_s(c′)| = 1 and |S_u(c) ∩ S_u(c′)| = 1
  (each forces a nonzero inner product by Lemma 2; Prop 1 forbids both).
- (P4) Every quantum square has an entry of weight exactly 3 (R3; weight ≤ 3 by R1).
First-row cells are included in all line conditions with S_s(0, j) = {j}.

## 4. Symmetry breaking (SB2)
Two operations preserve "4 MOQLS(7) in standard form w.r.t. row 0", supports up to the induced relabelling,
weights, classicality, and (P1)–(P4): (α) a permutation of rows 1..6 applied to all squares; (β) a permutation σ of
columns applied to all squares together with the unitary P_σ|k⟩ = |σ(k)⟩ on every quantum square and the symbol
relabelling x ↦ σ(x) on every classical square (row 0 becomes Ψ_s(0, σ(j)) = |σ(j)⟩ again).
By (α), (β) move a weight-3 entry of Ψ1 to (1, 0). Then L_t(1, 0) ≠ 0 are distinct (column 0 has symbol 0 in row 0;
orthogonality); by (β) with σ(0) = 0 make them 1, 2, … in the order of the classical squares. The allowed set at
(1,0) is then {1 + (4 − m), …, 6}, of size 6 − (4 − m) = m + 2; S1(1,0) takes 3 of them and each of S2..Sm a nonempty
disjoint part of the remaining m − 1, i.e. one each; by (β) with σ fixing 0, …, 4 − m make S1(1,0) the three
smallest and S2, S3, … the next ones in order. Finally by (α) on rows 2..6 sort the first classical square's column 0
(L(i,0) = i), when a classical square exists. Encoder B does not use the final row sorting.

## 5. Certificates (paths relative to the lane; CNF SHA-256 prefixes)
Solvers: CaDiCaL 3.0.1, kissat 4.0.4 (Homebrew); drat-trim compiled from drat-trim.c (SHA-256 d834b649…).

| class | encoder A CNF / result | DRAT (A) | encoder B CNF / result |
|---|---|---|---|
| K2 (2 quantum, 2 generic classical) | evidence/k2/a_generic_sb2.cnf f85f7e2a… UNSAT 39.6 s | VERIFIED (111.6 MB text DRAT, 16.5 s) | evidence/k2/b_generic_sb2.cnf f47ebde1… UNSAT 409.6 s (kissat) |
| K3 (3 quantum, 1 generic classical) | evidence/k3/a_k3_sb2.cnf 47b1df07… UNSAT 32.2 s | VERIFIED (93.6 MB, 20.4 s) | evidence/k3/b_k3_sb2.cnf 3b55b63c… PENDING |
| K4 (4 quantum) | evidence/k4/a_k4_sb2.cnf 96ac058a… UNSAT 824.7 s | PENDING | evidence/k4/b_k4_sb2.cnf ea3485b3… PENDING |

5.1 Earlier FIXED-net K2 instances (AG(2,7) pairs, harmonic and equianharmonic 4-nets): UNSAT for both encoders,
all four DRAT proofs VERIFIED (evidence/k2/*_fixed_*). 5.2 GENERIC runs without SB2 did not finish in 1 h (UNKNOWN;
recorded, not used).
5.3 Encoder controls (code/k2_controls.py; evidence/k2/controls_{a,b}.json): eleven fixed-pattern instances —
exact Corollary-7 square on its 3-net (positive), Cor-7 square + classical square encoded as a quantum square
(positive, exercises P3), a genuine QLS with a Fourier-rotated 3×3 Latin subsquare (weight-3 positive), its
singleton mutation (P2b negative), orthogonal vs non-orthogonal shift pairs (P3 positive/negative), classical-line
P2 positive/negative, a classical pair with and without (P4) — each encoder's SAT/UNSAT agrees with a direct
evaluation of (P1)–(P4) from the definitions. Generic positive controls (evidence/kctl): one quantum + one generic
classical square with a weight-≥3 entry, and two quantum squares (the Corollary-7 pair) — both SAT; the decoded
solutions pass the direct checker (code/check_model.py) with 0 violations.

## 6. What a reviewer must check
1. Lemma P and (SB2) (§3–§4); in particular that (P4) applies to every quantum square of S′ (R3).
2. Theorems A and B (PROOF_PARTIAL §2–§3) and their imports (IMPORTS.md), incl. the use of Lemma 10's proof
   properties (supports never grow; weight-1 entries fixed).
3. That the CNFs encode (P1)–(P4)+(SB2) and nothing stronger: read k2_encode_a.py / k2_encode_b.py (generated by
   `python -B k2_encode_{a,b}.py --mode generic [--quantum 123 --ngeneric 1 | --quantum 1234 --ngeneric 0]
   --p4 <all quantum labels> --sb2 --cnf …`), re-run the controls, regenerate the CNFs and compare hashes.
4. Re-run the solvers and drat-trim (minutes each).
Novelty/priority: not established; no literature search beyond the two sources in sources/.
