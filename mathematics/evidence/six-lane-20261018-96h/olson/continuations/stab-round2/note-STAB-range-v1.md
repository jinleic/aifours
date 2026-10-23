# Note: STAB is false at kappa = p - 1 (scout example verified by hand); exact range of STAB, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T04:53:25-0700.  Answers item 5 of run review/olson-priority-parent-note-v2.md
(84ed0775...).  Status: [W], elementary, unreviewed.  No computation.

## Claim
For every prime p >= 5 and all distinct a, b in C_p, the odd sequence Y_(a,b) := (1, a)^(2p-1) (1, b)^(p-1) over
C_(2p) = C_2 x C_p has length 3p - 2 = 3(p - 1) + 1 and satisfies (ZP_(p-1)) (no zero-sum of length 2p).  It fails (S1_(p-1))
iff it has a zero-sum of length >= 2p + 2.  In particular 1^21 5^10 over Z_22 (p = 11, kappa = 10) satisfies (ZP_10), fails
(S1_10), has length 31 = 3kappa + 1, and is neither E2(10) = h^21 (3h)^10 nor E3(10) = h^10 (3h)^21 for any generator h.
So STAB(p, p - 1) is false; STAB is stated (and only ever used) for floor(2p/3) + 1 <= kappa <= p - 2, as in
evidence/LSplus-scope-v1.md, addendum MAX v2 and STAB2-scope-v1.md.  LS+ at kappa = p - 1 is classical (s_(2p)(C_p) = 3p - 1),
as recorded by the parent.

## Proof
Odd elements of Z_(2p) are (1, x) in C_2 x C_p; a subsequence is a zero-sum iff it has even length and its C_p-coordinates sum
to 0.  A 2p-term subsequence (1, a)^(2p-j) (1, b)^j of Y_(a,b) (0 <= j <= p - 1, as 2p - j <= 2p - 1 forces j >= 1, and j <= p - 1)
has C_p-sum 2pa + j(b - a) = j(b - a) != 0 (0 < j < p, b != a).  So no zero-sum of length 2p.
1^21 5^10 over Z_22: (1, 1)^21 (1, 5)^10 in C_2 x C_11 (5 = (1, 5) as 5 is odd and 5 mod 11 = 5).  The subsequence 1^19 5^5 has
length 24 >= 2kappa + 2 = 22 and sum 19 + 25 = 44 = 0 (mod 22): a long zero-sum, so (S1_10) fails.  E2(10) and E3(10) for a
generator h have value-multiplicity pattern {21, 10} with the 21-fold value h (E2) or 3h (E3) and the 10-fold value 3h (E2)
or h (E3).  Matching 1^21 5^10: E2 needs h = 1, 3h = 3 != 5; E3 needs 3h = 1, h = 3^(-1) = 15 (mod 22) != 5.  Neither.  []
Remark.  The same check shows that at kappa = p - 1 the length-(3kappa + 1) extremal sequences form the much larger
classical family of s_(2p)(C_p)-extremal sequences; no classification is claimed here.
