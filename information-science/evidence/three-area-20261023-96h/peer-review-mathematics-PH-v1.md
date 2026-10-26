# Independent in-harness written review: repeated-pole PH candidate

Before-creation clock observed: **2026-10-23T12:58:51-07:00**. Reviewer: `InfoResearch96h`, at the parent's explicit request. This is a read-only mathematical review by a different in-harness agent, not cross-vendor, human, finite-certificate or kernel verification. No scientific program, symbolic-algebra execution, solver, test/build suite or nested agent was used. Author files were not modified.

## Reviewed inputs and exact boundary

Read the **entire** manuscript `mathematics/evidence/three-area-20261023-96h/proof-repeated-pole-PH-v1.md`, lines 1–251, SHA-256:

`ae4d983da5de5f897b262c92dd7594aac1905e2cdfcc6b6f8b5cb9e43b89bb6f`.

Read the complete `mathematics/evidence/three-area-20261023-96h/selection-v1.md`, including the untruncated candidate table, SHA-256:

`21afe24cf231072e051cc4474d774c5f75c042e94974e9042fdabf8d96ac595f`.

Opened the actual official [Ellard–Smigoc arXiv:1702.02650v1, Theorem 1.2](https://arxiv.org/html/1702.02650v1#S1.Thmtheorem2) and read its hypotheses, iff criterion and companion-plus-scalar conclusion. The 2006 proof is a classical theorem-level import; I did not authenticate its whole proof. No separate priority audit of repeated-pole PH literature was performed.

## Verdict

**No substantive mathematical defect found at the explicit boundaries below. Findings: 0 FATAL / 0 MAJOR / 0 MINOR.** Theorem A is supported conditional on the precisely declared classical Theorem 1.2 import. Theorem B's displayed five/six-state band and universal five-state exclusion reconstruct without that import. Novelty remains unestablished. This review is not a parent acceptance or a full-book resolution.

## Independent reconstruction

### 1. Denominator/characteristic binding — manuscript lines 34–42

The nonzero constant numerator is coprime to every denominator factor. For an N-state PH transform, its reduced denominator divides the monic characteristic polynomial of T. Thus N>=r+2q, and equality forces the full characteristic polynomial to equal D_(r,q), including algebraic multiplicities. This does not assume controllability/observability, absence of Jordan blocks or a priori minimal positive realization. The candidate correctly avoids treating a chosen spectrum as sufficient for the transfer function.

### 2. Exactly r Frobenius blocks — lines 44–50

For each irreducible Metzler diagonal block, shifting sufficiently far by the identity yields an irreducible nonnegative matrix with strictly positive diagonal; Perron–Frobenius makes the block spectral abscissa a real algebraically simple eigenvalue. The complete spectrum has only one real value, -c. Hence every block contains exactly one copy of -c and there are exactly r blocks. Realness forces its remaining entries to occur as conjugate pairs, so its size is 2q_j+1 and the q_j sum to q. Singleton blocks q_j=0 are allowed. The pigeonhole use q_j>=ceil(q/r) is valid.

### 3. Block trace obstruction — lines 50–71

For ell pairs, shifting by c yields eigenvalues 0 and -d±ib, each nonreal eigenvalue repeated ell times. Therefore trace=-2ell d and trace-square=2ell(d^2-b^2), even with nontrivial Jordan structure. Since the off-diagonal entries are nonnegative, trace(M^2) is at least the squared-diagonal sum; real Cauchy–Schwarz bounds this by trace(M)^2/(2ell+1). Rearrangement gives b^2<=d^2/(2ell+1). In particular every five-state representation of H_(1,2) requires beta^2<=1/5. No restriction to companions, cycles or irreducible global T is introduced.

### 4. Classical import and transfer-preserving normalization — lines 75–127

The accessed primary theorem indeed permits a self-conjugate list with rho>=0 and all other real parts <=0, and requires s_1>=0 and s_1^2<=n s_2. It also gives C+eta I with C a trace-zero nonnegative companion and eta>=0. The candidate's shifted list has s_1=0 and s_2=2ell(d^2/n-b^2)>=0. Trace therefore forces eta=0, supplying the required nonnegative companion itself. Repeated entries are not excluded by the theorem statement.

Independently solving the upper-shift companion's first n-1 equations gives y_i=(s+lambda)^(i-1)y_1 and the last equation D_ell(s)y_1=1 for input e_n. Thus output e_1 and input k e_n have transfer k/D_ell(s), in the **stated orientation**. The shift lambda=c+2ell d/n maps the positive eigenvalue to -c and the repeated pairs to -a±ib.

With h_i=lambda^(i-1), the first n-1 rows of -Ah vanish and the last is P(lambda)=k. Hence h is positive, -Ah=k e_n, S^(-1)AS is a Hurwitz Metzler subgenerator, and e_1 S=e_1. The exit and initial row in the candidate therefore preserve the exact transfer and total initial mass; this is not merely a spectral realization.

### 5. All-r cascade — lines 129–142

The balanced distribution of q pairs among r blocks has maximal count ceil(q/r), so all blocks satisfy the correct parameter inequality. For off-diagonal connector w_j alpha_(j+1), each nonfinal block row sum is zero because alpha_(j+1)1=1; only the final block absorbs. Block triangularity preserves stability, and successive block-resolvent multiplication gives the product of the normalized block transforms. State count is exactly r+2q. No extra Perron pole is silently assumed in the necessity direction.

### 6. Explicit five-state coefficients and endpoint — lines 144–175

By direct hand expansion,

    (x-4t)(x^2+2tx+v)^2
      =x^5+(2v-12t^2)x^3
          -(16t^3+4tv)x^2
          +(v^2-16t^2v)x-4tv^2.

These are exactly the candidate's U,V,W,Z signs and coefficients. Under b^2<=5t^2, v<=6t^2, U>=0, V,Z>0 and W=v(16t^2-v)>0. The shift lambda=c+4t gives the correct five denominator factors. Positive diagonal scaling has final exit K/lambda^4 and alpha=e_1. At equality U=0 is allowed; irreducibility and stability do not rely on U being strictly positive. The endpoint beta^2=1/5 is therefore included.

### 7. Six-state construction, cancellation and initial law — lines 177–227

Direct expansion gives

    (x^2-d^2)(x^2+b^2)^2
      =x^6-(d^2-2b^2)x^4
           -b^2(2d^2-b^2)x^2-d^2b^4.

Thus the displayed companion is nonnegative when b^2<=d^2/2; at equality its scalar A coefficient is zero but B,C remain positive. Shifting by a yields extra pole -(c+2d), not a missing or unstable eigenvalue.

The companion equations give e_2-resolvent output z/P_6(z), so the nonnegative row d e_1+e_2 creates numerator z+d=s+c+2d and cancels exactly the extra pole. This orientation and the sign of d are essential and correct.

For h_i=a^(i-1)/(c+2d), -Gh=K e_6 because P_6(a)=K(c+2d). The initial row is (d/(c+2d),a/(c+2d),0,...,0); its sum is 1 since a+d=c+2d. The final exit K(c+2d)/a^5 is positive, all other row sums are zero, and similarity preserves the stable spectrum. Thus these are genuine PH parameters, including beta^2=1/2. Above beta^2=1/5 the universal five-state obstruction makes this six-state representation minimal.

### 8. Remaining-range and topology statements — lines 237–245

The candidate explicitly limits the failure A<0 above beta^2=1/2 to its fixed construction, and makes no general six-state/non-PH conclusion. A real sixth-degree characteristic polynomial divisible by the fifth-degree D_(1,2) has one additional real linear factor, so the stated prospective form is correct.

The directed-single-cycle obstruction also checks: at a nonreal repeated root of prod_i(z+lambda_i)-kappa, the nonzero product allows logarithmic differentiation; every reciprocal has strictly negative imaginary part for Im z>0, so the sum cannot vanish. This only excludes that topology and is appropriately not asserted novel.

## Limits of this review

- All calculations above are written symbolic reconstruction, not executable output.
- The Ellard–Smigoc statement was authenticated at theorem level; its imported historical proof was not independently reproduced.
- I did not independently audit the source book images, every historical PH dossier, or the entire repeated-pole prior-art literature.
- Correctness at this scope does not establish scientific priority, a new spectral theorem, general minimum PH order, or publication readiness.
