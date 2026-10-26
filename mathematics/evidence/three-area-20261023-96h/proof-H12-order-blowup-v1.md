# H_{1,2}: finite-order obstruction near the positive-time zero boundary

Status: **CANDIDATE / NOVELTY_UNCLEAR**. Written reasoning only. This continues the frozen all-beta H_{1,2} minimal-order target; no second target or scientific execution is involved. It uses the exact density/threshold analysis in `proof-H12-PH-existence-threshold-v1.md` (SHA256 `a35c865eaf977b065635e31ee13b4e101306d69f8b7562470b6bafc3a82a1a32`), whose correctness is still under parent/peer review. No root approximation, parameter loop or finite matrix evaluation was executed.

## 1. Result and relation to the unresolved minimum-order band

Fix c,d>0, put a=c+d and vary b=beta d. Let f_beta be the exact inverse transform of

    H_beta(s)=c(a^2+b^2)^2/[(s+c)((s+a)^2+b^2)^2].

Let beta_* be the threshold defined in the preceding manuscript, and t_*=xi/(beta_* d). That manuscript proves directly that f_{beta_*} has exactly one positive-time zero t_*, is strictly positive at all other positive times, and is nonnegative. Its first derivative vanishes at t_* and its second derivative is strictly positive there.

**Candidate theorem O.** For every positive integer r, there exists epsilon_r>0 such that whenever

    beta_*-epsilon_r < beta < beta_*,

H_beta has no PH representation with r or fewer transient states. At the exact O'Cinneide-characterization import boundary, every such beta is nonetheless PH. Consequently its minimum PH order tends to infinity as beta increases to beta_*, even though the reduced transform always has degree5 and its three distinct pole locations remain separated.

A quantitative form is supplied below: for constants C>0 and epsilon_0>0 depending only on the fixed c,d and the exact boundary, one may choose a positive epsilon_r with

    epsilon_r >= min(epsilon_0, C/[r^2(2^r+2)^5]).

Equivalently, the forbidden r-state neighborhood has at least this size. The constants are defined analytically by compact extrema, not numerically estimated. No assertion that this lower bound is sharp is made.

## 2. Hankel-type nonnegative factorizations from a PH representation

If f(t)=alpha exp(Tt)w, w=-T1>=0, is a PH density of order n, then for any nonnegative times s_i,t_j,

    M_ij=f(s_i+t_j)
        =[alpha exp(Ts_i)] [exp(Tt_j)w].

Because a Metzler semigroup is entrywise nonnegative, this is a nonnegative matrix factorization M=UV with inner dimension n. Thus the nonnegative rank of each such finite matrix is at most the PH order. This only uses the semigroup identity and cannot be inferred merely from ordinary rank; in this family the ordinary Hankel rank remains5.

## 3. A robust zero-diagonal obstruction

**Lemma R.** Let M be a k-by-k nonnegative real matrix satisfying

    M_ii<=epsilon,
    m<=M_ij<=M_0 for i!=j,
    M_ij<=M_0 for all i,j,

where m,M_0>0. If k>2^r and

    epsilon < m^2/(4r^2 k M_0),

then M has no nonnegative factorization of inner dimension r or less.

**Proof.** Suppose M=UV with at most r nonnegative factors, padding zero factors if necessary. For every nonzero column of U, rescale it to have column sum1 and inversely rescale the corresponding row of V. Set both parts of a zero factor to zero. Then 0<=U_iell<=1 and

    V_ell j <= sum_i M_ij <= k M_0.

Indeed the sum of the active V_ell j over ell equals the column sum of M. Put tau=m/(2r k M_0) and define

    S_i={ell: U_iell>=tau} subset {1,...,r}.

If S_i were contained in S_j for i!=j, split M_ij into factors outside and inside S_i. The outside contribution is at most r tau k M_0=m/2. For ell in S_i, the inclusion gives U_jell>=tau, and the diagonal bound gives V_ell j<=epsilon/tau. Hence the inside contribution is at most r epsilon/tau, strictly smaller than m/2 under the displayed hypothesis. This contradicts M_ij>=m.

Thus the S_i are pairwise incomparable, in particular distinct. There are only2^r subsets, contradicting k>2^r. QED.

At epsilon=0, this specializes to the familiar support/rectangle obstruction for a matrix with zero diagonal and strictly positive off-diagonal entries. The quantitative estimate here is derived above; no external nonnegative-rank theorem is imported.

## 4. A nondegenerate double zero in the boundary density

Use the preceding manuscript's notation k_*=1/beta_* and x=b t. There,

    G_k'(x)=((1+k^2)^2/2) exp(-kx)(sin x-x cos x).

At x=xi, sin xi=xi cos xi>0, because xi lies in(2pi,5pi/2). Therefore

    G_{k_*}''(xi)=((1+k_*^2)^2/2) exp(-k_*xi) xi sin xi>0.

The density is f(t)=K exp(-ct)G_k(bt)/(d^2+b^2)^2 with strictly positive prefactors. At the threshold, G and G' vanish at xi, so differentiating twice gives f_{beta_*}''(t_*)>0, with no additional cross term. Thus the positive-time zero is exactly quadratic, not flatter.

Take the fixed compact interval

    J=[3t_*/4,5t_*/4].

On J define R(t)=f_{beta_*}(t)/(t-t_*)^2 away from t_*, extending continuously at t_* by f_{beta_*}''(t_*)/2. The uniqueness of the positive-time zero and the strict second derivative show R is continuous and strictly positive on J. Therefore

    C_0=min_{t in J} R(t)>0.

Choose some epsilon_0 in(0,beta_*/2), and let the parameter rectangle be [beta_*-epsilon_0,beta_*] times J. The exact closed-form f_beta(t) is continuously differentiable in beta there. Define finite positive constants

    C_1=1+max |partial_beta f_beta(t)|,
    M_0=1+max |f_beta(t)|

on that rectangle. Then, with delta=beta_*-beta in[0,epsilon_0],

    |f_beta(t)-f_{beta_*}(t)|<=C_1 delta,
    0<=f_beta(t)<=M_0 for beta<beta_*, t in J,
    f_beta(t_*)<=C_1 delta.

The nonnegativity in the second line is the elementary density-positivity result from the previous manuscript, not an assumption that a PH representation has already been constructed.

## 5. Exact sampled-time argument, without sampling execution

For a positive integer r put k=2^r+1 and define exact times

    h=t_*/[4(k+1)],
    s_i=t_*/2+i h,
    t_j=t_*-s_j,  i,j=1,...,k.

All times are positive, and

    s_i+t_j=t_*+(i-j)h in J.

Only the diagonal i=j has sum t_*. For i!=j, the distance from t_* is at least h. Consequently the boundary matrix has off-diagonal entries at least C_0 h^2. If

    delta <= C_0 h^2/(2C_1),

then for the neighboring strictly positive density,

    M_ij=f_beta(s_i+t_j)>=C_0 h^2/2=:m  for i!=j,
    M_ii=f_beta(t_*)<=C_1 delta.

Lemma R therefore rules out every r-state factorization, and hence every r-state PH representation, whenever additionally

    C_1 delta < (C_0 h^2/2)^2/(4r^2 k M_0)
             = C_0^2 h^4/(16r^2 k M_0).

One concrete positive neighborhood radius, with strict safety factors, is

    epsilon_r = min(epsilon_0/2,
                    C_0 h^2/(4C_1),
                    C_0^2 h^4/(32C_1 r^2 k M_0)).

For every 0<delta<epsilon_r, all hypotheses hold strictly. Since h=t_*/[4(k+1)] and k=2^r+1, fixed positive constants can be absorbed into C to give

    epsilon_r >= min(epsilon_0/2, C/[r^2(2^r+2)^5]).

For clarity, take C small enough to satisfy both

    C <= C_0 t_*^2/(64 C_1),
    C <= C_0^2 t_*^4/(8192 C_1 M_0).

The first h^2 term dominates C/[r^2(k+1)^5] because r>=1 and k+1>=1. The final term is C_0^2 t_*^4/[8192 C_1 M_0 r^2 k(k+1)^4], which dominates the chosen expression since k<=k+1. This verifies the claimed quantitative radius without omitting a k-dependent factor.

## 6. Consequence, import boundaries and novelty

The lower bound is independent of the PH-existence theorem: it applies to any hypothetical representation of f_beta. To say that finite minima actually diverge, combine it with the previous manuscript's positive-side O'Cinneide import, which proves PH existence for all beta<beta_*. No particular finite dimension in the remaining band is inferred from existence.

This obstructs the tempting but false global extension of the five/six-state table to a uniform bounded order over the entire PH region. It also explains why finding a single extra hidden pole cannot settle the all-beta target. The broad minimum-order function on1/sqrt2<beta<beta_* is still NOT determined.

All ingredients—PH Hankel factorizations, nonnegative-rank support obstructions, positive-time-zero barriers and classical PH characterization—have substantial prior art. The explicit fixed-degree family, quantitative neighborhood estimate and assembly are candidates for comparison, not a priority claim. Benvenuti2020's opened papers concern discrete-time spectral bounds and zero *samples*, not an authenticated exact statement of this continuous repeated-pole result; no claim of novelty is inferred from that distinction alone.

No scientific matrix was instantiated or checked in software. The k-by-k matrices above are quantified symbolic proof objects, not reported experiment outputs. Parent and independent written reconstruction remain required; formal/kernel verification has not occurred.
