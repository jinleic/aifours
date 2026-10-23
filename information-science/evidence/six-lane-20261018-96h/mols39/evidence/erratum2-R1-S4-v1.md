# Erratum 2 to reduction R1, structural note S4 and erratum 1 — disposition of the dual review (2026-10-19T06:09:36-0700, ContinueCFR21)

Base files (preserved unchanged; hashes re-checked when this file was written):
- R1 base: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/reduction-R1-beta-route-v1.md, sha256 eabe1fc4375ed05492e684d38418bda2c294305269240503e6e96c27c1a4669b
- S4 base: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/structural-note-S4-v1.md, sha256 49926433125f49a59095bcecc081b21a54fbb8f840566535a80fcfb44de250dc
- Erratum 1: /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/erratum-R1-S4-v1.md, sha256 74bc52ca1c5839c0eb6c15e729c44b0fd4cc23a8857be599a0f4a8e94189d8fd
Reviews disposed here (parent-owned files, read in full with :raw):
- Claude (opus-5-5) note /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-R1-claude-v1.prompt.note.md, sha256 78f13c8806b67c284b202413d93447fb4c60684e329ef9bf503e8dabe8dd14ae:
  Lemma U ACCEPT; corrected R1 ACCEPT-WITH-FIXES; MAJOR M1 (Consequence 3); MINOR m1-m12.
- Codex (gpt-6.1-sol) output /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-R1-codex-v1.prompt.stdout.txt, sha256 3d7509c17bfd62ebb69c68daa07ac723e0acba2dbe72d1864baa1b306d6810cd:
  Lemma U ACCEPT; corrected R1 ACCEPT conditional on Lemma U; MINOR output-contract and provenance qualifications (B.14).
- Review freeze /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-LemmaU-R1-review-freeze-v1.json, sha256 2af07bd4c475d12a493dada85c8b7eb4f9c6fc6092eb4d91677a53554035117a;
  parent endpoint audit /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-lift2-parent-endpoints-v1.json, sha256 c49207c361a09a2eab6a791345fef9033111b14a6b1620aa8524bb917cd8d4b9.
Status: worker disposition; the parent's verdict is pending. No statement is broadened: every change below restricts,
qualifies or corrects wording. Lemma U concerns the exact anchor only, is computer-assisted, and has no formal (Lean)
proof and no certificate (a certificate specification is frozen separately and has not been executed). Nothing here
concerns other difference matrices, CFR(6,39) or six MOLS(39).

## A. Provenance of Lemma U (cite this instead of "single-producer S4a")
A1. Route 2, run L4 (lane-authored by subagent ContinueCFR21.LiftRoute2 from a definition-only specification; the author
    had no access to S4, R1 or the route-1 probe): program /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/review/lift_route2/lift_route2.py
    sha256 7342496cfa8a980844a7a16ab4e3ac36d7d86f0ad75d9eda2a2cd6849fdc585b (README e5cdd7c039abddce22d6ad571435a531e5a7bac57b84304bd9a7d5f89dfa55a1);
    run directory /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/runs-lift2/L4-anchor: config 541d64eb2ff7aae4a4b9d77e1f6621b0c1ba4f7564954417be81d8dbbcc42d37,
    gate e1c3771fc204a181bde4a5a8fc0524d1c1bca8c4da768fa223f5fe52c8542196, receipt 2fa1ca6c91586324a97b4317aca2052e9f2a7e6695a37d88a7c0b00e3792dd58,
    stdout = out.json 71cd56d50feea9b377eb75477dbad775c36177e6df10924303174a135ba887e8; result COMPLETE, 19 nodes,
    N_classes 2 = {T, -T}, N_total 486, representative digests T 1c4846c9481ab831c34df4b4025afaa0886475bc245be6dff7509d4545f3732a
    and -T f5b8803442fbc2cde6d72af8f2eddbdd07910050e81f1e84c073dace428d0878. Index /Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lift2-results-v1.json
    sha256 e805e31422a68f18609efb56afb9d6cb9237f69a6a120405857ad70a2127314b.
A2. The parent's independent dense control: /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/mols39-lift-parent-control-v1/parent_dense_lift_v1.py
    sha256 94dff08b4f22e3fe09a819b534529b2721617f49c0469a4501c5e896bd5f37f3, result.json
    30341aaaa42ec80cb3bf1a60456f4630ae9b175860ba0abfe7e783c47cf66e87, receipt a1e413cf7423bf15d5d268521e793c894bbca3ac29cdef4785bef23a1f5cdcf8:
    190 gauged variables, rank 185, gauged dimension 5, all 243 vectors enumerated, 2 classes and 486 lifts, and
    representative digests equal to A1 (endpoint audit c49207c3...).
A3. Route 1 (S4a; probe code/probe_mod3_lift_v1.py 535831250d79f9a802ec8caca597de4c61bae82f21392e0635b05dd226e87c9b,
    stdout fd06bafb8dafa5ff2bd070e1d589cfecd20079227e0f7103eaedb27df47ddce5) corroborates the counts only (see B.m3).
A4. Route-2 gating controls: L1 DM21 (2 classes) and L3 Singer-type 57 with k = 8 (4 classes) as expected.
    L2 (DM21 without the linear propagator) agrees with L1 (see B.m4 and B.m5).

## B. Dispositions with exact replacement text
B.M1 (MAJOR; R1 base lines 45-47, Consequence 3): DOWNGRADED AND RESTRICTED. Replace base lines 45-47 by:
  "3. [Restricted by erratum 2.] For the exact anchor, by Lemma U and the corrected Proposition R1, the beta route is
   not wider than the anchor's free one-row extension (Consequence 1). For any other object no statement is made:
   (a) no per-object analogue of Proposition R1 is stated or proved here; (b) the S4 class counts for Sage DM33/DM51,
   P21 and the seven-row Singer restriction are unreviewed single-producer (route 1) observations; the counts for
   Sage DM21 (2 classes) and the eight-row Singer-type (57,8;1)-DM (4 classes) were reproduced by route 2 only in
   their role as engine controls (L1, L3); (c) for a k-row skeleton (k = 8 and 7 for the Singer objects) with more
   than one sign pair of rainbow lift classes, the beta route is POTENTIALLY wider than the free one-row extension
   of that one DM. This is not established: the additional pair +-alpha' may give DMs equivalent to CRT(alpha, beta)
   under the full equivalence group (not examined), and no extension is exhibited. Unreviewed single-producer
   observation; no claim."
  Withdrawn base wording: "genuinely wider", "6-row lift space", and "(and, by S4, Sage DM21/DM33/DM51 and P21:
  exactly 2 classes) it is not".
B.m1 (R1 base line 15, Setting): replace "then CRT(A, beta) is a (Z_39,6;1)-DM, and every 6-row DM with skeleton beta
  arises so." by "then CRT(A, beta) is a (Z_39,6;1)-DM E with E_0 = 0 and E mod 13 = beta, and every 6-row DM E with
  E_0 = 0 and E mod 13 = beta arises so; a general 6-row DM arises in this way only after normalising at its row 0."
B.m2 (S4 base line 16, last column header): replace "rainbow points mod constants" by "rainbow points mod ker F (the
  probe's output key rainbow_points_mod_kernel). In every row of this table this equals rainbow points mod row
  constants, because there functional rank = m = dim V - (k-1), i.e. ker F = the row constants".
B.m3 (route-1 status; R1 base lines 17-19 and S4 lines 3-6): route 1 is corroboration of the counts only. It builds no
  lift and re-checks no leaf against the definition. It counts rainbow points of im F, which is the count modulo row
  constants only because rank F = dim V - 5 was also reported. Its stdout is not embedded in the review packet.
  Replace the base Lemma U provenance "(computational; S4a, probe code/probe_mod3_lift_v1.py 53583125..., run
  S4a-six-row-3n, stdout sha256 recorded in S4)" by "(computer-assisted, exact anchor; provenance: erratum 2 section A;
  route 1 = corroboration of counts only)".
B.m4 (propagator cross-check): add to the provenance: "The propagator-free cross-check L2 covers DM21 only. The anchor
  run L4 used the linear propagator. On the anchor, the propagator is corroborated by the code audits in both reviews
  and by the parent's dense enumeration, not by a propagator-free anchor run."
B.m5 (Singer input): add: "The Singer-type input is generated from one definition in both routes; this worker supplied
  the construction text to the route-2 author. The L3 agreement is therefore engine-independent but not
  input-independent, which is acceptable for an engine control."
B.m6 (parent-owned control): citation text for this lane: "The parent control's DM3 positive control and its
  single-entry mutation controls show only that its checks are not vacuous. The substantive engine controls for this
  result are route 2 L1-L3."
B.m7 (record-before-gate): lane rule recorded for any future probe (none is authorized now): write the complete result
  record before any expectation gate. This lane's post-job checkers already comply: check_ext2_controls_v1
  (9f5408d30324c0c2c489a885642d15694489aabac0da60f290265fe0b926f034), check_ext2_targets_v1
  (6d5f00c2ebb0b6c3e743228c8d0fc61ae572efef36503332da8529344a088a78) and check_lift2_v1
  (cbdb6bf3933984c2ef0e9468c671592f840030a3ba14a2694d2491f071d8cb29) read the engine's completed stdout record only after
  the engine has exited and never gate the engine itself. The parent control is parent-owned.
B.m8 (provenance deviation, recorded here as M39-D6): for L1-L4 the pre-run report to the parent (IRC, 05:13) gave
  program, jobs-spec, checker and config hashes, but not the per-child launch identities. Each child's launch record
  (pid, pgid, start, abs_end) was written by owned_supervisor_v2 before compute, but was reported to the parent only
  after all four children had completed (index lift2-results-v1.json). The same applies to the ext2 control wave
  (10 children, reported with their results) and to the ext2 target wave, where only T3's identity was sent while it
  ran and T4-R7 were reported with the results.
  Impact: weaker pre-registration of child identities; no effect on the Lemma U result, which the parent's own
  supervised control reproduces. No further launches are authorized.
B.m9 (stale base text): the R1 base file still shows the withdrawn clause (line 26) and the superseded converse
  (line 27). From now on R1 must be cited as base + erratum 1 + erratum 2. The consolidated reading text in section C
  governs wherever it differs from the base or from erratum 1. Any positive control built under Consequence 4 must
  read the new beta-row after normalising at row 0: for the anchor, beta_6 = (f - D_0) mod 13; for a Singer-type
  control over Z_57, (f - D_0) mod 19.
B.m10 (erratum 1 E1, line 14): replace "is false as stated, and it is WITHDRAWN" by "is unsupported: the proof yields
  g = mu D_0, whose reduction mod 13 is D_0 mod 13, which is nonzero. Because the existence of any D* is open, the
  universally quantified clause can be neither refuted nor used. It is WITHDRAWN". E1 remains a statement change.
B.m11 (stale status and provenance lines):
  (i) Replace R1 base lines 3-4 by: "Status: worker proof. Dual review: Lemma U ACCEPT (Codex, Claude) as a
      computer-assisted exact-anchor result; corrected R1 ACCEPT conditional on Lemma U (Codex) and ACCEPT-WITH-FIXES
      (Claude), with the fixes disposed by erratum 2; parent verdict pending. Provenance of Lemma U: erratum 2
      section A. No search was run for this note."
  (ii) After R1 base line 7 add: "[Erratum 2: the parent later recorded that describing this route as strictly wider
      was only potential, not established (note S6 section 1, 282701f4...). For this anchor, R1 shows that the two
      routes are equivalent.]"
  (iii) Replace erratum 1 lines 6-7 ("Lemma U remains an exact-anchor candidate, pending the parent's independent
      audit; ...") by: "Lemma U: review status and provenance in erratum 2. Nothing here supports a broad conclusion
      about the existence of six MOLS(39)."
  (iv) Add after R1 base line 21 the derivation of every clause from the gauged count: "Let W = {A in V : A_x(0) = 0
      for all x} and let C be the row constants (e_0 = 0); then V = C (+) W. Route 2 and the dense control give
      dim W = 5 and exactly two rainbow points in W, namely +-alpha^ with alpha^_x(c) = alpha_x(c) - alpha_x(0).
      Hence dim V = 10. If 0 != h in W and F(h) = 0, then alpha^, alpha^ + h and alpha^ + 2h would be three distinct
      rainbow points of W (they have the same fibre-functional values), contradicting the count. So ker F = C,
      rank F = 5, and exactly 2 of the 3^5 classes of V / ker F are rainbow. The 486 lifts are the lifts with A_0 = 0 of
      the fixed labelled skeleton before quotienting by the five row constants (2 * 3^5)."
B.m12 (R1 base lines 35-38, Consequence 1): replace by: "1. For this anchor, the beta route and the anchor's free
  one-row extension are equivalent existence questions, with explicit maps in both directions:
  D* |-> f = mu^(-1)(D*_6 - D*_0) + D_0, and [D; f] |-> beta_6 = (f - D_0) mod 13. The equivalence uses only Lemma U,
  the CRT, and invariance of the DM property under column translation, adding a constant to a row, and multiplying
  all rows by a unit. Both questions are UNKNOWN. [Imported, not reviewed with R1 and not used by it: the
  free-extension runs v1 T2 and v2 T6 were incomplete at 270-282 s.] The COMPLETE negatives for the anchor with a
  symmetry imposed on the new row (G6 and C3: two producers; C2: one producer) are separate results. The map
  D* |-> f does not track equivariance, so these negatives are not special cases of, and do not transfer to, any
  statement about the beta route."
  Erratum 1 lines 27-28 ("Effect on the consequences: none. ...") are replaced by: "Effect on the consequences:
  Consequence 1 is restated (erratum 2, B.m12) and Consequence 3 restricted (erratum 2, B.M1). Consequences 2 and 4 do
  not use the withdrawn restriction; for Consequence 4's normalisation see erratum 2, B.m9."
B.13 (Claude section 6, unnumbered remark on Consequence 2, R1 base line 40): replace "explores a strictly looser
  relaxation" by "explores a relaxation, expected but not proved to be looser,". The order of magnitude (about 1
  expected beta-solution; the reviewer reproduces about 0.9) stays labelled HEURISTIC.
B.14 (Codex minors):
  (i) Interpreting route 1's count modulo row constants requires ker F = C: see B.m2, B.m3 and B.m11(iv).
  (ii) Status OK, exit 0 and settlement do not by themselves certify exhaustive enumeration. Section A relies on route
      2's COMPLETE status and on the parent's full 243-vector loop.
  (iii) "486 lifts" means lifts with A_0 = 0 before the quotient: see B.m11(iv).
  (iv) Representative digests agree between route 2 and the parent control only; route 1 emits counts only (A3).
  (v) Late registration of child launches: M39-D6 (B.m8).
  (vi) The non-anchor S4 rows are not promoted. The four Singer classes form two sign pairs under negation and
      establish no inequivalence: B.M1 and B.E2'.
B.E2' (erratum 1 E2; replaces S4 base lines 31-33 together with erratum 1 lines 33-36):
  "1. For every measured object the linear relaxation is small: m in {5,...,9} against 105-399 unknowns. Route 1
   found exactly 2 rainbow classes (+-alpha) for the five six-row objects, and 4 classes (two sign pairs) for the
   eight-row Singer-type object and for its seven-row restriction.
   - Five six-row objects: the mod-3 part is determined by the mod-q skeleton up to sign and row constants. For the
     anchor this is Lemma U (erratum 2, section A); for DM21 it was also reproduced by route 2 as engine control L1;
     for DM33, DM51 and P21 it is an unreviewed single-producer observation.
   - Singer-type objects: the mod-3 part is not determined in this sense. The eight-row count was also reproduced by
     route 2 as engine control L3; the seven-row count is single-producer. Whether the second sign pair gives an
     inequivalent DM was not examined."
  The S4 status line stays "UNREVIEWED" for every row except the anchor row (Lemma U) and the two engine-control
  reproductions (L1, L3).

## C. Consolidated reading text of R1 (base + erratum 1 + erratum 2; this text governs)
# Reduction R1 — the mod-13 ("beta-index-3") extension route for the anchor
Status: worker proof. Dual review: Lemma U ACCEPT (Codex, Claude) as a computer-assisted exact-anchor result; corrected
R1 ACCEPT conditional on Lemma U (Codex) and ACCEPT-WITH-FIXES (Claude), with the fixes disposed by erratum 2; parent
verdict pending. No search was run for this note.
Context: the parent proposed (2026-10-19, about 04:2x) to extend only beta = D mod 13 of the anchor by a seventh
beta-row and to solve the mod-3 lift of all seven rows afresh. The parent later recorded that describing this route as
strictly wider was only potential, not established (S6 section 1).
## Setting
D = exact anchor (Sage DM_39_6_1, raw sha256 3c8dbe62da8705eb6e713e85dae4d2fbf303614b2254f832a7291fe2f38a882a), rows 0..5
and columns C (|C| = 39) in file order. Z_39 = Z_3 x Z_13 (CRT). Normalise at row 0: D'_x = D_x - D_0,
beta_x = D'_x mod 13, alpha_x = D'_x mod 3 (beta_0 = alpha_0 = 0).
A in F_3^(rows x C) with A_0 = 0 is a lift of beta iff, for every pair x < y and every t in Z_13, the fibre
T_xy(t) = {c : beta_x(c) - beta_y(c) = t} (3 columns) carries 3 distinct values of A_x - A_y. Then CRT(A, beta) is a
(Z_39,6;1)-DM E with E_0 = 0 and E mod 13 = beta. Every 6-row DM E with E_0 = 0 and E mod 13 = beta arises so; a
general 6-row DM arises in this way only after normalising at its row 0.
## Lemma U (computer-assisted, exact anchor; provenance: erratum 2 section A)
The lifts of beta are exactly {eps*alpha + e : eps = +-1, e a row-constant vector with e_0 = 0}: 2 classes modulo row
constants, and 486 lifts with A_0 = 0. Equivalently, dim V(beta) = 10, the kernel of the fibre-functional map F on V
is the 5-dimensional space of row constants (rank F = 5), and exactly 2 of the 3^5 classes of V / ker F are rainbow
(derivation: erratum 2, B.m11(iv)). alpha and -alpha lie in different classes, because each D'_x (x >= 1) is a
bijection C -> Z_39, so its mod-3 part is balanced and not constant.
## Proposition R1 (corrected)
Let D* be any (Z_39,7;1)-DM whose rows 0..5, after normalising at row 0 (D*'_x = D*_x - D*_0) and labelling its
columns by C, reduce mod 13 to beta. Let eps be the sign given by Lemma U for the mod-3 part of rows 0..5 of D*'.
Put mu = 1 if eps = 1 and mu = 14 if eps = -1 (14 = -1 mod 3, 14 = 1 mod 13, 14^2 = 1 mod 39). Then
f := mu^(-1)(D*_6 - D*_0) + D_0 satisfies: [D; f] is a (Z_39,7;1)-DM. Conversely, if [D; f] is a (Z_39,7;1)-DM, then
normalising at row 0 gives a beta-route instance with new beta-row beta_6 = (f - D_0) mod 13 (take D* = [D; f]; then
eps = 1, e = 0, mu = 1, and the map returns f).
Proof. D*' is a DM, and its rows 0..5 form a 6-row DM with row 0 zero and mod-13 part beta. By Lemma U their mod-3
part is eps*alpha + e, with the sign eps unique (F(-alpha) != F(alpha)) and constants e_x. Multiplying all seven rows
by the unit mu^(-1) = mu keeps the DM property and maps rows 0..5 to (alpha + eps*e, beta) mod (3, 13), that is to
D'_x + r_x with r_x in 13Z_39 constant on each row (r_0 = 0). Subtracting the constants r_x from rows 0..5 keeps the DM
property and gives [D'; mu^(-1) D*'_6]. Adding the column function D_0 to every row preserves all differences and gives
[D; mu^(-1)(D*_6 - D*_0) + D_0]. QED.
Imports: only the class statement of Lemma U; the CRT; invariance of the DM property under column translation, adding
a constant to a row, and multiplying all rows by a unit. Nothing is used from T2/T6, from the G6/C3/C2 results, or
from the non-anchor S4 rows.
Scope: the labelled anchor and any D* as above (permuting the rows of D* is free).
## Consequences
1. (Text of B.m12.)
2. The beta-first search order (decide beta_6 in Z_13^39 by a demand exact cover: 78 items (x,t) with demand 3, 39
   column items, 39*13 = 507 options; then solve the mod-3 lift of row 6) explores a relaxation, expected but not
   proved to be looser, of the joint Z_39 exact cover used by v2 free0 (items (x,v), v in Z_39, demand 1).
   [HEURISTIC, not evidence: about 1 beta-solution expected, but about 1e23 capacity-feasible partial assignments at
   depth 26; joint-cover pruning is much stronger.] So for this anchor a beta-first engine is not expected to be a
   faster engine for the same question.
3. (Text of B.M1.)
4. Positive-control route if a beta engine were ever built (none is planned; S6): a Singer-type DM over Z_57 (mod-19
   skeleton, index 3). Delete one or two rows, re-find the deleted beta-row(s), read after normalising at row 0
   ((f - D_0) mod 19), and re-lift. These are controls for the engine only, not target evidence.
Scope: exact anchor only; no statement about other DM6(39), CFR(6,39) or six MOLS(39). The beta route and the free
one-row extension are both UNKNOWN. No formal proof or certificate of Lemma U exists; a certificate specification is
frozen separately and has not been executed.
