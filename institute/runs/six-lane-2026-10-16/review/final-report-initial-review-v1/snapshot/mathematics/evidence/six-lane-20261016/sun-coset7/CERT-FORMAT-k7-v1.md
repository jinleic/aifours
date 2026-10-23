# CERT-FORMAT-k7-v1: self-contained format of the core7_engine_v1 outputs (for a separately written checker)

- **Freeze record:** host-clock time and sha256 in `evidence/certformat-v1.sha256`.
- **Engine:** `code/core7_engine_v1.py`, sha256 e7b4f039…288d. This file is written so a checker can be built from it and `rules-k7-v1.md` alone, **without reading the engine**.
- **Status:** every run under this format is EXPLORATORY (parent GO of 13:35 PDT). A verified run removes a class only after the parent accepts it.

## 1. Universes

A universe is a list of k vertex roles and, for each unordered role pair, a set of allowed gcd values.

**Profile domains.** A vertex profile is a triple (e, f, g) of capped valuations (min(v_2(n),4), min(v_3(n),2), min(v_5(n),2)) of its index n. Each role has a domain:

| role | domain of (e, f, g) |
|---|---|
| C | e ∈ {1,2,3,4}, f ∈ {1,2}, g ∈ {0,1,2} |
| D2 | e ∈ {1,2,3,4}, f = 0, g ∈ {0,1,2} |
| D2E | e ∈ {2,3,4}, f = 0, g ∈ {0,1,2} |
| D3 | e = 0, f ∈ {1,2}, g ∈ {0,1,2} |
| X | e ∈ {1,2,3,4}, f = 0, g ∈ {1,2} |
| Y | e = 0, f ∈ {1,2}, g ∈ {1,2} |
| P1 | e = 1, f ∈ {0,1,2}, g ∈ {0,1,2} |
| P4, Q4 | e ∈ {2,3,4}, f ∈ {0,1,2}, g ∈ {0,1,2} |

The gcd of two profiles is gp(p, p′) = 2^min(e,e′) · 3^min(f,f′) · 5^min(g,g′).

**Universes.**

| name | roles (vertex order 0..k−1) | allowed gcds |
|---|---|---|
| X1 | D3, D3, C, C, C | D3–D3 {3}; C–D3 {3}; C–C {6} |
| MSP45 | P1, P4, P4, P4 | P1–P4 {2}; P4–P4 {4} |
| CORE5 | Q4 ×5 | Q4–Q4 {4} |
| K52 | D2E, D2E, C ×5 | D2E–D2E {4}; C–D2E {2,4}; C–C {6} |
| KII | X, Y, C ×5 | X–Y {5}; C–X {2,4}; C–Y {3}; C–C {6} |

A profile tuple is **admissible** if each vertex's profile is in its role's domain and every pairwise gp is allowed for the role pair.

**Profile coverage.** The engine lists one representative per orbit under permutations preserving roles: within each maximal run of equal roles, the profiles are non-decreasing in the domain's listing order, i.e. lexicographic in (e, f, g) with e outermost. A checker must enumerate admissible tuples independently and confirm that every one is equivalent to a listed representative. The representatives appear as `prof` in `leaves.jsonl.gz` only when a leaf is reached; the count is `profiles_total` in `run.json`.

## 2. Patterns, edge order, tree

- g_ij = gp(π_i, π_j). α_ij ranges over 1, …, g_ij − 1.
- **Edge order:** (i, j) with i < j, lexicographic, i.e. (0,1), (0,2), …, (0,k−1), (1,2), ….
- **Tree:** at depth t the edge E[t] gets α ∈ {1, …, g − 1} in increasing order.
- Triangle {h < i < j} is **completed** at edge (i, j).
- deg(v) counts the assigned edges at v.

**At each node, after assigning edge (i, j):**
1. **T:** if some triangle completed at (i, j) fails T, the node is closed ("T").
2. **VFC:** otherwise deg(i) and deg(j) are incremented. For v ∈ {i, j} with deg(v) ≥ 3, compute the signature sig(v) (§3). If sig(v) is in `vfc_killed.json.gz`, the node is closed ("VFC").
3. **K-partial:** otherwise, for each triangle completed at (i, j), each apex v and other two a, b: if a and b are linked at v (§3), and some S ⊇ {a, b} of v's assigned neighbours has all pairwise edges assigned, all pairs linked at v, and Σ_{u∈S} α_uv/g_uv ≥ 1, the node is closed ("Kp").

Every closure is sound by deletion: it uses only the subfamily formed by v and the vertices involved.

**Leaves** (all edges assigned) are identified up to the stabiliser of the profile tuple: the permutations mapping each vertex to a vertex of the same role and the same profile. The canonical code is the lexicographically smallest tuple (α_{p(i)p(j)})_{(i,j) in edge order} over all stabiliser permutations p. Each canonical class has exactly one line in `leaves.jsonl.gz`.

## 3. Exact formulas

Write ℓ-valuations per vertex z of a triangle {x, y, z}:
- γ_z = lcm(g_xz, g_yz);
- v_p(ℓ_z) = π_z[p] − v_p(γ_z), for p ∈ {2,3,5} with index 0, 1, 2.

| quantity | formula |
|---|---|
| τ_min(a,b,c) | lcm over the three edges xy (third vertex z) of α_xy / Π_p p^{min(v_p(α_xy), v_p(ℓ_z))} |
| τ_max(a,b,c) | min over apex y of ⌊γ_y · α_xz · min(α_xy/g_xy, α_yz/g_yz)⌋, with γ_y = lcm(g_xy, g_yz) |
| T passes | τ_min ≤ τ_max |
| linked(v; i, j) | τ_min(i,v,j)·g_iv ≥ lcm(g_iv, g_ij)·α_vj·α_iv, or τ_min(i,v,j)·g_jv ≥ lcm(g_jv, g_ij)·α_vi·α_jv |
| K (leaf) | some v and S ⊆ V∖{v}, \|S\| ≥ 2, with all pairs linked at v and Σ_{u∈S} α_uv/g_uv ≥ 1 |
| sig(v) | sorted tuple, over v's assigned neighbours j, of (g_vj, α_vj, b_2, b_3, b_5) with b_p = π_j[p] − v_p(g_vj) |

**VFC kill of a signature.** A signature entry (g, α, b_2, b_3, b_5) has admissible q ∈ {1, …, g − α}. For each q-vector, in itertools.product order of the signature entries:
- **LP key:** the sorted tuple of entries (num, den, v_2(q)+b_2, v_3(q)+b_3, v_5(q)+b_5), where num/den = q/g in lowest terms.
- **String form:** entries `num/den,d2,d3,d5` joined by `;`.
- **Allowed sets:** a subset T of the key's positions is allowed if |T| ≤ 1, or every T′ ⊆ T with |T′| ≥ 2 contains positions x ≠ y with 2^min(d2) · 3^min(d3) · 5^min(d5) ≥ |T′| (minimum taken over x and y). Check all subsets.
- **Required dual:** `lp_duals.json.gz` must contain the key with `y`, a list of exact rationals (strings, in key order), satisfying y ≥ 0, Σ_{x∈T} y_x ≤ 1 for every allowed T, and Σ_x (num_x/den_x)·y_x ≥ 1.

A signature is killed iff every q-vector's key has such a dual. `value` is informational.

**P (leaf), per vertex v**, for pairs {j, k} of the others:
- X_j = α_vj/g_vj;
- u = 1 / Π_p p^{min(π_v[p], max(π_j[p], π_k[p]) + v_p(α_jk))};
- Lb = max(τ_min(v,j,k)/(lcm(g_vj,g_vk)·α_jk), X_j + X_k − 1, 0);
- lo = u⌈Lb/u⌉;
- hi = u⌊min(X_j,X_k)/u⌋, minus u if hi = min(X_j, X_k) and the containment is barred. "U_vU_j ⊆ U_vU_k allowed" means α_vj/g_vj + α_kj/g_kj < 1. When X_j < X_k test (j → k); when X_k < X_j test (k → j); when they are equal, both must be allowed.

**Ppair:** lo > hi. **PB:** Σ_{j∈S}(1 − X_j) − Σ_{pairs ⊆ S}(1 − X_j − X_k + hi_jk) ≥ 1.

**RPLP (leaf), witness [v, certs].** Neighbours N = V∖{v} in increasing order (positions 0..n−1); pairs (a, b), a < b, in lexicographic order.

- **Entries:** for each neighbour the entry (g_vj, α_vj, b_2, b_3, b_5), unsorted, in N order.
- **certs:** one element per q in itertools.product order over N:
  - **["R", key-string]:** the key computed from (entries, q) must equal key-string, and its dual must verify as above.
  - **["P", vec]:** vec has 2n + 2·C(n,2) exact rationals: a (n), b (n), u (pairs), l (pairs); u, l ≥ 0.
- **Local valuations for that q:** dv_x = (v_2(q_x)+b_2, v_3(q_x)+b_3, v_5(q_x)+b_5). Allowed masks as above.
- **Forced pairs:** (a, b) is forced iff τ_min(v, N_a, N_b)·g_{vN_a} ≥ lcm(g_{vN_a}, g_{vN_b})·α_{N_aN_b}·α_{vN_a}. This is ordered: test (a, b) and (b, a) separately.
- **Columns:** all (A, S) with A ⊆ N non-empty, no forced (a, b) with b ∈ A and a ∉ A, and S ⊆ A with S = ∅ or S allowed.
- **Check (★) for every column:** Σ_{x∈S} a_x + Σ_{x∈A} b_x − Σ_{pairs ⊆ A} u + Σ_{pairs ⊆ A} l ≤ 1.
- **Objective:** Σ_x a_x·q_x/g_x + Σ_x b_x·(1 − α_x/g_x) − Σ_p u_p·yhi_p + Σ_p l_p·ylo_p ≥ 1, where yhi/ylo = 1 − X_j − X_k + hi/lo with lo, hi as in P.

## 4. Files per run directory

| file | content |
|---|---|
| `run.json` | status (COMPLETE or UNKNOWN), stop_reason, profiles_total, stats (nodes, leaves, closures per rule, leaf rule counts), survivor_count, output hashes |
| `vfc_killed.json.gz` | JSON list of killed signatures (each a list of [g, α, b2, b3, b5]) |
| `lp_duals.json.gz` | JSON object: key-string → {"value", "y"} |
| `leaves.jsonl.gz` | one JSON object per leaf class: prof, canon (canonical code string), rep (the engine's labelled leaf in edge order), rule ∈ {K, Ppair, PB, RPLP, SURVIVE}, witness |
| `survivors.json` | the SURVIVE lines |

## 5. What a checker must establish (fail closed)

1. **Profiles.** Its own enumeration of admissible profile tuples, up to role-preserving symmetry, matches profiles_total, and every orbit is represented.
2. **Tree.** For each representative, its own walk under §2 with the stored `vfc_killed` set (each used signature re-verified via §3).
3. **Leaves.** Every reached leaf's canonical class has exactly one line whose rep has that canonical code, and whose witness verifies.
4. **Survivors.** The SURVIVE lines are exactly the survivors.
5. **Parsing.** Exact rationals only (no floats); duplicate JSON keys rejected.
6. **UNKNOWN.** A run with status UNKNOWN proves nothing about the unvisited part.

A checker that prunes with T only must, at each leaf reached beyond the engine's pruning, find a killed partial signature or a K witness on that leaf. This is equivalent, by deletion.
