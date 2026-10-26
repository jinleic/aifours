# A complete distributional invariant for the entire sharp gamma-bound curve

**Status: CANDIDATE / NOVELTY_UNCLEAR.** Written strengthening within the frozen model. This gives an exact population-identified-set summary, not a Fisher–Neyman sufficient-statistic theorem, finite-sample result or new target. It uses the main theorem with its operative addendum. No scientific program was used. The earlier median/clamp selector manuscript remains correct; the formula below explains the additional simplification caused by the feasible switch-mass domain.

## 1. Feasible-domain identity

Use the main notation I=[l,u], h=q-p, t=r-h and eta=gamma-g_min in [0,1]. Every r in I satisfies

    r+t=2r-h<=1,
    r<=(1+h)/2.                                            (1)

Define

    W(r)=u_0(r)+u_1(r-h),
    Wbar(r)=r+(r-h)-ell_0(r)-ell_1(r-h).                    (2)

Both functions are nonnegative, concave and nondecreasing on I, with increments bounded above by twice the mass increment. Wbar is exactly the combined upper-tail function after reflecting the factual outcomes by y -> 1-y.

## 2. The slope-capped envelope

For any such W define, for every real m,

    E_W(m)=max_(r in I) [ W(r)-(r-m)_+ ].                   (3)

This is a well-defined attained maximum on compact I.

### Lemma 1

Restricted to I, E_W is the **least nondecreasing 1-Lipschitz majorant** of W. It is also concave. More precisely, choose any

    r_0 in argmax_(r in I) [W(r)-r],
    K=max_(r in I) [W(r)-r].

Then for all real m,

    E_W(m)=m+K,                if m<=r_0,
    E_W(m)=W(m),               if r_0<=m<=u,
    E_W(m)=W(u),               if m>=u.                    (4)

In the middle line m is automatically in I. At overlaps the formulas agree. If the argmax has several points, any choice gives the same function in (4).

### Proof

For fixed r, the function W(r)-(r-m)_+ is nondecreasing and 1-Lipschitz in m. Its maximum over r has the same two properties. Setting r=m shows E_W(m)>=W(m) for m in I.

If g is any nondecreasing 1-Lipschitz majorant of W on I, then for any m,r in I,

    g(m)>=g(r)-(r-m)_+>=W(r)-(r-m)_+.

The first inequality follows from monotonicity when r<=m, and from the Lipschitz property when r>=m. Taking the maximum in r proves g>=E_W on I. Thus the stated least-majorant characterization is exact.

The function W(r)-(r-m)_+ is jointly concave in (r,m). For two values m_1,m_2 and maximizing r_1,r_2, the convex combination of the r_i remains in I. Joint concavity then gives the concavity inequality for E_W. This argument does not require differentiability.

To prove (4), split the maximization into r<=m and r>=m. In the first part, the objective is W(r); monotonicity puts its maximum at the largest allowed r. In the second part the objective is m+[W(r)-r]. The bracket is concave, with maximum K at r_0. For m<=r_0 this second part reaches m+K, and every r<=m obeys W(r)<=r+K<=m+K. For r_0<=m<=u, concavity makes W(r)-r nonincreasing on [m,u], so its maximum there is W(m)-m; the r<=m part also has maximum W(m). For m>=u, every r is <=m and the maximum is W(u). If a whole interval maximizes W(r)-r, W(r)=r+K on that interval, so all choices of r_0 yield the same formula. QED.

## 3. Exact formulas for both bound curves

Define the two tent variables

    m_L(eta)=min(h+eta,1-eta),
    m_U(eta)=min(h+1-eta,eta).                              (5)

### Theorem 1

For every compatible gamma,

    L(gamma)=-E_W(m_L(eta)),
    U(gamma)= E_Wbar(m_U(eta)),
    eta=gamma-g_min.                                       (6)

Thus the complete dependence of both endpoints on gamma is encoded in **two slope-capped tail envelopes**, rather than the original two factual distributions or a fresh optimization for every gamma.

### Proof

The main lower objective is

    F_eta(r)=(r-(h+eta))_+ +(r-(1-eta))_+-W(r).

The two hinge locations sum to 1+h. Their larger value is at least (1+h)/2, which is >=r for every feasible r by (1). Therefore the hinge at the larger location is always zero, and

    F_eta(r)=(r-m_L(eta))_+-W(r).

Minimizing gives the first formula of (6).

For reflected outcomes the combined upper-tail function is Wbar, the budget is 1-eta and the treatment effect changes sign. Applying the same lower formula to that reflected model gives

    U(gamma)=E_Wbar(min(h+1-eta,eta)),

which is the second formula. This is also obtained by directly expanding the main G_eta. QED.

### Relation to the median/clamp selectors

Because the larger hinge is >=u, the lower minimizer in `proof-gamma-independent-selectors-v1.md` simplifies to

    r_L(eta)=clamp_I(max(r_minus,m_L(eta))),

and the upper selector to

    r_U(eta)=clamp_I(max(r_plus,m_U(eta))).

These are exactly the former median/clamp formulas on the actual feasible domain, not a different convention or changed optimizer. Equation (4) gives their values explicitly.

## 4. Necessity: the bound curves recover the envelopes

Fix p,q and g_min, so I and the compatible gamma interval [g_min,g_min+1] are fixed. For any m in I, set eta=m-h. This lies in [0,1] because eta=t is a feasible defier mass. Equation (1) gives

    min(h+eta,1-eta)=min(m,1-m+h)=m.

Hence the entire lower curve determines

    E_W(m)=-L(g_min+m-h),  m in I.                         (7)

Similarly, set eta=m, which lies in [0,1]. Again (1) gives min(h+1-m,m)=m, so

    E_Wbar(m)=U(g_min+m),  m in I.                         (8)

The envelope on I determines its values outside I as well: at the lower endpoint l<=r_0,

    K=E_W(l)-l,

so E_W(m)=m+E_W(l)-l for m<l, while E_W(m)=E_W(u) for m>u. The same applies to Wbar. Singleton I causes no exception.

### Corollary: exact equivalence criterion

For two factual-law pairs with the same p,q and g_min, the following are equivalent:

1. their sharp intervals [L(gamma),U(gamma)] agree for **every** compatible gamma;
2. their two envelope restrictions E_W|I and E_Wbar|I agree.

Sufficiency follows from (6) and the outside-I extensions; necessity follows from (7)–(8). This is an exact complete invariant for the population identified-interval curve. It is stronger than merely saying that the original distributions suffice, and it does not falsely imply that all differences between factual distributions change the answer: differences erased by both envelopes are irrelevant to this entire bound curve.

## 5. Relation to the moment barrier and sign threshold

The sharp positive-effect threshold is a single ordinate of the first envelope:

    Gamma_*=g_min+1+K
           =g_min+1+E_W(l)-l.                             (9)

Thus a purpose-built one-number summary suffices for that particular strict-positive decision at fixed p,q. The all-k moment-barrier manuscript says that no finite fixed order of ordinary raw moments can uniformly determine this number, even within positive smooth symmetric densities. There is no contradiction: an arbitrary nonlinear trimmed-tail functional is not an ordinary moment truncation.

For the whole gamma curve, the two envelopes in the exact equivalence criterion are sufficient and necessary at the level of population identified sets. No finite-dimensionality claim is made for the class of all such envelopes, and no assertion is made that a unique factual law can be reconstructed from them.

## 6. Boundaries

The envelope construction is elementary convex analysis and may be a classical corollary; no separate novelty claim attaches to it. The contribution proposed here is the exact reduction and invertible correspondence (7)–(8) for this particular sharp surrogate-bound model. This manuscript has no fresh independent review yet; its status is CANDIDATE, not automatically WRITTEN_CHECKED from the main proof. It changes none of the original assumptions, adds no statistical/clinical guarantee, and does not clear the Kuroki 2013 ACCESS_BLOCKED prior-art gate.
