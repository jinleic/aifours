# Theorem C (version r1): the defect-set argument for general run structures in item (iii), under the Lemma CORE hypothesis (H)

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).
Written in c3/ after host clock 2026-10-17T12:34:43-0700 (freeze time and SHA-256 in c3/out/freeze.txt).
Task OlsonRunCount3 (cycle 3), item (iii) of ../proof-MH.md Sec. 6.  Imported, not re-proved: Lemma H with the
07:39 correction (../../../inverse-parity/proof-PAR-K0.md Sec. 1), the Claim in the proof of Lemma BC (same
file, Sec. 2), Lemma L and Lemma CORE (c3/proof-NOLP-r2.md Sec. 1 = c2/proof-NOLP.md Sec. 1).
Scope: the words of item (iii) (more generally every NMH word with R <= 2p - 3, ZSI-B words included) that satisfy
the phi-independent hypothesis (H) below and a bound on the number of even-length aligned runs.  (H) is decidable
for each run datum by a finite computation (c3/cert.cpp, census3.cpp); it is NOT proved here for any infinite
family (c3/proof-WALL.md avoids (H) for W(p, kB), 3kB <= p + 4, by certifying only the patterns its own argument
uses).  NOT a proof of NMH(p), MIX_DEF_HIGH(p), RUNS(p), INV or ordered Olson for D_{2p}.
(Version r1: replaces the unfrozen draft c3/proof-C.md, whose scope sentence wrongly said that Lemma CW proves (H)
for an infinite family, and whose Remark (3) called Theorem W-ALL a special case of Corollary S; both corrected here.
The mathematics of Secs. 0-2 is unchanged.)

## 0. Setting

p >= 5 prime; w an NMH word (../README.md Sec. 1) with R <= 2p - 3: all reflection runs odd, k >= p + 1 rotation
runs, every run pure or a (1,1)-pair, 1 <= B <= kappa - 1, B <= A <= 2p - 1.  kB := kappa - B >= 1,
D := A - B = 2p - k + 2kB, R = 2p - k + 2kappa.  R <= 2p - 3 gives
   k >= 2kappa + 3 = 2kB + 2B + 3,                                                                        (0.1)
and the total excess E := R - k = sum_t (r_t - 1) satisfies E/2 = p - k + kappa and E <= p - 4.  Run classes:
aligned (a_t >= 1 letters rho_1, d_t = a_t), anti (b_t >= 1 letters rho_{-1}, d_t = -b_t), pair (one of each, d_t = 0);
their numbers n_al, n_an, n_pr; B = sum_anti b_t + n_pr.  n_ev := number of runs with d_t even (pairs, even
aligned runs, even anti runs; n_ev,al and n_ev,an the latter two numbers).  Every aligned run has a_t <= E + 1 <= p - 3.
Lemma H (beta = 0): lambda(Q) = min(p - m(Q) + 1, D_Q + m(Q) - kB, floor((D_Q + B)/2) + 1) for proper Q; in NMH the
empty and full patterns never kill.
(H): every proper pattern is certified by singleton extension (Lemma L), and some proper Q0 with Q0, Q0^c
certified has lambda(Q0) + lambda(Q0^c) >= 1.
Consequence of (H) (Lemma L + the pin of Lemma CORE): if w avoids, there are integers x_t (t a run) with
   sum_t x_t = p   and   X_Q := sum_{t in Q} x_t >= lambda(Q)  for every proper Q.                      (0.2)
(X_[k] = X_{Q0} + X_{Q0^c} lies in [lambda(Q0) + lambda(Q0^c), 2p - lambda(Q0) - lambda(Q0^c)], a subset of [1, 2p-1],
and is = 0 mod p.)

## 1. Coordinates, the kill criterion, defects

For integers x_t put bh_t := 2x_t - d_t (so bh_t = d_t mod 2), c_t := d_t - x_t, f_t := floor((d_t - 1)/2),
eps_t := c_t - f_t, and for a pattern Q: c(Q), bh(Q), eps(Q) the sums over Q, m(Q) its number of blocks,
Phi(Q) := c(Q) + m(Q).  If sum x_t = p:
   sum_t bh_t = 2p - D = k - 2kB,      sum_t eps_t = K := kB + n_ev/2.                                 (1.1)
(sum c_t = D - p; sum f_t = sum (d_t - 1 - [d_t even])/2 = (D - k - n_ev)/2; D = 2p - k + 2kB.)
**Kill lemma.**  For a proper Q, X_Q < lambda(Q) iff
   (M) Phi(Q) >= kB + 1,   (Fl) bh(Q) <= B,   (P) X_Q + m(Q) <= p.
Proof: X_Q <= D_Q + m - kB - 1 iff c(Q) >= kB + 1 - m; X_Q <= floor((D_Q + B)/2) iff 2X_Q <= D_Q + B iff bh(Q) <= B;
X_Q <= p - m is (P).  []
So under (0.2) NO proper pattern satisfies (M), (Fl), (P) together; the proof below exhibits one.
Defects.  Z := {t : bh_t <= 0}, N := [k] - Z.  For t in Z, parity gives bh_t <= -[d_t odd], hence
x_t <= floor(d_t/2), c_t >= ceil(d_t/2), eps_t >= 1 and x_t <= c_t; for t in N, bh_t >= 1 + [d_t even] and eps_t <= 0.
Put s := sum_N (bh_t - 1) >= 0 and sur := -eps(N) >= 0, n_odd(Z) := number of odd-d runs in Z.  By (1.1):
   bh(Z) = |Z| - 2kB - s,   |Z| + n_odd(Z) <= 2kB + s   (as bh(Z) <= -n_odd(Z)),                       (1.2)
   eps(Z) = K + sur,   i.e.  c(Z) = f(Z) + kB + n_ev/2 + sur.                                            (1.3)
Z is nonempty (sum_t (1 - bh_t) = 2kB > 0) and Z != [k] (else sum bh_t <= 0 < k - 2kB by (0.1)); so m(Z) >= 1 and,
as the blocks of Z and of N alternate, 2m(Z) <= k.

## 2. Theorem C

**Theorem C.**  Let w be an NMH word with R <= 2p - 3 (in particular any word of item (iii)) satisfying (H), and
assume (i) n_ev,al <= 4, or (ii) 2kB <= p and n_ev,al <= 2kB + 2.  Then w has an identity 2p-subword.
**Corollary S.**  Every all-singleton word of item (iii) (every rotation run a single letter; any number B of
anti runs, any positions) satisfying (H) has an identity 2p-subword (n_ev,al = 0).

Proof of Theorem C.  Suppose w avoids; take x as in (0.2) and use Sec. 1.  Every Q below is proper.

Case A: Phi(Z) >= kB + 1.  Every Q contained in Z satisfies (Fl), as bh(Q) <= 0 < B.
(A-i) Under (i): X_Z <= sum_Z floor(d_t/2) <= sum_{aligned t in Z} floor(a_t/2) <= sum_{aligned t in Z} (a_t - 1)/2
+ n_ev,al/2 <= E/2 + 2, and m(Z) <= k/2, so X_Z + m(Z) <= p - k + kappa + 2 + k/2 = p + 2 - (k/2 - kappa) <= p + 1/2 by
(0.1); being an integer, X_Z + m(Z) <= p.  So Z satisfies (M), (Fl), (P): contradiction.
(A-ii) Under (ii): for every defect t, the singleton constraint X_{t} >= lambda({t}) gives
c_t <= d_t - lambda({t}) = max(kB - 1, ceil((d_t - B)/2) - 1, d_t - p) <= max(kB - 1, (p - 5)/2) <= p - kB - 1
(d_t <= p - 3; 2kB <= p).  If Phi(Z) <= p let Q := Z.  Otherwise delete from Z, one run at a time, a run with at most
one neighbour in the current set (it exists: the current set is not [k]).  Deleting t changes Phi by -c_t (t was an
end of a block of >= 2 runs) or -c_t - 1 (t was a block by itself): Phi drops by at most c_t + 1 <= p - kB per step.
The sequence ends at the empty set (Phi = 0); let Q be its first member with Phi(Q) <= p.  Its predecessor has
Phi > p, so Phi(Q) >= kB + 1: (M).  (Fl) holds as Q is contained in Z, and (P): X_Q + m(Q) <= c(Q) + m(Q) = Phi(Q) <= p
(x_t <= c_t on defects).  Q is nonempty (Phi(Q) > 0) and proper.  Contradiction.

Case B: Phi(Z) <= kB.  Put Delta := kB - Phi(Z) >= 0.  By (1.2), c(Z) = (D_Z - bh(Z))/2 = (D_Z - |Z| + 2kB + s)/2, so
   Delta = (|Z| - D_Z - s)/2 - m(Z);                                                                     (2.1)
by (1.3), Delta = -f(Z) - m(Z) - n_ev/2 - sur;                                                         (2.2)
and as c(Z) >= sum_Z ceil(d_t/2) and m(Z) >= 1,  Delta <= kB - 1 - sum_Z ceil(d_t/2).                  (2.3)
(B1) Free odd runs.  Let X be the set of aligned runs u notin Z with eps_u = 0 and no neighbour in Z, and X_o its
members of odd length; for u in X_o, c_u = f_u = (a_u - 1)/2, x_u = (a_u + 1)/2 and bh_u = 1.  Claim:
|X_o| >= 2 Delta + 2.  The aligned runs outside X are: aligned defects, at most c(Z) + sum_{anti t in Z} floor(b_t/2) of
them (aligned defects have c_t >= 1, pair defects c_t >= 0, anti defects c_t >= -floor(b_t/2)); aligned non-defects with
eps_u <= -1, at most sur = c(Z) - f(Z) - K of them (1.3); aligned runs adjacent to Z, at most 2m(Z).  With
2c(Z) + 2m(Z) = 2kB - 2Delta this gives
   |X| >= n_al - kB + 2 Delta + n_ev/2 + f(Z) - sum_{anti t in Z} floor(b_t/2).
Now f(Z) >= -n_pr(Z) - sum_{anti t in Z} ceil((b_t + 1)/2) (aligned f_t >= 0), and ceil((b+1)/2) + floor(b/2) = b + [b even];
extending the sums to all pairs and anti runs, sum_anti b_t = B - n_pr, n_an + n_ev,an <= B - n_pr and
n_al = k - n_an - n_pr give
   |X| >= k - kB - 2B + 2 Delta + n_pr/2 + n_ev,al/2,   so   |X_o| >= |X| - n_ev,al >= 2 Delta + (k - kB - 2B) - n_ev,al/2.
By (0.1) k - kB - 2B >= kB + 3, and kB + 3 - n_ev,al/2 >= 2 under (i) (kB >= 1) and under (ii).  []
(B2) The construction.  X_o is not the whole cycle (Z is nonempty), so its maximal blocks are paths, and every other
run of each block gives at least |X_o|/2 >= Delta + 1 pairwise non-adjacent runs; let S be Delta + 1 of them and
Q := Z u S.  No run of S has a neighbour in Z u S, so m(Q) = m(Z) + Delta + 1, and Q is proper (a neighbour of Z is
outside Q).
(M): Phi(Q) = Phi(Z) + sum_S (c_u + 1) >= (kB - Delta) + (Delta + 1) = kB + 1, as c_u + 1 = (a_u + 1)/2 >= 1.
(Fl): bh(Q) = bh(Z) + Delta + 1.  By (1.2) and (2.1), bh(Q) = (|Z| - s) + (|Z| - D_Z - s)/2 - 2kB - m(Z) + 1.  Use
|Z| - s <= 2kB - n_odd(Z) (1.2) and |Z| - D_Z = sum_Z (1 - d_t) <= n_pr(Z) + sum_{anti t in Z} (1 + b_t) <= B + n_an(Z):
bh(Q) <= -n_odd(Z) + B/2 + n_an(Z)/2 - s/2 - m(Z) + 1 <= B/2 + n_an(Z)/2 <= B   (n_an(Z) <= B).
(P): X_Z <= sum_Z floor(d_t/2) = f(Z) + n_ev(Z) (floor(d/2) = f + [d even]), and by (2.2) f(Z) = -Delta - m(Z) - n_ev/2 - sur,
so X_Z + m(Z) <= -Delta + n_ev(Z)/2.  For u in S, x_u + 1 = (a_u + 3)/2.  Hence
   X_Q + m(Q) <= -Delta + n_ev(Z)/2 + sum_S (a_u - 1)/2 + 2(Delta + 1) = Delta + 2 + n_ev(Z)/2 + sum_S (a_u - 1)/2.
By (2.3) (pairs have ceil(d/2) = 0), Delta <= kB - 1 - sum_{aligned t in Z} ceil(a_t/2) + sum_{anti t in Z} floor(b_t/2).  With
n_ev(Z) = n_pr(Z) + n_ev,an(Z) + n_ev,al(Z), [a even]/2 - ceil(a/2) <= 0 and floor(b/2) + [b even]/2 = (b - 1)/2 + [b even]:
   X_Q + m(Q) <= kB + 1 + sum_{anti t in Z} (b_t - 1)/2 + n_ev,an(Z) + n_pr(Z)/2 + sum_S (a_u - 1)/2 <= kB + 1 + E/2 + n_ev,an(Z),
since E >= sum_anti (b_t - 1) + n_pr + sum_S (a_u - 1) (pairs have r = 2; S and Z are disjoint).  With E/2 = p - k + kappa,
(0.1) and n_ev,an(Z) <= B/2 (even anti runs have b >= 2): X_Q + m(Q) <= p + 1 - (k - 2kB - B) + B/2 <= p - 2 - B/2 < p.
So Q satisfies (M), (Fl), (P): contradiction.  []

Remarks.  (1) Hypotheses used: (H) (through (0.2) and, in (A-ii), the singleton bound), R <= 2p - 3 through (0.1) and
E <= p - 4, k >= p + 1 (for E <= p - 4), all reflection runs odd (Lemma H with beta = 0), the run classes
(pure / (1,1)), B >= 1 only through n_an(Z) <= B; A <= 2p - 1 is not used beyond NMH membership.  The hypothesis on
n_ev,al enters only in (A-i)/(A-ii) and in (B1).  (2) The argument uses integrality (eps_t >= 1 on defects, bh_t odd for
odd d_t); by Lemma NOLP (c3/proof-NOLP-r2.md) no argument by real combinations of the same lifted constraints can
cover W(p, kB) for kB >= 4, p >= 4kB - 1.  (3) Theorem W-ALL (c3/proof-WALL.md) treats the B = 1 words of Corollary S WITHOUT (H): it uses
a variant of Case B with patterns of at most kB + 1 runs, whose certification (and the pin) is proved there for
3kB <= p + 4 (Lemma CW).  Corollary S itself needs (H) for every word it is applied to.

## 3. Exact computations [F] (aids; never hypotheses)

* thmC.cpp / thmC2.cpp (literal replay of the proof, every intermediate inequality asserted, final window
  violation checked against the lambda table): p = 7, ALL 51,641 item-(iii) words (incl. ZSI-B; all satisfy (H) and
  n_ev,al <= 2): 1,202,586 lift vectors (pair-feasible DFS vectors plus 30 random singleton-feasible vectors with sum p
  per word), Case A 914,041, Case B 288,545, 0 failures (out/thmC2_p7.txt; out/thmC_p7.txt pair-feasible only);
  p = 11: 3,000 random words (seed 1103), 2,807 tested (182 fail (H), 11 fail the n_ev,al hypothesis), 99,255 vectors,
  0 failures (out/thmC2_p11.txt); p = 13: 400 random words (seed 1303), 370 tested, 14,517 vectors, 0 failures
  (out/thmC2_p13.txt).
* Mutation controls (thmC_mut.cpp, out/thmC_mut_p7.txt): |S| = Delta instead of Delta + 1 makes (M) fail in all
  288,545 Case B instances; shrinking every window by one (lambda - 1 in the final test) makes 673,950 Case A and
  288,535 Case B kills fail; MUT = 0 reproduces the 0-failure run.
* (H) itself: census3.cpp (out/census3_p*.txt) and the map (README Sec. 8).
