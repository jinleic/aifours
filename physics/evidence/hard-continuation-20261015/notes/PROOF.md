# Random 4-SAT and 5-SAT are unsatisfiable w.h.p. at densities 9.9325 and 21.1175

Continuation package of 2026-10-15 (PT). Self-contained written proof plus the exact
statement of every numerical premise. Status, stated separately:

* **Certificate (numerical premises):** rigorous outward-rounded rational enclosures of
  `Psi_512` for two explicit rational warning laws, reproduced by two new arithmetic
  implementations in this package (`code/certify_a.py`, `code/certify_b.py`) and by the
  parent's separately written checker (receipt referenced in `README.md`). The two epoch-2
  checkers (read-only snapshot code) reproduce the same laws' `T=128` enclosures.
* **Full proof:** Sections 1–7 below (the analytic bridge) plus those premises. The bridge is a
  written proof. It was audited by derivation in epoch 1 and epoch 2 (parent audit, two referee passes)
  and by an adversarial Opus review that returned "correct". It is **not formally verified and not
  peer reviewed.**
* **Formalized subset:** none in this lane. A separate lane owns `formal/`.

## 0. Attribution: no new method is claimed

Every method used here is prior art. Lower bounds on the ground-state energy of diluted spin
systems by Guerra-type replica interpolation, and the resulting 1RSB/cavity variational *upper*
bounds on the SAT threshold, are due to Franz–Leone (J. Stat. Phys. 111, 2003; arXiv
cond-mat/0208280), where the argument is proved for **even** clause arity. Panchenko–Talagrand
(PTRF 130, 2004) proved related bounds, also for even p. Lelarge–Oulamara (J. Stat. Phys. 173,
2018; arXiv:1708.02457, condition (4)) give a combinatorial interpolation that admits **odd**
arity when the factors are nonnegative. Achlioptas–Menchaca-Méndez (ICALP 2012) introduced an
energetic interpolation for unsatisfiability bounds. The integer-cost, `y`-reweighted energetic
interpolation and the exact-rational certificate style below follow Vorobyev (arXiv:2610.10599,
2026), which treats `k=3`. Its Lean development was not used. Sections 2–7 specialize that argument
to general `k`. The degree-`k` remainder (F) is the Lelarge–Oulamara nonnegativity condition.
The infinite-`T` functional `Psi_oo` is the zero-energy survey-propagation (energetic 1RSB)
complexity of Mézard–Parisi–Zecchina and Mertens–Mézard–Zecchina, evaluated at a trial law rather
than at a fixed point. At most the explicit certified constants could be new. Priority is the
parent's responsibility and is not asserted here.

## 1. Models, trial law, and the criterion

Fix integers `k >= 2`, `n >= 1`, density `alpha > 0`, an integer `T >= 1`, and a probability law
`rho` of finite support in `[0,1)`. All copies of a random variable `R ~ rho` are independent
unless explicitly shared.

*Auxiliary repeated-variable model.* Each ordered clause has `k` **independent** uniform indices in
`[n]` and `k` independent fair forbidden values `J in {0,1}`. Its cost at `sigma` is the product of its
`k` literal-violation indicators `1{sigma_i = J}`. Costs remain 0 or 1 when indices repeat. `E(F)` is
the minimum total cost over all `2^n` assignments.

*Target model.* `M = floor(alpha n)` independent clauses, each on a uniformly random set of `k`
**distinct** variables with independent fair signs. Clauses are sampled independently, so
repeated clauses are allowed.

Let `Q` be a product of `k-1` iid copies of `R` and `lambda = k alpha / 2`. Define

    nu_i  = E (1-Q)^i,                    M_i = exp(lambda (nu_i - 1)),        i = 0..T,
    mu_j  = sum_{i=0}^{j} (-1)^i binom(j,i) M_i,                                j = 1..T,
    d_oo  = E log(1 - R_1 ... R_k),
    Psi_T = - sum_{j=1}^{T} mu_j^2 / j  -  (k-1) alpha d_oo.

We prove, for every `y > 0` and every `n >= 1`,

    -(y/n) E E(F_rep_Poisson(alpha n))  <=  Psi_T + T exp(-y).                          (A)

Consequently, if `Psi_T <= -epsilon` and `T exp(-y) <= epsilon/2`, then

    E E(F_rep_Poisson(alpha n)) >= c0 n,   c0 = epsilon/(2y),   for every n >= 1.        (B)

## 2. Exact insertion identity

For an integer-valued `H` on the finite assignment space, a `{0,1}`-valued `V`, and the
(nonempty) minimizer set `M(H)`:

    min(H + V) = min H + 1{ V(sigma) = 1 for all sigma in M(H) }.                         (C)

If some minimizer has `V = 0`, the minimum is unchanged. Otherwise every old minimizer rises to
`min H + 1`, and since `H` is integer-valued every nonminimizer already has cost at least
`min H + 1`. Integrality is essential: `H = (0, 1/2)`, `V = (1, 0)` has increment `1/2`.

For a seed `x = (i, J, R)` put `b(x, a) = 1{sigma_i = J for every minimizer of H_a}`, where `H_a`
contains the existing clauses and the existing one-variable sites with activation outcome `a`. A
clause's indicator is the conjunction of its literal indicators. So the indicator in (C) for a new
clause is `prod_{l=1}^{k} b(x_l, a)`: the two universal quantifiers commute. If an index repeats with
opposite signs, the clause cost is identically 0 and the product of the `b` factors is 0, because a nonempty minimizer
set cannot fix one variable to both values.

## 3. Clause and site increments; the local comparison

A *row* is `k` independent seeds `x_l = (i_l, J_l, R_l)`: indices uniform and independent, `J_l` fair,
`R_l ~ rho`. Its clause has cost `prod_l 1{sigma_{i_l} = J_l}`. Its *site* has cost
`V 1{sigma_{i_1} = J_1}`, where `V` is an independent Bernoulli activation with mean
`Q = R_2...R_k`. Rows and activations are independent.

For `K` clauses and `L` sites, condition on the rows and average only over the activations `a`:

    Z_y = E_a exp(-y min H_a),  Phi_y = log Z_y,  f(K,L) = E_rows Phi_y,
    q = 1 - exp(-y),  d_y = E log(1 - q R_1...R_k).

`-y(K+L) <= Phi_y <= 0`, and adding one clause or site changes `Phi_y` by an amount in `[-y, 0]`. With the
tilted law `mu_y(a) = P(a) exp(-y min H_a)/Z_y` and brackets for `mu_y`-expectations, (C) and the
independence of a new site's activation give

    Delta_C Phi_y = log(1 - q < prod_{l=1}^k b(x_l, a) >),
    Delta_S Phi_y = log(1 - q R_2...R_k < b(x_1, a) >).                                   (D)

For `h >= 1` take `h` independent replicas `a_1..a_h` of `mu_y` (old rows fixed) and put
`B_h = E_x prod_{t=1}^h b(x, a_t)` and `C_h = E R^h`. Both lie in `[0,1]`. With
`W_C = < prod_l b(x_l,a) >`, `W_S = R_2...R_k < b(x_1,a) >` and `W_D = R_1...R_k`:

    E_new[W_C^h] = < B_h^k >_h,   E_new[W_S^h] = < B_h >_h C_h^(k-1),   E_new[W_D^h] = C_h^k.   (E)

**(E) uses that the `k` seeds of a new clause are iid, and in particular that their indices are
independent and uniform.** This is why the comparison is run in the repeated-variable model. For
distinct-variable clauses the seeds are dependent, and the first identity is false. The target model
enters only in Section 6, through a coupling with an explicit loss.
To prove (E), expand the `h`-th power as an expectation over `h` replicas, interchange finite
expectations, and average the `k` independent seeds; each contributes `B_h`. The site's rate
variables are independent of its first seed and of the old activations.

For all `B, C >= 0` (Lelarge–Oulamara-type remainder):

    B^k - k B C^(k-1) + (k-1) C^k = (B - C)^2 sum_{l=0}^{k-2} (l+1) B^(k-2-l) C^l >= 0.         (F)

It needs only `B, C >= 0`, so it holds for odd `k`. With `log(1 - q z) = -sum_h q^h z^h / h`, which is
absolutely convergent on `[0,1]` with total bound `sum q^h/h = y`, (D)–(F) give
`E_new Delta_C - k E_new Delta_S + (k-1) d_y <= 0`. Averaging over the old rows gives

    f(K+1, L) + (k-1) f(K, L) <= k f(K, L+1) - (k-1) d_y.                                  (G)

## 4. Finite replacement and Poissonization

`S_N(K,L) = sum_{j=0}^N binom(N,j)(k-1)^(N-j) f(K+j, L)` satisfies, by Pascal induction and (G),

    S_N(K, L) <= k^N [ f(K, L+N) - (k-1) N d_y / k ].                                      (H)

Set `K = L = 0`, divide by `k^N` and average over `N ~ Poisson(k alpha n)`. Binomial thinning turns `N`
into `J ~ Poisson(alpha n)`. Absolute convergence follows from `|f(K,L)| <= y(K+L)`. Hence

    -y E E(F_rep_Poisson(alpha n)) <= E_{L ~ Poisson(k alpha n)} f(0, L) - (k-1) alpha n d_y.   (I)

## 5. Exact site moments and a signed finite-y estimate

Hold the site rows fixed. At variable `v` let `A_v` (`B_v`) be the product of `(1-Q)` over the sites at
`v` that penalize value 0 (value 1), with empty products equal to 1, and put `G_v = A_v + B_v - A_v B_v`.
Given the rows, `G_v` is the probability over the activations that at least one value of `v` is
unpenalized. A variable whose two values are both penalized has at least one violation. So

    Phi_y <= sum_v log(G_v + (1 - G_v) exp(-y)).                                            (J)

Under `L ~ Poisson(k alpha n)` the marked counts at the `2n` pairs `(v, s)` are independent
`Poisson(lambda)` with iid `Q` marks. **This exact independence needs the Poisson count `L`, which
Section 4 supplies. With a fixed site count, `A_v` and `B_v` would be dependent and the formula for `M_i`
would be inexact.** Hence `E A_v^i = exp(lambda(E(1-Q)^i - 1)) = M_i`, `mu_j = E(1-A_v)^j >= 0`, and

    E[(1-A_v)^j (1-B_v)^j] = mu_j^2.                                                       (K)

For `x in [0,1]` and `delta in (0,1]`,
`log(1 - (1-delta) x) <= -sum_{j=1}^T (1-delta)^j x^j / j <= -sum_{j=1}^T x^j / j + T delta`.  (L)
Apply (L) with `x = (1-A_v)(1-B_v)` and `delta = exp(-y)`, then use (K):

    (1/n) E f(0, L) <= -sum_{j=1}^T mu_j^2 / j + T exp(-y).                                  (M)

Since `q <= 1`, `d_y >= d_oo`, and `d_y` has a negative coefficient. Substituting (M) into (I) proves (A).
Only finite sums of bounded quantities were averaged. No infinite-`y` limit is exchanged.

## 6. Poisson to fixed count; repeated to distinct variables

Couple the Poisson and fixed counts through one iid clause sequence. Adding a clause changes the
minimum by at most 1, so with `M = floor(alpha n)`,

    E E(F_rep_M) >= c0 n - E|N - M| >= c0 n - sqrt(alpha n) - 1.                              (N)

Keep each repeated-variable clause whose indices are distinct. Otherwise resample its ordered tuple uniformly
from the distinct ordered `k`-tuples, keeping its fair signs. The output clauses are iid, uniform over
distinct tuples, with fair signs. Forgetting order gives exactly the target model. A clause is
replaced with probability at most `binom(k,2)/n`, and each replacement moves the minimum by at most one:

    E E(F_dist_M) >= c0 n - sqrt(alpha n) - 1 - alpha binom(k,2).                             (O)

With `c = c0/2` the right side is at least `c n` whenever

    n >= N0 = ceil( max( k, 16 alpha / c0^2, 4 (1 + alpha binom(k,2)) / c0 ) ),                (P)

because the two middle conditions give `sqrt(alpha n) <= c0 n/4` and `1 + alpha binom(k,2) <= c0 n/4`.

## 7. Concentration (McDiarmid)

`X = E(F_dist_M)` is a function of the `M` independent clauses `C_1..C_M`, and replacing one clause
changes it by at most 1. McDiarmid's bounded-differences inequality (C. McDiarmid, *On the method
of bounded differences*, Surveys in Combinatorics 1989) gives

    P( X - E X <= -t ) <= exp( -2 t^2 / M ).

In conditional-Hoeffding form: the Doob increment `D_t = E[X | C_1..C_t] - E[X | C_1..C_{t-1}]`
lies in an interval `[L_t, L_t + 1]` whose endpoints are functions of `C_1..C_{t-1}` only. This uses
independence: `E[X | C_1..C_t] = g_t(C_1..C_t)` with `g_t(c_1..c_t) = E f(c_1..c_t, C_{t+1}..C_M)`, and
`sup_c g_t - inf_c g_t <= 1`. Hoeffding's lemma gives `E[exp(s D_t) | C_1..C_{t-1}] <= exp(s^2/8)`, and
Chernoff with `s = 4t/M` yields the bound. For `n >= N0` put `t = E X >= c n`. Since `M <= alpha n`,

    P( F_dist_M is satisfiable ) = P( X = 0 ) <= exp( -2 c^2 n / alpha ).                      (Q)

Satisfiability is monotone under adding clauses, so the same bound holds at every larger
density (couple `floor(alpha' n) >= floor(alpha n)` clauses). No limiting threshold is presupposed.

## 8. Moment identities used by certifier B (new in this package)

Let `c_h = E R^h` (`c_0 = 1`) and `r_max = max supp rho < 1`.

* (R2) `nu_i = sum_{h=0}^{i} (-1)^h binom(i,h) c_h^(k-1)`. This is the binomial expansion of `(1-Q)^i`,
  using `E Q^h = prod_l E R_l^h = c_h^(k-1)` for iid factors.
* (R3) `-d_oo = sum_{h>=1} c_h^k / h`. Expand `-log(1-z) = sum z^h/h` with `z = R_1...R_k in [0, r_max^k]`. All
  terms are nonnegative, so Tonelli lets us exchange the sum and the expectation, and
  `E (R_1...R_k)^h = c_h^k`. Since `c_h <= r_max^h`, the tail satisfies
  `sum_{h>H} c_h^k/h <= r_max^(k(H+1)) / ((H+1)(1 - r_max^k))`.
* (R4) `mu_j = (Delta^j M)_0` with `(Delta u)_i = u_i - u_{i+1}`. This follows by induction from
  Pascal's rule. Moreover `(Delta^j M)_i = E[A^i (1-A)^j] in [0,1]`.

These are identities of finite sums, or of absolutely convergent series with nonnegative terms.
Psi_T therefore depends on `rho` only through `c_0..c_max(T,H)` and the clause-series tail.

## 9. Explicit rational data and the certified inequalities

Laws (exact rationals; `certificates/trials.json`, sha256 `1cdc03c2…0913e`):

| law | atoms r_t | masses w_t |
|---|---|---|
| L4 | 12429/125000, 119439/500000, 374021/1000000, 459127/1000000, 706769/1000000, 907479/1000000 | 61927/500000, 62173/500000, 184067/1000000, 208197/1000000, 14413/50000, 17819/250000 |
| L5 | 178367/1000000, 38141/125000, 412273/1000000, 25963/50000, 537129/1000000, 97351/125000 | 15517/125000, 61949/500000, 35221/250000, 52589/250000, 207173/1000000, 193553/1000000 |

The masses sum exactly to 1, and every atom lies in `(0,1)`. Certifiers A and B give the enclosures below.
For the two `T=512` rows the parent's 768-bit checker prints the same upper bounds to all 18 of its
decimals, and it passed all four rows. The two epoch-2 checkers reproduce the `T=128` rows:

| trial | k | alpha | T | y | enclosure of Psi_T (outward, 20 d.p.) | epsilon |
|---|---|---|---|---|---|---|
| k4_T512 | 4 | 3973/400 = 9.9325 | 512 | 20 | [-0.00000599415877186445, -0.00000599415877186444] | 1/200000 |
| k5_T512 | 5 | 8447/400 = 21.1175 | 512 | 20 | [-0.00000683568324447069, -0.00000683568324447068] | 1/200000 |
| k4_T128 | 4 | 4967/500 = 9.934 | 128 | 20 | [-0.00005496703980446099, -0.00005496703980446098] | 1/20000 |
| k5_T128 | 5 | 21123/1000 = 21.123 | 128 | 20 | [-0.00001182413688821071, -0.00001182413688821070] | 1/100000 |

For every row, `T exp(-20) <= 0.00000105531065468855` (`T=512`) or `<= 0.00000026382766367214` (`T=128`).
Both are at most `epsilon/2`. With (B), (P) and (Q), the exact constants are (`code/transfer_constants.py`):

| k | alpha | c0 | c | N0 | P[SAT] for n >= N0 |
|---|---|---|---|---|---|
| 4 | 3973/400 | 1/8000000 | 1/16000000 | 10,170,880,000,000,000 | <= exp(-n / 1,271,360,000,000,000) |
| 5 | 8447/400 | 1/8000000 | 1/16000000 | 21,624,320,000,000,000 | <= exp(-n / 2,703,040,000,000,000) |

**Theorem (written proof + certified premises).** For `k = 4` and every `alpha >= 3973/400 = 9.9325`, and
for `k = 5` and every `alpha >= 8447/400 = 21.1175`, the target-model formula with `floor(alpha n)`
clauses is unsatisfiable with probability tending to 1. The table gives explicit rates.
The `N0` values are coarse sufficient cutoffs for the asymptotic statement, not finite-size predictions.

## 10. Enclosure obligations of the two arithmetic routes

Every inequality is decided by integer or `Fraction` comparison. No floating-point value enters a
gate, and gates use explicit exceptions rather than `assert`.

**Certifier A** (product laws; binary grid `2^-P`, `P = T + 192 + 8m`):
(A1) exact multiset enumeration of the `(k-1)`- and `k`-fold product laws, with total mass checked to be 1;
(A2) `nu_i` from per-atom powers of `1-q` with floor/ceil rounding. Products of nonnegative enclosures
are monotone, and the upper value is clamped to 1;
(A3) `exp(x)` for `x <= 0`: write `u = x/2^64` exactly, so `a = -u < 2^-20`. The magnitudes `a^n/n!`
strictly decrease, so Leibniz gives `|e^-a - S_N| <= a^(N+1)/(N+1)!`. Each magnitude is rounded in its
safe direction, and 64 outward squarings of a nonnegative enclosure give `exp(x)`. `M_i` takes its lower
end at the lower `x` and its upper end at the upper `x`;
(A4) `mu_j` by an interval forward-difference table, `[a] - [b] = [a_lo - b_hi, a_hi - b_lo]`, clamped to
`[0,1]` by (R4);
(A5) `sum mu_lo^2/j <= sum mu_j^2/j` because `0 <= mu_lo <= mu_j`;
(A6) `-log(1-z)` per atom: the series partial sum is a lower bound, and the same sum plus
`z^(N+1)/((N+1)(1-z))` is an upper bound;
(A7) `Psi_upper = -S_lo + C_hi <= -epsilon`, and `T e^-y <= epsilon/2` with the upper bound from (A3).

**Certifier B** (moments; decimal grid): (B1) exact integer moment sums give the exact rational `nu_i`
through (R2); (B2) the rational `a_i = lambda(1 - nu_i)` is enclosed on `10^-D`, and `exp(-a)` comes from the
full alternating Taylor series. That series has no argument reduction. Its magnitudes decrease for
`n >= a`, so Leibniz bounds the remainder by the first omitted magnitude. Guard digits
`ceil(0.4343 a) + 12` absorb the `e^a` cancellation; they affect width, not validity.
(B3) explicit binomial sums with endpoint selection by coefficient sign; (B4) as (A5) in exact
Fractions; (B5) the exact partial sum of (R3), plus its tail bound, at a cutoff `H` where the tail
is `< 10^-60`; (B6) the finite-`y` check with (B2).

The two routes share only the formula and the trial file. Their agreement checks arithmetic. It does
not independently establish the formula or the analytic bridge; Sections 1–7 do that.

## 11. What changed relative to the epoch-2 proof (each change audited here)

1. New laws and parameters (Section 9): six atoms, `T = 512`, and smaller `epsilon`. The analytic statement is
   unchanged. Larger `T` only removes more nonnegative terms from the truncation in (L).
2. Section 7 now cites McDiarmid and states the conditional-Hoeffding form with predictable endpoints.
   The bound and the factor 2 are unchanged.
3. (E) and (K) now flag their load-bearing modelling hypotheses: iid indices and a Poisson site count.
4. Section 8 (moment identities) is new. It is used only by certifier B, and each identity is proved above.
5. Section 10 records the two new enclosure algorithms. Each step's direction was checked against the
   code. The certified enclosures agree with each other to every printed digit and with the parent's
   768-bit checker.
6. Unchanged and still load-bearing: (A)–(Q) as in epoch 2, with `n >= 1` for (A) and `n >= k` only in Section 6.
