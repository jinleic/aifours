# Addendum to proof-ROT-ZX-v1.md: Lemma S1 (g) - (ZP) implies (S1) at kappa = (p + delta)/2 whenever p >= 12 delta - 36 (and two milder conditions), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:59:59-07:00.  Status [W], UNREVIEWED.

This addendum changes no file.  It generalises the method of Lemmas S1 (d) and S1 (e) (proof-ROT-ZX-addendum-S1d-v1.md,
aefcfc58...c61b; proof-ROT-ZX-addendum-S1e-v1.md, ec9fe140...a330; both unreviewed).  Those two remain the sharper
statements at small p.  The consequences are through the parent-accepted terminal criterion of
R/olson-zx-s1c-parent-verdict-v1.md (2f8d376b...e6af) item 3, read through its overlay.  No novelty claim.  Not ROT(p),
INV*(p) or ordered Olson in general.

Imports: (D); EGZ for Z_p; Davenport for Z_p (proved inline in proof-ROT-ZX-addendum-S1c-v1.md, 7ce7102c...b0b6); the
EXPLICIT classical Savchev-Chen / Yuan index theorem, with the sources listed in the S1 (d) addendum.  It is used once,
in Step (5), on a minimal zero-sum sequence over C_p of length >= p + 2 - delta >= floor(p/2) + 2.
Notation as in the S1 (d) addendum: x(y), x(U), half-sums, coefficients with respect to h.

## 1. Lemma S1 (g)

**Lemma S1 (g).**  Let p be prime, delta >= 3 odd, and kappa := (p + delta)/2.  Assume
  (P1) p >= 3delta + 4,   (P2) 4delta <= p + 10,   (P3) delta = 3 or p >= 12delta - 36.
Let Y be a sequence of odd elements of Z_(2p) with
  (ZP) no zero-sum subsequence of length in [2kappa + 2, 2p].
Then every zero-sum subsequence of Y has length <= 2kappa = p + delta.
For delta >= 5, (P3) implies (P1) and (P2).  For delta = 3 the hypotheses read p >= 13.

Proof.  Suppose not.  Let T be a zero-sum subsequence with |T| >= 2kappa + 2 and |T| least, and N := |T|.

(1) Lengths.
- N >= 2p + 2 by (ZP), and T has nonempty proper zero-sums by (D).
- For each nonempty proper zero-sum T' of T, both T' and T - T' have length <= p + delta, by minimality and parity.
- So every nonempty proper zero-sum of T has length >= l := N - p - delta.  Also l >= p + 2 - delta.

(2) Half-sums.  EGZ gives a half-sum T_1 <= T with |T_1| = p.  Put M := T - T_1 and mu := |M| = N - p, so M is a
half-sum.
- Claim A.  Let V be a nonempty sub-multiset of M with x(V) = 0 and V != M.  If |V| is even, V is a proper zero-sum
  of T, so |V| >= l.  If |V| is odd, T_1 V is a proper zero-sum of T, so p + |V| <= p + delta, i.e. |V| <= delta.
- Claim B.  M has no two disjoint odd such V.  Otherwise they form a nonempty proper zero-sum of length <= 2delta, but
  2delta < p + 2 - delta <= l by (P1).

(3) N <= 2p + delta - 1.  Suppose l > p.
- Then Davenport (on p terms of M) gives only odd V's, of length <= delta.
- So V_1 exists, and M - V_1 has >= mu - delta = l >= p terms, giving a second, disjoint V_2, contrary to Claim B.
- Hence l <= p; as l is even and p is odd, l <= p - 1.

(4) T has no term (1, 0).  Suppose u = (1, 0) is a term.
- Take T_1 by EGZ avoiding u, so that u lies in M.  Davenport in M - {u} (>= p + 1 terms) gives V with x(V) = 0 and
  1 <= |V| <= p.
- An odd V contradicts Claim B together with {u}.
- An even V has |V| >= l.  The rest M - {u} - V has x-sum 0 and an even number of terms: at least 2 and at most
  mu - 1 - l = delta - 1 < l.  So it is a zero-sum shorter than l, a contradiction.

(5) M = C V and index 1.
- Davenport gives V_0 <= M with x(V_0) = 0 and 1 <= |V_0| <= p.  If |V_0| is odd, put C := V_0; otherwise put
  C := M - V_0.  Either way C is an odd half-sum with 3 <= |C| <= delta (|C| != 1 by (4)).
- Put V := M - C, an even zero-sum with |V| >= mu - delta = l.
- V has no nonempty proper sub-multiset V'' with x(V'') = 0:
  - an even V'' makes V'' and V - V'' zero-sums of length >= l, so |V| >= 2l > mu by (P1);
  - an odd V'' contradicts Claim B, since V'' and V - V'' are disjoint.
- So the x-values of V form a minimal zero-sum sequence over Z_p, and beta := |V| lies in [l, p].
- By Savchev-Chen / Yuan (beta >= p + 2 - delta >= floor(p/2) + 2 by (P1)), there is h in Z_p \ {0} for which the
  coefficients of V are positive and sum to p.
  - So sum over V of (c - 1) = p - beta <= delta - 2.
  - With h^ := (1, h), the multiplicity m_V of h^ in V satisfies m_V >= 2beta - p >= p + 4 - 2delta.
- V is a zero-sum in Z_(2p).  Its signed weights relative to h^ are c (c odd) and c - p (c even), summing to p minus
  p times (number of even coefficients).  So the number of even coefficients is odd.
- Fix a term y of V with even coefficient e.  Then 2 <= e <= 1 + (p - beta) <= delta - 1.
- Let t be the multiplicity of h^ in T.  Then t >= m_V >= p + 4 - 2delta.

(6) Classification.  Let z != h^ be a term of T with coefficient c in [2, p - 1] (c != 0 by (4)).
- (6a) c even with p - c <= t.  Then h^^(p-c) z is a proper zero-sum of length p - c + 1 >= l, so c <= p + 1 - l
  <= delta - 1.
  - Hence every even c satisfies c <= K_e := max(delta - 1, p - t - 1), and p - t - 1 <= 2delta - 5.
- (6b) c odd, c <= p - e, with p - e - c <= t.  Then h^^(p-e-c) y z is a proper zero-sum of even length
  p - e - c + 2 >= l, so c <= p + 2 - e - l <= delta - e.
  - Hence every odd c <= p - e satisfies c <= K_o := max(delta - e, p - e - t - 1), and p - e - t - 1 <= 2delta - 7.
- (6c) c odd, c > p - e ("near p").  Put s := p - c, which is even with 2 <= s <= e - 2 <= delta - 3 <= m_V (by
  (P1)).
  - If z is not in C, then h^^s z (the h^'s taken from V) is a half-sum of size s + 1 disjoint from C.  So h^^s z C is
    a nonempty proper zero-sum of length <= (delta - 2) + delta < l (by (P1)), a contradiction.  So z lies in C.
  - Two near-p terms z, z' give h^^(s+s') z z', with x-sum 2p and length s + s' + 2 <= 2delta - 4 < l.  This is a
    contradiction once s + s' <= t, which holds because 2delta - 6 <= p + 4 - 2delta by (P2).
  - So there is at most one near-p term; call it q (u_q = 1), with s_q := p - c_q, or u_q = 0.
- Let U be the multiset of the remaining non-h^ terms (the "small" ones).
  - Their coefficients lie in [2, K] with K := max(K_e, K_o).  For delta >= 5, K <= 2delta - 5; for delta = 3, U has
    only coefficient 2 (K_e = 2 and K_o <= 1).
  - y lies in U.

(7) x-sum.  Put X := sum over U of (c - 1).
- x(T) = (t + sum_U c + (p - s_q) u_q) h with t = N - |U| - u_q.  So x(T) = 0 gives
  (N - 2p) + X - (s_q + 1) u_q = 0 (mod p).
- Here 2 <= N - 2p <= delta - 1 and s_q + 1 <= e - 1.
- If u_q = 0, then X = -(N - 2p) (mod p) with X >= 0, so X >= p - (N - 2p) >= p + 1 - delta.
- If u_q = 1, put r := s_q + 1 - (N - 2p), so 3 - delta <= r <= e - 3.
  - Either X = r: but X >= e - 1 because y is in U, a contradiction;
  - or X >= p + r >= p + 3 - delta.
- So in every surviving case, X >= p + 1 - delta.

(8) S-condition and contradiction.
- S-condition.  Let S <= U have an odd number of even-coefficient terms and sigma := (sum of coefficients over S) in
  [p - t, p].  Then h^^(p - sigma) S is a proper nonempty zero-sum: x-sum p, even length p - sigma + |S|.  So
  p - sigma + |S| >= l, i.e. sum over S of (c - 1) <= p - l <= delta - 2.
- Build S.  Start with S := {y}.  Repeatedly add either one odd-coefficient term of U - S, or two even-coefficient terms
  of U - S.  This keeps the number of even terms odd.
  - At most one even term can be left unused, of mass c - 1 <= K - 1.  So the mass sum (c - 1) over S can be raised to
    any value up to at least X - (K - 1).
  - Let T* := max(delta - 1, 2delta - 5), and stop at the first S with mass >= T*.
  - This is possible because X - (K - 1) >= p + 2 - delta - K >= T*.  For delta = 3: X >= p - 2 >= 3.  For delta >= 5
    it needs p >= 5delta - 12, which (P3) gives.
- Bounds on the final S:
  - Its mass is <= T* - 1 + 2(K - 1).
  - Every c >= 2 gives |S| <= mass, so sigma = mass + |S| <= 2(T* + 2K - 3).  This is <= 12delta - 36 <= p for
    delta >= 5 by (P3), and <= 6 <= p for delta = 3.
  - Also sigma >= mass + 1 >= T* + 1 >= 2delta - 4 >= p - t.
- So the S-condition applies, and the mass of S is >= T* >= delta - 1 > delta - 2: a contradiction.  []

**Corollary S1 (g)+.**  Let p >= 5 be prime and kappa an integer.  Then (ZP) implies (S1) at kappa in each of the
following cases:
- kappa <= (p + 1)/2: S1+, accepted;
- kappa = (p + 3)/2 and p >= 11: S1 (d), or S1 (g) for p >= 13;
- kappa = (p + 5)/2 and p >= 19: S1 (e);
- kappa = (p + delta)/2 with delta >= 5 odd and p >= 12delta - 36: S1 (g).
Since the hypotheses only weaken as delta decreases, for each p the set of covered kappa is an initial segment
kappa <= (p + delta*(p))/2.  For p >= 29, delta*(p) is the largest odd delta with p >= 12delta - 36 (and at least 5,
from S1 (e)).

## 2. Consequences (through the accepted terminal criterion; conditional on acceptance of the addenda used)

Terminal form: rotations lie in one nonzero pair whenever some normal form has k = 1, or has 3k <= 2p + 1 and
kappa^ <= (p + delta*(p))/2.
Uniform form, for words of length 4p - 2 (INV*) and 4p - 1 (ordered Olson):
- condition: 3o <= 2p + 1, and o <= (p + delta*(p) + 2)/2 or F >= o + p - delta*(p) - 2;
- proof as in the S1 (d) addendum Sec. 2 (deletion ledger unchanged).

Examples (delta* from S1 (e) and S1 (g)):
- p = 29, 31, 37, 41, 43, 47: delta* = 5 (S1 (g) with delta = 7 needs p >= 48).
- p = 53 through 71: delta* = 7.
- p = 73 through 89: delta* = 9 (delta = 11 needs p >= 96).
- In general delta* ~ p/12, i.e. kappa^ up to about 13p/24, against the 3k <= 2p + 1 limit kappa^ <= (2p - 2)/3.

Not covered by this route: inside 3k <= 2p + 1, the terminal pairs with kappa^ > (p + delta*(p))/2.  The smallest p
with such pairs is p = 29 (pair (19, 18)).  Nothing is claimed to fail.
The constant 12 in (P3) comes from the crude bound sigma <= 2 * mass in Step (8); it is not claimed to be optimal.
