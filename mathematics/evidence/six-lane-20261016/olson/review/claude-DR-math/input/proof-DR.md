# Theorem DR: the RGR problem at length 4p-1 reduces to an inverse statement at 4p-2

Lane MathOlson; written after host clock 2026-10-17T00:37:01-07:00.  Status: written
proof [W]; not yet hostile-reviewed.  Uses: Doubling Lemma (j = 0) and EGZ from
proof-dihedral-partial.md (reviewed).

## Definitions

p odd prime.  RGR_N(p): words of length N over D_{2p} whose rotation letters all lie
in {rho_x, rho_-x} for one x != 0 and whose maximal cyclic reflection runs are each
constant (proof-GR.md Sec. 1 with N in place of 4p-1).  If F, R >= 1 the cyclic
word is an alternation of k rotation runs and k reflection runs (2k runs).
An *avoider* is a word with no identity 2p-subword (increasing indices, ordered
product).  Deleting letters from an avoider leaves an avoider.

**INV(p).**  Every avoider in RGR_{4p-2}(p) with F, R >= 1 has all 2k maximal cyclic
runs of odd length and k <= p.

## Theorem DR

If INV(p) holds, every word in RGR_{4p-1}(p) has an identity 2p-subword.

Proof.  Let w in RGR_{4p-1}(p) be an avoider.
If R = 0, w is a single cyclic run sigma_y^{4p-1}, and sigma_y^{2p} = 1.  If F = 0,
R = 4p-1 >= 3p-1 rotations contain 2p with zero sum (EGZ).  So F, R >= 1 and w has
2k runs, 2k even, total length 4p-1 odd: some run has length >= 2.
Deleting one letter from a run of length >= 2 gives an avoider w' in
RGR_{4p-2}(p) with the same 2k runs (nothing merges; the shortened run is still
constant, resp. still has rotation values in {rho_x, rho_-x}), F, R >= 1.
(i) If X != Y are runs with |X|, |Y| >= 2: INV(p) for the deletion from X gives
|X| - 1 odd and |Y| odd; for the deletion from Y it gives |Y| - 1 odd.
Contradiction.  So exactly one run X has |X| >= 2 and the other 2k-1 runs are
single letters; |X| = 4p-1-(2k-1) = 4p-2k, and INV(p) gives k <= p, so |X| >= 2p.
(ii) If X is a reflection run, X = sigma_y^{|X|} contains sigma_y^{2p} = 1.
(iii) If X is a rotation run, it has >= 2p letters in {rho_x, rho_-x}, so >= p
equal ones, whose sum is +-px = 0: a gap of w containing p rotations with zero sum.
w has length 4p-1 and F >= 1, so the Doubling Lemma (j = 0) gives an identity
2p-subword.  Both contradict w being an avoider.  []

## Corollary DR' (full dihedral reduction)

Let INV*(p): every avoider of length 4p-2 over D_{2p} lies in RGR_{4p-2}(p).
INV*(p) and INV(p) together imply ordered Olson for D_{2p} (no avoider of length
4p-1).
Proof.  Let w be an avoider of length 4p-1.  Every one-letter deletion is an
avoider of length 4p-2, hence in RGR_{4p-2}(p).  (a) Rotation values: if w had a
rotation rho_0, or two rotations with values u, v, v not in {u, -u}, delete a letter
different from these (4p-1 >= 3 letters): the deletion still contains them and is
not RGR.  So all rotation values of w lie in one {x, -x}, x != 0.  (b) Reflection
runs: if a maximal cyclic reflection run of w is not constant, it contains two
cyclically ADJACENT different reflections sigma_u sigma_v (positions i, i+1).
Delete any letter at a position j not in {i, i+1}: in the deletion these two
letters are still adjacent reflections, hence in one maximal reflection run (a
deletion can merge runs, which only enlarges the run containing them), so that
run is not constant and the deletion is not RGR.  Hence w is in RGR_{4p-1}(p) and
Theorem DR applies.  []

## Finite-exact status of the hypotheses (repr-WAS.md Sec. 4)

INV(5) and INV(7) hold: the complete WAS enumerations at N = 18 and N = 26 (filters
off; all rotation-canonical run data; all theta) list every avoider run datum of
RGR_{4p-2}(p), and each has all runs odd and k <= p (with constant rotation runs and
equal brackets in addition).  Theorem DR then re-derives the p = 7 result of the
direct N = 27 search by a second route.  INV*(5) holds (all 3730 exhaustive D10
length-18 avoiders are RGR).  INV*(7) is untested.  No all-p proof of INV or INV*.
