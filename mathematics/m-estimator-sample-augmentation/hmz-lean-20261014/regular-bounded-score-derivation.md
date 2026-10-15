# Regular bounded-score extension: a subsequence compactness proof

Date: 2026-10-14 PT. This is an independent written derivation during the frozen HMZ run, subsequently audited by the parent agent with scope qualifications recorded in `written-proof-parent-audit.json`. It is not a Lean formalization and was not supplied as a new assumption to that frozen run. It makes no priority claim: it recovers a regular weak-consistency sufficiency regime of the type announced by Zhao--Rao--Chen (1993), whose complete theorem remains inaccessible. The precise argument below, rather than the abstract, is the justification under review. Keep this written/parent-audited proof separate from the compiled component and from the still unresolved unrestricted target.

## Statement

Let p be fixed. Let rho be a fixed finite convex coercive L-Lipschitz function on R. Fix a measurable subgradient selection psi, so |psi|<=L. Let epsilon_i be iid and assume

1. E psi(epsilon)=0;
2. for some a>0, as s->0,
   g(s):=E[rho(epsilon-s)-rho(epsilon)]=(a/2)s^2+o(s^2).

The expectation of the contrast is well-defined even when E|epsilon| is infinite because the contrast is bounded by L|s|. We do not require E rho(epsilon) to be finite. For any deterministic triangular design of full column rank, put S_n=sum x_ni x_ni'. Every measurable minimizer satisfies

||S_n^(1/2)(beta_hat_n-beta0)||=O_P(1).                         (A)

The assertion is uniform over all deterministic full-rank design arrays in fixed p (with the constants allowed to depend on rho and the error law). In particular, lambda_min(S_n)->infinity implies weak consistency. No diffuse-leverage assumption or eigenvalue growth rate is required. The limiting normalized law need not be Gaussian when some normalized rows persist.

For centered nondegenerate Gaussian errors and every even convex coercive Lipschitz loss, the two conditions hold. This includes LAD and Huber with a fixed positive cutoff. Combining this sufficiency statement with the existing proof.md Theorem 7 gives the **weak replication implication for centered nondegenerate Gaussian errors and every such loss**, for a nested eventually full-rank design and unique original minimizers. Pooled uniqueness is not needed for the positive conclusion: it controls every pooled minimizer. The zero-variance Gaussian case instead follows directly from equality of the two sample criteria up to a factor of two when original/pooled minimizers are unique.

The transfer conclusion explicitly inherits Theorem 7's **translation-equivariant original estimator** hypothesis; almost-sure uniqueness of the original minimizer is one sufficient way to obtain it. This is not automatic for every LAD design: for p=1, x_i=1 and even n, continuous errors give an interval of LAD minimizers almost surely. An arbitrary measurable consistent selector on a nonunique design is not covered by the necessity step. In contrast, once Gram divergence is assumed or established, the sufficiency conclusion controls every measurable selection.

This is not the unrestricted book target: it does not cover arbitrary error laws with atoms, misspecified score centering, non-Lipschitz losses, or the cases where g has no positive quadratic expansion. It imposes no score-centering requirement on the earlier Theorem 9.

Closely related prior work includes Keith Knight, *Limiting distributions for L1 regression estimators under general conditions*, Annals of Statistics **26** (1998), 755--770, [DOI 10.1214/aos/1028144858](https://doi.org/10.1214/aos/1028144858), and Chen--Zhao--Wu, *On conditions of consistency of ML1N estimates*, Statistica Sinica **3** (1993), 9--18. Knight's primary Crossref record confirms the citation and describes more general behavior of the error distribution near zero; the publisher HTML/PDF routes returned an access challenge in this session. The complete theorem was therefore not used as a substitute for the normalized-row argument above. The latter journal's primary host failed DNS/HTTP access as recorded in `source-access-audit.json`. These references prevent a novelty claim; they do not provide unseen theorem hypotheses.

## 1. Normalize and compactify the design

Translate beta0 to zero and set z_ni=S_n^(-1/2)x_ni. Then

sum_i z_ni z_ni'=I_p,   sum_i ||z_ni||^2=p.

The transformed empirical contrast is

Q_n(t)=sum_i [rho(epsilon_i-z_ni't)-rho(epsilon_i)].

Its minimizers are t=S_n^(1/2)beta_hat_n. Permute the deterministic rows by decreasing norm and pad them by zeros. This changes neither the distribution of Q_n nor any weak-consistency claim, because the errors are iid within each row of the triangular experiment. It does not replace the original nested-design target by a triangular counterexample.

The ordered rows obey ||z_n,j||<=sqrt(p/j). From every subsequence we can extract a further subsequence such that z_n,j->z_j for each fixed j. Fatou gives sum_j z_j z_j'<=I in the positive-semidefinite order. Write

A=I-sum_{j>=1} z_j z_j' >=0,
A_K=I-sum_{j<=K} z_j z_j'.

Then A_K->A in matrix norm and A+sum_{j<=K}z_jz_j'->I.

## 2. Separate the linear score and nonnegative remainder

Define

R(e,s)=rho(e-s)-rho(e)+psi(e)s.

Convexity gives R(e,s)>=0. Lipschitz continuity gives R(e,s)<=2L|s|. Its expectation is g(s), since the score is centered. For each sufficiently small h>0,

E sup_{|s|<=h} R(e,s)
 <= E[R(e,h)+R(e,-h)] <= C h^2.                               (B)

The first inequality uses convexity of s->R(e,s), R(e,0)=0, and nonnegativity; its maximum on [-h,h] is bounded by the sum of its endpoint values. Also

E R(e,s)^2 <= 2L|s| g(s) <= C' |s|^3                          (C)

for sufficiently small |s|. Thus no moment of epsilon was silently introduced.

Let tau>=0 satisfy tau^2=E psi(epsilon)^2. For iid errors e_j, the vector series

U=sum_j z_j psi(e_j)

converges in L2 and almost surely, by independence, centering, bounded score, and sum_j||z_j||^2<infinity (apply the square-integrable martingale convergence theorem coordinatewise). On every compact t-ball, (B) and Tonelli show that

sum_j R(e_j,z_j't)

converges uniformly almost surely: after finitely many rows, sup_{||t||<=r}R(e_j,z_j't) has summable expectations bounded by C r^2||z_j||^2. The finitely many remaining terms are continuous.

Take a standard p-dimensional Gaussian G independent of the e_j and put Z=tau A^(1/2)G. Define the finite continuous convex random function

Q(t)=sum_j [rho(e_j-z_j't)-rho(e_j)] - Z't + (a/2)t'At,

where the infinite sum means -U't+sum_j R(e_j,z_j't). It has Q(0)=0.

## 3. The normalized empirical contrasts converge locally in distribution

Here are the details behind the triangular-array limit, rather than an unqualified appeal to an asymptotic normality theorem.

Fix finitely many t values in a bounded ball and truncate at K. The first K terms of Q_n converge in distribution to the first K stable-row terms, because z_n,j->z_j and rho is continuous; they can also be coupled using the same first K errors. They are independent of the remaining score vector.

For the tail score vector U_n,K=sum_{j>K} z_n,j psi(e_j), any scalar projection v'U_n,K has total variance tau^2 v'A_n,K v, where A_n,K=I-sum_{j<=K}z_n,jz_n,j'. The largest summand is bounded by L||v||sqrt(p/(K+1)). Expanding the characteristic function of each centered bounded summand at zero and multiplying gives an error tending to zero as K->infinity, uniformly in n, in the approximation by the centered Gaussian vector of covariance tau^2 A_n,K. One explicit bound for each fixed Fourier vector v is a constant depending on L,p,v times max_{j>K}||z_n,j||: the sum of third absolute moments is at most L^3||v||^3 p max_{j>K}||z_n,j||, and the fourth-order product/log error has the same vanishing bound. This is a small-summand central-limit approximation, not the false assertion that all rows are infinitesimal.

For each fixed t, (C) and independence bound the variance of the centered tail remainder by

C'||t||^3 sum_{j>K}||z_n,j||^3
 <= C'p||t||^3 sqrt(p/(K+1)) ->0.

The expansion defining a gives, uniformly in n and ||t|| bounded,

sum_{j>K} E R(e_j,z_n,j't)
  =(a/2)t'A_n,K t + o_K(1),

because sum_j(z_n,j't)^2<=||t||^2 and max_{j>K}|z_n,j't|->0 uniformly. Consequently the finite-dimensional distributions of Q_n have the limit obtained from K stable rows plus an independent Gaussian score of covariance tau^2 A_K and the quadratic (a/2)t'A_Kt, with an error vanishing as K->infinity. As K->infinity these approximants converge to Q, by the series construction and A_K->A.

For completeness, finite-dimensional convergence on a countable dense set upgrades to weak convergence for the topology of uniform convergence on compact subsets. The needed deterministic fact is: finite convex functions converging pointwise on a dense set to a finite continuous convex function converge uniformly on compact subsets of the open domain. One proves it by enclosing each compact set in finitely many small simplices with vertices in the dense set; convexity gives upper bounds, and a second outer simplex bound gives lower bounds. To apply it here, the dense coordinate evaluations are tight in the countable product R^N; any subsequential weak limit has the just established joint law of Q. The product is Polish, so a Skorokhod representation gives almost-sure convergence of all dense coordinates on a further subsequence. The deterministic fact then gives local uniform convergence. This also identifies every subsequential limit, establishing Q_n=>Q locally uniformly.

This distributional convex-function argument does **not** assume that minimizer convergence implies objective convergence. It proves objective convergence first from the score and remainder calculations.

## 4. The limit is coercive, including singular diffuse covariance

This is the essential part that ordinary diffuse-leverage LAD asymptotics do not cover.

Because rho is convex and coercive on both ends, there are deterministic b>0 and c<infinity with rho(s)>=b|s|-c. For every fixed e,

rho(e-s)-rho(e) >= b|s|-[b|e|+c+rho(e)].

Let C_K=sum_{j<=K}(b|e_j|+c+rho(e_j)); it is finite almost surely, without an integrability claim. With U_K=sum_{j<=K}z_j psi(e_j), nonnegativity of the tail remainders gives

Q(t)>=b sum_{j<=K}|z_j't|-C_K-||(U-U_K)|| ||t||
       -tau ||G|| ||A^(1/2)t||+(a/2)||A^(1/2)t||^2.             (D)

Almost surely choose K large enough that ||U-U_K||<=b/8 and

A+sum_{j<=K} z_j z_j' >= (3/4)I.

Put r=||t|| and q=||A^(1/2)t||. If q<=r/2, then

sum_{j<=K}|z_j't| >= sqrt(sum_{j<=K}(z_j't)^2) >= r/sqrt(2).

Completing the square in q bounds the last two terms of (D) below by -tau^2||G||^2/(2a). Hence Q(t)>=(b/sqrt(2)-b/8)r minus a finite random constant.

If q>r/2, discard the nonnegative finite absolute-value term and use

(a/2)q^2-tau||G||q >= (a/4)q^2-tau^2||G||^2/a.

Then Q(t)>=(a/16)r^2-(b/8)r minus a finite random constant. Both cases tend to infinity as r->infinity. Thus Q is coercive almost surely. Persistent rows supply linear coercivity in directions where A is singular; the diffuse quadratic supplies coercivity in the complementary directions. The Gaussian score Z lives in the range of A^(1/2), which is crucial: an arbitrary extra linear term in its nullspace could invalidate the argument.

## 5. Tightness of every minimizer and weak consistency

For each realized coercive Q with Q(0)=0, inf_{||t||=r}Q(t)>0 for all sufficiently large r. Therefore P(inf_{||t||=r}Q(t)>0)->1 as r->infinity. At fixed r, local uniform weak convergence and the open-set Portmanteau inequality give

liminf_n P(inf_{||t||=r}Q_n(t)>0)
 >= P(inf_{||t||=r}Q(t)>0).

If a minimizer of Q_n lay on or outside that sphere, convexity along the segment from 0 to the minimizer would produce a point on the sphere with Q_n<=Q_n(0)=0. Thus the sphere-positivity event confines **all** minimizers to the r-ball. Every design subsequence has the extracted further subsequence above, so failure of uniform tightness would contradict this argument on a bad subsequence. This proves (A).

Finally ||beta_hat_n-beta0||<=lambda_min(S_n)^(-1/2)||S_n^(1/2)(beta_hat_n-beta0)||. If the eigenvalue diverges, tightness gives convergence in probability. Exact replication replaces S_n by 2S_n and does not alter the score or contrast hypotheses, so the sufficiency conclusion applies to all pooled minimizers as well.

## 6. Gaussian LAD and Huber really meet the loss assumptions

For LAD, rho(r)=|r| and psi(r)=sign(r), with any choice at zero. Centered Gaussian errors have no atom at zero, E psi=0, and

g'(s)=2F(s)-1,   g''(0)=2f(0)>0.

Thus a=2f(0), L=1. No unspecified behavior of the objective under extreme leverage is hidden in these formulas; that is handled in Sections 1-5.

For the Huber loss with fixed kappa>0,

rho(r)=r^2/2 if |r|<=kappa,
       kappa|r|-kappa^2/2 otherwise,

psi(r)=clip(r,-kappa,kappa), E psi=0 by symmetry, and a=P(|epsilon|<kappa)>0. Dominated convergence justifies differentiating the expected score, because the score is Lipschitz and the Gaussian has no atom at the two cutoff points. Here L=kappa.

More generally an even convex coercive Lipschitz loss has an odd subgradient off its at most countably many nondifferentiability points, which Gaussian errors hit with probability zero. Its distributional second derivative is a finite nonzero positive measure nu (total mass <=2L). Gaussian convolution gives a=integral f(s) nu(ds)>0, finite and continuous locally. Consequently g(s)=(a/2)s^2+o(s^2). This establishes the stated even-loss Gaussian regime.

For a nested design with unique original minimizers, equivariance and the Gaussian location-information argument in existing Theorem 7 force Gram divergence from original weak consistency. Sections 1-5 then give pooled consistency. Nothing here supplies the analogous necessity step for arbitrary atomic errors or for losses/error laws without the local contrast expansion.

## Formalization boundary and rejection ideas

The full compactness/CLT/argmin argument above has not been kernel checked. A useful nontrivial formal component is the two-case coercivity bound (D), including the range-constrained Gaussian linear term and the strict positivity of a and b. Removing a while retaining a free diffuse-score direction, or allowing a free linear score in null(A), must fail. Another component is the scalar nonnegative-remainder bound R^2<=2L|s|R and its finite-sum variance consequence. These are genuinely connected to the LAD/Huber extension, unlike a bare replication identity.
