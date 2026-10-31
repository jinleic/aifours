# Every critical seven-state Metzler spectrum has hidden sum greater than five

Status: **WRITTEN-checked with exact stdlib Fraction/Bernstein arithmetic**, awaiting independent scientific review. This strengthens the previously written universal bound `p>2alpha>49/10` to the rational inequality **`p>5`**, for real and complex stable hidden roots. It is a topology-independent necessary spectral condition, not a PH7 existence/exclusion result.

## 1. Theorem

Let a real seven-state Metzler generator have spectrum `0` and the target pair `-1 +/- i*sqrt(8/9)` each twice. Assume the remaining two eigenvalues are stable and define their monic real quadratic as `Q(y)=y^2+p*y+q`. Then

`p>5`.

If the hidden roots are real, the independently replayed all-real-root theorem `frontier-20261029-ph7-critical-all-real-hidden-roots-bound-v1.md` (SHA256 `f8f60590ff771dfde36c2693af8b1816208c5ba83ae700f45f8c88e128ec3512`) gives the stronger `p>3437/500>5`. It remains to rule out nonreal hidden roots `-r +/- i*h` with `r<=5/2`.

## 2. A universal fourth-trace inequality

For any real Metzler matrix `X` with `tr X=0`, let `tau2=tr X^2>=0` and `tau3=tr X^3`. Then

`tr X^4 + 3*sqrt(tau2)*max(tau3,0) + 10*tau2^2 >= 0`.       (FOURTH-ALL)

In particular, when `tau3<=0` this reduces to `tr X^4+10*tau2^2>=0`.

Proof. Write `X=D+A`, where `D=diag(d_i)` and `A` has nonnegative off-diagonal entries and zero diagonal. Let `b_ij=A_ij*A_ji>=0`, and let `W` be the sum of products over **all oriented directed triangle cycles counted once per orientation**. The exact walk expansions are

`tau2=sum_i d_i^2+2*sum_{i<j} b_ij`,

`tau3=sum_i d_i^3+3*sum_{i<j}(d_i+d_j)*b_ij+3W`,

`tr X^4=sum_i d_i^4+4*sum_{i<j}(d_i^2+d_i*d_j+d_j^2)*b_ij`

`             +4*sum_(oriented triangles C) [product of its three edges]*sum_{i in C}d_i + tr(A^4)`.

Both the pair term and `tr(A^4)` are nonnegative. Cauchy gives `sum_{i in C}d_i >= -sqrt(3*tau2)`, hence `tr X^4 >= -4*sqrt(3*tau2)*W`. Also `|sum_i d_i^3|<=tau2^(3/2)` and

`|3*sum_{i<j}(d_i+d_j)b_ij| <= (3/sqrt(2))*tau2^(3/2) < 3*tau2^(3/2)`,

because `|d_i+d_j|<=sqrt(2*tau2)` and `sum b_ij<=tau2/2`. The cubic identity therefore gives `3W<=tau3+4*tau2^(3/2)`. Replacing `tau3` by `max(tau3,0)` and combining with the fourth-trace bound yields

`tr X^4 >= -(4*sqrt(3)/3)*sqrt(tau2)*max(tau3,0) -(16*sqrt(3)/3)*tau2^2`.

Both constants are strictly below 3 and 10 respectively, proving(FOURTH-ALL). If `tau2=0`, every diagonal and bidirectional product is zero and `tr X^4=tr A^4>=0`; the same weak inequality holds. No diagonalizability or selected state is assumed.

## 3. Complex hidden pair: exact dual certificate

Write hidden roots `-r +/- i*h`, `r,h>0`, so `p=2r`. The earlier all-hidden-sum manuscript `frontier-20261029-ph7-critical-all-hidden-sum-lower-bound-v1.md` (SHA256 `fb7a5540887785cd64d5e73f397bafb0ec71261ed3b5945c612b97d8da64840a`) proves `r>43/20`; the visible trace-square identity gives

`0<h^2<=V(r):=(45r^2-72r-58)/63`.

For `r in [43/20,5/2]`, the sign of the centered `tau3` may be positive or nonpositive. Both cases are handled separately below.

When `tau3<=0`, two separate necessary inequalities hold:

`E3:=(25/42)*tau2^3-tau3^2 >=0`,

`E4:=tau4+10*tau2^2 >=0`.

The first is the seven-dimensional centered geometric-mean symmetrization bound, and the second is the `tau3<=0` case of (FOURTH-ALL). The exact stdlib checker `frontier-20261029-ph7-complex-hidden-third-fourth-fraction-check.py` (SHA256 `0dddba48dd1529aea13bb051aa35a7cd0eb30287fcb453798b45fd44be05d321`) parameterizes the **whole** rectangle `r=43/20+(7/20)s`, `h^2=t*V(r)`, `0<=s,t<=1`. It reconstructs the degree-`(6,3)` polynomial `-E3` and degree-`(4,2)` polynomial `-E4`, and verifies a complete exact Bernstein selector tree: **13** leaves have `-E3>0`, and **5** leaves have `-E4>0`. The actual program returned PASS. Thus no point in the rectangle with `tau3<=0` satisfies both necessary inequalities.

For `tau3>0`, let `J=tau4+10*tau2^2`. The full inequality(FOURTH-ALL) requires `J+3*sqrt(tau2)*tau3>=0`. The exact stdlib checker `frontier-20261029-ph7-complex-hidden-positive-skew-fraction-check.py` (SHA256 `9bff02666eecc6c4308568f8c95f5f8d5c3fe524deb28e0b06a1b3cec9eadc17`) verifies another **complete** selector tree on the same whole rectangle: 12 leaves have `-tau3>=0`, while 4 leaves have both `-J>0` and `J^2-9*tau2*tau3^2>0`. On the positive-`tau3` domain only the second alternative can hold; it implies `J+3*sqrt(tau2)*tau3<0`, contradicting(FOURTH-ALL).

Thus both centered-skew signs are excluded whenever `r<=5/2`; the hidden nonreal pair must have `r>5/2`, and `p=2r>5`. Combined with the real-hidden branch this proves the theorem.

Both exact dual checkers are independently written stdlib code by the same owner; the 18-leaf and 16-leaf trees are full-domain arithmetic evidence, not independent scientific review or formal proof. No PH7/PH8 existence verdict, novelty or parent adoption is asserted.
