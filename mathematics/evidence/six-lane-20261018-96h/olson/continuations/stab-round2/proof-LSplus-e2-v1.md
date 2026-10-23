# Lemma CT (complement multiplicity bound) and Theorem LS+2: LS+(p, p - 2) for every prime p >= 7, v1

Owner OlsonSTABSuccessor (Slice A).  Written after /bin/date 2026-10-19T05:46:13-0700.  Status: CANDIDATE, written proof [W], UNREVIEWED.
Dependencies (exact):
- Lemma RS(a) of proof-ROW-v1.md (a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; Cauchy-Davenport; scope 'any prime p, 1 <= n <= |S|', as accepted in
  the Codex prerequisite review run review/olson-CFXT-ROW-LSII-codex-v1.prompt.stdout.txt d049d531...b9e9 -- a model review, not a parent verdict).
- Lemma CF (a), (b) of proof-CF-XT-v1.md (aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f) read with erratum-1-CF-XT-ROW-range.md E1 (767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7).
- Parent-accepted Theorem SLZ3 (review/olson-SLZ3-parent-verdict-v1.md 2b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24) -- only for the reduction to length 3p - 4.
- The index-one theorem exactly as in the parent import record (run of 2026-10-16, review/olson-index-one-primary-statement-parent-
  v1.md, e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6), used with n = p prime.
Not used: Lemma AP/AP', DGM-p, LS-II, LS-small, TV, MAX, RED+, SHIFT, any LS/LS+/STAB hypothesis.  No computation.

## 1. Lemma CT
Let p >= 5 be prime, kappa an integer with 0 <= kappa <= p - 1, Y an odd sequence over C_(2p) with (ZP_kappa), and n an integer with
1 <= n <= |Y|, |Y| - n even and 2kappa + 2 <= |Y| - n <= 2p.  Then sum_x min(n, v_x(Y)) <= p + n - 2 (sum over distinct odd x).
Proof.  Write odd elements as (1, a) in C_2 x C_p; a -> (1, a) is a bijection, so the C_p-coordinate sequence A has the same
multiplicities as Y.  If an n-term subsequence S of Y had sigma_p(S) = sigma_p(Y), then Y - S would have even length |Y| - n and
C_p-sum 0, i.e. it would be a zero-sum of length in [2kappa + 2, 2p].  So sigma_p(Y) is not in Sigma_n(A), |Sigma_n(A)| <= p - 1,
and RS(a) gives min(p, sum_x min(n, v_x) - n + 1) <= p - 1.  []

## 2. Theorem LS+2
Let p >= 7 be prime and kappa := p - 2 (so floor(2p/3) + 1 <= kappa <= p - 2).  Every odd sequence Y over C_(2p) with no zero-sum
of length 2p - 2 or 2p ((ZP_(p-2))) and a zero-sum of length >= 2p + 2 has |Y| <= 3p - 5 = 3kappa + 1.
Sharpness.  E2(p - 2) = h^(2p-4) (3h)^(p-1) and E3(p - 2) = h^(p-4) (3h)^(2p-1) (h any odd generator) have length 3p - 5, satisfy
(ZP_(p-2)) (CF instances, Sec. 4) and contain the long zero-sums h^(p+3) (3h)^(p-1) resp. h^3 (3h)^(2p-1) of length 2p + 2
(p + 3 <= 2p - 4 and 3 <= p - 4 as p >= 7; coefficient sums 4p resp. 6p).

## 3. Proof
Step 0 (length 3p - 4).  Suppose |Y| >= 3p - 4.  A shortest long zero-sum T of Y has |T| <= 3kappa + 1 = 3p - 5 (SLZ3, kappa <= p - 1),
so some Y' with T <= Y' <= Y and |Y'| = 3p - 4 exists; Y' satisfies (ZP_(p-2)) and has the long zero-sum T.  Replace Y by Y'.
Step 1 (CT).  n := p - 2: |Y| - n = 2p - 2 is even and in [2kappa + 2, 2p] = [2p - 2, 2p].  Lemma CT: sum_x min(p - 2, v_x) <= 2p - 4,
so sum_x (v_x - min(p - 2, v_x)) >= (3p - 4) - (2p - 4) = p.  Hence either (one) exactly one value x0 has v_(x0) >= p - 1, and then
v_(x0) >= (p - 2) + p = 2p - 2; or (two) at least two values have multiplicity >= p - 1: they contribute 2(p - 2) = 2p - 4 to the
truncated sum, so no third value occurs at all, and Y = x0^(v0) x1^(v1) with v0 + v1 = 3p - 4, v0, v1 >= p - 1.
Step 2 (case two).  Write x0 = (1, alpha), x1 = (1, beta), alpha != beta.  A subsequence x0^i x1^j with i + j = 2p has C_p-sum
2p alpha + j(beta - alpha) = j(beta - alpha), zero iff p | j; so v0, v1 >= p would give the zero-sum x0^p x1^p of length 2p.  Hence
{v0, v1} = {p - 1, 2p - 3}; say v1 = p - 1, v0 = 2p - 3 (the other labelling is symmetric).  A subsequence x0^i x1^j with
i + j = 2p - 2 has C_p-sum (2p - 2)alpha + j(beta - alpha) = j(beta - alpha) - 2alpha; let j0 in [0, p - 1] be the residue of
2alpha/(beta - alpha).  If j0 >= 1, then j := j0 <= p - 1 = v1 and i := 2p - 2 - j0 is in [p - 1, 2p - 3], i <= v0: a zero-sum of
length 2p - 2.  So j0 = 0, alpha = 0: x0 = (1, 0) is the involution and x1 a generator.  Then a zero-sum x0^i x1^j has
j beta = 0 (mod p) with j <= p - 1, so j = 0 and its length i is even and <= 2p - 3, hence <= 2p - 4: no long zero-sum.  Contradiction.
Step 3 (case one).  v_(x0) >= 2p - 2.  x0 is not the involution ((1, 0)^(2p-2) would be a zero-sum of length 2p - 2), so x0 =: g is a
generator, and v_g <= 2p - 1 (g^(2p)).  Lemma CF w.r.t. g: M = v_g in {2p - 2, 2p - 1}, delta0 = 2p - M in {1, 2}, U of size
r = 3p - 4 - M = p - 4 + delta0 in {p - 3, p - 2}, e = 2.
(A) U is zero-sum-free over Z_p and no subsequence of U has sum = 1 (mod p).  Indeed a nonempty W <= U with rho(W) in {0, 1} has
    |W| + 2rho(W) >= 2 >= delta0 (rho = 0 forces |W| >= 2, the terms being nonzero mod p) and |W| + 2rho(W) <= r + 2 <= p <= 2p,
    which CF (F) forbids.
(B) U (-sigma(U)) is a minimal zero-sum sequence over C_p (-sigma(U) != 0; a proper nonempty zero-sum subsequence, or its
    complement, would be a nonempty zero-sum of U) of length r + 1 >= p - 2 >= floor(p/2) + 2 (p >= 7).  By the index-one theorem
    there are a != 0 in Z_p and integers x_u >= 1 (u in U) with u = x_u a and S := sum_(u in U) x_u <= p - 1.
(C) Every integer in [0, S] is a sum of a sub-multiset of (x_u).  Sort x_1 <= ... <= x_r.  If x_k > 1 + sum_(i<k) x_i for some k, then
    x_i >= k + 1 for i >= k and S >= (k - 1) + (r - k + 1)(k + 1) >= 2r (the middle expression is concave in k and equals 2r at k = 1
    and k = r) >= 2p - 6 >= p + 1 (p >= 7), contradicting S <= p - 1.  So x_k <= 1 + sum_(i<k) x_i for all k, and the standard
    induction gives every integer in [0, S].
(D) If a^(-1) mod p (in [1, p - 1]) were <= S, the sub-multiset with x-sum a^(-1) mod p would have sum 1 (mod p), against (A).  So
    a^(-1) mod p is in [S + 1, p - 1] <= [p - 2, p - 1] (S >= r >= p - 3): a^(-1) = -1 or a^(-1) = -2.
(E) No long zero-sum.  By CF (b) (M <= 2p - 1) a zero-sum of length >= 2p + 2 needs W <= U and an integer j >= 1 with
    p | sigma(W) + j and |W| >= delta0 + 2j.  Then rho(W) != 0 (else j >= p and |W| >= 2p > r), j >= p - rho(W), so
    |W| + 2rho(W) >= 2p + delta0.  Let s := sum of x_u over W, an integer in [|W|, S] <= [1, p - 1]; rho(W) = (s a mod p).
    a = -1: rho(W) = p - s and |W| + 2rho(W) <= s + 2p - 2s = 2p - s < 2p + delta0.
    a = -1/2: for s even rho(W) = p - s/2 and |W| + 2rho(W) <= 2p; for s odd rho(W) = (p - s)/2 and |W| + 2rho(W) <= p.
    In both cases |W| + 2rho(W) < 2p + delta0: no long zero-sum.  Contradiction.
Hence no Y as in Step 0 exists.  []

## 4. Sharpness verification (CF instances)
E2(k) w.r.t. g = h: delta0 = 2p - (3k - p + 2) = 3e - 2, U = 1^(p-1); W = 1^w has rho = w; rho <= e - 1 forces |W| + 2rho = 3w <= 3e - 3
< delta0: (F) holds.  E3(k) w.r.t. g = 3h: delta0 = 1, U = (mu*)^(p-3e+2) with -3mu* = 1 (mod p); W = (mu*)^t (1 <= t <= p - 3e + 2)
has -3rho(W) = t (mod p), and rho in [0, e - 1] would need t in {0, p - 3, ..., p - 3e + 3} (mod p), impossible: (F) holds.  At
k = p - 2, e = 2.  (The long zero-sums are exhibited in Sec. 2.)

## 5. Scope
Exactly kappa = p - 2, every prime p >= 7 (p = 7: kappa = 5 = floor(2p/3) + 1, also covered by BASE1).  Sequence level only.  This
is LS+ at e = 2; it implies LS(p, p - 2) independently of LS-small.  STAB(p, p - 2) (classification at length 3p - 5) is NOT claimed
here.  No INV*, ordered-Olson, novelty, Lean or human-review claim.
