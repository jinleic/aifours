# Addendum 7 — existence of a single universal weighted entropy certificate

InfoGuessingRminus-2. Actual native clock immediately before writing: **Tue Oct 27 15:26:56 PDT 2026**. AUTHOR-WRITTEN UNREVIEWED, S1 definition-first work only.

This proves a coupling/duality fact rather than merely proposing a new coordinate encoding. The proof pays exact FD-preserving products, the relevant entropy closure, compact attainment in that closure, and the supporting-hyperplane normalization. No external entropy-cone result, historical proof, held guide, program, selected numeric law or source expansion is used. No original guessing-number improvement or novelty is claimed.

## 1. Universal theorem and precise ceiling

Let G be any fixed nonempty finite loopless digraph and g=gn(G). Then there exist real nonnegative weights w_v, with

`sum_v w_v=g`,

such that EVERY finite joint law satisfying the ORIGINAL graph FDs obeys

`H(X_V) <= sum_v w_v H(X_v)`.   (WC)

Conversely any nonnegative weights proving (WC) for all those laws give the original universal word-count bound with exponent sum_v w_v.

Thus using max_v H(X_v) in the homogeneous all-law criterion does not mean an improved upper bound would require an intrinsically nonlinear certificate: a SINGLE set of universal nonnegative marginal weights exists at the exact original exponent. The theorem does NOT print the weights or give a finite Shannon/copy-inequality derivation of their validity.

If the exponent is strictly below a given positive rational endpoint c0, the weights can be chosen rational while keeping their sum strictly below c0. This is an existence consequence with explicit slack, not rational approximation of an exact boundary certificate.

## 2. Which entropy closure is used — no FD-intersection shortcut

Let E consist of entropy profiles h(P) of ACTUAL finite laws P satisfying every original neighbour FD, over arbitrary finite component alphabets. Coordinates are h_A=H(P_A), for nonempty vertex subsets A.

Define K to be the closure of the conic hull of E in this finite-dimensional real coordinate space.

This is **not** asserted equal to the intersection of an ambient almost-entropic cone with FD hyperplanes. Such an equality is neither supplied nor needed. Exact-FD realizability before taking limits is retained in the definition of E.

Every h in K inherits the ordinary inequalities

`0 <= h_A <= sum_(v in A) h_v`,

and the original FD equalities, because they are homogeneous continuous linear relations holding on E. This is only a one-way inheritance, not a converse realizability claim.

## 3. Exact products pay the conic step

For a finite collection of original FD laws P_j and positive integer multiplicities m_j, form independent copies of the ENTIRE laws and group all copies at each ORIGINAL vertex. Each original decoder relation is applied componentwise, so the resulting finite tuple law retains every original FD exactly. Entropy profiles add:

`h(product_j P_j^(m_j))=sum_j m_j h(P_j)`.

This is expanded-alphabet tuple product, not same-alphabet quasigroup/Latin merging. No original coordinates or observed neighbours are deleted.

For arbitrary nonnegative real coefficients lambda_j, choose integers m_(j,N) with m_(j,N)/N -> lambda_j. Dividing the exact product-law entropy profile by N converges to sum_j lambda_j h(P_j).

By v1's proved actual-law/word criterion, every finite original law satisfies

`h_V <= g max_v h_v`.

It therefore also holds on the conic hull, using the product realization and the displayed limits, and then on K by continuity. It is important that this was NOT inferred by naively adding the max-entropy inequalities: maxima of different marginal profiles need not occur at the same vertex. The actual product law pays that coupling.

## 4. Compact normalized primal and its exact value

Consider

`B={h in K: h_v<=1 for all v}`.

It is closed. The inherited entropy inequalities bound every coordinate between zero and |A|, so it is bounded and hence compact. The continuous coordinate h_V attains its maximum p on B.

Every finite nonconstant FD law can be normalized by its positive max marginal entropy to give an element of B; v1's homogeneous law/word theorem gives p>=g. The extension of h_V<=g max_v h_v to K gives p<=g. Thus

`p=g`.

No finite-alphabet maximizer is asserted. Attainment is only in the explicitly defined entropy closure K, which is enough for the dual argument.

## 5. A closed cone with an actual supporting hyperplane

In R^(|V|+1), define

`D={(u,t): some h in K has u_v>=h_v for every v, and t<=h_V}`.

It is a convex cone. It is also closed: if (u_j,t_j) converges, every associated h_j has all singleton coordinates bounded above by u_j and every other coordinate bounded by the sum of its singletons. Hence h_j is bounded, and a subsequence converges to h in the closed K. The limiting inequalities place (u,t) in D.

The point z=(1,...,1,g) belongs to D by §4 and is a boundary point: increasing its last coordinate while fixing u would exceed the normalized optimum. D has nonempty interior, since it contains all strictly positive u with t<0 (take h=0).

A supporting hyperplane at z follows by elementary Euclidean projection: take exterior points approaching z, project each to the closed convex D, and normalize the displacement. A convergent subsequence of these unit normals yields a nonzero supporting normal at z. The nearest-point first-variation inequality gives the support relation for every point of D. Since D is a cone and contains both zero and 2z, its supporting offset is zero.

Write the resulting support inequality as

`alpha t - sum_v w_v u_v <= 0` for all (u,t) in D,

with equality at z. The coefficient signs are forced:
- increasing any u_v preserves D, so w_v>=0;
- decreasing t preserves D, so alpha>=0.

If alpha=0, equality at z would give sum_v w_v=0. Nonnegative weights would all vanish, contradicting the nonzero normal. Thus alpha>0. Divide by alpha. Equality at z gives

`sum_v w_v=g`.

For any h in K, the point (h_singletons,h_V) belongs to D, yielding (WC). This proves the claimed single universal weighted inequality without a missing Slater, closure or normalization hypothesis.

## 6. Actual-word converse and rational strict slack

For any nonempty ACTUAL winning set W at alphabet q, the uniform law on W satisfies all original FDs, H(X_V)=log|W| and H(X_v)<=log q. From nonnegative weights in (WC),

`log|W| <= (sum_v w_v) log q`.

An empty winning set already satisfies the count bound. Hence a universally valid weighted inequality gives the original all-q word-count bound. This caller uses the actual winning law, not a support with merely partial decoders.

Suppose g<c0. Starting from the real weights above, approximate each weight UPWARD by a nonnegative rational with total increase smaller than c0-g. Entropies are nonnegative, so the stronger right side still bounds H(X_V) universally. Its rational weight sum is strictly below c0. This is a valid slack argument; no assertion that exact boundary weights are rational follows.

Conversely rational nonnegative weights with sum<c0 and a complete universal proof of (WC) give an original strict upper improvement. Thus the original strict-upper problem is equivalent to finding such a rational universal weighted certificate, not necessarily a fixed-size combination of known information inequalities.

## 7. Reflection-symmetric weights for the original graph

For the actual reflection rho from Addendum 6, replace weights w by their group average over {identity,rho}. Applying (WC) to relabelled original laws proves that the averaged weights remain universally valid, nonnegative and have the same sum. Therefore the weights can satisfy

`w_3=w_7`, `w_4=w_6`, `w_9=w_10`.

The exact total budget is

`w_1+w_2+w_5+w_8+2(w_3+w_4+w_9)`.

With strict improvement slack, choose rational approximations upward by ORBITS, so the equalities and strict total-budget condition survive exactly. No weight value is selected, evaluated or claimed to work here.

This conclusion depends only on the actually proved FD-product and graph-automorphism couplings, not on averaging original laws or assuming linear/field strategies.

## 8. Remaining scientific gap

The theorem proves existence of an optimal universal weighted entropy inequality in a carefully defined actual-FD closure. It does not identify an improving weight tuple, prove its graph-specific inequality, show a finite certificate search terminates, or supply a strict-gain law. A finite Shannon/copy inequality combination is a possible proof representation, not a consequence of this dual existence theorem.

The entropy closure must remain the closure generated by EXACT original FD laws. Replacing it with all submodular functions, a selected finite alphabet, a guessed representable entropy family, or an unchecked FD-intersection of another cone would change the problem.

Accordingly the inherited interval is unchanged. The exact next missing object can now be stated as seven rational orbit weights with a genuinely universal all-ten-variable proof and total budget below the inherited upper endpoint, or an original finite law violating the lower-gain criterion. None is provided here.

Ordinary facts named/proved: finite independent probability products and entropy additivity; entropy monotonicity/subadditivity; continuity of finite-coordinate maxima; finite-dimensional closed/bounded compactness and Euclidean nearest-point supporting hyperplanes. No research-specific entropy-cone theorem or scientific execution is imported.

Source-scope MINOR, prior exposures, STOP outside S1, all HELD/ZERO/finding histories, N4 historical outcome/exit UNKNOWN and aux214 STOP remain. Same original slot/new root/deadline; no novelty or stronger acceptance claim.
