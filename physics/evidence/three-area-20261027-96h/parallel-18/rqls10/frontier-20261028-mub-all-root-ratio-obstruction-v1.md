# A Weyl/MUB candidate cannot have all relative Schmidt ratios in a root-of-unity coset

**WRITTEN + EXACT CYCLOTOMIC-CHECKED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at the new exact check: **Wed Oct 28 19:07:54 PDT 2026**. The key pair-plus-triangle geometric obstruction is proved below without any root-of-unity restriction; the ALL-roots corollary explicitly imports Lam–Leung's cited theorem. This is a necessary condition only for the fixed Weyl/diagonal-transversal ansatz, not an unrestricted QLS10 no-go.

## 1. Claim and imports

For the fixed MUB triple `I10,F10,D10 F10` and CRT formulation in `frontier-20261028-mub-triple-rank2-reduction-v1.md` SHA **ef00b5db269a3e436365b4b98fd486c32836bbda931f00bba80afcaaea5dfc8c**, a common unbiased vector has the form

`phi=(|0> tensor a+|1> tensor b)/sqrt(2)`,
`|a_t|=|b_t|=1/sqrt(5)`, `<a,b>=0`,

and `P=aa†+bb†` has diagonal2/5 in the three bases I5, U and V, where

`U_(t,j)=omega^(3tj)/sqrt(5)`, `V=D5 U`, `D5_tt=omega^(4t²)`, `omega=exp(2*pi*i/5)`.

Set the unit phases `z_t=b_t/a_t`. Orthogonality gives `sum_t z_t=0`.

**Geometric claim (self-contained §§2–4):** the five z_t cannot consist of ONE antipodal pair and ONE equilateral triple, even allowing the pair and triple to have independent arbitrary continuous phases. Earlier packet `frontier-20261028-mub-primepower-ratio-obstruction-v1.md` SHA **c78bff776a962122ca1370a4acc8ec49d0b723b268194c45330f58e541743968** excludes a rotated regular pentagon.

**ALL-root corollary (named import):** Lam and Leung prove that a minimal vanishing sum of roots of unity is a regular prime-gon or, if it is asymmetric, has weight at least6: for at most two prime factors this is their Corollary3.4, and for >=3 it follows from Lower Bound Theorem4.8 with `p1(p2-1)+p3-p2>=6`. Source: T. Y. Lam and K. H. Leung, [On vanishing sums of roots of unity](https://arxiv.org/pdf/math/9511209v1), Cor.3.4 and Thm.4.8. Decompose any vanishing sum of FIVE roots into minimal subsums: it is necessarily one regular pentagon or a 2-gon plus a 3-gon. Both are excluded. Hence no common unbiased phi can have all z_t in a single arbitrary-phase coset of ANY finite root-of-unity group. Equivalently, at least one ratio `z_t/z_s` must have an irrational phase angle modulo2pi. The corollary is conditional on that named published import; the small-weight root classification was not independently reproved here.

No conclusion is drawn about arbitrary irrational phases, other MUB triples/resolutions, or non-Weyl QLSs. If a common phi with allowed phases were found, the earlier Weyl caller would yield the original 100-ray 1-RQLS and a fourth MUB.

## 2. Normalize ANY pair-plus-triangle configuration

Assume for contradiction `{z_t}` consists of `{alpha,-alpha}` and `{beta,beta*tau,beta*tau²}`, where alpha,beta are arbitrary unit complex numbers and `tau=exp(2*pi*i/3)`. The two pair positions can be moved to t=0,1 by an affine permutation of F5. The accompanying common chirp unitary on a,b preserves I5 and permutes U,V as shown and checked in §3 of the prime-power packet; it therefore preserves the required three flat P diagonals. A common phase of b sets the pair to 1,-1. Any permutation of the three triangle vertices is achieved by absorbing a power of tau into beta and, if needed, swapping a,b (which inverts all z_t). Hence WLOG

`(z0,z1,z2,z3,z4)=(1,-1,lambda,lambda*tau,lambda*tau²)`, `|lambda|=1`.    (1)

The steps preserve P, or conjugate it by a unitary permuting the three measured bases; they do not require preserving the separate X/Y cross gates, because we will contradict the NECESSARY flat-P condition alone.

## 3. Gap one forces two possible phases

Write `p_t=sqrt(5)*a_t`, so |p_t|=1, and for h=1,2 define

`y_t^(h)=5 P_(t+h,t)=p_(t+h) conjugate(p_t) (1+z_(t+h) conjugate(z_t))`.

The flat U and V diagonals imply the exact Fourier zeros

`sum_t y_t^(h)=0`, `sum_t y_t^(h) omega^(-3 h t)=0`.          (2)

Indeed `(D5† P D5)_(t+h,t)=omega^(-4(2ht+h²))P_(t+h,t)`, and `-8h=-3h mod5`; constant factors do not affect zero. For h=1, Fourier support is `{1,2,4}`. Write

`y_t=c1 omega^t+c2 omega^(2t)+c4 omega^(4t)`.

Because z1=-z0, y0=0 and `c1+c2+c4=0`. Set

`d_k=(1/5)sum_t |y_t|² omega^(-k t)`.

Direct multiplication gives

`d1=c2 conjugate(c1)`, `d2=c1 conjugate(c4)+c4 conjugate(c2)`,
`d2+2 conjugate(d1)=-(|c1|²+|c2|²)`.                        (3)

Write lambda=exp(i theta),

`A=|1-lambda|²=2-2 cos(theta)`,
`B=|1+conjugate(lambda) tau|²=2+2 cos(theta-2pi/3)`.

Then `(|y_t|²)_t=(0,A,1,1,B)`. Taking the imaginary part of (3) gives

`(2 sin(2pi/5)-sin(pi/5))*(A-B)/5=0`.

The prefactor is positive, so A=B and `cos(theta-pi/3)=0`. Consequently theta is **5pi/6 or 11pi/6 modulo2pi**, despite lambda having been arbitrary.

## 4. Both forced phases contradict flatness

Let `g=(1+sqrt(5))/2`, `h=(sqrt(5)-1)/2`.

### 4a. theta=11pi/6

Here A=B=2-sqrt(3). The gap-one coefficients are REAL and equal

`d1=(A*h-g)/5 < 0`, `d2=(-A*g+h)/5 > 0`.

The second sign follows from `2-sqrt(3)<h/g=(3-sqrt(5))/2`, equivalent to `1+sqrt(5)<2sqrt(3)`. But (3) and AM–GM imply `d2+2d1<=-2|d1|=2d1`, i.e. d2<=0. Contradiction.

### 4b. theta=5pi/6

Use gap h=2. Equations (2) now force Fourier support `{2,3,4}`:

`y_t^(2)=c2 omega^(2t)+c3 omega^(3t)+c4 omega^(4t)`.

The squared-modulus pattern is `(2-sqrt(3),2,1,2,2-sqrt(3))`. Its coefficients `d_k=(1/5)sum_t |y_t^(2)|² omega^(-k t)` obey

`d0=|c2|²+|c3|²+|c4|²=(9-2sqrt(3))/5`,
`d1=c3 conjugate(c2)+c4 conjugate(c3)`,
`d2=c4 conjugate(c2)`.

A direct calculation gives

`conjugate(d2)*d1² < 0` (real), `|d1|+|d2|=sqrt(15)/5`.

For full reproducibility, put `A=2-sqrt(3)`,

`R1=[sqrt(5)-A*(sqrt(5)+1)/2]/5 >0`,
`R2=[-sqrt(5)+A*(sqrt(5)-1)/2]/5 <0`.

Then `d1=omega^(-2) R1`, `d2=omega^(-4) R2`, and `R1-R2=sqrt(15)/5`.

Writing `c2=p exp(i alpha)`, `c4=q exp(i beta)`, `c3=r exp(i gamma)`, the negative-real phase identity forces `d1 exp(-i(beta-alpha)/2)` purely imaginary and hence `|d1|=r|p-q|`; also `|d2|=p q`. Thus

`d0=p²+q²+r² >= 2(pq+r|p-q|)=2sqrt(15)/5`.

But `(9-2sqrt(3))/5 < 2sqrt(15)/5`, since `(9-2sqrt(3))²=93-36sqrt(3)<60`. Contradiction. Both phase branches fail, proving the geometric claim.

`frontier-20261028-pair-triangle-cyclotomic-check-v1.py`, SHA **5796170f944763e4f1bbcf50b508cf825786b96994fddc1f994368dd9f75a8db**, independently reduces the two forced phase identities and squared-modulus patterns in Q(zeta60), checks the exact R1,R2 identities, and uses elementary rational comparisons for the signs. It does not replace the continuous lambda reduction or the cited Lam–Leung theorem. The earlier symmetry checker SHA **cb340e2351b4049e9fd672b2ef03f4154d564ce1940bbaafc1929c5f9379f34** covers all1000 required affine/chirp exponent identities.

## 5. Remaining gap

The result excludes ALL finite rational relative-phase alphabets only within the specified Weyl/MUB branch, assuming the explicitly named root-sum import. It also excludes the broader continuous pair-plus-triangle geometry unconditionally from flat P. It does NOT settle the existence of a common unbiased vector with more general irrational ratios or of any non-Weyl 1-RQLS10. No source's numerical MUB conjecture, or the unsuccessful local search, is treated as a proof. Independent full mathematical review and source verification are required.
