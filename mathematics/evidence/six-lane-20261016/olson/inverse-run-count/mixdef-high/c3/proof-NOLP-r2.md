# Lemma CORE and Lemma NOLP (revision r2): lifted window constraints, the integer core, and why real LP certificates
# cannot kill W(p, 4) for p >= 17

REVISION r2 (c3/proof-NOLP-r2.md), written after host clock 2026-10-17T11:44 PDT.  It supersedes
c2/proof-NOLP.md (frozen, unchanged; sha256 b66a4ec1...) and answers the parent's Codex review
institute/runs/six-lane-2026-10-16/review/olson-w4-nobc-nolp-codex-review-v1.note.md (verdict NOLP
ACCEPT-WITH-FIXES, one MINOR finding at proof-NOLP.md:45).  The only change is the scope sentence after
Lemma NOLP (marked [r2 fix]).  Sibling references (proof-NOBC.md, lpcert.py, farkas*.py, cutgen.py, famdfs.*,
nolp_check.cpp, out/...) mean the files in ../c2/; the ../../../ prefixes resolve identically from c3/.

Status: [W] = written proof, reviewed ACCEPT-WITH-FIXES (fix applied here); [F] = exact computation (aid
only).  Original version written 2026-10-17 after host clock 10:32 PDT (hashes: c2/out/freeze.txt).  Notation as in proof-NOBC.md (Lemma H
lambda for all-odd words, beta = 0; Lemma BC and its Claim, ../../../inverse-parity/proof-PAR-K0.md).
Nothing here bears on the truth of RUNS(p); Sec. 3 records that W(p, 4) has no avoider for p <= 17.

## 1. Lifted constraints and Lemma CORE [W]

Let w be an all-odd RGR word with k runs, A, B <= 2p - 1 and min(A, B) <= kappa (so the empty pattern does not
kill).  For proper Q put lo(Q) := lambda(Q), hi(Q) := p - lambda(Q^c).  Call Q CERTIFIED if |Q| = 1, or
Q = Q' u {t} (t not in Q') with Q' certified and
   lambda(Q') + lambda({t}) + lambda(Q^c) >= 1  and  lambda(Q) + lambda(Q'^c) + lambda({t}^c) >= p + 1   (1.1)
(this is condition (b) of Lemma BC with X = Q', Y = {t}, Z = Q^c).
**Lemma L (lifting).**  If w avoids with half-sums u, and x_t is an integer = u_t (mod p) in [lo({t}), hi({t})]
for each run t (such x_t exist, as in the proof of Lemma BC), then X_Q := sum_{t in Q} x_t lies in
[lo(Q), hi(Q)] for every certified Q.
Proof.  Induction along the certification: X_Q = X_{Q'} + x_t lies in [lo(Q') + lo(t), hi(Q') + hi(t)],
which by (1.1) is inside [1 - lambda(Q^c), p + lambda(Q) - 1]; X_Q = u_Q (mod p), so the Claim of Lemma BC
gives lambda(Q) <= X_Q <= p - lambda(Q^c).  []
**Lemma CORE.**  Suppose every proper pattern of w is certified and lambda(Q0) + lambda(Q0^c) >= 1 for some
proper Q0.  Then w is an avoider (for some choice of the reflection values) iff there are integers x_t with
   sum_t x_t = p   and   sum_{t in Q} x_t >= lambda(Q) for every proper Q.                         (1.2)
Proof.  If w avoids, take x as in Lemma L; X_[k] = 0 (mod p) and X_[k] = X_{Q0} + X_{Q0^c} lies in
[lambda(Q0) + lambda(Q0^c), 2p - lambda(Q0) - lambda(Q0^c)], a subset of [1, 2p - 1], so X_[k] = p; and
X_Q >= lambda(Q) by Lemma L.  Conversely, given (1.2), put u_t := x_t mod p (sum u_t = 0, so some reflection
values y realise these jumps, theta_t = 2u_t).  For proper Q, X_Q >= lambda(Q) and X_Q = p - X_{Q^c} <=
p - lambda(Q^c); if lambda(Q) + lambda(Q^c) >= 1, the p consecutive integers [1 - lambda(Q^c), p - lambda(Q^c)]
are the disjoint union of I(Q) = [1 - lambda(Q^c), lambda(Q) - 1] and [lambda(Q), p - lambda(Q^c)], so
u_Q is not in I(Q) (mod p); if lambda(Q) + lambda(Q^c) <= 0, I(Q) is empty.  With the empty-pattern
condition, Lemma H gives avoidance.  []
So, for such words, NMH is the statement that the set function lambda has NO integer point in its "core"
{x : x([k]) = p, x(Q) >= lambda(Q) for all proper Q}.  Lemma BC certificates are integer partitions with
sum lambda >= p + 1; by the Bondareva-Shapley theorem the REAL core is empty iff some balanced collection
(fractional partition) has weighted lambda-sum > p.

## 2. Lemma NOLP [W]

**Lemma NOLP.**  Let w be in W(p, kB) (proof-NOBC.md Sec. 1: k = p + 1 + kB single-letter runs, one anti
run, B = 1, kappa = kB + 1) with kB >= 4 and p >= 4kB - 1 (for kB = 4: p >= 17).  Then the real vector
   x_t := 4/5 + c (t aligned),   x_t := -1/5 + c (t the anti run),   c := (p - Phi)/k,  Phi := (4(p + kB) - 1)/5,
satisfies lambda(Q) <= X_Q <= p - lambda(Q^c) for EVERY proper Q (certified or not) and X_[k] = p.
Consequently no nonnegative real combination of lifted window constraints (lower or upper, any family),
together with X_[k] in pZ, is contradictory.  Hence a certificate for W(p, kB) that uses ONLY this lifted
constraint system (the bounds lambda(Q) <= X_Q <= p - lambda(Q^c) on lifts X_Q = sum_{t in Q} x_t, together
with X_[k] in pZ) must use integrality of the lifts (as Lemma AV does at p = 11, proof-NOBC.md Sec. 4).
Real feasibility of this relaxation does not classify proof methods outside this constraint system.
[r2 fix: scope of the conclusion restricted to certificates using this lifted constraint system.]
Proof.  phi(Q) := (4 j - e)/5 for Q with j aligned runs and e anti runs; phi is additive and phi([k]) = Phi.
proof-NOBC.md (2.1) and the two bounds after it give lambda(Q) <= phi(Q) for every proper Q.  Since
p >= 4kB - 1, c >= 0 and 0 <= c |Q| <= p - Phi for |Q| <= k.  Lower: X_Q = phi(Q) + c|Q| >= phi(Q) >= lambda(Q).
Upper: X_Q = phi(Q) + c|Q| <= phi(Q) + p - Phi = p - phi(Q^c) <= p - lambda(Q^c).  Total: X_[k] = Phi + ck = p.
Any Farkas combination would be violated by this point.  []
Remark.  For p = 11, 13 (where p < 4kB - 1 = 15) the real LP is infeasible: Sec. 3.

## 3. Exact computations [F]

* lpcert.py: W(11, 4), W(13, 4): all proper patterns certified; real LP infeasible (out/lpcert_p11.txt,
  out/lpcert_p13.txt).  farkas.py, farkas_win.py, cutgen.py: exact Farkas certificates, independently re-checked
  in fractions (out/farkas_p11.txt, 11 constraints; radius-7 window at p = 13, 14 constraints, README Sec. 13;
  out/cutgen_p11.txt, out/cutgen_p13.txt).  Multipliers are irregular (no uniform shape found).
* Exact avoider search over all patterns (famdfs.py and its C++ port famdfs.cpp, identical check counts at
  p = 11, 13, 17 and identical shrink-control outputs, out/famdfs_cpp_validate.txt): NO avoider in W(11, 4)
  (37,639 checks), W(13, 4) (157,720), W(17, 4) (3,082,898; out/famdfs_p17.txt).  So at p = 17 integrality
  (not the real LP) is what kills the word.  p = 19, 23: see c2/README.md Sec. 14/15.
