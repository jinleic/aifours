# Theorem ONE-SHORT-LS: (ZP_kappa) implies (S1_kappa) at the exact length p+2kappa (written proof), v1

Owner OlsonAssemblyLS. Written after /bin/date 2026-10-19T10:33:49-0700. Status: CANDIDATE_UNVERIFIED written proof. Scope frozen
BEFORE derivation: ONE-SHORT-LS-scope-v1.md, sha256 2b9cfbcdf66cf43b173aa2f9a43542c906b50e04cbae690a860e3c321dd5b872 (10:17:32).
CONDITIONAL on the statement-level external Lev 2022 Theorem 2 (arXiv:2110.01081v3), used once (Sec. 5) exactly as in G-LS; its
proof is not replayed. No computation, model call, novelty, priority, Lean or human-review claim. No pending narrower candidate is
a premise. The accepted G-LS text is a TEMPLATE only: every step used here is re-derived at the new length, and Sec. 9 lists every
changed constant against the G-LS line numbers.

## 0. Statement, notation, imports

THEOREM ONE-SHORT-LS. Let p >= 7 be prime and kappa an integer with floor(2p/3)+1 <= kappa <= p-2. Every sequence Y of odd
elements of C_(2p) with |Y| = p+2kappa EXACTLY that satisfies (ZP_kappa) satisfies (S1_kappa).

Remarks (no new claim). (i) kappa = p-1 is excluded and false there (scope file; the proof breaks exactly at Lemma DOM, see its
remark). (ii) Together with the accepted G-LS (|Y| >= p+2kappa+1), (ZP_kappa) implies (S1_kappa) for every |Y| >= p+2kappa; this is
a union of two trust classes, recorded only as a remark. (iii) This is sequence level only; nothing about words is asserted.

Notation. e := p-kappa, h := e-1. The kappa-range gives e >= 2 and 3e <= p-1 (p = 1 mod 3) or 3e <= p-2 (p = 2 mod 3); so
p >= 3e+1. C_(2p) = C_2 x C_p; the odd elements are the (1,x); iota := (1,0) is the unique odd element of order 2, and
p*x = iota for every odd x. Zero-sums of odd elements have even length. (ZP_kappa): no zero-sum of length in [2kappa+2, 2p];
(S1_kappa): every zero-sum has length <= 2kappa. Under (ZP_kappa) a zero-sum of length > 2kappa has length >= 2p+2; call it LONG.
All sub-multisets are occurrence sub-multisets. For an odd generator g (every odd element except iota): M := v_g(Y),
d := 2p - M; every other term is x = c_x g with c_x odd in [3, 2p-1]; mu_x := (c_x - 1)/2 in [1, p-1]; U := (mu_x) over the
non-g terms, r := |U|; for W <= U, sigma(W) is the INTEGER mu-sum and rho(W) := sigma(W) mod p in [0, p-1]. Note mu_x = (p-1)/2
iff c_x = p iff x = iota.

Imports (parent-accepted at their ORIGINAL scopes; Sec. 10 gives paths, lines, hashes, verdict items):
- CF(a). p >= 5 prime, integer 0 <= kappa <= p-1, any odd generator: Y satisfies (ZP_kappa) iff M <= 2p-1 and (F): there is no
  W <= U with rho(W) <= e-1 and d <= |W| + 2rho(W) <= 2p.
- CT. p >= 5 prime, 0 <= kappa <= p-1, odd (ZP_kappa) Y, 1 <= n <= |Y| with |Y|-n even in [2kappa+2, 2p]:
  sum_x min(n, v_x(Y)) <= p+n-2.
- ROW. (ZP_kappa), integer 0 <= kappa <= p-1, any odd generator g with r >= d and r+2e-2 <= 2p, K := r-d:
  sum_mu min(K, v_mu(U)) <= p-e-1.
- AP' (standalone admission). Prime p, n >= 1, 3n+2 < p: an (n+1)-term progression with nonzero difference x inside an arc of
  at most 2n+1 consecutive residues of Z_p has x in {1, -1, 2, -2}.
- Lev 2022 Theorem 2 (external, statement level, CONDITIONAL): a zero-sum-free sequence alpha of length n in an abelian group with
  |Sigma_inc(alpha)| < 2n (empty sum included) can be written a_k = x_k a with integers 1 = x_1 <= ... <= x_n,
  x_(k+1) <= x_1 + ... + x_k, Sigma_inc(alpha) = {0, a, ..., (x_1+...+x_n)a}, and x_1+...+x_n < ord(a) for finite order.
NOT imported: RED (it reduces to the threshold length p+2kappa+1, not to p+2kappa); DGM-p (its hypothesis |Y| >= p+2kappa+1 fails;
replaced by Lemma DOM); LS-II' (stated at the threshold length; re-derived in Sec. 4 with new constants); SLZ3 (not needed, Sec. 8
uses |T| <= |Y|); S1-sharp and G-LS (G-LS is the template only). New here: Lemma IP, Lemma DOM, Lemma AP''.

## 1. Lemma IP (involution pairs)

Let p be an odd prime, 0 <= kappa <= p-1 an integer, Y odd over C_(2p) with (ZP_kappa), and T <= Y a zero-sum with |T| >= 2p+2.
Then |T| - v_iota(T) >= 2p+1.
Proof. |T| is even. If v_iota(T) >= |T| - 2p (an even number >= 2), delete |T| - 2p occurrences of iota from T; they sum to
(|T| - 2p) iota = 0, so a zero-sum of length exactly 2p remains. As 2kappa+2 <= 2p, this contradicts (ZP_kappa). []
(The same deletion step occurs inside the accepted proof of CTgen; it is re-proved here, not imported.)
Corollary IP'. If, for an odd generator g with M = v_g(Y), at most 2p-M-1 = d-1 terms of Y equal neither g nor iota, then Y has
no long zero-sum. Proof: a long T has |T| - v_iota(T) <= v_g(T) + (d-1) <= M + d - 1 = 2p-1 < 2p+1, against Lemma IP. []

## 2. Lemma DOM (a dominant generator at length p+2kappa)

Let p, kappa be as in the theorem and Y odd with |Y| = p+2kappa, (ZP_kappa) and a long zero-sum. Then some odd generator g has
2kappa+2 <= M := v_g(Y) <= 2p-1; hence 1 <= d <= 2e-2 and r = |Y| - M = p-2e+d <= p-2.
Proof. Apply CT with n := p-2: 1 <= n <= |Y|, and |Y| - n = 2kappa+2 is even and in [2kappa+2, 2p]. So
sum_x min(p-2, v_x) <= 2p-4. Call x HEAVY if v_x >= p-1; each heavy x contributes p-2 to that sum. The excess
sum_x (v_x - min(p-2, v_x)) >= (p+2kappa) - (2p-4) = 2kappa-p+4 >= 1, so a heavy value exists, and there are at most two
(three would contribute 3p-6 > 2p-4).
Two heavy values x0 != x1. They exhaust the bound, so Y = x0^(v0) x1^(v1), v0+v1 = p+2kappa, v0, v1 >= p-1. If v0, v1 >= p,
x0^p x1^p (sum iota + iota = 0) is a zero-sum of length 2p: forbidden. As v0+v1 is odd, exactly one multiplicity equals p-1; call
that value x1, so v1 = p-1 and v0 = 2kappa+1. Write x0 = (1, alpha), x1 = (1, beta), alpha != beta, and L := 2kappa+2. The
C_p-sum of x0^(L-j) x1^j is L alpha + j(beta - alpha). Let j0 in [0, p-1] with j0 = -L alpha (beta - alpha)^(-1) (mod p). If
j0 >= 1, then j0 <= p-1 = v1 and L - j0 in [2kappa+3-p, 2kappa+1] <= [0, v0], so x0^(L-j0) x1^(j0) is a zero-sum of length
2kappa+2: forbidden. Hence j0 = 0, i.e. L alpha = 0 (mod p). L is even with 4 <= L <= 2p-2, so p does not divide L, and alpha = 0:
x0 = iota. Then a zero-sum x0^i x1^j needs j beta = 0 (mod p) with 0 <= j <= p-1 and beta != 0, so j = 0; it is iota^i of length
<= v0 = 2kappa+1, hence <= 2kappa. No long zero-sum: contradiction.
One heavy value x0. v_(x0) >= (p-2) + (2kappa-p+4) = 2kappa+2, and the other values (all non-heavy) total at most
(2p-4) - (p-2) = p-2. x0 != iota, since iota^(2kappa+2) would be a zero-sum of length 2kappa+2. So g := x0 is an odd generator,
and M <= 2p-1 because g^(2p) is a zero-sum of length 2p. []
Remark. At kappa = p-1 one has L = 2p and the step "p does not divide L" fails; the excluded sequence g^(2p-1)(3g)^(p-1) is
exactly a two-heavy sequence. This is where the endpoint drops out.

## 3. CF form and the dichotomy at length p+2kappa

Suppose, for a contradiction, that Y is a counterexample: |Y| = p+2kappa, (ZP_kappa), and a long zero-sum. Fix g from Lemma DOM
and its CF data. For W <= U, |W| + 2rho(W) <= r + 2h <= (p-2) + (2e-2) <= 2p (as 2e <= p). Hence CF(a) gives
  (1) for every W <= U:  rho(W) <= h  =>  |W| + 2rho(W) <= d-1.
Call W FORBIDDEN if rho(W) <= h and |W| + 2rho(W) >= d; by (1) none exists.
Put K := r-d = p-2e (>= e+1). ROW applies (r >= d, and r+2e-2 <= p+2e-4 <= 2p): sum_mu min(K, v_mu(U)) <= p-e-1. Two values of
multiplicity >= K+1 would give 2K <= p-e-1, i.e. p <= 3e-1, false. So exactly one of:
  (I)  every value of U has multiplicity <= K; then r <= p-e-1, i.e. d <= e-1 = h;
  (II) one value mu1 has multiplicity v1 >= K+1 = p-2e+1; the rest R' of U has s := |R'| <= (p-e-1) - K = e-1, and
       s = r - v1 <= r-K-1 = d-1.

## 4. Case (II) is impossible (LS-II' re-derived at the new constants)

Step 1 (mu1 in {1, -1, 1/2, -1/2}). For t in [d-s, v1] (d-s >= 1), W := mu1^t R' has |W| = t+s >= d, so by (1)
rho(W) = t mu1 + sigma(R') (mod p) is not in [0, h]. With x1 := mu1^(-1) mod p, the e points x1(rho - sigma(R')), 0 <= rho <= h
(an e-term progression with difference x1 != 0), avoid the K+1 = p-2e+1 consecutive residues d-s, ..., v1 (v1 <= r <= p-2), so
they lie in the complementary arc of 2e-1 = 2h+1 residues. AP' with n := h >= 1 (3h+2 = 3e-1 < p): x1 in {1, -1, 2, -2},
i.e. mu1 in {1, -1, 2^(-1), -2^(-1)}. [Threshold G-LS/LS-II used AP on an arc of 2e-2 and got only +-1.]
Step 2 (mu1 is not 1 or 2^(-1)). mu1 = 1: W := mu1^h (v1 >= K+1 > h) has rho = h and |W| + 2rho = 3h >= 2h >= d: forbidden.
mu1 = 2^(-1) = (p+1)/2: put m := min(h, floor(v1/2)) >= 1 and W := mu1^(2m). Then sigma(W) = m(p+1) = m (mod p), rho = m <= h,
and |W| + 2rho = 4m, which is >= 4h >= d if m = h, and >= 2(v1-1) >= 2(p-2e) >= 2e+2 > d otherwise: forbidden.
Step 3 (mu1 is not -2^(-1)). mu1 = -2^(-1) = (p-1)/2 means c = p: the dominant U-value is iota. The terms of Y equal to neither g
nor iota are the s <= d-1 terms of R'. Corollary IP' contradicts the long zero-sum.
Step 4 (mu1 = -1, i.e. -g: shape of R'). For t in [p-h, v1], W := mu1^t has rho = p-t <= h and |W| + 2rho = 2p-t >= 2p-v1 >= p+2
> d: forbidden; hence v1 <= p-e. For R'' <= R' with k := |R''|, phi := sigma(R'') mod p and W := mu1^t R'' (0 <= t <= v1),
sigma(W) = phi - t (mod p):
- if h <= phi <= v1: t := phi-h gives rho = h and |W| + 2rho = k + phi + h >= 1 + 2h > d: forbidden;
- if v1+1 <= phi <= v1+h: t := phi-h in [v1-h+1, v1] gives rho = h and |W| + 2rho >= v1+h+1 >= p-e+1 > d: forbidden;
- if phi <= h-1: t := 0 gives rho = phi, so k + 2phi <= d-1 is required.
(R) For every R'' <= R': sigma(R'') mod p lies in [0, (d-1-|R''|)/2] or in [v1+e, p-1].
With k = 1 (and mu_x != p-1 for x in R'): every x in R' is TINY (mu_x <= (d-2)/2) or NEGATIVE (mu_x in [v1+e, p-2]); for a
negative x, nu := p - mu_x is in [2, p-v1-e], contained in [2, e-1], and x = -c'g with c' = 2nu-1 in [3, 2e-3].
Step 5 (tiny sets). Every tiny R'' <= R' has |R''| + 2sigma(R'') <= d-1 (integer sum), so |R''| <= (d-1)/3. Otherwise take, in
any order, the first prefix with k + 2S_k >= d: k >= 2 (singletons have 1 + 2mu <= d-1), and
S_k <= (d-k)/2 + (d-2)/2 <= d-2 < min(p, v1+e), so S_k is a least residue outside [v1+e, p-1] and (R) gives k + 2S_k <= d-1.
Step 6 (the long zero-sum; LS-II' Step 5' re-derived). Here Y = g^M (-g)^(v1) R'. Let T be a long zero-sum.
(a) While a long zero-sum contains an occurrence of g and one of -g, delete one of each: a zero-sum two shorter remains; from
    length 2p+2 it would have length 2p (forbidden), so it is again long. The final T1 lacks g or lacks -g; without g it lies in
    (-g)^(v1) R', of length <= r <= p-2: impossible. So T1 = g^a W' with W' <= R'.
(b) While the current long zero-sum g^(a') W'' contains a negative x = -c'g with c' <= a', delete x and c' copies of g (a zero-sum
    is removed). The length drops by c'+1 <= 2e-2 from >= 2p+2, so the new length is >= 2p-2e+4 = 2kappa+4: it lies in the
    forbidden window [2kappa+2, 2p] (impossible) or is >= 2p+2. At the end: a long T2 = g^(a') W2, W2 <= R', with a' < c'_x for
    every negative x in W2.
(c) |W2| <= s <= h, so a' >= 2p+2-h = 2p-e+3 > 2e-3 >= c'_x: W2 has no negative term, i.e. W2 is tiny; and
    |W2| = |T2| - a' >= 2p+2-M = d+2 > (d-1)/3, contradicting Step 5.
So case (II) is impossible. []

## 5. Case (I): the core and the few-sums application (Lev, CONDITIONAL)

Now d <= h, and (1) holds. Choose an inclusion-maximal Z0 <= U with sigma(Z0) = 0 (mod p), possibly empty; k := |Z0| <= d-1 by (1).
U' := U - Z0 is zero-sum-free mod p (a nonempty zero-sum in U' could be adjoined to Z0). Put delta' := d-k in [1, h] and
n := |U'| = r-k = p-2e+delta' (>= e+2 >= 4).
  (2) For W' <= U': rho(W') <= h  =>  |W'| + 2rho(W') <= delta'-1   ((1) applied to Z0 u W').
Let t := max(1, floor(delta'/2)), so 1 <= t <= h. No residue in [t, h] lies in A := Sigma_inc(U') (the empty sum 0 included): a
W' representing rho in [t, h] is nonempty and |W'| + 2rho >= 1+2t >= delta' > delta'-1, against (2). Hence
  (3) |A| <= p - (h-t+1) = p-e+t < 2n,  since  2n - (p-e+t) = p-3e+2delta'-t >= p-3e+delta' >= 2.
U' is a nonempty zero-sum-free sequence in C_p with (3); Lev 2022 Theorem 2 (CONDITIONAL) gives a nonzero a in C_p and integers
x_u >= 1 (one of them 1) with mu_u = x_u a (mod p) and
  (4) n <= S := sum_(u in U') x_u < p,  Sigma_inc(U') = {0, a, 2a, ..., Sa}.
Every integer s in [0, S] is the x-sum of an actual occurrence sub-multiset of U': the residue sa is a subsum by (4), and any
realizing sub-multiset has x-sum in [0, S] congruent to s mod p (a is invertible), hence equal to s.

## 6. Pinning the multiplier (new arc length; new exceptional branch)

Let b := a^(-1) mod p. For rho in [t, h] the least representative of rho*b lies in I := [S+1, p-1]: a representative in [0, S]
would put rho in A by (4), and it is nonzero. In particular I is nonempty (S <= p-2) and
  l := |I| = p-1-S <= p-1-n = 2e-1-delta'.            [threshold: 2e-2-delta']
(a) delta' >= 2 (so e >= 3). t = floor(delta'/2), N := h-t >= 1; the N+1 points rho*b (t <= rho <= h) lie in I, with
    l <= 2e-1-2t = 2N+1 and 3N+2 <= 3e-4 < p. AP' gives b in {1, -1, 2, -2}. b = 1: the rho = t point is t, in [1, S]
    (t <= h < n <= S). b = 2: the rho = t point is 2t, in [2, delta'], inside [1, S]. b = -2: the rho = h point is
    p-2h = p-2e+2 <= n <= S. Each contradicts I. So b = -1.
(b) delta' = 1 and e >= 3. t = 1, N := h-1 >= 1; the h = N+1 points rho*b (1 <= rho <= h) lie in I, with l <= 2e-2 = 2N+2 and
    p >= 3e+1 = 3N+7. Lemma AP'' (6.1) gives b in {1, -1, 2, -2}, or N = 1 and b = +-3. b in {1, 2}: the rho = 1 point b is in
    [1, S]. If N = 1 (e = 3, so p >= 11 and S >= n = p-5 >= 6): b = 3 puts the point 3 in [1, S]; b = -3 puts the rho = 2 point at
    p-6 < p-4 <= S+1. b = -2: the points p-2rho (1 <= rho <= h) lie in I iff p-2h >= S+1, i.e. S <= p-2e+1 = n; with S >= n this
    is the EXCEPTIONAL branch S = n (6.2). Otherwise b = -1.
(c) e = 2. Then d = delta' = 1, k = 0, t = h = 1; the single point b lies in I = [S+1, p-1] with S >= n = p-3, so b in {-1, -2},
    and b = -2 forces S = p-3 = n: the exceptional branch (6.2). Otherwise b = -1.

6.1 Lemma AP'' (new). Let p be prime, N >= 1 and p >= 3N+5, x in Z_p nonzero, alpha in Z_p, and suppose the N+1 points
alpha + rho*x (0 <= rho <= N) lie in an arc I of l <= 2N+2 consecutive residues. Then x in {1, -1, 2, -2}, or N = 1 and x = +-3.
Proof (the accepted R6/D1 scheme with a longer arc). Let d0 := |x~| in [1, (p-1)/2] (signed representative). The N distinct
points with 1 <= rho <= N lie in I n (I + x), of size max(0, l-d0) + max(0, l-p+d0) (two arcs of l consecutive residues offset by
d0 overlap in at most one arc on each side).
(i) d0 >= l: l-d0 <= 0 and l-p+d0 <= 2d0-p < 0, so the intersection is empty: contradiction.
(ii) p-l < d0 < l: the size is 2l-p <= 4N+4-p < N (p > 3N+4): contradiction.
(iii) Otherwise d0 < l and d0 <= p-l; the size is l-d0 >= N, so d0 <= l-N <= N+2. Lift I to L = [lambda, lambda+l-1] and let
y_rho in L lift alpha + rho*x. Then y_(rho+1) - y_rho = x~ (mod p) and |y_(rho+1) - y_rho| <= l-1, while the other candidates
x~ +- p have absolute value >= p-d0 >= l; so y_(rho+1) - y_rho = x~ exactly. Hence N d0 = |y_N - y_0| <= l-1 <= 2N+1, i.e.
d0 <= 2 + 1/N: d0 <= 2, or N = 1 and d0 = 3. []

6.2 Exceptional branch (b = -2, S = n). Every x_u >= 1 and sum x_u = S = n = |U'| force x_u = 1, so mu_u = a = (-2)^(-1) =
(p-1)/2 (mod p) for every u in U': every term of U' is iota. The terms of Y equal to neither g nor iota lie in Z0: at most
k = d-1 of them. Corollary IP' contradicts the long zero-sum.

6.3 Main branch (b = -1). Then mu_u = -x_u (mod p) on U', and the rho = h point p-h lies in I, so S <= p-h-1 = p-e. Thus
  (5) mu_u = -x_u, x_u >= 1, n <= S <= p-e, and every integer s in [0, S] is an actual x-sum in U'.

## 7. Localization and the two signed bounds (constants re-derived)

Put R := p-S-h. By (5) and S >= n:
  (6) 1 <= R <= p-n-h = e-delta'+1 <= e.             [threshold: R <= e-delta']
Let z in Z0 have least mu-residue zeta in [1, p-1]. If h <= zeta <= S+h, take s := zeta-h in [0, S] and W'_s <= U' of x-sum s by
(5); {z} u W'_s has mu-sum = zeta - s = h (mod p) and weighted size >= 1+2h > d-1, against (1). If zeta < h, (1) gives
1+2zeta <= d-1. Since S+h <= p-1, every z is
  (7) POSITIVE: 1 <= zeta <= floor((d-2)/2), z~ := zeta;  or  NEGATIVE: zeta >= S+h+1, z~ := -nu, nu := p-zeta in [1, R-1].
(R = 1: no negatives; d <= 3: no positives.) Let q := |Z+|, P := sum of zeta over Z+, N_tot := sum of nu over Z-.
  (8) q + 2P <= d-1, hence P <= (d-1)/2 < h.
Otherwise, in any order, the first prefix j0 with j0 + 2P_(j0) >= d has j0 >= 2, 2P_(j0-1) <= d-j0 and 2zeta_(j0) <= d-2, so
1 <= P_(j0) <= d-2 <= h-2 < h; this prefix has rho = P_(j0) and weighted size >= d, against (1).
  (10) N_tot <= R-1.
Otherwise R >= 2 and the first prefix V of negatives with N_V >= R has N_V <= 2R-2. Put s := p - N_V - h. Then s <= S (N_V >= R),
and s >= 2S+h-p+2 >= 2n+h-p+2 = p-3e+2delta'+1 >= 4 [threshold: p-3e+3+2delta']. So W'_s exists, and V u W'_s has signed mu-sum
-N_V - s = h-p, residue h, and weighted size >= 1+2h > d-1, against (1).

## 8. The long zero-sum and the signed lift

Let T be ANY long zero-sum of Y: |T| = 2p+2j with j >= 1, and |T| <= |Y| = 3p-2e gives j <= (p-2e)/2, so p-j >= (p+2e)/2 > h.
[G-LS used SLZ3 here; it is not needed.] Write T = g^i W*, 0 <= i <= M, W* <= U. The g-coefficient sum
i + |W*| + 2sigma(W*) = 2p+2j+2sigma(W*) is divisible by 2p (ord g = 2p), so
  (12) sigma(W*) = -j (mod p),  |W*| = 2p+2j-i >= d+2j.
Split W* = W' u Z*, W' <= U', Z* <= Z0, l* := |Z*| <= d-1; let s be the x-sum of W' (|W'| <= s <= S) and z~* := sum of z~ over
Z*, so -(R-1) <= z~* <= P by (8), (10). tau := z~* - s = sigma(W*) = -j (mod p), and
  (13) -p+h+1 = -(R-1) - S <= tau <= P < h.
The integers congruent to -j mod p in (-p, p) are -j and p-j > h; hence tau = -j, i.e. s = z~* + j. By (12) and x_u >= 1,
  (15) d+2j <= |W*| = |W'| + l* <= s + l* = z~* + j + l*,  so  z~* >= d+j-l* >= j+1 >= 2.
As z~* <= P < h, Z* is nonempty and rho(Z*) = z~* in [2, h]; then |Z*| + 2rho(Z*) = l* + 2z~* >= d+j+z~* > d-1, against (1).
So case (I) is impossible as well. Cases (I) and (II) are exhaustive (Sec. 3): no counterexample exists, and Theorem ONE-SHORT-LS
holds relative to the stated imports and the conditional Lev statement. []

## 9. Constant-change table against the G-LS template (stab-round2/proof-general-LS-Lev-v1.md, bc4f4c70...06dc)

| Step | G-LS at |Y| = p+2kappa+1 (template lines) | Here at |Y| = p+2kappa (section) |
| --- | --- | --- |
| Start | RED to the threshold length (64-65) | none needed; |Y| = p+2kappa given (3) |
| Generator | DGM-p: M >= 2kappa+3, d <= 2e-3 (66-69) | Lemma DOM via CT with n = p-2: M >= 2kappa+2, d <= 2e-2 (2) |
| r | p-2e+1+d (71) | p-2e+d (2, 3) |
| Dichotomy | K = p-2e+1; (I) d <= e-2 (70-71) | K = p-2e; (I) d <= e-1 = h (3) |
| Case (II) | LS-II' (AP, arc 2e-2) (70) | AP' on arc 2e-1: mu1 in {+-1, +-1/2}; 1, 1/2 forbidden; -1/2 = iota via IP'; -1 with c' <= 2e-3, drop <= 2e-2 (4) |
| e = 2 | empty d-range (72) | d = 1; handled in 6(c) |
| Bound (1) | r+2h = p-1+d < 2p (73-77) | r+2h = p-2+d < 2p (3) |
| Core size | n = p-2e+1+delta' (81) | n = p-2e+delta' (5) |
| Few-sums margin | p-3e+2+2delta'-t (93-95) | p-3e+2delta'-t >= 2 (5) |
| Arc | l <= 2e-2-delta' (109) | l <= 2e-1-delta' (6) |
| delta' >= 2 | AP on 2N (112-114) | AP' on 2N+1; exclude b = 1, 2, -2 (6a) |
| delta' = 1 | AP' on 2N+1 (116-120) | NEW AP'' on 2N+2; b = -2 iff S = n, killed by IP' (6b, 6.1, 6.2) |
| R | <= e-delta' (128-129) | <= e-delta'+1 (6)-(7) |
| Positive prefix | P_(j0) <= d-2 <= h-3 (144) | P_(j0) <= d-2 <= h-2 (8) |
| Negative s | >= p-3e+3+2delta' (156-158) | >= p-3e+1+2delta' (10) |
| Witness length | SLZ3: j <= (p-3e+1)/2 (167-170) | |T| <= |Y|: j <= (p-2e)/2 (8) |
| Signed lift | (180-195) | unchanged in form (8) |

## 10. Interface table (sources and authorities; inclusive lines; whole-file sha256)

Abbreviations: R18 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/ ;
SR2 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/ .

| Interface | Source (path:lines, sha256) | Accepting verdict (path:lines, item, sha256) | Original domain | How met here |
| --- | --- | --- | --- | --- |
| CF(a) | SR2/proof-CF-XT-v1.md:15-33, aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f; range erratum SR2/erratum-1-CF-XT-ROW-range.md:7-11 (E1), 767fe8f8605019b3b3b7aa1ff6a610f088279ede30b9b3429544d4c8487c1db7 | R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md:17, item 1, ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 | p >= 5 prime, integer 0 <= kappa <= p-1, any odd generator | p >= 7, kappa <= p-2, g from Lemma DOM, M <= 2p-1 (Sec. 3) |
| CT | SR2/proof-LSplus-e2-v1.md:13-19, 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 | R18/olson-STAB-delta-parent-verdict-v1.md:23, item 6, ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 | p >= 5 prime, 0 <= kappa <= p-1, odd (ZP_kappa) Y, 1 <= n <= |Y|, |Y|-n even in [2kappa+2, 2p] | n = p-2, |Y|-n = 2kappa+2 (Sec. 2) |
| ROW | SR2/proof-ROW-v1.md:49-52, a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; rho-wording SR2/erratum-1-CF-XT-ROW-range.md:17-30 (E3, E4) | R18/olson-CFXT-ROW-LSII-parent-verdict-v1.md:22, item 6 | (ZP_kappa), integer 0 <= kappa <= p-1, any odd generator, r >= d and r+2e-2 <= 2p | K = r-d = p-2e >= 0; r+2e-2 <= p+2e-4 <= 2p (Sec. 3) |
| AP' | SR2/proof-LS-caseI-smalldelta-v1.md:30-31, 2ad172a026ee64441f00fd228b8b402a0a5f2e0d85df04512c87f0e70e5a68b1; proof SR2/erratum-1-delta-APprime.md:7-17 (D1), e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461 | R18/olson-general-LS-parent-verdict-v1.md:31, m1 standalone admission, 811e5807541f4adb27bf308456358de87cbbd444382103a3f98cda595c10f25b | prime p, n >= 1, 3n+2 < p, arc <= 2n+1 | Sec. 4 Step 1: n = h, arc 2h+1, 3h+2 = 3e-1 < p; Sec. 6(a): n = N = h-t >= 1, arc <= 2N+1, 3N+2 <= 3e-4 < p |
| Lev Thm 2 (external, conditional) | SR2/source-Lev-2110.01081v3-statement-v1.md:10-28, c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d | R18/olson-general-LS-parent-verdict-v1.md:5, 38 (declared statement-level premise of G-LS; statement re-read by parent; proof not replayed) | zero-sum-free sequence in an abelian group, |Sigma_inc| < 2n | U' zero-sum-free in C_p, (3) (Sec. 5) |
| Template only (no import) | SR2/proof-general-LS-Lev-v1.md:62-196, bc4f4c7035353bf904a202bd41811684a76cb5e9401905a2860e20222fec06dc; SR2/proof-LS-caseII-v2.md:39-66, 3df159ff61784cb3345b27a6cf9da873900051df92dbb3be019e846578d73a43; SR2/proof-LS-caseII-v2-addendum-1.md:10-23, c289db226c86ea7703af4a23c4a93dce543669cb911d36b5845e70aad2c98718; SR2/proof-LSplus-e2-v1.md:28-47 (LS+2 Steps 0-3) | G-LS: general-LS verdict item 1; LS-II': STAB-delta item 1; LS+2: STAB-delta item 4 | threshold length (G-LS, LS-II'); kappa = p-2 (LS+2) | every used step re-derived above; none applied outside its domain |

## 11. Trust boundary, cross-coverage and preserved failed branches

Trust. Written proof relative to CF(a), CT, ROW, AP' (parent-accepted, original scopes) and Lev 2022 Theorem 2 (external,
statement level, CONDITIONAL; used in Sec. 5 for every e >= 2 in case (I)). Lemmas IP, DOM, AP'' and all adapted steps are new
written arguments, CANDIDATE_UNVERIFIED. CT and ROW rest on Cauchy-Davenport (classical) through Lemma RS. No computation is a
premise; no transitive computer-assisted input is used by any cited interface.

Cross-coverage (internal consistency, not a premise). Accepted LS+ bounds |Y| <= 3kappa+1 imply the theorem wherever they hold,
because 3kappa+1 < p+2kappa for e >= 2: kappa = p-2 (LS+2, STAB-delta item 4); e >= 3 with p >= 10e-13 (LS+ linear band,
R18/olson-LSplus-chain-parent-verdict-v1.md:9-11, 4005007f4e073386236016b62949cba925cb5cde12ba13c24ce27b2a2c351b55); p = 1 mod 3,
kappa = (2p+1)/3 (BASE1+, STAB-delta item 3). Those cells are therefore also covered without Lev (relative to their own imports,
including the index-one theorem). The cells newly covered here, relative to the lane's accepted results and conditional on Lev, are
3 <= e with p < 10e-13 outside BASE1+, e.g. (p, kappa) = (11,8), (13,10), (17,12), (17,13), (19,14), (19,15), (23,16)-(23,19).
The E2/E3 families (length 3kappa+1 < p+2kappa) are consistent with the theorem.

Preserved failed branches (exact obstruction recorded; none is a premise).
- DGM-p at length p+2kappa: Lemma RS(a) with n = 2kappa+2 gives only sum_x min(2kappa+2, v_x) <= p+2kappa = |Y|, with no strict
  inequality, so no value of multiplicity >= 2kappa+3 is forced. Replaced by CT with n = p-2 (Lemma DOM), which forces M >= 2kappa+2
  only after excluding the two-heavy shape.
- LS-II' Step 1 with Lemma AP: the avoiding progression lies in an arc of 2e-1 residues, one more than AP's 2e-2; AP is inapplicable.
  Replaced by AP', which admits mu1 = +-1/2; both are excluded (CF, involution pairs).
- G-LS pinning at delta' = 1 with AP': the arc bound becomes 2N+2 > 2N+1. Replaced by the new AP''; the arc argument alone cannot
  exclude b = -2 when S = n (U' then consists of involutions); only Lemma IP excludes it.
- An extension-to-threshold route (adding one copy of g to reach length p+2kappa+1 and invoking G-LS) was considered and NOT used:
  adding g keeps (ZP_kappa) only if no W <= U has rho(W) <= h and |W| + 2rho(W) = d-1, which fails whenever the core Z0 has
  k = d-1 (e.g. in the exceptional branch). No claim is made about it.

Not claimed: LS+ (the 3kappa+1 bound) or STAB at any new cell; any length below p+2kappa; kappa = p-1; any word-level statement
(an o_F = p / terminal k = p consequence would remain conditional on the pending ASSEMBLY-LS and a separate word-level review);
novelty or priority; Lean or human review.
