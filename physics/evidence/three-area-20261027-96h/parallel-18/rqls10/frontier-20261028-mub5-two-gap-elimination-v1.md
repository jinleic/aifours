# Exact two-gap elimination for the 5D rank-two MUB problem

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at exact example check: **Wed Oct 28 19:20:39 PDT 2026**. This is a necessary-and-sufficient reparameterization of the THREE-FLAT-DIAGONAL projector subproblem, not yet of the additional X/Y cross-phase gates or of all QLS10s. It supplies a concrete all-continuous replacement for root-alphabet searches.

## 1. Setup and exact iff statement

Let `omega=exp(2*pi*i/5)` and let I,U,V be the 5D bases of `frontier-20261028-mub-triple-rank2-reduction-v1.md` SHA **ef00b5db269a3e436365b4b98fd486c32836bbda931f00bba80afcaaea5dfc8c**. Fix ANY five unit phases z_t such that

`sum_t z_t=0`, `w_t=1+z_(t+1)/z_t != 0` for every t.        (1)

Indices are in F5. Define `w2_t=1+z_(t+2)/z_t`,

`d_j=(1/5)sum_t |w_t|² omega^(-j t)`, j=0,1,2.

**Claim:** there exist flat orthonormal a,b∈C5 with `b_t/a_t=z_t` and P=aa†+bb† having diagonal2/5 in I,U,V if and only if there exist complex c1,c2,c4 such that

`|c1|²+|c2|²+|c4|²=d0`,
`c2 conjugate(c1)=d1`,
`c1 conjugate(c4)+c4 conjugate(c2)=d2`,                     (M)

and, defining

`y_t=c1 omega^t+c2 omega^(2t)+c4 omega^(4t)`,
`R_t=y_t y_(t+1) w2_t/(w_t w_(t+1))`,

both exact gap-two equations hold:

`sum_t R_t=0`, `sum_t R_t omega^(4t)=0`.                   (R)

All equations are exact complex equalities; no vector reconstruction, positive definiteness, nonzero coefficient or genericity is silently assumed. If any pair of z phases is antipodal, the remaining three sum to zero and form an equilateral triple; the separately pinned geometric proof `frontier-20261028-mub-all-root-ratio-obstruction-v1.md` SHA **3fac11c5e6f334f543de33bf934b89292df03aba18643efd63659e96fbcd8419** rules out flat P. Thus modulo that independently reviewable geometric result, condition w_t!=0 loses no possible flat-P solution.

## 2. Proof of necessity and sufficiency

Given such a,b, put p_t=sqrt(5)*a_t, so |p_t|=1 and b_t=z_t p_t/sqrt(5). Then

`y_t=5 P_(t+1,t)=p_(t+1) conjugate(p_t) w_t`.

Flat U,V diagonals give `sum y_t=0` and `sum y_t omega^(2t)=0`, hence y's Fourier support is `{1,2,4}`. Its squared moduli equal |w_t|². Taking the zeroth, first and second Fourier coefficients yields precisely (M); the remaining coefficients are conjugates.

For gap2, the actual `5 P_(t+2,t)` equals

`(p_(t+1)/p_t)*(p_(t+2)/p_(t+1))*w2_t=R_t`.

Flat U,V require its Fourier sums at indices0 and -4 to vanish, i.e. (R). Thus (M),(R) are necessary.

Conversely suppose (M),(R). Fourier inversion of the five squared magnitudes gives `|y_t|²=|w_t|²` for every t, so `q_t=y_t/w_t` has unit modulus. Replacing all c's by a common phase rho multiplies every q_t by rho and every R_t by rho², preserving (M),(R). Choose rho with `rho^5=(product_t q_t)^(-1)`. The rescaled q_t multiply to1, so starting with p0=1 and recursively setting `p_(t+1)=p_t q_t` defines a consistent periodic unit phase vector. Put `a_t=p_t/sqrt(5)`, `b_t=z_t p_t/sqrt(5)`.

Their norms are1 and `<a,b>=sum z_t/5=0`, so P is an actual rank-two orthogonal projector. I-diagonal flatness is immediate. For gaps h1,h2, construction gives the required two Fourier zeros; gaps h3,h4 follow from Hermiticity by conjugating and shifting indices. These vanishings are equivalent to the flat U,V diagonals. Thus the conditions are sufficient.

## 3. Optional scalar chart and exact boundary handling

If c1!=0, use the global phase gauge c1=sqrt(x)>0 and define `C=c4 sqrt(x)`. Then c2=d1/sqrt(x), and (M) is exactly

`x*d2 = x*conjugate(C)+conjugate(d1)*C`,
`x*d0 = x²+|d1|²+|C|²`.                                  (4)

Set `Y_t=x omega^t+d1 omega^(2t)+C omega^(4t)`; y_t=Y_t/sqrt(x), so (R) is equivalent to the SAME two sums with

`R_t=Y_t Y_(t+1) w2_t/(w_t w_(t+1))`.

If additionally `x² != |d1|²`, equation (4) gives the explicit rational coefficient

`C=x*(d1*d2-x*conjugate(d2))/(|d1|²-x²)`.                  (5)

Let `S=x+|d1|²/x`. The norm equation then implies the REAL CUBIC

`(d0-S)*(S²-4|d1|²)-|d2|²*S+2 Re(d1*d2²)=0`,
`2|d1|<=S<=d0`,                                            (6)

and x is a positive root of `x²-S*x+|d1|²=0`. One must still impose BOTH complex gap-two equations; the cubic alone is only necessary. These equations provide a finite scalar chart for generic z, and can be cleared of their explicitly nonzero denominators for resultant/interval analysis.

Do NOT divide by `|d1|²-x²` on its zero locus: use (4). If c1=0, then d1=0. When c2!=0, gauge `c2=sqrt(x)`, set `c4=d2/sqrt(x)`, and require `x*d0=x²+|d2|²` plus (R). If c1=c2=0, require d1=d2=0 and `|c4|²=d0`, then check (R). Thus the iff formulation (M),(R) covers these singular cases and the scalar chart has an explicit separate treatment for each.

## 4. Exact nonvacuous example, no target witness

Let `z_t=omega^(3t)` and `p_t=omega^(3t²)`. These are the two-column rank-two WH projector from `frontier-20261028-mub-triple-rank2-reduction-v1.md`. Here

`y_t=omega^(t+3)*(1+omega³)`, `c1=omega³*(1+omega³)`, `c2=c4=0`,
`d1=d2=0`, `d0=|c1|²`,

and the gap-two vector is `omega^(2t+2)*(1+omega)`, whose two required Fourier sums vanish. Independent exact `frontier-20261028-gap-reconstruction-check-v1.py`, SHA **19962a8f04b7b003f0909e607ec41f0f0e61cd498c6b24833c9507b918d900b1**, verifies these identities in Q(omega). This P is real physical and flat in all three bases, so (M),(R) are not a vacuous contradiction. The example nevertheless FAILS the additional X/Y cross-phase gates, as separately proved in the rank-two packet; it is NOT a common unbiased 10-vector and NOT a QLS witness.

## 5. Remaining original gap

The continuous z phases in (1) have two real shape parameters modulo common phase after `sum z=0`; no root-of-unity restriction is assumed. Next one may eliminate x,C from (4),(R), including the singular charts, or derive certified analytic bounds, then impose the full 5D cross-phase gates. No exhaustive resultant, all-irrational no-go, exact target vector, peer review, formal proof or novelty clearance is claimed.
