# A strict omitted-rate bound for the 2+2 length-five connector

Status: **WRITTEN with imported exact integer-replayed amplification certificates**, awaiting independent mathematical review. This applies to the length-five connector shape that visits **two vertices of each triangle**. It does not exclude that graph, the two 3+1 length-five shapes, or PH7 at `8/9`.

## Theorem

Let a seven-state row generator have the two-disjoint-triangle/singleton connector graph, with connector visiting two vertices of each triangle (cycle length five). Let `t_A,t_B` be the two omitted triangle-vertex diagonal rates. If the generator has the target pair `-d +/- ib` with algebraic multiplicity at least two and `b^2/d^2=8/9`, then

`min(t_A,t_B) < 24d/13`.

More precisely, for at least one of the two omitted rates `t`, the Perron decay `rho` of its own triangle block satisfies `rho+t<2d`, and that same omitted rate satisfies `t<24d/13`.

## Proof

Scale `d=1` and take `lambda=-1+i*sqrt(8/9)`. Let `C_A,C_B` be the two triangle characteristic polynomials, `-rho_A,-rho_B` their Perron roots, and `x>0` the singleton diagonal rate. Each induced triangle block is an irreducible Metzler subgenerator with a strict leak row, so `0<rho_A<t_A` and `0<rho_B<t_B`.

The exact directed-cycle determinant is

`P(y)=(y+x)*C_A(y)*C_B(y)-w*(y+t_A)*(y+t_B)`,

with connector-cycle product `w>0`. At the repeated nonreal root, logarithmic differentiation and the three-state full/real-root-quotient sector lemma of `frontier-20261028-ph7-three-state-log-derivative-sector-lemma-v1.md` (SHA256 `c2c30e487654f1d09f3e4d3df2eab19ceb80d21185912564fd8d345551c3944e`) give

`[1/v_{t_A}-1/v_{rho_A}]+[1/v_{t_B}-1/v_{rho_B}] > 0`,

where `v_s=(s-1)^2+8/9`. At least one bracket is positive; relabel that block `B`. Since `rho_B<t_B`, this implies `rho_B+t_B<2`, and in particular `t_B<2`.

If `t_B<=1`, the stated `24/13` bound is immediate. Otherwise `1<t_B<2` and `rho_B<2-t_B<1`. The positive scalar function `s -> |s/(lambda+s)|` is strictly increasing on `[0,1]`. Since the denominators for `s=2-t_B` and `s=t_B` agree,

`|[rho_B/(lambda+rho_B)]*[(lambda+t_B)/t_B]| < (2-t_B)/t_B`.

Write the full triangle polynomial as `C_B(y)=(y+rho_B)*B_2(y)`. The first-passage factors give the root identity

`1=|h_x(lambda)*h_A(lambda)*h_B(lambda)|`,

`h_x(y)=x/(y+x)`, `h_B(y)=[rho_B/(y+rho_B)]*[B_2(0)/B_2(y)]*[(y+t_B)/t_B]`,

and `h_A` is the two-visited-vertex triangle factor. The exact amplification bounds established in `frontier-20261028-ph7-nine-edge-length-six-high-rate-theorem-v1.md` (SHA256 `ecf238ccecf36369a614287579a19d6090a4093b6dbe760504d2ea408562da39`) give

`|h_x|<=sqrt(17/8)`, `|h_A|<=213/100`, `|B_2(0)/B_2(lambda)|<=15/4`.

For the last bound, if the two remaining block roots are real apply the one-rate bound twice; if they are nonreal the three-state trace-square inequality gives `v^2<=(h-rho_B)^2/3<=h^2/3`, exactly the domain of the cited quadratic certificate. The square of the product of the three displayed constants is `6941457/51200<136<144`, so their product is less than 12. Consequently

`1 < 12*(2-t_B)/t_B`, hence `t_B<24/13`.

Rescaling restores `d`. The certificate's exact finite cone/interval Bernstein covers and the separately implemented stdlib integer replay are pinned in the cited high-rate theorem; their replay is independent code by the same owner, not independent scientific review. The path from this graph-specific theorem to all nine-transition PH7 candidates additionally requires the pending template/capacity/overlap chain and the separately supported Perron normalization. No selected state, numerical exclusion, formal verification, novelty, parent adoption, or complete 8/9 decision is claimed.
