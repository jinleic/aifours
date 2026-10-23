# Lane info-2 (third target): point-cyclic resolutions of 2-(88,4,1) designs

Owner: worker `InfoCdf`. Contract: `institute/runs/six-lane-2026-10-16/screening/info-2-point-cyclic88-contract.json`
(recorded 2026-10-17T00:38:45-07:00). Lane opened 2026-10-17 00:39:55 PDT (host clock). The k5 lane and the
cpcw-optimal-prep lane are preserved untouched.

## 1. Frozen contract (written between 00:39:55 and 00:43:45 PDT, before any proof writing; exact mtime later overwritten)

### Exact target
For every 2-(88,4,1) design D = (V,B) (|V| = 88, b = 638 blocks, r = 29) and every resolution R of D into 29
parallel classes of 22 blocks: no permutation sigma of V that is a single 88-cycle maps B onto B and maps every
parallel class of R onto a parallel class of R. Equivalently: no 2-(88,4,1) design is cyclically resolvable in the
point-cyclic sense of the source (Definition 5). NOT the target: general resolvability (known to exist), existence
of cyclic 2-(88,4,1) designs (known: 149,494,720 per the source), the class-transitive notion of "cyclically
resolvable" (source Section 1.1 explicitly excludes it).

### Source and definition binding (local copy `sources/axioms-15-00762.pdf`, SHA-256 in `sources/SOURCES.md`)
Topalova, Zhelezova, "Point-Cyclic Resolutions of 2-(64,4,1) Designs", Axioms 15 (2026) 762, published 2026-10-13.
- Def. 2: parallel class = partition of the point set by blocks; resolution = partition of the blocks into
  parallel classes.
- Def. 3 + text after it: automorphism of D = point permutation preserving B; two resolutions are isomorphic if an
  automorphism of the design maps each class of the first to a class of the second. Hence an automorphism of a
  resolution R = design automorphism mapping every class of R to a class of R.
- Def. 5: "A resolution is point-cyclic if it has an automorphism permuting the points in one cycle."
- Section 7: "v = 88 is the smallest v for which the existence of cyclically resolvable 2-(v,4,1) designs has not
  yet been determined ... their possible point-cyclic resolutions are of type T1."

### Baseline
Open per the source (2026-10-13). An untrusted 4-step orbit-stabilizer obstruction is recorded in the contract.

### Acceptance gate (this lane's part)
A complete self-contained written proof of the full quantified statement (no assumption of type T1; short-block
classification, mixed-class exclusion, all stabilizer orders and the missing pair derived from the definitions),
or an explicit flaw/counterexample. Exact finite arithmetic re-checked by an independent script. Semantic positive
control: the explicit point-cyclic 2-(64,4,1) resolution printed in the source (PDF pp. 6-7) is transcribed,
expanded and verified, and the 88 argument's general form must not exclude it (nor v = 52, nor the Lam-Miao
existence family). Parent verification, hostile cross-vendor review and the priority audit are parent gates.

### Plan and limits
Proof text `PROOF.md`; finite checks `code/check88.py` (exhaustive where finite); positive control
`code/control64.py`; general consistency table `code/general_table.py`. Stdlib Python only, <= 1 CPU, no searches.
Claim discipline: computer checks are controls of finite lemmas, not the combinatorial proof itself.

## 2. Status (2026-10-17 00:51 PDT)
WRITTEN PROOF COMPLETE, awaiting parent verification and hostile review: `PROOF.md` (SHA-256 recorded in
`evidence/MANIFEST.md`). The untrusted 4-step candidate in the contract survived my hostile check; every step is
now derived from Defs. 1-5 (short-block classification, no mixed classes / type T1, all class stabilizer orders,
the uncovered pair {0,8}). No novelty or priority claim (parent audit; scout Cyclic88Priority).

Controls:
- `code/check88.py` (receipt `evidence/check88-receipt.json`, stdout `evidence/check88-stdout.txt`): exhaustive over
  all C(88,4) = 2,331,890 four-subsets (stabilizers; admissible short blocks = exactly the 22 cosets of {0,22,44,66});
  exhaustive (h, m) table: only (11,0), (22,0), (88,22); common non-short stabilizer H_11 meets H_4 trivially;
  witnesses 8, 16, ..., 80. Same code on v = 64, 52, 76, 148 behaves as known (64: T1 forced, no contradiction;
  52, 148: mixed (4,1) admissible, not excluded; 76: excluded, as by the Genma-Mishima-Jimbo prime condition).
- `code/control64.py` (receipt `controls/control64-receipt.json`): the published point-cyclic 2-(64,4,1)
  resolution (PDF pp. 6-7) transcribed, expanded and verified (design, 21 classes, invariance, orbit lengths
  1/4/16); lemma checks hold; intersection of non-short stabilizers = <16> = H_4, so no v=88-type contradiction;
  3 corruptions rejected, 1 reordering accepted. First run FAILED because my control applied the full-block form of
  Lemma 6 to the short class as well (a control bug, not a proof issue); fixed to the general form
  "d in Stab(P), x, x+d in X => d in Stab(X)", then PASS.
- `code/general_table.py` (outputs `evidence/general-table-{2000,10000}.txt`, `evidence/general-table.json` for
  v <= 10000): the general form of the argument excludes, for v = 4 (mod 12) <= 10000, exactly v = 4p (p prime,
  p = 7 mod 12; reproduces the GMJ prime condition) and v = 8p (p prime, p = 11 mod 12); it excludes no
  known-existence value (52, 64, 4q for primes q = 13 mod 24). Corollary in PROOF.md Section 6: no point-cyclic
  resolution for any v = 8p, p prime = 11 (mod 12) (88 is the smallest).

## 3. Log
- 00:39:55 lane created; source PDF saved (d5170670...).
- before 00:43:45 contract frozen in this README; 00:45 check88 run; 00:46-00:47 control64 (fail -> fix -> PASS);
  00:48 general table; 00:50:03 PROOF.md final; 00:50:24 check88 receipt; 00:50:38 general table 10000; 00:51 manifest.
- 01:13:07 PROOF.md revision r2 installed (write-up only); 01:13:24 general-table receipt and MANIFEST-r2.

## 4. PROOF.md revision r2 (write-up only, after the parent's hostile review)
- Review: `institute/runs/six-lane-2026-10-16/review/point-cyclic88-hostile-review.note.md` (Claude Opus 5.5 max,
  VERDICT ACCEPT, no fatal or major findings; minor items m1-m4). This supersedes the "awaiting review" wording in
  Section 2.
- Old (reviewed) r1: SHA-256 `227c200c6c0adb2874d4e1e482e88ad4de5edbe43c4ce12f8e1625f70de36bfa`, preserved
  byte-identical (checked before and after copying) as `archive/PROOF.r1-reviewed-227c200c.md` (mtime 00:50:03).
- New r2: `PROOF.md`, SHA-256 `d6faaf1151d6397b6ebc2a7c434b7b8df9518b91ed53c3dc944a0b9c71a78358` (mtime 01:13:07 PDT).
- Changelog:
  - m1: Section 0 now quotes verbatim (PDF text layer, normalization stated) Defs. 1-5 and the isomorphism sentence
    after Def. 3, notes that the source has no separate definition of an automorphism of a resolution, and states
    the binding (design automorphism mapping each class of R to a class of R = self-isomorphism in the sense of the
    quoted sentence) with the reviewer's robustness remarks. The working definitions and the Theorem are unchanged.
  - m2: Section 6 now separates the one mathematical claim (the Corollary) from consistency checks; every source
    statement (GMJ prime condition, Lam-Miao family, v = 52 orbit lengths 4 and 13 and six designs, 258 resolutions
    for v = 64, open status, T1, Theorem 1, convention) is backed by a verbatim quote in the new Appendix A; the cited
    papers [5], [6], [26] are marked as not read. The "exactly 4p and 8p up to 10000" statement is backed by the new
    receipt `evidence/general-table-receipt-v1.md` (SHA-256 ec3643ca...cee9: command, host time, Python 3.9.6, exact
    range 16 <= v <= 10000 with 833 values, script SHA 727446a0... unchanged, stdout byte-identical to the r1-time
    output, GMJ list equality True, PROBLEMS: none, A u B equality True).
  - m3: the Corollary's substitution list now includes 44 -> 4p (H_2 and the diameter pairs of Lemma 2) and
    28 -> r - 1 (Lemma 5), plus 66 -> 6p, 11 -> p, 21 -> 2p - 1 and the explicit H_4, H_p, H_2p.
  - m4: a definition "R has type T1 if the set S of short blocks is a class of R" (quoting the source's T1 line)
    precedes Corollary 4, whose title now reads "(no mixed class; R has type T1)".
  - The semantic-control bullet now states that the v = 64 transcription is by hand and not machine-compared with
    the PDF text layer (reviewer Task 4 limit).
- No mathematical change: a diff of r1 and r2 from the Theorem statement through the end of Section 5 shows only the
  inserted T1 definition and the new Corollary 4 title (run 2026-10-17 01:13 PDT).
- Hashes of all lane artifacts after r2: `evidence/MANIFEST-r2.md` (the r1-time `evidence/MANIFEST.md` is kept).
- Not touched: `review/point-cyclic88-kernel-worker-v1/` (Cyclic88Kernel), the k5 lane and `cpcw-optimal-prep/`.
  The lane is idle after this revision, awaiting a new target.
