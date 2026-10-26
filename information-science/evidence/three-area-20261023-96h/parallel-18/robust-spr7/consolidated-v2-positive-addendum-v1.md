# Positive conditional appendix to SPR7 consolidated v2: a cubic-comparator residue budget

Observed before creation: **2026-10-23T14:49:35-0700**. InfoSPR7, info-2. This is the positive-side continuation requested by the parent, attached to `consolidated-v2.md` SHA256 **`5d5f8d3708ff3368143289edc8866238603d8ea0c0db33b17eddb854f8fc3c18`**. It is **not another ansatz obstruction, problem slot or solved-problem count**. Status: complete **CANDIDATE written proof**, not independently reconstructed. No scientific executable, arithmetic interpreter, solver, enumeration or compilation ran.

## 0. What this adds and does not add

The dual lift in consolidated §5 explains what a certified common sextic numerator buys when the septic second coefficient is fixed. The following direct positive certificate does **not require that coefficient to be fixed**. It uses one specified monic cubic comparator, explicit coefficient/root bounds and one closed-form scalar choice. It produces an actual common **monic degree-seven** numerator and a quantitative whole-frequency pairing margin. It is an analytic sufficient theorem, not an LP/SOS encoding of eight unknown numerator coefficients.

The unresolved universal obligation is not hidden: robust stability gives the comparator interlacing/positive-residue hypotheses, but has **not** been shown to imply the displayed scalar budget. Failure of this sufficient budget is **UNKNOWN for synthesis**, not a counterexample or an obstruction to unrestricted numerators. No necessity, optimality or novelty is claimed.

## 1. Box data and the specified comparator

Let

`K={s^7+a_1s^6+a_2s^5+a_3s^4+a_4s^3+a_5s^2+a_6s+a_7 : l_i<=a_i<=u_i}`,

with finite strictly positive endpoints `0<l_i<=u_i`. Degenerate intervals are allowed. The positivity of endpoints is automatic for a compact robustly Hurwitz monic box, but stability is not initially assumed for the sufficient certificate below.

The components are

`E_a(t)=-a_1t^3+a_3t^2-a_5t+a_7`,

`O_a(t)=-t^3+a_2t^2-a_4t+a_6`.

Choose the **midpoint odd component**, not a midpoint numerator:

`Q(t)=-t^3+q_2t^2-q_1t+q_0`,

`q_2=(l_2+u_2)/2`, `q_1=(l_4+u_4)/2`, `q_0=(l_6+u_6)/2`.

Require that `Q` have three distinct positive roots `r_1<r_2<r_3`. For every even component in the box, require positive residues

`A_j(a)=E_a(r_j)/Q'(r_j)>0`.

These hypotheses can be stated entirely from the even coefficient intervals. Define

`E_-(r)=l_7-u_5r+l_3r^2-u_1r^3`,

`E_+(r)=u_7-l_5r+u_3r^2-l_1r^3`,

`A_j^- =min(E_-(r_j)/Q'(r_j), E_+(r_j)/Q'(r_j))`,

`A_j^+ =max(E_-(r_j)/Q'(r_j), E_+(r_j)/Q'(r_j))`.

The actual hypothesis is the explicit finite set **`A_j^->0`**. No search over numerator coefficients or unproved certificate-existence premise occurs.

For the original problem, these comparator hypotheses are automatic under robust Hurwitz stability: `Q` is an admissible odd component and can be combined independently with every admissible even component. Hermite–Biehler gives its simple positive roots and `E_a(r_j)` signs `-,+,-`, the same signs as `Q'(r_j)`. Compactness gives the strict uniform residue lower bounds. Thus it is the later budget, not this common interlacing, that remains an additional sufficient restriction.

Conversely, without initially assuming stability, `A_j^->0`, `a_1>0` and `E_a(0)>0` imply that every nominal polynomial `E_a(-s^2)+sQ(-s^2)` is Hurwitz: the even component has signs `+,-,+,-` at `0,r_1,r_2,r_3`, hence exactly three simple positive roots, one before each successive odd root. This will supply the starting point for the final stability homotopy.

## 2. Explicit constants and the scalar budget

Let the odd coefficient half-widths be

`w_2=(u_2-l_2)/2`, `w_4=(u_4-l_4)/2`, `w_6=(u_6-l_6)/2`.

Set

`alpha_j=r_j A_j^->0`,

`H_j=4+sum_{k!=j} r_k/(r_j-r_k)`,

`b_j=A_j^+ |H_j|+r_j u_1+r_j sum_{k!=j} A_k^+/|r_j-r_k|`,

`k_j=r_j(w_2 r_j^2+w_4 r_j+w_6)/|Q'(r_j)|`.

All are explicit real expressions in the known box endpoints and the roots of its specified midpoint odd cubic. In particular each `b_j>0`, and hence the constant `C` below is positive.

Choose a small-frequency endpoint explicitly from coefficient bounds:

`t_0=min(1, l_7/[2(1+u_5+u_1)], l_6/[2(2+u_4)],`

`             q_0/[2(5+2q_1)])>0`.

Finally define

`A=(1/2)sum_j k_j^2/alpha_j >=0`,

`B=w_2+sum_j k_j b_j/alpha_j >=0`,

`C=(1/2)sum_j b_j^2/alpha_j >0`.                              (1)

The following is a sufficient certificate:

- If `A>0`, require **`B+2 sqrt(A C)<t_0`** and choose `epsilon=sqrt(A/C)`.
- If `A=0`, all three odd half-widths are zero (because `r_j>0`), so `O_a=Q` for every member and `B=0`; choose `epsilon=t_0/(2C)`.

In either case `epsilon>0` and

`Lambda=A/epsilon+B+C epsilon<t_0`.                            (2)

The fixed-odd case is the already classical synthesizable regime, recovered here with a quantitative construction, not claimed as a new open case. In positive odd-width boxes, the strict scalar inequality is the additional hypothesis. Its failure has no negative synthesis implication.

## 3. The actual common numerator and theorem

Put `D(t)=(tQ(t))'=Q+tQ'`, and choose

`b_epsilon(s)=sQ(-s^2)+epsilon D(-s^2)`

` =s^7+4epsilon s^6+q_2s^5+3epsilon q_2s^4`

`      +q_1s^3+2epsilon q_1s^2+q_0s+epsilon q_0`.              (3)

**Positive certificate theorem.** Under the explicit hypotheses and budget above, every member of the full independent box `K` is strictly Hurwitz and the single polynomial (3) is a common monic exact-degree-seven strict SPR numerator. The proof supplies a positive number `mu` with

`P_{a,b_epsilon}(t)>=mu(1+t)^7` for every `a in K`, `t>=0`.     (4)

Neither the numerator nor `epsilon` depends on the chosen denominator or frequency. The coefficient `a_1=[s^6]a` may vary over its full interval.

## 4. Exact pole identities and the global comparison

Fix a denominator, write `c_a=a_1`, and let `R_a=O_a-Q`, a polynomial of degree at most two. With `A_j=E_a(r_j)/Q'(r_j)`, exact partial fractions give

`E_a/Q=c_a+sum_j A_j/(t-r_j)`,

`D/Q=4+sum_j r_j/(t-r_j)`.

Their product is

`D E_a/Q^2=4c_a+sum_j [r_j A_j/(t-r_j)^2+B_j(a)/(t-r_j)]`,

`B_j(a)=A_j H_j+r_j[c_a+sum_{k!=j} A_k/(r_j-r_k)]`.

The explicit bounds in §2 give `|B_j(a)|<=b_j` and `r_j A_j>=alpha_j`. The additional odd-uncertainty term has the exact partial-fraction form

`t R_a/Q=-[t^2]R_a+sum_j K_j(a)/(t-r_j)`,

`K_j(a)=r_j R_a(r_j)/Q'(r_j)`.

This identity follows by matching its simple poles and its limiting constant at infinity. Since `R_a` has coefficient deviations bounded by `w_2,w_4,w_6`,

`[t^2]R_a<=w_2`, `|K_j(a)|<=k_j`.

The pairing with (3) is exactly

`P_{a,b_epsilon}=tQ O_a+epsilon D E_a`.

Off the three roots of `Q`, division by `Q^2` therefore yields

`P/Q^2=t-[t^2]R_a+4epsilon c_a`

`       +sum_j [epsilon r_j A_j/(t-r_j)^2`

`                    +(K_j(a)+epsilon B_j(a))/(t-r_j)]`.

Apply `gamma x^2+v x >=(gamma/2)x^2-v^2/(2gamma)` to each pole, use the uniform bounds, and drop only the nonnegative term `4epsilon c_a`. With `Q_j=Q/(t-r_j)` as an actual quadratic polynomial, this proves

`P_{a,b_epsilon}(t)`

` >=[t-Lambda]Q(t)^2+(epsilon/2)sum_j alpha_j Q_j(t)^2`,        (5)

because

`w_2+sum_j (k_j+epsilon b_j)^2/(2epsilon alpha_j)`

` =A/epsilon+B+C epsilon=Lambda`.

Both sides of (5) are polynomials after multiplication. Continuity extends the inequality across **all three** apparent poles; no frequency point is omitted. This is the promised global cubic comparison, but under the explicit scalar budget, not yet under robust stability alone.

For `t>=t_0`, (2) makes the first term of (5) nonnegative and the second strictly positive. The latter never vanishes identically at a point: the three quadratics `Q_j` have no common root. More quantitatively, their Lagrange identity

`sum_j Q_j(t)/Q'(r_j)=1`

holds by degree-at-most-two interpolation at the three distinct roots. If

`J=sum_j 1/Q'(r_j)^2>0`, `alpha_min=min_j alpha_j>0`,

Cauchy–Schwarz gives `sum_j Q_j^2>=1/J`. Thus

`P_{a,b_epsilon}(t)>=epsilon alpha_min/(2J)>0` for `t>=t_0`.   (6)

No finite point test has been used to infer an unbounded-frequency inequality.

## 5. Zero, small frequencies and an explicit weighted margin

For `0<=t<=t_0<=1`, the endpoint definitions give

`E_a(t)>=l_7-(u_5+u_1)t>=l_7/2>0`,

`O_a(t)>=l_6-(u_4+1)t>=l_6/2>0`.

Also

`D(t)=-4t^3+3q_2t^2-2q_1t+q_0`

`    >=q_0-(2q_1+4)t>=q_0/2>0`.

The same choice of `t_0` gives `Q(t)>=q_0/2>0`. Therefore the first pairing term `tQO_a` is nonnegative and the second is at least

`epsilon D E_a>=epsilon q_0 l_7/4>0`.                         (7)

This includes `t=0`. In particular no nonstrict origin exception is being passed off as the printed strict criterion.

Set

`m_0=min(epsilon q_0 l_7/4, epsilon alpha_min/(2J))>0`,

`T=max(2,2r_3)`.

Equations(6)–(7) give `P>=m_0` through `T`. For `t>=T`, `Lambda<t_0<=1` implies `t-Lambda>=t/2`, and `t-r_j>=t/2` gives `Q(t)^2>=t^6/64`. Equation(5) consequently yields `P>=t^7/128`. Hence one explicit uniform margin in(4) is

`mu=min(m_0/(1+T)^7, (T/(1+T))^7/128)>0`.                    (8)

The numerator has leading coefficient1 and exact degree seven by(3), so its limiting ratio to each monic septic is1. Every finite frequency, including the interpolation poles and zero, has already been covered.

## 6. Why denominator stability also follows

The residue hypotheses prove every nominal polynomial `E_a(-s^2)+sQ(-s^2)` Hurwitz, as shown in §1. For any actual member, hold its even component fixed and join its odd part to `Q` by

`O_lambda=Q+lambda(O_a-Q)`, `0<=lambda<=1`.

Because the odd coefficients vary independently in closed intervals and `Q` is their midpoint, this path remains inside the original box. The bounds leading to (4) hold throughout. An imaginary-axis root of a path denominator would force its pairing with the fixed numerator to vanish, contradicting(4). Monicity, fixed degree and bounded path coefficients prevent escape to infinity. Root continuity therefore proves the actual denominator Hurwitz.

Thus the certificate supplies genuine stability of the given denominators, not only a rational expression made analytic by cancellation.

## 7. What the missing universal comparison must still deliver

For a robustly stable interval box, its actual midpoint odd cubic automatically supplies the comparator roots and positive even residues. Its actual odd coefficient widths determine `k_j,w_2`, including the **terminal scale `r_3`**. Unlike an even-data-only terminal bracket, every displayed constant uses those actual odd data.

The positive theorem then gives a full common numerator, strict whole-frequency margin and denominator stability whenever the scalar budget holds, without a fixed-`a_1` restriction. This sharpens what a successful cubic comparison would purchase.

However:

1. **No proof that all robustly stable boxes satisfy this budget exists here.** The absolute-value estimates deliberately lose cancellations and can be conservative. They must not be treated as necessary conditions.
2. No proof is given that another admissible comparator always makes the budget hold. The theorem fixes the midpoint odd comparator to avoid hiding a search or certificate-existence premise.
3. The general target is not narrowed to the explicit numerator ansatz(3). If this sufficient family of numerators fails, other degree-seven numerators remain fully admissible.
4. The old critical-contact alternatives and arbitrary radial boundary strata are not excluded by this certificate.

The remaining universal step is still new mathematics: control the true cubic interaction globally from the coefficient-width/stability hypotheses, preserving whatever cancellations this conservative bound discards, or exhibit an exact obstruction against unrestricted numerators. This appendix is a positive conditional ingredient, not that missing theorem.

## 8. Dependency, review and novelty ceiling

The derivation is a generalization of the same elementary positive-residue and square-completion mechanism already consolidated once in v2. It does not import the announced sextic theorem, its Lean build, or an unstated common-numerator theorem. The degree-specific Hermite–Biehler criterion, elementary rational partial fractions, polynomial interpolation, Cauchy–Schwarz and root continuity remain explicit standard imports.

This appendix has not been independently reviewed. Earlier reviews of the special residue constants in v1 do not automatically authenticate these new uniform formulas, the comparator assumptions, the scalar budget or the stability path. Parent and actual separate reconstruction must precede any promotion.

Fixed-parity synthesis and robustness near it are classical; positive-real residue methods and square completion are also classical. **NOVELTY-UNCLEAR**, no first/best/optimal/solved-book claim. No separate discovery or theorem tally is assigned to this positive-side consolidation. No scientific executable, formal/kernel, outside-model or human verification occurred.
