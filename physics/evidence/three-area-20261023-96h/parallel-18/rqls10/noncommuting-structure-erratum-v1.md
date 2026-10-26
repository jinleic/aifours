# Noncommuting structure — basis-normalization clarification v1

Governs unchanged `noncommuting-structure-v1.md`, §3 and its use in §4. No scientific execution or new acceptance. The normalized orthogonal-basis statement there is valid, but mixing it with the unnormalized rational pair basis needs an explicit metric.

Use throughout the K=Q(i sqrt7) basis `e0, e_r+e_-r` on E and `e_r-e_-r` on O. Its Gram matrices are

    G_E=diag(1,2,2,2,2),       G_O=2I4.

Write M's coordinate blocks as `[A B; C0 D]`. The actual consequence of `P_rho M` symmetric in this unnormalized basis is

    G_E A=A^T G_E,
    C0=-(1/2) B^T G_E,
    D=D^T.

Accordingly the entirely K-valued Schur system, replacing the unnormalized reading of (S4), is

    x=-A^-1 B y,
    [D+(1/2)B^T G_E A^-1 B] y=0.

The bracketed4×4 matrix is symmetric because `G_E A^-1` is symmetric. This agrees with the note's displayed normalized-basis formula after scaling the pair bases by1/sqrt2; no extension of the actual Schur coefficients beyond K is necessary. The unnormalized reconstruction `delta_r=x_j+y_j`, `delta_-r=x_j-y_j` and its exact unit-modulus equations stay unchanged. The rank-five floor, commuting-case obstruction and one-dimensional norm criteria are unaffected.
