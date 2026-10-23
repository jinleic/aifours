# Erratum 1 to `review/ENGINE_V2_GUARD.r1.md` (and annotations to frozen code docstrings)

Lane `physics/evidence/six-lane-20261016/ame46-support/`. Host clock PDT, 2026-10-17. Written once.
- The frozen files keep their bytes: `review/ENGINE_V2_GUARD.r1.md` (d5733a7366c6d7fb3c197829ed6232abcb74c27f7250fa556cc59f34a3a273fd),
  `code/large_t_lex.py` (cde05b00c0eb5ab6ce8724a14723a13522ee0106add714f001af7c2b7ae012b8) and `review/ENGINE_V3.r1.md`
  (fd7c7447d7140d934d3311a27e2e368dd1167334cf370bf7e8b3ddac1bd74449).
- This erratum supersedes the passages quoted below.
- Sources:
  - the parent orchestrator's reading of LOWER48 r1;
  - the Codex review `review/ame46-lower48-codex-review-v1.note.md` (one MAJOR, one MINOR);
  - the Claude review `review/ame46-lower48-claude-review-v1.note.md`. Its MAJOR is the same as E1, and its
    properties P1–P5 are used in `review/SUPPORT_LOWER48.r2.md` §3. It adds no other guard item.

## E1 (MAJOR): syntactic CNF symmetry
**Superseded text.** `ENGINE_V2_GUARD.r1.md` §3, "Why the assumption holds" (lines 62–65), says: "Each generator is
a symmetry of the CNF up to renaming of auxiliary variables. … This is the same invariance the frozen engine's orbit
blocking used." The completeness claim's hypothesis "assume every g ∈ H maps Sol to Sol" is justified by that
sentence. The engine-v2 docstring (`code/large_t_lex.py` lines 10–14) makes the same appeal.

**Why it is false.** The sequential-counter (Sinz) auxiliaries of `ame_e0_cnf.CNF.at_most_k` depend on the order of
the input literals, so a permutation of point variables need not lift to a clause-set automorphism. Counterexample
(Codex): in the (30,4) base CNF of profile {2,2,2}⁴, generator 3 swaps the points 3333 and 4333 (variables 1 and 28),
whose positive/negative clause-occurrence counts are (103, 61) and (168, 77). No auxiliary renaming can reconcile
them.

**Replacement (no change to search, certificates or results).** Completeness is argued from realizable supports:
1. Every H-image of a realizable non-classical support is realizable, since H acts by local value permutations
   inside d-classes and by permutations of equal-part parties. It has the same (t, e) and normal-form profile, so it
   extends to base-CNF auxiliaries by encoding necessity.
2. The lexicographically least H-image N* satisfies every generator lex-leader constraint, with the prefix-equality
   auxiliaries.
3. A certified final UNSAT forces N* to be a listed (blocked) support: the cardinality is fixed, so each blocking
   clause excludes exactly its listed support.
4. Every listed support fails an exact necessary check, contradicting realizability.
The argument is written out in `review/SUPPORT_LOWER48.r2.md` §3 and `review/ENGINE_V3.r1.md` §4. Neither syntactic
symmetry nor H-invariance of the CNF's projected solutions or of the checks is needed.

The frozen engine's orbit blocking (LOWER46) needs only the same realizability invariance:
- a realizable support is blocked, hence equals h(R) for a listed representative R;
- then R = h⁻¹(N) is realizable and is excluded by its checks.
The Codex LOWER46 review accepted exactly this, so LOWER46 is unaffected.

## E2 (MINOR): checker independence
**Superseded text.**
- `ENGINE_V2_GUARD.r1.md` line 22 (table row): "independent Python LRAT checker";
- `code/large_t_lex.py` docstring line 16: "The two independent checkers".

**Correction.** The C checker `code/lratcheck` and the Python checker `code/lratcheck_py.py` are separately
implemented by the same author, with the same RUP semantics. Their agreement is reproducibility, not independent
validation. The independent route is the parent's addition-only RUP replay with drat-trim (-I -U) against regenerated
or pinned CNFs.

## E3 (wording): "independent verifier" in the v3 spec
`review/ENGINE_V3.r1.md` line 14 calls `code/phase_cert.py` "an independent verifier". That means only that its
verifier does not call `phase_check.py`. It was written by the same author, and independent checking of phase
certificates is the parent's.

## E4 (cosmetic): duplicated bullet in the v3 spec
`review/ENGINE_V3.r1.md` §4, lines 75–76, states the same bullet twice. No content differs.

## E5 (label): officer-CNF pre-filter in v3 reports
Engine v3 (`code/large_t_lex3.py`, 139681a2…37e0) writes the label `"Lemma 18 (officer placement CNF UNSAT)"` for
profiles excluded by the officer-placement CNF. In the frozen spec `review/ENGINE_V3.r1.md` §3, that relaxation is
**Lemma 19**. Lemma 18 of `review/SUPPORT_LOWER48.r1.md` is the parent's binary-code lemma. Read the report label as
Lemma 19. Profiles excluded by Lemma 17 are labelled `"Lemma 17 (officer counting)"`, which is correct.
