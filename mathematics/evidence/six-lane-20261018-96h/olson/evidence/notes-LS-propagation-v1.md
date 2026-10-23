# Notes (candidate partials; LS NOT proved): sharpened EXT, propagation, the pair lemma, and the sharper conjecture LS+, v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:23:16-0700.  Status [W], unreviewed.  Builds on evidence/proof-SLZ-EXT-v2.md
(2495300317299fda49c0fb7d4b22daa81dfcecf1aef8c161361b9c04861bd751), evidence/notes-LS-base-v1.md (dcb03fb3e4e2c314778c39063fcfc9fdc9f1fd7f525632a48d5de6e359cad7b9) + erratum 1 (c24a43d5125bfd565745e71081027dfa6cbc6ddfbe06c4e604d6741d7f6bd561), Lemma FB (accepted) and
Lemma FB-p of evidence/proof-KPS-v4.md (68c4e7a7ff898219bfebee028052415cdb785b4b460b87e5cd4e7a6370510170).  Statements marked [S(p)] are relative to the classical import
evidence/import-Sp-XiaYuan-v1.md (d4d515cd4ff7b848d703f9337a3e9b6f12f85bd99319173207014519961381d7).  Notation as in proof-SLZ-EXT-v2.md: p >= 5 prime, 1 <= kappa <= p - 2,
(ZP_kappa), (S1_kappa), LONG = length >= 2kappa + 2 (under (ZP) >= 2p + 2); for a sequence V, 2t0(V) is the length of its
longest zero-sum.  thr := p + 2kappa + 1.

## 1. Lemma EXT' (EXT with the length condition depending on t0)
Let V satisfy (S1_kappa), t0 := t0(V), L := |V| - 2t0 >= p + 1 and |V| >= p + kappa + t0.  If y is odd and V y satisfies
(ZP_kappa), then V y satisfies (S1_kappa).
Proof.  t0 = 0: as in EXT.  t0 >= 1: run the proof of EXT (proof-SLZ-EXT-v2.md Sec. 3) verbatim; only Steps 2 and 3 used
|Y1| >= p + 2kappa, and they hold here:
- Step 2: n+ <= 2p - 1 - W <= 2p - 1 - L, so every s_i - 1 <= sum (s_i - 1) = 2n+ - 2t0 <= 4p - 2 - 2L - 2t0
  = 4p - 2 - 2|V| + 2t0 <= 2p - 2kappa - 2 (by |V| >= p + kappa + t0); so every step s + 1 <= 2p - 2kappa.
- Step 3: c <= 2t0 - 1 and A(H*) + |H*| <= 2e' with e' <= 2p - 1 - L <= p - 2, so c + A(H*) + |H*| <= 2p + 2t0 - 5
  <= 2p + 2kappa - 5 and |U(N1)| >= 3.  []
(For t0 <= kappa - 1 this lowers EXT's length requirement p + 2kappa to p + kappa + t0, together with L >= p + 1.)

## 2. Lemma EXT-p [S(p)] (the boundary L = p)
Let V satisfy (S1_kappa) with |V| = p + 2kappa and t0(V) = kappa.  If y is odd and V y satisfies (ZP_kappa), then V y
satisfies (S1_kappa).
Proof.  Let Z' be a longest zero-sum of V (length 2kappa); C' := V - Z' has length p and is zero-sum-free, hence SC by
Import S(p) with some generator g.  V has no zero-sum of length 2p ((ZP_kappa), kappa <= p - 2), so Lemma FB-p applies to
(V, Z', g).  Case (X): V is g^(p-1) (pg)^(2kappa+1) or g^(2p-1) (pg)^(2kappa-p+1); adding any odd y creates a zero-sum of
length in [2kappa + 2, 2p] (notes-LS-base-v1.md Sec. 3 and its erratum 1), contradicting (ZP_kappa) for V y.  Case (N): the
descent of EXT applies with L = p, exactly as in Lemma BB (notes-LS-base-v1.md Sec. 2): Step 2 gives n+ <= p - 1 and
sum (s_i - 1) = 2n+ - 2kappa <= 2p - 2 - 2kappa; Step 3 gives c <= 2kappa - 1 and A(H*) + |H*| <= 2e' <= 2p - 4.  []

## 3. Proposition PROP+ [S(p)]
Let Y satisfy (ZP_kappa) and contain a subsequence V0 satisfying (S1_kappa) with |V0| >= p + 2kappa - 1, where, if
|V0| = p + 2kappa - 1, t0(V0) <= kappa - 1.  Then Y satisfies (S1_kappa).
Proof.  Add the terms of Y - V0 one at a time; every intermediate V satisfies (ZP_kappa) and, inductively, (S1_kappa).  If
|V| = p + 2kappa - 1 (only V = V0): t0 <= kappa - 1, so L >= p + 1 and |V| >= p + kappa + t0: EXT'.  If |V| = p + 2kappa:
t0 <= kappa - 1 gives L >= p + 2 and |V| >= p + kappa + t0 (EXT'); t0 = kappa is EXT-p.  If |V| >= p + 2kappa + 1:
L >= p + 1 and |V| >= p + kappa + t0 for every t0 <= kappa (EXT').  []

## 4. Lemma PAIR [S(p)] (structure of a minimal counterexample, inductively)
Assume LS(p, kappa - 1) (true for kappa - 1 <= floor(2p/3) by S1-sharp).  Let Y be a counterexample to LS(p, kappa) of
length thr (WLOG by Corollary RED).  Then:
(a) for every term z, Y - z fails (S1_kappa) (no term lies in all long zero-sums);
(b) for every two terms z != z' (distinct occurrences), Y - z - z' contains a zero-sum of length exactly 2kappa (no two
    terms meet all 2kappa-zero-sums).
Proof.  (a) Otherwise PROP+ with V0 = Y - z (length p + 2kappa).  (b) Y - z - z' has length p + 2kappa - 1 = thr(kappa - 1)
and satisfies (ZP_kappa).  Without a zero-sum of length 2kappa it satisfies (ZP_(kappa-1)), hence (S1_(kappa-1)) by
LS(p, kappa - 1), hence (S1_kappa) with t0 <= kappa - 1, and PROP+ (V0 = Y - z - z') makes Y satisfy (S1_kappa).  []
Remarks.  (i) Under (a), the shortest long zero-sum T has length N <= thr - 2 (if N = thr, Y is the only long zero-sum and
any Y - z is (S1)), so X := Y - T has |X| >= 2.  (ii) Any two 2kappa-zero-sums Q1, Q2 meet in >= 2kappa - p - 1 terms (else
|Q1 u Q2| > thr); disjoint ones would form a long zero-sum of length 4kappa.  (iii) PROP+ also shows: a (ZP_kappa) sequence
containing an (S1_kappa) subsequence of length >= p + 2kappa satisfies (S1_kappa).

## 5. The sharper conjecture LS+ and its exact extremal family (not assumed)
LS+(p, kappa): every sequence of odd elements of C_(2p) satisfying (ZP_kappa) but not (S1_kappa) has length <= 3kappa + 1.
- LS+ implies LS (p + 2kappa + 1 > 3kappa + 1 as kappa < p) and implies S1-sharp (for kappa <= floor(2p/3) a long zero-sum
  has length >= 2p + 2 > 3kappa + 1).  At kappa = p - 1 it is Gao's s_(2p)(C_p) = 3p - 1 (classical; not used).
- Sharpness (verified here): for floor(2p/3) + 1 <= kappa <= p - 1 and any generator h, Y = h^a (3h)^b with
  a := 3kappa - p + 2, b := p - 1 has length 3kappa + 1, satisfies (ZP_kappa) and fails (S1_kappa).  Zero-sums are
  h^i (3h)^j with i + 3j in {2p, 4p} (a + 3b = 3kappa + 2p - 1 < 6p).  i + 3j = 2p needs j >= ceil((2p - a)/3) = p - kappa,
  so its lengths 2p - 2j are <= 2kappa; i + 3j = 4p has lengths 4p - 2j >= 2p + 2 (j <= p - 1) and is feasible
  (j = p - 1, i = p + 3 <= a iff 3kappa >= 2p + 1).
- Consistency with the finite aids (not premises): probe v12's maximal lengths of (ZP)-and-not-(S1) multisets are 16
  (p = 7, kappa = 5), 25 (p = 11, kappa = 8) and 28 (p = 11, kappa = 9), i.e. exactly 3kappa + 1 in every complete cell, and
  every longest multiset listed there is of the form h^a (3h)^b (e.g. 1^21 15^7 = h^7 (3h)^21 with h = 15 = 3^(-1) in Z_22).
  LS's threshold exceeds the extremal length by p - kappa (2 at kappa = p - 2).
- Structural remark toward LS+ (S1-sharp Step 2 argument): if a shortest long zero-sum T has |T| >= 3kappa + 1, every proper
  zero-sum of T is minimal (three nonempty proper zero-sums T'' < T' < T would give |T| <= 3kappa), i.e. T has two atoms.

## 6. Exact remaining obstruction for LS (relative to S(p) and inductively LS(p, kappa - 1))
A sequence Y of length p + 2kappa + 1 with (ZP_kappa) such that no term lies in all long zero-sums and no two terms meet all
2kappa-zero-sums.  No contradiction is derived here.
