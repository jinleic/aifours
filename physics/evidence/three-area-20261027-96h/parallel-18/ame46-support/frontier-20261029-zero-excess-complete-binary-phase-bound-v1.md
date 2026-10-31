# Complete finite phase group for zero-excess support realization

**WRITTEN candidate; not an exclusion, witness, formal proof, novelty clearance or adopted result.** This is an additive mathematical refinement of `frontier-20261029-zero-excess-support-phase-normal-form-v1.md`, whose exact support/P-code hypotheses and necessity/sufficiency proof remain in force. No other candidate or outside theorem is imported.

## Statement

For a zero-excess support specification with m=|E|>0, arbitrary-complex phase realizability is equivalent to realizability with every E phase a **2^m-th root of unity**. Thus for N=48,t=24,m=24 a24-bit phase variable per E position suffices for a *complete* phase feasibility formulation, not merely the sufficient fourth-root restriction.

This does not prove that fourth roots suffice. Nor does it eliminate the independent six-pair complement-P-code obligation.

## Proof

Use phase units pi: Mx=1 modulo2, with M having m columns. Each row of M has four distinct nonzero entries +1,-1,-1,+1. In particular every row has Euclidean norm2, and M*1=0. Write r=rank_Q(M), so r<=m-1.

Suppose an arbitrary complex solution exists and choose real lifts x. Then Mx is an integer vector all of whose entries are odd. Select r independent rows, and then r columns giving a nonsingular r-by-r integer minor D. Let d=|det(D)|>0. The selected rows of Mx form an integer right side b. Set all unselected coordinates of a new x' to zero and solve D*x'_selected=b.

The chosen r rows span the entire row space of M over Q. Therefore Mx'=Mx **as real vectors**, not merely on the selected rows: every other row is a rational linear combination of those selected rows, and those row evaluations have been preserved. In particular every entry of Mx' is still an odd integer. Cramer's rule gives d*x' integral.

Factor d=2^s*h with h odd. Put x''=h*x'. Then 2^s*x'' is integral, while Mx''=h*(Mx') is again coordinatewise odd. Thus x'' still solves Mx''=1 modulo2, and each exp(pi*i*x''_w) has order dividing2^(s+1).

Hadamard's determinant inequality, applied to the selected rows restricted to the selected columns, gives d<=2^r. Hence s<=r and s+1<=r+1<=m. Every resulting phase is consequently a2^m-th root of unity. The reverse implication is immediate because these roots are complex unit phases. If M has no rows/r=0, the all-zero phase vector suffices whenever the empty system is solvable; this harmless degenerate case also satisfies the statement.

The proof uses the selected right side from an existing real solution only to establish existence of an exact finite-group solution. It does **not** assume that arbitrarily forcing the selected original rows to right side1 preserves the other congruences; that generally unjustified shortcut is not used.

## Exact finite formulation and checking scope

Set L=2^m and give every potential E position an m-bit exponent v_w, forced to zero if the position is absent. Retain the support/P-code conditions from the normal-form theorem. On every actual2x2 block impose

`v_a-v_b-v_e+v_f = L/2 (mod L)`.

A SAT assignment gives a literal exact tensor through the normal-form formula. A complete UNSAT proof would exclude that particular fully specified support family over **all complex phases**, provided the support/P encoder is itself proved complete. A solver timeout proves nothing. No such complete UNSAT claim is made here.

Large L need not force large numeric field arrays in a positive checker. For2-power L, reduce a sparse Gram sum using zeta_L^(k+L/2)=-zeta_L^k. A Gram entry with at most36 terms remains sparse regardless of L. Zero reduced coefficients are exact identities; no floating trigonometry or exponentially long polynomial vector is required.

The current fourth-root search/control source remains honestly restricted; this theorem does not retroactively change the scope of any of its SAT/UNSAT/timeout results.
