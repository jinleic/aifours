# Dimensional price of full-D privacy at both asymptotic ends

**AUTHOR CANDIDATE — WRITTEN plus exact rational coefficient checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:19:11 PDT 2026`.

## 1. Exact gaps and explicitly scoped imports

Let V_J,V_L be the original 2D full-D all-law J=E|X|^2 and L=E||X||_1 minima, and V_1,J,V_1,L the exact 1D private minima. Define

    G_J=V_J-2V_1,J,       G_L=V_L-2V_1,L.                                 (1)

These measure the actual cost of the original joint sensitivity constraint beyond separately optimized coordinate marginals; they are NOT the source-vs-target selector gaps.

Every assertion below is conditional on pinned UNREVIEWED candidates. The 1D values import `frontier-20261028-exact-scalar-marginal-relaxation-v1.md` SHA `cde9bcc08bd4f87e635f1a2566fb2eaae6f1b289df5ebd4d36707229c8fc60ed`. The low-privacy 2D leading values import `frontier-20261028-peak-floor-low-privacy-universal-v1.md` SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43` and `frontier-20261028-peak-floor-first-norm-universal-v1.md` SHA `fa39d7bdc125da7c8f7424d5976309227d8101a58b15efea919e8eb8376f04ea`. The high-privacy displayed coefficients import `frontier-20261028-high-privacy-sharp-value-series-v1.md` SHA `f59f37a4848b27d98442fae91270a5b482592074e8654d4b6b948f0045214ef2`, including its named parent v253/MDA and unreviewed selector dependencies.

## 2. High privacy epsilon->0

At the named scope,

    G_J = 1/6-(sqrt(3)/54)epsilon+O(epsilon^4),                          (2)
    G_L = epsilon/12-(sqrt(3)/108)epsilon^2
              -epsilon^3/1728+O(epsilon^4).                              (3)

In (2) the epsilon^2 and epsilon^3 coefficients BOTH cancel. Thus the 1D marginal relaxation has the correct `4/epsilon^2` J leading scale, yet its absolute dimensional privacy gap tends to 1/6. The corresponding L gap tends to 0 linearly. These are conditional written expansions, not novelty or formal-proof claims.

## 3. Low privacy b=e^(-epsilon)->0

The same source-scoped inputs give

    G_J/V_J =1-2^(-2/3)sqrt(3pi) b^(1/6)+o(b^(1/6)),                   (4)
    G_L/V_L =1-2^(2/3)b^(1/6)+o(b^(1/6)).                               (5)

Thus both independent-coordinate relaxations capture an asymptotically vanishing FRACTION of the actual 2D cost when b->0, while they are leading-order sharp for high privacy. This comparison does not imply a new mechanism or any printed source equivalence.

## 4. Algebra and actual exact checks

Write q=e^epsilon-1, m=1/q and `t=[m^3+(3m^2+m)/2]^(1/3)`. The 1D theorem gives

    2V_1,J=2[m^2+m+t^2],   2V_1,L=1/sinh(epsilon/2).

Expand exactly in q:

    (t/m)^2 =1+q+q^2/12-q^4/144+q^5/144+O(q^6).                        (6)

Using q=epsilon+epsilon^2/2+epsilon^3/6+..., the q^2 and q^3 contributions after multiplying by m^2 cancel at epsilon^3. Consequently

    2V_1,J=4/epsilon^2-1/6+epsilon^2/360+O(epsilon^4),
    2V_1,L=2/epsilon-epsilon/12+7epsilon^3/2880+O(epsilon^5).            (7)

Subtract the pinned f59 expansions to obtain (2)–(3). In the Python eval kernel, `fractions.Fraction` checked the q^4 and q^5 coefficients -1/144,+1/144 and `1/540-7/2880=-1/1728`; these checks do not validate the optimizer imports.

For b->0, the exact 1D formula gives `2V_1,J~2^(1/3)b^(2/3)` and `2V_1,L~2b^(1/2)`. Divide by the pinned 2D values `V_J~2b^(1/2)/sqrt(3pi)` and `V_L~2^(1/3)b^(1/3)` to obtain (4)–(5). At epsilon=ln 2, the separately pinned unreviewed `frontier-20261028-ln2-dimensional-gaps-v1.md` SHA `da05d6704968e88a977500264b7284b1da698fb878a60ad6a4016d10ef39f40d` gives exact rational enclosures for the two finite-epsilon gaps.

## 5. Status

The four displayed asymptotics are written deductions and exact coefficient arithmetic conditional on the listed, unreviewed dependencies. They are not independently reviewed, formally checked, novel by assertion, or parent-adopted. Review should verify the q^5 coefficient and cubic cancellation, error orders, and the distinctions between absolute and relative gaps.
