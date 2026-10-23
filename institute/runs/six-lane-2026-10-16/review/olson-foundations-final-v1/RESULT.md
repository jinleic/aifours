# Olson foundations (second-family gaps of RUNS assembly v4): RESULT (2026-10-18T02:23:30-07:00, host clock)

Desk: OlsonFoundationDesk (sub-agent, anthropic/claude-opus-5-5).  NOT a parent verdict, theorem acceptance or gate; parent
acceptance of these foundations, of U2-U10 and of any theorem stays separate.  Lane O was only read; every file below is new
(exclusive create).

## Bottom line

The Claude-side full check that R/olson-runs-assembly-proof-v4.md L249-252, L253-257 and L261-262 listed as missing now exists.
R/olson-foundations-claude-v1.note.md (sha256 a063bc6b6cbc9ea580857618165cc0fbe2e1a14cb160142095b4f5edf9e3a6f5) returns DISPOSITION: ACCEPT-WITH-FIXES with FATAL none, MAJOR none and six MINOR documentation
findings (m1-m6).  INV*-SEPARATE: YES; CIRCULARITY: NONE; FINITE-PREMISE: NONE.  Both gaps G1 and G2 are closed at the review level:
* G1: Lemma H/HW in full from GR/WAS, both directions;
* G2: the upstream imports of DR-Res/DR.
Each audited foundation now has a full check by both model families (Codex earlier, Claude here).  The only exceptions are the two
classical imports: EGZ (Codex matched only its uses) and the Davenport constant D(Z_p + Z_2p) = 3p - 1.  This changes no conclusion.
Conditional on (GC), on U2-U10 and on these foundations, the chain still ends at RGR-LONG(p) (every word of RGR_(4p-1)(p) is
solvable).  Ordered Olson OO(p) for D_(2p) is NOT established: Corollary DR' also needs INV*(p), and both halves are open
(obligations-after-PAR.md L54-56; invstar/results.md L69-71).

## 1. Pins and snapshot

* All 22 pinned files match their SHA-256: the seven foundation pins of the assignment; assembly v2 and v4; the continuation
  contract 9a362a94...0512; invstar/results.md 2273f4fe...31d8; v3, the GC verdict, both v2 audit notes and the RUNS/OR/R4/OBL/GC/C3
  imports.  Details in snapshot-manifest.json.
* snapshot/ holds 32 byte-identical text files (351,744 B; no CNF, DRAT/LRAT, binary or code).  Each manifest entry records sha256,
  bytes and lf_lines = len(text.split('\n')).
* The review packet R/olson-foundations-claude-v1.prompt.txt (sha256 a0400dc8b058af39d95b6ee1caafb3df653557b8edbde49bea12239fb1bf9c8c, 102297 B) LF-numbers excerpts of 14 of these files.

## 2. Reviewer identity and run

* Receipt R/olson-foundations-claude-v1.receipt.json (sha256 e9a83b367349ad083c4fa83be565580fe6e17cf82ab2f84041bc9d89342a69cb):
  * status NOTE_RETURNED_UNVERIFIED, returncode 0;
  * 1936.7 s, under the internal 2,400 s limit: no timeout, no SIGTERM, no retry.
* Requested model claude-opus-5-5, effort max.  The run reported:
  * init model claude-opus-5-5 with tools [] and permissionMode dontAsk (Claude Code 2.1.302);
  * modelUsage key claude-opus-5-5 (canonicalModel claude-opus-5-5, provider firstParty);
  * 0 tool_use events in 2 turns; result success with is_error false;
  * list cost $5.36.
* stdout.json sha256 8e4743653bb9a7ebede6d511c5669b4e22020d58a85db01c7246be5f53689d1e; stderr.txt is empty.
* Rate-limit events: the five-hour window was at 0.86, then 0.92 ("allowed_warning").  This is informational; the run completed.
* Vendor: the reviewer is the Claude family, the same vendor as this desk.  For these foundations the other family is Codex
  gpt-6.1-sol (earlier reviews).  The desk files below are Claude-family derivations, not independent evidence.

## 3. Per-foundation status

| foundation (file:L) | Codex coverage | Claude coverage | status after this audit |
|---|---|---|---|
| Lemma GR (proof-GR.md L21-61, fixes L110-113) | v2 audit full (codex note L302-309, L345) | claude-lemmaGR (fixes applied); this audit F1 full | VERIFIED, two-family |
| Lemma WAS (repr-WAS.md L16-22, L153-157) | v2 audit full | claude-DR-math (fix applied); this audit F1 | VERIFIED, two-family |
| Lemma HW (inverse-run-count/README.md L17-36) | KBH review item 2; v2 audit full (codex note L290-296) | this audit F1 full (C_max = 2m + 2h, floor/ceil end points of either parity, empty/full, k = 1, both directions) | VERIFIED, two-family; gap G1 closed |
| Lemma H with the 07:39 correction (proof-PAR-K0.md L18-44) | parity-k0-kplus review; v2 audit full | this audit F2 full (lambda, I(empty), "A, B <= 2p - 1 => [0 notin I(empty)] <=> min(A, B) <= kappa", kappa < 0, the p = 5 counterexample) | VERIFIED, two-family; gap G1 closed |
| OR/M0 transfers (Kplus-r2 L24-35; RUNS L366-375, L402-414) | v2 audit | v2 audit; this audit F3 (necessity on w, sufficiency on w~/w') | VERIFIED-WITH-FIXES (m5, wording) |
| Lemma EGZ (dihedral-partial L27-28) | uses matched only (v2 audit) | this audit F4 (two applications of classical EGZ with n = p) | classical import; application VERIFIED-WITH-FIXES (m1, a missing derivation sentence) |
| gap Theorem P (dihedral-partial L30-31; proof-theoremP.md) | codex-theoremP "correct", input sha 58a85ebe... = current file | this audit F5 full (the hypothesis forces F >= 2p - 1) | VERIFIED, two-family |
| marked formulation and Doubling (L17-25, L33-59) | codex-T0-R "correct"; Secs. 0-3 byte-equal to the reviewed input | this audit F6 full | VERIFIED-WITH-FIXES (m2, m3, wording; desk: m3 is not a gap, see record) |
| Davenport-alpha (L61-73) | codex-T0-R "correct with minor fixes" (F >= 2 applied) | this audit F7 full | VERIFIED-WITH-FIXES (m4: N <= 4p - 1 and the frame left unstated; its only use has N = 4p - 1); D(Z_p + Z_2p) = 3p - 1 is a classical import |
| Theorem DR-Res (proof-INV-reduction.md L19-37) | v2 audit, relative to the imports above | claude-DRRes (fixes applied); this audit F8 with the upstream lemmas inlined | VERIFIED-WITH-FIXES (m6: pair wrapping the end of the word) |
| Theorem DR, Corollary DR' (proof-DR.md L21-58) | v2 audit | claude-DR-math "correct"; this audit F9 | VERIFIED |

Use of INV_Res (F9, Q6) is VERIFIED:
* DR-Res needs, for in-run deletions of a length-(4p - 1) avoider: inherited avoiders in RGR_(4p-2)(p) with F, R >= 1 have k <= p
  and all runs odd.
* Corollary D of v4 (L202-203) supplies exactly that.
* Corollary E (L204-205) follows from it.
* INV*(p) enters only DR' (proof-DR.md L47-58).  Nothing inlined concerns words outside RGR.

## 4. Delta v2 -> v4 (desk check, delta-v2-v4-check-v1.md)

* The 26 diff hunks are wording, citation, status, review-record or hypothesis clarifications.  No theorem statement, branch split
  or applied hypothesis changed.
* Three hunks change a justification rather than wording.  The desk re-derived each by hand; all are correct:
  * the vacuous R^ >= 2p exit is removed (R^ = A^ <= 2p - 1);
  * C2 is re-justified without (P): K0 uses (P) only at L103; e_F = k - o_F >= 2; e_R = e_F (mod 2) for kappa = 0; and (P) is in any
    case automatic for k >= p;
  * a new, correct non-inherited B = 0 remark is added (L269-270).  No theorem uses it.
* v3 -> v4 is layout only, confirmed by a whitespace-token diff.
* The corrected GC scope was checked against ALL NMH hypotheses, not just Delta0 >= 3 and k >= 7.  The full list: all reflection runs
  odd, k >= p + 1, every run pure or a (1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p - 1, R <= 2p - 3.
  * Theorem A satisfies every one of them.
  * So does Theorem B's w^.
  * Documentation findings (non-load-bearing):
    * DC-1: v4 L122 still glosses Lemma GC with "only Delta0 >= 3 and k >= 7"; it should be read with erratum 5 of the GC verdict.
    * DC-2 to DC-5 are nits.

## 5. Unresolved items (exact)

1. None at FATAL or MAJOR level in the audited foundations.
2. Errata m1-m6 and DC-1 to DC-5 are documentation only.  They are recorded here, not applied: lane O and v4 are outside this
   desk's write scope.  Also: proof-theoremP.md L3-6 still reads "NOT yet independently reviewed", although
   review/codex-theoremP ("correct", same sha) exists.
3. These statements in v4 Sec. 6 are superseded by this audit as review coverage only, not as acceptance: L249-252 (Claude checked
   Lemma H only as the image of HW), L251-252 (HW), L253-257 and L261-262 ("not re-audited / not covered by a second family").
4. Parent acceptance is still pending for: the U2-U10 imports, these foundations, Corollaries D and E, and RUNS(p)/INV_Res(p).
5. Open and not addressed here: INV*(p), both halves (a) rotation values and (b) constancy of reflection runs; hence OO(p) for
   every prime p >= 5.  Also not claimed: p = 3; non-inherited INV(p); formal verification; novelty.

## 6. Resources, safety, deviations

* Disk (statvfs) before the launch: 15461179392 B at 01:43 (gate 12.2e9 + 3e6 projected: PASS).  At closeout: 14983852032 B (floor 12e9
  held throughout).
* Math-2 load: at launch no other math-2 reviewer or native process was running (one physics Claude reviewer was); this desk then
  ran 1 reviewer CLI.  No native or scientific runs; no Python computation on mathematical objects.
* One CLI only (Claude, through the unchanged runner, sha256 39c5860b25d6a6b1e723ffff476251631a2847b3f81eaa2fac4b7d0b18428a9b); no Codex or other CLI.  The CLI ran with
  TMPDIR = olson-foundations-final-v1/tmp/ (0 files remain).  No /tmp output, Git, network beyond the CLI, installs, deletion or
  lane edits.
* Deviations:
  * (i) Read-only inspection commands issued before this directory existed (ls, shasum, diff, awk, grep, ps) ran with the
    harness's default TMPDIR.  None is known to create temporary files.
  * (ii) The note is 316 LF lines (the prompt asked for about 300).
  * (iii) The desk notes are same-vendor as the reviewer and are not counted as independent evidence.

## 7. Files (sha256)

* R/olson-foundations-claude-v1.prompt.txt a0400dc8b058af39d95b6ee1caafb3df653557b8edbde49bea12239fb1bf9c8c
* R/olson-foundations-claude-v1.note.md a063bc6b6cbc9ea580857618165cc0fbe2e1a14cb160142095b4f5edf9e3a6f5
* R/olson-foundations-claude-v1.receipt.json e9a83b367349ad083c4fa83be565580fe6e17cf82ab2f84041bc9d89342a69cb
* R/olson-foundations-claude-v1.stdout.json 8e4743653bb9a7ebede6d511c5669b4e22020d58a85db01c7246be5f53689d1e
* R/olson-foundations-claude-v1.stderr.txt (empty)
* olson-foundations-final-v1/snapshot-manifest.json e2192dd01fb6dc8bd749afa9570ed935efed7113b6258cb448ca0046c7f0c55b
* olson-foundations-final-v1/desk-math-check-v1.md b1a1df917a0fb1b5a380a46bb242b4447b842656b49801672e1b51229c8e5d51
* olson-foundations-final-v1/delta-v2-v4-check-v1.md 213277234db3182180aee2222d9e41dd5571bf0f666917360568c166690a8a5d
* olson-foundations-final-v1/claude-review-record-v1.json 6d47654dae0f5609c99f6c7699e68d50c65603bbe128482e4e8dacb663cfb1e0
* olson-foundations-final-v1/checkpoint-01.md 232ca628295fd3dcca2ab00fdd1c0f221045303408b9d3464db1c0892220c23f
* olson-foundations-final-v1/checkpoint-02.md f25eca60515454deacc76d16fc356157b1ae4f52c385aefd9f9f8c4dcc39c417
* olson-foundations-final-v1/checkpoint-03.md cb0af1d598717cac95e137db580b0970e79e3b9067226f302eb41b9a747eebbd
* olson-foundations-final-v1/snapshot/ (32 files; hashes in snapshot-manifest.json)
