# Rank-eight extension: four and five signed defects are impossible

Clock observed before creation: **2026-10-23T14:20:02-07:00**. Author: InfoBalancedNL242, info-6. **CANDIDATE WRITTEN PROOF**, not separately reconstructed, executed, formally checked or novelty-cleared.

This continues the same balanced nine-variable problem, not another slot. Together with the pinned `sparse-defect-proof-v1.md` (SHA256 `0325f3cf3d9131c8e11f524552a715e4ba47e2ff66eabc1010341f136af6c413`), the claim is that either surviving full-polar-rank type `(8,120)` or `(8,136)` requires **at least six** Walsh coefficients of magnitude4 or12. No entire residue type or unrestricted target is excluded.

## 1. Full-rank reconstruction formula

Retain S,D,A,delta and the256-point H from the prior manuscript. Here D has nonsingular polar form B on `V=F_2^8`. Write `chi=(-1)^D`. Its quadratic Walsh spectrum has magnitude16 everywhere. Set `Q=W_D/16`; then Q is a sign function and `H Q=16 chi`.

If `A={u_1,...,u_k}`, with signs epsilon_i=delta(u_i), put

`d_i(x)=epsilon_i(-1)^(u_i.x)`,

`u_I=sum_{i in I}u_i`, `epsilon_I=product_{i in I}epsilon_i`.

The same mod-three rigidity is exact:

`b=(H S)/512=phi(Q-sum_i d_i)`, `S=2H b`.

Multiplication of the sine addition formula gives, for every k,

`b=(-1)^k 2^(-k) [Q P_even - P_odd]`,

`P_even=sum_{|I| even}(-3)^(|I|/2) product_{i in I}d_i`,

`P_odd=sum_{|I| odd}(-3)^((|I|-1)/2) product_{i in I}d_i`.

This is the Q^2=1 specialization of the algebraic derivation in the prior manuscript. It is an identity for the actual signed functions, not a count relaxation. Transforming term by term therefore yields

`S(y)=F(y)+C(y)`,                                        (1)

`F(y)=(-1)^k 2^(5-k) sum_{|I| even}(-3)^(|I|/2) epsilon_I chi(y+u_I)`,

`C(y)=(-1)^(k+1)2^(9-k) sum_{|I| odd}(-3)^((|I|-1)/2) epsilon_I 1_{y=u_I}`.

Let `K=span{u_i+u_1:i=2,...,k}` be the direction space of the affine span of A, of dimension d. All even-subset sums lie in K. It follows from quadratic polarization that `F(y)/chi(y)` is constant on each affine coset of `K-perp_B`, a space of dimension `8-d`.

The correction C is supported in `L=u_1+K`, because every odd-subset sum belongs there. At any y outside L, we are outside A and C=0, so `|F(y)|=|S(y)|` must be20 or28.

**Fiber observation.** If no coset of `K-perp_B` lies wholly in L, every fiber contains a point outside L. Hence `|F(y)| in {20,28}` for **all** y, including the correction support. In particular this holds whenever `2^(8-d)>2^d` (d<=3). For d=4, it holds unless `K=K-perp_B`: both the fiber and L have size16, and containing an entire fiber forces equality of their direction spaces.

## 2. Exactly four defects

Four distinct points have affine dimension2 or3.

### Dimension3

Every odd-subset sum is distinct: the eight odd subsets of four indices map bijectively to L. Formula (1) gives singleton corrections `-32epsilon_i` at A and triple corrections `+96epsilon_I` at the other four points of L.

Fibers have32 points, while L has8, so the fiber observation forces `|F|<=28` everywhere. At a triple-sum point outside A, the correction is uniquely±96. Thus `|S|>=96-28=68`, contradicting the cap28.

### Dimension2

Now `u_1+u_2+u_3+u_4=0`. Let `e=epsilon_1epsilon_2epsilon_3epsilon_4`. Complementary pair sums agree. Dividing F by chi, its even-subset polynomial is

`F/chi =2[1+9e-3(1+e)(r_2+r_3+r_4)]`,

where each `r_j(y)=epsilon_1epsilon_j chi(y+u_1+u_j)/chi(y)` is±1. All odd-subset sums belong to A, so S=F outside A.

If e=-1, F/chi=-16. If e=+1, the sum of three signs is−3,−1,1 or3, so `|F| in {8,16,32,56}`. None is20 or28, which is required at every point outside A. Contradiction.

Thus a=4 is impossible for either full-rank type.

## 3. Exactly five defects

Five distinct points have affine dimension3 or4.

### Dimension3

The map from the four-dimensional space of even subsets of five indices to K has a one-dimensional kernel. Its unique nonempty element P has size4: size2 would identify distinct points. Let j be the index not in P. Then

`sum_{i in P}u_i=0`, `u_{all five}=u_j`.

Exactly two odd subsets map to u_j, namely `{j}` and all five indices. Their correction in (1) is

`C(u_j)=16epsilon_j(1+9epsilon_P)`,

of absolute value160 or128. The fiber observation again makes `|F|<=28` everywhere, since the fibers have32 points and L has8. Hence `|S(u_j)|>=100`, impossible (and u_j is itself a low-magnitude defect).

### Dimension4, K not totally isotropic

The sixteen odd-subset sums are all distinct. At the sum of all five, which is outside A, the correction is uniquely `144epsilon_all`.

If `K!=K-perp_B`, the fiber observation forces `|F|<=28` everywhere, and this point gives `|S|>=116`, impossible.

### Dimension4, K totally isotropic

The only remaining case is `K=K-perp_B`, a Lagrangian four-space. Here L is a whole fiber, and F is not bounded by the preceding outside argument on L. Instead use the **same** constant

`c=F(y)/chi(y)` for every y in L.

A quadratic restricts affinely to L. For any odd subset I, its XOR u_I lies in L and

`chi(u_I)=product_{i in I}chi(u_i)`.

One proof is to write `u_i=u_1+k_i`, with k_i in isotropic K. In the quadratic expansion of an odd XOR, the pairwise B terms cancel: each `B(u_1,k_i)` occurs an even number of times, and `B(k_i,k_j)=0`.

Put `r_i=epsilon_i chi(u_i)`. At a singleton defect u_i, formula (1) gives

`T(u_i)=chi(u_i)S(u_i)=c+16r_i in {-12,4}`.

At the all-five sum, which is not a defect, it gives

`T(u_all)=c+144 product_i r_i in {-28,20}`.

Their difference has absolute value128 or160, since it is `144 product_i r_i-16r_i`. But a value in `{−28,20}` and a value in `{−12,4}` differ by at most40. Contradiction.

Thus a=5 is impossible for either full-rank type.

## 4. Consequence and stopping boundary

The earlier all-type candidate excludes a<=3; the present complete case split excludes a=4,5 for polar rank8. Therefore the two surviving rank-eight types require a>=6, subject to independent written reconstruction of both manuscripts.

Nothing here excludes a>=6, a whole type, or balanced242 existence. At six affinely independent defects, the affine direction space may have dimension5 and the exceptional affine span has32 points, while the basic fibers have only8 points. It can contain entire fibers when `K-perp_B` lies inside K. The fiber argument used at four/five defects then stops. Nontrivial collisions of odd-subset sums also occur at lower affine dimensions. Those are precise additional obligations, not evidence of nonexistence or authority for an enumeration.

No scientific execution has occurred. The argument is a written interpolation/geometry derivation; finite evaluation, formal proof, outside review, novelty and significance remain separate. The bound is a structural restriction, not a change to the best attainable balanced value240.
