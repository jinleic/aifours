DISPOSITION: ACCEPT-BRIDGES-WITH-RESIDUALS

This audit is static reading of the inlined texts only. I ran nothing. Items I could not verify are marked UNCHECKED and summarised at the end.

## FATAL

None. I found no reachable path by which a counted UNSAT is unsound, and no path by which a valid array escapes the cover. Every encoder admits the section-8-normalised arrays. The items below are gaps in evidence or in acceptance code, not demonstrated holes.

## MAJOR

**MJ-1 (S). CNF delivery into drat-trim is unbound on every FIFO route, and drat-trim's early-EOF path is undefined behaviour. I contest the desk's "O" label.**
- **How the CNF reaches drat-trim.**
  - It goes through a FIFO written by `_writer`, which swallows OSError and records no completion (lane/src/stream_check15.py:376-381, lane/src/stream_check5.py:42-47).
  - The recorded `cnf_sha256` hashes the in-memory bytes (lane/src/stream_check15.py:412). It does not hash what drat-trim parsed.
- **What drat-trim does on an early CNF EOF.**
  - It sets fileSwitchFlag and breaks without reading any proof (lane/tools/drat-trim/drat-trim.c:1128-1134, :1149).
  - `formula[]` is sized from the header (:1085) and filled only for clauses actually parsed (:1218).
  - Lines :725-729 then dereference `formula[i]` for every i < nClauses and treat `clause[0]==0` as an empty formula clause.
  - Unless post-loop code that is not inlined resets nClauses, this is undefined behaviour that can plausibly end in `s VERIFIED` with rc 0.
- **Why it cannot be audited after the fact.**
  - Records keep only the s-lines, rc and stop (lane/src/stream_check15.py:559-565).
  - The early-EOF warning (drat-trim.c:1130) and the parse line (:1067) are discarded.
- **How likely it is.** A partial write to a live reader is practically remote.
  - Never-opened writer: drat-trim blocks and is terminated.
  - Zero bytes written: drat-trim exits with "no p cnf" and no s-line (:1064-1065).
  - Reader closed first: benign.
  - So this is not FATAL. But it is a soundness hole in the evidence chain, not an operational one (PROOF-MAP-v4.md:169-175).
- **Affected routes:** b (rev 1-5 streamed), c5, d/e records of rev ≥5, cell, and every M2 record including m2q0c.
- **Unaffected routes:** route a and E0-M1, which read CNF files from disk (lane/src/run_proofpass.py:50, lane/src/check_proofs.py:37).

**MJ-2 (O). Acceptance code does not fail closed.**
- (a) M1 split cover accepts n = 0 vacuously (lane/src/aggregate15.py:138). aggregate16 changed only the M2 branch (lane/src/aggregate16.py:160-169), so the M1 path is still vacuous.
- (b) `certified()` falls through to "drat_trim_verified and checked" for any unlisted or absent revision (lane/src/aggregate15.py:68). Unknown revisions therefore fail open.
- (c) The `multiset` key plus a 2-entry list is still read as a range (lane/src/aggregate15.py:92-93).
- (d) Several bindings are never checked:
  - filename against indices;
  - the record's tag, multiset or b_index against its path;
  - the record against an ext.json hash, encoder hash or rebuilt CNF.
- (e) E0 is counted by file count, with "graphs" hard-coded to 486 (lane/src/aggregate15.py:173-182). There is no per-index or graph6 coverage, and `*.check.json` matches any name.
- (f) Route b trusts `ps["ok"]` and `drat_trim_verified` with per-revision semantics (lane/src/aggregate15.py:115-117). Rev 1 is substring-only, and the rev 1-4 code is not inlined (UNCHECKED).
- None of these is shown to affect a counted case. But "M1 0 open" (lane/cycle2/m1-complete-candidate-20261018T012523.json:137) cannot be accepted until a parent fail-closed aggregator re-derives it from a frozen snapshot.

**MJ-3 (O). Most formula and list bindings rest on the producer or on a sample.**
- Split records: R8 covered a 374-record sample plus inc-001 (253 records, list unverified) out of a census of 25,711 at 14:56, with more records after that (review/pa19-subcase-binding-v1/README.md:7,11,14-15).
- Placement lists: 18 ms06 lists and all later M2 lists are producer-only (PROOF-MAP-v4.md:122-129).
- CNFs: M2 direct CNFs and E0 CNFs for both methods have never been rebuilt by a parent (PROOF-MAP-v4.md:69-71).

**MJ-4 (O). One checker and one harness serve both methods, and there is no parent native replay.**
- M1 and M2 share the same drat-trim binary and the same staged harness (review/pa19-encoder-scout-audit-v1.md:80; PROOF-MAP-v4.md:234).
- Staged proofs are not retained (lane/README.md:777, :787).
- The binary-to-source build has no record.

**MJ-5 (O). M2 is incomplete: 166 cases open at the pin** (lane/cycle2/m1-complete-candidate-20261018T012523.json:6,138). The contract requires an independent method (run/screening/info-1-packing-array19-contract.json:22).

## MINOR

- **mn-1 (O). The pinned M2 ms09 tally may contain the vacuous b3 0/0.**
  - ms09 shows "partbatch-drat: 1" (lane/cycle2/m1-complete-candidate-20261018T012523.json:131-134).
  - Under aggregate15, an existing empty ext.json counts as partbatch (lane/src/aggregate15.py:155-158).
  - The inlined data cannot tell whether that 1 is ms09_b00003 or ms09_b00002. Recompute with aggregate16. M1 is unaffected.
- **mn-2 (S, unreachable). Substring-only acceptance can admit the rc-1 "trivial UNSAT" verdict.**
  - Path a, E0-M1 and rev 1 accept the `s VERIFIED` substring without an rc gate (lane/src/run_proofpass.py:53; lane/src/check_proofs.py:40).
  - So they would accept `\rc trivial UNSAT\ns VERIFIED` with rc 1 (drat-trim.c:1480, :1500).
  - The M1 encoders never emit an empty clause (encode_e1 only adds non-empty clauses or units). The parse condition that produces "trivial UNSAT" is not inlined.
- **mn-3 (O). The s00468 production run deviated from the frozen contract.**
  - The contract freezes `run_s00468_cell.py`/`summarize12` at rev 13 (lane/cycle2/s00468-six-unit-contract.json:25-28).
  - Production used `run_s00468_cell14.py` and `summarize15`, and accepted rev 13/14 (lane/src/summarize15.py:51).
  - This is benign because summarize15 rebuilds each expected subcase CNF itself.
  - summarize15 does not check that the base contains the clause `421..426 0`. That fact is established statically (lane/src/encode_skel.py:37,40) plus the runner's byte-identity assert (lane/src/run_s00468_cell14.py:49-57).
- **mn-4 (O). SAT listing skips several trees:** m2q0b, cycle2/m2skel*, *_strict and archives.
- **mn-5 (O). The genbg help excerpt never says which class each number in `#:#` applies to** (lane/cycle2/genbg-help-flags.txt:1-6). The flag semantics are corroborated only by the R3 bijection with gen_skel, which uses geng.
- **mn-6 (O). Documentation and control gaps.**
  - R8's census shows 16 `_exact` records, but the map names only f00012 (review/pa19-subcase-binding-v1/README.md:7).
  - The contract's PA18 positive control never exercises the production cover (lane/README.md:141-142).
- **mn-7 (S, unreachable). Code nits.**
  - build_v2 treats n = 0 as n = 1 (lane/src/encode_skel_b.py:566-571).
  - build_partbatch's `[v]*(n-2)` silently drops n = 1. This is guarded by the P1 assert (lane/src/encode_skel_b.py:401,459).
  - extend_b has dead code: `compatible` (lane/src/extend_b.py:80-83).
  - The encode_skel_b docstring says "column-major" (:23-24). Both orders work for the generators involved.
- **mn-8 (O). aggregate16 records the empty-list sha but does not compare it** with 2fd71b8e… or validate the structural JSON (lane/src/aggregate16.py:160-167). Since the row is not counted, this is harmless.

## Bridge verdicts

- **B1: PASS.**
  - `partitions` is exhaustive (lane/src/profiles.py:13-25).
  - Budget is 171 − 8·21 = 3. There are exactly 6 profiles, all with six nonzero parts, and 10 multisets in the documented index order.
  - L = 171 − Σκ counts the pairs that agree nowhere. Every multiset is covered (lane/src/profiles.py:32-48; review/pa19-parent-cover-replay-v1/cover-binding-result.json:5-11).
- **B2: PASS-WITH-RESIDUAL.**
  - Re-derived: n2 = 13 + n0, n0 ≤ 3, simple graph, max degree 4. The 16-edge count of 6 matches the six 4-regular graphs on 8 vertices.
  - encode_q0: every constraint is necessary, and value precedence plus row lex are lex-leader in row-major order (lane/src/encode_q0.py:68-130).
  - encode_q0b: the Q_d∖Q_c rows pairwise agree in column d, so they sit in distinct triples, and the fixing is a per-column relabel (lane/src/encode_q0b.py:70-82).
  - Leave witnesses cover every possible agreement (:89-110).
  - Residual: no parent rebuilt the E0 CNFs, and coverage is not checked per index.
- **B3: PASS-WITH-RESIDUAL.** Every pruning is a necessary condition:
  - tmax = min(c0, 2 − wmin), because w ≥ wmin.
  - hmax is a union bound, because |T| ≥ 3 forces w ≤ −1.
  - Greedy interval matching and Kuhn matching are exact.
  - Linearity: in gen_skel, geng's simple graph plus the covered-pair checks; in gen_skel_b, `-Z1` (C4-free, so two rows share at most one quad).
  - Max degree 4, at most 19 rows, and h ≤ 2c0 (lane/src/gen_skel.py:61-116; lane/src/gen_skel_b.py:86-120).
  - Deduplication merges only kind-preserving incidence isomorphisms, which are genuine skeleton isomorphisms (lane/src/gen_skel.py:119-134; lane/src/compare_skel.py:49-58).
  - Trusted: geng/genbg completeness, the soundness of `nx.is_isomorphic` (a false True would drop a class), and graph6 parsing.
  - Shared by both generators: the formulas (re-derived above), the nauty package and networkx. Profile order is asserted (lane/src/compare_skel.py:36-37).
- **B4: PASS-WITH-RESIDUAL.**
  - (a) All M1 encoders and build_v2 break symmetry only with A ≤ g(A) constraints, for generators of the fixed-structure stabiliser, in one row-major integer order.
    - Non-adjacent `nxt[0]` row pairs are still transpositions whose intermediate rows are untouched (lane/src/encode_partq.py:118-132; lane/src/encode_full2.py:110-126).
    - In M2 v1, P0 fixing relabels P0 columns only. The remaining constraints act only on special-column cells and never move rows (lane/src/encode_skel_b.py:468-499).
  - (b) Every counting encoding admits every intended assignment, by setting each auxiliary variable to its exact unary or prefix meaning:
    - the Sinz counter (lane/src/encode_e1.py:44-63);
    - the weighted counter, including the w > cap units (:69-93);
    - the two-sided totalizer (lane/src/encode_skel_b.py:40-74);
    - binomial counts and the 4-clauses;
    - the u/z miss variables, which are only lower-bounded, which is harmless.
  - (c) The section 4 claims (PROOF-MAP-v4.md:92-98) are confirmed:
    - target = 2 + ns − |T| + #(n=1) ≥ Σ_X(min_X − 2) + #(n=1) ≥ 0, and target ≤ 6 < 18 ≤ len(o);
    - the weighted cap is ≥ 6 + L;
    - all counts are ≥ 1;
    - 2 − t ≥ 0;
    - Σl = 38 − 4c0 − 6ns = 2L.
  - Residual: build/build_part v1 are not inlined (UNCHECKED if any m2part_drat f*.json exists).
- **B5: PASS-WITH-RESIDUAL.**
  - extend_p1q's conditions are necessary.
  - Class uniformity holds because availability and agreement depend only on history (lane/src/extend_p1q.py:74-75, 96-108).
  - The extend_p1 diff is a q-generalisation only.
  - extend_b is complete:
    - count vectors plus within-class canonical rows;
    - Aut(S) is the full skeleton group, since types of size ≥ 2 are distinct;
    - merging happens only on equal canonical keys (lane/src/extend_b.py:54-126).
  - Selector batching gives "batch UNSAT ⇒ every listed subcase UNSAT", because placement-specific clauses all carry ¬t_i (lane/src/encode_partbatch.py:46-61, 113-135).
  - rerun_batch12 binds to the original CNF sha (lane/src/rerun_batch12.py:44-46).
  - `_exact` uses a sound strengthening (lane/src/encode_full2.py:88-95).
  - The denominators come from ext.json, not a heuristic.
  - Residual: MJ-3; rerun5 `_r3` is not inlined.
- **B6: PASS.**
  - The base is byte-identical to a fresh `encode_skel` rebuild, and the literal is asserted to be 421 + s (lane/src/run_s00468_cell14.py:47-59).
  - The ALO clause of cell (8,6) is at lane/src/encode_skel.py:40.
  - summarize15 rebuilds the six expected subcase files and applies the full predicate (lane/src/summarize15.py:25-55).
  - The cover is pure case splitting on that clause.
- **B7: PASS-WITH-RESIDUAL.**
  - Rev 11-15 gates: solver self-exit with rc 20, no cap, reader EOF reached, drat-trim self-exit with rc 0, exact s-lines, replay sha and length, no admission or abort (lane/src/stream_check15.py:556-567; lane/src/aggregate15.py:57-60).
  - rev 9 and rev 5 gates are as described (lane/src/stream_check9.py:149-156; lane/src/stream_check5.py:143).
  - Retired, lratstrict and capped records are excluded.
  - Residual: MJ-1, MJ-2 and mn-2.
- **B8: PASS-WITH-RESIDUAL.**
  - The parent argument is correct: 171 = C(19,2), t + Σe = 2, h needs e = −1 three times, and there is no partner (snapshot-supp2/pa19-ms09-b3-structural-parent-v1.md:21-27).
  - extend_b reproduces it: h is forced into P, singletons are blocked by the shared quad (lane/src/extend_b.py:94-100), and the empty class fails `ok_row(0,−1)`. So raw = 0 (lane/cycle2/m2part_drat/ms09_b00003/ext.json:1).
  - The worker JSON's extend_b, encode_skel_b and list hashes match the inlined banners (lane/cycle2/structural-ms09-b00003-proof.json:48-54).
  - aggregate16 fails closed for M2 only. It still accepts an empty M1 list (aggregate15:138 path unchanged). See also mn-1.
- **B9: PASS (not load-bearing).** The (13,5,4) runs, control13-v5, the checker smoke, PA18 and the verifier mutations are all post hoc. None of them carries any proof. Raw outputs are UNCHECKED.
- **B10: PASS-WITH-RESIDUAL.** Two dispositions are contested (below).
- **B11: PASS-WITH-RESIDUAL.** See the next two sections.
- **B12:** listed in the final section.

## Old scout gap dispositions

**Cover scout**
- **Major-1: CONFIRM.** M1 has 0 open, conditional on MJ-2. M2 is open at 166.
- **Major-2 pass-1 CNF: CONFIRM.** Routes a, b and c5 gate on the pass-1 sha. Resolution depends on R5, whose receipt is not inlined.
- **Major-2 split records: CONFIRM PARTIAL.** Only R8 sample plus inc-001.
- **Major-2 manifest: CONFIRM PARTIAL.**
- **Major-2 open-list cut: CONFIRM RESOLVED** (aggregate15:185).
- **Major-2 ms00 486: CONFIRM PARTIAL.** It is effectively still open: files are counted, not indices.
- **Minor-3: CONFIRM.** I re-derived the formulas.
- **Minor-4: CONFIRM for :137 and :262.** Lines :47 and :83 are not inlined (UNCHECKED).
- **Minor-5: CONFIRM still present.**
- **Minor-6: CONFIRM.**
- **Minor-7: CONTEST (minor).** The help text does not define the order in `#:#`. Only the R3 bijection supports the reading.
- **f00012: CONFIRM.** encode_full2's exact leave is a necessary condition, and it is in R8's rerun sample.

**Encoder scout**
- **F1: CONFIRM**, conditional on rev 1-4 setting `drat_trim_verified` only from drat-trim (README:357-358; code not inlined).
- **Control receipts: CONFIRM PARTIAL** (UNCHECKED).
- **Uncontrolled production encoders: CONFIRM OPEN.** Static completeness is shown here.
- **Weak binding: CONFIRM PARTIAL.**
- **One checker: CONFIRM OPEN.**
- **64 KiB stalls: CONFIRM.** They were treated as UNKNOWN and then recertified.
- **FIFO names: CONFIRM resolved for rev ≥5.** For rev 1-4, cross-talk between same-name jobs is benign.
- **SAT listing: CONFIRM mostly resolved.** mn-4 remains.
- **Range heuristic: CONTEST "resolved".** It is still present at aggregate15:92-93 and in aggregate16.
- **Weak controls and nits: CONFIRM non-load-bearing.**

## Producer/sample-only representations

- **E0 CNF bytes (both methods).**
  - The parent bound only specs and graph6 (R2).
  - M2 E0 is bound to its index by construction in run_m2q0c (lines 32-39), which is producer code.
- **M1 split records.**
  - The CNF-to-(spec, ext, indices) link is covered only by R8's sample of 374 plus inc-001.
  - Records carry no ext.json or encoder hash.
- **18 ms06 M1 lists and every M2 list after R6.** Producer-only.
- **M2 direct (build_v2) CNFs and M2 batch records.** Producer-only.
- **The candidate's `binding_pass1`.** It is a worker sample (step 50, 940 split results; lane/cycle2/m1-complete-candidate-20261018T012523.json:141-146), not a parent check.
- **drat-trim binary to source sha d834b649.** No build record.
- **PA19FinalReceiptAudit's "min M1 num_full 41".** Not inlined.
- **Parent all-case bindings that do exist:**
  - R2 (graph indices);
  - R3 (both lists and all 9 maps);
  - R4 (specs);
  - R5 (5577 base CNFs, receipt not inlined);
  - the parent b3 microproof.

## Trust base

- The mathematics in sections 1-6 and 8, re-derived here.
- nauty geng/genbg completeness and flag semantics.
- networkx 3.7: `is_isomorphic` soundness, WL-hash invariance, graph6 parsing.
- CPython, json, hashlib and zstd.
- POSIX FIFO and pipe semantics, including the assumption, needed to close MJ-1, that a blocking write to a live reader never ends partially.
- The drat-trim binary (sha 111b0405), the single checker for everything, together with its parser on FIFO input.
- The stream_check rev 1-5, 9 and 11-15 harnesses.
- aggregate15 and summarize15.
- The integrity of all records: no mislabelled tag, index or list, and no forgery.
- The structural b3 argument (M2 only).

Kissat and CaDiCaL are not trusted; they only produce proofs.

## Residuals before final claim (ordered)

1. **Complete M2 independently.**
   - Close all 166 open cases under the strict predicate.
   - Re-aggregate with aggregate16 so b3 appears only as the parent-accepted structural row.
   - Get parent review for any further empty list.
2. **Close MJ-1.** Either:
   - add a documented OS-level argument to the trust base, and rely on M1 ∧ M2 dual coverage of every case plus a parent native replay from on-disk CNFs on each route (a, b, c5, d, e, cell, M2 direct, M2 batch, E0); or
   - re-check the streamed routes with file-based CNFs.

   Patch the harness to record drat-trim's parsed-clause count and any early-EOF warning.
3. **Run a parent fail-closed aggregator**, rerun on a frozen snapshot. It must:
   - reject n = 0 for M1 as well as M2;
   - reject unknown revisions;
   - drop the range heuristic;
   - check filename against indices and record identity fields;
   - verify E0 per index (0..485, matching graph6);
   - scan every result tree for SAT.
4. **Bind formulas for all cases.**
   - For split records: CNF sha from spec, ext.json and indices.
   - Replay the 18 ms06 lists and all later M2 lists.
   - Rebuild M2 direct CNFs and E0 CNFs for both methods.
5. **Add checker independence.** Use an independently built drat-trim or a second checker on a sample. Path-a DRAT files are retained.
6. **Contract items.** Add a PA18 or other positive control that exercises the production cover and the E0 encoders (non-load-bearing, but the contract requires it). Record the s00468 contract deviation.
7. **Update the proof map** to list all 16 `_exact` records and the M1 empty-list policy.

## Not checked

- stream_check rev 1-4 and 11-14.
- Runners other than those inlined, and rerun5.
- encode_skel_b build/build_part v1 (lines 77-380).
- drat-trim post-loop parse code, the trivial-UNSAT condition and argument handling.
- Record contents, the receipt census, raw outputs of controls, map contents, skeleton and ext files other than b3.
- R3, R5, R6 (except v2) and R7 receipts.
- README lines outside the inlined ranges.
- Candidate lines 149-657.
