# Review package TCW v1 (third cut window, p = 4kappa-5)

Owner OlsonThirdCutWindow (throttled math2 slot, Olson lane). Written after /bin/date 2026-10-20T05:33:14-0700.
Status: CANDIDATE_UNVERIFIED written mathematics; no model review has been run by this owner (the parent runs all reviews
and verdicts). No novelty, priority, "first", Lean, human-referee or runtime claim.

## 1. Claim under review

THEOREM TCW (proof-TCW-v1.md Sec. 0, read with erratum-1). For every integer kappa >= 4 such that p = 4kappa-5 is prime
((kappa,p) = (4,11), (6,19), (7,23), (9,31), ...), no word of length 4p-2 over D_(2p) without an identity 2p-subword (in
increasing original index order) has an admissible normal form with terminal k = p+1 and kappa_hat = kappa. Full
existential antecedent: SOME admissible NF; extra reflection pairs anywhere in the odd blocks; genuine empty-run rule;
no o_F, nonempty-run, rotation-pair or rigidity hypothesis.
Outcome: PROVED (candidate), no failing lemma. Range: every kappa >= 4 with p = 4kappa-5 prime.
Cell (4,11): COVERED (proof Secs. 5 and 6; it is the cell kappa_hat = 4 at p = 11). The all-rotations-equal
configurations at (4,11) are excluded by the same argument; CJ''' is not used.
Not claimed: any p not of the form 4kappa-5 (FCW's p = 4kappa-1, SCW's p = 4kappa-3, any other deficiency); general
deficiency; kappa_hat != kappa; p = 7; nonterminal k; middle-range or upper-half cells; reflection rigidity; INV*; o_F
assembly; full ordered Olson; multiset-only statements outside the antecedent.

## 2. Files (this directory)

| File | Bytes | SHA256 |
|---|---|---|
| TCW-scope-v1.md (frozen 2026-10-20T03:27:24-0700, before any derivation) | 8581 | f0dacbe3e1f2f8a4267f7bdfa5ea91097690168bbf0e50dced92e6cc49be02d1 |
| proof-TCW-v1.md | 49889 | 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713 |
| erratum-1-proof-TCW-v1.md (citation/process corrections only) | 1780 | 00ba0139bc3f13025f7ba9474d3c48813c746839a35e33f95fb5ac3fa4edea01 |
| review-excerpts-TCW-v1.json (manifest, 16 entries) | 3757 | 3a21ad905ac96e68b60ecaeb1ced6bc9ed4dee122fbe5692f41fd9b6b0338058 |
| checkpoints/cp-01.md | 1307 | fbbcae9a12a3973d97ebddb0767f6f97aae337fec47f7231b261d403a45eb6d5 |
| checkpoints/cp-02.md | 2516 | ba69440cf52d6ee280ada271675c2c83b335bc34fe2e25b1ff3dc4ed1968b092 |
| checkpoints/cp-03.md | 1612 | 3edf3d8b169d0454e13c39bb1c026a71add2326c3e069970c83cfae909ef4e5a |
| checkpoints/cp-04.md | 1178 | 1fa2524326f210350abab91261eea18faedee669746f0b570c547dcc75783bec |
| checkpoints/cp-05.md | 1477 | b6ccce99d455c7dea06a35526ab50f3e07ff772666d6fd3d4e1634c043f5b409 |
| checkpoints/cp-06.md | 782 | 404a2c5f190b835b517caf022d1a73062b6dc38c3e2416735a8ecf4d79a87077 |
This package and the closing checkpoint cp-07 are recorded (with hashes) in cp-07.

## 3. Manifest

review-excerpts-TCW-v1.json (sha256 3a21ad905ac96e68b60ecaeb1ced6bc9ed4dee122fbe5692f41fd9b6b0338058): 16 entries
{path, sha256, start, end}, absolute paths, inclusive LF ranges: the proof (1-511), erratum-1 (1-19), the scope (1-120),
the authority transition (1-44), PL lines 40-129, LOWER parent erratum (1-10), LOWER-K1 verdict (1-22), NF (ROT 28-43),
GRX (7-20), the (S1) definition (zx-s1c line 19), SC0 (1-11), FB verdict (1-16), proof-FB (9-24), FB erratum 1 (1-7),
balfull (S') extension (26-34), FCW parent erratum (1-14; cited for the (SR) derivation m4 and as context). Raw excerpt
size 88,828 bytes (sum of the selected LF lines; measured by reading the files), about 920 lines. Every hash was
re-checked with shasum -a 256 at 2026-10-20T05:32 and equals the hashes recorded in TCW-scope-v1.md.
Not in the manifest (context or untrusted; all hashes in proof Sec. 8): FCW verdict and FCW proof (accepted only at
p = 4kappa-1; methods re-derived), USK and K0T verdicts, the SCW proof (unaccepted; methods only).

## 4. Premises actually used (each at its accepted scope)

NF (some admissible NF; odd blocks; empty-run rule); GRX if-direction through (SR) as in PL Sec. 2; PL IF(a), the
gamma-normalisation, the SS bijection and LT (re-derived); the (S1) definition only; SC0 read through the minimal-zero-sum
step Y'z; ZSTRUCT and Lemma FB in (S') at (k',kappa') = (p-1,kappa-1). NOT used: S1(a), the Setting fact, FB-E, Theorem P,
CJ''', K3-11, PL Lemmas D/U/A/C/THETA, every USK/K3/FCW/SCW lemma.

## 5. Where a reviewer should look first

- Lemma 6(b),(c) and Lemma 7: the exact exception lists for the windows [2,R-4] and [0,R-6] (minimal representations
  missing <= 4 letters are single-signed because u1 >= |c|+4).
- Lemma 9: the (lambda,mu) tables (m = kappa, kappa+1, and kappa-1 by duality, Lemma 8) and their consequences.
- (F1a): the coupling q(P u {i}) + q'(P) >= |A^c| >= 8, giving X <= 6 and |d-d'| <= 4kappa+4 < 2p at kappa = 4.
- (F4)(c): the two-step link at kappa = 4 for independent 4-sets with all gaps 2; (F5): the all-kappa triple.
- Sec. 5: Lemmas 14-16. The slack is exactly one unit (eps_ev + eps_od <= 1). Lemma 16 Case B at kappa = 4 is the most
  delicate place; its n1 = 2 branch uses the two-sided Lemma 13.

## 6. Process disclosure

- Freeze: TCW-scope-v1.md created 2026-10-20T03:27:24-0700 (date taken immediately before creation) before any
  derivation. Pre-freeze exposure (scope Sec. 4): the assignment and transition (including the parent's disclosed,
  unproved observation), directory listings, the FCW excerpt manifest (metadata only), shasum/wc outputs, and the harness
  memory summary (process-level mentions only). No mathematics was read or derived before the freeze.
- Post-freeze reading: listed in checkpoints/cp-01.md.
- Machine steps: /bin/date; shasum -a 256; wc -c -l; ls; mkdir of this directory and checkpoints/; reading files
  (including one Python read of the manifest sources to count the bytes of the selected line ranges, metadata only);
  one python3 json.load of the created manifest to confirm it parses (metadata only); exclusive creation of drafted text
  with Python open(path,'x'). The proof was drafted by hand in five in-memory parts with six rewording replacements
  before its single creation (erratum-1 item 1 corrects the count stated in the proof). No assert statement of any kind,
  no script or computation over scientific data, no enumeration, solver, test, Lean, model CLI, nested agent, network
  access, commit or push. No file was edited, overwritten, moved or deleted.
- Checkpoint cadence DEVIATION: the gap between cp-01 (03:29:52) and cp-02 (04:38:50) was 4138 s > 1800 s (a long
  derivation turn whose output was discarded by the harness and redone; disclosed in cp-02). All other gaps were below
  1200 s.
- Exposure use: the parent observation (windows [2,R-4], [0,R-6]; FCW-type slack 5; SCW pair does not fit at (4,11))
  was treated as untrusted; proof Sec. 7 (M2) records that the windows are as observed, that the relevant generic slack
  at N = 4kappa-4 is two units (one unit for the exceptions), and that the SCW pair indeed does not fit at kappa = 4.
