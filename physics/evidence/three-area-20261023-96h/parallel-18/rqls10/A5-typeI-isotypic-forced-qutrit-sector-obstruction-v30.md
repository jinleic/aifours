# RQLS10 v30 — two ACTUAL row/column orbit conditions FORCE a common3-sector in the isotypic ordinary TypeI family

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Mon Oct 26 08:38:31 PDT 2026**. AUTHOR-WRITTEN CANDIDATE. Exact finite subgroup-Fourier/Hermitian-PSD/multiplicity/orthogonality proof only; no scientific interpreter/eval/calculator/CAS/program/enumeration/solver/replay/CLI/nested agent/newGO/private approximate scout/backconversion. No machine/kernel/formal/configured-family/human/priority/novelty or accepted finite-witness claim.

## 1. Exact original-family theorem and genuinely forced sector

Assume the FULL ten-duad A5-covariant QLS10 setup of v29, without assuming covariance of a prospective designated-transversal resolution. Here the HONEST physical representation is

    V=C*e0 directsum (W tensor C3),
    U(g)=1 directsum (R(g) tensor I3),

where W is ONE real rotation3-representation of A5. Thus this covers the TypeI cases1+3+3+3 and1+3prime+3prime+3prime, NOT mixed3/3prime multiplicities. All hundred cells/rays and all row/column ONBs remain the ACTUAL original array, not a selected2-basis problem.

**Theorem.** Every such covariant QLS10 has a COMMON3-dimensional sector K containing ALL thirty disjoint-duad cells, with the other seventy cells in K-perp. Therefore it CANNOT be a maximal1-RQLS10: an actual3-sector would contain thirty distinct C3 rays with three original ONB context partitions, forbidden by the parent's ENTIRE adopted v16 rank3 argument.

The new mathematical point is that K is DERIVED from the two row/column conditions and positivity, not postulated as a symmetry ansatz or confused with the group-fixed line. The TypeI fixed line in v29 has nonbinary expectations and was correctly not called a common sector. Here a DIFFERENT multiplicity-null3-space becomes a true common sector.

This removes two whole ordinary physical-representation possibilities from the still-open A5-duad family. Mixed TypeI, TypeII–IV and all arbitrary noncovariant original intrinsic branches remain OPEN. No A5-WLOG,100-ray witness or unrestricted no-go.

## 2. The exact regular-orbit vector and subgroup conditions

From ENTIREv29: the forty diagonal/disjoint cells are orthogonal to e0, and the sixty intersecting-duad cells form ONE regular A5 orbit with squared e0-component1/6. Choose the canonical orbit phases so a reference intersecting cell(row a,column c) has vector

    q=e0/sqrt(6)+w,
    w=sum_(i=1)^3 sum_(r=1)^3 M_(i r) e_i tensor f_r,
    rho=M M^dagger,    trrho=5/6.                 (RHO)

The physical W basis e_i is REAL orthonormal, the multiplicity basis f_r is arbitrary complex orthonormal. This convention matters later: actual multiplicity amplitude vectors are the rows of M, regarded as columns, and their span is range(M^T), not casually range(M^dagger).

The row stabilizer H_a is S3. In W it decomposes as sign on its real unit axis n and standard2 on n-perp. The orbit of q under H_a consists of exactly the six ACTUAL intersecting cells in row a, which are orthonormal. Therefore for h in H_a,

    1/6+tr(rho R(h))=delta_(h,1).

The regular S3 character formula is

    delta_(h,1)=[1+sign(h)+2chi_std(h)]/6.

Orthogonality of irreducible matrix coefficients (or direct Fourier inversion on this six-element group) gives the COMPLETE conditions

    n^dagger rho n=1/6,
    P_(n-perp) rho P_(n-perp)=(1/3)P_(n-perp).     (ROW)

Indeed R(h) is block diagonal sign+standard; the standard matrix coefficients span the2x2 matrix algebra, fixing its compressed density to I2/3, while the sign coefficient fixes1/6. The cross blocks between axis and plane are unconstrained, and are NOT dropped as zero.

The COLUMN stabilizer H_c is another S3, with real unit axis m. The SAME reference vector q has a six-element orthonormal orbit there, so

    m^dagger rho m=1/6,
    P_(m-perp) rho P_(m-perp)=(1/3)P_(m-perp).     (COLUMN)

Thus BOTH actual orbit conditions act on ONE rho. No independent choice of row and column marginal or hidden free mixture is allowed.

## 3. The exact angle of these two axes

The S3 axis lines for the ten duads are the ten3-fold axes of the real icosahedral rotation representation. Their directions can be taken from the twenty dodecahedral vertices

    (+-1,+-1,+-1),
    (0,+-1/phi,+-phi) and its cyclic coordinate permutations,
    phi=(1+sqrt5)/2,

all of normsqrt3, with antipodal directions identified. For a fixed axis(1,1,1), the nine others have squared cosines5/9 for THREE axes and1/9 for SIX: the three other cube axes give1/9; each zero-coordinate family contributes one phi+1/phi=sqrt5 direction and one phi-1/phi=1 direction after antipodal identification.

The stabilizer S3 has exactly the same3+6 duad orbits: disjoint duads(3) and intersecting duads(6). Squared angle is invariant on those orbits, and the value multiplicities3 and6 distinguish them. The reference cell is INTERSECTING, hence

    |n dot m|=1/3.

Choose the sign of m so n dot m=1/3. This is only an axis orientation, not an altered physical ray. The3prime representation is obtained by the odd-permutation outer relabeling, which preserves whether duads intersect, so the same exact angle applies to the all3prime case.

No numerical principal-angle scout, decimal comparison or discarded approximate probe was used. This dodecahedral coordinate/angle argument is printed as part of the proof, not delegated to an unprovided catalogue.

## 4. Positivity forces a UNIQUE rank2 physical reduced matrix

Set A=rho-I3/3. ROW/COLUMN say its compressions to both n-perp and m-perp are ZERO and its trace is-1/6. A vector l perpendicular to BOTH real n,m satisfies Al in span(n) from the first compression and in span(m) from the second, so Al=0. Thus A is supported on span_C(n,m).

In that2-space the two compression conditions leave exactly the Hermitian matrices

    A=z*n m^T+conj(z)*m n^T,       z in C.

One may verify this directly in the basis n and(m-(n dot m)n); each vanishing compression imposes one real linear condition on a Hermitian2x2 matrix. The displayed complex parameter supplies all remaining two real dimensions. Since t=n dot m=1/3,

    trA=2t Re(z)=-1/6,
    Re(z)=-1/4.

The determinant of rho on span(n,m) is

    1/9+(trA)/3+detA
       =1/18-(1-t^2)|z|^2
       =1/18-(8/9)|z|^2.

But |z|^2>=1/16, so this determinant is<=0. Positive semidefiniteness of rho requires it>=0. Therefore Im(z)=0 and the determinant is EXACTLYZERO. We obtain

    rho=I3/3-(n m^T+m n^T)/4.                    (UNIQUE)

Its eigenvalues are0 on n+m,1/2 on n-m, and1/3 on l. Hence

    rankM=rankrho=2,
    M^dagger(n+m)=0,
    M^T m=-M^T n !=0.                            (KERNEL)

The last equality uses that n,m are real; it is the complex conjugate of the preceding kernel relation. The nonzero norm is fixed by n^dagger rho n=1/6. This is where positivity settles the whole continuous phase freedom—no generic-rank assumption, floating determinant or solver claim.

## 5. The same unused multiplicity line occurs in EVERY row and column

Let U be the2-dimensional multiplicity span of the rows of M, equivalently range(M^T), and let mu0=U-perp be its1-dimensional orthogonal complement. Define the invariant3-space

    K=W tensor mu0.

All sixty intersecting-cell vectors lie in Ce0 directsum(W tensor U) and are orthogonal to K, since the group acts ONLY on W and leaves the multiplicity factor untouched.

Write v=M^T n in U. By KERNEL, the column's sign-amplitude vector is M^T m=-v. Choose the unit multiplicity vector z0 in U perpendicular to v. The row's six-cell orbit span is EXACTLY

    Ce0 directsum (C*n tensor C*v)
         directsum (n-perp tensor U),

of dimension1+1+4=6. Here ROW gives full rank on the standard2 component, so its orbit spans all n-perp tensor U, not an asserted smaller space. Therefore the other four rays of that actual row span its orthogonal complement

    E_a=K directsum (C*n tensor C*z0).             (ROWCOMP)

The same calculation for the reference COLUMN gives

    E_c=K directsum (C*m tensor C*z0),             (COLCOMP)

with the SAME z0 because its sign vector is-v, not an unrelated multiplicity direction.

Covariance now transports these identities to ALL ten rows and ALL ten columns. It changes only the W-axis n or m, NOT mu0,v or z0 in the multiplicity space. Thus for every duad d,

    E_row(d)=K directsum (C*n_d tensor C*z0),
    E_col(d)=K directsum (C*n_d tensor C*z0),

where n_d is the corresponding distinct axis line. Their phase/sign choices do not alter these subspaces. This equality of the ROW and COLUMN multiplicity complement is the crucial global fact; without KERNEL it would be unjustified.

## 6. All thirty disjoint cells lie in K, all other seventy in K-perp

For a DISJOINT pair(a,b), its ray is one of the four nonintersecting cells in row a and in column b. Hence it belongs to E_row(a) intersect E_col(b). The two real axis lines n_a,n_b are distinct, so ROWCOMP/COLCOMP give

    E_row(a) intersect E_col(b)=K.

Thus ALL thirty disjoint-duad rays lie in K. In each actual row there are THREE such rays, orthonormal by the original ONB condition; they form an ONB of K. The row's diagonal ray must be orthogonal to them, so lies in K-perp (in fact in n_a tensor z0). All sixty intersecting rays were already proved in K-perp. Therefore EVERY one of the hundred rays lies wholly in K or K-perp. The projector onto K genuinely commutes with all the cell projectors.

This is the true common3-sector, not the group-fixed line Ce0. It contains exactlythirty actual cells, the disjoint pairs, with three rays per full original row/column/transversal ONB by the common-sector trace identity.

If the original array were maximal1-RQLS10, those thirty rays would be distinct. The complete parent-supported v16 theorem says a3-sector in ordern needs3n>=31: around a C3 ray its six orthogonal context neighbors, their24 outside neighbors and the ray itself are distinct, requiring31 rays. At n10, thirty cannot suffice. Hence no maximal1-RQLS10 exists in these isotypic TypeI representations.

The third resolution was arbitrary throughout. It was used only at this FINAL genuine-common-sector rank3 gate, not assumed covariant or cyclic. Without a resolution or without maximal distinctness, no corresponding unrestricted QLS no-go is asserted.

## 7. Full dependency/application boundary and remaining exact task

The entire chain needs all of the following, not one positive determinant check: v29's original full-array trace/typeI projection and orbit facts; the COMPLETE paired S3 reduced-matrix conditions; exact intersecting-axis1/3 angle; ALL complex Hermitian cross freedom retained until PSD forces rank2; correct multiplicity transpose convention; SAME row/column unused line; ALL disjoint cells in the actual common3-sector; finally ENTIRE parent v16 distinct-ray rank3 contradiction.

This is a NEW forced-sector theorem, not an application of rank3 geometry to rank4/5 or a false inference from reducible group representations. The mixed TypeI representations1+3+3+3prime and1+3+3prime+3prime do NOT share this single W tensor C3 factorization, and were NOT covered. Ordinary TypeII–IV also remain OPEN inside the A5 family, while the spinorial full-array case is independently excluded by v29. No scope is silently enlarged.

Named classical inputs are finite-group matrix-coefficient orthogonality, the real icosahedral3-representation/dodecahedral axes, and elementary Hermitian positivity. Their operative calculations are printed; no unseen Pauli/600-cell/classifier output is a premise. Optional ALLprojectiveA5 wording elsewhere still carries NR J-A5-SCHUR and is irrelevant to this HONEST ordinary family.

All statements are AUTHOR-WRITTEN candidates pending ENTIRE mathematical/dependency/application gates; no scientific interpreter or private approximate scout was used and nothing was machine-checked. No100-ray witness/unrestrictedno-go/formal/kernel/family/human/novelty/current-openness claim. All permanent process/math findings, v9/v14 withdrawals, frozen histories and ZERO-credit quarantines remain. Original18/exclusive-root/HOLD/cadence/science-cutoff2026-10-27T11:05:38-07:00/deadline12:35:38; no early pending-review park. The next actual remaining geometry is the MIXED TypeI or TypeII–IV ordinary irreducible10 case, not a retry of this forced-qutrit isotypic family.
