# Full-dependency in-harness reconstruction — two-pair Werner reference candidate

Reviewer: **MathSemigroup**, actual math-4 owner. Assigned by `peer-review-wave-eighteen-v3.json`; primary semigroup ownership retained. Actual clock observed immediately before creation: **2026-10-23T15:28:30-0700**.

## 1. Verdict, exposure and exact coverage

**FATAL0 / MAJOR0 / MINOR0 at Theorems A–B's stated two-equal-pairs reference scope and the exact load-bearing dependency closure.** The all256-dimensional asymmetric inequalities, t>0 kernel count, and arbitrary-complex rank-two range/co-range consequence reconstruct correctly on the boundaries detailed below. This is not unrestricted W4, a symmetric-GS theorem at every angle, novelty clearance, formal/kernel verification or automatic parent acceptance.

Exposure: this was a supplied-proof review, NOT blinded. I had round-level awareness of the W4/reference-ray topic, but had not previously authored or reviewed these Werner physical block tables. For this assignment I read the common/individual v3 contract, exact selection, complete manifest, complete358-line main proof, and **the actual complete bodies of ALL SIX leaves**. I did not infer correctness from their statuses/hashes or earlier model verdicts.

No scientific executable, Python/Fraction cell, CAS, matrix program, enumeration, eigensolver, compilation or certificate replay was used. All calculations below are written index/representation/algebra reconstructions. Commands were metadata hashes and actual clocks only. No author/shared file was edited; this is the only output created for this assignment.

### Observed source pins and body coverage

All paths below are under `physics/evidence/three-area-20261023-96h/parallel-18/werner3-ququart/`.

| Input | Actual SHA-256, matching assignment/manifest | Complete body read |
|---|---|---|
| main `proof-two-pair-reference-asymmetric-domination-v1.md` | `c882c5678969a80d0b7c9800dc9086070cf3f70f7b9143c0f08e77db41292478` |1–358|
| manifest |`6b16b61e9f2cae541c2f1e4df79f0b5a55e6f8cc0013c255ffbc60a63271370b`|full JSON|
| checkpoint002 |`47a24185bbf5f1a1de7fbe64f4ec585feda2b488b1e68b53c11fe35c7ad21ecf`|1–208|
| checkpoint003 |`761e04717ce22a786352ab75b1faf6ff3c4b865e13714a8da81a290def169a5e`|1–152|
| checkpoint004 |`fc210c46216932b4846d7cad6c1754538d4d66ff597c951d57533ff4b7e6eaf4`|1–111|
| checkpoint005 |`a7432f7d2d417f60f5bc64d3eea042ca8556b7fe936081afdf25bba4394f5147`|1–131|
| checkpoint006 |`cc8e1ed4830e728cd4f168d3ee3b9657f7aa684908842385a4ac719d0b281399`|1–223|
| checkpoint007 |`4299d5a8e3259f7d7c0911abe6a34a830c62318ad598476450dcf99daf9600b3`|1–273|

The needed fixed Schur matrices and one-site bridge from006 were reconstructed. Its **auxiliary symmetric-plus quartic classification** was read but is not a premise of main A–B or007's asymmetric proof; this verdict does not separately certify that auxiliary angular-classification result. The earlier checkpoint001, legacy uniform GSd acceptance, old assays and parent arithmetic were not imported to prove A–B. The required physical identities are reconstructed directly below. There is therefore no missing load-bearing body hidden behind those older consistency references.

## 2. Physical convention and FULL inverse

With Lambda(X)=Tr(X)I-X/2, direct marginal expansion gives

    A_eta=||eta||^2 I-(rho_1 tensor I+I tensor rho_2)/2
                   +|eta><eta|/4.

For eta=(1,1,t,t), D has precisely a=1+2s,b=2+s,c=3(1+s)/2 on AA,BB,mixed pairs. Hence

    A_eta=D+|eta><eta|/4,
    A_eta^-1=D^-1-r|H><H|,
    H=D^-1 eta, r=1/[4+2(k+l)].

This is Sherman–Morrison for the entire16-dimensional reference matrix. All diagonal D entries are positive including t=0. Also C_B=(I-F13/2)(I-F24/2)>=I/4. Its input-reference compression is A_eta, so A_eta>=||eta||^2 I/4 independently of Schmidt rank. There is no inversion of a compression masquerading as the full inverse.

I reconstructed the physical matrix elements from

    L_rs=delta_rs c_r I-(c_s E_rs tensor I+c_r I tensor E_sr)/2
                         +|rs><eta|/4,

which gives exactly the source's vector formula for L_rs†|uv>. The reversed co-Choi row/column orientation is

    S_((i,o),(j,p))=<L_j†o,A_eta^-1 L_i†p>.

A convenient independent way to organize ALL the real-basis contractions used here is to define

    T_uv=|uv><eta|-(c_u/2)(I tensor E_vu)
                      -(c_v/2)(E_uv tensor I)
                      +(c_u delta_uv/4)I.

Its i-th column is L_i|uv>. If R_X is the real coefficient matrix of a physical basis vector X (input rows/output columns), the D-inverse contribution is

    sum_uv d_uv^-1 Tr(R_X T_uv R_Y T_uv).

The inverse correction is -r Tr(R_X V R_Y V), V|i>=L_i H. These formulas retain the reversed-input convention; substituting an ordinary Choi matrix would change them.

Direct substitution gives V=0 on mixed input pairs. On AA it is delta I+k|Omega_A><Omega_A|, on BB it is -delta I+(1/b)s|Omega_B><Omega_B|, with the cross terms t k|Omega_A><Omega_B| and(t/b)|Omega_B><Omega_A|. Thus the normalized Omega block is exactly[[u/2,2t/a],[2t/b,v/2]] in002. This explains both where the inverse correction cancels and where it MUST remain. On nonzero central charges it vanishes by exact support; on fixed/product-adjoint/all-A adjoint sectors I retained its nonzero form.

## 3. Exhaustive representation accounting, not selected compressions

The correlated group acts with positive slots1,3 and conjugate negative slots2,4. Co-Choi covariance uses the SAME two-site representation on input and output for the reversed convention. The reference is invariant. Central charges have dimensions16,64,96,64,16: the charge-zero patterns are all-A16, all-B16 and four balanced mixed patterns of16 each.

Each all-A four-leg representation decomposes into two trivial copies, three adjoints and one spin-two, dimensions2+9+5=16; likewise all-B. Every mixed balanced pattern is End(A) tensor End(B)=(1+3) tensor(1+3). Consequently charge zero is exactly

    fixed8 + spin-two A5 + spin-two B5
           + product-adjoint36 + adjoint A21 + adjoint B21.

For charge+1, each of its two group patterns has an external two-dimensional fundamental and a triple on the other group. The triple has two fundamental copies and a four-dimensional higher component. Across orientations this gives higher16 and lower16 in EACH pattern; both charge signs give higher64+lower64. Extremal charges add32. All physical dimensions therefore total

    32+64+64+8+10+36+42=256.

The contraction embeddings U1,U2 have Gram blocks2I,I,2I and joint range dimension4. Their orthogonal complement is four-dimensional; the negative-leg swap is +I there because U1-U2 exhausts its two-dimensional antisymmetric part. Intertwiner completeness (the two-dimensional commutant span{I,F}) excludes coupling to the other charge-one pattern on this higher component. These are genuine reducing representations. No positivity is extended merely from a principal block.

The fixed eight contractions have the stated Gram data. Main's product-adjoint highest-weight coordinate vectors exhaust its four-copy multiplicity space. For adjoint A, P,Q,R are independent highest weights with Gram[[2,0,1],[0,2,1],[1,1,2]]; the four B patterns are orthogonal, norm squared2. Thus the seven-vector form exhausts that multiplicity, rather than an assumed invariant subspace of it.

## 4. Fixed8: physical table, upper sign and asymmetric lower sign

Using the trace-contraction formula of §2, I recovered002's fixed table. For example,

- <Omega_A|T|Omega_A> equals3/2 on each A diagonal label and t/2 on each B diagonal label. Squaring and summing D weights gives(9k+l)/2; the full correction is-r u^2.
- The p_A,q_A D part is(-3k+l)/4; its correction is-r u^2/2.
- The q_A,q_A trace over the four AA labels gives-3k/2, while the BB diagonal terms give l/2; its full correction is-r(3k^2+l^2).
- The cross p_A,p_B D term is zero, but its correction is-16rkl; the p_A,q_B and q_A,q_B corrections are respectively-8rkl and-4rkl.
- Each of the four p_A,q_AB contractions is-3t/(4c), giving-3t/c=g. The q_A,q_AB classes cancel. q_AB,q_BA gives3k/2+3l/2=h.

These recover all independent entry types; A/B interchange supplies their partners, not a new inverse approximation.

The reference-kernel identity follows directly from sum_i eta_i L_i=A_eta and adjoint preservation. Hence(C_B-S_eta)(eta tensor z)=0 without assuming the desired PSD. In fixed8 this gives exactly K_A,K_B. Their C form is the actual A_eta form on Omega_A,Omega_B:

    K2=[[3+4s,t],[t,4+3s]], det K2=12(1+s)^2.

For t>0 the stated basis change to(K_A,K_B,Z) is invertible. The separated z_minus scalars are positive. I checked003's Schur reduction: P has determinant64p/[3(1-p)] and inverse[[1/l+2,-1],[-1,1/k+2]]/8. Its residual R has diagonals(13+18k+9k^2)/8 and the l analogue, off-diagonal9p/2, coupling -g(1+3k,1+3l)/2 and z pivot3(1+3p). Thus R>=9I/8; the exact factorization

    81p^3-90p^2+18p-1=(9p-1)(9p^2-9p+1)

proves ||b||^2<=2 and final pivot>=11/9. The upper fixed form has exactly its two reference kernels for t>0.

For the fixed asymmetric lower bound I reconstructed the load-bearing006 Schur entries, including T^-1E's displayed columns, f(k), and R12=-6p(5+39p)/[35(1-p)]. Substitution l=(1-k)/(1+3k) gives the reported f polynomial; its factorization f(x)+1/2=(1-x)(231+387x+513x^2-171x^3)/[70(1+x)^2] yields R>=-7I/10.

In007, T3-T is positive because its unscaled determinant is10p(1-p); T3 has determinant616p/[3(1-p)]. The inverse and E-contraction give exactly

    1^T T3^-1 1=(1-p)/(22p),
    E^T T3^-1 1=((3k-1)/11,(3l-1)/11).

Therefore R3>=19I/5, Z3>=112/11 and ||q3||^2<=410/121. The last Schur subtraction is at most205/616, leaving10679/3080>0. The reference and z_minus blocks are positive. This proves the fixed lower sign for t>0; physical continuity supplies its nonnegative t=0 limit. The auxiliary symmetric quartic threshold is not needed.

## 5. Nonzero charges: every block and the full low-charge raw table

### Extremal32 and higher64

On an extremal sector the exact operator is

    S=(l/4)F_A+(k/4)F_B-(L/8)F_AF_B.

The correction vanishes by §2's support statement. Joint swap eigenspaces have multiplicities9,3,3,1 and give the source's uniform symmetric gaps, hence the asymmetric lower sign too.

On the higher charge-one component the full form reduces to S=diag(1,s)/(4c), while C=(1/2)[[1,-1/2],[-1/2,1]]. I also checked this at its explicit highest-weight coordinate vectors from the raw T formula: the two diagonal contractions are1/(4c),s/(4c) and the cross term cancels. Covariance and the reducing-space proof exhaust that irrep. The minus diagonals are at least1/3 with off-diagonal-1/4, giving I/12; the plus is at least I/4. Reciprocity/group and physical-factor interchanges supply the other higher components with no loss of dimensions.

### Remaining low charge-one multiplicity8

For an external pair alpha=0 in A,beta in B, the eight coefficient matrices can be organized as

    x1=sum_b|0b><b beta|, x2=|0 beta><Omega_B|,
    y1=x2^T, y2=x1^T,
    u1=|Omega_A><0 beta|, u2=sum_a|0a><a beta|,
    v1=u2^T, v2=u1^T.

Substituting them into §2's T traces reconstructs the FULL cross block W in007, including all zeros:

    [-3t/(2b), -3t/(4b), t/c, t/(2c)],
    [0,0,t/(2c),t/(4c)],
    [9t/(4c),0,-3t/(2a),0],
    [0,0,-3t/(4a),0].

For example x1,u1 has the two BB contractions -t/4,-t/2 after weighting, summing-3t/(2b); x2,u2 cancels its two group-label terms; y1,v1 gives the AA terms-t/2,-t, hence-3t/(2a); y2,v2 cancels its two AA diagonal terms. The universal vector formula therefore determines the zero entries too, rather than their being inferred from a desired kernel.

The S_I table follows by using Gram G=[[2,1],[1,2]] on U1,U2: the forms of T,P1,K12,K21 yield respectively B2,(column(2,1) outer itself), and the corresponding cross outers. Their combination gives the displayed diagonal D2 and cross E2. I independently checked its rank-one entries (x2 diagonal1/(4c), y1 diagonal9s/(4c), x2-y1 zero) and its contraction entries (x1 diagonal1/(4c), y2 diagonal-3s/(4c), x1-y1=-3l/4). S_II follows from the exact group/physical permutation. The C form is G-B2/2=(3/2)I per orientation, with cross -3I/4. This reconstructs the low raw form before any positivity elimination.

The exact K=u1+t y1 kernel is therefore consistent with every row and follows independently from the reference identity. After removing it, the y1 pivot is9/(4c), followed by positive dy=(3+4s)/[2(1+s)] and du=(4+3s)/[2(1+s)]. I re-derived all four residual diagonals and six edges by these three scalar Schur eliminations. In particular the x1-v1 edge is t(c^2-ab)/(cab)=t(s-1)^2/(4cab), retaining the sign.

Multiplying the diagonal differences by their positive denominators gives exactly the polynomial numerators176+521s+578s^2+309s^3+72s^4 and45+144s+148s^2+49s^3+s^4; the stronger small-s numerator is33+104s+101s^2+26s^3-3s^4. The stated coefficient bounds for h14,h23 follow from -4ab(4+3s)+27(1+s)^3 and its3+4s partner. Thus on0<=s<=1 the row sums5/12,11/24,1/4,7/24 are strictly below the respective diagonal bounds1/2,1/2,1/2,1/3. Reciprocity handles s>1. This proves all seven upper remainder directions, with exactly one K kernel for each external pair.

I also reconstructed EVERY lower row-sum bound from the raw8x8 table. The tight v1 row is bounded by3+4/5+2/3=67/15, below9/2 by1/30; the other bounds are49/12,17/6,227/60,151/60,17/4,9/4,29/12 as listed. The inequality t/a<=16/45 follows from32t^2-45t+16>0 (negative discriminant). Hence the coefficient form is at least I/30. Its Gram is at most3I, giving the PHYSICAL lower bound I/90. This conversion does not assume the eight contraction vectors are orthonormal.

## 6. Main's final88: physical matrices and all-angle signs

### Spin two and product-adjoint

For spin-two A, the raw diagonal on|01,01> is L/8-r delta^2. Since r=1/[6(1-p)] and delta^2=(1-p)(1-9p)/4, it is exactly1/12. C is1/4. Covariance supplies the full5-dimensional irrep; B is reciprocal. Both signs are strict.

For the four product-adjoint coordinate vectors, I reconstructed the displayed C4 and S4 from §2. The P1-P2 D edge is-L/8, but its correction is+r delta^2, giving the CONSTANT-1/12; the P3-P4 edge remains-L/8 because its mixed-input correction is zero. The four remaining edges are u,u,v,v with u+v=1/6. On P3-P4, both symmetric signs are strict. The upper Schur subtraction on its complement is exactly17/16-6uv, leaving3/16+L/8+6uv>0. For the plus sign, sum/difference coupling diagonalization gives at most22/35 subtracted from a Z diagonal at least9/8, leaving139/280>0. Thus the entire36-dimensional sector is strictly symmetrically dominated.

### Full adjoint-A raw7 and exact2+5 split

Using P=|01><Omega_A|, Q=P^T and R=sum_a|0a><a1|, and the four B matrices from the main body, I reconstructed the three all-A entries, four mixed-pattern block and entire3x4 cross block including R-B4=0. Useful checks showing the full correction is retained are

    S(P,B2)=-t k(1+theta)=-t/c,
    S(Q,B1)=(t/b)(1-theta)=t/c,
    S(R,R)=-2r delta k=(k-1/c)/2,
    S(R,B2)=(t k/2)(1-theta)=t(k-1/(2c)).

The B1-B2 D edge is(3l-k)/4 and its correction-r delta(k+3l), giving1/2-1/c; B3-B4 is(3l-k)/4 without a mixed correction. The remaining cross edges follow from the same two-label sums; R-B3=-t/c and R-B4 cancels between the two A labels. These reproduce the entire physical form rather than the kernel alone.

The stated Gram makes U,V,W,Z_± orthonormal and B1,B2 norm squared2. Direct congruence yields the exact2+5 split. On2, the determinant lower bounds71/144 and2/9 follow from |t/(2c)|<=1/6 and S22 in[-3/8,1/8]. Both signs are strictly positive.

On5, I checked the complete-square decomposition of the(U,V,B2) form:

    j|t U-B2|^2+h|t V+B2|^2.

The B1 couplings are(-1,1)/(2c), and Z couplings(1/(2c),-1/c). Their Schur subtraction gives exactly the source R11,R12,R22 with D=b(4+5s). In particular3D(R11-5/3)=2+2s+5s^2 and the numerator for R22-3/4 is

    4+5s-2s^2+6s^3+5s^4
     =(s^2-1)^2+4s^4+6s^3+5s+3.

Thus R is positive definite with determinant>1/4. For t>0 the only upper zero is U-V+tB2; no division by t is needed for endpoint PSD.

Finally I multiplied the displayed inverse C5 against S5. Its relative trace is exactly

    [4+(11/2)k+(15/2)l+32/(3(1+s))]/9.

For s>=5, l>=5/7 gives131/126; for s<=5, k+l>=2/3 and the tail>=16/9 give85/81. The normalized upper difference D5 is PSD, so lambda_max(D5)<=Tr(D5)<=499/126. Hence4I-D5>=5I/126, proving strict3C5+S5 positivity. This generalized trace is congruence-invariant, so the nonorthogonal form basis introduces no missing Gram factor. Reciprocity closes adjoint B.

## 7. All t, exact kernel and actual arbitrary-rank-two consequence

The block accounting in §3 exhausts256 physical dimensions. For t>0, upper kernels total8 from low nonzero charges,2 fixed and6 from the two adjoint irreps, exactly16. All other upper blocks are strict. The directly proved identity places eta_input tensor H_output in the kernel already, so this16-dimensional subspace is EXACTLY the kernel; no uncounted zero mode remains.

Every lower block is strict for t>0, by the sector arguments above. At t=0 the physical reference inverse remains bounded/invertible and every matrix entry is continuous, so both nonstrict inequalities extend without applying a singular1/t basis change. The theorem intentionally adds no t=0 kernel classification. Scaling and local-unitary co-Choi covariance transport all finite ratios; exchanging A,B covers the zero-first-pair case too. This gives precisely Schmidt(a,a,b,b), not arbitrary Schmidt spectra.

For the first-site ray, the |00> direction, the2x2 spans{|0a>,|a0>}, and Q tensor Q exhaust the whole one-site co-Choi space. The2x2 generalized determinant is -(1/4)(1-lambda)(1+3lambda); on Q tensor Q, S0=F/2 and C0=I-F/2. Thus the full spectrum is{1,-1/3} for n>=2, with multiplicities n(n+1)/2,n(n-1)/2; n=1 has only1. There is no omitted one-site sector.

With T_B in[-3,1], each product of its eigenvalues with1 or-1/3 is at most1. Therefore I-T0 tensor T_B is PSD. Congruence yields positive reversed co-Choi matrix of the switched map, i.e. a completely copositive and hence positive map. Complete copositivity is a sufficient property, not asserted necessary for unrestricted W4.

To verify the raw coefficient-operator bridge independently, put Psi=Lambda1 tensor B and write ANY rank<=2 C whose range contains u=|0> tensor eta as

    C=|u><v|+|x><y|,

with x,v,y arbitrary complex vectors. Expansion of the eight local swaps gives A=Psi(|u><u|), D=Psi(|x><x|), L=Psi(|x><u|) and the cross term2Re<y,Lv>. Its orientation is important: it is L, not L†, there. Completing the square gives exactly

    ||A^(1/2)(v+A^-1 L†y)||^2
        +<y,(D-L A^-1 L†)y>.

The product reference makes A^-1 the FULL tensor product inverse and the second operator is the positive switched map applied to|x><x|. Thus both terms are nonnegative without factoring x or restricting v,y. Local-unitary CONJUGATION of C preserves every partial-trace HS norm and transports the range ray. Also q3(C†)=q3(C), so the adjoint co-range case follows without a partial-trace rank shortcut.

## 8. Final scope and handoff

No load-bearing imported body is missing for this A–B reconstruction: all six were read and their needed physical forms/positivity arguments traced above. Auxiliary symmetric-angle classifications and old uniform-point/source-priority claims were not used as premises.

**Exact checked conclusion:** full256-dimensional -3C_B<=S_eta<=C_B for every two-equal-pairs reference angle, nonstrict endpoint t=0; strict lower sign and exactly16-dimensional stated upper kernel only for t>0; the resulting rank<=2 arbitrary-complex range/co-range class for the stated reference rays. **Not checked/accepted:** unrestricted64x64 rank-two W4, a negative rank-two witness, all-copy bound entanglement, literature novelty or publication priority. Those are separate source/science gates.

This is ordinary in-harness written reconstruction with supplied author proofs and declared prior exposure. Parent must still compose its own full-body verdict. Review returns go to PhysicsResearch96h and Main; reviewer retains the ONE semigroup primary.
