# Exact rational certificate for the original target at epsilon=ln 2

**AUTHOR CANDIDATE — WRITTEN plus exact Fraction interval arithmetic; NOT independently reviewed or parent-adopted.** Native pre-write observation: `Wed Oct 28 20:05:07 PDT 2026`.

## 1. Conditional original-model claim

For the original ALL-event, full closed l1-unit-diamond private problem, set epsilon=ln 2, so b=1/2 and m=b/(1-b)=1. The exact original squared-Euclidean optimum and its original full-law optimizer are the named conclusions of parent v253 `privacy-v253-MDA-mixed-cost-composition-entire-parent-v1.md`, SHA-256 `a32085f921269874b24821146d7af820451ac48b844288887805c75042e7e71d`, combined with parent v241 `privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md`, SHA-256 `48274df7a84b16cd8ead4a0b9069b8359110e1b216bc72e6baea1de03e626138`. The first-norm source selector uses the separate parent MDA per-cost theorem `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA-256 `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`.

Conditional on these named same-harness written parent results, the original target optimizer is the actual centered diamond staircase with the LARGER positive root gamma_J of

    P(x)=x^5+5x^4+14x^3+10x^2-21x+3.                                  (1)

Its true original all-law squared-Euclidean value V_J satisfies the EXACT RATIONAL bounds

    83046064347025039043 / 10^19 < V_J < 83046064347025039044 / 10^19. (2)

These are not floating-confidence intervals: the checks in §4 use exact fractions. The optimizer's offset satisfies

    7271025149432606453616 / 10^22 < gamma_J
       < 7271025149432606453617 / 10^22.                                 (3)

The first-norm global source optimizer is a different actual staircase, at the larger positive root gamma_L of

    Q(x)=x^4+4x^3+6x^2-8x+1.                                             (4)

Its exact root bracket is

    7061732346792597254817 / 10^22 < gamma_L
       < 7061732346792597254818 / 10^22.                                 (5)

For these two ACTUAL full-D laws, the exact interval arithmetic further proves

    J(gamma_L)-J(gamma_J)>1/10000,
    L(gamma_J)-L(gamma_L)>1/100000.                                      (6)

The named MDA input supports gamma_L as the global L minimizer; v253/v241 support gamma_J as the original global J minimizer. Equations (2)–(6) do not claim the first-norm source theorem itself asserts the squared-Euclidean optimum, and do not claim priority, novelty or independent review.

## 2. Branch qualification and root identification

At epsilon=ln 2, `s=sinh^2(epsilon/2)=1/8`. The v241 unique threshold root s_t of `2s^3-9s^2-108s-81=0` exceeds 1 because the polynomial is negative at 1 and its unique positive root is s_t. Hence 1/8<s_t and the named parent result puts the target on the diamond side. This is a use of the explicitly named parent theorem, not an independently proven branch theorem.

The exact centered-staircase moment functions at m=1 are

    D(x)=x^2+2x+3,
    N4(x)=x^4+4x^3+18x^2+52x+75,
    N3(x)=x^3+3x^2+9x+13,
    J(x)=N4(x)/(3D(x)),  L(x)=2N3(x)/(3D(x)).                         (7)

Direct differentiation gives `J'(x)=2P(x)/(3D(x)^2)` and `L'(x)=2Q(x)/(3D(x)^2)`. P has at most two positive roots by Descartes' sign rule; `P(0)>0`, `P(18/25)=-1692807/9765625<0`, and `P(3/4)=615/1024>0`. Thus its unique larger positive root lies in (18/25,3/4), and is the scalar J minimum because the normalized endpoint staircases agree. The same argument applies to Q using `Q(0)>0`, `Q(7/10)=-479/10000<0`, and `Q(71/100)=3036081/100000000>0`. This identifies both roots without importing an unreviewed author selector theorem.

## 3. Rational interval method

Let the gamma_J and gamma_L lower and upper endpoints in (3) and (5) be a_J,b_J and a_L,b_L. Their exact polynomial signs are `P(a_J)<0<P(b_J)` and `Q(a_L)<0<Q(b_L)`. The coefficients of D,N3,N4 are nonnegative, so every x in [a,b] satisfies

    N4(a)/(3D(b)) <=J(x)<=N4(b)/(3D(a)),
    2N3(a)/(3D(b)) <=L(x)<=2N3(b)/(3D(a)).                              (8)

All roots and objective claims use these outward RATIONAL bounds. The narrow denominator cross-comparison is deliberate; no assumption of monotonicity of J or L across their stationary point is needed. For the two differences in (6), subtract the appropriate upper endpoint for the smaller value from the lower endpoint for the larger one. The results exceed the two displayed rational margins.

## 4. Actual exact checks and scope

The Python eval kernel used `fractions.Fraction` for P,Q,D,N3,N4, exact-sign bisection and the four rational root endpoints. It checked both sign changes, the two 19-decimal original-J bounds in (2), and the exact comparisons `J_L_lower-J_J_upper>1/10000`, `L_J_lower-L_L_upper>1/100000`. It also checked P(18/25), P(3/4), Q(7/10), Q(71/100) as printed. Decimal renderings (not the proof) give gamma_J≈0.72710251494326064536, gamma_L≈0.70617323467925972548, J gap≈0.00014387991528 and L gap≈0.00004816580706.

The exact arithmetic checks do not verify the parent v253/v241/MDA theorems or formalize their scope. This is WRITTEN plus Fractions, conditional on the named original-model parent inputs; no external source equivalence, novelty, priority, cross-model or independent review, or parent adoption of this new certificate is claimed.
