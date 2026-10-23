# rqls10-maximal: frozen representation and initial obstacles (v1)

Recorded 2026-10-18 (lane created 14:02:07 PDT; this note written ~14:15 PDT, exact write time in README).
Lane: physics/evidence/six-lane-20261016/rqls10-maximal. Contract: screening/phys-2-rqls10-contract.json
(sha256 0adc1f92552936f8dbbaa5dcdc82a92c9a8aac32bd40481d835ab0c180750f16); priority pre-check sha256
4c62b2435ae08d8ce26b8554afceedf47b60891d41f561f69a6a18df4354aec5.

Status: **UNKNOWN**. No candidate, no nonexistence proof. Everything below marked R1-R6 is lane-internal
derivation, not reviewed. Each R-item is a statement about a *restricted ansatz* only. None of them is evidence
for unrestricted nonexistence.

## 0. Source read (primary)

Zhang-Cao, arXiv:2608.29201v2 (7 Sep 2026). Read from the arXiv HTML and the e-print TeX (RQLS.tex), which was
fetched into memory and not stored here.
- Def. 1.1: t-RQLS(v).
- Thm. 1.3: maximal-cardinality 1-RQLS(v) exists for v >= 7 except
  {10,14,18,22,26,30,34,38,42,46,54,58,62,66,74,82,94}. Order 10 is explicitly open (Section 5).
- Lemma 2.2: A is a t-RQLS(v) iff there are classical QLS B_0..B_{t-1} such that A,B_0,..,B_{t-1} are a
  (t+1)-MOQLS.
- Construction 3.3: vectors (1/sqrt v) sum_t chi_i(mu(t)) chi_j(t) |t> over G = Z_2 x Z_m, where mu is a
  complete mapping.
- Lemma 3.6: v = 0 mod 4.
- Construction 4.4: singular direct product, v = mn + h.
- Lemma 4.8: v = 90.
- Example 2.4: an explicit 1-RQLS(8) with T_k = {(i,j): i XOR j = k}.

Why order 10 is left open:
- Z_2 x Z_5 = Z_10 has no complete mapping (Hall-Paige).
- 10 = 7n + h has no admissible (n,h).
- No factorisation 10 = mn uses a maximal 1-RQLS of each factor.

## 1. Frozen representation (used by every later probe/check)

- Cells (i,j), i,j in {0..9}.
- A configuration is a pair (B, q).
  - B is a Latin square of order 10. B(i,j) = s means cell (i,j) lies in transversal T_s.
  - q is a vector of 100 unit vectors q_ij in C^10.
- Lines are the 10 rows, 10 columns and 10 classes T_s = {(i,j): B(i,j) = s}.
- **Target predicate MAX10(B,q)**, all three required:
  1. Every line's 10 vectors form an orthonormal basis.
  2. B is a Latin square, so T_0..T_9 partition the 100 cells with one cell per row and column.
  3. For all distinct cells p != p', q_p and q_p' are not parallel: no |<q_p,q_p'>| = 1. Equivalently, some 2x2
     minor of [q_p q_p'] is nonzero.

This is exactly Def. 1.1 with t = 1, via Lemma 2.2. B is arbitrary: it need not have a classical orthogonal
mate.

Frame identity: for every line, sum_{p in line} |q_p><q_p| = I. Two consequences:
- Any 0/1 cell set U whose indicator is a real combination of line indicators has a determined projector sum.
- Example: if B has the Z_2 block structure of Cay(Z_10), each parity block U has sum_{p in U} |q_p><q_p| =
  (5/2) I. A classical solution would need this coefficient to be an integer. A quantum one need not, so this is
  no contradiction.

Exact certificate format (planned):
- Every entry is (1/sqrt(n_p)) x with x in Q(zeta_N) and integer n_p. N must contain every needed root, e.g.
  sqrt2 in Q(zeta_8).
- Orthogonality, norms, the Latin property of B and nonparallelism (a nonzero 2x2 minor) are checked exactly in
  Q(zeta_N) mod Phi_N, standard library only.

## 2. Restricted-ansatz results so far (derivations; not reviewed; not unrestricted)

### R1. Laminar coordinate rotations from a classical point cannot reach maximal cardinality

Start from a classical pair (A0 orthogonal to B). Apply unitaries on coordinate subspaces span{|k>: k in K}
over unions of K-subnet components, with a laminar (nested) family of moves. Then any minimal nontrivial move
set C (|K| >= 2) contains two cells with the same A0 symbol, and those two cells get identical rays.

Reason: a K-component holding one cell per symbol lies in one row and one column, which forces |K| = 1.

### R2. Superposing two classical mates gives repeated rays

Ansatz: q_p proportional to |A1(p)> + e^{i phi_p}|A2(p)>, with A1 and A2 both mates of B.
- Orthogonality forces A2 o A1^{-1} to be an involution on every line, with a phase condition.
- Every partner component then has all cells of one type (a,b) on each side. So that ray repeats unless the
  component is a single pair, which is impossible.

### R3. Flat Fourier-permutation ansatz is impossible for every Latin square B

Ansatz: q_ij(t) = omega^{i mu(t) + j t}/sqrt10 with omega = e^{2 pi i/10}, mu any permutation of Z_10, and
maximal cardinality required.

The impossibility holds for any B, not only the cyclic one, because no single transversal class exists. Proof
outline:
- **Zero test.** Phi(a,b) = sum_t omega^{a mu(t)+bt} vanishes iff either:
  - every Z_5-fibre of y(t) = a5 mu5(t)+b5 t5 is balanced in u(t) = a2 mu2(t)+b2 t2; or
  - u is constant and y is 2-to-1.

  Here CRT coordinates are used, and the test is de Bruijn/Lam-Leung for n = 2*5.
- **Forcing.** Let a class be {(i, sigma(i))}.
  - Look at the pairs (i, i+5); maximal cardinality excludes u constant. This forces sigma(i+5) = sigma(i)+5
    and #{t: mu(t) = t mod 2} = 5.
  - The dual (frame) condition then forces sigma = (i2+r, h(i5)).
  - For each of the two parity classes P_r of mu, the sets E_r = {(t5, mu5(t)) : t in P_r} and the graph of h
    must form a spectral pair in Z_5^2.
- **Rédei.** In AG(2,5) a 5-set that is not a line determines >= 4 directions. Hence one set in each spectral
  pair is a line.
- **Contradiction.**
  - If the graph of h is a line, the classical sum argument applies: no complete mapping of Z_10.
  - If both E_r are lines, mu2 takes each value an even number of times, but it must take each value 5 times.

### R4. Group-orbit (translation) ansatz with G = Z_10^2 acting regularly on cells

Ansatz: q_g = pi(g) q0 with pi a projective representation, so B is isotopic to Cay(Z_10). Split
pi = pi_2 (x) pi_5 by CRT.
- (diagonal (x) diagonal): reduces to a complete mapping, impossible.
- (Pauli (x) diagonal): needs a qubit Bloch vector orthogonal to x, y and z. Impossible.
- (diagonal (x) Weyl-Heisenberg_5): parity contradiction alpha_0+beta_0 = alpha_1+beta_1. Impossible.
- (Weyl-Heisenberg_10) is the only open sub-case. It reduces to an orthonormal pair r0, r1 in C^5 with:
  - r0 and r1 flat in the computational basis;
  - r0 ± r1 flat in the Fourier basis;
  - r0 ± i r1 flat in the eigenbasis of X Z^k.

  This is 24 real equations on 16 real unknowns. The sub-family where r0 and r1 come from one Weyl-Heisenberg
  MUB is impossible by the Gauss-phase slope. The rest is UNKNOWN.

### R5. Splitting into two orthogonal halves is blocked for 5+5 rectangle blocks

Set-up: C^10 = W1 (+) W2 with every line meeting each half in dim W_k cells.
- 5+5 with two 5x5 QLS blocks per half (the shape of Example 2.4 for order 8): impossible by Mann parity
  (2x = 5).
- A dim-2 half always repeats rays.
- A 3+7 split cannot contain a 3x3 corner block (Parker QDM shape). That block would be a QLS(3), which has
  only 3 rays.

### R6. Replacing a common orthogonal subsquare never helps

In order 10 a common orthogonal subsquare has order s <= 5. Every 1-RQLS(s) with s <= 5 is classical
(Ball-Simoens, as cited by the source), so the subsquare stays classical.

## 3. Obstacles

- All structured routes tried hit the single factor 2 in 10: a Z_2 parity in the form of Hall-Paige, Mann or
  Rédei combined with parity.
- A witness must break every Z_2-labelled structure while keeping 30 ONB constraints.
- Naive real counting for a fixed B is heavily overdetermined: 1800 unknowns against 2700 equations. Near
  classical points, deformations are only 2-symbol trade rotations (tangent-space computation). So
  maximal-cardinality points, if they exist, lie far from classical points, like the character constructions.
- An unrestricted negative would need control of arbitrary B and arbitrary complex vectors. This is beyond
  current tools; even v = 4, 5 needed Ball-Simoens case analysis.

## 4. Planned routes (in order)

1. Exact definition-level checker (standard library, Q(zeta_N)). Positive control: source Example 2.4 (v = 8).
   Plus mutation controls.
2. Finish the WH_10 sub-case of R4. Exact analysis, or a numeric look if the parent grants a float-probe GO.
3. Half-splits without blocks: dim-3 halves as resolvable (30_3) orthogonality configurations in CP^2, with
   group-orbit ansätze.
4. Non-group B (twisted Z_2-extensions of Cay(Z_5), Parker-type B) with structured vector families.
