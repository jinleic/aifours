# Proposed unified n8 counterexample encoding: one P4 square and all16 column templates

Proof candidate only. No new solver run or cutover is authorised by this note. The approved13 old-F template
instances remain unchanged. The point is a target-complete route if later timing data justifies it.

## 1. Weakened formula and exact delta

Let F be the pinned generic five-Gram-square base6ecb77a7…469b (no classical symbol variables, no weight1, K5 SB2,
Q1 ROWLEX). Define F_one by removing ONLY the four row0 P4 at-least-one-flag clauses for squares2,3,4,5.
Keep Q1's P4 at-least-one clause, all one-way w3 clauses, and every other original clause. Deletion indices must be
re-derived/checked from the accepted encoder binding; no code or data is changed here.

Labels2–5 in this formula are arbitrary QLS, not an assertion of non-classicality. The only active requirement of
non-classicality is Q1's weight3 witness (indeed SB2 already fixes its weight3 support at(1,0)). The unused flags of
a square without weight3 may all be false, since its at-least-one clause is removed. No classical-square row sort
is imposed; the still-free common permutation of rows2–7 is used for Q1 ROWLEX as before.

## 2. Necessity for EVERY genuine non-classical five-set

Let S be any genuine set of five MOQLS(8) that is not wholly classical. Put each square in row0 standard form by
its own unitary. Classicality/ray counts and mutual orthogonality are preserved. By the accepted TheoremA8, if all
entries of all five squares had weights at most2 in this frame, S would be wholly classical. Therefore some square
has an entry of weight3 (all weights are at most3 by W8).

Relabel that square Q1. The established SB2 moves place such an entry at(1,0), with Q1 support{1,2,3} and the other
four supports{4},{5},{6},{7}; disjointness/nonemptiness forces this partition whether those four squares are classical
or non-classical. Re-sort rows2–7 by Q1's column0 overlap bits to restore the exact non-strict ROWLEX.

Every member of S satisfies G2,G3,G4,G5 and the Gram constants: those families hold for ALL QLS. Q1 satisfies row0
P4. Each of the other four squares satisfies its one-way P4 flag clauses by assigning flags their defining values,
or simply false when no weight3 entry exists. Thus the canonical assignment satisfies F_one.

This argument does not reduce S by Lemma10, assume its number of non-classical members, use a classical-net
catalogue or assume all-frame P4. The sole extra import is the accepted universal A8 implication.

## 3. The16-template cover still applies

The proof of `K5_COLUMN0_TEMPLATE_COVER.r1.md`§§1–4 uses only: a genuine five-set; standard form; Q1's fixed
weight3 support; both degree bounds from G2 and aligned ONBs; and the residual normalisation moves. None of those
uses P4 on squares2–5 or reducedK5 membership. Its invariance proof extends verbatim: no type/order on squares2–5
is specified, so their relabelling is permitted. Therefore every genuine counterexample admits one of its16
full-column support templates and yields a satisfying assignment of the corresponding F_one+42unit formula.

Consequently independently verified UNSAT of ALL16 such formulas, together with the reviewed necessity bridge and
cover proof, would prove that every set of five MOQLS(8) is classical — the full n8 instance of Problem16.
The accepted old c112 proof CANNOT be used here because it refutes a stronger formula requiring all five P4 clauses.
All three c112 templates must be included anew. The old13-case pass remains a valid separate restricted experiment.

No such16-case pass has run; no completeness or exclusion is asserted. SAT of a Boolean support formula would also
not by itself be a genuine vector counterexample. A future pilot/protocol and both independent reviews are needed
before this route replaces any approved computation.
