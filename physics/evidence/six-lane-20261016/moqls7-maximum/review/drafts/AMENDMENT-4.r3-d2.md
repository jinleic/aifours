# Amendment 4 r3: transported own-row/column-frame cuts for the K3 C311 cube

**Status: DRAFT 2 FOR PARENT SOURCE REVIEW, NOT FROZEN, INACTIVE.** It becomes usable only as the frozen file
`review/AMENDMENT-4.r3.md`, a byte-identical `cp -n` copy of this draft made after the parent source review PASSes
(parent AMENDMENT-4 disposition, decision 6), together with the frozen delta `review/K3-CUTS-CERT-DELTA.r2.json`.
Draft 1 (`review/drafts/AMENDMENT-4.r3.md`, 1ded55bb85a44fc7e7c1be22c49dfe44b8c28ba32ebea0cdb568c6af5e55c366) is
preserved unchanged and superseded by this draft, which answers the parent source review 15aae4593f5e6f0b (§11).
The name r2 is never used. Written 2026-10-18 02:48 PDT (host clock). This text makes no claim about K3 or M(7).

## 0. Bindings
Predecessors:
- `review/drafts/AMENDMENT-4.md`: d9794b9d7b9ba62747a8d78d7386a94acb2819f3faee33d6cb192a2a0347d7ee.
- Interim unreviewed text written at 23:47, originally named `AMENDMENT-4.r2.md` (the name is retired; m15), archived
  as `archive/AMENDMENT-4.interim-2347.unreviewed-draft.md`:
  e72233cac5d7a9ff9124ed7aa3ab72230cbf36703200a90c4445acbf7aa62870.
- `review/drafts/AMENDMENT-4.r1.md`: ef87fa492abcc9a86e02be9d8f14f7810908a83458b32e38788f99f3acc5abb1.

Parent records and reviews (under `institute/runs/six-lane-2026-10-16/review/`):
- K1 verdict `moqls7-k1-parent-verdict.md`: 1cd0603c5dc3e5d724725388de6f9130721c3b686bda3b6ebde765a53dd7dfb8.
  Lane `review/K1-THEOREM.r3.md`: 2d77c63719fafd1e7f7cfe2a3161931f2e90dff0976e3ee9c5083a88d076a096.
- K2 verdict `moqls7-k2-parent-verdict.md`: 25ecb6bab8caad2a7e9c79faa8fbf8d2f34befab8c000338d8d14d63df811242.
  Lane `review/K2-THEOREM.r2.md`: a73a90078a3b9923935755d2663ecba645ba7f231d8f07384b8f34656ab532cd.
- K3 cover disposition `moqls7-k3-cover-parent-disposition-v1.md`:
  fbfc0e1079cd94bcca65a9d1c68ef9f4ac545181d7f9f8bed02feb244aaff369. Its desk RESULT:
  0f80460c1059a10fe6f3c614e55a5fdd7fd2af6606cc0b8b80781cc8d89eef84.
- AMENDMENT-4 disposition `moqls7-amendment4-parent-disposition-v1.md`:
  3c9373c0ca7a8a98d9af3b2288b04076cad421e65ce645638ab151b850694e44. Its desk RESULT:
  3792077335885fe78c8c632c347502314148592fec90177121b6a16384c55dac. Review notes: Codex
  970430f7b51cbd6b987fc2e101844baa9a39fb2bf653f8a03c120674f0c02601; Claude
  dc66f3c118ad61f2bb966a31f127570bc83f68d44ce778a9be77d982e3de364a.

Block evidence (r1, reviewed as faithful; receipt = block evidence only):
- Generator `code/k3_cuts_r1.py`: 0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a; pin record
  `review/AMENDMENT-4.GENERATOR.r1.json`: 4c23ec44b7189e9df9fd36b39ee2d0a1e62e71bc02bdfd73ff49ab194ac65dd3.
- Receipt `evidence/k3cubes/cuts_r1_receipt.json`: 9cfc0e81bed2cbcbdcd2c205d697dc107b184609f722f0f799225e39092babbf.
- Block: 238140 clauses, 6974640 bytes, SHA 05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd.

Runtime B-map oracle: script `code/bmap_oracle_r1.py` 13f4a5e6c34b61478fcdbb5fddc1a934901c1b82480553cfee8b0f958f73cd8e;
pin record `review/K3-BMAP-ORACLE.r1.json` df28f4c558ac5d063d3a4057289ed4b3ac48252c00f48be370a1f8df7910f887; receipt
`evidence/k3cubes/bmap_oracle_r1.json` 6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c.

Lane texts relied on: `review/AMENDMENT-2.r1.md` 82ee394ef6b41c62991e3e8cce4077159a9a6432522abd0f7b1aa48ad0f714e0;
`review/AMENDMENT-3.r1.md` 374978c66af3c3f3a82a518a0466d4bf80e79accad845741edc33d48404bf3cc and its bindings
0d842cf890efe147662d7ca2500a3bea1e74c98b144931a0c914750df4fa0316; `review/GRAM-ENCODING.r2.md`
c6c506a7d1ecba15b2e31393b0da4caa248db5c9227f512c0df9ea5bd07ad6c7; `review/G6-G2-DERIVATION.r1.md`
8790e9e1af45d4b49e397a06fc4b8dbd70742278698c55561e03f0904f07e791; `review/K3-Q4-SIDECAR.r1.json`
34bb5251ce27e8c112c690fe2d6acec162f33d0e404251af5e54aff9cf3d16e5; `review/K3-ERRATA.r1.md`
85fa93fadaa636949c1c8c26672744833f8a42bc4ddd73d6328343eeeb47c662.

Chosen instances (§7):
- A route: lex C311 `explore/k3lex/A_C311.cnf` 059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f
  (metadata 7bef0b78007151d94661181244fa8614c114705522b58fc16cf287014bde190d), built on the original A C311
  7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001 (metadata
  3b2ab04f2b42b799169bdccf3d868f544ba571ff1d72e18d0cf68187a0f4d9ed; A base
  d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388).
- B route: original `explore/k3cubes/B_C311.cnf` b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077
  (metadata bfa298eea4a6b102a16e15663d42c2cdf86ab7ab093f86bdecb7d8bf8d28a056; B base
  42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac). No B lex input is generated.

Gate CNFs (§2): A_C321 d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388; B_C321
8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6; A_C411
2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2; B_C411
01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8.

New code bound by this text (caps and remaining pins are fixed in the delta):
- Generator r3 (controls C1–C4, guarded) `code/k3_cuts_r3.py`:
  e636924c919c94e2107b33f42f61cd6b6dd3b0b20a57972a842f43b65c8f3d0d.
- Appender and certification driver r2 `code/k3_cuts_certify_r2.py`:
  5b7ab798bb1d7d821152c6a94d4ca4bad542b93f93e0e362ba3da3527d58f0ff.
- Appender, parser, guard and transport controls (C5–C9) `code/k3_cuts_certify_controls_r2.py`:
  c9e287d995e4306e4c70f799e8bd2508725ac8a670c6724bda7de64fee522ef1.
- Stage guard `code/stage_guard_r1.py`: 2d945ed0274445ced50a99f6ed309734073aff92da79e2e3e3fe43ecdeae0fba.
- Preserved, never run, superseded: generator r2 `code/k3_cuts_r2.py` 5c1c1d67…bdd9, driver r1
  `code/k3_cuts_certify_r1.py` 0e978302…0b5a, controls r1 `code/k3_cuts_certify_controls_r1.py` 1dc761d1…0025.

Naming: Gram-G1 … Gram-G5 are the conditions of `GRAM-ENCODING.r2.md`; G1 and G2 without prefix are the exclusion
gates of §2.

## 1. Hypotheses (all must hold)
H1. K1 is parent-accepted (verdict 1cd0603c…dfb8), with its stated caveats.
H2. K2 is parent CORRECTNESS-ACCEPTED (verdict 25ecb6ba…1242), with its qualifiers: computer-assisted, conditional
    on the stated trust base and on the 35-class provenance caveat, and not a new gate (m7). With H1, every
    non-classical 3-MOQLS(7) is a K3 triple. G4 is justified, by the minimality lemma (`GRAM-ENCODING.r2.md` §2,
    `LEMMAS.md` 69–78), for triples that minimise the number of non-classical squares. With K1 and K2 excluded,
    every K3 triple is minimal, so each square is heavy on all 14 of its own lines (m2).
H3. Encoder soundness for the exact K3 base instantiation (m13): three quantum squares, no classical L, heavy,
    `--sym`, that is `gram_enc.build(3, None, True, True, None)` and `gram_encB.py --squares 3 --heavy --sym`.
    Every K3 triple, after the `--sym` normalisation of H5, gives g-values satisfying Gram-G1 … Gram-G5 and G4,
    and each encoder's auxiliaries can then be set (§8) so that every base clause holds. No parent file yet
    accepts this exact instantiation; it is an obligation of the composition review (decision 8; desk Q6 item 3).
H4. Scope: K3 only. The ONB lines are the 14 rows and columns; there are no classical symbol lines. Only minimal
    configurations are covered, and by H1–H2 these are all K3 configurations.
H5. The accepted three-cube cover and `--sym` WLOG (K3 cover disposition Q1, with the K3-ERRATA E4 wording).

## 2. Standard and gates (decision 1: A+B, no deviation)
Standard, per lane README Phase C (`README.md:80-81`, two encodings) and as for K2. Each of C321, C411 and C311 plus
the cuts needs a DRAT-checked UNSAT of its exact input on encoder A and on encoder B, plus a parent replay. The
DRAT check means solver rc 20, checker rc 0, exact `s VERIFIED`, no safety stop, and the regenerated input hash.
A-only acceptance is not available. A B certificate counts only after the runtime B-map oracle.

- G1: a parent verdict accepting the exclusion of C321 under this standard, naming A_C321 d598507d…8388 and B_C321
  8b7b8124…12c6.
- G2: a parent verdict accepting the exclusion of C411 under this standard, naming A_C411 2b92f5b1…ddf2 and B_C411
  01acf464…8bf8.

Producer receipts alone satisfy neither gate. No full-cap UNKNOWN or miss on C311 is a premise: the cuts follow from
G1, G2 and §3 alone. Certificate status is tracked in the lane README and LOG, not here.

Activation (decision 3). C311+cuts solving may start only when all of these exist: this text frozen, the delta
frozen, the generator r2 receipt PASS and the controls receipt PASS, all after the parent source review PASSes.
Solving does not wait for G1 and G2. No C311 result is accepted, and no composition is reviewed, until G1 and G2 hold.

## 3. Transport lemma (all 14 own lines, all 42 off-line points, every role assignment)
Let ℓ be any of the 14 own row/column lines and p any point off ℓ. For each square x, let w_x be the number of
r ∈ ℓ with g_x(p,r) = 1.
- w_x ≥ 1: ψ_{x,p} is a unit vector expanded in the ONB on ℓ (Gram-G3).
- The point of ℓ on p's other line (its column if ℓ is a row, its row if ℓ is a column) has g_x(p,·) = 0 by Gram-G1.
  It carries no variable. On the remaining six points, the neighbour sets of the three squares are pairwise disjoint
  by Gram-G5. Hence w_1 + w_2 + w_3 ≤ 6.

**Case (4,1,1).** If some w_a ≥ 4, the counts are exactly (4,1,1) and all six positions are used. Apply, in order:
- if ℓ is a column, the transpose of the cell array, acting simultaneously on all three squares (m14);
- a row relabelling ρ with ρ(ℓ) = 0 and ρ(row of p) = 1;
- a column relabelling κ with κ(column of p) = 0, the four a-neighbours sent to columns {1,2,3,4}, the b-neighbour to
  {5} and the c-neighbour to {6};
- the square relabelling a → 1, b → 2, c → 3.

These maps preserve the QLS axioms and mutual orthogonality, so the image is a K3 triple. Its Gram pattern meets the
18 signed C411 cube literals, the `--sym` units, Gram-G1 … Gram-G5, and G4 on all lines (H2); G6 follows by
`G6-G2-DERIVATION.r1.md`. With the auxiliaries reconstructed as in §8, it therefore satisfies every clause of the
CNF A_C411 2b92f5b15cd641e4a07ecec241b7957deac972aa3c7333056ff3e739e46addf2 and every clause of the CNF B_C411
01acf46491feef2fc26060266af8c2dead0cec9832c9e9ecbed83f886ecb8bf8. This contradicts G2.

**Case (3,2,1).** If w_a ≥ 3 and w_b ≥ 2 for distinct a, b, the counts are exactly (3,2,1). Use the same maps with
the a-neighbours sent to {1,2,3}, the b-neighbours to {4,5} and the c-neighbour to {6}. The image satisfies every
clause of A_C321 d598507d84a8d7595b30a100d528dca08bc0ce1aa71978583f09aac188298388 and of B_C321
8b7b8124dbaf7088626ae853f4e10fe9590459dde1676377326ceecfb6d812c6, which contradicts G1.

Transposition preserves the QLS axioms and globally reindexes every tensor ONB. This is existence transport; it is not
claimed to be one of the source's listed set-isotopy generators. No transport through arbitrary ONBs or through
classical symbol lines is used.

**Consequence.** In every own row/column frame and at every off-line point, w_x ≤ 3, and never both w_x ≥ 3 and
w_y ≥ 2 for x ≠ y. Every heavy local type is (3,1,1). Under H1–H5 and G1–G2, the cut clauses therefore hold for every
K3 configuration. So they may be appended to the original B cube as well as to the lex A cube (decision 1).

## 4. Cut family and appender (MAJOR-A split of r1 §3)
(i) **Block generator, as implemented.** The emission is that of `code/k3_cuts_r1.py`: 14 frames × 42 off-line
points × 6 available cells. That gives 26460 at-most-three clauses (one per square and 4-subset) and 211680 mixed
clauses (one per ordered x ≠ y, 3-subset R and disjoint 2-subset T), 238140 distinct clauses in all. Every literal
is a negative g literal and there are no auxiliaries. Serialised as DIMACS lines in emission order, the block has SHA
05f31da4…e6dd. The r1 receipt is block evidence only. Contrary to r1 §3, the r1 generator opens no C311 input,
selects no instance and binds no strengthened CNF; its header increment was descriptive text.

(ii) **Appender and certification driver** `code/k3_cuts_certify_r2.py`. For the named route it does the following,
in order:
- regenerates the input in memory by the r3 method:
  - A: `gram_enc.build` plus the C311 cube clauses, which must hash to the base d0d884f9… and the original cube
    7fca33f1…, then the AMENDMENT-3 lex clauses by the `k3_lex` make method, giving 059be616…;
  - B: `gram_encB.py` on stdout plus the C311 cube clauses, with base 42a5f304… equal to the oracle base, giving
    b3ec0108…;
- asserts the input header (A lex 107513/659168, B 461370/1629802), the input SHA, and byte equality with the named
  input file (prefix equality);
- re-emits the block with `k3_cuts_r1.emit` on the wrapper map and asserts 238140 clauses and SHA 05f31da4…;
- writes the incremented header and asserts A lex 107513/897308 or B original 461370/1867942;
- computes the strengthened SHA, which must equal the value in the controls receipt;
- streams the strengthened bytes from memory into two FIFOs, one read by the solver and one by drat-trim, hashing
  exactly the bytes written to each. Binary DRAT flows solver → FIFO → drat-trim stdin. No CNF or proof file is
  written.

For B, the driver also asserts that the oracle receipt says PASS with its pins, and binds the B_C311 metadata
bfa298ee… to the oracle's base hash, wrapper pin and encoder pin. This is the new-version oracle binding of B_C311
(m5).

Execution safety (parent source review items 1–4; §11):
- Preparation (in-process A build, B encoder child, appending) and the native pipeline each run inside a stage guard
  (`code/stage_guard_r1.py`). The guard covers the driver and every descendant, which it finds recursively through
  libproc. It enforces aggregate RSS ≤ 3.5 GiB, the 12e9 floor and a stage wall cap fixed in the delta. A sampler
  exception is itself a trip. A trip, or an external SIGTERM, stops all descendants by SIGTERM, waits at most 30 s
  and ends in UNKNOWN.
- Any descendant still alive after the grace period is listed in `evidence/k3cubes/C311cuts.QUARANTINE.json`
  (exclusive create, never removed by code). While it exists, the driver, generator r3 and controls refuse to start.
  No SIGKILL is sent and no subprocess timeout argument is used.
- Solver and checker status lines are parsed from bytes: remove only `\r`, split on `\n`, keep the lines starting
  with `s `, with no stripping. A certificate needs exactly [`s VERIFIED`] from drat-trim and exactly
  [`s UNSATISFIABLE`] from the solver.
- Each route uses one deliberately created directory, `evidence/k3cubes/C311cuts_<route>_r2` (made by mkdir; if it
  already exists, nothing runs), and every output in it is exclusive-create. A receipt is written on every outcome.

Literal map: the wrapper map `k3_cubes.variable_map()`, asserted equal to encoder A's map at run time and equal to
encoder B's map by the oracle; C3 re-decodes B's map at run time.

## 5. README:91 ruling (decision 2, MAJOR-C)
- The cut clauses are **derived conditional clauses**: consequences of H1–H5, §3 and the accepted exclusions G1–G2.
  They are not definition-level necessary conditions of quantum Latin squares.
- README:91 ("every necessary-condition encoding must admit all matched genuine controls before production") is
  applied at component level by the parent ruling (AMENDMENT-4 disposition 3c9373c0…4e44, decision 2). The recorded
  limitation is that no genuine K3 positive can be supplied, since one would refute the target. Under the ruling:
  - the base A and B encoders keep their 26/26 matched component controls (`evidence/gram/review_controls_r1/summary.json`
    6ce1ddc241a88da9f0d2fdc0be3551b8a73f5659a979c5034ebcee5caaecd685), and the K2 verdict's README:91 timing
    deviation still applies;
  - every cut clause is satisfied by all five classical AG(2,7) triples (slopes 1,2,3; 1,2,4; 2,3,5; 4,5,6; 1,3,6).
    These are genuine mutually orthogonal triples. The check covers the cut clauses alone, because the classical
    triples violate base G4;
  - C1 (2100 local assignments, exactly 450 rejected: 90 of type (4,1,1) and 360 of type (3,2,1), 0 mismatches) is
    re-bound to this frozen text by generator r3 (§6).

  This is a ruling, not a claim that a genuine K3 control passed.
- The genuine weight-5 Ψ(f) placed beside two classical squares gives exactly (2940, 0) violations. This is a
  non-vacuity check that the cuts bite; that configuration is not a K3 triple.

## 6. Controls before any use
Generator r3 (`code/k3_cuts_r3.py`, the guarded version of the never-run r2) refuses to run unless this frozen text
names its SHA, and it binds this text's SHA. The r1 controls bound draft r1; r3 re-binds them to this text (m15). It
runs entirely inside a stage guard (1800 s, 3.5 GiB, 12e9 floor), with every encoder B child owned by the guard.
Its controls:
- C1: the local coverage of §5.
- C2: exact counts, set distinctness, and the shape characterisation (588 groups of 45 + 360).
- C3: the literal maps. A: runtime equality with the wrapper map. B: the oracle receipt (PASS and pins) and the B_C311
  binding are asserted first; the B base output must equal the oracle base. Each of the 12 `--fix-json` designs must
  then reproduce the header, the byte-identical base clause prefix, exactly 2646 distinct units, and a positive count
  equal to the design population (m9). The runtime decode is the only datum. Block-SHA and set equality are recorded
  as its consequences, and the swapped-map test as SHA sensitivity (m10).
- C4: invariance under the 22 AMENDMENT-3 lex generators and under transposition of all three squares. As a
  non-vacuity check, the family minus one clause must fail invariance for some generator.
- Every mutation (cross-frame literal, mixed square merge, column frames replaced by duplicated row frames,
  at-most-four, one clause dropped, wrong column-frame exclusion) stores its full shape report, its set
  distinctness and its count separately, together with the failing checks (m11). The interpreter, flags and the
  path and SHA of every module are recorded (m12).

The appender controls (`code/k3_cuts_certify_controls_r2.py`):
- C5: the bindings among this text, the delta, the driver, the stage guard, the generator r3 receipt, the oracle
  receipt and the B_C311 metadata.
- C6: the pre-solve appender checks of §4(ii) on both routes, plus negative controls that must each raise in the
  intended check: a mutated block clause; a header without the increment; the wrong instance (by SHA and against
  the file); a one-byte change (against the file and by SHA); oracle receipts with status FAIL, with another B base
  or with another receipt SHA; and B_C311 metadata with another base hash or another file SHA.
- C7: tiny-CNF transport controls with cadical and kissat through the production streaming function. The input is
  UNSAT only with its appended block; the expected results are:
  - with the block: verified, and both feeds hash to the expected bytes;
  - SAT base alone: rejected;
  - checker fed without the block: rejected, with the feed-SHA mismatch detected.
- C8: status-line parser controls. Synthetic logs with leading, trailing or tab whitespace, duplicate lines,
  `s NOT VERIFIED` or `s TIMEOUT`, and `s UNSATISFIABLE ` with a trailing space are all rejected. The CR-prefixed
  drat-trim form is accepted. Replays of the real A/C321 checker and solver logs are accepted, and the B/C321 r5
  timeout log is rejected.
- C9: guard controls, each writing quarantine records only in the controls' own directory:
  - a wall-cap trip, an RSS trip (injected sampler) and a sampler exception each stop an owned child by SIGTERM
    (return code −15);
  - a child and grandchild that ignore SIGTERM are found, are quarantined after the grace period, and exit by
    themselves;
  - an external SIGTERM to a separate guarded process stops its child and gives a trip;
  - an external SIGTERM to a separate process running the production streaming function on PHP(12,11) stops solver
    and checker and gives UNKNOWN, for cadical and for kissat.
  The control directory itself tests the creation-only rule: a second mkdir must raise.

Order: freeze this text and the delta, then run generator r3, then the controls, then the first launch.

## 7. Instances, caps and outcomes
- A route: lex C311 059be616… plus the block, giving header 107513/897308. CaDiCaL 3.0.1, binary
  601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa.
- B route: original B_C311 b3ec0108… plus the block, giving header 461370/1867942. kissat 4.0.4, binary
  05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848.
- Checker: parent-trusted drat-trim, binary 111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4,
  source d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee.
- Caps and policy, fixed in the delta:
  - solver 3600 s;
  - drat-trim `-t 7200`. Its clock starts at checker start and so includes the FIFO wait during the solve;
  - cooperative wall guard 7320 s; stage guards of 900 s for preparation, 7500 s for the pipeline (wall guard + 180)
    and 1800 s for generator r3;
  - no separate exploratory screen: the certified run is the only search;
  - one attempt per route under this delta, and at most one C311+cuts pipeline at a time;
  - lane at most 4 busy processes and 8 GiB. B/C411 r5, the authorised B/C321 r6 retry and the parent A replays keep
    priority.
- Outcomes:
  - VERIFIED_UNSAT_CASE only with the full predicate of the driver;
  - SAT_PATTERN_ONLY is a Boolean pattern, not a witness;
  - everything else is UNKNOWN, and UNKNOWN is never relabelled.

  The old C321/C411 proofs certify nothing about a strengthened input. A parent replay is required.

## 8. Composition to be reviewed by the parent (decision 8)
K1 ∧ K2 ⇒ (minimality) G4 on all own lines ⇒ `--sym` WLOG (H5) ⇒ three cubes C311, C321, C411 ⇒ {C321 and C411
excluded under the A+B standard (G1, G2); transport (§3) ⇒ the cuts hold for every K3 configuration; C311 + cuts
certified UNSAT on A and on B} ⇒ no K3 triple.

Encoder instantiation and auxiliary reconstruction (H3, m13). Take a K3 triple normalised by `--sym` and set every g
variable from its Gram supports. Then set the auxiliaries as follows.
- Encoder A:
  - each AND auxiliary h = g(p,r) ∧ g(q,r) to that value;
  - each G4 guard w (one per square, line and off-line point with at least three possible neighbours) to "the
    point has at least three neighbours on the line";
  - all other Gram-G1 … Gram-G5 clauses are direct clauses on g.
- Encoder B:
  - each product m = g(p,r) ∧ g(q,r) to that value;
  - each register of the sequential counters for "≥ 1" and "≥ 2" (full equivalences over prefixes) to its true
    prefix threshold;
  - the registers of the one-directional "≥ 3" counter to their true prefix thresholds, and its output to "at least
    three of its items". One-directional definitions are satisfied by the true values.
- Cube units and same-ray identities (G6) hold by the choice of cube and `G6-G2-DERIVATION.r1.md`.
- Lex, on the A route only: take a lex-minimal member of the H-orbit. All 22 generators preserve base, cube and cuts
  (C4; desk Q5). Set each prefix-equality auxiliary to the truth of "equal so far". AMENDMENT-3's controls show
  exhaustively, for comparator lengths up to 4, that auxiliary values exist exactly when the Boolean lex
  comparison holds. The general-length chain argument is part of this review.
- Cuts: no auxiliaries; they hold by §3.

A K3 triple would therefore satisfy both the strengthened A lex input and the strengthened B input. Certified UNSAT of
both excludes K3 under H1–H5 and G1–G2. H3 and the lex-representative step are part of the parent's composition
review. Only after that review would the K1, K2 and K3 exclusions together bear on M(7). No such conclusion is drawn
here.

## 9. Resources and freeze rules
- Before regeneration and again before the native pipeline: a fresh gate of at least 12.2e9 bytes plus the
  projected retained growth (10 MiB: logs, checkpoints and one receipt).
- During each stage: a guard over the process and all its descendants enforcing the continuous 12e9 floor, aggregate
  RSS at most 3.5 GiB and the stage wall cap; checkpoints every 15 minutes during the pipeline; SIGTERM only with a
  30 s grace; survivors quarantined; no CNF or proof file.
- A failed gate gives one UNKNOWN receipt in the route directory; it is reported once and the worker then waits.
- This text becomes usable only as the frozen `review/AMENDMENT-4.r3.md`, after the parent source review PASSes,
  together with the frozen delta. Frozen files are never rewritten; fixes go into new versions.

## 10. Errata and new-version fixes (desk m1–m16; frozen files unchanged)
This section is the next sidecar/errata version of `review/K3-Q4-SIDECAR.r1.json` and `review/K3-ERRATA.r1.md`, and
the correction list for r1 and for the generator r1 artefacts.
- m1. Sidecar :40. The omission of the K2 half applies only to AMENDMENT-3.r1, the receipt scope fields and the old
  draft. `AMENDMENT-2.r1.md`:5-6 does name the K1/K2 exclusions.
- m2. Sidecar :40. It should read: "G4 is justified, by the minimality lemma, for minimal triples; with K1 and K2
  excluded, every K3 triple is minimal" (H2).
- m3. Sidecar :47 and ERRATA :59-60:
  - `GRAM-ENCODING.r1.md` already contains the minimality G4 argument;
  - the "K1 section 8" pointer is the `gram_enc.py`:15-16 comment, a dependency-reference error recorded at
    `GRAM-ENCODING.r2.md`:25-27;
  - the r2 digest ends …d6c7 (c6c506a7…d6c7), not …d7c6;
  - the destination `GRAM-ENCODING.r2.md`:52-65 and `LEMMAS.md`:69-78 is unchanged.
- m4. Provenance exceptions, recorded as post-hoc provenance and not as preregistration:
  - the AMENDMENT-3 bindings were written after the lex input was generated (lex metadata mtime 21:20:58) and before
    its search;
  - the AMENDMENT-2 `g6_controls` receipt was written at 20:15:24, after the first cube screen started at 20:13:35.
- m5. ERRATA :22-23. "Both B cube metadata files" means B_C321 and B_C411. A third file, B_C311 (bfa298ee…), exists
  and was only statically equal. It is bound to the oracle by this version's driver and controls before any B/C311
  use.
- m6. Sidecar binding 1 (written 00:51:30, after the lex screens ended at 23:47:55) is post-hoc provenance. It is not
  the pre-search binding of `AMENDMENT-3.r1.md`:46.
  - The ordering cited at :31 (driver r2 at 21:38:35 and delta r2 at 21:39:40, both before 21:39:49) rests on the
    file mtimes recorded in the K3 cover desk snapshot manifest.
  - The absence claim at :25 is softened to "no other binding was found by the worker".
- m7. The K2 prerequisite (Sidecar :43; ERRATA :68, :73) is met with the verdict's qualifiers: computer-assisted,
  conditional on the trust base and the 35-class provenance caveat, and not a new gate. The sentence "Parent replay
  is in progress" is withdrawn, since no parent record is cited for it.
- m8. The generator pin record cites the parent label "01:12 PDT". That is a label only: it is later than the 01:00:31
  pin and the 01:00:59 run, and the host-clock observation is the worker's own statement. The worker did not retain
  the parent message identifier; the parent's outbound record is authoritative.
- m9. Generator r1's B decode lacked header, base-prefix and sign checks and did not assert the oracle receipt. This
  is fixed in generator r2 and carried into the guarded generator r3 (C3). Its docstring phrase "(as in the B-map
  oracle)" is withdrawn.
- m10. In the r1 receipt, `block_sha_equal` and `sets_equal` are consequences of `B_map_equals_A_map`, and the
  swapped-map test is SHA sensitivity, not non-vacuity. They are relabelled in r2 and r3.
- m11. In r1, `distinct_ok` includes the total count, and per-mutation reasons were not stored. r2, and r3 after it,
  store the full reports and separate distinctness from count.
- m12. r1 and the oracle did not record the interpreter or the module paths. Generator r3, the driver r2 and the
  controls r2 record them and run as `/usr/bin/python3 -I -B` with an explicit lane path.
- m13. H3 is restated (§1), and the auxiliary reconstruction is added (§8).
- m14. Transposition acts on all three squares simultaneously, and the contradictions are stated against exact CNF
  hashes (§3).
- m15. The interim 23:47 text was named `AMENDMENT-4.r2.md`. That name is retired and never reused; the archive path
  and SHA are in §0. The r1 receipt binds draft r1 ef87fa49…; generator r3 re-binds the controls to this text.
- m16. The driver, caps, screen policy and RSS limit for C311+cuts are fixed in the delta (§7, §9).
- m17 was resolved by the desk (identical 16-byte solver logs); no action is needed.

## 11. Changes in draft 2 and new parent records
Parent source review of draft 1 (message 15aae4593f5e6f0b) put a HOLD on four issues. They are fixed in new
versions, and draft 1's code is preserved unchanged and never run:
1. Status parsing from bytes with no whitespace stripping, plus exact solver status: driver r2 and C8.
2. Guarded preparation and generator execution covering every descendant, with SIGTERM and a bounded wait, UNKNOWN
   on trips, no subprocess timeout and no SIGKILL: stage guard, driver r2, generator r3, C9.
3. SIGTERM handling for the whole run, with survivors quarantined and later admissions refused: stage guard,
   driver r2, C9.
4. Creation-only route directories with exclusive outputs: driver r2 and C9.

New parent records, under `institute/runs/six-lane-2026-10-16/review/`:
- `moqls7-amendment4-header-erratum-v1.md`, effec3dbc145dc366678bec31c2aa2b2cf8a13b3992bc4838e8f91f1058eb148. The
  disposition's larger header counts are the strengthened counts. This text has always asserted input headers A lex
  107513/659168 and B 461370/1629802, and strengthened headers 107513/897308 and 461370/1867942.
- `moqls7-k3-A-cubes-parent-verdict-v1.md`, 0ba3fe4f0e14d17abbb21766523f1a18627cb1ca6178c5bf546d4eec2cb81f97. It
  accepts the A-side exact-CNF facts for A_C321 and A_C411 (parent replays PASS). This covers the A side only, so G1
  and G2 are not met under the A+B standard until the B side is accepted.
