# Notes (candidate partial; LS NOT proved): the base case of LS -- induction on kappa, Lemma BB, and the exact residue, v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T02:50:30-0700.  Builds on evidence/proof-SLZ-EXT-v2.md (2495300...1bc751,
candidate) and Lemma FB-p of evidence/proof-KPS-cond-v3.md (cfaf3cc5...ed01, candidate; FB-p itself does not use S(p)).
Scope: evidence/LS-scope-v1.md.  Status [W], unreviewed.  thr := p + 2kappa + 1.

## 1. Induction on kappa
Suppose LS(p, kappa - 1) holds (true for kappa - 1 <= floor(2p/3) by S1-sharp).  If Y (|Y| >= thr, (ZP_kappa)) has no
zero-sum of length exactly 2kappa, then Y satisfies (ZP_(kappa-1)) and |Y| >= thr(kappa - 1) + 2, so (S1_(kappa-1)), hence
(S1_kappa).  So a counterexample to LS(p, kappa) (WLOG of length thr, Corollary RED) contains a zero-sum of length 2kappa,
whose complement has length p + 1.

## 2. Lemma BB (boundary branch)
Let 1 <= kappa <= p - 2 and Y satisfy (ZP_kappa) with |Y| >= thr.  Suppose a term z of Y is such that Y - z satisfies
(S1_kappa) and contains a zero-sum Z' of length 2kappa with Y - Z' zero-sum-free.  Then Y satisfies (S1_kappa).
Proof.  If |Y| >= thr + 1 this is Corollary PROP (|Y - z| >= thr).  Let |Y| = thr, C' := Y - z - Z' (|C'| = p).  Y - Z' =
C' z is zero-sum-free of length p + 1, so SC0 gives an odd generator g with coefficient sum <= 2p - 1 on C' z; writing
z = c g (c >= 1), C' is SC w.r.t. g with W' <= 2p - 1 - c <= 2p - 2.  Z' is a longest zero-sum of Y - z ((S1_kappa)), and
(ZP_kappa) excludes zero-sums of length 2p (kappa <= p - 2).  Lemma FB-p applies to (Y - z, Z', g): its exceptional case
(X) needs C' = g^(p-1)(pg) with W' = 2p - 1, impossible; so Z' = g^(n+) N with s_i <= 2p - 1 - W', S(N) = n+ and
W' + n+ <= 2p - 1.  Now run Lemma EXT's Steps 1-3 with Y1 := Y - z (L = p): Step 1 uses only W' + n+ <= 2p - 1; Step 2:
n+ <= 2p - 1 - W' <= p - 1, so sum (s_i - 1) = 2n+ - 2kappa <= 2p - 2 - 2kappa and every s_i + 1 <= 2p - 2kappa; Step 3:
c <= 2kappa - 1 (from a long zero-sum), and A(H*) + |H*| <= 2e' with e' = W' - p <= p - 1 - n+ <= p - 2 (n+ >= n- >= 1 as
kappa >= 1 and S(N) = n+), so c + A(H*) + |H*| <= 2p + 2kappa - 5.  The descent produces a zero-sum of Y of length in
[2kappa + 2, 2p]: contradiction with (ZP_kappa).  []

## 3. The residue of the base case
Let Y be a counterexample of length thr (Sec. 1: Y has 2kappa-zero-sums).  For every term z, exactly one of:
- (i) Y - z fails (S1_kappa) (some long zero-sum avoids z);
- (iii) Y - z satisfies (S1_kappa), its longest zero-sums have length exactly 2kappa (else PROP), and for EVERY such Z' the
  complement Y - Z' = C' z contains a zero-sum (necessarily through z, of length >= 2p + 2 - 2kappa; else Lemma BB).
Under S(p) (open; finite-checked for p <= 17 in the earlier round, not a premise), branch (iii) also closes except for the
FB-p family (X): C' is SC by S(p), FB-p gives (N) -- then the same descent applies -- or (X), where Y - z is
g^(p-1)(pg)^(2kappa+1) or g^(2p-1)(pg)^(2kappa-p+1); for the first, adding any odd z creates a zero-sum of every even length
in [1 + x, 1 + x + 2kappa] for some x in [1, p - 1], hence one of length in [2kappa + 2, 2p]; the second is not checked here.
Branch (i) for every z: then a shortest long zero-sum T has N <= thr - 2, and every term z of T lies in a sub-multiset
V_z of T with |V_z| <= 2kappa - p - 1 whose sum equals the sum of a sub-multiset of X := Y - T (from a long zero-sum
T_z avoiding z: V_z = T - T_z, T_z - T <= X).  No contradiction is derived here.

## 4. Sharpness information (aids)
Probe v12 (recorded in proof-SLZ-EXT-v2.md Sec. 6): (ZP)-and-not-(S1) multisets of length p + 2kappa - 1 exist at p = 11,
kappa = 9, with no term common to all long zero-sums; so branch (i) occurs just below the threshold, and any proof of the base
case must use the full length thr.
