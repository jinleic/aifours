# Theorem ROT-KP+ with Lemma FB-p and Lemma ARC0: the k = p cells with (S1), relative to the classical import S(p), v4

Owner ContinueOlson (math-2 lane, 96-hour continuation).  v4 written after /bin/date 2026-10-19T03:16:25-0700.  v4 = v3
(evidence/proof-KPS-cond-v3.md, cfaf3cc5ea6862ea7e7a3c1f28e3a1f9b781fb0345e629695c71b08fb51eed01) made unconditional relative to the
classical import S(p) recorded in evidence/import-Sp-XiaYuan-v1.md (sha256 d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7),
on parent instruction; NO mathematical step changed.  Changed text only: this header, the title, the S(p) and (SC') lines of
Sec. 0, the labels of the Theorem and Corollary, the import list of Sec. 1, the t = kappa^ bullet of Sec. 4, the label of
Sec. 5 and the first and third bullets of Sec. 6.  Earlier history: v1 (61d7f954...543e) and v2 (46bf6eca...8798) never sent;
v3 cited the k = p SHgen/SHgen-E caller to the accepted ROT-KP verdict scope and read ROT-FB (b) through
evidence/proof-FB-v1-erratum-1.md (33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202).
Dependency status (fact, not a body change): proof-FB-v1.md + erratum 1, including Theorem ROT-FB (b), is now parent-accepted
as a written scoped partial (run review/olson-FB-parent-verdict-v1.md, sha256 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a);
the body's '(candidate)' labels for ROT-FB (b) read accordingly.
Status: CANDIDATE, written proof [W], UNREVIEWED; relative to the imports of Sec. 1, including the classical import S(p) (a
corollary of Xia-Yuan 2010 Thm 3.1, the index-one theorem and splitting; Xia-Yuan's primary text not read, see the import
note's trust boundary).  No computation is a premise.  No novelty claim; no Lean.  Not unrestricted INV*(p), not ordered
Olson for D_2p, not the all-groups target.

## 0. Statements

S(p) (classical import, evidence/import-Sp-XiaYuan-v1.md; formerly open in notes-SC-lengthp-v2.md): every zero-sum-free
sequence of p odd elements of C_(2p) is SC, i.e. has an odd generator g with W := sum of the least positive coefficients
<= 2p - 1.
(SC') (per word: for the rotation sequence Y of w^, SOME longest zero-sum Z of length 2kappa^ has an SC complement) is implied
by S(p) and no longer a hypothesis.

**Lemma FB-p.**  Let p >= 5 be prime, Y a sequence of odd elements of C_(2p) with no zero-sum of length 2p, Z a longest
zero-sum subsequence with |Z| = 2t, 1 <= t <= p - 1, Y' := Y - Z of length exactly p, and g an odd generator with
W <= 2p - 1 for Y' (coefficients a_i, m := #{a_i = 1}, slack := 2p - 1 - W).  Then either
- (X) Y' = g^(p-1) (pg) and every term of Z is g or pg; or
- (N) every term of Z is g or -s g with s odd, 1 <= s <= min(2t - 1, slack), and (writing Z = g^(n+) N) S(N) = n+ and
  W + n+ <= 2p - 1.

**Lemma ARC0.**  Let p >= 5, w^ a normal form (k >= 2 blocks, all odd) of length 4p - 2 with kappa^ >= 1 and 2kappa^ <= 2p - 2,
whose rotation multiset is (X1) rho_c^(p-1) rho_0^(2kappa^+1) or (X2) rho_c^(2p-1) rho_0^(2kappa^-p+1) with 2kappa^ >= p + 1,
c != 0.  Then w^ has an identity 2p-subword.

**Theorem ROT-KP+ (relative to Import S(p)).**  Let p >= 7 be prime and w an avoider of length 4p - 2 over D_(2p) with an
admissible normal form w^ of terminal k = p, kappa^ >= 1, (S1) at kappa^ (automatic for kappa^ <= floor(2p/3) by S1-sharp).
Then every rotation letter of w lies in one set {rho_c, rho_-c}, c != 0.

**Corollary (relative to Import S(p)).**  For every prime p >= 7, every avoider of length 4p - 2 with o_F <= p and
kappa(w) <= floor(2p/3) satisfies INV*, and every word of length 4p - 1 with o_F <= p and F - o_F >= 2(p - 1 - floor(2p/3))
has an identity 2p-subword in increasing index order.

## 1. Imports

As in evidence/proof-FB-v1.md Sec. 1 (ZSTRUCT/REALIZE proofs, S1-sharp, the word-level chain incl. SHgen/SHgen-E with the
ROT-ZR caller discharge and restricted REFL for o_F(u°) <= k <= p), plus: Theorem ROT-FB (b) of proof-FB-v1.md
(candidate) for t <= kappa^ - 1; ROT-KP (accepted: k = p, kappa^ in {0, 1}); the ARC form of GRX (proof-ROT-KP-v1.md
Sec. 0, accepted): for blocks j != j' and the arc A = (j, j'] of runs, if some even m with max(0, 2kappa^) <= m <=
min(R, 2p - 2) and some m rotation letters have signed value sum y_(j') - y_j (sign + outside A, - inside), then w^ has an
identity 2p-subword.
Import S(p): evidence/import-Sp-XiaYuan-v1.md (sha256 d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7): Xia-Yuan,
Discrete Math. 310 (2010) Thm 3.1 (via Peng-Sun arXiv:1409.1970v1 Thm 1.3(2)), the index-one theorem (parent import record
e4615144...35c6) and the splitting lemma proved there.

## 2. Proof of Lemma FB-p

(R) Realisation at L = p.  Sort the coefficients 1 = ... = 1 < a_(1) <= ... <= a_(h) and X_i := m + sum_(j<i) a_(j).  If
a_(i) >= X_i + 1 for some i, with n := h - i + 1: W >= X_i + n(X_i + 1) and p = L <= X_i + n.  n = 1 gives W >= 2X_i + 1 >=
2p - 1, so W = 2p - 1, X_i = p - 1 and (X_i is the sum of the other p - 1 terms) Y' = g^(p-1)(pg).  For 2 <= n <= p - 1,
W >= (p - n)(n + 1) + n, a concave function of n equal to 3p - 4 at n = 2 and 2p - 1 at n = p - 1; equality W = 2p - 1 forces
n = p - 1, X_i = 1, m = 1, i = 1, and then W >= 1 + 3(p - 1) > 2p - 1; n >= p gives W >= 3p.  So outside (X) every
a_(i) <= X_i, the subset sums of the coefficients fill [0, W], and every integer in [2, W] is the coefficient sum of a
sub-multiset of Y' with at least two terms (a heavy value a_(i) is realised by the strictly smaller terms).
(Z) Shape of Z.  Let z = r g in Z, r odd in [1, 2p - 1].  If 3 <= r <= W and r is realised by a sub-multiset Q of Y' with
|Q| >= 2, then (Z - {z}) u Q is a longer zero-sum: impossible.  In case (X) (W = 2p - 1, slack = 0) every r in [3, 2p - 1]
except r = p is so realised (r <= p - 1 by units, r >= p + 1 by pg plus units), so z in {g, pg}.  Otherwise r = 1 or
r >= W + 1; then s := 2p - r <= slack, and m - slack >= 2L - 2p + 1 + h = 1 + h >= 1 gives g^s within Y', so g^s z is a
zero-sum of length s + 1 <= 2t.
(B) Balance and room (outside (X)).  S(N) = n+ (mod 2p) as sigma(Z) = 0.  Put delta := 2p - W = slack + 1 and suppose
S(N) >= delta.  Exactly as in Lemma FB (proof-FB-v1.md Sec. 2) take the r largest terms with S_r >= delta (r >= 2),
y := S_r - delta <= slack - 1 < m, y + r <= delta, and Z* := (Y' minus y terms g) u g^(n+) u (N minus those r terms), a
zero-sum of length L + 2t - (y + r) = p + 2t - (y + r).  As |Z*| and 2t are even and p is odd, y + r is odd.  If
W >= p + 2 then |Z*| >= 2t + p - delta = 2t + W - p >= 2t + 2.  If W = p (Y' = g^p, delta = p) then either y + r <= p - 2 and
|Z*| >= 2t + 2, or y + r = p = delta, which forces equality in y + r <= s_(r) + (r - 1) <=
(delta - 1)/(r - 1) + (r - 1) <= delta, i.e. r - 1 in {1, delta - 1} with all of s_(1), ..., s_(r) equal: r - 1 = 1 would
need s = delta - 1 = p - 1 even, impossible, so r = p and s_(1) = ... = s_(p) = 1; then Y contains g^p (Y' = g^p) and
(-g)^p, a zero-sum of length 2p: excluded by hypothesis.  In every case |Z*| >= 2t + 2 contradicts the maximality of Z.
So S(N) <= slack <= 2p - 1, and with 0 <= n+ <= 2t < 2p: S(N) = n+ and W + n+ <= 2p - 1.  []

## 3. Proof of Lemma ARC0

Fix blocks j != j' (k >= 2), A := (j, j'], tau := y_(j') - y_j and d in Z_p with d c = tau.  Let U+ / U- be the numbers
of rho_c letters outside / inside A (U+ + U- = a, the multiplicity of rho_c) and b the multiplicity of rho_0 (signed value
0 everywhere).  For an integer e = d (mod p) with -U- <= e <= U+ and integers j0 >= 0, 0 <= z <= b with
max(e, 0) + j0 <= U+ and max(-e, 0) + j0 <= U-, the letters (max(e,0) + j0 outside rho_c, max(-e,0) + j0 inside rho_c,
z letters rho_0) are m = |e| + 2j0 + z rotation letters with signed value sum e c = tau.  For fixed e these m fill the
integer interval [|e|, top(e)] with top(e) = |e| + 2J + b, J = min(U+ - max(e,0), U- - max(-e,0)) (b >= 1 gives both
parities).  It suffices to find e with an even integer in [max(|e|, 2kappa^), min(top(e), 2p - 2)] (then (ARC) applies;
m <= R holds as m counts letters of w^).
(X1) a = p - 1, b = 2kappa^ + 1: [-U-, U+] has exactly p integers, so e exists and |e| <= p - 1 <= 2p - 2.  Let
x := max(|e|, 2kappa^) <= 2p - 2.  top(e) >= |e| + b >= x + 1.  If x = 2p - 2, x is even; otherwise x and x + 1 both lie in
the window, one of them even.
(X2) a = 2p - 1, b = 2kappa^ - p + 1 >= 2: [-U-, U+] has 2p integers and contains two representatives e1 < e2 = e1 + p.
With e* := U+ - U-, |e| + 2J = a - |e - e*| (direct check for e >= 0 and e < 0), so top(e) = R - |e - e*|, R = p + 2kappa^.
Every representative lies in [-U-, U+], and e* lies there too; the one closer to e* has |e - e*| <= p - 1 (if e* is between
them the distance is <= (p-1)/2; otherwise both lie on one side within the 2p-window, the nearer at distance <= p - 1), so
top(e) >= 2kappa^ + 1.  If |e| <= 2kappa^, the window contains 2kappa^ (even, <= 2p - 2).  If 2kappa^ < |e| <= 2p - 3, it
contains |e| and |e| + 1 (top(e) >= |e| + b >= |e| + 2).  If |e| = 2p - 2 it is even.  If |e| = 2p - 1 then {U+, U-} =
{2p - 1, 0}, e = e*, and the other representative e' (|e'| = p - 1, J = 0) gives the sizes [p - 1, p - 1 + b] = [p - 1, 2kappa^],
containing 2kappa^.  []

## 4. Proof of Theorem ROT-KP+

w^ as in proof-FB-v1.md Sec. 4: k = p odd blocks, (ZP) at kappa^ (GRX), kappa^ <= p - 1 (DAV), R = p + 2kappa^, (S1) at
kappa^.  If kappa^ = 1: ROT-KP (accepted).  Let kappa^ >= 2 and let 2t be the length of a longest zero-sum of Y.
- t <= kappa^ - 1: Theorem ROT-FB (b) (candidate).
- t = kappa^: take any longest Z; Y' := Y - Z has length p, is zero-sum-free, and is SC by Import S(p), with an odd
  generator g = Y(c), c != 0.  (ZP) excludes zero-sums of length 2p (2kappa^ + 2 <= 2p).  Lemma FB-p applies.
  Case (X): the rotation multiset is rho_c^(p-1+n+) rho_0^(1+q) with Z = g^(n+)(pg)^q, n+ + q = 2kappa^ and n+ + pq = 0
  (mod 2p): q even forces n+ = 0, q = 2kappa^ (family X1); q odd forces n+ = p, q = 2kappa^ - p >= 1 (family X2).  Lemma
  ARC0 contradicts avoidance.
  Case (N): t >= 1 and balance give n+ = S(N) >= n- >= 1; W + n+ <= 2p - 1 gives e' := W - p <= p - 1 - n+ <= p - 2, so
  e' <= p - 3 (e' even) and every a_i <= p - 2; every s_i <= slack = p - 1 - e' gives s_i <= p - 2.  So every rotation has
  SHgen weight a_i, 1 or -s_i with |b| <= p - 2 (no rho_0) and
      E = e' + n+ - n- <= (p - 1 - n+) + n+ - n- = p - 1 - 2kappa^ + n+.
  If E = 0 the rotations lie in {rho_c, rho_-c}.  Otherwise eta >= 1:
  (H) n+ <= 2p - 1 - W <= p - 1 gives E <= 2p - 2 - 2kappa^ = 2H.
  (K) needs eta + a_max <= 2p - 1 - k = p - 1.  If eta >= 2: E >= (a_max - 1) + 2(eta - 1) gives eta + a_max <= E + 1 <=
  p - 2kappa^ + n+ <= p - 1 (n+ <= 2t - 1 = 2kappa^ - 1).  If eta = 1: eta + a_max = E + 2 <= p + 1 - 2kappa^ + n+, which is
  <= p - 1 unless n+ = 2kappa^ - 1, i.e. n- = 1 and s_1 = 2kappa^ - 1 >= 3; then s_1 is the only heavy, so e' = 0, Y' = g^p
  and Y contains g^(p + 2kappa^ - 1); (ZP) excludes g^(2p), so 2kappa^ <= p, and eta + a_max = 1 + s_1 = 2kappa^ <= p - 1
  (p odd).
  Theorem SHgen or Lemma SHgen-E contradicts avoidance; the k = p caller scope is that of the accepted ROT-KP verdict
  (run of 2026-10-16, review/olson-rotkp-parent-verdict-v1.md, sha256 dfb2fd0bdd05ae33a02b41fec318823115384ce7126758d27fe837a6e3bbfcf3: SHgen has no hidden
  k <= p - 1 restriction; SHgen-E base words keep k = p and o_F(u°) <= k = p inside restricted REFL-few-odd; the (K)
  equality case is allowed) with ZX overlay 4 (generalized ZS v2 overlay V3), as in evidence/proof-FB-v1-erratum-1.md R1.
So E = 0 and the rotations of w (= those of w^) lie in one nonzero pair.  []

## 5. Proof of the Corollary

o := o_F <= p, kappa(w) <= floor(2p/3).  Every admissible normal form has 1 <= k <= o, k = o (mod 2), kappa^ <= kappa(w).
k = 1: K1.  2 <= k <= p - 1: Corollary FB's case analysis (K01 for kappa^ <= 1, ROT-FB (a) otherwise).  k = p (o = p):
ROT-KP (kappa^ <= 1) or Theorem ROT-KP+ (kappa^ >= 2; (S1) by S1-sharp).  Restricted REFL (o <= p) gives INV*.  Ledger as
in Corollary FB (Case 1 uses o <= p <= 2p - 3; Cases 2, 3 do not decrease F - o and do not increase o).  []

## 6. Scope

- Relative to Import S(p) (evidence/import-Sp-XiaYuan-v1.md): a classical corollary at that note's trust level (Xia-Yuan's
  primary text not read; statement via Peng-Sun's restatement).  Finite checks of S(p) (lane probe v13, p <= 17; parent
  control, p <= 11) are not premises.
- Unconditional new content: Lemma FB-p and Lemma ARC0 (written, unreviewed).
- Remaining rotation residual within terminal k <= p, after ROT-FB and ROT-KP+ (relative to Import S(p)): kappa^ >= floor(2p/3) + 1 with
  (S1) failing at kappa^.  Terminal k >= p + 1 and the reflection half o_F > p remain open.
- Limits: written mathematics; no Lean, no human review, no literature search; a search miss is never novelty evidence.
