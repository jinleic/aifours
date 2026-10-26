# Eight-state PH upper interval from cubic cancellation — candidate v1

Clock actually observed before creation: **2026-10-23T14:56:44-07:00**. Owner MathResearch96h, math-1. All derivations were written; no scientific program, numerical root calculation, symbolic package or proof assistant ran. The symbolic exploration preceded this packet freeze and is disclosed as such.

## 1. Target and exact candidate statement

For c>0, d>0, a=c+d, b>0, z=b^2/d^2 and K=c(a^2+b^2)^2, retain

    H(s)=K/[(s+c)((s+a)^2+b^2)^2].

The candidate is an actual eight-state PH representation for **every**

    13/20 <= z <= 8/9.                            (C8)

It is not an order-eight lower bound. The supported unrestricted B6 barrier gives a lower bound seven throughout this interval, so the direct conclusion after a successful C8 review would only be

    minimum PH order belongs to {7,8} on [13/20,8/9].

The seven-state complex-hidden extension is still a separate candidate at this freeze. If it is supported, its upper endpoint 5935/9126 exceeds 13/20, since 20*5935-13*9126=62>0. Together with that candidate and the earlier supported lower bands, C8 would yield order at most eight throughout 0<z<=8/9, while retaining the sharper exact orders wherever already established. None of these statements determines the minimum beyond the seven-state range, the entire H_(1,2) minimum-order function, or the full book question.

Status: **CANDIDATE; NOVELTY_UNCLEAR; no formal verification**. This is one upper-bound construction with four connecting charts, not four independent discoveries.

## 2. Common polynomial template and coefficient binding

Take m>0 and eta=d/m, lambda=a+eta, w=1+m^2 z. Write

    S=m+5,
    U=4m+8+2w,
    V=4m+4+(2m+6)w,
    W=w^2+4(m+1)w,
    Z=(m+1)w^2.

The visible fifth-degree factor is exactly

    D(Y)=(Y-(m+1))(Y^2-2Y+w)^2
        =Y^5-SY^4+UY^3-VY^2+WY-Z.                (1)

Use a hidden cubic

    q(Y)=Y^3+SY^2+BY+C,

where B,C depend on the chart below. Set

    p(Y)=D(Y)q(Y),
    R(x)=x^3+S eta x^2+B eta^2 x+C eta^3,
    P(x)=eta^8 p(x/eta).

For reference, the complete product coefficients are

| power | coefficient in p(Y) |
|---|---|
| 8 | 1 |
| 7 | 0 |
| 6 | B-S^2+U |
| 5 | C-SB+SU-V |
| 4 | -SC+UB-SV+W |
| 3 | UC-VB+SW-Z |
| 2 | -VC+WB-SZ |
| 1 | WC-ZB |
| 0 | -ZC |

Every displayed coefficient is bound to an actual literal product, not to sampled evaluations. Three charts choose

    B=m^2+6m+17-2w,
    C=m^3+7m^2+23m+49-2(m+7)w,                  (2)

which make powers six and five vanish. The remaining chart uses fixed B,C and retains nonnegative feedbacks for those powers.

## 3. Four closed charts and all coefficient signs

Here c_j denotes the coefficient of Y^j in p. All four charts have c_7=0. The table lists the complete remaining nonleading coefficients, including zeros. A nonpositive c_j supplies the feedback -c_j.

### Chart I: m=6, 122/5<=w<=149/6

Use

    B=89-2w, C=655-26w.

Then c_6=c_5=0 and

    c_4=-3w^2+230w-4665,
    c_3=18468-760w-12w^2,
    c_2=-2w^3+424w^2-8570w-18340,
    c_1=w(-12w^2-696w+18340),
    c_0=-7w^2 C.

Here B>39 and 0<C<21. The coefficient signs follow on the whole interval:

- c_4 is increasing there and c_4(149/6)=-9641/12<0.
- c_3 is decreasing and c_3(122/5)=-180508/25<0.
- c_2 is increasing: using 24<w<25, its derivative is greater than -6*25^2+848*24-8570=8032>0. Its upper endpoint is c_2(149/6)=-33737/108<0.
- c_1/w is decreasing and at 122/5 equals -144668/25<0.
- c_0<0.

Its z-interval is exactly

    [13/20,143/216].                              (3)

### Chart II: m=4, 313/27<=w<=131/10

Use

    B=57-2w, C=317-22w.

Again c_6=c_5=0 and

    c_4=-3w^2+158w-1665,
    c_3=6468-472w-12w^2,
    c_2=-2w^3+280w^2-2858w-6340,
    c_1=w(-12w^2-408w+6340),
    c_0=-5w^2 C.

Here B>30 and 0<C<62.

- c_4 is increasing and c_4(131/10)=-11003/100<0.
- c_3 is decreasing; w>11 gives c_3<6468-472*11-12*11^2=-176<0.
- c_2 is increasing: 11<w<14 gives derivative greater than -6*14^2+560*11-2858=2126>0. Its upper endpoint is -112591/500<0.
- c_1/w is decreasing; at 313/27 it equals -592/243<0.
- c_0<0.

The z-interval is

    [143/216,121/160].                            (4)

### Chart III: m=3, 31/4<=w<=35/4

Use the fixed stable hidden cubic

    B=53/2, C=33.

The complete coefficients are

    c_6=2w-35/2,
    c_5=4w-35,
    c_4=w^2-27w+138,
    c_3=4w^2-124w+236,
    c_2=-(11/2)w^2+28w-528,
    c_1=w(528-73w),
    c_0=-132w^2.

Both c_6,c_5 are nonpositive, vanishing together at the upper endpoint. The quadratics c_4,c_3,c_2 are strictly decreasing throughout this interval. Their lower-endpoint values are, respectively,

    -179/16, -1939/4, -20523/32,

all negative. Also 528-73w<=-151/4<0, so c_1<0; c_0<0. This chart covers

    [3/4,31/36].                                 (5)

### Chart IV: m=3, 35/4<=w<=9

Use (2):

    B=44-2w, C=208-20w.

Then c_6=c_5=0 and

    c_4=-3w^2+128w-912,
    c_3=3456-352w-12w^2,
    c_2=-2w^3+220w^2-1472w-3328,
    c_1=w(-12w^2-288w+3328),
    c_0=-4w^2 C.

Here B>=26 and 28<=C<=33.

- c_4 is increasing and c_4(9)=-3<0.
- c_3 is decreasing and c_3(35/4)=-2171/4<0.
- c_2 is increasing: 8<w<=9 gives derivative greater than -6*9^2+440*8-1472=1562>0. Its maximum is c_2(9)=-214<0.
- c_1/w is decreasing and its value at 35/4 is -443/4<0.
- c_0<0.

This covers

    [31/36,8/9].                                 (6)

At w=35/4 the hidden coefficients agree with Chart III, namely B=53/2 and C=33. The two charts really meet at the same hidden cubic, not at a missing limiting representation.

### Coverage

Charts I and II meet exactly at z=143/216. Chart II extends beyond the start 3/4 of Chart III because 121/160>3/4. Charts III and IV meet exactly at 31/36. Equations (3)–(6) thus cover the entire closed interval [13/20,8/9], with no parameter holes.

## 4. Elementary hidden-cubic stability, not a spectral assumption

In each chart, S,B,C>0 and SB>C:

- I: S=11, B>39, C<21;
- II: S=9, B>30, C<62;
- III: S=8, B=53/2, C=33;
- IV: S=8, B>=26, C<=33.

For clarity, the elementary cubic stability fact used here has a short proof. A real cubic Y^3+AY^2+BY+C with A,B,C>0 has no nonnegative real root. If its nonreal pair were p+it,p-it with p>=0, the third root would be -A-2p. Vieta would give

    B=t^2-3p^2-2Ap,
    C=(A+2p)(p^2+t^2),
    AB-C=-2p[(A+p)^2+t^2]<=0.

This contradicts AB>C. If all three roots are real, the absence of nonnegative real roots already makes all of them negative. Hence all roots have strictly negative real part. This proves the needed statement without importing an unverified positivity or realization theorem.

Consequently all roots of R(x) lie strictly in the left half-plane. There is no requirement that they all be real or distinct.

## 5. Explicit eight-state PH matrix, positive vector and transfer

For the selected chart define, for j=2,...,8,

    fj=-c_(8-j) eta^j.

Here c_7=0 and therefore f1=0. Section3 proves every fj is nonnegative and f8>0. Let C8 be the upper-shift companion with

    (C8)_(i,i+1)=1        (i=1,...,7),
    (C8)_(8,:)=(f8,f7,f6,f5,f4,f3,f2,0),

and other entries zero. Its characteristic polynomial is P. Put G=C8-lambda I.

The exact factorization is

    P(x)=(x-(m+1)eta)[(x-eta)^2+b^2]^2 R(x),

so G has the visible eigenvalues -c, -a+ib,-a-ib (the latter two each repeated twice), and the three roots of R(s+lambda). The visible ones are strictly stable. Section4 makes the hidden ones strictly stable after the additional shift by lambda>0. Thus G is Hurwitz, including every closed-chart endpoint.

Let

    D0=R(lambda)>0,
    h_i=lambda^(i-1)/D0                (i=1,...,8),
    Delta=diag(h_1,...,h_8).

All coordinates are strictly positive. The actual PH pair is

    T=Delta^(-1) G Delta,
    alpha=(C eta^3, B eta^2 lambda, S eta lambda^2,
           lambda^3,0,0,0,0)/D0.                  (7)

Equivalently T has diagonal -lambda, superdiagonal lambda and last row

    (f8/lambda^7, f7/lambda^6, f6/lambda^5,
     f5/lambda^4, f4/lambda^3, f3/lambda^2,
     f2/lambda, -lambda).

It is Metzler, Hurwitz, and alpha>=0 with alpha1=1. Because

    P(lambda)=K R(lambda)=K D0,

its first seven rows sum to zero and its last row sums to -K D0/lambda^7<0. Thus

    omega=-T1=(K D0/lambda^7)e_8>0 on its last coordinate.     (8)

This verifies the subgenerator condition directly, rather than inferring PH from eigenvalues. Feedback zeros, including the simultaneous c_6,c_5 zeros at chart boundaries, cause no loss of scaling positivity, strict exit, or stability. The return feedback f8>0 and the superdiagonal path make the generator irreducible as a consequence; irreducibility was not imposed on a hypothetical lower-bound class.

For generic x, solving (xI-C8)y=e_8 gives y_i=x^(i-1)y_1 and P(x)y_1=1. Therefore

    e_j^T(xI-C8)^(-1)e_8=x^(j-1)/P(x).

With

    v=C eta^3 e_1^T+B eta^2 e_2^T+S eta e_3^T+e_4^T,

this yields the rational identity

    v(sI-G)^(-1)K e_8=K R(s+lambda)/P(s+lambda)=H(s),

since

    P(s+lambda)=(s+c)((s+a)^2+b^2)^2 R(s+lambda).

Moreover the resolvent at lambda gives G h=-K e_8, alpha=v Delta and omega=Delta^(-1)K e_8. Consequently (7)–(8) preserve the exact transfer:

    alpha(sI-T)^(-1)omega=H(s).

All three hidden factors, with whatever real/complex multiplicity the cubic has, are canceled by the full same R(s+lambda). Repeated desired complex poles retain their exact multiplicity two. This completes the literal eight-state construction for C8.

## 6. An exact upper endpoint and nonclaims

The top endpoint is Chart IV at m=3,w=9:

    eta=d/3, lambda=a+d/3, z=8/9,
    q(Y)=Y^3+8Y^2+26Y+28,
    p(Y)=Y^8-3Y^4-684Y^3-214Y^2-2124Y-9072.

This rational matrix anchor specializes the full proof; it is not an empirical certificate for the interval. Its hidden cubic has 8*26>28, so the displayed elementary proof gives strict stability.

The supported B6 source is `proof-unrestricted-six-state-barrier-v1.md`, SHA256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`, at its actual separate-review/parent-disposition boundary. Thus if C8 survives review, no value in its interval has minimum below seven. There is **no** order-seven exclusion above either previous upper endpoint, and no exact-minimum-eight claim.

The connecting seven-state candidate is `proof-seven-state-complex-hidden-extension-v1.md`, SHA256 `023ac8611a66263233288838eaf3dcd3ac0013111a5be93fb5974e7f47e39667`; it is not counted as accepted at this packet's freeze. The previously accepted v2 baseline and its later written-check overlays retain their exact statuses. The round's timestamp and verification errata apply. No formal proof or cross-vendor/human gate is implied.

The companion, canceled-mode and positive diagonal-scaling mechanisms are classical. The Kim–Ryou 2012 primary source already read for the immediately preceding packet treats general positive sufficient constructions with repeated complex poles: <https://www.scitepress.org/Papers/2012/39814/39814.pdf>. This is not an exhaustive prior-art or novelty verdict on the present constants. No new general positive-realization theorem is claimed.

The next correctness gate is an independent written reconstruction of the complete four product tables and their interval sign bounds; exact chart coverage; elementary cubic stability; actual positive normalization, exits and transfer cancellation; and the distinction between upper8 and exact8. No execution is requested or authorized by this manuscript.
