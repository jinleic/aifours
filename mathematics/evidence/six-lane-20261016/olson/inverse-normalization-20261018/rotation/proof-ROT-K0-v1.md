# Lemma KETA ((K) from E alone), Theorem ROT-K0 (terminal kappa^ = 0, 2 <= k <= p - 1), and ZX-SC up to k <= floor((4p+1)/5), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T13:36:13-07:00.  Status [W], UNREVIEWED.

This file changes no file.  It uses:
- the accepted ZX-SC results (proof-ROT-ZXSC-v1.md, 15958303...db1a; R/olson-zxsc-parent-verdict-v1.md,
  cf039654...b134, read through its overlay);
- the accepted terminal criterion (R/olson-zx-s1c-parent-verdict-v1.md, 2f8d376b...e6af, item 3 and overlay);
- Theorem SHgen and its definitions (proof-SHgen-v3.md, fcbd5a97...eb5e, L39-49).
The parent noted Claude's remark in the ZX-SC review ("eta + a_max <= E + 2"); it is NOT used as a premise.  It is
re-derived here from the SHgen definitions as Lemma KETA.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

## 1. Lemma KETA

Definitions (proof-SHgen-v3.md L39-42).  Fix c != 0.  rho_c and rho_-c are light.  Every other rotation rho_x is heavy,
with signed weight b_x: the odd integer with x = b_x c (mod p) and |b_x| <= p - 2 if x != 0, and b_0 := p.  Then:
- eta is the number of heavies;
- a_j := |b| of heavy j, and a_max := max_j a_j;
- E := sum over the heavies of (a_j - 1).

**Lemma KETA.**  If eta >= 1, then eta + a_max <= E + 2.
Proof.
- Every heavy has a_j >= 3: a_j is odd, and a_j != 1 because rho_(+-c) are light; for x = 0, a_j = p >= 5.
- Hence E = (a_max - 1) + (sum over the other eta - 1 heavies of (a_j - 1)) >= (a_max - 1) + 2(eta - 1).
- Since eta >= 1, a_max - 1 + 2(eta - 1) >= a_max + eta - 2.  []

**Corollary KETA.**  If eta >= 1, E <= k - 1 and k <= p - 1, then (K) k <= 2p - eta - a_max - 1 holds.
Proof.  2p - eta - a_max - 1 >= 2p - (E + 2) - 1 >= 2p - k - 2 >= k.  []
(In Theorems ROT-ZX and ROT-ZX-SC, (K) was obtained from 5k <= 4p - 1.  By Corollary KETA, k <= p - 1 suffices
whenever the cost lemma gives E <= k - 1.)

## 2. Lemma K0 and Theorem ROT-K0

**Lemma K0.**  Let p >= 5 be prime and 1 <= k <= p - 1.  Let Y be a zero-sum-free sequence of R = 2p - k odd elements of
Z_(2p).  Then there is a generator g with every b_g(y) odd and in [1, k], and cost_g(Y) <= k - 1.  In particular
N = 0 and E <= k - 1.
Proof.
- R = 2p - k >= p + 1, so Lemma SC0 (proof-ROT-ZXSC-v1.md Sec. 0; accepted) gives Y = (a_1 g) ... (a_R g) with odd
  a_i >= 1 and sum a_i <= 2p - 1.
- Hence cost_g(Y), computed with the a_i as signed weights, equals sum (a_i - 1) <= 2p - 1 - R = k - 1.
- Each a_i <= 1 + (k - 1) = k <= p - 1, and a_i is odd, so a_i <= p - 2.  Therefore b_g(a_i g) = a_i.  []

**Theorem ROT-K0.**  Let p >= 5 be prime and w an avoider of length 4p - 2.  Suppose some normal form w^ produced by
the accepted process has terminal k with 2 <= k <= p - 1 and kappa^ = 0.  Then all rotation letters of w lie in one
{rho_c, rho_-c}, c != 0.
Proof.
- kappa^ = 0 means H = p - 1, and R = 2p - k.
- GRX with z = all + gives (ZP) at kappa = 0, i.e. no zero-sum subsequence of length in [2, 2p].  As R < 2p, the
  rotation sequence Y is zero-sum-free.
- Lemma K0 gives a generator g = Y(c), with c != 0 since g is a generator.  All weights b = a_i are odd and lie in
  [1, k]; as k <= p - 1, every |b| <= p - 2.  Also N = 0 and E <= k - 1.
- The weights are the SHgen weights relative to c: |b| <= p - 2 and x = b c.
- If E = 0, every rotation is rho_c.  Otherwise eta >= 1, and:
  - (H): 2H = 2p - 2 >= k - 1 >= E;
  - (K): Corollary KETA.
- Theorem SHgen (all runs nonempty), or Lemma SHgen-E (empty runs, REFL needed only for o_F <= k <= p, supplied by
  Corollary REFL-few-odd), gives an identity 2p-subword, contradicting avoidance.  So E = 0.  []
- DAV, K1 and the k = 1 case are as in the accepted terminal criterion.  k = 1 gives one nonzero pair by K1.

**Corollary INV*-K0 / OLSON-K0 (uniform).**  Let p >= 5 be prime and o := o_F(w), F := F(w).
- (a) Every avoider of length 4p - 2 with o <= p - 1 and F >= o + 2p - 2 (i.e. kappa(w) <= 0) satisfies INV*.
- (b) Every word of length 4p - 1 with o <= p - 1 and F - o >= 2p - 2 has an identity 2p-subword in increasing index
  order.
Proof.
- (a) Any normal form has k <= o <= p - 1 and kappa^ = kappa(w) - (o - k)/2 <= 0, so kappa^ = 0 (kappa^ >= 0).  k = 1
  is K1; k >= 2 is Theorem ROT-K0.  REFL-few-odd applies with o <= p.
- (b) The OLSON-ZX proof with the accepted deletion ledger: Case 1 needs o <= 2p - 3; Case 2 gives (o - 1, F - 1);
  Case 3 gives (o or o - 2, F).  None raises o or lowers F - o.  []

## 3. ROT-ZX-SC up to k <= floor((4p + 1)/5)

Theorem ROT-ZX-SC (accepted) assumed 5k <= 4p - 1 only to get (K).  Lemma ZX-SC itself holds for k <= (4p + 1)/5
(integer k; see the overlay for p = 5, 7), and gives E <= k - 1.  With Corollary KETA (k <= p - 1), the theorem's proof
goes through for every terminal 2 <= k <= floor((4p + 1)/5) with kappa^ in {0, 1}.  The uniform corollaries then hold
with 5 o_F <= 4p + 1 and F >= o_F + 2p - 4.  This differs from the accepted 5 o_F <= 4p - 1 only when p = 1 (mod 5),
e.g. p = 11 (o_F = 9), 31 (o_F = 25), 41 (o_F = 33).

## 4. Scope

- New, relative to accepted results:
  - terminal kappa^ = 0 with (4p - 1)/5 < k <= p - 1;
  - uniformly, words with o_F <= p - 1 and F >= o_F + 2p - 2 (kappa(w) <= 0); this is new where o_F > (4p + 1)/5.
  - Exact uniform conditions: o_F <= p - 1 and F >= o_F + 2p - 2 (kappa(w) <= 0), or 5 o_F <= 4p + 1 and
    F >= o_F + 2p - 4 (kappa(w) <= 1).
- Examples: p = 7: o_F = 6 with F >= 18; p = 11: o_F in {9, 10} with F >= o_F + 20 (o_F = 9 also with F >= 27).
- Not covered by this route:
  - terminal k = p with kappa^ = 0 (R = p): Lemma SC0 needs length >= p + 1.  The length-p case is the open S(p)
    question of notes-SC-lengthp-v2.md;
  - kappa^ = 1 with k > (4p + 1)/5: the completeness of weights used in ZX-SC Steps C-D can fail there;
  - everything with kappa^ >= 2 beyond 3k <= 2p + 1.
- Sufficient classes only; no existence claim.
