# Supplied written lead — remove orthogonality from the three-ME scalar obstruction

Actual observed clock before freeze: **2026-10-25T07:24:34-0700 PDT**. NEW parent-supplied proof lead, developed before this freeze and explicitly exposed; not preregistered or accepted. No scientific interpreter or program is used. Read parent evidence erratum v9 first. This strengthens the SAME scalar-completion route, not unrestricted P44.

## Proposed theorem

Let Phi_j=vec(U_j)/2 for arbitrary4-by4 unitaries U_j, NOT necessarily Hilbert–Schmidt orthogonal or linearly independent. Let Q=sum_(j=1)^m p_j P(Phi_j), m<=3,p_j>=0. If W=lambda I16-Q is nonnegative on EVERY complex Schmidt-rank<=2 vector, then W^Gamma>=0; for nonzero Q the proposed argument even gives a strictly positive scalar lower margin. Scalar completion and maximal entanglement remain essential. No more-than-three-ray theorem is asserted.

## Written argument to reconstruct or refute

The existing simultaneous Gram derivation uses neither orthogonality nor independence: for every rank-two plane P,

H_ij=sqrt(p_i p_j) Tr(U_i^* P U_j)/4,

and two-block positivity implies lambda>=lambda_max H(P). Its diagonal is p_i/2. The separate swap argument also needs no orthogonality: Q^Gamma<=(sum p_i)I16/4.

Order p1>=p2>=p3>=0. Handle p2=0 by the original single-ME truncation (lambda>=p1/2); all-zero is trivial. For p2>0, use physical local unitaries to set U1=I and diagonalize V=U1^*U2. V is unitary; its four eigenphases have FOUR cyclic gaps summing2pi. At least one gap is<=pi/2, even with repeated phases. Choose the rank-two projector P onto the two corresponding orthonormal eigenvectors. Thus

|Tr(P V)|=|eta_i+eta_j|>=sqrt2.

This replaces the old trace-zero/six-pair-average argument. No trace-zero hypothesis is needed. The top-left2-by2 principal Gram block therefore has largest eigenvalue at least

[p1+p2+sqrt((p1-p2)^2+2p1p2)]/4
 = [p1+p2+sqrt(p1^2+p2^2)]/4.

The full Gram maximum is at least that principal-block maximum. Since p2>0,p1>=p2 and p3<=p2,

sqrt(p1^2+p2^2)>p2>=p3.

Consequently

W^Gamma >= [sqrt(p1^2+p2^2)-p3]I16/4 >0.

The proof uses an ACTUAL complex rank-two eigenplane, not simultaneous diagonalization of all rays. The third term may be arbitrary ME and nonorthogonal; its nonnegative contribution is simply retained by the principal-submatrix bound. This also sharpens the uniform lower margin for the orthogonal three-ray subclass; it is not a claim that the bound is the exact positivity threshold.

## Owner deliverable

Inspect every normalization, conjugation, local-unitary reduction, eigenphase-gap and zero-weight boundary. If valid, consolidate the arbitrary-nonorthogonal theorem and identify the genuine next escape (at least four rays, non-ME rays or non-scalar completion). Do not continue treating nonorthogonality ALONE as an escape from the three-ray scalar obstruction. If invalid, give the first explicit failed implication. Preserve the older narrower source and its review unchanged; this lead is not their retrospective scope. No scientific execution, solver, sampling, new GO, nested agent or external CLI.
