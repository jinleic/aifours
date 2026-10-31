# Definition-first common selection IX: stronger missing-pair capacity and exact Hamilton cut coupling after affine D2 closure

Owner **InfoRecursiveMDS18-2**, slot **info-4**. Actual native prewrite clock: **Tue Oct 27 15:21:58 PDT 2026**.

**NEW author-WRITTEN, unreviewed necessary/sufficient completion certificates.** These apply to ANY actual n−2-row partial system at the original n=11, not a maximal-overlap or selected support family. They retain all original actual-row quantifiers. No original partial input or witness is supplied, and no all-array contradiction is claimed.

## 0. Source and imports

Same admitted S1 definition-first actual-row line; the only external problem source is literal packet SHA256 `6a4abaf97065c6c4b5181529810e622f76e3f485660f489593cda3ccaa88878c`, complete LF1-37. This continues the fully proved own `prerequisite-two-row-completion-v8.md`, SHA256 `a7414abf523c8d76c26dca66fae4cf25ba255dbe58245167090010fc9ecb1bcb`.

Imports are the v8 sentinel equivalence, degree-two residual/component parametrization and exact D2-XOR lemma, plus elementary finite counting, binary equations and permutation-cycle connectivity. No old proof/turn/Latin-sign/support/source, held/ZERO guide, private method or Olson review input. Prior exposure is not certified absent.

No row/graph enumeration, scientific execution, arithmetic interpreter, calculator/CAS, selected numeric/control/boundary probe, solver, modelCLI or new GO. Universal cut families and affine variables below are mathematical quantifiers, not an executed cut-generation or search procedure.

## 1. Setting and a stronger capacity obstruction

Use v8's arbitrary fixed n−2 actual rows and augmented residual graph D on X∪{∞}, with all degrees2. The fixed rows have separately distinct starting and ending symbols; otherwise no extension is possible. Let U be their `(n−2)^2` already-used directed D2 outer pairs.

Among the UNUSED distinct outer pairs in X, define Z_j for j=0,1,2 according to whether exactly j residual paths a→b→c with b∈X are available. There are at most two paths, and the sets partition the unused pairs. Their total size is

`|Z_0|+|Z_1|+|Z_2|=n(n−1)−(n−2)^2=3n−4`.

**Proposition 1 — strengthened mandatory missing set.** In any two-row extension, EVERY pair in `Z_0∪Z_2` is absent from the final D2 event set. Consequently

`|Z_0|+|Z_2|≤n`, equivalently `|Z_1|≥2n−4`.                      (RES)

**Proof.** A pair in Z_0 has no path from which to create a new event and was unused before. A pair in Z_2 cannot be created by either path: by v8 Lemma2, the two paths are simultaneously monochromatic or simultaneously nonmonochromatic under any proper two-colouring; the first alternative would duplicate the pair, so both must be nonmonochromatic. Thus every pair in Z_0 or Z_2 is among the n final missing directed pairs. Equivalently the last two actual rows must obtain all their2(n−2) distinct new D2 events from Z_1. ∎

This strengthens v8's bound on Z_2 alone; it does not edit or invalidate that weaker necessary bound. No specific outer-pair count is asserted for an unprovided nine-row input.

## 2. Hamiltonicity is exactly a simultaneous two-colour cut condition

For a nonempty proper vertex subset A⊂X∪{∞}, write δ⁺(A) for the directed residual arcs leaving A.

A proper two-colouring χ gives one outgoing/incoming edge of each colour at each vertex, hence two permutation cycle covers P,Q. Such a permutation cover is a single Hamilton cycle exactly when it has an edge leaving every nonempty proper A: if it has multiple cycles, one cycle's vertex set is closed; conversely a closed proper set cannot occur in one full Hamilton cycle.

Therefore BOTH P and Q are Hamilton exactly when

> δ⁺(A) contains both colours for EVERY nonempty proper A.          (HCUT)

This is not just degree balance. In particular a cut with zero or one outgoing residual arc precludes any two-row extension.

With v8's component variables, `χ(e)=τ(e) xor x_j`, each HCUT is a not-all-equal constraint on the actual outgoing-arc colour literals. A two-arc cut gives the exact extra affine equation χ(e) xor χ(f)=1. Larger cuts are NOT replaced by an unjustified binary equation.

**Complete caller.** A two-row original extension exists iff there is one SAME component vector satisfying every v8 D2-XOR equation AND every HCUT. Forward is immediate from the two actual augmented Hamilton cycles. Conversely proper colouring plus HCUT makes both cycles Hamilton; deleting ∞ gives the actual rows, and D2-XOR checks every original outer pair. No sentinel event is counted as an original event.

## 3. What affine closure proves about each cut — exactly

Start with the D2-XOR equations. One may additionally include all mandatory two-arc HCUT equations. If they are inconsistent, there is no extension.

A consistent system of equations `x_j xor x_k=b_jk` partitions its variables into connected constraint classes. Choose one free bit y_C per class. Within it,

`x_j = y_C xor d_j`,

where d_j is fixed by any path from a reference variable; cycle consistency makes d_j well-defined. Thus every residual arc has colour

`χ(e)=y_(C(e)) xor s_e`,

where s_e is its fixed reference parity. Different classes' free bits are independent for THIS affine system. No independence after imposing HCUT is claimed.

### Lemma 2 — exact universal cut-safety criterion

For any fixed cut δ⁺(A), the following are equivalent:
1. EVERY solution of this affine system gives both colours on that cut.
2. The cut contains two arcs e,f in the SAME constraint class with fixed opposite parities `s_e xor s_f=1`.

**Proof.** Such a pair always differs in colour, proving2→1. If no such pair exists, all cut arcs belonging to any one class have the same s_e. Choose that class's free bit to cancel this parity. These choices are independent between classes, so one affine solution makes ALL cut arcs colour0; global complementation gives colour1. Thus1 fails. Empty and single-arc cuts also fail1 and have no such opposite pair, so the equivalence covers them. ∎

This is an exact statement about EVERY affine solution, not the stronger and unproved claim that failure of2 excludes SOME Hamilton solution.

### Corollary 3 — robust completion certificate

If the affine system is consistent and EVERY nonempty proper cut has a pair as in Lemma2(2), then EVERY affine solution gives two Hamilton cycles and hence an original two-row extension.

**Proof.** Lemma2 supplies HCUT simultaneously for each solution; v8's exact caller supplies the actual original rows. The existence of an affine solution is already included in the stated premise and follows from cycle consistency of its labelled constraint graph. ∎

This is a genuine realization direction: once those universal cut certificates and the affine consistency premise are proved for a given actual partial system, no separate favourable cycle-cover-to-row assertion is needed. No such partial system is constructed here.

## 4. Forced monochromatic cuts are unconditional noncompletion certificates

**Proposition 4.** If for some nonempty proper A all arcs of δ⁺(A) are in ONE affine constraint class and have the SAME fixed parity, that cut is monochromatic in EVERY affine solution. Thus no original two-row extension exists. A zero-arc cut is likewise impossible.

**Proof.** All those arc colours are the identical expression y_C xor s. No assignment can put both colours on the cut, so HCUT fails. ∎

This condition is stronger than merely observing that one affine solution makes a cut monochromatic. If the cut uses several independent classes but has no forced opposite pair, Lemma2 shows a bad affine solution exists; it does NOT show no good solution exists. The remaining not-all-equal constraints may couple those classes and still admit a Hamilton solution. That quantifier boundary is essential.

**Additional affine closure.** In particular a two-arc cut whose two arcs are forced equal contradicts its mandatory opposite-colour equation. More generally, adding ALL two-arc cut equations preserves an exact necessary system. It cannot justify discarding larger-cut constraints that are not thereby made universally safe.

## 5. Exact original scope and remaining selection issue

For every hypothetical original eleven-row array, EVERY choice of nine of its rows must yield a residual satisfying (RES), the affine constraints, the parity necessary condition of v8 and an actual common solution of HCUT. The results do not assert that some such choice necessarily violates one of them.

We now have:
- a stronger all-variable forced-missing capacity obstruction;
- an exact affine-plus-cut completion equivalence;
- a robust positive completion certificate (Corollary3);
- a robust negative completion certificate (Proposition4).

**Still unproved:** for an arbitrary original partial system, whether its remaining higher-arity cut constraints have a joint solution, or a universal reason why some unavoidable residual violates them. A feasible affine system or one nice colouring is not enough. No input-clean argument currently supplies a nine-row partial system meeting the positive certificate, and no all-array obstruction is claimed.

The route remains the literal original problem, not a promise to solve a smaller fixed-state instance. No computational cut/row search, modelCLI or new source is admitted. Old source/method/exposure STOP/HOLD/ZERO/findings, N4 UNKNOWN/historical exit UNESTABLISHED and auxiliary214 STOP remain. Same-harness author-written, unreviewed; no Main adoption, kernel/formal, executable, human, configured-family, source-openness, priority or novelty gate. Deadline unchanged.
