# Positive consolidation appendix v2 — explicit full-width application of the cubic budget

Observed before creation: **2026-10-23T14:53:37-0700**. InfoSPR7, same info-2 target. **CANDIDATE, unreviewed.** This v2 incorporates the general positive certificate/proof **by immutable reference**, without changing it:

`consolidated-v2-positive-addendum-v1.md`, SHA256 **`be9631c3dae51e4342fb192b932608c43ae6ba954e82cc7d0c2c9ad657fae172`**.

Read that complete v1 first; equations below invoke its exact global comparison(5), small-frequency bounds and stability homotopy. This adds one explicit positive application, not a fourth obstruction, a second problem or a discovery count. It also makes concrete what the positive budget purchases. No executable scientific calculation or search was used.

## 1. Full seven-width boxes and actual rational numerator

Fix the literal rational width **`rho=1/1000000`**. For every real `L>=1000`, define the independent monic septic box `K_L` by

`[s^6]a in[L-rho,L+rho]`, `[s^5]a in[12-rho,12+rho]`,

`[s^4]a in[99L/10-rho,99L/10+rho]`, `[s^3]a in[44-rho,44+rho]`,

`[s^2]a in[133L/5-rho,133L/5+rho]`, `[s]a in[48-rho,48+rho]`,

`[1]a in[177L/10-rho,187L/10+rho]`.

All seven lower widths are positive and independent. This width is **not** the much smaller `m/1484` frozen in the older plant-box candidate; the following positive proof is new and does not assume the earlier margin is enough at this larger width.

The midpoint odd comparator is exactly

`Q=-(t-2)(t-4)(t-6)=-t^3+12t^2-44t+48`.

Choose the explicit scalar

`epsilon=13rho/(8L)=13/(8000000L)`.

The common numerator to be proved is

`b_L=sQ(-s^2)+epsilon(tQ(t))'|_(t=-s^2)`

` =s^7+(13/(2000000L))s^6+12s^5+(117/(2000000L))s^4`

`      +44s^3+(143/(1000000L))s^2+48s+78/(1000000L)`.          (1)

It is real, monic, exact degree seven and independent of denominator/frequency. We prove every denominator Hurwitz and strict pairings for the entire box, including all frequencies, not just a sample.

## 2. Uniform residue and pole-budget bounds

Represent each even component as

`E_a=L(E_0+u)+delta E`, `0<=u<=1`,

`E_0=-(t-1)(t-3)(t-59/10)`,

where the four even coefficient perturbations defining `delta E` have absolute value at most `rho`. The constant-interval representation is a Minkowski sum and covers the full box.

At `r=(2,4,6)`, `Q'=(-8,4,-8)`. Without `delta E`, the residue lower bounds are respectively

`(29/80)L`, `(57/40)L`, `(1/16)L`,

and every upper bound is at most `(67/40)L`. At a node `r_j`, the residue perturbation has magnitude at most

`rho(1+r_j+r_j^2+r_j^3)/|Q'(r_j)| <=33rho`.

Since `L>=1000` and `rho<1/100`, the exact residue intervals therefore satisfy

`A_j^- >= L/16-33rho >= L/32>0`,

`A_j^+ <=67L/40+33rho <=2L`.                                 (2)

This verifies the nominal-interlacing premises of the imported positive certificate; it does not assume full-box stability.

The constants `H_j` in that certificate are `1/2,2,13/2`, so `|H_j|<=7`. The root gaps are at least2, `r_j<=6`, and `u_1=L+rho<=2L`. Hence its uniform simple-pole bounds obey

`b_j<=14L+12L+12L<=40L`.

Also

`alpha_j=r_j A_j^->=L/16`,

`k_j=r_j rho(r_j^2+r_j+1)/|Q'(r_j)|<=65rho`,

and the odd leading-deviation bound is `w_2=rho`.

Although the v1 statement provides an optimizing scalar choice, its proved global comparison(5) is valid for **any positive** epsilon whose explicit `Lambda` is small enough. With the literal epsilon in §1,

`epsilon*40L=65rho`,

`2epsilon alpha_j>=2[65rho/(40L)](L/16)=13rho/64`.

Thus each loss term has the exact upper bound

`(k_j+epsilon b_j)^2/(2epsilon alpha_j)`

` <=(130rho)^2/(13rho/64)=83200rho`.

Consequently

`Lambda=w_2+sum_j (k_j+epsilon b_j)^2/(2epsilon alpha_j)`

`        <=249601rho=249601/1000000`.                          (3)

There is no root/sample fit or solver status in these bounds.

## 3. The small-frequency endpoint is explicitly 8/31

For this box, the endpoint `t_0` defined in the positive certificate is exactly `8/31`. Indeed

`l_7>=17L`, `u_5<=27L`, `u_1<=2L`,

so its even-component quotient is at least `17/60>8/31`. Also `l_6>=47`, `u_4<=45`, so its odd-component quotient is at least `47/94=1/2`. Finally `q_0=48`, `q_1=44` give

`q_0/[2(5+2q_1)]=48/186=8/31`.

The minimum with1 is therefore `t_0=8/31`. The budget is strictly satisfied because

`249601/1000000<8/31`,

as the exact cross-products are `7737631<8000000`. Thus the supplied global comparison proves strict pairings for the actual rational numerator(1), and the supplied nominal-Q homotopy proves every denominator in the full box Hurwitz. The varying `s^6` coefficient causes no gap in this direct construction.

## 4. An explicit whole-half-line margin

Here `J=sum 1/Q'(r_j)^2=3/32`, and (2) gives `alpha_min>=L/16`. Therefore the positive certificate's large-frequency constant bound is at least

`epsilon alpha_min/(2J)>=13rho/24`.

The small-frequency bound is at least

`epsilon q_0 l_7/4 >=[13rho/(8L)]*48*17L/4`

`                         =663rho/2 >13rho/24`.

Its tail cutoff is `T=max(2,2r_3)=12`, and its tail pairing is at least `t^7/128`. The same compact/tail comparison therefore gives the literal rational uniform margin

`P_{a,b_L}(t) >= [rho/(24*13^6)](1+t)^7>0`

for every `a in K_L` and every `t>=0`. For the tail comparison, `rho<1/100` implies `13rho/24<1/128<=12^7/128`. Zero and the three roots of `Q` are included by the complete imported proof, not removed from the domain.

## 5. Relation to the earlier plant-box obstruction

The old two-frequency numerator-in-the-plant-box exclusion used only `L>=1000` and `rho<1/100` in its negative estimates. It therefore applies unchanged to these larger-width boxes: the two exact nodes `101/100` and `11/10` force a numerator's plant coordinate simultaneously below `1/4` and above `3/4`. Formula(1) lies outside the box, already in its `s^6` coefficient, and is the explicitly constructed common numerator.

This is the **same restricted ansatz obstruction**, not an additional result to count. The positive point of the present application is that its rational full-width construction follows directly from the new general cubic budget; it no longer depends on hoping that the old tiny thickening radius can be enlarged. The earlier plant-box v1 remains the queued review pin at its own exact smaller width. Review coverage of that old packet does not automatically authenticate this strengthening or the new positive-budget proof.

## 6. Scientific boundary and review request

This is still a special explicit continuum, not all robustly stable interval boxes. It demonstrates a concrete nonempty positive regime for the general direct certificate, using actual odd roots/terminal scale and allowing the second septic coefficient to vary. The universal missing comparison remains proving an adequate cubic positivity mechanism for **arbitrary** robustly stable interval boxes, not merely these near-fixed-odd families.

Dependency is explicit: the full general positive proof at pin `be9631c3...` plus the parameter bounds above. Neither is yet independently reconstructed. No sextic existence or Lean theorem, scientific execution, formal/kernel acceptance or novelty clearance is imported. Fixed-parity robustness, residues and square completion have classical precedents; publication significance and priority remain UNCLEAR. This is a positive consolidation/application, not another solved-book claim.
