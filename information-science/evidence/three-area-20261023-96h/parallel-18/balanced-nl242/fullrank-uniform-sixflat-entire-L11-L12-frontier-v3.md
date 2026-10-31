# Full-rank uniform six-flat obstruction; ENTIRE L11 and weight120/L12; actual weight136/L12 coupled residual

Owner InfoBalancedNL242-2. Actual `/bin/date` BEFORE this write: **Mon Oct 26 07:55:51 PDT 2026**. **NEW WRITTEN AUTHOR CANDIDATE**. Exact symbolic/fraction/integer-product reasoning only, even privately. No scientific interpreter/calculator/eval/program/CAS/enumeration/solver/replay/CLI/nested agent/new GO. No review/adoption/formal/kernel/novelty/SOTA claim.

All already-exposed arguments below were saved in checkpoint036. This is a successor to the complete404LF `fullrank-quartic-carry-entire-L9-L10-exclusion-v2.md` (SHA37797af6c5c28468782e1a4981d769b664313eb361d8b1bebfdcf0a3748e4667), not an edit to it or an expansion of any already frozen gate. The universal six-flat obstruction is the NEW main result; the next entire-stratum consequences are applications. No magnitude-only/profile construction or independent R completion is asserted.

## 1. Exact common-object setting and new theorem

Use the ACTUAL original balanced9-variable peak28 target interface of v2: SAME G=F2^8, BOTH actual Boolean inverse spectra, canonical K1,K2≡2mod8, S=K1+K2, R=K1-K2=8p, D=pmod2 quadratic with D0=0, R0=0, Hp=64a. All512 Boolean values and all256 S/R sites are retained.

Assume intrinsic polar rank8, d=wt(D)120 or136. Put chi=(-1)^D, q=Hchi/16, actual signed defects delta as in v2, A=supp(delta), L=|A|, b=phi(Hdelta), C=Hb, m=wt(b). The exact shared-carry theorem of v2 gives

```text
S=F+C,
F=2H[q(1-(3/2)b²)],
T=chi*S in{-28,-12,4,20},
kappa=(T-4)/16mod2, deg kappa<=4,
[kappa]_4=P4=sum_(i<j)ui vi uj vj.                      (1)
```

For support in an affine flat a0+K, F/chi is Kperp_(B_D)-periodic, and C is supported there. No phase in(1) is chosen independently.

**New uniform theorem.** In the FULL actual system:

- NO coisotropic affine6-flat can contain A, for EITHER parity of the local inverse support.
- In ANY noncoisotropic affine6-flat containing A one must have m<=216.
- Consequently, if L>=10, A has affine dimension at least7.
- ENTIRE L11 is impossible for BOTH d120/136. ENTIRE L12 is impossible for d120.
- At d136,L12 the ONLY remaining actual possibility has affine dimension7, m222,u26,w_R100, and the exact intrinsic support/sign class and common-carry/R completion conditions in sections7-8. It is NOT shown impossible or realized here.

No entire full-rank type, unrestricted nonlinearity value or actual Boolean witness is claimed.

## 2. COISOTROPIC affine6-flat: ALL local parities excluded

Let L0=a0+K have dim6 and T0=Kperp_(B_D)<=K have dim2. Write c=F/chi, constant on T0 fibres. On L0,

```text
C=4J, J=H6 z_local,
z_local=phi(H6 delta_local), m=4wt(z_local).            (2)
```

Outside L0, kappa is T0-periodic by S=F. If J is odd, the complete v2 section11.2 proof already applies without using L10 or m220: eta=(-1)^((J-1)/2) is affine, (J²-1)/8mod2 quadratic, and T≡4mod16 forces the necessary eta/chi phase T0-periodic. It follows that every D_t kappa, t inT0, is affine on L0 and zero outside.

We now cover EVERY EVEN J as well. Set j=J/2. Since H6j=32z_local, its parity lambda=jmod2 is affine by the face lemma. The actual congruence

```text
T=c+8chi*j≡4mod16
```

forces c≡4-8lambda mod16, so lambda is T0-periodic. Let

```text
vtilde=(j-lambda)/2,
h=(c-4+8lambda)/16.
```

The Walsh transform of any affine Boolean lambda is divisible by32. Thus H6vtilde=(32z_local-H6lambda)/2 is divisible by16, and v=vtilde mod2 is quadratic by the SAME face lemma. The integer h is T0-periodic. Using chi=1-2D gives

```text
T=4+16(h-Dlambda+chi*vtilde),
kappa|L0=h+Dlambda+v mod2.                             (3)
```

For t inT0, D_tD is constant on L0 because T0 is the radical of the polar form restricted to K; D_tlambda=0. Therefore D_t(Dlambda)=(D_tD)lambda is affine, as is D_tv. Again D_tkappa is affine on L0 and0 outside.

For BOTH local parities, D_tkappa equals 1_L0 times an affine extension to G. Adapt symplectic coordinates so T0=<u1,u2> and L0 fixes v1,v2. Its cubic top must be divisible by v1v2. But(1) forces

```text
[D_(u1)kappa]_3=v1(u2v2+u3v3+u4v4),
```

not divisible by v2. Contradiction. This is a UNIFORM obstruction to all coisotropic6-flats, not an odd-support-only specialization or count check.

## 3. NONCOISOTROPIC affine6-flat: actual m<=216

If K has dimension6 and T0=Kperp is not contained in K, its alternating2-dimensional restriction is nondegenerate. Indeed a2-dimensional alternating space has rank0 or2; rank0 would make T0 isotropic and contained in T0perp=K. Thus

```text
G=K6 orthogonal-direct-sum T2,
```

with both restrictions nondegenerate. Choose the actual affine support flat as t0+K. The quadratic sign factors chi=chi_K*chi_T, allowing arbitrary actual affine factors. Define q_K=H6chi_K/8 and q_T=H2chi_T/2, both signs; then q=q_K*q_T, H6q_K=8chi_K, H2q_T=2chi_T. No sign convention is suppressed.

The ACTUAL b is a T-character times z_local, so b²=z_local². Let

```text
Z_b={x inF2^6:z_local(x)=0}, e=|Z_b|,
n=wt(z_local)=64-e, m=4n.
```

Every T0 fibre meets the outside of the support flat. There delta=C=0 and c=F/chi is20 or-28. Expanding(1) with z_local²=1-1_Zb gives the exact physical expression

```text
c=-16+6chi_K H6(q_K*1_Zb).                             (4)
```

The coefficient6 is from 3*H2q_T=6chi_T. It is NOT12. Thus for the actual set Y of K-sites with c20,

```text
h0=chi_K H6(q_K*1_Zb)=-2+8*1_Y.                        (5)
```

Parseval gives

```text
64e=sum h0²=256+32|Y|,
|Y|=2e-8.                                               (6)
```

Inverting(5) and using H6chi_K=8q_K yields

```text
H6(chi_K*1_Y)=2q_K+8q_K*1_Zb.                          (7)
```

Equation(6) first ensures e>=4, so Z_b is nonempty. At ANY actual site of Z_b, the right side of(7) has absolute value10. The left side is a sum of |Y| signs, so |Y|>=10. Thus e>=9 and n<=55.

There is one further ACTUAL congruence, not an optional parity pruning: c20/-28 is4mod16 and T is4mod16, so C is divisible by16 on L0. By(2), J is divisible by4. Its common parity is nmod2, hence n is even. Consequently

```text
n<=54, m=4n<=216.                                      (8)
```

This proof retains the prescribed quadratic signs, exact local b zero set and common physical F fibres. A count alone would not give(7). It is not a freely chosen stream or a finite code-table assertion.

## 4. Uniform affine-dimension consequence

The exact full-rank occupancy and the ACTUAL R-zero Pfaffian theorem of v2 give

```text
m=264-(15/32)d+L+(3/8)u,
d120:u>=14 =>m>=213+L,
d136:u>=18 =>m>=207+L.                                  (9)
```

The v2 low-dimensional theorem already excludes all affine dimensions<=5 whenever L>=9. For L>=10, (9) gives m>=217, contradicting(8) in a noncoisotropic6-flat and section2 in a coisotropic6-flat. Hence

```text
L>=10 => affine dimension(A)>=7.                       (10)
```

L9 was separately excluded in v2; we do not silently treat that proof as a claim about every larger stratum. This uniform physical-dimension barrier is the new tool for the next entire cases.

## 5. ENTIRE L11, BOTH full-rank weights

For an ACTUAL signed k-point support with affine dimension s, let R_even be its COMPLETE even augmented relation code, dimension k-s-1, with no nonzero weight2. Its actual sign products e(P) form a character. The exact cube-root character identity gives for k11

```text
m=(2048+Sigma)/12,
Sigma=sum_(P in R_even) e(P)(-3)^(wt(P)/2).              (11)
```

By(9), m>=224 at d120 or>=218 at d136. By(10), s7 or8.

**s8, relation dimension2.** At most ONE word has weight10: two would differ in weight2, since each misses a single position. If present, the other pair has weights(4,6),(4,8) or(6,6). With x the10-word sign, the base is1-243x. When x=-1, the complementary-pair difference has absolute value at most72, so Sigma<=316. When x=+1, its sum has absolute value at most90, giving Sigma<=-152. Without a10-word, the three coefficients have absolute value at most81, giving Sigma<=244. Thus ALWAYS m<=197.

**s7, relation dimension3.** If a10-word is present there are THREE such complementary pairs. The same bounds give Sigma<=244+3*72=460 for its negative sign, or<=-242+3*90=28 for its positive sign. Hence m<=209. Without a10-word, write n4,n6,n8 for the seven nonzero word counts. Their total weight is4 times the active coordinate count, at most44. Thus n6+2n8<=8, and

```text
Sigma<=1+9n4+27n6+81n8
      =64+18n6+72n8<=352,
```

so m<=200. This exhausts all actual relation codes/signs, with no unrelated word choices presented as a witness.

Every case has m<=209<218. Therefore ENTIRE L11 is excluded at BOTH d120/136.

## 6. L12: complete high-dimensional relation analysis

Now m>=225 at d120 or>=219 at d136, and s7 or8 by(10). For k12,

```text
m=(4096-Sigma)/24.                                     (12)
```

Nonzero relation weights are4,6,8,10 or12.

### 6.1. Affine dimension8, relation dimension3

If J12 (the all-ones word) is present, the other six words form three pairs of weights4/8 or6/6. With x=e(J12), the base is1+729x. For x=+1 each pair contributes at least-90, hence Sigma>=460. For x=-1 each pair contributes at least-72, hence Sigma>=-944. In either case m<=210.

Without J12, there are at most THREE10-words. Their missing2-sets are pairwise disjoint; otherwise two would differ in forbidden weight2. Any four such10-words would be independent (no subset of sizes1/2/3/4 has zero sum), impossible in dimension3.

- Three10-words are independent and the remaining four words have weights4,4,4,6. With their three signs x,y,z,
  Sigma=1-243(x+y+z)+9(xy+xz+yz)-27xyz, minimum-728; hence m<=201.
- Two10-words give subgroup contribution at least-476; the remaining four terms have absolute value<=81, hence Sigma>=-800 and m<=204.
- One10-word gives Sigma>=1-243-6*81=-728, hence m<=201.
- No10-word gives Sigma>=1-7*81=-566, hence m<=777/4.

Thus ALL dimension8 cases have m<=210, below the actual minimum219.

### 6.2. Affine dimension7, relation dimension4, NO J12

There are at most FOUR10-words: their missing2-sets are disjoint, and FIVE would sum to a forbidden weight2 word. We exhaust their number r.

**r4.** They are independent and generate the relation code. Subset sizes1,2,3,4 have weights10,4,6,8. Thus

```text
Sigma=1-243 sum x_i+9 sum_(i<j)x_ix_j
          -27 sum_(i<j<k)x_ix_jx_k+81x1x2x3x4.
```

The value depends only on the number of negative x_i; its five values are-944,-512,64,352,1216. Hence m<=210.

**r3.** The three10-words generate a3-dimensional subgroup with minimum Sigma contribution-728, as in6.1. It uses ALL12 coordinates: each coordinate is missed by at most one of those three words. Consequently every coset of this subgroup has average word weight6. The remaining coset has eight words of weights4/6/8, so n4=n8<=4 and the sum of absolute coefficient values is

```text
9n4+27n6+81n8<=360.
```

Therefore Sigma>=-1088 and m<=216.

**r2.** Their2-dimensional subgroup also uses all12 coordinates and contributes at least-476. Each of the other THREE cosets has four words of weights4/6/8 and average weight6, hence n4=n8<=2 and absolute coefficient sum<=180. Thus Sigma>=-1016 and m<=213.

**r1.** Pair every remaining word with its sum with the10-word. The seven pairs have weights(4,6),(4,8),(6,6) or(6,8), since the two positions outside the10-word permit exactly those possibilities after forbidden2/10/12 are removed. For positive10-word sign, each pair sum has absolute value<=90, giving Sigma>=-242-7*90=-872 and m<=207. For negative sign each pair difference has absolute value<=108, giving Sigma>=244-7*108=-512 and m<=192.

**r0.** All fifteen words have weights4/6/8. Their total weight is8 times the active coordinate count, at most96, giving n6+2n8<=18. Thus

```text
Sigma>=1-(135+18n6+72n8)>=-782,
m<=813/4.
```

Therefore EVERY code without J12 gives m<=216, below219. This includes all actual sign characters, not just positive signs.

### 6.3. Affine dimension7 WITH J12

There are SEVEN complementary pairs of weights4/8 or6/6; a10-word is impossible because its complement has weight2. If x=e(J12)=+1,

```text
Sigma>=730-7*90=100.
```

If x=-1,

```text
Sigma>=-728-7*72=-1232,
m<=222.                                                (13)
```

At d120 the minimum225 is impossible. Thus ENTIRE full-rank d120/L12 is excluded.

At d136, m is even (support in a7-flat) and m≡L≡0mod3, so it is a multiple of6. The interval219<=m<=222 leaves ONLY

```text
d136,L12,m222,u26,w_R100,s7.                            (14)
```

The last two values are from the ACTUAL occupancy identity, not a new independent R count choice. Equality in(13) forces ALL seven complementary pairs to have weights4/8, EVERY4-word sign positive, EVERY8-word sign negative, and e(J12) negative.

## 7. Intrinsic reconstruction of the remaining support/sign class

Let R4 be the seven4-words together with0. Two distinct4-words cannot sum to an8-word: their actual sign product is positive but every8-word sign is negative. They cannot sum to12 by weight. Thus their nonzero sum is again a4-word, so R4 is a3-dimensional subcode whose seven nonzero words all have weight4.

Elementary column inversion for a constant-weight binary3-dimensional code shows that each nonzero3-column occurs once: for a nonzero dual label, the inversion of its seven equal weights4 gives multiplicity1. Hence this is the length7 simplex code, supported on seven of the twelve positions and zero on the other five. The full relation code is its span with J12.

For the ACTUAL seven corresponding signed support points, the augmented point matrix has rank4; the seven distinct points therefore occupy ALL BUT ONE point a of an affine3-cube. Their actual signs extend to an affine character on that cube, since every relation product is positive. Let the remaining five support points be b1,...,b5. The full J12 relation and its negative sign give

```text
b1+...+b5=a,
(product of all12 actual delta signs)=-1,
affine dimension of the ENTIRE twelve-point union=7.   (15)
```

The XOR of the seven cube points is a because the XOR of all eight cube points is0. This is a classification of every remaining ACTUAL signed support, not a declaration that such a class completes the prescribed spectra. It includes the common quadratic D, all signs and all phase requirements in the next section.

## 8. Same-object completion attempt and exact first unproved step

The actual support7-flat L0=a0+K is automatically coisotropic: its orthogonal T0 is a1-space contained in K. On it

```text
C=2J, J=H7 z_local,
wt(z_local)=m/2=111 ODD.                                (16)
```

Let eta=(-1)^((J-1)/2), an affine character, J_can=eta*J≡1mod4, qtilde=(J_can-1)/4, and q_J=qtilde mod2=(J²-1)/8mod2, a quadratic. Set gamma=chi*eta and c=F/chi, constant on T0 fibres. Then the actual S congruence is

```text
T=c+2gamma+8gamma*qtilde≡4mod16.                        (17)
```

Modulo8 this forces gamma to be T0-periodic; modulo16 it forces q_J to be T0-periodic as well. Thus T0 is in the radical of the polar form of q_J AND its affine derivative along T0 is zero. These are real phase constraints on the signed111-array, not independent stream choices.

Write qtilde=q_J+2wtilde, w=wtilde mod2. Then

```text
h=(c+2gamma+8gamma*q_J-4)/16 is integer/T0-periodic,
kappa|L0=h+w mod2.                                     (18)
```

For a generator t of T0, D_tkappa is0 off L0 and D_tw on L0. Since deg kappa<=4, its derivative has degree<=3. A degree<=3 Boolean function supported on one affine hyperplane is its indicator times a quadratic extension. Adapt coordinates so t=u4 and L0 fixes v4. Comparing its cubic top to the REQUIRED Pfaffian derivative in(1) gives

```text
D_tkappa=1_L0*g,
[g]_2=u1v1+u2v2+u3v3,                                 (19)
```

a NONDEGENERATE rank6 quadratic on the six-dimensional quotient L0/T0. Hence the ACTUAL higher local Walsh carry w in(18) must have exactly this nondegenerate derivative. We have not proved that impossible or constructed it. We do NOT assume an unjustified degree bound for w itself.

The R side simultaneously remains the ACTUAL same-coordinate p=D+2Etilde with

```text
Hp=64a, a ternary,
E=Etilde mod2 degree<=4, [E]_4=Pf4(B_D),
z=#{p0} even>=12, c1=#{|p|1}, z+2c1=26,
p(0)=0, pmod2=D,
p in{0,±2} on D0, p in{±1,±3} on D1,
```

and its phase must satisfy the actual canonical K2 relation with the S carry, not just agree on these counts. In the raw exact formulation the full R_D equation and norm

```text
beta star beta+delta star delta+chi star delta+chi star chi=e0
```

overF3[G] remain required at ALL256 positions. They enforce INTEGER a²+B²=1 and BOTH Boolean inverse spectra. ALL512 values are still

```text
F(x,0)=(1-B(x)-a(x))/2,
F(x,1)=(1+B(x)-a(x))/2.
```

Thus the exact first unproved step is completion/noncompletion of the actual signed cube-minus-point plus five-point class(15) with(16)-(19), the prescribed D/q, SAME beta/common carries and all512 Boolean values. No actual beta/p/w/truth table satisfying these conditions has been supplied. This is an explicitly coupled attempt/barrier, not a magnitude-only witness or a whole d136/L12 verdict.

## 9. Imports, exact scope and process

This successor consumes v2 in FULL, including its universal R-next-bit Pfaffian proof, ACTUAL canonical K2 carry, zero-moment inverse-polar matrix/Arf argument, physical-fibre derivation and small-affine-flat obstruction. It also consumes the full ordinary original canonical necessity and the205LF all-rank raw/norm/Boolean/occupancy manuscript SHA842bb4e629153bebb6c04d5041d96bedaf45ae341cd2e3c2d63a96a0b9cc86bf. The NEW local even-parity/coisotropic/noncoisotropic6-flat, signed11/12 relation-code exhaustion and actual twelve-point class/phase arguments are all written above. No executable table, prior signed8-classification or rank2 accepted union is a correctness premise for the new theorems. Their historical assurance/imports remain unchanged, not minimized by fiat.

Exact new scope: universal full-rank6-flat obstruction; ENTIRE full-rank L11; ENTIRE d120/L12; strict actual d136/L12 coupled residual. Combined with v2 one has new WRITTEN candidates for ENTIRE L9/L10/L11, but NOT a newly accepted combined frontier or the unrestricted original problem. Larger L, other intrinsic types, actual Boolean/code witness and global NL242 remain OPEN. Full raw system/Boolean map is not itself a proof that a residual is empty or a realized witness.

The author may request a NEW prospective entire union audit of these literal bodies and all named canonical antecedents. A prior rank4/rank6 gate/request does not include this source, and an old L9 partial read/review cannot clear this successor. No formal/kernel/configured-family/human/executable/triple-finite/novelty/SOTA upgrade follows.

All reasoning after actual v118-D RETURN and whole031 ACK WRITTEN+SENT; held leads checkpointed BEFORE any future opaque pause. Own v112 exactness/ENTIRE ZERO withdrawn unrelated RQLS scout/no-guidance, documentary14-not15, older cadence/v105 false quotation and all parent/owner read/freeze/root/ACK/inventory/admission/exit findings remain. Exact written work/static source/metadata/own-root outputs only, no scientific execution. Same18/HOLD/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38. Original research CONTINUES, not an early final park or global clean-thought/runtime census.
