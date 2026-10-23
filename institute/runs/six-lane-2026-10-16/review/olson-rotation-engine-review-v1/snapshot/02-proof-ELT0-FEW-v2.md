# Corollary ELT0-FEW: the kappa = 0 slice of ROT for 3o <= 2p + 1 (no SHgen), v2

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T06:37:56-07:00.  Status [W], UNREVIEWED.
v2 supersedes proof-ELT0-FEW-v1.md (kept unchanged): v1's range remark said "o <= 3 at p = 5, 7"; at p = 7 the
condition 3o <= 2p + 1 = 15 gives o <= 5.  No other change.
Imports: Lemma PM*, GRX (accepted, lowodd verdict v2); Corollary ELT0-ROT of proof-ELT0-v3.md (errata version of
ELT0-v2, which Codex reviewed ACCEPT-WITH-FIXES in R/olson-rotation-bundle1-codex-v1.note.md; v3 applies those fixes);
Lemma MULT (ii), (iii) of proof-ROT-few-v3.md (with Lemma SCHERK, GROW, Corollary SET there; all proved in that file).
Does NOT use Theorem SHgen, KB, KBH, B'(b) or C1.

## Statement

**Corollary ELT0-FEW.**  Let p >= 5 be prime and w an avoider of length 4p-2 over D_(2p) whose maximal cyclic
reflection runs are all constant, k >= 1 of them of odd length, with 3k <= 2p + 1, and with kappa = 0, i.e.
H := (F - k)/2 = p - 1.  Then all rotation letters of w are equal to one rho_c, c != 0.

## Proof

If R = 0 there is nothing to prove.  Iterated Lemma PM* (k >= 1 odd block) gives an avoider w^ of length 4p-2 with the
same rotation multiset, all k blocks odd, runs nonempty and blocks maximal, and the same H, so kappa = 0 and
R = 2p - k.  The all-plus pattern of GRX (Phi = 0, C_max = 2H = 2p - 2) forbids every zero-sum of even length in
[2, 2p] among Y(x) over the rotations: the sequence Y of length L = R = 2p - k is zero-sum-free in Z_(2p), with
e := 2p - 1 - L = k - 1.  As 3e + 2 = 3k - 1 <= 2p, Lemma MULT (iii), (ii) of proof-ROT-few-v3.md gives a generator
g = (1, c), c != 0, with Y = g^m (d_1 g) ... (d_q g), d_j odd >= 3, sum_j (d_j - 1) <= e and m >= e + 1.  In the
notation of ELT0 (weights a_x with (1, x) = a_x g) the weights are m ones and d_1, ..., d_q; listed in increasing order
each weight is at most 1 plus the sum of the smaller ones (d_j <= e + 1 <= m + 1), so (FULL) holds (ELT0-v3 Sec. 3).
Corollary ELT0-ROT (N = 4p-2, kappa = 0, (FULL), w^ avoids, all-odd RGR-shape form) gives E = 0: every rotation of w^,
hence of w, is rho_c.  []

## Scope and remarks

* With kappa = 0 the conclusion is stronger than ROT: all rotations are equal (B = 0), as in the accepted rigid
  normal form.
* Range: every o with 3o <= 2p + 1 (o <= 3 at p = 5; o <= 5 at p = 7; o <= 7 at p = 11; o <= 9 at p = 13; o <= 11 at p = 17), only
  for kappa = 0.  ROT-FEW (proof-ROT-few-v3.md, conditional on SHgen) covers every kappa but only 5o <= 2p + 4.
* CONDITIONAL REMARK (no import): if the Savchev-Chen structure theorem for zero-sum-free sequences of length > p in
  Z_(2p) were supplied with its exact statement, the same proof would give the kappa = 0 slice for every o < p.
* Observation [O] (existing data, not a premise): among the normalised avoiders listed in out/bases_p5_N18.txt (3,730)
  and out/bases_p7_N26.txt (3,738), all have constant runs, o <= p, and kappa in {0, o - 1}; kappa = 0 occurs for every
  o from 1 to p.
* Not ROT(p), INV*(p) or ordered Olson; no novelty claim.
