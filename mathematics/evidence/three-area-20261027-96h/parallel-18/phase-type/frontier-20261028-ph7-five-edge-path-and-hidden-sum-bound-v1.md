# A PH7 realization above 1/5 MUST have a supported 5-edge path, with a quantitative hidden-sum bound

**NEW ALL-TOPOLOGY WRITTEN CANDIDATE; independent review and novelty clearance pending.** MathResearch96h-2. This strengthens the simple long-path theorem `frontier-20261028-ph7-supported-long-path-necessity-v1.md`; no change to that immutable source is made. No PH7 8/9 existence/exclusion or new PH6 theorem is claimed.

## Main theorem

For the original H and any `z=b²/(a-c)²>1/5`, every actual PH representation with seven states whose normalized shifted generator has nonpositive diagonal entries has a supported **simple input-to-exit path of EXACTLY FIVE edges**. A length6 path alone cannot substitute for it.

Write the actual characteristic quotient as `Q(y)=y²+p y+q`. Normalize the actual input/exit path coefficients as in §2; let eta>=0 be the total normalized weight of all supported 5-edge paths, let b>=0 be their weighted complement diagonal contribution plus all supported 6-edge path weights, and let V>=0 be the variance of the two-state complement trace sums of the supported 4-edge paths. Then the exact necessary inequality is

    eta(2p-8/5) >= 4(z-1/5)+(6/5)eta²+2b+V.         (BOUND)

In particular eta>0 and

    p >= 4/5 + sqrt[(24/5)(z-1/5)].                 (PBOUND)

At z=8/9 this is

    p >= (12+2 sqrt(186))/15,
    eta(2p-8/5) >= 124/45+(6/5)eta²+2b+V.          (CRIT)

For a critical PH7 realization, the previously independently supported irreducibility/Perron theorem makes every normalized diagonal escape rate strictly positive; hence eta>0 forces b>0 and the inequality in(PBOUND) is STRICT at8/9. No rounded threshold is used.

## 1. Exact full path-numerator decomposition

Use the normalized Metzler G and actual nonnegative input/exit beta,gamma of the preceding path theorem. Its target characteristic is `det(yI-G)=D_z(y)Q(y)`, and its actual numerator is `K Q(y)` with K>0. Relative degree5 makes the shortest supported input-to-exit distance exactly4. Every supported simple path therefore has length4,5 or6.

The determinant/adjugate path identity from the preceding theorem gives the actual decomposition

    Q(y)=sum_S lambda_S det(yI-G_S) + eta y + b,    (DECOMP)

where the length4 paths have two-state complement S, positive weights normalized to `sum_S lambda_S=1`; eta is the sum of length5-path weights divided by K; and b is the sum of each length5 weight times its one remaining diagonal escape rate, plus every length6 weight, all divided by K. This is an exact polynomial identity. Under the theorem's nonpositive-diagonal assumption b>=0; all weights are nonnegative. No assumption is made that all input/exit pairs have the same distance or that their complement is acyclic.

For each two-state complement write

    det(yI-G_S)=y²+p_S y+q_S,
    P0=sum_S lambda_S p_S,
    Q0=sum_S lambda_S q_S,
    V=sum_S lambda_S p_S²-P0² >=0.

Coefficient matching in(DECOMP) yields

    p=P0+eta,       q=Q0+b.                         (PQ)

## 2. Exact trace/variance calculation

Write `G_ii=-u_i`. The characteristic `D_z Q` gives

    tr G=-(4+p),
    tr G²=4(1-z)+p²-2q.

A two-state principal block satisfies `tr G_S²=p_S²-2q_S`. Metzler signs give

    tr G²-tr G_S² >= sum_(i outside S) u_i²
                   >= (sum_(i outside S)u_i)²/5.

The weighted average of the five-state complement sums is

    sum_S lambda_S sum_(i outside S)u_i
      =4+p-P0=4+eta.

Cauchy and Jensen then imply

    tr G²-sum_S lambda_S tr G_S² >= (4+eta)²/5.

Using(PQ) and `sum lambda p_S²=P0²+V`, rearrange exactly:

    4(1-z) >= (4+eta)²/5+V-2eta P0-eta²+2b.

Substitute `P0=p-eta` and move terms to get(BOUND). If `z>1/5` its right-hand side is strictly positive, so eta cannot be0: there is at least one ACTUAL supported simple 5-edge path. This is stronger than merely requiring a path of length5 OR6.

Because eta>0 and b,V>=0, divide(BOUND) by eta and use AM–GM:

    2p-8/5 >= 4(z-1/5)/eta+(6/5)eta
              >= 2 sqrt[(24/5)(z-1/5)].

This proves(PBOUND). At8/9, `4(z-1/5)=124/45` and the root becomes `2 sqrt(186)/15`, proving(CRIT). If G is irreducible of spectral bound0, each u_i>0; since eta>0, at least one length5 path exists and its one-state complement contributes strictly positively to b, making the bound strict. □

## 3. Scope and review targets

For critical PH7, the diagonal sign and irreducibility follow from the named previously supported global SCC/Perron proof; no unverified PH8 or held source is imported. The definitions of eta and b are explicitly tied to all ACTUAL paths and K, not auxiliary independent variables.

A reviewer should independently reconstruct the full adjugate path expansion, nonnegativity of every length5/6 contribution, the variance/Jensen directions and the algebra in(BOUND), including the strictness qualification. This is written mathematics, not a formal, executable, human/cross-vendor, novelty or parent-adoption claim.

The bound does not exclude all 7-state systems: p can be large, and a 5-edge path may exist. It does not prove minimum8 or an 8/9 PH witness. Earlier holds remain nonpremises and historical process findings remain.

END — a critical seven-state PH representation requires a real supported 5-edge path and a quantitatively large hidden quadratic sum.
