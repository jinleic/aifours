# An exact isolated flat rank-two projector and its excluded MUB neighborhood

**COMPUTER-ASSISTED AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date` at completed check: **Wed Oct 28 19:22:48 PDT 2026**. This is a LOCAL, exact-algebraic result for ONE known rank-two 5D projector, not a classification of all such projectors, not an unrestricted MUB/QLS10 no-go, and not formal proof or peer acceptance.

## 1. The local statement

Let `omega=exp(2*pi*i/5)`, `U_(t,j)=omega^(3tj)/sqrt(5)`, `D5_tt=omega^(4t²)`, `V=D5 U`, and `W=D5² U`. Define

`P0=|W[:,0]><W[:,0]|+|W[:,1]><W[:,1]|`.

As checked in `frontier-20261028-rank2-mub-counterexample-check-v1.py` SHA **ed7f1d5b0ff3feb36f1c1aed7b14a7d2232c800dcf54cab1ad6043465da42c1f**, P0 is an actual orthogonal rank-two projector with diagonal2/5 in all three bases I,U,V. The new claim is that **P0 is isolated** among all rank-two orthogonal projectors with those three flat diagonals: some open neighborhood contains no other such P.

Consequently, in the specific Weyl/MUB construction of `frontier-20261028-mub-triple-rank2-reduction-v1.md` SHA **ef00b5db269a3e436365b4b98fd486c32836bbda931f00bba80afcaaea5dfc8c**, no common unbiased 10-vector can have its 5D Schmidt-support projection in that neighborhood. This is a local excluded neighborhood around P0, not a claim that P0 is the only feasible flat projector globally.

## 2. Grassmann chart and exact derivatives

Let W0 be W's first two columns and W_perp its last three. Every rank-two subspace sufficiently close to P0 has a unique graph chart `T in C^(3×2)` with projector

`P(T)=(W0+W_perp T)*(I+T†T)^(-1)*(W0+W_perp T)†`.

Write the 12 real and imaginary coordinates of T as x∈R^12. For each of I,U,V retain the first four diagonal residuals `diag(B†P(T)B)-2/5`; the fifth is determined by trace2. Let F(x)∈R^12 be these residuals. Its analytic expansion is

`F(x)=J x+Q(x)+O(||x||³)`,

where Q is homogeneous quadratic. The underlying projector expansion is

`P(T)=P0+W_perp T W0†+W0 T† W_perp†
          +W_perp T T† W_perp†-W0 T† T W0†+O(||T||³)`.       (1)

The exact checker computes these derivatives directly from (1), without finite differences.

## 3. Exact algebraic certificate and isolation proof

`frontier-20261028-rank2-projector-isolation-v1.py`, SHA **38645d8cba19326d5d28f9881b905f95405bc1ac632bf3eedf62e7f526a9beeb**, implements exact arithmetic in `Q(zeta20)` as rational polynomials modulo `Phi20=x^8-x^6+x^4-x²+1`. It uses the positive real field element `sqrt5=1+2(omega+omega^-1)` and checks every entry of `sqrt5*B†W` has exact modulus1. The observed result is

```text
PASS Phi20 arithmetic; exact 12x12 Jacobian rank 10 and real 2D kernels
PASS two left-null quadratic forms have nonzero exact resultant, including infinity
Therefore no nonzero common kernel direction; written local-isolation proof required
```

More precisely the script computes exact real bases k1,k2 of ker(J) and l1,l2 of ker(J^T). Each scalar `l_i^T Q(x k1+y k2)` is a homogeneous real quadratic in (x,y). The determinant of their 4×4 Sylvester resultant is nonzero in Q(zeta20), and their y² coefficients are not BOTH zero; thus they have no common nonzero projective zero, over C and therefore over R.

To derive isolation, suppose nonzero solutions x_n->0 of F(x)=0 existed. After normalizing and taking a subsequence, x_n/||x_n||->u with ||u||=1. The linear term gives J u=0. Left-multiplying by either l_i, dividing by ||x_n||², and taking the limit gives `l_i^T Q(u)=0`. This contradicts the exact resultant. Hence x=0 is isolated in the Grassmann chart, which is exactly the stated projector isolation.

The number-field operations, rank, kernel reality, quadratic assembly, nonzero resultant and at-infinity check are executable exact calculations, but a separate reviewer must inspect the implementation and the analytic limiting argument. No assumption that a singular Jacobian alone gives isolation is used.

## 4. Why the isolated projection cannot support a common 10D vector

If P=P0 and a,b are any orthonormal basis of its range, write `a=alpha W[:,0]+beta W[:,1]`. The ratio of the two W columns is `omega^(3t)`. If a is flat in the computational basis,

`|a_t|²=(1/5)*(1+2 Re(conjugate(alpha)*beta*omega^(3t)))=1/5` for all t.

The five characters span two noncollinear phases, so `conjugate(alpha)*beta=0`; a and b are exactly W's two columns up to phases and exchange. Their coordinate ratio is then a nontrivial fifth-root CHARACTER up to an arbitrary common phase. The written odd-cycle result `frontier-20261028-character-ratio-obstruction-v1.md` SHA **ae331153fb2b082ab50382e12531c2766b288e4cc654aacca11b86cdaf4036b8** excludes such a,b from the full X/Y cross gates. Therefore P0 itself is not a common-unbiased phi, and the isolation conclusion gives the stated excluded neighborhood.

## 5. Scope

A bounded floating 200-restart Grassmann search also found many near-zero points close to one of30 familiar WH pair projections, but that is NOT a proof that there are only30. Other isolated or continuous flat-projector components may exist away from P0, and a general QLS10 need not arise from this CRT/MUB construction. No global obstruction, original target witness, formal kernel result or novelty clearance is asserted.
