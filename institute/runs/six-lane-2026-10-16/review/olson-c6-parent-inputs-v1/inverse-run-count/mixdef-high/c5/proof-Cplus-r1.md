# Theorem C+ (version r1; a sharper count in step (B1) of Theorem C) and the exclusion of the 3 + 4 "hyp" words of the c3 samples

Version r1, written 2026-10-17T15:08:18-0700: replaces the UNFROZEN draft c5/proof-Cplus.md (never cited; kept, no deletion), whose
Remark (1) did not justify m(Z) >= 2 and whose Remark (3) did not say that the c4 coverage claim for the notH_cert words
is a cycle-4 [F] receipt.  Secs. 1-2 and the Corollary are unchanged.

Status: [W] written proof, NOT yet independently reviewed; [F] exact computation (aid only, never a hypothesis).
Written in c5/ after host clock 2026-10-17T15:07:36-0700 (freeze time and SHA-256 in c5/out/freeze.txt).  Task OlsonRunCount5, target T4 of
c5/README.md.  Paths "c3/...", "c4/...", "c5/..." are relative to mixdef-high/.
Imported (not re-proved): c3/proof-C-r1.md Secs. 0-2 (Theorem C, Codex ACCEPT): the setting (0.1), the hypothesis (H) and its
consequence (0.2), the coordinates bh, c, f, eps, Phi, the Kill lemma, defects and (1.1)-(1.3), and the proof of Theorem C,
which is reused VERBATIM except for the two places changed below; through it, Lemma H (corrected), the Claim of Lemma BC and
Lemma L / Lemma CORE (as listed in c3/proof-C-r1.md).
Scope: every NMH word with R <= 2p - 3 (in particular every item-(iii) word) that satisfies (H) and condition (i) or (ii+)
below; in particular the seven item-(iii) words of the c3 samples with open reason "hyp" (c3/out/map3_p11.txt lines
302-303, c3/out/map3_p13.txt lines 102-104).  (H) is a finite, phi-independent condition verified per word by exact
computation, exactly as for Theorem C; it is NOT proved here for any infinite family.  NOT a proof of NMH(p),
MIX_DEF_HIGH(p), RUNS(p), PAR(p), INV, INV* or ordered Olson for D_(2p).

## 1. Statement

Notation as in c3/proof-C-r1.md Sec. 0: kB = kappa - B >= 1, (0.1) k >= 2kB + 2B + 3, n_ev,al = number of even aligned runs,
n_pr = number of (1,1)-pairs.
**Theorem C+.**  Let w be an NMH word with R <= 2p - 3 satisfying (H), and assume
   (i) n_ev,al <= 4,   or   (ii+) 2kB <= p and n_ev,al <= 2(k - kB - 2B) + n_pr - 2.
Then w has an identity 2p-subword.
Remark.  By (0.1), k - kB - 2B >= kB + 3, so (ii+) holds whenever 2kB <= p and n_ev,al <= 2kB + 4 + n_pr; in particular
condition (ii) of Theorem C (2kB <= p and n_ev,al <= 2kB + 2) implies (ii+), and Theorem C+ contains Theorem C.

## 2. Proof

Suppose w avoids; take x as in (0.2) of c3/proof-C-r1.md and use its Sec. 1.  Every pattern below is proper.
Case A (Phi(Z) >= kB + 1).  Under (i): step (A-i) of c3/proof-C-r1.md verbatim.  Under (ii+): step (A-ii) verbatim; its proof
uses only 2kB <= p, the singleton constraint X_{t} >= lambda({t}) and d_t <= p - 3 (c3/proof-C-r1.md Sec. 0), not the bound
on n_ev,al.  Either way a pattern satisfying (M), (Fl), (P) is found: contradiction.
Case B (Phi(Z) <= kB).  Delta := kB - Phi(Z) >= 0, and (2.1)-(2.3) of c3/proof-C-r1.md hold (they use no hypothesis on n_ev,al).
X := the set of aligned runs u notin Z with eps_u = 0 and no neighbour in Z; X_o := its members of odd length.
(B1+) Claim: |X_o| >= 2 Delta + 1.
 Proof (the counting of c3's (B1), written out; only the last line differs).  An aligned run outside X is (a) an aligned
 defect, or (b) an aligned non-defect with eps_u <= -1, or (c) an aligned run adjacent to Z.  (a): aligned defects have
 c_t >= ceil(a_t/2) >= 1, pair defects c_t >= 0 and anti defects c_t >= ceil(-b_t/2) = -floor(b_t/2), so there are at most
 c(Z) + sum_(anti t in Z) floor(b_t/2) of them.  (b): non-defects have eps <= 0 and sur = -eps(N), so there are at most sur of
 them, and sur = c(Z) - f(Z) - K by (1.3) (K = kB + n_ev/2).  (c): at most 2m(Z).  With 2c(Z) + 2m(Z) = 2Phi(Z) = 2kB - 2Delta:
    |X| >= n_al - c(Z) - sum_(anti t in Z) floor(b_t/2) - sur - 2m(Z) = n_al - kB + 2Delta + n_ev/2 + f(Z) - sum_(anti t in Z) floor(b_t/2).
 Aligned runs have f_t >= 0, pairs f_t = -1 and anti runs f_t = -ceil((b_t + 1)/2); since ceil((b + 1)/2) + floor(b/2) = b + [b even],
    f(Z) - sum_(anti t in Z) floor(b_t/2) >= -n_pr - sum_anti (b_t + [b_t even]) = -n_pr - (B - n_pr) - n_ev,an = -B - n_ev,an
 (sums extended to all pairs and anti runs; sum_anti b_t = B - n_pr).  With n_ev = n_pr + n_ev,an + n_ev,al,
 n_al = k - n_an - n_pr and n_an + n_ev,an <= sum_anti b_t = B - n_pr (anti runs have b_t >= 1, even ones b_t >= 2):
    |X| >= k - n_an - n_pr - kB + 2Delta + (n_pr + n_ev,an + n_ev,al)/2 - B - n_ev,an
        >= k - kB - 2B + 2Delta + n_pr/2 + n_ev,al/2
 (this is the displayed inequality of c3's (B1)).  X - X_o consists of even aligned runs, so
    |X_o| >= |X| - n_ev,al >= 2Delta + (k - kB - 2B) + (n_pr - n_ev,al)/2.
 Under (ii+), (k - kB - 2B) + (n_pr - n_ev,al)/2 >= 1; under (i), it is >= (kB + 3) - 2 >= 2 by (0.1).  So |X_o| >= 2Delta + 1.  []
 [c3's step (B1) asked for |X_o| >= 2Delta + 2 and therefore needed (k - kB - 2B) + (n_pr - n_ev,al)/2 >= 2 (it also dropped
 the term n_pr/2); one run less suffices because of (B2+).]
(B2+) The construction.  X_o is disjoint from the nonempty set Z, so its maximal cyclic blocks are paths, of lengths
 L_1, ..., L_r with L_1 + ... + L_r = |X_o|.  Taking the 1st, 3rd, 5th, ... run of each block gives sum_i ceil(L_i/2) >= |X_o|/2 >=
 Delta + 1/2 runs, pairwise non-adjacent (two runs from different maximal blocks are not adjacent); being an integer
 > Delta, their number is >= Delta + 1.  Let S be Delta + 1 of them and Q := Z u S.  No run of S has a neighbour in Z u S
 (runs of X have no neighbour in Z), so m(Q) = m(Z) + Delta + 1, and Q is proper (a neighbour of Z lies outside Q).
 From here on the text of c3's (B2) applies verbatim: (M) Phi(Q) >= (kB - Delta) + (Delta + 1) = kB + 1 (c_u + 1 = (a_u + 1)/2 >= 1
 for u in X_o); (Fl) bh(Q) = bh(Z) + Delta + 1 <= B/2 + n_an(Z)/2 <= B (bh_u = 1 on X_o; (1.2), (2.1)); (P) X_Q + m(Q) <=
 p - 2 - B/2 < p ((2.2), (2.3), x_u + 1 = (a_u + 3)/2 on X_o, E/2 = p - k + kappa and (0.1)).  None of these uses a hypothesis
 on n_ev,al.  So Q satisfies (M), (Fl), (P): contradiction.  []

## 3. Corollary HYP (the c3 "hyp" words)

The item-(iii) words of the c3 samples whose open reason is "hyp" ((H) holds, Theorem C's condition on n_ev,al fails) were
regenerated by c5/map5.cpp (= c3/map3.cpp plus a dump of these words; same generator and seeds 1104, 1304; its other output
is byte-identical to c3/out/map3_p11.txt, map3_p13.txt).  They are (rotation run i has a_i letters rho_1, b_i letters
rho_(-1), followed by the reflection run of length l_i; s0 := (k - kB - 2B) + (n_pr - n_ev,al)/2):
 H1: p = 11, k = 13, kB = 1, B = 4, kappa = 5, E = 6, n_ev,al = 5, n_pr = 0, s0 = 1.5;
     a = [0, 1, 1, 2, 2, 0, 1, 2, 1, 0, 2, 1, 2], b = [1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0], l = [1, 1, 1, 1, 1, 3, 5, 1, 3, 1, 1, 3, 1]
 H2: p = 11, k = 13, kB = 1, B = 4, kappa = 5, E = 6, n_ev,al = 6, n_pr = 0, s0 = 1;
     a = [2, 0, 0, 2, 0, 1, 2, 0, 1, 2, 2, 2, 1], b = [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], l = [1, 3, 1, 1, 1, 1, 5, 1, 1, 1, 5, 1, 1]
 H3: p = 11, k = 13, kB = 1, B = 4, kappa = 5, E = 6, n_ev,al = 5, n_pr = 0, s0 = 1.5;
     a = [2, 1, 0, 2, 0, 1, 2, 2, 0, 1, 1, 1, 2], b = [0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], l = [1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 1, 3, 3]
 H4: p = 13, k = 15, kB = 1, B = 5, kappa = 6, E = 8, n_ev,al = 5, n_pr = 1, s0 = 2;
     a = [0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 1, 1, 1, 2, 2], b = [3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], l = [3, 5, 1, 1, 1, 1, 3, 1, 1, 1, 3, 3, 1, 1, 1]
 H5: p = 13, k = 15, kB = 1, B = 5, kappa = 6, E = 8, n_ev,al = 5, n_pr = 0, s0 = 1.5;
     a = [1, 1, 0, 1, 1, 0, 2, 2, 1, 1, 1, 1, 2, 2, 2], b = [0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0], l = [1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 1, 1, 1, 5]
 H6: p = 13, k = 14, kB = 2, B = 3, kappa = 5, E = 8, n_ev,al = 7, n_pr = 1, s0 = 3;
     a = [2, 2, 2, 1, 1, 2, 0, 1, 1, 2, 1, 2, 0, 2], b = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], l = [1, 3, 1, 1, 1, 7, 3, 1, 1, 1, 1, 1, 3, 3]
 H7: p = 13, k = 15, kB = 1, B = 5, kappa = 6, E = 8, n_ev,al = 5, n_pr = 0, s0 = 1.5;
     a = [1, 0, 1, 1, 2, 1, 2, 2, 1, 1, 0, 0, 0, 2, 4], b = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0], l = [3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 1]
**Corollary HYP.**  None of the seven words H1-H7 is an avoider.
Proof.  Each is an item-(iii) word ([F] out/hyprun.txt: all reflection runs odd, k in [p + 1, 2p - 2], R <= 2p - 3, runs pure or
(1,1), 1 <= B <= kappa - 1, B <= A <= 2p - 1, length 4p - 2, not ZSI-B), satisfies (H) ([F] map3/map5 certification DP; re-checked
by the independent c3/hcheck.py, out/hcheck_hyp.txt), and satisfies (ii+): 2kB <= p and s0 >= 1 (values 1.5, 1, 1.5, 2, 1.5, 3,
1.5 above).  Theorem C+ applies.  []
Remarks.  (1) For H1-H5 and H7 (kB = 1, k = p + 2, so D = 2p - k + 2kB = p, and every d_t <= 4 <= B + 2) the singleton
bounds give lambda({t}) = d_t, so the only integer x with sum p and X_{t} >= lambda({t}) is x = d; for it Z = the anti runs and
pairs (c = 0, so Phi(Z) = m(Z)), and m(Z) >= 2 = kB + 1 because in each of these six words the anti runs and pairs lie in at
least two blocks (H1: runs {0}, {5}, {9}; H2: {1, 2}, {4}, {7}; H3: {2}, {4}, {8}; H4: {0}, {4}, {6}; H5: {2}, {5}; H7: {1},
{10, 11, 12}); so Case A finishes ([F] out/cplus_replay_mut0.txt Part 1: all vectors end in (A-ii)).
(2) Independent of (H) and of this proof, the exhaustive avoider search c5/hypdfs.cpp (all proper patterns, Lemma H windows
with beta computed) finds no avoider for H1-H7 (out/hyprun.txt); with every window shrunk by 3 (H6: by 2) avoiders appear
(out/hypdfs_shrink.txt), so the search is not vacuous.
(3) c4/proof-INDstar-r1.md (Theorem IND*, Codex ACCEPT) covers every c3-sample word with open reason notH_cert according to
the cycle-4 [F] receipt c4/out/ind_star_ex.txt (its hypotheses are checked there with worst-case N for every open class of
the c3 maps; the c4 reviewer did not re-run that sample coverage, and it is not re-run here).  Granting that receipt, every
open item-(iii) word of the c3 samples (p = 11: 356 notH_cert + 3 hyp; p = 13: 87 notH_cert + 4 hyp) is excluded by a written
argument (Theorem IND* or Theorem C+); the c3-sample words labelled WALL or C were covered before.

## 4. Exact computations [F] (aids; never hypotheses)

* map5.cpp (out/map5_p11.txt, out/map5_p13.txt): regeneration of the c3 samples; non-dump output byte-identical to
  c3/out/map3_p11.txt and map3_p13.txt (checked with cmp); the seven hyp words dumped in full.
* hyprun.py + hypdfs.cpp (out/hyprun.txt): item-(iii) membership of H1-H7 from the run data, the quantities of Theorem C+,
  and the exhaustive search: no avoider at shrink 0, 1, 2 for H1-H5 and H7 and at shrink 0, 1 for H6 (an avoider at shrink 2);
  cross-check on all-singleton words: no avoider in W(11, 5..7), W(13, 6..9) (agreeing with c3/out/famdfs_W_high.txt,
  identical check counts).  out/hypdfs_shrink.txt: first shrink with an avoider = 3 (H1-H5, H7), 2 (H6).
* c3/hcheck.py (frozen c3 code, run read-only on out/hyp_dump.txt): (H) re-verified for all 7 words (out/hcheck_hyp.txt);
  mutation (condition (B) demanded with p + 1 + MUT): verdicts unchanged for MUT = 1, 2, 3, 4 (slack), 6 of 7 change at MUT = 6
  (out/hcheck_hyp_mut1..4.txt, mut6.txt).
* cplus_replay.py (out/cplus_replay_mut0.txt): Part 1, H1-H7, 30 vectors each (random and local-search near-feasible; for the
  six forced words all equal x = d): every vector ends with a pattern Q with X_Q < lambda(Q), lambda recomputed by an
  independent slow routine; every intermediate claim asserted; 0 failures.  Part 2 (the implication "(0.2) => contradiction"
  needs no (H)): 240 random item-(iii) words (own generator, p = 11, 13, 17, 19, anti runs in one block, 2kB <= p and (ii+);
  165 of them outside Theorem C's hypothesis), 7,200 vectors: 7,200 kills, 0 assertion failures, 4,208 Case B instances, 67 of
  them with |X_o| = 2Delta + 1 (where c3's (B1) requirement fails and (B1+)/(B2+) are needed).  Mutation controls:
  out/cplus_replay_mut1.txt (|S| = Delta): (M) fails in all 4,334 Case B instances; out/cplus_replay_mut2.txt (final test
  against lambda - 1): 4,709 no-kill.
