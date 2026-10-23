# P11R review package: K3 p=11 residual ((H11) failing) - near-rigidity B* in {16,18} + exact obstruction, v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-20T00:20:48-0700. CANDIDATE_UNVERIFIED written proofs; outcome = LABELLED PARTIAL of the
frozen target plus EXACT OBSTRUCTION: the residual branch is NOT shown empty. Parent owns both-family reviews and verdicts. No
scientific computation, enumeration, script, assertion, solver, model CLI, tests/build or Lean; all case work by hand. No
novelty/priority/first/human-review claim; no other prime, kappa or cell; no full ordered Olson. Owner throttle: single
deliverable; the slot parks after it.

## 1. Frozen texts (directory /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/kappa3-p11-residual/)
- proof-P11R-v1.md, SHA256 6ee3df0985f02d01e6cde08c88944791b91dbc76e389e20f16e6b9accec87ac4, lines 1-175 (16,345 bytes), frozen 00:13:30.
- erratum-1-proof-P11R-v1.md, SHA256 b2fe448f853ee881ed002739217f6e4227081a546960da986e8bb4ac62e1895a, lines 1-30 (1,766 bytes), 00:14:31:
  two Sec. 8 route remarks only (E1: the K3 Sec. 6 final cases are a route description to be re-derived, not a premise; E2: the
  F1 example label multiset is itself excluded by CJ'''). No claim changes. Read the proof with this erratum.
- P11R-scope-v1.md, SHA256 14701fd9860d6b4288c4373f683cca6883273c7cd433322a5af81f0b61c9e00c, frozen 23:55:39 BEFORE derivation
  (exposure disclosed: K3 candidate, unfrozen ideas (i)-(v)). Authority RUN/control/written-olson-kappa3-p11-residual-transition-v1.json,
  SHA256 2aff97fc4770e0898df336669a50e58f1aa45c306a7f55e61b9ce45bdf252ed4.
- checkpoints/checkpoint-001.md 9652bd5d356e4b7ae9c8325efc6fcdc5081eb79e366aa3fd92a0c5980114892e (00:03:06),
  checkpoints/checkpoint-002.md 55e7d645f031df21c245b10960a4f033af0f6a994fdcf24d853775e0f58501c2 (00:09:21).
Claims (p=11, k=12, kappa_hat=3, full existential NF/word antecedent, arbitrary extra-pair placement, empty-run rule; no o_F/run/
pair hypothesis; residual = (H11) failing in the integer frame):
- THEOREM P11R (a)-(f): frame data; Lemma ARC (light arc P0 has <=5 letters, light side unique); run classes (k_P>=3 positive
  runs, <=3 negative runs, 1<=E<=6 empty runs, no mixed run); Lemma FULL11 (m in {3,4}: full iff two-signed; single-signed iff
  letters(Q) or letters(Q^c) equals A-; P-split patterns are full); THEOREM NR (B* in {16,18}; B*=16: all letters rho_(+-gamma),
  nu0 in {1,2,3}; B*=18: one rho_(3gamma), others rho_(+-gamma), nu0<=1); Lemma BOTH (top-3 and top-4 of an alternating set
  both single-signed only in configurations (alpha), (beta)).
- Lemma N11 (negative letters at p=11: A- in a list of seven multisets, nu0<=5, 2Pi0+3+nu0>=30) and Lemma PAIR (disjoint P1, P2
  with m(P1)=m(P2)=m(P1 u P2)=3, all P-split).
- EXACT OBSTRUCTION (Sec. 8, NOT proved): the near-rigid residual; missing claim = a toggle-connected family of full m in {3,4}
  patterns containing PAIR, a complementary pair and, for each alternating set, its theta-top-3 or top-4 set; failed routes
  F1-F5 kept.

## 2. Manifest and imports
review-excerpts-P11R-v1.json, SHA256 e81f1b9763b6f7e8529d9f854e599d6d0a1c90a497f23017c50e7deae76af281 (4,483 bytes): JSON list {path,sha256,start,end}, whole-file SHA256, inclusive
LF ranges, absolute paths; 19 ranges from 18 files; raw 56,954 bytes, LF-numbered ("N: " prefix) 59,343. Package + manifest +
numbered excerpts < 75,000 bytes. Accepted inputs at literal scope: K1 verdict (PL = proof-LOWER-v1.md Theorem S relative to its
inputs: SR, (S1) via accepted Theorem P, IF, D, SS, LT, U, A, C) with LOWER parent erratum 087ab3ae (m(P) convention); through
Lemma IF: NF, GRX (if direction), S1(a) at kappa'=2, SC0, ZSTRUCT/FB/FB-E in (S') with (k',kappa')=(10,2); Theorem P (accepted
import, K0*-RED verdict line 7) only through (S1); CJ''' only for B*=16, nu0=0 (all letters equal). Not used in proved claims:
Lemma THETA (route text only), Lemma CR, K2, Cauchy-Davenport, RS(a)/RS(b). proof-K3-v1.md lines 10-22 and 170-187 are
UNTRUSTED CONTEXT (where the residual comes from), not premises; K3 and its review freeze 93b25a2f... remain queued separately.

## 3. Hostile-review focus
A. Sec. 1 at p=11: windows; t in {0,1,2} with balance forcing the extra labels ({+1,-1}; {+1,+1,-1,-1} or {+1,+1,+1,-3});
   W parity bounds 20/20/18; #1>=11; |b|<=7; exactly one light side; u+>=8.
B. Lemma N11: c=-7 forces t>=1, all other a-labels 1, u+>=10, zero-sum of size 8; weights {2,4,6} with no sub-sum 8 force a 6,
   no 2, at most one 4; {-5,-3} gives size 10; two -5's impossible (W-L<=6, or <=4 at t=0).
C. Lemma ARC: P0 letters = (b>0, all in A-, <=3) + (extra negative labels, <=2).
D. Sec. 4: (c3) k_P>=3 from 13<=sum_P r_i<=k_P+10 via (S1); (c4) E<=6 from sum(r_i-1)=4+E<=2*5.
E. Lemma FULL11: m=3 window [2,16] means fullness iff a NONEMPTY zero-sum exists; m=4 window [0,14]: minimal representation, >=7
   unit letters in J when |J|>=15, labels <=7, parity forces |J|=16; single-signed patterns not full (v=+-B* needs 16 letters).
F. Lemma PAIR: the three choices of (g1,g2); blocks of length >=2, pairwise non-adjacent (wrap through run 0); m=3 for P1, P2 and
   P1 u P2; each P-split.
G. Theorem NR: Lemma U interval [B*-nu0-21,-1-nu0] at p=11; B*=20 contradicts Lemma A on PAIR; B*=18 gives nu0<=1, A- in {},{-1},
   the |c|=3 letter positive; B*=16 gives |c|=1 throughout, nu0<=3, nu0=0 excluded by CJ'''.
H. Lemma BOTH: the four type combinations; (beta) counting: sum_P r=13 with odd lengths by (S1) equality, other runs of length
   <=1, |A-|=3 forces {-1,-1,-1}, B*=16 by Theorem NR.
I. Sec. 8: exactness of the residual statement; accuracy of F1-F5. Known wording points (no claim affected): the F1 illustration
   uses tau_e!=0 for an empty run (empty-run rule) without saying so; F5 means Theorem P's hypothesis F+sum floor(r_i/2)>=3p-1=32
   cannot hold (26+5=31), so Theorem P gives nothing beyond (S1); Sec. 9 is a paragraph-form interface table.

## 4. Verdict boundary
Judge Theorem P11R (a)-(f), Lemmas N11, ARC, FULL11, PAIR, BOTH and Theorem NR at p=11, kappa_hat=3, in the residual ((H11)
failing) under the full antecedent. Sec. 8 (residual, missing claim, failed routes) is obstruction/route text, not claims. Not
claimed: emptiness of the residual, the whole p=11 kappa_hat=3 cell, Theorem K3/K3-11 (queued separately), other cells or primes,
reflection rigidity, full ordered Olson. No earlier candidate is promoted by this packet.
