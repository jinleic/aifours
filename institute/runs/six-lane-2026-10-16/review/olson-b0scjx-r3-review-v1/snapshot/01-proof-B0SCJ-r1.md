# Theorem B0S-CJ: B = 0 under R >= 4 kappa + 1 with two disjoint heavy admissible intervals (contains B0S++)

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T06:56:44-0700.  Status: written proof [W], UNREVIEWED.
Builds on proof-B0SPP-r5.md (d388d391...bd64; r4 Codex ACCEPT-WITH-FIXES 0/0/1, r5 = that erratum).  Used verbatim from it: Sec. 1
(set-up, P0 consequences, windows, gaps), Lemmas C1 and C2, and Sec. 3 (the kill, which needs only sum_t w_t = p, the singleton
gaps and (H)).  New here: Lemma CJ and the covering arguments.  The unsent draft proof-B0SEED-r1.md (33a164cd...8e55) is
superseded and must not be reviewed: its seed hypothesis is unnecessary, and its Sec. 2 (a) and Remark (1) contain unfinished
sentences.
Scope: B = 0 only.  No statement about rotation values, INV*(p), REFL(p) or ordered Olson.

## 0. Statement

Setting of proof-B0SPP-r5.md Theorem B0S++.  w has length 4p - 2, p >= 5 prime, and all rotations equal rho_1 (B = 0).  All
maximal reflection blocks are odd, kappa >= 1, genuine empty runs are allowed.  Delta := k - p - kappa - 1, and
(H) R >= 4 kappa + 1.
For a proper cyclic interval S = [a, b] of runs, its outer arc is O(S) := [b + 1, a - 1], and m(.) is the number of rotations.
* S is HEAVY if m(S) >= 2 Delta - 1.
* S is ADMISSIBLE if m(O(S)) >= 2 Delta - 1 and either |O(S)| = 1, or some run x of O(S) other than its last run a - 1 satisfies
  m([b + 1, x + 1]) >= 2 Delta - 1 and m([x, a - 1]) >= 2 Delta - 1.
**Theorem B0S-CJ.**  Assume (H), and either Delta <= 0 or (2HA): w has two disjoint heavy admissible intervals.  Then w has an
identity 2p-subword.
**Corollary 1.**  (3H) => (2HA), where (3H) means the cycle of runs splits into three consecutive arcs, each of mass >= 2 Delta - 1.
**Corollary 2.**  If w avoids, Delta >= 1 and p >= kappa + 5 Delta - 5, then (2HA) holds.  Hence, under (H), no avoider has
Delta <= 1 or p >= kappa + 5 Delta - 5.  Under (H) the latter holds whenever 4 Delta <= 2 kappa + 7.  For p in
{5, 7, 11, 13, 17, 19, 23}, RES_<(p) has no avoider with B = 0 and R >= 4 kappa + 1, for any k.
(Delta <= kappa - 1 for avoiders, and (H) is equivalent to p >= 3 kappa + 2 + Delta.  The parameter check for p <= 23 is a direct
enumeration of the triples (p, kappa, Delta) with 2 <= Delta <= kappa - 1 and p >= 3 kappa + 2 + Delta; none violates
p >= kappa + 5 Delta - 5.  Delta <= 1 is the Corollary of B0S++.)
**Containment.**  Hypothesis (D) of B0S++ implies (2HA).  Take two disjoint pairs P1 = {s, s + 1}, P2 = {t, t + 1} of mass
>= 2 Delta - 1.  For P1 put x := t: the run t + 1 lies in O(P1), so t is not its last run, and both [s + 2, t + 1] and [t, s - 1]
contain P2.  P2 is treated symmetrically.  So B0S-CJ contains B0S++.

## 1. Facts (w an avoider; proof-B0SPP-r5.md Sec. 1)

(F1) N_+ := number of nonempty runs = k - n_E >= k - 2 kappa = p - kappa + 1 + Delta  (P0: n_E <= 2 kappa).
(F2) For every run t, R - r_t >= N_+ - 1 >= p - kappa + Delta >= 2 Delta - 1.  The last step holds because Delta <= kappa - 1 and
2 kappa <= p - 1.
Notation for a split: Q = Q1 u Q2 a proper interval with Q1, Q2 nonempty consecutive sub-intervals, and Q3 := Q^c.
Lemma C2(b) then gives (B') whenever the three pair sums m(Q1 u Q2), m(Q2 u Q3), m(Q1 u Q3) are all >= 2 Delta - 1.
Lemma C2(a) gives (A') for every split.  Lemma C1(c) turns (A') and (B') into c(Q) >= c(Q1) + c(Q2) and c(Q) <= c(Q1) + c(Q2).
C1(a) gives c({t}) = 0, and C2(c) gives 0 <= c <= J.

## 2. Lemma CJ

**Lemma CJ.**  Assume (H), Delta >= 1 and w avoids.  Then c(S) = J for every heavy admissible interval S.
Proof.  Let S = [a, b] and O = O(S).
* Case |O| = 1.  C1(b) gives J = c(S) + c(O) = c(S), because O is a single run and c(O) = 0.
* Case |O| >= 2.  Let x be the run in the definition of admissible.  Then b + 1 <= x <= a - 2 in the order of O.  Put
  Y1 := [a, x] and Y2 := [x + 1, b].  Both are proper: Y1 misses [x + 1, a - 1] and Y2 misses [b + 1, x].
  - Grow S to Y1 by adding b + 1, ..., x in turn.  When i is added, the split is ([a, i - 1], {i}, [i + 1, a - 1]); the third
    part is nonempty since i <= a - 2.  Its pair sums are m([a, i]) >= m(S) >= 2 Delta - 1, m([i, a - 1]) >= m([x, a - 1]) >=
    2 Delta - 1 (as i <= x) and R - r_i >= 2 Delta - 1 (F2).  So c([a, i]) <= c([a, i - 1]) + c({i}) = c([a, i - 1]), and
    c(Y1) <= c(S).
  - Grow S to Y2 by adding a - 1, a - 2, ..., x + 1 in turn.  When i is added, the split is ({i}, [i + 1, b], [b + 1, i - 1]);
    the third part is nonempty since i >= x + 1 >= b + 2.  Its pair sums are m([i, b]) >= m(S), m([b + 1, i]) >=
    m([b + 1, x + 1]) >= 2 Delta - 1 (as i >= x + 1) and R - r_i.  So c(Y2) <= c(S).
  - Y2 is the union of the consecutive intervals Y1^c = [x + 1, a - 1] and S, with third part [b + 1, x].  (A') gives
    c(Y2) >= c(Y1^c) + c(S), so c(Y1^c) <= c(Y2) - c(S) <= 0, and c(Y1^c) = 0 by C2(c).
  - C1(b) gives J = c(Y1) + c(Y1^c) = c(Y1) <= c(S), and c(S) <= J by C2(c).  []

## 3. Proofs

**Theorem.**  Delta <= 0 is Theorem B0S++.  Let Delta >= 1 and suppose w avoids.  Let S1 = [a1, b1] and S2 = [a2, b2] be disjoint
heavy admissible intervals, so c(S1) = c(S2) = J by Lemma CJ.
Put X := [a1, a2 - 1], which is S1 followed by the possibly empty gap G = [b1 + 1, a2 - 1].  Then X^c = [a2, a1 - 1] contains S2.
If G is nonempty, (A') on the split (S1, G) of X (third part X^c) gives c(X) >= c(S1) + c(G) >= c(S1).  If G is empty, X = S1.
In the same way c(X^c) >= c(S2).  By C1(b), J = c(X) + c(X^c) >= 2J, so J = 0, i.e. sum_t w_t = p.
proof-B0SPP-r5.md Sec. 3 with x_t := w_t now yields a pattern P with x(P) in I(P), i.e. an identity 2p-subword.  []
**Corollary 1.**  Let the arcs be A1, A2, A3 in cyclic order.
* A1 is admissible.  O(A1) = A2 u A3 has mass >= 2 Delta - 1 and at least two runs.  Take x := the last run of A2; it is not the
  last run of O(A1), which ends A3.  Then [b1 + 1, x + 1] contains A2 and [x, a1 - 1] contains A3.
* A2 is admissible in the same way, with x := the last run of A3.
A1 and A2 are disjoint and heavy.  []
**Corollary 2.**  Call a heavy S = [a, b] minimal if deleting either end run leaves mass <= 2 Delta - 2.
* A minimal heavy S contains at most 2 Delta - 1 nonempty runs: [a, b - 1] has mass <= 2 Delta - 2.  So by (F1),
  m(O(S)) >= N_+ - (2 Delta - 1) >= p - kappa + 2 - Delta, and this is >= 4 Delta - 3 iff p >= kappa + 5 Delta - 5.
* A heavy S with m(O) >= 4 Delta - 3 is admissible.
  - If |O| = 1, this is immediate.
  - If |O| >= 2, let x* be the last run x of O other than a - 1 with m([x, a - 1]) >= 2 Delta - 1.  It exists because x = b + 1
    qualifies.  By maximality m([x* + 2, a - 1]) <= 2 Delta - 2: if x* + 1 != a - 1 then x* + 1 does not qualify, and otherwise
    the arc is empty.  Hence m([b + 1, x* + 1]) >= m(O) - (2 Delta - 2) >= 2 Delta - 1.
* Existence of two disjoint ones.  For any run t, [k] \ {t} is heavy by (F2).  Delete end runs while the interval stays heavy; this
  gives a minimal heavy S1.  Its complement is an interval of mass >= 4 Delta - 3 >= 2 Delta - 1, so it contains a minimal heavy S2,
  obtained the same way.  Both are admissible by the two bullets above.  []

## 4. Remarks

(1) Why B0S++ needed (D).  SIGMA-2P derived c = 0 along chains that start from singletons.  Lemma CJ instead grows OUTWARD from a
heavy interval, so no chain inside it is needed, and any two disjoint heavy admissible intervals force 2J <= J.
(2) Covered now, but not by B0S++:
* the thin examples of B0S++ Remark (2) (p = 17, kappa = 4, k = 24) and notes-B0L-open-r1.md;
* the E12 datum (p = 13, kappa = 3, k = 19);
* the seedless p = 17, kappa = 4, k = 24, R = 18 words with eighteen runs rho_1 and six empty runs.
In each, p >= kappa + 5 Delta - 5 with Delta = 2.
(3) Still open for B = 0, k >= p + 1:
* (III) R <= 4 kappa, where (A') can fail;
* (H)-words without (2HA), which need p < kappa + 5 Delta - 5.
(H)-triples (p, kappa, Delta) with Delta >= 2 where Corollary 2 does not apply, p <= 43:
(29, 7, 6), (31, 7, 6), (37, 8, 7), (37, 9, 7), (37, 9, 8), (41, 9, 8), (41, 10, 8), (41, 10, 9), (43, 9, 8), (43, 10, 8), (43, 10, 9), (43, 11, 8).
There are 43 such triples with p <= 61.  The first are (29, 7, 6) and (31, 7, 6): k = p + 2 kappa, every nonempty run is a
single rho_1, and (2HA) fails for the all-ones words there.  Individual words in these cells may still satisfy (2HA).
(4) No finite computation is used.  The parameter check in Corollary 2 is the enumeration stated there (eval transcript of this
worker, 06:56 PDT; it reproduces the list in (3)).
