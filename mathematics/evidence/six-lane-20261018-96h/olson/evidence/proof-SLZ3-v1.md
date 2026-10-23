# Theorem SLZ3: under (ZP_kappa) a shortest long zero-sum has length <= 3kappa + 1 (kappa > floor(2p/3)), v1

Owner ContinueOlson (math-2 lane, 96-hour continuation).  Written after /bin/date 2026-10-19T03:27:25-0700.  Status: CANDIDATE, written proof
[W], UNREVIEWED.  It re-runs the accepted proof of Lemma S1-sharp (evidence/proof-S1-sharp-v1.md 992ab63f40aa08626560ccf121b0004a08588fdb24805ff4eb30d25a2150cb0c + erratum 1
bf504cdf8b8cfd3e96a26609d00162d365415b3481ca3a7dcbd7112af82f9507; parent verdict run review/olson-s1sharp-parent-verdict-v1.md bd4a0a60cdea0765517ca33a9a2ddefb664b24fad7b20e709835bbdec1e94f41) above its kappa-range, replacing its three
uses of p >= 3delta - 1 by the length hypothesis N >= 3kappa + 2.  No computation is a premise.  No novelty claim (Steps 4/6/7
are routine given Zeng-Yuan 2011: evidence/disposition-S1sharp-ZengYuan-v1.md 439b80debaafb015721730c940de8d4cbf45d5d59db042507b6910d3bd176315); no Lean.  Not LS, not LS+, not
unrestricted INV*(p).

## 0. Statement

Notation of proof-S1-sharp-v1.md: odd elements of Z_(2p); (ZP_kappa): no zero-sum subsequence of length in [2kappa + 2, 2p];
a zero-sum is LONG if its length is >= 2kappa + 2 (under (ZP_kappa): >= 2p + 2).

**Theorem SLZ3.**  Let p >= 5 be prime and kappa an integer with floor(2p/3) + 1 <= kappa <= p - 1.  If a sequence Y of odd
elements of Z_(2p) satisfies (ZP_kappa), then every long zero-sum subsequence of Y of minimal length N satisfies N <= 3kappa + 1.
Equivalently: a zero-sum sequence T of odd elements with (ZP_kappa) and |T| >= 3kappa + 2 has a proper long zero-sum
subsequence.

Sharpness.  For p = 1 (mod 3) and kappa = (2p + 1)/3, the S1-sharp family F1 = g^(p+3) (3g)^(p-1) is a (ZP_kappa) zero-sum
of length 2p + 2 = 3kappa + 1 without proper long zero-sums (its zero-sums g^i (3g)^j have i + 3j in {2p, 4p}; i + 3j = 4p
forces j = p - 1, i = p + 3; i + 3j = 2p gives lengths 2p - 2j <= 2kappa as j >= ceil((p - 3)/3)).  For p = 2 (mod 3) and
kappa = (2p + 2)/3 the bound reads N <= 2p + 2, i.e. N = 2p + 2.
Consequence.  The bound improves Lemma SLZ (proof-SLZ-EXT-v2.md, N <= p + 2kappa + 1) whenever kappa <= p - 1.

## 1. Imports

As in proof-S1-sharp-v1.md Sec. 1: the index-one theorem (parent import record run of 2026-10-16
review/olson-index-one-primary-statement-parent-v1.md e4615144...35c6) and Lemma S1-sharp itself (for the base of the
induction).  Nothing else.

## 2. Proof

Induction on kappa.  For kappa0 := floor(2p/3), Lemma S1-sharp says a (ZP_kappa0) sequence has no long zero-sum.  Let
floor(2p/3) + 1 <= kappa <= p - 1 and assume the Theorem at kappa - 1 when kappa - 1 > kappa0.  Put u := 2kappa,
delta := u - p (odd; delta >= 3 since kappa >= (2p + 1)/3 >= (p + 3)/2 for p >= 5).  Suppose Y satisfies (ZP_kappa) and its
shortest long zero-sum T has N := |T| >= 3kappa + 2.  The Steps below are those of proof-S1-sharp-v1.md Sec. 2, with T and
the notation l, D, Q, Q', m, S_Q, b_min, t', Y (the non-unit part of Q') defined there; only the changes are written out.
Step 1.  Unchanged: every nonempty proper zero-sum of T has length in [l, u], l := N - u, D := u - l = 4kappa - N.  From
N >= 2p + 2: D <= 2delta - 2 and l >= p - delta + 2 (as in S1-sharp).  From N >= 3kappa + 2: D <= kappa - 2 and l >= kappa + 2.
Step 2 (all proper zero-sums minimal).  S1-sharp's argument gives N <= 3kappa if not; here N >= 3kappa + 2.  (Replaces
'3kappa <= 2p < N'.)
Step 3 (a proper zero-sum of length exactly u).  If every nonempty proper zero-sum of T had length <= u - 2, then T would
satisfy (ZP_(kappa-1)) (its zero-sums of length in [2kappa, 2p] would be proper ones of length >= 2kappa).  If
kappa - 1 = kappa0, this contradicts Lemma S1-sharp (T itself is a long zero-sum of T).  Otherwise the Theorem at kappa - 1,
applied to the sequence T, gives a long zero-sum T0 of T with |T0| <= 3(kappa - 1) + 1; T0 has length >= 2p + 2, so it is a
long zero-sum of Y contained in T, and minimality of N gives N <= 3kappa - 2: contradiction.  So T has a proper zero-sum Q
with |Q| = u; Q' := T - Q has |Q'| = l; both are minimal (Step 2).  (Replaces the use of the Lemma at kappa - 1.)
Step 4 (index one).  Unchanged (|Q| = p + delta >= p + 3; u = 2kappa <= 2p - 2, so S_Q is nonempty): a generator g with
A_Q = 2p, m >= (p + 3delta)/2, b_min <= p - delta + 1, every b in S_Q is <= p - delta - 2|S_Q| + 3.
Step 5 (MC).  Unchanged.
Step 6 (coefficients of Q' are <= D + 1).  Unchanged; it uses only D <= 2delta - 2, m >= (p + 3delta)/2 >= D + 2 and the
Step 4 facts.
Step 7 (A_Q' = 2p).  S1-sharp's argument reaches 'l <= D', i.e. 2l <= u, i.e. N <= 3kappa: contradiction with
N >= 3kappa + 2.  (Replaces 'u <= 2D <= 4delta - 4, i.e. p <= 3delta - 4'.)
Step 8.  Unchanged.
Step 9 (counting).  base := (3l - 2p)/2 is an integer with 3l - 2p >= 3kappa + 6 - 2p >= 7 (3kappa >= 2p + 1), so base >= 4 >= 3
(replaces 'base >= (p - 3delta + 6)/2 >= 5/2').  The rest is unchanged: at most one term of Y has coefficient > t', so
3l <= b_min + 2t' + 2 <= 3 b_min, i.e. l <= b_min, while l >= p - delta + 2 > p - delta + 1 >= b_min: contradiction.
Hence N <= 3kappa + 1.  []

## 3. Hypothesis map
- N >= 3kappa + 2 is used in Steps 2, 7 and 9 (where S1-sharp used p >= 3delta - 1) and in Step 1's D <= kappa - 2 (not needed
  elsewhere); N >= 2p + 2 (from (ZP_kappa)) in Steps 1, 4 (via l), 6 and 9; kappa <= p - 1 in Step 4 (S_Q nonempty).
- The induction uses the Theorem at kappa - 1 only through Step 3, applied to the sequence T.

## 4. Relation to the lane's LS work (internal; not a premise)
In a counterexample to LS(p, kappa) (evidence/notes-LS-propagation-v1.md), the shortest long zero-sum T has N <= 3kappa + 1 <=
thr - (p - kappa), so at least p - kappa terms lie outside T.  The sharper conjecture LS+ (|Y| <= 3kappa + 1 for
(ZP)-and-not-(S1) sequences) is exactly SLZ3 for sequences Y that have no proper long zero-sum; the general case (terms
outside every shortest long zero-sum) remains open.
