# The full level-six invariant map: injective for every r,s>=6

MathKacMoody-2, original math-3. Actual `/bin/date` returned before this new write: **Wed Oct 28 22:14:18 PDT 2026**. **UNREVIEWED exact-computation-assisted candidate**, not a parent adoption, formal/kernel, independent-model/human, priority or novelty verdict.

## 1. Exact theorem at its source cut

For every integer r,s>=6, every allowed FULL complex Cartan realization C of A(r,s), the original Serre quotient S=G_C/J and the finite Levi l=sl3, at the full-Cartan/free-Levi/lowering interfaces in `frontier-20261028-Levi-free-quotient-critical-reduction-v1.md` Sections 0–4:

> The ORIGINAL lowering D3 is injective on the **entire 20-dimensional level-six Levi-invariant space**, which is P_(6,6,6)=ker f1 intersect ker f2 in that actual degree, with target S_(6,6,5).

The source/target cut is substantive: r,s>=6 implies neither repeated-node3 seed occurs through level six; hence this is the free-Levi source and target at those levels. The actual source is not inferred from the rank of an arbitrary 20-column submatrix.

This does not settle other level-six primitive maps, the small-row regime, F6/B6, the arbitrary-GCM/all-level book conjecture, H13 authenticity or novelty. The word “entire” concerns this invariant source, not the whole level-six band.

## 2. The full source, without a 2520-column RREF

The exact free-Lie Witt character is `(V^6-psi2(V^3)-psi3(V^2)+psi6(V))/6`, for the adjoint generator weights `(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)`. The finite-sl3 Weyl-denominator extraction gives weight dimension 2520 and **lowest multiplicity 20** at (6,6,6). This is the trivial Levi type.

The independently authored source replay verifies all 2520 standard Lyndon brackets are monic at their displayed leading word; verifies 20 stored coefficient vectors are independent; rebuilds their Lie vectors; and checks all 40 f1/f2 actions vanish. The independent character calculation says the whole horizontal space has dimension 20, so these 20 vectors span it. This closes the source-span obligation at the named Witt/finite-Levi interfaces, rather than relying on a producer's kernel-count header.

The earlier slow full 2520-column horizontal-RREF replay was **cancelled, NOT passed**. Its replacement is the explicit character-plus-20-vectors argument just stated, together with the completed matrix/resultant replay below. No success is backdated to the cancelled run.

## 3. Two actual maximal minors and an exact integer-fibre exclusion

Put x=r-6,y=s-6. For the full 1780×20 affine D3 matrix on those 20 vectors, use its baseline selected rows and a second set replacing row-slot 0 (`00777`) with target word `04657`. Exactly:

    P1 = (531441/1048576)(x+y+11) A19(x,y),
    P2 = (531441/262144)(x+y+11) B19(x,y).

A19 and B19 are integer polynomials of total degree 19, each with 210 terms and nonzero CONSTANT x-leading coefficient. The common linear factor is strictly positive on x,y>=0.

Let H(y)=Res_x(A19,B19). Its degree is 360 (a priori bound 19*19=361). Its only repeated factors are, at the multiplicities in H,

    (y+4)^2 (y+6)^2 (8y+43)^9 (5y+28)^12 (y+5)^29.

The remaining squarefree integer-root calculation gives exactly **y=-6,-5,-4** as all integer roots of H. The producer uses Cauchy's bound and Hensel uniqueness at p=1009; the separate matrix replay strips the displayed factors, proves the remaining factor squarefree mod p=5003, exhausts its residue roots, lifts each uniquely beyond twice the Cauchy bound, and finds no additional integer root. Non-integral negative rational roots of the displayed factors do not add any integer fibre.

Since the x-leading coefficients are constant, H(y0) is the exact specialized resultant for every y0. Thus for every integer y0>=0 there is no common complex root of A19(·,y0), B19(·,y0). In particular at every integer point x,y>=0, at least one maximal minor is nonzero. The full 20-column map is injective, proving the theorem at the stated source cut.

## 4. Evidence

- Producer: `frontier-20261028-level6-two-minor-general.py`, SHA `c22754a615becd06aed9aec9ab286a68069db1c977ecec265de4c487878821c6`, run `--a 6 --b 6 --slot 0 --word 04657`. Output `frontier-20261028-level6-666-two-minor-certificate-v1.json`, SHA `a59569fdecaff1c7c81a7c6d28b48ee8548d5ccbdc1107a145ede26d452a19ef`, returned all-integer-quadrant full rank in the call ending **Wed Oct 28 21:38:36 PDT 2026**.
- Matrix/resultant reconstruction: `frontier-20261028-level6-666-matrix-replay.py`, SHA `dd9b3639ed25d3d31164ac85b5fd48cd31fead79ea0d9932a26babe0ecb29df7`, independently rebuilds the 20 source-combination images using tree-Jacobi, verifies BOTH minors by 462 exact shifted-triangle determinant evaluations, and verifies H by **362 exact integer Sylvester determinants**. This is a whole unisolvent set for the resultant degree bound, not a few modular spot checks. It then supplies the p=5003 integer-root proof. Output SHA `95a610d047f1fc68304e2695d3ff21bcc7438670c17a09f3789002b0f2fd04d2`, PASS in the call ending **Wed Oct 28 22:11:05 PDT 2026**.
- Full source by character and combinations: `frontier-20261028-level6-666-source-by-character.py`, SHA `bfa578b45aa9a55dd04ee0720b7eead253c2a69e86f92735439a191da0e41c88`; output `frontier-20261028-level6-666-source-by-character-v1.json`, SHA `5e48a0676d724dc38b05575436a909915e9179e381a17d1dbf98aed519e04663`, PASS in the call ending **Wed Oct 28 22:13:37 PDT 2026**. It pins the same pencil SHA as the producer and matrix replay.

The two successful replays are complementary: one proves full primitive-source coverage at the named character interfaces; the other checks every finite determinant/resultant identity needed here. Both are same-owner implementations, not independent-model or formal verification. Full scientific review and parent disposition remain pending.

All prior immutable findings and quarantines remain historical, and no held output is a premise. Other pending native resultants and broad-band audits are not consumed by this theorem.

**END — entire level-six invariant source, all r,s>=6; independent scientific review pending.**
