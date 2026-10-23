# RESULT v2: adds a parent-reported attribution-limits section only

Written 2026-10-18T01:48:33-07:00 PDT. Supersedes `RESULT.md` (sha `10b192149a4cca582452fbb00774297414bcae7bc97c3b81c29915f47299e634`, kept unchanged) only by adding the final section. The correctness content below is verbatim from v1.

---

# phase-type-complex3 hostile review desk - RESULT (Ph3HostileDesk)

Written 2026-10-18T01:46:36-07:00 PDT. **Status:** both delegated reviews returned. Their dispositions are advisory; this is not an
acceptance — the parent owns the gate. Scope is correctness only; no novelty statement. Per the parent's 01:29 notice,
nothing here calls the angle construction or any boundary case new.

## Outcome

| Reviewer (identity from receipts/logs) | Line 1 | Proof status | FATAL / MAJOR / MINOR |
|---|---|---|---|
| Codex `gpt-6.1-sol`, effort max, sandbox read-only (stderr header) | DISPOSITION: ACCEPT-WITH-FIXES | COMPLETE-NO-IMPORTS | 0 / 0 / 3 |
| Claude `claude-opus-5-5` (init model and modelUsage), effort max, tools [] | DISPOSITION: ACCEPT-WITH-FIXES | COMPLETE-NO-IMPORTS | 0 / 0 / 7 |
| Desk static audit (written before reading either note) | — | agrees: no gap found | 0 / 0 / 4 (+4 NIT) |

There are **no load-bearing findings.** Both reviewers, and the desk independently, judge the written argument a
complete proof of the frozen statement using ordinary background only (for all real a > c > 0, b > 0, the minimal PH
order of c(a²+b²)/((s+c)((s+a)²+b²)) is n* = min{n ≥ 3 : b ≤ (a−c)cot(π/n)}):
- Part A with Appendix A gives the lower bound for every PH representation; Appendix A replaces Theorem 6.
- Part B, n ≥ 3, gives the construction; its n = 3 branch replaces Theorem 14.

If one uses the imported Theorems 6 and 14 instead, their printed hypotheses hold, except that Theorem 14's
"Consider a PH-distribution" is never discharged on its own (F1). That point is not load-bearing.

## Per question (Codex / Claude / desk)

| Q | Codex | Claude | Desk |
|---|---|---|---|
| Q1 | OK | OK-WITH-MINOR (F2) | OK (F2 scope wording; F10, F11 nits) |
| Q2 | OK | OK-WITH-MINOR (F7 notation) | OK |
| Q3 | OK | OK | OK |
| Q4 | OK | OK | OK |
| Q5 | OK | OK | OK (F9 nit) |
| Q6 | OK-WITH-MINOR (F1) | OK-WITH-MINOR (F1) | OK-WITH-MINOR (F1, F8) |
| Q7 | OK-WITH-MINOR (F3, F4) | OK-WITH-MINOR (F3-F6) | OK-WITH-MINOR (F3 resolved by mtime, F5) |
| Q8 | OK | OK | OK |

What the desk checked on each topic:
- **Q2.** The lower bound is checked on:
  - trimming of unreachable states;
  - the exclusion of never-absorbing states (Hurwitz);
  - the Perron left-vector argument for s(T_RR) = −c. This needs no matrix irreducibility; realization irreducibility is certified only in the paper's graph sense.
  - Theorem 6 applicability;
  - every step of Appendix A: the tangent-cone orientation, the law-of-sines product, the monotonicity range, Jensen, and the reducible case.
- **Q3.** The IVT bands are checked, including t₀ = 2φ for n = 3 and t₀ = 0 for n ≥ 4, strictness θ₁ > 0, equality at the upper endpoint, and the lower endpoint assigned to n − 1.
- **Q4.** The cycle determinant, divisibility, the Perron root and the resolvent orientation are checked. The cancelled roots of P are harmless (P(1) ≠ 0).
- **Q5.** The Chebyshev sign interval is checked for every n. So are B8 diagonal scaling, v₁ = 1 (so α = e₁) and the time rescaling.
- **Q8.** The n = 3 branch: t₀ = 2φ, P = 1, empty Taylor sum, t = (0, 0, K). All three reviews find this branch proves n* = 3 without Theorem 14.

## Consolidated findings (deduplicated; all non-load-bearing)

1. **[MINOR] F1** `target/ph3-theorem-v3.md:193-197 (also :12-13, :206-207)`. Sources: codex#1, claude#1, desk#1. Theorem 14 import (route (i) for n*=3) checks only the printed parameter domain and 1/q=F; its printed hypothesis "Consider a PH-distribution with Laplace transform 1/q(s)" is never discharged independently of Part B. Desk check: confirmed on p.577 (PDF13), primary/EXCERPTS.md E6. Correction: state that F is a PH Laplace transform for all a>c>0,b>0 (by Part B, or by O'Cinneide's characterization: density (c(a^2+b^2)/b) e^{-ct} int_0^t e^{-(a-c)u} sin(bu) du > 0 for t>0), or call route (i) an alternative basis given PH-ness.
2. **[MINOR] F2** `target/ph3-theorem-v3.md:205 (also :5)`. Sources: claude#2. "Conjecture 1 holds for the Eq. (42) family" lacks the domain qualifier; printed (42) has a,b,c>=0 while the theorem (v3:31) proves a>c>0, b>0. Desk check: confirmed (v3:31 vs v3:205; E6). Correction: write "for the Eq. (42) family with a>c>0, b>0"; optionally note b=0 is order 3 (three exponential phases in series) and b>0, a<=c is not PH.
3. **[MINOR] F3** `lane/receipts/pin-candidate-v1.json:3,33; lane/receipts/pin-candidate-v2.json:15; lane/README.md:110`. Sources: codex#2, claude#3. pin-v1 pinned_at 01:03:30 is later than d01 (01:03:00-01:03:18), contradicting "not yet run at pin time"/"post-pin". Desk check: pin-candidate-v1.json filesystem mtime = ctime = 2026-10-18T01:02:22 PDT, before d01 started; so the narrative order is right and the pinned_at label is forward-dated by ~68 s (pin-v2 label 01:06:00 vs mtime 01:05:55). No hash affected.. Correction: worker erratum/new pin version giving the actual write time; keep the narrative.
4. **[MINOR] F4** `target/ph3-theorem-v3.md:13; lane/receipts/pin-candidate-v2.json:12`. Sources: codex#3, claude#4. "Appendix B lists every run" but v3:250-256 omits p00-flint-probe (API probe). Desk check: confirmed. Correction: add p00 or say "every mathematical smoke run".
5. **[MINOR] F5** `target/ph3-theorem-v3.md:250-256; lane/receipts/pin-candidate-v1.json:39`. Sources: claude#5, desk#2, desk#3. Appendix B cites b01 next to b02 without its ALL_OK=false 88/98 status; the "ONLY absolute radius" explanation is not recorded in ball.json; the f01 cause (pivot threshold) is stated as fact although f01d records only the failing instance and f02 reaches max_n=29. Desk check: b01 flags are conjunctions contains(0) AND rad<2^-150 (code/ph3_ball_v1.py:58-61); containment of 0 is automatic for rigorous enclosures of exact identities [inference], so the radius conjunct failed; b02 112/112 with a relative test; d01 covers n=35.. Correction: write "b01 88/98 OK, 10 flagged by an absolute enclosure-width test, superseded by b02 112/112"; "f01 aborted (numerically singular at n*=35; attributed to the pivot threshold; d01 covers n=35)".
6. **[MINOR] F6** `target/ph3-theorem-v3.md:253-254, 258 (also README.md:107,110; pin-v2:12)`. Sources: claude#6. count wording: 1,605 = 38x42 (n=3..40) + 9 (n=64,100,128); "390 arrangements" = 195 distinct arrangements x 2 beta values. Desk check: confirmed from code/ph3_ball_dense_v1.py:3-4 and mutations2.json. Correction: state the decomposition explicitly.
7. **[MINOR] F7** `target/ph3-theorem-v3.md:214-222, 227`. Sources: claude#7, desk#6. Appendix A reuses symbols (r = Perron vector and time; w = eigenvector and dummy point; phi redefined; K, s, u, eps, p, C overloaded). Desk check: confirmed; meaning recoverable. Correction: tau for time, xi for the dummy point, phi_A in Appendix A.
8. **[MINOR] F8** `target/ph3-theorem-v3.md:13 vs :206-207 (v2:196-197)`. Sources: desk#4. "No mathematical step changed" is true of the steps, but the headline dependency changed from conditional (v2: Theorem 14; Theorem 6 if Appendix A unused) to "Imports: none are needed". Desk check: diff v2->v3. Correction: say explicitly that v3 strengthens the dependency claim using the existing Part B n=3 branch and Appendix A.
9. **[NIT] F9** `target/ph3-theorem-v3.md:174`. Sources: desk#5. B7 title "every exit positive" while t1=t2=0 (v3:167) Desk check: n/a. Correction: "every exit nonnegative; t3..tn > 0".
10. **[NIT] F10** `target/ph3-theorem-v3.md:26-27`. Sources: desk#7. "non-singular PH generator" in quotation marks is a paraphrase of p.567/p.568 Desk check: n/a. Correction: drop quotes or quote p.567.
11. **[NIT] F11** `target/ph3-theorem-v3.md:61-62`. Sources: desk#8. irreducibility cited from p.570 (positive realizations); the PH definition is p.568 (Neuts 1981); equivalent Desk check: n/a. Correction: cite both.

## Evidence honesty (Q7)

All pins and receipts agree with the outputs. Desk check: 61 hash bindings. Codex: 95/95 manifest hashes and 12
receipt chains. Claude: 90 bindings plus 118 code-hash entries.

Every count in the pins, README §7 and Appendix B matches the run outputs:
- e01 is 32/33. The E4 FAIL is reported as a simplifier miss everywhere and is explained by e02's three methods.
- b01 is 88/98, with 10 radius-flagged instances superseded by b02 112/112 (336 checks).
- d01 has 1,605 instances and 3,210 checks.
- f02 is 187/187.
- m01 core is 71/87. The per-type counts, positive controls, n*−1 and lower-endpoint results are as stated.
- m02: 15/15, 15/15, 90/90 and 10/10, plus 390 arrangement cases.
- s01 has 47,070 complex eigenvalues and 0 violations.

No document counts any of these as passing negative controls:
- b01's flags;
- the f01 abort;
- the ineffective all-exit-scaling mutation (0/15);
- the reorderings (0/24).

The defects are labels and wording only (F3–F6). The README's first 7,366 bytes still hash to the frozen sha, so only
log rows were appended. All finite runs are smoke and are not premises.

## Unresolved assumptions

- ordinary background only: Perron-Frobenius (reducible and primitive cases), Frobenius normal form, IVT, Jensen, Laplace transform of matrix exponentials, plane convexity/supporting line, law of sines, Chebyshev U generating function
- Theorem 14 route presupposes F is PH (F1); the no-import route does not need it
- faithfulness of the desk transcription primary/EXCERPTS.md: Claude relied on it without images; Codex states it compared against the page images but its stderr logs no image-tool event; the desk transcribed directly from the rendered pages
- scope: b=0 and the book p.544 general question are outside the statement; novelty not assessed (parent 01:29 notice: the spectral angle construction and the beta=1, n*=4 example are prior literature)
- not verified by anyone: internals of b02 eigen-enclosures and the "independent code path" claim for f02 (smoke only, non-load-bearing)

Several gaps Claude could not check (it had no tools) were resolved by the desk:
- README sections 1-6 unchanged: first 7,366 bytes of current README hash to frozen db34b018... (desk and Codex).
- b01 flag definition: code/ph3_ball_v1.py:58-61 conjunction contains(0) AND rad<2^-150 (desk).
- d01 band positions: code/ph3_ball_dense_v1.py:3-4: f=k/40 (k=1..40), 1e-3, 1e-9 for n=3..40; {1,1/2,1e-9} for n=64,100,128 (desk).
- f02 case composition: 160 random + 14 upper_endpoint + 13 just_above_lower = 187, 67 with density fields (desk).

## Delegation integrity

**Snapshot.** The snapshot was built from byte-identical copies (MANIFEST.json lists 95 files, about 4.9 MB). It
contains:
- target v3;
- reference v2;
- the contract;
- the pinned PDF;
- 6 rendered pages (PDF 3, 4, 6, 7, 10, 13 = printed pp. 567, 568, 570, 571, 574, 577) with their text layers;
- the desk transcription `primary/EXCERPTS.md`;
- the lane README, receipts, runs and code.

**Withheld from the snapshot and both prompts:** the parent derivation, the parent smoke, the untrusted candidate note, proof v1, and the screens. A marker scan of both prompts found none of them.

**Codex.** All 44 executed commands were static (nl, rg, cat, shasum, tail, diff, head), and every one ran with cwd
inside the snapshot. None used an interpreter, the network, or any path outside the snapshot. The provenance record
is `desk/codex-command-provenance.json`. Codex says it compared EXCERPTS.md against the page images, but its log
records no image-tool event, so that comparison is unverified.

**Claude.** One turn, no tool_use blocks, cost $3.40.

**Gates.** The disk gate passed before each launch: 15.64e9 bytes free at both the 01:24:43 and 01:24:52 checks,
against 12.203e9 required.

**Timing.** Codex ran 529 s (01:24:48–01:33:37) and Claude 1,051 s (01:24:57–01:42:27). There were no timeouts or
retries.

## Deviations

- target switched to v3/pin-v2 on parent instruction before launch (assignment named v2/pin-v1)
- added printed p.567 (PDF3: PH-generator, representation and order definitions) to the requested pages 568, 570, 571, 574, 577
- primary excerpts are a desk visual transcription (PDF text layer garbles math); page PNGs rendered by the desk with poppler pdftoppm/pdftotext (TMPDIR in desk)
- Claude prompt 207,517 bytes (all load-bearing sources inlined with LF numbering; Q7 data as receipts, stdout, small outputs and a selected extract of large outputs); returned in 1,051 s, no timeout
- Codex ran with cwd = review dir (runner -C); read confinement to the snapshot was by prompt only; command log shows 44/44 static commands inside the snapshot
- desk performed only hashing, JSON reading/counting and page rendering; no scientific rerun

## Files

- Desk: [/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/phase-type-complex3-hostile-v1](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/phase-type-complex3-hostile-v1): `RESULT.md`, `RESULT.json`, `DESK_LOG.jsonl`, `checkpoints/`, `desk/static-audit-v1.md`, `desk/codex-command-provenance.json`, `snapshot/` (with MANIFEST.json)
- Codex: [/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/phase-type-complex3-codex-v1.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/phase-type-complex3-codex-v1.note.md), sha `7cd3e9a524e539ae442dc41fbef9f3086624a51205162d4e7b6b36157232fff2`; receipt sha `5257740f7824b6fd0d470f912f509bd925e350b4be7d0974411c3f0d55cbf56d`; stderr sha `a38a1f7c1dd6eb0bef89d06176981053299f5c01cd5a6d98cf05813e5ba869c6`; prompt sha `72e2f4720060ad285c8a1cd34b5196e3d1ff9da2ef76e7e55bcd186dd763d1bd`
- Claude: [/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/phase-type-complex3-claude-v1.note.md](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/phase-type-complex3-claude-v1.note.md), sha `b869f4f63ac8a9ff0dea03fef55af398e13a767fa8c3c58841e06ea2cc597fa0`; receipt sha `d89cdc52be68359dda655d2f2c3dfa5eda2d0e738e18ec2864c467cbd7333c91`; stdout sha `5e2b08ffa8535afc6dce5ffbb2501a8e26880de4942653f23a9efd03c30a790c`; prompt sha `ee4b4c8def041dd2e0801658a7bf002895256043370950c4f189ef4d0407fccf`
- Pins are unchanged. No lane file was written.

## Attribution limits (parent-reported; added in v2)

The desk did not read these documents. It recomputed the sha256 of the two PDFs only, and it makes no novelty or priority determination.

- **Mocanu (1999) thesis.** `screening/phase-type-complex3-priority-parent-v2/mocanu-thesis.pdf`, sha `1d08aee2137c7a803de8ab90b6d63f7009409786fde8d04f045f7d0b5e8efef5`. The parent read rendered PDF pp.97–99 (printed pp.80–82) and reports:
  - Theorem 50 gives order n*+1 for the whole family.
  - Lemma 51 gives order n on every upper boundary β = cot(π/n).
  - Eq. 4.13, α_j = [sin((j+1)π/n) sin((j+2)π/n)/(sin(π/n) sin(2π/n))] w^j α_0, is the boundary version of the v3 B7 Chebyshev exit coefficients.
- **Kim (2016).** `screening/phase-type-complex3-priority-parent-v2/kim-hfcb2016.pdf`, sha `8c2c4ebc1058cbd97aaa3db1476967f6410a5e5c506fb6f9237eeeedd4ad1d3b`. The parent reports a numerical HFCB optimization in which tails may be needed (p.15, LF264), with no all-parameter n* guarantee.
- **Earlier notices (01:29).**
  - Verbeken–Ginis arXiv 2606.10143v2 (2026-09-14) publishes the spectral-only angle and eigenvalue-placement mechanism.
  - β = 1, n* = 4 is the Benvenuti–Farina 4-cycle example after shifting.

**Prior work, per the parent.** All of the following are prior:
- the uniform-boundary solution on every β = cot(π/n), with its trigonometric positivity mechanism;
- the n*+1 bound;
- the angle mechanism;
- the β = 1, n* = 4 example.

**The candidate delta, per the parent,** is only the off-boundary order-n* realization (cot(π/(n−1)) < β < cot(π/n)) with its exit-positivity proof, plus the assembled all-n statement. This desk does not establish that it is new.

**Wording consequence.** Do not call the angle construction, the boundary uniform cycle, the trigonometric or Chebyshev exit positivity, or any boundary case new.
- v3 makes no novelty claim (v3:4-5, :200, :242).
- v3:248-249 (Appendix B uniform-cycle remark) and v3:179 (B7 coefficients) coincide at the boundary with the thesis items above, per the parent.
- A write-up should therefore cite Mocanu (1999) Theorem 50, Lemma 51 and Eq. 4.13; Verbeken–Ginis (2026); Benvenuti–Farina; and Kim (2016) as numerical related work.

**Correctness is unaffected.** Pins, the delegated dispositions and the desk findings are unchanged.
