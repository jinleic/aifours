# Problem 16 at n = 7 — proof package, revision r2 (frozen 2026-10-17 PDT)

Supersedes PROOF_CANDIDATE.md (pinned, unchanged) for status, certificate data and wording; the mathematics is the
same. Errata for all earlier lane documents: review/ERRATA_r2.md.

**Result.** Every set of 4 MOQLS(7) is classical. Hence M(7) ≤ 3, and with Ball–Simoens Corollary 7 (q = 7, d = 3,
H = {1,2,4}) 2 ≤ M(7) ≤ 3. Required wording: this *resolves the n = 7 instance of Problem 16* of arXiv:2607.12933v2;
"2 ≤ M(7) ≤ 4 becomes 2 ≤ M(7) ≤ 3". It does not solve Problem 16 and does not determine M(7).

**Status.** Correctness accepted by the parent (institute/runs/six-lane-2026-10-16/review/moqls7-parent-verdict.md);
computer-assisted. The written arguments are MODEL-AUTHORED (lane worker), checked by model reviewers (two task-agent
reviewers, Codex CLI gpt-6.1-sol, Claude CLI claude-opus-5-5: ACCEPT / ACCEPT-WITH-FIXES); no human peer review.
Novelty: unclear after a bounded parent audit (no earlier n = 7 resolution found). The logic needs ONE verified UNSAT
per class K2, K3, K4; two independently implemented encodings per class were each solved and DRAT-checked.

## 1. Conventions (F12)
This revision, PROOF_CANDIDATE.md and all code index rows, columns, symbols and coordinates by 0..6, with row 0 the
reference row. PROOF_PARTIAL.md uses 1..7 with row 1 as reference: its (i, j), |k⟩, "first row" correspond to
(i−1, j−1), |k−1⟩, row 0 here. Standard form w.r.t. row 0: Ψ_s(0, j) = |j⟩ for every square (one unitary per square).
supp Ψ_s(c) = {k : ⟨k|Ψ_s(c)⟩ ≠ 0}; weight = |supp|. In standard form a square is classical iff all weights are 1
(then Ψ_s(c) ∝ |L_s(c)⟩, L_s Latin with L_s(0, j) = j); mutually orthogonal classical QLS ↔ MOLS. A set is classical
iff every square is (source §2.2–2.3).

## 2. Reduction (F5)
Let S be a non-classical set of 4 MOQLS(7) in standard form w.r.t. row 0.
- (R1) Lemma 4 (PROOF_PARTIAL): off row 0 every weight is ≤ 3; a weight-3 entry forces weight 1 in the other squares.
- (R2) Theorem A: not all weights are ≤ 2; some square has a weight-3 entry.
- (R3) S′ := Lemma 10 (computational basis of row 0) applied to every square of S without a weight-3 entry. Lemma 10
  is never applied to a square with a weight-3 entry (hypothesis fails), so those m ≥ 1 squares pass into S′ entry
  for entry and stay non-classical; the modified squares are classical (properties in IMPORTS_r2 I1). **S′ need not be
  isotopic to S**: only its existence is used — S′ is a set of 4 MOQLS(7) in row-0 standard form whose non-classical
  squares are exactly the m untouched ones, each with a weight-3 entry.
- (R4) Theorem B: m ≠ 1. So S′ ∈ K_m, m ∈ {2, 3, 4} (m quantum + 4 − m classical squares).
- (R5) (SB2) normalization is applied to the VECTORS of S′: (α) a permutation of rows 1..6; (β) one column permutation
  σ applied to every square together with P_σ|k⟩ = |σ(k)⟩ on every square (on a classical square P_σ is exactly the
  symbol relabelling x ↦ σ(x)). Both are isotopies of S′ preserving row-0 standard form, weights, the
  quantum/classical split and (P4); the normalized set is again in K_m. Steps: move a weight-3 entry of Ψ1 to (1,0);
  σ with σ(0) = 0 sends the distinct nonzero L_t(1,0) to 1, …, 4 − m; σ fixing 0, …, 4 − m arranges the forced split
  S1(1,0) = three smallest of {5 − m, …, 6}, then one singleton each for Ψ2, …, Ψm; each later step fixes what earlier
  steps normalized. Lemma P (§3) is then applied to the normalized set.
- (R6) The CNFs encode: classical squares as free MOLS variables (first row identity), patterns S_s with (P1)–(P4),
  the (SB2) unit clauses, and — in ENCODER A ONLY — the extra row sort L_first(i,0) = i for i = 1..6 (by (α) on rows
  2..6, after (SB2) fixed L_first(1,0) = 1). Encoder B has no row sort. Each of the six CNFs is UNSAT (§5).
Contradiction; hence no non-classical set of 4 MOQLS(7) exists. A non-classical t-set with t ≥ 4 would contain a
non-classical 4-subset, so M(7) ≤ 3.

## 3. Lemma P (necessary conditions, unchanged from PROOF_CANDIDATE §3)
(P1) nonempty supports; column coordinate excluded; L_t(c) excluded for classical t; quantum supports at a cell
pairwise disjoint. (P2) on every row, column and classical symbol line (with its row-0 cell), each quantum square is an
ONB, so its 7×7 coefficient matrix is unitary: every coordinate covered; no two cells share exactly one coordinate; no
two coordinates co-occur in exactly one cell. (P3) for quantum s ≠ u and cells c ≠ c′, not both "share exactly one".
(P4) every quantum square has an entry of weight 3 (encoded as ≥ 3, which is weaker). All inferences use only: a
single-term inner product is nonzero; a unitary row/column cannot have exactly one nonzero product term; a unit
column is nonzero.

## 4. Imports and written lemmas
See review/IMPORTS_r2.md. Geometry route accepted by the parent: Egan–Wanless Table 6 (one paratopism class each
for 3- and 4-MOLS(7), explicit linear representatives) gives the AG(2,7) direction-class models used in Theorems A
and B; Facts C and L have analytic proofs (parent: review/moqls7-parent-affine-lemmas-v1.md) in addition to the lane's
two finite implementations. Shrikhande, Bose and Hall 1953 (with its 1954 correction; originals not read) are
redundant on that route. Lemma 10 is used through its printed proof (properties verified in review).

## 5. Certificates (full SHA-256; argv exactly as below; parent receipt
institute/runs/six-lane-2026-10-16/review/moqls7-parent-proofcheck-v1/parent-result.json, 04:18:10–04:30:09 PDT)
Pinned encoders: k2_encode_a.py b935bb11f1e8cf6983150657116b04cf389d90ed23ec46dcc6aa69067912239e,
k2_encode_b.py 097c62f8ecdb0980369d555b8aafecc6eb8f179aec6996a4fedf9c091bfe0299.
argv: `python -B <encoder> --mode generic --sb2 --quantum Q --ngeneric G --p4 Q --cnf <cnf> [--map <map> (A)]` with
(Q, G) = (12, 2) K2, (123, 1) K3, (1234, 0) K4. Solvers: CaDiCaL 3.0.1 (binary SHA-256 601c9fa8…d1fa) for A,
kissat 4.0.4 (05d6f3e9…a848) for B. drat-trim source d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee
(upstream master 2e3b2dc0); lane binary 111b0405…d5e4, parent binary a46c0c71…8e37 (cc -O2).

| case | CNF SHA-256 | proof (lane path, bytes) | proof SHA-256 | lane drat-trim | parent drat-trim |
|---|---|---|---|---|---|
| K2 A | f85f7e2a584e48da7d6b39306f6486fd0df853351b6164d24c839f25947fac28 | evidence/k2/a_generic_sb2.drat, 111614714 (text) | 664f8519d7a076608cd279040a47ba5e69053e247f7fb69de56ecb0b473ccf65 | VERIFIED 16.5 s | VERIFIED 16.4 s |
| K2 B | f47ebde19e86cd2975e505b99c2aff84c35d66ed3cf47dd94ca9417c191d2b27 | evidence/k2/b_generic_sb2.drat, 441237702 (binary) | 35fefe2826e0277b7af913f15c8a1493f84d973c3eb9f8c82ce057f116813cbc | VERIFIED 260.5 s | VERIFIED 280.1 s |
| K3 A | 47b1df07657b204c31178eeee8893d18588dc4543f8fc081e697d0e587a9d045 | evidence/k3/a_k3_sb2.drat, 93578637 (text) | c8e340f8e03068a4a30669e5c49171359aef29c84fb0eab3ad883d060316be03 | VERIFIED 20.4 s | VERIFIED 20.1 s |
| K3 B | 3b55b63ccb9d18cb85fde09c39291fd5451371045a33b325a44098049c3ea79f | evidence/k3/b_k3_sb2.drat, 958942562 (binary) | 0a8d1323ff68de04e0502335f143a2927e82e693dcb38cbfb986fba74ce35135 | VERIFIED 499.2 s | VERIFIED 515.8 s |
| K4 A | 96ac058a2928aeec48a693d1aa8e416126796b772b5b06399833583b57910b0b | evidence/k4/a_k4_sb2.drat, 1160397645 (binary) | d32a2a2706ed7b3f94027b2b199ea5f44b4c337bf60f31e9ccfb92012675534c | VERIFIED 293.3 s | VERIFIED 301.6 s |
| K4 B | ea3485b38bf360095be94e51d19afa5946e5eff6cc560c58392c0be1e0e190a2 | evidence/k4/b_k4_sb2.drat, 1116767447 (binary) | 5b33bed3e365060444b7afdaa2594ed51b2bce403fbc7eba865d0cdc4f575d0a | VERIFIED 427.0 s | VERIFIED 435.4 s |

Proof generation (lane, host clock PDT): K2A `cadical -q --no-binary` 03:39:53–03:40:34; K3A same 03:40:55–03:41:28;
K4A `cadical -q` (binary DRAT) 03:52:24–04:06:22; K2B `kissat -q` 03:45:18–03:52:04; K3B 03:56:35–04:10:07; K4B
03:57:28–04:09:37; each exit 20. Solver-only runs: K2A 39.6 s, K3A 32.2 s, K4A 824.7 s, K2B 409.6 s, K3B 804.3 s,
K4B 723.2 s (UNSAT). The six final CNFs regenerated with the exact argv (evidence/final_v1/INSTANCES_RECEIPT.json,
4315f377…0ea0b) and by the parent from the pinned snapshot copies are byte-identical to the solved CNFs.

## 6. Controls and checks (not load-bearing; fail-closed)
- Fixed-pattern controls (11 per encoder; ERR/timeout = failure): evidence/controls_v3/controls_{a,b}.json, run with
  the r2 encoders (identical clause generation; r2 CNFs byte-identical to the final ones, evidence/r2check_v1) — all
  agree with the exact expected status. The earlier receipts evidence/k2/controls_{a,b}.json (ERR could count as
  agreement) are withdrawn as evidence (F3); evidence/controls_v2 used the in-place-edited encoders (now *_r2).
- (SB2) clauses: evidence/sb2check_v1 — for all six final CNFs, SB2 CNF = non-SB2 CNF + unit clauses only (16/22/28),
  decoding exactly to the §2 (R5) assignment.
- Generic-mode positive controls (G1: one quantum + one generic classical square with a weight-≥3 entry; G2: two
  quantum squares, Cor-7 type): evidence/kctl_v4/RECEIPT.json (see ERRATA_r2 for its outcome and for the failed
  kctl_v2 run). No SAT control exercises (SB2) (review N3): the relaxed SB2 runs without (P3) were UNSAT for K2, K3 and
  timed out for K4 (evidence/kctl, diagnostics).
