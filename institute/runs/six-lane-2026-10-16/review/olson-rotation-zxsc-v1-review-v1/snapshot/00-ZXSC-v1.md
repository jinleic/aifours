# Lemma ZX-SC and Theorem ROT-ZX-SC: rotation rigidity beyond 3k <= 2p + 1 for terminal kappa^ in {0, 1} and 5k <= 4p - 1, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T13:11:33-07:00.  Status [W], UNREVIEWED.

This file changes no file.  It reuses the exchange proof of Lemma ZX (proof-ROT-ZX-v1.md, ad2460b2...815b, accepted
with overlay in R/olson-zx-s1c-parent-verdict-v1.md, 2f8d376b...e6af).  Lemma MULT is replaced by the Savchev-Chen
structure of long zero-sum-free sequences, derived in Sec. 0 from the same explicit classical index theorem as the S1 (d)
addendum (proof-ROT-ZX-addendum-S1d-v1.md, aefcfc58...c61b).
- New coverage: avoiders whose terminal k exceeds (2p + 1)/3, up to 5k <= 4p - 1, when terminal kappa^ is 0 or 1.
- This is a high-o range, outside 3 o_F <= 2p + 1, which no earlier file covers.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

Imports:
- (D);
- the explicit classical index theorem (Savchev-Chen 2007 / Yuan 2007), with the sources listed in the S1 (d) addendum;
  per the S1 (d) Codex review, Savchev's initial is S.;
- for Sec. 2, everything Theorem ROT-ZX imports (normal form, PM*, K1, GRX, DAV, SHgen, SHgen-E, REFL-few-odd), at the
  same scopes.

## 0. Long zero-sum-free sequences (consequence of the import)

**Lemma SC0.**  Let S be a zero-sum-free sequence over Z_(2p) of length t >= p + 1.  Then there are a generator g and
positive integers a_1, ..., a_t with S = (a_1 g) ... (a_t g) and a_1 + ... + a_t <= 2p - 1.
Proof.
- Let s := sum(S) and S^+ := S (-s).  Then S^+ is a zero-sum of length t + 1 >= p + 2 = floor(2p/2) + 2.
- S^+ is minimal: a proper zero-sum subsequence cannot lie in S, so it contains -s.  It then has the form U (-s) with
  sum(U) = s, so S - U is a zero-sum in S, forcing U = S.
- By the index theorem, S^+ = (x_1 a) ... (x_(t+1) a) with positive integers x_i summing to ord(a).
- ord(a) >= t + 1 >= p + 2 forces ord(a) = 2p, so a is a generator.
- Dropping the term -s leaves sum x_i <= 2p - 1 over the terms of S.  []
If S consists of odd elements, g is odd (it is a generator) and every a_i is odd.

## 1. Lemma ZX-SC

**Lemma ZX-SC.**  Let p >= 5 be prime and k, kappa integers with
  (R1) 1 <= k <= (4p + 1)/5,  0 <= kappa <= k - 1,  2kappa + k <= 2p - 1,
  (R2) kappa (k - 1) < p, or 3(k - 1) <= 2p - 1.
Let Y be a sequence of R = 2p + 2kappa - k odd elements of Z_(2p) with
  (S1) every zero-sum subsequence of Y has length <= 2kappa.
Let Z be a longest zero-sum subsequence of Y (possibly empty), Y' := Y - Z, and g the generator given by Lemma SC0 for
Y'.  Then cost_g(Y) <= e := k - 1 - 2kappa + |Z| <= k - 1, and every |b_g| <= k.

Proof.  This is the proof of Lemma ZX (proof-ROT-ZX-v1.md Sec. 2), with Step A replaced as follows and with two
remarks on Steps E and F.

Step A'.
- By (S1), |Z| <= 2kappa.  Y' is zero-sum-free.
- L := |Y'| >= 2p - k >= p + 1, since k <= (4p + 1)/5 <= p - 1 for p >= 5.
- e := 2p - 1 - L = k - 1 - 2kappa + |Z|, so 0 <= e <= k - 1.
- Lemma SC0 gives Y' = (a_1 g) ... (a_L g) with odd a_i >= 1 and W' := sum a_i <= 2p - 1.
  - Let m be the number of a_i equal to 1, and e' := W' - L <= e.
  - Each a_i >= 3 adds >= 2 to e', so m >= L - e'/2.  Every a_i <= e' + 1.
- (A2') Every a_i <= m.  Indeed e' + 1 <= L - e'/2 follows from e' <= e and 3e <= 2L - 2, i.e. 5L >= 6p - 1.  That
  holds because L >= 2p - k and k <= (4p + 1)/5.
  - So g has the largest multiplicity in Y'.  Every a_i is odd and <= e + 1 <= k <= p - 1, hence a_i <= p - 2, and
    b_g(a_i g) = a_i.
- COMP (a)-(c) of proof-ROT-ZX-v1.md hold verbatim: (a) by (A2'), (b) by W' <= 2p - 1, (c) trivially.
- (A3) W' >= L >= p + 1 > p.  (Steps C and D use only W' > p; ZX's "p + 2" is not needed.)
- (A4) Every single term of Y' has weight <= m.
Steps B, C, D: unchanged.  They use only (A2'), COMP and (A3)-(A4).

Step E (sigma = r): unchanged when 3e <= 2p - 1, which (R2)'s second alternative gives.
- Under (R2)'s first alternative, the case t >= 1 cannot occur: every beta <= e - e' <= k - 1 (Step D) and
  |T| <= |Z| <= 2kappa, so sigma <= 2kappa(k - 1) < 2p.
- Hence sigma = r + 2pt with t = 0.

Step F: unchanged.  Its final contradiction 2p <= |Z| + e' <= 2kappa + e <= 2kappa + k - 1 uses (R1).
Step G: unchanged.  cost_g(Y) = e' + r <= e <= k - 1, and every |b| <= k.  []

## 2. Theorem ROT-ZX-SC

**Theorem ROT-ZX-SC.**  Let p >= 5 be prime and w an avoider of length 4p - 2.  Suppose some normal form w^ produced by
the accepted process (proof-ROT-few-E-v4.md Sec. 0) has terminal k with 2 <= k <= (4p - 1)/5 and kappa^ in {0, 1}.  Then
all rotation letters of w lie in one {rho_c, rho_-c}, c != 0.
Proof.
- As for Theorem ROT-ZX, with Lemma ZX-SC in place of Lemma ZX.
- Hypotheses of Lemma ZX-SC:
  - k <= (4p - 1)/5 <= (4p + 1)/5;
  - kappa^ <= k - 1 (DAV);
  - 2kappa^ + k <= 2 + k <= 2p - 1;
  - kappa^ (k - 1) <= k - 1 < p;
  - (S1) at kappa^ in {0, 1} is Corollary S1+ (accepted), with (ZP) from GRX.
- Lemma ZX-SC gives |b| <= k <= p - 2 (so no rotation is rho_0) and E + N <= k - 1.
- SHgen hypotheses:
  - (H): 2H = 2p - 2 - 2kappa^ >= 2p - 4 >= k - 1 >= E;
  - (K): eta <= (k - 1)/2 and a_max <= k, so 2p - eta - a_max - 1 >= k, because 5k <= 4p - 1.
- SHgen, or SHgen-E with REFL for o_F <= k <= p (Corollary REFL-few-odd), gives E = 0.  []

**Corollary INV*-ZX-SC.**  Every avoider w of length 4p - 2 (p >= 5 prime) with 5 o_F(w) <= 4p - 1 and
F(w) >= o_F(w) + 2p - 4, i.e. kappa(w) <= 1, satisfies INV*.
Proof.
- Any normal form has k <= o and kappa^ = kappa(w) - (o - k)/2 <= kappa(w) <= 1.  The case k = 1 is K1.
- For k >= 2, Theorem ROT-ZX-SC applies.
- Then Corollary REFL-few-odd applies with o_F(w) <= (4p - 1)/5 <= p.  []

**Corollary OLSON-ZX-SC.**  Every word of length 4p - 1 over D_(2p) (p >= 5 prime) with 5 o <= 4p - 1 and
F - o >= 2p - 4 (o := o_F, F := F(w)) has an identity 2p-subword in increasing index order.
Proof.  The proof of OLSON-ZX (proof-ROT-ZX-v1.md Sec. 5), with the accepted deletion ledger:
- Case 1 needs o <= 2p - 3;
- Case 2 gives (o - 1, F - 1);
- Case 3 gives (o or o - 2, F).
None lowers F - o or raises o.  []

## 3. Scope

- New relative to the accepted range (3 o_F <= 2p + 1):
  - terminal (2p + 1)/3 < k <= (4p - 1)/5 with kappa^ <= 1;
  - uniformly, (2p + 1)/3 < o_F <= (4p - 1)/5 with F >= o_F + 2p - 4.
  - Examples: p = 11: o_F = 8 (needs F >= 26); p = 13: o_F = 10 (F >= 32); p = 19: o_F in {14, 15}; p = 29: o_F in
    {20, ..., 23}.
- Lemma ZX-SC also holds for larger kappa whenever (R1)-(R2) and (S1) hold.  But if k > (2p + 2)/3, then
  3(k - 1) > 2p - 1, so (R2) forces kappa(k - 1) < p.  Since k - 1 > (2p - 1)/3, this gives kappa < 3p/(2p - 1) < 2,
  i.e. kappa <= 1.  So beyond 3k <= 2p + 2 only kappa^ in {0, 1} occurs, and the theorem states only that case.
- Not covered by this route: terminal k > (4p - 1)/5, and terminal (2p + 1)/3 < k <= (4p - 1)/5 with kappa^ >= 2.  The
  accepted (p, p - 1) sequence obstruction concerns k = p only.
- Sufficient classes only.  No claim that such avoiders exist, and no claim that the remaining classes fail.
