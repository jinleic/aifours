# RUNS(p) assembly after Lemma GC: result of the OlsonRunsAssembly slice (2026-10-18T01:18:58-0700, host clock)

Not a parent theorem or gate verdict.  Lane O was only read.  Every file below is new, created with exclusive create under the
prefix olson-runs-assembly-.

## Strongest defensible conclusion (conditional)

For every prime p >= 5, given (i) Theorem NMH-iii (parent-accepted at the normalised NMH, R <= 2p - 3 scope,
R/olson-gc-parent-verdict.md 8e363920...6f70), (ii) the parent-accepted Theorems M, P, Lemma M0 and the SEED-G r2 / A0-r1 / C0W
chain, and (iii) parent acceptance of the imports U2-U10 of olson-runs-assembly-proof-v4.md Sec. 6, the written assembly proves:
NMH(p); MIX_DEF_HIGH(p); MIX_DEF(p), and solvability of every RGR word of length 4p - 2 with 1 <= B < kappa (any parities, no
inherited hypothesis); RUNS(p); every inherited avoider (F, R >= 1) normalises to B = kappa = 0; INV_Res(p); and, through Theorem
DR-Res, every word of RGR_(4p-1)(p) has an identity 2p-subword.
NOT proved: ordered Olson for D_(2p).  Corollary DR' needs INV*(p) as well; both halves are open: (a) rotation values in one
{rho_x, rho_-x}, (b) constancy of reflection runs.  Also not claimed: non-inherited INV(p) or MIX_RUNS(p) (only gap: Theorem KB's
capped case uses (D0)), p = 3, formal verification, novelty.

## Branch map of RUNS(p) (after N; Fact Z: A, B <= 2p - 1, B <= kappa, o_F >= 2 kappa - B + 1, so (V) is automatic)

C1 B = 0 < kappa: OR, then S1'/A1'/cut (o_F <= p) or C0-B'/A1/cut (o_F >= p + 1) on w~.  C2 B = 0 = kappa: K0 with its k >= p + 1
extension on w'.  C3 B = kappa >= 1, o_F <= p: Theorem KB on w' (the capped case uses (D0) of w', the only inherited condition used
anywhere).  C4 B = kappa >= 1, o_F >= p + 1: KBH.  C5 1 <= B < kappa, o_F <= p: OR + Theorem M (the B < kappa half of Corollary RL).
C6 1 <= B < kappa, o_F >= p + 1: Theorem B = MIX_DEF_HIGH (cut, OR, ALT at k~ = 2p - 1, M0 to NMH form; B^ = 0 exit by C0-B'/A1;
NMH(p) = FW+ for R >= 2p - 2 + NMH-iii for R <= 2p - 3).  No inherited inequality is used on any OR/M0-reduced word.

## Static audits of v2 (identities from receipts)

| audit | identity | disposition | FATAL/MAJOR/MINOR | INV* separate |
|---|---|---|---|---|
| olson-runs-assembly-codex-v1.note.md (4f2317413031a7f127dd9e2d56f839baaa08783115b00e28505e6f78153577aa) | gpt-6.1-sol, openai, effort max, read-only sandbox, 1071 s; only shasum/nl/sed/cat inside the snapshot | ACCEPT-WITH-FIXES | 0/0/2 | YES |
| olson-runs-assembly-claude-v1.note.md (aadb6d554f7a3e5ab36706406c3fadae9e2cb5e07988d93f5c5aaad74f5d1eab) | claude-opus-5-5 (init model and model usage), no tools, 1957 s | ACCEPT-WITH-FIXES | 0/0/7 | YES |

Codex MINOR: (1) the OR/M0 avoidance transfers use the full HW/H equivalence, not only the one-pattern direction (v2 L43);
(2) Corollary B' title read as a false universal (v2 L149).  Codex also notes (P) is automatic for k >= p, and marks "Q7 INCOMPLETE"
only for upstream lemmas of DR-Res/DR (EGZ, gap Theorem P, Davenport-alpha, Doubling) that were not in its snapshot.
Claude MINOR: m1 (P) over-attributed to C2 (C2 uses no inherited condition); m2 U6 should list S1 Steps 0-4 (L188-243); m3 name
collisions ("C2" file vs branch; PAR's Theorem P vs the gap theorem used by DR-Res); m4 = Codex (2); m5 the R^ >= 2p exit is
vacuous; m6 C5 re-proves only the B < kappa half of RL; m7 add "F, R >= 1".  All are documentation-level; all are applied in
olson-runs-assembly-proof-v3.md / v4.md (Sec. 8 change log); v3/v4 are not re-reviewed.
Both auditors: no circularity (Theorem M does not use PAR; Theorem P is used only after RUNS), no finite premise, no overreach
beyond the listed wording; both endorse the conditional conclusion above and neither endorses ordered Olson.

## Which obligations still need independent review (Main's question)

* proof-C2.md (R2, BR, FW+): Codex ACCEPT (earlier target review) + Claude full line-by-line check here, no finding.  Two-family
  covered; only parent acceptance remains.
* README Sec. 1 reductions = Theorem B (OR, M0, ALT, B = 0 exit by C0-B'/A1, trivial cut): full by both auditors here (M0 accepted
  earlier; OR also Codex-reviewed earlier).  Theorem FWH (proof-MH.md Sec. 3): full by both here.  Only parent acceptance remains.
* Corollary RL: full by both here (in Theorem C it is C3 + C5).  KBH: Codex earlier + Claude full here.  KB, S1', A1', BC, K0 and
  the k >= p + 1 extension of K0: Codex (earlier and/or here) + Claude full here.  C0-B' chain (TL, KW, S1, Split, Depth, C0-B),
  A1, ALT, B0: full by both here.  Only parent acceptance remains.
* INV_Res(p) = RUNS(p) + Theorem P (accepted): endorsed by both.  RGR-LONG(p) via DR-Res: DR-Res/DR' Claude-reviewed earlier and
  checked by Codex here relative to upstream imports.
* Still lacking a second family in this cycle (small): Claude-side full check of Lemma H/HW beyond the interfaces (Codex full;
  both rest on GR/WAS, Claude-reviewed earlier, Codex-verified here); the upstream lemmas of DR-Res/DR in proof-dihedral-partial.md
  (Codex-reviewed earlier; needed for RGR-LONG, not for RUNS/INV_Res); a parent delta check of v2 -> v4 (documentation only).
* Open (not a review question): INV*(p), both halves; hence ordered Olson for D_(2p).

## Files (sha256)

* olson-runs-assembly-proof-v4.md  06579ba5d23f194cf4cf61241fbbc6eebdaa6fb991d004f1642f43277bb3b104  (final assembly; v3 c5f896912291d144f3fef8d00f846f80d6185ca8cbfab042151bee71705c0665; v2 0b78850fa232f61c6f45e01c5e8e9f3e2582e96572c3a4fa810fe357ac324abb = audited target; v1 153dff8a82786d04f8a9184f1f42cedee6dc6517b606593d91e1c90cb01b7bef never sent)
* olson-runs-assembly-inputs-v1/ (Codex snapshot: 29 byte-identical files + manifest.json; the parent GC spot note was not included)
* olson-runs-assembly-codex-v1.prompt.txt  d962b813bff102d8a10da1da4ea08c80d2e2433e048ffbdeec98eedf81ec899b; .note.md/.receipt.json/.stdout.txt/.stderr.txt
* olson-runs-assembly-claude-v1.prompt.txt  6a36c252d363f1a837f2df9ea3cb78357a7bf4cc4e8f624104aeb87942c223d1 (173,739 B, one packet); .note.md/.receipt.json/.stdout.json/.stderr.txt
* olson-runs-assembly-checkpoint-01.md, -02.md; olson-runs-assembly-tmp/ (TMPDIR of both CLIs)

## Resource and safety record

Disk gate before each launch: free 17,779,748,864 B (00:39:59) and 17,776,291,840 B (00:40:15), threshold 12.2e9 + ~3e6 projected.
Math-2 reviewer CLIs at launch: 1 (GC desk Claude), 3 after launch.  Both runners started by bash async (limit 3,000 s; internal
2,400 s + SIGTERM-only grace); both exited 0 with status NOTE_RETURNED_UNVERIFIED; no timeout, no kill signal, no Python computation
by the reviewers, no network beyond the CLIs, no Git, no lane edit, no /tmp use by this slice (CLIs given TMPDIR =
olson-runs-assembly-tmp/).
