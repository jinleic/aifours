# Lemma GR0: Lemma GR with empty rotation runs; reductions for INV*b-rig(p)

Owner OlsonParity2.  Written after host clock 2026-10-17T18:41:50-07:00.  Status: written proofs [W], unreviewed.
Imports: Lemma GR, Lemma WAS (../../../../proof-GR.md Sec. 2, ../../../../repr-WAS.md Sec. 1, 5; reviewed), Lemma H
(../../../proof-PAR-K0.md Sec. 1; reviewed), Theorem P (../../../../proof-theoremP.md; reviewed), Lemma Davenport-alpha
(../../../../proof-dihedral-partial.md Sec. 4; reviewed), Lemma M0 and Lemma PM (../../../../inverse-run-count/proof-RUNS.md
Sec. 12; M0 is inside the parent's olson-par2-closure reviews, not yet returned).  p >= 5 prime throughout; p = 3 is not
treated here.

## 0. Generalised RGR words

A word w over D_(2p) with F >= 1 reflections and all rotation letters in {rho_x, rho_-x}, x != 0, is a *generalised RGR
word*; normalise x = 1.  Cutting every maximal cyclic reflection run at each change of letter gives maximal constant
blocks S_1, ..., S_k (S_i = sigma_(y_i)^(l_i), l_i >= 1) and between S_(i-1) and S_i the rotation run R_i (a_i letters
rho_1, b_i letters rho_-1, r_i = a_i + b_i >= 0; y_0 := y_k).  R_i is *empty* if r_i = 0; then y_(i-1) != y_i by
maximality (theta_i := y_(i-1) - y_i != 0): a *genuine* empty run.  w is RGR iff it has no empty run (k >= 1).
More generally, any cyclic alternation R_1 S_1 ... R_k S_k with constant blocks and possibly empty rotation runs (adjacent
blocks may have equal values) is called a *representation* of w.

## 1. Lemma GR0 and its corollaries

**Lemma GR0.**  For every representation of a generalised RGR word w (any length N), with f_i, Phi, delta, C_max, E+,
E-, s0, s1, Ach(z), tau(z) defined from (a_i, b_i, l_i, y_i) exactly as in Lemma GR, w has an identity 2p-subword iff
some z in {+-1}^k has Ach(z) intersect (tau(z) + pZ) != empty.
Proof.  The proof of Lemma GR (proof-GR.md Sec. 2) applies verbatim; its steps never use r_i >= 1:
(1) a selection with an even number of reflections gives data (z; c_i; chosen rotations), z_i := the sign of the zone
    of R_i (parity of the selected reflections before R_i), defined also for empty R_i; c_i = f_i (mod 2);
(2) the ordered product is rho_V, V = sum_i z_i n_i + sum_{f_i = 1} z_i y_i, with n_i = 0 for an empty R_i (the blocks
    are constant, so the letters chosen from S_i multiply to sigma_(y_i) or 1);
(3) sum_{f_i = 1} z_i y_i = sum_i z_i (y_i - y_(i-1))/2 is an identity;
(4) the realisable C = sum c_i are the even numbers in [Phi, C_max] (block by block);
(5) a given t is realised iff the counts E+, E- of available effectively positive/negative rotations allow it; empty
    runs contribute 0 to both.
Conversely every admissible data point is realised by a selection, and identity subwords are invariant under cyclic
rotation.  []
**Corollary WAS0.**  w avoids iff for every P subset of [k]: sum_{i in P} theta_i notin Ach(z_P) (mod p),
theta_i := y_(i-1) - y_i.  (Proof of Lemma WAS: tau(z_P) = sum_{i in P} theta_i.)
**Corollary H0.**  Lemma H holds for generalised RGR words of length 4p-2 with H := sum_i floor(l_i/2) over BLOCKS,
kappa := p - 1 - H, o_F := number of odd blocks and beta(P) := number of even blocks among the 2m(P) boundary blocks (its
proof is algebra on WAS0).  In particular (P = empty pattern; A, B <= 2p - 1): the empty pattern kills iff
A, B >= kappa + 1, so an avoider has min(A, B) <= kappa.
**Corollary MP0.**  Lemma M0 (pair removal; adding sigma_y sigma_y to any block) and Lemma PM (merging R_j and R_(j+1)
across an even block S_j, the letters of S_j joining S_(j+1)) preserve avoidance for generalised RGR words: their proofs
compare half windows / pattern conditions only (Corollary H0, WAS0).  Both keep the length, every block value, and every
empty run other than R_j, R_(j+1) together with its two neighbouring block values.

## 2. Value-independent necessary conditions (generalised avoider of length N <= 4p - 1)

(a) A, B <= 2p - 1 (2p equal rotations multiply to 1).  (b) H <= p - 1 (p disjoint adjacent equal pairs inside blocks).
(c) Theorem P (any word, N <= 4p - 1; its gaps are the rotation runs, empty ones included): F + sum_i floor(r_i/2) <= 3p - 2.
(d) Davenport-alpha (F >= 2): R + H <= 3p - 2, using the H gaps "every second gap inside each block"; they are pairwise
    non-adjacent (two chosen gaps in different blocks never share a reflection; the gap at an empty run is not chosen).
(e) (N = 4p - 2) min(A, B) <= kappa (Corollary H0).

## 3. Lemma NF (merge normal form)

**Lemma NF.**  If some generalised RGR avoider of length N <= 4p - 1 has a genuine empty run, then one of the same length
exists that also has a genuine empty run and moreover (i) every rotation run is pure or a (1,1)-pair, and (ii) for every
even block S_j, every empty run is R_j or R_(j+1).
Proof.  Apply Lemma M0 while some run has a, b >= 1 and r >= 3, and Lemma PM across an even block S_j while some empty run
R_t has t notin {j, j+1}.  Each step preserves avoidance and the length (Corollary MP0) and strictly decreases R or k.  A PM
step across S_j with t notin {j, j+1} leaves R_t and its neighbouring blocks S_(t-1), S_t (none of them is S_j, which is
adjacent only to R_j, R_(j+1)) with their values, so R_t stays a genuine empty run (if R_j, R_(j+1) are both empty and
theta_j + theta_(j+1) = 0, the blocks S_(j-1), S_(j+1) fuse; values are unchanged).  M0 steps change no block value and no
empty run.  At termination (i) and (ii) hold.  []

## 4. Reformulation

INV*b-rig(p) (invstar/README.md) <=> no generalised RGR avoider of length 4p - 2 has a genuine empty run <=> (Lemma NF) none
in the normal form (i), (ii) satisfying 2(a)-(e).  This is decided for a given p by a finite exact search over run data
and theta (WAS0); see results.md.  INV*(p) itself additionally needs half (a) (rotation values) -- not addressed here.
