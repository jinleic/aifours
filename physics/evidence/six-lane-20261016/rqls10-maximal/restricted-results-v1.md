# rqls10-maximal: restricted-ansatz results, detailed derivations (v1)

Lane-internal derivations; **unreviewed**. Every statement here is about a *restricted ansatz*. None is a statement
about arbitrary complex vectors and arbitrary resolutions. None is evidence for or against the target. They are
recorded separately from the target and must not be cited as no-go theorems until reviewed.

External imports are marked [IMPORT]:
- Rédei's direction theorem.
- The cardinality facts for QLS(2), QLS(3) and 1-RQLS(4), 1-RQLS(5), as cited by Zhang-Cao (Paczos et al.;
  Ball-Simoens).
- The bound that a proper Latin subsquare has order at most n/2.

Conventions:
- omega = e^{2 pi i/10} and zeta = e^{2 pi i/5}.
- CRT coordinates: x in Z_10 corresponds to (x2, x5) = (x mod 2, x mod 5), and x = 5*x2 + 6*x5 (mod 10).
- Hence omega^x = (-1)^{x2} zeta^{3 x5}.

## R3. Flat Fourier-permutation ansatz: no orthonormal transversal when mu(t) - t is non-constant mod 2

**Ansatz.**
- mu is a permutation of Z_10.
- q_ij = (1/sqrt10) (omega^{i mu(t) + j t})_{t in Z_10}, for i, j in Z_10.
- Rows and columns are orthonormal automatically.
- Phi(a,b) := sum_t omega^{a mu(t) + b t}, so that <q_ij, q_i'j'> = Phi(i'-i, j'-j)/10.

This family is closed under the natural equivalences: permuting or rephasing coordinates t, permuting rows and
columns, and scaling by units.

**Hypothesis (H).** pi(t) := mu2(t) + t2 (mod 2) is not constant.
- If pi is constant, then 5 mu(t) + 5 t is constant. Hence q_ij is parallel to q_{i+5,j+5} for all i, j, and the
  square has at most 50 rays.
- Therefore maximal cardinality implies (H).

**Theorem R3.** Under (H) there is no permutation sigma of Z_10 with {q_{i,sigma(i)}} pairwise orthogonal.
Consequently:
- for every Latin square B, (B,q) is not a 1-RQLS(10), because each class T_s = {(i, sigma_s(i))} would be such a
  set;
- every 1-RQLS(10) of this form has at most 50 rays.

### Lemma A (zero test)

Put u(t) = a2 mu2(t) + b2 t2 (mod 2) and y(t) = a5 mu5(t) + b5 t5 (mod 5). Then Phi(a,b) = 0 iff one of the
following holds:
- (I) every fibre y^{-1}(c) contains equally many t with u = 0 and with u = 1;
- (II) u is constant and every fibre of y has exactly two elements.

*Proof.*
1. Phi = sum_c k_c zeta^{3c}, where k_c = sum_{t in y^{-1}(c)} (-1)^{u(t)} is an integer.
2. 1, zeta, zeta^2, zeta^3 are Q-independent and 1 + zeta + ... + zeta^4 = 0. So Phi = 0 iff all k_c equal a
   common value kappa.
3. Let n_c be the size of fibre c. Then |kappa| <= n_c, kappa = n_c (mod 2), and sum_c n_c = 10.
4. kappa odd forces every n_c odd, so the sum of five odd numbers is odd, not 10. Impossible.
5. |kappa| >= 4 forces sum_c n_c >= 20. Impossible.
6. |kappa| = 2 forces every n_c = 2 with equal signs everywhere. That is (II).
7. kappa = 0 is (I).
8. The converse is immediate. QED

### Proof of Theorem R3

Suppose sigma is a permutation with Phi(i'-i, sigma(i')-sigma(i)) = 0 for all i != i'.

**Step 1: pairs (i, i+5).**
- Here a = 5, so (a2, a5) = (1, 0). Let b = sigma(i+5) - sigma(i), which is nonzero.
- Case (alpha): b = 5. Then y = 0 and there is one fibre of size 10. (II) is impossible. (I) reads
  #{t : pi(t) = 0} = 5. Call this (C0).
- Case (beta): b5 != 0 and b2 = 0. The fibres are {(0,x),(1,x)}, and u = mu2.
  - (II) would need mu2 constant, which is impossible for a bijection.
  - (I) reads mu2(0,x) != mu2(1,x) for every x ("mixed").
  - Mixed gives pi(0,x) = pi(1,x), so #{pi = 0} is even and (C0) fails.
- Case (gamma): b5 != 0 and b2 = 1. Then u = pi.
  - (II) is excluded by (H).
  - (I) gives mu2(0,x) = mu2(1,x) for every x ("pure"). Then #{mu2 = 0} is even, contradicting bijectivity.
- So (alpha) and (beta) cannot both occur among the five pairs, and (gamma) never occurs.
- All-(beta) is also impossible. It would make sigma map the five pairs {i, i+5} onto five same-parity pairs, but
  Z_10 has five even elements, an odd number.
- Hence sigma(i+5) = sigma(i) + 5 for all i, and (C0) holds.

**Step 2: form of sigma.** sigma(i2+1, i5) = sigma(i2, i5) + (1, 0). So sigma(i) = (i2 + g(i5), h(i5)) with h a
permutation of Z_5.

**Step 3: dual condition.**
- The vectors w_i = q_{i,sigma(i)} form an ONB, so sum_i |w_i><w_i| = I.
- For t != t' this gives Psi := sum_i omega^{i alpha + sigma(i) beta} = 0, where alpha = mu(t) - mu(t') and
  beta = t - t'.
- Psi factors as (sum over i2 of (-1)^{i2(alpha2 + beta2)}) times (sum over i5 of (-1)^{g(i5) beta2}
  zeta^{3(i5 alpha5 + h(i5) beta5)}).
- The first factor is nonzero iff alpha2 = beta2, i.e. iff pi(t) = pi(t').
- A five-term sum of +-zeta^k vanishes iff its exponents are distinct and its signs are equal.
- So, for t != t' with pi(t) = pi(t'), condition (D) holds:
  - i5 -> i5 alpha5 + h(i5) beta5 is a bijection of Z_5;
  - if t2 != t2', then g is constant.

**Step 4: g is constant.**
- Let P_r = pi^{-1}(r). By (C0), |P_r| = 5.
- Suppose g is not constant. By (D), each P_r then lies in a single level {t2 = c_r}. Since the level also has 5
  elements, P_r is that level.
- Then mu2 = c_0 on both levels. This contradicts bijectivity.
- So sigma(i) = (i2 + r, h(i5)).

**Step 5: primal condition.**
- Take i5 != i5' and set (a5, b5) = (i5'-i5, h(i5')-h(i5)). Both entries are nonzero, and a2 = b2 can be 0 or 1.
- For a2 = 0: u = 0, so (II) applies and every y-fibre has exactly two elements.
- For a2 = 1: u = pi, (I) applies by (H), and every fibre is pi-balanced.
- Together, condition (P) holds: t -> a5 mu5(t) + b5 t5 is injective on P_0 and on P_1.

**Step 6: spectral pair and Rédei.**
- Let E_r = {(t5, mu5(t)) : t in P_r} and Gamma = graph of h, both in AG(2,5).
- By (P), the functional (x,y) -> b5 x + a5 y is injective on E_r. Hence E_r has 5 distinct points. Moreover E_r
  determines no direction (a5, -b5) for any direction (a5, b5) determined by Gamma.
- [IMPORT: Rédei 1970; Lovász-Schrijver 1981] A p-set in AG(2,p), p prime, that is not a line determines at least
  (p+3)/2 directions. For p = 5 that is at least 4 of the 6 directions.
- So if Gamma is not a line, each E_r determines at most 2 directions and is therefore a line.

**Step 7: contradiction.**
- *Gamma is a line.*
  - Then h(i5) = lambda i5 + c with lambda != 0. So sigma(i) = lambda' i + c' with lambda' a unit of Z_10, and
    lambda' is odd.
  - Phi(a, lambda' a) = 0 for all a != 0. Hence nu = mu + lambda' id is a bijection.
  - Then sum_t nu(t) = (1 + lambda') * 45 = 0 (mod 10). But summing a bijection gives 45 = 5 (mod 10).
- *Gamma is not a line.*
  - Then E_0 and E_1 are both non-vertical lines.
  - Each P_r contains exactly one t over each t5. So P_0 = {(s(x), x)} and P_1 = {(1 - s(x), x)}.
  - On P_0, mu2 = s(x) because pi = 0. On P_1, mu2 = (1 - s(x)) + 1 = s(x) because pi = 1.
  - Hence #{mu2 = 0} = 2 #{x : s(x) = 0} is even. A bijection would give 5.
- Both cases are contradictory. QED

**Scope.**
- This is one explicit vector family. Arbitrary complex vectors and arbitrary B are not covered.
- The case pi constant gives at most 50 rays. This matches the contract's warning that 50-ray tensor-type
  constructions do not suffice.

## R1. Laminar coordinate rotations from a classical pair

**Setting.**
- Start from a classical 1-RQLS(10): (A0, B) is a MOLS(10) pair and q_p = |A0(p)>.
- A *move* (S, K, U):
  - K is a symbol set with |K| >= 2;
  - S is a nonempty union of connected components of the K-subnet. The K-subnet consists of the cells with
    A0 in K; two cells are adjacent when they share a row, column or B-class;
  - U is a unitary on span{|k> : k in K}, extended by the identity elsewhere;
  - the move applies U to q_p for every p in S.
- A family of moves is *laminar-nested* if any two moves have disjoint S, or S_m is contained in S_n with K_m
  contained in K_n (or the reverse). Moves are applied innermost first.
- Such moves preserve every line-ONB condition. A line meeting S has all its K-cells in S, and their vectors stay
  an ONB of span K.

**Lemma.** A component C of a K-subnet with |K| >= 2 contains at least two cells of each symbol it contains.
- Let p in C have symbol a, and pick b in K \ {a}.
- The row of p and the column of p contain distinct b-cells r and c, both in C.
- The a-cell in the column of r is in C and differs from p.

**Claim R1.** Every final configuration has repeated rays.
- Take an inclusion-minimal move set S.
- Every move touching a cell of S contains all of S, so all cells of S receive the same product of unitaries.
- By the Lemma, S contains two cells with equal initial vector |a>, and these end with equal rays.

**Scope.** Only coordinate-subspace moves in laminar order are covered.

## R2. Superposing two classical mates

**Ansatz.** A1 and A2 are Latin squares, each orthogonal to B. Set:
- q_p = |a> if A1(p) = A2(p) = a;
- otherwise q_p is proportional to |A1(p)> + e^{i phi_p} |A2(p)>.

**Consequences of orthogonality on a line.**
- For p != p' on a line, <q_p, q_p'> is proportional to
  e^{i phi_p'} [A1 p = A2 p'] + e^{-i phi_p} [A2 p = A1 p'].
- The partner p' of a non-fixed cell p on a line has A1(p') = A2(p). Then A2(p') = A1(p) and
  e^{i phi_p'} = -e^{-i phi_p}.
- Following partners twice returns the same phase. So all cells of type (a,b) in one partner component share the
  ray |a> + e^{i phi}|b>.
- Each component contains at least two such cells: take the column partner of the row partner of p.
- So rays repeat. If there are no non-fixed cells, the square is classical.

## R4. Translation-group orbit ansatz with G = Z_10^2 (B isotopic to Cay(Z_10))

**Ansatz.**
- q_g = pi(g) q0 for a projective unitary representation pi of G on C^10.
- Lines are the cosets of H_R = Z_10 x 0, H_C = 0 x Z_10 and H_T = {(a, lambda a)}, with lambda a unit.
- Requirement: {pi(h) q0 : h in H_X} is an ONB for X = R, C, T.
- Under CRT, H^2(G, U(1)) = Z_2 x Z_5. The commutator values have coprime orders, so pi splits accordingly.

**Cases.**
- *Trivial x trivial.* Commuting diagonal operators. ONB-ness forces uniform push-forwards, which gives a
  complete mapping of Z_10. Impossible.
- *Pauli x diagonal.*
  - For each s, the qubit part w_s needs <X> = <Y> = <Z> = 0 with w_s != 0. Impossible.
  - This comes from the H_R, H_C, H_T conditions combined with bijective character labels.
- *Diagonal x WH_5.*
  - The H_R and H_C conditions force alpha_0 != alpha_1 and beta_0 != beta_1.
  - The H_T condition with lambda odd needs alpha_0 + beta_0 != alpha_1 + beta_1. Contradiction.
- *Pauli x WH_5 = WH_10.* UNKNOWN. It reduces to:
  - an orthonormal pair u, w in C^5;
  - u and w flat in the computational basis;
  - (u ± w)/sqrt2 flat in the Fourier basis;
  - (u ± i w)/sqrt2 flat in the eigenbasis of X_5 Z_5^{3 lambda}.

  The single numeric probe found best residuals 0.0523 (lambda = 3, 7) and 0.2020 (lambda = 1, 9), with no
  candidate. This is numeric and non-certifying.

**Scope.** Only G = Z_10^2 is covered. Non-abelian regular groups of order 100 and non-regular orbit ansätze are
not covered.

## R5. Half-splits

Suppose every q_p lies in W or in W^perp.

- **dim W = 5, rectangular.** Suppose the W-cells form (R1 x C1) union (R2 x C2) with all four sets of size 5. A
  B-class meeting R1 x C1 in x cells has 2x W-cells, but it needs 5. Impossible (Mann parity).
- **dim W = 2.** The W-cells carry the rays u and u^perp alternately along components. The column partner of the
  row partner of p repeats the ray of p.
- **dim W = 3 with a 3x3 W-block.** A 3x3 W-block closed in its rows and columns is a QLS(3) on W.
  [IMPORT: every QLS(3) has cardinality 3.]

Non-rectangular W-cell patterns are **not covered**.

## R6. Common orthogonal subsquares

- [IMPORT] A proper subsquare of a Latin square of order 10 has order s <= 5.
- [IMPORT, via Zhang-Cao] Every 1-RQLS(s) with s <= 5 has cardinality s, and none exists for s = 2.
- So replacing a common orthogonal subsquare repeats rays inside the block.
