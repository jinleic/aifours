# Six-lane phys-2 (fifth target): minimum support of AME(4,6) states

Worker: PhysEpQutrit. Host clock PDT; every time label below comes from `date` on the host. Lane created 10:37:21.

## 0. Frozen protocol (written before any computation; never edited afterwards)

A byte copy of this README, taken at freeze time, is kept in `archive/`. §1 below holds the checkpoints and is the
only part that changes.

### 0.1 Target and contract
- Contract (read-only): `institute/runs/six-lane-2026-10-16/screening/phys-2-ame46-support-contract.json`, SHA-256
  1baee48355c8e67e42c14ecf8164d4ace9591e6c5288c82f824ddec410d85f15.
- The target is to determine the minimum support of AME(4,6) states. Either:
  - exhibit an exact AME(4,6) state with at most 59 non-zero coefficients in some product basis; or
  - prove that every AME(4,6) state has at least 60 non-zero coefficients in every product basis.
- A fully proved lower bound L > 38 is partial progress only.
- Known status (Pandya arXiv:2610.16673v1, §VI, pinned layout LF498–520): 38 ≤ s_min ≤ 60, and "Whether the gap
  between 38 and 60 can be closed is open."
- This is a crowded field. No novelty claims will be made, and a search miss is not novelty.

### 0.2 Definitions and representation (fixed)
- **State and reshapings.** ψ ∈ (C^6)^{⊗4}, with coefficients ψ_x for x = (x1, x2, x3, x4) ∈ [6]^4, [6] = {0, …, 5}.
  - The support is S = {x : ψ_x ≠ 0}, and s = |S|.
  - The three reshapings are π ∈ {12|34, 13|24, 14|23}. For π = (ab|cd), U_π has rows (x_a, x_b), columns (x_c, x_d)
    and entries U_π[(x_a,x_b),(x_c,x_d)] = 6ψ_x.
  - ψ is AME(4,6) iff all three U_π are unitary (all six two-party marginals equal I/36).
  - Local unitaries preserve the AME property. So "minimum over product bases" = minimum of |S| over all AME states
    in the computational basis.
- **Rows and columns.** Each pair P ⊂ {1,2,3,4} of coordinates, together with a value z ∈ [6]², is a row (or a
  column) of exactly one reshaping. Call these P-lines.
- **Classical officers and counts.**
  - Classical officers are T = {x : |ψ_x| = 1/6}, with t = |T|. The non-classical part is N = S ∖ T.
  - e := s − (72 − t). It is the same for all three reshapings, because s and t are.
  - t_{i,a} := |{x ∈ T : x_i = a}|, and d_{i,a} := 6 − t_{i,a}.
- **Relaxed combinatorial model RCM(B).** Boolean pattern (S, T), T ⊆ S ⊆ [6]^4, with:
  - (C1) every P-line meets S;
  - (C2) x ∈ T ⇒ no other element of S agrees with x in ≥ 2 coordinates;
  - (C3) a P-line meeting S in exactly one element ⇒ that element is in T;
  - (C4) combinatorial orthogonality. In every reshaping, the column sets of two distinct rows do not meet in exactly
    one column, and the row sets of two distinct columns do not meet in exactly one row;
  - (C5) |S| ≤ B.
  RCM ignores moduli and phases. It is a necessary condition for realizability, used only in that direction.
- **Realizability filters (exact).**
  - Moduli: an LP in m_x = 36|ψ_x|² > 0 with every P-line sum equal to 1.
  - Phases: for every 2×2 connected component of a reshaping, with rows r, r′ and columns c, c′,
    φ_rc − φ_rc′ − φ_r′c + φ_r′c′ ≡ π (mod 2π). The system is integer-linear modulo 2π. It is inconsistent iff some
    integer combination of its rows cancels every φ and has an odd sum of right-hand multiples of π.
  - Components larger than 2×2 enter only through their combinatorial and LP constraints, unless further conditions
    are proved first.

### 0.3 Attack (in this order)
- **Stage 0.**
  - Pin the sources in `sources/` with SHA-256.
  - Re-check the open status.
  - Positive control: reproduce Pandya's 60-term real state (Table I) exactly, using integer arithmetic over Z[√2].
    Check that the three reshapings are orthogonal, the support is 60, t = 12, and each reshaping is twelve 1×1 blocks
    plus twelve 2×2 blocks. Mutations must be rejected.
- **Stage 1.** Written proofs, each line checkable:
  - the classical-officer code;
  - s ≥ 72 − t;
  - the row-overlap lemma;
  - the component lemma: components of size k ≥ 2 have 2k + e_C entries, with e_C = 0 ⇒ k = 2 and e_C ≠ 1;
  - the scout lead: s ≤ 59 ⇒ t ≥ 14;
  - the slice lemma: t_{i,a} ≠ 5, and N-elements with x_i = a lie in {a} × D_j × D_k × D_l with |D| = d_{i,a};
  - the hole bound |N| ≤ (36 − t)².
- **Stage 2.** Exclusions from the large-t end (partial lower bounds), proving L stepwise. For each candidate pair
  (t, e) with 72 − t + e < L, every configuration must be excluded by:
  - a written argument; or
  - an exhaustive search whose completeness is argued in writing, with exact phase and moduli checks.
  Classical theorems may be cited only through the pinned sources: the nonexistence of a pair of orthogonal Latin
  squares of order 6 (Pandya LF45 [7–9]), and Parker's bound t ≤ 34 (Pandya LF509–511 [32]). Each use is labelled.
- **Stage 3.** A general SAT model, RCM plus 2×2-component phase obstructions (as proved local lemmas or as CEGAR
  cuts, each cut justified), for t ≥ 14 and e ≤ t − 13:
  - CNF generated by `code/`;
  - solvers kissat 4.0.4 and CaDiCaL 3.0.1;
  - UNSAT claims need an LRAT proof (CaDiCaL `--lrat`) checked by an independently written checker in this lane;
  - the positive control is RCM(60) with Pandya's pattern, which must be satisfiable.
- **Stage 4.** Construction attempts with t ≥ 14 and e ≤ t − 13. Any candidate pattern must pass the moduli LP and the
  phase system. A witness requires exact coefficients in a stated number field and an exact check of all three
  reshapings.

### 0.4 Symmetry
- The symmetry group G = S_6 ≀ S_4 (local relabelings and party permutations) preserves AME, s, t and every RCM
  constraint.
- A symmetry reduction may be used only after its soundness proof is written in `review/` or `evidence/`:
  - (SB1) If t ≥ 1, then WLOG 0000 ∈ T.
  - Any further normal form (for example, a maximal classical slice in coordinate 1 placed as (0, j, j, j)) and any
    lex-leader predicate: the proof must show that the normal form is reachable by G, and that the residual group
    used for lex-leader preserves it.
- No unproved symmetry reduction will be used.

### 0.5 Stop rules and claims
- Timeouts, UNKNOWN, heuristic misses and incomplete searches are not nonexistence.
- RCM solutions are not AME states.
- A claimed lower bound needs a complete written proof plus checked computations.
- A claimed witness needs exact verification.
- Nothing is called "first", and no novelty or priority claim is made.
- Floats are exploration only, never evidence.
- Resources: ≤ 4 CPU processes, ≤ 8 GiB, ≤ 10 GiB of new data, chunks ≤ 3 h, README checkpoints ≤ 30 min.
- Solvers are stopped only through their native time limits or SIGTERM with a bounded wait. Never SIGKILL or
  `subprocess.run(timeout=…)`.
- No writes outside this lane. No deletion: superseded files go to `archive/`.
- Freeze-once: a frozen proof goes to rN+1 for corrections.

## 1. Status (checkpoints)
- 10:37:21 lane created; §0 written before any computation.
