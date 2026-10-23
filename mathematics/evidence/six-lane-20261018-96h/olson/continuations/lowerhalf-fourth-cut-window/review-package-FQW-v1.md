# Review package FQW v1 (fourth cut window, p = 4kappa-7, delta = 6)

Owner OlsonThirdCutWindow (same math2 slot). Written after /bin/date 2026-10-20T07:10:43-0700.
Status: CANDIDATE_UNVERIFIED written mathematics; no model review has been run by this owner (the parent runs all reviews
and verdicts). No novelty, priority, "first", Lean, human-referee or runtime claim. TCW and P7L (unaccepted) are not
premises; FCW/SCW/USK lemmas are not used.

## 1. Claim under review

THEOREM FQW (proof-FQW-v1.md Sec. 0, read with erratum-1). For every integer kappa >= 5 such that p = 4kappa-7 is prime
((kappa,p) = (5,13), (6,17), (9,29), (11,37), (12,41), ...), no word of length 4p-2 over D_(2p) without an identity
2p-subword (increasing original index order) has an admissible normal form with terminal k = p+1 and kappa_hat = kappa.
Full existential antecedent: SOME admissible NF; extra reflection pairs anywhere in the odd blocks; genuine empty-run rule;
no o_F, nonempty-run, rotation-pair or rigidity hypothesis.
Outcome: PROVED (candidate), no failing lemma. Range: every kappa >= 5 with p = 4kappa-7 prime.
Cell (5,13): COVERED (Secs. 5-6). At kappa = 5 two margins are tight: pair-independence of theta (2D0+21 <= 25 < 26,
Lemma 12(e)) and the case-H sub-case with both outside letters in B_1, closed by the two-sided Lemma 14.
Not claimed: any p not of the form 4kappa-7; any other deficiency; kappa_hat != kappa; kappa_hat = 0; p = 7; nonterminal k;
middle-range or upper-half cells; reflection rigidity; INV*; o_F assembly; full ordered Olson; multiset-only statements.

## 2. Files (this directory)

| File | Bytes | SHA256 |
|---|---|---|
| FQW-scope-v1.md (frozen 2026-10-20T06:26:24-0700, before any derivation) | 8667 | 97cbf46c970eca6e576b349f889cace799d33aec9bf37c268fbc1d17d604ba3d |
| proof-FQW-v1.md | 47237 | 9b4561780b37874c47a188fc788ae34fc223f1252f7e4bf9a1be9a6dffd09dc5 |
| erratum-1-proof-FQW-v1.md (wording/clarifications only) | 1047 | 9cf740b22a6b5f20d1562c38be4ebeedfd5b95e003542a57f71e85072f965fd5 |
| review-excerpts-FQW-v1.json (manifest, 14 entries) | 3285 | bc99bbe918ef663c6d934cd5d6271373aa6a5893305d304d47c01ca4c75dde26 |
| checkpoints/cp-01.md | 2308 | 06f9f37f65283781a853455b44ae8b913f91a324602577f4649ac18e9ab1c01a |
| checkpoints/cp-02.md | 1618 | 30d59896ae94a3a9fc11a503bf3b80b650dd14f47f8c10d2026b5e7d715f04f1 |
| checkpoints/cp-03.md | 687 | 8ffcd95cc7744d4e3c97fa76838ea5617230a9ee6f0718b372644b32380f31dd |
| checkpoints/cp-04.md | 767 | 4672b52de38a37c9f726efd06bf60f870b490e70f06c02df080e0dba0c292d32 |
| checkpoints/cp-05.md | 835 | 295488f2190e8760dfb0e518af8d10b03e5585ff5c5f8f4faa44b9d64f4dba24 |
This package and the closing checkpoint cp-06 are hashed in cp-06 and in the owner's final report.

## 3. Manifest

review-excerpts-FQW-v1.json (sha256 bc99bbe918ef663c6d934cd5d6271373aa6a5893305d304d47c01ca4c75dde26): 14 entries
{path, sha256, start, end}, absolute paths, inclusive LF ranges: proof (1-482), erratum-1 (1-12), scope (1-99), authority
transition (1-55), NF (proof-ROT-few-E-v4.md 28-43), GRX (7-20), SC0 (1-11), FB verdict (1-16), proof-FB (9-24), FB
erratum 1 (1-7), balfull (S') extension (26-34), (S1) definition (zx-s1c line 19), LOWER parent erratum (1-10), FCW
parent erratum (1-14; derivation patterns only). Raw excerpt size about 74.4 KB in 762 lines (whole-file entries from wc
byte counts; partial ranges from the byte counts measured for the identical files, hashes and ranges in the TCW packet).
Every hash was re-checked with shasum -a 256 at 2026-10-20T07:10 and equals the scope/proof records.
Not in the manifest (context or untrusted; hashes in proof Sec. 8): FCW, SCW, USK, K0T and LOWER-K1 verdicts, PL, the
TCW proof and its parent errata, the P7L, FCW and SCW proof texts.

## 4. Premises actually used (each at its accepted scope)

NF; GRX if-direction (Lemma 1); SC0 through Y'z (Lemma 3(c)); ZSTRUCT and Lemma FB in (S') at (k',kappa') =
(p-1,kappa-1) for t >= 1 (Lemma 3(d)); the (S1) definition; the LOWER parent erratum conventions. Everything else is
proved in the text at p = 4kappa-7. NOT used: PL lemmas (including its (SR) text: Lemma 1 is derived directly), Theorem P,
B0S-CJ''', S1(a), the Setting fact, FB-E, and every USK, K3, FCW, SCW, TCW and P7L lemma.

## 5. Where a reviewer should look first

- Lemma 7(b) with Lemma 4(v) (u1 >= |b|+9 makes six missing letters harmless) and Lemma 8(b) (the enlargement analysis
  for the self-dual window [4,R-4]).
- Lemma 11 (the three (lambda,mu) tables) and Lemma 12(d)-(e): the two couplings and the bound Xmax+Ymax <= 21, which is
  exactly what is needed at kappa = 5 (2D0+21 <= 25 < 26); the degenerate case L_i = all letters.
- (F3)(c) (the two-step link for kappa in {5,6}) and (F4)-(F5) (the all-(kappa-1) additive triple; Delta >= M0-6 >= 3).
- Sec. 5: the switch to sorting the top kappa-1 runs; Lemma 13(c) (type Q with t = 0 impossible), Lemma 15(b) (two type-Q
  sets impossible), Lemma 15(d) with Lemma 14 at kappa = 5.

## 6. Process disclosure

- Freeze: FQW-scope-v1.md created at 2026-10-20T06:26:24-0700 (date taken right after mkdir, before creation), before any
  derivation. Pre-freeze exposure (scope Sec. 4): my TCW and P7L work (methods), FCW/SCW and inputs read earlier, the Main
  IRC assignment and the transition including the parent's untrusted notes, shasum/wc/ls metadata, the memory summary. No
  derivation concerning delta = 6 was made before the freeze. The TCW parent errata were read only after the freeze (cp-01).
- Machine steps: /bin/date before every timestamp; shasum -a 256; wc -c -l; ls; mkdir of this directory and
  checkpoints/; reading files; exclusive creation of drafted text with Python open(path,'x'). The proof was drafted by hand
  in eight in-memory parts with two rewording replacements before its single creation (cp-04, cp-05). No assert statement
  of any kind, no parsing or checking of mathematical objects, no script, enumeration, solver, test, Lean, model CLI,
  nested agent, network, /tmp, deletion, commit or push. No file was edited, overwritten, moved or deleted.
- Checkpoint cadence: freeze 06:26:24; cp-01 06:43:22 (1018 s); cp-02 06:55:19 (717 s, final count recorded before
  drafting); cp-03 07:00:25; cp-04 07:03:39; cp-05 07:08:03 (after creation of the proof); all gaps below 1200 s. No
  output was lost in this assignment.
- Exposure use: the parent's untrusted notes were checked, not used as premises; proof Sec. 7 (M1)-(M3) records the
  comparison (windows as noted; u1 margin 9 > 6 at every kappa >= 5; N even, 2kappa-3 runs per alternating set; the TCW
  swap machinery is replaced by top-(kappa-1) sorting with empty-run arguments).
