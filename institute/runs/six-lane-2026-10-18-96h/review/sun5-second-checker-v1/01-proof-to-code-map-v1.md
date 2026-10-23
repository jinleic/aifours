# Sun5 second checker v1 — mathematical bridge and proof-to-code map

- Written: 2026-10-19T17:28:30-0700 (host /bin/date). Source-only; nothing executed.
- Checker: `code/sun5_second_checker_v1.py`, sha256 a6ecf3122320b321e899504778fe5024bba96dc4babe8fd04d025d0d260b78f0, 38302 bytes. Line numbers below refer to this exact file.
- Sources of every predicate: proof-v4.md (3d17efcc…4516), rules-v1.md (cb86c168…390f), rules-v1-erratum-v3.md (1b3e126e…25e8ed), README.md (6bff400c…a75e), README-addendum-v4.md (2995d392…0953). No earlier checker/engine/controls code was read.

## 0. Theorem chain and what this program covers

| step | statement | basis | checked here |
|---|---|---|---|
| R0 | any counterexample yields one in a finite group | proof-v4 §1 | no (written) |
| R1 | Sun(5) ⇔ Core(5) group by group; Prop 4.5 | proof-v4 §2 (+ Zhu Thm 1.1 import) | no (written) |
| min | a minimal-order counterexample G carries a Core(5) configuration; proper subgroups satisfy Sun(5); every group satisfies Sun(k≤4) | proof-v4 §3 | no (written) |
| P | its pattern (α,E2,E3) lies in 𝓛 | rules-v1 §0, L0.3 | universe definition (§1 below) |
| C | every labelled pattern of 𝓛 outside orbit(S-D) is impossible | rules-v1 L1–L8 + erratum v3, certificate per orbit | **yes: the whole finite obligation** |
| S-D | orbit(S-D) is impossible | proof-v4 §5 Lemma R, §6 | no (written); checker only proves SURVIVE coverage = orbit(S-D) exactly |
| close | no counterexample | proof-v4 §7 | no (written) |

PASS (`PASS_MODULO_WRITTEN_SD`) certifies exactly row C plus the exact identity "uncertified residue = orbit(S-D)". The lemma statements L1–L8/H2/F/N2 are used as written and reviewed elsewhere; the checker verifies that each certificate satisfies the hypotheses of the cited lemma for its pattern, for all admissible τ and all admissible r.

## 1. Universe 𝓛 (completeness)

- α_ij = [G:U_i∩U_j]/(4r_ir_j) ∈ {1,2,3} for every pair (rules-v1 L0.3: 1 ≤ α ≤ g_ij − 1 with g_ij = 4). E2 = the unique vertex with r even, or none; E3 = the unique vertex with 3 | r, or none; E2 = E3 allowed (rules-v1 §0). Uniqueness: r pairwise coprime. So every Core(5) configuration has a pattern in 𝓛 = {1,2,3}^{E(K5)} × (V∪{none})².
- Code: constants `EDGES` (l.57), `ALPHA_VALUES` (l.64), `N_COLOURINGS = 3^10` (l.65), `MARKER_SYMBOLS` (l.66), `N_LABELLED` (l.69). `build_universe` (l.360–384): every colouring c ↔ the disjoint pair (A1, A2) = (c⁻¹(1), c⁻¹(2)); A1 ranges over all 2^10 subsets of E and A2 over all submasks of E∖A1 (standard descending-submask enumeration ending at 0), so each colouring is produced exactly once; a direct-address table detects any repeat; the count is compared with 3^10 from the definition. Markers: 6 × 6 indices (none + 5 vertices each). Dense index `dense_index` (l.387–388).
- Key decoding (cited, not guessed): engine-v1-run1/survivors.json decodes `1122333333/10` as α in edge order 01,02,03,04,12,13,14,23,24,34 followed by E2, E3; controls.json data and the six observed marker symbols {0,…,4,-} versus the six marker values per proof-v4 §4/§7 (vertex or none) fix `-` = none. Robustness: the PASS statement is about the checker's own universe and decoding; a wrong decoding cannot create a false PASS because coverage and every certificate are re-derived under the checker's decoding.

## 2. Relabelling and orbit partition

- If a configuration (U_i, g_i) has pattern x, then for π ∈ S5 the relabelled configuration (U_{π⁻¹(i)}, g_{π⁻¹(i)}) has pattern π·x with (π·α)(π(i),π(j)) = α(i,j), π·E2 = π(E2), π·E3 = π(E3). Hence "no configuration has pattern x" is S5-invariant and one verified certificate on any representative disposes of its whole orbit (proof-v4 §4 "every rule is S5-equivariant").
- Code: `build_group` (l.316–336) closes {(0 1), (0 1 2 3 4)} under composition and requires 120 distinct bijections (= |S5| = 5!, so the closure is S5); `edge_permutation`, `mask_table`, `marker_map` (l.339–357) implement the induced action on masks and one-hot markers; `orbit_of` (l.391–409) forms {g·x} and the stabiliser size, requiring |orbit|·|stab| = 120 and no image outside 𝓛 (else INCOMPLETE_ERROR).
- Exact set equality (run l.748–790): an owner array over all |𝓛| indices; each record's full orbit is written into it; any already-owned index → `ORBIT_OVERLAP`/`ORBIT_OVERLAPPED` on both records; any unowned index after all records → `UNIVERSE_MISSING` (with decoded examples); duplicate key strings → `PARSE_DUPLICATE_KEY`. PASS requires missing = 0 and overlap = 0, i.e. ⋃ orbits = 𝓛 and orbits pairwise disjoint — set equality, not totals.
- Independent cross-check (l.816–825, `burnside_orbit_count` l.422–438): (1/120)Σ_π 3^{#edge cycles of π}(1 + #fixed vertices)² must be an integer and, under an exact partition, equal the number of keyed records; mismatch → INCOMPLETE_ERROR. No old count is used anywhere.
- No canonical form is computed or compared.

## 3. Marker / high-cofactor interface (how r enters)

Every rule depends on r only through the following, and the checker evaluates them for **all** pairwise-coprime r with the given marker status, never by representative numbers:
1. gcd(α, r_z) for α ∈ {1,2,3}: = 2 iff α = 2 and z = E2; = 3 iff α = 3 and z = E3; else 1 (rules-v1 L1 Core(5) form; erratum v3 E5). Code `gcd_alpha_r` (l.444–452). Used by T (τ_min) and K (links), and as γ = gcd(r_v, α_jk) by PB (rules-v1 L4 P2: gcd(4r_v, 4r_jr_kα_jk) = 4·gcd(r_v, α_jk) because gcd(r_v, r_jr_k) = 1).
2. FH2 only: gcd(λ_l, λ_l') with λ_l = 4r_lt_l/m. For l ≠ l': a prime p ≥ 5 dividing both would divide r_l and r_l' (t ≤ 4 < p, m ∈ {2,4}), impossible; so gcd = 2^{min v2}·3^{min v3} with v2(λ_l) = 2 + v2(r_l) + v2(t_l) − v2(m) and v3(λ_l) = v3(r_l) + v3(t_l). v2(r_l) = 0 unless l = E2, where it is an arbitrary integer ≥ 1; v3 likewise with E3. `lambda_exponents` (l.560–569) returns None (= unbounded) for the marker vertex; `min_exponent` (l.572–579) returns the other (finite, since l ≠ l' and markers are unique); `lambda_gcd_sup` (l.582–585) is therefore the supremum over all instances, attained simultaneously for all pairs by any r with large v2(r_E2), v3(r_E3). The kill test "all pairwise gcds < s" is monotone (each instance's gcd ≤ the sup), so a kill at the sup is a kill for every instance, including r_i = 1 and arbitrary prime powers. This replaces the engine's representative 16/81 (rules-v1 L8 M2) by the exact supremum.
3. τ never enters FH2, PB hi, K2 or N2 (rules-v1 L8 M1); T and K use τ_min only as below.

## 4. Certificates

### T(a,b,c) — rules-v1 L1, L8 M1; proof-v4 §4
- (T1) Core(5): α_xy | r_zτ ⇔ (α_xy/gcd(α_xy,r_z)) | τ, so admissible τ are the multiples of τ_min = lcm of the three quotients; (T2) Core(5): τ ≤ product of the two α's at each vertex, so τ ≤ τ_max = min vertex product. τ_min > τ_max ⇒ no admissible τ.
- Code: `tau_min` (l.459–464), `tau_max` (l.467–469), `check_t` (l.472–484): reasons `T_SERIALIZED_TAU_MIN_MISMATCH`, `T_SERIALIZED_TAU_MAX_MISMATCH`, `T_NOT_KILLING`.

### K(v,S) — rules-v1 L2, L3 (K1), L8 M1; erratum v3 E9
- For each pair {i,j} ⊆ S: if τ_min(v,i,j) = α_viα_vj then either τ_max(v,i,j) < τ_min (T-kill of that triangle, pattern impossible) or τ_max = τ_min (τ_max ≤ α_viα_vj) and τ = τ_min is forced, giving (T3) |U_i(U_v∩U_j)| = τ|G|/(4α_vj) = α_iv|G|/4 = |U_iU_v|, hence by L2 U_vU_i ⊆ U_jU_i — L3's first alternative (no inversion needed). With every pair linked, L3 gives Σ_{i∈S} α_iv ≤ 3; the certificate requires Σ ≥ 4.
- Code: `check_k` (l.487–500): `K_LINK_ABSENT:ij`, `K_SUM_BELOW_4`, `K_SERIALIZED_SUM_MISMATCH` (serialized value = Σα_iv/4, see schema).

### PB(v,S) — rules-v1 L4 (P1, P2, P4, P5), K2
- x_j = |X_j|/|G| = α_vj/4 (P1); |X_j∩X_k| is a multiple of u = 1/(4γ), γ = gcd(r_v, α_jk) (P2); |X_j∩X_k| ≤ min(x_j, x_k), and equality forces X_j ⊆ X_k (resp. the reverse, resp. both when x_j = x_k), which K2 permits only if α_vj + α_jk ≤ 3 (resp. α_vk + α_jk ≤ 3, resp. both) (P4). So |X_j∩X_k| ≤ hi_jk := largest multiple of u ≤ min, minus u if the forced containment is barred. (P5) Bonferroni with ⋃Y_j ⊆ G∖U_v: Σ(1−x_j) − Σ_pairs(1−x_j−x_k+|X_j∩X_k|/|G|) < 1; the left side is non-increasing in each intersection, so value(hi) ≥ 1 contradicts (P5). Independent of τ and of r beyond γ.
- Code: `pb_value` (l.503–529), `check_pb` (l.532–540): `PB_NOT_KILLING`, `PB_SERIALIZED_VALUE_MISMATCH`.

### N2 — rules-v1 L5
- Hypothesis: all ten α = 2 (valid for every marker status). Code `check_n2` (l.543–547): `N2_NOT_ALL_TWO`.

### FH2(a,b) — rules-v1 L6 (F1–F3), L7 H2; proof-v4 §4
- Hypotheses: α_ab = 1 and V2 = {v ∉ {a,b} : α_va = α_vb = 2} ≠ ∅ (recomputed, must equal the serialized list). H2: W = ⟨U_a,U_b⟩ satisfies (i) [G:W] = 4, t_v = 2 on V2, or (ii) [G:W] = 2, t_v = 1 on V2; t_a = t_b = 1 in both. The SAME W (same a,b) is used in both alternatives; both must be refuted.
- F with H = W, m = [G:W]: (F1) t_l ∈ 1..m and g_lU_l meets exactly t_l left cosets (met set M_l, |M_l| = t_l); (F2) a coset with s ≥ 2 met vertices needs gcd(λ_l,λ_l') ≥ s for some pair (Sun(s) in H: L0.6 for s = 2, Zhu for s = 3,4, minimality for s = 5 since H is proper); (F3) t_i = 1 ⇔ U_i ⊆ H ⇒ α_il/4 ≤ t_l/m for every l ≠ i.
- Enumeration domain (`fh2_options` l.611–622): M_a = {0} (relabelling the m cosets is the only symmetry used); b: any singleton; V2: all t_v-subsets; every other vertex: every t ∈ 1..m and every t-subset; no coverage or balance constraint. `fh2_rejected` (l.588–604) implements (F3) at every t = 1 vertex against every other vertex, then (F2) at every coset with the sup-gcd of §3. `fh2_case` (l.625–637) counts all assignments and survivors. `check_fh2` (l.640–665): `FH2_ALPHA_AB_NOT_1`, `FH2_V2_EMPTY`, `FH2_V2_MISMATCH`, `FH2_CASE_I_NOT_REFUTED`, `FH2_CASE_II_NOT_REFUTED`, `FH2_COUNT_I_MISMATCH`, `FH2_COUNT_II_MISMATCH` (serialized counts must equal the exact number of assignments enumerated in each case).

### SURVIVE — proof-v4 §4, §6
- S-D is hard-coded from proof-v4 §6 (`SD_ALPHA`, `SD_E2`, `SD_E3`, l.73–76), never from the extract. Its orbit is computed (run l.727–746) and its stabiliser must equal the text's {id,(3 4)} (`SD_STABILISER_TEXT` l.78), else INCOMPLETE_ERROR. A SURVIVE record is `WRITTEN_SD` iff its orbit equals orbit(S-D) exactly (l.772–776); otherwise `SURVIVOR_NOT_SD` → FAIL. Coverage exactness makes orbit(S-D) the entire uncertified residue. WRITTEN_SD is never counted as VERIFIED.

## 5. Rules not admitted
P-pair and F-H1 appear in the rules-v1 engine order but no run1 record uses them and their serialization is not cited; any such tag (or any other tag) → `PARSE_UNKNOWN_RULE` → FAIL. This is fail-closed, not a mathematical claim.

## 6. Fail-closed interface
- Input bytes read once, sha256 compared with `--expected-sha256` before parsing (`run` l.694–706); mismatch → INPUT_PIN_MISMATCH, nothing verified.
- `Guard` (l.115–139): SIGTERM/SIGINT flag, cancel-file existence, deadline; polled in parse, tables, universe, coverage, witnesses, FH2 enumeration, labelled accounting, pre-publication and again just before COMPLETE.json (`late`, l.940).
- `decide` (l.846–859): pin mismatch → INPUT_PIN_MISMATCH; internal error → INCOMPLETE_ERROR; any file-level reason or FAILED record → FAIL; stop → INCOMPLETE_*; any UNVERIFIED or incomplete phase → INCOMPLETE_ERROR; else PASS.
- `publish` (l.904–954), `write_exclusive` (l.865–882): records.tsv, RESULT.json, COMPLETE.json each O_CREAT|O_EXCL, mode 0444, full write loop, fsync, read-back equality; COMPLETE.json last, binding both hashes, with `pass_valid` true only for PASS with no late stop condition and finish < deadline. Any exception → exit 7, no COMPLETE marker. Exit 0 only when pass_valid.

## 7. Irreducible gaps
None found inside the finite obligation (row C). Outside it, the result still depends on the written steps R0, R1/Prop 4.5, minimality, Lemma R/S-D and the imported Zhu Theorem 1.1 and standard facts, and on the reviewed truth of the lemma statements L1–L8 as written; this checker does not re-prove them.
