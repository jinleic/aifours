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
- 10:37:52 (mtime) §0 frozen, SHA-256 b1fccb5392dcd2c70ef0e38ad09d8a38530a3c427801522d2c72b500f430dafe. A byte copy
  is kept as `archive/README.protocol-frozen-2026-10-17T103752.md`.
- 10:37:58 the eight parent-pinned source files were copied into `sources/`; their SHA-256 values match the parent
  manifest. Open status re-checked: the pinned arXiv listing (10:24) and two web searches at about 10:40 found
  nothing newer about AME(4,6) support.
- 10:39:39–10:39:40 positive control `code/pandya_control.py` (0a7f14a9…03f0) → `evidence/pandya_control.json`
  (0e0f2a86…ca74): all_required_true = true. Checked exactly over Z[√2]:
  - all six marginals satisfy 72ρ = 2I;
  - s = 60, t = 12, e = 0, and the classical officers equal P1∪P2∪P3 (a distance-3 code);
  - each reshaping is twelve 1×1 and twelve 2×2 components;
  - RCM constraints C1–C4 hold;
  - all five mutations are rejected.
- 10:47–10:49 e = 0 SAT model `code/ame_e0_cnf.py` (exact-two lines, row overlap, |T| = t, optional SB, and the
  phase-obstruction families TBL and TWIN):
  - the CNF with Pandya's pattern fixed is SAT under kissat, so TBL and TWIN do not exclude a phase-consistent
    pattern;
  - `code/phase_check.py` (exact HNF left kernel) reproduces Pandya's phase system: 36 equations, rank 28,
    consistent for both complex and real phases. It detects verified three-block obstructions on all four
    hole-2 structures (OA(8,4,2,2) on a 2^4 subcube).
- 10:49:07 kissat runs on t = 14 (e = 0 forced), split by SB2 into τ ∈ {3, 4, 6}, limit 1800 s each, 3 processes.
  This is exploration only, with no proof logging yet.
- 11:19:07 all three t = 14 kissat runs (τ = 3, 4, 6) ended UNKNOWN at the 1800 s limit. This is not UNSAT. Plain
  CDCL with SB2 alone does not settle t = 14 quickly.
- 11:19 `review/drafts/LEMMAS_AME46.draft.md` drafted, not frozen. It contains:
  - Lemmas 1–11: norms, classical officers, code, count, overlap, components, e_K ∉ {1} with e_K = 0 ⇔ 2×2, the
    scout lead (s ≤ 59 ⇒ t ≥ 14), slices with d_{i,a} ≠ 1, the hole bound, and e = 0 line structure;
  - draft Theorem A: s ≥ 42 proved, with Tarry cited for t = 36 and a Fourier classification of OA(8,4,2,2) for
    t = 32. s ≥ 43 is pending the (t, e) = (30, 0) analysis;
  - the TBL and TWIN obstruction proofs, the 4×4 component lemma (at least 11 entries), and the SB1/SB2 soundness
    proofs.
- 11:21:19 kissat probes of the e = 0 model at t = 30, 28, 26 (τ = 6 forced), limit 1200 s, to gauge large-t
  difficulty.
- 11:33–11:41 the probes ended. t = 30 was UNSAT at 727 s (kissat, no proof; not a claim). t = 28 and t = 26 were
  UNKNOWN at 1200 s.
- 11:45 the N-only relaxation at t = 30 was SAT in 12 s. Its N has a consistent phase system, so at t = 30 the
  obstruction is classical completion.
- 11:52:42 (mtime) **FROZEN partial result `review/SUPPORT_LOWER42.r1.md`**, SHA-256
  54880341b045b18fac6b60394c9ad12ae778de40945f2454fa04142c079bb2ad: every AME(4,6) state has s ≥ 42 in every
  product basis. Tarry is cited for t = 36.
  - Replay: `code/verify_lower42.py` (9106089a…182b) → `evidence/verify_lower42.json` (caee2f5e…1eaa), all facts
    true.
  - The draft LEMMAS file is unchanged.
  - Next step: the s ≥ 44 route. (30, 0) is the only case left for s ≥ 44, because t = 31 is impossible (a profile
    lemma) and (32, 3) is impossible (a 4×4 lemma).
- 11:53–12:00 structured engines `code/large_t_e0.py` (e = 0, exact two per line) and `code/large_t_gen.py` (any e).
  Both use profile enumeration, an N-only product-space CNF, orbit-blocked enumeration with an LRAT-checked final
  UNSAT, then exact per-orbit checks (components, 2×2 phases), then a classical-completion CNF with LRAT.
  - EXCLUDED: (30,0), (30,2), (30,3), (29,2), (32,0..3) and (28,0). For (28,0), 26 orbits were all excluded, 23 by
    phase obstruction and 3 by completion UNSAT.
  - t = 32 with e ≥ 4: 3 orbits pass the checks and have satisfiable completions (IMOLS(6,2)-type T). These are
    handled by the AME(4,2) shadow lemma.
  - Controls (`code/engine_control.py`): both engines accept Pandya's relabelled N and reject a mutation.
- 12:03 the C LRAT checker was too strict: it rejected hints already satisfied, which CaDiCaL emits. A second
  checker, `code/lratcheck_py.py`, written independently, agrees on the diagnosis. Both now skip satisfied hints,
  which is sound. All 16 large-t proofs re-verified.
- 12:08:10 (mtime) **FROZEN `review/SUPPORT_LOWER42.r2.md`**, SHA-256
  1db90164f6de13cad9211a2e79b3b75c0c604239b5037b44f9a2f072f0bd1418. Codex and Claude fixes applied; the proof no
  longer depends on the machine checks. New cross-check `code/verify_lower42_r2.py` (9be67daf…4125). r1 unchanged.
- 12:13 **sympy 1.14 `lpmax` bug.** It returned optimum 1 (instead of 1/2) for max e s.t. x ≥ e, y ≥ e, x + y = 1.
  The moduli-LP check is removed from the engine's exclusion logic. An audit shows that no exclusion so far relied
  on it. Reports will be regenerated with the fixed engine before any freeze.
- 12:09 background batches of engine cases started: (28,0), (28,2), (29,3), (30,4) and (26,0), (27,2), (28,3),
  (29,4), (30,5). In draft: `review/drafts/SUPPORT_LOWER46.r1.DRAFT.md` (s ≥ 46 = LOWER42 r2 lemmas + Lemma 12 slice
  values + Lemma 13 (t = 31) + Lemma 14 closure + Lemma 15 no-AME(4,2) shadow proof + Lemma 16 (t = 32, any e) +
  engine certificates for (30,0), (30,2), (30,3), (29,2), (28,0)).
- 12:23:46 LRAT checker soundness tests (parent's request: N1–N4, P1, plus N5–N7 and P2) pass for both checkers
  (`evidence/lrat_soundness_tests.json` e9e06466…4230).
- 12:25 moduli exclusion is now possible only through an exactly verified Stiemke certificate (Aᵀw ≥ 0, bᵀw ≤ 0,
  (Aᵀw ≠ 0 or bᵀw < 0)). Controls, including the intended-reason negative Aᵀw = 0, bᵀw = 0, pass
  (`evidence/moduli_cert_tests.json` 9b682748…ca91). Engine code `code/large_t_gen.py` is now 28c0c1f9…bcfd.
- 12:25–12:35 regenerated with the final engine: (30,0), (30,2), (30,3), (29,2) and (28,0), all excluded. The e = 0
  cross-check engine also excludes (30,0) and (28,0). Batch A (older engine code) found (28,2), (29,3) and (30,4)
  excluded; these will be regenerated. Batch B, (26,0) and later cases, is still running.
- 12:35:20 `code/lower46_receipt.py` running. It re-checks every CNF/LRAT pair with both checkers and records
  satisfied-hint counts.
- **12:39 RESOURCE VIOLATION (recorded prominently).** The (26,0) run of `code/large_t_gen.py` (frozen engine
  28c0c1f9…) on profile {5,5}{2,2,2,2,2}³ materialised whole orbits of a symmetry group of order 20,736,000. Its
  orbit-blocking CNF grew to 1.96 GB, and the Python process reached about 35 GiB RSS (ps 36,567,968 KiB), far above
  the 8 GiB lane cap.
  - It was stopped with SIGTERM at 12:39:39 and exited cleanly (exit 143, no SIGKILL).
  - **(26,0) outcome: UNKNOWN.**
  - Batch B then ran (27,2), excluded with older code. (28,3) was stopped with SIGTERM at 12:45:56 for disk, outcome
    UNKNOWN. (29,4) and (30,5) were excluded with older code. All older-code results are uncertified, and are not
    claims.
  - Parent instruction: pause every search that materialises whole orbits until a resource guard is frozen.
- 12:48:31 exact byte accounting.
  - Lane apparent size 9,289,539,849 B, du 9,334,255,616 B.
  - Cap 10 GiB = 10,737,418,240 B, minus 256 MiB headroom, leaves 1,134,727,168 B for any new writes (computed with
    du).
  - Parent decision: option (c), no cap increase, no deletion, gzip or moving. Proof-free exploration counts as
    UNKNOWN until certified.
- 13:01:16 FROZEN `review/ENGINE_V2_GUARD.r1.md` (d5733a73…73fd).
  - Engine v2 is the new file `code/large_t_lex.py` (cde05b00…12b8); the frozen engine 28c0c1f9… is untouched.
  - Lex-leader generators replace orbit materialisation.
  - Guard: pre-bounds; RSS watchdog at 6 GiB (SIGTERM only); exact disk accounting; a solution cap; CaDiCaL -t.
  - CNFs go on stdin. Proofs are gzip LRAT streams, checked through a FIFO and a pipe.
  - Smoke S1–S9 all match: `evidence/guard_smoke.json` 3c4ea4e6…db46.
  - Hashes sent to the parent. The parent's 18-pair drat-trim recheck is running, so this lane is held at ≤2 CPU.
- 13:02:03–13:02:24 v2 proof mode, released for small already-bounded cases: (29,3), (30,4), (28,2), (29,4), (30,5),
  (27,2), (28,3) all EXCLUDED, no guard trips.
- 13:03:28–13:22:25 (26,0) v2 exploration, parent-released: EXCLUDED-EXPLORATION, 1695 solutions.
- 13:24:12–13:43:48 (26,0) v2 proof mode, parent-approved: EXCLUDED. Peak RSS 930 MiB; 37,787,960 B of gz streams; the
  12e9 free floor was never crossed.
- 13:26:42 `evidence/lower46_phase_certificates.json` (94dc8db5…cd63): 24/24 explicit LOWER46 phase certificates
  verified.
- 13:44:00–13:45:04 receipt `evidence/v2_receipt_r2.json` (bf05ec21…a5fa) over the 8 v2 cases: all_required_true.
  131 streams, 1619 stored phase certificates, controls rejected.
- **13:47:22 FROZEN `review/SUPPORT_LOWER48.r1.md`** (0457570502535eb3bb6aaa8002f81ca640451c8364079c9e0f4cc9413fb49f95):
  s ≥ 48, CANDIDATE.
  - Lemma 17 (officer counting) and Lemma 18 (the parent's binary code) are load-bearing there.
  - Parent note: the §3 wording "each generator is a CNF symmetry" is too strong. It is to be replaced in r2 by the
    genuine-support argument.
- 13:49:36 FROZEN `review/ENGINE_V3.r1.md` (fd7c7447…4449); v3 is `code/large_t_lex3.py` (139681a2…37e0). Smoke
  T1–T8, U1 and U2 match. The spec repeats one bullet in §4 (cosmetic).
- 13:51:01 FROZEN `README.AMENDMENT-1.md` (47f8e5c1…d061): proof-free exploration of (30,6), (29,5), (28,4),
  (27,3), (26,2), (24,0) under v3. Started 13:51.
- LOWER46 r2 draft (`review/drafts/SUPPORT_LOWER46.r2.md`) awaits the Claude review note. Its dependency chain stays
  identical to r1, as the parent required.
- 13:51–13:52:43 amendment-1 exploration, not certificates: (30,6), (29,5), (28,4), (27,3) and (26,2) all
  EXCLUDED-EXPLORATION.
- **(24,0): stopped manually with SIGTERM at 14:19:14; outcome UNKNOWN.** Profile 0, {6,6}{2⁶}³ (|H| = 4.5e9),
  had yielded 980 lex-leader solutions in 26 minutes without finishing. Probes show that most other (24,0) profiles
  enumerate in seconds. The difficulty is concentrated in the high-symmetry {6,·}{2⁶}³ profiles.
- **14:12:01 FROZEN `review/SUPPORT_LOWER46.r2.md`** (fac5242b90554de86cd6bd8e17fb2a6800fbd4a3e71d2e4a99f154d5a216f35b):
  correction-only, with dispositions for the Codex and Claude reviews. The parent's delta check PASSED, and
  **s ≥ 46 is CORRECTNESS-ACCEPTED** (partial), per `review/ame46-lower46-parent-verdict.md`.
- 14:16:05 FROZEN `review/ENGINE_V2_GUARD.erratum-1.md` (6cb1fd8c…ab65).
- **14:16:50 FROZEN `review/SUPPORT_LOWER48.r2.md`** (70daac01707158b2842159dbdc6713afa33e541c51f100a91034fdf4d432f60e):
  the realizable-support completeness argument, P1–P5 and the lex schema, with the 37 load-bearing streams named.
  The parent's replay PASSED. The verdict is pending.
- 14:20– method experiments for the hard (24,0) profiles (`code/exp_symbreak.py`, `code/exp_joint.py`), exploration
  only.
- **14:4x parent: s ≥ 48 CORRECTNESS-ACCEPTED** (partial), per `review/ame46-lower48-parent-verdict.md`.
- 15:13 **VOID** exploration run (`exp_triangle.py` with a broken filter emitted unsound clauses; recorded in LOG). It
  is distinct from all v4 evidence.
- 15:33:10 FROZEN `review/ENGINE_V4.r1.md` (fd1d47f2…8c12).
  - Engine v4 is `code/large_t_joint4.py` (42d6e510…26a9): the joint officer model J, and the e = 0 doubled-triangle
    clauses W (Lemma 20, written).
  - Controls `evidence/guard_smoke4.json` (e0eff74b…e208), all true. Pandya's genuine state satisfies J+W.
- 15:33:22 FROZEN `README.AMENDMENT-2.md` (31be56f5…aa56); (24,0) v4 exploration started.
- 15:37:22 FROZEN `review/V4_PROOF_SCHEMA.r1.md` (f558e75b…b986).
- Parent bound the W generator: PASS. The Codex v4 review is ACCEPT-WITH-FIXES: Lemmas 19 and 20 accepted; an engine
  M1 issue in non-joint proof mode; m1, m2. Fixes are being prepared in the new file `code/large_t_joint5.py`
  (unfrozen; it waits for the Claude review).
- 15:46 (24,0) progress: 75 of 158 profiles done. Profile 0 {6,6}{2⁶}³ has 42 solutions, all phase-excluded, in
  412 s; the rest have none so far. No candidate.
- 15:57:41 (24,0) v4 exploration finished EXCLUDED-EXPLORATION (`evidence/large_t_joint4_t24_e0_explore.json`
  b2887b51…ba1f).
  - 158 profiles; 42 solutions, all in profile 0 and all phase-excluded; no candidate, no trip.
  - Not a certificate. All s ≥ 49 cases are now EXCLUDED-EXPLORATION: (24,0), (26,2), (27,3), (28,4), (30,6), plus
    (29,5) by Lemma 17.
- 15:59:07 FROZEN `review/ENGINE_V5.r1.md` (5393238f…bf0a); v5 `code/large_t_joint5.py` (e57067c2…33f8).
  - All Codex and Claude v4 review items are dispositioned.
  - Controls K1–K7 are true (`evidence/guard_smoke5.json` 1d9c3cb0…a0).
  - Proof-mode go for s ≥ 49 requested with resource estimates.
- 16:00:48 v5 proof-mode smoke on the certified (30,0) and `code/v5_receipt.py` replay: EXCLUDED, receipt
  all_required_true. Control only, not a new case.
- 16:02 parent GO for v5 proof mode on the s = 48 layer: (30,6), (28,4), (27,3), (26,2), then (24,0) with
  `--triangles`. Started 16:0x with `code/run_chunk5.sh` (one chunk at a time).
- **Scaling projection (16:05).** Cases remaining per layer after the written exclusions (t ≥ 31, e = 1, e = 0 with t
  odd, t = 29 by Lemma 17), with live profile counts after Lemma 17 and the largest product space P:
  - s = 49: (25,2) 21 live, P 625; (26,3) 24, P 625; (27,4) 3, P 256; (28,5) 5, P 256; (30,7) 1, P 81. This is small,
    comparable to the s = 48 e > 0 cases (seconds to minutes each in exploration). Projection: under 30 min in
    exploration and about 1 h with proofs.
  - s = 50 adds (22,0), 345 live, h = 14, P 1296, and (24,2), 153 live, P 1296. (22,0) is the (24,0) analogue with
    |N| = 28; projected at least 1–3 h in exploration. (24,2) has no triangle family, since e > 0, and the
    {6,6}{2⁶}³ analogue may be slow.
  - s = 51–59: each layer adds cases with h = 13–22 and 102–5,420 live profiles per case (e.g. s = 59: (15,2) 4,232
    live, (16,3) 4,136, (17,4) 2,675, …). All have P = 1296 and |N| up to about 46. Projection: days at least.
  - **Conclusion:** the lower-bound route cannot reach 60 by 18:31. The reachable targets are s ≥ 49 (this GO) and
    possibly s ≥ 50. A witness with s ≤ 59 would need t ≥ 13; the earlier t = 14 full-model SAT runs were UNKNOWN at
    1800 s, and no witness search is planned without a parent decision.
  - **Correction (16:1x):** the deadline is 2026-10-18 18:31:43 PDT, i.e. tomorrow, not today at 18:31 as the
    16:05 conclusion implied. The conclusion stands: s = 51–59 needs days. The parent agrees that the frozen gate
    (a witness with s ≤ 59, or a bound of 60) is not reachable by these routes before the deadline. Parent decision
    (a): after (24,0), proof-free v5 exploration of the s = 49 layer under a new amendment; s = 50 is not started.
- 16:02–16:03:4x **v5 proof mode, s = 48 layer, e > 0: (30,6), (28,4), (27,3), (26,2) all EXCLUDED** (worker
  evidence), guard_tripped null. Zero recorded Y: every enumerated profile is UNSAT under J at the first solve.
  - Receipt `evidence/v5_receipt_s48_e_pos.json` (fa0bcf45…e4ee9), all_required_true.
  - Two (26,2) streams fail strict mode (5 satisfied hints).
- 16:11:37 FROZEN `review/V4_PROOF_SCHEMA.r2.md` (ef692d9d…c9309), after Codex v5 delta MAJOR M1. r1 had stated the
  wrong pair order: the base and the linking use BPAIRS = [01,23,02,13,03,12], the officer CNF uses sorted SPAIRS.
  `code/schema_regen_check.py` (2b9382b0…0a06) regenerated all 34 final CNFs (the four e > 0 cases and the (30,0) W
  smoke) from the r2 text: 34/34 MATCH, at 16:22:41.
- **16:04:48–16:21:57 (24,0) v5 proof run: UNKNOWN.** The disk guard tripped: 534,205,150 B written plus a growing
  stream exceeded the 512 MiB budget. 16 of 158 profiles were reported; profile 0's proof alone is 471,421,610 B gz.
  - Lane at 16:22: 9,949,798,400 B, so 519,184,384 B remain under the cap.
  - The full (24,0) proof (≈1.2 GB of text LRAT) cannot fit. **s ≥ 49 is blocked under the current caps.** Options
    (DRAT format, cap exception, stop at s ≥ 48) have been sent to the parent.
- 16:22:57 FROZEN `README.AMENDMENT-3.md` (0ef73324…a6d); proof-free v5 exploration of the s = 49 layer started.
  - Results, not certificates: (30,7), (28,5), (27,4) EXCLUDED-EXPLORATION.
  - **Parent decision (i), 16:2x:** stop the bound at s ≥ 48, with no further proof runs and no s = 49 exploration.
    (26,3) and (25,2) were stopped with SIGTERM at 16:23:2x and wrote no reports (not run / UNKNOWN).
  - Incident: the SIGTERM sent to stop the outer loop also hit its parent PID 61118, the tool's job runner for that
    background job. That job ended with exit 143; nothing else was affected.
- 16:25:03 FROZEN `review/ENGINE_V6.r1.md` (7c997fc8…eb68).
  - v6 is `code/large_t_joint6.py` (37925573…a5d) with `code/lratcheck_py2.py` (f2fdf578…f8e).
  - Controls `evidence/guard_smoke6.json` (94b7daad…365), all true. v6 is unused for proofs.
  - The unfrozen LOWER49 draft was moved to `archive/SUPPORT_LOWER49.r1.DRAFT-unfrozen-not-claimed.md`. s ≥ 49 is
    not claimed.

## 2. Lane status and handoff (16:25, compute stopped)

**Accepted results (parent verdicts):**
- s ≥ 42 (`review/SUPPORT_LOWER42.r2.md`);
- s ≥ 46 (`review/SUPPORT_LOWER46.r2.md`, fac5242b…f35b);
- s ≥ 48 (`review/SUPPORT_LOWER48.r2.md`, 70daac01…f60e).

These are lower bounds on the support of every AME(4,6) state in every product orthonormal basis. With Pandya's
upper bound of 60, the open range is 48..60. The contract's gate (a witness with s ≤ 59, or a proof of s ≥ 60) is not
reached. No novelty claim.

**Written lemmas beyond L48:**
- **Lemma 19** (officer placement; `review/ENGINE_V3.r1.md` §3);
- **J** (a hole line holds no officer, for every e);
- **Lemma 20** (doubled triangles, e = 0; `review/ENGINE_V4.r1.md` §4);
- the realizable-support completeness argument.

The Codex and Claude v4 reviews accepted all four (ACCEPT-WITH-FIXES, mathematics accepted). The parent bound the W
generator independently.

**Engines:**
- v2 is frozen (orbit-free lex-leader, guard): `review/ENGINE_V2_GUARD.r1.md`, with erratum 1.
- v3: Lemma 17 and 19 pre-filters, stored certificates.
- v4: J and W.
- v5: review fixes and asserted bindings.
- v6: Codex v5 delta fixes.
- The exact final-CNF text is `review/V4_PROOF_SCHEMA.r2.md`, validated 34/34 by `code/schema_regen_check.py`.
- Each version has a frozen spec and controls (`evidence/guard_smoke{,3,4,5,6}.json`).

**The s = 48 layer** (needed for s ≥ 49):
- (30,6), (28,4), (27,3), (26,2): v5 proof mode EXCLUDED, worker evidence.
  - Receipt `evidence/v5_receipt_s48_e_pos.json` (fa0bcf45…e4ee9). There are zero recorded Y, and 33 final streams.
  - The parent's independent replay was in progress at 16:2x.
- (29,5): excluded by L48 Lemma 17.
- (24,0): exploration EXCLUDED-EXPLORATION (`evidence/large_t_joint4_t24_e0_explore.json`, b2887b51…ba1f; 42 Y, all
  phase-excluded). The proof run is UNKNOWN (disk guard; profile 0 alone is 471 MB gz of text LRAT).
  - The full case would need ≈1.2 GB, against 519 MB left in the lane.
  - The 16 partial streams are kept in `explore/large_t_joint5/` and are not a certificate.

**What a future certification of s ≥ 49 would need:**
1. A proof format that fits the data budget. Option (ii) is DRAT without hints, since the parent's load-bearing route
   is additions-only RUP anyway. It is untested; profile 0 would need to be measured first under a hard byte cap.
   Other routes: a fresh lane with its own data budget, or a written exclusion of profile {6,6}{2⁶}³ at t = 24
   (it has only 42 Y, all phase-excluded, but its UNSAT proof is large).
2. The parent's replay of the four e > 0 cases and of (24,0) against `review/V4_PROOF_SCHEMA.r2.md`, with
   additions-only RUP, the 42 phase certificates checked with closure, and profile completeness.
3. Proof runs with v6, the engine with all review fixes.

**Beyond s ≥ 49:** see the 16:05 scaling projection in §1.
- s = 49 is small: (25,2), (26,3), (27,4), (28,5), (30,7).
- s = 50 adds (22,0) with 345 live profiles, and (24,2).
- s = 51–59 need 10²–10⁴ profiles per case at P = 1296. That is days of compute and well over the data budget for
  proofs. The lower-bound route cannot reach 60 by the deadline (2026-10-18 18:31:43 PDT).

**Data:** the lane holds ≈9.95e9 B under the 10 GiB cap (no deletion, as required). The largest items are the old
frozen-engine exploration CNFs and LRATs (`explore/large_t_gen` 4.7 GB) and the (24,0) partial streams (0.53 GB).
