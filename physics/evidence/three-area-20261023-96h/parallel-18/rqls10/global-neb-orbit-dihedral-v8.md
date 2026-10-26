# RQLS10 - all nice-error-basis orbit families: the dihedral family, its exact system, and a sharpened Galois constraint

Owner PhysicsRQLS10-2 (physics-5). Actual `/bin/date` observed immediately before this file: `Sun Oct 25 20:48:52 PDT 2026`.

**WRITTEN CANDIDATE. No independent reconstruction, parent disposition, formal, kernel, human, cross-vendor, executable-certificate or novelty acceptance.** All mathematics is hand-written exact reasoning. No scientific interpreter, eval cell, program, CAS, enumeration, solver, replay, external CLI or nested agent was used. V9/v10/v11 and the HOLD are binding. The original target, cutoff `2026-10-27T11:05:38-07:00` and deadline `2026-10-27T12:35:38-07:00` are unchanged. This is ONE new successor. It does not edit the pinned v7 (`global-weyl-covariant-two-class-v7.md`, SHA256 `8636f5239218dc51126b57bcc376f5027876ec20d2ea0d78e34e3d49ec76997d`), and it uses v7's notation and results as stated there.

## 0. Result

Group-covariant 1-RQLS(10) of the following form:

- the 100 cells are the elements of the index group of a nice error basis (NEB) `{pi(g)}` on `C^10`;
- cell `g` carries `pi(g)psi`;
- rows, columns and transversals are invariant under left translation.

There are exactly two NEB index groups in dimension 10. This is conditional on one direction of the DeMeyer-Janusz Sylow criterion (named import J1). They are the abelian `Z10^2` (Weyl, v7) and a **non-abelian** group `G_d = Dih(Z5^2) x Z2`, realized by the explicit NEB

    I (x) D5(l),    sz (x) D5(l),    sx (x) D5(l) Pi5,    sy (x) D5(l) Pi5      (l in Z5^2),     (0.1)

where `Pi5 v(K) = v(-K)` is C^5 parity. The resulting **dihedral family** is new and is NOT a mutually-unbiased-basis extension problem, so import I1 does not apply to it. It reduces to an exact system of 18 real equations in 9 real phases (Section 5). Unlike the Weyl family:

- its qubit marginal is not forced to be maximally mixed;
- maximality is not automatic, and two explicit eigenvector types must be excluded.

On parity-even vectors it coincides exactly with the Weyl family. Its two Clifford classes are Galois conjugate.

**Consolidated statement (given I1 and J1).** A coset-covariant NEB-orbit maximal 1-RQLS(10) exists iff one of three explicit systems has an admissible real solution: Weyl-A (v7, (9.1)), dihedral-A or dihedral-B (Section 5 here). In addition, Weyl-A solutions need coordinates with no real place over `sqrt5 -> -sqrt5` (Theorem 7).

## 1. NEB index groups in dimension 10

An NEB in dimension `d` is a projective representation of an index group `G`, `|G| = d^2`, with irreducible degree `d` (a "group of central type").

**Import J1** (DeMeyer-Janusz, Math. Z. 108 (1969); the direction quoted in Pacific J. Math. 151(1) "On central type factor groups"): if `(G, alpha)` is of central type, then so is every Sylow subgroup with the restricted cocycle. NOT re-proved here.

**Proposition 1.** For `|G| = 100`, the index group is `Z10^2` or `G_d = (Z5^2 x| <s>) x <c>`, where `s` acts by `-I` and `c` is central.

Proof:

1. `n_5` divides 4 and is `1 mod 5`, so the Sylow-5 subgroup `P5` is normal.
2. By J1, `P5` and the Sylow-2 subgroup `P2` are of central type. Cyclic groups have trivial Schur multiplier, so `P5 = Z5^2` and `P2 = Z2^2`.
3. Conjugation by `P2` must fix the restricted nondegenerate class in `H^2(Z5^2, C^*) = Z5`, on which `A in GL(2,5)` acts by `det A`. Hence `P2` maps into `SL(2,5)`.
4. `SL(2,5)` has the unique involution `-I`, so the image is `{I}` or `{+-I}`.
5. The trivial action gives `Z2^2 x Z5^2 = Z10^2`. The other action is `G_d`, up to automorphisms of `Z2^2`.

QED.

The NEB (0.1) realizes `G_d`: `l -> I(x)D5(l)`, `s -> sx(x)Pi5`, `c -> sz(x)I`.

**Lemma 1.1 ((0.1) is an NEB).**

- Closure up to phase follows from `Pi5 D5(l) Pi5 = D5(-l)` and the Pauli products.
- Every non-identity element is traceless: `tr D5(l) = 0` for `l != 0`, and every term with `sx`, `sy` or `sz` has a traceless qubit factor.
- So the 100 operators are orthogonal, and they form a unitary basis of `M_10`.

For symmetric Weyl operators (`D5(-l) = D5(l)^dagger`), the operators `D5(l)Pi5` are Hermitian involutions. These are the phase-point operators `A_{l/2}`.

## 2. Orbit arrays and admissible subgroup triples

Left-translation-invariant partitions are left cosets of subgroups. The proof of v7 Lemma 1 carries over verbatim to left actions. Orthonormality of `{pi(gh)psi : h in H}` holds iff `A(h) := <psi, pi(h) psi> = 0` for all `h in H\{1}`.

Order-10 subgroups of `G_d`: a Sylow-5 line `L`, extended by an involution normalizing it. The involutions are `c`, `ts` and `tsc` (`t in Z5^2`). This gives:

- `L x <c>` (6 subgroups, abelian);
- `L x| <ts>` (30, dihedral);
- `L x| <tsc>` (30, dihedral).

**Lemma 2.1.** Pairwise trivial intersection of three such subgroups forces exactly one of each type, with distinct lines `L1, L2, L3`. Proof:

- Two `·s`-type subgroups `L x| <ts>` and `L' x| <t's>` share the involution `us` whenever the affine lines `t + L` and `t' + L'` meet. Non-parallel affine lines in `F5^2` always meet, and equal lines share `L`.
- The same holds for the `·sc` type.
- Two `·c`-type subgroups share `c`.
- Mixed pairs meet trivially iff their lines differ.

**Lemma 2.2 (grids).** Fix `H1 = L1 x <c>`, `H2 = L2 x| <t2 s>`, `H3 = L3 x| <t3 sc>`. Then `|H_i H_j| = 100` and `|H_i ∩ H_j| = 1` for `i != j`, so every left coset of `H_i` meets every left coset of `H_j` exactly once (`|H_i ∩ z H_j| = 1` for all `z`). Rows `H1`, columns `H2` and classes `H3` therefore form a 1-RQLS grid.

**Normalization.** Conjugating by `I(x)D5(u)` sends `ts -> (t + 2u)s` and fixes `H1`. Since `Z5^2 = L2 + L3`, one `u` makes `t2 = t3 = 0`.

The Weil operators of `SL(2,5)` commute with `Pi5 = U(-I)` and normalize (0.1). The qubit `S` and `X` gates exchange the `s` and `sc` types. Configurations `(L1; {L2, L3})` therefore form two `PSL(2,5)` orbits of size 30: face and non-face, as in v7 Theorem C.

**Lemma 2.3 (regular restriction).** `pi|_{H_i}` is a linear representation with character `10 delta_1`, which is the regular representation. So orbit ONBs exist for each single subgroup, and no a-priori obstruction arises.

## 3. Exact conditions

Let `psi = |0>(x)v0 + |1>(x)v1`, with `L1 = E` (the `Z5` line), `L2 = F` (the `X5` line) and `L3 = G` (the line of `X5 Z5^{2 alpha}`), whose eigenbasis is the chirp `omega5^{alpha K^2 + M K}`.

- (R) `H1`: `v0` and `v1` are both E-flat, with `|v_j(K)|^2 = 1/10`.
- (C1) `A(mu) = 0` for `mu` in `F\{0}`: `rho_B = |v0><v0| + |v1><v1|` has flat F-diagonal.
- (C2) `A(mu s) = 0` for `mu` in `F`: `<psi, (sx(x)D5(mu)Pi5) psi> = 2 Re <v0, D5(mu) Pi5 v1> = 0`, by Hermiticity.
- (T1) `A(nu) = 0` for `nu` in `G\{0}`: `rho_B` has flat G-diagonal.
- (T2) `A(nu sc) = 0` for `nu` in `G`: `<psi, (sy(x)D5(nu)Pi5) psi> = 2 Im <v0, D5(nu) Pi5 v1> = 0`.

At `mu = nu = 0` this gives `<v0, Pi5 v1> = 0`, but NOT `<v0, v1> = 0`. The qubit marginal is not forced to be `I/2` (contrast v7 Step 1).

## 4. Theorems on the dihedral family

**Theorem 4.1 (even slice = Weyl even slice).** If `Pi5 v0 = v0` and `Pi5 v1 = v1`, conditions (R, C1, C2, T1, T2) coincide with the Weyl conditions (v7, (7.1) in E/F/G-coefficient form) for the same `(v0, v1)`. The reason: `D5(mu) Pi5 v1 = D5(mu) v1`, and the cross-coefficients `c_L = conj(<f_L|v0>) <f_L|v1>` are even in `L`, so `c_L + conj(c_{-L}) = 2 Re c_L`. E-flatness forbids odd components (they vanish at `K = 0`). Therefore every `I(x)Pi5`-symmetric dihedral solution is a Weyl solution, and genuinely new dihedral solutions are non-parity-symmetric.

**Theorem 4.2 (maximality analysis).** Some `pi(g)psi` with `g != 1` can be parallel to `psi` only if `|A(g^k)| = 1` for all `k`, so `<g>` must avoid `H1 ∪ H2 ∪ H3`.

- `g = l c` (`l != 0`) is excluded, since `(lc)^5 = c` lies in `H1`.
- `g` on `L1`, `L2` or `L3` is excluded, since it lies in some `H_i`.
- `g = l` on an H-line is excluded as follows. Then `psi = (alpha|0> + beta|1>)(x)h` with `h` a stabilizer state, and (R) forces `|alpha| = |beta| = 1/sqrt2`. The Wigner function of `h` is `1/5` on one affine line `l_h` (parallel to the H-line) and `0` elsewhere, so `<h, D5(mu)Pi5 h> = 5 W_h(mu/2)` is `1` at exactly one `mu` in `F` and one `nu` in `G`. (C2) and (T2) then give `Re(conj(alpha) beta) = Im(conj(alpha) beta) = 0`. Contradiction.
- **Not excluded:** `g = us` with `u` not in `F`, i.e. `v1 = +-D5(u)Pi5 v0`; and `g = usc` with `u` not in `G`, i.e. `v1 = +-i D5(u)Pi5 v0`. Any candidate solution must be checked against these two non-maximal types.

**Theorem 4.3 (Galois conjugacy).** `sigma_7` (`zeta20 -> zeta20^7`) maps the NEB (0.1) to itself up to phases: it sends `sy -> -sy`, `Pi5 -> Pi5` and the chirp coefficient `alpha -> 2 alpha`, which flips the Legendre symbol. The complexified varieties of dihedral-A and dihedral-B are therefore Galois conjugate, exactly as in v7 Theorem D.

## 5. Explicit dihedral systems (exact remaining question)

Write `v0 = a/sqrt10` and `v1 = b/sqrt10` with `|a_K| = |b_K| = 1`. Define the chirped sequences `a~_K = omega5^{-alpha K^2} a_K` and `b~_K = omega5^{-alpha K^2} b_K`. Define autocorrelation `R_x(m) = sum_K conj(x_K) x_{K+m}` and convolution `(x * y)(p) = sum_K conj(x_K) y_{p-K}`. Then (R)+(C1)+(C2)+(T1)+(T2) is equivalent to:

    (C1) R_a(m) + R_b(m) = 0                      (m = 1..4)
    (C2) Re (a * b)(p) = 0                         (all p in Z5)
    (T1) R_{a~}(m) + R_{b~}(m) = 0                 (m = 1..4)
    (T2) Im (a~ * b~)(q) = 0                        (all q in Z5)          (5.1)

Here `alpha = 2` (or 3) gives **dihedral-A** and `alpha = 4` (or 1) gives **dihedral-B**.

Derivations:

- `(X^p Pi5 v)(K) = v(p - K)` gives (C2).
- `D5(q, 2 alpha q) Pi5 v1` at `K` equals `omega5^{2 alpha q K - alpha q^2} v1(q - K)`. Since `2 alpha q K - alpha q^2 = alpha K^2 - alpha (q-K)^2`, this gives (T2).
- `sum_K omega5^{-2 alpha m K} conj(a_K) a_{K+m} = omega5^{alpha m^2} R_{a~}(m)` gives (T1).

Counting: 4 + 5 + 4 + 5 = 18 real equations in 9 real unknowns (phases mod global phase).

For comparison, the Weyl system (v7 (9.1)) has the same (C1)/(T1) but CORRELATION cross terms `C_ab(m) + C_ba(m) = 0` where (5.1) has CONVOLUTION terms. Parity flips one argument.

## 6. What changed relative to v7

v7 classified the abelian (Weyl) orbit families. This file shows that the abelian NEB is not the only NEB in dimension 10, through J1 and Proposition 1, and adds the unique non-abelian one. Under I1 + J1, the set of open coset-covariant NEB-orbit cases is exactly `{Weyl-A, dihedral-A, dihedral-B}`.

## 7. Theorem 7 (sharpened Galois constraint for Weyl-A; needs I1 real emptiness only)

Let `G_A(u,v)` and `G_B(u,v)` be the real-variable Weyl systems (`psi = u + iv`). Their coefficients lie in `k = Q(zeta20) ∩ R = Q(zeta20)^+`, because each equation is real-valued with coefficients in `Q(zeta20)`.

From v7 Theorem D, `sigma_7(G_A)(u,v) = sigma_7(F_A)(u - iv, u + iv) = F_B(u - iv, u + iv) = G_B(u, -v)`, using `sigma_7(i) = -i`.

Let `(u,v)` be a real algebraic class-A solution, and let `F = k(u,v)` (a subfield of `R`). If some field embedding `tau: F -> R` restricts to `sigma_7` on `k`, then `(tau u, -tau v)` is a REAL class-B solution, contradicting I1. Real algebraic points are dense in each real component, so a solution exists iff an algebraic one does.

**Hence every class-A solution field has no real place above the place of `k` where `sqrt5 -> -sqrt5`.** `sigma_7` restricts to `zeta5 -> zeta5^2` on `Q(sqrt5)`, which negates `sqrt5`. For example, coordinates must involve numbers such as `sqrt(phi)`, with `phi = (1 + sqrt5)/2`, whose conjugate radicand is negative. This strictly contains v7 Corollary D2.

## 8. Non-claims and assurance

No 100-ray witness, no solution or refutation of (5.1) or of v7 (9.1), and no unrestricted no-go. I1 (computer-aided) and J1 (classical, one direction) are named imports, not reconstructed. The Wigner/stabilizer facts used in Theorem 4.2 are standard odd-prime discrete phase-space facts (Gross 2006): stabilizer states have Wigner functions uniform on a line. They are cited as standard and not re-derived here. Novelty and priority are UNCLEAR: dihedral-type NEBs in dimension `2p` may already appear in the nice-error-basis literature (Klappenecker-Roetteler), and that has not been checked. Same-harness written candidate only.
