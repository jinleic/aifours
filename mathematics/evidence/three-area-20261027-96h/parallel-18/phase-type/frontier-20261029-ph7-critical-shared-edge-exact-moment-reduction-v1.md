# An exact moment reduction for the shared-edge three-triangle case

Status: **WRITTEN-checked-in-kernel symbolic algebra**, pending independent scientific review. This is a necessary algebraic representation for one all-edge graph class; the relevant sign inequality remains unproved. It does not exclude the graph or solve PH7.

## 1. Graph and row-fraction bound

Consider a seven-state irreducible row generator with no directed two-cycle and exactly three directed triangle vertex sets: disjoint triples `A={a_1,a_2,a_3}`, `B={b_1,b_2,b_3}`, and `C={a_1,a_2,b_1}`. The third triangle shares the edge `a_1->a_2` with `A`; its orientation is `a_1->a_2->b_1->a_1`. The seventh vertex has escape rate `x`. Arbitrarily many other edges and directed four-cycles are allowed, provided no additional directed triangles or two-cycles are created.

Let `w_A,w_B,w_C>0` be the actual cycle products. Define `theta_A=w_A/(a_1*a_2*a_3)`, `theta_B=w_B/(b_1*b_2*b_3)`. Row fractions at `a_2` and `b_1` give

`w_C <= (1-theta_A)*(1-theta_B)*a_1*a_2*b_1`.

Write `w_C=theta_C*(1-theta_A)*(1-theta_B)*a_1*a_2*b_1` with `theta_C in (0,1]`. This is a safe enlarged parameter domain, not an assumption that the three fractions are independent actual transition choices.

## 2. Eliminate the seventh rate exactly

Scale the critical repeated pair to `-1 +/- i*sqrt(8/9)`. Let `f_j` be elementary symmetric sums of the six triangle rates, and define

`A0=f_2-4*f_1+74/9`,

`B0=f_3-4*f_2+(74/9)*f_1-28/3-w_A-w_B`,

`h0=f_4-(70/9)*f_2+(212/9)*f_1-1007/27-w_A*(b_1+b_2+b_3)-w_B*(a_1+a_2+a_3)`,

`h1=f_3-(70/9)*f_1+212/9-w_A-w_B`, `T=a_3+b_2+b_3`.

The hidden quadratic is `y^2+p*y+q`, with `q>0` by irreducible row-generator stability. Since there are no 2-cycles, comparing `y^6,y^5,y^4` gives

`q=A0+x*(f_1-4)`, `A0*x+B0-w_C=0`.                         (E4)

The third triangle's outside-rate sum is **exactly** `x+T`; keeping all directed four-cycles in a total `V4>=0`, the next coefficient gives

`h0+x*h1-w_C*(x+T)-V4=0`.                                   (E3)

Define the two elimination polynomials

`Q=A0^2-(f_1-4)*(B0-w_C)`,

`H=-243*[A0^2*(h0-w_C*T)+A0*(w_C-B0)*(h1-w_C)-w_C*(w_C-B0)^2]`.

The exact identities are

`Q=q*A0`,

`H=-243*A0^2*V4`.                                            (ID)

If `A0=0`, (E4) forces `B0=w_C`, so `Q=0`; this case is **not** automatically excluded unless an independent strict `Q>0` lemma is proved. If `A0>0`, the positivity of `x` additionally forces `B0-w_C<0`, while(ID) forces `H<=0`.

## 3. Exact remaining gap and verification

An all-variable proof that `Q>0` for the enlarged parameter domain, plus a proof that `H>0` whenever `A0>0` and `B0-w_C<0`, would contradict(ID) and exclude this shared-edge class, including all directed four-cycles. No such sign certificate is supplied here. The first expression is degree three in the three fraction variables and the second can have total fraction degree nine; the higher degree comes from the actual shared-edge outside term and must not be replaced by the easier singleton-connector formula.

The coefficient and substitution identities were checked in the owner's SymPy kernel. Bounded floating stress-tests found no negative `H` in sampled points satisfying the named positivity conditions, but this is only a diagnostic; it does not establish universal positivity, rule out boundary failures, or constitute a certificate. The original graph, PH7 at `8/9`, and wider graph families remain open; no PH8/minimum-state, formal proof, novelty, independent-review or parent-adoption claim is asserted.
