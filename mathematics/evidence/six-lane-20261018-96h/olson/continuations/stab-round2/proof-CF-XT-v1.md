# Lemma CF (coefficient form of (ZP_kappa) / long zero-sums) and Lemma XT (all <= 3-term (ZP_kappa)-extensions of
# E2(kappa - 1), E3(kappa - 1)), v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T04:45:10-0700.  Status: CANDIDATE, written proofs [W],
UNREVIEWED.  Scope: STAB2-scope-v1.md (c98182632eb9ef39904c43ef75815919b56142ade2137f30c5d99482dcaa4e89), items (A), (B).  No computation; no
import beyond elementary arithmetic of Z_(2p).  LS, LS+, STAB are NOT assumed.  No novelty claim; no Lean.

## 0. Notation
p >= 5 prime; odd elements of Z_(2p); e := p - kappa.  (ZP_kappa): no zero-sum subsequence of length in [2kappa + 2, 2p] =
[2p - 2e + 2, 2p].  A zero-sum is long if its length is >= 2kappa + 2 (under (ZP_kappa): >= 2p + 2).  Sub-multisets are
occurrence sub-multisets.  An odd generator is an odd element of order 2p, i.e. every odd element except p.  For an odd
generator g, every odd x equals c_x g for a unique odd c_x in [1, 2p - 1] (c -> cg is a bijection of Z_(2p) preserving
parity).  For h a generator: E2(k) := h^(3k-p+2) (3h)^(p-1), E3(k) := h^(3k-2p+2) (3h)^(2p-1) (when the exponents are >= 0).

## 1. Lemma CF
Let Y be a sequence of odd elements and g an odd generator; M := v_g(Y), delta0 := 2p - M; R := Y with all copies of g
removed; for x in R, mu_x := (c_x - 1)/2 in [1, p - 1]; U := (mu_x)_(x in R) (a multiset, |U| = |R| = |Y| - M); for W <= U,
sigma(W) := sum of its mu (an integer) and |W| its size.
(a) Y satisfies (ZP_kappa) iff M <= 2p - 1 and
    (F) no W <= U with rho := sigma(W) mod p <= e - 1 and delta0 <= |W| + 2rho <= 2p.
(b) If M <= 2p - 1, Y has a zero-sum of length >= 2p + 2 iff
    (L) there are W <= U and an integer j >= 1 with p | sigma(W) + j, sigma(W) + j >= p, and delta0 + 2j <= |W| <= 2p + 2j;
    the zero-sum then has length 2p + 2j.
(c) |Y| <= 3kappa + 1 iff |U| <= p - 3e + 1 + delta0;  |Y| <= p + 2kappa iff |U| <= p - 2e + delta0.
Proof.  If M >= 2p, g^(2p) is a zero-sum of length 2p in the window; so assume M <= 2p - 1.  A subsequence is g^i W
(0 <= i <= M, W <= R identified with a sub-multiset of U); its sum is (i + A_W) g with A_W := sum of c_x = |W| + 2sigma(W),
and its length is i + |W|.  It is a zero-sum iff i + A_W = 2pk for an integer k >= 0; as 0 <= i <= M < 2p, for given W
there is at most one such i, namely i = 2pk - A_W with k = ceil(A_W/(2p)), and it exists iff 2pk - A_W <= M.  So the
zero-sums are exactly the pairs (W, k) with 2pk - M <= A_W <= 2pk, of length 2pk - A_W + |W| = 2pk - 2sigma(W).
(a) The length lies in [2p - 2e + 2, 2p] iff sigma(W) lies in [p(k - 1), p(k - 1) + e - 1] (k >= 1 then).  Write q := k - 1,
rho := sigma(W) - pq in [0, e - 1] (so rho = sigma(W) mod p, as e - 1 < p); then A_W = |W| + 2pq + 2rho and
2pk - M <= A_W <= 2pk iff delta0 <= |W| + 2rho <= 2p.  Conversely any W as in (F) gives the zero-sum (W, q + 1) of length
2p - 2rho in the window.
(b) Length 2pk - 2sigma(W) >= 2p + 2 iff sigma(W) = p(k - 1) - j with j >= 1; then A_W = |W| + 2p(k - 1) - 2j and
2pk - M <= A_W <= 2pk iff delta0 + 2j <= |W| <= 2p + 2j; the length is 2p + 2j.  Conversely such (W, j) gives k :=
(sigma(W) + j)/p + 1 >= 2.
(c) |Y| = M + |U| = 2p - delta0 + |U|, 3kappa + 1 = 3p - 3e + 1, p + 2kappa = 3p - 2e.  []
Instances (used below; direct from the definitions).  E2(k) with g = h: delta0 = 2p - (3k - p + 2), U = 1^(p-1).  E3(k)
with g := 3h (a generator, p != 3): v_g = 2p - 1, delta0 = 1, U = (mu*)^(3k-2p+2), where h = c* g with c* = 3^(-1) mod 2p and
mu* = (c* - 1)/2 satisfies 3mu* = -1 (mod p) (from 3(2mu* + 1) = 1 (mod 2p)).

## 2. Lemma XT
Let p >= 7 prime, kappa0 + 1 <= kappa <= p - 2 (kappa0 := floor(2p/3); so 2 <= e and 3e <= p - 1), h a generator, and
Z a sequence of at most three odd elements.
(i) E2(kappa - 1) Z satisfies (ZP_kappa) iff Z is one of: empty, h, -h, -3h, h^2, h(-h), h^3.
(ii) If kappa >= kappa0 + 2, E3(kappa - 1) Z satisfies (ZP_kappa) iff Z is one of the same seven sequences.
In particular the only three-term (ZP_kappa)-extensions are E2(kappa - 1) h^3 = E2(kappa) and E3(kappa - 1) h^3 = E3(kappa).
(p >= 7 because the kappa-range is empty at p = 5.)
Proof.  (ZP_kappa) passes to subsequences, so a Z of length t is admissible only if all its subsequences are; we classify
lengths 1, 2, 3 in turn and in each step only test the sub-multisets W of U that contain all added non-g terms (the others
were tested at a smaller length).  E2(kappa - 1) and E3(kappa - 1) satisfy (ZP_(kappa-1)) (Lemma TV's E2/E3 computation at
kappa - 1; re-derived for the base below), hence (ZP_kappa).
(i) Take g = h.  E2(kappa - 1) has v_h = 3(kappa - 1) - p + 2 = 2p - 3e - 1, so delta0 = 3e + 1, U = 1^(p-1).  Base: W = 1^w,
sigma = w <= p - 1; rho = w only if w <= e - 1, and then |W| + 2rho = 3w <= 3e - 3 < delta0: (F) holds.  Adding h lowers
delta0 by one and does not change U; adding x = c h with c >= 3 adds mu := (c - 1)/2 to U.
- One term x, mu in [1, p - 1].  The new sets are W = 1^w {mu}, 0 <= w <= p - 1, sigma = w + mu in [mu, mu + p - 1].  For each
  rho in [0, e - 1] there is exactly one such W with sigma = rho (mod p): w = rho - mu if rho >= mu (then |W| + 2rho =
  3rho - mu + 1 <= 3e - 3 < 3e + 1: harmless), and w = p + rho - mu if rho < mu (then |W| + 2rho = p + 1 + 3rho - mu <= 2p).
  So x is forbidden iff some rho in [0, min(e - 1, mu - 1)] has p + 1 + 3rho - mu >= 3e + 1.  For mu <= e - 1 take
  rho = mu - 1: 2mu >= 3e + 3 - p holds as 3e + 3 - p <= 2.  For mu >= e take rho = e - 1: forbidden iff mu <= p - 3.
  Hence the admissible one-term Z are h (delta0 = 3e: base check 3w <= 3e - 3 < 3e), and mu in {p - 2, p - 1}, i.e.
  c in {2p - 3, 2p - 1}: x = -3h or -h.
- Two terms from {h, -h, -3h}.  Write mu = p - 1 for -h and p - 2 for -3h.  The sets to test are W = 1^w plus the added
  non-g terms, 0 <= w <= p - 1.
  h^2: delta0 = 3e - 1, U unchanged: 3w <= 3e - 3: admissible.
  h(-h): delta0 = 3e; W = 1^w {p - 1}: sigma = p + (w - 1), rho = w - 1 <= e - 1 iff 1 <= w <= e, |W| + 2rho = 3w - 1 <= 3e - 1
  < 3e (w = 0 gives rho = p - 1 >= e): admissible.
  h(-3h): delta0 = 3e; W = 1^(e+1) {p - 2}: sigma = p + e - 1, |W| + 2rho = e + 2 + 2e - 2 = 3e: forbidden.
  (-h)^2: delta0 = 3e + 1; W = 1^(e+1) {p - 1}^2: sigma = 2p + e - 1, |W| + 2rho = e + 3 + 2e - 2 = 3e + 1: forbidden.
  (-h)(-3h): W = 1^(e+2) {p - 1, p - 2}: sigma = 2p + e - 1, |W| + 2rho = e + 4 + 2e - 2 = 3e + 2 >= 3e + 1: forbidden.
  (-3h)^2: W = 1^(e+3) {p - 2}^2: sigma = 2p + e - 1, |W| + 2rho = 3e + 3: forbidden.
  (In each forbidden case w <= e + 3 <= p - 1 and |W| + 2rho <= 2p, as 3e <= p - 1, p >= 7.)
- Three terms: every two-term subsequence must be h^2 or h(-h); so Z is h^3 or h^2(-h).  h^3: delta0 = 3e - 2, 3w <= 3e - 3:
  admissible (this is E2(kappa)).  h^2(-h): delta0 = 3e - 1; W = 1^e {p - 1}: sigma = p + e - 1, |W| + 2rho = 3e - 1: forbidden.
(ii) Take g := 3h, mu* as in Sec. 1, n := 3(kappa - 1) - 2p + 2 = p - 3e - 1; kappa >= kappa0 + 2 gives 3kappa >= 2p + 4, so n >= 3.
E3(kappa - 1) has delta0 = 1, U = (mu*)^n.  Adding g is impossible (M = 2p gives g^(2p)).  With delta0 = 1, (F) says: no
NONEMPTY W with sigma(W) mod p in [0, e - 1] (every |W| here is <= n + 3 <= p, so |W| + 2rho <= 2p).  Multiply by -3 (an
automorphism of Z_p): put nu(x) := -3 mu_x mod p, so nu = 1 for every term of U; the forbidden condition becomes
nu(W) := sum of nu over W in Phi := {0, -3, -6, ..., -3(e - 1)} (mod p), whose nonzero elements, as integers in [1, p - 1], are
p - 3, ..., p - 3e + 3 = n + 4.
- One term x with nu := nu(x) in [1, p - 1] (nu = 0 would be mu = 0, i.e. x = g).  The sets W = (mu*)^t {x}, 0 <= t <= n, have
  nu(W) = t + nu.  So x is forbidden iff nu in {phi - t : phi in Phi, 0 <= t <= n}; as n >= 2 the intervals
  [-3rho - n, -3rho] (rho = 0, ..., e - 1) overlap consecutively, and their union is [-(3e - 3 + n), 0] = [-(p - 4), 0], i.e.
  every residue except 1, 2, 3.  So x is admissible iff nu(x) in {1, 2, 3}.  Translating (h = c* g; an element with
  g-coefficient c has h-coefficient 3c mod 2p): nu = 1 is mu = mu*, x = h; nu = 3 is mu = p - 1 (as -3(p - 1) = 3), x = -g =
  -3h; nu = 2 is mu = 2mu* (mod p), c = 2c* - 1, h-coefficient 6c* - 3 = -1, x = -h.
- Two and three terms.  Adding a copies of h, b of -h, c of -3h gives the nu-multiset 1^(n+a) 2^b 3^c with n + a >= 2 ones, whose
  nonempty sub-multiset sums are exactly the integers in [1, n + a + 2b + 3c] (adding an element v <= S + 1 to a multiset whose
  sums fill [0, S] makes them fill [0, S + v]; start from 1^(n+a), S = n + a >= 2).  All of these are < 2p (n + a + 2b + 3c <=
  n + 9 < 2p), so a forbidden sum is an integer = 0 or in {p - 3, ..., n + 4} (mod p) inside [1, n + a + 2b + 3c]; the
  least such is n + 4.  Hence Z = h^a (-h)^b (-3h)^c is admissible iff a + 2b + 3c <= 3: for |Z| = 2 exactly h^2, h(-h); for
  |Z| = 3 exactly h^3 (= E3(kappa)).  []
Remark.  For kappa = kappa0 + 1 (n in {0, 1}), E3(kappa - 1) = E3(kappa0) has no long zero-sum (it has no zero-sum of length
> 2kappa0, by S1-sharp or directly), so (ii) is not needed there.  Similarly E2(kappa0) has no long zero-sum.

## 3. Consequence (conditional; nothing assumed)
TR(p, kappa) (three-occurrence transversal, OPEN): every (ZP_kappa) sequence Y of length 3kappa + 1 with a long zero-sum has
three occurrences whose deletion leaves a sequence with a long zero-sum and no zero-sum of length 2kappa.
Proposition.  Let kappa0 + 2 <= kappa <= p - 2.  STAB(p, kappa - 1) and TR(p, kappa) imply STAB(p, kappa).
Proof.  Y as in TR; delete the three occurrences: V has length 3(kappa - 1) + 1, satisfies (ZP_(kappa - 1)) (no zero-sum of
length 2kappa, and (ZP_kappa)) and has a long zero-sum (length >= 2p + 2 >= 2(kappa - 1) + 2), so by STAB(p, kappa - 1),
V = E2(kappa - 1) or E3(kappa - 1) for some generator h; Y = V Z with |Z| = 3 satisfies (ZP_kappa), so Lemma XT gives
Z = h^3 and Y = E2(kappa) or E3(kappa).  []
The base kappa = kappa0 + 1 of such an induction is not covered by this Proposition.
