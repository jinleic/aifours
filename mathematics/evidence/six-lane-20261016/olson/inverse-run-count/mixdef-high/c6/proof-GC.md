# Generic configurations at every run (Lemma GC); every NMH word with R <= 2p - 3 has an identity 2p-subword

Written 2026-10-18T00:06:52-0700 in c6/ (task OlsonRunCount5, cycle 6; parent direction 2026-10-17 23:3x: continue only the positive-excess
residual).  Status: Lemma GEN, Lemma GC and Theorem NMH-iii are [W] written proofs, NOT independently reviewed.  The controls of
Sec. 5 are [F] aids only; no finite computation is a hypothesis.  Paths are relative to mixdef-high/.  This file does NOT claim
NMH(p), MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson for D_(2p); Sec. 4 states the exact scope.

Imports (each used only inside its stated hypotheses):
 * the NMH setting and parameter identities of c3/proof-C-r1.md Sec. 0 and c6/proof-SEEDG-r2.md Sec. 0 ((0.1'), (0.2'));
 * Lemma H with beta = 0 (../../inverse-parity/proof-PAR-K0.md Sec. 1, with its 07:39 correction), in the form displayed in
   c6/proof-SEEDG-r2.md Sec. 0: lambda(Q) = lam(y, m), lambda(Q^c) = lamc(y, m), U(Q) = p - lambda(Q^c);
 * c6/proof-SEEDG-r2.md Sec. 1: the Definition of seeds and quality seeds (QS), Lemma NW and Lemma GS (a), (b), including the
   actual-empty alternative of its r2 delta (r1 reviewed ACCEPT-WITH-FIXES by Codex and Claude; r2 delta parent-accepted);
 * c6/proof-A0-r1.md: its Corollary (count-free seed certificate), cases (a) and (b), which runs through Theorem C0-all; the parent
   reported (IRC after 23:37) that the six versioned files are accepted at exact scope and that Lemma C0W is accepted, so the
   conditional import of C0-all is discharged in the NMH/lift setting (institute/runs/six-lane-2026-10-16/review/
   olson-c6-uniform-parent-verdict.md; not re-read by this worker).
Not used: SEED-G*, (QS*), (P2), Lemma QQ, the profile lemma, any class census or finite certificate (LB, X, X*, X**, the E2 315-row
table), and the region theorems RZ-wide, S2-wide, E-wide, S2-E, E-global, E2-*.  Their seed conclusions are re-derived here in
general, not cited.

## 1. Setting and notation

p >= 5 is prime and w is an NMH word with R <= 2p - 3 (c3 Sec. 0): k rotation runs on a cycle, all reflection runs odd, every run t
pure aligned (d_t = a_t >= 1), pure anti (d_t = -b_t <= -1) or a (1,1)-pair (d_t = 0); r_t is its number of letters and
e_t := r_t - 1 >= 0 its excess, E := R - k = sum_t e_t (even).  As in c6/proof-SEEDG-r2.md Sec. 0, kB := kappa - B >= 1, B >= 1,
Delta0 := 2p - R >= 3, A = p + kB + E/2, and
   D := A - B = sum_t d_t = 2kB + E + Delta0,    k = 2kappa + Delta0 >= 7,    p - kappa = E/2 + Delta0.            (1.1)
For every run |d_t| <= r_t = e_t + 1 (a pair has |d_t| = 0 = e_t - 1).  For a pattern Q (a set of runs) let y := D_Q = sum over Q
of d_t and m := m(Q) its number of cyclic blocks; Q is proper if it is neither empty nor [k].  By Lemma H (beta = 0), for proper Q,
   lambda(Q) = min(p - m + 1, y + m - kB, floor((y + B)/2) + 1),
   lambda(Q^c) = min(p - m + 1, A - kappa - y + m, floor((A - y)/2) + 1)     (m(Q^c) = m, D_(Q^c) = D - y).
Following Lemma GS (b), Q is GENERIC if lambda(Q) and lambda(Q^c) both equal their floor terms.  Since D_(Q^c) = D - y,
m(Q^c) = m, D - y + B = A - y and A - (D - y) = B + y, the two conditions for Q^c are exactly the two conditions for Q:
   (1.2)  a proper pattern Q is generic iff its complement Q^c is generic.

## 2. Lemma GEN (closed form of genericity)

**Lemma GEN.**  A proper pattern Q with y = D_Q and m = m(Q) is generic iff
   |4m - (k + 2)| + |2y - D| <= E + 2 Delta0.
Proof.  lambda(Q) equals its floor term iff (i) floor((y + B)/2) + 1 <= y + m - kB and (ii) floor((y + B)/2) + 1 <= p - m + 1;
lambda(Q^c) equals its floor term iff (iii) floor((A - y)/2) + 1 <= A - kappa - y + m and (iv) floor((A - y)/2) + 1 <= p - m + 1.
Write floor((y + B)/2) = (y + B - th)/2 with th := [y + B odd] and floor((A - y)/2) = (A - y - th')/2 with th' := [A - y odd].
Doubling,
   (i) 2m + y >= 2kB + B + 2 - th,  (ii) 2m + y <= 2p - B + th,  (iii) 2m - y >= 2kappa + 2 - A - th',  (iv) 2m - y <= 2p - A + th'.
Now 2m + y == y == B + th (mod 2), and both bounds in (i), (ii) are == B + th as well; hence (i) is equivalent to
2m + y >= 2kB + B + 1 (for th = 1 this is the same bound; for th = 0 the value 2kB + B + 1 has the other parity) and (ii) to
2m + y <= 2p - B + 1.  In the same way 2m - y == A + th' (mod 2) and (iii), (iv) are equivalent to 2kappa + 1 - A <= 2m - y <=
2p - A + 1.  Both intervals have length 2(p - kappa); with
   a1 := 2m + y - (p + kB + 1),     a2 := 2m - y - (p + kappa + 1 - A),
Q is generic iff |a1| <= p - kappa and |a2| <= p - kappa.  Using (1.1): a1 + a2 = 4m - (2p + kB + kappa + 2 - A) = 4m - (k + 2)
and a1 - a2 = 2y - (A - kappa + kB) = 2y - D.  Since max(|a1|, |a2|) = (|a1 + a2| + |a1 - a2|)/2 and 2(p - kappa) = E + 2 Delta0,
the lemma follows.  []

## 3. Lemma GC (a generic configuration at every run)

**Lemma GC.**  For every run t of w there is a proper pattern Q with t notin Q such that Q + t := Q u {t} is proper and both Q and
Q + t are generic.

Proof.  Put d := d_t, L := k - 1 and r_i := t + i (i = 1, ..., L, cyclic), the path of the other runs.  A colouring chi of [L] by
X, Y defines X(chi) := {r_i : chi_i = X} and Y(chi) := {r_i : chi_i = Y}; its blocks are the maximal intervals of constant colour.
Two runs r_i, r_j are cyclically adjacent iff |i - j| = 1 (the only other adjacency of the cycle passes through t, and r_1, r_L
are not adjacent since k >= 7).  Hence the cyclic blocks of the pattern X(chi) are exactly the X-blocks of chi, and likewise for
Y(chi).  If X(chi) and Y(chi) are both nonempty, Q := X(chi) is proper, t notin Q, Q + t = [k] - Y(chi) is proper, and by (1.2)
Q + t is generic iff Y(chi) is generic.  Moreover D_X(chi) + D_Y(chi) = D - d.

Choose m := floor((k + 4)/4).  Then c := |4m - (k + 2)| <= 2 (c = 0, 1, 2, 1 for k + 2 == 0, 1, 2, 3 mod 4), and k >= 7 gives
2 <= m and 2m <= k - 2 = L - 1 (k = 7: m = 2; k >= 8: 2m <= (k + 4)/2 <= k - 2).  Let C be the set of colourings with first colour
X, last colour Y, exactly m X-blocks and m Y-blocks.  A colouring in C is the same as a boundary vector
1 <= b_1 < b_2 < ... < b_(2m-1) <= L - 1 (block j is (b_(j-1), b_j], b_0 = 0, b_(2m) = L, odd-numbered blocks X).
For chi in C put v(chi) := D_X(chi) and W' := E + 2 Delta0 - c.  By Lemma GEN (both patterns have m blocks), X(chi) and Y(chi) are
both generic iff |2v - D| <= W' and |2(D - d - v) - D| <= W', i.e. iff
   v(chi) in [lo, hi],   lo := ceil((D - W')/2) + max(0, -d),   hi := floor((D + W')/2) - max(0, d).                  (3.1)

Two colourings in C.  chi0 has block lengths (1, 1, ..., 1, L - 2m + 1): 2m - 1 unit blocks, then a final Y-block of length
L - 2m + 1 >= 2.  chi* is obtained from chi0 by exchanging the two colours everywhere and then recolouring position 1 by X and
position L by Y.  After the exchange the blocks are Y, X, ..., Y, X with the same lengths.  Recolouring position 1 merges that
unit block into the following X-block (m >= 2), leaving m X-blocks and m - 1 Y-blocks; recolouring position L splits a final
Y-block of length 1 off the last X-block, whose length L - 2m >= 1 stays positive.  So chi* is in C, and
   v(chi0) + v(chi*) = D - d + d_(t+1) - d_(t-1) =: Sigma.                                                             (3.2)

A walk inside C.  Starting from the boundary vector b of chi0, first for j = 2m - 1 down to 1 raise b_j one unit at a time up to
b*_j (the boundary vector of chi*) whenever b_j < b*_j; then for j = 1 up to 2m - 1 lower b_j one unit at a time down to b*_j
whenever b_j > b*_j.  Every move keeps the vector strictly increasing: in the first pass b_(j+1) is already final (b*_(j+1) > b*_j)
or still at its initial value, which then exceeds b*_(j+1) > b*_j; in the second pass b_(j-1) is already final, b*_(j-1) < b*_j.
A unit move of b_j recolours exactly one position (b_j + 1 when raising, b_j when lowering), keeps every block nonempty and keeps
the colours of positions 1 and L, so all colourings chi^(0) = chi0, chi^(1), ..., chi^(N) = chi* of the walk lie in C, and
|v(chi^(i+1)) - v(chi^(i))| = |d_a| for a single run a != t.

Two inequalities.  (S) For every run a != t, |d_a| <= e_a + 1 <= E - e_t + 1; this is E + 2 - |d| if t is pure (e_t = |d| - 1) and
E if t is a pair (d = 0, e_t = 1).  Since W' - |d| >= E + 2 Delta0 - 2 - |d| >= E + 4 - |d|, every step satisfies
|d_a| <= W' - |d| <= hi - lo + 1; the last inequality is (3.1) with ceil(x/2) <= (x + 1)/2 and floor(x/2) >= (x - 1)/2.
(M) The runs t, t + 1, t - 1 are distinct, so |d| + |d_(t+1)| + |d_(t-1)| <= e_t + e_(t+1) + e_(t-1) + 3 <= E + 3 <= W'.  Hence
|d_(t+1) - d_(t-1)| + |d| <= W', which gives (using 2 max(0, -d) + d = |d| = 2 max(0, d) - d)
   2 lo <= D - W' + 1 + 2 max(0, -d) <= Sigma + 1   and   2 hi >= D + W' - 1 - 2 max(0, d) >= Sigma - 1.               (3.3)

Crossing.  Let v_i := v(chi^(i)); v_0 + v_N = Sigma by (3.2).  If v_0 lies in [lo, hi], take chi^(0).  If v_0 < lo, then
v_N = Sigma - v_0 >= Sigma + 1 - lo >= lo by (3.3); for the least i with v_i >= lo we have i >= 1, v_(i-1) <= lo - 1 and, by (S),
v_i <= lo - 1 + (hi - lo + 1) = hi.  If v_0 > hi, then v_N <= Sigma - hi - 1 <= hi, and the least i with v_i <= hi has
v_i >= hi + 1 - (hi - lo + 1) = lo.  In every case some chi in C has v(chi) in [lo, hi]; by (3.1) X(chi) and Y(chi) are generic,
and Q := X(chi) has the required properties.  []

Remarks.  (1) Only Delta0 >= 3 (through W' >= E + 4) and k >= 7 are used; E, kB, B, the run lengths and their positions are
arbitrary.  (2) Q may contain t + 1, i.e. t need not be isolated from Q; Lemmas TS and GS do not require isolation.  (3) The
lemma is constructive and linear in the word: the walk has at most (2m - 1)(L - 2) steps.

## 4. Theorem NMH-iii and its exact scope

**Theorem NMH-iii.**  For every prime p >= 5, every NMH word with R <= 2p - 3 (the setting of c3/proof-C-r1.md Sec. 0; in particular
every item-(iii) word of c3/README.md Sec. 1 and every ZSI-B word) has an identity 2p-subword.
Proof.  Let w be such a word.  For every run t, Lemma GC gives an actual configuration Q with t notin Q, Q and Q + t proper and both
generic.  By Lemma GS (b) of c6/proof-SEEDG-r2.md (with Lemma NW) the hypothesis of Lemma GS (a) holds and the GS (a) interval
[max(lambda({t}), s_lo), min(U({t}), s_hi)] is a quality seed of t, unless it is empty, in which case w does not avoid (proof of
Lemma GS (a): if w avoids, x_t lies in it).  Thus either some run has an empty seed intersection from actual configurations (case
(a) of the Corollary of c6/proof-A0-r1.md) or every run has a quality seed from actual configurations (case (b)).  In both cases
that Corollary, which needs no count condition and no defect bound and runs through Theorem C0-all, gives an identity 2p-subword.  []

Scope.  Theorem NMH-iii is item (iii) of ../proof-MH.md Sec. 6 together with its ZSI-B part, for all primes p >= 5, without any
region, count condition or finite certificate.  It supersedes, as a conclusion (not as a citation), the seed regions of
c6/proof-SEEDG-r2.md Secs. 4-5, c6/proof-RZwide-r1.md, c6/proof-S2wide-r1.md, c6/proof-Ewide.md, c6/proof-S2E.md,
c6/proof-Eglobal.md, the E2 files and the finite class censuses; none of them is used.  [I] c2/proof-C2.md proves (as [W]) the
NMH words with R >= 2p - 2; if that file and this one are accepted, NMH(p) and, through the reductions cited in README.md Sec. 1,
MIX_DEF_HIGH(p) would follow.  That assembly, and anything about RUNS(p), PAR(p), INV, INV* or ordered Olson, is left to the
parent and is NOT asserted here.

## 5. Controls [F] (aids, not hypotheses)

c6/gc_controls.py (sha256 a6c752163fee4e9a838983fe9647722d50296a3ffffb38746ad02c3d853604fc), one process, native RLIMIT_CPU
1200 s and RLIMIT_FSIZE 128 MiB, started 2026-10-18T00:03:58-0700, finished 00:06:30 (exit 0, empty stderr, child CPU 108 s,
peak child RSS 13,860,864 bytes); receipt c6/out/gc_controls.txt:
 * Part A (Lemma GEN): the closed criterion agrees with the floor-term definition on all 2,305,200 tuples (every NMH class with
   prime p <= 23, every 1 <= m <= k - 1 and -B - 2 <= y <= A + 2) and on 137,771 random tuples with p < 10^6 or p = 2^61 - 1 (the
   identity uses no primality): 0 mismatches.
 * Part B (Lemma GC on explicit words): 36,370 words (5 per NMH class, primes 5..31; generators with spread or concentrated excess,
   long runs adjacent or at distance <= 2, all anti runs in one block), 1,389,045 targets (930,955 with E >= 4).  The recipe is
   followed literally; every walk invariant and the inequalities (S), (M), (3.3) are asserted; the final X, Y and X + t are
   re-checked generic by an independent slow lambda computed from the explicit run list, and the Lemma GS seed computed from those
   lambdas satisfies (QS) and both no-wrap inequalities.  0 failures (any failure aborts the run).  5,739 GS intervals were
   actually empty (direct exclusions).  Longest walk: 51 steps.  In every target X contains t + 1 (Remark (2)).
 * Part C (exhaustive): every run-weight sequence of every NMH class at p = 5 (7 sequences, 49 targets) and p = 7 (2,591 sequences,
   23,556 targets): 0 failures; 8,117 of the p = 7 GS intervals were actually empty.
 * Part D (mutations; primes <= 23, 2 words per class, 121,352 targets each): D1, window widened by one on each side: 26,533 picks
   are not generic (detected by the slow lambda); D2, m := m + 2 with its own correct window: 594 targets have no colouring class
   and 15,397 walks never enter the window; D3, the Y-condition dropped: 4,082 picks detected as not generic.
These controls are this script's only; the exploratory kernel prototypes of c6/README.md Sec. 40 are not cited as evidence.
