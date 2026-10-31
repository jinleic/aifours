# Higher-order high-privacy values and inverse budgets

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction-in-Q(sqrt(3)) coefficient checks; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 19:46:24 PDT 2026`.

## 1. Imports, exact scope and claims

For epsilon->0 let V_J be the original all-law full-D squared-Euclidean infimum, and V_L the original all-law full-D first-l1-norm infimum. This note CONDITIONS on the named current parent v253 composition, `privacy-v253-MDA-mixed-cost-composition-entire-parent-v1.md`, SHA-256 `a32085f921269874b24821146d7af820451ac48b844288887805c75042e7e71d`, only for its small-epsilon identification of the original J optimizer with the centered squared-l1 staircase. It also imports the parent MDA matching-norm theorem `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`, for the actual L optimum, and the UNREVIEWED local selector expansions in `frontier-20261028-high-privacy-selector-tradeoff-v1.md`, SHA-256 `aa45831697246a418364e72eedc4345e11afb1a988076ac730a204c8fd9617b7`.

At exactly those scopes the written claims are

    V_J(epsilon)=4/epsilon^2 - (sqrt(3)/54)epsilon
                   +epsilon^2/360 + O(epsilon^4),                         (1)
    V_L(epsilon)=2/epsilon - (sqrt(3)/108)epsilon^2
                   +epsilon^3/540 + O(epsilon^4).                         (2)

In particular the J constant and epsilon^3 coefficients are BOTH zero. These are asymptotic coefficients, not an unqualified source-equivalence claim or a new independent proof of v253/MDA. The source-independent nearopt theorem 8615 gives only the leading values; it is not needed for the expansions.

For the corresponding all-law minimal epsilon under budgets `J<=j` and `L<=ell`, inversion of (1)–(2) gives, on the same imported local branch,

    epsilon_J(j)=2 j^(-1/2) - (sqrt(3)/27)j^(-2)
                    +(1/90)j^(-5/2)+O(j^(-7/2)),      j->infinity,       (3)
    epsilon_L(ell)=2/ell - (2sqrt(3)/27)ell^(-4)
                    +(4/135)ell^(-5)+O(ell^(-6)),     ell->infinity.     (4)

The sharper error exponent in (3) uses the zero epsilon^3 coefficient in (1). These are separate single-budget inversions, not a joint-budget claim.

## 2. Exact staircase formulas and selected roots

Put `m=1/(e^epsilon-1)`, `q=1/m=e^epsilon-1`, and

    D=gamma^2+2m gamma+m+2m^2,
    M3=gamma^3+3m gamma^2+3(m+2m^2)gamma+m+6m^2+6m^3,
    M4=gamma^4+4m gamma^3+6(m+2m^2)gamma^2
        +4(m+6m^2+6m^3)gamma+m+14m^2+36m^3+24m^4.

For the actual centered diamond staircase,

    L_gamma=(2/3)M3/D,          J_gamma=M4/(3D).                         (5)

The imported work selects the squared-cost and mean-cost roots, respectively,

    gamma_J=g-q/12+O(q^2),  gamma_L=g-q/9+O(q^2),
    g=(3+sqrt(3))/6,  g^2=g-1/6.                                         (6)

The g1 coefficients differ; no assumption that the source selector equals the original Euclidean selector is made.

## 3. Squared-Euclidean coefficients and cubic cancellation

Polynomial division of (5) gives the uniform-in-gamma expansion, for gamma in a fixed neighborhood of g,

    J_gamma=4m^2+4m+1/3 + [A(gamma)/3]q+[B(gamma)/3]q^2
             +[C(gamma)/3]q^3+O(q^4),                                   (7)
    A=gamma-3gamma^2+2gamma^3,
    B=(-gamma+4gamma^3-3gamma^4)/2,
    C=-[B(1+2gamma)+A gamma^2]/2.

At g, let r=sqrt(3). Exact algebra gives

    A(g)=-r/18,  A'(g)=0, A''(g)=2r,
    B(g)=(2r-3)/72, B'(g)=r/6, C(g)=(18-5r)/432.                       (8)

Use gamma_J=g-q/12+O(q^2) and `q=epsilon+epsilon^2/2+epsilon^3/6+O(epsilon^4)`. Also

    4m^2+4m+1/3=4/epsilon^2+epsilon^2/60+O(epsilon^4).                  (9)

The epsilon coefficient is A(g)/3=-r/54; the epsilon^2 coefficient is `1/60+A(g)/6+B(g)/3=1/360`. The epsilon^3 coefficient is

    A(g)/18+B(g)/3
      +[C(g)-B'(g)/12+A''(g)/288]/3 =0.                                 (10)

A'(g)=0 eliminates the unknown q^2 coefficient of gamma_J, so the stated O(epsilon^4) requires no stronger selector expansion than (6). This proves (1) conditional on the v253 identification.

## 4. First-norm coefficients

A separate division of (5) gives

    L_gamma=2m+1-q/6+(2/3)R3(gamma)q^2+(2/3)R4(gamma)q^3+O(q^4),      (11)
    R3=gamma^3/2-3gamma^2/4+gamma/4+1/8,
    R4=-[R3(1+2gamma)-gamma^2/4]/2.

At g,

    R3(g)=(9-r)/72, R3'(g)=0, R4(g)=(-11+2r)/144.

Use `2m+1=coth(epsilon/2)=2/epsilon+epsilon/6-epsilon^3/360+O(epsilon^5)` and (6). Again the selector's first displacement drops out at the displayed orders. The epsilon term cancels, the epsilon^2 coefficient is `-1/12+(2/3)R3(g)=-r/108`, and the epsilon^3 coefficient is

    -1/360-1/36+(2/3)[R3(g)+R4(g)]=1/540.                              (12)

This gives (2) conditional on the actual MDA first-norm optimizer.

## 5. Inversion and exact checks

The imported exact scalar equations and simple-root branches make the small-epsilon value functions continuous and strictly decreasing locally; the displayed leading derivatives are `-8/epsilon^3` and `-2/epsilon^2`. Hence their actual budget infima invert the branches. Substitution `epsilon=2j^(-1/2)+a j^(-2)+b j^(-5/2)+...` in (1) gives `a=-sqrt(3)/27`, `b=1/90` and no j^-3 term; similarly substituting `epsilon=2/ell+a ell^(-4)+b ell^(-5)+...` in (2) gives `a=-2sqrt(3)/27`, `b=4/135`. This proves (3)–(4) at the named conditional scope.

In the Python eval kernel, exact `fractions.Fraction` pairs `(a,b)` representing `a+b sqrt(3)` checked A(g), B(g), C(g), both J coefficients 1/360 and 0, and L coefficients `-sqrt(3)/108` and 1/540. It did NOT check global optimization or convergence. Separate 70–80 digit Decimal diagnostics at epsilon 0.1, 0.05, 0.02, 0.01 used the APPROXIMATE selector `g-epsilon/12` or `g-epsilon/9`; their residual trends were consistent with (1)–(2), but are not interval certificates or actual optimizer evaluations.

The four displayed formulae are written results conditional on the pinned parent/author inputs; no formal proof, independent review, novelty, priority or parent adoption is claimed. Review should reconstruct the exact polynomial division, O-term uniformity, cubic cancellation and inversion.
