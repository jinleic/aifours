# Candidate v1 — an even-anchor complementary-Euler comparator beyond the failed odd profile

Actual clock observed before creation: **2026-10-24T03:50:07-0700 PDT**. InfoSPR7, info-2. The same-primary freeze is `selection-addendum-v2-even-anchor.md`. **Complete WRITTEN CANDIDATE, pending actual separate reconstruction and parent disposition.** No scientific program, arithmetic interpreter, CAS, solver, enumeration, compilation, model CLI or nested agent was used. The original deadline and universal degree-seven target are unchanged.

## 0. Exact change of mechanism and original-target gap

The earlier supported profile anchored the midpoint **odd** component Q and used `sQ(-s^2)+epsilon(tQ)'(-s^2)`. It fails for every epsilon on the exact stable control with even roots1/2,500,1500. Its budget cannot be repaired into a universal theorem.

Here the anchored component is instead the normalized midpoint **even** cubic F, and its complementary Euler polynomial is

`H_F(t)=4F(t)-tF'(t)`.

The actual numerator is

`b_epsilon(s)=F(-s^2)+epsilon*s*H_F(-s^2)`.                   (1)

This changes the numerator's component/phase profile, not merely the old epsilon or its loss estimate. The proof below gives a direct global certificate allowing **all seven lower coefficients** to vary, and an explicit full-seven-width box containing the old failing control for which(1) works. The old odd profile still fails on that same box for every scalar parameter.

**Not claimed:** this new profile or its sufficient budget is universal. The unrestricted original numerator quantifier remains untouched. The result is a sufficient construction mechanism and a demonstrated escape from the earlier profile barrier, not a solution of universal SPR7, a necessary test, or an obstruction to all unrestricted numerators.

Fixed-even/fixed-odd synthesis is prior art, explicitly in the actual book p681 and Wang–Yu's primary introduction. The sextic paper's fixed-even Lemma2.3 uses an even derivative in its special case. Residues, Euler differentiation and square completion have classical antecedents. The fixed-even specialization below is not a discovery; novelty of the variable-even certificate and precise application is **UNCLEAR**.

## 1. Literal box, pairing and new anchor

Let

`K={a=s^7+a_1s^6+a_2s^5+a_3s^4+a_4s^3+a_5s^2+a_6s+a_7 : l_i<=a_i<=u_i}`,

where all endpoints are finite and `0<l_i<=u_i`. Degenerate intervals are allowed. Endpoint positivity is automatic for a compact robustly Hurwitz monic box, but the sufficient theorem below will prove stability rather than assume it.

Write

`E_a(t)=-a_1t^3+a_3t^2-a_5t+a_7`,

`O_a(t)=-t^3+a_2t^2-a_4t+a_6`,

`P_{a,b}(t)=E_a(t)E_b(t)+tO_a(t)O_b(t)`.

For Hurwitz denominators, positive P on every `t>=0` is exactly the book's strict finite-real-frequency criterion, including zero.

Set `m_i=(l_i+u_i)/2`, `w_i=(u_i-l_i)/2`, and specify

`F(t)=E_mid(t)/m_1=-t^3+f_2t^2-f_1t+f_0`,

`f_2=m_3/m_1`, `f_1=m_5/m_1`, `f_0=m_7/m_1`.

Require that F have three distinct positive roots `r_1<r_2<r_3`. These are **even-anchor roots**, not the old odd-root coordinates. Define the literal odd-component endpoint values

`O_-(r)=-r^3+l_2r^2-u_4r+l_6`,

`O_+(r)=-r^3+u_2r^2-l_4r+u_6`,

and residue endpoints

`beta_j^- =min(-O_-(r_j)/F'(r_j),-O_+(r_j)/F'(r_j))`,

`beta_j^+ =max(-O_-(r_j)/F'(r_j),-O_+(r_j)/F'(r_j))`.

The remaining sign hypothesis is the explicit finite set **`beta_j^->0`**.

For a robustly stable original box these hypotheses hold automatically: its actual midpoint even component can be combined independently with every actual odd component. Hermite–Biehler gives three simple positive even roots and odd signs `+,-,+` at them, opposite the signs `-,+,-` of F'. Compactness makes the residue lower bounds positive. This fact does **not** imply the later sufficient budget.

## 2. Completely specified data and scalar choice

For each even-anchor root put

`a_j=(w_7+w_5r_j+w_3r_j^2+w_1r_j^3)/|F'(r_j)|`,

`alpha_j=r_j^2 beta_j^->0`,

`R_j=2r_j-r_j^2 sum_(k!=j) 1/(r_j-r_k)`,

`d_j=r_j^2[1+sum_(k!=j) beta_k^+/|r_j-r_k|]+beta_j^+|R_j|`.

These are explicit expressions in known box endpoints and roots of its specified even cubic. They do not encode unknown numerator coefficients. Define

`A=(1/2)sum_j a_j^2/alpha_j`,

`B=sum_j a_j d_j/alpha_j`,

`C=u_2+(1/2)sum_j d_j^2/alpha_j>0`.

**Sufficient scalar condition.** Supply an explicit `epsilon>0` such that

`Lambda(epsilon)=A/epsilon+B+C epsilon<l_1`.                  (2)

There is a closed-form selection, not a search:

- if A>0 and `B+2sqrt(A C)<l_1`, choose `epsilon=sqrt(A/C)`;
- if A=0, every even coefficient interval is degenerate, B=0, and `epsilon=l_1/(2C)` works.

The actual theorem permits any explicit epsilon meeting(2), including a conservative rational choice in the application below. The fixed-even case is the classical baseline recovered quantitatively, not a newly selected unsolved problem.

## 3. Positive synthesis theorem

**Candidate theorem.** Under §1's root/residue hypotheses and(2), every member of the original independent box K is Hurwitz, and the one polynomial(1) is a common real **exact-degree-seven** strict SPR numerator. Division by epsilon makes it monic if desired. A positive explicit number mu satisfies

`P_{a,b_epsilon}(t)>=mu(1+t)^7` for every `a in K`, `t>=0`.    (3)

In expanded form,

`H_F=-t^3+2f_2t^2-3f_1t+4f_0`,

`b_epsilon=epsilon s^7+s^6+2epsilon f_2s^5+f_2s^4`

`                +3epsilon f_1s^3+f_1s^2+4epsilon f_0s+f_0`.

Its leading coefficient is epsilon>0, and every choice is fixed across denominators/frequencies. There is no fixed-a_1 assumption. The general coefficients are real; no rational-coefficient claim is made merely because the formulas are explicit.

## 4. Exact global rational identity

Fix an actual denominator. Its residues at the even anchor are

`A_j(a)=E_a(r_j)/F'(r_j)`, `B_j(a)=-O_a(r_j)/F'(r_j)>0`.

Since `E_mid=m_1 F`, the even deviations imply `|A_j(a)|<=a_j`; the odd endpoints give `beta_j^-<=B_j(a)<=beta_j^+`. Polynomial division gives the exact identities

`E_a/F=a_1+sum_j A_j(a)/(t-r_j)`,

`O_a/F=1-sum_j B_j(a)/(t-r_j)`.

The latter has constant1 because both F and O have leading coefficient-1. Let `S=r_1+r_2+r_3=f_2`. Logarithmic differentiation yields

`H_F/F=4-tF'/F=1-sum_j r_j/(t-r_j)`,

`tH_F/F=t-S-sum_j r_j^2/(t-r_j)`.

Its regular part at r_j is exactly R_j from §2. Indeed

`r_j-S-sum_(k!=j) r_k^2/(r_j-r_k)`

` =2r_j-r_j^2 sum_(k!=j) 1/(r_j-r_k)`.

Thus the double-pole coefficient of `tH_F O_a/F^2` at r_j is `r_j^2 B_j(a)>0`, and its simple-pole coefficient is

`Gamma_j(a)=-r_j^2[1-sum_(k!=j) B_k(a)/(r_j-r_k)]`

`                -B_j(a) R_j`,

with `|Gamma_j(a)|<=d_j`.

The polynomial part is **exactly `t-a_2`**, not a bound inferred from even roots. At infinity, the coefficient comparison in `O_a/F=1-sum B_j/(t-r_j)` gives

`sum_j B_j(a)=a_2-S`.

Therefore the product's limiting constant after its leading t is `-S-sum B_j=-a_2`. Matching principal parts and the polynomial part proves

`tH_F O_a/F^2=t-a_2`

`       +sum_j [r_j^2 B_j(a)/(t-r_j)^2+Gamma_j(a)/(t-r_j)]`.  (4)

This identity uses the **actual odd coefficients**. No finite terminal odd-root bound from even data alone has been inserted.

## 5. Square completion proves the entire half-line at once

The actual pairing is

`P_{a,b_epsilon}=F E_a+epsilon tH_F O_a`.

Combining(4) with the even partial fractions, off the three poles,

`P/F^2=a_1+epsilon(t-a_2)`

`    +sum_j [epsilon r_j^2 B_j(a)/(t-r_j)^2`

`                  +(A_j(a)+epsilon Gamma_j(a))/(t-r_j)]`.

For positive gamma, the elementary inequality

`gamma x^2+v x >=(gamma/2)x^2-v^2/(2gamma)`

retains half the positive double-pole mass. Use `a_1>=l_1`, `a_2<=u_2`, the residue lower bounds and the simple-pole absolute bounds. With `F_j=F/(t-r_j)` as an actual quadratic polynomial, this gives

`P_{a,b_epsilon}(t)`

` >=[l_1+epsilon t-Lambda(epsilon)]F(t)^2`

`       +(epsilon/2)sum_j alpha_j F_j(t)^2`.                  (5)

The cost is precisely

`epsilon u_2+sum_j (a_j+epsilon d_j)^2/(2epsilon alpha_j)`

` =A/epsilon+B+C epsilon`.

After multiplying by F² both sides are polynomials, so continuity establishes(5) at the three apparent poles as well. Because(2) makes the first coefficient strictly positive for **every t>=0**, there is no small-frequency gap or need to discard the origin.

The degree-two interpolation identity

`sum_j F_j(t)/F'(r_j)=1`

is exact: both sides agree at three distinct roots and have degree at most two. If

`J=sum_j 1/F'(r_j)^2>0`, `alpha_min=min_j alpha_j>0`,

Cauchy–Schwarz gives `sum F_j^2>=1/J`. Hence(5) proves the uniform positive constant lower bound

`P_{a,b_epsilon}(t)>=epsilon alpha_min/(2J)>0`                (6)

on the **entire** half-line, including zero, every pole and all finite tails. No finite evaluation is used to infer(4) or(5).

For an explicit weighted margin, take `T=max(1,2r_3)`, `m_0=epsilon alpha_min/(2J)`. For t>=T, every `t-r_j>=t/2`, so (5) gives `P>=epsilon t^7/64`; through T, (6) gives P>=m_0. Thus one value in(3) is

`mu=min(m_0/(1+T)^7, (epsilon/64)(T/(1+T))^7)>0`.             (7)

## 6. Actual denominator stability, not cancellation

The sign/residue hypotheses alone show every nominal polynomial `m_1 F(-s^2)+sO_a(-s^2)` Hurwitz: O has signs `+,-,+` at r_1,r_2,r_3 and tends to negative infinity. Its three simple roots therefore lie in `(r_1,r_2),(r_2,r_3),(r_3,infinity)`, strictly interlacing the even roots, with the correct component constants/leading signs.

For an actual member, keep O_a fixed and interpolate the **even** component from E_mid to E_a. The independent closed coefficient box contains this entire path. The strict polynomial bound(5) holds for every point of the path, before any denominator is assumed Hurwitz. An imaginary-axis zero would make its pairing vanish, contradiction. Monicity and bounded path coefficients prevent roots escaping through infinity. Root continuity from the nominal Hurwitz member proves the actual denominator Hurwitz.

Thus(1) is a genuine strict common numerator for the original denominators. Its limiting ratio is epsilon>0; dividing by epsilon normalizes it to a monic degree-seven numerator without changing any sign.

## 7. Explicit full-seven-width application containing the old failed-profile control

Fix **`rho=1/1000`**. Let K_* be the full independent monic box

`a_1 in[1-rho,1+rho]`, `a_2 in[3050-rho,3050+rho]`,

`a_3 in[4001/2-rho,4001/2+rho]`,

`a_4 in[2150000-rho,2150000+rho]`,

`a_5 in[751000-rho,751000+rho]`,

`a_6 in[2000000-rho,198000000+rho]`,

`a_7 in[375000-rho,375000+rho]`.

All seven widths are strictly positive; the linear coefficient has a large interval rather than a small perturbation of a fixed odd component. The normalized even anchor is exactly

`F=-(t-1/2)(t-500)(t-1500)`.

Its derivative values are

`F'(1/2)=-2996001/4`, `F'(500)=499500`, `F'(1500)=-1499500`.

All have absolute value greater than400000. Choose the literal scalar

`epsilon=rho/10000=1/10000000`.

### 7.1 All actual odd residues, including the terminal scale

Before the extra rho perturbations in a_2,a_4,a_6, the odd values on the three F roots have ranges

- at1/2: `[7406099/8,1575406099/8]`;
- at500: `[-435500000,-239500000]`;
- at1500: `[264500000,460500000]`.

The additional odd perturbation at r_j has magnitude at most `rho(r_j^2+r_j+1)`. Even for the larger conservative range rho<=1/100, these are respectively less than1,3000,23000. Dividing with the exact signs of F' therefore gives the valid uniform bounds

`1<=B_1(a)<=300`, `400<=B_2(a)<=900`, `100<=B_3(a)<=400`.       (8)

These include every coefficient choice independently, not merely the old c-endpoints. In particular all required positive residue bounds are verified before stability is concluded.

### 7.2 Even deviations and the exact regular parts

The four independent even half-widths are rho. Directly from the three root values,

`a_1^(res)<=rho/100000`, `a_2^(res)<=300rho`,

`a_3^(res)<=3000rho`.                                        (9)

The superscript distinguishes these residue-error bounds from the plant coefficients. For example their exact ratios are `(15/8)/(2996001/4)`, `125250501/499500` and `3377251501/1499500`, bounded as in(9).

The regular parts R_j in §2 have absolute bounds

`|R_1|<2`, `|R_2|<1000`, `|R_3|<1000`.

To make the cancellations explicit,

`R_1=1+1/(2*999)+1/(2*2999)`,

`R_2=1250-500000/999`,

`R_3=750-4500000/2999`.

The latter two lie respectively between749and750 and between-751and-750. The bounds are not obtained by discarding their cancellation and then treating a large numerical residual as exact.

Using (8), the root gaps and these regular parts in the definition of d_j gives

`d_1<=1000`, `d_2<=2000000`, `d_3<=6000000`,

while the double-pole lower masses are

`alpha_1>=1/4`, `alpha_2>=100000000`,

`alpha_3>=225000000`.                                        (10)

For transparent upper bounds: the first pieces of d_1,d_2,d_3 are respectively less than1,600000,4837500; their remaining pieces are at most600,900000,400000. This proves the displayed conservative integer bounds.

### 7.3 The scalar budget is verified, not assumed

Equations(9)–(10) give

`A<rho^2/40`, `B<100rho`, `C<3000000`.

For the last bound, the inverse-square sum before dividing by2 is at most

`4000000+40000+160000=4200000`,

and `u_2<3051`. For B the exact three upper contributions are `rho/25,6rho,80rho`, summing to less than100rho. For A the bracket before dividing by2 is `rho^2(4/10^10+9/10000+1/25)<rho^2/20`.

At the chosen epsilon=rho/10000,

`Lambda(epsilon)<250rho+100rho+300rho=650rho=13/20`

`                  <999/1000=l_1`.

Every hypothesis of the direct global theorem is therefore verified for this **complete independent seven-width box**. This is not a claimed sufficiently-small perturbation with no actual radius.

### 7.4 Literal common numerator and margin

Here

`H_F=-t^3+4001t^2-2253000t+1500000`.

An explicit monic common numerator is `B_*(s)=b_epsilon(s)/epsilon`, namely

`B_*(s)=s^7+10^7s^6+4001s^5+(4001/2)*10^7s^4`

`           +2253000s^3+751000*10^7s^2+1500000s+375000*10^7`.  (11)

All data and coefficients in this literal example are rational numbers. The polynomial is independent of every plant coefficient.

For an exact simple margin, (8)–(10) give alpha_min>=1/4 and `J<3/(400000^2)`, so (6) gives the raw pairing a constant lower bound greater than `2000/3>1`. With `T=3000`, the raw tail is at least `epsilon t^7/64`. Since `3000^7>=64*10^7`, the compact/tail comparison proves

`P_{a,b_epsilon}(t)>=[1/(3001^7)](1+t)^7`,

`P_{a,B_*}(t)>=[10^7/(3001^7)](1+t)^7>0`                     (12)

for every actual a in K_* and every t>=0. The even-interpolation homotopy in §6 proves every denominator strictly Hurwitz. Both denominator and common numerator have exact degree seven.

## 8. The old profile still fails on this very same full-width box

K_* contains the previously used exact lower-endpoint denominator with fixed even F and

`O_low=-t^3+3050t^2-2150000t+2000000`.

Its midpoint odd component is still

`Q_old=-(t-50)(t-1000)(t-2000)`.

Indeed the new odd intervals are symmetric around the same three midpoint coefficients. Thus the old profile is still `sQ_old+eta(tQ_old)'`, with its scalar eta entirely unrestricted.

For completeness the same exact isolator applies:

`D_old=(tQ_old)'=-4t^3+9150t^2-4300000t+100000000`,

`D_old(20)=17628000>0`, `D_old(30)=-20873000<0`,

and `D_old'<0` throughout[20,30]. Let tau be its unique root there. Q_old is positive and decreasing on that interval, with `Q_old(20)=58212000<98000000`. Therefore

`O_low(tau)=Q_old(tau)-98000000<0`.

The old profile has pairing

`tau Q_old(tau) O_low(tau)<0`

at tau for **every real eta**. The newly added seven widths do not remove this denominator, so they cannot repair the old profile.

The new construction(11) has the strictly positive global bound(12) on the same box. It is not a rescaling or parameter change in the old profile: its odd component is proportional to H_F, whose t² coefficient is4001, while Q_old's is3050 and both have leading coefficient-1. This is an actual component/profile change, not an improvement of the old budget constants.

## 9. Scientific limits and required reconstruction

This proves a different positive comparator mechanism and a full-width application outside the earlier profile's reach, **subject to actual verification of these candidate bytes**. It does not prove that every robustly stable interval box meets(2), that this even-midpoint profile is universal, or that failure of its budget excludes unrestricted numerators. We do not propose that merely tightening this new scalar budget would by itself solve the full problem.

The actual odd terminal data enter u_2 and the full O/F residue intervals in(4)–(5). These may grow as terminal odd scales grow; epsilon is selected from those actual finite data. No upper terminal-root bracket derived from even roots alone is assumed. The proof is direct in the original monic box; it does not apply a monic theorem to an invalid independently normalized reciprocal family.

No prior review or parent disposition is inherited by this manuscript. The earlier written support concerns different pinned profiles. Separate reconstruction must check the complementary-Euler polynomial part `t-a_2`, all double/simple pole coefficients, the shared common-denominator quantifier, both exact endpoint limits, the even-homotopy stability proof, all rational bounds in §7, and coexistence of the new positive and old negative pairings on the same literal box. Standard Hermite–Biehler, elementary partial fractions/interpolation, Cauchy–Schwarz and root continuity are named classical imports; no sextic existence/Lean result is needed.

The original universal degree-seven question and the book's all-order question remain unresolved. Novelty/significance are UNCLEAR; the classical fixed-even specialization and shared positive-real machinery must not be counted as new discoveries. No mathematical executable, formal/kernel check, outside-model/human review, publication or new scientific GO occurred.
