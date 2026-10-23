# Lane log (host clock, PDT, 2026-10-17)

## Setup
- 07:27 parent decision by IRC: χ7 r2 accepted, so freeze the χ8 target (v1 contract
  `screening/phys-2-random8reg-colour-contract.json`, 07:27:43).
- Parent preservation correction by IRC, received after 07:34:11 and before 07:34:31 (host clock). Replacement
  targets need their own directories. The χ8 work moves to this new lane; `random7reg-colour` becomes read-only
  prior input.
- Corrected contract r2: `screening/phys-2-random8reg-colour-contract-r2.json`, SHA dc451d82…46aa (host 07:34:36).
  A diff against v1 shows that only the lane path changed, plus the `prior_inputs_read_only` and `supersedes`
  fields. The target and acceptance are unchanged.
- **Superseded draft in the old lane, left unchanged.** `random7reg-colour/code/verify_chi8.py`, SHA-256
  9a400a5502acf312519efc5afbd9a039a14422bb0b9e83134a5bf8aa6ecd0cdc, mtime 07:34:11. It was written there before the
  correction arrived and was never run in that form; it is not used. No other χ8 file exists in the old lane.
- 07:34:37 created `random8reg-colour/` with `mkdir` (no -p; it refuses an existing directory), plus code/,
  evidence/, review/ and archive/.
- README §0 frozen protocol written after 07:34:37 and before the verifier run at 07:37:16, i.e. before the
  verifier and the proof.

## Priority kill check (contract item)
- 07:22:23–07:24:04 five web queries, recorded in the prior lane's LOG:
  - "random 8-regular" 4-colourable;
  - G_{n,8} / χ(G_{n,8});
  - 4-colourability threshold at d = 8, 9;
  - "8-regular" with {4, 5};
  - a recent-year query on small-degree colouring.
- Between 07:24:04 and 07:31:29, three more queries:
  - second moment for balanced colourings of random regular graphs, exact overlap optimisation, improvement beyond
    the Achlioptas–Naor bound at k = 4;
  - hypercontractivity / log-Sobolev treatments of the colouring second moment;
  - "(k−1)³" "log(k−1)" "k(k−2)" for the uniform model.
- Hits were already-known sources only: Shi–Wormald, AM04, KPW, Coja-Oghlan–Efthymiou–Hetterich (k ≥ k₀ only),
  the Kang–McDiarmid survey, Bykova, and Pérez-Giménez's 2012 talk slides (surfaced, not read). No statement of
  χ(G_{n,8}) = 4 for the uniform model was found.
- Access holes, as in the parent's χ7 audit: Semantic Scholar, Google Scholar, dblp, ScienceDirect.
- A miss is not novelty.

## Verifier
- 07:35–07:37 `code/verify_chi8.py` written. It is self-contained and reads nothing from other lanes. Sections:
  - A: (4, 8) arithmetic;
  - B: Lemma A, Proposition B and Theorem C identities and constants;
  - C: row-inequality Proof 2 in arb;
  - D: controls;
  - E: exact-count check of the exponent at M = I;
  - S: float sanity.
- One fake placeholder check was replaced by a real symbolic identity (E on a generic doubly stochastic matrix)
  before the run.
- 07:37:16–07:37:24 run → `evidence/verify_chi8.json` and `.stdout.txt`: all_required_true = true.
  - Constants: C_8 = 0.0147314817863750198…, κ = 0.0234376440031617555…
  - Proof 2: 8000 + 8000 pieces, 113 needing the centred form.
  - Exact-count gap at n = 120 is 0.0547.

## Proof
- 07:38–07:42 `review/PROOF_CHI8.r1.md` written. One precision edit (the ε′ bound in (I2)) was made before
  freezing.
- 07:42:34 (mtime) FROZEN r1, SHA-256 7ed7f8c865468326b307b2ce8fd93048cc5ceed807eb98503e7b1c32248a4c8a,
  525 lines. README §1 updated.
- No processes left running; nothing was stopped.

## Optional exploratory general-k check (after r1 froze; parent IRC: exploratory only, [INFERENCE])
- 07:45:22 created `explore/` (not part of the frozen target).
- 07:46:08–07:46:13 `explore/check_general_k.py` → `explore/check_general_k.json` (+ `.stdout.txt`). Results:
  - All identities are exact for k = 3…6.
  - (5, 12): a = 0.250304… > 1/4 (certain, via an exact partial sum showing e^12 > 11^5); κ = 0.0010228…;
    C_12 = 5.866e−4 > 0.
  - (H1) = 5; series ratio 11/16; Molloy–Reed 729/1024.
  - Control: d = 13 fails.
  - The route goes beyond NPG only for k = 3, 4, 5.
- `explore/GENERAL_K_LEAD.md` written: [INFERENCE] lead, no claim.

## r2 preparation (parent IRC: Codex ACCEPT; first Claude review timed out with no verdict; second Claude review
## running; priority audit received; prepare ONE r2, do not freeze before the Claude findings)
- Inputs read:
  - `institute/…/review/chi8-codex-hostile-review-v1.note.md`: ACCEPT, no fatal or major finding, no fix requested.
    Minor: KPW l.1251 at k = 3.
  - `chi8-priority-audit.md` (08:22:54): GSV/GSVY Φ formulation; AM04 §6 tightness counterpoint; CLMS "trick".
  - AM04 layout l.296–543 re-read (prior lane, read-only); KPW l.1236–1275 read.
- 08:35:43 created `sources/` (mkdir, no -p). Fetched arXiv GSV 1305.2902v3 and GSVY 1311.4839v3, plus layouts.
  SHA-256: GSV pdf 1539a5ec…a366, layout c24b8836…c5;
  GSVY pdf 54589174…352a, layout 6d2b5a7e…664a.
- 08:39:33 fetched CLMS 2009.10483v2 (pdf a8788f83…7dd8, layout a6a30f2a…9e).
- Read GSVY §§4–5 (l.499–775), and GSV §§2–3 (l.480–643) and §4.1 (l.729–833, Lemmas 4.9–4.12 by grep). Findings:
  - U(M) = Φ_1^{B⊗B}(M^{7/8});
  - GSVY map (20) sends M^{7/8} to M/4;
  - Ψ_8(M) = Ψ_1^{B⊗B}(M/4);
  - GSV/GSVY relate Φ and Ψ_1 only at critical points and through equality of maxima; no pointwise inequality was
    found in the parts read;
  - their matrix-norm route needs a bipartite or PSD (ferromagnetic) B, and B ⊗ B here is not PSD.
- 08:41–08:46 `code/verify_chi8_r2.py` written and run. Two failed attempts were fixed:
  - a fake unconditional True was removed;
  - a sympy branch issue in the weak-duality check was fixed by using w = e^{2c−1};
  - a sympy Boolean was cast to bool.
  Final run 08:46:11–08:46:12 → `evidence/verify_chi8_r2.json` (+ `.stdout.txt`), all_required_true = true:
  - F: AM04 marginals; (J+I)/2 gives 35/26 vs 5/4 and 17/78 vs 1/4; overestimate 0.0361835…;
  - G: KPW l.1251;
  - H: GSVY identification; eigenvalues of B ⊗ B are 9, −3 (×6), 1 (×9);
  - I: first-moment weak duality; exact E Z_3 control for n ≤ 60.
- 08:43:08–08:43:21 `explore/unconstrained_phi1.py` (floats, not evidence): the unconstrained sup of Φ_1^{B⊗B} at
  (4, 8) is attained at R ∝ 1 (396 of 400 BFGS starts), value U(J). So the overlap constraint is used by the proof
  method, not shown necessary.
- `review/drafts/PROOF_CHI8.r2.DRAFT.md` prepared (copied from r1 with `cp -n`, then edited). It is a working draft,
  NOT frozen. r1 is unchanged (7ed7f8c8…4c8a). The final r2 will be written to `review/PROOF_CHI8.r2.md` once the
  Claude findings arrive; the draft will then be retired to `archive/`.
- After 08:51:46, parent IRC: the framing is agreed. Keep the 16 per-cell constraints as the essential gain; do not
  assert that double stochasticity is necessary; floats are not a global-maximum proof; keep the draft unfrozen.
  Draft edits:
  - §2.1 item 2 now says Theorem C holds on all row-stochastic M, with an explicit no-necessity sentence;
  - the float observation is reworded ("not a global-maximum proof"; nothing claimed about the true unconstrained
    maximum);
  - §5.1 states S_2/S_1 = O(n^{199/2} exp(−C_8 ε² log² n/81));
  - §8 cites the parent's `chi8-parent-rational-arithmetic-v1.json` (SHA cc17d09d…63a9, 08:48:58) as parent
    evidence, not this worker's execution.
  Still waiting for the second Claude review. No processes running.

## r2 freeze (parent IRC: Claude v2 returned 08:50:47, ACCEPT-WITH-FIXES with seven editorial minors; apply them and
## freeze one final r2)
- Read `institute/…/review/chi8-claude-complete-review-v2.note.md`. Re-read KPW l.18–34 (abstract) and
  l.98–118 (Theorem 1): both use k smallest with d < 2(k−1) log(k−1), with χ ∈ {k−1, k}.
- 08:56:45–08:56:48 `verify_chi8_r2.py`, new section K (multiplier scaling identity; arb slack point values), all
  true. Family-1 slack at x = 29/100 is 2.3667e−4 and at 31/100 is 4.935e−4, against the certified piece minimum
  1.83e−6.
- 09:00:44–09:00:49 rerun with an exact check of KPW's H at (4, 8) added: eigenvalues 1/5 (×4), 4/5 (×4), 16/5 (×1);
  det 4⁶5⁻⁹. all_required_true = true. SHAs: script 1885293866…5f0e, json cb3fe9b0…11ab, stdout 27c11bf5…dece.
- Draft edits applied the seven Claude items (r2 §11, items 7–13) and the parent's conventions:
  - μ = c_0 + (7/8) ln m everywhere, with the pilot scaling stated explicitly;
  - u_*, supp M, c_0, c_row, K_b, c_KPW, c_1 and η introduced;
  - review appeals removed from the audit;
  - the analytic proof made primary and the interval argument supplementary;
  - the Theorem 10 sketched steps disclosed.
- One bash call that included rmdir was blocked by tool policy before it ran; nothing executed. It was rerun without
  rmdir.
- 09:01:28 (mtime) FROZEN `review/PROOF_CHI8.r2.md`, SHA-256
  055d295258dfe294b701f6e461684f82b7f8a9435a68d49ab52634d247644cb1, 836 lines (cp -n from the draft). The draft was
  moved with `mv -n` to `archive/PROOF_CHI8.r2.DRAFT-working-copy.md`. r1 is unchanged.

## r3 freeze (parent IRC: Codex delta review of r2 ACCEPT-WITH-FIXES; make r3 = r2 + exactly three editorial fixes)
- Read `institute/…/review/chi8-r2-delta-codex-review-v1.note.md`. Confirmed the parent's pinned r2
  (`chi8-parent-inputs-r2/PROOF_CHI8.r2.md`) has the same SHA as the lane r2 (055d2952…44cb1).
- Checked the fixes by hand:
  - β_e = b_e/n = d·y_e (GSVY: edges between classes = Δ y n);
  - M_{2/3} = J/3 + 2I/3 has rows (3/4, 1/12, 1/12, 1/12); the marginals 99/62 and 25/186 were re-derived;
  - E = 0 for the row-stochastic M with every row (1, 0, 0, 0), since no allowed pair lies within one column.
- 09:18:55 `cp -n` r2 → `review/drafts/PROOF_CHI8.r3.DRAFT.md`. Edits:
  - fix 1: AM04 §7 inference;
  - fix 2: β notation and the M_t definition;
  - fix 3: Theorem C domain;
  - §11 items 14–16;
  - title, supersession and status lines.
- 09:20:07 (mtime) FROZEN `review/PROOF_CHI8.r3.md`, SHA-256
  e7c506d0bcd75aad69ce004c4633ffa15e5a8ee64d90f53bf9c6867b95187e2d, 860 lines. `diff -u` r2 → r3 was saved to
  `evidence/r2-to-r3.diff` (f6d99375…e054): 6 hunks, +37/−13 lines, no other change. The draft was moved with
  `mv -n` to `archive/PROOF_CHI8.r3.DRAFT-working-copy.md`. r1 and r2 are unchanged. No verifier change.
- SHA and diff summary sent to Main. Per the parent, no new work: waiting for the χ8 verdict and the new χ12 contract
  (lane random12reg-colour/). No processes running.
