# Notes: the Savchev-Chen-type lemma at length exactly p (what is proved, what remains), v2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T07:24:30-07:00 (v2 at 07:28:08).  v2 = v1 with the
garbled last sentence of (1f) replaced (s = 3 case); no other change; v1 kept.  Status: NOTES [W]; partial results
with proofs, an exact open step, and finite observations.  No claim of the lemma itself.  No import of Savchev-Chen.
Purpose: the kappa = 0 slice of ROT for constant runs would be complete for every o (o <= p always holds there) if
S(p) below were proved: ELT0 (proof-ELT0-v3.md) then applies exactly as in proof-ELT0-FEW-v2.md.

## 0. Statements

"Odd" elements of Z_(2p) = Y(x) = (1, x).  For a generator g, a_y(g) in {1, 3, ..., 2p-1} with y = a_y(g) g.
SC(Y): some generator g has sum_y a_y(g) <= 2p - 1.  FULL(Y, g): the subset sums of the weights a_y(g) fill an integer
interval [0, W].  S(L): every zero-sum-free sequence of L odd elements is SC.  Known (proof-ROT-few-v3.md MULT (iii),
(ii)): S(L) for 3L >= 4p - 1.

## 1. Proved here

(1a) SC and L >= p imply FULL.  Proof: sort the weights; if FULL failed at a heavy a* > 1 + (sum of the smaller
weights) >= 1 + m (m = number of ones), the total would exceed 2m + 1 + 3(q - 1) where q = L - m heavies, giving
2p - 1 >= 2L + q - 1 >= 2L, i.e. L <= p - 1/2.  []
(1b) Upward step: if L >= p + 1 and S(L-1), then S(L).  Proof: Y - y is SC and, by (1a), FULL with top W' >= L - 1 >= p
for some g; y = d g; zero-sum-freeness gives d <= 2p - 1 - W' <= p - 1 <= W' + 1, so the interval extends: Y is SC with
total W' + d <= 2p - 1.  []  Hence S(p) implies S(L) for every L >= p.
(1c) At L = p: if some Y - y is SC then Y is SC.  Proof: if Y - y is FULL argue as in (1b) (W' >= p - 1, a jump would
need d >= p + 1 and d <= 2p - 1 - W' <= p).  An SC sequence of length p - 1 that is not FULL is g^(p-2) (pg) (the only
case allowed by the computation in (1a) with L = p - 1: one heavy a* in {p}); its subset sums are [0, 2p-2] minus
{p - 1}, so the only odd y keeping Y zero-sum-free is y = g, and g^(p-1)(pg) is SC.  []
(1d) Consequently S(p) is equivalent to SAT(p-1): "every zero-sum-free odd sequence of length p - 1 that is not SC is
saturated" (contains every odd element among its subset sums).  [SAT(p-1) => S(p): a non-SC Y of length p has every
Y - y non-SC by (1c), hence saturated, so -y is a subset sum of Y - y: zero-sum.  S(p) => SAT(p-1): a non-saturated
Z extends to a zero-sum-free Z y of length p, which is SC, hence so is Z.]
(1e) AP framework.  Fix a generator g; T := the longest FULL prefix of the sorted g-weights (top M), U := the other
terms ("jumpers"), t := |U|, n_A := |T| <= M, s := p - M.  Zero-sum-freeness gives every jumper weight in
[M + 2, 2p - M - 1] (so M <= p - 2 if t >= 1) and: every nonempty sub-multiset of U has weight sum (mod 2p) in
[1, 2p - M - 1].  If L >= p then t = L - n_A >= s.
(1f) Lemma (small s).  If 3s <= p + 3 there is no such configuration with t >= s (any g, any L).  Proof: write the
jumper weights p + delta, delta even in [-(s-2), s-1].  For a sub-multiset of size j with delta-sum D the condition reads:
j even: D mod 2p in [1, p + s - 1]; j odd: D mod 2p in [p + 1, 2p - 1] u [0, s - 1].  Two deltas with sum <= 0 would
need a sum <= s - p - 1 < -2(s-2) (as 3s <= p + 4): impossible, so at most one delta <= 0 and the other t+ >= t - 1 >= s - 1
are >= 2.  For the positive deltas, the odd-size partial sums of any ordering start <= s - 1 and grow by <= 2(s - 1)
per two steps; reaching [p + 1, ...] from <= s - 1 needs 3s - 3 >= p + 1, false; so every odd-size partial sum is
<= s - 1, while it is >= 2(t+ - 1) for the largest odd size: t+ <= (s+1)/2.  With t+ >= s - 1 this forces s <= 3;
s = 2 leaves only delta = 0 (the element (1,0), multiplicity <= 1 < t); s = 3 (so p >= 7 here) leaves deltas in
{0, 2} with at most one 0, and three of them have D in {4, 6}, outside [p + 1, 2p - 1] u [0, 2]: forbidden for j = 3.  []
(1g) So at length p a stuck AP process (t >= 1) must have M <= (2p - 4)/3, for EVERY generator g.

## 2. The open step and why the multiplicity hypothesis is needed

Open: the case M <= (2p - 4)/3 (s >= (p + 4)/3) with g a MOST FREQUENT value.  The multiplicity hypothesis (every
jumper value occurs at most m <= M times) is essential: without it the analogue of (1f) fails, e.g. for p = 1 mod 3
the sequence g (3g)^(p-1) (length p, zero-sum-free; checked by hand for p = 7) has M = 1 relative to g and p - 1 jumpers;
it is SC relative to 3g.  A proof must therefore use the most frequent value (or a maximising generator) in the
large-s regime.

## 3. Finite observations [O] (out/sc_explore_v1.jsonl, 3e6268cb...a498; not premises)

p = 7, 11, 13, 17: all zero-sum-free odd multisets of length p and p + 1 are SC; at length p - 1 every non-SC one is
saturated and lies in the two classes g^(p-3)(pg)((p+2)g), g^(p-3)((p+2)g)^2; at length p the most frequent value's AP
process never stops early.

## 4. Use

If S(p) is proved (equivalently SAT(p-1)), then by (1b) S(L) for all L >= p, (1a) gives FULL, and Corollary ELT0-FEW's
proof gives: every constant-run avoider with kappa = 0 has all rotations equal, for every number of odd blocks
(kappa = 0 forces o <= p, i.e. L = R = 2p - o >= p), independently of SHgen.
