# Erratum 1 to proof-CF-XT-v1.md, proof-ROW-v1.md, note-STAB-range-v1.md (wording/scope; no statement strengthened)

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T05:11:38-0700, on the parent's preflight message.  Applies to the frozen texts
proof-CF-XT-v1.md aa602d45e154a7787ac3f0270a3c26deb5e8c6a70736cf4a82c700f5368c191f, proof-ROW-v1.md a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d, note-STAB-range-v1.md
5b8faa3ab578c373e6fa01be32b10b476950f450f93a00580dd082366a630115 (none edited).  Where this erratum and a v1 text differ, the erratum governs.

## E1 (CF, kappa range)
proof-CF-XT-v1.md Sec. 0 and Lemma CF: read 'kappa is an INTEGER with 0 <= kappa <= p - 1, e := p - kappa (so 1 <= e <= p)'.
This is the range in which Lemma CF is claimed and proved: (a) uses rho := sigma(W) - pq in [0, e - 1] with e - 1 < p, so rho =
sigma(W) mod p, and the window [2kappa + 2, 2p] is nonempty; (b) does not involve kappa; (c) is arithmetic.  Lemma XT keeps its
own narrower range (p >= 7, kappa0 + 1 <= kappa <= p - 2).
## E2 (XT base)
proof-CF-XT-v1.md Sec. 2 proof, first paragraph: the parenthetical '(Lemma TV's E2/E3 computation at kappa - 1; re-derived for
the base below)' is replaced by: 'Lemma XT uses only that E2(kappa - 1) and E3(kappa - 1) satisfy (ZP_kappa), which is
re-derived below in CF form (for E3(kappa - 1) it is the case a = b = c = 0 of the last paragraph).  No statement about
(ZP_(kappa - 1)) is used, and the unreviewed Lemma TV is not used.'
## E3 (ROW, rho-wording; parent's preflight point)
proof-ROW-v1.md Sec. 3 (proof of Theorem U), the sentence 'For every V' <= V, W := W0 V' has delta0 <= |W| <= |W| + 2rho(W) <=
r + 2e - 2 <= 2p (e <= (p + 3)/2), so by CF (F) rho(W) is not in [0, e - 1]' is replaced by: 'Let V' <= V and W := W0 V', so
|W| >= delta0 and |W| <= r.  If rho(W) were in [0, e - 1], then delta0 <= |W| + 2rho(W) <= r + 2e - 2 <= 2p (r <= p - 2 and
e <= (p + 3)/2), contradicting CF (F).  Hence rho(W) avoids [0, e - 1].'
Sec. 4 (proof of Lemma ROW), the sentence 'Every W <= U with |W| >= delta0 has delta0 <= |W| + 2rho(W) <= 2p, so rho(W) is
not in [0, e - 1] (CF (F))' is replaced by: 'Let W <= U with |W| >= delta0.  If rho(W) were in [0, e - 1], then
delta0 <= |W| + 2rho(W) <= r + 2e - 2 <= 2p (hypothesis), contradicting CF (F).  Hence rho(W) avoids [0, e - 1].'
## E4 (ROW, exact scopes; restated, unchanged)
Lemma RS: any prime p; (a) 1 <= n <= |S|; (b) nonzero terms, K >= 0.  Lemma DGM-p and Theorem U: p >= 5 prime, integer kappa with
(p - 3)/2 <= kappa <= p - 1.  Lemma ROW: integer 0 <= kappa <= p - 1, any odd generator g, under the two stated hypotheses
r >= delta0 and r + 2e - 2 <= 2p.  LS-threshold dichotomy: floor(2p/3) + 1 <= kappa <= p - 2, a LS-counterexample of length exactly
p + 2kappa + 1, g = g0 of DGM-p.  Length-(3kappa + 2) dichotomy: |Y| = 3kappa + 2 with (ZP_kappa), conditional on a generator g with
v_g(Y) >= p - e (not guaranteed by anything proved).  None of these is LS, LS+ or STAB.
## E5 (range note wording)
note-STAB-range-v1.md: 'So STAB(p, p - 1) is false' is replaced by: 'So extending STAB to the endpoint kappa = p - 1 is false in
general: already at p = 11 (1^21 5^10), and in fact for EVERY prime p >= 7 by the following family; p = 5 is not decided here.'
Family (proof).  p >= 7, b in Z_p with b not in {0, 1, -1, 3, 3^(-1)} (possible as p >= 7).  Y := (1, 1)^(2p-1) (1, b)^(p-1) satisfies
(ZP_(p-1)) (proved in the note for any distinct a, b).  Put j0 := (-2/(b - 1)) mod p; j0 != 0, j0 != 1 (b != -1), j0 != 2 (b != 0),
so 3 <= j0 <= p - 1 and i0 := 2p + 2 - j0 is in [p + 3, 2p - 1].  (1, 1)^(i0) (1, b)^(j0) has length 2p + 2 and C_p-sum
i0 + j0 b = 2 + j0(b - 1) = 0 (mod p): a long zero-sum.  E2(p - 1) = h^(2p-1) (3h)^(p-1) and E3(p - 1) = h^(p-1) (3h)^(2p-1); as
2p - 1 != p - 1, Y = E2 forces h = (1, 1), 3h = (1, 3) = (1, b), i.e. b = 3, and Y = E3 forces h = (1, b), 3h = (1, 3b) = (1, 1),
i.e. b = 3^(-1).  Both are excluded.  []
