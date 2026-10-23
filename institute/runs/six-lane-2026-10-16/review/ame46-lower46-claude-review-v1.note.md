VERDICT: ACCEPT-WITH-FIXES

This acceptance is conditional. The Theorem is not established until bindings P1–P4 below pass, using code independent of the worker's engine, and r2 records them (P5). No written step was found mathematically invalid.

## FATAL

None found. I checked Lemmas 12–16, the case table (L46 LF99–114) and the bridge design (L46 LF116–169). No step in them lets a true AME(4,6) state be excluded. The only routes by which one could still be excluded are file contents that have not been recorded. M1–M3 cover them.

## MAJOR

**M1. The clause content of the pinned CNFs is never specified (L46 LF118–119, LF131–139, LF163–165, LF171–176).**
- **Nature:** missing verification record, with a possible mathematical consequence.
- **What is sound:** families (i)–(iv) at LF132–138 are each necessary:
  - (i) by L42-2(a) and L42-4;
  - (ii) by L42-8 together with Lemma 12, which puts every D_j^{(i,a)} inside V_j;
  - (iii) by the definition of e;
  - (iv) by L42-5.
- **What is missing:** the text never says that the 14 final CNFs contain only these families plus blocking clauses.
- **Why it matters:** `large_t_gen.py` imports helpers from the e = 0 engine (LF118–119). LF171–172 implies that engine has an optional "phase clauses" family and adds an exactly-two-per-hole-line family (L42-9). Both are valid only when e = 0:
  - Exactly-two is false for e > 0. Combined with |N| = 2h + e > 2h, it makes the CNF trivially UNSAT.
  - Four grid points of N form a block only if its rows and columns hold no other N-point. That is automatic only under exactly-two.
- **Exposure:**
  - 9 of the 14 final CNFs never had a solution: (30,0) {2,2,2}⁴, both (30,2), both (30,3), (29,2), and three (28,0) profiles.
  - (30,2), (30,3) and (29,2) are excluded by nothing else.
  - The only positive control (LF174–176) is at (12,0), which has e = 0. No control exercises an e > 0 encoding.
- **Fix:**
  - r2 lists, for each of the 18 CNFs, the variable map and every clause family together with its lemma.
  - r2 states that no phase, exactly-two or symmetry-breaking family occurs. If one does, r2 proves its soundness for the (t, e) where it occurs.
  - The bindings must establish three things:
    - (a) the header data of each CNF;
    - (b) soundness: every N ⊆ ΠV_i that satisfies (i)–(iv) with |N| = 2h + e extends to a model;
    - (c) no other clause family is present.
  - Add a planted positive control with e > 0: any N satisfying (i)–(iv). It does not need to come from an AME state.
  - Preferred route: regenerate the CNFs independently (different author, no shared module, different cardinality encoding, different solver), then run a RUP check.

**M2. Completeness and orbit transfer rest on blocking clauses that are not recorded (L46 LF140–147, LF166–169, LF189–209).**
- **Nature:** missing record. The logic is valid.
- **Why the logic holds:** under exact cardinality, the clause ∨_{x∈X} ¬n_x with |X| = 2h + e blocks only N = X. So UNSAT of (base ∧ blocks) confines every true N to the blocked sets.
- **What could go wrong silently:** a shorter clause, a mis-indexed variable, or an X that is not an image of an excluded representative would exclude true candidates.
- **Fix (representative-to-orbit binding):**
  - Every non-base clause is all-negative on n-variables and has exactly 2h + e literals.
  - Its point set equals g(N0) for a listed representative N0 and some g ∈ G (as in L42-11). Membership in H is not needed (see m7).
  - The variable map is the same as the base CNF's.
  - The listed representatives are exactly the 28 excluded ones (2 for (30,0), 26 for (28,0)).
  - Sanity check: the number of distinct blocking clauses should equal the orbit sums: 144, 78192, 21600, 16 and 64800 for (30,0){3,3}, {4,4}, {4,2,2}, {3,3,2}⁴ and {2,2,2,2}⁴.

**M3. The phase-certificate record contradicts what is actually relied on (L46 LF19–20, LF160–161, LF191, LF198–199, LF204, LF211–212).**
- **Nature:** missing record, not a mathematical defect.
- **Why the evidence suffices once bound:** a parent-checked ±1 certificate excludes its representative by L42-10. By L42-11(c) the exclusion extends to every G-image. Who found the certificate does not matter.
- **What is wrong:** "certificate-producing", "re-verified" and "verified integer certificate" describe engine artifacts that do not exist. The certificates used were reconstructed by a scout.
- **Fix:**
  - Pin the certificate file, the parent's checker, the command and the output.
  - State the criteria checked:
    - the four points lie in N0;
    - in the stated reshaping, the block's two rows and two columns each contain exactly two N0-points;
    - the + signs sit on one diagonal;
    - the signed sum is the zero form;
    - the number of terms, counted with multiplicity, is odd.
  - Bind each certificate's point set to the exact engine representative, or to a G-image of it.
  - Strike the engine's claims, or label them as unrecorded.

**M4. The stated UNSAT basis is false, and the actual basis is not recorded (L46 LF20–21, LF146, LF165, LF186–187, LF212, LF233–249, LF255–256).**
- **Nature:** false record statement. There is no mathematical consequence, because the parent's addition-only RUP recheck of the 18 CNFs bypasses both worker checkers:
  - A RUP-only check is sound.
  - Ignoring deletions only enlarges the set of clauses available for propagation.
  - The LRAT→DRAT conversion is rechecked from scratch against the pinned CNF, so it cannot introduce unsoundness.
- **What is wrong:**
  - "Two independently written checkers": both have the same author.
  - The satisfied-hint argument at LF240–246 is correct but moot.
  - LF256's "all LRAT checks verified" rests only on the worker checkers.
- **Fix:**
  - Replace LF20–21 and LF236–239 with the parent's recheck:
    - drat-trim source and binary SHA;
    - flags, including whether RAT was disabled;
    - each CNF and proof SHA, matching the receipt;
    - each VERIFIED output.
  - Demote the worker checkers and LF240–249 to non-load-bearing.
  - Delete "independently written".

## MINOR

**m1. Profile completeness is delegated to code (L46 LF121–125).**
- **Nature:** record only. The list in §4 is correct.
- **Written derivation for r2:** parts are ≥ 2 and sum to h. Each partition's largest part is at most the minimum number of parts of the other coordinates, which is at most 4.
  - h = 6: {6} and {4,2} are excluded. A {3,3} coordinate forces the other three to be {2,2,2}. This gives {3,3}{2,2,2}³ and {2,2,2}⁴.
  - h = 7: only {3,2,2} qualifies, giving {3,2,2}⁴.
  - h = 8: {8}, {6,2} and {5,3} are excluded.
    - {4,4} or {4,2,2} forces the other three to be {2,2,2,2}.
    - {3,3,2} forces each of the others to be {3,3,2} or {2,2,2,2}.
    - This gives seven profiles, exactly those at LF198–204.
- **Fix:** insert this derivation.

**m2. Citations and imports (L46 LF10–14, LF85, LF112, LF126–127, LF136).**
- **Nature:** citation only.
- **Corrections:**
  - LF10–14 omit L42 LF42–50 (the reshaping lemma and the product-basis reduction), the corollary at L42 LF202–204 and L42-9.
  - LF85: "a line without an officer meets N" is L42-4, not L42-3.
  - LF112 has no citation. Cite L42 LF202–204.
  - LF126–127: L42 §0 does not cover party permutations. Add one sentence: they permute the six two-party marginals.
  - LF136: |N| = 2h + e follows from the definition of e (L42 LF54) and s = t + |N|, not from L42-7(c).

**m3. Quantifiers (L46 LF26, LF101).**
- **Nature:** presentational.
- **What is missing:** the Theorem does not say "complex", and §2 does not invoke the basis reduction. Nothing in Lemmas 12–16 or §3 assumes real amplitudes or a particular basis.
- **Fix:** cite L42 LF32 for the definition and L42 LF47–50 for the basis reduction.

**m4. The e = 0 cross-check (L46 LF171–172, LF212–213, LF255–256).**
- **Nature:** record. The run carries zero evidential weight:
  - It shares `ame_e0_cnf.py` and `phase_check.py` with the main engine.
  - Its proofs are not among the 18 that were rechecked.
  - "Without phase clauses … agrees" leaves unexplained how the 23 (28,0) representatives that the main engine excluded only by phase obstruction were excluded in that run.
- **Fix:** relabel it as a same-code consistency run and state its exclusion mechanism, or delete it.

**m5. Filters (a) and (b), and stale material (L46 LF150–159, LF177–179, LF233–235, LF257–258).**
- **Nature:** editorial.
- **Status:** both filters are valid necessary conditions, and the Farkas argument at LF155–156 is correct. Neither excluded anything, so neither is part of the proof.
- **Fix:**
  - Say so in §3.
  - Remove the dead sympy/LP code and the stale docstrings, or mark them as never called.
  - Remove stale receipt keys and regenerate the receipt.

**m6. Pin hygiene (L46 LF185, LF220–221, LF238, LF247, LF255–256).**
- **Nature:** provenance only, and not load-bearing once the bindings are independent.
- **Problems:**
  - The interpreter lives in another lane's venv.
  - There is no hash for the interpreter, a lockfile or the CaDiCaL binary.
  - Several SHAs are truncated.
  - Run times are given without dates.
- **Fix:** record:
  - the absolute interpreter path, `sys.version`, and the binary or lockfile SHA;
  - the CaDiCaL binary SHA and build options;
  - full SHAs and dates.

**m7. Orbit transfer (L46 LF141–143, LF166–167).**
- **Nature:** presentational; the argument is valid.
- **Problems:** G is never defined in L46. Invariance of filters (a) and (b) is asserted without proof; they are unused anyway.
- **Fix:** use a state-level argument. If ψ has N(ψ) = g(N0), the corresponding local permutation unitaries and party permutation give an AME state with N = N0. Phase obstruction and completion failure are necessary conditions on N alone. So excluding N0 excludes every G-image, and H-membership becomes irrelevant to M2.

**m8. Lemmas 15 and 16 (L46 LF70, LF96–97).**
- **Nature:** presentational. Both lemmas were checked in full:
  - A1 = A2 = 0, A3 = 12, A4 = 3;
  - Y^{⊗4} P̄ Y^{⊗4} = (−1)^{wt P} P;
  - tr(ρρ̃) = −1/2;
  - ‖ω‖ = 1;
  - the three 4×4 hole blocks are unitary for every e.
- **Fix:**
  - LF70: justify positive semidefiniteness. ρ̄ = Σ λ|v̄⟩⟨v̄|, and Y^{⊗4} is unitary.
  - LF96–97: write out ρ_ab = (2ω)(2ω)†/4 and ρ_cd = ((2ω)†(2ω))ᵀ/4.

## Established scope

- **Written, with Tarry cited:**
  - Lemmas 12, 13, 15 and 16 are correct for every e.
  - Lemma 14 is correct, but only unused filter (a) depends on it.
  - For every complex AME(4,6) state in every product orthonormal basis: t ≤ 30, e ≠ 1, and e = 0 implies t is even.
  - The written-only lower bound remains 42. The case (30,0) is the first that needs computation.
- **Case table:**
  - s ≤ 45 gives 27 ≤ t ≤ 36 and 0 ≤ e ≤ t − 27.
  - I checked every row and boundary: t = 27 (e = 0 with t odd), t = 36 (N = ∅), and e = 1 at t = 28, 29 and 30.
  - Exactly five cases remain: (30,0), (30,2), (30,3), (29,2) and (28,0).
- **Bridge:**
  - The profile lists are complete and the normalization is valid.
  - Constraints (i)–(iv) are necessary, and H preserves them.
  - Exact-cardinality blocking plus a final UNSAT gives completeness.
  - Phase and completion exclusions are necessary conditions on N, and they transfer to G-images.
- **Conditional on P1–P5:**
  - Excluding (30,0) gives s ≥ 44.
  - Adding (28,0) and (30,2) gives s ≥ 45.
  - Adding (29,2) and (30,3) gives s ≥ 46.
  - A failed binding falls back along this chain.
- **Limits:** this is a lower bound only. Combined with Pandya's upper bound of 60 (not reviewed here), the range narrows conditionally from 38..60 to 46..60. Nothing proves the minimum support is 46. Nothing here bears on 59 versus 60. No novelty or priority is claimed.

## Imports / pending evidence

- **Imported:**
  - LOWER42 r2 (1db90164…1418): §0, Lemmas L42-1 to L42-11, the §2 cases t = 33–36 and the corollary.
  - Tarry's theorem, cited through Pandya LF42–46; the primary references are not pinned.
- **Conditioned on, not verified by me:**
  - the parent's drat-trim RUP recheck of the 18 CNFs;
  - the parent's check of the 24 phase certificates.
- **Required, using independent code:**
  - **P1:** the 14 final CNFs correspond to the 14 profiles of m1, with normalized V_i and the parts validly assigned to values.
  - **P2:** base-CNF and completion-CNF soundness, as in M1(b) and M1(c). For each completion CNF:
    - its hole lines are all lines of the six pairs that meet N0;
    - it puts no T-point on a hole line;
    - it puts exactly one T-point on every other line;
    - it contains nothing else.
  - **P3:** the blocking binding, as in M2.
  - **P4:** the exclusion binding:
    - the 24 certificates are bound to their representatives under the M3 criteria;
    - the 4 completion CNFs are bound to the remaining representatives: (30,0) ×1, (28,0){4,4} ×2 and (28,0){3,3,2}⁴ ×1.
  - **P5:** r2 pins the drat-trim run, the certificates and their checker, and the binding scripts and outputs, and it fixes M3 and M4.
- **Sufficiency:**
  - Once P1–P5 pass, the evidence is mathematically sufficient for s ≥ 46. Tarry's theorem is the only external input.
  - A byte-identical re-run of the worker's generator is not a binding.
  - Not needed: the worker LRAT checkers, the satisfied-hint argument, the e = 0 run, filters (a) and (b), and the controls.
