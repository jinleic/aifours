DISPOSITION: UNIFIED-r2=ACCEPT-WITH-FIXES; DELETIONS-v1=ACCEPT-WITH-FIXES

**Scope.** These dispositions cover the correctness of the written bridge and of the deletion manifest only. This is not a cutover verdict. Problem 16 at n = 8, K4 and K5 are not decided. Desk [F] files are aids, not premises. All derivations below are static.

**Abbreviations.**

| Short | File |
|---|---|
| BR2 / BR1 | review/N8_UNIFIED_ONE_P4_BRIDGE.r2.md / .r1.md |
| DEL | evidence/UNIFIED_ONE_P4_DELETIONS_v1.json |
| PV | parent/moqls8-k1k2-parent-verdict.md |
| KK1 / KK2 | review/PROOF_K1_K2.r1.md / .r2.md |
| SRC | sources/2607.12933v2.raw.txt |
| GA | code/gram_a.py |
| TPL | review/K5_COLUMN0_TEMPLATE_COVER.r1.md |
| IMP | review/K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md |
| ENC | review/K4K5_ENCODING_SOUNDNESS.r3.md |
| RM | README.md |
| DX / DC / EF | desk/DELETION_EXTRACT.json / desk/DESK_CHECKS.json / desk/EARLIER_FINDINGS_SUMMARY.txt |

## Target 1: BR2

**FATAL: none. MAJOR: none.** The chain is sound for every non-classical set:
- A8 contrapositive plus W8 gives a weight-3 entry.
- §3 puts the set in normal form.
- The template theorem picks one of 16 templates.
- The canonical assignment satisfies F_one ∧ U_T.

**MINOR**

1. **BR2:72-74 — canonical w3 values are under-specified.**
   - Defect: "its flag at(1,0) may be true" does not define an assignment, yet the kept ALO (index 5733728) needs some Q1 flag set true. Also, "defining values" (L74) is undefined for the one-way w3 (ENC:36).
   - Fix: set w3_1(0,(1,0)) := ⊤. Each of its 28 clauses ¬w ∨ ∨_{k∈K} g_1((0,k),(1,0)) (GA:244-245, |K| = 6) meets {1,2,3}, because |{0..7}∖K| = 2. Set every other w3 flag := ⊥.
   - Cite GA:242-247: w3 literals occur only negatively in one-way clauses and positively only in the five ALOs. DX:106-135 can be cited as an aid.

2. **BR2:27-31 — provenance is overstated.**
   - "read/hash-bound once" and "independently identified" have no pinned script or receipt. The only independent re-scan (DC:2-3, 23:43) post-dates the 23:34 freeze (RM:373) and is an aid.
   - L30-31 ("All other clause bytes/order remain identical") asserts a property of a file that does not yet exist (L31; DEL:20).
   - Fix: drop "independently", cite a receipt, and restate L30-31 as the generator obligation in DEL MINOR 2.

3. **BR2:80-89 (with TPL:59, 111-113, 117-120) — the template import is outside TPL's stated scope.**
   - TPL's conclusion is about "genuine K5" (TPL:111, 119-120).
   - TPL invokes the reduced-K5 bridge (TPL:59 → IMP:11-14, 72-74), whose conclusion concerns F, not F_one.
   - TPL bundles a 13-case/c112 interface that this route must not import.
   - The proof itself uses no K5 hypothesis (see U5), so a restatement fixes this. State the property-form theorem T16:
     > Every set of 5 MOQLS(8) in row-0 standard form with (1,0) supports A, {4}, {5}, {6}, {7} in square order admits σ ∈ Sym(A)×Sym(B), a relabelling of squares 2–5 and a permutation of rows 2–7, after which those supports and ROWLEX still hold and (supp Q1(i,0))_{i=2..7} is one of the lists at TPL:84-104.
   - Declare TPL:111-113 and 117-120 not imported.
   - Pin TPL `1ae1c81d…` (RM:352) and the 16 unit lists (RM:364 `f77c0619…`, or a new F_one manifest).

4. **BR2:59-62, 84-88 — residual action and relabelling are not written out.**
   - Earlier findings EF:5-6 (K5NF-r2 m1) and EF:12-13 (TPL m1) are now load-bearing.
   - Under σ ∈ Sym(A), Q1(1,0) is not fixed as a vector (contrary to IMP:67); only its support A as a set is preserved. L87 ("Q1 still has its weight3 witness") understates what is needed.
   - Fix:
     - Write Q'_s(i,σ(j)) = P_σ Q_s(i,j), so supp Q'_1(1,0) = σ(A) = A.
     - State that SB2, the kept ALO and its one-way clauses depend only on that set.
     - Relabel square s ≥ 2 as σ(s+2)−2 (IMP:68-69).
     - List square relabelling (ρ) as an explicit move (used at L59 and L84; the set is unordered).

5. **BR2:47 — novelty mixed into a correctness import.** "partial original result" conflicts with PV:36 ("No novelty claim"). Replace with "correctness-accepted partial result; no novelty claim."

6. **BR2:93-95, 100-101 — premises and gates are incomplete.**
   - Missing premises:
     - SRC definitions and rules #2/#3 (SRC:195-225, 297-302).
     - Lemma 10 (SRC:342-356), carried inside A8.
     - ROWLEX bit order (IMP:42-51; GA:248-270).
     - Machine facts: byte-exact generator receipts, 16 strict drat-trim VERIFIED results, parent replay.
   - "Reviewed template theorem" is not the same as parent-accepted (RM:371). The gate should name the parent disposition of T16, as RM:390 does.
   - "FULL n8 instance" (L95) is valid only as the consequent of the conditional. Write: "would answer the n = 8 case (SRC:642, n−3 = 5) affirmatively."

7. **Wording and pins.**
   - L62: "row/column orthogonality" should be column-j orthogonality with (0,j) = |j⟩ (rule #2, SRC:297-299).
   - L68: "restoring" should be "establishing" ROWLEX (EF:7).
   - L71-72: G3–G5 and the constants hold for every QLS; G2 holds for every orthogonal pair.
   - L11-12: the list omits the b3/c4 AND, u5 and lexeq definition clauses (EF:17). L30-31 and L74 cover them.
   - L13-14 and L80 cite IMP, ENC and TPL without SHAs (`34e11e52…`, `a83d3050…`, `1ae1c81d…`) (EF:18).

## Target 2: DEL

**FATAL: none. MAJOR: none.** Indices, conventions, line hashes, square assignment, the Q1 keep and the counts are correct (see U4).

**MINOR**

1. **DEL:9 — unreceipted process claim.** There is no script, argv or output SHA, and "Read/hash source once" cannot be verified. The data are corroborated by DX:17-98 [F] and by the static GA derivation in U4, but neither is the manifest's own evidence. Add receipt fields, or mark the entry as desk/parent-verified.

2. **DEL:19 — "All retained byte-for-byte" describes a CNF that does not exist yet (DEL:20).** The listed families also omit the AND/u5/lexeq definition clauses. Rename the field to `generator_obligations`. The generator receipt must prove:
   1. Source SHA is `6ecb77a7…`, the header is `p cnf 509915 5740230`, and there are 5740230 LF-only clause lines with no CR or comment lines.
   2. The four pinned SHAs appear at the four indices and the Q1 SHA appears at index 5733728; otherwise abort.
   3. The output header is `p cnf 509915 5740226`.
   4. The output body equals the source body with exactly those four lines removed. Pin the expected F_one SHA now (computable in one streamed pass) and require equality.
   5. For each template, exactly the 42 pinned units are appended in a declared order, the header reads 5740268, and the per-case SHA is pinned before solving.
   6. The solver and drat-trim streams hash-equal that SHA.
   7. The parent regenerates byte-identically, and fail-closed negative controls are run.

3. **DEL:2-7, 10, 21 — missing conventions.**
   - The exact output header bytes are not given.
   - "file line = index+2" (DEL:12-17) silently assumes the header is line 1 with no comment lines.
   - The 16-case count 5740268 is not linked (it appears only at BR2:99).
   - No generation method is stated. It must be a byte filter of the pinned F, not a re-encoding with `--p4 1`. That re-encoding would also drop 6272 one-way clauses and 224 w3 variables, and would renumber lexeq starting at 509657.
   - Paths mix relative (DEL:2) and absolute home-directory forms (DEL:10, 21).

## Answers

**U1 — A8 import.** The import is faithful: BR2:38-39 matches KK2:45 and PV:13.

The proof steps check out (KK1:38-48):
- **Sequential Lemma 10 on the other four squares.** This is legitimate: each output is independent of the other squares and preserves orthogonality (KK2:34-39).
- **The six classes form a net.** The L′_r are Latin with identity first row and pairwise orthogonal, so rows, columns and the four L′_r classes form a 6-net.
- **Lemma 3 on each line.** Ψ_s is an ONB of weight-≤2 vectors on each line (Prop 1), so Lemma 3 (KK2:23-29) gives E∩M ∈ {∅, V∩M}.
- **H is 6-regular and connected.** H is simple and 6-regular, and two a-cells share at least 4 neighbours, so H is connected.
- **The weight-1 cell (0,a).** This cell lies in V but not in E, so E = ∅.

The use here is no stronger than what was accepted: KK2:76 already applies A8 to an arbitrary non-classical S.

Classicality matches. Set isotopy (iii) applies per-square unitaries (SRC:220-225), so a set is classical iff each square has 8 rays iff all row-0-frame weights are 1 (KK2:14-17). Hence in every row-0 standard form of a non-classical set:
- some entry has weight ≥ 2;
- by A8, some entry has weight ≥ 3;
- by W8 (KK2:40-43), that weight is exactly 3 and the entry is off row 0.

No Egan–Wanless input is needed (BR2:51 is correct).

**U2 — Normalisation.** Every move is valid for an arbitrary S, and none uses non-classicality, reduced-K5 membership or P4 of squares 2–5.
- **(γ) Per-square standardisation** is isotopy item (iii) (SRC:222, 287-288).
- **Choice of Q1** is just a label: any square with a weight-3 entry.
- **(α) Common row permutation** of rows 1–7 leaves row 0 fixed.
- **(β) Column permutation σ** with σ(j) = 0 and P_σ on all vectors gives Q'(0,σ(k)) = |σ(k)⟩, so standard form is kept. The witness support avoids j, hence avoids 0 after the move.
- **Cell (1,0).** The supports are disjoint (SRC:300-302), nonempty, and avoid 0. So 3+1+1+1+1 partitions {1..7}.
- **Second permutation τ fixing 0.** τ with τ(S₁) = {1,2,3} and τ(S_s) = {s+2} exists for any labelling, so no square relabelling is needed here.
- **Final sort of rows 2–7** by v_i (GA:253-255; the coordinate-0 bit is constant ⊥) gives non-strict ROWLEX without touching rows 0 and 1.

**U3 — Canonical assignment satisfies F_one.** Yes, for every genuine set.
- **Families valid for any set.** G2 (Prop 1), G3 (unitary transition), G4 (one-term/zero-term Parseval), G5 (same ray), the constants, and the full-equivalence definitions of b3/c4/u5/lexeq all hold (ENC:27-37, 94-101).
- **Q1.** w3_1(0,(1,0)) := ⊤ satisfies its 28 clauses and the kept ALO. Every sampled clause contains 50, 99 or 148 (DX:142-486 [F]).
- **Squares 2–5.** With all their flags ⊥, every one-way clause holds. Their positive occurrences are only in the ALOs (GA:242-247; DX:106-135: 1568 = 56·28 negative occurrences per square, 5880+1960 one-way clauses). So the only clauses falsified are the four deleted ones.
- **No retained clause forces non-classicality of squares 2–5.** SB2 forces their (1,0) weight to 1, and ROWLEX involves only Q1.
- **Observation.** Given the SB2 units, the kept ALO is always satisfiable via w3_1(0,(1,0)). So F_one ∧ U_T is satisfiability-equivalent to the same formula with all P4 clauses removed.

**U4 — Exact deletions.** Correct.
- **Conventions** agree across BR2:16-17, DEL:8 and DX:16. The SHAs agree across BR2:21-25, DEL:12-17 and DX; the hash values themselves are desk/replay facts.
- **Static index check from GA:**
  - Each P4 block is 56×28 one-way clauses plus the ALO (GA:235-247), giving a spacing of 1569.
  - The tail is ROWLEX (5×(1+36+1) = 190 clauses) plus SB2 (5×7 = 35 units) = 225 clauses (GA:253-281).
  - So the square-5 ALO is at 5740229−225 = 5740004. Stepping back by 1569 gives 5738435, 5736866, 5735297 and 5733728, exactly matching DEL:12-17. DX:145 agrees (5732160 = 5733728−1568).
- **Variable layout:** 509600 g/b3/c4/u5 variables; w3 = 509601–509880 in row-major order per square; lexeq = 509881–509915.
- **Line content:** each deleted line consists of exactly that square's 56 positive frame-0 flags, covering every off-row-0 cell (GA:239-247; DX:31-96). Q1's ALO is kept.
- **Counts:** 5740226, and +42 = 5740268. The 42 are the 6×7 non-constant g_1((0,c),(i,0)) (GA:130-131).
- **Receipt obligations:** see DEL MINOR 2.

**U5 — Template coverage.** All hypotheses hold without assuming squares 2–5 are non-classical:
- The degree bound (TPL:9-12) holds for any line and any five MOQLS(8), classical or not. This gives column degrees ≤ 3 (frame row 0) and row degrees ≤ 3 (frame column 0) for U.
- TPL §2 is pure support algebra. I checked the K33−e closure and K44−M (with x = y = z).
- P0/P1/P2 need only supp Q1(1,0) = A.
- Sym(A)×Sym(B) fixes 0 and keeps A as a set; relabelling restores SB2; re-sorting restores ROWLEX.
- The lists at TPL:84-104 are non-decreasing in GA bit order, with roots 10/3/3.

These moves preserve F_one's hypotheses.

Status changes among earlier findings:

| Earlier finding | New status |
|---|---|
| TPL m1 (Sym(A) action) | Load-bearing → BR2 MINOR 4 |
| K5NF-r2 m1 (relabelling move) | Load-bearing → BR2 MINOR 4 |
| TPL m2 ("reduced K5" wording) | Flips from over-broad wording to a required restatement → BR2 MINOR 3; not a correctness gap |
| TPL m3 (c112 citation) | Moot here |
| TPL m4 | Unchanged |
| IMP m1 / m2 / m4 | Recur → BR2 MINORs 2 and 7 |

**U6 — Consequence and acceptance conditions.** The logic is complete. For every non-classical S:
1. A8 and W8 give a weight-3 entry.
2. §3 gives the normal form.
3. T16 gives some T among the 16 templates.
4. The canonical assignment satisfies F_one ∧ U_T.

So UNSAT of all 16 formulas would imply that every set of 5 MOQLS(8) is classical.

No old certificate transfers:
- F_one ⊊ F as clause sets, so UNSAT(F ∧ c112) and the 13 old UNSAT(F ∧ U_T) imply nothing for F_one.
- A DRAT proof certifies only the exact bytes it was checked against.

Acceptance requires 16/16 strict refutations with byte-exact receipts, parent independent replay, and parent disposition of BR2 and T16. Thirteen is not enough. No Boolean-cover claim and no "F_one UNSAT" claim is needed (BR2:99-100; TPL:122-123).

**U7 — Consistency and overstatement.**
- BR1 → BR2 is consistent. BR1:30-31 ("defining values or false") is resolved to "false".
- RM:373-391 and DEL agree with BR2 field for field. RM:383-384 should say "in some square, then labelled Q1."
- **Overstated:** "read/hash-bound once" and "independently identified" (BR2 MINOR 2); "partial original result" (BR2 MINOR 5).
- **Not overstated:** "No other family requires them to have a weight3 entry" (BR2:34) is true by GA:242-247, which should be cited. "FULL n8 instance" is correct as the conditional's consequent.

**Correctness, novelty and significance, kept separate.**
- **Correctness:** both targets are correct subject to the MINOR fixes. Nothing is certified yet.
- **Novelty:** not assessed and not claimed (PV:36).
- **Significance:** conditional only. Problem 16 at n = 8, K4 and K5 remain undecided.

UNIFIED-r2 FATAL=0 MAJOR=0 MINOR=7
DELETIONS-v1 FATAL=0 MAJOR=0 MINOR=3
