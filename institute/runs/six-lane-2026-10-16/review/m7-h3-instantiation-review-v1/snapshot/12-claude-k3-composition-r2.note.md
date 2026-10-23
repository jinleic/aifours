# K3 composition r2: hostile static audit (conditional preflight)

**Conventions.**
- SOURCE00 and SOURCE01 are cited by their embedded original-LF labels, written `oLF`. All other sources are cited by their own LF.
- The r2 fixes are applied and not re-flagged: F1 (cube-specific H_311), F2 (residual normalisation after `--sym`) and F3 (A's G2 clauses contain h).
- This is a static read only: no solver runs, and no hash or byte checks. Nothing is inferred about pending replays or about literal proof provenance.
- No gate authority and no novelty claim.
- This is a preflight, not the parent composition review. SOURCE14:21 and SOURCE01:oLF131 defer that review until G1–G2 are parent-accepted.

## DISPOSITION: ACCEPT-WITH-FIXES (0 FATAL, 0 MAJOR, 9 MINOR)

Given its premises, the chain excludes every K3 triple, and M(7) = 2 follows using the imported lower bound. Every fix is a citation or wording change. None changes a CNF, proof object, status or conclusion.

**The disposition is conditional on:**
1. **G1/G2 parent verdicts** naming all four cube hashes. These need parent replays of B_C321, whose first attempt was UNKNOWN, and of B_C411 (SOURCE00:oLF161-163, oLF173-174).
2. **A certificate for Link 12.** None exists yet; the run is RUNNING (SOURCE00:oLF224-225). This is stronger than "pending replay". A VERIFIED_UNSAT certificate with a clean supervisor record must first exist, and then be replayed by the parent. If attempt 3 ends UNKNOWN, the composition does not close under decision 1.
3. **A parent replay of the strengthened B input** ae3b8309… (SOURCE00:oLF236).
4. **The inherited trust base** (SOURCE00:oLF270-276).

## Findings

| ID | Sev | Where | Issue | Repair |
|---|---|---|---|---|
| m1 | MINOR | SOURCE00:oLF249-250 | Both strengthened inputs contain the cut block. The A side cites only "(Links 7, 11)" and the B side only "(Link 7)". | A side: "(Links 7, 10, 11)". B side: "(Links 7, 10)". |
| m2 | MINOR | SOURCE00:oLF241 vs oLF288-292 | §4 lists "Link 10's use of G1–G2" as a composition-review item. Link 14's premise list names only Links 3, 7 and 11. | Add Link 10 (transport and cut derivation) at oLF241. |
| m3 | MINOR | SOURCE00:oLF193-197 | Link 10's status names G1–G2 as its only condition. But the transport images satisfy the exact C321/C411 CNFs only through G4 on the image (Link 3) and the instantiation (Link 7). SOURCE01:oLF148-152 and oLF164 already say "Under H1–H5". | Change to "condition: G1–G2 and Links 3, 7". |
| m4 | MINOR | SOURCE01:oLF148 | "preserve the QLS axioms and mutual orthogonality, so the image is a K3 triple" omits that each square stays individually non-classical. | Add: "cell permutations, including transposition, leave each square's ray set unchanged, hence its non-classicality (SOURCE03:9-11)". |
| m5 | MINOR | SOURCE00:oLF207 | "The C311 generators also preserve the cuts (C4)" cites a finite control for what is a structural fact. | State the reason. The cut family is indexed uniformly by frame, off-line point, square(s) and subsets, so every row/column permutation and square relabelling maps it onto itself. Independently, Link 10 gives the cuts for every K3 configuration. |
| m6 | MINOR | SOURCE00:oLF216; SOURCE01:oLF373-375 | The general-length comparator argument is still PENDING. | Insert the induction given under Link 11 below. The length-≤4 control then serves only as corroboration. |
| m7 | MINOR | SOURCE00:oLF132-142 | "Every clause holds" also requires that the K3 base emits no empty clause and no `None` literal. Such branches exist: SOURCE08:48, :106, :137 and SOURCE09:65, :148, :151 (with s2 = None), :169. | Cite SOURCE02:141-147 for the 2-net domain and record the sizes. G2 has 

5–6 items, G3 has 6 candidates, and G4 has 6 candidates at each of 42 points. Every degenerate branch is therefore unreachable. |

| ID | Sev | Where | Issue | Repair |
|---|---|---|---|---|
| m8 | MINOR | SOURCE01:oLF362-363 | "One guard per square, line and off-line point" overstates the guard set. (Square 1, row 0) has no guards, because `--sym` replaces that G4 clause by units (SOURCE08:123-126; SOURCE09:191-194). | Wording only. |
| m9 | MINOR | SOURCE00:oLF270-276 | The imported-results list omits the lower-bound source used in §3 step 3 (Ball–Simoens Cor. 7 / Huang–Li Thm 5.2). It also omits the source's set-isotopy definition, on which (C0) rests (SOURCE03:12-13). | Add both. |

## Link 3: ACCEPT

- **Lemma 10 step.** Suppose a square of a K3 triple is light in some ONB. Basis-free Lemma 10 (SOURCE03:54-67) replaces it by a classical square. The replacement keeps every zero inner product, so the row/column ONBs and both partner orthogonalities survive at once (SOURCE03:63-64).
- **Contradiction.** The new square is orthogonal to both partners, so it is distinct from them. The result is a genuine triple with exactly two non-classical squares, which contradicts K2 directly. The minimality route (SOURCE02:52-65; SOURCE03:69-75) is also correct; K1 is needed there only to make every K3 triple minimal.
- **Own-line reading.** Take B to be the ONB of an own line ℓ. On-line entries have weight 1, so the heavy witness lies off ℓ, with weight #{r∈ℓ : g(p,r)} (SOURCE02:59-60). That is exactly the clause at SOURCE08:127-137 and SOURCE09:195-202: 42 candidate points, each with 6 non-collinear cells.
- **Later images.** Every normalised or transported image used later is again a K3 triple, so G4 holds for it without further argument.

## Link 7 (H3): ACCEPT-WITH-FIXES (m7, m8)

Every emitted clause family traces to a necessary condition, or to an auxiliary with a canonical value. No other families are emitted.

**Encoder A, `build(3, None, True, True, None)`:**

| Family | Lines | Reason | Aux value |
|---|---|---|---|
| g vars; collinear pairs absent | SOURCE08:58-71 | G1 by absence | — |
| h ↔ g∧g | SOURCE08:75-86 | definition | the conjunction |
| G2, count 0 | SOURCE08:95-96 | G2 (SOURCE02:40-42) | — |
| G2, count 1 / collinear | SOURCE08:97-99 | G2; G1+G2 when collinear (F3) | — |
| G3 cover and singleton | SOURCE08:105-114 | G3 (SOURCE02:43-47), parallel and perpendicular lines | — |
| G5 | SOURCE08:115-118 | exact orthogonality (SOURCE02:49-50) | — |
| `--sym` units | SOURCE08:123-126 | Link 5; residual normalisation fixes square 1 and columns 0–3 (SOURCE05:20-22) | — |
| guarded at-least (15 four-subsets) | SOURCE08:45-51, 127-136 | definition | w := [≥3 neighbours] |
| OR of guards | SOURCE08:137 | G4 (Link 3) | — |

**Encoder B, `--squares 3 --heavy --sym`:**

| Family | Lines | Reason | Aux value |
|---|---|---|---|
| g vars, allocated first in the SOURCE10:58-67 order | SOURCE09:111-118 | G1 by absence; agrees statically with the oracle (SOURCE06:18-24) | — |
| m ↔ g∧g | SOURCE09:126-135 | definition | the conjunction |
| counter2 (G2, G3) | SOURCE09:41-57 | full equivalences | true prefix ≥1 / ≥2 |
| G2 clauses | SOURCE09:150-157 | G2; s2 ≠ None because items ≥ 5 | — |
| G3 c1 and singleton | SOURCE09:171-183 | G3; 6 literals | — |
| G5 | SOURCE09:184-187 | G5 | — |
| `--sym` units | SOURCE09:191-194 | as for A | — |
| ≥3 registers and output t | SOURCE09:60-89 | one-directional; true counts satisfy every implication; the first-item k=2,3 registers are forced false, which is their true value | true thresholds; t := [≥3] |
| OR of t | SOURCE09:202 | G4 | — |

**Cube block (SOURCE10:70-99):**

| Family | Lines | Reason |
|---|---|---|
| 18 signed units | SOURCE10:75-79 | hold after `--sym` plus residual normalisation (Link 6, F2); hold by construction in the transport |
| G6 (an absent predicate gives a unit) | SOURCE10:81-98 | derived from G1/G2 plus the units (SOURCE07:8-14; E5) |

`fix` and `--fix-json` are never invoked (SOURCE10:112, 119-121).

**No clause can exclude a genuine K3 configuration.** Only three families are not universal: the `--sym` units, the cube units and the lex block. Each holds for a named representative, either the normalised configuration or its lex-minimal orbit member.

## Link 10: ACCEPT-WITH-FIXES (m3, m4), conditional on G1–G2

- **Counts.** Each w_x ≥ 1: ψ_{x,p} is a unit vector and the meet point is zero by G1. The three neighbour sets are disjoint by G5 and lie within 6 cells. So w ≥ 4 forces exactly (4,1,1), and w_a ≥ 3 with w_b ≥ 2 forces exactly (3,2,1) (SOURCE01:oLF134-157; consistent with SOURCE03:33-35).
- **Transport.**
  - The maps at oLF142-146 send ℓ to row 0, p to (1,0), and the neighbour sets onto the canonical columns.
  - All 18 predicates then equal the C411 or C321 pattern, with the `--sym` units inside S_1.
  - The image is K3 (given m4), so H2 and H3 give every clause of the exact cube CNF. UNSAT of either encoder's CNF yields the contradiction.
  - No arbitrary-ONB or symbol-line transport is used (oLF159-161).
- **Cuts.**
  - At-most-three clauses express ¬(w_x ≥ 4).
  - Mixed clauses express ¬(R⊆N_x ∧ T⊆N_y) for disjoint R, T.
  - Since N_x∩N_y = ∅, the family is equivalent to w_x ≤ 3 ∧ ¬(w_x≥3 ∧ w_y≥2), which is exactly the excluded types.
  - Counts: 588·3·15 = 26,460 at-most-three clauses and 588·6·20·3 = 211,680 mixed clauses.
  - C1: there are 2,100 surjective local assignments, and 90 + 360 = 450 are excluded, matching inclusion–exclusion (SOURCE00:oLF187-188).
- **Validity.** The cuts are valid consequences once C321 and C411 are UNSAT. The argument is not circular, because the cuts never use C311.
- **Observation.** Logically, the accepted A_C321/A_C411 (SOURCE15:7-8) plus H3 already suffice. The B halves are decision-1 redundancy (SOURCE14:13). I am not suggesting a deviation.

## Link 11: ACCEPT-WITH-FIXES (m5, m6)

**Comparator lemma, any length.** Fix a generator σ. Let v_1 < … < v_n be the indices with σ(v) ≠ v, let x_i = X_{v_i} and y_i = X_{σ(v_i)}, and let e_1 ≡ ⊤. SOURCE11:57-68 emits:
- C_i = ¬e_i ∨ ¬x_i ∨ y_i, for i ≤ n;
- D_i = ¬e_i ∨ ¬x_i ∨ ¬y_i ∨ e_{i+1}, for i < n;
- D′_i = ¬e_i ∨ x_i ∨ y_i ∨ e_{i+1}, for i < n.

Claim: some assignment to e satisfies these clauses iff x ≤lex y.
- (⇐) Set e_i := [x_k = y_k for all k < i]. Whenever the premise of D_i or D′_i holds (e_i ∧ x_i = y_i), e_{i+1} is true. If e_i is true, then i ≤ j, the first differing position (if any), so x_i ≤ y_i and C_i holds.
- (⇒) Suppose the first difference j has x_j = 1 and y_j = 0. Induction through D/D′ forces e_1, …, e_j true, and then C_j fails.

Positions fixed by σ are equal in X and X∘σ, so skipping them does not change the comparison. The appended block therefore says exactly X ≤lex X∘σ. Each generator gets fresh prefix variables (SOURCE11:118-121), so the comparators are independent. The length-≤4 control (SOURCE11:72-86) is a special case.

**Representative.**
- Let Π = ⟨σ_1, …, σ_7⟩, where σ_i comes from `image` (SOURCE11:43-51), and let X0 be the canonical-C311 Gram pattern.
- The orbit {X0∘τ : τ ∈ Π} is finite and closed under ∘σ_i. Its lex-minimum X* therefore satisfies all seven comparators.
- By E3 (SOURCE06:39-43), each orbit element is the Gram pattern of the configuration moved by some element of H_311, so it is again a K3 triple.
- Every C311 generator fixes rows 0 and 1 and column 0, and maps columns {1,2,3} onto themselves. The combined generator swaps (square 2, column 4) with (square 3, column 5) and fixes column 6. So both the `--sym` units and the exact C311 pattern are preserved.
- X* therefore satisfies the strengthened A input:
  - H3 gives base ∧ cube ∧ G6;
  - Link 10 gives the cuts;
  - the lemma, with e_i := equal-so-far, gives the lex block.
- No involution is assumed.
- At clause level, the C311 generators map the base, cube, G6 and cut clause sets onto themselves. That is stronger than the base∧cube projection that E2 needs for C411 (SOURCE06:30-36).

## Link 14 and §3: ACCEPT-WITH-FIXES (m1, m2, m9), conditional

- **Case split.**
  - Links 3, 5 and 6 put every K3 triple into exactly one canonical cube.
  - C321 contradicts G1, and C411 contradicts G2, via Link 7.
  - In C311 the configuration satisfies B_C311 + cuts, and its lex-minimal orbit member satisfies lex A_C311 + cuts. Certified UNSAT of either input excludes it; decision 1 requires both.
  - As a cross-check, the C321 and C411 branches would also violate the cuts at (row 0, (1,0)).
- **§3 step 2, the (C0) argument.** The step is valid, and it uses both directions of (C0) (SOURCE03:12-13):
  - a non-classical t-set has a non-classical member;
  - any set containing that member is non-classical.

  Since t ≥ 3, there are two partners to pick. Orthogonality is pairwise by definition. The three squares are distinct, because no QLS(7) is orthogonal to itself: that would need 49 pairwise-orthogonal vectors in C^7. So M(7) ≤ 2 follows without the baseline M(7) ≤ 3.
- **Steps 3–4.** M(7) ≥ 2 is imported from the published non-classical pair (SOURCE00:oLF43-47, oLF264-265). Given all premises, M(7) = 2.

## Static cross-check

These are hand counts from SOURCE08–11. They check structure only, not bytes or hashes, and no verdict depends on them.

| Object | Vars | Clauses |
|---|---|---|
| A base | 96,978 (2,646 g + 92,610 h + 1,722 guards) | 627,398 |
| B base | 461,370 | 1,629,644 |
| + C311 units + G6 | 0 | +158 (18 + 2·70) |
| + lex, 7 C311 generators (10,542 moved predicates) | +10,535 | +31,612 |
| + cuts | 0 | +238,140 |

- A lex + cuts = 107,513 / 897,308, matching SOURCE00:oLF220.
- B + cuts = 461,370 / 1,867,942, matching oLF229.
- A original + cuts = 96,978 / 865,696. So the SOURCE14:27 headers are post-append headers.
- The guard count 1,722 = 41·42 shows `--sym` was active.
- Using all 22 generators would add 32,150 auxiliaries, so the A header corroborates F1.

## Probes that did not break the chain

- A light square in a K3 triple: yields a K2 triple, so it is excluded.
- Collinear G2, parallel-line G3 and absent-predicate G6 cases: all necessary conditions.
- Residual normalisation: preserves the `--sym` units.
- A non-stabilising lex generator on C311, such as C321's plain 4↔5: this would be unsound, but it is not used (F1, header count).
- Degenerate encoder branches: unreachable.

## Audited vs imported

**Audited here (static):**
- Link 3: the deduction.
- Link 7: every A and B clause family under the exact arguments, the cube/G6 block, canonical auxiliaries, and branch reachability.
- Link 10: the local counting, transport, cut equivalence and counts, and the C1 arithmetic.
- Link 11: the comparator lemma, H_311 invariance, and the representative.
- Link 14 and §3: the logic, including the (C0) step.
- The structural header arithmetic.

**Imported, not re-audited:**
- K1 and K2, with their trust bases (35-class caveat, Egan–Wanless tables).
- The Ball–Simoens definitions and set isotopy, on which (C0) rests, and Lemma 10's printed proof.
- Links 4–6 and the B-map oracle as accepted. I re-read them in passing and saw no defect.
- Every certificate status, and every SHA-256 together with its claimed construction:
  - d598507d and 2b92f5b1 as plain base ∧ cube ∧ G6 (supported by SOURCE15:12);
  - 18583aab as lex-C311 + block, and ae3b8309 as B_C311 + block;
  - block 05f31da4.
- The receipts and controls: C1, C4, AG(2,7), and Ψ(f).
- The published non-classical pair.
- The correctness of CaDiCaL and kissat (untrusted producers) and of drat-trim and CPython (trusted).
