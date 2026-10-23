# Frozen representation for the no-window RGR residual: window-avoidance system (WAS)

Lane MathOlson.  FROZEN before any WAS computation (host clock read
2026-10-17T00:13:00-07:00 just before writing).  Builds only on proof-GR.md
(Lemma GR, hostile-reviewed).  Later edits go to an appended, dated section.

## 1. Representation (exact)

RGR word (proof-GR.md Sec. 1): x = 1, cyclic runs R_1 S_1 ... R_k S_k, R_i with a_i
letters rho_1 and b_i letters rho_{-1} (order inside R_i irrelevant), S_i =
sigma_{y_i}^{l_i}.  Put theta_i := y_{i-1} - y_i (y_0 := y_k), so sum_i theta_i = 0,
and every theta in Z_p^k with zero sum arises (y_i = y_0 - theta_1 - ... - theta_i).
For P subset of [k] let z_P be the pattern z_i = +1 iff i in P, and
W(P) := Ach(z_P) mod p  (Ach as in proof-GR.md Sec. 2; a set of even integers).

**Lemma WAS.**  The RGR word with run data (a, b, l) and reflection values y has NO
identity 2p-subword iff
    for every P subset of [k]:  sum_{i in P} theta_i  is not in  W(P)   (in Z_p).
Proof.  Lemma GR: a solution exists iff some z has t in Ach(z) with
t = tau(z) (mod p), tau(z) = -2^{-1} sum_i z_i (y_i - y_{i-1}) = 2^{-1} sum_i z_i theta_i.
With P = {z_i = +1}: sum_i z_i theta_i = sum_P theta - sum_{P^c} theta
= 2 sum_P theta (as sum theta = 0), so tau(z_P) = sum_{i in P} theta_i.  []

Consequences used for certificates:
* P = empty: tau = 0, value-independent.  Cyclic interval P = {i, ..., j}:
  tau = y_{i-1} - y_j (telescoping; one bracket sigma_{y_{i-1}} ... sigma_{y_j}).
  A union of m disjoint cyclic intervals has 2m pattern boundaries.
* Complement symmetry: W(P^c) = -W(P) and sum_{P^c} theta = -sum_P theta, so
  the constraints for P and P^c coincide (2^{k-1} distinct constraints).
* The run data (k; a_i, b_i, l_i) fixes every W(P); the reflection values enter
  ONLY through theta.  So "the RGR words with run data D are all solvable" is the
  statement "the WAS of D has no solution theta" -- a finite covering problem in
  Z_p^{k-1} per run datum, and a sumset problem in general.

