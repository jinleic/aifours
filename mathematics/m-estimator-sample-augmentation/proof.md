# Proofs and counterexamples: repeated-design M-estimation

Date: 2026-10-14 (PT). These are written mathematical arguments, not full Lean formalizations. No historical priority claim is made. Theorem 11 refutes broad formalization (c): **written proof, parent-audited, independent Opus referee correct (minor fixes applied); not Lean-certified; not HMZ-accepted**. It requires E|epsilon|=infinity. Cui's unspecified regular-error question and the finite-moment general-convex regime remain open beyond Theorems 9/10. The separate no-tools referee reviewed written mathematics, not Lean artifacts, and does not retroactively supply the stopped HMZ run's missing verdict.

## 1. Definitions: three error couplings and design indexing

Fix a finite dimension p, a deterministic infinite sequence x_i in R^p, a finite convex function rho:R -> R with rho(t) -> infinity as |t| -> infinity, a parameter beta_0, and i.i.d. errors. The loss does not change with n. Write

F_n(b) = sum_{i=1}^n rho(epsilon_i - x_i'(b-beta_0)).

Assume the displayed minimizers exist. Eventually full column rank suffices for the losses used below. An estimator is a specified measurable selection, not the set-valued symbol argmin. When an assertion concerns every selection, this is stated. Weak consistency means convergence in probability; strong consistency means almost-sure convergence on a specified common probability space.

Three error couplings, and a separately enlarged design class, must be distinguished:

* **R: two fixed replicate streams.** Take independent i.i.d. sequences epsilon_i and epsilon_i'. The pooled criterion is F_n + F_n', each using x_1,...,x_n. Both streams are nested as n grows.
* **S: the book-indexed sliding second block.** On one i.i.d. sequence, use epsilon_1,...,epsilon_n for the original experiment and epsilon_{n+1},...,epsilon_{2n} at the repeated rows x_1,...,x_n. The second block is fresh relative to the first at each n, but is not a nested replicate stream across n.
* **I: independent experiment vectors across n.** At each n draw a new independent 2n-vector of i.i.d. errors, using its first n entries for the original estimate and all entries for the pooled estimate. The vectors for different n are independent.
* **T: triangular designs.** The design x_{n,i} is allowed to change at old indices as n changes. This is not a single nested sequence x_i.

R, S, and I have the same distribution at each fixed n, so their weak-consistency questions agree and are coupling-free. Their strong-consistency questions need not agree. T is a genuine enlargement of the book's design-sequence formulation, not a fourth error coupling. Theorem 3 is about S; Theorem 5 is about T only.

## 2. Scalar preservation and least-squares preservation

### Theorem 1 (scalar, unique half minimizers)

Let p=1. Suppose the minimizers a_n of F_n and b_n of its replicate are unique, and both converge to beta_0 in probability. Every minimizer c_n of F_n+F_n' lies in the closed interval with endpoints a_n,b_n. Consequently c_n converges in probability to beta_0. For R, if the original estimator is strongly consistent, the same conclusion holds almost surely.

**Proof.** A convex function with a unique minimizer a is strictly decreasing in the order sense on (-infinity,a] and strictly increasing on [a,infinity): for x<y<=a, the convexity inequality with y between x and a, together with f(a)<f(x), gives f(y)<f(x). Thus the sum cannot attain a minimum below both a_n,b_n or above both. Hence

|c_n-beta_0| <= max(|a_n-beta_0|,|b_n-beta_0|).

The union bound proves the probability statement. For R, the two entire streams have the same law; each strong-convergence event has probability one, and their intersection does too. The identical argument works if all minimizers of each half lie in an interval shrinking to beta_0. It does **not** say that arbitrary chosen minimizers control other points on a flat minimizing interval. QED.

### Theorem 2 (least squares, all dimensions)

If S_n=sum x_i x_i' is invertible, rho(r)=r^2, and a_n,b_n are the two least-squares estimators, the pooled estimator is exactly (a_n+b_n)/2. Therefore weak consistency transfers without moment assumptions, and strong consistency transfers under R.

**Proof.** The pooled normal matrix is 2S_n; its right-hand side is the sum of the two right-hand sides. The formula and convergence claims follow immediately. This argument by itself does not prove strong transfer under S. QED.

## 3. Strong consistency fails for sliding blocks, even for scalar least squares

### Theorem 3

Let p=1, beta_0=0, rho(r)=r^2, epsilon_i independent with probabilities 1/2 each at -1 and +1, and

x_i = 1 if i=4^k for some integer k>=1, and x_i=0 otherwise.

For n>=4 the original estimator is unique and strongly consistent. Its S-pooled estimator is unique and weakly consistent, but almost surely

limsup_n beta_hat_{2n}^{S}=1/2,   liminf_n beta_hat_{2n}^{S}=-1/2.

Thus even bounded, mean-zero, variance-one errors and lambda_min(S_n)->infinity do not give the strong sliding-block implication.

**Proof.** For 4^j<=n<4^{j+1}, exactly j rows are informative. Define

A_j = (1/j) sum_{k=1}^j epsilon_{4^k},
B_n = (1/j) sum_{k=1}^j epsilon_{n+4^k}.

The original estimator is A_j; the pooled estimator is (A_j+B_n)/2. The strong law gives A_j->0 almost surely. At each fixed n the two sums use disjoint indices. Thus the pooled estimator has mean zero and variance 1/(2j), proving weak consistency by Chebyshev.

It remains to control the whole sliding sequence. In the integer interval I_j=[4^j,4^{j+1}-1], put T_n={n+4^k:1<=k<=j}. Two such sets intersect only if

n'-n = 4^a-4^b

for some a,b in {1,...,j}. The graph on I_j connecting intersecting sets has maximum degree at most j(j-1). A greedy independent set C_j therefore has size

M_j >= |I_j|/[j(j-1)+1] = 3*4^j/[j(j-1)+1].

(The usual greedy algorithm selects a vertex and removes it and at most that many neighbors; rounding only improves the inequality.) The sets T_n for n in C_j are pairwise disjoint. Consequently the events {B_n=1} over C_j are independent, each with probability 2^{-j}. Therefore

P(no n in I_j has B_n=1)
 <= (1-2^{-j})^{M_j}
 <= exp(-3*2^j/[j(j-1)+1]).

These probabilities are summable: for all sufficiently large j their exponent is at least j. The same estimate holds for B_n=-1. The first Borel-Cantelli lemma, requiring no independence between different j, implies that every sufficiently large I_j contains both a B_n=1 and a B_n=-1, almost surely. Since A_j->0 and |B_n|<=1, the claimed limsup and liminf follow. QED.

**Scope.** This does not contradict Theorem 2, or ordinary nested-design least-squares consistency theorems. The repeated 2n-row arrays in S are not initial segments of one fixed infinite design. Under R, this **least-squares** estimator is (A_j+A_j')/2 and is strongly consistent; the general scalar convex positive result uses the sandwich argument of Theorem 1, not averaging. Under I, even the **original** estimator in this example fails strong consistency. Indeed, in I_j there are 3*4^j independent original experiments, each with probability 2^{-j} of having all j informative errors equal +1. The probability of no such experiment is at most exp(-3*2^j), which is summable in j; the same is true for -1. Thus the original estimates have limsup +1 and liminf -1 almost surely under I. The counterexample to the implication therefore concerns S, not I. All formulas and uniqueness assertions here use n>=4.

## 4. The Gram eigenvalue condition is not necessary for general convex M-estimation

### Theorem 4A (LAD with an atom: eventual exact recovery)

Take p=1, x_i=1/i, rho(r)=|r|, and probabilities 1/4,1/2,1/4 at errors -1,0,+1. For every beta_0, almost surely the LAD minimizer equals beta_0 uniquely for all sufficiently large n. Nevertheless S_n=sum_{i<=n}i^{-2}<2 for every n.

**Proof.** By translation, set beta_0=0. Let H_n=sum_{i<=n}1/i. The right and left derivatives at zero are

D_n^+ = sum_i [1{epsilon_i=0}+1{epsilon_i=-1}-1{epsilon_i=1}]/i,
D_n^- = sum_i [-1{epsilon_i=0}+1{epsilon_i=-1}-1{epsilon_i=1}]/i.

Their expectations are H_n/2 and -H_n/2. Each centered series converges almost surely because its independent, centered summands have summable variances, bounded by sum i^{-2}. One elementary justification is that the partial sums form an L^2-bounded martingale, hence converge almost surely. Thus D_n^+->+infinity and D_n^-->-infinity almost surely. Eventually D_n^-<0<D_n^+. For a convex function this makes zero the unique global minimizer: its secant slope to any positive point is at least D_n^+>0, and its secant slope from any negative point to zero is at most D_n^-<0. Finally sum i^{-2}<1+integral_1^infinity t^{-2}dt=2. QED.

### Theorem 4B (continuous bounded errors and a flat-bottom loss)

Take x_i=1/i, errors uniform on [-1,1], and rho(r)=(|r|-1)_+, where a_+=max(a,0). Every minimizing selection is strongly consistent for every beta_0, although the same S_n remains bounded.

**Proof.** At beta_0 every loss is zero. Writing h=b-beta_0, the entire minimizing set is exactly the compact interval

[L_n,U_n],  L_n=max_{i<=n} i(epsilon_i-1),  U_n=min_{i<=n} i(epsilon_i+1).

Here L_n<=0<=U_n. For any fixed delta>0 and all sufficiently large i,

P(i(epsilon_i+1)<delta)=delta/(2i).

These independent events have divergent probability sum, so the second Borel-Cantelli lemma gives U_n->0 almost surely. Applying the same argument to 1-epsilon_i gives L_n->0. A countable intersection over positive rational delta proves that the full minimizing interval shrinks to {0}. QED.

Both examples rule out an unqualified claim that lambda_min(S_n)->infinity is necessary for every nondegenerate error law and every convex rho. They do not refute its necessity for Gaussian-error least squares or for appropriately regular identifiable location experiments. Neither example refutes duplication: consistency is preserved, even strongly under S. For 4A, the pooled right derivative has mean H_n and the pooled left derivative has mean -H_n. Each is a sum of 2n independent terms at a fixed n, with ranges of length 2/i occurring twice. Hoeffding's inequality bounds either wrong-sign probability by exp(-H_n^2/(4 S_n))<=exp(-H_n^2/8). Since H_n>=log(n+1), these bounds are summable; the first Borel-Cantelli lemma gives eventual unique recovery at zero. For 4B, every pooled loss remains nonnegative and zero at the truth, and the pooled minimizing interval is contained in the original shrinking interval. For R, the corresponding claims also follow from the two fixed streams.

## 5. A genuine failure under triangular designs, with no arbitrary selection trick

### Theorem 5

There is a fixed finite coercive convex loss, bounded nondegenerate i.i.d. errors, p=4, and deterministic triangular designs for which **every original minimizing selection is strongly consistent**, but **every replicated minimizing selection is weakly inconsistent**. This is not a counterexample for a single nested design sequence.

**Construction.** Let rho(r)=10|r|+(r-1)_+, errors be independent Rademacher variables, and beta_0=0. Fix c=1/10. At stage m use n_m=6m+2 rows and coordinates

z=(u_1,u_2,t,v)=(m beta_1,m beta_2,m beta_3,beta_4).

The first two predictions are u_1 and u_2. For each of the following six linear forms L_r(z), include m rows whose prediction is -(2c/m)L_r(z):

L_1=2(u_1-t), L_2=2(-u_1-t),
L_3=2(u_2+v-t), L_4=2(-u_2+v-t),
L_5=t/2, L_6=(t-v)/2.

This specifies ordinary deterministic design vectors in the beta coordinates. Couple errors by using two fixed high-row errors e_1,e_2 and six independent infinite Rademacher streams for the six groups. All errors within any stage are i.i.d. Use a second independent copy of these eight streams for the repeated experiment. Sizes between n_m and n_{m+1} may be defined by the stage-m design plus zero rows; their extra losses do not affect minimizers.

Define G(z)=sum_{r=1}^6 (L_r(z))_+.

**Lemma 5.1 (the exact geometry).** For fixed u_1,u_2, G has a unique minimizing pair

t=|u_1|, v=|u_1|-|u_2|,

and its minimum is (|u_1|+|u_2|)/2. Moreover G is coercive on R^4.

**Proof.** Fix also v and put M=max(|u_1|,|u_2|+v). Below t=M at least one of the four first positive parts is active, contributing slope -2 with respect to t. The last two terms together contribute slope at most +1; all other active constraint terms contribute nonpositive slopes. Thus G strictly decreases up to M. At t>=M, all constraint penalties vanish, t>=0, and t-v>=0, giving G=t-v/2, strictly increasing in t. Its unique minimizing t is therefore M. The remaining expression max(a,b+v)-v/2, where a=|u_1| and b=|u_2|, strictly decreases until v=a-b and strictly increases afterwards. This proves the formula and uniqueness. G is continuous, positively homogeneous, nonnegative, and zero only at z=0 by the formula and uniqueness. Its minimum on the unit sphere is positive, which proves coercivity. QED.

**Lemma 5.2 (local uniform almost-sure limits).** Subtract the low-row objectives' values at z=0. On every compact set of z, the original objectives converge uniformly almost surely to

Q(z)=rho(e_1-u_1)+rho(e_2-u_2)+cG(z).

The doubled objectives converge similarly to

Q_2(z)=sum_{a=1}^2 [rho(e_a-u_a)+rho(e_a'-u_a)]+2cG(z).

**Proof.** Put d=2c/m. On a fixed compact set, |d L_r|<1 eventually. For one row with prediction -d L and error e,

rho(e+d L)-rho(e)=10 e d L + 1{e=1} d(L)_+.

This is an exact identity in that region. For each group its sum is

20c (m^{-1}sum e_i)L + 2c(m^{-1}sum 1{e_i=1})(L)_+.

The strong law sends the two coefficients to 0 and c. There are only six groups and finitely many linear forms, so convergence is uniform on every compact set, almost surely. A countable sequence of balls makes this simultaneous on all compacts. The duplicate proof is identical. QED.

**Minimizers and limits.** For fixed u_1,u_2, Lemma 5.1 uniquely determines t,v in both limit objectives. The reduced original objective is

sum_{a=1}^2 [rho(e_a-u_a)+(c/2)|u_a|].

Since rho(r)>=10|r| and rho(0)=0, the reverse triangle inequality shows that replacing u_a=e_a by any different value increases this expression by at least (10-c/2)|u_a-e_a|. Thus Q has the unique minimizer

(e_1,e_2,1,0).

For Q_2 the reduced coordinate objective is

rho(e-u)+rho(e'-u)+c|u|.

If e=e', its unique minimizer is u=e by the same inequality. If e=-e', then for -1<=u<=1 its first two terms equal 20+(-u)_+. Adding c|u| makes the unique minimum u=0; convexity excludes minima outside this interval. Write s_a=e_a if e_a=e_a', and s_a=0 otherwise. The unique minimizer of Q_2 is

(s_1,s_2,|s_1|,|s_1|-|s_2|).

For completeness, local uniform convergence of convex functions to a coercive continuous function with a unique minimizer forces every minimizer to converge to that point. Choose a sphere centered at the limiting minimizer on which the limiting objective exceeds its minimum by a positive amount. Uniform convergence on that sphere and at its center gives the same strict inequality for all sufficiently large finite objectives. If one had a minimizer outside the sphere, convexity along the segment from the center to it would contradict the sphere inequality. Compactness then puts all minimizers in any prescribed neighborhood by uniform convergence and the uniqueness gap. In the present construction every finite objective has minimizers: its design has rank four, and rho is coercive, so its objective is coercive.

Consequently all original beta estimates converge almost surely to zero: their first three coordinates are bounded z coordinates divided by m, and their fourth coordinate tends to zero. In the doubled experiment the fourth coordinate converges almost surely to |s_1|-|s_2|, which has probabilities 1/4,1/2,1/4 at -1,0,+1. In particular,

lim_m P(|beta_hat_{2n_m,4}|>1/2)=1/2.

There is no tie-breaking pathology: every minimizing selection has the asserted limit. QED.

**Why this does not settle the nested problem.** The first two rows change with m, and the fourth components of low rows in groups 3, 4, and 6 change with m. One cannot reinterpret this array as prefixes of a fixed x_i sequence. Attempts to concatenate stages leave old weak-direction penalties in the objective and destroy the argument. This obstruction has not been overcome.

## 6. A literal arbitrary-selection version is false, but for an uninteresting reason

### Theorem 6 (selection diagnostic, not a resolution of the intended conjecture)

Use p=1, beta_0=0, x_i=2^{-i}, errors equal to -1/4 or +1/4 independently, and rho(r)=(|r|-1)_+. Define one fixed measurable rule on a finite scalar dataset as follows: among its minimizers, choose the point closest to zero if all nonzero design rows are distinct; otherwise choose the largest minimizer. For other datasets where a largest minimizer does not exist, use the closest-to-zero selection; this fallback is irrelevant here.

Every original estimate is exactly zero, but every duplicated-design estimate is at least 3/2. Both weak and strong implications fail for this rule.

**Proof.** The minimizing interval is the intersection of [2^i(epsilon_i-1),2^i(epsilon_i+1)]. All these intervals contain [-3/2,3/2]. The first row's interval is contained in [-5/2,5/2], while all later rows' intervals contain [-3,3], so the first row determines the original interval. The original designs are distinct, hence the rule chooses zero. In the duplicated design there are two first-row intervals and all later intervals are wider; their intersection still contains [-3/2,3/2] and has a largest point at least 3/2. The fixed rule chooses that point. These choices are measurable (finite maxima, minima, and a deterministic test on the design). QED.

This estimator is intentionally non-equivariant and changes its tie preference when rows repeat. Its consistency is only asserted at beta_0=0. It explains why an unspecified argmin cannot support a universal theorem. It is not evidence against a uniqueness-based or stable-selection version, and it does not invalidate Theorem 1's stated hypotheses.

## 7. A necessary-information lemma for the actual nested problem

### Theorem 7 (regular location errors and equivariant estimation)

Suppose the errors have a density f on R, q=sqrt(f) belongs to the Sobolev space H^1(R), and J=4 integral |q'(x)|^2 dx is finite. Let x_i be one fixed deterministic infinite design. If a translation-equivariant estimator is weakly consistent at one parameter value, then lambda_min(S_n)->infinity. Translation equivariance means T_n(y+X_n h)=T_n(y)+h for every parameter shift h. Unique M-minimizers automatically have this property wherever they exist.

This is a necessity theorem, not a sufficiency theorem for an arbitrary convex rho.

**Proof.** Equivariance makes the estimation-error distribution independent of beta_0, so consistency holds at every parameter value. Suppose lambda_min(S_n) does not diverge. Since S_n increases in the positive-semidefinite order, these smallest eigenvalues are bounded by a constant C. Choose unit eigenvectors along a subsequence converging to a unit vector u. For each fixed m and all later n, u_n'S_m u_n<=u_n'S_n u_n<=C. Passing to the subsequential limit gives u'S_m u<=C for every m. Therefore sum_i (x_i'u)^2<=C.

For any scalar h, the H^1 translation bound gives

||q(.-h)-q||_2 <= |h| ||q'||_2.

Indeed, write the difference as an integral of translates of q' and apply the integral triangle inequality; the standard absolutely continuous representative of an H^1 function justifies this identity. Its Hellinger affinity with its translate is

A(h)=integral q(x)q(x-h)dx
    =1-(1/2)||q(.-h)-q||_2^2
    >=1-J h^2/8.

Choose a nonzero constant a sufficiently small that J a^2 C/8<=1/2. If C=0 no smallness is needed: every x_i'u=0 and the two experiments are identical. Put h_i=a x_i'u. The affinity between the first n observations at beta_0 and at beta_0+a u is the product A_n=product_{i<=n}A(h_i). Since all J h_i^2/8<=1/2 and log(1-z)>=-2z on [0,1/2],

A_n >= exp[-(J/4) sum_{i<=n}h_i^2] >= exp(-J a^2 C/4)>0.

For any two densities with affinity A, Cauchy-Schwarz applied to |sqrt(p)-sqrt(q)|(sqrt(p)+sqrt(q)) gives total variation at most sqrt(1-A^2). Thus these two n-sample experiments have total variation bounded uniformly strictly below one. But consistency at both parameters gives a contradiction: the event that T_n is within |a|/3 of beta_0 has probability tending to one at beta_0 and to zero at beta_0+a u. Its probability difference tends to one, which total variation forbids. QED.

For Gaussian errors of variance sigma^2, J=1/sigma^2. The lemma also covers other finite-location-information densities satisfying the displayed H^1 condition; it does not cover atomic laws or the uniform-density support boundary in Theorems 4A/4B. It closes the *necessary design condition* for equivariant estimators in this regular class. Applying a suitable independently established M-consistency sufficiency theorem would then give weak transfer because duplication replaces S_n by 2S_n. A general sufficiency theorem for every finite convex coercive rho has not been established here, and the truncated 1993 preview is not used to assume one.

## 8. A direct necessary design condition for LAD, including atoms

### Theorem 8 (two-sided errors force L1 design divergence)

Let rho(r)=|r|, let span{x_i:i>=1}=R^p for a single nested deterministic design, and suppose the i.i.d. error law satisfies P(epsilon>0)>0 and P(epsilon<0)>0. If even one measurable LAD minimizing selection is weakly consistent at beta_0, then

ell_n := inf_{||u||=1} sum_{i<=n}|x_i'u| -> infinity.

This necessity does not require a density, score moments, unique minimizers, or equivariance. It is weaker than Gram divergence: x_i=1/i in Theorem 4A satisfies it. No sufficiency is claimed.

**Proof.** Suppose ell_n does not diverge. It is nondecreasing, so ell_n<=C for every n. Choose unit minimizing directions along a subsequence converging to u. For each fixed m, continuity and nestedness give sum_{i<=m}|x_i'u|<=C. Thus L=sum_{i>=1}|x_i'u| is finite. It is positive because u is a unit vector and the design spans R^p. Choose M with A=sum_{i<=M}|x_i'u|>L/2; put B=L-A<A.

There is an r>0 with both P(epsilon>=r)>0 and P(epsilon<=-r)>0. Consider the event E on the first M errors requiring epsilon_i>=r when x_i'u>0, and epsilon_i<=-r when x_i'u<0; impose no condition when x_i'u=0. Independence and finiteness give P(E)>0. Choose delta>0 so that ||x_i|| delta<r/2 for every relevant i<=M.

On E, for every b with ||b-beta_0||<=delta, the first M residuals in the relevant rows have the prescribed nonzero signs. Their directional derivatives along +u therefore sum to -A. Every later absolute-loss term has right directional derivative at most |x_i'u|, including when its residual vanishes. Consequently, for every n>=M and every such b,

D_u^+ F_n(b) <= -A + sum_{M<i<=n}|x_i'u| <= -A+B<0.

A point with a negative right directional derivative cannot minimize a finite convex function. Hence on E no minimizing selection lies within the closed delta-ball, for any n>=M. Its error probability is bounded below by P(E)>0, contradicting weak consistency. QED.

The doubled design has ell_{2n}^{rep}=2 ell_n. Thus this necessary condition is exactly preserved by replication, but necessary conditions alone do not prove consistency of the pooled estimator. The result is independently derived here, without asserting that its assumptions coincide with the inaccessible Bai–Wu (1997) theorem.

## 9. Full weak-preservation theorem for uniformly curved losses

### Theorem 9 (all fixed dimensions; finite-variance errors, including atoms)

Let p be fixed, let (x_i) be one deterministic nested design with S_{n_0}>0 for some n_0, and let rho be a fixed C^2 function satisfying

0 < m <= rho''(r) <= M < infinity for every real r.

Let the original errors be i.i.d. with finite variance sigma^2 (their mean need not be zero). For every n, the replicate errors epsilon'_1,...,epsilon'_n are independent of (epsilon_1,...,epsilon_n) and are i.i.d. with the **same law as epsilon_1**. Then the original and repeated-design M-minimizers exist uniquely for all n>=n_0, and **original weak consistency implies repeated-design weak consistency**, in every dimension p. No density, score-centering E rho'(epsilon)=0, or Fisher-identification assumption is needed. All limits are taken along n>=n_0. This theorem is about weak consistency and therefore does not depend on the strong coupling R/S/I.

For every n>=n_0, define beta_hat_n=argmin F_n, beta_tilde_{2n}=argmin(F_n+F_n'), and theta_n=argmin E F_n; each minimizer is unique. For all n>=n_0,

E||beta_hat_n-theta_n||^2
 <= M^2 sigma^2 p / [m^2 lambda_min(S_n)],  n>=n_0,               (9.1)

E||beta_tilde_{2n}-theta_n||^2
 <= M^2 sigma^2 p / [2 m^2 lambda_min(S_n)],  n>=n_0.             (9.2)

If the error law is nondegenerate, original weak consistency forces lambda_min(S_n)->infinity. Consequently, **for nondegenerate error laws in this class**, original weak consistency is equivalent to the conjunction of Gram divergence and theta_n->beta_0. The latter deterministic minimizer is unchanged by exact design replication. For degenerate errors only the replication implication is asserted, not this characterization.

**Proof of existence and notation.** Put psi=rho'. The curvature bounds imply that psi is M-Lipschitz and has at most linear growth, while rho has at most quadratic growth and a positive quadratic lower bound up to an affine function. Thus the finite sample criterion and its expectation are finite, coercive, and strictly convex whenever S_n>0. They have unique minimizers, their gradients exist, and differentiation of the finite expected sum is justified by finite second moments. This also makes the sample minimizer a measurable, continuous function of the response vector.

**Step 1: consistency forces Gram divergence without a density assumption.** This step only requires a nondegenerate error law, not moments. Suppose Gram divergence fails. Since S_n increases, S_n^{-1} decreases in the positive-semidefinite order for n>=n_0 and converges to a positive-semidefinite matrix B. Failure of lambda_min(S_n)->infinity implies B is nonzero. The first n_0 design vectors span R^p, so there is a fixed i<=n_0 with

x_i'B x_i = c > 0.

Therefore x_i'S_n^{-1}x_i>=c for every n>=n_0. Hold every response except y_i fixed. The unique sample minimizer b(y_i) is continuously differentiable by the implicit function theorem, since its Hessian

H = sum_{j<=n} rho''(y_j-x_j'b) x_j x_j'

satisfies mS_n<=H<=MS_n and is invertible. Differentiating the first-order equation gives

db/dy_i = H^{-1} rho''(y_i-x_i'b) x_i.

Thus, for every n>=n_0, the fitted value g_n(y_i)=x_i'b(y_i) has, for every real y_i and every choice of the other responses,

g_n'(y_i)
 = rho''(y_i-x_i'b) x_i'H^{-1}x_i
 >= (m/M) x_i'S_n^{-1}x_i
 >= alpha := (m/M)c > 0,  for all n>=n_0.                        (9.3)

Nondegeneracy gives real a<b with q_-=P(epsilon_i<=a)>0 and q_+=P(epsilon_i>=b)>0. Conditional on all other responses, the fitted values arising from these two events are separated by at least alpha(b-a), since y_i=x_i'beta_0+epsilon_i and (9.3) holds everywhere. An interval of radius eta=alpha(b-a)/4 cannot intersect both ranges. Hence, uniformly over n>=n_0 and the other responses,

P(|x_i'beta_hat_n-x_i'beta_0|>eta | other responses)
 >= min(q_-,q_+) > 0.

Independence ensures the conditional error law remains the original law. Averaging this inequality contradicts beta_hat_n->beta_0 in probability, because x_i is fixed and nonzero. This proves Gram divergence.

**Step 2: concentration about the deterministic population minimizer.** At theta_n write

Z_n = sum_{i<=n} x_i {psi(Y_i-x_i'theta_n)
                         - E psi(Y_i-x_i'theta_n)}.

The population first-order equation gives grad F_n(theta_n)=-Z_n. Put d=beta_hat_n-theta_n. Strong monotonicity of the sample gradient, with grad F_n(beta_hat_n)=0, yields

m d'S_n d <= d' Z_n
           <= ||S_n^{1/2}d|| ||S_n^{-1/2}Z_n||.

Consequently ||S_n^{1/2}d||<=m^{-1}||S_n^{-1/2}Z_n||, including d=0. For any deterministic shift t and independent copies epsilon,epsilon',

Var(psi(epsilon-t))
 = (1/2) E[psi(epsilon-t)-psi(epsilon'-t)]^2
 <= (M^2/2) E(epsilon-epsilon')^2
 = M^2 sigma^2.

Independence and the trace identity sum_i x_i'S_n^{-1}x_i=p now give

E||S_n^{-1/2}Z_n||^2
 = sum_i Var(psi(Y_i-x_i'theta_n)) x_i'S_n^{-1}x_i
 <= M^2 sigma^2 p.

Using ||d||^2<=lambda_min(S_n)^{-1} d'S_n d proves (9.1). The expected pooled criterion is exactly 2 E F_n, so its population minimizer is the same theta_n. Repeating this argument with design matrix 2S_n proves (9.2).

**Step 3: transfer.** For nondegenerate errors, original consistency and Step 1 give Gram divergence. By (9.1), beta_hat_n-theta_n->0 in probability, so the deterministic sequence theta_n must converge to beta_0. Equation (9.2) then gives pooled weak consistency. Conversely, Gram divergence and theta_n->beta_0 imply original weak consistency by (9.1), proving the stated characterization for nondegenerate error laws. If sigma^2=0, both same-law error streams equal the same constant almost surely; almost surely the pooled criterion equals 2F_n, so beta_tilde_{2n}=beta_hat_n a.s. for all n>=n_0, and the transfer is immediate. QED.

**Nonquadratic example and scope.** The loss rho(r)=r^2/2+log(cosh r) has 1<=rho''(r)<=2 and is not least squares. The theorem permits atomic errors and nonzero error mean. With errors equally likely 0 and 2 and rows cycling e_1,-e_1,e_2,-e_2, theta_n=beta_0 when n=4k or 4k+2, although E psi(epsilon) is nonzero. For n=4k+1 or 4k+3, the one unbalanced coordinate displacement u minimizes h(u)=(k+1)E rho(epsilon-u)+k E rho(epsilon+u). Since h'(0)=-E psi(epsilon) and h''>=2k+1, its displacement satisfies |u|<=|E psi(epsilon)|/(2k+1). The other coordinate is balanced. Thus theta_n->beta_0 along every prefix, and lambda_min(S_n)>=2k for n=4k+r, 0<=r<=3, k>=1. Theorem 9 therefore gives consistency throughout this example, not just at complete cycles. The conclusion is genuinely a theorem for a subclass of the original nested-design weak conjecture, not a triangular substitute. No novelty claim is made.

**Obstruction to extending this proof.** LAD, Huber, and other bounded-score losses do not have a positive global lower curvature bound. Then both the fixed-observation influence lower bound (9.3) and the uniform sample-gradient coercivity used in (9.1) can fail. The bounded-Gram consistent LAD example in Theorem 4A proves that the necessity step cannot hold universally. For losses whose curvature is unbounded above, the shift-uniform score variance bound and Hessian comparison also need new arguments. Finite error variance is used essentially for (9.1), and no infinite-variance extension is claimed.

## 10. Focused scale-separation attack and its precise failure

The following is a diagnosis of the constructed candidate, not an impossibility theorem for all nested counterexamples.

For an L-Lipschitz loss (including LAD and Huber), split each retained design row as (a_i,b_i), with a_i in the rescaled strong coordinates and b_i in the weak coordinate. On ||z||<=R, the old-row contrast at parameters (z/A,v) obeys

|sum_{i<=k} [rho(epsilon_i-a_i'z/A-b_i v)-rho(epsilon_i-b_i v)]|
 <= (L R/A) sum_{i<=k}||a_i||.                                (10.1)

This follows term by term from Lipschitz continuity. Even super-exponential A can therefore eliminate only the old **strong-coordinate** perturbations. The remaining function sum_{i<=k}[rho(epsilon_i-b_i v)-rho(epsilon_i)] is independent of A and need not vanish. A bounded score limits residual sensitivity, not the design coefficient multiplying that score.

For the actual hinge geometry in Theorem 5, the surviving profile is exactly

G(0,0,0,v)=4v_+ + (1/2)(-v)_+.

It is 4 at v=1 and 1/2 at v=-1. Rescaling old strong coordinates by any ratio r->0 leaves these barriers, rather than making them negligible. With fixed positive stage weights, retained stages accumulate them. Increasing the new stage weight without bound is incompatible with the finite high-row pinning mechanism used in Theorem 5.

The every-prefix requirement creates a separate diagnostic. If a new high row rescales only the first active coordinate before its partner is installed, the previously isolated stage can pass from |u_1|=|u_2|=1 to |u_1|=r, |u_2|=1. Lemma 5.1 then gives the exact conditional minimizer v=r-1, tending to -1, not zero. Older retained penalties might prevent this displacement, but those are precisely the penalties the proposed scale-separation counterexample needed to erase. No construction satisfying both requirements was obtained.

Exact rational profiles, this intermediate-prefix geometry, and finite matrix checks for Theorem 9 are reproduced by `work/check_curvature_round.py`. They illustrate and check the displayed algebra; the proofs above, rather than finite checks, establish the statements.

## 11. What has not been proved

The weak nested-design implication is proved in Theorem 9's exact globally bounded positive-curvature, finite-variance regime, including atoms and nonzero mean without score-centering. The written, parent-audited Theorem 10 adds the centered Gaussian even-Lipschitz-loss regime, including LAD/Huber for an equivariant original estimator. Theorem 11 supplies a written genuine nested counterexample to the broad no-moment formulation, with infinite absolute first moment and variance. What remains unresolved is the intended book formulation under unspecified error conditions and regular/finite-moment-score regimes beyond Theorems 9/10, not the already refuted broad formulation. The full asymptotics of Theorems 10/11 are not kernel-checked, the HMZ run is not RLAR-accepted, and the general strong R statement remains unresolved outside separately proved sufficient regimes.

## 12. Regular bounded-score extension and Gaussian LAD/Huber transfer

### Theorem 10 (written, parent-audited; not a complete Lean formalization)

Let p be fixed, rho be finite, convex, coercive and globally Lipschitz, and psi a measurable subgradient. Suppose the iid errors satisfy E psi(epsilon)=0 and

E[rho(epsilon-s)-rho(epsilon)]=(a/2)s^2+o(s^2) as s->0,

for some a>0. For every deterministic full-rank design array with S_n=sum x_ni x_ni', every measurable M-minimizing selection satisfies

||S_n^(1/2)(beta_hat_n-beta_0)||=O_P(1).

Consequently lambda_min(S_n)->infinity suffices for weak consistency, without a leverage-rate condition. The contrast expectation exists because its integrand is bounded by L|s|; no error moment or integrability of rho(epsilon) is required for this sufficiency assertion.

For centered nondegenerate Gaussian errors, every fixed even convex coercive Lipschitz loss satisfies these hypotheses. Thus, on a **single nested eventually full-rank deterministic design**, original weak consistency of a **translation-equivariant original M-estimator** implies pooled weak consistency for **every measurable pooled M-minimizer**, with independent fresh iid **same-law** replicate errors. Almost-sure uniqueness of the original minimizer is sufficient for equivariance; it is not automatic for LAD. With p=1, x_i=1 and even n, continuous errors give a whole LAD minimizer interval. An arbitrary original selector on a nonunique design is not covered by the necessary-information argument.

**Proof and mechanism.** The complete written argument is [regular-bounded-score-derivation.md](hmz-lean-20261014/regular-bounded-score-derivation.md). Normalize rows by S_n^(-1/2), order them by norm, and extract persistent rows z_j with residual covariance A=I-sum z_jz_j'>=0. The empirical convex contrasts converge locally in distribution to the sum of the persistent-row contrasts, an independent Gaussian linear term in the range of A^(1/2), and a positive quadratic form on A. Nonnegative convex remainders have E R(e,s)=O(s^2) and E R(e,s)^2=O(|s|^3), giving the tail approximation without diffuse leverage. A finite persistent-row frame controls the nullspace of A while its quadratic form controls the complement, so the limit is almost surely coercive. Positivity on a large sphere confines all sample minimizers by convexity and yields normalized tightness. For Gaussian errors, Theorem 7 supplies necessary Gram divergence from original consistency/equivariance; exact replication doubles S_n, and the sufficiency assertion applies.

**Status and prior work.** This is a written derivation with [parent mathematical audit and qualifications](hmz-lean-20261014/written-proof-parent-audit.json), not kernel verification of the stochastic compactness proof. It is a genuine extension beyond Theorem 9's positive sample-curvature regime, not a solution for arbitrary error laws. It makes no novelty claim: related literature includes Zhao--Rao--Chen (1993), Chen--Zhao--Wu (1993), and Knight (1998), Annals of Statistics 26:755--770, [DOI 10.1214/aos/1028144858](https://doi.org/10.1214/aos/1028144858). Access and theorem-scope limits are recorded in [source-access-audit.json](hmz-lean-20261014/source-access-audit.json).

## 13. Full-scope written counterexample to the broad no-moment formulation

### Theorem 11 (written proof, parent-audited, independent Opus referee correct; minor fixes applied)

There exist p=2, one fixed nested eventually spanning deterministic design, one fixed finite C^2 convex coercive loss satisfying 3/4<=rho''<=5/4 globally, and one fixed identifiable iid error law such that the original and exactly replicated criteria have unique minimizers for every n>=2, the original minimizer is weakly consistent along every prefix, but independent fresh **same-law** replication is weakly inconsistent.

The explicit loss is

rho(r)=r^2/2+(1/(4 pi^2))(1-cos(pi r)).

The fixed symmetric lacunary law has F{+T_j}=F{-T_j}=1/(2N_j), with N_j=2^(4*10^j), T_j=2N_j^2, and its remaining mass at zero. It has E|epsilon|=infinity and E epsilon^2=infinity. The design begins with e_1,e_2; every stage appends a weak-coordinate buffer, a pure strong-coordinate block, then complete five-row cycles, without ever changing an old row. [counterexample.md](hmz-lean-20261014/counterexample.md) gives the exact row coefficients/counts and all-prefix probability bounds.

For even-integer errors, the exact finite-sample contrast is rho(e-t)-rho(e)=rho(t)-e*t. The original strong normalized coordinate approaches an integer rare-error count, where each cycle's weak periodic score cancels. Pooling two independent counts can approach a half-integer; the weak score then remains nonzero. The buffer controls every intermediate prefix. At completed stages, the construction gives

liminf_j P(||beta_tilde_{2n_j}||>eta/(20M)) >= exp(-2)/2 > 0,

where eta=1/(4pi) and M=5/4, while beta_hat_n->0 in probability along every n.

The parent found no error after checking the exact criterion, scale exponents, all prefix cases and pooled event/root bound; [audit](hmz-lean-20261014/counterexample-parent-audit.json). A separate parent-owned **Claude Opus 5.5/max, no-tools** referee returned **correct**, checking 44 written claims and establishing every-prefix consistency, pooled inconsistency and all target hypotheses. It reviewed hash `f8e22b6f4c4fe7eb1d19291e2998abdce9ce2e99ed507f9fa239c25ae7c8acfd`, preserved in the scratch original and [reviewed snapshot](hmz-lean-20261014/evidence/counterexample-reviewed.md). Its five presentation findings were applied only to the integrated proof, now hash `bb9f4ec1750cb8aad9da272769f4999bdc14216a98d2eb36a5db704f2c717d15`; [resolution](hmz-lean-20261014/independent-referee-resolution.json). The construction is unchanged. The referee did not inspect or use Lean artifacts.

**Scope and verification.** This refutes formulation (c), which explicitly imposes no moment condition. It shows Theorem 9's finite-variance hypothesis cannot simply be dropped for uniformly curved losses; it does not say finite variance is necessary, nor settle the intermediate finite-mean/infinite-variance regime. Because Cui leaves the error conditions unspecified, it does not establish that the intended book question with standard centered/finite-moment scores is resolved. Thirty Lean declarations check real loss/profile calculus, the exact even-error contrast, integer/half-integer scores, weighted second moments and related components. The infinite law/design and asymptotic conclusions above remain written proofs. The real 3600-second HMZ loop ended `stopped` without a reviewer verdict, so **no RLAR acceptance or full asymptotic Lean proof is claimed**.

