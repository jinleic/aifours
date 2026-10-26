# Candidate: the rank-two balanced branch requires L in {16,20,24,28}

Owner: InfoBalancedNL242, info-6. Clock observed immediately before creation: 2026-10-24T03:48:07-07:00. Written mathematics only; no executable Walsh check, enumeration, solver, compilation, native program, old runtime, or independent-model CLI. This is ONE consolidated mechanism packet, not a series of per-defect claims.

## 1. Literal statement, dependency, and scope

Use the unnormalized Walsh matrix H on F_2^8, so H^2=256I. Let K_1,K_2 be actual Walsh spectra of eight-variable Boolean signs: HK_i takes values in {−256,256}. Suppose

- K_1(a)=K_2(a)=2 modulo 8 for every a;
- |K_1(a)|+|K_2(a)| <= 28 for every a;
- S=K_1+K_2, R=K_1−K_2, and D=R/8 modulo 2 is quadratic of polar rank 2 and weight 192;
- R has at least one zero.

Define L=#{a: |S(a)| is 4 or 12}. The candidate conclusion is

**L belongs to {16,20,24,28}, and the L distinct defect points affinely span all of F_2^8.**

In particular, every balanced nine-variable Boolean function with nonlinearity at least 242 in the intrinsic residue branch (polar rank 2, weight 192) has these necessary properties, using the unrestricted split in the frozen v1 packet. No half of its table is fixed. L counts ALL 512 coefficients of magnitude 4 or 12: the 256 R-sector coefficients have magnitudes divisible by 8 and contribute none.

The explicit foundation is `rank2-dual-support-obstruction-v1.md`, SHA-256 `7b230dbbb6da5f457f78179dea5ecfd79c892c2b9c7878f4fcfea5dbb2737958`. Its assigned PhysicsPPT44 reconstruction continues. Its canonical normalization, balance bridge, Gamma identity, occupancy identity, m identity, four-point signature, and L=0/4/8 dispositions remain frozen review inputs. Any reported v1 defect is live for this chain and must be resolved, not dismissed as superseded. The spatial route below independently obtains the lower floor L>=12 without using the signed-eight-point tables, but it does NOT bypass the shared v1 foundations or their actual review gate.

This packet adds the exact C/P identity, a proper-affine-span obstruction, a complete written L=12 relation-code classification, the upper bound L<=28, and the four-value residual frontier. It does not exclude the entire rank-two type, any other entire type, or unrestricted balanced NL242. It is CANDIDATE pending actual separate reconstruction. No novelty or formal/kernel claim is made.

## 2. Foundational identities and the nonfull quadratic dual

Write chi=(-1)^D, d=wt(D)=192, z=#{R=0}, c=#{|R|=8}, and u=z+2c. All these refer to actual arrays, not an archived multiplicity relaxation. Put Gamma=sum_a chi(a)S(a).

The shared v1 identities are

    w_R = #{x: HR(x) != 0} = 124−u/4,
    w_S = #{x: HS(x) != 0} = 132+u/4,
    Gamma = 1024−64L−32u.                              (1)

Here HS and HR have complementary supports and values 0 or ±512. The identity for w_R follows by summing R^2, using R in {0,±8,±16,±24}; the Gamma identity follows from

    (chi S)^2 + 8 chi S = 560−512·1_A,

where A is the defect set. The full Boolean pair gives sum(S^2+R^2)=262144.

A zero R(a_0)=0 gives

    0 = (1/256) sum_x HR(x)(−1)^(a_0·x)
      = 2 sum_{x:HR(x)!=0} (HR(x)/512)(−1)^(a_0·x).

Consequently w_R is even, u is a multiple of 8, and, because z>=1, **u>=8**.

Let W_D=Hchi. Its support U has exactly four points and its nonzero values are ±128. Define

    q = phi(W_D) = −W_D/128,

where phi maps each integer modulo 3 to {−1,0,1}. In particular q is ZERO at the other 252 points. No full-rank sign vector is substituted here.

Set T=chi S. Since S is 4 modulo 8 and |S|<=28,

    T is in {−28,−12,4,20}.

Define the signed defect array

    delta(a) = chi(a)  if T(a)=−12,
               −chi(a) if T(a)=4,
               0       otherwise.

Thus A=supp(delta), |A|=L, and S=−chi+delta modulo 3. Let

    b=phi(Hdelta),    m=wt(b),    B=HS/512.

Reduction modulo 3 gives B=phi(q−b). Let

    alpha = #{x in U: b(x)=q(x)},
    E     = {x in U: b(x)=−q(x)},    nu=|E|.

The possibilities for B inside U are q,0,−q according as b is 0,q,−q; outside U, B=−b. The exact v1 identities are

    alpha+2nu = 8−L/4−u/8,                           (2)
    m = 144−L/2−3nu.                                (3)

For clarity, Gamma=−256 sum_U qB=−256(4−alpha−2nu), while m=w_S−4+2alpha+nu. Substitution of (1) gives (2) and (3). Also Gamma is divisible by 256; together with u in 8Z and (1), this gives **L in 4Z**.

The v1 L=0 exclusion can also be seen from (3): delta=0 implies b=0, nu=0, m=0, contradicting m=144. Hence L is a positive multiple of 4.

## 3. Exact spatial reconstruction: C+3P

Define INTEGER arrays

    C=Hb,    P=H(q·1_E).

Because B=phi(q−b), as an integer identity—not just a congruence—

    B=q−b−3q·1_E.

Also Hq=−2chi. Inverting HS=512B gives

    S=2HB=−4chi−2C−6P.                               (4)

On a defect a in A, the definition of delta gives S(a)=−4chi(a)−8delta(a). Outside A, S(a)=−4chi(a)±24chi(a). Thus (4) implies exactly

    C(a)+3P(a)=4delta(a)             for a in A,
    |C(a)+3P(a)|=12                 for a outside A. (5)

Since P is the sum of nu signed Walsh characters,

    |P(a)|<=nu,
    |C(a)|<=4+3nu                   for a in A.       (6)

These are simultaneous constraints on the same signed defect support and the same quadratic-dual exceptional set E. They are stronger than the scalar correlation and Parseval identities alone.

## 4. Defects must have affine rank eight

Let V=affspan(A)=a_0+W. For h in W-perp,

    Hdelta(x+h)=(−1)^(a_0·h) Hdelta(x).

The function phi is odd, so the same covariance holds for b=phi(Hdelta). Its Walsh transform C=Hb is therefore supported on V: C(a)=0 whenever a is outside V. This is an exact integer cancellation, not a modulo-3 support assertion.

If V were proper, choose a outside V. It is also outside A, so (5) gives |3P(a)|=12. But (2), L>=4 and u>=8 imply 2nu<=6, hence nu<=3; therefore |3P(a)|<=9. Contradiction.

Thus affspan(A)=F_2^8. At least nine distinct points are needed, and L is a multiple of 4, so **L>=12**. This route needs no signed-four-point or signed-eight-point transform classification, although those remain part of the frozen v1 review chain.

From (2), u>=8 and alpha,nu>=0 also give

    0 <= 8−L/4−u/8 <= 7−L/4,

so **L<=28**. It remains to exclude L=12 before listing the residual frontier.

## 5. The complete L=12 interface

Assume L=12. The preceding section forces affine rank 8. Label the distinct points a_1,...,a_12, put epsilon_i=delta(a_i) in {−1,1}, and form the binary affine-relation code

    Rcal = {p in F_2^12: sum_i p_i a_i=0 and sum_i p_i=0}.

The augmented point matrix has rank 9, so dim(Rcal)=3. Every word has even weight. No nonzero word has weight 2 because the points are distinct. Thus its seven nonzero words have weights in {4,6,8,10,12}. This exhausts all allowable affine positions; no preferred placement, sign pattern, or relation is imposed.

For p in Rcal, set e(p)=product_{i:p_i=1} epsilon_i. This is a character of the code and includes EVERY sign assignment relevant to the following expressions. From (2), u>=8 gives nu<=2. Equation (3) becomes

    m=138−3nu,   nu in {0,1,2}.                       (7)

The spatial bound (6) must hold at every one of the twelve points.

### 5.1 Two exact character formulas

The following are finite symbolic character identities, not results of an enumeration program:

    m = (512/3) [1−2^(−12) sum_{p in Rcal}
                           e(p)(−3)^(wt(p)/2)].        (8)

Define

    Wcal = sum_{0!=p in Rcal} e(p) g(wt(p)),
    g(4)=1, g(6)=−3, g(8)=9, g(10)=−27, g(12)=81.

Then (7) and (8) say

    Wcal=87+8nu, namely 87,95,103.                    (9)

The second formula, for each actual defect point, is

    C(a_i) = −epsilon_i/8 · sum_{p in Rcal}
                      e(p)(−3)^((|p triangle {i}|−1)/2). (10)

Here triangle is symmetric difference, so the exponent is always a nonnegative integer.

Derivation of (8): phi(t)^2=(2/3)(1−cos(2pi t/3)). Adjoin an independent global sign to the twelve characters (−1)^(a_i·x); their image is uniform on the sign vectors whose products along p are e(p). The code-projector expansion and cos(2pi/3)=−1/2, sin(2pi/3)=sqrt(3)/2 give the average cosine 2^(−12) sum_p e(p)(−3)^(wt(p)/2). Multiplication by 256 gives (8). The global sign changes no square or cosine.

Derivation of (10): the multilinear Fourier coefficient, at an ODD subset J of twelve independent signs, of phi(sum of those signs) is

    −(−3)^((|J|−1)/2)/2048;

the even-subset coefficients vanish. This follows directly by taking the imaginary part of the product of twelve factors (−1+i sqrt(3) s_i)/2. After substituting s_i=epsilon_i(−1)^(a_i·x), the odd subsets mapping to frequency a_i are EXACTLY J={i} triangle p, p in Rcal. Their signs are epsilon_i e(p). Multiplication by the Walsh size 256 gives (10). Thus the dimension and all sign factors in (8) and (10) are explicit.

## 6. L=12 when the all-ones word is a relation

Let J be the word of weight 12 and suppose J belongs to Rcal. No word has weight 10, since its complement would have forbidden weight 2. The other six nonzero words form three complementary pairs. A pair has weights (4,8), called type A, or (6,6), called type B.

First, if e(J)=−1, the contribution of J to Wcal is −81, a type-A pair contributes −8r for r=±1, and a type-B pair contributes 0. Hence Wcal<=−81+24=−57, impossible in (9).

It remains that e(J)=1. The character descends to Rcal/<J>, a two-dimensional binary group. On its three nonzero elements the three pair signs r are either all +1 or consist of one +1 and two −1. Let k be the number of A pairs and a the sum of their pair signs. Then

    Wcal = 81+10 sum_A r−6 sum_B r.                  (11)

For an A pair denote its weight-four member by P_4. At coordinate i put

    h_i=sum_A r·1_{i in P_4}.

In (10), the zero word and J contribute 1−243=−242. An A pair contributes −18r+96r·1_{i in P_4}; a B pair contributes −18r. Consequently

    C(a_i)/epsilon_i = 37−12h_i   if all pair signs are +1,
                      28−12h_i   otherwise.           (12)

This checks the actual spatial coefficients, not only their squared sum.

If all pair signs are +1, (11) reads Wcal=63+16k. Among {87,95,103}, only 95 occurs, at k=2 and nu=1. Then 0<=h_i<=2, so (12) gives C(a_i)/epsilon_i>=13 for every i. This contradicts |C(a_i)|<=4+3nu=7.

If the pair character is nontrivial, sum of the three signs is −1, and (11) gives Wcal=87+16a. The only possibilities in (9) are:

- nu=0, a=0. The A pairs are either absent or consist of one positive and one negative pair. Thus h_i<=1, and C(a_i)/epsilon_i>=16>4.
- nu=2, a=1. The only A pair is the positive one. Thus h_i is 0 or 1, and C(a_i)/epsilon_i>=16>10.

Both violate (6). There is no nu=1 solution in this nontrivial-character case. This disposes of every code and sign character containing J.

## 7. L=12 when the all-ones word is NOT a relation

Now weights are only 4,6,8,10. Any weight-ten word is the complement of a two-element missing set. Two such missing pairs are disjoint: otherwise the two codewords would differ in weight 2. Any three weight-ten words are independent, and their pairwise sums have weight 4 and their triple sum weight 6. Thus a three-dimensional code has at most three words of weight 10. This gives the exhaustive cases below.

### 7.1 Zero or one weight-ten word

Using absolute values of the seven contributions to Wcal gives respectively

    Wcal<=7·9=63,
    Wcal<=27+6·9=81.

Neither reaches the smallest required value 87.

### 7.2 Exactly two weight-ten words

Let their character values be x,y. Their sum has weight 4. The contribution of this two-dimensional subgroup, excluding zero, is

    −27(x+y)+xy,

which is 55,−1,−53 as (x,y) are (−1,−1), mixed, or (1,1). Each of the other four terms is in {±1,±3,±9}, so their sum is at most 36. To reach 87 or more requires x=y=−1. Their remaining sum would have to be 32,40,48 for nu=0,1,2.

The last two exceed 36. The first is impossible as well: the maximum 36 consists of four 9s, and replacing any 9 by another allowed term reduces it by at least 6, never by exactly 4. Thus no signs in this case satisfy (9).

### 7.3 Exactly three weight-ten words

Write the three missing pairs as P,Q,R; they are pairwise disjoint. Their three words generate the entire code. If their character values are x,y,z, the distribution is three weight-ten words, three weight-four pair sums, and one weight-six triple sum. Therefore

    Wcal=−27(x+y+z)+(xy+xz+yz)−3xyz.

For respectively 0,1,2,3 negative signs, its values are

    −81, −25, 23, 87.

Only the last can satisfy (9): nu=0 and x=y=z=−1.

There are six coordinates outside the three missing pairs. At any such coordinate i, all three weight-ten words contain i, all three weight-four words omit i, and the weight-six triple word contains i. The sum in (10) is exactly

    1 − 3·81 + 3·9 − 9 = −224.

Thus C(a_i)=28epsilon_i. But nu=0 requires C(a_i)=4epsilon_i by (5), a contradiction. These six coordinates are actual nonzero entries of delta, so none can be ignored.

This completes ALL three-dimensional even relation codes, all allowed weights, and all characters. Hence **L=12 is impossible**.

## 8. Conclusion and exact residual cases

The shared v1 identities give a positive multiple-of-four L; the spatial obstruction gives affine rank eight and L>=12; the R-zero and occupancy identities give L<=28; Sections 5–7 exclude L=12. Therefore

    L in {16,20,24,28},    affrank(supp(delta))=8.      (13)

No claim is made that any of these four cases is realizable. For the actual balanced branch the following are exact NECESSARY residual scalar cases; all u values are multiples of 8:

| L | nu | m | possible u from occupancy alone |
|---|----|---|--------------------------------|
| 16 | 0 | 136 | 8,16,24,32 |
| 16 | 1 | 133 | 8,16 |
| 20 | 0 | 134 | 8,16,24 |
| 20 | 1 | 131 | 8 |
| 24 | 0 | 132 | 8,16 |
| 28 | 0 | 130 | 8 |

In each row alpha=8−L/4−u/8−2nu; the same signed set must satisfy (5), the actual quadratic q and E constraints, the cap, and BOTH genuine Boolean inverse transforms. This is not a finite list of functions or a scalar-feasibility certificate.

The first unproved case is L=16 with a full-affine-rank sixteen-point signed support. Its affine relation code has dimension 16−9=7. The next consequential input must enforce the same C+3P identity on and off that actual support and then the simultaneous S/R Boolean inverse restrictions; another scalar Parseval witness is not such an input. No execution or search is authorized by this protocol.

## 9. Attribution, verification gates, and honest campaign state

The canonical Boolean-pair interface is the actual current `information-science/evidence/hard-continuation-20261015/proof.md`, SHA-256 `d2c1605d8ee20423e137066b62b3dac31406bd4380d075c1b85064c01cf6dff9`, especially sections 2 and 4. The current balanced split source, read before v1 and explicitly rederived there, is `quadratic-distance/PROOF.md` section 6, SHA-256 `caf7db55c93a6b3fc73d461fd4dc018f387ec510adf29417605ee4e3e71730b5`. The exact v1 source/receipt/earlier-import paths and hashes are recorded in `rank2-dual-support-result-v1.json`.

The present new L=12 classification imports no archived scalar producer, no full-rank m=224 assumption, and no signed-eight-point table. It is an exhaustive hand proof using a dimension-three even binary relation code, with every sign character retained. Its correctness still needs an actual separate peer reconstruction and parent read on these pinned bytes, plus disposition of the retained v1 reconstruction. Import trust, correctness, balanced/full-512 scope, novelty, and significance remain distinct gates. Python/Fraction arithmetic or a hash would not be a formal proof; no such arithmetic was run here.

This improves a necessary condition for ONE of the seven remaining entire types. It does not turn seven types into six, prove nonexistence in type (2,192), prove a new unrestricted balanced nonlinearity ceiling, construct an NL242 function, certify novelty, or establish a Lean/kernel theorem. The explicit classical NL240 table and its L=0 symbolic certificate remain only the sharpness control for the separate low-L ceiling. The unrestricted balanced NL242 question remains unresolved.
