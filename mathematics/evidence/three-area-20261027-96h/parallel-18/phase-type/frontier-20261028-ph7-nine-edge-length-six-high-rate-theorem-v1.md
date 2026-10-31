# Length-six connectors force four large diagonal rates at z=8/9

Status: **WRITTEN-checked with an independently implemented exact integer certificate replay**, awaiting independent mathematical review. This eliminates the small-rate branches of the prior joint Perron gap, but does **not** yet exclude the entire length-six graph family, all nine-edge graphs, or PH7 at `8/9`.

## 1. Theorem

For a seven-state row generator whose graph is two vertex-disjoint directed triangles plus a singleton on a six-edge connector cycle, suppose the generator has the target eigenvalue pair `-d +/- ib` with algebraic multiplicity at least two and `b^2/d^2=8/9`. Let `x` be the singleton's diagonal rate, `-r_A` the Perron eigenvalue of the triangle fully visited by the connector cycle, and `a_1,a_2,a_3` that triangle's three diagonal rates. Then

`x>17d/9`, `r_A>17d/9`, and therefore `a_i>17d/9` for all three `i`.

In addition, `max(x,r_A) > d*(1+10*sqrt(2)/9)`.

The final implication to the diagonal rates uses a positive Perron eigenvector and the strictly positive internal transition in each triangle row. These are strict necessary conditions for every graph in this named family; neither their simultaneous feasibility nor the existence of any PH input/exit is claimed.

## 2. Transfer factorization and earlier gap

Scale `d=1`, so `lambda=-1+i*sqrt(8/9)`; conjugation handles the other sign. On each triangle write `C(y)=prod_i(y+r_i)-theta*prod_i r_i`, where the unique connector-departure row sends fraction `theta` to its internal successor and fraction `1-theta` to the connector. Here `r_i>0` and `0<theta<1`. Triangle `A` is fully visited, while triangle `B` has two visited vertices and one omitted rate `t`. Define

`h_A(y)=C_A(0)/C_A(y)`,

`h_B(y)=(1-theta_B)*b_1*b_2*(y+t)/C_B(y)`,

`h_x(y)=x/(y+x)`.

The directed-cycle determinant is `(y+x)C_A C_B-w(y+t)`, and the explicit cycle product gives the exact root identity

`h_x(lambda)*h_A(lambda)*h_B(lambda)=1`.

All denominators are nonzero by the three-state sector lemma `frontier-20261028-ph7-three-state-log-derivative-sector-lemma-v1.md` (SHA256 `c2c30e487654f1d09f3e4d3df2eab19ceb80d21185912564fd8d345551c3944e`). The prior exact joint-gap theorem `frontier-20261028-ph7-nine-edge-length-six-perron-gap-v1.md` (SHA256 `8567a88345a871ded458ebd15b33ac15dee3e71fc8b6c69f01a75ff903de1d26`) yields the two disjunctions

`x<1/9 or x>17/9`, and `r_A<1/9 or r_A>17/9`,

as well as the joint inequality `1/v_x+1/v_{r_A}<81/136`, where `v_s=(s-1)^2+8/9`.

## 3. Three universal 8/9 amplification bounds

For `r_i>0`, `0<=theta<=1`, and `lambda` as above, the following inequalities hold:

1. Full three-state visit: `|(1-theta)*r_1*r_2*r_3/C(lambda)| <= 4`.
2. Two-state visit with omitted `r_3`: `|(1-theta)*r_1*r_2*(lambda+r_3)/C(lambda)| <= 213/100`.
3. For any `h>0` and `0<=v^2<=h^2/3`, `|(h^2+v^2)/[(lambda+h)^2+v^2]| <= 15/4`.

The first two are certified by nonnegativity of explicit rational polynomials. Set `a_i=r_i-1`, `P=r_1*r_2*r_3`,

`R=a_1*a_2*a_3-(8/9)*(a_1+a_2+a_3)-theta*P`,

`I=a_1*a_2+a_1*a_3+a_2*a_3-8/9`, `N=R^2+(8/9)*I^2`.

The respective polynomials are

`16*N-(1-theta)^2*P^2 >= 0`,

`(45369/10000)*N-(1-theta)^2*r_1^2*r_2^2*((r_3-1)^2+8/9) >= 0`.

For the third bound, set `v^2=h^2*eta/3`, `0<=eta<=1`; its squared-modulus inequality is the polynomial nonnegativity

`(225/16)*[((h-1)^2-8/9+h^2*eta/3)^2+(32/9)*(h-1)^2] - (h^2+h^2*eta/3)^2 >= 0`.

For the two triangle polynomials compactify `r_i=u_i/(1-u_i)` and retain `theta=u_4`. The only simultaneous infinite-rate/`theta=1` corner is resolved by four cones: write `e_i=1-u_i`, take one maximal `e_i` as `s`, set each other `e_j=s*v_j`, and divide the compactified polynomial by the common `s^2`. All four resulting polynomials are checked on `[0,1]^4` by exact integer Bernstein subdivision. The full-visit cone covers have `26,26,26,80` leaves; the two-visit covers have `26,26,76,261` leaves. For the third inequality, compactify `h=H/(1-H)` and use an exact 15-leaf two-dimensional Bernstein cover. The four cones cover the entire compact cube; finite positive rates give `s>0`. Nonnegative Bernstein coefficients prove the required nonnegativity, including all finite boundary cases.

Frozen certificate `frontier-20261028-ph7-length-six-amplification-certificate-v1.json` SHA256 `9ee67b08a8da54257e767bb3e69d79de1601bf5e13b11910b9bc6cc308aa6d60`, primary generator `frontier-20261028-ph7-length-six-amplification-certificate.py` SHA256 `0cede31a2322b00f9652fe43311a449296282c29c2d5a33e7a5515ce3a54b077`. A separately implemented stdlib `fractions.Fraction`/integer replay `frontier-20261028-ph7-length-six-amplification-integer-replay.py` SHA256 `37a23906e50b5483cdb03f21b420a060f02968bf06a88e38e538a212e5ccbb06` returned PASS after independently reconstructing the polynomials, comparing their coefficient hashes, and checking full prefix covers and every Bernstein sign. This is independent code replay by the same owner, **not** independent scientific review or formal verification.

For later use, the single-rate bound `|s/(lambda+s)|^2<=17/8` follows directly from `(17/8)*[(s-1)^2+8/9]-s^2=(9/8)*(s-17/9)^2`.

## 4. Excluding both small branches

If `0<s<1/9`, then `|s/(lambda+s)|^2<1/136`. Suppose first `x<1/9`. The root identity and the first two amplification bounds give

`1=|h_x*h_A*h_B|^2 < 16*(45369/10000)/136 < 1`,

a contradiction. Hence `x>17/9`.

Suppose instead `r_A<1/9`. Factor the real Perron root: `C_A(y)=(y+r_A)*C_2(y)`, so

`h_A(lambda)=[r_A/(lambda+r_A)]*[C_2(0)/C_2(lambda)]`.

If the other two triangle eigenvalues are real, the second factor has modulus at most `17/8` by the single-rate bound. If they are `-h +/- iv`, the 3-state Metzler trace-square inequality after shifting the Perron root gives `v^2<=(h-r_A)^2/3<=h^2/3`; the third certified bound gives modulus at most `15/4`. Thus in either case `|C_2(0)/C_2(lambda)|<=15/4`, and

`1=|h_x*h_A*h_B|^2 < (17/8)*(225/16)*(45369/10000)/136 < 1`.

The final exact product is `6941457/51200 < 136`; the gap is `21743/51200`. Hence `r_A>17/9`.

Finally, using the prior joint inequality with both variables above `17/9`, if both were at most `1+10*sqrt(2)/9`, then `v_x,v_{r_A}<=272/81`, so their reciprocal sum would be at least `81/136`, a contradiction. This proves the max bound and, by scaling, the theorem. □

The graph-specific theorem depends on the named sector/joint-gap written results and the above exact certificate. Applying it to all nine-transition critical PH7 candidates further requires the pending nine-edge graph-template and its capacity/overlap-budget chain, plus the supported irreducibility normalization. No stronger independent review, formal verification, numerical witness, ten-edge exclusion, novelty, or complete 8/9 decision is asserted.
