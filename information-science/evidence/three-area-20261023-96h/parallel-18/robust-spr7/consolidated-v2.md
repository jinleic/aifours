# SPR7 consolidated v2 — two scoped obstructions, one conditional lift, one shared positivity proof

Observed before creation: **2026-10-23T14:39:11-0700**. InfoSPR7, info-2. This consolidation follows the parent's packaging instruction; all v1 snapshots remain unchanged. **Universal degree-seven synthesis is unresolved.** The consolidated bytes are a new unreviewed presentation; prior reviews apply only to their pinned source claims as recorded below. No scientific program, arithmetic interpreter, solver, enumeration, compilation, executable certificate replay or model CLI was used.

## 1. Exact target, evidence and provenance

The target remains:

> For every closed monic real degree-seven coefficient box `K`, allowing degenerate intervals, if every denominator is strictly Hurwitz, is there one fixed real polynomial `b` of **exact degree seven**, independent of denominator and frequency, with `Re(b(iw)/a(iw))>0` for every `a in K` and every finite real `w`, including zero?

The book's actual pp680–682 images were read. Page680 fixes exact polynomial order, Hurwitz denominators and finite-real-frequency strict positivity; page682 poses sufficiency above order four. The monic specialization follows the actual Wang–Yu and modern quintic/sextic source definitions; the book itself does not explicitly restrict the leading coefficient. Uncertain leading coefficients are not silently included.

This document contains:

- **Routh-hull obstruction:** pointwise stable normalized sextic reductions can have an unstable independent coefficient hull, even for full-seven-width septic boxes with an actual common strict numerator.
- **Conditional dual lift:** when the second septic coefficient is the same fixed `c` across a compact family and a certified common strict sextic numerator for its **actual correlated image** is supplied, an exact polynomial identity gives a common septic numerator after controlled degree raising. Existence of the supplied sextic numerator is not proved.
- **Plant-box numerator obstruction:** full-seven-width septic boxes can have a common strict numerator while every numerator belonging to the plant box itself fails. This excludes corners, midpoint and convex mixtures, not the unrestricted numerator quantifier.
- **Terminal-root control:** even-root data alone cannot provide a finite terminal odd-root bracket. It does not rule out cubic bounds using actual odd coefficients.

### Immutable source pins and actual review coverage

All four source hashes below were freshly observed together before this consolidation:

| Source in this root | SHA256 | Actual review evidence observed |
|---|---|---|
| `routh-obstruction-candidate-v1.md` | `47953be4805c2838a93204d077e71d2332e3468c09dc69fb973fba6563058cac` | InfoHinfPreview's complete reconstruction found no FATAL/MAJOR/MINOR defect at stated scope |
| `dual-lift-candidate-v1.md` | `d9861944688b8b4bb958b6622ce84401735e59f91cec5212b16206478e8a66da` | Same separate agent reconstructed the fixed-c conditional claim; no substantive defect |
| `cubic-bound-attack-v1.md` | `9e5e2ed587fc88d14de7985810552a1cf97ecc14c79bc6230eb95517e6f87d4f` | Reviewed with the dual lift; only even-data-only terminal bounds are excluded |
| `plant-box-numerator-obstruction-candidate-v1.md` | `fe19b52a9fe9e4a319b498b72d011c25ccbcf326cf2b3b01fac97ccf199c2d88` | **Not independently reviewed yet**; queued by parent |

The two actual review files, read in full and independently hash-observed, are in the reviewer's own `../stochastic-hinf-preview/` root:

- `peer-review-SPR7-Routh-obstruction-v1.md`: `cc5afd3f33275acad5033a2449cc9e03f0a1a7372fd3e9eb5dc6aa74684d7bda`.
- `peer-review-SPR7-dual-lift-v1.md`: `f59541da355c464eb362e4d3669bdf9870c3a1052c7a6e55aef6eb1db511e723`.

These are ordinary in-harness written reconstructions with supplied proofs, not blind, different-model-family, outside-model, human or formal reviews. Parent acceptance of these claims has not been observed. Consolidation itself still needs a fidelity/reconstruction pass against the above source snapshots.

**One common positivity import, not several independent results:** §3 below reproduces the residue-margin proof from the Routh v1. Both the full-width Routh countercontrol (§4) and the scaled plant-box numerator exclusion (§6) use that same lemma. The positive synthesis component must not be counted twice. The conditional lift in §5 uses a separately supplied sextic margin, not this residue lemma.

## 2. Definitions and classical interlacing boundary

For real polynomials `p,b`, put `t=w^2` and write

`p(s)=E_p(-s^2)+s O_p(-s^2)`,

`P_{p,b}(t)=E_p(t)E_b(t)+t O_p(t)O_b(t)`.

Then `p(iw)=E_p(t)+iw O_p(t)` and

`Re(b(iw)/p(iw))=P_{p,b}(t)/|p(iw)|^2`

when the denominator is Hurwitz. Strict pairings on `t>=0` therefore give exactly the stipulated finite-frequency strictness.

The named classical import is Hermite–Biehler. For degree seven with positive polynomial leading coefficient, positive component constants and negative leading coefficients in the two cubic components, the strictly Hurwitz order is

`e_1<o_1<e_2<o_2<e_3<o_3`,

all roots being positive and simple. For degree six, a cubic even part and quadratic odd part have order

`e_1<v_1<e_2<v_2<e_3`,

with the corresponding positive constants and leading signs. These degree-specific criteria, root continuity, elementary partial fractions/interpolation and Cauchy–Schwarz are explicit classical imports. No old critical-certificate theorem or unauthenticated Lean theorem is needed for the constructions here.

## 3. The single shared residue-margin lemma

For `0<d<=1/10` and `0<=u<=10d`, define

`O(t)=-(t-2)(t-4)(t-6)=-t^3+12t^2-44t+48`,

`E_{d,u}(t)=-(t-1)(t-3)(t-6+d)+u`

`             =-t^3+(10-d)t^2-(27-4d)t+18-3d+u`,

`D(t)=(tO(t))'=-4t^3+36t^2-88t+48`,

`epsilon_d=d/104`, `m_d=5d^2/(78*13^7)`.

**Shared lemma.** For the full parameter range and every `t>=0`,

`tO(t)^2+epsilon_d D(t)E_{d,u}(t) >= m_d(1+t)^7>0`.            (M)

This is the one positivity proof used in both obstruction constructions.

### 3.1 Residues and exact rational identity

At `r=(2,4,6)`, `O'=(-8,4,-8)`. Put

`A_1=(4-d-u)/8`, `A_2=(6-3d+u)/4`, `A_3=(15d-u)/8`.

They are exactly `E_{d,u}(r_j)/O'(r_j)`. Hence

`E_{d,u}/O=1+sum_j A_j/(t-r_j)`,

`D/O=4+sum_j r_j/(t-r_j)`.

The residues obey

`29/80<=A_1<=1/2`, `57/40<=A_2<=67/40`,

`5d/8<=A_3<=15d/8<=3/16`.                                    (10)

Multiplying the two partial-fraction expressions gives

`D E_{d,u}/O^2=4+sum_j [alpha_j/(t-r_j)^2+B_j/(t-r_j)]`,

`alpha_j=r_j A_j`,

`B_1=A_1/2+2-A_2-A_3/2`,

`B_2=2A_2+4+2A_1-2A_3`,

`B_3=(13/2)A_3+6+(3/2)A_1+3A_2`.                             (11)

For completeness this identity follows from the principal parts at each simple pole and the limiting constant4 at infinity. The regular parts of `D/O` at the three poles are respectively `1/2,2,13/2`, producing the displayed simple-pole coefficients.

The residue bounds imply

`0<B_1<=9/4`, `0<B_2<9`, `0<B_3<13`.

In detail, `B_1>=2-67/40-3/32=37/160>0`, `B_2<=167/20<9`, and `B_3<=2079/160<13`. Therefore

`sum_j B_j^2/(4alpha_j)`

` <=405/232+135/38+169/(15d)`

` <6+12/d<13/d`.                                              (12)

These are symbolic parameter inequalities, not inferred from finite evaluations.

### 3.2 Square completion retains positivity at every apparent pole

The elementary inequality

`alpha x^2+B x >=(alpha/2)x^2-B^2/(2alpha)`

and (11)–(12) give, after multiplication by `O^2`,

`tO^2+epsilon_d D E_{d,u}`

` >=(t-1/4)O^2+(epsilon_d/2)sum_j alpha_j Q_j^2`,

where `Q_j=O/(t-r_j)` is the actual quadratic polynomial. Though first derived off the three poles, both sides are polynomials; continuity proves the inequality at the poles too.

Every `A_j>=5d/8`, so `alpha_j>=5d/4`. For `t>=1/2`,

`tO^2+epsilon_d D E_{d,u}`

` >=(t/2)O^2+(5d^2/832)sum_j Q_j^2`.                          (13)

The Lagrange identity `sum_j Q_j/O'(r_j)=1` is exact: both sides have degree at most two and agree at the three distinct interpolation nodes. Cauchy–Schwarz gives

`1 <=(sum_j Q_j^2)(1/64+1/16+1/64)=(3/32)sum_j Q_j^2`.

Thus (13) bounds the pairing below by `5d^2/78` on the whole `t>=1/2`, including exactly `2,4,6`. This interpolation has the requisite degree argument; it is not a sampling-based proof.

### 3.3 Origin and infinity

On `0<=t<=1/2`, the factored even polynomial satisfies

`E_{d,u}(t)>=(1/2)(5/2)(27/5)=27/4`.

Also `D'<0` there and `D(1/2)=25/2`. Hence the pairing is at least

`(d/104)(25/2)(27/4)=675d/832 >=5d^2/78`.

This includes strict positivity at zero. For `t>=12`, each `t-r_j>=t/2`, so (13) gives the additional lower bound `t^7/128`. Through `t=12`, divide the constant bound by `(1+t)^7<=13^7`; beyond it use `t/(1+t)>=12/13` and `12^7/128>5d^2/78`. Together these prove (M) everywhere on the half-line.

## 4. Routh-hull obstruction with actual strict synthesis

### 4.1 Pointwise normalized Routh reduction is genuinely stable

For a monic Hurwitz septic `p`, let `c=[s^6]p>0` and define

`T(p)(s)=(E_p(-s^2)+s[O_p(-s^2)-E_p(-s^2)/c])/c`.             (R)

The cubic terms of `O_p-E_p/c` cancel, and the even leading coefficient after division is monic. At the three even roots, the remaining quadratic agrees with `O_p` and has signs `+,-,+`. It therefore has exactly two simple roots between successive even roots and positive leading coefficient. Its constant is positive because those roots are positive. The degree-six Hermite–Biehler order proves that each `T(p)` is Hurwitz. The obstruction below is not a failure of this pointwise step.

### 4.2 Full-width septic boxes

Let

`a_{d,u}(s)=s^7+s^6+12s^5+(10-d)s^4+44s^3`

`             +(27-4d)s^2+48s+(18-3d+u)`.

Its components are `E_{d,u},O`. The signs of `E_{d,u}` at `0,2,4,6` are `+,-,+,-`, since

`E(2)<=-4+11d<0`, `E(4)=6-3d+u>0`, `E(6)<=-5d<0`.

The even roots lie one each in `(0,2),(2,4),(4,6)`, are simple and interlace the fixed odd roots. Thus every base denominator is strictly Hurwitz.

Define

`b_d(s)=sO(-s^2)+(d/104)D(-s^2)`

` =s^7+(d/26)s^6+12s^5+(9d/26)s^4+44s^3`

`      +(11d/13)s^2+48s+(6d/13)`.

Its pairing is exactly the left side of (M). To get all seven widths positive, set `rho_d=m_d/1484` and let `B_d` be every `a_{d,u}+v`, with `0<=u<=10d` and independently `|[s^k]v|<=rho_d`, `0<=k<=6`. The independent lower intervals are

`[1±rho_d]`, `[12±rho_d]`, `[10-d±rho_d]`, `[44±rho_d]`,

`[27-4d±rho_d]`, `[48±rho_d]`, `[18-3d-rho_d,18+7d+rho_d]`.

Here `[x±r]` denotes `[x-r,x+r]`; the leading coefficient stays1.

The absolute coefficient sum of `b_d` is `105+176d/104<=105+11/65<106`. For `t=w^2`, each monomial up to degree seven has magnitude at most `(1+t)^(7/2)`. Thus

`|P_{v,b_d}(t)|<=106*7*rho_d(1+t)^7=(m_d/2)(1+t)^7`.

Using (M),

`P_{p,b_d}(t)>=(m_d/2)(1+t)^7>0` for every `p in B_d`.         (14)

Denominator stability for the full box is proved, not assumed: on the path `a_{d,u}+lambda v`, (14) prevents an imaginary-axis zero. Fixed monic degree and bounded path coefficients prevent roots escaping through infinity. Root continuity from the Hurwitz base member proves every denominator strictly Hurwitz. Thus `b_d` is an actual common exact-degree-seven strict numerator for the full box.

### 4.3 The independent sextic hull contains an exact unstable polynomial

On the base family, (R) gives

`q_{d,u}=s^6+(2+d)s^5+(10-d)s^4+(17+4d)s^3+(27-4d)s^2`

`          +(30+3d-u)s+(18-3d+u)`.

The last two coefficients sum to48. Discarding that correlation puts

`q_d^bad=s^6+(2+d)s^5+(10-d)s^4+(17+4d)s^3+(27-4d)s^2`

`           +(30-7d)s+(18-3d)`                                (15)

inside the independent coefficient hull: it takes the smaller linear coefficient at `u=10d` and the smaller constant at `u=0`.

Its even component has exact roots `1,3,6-d`. At the largest root `r=6-d`, its odd component is

`O(r)-E_{d,0}(r)-10d=d[(4-d)(2-d)-10]<-2d<0`.

A Hurwitz sextic requires the odd component positive at that largest even root. Hence (15) is not Hurwitz. At the other two even roots the odd values are `15-10d>0` and `-3-10d<0`, so there is no imaginary-axis zero; the positive constant excludes zero as well. Non-Hurwitz therefore means an open-right-half-plane root. All coefficients are positive, excluding positive real roots, so a nonreal conjugate pair is present; no exact root count is asserted.

The base family is contained in `B_d`, hence its hull witness remains in `Hull(T(B_d))`. This refutes only the naive independent-hull induction. It does not refute a correlation-preserving method, another stable enclosure or universal SPR7. Small absolute widths do not repair the rule: `d` can tend to zero, though the displayed margin and thickening shrink like `d^2`.

## 5. Conditional correlation-preserving dual lift

This section is a sufficient analytical bridge, **not a third obstruction or an existence theorem for the required sextic numerator**.

Let `K` be any compact robustly Hurwitz monic septic family whose coefficient `[s^6]a=c>0` is the same fixed number for every member. Let `q_a=T(a)` be its true correlated image. Suppose a real degree-six polynomial

`beta(s)=F(-s^2)+sG(-s^2)`

is supplied with a correct common strict-SPR proof for **every actual** `q_a`. No interval hull is introduced, and no unverified sextic existence/Lean claim is used as a premise in disguise.

Put

`b_0(s)=F(-s^2)+(s+s^2/c)G(-s^2)`.

Because `deg F<=3`, `deg G<=2`, `deg b_0<=6`. Its components are `F-tG/c,G`, so exact multiplication gives

`P_{a,b_0}=(F-tG/c)E_a+tG O_a`

`          =F E_a+tG(O_a-E_a/c)`

`          =c P_{q_a,beta}`.                                  (16)

The leading coefficient of `beta` is positive: its ratio to monic `q_a` has a nonnegative limit, and exact degree rules out zero. Therefore

`P_{q_a,beta}(t)/(1+t)^6`

extends continuously to the compactified endpoint `t=infinity` with that same positive leading coefficient. Compactness of the actual image family and strictness at every finite frequency give a positive minimum `mu`. Any supplied certified positive lower bound can replace this minimum; the argument does not claim a numerical algorithm establishing the omitted common numerator.

Write `a=s^7+c s^6+a_2s^5+...+a_6s+a_7`, and let `U_2=max a_2`, `U_6=max a_6`. Every monic Hurwitz coefficient is positive. Set

`epsilon=c mu/[2(1+U_2+U_6)]>0`, `b=b_0+epsilon s^7`.

The exact monomial pairing is

`P_{a,s^7}=-t^4O_a=t^7-a_2t^6+a_4t^5-a_6t^4`

`             >=-(U_2+U_6)(1+t)^6`.

Together with (16), this proves

`P_{a,b}> (c mu/2)(1+t)^6>0` for all `a,t>=0`.

The added leading term has positive coefficient `epsilon` and cannot cancel against degree-at-most-six `b_0`; hence `b` has exact degree seven. This covers zero and every finite frequency and has positive limiting ratio `epsilon` at infinity.

**Both missing obligations remain explicit:** a common strict `beta` for arbitrary true images has not been supplied; and when `[s^6]a` varies, the formula's `1/c` would make the numerator denominator-dependent. Neither premise can be dropped silently.

## 6. Plant-box numerator obstruction, using exactly the same margin (M)

### 6.1 Full-width boxes with an actual outside numerator

Fix `d_0=1/10`, so

`m=m_{d_0}=1/(1560*13^7)`, `rho=m/1484<1/100`.

For every real `L>=1000`, define

`a_{L,u}=s^7+L s^6+12s^5+(99L/10)s^4+44s^3`

`           +(133L/5)s^2+48s+L(177/10+u)`, `0<=u<=1`.

Let `B_L` be the independent box obtained by allowing `|[s^k]v|<=rho`, `0<=k<=6`, in `a_{L,u}+v`. Its seven lower intervals are

`[L±rho]`, `[12±rho]`, `[99L/10±rho]`, `[44±rho]`,

`[133L/5±rho]`, `[48±rho]`, `[177L/10-rho,187L/10+rho]`.

Their independence is literal: the constant interval is the Minkowski sum of the base segment and `[-rho,rho]`. All widths are positive.

Let `E_0=E_{d_0,0}` and use the same fixed `O,D` as §3. The base components are `L(E_0+u),O`; multiplying the even part by `L>0` preserves its roots/signs, so the same strict Hermite–Biehler argument proves base stability.

The outside numerator is

`b_L^outside=sO(-s^2)+(1/(1040L))D(-s^2)`

` =s^7+(1/(260L))s^6+12s^5+(9/(260L))s^4`

`      +44s^3+(11/(130L))s^2+48s+3/(65L)`.                    (17)

Its base pairing is **exactly the same** positivity expression as (M) at `d_0`:

`tO^2+(1/(1040L))D*L(E_0+u)=tO^2+(1/1040)D(E_0+u)`.

Thus the lower bound is `m(1+t)^7`, not a newly independent positivity theorem. Its coefficient sum is `105+176/(1040L)<106`; the seven-coefficient perturbation bound is again `742rho(1+t)^7`. Hence

`P_{p,b_L^outside}>=(m/2)(1+t)^7>0` for every `p in B_L`.

The same nonzero-pairing homotopy proves all full-box denominators Hurwitz. This is an actual strict common monic degree-seven numerator. It lies outside `B_L`, already because `1/(260L)<L-rho` in the `s^6` coordinate.

### 6.2 Every numerator inside the box fails an exact finite obstruction

Suppose `b in B_L`, so write `b=a_{L,theta}+v`, `0<=theta<=1`, `|[s^k]v|<=rho`. A common numerator would have to work for both exact denominators `a_{L,0}` and `a_{L,1}`, which belong to the box.

Take the two exact squared frequencies

`t_1=101/100`, `t_2=11/10`, and `alpha_i=-E_0(t_i)`.

The factorization of `E_0` gives

`alpha_1=97311/1000000`, so `9/100<alpha_1<1/10`,

`alpha_2=114/125`, so `alpha_2>9/10`, `1-alpha_2=11/125>2/25`.

Both frequencies are below2. Thus `|O(t_i)|<=48`, `t_iO(t_i)^2<=4608`. At these nodes, for `j=0,1`,

`|a_{L,j}(i sqrt(t_i))|<=L+96<=2L`.

There are seven perturbation monomials of degree at most six, each at most `8rho` in magnitude, so

`|v(i sqrt(t_i))|<=56rho`, `|P_{a_{L,j},v}(t_i)|<=112Lrho`.

Define

`e_L=4608/L^2+112rho/L`

`    <4608/1000000+112/100000=716/125000<1/100`.                (18)

At the first node, strict pairing against the lower-constant denominator requires

`0<P_{a_{L,0},b}(t_1)`

` =-L^2 alpha_1(theta-alpha_1)+t_1O(t_1)^2+P_{a_{L,0},v}`,

which forces

`theta<alpha_1+e_L/alpha_1<1/10+1/9=19/90<1/4`.

At the second node, strict pairing against the upper-constant denominator requires

`0<P_{a_{L,1},b}(t_2)`

` =L^2(1-alpha_2)(theta-alpha_2)+t_2O(t_2)^2+P_{a_{L,1},v}`,

which instead forces

`theta>alpha_2-e_L/(1-alpha_2)>9/10-1/8=31/40>3/4`.

Contradiction. Thus **no polynomial belonging to the entire plant coefficient box `B_L` is a common numerator**. Since a coefficient box is the convex hull of its vertices, this includes corners, midpoint and every convex mixture of its plant polynomials.

Two exact frequency constraints suffice for this **restricted numerator ansatz** because the displayed uniform estimates prove the contradiction for every `L,theta,v`. This is not a numerical sample being promoted to a universal synthesis claim. Numerator (17) explicitly proves that unrestricted synthesis is still possible for these same boxes.

## 7. Cubic terminal-root control: the precise scope of the failed extrapolation

The actual sextic primary Lemma3.2, including its whole proof, was read again. Its varying odd components are quadratics with both roots in bounded gaps between the three even root bands. Its global scaled quadratic bounds use the completed-square identity(3.9). A septic has three odd roots, the last after the last even root.

For an exact control, fix any `R>20`, take

`E=-(t-1)(t-3)(t-5)=-t^3+9t^2-23t+15`,

and independently vary

`O=-t^3+A t^2-Bt+C`,

`A in[R+6,R+7]`, `B in[6R+8,6R+14]`, `C in[8R,8R+8]`.

Then every member satisfies

`O(1)>=3R-9>0`, `O(3)<=20-R<0`, `O(5)>=3R-45>0`.

Together with its negative leading term, these give one simple odd root in each of `(1,3),(3,5),(5,infinity)`, exactly interlacing the fixed even roots. The full independent coefficient box is therefore Hurwitz by Hermite–Biehler. It contains the endpoint member

`O_R=-(t-2)(t-4)(t-R)`.

Its terminal odd root is exactly `R`, arbitrarily large while the whole even polynomial remains fixed.

**Only the following extrapolation is excluded:** a finite terminal odd-root upper bracket depending on the even-root data alone. Each fixed-R family is compact and has ordinary coefficient-based bounds. The control does **not** exclude comparisons using the actual odd coefficients, an R-dependent terminal scale or another global cubic construction. It has fixed even part, whose synthesizability is already classical; it is an attack record identifying a missing ingredient, not another new solved class or a proof that cubic comparison is impossible.

## 8. Primary-source comparison, novelty and scientific limits

Primary statements actually read:

1. [Wang–Yu, arXiv:math/0202242v1](https://arxiv.org/html/math/0202242v1), Sections1–2 and relevant construction discussion: monic interval formulation, exact equal-degree definition, low-order theorem and existing fixed-parity synthesis. The fixed-parity base examples above are not new unsolved classes.
2. [Xu et al., arXiv:2609.26541v2](https://arxiv.org/html/2609.26541v2), Theorem2.1, Section2, Lemma3.2 with its full proof, Sections5–8: the announced sextic theorem requires a whole robustly Hurwitz independent monic box. It cannot be invoked on the unstable hull in §4 or substituted for the missing correlated-image numerator in §5. Its global quadratic construction is not an arbitrary-order assertion. No Lean build or axiom authentication was performed here.
3. [Bokam et al., Archives of Control Sciences31(2),347–373(2021), doi:10.24425/acs.2021.137422](https://journals.pan.pl/Content/120111/PDF/art06.pdf), actual introduction pp348–349 and Section2.1: instability of reduced interval models from stable interval systems is prior art; that paper uses modified Routh constructions. The specific map (R) is the object obstructed here, not their modified method.
4. [Bianchini–Tesi–Vicino, *Synthesis of robust strictly positive real systems with l2 parametric uncertainty*](https://www3.diism.unisi.it/~giannibi/research/papers/cas2001.pdf), actual introduction, definitions and Theorem1 read: robust stable convex families admit broader rational-filter constructions, with degree questions distinguished explicitly; its ellipsoidal uncertainty result is not an exact-degree-seven polynomial-numerator theorem for interval boxes. This reinforces, rather than removes, the book's degree boundary.

The live quintic README and sextic source, author public repository inventory, local math corpus and live remote openai/math catalogue were screened as recorded in `selection-v1.md`. No matched degree-seven solution was located, but the correct status remains **UNCERTIFIED-CURRENT-OPEN**, not a proof of openness. Generic Routh intervalization failure, fixed-parity synthesis, degree raising and compactification are classical mechanisms. Priority of the exact countercontrol packets is **NOVELTY-UNCLEAR**. Neither shortness nor a search miss grants discovery or publication significance.

## 9. Dependencies and what remains genuinely unproved

Dependency map:

- Classical Hermite–Biehler + elementary identities → pointwise Routh stability and base denominator stability.
- **One shared residue-margin lemma (M)** → strict numerator and full-width homotopy in §4; the same lemma at `d=1/10`, with an explicit parity scale, → strict outside numerator and full-width homotopy in §6.
- Stable septic + **supplied common sextic numerator**, common fixed `c`, compactness → conditional dual lift in §5. This branch does not manufacture the supplied numerator or its uniform margin.
- Elementary exact endpoint signs + the same classical interlacing → the limited terminal-root control in §7.

The original unrestricted target is not narrowed to any of these constructions. In particular, the full-zero/infinity critical supports and arbitrary partial/collapsed radial boundary strata in the old dossier remain unexcluded. No new conclusion is drawn from re-encoding their feasibility conditions.

The next consequential mathematical obligation is a **global cubic comparison/positivity lemma using both the actual odd terminal scale and the interval coefficient-width constraints**, or a true exact positive-dependence obstruction to **all** degree-seven numerators. The Routh branch alternatively requires common synthesis for arbitrary actual correlated sextic images and a genuinely common lift when `[s^6]a` varies. The two obstructions above prevent tempting shortcuts but do not supply any of these missing claims.

**Evidence ceiling:** original Routh and dual/terminal claims have actual separate-agent written reconstructions at their pinned v1 bytes; the plant-box exclusion and this consolidated presentation are still candidates pending their own checks. No parent, formal/kernel, human, external-model or novelty acceptance is claimed. No aggregate theorem, discovery or solved-book count is assigned to these related ingredients.
