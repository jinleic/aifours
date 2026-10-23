# An exact finite moment criterion (no novelty asserted)

Let n>2 be even, p=n²+n+1 prime, m=n+1, and D=mu_m in F_p^*.
For each even t with 2<=t<=n-2 set

    A_t = sum_{j=0}^t (-1)^j binom(t*m,j*m).

Then D is a planar difference set if and only if A_t=0 (mod p) for all
these t. This is an elementary finite-field moment reformulation, likely
part of the classical character/binomial criteria for cyclotomic difference
sets. It is not asserted to be new and does not prove their inconsistency.

Proof. For an integer k>=0 write S_k=sum_{a in D} a^k in F_p. Since D is
a cyclic group of order m, S_k=m if m|k and S_k=0 otherwise. Put

    N_x = #{(a,b) in D²: a-b=x}  (x in F_p^*).

There are m(m-1)=p-1 nonzero ordered differences in total, and 0<=N_x<=m<p.
For k>=1, expansion gives

    sum_{x!=0} N_x*x^k = sum_{a,b in D}(a-b)^k
                       = sum_{j=0}^k (-1)^j binom(k,j) S_{k-j} S_j.

For 1<=k<=p-2 this is automatically zero unless k=t*m with 1<=t<=n-1.
At those exponents it equals m²*A_t, because m is odd. If t is odd,
pairing j with t-j makes A_t vanish as an integer. Thus the displayed
even-t conditions are exactly the vanishing of every moment 1<=k<=p-2.

If D is planar, N_x=1, so all those moments vanish. Conversely, suppose
the conditions hold. Let c_x=N_x-1 in F_p. Its moment at k=0 vanishes
because sum N_x=p-1. Its moments at every k=1,...,p-2 vanish by the
expansion and sum_{x!=0}x^k=0. The (p-1)-by-(p-1) Vandermonde matrix on
the distinct nonzero field elements is invertible. Hence all c_x=0 in F_p.
Since 0<=N_x<=m<p, it follows that N_x=1 as an ordinary integer. This is
planarity. QED.

In particular, the t=2 condition is

    binom(2n+2,n+1) = 2 (mod p).

The restriction n>2 matters: at n=2 the exponent 2m is p-1 rather than
below p-1, and the stated t=2 necessary congruence does not apply.

This angle does not resolve the contract. Direct central-binomial evaluation
already takes work growing with n; all moments are much more expensive at
the production orders. No all-orders contradiction was obtained. The much
cheaper base-two necessity and exact divisor sieve remain the scan filters.

Cheap falsification controls in `moment-controls.json` retain n=8, for which
all required even moments t=2,4,6 vanish. The nonplanar base-two controls n=90
and n=512 already fail at t=2; n=24 passes t=2 but fails t=4. These are alternate
checks of known isolated exceptions, not new nonexistence results. At n=2 the
t=2 central-binomial residue is 6 modulo 7, confirming the need for the stated
exponent-range guard. `code/moment_controls.py` records all exact binomial sums
computed here; it evaluates only t<=8 and is not a production filter.
