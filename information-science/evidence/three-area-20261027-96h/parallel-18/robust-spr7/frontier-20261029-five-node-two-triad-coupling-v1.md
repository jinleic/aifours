# Two quantitative triad constraints on actual septic-box certificates

Owner InfoSPR7-2, info-2. Native clock observed before writing: **Thu Oct 29 14:58:55 PDT 2026**. **WRITTEN theorem candidate with WRITTEN-checked-in-kernel finite rational example; not parent adoption, independent review, formal verification or novelty clearance.** The original all-box synthesis-or-obstruction problem remains open.

## 1. Universal necessary conditions

Let \(K\) be any compact all-Hurwitz independent monic septic box, with degenerate intervals allowed. Consider any finite positive-weight actual-member/frequency atom sum whose eight numerator-monomial coordinates are all strictly negative. Suppose it has exactly five distinct positive finite squared frequencies \(t_1<\cdots<t_5\); zero and compactified infinity atoms may also be present. Merge atoms at each positive frequency by positive-weight averaging of their denominators; their means remain actual stable members of \(K\). Write their even/odd evaluations \(E_i,O_i\), and assume the first four merged sign pairs are
\[
(E_1,O_1):(-,-),\quad(E_2,O_2):(-,+),\quad
(E_3,O_3):(+,-),\quad(E_4,O_4):(-,-).
\]
The fifth member is unrestricted. Define \(r_i=t_i|O_i|/|E_i|>0\), \(1\le i\le4\). Then necessarily
\[
\begin{aligned}
G_{123}&:=t_2(t_3-t_1)r_1(r_2-r_3)
-t_1(t_3-t_2)r_2(r_1+r_3)>0,\\
D_{234}&:=(r_2-r_3)(t_4-t_3)
-(r_3+r_4)(t_3-t_2)>0. \tag{1}
\end{aligned}
\]
In particular \(r_2>r_3\), but (1) is strictly stronger than that single comparison. These are necessary conditions for an original **strict-negative-coordinate** certificate, not for a zero annihilator; they do not exclude a certificate with six or more positive nodes.

## 2. Proof by two exact three-node tests

For any two positive nodes \(u,v\), \(H(s)=(s^2+u)(s^2+v)\) has nonnegative coefficients. For each \(k=0,1,2,3\), the nonzero coefficient vector of \(H(s)s^k\) is nonnegative; its dot product with an all-strictly-negative aggregate vector is therefore strictly negative. An atom at zero or infinity contributes a nonnegative amount to this dot product, since each denominator has positive constant and monic leading coefficient. Removing those endpoint contributions preserves strict negativity of the positive-node sum.

First use \(H_{45}(s)=(s^2+t_4)(s^2+t_5)\). It vanishes at \(t_4,t_5\) and is positive at the first three nodes. After absorbing its positive value, the atom weight and \(|E_i|\), let the positive quantities be \(A,B,C\). The four tests \(H_{45}s^k\) give
\[
\begin{aligned}
-A-B+C&<0,&-t_1A-t_2B+t_3C&>0,\\
-r_1A+r_2B-r_3C&<0,&-t_1r_1A+t_2r_2B-t_3r_3C&>0.
\end{aligned} \tag{2}
\]
Set \(z=B/A\), \(x=C/A\). The inequalities require
\[
\max\left\{\frac{t_1+t_2z}{t_3},\frac{r_2z-r_1}{r_3}\right\}<x<
\min\left\{1+z,\frac{t_2r_2z-t_1r_1}{t_3r_3}\right\}.
\]
Comparing these four bounds shows that such positive \(z,x\) exist **if and only if** \(r_2>r_3\) and
\[
\frac{t_1(r_1+r_3)}{t_2(r_2-r_3)}<z<
\min\left\{\frac{r_1+r_3}{r_2-r_3},\frac{(t_3-t_1)r_1}{(t_3-t_2)r_2}\right\}.
\]
Since \(t_1<t_2\), the lower bound is automatically below the first upper bound; comparison with the second is exactly \(G_{123}>0\).

Next use \(H_{15}(s)=(s^2+t_1)(s^2+t_5)\), which vanishes at nodes 1 and 5 and is **negative** at nodes 2, 3 and 4. After absorbing the absolute value of this factor, the positive weights and \(|E_i|\) into \(A,B,C\), the four tests give
\[
\begin{aligned}
A-B+C&<0,&t_2A-t_3B+t_4C&>0,\\
-r_2A+r_3B+r_4C&<0,&-t_2r_2A+t_3r_3B+t_4r_4C&>0.
\end{aligned} \tag{3}
\]
The first pair yields
\[
 B>A+C,\qquad \frac CA>\frac{t_3-t_2}{t_4-t_3}.
\]
The third inequality then yields
\[
 r_2>r_3+(r_3+r_4)\frac CA,
\]
which proves \(D_{234}>0\). Conversely, for fixed positive \(r_2,r_3,r_4\), these four three-node inequalities are simultaneously feasible exactly when \(D_{234}>0\): choose \(C/A\) strictly between
\[
\max\left\{\frac{t_3-t_2}{t_4-t_3},\frac{t_2}{t_4}\frac{r_2-r_3}{r_3+r_4}\right\}
\quad\text{and}\quad\frac{r_2-r_3}{r_3+r_4},
\]
then choose \(B/A\) between the resulting lower and upper bounds. These separate feasibility statements do **not** imply that one common five-node atom system exists.

## 3. Exact obstruction to a tempting two-zero proof route

The joint inequalities (1) do **not** themselves close the original problem. The following single rational full-width box and five rational nodes show a further issue: every nonnegative cubic test multiplied by **any two** selected imaginary-axis factors fails to separate all five nodes, yet a different nonnegative polynomial separates all four actual corners at all five nodes. This is a finite-node obstruction to that proof route, not an all-frequency synthesis or a counterexample.

In ascending coefficients \(a_0,\ldots,a_6\), let the lower and upper vectors be
\[
\ell=(1/2,\ 8066931430583/5000000,\ 2192672625039/2000000,\
1212386815553/10000000,\ 92232966209/2000000,\
19302663807/10000000,\ 130713597/5000000),
\]
\[
u=(337520809988/78125,\ 8066933930583/5000000,\
20431428914531/10000000,\ 3319907356313/10000000,\
92233966209/2000000,\ 19307663807/10000000,\ 133213597/5000000).
\]
All seven widths are positive. The five nodes are \((6,10,26,43,455)\). Use the corner order \(0=(E_-,O_-)\), \(1=(E_-,O_+)\), \(2=(E_+,O_-)\), \(3=(E_+,O_+)\).

The marker sign sequence for **all four corners**, starting at zero, is
\[
(+,+),(-,+),(-,-),(+,-),(+,+),(-,+),(-,-),
\]
with the five finite markers \(1001/200,19,91/2,455,1740\). At each finite marker the minimum of the four required signed parity values is respectively
\[
200000005207/400000000000,\quad2500007/5000000,\quad4983529/10000000,\quad779873120191463/5000000,\quad2474873/5000000,
\]
all positive. Every box member lies between the corresponding parity endpoints at each marker, so the same signs hold throughout the box. Intermediate value plus cubic degree forces the six separated alternating positive parity roots; the standard degree-seven Hermite–Biehler criterion then gives strict Hurwitz stability of every member.

For the four signs in §1, choose corners \(2,3,3,1\) at nodes 1–4 respectively. Direct rational substitution makes **both** \(G_{123}>0\) and \(D_{234}>0\). Hence the two individually necessary tests cannot alone exclude all original boxes.

A different polynomial
\[
b_*(s)=7696s+1014s^2+1244s^3+25s^4+21s^5
\]
has strictly positive pairing against every corner at all five nodes. The exact minimum over the four corners is, in node order,
\[
80842648182873/62500,\quad966724456223/25000,\quad
806593120995311/125000,\quad12771491568354987/625000,\quad
74427086588389009896967/250000.
\]
Thus no strictly negative atom sum supported on these five nodes can exist. This polynomial has zero constant and degree five; it is **not** claimed to be an original common exact-degree-seven numerator and its pairing has not been proved positive between the nodes.

## 4. Exact certificates for all ten two-zero families

For a pair of node indices \(J=\{j,k\}\), set \(H_J(t)=(t_j-t)(t_k-t)\). At each of the remaining nodes and each corner define the four-coordinate row
\[
V_J(t,a)=H_J(t)\bigl(E_a(t),\ tO_a(t),\ -tE_a(t),\ -t^2O_a(t)\bigr),\qquad M_J=\max_{0\le h\le3}|(V_J)_h|.
\]
These are exactly the pairings with \((s^2+t_j)(s^2+t_k)\) times the cubic monomials \(1,s,s^2,s^3\). The following table gives positive rational weights for actual (node,corner) rows. In every row of the table, the weighted sum of \(V_J/M_J\) has **all four coordinates less than \(-10^{-8}\)**. Consequently no nonzero cubic with nonnegative coefficients can make all five-node corner pairings nonnegative in that two-zero family.

| \(J\) | Positive-weight triples `(node, corner, weight)` |
|---|---|
| 1,2 | (3,1,7/100), (4,0,1/10), (5,2,83/100) |
| 1,3 | (4,0,1/25), (4,1,2/25), (5,2,22/25) |
| 1,4 | (2,3,1/20), (3,3,3/50), (5,1,89/100) |
| 1,5 | (2,3,30083/125000), (3,3,210699/500000), (4,1,168961/500000), (4,3,1/62500) |
| 2,3 | (4,1,11/100), (4,3,7/100), (5,1,41/50) |
| 2,4 | (1,2,1/50), (5,2,49/50) |
| 2,5 | (1,0,23/100), (1,2,13/100), (3,1,16/25) |
| 3,4 | (2,2,11/500), (5,2,489/500) |
| 3,5 | (1,0,453/1000), (4,1,501/1000), (4,3,23/500) |
| 4,5 | (1,2,2387/10000), (2,2,17/2000), (2,3,2501/5000), (3,3,1263/5000) |

All signs and fractions in §§3–4 were checked with integers and `fractions.Fraction` in one Python Eval host; rational linear programming was used to locate the weights, but the displayed rational inequalities, not solver UNSAT, are the claimed finite evidence. The general derivation in §§1–2 is written mathematics. A subsequent all-frequency exchange attempt for this box timed out and destroyed its Eval kernel; it delivered **no** all-frequency conclusion and is not used here. No held historical source, prior unreviewed theorem, or external-model output is used as a premise. Parent-classified incidental source exposure remains disclosed in `owner-incidental-held-source-search-display-v1.json`; no clean-cognition claim is made.

**Exact remaining step:** prove or disprove the full common-numerator assertion for arbitrary boxes, including certificates on six or more nodes; neither the necessary triad conditions nor this finite-node example does so. The next representation must use the full eight-coordinate positive-numerator cone, or another rigorously complete construction; the ten two-zero cubic tests are insufficient even at five nodes.
