DISPOSITION: ACCEPT-WITH-FIXES

This is a static audit of the packet only. Nothing was executed. Receipt values are taken as rendered; this rendering cannot be re-hashed to `d688277f…`.
Legend: **N** = `review/K4_ORBIT_REDUCTION.r1.md`, **C** = `code/k4_automorphism_r2.py`.

The transfer lemma and the exact automorphism test are sound. There is no FATAL finding. Two gaps sit exactly at the soundness hinge, and both are fixable. Fixing M1 means re-issuing the receipt.

## FATAL
None.

## MAJOR

**M1. The verified permutation is never bound to the permutation the ledger applies (item 6).**
- C:197–204 builds π1 and π2 in memory only. C:268–279 serialises booleans, counts, σ lists and ρ dicts, but no array and no hash.
- N:51–52 then has the validator re-derive π_w "from the generator definitions (σ, ρ) and the pinned name table". That is the construction route N:34–36 declares irrelevant to soundness.
- So the receipt certifies "the map produced by C:67–107 on the pinned table is an automorphism". Certificates, however, would be checked against whatever a second, unreviewed implementation produces.
- A divergent reconstruction (σ list, ρ, canonicalisation, index) can map lits(R) onto a cube outside R's orbit, e.g. c001 ↦ c016. The set test at N:52 would then certify a leaf that no automorphism relates to R.
- "Leaf literals are g-variables only" (N:52) is an assumption, not an obligation. A g-only map that defaults to identity on other variables becomes unsound the first time a leaf carries a non-g literal.

Fix:
- r3 writes π_g1 and π_g2 as full arrays over 0..V (perm[0]=0, LE int32) to pinned files.
- It runs C:106 and C:127 on the re-loaded bytes and records their SHA-256 in both the receipt and the verdict.
- The validator composes only those arrays (N:22–23) and rejects any literal with |l| ∉ [1,V].
- The name table then genuinely becomes construction-only.

**M2. lits(·) is undefined, and §3.3 reuses "R" for a different object. The same-π property holds only for full-path cubes (item 4).**
- N:48 and N:52 make R the source node. N:62–64 make R the root, describe the test as "π_w maps the sibling's literals to the child's", and leave π_w ∈ H_R as prose.
- The lemma (N:16–20) covers exactly the unit set of the formula proved UNSAT.
- With per-node (incremental) literal sets, N:52 accepts g1 for c016.y → c016.x. g1 maps the V2 part y to x but sends lits(c016) to lits(c032). What is actually proved is F4∧lits(c032)∧x UNSAT, not the leaf being closed.
- With full cubes, the problem disappears:
  - |π(S)| = |S|.
  - Every group element preserves the V1 and V2 variable sets. The receipt shows this: all_images_are_roots, and c000 has stabiliser order 6 with V2_images_are_children.
  - So equality of 14-literal cubes forces the *same* π to map parent→parent and extension→extension, and π_w ∈ H_parent follows automatically.

Fix:
- Define lits(X) := all cube literals on the path root→X, i.e. exactly the units appended to the base in X's leaf CNF.
- The validator derives lits(X) from the tree, never from a stored per-node field.
- For strict sources, the validator also checks lits(R) against the unit set of the leaf CNF bound in that strict receipt.
- Rename 3.3's R (e.g. to P), and state that the stabiliser condition is a consequence of (b).

## MINOR

- **m1 (N:69–71): trust base misstated.**
  - Orbit certificates add the checker (NumPy parse, row sort, lexsort), the lemma, and the new validator rule to the TCB.
  - "Re-run C" replays the same logic, so it cannot catch the code's own bugs.
  - Make an independent check a GO condition: a different code path and DIMACS parser, run on the M1 arrays.
- **m2 (N:21–22): the DRAT remark is unqualified and unused.**
  - It holds only if:
    - renaming is in place (no sort or dedup), so the RAT pivot stays first;
    - π is extended by identity to proof-introduced variables > V;
    - deletions are renamed literally (drat-trim's unit-deletion handling is renaming-invariant);
    - binary DRAT is re-encoded.
  - It does **not** hold for LRAT/FRAT/LPR as-is. Hints are positional, and π(F)=F only as a multiset, so clause IDs need an explicit matching.
  - Either qualify it or mark it non-load-bearing.
  - Optional hardening: emit π(P) and DRAT-check it against L's leaf CNF. That gives a strict certificate needing no automorphism trust.
- **m3 (C): hash/parse binding.**
  - The SHA (C:151) and the parse (C:175) are separate reads, a TOCTOU gap made more relevant by the concurrent K5 run (N:13). Hash `raw` instead.
  - Tokens after the last 0 belong to no clause, because C:180–182 build clauses from zeros only.
  - `np.fromstring` (C:178) stops at a non-numeric token with only a warning.
  - C:185 catches truncation inside the clause region, but not a trailing unterminated clause.
  - Assert `arr[-1]==0` and `lens.sum()+zeros.size==arr.size`.
- **m4 (N:55–57): validator obligations incomplete.**
  - (i) Run the topological check on the combined dependency graph, parent→child plus L→R edges. Orbit-only acyclicity suffices only because, under M2, orbit edges preserve cube size and refinement increases it.
  - (ii) Explicitly forbid R = L.
  - (iii) A REFINED source must be an exact partition: 128 distinct V2 assignments, each child cube = parent cube ⊎ assignment. Internal-node settledness is newly load-bearing.
  - (iv) Allow one evidence record per node.
  - (v) Pin the alphabet "g1"/"g2" to the M1 hashes.
- **m5 (N:50): require strict JSON `true` by identity.**
  - C:279 uses `default=str`, which would turn any NumPy scalar into "True"/"False", and "False" is truthy.
  - Also check receipt `script_sha256`, `names_sha256` and the M1 hashes against the pins.
- **m6: claims not verifiable from this packet.**
  - The receipt rendering cannot be hashed.
  - V2_children is cut after c062, so the c112 claim at N:43 is not visible. It is expected by structure, since c112 sets all three permuted bits.
  - Label N:39–43 as planning-only. A wrong table can only leave leaves UNKNOWN; it cannot certify one.
- **m7 (N:8–9; C:152, 169–172): lane-map cross-check is not a binding.** The map SHA is pinned nowhere, the mismatch count is not enforced, and the check is one-directional. Don't cite it as a binding.
- **m8 (N:53–54): "only V1–V3" is not a consequence of the group.** (6 7) fixes row 5. This is harmless, but don't encode it as a rule.
- **m9 (N:36–38, N:44): unverified commentary.** "Explains WHY" and "moves the SB2 units" are not established by the receipt; label them as commentary.
- **m10: checker hygiene.**
  - C:163 `assert` vanishes under -O. A failure would still surface at C:101, but make the check explicit.
  - C:59–64 canonicalise lossily (T drops extra components; `line_id` never checks collinearity). Collisions are caught at C:166–167 and non-bijections at C:106, so there is no soundness impact.
  - C:35 uses an absolute path, so replay elsewhere changes the script SHA.
  - C:44–48: ru_maxrss is in bytes on darwin and KiB on Linux, so the guard is inert on Linux.
  - Record Python and NumPy versions.
- **m11 (N:44–45; C:198–209): weak controls.** Add a polarity-flip control (v ↦ −π(v)) and a non-injective control. The 57/64 swap touches only two fixed cube-row variables.

## Audit items

1. **Transfer lemma (N:16–24): correct.**
   - β is total because π is onto 1..V. Polarity is handled by π(−v) = −π(v). The converse follows from π⁻¹.
   - Cube transfer by exact set equality (N:52) is what the lemma needs.
   - Certificates rely only on the semantic statement; for DRAT renaming see m2.
   - Using residual symmetry is compatible with SB2, standard form and weight1, because the automorphism is checked on F4 itself, those clauses included.
2. **Checker: correct for the map it builds.**
   - Total: C:100–105, unmapped 0.
   - Bijective: C:106, sorted image = 1..V exactly.
   - Polarity-preserving: C:121–124; perm[0]=0 keeps terminators.
   - Exact multiset equality, no hashing: C:110–118 sort rows, then lexsort with column 0 primary; C:127–129 compare with array_equal per length.
   - V = table size = header vars (C:185). Any literal > V would raise IndexError.
   - Family counts sum to 513184, so every variable is named.
   - Injectivity (C:164–168) plus the integer-array bijection test mean the name layer cannot hide a collision.
   - Receipt internals match N:5–13: hashes, counts, timing 17:02:10–17:02:28 PDT, peak 1,753,612,288 B.
   - Residual gaps: M1 and m3.
3. **Group: correct, but not needed for soundness.**
   - `comp(p,q)=p[q]=p∘q` matches N:23.
   - g1²=g2²=(g1g2)³=1 with g1g2≠1 forces both generators to be nontrivial and the group to be S3.
   - The BFS closure is correct, and all 6 elements are re-checked exactly (C:232).
   - Soundness does not need the order-6 result, since any word is a product of verified automorphisms.
4. **Orbits: consistent with the receipt.**
   - The action is the natural S3 action on bits 4–6 (253/302/351), with bits 0–3 fixed: 16·4 = 64 orbits.
   - Stabiliser orders are 6 and 2. Child orbits are 16·4 = 64 under S3 and 16·6 = 96 under a transposition.
   - Depth 1 is sound: non-representatives are terminal, and the transfer from a SETTLED (possibly REFINED) representative is semantic.
   - Depth 2 is sound iff full-path cubes are used (M2).
5. **Ledger contract.**
   - (a): see m5. (b): see M1 and M2. (c): see m4.
   - (d) is adequate. It is also needed so the terminal-leaf completeness rule (N:65–66) never looks past orbit evidence.
6. **Construction dependence: currently yes, via N:51–52 (M1).**
   - After M1, soundness rests only on: the pinned F4 bytes, the pinned arrays, an independently replayed exact check, the lemma, and the ledger's set and graph checks.

**GO conditions:**
- Fix M1 and M2.
- Issue an r3 checker that includes the m3 and m10 fixes, re-issue the receipt with the array hashes, and have it replayed independently.
- Update the validator spec per m4 and m5.
