You are an independent mathematical collaborator. Work only from this prompt (no files, no web,
no tools needed, no further delegation). Be rigorous; label anything unproved as such.

## Problem (open; do not claim a solution without a complete proof)
Monic interval box of degree n: K = {s^n + a_1 s^(n-1) + ... + a_n : l_i <= a_i <= u_i}.
For real p(s) write p(iw) = E_p(t) + i w O_p(t), t = w^2, E_p(t) = sum_l (-1)^l p_{2l} t^l,
O_p(t) = sum_l (-1)^l p_{2l+1} t^l (p_k = coefficient of s^k). Pairing P_{a,b}(t) = E_b E_a + t O_b O_a
= Re(b(iw) conj a(iw)). For a box, E_- <= E_a <= E_+ and O_- <= O_a <= O_+ on t >= 0 with four
Kharitonov corners (E_+/-, O_+/-); widths W_E = E_+ - E_-, W_O = O_+ - O_- have NONNEGATIVE
t-coefficients (they are sums of coefficient-interval lengths times t^l). Conjecture (book, open for
n >= 7): every robustly Hurwitz box has b with deg b = n and P_{c,b}(t) > 0 for all t >= 0 and all
four corners c. It is known (closed-to-strict transfer) to be equivalent to: every box on the
first radial stability boundary has a NONZERO b, deg b <= n, with P_{c,b} >= 0 on [0,inf) for all
corners ("closed numerator").

## The most constrained stratum: fully-closed boxes, n = 7
Points 0 < x0 < x1 < ... < x6. Bands: E1=[x0,x1], O1=[x1,x2], E2=[x2,x3], O2=[x3,x4], E3=[x4,x5],
O3=[x5,x6]. Components (written lead * prod (r - t)):
  E_- = L_- (x0 - t)(x3 - t)(x4 - t),   E_+ = L_+ (x1 - t)(x2 - t)(x5 - t),   L_- >= L_+ > 0,
  O_- = (x1 - t)(x4 - t)(x5 - t),        O_+ = (x2 - t)(x3 - t)(x6 - t).
Box conditions = nonnegative t-coefficients of W_E = E_+ - E_- (degree 3) and W_O = O_+ - O_-
(degree 2). The four corners are marginally stable: corner (+,-) vanishes at x1 and x5,
(+,+) at x2, (-,+) at x3, (-,-) at x4 (both components vanish there); otherwise Hurwitz.
Closed numerators b must satisfy the five double-contact conditions P_c(x_j) = P_c'(x_j) = 0 for the
touching corner, i.e. E_b(x_j) + r_j O_b(x_j) = 0 with r_j = x_j O_c'(x_j)/E_c'(x_j), sign r_j =
(-1)^(j+1); these have rank exactly 5, leaving a 3-dimensional kernel of b's.
Binding (extreme-angle) corners: on [0,x0]: (+,-),(-,+); E1: (+,-),(-,-); O1: (+,-),(+,+);
E2: (+,+),(-,+); O2: (-,+),(-,-); E3: (-,-),(+,-); O3: (+,-),(+,+); [x6,inf): (+,-),(-,+).
So it suffices that P_{+-} >= 0 on [0,x2] u [x4,inf), P_{-+} >= 0 on [0,x0] u [x2,x4] u [x6,inf),
P_{++} >= 0 on [x1,x3] u [x5,x6], P_{--} >= 0 on [x0,x1] u [x3,x5], with the forced double roots.
On each interior band the SPR corridor for arg b(iw) is exactly between (phase of the left
touching corner's cofactor + pi/2) and (phase of the right touching corner's cofactor + pi/2).

## Facts established (do not re-derive)
* Any closed numerator is Hurwitz up to a factor s; its component roots interlace with the band
  points: one E-root in (0,x1), one O-root in (x1,x2), E-root in (x2,x3), O-root in (x3,x4),
  E-root in (x4,x5), O-root in (x5,inf) (phase index of b at x_j is j).
* Exact control: x = (1,11,12,134,137,1505,1508), L_- = 2240, L_+ = 400 is a valid box. The kernel
  vector with b0=1e6, b6=b7=1 is Hurwitz with positive coefficients but P_{--}(2) < 0 (fails in E1),
  while the kernel vector with b0=b6=b7=1 is a closed numerator (all four residuals >= 0, exact).
  The numerically best kernel vectors bind at t=0 and in the end regions [0,x1], [x5,inf).
* The coefficient structure is ESSENTIAL: generalized families with W_E, W_O >= 0 pointwise on
  [0,inf) but a negative t-coefficient can be closed-infeasible already at n = 6 (exactly
  certified); there both widths nearly vanish inside a cluster of band points. The n = 6 published
  construction (Xu-Dou-Ji-Wang-Yu, arXiv:2609.26541) uses exactly W_E'(x0) >= 0 and a discriminant
  inequality disc(O_+) <= disc(O_-) for its odd bounds; its numerator has odd part ~ U + mV (the
  two closed odd endpoints) and even part U L_a + V L_g (closed odd endpoints times linear
  polynomials) plus an interpolation correction.

## Task (one focused bottleneck)
For the n = 7 fully-closed stratum above, find a canonical element of the 3-dim kernel (two more
natural linear conditions, or an explicit formula in x0..x6, L_-, L_+) that is plausibly ALWAYS a
closed numerator, and try to PROVE the four residual nonnegativity conditions on their binding
sets using only: the ordering of the x's, the nonnegativity of the 4 + 3 width coefficients, and
L_- >= L_+. If you find a configuration (satisfying all box conditions) where you can show NO
kernel element works, give it exactly (rationals) with the reason. Prioritise: (1) the exact
inequalities among x's and L's that a proof needs and whether box conditions imply them;
(2) any reduction to fewer cases (e.g. using that P_{+-} has two forced double roots so its
residual is a cubic); (3) a clearly separated list of what is proved vs conjectured.
Output plain text, at most ~1500 words, with explicit formulas.
