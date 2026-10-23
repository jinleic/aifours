VERDICT: ACCEPT-WITH-FIXES

Line numbers are 1-based over the inlined candidate text, counting blank lines. Each finding also quotes an anchor in case the file's wrapping differs.

## FATAL

None.

## MAJOR

None. I checked every load-bearing implication in §§2–6 by hand, and no preservation lemma is missing. The composite move ab is covered in two ways: by the direct setwise check at L92, and by closure of Lemma-2 moves under composition ([BR] Proposition, last sentence).

## MINOR

**m1. §1 L9, L20, L33 — quantifier and hypothesis attribution.**
- L33 reads existentially: "There is a genuine normal-form configuration Q'…". The §6 contradiction at L119 needs the universal form. Corrected scope: "For the arbitrary Q of §1, a single move (σ,ρ,τ) ∈ {id,a,b,c,ab} gives Q' with …".
- L9 calls items 1–4 "accepted U/T16 normal-form hypotheses". Item 3 is actually the template-conditioning hypothesis of [E] E2/N1. U/T16 itself is accepted only conditionally ([E] N1). Reword accordingly.
- Item 4 (ROWLEX) follows from item 3, because the template rows are already sorted. The proved exclusion therefore does not depend on ROWLEX. Say so.

**m2. §2 L44–L58 — wording of the count.**
- L56 says "If three … were non-permutation"; it should say "at least three".
- The "+7" at L58 needs a reason: it is the row-(A) lower bound for the remaining square, whether or not that square is a permutation. Without this, the case where all four are non-permutation is only implicit.
- (B) at L46 silently uses ⟨0|Q_s(i,0)⟩=0. That is what makes the inner product a sum over common support in {1..7}. State it.
- The column halves of (A) and (B) are not load-bearing. The 7-ones case already closes with row-(B).

**m3. §5 L111–L113 — licence for re-applying necessity.**
- [G]'s necessity bullet is phrased for configurations "already in the accepted U/T16 normal form". Applying it to the moved Q' is licensed, but the licence should be cited explicitly:
  - [G] bullet 3: moves preserve row-0 form, SB2, the Q1 witness, the SAME template and ROWLEX.
  - [G] bullet 4 ("Consequently…") and [E] N6 item 1, which already apply necessity to moved configurations.
- L113 lists only G2–G5 and P4. Add the TRUE unit and row/column constants, and the SB2 unit family restored at L82, so the list matches "complete GB base".
- This is wording only; the import scope is unchanged.

**m4. §1 L31 — "they are not GA's offset-by-one IDs".** No inlined source says GA's convention is offset-by-one. [D] §3 item 6 says only that no GA IDs are translated by offsets. Delete the phrase or pin a source. It is non-load-bearing.

**m5. §4 L107 — "preserve the block partition… cannot mix".** This is true for ⟨a,b,c⟩, but coverage never uses this orbit statement. Mark it non-load-bearing. It does not show that H_23 and H_24 are inequivalent under all symmetries, and it does not allow dropping either one. Both remain required.

**m6. L5, L121, L132/L141 — unverified status claims.** These are "three surviving GB UNKNOWNs and GB15/18", "B3.M2 UNKNOWN" and the [SCOPE] authorization. Their sources are not inlined and I did not verify them. Treat them as unverified metadata, outside the reduction.

## Audit of requested checks (no further findings)

1. **Nine-ones lemma and two permutation supports.** The lemma is correct.
   - With 7 ones, row-(A) forces singleton rows and row-(B) forces distinct columns.
   - With 8 ones, the single degree-2 row must avoid six isolated columns, which is impossible.
   - X_1 has 3+2+2+2+2+2+3 = 16 ones, matching [J].
   - (C) caps the total at 49, but three or more non-permutation squares force at least 50.
   - So two permutation supports coexist in the SAME configuration. This is self-contained and agrees with [E] N2.

2. **Label maps and ρ/τ.** From τ(s)=σ(s+2)−2: a gives (2 3), b gives (4 5), c gives (2 4)(3 5), ab gives (2 3)(4 5). Also ab=ba with ρ=id. Each table row checks:

   | Labels | Move | New labels | Squares |
   |---|---|---|---|
   | {6,7} | c | {4,5} | {4,5}→{2,3} |
   | {4,7} | b | {4,6} | {2,5}→{2,4} |
   | {5,6} | a | {4,6} | {3,4}→{2,4} |
   | {5,7} | ab | {4,6} | {3,5}→{2,4} |
   | {4,5}, {4,6} | identity | unchanged | unchanged |

   All six unordered pairs are covered.

3. **σ(T_i)=T_{ρ(i)} and the rest of the normal form.**
   - a, b and ab fix {1,2,3}, {2,3}, {4,5} and {6,7} setwise, with ρ=id.
   - c sends rows 2,3 (support {6,7}) to {4,5}=T_4=T_5, and rows 4,5 (support {4,5}) to {6,7}=T_2=T_3. Rows 6 and 7 are fixed pointwise.
   - σ is a bijection of {1..7} that fixes 0. So negative bits and the absent coordinate 0 transfer.
   - Row 0: P_σ|j⟩=|σ(j)⟩.
   - SB2: {s+2} goes to {τ(s)+2}, and Q'_1(1,0) keeps support {1,2,3}.
   - ROWLEX: the final masks equal the template. Its keys are 3, 3, 12, 12, 48, 112, which is sorted under E1's domain.

4. **Simultaneous survival.** X'_{τ(s)}(ρ(i),σ(c))=X_s(i,c) holds for every s under one move. ab is a single move, equivalent to a followed by b, and b fixes label 4. So no second normalization can displace the first square.

5. **Fresh auxiliaries.** Necessity is re-applied to the genuine Q'. Every primary and auxiliary takes its semantic value from Q'. No Boolean-model relabelling, GB auxiliary invariance or GA identification is used.

6. **Same assignment satisfies both M tails.** The tails contain only primaries. Both final X'_s are permutations, so every binary has a false literal in the one canonical assignment. No conflict between auxiliary extensions can arise.

7. **Scope of the conclusion.** §6 is correctly limited. It is genuine-level only and needs BOTH UNSAT hypotheses. It leaves untouched the Boolean status of GB_B3∧M_2, A10/A11, and B1/B2/B5.

## Proved, conditional on imports

The imports are:
- the MOQLS and isotopy definitions as used in [BR] and [G];
- the P1-B3 template table and the GB_B3 own-name-ID identities ([J], WMAN);
- GB necessity ([G] read with [D,E]) at its stated scope;
- U/T16, needed only to connect to arbitrary genuine non-classical five-sets.

Given these, the candidate proves:
- Any genuine five-set with row-0 standard form, SB2 with the weight-3 Q_1 witness, and the P1-B3 template has at least two permutation supports among X_2..X_5.
- One move from {id,a,b,c,ab} gives a genuine configuration with the same properties in which squares {2,3} or squares {2,4} both have permutation supports.
- The canonical GB assignment of that configuration satisfies H_23 or H_24.
- Hence UNSAT(H_23) ∧ UNSAT(H_24) implies that no such genuine configuration exists.

## Genuinely new written detail vs [P]

- A direct proof of "at least two" (nine-ones lemma, 50 > 49), instead of citing NF §1 and the receipt.
- τ derived explicitly for each generator and for ab.
- σ(T_i)=T_{ρ(i)} verified by hand for B3, including negative bits and coordinate 0. The bridge only imported this ([E] N3: "not re-derived here").
- A literal map for each of the six pairs, replacing [P]'s scripted orbit closure. The group order 8 is never used.
- The simultaneous-tracking identity under one move, stated explicitly.
- A GB endpoint: a fresh canonical assignment for Q', one assignment satisfying both tails, and GB's own-name IDs.
- [P]'s Boolean-setting sentence ("would extend NF §4") and its GA clause counts are removed, and the exclusions are spelled out.

## Remains unproved / open

- **UNSAT(H_23) and UNSAT(H_24).** No DIMACS file, byte/hash binding, proof, checker run or qualified replay exists. A future binding must be exactly the GB_B3 bytes (f8fd0a51…) plus the 252 own-name binaries.
- **Boolean statements.** Boolean UNSAT of GB_B3, or of GB_B3∧M_2, is not proved. Any claim about arbitrary models would need a GB invariance lemma that has not been proved: primary relabelling under (σ,ρ,τ), plus canonical re-extension of the counter2, atleast3 and single auxiliaries (cf. [E] G5).
- **Adoption.** No parent decision or amendment replaces B3.M2.
- **Other cases.** The B5 half of [P], B1/B2, the other leaves, A10/A11 and any n=8 theorem are all open.
- **Shared imports.** U/T16 and the WMAN template table are not independently re-checked. GA/GB independence holds at CNF construction only.
