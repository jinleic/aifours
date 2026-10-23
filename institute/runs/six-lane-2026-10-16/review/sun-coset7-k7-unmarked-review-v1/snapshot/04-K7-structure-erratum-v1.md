# K7-structure-erratum-v1: overlay on K7-structure-v1, addressing the Codex review findings

- **Freeze record:** host-clock time and sha256 in `evidence/k7-structure-erratum-v1.sha256`.
- **What it overlays:** `K7-structure-v1.md` (f4534c07c556557c9113c6db6106f081486316e326c6d92db3f069d5fc539fc1), which stays frozen and byte-identical. Read the two files together.
- **Source of the findings:** the Codex review of K7-structure-v1, as relayed by the parent.

  | part | verdict |
  |---|---|
  | TRI, U, TWIN, Q5 | ACCEPT |
  | K7-Q | ACCEPT-WITH-FIXES: one MINOR finding |
  | K7-COV | ACCEPT-WITH-FIXES: one MAJOR and one MINOR finding |

  The Claude review is pending.
- **Scope:** this file addresses exactly those three findings, plus one consistency note (S1) about files that depend on the changed convention. It makes no other change.
- **Status:** this is a written overlay, and it is unreviewed. K7 stays OPEN.

## X1 (K7-Q, MINOR): make "exactly one family" true

**Defect.** K7-structure-v1 §4 says "exactly one of the following holds", yet notes that the degenerate cases (b = 1, and all β = 2) fall under both Q23 and Q24.

**Replacement definitions** (Codex's convention). On the twin blocks put B ≡ B′ iff B = B′ or β(B, B′) = 2. The three families become:

| family | definition |
|---|---|
| Q5 | every block is a singleton and every β = 5 (unchanged) |
| Q23 | every β ∈ {2, 3}. The ≡-classes are the 2-classes. This **includes** b = 1 and the all-2 case, where there is a single 2-class. |
| Q24 | every β ∈ {2, 4} **and at least one β = 4** |

**Proof that exactly one family holds.**
- **Q5:** if some β = 5, Q5 holds and no other β occurs (K7-Q proof, "a 5 forces Q5").
- **Q24:** otherwise, if some β = 4, there is no 3 (K7-Q proof, "3 and 4 never coexist"), so Q24 holds.
- **Q23:** otherwise every β ∈ {2, 3}, so Q23 holds. ≡ is an equivalence relation because the type (2,2,3) fails T.
- **Disjointness:** the three conditions are pairwise disjoint (5 present; 4 present and no 5; neither 4 nor 5). ∎

## X2 (K7-COV, MAJOR): VFC must be a hypothesis of (i)

**Defect.** K7-COV (i) lists only T and Ppair as hypotheses, yet item (i).3 restricts Q5 to |U| = 4. That restriction uses K7-Q5, which uses VFC.

**Codex's counterexample.** Seven unmarked (1,1,0) profiles with every α = 5 pass T and Ppair, but violate the stated restriction.

**Corrected hypothesis of (i).** Every K7 pattern that passes:
- T and Ppair on all triangles of U;
- T and Ppair on all triangles with two vertices in one twin block;
- **and Corollary VFC-count at every unmarked vertex, for every admissible q;**

is determined by the data (i).1–5, with Q5 restricted to |U| = 4.

**Alternative.** If VFC is not assumed, (i).3 must allow Q5 for every |U| ≥ 4 (all blocks singletons, every β = 5).

**Unaffected parts.**
- (ii)–(v) are unchanged. (v) and its proof already invoke VFC: the pattern of any configuration passes T, Ppair and VFC.
- The completeness statement (v) is unaffected, because actual configurations satisfy every rule.

## X3 (K7-COV (iii), MINOR): fix the marking data before the orbit criterion

**Replacement text for the second bullet of (iii).** Two data sets D = (Mk, Π, Q, A, N) and D′ = (Mk′, Π′, Q′, A′, N′) give the same pattern orbit iff both of the following hold:
1. Mk = Mk′: the same marker partition and the same capped excesses, hence identical marked profiles at identical marked positions. Marked vertices are fixed by the stabiliser.
2. Some size-preserving bijection σ of the blocks of Π onto the blocks of Π′ carries (Q, A, N) onto (Q′, A′, N′). That is:
   - β′(σB, σB′) = β(B, B′), equivalently σ maps 2-classes to 2-classes in Q23;
   - a′_{z,σB} = a_{z,B};
   - N′ = N.

## S1 (consistency note): files that depend on the family convention

These follow from X1. None of the files below is modified.

**`K7-enumeration-spec-v1.md`** (e5aa176b…795f), §1.3, uses the opposite but also exact assignment: all-2 and b = 1 go to Q24, and Q23 requires at least two classes. Either convention gives a partition. An implementation must follow exactly one, and a spec v2 (not written) would adopt X1.

**`K7-pair-lemma-v1.md`** (77ce8b1b…c3d):
- P1 and P2 are stated for Q23 "with at least two 2-classes". Their content is unchanged. Under X1 they do not cover the single-class Q23 case.
- P3's proof uses only that every outside α lies in {2, 4}. So it holds for every {2,4} pattern. Under X1 that means single-class Q23 together with Q24. In particular, for M = ∅, a single-class (all-2) pattern containing a twin pair is impossible by P3's argument, since there k_4 = 0.

**`K7-unmarked-lemmas-v1.md`** (frozen after this erratum) states its Q23 results for "at least two 2-classes" only.
