# LOWER review package: lower-half k=p+1 - kappa_hat=1 excluded, uniform structure, conditional rigidity, exact residual, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T22:10:16-0700. CANDIDATE_UNVERIFIED written proofs; outcome = LABELLED PARTIAL + EXACT
OBSTRUCTION of the frozen target. Parent owns both-family reviews and verdicts. No scientific computation/enumeration, script,
assertion, solver, model CLI, test/build or Lean; all case work by hand. No novelty/priority/first/human-review claim, no full
ordered-Olson claim. Unreviewed BOTTOM/RUH3/RUH2/KP3/KP4/R7 texts are not premises. Owner throttle: this is the single
deliverable of this slot; the slot parks after it.

## 1. Frozen texts (directory /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/)
- proof-LOWER-v1.md, SHA256 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d, lines 1-197 (19,418 bytes).
- residual-LOWER-v1.md, SHA256 cc623793d80a37654423dbc31ee13935877b6dbc8b44e6cc5b2be3b05e308ceb, read with erratum-1-residual-LOWER-v1.md, SHA256 ed049c066217ddde5950855639a63900057bc4d36288012b68b40e099bebd5d9.
- LOWER-scope-v1.md, SHA256 2e9784c14a8c467d52eb43e2787d22a0d947a2bee255dd731ccc5a65b1007959 (frozen 21:17:19 before derivation, exposure disclosed) and input addendum
  LOWER-scope-addendum-1.md, SHA256 0a68bf4204623d9cff7950175bda235fffefe120a3a203e478fc333fadd60442 (accepted inputs added before first frozen use; target unchanged).
- Authority RUN/control/written-olson-lowerhalf-transition-v1.json, SHA256 3ff7a017912c3c89c8022c7d667ef417927b8eafae9eaedb8f8141bd59717b03.
Claims (full existential-NF/word antecedent, arbitrary extra-pair placement, empty-run rule, p>=11, 1<=kappa_hat<=(p-3)/2):
- Theorem R: admissible k=p+1 range 0..p-1; no accepted whole-cell exclusion found in the lower half; B0S-CJ''' (cited) covers
  only the all-rotations-equal sub-case.
- Theorem S: (S1) sum floor(r_i/2)<=2kappa-1 (Theorem P); integer form at a T=0 arc (S1(a), SC0, ZSTRUCT/FB in (S') with
  (k',kappa')=(p-1,kappa-1)); signed sums fill [-nu(P),Pi(P)]; light side; lift framework for FULL patterns (Lemmas U/A/C/THETA).
- Theorem K1: the whole cell kappa_hat=1 is excluded for every prime p>=11.
- Lemma CR: conditional on (H-ALT), kappa<=(p-3)/4 and 2Pi0+3+nu0>2p, rotation rigidity with tight lift data.
- Residual: every 2<=kappa_hat<=(p-3)/2 (missing claims MC-L1 rigidity/(H-ALT), MC-L2 the tight pair case).

## 2. Manifest and imports
review-excerpts-LOWER-v1.json, SHA256 567f89b3d34d69b2aaec46916ace05d25f7531125b0ae3392d72145abf4c545f (4227 bytes): JSON list {path,sha256,start,end}, whole-file SHA256,
inclusive LF ranges, absolute paths; 18 ranges from 18 files; raw 60953 bytes, LF-numbered 63599.
Package + manifest + numbered excerpts < 100,000 bytes. Inputs at literal scope: NF, GRX (if), range record, Theorem P,
S1(a), SC0, ZSTRUCT + FB + FB-E + Setting fact in (S'), B0S-CJ''' (equal-rotation sub-case only).

## 3. Hostile-review focus
A. Sec. 2 (SR) from GRX with all blocks odd: n in [max(0,2kappa+2-2m),min(R,2p-2m)]; GRX theta_i = -tau_i and the target sign.
B. Sec. 4: the T=0 arc gives (ZP) at kappa-1 for X^(P0) (R<=2p-4), S1(a), SC0 at length >=p+1, and the (S') parameter match
   |Y| = 2p+2kappa'-k' = R, kappa'>=1 only when t>=1; oddness forces g=(1,gamma); FB balance gives n-<=n+.
C. Sec. 5: every element <= m1+1 (W<2L+r-2; s_j<=slack<=m1-3) and the greedy cover; the bijection J <-> U.
D. Sec. 7: Lemma U (one parity, p representatives), Lemma A (D in (0,4p)), Lemma C (class of Pi0-nu0 in [2Pi0+2,4p-2-2nu0]),
   Lemma THETA (|difference| <= 2p-2-B* < p).
E. Sec. 8 (K1): K1.1 (P0 letters all b=1, at most one), fullness K1.2 (arcs need both signs; ones abundance (p+2+w)/2 >= w),
   decomposition of G' into <=4 maximal arcs, inequality (K1), the W=p+1 equal-rotation case sent to CJ''', delta=1 parity.
F. Sec. 9: f constant and f=2f; sorting; Lemma C on S_ev, S_od; equality case. (H-ALT) is a hypothesis only.
Endpoints: p=11 (kappa=1 cell; residual kappa in {2,3,4}), shapes (a)/(b)/(c), delta in {0,1}.

## 4. Verdict boundary
Judge Theorems R, S, K1 and the conditional Lemma CR at the exact antecedent; confirm the residual does not overstate
(MC-L1/MC-L2 are route targets). Only the cell kappa_hat=1 is claimed excluded; no other lower-half cell, no rotation rigidity
without (H-ALT), and no UH/bottom/KP cell is promoted by this packet.
