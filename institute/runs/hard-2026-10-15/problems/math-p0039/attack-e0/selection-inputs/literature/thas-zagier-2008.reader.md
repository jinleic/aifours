URL: https://people.mpim-bonn.mpg.de/zagier/files/doi/10.4171/JEMS/107/fulltext.pdf
Content-Type: application/pdf
Method: markit
Notes: Converted with markit

---

<!-- Page 1 -->

J. Eur. Math. Soc. 10, 173–190 ©c European Mathematical Society 2008
## Koen Thas · Don Zagier

# Finite projective planes, Fermat curves, and Gaussian periods

Received October 7, 2006 and in revised form February 20, 2007

**Abstract.** One of the oldest and most fundamental problems in the theory of finite projective planes is to classify those having a group which acts transitively on the incident point-line pairs (flags). The conjecture is that the only ones are the Desarguesian projective planes (over a finite field). In this paper, we show that non-Desarguesian finite flag-transitive projective planes exist if and only if certain Fermat surfaces have no non-trivial rational points, and formulate several other equivalences involving Fermat curves and Gaussian periods. In particular, we show that a non-Desarguesian flag-transitive projective plane of order *n* exists if and only if *n >* 8, the number ∑ *p* = *n* 2 + *n* + 1 is prime, and the square of the absolute value of the Gaussian period*a*∈*D* *n* *ζ a* (*ζ* = primitive *p*th root of unity, *Dn* = group of *n*th powers in F*p* ×) belongs to Z. We also formulate a conjectural classification of all pairs *(p, n)* with *p* prime and *n* | *p* − 1 having this latter property, and give an application to the construction of symmetric designs with flag-transitive automorphism groups. Numerical computations are described verifying the first conjecture for *p <* 4 × 1022 and the second for *p <* 107.

## 1. Introduction

A finite *projective plane of order n*, where *n* ∈ N, is a point-line incidence structure satisfying the following conditions:

(i) each point is incident with (“lies on”) *n* + 1 lines and each line is incident with (“contains”) *n* + 1 points; (ii) any two distinct lines intersect in exactly one point and any two distinct points lie on exactly one line. One also traditionally requires that *n* be ≥ 2 to exclude the uninteresting cases of a single line and a point not on it (*n* = −1), a single line and one point on it (*n* = 0), or the three vertices and three sides of a triangle (*n* = 1). This is equivalent to requiring that contains an ordinary quadrangle (four points with no three on a line) as subgeometry.
K. Thas: Department of Pure Mathematics and Computer Algebra, Ghent University, Galglaan 2, B-9000 Ghent, Belgium; e-mail: kthas@cage.UGent.be
D. Zagier: Max-Planck-Institut für Mathematik, Vivatsgasse 7, D-53111 Bonn, Germany, and Collège de France, 3, rue d’Ulm, F-75005 Paris, France; e-mail: zagier@mpim-bonn.mpg.de *Mathematics Subject Classification (2000):* 51E15, 05E20, 11L05, 14G05

<!-- Page 2 -->

<u>Koen Thas, Don Zagier</u>

A *flag* of is an incident point-line pair. It is easily seen that a finite projective plane of order *n* has *n* + *n* + 1 points, *n* + *n* + 1 lines, and *(n* + 1*)(n* + *n* + 1*)* flags. The obvious examples of finite projective planes are the projective planes P 2

*(*F*)* over
finite fields F. In this case the order *n* = |F| is a prime power, and in fact no examples of finite projective planes of non-prime power order are known, though there are examples of prime power order which are not isomorphic to P 2

*(*F*)*. A classical theorem of R. Moufang
(cf. [9]) states that a finite projective plane is isomorphic to some P 2

*(*F*)* if and only if a
certain configurational property corresponding to the classical theorem of Desargues is satisfied. Projective planes of this type are therefore often called *Desarguesian*. We call a projective plane *flag-transitive* if its group of automorphisms acts transitively on the flags. Clearly Desarguesian planes have this property, since the automorphism group of the projective plane P 2

*(*F*)* over a finite field F of characteristic *p* is
the semi-direct product **P***0***L**3*(*F*)* = **PGL**3*(*F*)* Gal*(*F*/*F*p)* and already the subgroup **PGL**3*(*F*)*acts transitively on the flags. Conversely, it is an old and fundamental conjecture in the theory of projective planes, first mentioned in D. G. Higman and J. E. McLaughlin [8], that every flag-transitive finite projective plane is Desarguesian. The following theorem, which is an amalgam of results from a large number of papers in the literature (see e.g. [6]), strongly limits the possibilities for a counterexample to this conjecture.

**Theorem 1.1.** *Let be a finite flag-transitive projective plane of order n, and suppose* *that is not Desarguesian. Then*

(a) *n is even;*
(b) *the number p* = *n*
2 + *n* + 1 *is prime;*

(c) *the automorphism group* Aut*() of acts regularly (simply transitively) on the flags* *of.* Note that part (c) implies that |Aut*()*| = *(n* + 1*)(n*
2 + *n* + 1*)*, the number of flags. This is in stark contrast to the Desarguesian case, where already the subgroup **PGL**3*(*F*)* of Aut*()* has a much larger order. In fact, if is Desarguesian of order different from 2 or 8, then it is known [3] that Aut*()* contains *no* subgroup which acts regularly on the flags of.

**Remark 1.2.** In [4], W. Feit claims that if and *n* are as in Theorem 1.1, then *n* is not a power of 2, and in a recent paper [12], U. Ott claims that any flag-transitive finite projective plane has prime power order. Together with the above theorem, these two results would imply the non-existence of non-Desarguesian flag-transitive finite projective planes. Unfortunately, both proofs appear to contain mistakes: Feit uses a lemma of

B. Gordon, W. H. Mills and L. R. Welch [7] (in the proof of [4, Theorem A]) which is proved only under much more restrictive hypotheses in [7], and there is a mistake in [12] in deriving [12, formula (18)] from [12, formula (17)], as pointed out in [15]. As already mentioned, Theorem 1.1 is a combination of a collection of difficult theorems from a number of different papers, but in fact a large part of it can be deduced in one step from a later theorem of W. M. Kantor, since it is relatively easy to show that any group which acts flag-transitively also acts point-primitively. (This is a corollary of

<!-- Page 3 -->

<u>Finite projective planes</u>

a more general result in [8].) Kantor’s result, whose proof invokes the classification of finite simple groups, is as follows.

**Theorem 1.3 (W. M. Kantor [10]).** *Let be a finite projective plane of order n. Suppose that there is a group of automorphisms G which acts primitively on the points of* *and that is not Desarguesian. Then n is even, n* 2 + *n* + 1 *is prime, G is a Frobenius* *group, and* |*G*| *divides (n* + 1*)(n* 2 + *n* + 1*) or n(n* 2 + *n* + 1*).*

In the paper of Feit cited above, it is proved that under the assumptions of Theorem 1.1 every divisor *d* of *n* must satisfy *d* *n*+1 ≡ 1 *(*mod*n* 2 +*n*+1*)*, and also that *n* must be larger than 14 400 008. An elementary proof of the first assertion is given in a recent paper by the first author [14], which also contains a survey of the most important results on finite flag-transitive projective planes since 1961 and some related problems.

## 2. Classification of flag-transitive projective planes

A general construction of potential examples of finite projective planes, known in the literature as the method of *difference sets*, is as follows. Suppose we have a finite (not necessarily abelian) group *F* containing a subset *D* for which the map

*D* × *D* {diagonal} → *F* {*e*}*, (x, y)* → *xy* −1 *,* (1)

is bijective, so that |*F* | = *n* 2 + *n* + 1, where |*D*| = *n* + 1. Then we obtain a finite projective plane = *(F, D)* of order *n* by taking both the set of points and the set of lines of to be the elements of *F*, with the incidence relation that a point *x* and a line *y* are incident if and only if *yx* −1 belongs to *D*. We will be concerned with the special case of this described by the following proposition, which is essentially a restatement of a result of J. Fink [5]. Before stating it, we make two definitions. We call a prime number or prime power *special* if it has the form *q* = *n* 2 + *n*+ 1 and every element of the finite field F*q*is a difference of two non-zero *n*th powers. We call a finite projective plane *flag-regular* if it has a group of automorphisms that acts regularly (simply transitively) on the flags.

**Proposition 2.1.** *If q* = *n* 2 + *n* + 1 *is a special prime or prime power with n >* 1*, then* *(*F*q, (*F ×

*q)* *n* *) is a flag-regular finite projective plane. Conversely, if is a flag-regular*
*finite projective plane of order n, and if the number p* = *n* 2 + *n* + 1 *is prime, then p is* *special and* ∼= *(*F*p, (*F*p* × *)* *n* *).*

**Remark 2.2.** Note that, since the group law of F*q*is addition, the expression *xy* −1 in the general formula (1) is to be interpreted as *x* − *y* when defining *(*F*q, (*F ×

*q)* *n* *)*.
**Remark 2.3.** The restriction *n >* 1 in the first part of the proposition is needed only because this is a requirement in the definition of finite projective planes we are using; axioms (i) and (ii) and the flag-regularity hold also for *n* = 1, *p* = 3.

<!-- Page 4 -->

*Proof of Proposition 2.1.* Let *Dn*= *Dq,n*denote the set of *n*th powers (or equivalently, of *(n* + 1*)*st roots of unity) in F ×

*q*. The fact that every element in F*q*is a difference of
two elements of *Dn*tells us that the map (1) with *D* = *Dn*and *F* = F*q*is surjective, and since the two sides are finite sets of the same cardinality it must be a bijection. Hence *(*F*q, Dn)*is a finite projective plane, and it is also clear that the permutations*x* → *ax*+*b* (*a* ∈ *Dn*, *b* ∈ F*q*) of F*q*give automorphisms of this projective plane and that the group of these automorphisms acts simply transitively on the flags. Conversely, let be a projective plane of order *n* for which a group of automorphisms *G*acts regularly on the flags. Let *(p*0*, L*0*)*be a fixed flag of, so that by assumption every flag can be written as *g(p*0*, L*0*)* for a unique *g* ∈ *G*. If *H* and *K* are the stabilizers of *p*0 and *L*0in *G*, then it follows that *H* ∩ *K* = {*e*} and that both the map

*H* × *(K* {*e*}*)* × *H* → *G H* (2)

given by multiplication and the corresponding map with the roles of *H* and *K* interchanged are bijections. (To see the bijectivity of (2), note first that the two sets have the same cardinality, since *(n* + 1*)n(n* + 1*)* = *(n* + 1*)(n* 2 + *n* + 1*)* − *(n* + 1*)*, so that it suffices to prove surjectivity. If *g* ∈ *G H*, then the line through *p*0and *gp*0has the form *hL*0for some *h* ∈ *H*, so the flag *(h* −1 *gp*0*, L*0*)* equals *k(p*0*, L*0*)* with *k* ∈ *K* {*e*}, and then *g* = *hkh* ′ with *h* ′ ∈ *H*.) We also mention the converse: if *G* is any finite group containing subgroups *H* and *K* for which both (2) and the analogous map with *H* and *K* interchanged are bijections, then we obtain a finite projective plane having *G* as a group of automorphisms acting regularly on the flags by taking the points and lines to be the left cosets of *H* and *K* in *G*, respectively, and defining “incidence” to mean “non-empty intersection.” For instance, two distinct “points” *p*1= *g*1*H* and *p*2= *g*2*H* lie on the unique “line” *L* = *gK* given by *g* = *g*1*h*1*k* = *g*2*h*2, where *g* 1−1 *g*2= *h*1*kh* − 2 1 is the decomposition of *g* 1−1 *g*2∈ *G H* given by the bijection (2). If we now further assume that *p* = *n* 2 + *n* + 1 is prime, then the Sylow theorems and the fact that |*G*| = *p(n* + 1*)* with *p > n* + 1 imply that *G* has a unique (and hence normal) subgroup *F* of order *p*. Since *(*|*F* |*,* |*H* |*)* = 1 and |*F*||*H*| = |*G*|, the map *F* ×*H* → *G* given by multiplication is a bijection, so *G* is the semi-direct product *F H*. Moreover, the action of *H* on *F* by conjugation is faithful, because the uniqueness of the decomposition in (2) shows that there can never be a relation *g* = *hgh* −1 with *h* ∈ *H* {*e*} and *g* ∈ *G H*. Identifying *F* with F*p*and observing that Aut*(*F*p)* = F*p* × is cyclic and has *Dn*as its unique subgroup of order *n* + 1, we can make the further identifications *H* = *Dn*and *G* = F*pDn*or, in a convenient matrix representation, {()} {()} {()} *a b* 1 *b a* 0 *G* =*, F* =*, H* =*.* 0 1 *a*∈*D ,b*∈F 0 1 *b*∈F 0 1 *a*∈*D* *n p p n* For the same reason the subgroup () *K* of *G* is also cyclic, generated by some element () *a* 0*b*0with *a* a generator of *D* and *b* = 0, and conjugating all matrices of *G* by*λ* 0 0 1 0 *n* 0 0 1 with *λ* = *(a*0− 1*)/b*0we can suppose {()} *a a* − 1 *K* =*.* 0 1 *a*∈*Dn*

<!-- Page 5 -->

( *a b* ) Now the requirement that the map (2) be an isomorphism says that every matrix 0 1 with *a* ∈ *Dn*and *b* ∈ F*p* × can be factored uniquely as () () () *a* 10 *a*2*a*2− 1 *a*30 *,* 0 1 0 1 0 1

and multiplying this out we find that this is precisely equivalent to the requirement that every element of F*p* × is uniquely a difference of two elements of *Dn*. Hence *p* is special and ∼= *(*F*p, Dn)*.

In Section 6, we will obtain a generalization of this result (for certain symmetric 2- designs), with an entirely different proof. The proof of Proposition 2.1 was self-contained. If we combine it with parts (a) and (b) of Theorem 1.1, we obtain the following stronger result:

**Theorem 2.4.** *Let n be the order of a flag-transitive finite projective plane. Then at* *least one of the following holds:*

(a) *n is a prime power and* ∼= P
2 *(*F*n);*

(b) *p* = *n* 2 + *n* + 1 *is a special prime and* ∼= *(*F*p, (*F*p*
× *)* *n* *).*

Notice that the two alternatives occurring in the theorem are not necessarily exclusive: it is possible that the number *n* is both a prime power and is associated to a special prime *p* = *n* 2 +*n*+ 1, and in this case the projective plane of this order, while still unique, has both forms P 2 *(*F*n)* and ∼= *(*F*p, (*F*p* × *)* *n* *)*. By the discussion following Theorem 1.1, we know that this can happen for only two values of *n*, namely *n* = 2 (*p* = 7*)* and *n* = 8 (*p* = 73). Let us look in detail at these two exceptional cases to see how the isomorphism between the two differently-defined projective plane structures works. Consider first the case *n* = 2. We define an automorphism *A* of P 2 *(*F2*)* of order 7 by

*A* : *(x* : *y* : *z)* → *(y* : *z* : *x* + *y).*

Then every point of P 2 *(*F2*)* has the form *pi*= *A* *i* *(p*0*)* for a unique *i* ∈ Z*/*7Z, where *p*0 is the point *(*1:0:0*)*:

*i* 0 1 2 3 4 5 6 *pi (*1:0:0*) (*0:0:1*) (*0:1:0*) (*1:0:1*) (*0:1:1*) (*1:1:1*) (*1:1:0*)*

and every line in P 2 *(*F2*)* has the form *Lj*= *A* *j* *(L*0*)* for a unique *j* ∈ Z*/*7Z, where *L*0is the line {*x* = 0}:

*j* 0 1 2 3 4 5 6 *Lj x* = 0 *x* = *z x* + *y* + *z* = 0 *y* = *z x* = *y z* = 0 *y* = 0

Then *Lj*= {*pj*+1*, pj*+2*, pj*+4*)* for every *j*, so the correspondence *(pi, Lj)* → *(i, j )* defines an isomorphism between the Desarguesian projective plane {points in P 2 *(*F2*)*, lines

<!-- Page 6 -->

in P *(*F2*)*, usual incidence} and the special projective plane {*i* ∈ F7*, j* ∈ F7*, i* − *j* ∈ *D*}, where *D* = *(*F × *)* = 〈2〉 = {1*,*2*,*4}. The automorphism

*B* : *(x* : *y* : *z)* → *(x* : *y* + *z* : *y)*

of P 2 *(*F2*)* fixes *p*0and *L*0and sends *pi*to *p*2*i*and *Lj*to *L*2*j*, and the group of automorphisms generated by *A* and *B*, with the relations *A* 7 = *B* 3 = 1, *BAB* −1 = *A* 2, acts regularly on the flags of P 2 *(*F2*)*. The case *n* = 8 is similar, but more complicated because now the group of automorphisms of P2*(*F*n)* is not just **PGL**3*(*F*n)* but the extension of this group by the group Gal*(*F8*/*F2*)* of order 3. We represent F8as F2[*α*] where *α* 3 + *α*+ 1 = 0. Then *α* 7 = 1 and F × 8 = {1*, α,..., α* 6 } = {1*, α, α* 2 *, α* + 1*, α* 2 +*α, α* 2 + *α* + 1*, α* 2 + 1}. The automorphism

*A* : *(x* : *y* : *z)* → *(α* 6 *x* + *α* 2 *z* : *α* 4 *x* + *α* 6 *y* + *α* 3 *z* : *α* 3 *y* + *z)*

of P 2 *(*F8*)* of order 73 acts simply transitively on lines and points, so every point is uniquely representable as *pi*= *A* *i* *(p*0*)* and every line uniquely representable as *Lj*= *A* *j* *(L*0*)*, where *p*0= *(*1:0:0*)* as before and *L*0is the line *x* + *α* 5 *y* + *αz* = 0. The points of *L*0are *pi*with *i* ∈ *D* = *(*F × 73 *)* 8 = 〈2〉 = {1*,*2*,*4*,*8*,*16*,*32*,*37*,*55*,*64}, so *Lj*= {*pi*| *i* − *j* ∈ *D*} and just as before the correspondence *(pi, Lj)* → *(i, j )* defines an isomorphism between the Desarguesian projective plane P 2 *(*F8*)* and the special projective plane *(*F73*, D)*. The only difference is that the group of automorphisms acting transitively on the flags of P 2 *(*F8*)*, generated by *A* and a second automorphism *B* of order 9 satisfying *BAB* −1 = *A* 2, can no longer be realized in **PGL**3*(*F8*)* but only in the full group of automorphisms **P***0***L**3*(*F8*)* of P 2 *(*F8*)*: the automorphism *B* of P 2 *(*F8*)* of order 9 fixing *p*0and *L*0and sending *pi*and *Lj*to *p*2*i*and *L*2*j*for every *i* and *j* is given by

*B* : *(x* : *y* : *z)* → *(x* ′ : *α* 5 *x* ′ + *y* ′ + *α* 6 *z* ′ : *α* 6 *x* ′ + *αy* ′ *),*

where *x* → *x* ′ denotes the Galois automorphism of order 3 of F8that sends *α* to *α* 2. We can summarize the results of this section as follows. Call a finite projective plane *special* if it has the form ∼= *(*F*p, (*F*p* × *)* *n* *)* for some special prime *p* = *n* 2 + *n* + 1. Then

(i) any flag-transitive finite projective plane is either Desarguesian or special; (ii) exactly two finite projective planes, of order 2 and 8, are both Desarguesian and special. Moreover, if there are any special projective planes other than the two in (ii), then they must have order *n >* 1*.*44 × 10
7 (*p >* 2 × 10 14 ) by the result of Feit quoted in the introduction, and from the computations on special primes described later in this paper we can strengthen this to *n >* 2 × 10 11 (*p >* 4 × 10 22 ). It is thus highly unlikely that any non-Desarguesian flag-transitive finite projective planes exist.

<!-- Page 7 -->

## 3. Special primes, Fermat surfaces and Gauss periods

We have seen that a non-Desarguesian finite flag-transitive projective plane of order *n* exists if and only if *p* = *n* 2 + *n* + 1 is a special prime, i.e., if and only if *p* is prime and every element of the finite field F*p*is the difference of two elements of *D* = *(*F*p* × *)* *n*. In this section we give a number of elementary number-theoretical statements about *n* and *p* which are equivalent to this property. These involve the *Fermat surface*

S : *X*0 *n* + *X*1 *n* = *X*2 *n* + *X*3 *n* *,* (3)

the *Fermat curves* *Fη*: *X*0 *n* − *X*1 *n* = *ηX*2 *n* *(η* ∈ F*p* × *),*

## and the Gaussian periods

∑ <u>1</u> ∑*n*∑*n* *ω* = *ζ* *a* = *ζ* *x* *,* = *ζ* *x* =1+ *nω,* *a*∈*D* *n* *x*∈F*p* ×*x*∈F *p*

where *ζ* = *ζp*denotes a primitive *p*th root of unity. All of these are classical objects, much studied in number theory. In particular, the Gaussian periods, which are defined for any prime number *p* and divisor *n* of *p* − 1 (and will be used in this generality in Section 4), generate the unique subfield of degree *n* of the cyclotomic field Q*(ζ )* and were introduced for essentially this purpose by Gauss. We will show: the prime *p* = *n* 2 + *n*+ 1 is special if and only if the Fermat surface S has no non-trivial F*p*-rational points (by *trivial points* of S over F*p*we mean points *(x*0*, x*1*, x*2*, x*3*)* ∈ S*(*F*p)* with either *x*0*x*1*x*2*x*3= 0 or {*x* 0 *n* *, x* 1 *n* } = {*x* 2 *n* *, x* 3 *n* }); if and only if the Fermat curves *Fη*all have the same number of F*p*-rational points; and if and only if the absolute value of the Gaussian period *ω* is the square root of a rational integer. We denote by *X(*F*)* the set of F-rational points of any variety *X* defined over a finite field F and by |*X(*F*)*| its cardinality.

**Theorem 3.1.** *Suppose that p* = *n* 2 + *n*+ 1 *is prime. Then the following are equivalent:*

(a) *p is special;*
(b) *the map φ* : *D* × *D (*diagonal*)* → F*p*
× *sending (x, y) to x* − *y is bijective;*

(c) *the surface* S *has no non-trivial points over* F*p;*
(d) |*Fη(*F*p)*| *>* 3*n for every η* ∈ F*p*
× *;*

(e) |*Fη(*F*p)*| *<* 2*n*
2 + *n for every η* ∈ F*p* × *;*

(f) |*Fη(*F*p)*| = *n*
2 + *n or n* 2 + 2*n for every η* ∈ F*p* × *;*

(g) |S*(*F*p)*| *<* 2*n*
4 + 5*n* 3 + 4*n;*

(h) |S*(*F*p)*| = 2*n*
4 + *n* 3 + 4*n* 2 + 4*n;*

(i) |*ω*| 2 ∈√Q<u>;</u>
(j) |*ω*| = *n;*
(k) trQ*(ζ )/*Q*(*| |
4 *)* = *n* 8 + *n* 7 − 2*n* 4 − 4*n* 3 − 5*n* 2 − 3*n.*

<!-- Page 8 -->

*Proof.* The proofs of the equivalences of (a)–(f) are elementary. By definition, *p* is special if and only if the map *φ* in (b) is surjective. Since the domain and range of *φ* have the same cardinality, this is equivalent to *φ* being bijective or injective. The injectivity says that the equation *x* 1 *n* − *x* 2 *n* = *x* 3 *n* − *x* 0 *n* is possible for *xi*∈ F*p* × only if *x* 1 *n* = *x* 2 *n* and *x* 3 *n* = *x* 0 *n*

or *x* 1 *n* = *x* 3 *n* and *x* 2 *n* = *x* 0 *n*, so is equivalent to (c). For *η* ∈ F*p*, let *t (η)* denote the number of representations of ∑ *η* as the difference of two elements of *D*. Then *t (*0*)* = *n*+ 1 and*η*∈F *p* *t (η)* = |*D*| 2 = *(n*+ 1*)* 2, so that the average value of *t (η)* with *η* ∈ F*p* × is 1. This again gives the equivalence of (a)–(c), since (a) says that *t (η)* ≥ 1 for every *η* ∈ F*p*, (b) that *t (η)* = 1 for every *η* ∈ F*p* ×, and (c) that *t (η)* ≤ 1 for every *η* ∈ F*p* ×. We now claim that   *n* if *η* ∈ F*p* ×, ±*η* ∈*/ D*, |*Fη(*F*p)*| = *n* 2 *t (η)* + 2*n* if ±*η* ∈ *D*, −1 ∈*/ D*, (4)   3*n* if *η* ∈ *D*, −1 ∈ *D*.

To see this, we observe first that the number of F*p*-rational points *(x*0*, x*1*, x*2*)* on the curve *Fη*with *x*0*x*1*x*2= 0 equals *n*, 2*n* or 3*n* in the three cases given, while the number of points with *x*0*x*1*x*2= 0 is always divisible by *n* 2, because the group *(µ* 3 *n* *)/µn*(where *µn*⊂ F*p* × is the subgroup of *n*th roots of unity and the action is diagonal) acts freely on them. Moreover, the quotient of *Fη(*F*p)* ∩ *(*F*p* × *)* 3 */*F*p* × by this action is just the set of points *(Y*0: *Y*1: 1*)* with *Y*0*, Y*1∈ *D* and *Y*1− *Y*0= *η*, so its cardinality is *t (η)*. This proves (4) and hence the equivalence of (a)–(c) with (d)–(f), since we will see below that *n* must be odd if *p* is special, so that the third option in (4) cannot then occur. To prove the other equivalences, we define a number *δ(p)*, the *defect* of *p*, by

∑ ( *t (η)* ) *δ(p)* =*,* ×2 *η*∈F*p/*{±*D*}

where ±*D* = *D* ∪ −*D* = *µ*2*n*+2. Using the fact that the average value of *t (η)* with *η* ∈ F*p* × is 1 and that the value of *t (η)* depends only on the class of *η* in the quotient group F*p* × */(*±*D)*, we obtain the alternative formula ( ∑ ) <u>1</u>2<u>n</u> *δ(p)* = *t (η)* −*.* 2×2 *η*∈F*p/*{±*D*}

The Cauchy–Schwarz inequality and the fact that the average value of *t* is 1 then show that the defect is always non-negative and is zero if and only if ∑ *p* is special. Now observe that*η*∈F *p* *t (η)* 2 is the number of 4-tuples *(u, v, w, x)* in *D* 4 for which *u*+*v* = *w*+*x*, and by the formula just given this number is equal to *(n*+1*)(*2*n*+1+4*δ(p))*. Since there are already *(n*+1*)(*2*n*+1*)*trivial solutions, i.e., solutions with {*u, v*} = {*w, x*}, this shows again that *p* is special if and only if there are no non-trivial solutions, which is just (c), but it also shows that the number of rational points of S is given by

|S| = *(*2*n* +1+4*δ(p))n* 3 + 4*n* 2 *t (*1*)* + 4*n,*

<!-- Page 9 -->

which equals *(*2*n* + 1*)n* + 4*n* + 4*n* if *p* is special (since then *δ(p)* = 0 and *t (*1*)* = 1) and is ≥ *(*2*n* + 5*)n* + 4*n* if *p* is not special (since then *δ(p)* ≥ 1 and *t (*1*)* ≥ 0). This proves the equivalence of (g) and (h) with (a).

∑ Finally, the equivalence of (i) and (j) with (a) follows from the observation that | *t (η)* *ω*| = 2

*η*∈F*pζ*, which belongs to Q if and only if *t (η)* is constant for *η* = 0 and is equal to *n* if *t (η)* equals *n* + 1 for *η* = 0 and 1 otherwise, while the equivalence of (k) with (a) follows from the calculation

1 + *(p* − 1*)*|S| = |{*(x*0*, x*1*, x*2*, x*3*)* ∈ F*p* 4 | *x*0 *n* + *x*1 *n* = *x*2 *n* + *x*3 *n* }| <u>1</u> ∑ ∣∣ ∑*an* ∣∣ 4 3<u>1</u>4 = ∣ *z* ∣ = *p* + trQ*(ζ )/*Q*(*| |*).* *p* *z* *p* =1 *a*∈F *p* *p*

This completes the proof of the theorem.

## 4. A generalization and a conjecture

The above considerations can be generalized in the following way. Let *p* be an arbitrary prime number. Then any subgroup of F*p* × has the form

*Dn*= {*x* *n* | *x* ∈ F*p* × } = {*x* ∈ F*p* × | *x* *k* = 1}

for some divisor *n* of *p* − 1 and *k* = *(p* − 1*)/n*. We define the Gaussian period *ωn*as before by ∑ <u>1</u> ∑*n* *ωn*= *ζ* *x* = *ζ* *a* = trQ*(ζ )/K<sub>n</sub>(ζ ),* *x*∈*Dn* *n* *a*∈F*p* ×

where *ζ* is a primitive *p*th root of unity and *Kn*is the unique subfield of Q*(ζ )* of degree *n* over Q. We further define *tn(η)* for *η* ∈ F*p*as the number of representations of *η* as the difference of two elements of *D* ∑*n*, and call the pair *(p, n) special* if this number is independent of *η* for *η* = 0. Since*η*=0*tn(η)* = |*Dn*| 2 − |*Dn*| = *k* 2 − *k*, this common value must then be equal to *(k* − 1*)/n*, which must therefore be an integer. In particular, except in the trivial case when *k* = 1 and *n* = *p* − 1, we always have *k* ≥ *n* + 1 and *p* ≥ *n* 2 + *n* + 1, so that the case of special primes (*k* = *n* + 1, *tn(η)* = 1) is extremal. Using the same arguments as before, we can prove:

**Theorem 4.1.** *Let p* = *nk* + 1 *be prime. Then the following are equivalent:*

(a) *the pair (p, n) is special;*
(b) *tn(η)* = *(k* − 1*)/n for all η* = 0*;*
(c) *the surface (*3*) in* P
3 *has precisely n* 3 *k* + *n* 2 *(k* − 1*)* 2 + 4*nk* F*p-rational points;*

(d) |*ωn*| 2 *is a rational number;*
(e) |*ωn*| 2 = *k* − *(k* − 1*)/n.*

<!-- Page 10 -->

The analogue of the construction given in §2 is now the following. Suppose *(p, n)* is special, *k* = *(p* − 1*)/n*. Define a point-line incidence structure as follows: the points of are the elements of F*p*; the lines or *blocks* of also consist of the elements of F*p*; and a point *α* ∈ F*p*is incident with a block *β* ∈ F*p*if and only if *α* − *β* ∈ *Dn*. Thus there are *p* points and *p* blocks, each point is incident with *k* blocks and each block is incident with *k* points, any two distinct points are contained in exactly *(k* − 1*)/n* distinct blocks, and any two distinct blocks intersect in exactly *(k* − 1*)/n* distinct points. Hence is a 2*-(p, k, (k* − 1*)/n) symmetric block design*. It is clear that for *a* ∈ *Dn*and *b* ∈ F*p*the map *x* → *ax* + *b* from F*p*to itself defines an automorphism of in a natural way and that the group of these automorphisms acts regularly on the flags (= incident point-block pairs) of. To the knowledge of the authors, the only known examples of such designs other than finite projective spaces (of dimension at least 3) follow from [2, 11, 13]. These constructions are essentially covered by Theorem 4.2 (and Theorem 5.1) below, where among other results the existence results of [2, 11, 13] are re-proved in an alternative fashion. In view of these observations, and of the known difficulty of producing examples of symmetric designs admitting a flag-regular automorphism group, it is of interest to find examples of special pairs *(p, n)*. These are provided by the following theorem, whose proof will be given together with that of Theorem 5.1 below.

**Theorem 4.2.** *Let p be a prime and n*|*(p* − 1*). Then (p, n) is special in each of the* *following five cases:*

(a) *n* = 1*, p arbitrary,* |*ωn*|
2 = 1*,*

(b) *n* = 2*, p* ≡ 3 *(*mod 4*),* |*ωn*|
2 = *(p* + 1*)/*4*,*

(c) *n* = 4*, p* = 4*b*
2 + 1 *with b odd,* |*ωn*| 2 = *(*3*p* + 1*)/*16*,*

(d) *n* = 8*, p* = 64*b*
2 +9=8*d* 2 + 1 *with b and d integral,* |*ωn*| 2 = *(*7*p* + 1*)/*64*,*

(e) *n* = *p* − 1*, p arbitrary,* |*ωn*|
2 = 1*,*

*the corresponding values of ωnbeing given by*

(a) *ω*1= −1*,*
√ <u>−1 + i p</u>

(b) *ω*2=*,* √
2 √ √ *p* − 1 *p* + *p*

(c) *ω*4= ± *i,*
4 8 √ √ √ √ √ √ √ √ *p* − 1 *p* + 3 *p p* − 1 √ *p* + 3 *p*

(d) *ω*8= + + *i p* −*,*
8 32 16 2

(e) *ωp*−1= *ζ.* Cases (a) and (e) of this theorem are trivial and do not lead to interesting designs, but the families (b), (c) and (d) give us three infinite or potentially infinite classes of interesting flag-regular symmetric designs. Note that the family (c) is quite sparse: the only primes up to 40000 belonging to this class are 5, 37, 101, 197, 677, 2917, 4357, 5477, 8101, 8837, 12101, 15877, 16901, 17957, 21317, 22501, and 28901. The family (d), corresponding to the prime solutions of a Pell’s equation, is even thinner, though conjecturally still infinite:

<!-- Page 11 -->

the first prime of this form is our old acquaintance *p* = 73, with *b* = 1 and *d* = 3; the next two are 104411704393 (*b* = 40391, *d* = 114243) and 160459573394847767113 (*b* = 1583407981, *d* = 4478554083), with 12 and 21 digits, respectively, and the next four have 103, 119, 425, and 615 decimal digits, respectively. The conjecture about the non-existence of non-Desarguesian flag-transitive projective planes can now be generalized to the following:

**Conjecture 4.3.** *The only special pairs are the ones listed in Theorem* 4.2.

We have checked this conjecture by computer for all primes *p <* 10 000 000 and all divisors *n* of *p* − 1. (For the special case when *p* = *n* 2 + *n* + 1, as already mentioned,

W. Feit’s result verifies it for all *p <* 2 × 10
14 and we have extended this to *p <* 4 × 10 22 .) These numerical computations are described in an appendix. Apart from this, we have only the partial results and evidence presented in the next section.

## 5. Special primes, Gauss sums and Jacobi sums

In this section we prove Theorem 4.2 and a partial converse.

**Theorem 5.1.** *Assume that p* = *kn* + 1 *is prime and that (p, n) is special.*

(a) *If n >* 1*, then n is even and k is odd.*
(b) *If n <* 10*, then (p, n) belongs to one of the families of Theorem* 4.2. *Proof.* Let *ζ* = *ζp*, *Kn*and *ωn*be defined as at the beginning of the previous section. Then *ωn*∈ *Kn*, and it is well known that *ωn*generates *Kn*over Q. If *k* is even, then −1 belongs to *D*, so *ωn*is a real number. But then *ωn*
2 = |*ωn*| 2 ∈ Q, so *n* = [Q*(ωn)* : Q] ≤ 2. Therefore *k* must be odd if *n >* 2, in which case *n* is even since *nk* = *p* − 1 is even, and *k* is also odd when *n* = 2 since *k* ≡ 1 *(*mod*n)* for special *(p, n)*. This proves (a). To prove (b), we have to look at each value *n* ≤ 9 separately. The case *n* = 1 is of course trivial, since *D*1= F*p* ×, *ω*1= −1, so by virtue of part (a) we need only analyze the cases *n* = 2, 4, 6, and 8. This will at the same time provide the proof of Theorem 4.2, since *n* ≤ 8 in all cases of that theorem except for the case *n* = *p* − 1, which is trivial. All the proofs will involve Gauss sums, so we begin by recalling the main properties of these. Suppose *p* = *nk*+ 1 with *n* even and *k* odd (since by part (a) this is the only case that can occur for *(p, n)* special) and let *χ* : F*p* × → C × be a character of order *n*, which we fix by sending some chosen generator of the cyclic group F*p* × to a chosen primitive *n*th root of unity *λn*. To each *r* ∈ Z*/n*Z we associate the *Gauss sum* ∑ *Gr*= *G(χ* *r* *)* = *χ(x)* *r* *ζ* *x* *(r* ∈ Z*/n*Z*).* *x*∈F*p* ×

√ For*r* = 0 this equals −1, but according to Gauss for other values of*r* we have |*Gr*| = *p* and *G*−*r*= *(*−1*)* *r* *Gr*(the latter because *χ(*−1*)* = −1 since *k* is odd). In particular, 2 *n/*2√ √ *G* *n/*2 = *(*−1*) p* (and in fact *Gn/*2= + *p* for *n/*2 even and *Gn/*2= +*i p* for *n/*2

<!-- Page 12 -->

odd, as Gauss showed). The key property of the Gauss sums comes from the classical calculation ∑ ∑ ∑ *GrGs*= *χ(x)* *r* *χ(y)* *s* *ζ* *x*+*y* = *χ(z)* *s* *χ(x)* *r*+*s* *ζ* *x(z*+1*)*

*x,y*∈F*p* × *z*∈F*p* × *, z*=−1 *x*∈F*p* ×

if *r*, *s* and *r* + *s* are ≡ 0 *(*mod*n)* (set *y* = *zx* and observe that the sum of the terms with *z* = −1 vanishes); now substituting ∑ *x* = *x* ′ *(z* + 1*)* −1 we find that *GrGs*= *Gr*+*sJr,s* where the *Jacobi sum Jr,s*= *z*∈F*p* × {−1} *χ(z)* *s* *χ(z)* ¯ *r*+*s* is an element of the ring Z[*λn*] √ of absolute value *p*. On the other hand, the Gaussian period and Gauss sums are related by <u>1</u> ∑ *ωn*= *Gr,* *n* *r (*mod*n)* ∑ *r* because*r (*mod*n)χ(x)* equals 0 if *x* ∈ *Dn*and *n* if *x* ∈ *Dn*. These two facts together combine to give sufficiently strong information about *ωn*to contradict the hypothesis |*ωn*| 2 ∈ Q in many cases. We now look at each case separately. √<u>1</u>√2

- *n* = 2. Here *G*1= *i p*, so *ω*2=
2 *(*−1 + *i p)* and |*ω*2| = *(p* + 1*)/*4∈Z for any *p* ≡ 3*(*mod 4*)*, proving part (b) of the theorem (as well as part (b) of Theorem 4.2) in this case, since we already know that *(p,*2*)* can only be special for *k* odd. We could also use Gauss sums to show this latter fact without using part (a), since if *p* ≡ 1 *(*mod 4*)* we have <u>1</u>√2 <u>1</u>√ *ω*2= 2 *(*−1 + *p)* and hence |*ω*2| = 4 *(p* +1−2 *p)* ∈ Z. √2

- *n* = 4. Here *G*0= −1, *G*2= *p*, *G*3= −*G*1and *G*
1 */G*2= *J*1*,*1∈ Z[*i*], where *J*1*,*1= *A* + *Bi* with *A* 2 + *B* 2 = *p* and *A* ≡ 3*(*mod 4*)* and *B* even. Hence √ √ √ −1 + *G*1+ *G*2+ *G*3*p* − 1 *p* − *A p* *ω*4= = ± *i,* 4 4 8 2√ so 16|*ω*4| = 3*p* +1−2*(A* + 1*) p*. Clearly this is a rational number if and only if *A* = −1, i.e., if and only if *p* = *B* 2 + 1, corresponding to case (c) of Theorem 4.2.

- *n* = 6. This time the relationship with the Jacobi sums gives *G*1= *ip* 1*/*6
*α* 2 *, G*2= *p* 1*/*3 *αρ,*¯ *G*3= *ip* 1*/*2 *, G*4= *p* 1*/*3 *ᾱρ, G*5= *ip* 1*/*6 *ᾱ* 2 *,* 3 <u>1</u> √ where *α* = 2 *(M* + *N* −3*)* is an element of Z[*λ*3] of norm *p* and *ρ* is a cube root of unity. (In fact one has *M* ≡ 1 *(*mod 3 √ *)* and *N* ≡ 0 *(*mod 3*)*, and *z* is equal to 1 if *M* ≡ *N* ≡ 0 *(*mod 2*)* and to *(*−1 ∓ *i* 3*)/*2 if *MN* ≡ ±1 *(*mod 4*)*, with the former case occurring if and only if 2 is congruent to a cube modulo *p*, but we do not need to know any of this.) Hence 1*/*3√1*/*6 2 6 *(ω*6*)* = −1 + 2*p (αρ),* ¯ 6 *(ω*6*)* = *p* + 2*p (α).*

Write 2*p* 1*/*3 *αρ*¯ = *γ* +*iδ* with *γ* and *δ* real. Then *γ* is one of the three roots (all of which √ are real) of the cubic equation *γ* 3 − 3*pγ* − *pM* = 0, and *δ* = 4*p* − *γ*2. Hence √ <u>γ</u> 2 <u>− p 4p − γ</u> 2 <u>± γ 12p − 3γ</u>2 6 *(ω*6*)* = *γ* − 1*,* 6 *(ω*6*)* = √ or √*,* *p* 2 *p*

<!-- Page 13 -->

depending on whether *ρ* equals 1 or not. Using the equation *γ* − 3*pγ* − *pM* = 0, we find

36|*ω*6| 2 = 2*γ* 2 + *(M* − 2*)γ* + *p* + 1 or √ <u>γ</u> 2 <u>− (M + 4)γ + 8p +2± (γ − M) 12p − 3γ</u>2 *.* 2 The first of these two expressions cannot be rational since then*γ* would satisfy a quadratic as well as a cubic equation and hence would belong to Q, contradicting the fact that *ω*6 has degree 6 over Q. Hence the second equation must hold if *(p,*6*)* is special, and since we know from Theorem 4.1(e) that 36|*ω*6| 2 = 5*p* + 1 in this case, we find

*(p,*6*)* is special ⇒ *(γ* 2 − *(M* + 4*)γ* − 2*p)* 2 = *(γ* − *M)* 2 *(*12*p* − 3*γ* 2 *)*

⇒ *(M* 2 + 2*M* +4− *p)γ* 2 + 2*p(M* − 1*)γ* + *p(p* − 5*M* 2 − 2*M)* = 0*,*

where in the last line we have again used the equation of *γ*. Since *γ* has degree 3 over Q, this can only happen if *M* = 1 and *p* = *M* 2 + 2*M* +4=5*M* 2 + 2*M* = 7.

- *n* = 8. The analysis in this case is more complicated and we will be even sketchier than
√2 before. As in the case *n* = 4 we find *G*4= *p*, *G*6= *G*2and *G* 2 */G*4= *A* + *Bi* with *A* 2 + *B* 2 = *p*, now with *A* ≡ 3*(*mod 8*)* and *B* ≡ 0*(*mod 4*)*, so √ √ √ <u>p −1+2γ p + A p</u> *(ω*8*)* =*, γ* := *(G*2*)* = ±*.* 8 2 The odd-index Gauss sums are given by *G*1= *σ τ*, *G*3= −√*ε*<u>σ τ,</u> *G*5= *εστ* and *G*7= −*σ τ*, where *ε* = *(*−1*)* *B/*4, *σ* 2 = *G*2, and *τ* 2 = *C* + *D* −2 with *D* ≡ *C* − 5 ≡ *ε* + 1*(*mod 8*)*, so <u>(σ − εσ )(τ + ετ )</u> 2 *(ω*8*)* = = *(σ ) (τ )* or *(σ ) (τ ),* 4*i* depending on whether *ε* = 1 or −1. This gives 2√ √ 16 *(ω*8*)* = *( p* − *εγ )( p* + *εC),*

and combining this with the formula just given for *(ω*8*)* we obtain 2√ √ 64|*ω*8| = 7*p* +1+2*(A* −1+2*εC) p* − 4*(C* + 1*)γ* + 4*(*1 − *ε)γ p.* √ √ This is rational if and only if the coefficients of *p*, *γ* and *γ p* all vanish, i.e., if *ε* = 1, *C* = −1 and *A* =1−2*εC* = 3, and this corresponds (with *B* = 8*b*, *D* = 2*d*) exactly to the conditions *p* = 64*b* 2 + 9 and *p* = 8*d* 2 + 1 given in part (d) of Theorem 4.2.

As the proof makes clear, the analysis of the Gaussian periods becomes more and more difficult as *n* increases, and we cannot hope to progress much further by these methods (though a few more cases might still be tractable). On the other hand, the proof also makes it clear that the conditions on the Gauss sums and Jacobi sums imposed by the assumption that |*ωn*| 2 is rational become more and more restrictive as *n* increases, with the condition in the case *n* = 8 already strong enough to lead to a doubly exponentially thin set of solutions, so that the conjecture that there are no other solutions than the ones we have already found is at least quite plausible.

<!-- Page 14 -->

**6. Flag-regular symmetric designs with** *k* **dividing** *v* − 1 In the examples of flag-regular symmetric 2-designs that we constructed via special pairs, the parameter *k* divided the number of points minus one. The following theorem describes how, conversely, this (rather strong) algebraic assumption affects the design. **Theorem 6.1.** *Let be a symmetric* 2*-(v, k, λ) design admitting a flag-regular automorphism group G. Suppose that k divides v* − 1*. Then*
(a) *v* = *p* *h* *for some prime p and natural number h, and we can identify the point set P* *of with the points of the h-dimensional vector space* F*p*
*h* *over* F*p;*

(b) *G* ∼= F*p* *h*
*H where H is a subgroup of* **GL***h(*F*p) that is isomorphic to Gxfor any* *point x of.*

*Proof.* Since is a symmetric design, we have (see e.g. [1])

*λ(v* − 1*)* = *k(k* − 1*).*

Together with the assumption that *k* divides *v* − 1, this implies that *λ* divides *k* − 1, so that *(λ, k)* = 1. But the number of blocks of incident with a point equals *k*. By 8(b) of [3, p. 80], it follows that *G* acts as a Frobenius group on the points (and blocks) of. So the Frobenius kernel *F* acts regularly on the points. Also, by 7(a) of [3, p. 79], *G* acts primitively on the points of. As the Frobenius kernel *F* is nilpotent, it is the direct product of its Sylow subgroups, say

*F* = *Sp*1× · · · × *Sp<sub>j</sub>,*

where {*p*1*,..., pj*} is the set of distinct primes dividing *F*. Let *Z* be the center of *F* (which is non-trivial). As *F ✂ G*, *G* acts on the *Z*-orbits of points, contradicting the point-primitivity of *G* unless *Z* = *F*. Since each *Spi*is a characteristic subgroup of *F*, in the same way we find that *j* = 1. So *F* is an abelian *p*-group (*p* = *p*1). Now let *A* be the unique maximal elementary abelian *p*-subgroup of *F*. Then *A* is a characteristic subgroup of *F*, so if *A* = *F* the *A*-orbits of points of are non-trivial blocks of imprimitivity, again a contradiction. Hence *F* is elementary abelian. Put |*F*| = *p* *h*. As *F* acts regularly on the points of, we can identify both *F* and the point set of with the additive group F*p* *h*, acting on itself by translation. This proves part (a). Since *F ✂ G*, we also see that for any point *x* of, *Gx*acts as an automorphism group on *F* by conjugation. As *F* acts regularly on the points of, *Gx*acts faithfully on *F*, so is isomorphic to a subgroup of **GL***h(*F*p)*. Part (b) follows.

**Remark 6.2.** Note that for symmetric designs, points and blocks play interchangeable roles, so we could equally well formulate Theorem 6.1 with points replaced by blocks.

In the case when *v* is prime the analysis is easier and leads to the same conclusion as in the special case *λ* = 1, namely, that the only flag-regular 2-designs with *k* |*(v* − 1*)* are the ones constructed in Section 4. In fact, we need only the assumption *k < v*.

<!-- Page 15 -->

**Theorem 6.3.** *Let be a symmetric* 2*-(p, k, λ) design admitting a flag-regular automorphism group G, with p prime and k < p. Then k* = *(p* − 1*)/n, λ* = *(k* − 1*)/n where* *(p, n) is a special pair and is isomorphic to the design constructed in Section* 4.

*Proof.* The argument is essentially the same as in the proof of Proposition 2.1. If *H* and *K* are the stabilizers of *p*0and *L*0for some flag *(p*0*, L*0*)* of, then it follows just as before that *H* ∩ *K* = {*e*} and that both the map (2) and the corresponding map with *H* and *K* interchanged are exactly *λ* : 1, i.e., every element *g* ∈ *G H* has precisely *λ* representations as *hkh* ′ with *h, h* ′ ∈ *H* and *e* = *k* ∈ *K* (and similarly with *H* and *K* interchanged). Since |*G*| = *kp* and *k < p*, the Sylow theorems again imply that the *p*- Sylow subgroup *F* of *G* has order *p* and is normal, so that we can again identify *G/H* and *G/K* with *F* ∼= F*p*, and *H* and *K* with the unique subgroup of F*p* × of order *k*, which is then *Dn*= *(*F*p* × *)* *n* with *n* = *(p* − 1*)/k*. Everything else goes through exactly as before: ( *Dn*F1*p* ) ( 1*p* ) ( *D* 0 ) we again have compatible isomorphisms *G* ∼= 0, *F* ∼= 0 F1, *H* ∼= 0 *n* 1 and ( 1 ) ( 1 1 ) *K* = 0 −11 *H* 0 1, and the fact that the map (2) is *λ* : 1 translates directly into the property that every element of F*p* × can be written in exactly *λ* ways as a difference of two elements of *Dn*, i.e., *(p, n)* is a special pair.

## Appendix. Numerical computations

In the text we mentioned several numerical results, specifically, that there are no special primes less than 2 × 10 22 and no special pairs *(p, n)* with *p <* 10 7. We indicate briefly how these calculations were carried out. We start with the discussion of special pairs. If *(p, n)* is special, then *p* has the form *tn* 2 +*n*+1 for some *t* ≥ 1. By Dirichlet’s theorem the number of primes *p < X* satisfying *p* ≡ *n* + 1 *(*mod*n* 2 *)* with *n* fixed is asymptotically *ϕ(n* 2 *)* −1 *X/*log*X* for *X* large, so the total number of pairs ∑ *(p, n)* with *p < X* of the form *tn* 2 + *n* + 1 is roughly *CX/*log*X* with *C* = ∞ *n*=1*ϕ(n* 2 *)* −1 = 2*.*203856596437859*.. .*. If we use the results of Section 5, then we can assume that *n* is even and larger than 8, which reduces the number of pairs to be tested to *C* ′ *X/*log*X* with ∑ 1 2*C* 1 1 1 1 *C* ′ = 2 = − − − − = 0*.*14195282662358*... ,* 2|*n, n>*8 *ϕ(n )* 5 2 8 12 32

a saving of a factor of about 16. We initially tested all pairs with *p <* 10 5, finding only solutions with *n* = 2, 4, 6 or 8. This led to the statements of Theorems 4.2 and 5.1. Once they were proved, the tests in larger ranges were carried out only for even *n* ≥ 10. Two methods were used to test whether a given pair *(p, n)*, where *p* = *tn* 2 + *n*+ 1 is prime, is special. The first uses part (e) of Theorem 4.1, i.e., the equality |*ωn*| 2 = *k* − *t*, where *k* = *(p* − 1*)/n* = *tn* + 1 as usual. To compute *ωn*, we choose a primitive root *n* ∑ *Gj* *g* modulo *p* and set *G* = *g*. Then *G* generates the group *Dn*and *ωn*=*j (*mod*k)ζ*, where *ζ* = *e* 2*πi/p*. The corresponding program in GP/PARI is very short:

<!-- Page 16 -->

{try(p,n)=z=exp(2*Pi*I/p); G=znprimroot(p)ˆn; om=sum(j=1,p\n,zˆlift(Gˆj)); kk=norml2(om); if(abs(n*kk-p+p\n)<.1,print(p," ",n," ",kk))}

and is quite efficient for small *p* (for instance, the time to check the 5101 pairs *(p, n)* with *p <* 10 5 and *n >* 3 on a SUN Sparc workstation was 34 minutes, and under 4 minutes if one considered only the 1352 pairs with *n* even and *>* 8), but grows quadratically with the size of the bound *X*. The second method, which is somewhat faster, is based on part (b) of Theorem 4.1,

i.e., on checking that the number *tn(η)* of representations of *η* ∈ F*p*
× as a difference of two elements of *Dn*is always equal to *t*. We can compute *tn(η)* as the number of *j* (mod *k*) for which *(G* *j* +*η)* *k* equals 1 (mod *p*), where *G* = *g* *n* as before. This is done in PARI-GP by the program

```
t(p,n,eta) = k=p\n; G=znprimroot(p)ˆn;
sum(j=1,k,(gˆj+r)ˆk==1)
```
(A slightly different approach, of comparable speed for a single value of *η* but more efficient if one is going to compute *tn(η)* for several *η*’s for the same *n* and *p*, is to precompute the subset *Dn*⊂ Z*/p*Z by sorting the set {*G* *j* } *j (*mod*k)*and then to count the number of *m* ∈ *Dn*with *m* + *η* ∈ *Dn*. The sorting algorithm is included in PARI and similar languages.) Checking the equality *tn(η)* = *t* for all *η* ∈ F*p* × would be very time- consuming, but we can of course abort the test as soon as it has failed for a single value of *η*, and this leads to a considerable speeding-up. For instance, the prime *p* = 1021 has the form *tn* 2 + *n*+ 1 for *n* = 3, *t* = 113 and for *n* = 12, *t* = 7, and since *t*3*(*1*)* = 111 and *t* 12*(*1*)* = 6 both pairs can immediately be eliminated. Of the 6702 pairs *(p, n)* of the form *p* = *tn* 2 + *n* + 1 with *p <* 10 5 and 2 *< n < p* − 1, only 147 pass the first test *tn(*1*)* = *t* and only 27 satisfy *tn(η)* = *t* for 1 ≤ *η* ≤ 6, and all but three of these are in fact special pairs, the exceptions being *(p, n, t)* = *(*601*,*24*,*1*)*, *(*6079*,*3*,*675*)* and *(*54679*,*3*,*6075*)*. It is interesting to note that in each of these three cases, the non-zero values of *tn(η)* − *t* (for all *η* in the first two cases and for at least the first few thousand *η* in the third) are all the same up to sign, assuming only the values ±1, ±15 and ±45, respectively. Moreover, the set of *η*’s for which *tn(η)* = *t* also seems not to be random (e.g., in the three cases mentioned one has *tn(η)* = *t* not only for *η* ≤ 6, but for all *η* ≤ 20 except 7, 11, 13, 14, 17 and 19). These observations suggest that the distribution of the cardinalities of the Fermat curves *Fη*may have some possibly interesting additional structure. The total computational time with the second method for *p <* 10 5 was about 16 minutes if we looked at all pairs with 2 *< n < p* − 1, and about 1 minute if we restricted to even *n >* 8, as opposed to 34 minutes and 4 minutes with the first method. A further speeding up is obtained by noting that the number *t* = *(p*− *n*− 1*)/n* 2 must have a specific parity in order for the pair *(p, n)* to be special. Indeed, the number *tn(*1*)* is the cardinality of the set of *x* ∈ *Dn*for which *x*+ 1 also belongs to *Dn*, and this set has an involution *x* → *x* −1 which is fixed-point free if 2 ∈ *Dn*and has exactly one fixed point if 2 ∈ *Dn*. Hence, unless 2 belongs to *Dn*(which happens only rarely, with frequency 1*/n*), the number *tn(*1*)* is even and hence *t* must also be even if *(p, n)* is special, and similarly *t* must be odd in the remaining cases when 2 ∈ *Dn*. This eliminates about half of the

<!-- Page 17 -->

possible pairs *(p, n)* right away and hence speeds up the calculations roughly by a factor of 2. In the range 10 5 *< p <* 10 7 we used only the second method and considered only pairs with even *n* ≥ 10 that passed the parity test. The running times were 20 minutes up to 10 6 and 25 hours up to 10 7. Of the 92782 pairs *(p, n)* with 10 5 *< p <* 10 7, 8 *< n < p* − 1 and *n* even, only 913 passed the first test *tn(*1*)* = *t* and only two satisfied *t* *n*

*(η)* = *t* for 1 ≤ *η* ≤ 6, namely *(*226129*,*336*)* and (3041407,18), with *t* = 2 and
*t* = 9387, respectively, and in both cases the test failed for *η* = 7, so that these pairs are also not special. (The above-noted constancy of *tn(η)*−*t* did not occur here.) This verifies Conjecture 4.3 for all *(p, n)* with *p <* 10 7. We now turn to special primes. Here we could of course use the same methods, with *t* = 1, but now there is a much faster way. By the parity observation above, a prime *p* = *n* 2 + *n*+ 1 can only be special if 2 ∈ *Dn*, i.e., if 2 *n*+1 ≡ 1*(*mod*p)*. (This is a special case of the fact mentioned in Section 1 that *d* ∈ *Dn*for every divisor *d* of *n*.) This can be tested extremely rapidly—so rapidly, indeed, that it is not even worth testing first whether *p* is prime, since this actually takes longer. (Even the weaker pseudoprimality tests for a large number *p* involve calculating *a* *p*−1 or *a* *(p*−1*)/*2 for several values of *a*, and here we need only a single such calculation and with a smaller exponent.) We can speed up the search even more by restricting *n* to certain congruence classes, as indicated below, but since it is so rapid to search for solutions of 2 *n*+1 ≡ 1*(*mod*n* 2 + *n* + 1*)* we first did this for all (even) *n* up to 5 × 10 9 (this took about four hours), finding only the following seven solutions in this range:

*n* 2 8 24 90 512 134217728 297474474 *p* 7 73 601 8191 262657 18014398643699713 88491062979051151

The third, fourth and fifth of these can be checked directly not to be special. The sixth can be eliminated because *p* is not prime (it factors as 2593 × 71119 × 97685839) and the seventh because it fails to satisfy the congruence *n* ≡ 8 *(*mod 24*)*, which is a nec- essary condition for *(n, p)* to be special. (The divisibility of *n* by 8 was proved by Feit in the previously cited paper [4], and we must have *n* ≡ 2 *(*mod 3*)* because both *n* 3

and *n* *n*+1 are congruent to 1 modulo *p*.) Hence in this range only the values *n* = 2 and *n* = 8 give special primes. Continuing the search up to 2 × 10 11, now with *n* restricted to the congruence class 8 (mod 24), led to no further solutions (computation time roughly 3 days), verifying the non-existence of non-Desarguesian flag-transitive projective planes for *n <* 2 × 10 11, or *p <* 4 × 10 22.

*Acknowledgments.* The first author is a Postdoctoral Fellow of the Fund for Scientific Research — Flanders (Belgium).

## References

[1] Beth, T., Jungnickel, D., Lenz, H.: Design Theory, Vol. I. 2nd ed., Encyclopedia Math. Appl. 69, Cambridge Univ. Press, Cambridge (1999) Zbl 0945.05004 MR 1729456

<!-- Page 18 -->

[2] Chowla, S. A.: A property of biquadratic residues. Proc. Nat. Acad. Sci. India Sect. A **14**, 45–46 (1944) Zbl 0063.00871 MR 0014119 [3] Dembowski, P.: Finite Geometries. Ergeb. Math. Grenzgeb. 44, Springer, New York (1968) Zbl 0159.50001 MR 0233275 [4] Feit, W.: Finite projective planes and a question about primes. Proc. Amer. Math. Soc. **108**, 561–564 (1990) Zbl 0737.05022 MR 1002157 [5] Fink, J. B.: A note on sharply flag-transitive projective planes. In: N. L. Johnson, M. J. Kalla- her and C. T. Long (eds.), Finite Geometries, in honor of T. G. Ostrom (Pullman, WA, 1981), Lecture Notes in Pure Appl. Math. 82, Dekker, New York, 161–164 (1983) Zbl 0532.51011 MR 0690803 [6] Fink, J. B.: Flag-transitive projective planes. Geom. Dedicata **17**, 219–226 (1985) Zbl 0569.51006 MR 0779176 [7] Gordon, B., Mills, W. H., Welch, L. R.: Some new difference sets. Canad. J. Math. **14**, 614– 625 (1962) Zbl 0111.24201 MR 0146135 [8] Higman, D. G., McLaughlin, J. E.: Geometric *ABA*-groups. Illinois J. Math. **5**, 382–397 (1961) Zbl 0104.14702 MR 0131216 [9] Hughes, D. R., Piper, F. C.: Projective Planes. Springer, New York (1973) Zbl 0267.50018 MR 0333959 [10] Kantor, W. M.: Primitive groups of odd degree and an application to finite projective planes.

J. Algebra **106**, 15–45 (1987) Zbl 0606.20003 MR 0878466
[11] Lehmer, E.: On residue difference sets. Canad. J. Math. **5**, 425–432 (1953) Zbl 0052.03904 MR 0056007 [12] Ott, U.: Flag-transitive projective planes and power residue difference sets. J. Algebra **276**, 663–673 (2004) Zbl 1049.05013 MR 2058461 [13] Paley, R. E. A. C.: On orthogonal matrices. J. Math. Phys. **12**, 311–320 (1933) Zbl 0007.10004 [14] Thas, K.: Finite flag-transitive projective planes: a survey and some remarks. Discrete Math. **266**, 417–429 (2003) Zbl 1026.51005 MR 1991732 [15] Yuan, P., Yahui, H.: A note on power residue difference sets. J. Algebra **291**, 269–273 (2005) Zbl 1074.05019 MR 2158523