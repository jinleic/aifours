# USK review package: lower-half terminal cells 3 <= kappa_hat <= floor((p-1)/4) excluded uniformly in p, v1

Owner OlsonUniformSmallKappa. Frozen after /bin/date 2026-10-20T00:52:02-0700. CANDIDATE_UNVERIFIED written proof. Outcome: the FULL frozen
target is proved, with no obstruction; LABELLED PARTIAL of ordered Olson. The parent owns both-family reviews and verdicts.
No scientific computation, enumeration, script, assertion, solver, model CLI, test/build or Lean; all case work by hand. The
only machine steps were metadata: /bin/date, whole-file SHA256, line counts and byte counts of the listed ranges (the
metadata helper included a line-range bounds check). No novelty/priority/first/human-review claim, no other cell, no full
ordered Olson. Owner throttle: single deliverable; the slot parks after it.

## 1. Frozen texts (directory /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-small-kappa/)
- proof-USK-v1.md, SHA256 a88c65e201a0446212d3eceb6b1d6316021d5542aa9d0ddcfa0f5d93e27f6623, lines 1-296 (29,055 bytes).
- USK-scope-v1.md, SHA256 fabc84fbe78dc978cb7164da1ecd34ed62925f3c2c178984b1669dac1eeec17e, frozen 2026-10-20T00:25:01-0700 BEFORE derivation
  (pre-freeze exposure disclosed). Authority RUN/control/written-olson-uniform-small-kappa-transition-v1.json, SHA256
  3ea785068797a0e0939d9c9130cee764a2774219717d8f7901cd7147919cb4ca.
- USK-scope-addendum-1.md, SHA256 2dca26393f971953a4b6cb892430af185b0676f0960f0148b5d698dc0ba4d550 (00:40:01): records Main's IRC (K3 accepted as
  context; input hygiene: no S1(a), no Setting fact, explicit general-kappa prerequisites). Written before the proof text.
- checkpoints/checkpoint-001.md, SHA256 83f8a8d82370b27248c9db7716800cdcd8d6accc238b36607b8c544394ec70c7 (00:39:24); a closing checkpoint-002.md
  follows this package.
Claim (full existential NF/word antecedent: SOME admissible NF, arbitrary extra-pair placement, genuine empty-run rule; no o_F,
nonempty-run, rotation-pair or reflection-rigidity hypothesis):
- THEOREM USK: for every prime p and every integer kappa with 3 <= kappa <= floor((p-1)/4), no length-(4p-2) word over D_(2p)
  avoiding an identity 2p-subword in increasing original index order has an admissible NF with terminal k=p+1 and
  kappa_hat=kappa.
Intermediate, this range only: Lemma W (windows), IF* (frame; direct zero-sum bound), D* (density), N (negative letters:
(a) label count, (b) u+ count, (c) |A-|+nu0 <= 2kappa via integer zero-sums at the empty pattern; lift margin >= 2kappa+2),
F (lift framework on m=kappa+1), RIG (B*=R; theta >= -1; excess kappa-nu0 per alternating set), Sec. 5 (one m=kappa selection).

## 2. Manifest and imports
review-excerpts-USK-v1.json, SHA256 8f44758b3effcf56aec26b73e1cc10a17e505cfcd253011a9641dfce9021f83f (4202 bytes): JSON list {path,sha256,start,end}, whole-file
SHA256, inclusive LF ranges, absolute paths; 18 ranges from 18 files; every hash re-checked equal at freeze; raw 66,646
bytes, LF-numbered about 70,717 bytes. Package + manifest + numbered excerpts stay below 100,000 bytes (Sec. 6).
Accepted inputs at literal scope: K1 verdict (PL Theorem S relative to its inputs) with the LOWER parent erratum (m(P)
convention; theta only via full pairs); PL Secs. 2, 4-7: (SR), IF(a), normalisation, the covering step of D, SS, LT, U, A, C;
through IF*: NF, GRX (if direction), SC0, and ZSTRUCT/FB in (S') at (k',kappa')=(p-1,kappa-1) for t>=1, with the (S1)
definition only. NOT used: S1(a), the Setting fact, FB-E, Theorem P, B0S-CJ''' (its all-equal sub-case nu0=0 is covered by
Sec. 5), PL Lemma THETA (replaced by (F2)), PL Secs. 8-9, K2/K3 lemmas, P11R and other unreviewed candidates. Context only:
K2 verdict, K3 verdict and erratum; proof-K2-v1.md and proof-K3-v1.md were read after the freeze, and their methods are
re-derived for general kappa.

## 3. Expected checks of the transition -> proof location
- Windows: Lemma W (m=kappa+1 window is [0,R] iff p >= 4kappa+1; m=kappa window [2,R]); Sec. 6.
- Negative-letter lemma: Lemma N(c) (window [2kappa+2,R] at the empty pattern) gives |A-|+nu0 <= 2kappa and hence
  2Pi0+3+nu0 > 2p; Lemma N(a) proves the same inequality independently by a label count.
- Lift framework: (F1) every m=kappa+1 pattern is full; (F2) explicit full pairs Q_i={i+1,...,i+2kappa+1}, Q_i u {i}; (F3)
  toggle connectivity by gap moves; (F4) disjoint independent sets {0,3,...,3kappa}, {1,4,...,3kappa+1} with union in F fix
  the additive constant; (F5) complement total via {0,2,...,2kappa}. All valid for N=p+1 >= 4kappa+2 (Sec. 6 at p=4kappa+1).
- Rigidity: Lemma RIG (top kappa+1 of each alternating set; B*=R; tight theta data).
- Final cases: Sec. 5, case (i) (f >= 1, contains every nu0 >= 1) and case (ii) (f=0, nu0=0, empty-run rule); per-nu0 line;
  endpoint p=4kappa+1 and (kappa,p)=(3,13) in Sec. 6. Exact first failing lemma: none in the target range.

## 4. Hostile-review focus
A. IF*(b),(d),(f): zero-sum lengths are even and <= R <= 2p-2, W_1=[2kappa,R], so 2t <= 2kappa-2; the (S') hypotheses at
   (p-1,kappa-1); ZSTRUCT (s_j <= 2t-1, n- >= 1) and FB (balance, W+n+ <= 2p-1); E <= p-2kappa+n-; m1 >= (p+kappa+3)/2.
B. D*: s_j <= 2kappa-3 <= m1+1 (3kappa <= p+11) and a_max <= m1+1 (E <= L+r-2) without the Setting fact; B*-R = E+n+-n-.
C. N(a): nu0 <= q1+3E/2+n+ and the margin 2kappa+2+E/2. N(b): u+ >= (p-2+6kappa-3n-+sum(B_k-3))/2-q1. N(c): (c1) single
   letters B >= 2kappa+1 (size B+1 <= p-kappa+1); (c2) k1 <= kappa; (c3) j* >= k1+1, X_(j*) <= 4kappa <= R,
   w(S) <= 2kappa+B-k1, and the two type cases.
D. F: fullness from SS parity at window [0,R]; (F2) |d| <= p-1-2kappa and uniqueness mod 2p; (F3) moves (a)-(d), target gaps
   (1,...,1,N-2kappa-1); (F4) wrap gaps N-3kappa-1 and separator N-3kappa-2 >= kappa; (F5) intervals of Q0^c.
E. RIG: J* in F; (R1); adding over S_ev, S_od with (F5); equality analysis needs M=(p+1)/2 >= kappa+2.
F. Sec. 5: (T) from theta_i = h_i (mod p) and the parity from (F2); Theta(P(O')) = -nu0 because P(O') contains the excess
   support Z_S; T(P) = -nu(P) with nu(P) even; KEY uses all nu(P) letters of value -1, n in [2,R]; case (i): two choices
   with different letter sets (nonempty o by (E1)); case (ii): nu0=0 and theta=0 runs nonempty by the empty-run rule (E2).
G. Sec. 6: endpoint (W_(kappa+1) reaches R exactly, W_(kappa+2) stops at R-2) and the explicit (3,13) sets.

## 5. Verdict boundary
Judge Theorem USK and Lemmas W, IF*, D*, N, F, RIG at 3 <= kappa <= floor((p-1)/4) under the full antecedent. Not claimed:
kappa_hat <= 2 (accepted separately), kappa_hat > (p-1)/4 (including p=11 with kappa_hat=3), kappa_hat=0, p=7, reflection
rigidity, INV*, o_F assembly, full ordered Olson. Sec. 7 route remarks (R1)-(R3) and the boundary remark are not claims.
No earlier candidate is promoted by this packet.

## 6. Size
Package 6,956 bytes + manifest 4202 bytes + LF-numbered excerpts about 70,717 bytes = about 81,875 bytes (<= 100,000).
