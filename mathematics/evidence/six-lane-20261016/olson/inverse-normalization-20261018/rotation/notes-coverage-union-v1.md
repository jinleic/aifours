# Notes: exact (p, o_F, F) coverage of K01 u ROT-KP u ROT-ZR u S1 (g) for 5 <= p <= 31, IF all were accepted, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T14:48:22-07:00.  Status: NOTES (conditional
bookkeeping).  Derived by hand from the stated hypotheses; no script was executed.  ROT-KP (proof-ROT-KP-v1.md,
472e43cf...800e) and ROT-ZR (proof-ROT-ZR-v1.md, e8903ff4...69a7) are UNREVIEWED non-premises; K01 and S1 (g) are
parent-accepted.  The parked ZR+ addendum is NOT used.  No novelty claim; no claim of unrestricted INV* or Olson.

## 1. Conventions and rule

- o := o_F, kappa := kappa(w) = p - 1 - (F - o)/2, so F = o + 2(p - 1 - kappa) and F = o (mod 2).  For an avoider of
  length 4p - 2: 0 <= kappa <= o - 1 (GRX; DAV with kappa^ <= k - 1), i.e. 2p - o <= F <= o + 2p - 2.
- "(p, o, F) covered" = the uniform conclusions hold: INV* for avoiders of length 4p - 2 and the increasing-order
  identity 2p-subword for words of length 4p - 1 with these (o, F) (the corollaries of each file state both, with the
  deletion ledger, which never raises o nor lowers F - o; words with kappa < 0 are trivial).
- (o, kappa) is covered iff every possible normal-form pair (k, kappa^) = (o - 2j, kappa - j), j >= 0, k >= 1,
  kappa^ >= 0, is covered by one of: K1 (k = 1); K01 (2 <= k <= p - 1, kappa^ <= 1); ROT-KP (k = p, kappa^ <= 1);
  S1 (g) with ZX (3k <= 2p + 1, kappa^ <= (p + delta*)/2); ROT-ZR (2 <= k <= p - 1, 2 <= kappa^ <= (p - 1)/2, (Lambda),
  (H'), (K'), p >= 7).  Restricted REFL needs o <= p, so o > p is never covered here.
- S1 (g) range: kappa^ <= k - 1 <= (2p - 2)/3 <= (p + delta*)/2 for every p <= 29 (delta* = 1, 1, 3, 3, 3, 5, 5, 7 for
  p = 5, 7, 11, 13, 17, 19, 23, 29), so every pair with 3k <= 2p + 1 is covered there; at p = 31 (delta* = 7) the only
  uncovered such pair is (21, 20) (the accepted first gap).
- ROT-ZR, with G(2) = -1, G(3) = 0, G(4) = 1, G(5) = 2, G(6) = 3, G(7) = 13/3, G(8) = 17/3:
  (Lambda) 8 kappa^ <= 4p - 3k + 5 or kappa^(2 kappa^ - 1) < p;  (K') 2k <= 2p - 2 - G(kappa^);
  (H') k - 1 + G(kappa^) <= 2p - 2 - 2 kappa^ (never binding below).
  Each condition weakens from (k, kappa^) to (k - 2, kappa^ - 1) (G is nondecreasing), so for o > (2p + 1)/3 the
  binding pair is j = 0, and lower pairs with 3k <= 2p + 1 are covered by S1 (g) (at p = 31 they never equal (21, 20),
  since kappa <= 7 there).
- Hence, with o_S := floor((2p + 1)/3) and K(p, o) := the largest covered kappa:
  - o <= o_S: every F (p = 31: every F except (o, F) = (21, 41), i.e. kappa = 20);
  - o_S < o <= p - 1: F >= F_min := o + 2(p - 1 - K(p, o)), i.e. kappa <= K(p, o);
  - o = p: kappa <= 1, i.e. F >= 3p - 4 (ROT-KP);
  - o > p: nothing.

## 2. Table (o_S < o <= p; covered iff F >= F_min, F = o mod 2)

| p | o_S | o : K(p, o), F_min |
|---|---|---|
| 5 | 3 | 4: 1, 10 (ROT-ZR needs p >= 7); 5: 1, 11 |
| 7 | 5 | 6: 2, 14; 7: 1, 17 |
| 11 | 7 | 8: 3, 22; 9: 2, 25; 10: 2, 26; 11: 1, 29 |
| 13 | 9 | 10: 3, 28; 11: 3, 29; 12: 2, 32; 13: 1, 35 |
| 17 | 11 | 12: 4, 36; 13: 4, 37; 14: 3, 40; 15: 3, 41; 16: 3, 42; 17: 1, 47 |
| 19 | 13 | 14: 4, 42; 15: 4, 43; 16: 4, 44; 17: 3, 47; 18: 3, 48; 19: 1, 53 |
| 23 | 15 | 16: 6, 48; 17: 5, 51; 18: 5, 52; 19: 5, 53; 20: 4, 56; 21: 4, 57; 22: 3, 60; 23: 1, 65 |
| 29 | 19 | 20: 7, 62; 21: 7, 63; 22: 6, 66; 23: 6, 67; 24: 6, 68; 25: 5, 71; 26: 5, 72; 27: 5, 73; 28: 3, 78; 29: 1, 83 |
| 31 | 21 | 22: 7, 68; 23: 7, 69; 24: 7, 70; 25: 6, 73; 26: 6, 74; 27: 6, 75; 28: 5, 78; 29: 5, 79; 30: 3, 84; 31: 1, 89 |

Binding constraint for each K (first failure at K + 1), all by hand:
- kappa^ = 2: (Lambda) holds as 6 < p; (K') is 2k <= 2p - 1: always.  So K >= 2 for every o <= p - 1 when p >= 7.
- kappa^ = 3: (Lambda) by 15 < p for p >= 17; for p = 11, 13 it needs 3k <= 4p - 19 (k <= 8, resp. 11).  (K') 2k <= 2p - 2.
- kappa^ = 4: (Lambda) by 28 < p for p >= 29; else 3k <= 4p - 27 (p = 17: k <= 13; 19: 16; 23: 21).  (K') 2k <= 2p - 3,
  i.e. k <= p - 2 (fails at o = 28 for p = 29 and o = 30 for p = 31).
- kappa^ = 5: (Lambda) 3k <= 4p - 35 (p = 23: k <= 19; 29: 27; 31: 29); (K') 2k <= 2p - 4.
- kappa^ = 6: 3k <= 4p - 43 (p = 23: 16; 29: 24; 31: 27); (K') 2k <= 2p - 5.
- kappa^ = 7: 3k <= 4p - 51 (p = 29: 21; 31: 24); (K') 2k <= 2p - 2 - 13/3.
- kappa^ = 8: 3k <= 4p - 59 (p = 29: 19; 31: 21): fails for every o > o_S; (kappa^(2kappa^ - 1) = 120 > p.)
- kappa^ <= (p - 1)/2 holds in every entry (largest: 7 <= 14, 15).

## 3. Exact complement within o <= p (avoider ranges), and remarks

- Uncovered: for o_S < o <= p, the F with 2p - o <= F <= F_min - 2, F = o (mod 2); all o > p; and at p = 31 the single
  pair (21, 41).  Example: p = 7, o = 6: F in {8, 10, 12}; o = 7: F in {7, 9, 11, 13, 15}.
- Outside the requested union (not used above): the accepted INV*-FEW / OLSON-FEW chain covers o <= 4 for p >= 7
  and, with the accepted p = 5 finite result, o = 4 at p = 5 for every F; this changes only the p = 5 row.
- With only the accepted parts (K01 and S1 (g)): same table with K(p, o) = 1 for o_S < o <= p - 1 and nothing at o = p.
