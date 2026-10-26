# Rational-inner candidate addendum 1: explicit Fourier separator and rho=1/100000

Before-creation clock observed: **2026-10-23T14:07:43-07:00**. **CANDIDATE / NOVELTY_UNCLEAR**, new work only in retained info-1's slot. Read with immutable legacy `proof-SOF24-rational-inner-candidate-v1.md`, SHA `267d717cd735537ff8c29a3c73a17ed7fb1f7939c85788a8cbd60374f74ab8a0`. This addendum replaces that candidate's unevaluated determinant radius recipe by an explicit rational radius and separator. It does not claim independent acceptance of the base construction or the P24 conclusion. No scientific program, Fourier/rank computation or symbolic engine was run.

## 1. An explicit real Fourier functional

Use the legacy p,q on |t|=1, with r=3/5,s=4/5. For a real Laurent polynomial G of degrees -4,...,4, write g_j=[t^j]G, so g_-j=bar(g_j). Define the following real-linear expressions in its positive Fourier coefficients:

    b=(10/3)g_4,
    c_0=(1+3i/4)b-(5i/2)g_3,
    T=-(400/3)g_2+(160i/3)b+(40/3)(-3+4i)c_0,
    a_0=T/(12+41i),
    Z=400g_1-120c_0.                                      (1)

Now set

    L(G)=13776 Re Z+22300 Im Z
          -106164 Re a_0+4029152 Im a_0.                   (2)

This is a completely explicit real linear functional; it ignores g_0. All coefficients are rational complex numbers, and real G with the rational Cayley coefficients used below gives rational L(G).

### Lemma 1

L vanishes on the eight-dimensional real span

    1, |p|^2, Re(p bar q), Im(p bar q),
    Re p, Im p, Re q, Im q.                               (3)

**Derivation.** For an element of that span, write

    G=h+d|p|^2+a p bar q+bar(a)bar(p)q
        +b p+bar(b)bar(p)+c q+bar(c)bar q,

with h,d real. Comparing orders4,3,2 in the legacy coefficients gives exactly

    b=(10/3)g4,
    c=9i a/40+c_0,
    (12+41i)a+16i d=T.

Therefore

    a=a_0+(-656-192i)d/1825.

The order1 identity is

    Z=-28d+(-100+27i)a+64bar(a).

Putting x=Re a, y=Im a, x0=Re a0,y0=Im a0 gives

    Re Z=-36x0-27y0-(22300/1825)d,
    Im Z=27x0-164y0+(13776/1825)d.

Eliminating d yields

    13776 Re Z+22300 Im Z
      -106164 x0+4029152 y0=0.

The coefficients follow directly from

    13776*36-22300*27=-106164,
    13776*27+22300*164=4029152.

This proves the lemma without point evaluations or an executable rank calculation. The separate eight-function independence in the base manuscript is still required for its exact real-basepoint-free kernel identification.

## 2. Positive separation of the pure eighth power

For

    G_8(t)=(t+1)^8/(256t^4),

the positive coefficients are g4=1/256,g3=1/32,g2=7/64,g1=7/32. The base symbolic comparison gives

    c_0=(20-105i)/1536,
    a_0=(18175+299100i)/1051200,
    Z=1375/16+(525/64)i.

Thus alpha=L(G_8) is positive. A deliberately crude exact bound is

    alpha
      =13776*(1375/16)+22300*(525/64)
        -106164*(18175/1051200)
        +4029152*(299100/1051200)
      >1183875-106164
      =1077711>1000000.                                   (4)

The inequality uses 0<18175/1051200<1 and positivity of the two discarded terms. This proves a quantitative separator, not just nonmembership.

## 3. A uniform functional norm bound

Let G have max_(j=1,...,4)|g_j|<=M. From (1),

    |b|<4M,
    |c_0|<= (5/4)(10/3)M+(5/2)M=(20/3)M,
    |T|<= [400/3+1600/9+4000/9]M=(6800/9)M<756M,
    |a_0|<19M,
    |Z|<=400M+120*(20/3)M=1200M.

Here |1+3i/4|=5/4, |-3+4i|=5 and |12+41i|>41. Therefore

    |L(G)|
       <=(13776+22300)*1200M
          +(106164+4029152)*19M
       =121862204M
       <122000000M.                                       (5)

These are symbolic triangle inequalities, not numerical fitting. The looseness is intentional.

## 4. Returning to real polynomial coefficients

For a real polynomial phi(z) of degree<=8 put

    G_phi(t)=phi(i(t+1)/(t-1))*(t-1)^8/(256t^4).           (6)

On the unit circle this equals phi(z)/(z^2+1)^4 under t=(z+i)/(z-i). It is a real Laurent polynomial of degrees -4,...,4; the apparent singularity at t=1 cancels because deg phi<=8.

Define

    ell(phi)=L(G_phi)/alpha.                              (7)

Then ell(z^8)=1 and, by Lemma1, ell annihilates the whole linear pole-polynomial image of the rational-inner row curve. This is the same separating normalization as the base manuscript's determinant functional, though no equality of formula representations is needed.

For 0<=j<=8, the real function |z^j|/(z^2+1)^4 is bounded by1: for |z|<=1 use numerator<=1, and for |z|>=1 use denominator>=|z|^8. Hence every Fourier coefficient of G_(z^j) has magnitude at most1, by the integral definition of Fourier coefficients. Applying (4)–(5) gives

    |ell(z^j)|<122, j=0,...,7.                             (8)

All these ell values are rational because (6) and (1)–(2) use rational complex arithmetic only.

## 5. Explicit rational disk radius

Take

    rho=1/100000.                                         (9)

For a monic eighth-degree real polynomial phi whose roots all satisfy |z|<=rho, its lower coefficients obey

    |[z^j]phi|<=binom(8,j)rho^(8-j), j<8.

Using rho<=1 and (8),

    |ell(phi)-1|
      <122*sum_(j=0)^7 binom(8,j)rho^(8-j)
      <=122*(2^8-1)*rho
      =31110/100000
      <1/2.                                               (10)

Thus the whole closed disk-root family is strictly separated from the original pole-polynomial image. The real fractional-linear step in the base candidate can now use the **fixed rational value (9)**, rather than a determinant-defined unexpanded parameter.

Accordingly (6) of the base manuscript followed by

    V_tilde(s)=(s-1)^4 V_0((s+1)/(100000(s-1)))

is an explicit rational polynomial recipe. Its row/column normalization and companion plant (base Section9) have only rational operations. An actual decimal/byte-expanded 8x8 plant has not been generated or checked, and no FINITE_VERIFIED label is implied. The direct open-neighborhood argument, real versus complex basepoint distinction and all coefficient/rank claims still need independent review.

## 6. Scope and next check

The advance here is a concrete exact linear separator and explicit radius for the **same one P24 candidate**. It is not another problem, a proof-assistant result, a cleared novelty claim or permission for executable replay. The most valuable independent check is to reconstruct (1) from the Laurent support, then (2), rather than merely evaluate the functional on a few examples. A sustained error in the base Hermitian pairing or open-plant bridge would still invalidate the proposed P24 conclusion even if this scalar separator is correct.
