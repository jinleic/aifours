# Notes on regime (III) for B = 0 (R <= 4 kappa - 5 after B0S-CJ'''): representation, exact facts, finite aids

Owner OlsonReflectionRigidity.  r2 written after host clock 2026-10-18T10:02:31-0700: the sign of omega in Sec. 2 (W) is corrected, and the
E15/E15b census results are added in Sec. 3b.  r1 (82548b93...b1f) is kept unchanged.  r1 was written after host clock 2026-10-18T07:56:49-0700.  Status: working notes [W].  Secs. 1-2 are proved here.
Sec. 3 holds finite aids only (not premises).  Sec. 4 gives the open map.  No claim about REFL(p), INV*(p) or ordered Olson.

## 1. The v-formulation (exact)

Setting: B = 0, all blocks odd, kappa >= 1, an avoider.  P0 gives n_E <= 2 kappa, R >= p and Delta := p + kappa - 1 - R
<= kappa - 1.  For a run t put v_t := u_t - r_t, and for a pattern P put v_P := u_P - E (E = R_P), so v is additive.
The H0 window of an m-interval pattern (B0S-r4 Imports), written in v, says that v_P (mod p) lies in
   A_m(E) := [l_m(E), h_m(E)],
   l_m(E) = min(p - m - E + 1, m - kappa, 1 - ceil(E/2)),
   h_m(E) = max(m - 1 - E, Delta + 1 - m, p - 1 - floor((R + E)/2)).
(This is the complement of [-g_m(R - E), g_m(E)] - E.  It holds whenever the window is nonempty; otherwise P imposes nothing.)
For intervals (m = 1) set alpha(E) := max(0, ceil(E/2) - kappa) and beta(E) := max(0, ceil((R - E)/2) - kappa).  Then
A_1(E) = [1 - kappa - alpha(E), Delta + beta(E)].  Note alpha(R - E) = beta(E).
- "Light": E <= R - 2 kappa - 1 (beta > 0).
- "Heavy": E >= 2 kappa + 1 (alpha > 0).
- "Middle": otherwise; there A_1 = [1 - kappa, Delta] and A_2 = [2 - kappa, Delta - 1].
Separation therefore shrinks the allowed set by one at each end in the middle range.
Total: v_[k] = -R = mu := Delta - kappa + 1 (mod p).

## 2. Two exact identities

(C) Complement.  For every proper interval Q, with v*_Q the representative of v_Q in A_1(m_Q): v*_Q + v*_(Q^c) = mu, exactly.
Proof: A_1(m) + A_1(R - m) = [mu - N', mu + N'], N' := kappa + Delta - 1 + alpha + beta = |A_1(m)| - 1 <= p - 2 < p.  []
(W) Winding cocycle.  For a 3-partition of the cycle into consecutive arcs X, Y, Z put omega(X, Y, Z) := (v*_X + v*_Y + v*_Z - mu)/p.
* omega is an integer, takes values in {-1, 0, 1}, and is symmetric.
* It equals the c-defect of each of the three splits: c(X u Y) - c(X) - c(Y) = +omega.  [r2: r1 printed -omega.  Indeed
  c(X u Y) - c(X) - c(Y) = (v*_X + v*_Y - v*_(X u Y))/p = (v*_X + v*_Y + v*_Z - mu)/p, by (C).]
* It satisfies the 2-cocycle identity on 4 cuts.
* J (proof-B0SPP-r5.md) is the sum of omega over any triangulation of the k-gon of cuts.
An upward wrap (omega = +1) needs beta(m_X) + beta(m_Y) + beta(m_Z) >= theta+ := 2R - p - 3 kappa + 3.
A downward wrap (omega = -1) needs the alpha-sum >= theta- := R - 3 kappa + 3, i.e. a heavy arc and two light arcs of total
<= 4 kappa - 5 - R.  ((C) and (W) are pure arithmetic of the windows; the (A')/(B') conditions of Lemma C1 are the
"no wrap" conditions.)

## 3. Finite aids (pre-registered; not premises)

The plan files' "~HH:MM" labels in plan-E14c ... plan-E15 were estimates and ran ahead of the clock.  The file mtimes (host
clock) are authoritative: plan-E14 07:19:14, E14b 07:23:54, E14c 07:39:31, E14d 07:40:43, E14e 07:43:33, E14f 07:45:46,
E15 07:47:56, E15b 07:5x.  Each plan's mtime precedes its output's mtime (e14 07:20:37, e14b 07:24:47, e14c 07:40:07,
e14d 07:41:08, e14e 07:44:26, e14f 07:45:58, e15 07:49:06).
- E14 / E14b (interval-feasible DFS leaves; c on all proper intervals):
  - c = 0 everywhere and J = 0 in all 252,000 leaves of
    (p, kappa, R) = (7,3,7), (11,4,11), (11,5,13), (13,5,16), (13,6,17), (11,4,12), (7,3,8);
  - c != 0 and J in [-4, 3] for (7, 4, 7), where R <= 2 kappa and the interval windows are empty.
- E14c / E14d: interval-level SIGMA FAILS in parts of IIIa.
  - c != 0 and J != 0 in interval-feasible data at (13,6,13), (17,8,17), (13,6,14), (11,5,11) (theta+ <= 0), and at (17,7,18)
    (theta+ = 1, theta- = 0).
  - c = 0 everywhere at (19,8,21), (17,6,18), (19,7,20).
  - So no interval-level SIGMA can hold throughout regime III.
- E14e / E14f: every tested interval-feasible leaf, whether J != 0 or J = 0, is killed by a 2-interval pattern.  This covered
  4 IIIa cells and 4 IIIb cells, 2,000 + 6,600 leaves.  These leaves are random-like, so the evidence is weak.
- E15 (exhaustive): in the cell (kappa, k, R) = (3, 13, 7) at p = 7, NO assignment satisfies every interval window and every
  2-interval window.  All 132 run data were searched, in 70,759 DFS nodes.  So (given H0) that cell has no avoider.
- E15b: the same census for the other 21 uncovered p = 7, B = 0 cells.  Running; results go to out/e15b_<kappa>_<k>.json.

## 3b. p = 7, B = 0 census (E15, E15b; plan-E15.md, plan-E15b.md; code/e15_two_avoiders.py 133eeb7a...144d,
code/e15b_census_v2.py 5c9b9b57...0a7e)

The search is exhaustive over run data with P0 (e_R <= 2 kappa) and residues u.  It prunes by every interval and 2-interval
window; survivors get the m = 3 test and then the full 2^k check.
| (kappa, k, R) | run data | DFS nodes | 2-avoiders | killed at m = 3 | full avoiders |
|---|---|---|---|---|---|
| (3, 13, 7) | 132 | 70,759 | 0 | - | 0 |
| (4, 9, 13) | 22,610 | 1,133,384 | 0 | - | 0 |
| (4, 10, 12) | 28,910 | 1,792,683 | 0 | - | 0 |
| (4, 11, 11) | 29,063 | 4,679,290 | 0 | - | 0 |
| (4, 12, 10) | 21,532 | 4,440,755 | 0 | - | 0 |
| (4, 13, 9) | 10,780 | 5,922,302 | 2 | 2 | 0 |
| (4, 14, 8) | 3,220 | 2,679,882 | 380 | 380 | 0 |
| (4, 15, 7) | 429 | 3,533,152 | 54,927 | 54,927 | 0 |
| (5, 11, 13) | 104,006 | 14,042,780 | 0 | - | 0 |
| (5, 12, 12) | 111,682 | 19,521,467 | 0 | - | 0 |
| (5, 13, 11) | 97,818 | 50,562,997 | 0 | - | 0 |
| (6, 13, 13) | 400,024 | 259,068,553 | 2 | 2 | 0 |
(4, 15, 7) was run with v1 (full check for every survivor).  Interrupted and UNKNOWN: (5, 17) (exit 152, then exit 143 in the
09:25:49 SIGTERM event).  The remaining IIIb cells are run by E15c (plan-E15c.md) with 3-pattern pruning.
Reading (an aid, not a premise):
* In the IIIa cells, intervals plus 2-interval patterns already leave at most 2 survivors per cell.
* In the IIIb cells, 2-avoiders are abundant, and every one found so far is killed by a 3-interval pattern.

## 4. Open map for B = 0, k >= p + 1 (after B0S-CJ, proof-B0SCJ-r2.md, and B0S-CJ''', proof-B0SCJx-r4.md)

Covered:
- R >= 4 kappa + 1 with p >= kappa + 5 Delta - 5 or Delta <= 1;
- 4 kappa - 4 <= R <= 4 kappa with 2 kappa <= p - 1 and the same numerical condition (or a word-level (2HA)).
Open:
- (a) the numerical failures of Corollary 2 (large Delta; first (13, 4, 13, 3, 21) and (29, 7, 6) / (31, 7, 6));
- (b) the edge cells kappa = (p + 1)/2, R >= 2p - 2 (only (U1)/(L1) of Case I are missing);
- (c) deep IIIa, 2 kappa < R <= 4 kappa - 5;
- (d) IIIb, R <= 2 kappa.
In (c) and (d), interval-level SIGMA is false in general (E14c/d).  A proof must use multi-interval patterns directly.  The data
suggest that intervals together with 2-interval patterns already suffice (E15, E14e/f).
Proof route suggested: let (a, b] be a middle interval with the extreme representative Delta (or 1 - kappa).  Separation then
forces every middle interval separated from it to have representative <= -1 (resp. >= 1).  Combined with (C) and the
genuineness of empty runs, this should force a counting contradiction.  Not done.
