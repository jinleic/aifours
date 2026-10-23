# Engine v5 for the AME(4,6) support lane: v4 plus review fixes (r1)

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once.
- v4 (`code/large_t_joint4.py`, 42d6e510…26a9), its spec `review/ENGINE_V4.r1.md` (fd1d47f2…8c12) and its outputs
  are unchanged.
- The mathematics is unchanged from v4, and both model reviews accepted it:
  - Codex: `review/ame46-v4-codex-review-v1.note.md`;
  - Claude: `review/ame46-v4-claude-review-v1.note.md`.
  - Accepted: Lemma 19 (officer placement), J (linking), Lemma 20 (doubled triangles, e = 0) and the
    realizable-support lex argument.
- v5 changes only the record, the guards and the code-level binding assertions.

## 1. Files
- **v5:** `code/large_t_joint5.py`, a new file, SHA-256 `e57067c247d3e5c6ca8e7f28035a6d9ec45b1a77238fe8ccd5046eff7f0033f8`.
- **Imports:** as v4 (`review/ENGINE_V4.r1.md` §1).
- **Schema:** the final-CNF order is exactly `review/V4_PROOF_SCHEMA.r1.md`
  (f558e75b6d7f87ea5db3f8025be8475694715d1f8e2f94f88673094936e0b986). v5 adds assertions only, no clauses.
- **Controls:** `code/guard_smoke5.py` (002967ef1538ee0edc2068a34b5c9b0a2530f2ceb565c698f34c54d86943f589) →
  `evidence/guard_smoke5.json` (1d9c3cb07ff99cbbd3365beb94f04c6f4042c232a7e1893206cd89324c5ee4a0); stdout
  `explore/large_t_joint5_guard_smoke5.stdout.txt` (f4aad77cdf7e640af938ce0faeb2656e28e302b30b2a1bc6e14f7d2d029fa0e0).

## 2. Naming (Claude MINOR-1)
- Base clause families: B1 (two-sided hole indicators and the line rule "0 or ≥ 2 points"), B2 (hole counts),
  B3 (|N| = 2h + e) and B4 (overlap). These are the F1–F4 of `review/SUPPORT_LOWER46.r2.md` §3 step 2.
- Officer constraints: C1–C3 of Lemma 19.
- Controls: K1–K7.
- Lex chain variables: q_k.

## 3. Blocking, T-independence and the EXCLUDED rule (Claude MAJOR-1)
- **(i)** Every base model has Σ n_x = 2h + e. B3 (`large_t_gen.py` line 65) is an EQK over all point variables
  with right-hand side 2h + e, for every e. So for a recorded Y with |Y| = 2h + e, a base model falsifies the
  all-negative blocker ∨_{x∈Y} ¬n_x if and only if its point assignment equals Y. This holds across all officer and
  auxiliary assignments.
- **(ii)** Every line meeting Y holds no officer (O1, and the J linking). The component, moduli and phase systems of Y
  are therefore those of every AME state with non-classical part Y, whatever its officers. A rejection of Y is
  independent of T, and blocking on point variables alone is valid in the joint model.
- **(iii)** A case is EXCLUDED only if all of the following hold:
  - every profile is EMPTY, EXCLUDED-BY-LEMMA (Lemma 17) or ENUMERATED;
  - every recorded Y has an exact rejection (components, moduli certificate, or phase certificate);
  - there is no UNKNOWN and no candidate;
  - in proof mode, every final UNSAT stream is verified.
  A candidate, or a failed reconstruction, never produces a rejection.

## 4. Code-level bindings asserted in `build()` (Claude MAJOR-2, MINOR-3, MINOR-6)
A failed assertion makes the profile UNKNOWN. It never excludes.
- **(a)** profile_officer_cnf's V and d (top |p_i| values; the k-th smallest gets p_i[k]) equal SmallGen's V and d.
- **(b)** Hole indicators are two-sided: for every line (i, j, a, b) of V_i × V_j, the clauses (¬hl ∨ points) and
  (¬point ∨ hl) for each point are present in the base.
- **(c)** Variable ranges:
  - every base literal is ≤ nv0;
  - the officer CNF has every literal ≤ F.nv, and its shifted copy lies in (nv0, nv0 + F.nv];
  - the joint variable count is nv0 + F.nv;
  - the base block of the joint CNF is identical to the stand-alone base;
  - the linking clauses equal the written schema (¬hl ∨ ¬o for each o, then hl ∨ Λ), in order;
  - every lex clause uses only point variables or fresh variables above the pre-lex count.
- **(d)** W is gated in code: `--triangles` with e ≠ 0 raises. The W clause count must equal 2·Π_k |V_k|(|V_k| − 1),
  with no duplicates. Every W clause is checked for shape: six distinct points in three doubled pairs along one
  coordinate, with the three z-pairs agreeing in three distinct coordinates.
  - This assertion rejects the void 15:13 generator, which emitted 466,560 clauses (K7).
- **MINOR-6:** every profile part sums to h, and 0 ≤ |V_k| − d_{j,a} ≤ |V_k| for all j, a and k ≠ j.

## 5. Record clarifications
- **Witness, for completeness (Claude MINOR-2).** For a realizable (N, T), the witness assignment consists of:
  - N* = g(N) on the point variables;
  - g(T) on the officer variables;
  - the base auxiliaries of g·ψ, including hl = [line meets N*];
  - the officer-CNF auxiliaries, i.e. the C3 indicators v = OR of their line and the sequential-counter partial sums;
  - the lex chains q_k = "the prefixes agree up to position k".
- **W orientation (Claude MINOR-3).**
  - c1 < c2 < c3 are the coordinates other than i.
  - The vertices are named so that the c1-edge is z1z2 and the c3-edge is z1z3. Hence z2z3 is the c2-edge, and the
    labels are unique.
  - Degenerate triangles, where an edge agrees in two coordinates, are omitted. At e = 0 the base's two-per-line rule
    already excludes them.
  - Odd cycles of length ≥ 5 are not encoded.
  - The count is 2·Π_k |V_k|(|V_k| − 1), asserted at build time. The parent bound it independently: 108,000 for
    (2,6,6,6) and 1,620,000 for 6⁴.
- **Lex indicator order.** The order is the shared point order (`itertools.product` over the normal-form V_i), with
  false < true. At k = 1 one substitutes q0 = true and drops the tautological clause.
- **Phase flags (Codex m1).** `phase_complex_consistent`, `theta_verified` and `phase_obstruction_verified` are stored
  as returned. Their scope is the closed 2×2 components; for e > 0 that is a necessary condition only.
- **Candidate semantics (Claude MINOR-5; Codex note).**
  - Reconstruction applies only at e = 0.
  - Equal moduli |6ψ| = 1/√2 on N lose nothing for existence. Any AME state with e = 0 has phases solving the block
    system (L42-10 holds for arbitrary amplitudes), and the equal-moduli tensor with those phases and the same T is
    then AME. This is an existence construction. It does not claim that every e = 0 AME state has equal moduli.
  - A candidate whose exact reconstruction fails signals a defect and stays unresolved. It is never a rejection.
- **UNKNOWN precedence (Codex m2).** A completion status other than 10 or 20 in exploration, or a final proof not
  verified by both worker checkers, makes the profile UNKNOWN. UNKNOWN takes precedence over candidates and
  exclusions; candidates are still listed in `report["candidates"]`.
- **Proof mode requires `--joint` (Codex M1).** There is no uncertified completion fallback. Without `--joint`,
  exploration runs completion through the guarded wrapper, records the completion CNF's SHA-256, and never treats
  the result as a certificate.

## 6. Controls (K1–K7, run 15:55:38–15:56:26)

| control | observed | expected |
|---|---|---|
| K1 | Pandya's state, base + J + W with all v5 assertions (1,620,000 W clauses): SAT with N fixed; SAT with N and T fixed | SAT, SAT |
| K2 | Pandya's N with one point moved: UNSAT | UNSAT |
| K3 | doubled triangles in Pandya's N: 0 | 0 |
| K4 | profile {6,6}{2⁶}³ at t = 24; an N of base + J with a doubled triangle (found at the first try): SAT without W, UNSAT with W | SAT, UNSAT |
| K5 | the stored phase-consistent, completion-UNSAT N of profile 0: SAT with the base only, UNSAT with J | SAT, UNSAT |
| K6 | RSS cap 20 MiB: UNKNOWN; free floor 10^15: UNKNOWN; `--proof` without `--joint`: UNKNOWN ("proof mode requires --joint"); `--profiles 0`: PARTIAL; (30,0) agreement: EXCLUDED-EXPLORATION | as stated |
| K7 | the void 15:13 generator is rejected by the count assertion (466,560 ≠ 108,000); `--triangles` with e = 2 raises | rejected, raises |

all_required_true = true. Controls are not proof. K4 and K5 show that W and J each remove an N the other families
allow. K1 and K3 show that a genuine state satisfies them.

## 7. Disposition table

| review item | disposition |
|---|---|
| Codex M1 (uncertified completion fallback) | fixed: `--proof` requires `--joint` (K6) |
| Codex m1 (phase flags) | fixed: flags stored as returned, scope stated |
| Codex m2 (UNKNOWN reporting) | fixed: UNKNOWN precedence, completion status and final-proof failure handled |
| Claude MAJOR-1 (blocking) | fixed: §3 (i)–(iii) |
| Claude MAJOR-2 (bindings a–d) | fixed: asserted in code (§4); K7 shows the W assertion rejects the void generator |
| Claude MINOR-1 (names) | fixed: B1–B4, C1–C3, K1–K7 |
| Claude MINOR-2 (witness) | fixed: §5 |
| Claude MINOR-3 (encoding text and count) | fixed: §4 (d) and §5 |
| Claude MINOR-4 (discriminating controls) | added: K4 (W) and K5 (J) |
| Claude MINOR-5 (candidate semantics) | fixed: §5 |
| Claude MINOR-6 (builder guards) | fixed: §4 |
| NITs (v3 duplicate bullet; "composition of"; "non-classical part g(N)"; z3 scan) | noted. The v3 and v4 specs stay frozen. The z3 scan is efficiency only and unchanged, so the schema is identical |

## 8. Proof-mode resource estimate for s ≥ 49 (requested go)

All measured data come from exploration runs; no proof run has been made.
- **(24,0)**, v4 exploration (`evidence/large_t_joint4_t24_e0_explore.json`,
  b2887b51312c38b3907fcb0becd0eb9e1f65af1ba5fe9eb139852e66ded2ba1f), 15:33:22–15:57:41:
  - 158 profiles: 153 enumerated, 5 excluded by Lemma 17;
  - 42 solutions, all in profile 0 and all phase-excluded (23 three-term, 17 seven-term, 2 nine-term certificates);
  - 1453 s in total, profile 0 412 s, every other profile ≤ 21 s;
  - sampled peak RSS 3,565 MiB, with the engine and the solver child together;
  - no candidate, no trip.
  - Proof-mode estimate:
    - one extra solve with LRAT and two checker runs per enumerated profile, plus the v5 build-time assertions;
    - about 1.5 h wall, within the 3 h chunk limit;
    - gzip streams estimated at 0.2–0.5 GB. This is an extrapolation; the budget guard stops the run as UNKNOWN if
      exceeded;
    - the RSS cap stays 6 GiB. The Python checker on the largest CNFs (product space 1296, 1.62M W clauses) is the
      memory risk, and a trip gives UNKNOWN.
- **(26,2), (27,3), (28,4), (30,6)**, v3 exploration (EXCLUDED-EXPLORATION): 30 s, 5 s, 50 s and under 1 s, with
  peak RSS ≤ 607 MiB.
  - Proof mode with v5 `--joint` (no W for e > 0): estimated ≤ 15 min in total and ≤ 50 MB of streams.
- **Lane disk:** du 9,354,076,160 B at 15:58, which leaves 1,114,906,624 B under 10 GiB − 256 MiB. v5 caps each run at
  512 MiB. Filesystem free: 18.6e9 B, above the 12e9 floor.
- **Order:** (30,6), (28,4), (27,3), (26,2), then (24,0). Each is one chunk under `run_chunk` with a 3 h limit, at most
  2 busy processes, and the free-floor watchdog.
