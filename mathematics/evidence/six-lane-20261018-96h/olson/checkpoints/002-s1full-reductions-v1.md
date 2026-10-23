# Checkpoint 002: S1-full attack, first reductions (written work only; unreviewed; no claim)

Owner ContinueOlson.  Written after /bin/date 2026-10-18T23:45:47-0700.  Supersedes nothing; continues checkpoint 001
(5d64419cecad3fa5054b30c47464a5f34f5e4f128e51d4a9cc1080eeaf9d6a71).  No computation run.

## Actual result (derivations to be frozen in evidence/ before any review request)

Setting: p prime, delta >= 3 odd, kappa = (p+delta)/2, (P1) p >= 3delta+4 (<=> 3kappa <= 2p-2), u := p+delta.
T = shortest zero-sum of length >= u+2 in a (ZP)-sequence of odd elements of Z_2p; N = |T| >= 2p+2; every proper
zero-sum of T is minimal with length in [l, u], l := N-u; D := u-l = 2u-N (even, <= 2delta-2).  [S1(g) steps 1-4 and
notes-ZX-residual (R1), accepted/derived under P1 only.]

R0 (minimal-delta normalization, new).  Induct on kappa (base S1+, kappa <= (p+1)/2).  If no proper zero-sum of T had
length exactly u, T itself would be a (ZP)-sequence at kappa-1 violating (S1) at kappa-1.  So some proper zero-sum Q
has |Q| = u >= p+3; by the imported index-one theorem (C_2p, length >= p+2) Q = (b_i g) with g an odd generator,
b_i odd, sum b_i = 2p.  Hence m := v_g(Q) >= (3u-2p)/2 = (p+3delta)/2 (vs S1(g)'s t >= p+4-2delta).

R1 (main constraint MC, new).  Q' := T-Q (minimal, length l).  For every proper nonempty W of Q' and every Q_1 <= Q
with coefficient sum = A_W (mod 2p): |W| <= |Q_1| <= |W| + D, because (Q-Q_1) W is a proper zero-sum of T.

R2 (extreme profile closed, new, to be re-checked).  If Q = g^m (3g)^n (m = (p+3delta)/2, n = (p-delta)/2): MC forces
(i) every term of Q' has coefficient <= D+1, (ii) residues in [1.5D+3, 2p-1.5D-3] are forbidden for proper prefixes
(spread of Q's representation lengths > D there; uses (m-4)/3 > D/2 <=> P1), (iii) proper prefixes never wrap, and
mass(W) <= D in the low region, mass in [p-delta, p-delta+D] in the high region; (iv) Q' has <= 2 copies of g.  Any
ordering of Q' then gives l <= D+4, i.e. p+delta <= 2D+4 <= 4delta, contradicting P1.  So the sharp extremal profile
(which at the threshold has m = p-2 exactly) is impossible under P1 alone.

## Exact blocker

General S_Q (Q's non-g terms) with large elements: Q' may then contain many g's (< min S_Q) and 'high' terms
(coefficient in [p+1, p+delta-1]) that let prefixes jump; the counting of R2 needs a replacement there.  Partial
handling found: a jump term needs coefficient >= p-3delta+3; if the low/high gap has width >= D+1 no ordering can cross.

## Next bounded action

Write the general-S_Q case analysis (big-element / gap-width / high-term cases), then freeze v1 of the written lemma in
evidence/ with a hypothesis map; then a frozen <=300 s stdlib probe plan (exhaustive small-p check of MC-consequences
and of the sequence statement where feasible, plus the parent-checked sharp family as positive control).
