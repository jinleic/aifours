# Independent written reconstruction: NL242 joint signed-support profile

Clock actually observed before creation: **2026-10-23T15:29:14-07:00**. Reviewer MathResearch96h, primary slot math-1 (repeated-pole PH). Temporary parent-assigned mathematical review, not a new problem owner. Review-start clock actually observed: **2026-10-23T15:25:35-07:00**.

Exposure: supplied author proof, intended conclusions and parent steering were read before this reconstruction. This is a different in-harness worker's explicit hand reconstruction, not blind, human, cross-vendor, kernel or novelty acceptance. No scientific program, Walsh enumeration/replay, solver, mathematical code, compilation, tests, model CLI or nested agent was used. Only reads, metadata checksums, clock observations and written reasoning were performed.

## 1. Actual pins, complete read scope and verdict

Read all278 lines of the author source and all7 lines of its operative erratum. Observed source SHA256 values match the assigned pins:

| Source | SHA256 |
|---|---|
| `information-science/evidence/three-area-20261023-96h/parallel-18/balanced-nl242/joint-profile-realizability-v1.md` | `5bbe53363d8a485d3cd9b4f3840d8691433e8cd1aef414eb9902b86f0ea32822` |
| Same root, `joint-profile-realizability-erratum-v1.md` | `28fad30f9393ba907c8ef24f002d0990221aa958eb9a0e87502c19e4168fbd47` |
| `information-science/evidence/hard-continuation-20261015/proof.md` | `d2c1605d8ee20423e137066b62b3dac31406bd4380d075c1b85064c01cf6dff9` |
| `information-science/evidence/hard-continuation-20261015/quadratic-distance/remaining-types/results/explore.json.gz` | `1e1470a7d5380bb61ac5ebb95221f531c44fdd67f53a3463fe7e4fc3c98d5136` |
| Same remaining-types root, `result.json` | `5548853b6be9c2af0d251afe2ca4101c4b70437fdda19e1d5c21977e4aa16d2c` |

For the historical proof, read the actual definitions/half interface and complete Sections2 and4 needed here (lines7–42,70–88); the finite exclusion/checker claims elsewhere were not adopted. Read the actual compressed `explore.json` member, including its literal `(8,136)` vector, and the actual receipt's seven-type list and scalar-witness statistics, especially lines147–153. These artifacts were read, not rerun. Their producer/audit status labels are not mathematical premises substituting for Boolean realizability.

**Verdict: 0 FATAL / 0 MAJOR / 0 substantive MINOR at the requested scope.** The signed-eight-point bound224 covers every affine dimension3–7 and every sign choice; the archived literal profile forces236 under the actual canonical Boolean interface; the full-rank L=8 boundary deductions reconstruct. The erratum is mandatory: **seven total types remain**, including the two full-rank types, not two plus seven.

This review supports exclusion of that one archived profile from every **genuine canonical Boolean** spatial realization and the displayed necessary boundary conditions. It does not exclude all integer arrangements of a count table, an entire residue type, balanced242 functions, or the full book question. Parent disposition remains separate.

## 2. Actual canonical Boolean interface, independently checked

Let H be the unnormalized Walsh matrix on V=F2^8. Character orthogonality gives H^2=256I and H^T=H. For an odd-weight Boolean h of weight w, put I(a)=sum_(x in supp h)(a.x mod2), an ordinary integer. Then

    W_h(a)/2=128*1_(a=0)-w+2I(a).

For odd t, (t^2-1)/8 modulo2 depends only on t modulo8. Expanding therefore gives the actual quadratic residue

    J_h=(W_h^2-4)/32
       =(w^2-1)/8+binom(I,2)+((1-w)/2)I mod2.

Here binom(I,2) modulo2 is the sum of the products of all unordered pairs of the Boolean linear forms a.x, so J_h has degree at most2. This is the source's precise odd-spectrum hypothesis, not an arbitrary-array property.

Let s be the XOR of supp h and epsilon=(-1)^((w+1)/2). Since I(a) mod2=a.s, the displayed expansion modulo4 gives

    W_h(a)/2=epsilon*(-1)^(a.s) mod4.

The canonical signed magnitude K, uniquely chosen to be2 modulo8, consequently satisfies

    K(a)=epsilon*(-1)^(a.s) W_h(a),
    (H K)(x)=epsilon*256*(-1)^h(x+s).

Thus **H K is pointwise +/-256**. Conversely, if an integer K has H K pointwise +/-256, then (H K)/256 is a Boolean sign table and its Walsh transform is K. The proof does not assume this pointwise identity for a scalar-feasible profile. A magnitude cap or Parseval equality alone does not establish it.

For two genuine canonical spectra write K_g=2+8t_g, K_h=2+8t_h. Their square residues equal t_g,t_h modulo2. Hence

    D=(K_g-K_h)/8 mod2=J_g+J_h

is quadratic. Also S=K_g+K_h satisfies S=4+8D modulo16. Under the cap28, R=K_g-K_h has values0,+/-8,+/-16,+/-24; T=(-1)^D S has exactly the four permitted values -28,-12,4,20. For those T values the source's signed delta gives S=-chi+delta modulo3, checked individually: only T=-12 and4 require a correction.

If D has nonsingular polar form, its Walsh magnitude is16. One can check the classical fact directly: expanding |H chi(x)|^2 by the difference t leaves an inner character sum over the polar form; nonsingularity kills every t except0, leaving256. Since the transform is real, H chi=16Q with Q pointwise +/-1. This discharges the actual full-rank interface without importing a classification of all seven global types.

## 3. Literal archived vector and every necessary statistic

The14 source rows agree exactly with the actual `scalar_witnesses["(8, 136)"]["counts"]` member. The following hand reduction also binds the signs and the defect support. The delta column is per position; multiplicity is in the count column.

| K_g | K_h | count | R | T | delta |
|---:|---:|---:|---:|---:|---:|
|2|18|2|-16|20|0|
|2|-22|22|24|20|0|
|2|26|44|-24|-28|0|
|-6|18|1|-24|-12|-1|
|-6|-22|22|16|-28|0|
|10|10|18|0|20|0|
|10|18|1|-8|-28|0|
|-14|2|6|-16|-12|1|
|-14|10|1|-24|4|1|
|-14|-14|52|0|-28|0|
|18|10|1|8|-28|0|
|-22|2|19|-24|20|0|
|-22|-6|20|-16|-28|0|
|26|2|47|24|-28|0|

The counts sum256. Thus delta has exactly8 support points (seven positive and one negative in this particular vector); no placement is assumed. Counting magnitudes in the combined S/R multiset gives

    (N0,N4,N8,N12,N16,N20,N24,N28)
      =(70,1,2,7,50,61,134,187).

Their sum512 is appropriate: each position contributes |S| and |R|. The R magnitudes have counts70,2,50,134 at0,8,16,24. Therefore

    wt(D)=2+134=136,
    sum R^2=2*64+50*256+134*576=90112,
    sum S^2=1*16+7*144+61*400+187*784=172032,
    Gamma=sum T=-28*187-12*7+4+20*61=-4096.

The two energy sums add262144. These hand-derived values agree with the actual archived receipt z=70,c=2,a=L=8,w_R=88,Gamma=-4096. No assumption that the stored vector is already Boolean was made.

## 4. Why genuine complementary transforms force m=236

For genuine canonical Boolean pairs, H K_g and H K_h are each +/-256. Their sum H S and difference H R therefore have complementary supports and their nonzero values are +/-512. If B=(H S)/512, then B is0,+/-1 and the number w_R of its zero entries is

    w_R=|supp(H R)|=sum R^2/1024=88,

by the exact Walsh Parseval normalization256.

Set b=phi(H delta), m=wt(b), Q=(H chi)/16. Since512=-1 and16=1 modulo3, the transformed congruence S=-chi+delta gives

    B=phi(Q-H delta)=phi(Q-b).

The six possibilities Q=+/-1,b=0,+/-1 give exactly:

- b=0: B=Q;
- b=Q: B=0;
- b=-Q: B=-Q.

Equivalently B=Q(1-3b^2/2)+b/2. Exactly w_R points have b=Q. Hence

    sum Q B=(256-m)-(m-w_R)=256+w_R-2m.

Character orthogonality and the symmetric Walsh matrix also give

    Gamma=<chi,S>=<H chi,H S>/256=32 sum Q B.

Thus m=(256+w_R-Gamma/32)/2=(256+88+128)/2=236. Every equality needs the actual pointwise Boolean transforms, not just scalar Parseval. The spatial assignment and the quadratic sign Q remain arbitrary throughout.

## 5. Signed-eight-point theorem: all affine dimensions and signs

Let delta take +/-1 on exactly8 distinct support points and0 elsewhere. If its affine span has dimension d, then3<=d<=7. Translating the support only multiplies H delta by a sign character and cannot change its zeros modulo3. Each character restricted to the d-dimensional direction space occurs2^(8-d) times, so2^(8-d) divides m.

Also, exactly modulo3,

    m=sum_x(H delta(x))^2=256*sum_u delta(u)^2=256*8=2 mod3.

This is a congruence, not an integer equality m=2048. For d=3 or4, m is a multiple16. The possible such values satisfying the congruence and0<=m<=256 are32,80,128,176,224; the stronger d=3 divisibility only restricts this set. In particular every low-dimensional/sign case has m<=224 and no value strictly between200 and224.

For d=5,6,7, use the actual augmented affine map with columns (1,u_i). Its rank is d+1, so its relation code C has dimension7-d. Each relation has even weight. A relation of weight2 would equate two distinct support points and is forbidden, leaving nonzero weights4,6,8 only. If epsilon_i are the support signs, e_P=product epsilon_i over P is a character of C.

### Exact zero-count normalization

Write epsilon_i=(-1)^a_i. The negative-sign phase vectors of the signed evaluations, including a global sign t, form the coset

    a+{(t+x.u_i)_i:x in F2^8,t in F2}=a+C^perp.

Its dimension is d+1 and each phase vector has2^(8-d) preimages among the512 pairs(x,t). At phase weight j the signed sum is8-2j, divisible by3 exactly for j=1,4,7. The coset indicator is

    |C|^(-1) sum_(P in C) e_P (-1)^(P.phase).

Summing over those weights gives K1(wt P)+K4(wt P)+K7(wt P)=F(wt P), with K_j(w)=[z^j](1-z)^w(1+z)^(8-w). To convert phase-vector counts to the256 original x, the factor is

    (1/2)*2^(8-d)/|C|=1,

since |C|=2^(7-d). The division by2 is legitimate because changing global sign preserves divisibility by3. Therefore the exact ambient zero count is

    86+sum_(P!=0) e_P F(wt P),
    m=170-sum_(P!=0) e_P F(wt P).

No missing power of2 remains.

### Every binomial value and table

At weight0 the three K values are8,70,8, summing86. At weight4 the polynomial is(1-z^2)^4 and the values are0,6,0. At weight6, (1-z)^6(1+z)^2 gives -4,-10,-4. At weight8 they are -8,70,-8. Thus F(4)=6,F(6)=-18,F(8)=54, exactly as stated.

For d=7, C=0 and m=170 independently of all signs.

For d=6 there is exactly one nonzero relation. The two character signs exhaust its possibilities:

| relation weight | e=+1 | e=-1 |
|---:|---:|---:|
|4|164|176|
|6|188|152|
|8|116|224|

For d=5, the three nonzero relations satisfy P3=P1+P2 and e1 e2 e3=1. Each coordinate belongs to either0 or2 of those words, so their weight sum is at most16. Combining this with even weights at least4 leaves precisely the four candidate triples below. The four character signs give:

| weights | +++ | +-- | -+- | --+ |
|---|---:|---:|---:|---:|
|4,4,4|152|176|176|176|
|4,4,6|176|152|152|200|
|4,4,8|104|224|224|128|
|4,6,6|200|128|176|176|

Each entry is170 minus the signed sum of the three displayed F values. For example(4,4,8) with+-- gives170-(6-6-54)=224; (4,6,6) with+-- gives170-(6+18+18)=128. No sign character or affine dimension is omitted. Every high-dimensional value is at most224, and the tables also establish that m>200 forces m=224.

### Sharpness, without a Boolean-witness claim

For a linear three-flat U, delta=1_U-2*1_{0} has8 support points, one negative sign and seven positive. Its transform is8*1_(U^perp)-2, equal6 on32 points and-2 on224 points. Thus its mod3 support has exactly224 points. This proves sharpness symbolically; it does not construct a compatible canonical S/R pair or a balanced242 function.

Combining this all-support theorem with Section4's forced236 excludes the exact archived vector for every genuine spatial realization.

## 6. Entire full-rank L=8 boundary, independently reconstructed

Here N_j counts occurrences in the S/R magnitude multiset. Only R contributes to N0,N8,N16,N24; only S contributes to the odd multiples4,12,20,28. Put u=N0+2N8 and let d=wt(D)=N8+N24. The R magnitude counts immediately give

    sum R^2=64N8+256(256-d-N0)+576(d-N8)
           =65536+320d-256u,
    w_R=64+(5/16)d-u/4.

For T=-28,-12,4,20, the value T^2+8T is560 except at the L defect positions, where it is48. Hence

    sum S^2+8Gamma=560*256-512L.

The canonical Boolean Parseval identities give sum(S^2+R^2)=262144. Substitution therefore yields

    Gamma=40d-6656-64L-32u,
    m=264-(15/32)d+(3/8)u+L.

At L=8,d=120, this is m=215.75+3u/8>=216 after integrality. At d=136 it is m=208.25+3u/8>=209. Since u>=0, both cases have m>200; the full signed-support proof above forces m=224, not merely m<=224.

Solving the displayed affine equations gives exactly

- d=120: u=22;
- d=136: u=42.

For either case, w_R=96 and Gamma=-3072. Independently, m=224,w_R=96 gives sum Q B=256+96-448=-96 and therefore Gamma=32*(-96)=-3072. The archived vector has u=70+2*2=74, so it violates the full-rank L=8 boundary as well as the direct236-versus224 contradiction.

These are **necessary joint Boolean-realizability constraints**, not existence of the boundary count values, an exclusion of all L=8 profiles, or a type closure.

## 7. Findings and return boundary

- **FATAL / MAJOR / substantive MINOR:** none found within the stated mathematical scopes, reading the source together with its operative erratum.
- **Reconstructed:** actual canonical odd-spectrum/Boolean/quadratic interfaces; every literal profile statistic; complementary transforms and forced236; all affine dimensions/sign characters of the signed-eight-point bound; exact phase/Krawtchouk normalization; sharpness control; full-rank L=8 values224/96/-3072 and u22/42.
- **Historical boundaries:** the archived receipt's PASS label and the older finite exclusions were not replayed. The source's Section7 references to earlier L2 exclusions and its residual profile bookkeeping retain their own historical gates; they are not premises of the new contradiction. Seven total entire types remain unexcluded by this packet. No further global classification is imported.
- **Not established:** balanced242 existence/nonexistence, exclusion of either complete full-rank type, attainability of the constrained counts, worldwide novelty, formal proof, human or cross-vendor review.

The assigned bounded reconstruction is complete. PH remains the reviewer's sole primary problem. Its actual supported minimum7 band and the separate still-unreviewed PH8/PH9 candidates are unchanged; no new upper certificate or execution was undertaken during this assignment.
