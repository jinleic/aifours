# CERT-FORMAT-k6-v2: self-contained certificate format for the Core5(6) case analysis (supersedes v1 text; the certificates are unchanged)

This file describes the output of `code/core56_engine_v3.py` (sha256 01f0de4c…d0cd), run under rules-k6-v1, v2 and v3. It is written so that an independent checker can be built from this file plus the rules texts, without reading any engine code.

The host-clock freeze record is in `evidence/certformat-v2.sha256`. The certificates are produced in `evidence/engine-v3-core56/` and are unchanged. Compared with v1 (45f5d73c…68e2), only two passages change, both following the Codex v2/v3 delta review: the PB grid rounding is now explicit, and the N26 test for E3 is corrected.

## 0. Mathematical setting (summary of rules-k6-v1 §0)

**The configuration.**
- G is a finite group. There are six subgroups U_0, …, U_5 with [G:U_i] = 5r_i, and the r_i are pairwise coprime.
- The cosets g_iU_i are pairwise disjoint.
- For i ≠ j, put α_ij = [G:U_i∩U_j]/(5r_ir_j). Each α_ij lies in {1, 2, 3, 4}.
- A pattern is the symmetric matrix α together with the special statuses below.

**Special statuses.**
- **E2:** the vertex with r even, if any, together with a class: c2 = 1 if v₂(r) = 1, and c2 = 2 if v₂(r) ≥ 2.
- **E3:** the vertex with 3 | r, if any.
- **E5:** the vertex with 5 | r, if any. It is used only by FH5, which must refute all seven placements: none, or each of the vertices 0..5.

**Units.** All sizes are in units of |G|.

## 1. Types and stabilisers

**The eight types.** A type is a triple (e2, c2, e3). Here e2 is either `None` or the E2 vertex, c2 ∈ {0, 1, 2} with 0 meaning "no E2", and e3 is either `None` or the E3 vertex. The types used are exactly:

```
(None,0,None) (None,0,0) (0,1,None) (0,1,0) (0,1,1) (0,2,None) (0,2,0) (0,2,1)
```

- (0,c,0) means E2 and E3 lie on the same vertex 0.
- (0,c,1) means they lie on different vertices.

**Completeness.** Every placement of E2 (with its class) and E3 on the six vertices is mapped onto exactly one of these types by some permutation in S6.

**Stabiliser of a type.** These are the permutations p of {0, …, 5} with p(e2) = e2 when e2 is not `None`, and p(e3) = e3 when e3 is not `None`. E2 and E3 are never exchanged. Orbits of a type are orbits of this group acting on α-labellings.

**String keys.** In run.json, types appear as Python tuple strings, for example `"(None, 0, None)"` and `"(0, 2, 1)"`.

## 2. Edge order and leaf codes

**Edge order E.** This order is used for every 15-character code:

```
(0,1),(0,2),(1,2),(0,3),(1,3),(2,3),(0,4),(1,4),(2,4),(3,4),(0,5),(1,5),(2,5),(3,5),(4,5)
```

These are the pairs (i,j) with i < j, sorted by (j, i).

**Codes.** A labelling is the 15-character string of its α-values, each in {1, 2, 3, 4}, written in edge order E.

**T-consistent leaves.** For a fixed type, a labelling is a *T-consistent leaf* if every one of the 20 triangles passes rule T (rules-k6-v1 L1).

- For each edge e of a triangle, take the vertex z opposite e and the table entry gcd(α_e, r_z):
  - α = 1: 1.
  - α = 2: 2 if z = E2, else 1.
  - α = 3: 3 if z = E3, else 1.
  - α = 4: 4 if z = E2 with c2 = 2; 2 if z = E2 with c2 = 1; else 1.
- **τ_min** is the lcm over the three edges e of α_e / gcd(α_e, r_z).
- **τ_max** is the minimum, over the three vertices, of the product of the two α's at that vertex.
- **T passes** if τ_min ≤ τ_max.

Every labelling that fails T on some triangle is killed by that triangle, by rules-k6-v1 L1. No further certificate is needed for it.

**What run.json reports per type** (under `summary[type]`):
- `leaves_labelled`: the number of T-consistent leaves.
- `pruned_nodes`: the number of pruned nodes. This count belongs to the engine's search order and does not need to be matched.
- `leafcodes_sha256`: the sha256 of the UTF-8 string formed by sorting all T-consistent leaf codes ascending, joining them with "\n", and appending a final "\n".
- `orbits`: the number of stabiliser-orbits of T-consistent leaves.
- `orbit_rule_counts`: counts by rule.

## 3. orbits.jsonl.gz

The file is gzip-compressed. It has one JSON object per line, and one line for every orbit of every type:

```
{"type":[e2,c2,e3], "code":"<engine canonical code>", "rep":"<15-char labelled representative, edge order E>",
 "rule":"K|RLP|PB|Ppair|FH5|N26|RPLP|SURVIVE", "witness":[...]}   (no "witness" key when rule is SURVIVE)
```

- `code` is the engine's canonical form. A checker should use its own canonical form and check that the representatives (`rep`) meet each orbit exactly once.
- The rule fields below all refer to `rep`, read as a labelled pattern of the given type.

### "K", witness `[v, S]`

This is rules-k6-v1 L3 with K1.
- **Check:** Σ_{i∈S} α_iv ≥ 5, and τ_min(i,v,j) = α_iv·α_vj for every pair {i,j} ⊆ S. Here τ_min is computed on the triangle {i, v, j} as in §2.
- **Proves:** the pattern is impossible, because L3 requires Σ ≤ 4.

### "RLP", witness `[v]`

This is rules-k6-v1 L7 with rules-k6-v2 L9.

**Neighbours.** Write N for the five vertices other than v, in ascending order. For each j ∈ N, set st_j = (E2-class digit, E3 flag). The class digit is 0 if j is not E2 and c2 if j is E2. The flag is 1 if j = E3 and 0 otherwise.

**Admissible q.** Every q ∈ ∏_{j∈N} {1, …, 5 − α_vj}, enumerated in itertools.product order with the first neighbour varying slowest.

**Allowed supports S** (S is a non-empty subset of positions 0..4 of N; every subset must be considered):
1. **Exponents.** For each position x: e2(x) = v₂(q_x) + {0 if digit 0; 1 if digit 1; SAT if digit 2}, and e3(x) = v₃(q_x) + {SAT if flag 1}. Here SAT is any number ≥ 3 for 2 and ≥ 2 for 3, for example 30.
2. **maxgcd.** maxgcd(x,y) = 2^min(e2(x),e2(y)) · 3^min(e3(x),e3(y)).
3. **Allowed.** S is allowed if |S| = 1, or if every subset T ⊆ S with |T| ≥ 2 contains a pair with maxgcd ≥ |T|.

**The dual.** In `rlp_duals.json`, under key = `"q_1,...,q_5|d1f1;d2f2;...;d5f5"` (digits of st_j in neighbour order), there must be y = list of 5 exact rationals as strings such that:
- y_x ≥ 0 for every x;
- Σ_{x∈S} y_x ≤ 1 for **every** allowed S;
- Σ_x (q_x/5)·y_x ≥ 1.

**Proves:** for every admissible q, the covering LP minimum is ≥ 1 by weak duality. So vertex v is impossible.

`value` in `rlp_duals.json` is informational. The check is the inequalities above.

### "PB", witness `[v, S]`, and "Ppair", witness `[v, [j,k]]`

This is rules-k6-v1 L4.

**Per pair** {j,k} ⊆ N, sizes in units of |G|:
- x_j = α_vj/5.
- u = 1/(5·gcd(r_v, α_jk)), with the gcd read from the §2 table taking z = v.
- **lo:** let Lb = max(τ_min(v,j,k)/(5α_jk), x_j + x_k − 1, 0). Then lo = u·⌈Lb/u⌉, the least multiple of u that is ≥ Lb.
- **hi:** start from hi = u·⌊min(x_j, x_k)/u⌋, the greatest multiple of u that is ≤ min(x_j, x_k). If hi = min(x_j, x_k), lower it by one u when the containment is barred:
  - if x_j < x_k, barred unless α_vj + α_kj ≤ 4;
  - if x_k < x_j, barred unless α_vk + α_jk ≤ 4;
  - if x_j = x_k, barred unless both inequalities hold.

**Ppair:** check lo > hi for the witnessed pair.

**PB:** every pair of N has lo ≤ hi (otherwise a Ppair would apply), and
  Σ_{j∈S}(1 − x_j) − Σ_{{j,k}⊆S}(1 − x_j − x_k + hi_jk) ≥ 1.

**Proves:** the pattern is impossible.

### "FH5", witness `[[a,b], V, counts]`

This is rules-k6-v1 L5 and L6 with rules-k6-v2 L9.

**Hypotheses and setup:**
- α_ab = 1, and V = {v ∉ {a,b} : α_va = α_vb} is non-empty.
- There are m = 5 cosets, labelled 0..4.

**Coset choices for each vertex l:**
- l = a: fixed to t = 1 and coset set {0}.
- l = b, or l ∈ V with α_la = 1: t = 1, with each of the 5 singletons.
- l ∈ V with α_la = c > 1: t = c, with all C(5,c) subsets.
- Every other vertex: t ∈ {1..5}, with all t-subsets.

**Rejection rules.** An assignment is rejected iff (i) or (ii) holds:
- (i) (F3) fails: some vertex i with t_i = 1 has α_il > t_l for some l ≠ i.
- (ii) Some coset c has a member set M_c = {l : c ∈ set_l} of size ≥ 2 that contains a subset T, |T| ≥ 2, in which no pair has fgcd ≥ |T|.

Here fgcd(x,y) = 2^min · 3^min · 5^min of the exponents of λ_l = r_l·t_l:
- 2-exponent: v₂(t) + {1 if l = E2 with c2 = 1; SAT if l = E2 with c2 = 2};
- 3-exponent: v₃(t) + {SAT if l = E3};
- 5-exponent: v₅(t) + {SAT if l = e5}.

**The certificate.** Every assignment is rejected, for each of the seven placements e5 ∈ {None, 0, …, 5}. `counts` lists the number of assignments examined per placement. These counts are informational and depend on the engine's loop order.

### "N26", witness `[v]`

This is rules-k6-v3 L11. The check:
- v ≠ E2;
- α_vj = 2 for all j ≠ v;
- α_jk ∈ {2, 4} for all pairs j, k ≠ v;
- If v = E3: τ_max(j,k,l) < 3·τ_min(j,k,l) for **every** triple j, k, l ≠ v.
  - Why this suffices: every α among the neighbours lies in {2, 4}, so every τ_min is a power of 2, and τ is a multiple of τ_min that is ≤ τ_max.
  - The possible τ by triangle type are listed below. "At most one 4-edge" means that at most one 4-edge has its divisibility reduced by E2.

    | triangle | τ_min | possible τ |
    |---|---|---|
    | 2,2,2 | 2 | {2, 4} |
    | 2,2,4 | 2 or 4 | {2, 4} or {4} |
    | 2,4,4 | 4 | {4, 8} |
    | 4,4,4 | 4 | {4, 8, 12, 16} |

  - So the only τ divisible by 3 is 12, in a 4,4,4 triangle. The test fails exactly for such triangles: τ_max = 16 ≥ 12 = 3·τ_min.

### "RPLP", witness `[v, certs]`

This is rules-k6-v3 L12.

**Shape of `certs`.** It has one entry per admissible q at v, in the itertools.product order defined under RLP.
- **["R", key]:** key is the RLP key for this q, and its dual must pass the RLP check above.
- **["P", vec]:** vec is a list of 30 exact rationals as strings, giving (a_j for j ∈ N ascending; b_j for j ∈ N ascending; u_p for pairs p of N in lexicographic order; l_p in the same pair order). The checks below apply.

**Exponents and allowed S** are as for RLP, with q.

**Forced containments.** These are the pairs (w,j) of N with τ_min(v,w,j) ≥ α_vw·α_wj.

**Columns.** All (A, S) such that:
- A ⊆ N is non-empty;
- no forced pair (w,j) has j ∈ A and w ∉ A;
- S ⊆ A, where S is empty, a singleton, or hereditary-allowed.

**Checks for ["P", vec]:**
- u_p ≥ 0 and l_p ≥ 0.
- **Every column:** Σ_{j∈S} a_j + Σ_{j∈A} b_j − Σ_{p⊆A} u_p + Σ_{p⊆A} l_p ≤ 1.
- **Objective:** Σ_j a_j(q_j/5) + Σ_j b_j(5 − α_vj)/5 − Σ_p u_p·yhi_p + Σ_p l_p·ylo_p ≥ 1, where for p = {j,k}:
  - yhi_p = 1 − (α_vj + α_vk)/5 + hi_jk;
  - ylo_p = 1 − (α_vj + α_vk)/5 + lo_jk;
  - lo and hi are as defined under PB.

**Proves:** for every admissible q, the joint LP minimum is ≥ 1, or the LP is infeasible (weak duality, or Farkas). So vertex v is impossible.

### "SURVIVE"

No rule killed the orbit. Such orbits are listed in survivors.json; the expected number is 0.

## 4. What the whole certificate set proves

**Statement.** Every pattern of Core5(6) is equivalent under S6 to a T-consistent leaf of one of the 8 types, or is killed by T. Every orbit of T-consistent leaves of each type has a line with a valid certificate.

**Conclusion.** If every line verifies and there is no SURVIVE line, then no Core5(6) configuration exists. This rests on:
- the written proofs of the rules;
- the evaluation-point lemma rules-k6-v1 L8 (M1, M2);
- the frame inputs: Sun(k ≤ 4) from Zhu; Sun(5) from the accepted Core(5) result (R/sun-coset5-parent-verdict-v1.md); and Sun(6) in proper subgroups, by minimality. The last is used only when 6 vertices meet one fibre coset in FH5.
