# K3-COMPOSITION.r5: final hostile composition audit (Claude family)

**Conventions.**
- SOURCE00 and SOURCE01 are cited by the excerpt's own LF numbers.
  - r5 original LF = excerpt LF + 5 up to oLF422, and excerpt LF + 182 from oLF610.
  - AMENDMENT-4.r4 original LF = excerpt LF + 94, then excerpt LF + 272.
- This is a static reading only. I had no tools, so no SHA-256 was recomputed. Hashes were compared as strings across the sources and agree wherever they are cross-referenced.
- No gate, priority or novelty authority is exercised here.

## Disposition: COMPLETE-COMPOSITION ACCEPT-WITH-FIXES (0 FATAL, 0 MAJOR, 7 MINOR)

**Explicit answer: yes.** The bridge re-derived below, applied to the supplied accepted premises, establishes K3 nonexistence and M(7) = 2. The premises are:
- K1 (SOURCE16:5) and K2 (SOURCE12:5-6);
- Links 4–6 (SOURCE13:9-11);
- H3 (SOURCE19:3-8);
- G1 (SOURCE17:3) and G2 (SOURCE18:5);
- both strengthened C311+cuts exact-CNF verdicts (SOURCE20:5; SOURCE21:5).

The consequence is that no MOQLS(7) triple has three non-classical squares. With K1 and K2, every MOQLS(7) triple is classical, and M(7) = 2. This holds at the existing M7 exact-CNF standard and inherits its full trust base.

No substantive mathematical prerequisite remains. Two procedural items remain:
- the other-family final review (SOURCE00:386);
- the parent's decision-8 verdict (SOURCE14:35), which alone can move Link 14 off PENDING (SOURCE00:354-355).

All seven fixes are wording, status or import-listing items for that verdict. None changes a CNF, a proof, a status or an inference.

## Per-link verdicts

### Link 3 (minimality ⇒ G4): ACCEPT

- **Every K3 triple is minimal.** By (C0) and K1/K2, every non-classical triple has exactly three non-classical members, so every K3 triple attains the minimum. No compactness argument is needed (SOURCE02:63-64; SOURCE00:98).
- **Lemma 10 as written is self-contained and correct** (SOURCE03:54-67).
  - An entry whose support meets {a,b} in exactly one coordinate has a nonzero inner product with every entry supported on {a,b}.
  - So every zero inner product involving a transformed entry is with an entry of equal support (moved by the same U) or of disjoint support. Either way it stays zero.
  - Norms are kept, so rows and columns stay ONBs. The number of weight-two entries strictly decreases, so the process terminates.
  - Every tensor-product zero keeps its zero factor, so both partners are preserved at once (SOURCE03:63-64).
  - A global unitary on the chosen square alone fixes its Gram matrix (SOURCE03:65-66).
  - The new square is distinct from both partners, since no QLS(7) is self-orthogonal. The result is a triple with exactly two non-classical squares, which contradicts K2.
- **Own-line reading.** Take B to be the ONB of an own line ℓ. Entries on ℓ have weight 1, so the heavy witness lies off ℓ, with weight #{r∈ℓ : g(p,r)} ≥ 3 (SOURCE02:59-60). This holds for all 3 squares × 14 lines.
- **Later images.** Every later image (`--sym`, residual normalisation, transport, H_311 orbit) is again a K3 triple, so G4 holds for it directly.

### Link 7 (H3): ACCEPT

H3's hypotheses (SOURCE19:8) are now supplied by Links 3, 5 and 6. I re-checked the code directly; the H3 text of record is not in this snapshot.

**Encoder A, `build(3, None, True, True, None)`:**
- The h definitions are full equivalences (SOURCE08:75-86).
- G2 zero, one and collinear clauses hold by frame consistency once h is set to its conjunction (SOURCE08:91-99).
- G3 cover and singleton clauses (SOURCE08:100-114) are valid. The transition matrix is unitary, the meet entry is 1, and on parallel lines the collinear positions are G1 zeros.
- G5 holds (SOURCE08:115-118).
- Each guard emits 15 four-subset clauses, which is exactly "≥3 of 6" (SOURCE08:45-51). Canonical value: w := [≥3 neighbours]. The OR of guards (SOURCE08:137) holds by G4.

**Encoder B, `--squares 3 --heavy --sym`:**
- The m definitions are full equivalences (SOURCE09:126-135).
- `counter2` implements n1 ↔ a1∨x and n2 ↔ a2∨(a1∧x) (SOURCE09:41-57).
- `counter_ge3` emits only the implications v → prev[k] ∨ (x ∧ prev[k−1]). The first-item k = 2, 3 registers are forced false, which is their true value (SOURCE09:73-88).
- Canonical values are the true prefix thresholds, with t := [≥3].

**Degenerate branches.** In production the list sizes are:
- G2: 7 − |{columns of p, q}| = 5 or 6 items;
- G3: 6 candidates (parallel lines lose one collinear point; perpendicular lines lose the meet point);
- G4: 6 candidates at each of the 42 off-line points.

So SOURCE08:48, 106, 132-133, 137 and SOURCE09:65, 148, 151 (a `None` literal when s2 = None; SOURCE19:13), 169 are unreachable. No empty clause or `None` literal is emitted. No diagonal G(a,p,p) is ever queried, and `fix`/`--fix-json` are never used (SOURCE10:112, 119-121).

**Variable maps.** Both encoders allocate the g variables first, in (square, earlier cell, later cell) order, skipping common lines (SOURCE08:66-71; SOURCE09:113-118). That equals `variable_map()` (SOURCE10:58-67). Agreement is asserted at runtime for A (SOURCE10:115) and confirmed for B by the oracle (SOURCE06:18-24).

**Cube block.** 18 signed units (SOURCE10:75-79) plus G6 (SOURCE10:81-98). Each singleton gives 70 clauses: 10 + 10 units and 25 equivalences. That matches +158 and +88 (SOURCE00:522-524), and G6 is redundant by SOURCE07:5-14.

### Link 10 (transport ⇒ cuts): ACCEPT

- **Local count.**
  - w_x ≥ 1, because ψ_{x,p} is a unit vector in ℓ's ONB.
  - The cell of ℓ on p's other line is zero by G1, leaving six cells.
  - The neighbour sets are pairwise disjoint by G5, so Σw ≤ 6.
  - Hence w ≥ 4 forces exactly (4,1,1), and w_a ≥ 3 with w_b ≥ 2 forces exactly (3,2,1) (SOURCE01:40-47, 60).
- **Transport.**
  - The maps are: transposition if ℓ is a column; ρ (ℓ → 0, row of p → 1); κ (column of p → 0, neighbour sets onto canonical columns); square relabelling. Because all six cells are used, κ is a bijection.
  - The image is a genuine triple with unchanged ray sets, so it is again K3 (SOURCE03:9-11; SOURCE00:218-220). G4 holds by Link 3, the `--sym` units lie in S_1, the exact C411/C321 signed units hold, and G6 holds.
  - So the image satisfies A_C411 and B_C411 (or the C321 pair) with canonical auxiliaries, which contradicts G2 (or G1).
- **No circularity.**
  - The gate inputs are base ∧ cube only. Their headers 627,486 / 1,629,732 / 627,556 / 1,629,802 are base + 88 or + 158 (SOURCE00:533-536), and these are exactly the formulas named in SOURCE17:8-9 and SOURCE18:9-10.
  - G4 itself uses only K1 and K2.
- **Exact family.**
  - At-most-three clauses ≡ ¬(w ≥ 4). Mixed clauses ≡ ¬(R⊆N_x ∧ T⊆N_y); R and T can be taken disjoint by G5.
  - Counts: 14·42·3·C(6,4) = 26,460 and 14·42·6·C(6,3)·C(3,2) = 211,680, so 238,140 in all.
  - C1 arithmetic: 2,100 = 4⁶ − 3·3⁶ + 3·2⁶ − 1, and 450 = 3·15·2 + 6·20·3 (SOURCE00:227-228).
- **Condition met.** The condition at SOURCE00:237-239 (G1, G2, Link 7, Link 3) is now satisfied.

### Link 11 (lex representative): ACCEPT

- **Generators.** SOURCE11:25-34 yields exactly the seven H_311 generators (SOURCE00:246-248).
  - All of them fix rows 0 and 1 and column 0, and map columns {1,2,3} onto themselves.
  - The combined operation swaps (square 2, column 4) with (square 3, column 5) and fixes column 6.
  - So C311's 18 signed units, the `--sym` units, and the (square 1, row 0) G4 exemption are all preserved.
- **Representative.**
  - Every τ(C) with τ ∈ H_311 is a genuine K3 triple satisfying the `--sym` and C311 units. So base ∧ cube ∧ G6 hold for it (Link 7), and the cuts hold (Link 10). Structural invariance of the cuts is not even needed.
  - X∘σ is the Gram pattern of σ⁻¹(C) (E3, SOURCE06:39-43), and σ⁻¹ lies in the group.
  - The finite orbit of patterns is closed under each ∘σ_i, so its lex-minimum X* satisfies X* ≤lex X*∘σ_i for every i.
  - Only this one member is claimed, not every representative (SOURCE00:249, 349-350; SOURCE04:33-37).
- **Comparator.**
  - Both directions re-derived from SOURCE11:54-69 as at SOURCE00:257-266. Fixed positions are skipped.
  - Prefix variables are fresh and start above the old variable count (SOURCE11:116-121), so they never clash with base auxiliaries.
  - Moved predicates: 1,386 per simple swap (3·(882 − 420)) and 2,226 for the combined operation (462 + 1,764). That gives 6·4,156 + 6,676 = 31,612 clauses and 6·1,385 + 2,225 = 10,535 auxiliaries (SOURCE00:525-527).
  - The 340 truth tables (Σ4ⁿ, n ≤ 4) are corroboration only.

### Link 14 (composition): ACCEPT (fixes concern reporting only)

- **Exhaustive cover.** The cover is exhaustive: 18 = 64 − 54 + 8 assignments in three disjoint orbits of six (SOURCE10:31-55).
- **C321 and C411.** A C321 configuration contradicts G1; a C411 configuration contradicts G2.
- **C311, B side.** The configuration itself satisfies ae3b8309… (461,370 vars / 1,867,942 clauses).
- **C311, A side.** X* satisfies 18583aab… (107,513 / 897,308) (SOURCE00:539, 541; SOURCE20:7; SOURCE21:7; SOURCE22:7-8).
- **A+B standard.** Either UNSAT suffices logically. Decision 1 requires both, and both are met.

**Original quantifiers are retained:**
- arbitrary complex unit vectors, with no field, tolerance or numerics;
- all non-classical triples;
- G4 on all 3 × 14 lines;
- all 14 × 42 frame/point pairs and every role assignment;
- all 18 residual assignments;
- every orbit.

## (C0), t ≥ 3, and the lower bound

**(C0).** C0 (SOURCE03:8-14) is correct under the imported convention: entry phases, simultaneous row/column permutations, and a separate unitary per square (SOURCE00:636-638). Individual classicality means "exactly 7 rays", a property invariant under every isotopy move and every cell permutation.

**§3 step 2** (SOURCE00:362-364):
- It uses only "all members classical ⇒ set classical", which needs the per-square unitary, to obtain a non-classical member.
- That member plus any two others is a mutually orthogonal triple (orthogonality is pairwise) with at least one non-classical member. K1, K2 or K3 excludes it directly.
- So M(7) ≤ 2, and the baseline bound ≤ 3 is not used.

**§15** (SOURCE00:615-626) checks out arithmetically:
- H = {1,2,4}, f0 = (0,1,2,0,4,0,0), and f0 − mx is a permutation exactly for m ∈ {2,6}.
- f = (0,6,5,1,3,4,2) and f − 4x = (0,2,4,3,1,5,6).
- f is not affine: f(3) = 1 ≠ 4.

At q = 7, Lemmas 12–14 also follow from the character-sum fact at SOURCE00:628-629:
- rows and columns are orthonormal, because jx and f are permutations;
- the Φ(4) product inner product reduces to Σω^{(k−i)(f(x)−4x)} = 0;
- ψ_{1,0} ∝ Σω^{f(x)}|x⟩ is parallel to a row-0 vector Σω^{jx}|x⟩ only if f is affine, so there are at least 8 rays and Ψ(f) is non-classical.

This corroborates the import; it does not replace it.

## Findings (all MINOR)

| ID | Where | Issue | Concrete fix |
|---|---|---|---|
| m1 | SOURCE17:16 vs SOURCE00:105-108, 387-389 | The G1 verdict calls Links 3 and 5–7 "accepted". r5 keeps Link 3's K3 application, the Link 10 transport and Link 11 PENDING composition review. | The final verdict records those three as accepted by the composition reviews, and reads SOURCE17:16 as anticipatory. |
| m2 | SOURCE00:633-656 | The "complete" import list omits three items:<br>• fidelity of block 05f31da4 to the family in SOURCE01:73-79 (the k3_cuts_r1/r6 code is not in this snapshot);<br>• the appender and regeneration drivers that define 18583aab and ae3b8309 (only CPython is listed, 654-655);<br>• a hash for the decision-6 source-review PASS (SOURCE14:33). | List them as reviewed premises. Basis: SOURCE14:10, SOURCE00:227-231 and 598-601, and the pure-append arithmetic at 545-547. |
| m3 | SOURCE24:161; SOURCE00:525-527 | The 10,535 / 31,612 header equally fits six simple swaps plus C411's combined 5/6 + 2/3 (also 2,226 moved predicates). The header does not identify H_311. | Rest generator identity on SOURCE11:28-29, metadata 7bef0b78 (SOURCE00:272) and the unit-preservation control (SOURCE11:93-98). |
| m4 | SOURCE18:23; SOURCE22:97 | The B_C411-p3 and B_C311cuts-p2 solver logs share the SHA bde6e1ee…a162 (16 B). This is expected, since under `-q` the log is exactly `s UNSATISFIABLE\n`. It is neither a copy error nor evidence of run identity. | Note this. Run binding rests on the receipt and driver hashes (SOURCE22:14-53, 60-92). |
| m5 | SOURCE00:313 vs 319 | "Result: PRODUCER" sits beside the ACCEPTED status. | Relabel it "Producer result (evidence only)". |
| m6 | SOURCE00:398-401 vs 289, 474 | The path-only-delta erratum lists r6 and r7. A attempts 4–5 ran under r8 and r9, and this excerpt cites no parent PASS for them. Non-contributing, because Link 12 rests on A_C311cuts-p2. | Cite the PASS records, or point to the omitted §6. |
| m7 | SOURCE00:362-364; 229 | Two things are left implicit: that step 2 uses only C0's per-square-unitary direction, and that the chosen members are distinct. Separately, the classical AG(2,7) cut control is near-vacuous, because every local weight is 1. | Add one sentence for each. State that the block's semantic evidence is C1 plus the AMENDMENT-4 reviews. |

**Carried-forward errata (unchanged, correctly handled):** the false "Both logs are empty" template lines (SOURCE00:416-423), and the A-audit 466/475 label (SOURCE00:424-426; SOURCE21:24).

## Reconciliation with earlier reviews and statuses

**Codex (3 MINOR)** (SOURCE23:9-38; r2 fix map SOURCE00:436-438):

| Fix | Applied in r5 |
|---|---|
| F1 | SOURCE00:246-252, 349, 404-405 |
| F2 | SOURCE00:150, 157-159, 408-409 |
| F3 | SOURCE00:154-156, 406-407 |

**Claude (9 MINOR)** (SOURCE24:24-37; r3 fix map SOURCE00:451-459):

| Fix | Applied in r5 |
|---|---|
| m1 | SOURCE00:349-350 |
| m2 | SOURCE00:341 |
| m3 | SOURCE00:237-239, 343 |
| m4 | SOURCE00:218-220, 410-412 |
| m5 | SOURCE00:253-256 |
| m6 | SOURCE00:257-266 |
| m7 | SOURCE00:160-164 |
| m8 | SOURCE00:413-415 |
| m9 | SOURCE00:376-378, 635-645 |

All are applied, and none changed the logic (SOURCE00:445-446, 509-510, 683-685).

**The four conditions of the Claude note (SOURCE24:14-18) are now met:**
1. G1 (SOURCE17);
2. G2 (SOURCE18);
3. the A strengthened replay (SOURCE20);
4. the B strengthened replay (SOURCE21-22).

The trust base is inherited.

**Chronology is consistent:**

| Event | Time |
|---|---|
| H3 verdict | 08:06:03 |
| r4 | 08:21:45 |
| G1 verdict | 08:36:51 |
| G2 verdict | 10:57:25 |
| A-cut verdict | 11:06:26 |
| B raw audit | 12:08:22 |
| B-cut verdict | 12:09:07 |
| r5 frozen | 12:14:21 |

## Imports, observed evidence and residual limitations

**Imported mathematics:**
- The Ball–Simoens definitions: product-form orthogonality, and set isotopy with a per-square unitary. The case split and step 2 depend on that convention.
- Lemma 10, although LEMMAS.md:54-67 is a complete argument and was checked above.
- The lower bound (Corollary 7, or Huang–Li Theorem 5.2), re-derived at q = 7 above.
- K1 and K2 as accepted computer-assisted theorems, and through them the Egan–Wanless tables, which parent enumerations corroborate (SOURCE16:29-32; SOURCE12:25).
- Fidelity of the cut block and the appender (m2).
- The B-map oracle (SOURCE06:18-24), which my static allocation check corroborates.

**Observed finite evidence** (recorded in receipts and audits, not re-observed here). Six parent replays, each with rc 20/0 and singleton exact status lines:
- A_C321 and A_C411: same CaDiCaL binary as the producer; CNF feeds were pre-hashed buffers (SOURCE15:7-14).
- B_C321-a3 (SOURCE17:11).
- B_C411-p3: 1,072,845,839 proof bytes (SOURCE18:14-20).
- A_C311cuts-p2: 705,539,296 proof bytes; raw logs 16/475 B (SOURCE20:7-16).
- B_C311cuts-p2: 842,063,946 proof bytes; raw logs 16/478 B; 43 conditions and 39 parent predicates, none failed (SOURCE21:7-13; SOURCE22:13-59).

These reused controls were not rerun (SOURCE00:587-603):
- coverage;
- G6;
- lex comparators;
- 26/26 matched component controls;
- transport r2;
- no-duplicate regeneration;
- the B-map oracle (0 of 2646 differ);
- cut controls C1 (450 of 2100), classical (0 violations) and Ψ(f) (2940, 0);
- appender C5–C8;
- supervisor;
- desk self-checks.

**Residual limits that must remain attached:**
- *Proof provenance.*
  - No proof was retained or digested, and no producer–replay proof identity is claimed.
  - The equal counts 1,072,845,839 and 842,063,946 are not identity (SOURCE00:575-579; SOURCE21:12).
  - The M7 protocol needs no proof-stream digest. It is not n8's protocol, and n8 is not substituted (SOURCE00:582-583; SOURCE22:129).
- *A-side checker log.* It is 475 B raw. The 466 B figure is the CR-stripped count (9 CRs removed), mislabelled as raw.
- *Toolchain trust.*
  - The solvers are untrusted.
  - The drat-trim builds, CPython, the compiler, macOS and the hardware are trusted.
  - There is no Lean verification and no human peer review, and the 2026 sources are unrefereed (SOURCE16:75-78).
- *K2's 35-class caveat, verbatim* (SOURCE12:54).
- *Controls.*
  - The matched controls ran after K2 production (SOURCE12:51-52; SOURCE00:594).
  - README:91 is applied at component level only; no genuine K3 positive control is possible (SOURCE14:14-20; SOURCE00:605-607).
- *Non-contributing attempts.* All UNKNOWN and NOT_STARTED attempts, and the UNKNOWN first audit attempt, stay non-contributing (SOURCE00:647-673; SOURCE22:132-136).

## Correctness versus priority

This audit addresses correctness only. The bounded NONE-FOUND-IN-SCOPE priority screen comes from K1 and was inherited by K2 (SOURCE12:8); it covers neither K3 nor M(7). Novelty, significance, and lifting the "never claim M(7)" guidance (SOURCE16:66-68) remain for the parent, after a fresh priority screen.
