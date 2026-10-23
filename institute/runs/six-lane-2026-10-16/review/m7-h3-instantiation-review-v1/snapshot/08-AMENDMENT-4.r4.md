# Amendment 4 r4: transported own-row/column-frame cuts for the K3 C311 cube

**Status: DRAFT FOR PARENT SOURCE REVIEW, NOT FROZEN, INACTIVE.** This draft becomes usable only as the frozen file
`review/AMENDMENT-4.r4.md`: a byte-identical `cp -n` copy made after the parent source review PASSes, frozen
together with the delta `review/K3-CUTS-CERT-DELTA.r5.json`.

Superseded texts:
- The frozen `review/AMENDMENT-4.r3.md` (c390a8bfcc2e8663278264729271a744e91d0d9231044a9cd74ea2159997034c) and its
  frozen delta r4 (9d93687e2f07e1563c81608fa929c3560efcab35efac26c42219ae2bed72006c) are historical failed
  preparation. They are not activated mathematical cuts.
- Their supervisor controls failed on this host (§11), and nothing scientific ran under them.
- Drafts r3-d1, d2 and d3 are also superseded and are preserved unchanged.

Written 2026-10-18 03:27 PDT (host clock). The mathematics, the A+B standard and the scientific acceptance rules are
unchanged from r3. Only the execution supervisor and the file versions that depend on it change. This text makes no
claim about K3 or M(7). Every control outcome named here is an expected result: none of the new code has run.

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
- Supervisor r3 `code/supervise_r3.py`: 0ee8f39496fa3d6051639e99f10d907b8adadcb5d3446f2bb6242c924a83ec4d.
- Supervisor controls r3 (P1–P12, S1–S15) `code/supervise_controls_r3.py`:
  60a94eb2e0324975db81b7117b3717eec24d348d2e05a98fbd57433a91993cd3.
- Appender and certification driver r5 `code/k3_cuts_certify_r5.py`:
  a12f9632f23cc76f66de7d619da6f2217480544625d047f0e21c27a3325ee0a5.
- Generator r6 (controls C1–C4) `code/k3_cuts_r6.py`: d0fc540e71c6de97027b59e74f35ed4d30a72c70cc57a830f67b5f0b58b2b1aa.
- Appender, parser and transport controls r5 (C5–C8) `code/k3_cuts_certify_controls_r5.py`:
  e244ddda0d3e8beaaad9ac293c1fc5f3dc3ffd6c4c6cfb0e77fc37f9c6f2dff0.
- Superseded files, all preserved:
  - generator r2 `code/k3_cuts_r2.py` 5c1c1d67…bdd9, r3 `code/k3_cuts_r3.py` e636924c…3d0d, r4
    `code/k3_cuts_r4.py` 5c19b64a…24d9 and r5 `code/k3_cuts_r5.py` 2b9b1189…8e87 (never run);
  - driver r1 `code/k3_cuts_certify_r1.py` 0e978302…0b5a, r2 5b7ab798…f0ff, r3 7453009c…5fbe and r4 3ad6a4df…c038
    (never run, except driver r4's refusal to run unsupervised, observed in S11 of the failed r2 controls);
  - controls r1 `code/k3_cuts_certify_controls_r1.py` 1dc761d1…0025, r2 c9e287d9…2ef1, r3 90634fb3…1c3f and r4
    646798ef…07e5 (never run);
  - stage guard `code/stage_guard_r1.py` 2d945ed0…0fba (never run);
  - supervisor r1 `code/supervise_r1.py` 0755d68e…8b53 and supervisor controls r1 0f61b466…01c5 (never run);
  - supervisor r2 `code/supervise_r2.py` 0b023e2c…8c37 and supervisor controls r2 f8f71254…11ec. These ran once and
    FAILED: receipt `evidence/k3cubes/supervise_controls_r2.json`
    8313d092308a2de1df38e9cf09d2d8e0bade9cfe6b625e49aa40e12a30e918a1. Its test records and test quarantines are
    preserved in `evidence/k3cubes/supervise_controls_r2/`.

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

(ii) **Appender and certification driver** `code/k3_cuts_certify_r5.py`. For the named route it does the following,
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

Execution safety (parent source reviews of drafts 1–3; §11):
- The driver, generator r6 and controls r5 refuse to run unless they are the session and process-group leader
  started by the supervisor file that the frozen delta pins (`code/supervise_r3.py`). The supervisor is one
  single-threaded process. Its scope
  is the command's process group and nothing else. Members keep the group across re-parenting. A process that
  leaves the group is detected while it is still a child of a live member; it is never signalled and capacity is
  quarantined. The production commands (lane python drivers, gram_encB.py, cadical, kissat, drat-trim) do not leave
  the group. The /usr/bin/python3 shim execs in place, so the driver is the leader.
- Every 0.25 s it probes itself, the leader and every member through proc_pidinfo, against a fresh group listing
  from the same sample. Each probe is one of four states:
  - alive: full reads and RSS > 0;
  - zombie: BSD status SZOMB or, as on this Darwin host, ESRCH while the pid is still listed in our process group;
  - gone: ESRCH while not listed;
  - unknown: any other short, failed or zero-RSS read.
  A failed read never counts as death. The run trips on aggregate RSS above 3.5 GiB, free space below the 12e9 floor,
  the wall cap, an external SIGTERM, or a member alive after the leader exited. It also trips on any uncertainty: an
  unknown probe, a failed listing, a leader gone (ESRCH and not listed) while unreaped, or an escape.
- Stop: killpg(group, SIGTERM), sent only while the group has live or unknown members, and only while the leader is
  unreaped. The zombie leader keeps the group ID reserved, so no unrelated reused PID can be signalled. A group whose
  only member is a zombie is not signalled, because killpg raises EPERM on Darwin. If killpg fails while live members
  exist, those members stay unresolved and are quarantined as survivors. The supervisor waits at most 30 s.
- Survivors, or any uncertain trip, give an exclusive-create capacity quarantine at
  `evidence/k3cubes/C311cuts.QUARANTINE.json` listing process identities (pid, ppid, pgid, start time). Code never
  removes it, and the supervisor, driver, generator and controls refuse to start while it exists.
- When the leader becomes a zombie, the supervisor runs a final synchronous check of members, RSS, floor and wall
  before reaping it. No SIGKILL is sent and no subprocess timeout is used.
- Solver and checker status lines are parsed from bytes: remove only `\r`, split on `\n`, keep the lines starting
  with `s `, with no stripping. A certificate needs exactly [`s VERIFIED`] from drat-trim and exactly
  [`s UNSATISFIABLE`] from the solver.
- Each route uses one deliberately created directory, `evidence/k3cubes/C311cuts_<route>_r5` (made by mkdir; if it
  already exists, nothing runs). Every output in it is exclusive-create. The driver writes a receipt on every outcome
  it survives; if the supervisor stops the group, the supervisor record is the receipt of that stop.
- Fail-closed exception path (unchanged from supervisor r2). Any exception after the command starts records an
  uncertain UNKNOWN.
  The supervisor then SIGTERMs the still reserved group (the leader is unreaped), waits at most 30 s and quarantines
  capacity. If measurement fails during the stop, it falls back to one killpg, a bounded unmeasured wait and
  survivors reported as unknown, which quarantines. It always attempts the record, falling back to
  RECORD.failure.json, and restores its signal handlers in a finally block.
- Acceptance of a route needs both the driver receipt (VERIFIED_UNSAT_CASE) and the supervisor record of that run
  (completed_cleanly, no trip, no quarantine).

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
    re-bound to this frozen text by generator r6 (§6).

  This is a ruling, not a claim that a genuine K3 control passed.
- The genuine weight-5 Ψ(f) placed beside two classical squares gives exactly (2940, 0) violations. This is a
  non-vacuity check that the cuts bite; that configuration is not a K3 triple.

## 6. Controls before any use
Generator r6 (`code/k3_cuts_r6.py`) has the content of the never-run r2 and imports driver r5. It runs only under the
supervisor, which guards it and every encoder B child in its group. It refuses to run unless this frozen text names
its SHA, and it binds this text's SHA. The r1 controls bound draft r1; r6 re-binds them to this text (m15). Its
controls:
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

The appender controls (`code/k3_cuts_certify_controls_r5.py`, run under the supervisor):
- C5: the bindings among this text, the delta, the driver, the generator r6 receipt, the supervisor, the supervisor
  controls, the oracle receipt and the B_C311 metadata.
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
- The control directory itself tests the creation-only rule: a second mkdir must raise.

The supervisor controls (`code/supervise_controls_r3.py`) run as a plain top-level process, because their test
commands create their own groups. Every test command is supervised by the supervisor under test. Expected outcomes:
- probe classification on real processes and on deterministic fakes around proc_pidinfo:
  - self is alive with RSS > 0;
  - an unreaped exited child in its own group is a zombie by member_state, which uses a fresh group listing;
  - the raw probe of that child is recorded for information (ESRCH on this host);
  - after reaping, the child is gone;
  - ESRCH while not listed stays gone, and an unknown probe stays unknown even when the pid is listed;
  - a short task-info read, a zero-RSS task-info read, a short BSD read, EPERM and a pid mismatch are all unknown;
  - ESRCH is gone;
  - a task-info failure followed by a zombie re-read with the same start time is zombie;
- a clean short command completes cleanly;
- the wall cap stops the leader (rc −15);
- a short command still meets the completion check (a floor above the free space trips);
- injected RSS above the cap trips and stops;
- an injected unknown probe trips as uncertain and leaves a capacity quarantine even without survivors;
- re-parenting: a grandchild that ignores SIGTERM is listed with ppid 1, quarantined, and exits by itself;
- a re-parented grandchild that obeys SIGTERM is stopped through the reserved group ID, with no quarantine;
- a child that leaves the group is detected as uncertain, is not signalled, is quarantined and exits by itself;
- external SIGTERM to a separate supervisor process stops its leader and exits 3;
- an existing quarantine record refuses admission;
- the driver refuses to run unsupervised and creates nothing;
- a real statvfs exception inside the loop (a nonexistent lane path) still SIGTERMs the reserved group (leader
  rc −15), records an uncertain UNKNOWN and leaves a capacity quarantine;
- a probe that raises (not one that returns unknown) inside the loop and again during the stop, on a leader that
  ignores SIGTERM, takes the fallback: one killpg, a bounded unmeasured wait, survivors unknown, quarantine and a
  written record; the leader then exits by itself;
- a trip on a group whose only member is the zombie leader sends no killpg, records no killpg error, and has no
  survivors and no quarantine;
- a killpg failure (EPERM injected) while a live member exists records the error and keeps that member as an
  unresolved survivor in quarantine; the member then exits by itself.

Order: freeze this text and the delta, then run the supervisor controls, then generator r6 and the appender
controls (both under the supervisor), then the first launch.

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
  - cooperative wall guard 7320 s inside the driver; supervisor wall caps of 8400 s for a driver run (preparation
    plus pipeline), 1800 s for generator r6 and 1800 s for the appender controls;
  - no separate exploratory screen: the certified run is the only search;
  - one attempt per route under this delta, and at most one C311+cuts pipeline at a time;
  - lane at most 4 busy processes and 8 GiB. The authorised sequential B r6 retries (B/C321, then B/C411) keep
    priority. The parent A replays are complete; their freed slots are used only after a fresh lane-load gate.
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
- Throughout every supervised run: the supervisor's strict probes over the whole process group, with the continuous
  12e9 floor, aggregate RSS at most 3.5 GiB and the wall cap; checkpoints every 15 minutes during the pipeline;
  SIGTERM only, with a 30 s grace; survivors and uncertainty quarantined; no CNF or proof file.
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
  is fixed in generator r2, whose content generator r6 carries (C3). Its docstring phrase "(as in the B-map
  oracle)" is withdrawn.
- m10. In the r1 receipt, `block_sha_equal` and `sets_equal` are consequences of `B_map_equals_A_map`, and the
  swapped-map test is SHA sensitivity, not non-vacuity. They are relabelled in r2 and r6.
- m11. In r1, `distinct_ok` includes the total count, and per-mutation reasons were not stored. r2, and r6 after it,
  store the full reports and separate distinctness from count.
- m12. r1 and the oracle did not record the interpreter or the module paths. Generator r6, driver r5 and controls r5
  record them and run as `/usr/bin/python3 -I -B` with an explicit lane path.
- m13. H3 is restated (§1), and the auxiliary reconstruction is added (§8).
- m14. Transposition acts on all three squares simultaneously, and the contradictions are stated against exact CNF
  hashes (§3).
- m15. The interim 23:47 text was named `AMENDMENT-4.r2.md`. That name is retired and never reused; the archive path
  and SHA are in §0. The r1 receipt binds draft r1 ef87fa49…; generator r6 re-binds the controls to this text.
- m16. The driver, caps, screen policy and RSS limit for C311+cuts are fixed in the delta (§7, §9).
- m17 was resolved by the desk (identical 16-byte solver logs); no action is needed.

## 11. Changes in r3 drafts 2–4 and in r4, and new parent records
Parent source review of draft 1 (message 15aae4593f5e6f0b) put a HOLD on four issues. Draft 2 addressed them with an
in-process stage guard. The review of draft 2 kept the HOLD:
- a failed or short RSS read could count as zero or as dead;
- grandchildren could be lost when re-parented;
- raw-PID signalling risked hitting a reused PID;
- short stages could finish before any check;
- draft 2 listed expected control outcomes in a way that could be read as results.
Draft 3 replaced the stage guard with a process-group supervisor (`code/supervise_r1.py`) and made the fixes below.
Draft 4 adds the fail-closed exception path that the review of draft 3 asked for (message 15aaec72049e6f66), in
`code/supervise_r2.py`, with its controls, and carries the version cascade: driver r4 reads the supervisor pin from
the frozen delta, generator r5 and controls r4 import driver r4. All code of drafts 1–3 is preserved and was never
run.
1. Strict byte status parsing with exact solver status: driver r4 and C8.
2. Supervised preparation, generator and controls covering the whole process group. Strict probes: unknown trips and
   quarantines; a dead state needs positive zombie or ESRCH evidence; the leader is never judged by RSS. Re-parented
   members stay covered, escapes are detected and quarantined, signals go only to the group while its leader is
   unreaped, there is a final check at completion, and there is no SIGKILL and no subprocess timeout.
3. External SIGTERM to the supervisor stops the group. Survivors or uncertainty quarantine capacity, and later
   admissions are refused.
4. Creation-only route directories with exclusive outputs: driver r4 and C8.
5. Fail-closed supervisor exception path (draft 4): uncertain UNKNOWN, SIGTERM to the reserved group, bounded wait,
   capacity quarantine, a record attempt and handler restoration in a finally block; deterministic statvfs and
   raising-probe controls.

r4 (this text). The frozen r3 package (amendment c390a8bf…034c, delta r4 9d93687e…006c) was run as far as its first
control stage under the parent GO for control stages only. Supervisor controls r2 FAILED, receipt
`evidence/k3cubes/supervise_controls_r2.json` 8313d092308a2de1df38e9cf09d2d8e0bade9cfe6b625e49aa40e12a30e918a1:
- P2 failed: an unreaped exit probed as "gone";
- S1, S6 and S7 failed: "leader gone while unreaped", and in S1 the stop fell back after killpg raised EPERM;
- all other tests passed. No test process survived; all test quarantines are preserved.
The parent accepted that observation as ground truth, and it was not rerun. Generator r5, controls r4 and any
scientific run were not started.

**Host-specific assumption that failed.** Supervisor r1/r2 assumed proc_pidinfo returns BSD info with status SZOMB
for a zombie. A one-second diagnostic on this Darwin host (03:20 PDT) showed:
- proc_pidinfo PROC_PIDTBSDINFO and PROC_PIDT_SHORTBSDINFO return 0 with ESRCH for an unreaped exited child;
- proc_listpids(PROC_PGRP_ONLY) still lists that zombie;
- killpg on a zombie-only group raises EPERM (also for signal 0);
- os.waitid does not exist in this Python 3.9.

**Fix, in supervise_r3 (narrow).** A pid is a zombie only on positive evidence: ESRCH while freshly listed in our
group. Every other failed, short or zero-RSS read stays unknown. A listing failure stays uncertain. killpg is sent only
while live or unknown members exist. A killpg failure while live members exist leaves them as quarantined survivors.
The leader stays unreaped until the final stop decision. There is no SIGKILL, and the supervisor's scope is unchanged.

The new controls are P2 (zombie by group listing), P11 and P12 (the rule's negative cases), S14 (a zombie-only group
is not signalled) and S15 (a killpg failure is quarantined). The dependent versions are driver r5, generator r6 and
controls r5. They change only paths and imports.
All control outcomes in §6 are expected results until the receipts exist.

New parent records, under `institute/runs/six-lane-2026-10-16/review/`:
- `moqls7-amendment4-header-erratum-v1.md`, effec3dbc145dc366678bec31c2aa2b2cf8a13b3992bc4838e8f91f1058eb148. The
  disposition's larger header counts are the strengthened counts. This text has always asserted input headers A lex
  107513/659168 and B 461370/1629802, and strengthened headers 107513/897308 and 461370/1867942.
- `moqls7-k3-A-cubes-parent-verdict-v1.md`, 0ba3fe4f0e14d17abbb21766523f1a18627cb1ca6178c5bf546d4eec2cb81f97. It
  accepts the A-side exact-CNF facts for A_C321 and A_C411 (parent replays PASS). This covers the A side only, so G1
  and G2 are not met under the A+B standard until the B side is accepted.
