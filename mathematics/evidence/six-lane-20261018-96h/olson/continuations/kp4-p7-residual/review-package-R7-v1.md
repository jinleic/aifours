# R7 review package: p=7, terminal k=8, kappa^=3 cell excluded (all non-pure cases; pure case re-proved), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T17:02:38-0700. CANDIDATE_UNVERIFIED written proof (outcome O1 of the frozen scope).
Parent owns both-family reviews and verdicts. No scientific computation, enumeration, script, assertion, solver, model CLI,
test/build or Lean was used; all case work is by hand in the frozen text. No novelty, priority or human-review claim.

## 1. Review exactly these frozen texts

- proof-R7-v1.md, SHA256 2619ab5d9aa2e673a2437587287542cc18cc11575eec8ff6d3eadfd0b336c0b7, lines 1-261, 25,852 bytes, read
  with erratum-1-proof-R7-v1.md, SHA256 6a8e6600ea806d5f6e03f11b951ce3b6044a534d5e201c6bb9999915501be22a (wording of one
  partition list in Sec. 5.3 C12 (c1); no logical change).
- Scope R7-scope-v1.md, SHA256 6310d69356c0ae85662dded3b3ff2d45d9ca3f8bf2ea42b0ffb01206092e8b39, frozen 16:40:24 BEFORE any
  derivation, with prior KP4 material and unwritten sketches disclosed. Authority: RUN/control/written-slot-transitions-olson-
  moqls8-20261019-1634-v1.json, SHA256 0c852bf12ebc5daa6e176ae465a038cb5e82f5f24d8355e925b09ada6276b0de.

Claims (full antecedent: SOME admissible NF of a length-26 avoider over D_14 has terminal k=8, kappa^=3; the three extra
reflection pairs anywhere in the odd blocks; empty runs separate different values; no o_F/run/pair hypothesis):
- THEOREM R7: no such avoider has a non-constant rotation multiset (the assigned target).
- PROPOSITION R7-PURE: none has all rotation letters equal (re-proved here independently of the pending KP4 Sec. 7.3).
- COROLLARY: the whole p=7 cell is empty. Not claimed: any combination with the pending KP4 p>=11 theorem; other cells;
  reflection rigidity, INV*, REFL, o_F assembly, ordered Olson; multiset-only statements outside the full antecedent.

## 2. Manifest, imports and byte boundary

Governing review-excerpts-R7-v1.json, SHA256 7a70a3bdc5a447dbdb260132376ddd7c6a2269be7162b1bd43bcf048e409fa38 (4,276 bytes):
JSON list {path,sha256,start,end}, whole-file SHA256, inclusive LF line ranges, absolute paths; 18 ranges from 17 files;
selected raw bytes 65,460, LF-numbered 67,905. Package + manifest + numbered excerpts stay below 100,000 bytes.
Load-bearing inputs: NF (ROT-few-E-v4 28-43; lowodd item 2/M1/M4, fewodd addendum 1 line 12, ZX overlays 1-3), GRX if
direction (notes-GRX 7-20; lowodd item 1/M2), RS(b) (proof-ROW 16-27 with R5, K=6 only) and classical Cauchy-Davenport inside
it. INPUT CHANGE: accepted UH-A (verdict 7c7b90f2... line 15, antecedent line 9, errata v1-v3) gives A>=9 at p=7, kappa=3;
used once (proof Sec. 2.4). Context only: the KP4 p=7 obstruction note (it names this residual).

## 3. Argument map and hostile-review focus

A. Sec. 1: SR7 lengths per m (C_max=Phi+6; n<=R=12 removes n=14); cycle facts on C_8.
B. Sec. 2 [RE-DERIVED]: Lemma P7 (six unequal pairs at n=6, RS(b) K=6); Lemma U7 (class {a,-a}, a!=0 by the block-value
   pigeonhole); normalization by the automorphism (v,e)->(v/a,e) with the sign chosen so A>=A'; window (W7): every proper
   nonempty set of runs has d=alpha-beta outside the band [A-6,6-A']; A'<=3; UH-A input A>=9, b=12-A<=3.
C. Sec. 3 [NEW]: Lemma S (negative side consisting of empty runs; both occurrence bounds |J|<=2nu and 2nu-|J|<=A kept).
   Lemma B (all-plus nu=4,5,6) and the exhaustive classification of the letters !=1 into twelve configurations C1..C12
   (check the excluded pairs/triples and beta=1+2omega). Lemma E per configuration (E1/E2, three-empty rule), giving E=0,
   E<=1 or E<=2 as tabulated; check every G, G_(>=1) and M.
D. Sec. 4 [RE-DERIVED]: pair-case intervals [max(-nu,nu-eps), min(nu,12-eps-nu)]; FORB for m=2,3 at eps=4,8; the four
   allow-sets Allow_1(3), Allow_1(5), Allow_2(5), Allow_2(7).
E. Sec. 5: 5.1 heavy single run, light sets and run count force >=2 empty runs in C4, C5, C9, C10, C11 where E=0.
   5.2 band subset sums with complete partition lists (C2, C3, C6, C7, C8): zero-weight run counts, maximal-part reductions.
   5.3 C1 and C12: profile reduction by band subset sums, then FORB (eps=4 or 8 on explicit m=2/m=3 sets) or the allow-set
   t-arguments (independent triple among five 2-runs; non-adjacent pairs among three or four 2-runs).
   5.4 pure case: profile (7,1^5) and the m=2 set with alpha=8.
Endpoints: completeness of every partition list (the text lists all partitions of the stated size; erratum E1 cleans one
list); every "zero run" count (empty, balanced, deviant-only runs); every adjacency claim on C_8; which configurations allow
the -1 letter and the deviant in the same run (C6, C7); the exact use of UH-A (only A>=9).

## 4. Requested verdict boundary

Judge Theorem R7, Proposition R7-PURE and the Corollary at the exact full NF antecedent relative to the listed accepted
inputs and the recorded UH-A input change. Report import-scope issues separately from mathematical gaps, and check the
[RE-DERIVED]/[NEW] labels. Nothing outside the p=7 cell is requested.
