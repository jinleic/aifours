# Ame46CoverAudit report (verbatim)

Recorded 2026-10-17 13:33:21 PDT. Agent output is untrusted until parent-bound.

I found no FATAL problem and no mathematical error in my slice (profile enumeration, N-only encoding, symmetry/orbit blocking, CNF binding). All 14 final-enumeration CNF headers match clause and variable counts I derived by hand from the code. In 6 checked cases each listed representative sits in the right block segment. That is static consistency evidence only. Parent regeneration of every block segment and the parent proof re-checks are still not done.

## Findings

**FATAL:** none.

**MAJOR — open verification gap; no defect found**
- **M1. The receipt does not check that the final CNFs match the listed orbits.**
  - `code/lower46_receipt.py:54-80` loads each JSON, hashes the files, runs the two LRAT checkers and trusts the engine flags (`ok &= r["excluded"]`, line 74).
  - It never regenerates the base clauses, never recomputes orbits, and never compares the blocking clauses with the listed representatives.
  - It also loops only over profiles already in the JSON (line 60), so a dropped profile would not be noticed.
  - The binding currently rests on what the code does (`large_t_gen.py:204-221`) and on my static checks below. It closes only when the parent regenerates the files and compares them.

**MINOR**
- **m1. Stale moduli text and dead code.** The `large_t_gen.py:13-14` docstring still says the moduli check is "an exact rational LP (sympy)". The dead `moduli_lp` is still at lines 112-136. The code actually used is the scipy search plus exact certificate check (lines 164-188, 227-236). Not load-bearing: in all 28 representatives `components_ok=true`, `moduli_excluded=false` and the certificate is `null`.
- **m2. Receipt reason labels use fields that no longer exist.** `lower46_receipt.py:67-70` reads `moduli_ok` and `moduli_lp_max_eps`. A rep excluded by moduli would be mislabelled "completion None". The "phase obstruction" label ignores `phase_obstruction_verified`. Harmless for these runs.
- **m3. The e=0 cross-check engine is not independent.**
  - At e=0 the general CNF already forces exactly two points per hole line: the d-constraints give h hole lines per pair, each has at least 2 points, and |N| = 2h.
  - So `large_t_e0` without phase clauses has the same point-level solution set. It also shares `Small`, `profiles`, `group`, `apply`, `write`, the Sinz encoder, `solve` and `lrat_check`.
  - The orbit-size multisets do match (I checked t28 and t30 against `large_t_e0_t28_nophase.json` and `large_t_e0_t30_nophase.json`). But LOWER46:171-172 and 213 ("agrees") show reproducibility, not an independent check of the encoding, the profiles or H.
- **m4. The positive control covers only the full value set.** `engine_control.py` tests profile (6,6,3,3,3,3)⁴ at e=0, so every V_i = [6]. Nothing exercises a restricted product ΠV_i or e>0. For those, soundness rests on the written necessity argument, which I checked.
- **m5. LOWER46 §3 step 1 (lines 122-125) leaves out two caps** that `partitions` applies (`large_t_e0.py:34-46`): part ≤ 6 and at most 6 parts. Both are necessary. For h ≤ 8 they only drop (8), which Lemma 12 rejects anyway.
- **m6. "H maps solutions to solutions" is asserted, not proved** (LOWER46:142-143). It does hold:
  - π permutes only coordinates with equal partitions, so V and d are preserved.
  - Each β_i permutes values within one deficit class.
  - Lines go to lines and pairings to pairings (L42-11(a)); both row and column orientations are encoded.
- **m7. Building H is O(|H|).** `Small.group()` (`large_t_e0.py:135-155`) builds the whole group list, 7,962,624 elements for (2⁴)⁴. It is called even for profiles with no orbits (`large_t_gen.py:204`), and every element is applied per representative (line 218). This is correct, but it blows up at smaller t; that probably explains the 35 GB t26 run [INFERENCE].
- **m8. Block order is CPython set order** (`large_t_gen.py:218-220`). The engine ran under Python 3.13.9 (LOWER46:219-221); the receipt ran under 3.9.6 (`lower46_receipt.json` `"python"`). Byte-identical regeneration therefore depends on the interpreter.
- **m9. Unchecked status.** `large_t_gen.py:212` ignores the status of the run that writes the LRAT proof. Only `lrat_check` (line 213) gates acceptance, so this is sound.

## Code conclusions: all checks are necessary for arbitrary complex AME
- **Profiles** (`large_t_e0.py:34-58`). Partitions of h into parts ≥ 2 (L42-8(a),(b)), each part ≤ 6 (d ≤ 6), at most 6 parts. They are taken as multisets via `combinations_with_replacement`, then filtered by `max(prof[i]) ≤ min_{j≠i} len(prof[j])`, which is exactly Lemma 12.
- **Normal form** (`large_t_e0.py:64-67`): `V[i]=range(6−len(p),6)`, the parts in non-increasing order on increasing values, `var[x] = 1 + lexicographic rank in product(*V)`. N ⊆ ΠV by L42-8(c).
- **Clause families** in `build_gen` (`large_t_gen.py:42-85`):
  - F1 (lines 44-56): for each pair in `PAIRS=[(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]` and each (a,b) ∈ V_i×V_j:
    - a line variable v ⇔ OR(line), with clauses `[-v]+ns` and `[-n,v]`;
    - a 0-or-≥2 clause `[-n_x]+others`.
  - F2 (lines 57-64): for each ordered (i,j) and a ∈ V_i, `eqk` sets the number of hole lines (a,b), b ∈ V_j, equal to d_i[a].
    - Hole lines are exactly the lines with b ∈ D_j^{(i,a)} (L42-8, L42-2(a)), and D_j^{(i,a)} ⊆ V_j (Lemma 12).
  - F3 (line 65): |N| = 2h+e. This is just the definition of e.
  - F4 (lines 66-85): L42-5 for each reshaping in both orientations, with one-way auxiliaries aux→AND.
    - The clause fires only when both rows meet N, i.e. both rows are hole lines, whose whole support lies in N ⊆ ΠV.
- **Sinz encoder** (`ame_e0_cnf.py:48-68`): standard. `eqk(lits,k)` is at-most-k on the literals plus at-most-(m−k) on their negations. There are no phase, real or ansatz clauses; the TBL/TWIN families exist only in `large_t_e0` and are off in the cross-check (`"phase_clauses_in_cnf": false`).
- **Symmetry group H** (`large_t_e0.py:135-164`): π fixes the partition signature; β_i permutes within a d-class; the action is `(g·x)_{π(i)} = β_i(x_i)` (L42-11 form). There are no swaps across unequal deficits.
- **Blocking**: one clause per orbit image, `[-var[x] for x in sorted(img)]`. Every solution has exactly 2h+e points, so each clause blocks exactly one solution.
  - The pinned blocks have 12 literals (t30) or 16 (t28), as required.
  - The receipt's 28 representatives have 12 or 16 points.

## Exact cover map
For s ≤ 45: t ≥ 27 (L42-4), t ≤ 36 (L42-3), and e = s−72+t.
- **Written cases**
  - t = 36: Tarry.
  - t = 33, 34, 35: LOWER42.
  - t = 32: Lemma 16 with Lemma 15.
  - t = 31: Lemma 13.
  - e = 1 (t = 28, 29, 30): L42-7(b),(c).
  - (27,0) and (29,0): odd t with e = 0.
- **Computer cases:** (30,0), (30,2), (30,3), (29,2), (28,0).
- **Profiles removed by the Lemma 12 filter** (I enumerated these by hand):
  - h=6: any profile containing (6) or (4,2), or two copies of (3,3).
  - h=7: any containing (5,2) or (4,3).
  - h=8: any containing (6,2) or (5,3); (4,4) or (4,2,2) unless the other three coordinates are all (2⁴); (8) is never generated.

The table lists every remaining profile. In the header column, nv is the total variable count and the clause count is base + blocks.

| case | profile | \|H\| | base clauses | blocks (Σ orbit sizes) | header (nv, clauses) | representatives → exclusion |
|---|---|---|---|---|---|---|
| (30,0) | (3,3),(2,2,2)³ | 2592 | 9898 | 144 = 108+36 | 4122, 10042 ✓ | rep0 phase; rep1 completion UNSAT (`_rep1_completion`) |
| (30,0) | (2,2,2)⁴ | 31104 | 20365 | 0 | 8775, 20365 ✓ | — |
| (30,2), (30,3) | (3,3),(2,2,2)³ | 2592 | 9898 | 0 | 4122, 9898 ✓ (both) | — |
| (30,2), (30,3) | (2,2,2)⁴ | 31104 | 20365 | 0 | 8775, 20365 ✓ (both) | — |
| (29,2) | (3,2,2)⁴ | 384 | 20245 | 0 | 8703, 20245 ✓ | — |
| (28,0) | (4,4),(2⁴)³ | 165888 | 47590 | 78192 (14 reps) | 20968, 125782 ✓ | rep6, rep7 completion UNSAT; 12 phase |
| (28,0) | (4,2,2),(2⁴)³ | 165888 | 99334 | 21600 (7 reps) | 44868, 120934 ✓ | 7 phase |
| (28,0) | (3,3,2)⁴ | 384 | 20125 | 16 | 8631, 20141 ✓ | rep0 completion UNSAT |
| (28,0) | (3,3,2)³,(2⁴) | 1152 | 34315 | 0 | 15021, 34315 ✓ | — |
| (28,0) | (3,3,2)²,(2⁴)² | 9216 | 58365 | 0 | 25981, 58365 ✓ | — |
| (28,0) | (3,3,2),(2⁴)³ | 165888 | 99400 | 0 | 44904, 99400 ✓ | — |
| (28,0) | (2⁴)⁴ | 7962624 | 169790 | 64800 (4 reps) | 77728, 234590 ✓ | 4 phase |

- **Totals:** 14 final-enumeration CNF/LRAT pairs plus 4 completion pairs = 18. There are 28 representatives: 24 excluded by phase obstruction, 4 by completion UNSAT.
- **Group orders:** every |H| equals the formula ∏(sizes of runs of equal partitions)! × ∏_i ∏(sizes of runs of equal deficits)!, and every orbit size divides |H|.
- **Static binding checks I ran:**
  - All 14 headers match.
  - The base/block boundaries fall exactly at base+1 for (30,0)(3,3), (4,4), (4,2,2), (3,3,2)⁴ and (2⁴)⁴.
  - Each representative's own clause lies in its expected segment:
    - t30_e0 rep0 at line 9945 (segment 9900–10007) and rep1 at line 10027 (10008–10043);
    - (4,4) rep0 at line 49049 (47592–50183);
    - (4,2,2) rep0 at line 99738 (99336–101927) and rep6 at line 120361 (120072–120935).
  - For (3,3,2)⁴, lines 20127–20142 are 16 distinct clauses forming the full 2⁴ value-swap pattern and including rep0. I confirmed one generator image by hand.
  - The grep tool only scans the first 4 MB of a file, so I could not check (2⁴)⁴ representatives past that point.

## APIs to rebuild a base CNF without a solver
Use `python -B` on a scratch copy of the code. Importing `large_t_gen` needs only the standard library plus `large_t_e0`, `ame_e0_cnf` and `phase_check`; numpy, scipy and sympy are imported lazily, only by the moduli functions.
```python
prof_list = lte.profiles(36 - t)        # canonical 4-lists of tuples (large_t_e0.py:50-58)
S = ltg.SmallGen(prof); S.build_gen(e, h)   # S.cl = base clauses, S.nv = total vars (no I/O)
tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof)
# Serialization (large_t_e0.py:166-170): f"p cnf {nv} {len(cl)+nblocks}\n", then " ".join(map(str,c))+" 0\n"
```
- The base clause order is F1, then F2 (i-major, then j, then a), then F3, then F4 (reshaping, orientation, row pairs, then per column: 2 auxiliary binary clauses, then the long clauses). No set or dict iteration affects the order, so the base portion should be byte-reproducible.
- Do **not** call `run()` (it writes files and runs cadical), `group()` or `write()` into the snapshot.

## Blocking-clause order and safe regeneration
- **Layout:** blocks start at line base+2. They come in segments, one per representative, in JSON `reps` order, of length `orbit_size`.
  - (4,4) segment starts are 47592 + the cumulative sums of [2592, 10368, 20736, 13824, 10368, 5184, 5184, 1728, 2592, 2592, 1296, 432, 864, 432]. The last line is 125783.
  - (2⁴)⁴ segments: 169792 / 180160 / 211264 / 232000, ending at line 234591.
  - Within a segment the order is CPython set order. Each clause is all-negative, has strictly increasing variables, and has exactly 2h+e literals.
- **Plan:**
  1. Enumerate profiles independently and compare with `lte.profiles` and the JSON.
  2. Compare the base clauses line by line with the pinned CNF.
  3. Stream the block lines, check their format, and cut them into segments.
  4. For each representative, enumerate its orbit by breadth-first search over generators and require the segment to equal that orbit as a set, with no duplicates.
     - Generators: adjacent coordinate swaps (i,i+1) where `prof[i]==prof[i+1]`, and adjacent value swaps (a,a+1) in V_i where d_i[a]==d_i[a+1]. Both are contiguous in the canonical form, so they generate H.
     - Cost is about |orbit| × (≤23 generators) × 16. Memory is in the tens of MB; G is never built.
  5. Check the representatives and all orbit images against an independently written predicate covering F1–F4 and |N|. This also tests that H preserves the predicate.
  6. Check |H| against the formula and against `group_order`.
  7. Optional byte identity: run under Python 3.13 and iterate the original G order lazily (`for pi in coord_perms: for vs in product(*vperms)`) into a set. It should reproduce the same order and SHA [INFERENCE].
  8. Optional independent cross-check: a backtracking count of all base solutions per profile, which must equal 144 / 78192 / 21600 / 16 / 64800, and 0 for the other profiles.
  9. For the parent's DRAT re-check: original clause IDs follow file order (base, then blocks). Dropping deletions is sound.

## Pins beyond the snapshot
- **None** are needed for my slice's regeneration (base CNFs, orbit search, segment comparison).
- **Not pinned (version string only):**
  - the Python 3.13.9 engine interpreter, needed only for byte-identical block order;
  - the CaDiCaL 3.0.1 binary, needed only to regenerate representatives or LRAT proofs.
- **Referenced but absent:**
  - the `code/lratcheck` binary (b4e14cd9…3470);
  - `moduli_cert_tests.py`/`.json` and `lrat_soundness_tests.py`/`.json`;
  - the contract JSON and the README/LEMMAS files that docstrings cite;
  - the `explore/engine_control/` and `explore/large_t/` files.

  None of these is load-bearing for coverage, as long as the parent uses its own drat-trim instead of the C checker.

## Files
- `review/SUPPORT_LOWER46.r1.md:101-114` (case table), `:121-147` (procedure), `:171-172` and `:185-213` (results)
- `code/large_t_gen.py:41-85` (encoding), `:190-263` (enumeration loop)
- `code/large_t_e0.py:34-58` (profiles), `:61-84` (normal form and `eqk`), `:135-170` (group, apply, write)
- `code/ame_e0_cnf.py:22-23` (PAIRS, RESHAPINGS), `:48-71` (Sinz encoder)
- `code/lower46_receipt.py:54-80` (receipt loop)
- `evidence/large_t_gen_t*_e*.json`, `evidence/lower46_receipt.json`, `parent-pin-receipt.json` (56 files, 18 pairs)

## How the pieces connect
For each case, `run` loops over profiles. For each profile it builds a `SmallGen`, then repeats: solve, block the whole orbit, until UNSAT; the final CNF and LRAT are written under `explore/large_t_gen/<tag>`. Each representative then gets the checks (a)–(d), and the results go to `evidence/*.json`. The receipt hashes those files and re-checks the LRAT proofs; it does not regenerate anything.
