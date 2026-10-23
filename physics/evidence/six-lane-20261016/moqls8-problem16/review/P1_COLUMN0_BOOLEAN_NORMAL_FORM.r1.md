# P1 column0 Boolean normal form r1 — UNREVIEWED proof candidate, no cutover

This strengthens the separate physical/unitary proposal34e90d73…284a. It is a written proof candidate, not an
accepted lemma, completed root proof or running protocol. No strengthened CNF, solver run, original-ledger
amendment or change to the approved signed-cube pilot is authorised/implied. No novelty/priority claim.

## Claim and exact setting

Let F_one be the frozen weak CNF with SHA374d6fb4…eeb9, generated from the unconditional generic5-square,
no-classical-square instance by deleting ONLY the four P4-ALO clauses of squares2–5. Let C be one of the full
42-unit P1-B1/B2/B3/B5 column0 templates. For s=2..5, M_s means every column0 vector has singleton support
in the row0 frame. It says NOTHING about cells outside column0 or whether the whole square is classical.

**Claim:** existence of ANY Boolean model of F_one AND C implies existence of a Boolean model of at least one
of the following stronger formulas, with the SAME source template C:

- P1-B1: F_one AND C AND M2;
- P1-B2: F_one AND C AND M2, or F_one AND C AND M4;
- P1-B3: F_one AND C AND M2;
- P1-B5: F_one AND C AND M2, or F_one AND C AND M3.

This is a MODEL-EXISTENCE normal form, not an assertion that each individual model already satisfies the extra
M_s, nor an exact permutation of the whole CNF's aux-variable names. If independently accepted, UNSAT of the
six stronger formulas would imply literal Boolean UNSAT of the four original source leaves. It would not merely
exclude physically realizable images. There are currently NO such stronger-formula refutations in this note.

## 1. Pure support lemma — actual vector/phase existence is unnecessary

For each square s define the7×7 Boolean matrix X_s(i,c)=g_s((0,c),(i,0)), i,c=1..7. The row0/column0 overlap
matrix of size8 has the isolated common-point entry(0,0)=1 and zeros elsewhere in its row and column by the
encoder's g constants (gram_a.py:127–138). Deleting that entry leaves these axioms:

(A) Every row and column of every X_s is nonempty.
(B) Two rows of one X_s never have intersection size exactly1; the same holds for two columns.
(C) The five X_s are entrywise disjoint.

These are actual Boolean consequences of the frozen encoder: G2 at150–153 gives(C); G3 at179–190 gives(A)
and(B), with AND auxiliaries exactly equivalent to the two input bits by63–75. No G4, G5, PSD/rank condition,
H3 clause or complex phase is needed for the LOCAL lemma below.

Assume X_1 is a P1 template. Rows1,7 have support123, row6 has support23, and the remaining four rows have
B1..B6 on B={4,5,6,7}. Write k for the number of non-permutation matrices among X_2..X_5.

A singleton row is an isolated edge: any other row meeting its sole column would have intersection size1,
contradicting(B). The column version is identical. Since all five matrices have nonempty rows/columns and are
disjoint, each individual degree is≤3. Rows1,7 and columns2,3 of X_1 have degree3, so in every other X_s those
rows and columns are singleton isolated edges. The two rows use distinct B coordinates; the two columns use
two further distinct rows. Neither of those further rows is6, since X_1 already uses(6,2),(6,3).

Remove these four isolated edges. The remaining3×3 support matrix R_s has all rows/columns nonempty and
inherits(B). It includes distinguished row6 and column1. Their degrees are each≤2, since X_1 contributes2 at
row6/column1 and the other three squares each need≥1, out of total capacity7.

Classify R_s using ONLY(A),(B): if a singleton exists, remove its isolated edge and the residual2×2 is either a
permutation or a fullK22. If no singleton exists, all degrees are≥2. There must be a zero, because the distinguished
row/column have degree≤2. Two zeros cannot share a row/column; zeros in different rows/columns would make
the two degree2 rows overlap in exactly1 position. Hence there is exactly one zero, at(6,1). Thus R_s is either
a permutation, K22 plus an isolated edge, or K33 minus the edge(6,1).

Let A1 be the other squares of degree2 in column1, and A6 those of degree2 in row6. Each set has size≤1 by
support capacity: X_1 has degree2, four nonempty others need4, leaving only1 extra. A non-permutation X_s
outside A1 UNION A6 has both distinguished degrees1; its R_s must be K22 plus the SAME isolated edge(6,1).
By(C), at most one other square can have that edge. Therefore k≤|A1|+|A6|+1≤3: at least ONE other X_s is a
permutation. This argument is fully propositional/combinatorial; no unitary realization is used.

A non-permutation7×7 matrix obeying(A),(B) has at least9 ones. Otherwise only one row could have degree≥2;
the other six singleton rows would isolate six columns, leaving only one column for that row, a contradiction.
If X_1 has m ones, disjointness gives m+4×7+2k≤49. Together with k≤3 this proves minimum permutation counts
among the other four of[1,1,2,3,2,4] for B1..B6, whose m values are[12,14,16,18,17,20]. In particular B5 gives≥2.

## 2. Primary-level invariance of the actual Boolean core

Let sigma permute B, fixing coordinates0,1,2,3. Let rho permute rows2..5, fixing0,1,6,7. Define the common cell
permutation T(i,j)=(rho(i),sigma(j)). Relabel squares by tau(1)=1 and tau(s)=sigma(s+2)−2 for s=2..5. For all
primary Gram bits define

    g'_{tau(s)}(T(p),T(q)) = g_s(p,q).

This is a bijection of unordered-cell-pair primary variables and constants. It preserves SAME-CELL=true and
SAME-ROW/COLUMN=false (127–138). It permutes the16 fixed row/column lines of165 among themselves. Therefore:
- G2 is preserved: every distinct-cell pair and pair of quantum squares is included (150–153).
- G3 nonemptiness and no-singleton-intersection are preserved under row/column permutations/transposition
  of each pair-of-lines overlap pattern (179–190).
- G4 is preserved: for every fixed line and every p,q outside it, the overlap-intersection cardinalities and g(p,q)
  are merely relabelled (191–206).
- G5 is preserved: singleton support in any fixed line and the resulting same-ray primary equalities are merely
  relabelled (207–232).

There are NO classical L variables/constraints in the frozen instance: generic ngeneric0 makes CL empty at87,
so the classical branches100–125/140–149 contribute nothing. fixg is absent. This note is NOT asserting these
invariances for an instance with fixed classical data or an arbitrary fixg input.

For any primary model of these core rules, all AND_DEF/b3/c4 auxiliary bits can be evaluated to their exact
conjunctions;63–75 proves both directions. Likewise u5 at220–226 is exactly the singleton-support condition,
and its remaining clauses227–232 are exactly the G5 primary equalities just listed. Hence relabelled primary
bits admit the required core auxiliary extension; no guessed bijection of allocated aux IDs is needed.

## 3. P4, SB2 and ROWLEX are retained, not silently dropped

SB2 assigns Q1's(1,0) support123 and Q2..Q5's supports4,5,6,7 (271–281). Because rho fixes row1 and sigma fixes
A, Q1's witness persists. The formula for tau makes every other square's transformed singleton agree with its
NEW square label, so the SAME SB2 units hold.

Only Q1's P4-ALO remains. At(1,0), the support has exactly3 true row0 coordinates by SB2. Set that Q1 w3 flag
TRUE, and all other w3 flags FALSE. The one-way P4 clauses233–247 hold: every6-subset of8 coordinates meets
a3-set; only Q1 has a retained at-least-one clause. This explicit extension works for arbitrary Boolean primary
patterns, not only actual vector assignments. No deleted other-square ALO is re-imported.

The row-lex keys are EXACTLY the Q1 column0 support bits k=0..7, most significant k=0 (248–270). Full42-unit
source templates plus SB2/constants FIX EVERY ONE of those key bits. The actions in §4 preserve the SAME key
mask in each final row, not merely its multiset. Those masks are already nondecreasing. Thus the transformed
pattern admits the canonical prefix-equality extension for ROWLEX (or can retain the old prefix values, since
the key values are identical). ROWLEX is present in the target formula and is not assumed invariant on arbitrary
unfixed keys. This is why the FULL-column templates, not only a seven-bit root cube, are essential.

## 4. Exact support-stabilizer actions and selection of six representatives

Use only the following generator pairs(sigma,rho). Square action is ALWAYS the tau determined by sigma.
They fix all distinguished rows/columns required above.

- B1: for any sigma in Sym(B), define r(b)=9−b (b4..7 corresponds to rows5..2), and rho(r(b))=r(sigma(b)).
  This sends each singleton Q1 B row back to its exact canonical position. The action on B is transitive.
- B2: sigma=(4 5),rho=id; sigma=(6 7),rho=(2 3). The B orbits are{4,5},{6,7}.
- B3: sigma=(4 5),rho=id; sigma=(6 7),rho=id; sigma=(4 6)(5 7),rho=(2 4)(3 5).
  These generate a transitive action on B.
- B5: sigma=(5 6),rho=id. Its B orbits are{4},{5,6},{7}.

Each displayed pair preserves every Q1 column0 support mask in its FINAL row. This can be checked directly
from the frozen template table; closure under composition follows from preservation. These are sufficient
subgroups, not an asserted enumeration of the full automorphism group of the huge CNF.

Permutation-column status is invariant under these actions. By §1 a source B1 model has some M_s; transitivity
sends that square's row1 label s+2 to4, giving M2. The same argument applies to B3. For B2, send its available
label to orbit representative4 or6, giving M2 or M4. For B5, at least TWO of the four are permutation columns;
at most one has row1 label7, so one has label in{4,5,6}. Either label4 gives M2 or(5 6) yields label5 and M3.
No omitted seventh case is needed.

The primary transformation preserves the core, the SAME template, SB2 and the chosen Q1 witness. §3 supplies
P4/ROWLEX and §2 supplies all other aux bits. Thus it constructs a full Boolean model of one of the six named
stronger formulas. The contrapositive is the claimed Boolean-UNSAT transfer.

## 5. Proposed encoding and limits of this claim

M_s can be imposed by126 negative binary clauses for i=2..7 and1≤c<d≤7:

    NOT g_s((0,c),(i,0)) OR NOT g_s((0,d),(i,0)).

G3 already gives nonemptiness, and SB2 makes row1 singleton. Constants handle coordinate0. Therefore these
clauses express the intended one-column property, without new variables or a whole-square-classical/K4
assumption. A source leaf5740268clauses would become5740394clauses. No such CNF has been generated/run.

This proof is UNREVIEWED. It has not been compiled into DRAT, Lean or an independently checked clause audit.
It claims no exact full-CNF variable-permutation automorphism; it uses a primary-model transformation plus
explicit canonical aux extension. The original16-case ledger is untouched. Parent acceptance/amendment and
independent hostile reviews would be required before these six restricted certificates could discharge the
four original Boolean obligations. Current signed-cube pilot remains unchanged. The finite local15-cell
example of34e90d73…284a is NOT a full CNF model and is not used to assert a physical counterexample.
