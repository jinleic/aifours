DISPOSITION: ACCEPT-WITH-FIXES

**Scope.** This is a static audit of the quoted excerpts only. Several dependencies were not supplied, so I did not inspect them:
- `ltg.SmallGen` (its V, d, var and hl)
- `ame_e0_cnf.CNF.at_most_k`
- `lte.PAIRS`
- the v4 driver, the lex encoder and the exact checkers

Anything that depends on these is listed below as a binding obligation, not as verified. I found no blocking defect. The mathematics of Lemma 19, J, Lemma 20 and the orbit-lex argument is sound. `triangle_clauses` matches the written pattern and its counts are exact. Nothing here establishes s ≥ 49; s ≥ 48 stands.

### 1. Lemma 19 and J: sound

- **C1.** N ⊂ ΠV_i, so a line with (b,c) ∉ V_j×V_k has no point of N. The line is non-empty (norm 1), so its support points are officers, and there is at most one (L42-3). So it holds exactly one. ✓
- **C2.** Follows from L42-3. ✓
- **C3.** Let D be the set of b for which line (a,b) has no officer.
  - |D| = d_{i,a}, because officers with x_i = a have distinct j-coordinates.
  - D ⊂ V_j, because a line with no officer carries at least two points of N, and their j-coordinate lies in V_j.
  - So exactly d_{i,a} of the |V_j| lines have no officer, and each of the others holds exactly one. ✓
  - Worth recording: C1 and C3 together force 6 − d_{j,a} officers with x_j = a. Hence t = 36 − h is implied, not assumed.
- **Encoding** (`code/profile_officer_cnf.py:36-58`). This matches the lemma.
  - C1 is at-least-one plus at-most-one; C2 is at-most-one.
  - At :52-54, v ↔ OR(line) is encoded in both directions.
  - The pair of `at_most_k` calls on the indicators and their negations encodes "exactly `want`".
  - For a genuine T, the auxiliaries are v = OR and the sequential counter's partial sums. That these exist is a property of the counter alone; no symmetry is used.
- **Offset** (`code/exp_joint.py:26-33`). The map l ↦ l ± off preserves sign, and `ovar[x]` equals the shifted `var[x]`. ✓
- **Linking** (`code/exp_joint.py:34-42`). Take v = [line meets N]. Then L42-2(a) gives the two-literal clauses and L42-4 gives the long clause, for every e. ✓

Can a genuine state fail J? Not mathematically. In the implementation, only through the hidden bindings in MAJOR-2.

Exceptional profiles are not a risk:
- want < 0 would mean d_{i,a} > |V_k|. That is impossible for a genuine state, since D ⊂ V_k, so any behaviour of `at_most_k` there is sound.
- k = 0 and k = |inds| both occur in the Pandya control (d = 6).

"Records imply completion" can be stated only in this form. If hl is two-sided, a record's T is an exact officer placement for its N:
- lines meeting N have no officer, by linking;
- every other line has exactly one officer, by C1 outside the V_i×V_j lines and by linking plus C2 inside.

Whether an AME state exists is decided only by the exact check of all three reshapings. The excerpts do not overclaim this.

### 2. Lemma 20: sound

Take the edge (z1, z2) in reshaping (i c1 | c2 c3).
- The rows are (a, p) and (a′, p), where p = z1_{c1} = z2_{c1}.
- The columns are (z1_{c2}, z1_{c3}) and (z2_{c2}, z2_{c3}). They differ because z1 ≠ z2 and the two agree on c1.
- Each of these four lines meets N, so at e = 0 each holds exactly the two listed points. The 2×2 block is closed.
- Row orthogonality has two non-zero terms, which gives δ(z1) − δ(z2) ≡ π.

None of the proposed escapes works:
- **Arbitrary amplitudes.** The moduli never enter; only non-vanishing is used. A non-flat block is no escape.
- **Orientation.** Swapping r↔r′ or c↔c′ negates the left side, and −π ≡ π. The alternating sum is also invariant under local diagonal phase gauge.
- **Across reshapings.** The three edges pair i with c1, c2 and c3, which are the three distinct reshapings. φ_x = arg ψ_x does not depend on the reshaping. Summing gives 0 ≡ π + π − π ≡ π, a contradiction.
- **Distinctness.** a ≠ a′ and pairwise-distinct z suffice. "Differs in both other coordinates" is stronger than needed.
- **e = 0.** This is the only source of "exactly two support points on each of the 12 lines". At e > 0 a row can carry a third entry (a component with e_K ≥ 2). Orthogonality then has three or more terms and gives no ±π congruence. The restriction is necessary.

### 3. `triangle_clauses`: matches the pattern; counts exact

- The filters:
  - :48 requires z2 = z1 on c1 and z2 ≠ z1 on c2 and c3.
  - :51 requires z3_{c2} = z2_{c2} and z3_{c3} = z1_{c3}.
  - :53 requires z3_{c1} ≠ z1_{c1}.
- The remaining differences follow:
  - z2 and z3 differ on c1, since z3_{c1} ≠ z1_{c1} = z2_{c1}, and on c3.
  - z1 and z3 differ on c1, from :53, and on c2.
  - So every emitted clause is a valid six-set with six distinct literals inside ΠV.
- Count. Each triangle is z2 = (z1_{c1}, q′, r′) and z3 = (p′, q′, z1_{c3}), with each primed value different from z1's.
  - That gives Π_{k≠i}|V_k|(|V_k|−1) triangles per (i, {a, a′}).
  - The total is **2·Π_k |V_k|(|V_k|−1)**.
  - For sizes (2,6,6,6): 2·2·30³ = 108,000 ✓ (27,000 for each i).
  - For (6,6,6,6): 2·30⁴ = 1,620,000 ✓.
- Duplicates: none. A six-set determines i (the only coordinate whose values split 3+3), then {a, a′}, then the labels (z1 is the vertex shared by the c1- and c3-edges).
- Two families are omitted; both affect efficiency only, never soundness:
  - Degenerate triangles, where an edge agrees in two coordinates. These put (a;z1), (a;z2), (a;z3) on one {i,c}-line, which the base's two-per-line family already excludes at e = 0.
  - Odd cycles of length 5 or more (k·π with k odd). These are not encoded.

### 4. Orbit-lex: valid with officer variables left unbroken

The witness assignment satisfies base, J, W (when e = 0) and Lex_Γ:
- N* = g(N);
- g(T) for the officers;
- the base auxiliaries of g·ψ;
- v = OR over g(T), plus the counters' partial sums;
- lex chains set to "prefix agrees".

H preserves the normal form and e, so W's restriction to e = 0 is orbit-stable. No symmetry of the CNF or of the officers is needed. Γ consists of transpositions, so the encoder's action-versus-inverse convention does not matter. "Least" must mean least in the order the encoder actually imposes, including its bit direction. The blocking step does need an explicit statement; see MAJOR-1.

### Findings

**MAJOR-1: the blocking step is incomplete as written** (`review/ENGINE_V3.r1.md:85-87`, `review/ENGINE_V4.r1.md:84-85`).

The step "UNSAT ⇒ N* is a recorded solution" uses three facts that are not stated. Insert:

> Every base model has Σ n_x = 2h + e. [For e = 0: from the base's exactly-two, n_x → hl and per-value hole-count families, Σ n_x = 2·Σ_a d_{1,a} = 2h. For e > 0: cite the base family that fixes |N|.] Every recorded Y is a base model, so a base model falsifies ∨_{x∈Y} ¬n_x if and only if N = Y.
>
> Every line meeting Y has no officer. So Y's component, modulus and phase systems are those of every AME state with non-classical part Y, whatever its officers. A rejection of Y is therefore independent of T, and blocking on point variables alone is valid in the joint model.
>
> A case is EXCLUDED only if every recorded Y has such a rejection. A candidate, or a failed reconstruction, never produces a block.

Soundness is unchanged if |N| is fixed for e > 0. If it is not fixed, the short blocks also exclude unchecked supersets of Y. In that case e > 0 exclusions are unsound until the blocks are replaced by full ones: ∨_{x∈Y} ¬n_x ∨ ∨_{x∈ΠV∖Y} n_x.

**MAJOR-2: the J/W bindings are not visible, and no control covers them.** The following must hold and be asserted in code:

- **(a) One source for V and d.** `poc.build` derives V and d itself (`code/profile_officer_cnf.py:26-27`): the top |V_i| values, with the k-th smallest value given prof[i][k]. The linking uses `S.V` and `S.hl` instead (`code/exp_joint.py:35-38`).
  - If SmallGen's convention differs, J is unsound on every profile with some |V_i| < 6 or with mixed deficits. An example is {6,6}{2⁶}³, which is in the s = 48 layer.
  - The only positive control, Pandya's state, has V_i = [6] and exercises one deficit order.
  - Fix: compute V and d once and pass them to both builders, or assert equality in `build_joint`.
- **(b) hl is two-sided.** `S.hl[(i,j,a,b)]` must equal [line meets N] under the genuine assignment of L46 r2 §3 step 2. ENGINE_V4 §3 identifies the two silently.
- **(c) Variable ranges.**
  - Every base variable, including any hl created lazily, is ≤ off.
  - The officer block lies in (off, off + F.nv].
  - Lex chains start above off + F.nv.
  - `at_most_k` allocates from `F.nv`; line :51 writes `F.nv` directly, so both must share one counter.
- **(d) W gated in code.** The driver must raise a hard error when `--triangles` is given with e ≠ 0, and e and the flags must be recorded in the CNF provenance. At present the restriction exists only in prose (`review/ENGINE_V4.r1.md:28`).

Soundness is unchanged if (a)–(d) hold. A failure of any one voids J- or W-assisted exclusions for the affected profiles.

**MINOR-1: identifier collisions.** Two names are reused for different things:
- Lemma 19's C1–C3 versus the controls C1–C5. For example, `review/ENGINE_V4.r1.md:106` says "C1 and C3 are genuine-state positive controls".
- Facts F1–F4 (`review/ENGINE_V3.r1.md:46`) versus clause families F1–F4 (`review/ENGINE_V4.r1.md:22,36`).

Rename the controls K1–K5 and the clause families B1–B4. Soundness is unchanged.

**MINOR-2: the §5 and §3 witness is incomplete** (`review/ENGINE_V4.r1.md:36-39,82-83`). Add "officer-CNF auxiliaries (C3 indicators v = OR; sequential-counter partial sums)" and "hl = [line meets N]". Soundness is unchanged.

**MINOR-3: the encoding text** (`review/ENGINE_V4.r1.md:70-73`).
- "name its vertices so that the c1-edge is z1z2" leaves z1↔z2 open; add "and the c3-edge is z1z3".
- Add the closed form 2Π|V_k|(|V_k|−1) and the remark on degenerate triangles.
- Replace the "15:2x" self-check with a build-time assertion on the count and on each clause's shape. That assertion would have rejected the void run. 466,560/2 = 2⁶·3⁶·5, but a product of four factors n(n−1) ≤ 30 contains at most 3⁴, so 466,560 is not the correct count for any sizes.

Soundness is unchanged.

**MINOR-4: the controls do not discriminate.**
- C4's agreement with certified UNSAT results cannot detect over-constraint; the void clause set would have agreed too.
- C2 has not been shown to come from J or W.
- Add two negatives:
  - an N that satisfies base and J and contains a doubled triangle: SAT without W, UNSAT with W;
  - an N that satisfies the base but has no officer placement: SAT without J, UNSAT with J.

Soundness is unchanged; controls are not proof.

**MINOR-5: candidate semantics** (`review/ENGINE_V4.r1.md:88-95`).
- State that reconstruction applies only at e = 0.
- Uniform moduli lose nothing for existence there. Any AME e = 0 state's phases solve the block system (Lemma 10 holds for arbitrary amplitudes), and the equal-moduli tensor with those phases and the same T is AME. This does not claim that AME e = 0 states have equal moduli.
- Consequently, with MAJOR-2(b), a candidate's reconstruction must succeed. A failure signals a defect, not a rejection.

Soundness is unchanged.

**MINOR-6: guards in the builders.**
- Assert 0 ≤ `want` ≤ |V_k| at `code/profile_officer_cnf.py:56`, citing D ⊂ V_k, or emit an explicit empty clause.
- In `build_joint`, assert that Σ prof[i] = h for every i, since h is passed to `build_gen` separately. `h` at :25 is unused.

Soundness is unchanged.

**NIT.**
- `review/ENGINE_V3.r1.md:75-76` has a duplicated bullet.
- At `review/ENGINE_V3.r1.md:78`, "each element of H acts as a local or a party permutation" should read "a composition of…".
- At `review/ENGINE_V4.r1.md:81`, "support g(N)" should read "non-classical part g(N)".
- `triangle_clauses` rebuilds Z for every pair and scans all z3, although z3 has only |V_{c1}| − 1 candidates.

### 5. Obligations before any s ≥ 49 claim

1. **Case layer s = 48.** This is e = t − 24 for t ∈ {24, 26, …, 34}; t = 25 is impossible because e ≠ 1. Each case is either dispatched by an accepted written lemma or covered by items 2–6.
2. **Profiles.**
   - Prove that the enumerator lists every normal-form profile for each t: parts in {2,…,6}, summing to h, at most 6 parts, in canonical coordinate order.
   - Hash-bind the generator.
   - PARTIAL runs and `--profiles` subsets never count.
   - Any pruning (officer-only UNSAT, or a d ≤ |V| filter) is certified separately.
3. **Code bindings.** The MAJOR-2 bindings are asserted in proof-mode code.
4. **Final CNF per profile.**
   - Regenerate the final CNF deterministically from hashed code and parameters: base ∧ J ∧ [W iff e = 0] ∧ Lex_Γ ∧ blocks.
   - Record its DIMACS hash.
   - Run a schema checker that validates every non-base clause (J, W, Lex, blocks) against its written form.
   - Produce a DRAT/LRAT proof checked by an independent checker. Exit code 20 alone is not a certificate.
5. **Per block Y.**
   - |Y| = 2h + e.
   - An exact, T-independent, re-checkable rejection: a component witness; a rational Farkas certificate for moduli; or, for phase, an integer combination of block congruences whose phase part vanishes and whose right side is an odd multiple of π.
   - No candidates in the case.
6. **Guards.** Any cap trip, timeout, or solver status other than 10 or 20 makes the whole case UNKNOWN, and an UNKNOWN case blocks the bound. Proof mode needs a fresh parent go.
7. **The void run.** Nothing from the 15:13 run (CNFs or COMPLETE labels) enters any certificate. Its recorded Y may be reused only with their own exact certificates.
8. **Not proof, in any amount:** SAT positive controls, zero triangles in Pandya's state, C4 agreement, any reconstruction outcome, or solver UNSAT without a checked proof and binding.
