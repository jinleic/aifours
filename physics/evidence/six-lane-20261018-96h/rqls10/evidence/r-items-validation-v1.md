# W1: re-derivation of the inherited restricted results R1-R10 (validation note v1)

Recorded 2026-10-18T23:26:42-0700. Written re-derivation by ContinueRQLS10 of the old lane files (hashes in review/plan-v1.md). This is a
single-author check, not an independent review. Every item below concerns a restricted vector family or ansatz;
none is a statement about arbitrary vectors and arbitrary Latin squares, so none changes the target status (OPEN).
Verdict vocabulary: VALID (argument re-derived, possibly with a repaired or simplified step), VALID-WITH-IMPORT
(re-derived modulo the named external theorem), DEFECT (gap found).

| item | statement (short) | verdict |
|---|---|---|
| Lemma A | zero test for Phi(a,b) = sum_t omega^(a mu(t) + b t), omega = e^(2 pi i/10) | VALID |
| R3 | flat Fourier-permutation family: no orthonormal transversal when pi = mu_2 + t_2 is non-constant; at most 50 rays otherwise; for every B | VALID-WITH-IMPORT (Redei for p = 5; exact finite check proposed in W3) |
| Lemma Q, Q3 | quaternary parity in length 10 | VALID |
| R9 | Paley x Paley products (any coordinate permutation, any phases): no orthonormal transversal | VALID |
| R10 | Paley x any i-free complex Hadamard: no orthonormal transversal | VALID |
| R4 | Z_10^2 projective orbit ansatz: three of four cocycle cases impossible; WH_10 open | VALID for the three cases; WH_10 UNKNOWN |
| R5 | rectangular 5+5 halves (Mann parity); dim-2 part; closed 3x3 dim-3 block | VALID (last part VALID-WITH-IMPORT: QLS(3) has 3 rays) |
| R6 | common orthogonal subsquares stay classical | VALID-WITH-IMPORT (subsquare order <= 5; 1-RQLS(s<=5) classical) |
| R7 | sigma (x) e with e from pairwise non-orthogonal bases of C^5 | VALID |
| R8 | controlled tensor products 2x5 and 5x2 | VALID |
| R1 | laminar coordinate-subspace moves from a classical MOLS pair | VALID (in its stated laminar setting) |
| R2 | superposing two classical mates | VALID |
| Add. 3 | flat 5th-root half-splits, uniform directions are rectangular | VALID-WITH-IMPORT (Haagerup order-5 classification) |
| Add. 5 | parity constant only for 4th roots in length 10 | VALID |
| Add. 7 | Hadamard-product family needs rank M_b <= 8 for all 45 pairs | VALID |

## Details and repairs

**Lemma A.** With CRT, omega^x = (-1)^(x_2) zeta^(3 x_5) (zeta = e^(2 pi i/5)), so Phi = sum_c k_c zeta^(3c) with
integer k_c. The only Q-relation among the five 5th roots is the all-ones relation, so Phi = 0 iff all k_c equal a
common kappa. Parity and size give kappa in {0, +-2} with |kappa| = 2 forcing all fibres of size 2 with constant u.
Re-derived exactly as recorded.

**R3, Step 3 (five-term signed sums).** The old note uses "a five-term sum of +-zeta^k vanishes iff exponents distinct
and signs equal". Elementary proof (no import): write the sum as sum_c (n_c^+ - n_c^-) zeta^c; vanishing forces
n_c^+ - n_c^- = kappa for all c; kappa = 0 would make the total number of terms even, not 5; so |kappa| >= 1 for
all five c, hence exactly one term per exponent, all of sign kappa. VALID.

**R3, Steps 1-2, 4-5.** Re-derived case by case: (gamma) contradicts bijectivity of mu (mu_2 takes 0 five times);
(alpha) and (beta) are incompatible through (C0); all-(beta) would pair the five even residues; hence
sigma(i+5) = sigma(i)+5 and sigma(i) = (i_2 + g(i_5), h(i_5)) with h a permutation. Step 4 forces g constant.
Step 5: for i_5 != i_5' the cases a_2 = 0 and a_2 = 1 both occur for the same (a_5,b_5); a_2 = 0 forces (II)
(u = 0 cannot balance non-empty fibres) and a_2 = 1 forces (I) by (H); together every y-fibre has one point of each
P_r. VALID.

**R3, Steps 6-7.** E_r avoids the slopes -s for every slope s determined by Gamma = graph(h). If Gamma is not a line it
determines all four non-axis slopes (Redei: >= (p+3)/2 = 4 directions, and a graph determines neither axis slope),
so E_r determines only axis slopes, at most 2, hence is a line; a vertical line is impossible (|P_r| = 5 > 2 points
per t_5). Simplification of the last step: a horizontal E_r means mu_5 is constant on five points, while a bijection
mu takes each mu_5 value exactly twice. Contradiction, without the parity count. If Gamma is a line, sigma is affine
with odd unit slope lambda' and mu + lambda' id would be a bijection summing to 45(1 + lambda') = 0 (mod 10), not
45 = 5 (mod 10). VALID-WITH-IMPORT (Redei's direction bound, p = 5; W3 proposes an exhaustive exact check of all
53,130 five-subsets of AG(2,5), which would remove this import for p = 5).

**Lemma Q / Q3 / R9.** <x,y> = (n_0 - n_2) + i(n_1 - n_3) = 0 gives n_0 = n_2 = A, n_1 = n_3 = C, A + C = 5;
sum h = 2A + 4C = 2A = 2 + 2C = 2 + wt(h mod 2) (mod 4). Cyclic summation gives
sum_(a<b) <tau_a,tau_b> = 1 + sum_a wt(tau_a) (mod 2). For Paley rows h_r(t) in {1} at t = r and in {+-i} otherwise,
tau of the class vector at row r is {r} symmetric-difference {rho(r)}, rho = pi^(-1) sigma, so all weights are
even and <tau_k,tau_l> is the adjacency of the functional graph of rho (max degree 2); an independent triple
exists in 10 vertices and violates Q3. Row/column phases and row/column permutations of either Paley factor are
covered (phases give a global diagonal unitary; permutations give rho). VALID.

**R10.** u = conj(h_a) o h_a' is +-1 off {a,a'} and +-i C_(aa') at a, a' (C symmetric), so with w in the i-free field F
orthogonality splits into R + i X = 0 with R, X in F, forcing w(a) = w(a'), i.e. vanishing principal 2x2 minors of
the row- and column-permuted Hadamard G; D^(-1/2) G D^(-1/2) is a Hermitian complex Hadamard matrix with unit
diagonal, whose trace 10 would equal (n_+ - n_-) sqrt10. Column phases of either factor cancel in u and w. VALID.

**R4 (three cases).** The commutator pairing between the 2-part and 5-part of Z_10^2 is trivial (its values have
order dividing 2 and 5), so pi is a module over C^a[Z_2^2] (x) C^b[Z_5^2]. (trivial x trivial): diagonal characters;
the weights |c_k|^2 must have uniform marginals under x, y and x + lambda y on at most 10 support points, so the
support is the graph of a bijection f with x + lambda f(x) bijective, a complete mapping of Z_10: impossible.
(Pauli x diagonal): C^10 = C^2 (x) C^5 with the Z_5^2 part diagonal; uniformity over each 5-part forces each of the
five components w_s (|w_s|^2 = 1/5) to satisfy <X> = <Y> = <Z> = 0 (the three 2-parts of H_R, H_C, H_T map to the
three Paulis because lambda is odd): impossible. (diagonal x WH_5): the H_X 2-part condition forces the two Z_2^2
characters to differ on (1,0), (0,1) and (1,lambda) = (1,1), impossible for a character ratio. WH_10: unchanged,
UNKNOWN. VALID.

**R5, R6, R8.** Mann parity: a class meeting R1 x C1 in x cells has exactly 2x cells in W, but needs 5. Dim 2: the
column partner of the row partner of p differs from p and carries p's ray. Closed 3x3 block: a QLS(3) on W [IMPORT
Paczos et al.: QLS(3) has 3 rays]. R6 [IMPORT: proper subsquares of order-10 Latin squares have order <= 5; 1-RQLS(s)
classical for s <= 5, Ball-Simoens via Zhang-Cao]. R8: QLS(2) forces x_11 || x_00, reducing m = 2 to the rectangular
case; m = 5 gives two rays per outer cell. VALID.

**R7.** Lemma 7.1 (counting over the 2^m axis-choices; orthonormal 5-sets inside a union of pairwise non-orthogonal
bases are whole bases; bases are disjoint) and Claim R7 steps 1-5 re-derived. VALID.

**R1, R2.** R2: on a line, a non-fixed cell's partner has swapped type and ray |a> - e^(i phi)|b>; the column partner
of the row partner repeats p's ray. R1: a K-component with |K| >= 2 contains two cells of each of its symbols; an
inclusion-minimal laminar move set receives one product unitary. VALID within the stated settings.

**Addendum 3.** Flat 5th-root vectors are orthogonal iff the exponent difference is a permutation of Z_5 (five
5th roots vanish only as a full set). Remark (new, exact): as functions Z_5 -> Z_5 modulo constants the six
permutation directions are t and (t+c)^3 for c in Z_5 (reduced degree of a permutation polynomial of F_5 is <= 3, no
degree-2 permutation exists, and the x^2/x^3 coefficient ratio 3c separates the cubics). Uniform-direction closure
re-derived. VALID-WITH-IMPORT (Haagerup).

**Addenda 5 and 7.** Re-derived; VALID.

## Consequence for this round

The excluded families are exactly: flat Fourier-permutation with 10th roots (R3), Paley-involving Hadamard products
(R9, R10), three of four Z_10^2 projective orbit cases (R4), rectangular / dim-2 / closed-3x3 splits (R5), product
families of R7/R8, classical-deformation families R1/R2. Everything else listed in the old summary remains OPEN.
