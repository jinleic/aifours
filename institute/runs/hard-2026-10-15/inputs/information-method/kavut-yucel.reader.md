URL: https://arxiv.org/pdf/0808.0684
Content-Type: text/markdown
Method: arxiv
Notes: Fetching PDF for full content...; PDF converted via markit

---

# 9-variable Boolean Functions with Nonlinearity 242 in the Generalized Rotation Class

**Authors:** Selcuk Kavut, Melek Diker Yucel
**Published:** 2008-08-05
**Categories:** cs.CR, cs.IT
**arXiv:** 0808.0684

---

## Abstract

In 2006, 9-variable Boolean functions having nonlinearity 241, which is strictly greater than the bent concatenation bound of 240, have been discovered in the class of Rotation Symmetric Boolean Functions (RSBFs) by Kavut, Maitra and Yucel. To improve this nonlinearity result, we have firstly defined some subsets of the n-variable Boolean functions as the "generalized classes of k-RSBFs and k-DSBFs (k-Dihedral Symmetric Boolean Functions)", where k is a positive integer dividing n and k-RSBFs is a subset of l-RSBFs if k < l. Secondly, utilizing the steepest-descent like iterative heuristic search algorithm used previously to identify the 9-variable RSBFs with nonlinearity 241, we have made a search within the classes of 3-RSBFs and 3-DSBFs. The search has accomplished to find 9-variable Boolean functions with nonlinearity 242 in both of these classes. It should be emphasized that although the class of 3-RSBFs contains functions with nonlinearity 242; 1-RSBFs or simply RSBFs, which is a subset of 3-RSBFs, does not contain any. This result also shows that the covering radius of the first order Reed-Muller code R(1, 9) is at least equal to 242. Thirdly, motivated by the fact that RSBFs are invariant under a special permutation of the input vector, we have classified all possible permutations up to the linear equivalence of Boolean functions that are invariant under those permutations. Specifically, for 9-variable Boolean functions, 9! possible permutations are classified into 30 classes; and the search algorithm identifies some of these classes as "rich". The rich classes yield new Boolean functions with nonlinearity 242 having different autocorrelation spectra from those of the functions found in the generalized 3-RSBF and 3-DSBF classes.

---

## Full Paper

<!-- Page 1 -->

# 9-variable Boolean Functions with Nonlinearity 242 in the Generalized Rotation Class<sup>∗</sup>

† †

#### Sel¸cuk Kavut and Melek Diker Y¨ucel

Abstract

In 2006, 9-variable Boolean functions having nonlinearity 241, which is strictly greater than the bent concatenation bound of 240, have been discovered in the class of Rotation Symmetric Boolean Functions (RSBFs) by Kavut, Maitra and Y¨ucel. To improve this nonlinearity result, we have firstly defined some subsets of the n-variable Boolean functions as the “generalized classes of k-RSBFs and k-DSBFs (k-Dihedral Symmetric Boolean Functions)”, where k is a positive integer dividing n and k-RSBFs is a subset of l-RSBFs if k < l. Secondly, utilizing the steepest-descent like iterative heuristic search algorithm used previously to identify the 9-variable RSBFs with nonlinearity 241, we have made a search within the classes of 3-RSBFs and 3-DSBFs. The search has accomplished to find 9-variable Boolean functions with nonlinearity 242 in both of these classes. It should be emphasized that although the class of 3- RSBFs contains functions with nonlinearity 242; 1-RSBFs or simply RSBFs, which is a subset of 3-RSBFs, does not contain any. This result also shows that the covering radius of the first order Reed-Muller code R(1, 9) is at least equal to 242. Thirdly, motivated by the fact that RSBFs are invariant under a special permutation of the input vector, we have classified all possible permutations up to the linear equivalence of Boolean functions that are invariant under those permutations. Specifically, for 9-variable Boolean functions, 9! possible permutations are classified into 30 classes; and the search algorithm identifies some of these classes as rich. The rich classes yield new Boolean functions with nonlinearity 242 having different autocorrelation

## arXiv:0808.0684v1 [cs.CR] 5 Aug 2008

spectra from those of the functions found in the generalized 3-RSBF and 3-DSBF classes. However, there is no zero value in the Walsh spectra of these functions; hence, none of them can be linearly transformed to 9-variable balanced functions with nonlinearity 242.

Keywords: Boolean Functions, Combinatorial Problems, Cryptography, Dihedral Symmetry, Nonlinearity, Rotational Symmetry.

<sup>∗</sup>This work is based on the conference papers [14] and [15]. <sup>†</sup>Department of Electrical Engineering and Institute of Applied Mathematics, Middle East Technical University – ODTÜ, 06531 Ankara, Turkey. Email: {kavut, melekdy}@metu.edu.tr.

<!-- Page 2 -->

### 1 Introduction

On odd number of input variables n, constructing Boolean functions with maximum possible nonlinearity is an unsettled open problem in the area of cryptography and combinatorics. The problem is also related to the upper bound ⌊2<sup>n−1</sup> − 2<sup>n</sup><sup>2</sup> <sup>−1</sup>⌋ on the covering radius of the first order Reed-Muller code [8], which is later improved [9] as 2⌊2<sup>n−2</sup> − 2<sup>n</sup><sup>2</sup> <sup>−2</sup>⌋. Boolean functions on even number of input variables n, attaining maximum nonlinearity of (2<sup>n−1</sup> − 2<sup>n</sup><sup>2</sup> <sup>−1</sup>) are called the bent functions [21]. For odd n, the nonlinearity value <sup>n−1</sup> n−1 (2 − 22) is known as the bent concatenation bound, since the concatenation of two bent functions on (n − 1) variables yields n-variable functions achieving this bound. In

Table 1, we present the bent concatenation bound for 7 ≤ n ≤ 15, together with recent

nonlinearity results.

Table 1. Summary of Nonlinearity Results for n = 7, 9, 11, 13, 15.

n 7 9 11 13 15 <sup>n−1</sup> n−1 Bent Concatenation Bound: 2 − 2256 240 992 4032 16256 Nonlinearity Results in [11] − 241 994 4036 16264 Our Nonlinearity Results − 242 996 4040 16272 Patterson-Wiedemann Construction [19] − − − − 16276 Upper Bound [9] 56 244 1000 4050 16292

For odd n ≤ 7, it is known that the maximum nonlinearity is equal to the bent concatenation bound [1, 18]. Clearly, as the number of n-variable Boolean functions (2<sup>2</sup><sup>n</sup>) increases super-exponentially as n increases, exhaustive search of the whole space is not feasible for n ≥ 7 with currently available hardware. Therefore, for any search attempt, different subclasses of Boolean functions are always significant and interesting. In 1983, Patterson and Wiedemann [19] demonstrated a construction in the idempotent class, of 15-variable Boolean functions with nonlinearity 16276 (exceeding the bent concatenation bound by 20), using combinatorial techniques and search methods. Since <sup>n−1</sup> n−1 n−15 then, it has been possible to get functions with nonlinearity (2 − 22+ 20 × 22) for n−15 odd n ≥ 15, which exceeds the bent concatenation bound by 20 × 22. Until 2006, the maximum nonlinearity known for the cases of n = 9, 11, 13 was equal to the bent concatenation bound. In 2006, 9-variable Rotation Symmetric Boolean Functions (RSBFs) with <sup>9−1</sup> 9−1 nonlinearity 241 (= 2 − 22+ 1) were discovered [11], which led to the construction n−9 of functions with nonlinearity exceeding the bent concatenation bound by 1 × 22, for odd n ≥ 9 (see Table 1). Such functions were attained utilizing the steepest-descent like iterative algorithm that first appeared in [13] and then suitably modified in [11] for a search in the class of RSBFs. The class of Rotation Symmetric Boolean Functions seems to be rich in terms of highly nonlinear functions and there is a close relation between RSBFs and idempotents [5, 6]. Considering a Boolean function f as a mapping from GF (2<sup>n</sup>) → GF (2), the functions for which f (α²) = f (α) for any α ∈ GF (2<sup>n</sup>), are referred to as idempotents. As pointed

<!-- Page 3 -->

out in [5, 6], the idempotents can be regarded as Rotation Symmetric Boolean Functions with proper choice of basis. In [19], 15-variable Patterson-Wiedemann functions having nonlinearity 16276 are also identified in the idempotent class. 2n As the space of the RSBF class is much smaller (≈ 2n) than the total space of Boolean functions (2<sup>2</sup><sup>n</sup>) on n variables, it is possible to exhaustively search the space of RSBFs up to a certain value of n. In [10], an exhaustive search carried out for the whole space (2<sup>60</sup>) of 9-variable RSBFs exploiting some combinatorial results related to the Walsh spectra of RSBFs, has shown that there is no RSBF having nonlinearity greater than 241. Consequently, in order to find functions with higher nonlinearity, one needs to increase the search space. Motivated by this fact, we have firstly proposed the generalized k-RSBFs, as functions which satisfy f (α²<sup>k</sup>) = f (α), where 1 ≤ k | n. Note that if k = 1, the resulting functions are the same as idempotents; whereas for k = n the entire space of n-variable Boolean functions is covered. In the space of generalized k-RSBFs, imposing the condition of invariance under the action of dihedral group, we have defined the class of generalized k-DSBFs as a subset of k-RSBFs. Secondly, we have used the steepest-descent like iterative algorithm in [11] for a search in the generalized 3-DSBF and 3-RSBF classes. This search has successfully ended up with 9- variable functions in both of these classes, having nonlinearity 242, absolute indicator values 32, 40 and 56. This result shows that the covering radius of the first order Reed-Muller code R(1, 9) is at least 242. This result is also important for n = 11 and n = 13, since the bent concatenation of 9-variable functions with nonlinearity 242 leads to the construction <sup>n−1</sup> n−1 n−9 of 11-variable and 13-variable functions with nonlinearity (2 − 22+ 2 × 22), which n−9 exceeds the bent concatenation bound by 2 × 22(see Table 1). However, we should <sup>n−1</sup> n−1 n−15 mention that for odd n ≥ 15, the nonlinearity (2 − 22+ 20 × 22) given in [19] that can be obtained by concatenating 15-variable Patterson-Wiedemann functions is still <sup>n−1</sup> n−1 n−9 greater than the nonlinearity (2 − 22+ 2 × 22). Thirdly, knowing the fact that RSBFs, DSBFs, as well as the generalized k-RSBFs and k-DSBFs are invariant under some special types of permutations on input vectors, we have focused on the same search problem from a different direction and considered the possibility of other ‘rich’ classes that are invariant under some permutations. Linearly equivalent Boolean functions have the same nonlinearity; therefore, while searching for highly nonlinear functions, it is quite logical to classify all n! permutations up to the linear equivalence of Boolean functions that are invariant under them. More specifically, for 9- variable Boolean functions, we have classified 9! many permutations into 30 classes which are different up to the linear equivalence of Boolean functions that are invariant under them. Then for each class, by picking up a representative permutation arbitrarily, we have searched the corresponding set of Boolean functions. Consequently, in some of these sets, we have obtained 9-variable Boolean functions with nonlinearity 242 and absolute indicator values 40, 48 & 56. So, our aim of defining other ‘rich’ classes is accomplished. We note that, however, the functions presented in this paper do not contain any zero in their Walsh spectra, and hence, they cannot be linearly transformed to balanced functions.

<!-- Page 4 -->

In the following section, after reviewing some basic definitions related to Boolean functions, we present preliminaries of permutation group actions. In Section 3, we introduce the generalized rotation symmetric and dihedral symmetric Boolean functions. Classification of permutations on inputs of 9-variable Boolean functions, with respect to the linear equivalence of Boolean functions that are invariant under them, is presented in Section 4. Different results related to 9-variable Boolean functions with nonlinearity 242 are presented in both Section 3 and Section 4. Finally, some additional 11 and 13-variable DSBFs, which are attained by the steepest-descent like search algorithm with nonlinearities 994 and 4036 respectively, are presented in Section 3. It should be noticed that those functions have exactly the same nonlinearities, as those would be obtained by concatenating 9-variable functions with nonlinearity 241.

### 2 Preliminaries

#### 2.1 Boolean Functions

An n-variable Boolean function f (x) produces a single-bit result for each n-bit input vector x = (x₀,..., x<sub>n−1</sub>), which may be considered as a mapping from {0, 1}<sup>n</sup> into {0, 1}. f (x) is basically represented by its truth table, that is, a binary vector of length 2<sup>n</sup>,

f = [f (0, 0,..., 0), f (1, 0,..., 0), f (0, 1,..., 0),..., f (1, 1,..., 1)].

We represent the set of all n-variable Boolean functions by B<sub>n</sub>; clearly |B<sub>n</sub>| = 2<sup>2</sup><sup>n</sup>. A binary vector g has the Hamming weight wt(g) equal to the number of its nonzero elements. The Hamming distance between two binary vectors g and h, both having the same length, is defined as the number of places for which g and h differ, i.e., d(g, h) = wt(g ⊕ h), where ⊕ denotes the addition over GF (2). An n-variable Boolean function f is called balanced if wt(f) = 2<sup>n−1</sup>. The algebraic normal form (ANF) of a Boolean function is defined as its unique representation in the form of a multivariate polynomial over GF (2), ⊕ ⊕ f (x₀,..., x<sub>n−1</sub>) = c ⊕ a<sub>i</sub>x<sub>i</sub> ⊕ a<sub>ij</sub>x<sub>i</sub>x<sub>j</sub> ⊕... ⊕ a<sub>01...n−1</sub>x₀x₁... x<sub>n−1</sub>, 0≤i≤n−1 0≤i<j≤n−1

where the coefficients c, a<sub>i</sub>, a<sub>ij</sub>,..., a<sub>01...n−1</sub> ∈ {0, 1}. The algebraic degree, or simply the degree of f, is the number of variables in the highest order product term with nonzero coefficient, which is denoted by deg(f). A Boolean function is called affine if its degree is at most one. The set of all n-variable affine functions is represented by A<sub>n</sub>. The nonlinearity of an n-variable Boolean function f is defined as its minimum distance to any affine function, i.e.,

nl(f) = min (d(f, g)). g∈A<sub>n</sub>

Boolean functions used in cryptographic systems must be highly nonlinear to resist Best Affine Approximation (BAA) and correlation attacks [3, 4].

<!-- Page 5 -->

The Walsh transform of an n-variable Boolean function f (x) is an integer valued function over {0, 1}<sup>n</sup> defined as ∑ f (x) <x,w> W<sub>f</sub> (w) = (−1) (−1), x∈{0,1}<sup>n</sup>

where x = (x₀,..., x<sub>n−1</sub>), w = (w₀,..., w<sub>n−1</sub>) ∈ {0, 1}<sup>n</sup> and < x, w >= x₀w₀ ⊕... ⊕ x<sub>n−1</sub>w<sub>n−1</sub>. The nonlinearity of an n-variable Boolean function f (x) can be alternatively expressed by means of its Walsh spectrum, i.e.,

1 nl(f) = (2<sup>n</sup> − max |W<sub>f</sub>(w)|. 2 w∈{0,1}<sup>n</sup>

The autocorrelation function of f (x) is given by ∑ r<sub>f</sub>(d) = (−1) f (x) (−1) f (x⊕d), x∈{0,1}<sup>n</sup>

where d = (d₀,..., d<sub>n−1</sub>) ∈ {0, 1}<sup>n</sup>. The autocorrelation value having maximum magnitude except the origin is also known as the absolute indicator [24] and denoted as

∆<sub>f</sub> = max |r<sub>f</sub>(d)|. d=(0,...,0)∈{0,1}<sup>n</sup>

A Boolean function is balanced if and only if its Walsh spectrum value is zero at the origin. On the other hand, if an unbalanced Boolean function g(x) contains a zero in its Walsh spectrum except the origin, say W<sub>g</sub>(u) = 0 and u = (0,..., 0), it can be linearly transformed into a balanced function f (x) = g(x)⊕ < x, u >, which has the same nonlinearity and absolute indicator; i.e., nl(f) = nl(g) and ∆<sub>f</sub> = ∆<sub>g</sub>.

#### 2.2 Group Action by Permutation Groups

A group G is said to act on a set X if there is a mapping φ : G × X → X denoted as g · x, which satisfies the following two axioms for all elements x ∈ X.

1. e · x = x where e stands for the identity element of G.
2. g · (h · x) = (gh) · x for all g, h ∈ G.
The mapping φ is called the group action and the set X is called a G-set. The orbit of x is defined as the set G(x) = {g · x | g ∈ G}, i.e., the group action moves x to its orbit. As the set of orbits of X under the action of G, denoted by G, constitutes a partition of X, the corresponding equivalence relation is defined by x ∼ y iff there exists a g ∈ G such that g · x = y. Hence, the orbits form the equivalence classes under this relation.

<!-- Page 6 -->

Let G be a permutation group acting on {0, 1}<sup>n</sup>, and consider the class of n-variable Boolean functions which are invariant under the action of G, i.e., any Boolean function f in the class satisfies the condition for each x ∈ {0, 1}<sup>n</sup>, f (x) = f (y), for all y ∈ G(x). As a consequence of the invariance property, the class composes a subclass of B<sub>n</sub>, and knowing the number of orbits, i.e., |G|, it contains 2 |G| many n-variable Boolean functions, each satisfying the given condition. The value of |G| can be determined using Burnside’s Lemma.

Lemma 1 (Burnside’s Lemma) Let G be a group of permutations acting on a set X, and f ix<sub>X</sub>(g) = {x ∈ X | g · x = x} for each g ∈ G. Then the number of orbits induced on X is given by 1 ∑ |f ix<sub>X</sub>(g)|. |G| g∈G

Let us represent an orbit by its lexicographically first element denoted by Λ<sub>i</sub>. The Boolean function f which is invariant under the action of G, can be represented by (f (Λ₀),..., f (Λ|G|−<sub>1</sub>)), where Λ₀,..., Λ|G|−<sub>1</sub> are again arranged lexicographically. Clearly, this representation is shorter than the truth table of f. Further, it can be shown [23] that W<sub>f</sub>(u) = W<sub>f</sub>(v) if u ∈ G(v), implying that the Walsh spectrum of f can be at most |G| ∑ <x,Λ > valued. Then, defining a |G| × |G| matrix M as M<sub>i,j</sub> = x∈GΛ (−1) <sub>j</sub>, the Walsh <sub>i</sub> spectrum of f can be calculated as [23]

|G|− ∑<sup>1</sup> W<sub>f</sub>(Λ<sub>j</sub>) = (−1) f (Λ<sub>i</sub> <sup>)</sup> M<sub>i,j</sub>. i=0

### 3 Generalized Rotation and Dihedral Symmetric Boolean Functions

After briefly summarizing RSBFs, we propose the generalized classes of k-RSBFs and k- DSBFs in Definition 1 and Definition 2 respectively. Letting (x₀, x₁,..., x<sub>n−1</sub>) ∈ {0, 1}<sup>n</sup>, the (left) i-cyclic shift operator ρ<sup>in</sup> on n-tuples is defined as

ρ<sup>in</sup>(x₀, x₁,..., x<sub>n−1</sub>) = (x(0+i) mod n,..., x(n−1+i) mod n),

for 1 ≤ i ≤ n. A Boolean function f is called rotation symmetric if for each input (x₀,..., x<sub>n−1</sub>) ∈ {0, 1}<sup>n</sup>, f (ρ<sup>1n</sup>(x₀,..., x<sub>n−1</sub>)) = f (x₀,..., x<sub>n−1</sub>). That is, RSBFs are invariant under all cyclic rotations of the inputs. The inputs of a rotation symmetric Boolean function can be divided into orbits so that each orbit consists of all cyclic shifts of one input. An orbit generated by (x₀, x₁,..., x<sub>n−1</sub>) is denoted by G<sub>n</sub>(x₀, x₁,..., x<sub>n−1</sub>) = {ρ<sup>in</sup>(x₀, x₁,..., x<sub>n−1</sub>) | 2n 1 ≤ i ≤ n} and the number of such orbits is represented by g<sub>n</sub> (≈ 2n). More specifically,

<!-- Page 7 -->

∑n g<sub>n</sub> is equal to n t|n φ(t)2 <sup>t</sup> [22], where φ(t) is the Euler’s phi-function. The total number of n-variable RSBFs is 2<sup>g</sup><sup>n</sup>. In the following, we define the generalized RSBFs as k-rotation symmetric Boolean functions (k-RSBFs).

Definition 1 Let 1 ≤ k ≤ n, k | n. An n-variable Boolean function f is called k-rotation symmetric if for each input (x₀,..., x<sub>n−1</sub>) ∈ {0, 1}<sup>n</sup>, f (ρ<sup>kn</sup>(x₀,..., x<sub>n−1</sub>)) = f (x₀,..., x<sub>n−1</sub>).

As can be seen, the k-rotation symmetric Boolean functions are invariant under k-cyclic rotations of inputs. Therefore, an orbit of a k-RSBF generated by (x₀, x₁,..., x<sub>n−1</sub>) is G<sup>kn</sup>(x₀, x₁,..., x<sub>n−1</sub>) = {ρ<sup>in</sup>(x₀, x₁,..., x<sub>n−1</sub>) | i = k, 2k, 3k,..., n}. For example, G³⁹(001 001 111) = {(001 001 111), (001 111 001), (111 001 001)}. If g<sub>n,k</sub> is the number of distinct orbits in the class of k-RSBFs of n variables, one can k ∑n k× <sup>2n</sup> show that g<sub>n,k</sub> = n t| <sup>n</sup> φ(t)2 <sup>t</sup> (≈ 2n), where φ(t) is the Euler’s phi function. <sub>k</sub> The class of Dihedral Symmetric Boolean Functions (DSBFs) [17], a subset of the RSBF class, is invariant under the action of the dihedral group denoted by D<sub>n</sub>. In addition to the (left) i-cyclic shift operator ρ<sup>in</sup> on n-tuples, which is defined previously, the dihedral group D<sub>n</sub> also includes the reflection operator τ<sub>n</sub>(x₀, x₁,..., x<sub>n−1</sub>) = (x<sub>n−1</sub>,..., x₁, x₀). The 2n permutations of D<sub>n</sub> are then defined as {ρ<sup>1n</sup>, ρ<sup>2n</sup>,..., ρ<sup>n−1n</sup>, ρ<sup>nn</sup>, τ<sub>n</sub>ρ<sup>1n</sup>, τ<sub>n</sub>ρ<sup>2n</sup>,..., τ<sub>n</sub>ρ<sup>n−1n</sup>, τ<sub>n</sub>ρ<sup>nn</sup>}. The dihedral group D<sub>n</sub> generates equivalence classes in the set {0, 1}<sup>n</sup> [20]. Let d<sub>n</sub> be the number of such partitions. The following proposition gives the exact count of d<sub>n</sub> [7, page 184], [17].

Proposition 1 Let d<sub>n</sub> be the total number of orbits induced by the dihedral group D<sub>n</sub> act- <sup>n</sup> 1 ∑n ing on {0, 1}. Then d<sub>n</sub> = g<sub>n</sub>/2 + l, where, g<sub>n</sub> = n t|n φ(t)2 <sup>t</sup> is the number of rotation symmetric classes [22], φ(t) is the Euler’s phi-function and { <sup>3</sup> n <sub>4</sub>2 <sup>2</sup>, if n is even, l = n−1 22, if n is odd.

<sup>d</sup><sup>n</sup> 2n Since there are 2 many n-variable DSBFs and d<sub>n</sub> ≈ 2 <sup>2n</sup>, a reduction in the size of the search space over the size of RSBFs is provided.

Definition 2 Let 1 ≤ k ≤ n, k | n. An n-variable Boolean function f is called k-dihedral symmetric if f is invariant under the group action D<sup>kn</sup> = {ρ<sup>in</sup>, τ<sub>n</sub>ρ<sup>in</sup> | i = k, 2k, 3k, ..., n}.

As the class of DSBFs is a subspace of k-DSBFs, we call k-DSBFs “generalized dihedral symmetric Boolean functions”. One should observe that k-DSBFs is a subspace of k- RSBFs. When Proposition 1 is applied to k-dihedral symmetric functions, we obtain the following corollary.

<!-- Page 8 -->

Corollary 1 Let d be the number of distinct orbits, in the class of k-DSBFs of n vari-

||<sub>n,k</sub>||||||
|---|---|---|---|---|---|---|
|||k||n|||
|ables.|Then, d<sub>n,k</sub> = g<sub>n,k</sub>/2 + l, where, g|= n|t| <sup>n</sup><sub>k</sub>|<sup>t</sup>|||
||<sup>n</sup> <sup>−1</sup> <sup>2</sup>, if n is even, k is even,||||||
||n||||||
|l =|<sup>3</sup>2 <sup>2</sup>, if n is even, k is odd, <sub>4</sub>||||||
||n−1 2 2, if n is odd.||||||
|Table|2.|<sub>n</sub>, d<sub>n</sub>|<sub>n,k</sub>|<sub>n,k</sub>|||
||k 2|3|4|5||6 7|
||n g₄ = 6 g<sub>4,k</sub> 10|–|–|–||– –|
||4 d₄ = 6 d<sub>4,k</sub> 7 g₆ = 14 g<sub>6,k</sub> 24|– 36|– –|– –||– – – –|
||6 d₆ = 13 d<sub>6,k</sub> 16 g₈ = 36 g<sub>8,k</sub> 70|24 –|– 136|– –||– – – –|
||8 d₈ = 30 d<sub>8,k</sub> 43 g₉ = 60 g<sub>9,k</sub> –|– 176|76 –|– –||– – – –|
||9 d₉ = 46 d<sub>9,k</sub> – g₁₀ = 108 g<sub>10,k</sub> 208|104 –|– –|–||– – – –|
||10 d₁₀ = 78 d<sub>10,k</sub> 120 g₁₂ = 352 g<sub>12,k</sub> 700|– 1044|– 1376|–||– – 2080 –|
||12 d₁₂ = 224 d<sub>12,k</sub> 382 g₁₄ = 1182 g<sub>14,k</sub> 2344|570 –|720 –|– –||1072 – – 8256|
||14 d₁₄ = 687 d<sub>14,k</sub> 1236 g₁₅ = 2192 g<sub>15,k</sub> –|– 6560|– –|–||– 4224 – –|
||15 d₁₅ = 1224 d<sub>15,k</sub> –|3408|–|||– – like iterative search|
|3.1|||||||
|||||||<sup>104</sup>|
|242.|||||||

∑ <sub>n,k</sub> φ(t)2 is the number of k-rotation symmetric classes, φ(t) is the Euler’s phi-function and

#####  2

Table 2 compares the orbit counts of k-rotational classes, k-dihedral classes, RSBFs

and DSBFs for k | n, n ≤ 15.

Comparison of the Orbit Counts g, g and d (for n = 4, 6,..., 15, and all integers k, which divide n).

528 288

10944 5600

As mentioned previously, we have utilized the steepest-descent algorithm, which was used to discover 9-variable RSBFs having nonlinearity 241 [11]. The details, which can be found in the related literature, are extraneous for present purposes. We note only that it is an efficient search technique with an outstanding ability to escape from local optima.

#### 9-variable 3-DSBFs and 3-RSBFs

We have applied the search to 9-variable 3-DSBFs for which the size of search space is 2 (see Table 2). We have found several unbalanced Boolean functions having nonlinearity Among them there are two different absolute indicator values, which are 32 and 40.

<!-- Page 9 -->

The following is the truth table of a 9-variable, 3-dihedral symmetric Boolean function having nonlinearity 242, absolute indicator value 40, and algebraic degree 7:

68B7EF2DA03B0D3EA00DB6A96DD99AEAFDB9C842B6D5DC8C4526CE0DD29020DB B75FE3314568344E73688FF0CB2482E065231869E1AA4583765CC491F8A8DB12

And, the function below is another 9-variable 3-DSBF having nonlinearity 242, absolute indicator value 32, and algebraic degree 7:

125425D30A398F36508C06817BEE122E250D973314F976AED58A3EA9120DA4FE 0E4D4575C42DD0426365EBA7FC5F45BE9B2F336981B5E1863618F49474F6FE00

Using a computer system with Pentium IV 2.8 GHz processor and 256 MB RAM, a typical run of the search algorithm takes 1 minute and 17 seconds. We have carried out 100 runs, each each starting with a randomly chosen Boolean function in the space of 9-variable 3-DSBFs. The algorithm has produced 152 functions with the nonlinearity 241, and 36 many 3-DSBFs having nonlinearity 242. Additionally, we have applied the search strategy to 9-variable 3-RSBFs (the size of the search space is now 2<sup>176</sup> as can be seen from Table 2), for which we initiate the search algorithm with a 9-variable 3-DSBF having nonlinearity 242. Then we have obtained some 9-variable 3-RSBFs (which are not in 3-DSBFs) having nonlinearity 242, absolute indicator 56, and algebraic degree 7. The following is the truth table of such a function:

3740B6A118A1E19642A85E2B7E2F3C3CB65FA0D95EC9DB1EA92BDB3666185AE0 087F5FE6E0757106A12FC918754C40E8A1BCCB7A714032A8961456E066E8A801

It is clear that using one of the above 9-variable functions (say f) and a 2-variable bent function (say g), the 11-variable function g(y₀, y₁) ⊕ f (x₀,..., x₈) with highest -till <sup>11−1</sup> 11−1 date-nonlinearity of 2 − 22+ 4 = 996, can be obtained. Similarly h(y₀, y₁, y₂, y₃) ⊕ f (x₀,..., x₈) is the most nonlinear 13-variable function known to date, with nonlinearity <sup>13−1</sup> 13−1 2 − 22+ 8 = 4040 where h is a 4-variable bent function and f is one of the above 9-variable functions with nonlinearity 242. We think this is a significant improvement on <sup>n−1</sup> n−1 n−9 the results of [11]. However, since the nonlinearity (2 − 22+ 2 × 22), which can be obtained by bent concatenation of 9-variable functions with nonlinearity 242 is less than <sup>n−1</sup> n−1 n−15 the nonlinearity (2 − 22+ 20 × 22) given in [19] for odd n ≥ 15, this result is significant only for odd 13 ≥ n ≥ 9.

#### 3.2 11 and 13-variable DSBFs

In [17], the class of Dihedral Symmetric Boolean Functions (DSBFs), a subset of the RSBF class, which is invariant under the action of the dihedral group, is introduced. It has been shown that some of the 9-variable RSBFs having nonlinearity 241 also belong to this subset, demonstrating the richness of DSBFs in terms of high nonlinearity. Motivated by this, we have carried out a systematic search in the DSBF class for 15 > odd n > 9, and found

<!-- Page 10 -->

<sup>n−1</sup> n−1 Boolean functions having nonlinearity > 2 − 2. More specifically, for 11-variable DSBFs, we have attained an 11-variable DSBF with nonlinearity 994 within the space of size 2<sup>126</sup>. For 13-variable DSBFs, in order to reduce the search space (2<sup>380</sup>), we have applied some additional permutations on input vectors, and obtained a subset of size 2<sup>74</sup>, in which we have found several 13-variable DSBFs with nonlinearity 4036. Consequently, our trials confirm that the DSBF class contains highly nonlinear Boolean functions and it is a rich subset of the RSBF class for n = 11, 13, as well. We should also mention that, this is the first demonstration of Boolean functions on odd number of input variables 9 < n < 15 having nonlinearity greater than the bent concatenation bound, which are not obtained by the bent concatenation of 9-variable Boolean functions with nonlinearity > 240. For the 11-variable DSBF case for which the size of search space is 2<sup>126</sup>, we have carried out 8000 runs of the search algorithm, and found the following 11-variable DSBF having nonlinearity 994, absolute indicator value 200, and algebraic degree 9:

68C1F052AA14260999DD0365487844C6C397A7B6114A787724957BC46471F12D F05F873ECC6E8A29034265887BD17A2A483583367B8FF1312C347E12FA1708F3 AA1433AF952B5BE9B5F02CA891985C92114A640C2D6380C57B9BB3027E991D8D 34C45B66D00E5B7D6ACF80EEAB021A430CE54E707AAD520DAB9D472F4081FF1F 89CC06215F1B8CAA973658CF27DAADD3CF36AA0118B0DDC08716D3D526E4C70D 065371D97C2054E458A2390BD550E5736ADAC2DF8B0A10492BACC3C317B381F7 1A21F52076CB3C3DB60144F836DF2AB32DDDE0EAC051FCBD8C8F10491299751F 41F0E96761AC6F053F888DE7234945F79C9B92B3703B19BF6545C557BBBF57FF

A typical run of the search algorithm takes 1 minute and 16 seconds using the same computer system. For the 13-variable DSBF case, since its search space is huge (2<sup>380</sup>), before starting the search we apply the following permutation in addition to the permutations of dihedral group on input vectors

π(x₀, x₁,..., x₁₂) = (x₀, x₂, x₄, x₆, x₈, x₁₀, x₁₂, x₁, x₃, x₅, x₇, x₉, x₁₁)

such that for each input (x₀,..., x₁₂) ∈ {0, 1}¹³,

f (ρ<sup>1n</sup>(x₀,..., x₁₂)) = f (τ<sub>n</sub>(x₀,..., x₁₂)) = f (π(x₀,..., x₁₂)) = f (x₀,..., x₁₂),

and the search space of 13-variable DSBFs is reduced from 2<sup>380</sup> to 2<sup>74</sup>. Note that this permutation constitutes a subset of 13-variable DSBFs for which, using similar combinatorial methods as in [10], it may be possible to carry out an exhaustive search to enumerate 13-variable DSBFs with nonlinearity ≥ 4036, with a reasonable amount of computational power. We have carried out 500 runs of the search algorithm, and found two 13-variable DSBFs having nonlinearity 4036 in this subset. One of them with nonlinearity 4036, absolute indicator value 208, and algebraic degree 10 is given below:

177E7EF97EFCFF937FF8EBA0FAFBC71A7EFBEAD0EC8B8815EA99FADEA12A568D

<!-- Page 11 -->

7EE8EA8BF889B215FDB1848F80950677EDC883D3AE9DB2ED9D031888277CD4F7 7FEDE881ECDC948AFF90D0968B0C0676EFE3CE028524D4FAC114C666116C2A6B F8E2A195815AF71A89FCD3A29B48BDE3C7F6155F139090904C2B2AA1F321AA3F 7EEEF8B2E881D107ECA1E3B5C665D088EAAE9354A710C37C81CB04E4156C3A28 ECAFEC0AB5ED504C85361D75B325AA88F4560730A4386C7C13537CF04CCD299B FA85B81D9C129772D143368CFE2A43C88096AEB4B35E8809D3DE64959BE7A90E A12BBF7D077227FA034FC601D340931535A159CF4C88CC17BB0B4D13C8990BAE 7EFCE8ACEAC18B0DE881C517E253407FF8F4C917EC5E9F32A12C3826F700C081 F889C9F8934B2770DC7B5710F44F2EF09146A5CA1530BD3107663CA14BCD0C81 F9A18DABB9F411C88A26ECF6364474B484321F7D47E33B779B5E58679CCD85D5 FA35626C042E4E419C244A902CF12EF5420E660B6EA0EE0570A0A4B64D86979E FFCDD1728BC516A786F10348976A7F09B212350A0A78D5F1BFA85CD8350BA194 C015D72899F98F208E1B73E9C0950093B24AE7B96C65933782CAFC7BCCD715BC 9D0208CA8AAA7FE2147A2E49192BFBCD145A74FAF0790003E75B7451930B1736 1E76880372D3A1AB70F18590E1F5177A8E8B449F61B2075AF08597D6519ECCE9 7EEDEEF5FC90CDB4ED8CA10785CE10E3E881C147F523072FB81D274B71403EEF FB81AE60F4C6122EB9A032EC96AA5A09C8171CF41ED05879BE7F5444A101D107 EAC481D3A197ABC0825E349E192A7A40A3A07BCA367F5300EE3424AE5DECAB15 C347647CD962E09806265E01DEA75B12117F3C3C1BA1D85771DBA0A751B58512 EE82891381B78D8FCE97AE741242F081C19C593CEDF4EB2C5A3874753A619B21 D1315E5802AE6AE6247FB95F5ECB6B3FC78A22A962842D2F82A1A0A3C026B276 FBDC1B632D1878F144700CFD70EC711687F05D3025D9870548B5AB5708EDAF76 700800F86C2951DB6CECCD01BDED51766E01CD11CD349F7C21A7943CC37ED6A9 EBAFE4B6B2133A49819BF1334739D86BD128EA42504A60C1876E6CCD6FEA11D3 8A1D17180E6650C810D86FD0A622FA179BAED88422E1E3D45F6651CFDD03D734 A0151733A72E48C196D6BE92C4EF4951D5EC028A2F5FE997B00182330101824E DE5934CDAC2FCAD63CF43D33871F0B3EC00CA1DDAAB17BDEA1B5B67E13669EE1 93A6454915D5B5C9D088C8893AABB85D07742AC84CBC20C752C2099EFADBF1F6 077532896E64AB9DFA003F974105110AED6B238E6E753716821F05DE176E5A69 52B97F79C081414F3E08A60BC816CDDE3F41AA17C0779350B912AF76073E7AC9 C5FD819B602186BE79078F5C543E36C9BF158126D33EE6697712D6A9F4E1E997

In this case, a typical run takes one minute using the same computer system. Since these results confirm that the DSBF class contains highly nonlinear Boolean functions on 11 and 13-variables as well, it would be an interesting and open problem to attain some rich subsets achieving higher nonlinearity in the DSBF class.

### 4 Permutations on Input Vectors of 9-variable Boolean Functions

As it is deduced from the discussion in the preceding section, RSBFs are invariant under a special type of permutation. To search for better cryptographic characteristics, we con-

<!-- Page 12 -->

sider the possibility of other classes of Boolean functions that are invariant under some permutations. Since linearly equivalent functions have the same nonlinearity, it makes sense to classify all n! permutations up to the linear equivalence of Boolean functions that are invariant under them. The classification is based on the following proposition, which is easy to prove.

Proposition 2 Let f and g be Boolean functions which are invariant under arbitrary permutations π<sub>f</sub> and π<sub>g</sub> respectively. Then, f and g are said to be linearly equivalent if there exists a bijective linear mapping L : {0, 1}<sup>n</sup> → {0, 1} such that π<sub>f</sub> = (L<sup>−1</sup> ◦ π<sub>g</sub> ◦ L).

Proof. Suppose f (x) = g(L(x)), i.e., f = g ◦ L. Then, it holds that

f = g ◦ L = g ◦ π<sub>g</sub> ◦ L = f ◦ L<sup>−1</sup> ◦ π<sub>g</sub> ◦ L = f ◦ π<sub>f</sub>.

Thus, we classify all possible permutations up to the equivalence

π<sub>f</sub> ∼ π<sub>g</sub> ⇔ ∃L such that π<sub>f</sub> = (L<sup>−1</sup> ◦ π<sub>g</sub> ◦ L).

The classification can be accomplished through a computer program by exploiting the Jordan Normal Form for matrices. Specifically for 9-variable Boolean functions, all permutations of the identity matrix (362, 880 many) yield that there are only 30 permutations (see Table 3), which are different up to the equivalence defined above. Then, we apply the search algorithm for each class using its representative permutation and determine the corresponding nonlinearity given in the last column of Table 3. Our results show the existence of permutations having similar cryptographic characteristics with k-RSBFs and k-DSBFs. From Table 3, it is seen that we have attained several 9-variable Boolean functions with nonlinearity 242, which we initially found in 3-DSBFs and 3-RSBFs, in the classes with sizes 2<sup>100</sup>, 2<sup>104</sup>, 2<sup>140</sup>. In the following, we present 9-variable Boolean functions having nonlinearity 242 and different autocorrelation spectra from those of the functions found in 3-DSBFs and 3-RSBFs. We have applied 100 runs of the search algorithm [11] to the space of size 2<sup>104</sup> and found two 9-variable Boolean functions with nonlinearity 242, absolute indicator value 48, and algebraic degree 7. A typical run takes the same amount of time as for the case of 3-DSBFs (since the sizes of both spaces are the same). One of these functions is given below:

7B8F94BAD364DAC9931906F9465FF33E921E13D7552DAFD684757B662FDA3C68 FA8D94B3C3659B5FCC46FD1518050F97A1E02039AAF74337134F30AB5B41D9DE

which is invariant under the representative permutation

π(x₀, x₁,..., x₈) = (x₀, x₂, x₁, x₄, x₅, x₆, x₇, x₈, x₃).

<!-- Page 13 -->

Table 3. Classification of all possible 362, 880 many permutations for 9-variable Boolean func-

tions, and the best achieved nonlinearity result for each class.

|||Maximum|Total||
|---|---|---|---|---|
|||number of|number of|Best achieved|
|Representative|Number of|input vectors|distinct|nonlinearity|
|permutation (0,1,2,3,4,5,6,7,8)|permutations|in an orbit|orbits|result|
|(identity)|1|1|512|239|
|(5,7,4,8,2,0,6,1,3)|945|2|272|240|
|(3,1,7,0,5,4,6,2,8)|1260|2|288|240|
|(7,1,2,3,5,4,6,0,8)|378|2|320|240|
|(0,8,2,3,4,5,6,7,1)|36|2|384|240|
|(4,6,7,2,8,1,5,3,0)|2240|3|176|242|
|(5,1,2,4,7,8,6,3,0)|3360|3|192|240|
|(0,1,2,8,4,5,6,3,7)|168|3|256|240|
|(1,4,7,5,6,2,0,3,8)|11340|4|140|242|
|(4,7,5,6,0,1,3,2,8)|11340|4|168|240|
|(0,2,1,7,4,3,5,6,8)|7560|4|176|240|
|(0,8,2,3,4,1,6,5,7)|756|4|192|240|
|(0,7,2,5,4,1,3,6,8)|3024|5|128|239|
|(8,7,3,0,1,6,2,4,5)|20160|6|100|242|
|(0,2,1,4,5,6,7,8,3)|30240|6|104|242|
|(7,1,0,3,4,2,8,6,5)|10080|6|112|240|
|(7,4,0,5,1,8,6,2,3)|10080|6|144|240|
|(8,4,3,2,1,7,5,6,0)|2520|6|144|240|
|(0,6,2,7,8,1,5,3,4)|7560|6|160|240|
|(8,1,3,2,4,5,0,7,6)|2520|6|192|240|
|(2,0,6,1,4,5,7,8,3)|25920|7|80|240|
|(0,3,5,8,1,4,7,2,6)|45360|8|72|240|
|(1,6,7,4,8,2,5,3,0)|40320|9|60|241|
|(5,8,6,7,2,0,1,3,4)|9072|10|80|240|
|(1,3,8,7,4,0,6,5,2)|18144|10|96|240|
|(3,5,7,1,6,0,8,2,4)|15120|12|88|240|
|(0,2,7,8,4,6,3,1,5)|15120|12|96|240|
|(4,5,7,1,0,8,3,6,2)|25920|14|60|240|
|(6,5,1,4,7,2,3,0,8)|24192|15|64|238|
|(4,8,1,2,6,7,5,0,3)|18144|20|48|240|

<sup>6</sup>

<sup>3,4</sup>

<sup>2</sup>

<sup>1</sup>

<sup>5</sup>

1 Nonlinearity result of 242 is attained in the subset of size 2<sup>74</sup> in the set of size 2<sup>100</sup>. 2 Nonlinearity result of 242 is attained in the subset of size 2<sup>86</sup> in the set of size 2<sup>140</sup>. 3 Nonlinearity result of 242 is attained in the subset of size 2<sup>104</sup> in the set of size 2<sup>176</sup>. 4 The class contains the permutation corresponding to 3-RSBFs. 5 The class contains the permutation corresponding to RSBFs. 6 The class contains the permutation corresponding to 9-DSBFs.

<!-- Page 14 -->

Then, in order to reduce the search space, we have considered some subclasses. For this purpose, we have applied the reflection operator, which is defined as τ<sub>n</sub>(x₀, x₁,..., x₈) = (x₈,..., x₁, x₀) for 9-variable Boolean functions, in addition to the representative permutation. As a result of this method, we have identified a subset of size 2<sup>74</sup> in the set of size 2<sup>100</sup>. In this subset, we have attained several 9-variable Boolean functions with nonlinearity 242, absolute indicators 40 and 64, and algebraic degree 7. One of them having absolute indicator 64 is provided below:

0331786B34D878855663A2E961F1CB4F779EBBF6881ABB24AC033E6C2B32E049 3D0891DB1888EA5E6F910310311532FC68D5F2A4B5BE6445E41F64299F0CC99A

which is invariant under the permutations of the reflection operator τ<sub>n</sub> and the representative permutation

π(x₀, x₁,..., x₈) = (x₈, x₇, x₃, x₀, x₁, x₆, x₂, x₄, x₅).

For this case, we have carried out 100 runs of the search algorithm resulting in 9 many Boolean functions with nonlinearity 242 such that seven of them with absolute indicator value of 64, and the remaining with that of 40. A typical run takes 1 minute and 4 seconds using the same computer system.

### 5 Conclusions

By suitably generalizing the class of RSBFs, we have introduced k-RSBFs, as functions which satisfy f (α²<sup>k</sup>) = f (α), where the nonzero positive integer k divides n, and α ∈ GF (2<sup>n</sup>). We have also defined the class of k-DSBFs as a subset of k-RSBFs imposing the condition of invariance under the action of dihedral group. Using the steepest-descent like iterative algorithm in [11, 12] for a search in the generalized 3-DSBF and 3-RSBF classes, we have attained 9-variable 3-RSBFs and 3-DSBFs with nonlinearity 242. This result shows n−1 n−9 the existence of n-variable Boolean functions having nonlinearity 2<sup>n−1</sup> − 22+ 2 × 22 for n = 9, 11, 13. In [2], it is conjectured that the covering radius [16, 19] of R(1, n) is even. Our nonlinearity result for n = 9 shows that the covering radius is at least 242 and it is an interesting open question to settle it. The upper bounds presented in [8, 9] for the covering radius of R(1, 9) is 244. Further, we have classified all possible permutations up to the linear equivalence of Boolean functions that are invariant under them. Specifically for n = 9, there are 30 such classes. Exploiting the same search algorithm [11], we have attained 9-variable Boolean functions having nonlinearity 242 in the class of size 2<sup>104</sup>. Then, we have considered some subclasses by adding permutation of the reflection operator τ<sub>n</sub> to the representative permutation and found many functions with nonlinearity 242 shown in Table 3. As an example, we have identified a subset of size as small as 2<sup>74</sup>, in the set of size 2<sup>100</sup>, having 9-variable Boolean functions with nonlinearity 242. Considering the combinatorial search techniques in [10], we note that it may be possible to exhaustively search the subset of size

<!-- Page 15 -->

2 for the enumeration of 9-variable Boolean functions having nonlinearity ≥ 242, with a reasonable amount of computational power. Moreover, we have obtained an 11-variable DSBF having nonlinearity 994 and several 13-variable DSBFs having nonlinearity 4036, which confirm the richness of DSBFs [17] in terms of high nonlinearity for n = 11 and 13. We think that the results that we present contain significant information on the existence of maximum nonlinearity-Boolean functions with odd number of input variables, within the classes that are invariant under some permutations.

Acknowledgment. We acknowledge Dr. Gregor Leander for his discussion on linear equivalence of Boolean functions that are invariant under random permutations, which has helped us find one missing class in Table 3.

### References

[1] E. R. Berlekamp and L. R. Welch. Weight distributions of the cosets of the (32, 6) Reed-Muller code. IEEE Transactions on Information Theory, Volume IT-18(1), 203– 207, January 1972.

[2] R. A. Brualdi, N. Cai and V. Pless. Orphan structure of the first order Reed-Muller codes. Discrete Mathematics, Volume 102, pp. 239–247, 1992.

[3] A. Canteaut and M. Trabbia. Improved fast correlation attacks using parity-check equations of weight 4 and 5. In Eurocrypt 2000, Number 1807 in Lecture Notes in Computer Science, pp. 573–588. Springer Verlag, 2000.

[4] C. Ding, G. Xiao, and W. Shan. The Stability Theory of Stream Ciphers. Number 561 in Lecture Notes in Computer Science. Springer-Verlag, 1991.

[5] E. Filiol and C. Fontaine. Highly nonlinear balanced Boolean functions with a good correlation-immunity. Advances in Cryptology-EUROCRYPT’98, Lecture Notes in Computer Science, Springer-Verlag, Volume 1403, 475–488, 1998.

[6] C. Fontaine. On some cosets of the First-Order Reed-Muller code with high minimum weight. IEEE Transactions on Information Theory, Volume IT-45(4), 1237–1243,

1999.
[7] F. Harary. Graph Theory. Addison-Wesley Publishing Company, 1972.

[8] T. Helleseth, T. Kløve and J. Mykkeltveit. On the covering radius of binary codes. IEEE Transactions on Information Theory, Volume IT-24, pp. 627–628, September

1978.
[9] X. -d. Hou. On the norm and covering radius of the first order Reed-Muller codes. IEEE Transactions on Information Theory, Volume IT-43(3), pp. 1025–1027, 1997.

<!-- Page 16 -->

[10] S. Kavut, S. Maitra S. Sarkar and M. D. Y¨ucel. Enumeration of 9-variable Rotation Symmetric Boolean Functions having Nonlinearity > 240. Proceedings in Cryptology-INDOCRYPT 2006, Lecture Notes in Computer Science, Springer-Verlag, Volume 4329, pp. 266–279, 2006.

[11] S. Kavut, S. Maitra and M. D. Y¨ucel. Search for Boolean Functions with Excel- lent Profiles in the Rotation Symmetric Class. IEEE Transactions on Information Theory, Volume IT-53(5), pp. 1743–1751, May 2007. An earlier version of this paper is available under the title “There exist Boolean functions on n (odd) variables <sup>n−1</sup> n−1 having nonlinearity > 2 − 22if and only if n > 7” at IACR eprint server, [http://eprint.iacr.org/2006/181](http://eprint.iacr.org/2006/181), 28 May, 2006.

[12] S. Kavut, S. Maitra, M. D. Y¨ucel. Autocorrelation spectra of balanced boolean func- n+1 tions on odd number input variables with maximum absolute value < 22. Second International Workshop on Boolean Functions: Cryptography and Applications, BFCA 06, Publications of University of Rouen and Havre, pp. 73–86, 2006.

[13] S. Kavut and M. D. Y¨ucel. A new algorithm for the design of strong Boolean functions (in Turkish). In First National Cryptology Symposium, pages 95–105, METU, Ankara, Turkey, November 18–20, 2005.

[14] S. Kavut and M. D. Y¨ucel. Generalized Rotation Symmetric and Dihedral Symmetric Boolean Functions – 9 variable Boolean Functions with Nonlinearity 242. 17<sup>th</sup> International Applied Algebra, Algebraic Algorithms, and Error Correcting Codes (AAECC-

17) Symposium, LNCS vol. 4851/2007, pp. 321–329, Bangalore, India, December 16– 20, 2007. An earlier version of this paper is available under the same title at IACR eprint server, [http://eprint.iacr.org/2007/308](http://eprint.iacr.org/2007/308), Aug 8, 2007).
[15] S. Kavut and M. D. Y¨ucel. Random Permutations on Input Vectors of Boolean Functions. Fourth International Workshop on Boolean Functions: Cryptography and Applications, BFCA’08, Copenhagen, Denmark, May 19–21, 2008.

[16] F. J. MacWillams and N. J. A. Sloane. The Theory of Error Correcting Codes. North Holland, 1977.

[17] S. Maitra, S. Sarkar and D. K. Dalai. On Dihedral Group Invariant Boolean Functions. In Third International Workshop on Boolean Functions: Cryptography and Applications, BFCA’07, University of Rouen, France, May 2–3, 2007.

[18] J. J. Mykkeltveit. The covering radius of the (128, 8) Reed-Muller code is 56. IEEE Transactions on Information Theory, Volume IT-26(3), pp. 359–362, 1980.

[19] N. J. Patterson and D. H. Wiedemann. The covering radius of the (2<sup>15</sup>, 16) Reed-Muller code is at least 16276. IEEE Transactions on Information Theory, Volume IT- 29(3), pp. 354–356, 1983. See also the correction in IEEE Transactions on Information Theory, Volume IT-36(2), 443, 1990.

<!-- Page 17 -->

[20] F. S. Roberts. Applied Combinatorics. Prentice-Hall, Inc, Englewood Cliffs, New Jersey.

[21] O. S. Rothaus. On bent functions. Journal of Combinatorial Theory, Series A, Volume 20, pp. 300–305, 1976.

[22] P. St˘anic˘a and S. Maitra. Rotation Symmetric Boolean functions – count and cryptographic properties. In R. C. Bose Centenary Symposium on Discrete Mathematics and Applications, December 2002. Electronic Notes in Discrete Mathematics, Elsevier, Vol. 15, pp. 139–145.

[23] P. St˘anic˘a, S. Maitra and J. Clark. Results on Rotation Symmetric Bent and Correlation Immune Boolean Functions. Fast Software Encryption Workshop (FSE 2004), New Delhi, INDIA, Lecture Notes in Computer Science, Springer-Verlag, Volume 3017, pp. 161–177, 2004.

[24] X. M. Zhang and Y. Zheng. GAC – the criterion for global avalanche characteristics of cryptographic functions. Journal of Universal Computer Science, Volume 1(5), pp. 316–333, 1995.

Text extraction is incomplete for PDF pages 4. Use the browser prelude to render those pages or OCR them.