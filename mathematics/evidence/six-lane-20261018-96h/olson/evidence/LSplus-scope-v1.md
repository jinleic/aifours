# LS+: frozen scope (before proof text or probe), v1

Owner ContinueOlson.  Written after /bin/date 2026-10-19T03:38:33-0700, on parent instruction (IRC: 'Resume LS+ beyond SLZ3 now under frozen 96h
contract: exact length/quantifier scope first; no theorem/novelty promotion while pending').  Status: scope only.  LS and
LS+ are conjectures (LS the parent's, LS+ the lane's); neither is assumed anywhere.

## Statement under test
p >= 5 prime; kappa0 := floor(2p/3); kappa an integer with kappa0 + 1 <= kappa <= p - 2 (kappa = p - 1 is the classical
s_(2p)(C_p) = 3p - 1 and is not part of the scope).  Sequences = finite multisets of odd residues mod 2p (odd elements of
C_(2p)); zero-sum, (ZP_kappa), (S1_kappa), LONG as in evidence/proof-SLZ3-v1.md (0cfe637f919bdaab937f8292fa527d7fbd54e3af7d55bb07ddf137c0ad263c1c).
LS+(p, kappa): for EVERY sequence Y with (ZP_kappa) that fails (S1_kappa), |Y| <= 3kappa + 1.
Quantifiers: for all p, all kappa in the range, all Y (no condition on the generator, the multiplicities or sigma(Y)).
Minimal-counterexample length: a counterexample can be cut to length exactly 3kappa + 2 (keep a shortest long zero-sum T,
|T| <= 3kappa + 1 by SLZ3, and delete terms outside T); so it suffices to exclude |Y| = 3kappa + 2.
Induction frame: LS+(p, kappa0) holds vacuously by S1-sharp; the step is LS+(p, kappa') for all kappa0 < kappa' < kappa
=> LS+(p, kappa).  LS+ implies LS (p + 2kappa + 1 > 3kappa + 1) and S1-sharp.

## Claims distinguished (none promoted while pending)
- Exact extremal structure for sequences supported on two values {h, 3h} (written proof planned).
- Inductive structure of a minimal counterexample (written proofs planned): a zero-sum of length exactly 2kappa exists in
  every subsequence of length >= 3kappa - 1 containing a long zero-sum; short zero-sums (length <= 2(p - kappa)) meet every
  long zero-sum; consequences for the complement of a long zero-sum.
- The general step LS+(kappa') (kappa' < kappa) => LS+(kappa): open; any partial result will state its extra hypotheses.

## Finite aids
Existing: probe v11/v12 (complete DFS p = 7, kappa = 5; p = 11, kappa = 8, 9): maximal (ZP)-and-not-(S1) length = 3kappa + 1.
Any new probe: falsification aid only, launch plan to the parent first, gated launcher with pre-compute PID record,
<= 300 s self-budget, stdout only; never offered as a larger finite range.
