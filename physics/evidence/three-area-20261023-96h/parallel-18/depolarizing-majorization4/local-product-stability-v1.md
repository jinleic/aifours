# Explicit near-product exclusion for all five central Ky-Fan indices

Clock observed before creation: **2026-10-23T14:14:40-0700**. Author: PhysicsDepol4. Status: **CANDIDATE, written derivation only**. This continues the same assigned four-qubit problem; it is not a new problem slot or an accepted second discovery. No scientific execution was used.

## 1. Exact statement and role

For a pure four-qubit state psi define its maximum product overlap

`G(psi)=max_{unit u_1,...,u_4} |<u_1 tensor ... tensor u_4|psi>|^2`.

**Claim.** If `G(psi)>=1-1/900000000`, then for every `k=6,7,8,9,10`,

`K_k(X_2(psi))<=k+13`.

More quantitatively, put `s=sqrt(1-G(psi))`. For `0<s<=1/30000`,

`K_(5+m)(X_2(psi)) <=18+m-s^2/15`, `1<=m<=5`.                    (1)

At s=0 equality holds. The radius is deliberately conservative, not an optimized threshold. The common-order channel bridge in `proof-v1.md` then proves these **central indices for every physical replacement p**. This is not a proof of the remaining low-noise indices k=2,3,4 for such states.

Unlike the earlier moment region, this excludes pure inputs very close to products, exactly where the moment certificate is loose. It uses compatibility of the off-diagonal marginal perturbations, not a PPT relaxation or a substituted logdet inequality.

## 2. Closest-product coordinates are general, not an input ansatz

A closest product vector exists by compactness. Local unitaries and a global phase put it at `|0>=|0000>`, with its overlap with psi real and nonnegative. Write

`psi=sqrt(1-s^2)|0>+s phi`, `||phi||=1`, `<0|phi>=0`.

For s>0, all four weight-one amplitudes of phi vanish. Indeed, vary only qubit i in the closest product as `cos(theta)|0>+exp(i eta)sin(theta)|1>`. The derivative of the squared overlap at theta=0 vanishes for every eta. Since the vacuum overlap is nonzero, this forces the single-excitation amplitude to vanish. Our small-radius hypothesis guarantees a nonzero vacuum overlap.

Let H_j be the computational subspace of Hamming weight j, and let P_j be its projector. Thus phi belongs to `H_2 direct_sum H_3 direct_sum H_4`. Put

`a=||P_2 phi||^2`, `b=||P_3 phi||^2`, `e=||P_4 phi||^2`, so `a+b+e=1`.

For each pair S of qubits, let c_S be the coefficient of its weight-two basis vector in phi. Then `sum_S |c_S|^2=a`. Define the six-vector d by `d_R=conjugate(c_(R^c))`, so `||d||^2=a`.

## 3. Exact matrix expansion and block norms

Write Phi_2 for the linear map with `Phi_2(rho)=X_2(rho)`. Set

`A_0=T_2=Phi_2(|0><0|)`,

`C=Phi_2(|phi><0|+|0><phi|)`,

`B=Phi_2(|phi><phi|)-T_2`.

Here C is a matrix, **not** the spin-flip scalar C in `proof-v1.md`. The exact expansion is

`A(s):=X_2(psi)=A_0+s sqrt(1-s^2) C+s^2 B`.

The spectrum of A_0 is 6 on H_0, 3 on H_1, 1 on H_2, and 0 on `H_3 direct_sum H_4`. Every marginal term of Phi_2 applied to a state lies between zero and I; there are six terms. Hence

`0<=Phi_2(|phi><phi|)<=6I`, `0<=T_2<=6I`, and `||B||<=6`.            (2)

Only the weight-two part of phi survives in C. For each pair S its term is

`c_S (|11><00|)_S tensor I_(S^c) + conjugate(c_S)(|00><11|)_S tensor I_(S^c)`.

Thus the only nonzero blocks of C are between H_0 and H_2, H_1 and H_3, and H_2 and H_4. The H_0-to-H_2 column is c and the H_4-to-H_2 column is d. The H_1-to-H_3 matrix M has entry c_(R minus {i}) when the weight-one index i belongs to the weight-three set R, and zero otherwise. Each c_S occurs twice in M, giving

`||M||_F^2=2a`, `||c||^2=||d||^2=a`.

On the even-weight subspace C is an off-diagonal matrix with rectangular block `[c,d]`; on the odd-weight subspace it has block M. Therefore

`||C||<=sqrt(2a)<=2`.                                             (3)

## 4. Second-order effective blocks, derived by a unitary change of basis

Use the four spectral subspaces of A_0, of eigenvalues 6,3,1,0; the last combines H_3 and H_4. There are no within-subspace blocks of C. Define an anti-Hermitian matrix S by

`S_(ij)=-C_(ij)/(lambda_i-lambda_j)` between different spectral subspaces, with zero diagonal blocks.

Then `[A_0,S]=-C`. The three kinds of nonzero C blocks have gaps 5,3,1, so

`||S||_F^2=2a/25+4a/9+2a=568a/225<4`, and `||S||<=2`.              (4)

Conjugating by `exp(sS)` gives the effective second-order matrix

`B_eff=B+(1/2)[C,S]`.

Indeed, `exp(-sS) A(s) exp(sS)` has zero first-order term, since `C+[A_0,S]=0`; its second-order term is `B+[C,S]+(1/2)[[A_0,S],S]=B_eff`. Its diagonal spectral blocks satisfy

`(B_eff)_(ii)=B_(ii)+sum_(j!=i) C_(ij)C_(ji)/(lambda_i-lambda_j)`.   (5)

Let L=`H_0 direct_sum H_1` (the top-five subspace of T_2), and let

`H=P_2 B_eff P_2`

be the six-dimensional effective central block. Formula (5) gives

`Tr(P_L B_eff)=7a+3b-18 +a/5+2a/3 =118a/15+3b-18`,                (6)

`H=P_2 Phi_2(|phi><phi|)P_2-I_(H_2) -(1/5)cc^dagger+dd^dagger`.    (7)

Here are direct checks of the traces, not numerical substitutions. For a basis input of weight w, the diagonal operator `Phi_2(P_L)` has value

`3 binom(4-w,2)+w(4-w)`,

which is 7,3,0 at w=2,3,4 respectively. This proves the B contribution in (6). The positive correction in (6) consists of c across gap 5 and M across gap 3.

Similarly `Phi_2(P_2)` has diagonal values 10,9,6 at input weights 2,3,4. Count pairs I by the number j of occupied bits in I: the number of weight-two output strings agreeing with the input on I is `binom(2,2-j)`. At w=2 the contributions are `1+8+1=10`; at w=3 they are `0+6+3=9`; at w=4 they are 6. Thus (7) gives

`Tr H=10a+9b+6e-6-a/5+a =24a/5+3b`.                              (8)

Its positive terms also give the operator lower bound

`H>=-I_(H_2)-(1/5)cc^dagger`.                                     (9)

For `1<=m<=5`, the sum of the 6-m smallest eigenvalues in (9) is at least `-(6-m)-a/5`. Subtract this from (8):

`K_m(H)<=5a+3b+6-m`.                                              (10)

Combining (6) and (10),

`Tr(P_L B_eff)+K_m(H) <=193a/15+6b-12-m <=13/15-m`,                (11)

because a+b+e=1, a,b,e>=0 and `193/15>6`.

Every coefficient in (5)–(11) follows from the displayed compatible marginal blocks. No unproved majorization property of an arbitrary Gram matrix is used.

## 5. Uniform explicit remainder: replacing an asymptotic claim by a radius

All matrix norms in this section are operator norms, except where subscript F is shown. For real s, the changes of basis below are unitary. For `0<=s<=1/1000`,

`A(s)=A_0+sC+s^2 B+R_0`, `||R_0||<=2s^3`,

because `|sqrt(1-s^2)-1|<=s^2` and ||C||<=2.

The commutator expansion for `exp(-sS)(.)exp(sS)`, with `||A_0||=6`, `||C||<=2`, `||B||<=6` and `||S||<=2`, bounds the first omitted terms as follows:

- A_0 terms of order at least three: at most `64 exp(4s)s^3`;
- sC terms of order at least two in the conjugation: at most `16 exp(4s)s^3`;
- s^2 B terms of order at least one: at most `24 exp(4s)s^3`;
- the conjugated R_0: at most `2s^3`.

These bounds use `||[U,V]||<=2||U||||V||` and the elementary exponential-series tail estimate `sum_(j>=l) x^j/j! <=x^l exp(x)/l!`. Since `exp(4s)<4/3` in this range,

`exp(-sS)A(s)exp(sS)=A_0+s^2 B_eff+R_1`, `||R_1||<=142s^3`.        (12)

Also `||B_eff||<=6+||C||||S||<=10`. Let D be the block-diagonal part of B_eff in the four spectral subspaces of A_0. Define a second anti-Hermitian T, with zero diagonal blocks, by

`T_(ij)=-(B_eff)_(ij)/(lambda_i-lambda_j)` for i!=j.

All denominators have modulus at least one, so

`||T||<=||T||_F<=||B_eff||_F<=4||B_eff||<=40`.

Conjugate (12) by `exp(s^2 T)`. This cancels the off-diagonal second-order blocks. The additional remainder, beyond the unitarily conjugated R_1, is at most

`19200 exp(80s^2)s^4 +800 exp(80s^2)s^4`.

Since `exp(80s^2)<2` and s<=1/1000, this is at most `40s^3`. Therefore the exact twice-conjugated matrix has the form

`A_0+s^2 D+R`, `||R||<=200s^3`.                                  (13)

The use of the Frobenius norm above is legitimate even though T is formed by dropping diagonal blocks: that dropping is an orthogonal projection for the Frobenius norm, and division by gaps of modulus at least one can only decrease its squared entries in an A_0 eigenbasis.

Because ||D||<=10 and `20s^2<1`, the spectral clusters of `A_0+s^2 D` retain their order 6,3,1,0. Thus its leading 5+m sum is exactly

`18+m+s^2(Tr(P_L B_eff)+K_m(H))`.

A Ky-Fan sum of k eigenvalues changes by at most `k||R||`. From (11) and (13), for k=5+m<=10,

`K_(5+m)(A(s)) <=18+m +(13/15-m)s^2+2000s^3`.

For `s<=1/30000`, `2000s<=1/15`. Hence

`K_(5+m)(A(s)) <=18+m +(14/15-m)s^2 <=18+m-s^2/15`.

This proves (1) and the explicit overlap radius. No finite point testing or unobserved numerical eigenvalue is involved.

## 6. Exact residual after both written candidates

For k=6, the moment candidate already excludes `10R+4C<=74/3`. This manuscript additionally excludes the tiny but genuine closest-product neighborhood `1-G<=1/900000000`, including its high-R states. A remaining pure k=6 counterexample would have to satisfy **both**

`10R+4C>74/3` and `G<1-1/900000000`.

The unresolved obligation is still the unrestricted inequality `K_6(X_2)<=19` in that complementary region, and the analogous remaining central/low-noise inequalities. This overlap radius does not make that compact residual small or easy. The work does not claim a full index closure, full majorization for every input, an exact counterexample, or a literature-new perturbation method.

Correctness/review boundary: complete author-written candidate, to be reviewed on pinned bytes by parent and a separate in-harness reconstruction. Formal, human and independent-model CLI review have not been performed.
