# Additive written reconstruction for v29-C: R2 witness derivation and the exact remaining R1 gate

Owner MathKacMoody. Verbatim observed metadata clock before creation: **Sun Oct 25 04:39:46 PDT 2026** (`/bin/date`). All original packets and the actual reviewer return are preserved.

**WRITTEN ONLY.** No scientific eval, arithmetic interpreter, enumeration, symbolic program, Casimir application program, determinant replay or scientific process was used. The calculations below are displayed paper algebra. Earlier unadmitted owner calculations provide NO executable-verification or finite-certificate credit. Parent evidence erratum v7 and the owned admission qualification remain binding.

## 0. Exact response to the actual review

I read the complete251-line actual `peer-review-kac-level5-quotient-v1.md` in the Tuscan owner's root, including its closing raw lines. It correctly left two MAJOR acceptance obligations, not mathematical counterexamples. This supplement does NOT label the full invariant quotient settled at parent level.

- **R2:** §§2–7 below give a NEW complete written derivation of the OLD projected coefficients `3,3,158,-168,-87,245` and determinant996. Instead of applying a sixth-degree Casimir polynomial to thousands of tensor coefficients, I construct its unique lowest summand by elementary Clebsch equations, compute an exact finite-unitary norm, and read only the required words. This is a contraction/elimination proof, not another support-count table or computation-output boolean.
- **R1:** §8 proves a trace-completeness cut/join reduction eliminating all summed basis indices from every entry. Section9 works one coefficient fully. **The remaining numerical evaluation of all36 entries and the full six-by-six determinant identity are STILL NOT_RECONSTRUCTED here.** The reduction is not advertised as acceptance of those identities. The invariant/actual3-to5 conclusion therefore remains a candidate requiring that exact gate.

The old source geometry uses the reviewed free character/domain facts plus the R2 image witnesses. If the fresh reconstruction accepts §§2–7, those image witnesses and the affected exact entry-three source dimensions no longer depend on any historical Casimir interpreter output. This does not infer any of the seven full primitive lowering-map ranks.

## 1. Fixed interfaces and elementary notation

Use the same basis

    u0=E12, u1=E21, u2=E23, u3=E32,
    u4=E13, v=u5=E31, u6=H1, u7=H2,
    H1=diag(1,-1,0), H2=diag(0,1,-1).

These u labels are positive level-one vectors, not ambient Cartan elements. E1,E2,F1,F2 act by the finite Levi. Composition AB means that B acts FIRST. Put e=E1, f=E2, z=[e,f], and

    q=[v,[v,[v,u3]]].

The named structural input identifies its free simple module Q with L(5,2)=81, with q lowest of (h1,h2)-weight(-2,-5). The imported bracket map is the literal equivariant map

    phi: V tensor Q -> L5(V),    u tensor t -> [u,t].

The actual source ideals and isotypic arguments remain those in `level5-structural-interface-v1.md`, SHA256 `ef56a3c2406f80924ce7a1b5bb9e4ac904398088a1f06c4f68cb4833738bcc44`. The v29-C review already reconstructed the domain decomposition, the Casimir scalars60,54,48,40,36,30,24, and the old projector multipliers -135 and648. I use those explicit finite-Levi identities, not the unadmitted coefficient data.

For a lowest t of weight(-m,-n), direct commutation gives

    F1(e^i z^j f^k t)
      =i(m-j+k-i+1)e^(i-1) z^j f^k t
          +j e^i z^(j-1) f^(k+1)t,

    F2(e^i z^j f^k t)
      =-j e^(i+1) z^(j-1) f^k t
          +k(n-k+1)e^i z^j f^(k-1)t.                 (1.1)

Here [F1,z]=f and [F2,z]=-e; z commutes with e,f. These formulas, with m=2,n=5, are all the Clebsch/norm algebra required below.

## 2. The unique 64-lowest domain vector, explicitly

Define T64 in V tensor Q by replacing every bracket in the following expression by a tensor product:

    C64=160[u2,q]-8[u3,f^2q]
       +24[u1,efq]-20[u1,feq]
       -5[v,ef^2q]+4[v,fefq]+32[u7,fq].               (2.1)

Thus C64=phi(T64). The finite matrix lowerings are

    F1u3=-v, F1u1=F1u2=F1v=0, F1u7=-u1,
    F2u2=-u7, F2u1=v, F2u3=F2v=0, F2u7=2u3.

Using (1.1), F1T64 has coefficient groups

    8-20+12=0,    72-40-32=0,

and F2T64 has groups

    -160+160=0, -64+64=0, 24-40+16=0,
    -20+20=0, 120-120=0.

These correspond respectively to v tensor f^2q and u1 tensor fq for F1; and u7 tensor q, u3 tensor fq, v tensor efq, v tensor feq, u1 tensor eq for F2. This verifies lowestness without any spectral program. Its full degree is(2,2,5), lowest weight(-3,-3), so it is a64 vector. The domain decomposition contains this type ONCE.

## 3. The unique 35-lowest domain vector, explicitly

The following table defines T35 as the sum of coefficient times its tensor factor pair. Set C35=phi(T35).

|first factor|second factor|coefficient|
|---|---|---:|
|u4|q|560|
|u0|fq|112|
|u2|eq|-280|
|u6|efq|14|
|u6|zq|70|
|u7|efq|-35|
|u7|zq|105|
|u1|e^2fq|-7|
|u1|ezq|-35|
|u3|ef^2q|7|
|u3|zfq|-28|
|v|e^2f^2q|1|
|v|ezfq|1|
|v|z^2q|-15|

For clarity label these fourteen coefficients A through N in table order. Formula(1.1) plus the matrix lowerings makes F1T35=0 equivalent to the eight literal equations

    A+2C=0, -B+3D+E=0, 3F+G=0,
    2D-F+4H+I=0, 2E-G+I=0,
    -J+6L+M=0, -K+2M+2N=0, 4J+K=0.

F2T35=0 is equivalent to

    -A+5B=0, -C+5F-G=0, 5D-E=0,
    -D+2F+8J-K=0, -E+2G+5K=0,
    H+8L-M=0, I+5M-2N=0, 5H-I=0.

Substitution gives zero in each equation. Thus T35 is lowest at full degree(3,2,5), of type35=L(4,1). This type also occurs ONCE in V tensor Q. This fourteen-term linear elimination is the promised constructive replacement for applying the Casimir polynomial directly.

## 4. Exact projection constants from invariant Hermitian norms

Take the compact finite-Levi Hermitian form, with E_i adjoint to F_i, normalize ||q||=1, and use Tr(A^* B) on V. Root matrix units have norm1; on (u6,u7) the Gram matrix is [[2,-1],[-1,2]]. The finite Casimir is self-adjoint. Its spectral projectors are therefore the orthogonal projectors, even though the algebraic proof is over C.

The relevant elementary q norms/Grams are:

    ||fq||^2=5, ||f^2q||^2=40, ||eq||^2=2;

    Gram(efq,feq) = [[15,10],[10,12]],
    Gram(efq,zq)  = [[15,5],[5,7]],
    Gram(ef^2q,fefq) = [[160,120],[120,110]],
    Gram(e^2fq,ezq) = [[60,20],[20,12]],
    Gram(ef^2q,zfq) = [[160,40],[40,30]],

    Gram(e^2f^2q,ezfq,z^2q)
       = [[960,240,80],[240,100,60],[80,60,84]].        (4.1)

Each entry is obtained by moving one raising operator across the inner product and applying(1.1). For example ||efq||^2=3||fq||^2=15; <efq,feq>=2||fq||^2=10; <ef^2q,fefq>=3||f^2q||^2=120. Also zq has norm7 and z^2q norm2*7*6=84, since q is lowest of h1+h2-weight-7. For the final Gram matrix, F1(ezfq)=2zfq+ef^2q and F1(z^2q)=2zfq give the off-diagonal entries240,80,60. Thus (4.1) is reconstructible by the displayed lowering rules, not a list imported from execution.

Grouping T64 by its orthogonal first-factor spaces gives contributions

    25600, 2560, 3840, 960, 10240,

whose sum is43200. For example the u1 block is

    24^2*15+20^2*12-2*24*20*10=3840,

and the v block is25*160+16*110-40*120=960. The H2 block is32^2*2*5=10240. Since <T64,u2 tensor q>=160,

    P64(u2 tensor q)=T64/270.                         (4.2)

For T35 the contributions from u4,u0,u2, the Cartan pair, u1,u3,v are respectively

    313600,62720,156800,133280,27440,15680,16240,

summing to725760. The Cartan contribution is explicit: for X=14efq+70zq and Y=-35efq+105zq, one has ||X||^2=47040, ||Y||^2=58800 and <X,Y>=39200, so the first-factor Gram contributes2*47040+2*58800-2*39200=133280. The final v contribution is

    960+100+225*84+2*240-30*80-30*60=16240.

Since <T35,u4 tensor q>=560,

    P35(u4 tensor q)=T35/1296.                        (4.3)

There is no assumption about injectivity of phi in(4.2),(4.3). They are domain projections; the actual nonzero bracket-image witnesses are derived next.

The old Casimir definitions are -135 times the64 projector and648 times the35 projector. Equivariance of phi and(4.2),(4.3) therefore prove EXACTLY

    U64plus = -C64/2,       U35plus=C35/2.             (4.4)

This derives the old projected-vector normalizations without expanding a sixth-degree operator on a6552-dimensional space.

## 5. Hand tensor coefficients for BOTH 64 images

For this section write a=u3, b=u1, c=u0, d=u2 and h=u7. The needed single-letter raising rules are

    ev=-a, fv=b, ea=0, fa=h, eh=c,
    fh=-2d, eb=u6, f(u6)=d.

In particular ef a=c (the plus sign matters), fef v=d, and ef^2 v=0. Expand

    q=v^3 a-3v^2 a v+3v a v^2-a v^3.                 (5.1)

For a tensor word ending in v and starting in c or d, the ONLY contributing summands of C64 are its direct160[u2,q] term when the initial letter is d, and the right ends of the two outer-v brackets. Thus the coefficient is

    direct +5*[prefix](ef^2q)-4*[prefix](fefq),

where prefix deletes the final v. The complete needed reductions are:

|word in C64|direct|prefix coefficient in ef^2q|prefix coefficient in fefq|result|
|---|---:|---:|---:|---:|
|c b v v v|0|-2|-1|-6|
|c v b v v|0|-2|-1|-6|
|d a v v v|-160|-2|1|-174|
|d v a v v|480|-2|-5|490|

Here is the finite derivation behind the table. For the first two rows, the original a must become c by one e and one f, and one original v becomes b by f. The two possible f placements give factor2 for ef^2, and factor1 for fef; the coefficient of the original a v v v is-1, giving-2,-1. For the last two rows, either one original v becomes d by fef (coefficient1, whereas ef^2v=0), or a becomes d by f^2a=-2d while another v becomes a by ev=-a. The latter transfer has coefficient2. Inserting the q coefficients-1,3,-3 from(5.1) gives respectively(-2,1) and(-2,-5). There are no other transfers with the required letter weights. This proves all four rows, rather than inferring them from a printed coefficient list.

The diagram automorphism sigma=-J transpose J^-1 sends c->-d, b->-a and v->-v. Hence a five-letter root-only word receives sign-1. On the first two table words, sigma(C64) has coefficients174 and-490. Equation(4.4) now gives the OLD literal two-column matrix

    coefficients of (U64plus,sigma(U64plus))
    at (c b v^3, c v b v^2):

             [ 3   -87 ]
             [ 3   245 ].                             (5.2)

Its determinant is3*245-3*(-87)=996 !=0. Both projected64 bracket images are nonzero and independent. This proves the needed image rank directly in the FREE source; finite semisimplicity then gives the stated actual selected-image subtraction at entry three. No original D3 rank is inferred from it.

## 6. Hand tensor coefficients for the projected35 image

Read the two OLD words c b a v v and c b v a v. Among the fourteen summands of C35, only112[u0,fq] on the left and the three outer-v terms on the right can contribute. The direct112 term contributes336 and-336, since the required fq words come from q coefficients3 and-3 in(5.1).

For the right-v terms use

    Q0=e^2f^2q, Q1=ezfq, Q2=z^2q.

At the respective four-letter prefixes the required coefficients are

|prefix|Q0|Q1|Q2|
|---|---:|---:|---:|
|c b a v|16|4|0|
|c b v a|0|0|0|

To derive this short table, there are only TWO possible letter-weight transfers from v^3a:

I. original a becomes c by(1,1), one v becomes b by(0,1), another v becomes a by(1,0);
II. original a stays a, one v becomes c by(2,1), another v becomes b by(0,1).

For each fixed assignment, the transfer coefficients are-4 for e^2f^2, -1 for ezf and0 for z^2. Indeed in I the two f choices and two e choices give2*2*(-1)=-4; z acts on a to give c, while e acts on the v destined for a, giving-1. In II, e^2fv=-2c and the f split gives factor2, again-4; ezv=-c gives-1. A z-only transfer cannot produce either required (1,0) or(0,1) change, hence zero for z^2.

For prefix c b a v, the original words in I and II are a v v v and v v a v, whose q coefficients are-1,-3. Their contributions are therefore4+12=16 and1+3=4. For c b v a the original coefficients are-1,+1, which cancel. This derives every entry of the table without a large expansion.

The outer-v coefficients in T35 are1,1,-15, with a minus sign from their right ends. Consequently C35 has coefficients

    336-16-4=316,       -336-0-0=-336.

Equation(4.4) proves that the OLD projected U35plus has coefficients158,-168, exactly as advertised. Its bracket image is therefore nonzero. Diagram exchange gives the nonzero35* image.

## 7. R2 disposition at its exact mathematical boundary

The old projected values3,3,158,-168,-87,245 have now each been derived by a displayed finite-Levi elimination, exact invariant-domain norm and elementary word transfer. The two64 images are independently nonzero and their independentness is proved by(5.2), not guessed from two nonzero projections.

Combined with the domain multiplicity-one and free/actual isotypic facts independently reconstructed by v29-C, this proves the exact selected entry-three source dimensions claimed in the original geometry packet. It still proves NO full original lowering-map rank for any of the seven nontrivial types. The separate two-line64 original-lowering packet retains its own fresh-review gate.

A fresh reviewer should specifically reconstruct the norm Grams, the signs eh=+c and ev=-a, the projection multipliers, and the transfer tables. This author supplement is not parent acceptance. The old computed support sizes217,378 are NOT needed and are not newly certified here.

## 8. R1: trace-completeness contraction eliminates the 8^5 sums

Let b_i be the unscaled basis, d^i its trace-dual, and use

    sum_i d^i M b_i=Tr(M) I-M/3,
    sum_i d^i Tr(M b_i)=M-Tr(M)I/3.                   (8.1)

These follow from the full matrix-unit completeness relation after subtracting the scalar line. All source c_i equal3d^i, so the five source slots contribute the common factor3^5=243.

In a lowering pair the deleted original variable is b_p, the acted-on original variable is b_q, and the selected output coefficient is read by a traceless trace-dual Z. Let x=E13. The local pair coefficient is

    a Tr(Z[[x,b_p],b_q])
     +b Tr(Z[xb_p+b_p x,b_q])
     -c Tr(xb_p)Tr(Z b_q),                            (8.2)

with a=(r+s)/2,b=(r-s)/2,c=2-r-s. Here a,b,c are SCALARS, unrelated to the root-letter abbreviations in §§5–6.

### 8.1 Both contracted slots in one trace cycle

Rotate that source cycle to Tr(d^p A d^q B), with A,B the ordered products of its remaining fixed dual matrices (possibly the empty product I). Multiply by any unaffected source-cycle traces. Applying(8.1) first to q and then to p gives the following EXACT pair contractions:

    K_a(A,B,Z,x)
      =Tr(AZx)Tr(B)-Tr(AZ)Tr(xB)
         -Tr(Ax)Tr(ZB)+Tr(A)Tr(xZB),

    K_b(A,B,Z,x)
      =Tr(AZx)Tr(B)+Tr(AZ)Tr(xB)
         -Tr(Ax)Tr(ZB)-Tr(A)Tr(xZB)
         +(2/3)Tr(A[x,Z]B),

    K_c(A,B,Z,x)=-Tr(xAZB).                           (8.3)

For example the a contraction is sum_p Tr(d^p A[Z,[x,b_p]]B). Its four expanded terms have respectively the products Tr(AZx)TrB, -Tr(AZ)Tr(xB), -Tr(Ax)Tr(ZB), TrA Tr(xZB); their four one-third correction traces cancel exactly. For b, the changed signs leave precisely the displayed rank-two trace correction. For c, direct duality gives -Tr(xAZB). Thus no summed Lie-basis index remains in(8.3).

### 8.2 The two slots in different trace cycles

For source factors Tr(d^p A)Tr(d^q B), the pair contractions are instead

    J_a=Tr(B[Z,[x,A]]),
    J_b=Tr(B[Z,xA+Ax])-(2/3)Tr(A)Tr(B[Z,x]),
    J_c=-Tr(xA)Tr(ZB).                                (8.4)

The subtraction in J_b is essential: duality replaces A by A-Tr(A)I/3. Again multiply unaffected cycles. Equations(8.3),(8.4) cover both the single-trace sources and both pair-times-triple sources, including the cases with two slots in the same short trace.

### 8.3 Completely specified finite sum for each R1 entry

For the right-normed bracket on slots0,...,4, its sixteen tensor permutations are indexed by R subset{0,1,2,3}:

    pi_R=(indices outside R in increasing order,
          4, indices in R in decreasing order),
    sign=(-1)^|R|.

For a target word w=(w0,w1,w2,w3), and an ordered lowering pair i<j in{0,...,4}, insert abstract contracted variables P,Q at slots i,j. Put Z=d^(w_(j-1)); fill each other slot k by d^(w_k) if k<i and d^(w_(k-1)) if k>i. For a single-trace source order sigma, take the trace cycle whose slot order is pi_R^-1(sigma). For a product-trace source apply pi_R^-1 to BOTH declared cycles. Rotate the P cycle as needed, use(8.3) when P,Q share a cycle and(8.4) otherwise.

Then, for each of the three scalar coefficients, the detector entry is EXACTLY

    (243/N_source) * sum_(i<j) sum_R (-1)^|R| K_or_J,   (8.5)

where N_source is -27,27,-27,81,-81,-27 for the six sources. All remaining operations are traces of explicit products of at most five3x3 rational matrices. Formula(8.5) replaces the 8^5 sum by at most160 elementary cut/join terms and makes every convention, normalization and permutation explicit. It is a derived contraction formula, not an appeal to an executed checker.

## 9. One R1 entry worked through, and the honest remaining gate

As a check of the reduction, take source1 and target word(0,0,1,2), and read its c coefficient. Only the deleted positive label v pairs with x=E13. On the relevant generator multiset the single trace has value1 precisely on the five cyclic rotations of input sequence(1,0,5,2,0), with common scale243. This follows directly from multiplying its matrix-unit trace cycle; no other order closes the same directed edges.

On a right-normed five-letter word containing v once at position k, the pure central derivative has factor -(4-k)c when k=0,1,2,3, and +c when k=4. The five rotations therefore give

    c[-2 R(1,0,2,0)-3 R(0,2,0,1)
          -3 R(2,0,1,0)-R(0,1,0,2)],

where R now denotes the right-normed FOUR-letter bracket. At target word(0,0,1,2), these four coefficients are respectively0,-1,+1,0. Their weighted sum is0. Dividing by N_source=-27 leaves zero, reconstructing the advertised c entry in M11.

This sample does NOT close the rest of R1. The exact remaining obligations are:

1. Evaluate(8.5), with its product-trace branch where applicable, to derive the COMPLETE36 advertised triples. Only the central coefficient of M11 is fully worked here; no other numerical triple is declared newly verified by this supplement.
2. Once the complete matrix is derived, give a written elimination/factorization or complete coefficient calculation for det M=-43740 P(r-1,s-1). Positivity of the copied triangle and the old unadmitted determinant output do not prove that identity.

Accordingly the full invariant source-basis claim, full invariant injectivity and actual3-to5 quotient verdict remain **NOT_RECONSTRUCTED at the parent acceptance gate R1**. This packet genuinely removes the huge summations as a representation obstacle and supplies the complete written R2 witness proof, but does not hide an unfinished numerical contraction/determinant derivation under a new theorem label. No general F5, H13 authentication, formal/kernel or novelty claim follows. No scientific replay is requested or authorized by this written supplement.
