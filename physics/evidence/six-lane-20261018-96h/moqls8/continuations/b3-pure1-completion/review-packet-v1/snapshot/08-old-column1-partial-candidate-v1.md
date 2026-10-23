# PURE corner subfamily: structure lemmas, an exact partial assignment and the remaining obligation — CANDIDATE v1

Frozen at 2026-10-19T18:21:21-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `0481f24b0e0dc75321220584d7e5db2914589db5c1749a723621040e3e14d99a`). Status: CANDIDATE written mathematics, not reviewed. No candidate is a premise; every fact is re-proved here or in the frozen working notes [N] (`/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure-corner/WORKING-NOTES-v1.md`, SHA256 `0f4b807526652878090102e9875879a01e75dd8709c2e19e13f0ea66399f0f06`), whose lemmas are restated below with proofs. No script, assertion, enumeration or numerical check was used. All verification is by hand.

**Outcome: NOT EXCLUDED; EXACT PARTIAL ASSIGNMENT PLUS REMAINING OBLIGATION.**
- The subfamily PURE (at least one pure-A corner cell (r,c) of square 1, with r ∈ {1,7} and c ∈ {1,2,3}) is not decided.
- Proved structure: Lemma W (general B3), and Lemmas P1, P2, P3, T.
- For the column-1 case, an explicit partial assignment of rows 0 and 1 of all five squares, together with the column-0 entries at rows 6 and 7, satisfies every direct equation among the assigned cells, as checked by hand in section 4. So no contradiction can come from those cells alone.
- For c ∈ {2,3}, the structure lemmas hold, but no assignment is given and no decision is made.
- No B3 no-go, no Boolean/GB/n=8 claim, no novelty claim.

## 1. Hypotheses and basics (re-proved)

- **H1.** Genuine pairwise-orthogonal QLS(8), Q_1,...,Q_5 ([PRIM] LF195-225). Rows and columns are ONBs, and for distinct cells x, y and distinct squares s, t, <Q_s(x),Q_s(y)><Q_t(x),Q_t(y)> = 0. This holds because {Q_s(x)⊗Q_t(x)}_x is orthonormal and all vectors are unit.
- **H2.** Q_s(0,c) = w_{s,c}e_c.
- **H4 (part, template [J]).** q^1, q^7 ∈ V_A have full support {1,2,3}, and q^6 has support {2,3}. Square 1's column 0 is orthonormal.
- H3 (SB2) is not used in the lemmas. The assignment of section 4 happens to satisfy it.

Notation: q^k := Q_1(k,0), q_s^k := Q_s(k,0), Q := Q_1. Also r ∈ {1,7}, r' := the other element, and W := {4,5,6,7}.

The facts (F1), (F2) (common and own index), (AX) and the corner lines (L), with ℓ_{r,c} = conj(a^r) × e_c, are proved in [N] N0. They are restated here:
- (F1) coordinate c and own index i are absent at (i,c);
- (F2) at most one square uses a given coordinate d != c, or a given own index k != i, at (i,c);
- (AX) for s >= 2, q_s^r ⊥ V_A ⊕ span{e_0}, and q_s^6 ⊥ e_0, e_2, e_3;
- (L) P_A Q(r,c) ∈ span{ℓ_{r,c}}, supp ℓ_{r,c} = A \ {c}, and <ℓ_{r,c},ℓ_{r,c'}> = −a^r_{c'} conj(a^r_c) (c != c'), <ℓ_{1,c},ℓ_{7,c'}> = −a^1_{c'} conj(a^7_c), all nonzero.

## 2. Lemma W (rows 1 and 7 of squares 2..5 are single basis vectors; all of B3)

For s ∈ {2,..,5} and r ∈ {1,7}, q_s^r = ω e_{π_s(r)}, where π_·(r) : {2,3,4,5} → W is a bijection. Also π_s(1) != π_s(7).

*Proof.*
- By (AX) and column-0 orthonormality, q_s^r ∈ span{e_4,...,e_7}.
- For s != t >= 2, H1 at (r,0) and (0,d) gives <e_d,q_s^r><e_d,q_t^r> = 0. So the four supports are nonempty and pairwise disjoint in the 4-set W, hence singletons forming a bijection.
- q_s^1 ⊥ q_s^7 gives π_s(1) != π_s(7).
QED

## 3. Lemmas for a pure-A corner (r,c): Q(r,c) = ω ℓ̂_{r,c}

**P1 (row r; proof in [N] N1).**
- The partner (r',c) is A-free.
- Row r of square 1 has exactly two A-carrying cells, (r,c) and (r,c*) with c* ∈ W. Here Q(r,c*) = ω' m, where m is the unit vector of P_r orthogonal to ℓ_{r,c}, of full support.
- The other five cells form an ONB of span{e_0,e_4,...,e_7}.
- The A-support excess of squares 2..5 in row r is at most 1.
- For c = 1, ℓ ∝ q^6 and m ∝ q^{r'}. For c ∈ {2,3}, both Q(r,c) and m have nonzero coefficients on q^6 and on q^{r'}.

**P2 (purity at (r,c*); proof in [N] N2).** Q_s(r,c*) = ω e_{d_s} for s >= 2, where the d_s are distinct and {d_s} = {0} ∪ W \ {c*}.

Sharpened with Lemma W and (F2)-own: d_s ∉ {π_s(r), π_s(r')}.
- d_s != π_s(r) by row orthogonality.
- Square 1 uses own index r' at (r,c*), because <q^{r'},m> != 0 (m ∝ q^{r'} for c = 1, and m has a nonzero q^{r'}-coefficient for c ∈ {2,3}). So by (F2)-own, <q_s^{r'},e_{d_s}> = 0.
- For c ∈ {2,3}, square 1 also uses own index 6 there, so additionally <q_s^6,e_{d_s}> = 0.

**P3 (column c; proof in [N] N3).**
- The other cells of column c carry A-parts only on n_c, the unit vector of span(A \ {c}) orthogonal to ℓ_{r,c}, with total mass 1.
- For c ∈ {2,3}, the corner (6,c) is A-free.

**T (column-1 twins; c = 1).** Q(r,1) = ω q^6 and Q(r,c*) = ω' q^{r'}, so Q_s(r,1) ⊥ q_s^6 and Q_s(r,c*) ⊥ q_s^{r'} for s >= 2. Proof: H1 on (r,1),(6,0) and on (r,c*),(r',0). Neither pair shares a line, and |G_1| = 1 on both.

## 4. Exact partial assignment (column-1 case: r = 1, c = 1, c* = 4)

Vectors are given in the standard basis; e_d denotes a basis vector. Square 1's A-block:

    q^1 = (e_1 + e_2 − e_3)/√3,  q^6 = (e_2 + e_3)/√2,  q^7 = (2e_1 − e_2 + e_3)/√6.

These are orthonormal, with supports {1,2,3}, {2,3}, {1,2,3} as in the template.

**Assigned cells.**
- Row 0 of every square: e_c at column c (H2 with w = 1).
- Column 0 at rows 0, 1, 6, 7 of every square.
- The whole of row 1 of every square.

| square | col 0 r0 / r1 / r6 / r7 | row 1, columns 1..7 |
|---|---|---|
| 1 | e_0 / q^1 / q^6 / q^7 | q^6, e_0, e_4, q^7, e_6, e_7, e_5 |
| 2 | e_0 / e_4 / e_6 / e_5 | e_7, e_1, e_0, e_6, e_3, e_5, e_2 |
| 3 | e_0 / e_5 / e_1 / e_4 | e_6, e_3, e_2, e_7, e_0, e_1, e_4 |
| 4 | e_0 / e_6 / e_4 / e_7 | e_0, e_4, e_7, e_5, e_1, e_2, e_3 |
| 5 | e_0 / e_7 / e_5 / e_6 | e_4, e_6, e_5, e_0, e_2, e_3, e_1 |

**Direct equations checked by hand (all and only those among assigned cells).**
- **(i) Row 1 ONB in each square.**
  - Square 1: {q^1, q^6, q^7} is an ONB of V_A, and the other five vectors are e_0, e_4, e_5, e_6, e_7.
  - Squares 2..5: the eight entries are the eight distinct basis vectors: {4,7,1,0,6,3,5,2}, {5,6,3,2,7,0,1,4}, {6,0,4,7,5,1,2,3}, {7,4,6,5,0,2,3,1}.
- **(ii) Column-0 orthonormality on rows {0,1,6,7}.** Distinct basis vectors for s >= 2; for square 1, e_0 ⊥ V_A and the triple is orthonormal.
- **(iii) Column orthogonality between rows 0 and 1, i.e. (F1).** No square has e_x at (1,x).
  - Square 1's (1,1) = q^6 has no e_1, and (1,4) = q^7 ∈ V_A.
  - Squares 2..5, by column: col 1 {7,6,0,4}, col 2 {1,3,4,6}, col 3 {0,2,7,5}, col 4 {6,7,5,0}, col 5 {3,0,1,2}, col 6 {5,1,2,3}, col 7 {2,4,3,1}.
- **(iv) H1 for every pair of distinct assigned cells sharing no line.** Such pairs are of the types ((0,d),(k,0)), ((0,d),(1,x)), ((0,0),(1,x)), ((k,0),(1,x)) with k ∈ {6,7}. Within each type, the products reduce to the following disjointness conditions (with ω = 1):
  - **(iv-a) Column-0 supports per row are pairwise disjoint over the five squares.**
    - Row 1: {1,2,3}, {4}, {5}, {6}, {7}.
    - Row 6: {2,3}, {6}, {1}, {4}, {5}.
    - Row 7: {1,2,3}, {5}, {4}, {7}, {6}.
  - **(iv-b) Supports at each row-1 cell are pairwise disjoint (squares 1..5), including coordinate 0.**
    - (1,1): {2,3}, 7, 6, 0, 4.
    - (1,2): 0, 1, 3, 4, 6.
    - (1,3): 4, 0, 2, 7, 5.
    - (1,4): {1,2,3}, 6, 7, 5, 0.
    - (1,5): 6, 3, 0, 1, 2.
    - (1,6): 7, 5, 1, 2, 3.
    - (1,7): 5, 2, 4, 3, 1.
  - **(iv-c) Own index 6 (G_s = <q_s^6,Q_s(1,x)>).** Nonzero only for: square 1 at (1,1); square 4 at (1,2) (e_4 = q_4^6); square 5 at (1,3) (e_5); square 2 at (1,4) (e_6); square 3 at (1,6) (e_1). Each cell has at most one nonzero. Square 1's values vanish off (1,1), because q^6 ⊥ q^7 and q^6 ⊥ Z⊕W.
  - **(iv-d) Own index 7 (G_s = <q_s^7,Q_s(1,x)>).** Nonzero only for: square 1 at (1,4); square 5 at (1,2) (e_6 = q_5^7); square 4 at (1,3) (e_7); square 2 at (1,6) (e_5); square 3 at (1,7) (e_4). At most one per cell. Square 1's values vanish off (1,4).

  Pairs sharing a row or column need no H1 check: their products vanish by (i)–(iii).

**Consistency with the lemmas.**
- P1: (1,1) = q^6 and (1,4) = q^7 are pure-A; (7,1) is unassigned and must be A-free.
- P2: d = (6,7,5,0), and d_s ∉ {π_s(1), π_s(7)}.
- T: Q_s(1,1) ⊥ q_s^6 and Q_s(1,4) ⊥ q_s^7.
- Lemma W: π(1) = (4,5,6,7) and π(7) = (5,4,7,6).

**This is NOT a full-grid witness.** Rows 2..7 (interior), column 0 at rows 2..5 (template: q^2, q^3 ∈ V_B and q^4, q^5 ∈ V_C dense), and all equations involving them are unassigned and unchecked.

## 5. Precise remaining obligations

1. **Column-1 case.** Decide whether the assignment of section 4, or any assignment with the same lemma structure, extends. The extension must satisfy:
   - square 1's column-0 rows 2..5 per the template;
   - rows 2..7 of all squares (ONBs);
   - all column ONBs;
   - H1 for all remaining cell pairs.

   Forced next constraints already proved:
   - (7,1) is A-free (P1);
   - column 1's other A-parts lie on v ⊥ q^6, with mass 1 (P3);
   - column 4's A-parts are orthogonal to q^7 below row 1;
   - squares 2..5 must place their A-mass 3 in row 7 (AX), with A-slot excess at most 6 − σ_1^A(7), where σ_1^A(7) >= 4.
2. **Columns 2 and 3 (pure-A at (r,2) or (r,3)).** Lemmas W, P1, P2 and P3 apply, with the extra own-6 exclusion in P2. No assignment and no decision; this is the analogous problem.
3. Any exclusion must use cells outside those of section 4.

## 6. Sources

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [N] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure-corner/WORKING-NOTES-v1.md`, SHA256 `0f4b807526652878090102e9875879a01e75dd8709c2e19e13f0ea66399f0f06`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure-corner/SCOPE-FREEZE-v1.json`, SHA256 `0481f24b0e0dc75321220584d7e5db2914589db5c1749a723621040e3e14d99a`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-B3-pure-corner-transition-v1.json`, SHA256 `237d4763931fa7d38b352d667d6b19e6ab6bd5e44b04d6d1e66d442b2adb26ea`.
- [ERR-AZ] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-az-corner/B3-AZ-CORNER-PURITY-CANDIDATE-v1-erratum-1.md`, SHA256 `a0c9b96044896817d2f2730749d218138d61d7a192ee78939e422382f5f31069`.
