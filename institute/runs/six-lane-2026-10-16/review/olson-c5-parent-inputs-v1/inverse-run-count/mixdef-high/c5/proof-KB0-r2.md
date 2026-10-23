# Theorem KB0 (version r2): no word of W(p, (p+5)/3) is an avoider (every prime p = 1 (mod 6), p >= 13)

Version r2, written 2026-10-17T14:30:11-0700 in c5/ (task OlsonRunCount5): answers the MINOR finding of the parent's Codex review of
cycle 4 (institute/runs/six-lane-2026-10-16/review/olson-c4-codex-review-v1.note.md line 14: proof-KB0-r1.md:15 cited
the unfrozen, superseded c4/proof-NOBCplus-r2.md).  The ONLY change: the Scope paragraph now cites the frozen
c4/proof-NOBCplus-r3.md (reviewed ACCEPT; its Lemma D is the statement used here).  Everything else is c4/proof-KB0-r1.md
(sha256 5fb878e424ca3b9ed19fb21e9c41fb6aa4f16a292b168e29fd9ff95780f3fb5e) verbatim, including its own version note below;
paths "c3/...", "c4/..." are relative to mixdef-high/, and the receipts and code named in Sec. 3 (out/..., *.py, *.cpp)
are the unchanged cycle-4 files in c4/ and c4/out/.  The review verdict on the mathematics (ACCEPT-WITH-FIXES, the fix
being this citation) is unaffected.

Version r1, written 2026-10-17T13:32:27-0700: replaces the UNFROZEN draft c4/proof-KB0.md, whose Sec. 3 misquoted two mutation-control
counts of out/kb0_replay.txt (MUT = 1: 547 instead of 546; MUT = 3: 266 instead of 240).  The mathematics (Secs. 0-2)
is unchanged; proof-KB0.md is kept (no deletion) and never cited.

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).
Written in c4/ after host clock 2026-10-17T13:31:44-0700 (freeze time and SHA-256 in c4/out/freeze.txt).  Task OlsonRunCount4.
Origin: the parent's Codex review of cycle 3 (institute/runs/six-lane-2026-10-16/review/olson-c3-codex-review-v1.note.md,
lines 25-32) sketched this argument for W(19, 8); here it is written for the whole family and every step is proved.
Imported (not re-proved): Lemma H with the 07:39 correction (../../../inverse-parity/proof-PAR-K0.md Sec. 1), the Claim
in Lemma BC (same file, Sec. 2), Lemma L (c3/proof-NOLP-r2.md Sec. 1), the family W(p, kB), formulas (0.1), (0.2) and
the c-coordinate criterion (2.1) of c3/proof-WALL.md (all reviewed ACCEPT or ACCEPT-WITH-FIXES).
Scope: the single value kB = K := (p + 5)/3 for the primes p = 1 (mod 6), p >= 13 (p = 13, 19, 31, 37, 43, 61, ...).  By
c4/proof-NOBCplus-r3.md Lemma D these are exactly the values beyond Theorem W-ALL (3kB >= p + 5) at which aligned
pairs are certified; they contain DOB(p) - DOB*(p).  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), INV or ordered
Olson for D_{2p}.

## 0. Parameters and lambda values

p = 3K - 5 with K even (p = 1 (mod 6) iff K is even), K >= 6, K <= p - 4.  Runs: the anti run 0 (d_0 = -1) and the
aligned runs 1, ..., n (d_t = 1), n = p + K, k = n + 1 = 4K - 4; B = 1, kappa = K + 1, kappa - B = K, D = p + K - 1 = 4K - 6.
Every word of W(p, K) is all-odd with A = p + K <= 2p - 1 and B = 1 <= kappa, so Lemma H and Lemma L apply.
For a proper pattern Q with y := D_Q and m := m(Q) blocks (c3/proof-WALL.md (0.1), (0.2)):
   lambda(Q) = lam(y, m) := min(p - m + 1, y + m - K, floor((y + 1)/2) + 1),
   lambda(Q^c) = lamc(y, m) := min(p - m + 1, p - 1 - y + m, floor((p + K - y)/2) + 1),   p + K = 4K - 5.
Singletons: lambda({t}) = 2 - K (t aligned), lambda({0}) = -K;
   Lambda1 := lambda({t}^c) = lamc(1, 1) = min(p, p - 1, 2K - 2) = 2K - 2,   Lambda0 := lambda({0}^c) = lamc(-1, 1) = 2K - 1
(p - 1 = 3K - 6 >= 2K - 2 as K >= 4).  Certification step (Lemma L): Q = Q' u {t} (t notin Q', Q' certified) is certified if
   (A) lambda(Q') + lambda({t}) + lambda(Q^c) >= 1   and   (B) lambda(Q) + lambda(Q'^c) + lambda({t}^c) >= p + 1.
Below, when a lambda is a minimum of terms, a lower bound for a sum of lambdas is obtained by bounding every sum of one
term from each minimum.

## 1. Lemma CW-K (certification)

**Lemma CW-K.**  In every word of W(p, K):
(a) every aligned pair is certified;
(b) every anti triple {0, s, t} (s, t aligned) is certified;
(c) every proper pattern Q with 3 <= |Q| <= K + 1 is certified;
(d) P := {0, 2, 4} and P^c = {1, 3, 5, 6, ..., n} are certified, and lambda(P) + lambda(P^c) = K + 2.
(The anti pairs {0, s} are NOT certified (Lemma NOLIFT(a), 3K = p + 5) and are never used below.)

Proof of (a).  Q' = {s}, t aligned, m := m({s, t}) in {1, 2}.  lambda({s, t}^c) = lamc(2, m) = min(p - m + 1, p - 3 + m,
floor((4K - 7)/2) + 1) = 2K - 3 (as p - 2 = 3K - 7 >= 2K - 3).  (A): 2(2 - K) + 2K - 3 = 1.  (B): lam(2, m) + 2 Lambda1
>= (3 - K) + 4K - 4 = 3K - 1 = p + 4.
Proof of (b).  Q' = {s, t} is certified by (a); adjoin t* = 0.  m' := m(Q') in {1, 2}, m := m(Q) in {1, 2, 3}, y(Q') = 2,
y(Q) = 1.  lamc(1, m) = min(p - m + 1, p - 2 + m, floor((4K - 6)/2) + 1) = 2K - 2 (as p - 2 = 3K - 7 >= 2K - 2 for K >= 5),
lam(2, m') >= 3 - K, lamc(2, m') = 2K - 3 (as in (a)), lam(1, m) = min(p - m + 1, 1 + m - K, 2) = 1 + m - K.
(A): lam(2, m') - K + 2K - 2 >= (3 - K) + K - 2 = 1.  (B): (1 + m - K) + (2K - 3) + Lambda0 = 3K - 3 + m = p + 2 + m >= p + 3.
Proof of (c).  Induction on s := |Q|, 3 <= s <= K + 1.  Anti triples are (b).  Otherwise let Q have j aligned runs,
e = [0 in Q], y = j - e, m blocks.  Then 2 <= y <= K + 1 (e = 0: y = s >= 3; e = 1: s >= 4 and y = s - 2 >= 2) and
m <= s <= K + 1.  Choose t as in Lemma CW of c3/proof-WALL.md: if some block of Q has >= 2 runs, t is an aligned end run
of such a block (its two ends are distinct and at most one is the anti run), and m' := m(Q - t) = m; otherwise every block
is a single run and t is an aligned one, m' = m - 1 (>= 2 since then m = s >= 3).  Q' := Q - t has s - 1 >= 2 runs and is
not an anti pair (if s - 1 = 2 then e = 0, because e = 1 and s = 3 is an anti triple), so Q' is certified by (a), (b) or the
induction hypothesis.  y(Q') = y - 1 >= 1, 1 <= m' <= s - 1 <= K, m' >= m - 1.
(A) reads lam(y - 1, m') + lamc(y, m) >= K - 1.  Terms of lam(y - 1, m'): U1 = p - m' + 1 >= p - K + 1, U2 = y - 1 + m' - K,
U3 = floor(y/2) + 1 >= 2.  Terms of lamc(y, m): T1 = p - m + 1 >= p - K, T2 = p - 1 - y + m >= p - K - 1 = 2K - 6,
T3 = floor((4K - 5 - y)/2) + 1 >= floor((p - 1)/2) + 1 = (3K - 4)/2 (y <= K + 1).
* U1 + Tb >= (2K - 4) + min(2K - 6, (3K - 4)/2) >= K - 1;   U3 + Tb >= 2 + min(2K - 6, (3K - 4)/2) >= K - 1 (K >= 3).
* U2 + T1 = p + y - K + (m' - m) >= p + y - K - 1 >= p + 1 - K = 2K - 4 >= K - 1.
* U2 + T2 = p - 2 - K + m + m' >= p - K = 2K - 5 >= K - 1 (K >= 4).
* U2 + T3 >= y + m' - K + (4K - 6 - y)/2 = K - 3 + y/2 + m' >= K - 1, as y >= 2 and m' >= 1.
(B) reads lam(y, m) + lamc(y - 1, m') >= p + 1 - Lambda1 = K - 2.  Terms of lam(y, m): V1 = p - m + 1 >= p - K, V2 = y + m - K,
V3 = floor((y + 1)/2) + 1 >= 2.  Terms of lamc(y - 1, m'): T1' = p - m' + 1 >= p - K + 1, T2' = p - y + m' >= p - K,
T3' = floor((4K - 4 - y)/2) + 1 >= (3K - 4)/2.
* V1 + Tb' >= (p - K) + min(p - K, (3K - 4)/2) >= K - 2;   V3 + Tb' >= 2 + min(p - K, (3K - 4)/2) >= K - 2.
* V2 + T1' = p + 1 + y - K + (m - m') >= p + y - K >= K - 2;   V2 + T2' = p - K + m + m' >= K - 2.
* V2 + T3' >= y + m - K + (4K - 5 - y)/2 + 1 = K - 3/2 + y/2 + m >= K - 2.
Proof of (d).  P = {0, 2, 4} is an anti triple (y = 1, m = 3), certified by (b).  For P^c use the chain Q_1 = {1}, Q_2 = {1, 3},
Q_3 = {1, 3, 5} and Q_i = {1, 3} u {5, 6, ..., i + 2} for 4 <= i <= n - 2, so that Q_{n-2} = {1, 3, 5, 6, ..., n} = P^c.  Q_2 is an
aligned pair ((a)); Q_3 has 3 runs ((c)).  For 4 <= i <= n - 2 = 4K - 7, Q_i = Q_{i-1} u {i + 2} with every Q_i all-aligned,
y(Q_i) = i and three blocks {1}, {3}, {5, ..., i + 2} (so m = m' = 3); the new run i + 2 is aligned (lambda = 2 - K,
lambda(complement) = Lambda1).
(A) reads lam(i - 1, 3) + lamc(i, 3) >= K - 1 with lam(i - 1, 3) = min(p - 2, i + 2 - K, floor(i/2) + 1) and
lamc(i, 3) = min(p - 2, p + 2 - i, floor((4K - 5 - i)/2) + 1); the nine sums are: (p - 2) + (p - 2); (p - 2) + (p + 2 - i) >=
2p - 4K + 7 = 2K - 3; (p - 2) + floor((4K - 5 - i)/2) + 1 >= p (as i <= 4K - 7); (i + 2 - K) + (p - 2) = p + i - K;
(i + 2 - K) + (p + 2 - i) = p + 4 - K; (i + 2 - K) + floor((4K - 5 - i)/2) + 1 >= K + i/2; floor(i/2) + 1 + p - 2;
floor(i/2) + 1 + p + 2 - i = p + 3 - ceil(i/2) >= p + 3 - (2K - 3) = K + 1; floor(i/2) + floor((4K - 5 - i)/2) + 2 >=
(4K - 7)/2 + 1; each is >= K - 1.
(B) reads lam(i, 3) + lamc(i - 1, 3) >= K - 2 with lam(i, 3) = min(p - 2, i + 3 - K, floor((i + 1)/2) + 1) and
lamc(i - 1, 3) = min(p - 2, p + 3 - i, floor((4K - 4 - i)/2) + 1); the nine sums are: 2p - 4; (p - 2) + (p + 3 - i) >= 2K - 2;
(p - 2) + floor((4K - 4 - i)/2) + 1 >= p; (i + 3 - K) + (p - 2); p + 6 - K; (i + 3 - K) + floor((4K - 4 - i)/2) + 1 >= K + i/2 + 3/2;
floor((i + 1)/2) + 1 + p - 2; floor((i + 1)/2) + 1 + p + 3 - i = p + 4 - ceil((i - 1)/2) >= p + 4 - (2K - 4) = K + 3;
floor((i + 1)/2) + floor((4K - 4 - i)/2) + 2 >= (4K - 3)/2 + 1; each is >= K - 2.
Finally lambda(P) = lam(1, 3) = min(p - 2, 4 - K, 2) = 4 - K and lambda(P^c) = lamc(1, 3) = min(p - 2, p + 1, 2K - 2) = 2K - 2,
sum K + 2.  []

**Corollary (pin).**  If w in W(p, K) avoids and x_t are integer lifts of its half-sums u_t with x_t in
[lambda({t}), p - lambda({t}^c)], then X_Q := sum_{t in Q} x_t lies in [lambda(Q), p - lambda(Q^c)] for every Q certified in
Lemma CW-K, and X_[k] = p.
Proof.  Lemma L gives the first claim.  X_[k] = X_P + X_{P^c} lies in [K + 2, 2p - K - 2], inside [1, 2p - 1], and is = 0 (mod p).  []

## 2. Theorem KB0

**Theorem KB0.**  Let p be a prime with p = 1 (mod 6) and p >= 13, and K = (p + 5)/3.  No word of W(p, K) is an avoider:
every inherited all-odd RGR word of length 4p - 2 with p + 1 + K single-letter rotation runs, exactly one of them rho_{-1},
has an identity 2p-subword.

Proof.  Suppose w avoids; take x as in the Corollary, so X_[k] = p and X_Q >= lambda(Q) for every certified Q.  Put
c_t := d_t - x_t, c(Q) := sum_{t in Q} c_t = D_Q - X_Q.  Then sum_t c_t = D - p = K - 1; the singleton lower bounds give
c_t <= K - 1 for every t (aligned: x_t >= 2 - K; anti: x_0 >= -K).  By c3/proof-WALL.md (2.1) (pure algebra from (0.1)),
for every proper Q:
   X_Q >= lambda(Q)  <=>  c(Q) <= gamma(Q) := max(D_Q + m(Q) - p - 1, K - m(Q), ceil((D_Q - 1)/2) - 1).
Let Z_al := {aligned t : c_t >= 1}, e_Z := [c_0 >= 0], Z := Z_al u ({0} if e_Z = 1).
Step 1.  If |Z_al| >= K, let Q consist of K runs of Z_al.  Q is certified (Lemma CW-K (a)/(c): all aligned, K >= 6 runs), c(Q) >= K,
D_Q = K, 1 <= m(Q) <= K, so gamma(Q) <= max(2K - p - 1, K - 1, ceil((K - 1)/2) - 1) = K - 1 (2K - p - 1 = 4 - K) < c(Q).
Contradiction.
Step 2.  So |Z_al| <= K - 1 and |Z| <= K.  Outside Z every aligned run has c_t <= 0 and the anti run (if outside) has
c_0 <= -1; hence c(Z) = (K - 1) - c([k] - Z) >= K - e_Z.  Z is nonempty (c(empty) = 0 < K - e_Z) and proper.
Case 2a: Z = {0, a} is an anti pair (uncertified).  Then c(Z) >= K - 1 and c(Z) <= 2(K - 1).  The n - 1 aligned runs outside Z
have c_t <= 0 and sum (K - 1) - c(Z) >= -(K - 1), so at least n - 1 - (K - 1) = p of them have c_t = 0.  At most four runs
are adjacent to 0 or a; pick s outside Z with c_s = 0 adjacent to neither (p >= 13).  Q := {0, a, s} is an anti triple, certified
by Lemma CW-K (b); D_Q = 1, m(Q) = m(Z) + 1 in {2, 3}, c(Q) = c(Z) >= K - 1, gamma(Q) = max(m(Q) - p, K - m(Q), -1) = K - m(Q)
<= K - 2.  Contradiction.
Case 2b: otherwise Z is certified (a singleton, an aligned pair, an anti triple or a pattern with 3 <= |Z| <= K; Lemma CW-K).
As in c3/proof-WALL.md Step 2: D_Z = |Z_al| - e_Z and c(Z) >= |Z_al| (aligned members have c_t >= 1, the anti member c_0 >= 0),
and c(Z) >= K - e_Z >= 0.  The third term of gamma(Z) is ceil((D_Z - 1)/2) - 1 <= ceil((|Z_al| - 1)/2) - 1 < |Z_al| <= c(Z); the
first is D_Z + m(Z) - p - 1 <= (K - 1) + K - p - 1 = 3 - K < 0 <= c(Z).  So c(Z) <= gamma(Z) forces c(Z) <= K - m(Z), and with
c(Z) >= K - e_Z we get m(Z) <= e_Z <= 1: e_Z = 1 (0 in Z), m(Z) = 1 (Z is one cyclic interval through 0) and c(Z) = K - 1.
Then c([k] - Z) = 0, and every aligned run outside Z has c_t = 0, i.e. x_t = 1.
Step 3.  (Z as at the end of Case 2b; |Z| = 2 is impossible there, since an interval of two runs through 0 is an anti pair,
which is Case 2a.)
Case 3a: |Z| >= 3.  Z is an interval of at most K runs, so at least k - K - 2 = p - 1 >= 1 runs are neither in Z nor adjacent
to Z; all are aligned with c_s = 0.  Q := Z u {s} has 4 <= |Q| <= K + 1 (certified by Lemma CW-K (c)), m(Q) = 2, c(Q) = K - 1,
D_Q = |Z_al| <= K - 1, so gamma(Q) <= max(K - p, K - 2, ceil((K - 2)/2) - 1) = K - 2 < c(Q).  Contradiction.
Case 3b: Z = {0}.  Then c_0 = K - 1 and every aligned run has c_t = 0.  Let s, s' be aligned runs pairwise non-adjacent and
not adjacent to 0 (e.g. s = 2, s' = 4).  Q := {0, s, s'} is an anti triple (certified), D_Q = 1, m(Q) = 3, c(Q) = K - 1, and
gamma(Q) = max(3 - p, K - 3, -1) = K - 3 < c(Q).  Contradiction.
Every case contradicts the Corollary, so w does not avoid.  []

Remarks.  (1) Patterns used: certified patterns with at most K + 1 runs (Steps 1-3), and the pin pair P, P^c.  The two
places where Theorem W-ALL's proof would use an (uncertified) anti pair -- Z = {0, a} in Step 2 and Z u {s} with Z = {0} in
Step 3 -- are replaced by anti triples.  (2) Hypotheses used beyond the imports: 3K = p + 5, K even (only through the
evaluation of floors, e.g. floor((4K - 7)/2) = 2K - 4), K >= 6 (p >= 13).  (3) Together with Theorem W-ALL
(c3/proof-WALL.md, ACCEPT) this excludes W(p, kB) for all 1 <= kB <= (p + 5)/3 when p = 1 (mod 6); for p = 13 that is
1 <= kB <= 6, leaving only W(13, 7..9) of the B = 1 all-singleton words at p = 13.

## 3. Exact computations [F] (aids; never hypotheses)

* review_check.py (out/review_check.txt): every certification step of Lemma CW-K on the type level (all (y, m, m') that occur)
  for every prime p = 1 (mod 6), 13 <= p <= 199: 20 primes, 0 failures; minimum slacks (A) - 1 = 0 (aligned pairs, anti
  triples, the size-4 step, the P^c chain start), (B) - (p + 1) >= 2.
* certk.cpp (out/certk_kb0.txt): exact certification DP.  W(13, 6) (k = 20, all sizes): every proper pattern is certified
  except the 19 anti pairs and the single pattern {0}^c; W(19, 8) (k = 28, sizes <= 9): exactly the 27 anti pairs are
  uncertified; in both the chain of (d) is valid step by step and lambda(P) + lambda(P^c) = K + 2 (= 8, 10).
* kb0_replay.py (out/kb0_replay.txt): the case analysis of Sec. 2 followed literally on 3,000 random integer vectors with
  singleton bounds and sum p for each of p = 13, 19, 31, 37, 43 (15,000 vectors): every vector yields a pattern in the
  certified family with X_Q < lambda(Q); every intermediate claim asserted; 0 failures.  Mutation controls: sum p + 1
  (MUT = 1: 546 failures), kill test against lambda - 1 (MUT = 2: 75 failures), the uncertified anti pair {0, s} in Case 3b
  (MUT = 3: all 240 Case-3b vectors rejected by the membership test).
* kb0_replay_s3.py (out/kb0_replay_s3.txt): targeted Case 3a vectors (every interval Z through 0 with 3 <= |Z| <= K and
  capped enumerations of c on Z), p = 13, 19, 31, 37, 43, 61: 98,226 vectors, 0 failures.
* Independent of this proof: c2/famdfs found no avoider in W(13, 6) (c3/out/famdfs_W_high.txt).
