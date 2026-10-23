# K62-DT-A-v1: apex forcing in O-triangles and the cherry-isolation lemma CI (Part A of the DG case analysis) [CANDIDATE]

- **Written:** `/bin/date` read immediately before this exclusive write: 2026-10-19T06:28:22-0700.
- **Author:** Sun63Successor; single author, unreviewed, written only (HOLD in force; nothing run).
- **Status labels.** Sections 1-2 are unconditional (given the imports below). Section 3 is **CONDITIONAL ON DG**
  (`K62-DG-v1.md` sha256 a4bfc41e832ebc4e77770cab7a8092a3341827cec93a01bfb437c978c1e84f52 + erratum e435430c…, under dual
  review). Section 2 uses the global bound (C1) of the candidate `K62-CAP-v1.md` (sha256
  19dccc3d8bce5908a14ff96462a05beeb38ba966374c8c4740e6a66a312b16d5), re-stated below with its one-line source.
- **Imports (accepted):** old README section 0 L0.1 with Lagrange; E1; LFC (a)-(d), INV (a)-(b) with E6 (8621e744…);
  rules-k7-v1 L1 (T rule, (T3)) and VFC (V1)-(V4) with the count (73a25ba6…); K62-E3 with errata (576969dd…):
  Lemma 1, Lemma 2, C2 sub-claim (a) (O-O entries of alpha and alpha* in {1, 2, 4}), Corollary C2. Sun instances:
  Sun(2), Sun(3) via (V3). Setting and notation: `K62-CAP-v1.md` section 0 (residue e_d >= 4, e* = 2, any markers).

## 0. Conventions
For a family x in {alpha, alpha*} let x' be the other one. "The Phi^x-configuration" is the configuration
(g_jU_j) if x = alpha and its inverted configuration if x = alpha* (INV (a)); at a vertex v (after the left translation
making v's representative 1) its VFC data are: X^v_j := Phi_vPhi_j of measure x_vj / g_vj, D'_j of measure
x'_vj / g_vj contained in Y^v_j := G minus X^v_j (V1, INV (b)), and local indices lambda'_j = n_j x'_vj / g_vj (V2, V3).
An edge vj is **tight** if x_vj + x'_vj = g_vj; then D'_j = Y^v_j (finite sets of equal measure).

## 1. Apex forcing in an O-triangle (unconditional)
Let {v, a, b} be in O with x-values x_va, x_vb, x_ab in {1, 2, 4} and tau = tau_x(vab). By L1 (T3) (gamma = 6),
mu(Phi_v(Phi_a cap Phi_b)) = tau / (6 x_ab), and Phi_v(Phi_a cap Phi_b) lies in X^v_a cap X^v_b. Hence, if
**tau = x_ab * x_va**, then X^v_a = Phi_v(Phi_a cap Phi_b) is contained in X^v_b, with equality if moreover x_va = x_vb.
With tau a multiple of lcm(x's) and tau <= (product of the two smallest values) (K62-DG Lemma DG-3, whose proof is L1):
| sorted values | admissible tau | forced at apexes (equality = "X_a = X_b at the apex opposite ab") |
|---|---|---|
| (1,1,1) | 1 | equality at all three apexes |
| (1,2,2) | 2 | equality at the apex opposite the 1-edge; containments X(1) in X(2) at the other two |
| (1,4,4) | 4 | **equality at the apex opposite the 1-edge**; containments at the other two |
| (2,2,2) | 2 or 4 | tau = 4: equality at all three apexes; tau = 2: nothing |
| (2,2,4) | 4 | containment X(2) in X(4) at both ends of the 4-edge |
| (2,4,4) | 4 or 8 | tau = 8: **equality at the apex opposite the 2-edge**, containments at the other two; tau = 4: nothing |
| (4,4,4) | 4, 8, 12, 16 | tau = 16: **equality at all three apexes**; otherwise nothing |
Forbidden by the T rule: (1,1,2), (1,1,4), (1,2,4).

## 2. Lemma CI (cherry isolation) [NEW]
**Hypotheses.** v in O unmarked; x a family with **x_(d i*) = 1**; a != b in O minus {v} with x_va = x_vb = 4,
**X^v_a = X^v_b**, and **both edges va, vb tight** (x'_va = x'_vb = 2). **Conclusion: contradiction.**
*Global bound used (K62-CAP-v1 (C1), candidate):* with x_(d i*) = 1, gcd(n_v, T_x(V minus {v})) divides 6 (chain d, i*, t, p,
rest); the set Phi_v W (W the intersection of all Phi_j, j != v) has measure >= 1/6, lies in every X^v_j, hence (V1)
misses every D'_j; so **mu(union of the D'_j) <= 5/6**.
*Proof.* 1. Y^v_a = Y^v_b and tightness give D'_a = D'_b =: D, of measure 2/6.
2. For j in {d} cup (O minus {v, a, b}), D cap D'_j is empty: a right coset R in it has S_R containing {a, b, j}, and the
three local indices have pairwise gcds at most 2. Indeed lambda'_a, lambda'_b have 2-part exactly 2 (x' = 2); the
entries x'_va, x'_vb, x'_vj lie in {1, 2, 4} (x'_vd = 1), so they contribute no 3 or 5; the w-parts are pairwise coprime;
and no prime 3 or 5 divides two of the three labels, since at most one vertex carries each marker. Three pieces with
pairwise gcds < 3 violate (V3) (Sun(3)).
3. mu(D'_d) = x'_vd / 2 = 1/2, so mu(D cup D'_d) = 5/6, which is the maximum allowed for the union of all D'_j. Hence every
D'_j is contained in D cup D'_d, and by step 2, **D'_c is contained in D'_d for both c in O minus {v, a, b}**.
4. For such c, every right coset in D'_c (non-empty: measure x'_vc / 6) carries pieces of c and d, so gcd(lambda'_c,
lambda'_d) >= 2 (Sun(2)); lambda'_d has odd part 5^(h_d) w_d and lambda'_c has no factor 5 in common with it (one 5-marker),
so x'_vc is even; and x'_vc / 6 = mu(D'_c) <= mu(D'_d) = 1/2 forces **x'_vc = 2**.
5. The two vertices c != c' of O minus {v, a, b} then have D'_c, D'_c' inside D'_d; a right coset in D'_c cap D'_c' would carry
{c, c', d} with pairwise gcds 2 (2-parts 2, 2, >= 8; odd parts as in step 2), violating (V3). So D'_c and D'_c' are
disjoint subsets of D'_d: 2/6 + 2/6 <= 1/2, false. QED
*Remark.* No hypothesis on markers of a, b, c, c' is needed (step 2 uses only that each marker lies on one vertex and
that O-O and d-entries have no factor 3 or 5).

**Corollary CI'.** If v in O is unmarked, x_(d i*) = 1, and {v, a, b} in O has x_va = x_vb = 4 and tau_x(vab) = 4 x_ab
(automatic for x_ab = 1; tau = 8 for x_ab = 2; tau = 16 for x_ab = 4), then at least one of va, vb is **non-tight**,
i.e. has (x, x') = (4, 1).

## 3. Consequences for Theorem DG (CONDITIONAL ON DG)
In the case (alpha_(d i*), alpha*_(d i*)) = (1, 1) (in particular whenever no 3-marker lies in O), Theorem DG applies to
both families and CI' applies to both at every unmarked O-vertex. For a family x write n_k(x) for the number of O-pairs
with x = k, H_x for the graph of O-pairs with x = 4, and u(x) for the number of those with (x, x') = (4, 1).
- (3a) **Deep triples.** In Theorem DG (b) the triples R with min(e_d, depth) >= 4 have x-values (2,4,4) with tau = 8
  (type T1) or (4,4,4) with tau in {8, 16} (types T2: tau = 8, depth 4, no forcing; T3: tau = 16, depth 5). By CI', a
  T1 triple's apex opposite the 2-edge, if unmarked, has a non-tight incident edge in the triple; a T3 triangle with
  all three apexes unmarked has at least two non-tight edges. Every (1,4,4) triple likewise has a non-tight edge at its
  apex opposite the 1-edge (if unmarked), whether or not it is deep.
- (3b) **Budget.** Each non-tight x-4-edge is an x'-1-edge, so n_1(x') >= u(x), and accepted K62-E3 C2 for x' gives
  n_4(x') >= 2 n_1(x') + 2 >= 2 u(x) + 2. H_alpha and H_alpha* are edge-disjoint (INV), so
  n_4(alpha) + n_4(alpha*) <= 10.
- (3c) **Weights.** Writing a, b, c, e for the numbers of triples of depth 4, depth 5, depth 2 and depth 1, DG (a)
  (all 4-subsets of depth <= 4) reads 2a + 3b >= 3 + 4c + 12e (sum over triples of 2^(-depth) at most 37/32).
The case analysis that combines (3a)-(3c) with the O-row bounds of K62-CAP (C) and with 4-subsets of depth >= 5 is
Part B (to follow). Nothing in this file excludes a sub-case of the residue by itself. Full K6.2* (e_d >= 4) and full
Sun(7) remain OPEN.
