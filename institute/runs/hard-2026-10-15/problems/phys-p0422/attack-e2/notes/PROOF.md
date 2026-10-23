# Energetic comparison for random k-SAT, with explicit finite trials

This is a self-contained re-derivation and general-k extension of the
integer-cost, y-reweighted energetic interpolation in Fedor Vorobyev (2026),
*An upper bound of 4.268 for the random 3-SAT satisfiability threshold*,
arXiv:2610.10599v1, Sections 2–5 (staged reader text). The degree-k polynomial
remainder is credited to Marc Lelarge and Mendes Oulamara (2018), *Replica
bounds by combinatorial interpolation for diluted spin systems*, condition
(4), equation (30), following that staged preprint's attribution. Their primary
text is not staged. These are method attributions, not independent-discovery
claims. All identities and inequalities needed here are proved below; no
statement about the preprint's Lean code or hypotheses of an unavailable
literature theorem is invoked. No convergence of population dynamics or
existence of a threshold is assumed. This written proof has been audited
line by line in the continuation; it is not formally verified or externally
refereed. Arithmetic replay does not verify the analytic argument.

## 1. Models, trial law, and the criterion

Fix integers k >= 2 and n >= 1, density alpha > 0, an integer T >= 1,
and a probability law rho of finite support in [0,1). All copies of a random
variable R with law rho below are independent unless explicitly shared.

In the auxiliary repeated-variable model each ordered clause has k independent
uniform indices in [n] and k independent fair forbidden values J in {0,1}.
Its cost at sigma is the product of its k literal violation indicators
1{sigma_i=J}. Costs remain 0 or 1 even when indices repeat. The energy E(F)
is the minimum total cost over all 2^n assignments.

Let Q be a product of k-1 copies of R and put lambda=k alpha/2. Define

    nu_i = E (1-Q)^i,
    M_i = exp(lambda (nu_i-1)),                         i=0,...,T,
    mu_j = sum_{i=0}^j (-1)^i binom(j,i) M_i,          j=1,...,T,
    d_infinity = E log(1-R_1...R_k),
    Psi_T = -sum_{j=1}^T mu_j^2/j - (k-1)alpha d_infinity.

The expectations defining nu_i and d_infinity are finite sums over rho.
The strict bound max(support rho)<1 ensures that d_infinity is finite.
We prove the following finite-n inequality for every y>0 and every n>=1
(n>=k is needed only when constructing the distinct-variable model):

    -(y/n) E E(F_rep_Poisson(alpha n)) <= Psi_T + T exp(-y).       (A)

Consequently Psi_T <= -epsilon and T exp(-y) <= epsilon/2 imply

    E E(F_rep_Poisson(alpha n)) >= c0 n,
    c0 = epsilon/(2y) > 0,                            every n>=1. (B)

The sign of every inequality and the fact that costs are integers matter.

## 2. Exact insertion identity

For any integer-valued H on the finite assignment space and any indicator
V taking values in {0,1}, let M(H) be its nonempty set of minimizers.
Then

    min(H+V) = min H + 1{V(sigma)=1 for all sigma in M(H)}.       (C)

If some minimizer has V=0, the minimum stays unchanged. Otherwise all old
minimizers have new cost min H+1, and all nonminimizers already have cost
at least min H+1. This proves (C). The identity need not hold for noninteger H.

For a seed x=(i,J,R), define

    b(x,a) = 1{sigma_i=J for every minimizer of H_a}.

Here H_a includes existing clauses and existing one-variable sites with
auxiliary activation outcomes a. Since a clause's indicator is the conjunction
of its literal indicators, the indicator on the right of (C) for a new clause
is exactly product_{ell=1}^k b(x_ell,a): the two universal quantifiers commute.
Repeated variable positions, including inconsistent signs, cause no exception.

## 3. Clause and site increments

A row comprises k independent seeds x_ell=(i_ell,J_ell,R_ell). Indices are
uniform, J_ell are fair, and R_ell have law rho, independently.
Its clause has cost product_{ell=1}^k 1{sigma_{i_ell}=J_ell}.
Its site has cost V 1{sigma_{i_1}=J_1}, where V is an independent Bernoulli
variable of conditional mean Q=R_2...R_k. Equivalently it is the product
of k-1 independent Bernoulli warnings with their specified rates. Rows,
including any auxiliary activation variables, are independent.

For K clauses and L sites, condition on their rows and average only over the
independent site activations a. Set

    Z_y = E_a exp(-y min H_a),
    Phi_y = log Z_y,
    f(K,L) = E_rows Phi_y,
    q = 1-exp(-y) in (0,1),
    d_y = E log(1-q R_1...R_k).

All conditional averages over a are finite. We have
-y(K+L)<=Phi_y<=0, and adding one clause or site changes Phi_y by a number
in [-y,0], by (C) or simply because the minimum changes by 0 or 1.

For the fixed old rows put

    mu_y(a) = P(a) exp(-y min H_a)/Z_y,

and write angle brackets for expectation under mu_y. Applying (C) and
averaging a new site's activation gives the exact increments

    Delta_C Phi_y = log(1-q <product_{ell=1}^k b(x_ell,a)>),
    Delta_S Phi_y = log(1-q R_2...R_k <b(x_1,a)>).                (D)

For each positive integer h, take independent replicas a_1,...,a_h under
mu_y and set

    B_h = E_x product_{t=1}^h b(x,a_t),
    C_h = E R^h.

Here <.>_h denotes expectation over these h independent replicas; all old
rows stay fixed. Both B_h and C_h lie in [0,1]. The same new seed is shared
across the h replicas; different literal positions use independent seeds.
To state the expectation order precisely, let

    W_C = <product_{ell=1}^k b(x_ell,a)>,
    W_S = R_2...R_k <b(x_1,a)>,
    W_D = R_1...R_k.

These are the three arguments z in log(1-qz), before the factor q. Then

    E_new[W_C^h] = <B_h^k>_h,
    E_new[W_S^h] = <B_h>_h C_h^(k-1),
    E_new[W_D^h] = C_h^k.                                     (E)

For the first identity, expand the h-th power as an expectation over the
h old-activation replicas, interchange finite expectations, and average the
k independent new seeds. Each seed contributes B_h. For the second, the
site's k-1 rate variables are independent of its first seed and the old
activations; they contribute C_h^(k-1). The third is independence of k rates.

The degree-k remainder of Lelarge–Oulamara has the following elementary
factorization, which supplies its sign here. For all B,C>=0,

    B^k-k B C^(k-1)+(k-1)C^k
      = (B-C)^2 sum_{ell=0}^{k-2} (ell+1) B^(k-2-ell) C^ell
      >= 0.                                                   (F)

Thus the argument covers odd k=5. In the cases at issue the final factors
are B^2+2BC+3C^2 (k=4) and B^3+2B^2C+3BC^2+4C^3 (k=5).
No assertion about a signed overlap is being made.

Use log(1-qz)=-sum_{h>=1} q^h z^h/h, uniformly absolutely convergent on
0<=z<=1, with total absolute bound sum q^h/h=y. Equations (D)-(F) give

    E_new Delta_C Phi_y - k E_new Delta_S Phi_y + (k-1)d_y <= 0.

Termwise averaging is justified by that uniform bound, including averages
over the finite old rows. Averaging old rows therefore yields

    f(K+1,L)+(k-1)f(K,L)
       <= k f(K,L+1) - (k-1)d_y.                              (G)

This is the load-bearing comparison, derived for every k>=2.

## 4. Finite replacement and Poissonization

For any f with bounded increments satisfying (G), define

    S_N(K,L) = sum_{j=0}^N binom(N,j)(k-1)^(N-j) f(K+j,L).

Induction on N proves

    S_N(K,L) <= k^N [f(K,L+N) - (k-1)N d_y/k].                (H)

The N=0 case is equality. Pascal's identity gives
S_{N+1}(K,L)=S_N(K+1,L)+(k-1)S_N(K,L).
Apply the induction hypothesis to these two terms, then (G) at (K,L+N).
The constant contribution becomes
-k^N (k-1)(N+1)d_y, exactly as required in (H) for N+1.

Set K=L=0, divide by k^N, and average N~Poisson(k alpha n). The left
side is the average of f(J,0) with J|N~Binomial(N,1/k). Direct expansion
of the Poisson probabilities shows J~Poisson(alpha n). Since increments
are bounded and f(0,0)=0, |f(K,L)|<=y(K+L); all rearrangements and
expectations are absolutely convergent. Using E N=k alpha n gives

    -y E E(F_rep_Poisson(alpha n))
       <= E_{L~Poisson(k alpha n)} f(0,L) - (k-1)alpha n d_y.   (I)

## 5. Exact site moments and a signed finite-y estimate

Hold the site rows fixed. For each v, let N_{v,s} count its active sites
penalizing value s in {0,1}, and define

    A_v = product_{sites at (v,0)} (1-Q),
    B_v = product_{sites at (v,1)} (1-Q),
    G_v = A_v+B_v-A_v B_v.

The empty product is 1. The two disjoint groups use independent activation
variables, so G_v is the conditional probability that at least one value is
unpenalized. A variable with both values penalized must incur at least one
violation. Independence across variables of the site activations gives

    Phi_y <= sum_v log(G_v+(1-G_v)exp(-y)).                    (J)

Indeed the actual site-only minimum is sum_v min(N_{v,0},N_{v,1}); using
only the conflicting-variable indicator is a lower bound on that minimum,
which becomes the upper bound (J) on its negative exponential moment.

Under L~Poisson(k alpha n), the marked counts at the 2n possible pairs
(v,s) are independent Poisson variables of mean lambda=k alpha/2, with
iid Q marks. This can be checked from their joint probability generating
function, or directly by multinomial expansion of the Poisson series.
Hence A_v and B_v are independent and identically distributed, with

    E A_v^i = exp(lambda(E(1-Q)^i-1)) = M_i.

Consequently mu_j=E(1-A_v)^j is nonnegative, and

    E[(1-A_v)^j (1-B_v)^j] = mu_j^2.                          (K)

For x in [0,1] and delta in (0,1], truncating the logarithmic series and
using 1-(1-delta)^j<=j delta gives

    log(1-(1-delta)x)
      <= -sum_{j=1}^T (1-delta)^j x^j/j
      <= -sum_{j=1}^T x^j/j + T delta.                       (L)

Apply this to x=(1-A_v)(1-B_v), delta=exp(-y), and average (J). By (K),

    (1/n) E f(0,L) <= -sum_{j=1}^T mu_j^2/j + T exp(-y).     (M)

Only finite bounded polynomials have been averaged. There is no unproved
interchange of an infinite alternating sum, and no limiting-y interchange.
Since q<=1, d_y>=d_infinity. Substituting (M) into (I), and respecting the
minus sign in -(k-1)alpha d_y, proves (A). This completes the comparison.

For relation to a finite-temperature partition moment, if desired, the
same activation distribution satisfies

    exp(-beta E_a) <= sum_sigma exp(-beta H_a(sigma))
                    <= 2^n exp(-beta E_a).

Raising to m=y/beta>0 and averaging gives, after taking logarithms,

    Phi_y <= log E_a[(sum_sigma exp(-beta H_a(sigma)))^m]
          <= Phi_y + (y/beta)n log 2.

This is controlled uniformly in n after division by n. The proof above
uses finite y directly and requires no finite-temperature theorem.

## 6. Poisson to fixed counts; repeated to distinct variables

Suppose (B) holds, set M=floor(alpha n), and couple the Poisson-count and
fixed-count auxiliary formulas using one infinite independent clause sequence
and N~Poisson(alpha n). Since adding one clause changes the minimum by at
most 1,

    E E(F_rep_M) >= c0 n - E|N-M|
                 >= c0 n - sqrt(alpha n) - 1.                (N)

Here E|N-alpha n|<=sqrt(Var N)=sqrt(alpha n) by Cauchy-Schwarz and
|alpha n-M|<1.

For each of the M ordered repeated-variable clauses, keep it if its k indices
are distinct; otherwise independently resample the variable tuple uniformly
from all ordered distinct k-tuples, retaining its independent fair signs.
The output clauses are independent, each with uniformly distinct variable
indices and independent fair signs. Forgetting the ordering gives exactly
the model in the frozen contract. By a union bound a clause is replaced
with probability at most binom(k,2)/n. The difference between minima is
at most the number of replaced clauses, deterministically. Therefore

    E E(F_dist_M) >= c0 n - sqrt(alpha n) - 1 - alpha binom(k,2). (O)

In particular with c=c0/2 this is at least c n whenever

    n >= N0 = ceil(max(k, 16 alpha/c0^2,
                            4(1+alpha binom(k,2))/c0)).        (P)

Both losses have thus been stated explicitly and are sublinear in n.

## 7. Concentration and the required high-probability conclusion

E(F_dist_M) is a function of M independent clauses; replacing one changes
it by at most 1. The Doob martingale for exposing the clauses has each
conditional difference lying in an interval of length at most 1. The
elementary Hoeffding exponential bound (obtained by convexity of exp on
an interval and minimizing the resulting bound) gives

    P(E(F_dist_M)-E E(F_dist_M) <= -t) <= exp(-2t^2/M).

For n>=N0 in (P), put t=E E(F_dist_M)>=c n. As M<=alpha n,

    P(F_dist_M is satisfiable) <= exp(-2c^2 n/alpha) -> 0.      (Q)

For larger densities couple by adding clauses; satisfiability is decreasing.
This proves the upper-bound statement without presupposing a limiting
threshold constant.

## 8. Explicit rational data and certified inequalities

Use the following laws (all decimal-looking fractions are exact):

| k | alpha | R support numerators over 10000 | probability numerators over 10000 |
|---|---|---|---|
|4|249/25|1745, 7707, 4454|2946, 3363, 3691|
|5|1057/50|5391, 3691, 7344|1009, 6190, 2801|

For both use T=128 and y=20. The exact arithmetic producer and an
algorithmically distinct implementation of the same formula certify
Psi_128<=-epsilon, respectively epsilon=1/1000 and 1/2500,
and 128 exp(-20)<=epsilon/2. In particular the bounds (B) and (Q) give

| k | c0 | c | asymptotic fixed-model SAT probability bound, n>=N0 |
|---|---|---|---|
|4|1/40000|1/80000|exp(-2 n/((80000)^2 (249/25)))|
|5|1/100000|1/200000|exp(-2 n/((200000)^2 (1057/50)))|

Rational comparison gives 249/25<1023/100 and 1057/50<2133/100.
No claim of optimality, exact thresholds, current novelty, or resolution of
the broader Challenge 5 is implied.

## 9. Numerical-enclosure proof obligations

`code/certify.py` forms the finite product laws by ordered enumeration and
calculates nu_i exactly as Fractions. For x<=0 and u=x/2^s,

    max(0,1+u) <= exp(u) <= 1/(1-u).

The first inequality is the exponential tangent bound; the second follows
by applying that bound to -u and taking reciprocals of positive quantities.
The producer squares s=220 times, rounding each lower endpoint down and
upper endpoint up on the grid 2^-384. All endpoints remain nonnegative;
squaring therefore preserves enclosure. Moment coefficients of either sign
use the corresponding endpoints in their alternating binomial sums. Since
mu_j>=0, max(0,lower_mu_j)^2<=mu_j^2. Upper endpoints give the opposite
inequality, after intersecting with the known interval [0,1].

For 0<=z<1 and N=160, with S_N=sum_{h=1}^N z^h/h,

    S_N <= -log(1-z) <= S_N + z^(N+1)/((N+1)(1-z)).

This follows termwise from 1/h<=1/(N+1) for h>=N+1. Thus the positive
correction -(k-1)alpha d_infinity uses an upper bound with the right sign.
Combining these bounds gives an exact rational upper bound on Psi_T.
No omitted Poisson tail remains: the marked-Poisson moment is its exact
generating function, not a truncated degree sum. The only site-log series
truncation is already signed in (L).

`code/independent_check.py` is an algorithmically distinct implementation of
the same Psi_T formula, written by the same producer in the prior attempt.
It checks arithmetic, not the formula or analytic bridge. It reads the trial
data alone. It forms product laws
from multinomial compositions. To enclose exp(-a), a>=0, it sets t=a/128<1,
uses the positive Taylor polynomial of exp(t) through degree 160, and bounds
the remaining tail by its next term divided by 1-t/162. It rounds every
operation outward on the grid 10^-150, reciprocates the positive interval,
and squares seven times, using a different exponential algorithm from the
producer's. For logarithms it uses u=z/(2-z) and

    -log(1-z)=2 sum_{j>=0} u^(2j+1)/(2j+1),

bounding the tail after 160 terms by
2 u^321/(321(1-u^2)). Its moment bounds and final sign checks are again
exact integer and Fraction operations. Neither code imports the other.
All decimal intervals printed in the evidence are outward rounded.
