# K3 review package: lower-half terminal cell kappa_hat=3 - every prime p>=13 excluded; p=11 partial + exact residual, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T23:53:25-0700. CANDIDATE_UNVERIFIED written proofs; outcome = LABELLED PARTIAL of the
frozen target: full exclusion for every prime p>=13, and for p=11 exclusion under (H11) with the remaining p=11 regime stated
exactly. Parent owns both-family reviews and verdicts. No scientific computation, enumeration, script, assertion, solver, model
CLI, tests/build or Lean; all case work by hand. No novelty/priority/first/human-review claim, no other cell, no full ordered
Olson. Owner throttle: single deliverable; the slot parks after it.

## 1. Frozen texts (directory /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-kappa3/)
- proof-K3-v1.md, SHA256 35ea47b03ad4a2c57c5b1430dfd642d524a935ae0c152ad220d5bb388da4ab30, lines 1-203 (19,815 bytes).
- K3-scope-v1.md, SHA256 5b04e5ac805c225f25820d52447752ebc6a8d6278dde9e459a24ca38c7c12676, frozen 23:29:01 BEFORE derivation (exposure disclosed, including the
  observation that the full-window family is empty at p=11 and only m=4 at p=13). Authority
  RUN/control/written-olson-lowerhalf-kappa3-transition-v1.json, SHA256 d7530d176e16a5b2a4555335487f1462bf5091068f7c005d43419de2acb22311.
Claims (full existential NF/word antecedent, arbitrary extra-pair placement, empty-run rule; no o_F/run/pair hypothesis):
- THEOREM K3: for every prime p>=13, no length-(4p-2) avoider over D_(2p) has an admissible NF with terminal k=p+1, kappa_hat=3.
- THEOREM K3-11 (partial): for p=11 the same holds for avoiders whose NF, in the integer frame of Sec. 1 (any admissible choice
  of the T=0 arc and light side), satisfies (H11): some run holds letters of both label signs, or at most three runs hold no
  positive-label letter.
- Residual (NOT proved, Sec. 7): p=11 with (H11) failing (no two-signed run and at least four runs without positive letters).
Intermediate, kappa_hat=3 only: Lemma N3 (negative letters, x(A-)<=6, lift inequality 2Pi0+3+nu0>=2p+8), Lemma FULL (every
m=4 pattern full for p>=13; at p=11 exactly the two-signed ones), Lemma F3 (lift framework on all m=4 patterns), Lemma RIG3
(B*=R: all rotations in one pair; theta>=-1; alternating-set excess 3-nu0), final single/two/three-run (SR) contradictions.

## 2. Manifest and imports
review-excerpts-K3-v1.json, SHA256 f871821b2a073cf35e2993611c6eae1cfa60bf0c33d2fa54d0dd5a7de809a81e (3724 bytes): JSON list {path,sha256,start,end}, whole-file SHA256, inclusive
LF ranges, absolute paths; 16 ranges from 16 files; raw 54604 bytes, LF-numbered 56800.
Package + manifest + numbered excerpts < 100,000 bytes. Accepted inputs at literal scope: K1 verdict (PL Theorem S relative to
its inputs: SR, IF, D, SS, LT, U, A, C) with LOWER parent erratum 087ab3ae (m(P) convention, theta only via full pairs);
through Lemma IF: NF, GRX (if), S1(a) at kappa'=2, SC0, ZSTRUCT/FB/FB-E in (S') with (k',kappa')=(p-1,2); CJ''' only for the
all-equal sub-case. K2 is cited only as method context. Not used: Theorem P, Lemma CR, unreviewed candidates, UH results.

## 3. Hostile-review focus
A. Sec. 1: windows at kappa=3 (m=4 window [0,R] iff p>=13; [0,14] at p=11); IF data t in {0,1,2} with balance forcing the
   extra labels; W parity bounds; #1>=(p+11)/2; |b|<=p-4; u+>=(p+5)/2.
B. Lemma N3: the B>=7 counts per t; the weight-multiset analysis (no sub-sum 8 forces {6,4} or {6,6}); the refined count
   u+>=10 for {-5,-5}; sizes 8, 10, 12 inside [8,p+5].
C. Lemma FULL(b): minimal-representation argument at p=11 (>=7 unit letters in J, labels <=7, parity forces |J|=16);
   (c),(d): single-signed iff letters(Q) or letters(Q^c) equals A-; (H11) excludes both for m=4.
D. Lemma F3: theta via Q_i={i+1,i+3,i+5,i+7}; |d|<=p-7; gap-transfer connectivity of independent quadruples (target
   (2,2,2,N-10), shift by advancing v4,v3,v2,v1); f0=0 via {0,3,6,9},{1,4,7,10} (union m=4); total via {0,2,4,6}.
E. Lemma RIG3: top four of each alternating set lie in F4; B*<=R and the equality analysis (|S|>=6).
F. Sec. 6: no empty runs for nu0>=1; unit runs count p-9+nu0; nu0 in {2,3} (n=4); nu0=1 sub-cases (theta=1 run with s_e>=1:
   n=s_e+3; e={-1}: m=3, n=2; four theta=0 runs: n=4); nu0=0 via CJ''' (Delta=-3, R=p+5>=8, 2kappa=6<=p-1).
Endpoints: p=13 (m=4 window exactly [0,18]); p=11 (N=12, |S|=6, u+>=8, labels<=7, unit-run counts).

## 4. Verdict boundary
Judge Theorem K3 (p>=13), Theorem K3-11 (p=11 under (H11)) and Lemmas N3, FULL, F3, RIG3 at kappa_hat=3 and the full
antecedent. The p=11 residual and missing claim are route statements, not claims. Not claimed: the whole p=11 cell, other cells,
reflection rigidity, INV*, o_F assembly, full ordered Olson. No earlier candidate is promoted by this packet.
