# Inverting the original all-law privacy/accuracy frontier

**AUTHOR CANDIDATE — WRITTEN with a bounded Decimal coefficient diagnostic; NOT independently reviewed or parent-adopted.** Native pre-write clock: `Wed Oct 28 19:04:55 PDT 2026`.

## 1. Exact inverse problems and source-independent leading terms

Let F_epsilon be ALL Borel additive-noise laws on R^2 satisfying epsilon privacy for EVERY Borel event and EVERY shift in the FULL CLOSED unit l1 diamond. Define, for positive accuracy budgets C,A,

    E_J(C)=inf{epsilon>0: exists mu in F_epsilon with E|X|_2^2<=C},
    E_L(A)=inf{epsilon>0: exists mu in F_epsilon with E||X||_1<=A}.

These are different objectives and different budget units; neither is an inference from PMLR's first-power theorem to the registered Euclidean squared cost.

At the two explicitly named, still-UNREVIEWED source-independent peak-floor candidates in §2, the inverse statements as C,A->0+ are

    E_J(C)=2 log(1/C)+log[4/(3pi)]+O(sqrt(C)),                           (1)
    E_L(A)=3 log(1/A)+log 2+O(A).                                        (2)

The second result is a direct first-moment inverse, not a squared-cost formula with a renamed budget. Both quantify ALL original Borel laws, not just a staircase class.

Moreover, for every `0<C<1/3`, EVERY such feasible law with squared cost at most C obeys the explicit nonasymptotic necessary bound

    epsilon >= log[4(1-3C)/(3pi C^2)].                                    (3)

This is meaningful even when the logarithm is negative, although only small C is used for (1).

## 2. Named candidate inputs and assurance

For (1)–(3) and (2), the ONLY nonstandard inputs are my own still-UNREVIEWED source-independent all-law proofs:

- `frontier-20261028-peak-floor-low-privacy-universal-v1.md`, SHA `d44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43`: `V(b)=c0 sqrt b+O(b^(3/4))`, `c0=2/sqrt(3pi)`, an actual full-D upper law, and its explicit all-b lower bound.
- `frontier-20261028-peak-floor-first-norm-universal-v1.md`, SHA `fa39d7bdc125da7c8f7424d5976309227d8101a58b15efea919e8eb8376f04ea`: `L_*(b)=2^(1/3)b^(1/3)+O(b^(2/3))`, explicit all-law lower bound and an actual shell upper law.

Neither predecessor imports LAW642, MDA, v241, PMLR, f68, or a historical held result. Their hashes do NOT mean they have been reviewed. The conditional refinement in §6 has additional explicitly UNREVIEWED inputs and is not needed for the source-independent leading terms.

## 3. A direct nonasymptotic Euclidean inverse bound

The Euclidean peak-floor lower bound states that any original law of actual cost J satisfies

    J >= sqrt[4b/(3pi)+4b^2/pi^2]-2b/pi.                                 (4)

Both sides allow the following squaring: `J+2b/pi>0`. Rearranging gives

    J^2 >= (4b/pi)(1/3-J).

When `0<J<=C<1/3`, the right factor is positive, and the function `3pi J^2/[4(1-3J)]` is increasing. Consequently

    b <= 3pi C^2/[4(1-3C)],

which is exactly (3) after `epsilon=-log b`. A zero-cost law is impossible under full-shift privacy; no division by a zero cost is needed.

## 4. Why inverse near-zero budgets really have b->0

The universal density bound is `p<=1/(2b)` a.e. The l1 ball rD has area 2r^2, so `mu(rD)<=r^2/b`. Put `r=sqrt(b)/2`; then at least 3/4 of the mass lies outside rD. Since `||x||_2^2>=||x||_1^2/2`,

    E||X||_1 >= 3sqrt(b)/8,        E|X|_2^2 >= 3b/32.                  (5)

Thus any sequence whose first or squared budget tends to 0 has b->0, independently of a conjectured optimizer or an asymptotic-inversion circularity.

## 5. Source-independent inversion of the leading bounds

Let `c0=2/sqrt(3pi)`. The lower bound (3) gives

    E_J(C) >= 2log(1/C)+log[4/(3pi)]+log(1-3C).

For the reverse direction, the actual disk-shell upper law has cost `c0 sqrt b+O(b^(3/4))`. Choose b=`(C/c0)^2[1-K sqrt C]` for a sufficiently large constant K and C small. Its cost is <C, so it is an actual feasible witness at epsilon=-log b. This gives the matching upper `2log(1/C)+log[4/(3pi)]+O(sqrt C)`, proving (1). There is no assertion that the exact inverse infimum is attained.

For first norm, write t=b^(1/3), d0=2^(1/3). Its all-law lower and actual shell upper are `d0 t-2t^2 <= L_* <= d0 t+O(t^2)`. By §4 any admissible small-A sequence has t->0. Solving the inequalities by elementary one-sided comparison gives `t<=A/d0+O(A^2)` necessarily. Conversely choose `t=A/d0-K A^2` with K large; the actual shell upper law has mean <A. Taking `-3log t` on the two sides yields

    E_L(A)=3log(1/A)+3log d0+O(A)
          =3log(1/A)+log 2+O(A),

which is (2). This is a bracketing argument using explicit inequalities, not an assumption of continuity, uniqueness or exact minimizer existence.

## 6. Sharper inverse Euclidean terms — explicitly conditional

The following additional candidate requires BOTH unreviewed original-value packets, beyond the source-independent leading terms:

- `frontier-20261028-euclidean-second-term-and-disk-law-v1.md`, SHA `188cd3ff1648e9f46ac00fdc1d0068272715559143fe9ec5643a7af03740b4d4`;
- `frontier-20261028-euclidean-fractional-third-term-v1.md`, SHA `4efc24ca86ef336292f27d7130c456ff35fc84022ab05fd33a0c72f5815a50c6`.

Those import the separately parent-WRITTEN_SUPPORTED LAW642 original optimum/core and the first disk-limit predecessor, and remain UNREVIEWED. At their exact scope they give, with t=b^(1/4), R=(4/(3pi))^(1/4),

    V(b)=c0 t^2+c1 t^3-c2 t^(11/3)+o(t^(11/3)),
    c0=R^2,  c1=8sqrt(2)/(3pi R),
    c2=8sqrt(2)/(5pi R^3 4^(2/3)).                                      (6)

Conditional on those inputs, the inverse expansion is

    E_J(C)=2log(1/C)+log[4/(3pi)] +4sqrt(2C)
            - [3^(5/3)pi^(2/3)/(5*2^(1/6))] C^(5/6)
            +o(C^(5/6)).                                                 (7)

This is a prospectively derived conditional inverse, not an independent review of (6).

### Direct bracketing proof, no assumed inverse differentiability

Put `r=sqrt(C/c0)` and consider the two small-positive t values

    t_±=r -[c1/(2c0)]r^2 + [c2/(2c0) ± eta]r^(8/3),   eta>0 fixed.

Substitution in (6) gives `V(t_±^4)-C=±2c0 eta r^(11/3)+o(r^(11/3))`. For small C, at t_- the infimum is strictly below C, so an actual feasible law of cost <C exists; at t_+ it is strictly above C, so none exists. The privacy classes are nested in epsilon, so `-4log(t_+)<=E_J(C)<=-4log(t_-)`. Expanding the logarithms, then sending eta->0, proves (7) without assuming a differentiable or attained inverse.

The square-root coefficient simplifies using `c0=R^2`, `R^4=4/(3pi)`:

    2c1/c0^(3/2)=4sqrt(2).

The fractional coefficient is `2c2/c0^(11/6)`, equal to the coefficient displayed in (7). No O(C) term is silently mixed into the larger C^(5/6) term.

## 7. Actual bounded coefficient diagnostic and limits

A 70-digit Decimal calculation independently evaluated the two equivalent coefficient expressions:

```text
inverse sqrt coefficient formula= 5.656854249492380 target 4sqrt2= 5.656854249492380
inverse fractional coefficient formula= 2.385029029153412 simplified= 2.385029029153412
coefficient identity relative error <1e-60: True
```

These decimals are a diagnostic, not interval proof; the algebraic coefficient identities and bracketing are the written argument. The parent-independent leading bounds still depend on the TWO unreviewed peak-floor candidates, and the refined term additionally depends on BOTH unreviewed original rounded-core candidates. Request disjoint review of the monotone inverse brackets, strict inequalities, budget variables and coefficient powers. No source-priority, novelty, formal/kernel/human/configured-family or parent-adoption claim is made; historical held results are not premises.
