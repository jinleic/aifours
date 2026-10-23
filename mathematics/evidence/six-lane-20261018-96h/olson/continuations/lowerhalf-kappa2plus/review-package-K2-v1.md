# K2 review package: lower-half terminal cell kappa_hat=2 excluded for every prime p>=11 (candidate), v1

Owner OlsonPP1Exclusion. Frozen after /bin/date 2026-10-19T23:01:20-0700. CANDIDATE_UNVERIFIED full written proof of the frozen primary target.
Parent owns both-family reviews and verdicts. No scientific computation, enumeration, script, assertion, solver, model CLI,
tests/build or Lean; all case work by hand. No novelty/priority/first/human-review claim, no other cell, no full ordered Olson.
Owner throttle: single deliverable; the slot parks after it.

## 1. Frozen texts (directory /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-kappa2plus/)
- proof-K2-v1.md, SHA256 04dc8c68cbe80044c040ea9d6a85acb12960094b0a06f7ce90106af6a8193272, lines 1-149 (14,473 bytes), read with erratum-1-proof-K2-v1.md,
  SHA256 db8c13ee19101b797f578cb8616deab2c208213f0a5a6f77af91faf8fa7ac812 (wording of the final sentence and of Sec. 0 only).
- K2-scope-v1.md, SHA256 37d39e81cad02fbe13f93d299d171c4e19b18a1be4f98b91b1704d137104593f, frozen 22:46:31 BEFORE derivation (exposure disclosed). Authority
  RUN/control/written-olson-lowerhalf-kappa2-transition-v1.json, SHA256 93f75a59338fcfbc327d3fe9ef71118dab8a5aeb30bf33415886cbf857c7136e.
Claim: THEOREM K2 - for every prime p>=11, no length-(4p-2) avoider over D_(2p) has an admissible NF with terminal k=p+1 and
kappa_hat=2 (full existential NF/word antecedent, arbitrary extra-pair placement, empty-run rule; no o_F/run/pair hypothesis).
Intermediate, kappa_hat=2 only: Lemma N (negative letters |A-|+nu0<=4, hence 2Pi0+3+nu0>=2p+6), Lemma F (the family
3<=m<=(p-3)/2 is full; theta_i defined for all runs; U'(Q)=sum_Q theta on F; sum_all theta=Pi0-nu0-2p), Lemma RIG (B*=R:
all rotations in one pair; tight theta data). Final step: single-arc (SR) contradictions for nu0=1,2; nu0=0 by cited CJ'''.

## 2. Manifest and imports
review-excerpts-K2-v1.json, SHA256 5d9dda935679d2e9780ce1c9d28477dd1cb162f9b348fdafd211937ca2fb5f52 (3764 bytes): JSON list {path,sha256,start,end}, whole-file SHA256, inclusive
LF ranges, absolute paths; 16 ranges from 16 files; raw 51363 bytes, LF-numbered 53444.
Package + manifest + numbered excerpts < 100,000 bytes. Accepted inputs at literal scope: K1 verdict (Theorem S of
proof-LOWER-v1.md relative to its inputs) with parent erratum 087ab3ae (m(P) convention; theta only via full pairs); through
Lemma IF: NF, GRX (if), S1(a), SC0, ZSTRUCT/FB/FB-E/Setting fact in (S'); CJ''' for the all-equal sub-case. Not used: Theorem P,
Lemma CR (conditional), unreviewed candidates, UH results.

## 3. Hostile-review focus
A. Sec. 1 frame at kappa=2: windows ([6,p+3] for P empty, [4,p+3] arcs, [0,p+3] for 3<=m<=(p-3)/2); Lemma IF data for t=0
   (W even, W<=2p-2, b<=p-4) and t=1 (n+=n-=1, s_1=1 by ZSTRUCT+FB; W<=2p-2; a_i<=p-2); #(b=1)>=(p+7)/2.
B. Lemma N: u+>=#(b=1)-o(P0); the refined count u+>=(p+B)/2>=B for a negative label B>=5 (t=0 and t=1 separately); the even
   prefix sizes x_j in {6,8} with weight <=7<=(p+3)/2; all zero-sums used are integer zero-sums of X at the empty pattern.
C. Lemma F: fullness of 3<=m<=(p-3)/2; |d|<=2p-2-B*<=p-5 and uniqueness of theta_i; the toggle connectivity (interval
   shrinking, triple reduction, gap transfers and rotation, with every intermediate set having m=3); f0=2f0 via
   {0,2,4},{1,6,8} (union m=4); complement identity via {0,2,4}.
D. Lemma RIG: top three of an alternating set lie in F; theta_(3)<=-1; the summed bound gives B*<=R; equality analysis.
E. Sec. 5: tau_i=theta_i-sigma({i}) (mod p); nu0=2 (all theta=-1, a +1 singleton, n=4); nu0=1 (theta=0 runs: even, nonempty by
   the empty-run rule, one free of the -1 letter, n=r_e+2); nu0=0 by CJ''' (Delta=-2, R=p+3>=4, 2kappa=4<=p-1).
Endpoints: p=11 (N=12, M=4, |S|=6, N-3=9, u+>=7), t=0/t=1, the location of z+ and z-.

## 4. Verdict boundary
Judge Theorem K2 and Lemmas N, F, RIG at kappa_hat=2 and the full antecedent. Not claimed: any other lower-half cell
(3<=kappa_hat<=(p-3)/2 remain open), kappa_hat=0, p<11, (H-ALT) or the lift inequality for kappa>=3, reflection rigidity, INV*,
o_F assembly or full ordered Olson. No earlier candidate is promoted by this packet.
