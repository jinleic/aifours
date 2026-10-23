# Ame46RepAudit report (verbatim)

Recorded 2026-10-17 13:33:21 PDT. Agent output is untrusted until parent-bound.

I found no FATAL or soundness defect in the exclusion routes. All 28 representatives are excluded by sound routes: 24 by phase obstructions and 4 by classical completion. I hand-derived and checked every phase certificate and found short written proofs for all 4 completion cases. **s ≥ 46 is not accepted:** the 18 LRAT proofs still need the parent's independent recheck, and the N-only cover is another slice's job.

Everything here is static reading plus hand arithmetic. I ran no solvers, checkers or code. Worker logs and receipts are reported as claims only.

## Summary
- **Components, closure and moduli are not used.** All 28 report entries show `components_ok:true`, `components_reason:"ok"`, `moduli_certificate:null` and `moduli_excluded:false`. That is expected: with e = 0 every hole line has exactly 2 points, so m ≡ 1/2 is feasible and moduli could not exclude anything anyway.
- **Phase route (24 reps).** The code is sound:
  - Each 4-tuple point gets one phase variable φ_x, shared across all three reshapings (`phase_check.py:48-62`).
  - Signs follow the Lemma 10 diagonal pattern (+r1c1, −r1c2, −r2c1, +r2c2, at `:61`). The right-hand side π is orientation-free.
  - The kernel vector is re-checked exactly: nᵀA = 0 and odd sum (`:108-117`).
  - Each certificate below is a ±1 combination of 3 forms (5 forms for {4,4} r4 and r5) that sums to the zero form. The weight sum is odd, so 0 ≡ π (mod 2π), a contradiction.
- **Completion route (4 reps).** The encoding is a sound relaxation (`large_t_e0.py:194-216`):
  - "Allowed" points are those on no hole line, so officers automatically avoid N and every hole line.
  - Every non-hole line gets exactly one officer: an at-least-one clause plus a Sinz at-most-one encoding (`ame_e0_cnf.py:48-70`).
  - t is not encoded. It is implied (h hole lines per pair gives |T| = 36 − h) and is not needed for soundness.
  - I recomputed the allowed-point counts by hand: 606, 464, 464, 472. The CNF headers match the closed form nv = 7A − 6t and clauses = 18A − 18t.

## Findings
**FATAL: none.**

**MAJOR (evidence binding, not soundness)**
- **M1. The phase certificates are never stored.** The engine records only the booleans `phase_complex_consistent:false` and `phase_obstruction_verified:true` (`large_t_gen.py:238-242`). The receipt only echoes `r["excluded"]` (`lower46_receipt.py:73`). Yet LOWER46:160-162 and :211-212 claim a "verified integer certificate". The 24 explicit certificates below close this gap; the parent should machine-check them.

**MINOR (ancillary checker and doc issues)**
- m1. `lower46_receipt.py:68` uses stale keys (`moduli_ok`, `moduli_lp_max_eps`), so a moduli exclusion would be mislabelled. No effect here, since none occurred.
- m2. The docstring at `large_t_gen.py:18` still says moduli uses a sympy exact LP. The sympy `moduli_lp` is still defined at `:112` but never called, while LOWER46:257 says "now removed".
- m3. The comment at `lratcheck.c:85` says a tautological lemma is accepted only if it has no hints. In fact `:90` skips its hints regardless. This is sound but the comment is wrong.
- m4. `lratcheck_py.py:99` prints `s NOT VERIFIED (no empty clause)` and still exits 0. Callers rely on a substring test, which is fragile.
- m5. The Python checker silently overwrites an id that is still alive (`:93`); the C checker rejects that (`lratcheck.c:77`). Both are sound.
- m6. The "two independently written checkers" claim (LOWER46:21) is weak: same author, same semantics. Their test evidence (`lrat_soundness_tests.*`, C binary `b4e14cd9…`) and `moduli_cert_tests.*` are cited at LOWER46:177-181 and :238-254 but are neither in the snapshot nor in the receipt.
- m7. The e = 0 cross-check shares `phase_check`, `completion_cnf`, `solve`, `lrat_check` and `group()` with the main engine, and its proofs (`explore/large_t/`) are not pinned. Its agreement is therefore neither independent nor bound. Its orbit-size multisets do match: {4,4} 78192, {4,2,2} 21600, {3,3,2}⁴ 16, {2,2,2,2}⁴ 64800, t30 108+36.
- m8. The receipt reports `"python":"3.9.6"`, while the engine runs used 3.13.9. No CaDiCaL binary hash is recorded, only "3.0.1". No positive control for the phase checker was recorded (for example, Pandya's support should come out consistent).

## Phase certificates (all 24)
Notation: `[k: a b c d]` means φa − φb − φc + φd. It is the form of the 2×2 component of reshaping k (0 = 12|34, 1 = 13|24, 2 = 14|23), with corners (r1c1, r1c2, r2c1, r2c2), exactly as `block_equations:61` emits it. For every block below I checked that it is a genuine component: each of its rows and columns holds exactly two points of N.

| case | rep (orbit) | certificate (sums to the zero form; weight sum odd) |
|---|---|---|
| (30,0) {3,3} | r0 (108) | +[0: 4335 4354 5335 5354] +[1: 4354 4555 5354 5555] −[2: 4335 4555 5335 5555] |
| (28,0) {4,4} | r0 (2592) | −[0: 4243 4245 5543 5545] +[1: 4533 4535 5543 5545] +[2: 4243 4533 4245 4535] |
| | r1 (10368) | +[0: 4222 4234 5222 5234] +[1: 4234 4432 5234 5432] −[2: 4222 4432 5222 5432] |
| | r2 (20736) | +[0: 4222 4234 5222 5234] −[1: 4222 4324 5222 5324] +[2: 4234 4324 5234 5324] |
| | r3 (13824) | +[0: 4543 4555 5543 5555] +[1: 4345 4543 5345 5543] −[2: 4345 4555 5345 5555] |
| | r4 (10368) | +[0: 4434 4455 5434 5455] +[1: 4455 4552 5455 5552] −[2: 4222 4552 5222 5552] +[1: 4222 4324 5222 5324] +[2: 4324 4434 5324 5434] (weight sum 3) |
| | r5 (5184) | +[0: 4435 4454 5435 5454] −[2: 4324 4454 5324 5454] −[1: 4222 4324 5222 5324] +[0: 4222 4233 5222 5233] +[1: 4233 4435 5233 5435] (weight sum 1) |
| | r8 (2592) | +[1: 4324 4423 4334 4433] +[2: 4423 4433 5424 5434] −[0: 4324 4334 5424 5434] |
| | r9 (2592) | +[0: 4225 4254 4325 4354] +[2: 4254 4354 5255 5355] −[1: 4225 4325 5255 5355] |
| | r10 (1296) | +[0: 4225 4245 5525 5545] −[2: 4524 4544 5525 5545] −[1: 4225 4524 4245 4544] |
| | r11 (432) | +[0: 4224 4243 5224 5243] +[1: 4243 4444 5243 5444] −[2: 4224 4444 5224 5444] |
| | r12 (864) | +[0: 4344 4352 5344 5352] +[2: 4352 4442 5352 5442] −[1: 4344 4442 5344 5442] |
| | r13 (432) | +[0: 4222 4243 5322 5343] +[1: 4243 4342 5223 5322] −[2: 4222 4342 5223 5343] |
| (28,0) {4,2,2} | r0 (2592) | +[0: 3222 3243 3322 3343] +[2: 3243 3343 4242 4342] −[1: 3222 3322 4242 4342] |
| | r1 (5184) | +[0: 3232 3234 5432 5434] −[1: 3232 3234 5252 5254] −[2: 5252 5432 5254 5434] |
| | r2 (1728) | +[0: 3345 3353 4345 4353] +[2: 3353 3443 4353 4443] −[1: 3345 3443 4345 4443] |
| | r3 (5184) | +[0: 3233 3235 5533 5535] −[1: 3233 3235 5253 5255] −[2: 5253 5533 5255 5535] |
| | r4 (5184) | +[0: 3242 3252 5342 5352] −[2: 3242 3252 5245 5255] −[1: 5245 5342 5255 5352] |
| | r5 (864) | +[0: 3225 3244 5225 5244] +[2: 3244 3424 5244 5424] −[1: 3225 3424 5225 5424] |
| | r6 (864) | +[0: 3235 3244 5335 5344] −[1: 3235 3334 5245 5344] +[2: 3244 3334 5245 5335] |
| (28,0) {2,2,2,2}⁴ | r0 (10368) | +[0: 2454 2455 3554 3555] −[1: 2544 2545 3554 3555] −[2: 2454 2544 2455 2545] |
| | r1 (31104) | +[0: 2324 2342 2424 2442] +[2: 2342 2442 5344 5444] −[1: 2324 2424 5344 5444] |
| | r2 (20736) | +[0: 4244 4255 5244 5255] +[2: 4255 4445 5255 5445] −[1: 4244 4445 5244 5445] |
| | r3 (2592) | +[0: 2222 2233 3322 3333] −[1: 2222 2323 3232 3333] +[2: 2233 2323 3232 3322] |

As a side check, I confirmed the engine's "consistent" verdicts for the reps it sent to completion. For {4,4} r6 and r7 and t30 r1, N is two copies of a set M (first coordinate 4 or 5), and the M-graph whose edges each force a phase difference of π is bipartite. For t30 r1 it is K₃,₃.

**To verify independently:**
- Rebuild components from the report's N strings with `RESHAPINGS = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]` (`phase_check.py:18`).
- Check that every occupied line holds exactly 2 points and that each pair has h occupied lines.
- Check each combination above.
- Do not compare against the engine's `"obstruction"` equation indices: they depend on set iteration order.

## Completion route: regeneration data and written proofs
**Regeneration.** Call `completion_cnf(N, path)` with N as int 4-tuples taken from the report strings.
- Pair order is `PAIRS = [(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]` (`ame_e0_cnf.py:22`).
- Allowed points are enumerated in `product(range(6), repeat=4)` order, with variables 1..A.
- For each non-hole line: one at-least-one clause, then the Sinz at-most-one, whose auxiliary variables are allocated sequentially.
- Header is `p cnf nv nc`; each clause line is the literals followed by `" 0"`.
- Compare the result's SHA-256 with the pinned file.

| rep | A | CNF header | CNF SHA | LRAT SHA | first id … empty-clause id / deletions |
|---|---|---|---|---|---|
| (30,0) {3,3} r1 | 606 | 4062 10368 | b95b02c1…bc53d | e2e9d6cc…72497 | 10369…12721 / 266 |
| (28,0) {4,4} r6 | 464 | 3080 7848 | 9eedfca9…31d0c | 22cf0dc2…00b24 | 7849…7984 / 7 |
| (28,0) {4,4} r7 | 464 | 3080 7848 | 91a33b87…85886 | 5b472911…f59af | 7849…8181 / 10 |
| (28,0) {3,3,2}⁴ r0 | 472 | 3136 7992 | 9e56c70c…7ff9a | 720c15db…8ce7 | 7993…8222 / 18 |

All four headers agree with the closed form, which rules out any unit or empty clause in these CNFs.

**Written proofs.** These are my own derivations and need parent re-derivation. Each excludes the whole profile for every e and every N, so these 4 LRATs are not load-bearing.
- **Counting identity.** For each officer y, let k(y) be the number of coordinates i with y_i ∈ V_i, and let σ_m = Σ_y C(k(y), m). Then:
  - σ₀ = t;
  - σ₁ = 6Σ|V_i| − 4h;
  - σ₂ = e₂(|V|) − 6h, because each pair has h hole lines, all inside V_i×V_j (L42-8(c)), and every other line in V_i×V_j holds exactly one officer;
  - #{y : k(y) = 0} ≤ σ₀ − σ₁ + σ₂ (Bonferroni), and it cannot be negative.
- **(30,·) {3,3}{2,2,2}³:** σ₀ − σ₁ + σ₂ = 30 − 42 + 9 = −3. Contradiction.
- **(28,·) {3,3,2}⁴:** 28 − 40 + 6 = −6. Contradiction.
- **(28,·) {4,4}{2,2,2,2}³:**
  - D_j^{(1,a)} = V_j by Lemma 12, since d_{1,a} = 4 = |V_j|.
  - So the four officers with x₁ ∈ {4,5} lie in {4,5} × {0,1}³ and pairwise agree in at most one coordinate (L42-3).
  - That is 4 words of a binary length-4 code with minimum distance 3, which is impossible (the maximum is 2).
- **Bonus for the cover slice [INFERENCE]:** the same identity gives −3 for (29,·) {3,2,2}⁴ and for (28,·) {3,3,2}³{2,2,2,2}.

## LRAT checker semantics
Both checkers implement RUP-only LRAT soundly. For each lemma they negate it, then process hints in order:
- a satisfied hint is skipped and counted (C `:96`; Python only with `--allow-satisfied`, otherwise an error);
- a unit hint assigns its literal;
- a fully falsified hint, an actual conflict, is the only way to succeed (C `:97`, Python `:84`);
- a hint with two or more unassigned literals is rejected;
- running out of hints without a conflict is rejected (C `:101`);
- negative (RAT) hints and unknown or deleted ids are rejected;
- the empty clause must be derived (C `:109`).

Tautological lemmas are accepted, which is sound. The C checker reads exactly the header's clause count and ignores any extra clauses, which can only weaken the formula. Both reject the memory lesson's negatives (`p cnf 1 1 / 1 0` with proof `2 0 0` or `2 0 1 0`), according to my trace of the code. This is semantics only; it does not accept any proof.

## LRAT syntax and the 18 pairs
- **Syntax (observed):** additions are `<id> <lits> 0 <hints> 0`. Deletions are `<id> d <ids> 0`, where `<id>` repeats the last added id (e.g. `7863 d 7861 0`). The last line is the empty clause, e.g. `7984 0 7960 7968 1302 0`. Ids are contiguous, starting at clause count + 1. A grep of the r7 completion found no negative hints.
- **14 final enumerations:**
  - (30,0) {3,3} 29549ea0/11892b69 and {2,2,2}⁴ 123d9d21/268b0212
  - (30,2) 6cc12de9/7a7eabc9 and fdb3bf5a/23be0cb6
  - (30,3) 7c7fbf83/a32475e9 and 9c25a806/b68bdd4b
  - (29,2) 5aab5022/1178c91c
  - (28,0) {4,4} 52c45916/3b4ec9d7; {4,2,2} a54f837e/11abed0b; {3,3,2}⁴ ed5f4917/7d824319; {3,3,2}³{2⁴} 9a901d04/18872106; {3,3,2}²{2⁴}² 27faa3e4/44974f46
  - (28,0) {3,3,2}{2⁴}³ d5ac33b1/7b3c3807 and {2⁴}⁴ 2b874174/18a0d0a9 each carry 3 satisfied hints and fail Python strict mode.
- **4 completions:** the four in the table above. 14 + 4 = 18, all accounted for.
- **Count cross-check:** (30,0) {3,3} has 10042 clauses = 9898 (the e = 2/3 CNF of the same profile) + 144 = 108 + 36 blocking clauses.

## Safe independent recheck recipe
1. Work in a fresh, no-overwrite directory. Check SHAs against `parent-pin-receipt.json`. Run one job at a time with `nice`, an RSS watchdog and a wall-clock cap.
2. Parse each CNF as a stream: exact clause count and variable bounds.
3. Parse each LRAT as a stream:
   - every line is an addition or a deletion;
   - addition ids are strictly increasing from clause count + 1;
   - hints are positive and smaller than the current id;
   - there is one empty clause, on the last line;
   - recount additions and deletions against the receipt.
4. Convert to DRAT: for each addition, write its literals followed by `0`. Drop all deletions (sound). Cut at the first empty clause.
5. Run a pinned drat-trim on `cnf` + `drat`. Strip `\r` and whitespace, then require an exact `s VERIFIED` line. Set the timeout explicitly; I believe the default is 20000 s, but have not checked.
6. Negative controls:
   - a satisfiable CNF with an empty-clause DRAT must fail;
   - a core clause removed from a small completion CNF must fail.
   - Do not use the upstream `lrat-check`.
7. Optionally re-solve with a different solver and check its fresh DRAT [INFERENCE: `cake_lpr` is another option].
8. Do not re-run the worker's group enumeration for {2,2,2,2}⁴ (7,962,624 elements) without a memory cap.

## Missing or unbound evidence
- The 24 phase certificates (supplied above).
- No recorded check that each completion CNF equals `completion_cnf(N)`; only the SHA and file name tie them together. My counts and headers are consistent.
- The C binary, `lrat_soundness_tests.*`, `moduli_cert_tests.*`, LOG.md and SHA256SUMS.txt.
- The e = 0 cross-check proofs, the CaDiCaL binary hash, and a phase positive control.

## Files
- `code/phase_check.py:18,21-62,65-117`: components, Lemma 10 forms, kernel and odd-sum check.
- `code/large_t_gen.py:88-110,164-187,226-260`: component check, moduli, route order and the exclusion predicate.
- `code/large_t_e0.py:173-216`: `solve` (`cadical -q --lrat --binary=false`), `lrat_check` and `completion_cnf`.
- `code/lratcheck.c:55-111`, `code/lratcheck_py.py:13-99`, `code/lower46_receipt.py:67-88`.
- `evidence/large_t_gen_t{30,28}_e0.json` (representatives' N); `parent-pin-receipt.json` (SHAs, counts).
- `review/SUPPORT_LOWER46.r1.md:148-181,211-257`.

## Architecture
For each representative, the engine applies the checks in order: components, then moduli, then 2×2 phases, then completion. The first one that fails excludes it, and the exclusion carries over to its whole orbit by the Lemma 11 symmetries. The receipt then hashes the files and re-runs both checkers on the 18 pairs. The parent pin copies those 56 files.
