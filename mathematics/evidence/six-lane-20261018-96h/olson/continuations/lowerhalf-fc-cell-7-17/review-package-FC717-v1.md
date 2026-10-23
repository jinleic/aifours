# FC717 review package v1

Owner: OlsonThirdCutWindow, same throttled math2 slot. Written after /bin/date 2026-10-20T09:40:07-0700.
Outcome: CONDITIONAL PROOF COMPLETE for the single cell (kappa,p)=(7,17), terminal k=18, kappa_hat=7.
No model review was run by this worker. The parent controls review, acceptance and composed frontier claims.

## 1. Exact deliverable and prerequisite

Theorem FC717: assuming the literal UMR-F and UMR Lemmas 3,5,7,8,10,13 at (7,17), read with UMR parent erratum v1,
no length-66 avoider over D_34 has SOME admissible NF with terminal k=18 and kappa_hat=7. Full existential NF/word
antecedent: arbitrary extra-pair placement in the odd blocks, genuine empty-run rule, no o_F/nonempty-run/rotation-pair/
rigidity premise. EVERY UMR frame is covered, including RES, without requiring that either UB condition hold.

UMR remains NOT ACCEPTED under this assignment (one-family support plus parent hand-check, second family pending).
The word-level exclusion is explicitly CONDITIONAL; an accepted cell result requires accepted UMR premises. There is
no claim of independent UMR verification. The new integer-window lemma WC717 is proved from the reduced contract
(A1)-(A4) of proof Sec. 1; it does not use UMR's unproved final count or its total identity during the count.
No failing step remains relative to the permitted conditional premises.

No other cell, k, prime, full p=17 union, full ordered Olson, INV*, reflection rigidity, o_F assembly, priority,
novelty, Lean, human-referee or runtime claim. FQW's frontier is context only, not a premise of the count.

## 2. Argument and review focus

The balanced central level m=5 has ell=M=6 and the letter-length window [6,24]. Conditional UMR yields the symmetric
five-subset bounds
  e-2-nu-chi(Q) <= Theta(Q) <= -2-nu+chi(Q),
  chi(Q)=max(1,6-q(Q),6-q'(Q)), q(Q)=|L(Q) symdiff A|, q'=30-q.
The literal UMR offset is no larger than chi; weakening to chi is proved in Sec. 1. A total-excess fact derived from
label definitions, not imported as an extra margin, is e>=nu-a>=0. Empty theta values are nonzero even integers.

For each alternating set of nine runs, sort the top five J and bottom four B. Types G, P and Q mean respectively
min(q,q')>=5, q'<=4 and q<=4. The fifth theta t satisfies t<=0; type Q cannot have t=0. A generic set gives Xi<=-3,
where Xi=Theta(S)+nu+2. Negative-threshold exceptional sets give Xi<=-2-k if t<=-2 or Xi<=2-k-e(B) if t=-1.
- Both P is impossible since a'>=13>8; mixed P/Q gains enough empty bottom runs to give Xi_sum<=-4.
- Two Q with t=-1 give k1+k2>=6+nu from EMPTY TOP runs, hence Xi_sum<=-2-nu. The remaining negative-threshold Q/Q
  cases also close (the only zero-loss corner forces an empty fifth run to have theta=-1).
- Case H (P,t=0) leaves at most four letters outside J and nu+k<=4. The sparse lemma is the important LOWER-window
  step: when nu<=4, an alternating set with <=2 letters has t<=-2; one with <=1 letter is impossible (bottom-five
  lower bound >=-9, but its fifth threshold makes their sum <=-10).
- H is split explicitly by n=0,1,2,3,4 nonempty bottom runs. n>=3 is sparse-impossible; n=2 uses the sparse threshold
  and disjoint A/A^c letter sets; n=1 has exact other-top sum1 and empty bottom runs; n=0 retains the empty-run bonus.
Thus Xi_even+Xi_odd<=-1 in all cases. Conditional UMR independently gives the sum=e>=0, the contradiction.

Review priority: proof Lemmas 2(c)-(d), 3(b), and every case n=0..4 in Lemma 4. No saturation gloss or converse of UMR
Lemma20 appears in any inference. Empty-run bonuses, especially the n=0 corner, are not discarded.

## 3. Frozen files

All paths below are relative to the assigned directory; all files were created exclusively, never edited.
| File | Bytes | Whole-file SHA256 |
|---|---|---|
| FC717-scope-v1.md | 6325 | 869d0ca7ab1cfd76d4e2c170b5813c5d6da53cc8260363ad06c8c01ec111fcad |
| proof-FC717-v1.md | 18792 | e2c74806fc5f1986b298d490b121676eff7dce5f90f014311d3d8c099800b945 |
| review-excerpts-FC717-v1.json | 1845 | 321af70443fc74790c6928f9edbc443dadfd6f81b8bc1f8280b20c478fb6a82b |
| checkpoints/cp-01.md | 2377 | 471fa7321884dace30ba831b54cfb2746cf3d1e59422a6e74649710e7bf29c14 |
| checkpoints/cp-02.md | 967 | 643f6b66086d9c7663c20cbf675fc3a628b88a0535b6e4fbf8653e152c2f3938 |
| checkpoints/cp-03.md | 979 | 77b779ee3707202a74b760e3f878db554be8f39ed0997c20ad757ff3871bbad7 |
| checkpoints/cp-04.md | 1050 | 81e0bc06c260f61a61061d8c1a37d0912e5288c0f43c662885bcbbafa46ebacd |
The package and closing cp-05 are bound in cp-05/final handoff (no self-hash cycle).

## 4. Manifest and packet size

review-excerpts-FC717-v1.json is an eight-entry JSON list {path,sha256,start,end}; paths absolute, ranges inclusive LF:
- Own proof LF1-231 and frozen scope LF1-75.
- Authority LF1-70.
- CONDITIONAL UMR proof LF1-258 (contains all frame, window, theta, total premises used; no unproved FC is imported).
- Governing UMR parent erratum LF1-10 (MUST be read with UMR).
- UMR first-family disposition LF1-24 (status only).
- FQW verdict LF1-9 and terminal range clarification LF1-7 (context only).
All hashes were checked at intake and again before this package; no mismatch observed. Metadata-only measurement:
63,060 raw source bytes, 684 selected LF lines. With each line prefixed by five decimal digits and '|', plus one
header per excerpt of the form '\n### ABSOLUTE_PATH\nSHA256 HASH; LF START-END\n', the selected source text is 68,838 bytes.
This is below 100,000 bytes with ample room for the package, manifest and checkpoints. No new numbered-source file is
created; the manifest is the review input. JSON was drafted and checked by eye, not machine-parsed.

## 5. Process and exposure

Freeze: 2026-10-20T09:26:06-0700; no new derivation before it. Prior UMR/FQW/P7L/TCW derivations, including the (7,17)
constants and all unwritten RES attempts from UMR, are disclosed in scope Sec. 3. After freeze the governing erratum,
review status, frontier context and conditional UMR ranges were read. The erratum's top-level connectivity restriction
is retained; its withdrawal of LF328-330 saturation is binding. A surviving word's EVERY frame would have to survive
the count, but the count below excludes each individually (relative to UMR).

Checkpoints: cp-01 09:32:13 (367 s after freeze), cp-02 09:35:26 (193 s, before sparse/H drafting), cp-03 09:37:11
(105 s, after H), cp-04 09:38:29 (78 s, after proof creation); no gap over 1200 s. No output loss.
The proof was drafted in three in-memory text parts. Two pre-creation wording replacements (CONDITONALLY ->
CONDITIONALLY; type-name notation) are disclosed in cp-04. No file was rewritten. An unused post-freeze idea about
extending m=0/1 windows is disclosed in cp-01; no claim or premise depends on it.

Machine operations, complete categories: /bin/date; shasum -a 256; wc byte/LF counts; reading files; mkdir of the
assigned directory/checkpoints; exclusive creation of drafted text with Python open(path,'x'); metadata-only byte/LF
counts for selected source ranges and numbered prefixes/headers in Python. No scientific computations, scripts,
enumeration, assertion statements, solvers, tests, model CLIs, nested agents, network, /tmp, deletion, commit or push.
No mathematical checks were delegated or run as code. No process deviation is identified in this assignment; the
metadata counts and pre-creation text replacements are disclosed rather than described as mathematical validation.
