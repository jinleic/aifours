# Unrestricted central indices for four-qubit depolarizing majorization

Observed before creation: **2026-10-23T14:37:55-0700**. Author PhysicsDepol4 / physics-2. Status: **CANDIDATE — complete written argument, separate reconstruction and parent acceptance pending; NOVELTY_UNCLEAR**. No scientific program, eigensolver, enumeration, optimizer or executable certificate replay was used.

This is the next own-primary obligation pursued after returning the PH6 review. Unlike the preceding state-region candidates, the theorem below has **no input restriction**. The full all-noise target still has the low-noise indices k=2,3,4 unresolved.

## 1. Literal statement and baseline delta

For any four-qubit density matrix rho, put

`X_s(rho)=sum_(|I|=s) rho_I tensor I_(I^c)`,

with unnormalized identity factors. Let `T_s=X_s(|0000><0000|)` and let K_k be the leading k-eigenvalue sum.

**Theorem C.** For **every** four-qubit state rho, including mixed states,

`K_k(X_2(rho))<=k+13=K_k(T_2)` for `k=6,7,8,9,10`.                  (C)

Consequently these five previously missing depolarizing-output partial sums hold for every input and every physical **replacement parameter** `0<=p<=4/3`, with `D_p(X)=(1-p)X+(p/2)Tr(X)I`.

Together with the actual inherited partial package, this implies **full four-qubit output majorization for every rho whenever 2/3<=p<=4/3**. For `0<p<2/3`, only k=2,3,4 remain unclosed by the combined arguments. This is not a claim to have proved those low-noise inequalities, a general-n theorem, or the book's quantum-capacity problem.

The target and primary convention remain SWTF [2609.37240v1](https://arxiv.org/abs/2609.37240v1), Eq.(2), n=4,d=2. The new proof neither imports its weaker logdet order nor assumes the old PPT/Gram relaxation is tight.

## 2. A universal operator lower bound that retains the useful half-strength

Let `tilde(rho)=sigma_y^tensor4 rho^T sigma_y^tensor4`. This is a positive trace-one state: it is global transpose followed by a unitary conjugation.

The single-qubit identity `sigma_y Y^T sigma_y=Tr(Y)I-Y` tensors to the exact inclusion-exclusion identity

`tilde(rho)=I-X_1+X_2-X_3+rho`.                                    (2)

For any qubit i and any state rho,

`rho_(complement i) tensor I_i >=rho/2`.                           (3)

Here is an elementary proof, including arbitrary rest dimension. For a pure input, Schmidt-decompose across i versus the other three qubits as `psi=sqrt(mu)|0>alpha+sqrt(nu)|1>beta`, with mu+nu=1. For any vector v,

`|<psi|v>|^2 <=2mu|<0,alpha|v>|^2+2nu|<1,beta|v>|^2`

`              <=2<v|rho_(complement i) tensor I_i|v>`.

The first line is the two-term Cauchy inequality; the second includes only part of the nonnegative marginal quadratic form. Linearity extends the operator inequality from pure to mixed inputs. Summing (3) over the four sites gives `X_3>=2rho`.

Rearrange (2):

`X_2=X_1-I+(X_3-rho)+tilde(rho)`

`   >=X_1-I+rho+tilde(rho) >=X_1-I`.                               (4)

This holds for every state, without constant local spectra, a product ansatz or pure-state restrictions. Also X_2>=0 and Tr X_2=24.

Write the one-qubit marginals as `rho_i=(I+r_i dot sigma)/2`, and let `t_i=|r_i| in[0,1]`. After local diagonalization,

`X_1-I=I+(1/2)sum_i t_i sigma_z^(i)`.

Thus its eigenvalues are `1+eta_j/2`, where eta is the sixteen signed sums `sum_i epsilon_i t_i`, ordered decreasingly. Their symmetry gives `eta_(17-j)=-eta_j`, and the largest eight eta values are nonnegative (zeros included). From (4) and X_2>=0, eigenvalue monotonicity yields

`lambda_j(X_2)>=max(0,1+eta_j/2)`, `j=1,...,16`.                    (5)

This is an eigenvalue statement. It does not assert that taking the positive part preserves arbitrary Loewner inequalities.

The earlier Weyl route used `X_2>=2X_1-3I`, whose coefficient on the local Kronecker sum is one rather than one half. That bound is stronger on positive eta but weaker on the negative tail. Replacing it by the valid half-strength bound is material for the central Ky-Fan sums; it is not a claim that one operator dominates the other for all local eigenvectors.

## 3. A clipped four-sign inequality

**Lemma H4.** For `0<=t_i<=1`, let `a_1,...,a_8` be the eight nonnegative signed sums, paired with their negatives and counted with multiplicity. Then

`sum_(j=1)^8 min(a_j,2)<=10`.                                      (6)

*Proof.* Permuting qubits, take `t_1>=t_2>=t_3>=t_4>=0` and set

`A=t_1+t_2`, `B=t_1-t_2`, `C=t_3+t_4`, `D=t_3-t_4`.

We have `A>=C>=D>=0`, `B>=0`, `A+B<=2`, and

`B+C<=A<=2`, `B+D<=B+C<=2`.

Indeed t_3+t_4<=2t_2. The eight nonnegative magnitudes are, with their exact multiplicities,

`|A+C|,|A-C|,|A+D|,|A-D|,|B+C|,|B-C|,|B+D|,|B-D|`.

This remains true with zero t_i or repeated/zero signed sums. Define

`L(x,y)=min(x+y,2)+min(|x-y|,2)` for x,y>=0.

The desired sum is `L(A,C)+L(A,D)+L(B,C)+L(B,D)`. Since B+C and B+D are at most two, the last two terms are exactly

`L(B,C)=2max(B,C)`, `L(B,D)=2max(B,D)`.

For y=C,D, A>=y and A-y<=2, hence

`L(A,y)=min(A+y,2)+A-y`.

This expression is nondecreasing in A. Keeping B,C,D fixed, enlarge A to `A'=2-B>=A`. The order A'>=C,D persists. Since C,D<=2 and A'-C,A'-D<=2, the same formula applies at A'. Directly considering whether y>=B gives

`L(2-B,y)=4-B-max(B,y)`.

Therefore the entire clipped sum is at most

`8-2B+max(B,C)+max(B,D)`

` <=8-2B+(B+C)+(B+D)=8+C+D=8+2t_3<=10`.

This proves (6) symbolically for the whole four-dimensional cube; no grid enumeration or numerical optimization is used. Equality is possible, for example at t_1=t_2=t_3=1 and any t_4 in[0,1].

## 4. Bottom spectral sums and the central bounds

Apply Lemma H4 to the positive half of eta. For the eight nonpositive eta values the lower bounds in (5) sum to

`F=sum_(j=1)^8 (1-a_j/2)_+`

` =8-(1/2)sum_(j=1)^8 min(a_j,2) >=3`.                             (7)

Each of these eight scalar lower bounds lies in [0,1]. For a tail of m=6,7,8 eigenvalues, its lower-bound sum is at least F minus at most 8-m omitted terms of size at most one. Thus

`sum_(j=17-m)^16 lambda_j(X_2)>=F-(8-m)>=m-5`.

For m=8,9,10, the eight nonpositive-eta positions contribute at least F, and the additional m-8 nonnegative-eta positions each contribute at least one. Hence again

`sum_(j=17-m)^16 lambda_j(X_2)>=F+(m-8)>=m-5`.

These deductions subtract bounds from the scalar sequence on the right side of (5), **not unknown upper bounds on actual X_2 eigenvalues**. At zeros, either half assignment gives exactly the value one, so ties cause no gap.

For each central k=6,...,10, put m=16-k, also in6,...,10. Since Tr X_2=24,

`K_k(X_2)=24-sum_(j=k+1)^16 lambda_j(X_2)`

`          <=24-(m-5)=k+13`.

The product T_2 spectrum is `6,3,3,3,3,1,1,1,1,1,1,0,0,0,0,0`; its central sums are precisely k+13. This proves Theorem C.

## 5. Channel bridge and the remaining low-noise target

For q in[0,1], the exact expansion is

`D_q^tensor4(rho)=sum_(s=0)^4 a_s X_s(rho)`,

`a_s=(1-q)^s q^(4-s)2^(s-4)>=0`.

At central k, X_0=I and X_4=rho have immediate bounds. X_1 is a Kronecker sum of one-qubit marginals, majorized by T_1 via the mixture of local bit-flip conjugates. X_3 is positive of trace eight, and K_k(T_3)=8 for k>=5. Theorem C supplies the only missing subset-size bound. All product T_s have diagonal entries `binom(z,s)`, z the number of zero bits, so their leading sums share Hamming order. Ky-Fan subadditivity and common ordering give the exact central channel inequalities.

For 1<p<=4/3, use `q=2-p` and the tensor identity

`D_(2-p)^tensor4(rho)=sigma_y^tensor4 [D_p^tensor4(rho)]^T sigma_y^tensor4`.

It preserves the spectra of both the arbitrary output and the product reference. Thus all physical replacement p are covered at the five central indices.

The inherited package already closes indices1,5,11..15 for every physical p, and indices2,3,4 for `2/3<=p<=4/3`. That package was actually read with its operative correction and review:

- `physics/evidence/six-lane-20261016/depolarizing-majorization-n4/frozen-partial-v1/PROOF.md`, SHA `6789e392dbc70dbed479ba8f307e0eb6c786d735de691d425583ec0d8b2fce8a`;
- `ADDENDUM_v1_1.md`, SHA `73b6abb4e0a10b4fb9fe54ae5be853130c45a466b65a258c17385bc9911267d4`;
- its actual stored `review/codex-frozen-partial-output.md`.

Combining that precise baseline with Theorem C proves the stated full high-noise interval. Its earlier central-index status remains an immutable historical baseline; the present proof is not retroactively inserted into old receipts.

For `0<p<2/3`, the unrestricted k=2,3,4 bounds remain. A sufficient remaining ingredient is the true compatible-marginal inequality `K_k(X_3)<=3+k` at k=2,3,4 (or a direct combined-channel inequality). The previous loose Pauli-Gram/PPT encoding does not supply it. The state-region and near-product candidates remain scoped auxiliary results, not substitutes for this residual.

## 6. Review and novelty boundary

All input and parameter quantifiers in Theorem C are unrestricted within four qubits and the stated physical channel. The proof uses a universal reduction estimate, exact spin-flip inclusion-exclusion, an elementary four-sign clipped inequality, eigenvalue monotonicity and trace. No coefficient fit, surrogate order, incompatible marginal tuple, optimized numerical state or unproved Z-lemma is a premise.

Correctness status is **CANDIDATE pending separate pinned reconstruction and parent acceptance**. No formal/kernel or human verification occurred. These elementary mechanisms may have prior equivalents; a bounded source search is not a priority certificate. The full all-noise four-qubit target and the broad book question are not declared solved.
