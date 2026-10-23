# Desk static reading (M7CutsHostileDesk), written 2026-10-18T01:25:23-07:00 while both reviewers ran

Snapshot-relative paths; LF = 1-based index into text.split('\n'). Desk readings only: not reviewer findings, not a
parent verdict. No solver, encoder, checker, generator or oracle was run by the desk; only in-process SHA-256 and JSON
value comparisons of snapshot files.

## Hash and value cross-checks (in-process)
- All 8 assignment pins and the 3 parent-document pins match (manifest 4b563226…63fb).
- K3-Q4-SIDECAR.r1.json: all 20 file SHA references match the copied files (proof_stream.py checked at the lane
  source; it is not in the snapshot). Source CNF 7fca33f1…2001 equals lex-meta source_cube_cnf_sha256, cube-meta
  cnf_sha256 and the original screen receipt; lex CNF 059be616…8c4f equals lex-meta cnf_sha256. Screen facts match:
  original UNKNOWN 1800.145 s rc 0; lex r1/r2 UNKNOWN safety stop 769.881 s / 1229.385 s, rc -15, both on lex meta 7bef0b78….
- cert_r2 receipts pin k3_cube_certify_r2.py 49677766…; solver/checker commands carry `-t 3600` each (3600/3600).
  K3-CERTIFICATION-DRIVER-DELTA.r2.json frozen_at 21:39:20 precedes the A/C321 start 21:39:49.

## Static readings
D1 (oracle is a genuine observation of B). gram_encB.py:113-118 allocates gv before any other variable; g() reads gv;
   the --fix-json branch (gram_encB.py:203-215) iterates the same gv dict and emits +v/-v per B's own pair. Designs carry
   pairs only, never indices, so an identity decode plus the all-nonzero sign control forces B-pair(v) = A-pair(v) for every
   v; base-prefix identity shows the branch only appends. Not an echo of A. Assumptions: --fix-json changes nothing before
   the units (checked by prefix identity per design); B base hash 42a5f304… equals B_C321/B_C411 metadata (checked) and also
   B_C311 metadata (static equality only; bmap_oracle_r1.py:115 checks only C321/C411, and k3_direct_B_r5.py:62 would
   refuse a B/C311 run, so a B route for C311+cuts needs a new binding).
D2 (generator family). emit() over FRAMES x off_points x template gives the draft section 3 family. shape_report is a
   complete characterisation relative to A's inverse map: per (frame,p) group, 45 = 3*C(6,4) and 360 = 6*C(6,3)*C(3,2)
   are the maximal numbers of distinct admissible keys, so 588 full groups + no bad shape + no duplicate + 238140 total
   pins the family exactly. Semantic correctness of literals for A rests on amap = gram_enc.build vmap = k3_cubes.variable_map.
D3 (B decode inside the generator). run_b/decode_b_map (k3_cuts_r1.py:238-274) read only the last 2646 lines before the
   `vars` line; no header, base-prefix or sign-control check, and the oracle receipt is hashed (k3_cuts_r1.py:298) but its
   status is not asserted. Adequate only together with the pinned oracle receipt.
D4 (bindings vs draft). Draft r1 section 3 (drafts/AMENDMENT-4.r1.md:69) says the generator binds the source cube CNF SHA;
   the receipt has no source-CNF field. The header increment exists only as a stated rule (cuts_r1_receipt.json:31);
   no appender/strengthened-CNF code exists.
D5 (local count, by hand). 4^6 - 3*3^6 + 3*2^6 - 1 = 2100; forbidden = 3*6!/(4!) + 6*6!/(3!2!) = 90 + 360 = 450.
D6 (Psi(f) prediction, by hand). With H = {1,2,4}: f0 + lambda*x is a permutation iff lambda in {1,5}; psi_gram picks
   m0 = 2, so f + lambda'*x is a permutation iff lambda' in {0,3}. Every row-frame point therefore has exactly one
   non-neighbour among 6 frame cells (weight 5); for column frames the analogous unique ratio is mu = 5 (weight 5). So
   (2940,0) = 588*C(5,4) is the right prediction. Weight 5 exceeds the (W) bound 4 for any orthogonal triple, so this
   configuration is outside every triple encoding: a non-vacuity check only.
D7 (control e). Once decode gives bmap == amap, block-SHA equality and set equality are tautological, and the swapped-map
   SHA difference is trivially true. The only non-tautological datum is the runtime decode itself.
D8 (control d). Confirms for the 22 listed generators and transposition what the uniform definition already gives;
   minus-one non-vacuity is weak but real (clauses_a[0] is moved by C311 columns(4,5)+squares(2,3)).
D9 (instance and standard). Draft r1 section 5 (LF84-85) names only encoder-A C311 instances; B_C311 b3ec0108… exists and
   no B lex C311 exists. README.md:80-82 (Phase C) asks for two encodings. Section 1 asks G1/G2 verdicts to state their
   standard but does not fix the standard of the C311+cuts certification.
D10 (composition). The cut clauses are claimed valid for every K3 configuration (transport lemma + G1/G2), so the
   lex-minimal orbit member, being an actual K3 configuration in C311, satisfies them; H-invariance is a second, syntactic
   route and also holds.
D11 (dating). Oracle pin frozen_at 00:48:54 (mtime 00:49:12) < oracle start 00:49:18; generator pinned_at 01:00:31
   (mtime 01:00:53) < run start 01:00:59; sidecar 00:51:30, errata 00:52, draft 00:53 follow the 00:42:59 disposition.
   GENERATOR authority cites a parent label (01:12 PDT) that is later than the host clock; LOG.md:167 records this.
D12 (wording). K3-Q4-SIDECAR.r1.json:40 "holds ... only when the triple minimises" reverses the logical direction; the
   lemma establishes G4 when the triple is minimal.
D13 (interim draft). README.md:207-209 names review/drafts/AMENDMENT-4.r2.md with no SHA; the archive copy cannot be
   hash-linked to it; the r2 name was used before r1, so a frozen successor needs an unambiguous new name.
D14 (procedure). Draft r1 drops the old draft's single <=1800 s screen rule and names no driver, caps or outcome classes for
   a C311+cuts run; those belong in the frozen version and a pinned driver delta.
