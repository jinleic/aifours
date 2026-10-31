# Any PH7 realization at 8/9 needs triangles on at least TWO distinct vertex triples

**NEW ALL-TOPOLOGY CRITICAL THEOREM CANDIDATE. Exact six-variable copositivity certificate plus separately written stdlib integer replay. Independent peer review, parent adoption, formal proof and novelty clearance pending.** MathResearch96h-2, original math-1. This strengthens the earlier mandatory/imbalanced-triangle candidates; it does NOT settle the existence of a seven-state realization.

## 1. The theorem

At `z=b²/(a-c)²=8/9`, any actual PH representation of the original H using at most seven states has directed 3-cycles supported on at least **two different unordered sets of three vertices**.

Equivalently, no irreducible real seven-state Metzler matrix of spectral bound0 and characteristic factor `D(y)=y[(y+1)^2+8/9]^2` can have all its directed triangles confined to ONE vertex triple. That triple may carry one orientation, BOTH orientations, or no triangle. Arbitrarily many 2-, 4- and longer cycles and arbitrary edge counts are allowed.

This is not merely a count of orientations: the two opposite orientations on one triple do not suffice. The theorem still permits two triangles on different triples, so unrestricted PH7 at8/9 and minimum8 remain open.

## 2. Symmetrization and the discrepancy of the single triple

Normalize G by a positive Perron diagonal similarity to an irreducible row generator; this preserves graph, diagonal entries and all directed cycle products. Define

    S_ii=G_ii,   S_ij=sqrt(G_ij G_ji),   M=-S.

As in the separately frozen mandatory-triangle proof, Perron left/right vectors and rowwise Cauchy imply S is negative semidefinite, so M is symmetric positive semidefinite. Every proper principal block of M is positive definite: after adding a sufficiently large scalar identity, a proper principal block of the irreducible nonnegative G has strictly smaller Perron radius, and geometric-mean symmetrization cannot increase its radius.

Let C be the sole possible triangle vertex triple. Denote by A and B the actual products of the two opposite triangle orientations, allowing either to be0, and set

    w=A+B-2 sqrt(A B)=(sqrt(A)-sqrt(B))² >=0.

Every other triangle contribution vanishes. Symmetric S has the same 2-cycle products as G; its two triangle orientations on C have total product `2sqrt(A B)`. Thus

    [y^4]det(yI-G)=[y^4]det(yI-S)-w.                (C4)

Let L be the sum of the four original diagonal escape rates outside C, equivalently `tr M_(outside C)`. At y3, the disjoint 2+2 terms are the same and the 3-cycle discrepancy is `-w L`. For each unoriented 4-cycle, the two G orientation products sum to at least the two S orientation products by AM–GM, including missing edges. Therefore

    [y^3]det(yI-G) <= [y^3]det(yI-S)-w L.          (C3)

The y6 and y5 coefficients of G and S are identical. These statements account for ALL triangles, 4-cycles and disjoint 2-cycles; no graph sparsity or numerator simplification is assumed.

## 3. Bound the triangle discrepancy by a principal determinant

Label C so one orientation is `1->2->3->1`, and write original diagonal escape rates as u1,u2,u3>0. Let

    p_i=G_(i,i+1)/u_i,     q_i=G_(i,i-1)/u_i,
    P=p1p2p3,             Q=q1q2q3.

Row normalization gives `p_i,q_i>=0` and `p_i+q_i<=1`. The triangle products are `A=u1u2u3 P`, `B=u1u2u3 Q`, and

    det(M_C)/(u1u2u3)
      =1-[p1q2+p2q3+p3q1]-2 sqrt(P Q),
    w/(u1u2u3)=P+Q-2 sqrt(P Q).

Because `q_(i+1)<=1-p_(i+1)` and `Q<=product_i(1-p_i)`, the identity

    sum_i p_i(1-p_(i+1))+P+product_i(1-p_i)=1

shows `w<=det(M_C)`. The proper principal block M_C is positive definite.

Let the eigenvalues of M be `0<=lambda1<=...<=lambda7`. Cauchy interlacing gives each eigenvalue of M_C at most the corresponding one of `lambda5,lambda6,lambda7`; hence

    0<=w<=det(M_C)<=lambda5 lambda6 lambda7,
    lambda5,lambda6,lambda7>0.

Ky Fan's minimum trace principle, applied to the four-coordinate outside projection, gives

    L=tr M_(outside C) >= lambda1+lambda2+lambda3+lambda4.  (KY)

Thus `theta=w/(lambda5 lambda6 lambda7)` belongs to[0,1], even when the triangle is balanced and w=0.

## 4. Reduce to a universal six-rate inequality

Let e_j be the elementary sums of all seven lambda_i, and set `m4=lambda1+...+lambda4`. The actual target quotient is a real monic `Q=y²+p y+q`; irreducibility gives `q>0`. By the y6,y5 identities, p and q are the usual polynomials of e1,e2. Equations(C4),(C3),(KY) imply

    E4=e3-w-4e2+(74/9)e1-28/3=0,
    E3=e4-w m4-(70/9)e2+(212/9)e1-1007/27 >=0.     (NEC)

Take the first six auxiliary rates as the positive top three `lambda5,lambda6,lambda7` followed by any three of the nonnegative bottom four; call the remaining bottom rate x>=0. Let f1,...,f4 be the elementary sums of those six and O the sum of their three outside rates. Define

    A0=f2-4f1+74/9,
    B0=f3-4f2+(74/9)f1-28/3-w,
    h0=f4-(70/9)f2+(212/9)f1-1007/27-w O,
    h1=f3-(70/9)f1+212/9-w,
    Qpol=81[A0²-(f1-4)B0],
    Hpol=-243[h0 A0-h1 B0].                         (QH)

The exact universal lemma in §5 proves `Qpol>0,Hpol>0` for EVERY three positive triangle rates, EVERY three nonnegative outside rates, and EVERY theta in[0,1], with `w=theta product(top3)`.

The first condition in(NEC) is `A0 x+B0=0`. If A0=0 it forces B0=0 and hence Qpol=0, contradiction. Otherwise x=-B0/A0, and the hidden constant and second residual are

    q=Qpol/(81 A0),       E3=-Hpol/(243 A0).

Since q>0 and Qpol>0, A0>0, hence E3<0. This contradicts(NEC), proving the theorem. □

## 5. The exact universal six-rate/whole-theta lemma

For fixed rates, Qpol is linear in theta. Its Bernstein endpoints `Q0,Q1` are strictly positive on the stated rate domain. Hpol is quadratic; write

    Hpol=H0(1-theta)²+2 H1 theta(1-theta)+H2 theta².

The certificate proves `H0>0,H2>0`, and on EVERY rate point proves at least one of

    H1>=0     OR     H0 H2-H1²>0.                   (DUAL)

If H1>=0 the quadratic is strictly positive. Otherwise(DUAL) makes the symmetric matrix `[[H0,H1],[H1,H2]]` positive definite, so the quadratic is strictly positive for all theta, including endpoints. Hence Qpol,Hpol are strictly positive for all theta in[0,1].

The rate domain is mixed: the FIRST three rates are strictly positive, the OTHER three may be0. Compactify `ui=xi/(1-xi)`; the checker certifies positivity on the entire resulting mixed six-cube, using exact integer tensor Bernstein subdivision and all required finite zero-rate faces. The four endpoint polynomials use `5332,1869,5334,2443` certified leaves. A two-way cover adds `2714` leaves where `2H1>=0` and `199` leaves where `4(H0H2-H1²)>0`; these 2913 leaves cover the FULL domain. Strict vertex tests include the nonnegative outside-rate boundary and require positivity only for finite points with the first three rates positive.

## 6. Actual verification and independent review interface

Primary `frontier-20261028-ph7-one-triple-universal-lemma-check.py`, **89LF/4997B**, SHA256 `55491fb10cf0b707c093778a08f42c0af0e49d81703d09f1aceec99efbf69f8f`, actually printed

    SymPy 1.14.0 integer Bernstein PASS: Q,H positive for all theta and nonnegative outside rates
    single leaves 5332/1869/5334/2443; dual H1/Gram leaves 2714/199

Certificate `frontier-20261028-ph7-one-triple-universal-lemma-certificate.json`, **17991LF/459106B**, SHA256 `5ae72d0faddcd3865db5e91f2ac3d511ac77f5ce89f32c33faf50f45c94d0920`, pins all six exact coefficient digests and all binary trees. NumPy object arrays in the primary contain only Python integers.

Separately written STANDARD-LIBRARY-ONLY replay `frontier-20261028-ph7-one-triple-universal-lemma-integer-replay.py`, **133LF/5847B**, SHA256 `c7c06246f96a901e7f2aa5bb1029c379e5d8d5d2862134a9256b73dabdc97694`, independently constructs Q/H from sparse rational elementary sums, derives all six Bernstein/Gram polynomials, checks coefficient digests, and verifies every required integer coefficient, open/zero boundary face and FULL dual tree. It actually returned

    Independent stdlib integer PASS: 6 exact polynomials, 14978 positive leaves and 2913 complete copositive leaves

It consumes the certificate's path lists; it is independent implementation evidence, not human/cross-vendor/Lean verification. A disjoint reviewer should reconstruct the six polynomials and BOTH classes of cover leaves rather than rely on these scripts, and check the complement condition in(DUAL), not an assumption that H1 itself is always positive.

## 7. Review and original-question boundary

The PH application depends on the separately supported SCC/Perron normalization. Named ordinary imports: determinant cycle expansion; positive Perron comparison; 3-by3 determinant; Cauchy interlacing and Ky Fan trace; AM–GM; exact integer Bernstein subdivision. Review must check BOTH triangle orientations, the actual w<=det(M_C) identity, all 4-cycle signs, the mixed zero-face domain, q>0, and the PH caller.

The result does NOT exclude two triangles on different triples, any more complicated short-cycle graph, or an actual PH7 solution at8/9. No minimum8, global frequency bound, novelty, formal/kernel, cross-vendor review or historical process repair is claimed. Earlier held outputs remain nonpremises and process findings survive.

END — every critical seven-state PH representation must have directed 3-cycles on at least two distinct vertex triples.
