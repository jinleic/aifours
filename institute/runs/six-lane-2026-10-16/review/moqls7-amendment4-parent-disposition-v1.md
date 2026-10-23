# MOQLS(7) K3: parent disposition of AMENDMENT-4.r1 (transported C311 cuts)

Parent, 2026-10-18 PDT (written after the desk result `R/moqls7-amendment4-review-v1/RESULT.md`, SHA `3792077335885fe78c8c632c347502314148592fec90177121b6a16384c55dac`). This is a process and scope decision. It is not a K3 or M(7) verdict, and nothing below accepts a certificate.

## Inputs
- Draft `lane/review/drafts/AMENDMENT-4.r1.md` `ef87fa492abcc9a86e02be9d8f14f7810908a83458b32e38788f99f3acc5abb1`; generator `lane/code/k3_cuts_r1.py` `0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a`; receipt `lane/evidence/k3cubes/cuts_r1_receipt.json` `9cfc0e81bed2cbcbdcd2c205d697dc107b184609f722f0f799225e39092babbf`; block SHA `05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd`; B-map oracle receipt `6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c`. Here `lane/` = `physics/evidence/six-lane-20261016/moqls7-maximum/`.
- Codex `gpt-6.1-sol` note `970430f7b51cbd6b987fc2e101844baa9a39fb2bf653f8a03c120674f0c02601`: ACCEPT-WITH-FIXES, 0 FATAL, 2 MAJOR. Claude `claude-opus-5-5` note `dc66f3c118ad61f2bb966a31f127570bc83f68d44ce778a9be77d982e3de364a`: ACCEPT-WITH-FIXES, 0 FATAL, 3 MAJOR.

## Mathematics
Both reviews find the transport lemma sound for all 14 own row/column frames, all 42 off-line points and every role assignment, under H1–H5 and G1–G2. They also find the (4,1,1)/(3,2,1) threshold counts, the 238,140-clause cut family and its lex compatibility sound. The parent adopts that as **CONDITIONALLY SOUND**. Every cut clause is a derived consequence that is valid only under K1, K2 (both parent-accepted, with their stated caveats) and G1–G2, the exclusions of the exact C321 and C411 cube inputs. The final K3 composition therefore stays conditional on parent-accepted C321 and C411 exclusions under the standard below.

## Decisions
1. **Standard (MAJOR-B): A+B, no deviation.** Lane README Phase C (`README.md:80-81`) requires two encodings, and K2 was accepted on both encoders. Every K3 cube needs a DRAT-checked UNSAT of its exact input on encoder A and on encoder B: C321, C411, and C311 strengthened by the cuts. Each also needs a parent replay. A-only acceptance is not available. The A route may use lex C311 (`059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f`), because a common lex-minimal orbit member satisfies base, cube, lex and cuts. The B route uses original B_C311 (`b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077`) plus cuts, unless a B lex input is generated and bound under AMENDMENT-3 before any B solve. The cut clauses are valid for every K3 configuration, so they may be appended to an original cube as well as to a lex cube.
2. **README:91 ruling (MAJOR-C).** No genuine K3 positive can be supplied: one would refute the target. README:91 is applied at component level, with this recorded limitation:
   - the base A and B encoders keep their reviewed matched component controls (26/26), and the K2 verdict's README:91 timing deviation still applies;
   - each cut clause must be satisfied by all five classical AG(2,7) triples, which are genuine mutually orthogonal triples. Receipt control (b) shows this for the cut clauses alone;
   - the C1 local-coverage control (2,100 assignments, exactly 450 rejected) must be re-bound to the frozen r3 text;
   - the frozen r3 must state that the cuts are derived conditional clauses, not definition-level necessary conditions, and cite this ruling.

   This is a ruling, not a claim that a genuine K3 control passed.
3. **Activation.** C311+cuts solving may start once items 4–6 are done. It does not have to wait for parent acceptance of C321/C411; that dependency enters only at final composition. No C311 result is accepted, and no composition is reviewed, until G1–G2 are parent-accepted under decision 1.
4. **New frozen draft, never named r2.** Write `AMENDMENT-4.r3.md`. Bind the archived interim text (`e72233ca…2870`), r1 `ef87fa49…bb1`, generator, receipt, block and oracle SHAs, the K1/K2 verdicts and the chosen instances. Carry every MINOR m1–m16 as an erratum or new-version fix, and record the freeze-order exceptions (m4) as post-hoc provenance, not preregistration. H3 must be stated as encoder soundness for the exact K3 base instantiation (3 squares, no L, heavy, `--sym`), with auxiliary reconstruction for each encoder (m13).
5. **Code (MAJOR-A).** Write a new pinned appender/certification driver that:
   - regenerates the named input in memory by the r3 method and asserts its SHA;
   - re-emits the block and asserts `05f31da4…e6dd`;
   - writes the incremented header;
   - asserts these headers: A original 96978/865696, A lex 107513/897308, B original 461370/1867942;
   - asserts prefix equality with the named input;
   - binds and records the strengthened-input SHA, measured as fed to the solver and to the checker;
   - for B, asserts that the oracle receipt says PASS with its pins, or replicates the oracle checks, and binds B_C311 (meta `bfa298ee…a056`) to the oracle in a new version.

   It streams solver → FIFO → parent-trusted drat-trim, with no CNF or proof file. It uses the existing 12.2e9 + growth gate twice, the continuous 12e9 floor, RSS ≤3.5 GiB per pipeline, SIGTERM only, and pre-declared caps; time budgets are fixed in the delta before launch.
6. **Parent source review** of the r3 draft, the appender/driver and the controls must PASS before the first C311+cuts launch. Send SHAs to the parent; the parent may delegate a static desk.
7. **Resources.** The phys-2 lane stays within ≤4 busy, ≤8 GiB and ≤10 GiB new data. In-flight B/C411 r5, the authorized B/C321 r6 retry and the parent A replays keep priority. C311+cuts runs when a slot is free.
8. **Final composition.** The parent will review K1 ∧ K2 ⇒ G4 ⇒ `--sym` ⇒ three cubes ⇒ {C321, C411 accepted; transport ⇒ cuts; C311+cuts certified on A and B}, including the encoder instantiation (H3) and the lex-representative step. That composition is the earliest point at which K3 and the exact value of M(7) can be decided.

## Status after this disposition
AMENDMENT-4 is mathematically conditionally sound and stays NOT FROZEN and INACTIVE until items 4–6 are met. No new claim.
