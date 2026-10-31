# Review v1 — f91-moqls-q1-species0-rup-exclusion

- Manifest: `manifest-v1.json` (SHA256 7a72d6a5cf5a1bd4bdc0641a65bf59b2aa7871a666a2c14fb1ccf81365e55d34), binding version 1, no predecessor.
- Authority: `contract-addendum-2-frontier-first-owner-direction-v1.json` (frontier-first; fresh local exact computation and public-source reading permitted).
- Reviewer: same-harness disjoint reviewer (slot physics-4 review). This is NOT external-family, human, formal/kernel or novelty verification.
- `/bin/date` observed immediately before this file was written: **Wed Oct 28 19:08:xx PDT 2026** (the exact stamp is the shell line printed directly above the write; last receipt clock before it was `Wed Oct 28 19:08:15 PDT 2026`).
- Writes: only this directory (`review-v1.md`, four `reviewer-*.py`/receipt files, `controls/`). No Git, deletion, author contact, external model or paid API.

## 0. Verdict

| Candidate | FATAL | MAJOR | MINOR | Status |
|---|---|---|---|---|
| `frontier-20261028-q1-species0-rup-exclusion-v1.md` (SHA256 58629d64…, 7946 B, 32 LF) | 0 | 0 | 2 | **No scientific defect found at the stated scope.** The physical→support reduction is sound as written, every one of the 7697 pinned clauses is a necessary condition under an explicit variable interpretation I derived myself, and the pinned 262-step proof is a valid RUP refutation of the pinned CNF under my own checker. The certified statement is in fact stronger than the candidate states (MINOR-1). |

## 1. Inputs actually read and hash-verified

Manifest input (read completely, raw, lines 1–32): candidate `.../parallel-18/moqls8/frontier-20261028-q1-species0-rup-exclusion-v1.md` — SHA256 `58629d647618bcbac2eb636d4c831f00d8cc99f9ef274ee3cfcb680124154c2e`, 7946 bytes, 32 LF: **match**.

Named imports in the owner root (all read raw and completely, all SHA256 **match** the candidate's citations):

| File | SHA256 (candidate = observed) |
|---|---|
| `frontier-20261028-source-wanless-max3-order8-v1.txt` | 95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67 |
| `frontier-20261028-wanless-source-page-audit-v1.json` | 07cc372190f3d2d3100f8d389c4efaf739ca1eed29afad439f8e346e9363ec8b |
| `frontier-20261028-q1-support-cnf-v1.py` (producer) | 4c95605057d0dd540041b905f889b68e35fb6a8682011faed021a403c0cd4d53 |
| `frontier-20261028-anchor-sparse-net-obstructions-v1.py` (net module imported by producer, pinned inside it) | 6e46c39749b322809758b16d64171c89d429a4d6bfcdc848bed86508f9f1c8e3 |
| `frontier-20261028-q1-support-species0-v1.cnf` (102,692 B, `p cnf 2176 7697`) | 0ddbe3818bba22fb3e040d669f0b81dcfe8f39f3b005db842a6c969db8f00f63 |
| `frontier-20261028-q1-support-species0-cnf-receipt-v1.json` (producer receipt) | ebe0df5ebb8bcdb5322e681f7c0bd523551dafaaff030cbd44a2ed16d9692154 |
| `frontier-20261028-q1-support-cnf-check-v1.py` | e824a35b1f304ce8472770d1d281a36d88ce983a95b480ce7de2697d0f19021b |
| `frontier-20261028-q1-support-species0-cnf-check-receipt-v1.json` | f1cb824dac1c117cd5041f5a268c6d3595c1453b4663701bd0501a09c204c26e |
| `/opt/homebrew/bin/kissat` → Cellar 4.0.4 | 05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848 |
| `frontier-20261028-q1-support-species0-proof-v1.drup` (3,401 B, 262 lines) | 2d405f676add4fe7967e98722834c536d9545ed1a0038f4546b1721e55b33599 |
| `frontier-20261028-rup-proof-check-v1.py` / receipt | 82e0b595da1798a67e83fc2b80885856dab3c004b07abddadb04fb59f31c08cc / 2aee669484ac244c590319e9c4b096ac3b07f809104bde8a408c0b238df8329c |
| `frontier-20261028-rup-scan-check-v1.py` / receipt | 77fdc7f3918c6945adce1e7124c6e21552da1d57fbcedad3c52549e73c39321c / a19976859fa40579fe89454c2834422c0f9ac949cfe14e9dc7db431a62f6503e |
| `frontier-20261028-q1-support-physical-control-v1.py` / receipt | ca8f42999f128a8f42a98c480c81eca747abeb60497af9513202f881d0234a8c / 48d467c1493904d5b4c3108e12ac545875c72e438277a5597d697efb3bf80ef3 |

Also read for the kissat option list (not named in the candidate): `frontier-20261028-q1-support-proof-batch-v1.py`, observed SHA256 22a99215f45b9d56ce975d58ff98786e3f19d5fc26be4e4bbe9e05d68ccb7215. Definitions of QLS / pair-product orthogonality / per-member global-ONB-ray classicality were taken from the slot's `intake-v1.md` §2 (registered target quote). No held, withdrawn or quarantined body was used as a premise.

## 2. Exactly what is excluded (reviewer's statement)

Let N be the 5-net of order 8 whose five parallel classes are the rows, the columns and the three symbol classes of the first printed triple (squares 1–3, zero-based species index 0) in the pinned bytes 95943777…. (The same 24 lines appear, in order, in the local unpaginated reader snapshot abcf7401… and — read today at reader level — at the head of the public `users.monash.edu.au/~iwanless/data/MOLS/maxMOLS8.3.txt`; no HTTP byte identity is claimed.)

**Certified (pinned CNF + pinned proof, verified by my own checker):** there is no assignment of unit vectors of C^8 to the 64 points of N that is an orthonormal basis on every one of the 40 lines of N **and** is not contained in a single ONB. By the reduction in §3 this is equivalent to: no actual four-MOQLS(8) family (Q, M1, M2, M3) exists with M1, M2, M3 classical, Q nonclassical, and net(M1, M2, M3) isomorphic (any class permutation, any isotopy) to N. Q's amplitudes/phases/supports are unrestricted; only the unit-ray, row/column ONB and six pair-product ONB conditions of the registered target are used, and of those only (i) Q's own row/column ONBs, (ii) orthogonality within each same-mate-symbol line, (iii) completeness of the 8-vector ONB on each line.

**Also certified, stronger (D1/D2 below, reviewer-verified):** the 7696 clauses *without* the nonclassicality clause are already UNSAT; the pinned 262-step proof itself refutes them. Hence **no fourth QLS at all — classical or not — is pair-product orthogonal to the three classical mates of N**. The classical half independently reconfirms the catalogue's "maximal" label for this triple from the pinned bytes alone.

**Not established (explicit non-claims):** anything about the other 37 maximal species or the nonmaximal species 38 (only one net); completeness of the Wanless catalogue or the Hcat classification of all 3-MOLS(8) nets; any unrestricted q1 theorem (a four-family whose classical triple is *not* in this species is untouched); q2/q3/q4; any numerical M(8), A10/A11 or five-family statement; historical novelty; formal/kernel, external-family, human or drat-trim/FIFO parent-replay acceptance. "Species/paratopic" is read as net isomorphism with free class permutation; if the catalogue's equivalence is narrower, the statement here is at least as strong.

## 3. Re-derivation of the physical → necessary-support reduction (candidate L9–L21)

Definitions used (intake §2): a member is an 8×8 array of unit rays with every row and column an ONB; two members are orthogonal iff their 64 same-cell tensor products form an ONB of C^8⊗C^8; a member is classical iff all its rays lie in one ONB (phases and a per-member output unitary free).

1. *Classical mates ⇒ 3 MOLS ⇒ 5-net (L9).* A classical QLS with ONB {f_a} is [f_{L(x)}] for a map L; its row/column ONBs force L Latin. For two classical mates, ⟨f_{L(x)}⊗g_{L'(x)}, f_{L(y)}⊗g_{L'(y)}⟩ = δ_{L(x)L(y)} δ_{L'(x)L'(y)}, so 64 orthonormal products ⇔ the pairs (L(x),L'(x)) are distinct ⇔ L ⊥ L'. Rows, columns and the three symbol maps are pairwise orthogonal classes: a 5-net / OA(64,5,8,2). I re-verified strength 2 for all 10 class pairs of the pinned triple in my own parser (`reviewer-cnf-semantic-audit-v1.py` §2).
2. *Q is an ONB on every line (L9).* Rows/columns: QLS property. Symbol line of mate k with value a: for x≠y on it, ⟨f_a⊗Q(x), f_a⊗Q(y)⟩ = ⟨Q(x),Q(y)⟩ must vanish (orthogonality part of the pair-product ONB only), so the 8 unit rays are pairwise orthogonal, hence a complete ONB of C^8.
3. *Reorientation under paratopy (L9).* A net isomorphism φ: N(M1,M2,M3) → N maps lines to lines; Q∘φ⁻¹ is an ONB on every line of N. Index the 64 points by N's classes 0 (row) and 1 (column); Q is then a QLS orthogonal to the classical squares of classes 2–4, with the same ray multiset, so nonclassicality is preserved. For the pinned triple `orient(T,0,1,0)` is the identity (all three first rows are `abcdefgh`), so the CNF's net is literally the printed triple.
4. *Anchor and allowed sets (L11).* Apply the output unitary U with U·Q(0,j) = e_j (an output unitary on Q alone preserves every condition above). For x=(i,j), i>0: Q(x) ⊥ e_j (column ONB) and Q(x) ⊥ e_{L_k(x)} for k=0,1,2 (cell (0,L_k(x)) shares symbol line k, since L_k(0,s)=s). The four labels are distinct: j≠L_k(x) by column-Latinness; L_k(x)≠L_l(x) because the pair (s,s) already occurs at (0,s) and L_k ⊥ L_l. So S_x := supp Q(x) is a nonempty subset of the 4-set A_x = V∖{j, L_0(x), L_1(x), L_2(x)} — verified |A_x|=4 for all 56 cells.
5. *Nonclassical ⇔ some |S_x| ≥ 2 (L11).* If all S_x are singletons every ray is an e_t. Conversely a classical Q has all rays in one ONB B; row 0 already contributes eight orthogonal rays, so B = {e_t} and every S_x is a singleton.
6. *Clause families are necessary (L15–L19).* (a) S_x ≠ ∅ (unit vector). (b) On a line ℓ with Q|ℓ a complete ONB, Σ_{x∈ℓ}|Q(x)_t|² = 1, so some x∈ℓ has t∈S_x; if (0,t)∈ℓ this is trivial and every off-row x∈ℓ has t∉A_x by construction; otherwise exactly four off-row cells allow t (one cell per class excludes t, the four are distinct by the same Latin/orthogonality argument) — the clause must contain **all** of them, which I checked. (c) Collinear x,y with A_x∩A_y={t}: ⟨Q(x),Q(y)⟩ = conj(Q(x)_t)Q(y)_t, so not both nonzero. (d)/(e) With B_{xy,t} := P_{x,t}∧P_{y,t} (definitional, three clauses), |S_x∩S_y|=1 is impossible for orthogonal vectors, so B_{xy,t} → ∨_{u∈A_x∩A_y∖{t}} B_{xy,u}; the disjunction must range over **all** other common labels, checked. (f) Triangle x,y,z pairwise collinear with all three pairwise allowed intersections = {t,u}: the three projections to span{e_t,e_u} are pairwise orthogonal; if all six coordinates are nonzero they are three nonzero pairwise-orthogonal vectors in C², impossible. Valid for arbitrary complex entries. (g)/(h) n_{x,{t,u}} → P_{x,t}∧P_{x,u}; a nonclassical Q sets one such n true, so the 336-literal clause must cover every (cell, pair) — checked.

Conclusion of §3: every actual Q satisfying the registered conditions induces a satisfying assignment of the pinned CNF (with n/B set as above). No equal-weight, real-flat, generic-position or sign premise enters. L21 is correct.

## 4. Encoder audit (reviewer code, not the author's check script)

`reviewer-cnf-semantic-audit-v1.py` (SHA256 acad33ef9d9c63d516fe6fc0a6f6b69a23e9ec736a66b72a6ee25d6b90984fc1; receipt `reviewer-cnf-semantic-audit-receipt-v1.json`, SHA256 8c1397efe33683c3b4b0d8e23425a2559cf31d4d00a9fc4492859aff61788fad) parses the raw pinned text itself, checks Latin/MOLS/OA(64,5,8,2), fixes the support-variable interpretation P_{x,t} (x=8..63 ascending, t ascending in A_x — 224 variables), derives the meaning of each of the 1952 auxiliary variables **from the pinned clauses themselves** (B: exactly two `(-b,P)` plus one `(b,-P,-P)` with equal t on collinear cells, 1616; N: exactly two `(-n,P)` on one cell, 336; each defined exactly once), and then classifies every pinned clause:

| family | count | necessity check applied |
|---|---|---|
| (a) nonempty support | 56 | literal set = {P_{x,t}: t∈A_x} |
| (b) axis on line | 280 | literal set = **all** off-row cells allowing t on a line not containing (0,t) |
| (c) one-overlap | 64 | collinear, A_x∩A_y = {t} exactly |
| (d) B definitions | 3232 + 1616 | b ↔ P_{x,t}∧P_{y,t} |
| (e) overlap ≠ 1 | 1616 | tail = **all** of A_x∩A_y∖{t} |
| (f) triangles | 160 | pairwise collinear, all three allowed intersections = {t,u} |
| (g) N definitions | 672 | n → both axes |
| (h) nonclassicality | 1 | covers all 56×6 = 336 (cell, pair) options |
| unclassified | **0** | |

Totals 7697/7697, no duplicate clauses, no tautologies. Direct three-cell enumeration gives 160 triangles; 868 collinear off-row pairs (64 zero-overlap, 64 one-overlap, 740 multi-overlap, Σ|common| = 1616). Finally a from-scratch CNF built by me (same P numbering, auxiliaries mapped through the derived bijection) is clause-multiset identical to the pinned formula. Note: the author's "independent" check script shares the producer's variable-numbering convention (P, then B in sorted-edge order, then N); its multiset equality is therefore a same-convention comparison, whereas the audit above is interpretation-level. This is informational, not a defect.

## 5. RUP verification receipt (reviewer checker)

`reviewer-rup-check-v1.py` (SHA256 61e294826beeea199c002c050d37a844c67c645ce69535f3686f762f08353687): standard library only; hashes inputs; parses DIMACS and ASCII DRUP; for every non-deletion line asserts the negation of the lemma plus all current units, unit-propagates over occurrence lists until conflict (accept) or fixpoint (reject); deletions are counted and ignored (sound for refutations; the pinned trace has none); the last line must be the empty clause and must itself propagate to conflict. No author checker code is imported.

- **Pinned CNF 0ddbe381… × pinned proof 2d405f67…: PASS** — 2176 variables, 7697 input clauses, 262 proof lines, **262 RUP additions, 0 deletions**, final empty clause RUP. Receipt `reviewer-rup-check-pinned-receipt-v1.json` (SHA256 62044b4a9280a71b2e70a7883e1186247a16f89e1d6093748c233efc2d881bb8). Checked at `Wed Oct 28 19:03:41 PDT 2026`.
- Tamper controls (`reviewer-controls-v1.py`, SHA256 a6ee27b1cd011040555437de7a52d80b7ae2fc94c5b8bfeadbca177a0dbfcadc, run 19:04:12 PDT, plus an in-kernel follow-up): T1 truncated proof → REJECT (no final empty clause); T2 bogus unit `1 0` prepended → REJECT (step 1 not RUP); T3 satisfiable 2-variable formula with proof `0` → REJECT; T4 proof against the first 3000 clauses only → REJECT (step 1 not RUP); T6 unit lemma 59 `121 0` flipped to `-121 0` → REJECT (also rejected by the author's scan checker, run only as a cross-check); T7 lemma 59 deleted → REJECT at step 106. Two mutations were *accepted* and are not checker defects: T5 (first literal of the 11-literal lemma 16 flipped) is itself a RUP clause — the author's independent scan checker accepts the identical mutated bytes — and T8 (deleting the penultimate unit `107 0`) leaves the empty clause still RUP, i.e. that lemma is redundant.
- **Fresh solver replay.** `kissat --quiet --plain --no-binary --no-preprocess --no-eliminate --no-substitute --no-factor --no-probe --no-sweep --no-vivify --no-transitive --time=3 --conflicts=20000 <pinned cnf> controls/species0-plain-kissat.drup` (option list taken from the batch runner) → `s UNSATISFIABLE`, exit 20, and the produced trace is **byte-identical to the pinned proof** (SHA256 2d405f67…, 3,401 B). A default `kissat -q --no-binary` run also returns exit 20 but emits a 16,244-line trace with 9,000 deletions and extension variables (2177…), i.e. RAT/BVA steps that neither my RUP checker nor the author's can accept (my checker correctly rejects it as a non-RUP/out-of-range trace). See MINOR-2.
- **D1/D2 (nonclassicality clause inert).** Removing the single 337-token clause gives `controls/species0-without-nonclassical-clause.cnf` (SHA256 ff9aacd162821b883be03d3a7deb5ac9b71185718d8dc5e34324e7b4badd052b, 7696 clauses). The *pinned* 262-step proof passes my checker against it unchanged (receipt `reviewer-rup-check-noN-pinnedproof-receipt-v1.json`, SHA256 eb641c8441b2df6b6f3b680bcea4a7de21ff8d09b4a15d22fb2cbc1bc31af62a). A fresh plain kissat run on it is UNSAT with a 1005-step pure-RUP trace (`controls/species0-without-nonclassical-plain.drup`, SHA256 60f74f91a7d11df567337fd2bbe8bfebcec100130174fbcc8081b52f2663a092) that my checker verifies (receipt `reviewer-rup-check-noN-freshproof-receipt-v1.json`, SHA256 b9ec6dd9d63b98fdfacbfec608470cbf11fb401d8c588c5705d637454013068d).

## 6. Findings

**MINOR-1 (scope/presentation, L3, L19, L21): the certificate proves more than the candidate states, and the nonclassicality clause is not load-bearing.** L19 presents the 336-literal clause as the device that "requires at least one cell to have two supported axes", and L3/L21 state the exclusion only for a *nonclassical* fourth member. D1 shows the pinned proof never needs that clause: the necessary-support conditions (a)–(f) alone are contradictory for this net. Correct sharpened statement: *no QLS(8) whatsoever (arbitrary complex, classical or not) is pair-product orthogonal to the three classical mates of the species-0 net*; the classical sub-case is Wanless's maximality, here reconfirmed from the pinned bytes. Nothing in the candidate is false; the written claim is strictly weaker than what the frozen artifacts certify. Suggested fix: an additive erratum/addendum stating the stronger exclusion and that the N-clause is redundant for species 0 (it is presumably needed for non-maximal nets such as species 38, where classical completions exist).

**MINOR-2 (process/reproducibility, L28): the solver invocation is not frozen in the candidate or in any species-0 receipt.** L28 says only "Local Kissat 4.0.4 … produced ASCII trace" and admits the console transcript is not frozen. With kissat 4.0.4's *default* options the trace contains extension variables/RAT steps that the two pinned RUP checkers (and mine) cannot verify, so pure-RUP checkability depends on the `--plain --no-factor …` option set that appears only in `frontier-20261028-q1-support-proof-batch-v1.py` (SHA256 22a99215…), which the candidate does not cite. I reproduced the pinned proof byte-for-byte with that option list, so the gap is documentary, not scientific. Suggested fix: pin the exact argv (and that the trace is byte-reproducible) in a species-0 solver receipt.

Notes (no finding): the physical control's "Gram entries" (L30) are evaluated by symbol equality, which equals the complex Gram entry only because the control family is classical — accurate for its stated purpose. The author's three RUP tamper controls and three CNF-mutation controls behave as described in the receipts I read; I did not use them as evidence.

## 7. Unverified imports and scope limits

- Not verified: HTTP byte identity of the Wanless snapshot (only reader-level agreement of the first triple today); that the catalogue's 38+1 species exhaust all 3-MOLS(8) nets (Hcat); that "species" in the catalogue coincides with full net isomorphism (if narrower, this result is stronger, not weaker); the results for species 1–38 (batch receipts exist in the owner root but are outside this manifest and were not reviewed).
- Checker trust: UNSAT rests on my RUP checker (and, independently, the two author checkers and a byte-identical kissat replay), not on a certified kernel (no drat-trim available on this host; cadical present but not used). Same-harness only.
- The reduction uses the registered definitions quoted in `intake-v1.md`; the primary Ball–Simoens/Musto–Vicary source text was not opened for this review.

## 8. Receipt inventory (this directory)

| file | SHA256 | bytes |
|---|---|---|
| `reviewer-cnf-semantic-audit-v1.py` | acad33ef9d9c63d516fe6fc0a6f6b69a23e9ec736a66b72a6ee25d6b90984fc1 | 11527 |
| `reviewer-cnf-semantic-audit-receipt-v1.json` | 8c1397efe33683c3b4b0d8e23425a2559cf31d4d00a9fc4492859aff61788fad | 915 |
| `reviewer-rup-check-v1.py` | 61e294826beeea199c002c050d37a844c67c645ce69535f3686f762f08353687 | 4368 |
| `reviewer-rup-check-pinned-receipt-v1.json` | 62044b4a9280a71b2e70a7883e1186247a16f89e1d6093748c233efc2d881bb8 | 784 |
| `reviewer-rup-check-noN-pinnedproof-receipt-v1.json` | eb641c8441b2df6b6f3b680bcea4a7de21ff8d09b4a15d22fb2cbc1bc31af62a | 700 |
| `reviewer-rup-check-noN-freshproof-receipt-v1.json` | b9ec6dd9d63b98fdfacbfec608470cbf11fb401d8c588c5705d637454013068d | 611 |
| `reviewer-controls-v1.py` | a6ee27b1cd011040555437de7a52d80b7ae2fc94c5b8bfeadbca177a0dbfcadc | 3847 |
| `controls/species0-plain-kissat.drup` (= pinned proof) | 2d405f676add4fe7967e98722834c536d9545ed1a0038f4546b1721e55b33599 | 3401 |
| `controls/species0-without-nonclassical-clause.cnf` | ff9aacd162821b883be03d3a7deb5ac9b71185718d8dc5e34324e7b4badd052b | 101010 |
| `controls/species0-without-nonclassical-plain.drup` | 60f74f91a7d11df567337fd2bbe8bfebcec100130174fbcc8081b52f2663a092 | 8963 |
| `controls/species0-fresh-kissat.drup` (default binary, diagnostic) | 9fdca7cd4b50a101ccf0c63344bfb9ebf1aa060d5c2431834eb944bf7a6afdcc | 97013 |
| `controls/species0-fresh-kissat-ascii.drup` (default ASCII, RAT/extension vars, diagnostic) | 4621465b1379b912292cb1809ecd1a83048d851ee31fdfdf73c813bb39618a18 | 212799 |
| `controls/species0-without-nonclassical-clause.drup` / `-ascii.drup` (default runs, diagnostic) | 635a9e355b981a24c254965368111ac39344c70e84a024e7886b410cac3ab539 / a982351b691915e325d3e6facde5721409f0609ba701f2b0f9328fc4ce591340 | 97728 / 214129 |

Disposition recommended to the parent: accept the species-0 net exclusion at the sharpened scope of §2 as a same-harness-reviewed finite certificate (not a parent certificate acceptance: the strict drat-trim/FIFO replay named in L5 remains the parent's); request the two MINOR additive corrections; nothing here extends to other species, Hcat, or global q1.
