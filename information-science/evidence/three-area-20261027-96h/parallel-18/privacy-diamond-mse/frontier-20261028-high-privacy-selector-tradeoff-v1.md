# High-privacy source-selector tradeoff and Laplace scaling

**AUTHOR CANDIDATE — WRITTEN with exact rational selected-parameter checks; NOT independently reviewed or parent-adopted.** Native pre-write clock `Wed Oct 28 18:17:50 PDT 2026`.

## 1. Actual model and new asymptotic claims

Fix finite epsilon>0, `b=e^(-epsilon)`, `m=b/(1-b)`, and the FULL CLOSED l1 unit diamond D. F_epsilon is the entire class of Borel laws satisfying the additive event inequality for EVERY Borel set and EVERY h in D. Choose the actual globally first-l1-moment-optimal staircase `mu_1=Q_gamma1` and actual globally squared-l1-optimal staircase `mu_2=Q_gamma2`, whose scalar selectors satisfy gamma1<gamma2 at the named input scope below.

As epsilon decreases to 0 (a limit, not an epsilon=0 privacy law), let `g=(3+sqrt(3))/6`. The new candidate results are

    gamma1 = g - epsilon/9 + O(epsilon^2),
    gamma2 = g - epsilon/12 + O(epsilon^2),
    gamma2-gamma1 = epsilon/36 + O(epsilon^2),                           (1)
    TV(mu_1,mu_2) = epsilon^2/36 + O(epsilon^3),                         (2)
    D_infinity(mu_1||mu_2) = epsilon^2/36 + O(epsilon^3),
    D_infinity(mu_2||mu_1) = epsilon - epsilon^2/36 + O(epsilon^3).      (3)

Thus the same source-optimal and squared-cost-optimal laws are close in TV at high privacy, with an asymmetric max-likelihood-ratio profile; this does not negate their strict finite-epsilon difference. At low privacy their TV instead tends to one at the separately recorded rate.

Let L(mu)=E||X||_1 and J(mu)=E||X||_2^2. Their opposite loss penalties obey

    J(mu_1)-J(mu_2) = (sqrt(3)/3888)epsilon^3 + O(epsilon^4),            (4)
    L(mu_2)-L(mu_1) = (sqrt(3)/7776)epsilon^4 + O(epsilon^5).           (5)

On the named v253/v241 diamond regime, including all sufficiently small epsilon, `mu_2` is the unique ORIGINAL all-law Euclidean optimizer. Thus (4) gives the actual Euclidean source-selector excess `J(mu_1)-V` in that regime. This last identification is an explicit separate import; the first-moment PMLR theorem alone does not establish it.

Finally, for ANY family of offsets gamma(epsilon) in [0,1], the rescaled staircase law `Law(epsilon X_gamma)` converges to the unit-scale product Laplace density `(1/4) exp(-||y||_1)` with likelihood ratio converging uniformly to 1, not merely weakly. This applies to both mean and squared selectors and, on the diamond side, to the original Euclidean optimizer. No uniform-in-epsilon density statement at fixed unscaled x is implied.

## 2. Exact input boundaries

The named global existence import is the parent-WRITTEN_SUPPORTED alternative matching-norm per-cost theorem `privacy-MDA26-entire-norm-cost-and-weighted-decay-parent-v1.md`, SHA `75614a6fc5cb66d9b26f13e64e58935fe6ea52121948e7a56592b91611576ac3`. My own UNREVIEWED `frontier-20261028-universal-pmlr-selector-separation-v1.md`, SHA `4c92d56867a959298836063d0045634cd61a0efb8f3175fcb701c4ac4a722fc6`, establishes scalar-root uniqueness and gamma1<gamma2; I rederive the needed local expansions below. Neither is presented as a repair of a printed source proof.

The original-Euclidean-optimum identification in the last sentence of §1 additionally imports parent v253 `privacy-v253-MDA-mixed-cost-composition-entire-parent-v1.md`, SHA `a32085f921269874b24821146d7af820451ac48b844288887805c75042e7e71d`, with its LAW642/MDA/NORM148/separated-v241 union. It states equality `V=(2/3)W` and the unique Euclidean law equals the radial squared-l1 minimizer for epsilon<=epsilon_t, with epsilon_t>0. No direct PMLR-to-Euclidean attribution or novelty/priority claim is made.

## 3. Two globally selected scalar roots

For 0<=gamma<=1 write

    D(gamma)=gamma^2+2m gamma+m+2m^2,
    M3(gamma)=gamma^3+3m gamma^2+3(m+2m^2)gamma+m+6m^2+6m^3,
    M4(gamma)=gamma^4+4m gamma^3+6(m+2m^2)gamma^2
                +4(m+6m^2+6m^3)gamma+m+14m^2+36m^3+24m^4.

Exact layer integration gives `L=(2/3)M3/D`, `W=E||X||_1^2=M4/(2D)`, and `J=(2/3)W` for centered D-radial staircases. Their derivative signs are the quartic Q_m and quintic P_m in the named universal-selector candidate.

For m->infinity, divide the mean derivative polynomial by m^2:

    Q_m(gamma)/m^2 = 6gamma^2-6gamma+1
                      + (4gamma^3-2gamma)/m + gamma^4/m^2.              (6)

Its selected larger root tends to `g=(3+sqrt(3))/6`, the unique root of the leading quadratic above 1/2. At g, `g^2=g-1/6` and `4g^3-2g=(2/3)(2g-1)`, while the leading derivative is `6(2g-1)`. The implicit function theorem therefore gives gamma1=g−1/(9m)+O(m^-2).

For the squared-l1 selector the corresponding expansion is

    P_m(gamma)/m^3 = 12gamma^2-12gamma+2
                      +(12gamma^3-8gamma+1)/m+O(m^-2).

Its selected root tends to the same g; using `12g^3-8g+1=2g-1` and derivative `12(2g-1)` gives gamma2=g−1/(12m)+O(m^-2). Because `1/m=e^epsilon−1=epsilon+O(epsilon^2)`, these are (1). This is not a numerical root-branch selection; the preceding all-variable proof has already identified the larger roots as the unique scalar minima.

## 4. Exact TV and max-divergence formulas

For `0<gamma1<gamma2<1`, the two densities have the same geometric level except in the disjoint radial bands `(gamma1+k,gamma2+k)`. On a band, q_2/q_1=`Z1/(bZ2)>1`; off the bands it is `Z1/Z2<1`, because `Z_i=2D_i`, `D2>D1>bD2`. Integrating the positive density difference exactly gives

    TV(mu_1,mu_2)
      = [(gamma2-gamma1)(gamma1+gamma2+2m)/(1-b)] [1/D2-b/D1].        (7)

This is derived here from the actual density ratios and diamond area 2r^2; it does not assume any TV inequality or previous unreviewed TV-formula input.

The SAME two constant ratios give exact max-divergences

    D_infinity(mu_1||mu_2)=log(D2/D1),
    D_infinity(mu_2||mu_1)=epsilon-log(D2/D1).                           (8)

Using `gamma2-gamma1=1/(36m)+O(m^-2)`, `1-b=1/(1+m)`, and `D_i=2m^2+O(m)`,

    1/D2-b/D1 = 1/(2m^3)+O(m^-4),
    [(gamma2-gamma1)(gamma1+gamma2+2m)/(1-b)] = m/18+O(1),
    log(D2/D1)=1/(36m^2)+O(m^-3).

Substituting 1/m=epsilon+O(epsilon^2) proves (2)–(3). All relative densities are strictly positive; the max divergences are finite for every epsilon>0 even though they are asymmetric.

## 5. Opposite-cost penalties and the ORIGINAL Euclidean import

At gamma2, W'=0. Uniform differentiation of the exact formula on gamma in [0,1] gives

    W''(gamma2)=sqrt(3)/m+O(m^-2),       W'''=O(m^-1).

At gamma1, L'=0 and similarly

    L''(gamma1)=sqrt(3)/(3m^2)+O(m^-3),  L'''=O(m^-2).

Taylor's theorem over the ACTUAL interval [gamma1,gamma2], length `1/(36m)+O(m^-2)`, gives

    W(gamma1)-W(gamma2)=sqrt(3)/(2592m^3)+O(m^-4),
    L(gamma2)-L(gamma1)=sqrt(3)/(7776m^4)+O(m^-5).

Multiplying the first difference by the valid centered-radial angular factor 2/3 and replacing 1/m by epsilon+O(epsilon^2) yields (4)–(5). The source mean law is globally optimal for L by the named matching-norm theorem; Q_gamma2 is globally optimal for W by the same theorem. Without further imports these are comparisons of actual laws, not an assertion Q_gamma2 is all-law J-optimal.

The separately parent-supported v253/v241 union says the all-law J optimum is precisely this unique centered squared-l1 minimizing staircase whenever epsilon<=epsilon_t, and epsilon_t>0. Therefore (4) is indeed `J(mu_1)-V` for all sufficiently small positive epsilon, at that explicit union. It is not a circular external-publication proof of the original optimizer.

## 6. Uniform relative convergence to the unit product Laplace law

For ANY gamma in [0,1], the staircase index `n_gamma(r)=min{k>=0:r<=gamma+k}` satisfies `|n_gamma(r)-r|<=1` for all r>=0. The density of Y=epsilon X_gamma is

    f_(epsilon,gamma)(y) = [epsilon^2 Z_gamma]^(-1)
                            exp[-epsilon n_gamma(||y||_1/epsilon)],
    Z_gamma=2D(gamma).

For the unit product Laplace density `f0(y)=(1/4)exp(-||y||_1)`, this gives FOR ALL y

    e^(-epsilon) 4/(epsilon^2 Z_gamma)
        <= f_(epsilon,gamma)(y)/f0(y)
        <= e^(epsilon) 4/(epsilon^2 Z_gamma).                            (9)

The elementary expansion `m=1/epsilon+O(1)` implies `epsilon^2 Z_gamma/4=1+O(epsilon)` uniformly for gamma in [0,1]. Therefore the likelihood ratio in (9) converges uniformly to 1, for ANY choice of gamma(epsilon). In particular all such scaled laws converge to f0 in total variation, and both directed D_infinity divergences to f0 vanish. This directly pays the complete density normalization and the rescaling; it is not an appeal to a limiting sampler or fitted grid.

## 7. Actual exact sample checks and limitations

A bounded local Fraction computation used m=1000 and exact bisection brackets around the two larger scalar roots. It observed:

```text
m=1000: mean and squared offset intervals disjoint: True
m*(gamma2-gamma1) interval within (1/40,1/30): True
m^2*TV interval within (1/40,1/30): True
exact first-order root-gap coefficient= 1/36
m=1000, exact root-bracket midpoints: scaled m^3 W-gap in (1/1600,1/1400): True
scaled m^3 Euclidean-gap in (1/2400,1/2100): True
m=1000, root-bracket midpoints: scaled m^4 mean-gap in (1/5000,1/4000): True
scaled mean-gap positive: True
```

The first three are interval bounds; the last four evaluate rational MIDPOINTS of the root brackets and are only diagnostics, not certified endpoint bounds. The asymptotic root selection, Taylor remainders, TV and cost coefficients are the written analysis above, conditional on the named model-specific input. No floating fit or selected original Euclidean optimum was used.

No f68 near-optimal TV-stability theorem is imported in this note: (2) is a DIRECT density identity for two exact staircase laws and v253 is used only for the separate original-Euclidean identification. Request disjoint review of both implicit-function expansions, Taylor orders, the exact likelihood-ratio bands and the global-optimizer import. No formal/kernel/human/configured-family/novelty or parent acceptance is claimed.
