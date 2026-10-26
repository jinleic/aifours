# Candidate v1: a full-width degree-seven obstruction to intervalized one-step Routh induction

Observed before creation: **2026-10-23T14:12:14-0700**. Author: InfoSPR7, info-2. Status: **CANDIDATE — complete written argument, awaiting separate reconstruction**. No scientific program, solver, enumeration, arithmetic interpreter, compilation or certificate replay was executed. Classical Hermite–Biehler interlacing is an explicit import; the sextic SPR claim, its Lean development and the old dossier's critical-certificate theorems are not imports to this proof.

## 0. Scope and decision value

This is **not** a proof or counterexample to universal degree-seven interval synthesis. It is an exact, all-parameter obstruction to a specific possible induction:

> Lower each Hurwitz septic by one Routh step, take the independent coefficient-interval hull of the resulting monic sextics, and apply the sextic interval SPR theorem to that hull.

The hull need not be Hurwitz. We prove failure even for degree-seven boxes with **all seven lower coefficient widths positive** and an **explicit strict common degree-seven numerator**. The unmodified route therefore fails before any numerator-lifting issue. The original conjecture still needs a different uniform positivity mechanism, or an exact obstruction to the original full numerator quantifier.

Fixed-odd-part synthesis and the general danger of intervalized Routh reduction are prior art, not discoveries here. The exact parametric packet and the full-width quantitative extension below have not received priority clearance. The primary comparison in §8 already rules out presenting the generic instability phenomenon as new.

## 1. Definitions and classical import

For a real polynomial `p`, write

`p(i w) = E_p(t) + i w O_p(t)`, where `t=w^2`,

or equivalently `p(s)=E_p(-s^2)+s O_p(-s^2)`. Define

`P_{p,b}(t)=E_p(t)E_b(t)+t O_p(t)O_b(t)`.

For a Hurwitz denominator, strict positivity of this real polynomial on `t>=0` is exactly the book's finite-frequency SPR inequality.

The form of **Hermite–Biehler** used here is: a degree-seven real polynomial with positive leading coefficient, positive component constants, and negative leading coefficients in its cubic components is Hurwitz exactly when its three even-component and three odd-component roots are positive, simple and strictly ordered

`e_1 < o_1 < e_2 < o_2 < e_3 < o_3`.

For degree six, the cubic even and quadratic odd roots must instead be strictly ordered

`e_1 < v_1 < e_2 < v_2 < e_3`,

with positive polynomial leading coefficient and the corresponding positive constants. These are the degree-specific classical interlacing criteria, not new claims.

For any monic Hurwitz septic `p`, put `c=[s^6]p>0` and define its **normalized one-step Routh reduction** by

`T(p)(s) = ( E_p(-s^2) + s[O_p(-s^2)-E_p(-s^2)/c] )/c`.       (1)

This is monic of degree six: the degree-three terms of `O_p-E_p/c` cancel. It is Hurwitz. Indeed its odd component before division by `c` agrees with `O_p` at the three roots `e_1,e_2,e_3` of `E_p`, and therefore has signs `+,-,+` there. A polynomial of degree at most two with these signs has exactly two simple roots, one in each intervening interval, and positive leading coefficient. Hermite–Biehler gives the conclusion. Thus **every pointwise reduction in the construction below really is stable**; instability appears only when its coefficient correlations are discarded.

For any bounded polynomial family, `Hull` below means the smallest independent closed interval for each lower coefficient, keeping the monic leading coefficient fixed.

## 2. The base degree-seven interval family

Let

`0 < d <= 1/10`, `0 <= u <= 10d`,

and define

`O(t)=-(t-2)(t-4)(t-6)=-t^3+12t^2-44t+48`,

`E_{d,u}(t)=-(t-1)(t-3)(t-6+d)+u`

`             =-t^3+(10-d)t^2-(27-4d)t+18-3d+u`.

Set

`a_{d,u}(s)=s^7+s^6+12s^5+(10-d)s^4+44s^3`

`             +(27-4d)s^2+48s+(18-3d+u)`.                     (2)

For fixed `d`, these polynomials form a genuine closed interval box with only its constant interval nondegenerate. Call it `K_d`.

Every member is strictly Hurwitz. In fact

- `E_{d,u}(0)>0`;
- `E_{d,u}(2)=-4+d+u <= -4+11d <0`;
- `E_{d,u}(4)=6-3d+u >0`;
- `E_{d,u}(6)=-15d+u <= -5d <0`.

The cubic therefore has one root in each of `(0,2)`, `(2,4)`, `(4,6)`. These three distinct roots exhaust its degree, hence are simple. They interlace the fixed odd roots `2,4,6` in precisely the degree-seven Hurwitz order. All component constants and leading signs have the required values.

## 3. Exact unstable sextic hull member

Since `[s^6]a_{d,u}=1`, (1) gives

`q_{d,u}(s)=T(a_{d,u})(s)`

` =s^6+(2+d)s^5+(10-d)s^4+(17+4d)s^3+(27-4d)s^2`

`     +(30+3d-u)s+(18-3d+u)`.                                (3)

Every `q_{d,u}` is Hurwitz by §1, but its last two coefficients obey the correlation

`[s]q_{d,u} + [1]q_{d,u} =48`.

Their independent interval hull contains

`q_d^bad(s)=s^6+(2+d)s^5+(10-d)s^4+(17+4d)s^3`

`             +(27-4d)s^2+(30-7d)s+(18-3d)`.                  (4)

This selects the smaller linear coefficient from `u=10d` and the smaller constant coefficient from `u=0`, and so is **not an actual pointwise reduction**.

Its even component is `E_{d,0}`, whose roots are exactly `1,3,6-d`. At the largest root `r=6-d`, its odd component is

`O(r)-E_{d,0}(r)-10d`

` = d[(4-d)(2-d)-10] < -2d <0`.                              (5)

A Hurwitz sextic with this even component must have a quadratic odd component positive at the largest even root. Equation (5) contradicts that necessary Hermite–Biehler sign. Thus (4) is not Hurwitz. This is an exact polynomial obstruction valid for **every** `d` in the displayed continuum, not a numerical sample.

There is no imaginary-axis ambiguity: at the other two even roots its odd component has values `15-10d>0` and `-3-10d<0`, and the value in (5) is nonzero; its constant coefficient is positive. Hence (4) has no imaginary-axis zero and actually has an open-right-half-plane root. Positive coefficients exclude a positive real root, so a nonreal conjugate pair is present. An exact count of those roots is not needed or claimed.

## 4. An actual strict common numerator for the original degree-seven family

Define

`C(t)=(t O(t))'=O(t)+t O'(t)=-4t^3+36t^2-88t+48`,

`epsilon=d/104`,

`b_d(s)=s O(-s^2)+epsilon C(-s^2)`

` =s^7+(d/26)s^6+12s^5+(9d/26)s^4+44s^3`

`      +(11d/13)s^2+48s+(6d/13)`.                            (6)

It is real, monic and of exact degree seven, and independent of `u`. Its pairing with (2) is

`P_{a_{d,u},b_d}(t)=t O(t)^2+epsilon C(t)E_{d,u}(t)`.          (7)

We prove the quantitative whole-half-line estimate

`P_{a_{d,u},b_d}(t) >= m_d (1+t)^7` for every `t>=0`,

`m_d=5d^2/(78*13^7)>0`.                                      (8)

### 4.1 Positive residues and their uniform bounds

Write `r_1=2,r_2=4,r_3=6`, and

`A_1=(4-d-u)/8`, `A_2=(6-3d+u)/4`, `A_3=(15d-u)/8`.

These are exactly `E_{d,u}(r_j)/O'(r_j)`. Partial fractions give

`E_{d,u}/O =1+sum_j A_j/(t-r_j)`,

`C/O =4+sum_j r_j/(t-r_j)`.                                  (9)

Uniformly over the full `d,u` range,

`29/80 <= A_1 <= 1/2`,

`57/40 <= A_2 <= 67/40`,

`5d/8 <= A_3 <= 15d/8 <= 3/16`.                              (10)

In particular all residues are strictly positive. Multiplying (9), the partial-fraction identity is

`C E_{d,u}/O^2 =4+sum_j [alpha_j/(t-r_j)^2+B_j/(t-r_j)]`,

`alpha_j=r_j A_j`,

`B_1=A_1/2+2-A_2-A_3/2`,

`B_2=2A_2+4+2A_1-2A_3`,

`B_3=(13/2)A_3+6+(3/2)A_1+3A_2`.                            (11)

The identity follows by matching the double and simple principal parts at each pole and the limiting constant `4` at infinity. For example the regular part of `C/O` at `r_1` is `4+4/(2-4)+6/(2-6)=1/2`; the other two regular parts are `2` and `13/2`, giving exactly the displayed `B_j`.

The bounds (10) imply

`0<B_1<=9/4`, `0<B_2<9`, `0<B_3<13`.                          (12)

For the only potentially delicate sign, `B_1 >=2-67/40-3/32=37/160>0`. The last upper bound is `B_3<=2079/160<13`; the middle upper bound is `B_2<=167/20<9`.

Consequently

`sum_j B_j^2/(4alpha_j)`

` <=405/232 + 135/38 + 169/(15d)`

` <6+12/d <13/d`.                                            (13)

No finite evaluation is used to infer any identity or parameter inequality.

### 4.2 Completing squares globally, including all odd-root frequencies

For real `x` and `alpha>0`,

`alpha x^2+B x >= (alpha/2)x^2-B^2/(2alpha)`.

Apply this to (11), use (13), multiply by `O(t)^2`, and substitute `epsilon=d/104`. With `Q_j(t)=O(t)/(t-r_j)` interpreted as its actual quadratic polynomial, (7) satisfies

`P_{a_{d,u},b_d}(t)`

` >= (t-1/4)O(t)^2+(epsilon/2)sum_j alpha_j Q_j(t)^2`.         (14)

Initially this is obtained off `2,4,6`; both sides are polynomials, so continuity establishes it at those frequencies too. Since every `A_j>=5d/8` and every `r_j>=2`, for `t>=1/2` it gives

`P_{a_{d,u},b_d}(t)`

` >= (t/2)O(t)^2 + (5d^2/832)sum_j Q_j(t)^2`.                 (15)

The exact Lagrange identity is

`sum_j Q_j(t)/O'(r_j)=1`.

Its two sides are degree-at-most-two polynomials agreeing at the three distinct nodes `r_j`, so this is a legitimate interpolation proof, not a finite-value smoke check. Since `O'(r_j)=(-8,4,-8)`, Cauchy–Schwarz yields

`1 <= (sum_j Q_j(t)^2)(1/64+1/16+1/64)`

`   =(3/32)sum_j Q_j(t)^2`.

Thus (15) proves

`P_{a_{d,u},b_d}(t) >=5d^2/78` for `t>=1/2`.                  (16)

In particular the bound covers exactly `t=2,4,6`, not only punctured neighborhoods.

### 4.3 Zero and the frequency tail

For `0<=t<=1/2`, the factorization gives

`E_{d,u}(t)>=(1/2)(5/2)(27/5)=27/4`.

Also `C'(t)=-12t^2+72t-88<0` on that interval, and `C(1/2)=25/2`; hence `C(t)>=25/2`. Formula (7) therefore gives

`P_{a_{d,u},b_d}(t)>=675d/832 >=5d^2/78`.                     (17)

In particular `t=0` is strictly positive; no weak-origin exception is hidden.

For `t>=12`, every `t-r_j>=t/2`. Therefore (15) gives

`P_{a_{d,u},b_d}(t)>=(t/2)O(t)^2>=t^7/128`.                  (18)

On `0<=t<=12`, (16)–(17) imply (8) because `(1+t)^7<=13^7`. For `t>=12`, use `t/(1+t)>=12/13` and

`12^7/128 >5d^2/78`

to obtain (8) from (18). This proves the claimed global strict estimate, without sampling and without invoking the sextic theorem.

## 5. Full-width degree-seven boxes with the same obstruction

Set

`rho_d=m_d/1484=5d^2/(78*13^7*1484)>0`,

and let `B_d` consist of every monic degree-seven polynomial `a_{d,u}+v`, where `0<=u<=10d` and

`v(s)=sum_{k=0}^6 eta_k s^k`, `|eta_k|<=rho_d` independently.

Equivalently its seven independent intervals, in descending order below the monic leading term, are

- `[s^6]p in [1-rho_d,1+rho_d]`;
- `[s^5]p in [12-rho_d,12+rho_d]`;
- `[s^4]p in [10-d-rho_d,10-d+rho_d]`;
- `[s^3]p in [44-rho_d,44+rho_d]`;
- `[s^2]p in [27-4d-rho_d,27-4d+rho_d]`;
- `[s]p in [48-rho_d,48+rho_d]`;
- `[1]p in [18-3d-rho_d,18+7d+rho_d]`.

All widths are positive. The base family `K_d` is contained in `B_d`.

The sum of absolute coefficients of (6) is

`105+176epsilon <=105+11/65 <106`.

For `t=w^2>=0`, each `|w|^k`, `0<=k<=7`, is at most `(1+t)^(7/2)`. Therefore

`|b_d(iw)| <=106(1+t)^(7/2)`,

`|v(iw)| <=7rho_d(1+t)^(7/2)`,

and hence

`|P_{v,b_d}(t)|<=742rho_d(1+t)^7=(m_d/2)(1+t)^7`.

Together with (8), this proves

`P_{p,b_d}(t)>=(m_d/2)(1+t)^7>0`                             (19)

for every `p in B_d` and every `t>=0`.

Every denominator in `B_d` is actually strictly Hurwitz, not merely a canceled rational function. To see this, connect `p=a_{d,u}+v` to its Hurwitz base `a_{d,u}` by `a_{d,u}+lambda v`, `0<=lambda<=1`. Estimate (19) holds throughout. An imaginary-axis zero of any polynomial on the path would force its pairing to vanish at that frequency, contradicting (19). The degree is fixed and monic and coefficients remain bounded, so roots cannot escape to infinity. Root continuity therefore preserves their open-left-half-plane location along the path. Thus (6) is a genuine common exact-degree-seven strict SPR numerator for the full box `B_d`.

For every `p in B_d`, `T(p)` is a stable monic sextic by §1. Nevertheless

`Hull(T(B_d)) superset Hull(T(K_d))`

contains the explicit non-Hurwitz polynomial (4). The failure therefore persists with **independent positive uncertainty in every lower coefficient**, not only on a coefficient-fixed face.

## 6. Literal theorem established by the written candidate

For every real `d` with `0<d<=1/10`, the explicit full-width monic interval box `B_d` in §5 is robustly Hurwitz and has the explicit fixed monic numerator (6), satisfying the uniform strict pairing estimate (19) at every real frequency. The normalized one-step Routh reduction (1) maps each of its members to a Hurwitz monic sextic, but the independent coefficient-interval hull of all those sextics is not Hurwitz, with exact witness (4) and sign obstruction (5).

The parameter `d` may tend to zero; there is no lower bound on the positive widths. Thus small absolute uncertainty alone does not repair the induction rule. This does **not** claim a fixed stability margin as `d` tends to zero: the displayed pairing and thickening bounds shrink like `d^2`.

## 7. Original-target gap, trust and verification boundaries

- **Original target:** universal synthesis for every robustly Hurwitz monic degree-seven interval family. **Unresolved.** The explicit `B_d` are a special sufficient family, not a covering class or a universal radial-boundary argument.
- **What is obstructed:** replacing the actual correlated sextic Routh image by its independent coefficient-interval hull and assuming that hull stable. Nothing here excludes a genuinely correlation-preserving induction, a different stable enclosure, or another numerator-lifting map.
- **Actual numerator:** (6), not a feasibility encoding or a numerical LP vector. Its proof covers the full seven-width boxes and all finite frequencies, including the poles of the partial-fraction calculation and zero. Both numerator and denominators have exact degree seven. The limiting ratio at infinity is one because both are monic.
- **Imports:** only the stated classical Hermite–Biehler criterion, elementary polynomial interpolation/partial fractions, Cauchy–Schwarz and root continuity. No old critical-contact theorem or unauthenticated Lean claim is needed.
- **Evidence:** authored written proof only, pending separate reconstruction and parent review on the immutable hash. No numerical search, scientific executable, proof-assistant kernel, human review or outside-model review performed.
- **Novelty/significance:** NOVELTY-UNCLEAR; generic interval-reduction instability is known. This exact septic-to-sextic countercontrol prevents an invalid extension of the new sextic source but does not close an original open-case quantifier. It must not be counted as a solved book problem.

## 8. Primary-source comparison actually read

1. [Xu et al., sextic SPR, arXiv:2609.26541v2](https://arxiv.org/html/2609.26541v2), Theorem2.1, Section2 and Sections5–8: the theorem requires the **whole independent monic sextic box** to be Hurwitz; it gives no conclusion for an unstable hull or an arbitrary correlated image. Its fixed-even-part case and the older fixed-parity results are baselines.
2. [Wang–Yu, arXiv:math/0202242v1](https://arxiv.org/html/math/0202242v1), Sections1–2: fixed even or odd parts were already known synthesizable; the base family `K_d` is not a new unsolved class.
3. [Bokam–Singh–Devarapalli–García Márquez, *An improvement of Gamma approximation for reduction of continuous interval systems*, Archives of Control Sciences31(2),347–373(2021), doi:10.24425/acs.2021.137422](https://journals.pan.pl/Content/120111/PDF/art06.pdf), actual introduction pp348–349 and Section2.1 read. The paper records that earlier interval Routh reductions can turn stable interval systems into unstable interval models and uses modified Routh constructions. This is direct prior-art evidence against novelty of the generic phenomenon. The present map (1) and its exact normalized interval hull, rather than that paper's modified approximation, are the object proved unsafe here. No claim is made to refute its modified method, and its numerical examples were not replayed.

Failed source accesses retained as limits: the earlier Citeseer Routh link returned a Wayback wrapper rather than paper text; a ScienceDirect source returned HTTP403. Neither is treated as read primary theorem evidence.
