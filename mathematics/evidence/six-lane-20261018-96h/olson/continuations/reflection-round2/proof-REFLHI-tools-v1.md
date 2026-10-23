# Reflection half for o_F > p: frozen target, exact residual, Cauchy-Davenport toggle lemma (candidate v1)

Owner OlsonReflectionSuccessor (Slice B of review/olson-two-slice-successor-brief-v1.md).  Written after host clock
2026-10-19T04:59:36-0700.  Status: CANDIDATE_UNVERIFIED, written research only, no computation, no model review.
Scope: words of length 4p - 2 over D_(2p) whose rotation letters lie in one pair {rho_x, rho_-x}, x != 0.  Nothing here
concerns rotation values, INV*(p) as a whole, ordered Olson, Lean, novelty or priority.

Path abbreviations.  REFL/ := mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/;
R16/ := institute/runs/six-lane-2026-10-16/review/; R18/ := institute/runs/six-lane-2026-10-18-96h/review/.

## 0. Imports (parent-accepted, used at their exact scopes; hashes re-checked 2026-10-19 03:5x PDT)

* (H0) Lemma H0 of REFL/proof-K0star-r2.md (sha256 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1),
  L55-65, accepted in R16/olson-reflection-K0star-RED-parent-verdict-v1.md (879aeee7...c02a) as algebra on the accepted GRX.
  It holds for every cyclic constant-block representation of any length (its proof never uses the length or r_i >= 1).
* (RED) Theorem RED and its proof, REFL/proof-RED-r2.md (c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7),
  same verdict, with its imports (I1)-(I4), K0*, K1*, SING, KB*, CAP, KBH*, TII, QQ at their accepted scopes.
* (SMALLK) R16/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf4...13b8): RES_<(p) has no avoider with k <= p.
* (FEW) Corollary REFL-few-odd, REFL/proof-REFL-fewodd-r5.md (4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363;
  verdict R16/olson-refl-fewodd-parent-verdict-v1.md binds r4 1e447754...861d; r5 is errata-only) and its Claim MON.
* (CD) Cauchy-Davenport (classical): for nonempty A_1, ..., A_s in Z_p (p prime),
  |A_1 + ... + A_s| >= min(p, |A_1| + ... + |A_s| - s + 1).
No finite computation is used.  No rotation-rigidity, INV*, SLZ3 or unreviewed documentation successor (RED-r3, K0star-r3)
is used.

## 1. Frozen target and exact residual

**REFL-HI(p).**  Let p >= 5 be prime and w0 an avoider (no increasing-index identity 2p-subword) of length 4p - 2 over
D_(2p) whose rotation letters lie in one set {rho_x, rho_-x}, x != 0, with o_F(w0) >= p + 1, where o_F counts the ODD
blocks of the maximal cyclic CONSTANT reflection-block decomposition (not maximal reflection runs).  Then every maximal
cyclic reflection run of w0 is constant.
REFL(p) (frozen in REFL/README.md L17-19) is the conjunction of (FEW) and REFL-HI(p).

**RES-HI(p)** := no avoider in RES_<(p) (RED-r2 L132-133) with kappa >= 2 and k >= p + 1.
**Lemma 1.1.**  RES-HI(p) implies REFL-HI(p); hence RES-HI(p) implies REFL(p).
Proof.  If REFL(p) fails, the proof of Theorem RED (RED-r2 L136-164) turns the violating word into an avoider of RES_<(p)
with kappa >= 2 (its terminal state); by (SMALLK) that avoider has k >= p + 1, contradicting RES-HI(p).  []
Remark.  Claim MON of (FEW) shows k(terminal) <= o_F(w0); the converse inequality is false in general, so RES-HI(p) is
needed for every w0 with o_F(w0) >= p + 1, and also for no other w0.  Restricted versions of RES-HI transfer to w0 only
through the move bookkeeping of RED (P1, P2 keep R, B; P3 keeps R, B, kappa; P4 lowers R by 2, B and kappa by >= 1).

Exact parameters of a word w of RES-HI type (normalised x = 1, A >= B; notation of K0star-r2 Sec. 0): all k maximal
constant blocks odd (o_F = k, beta(P) = 0 for every pattern P), every run pure (a_t b_t = 0) or empty, g_E >= 1 empty runs
(each genuine), 0 <= B < kappa, kappa >= 2, k >= p + 1, and
   R = A + B = 2p - k + 2 kappa,   D = A - B = 2p - k + 2g,   g := kappa - B >= 1,
   A <= 2p - 1 (else rho_1^(2p)),   e_R <= 2 kappa (P0 with e_F = 0; empty runs count as even runs).            (1.1)
(Here g is kappa - B, the notation of MXG-r2; the number of empty runs is written g_E.)

## 2. Two exact reformulations

**Lemma RW (reduced word).**  Let w be any word over D_(2p) cut into maximal constant reflection blocks of lengths
l_i = 2h_i + e_i (e_i in {0, 1}) and rotation runs, H = sum h_i.  Let w_red be obtained by deleting 2h_i letters from each
block (keeping one letter of each odd block and none of each even block).  Then w has an identity 2p-subword iff w_red has
an identity subword of even length L with 2p - 2H <= L <= 2p.
Proof.  If T is an identity 2p-subword of w, it selects c_i letters of block i; these are consecutive in the selection,
all equal, so removing floor(c_i/2) adjacent equal pairs from each block's selected letters (they multiply to 1) leaves the
product unchanged and gives a selection with c_i mod 2 <= e_i letters of block i (an even block has c_i mod 2 = 0
selected after removal? no: c_i mod 2 can be 1 for an even block; then keep one letter, which exists in w_red only if
e_i = 1).  See the correction in the next sentence.  Precisely: an even block contributes, in any identity selection, an
even or odd number of letters; if odd, its single remaining letter is not present in w_red.  So Lemma RW is stated and used
below ONLY for words all of whose blocks are odd (then every block keeps one letter in w_red): in that case the
reduced selection lies in w_red, has length 2p - 2j with j = sum floor(c_i/2) <= H, and is an identity subword.
Conversely an identity subword of w_red of even length 2p - 2j, 0 <= j <= H, extends to an identity 2p-subword of w by
adding j adjacent equal pairs inside blocks (each block i offers h_i pairs disjoint from its kept letter; inserting a pair
sigma_y sigma_y next to a selected or unselected sigma_y of the same block changes no product).  []
(For all-odd words this is the statement used; it is the identity behind the windows of H0: kappa = p - 1 - H.)

**Lemma W (window table).**  For an all-odd G-word (beta = 0), H0 reads: w avoids iff 0 notin I(empty) (mod p) and for
every proper nonempty pattern P with m = m(P) intervals and D_P = sum_{t in P} d_t,
   u_P notin I(P) = [-G_m(D - D_P), G_m(D_P)] (mod p),   G_m(x) := min(p - m, x - g + m - 1, floor((x + B)/2)),
with g = kappa - B and u_P = 2^(-1) sum_{t in P} theta_t.
Proof.  H0 with beta = 0: lambda(P) - 1 = min(p - m, D_P + B - kappa + m - 1, floor((D_P + B)/2)).  []
Facts used below: G_m(x) is nondecreasing in x; for fixed x it is nondecreasing in m as long as p - m is not the minimum;
empty runs have d_t = 0, so adding or removing empty runs never changes D_P; for an empty run t, u_t != 0 (genuine).

## 3. Lemma TOG (Cauchy-Davenport toggles over empty runs)

Let w be an all-odd G-word (any length, rotations in {rho_1, rho_-1}, F, R >= 1), notation of Lemma W.
A **region** is a nonempty cyclic interval Z of runs all of which are EMPTY.  Fix a proper nonempty pattern P_0 with m_0
intervals and D_0 := D_(P_0), and pairwise disjoint regions Z_1, ..., Z_s, none meeting P_0, such that
 (i) no run of Z_i is cyclically adjacent to a run of Z_j (i != j);
 (ii) each Z_i is either FREE (no run of Z_i is adjacent to a run of P_0) or ATTACHED: Z_i = {e + 1, ..., e + L} with e the
      last run of an interval of P_0 and e + L + 1 notin P_0 (or the mirror image at the first run of an interval);
 (iii) P_0 u Z_1 u ... u Z_s != [k].
Choices: for a free region, either nothing or one cyclic sub-interval of Z_i; for an attached region, the first i runs of
Z_i (mirror: the last i), 0 <= i <= L.  A choice c gives P_c := P_0 u (chosen runs).  Contribution sets:
 A_i := {0} u {u_J : J a nonempty cyclic sub-interval of Z_i} (free),   A_i := {u_(e+1) + ... + u_(e+j) : 0 <= j <= L} (attached).
Let f = number of free regions, m_1 := m_0 + f, and
   G  := min(p - m_1, D_0 - g + m_0 - 1, floor((D_0 + B)/2)),
   G' := min(p - m_1, (D - D_0) - g + m_0 - 1, floor((D - D_0 + B)/2)).
**Lemma TOG.**  If G + G' >= 0 and  1 + sum_(i=1..s) (|A_i| - 1) + (G + G' + 1) >= p + 1,  then w has an identity
2p-subword.
Proof.  For every choice c: (a) P_c is proper (by (iii)) and nonempty; (b) D_(P_c) = D_0, since only empty runs are added;
(c) m(P_c) = m_0 + (number of free regions with a nonempty choice), because a chosen sub-interval of a free region is
separated from P_0 and from every other chosen set by (i), (ii), and an attached choice extends one interval of P_0 without
reaching another interval of P_0 or another region (e + L + 1 notin P_0, and (i)); so m_0 <= m(P_c) <= m_1; (d)
u_(P_c) = u_(P_0) + sum_i a_i with a_i in A_i the contribution of region i (u is additive over runs).  By Lemma W and the
monotonicity facts, for m_0 <= m <= m_1:  G_m(D_0) >= min(p - m_1, D_0 - g + m_0 - 1, floor((D_0 + B)/2)) = G and
G_m(D - D_0) >= G'.  Hence the integer interval W := [-G', G] is contained in I(P_c) for every choice c.  By (CD),
X := u_(P_0) + A_1 + ... + A_s has at least min(p, 1 + sum(|A_i| - 1)) residues, and W has min(p, G + G' + 1) residues.
Their sizes add up to more than p, so X meets W (mod p): some choice c has u_(P_c) congruent to an element of
W subset of I(P_c), and P_c kills (Lemma W), i.e. w has an identity 2p-subword.  []
**Lemma NU (size of contribution sets).**  Let the region's runs be r_1 < ... < r_L (consecutive) and let y^0, y^1, ..., y^L
be the values of the L + 1 blocks bounding them in order (y^(j-1) before run r_j, y^j after it).  Then |A| >= nu(Z) :=
number of distinct values among y^0, ..., y^L, and nu(Z) >= 2.
Proof.  A sub-interval {r_a, ..., r_b} has u = (y^(a-1) - y^b)/2 (telescoping theta).  Attached: the prefixes give
{(y^0 - y^j)/2 : 0 <= j <= L}, of size nu(Z) as 2 is invertible.  Free: A contains 0 and (y^0 - y^b)/2 for 1 <= b <= L, the
same set.  y^0 != y^1 because r_1 is a genuine empty run.  []
So Lemma TOG applies as soon as  sum_i (nu(Z_i) - 1) >= p - 1 - (G + G') (and G + G' >= 0).
