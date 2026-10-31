# Exact omitted-rate obstruction for every nine-edge connector shape

Status: **WRITTEN-checked-in-kernel / stdlib Fraction coefficient replay**, pending independent mathematical audit. This strengthens the graph-specific spectral exclusion in `frontier-20261028-ph7-nine-edge-hamiltonian-cycle-exclusion-v1.md` without assuming any initial or exit vector. It does **not** exclude the whole nine-edge family, ten-or-more-edge graphs, or PH7 at `z=8/9`.

## 1. Statement

Let `G` be an irreducible seven-state row generator whose nine positive off-diagonal edges consist of two vertex-disjoint directed 3-cycles `A,B`, and three connector edges cyclically joining `A` to `B`, `B` to the singleton `x`, and `x` to `A`. Let the connector's return through a triangle visit one, two, or all three of that triangle's vertices. A vertex of a triangle is **omitted** when it is not visited by the connector cycle. Write `u_v=-G_vv>0` for the diagonal rate.

Suppose `G` has a repeated eigenvalue `-d+ib`, where `d>0` and `b^2/d^2=8/9`. Then at least one of the following holds:

* A triangle has exactly one omitted vertex `v` with `u_v < 2d`.
* A triangle has exactly two omitted vertices `v,w` with `min(u_v,u_w) < 3d`.

In particular the Hamiltonian connector, with no omitted vertices, is impossible. For connector length 6 the unique omitted vertex must satisfy `<2d`; for length 5 with one omitted vertex in each triangle, at least one of those rates must be `<2d`; for length 5 with two omissions in one triangle, at least one omitted rate in that triangle must be `<3d`. Lengths 3 and 4 have the corresponding mixed necessary disjunction, not a full exclusion.

## 2. Shared logarithmic-derivative notation

Scale all rates by `d`, and let `y=-1+i*sqrt(8/9)`. For positive `r,s,t` and `0<=theta<=1`, define

`C(y)=(y+r)(y+s)(y+t)-theta*r*s*t`,

`v_r=(r-1)^2+8/9`, with `v_s,v_t` similarly, and

`N=-Im(C'(y)*conj(C(y)))/sqrt(8/9)`.

The full-block lemma in the Hamiltonian manuscript proves `C(y)!=0` and `Im(C'/C)<0` for every such block (in fact for every squared ratio at least `3/4`). It uses a smoothing inequality and a positive five-coefficient Bernstein representation, and is imported here at its explicit written, not independently reviewed, status.

We now pay for the one- and two-omission cases. All subsequent identities were independently coefficient-checked by `frontier-20261028-ph7-nine-edge-log-derivative-fraction-check.py` (SHA256 `e1532f4ac4e22a09bba6804e7c8ad36b81349b0e0fed48d6844f3f63dc650817`): exact `fractions.Fraction` multivariate coefficient dictionaries, not floating evaluations. Its run returned PASS for the stated identities and the full-block Bernstein coefficients.

## 3. One omitted rate at least 2

For the one-omission block the relevant factor is `C(y)/(y+t)`, so

`-Im(C'/C - 1/(y+t))/sqrt(z) = M/(|C|^2*v_t)`,

where `z=8/9` and `M=N*v_t-|C|^2`. In fact the following identity holds for every `z>0`. Set `R=r-1`, `S=s-1`, `T=t-1`, and `v_t=T^2+z`. Then

`M=(R^2+S^2+2z)*v_t^2 + 2*theta*r*s*t*T*(T+R)*(T+S) - theta^2*r^2*s^2*t^2`.

If `t>=2`, then `T>=1`, `T+R=t+r-2>=r`, and `T+S>=s`. Therefore the last two terms together are at least

`theta*r^2*s^2*t*[2*(t-1)-theta*t] >= theta*r^2*s^2*t*(t-2) >= 0`.

The first term is strictly positive. Thus `M>0`, which also proves `C(y)!=0` (if it vanished, both `N` and `M` would vanish), and the imaginary logarithmic derivative of `C(y)/(y+t)` is strictly negative. The one-omission lemma actually holds for any positive squared frequency and omitted rate `t>=2` in this normalization.

## 4. Two omitted rates at least 3, at z=8/9

For the two-omission block use `C(y)/((y+t)(y+u))` with the visited rate `r`. With

`v_t=(t-1)^2+8/9`, `v_u=(u-1)^2+8/9`,

its negative imaginary logarithmic derivative, after multiplication by the positive denominator `|C|^2*v_t*v_u`, has numerator

`M_theta = N*v_t*v_u - |C|^2*(v_t+v_u)`.

This polynomial is concave in `theta`, and exactly

`M_theta=(1-theta)*M_0 + theta*M_1 + theta*(1-theta)*r^2*t^2*u^2*(v_t+v_u)`,

with `M_0=v_t^2*v_u^2>0`. To prove `M_1>0` for `t,u>=3`, put `T=t-3`, `U=u-3`, `H=T+U`, and `V=T*U`. Direct expansion gives

`M_1 = v_t^2*v_u^2 + (2*r*t*u/81)*P_1(H,V) + (r^2*t*u/81)*P_2(H,V)`,

where

`P_1 = 162H^3 + 243H^2 V + 1296H^2 + 81H V^2 + 1620H V + 2240H + 405V^2 + 1800V + 528`,

`P_2 = 81H^3 + 81H^2 V + 891H^2 + 810H V + 3060H + 2250V + 1672`.

Every coefficient is strictly positive and `H,V>=0`, so `M_1>0`. Concavity then gives `M_theta>0` for the entire closed interval `0<=theta<=1`. As in §3, this also excludes `C(y)=0`; hence the relevant logarithmic derivative is strictly negative.

## 5. Determinant and conclusion

For each triangle let `C_A,C_B` be the polynomials of §2 with their respective normalized diagonal rates and `theta` equal to directed-triangle edge product divided by the product of its three diagonal rates. The row-generator property and the positive connector departures give `0<theta<1`. Let `E_A,E_B` be the products of `(y+u_v)` over the vertices omitted from the respective triangles. The exact directed-cycle determinant expansion is

`det(y I-G) = (y+x)*C_A(y)*C_B(y) - w*E_A(y)*E_B(y)`,

where the positive `w` is the product of the connector cycle's transition rates. Its simple cycles are exactly the two triangles and the connector cycle; the two triangles are the only nonempty disjoint pair. Every denominator `(y+u_v)` is nonzero.

At a hypothetical repeated root of the determinant, the product is nonzero and

`(y+x)*(C_A/E_A)*(C_B/E_B)=w`,

`0 = 1/(y+x) + (C_A'/C_A - E_A'/E_A) + (C_B'/C_B - E_B'/E_B)`.

The singleton term has negative imaginary part. If a triangle omits no vertices, §2 gives a negative block term. If it omits one and that rate is at least 2, §3 gives a negative block term. If it omits two and both rates are at least 3, §4 does the same. If every omitted rate satisfied its applicable threshold, all three imaginary parts would be strictly negative, a contradiction. Scaling back by `d` gives §1.

The critical PH7 application is conditional on the separate `frontier-20261028-ph7-critical-nine-edge-graph-template-v1.md` and its pending triangle-capacity/overlap-budget chain; the spectral result for this explicitly described graph stands independently of that reduction. No selected generator, computational search, parent adoption, formal verification, novelty, original PH7 decision, or ten-edge conclusion is asserted.
