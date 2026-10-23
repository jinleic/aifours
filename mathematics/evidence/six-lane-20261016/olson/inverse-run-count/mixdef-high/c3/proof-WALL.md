# Theorem W-ALL: no word of W(p, kB) is an avoider when 1 <= kB <= min(p - 4, (p + 4)/3)

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a
hypothesis).  Written in c3/ after host clock 2026-10-17T12:12:22-0700 (freeze time and SHA-256 in
c3/out/freeze.txt).  Task OlsonRunCount3, cycle 3 of OlsonRunCount, item (iii) of ../proof-MH.md Sec. 6.
Imported (not re-proved): Lemma H with the 07:39 correction (../../../inverse-parity/proof-PAR-K0.md Sec. 1),
the Claim in the proof of Lemma BC (same file, Sec. 2), Lemma L (c3/proof-NOLP-r2.md Sec. 1 = c2/proof-NOLP.md
Sec. 1, reviewed ACCEPT-WITH-FIXES, the fix not touching Lemma L).
Scope: the single-letter family W(p, kB) only (defined below; it is the B = 1 part of the all-singleton words
of item (iii)).  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), INV or ordered Olson.  For kB = 4 it gives
a second, independent proof of Theorem W4 (c3/proof-W4-r2.md).

## 0. The family and its parameters

For a prime p >= 5 and an integer kB with 1 <= kB <= p - 4, W(p, kB) is the set of RGR words of length 4p - 2
(x normalised to 1) with k = p + 1 + kB rotation runs, each a single letter, exactly one of them rho_{-1}
(the anti run, placed at position 0 after a rotation) and the others rho_1 (aligned runs 1, ..., k - 1), and
odd reflection runs l_1, ..., l_k with sum_j floor(l_j/2) = p - 2 - kB.  (This is the definition of
c2/proof-NOBC.md Sec. 1 with the range of kB extended from 4 <= kB < (p+6)/4 to 1 <= kB <= p - 4.)
Parameters: R = k, A = p + kB, B = 1, D = A - B = p + kB - 1, H = p - 2 - kB, kappa = p - 1 - H = kB + 1,
kappa - B = kB.  Membership in item (iii): all reflection runs odd; p + 1 <= k = p + 1 + kB <= 2p - 3;
every run pure; 1 <= B = 1 <= kappa - 1 = kB; B <= A = p + kB <= 2p - 1; R = k <= 2p - 3; k >= p + 2, so
not the ZSI-B case (k = p + 1).  Conversely every all-singleton item-(iii) word with B = 1 lies in some
W(p, kB) (all-singleton means kappa = k - p, so kB = k - p - 1 and 1 <= kB <= p - 4).

Lambda (Lemma H, all reflection runs odd so beta = 0): for a proper pattern Q with j aligned runs,
e in {0, 1} anti runs (e = [0 in Q]) and m blocks, D_Q = j - e and
   lambda(Q) = min(p - m + 1, j - e + m - kB, floor((j - e + 1)/2) + 1).                        (0.1)
Q^c has p + kB - j aligned runs, 1 - e anti runs and the same m blocks, so
   lambda(Q^c) = min(p - m + 1, p - 1 - (j - e) + m, floor((p + kB - (j - e))/2) + 1).           (0.2)
Special values: aligned singleton lambda = 2 - kB; anti singleton {0}: lambda = -kB; the complement of an
aligned singleton: Lambda1 := floor((p + kB - 1)/2) + 1 (the middle term p - 1 of (0.2) is larger as
kB <= p - 3), and Lambda1 >= (p + kB)/2; the complement of {0} (the interval I_{p+kB} of all aligned
runs): Lambda0 := floor((p + kB + 1)/2) + 1 <= p.

Lemma L (imported).  A proper pattern Q is certified if |Q| = 1, or Q = Q' u {t} (t notin Q') with Q'
certified and
   (A) lambda(Q') + lambda({t}) + lambda(Q^c) >= 1,   (B) lambda(Q) + lambda(Q'^c) + lambda({t}^c) >= p + 1.
If w avoids, with half-sums u_t (Lemma H), and the integers x_t = u_t (mod p) are chosen in
[lambda({t}), p - lambda({t}^c)], then X_Q := sum_{t in Q} x_t lies in [lambda(Q), p - lambda(Q^c)] for every
certified Q.

## 1. Lemma CW (certification in W(p, kB))

**Lemma CW.**  Let p >= 5 be prime, 1 <= kB <= p - 4 and 3kB <= p + 4.  In every word of W(p, kB):
(a) every proper pattern with at most kB + 1 runs is certified;
(b) every interval I_i := {1, ..., i} (1 <= i <= p + kB) is certified.

Preliminary: 2kB <= p - 1.  (For p >= 11, 2kB <= 2(p + 4)/3 <= p - 1; for p = 5, kB = 1; for p = 7, kB <= 3.)

Proof of (a).  Induction on |Q|; singletons are certified.  Let 2 <= |Q| <= kB + 1, j aligned runs, e anti
runs, m blocks.  Q contains an aligned run (there is only one anti run).  If some block of Q has >= 2 runs,
let t be an aligned END run of such a block (its two ends are distinct and at most one is the anti run);
then Q' := Q - {t} has m' = m blocks.  Otherwise all blocks are single runs; let t be an aligned one; then
m' = m - 1.  In both cases j' = j - 1, e' = e, and with y := j - e we have 0 <= y <= kB + 1 (j >= 1 >= e),
1 <= m' <= |Q'| <= kB, m' >= m - 1 and m <= kB + 1.  By induction Q' is certified; we verify (A), (B).
Each lambda is a minimum of terms, and a sum of minima is the minimum of the sums of one term from each, so it
suffices to bound every such sum.

(A) reads lambda(Q') + lambda(Q^c) >= kB - 1 (as lambda({t}) = 2 - kB).  Terms of lambda(Q') (by (0.1)):
U1 = p - m' + 1 >= p - kB + 1, U2 = y - 1 + m' - kB, U3 = floor(y/2) + 1 >= 1.  Terms of lambda(Q^c) (by (0.2)):
T1 = p - m + 1 >= p - kB, T2 = p - 1 - y + m >= p - kB - 1, T3 = floor((p + kB - y)/2) + 1 >= (p + 1)/2.
* U1 + T_b >= p - kB + 1 + min(p - kB - 1, (p + 1)/2) >= kB - 1, since p >= 2kB + 1.
* U3 + T_b >= 1 + min(p - kB - 1, (p + 1)/2) >= kB - 1.
* U2 + T1 = p + y - kB + (m' - m) >= p - kB - 1 >= kB - 1.
* U2 + T2 = p - 2 - kB + m + m' >= p - kB >= kB - 1.
* U2 + T3 = y + m' - kB + floor((p + kB - y)/2); we need floor((p + kB - y)/2) >= 2kB - 1 - y - m'.
  If y >= 1: the right side is <= 2kB - 2 - y and the left side is >= (p + kB - y - 1)/2; the inequality
  follows from p + 3 + y >= 3kB, true as y >= 1 and 3kB <= p + 4.  If y = 0 and m' >= 2: need
  (p + kB - 1)/2 >= 2kB - 3, i.e. p + 5 >= 3kB.  If y = 0 and m' = 1: then j = e = 1, Q = {0, t}, Q' = {0},
  and we need floor((p + kB)/2) >= 2kB - 2: for kB odd this is p + 4 >= 3kB; for kB even it is p + 3 >= 3kB,
  which follows from 3kB <= p + 4 because 3kB is even and p + 4 is odd.
(B): lambda(Q) + lambda(Q'^c) + Lambda1 >= p + 1.  Terms of lambda(Q): V1 = p - m + 1 >= p - kB, V2 = y + m - kB,
V3 = floor((y + 1)/2) + 1 >= 1.  Q' has j - 1 aligned runs, so lambda(Q'^c) has terms T1' = p - m' + 1 >= p - kB + 1,
T2' = p - y + m' >= p - kB, T3' = floor((p + kB - y + 1)/2) + 1 >= (p + kB - y)/2 + 1 >= (p + 1)/2.  Using
Lambda1 >= (p + kB)/2:
* V2 + T3' + Lambda1 >= y + m - kB + (p + kB - y)/2 + 1 + (p + kB)/2 = p + 1 + y/2 + m >= p + 1.
* V2 + T2' + Lambda1 = p + m + m' - kB + Lambda1 >= p + 2 - kB + (p + kB)/2 >= p + 1.
* V2 + T1' + Lambda1 = p + 1 + y + (m - m') - kB + Lambda1 >= p + 1 - kB + (p + kB)/2 >= p + 1.
* V1 + T_b' + Lambda1 >= (p - kB) + (p + 1)/2 + (p + kB)/2 >= p + 1, and V3 + T_b' + Lambda1 >= 1 + (p + 1)/2 + (p + kB)/2 >= p + 1,
  using min(T1', T2', T3') >= (p + 1)/2 (as p - kB >= (p + 1)/2).
So (A), (B) hold and Q is certified.

Proof of (b).  I_1 is a singleton.  For 1 <= i <= p + kB - 1, I_{i+1} = I_i u {i + 1} with i + 1 aligned.  By
(0.1), lambda(I_i) = min(p, i + 1 - kB, floor((i + 1)/2) + 1); I_i^c = {0, i + 1, ..., p + kB} is one block, so
by (0.2) c_i := lambda(I_i^c) = min(p - i, floor((p + kB - i)/2) + 1) (the term p is >= p - i), and c_{p+kB} =
lambda({0}) = -kB fits this formula.
(A) lambda(I_i) + c_{i+1} >= kB - 1:
* (i + 1 - kB) + (p - i - 1) = p - kB >= kB - 1;
* (i + 1 - kB) + floor((p + kB - i - 1)/2) + 1 >= (p + i + 2 - kB)/2 >= kB - 1 as p + i + 4 >= 3kB (i >= 1);
* floor((i + 1)/2) + 1 + (p - i - 1) = p - floor(i/2) >= p - floor((p + kB - 1)/2) >= kB - 1: for kB even this is
  (p + kB - 1)/2 <= p - kB + 1, i.e. 3kB <= p + 3 (true by parity as above); for kB odd, (p + kB - 2)/2 <= p - kB + 1,
  i.e. 3kB <= p + 4;
* floor((i + 1)/2) + 1 + floor((p + kB - i - 1)/2) + 1 >= (p + kB)/2 + 1 >= kB - 1;
* p + c_{i+1} >= p - kB >= kB - 1 (c_{i+1} >= min(p - i - 1, 1) >= -kB).
(B) lambda(I_{i+1}) + c_i + Lambda1 >= p + 1:
* (i + 2 - kB) + (p - i) + Lambda1 = p + 2 - kB + Lambda1 >= p + 1;
* (i + 2 - kB) + floor((p + kB - i)/2) + 1 + Lambda1 >= i + 3 - kB + (p + kB - i - 1)/2 + (p + kB)/2 = p + 5/2 + i/2;
* floor((i + 2)/2) + 1 + (p - i) + Lambda1 >= p + 1 iff Lambda1 >= ceil(i/2) - 1, true as i <= p + kB - 1;
* floor((i + 2)/2) + 1 + floor((p + kB - i)/2) + 1 + Lambda1 >= (p + kB)/2 + 2 + Lambda1 >= p + 1;
* p + c_i + Lambda1 >= p + 1 as c_i >= min(p - i, 1) >= 1 - kB and Lambda1 >= kB.  []

**Corollary (pin).**  In the setting of Lemma CW, if w avoids and x is as in Lemma L, then X_[k] = p.
Proof.  {0} is certified (singleton) and so is I_{p+kB} = {0}^c (Lemma CW(b)).  By Lemma L, x_0 is in
[-kB, p - Lambda0] and X_{I_{p+kB}} is in [Lambda0, p + kB].  So X_[k] = x_0 + X_{I_{p+kB}} lies in
[Lambda0 - kB, 2p + kB - Lambda0], which is inside [1, 2p - 1] because Lambda0 - kB = floor((p + kB + 1)/2) + 1 - kB >= 1
(p + 1 >= kB).  X_[k] = sum_t u_t = 0 (mod p), hence X_[k] = p.  []

## 2. Theorem W-ALL

**Theorem W-ALL.**  Let p >= 5 be prime and kB an integer with 1 <= kB <= p - 4 and 3kB <= p + 4.  Then no word
of W(p, kB) is an avoider: every such word has an identity 2p-subword.

Proof.  Suppose w in W(p, kB) avoids; take x as in Lemma L.  By Lemma CW and the Corollary, X_Q >= lambda(Q)
for every proper Q with |Q| <= kB + 1, and X_[k] = p.  Put c_t := d_t - x_t (so c_0 = -1 - x_0 and c_t = 1 - x_t for
aligned t) and c(Q) := sum_{t in Q} c_t = D_Q - X_Q.  Then sum_t c_t = D - p = kB - 1, and since
D_Q - lambda(Q) = max(D_Q + m - p - 1, kB - m, D_Q - floor((D_Q + 1)/2) - 1) and D_Q - floor((D_Q + 1)/2) =
ceil((D_Q - 1)/2),
   X_Q >= lambda(Q)  <=>  c(Q) <= gamma(Q) := max(D_Q + m(Q) - p - 1, kB - m(Q), ceil((D_Q - 1)/2) - 1).   (2.1)
Let Z_al := {aligned t : x_t <= 0} = {aligned t : c_t >= 1}, e_Z := [x_0 <= -1] = [c_0 >= 0], Z := Z_al u ({0} if e_Z = 1).
Step 1.  If |Z_al| >= kB, let Q consist of kB runs of Z_al.  Then c(Q) >= kB, D_Q = kB, 1 <= m(Q) <= kB, and
gamma(Q) <= max(2kB - p - 1, kB - 1, ceil((kB - 1)/2) - 1) = kB - 1 < c(Q), contradicting (2.1) (|Q| = kB).
Step 2.  So |Z_al| <= kB - 1 and |Z| <= kB.  Runs outside Z: aligned ones have c_t <= 0, and the anti run, if
outside Z, has c_0 <= -1.  Hence c(Z) = (kB - 1) - c([k] - Z) >= kB - 1 + (1 - e_Z) = kB - e_Z.  In particular Z is
nonempty (c(empty) = 0 < kB - e_Z unless kB = 1 = e_Z, and e_Z = 1 means 0 in Z) and proper (|Z| <= kB < k), so
m(Z) >= 1, and (2.1) applies to Z.  Now D_Z = |Z_al| - e_Z and c(Z) >= |Z_al| (aligned members have c_t >= 1, the
anti member c_0 >= 0); also c(Z) >= kB - e_Z >= 0.  The third term of gamma(Z) is ceil((D_Z - 1)/2) - 1 <=
ceil((|Z_al| - 1)/2) - 1 < |Z_al| <= c(Z); the first is D_Z + m(Z) - p - 1 <= (kB - 1) + kB - p - 1 < 0 <= c(Z)
(2kB <= p - 1).  Hence c(Z) <= kB - m(Z), and with c(Z) >= kB - e_Z we get m(Z) <= e_Z <= 1.  Therefore e_Z = 1
(the anti run is in Z), m(Z) = 1 (Z is a single cyclic interval containing the anti run), and c(Z) = kB - 1.  Then
c([k] - Z) = 0, and as every run outside Z is aligned with c_t <= 0, every aligned run outside Z has c_t = 0,
i.e. x_t = 1.
Step 3.  Z is an interval of at most kB runs, so at least k - kB - 2 = p - 1 >= 1 runs are neither in Z nor
adjacent to Z; let s be one (aligned, c_s = 0).  Q := Z u {s} has |Q| <= kB + 1, m(Q) = 2, c(Q) = kB - 1 and
D_Q = |Z_al| <= kB - 1, so gamma(Q) <= max(kB - p, kB - 2, ceil((kB - 2)/2) - 1) = kB - 2 < c(Q), contradicting (2.1).  []

Remarks.  (1) Hypotheses used: Lemma H, Lemma L (Claim of Lemma BC), Lemma CW (needs 3kB <= p + 4) and the
integrality of the lifts (c_t >= 1 for aligned t with x_t <= 0); every pattern used has at most kB + 1 runs.
By Lemma NOLP (c3/proof-NOLP-r2.md) integrality is unavoidable for kB >= 4, p >= 4kB - 1 within the lifted system.
(2) Range.  For each prime p the theorem covers 1 <= kB <= min(p - 4, floor((p + 4)/3)): p = 5: kB = 1 (all of item
(iii) at p = 5, see README Sec. 5); p = 7: kB <= 3 (all W(7, kB)); p = 11: kB <= 5; p = 13: kB <= 5; p = 17, 19: kB <= 7;
in particular every kB with 4 <= kB < (p + 6)/4 (as (p + 6)/4 <= (p + 4)/3 for p >= 2).  NOT covered:
(p + 4)/3 < kB <= p - 4 (nonempty for p >= 11).  There the method fails at its first step: for 3kB >= p + 5 the
anti pair {0, s} is not certified by singleton extension ((A) needs floor((p + kB)/2) >= 2kB - 2), and for
3kB >= p + 7 no pair is ([F] cert.cpp: W(11, 6), W(11, 7) have no certified pair).
(3) Relation to Theorem W4: kB = 4, p >= 11 satisfies 3kB = 12 <= p + 4; the argument above is different (patterns
with <= 5 runs, three short steps).

## 3. Exact computations [F] (aids; never hypotheses)

* cert.cpp (exact singleton-extension DP over all 2^k patterns): W(11, kB): every proper pattern certified for
  kB <= 5, no pair certified for kB = 6, 7 (out/cert_W.txt).  Further (p, kB) in out/cert_W.txt.
* Type-level replay of Lemma CW (cw_check.py, out/cw_check.txt): the inequalities (A), (B) for every step type used in
  the proof of (a) (all (j, e, m) with j + e <= kB + 1) and every step of (b), for every prime 5 <= p <= 199 and every
  1 <= kB <= p - 4: they hold exactly when 3kB <= p + 4.
* wkill.py / wkill2.py (kill rule of the proof, README Sec. 4): hard lift vectors (sum p, singleton bounds, all pair
  constraints) for (p, kB) in {(11,1..5), (13,2..5), (17,4), (17,7), (19,7), (23,9)} plus random ones; the procedure of
  Steps 1-3 always outputs a pattern with <= kB + 1 runs violating its window (re-checked by an independent lambda), and
  every intermediate claim (sum c = kB - 1, c(Z) >= kB - e_Z, Step 2 structure) holds (out/wkill.txt, out/wkill2.txt).
* c2/famdfs (exact avoider search over ALL patterns, mod p): no avoider in W(11, kB), kB = 5, 6, 7, and W(13, kB),
  kB = 6, 7, 8, 9 (out/famdfs_W_high.txt) -- the uncovered range (p + 4)/3 < kB has no avoider at p = 11, 13.
