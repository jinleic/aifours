# Conditional four-qubit majorization from marginal moments and rank

Observed before freezing: **2026-10-23T14:07:28-0700**. Author: PhysicsDepol4. Evidence level: **CANDIDATE, written derivation only**. No scientific program, numerical eigensolver, optimizer or executable check was used. The unrestricted assigned conjecture is **not solved**. This is one partial attack on that conjecture, not a replacement problem or a discovery claim.

## 1. Statements

Let `rho=|psi><psi|` be an arbitrary pure four-qubit state. Write the one-qubit marginals as `rho_i=(I+r_i dot sigma)/2`, and define

`R = sum_{i=1}^4 |r_i|^2`,

`C = |<psi|sigma_y^tensor4|bar(psi)>|^2`.

Thus `0<=R<=4`, `0<=C<=1`. `C` is the **squared** global spin-flip overlap; no assertion that it measures only genuine four-party entanglement is made. Use the unnormalized-identity convention

`X_s = sum_{|I|=s} rho_I tensor I_{I^c}`.

Let `T_s=X_s(|0000><0000|)` and `K_k` denote the sum of the `k` largest eigenvalues.

**Theorem A — central indices, state-dependent analytic certificate.** For `6<=k<=10`, set

`H_k = (k+13)^2/k + (11-k)^2/(16-k) - 38`.

If `10R+4C <= H_k`, then `K_k(X_2)<=k+13`. Consequently the previously missing **same k** depolarizing-output inequality holds for this input for every physical replacement parameter `0<=p<=4/3`.

The exact thresholds are:

| k | H_k | sufficient R-only condition, using R+4C<=4 |
|---|---|---|
| 6 | 74/3 | R<=62/27 |
| 7 | 1318/63 | R<=1066/567 |
| 8 | 73/4 | R<=19/12 |
| 9 | 1030/63 | R<=778/567 |
| 10 | 226/15 | R<=166/135 |

In particular, `10R+4C<=226/15` closes **all five central indices** for every physical p. The thresholds decrease along this table; they are sufficient, not claimed optimal.

**Theorem B — complete majorization on a certified pure-state region.** If

`3R+2C <= 157/36`,                                                   (B)

then for every `0<=p<=4/3`,

`lambda_down(D_p^tensor4(rho)) prec lambda_down(D_p^tensor4(|0000><0000|))`.

This statement includes **all fifteen** spectral partial sums, but only the specified input region. It also holds for any mixed state admitting a convex decomposition into pure states satisfying (B). It does **not** assert that a mixed state with small one-body Bloch vectors automatically has such a decomposition.

**Corollary B1.** Every pure state with `R<=17/18` satisfies complete majorization for all physical p. In particular, every pure state whose four one-qubit marginals are all maximally mixed is covered.

These are algebraic sufficient regions. Their omission from the read baseline is not a literature-wide novelty clearance.

## 2. A spectral moment lemma, including its rank dependence

Let `A>=0` have rank at most `r`, trace `t`, and squared Hilbert-Schmidt norm `q=Tr A^2`. Pad its nonzero spectrum to length r with zeros. For `1<=k<r`, put `S=K_k(A)`. Cauchy-Schwarz separately on the first k and last r-k entries gives

`q >= S^2/k + (t-S)^2/(r-k) =: f_k(S)`.                             (1)

The right side is increasing for `S>=kt/r`, since

`f_k'(S) = 2(rS-kt)/(k(r-k))`.

Also `S>=kt/r` by sortedness. Therefore, if `B>=kt/r` and

`q <= B^2/k + (t-B)^2/(r-k)`,                                      (2)

then `K_k(A)<=B`. This is a genuine one-sided partial-sum certificate at the displayed moment threshold; the proof does **not** infer majorization merely from comparison of purities with a reference state.

Equivalently, for dimension r,

`K_k(A) <= kt/r + sqrt(k(r-k)/r * (q-t^2/r))`.                      (3)

All uses below are within the monotone branch. If the actual rank is smaller than r, padding is legitimate and (1) still holds.

## 3. Pure-state compatibility identities

Expand rho in the four-qubit Pauli basis:

`rho = (I+P_1+P_2+P_3+P_4)/16`,

where `P_j` is the sum of its real Pauli coefficients times the weight-j Pauli strings. Set `A_j=Tr(P_j^2)/16`, and `A_0=1`. Orthogonality of different Pauli strings gives

`A_1=R`, and `1+A_1+A_2+A_3+A_4=16`.                               (4)

For each pure bipartition `i | complement(i)`, the one- and three-qubit marginals have the same nonzero eigenvalues. Summing their purities yields

`(4+3A_1+2A_2+A_3)/8 = (4+A_1)/2`.

Thus

`A_3=12+A_1-2A_2`, and `A_4=3-2A_1+A_2`.                          (5)

Global spin flip changes the sign of every odd-weight Pauli string. Therefore

`C = Tr(rho * tilde(rho)) = (1-A_1+A_2-A_3+A_4)/16`

`  = (A_2-A_1-2)/4`.

Solving gives the exact identities

`A_2=R+2+4C`, `A_3=8-R-8C`, `A_4=5-R+4C`.                         (6)

These sector-length/purity methods are classical, not inventions of this round. The definitions and the pure-state marginal-purity relations appear in Wyderka–Gühne, [arXiv:1905.06928v3](https://arxiv.org/pdf/1905.06928), Eqs. (1), (3), (4), with spin inversion discussed there as well. Equations (4)–(6) are fully derived above, so this proof does not depend on importing an unverified assertion from that paper.

Directly tracing out the Pauli expansions gives

`X_2 = (3/2)I + (3/4)P_1 + (1/4)P_2`,

`X_3 = (1/2)I + (3/8)P_1 + (1/4)P_2 + (1/8)P_3`.

Consequently

`Tr X_2 =24`, `Tr X_2^2 =36+9A_1+A_2 =38+10R+4C`,                 (7)

`Tr X_3 =8`, `Tr X_3^2 =4+(9/4)A_1+A_2+A_3/4 =8+3R+2C`.          (8)

No finite evaluations are used to infer these polynomial identities.

## 4. Rank at most thirteen for X_3

Define

`Z=sum_{i=1}^4 sum_{a=x,y,z} sigma_a^(i) rho sigma_a^(i)`.

For any 2x2 matrix Y, `sum_a sigma_a Y sigma_a =2Tr(Y)I-Y`. Applying this at each qubit gives

`Z=2X_3-4rho`, hence `X_3=2rho+Z/2`.                              (9)

For pure rho, Z is the sum of twelve positive rank-one operators, with vectors `sigma_a^(i)psi`. Thus the support of X_3 is contained in the span of psi and these twelve vectors:

`rank X_3 <=13`.                                                   (10)

This uses the **exact orbit rank**, not the earlier loose PPT/Pauli-Gram relaxation and not its unproved Z-majorization lemma. No bound on the top eigenvalues of Z is assumed.

## 5. Proof of Theorem A

The product-reference X_2 spectrum is

`(6,3,3,3,3,1,1,1,1,1,1,0,0,0,0,0)`.

For `6<=k<=10`, its leading sum is `B=k+13`. Apply the moment lemma with `r=16,t=24,q=38+10R+4C`. Since `B>24k/16` throughout this range, the lemma applies. Its threshold is exactly

`B^2/k+(24-B)^2/(16-k) =38+H_k`.

This proves `K_k(X_2)<=K_k(T_2)` under the stated condition. For example k=6 has threshold

`19^2/6 +5^2/10 =188/3`,

so `10R+4C<=74/3` is sufficient.

For the channel bridge, put `q=min(p,2-p)` and write

`D_q^tensor4(rho)=sum_{s=0}^4 a_s X_s`, `a_s=(1-q)^s q^(4-s)2^(s-4)>=0`.

At k=6..10 the other subset-size bounds require no unproved majorization theorem: `X_0=I`; `K_k(rho)<=1`; `X_1` is the sum of four commuting one-qubit marginals and is majorized by T_1 (diagonalize each marginal, then mix the sixteen bit-flipped product-reference Kronecker sums); and `K_k(X_3)<=Tr X_3=8=K_k(T_3)` for k>=5. All T_s have diagonal entries `binom(z,s)`, with z the number of zero bits, so their leading eigenspaces share Hamming order. Ky-Fan subadditivity therefore gives

`K_k(D_q^tensor4(rho)) <=sum_s a_s K_k(T_s) =K_k(D_q^tensor4(|0000><0000|))`.

Finally `sigma_y D_p(X)^T sigma_y =D_(2-p)(X)` tensors to global transpose followed by unitary conjugation. This preserves both output spectra and proves the bridge for `p>1` as well.

To obtain the R-only conditions, Section 7 proves `R+4C<=4`; hence `10R+4C<=9R+4`. Substitution into the thresholds gives the table exactly.

## 6. Proof of Theorem B, without importing the earlier LP certificates

Condition (B), together with C>=0, implies

`10R+4C = (10/3)(3R+2C) -(8/3)C <=785/54`.

Thus

`Tr X_2^2 <=2837/54 <796/15`; the exact positive difference is `143/270`.

For the product X_2 target, the moment-lemma thresholds for k=2..10 are:

| k | target B=K_k(T_2) | B^2/k+(24-B)^2/(16-k) |
|---|---|---|
| 2 | 9 | 396/7 |
| 3 | 12 | 768/13 |
| 4 | 15 | 63 |
| 5 | 18 | 3744/55 |
| 6 | 19 | 188/3 |
| 7 | 20 | 3712/63 |
| 8 | 21 | 225/4 |
| 9 | 22 | 3424/63 |
| 10 | 23 | 796/15 |

Each entry is at least 796/15. The comparison is rational arithmetic on displayed expressions, not a software assertion. Therefore `K_k(X_2)<=K_k(T_2)` for k=2..10. At k=1, each of the six positive marginal terms is bounded above by I, so `X_2<=6I`; at k>=11 the target sum is the full trace 24. This establishes **X_2 majorization at every index for this input**.

For X_3, condition (B) gives `Tr X_3^2<=445/36`. Use its rank bound r=13 and trace t=8 from (8)–(10). The target spectrum is `(4,1,1,1,1,0,...,0)`. The thresholds at the three nontrivial indices are:

| k | target B=K_k(T_3) | B^2/k+(8-B)^2/(13-k) |
|---|---|---|
| 2 | 5 | 293/22 |
| 3 | 6 | 62/5 |
| 4 | 7 | 445/36 |

All are at least 445/36. The monotone-branch condition B>=8k/13 holds. Therefore `K_k(X_3)<=K_k(T_3)` at k=2,3,4. The k=1 bound `X_3<=4I` is termwise; k>=5 is the trace bound 8. This establishes **X_3 majorization at every index for this input**.

The same X_0, X_1, X_4 bounds and common-order argument of Section 5 now work at **every** k=1..15. Reflection covers p>1. This proves Theorem B. By convexity of the Ky-Fan sums, every convex combination of pure inputs satisfying (B) obeys the same channel inequalities. No compatibility condition is incorrectly imposed on the marginals of a general mixed input.

## 7. Proof of R+4C<=4 and Corollary B1

Fix a qubit i and take its Schmidt decomposition

`psi=sqrt(mu)|0>alpha +sqrt(1-mu)|1>beta`,

with alpha,beta orthonormal on the other three qubits. Local unitary rotations do not change either `|r_i|` or the magnitude of the global spin-flip overlap. The single-qubit spin flip interchanges the two Schmidt basis vectors up to phases. Expanding `<psi|tilde(psi)>` therefore has two cross terms, each with coefficient `sqrt(mu(1-mu))`; their inner products have modulus at most one. Hence

`C<=4mu(1-mu)=1-|r_i|^2`.

Sum over i to get `R+4C<=4`. Consequently

`3R+2C <=2+(5/2)R <=2+(5/2)(17/18) =157/36`

whenever R<=17/18. This proves the corollary.

## 8. Scope, baseline delta and the still-missing ingredient

This manuscript gives a **state-dependent, all-noise, exact written certificate** for formerly unresolved four-qubit partial sums, plus a region on which all fifteen sums hold. It does not merely restate a weaker logdet/Schatten order and does not require the prior numerical hierarchy to be tight. For the main conditional theorem the earlier exact LP package is not an import at all.

However, pure products have `(R,C)=(4,0)`, outside (B), and still saturate the full conjecture. So (B) is not necessary; it cannot be promoted to the unrestricted target. A pure counterexample at k=6 would have to satisfy `10R+4C>74/3` and hence `R>62/27`. A pure counterexample at any index must lie outside (B), hence outside the sufficient ball R<=17/18. These are exclusions of counterexample regions, not counterexamples or a global nonexistence proof.

The next missing ingredient is **spectral compatibility beyond the first two moments** for weakly entangled/high-local-purity pure states. Moment bounds alone are insufficient there: the artificial positive spectrum `(10/3 repeated 6 times, 2/5 repeated 10 times)` has trace 24, squared norm `1024/15<78=Tr(T_2^2)`, and `K_6=20>19`. It obeys the already-closed U_2 bounds k=1..5 and k>=11, but is not asserted to be any X_2(rho). This shows precisely why replacing the actual pure-state marginal structure by a purity comparison cannot finish the unrestricted argument.

Review status: author-written only, awaiting parent/separate in-harness reconstruction of pinned bytes. No formal proof, human review, cross-vendor review, numerical verification, literature priority, full-target solution or new global Ky-Fan-index closure is claimed.
