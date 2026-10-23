# FC19 review package v1 — both p=19 cells

Owner: OlsonThirdCutWindow, same throttled math2 slot. Written after /bin/date 2026-10-20T10:37:35-0700.
WRITTEN CANDIDATE, NOT YET REVIEWED OR ACCEPTED. Outcome: proof complete in BOTH cells, separately, relative to
CORRECTNESS_ACCEPTED_SCOPED_PARTIAL UMR through parent errata v1 and v2. No review is run by this worker.

## 1. Exact claims and cell statuses

| Cell | Claim | Written outcome | First unproved step in this packet |
|---|---|---|---|
| (kappa,p)=(7,19), terminal k=20, kappa_hat=7 | Theorem FC19(a): full cell excluded | Proof complete, candidate | None relative to accepted UMR inputs |
| (kappa,p)=(8,19), terminal k=20, kappa_hat=8 | Theorem FC19(b): full cell excluded | Proof complete, candidate | None relative to accepted UMR inputs |

The full existential NF/word antecedent is retained: a length-74 word over D_38 with no identity 38-subword in increasing
original index order, SOME admissible NF, extra reflection pairs anywhere in the odd blocks, every empty run separating
different reflection values. No o_F, nonempty-run, rotation-pair or rigidity premise. Both new counts hold in EVERY
frame, including any frame that would be called RES. No UB, saturation or Lemma20 converse is used. No remaining
residual is left in either of these two cell proofs. No implication from one cell to the other is used.

UMR-F, literal frame/window lemmas and the total identity are accepted premises at the exact scope of UMR verdict
LF7-11, read through both errata. FC717 is method inspiration only, NOT a premise (its status is pinned by the
transition). No UMR claim outside its accepted scope is needed.
Non-claims: any other cell, prime, kappa or terminal k; a full p=19 union beyond these two kappa values; full ordered
Olson; INV*, reflection rigidity, o_F assembly, priority, novelty, Lean, human-referee or runtime verification.
The parent controls mathematical review, acceptance and all composed claims.

## 2. Argument map and recommended review order

The data contract (D1)-(D3), derived at literal UMR scope, uses only letter counts, nu>=a, nu=a mod2, e>=nu-a,
a'>=14, nonzero-even empty theta and the central windows. Identity (D4) is independent of the new counts:
Xi(S_even)+Xi(S_odd)=e>=0. Both WC719 and WC819 give the contradictory <=-1 bound from (D1)-(D3).

(7,19): R=32,g=6. The level-5 UPPER window has x=max(eps,6-q,4-q'). Sort top5/bottom5 in each alternating ten-run
set. Types G/P/Q (generic/near A^c/near A) cover every top5. Near A with fifth theta>=0 is impossible. Near A^c with
fifth theta0 leaves at most two outside letters. Disjointness and empty-run bonuses close all pairs (Sec.3).
No LOWER window is used in this cell.

(8,19): R=34,g=4. Combine level5 x=max(eps,8-q,6-q') with level6 x=max(eps,6-q,8-q'). Six classes C1-C6 cover every
sorted alternating set. C3 is the nonnegative-top5 near-A^c case, leaving <=4 outside letters. C6 is the hybrid
near-A top5 / near-A^c top6; its sixth run contains >=22 A^c letters. All ordinary pairings close by empty-run
coupling. The negative hybrid uses the same coupling. The nonnegative hybrid uses all five swapped 5-subsets
Q_v=(J5\{v})u{sixth run}; summing their inequalities gives 5o+8a+8e(J5)<=16. The other alternating set is then sparse,
and the level5 LOWER window closes the only delicate negative-five possibilities (Sec.4).

Review focus:
- Lemma3.2(c): both near-A top5 sets with fifth theta=-1; the lower estimate is from empty TOP runs.
- Lemma4.2: LOWER-window bound e-nu>=-a yields Theta(K)>=-2-max(a+1,6+beta'(K)); empty negative five needs beta'>=2.
- Lemma4.4: both sparse subcases, theta6=-1 (>=3 nonempty top runs) and theta6<=-2 (negative-five lower window).
- Lemma4.6 Steps1-4: parity nu=a, swapped-set q' calculation, sum over all five v, and forcing a=0,o=3=l(S').
- The completion paragraphs: check that the class pairings are exhaustive and no UB hypothesis was inserted.

## 3. Immutable artifact bindings

Paths relative to /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells.
| File | Bytes | Whole-file SHA256 |
|---|---|---|
| FC19-scope-v1.md | 6414 | 889acf673aed2005ee3ab412d5d82050c7026d053e54844574a000619eee3c05 |
| proof-FC19-v1.md | 24042 | 10cc94b0210274167b1aa124e2a977b1b94c65275c153cd8a4492564e1bdb57b |
| erratum-1-process-wording-v1.md | 1497 | 6642ac5fe622fc0007164cae223bc9448ee8c0e06e615c663527700ccbfda528 |
| review-excerpts-FC19-v1.json | 2311 | d41ff0561aeea19b9e0935e58446c80303c8aed0f23b39e3b82fdc14bcc0ba21 |
| checkpoints/cp-01.md | 1281 | 9ce2541a6dd21056835e7df2ab6a661741c11f9812dd8ab9453e9a5802ea6be6 |
| checkpoints/cp-02.md | 1336 | acf8c823fa9b674e9bcc2299ad6e01c10e42fec3635c9f275054aedfaccee2d1 |
| checkpoints/cp-03.md | 1598 | 643ace91af5f9a2d1e848574d3b13cbc16c0dac0fc5470397bbeb39ad91778a3 |
| checkpoints/cp-04.md | 811 | 917b21f5d62fe4ddcbd9bdd68f1905d53d1da2521b3a041a357060f6ac924744 |
This package and closing cp-05 are bound in the closing checkpoint/final handoff, without a self-hash cycle.

## 4. Excerpt manifest and byte bound

review-excerpts-FC19-v1.json is a ten-entry JSON list {path,sha256,start,end}; paths absolute, LF endpoints inclusive.
It includes the new proof LF1-261, frozen scope LF1-78, process-wording erratum LF1-18, authority LF1-49, UMR verdict
LF1-38, UMR proof LF1-258 and LF344-355, both governing UMR errata (v1 LF1-10, v2 LF1-9), and FQW frontier LF9 only
(context only). All source hashes match their pins. FC717 is deliberately not a mathematical source in the manifest;
its method exposure and exact hash are disclosed in the scope and proof interface. Primitive NF/GRX/SC0/FB inputs
enter only through accepted UMR, not by an unreviewed extension of their scopes.
Metadata-only counts: 72,503 raw selected bytes, 734 LF lines. With each selected line prefixed by five decimal
digits and '|', and each excerpt headed '\n### ABSOLUTE_PATH\nSHA256 HASH; LF START-END\n', numbered source text is
79,005 bytes (<100,000). The package/manifest/checkpoints fit within the remaining allowance. No numbered-source
copy was created; the manifest supplies the sources. JSON was drafted and checked by eye, not machine-parsed.

## 5. Process, qualifications and machine steps

Freeze 2026-10-20T10:04:27-0700 preceded all NEW derivation, including arithmetic checking the parent hint. Entire prior
UMR/FC717 exposure and earlier unpublished attempts are disclosed in scope Sec.4. The hint is untrusted and no lemma
premise. From the post-freeze constants it is derived that the real balanced level is5.5; the actual proof uses
levels5 and6 as specified above. Prior UMR process qualifications remain inherited and are not recertified here.

Checkpoint times: cp-01 10:11:27 (420s after freeze), cp-02 10:24:30 (783s), cp-03 10:35:00 (630s), cp-04 10:36:24
(84s). No gap over1200s; checkpoints bracket substantial derivation and completed drafts. Closing cp-05 follows.
The process-wording erratum corrects: scope's UB-failure exposure is only UMR's unexcluded-method cases (no universal
UB failure); pre-freeze wc covered authority/verdict/v2 only; cp-01's read claim excludes truncated, unused UMR LF400.
No target change, missed freeze or cadence breach is identified. No proof erratum was needed before delivery.

Pre-creation proof wording replacements (cp-03): D1 cites nu>=a/Pi0>=a' explicitly; part(a)'s completion cites all
of Lemma3.1; the symmetric threshold case in Lemma4.3(c) is explicit; candidate status added; label citation expanded
to LF88-110/interface LF88-118. Four in-memory parts were created once as the immutable proof, with no file edits.

Machine operations, complete categories: /bin/date for timestamps; shasum -a256; wc byte/LF counts; reading files;
mkdir assigned directory/checkpoints; exclusive creation of drafted text via Python open(path,'x'); metadata-only
byte/LF counting of selected source ranges and the documented numbering/headers in Python. In-memory text drafting,
readback and wording replacements are not scientific computation. No assertion statements, scripts, enumeration,
solvers, tests, Lean, model CLIs, nested agents, network, /tmp, deletion, commit or push. Mathematical derivations and
case analysis were by hand. Candidate complete; after final binding, park without another target.
