# Universal next-bit quartic rigidity, and ENTIRE full-rank L9/L10 exclusion

Owner InfoBalancedNL242-2. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:41:33 PDT 2026**. **NEW WRITTEN AUTHOR CANDIDATE**, not reviewed/adopted/formal/kernel/finite checked or novelty-cleared. Exact symbols/fractions/integer products only, including private reasoning. No scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/CLI/nested agent/new GO.

The entire new already-exposed proof was saved in checkpoint035 at actual07:36:44. This successor closes the genuine coisotropic5-flat residual left OPEN in `fullrank-L9-coisotropic-affine5-reduction-v1.md`; the older partial source is unchanged and does NOT retrospectively prove the closure. It also treats ALL ten-defect supports/signs at BOTH full-rank weights, not one Gold/graph/coset profile. The two new complete strata remain only WRITTEN candidates until a fresh entire-scope gate. They are NOT part of the earlier rank4/rank6 gate requests and cannot inherit their prospective acceptance.

## 1. Exact quantities and theorem

Let an ACTUAL balanced Boolean function on F2^9 have ALL512 Walsh magnitudes at most28. Use a genuine common-coordinate canonical pair K1,K2 on G=F2^8, H²=256I, with K_i≡2mod8, BOTH actual Boolean inverses, and

```text
S=K1+K2, R=K1-K2, p=R/8,
D=p mod2 quadratic, D(0)=0, chi=(-1)^D,
R(0)=0, Hp=64a, a ternary,
S≡4+8D mod16, |S|,|R|<=28.
```

These are the retained original-target canonical/odd-half identities, not free stream choices. Put T=chi*S, so T takes precisely the allowed values -28,-12,4,20. Define the actual signed defect delta=chi at T=-12, delta=-chi at T=4, and0 otherwise; A=supp(delta), L=|A| is exactly the total number of original magnitudes4/12. Write b=phi(Hdelta), C=Hb, m=wt(b), where phi is centered reduction mod3. All arrays remain on this SAME G. The actual ternary inverse B=HS/512 is phi(q-b), where q=phi(Hchi).

**New universal theorem.** For ANY intrinsic quadratic rank, E=((p-D)/2)mod2 has degree at most4, with its top quartic equal to the Pfaffian4 polynomial of the polar matrix of D. The top quartic of a second ACTUAL common S/R carry kappa is the SAME polynomial, not independently chosen.

**New full-rank theorems.** If the polar rank of D is8:

1. The signed defect cannot be supported in ANY coisotropic affine5-flat.
2. If L>=9, its affine span has dimension at least6.
3. The zero set Z={p=0} has even size z>=10 and zero XOR; its second-moment matrix is the inverse polar matrix of D. At wt(D)=136, in fact z>=12.
4. ENTIRE L9 and ENTIRE L10 are impossible, at BOTH wt(D)=120 and136, with all actual supports/signs and the real coupled R completion retained.

This does NOT claim that larger L are excluded, that a solution in another intrinsic type is constructed, or that the unrestricted original NL242 problem is settled. It does not silently union old small-L results into a new numerical ceiling.

## 2. Elementary exact Walsh bit lemmas

We supply the bit arguments rather than import a computational table. All Boolean polynomial degrees below are over F2.

### 2.1. Odd signed Walsh sum

Let J(x)=sum_y z(y)(-1)^(x.y), z(y) in{0,±1}, with odd support size. Then J is odd at every x. The phase

```text
eta_J=(-1)^((J-1)/2)
```

is an affine character, because J=w-2I(x), w=sum z odd, I=sum z(y) l_y(x), and mod2 I is affine-linear. Here l_y(x)=x.y, with affine coordinates allowed. Also

```text
q_J=(J²-1)/8 mod2                                      (1)
```

is quadratic. Indeed

```text
(J²-1)/8=(w²-1)/8 + binom(I,2) + ((1-w)/2)I.
```

Expanding binom(sum z(y)l_y,2), each two-distinct-index term is a product of two affine forms; a coefficient z=-1 adds only the linear term binom(-l,2)=l. Thus the entire residue is degree<=2, for signed arrays too. No sign of J or choice of a particular point is required. Since eta_J*J≡1mod4,

```text
(eta_J*J-1)/4 mod2 = (J²-1)/8 mod2 = q_J.               (2)
```

An actual normalized odd-half spectrum K≡2mod8 therefore has

```text
J_K=(K-2)/8 mod2 quadratic.                            (3)
```

For completeness K/2, modulo16, is a signed affine-character multiple of an odd-support Walsh sum: the ordinary odd-weight half has W/2=128*1_{x=0}-H1_support, whose first term vanishes mod16. Multiplying by its actual canonical character does not change its square. Since K/2≡1mod4, (1) equals (K-2)/8mod2. This proves(3) at the genuine odd-half interface.

### 2.2. Divisible inverse implies a low parity degree

For an integer array v on F2^n with Hv divisible by2^h, the parity function vmod2 has degree at most n-h. To see this, the ANF coefficient on a k-dimensional coordinate face is its integer face sum mod2; the Walsh expression for that sum is 2^(k-n) times a sum of Hv entries, hence even whenever k>n-h. The assertion is also valid in any translated coordinate system. We use only this face-sum identity, not an executable degree test.

## 3. UNIVERSAL quartic of the actual R next bit

Let Etilde=(p-D)/2 as an INTEGER array and E=Etilde mod2. Fix a k-dimensional coordinate face through0. Since Hp=64a,

```text
sum_face p = 2^(k-8) sum_(frequencies zero on face) Hp
           = 2^(k-2) sum a.
```

For k>=4 this is divisible by4. Therefore its E ANF coefficient is

```text
sum_face Etilde mod2 = -(wt(D restricted to face)/2)mod2. (4)
```

The weight of a quadratic in k>=5 variables is divisible by4: a radical-linear term gives the balanced value2^(k-1); otherwise the elementary symplectic normal form gives2^(k-1)±2^(k-r-1), and k-r-1>=2. Thus EVERY coefficient of E of degree>=5 vanishes.

On a4-face the half-weight is odd exactly when the restricted polar matrix has rank4, with weight6 or10. Its determinant is the square of its Pfaffian, so over F2 the coefficient is precisely that Pfaffian. Hence

```text
deg E<=4,
[E]_4 = sum_(i<j<k<l) Pf(B_D|{i,j,k,l}) x_i x_j x_k x_l. (5)
```

The argument can be reapplied after ANY linear change of G; it does not assume that D originally had no affine part. In a full-rank adapted symplectic basis (u_i,v_i),1<=i<=4, its top quartic is

```text
P4 = sum_(i<j) u_i v_i u_j v_j.                         (6)
```

This is a genuine simultaneous restriction on the next carry of p. It is stronger than a loose degree bound, but does not turn a previously unproved residue-class table into an input.

## 4. The SAME quartic controls the actual S/R carry

Set zeta=(-S-4chi)/8, which is an odd integer everywhere by the actual S congruence/cap. Let jtilde=(zeta-1)/2 and j=jtilde mod2. Since chi=1-2D and p=D+2Etilde,

```text
K2=(S-R)/2=-2chi-4zeta-4p=-6-8(jtilde+Etilde).
```

Equation(3) applied to the ACTUAL K2 shows that j+E differs from a quadratic by the constant1. Hence the phase

```text
tau=-(-1)^j,  chi*tau=(-1)^kappa,
kappa=D+j+1
```

has degree<=4 and exactly the quartic(5). One may also check directly from the FOUR allowed values of T that

```text
kappa=(T-4)/16 mod2.                                   (7)
```

For T=-28,-12,4,20 this bit is respectively0,1,0,1. This is the ACTUAL common carry. Independent choices of Fourier modes or a new phase fitted separately to each fibre would violate(5)-(7).

## 5. Full-rank physical fibres and local inverse

Now assume rank(B_D)=8, d=wt(D) in{120,136}. The quadratic transform q=Hchi/16 is a global sign and Hq=16chi. The centered-residue polynomial of q-b is

```text
B=q(1-(3/2)b²)+(1/2)b,
S=F+C, F=2H[q(1-(3/2)b²)], C=Hb.                       (8)
```

This is an identity of actual arrays. Suppose A is contained in an affine flat L0=a0+K of dimension s. Signed annihilator covariance makes C supported inside L0 and b² K-annihilator-periodic. Expanding b² in characters labelled by K shows that F/chi is constant on cosets of

```text
T0=K^perp_(B_D), dim T0=8-s.                            (9)
```

Indeed each shifted quadratic sign chi(y+k)/chi(y) is constant on those cosets. If T0 is NOT contained in K, EVERY T0 fibre meets the outside of L0. There delta=0, C=0, and chi*S is20 or-28. Thus |F|<=28 everywhere in this noncoisotropic situation. No independent extension of a background is assumed.

In local affine coordinates on L0 the exact inverse is

```text
C=2^(8-s)J, J=H_s z_local,
z_local=phi(H_s delta_local), m=2^(8-s)wt(z_local),
sum J²=2^s wt(z_local).                                (10)
```

The support flat can strictly contain A; all formulas remain valid. Outside A, C≡0mod3, and on A, C≡delta mod3, because H²=256≡1mod3.

## 6. NO coisotropic affine5-flat can contain A

Assume dim K5 and T0<=K, dim T0=3. Write c=F/chi, constant on T0 fibres, and C=8J locally. Outside L0 equation(7) and S=F show that kappa is T0-periodic. On L0 all J entries have common parity.

**J even.** Write J=2j0. Since H5 j0=16z_local, lemma2.2 makes j0mod2 affine. As T=chi*S≡4mod16, c=4+16h with h constant per T0 fibre. Then(7) gives

```text
kappa|L0 = h + j0 mod2.
```

For each t inT0 its derivative along t is constant on L0.

**J odd.** Write J=1+2j0. Lemma2.1 makes j0mod2 affine. The congruence now gives c=12+16h. Since chi=1-2D,

```text
T=c+8chi*J=20+16(h-D+chi*j0),
kappa|L0=1+h+D+j0 mod2.
```

Again every t inT0 gives a constant derivative on L0, because T0 is the radical of the restriction of B_D to K, so D_t D is constant on L0.

Since t preserves L0, outside it the derivative is zero. Therefore for EVERY t inT0

```text
D_t kappa = gamma_t*1_L0 on ALL G, gamma_t inF2.         (11)
```

Choose an actual symplectic basis with T0=<u1,u2,u3>; then K=T0perp is given by the three fixed coordinates v1,v2,v3. The cubic top of 1_L0 is v1v2v3. But (6) gives the cubic top of D_(u1)kappa as

```text
v1(u2v2+u3v3+u4v4),                                    (12)
```

which is neither zero nor v1v2v3. This contradicts(11). The contradiction includes ALL support sizes/signs in L0 and BOTH J parities; it is not a chosen coisotropic profile.

## 7. If L>=9, the full-rank affine support dimension is at least6

We reproduce the full lower-dimensional obstruction, so this application is not a narrowed use of the old L9 partial source.

The ACTUAL occupancy/energy identities from `global-all-rank-ternary-lift-and-dual-occupancy-v1.md` give

```text
m=264-(15/32)d+L+(3/8)u >=201+L,                        (13)
u=#{p0}+2#{|p|1}>0.
```

These follow from BOTH inverse spectra: sum p²=1024+5d-4u and the signed chi*S inner product. They are not optional histogram constraints. Since R(0)=0, its inverse support size is even, which gives u≡6mod8 at d120 and u≡2mod8 at d136.

An affine3-flat cannot contain L>=9 distinct points. If the affine dimension is4 and K is Lagrangian, extend it to a coisotropic5-space by adjoining any vector outside K; its perpendicular is a3-subspace of K. Section6 excludes it. In a NON-Lagrangian4-space all F fibres meet the outside, so on A, |C|<=40, and off A, |C|<=56. Write C=16J by(10). If J odd, its absolute values on/off A are bounded by1/3; hence

```text
m=sum J²<=L+9(16-L)=144-8L.
```

If J even, its congruence mod3 forces J=-2delta on A and0 off A, hence m=4L. Both contradict(13).

For affine dimension5, the coisotropic case is section6. In the NON-coisotropic case write C=8J and n=wt(z_local), so m=8n=(sum J²)/4. If n odd, J is odd, with |J|<=5 on A and<=7 off A. Mod3 sharpens these to |J|1 or5 on A and3 off A. Thus

```text
m<=(25L+9(32-L))/4=72+4L,
```

which with(13) requires L>=43, impossible in32 points.

If n even, put j0=J/2; H5j0=16z_local makes its parity affine. Let w be its odd-value count, so w=0,16 or32. Let x be the number of odd j0 entries on A. On A, |j0|1 or2; off A it is0 or3. Thus

```text
m=sum j0²=4L+9w-12x,   and m<=288-5L.                  (14)
```

If w0, m4L contradicts(13). If w16, the first bound gives L>=19 while the second gives L<=14. If w32, x=L and m=288-8L, so(13) gives L<=9; but n=m/8=36-L is even, forcing L even. No L>=9 remains. This exhausts all dimension<=5 supports.

## 8. ENTIRE full-rank L9 exclusion

For k distinct signed points of affine dimension s, let R_even be the complete even relation code of the augmented point columns (1,x). It has dimension k-s-1 and minimum nonzero weight4. Let e(P) be the product of the actual signs on a relation P. Character averaging at the cube roots of unity gives, for k odd,

```text
m=(512/3)[1+2^-k sum_(P in R_even) e(P)(-3)^(wt(P)/2)]. (15)
```

It is an exact all-sign relation identity, not enumeration. One can derive it by expanding the product of the k factors -1/2 plus the signed imaginary sqrt3/2 character term; only EVEN augmented relations survive after an independent harmless global-sign average. Actual signs give a CHARACTER of the relation code.

At k9, any affine dimension>=6 has m<=204:

- Dimension8: m171.
- Dimension7: a single relation of weight4/6/8 gives m174/168,162/180,198/144.
- Dimension6: three nonzero relations; at most one has weight8, since two would differ in weight2. If present the three weights are(8,4,4) or(8,4,6). The sign-character expressions give respectively m204/192/144 or m192/204/156/132. Without an8-word, the three nonzero coefficients have absolute value at most27, so m<=198.

But(13) in its exact form gives m>=219 at d120 and>=210 at d136. Therefore L9 would require affine dimension<=5, contradicting section7. This excludes ENTIRE L9 at BOTH full-rank weights, including the coisotropic residual that was genuinely open in the previous partial source.

## 9. Zero-set Pfaffian second moments and the sharpened u lower bounds

The actual zero indicator is

```text
1_Z=(1-D)(1+E) overF2.                                 (16)
```

On D=1 there is no zero. On D=0, p is0 or±2 and E distinguishes those possibilities. By(5), deg1_Z<=6. Therefore z is even and the XOR of Z is0. Its top6 coefficients are those of D2*P4: a perfect matching on six labels can choose its distinguished D pair in THREE ways, hence has coefficient1 mod2. They are exactly the Pfaffians of the6x6 principal minors of B_D.

Consequently the actual second moment M_Z, with entries sum_(x inZ) x_i x_j, has diagonal0 and off-diagonal

```text
(M_Z)ij=Pf(B_D with labels i,j deleted).                (17)
```

For a nonsingular alternating8-matrix B, this Pfaffian cofactor matrix is B^-1. Here is the elementary identity used: multiplying B by its Pfaffian cofactor matrix, a diagonal entry expands each perfect matching of all8 labels exactly once by the partner of the fixed label, giving Pf(B); in an off-diagonal entry each matching with the two unmatched marked labels occurs twice with opposite partner choices and cancels in F2. Since detB=Pf(B)²=1, Pf(B)=1, proving the inverse identity. Thus

```text
M_Z=B_D^-1, rank M_Z=8.                                (18)
```

The eight coordinate evaluation rows on Z are independent and have nondegenerate Gram matrix. The all-ones row is orthogonal to all of them and has zero self-pairing (z even), but is nonzero and cannot lie in their span. The augmented evaluation matrix therefore has rank9. Its column sum is0 by the even-size/zero-XOR facts, so its nonzero all-ones coefficient vector lies in the kernel; hence z>=10.

If z10, the ACTUAL point0 belongs to Z since p(0)=0. Choose eight independent other points as a linear basis. The tenth is their sum by zero XOR. Thus in those coordinates

```text
Z={0,e1,...,e8,e1+...+e8}, M_Z=I+J8, (I+J8)^-1=I+J8.
```

Equation(18) gives B_D=I+J8. Also D(0)=D(ei)=0 because p vanishes there, so D has no constant/linear part and is exactly sum_(i<j)xi xj. Its exact bias is

```text
1+8-28-56+70+56-28-8+1=16,
```

by the nine binomial layers of F2^8. Hence d120, NOT136. Therefore

```text
d120: z>=10, u≡6mod8 =>u>=14;
d136: z>=12, u≡2mod8 =>u>=18.                           (19)
```

This is a new intrinsic moment/Arf restriction on the actual R zeros, not a list of possible counts chosen independently of p.

## 10. ENTIRE L10: affine relation exhaustion leaves ONLY m220, dimension6

At L10, (13),(19) give m>=223 for d120 and m>=217 for d136. Section7 requires affine dimension>=6. The even relation identity for EVEN k10 is

```text
m=(1024-Sigma)/6,
Sigma=sum_(P in R_even) e(P)(-3)^(wt(P)/2).              (20)
```

The code has no weight2 word and its dimension is9-s.

**Dimension8.** A single nonzero relation of weight4,6,8 or10 gives respectively m169/172,175/166,157/184 or211/130. All are too small.

**Dimension7.** There are three nonzero relations. If the all-ones word J10 is present, the other two are complementary weights4/6. With x=e(J10),y=e(P4),

```text
Sigma=1-243x+9y-27xy.
```

The four actual character values give m214,208,124,136. Without J10 every coefficient has absolute value at most81, giving Sigma>=-242 and m<=211. This covers ALL dimension7 relation codes and actual sign characters.

**Dimension6.** There are seven nonzero relations. If J10 is present, the other six form THREE complementary pairs4/6; no8-word is possible because its complement would have forbidden weight2. With x=e(J10) and y_i the three4-word signs,

```text
Sigma=1-243x+(9-27x)(y1+y2+y3).
```

For x=-1 this is>=136. For x=+1 it is>=-296, so m<=220, equality only at all y_i=+1.

If J10 is ABSENT, there are at most THREE8-words. Indeed any two have disjoint missing2-sets, since an intersection would give a forbidden weight2 difference. FOUR such8-words would be linearly independent: no one/two/three/four of them sums to0, as the corresponding sums have weights8/4/4/8. That contradicts relation-code dimension3.

- With three8-words they are independent and the remaining FOUR words all have weight4. Writing their three signs x,y,z,
  Sigma=1+81(x+y+z)+9(xy+xz+yz+xyz), whose minimum is-224. Thus m<=208.
- With two8-words their subgroup contributes at least-152 (identity plus two81 terms and one9 term). The other four terms have absolute value at most27, so Sigma>=-260 and m<=214.
- With one8-word, Sigma>=1-81-6*27=-242, so m<=211.
- With no8-word, Sigma>=1-7*27=-188, so m<=202.

Thus EVERY dimension6 code has m<=220. Moreover m is divisible by4 by(10) and m≡L≡1mod3 by the mod3 norm. In the range m>=217 this forces m220. The d120 minimum223 is impossible. At d136 exact(13) forces

```text
L10, m220, u26, w_R100, affine dimension6.              (21)
```

The relation code necessarily contains J10 with trivial actual sign character. We do not need to classify the support further or use that last sign rigidity: the following argument excludes ANY actual dimension6 support at m220.

## 11. Excluding the last L10 geometry using the same quartic carry

Let L0=a0+K be the actual6-flat and T0=Kperp_B of dimension2. By(10),

```text
C=4J, J=H6 z_local, wt(z_local)=m/4=55 ODD.             (22)
```

Hence J is odd EVERYWHERE on L0.

### 11.1. Noncoisotropic K

If T0 is not contained in K, every fibre meets the outside. There c=F/chi=20 or-28, in particular c≡4mod16. Since chi*S≡4mod16 globally, chi*C must be divisible by16 on L0. But C=4J with J odd cannot be divisible by16. This excludes the ENTIRE noncoisotropic geometry, not just a high-coefficient site.

### 11.2. Coisotropic K

Now T0<=K. Outside L0, kappa is T0-periodic. On L0 use lemma2.1 with the ACTUAL local signed Walsh sum J:

```text
eta=(-1)^((J-1)/2) an affine character,
J_can=eta*J≡1mod4,
j2=(J_can-1)/4mod2=(J²-1)/8mod2 quadratic.
```

Write J_can=1+4j2tilde as an INTEGER identity and gamma=chi*eta. Then

```text
T=chi*S=c+4gamma+16gamma*j2tilde.
```

The congruence T≡4mod16 determines gamma uniquely from c, so gamma is constant on every T0 fibre. Moreover h=(c+4gamma-4)/16 is an integer and T0-periodic. Equation(7) therefore gives

```text
kappa|L0=h+j2 mod2.                                    (23)
```

For EVERY t inT0, D_t kappa is affine on L0 (derivative of the quadratic j2), and0 off L0. Hence it is 1_L0 times an affine extension to G.

Choose an actual symplectic basis with T0=<u1,u2>, so K is given by fixed v1,v2. The top of 1_L0 is v1v2; therefore the cubic top of D_(u1)kappa must be divisible by v1v2. But the REQUIRED quartic(6) gives again

```text
[D_(u1)kappa]_3=v1(u2v2+u3v3+u4v4),
```

with the term v1u3v3 NOT divisible by v2. Contradiction. This closes(21), and therefore ENTIRE L10 for BOTH full-rank weights.

## 12. Original Boolean applicability, exact import union and limits

The proof concerns an ACTUAL original target and never weakens its same-coordinate reconstruction. For the equivalent raw all-rank system, the full norm equation is

```text
beta star beta+delta star delta+chi star delta+chi star chi=e0 inF3[G].
```

Its actual centered inverses a,B obey INTEGER a²+B²=1 pointwise, giving BOTH genuine Boolean inverse signs B+a and B-a and ALL512 values

```text
F(x,0)=(1-B(x)-a(x))/2,
F(x,1)=(1+B(x)-a(x))/2.
```

Together with S and R and the actual zero/balance condition, this is the retained original interface, not a separately completed stream. Sections3/4/9 explicitly use the actual R, actual canonical K2 and shared carry; they cannot be asserted for arbitrary signed-support spectra without that interface.

Named ordinary-WRITTEN inputs are the original nonzero-support-XOR/genuine odd-half/canonical pair necessity and quadratic normal form, plus the exact all-rank raw norm/Boolean map/energy identities in `global-all-rank-ternary-lift-and-dual-occupancy-v1.md` (205LF, SHA842bb4e629153bebb6c04d5041d96bedaf45ae341cd2e3c2d63a96a0b9cc86bf). The complete new Pfaffian/degree/odd-Walsh/local-fibre/affine-relation/zero-rank/coisotropic model-specific arguments are written ABOVE. The earlier partial fullrank-L9 source is explanatory history, not an unproved coisotropic premise; its high-dimensional signed9 bound is reproduced in section8. No old seven/eight-defect code table or rank2 classification is a correctness input to these new L9/L10 theorems.

This new direct proof does NOT silently minimize FULL J_U2 or the historical accepted rank2/rank4/rank6 DAG. The proposed new fresh gate may compare and independently audit this explicit smaller ordinary algebraic interface, but its acceptance is NOT manufactured here. Any union with older full-rank smaller-L results needs the literal originals, exact full imports and its OWN joint audit before a combined numerical/frontier claim.

Remaining actual full-rank L>=11, other intrinsic proper types, any actual Boolean witness/code/rho, and unrestricted balanced-NL242 remain OPEN. The new low-defect exclusions are not a whole-type solution or a nonlinearity value. Priority/novelty/SOTA UNCLEAR. No configured-family/human/formal/kernel/executable/triple-finite gate follows.

All new primary reasoning followed actual v118-D RETURN and whole031 primary ACK WRITTEN+SENT. No paused-review expansion. Own v112 exactness/ENTIRE ZERO withdrawn unrelated RQLS scout/no-guidance, documentary14-not15, older cadence/v105 false quotation and all parent/owner source/read/freeze/root/ACK/inventory/admission/exit findings remain permanent. Exact written source work only, not scientific execution. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38. Original research CONTINUES; no early final park or global clean-thought/runtime census.
