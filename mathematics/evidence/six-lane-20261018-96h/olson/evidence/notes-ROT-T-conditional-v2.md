# Note (unreviewed; precise-obstruction statement, not submitted as a result): Proposition ROT-T, rotation rigidity
# conditional on the longest zero-sum length; the remaining rotation residual is exactly 'long longest zero-sums', v2

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:12:40-0700.  v2 after /bin/date 2026-10-19T01:13:09-0700 supersedes v1 (51275a5d...2a06, never sent): the
k = p bullet wrongly claimed (iii) up to kappa^ = (p + 3)/2; the t <= kappa^ bullet was imprecise about (iii).  Depends on the unreviewed candidate evidence/proof-BALfull-v2.md
(dffbfea8...a3e1: Lemma BAL-forall, Lemma ROOM) and the accepted chain listed there (REALIZE, ZSTRUCT, GRX, normal form,
DAV, KETA, SHgen/SHgen-E, restricted REFL).  Supersedes evidence/notes-kp-under-zb-v1.md (6cadd03d...8ddc) for k = p.

**Proposition ROT-T (conditional).**  Let p >= 7 be prime, w an avoider of length 4p - 2 over D_(2p), and w^ an admissible
normal form with terminal 2 <= k <= p and kappa^ >= 1; R = 2p + 2kappa^ - k; Y its rotation sequence and 2t the length of
a longest zero-sum of Y.  If
  (i) R - 2t >= p + 1,  (ii) R - 2t >= 2t + 1,  (iii) 2t <= 2p - k,  (iv) 2t <= 2p - 2k + 2kappa^ - 1,
then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0.

Proof.  t = 0: Y is zero-sum-free of length R >= p + 1; E = e' <= 2p - 1 - R = k - 1 - 2kappa^ and SHgen applies as in
ROT-ZR.  t >= 1: (i) gives the Setting-(S') objects (Z longest, L = R - 2t >= p + 1, g, ZSTRUCT); (S1) is used in
BAL-forall/ROOM only through 'Z longest' and the value of t, which is given here.  (ii) and Lemma BAL-forall: Z balanced.
Lemma ROOM (L >= 2t): W <= 2p - 1 - n+, so E <= k - 1 - 2kappa^ + n+ and all |b| <= p - 2 (e' <= 2p - 1 - L <= p - 2,
s_i <= slack <= p - 2).  n+ <= 2t - 1 (n- >= 1).  SHgen (H): 2H = 2p - 2 - 2kappa^ >= E iff n+ <= 2p - 1 - k, implied by
(iii).  SHgen (K) via KETA: eta + a_max <= E + 2 <= k - 2kappa^ + 2t <= 2p - k - 1 by (iv).  SHgen-E caller: base words
have o_F <= k <= p (restricted REFL).  []

Consequences (all conditional, all from the same chain):
- 2 <= k <= p - 1 and t <= kappa^ (the maximum allowed by (S1)): (iv) holds; if 2kappa^ + k <= 2p - 1 then (i)-(iii)
  hold for every t <= kappa^, i.e. Theorem ROT-ZB+ is this case of the proposition.
- High cells 2kappa^ + k >= 2p (k <= p - 1): if t <= kappa^ - d (d >= 1), then (ii) holds when 2kappa^ + k <= 2p - 1 + 4d
  (and (i) via L >= 2p - k + 2d), (iii) when 2kappa^ + k <= 2p + 2d, (iv) always.
- k = p (Q1a): if t <= kappa^ - 1 and 2 <= kappa^ <= (p + 1)/2: (i) L >= p + 2; (ii) 4t <= p + 2kappa^ - 1, true;
  (iii) 2t <= 2kappa^ - 2 <= p - 1, true; (iv) 2t <= 2kappa^ - 1, true.  (At kappa^ = (p + 3)/2, t = (p + 1)/2, (iii)
  fails although n+ <= p - 1 still holds there: n+ = p would force n- = 1 and s_1 = p > slack <= p - 3; this edge case
  is outside the proposition as stated.)

Precise remaining rotation obstruction.  For every terminal cell with 2 <= k <= p, rotation rigidity fails to follow from
this chain only when the rotation sequence has a LONG longest zero-sum: 2t > min over (ii)-(iv) bounds; in particular at
k = p exactly when t = kappa^ (complement of length exactly p; S(p) open) or kappa^ > (p + 1)/2, and in the high cells
when t is within about (2kappa^ + k - 2p)/4 of kappa^.  Deciding whether such avoiders exist needs a word-level argument
(the arc/sign-pattern machinery), not further sequence-level balance.
