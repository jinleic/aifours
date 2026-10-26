# Full MOQLS(8): exact Gram representation, global defect budget, and a B3 span dichotomy — candidate v1

Status: CANDIDATE WRITTEN PARTIAL. This is not a five-MOQLS(8) classicality proof, a new checked GB case, or a physical witness. The primary target remains the unrestricted problem in selection-v1.md. No scientific program, numerical check, enumeration, solver, certificate replay, compilation, nested agent or model CLI was used. All statements below are written derivations. Parent and separate reconstruction have not yet occurred.

## 1. Exact definitions and scope

Let n>=2, N=n^2 and Omega={0,...,n-1}^2. Write x=(i,j). A QLS is an array of unit vectors q_x in C^n, with each row and each column an orthonormal basis. A family of t QLS is mutually orthogonal when, for s!=u, the N vectors q_{s,x} tensor q_{u,x}, x in Omega, form an orthonormal basis of C^n tensor C^n. These are Ball–Simoens §§2.2–2.3 and Musto–Vicary Definition4, not entangled quantum-officer cells.

Classicality allows independent entry phases and a separate output unitary for each square, with common row/column permutations. Since phases and output unitaries do not alter the number or overlap pattern of rays, the family is classical iff each square is classical. Common row/column permutations do not change which rays occur, so no conflict between separately classical squares arises.

The arguments in §§2–6 apply to EVERY family just defined. They do not assume U, T16, a support class, phases in a finite field, real vectors, maximal cardinality, or a preselected classical square. Only §7 conditions on the old B3 axis data, as an application rather than a replacement primary target.

## 2. A quadratic Hermitian system equivalent to the FULL problem

For each s let G_s be an N by N complex matrix. Define system E(n,t):

(E1) G_s is Hermitian.

(E2) G_s[x,x]=1 for every x; G_s[x,y]=0 for distinct cells in a common row or a common column.

(E3) G_s^2=n G_s.

(E4) G_s[x,y] G_u[x,y]=0 for every s!=u and x!=y.

Equivalently, (E4) says G_s Hadamard G_u=I_N. Hadamard product here has NO conjugation: it is the Gram product for q_{s,x} tensor q_{u,x}. All variables not fixed by (E1)–(E2) remain arbitrary complex numbers.

**Theorem G (two-direction equivalence and reconstruction).** Families of t MOQLS(n) give solutions of E(n,t) by G_s[x,y]=<q_{s,x},q_{s,y}>. Conversely, EVERY solution of E(n,t) factors into a family of t MOQLS(n), with no further rank, positivity, phase or support condition needed.

*Forward proof.* Let V_s be the n by N matrix whose columns are q_{s,x}. Summing the rank-one projectors along each row gives I_n, and there are n rows, so

    V_s V_s^*=n I_n.

Consequently G_s=V_s^*V_s has G_s^2=V_s^*(n I_n)V_s=nG_s. Its diagonal and common-line entries have the specified values. Tensor-product orthogonality gives (E4).

*Reverse proof.* By the finite-dimensional spectral theorem, a Hermitian G_s satisfying (E3) has every eigenvalue in {0,n}. In particular it is positive semidefinite, not merely a Hermitian matrix passing a few minors. Its trace is N by (E2), so its rank is N/n=n. Choose an orthonormal eigenbasis of its positive eigenspace and factor G_s=V_s^*V_s with V_s of size n by N. The diagonal entries show that all columns q_{s,x} are unit vectors. Each actual row and column of the array contains n pairwise orthogonal such vectors, hence is a basis of C^n. Finally (E4), with unit diagonal, makes the tensor-product Gram matrix exactly I_N. Those N product vectors are an orthonormal basis. This constructs the required family. QED.

At n=8,t=5, after Hermitian symmetry and the fixed common-line entries, there are 1568 free COMPLEX off-diagonal positions per square: every one of 64 cells has 49 cells outside its row and column, and unordered pairs divide 64*49 by 2. Thus the full system uses 7840 complex, or 15680 real, free matrix coordinates. This is a dimension/representation count, not a search or a complexity guarantee. All equations are of degree at most two in real and imaginary parts.

Independent output unitaries disappear from G; entry phases act by diagonal-unitary conjugation. Physical relative phases remain in its complex entries and in (E3). Nothing replaces G by its support or modulus in Theorem G.

## 3. An exact nonclassicality invariant and equality-only witness proposal

Define h_s[x,y]=|G_s[x,y]|^2 and

    D(G)=sum_s sum_{x,y} h_s[x,y](1-h_s[x,y]).             (1)

Every solution of E(n,t) has 0<=h_s[x,y]<=1, either by reconstruction or by the 2 by 2 principal minors of the positive-semidefinite G_s. Thus D>=0.

**Theorem C (exact classicality criterion).** A solution of E(n,t) reconstructs a classical family iff D(G)=0.

*Proof.* If the family is classical, every pair of vectors in each square is either parallel or orthogonal, so h is 1 or 0 and D=0. Conversely D=0 implies every h entry is 0 or 1 because every summand in (1) is nonnegative. Fix a square and use its first row as an orthonormal basis b_0,...,b_{n-1}. For any cell vector v, Parseval gives

    sum_j |<b_j,v>|^2=1.

Every term is 0 or 1, so exactly one is 1. Equality in Cauchy–Schwarz makes v a phase multiple of that b_j. A separate unitary for this square therefore makes all its entries computational rays; entry phases remove their scalar phases. Do this for every square. QED.

D is invariant under all the allowed isotopies and square relabelling. A single certified 0<|G_s[x,y]|^2<1 is already a nonclassicality certificate. Conversely a nonclassical QLS must have such a pair, by the same first-row argument.

**Exact construction representation.** Add one REAL scalar z and the polynomial equation

    z D(G)-1=0.                                           (2)

The n=8,t=5 system (E1)–(E4),(2), split into real/imaginary parts, has a real solution iff a genuinely nonclassical family of five MOQLS(8) exists. This follows from Theorems G/C: a nonclassical solution has D>0 and can take z=1/D; any solution of (2) has D!=0, hence D>0. No lower bound epsilon, fixed support, phase alphabet or floating-point tolerance is added. In particular z is not artificially capped.

This is an EXACT witness proposal/interface, not an exhibited solution. A future candidate must give exact field elements or exact real algebraic descriptions for all entries and z, prove the complete matrix equations, and reconstruct the vectors or use Theorem G at its stated spectral-factorization boundary. Modulus data h alone are NOT enough. No algebraic-degree bound, executable solver or existence of such a point is asserted here.

The unproved global theorem is equivalently: this saturated system has NO real solution; or D=0 on all E(8,5); or each square has only orthogonal/parallel rays. These are the SAME full target, not three separate problems.

## 4. Projector-span geometry in the 49-dimensional contrast complement

Let P_{s,x}=|q_{s,x}><q_{s,x}| and H_s=(h_s[x,y]). Then

    h_s[x,y]=tr(P_{s,x}P_{s,y}).

Hence H_s is a real positive-semidefinite Gram matrix in the real Hilbert space of Hermitian n by n matrices, with inner product tr(AB). Its rank equals

    a_s=dim_R span_R {P_{s,x}: x in Omega}.                 (3)

Let J be the N by N all-ones matrix, p=J/N, and let R[x,y] and C[x,y] indicate equality of row and column, respectively. Put r=R/n and c=C/n. These are orthogonal projections, rc=cr=p, and

    E=I_N-r-c+p

is the orthogonal projection onto W, the arrays whose sum in each row and each column is zero. Its dimension is (n-1)^2: the first (n-1) by (n-1) entries determine the remaining row/column entries uniquely.

For every actual array row L and fixed x, completeness gives sum_{y in L} h_s[x,y]=1; the analogous column equation holds. Thus H_s R=H_s C=J and H_s 1=n 1. Define

    T_s=H_s/n-p.                                         (4)

**Theorem T (global covariance operators).** The operators T_s satisfy:

(a) 0<=T_s<=E, ET_s=T_sE=T_s;

(b) tr(T_s)=n-1 and rank(T_s)=a_s-1;

(c) T_s T_u=0 for s!=u.

*Proof.* H_s is positive semidefinite, with constant vector an eigenvector of eigenvalue n. Subtracting p from H_s/n removes just that one-dimensional eigenprojection, so T_s is positive semidefinite. Since H_s has nonnegative entries and every row sum is n, every eigenvalue has absolute value at most n: for an eigenvector choose a coordinate of maximum absolute value and apply the row sum bound. Therefore T_s is a contraction. The identities H_sR=H_sC=J imply T_s r=T_s c=0; Hermitian symmetry gives the reverse products, so its range is in W and T_s<=E. Trace H_s=N, hence tr(T_s)=N/n-1=n-1. Removing the strictly positive constant eigenvalue decreases rank by one, proving (b).

For (c), tensor-product orthogonality makes h_s[x,y]h_u[x,y]=0 off the diagonal. The diagonal terms are 1, so

    tr(H_s H_u)=sum_{x,y}h_s[x,y]h_u[y,x]=N.

Also tr((H_s/n)p)=tr((H_u/n)p)=tr(p)=1. Therefore

    tr(T_s T_u)=N/n^2-1-1+1=0.

For positive-semidefinite A,B, tr(AB)=0 implies AB=0: A^(1/2)BA^(1/2) is positive semidefinite with zero trace, hence zero; this implies B^(1/2)A^(1/2)=0, and consequently AB=0. Apply this to T_s,T_u. QED.

A crucial distinction: the T_s have orthogonal ranges, but are generally NOT projections. Orthogonal ranges do not make their individual eigenvalues 0 or 1.

**Corollary T1 (global span/defect budget).**

    sum_s (a_s-1) <= (n-1)^2,
    sum_s (a_s-n) <= (n-1)(n-1-t).                         (5)

Every a_s>=n, and a_s=n iff square s is classical.

*Proof.* The ranks of operators with mutually orthogonal ranges add and their sum lies in W. Every first row gives n linearly independent orthogonal rank-one projectors, so a_s>=n. If equality holds, the span in (3) is exactly the diagonal matrices in the first-row basis. Every rank-one projector of the square is then diagonal, and therefore a coordinate rank-one projector. The converse is immediate. QED.

In the actual five-square order-eight problem this reads

    sum_{s=1}^5 (a_s-8) <=14.                              (6)

The integer a_s-8 measures the extra dimension of each square's projector span beyond a classical basis. Arbitrary independently perturbed QLS typically need not fit this small JOINT budget; (6) is a necessary constraint on actual MOQLS, not merely on their axis supports. No claim of novelty or prior-art optimality is made.

## 5. A positive residual operator and the exact missing fractional-spectrum step

Set

    K=E-sum_s T_s.

The mutually orthogonal ranges and contraction bounds in Theorem T give K>=0; also K<=E. Its trace and diagonal are

    tr K=(n-1)(n-1-t),
    K[x,x]=(n-1)(n-1-t)/n^2.                               (7)

At n=8,t=5:

    tr K=14,                  K[x,x]=7/32,
    K[x,y]=-1/32             if x!=y share a row or column,
    K[x,y]=3/32-(1/8)sum_s h_s[x,y] otherwise.              (8)

At most one h_s[x,y] is nonzero for a fixed distinct pair; the last expression therefore retains its actual overlap value, not just a bit. To check (8), expand

    K[x,y]=delta_xy-(R[x,y]+C[x,y])/8+6/64
             -(1/8)sum_s h_s[x,y].

**Theorem D (fractional-spectrum identity).** At n=8,t=5,

    K-K^2=sum_s (T_s-T_s^2),
    tr(K^2)=14-D(G)/64.                                    (9)

Consequently a nonclassical family requires rank(K)>=15. Classicality is equivalent to K being a projection, and also equivalent to all T_s being projections.

*Proof.* ET_s=T_s and T_sT_u=0 for s!=u make the first identity an expansion of K^2. Moreover

    tr(T_s^2)=tr(H_s^2)/64-1,
    tr(T_s-T_s^2)=8-(1/64)sum_{x,y} h_s[x,y]^2.

The row sums of H_s are 8, so sum_{x,y}h_s[x,y]=512. Thus the last expression is (1/64)sum h_s(1-h_s). Summing proves (9). If D>0, then tr(K^2)<14. For a positive-semidefinite matrix of rank m, Cauchy–Schwarz on its positive eigenvalues yields (tr K)^2<=m tr(K^2). Therefore 196<14m and m>14. Conversely K is a projection iff tr(K-K^2)=0, because its eigenvalues lie in [0,1]. By (9) this is D=0, exactly classicality by Theorem C. The identical argument applies to the individual T_s. QED.

This isolates a precise global obstruction: five MOQLS can violate classicality only through FRACTIONAL eigenvalues in these orthogonal covariance ranges, producing a positive trace-14 residual of rank at least 15. The theorem does NOT exclude such an operator. An integer trace is NOT proof of idempotence, and rank>=15 in a 49-dimensional space is not a contradiction. Neither (5) nor (9) closes the full target.

## 6. Two-basis span lemma, retaining every amplitude and phase

Let b_1,...,b_n and v_1,...,v_n be orthonormal bases and U[k,i]=<b_k,v_i>. Form its bipartite support graph on the n row vertices k and n column vertices i, joining them exactly when U[k,i]!=0. Let c(U) be the number of connected components.

**Lemma B (exact axis span).** The real span of the 2n rank-one projectors onto these two bases has dimension

    2n-c(U).                                               (10)

*Proof.* Each basis spans an n-dimensional real diagonal algebra A_b or A_v of Hermitian matrices. An operator D in their intersection is D=diag_b(d_k)=U diag(lambda_i) U^*, with real coefficients. Equivalently

    D U=U diag(lambda_i),
    (d_k-lambda_i)U[k,i]=0.

Thus d_k=lambda_i across every support edge, so all values are constant on each graph component. Conversely assigning an arbitrary real constant to each component gives exactly such a common diagonal operator. Hence the intersection has dimension c(U), and the dimension formula for the sum gives (10). This proof uses no restriction on nonzero amplitudes or phases. QED.

If the transition has an entry supported on w basis coordinates, its graph component contains at least w row vertices, so c(U)<=n-w+1; (10) gives a_s>=n+w-1 for any square containing both bases. This is only a necessary lower bound, not a support classification.

## 7. Substantive B3 consequence: minimal rank forces block-pure full cells

Condition ONLY in this section on the old P1-B3 H1–H4 data:

- The five Q_s satisfy the full physical axioms.
- Row0 is the computational basis up to phases.
- Q_1 column0 supports, in rows 0,...,7, are

    {0}, {1,2,3}, {6,7}, {6,7}, {4,5}, {4,5}, {2,3}, {1,2,3}.

These are literal support hypotheses; this section does not claim that the old U/T16 global import is freshly discharged. Put Z={0}, A={1,2,3}, C={4,5}, B={6,7}, and use the corresponding coordinate subspaces V_X.

The row0/column0 transition graph has exactly FOUR components:

- row0 and coordinate0;
- rows1,6,7 and coordinates1,2,3 (connected, including the prescribed nonzero coordinates of rows1 and7);
- rows2,3 and coordinates6,7;
- rows4,5 and coordinates4,5.

Thus Lemma B makes the span S_axis of the rank-one projectors on those two axes have dimension 16-4=12, for ALL amplitudes/phases realizing the stated column ONB. In particular

    a_1>=12,
    sum_{s=2}^5(a_s-8)<=10.                                (11)

**Theorem B3 (minimum-span dichotomy).** Every genuine full P1-B3 family satisfies one of:

(i) a_1>=13; or

(ii) a_1=12, EVERY cell vector of square1 lies entirely in one of V_Z,V_A,V_B,V_C, and every row and every column of square1 has exactly 1,3,2,2 vectors in those blocks, respectively.

If any cell of square1 has nonzero components in two different blocks, case(i) is forced and the right side of the second inequality in (11) decreases to 9.

*Proof.* Every axis projector is block diagonal for the displayed four-block decomposition. Therefore S_axis is a 12-dimensional subspace of the block-diagonal Hermitian matrices. If a_1=12, the full projector span equals S_axis; in particular every full-cell projector vv^* is block diagonal. A rank-one vv^* is block diagonal iff v has a nonzero component in just one block: if v_X and v_Y were both nonzero, its X,Y block v_X v_Y^* would be nonzero. Thus all full-cell vectors are block-pure. In a complete orthonormal basis assembled from vectors in orthogonal blocks, the number in each block equals that block's dimension. This proves the row/column counts. Conversely a mixed-block cell contributes a projector outside the block-diagonal S_axis, so adjoining it increases the span dimension to at least13. Apply (6) for the remaining budget. QED.

A useful exact consequence of case(ii): the eight Z-cells of square1 contain the ray e_0, one per row and column. On those same eight cells, EACH other square is an ONB, because its tensor product with square1 must be orthogonal for every distinct pair of Z-cells. This is a necessary shared-transversal condition, not a completed extra QLS or a whole-grid witness.

**What this does and does not add.** The old B3 analysis projected cells onto blocks and constrained masses/capacities; it did not supply this projector-span budget or this written rank-saturation alternative in the baseline sections read. Here the full square is either already above its axis-span minimum or is block-pure everywhere. The result is uniform in arbitrary axis phases and arbitrary full interior vectors. It does NOT assert that a_1=12 is realizable, that the block-pure case is impossible, that every cell is mixed, or that either branch is excluded. Its novelty outside this repository is unassessed.

## 8. Trust map and unchanged obligations

### A. Mathematical imports used by this candidate

- Ball–Simoens arXiv:2607.12933v2 §§2.2–2.3 for the literal physical definitions; Problem16 for the target. Musto–Vicary arXiv:1804.04042v3 Definition4/Lemma6 supplies the same product-Gram convention. The forward/reverse theorem here is proved above, rather than imported as an unverified equation-system sufficiency claim.
- Elementary finite-dimensional complex spectral theorem/Gram factorization; real Gram rank equals real span dimension; positive-semidefinite trace-zero and square-root facts; dimension formula for sums of subspaces; Parseval and Cauchy–Schwarz. The load-bearing applications and all counts are displayed in the written proofs.
- For §7 ONLY: the exact B3 support table from the old genuine-pair/continuation manuscripts. Its ONB/full-family assumptions remain explicit. No numerical sparse-class classification, UNSAT certificate, catalogue count, withdrawn sparsity overclaim, mass-case sufficiency or 22-cell-to-full-grid bridge is used.

### B. Baselines consulted but NOT mathematical premises of §§2–6

- six-lane-2026-10-18-96h/report/continuation-report-2026-10-22-final-v17.md §5.1, read with review/sixlane-report-v17-operative-delivery-erratum-v1.md.
- Genuine GB/NF verdict, pair reduction and their errata; FRONTIER-after-gbs7-distinct-six-v1.json and the original GB necessity text. These fix the baseline/count boundary only. No old Boolean SAT model is treated as physical.
- M(7)=2, K1/K2/K3 exclusions, external MOLS classifications and the 18 GA/18 GB coverage contract. None is needed to prove Theorems G/C/T/D/B3 here. This candidate changes NONE of their scientific/verification statuses.

### C. Explicit residual scientific and acceptance gates

1. Still unproved: D=0 on all E(8,5), or an exact point with D>0. No full Problem16 answer or independent scientific gate is claimed.
2. B3 case(i) is unrestricted beyond the proved span budget; case(ii)'s block-pure full-grid existence/exclusion is open here. Both remain in the primary target. B2 and all other normalized classes were not silently discarded.
3. GB B2.M2, B2.M4, B3.M2 remain UNKNOWN. H23/H24 pair UNSAT premises remain unproved. A10/A11, shared U/T16/WMAN/NF imports and whole-vector completion retain their prior boundaries.
4. Old runtime HOLD, unbounded final-wait risk, unexplained old termination, proof-retention qualifications, controls and preservation obligations survive. No held runtime is restarted or repaired, and no new computation is requested by writing this proof.
5. Correctness level is author-written CANDIDATE only. No independent reconstruction, parent acceptance, formal kernel, human referee, novelty clearance or SOTA improvement has occurred for this file. A source search miss is not an openness or priority theorem.
