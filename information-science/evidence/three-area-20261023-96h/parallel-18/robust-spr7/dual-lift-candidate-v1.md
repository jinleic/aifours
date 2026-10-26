# Candidate v1: an exact correlation-preserving dual Routh lift

Observed before creation: **2026-10-23T14:16:13-0700**. Author: InfoSPR7, info-2. Status: **CANDIDATE**, complete written argument only; independent reconstruction and priority review not performed. No executable scientific check. This is another ingredient for the same universal degree-seven problem, not a second active problem or solved-problem count.

## Statement

Let `K` be a compact robustly Hurwitz family of monic real degree-seven polynomials, not necessarily an independent coefficient box. Assume its coefficient `[s^6]a=c>0` is **fixed across the family**. Write `a(s)=E_a(-s^2)+s O_a(-s^2)` and let

`q_a(s)=(E_a(-s^2)+s[O_a(-s^2)-E_a(-s^2)/c])/c`.

As proved by the explicit Hermite–Biehler argument in §1 of `routh-obstruction-candidate-v1.md`, each `q_a` is a monic Hurwitz sextic. Keep its actual coefficient correlations.

Suppose a polynomial `beta(s)=F(-s^2)+s G(-s^2)` of exact degree six is supplied with a correct common strict-SPR proof for **every actual** `q_a`. The proof may be direct or imported at a stated trust boundary; the current unauthenticated sextic Lean announcement is not an import here. Then an explicit real polynomial of exact degree seven, common to all `a in K`, is

`b_epsilon(s)=F(-s^2)+(s+s^2/c)G(-s^2)+epsilon s^7`,           (1)

with the positive `epsilon` defined below. This gives a genuine numerator lift, not a feasibility encoding or a claim that a stable interval hull exists.

## Exact identity

First omit the `epsilon s^7` term and call the result `b_0`. Since `deg F<=3`, `deg G<=2`, its degree is at most six, and

`E_{b_0}(t)=F(t)-tG(t)/c`, `O_{b_0}(t)=G(t)`.

Direct multiplication gives, symbolically for every member and every `t`,

`P_{a,b_0}(t)`

` =(F-tG/c)E_a+tG O_a`

` =F E_a+tG(O_a-E_a/c)`

` =c P_{q_a,beta}(t)`.                                       (2)

This identity preserves the actual family. No independent interval hull or inference from point tests appears.

## Quantitative strictness and degree raising

The leading coefficient of `beta` is positive, since the monic sextic denominators and strict positive realness force a positive leading ratio. Compactify `t` by `x=t/(1+t)`. The function

`P_{q_a,beta}(t)/(1+t)^6`

extends continuously to `x=1` with that positive leading coefficient. The image family is compact. It is strictly positive at every finite `t` by hypothesis and at infinity by the leading coefficient. Thus the well-defined number

`mu=min_{a in K, 0<=x<=1} [(1-x)^6 P_{q_a,beta}(x/(1-x))]`     (3)

is positive, with the endpoint value interpreted continuously. In an actual application `mu` may instead be replaced by any supplied certified positive lower bound; no numerical optimization is required by this argument.

Use descending septic coefficient notation `a=s^7+c s^6+a_2 s^5+...+a_6 s+a_7`. Every coefficient of a monic Hurwitz polynomial is positive. Let

`U_2=max_{a in K}a_2`, `U_6=max_{a in K}a_6`,

`epsilon=c mu/[2(1+U_2+U_6)]>0`.                             (4)

The pairing with the degree-seven monomial is exactly

`P_{a,s^7}(t)=-t^4 O_a(t)`

` =t^7-a_2 t^6+a_4 t^5-a_6 t^4`

` >=-(U_2+U_6)(1+t)^6` for `t>=0`.                           (5)

Combining (2)–(5) proves

`P_{a,b_epsilon}(t)`

` >=[c mu-epsilon(U_2+U_6)](1+t)^6`

` >(c mu/2)(1+t)^6>0`.                                       (6)

The new polynomial has exact degree seven because `b_0` has degree at most six and the added leading coefficient is `epsilon>0`. It is fixed across the family and independent of frequency. Thus it meets the book's equal-degree and strict finite-frequency requirements, including `t=0`. At infinite frequency the leading ratio is the same positive `epsilon`; the finite-frequency problem has not been replaced by a nonstrict closure.

## Original-target gap and use with the obstruction candidate

This lemma closes the **numerator-lifting** step whenever a common strict sextic numerator for the true correlated image is actually supplied and `[s^6]a` is fixed. It does not supply that numerator. The image need not have an independent coefficient-box description, and its smallest such hull need not be stable: the exact obstruction candidate gives an explicit continuum of countercontrols.

Two missing obligations remain for universal degree-seven synthesis:

1. A common numerator for arbitrary true Routh images, without replacing them by an unjustifiably stable interval hull.
2. A family-independent lift when `[s^6]a` varies. Formula (2) uses the same `c` in the numerator for every denominator; substituting each member's own `c` would violate the common-numerator quantifier.

Consequently this is a scoped analytical ingredient only, not a universal theorem and not an independent discovery claim. Priority in the classical SPR/Routh-transform literature has not been cleared. The compactification and degree-raising mechanisms are standard; the load-bearing item to reconstruct is the exact dual-shear identity (2) and its dependence on the fixed coefficient.
