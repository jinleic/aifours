# Lane log (host clock, PDT)

Time labels: HH:MM:SS = captured `date` output or file mtime; HH:MM = start-of-command `date` rounded down;
"~" = no separate receipt (bracketing receipts given).

- 2026-10-17 02:57 lane assigned; contract read (phys-2-dualunitary-ep15-16-contract.json).
- 03:00 sources fetched: arXiv 1912.12021, 2101.04580, 2205.08842v2 (curl; PDF mtimes 03:00:06–03:00:16); Rather
  thesis [62] chapter PDFs via managed browser (proof-of-work page; PDF mtimes 03:01:54–03:02:13), text extracted;
  U(θ) (3.36) read from the rendered page image. [Corrected: an earlier "03:06" fetch label was a guess.]
- README §0 frozen protocol written before any search: no separate receipt captured; README.md mtime
  2026-10-17T03:05:00-07:00, SHA-256 7d16a1d39b683869a98b8843c93b9ca59155124a029e0423b6392cfdf50370a7 (taken before
  the provenance edit). [Corrected: an earlier "03:2x" label was a guess and is withdrawn.]
- 03:05:55 code/controls_exact.py run (sympy exact): all controls as expected -> evidence/controls_exact.json.
- 03:07 code/explore_dim.py: rank J_dual = 119 (tangent 43) at random dual points and at U_s(2π/3); 129 at P9
  (tangent 33 = LU orbit); LU tangent rank 33 -> D/LU is (generically) 10-dimensional. evidence/explore_dim.json.
- 03:08 first ascent test (code/ascent.py): random dual starts converge in ~20 steps to e_p = 0.9375 with
  sv(U^Γ) = (√1.5)^6 0^3. MR-map outputs have rank U^Γ = 6 (most), 4 (some), 9 only for 2-unitaries.
- 03:10 code/explore_rank.py (evidence/explore_rank.json): at polished non-O9 dual points sigma_7(U^Γ) stays ~1e-16
  after Gauss–Newton-retracted tangent moves of size 1e-3..1e-1 (rank<=6 is an open condition on the 43-dim stratum);
  kernels of U^Γ (both sides) are 3-dim spaces of rank-2 matrices with no common null vector (skew type).
- ~03:13 (no receipt; between explore_rank start 03:10:09 and components launch 03:23:11) scratch: every unit vector
  in either kernel has Schmidt coefficients (1/√2,1/√2,0) and kernel projector
  marginals = I  ->  kernel = (u⊗v)Λ²(C³) with u,v unitary  ->  U is LU-equivalent to a self-dual gate (U^R = U).
  Self-dual set SD tangent dimension at U_s = 35 (35 + 33 − 25 = 43 consistent). All 9! permutations: dual
  permutations have rank P^Γ <= 5 (random enphasing <= 5) except the 72 2-unitary ones (rank 9).
- 03:23 code/explore_components.py launched, 4 workers, seeds 101-104 (OMP/VECLIB threads = 1).
- 03:27 interim: strata seen (tangent dim, rank U^Γ) = (43,6) main, (41,4), (45,4) singular?, (33,9)=O9.
  Ascent maxima: 15/16 on (43,6) from every start; 5/6 on (41,4); 1 only on O9. No candidate > 15/16.
- 03:35:25 components runs finished (174 records): no non-O9 rank>6; ascent maxima 15/16 (main), 5/6 (rank-4), 1 (O9).
- 03:36:04 code/explore_rank9_seeds.py launched (4 workers, seeds 201-204; T-dual / partially 2-unitarised / P9-far
  seeds); output mtimes 03:36:08–03:36:09: three apparent rank-8 points; code/scratch/repolish.py (mtime 03:39:33) and
  rank4proj.py (mtime 03:40:06): GN stalls at residual 4e-14 with sigma ~1.5e-7; rank-4 alternating projection reaches residual
  4e-16 within 3e-7 (one point exactly rank 4, two with sigma_5 <= 2e-9) -> artifacts near singular rank-4 points.
- ~03:45 (no receipt; review/REDUCTION.md mtime 03:45:01) reduction note v0 written. Parent provenance note received
  and applied (README §0 / LOG time labels corrected; see top of README §0).
- 03:52:37 code/seek_rank7.py launched (4 workers, seeds 301-304, 150 runs each, rewards sigma_7..9 under an
  e_p <= 0.99 barrier); finished before 03:59:19: 566 converged runs, ranks {6: 524, 4: 21, 9 (O9): 32}; 23 runs
  diverged (no conclusion); no non-O9 rank>6.
- 03:57:58 / 03:58:34 code/local_theorem_exact.py (sympy + mod-p ranks, p = 1e9+7): all certificates pass
  (A1, A3, det M = 3^17/4, rank J_dual(U_s) >= 119, rank dG|_V >= 73, dim T_LU = 33, rank (R-id)|T_LU >= 8;
  controls: rank J_dual(P9) = 129, SWAP = 81; A1 fails off V; A3 mutation fails) -> evidence/local_theorem_exact.json.
  review/LOCAL_THEOREM.md: Theorem L (D = LU·SD near U_s; e_p <= 15/16 there).
- code/scratch/controlled.py (file mtime 04:01:20; run right after): S·(controlled unitary) has tangent 45, rank U^Γ = 3.
  [An earlier "~04:05" label on this line was a guessed future time and is withdrawn.]
- 04:07:01 (script mtime) code/scratch/float_crosscheck_L.py (independent numpy path): det M = 32285040.75 = 3^17/4, (H_jU_s)^R = −H_jU_s to
  2e-16, rank (R−id)|T_LU = 8, A1 residual 1e-14 — agrees with the exact certificates.
- 04:06:20 (json mtime) code/enphased_perms_exact.py (stdlib, exact combinatorics) -> evidence/enphased_perms_exact.json: 8784 dual
  permutations, 72 two-unitary; all others have term rank of supp P^Γ <= 5 => enphased e_p <= 9/10 (Prop. P).
- 04:08:28–04:10:41 (script mtimes) code/scratch/nf_survey.py, nf_survey2.py, nf_survey3.py (Newton-polished max-overlap normal forms): every normal
  form of P9 has N_0 = R_0 = 0 and complementary A,B; every normal form of non-O9 points (main, rank-4, S·controlled)
  has N_0 != 0 and A = B; main stratum: span{N_1,N_2} = span{Q_1,Q_2}, rank N = rank L = 2, rank ρ_14 = 6.
  Recorded as conjectural Lemma N in review/REDUCTION.md §5.
- 04:11:38 cycle-1 checkpoint: README §1, review/REDUCTION.md v1, review/LOCAL_THEOREM.md v1, evidence/SHA256SUMS.txt.

## Chunk 2 (parent IRC: Lemma R via the normal form; Theorem L replay; first captured host time 04:16:20)

- 04:16:20–04:35:56 (captured `date` outputs) normal-form exploration: code/scratch/tensor_rank_test2.py (mtime
  04:22:16; 300/300 random instances rank ≤ 2), generic_case_check.py / generic_case_check2.py (04:26:58 / 04:27:39;
  Lemma N1/N1' residuals ~1e-16, rB = rP = 2, rank M = 6), degenerate_omega.py (04:31:23; the Ω-system alone is
  solvable when N_0 = sI, so border relations are needed). review/LEMMA_R_NORMAL_FORM.md v1: cases G, S proved, R* open.
- code/nf_case_survey.py (mtime 04:35:25), 4 workers, seeds 401–404; outputs evidence/search/nfcases_40[1-4].jsonl/.log
  (mtimes 04:36:00–04:36:05; all finished by 04:38:03): 120 points / ~3,600 normal forms. Rank-6 points (MR, MR-ascent
  incl. points at e_p = 15/16, U_s(θ)): all case G. Rank-3/4 (controlled, S·diag, rank-4 MR): all case S. P9 and other
  2-unitaries: all R*. R* at non-2-unitary points: 0.
- 04:43:42 code/scratch/relations_check.py: every relation used, float residual ≤ 3e-15 on normal forms of main, rank-4,
  controlled and P9 points.
- 04:46:12 review/LEMMA_R_PROOF.md v1 (candidate full proof: Props A*, B* close R*), SHA at that time
  263f9df93c9af72aec1588fb072e27ba56d0fb62d39bee6a02813a7a914fa6a8; candidate message sent to Main right after.
- 04:47:29 code/relations_exact.py -> evidence/relations_exact.json: 30/30 relations are exact block identities of the
  biunitarity equations (56 free entries + formal conjugates).
- 04:50:02–04:50:03 code/replay_theorem_L.py + evidence/theorem_L_manifest.json: single-command replay of Theorem L,
  25/25 checks, regenerated output byte-identical (f1a73297…7264); receipt
  evidence/replay/theorem_L-20261017T045002-0700/receipt.json. review/LOCAL_THEOREM.md (mtime 04:50:33): replay
  section + exact meaning of "local maximiser" (on D, on D/LU, non-strict).
- 04:51:57 code/lemma_T_exact.py -> evidence/lemma_T_exact.json: Lemma T / Lemma N1 algebra exact, all true
  (control without hypothesis: rank 4).
- 04:53:46–04:54:20 (mtimes) README §1, review/REDUCTION.md, review/LEMMA_R_NORMAL_FORM.md status notes;
  review/LEMMA_R_PROOF.md edited after the v1 message (exact-check citations, a self-contained proof replacing the
  bare citation of Fact K, status wording; the case analysis §§2–5 is unchanged). Current SHAs: evidence/SHA256SUMS.txt.
- 04:56:53 / 04:57:17 code/case_algebra_exact.py -> evidence/case_algebra_exact.json (second run after replacing a
  vacuous placeholder check by the PP†/𝐁𝐁† computation): computational steps of Props A*/B* exact, all true.
  LEMMA_R_PROOF.md §6/status and README §1 updated to cite it; theorem statement now points to REDUCTION.md §3 for
  the T-dual transfer.
- 04:59:35–04:59:37 final control run after code stabilised: relations_exact.py (30/30 true; 3 mutation controls
  rejected), case_algebra_exact.py (all true; 2 controls behave as required), lemma_T_exact.py (all_ok). No background
  processes left running.

### Parent IRC (received after 04:59:37): reviews of v1; request for a frozen r2

- Parent: generic branch ACCEPT-WITH-FIXES, with two fixes: (F1) the Fact K complement/right-multiplier wording, and
  (F2) the REDUCTION line-12 marginal identity. Residual A*/B*/S/assembly ACCEPT. The parent's exact relation
  re-derivation agrees.
- Provenance note: review/LEMMA_R_PROOF.md had been edited in place after the 04:46:12 v1 message, giving
  a05e563b…2f7c (pinned by the parent as inputs-v2). That file is left unchanged from now on.
- 05:03:39 primary Fact K sources downloaded (public arXiv PDFs, read-only use): sources/quant-ph-0101003v2.pdf
  (Ruskai–Szarek–Werner; 85ef009e…65cd) and sources/quant-ph-9911079v1.pdf (King–Ruskai; a709d13e…f43b), plus their
  pdftotext -layout files.
- 05:04:59 code/marginal_identity_exact.py -> evidence/marginal_identity_exact.json: 9ρ_14 = MM† = (U^Γ†U^Γ)^T and
  U^ΓU^Γ† = Π(M†M)^TΠ^T hold as polynomial identities; the wrong form MM† = (U^ΓU^Γ†)^T is rejected.
- 05:05:09 byte-exact v1 copies placed in the lane (cp -p from the parent pin dualunitary-rank-bound-parent-inputs-v1, so
  the file mtimes show 04:52:33): review/LEMMA_R_PROOF.v1.md (263f…a6a8), review/LEMMA_R_NORMAL_FORM.v1.md (37fb…e587),
  review/REDUCTION.v1.md (8190…df80).
- 05:06:28 (captured) to 05:09:26 (mtime) review/LEMMA_R_PROOF.r2.md written and FROZEN.
  SHA-256 c8e62cba20241fae36b5405cba5c4c19c4b02fab7aecbb5fcf1c837ecb3e4284.
  - It applies F1 and F2, adds a self-contained Theorem A, T-dual transfer, Fact K derivation and quoted primary
    sources, the exact verification record, and errata for v1 and REDUCTION.
  - Before the hash was taken, three pre-freeze corrections were made in the same session: a hash abbreviation,
    "(M†M)^T = 9ρ_23", and the ε_j0 sign rule.
  - The case analysis is unchanged from v1. Per the parent instruction, no further numerics were run for relations
    already proved symbolically.

### Parent IRC (received before 05:22:31): Codex review of the interim text; request for a frozen r3 (bounded 45 min)

- 05:22:31 (captured) start. Inputs read: institute/…/review/qutrit-sharp-codex-hostile-review-v1.note.md (Codex
  gpt-6.1-sol, ACCEPT-WITH-FIXES; minors 1–4) and institute/…/review/qutrit-sharp-priority-audit.md.
- The thesis page was checked with `pdftotext -f N -l N` on sources/rather-thesis-2023/07_chapter3.pdf (05:25:32).
  Eq. (3.36) is on PDF page 16, printed footer 84. Eq. (3.37) and Conjecture 3.3.2 are on PDF page 17, footer 85.
  The parent's "p. 84" is therefore the page of (3.36); r3 quotes the conjecture with the footer-85 location.
- 05:24:18 code/witnesses_exact.py -> evidence/witnesses_exact.json. Exact over Q(√3) and Q(√6):
  - U_s(2π/3) and the Codex normal-form gate H are both unitary, self-dual and dual, with W² = (3/2)W, tr W = 9,
    tr W² = 27/2, rank 6, not 2-unitary, and e_p = 15/16.
  - H additionally satisfies H^ΓH^Γ† = (3/4)(I+S).
  - 5 mutation controls were rejected.
- 05:25:53 r3 seeded as a byte copy of r2 (cp; r2 untouched), then edited to 05:28:49 (mtime).
  review/LEMMA_R_PROOF.r3.md is FROZEN, SHA-256 ae42fcbb99247aaa453a2f05ddb5482226b910ba898af07c29fb81e4a03890ea.
  - Changes: §P quotes (thesis Conjecture 3.3.2 and the survey sentence), the precise T-dual statement (R2), the
    Rank Lemma with explicit pivot (R3), and the explicit witness tables (R4).
  - The case analysis is unchanged apart from citations of the Rank Lemma.
- 05:29:16 `witnesses_exact.py --check-doc review/LEMMA_R_PROOF.r3.md`: tables_match_and_certify = true (exit 0).
- 05:29:38 control: a copy with one token of 2U_s changed (evidence/replay/doccheck-control-20261017T0529/r3-mutated.md)
  gives tables_match_and_certify = false (exit 1). The r3 hash is unchanged.
- No new numerics were run for relations already proved symbolically.

### Parent IRC (received before 05:51:47): Claude complete r3 review; request for ONE final frozen r4 (bound 25 min)

- 05:51:47 (captured) start. Input read: institute/…/review/qutrit-sharp-claude-complete-r3-review-v1.note.md
  (Claude CLI claude-opus-5-5, ACCEPT-WITH-FIXES, 12 minor editorial findings, no missing case, no fatal or major issue).
- 05:52:37 r4 seeded as a byte copy of r3 (cp; r3 untouched, ae42fcbb…90ea). Edits E1–E12 were applied, mostly with
  the review's own text. Two small clarifications were added: "If dim A = 3" in the N1 application, and naming the first
  B* support pattern. Frozen at mtime 05:56:23. review/LEMMA_R_PROOF.r4.md SHA-256
  afd392daa38b9b8bccfded8d855bd72c1f1b824ab844a5f4c32c7db28d6659ed.
- 05:56:23 textual checks only, with no numerics, per the parent's instruction:
  - The 18 table lines (2Us[·], 4H[·]) of r3 and r4 are byte-identical (cmp).
  - `diff` of §§2–W between r3 and r4 shows only the E6, E7 and E8 additions.
  - Disclosure: the two table extracts were first written to /tmp (outside the repo, against the lane rule). At
    05:56:34 they were moved, not deleted, into evidence/replay/r4-table-diff-20261017T0556/. Both have SHA
    c5897e3b…26ed (identical).
- witnesses_exact.py --check-doc was not re-run for r4 (no new numerics); its r3 pass applies to the byte-identical
  tables.

### Parent IRC (received before 06:04:34): verdict

- Parent: the sharp 15/16 result is ACCEPTED (gate met), with r4 afd392da…59ed
  (institute/runs/six-lane-2026-10-16/review/qutrit-sharp-parent-verdict.md).
- Parent instruction: record the /tmp slip above in this lane log only, and make no further out-of-repo writes;
  use lane-local directories. Lane closed; the next target runs in physics/evidence/six-lane-20261016/random7reg-colour/.

### Parent safety rule (received 06:28, all lanes): cooperative stops only; record past SIGKILLs

- Audit at 06:28:47 of past process stops in this lane:
  - The only subprocess call is code/replay_theorem_L.py, which uses subprocess.run with no timeout, so it has no
    SIGKILL path. Its run completed in 1.7 s.
  - Shell `timeout N` wrappers (coreutils, SIGTERM by default) were used on a few runs. None reached its limit.
  - The earlier explore_components launch, which wrote partial outputs up to 03:23, was stopped before the 03:23:11
    relaunch, and its partial outputs were moved to archive/aborted-0323/. How it was stopped was not recorded at the
    time, so a SIGKILL (for example a tool-level job kill) cannot be excluded.
  - No result was drawn from those partial outputs; the 03:23:11–03:35:25 relaunch is the evidence.
  - No other run was stopped. All other runs finished or were bounded by their own iteration limits ("diverged"
    runs in seek_rank7 are optimiser outcomes, not kills).
- This lane is closed, and no further runs will be made here.
