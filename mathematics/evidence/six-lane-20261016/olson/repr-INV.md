# Frozen representation for INV(p): inverse problem at length 4p-2 in bracket/mark coordinates

Lane MathOlson.  FROZEN before any INV work; host clock read just before writing
is recorded in Sec. 4.  Builds on proof-GR.md (Lemma GR, any length N) and
repr-WAS.md Sec. 1 + Sec. 5 (Lemma WAS, reviewed).  Later edits only in appended,
dated sections.  Disjoint new files for this work: repr-INV.md, proof-INV-*.md,
code/inv_*.py|cpp, evidence/inv/.

## 1. Target (exact)

INV(p), p odd prime: if w is an RGR word of length N = 4p-2 over D_{2p} with
F, R >= 1 (k rotation runs, k reflection runs, x normalised to 1) and w has no
identity 2p-subword, then (i) every reflection run has odd length, (ii) every
rotation run has odd length, (iii) k <= p.
Not hypotheses: unique theta, equal brackets, constant rotation runs (observed at
p = 5, 7 only; may be used as heuristics, never as assumptions).

## 2. Representation (exact; derived from Lemma GR / WAS)

Bracket of rotation run i: beta_i := theta_i - d_i, d_i := a_i - b_i, i.e. the
product sigma_{y_{i-1}} R_i sigma_{y_i} = rho_{beta_i}.
Selections with an even number of reflections <-> (P, C, marks): P = set of runs in
the "+" zone (one global sign), C = number of reflections (even, Phi(P) <= C <=
C_max(P)), and for every run i a number mu_i^+ <= a_i, mu_i^- <= b_i of MARKED
letters rho_1, rho_{-1} (marked = selected if i not in P, unselected if i in P).
Value (exactly as Lemma GR with u = t - D_P):
    V = sum_{i in P} beta_i + sum_i (mu_i^+ - mu_i^-)            (mod p)
Size:
    C + sum_{i in P} (r_i - mu_i^+ - mu_i^-) + sum_{i not in P} (mu_i^+ + mu_i^-) = 2p.
w avoids iff no (P, C, mu) satisfies V = 0 and the size equation.  The window of
Lemma GR is the projection of this set onto t = D_P - sum (mu^+ - mu^-).
Facts used: P -> sum_P beta_i is additive on disjoint unions; P and its
complement give the same selections; Phi(P) = number of cyclic boundaries of P;
delta(P) = #{j : l_j != f_j mod 2}, C_max = F - delta.

## 3. Attack protocol (bounded)

A1 (closed-form necessary conditions): derive, for P = empty and P = single runs /
single cyclic intervals, the exact inequalities an avoider must satisfy, in terms
of (a_i, b_i, l_i, beta_i).
A2 (certificate family, bounded computation as an aid only): for p = 5 (N = 18,
complete, < 1 s) and p = 7 (N = 26, one complete run <= 10 min), restrict the WAS
to a pattern family (Phi <= 2, then Phi <= 4, ...) and record whether every run
datum VIOLATING (i)-(iii) is already certified solvable by the family.  The
smallest certifying family guides A3; it is not a proof.
A3 (all-p proof): prove that the family from A2 certifies every violation of
(i)-(iii) for every p, by an extremal-window / Cauchy-Davenport argument on the
additive map P -> sum_P beta_i and the window inequalities.
A4 (refutation search, only if it can refute INV): at p = 11, N = 42, structured
families that A1-A3 identify as the hardest violations (e.g. one even run inside
an otherwise extremal shape, or k = p+1 short runs); any WAS solution must be
re-verified by the raw ordered-product DP (code/was_verify.py dp_has) on the
explicit word before any report.  Unfinished or timed-out searches prove nothing.
Controls for A2/A4: the unrestricted WAS at N = 4p-2 must reproduce the known
avoider sets (p = 5: 210 run data; p = 7: 3738); within A4 families, extremal
shapes (all runs odd, k <= p) must appear as avoiders (positive control).
Deliverable: a complete proof of INV(p), an exact counterexample, or a precisely
stated irreducible lemma with what remains.

## 4. Freeze record

Freeze finalised at host clock 2026-10-17T01:56:00-07:00.  Before finalising, one sign in the
Sec. 2 value formula was corrected (written as "- sum (mu^+ - mu^-)"; derivation:
t = D_P - sum_i (mu_i^+ - mu_i^-) and the GR condition t = tau(P) = sum_P theta_i
give sum_P beta_i + sum_i (mu_i^+ - mu_i^-) = 0).  No computation preceded this.
