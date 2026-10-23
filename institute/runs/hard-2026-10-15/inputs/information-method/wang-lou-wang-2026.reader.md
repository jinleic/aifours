URL: https://arxiv.org/pdf/2610.17871
Content-Type: text/markdown
Method: arxiv
Notes: Fetching PDF for full content...; PDF converted via markit

---

# The Covering Radius of the Reed--Muller Code RM(1,9) is 242

**Authors:** Qichun Wang, Yueying Lou, Zifan Wang
**Published:** 2026-10-13
**Categories:** cs.IT
**arXiv:** 2610.17871

---

## Abstract

What is the covering radius of the Reed--Muller code RM(1,9) ? This is a long-standing open problem in cryptography and coding theory. In this paper, we resolve this problem, and prove that the covering radius of RM(1,9) is 242. We exclude nonlinearity 244 by obtaining a cubic Boolean function achieving a sharp Walsh $\ell^1$ bound. Its equality cases reduce either to an impossible cubic hyperplane restriction or to two homogeneous cubic forms in the Brier--Langevin classification. To exclude nonlinearity 243, we deduce the inequality ${\Vert W_g\Vert }_{1}+2|W_g(0)|\le 10368$, and then reduce either to a spectrum bounded by 24 or to the same expression to be at least 10496.

---

## Full Paper

<!-- Page 1 -->

## The Covering Radius of the Reed–Muller Code RM(1,9) is 242

#### Qichun Wang <sup>∗</sup>, Yueying Lou<sup>†</sup> and Zifan Wang<sup>‡</sup>

Abstract What is the covering radius of the Reed–Muller code RM(1,9) ? This is a long-standing open problem in cryptography and coding theory. In this paper, we resolve this problem, and prove that the covering radius of RM(1,9) is 242. We exclude nonlinearity 244 by obtaining a cubic Boolean function achieving a sharp Walsh *ℓ¹* bound. Its equality cases reduce either to an impossible cubic hyperplane restriction or to two homogeneous cubic forms in the Brier–Langevin classification. To exclude nonlinearity 243, we deduce the inequality *∥W<sub>g</sub>∥<sub>1</sub>* + 2*|W<sub>g</sub>*(0)*|≤* 10368, and then reduce either to a spectrum bounded by 24 or to the same expression to be at least 10496.

Keywords: Boolean functions, nonlinearity, Walsh transform, Reed– Muller codes, cubic forms.

### 1 Introduction

Boolean functions play an important role in both cryptography and coding theory [2, 14]. The covering radius of RM(1,*m*) is the maximum nonlinearity of *m*-variable Boolean functions, which is known for *m* even. In 1980, Mykkeltveit proved that the covering radius of RM(1, 7) is 56 [15]. Hou

# arXiv:2610.17871v1 [cs.IT] 13 Oct 2026

then gave a simpler proof for this in [9]. However, despite more than four decades of effort, the covering radius of RM(1,9) has yet to be resolved. The general upper bound for RM(1, 9) is 244. In 1996, Hou proved that the covering radius of RM(1, 9) in RM(4, 9) is 240 [10]. For *r ≥* 5, the

<sup>∗</sup>School of Computer and Electronic Information/School of Artificial Intelligence, Nanjing Normal University, Nanjing, China. Email: qcwang@fudan.edu.cn. <sup>†</sup>School of Computer and Electronic Information/School of Artificial Intelligence, Nanjing Normal University, Nanjing, China. Email: 232212001@njnu.edu.cn. <sup>‡</sup>Nanjing Foreign Language School, Nanjing, China. Email: 114064796@qq.com.

<!-- Page 2 -->

covering radius of RM(1, 9) in RM(*r*, 9) is also still unknown. There are 9- variable Boolean functions with nonlinearity 242 in the generalized rotation symmetric class [12, 13], thus the covering radius of RM(1,9) is between 242 and 244. For odd *m >* 9, the covering radius of RM(1,*m*) is completely open. Asymptotically, the lower bound for the covering radius of RM(1,*m*) is es- sentially as large as the classical upper bound [17]. For more results on the covering radius of RM(*r,m*), we refer to [4, 5, 6, 7, 8, 18]. The purpose of this paper is to determine the covering radius of RM(1,9), and prove the following theorem.

Theorem 1. *For every 9-variable Boolean function f,*

*nl*(*f*) *≤* 242*.* (1)

*Equivalently, the covering radius of RM(1,9) is 242.*

We exclude nonlinearity 244 through obtaining a cubic Boolean function achieving a sharp Walsh *ℓ¹* bound with two equality cases. One case is elim- inated by eight-variable restrictions. In the other, a residue duality imposes two explicit conditions on the homogeneous cubic part. The classification of Brier and Langevin [1, 3] leaves only two nonzero forms. For both forms, the reciprocity equations reduce them to finitely many normal forms, and each normal form has a Walsh coefficient of absolute value at least 80. For nonlinearity 243, we deduce the inequality *∥W<sub>g</sub>∥<sub>1</sub>*+2*|W<sub>g</sub>*(0)*|≤* 10368, and then either lead back to the previously excluded spectrum, or give a numerical contradiction with a gap of 128. The rest of the paper is organized as follows. In Section 2, the necessary background is established. We obtain a cubic Boolean function achieving a sharp Walsh *ℓ¹* bound in Section 3, and exclude nonlinearity 244 in Section

4. In Section 5, we exclude nonlinearity 243 and prove the main theorem. We end in Section 6 with conclusions.
### 2 Preliminaries

Let F₂<sup>m</sup> be the *m*-dimensional vector space over the binary finite field F₂. A Boolean function of *m* variables is a map from F₂<sup>m</sup> to F₂. We denote by B<sub>m</sub> the set of all *m*-variable Boolean functions. We identify a Boolean function *f* with its unique squarefree polynomial over F₂; its degree, denoted by deg(*f*), is the degree of that polynomial. A

<!-- Page 3 -->

Boolean function is affine if its degree is at most one. A “cubic” function throughout this paper has degree at most three. <sup>I</sup> Q For *I ⊆* [*m*] = *{*1*,...,m}*, write *x* = *i∈I* *x<sub>i</sub>*. Polynomial sums are over F₂ unless an integer-valued expansion is explicitly indicated. Let *f ∈* B<sub>m</sub>. the Hamming weight of *f*, denoted by *wt*(*f*), is the number of inputs at which *f* takes the value 1. The function *f* is balanced if *wt*(*f*) = 2<sup>m−1</sup>. Let *f,g ∈* B<sub>m</sub>. The Hamming distance between *f* and *g* is *d*(*f,g*) = *wt*(*f* +*g*). The nonlinearity of *f*, denoted by *nl*(*f*), is its minimum Hamming distance from the set of affine Boolean functions. For a real function *f* on F₂<sup>m</sup>, the Fourier-Hadamard transform of *f* is the integer-valued function over F₂<sup>m</sup> defined by X *H<sub>m</sub>f* (*ω*) = *f* (*x*)(*−*1) *ω·x* *.* *x∈*F*m* 2 P Writing (*f₁,f₂*) = <sup>m</sup> <sup>x</sup> *f₁*(*x*)*f₂*(*x*), character orthogonality gives *H²<sub>m</sub>* = 2 *I*, P <sup>m</sup> P 2 <sub>ω</sub>(*H<sub>m</sub>f*)(*ω*)² = 2 <sub>ω</sub> *f* (*ω*), and (*H<sub>m</sub>f₁,f₂*) = (*f₁,H<sub>m</sub>f₂*) [2]. The Walsh transform of *f ∈* B<sub>m</sub> is the function *W<sub>f</sub>* = *H<sub>m</sub>*(*−*1)<sup>f</sup>. Parseval gives X *W<sub>f</sub>* (*a*)² = 2<sup>2m</sup>*.* *a* Clearly, the nonlinearity of *f* can be determined by

<sup>m−1</sup> <u>1</u> *nl*(*f*) = 2 *− ∥W<sub>f</sub> ∥* *∞* *.* 2

By the Parseval formulae, every 9-variable Boolean function has a *∥W<sub>f</sub> ∥* *∞* at least 24, and its nonlinearity is upper bounded by 244. The Reed–Muller code RM(*d,m*) consists of the truth tables of all *m*- variable Boolean functions of degree at most *d*. The covering radius of a binary code *C* is the maximum, over all binary words of its length, of their minimum Hamming distance to *C*. It is known that RM(*d,m*) has minimum Hamming distance 2<sup>m−d</sup> [2, 11, 16], which we state as the following lemma.

Lemma 1. *An m-variable nonzero Boolean function of degree at most d has* *weight at least* 2<sup>m−d</sup>*, where d ≤ m.*

Below, inner products and norms are unnormalized sums over their indexing sets.

<!-- Page 4 -->

### 3 Reducing to a cubic form problem

Lemma 2. *Let f ∈* B<sub>m</sub>*. Its Walsh transform has the integer expansion* X X *W<sub>f</sub>* (*a*) = (*−*2) *|I|* *a<sup>I</sup>* (*−*1)<sup>f(x)</sup>*.* (2) *I⊆*[*m*] *x*: *xi*=1 (*i∈I*)

*In particular, for m* = 9*, if W<sub>f</sub> ≡ c* (mod 2<sup>r</sup>) *and* 2 *≤ r ≤* 4*, then*

<u>W<sub>f</sub> − c</u> deg <sup>r</sup> mod 2 *≤ r −* 1*.* (3) 2

*Proof.* Clearly,

X X Y *m* *W<sub>f</sub>* (*a*) = (*−*1)<sup>f(x)+</sup> *a·x* = (*−*1)<sup>f(x)</sup> (1 *−* 2*a<sub>i</sub>x<sub>i</sub>*)*.* *x x i*=1 Q Expanding <sub>i</sub>(1*−* 2*a<sub>i</sub>x<sub>i</sub>*) proves (2). For nonempty *I ⊂* [9], the inner sum of

(2) is even, so the corresponding coefficient is divisible by 2
*|I|* <sup>+1</sup>. If *W<sub>f</sub> − c* is pointwise divisible by 2<sup>r</sup>, then all its integer multilinear coefficients are divisible by 2<sup>r</sup>. By (2), for *m* = 9 and *r ≤* 4, after division, every coefficient of degree at least *r* is even, and the result follows.

Lemma 3. *If f ∈* B<sub>m</sub> *with* deg(*f*) *≤* 3*, then*

2 *⌈m/*3*⌉* *| W<sub>f</sub>* (*a*) (*a ∈* F₂<sup>m</sup>)*.* (4)

#### For a cubic g ∈ B₉:

*1.* 8 *| W<sub>g</sub>, and W<sub>g</sub>* mod 16 *is constant;*
*2. W<sub>g</sub>* mod 32 *has integer multilinear degree at most 1, with nonconstant* *coefficients divisible by 16;*
*3. W<sub>g</sub>* mod 64 *has integer multilinear degree at most 3.*
*For a cubic on 8 variables, its Walsh transform is divisible by 8 and is* *constant modulo 16.*

*Proof.* Apart from a constant sign, (*−*1)<sup>f(x)+</sup> *a·x* is a product of factors 1 *−* 2*M* (*x*), where each *M* is a monomial of degree at most 3. A term selecting *j* factors and involving *e* distinct variables contributes to the sum over *x* a multiple of 2<sup>j+m−e</sup>. Since *e ≤* min(3*j,m*),

*j* + *m − e ≥* max(*j,m −* 2*j*) *≥⌈m/*3*⌉.*

<!-- Page 5 -->

This proves (4), including restrictions of *f*. Apply this fact to each restricted function in (2). A coefficient indexed by *I* is divisible by 2 *|I|*+*⌈*(*m−|I|*)*/*3*⌉*

*.* (5)
For *m* = 9, the exponent is at least 4 when *|I|≥* 1, at least 5 when *|I|≥* 2, and at least 6 when *|I|≥* 4. For *m* = 8, it is at least 3 at *I* = ∅ and at least 4 when *|I|≥* 1.

Proposition 1. *Let f ∈* B₉ *be with ∥W<sub>f</sub> ∥* *∞* = 24*. Then its spectrum* *satisfies* *W<sub>f</sub> ≡* 8 (mod 16)*, W<sub>f</sub>* (*a*) *∈{±*8*, ±*24*},* (6)

*with 64 coefficients of magnitude 8 and 448 of magnitude 24. Moreover,*

*g* = (*W<sub>f</sub> −* 8)*/*16 mod 2 (7)

*is cubic, and* ((*−*1)<sup>f</sup>*,W<sub>g</sub>*) = (*W<sub>f</sub>,* (*−*1)<sup>g</sup>) = *−*10240*.* (8)

*Proof.* Clearly, 4 *| W<sub>f</sub>*. By Lemma 2, *W<sub>f</sub> /*4 mod 2 is affine. If it is constantly one, every magnitude is at most 20. If it is balanced, the mean square is at most (20<sup>2</sup> + 24<sup>2</sup>)*/*2 = 488 *<* 512. Hence it is zero, and 8 *| W<sub>f</sub>*. Now *q* = *W<sub>f</sub> /*8 mod 2 is quadratic. If *q ̸*= 1, Lemma 1 applied to 1 + *q* gives at least 128 zeros of *q*. On them *|W<sub>f</sub> |≤* 16, so X *W<sub>f</sub>* (*a*)² *≤* 128 *·* 16<sup>2</sup> + 384 *·* 24<sup>2</sup> = 253952 *<* 2<sup>18</sup>*.* *a*

Thus *q* = 1, proving (6). Parseval fixes the two multiplicities. Lemma 2 makes (7) cubic. Pointwise, (*−*1)<sup>g</sup>*W<sub>f</sub>* = 8 on the 64 small positions and (*−*1)<sup>g</sup>*W<sub>f</sub>* = *−*24 elsewhere. Their sum is *−*10240, and the result follows.

By Propostion 1, if *f ∈* B₉ and *∥W<sub>f</sub> ∥* *∞* = 24, then *g ∈* B₉ is cubic, and *∥W<sub>g</sub>∥<sub>1</sub>* = 10240. The next result controls both the size of a cubic Walsh transform in *ℓ¹* and the form of its equality cases.

Theorem 2. *If g ∈* B₉ *is cubic, then*

*∥W<sub>g</sub>∥<sub>1</sub> ≤* 10240*.* (9)

*Equality holds only in one of the following two cases:*

*(A) W<sub>g</sub>*(*x*) *∈{±*16*, ±*48*} for every x;*

<!-- Page 6 -->

*(B) on an affine hyperplane E, W<sub>g</sub>*(*x*) = *±*16*; off E, exactly 192 entries* *are ±*32 *and the other 64 are zero.*
*Proof.* By Lemma 3, 8 *| W<sub>g</sub>* and *W<sub>g</sub>* mod 16 is constant. Suppose first that *W<sub>g</sub> ≡* 8 (mod 16). By Lemma 3, *W<sub>g</sub>/*8 *≡* 1 + 2*ℓ* (mod 4) for an affine Boolean function *ℓ*. Then we have

*z<sub>x</sub>* = (*−*1)<sup>ℓ(x)</sup>*W<sub>g</sub>*(*x*)*/*8 *≡* 1 (mod 4)*.* (10)

Walsh inversion and Parseval imply X X *z<sub>x</sub>* = *±*64*, z²<sub>x</sub>* = 4096*.* (11) *x x* For integers *z ≡* 1 (mod 4), define

<u>3z² − 2z + 15</u> Φ(*z*) =*.* (12) 16 Then *|z|≤* Φ(*z*). Indeed, for positive *z* the difference has numerator 3(*z −*

1)(*z −*5); for negative *z* its numerator is (3*z*+5)(*z*+3). Both are nonnegative on the specified progression. Therefore,
X <u>3 · 4096 + 128 + 15 · 512</u> Φ(*z<sub>x</sub>*) *≤* = 1256*,* (13) 16 *x* P and *∥W<sub>g</sub>∥<sub>1</sub>* = 8 <sub>x</sub> *|z<sub>x</sub>|≤* 10048 *<* 10240. It remains that 16 *| W<sub>g</sub>*. Put *k* = *W<sub>g</sub>/*16. Then by the Parseval formulae and Lemma 3, X *k²<sub>x</sub>* = 1024*, k* mod 2 is affine*.* (14) *x* For even integers *k* and odd integers *j*, we have

*|k|≤ k²/*2*, |j|≤* (*j²* + 3)*/*4*.* (15)

If the parity is constantly even, these inequalities give *∥W<sub>g</sub>∥<sub>1</sub> ≤* 16*·*1024*/*2 = P

8192. If it is constantly odd, we have *|k<sub>x</sub>|≤* (1024 + 3 *·* 512)*/*4 = 640, with equality only at *k<sub>x</sub> ∈{±*1*, ±*3*}*, which is case (A). If the parity is nonconstant, then exactly 256 entries are odd. Let *A* be the squared sum on those entries. Then *A ≥* 256, and by (15),
X *A* + 3 *·* 256 1024 *− A A* *|k<sub>x</sub>|≤* + = 704 *− ≤* 640*.* (16) 4 2 4 *x* Equality requires all odd entries to be *±*1 and all even entries to be in *{*0*, ±*2*}*. Equation (14) gives 192 nonzero even entries and 64 zeros, and the result follows.

<!-- Page 7 -->

### 4 Excluding nonlinearity 244

Throughout this section, we assume that *f* has Walsh transform satisfying *∥W<sub>f</sub> ∥* *∞* = 24. Theorem 2 and (8) force equality in (9). In addition,

(*−*1)<sup>f(x)</sup> = *−*sgn(*W<sub>g</sub>*(*x*)) whenever *W<sub>g</sub>*(*x*) *̸*= 0*.* (17)

#### 4.1 Eliminating case (B) of Theorem 2

We eliminate case (B) of Theorem 2 first.

Lemma 4. *The function f has no restriction of degree at most three to an* *affine hyperplane of V.*

*Proof.* An affine change of variables preserves the set of absolute Walsh values, so let the hyperplane be a coordinate slice. Let *A* and *B* be the 8-variable Walsh transforms of its two restrictions. For each frequency,

*A* + *B, A − B ∈{±*8*, ±*24*}, |A|* + *|B|≤* 24*.* (18)

If the first restriction is cubic, by Lemma 3, *A ≡* 0 or 8 (mod 16). In the first case, (18) gives *A ∈{*0*, ±*16*}*. Parseval forces *|A|* = 16 at every frequency, then by (18), *|B|* = 8 everywhere, impossible. In the second case, *A ∈ {±*8*, ±*24*}*. Parseval gives 96 entries of magnitude 24 and 160 of magnitude eight. Equation (18) forces *B* = 0 on the P former and *|B|≤* 16 on the latter. Thus *B² ≤* 160 *·* 16<sup>2</sup> = 40960 *<* 256<sup>2</sup>, again impossible.

Proposition 2. *Case (B) of Theorem 2 cannot arise from f.*

*Proof.* Let *k* = *W<sub>g</sub>/*16 and let *q* = *k* mod 2 be its affine Boolean parity, so the affine hyperplane *E* = *{q* = 1*}*. The Boolean function

*r* = (*k − q*)*/*2 mod 2 (19)

has degree at most three. Indeed, Lemma 3 ( the last assertion) gives an integer expansion of *k* mod 4 of degree at most three. An affine Boolean function has integer degree at most two modulo 4, as follows from expanding its parity expression. Finite differences permit coefficientwise division of *k−q* by two, proving the claim. On *E*, *k* = *±*1, hence by (19), *k* = (*−*1)<sup>r</sup>. Equation (17) now gives *f* = 1 + *r* on *E*, contradictory to Lemma 4.

<!-- Page 8 -->

#### 4.2 Eliminating case (A) of Theorem 2

In case (A), define *h* = (*W<sub>g</sub>/*16 *−* 1)*/*2 mod 2*.* (20)

By Lemma 3, *h* is cubic. For *k* = *W<sub>g</sub>/*16 *∈{±*1*, ±*3*}*, direct substitution in (17) gives *k* = (*−*1)<sup>h+1</sup>*−*2(*−*1)<sup>f</sup>. Applying the Fourier-Hadamard transform *H₉* yields *W<sub>h</sub>* = *−*32(*−*1)<sup>g</sup> *−* 2*W<sub>f</sub>.* (21)

The right side equals *−*48(*−*1)<sup>g</sup> at the 64 positions with *|W<sub>f</sub> |* = 8, and 16(*−*1)<sup>g</sup> at the other positions. Therefore,

(*W<sub>h</sub>/*16 *−* 1)*/*2 mod 2 = *g.* (22)

Thus the residue operation in (20) takes *g* to *h* and then returns to *g*. P For a homogeneous cubic *P* = *|I|*=3 *p<sub>I</sub>XI*, define another homogeneous cubic *J*(*P*) by (the coefficient of *XI* in *J*(*P*)) X [*XI*]*J*(*P*) = *p<sub>A</sub>p<sub>B</sub>,* (23) *{A,B}*: *A∪B*=[9]*\I* *|A|*=*|B|*=3

and define X *C*(*P*) = *p<sub>A</sub>p<sub>B</sub>p<sub>D</sub>.* (24) *{A,B,D}*: *A∪B∪D*=[9] *|A|*=*|B|*=*|D|*=3 Both sums are over unordered partitions and take values in F₂.

Lemma 5. *If P is the homogeneous cubic part of the function g obtained* *above, then* *J*(*J*(*P*)) = *P, C*(*P*) = 0*.* (25)

*Proof.* For *|I|* = 3, the coefficient of *a<sup>I</sup>* in the integer expansion of *W<sub>g</sub>* is P *−*8 <sup>g(x)</sup> *x* *i* =1 (*i∈I* <sub>)</sub>(*−*1). To obtain the cubic coefficient of *h* in (20), divide by 32 and reduce modulo 2. This is, up to an irrelevant sign, the 6-variable restricted Walsh sum divided by 4, modulo 2. In the product expansion used in Lemma 3, the only contributions to that restricted sum modulo 8 select two disjoint cubic monomials covering the 6 free variables. Therefore the homogeneous cubic part of *h* is exactly *J*(*P*). Applying the same argument to (22) proves *J*(*J*(*P*)) = *P*. For a 9-variable Walsh sum modulo 16, the only contributing selections consist of three disjoint cubic monomials covering all 9 variables. Thus, for every frequency *x*, *W<sub>g</sub>*(*x*)*/*8 *≡ C*(*P*) (mod 2)*.* (26)

<!-- Page 9 -->

Since 16 *| W<sub>g</sub>* in case (A), we have *C*(*P*) = 0.

The classification of *RM*(3*,*9)*/RM*(2*,*9) under *GL*(9*,*2) is completely known. So, using (25), we can reduce the problem to a finite verification. In fact, Brier and Langevin classify the 349 orbits of *RM*(3*,*9)*/RM*(2*,*9) under *GL*(9*,*2) [1]. We use their published representative list [3], with its original indexing, including the zero form at index 349. For *A ∈ GL*(9*,*2), replace *g*(*a*) by *g*(*Aa*) and *f* (*x*) by *f* (*A<sup>−T</sup> x*). Their transforms change according to

*W<sub>f′</sub>* (*a*) = *W<sub>f</sub>* (*Aa*)*, W<sub>g′</sub>*(*x*) = *W<sub>g</sub>*(*A<sup>−T</sup> x*)*.* (27)

All preceding spectral and residue identities remain valid. We first choose *A* so that the cubic part is a listed representative, and then apply Lemma 5 to the transformed functions.

Proposition 3. *Among the 349 listed representatives, J*(*J*(*P*)) = *P holds* *precisely at indices*

#### 282, 290, 320, 326, 329, 349.

*Imposing C*(*P*) = 0*, only the representatives with indices* 282*,*290*,*349 *sur-* *vive.*

*Proof.* This is the only one time finite calculation. Represent a monomial by the 9-bit mask of its support. For each representative, evaluate (23) by switching the complementary mask for every unordered disjoint pair of present cubic monomials. Evaluate (24) by counting modulo two the unordered partitions into three present monomials. Apply the first operation twice and compare all 84 cubic coefficients. Both supplied implementations perform these operations for all 349 entries and obtain the stated lists.

The zero class 349 is also impossible. A quadratic function of rank 2*s ≤* 8 has Walsh *ℓ¹* norm 512 *·* 2<sup>s</sup> *≤* 8192, whereas (8) requires 10240. To verify the quadratic formula, reduce its quadratic part by a nonsingular linear P<sub>s</sub> substitution to *i*=1 *x<sub>2i−1</sub>x<sub>2i</sub>*. Its Walsh transform is a product of *s* two-variable transforms and 9*−* 2*s* one-variable transforms. Adding affine terms only shifts or negates the spectrum. With *ijk* denoting *x<sub>i</sub>x<sub>j</sub>x<sub>k</sub>*, the two remaining forms are

*P₂₈₂* = 125 + 145 + 345 + 346 + 137 + 248 + 349 + 569 + 789*,* (28) *P₂₉₀* = 125 + 235 + 245 + 345 + 136 + 127 + 347 + 128 + 238 + 148 + 129 + 349 + 569 + 789*.* (29)

<!-- Page 10 -->

We eliminate these two cases in Appendix A, and prove the following theorem.

Theorem 3. *Let g be a 9-variable cubic Boolean function satisfying W<sub>g</sub>*(*a*) *≡* 16 (mod 32) *for every a ∈* F₂<sup>9</sup>*, and suppose that*

<sup>2</sup> <u>W<sub>g</sub>(a) − 16</u> *T* (*g*) = *g, T* (*g*)(*a*) = (mod 2)*.* 32 *Then the cubic part of g cannot belong to class* 282 *or class* 290 *if* max<sub>a</sub> *|W<sub>g</sub>*(*a*)*|≤*

48*. Indeed, in either class one necessarily has* max<sub>a</sub> *|W<sub>g</sub>*(*a*)*|≥* 80*.* We now can conclude that there does not exist a 9-variable Boolean function with nonlinearity 244. Theorem 4. *No Boolean function on 9 variables has nonlinearity 244.* *Proof.* Proposition 1 and Theorem 2 force case (A) or (B), with (17). Proposition 2 excludes (B). In (A), Lemma 5 and Proposition 3 leave the zero form or the two forms (28) and (29). The zero form was excluded by its quadratic Walsh norm. Theorem 3 excludes both remaining forms.
### 5 Excluding Nonlinearity 243

Theorem 5. *For every cubic g ∈* B₉*, we have*

*∥W<sub>g</sub>∥<sub>1</sub>* + 2*|W<sub>g</sub>*(0)*|≤* 10368*.* (30)

*Proof.* In the case *W<sub>g</sub> ≡* 8 (mod 16), use (10)–(12). On the progression *z ≡* 1 (mod 4), we have 3*|z|−* Φ(*z*) *≤* 12*.* Indeed, for positive *z* the numerator is *−*3*z²* + 50*z −* 15, whose maximum on the progression is 192 at *z* = 9. For negative *z*, the numerator is *−*3*z²−*46*z −*15, with maximum 160 at *z* = *−*7. Therefore, by (10) and (13),

<u>∥W<sub>g</sub>∥<sub>1</sub> + 2|W<sub>g</sub>(0)|</u> X X = *|z<sub>x</sub>|* + 3*|z₀|≤* Φ(*z<sub>x</sub>*) + 3*|z₀|−* Φ(*z₀*) *≤* 1268*.* 8 *x̸*=0 *x*

This gives the stronger bound 10144 in this case. If 16 *| W<sub>g</sub>*, put *s* = *|k₀|* and apply (15) to the other entries. When the parity is constantly odd, P X <u>x</u>*̸*<u>=0</u> <u>(k²<sub>x</sub> + 3) 2<sup>10</sup> + 3 · 512 − (s² + 3)</u> 3*s* + *|k<sub>x</sub>|≤* 3*s* + *≤* 3*s* + 4 4 *x̸*=0 <u>2593 − (s − 6)²</u> = *≤* 648*,* 4

<!-- Page 11 -->

since *s* is odd. When it is constantly even,

X <u>1033 − (s − 3)²</u> 3*s* + *|k<sub>x</sub>|≤ ≤* 516*,* 2 *x̸*=0

since *s* is even. For balanced parity and odd *s*, let *A ≥* 255 be the squared sum on the other odd entries. Then X X X 3*s* + *|k<sub>x</sub>|* = 3*s* + *|k<sub>x</sub>|* + *|k<sub>x</sub>|* *x̸*=0 *x̸*=0*, kx odd kx even* <u>A + 765 1024 − s² − A</u> *≤* 3*s* + + 4 2 <u>(s − 3)²</u> *≤* 644 *− ≤* 644*.* 2

For balanced parity and even *s*, all 256 odd entries remain. Their squared sum is at least 256, giving

X <u>1280 − s² 1289 − (s − 3)²</u> 3*s* + *|k<sub>x</sub>|≤* 3*s* + = *≤* 644*.* 2 2 *x̸*=0

Thus the largest upper bound is 16 *·* 648 = 10368.

We now can prove the main theoreom by eleminating nonlinearity 243.

*Proof of Theorem 1.* In view of Theorem 4, it suffices to exclude *nl*(*f*) = 243, or equivalently *∥W<sub>f</sub> ∥* *∞* = 26. Now, all Walsh coefficients have a com- mon residue 2 modulo 4. By Lemma 2,

*ℓ* = (*W<sub>f</sub> −* 2)*/*4 mod 2

is affine. Multiplication of *W<sub>f</sub>* (*a*) by (*−*1)<sup>ℓ(a)</sup> corresponds to an affine transformation of *f*, and normalizes the residue to *W<sub>f</sub> ≡* 2 (mod 8). Thus we may assume *W<sub>f</sub>* (*a*) *∈{−*22*, −*14*, −*6*,*2*,*10*,*18*,*26*}.* (31)

Again by Lemma 2, *q* = (*W<sub>f</sub> −* 2)*/*8 mod 2 is quadratic. Clearly, the seven values in (31) obey

*W<sub>f</sub>* (*a*)² *≤* 4*W<sub>f</sub>* (*a*) + 252 + 320*q*(*a*)*.* (32)

<!-- Page 12 -->

If *q ̸*= 1, Lemma 1 applied to 1 + *q* gives *wt*(*q*) *≤* 384. Summing (32), we have 262144 *≤* 4 *·* 512 + 252 *·* 512 + 320 *·* 384 = 253952*,*

which is impossible. Hence *q* = 1 and

*W<sub>f</sub> ∈{−*22*, −*6*,*10*,*26*}, T* := *W<sub>f</sub> −* 2 *∈{±*8*, ±*24*}.* (33)

If *f*(0) = 0, change the value to 1 and leave all other entries fixed. The resulting Boolean function has Walsh transform *T*, contrary to Theorem 4. Therefore, *f*(0) = 1, and X *T* (*a*)² = 2<sup>18</sup> + 2<sup>10</sup> + 4 *·* 2<sup>9</sup> = 2<sup>18</sup> + 8 *·* 2<sup>9</sup>*.* (34) *a*

Together with (33), this gives exactly 56 entries of magnitude 8 and 456 of magnitude 24. Define *g* = (*W<sub>f</sub> −* 10)*/*16 mod 2 = (*T −* 8)*/*16 mod 2*.* (35)

Then *g* is cubic by Lemma 2. On the 56 small positions, (*−*1)<sup>g</sup>*T* = 8; on the other 456 positions, (*−*1)<sup>g</sup>*T* = *−*24. Thus

((*−*1)<sup>g</sup>*,T*) = 56 *·* 8 *−* 456 *·* 24 = *−*10496*.* (36) P Since *W<sub>f</sub>* = *T* + 2 and <sub>a</sub>(*−*1)<sup>g(a)</sup> = *W<sub>g</sub>*(0), symmetry of *H₉* gives

((*−*1)<sup>f</sup>*,W<sub>g</sub>*) = (*W<sub>f</sub>,* (*−*1)<sup>g</sup>) = *−*10496 + 2*W<sub>g</sub>*(0)*.*

#### Theorem 5 now yields the contradiction

10496 = 2*W<sub>g</sub>*(0) *−* ((*−*1)<sup>f</sup>*,W<sub>g</sub>*) *≤* 2*|W<sub>g</sub>*(0)*|* + *∥W<sub>g</sub>∥<sub>1</sub> ≤* 10368*.*

Hence nonlinearity 243 is impossible, and the result follows.

### 6 Conclusions

This paper determined the covering radius of the Reed–Muller Code RM(1,9). That is, the maximum nonlinearity of 9-variable Boolean functions is 242. Since the known 9-variable functions with nonlinearity 242 are not balanced, it is still an open problem to determine whether there exists a balanced 9- variable Boolean function with nonlinearity 242, which could be further considered in the future.

<!-- Page 13 -->

### Acknowledgment

The authors would like to thank the financial support from the National Natural Science Foundation of China (Grant 62172230).

### References

[1] E. Brier and P. Langevin, “Classification of Boolean Cubic Forms of Nine Variables,” in *Proc. 2003 IEEE Information Theory Workshop*, 2003, pp. 179–182.

[2] C. Carlet, “Boolean Functions for Cryptography and Coding Theory,” Cambridge University Press, 2021.

[3] E. Brier and P. Langevin, “Cubics in Nine Variables”. [Online]. Avail- able: [https://langevin.univ-tln.fr/project/cubics/](https://langevin.univ-tln.fr/project/cubics/).

[4] R. Dougherty, R. D. Mauldin, and M. Tiefenbruck, “The Covering Radius of the Reed–Muller Code *RM*(*m −*4*,m*) in *RM*(*m −*3*,m*),” *IEEE* *Transactions on Information Theory*, 68:1 (2022), 560–571.

[5] D. Elimelech, H. Wei, and M. Schwartz, “On the Generalized Covering Radii of Reed–Muller Codes,” *IEEE Transactions on Information* *Theory*, 68:7 (2022), 4378–4391.

[6] J. Gao, “Numerical Results and Asymptotic Lower Bound on the Covering Radius of Reed–Muller Codes *RM*(2*,*11) and *RM*(3*,n*),” *IEICE* *Transactions on Fundamentals*, E109-A:1 (2026), 35–46.

[7] J. Gao, H. Kan, Y. Li and Q. Wang, “The Covering Radius of the Third-Order Reed–Muller Code RM(3,7) is 20,” *IEEE Transactions on* *Information Theory*, 69:6 (2023), 3663–3671.

[8] V. Gillot and P. Langevin, “Covering Radius of *RM*(4*,*8),” *Advances* *in Mathematics of Communications*, 18:2 (2024), 383–393.

[9] X. Hou, “Covering Radius of the Reed–Muller Code R(1, 7) - A Simpler Proof,” *Journal of Combinatorial Theory, Series A*, 74:2 (1996), 337–

341.
[10] X. Hou, “The Covering Radius of R(1, 9) in R(4, 9), ” *Designs, Codes* *and Cryptography*, 8:3 (1996), 285–292.

<!-- Page 14 -->

[11] T. Kasami and N. Tokura, “On the Weight Structure of the Reed– Muller Codes,” *IEEE Transactions on Information Theory*, 16 (1970), 752–759.

[12] S. Kavut and M. D. Y¨ucel, “9-variable Boolean Functions with Nonlinearity 242 in the Generalized Rotation Symmetric Class,” *Information* *and Computation*, 208:4 (2010), 341–350.

[13] S. Kavut, S. Maitra and M. D. Y¨ucel, “Search for Boolean Functions with Excellent Profiles in the Rotation Symmetric Class,” *IEEE Transactions on Information Theory*, 53:5 (2007), 1743–1751.

[14] O. A. Logachev, A. A. Salnikov and V. V. Yashchenko, “Boolean Functions in Coding Theory and Cryptography,” American Mathematical Society, 2012.

[15] J. Mykkeltveit, “The Covering Radius of the (128,8) Reed–Muller Code is 56 (Corresp.),” *IEEE Transactions on Information Theory*, 26:3 (1980), 359–362.

[16] F. J. MacWilliams and N. J. Sloane, “The Theory of Error-correcting Codes,” North Holland, 1977.

[17] K. Schmidt, “Asymptotically optimal Boolean functions,”*Journal of* *Combinatorial Theory, Series A*, 164 (2019), 50–59.

[18] Q. Wang, “The Covering Radius of the Reed–Muller Code RM(2,7) is 40,” *Discrete Mathematics*, 342 (2019), Art. no. 111625.

### A Eliminating both remaining classes 282 and 290

<u>Wg (a)−16</u> Define *T* (*g*)(*a*) = <sup>2</sup> 32 (mod 2). We have *T* (*g*) = *g*. In the following, we will prove that classes 282 and 290 are impossible. For a cubic Boolean function *p* satisfying *W<sub>p</sub>*(*a*) *≡* 16 (mod 32), summing its defining congruences for *T* (*p*) gives (the coefficient of *x<sub>i</sub>x<sub>j</sub>* in *T* (*p*))

<u>wt(p|<sub>x</sub>i=xj=0)</u> [*x<sub>i</sub>x<sub>j</sub>*]*T* (*p*) = (mod 2)*,* (37) 4

and similarly (the coefficient of *x<sub>i</sub>x<sub>j</sub>x<sub>k</sub>* in *T* (*p*))

<u>wt(p|<sub>x</sub>i=xj=x</u> <u>k</u> <u>=0)</u> [*x<sub>i</sub>x<sub>j</sub>x<sub>k</sub>*]*T* (*p*) = (mod 2)*.* (38) 2

<!-- Page 15 -->

All coefficient calculations below may be obtained from the inclusion-exclusion identity ! X X S *wt x<sub>M</sub>* = (*−*2) *|S|−* <sup>1</sup>2<sup>m−</sup> *|M ∈SM|.* (39) *M ∈M* ∅*̸*=*S⊆M*

#### A.1 Class 282: the determinant model

Let *X* = (*x<sub>ij</sub>*) *∈ M₃*(*F₂*), and *D*(*X*) = det*X*. This cubic represents class

282. Indeed, the transformation is (*y₁,...,y₉*) = (*t₁, t₂* + *t₆, t₉, t₂, t₈,t₃* + *t₄* + *t₈, t₅, t₇, t₃*)*,* where *t₁,...,t₉* are the row-major entries of *X ∈ M₃*(*F₂*). For *A,B ∈* *M₃*(*F₂*) define
X Y *RA*(*X*) = *A<sub>ij</sub> x<sub>ik</sub>,* (40) *i,j k̸*=*j* X Y *CB*(*X*) = *B<sub>ij</sub> x<sub>kj</sub>.* (41) *i,j k̸*=*i*

By a translation and addition of an affine function, every function in this class has the form

*g*(*X*) = *GA,B*(*X*) := *D*(*X*) + *RA*(*X*) + *CB*(*X*)*.* (42)

The nine nonconstant coefficients of *W<sub>g</sub>/*16 mod 2 give nine independent linear conditions on the 36 quadratic coefficients. In determinant coordinates, the resulting kernel is the 18-dimensional space represented by *RA* + *CB*. Write cof(*A*) for the cofactor matrix, without transposing it. A direct application of (39) gives

<u>WG<sub>A,B</sub>(Y)</u> X *≡* 1 + det*A* + det*B* + *A<sub>ij</sub>B<sub>ij</sub>* (mod 2)*,* (43) 16 *i,j*

independently of *Y*. Hence,

det*A* + det*B* + *A* : *B* = 0*,* (44) P where *A* : *B* = *ij* *A<sub>ij</sub>B<sub>ij</sub>*. On the quadratic parameters, *T* induces the map

Φ(*A,B*) = *B* + cof(*A*)*, A* + cof(*B*)*.* (45)

<!-- Page 16 -->

Thus *T <sup>2</sup>*(*g*) = *g* implies Φ²(*A,B*) = (*A,B*). Define

*U ⋆V* = cof(*U* + *V*) + cof(*U*) + cof(*V*)*.*

#### Using cof(cof(A)) = (detA)A, we obtain

(det*A*)*A* + *B ⋆* cof(*A*) = 0*,* (46) (det*B*)*B* + *A⋆* cof(*B*) = 0*.* (47)

Suppose *A* is invertible. Under (*A,B*) *7−→* (*PAQ,P <sup>−T</sup> BQ<sup>−T</sup>*) we may normalize *A* = *I*. Then (46) becomes *I* + *B ⋆I* = 0*.* But

*B ⋆I* = (tr(*B*))*I* + *BT,* (48)

whose trace is zero in characteristic two, whereas tr(*I*) = 1. This is impossible. Therefore *A* is singular; by symmetry, so is *B*. Hence

rank *A,* rank *B ≤* 2*.* (49)

Since both determinants vanish, (44) gives *A* : *B* = 0*.* Transposition exchanges (*A,B*) with (*BT,AT*), so we may assume rank *A ≥* rank*B*. If rank*A* = 0, then *A* = *B* = 0. If rank*A* = 1, normalize *A* = *E₁₁*. Since rank *B ≤* 1 and *A* : *B* = 0, we have *B₁₁* = 0. Up to the stabilizer of *E₁₁* the nonzero possibilities of *B* are *E₁₂*, *E₂₁* and *E₂₂*. If rank*A* = 2, normalize *A* = *D₂* := diag(1*,*1*,*0). Equations (46)-(47) force   0 0 *u₁* *B* =0 0 *u₂**, u₁v₁* + *u₂v₂* = 0*.* (50) *v₁ v₂ b*

The stabilizer of *D₂* reduces this to *B ∈{*0*,E₃₃,E₁₃,E₃₁,E₁₃* +*E₃₂}.* Thus, up to the allowed equivalences, the complete list is

(0*,*0)*,* (*E₁₁,*0)*,* (*E₁₁,E₁₂*)*,* (*E₁₁,E₂₁*)*,* (*E₁₁,E₂₂*)*,* (51) (*D₂,*0)*,* (*D₂,E₃₃*)*,* (*D₂,E₁₃*)*,* (*D₂,E₃₁*)*,* (*D₂,E₁₃* + *E₃₂*)*.*

For these ten normal forms, direct Walsh evaluation gives Table 1. Every entry in the table is therefore an elementary finite character sum. In particular, max *|WG<sub>A,B</sub>*(*Y*)*|≥* 80 (52) *Y* for every reciprocal form in class 282. Thus class 282 is impossible whenever the Walsh spectrum is restricted to *{±*16*, ±*48*}*.

<!-- Page 17 -->

Table 1: Values of *WG<sub>A,B</sub>*(*Y*).

|A|B|Y|WG|( Y|)|
|---|---|---|---|---|---|
|||||<sub>A,B</sub>||
|0|0|0||176||
|E₁₁|0|0||112||
|E₁₁|E₁₂|0||80||
|E₁₁|E₂₁|0||80||
|E₁₁|E₂₂|0||112||
|D₂|0|0||80||
|D₂|E₃₃|0||80||
|D₂|E₁₃|0||80||
|D₂|E₃₁|E₁₂||80||
|D₂ E₁₃|+ E₃₂|E₁₂||80||

#### A.2 Class 290: the Hermitian determinant model

Let F₄ = F₂(*ω*), *ω²* = *ω* + 1, and ¯*z* = *z<sup>2</sup>*. Consider   *a z ȳ* *X* = *z b x* ¯ *, a,b,c ∈* F₂*, x,y,z ∈* F₄*.* *y x c* ¯

Its determinant is

*N* (*X*) = *abc* + *axx*¯ + *byȳ* + *czz*¯ + Tr<sub>4/2</sub>(*xyz*)*.* (53)

Its cubic part represents class 290. Indeed, the transformation is

(*y₁,...,y₉*) = (*t₃* + *t₄, t₅* + *t₇, t₅, t₄* + *t₅* + *t₆* + *t₇,t₂* + *t₃* + *t₅,* *t₁* + *t₂* + *t₅* + *t₇, t₄* + *t₆* + *t₈* + *t₉, t₅* + *t₇* + *t₉, t₃*)*,*

where (*a,b,c*) = (*t₁,t₂,t₃*), *x* = *t₄* + *ωt₅*, *y* = *t₆* + *ωt₇* and *z* = *t₈* + *ωt₉*. Use the nondegenerate symmetric pairing (*X,Y*) = tr(*XY*) *∈* F₂*.* For *A∈M₃*(F₄) define   X Y *QA*(*X*) = Tr<sub>4/2</sub>  *A<sub>ij</sub> X<sub>ik</sub>**.* (54) *i,j k̸*=*j*

After the allowed normalization, every function in this class satisfying the Walsh congruence has the form *g* = *N* + *QA.*

<!-- Page 18 -->

Put *t* = tr(*A*), *s* = tr(cof(*A*)), and *d* = det(*A*). A direct expansion gives

<u>WN<sub>+QA</sub>(Y)</u> *≡* 1 + *tt*¯+ Tr<sub>4/2</sub>(*d*) (mod 2)*,* (55) 16 so *tt* ¯ = Tr<sub>4/2</sub>(*d*)*.* (56)

The induced transformation on *A* is Φ(*A*) = cof(*A*) + *tI.* The condition *T <sup>2</sup>*(*g*) = *g* implies Φ²(*A*) = *A*. Using adj(*A*) = *A²* + *tA* + *sI,* we obtain

*tA²* + (*d* + 1 + *tt*¯)*A* + ¯*sI* = 0*.* (57)

If *t* = 0, then (56) gives *d ∈{*0*,*1*}*. If *d* = 0, equation (57) gives *A* = ¯*sI*, and taking traces forces *s* = 0, hence *A* = 0. If *d* = 1, equation (57) gives *s* = 0, so the characteristic polynomial

*χ<sub>A</sub>*(*λ*) = *λ³* + 1 = (*λ* + 1)(*λ* + *ω*)(*λ* + *ω²*)*,*

and therefore *A ∼* diag(1*,ω,ω<sup>2</sup>*)*.* If *t ̸*= 0, then *tt*¯ = 1, so *d ∈ {ω,ω²}.* Equation (57) becomes *tA²* ¯ + *dA* + ¯*sI* = 0*.* Its annihilating polynomial has nonzero derivative *d*, so *A* is semisimple. It cannot be scalar because a nonzero scalar 3 *×* 3 matrix has determinant 1. Thus its eigenvalues have multiplicities 2*,*1, and after the allowed scalar and similarity normalizations we obtain

#### A ∼ diag(ω,ω,1), A ∼ diag(ω<sup>2</sup>,ω²,1).

#### Thus only the four forms

0*,* diag(1*,ω,ω²*)*,* diag(*ω,ω,*1)*,* diag(*ω<sup>2</sup>,ω²,*1) (58)

remain. Set     1 *ω ω²* 1 0 1 *Y₁* = *ω²* 1 1 *, Y₂* = 0 1 1*.* *ω* 1 1 1 1 1

#### For A = diag(r,s,t), put

*ψ*(*x,y,z*) = Tr<sub>4/2</sub> *xyz* + *rzȳ* + *szx* ¯ + *tyx*¯ + *xū* + *yv*¯ + *zw*¯*,*

where (*u,v,w*) = (*Y₂₃,Y₃₁,Y₁₂*). Summing first over *a,b,c* gives

*WN<sub>+QA</sub>*(*Y*) = 8*S₁ −* 2*S₀,* (59)

<!-- Page 19 -->

where X *S₁* = (*−*1)<sup>ψ</sup>*,* (60) *xx*¯=*ϵ*1 *yȳ*=*ϵ*2 *zz*¯=*ϵ* X³ ¯+*yȳ*+*zz*¯+*ϵ*1+*ϵ*2+*ϵ* *S₀* = (*−*1)<sup>ψ+xx</sup> <sup>3</sup>*,* (61) *x,y,z∈*F4

and each *ϵ<sub>i</sub> ∈* F₂ is fixed. For the four normal forms in (58), with frequencies *E₁₁,Y₁,Y₂,Y₂*, respectively, direct calculation gives

(*S₁,S₀*) = (3*, −*28)*,* (7*, −*12)*,* (11*,*4)*,* (11*,*4)*.*

Hence in every case *WN<sub>+QA</sub>*(*Y*) = 8*S₁ −* 2*S₀* = 80. The elementary identity X (*Rz*)+*zz*¯ (*−*1)<sup>Tr</sup>4*/*2= 2 *−* 4 *·* 1<sub>R</sub>=0 *z∈*F4

provides a direct reduction of the character sums. Therefore

max *|WN<sub>+QA</sub>*(*Y*)*|≥* 80 (62) *Y*

for every reciprocal form in class 290. Thus class 290 is impossible whenever the Walsh spectrum is contained in *{±*16*, ±*48*}*. So, we have proved Theorem 3.