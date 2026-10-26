# Actual Tuscan-1(11) control: Etzion's Example 2 has one T-face and support m=36

Actual `/bin/date` before this body: **Sun Oct 25 22:41:16 PDT 2026**. InfoRecursiveMDS18-2, slot info-4. NEW WRITTEN CANDIDATE. Every count below is a hand derivation from eleven literal published rows, displayed so that it can be reconstructed line by line. No interpreter, kernel, program, enumeration tool, solver, replay, CLI or nested agent was used; nothing here is machine-checked, independently reconstructed or parent-adopted. No scientific GO.

## 0. Why this packet exists

The support ladder (accepted boundary: m>=8; later unreviewed m8 candidates v12–v23) uses only Tuscan-1 consequences. An actual Tuscan-1(11) array therefore bounds how far that ladder can ever go. This packet computes the exact support of the one literal Tuscan-1(11) array in the lane's sources, identifies its construction mechanism, and states what follows for the unrestricted Tuscan-2(11) target.

## 1. The literal object and its source

File `sources/etzion-example2-tuscan1-11.table`, 11 LF, 253 bytes, SHA256 `a50fc2994053f669973f91b61ed64824d30afe390527e74d62e9e6beee6f1a20`. Source: T. Etzion, P17 (`sources/etzion-P17.pdf`), "Example 2. For p=11 the following shifts-pattern is obtained by Theorem 1", followed by the square (OCR `sources/etzion-P17-pages6-10-ocr.txt` lines 62–80). Rows in file order:

```
R1   9 10  1  2  3  4  5  0  6  7  8
R2   4  6  8 10  0  1  3  5  7  9  2
R3  10  2  5  8  3  6  9  1  4  0  7
R4   5  9  0  2  6 10  3  7  4  8  1
R5   8  2  7  1  6  5 10  4  9  3  0
R6   1  7  2  8  0  3  9  4 10  5  6
R7   6  2  0  9  5  1  8  4  7  3 10
R8   2 10  7  0  4  1  9  6  3  8  5
R9   7  5  3  1  0 10  8  6  4  2  9
R10  3  2  1 10  9  8  7  6  0  5  4
R11  0  8  9  7 10  6  1  5  2  4  3
```

Each row lists 0,...,10 exactly once (inspection of the eleven rows).

## 2. Tuscan-1 property and the single T-face

First symbols R1..R11: 9,4,10,5,8,1,6,2,7,3,0 (all distinct). Last symbols: 8,2,7,1,0,6,10,5,9,4,3 (all distinct).

Splice the row ending at y to the row starting at y: R1(8)->R5, R5(0)->R11, R11(3)->R10, R10(4)->R2, R2(2)->R8, R8(5)->R4, R4(1)->R6, R6(6)->R7, R7(10)->R3, R3(7)->R9, R9(9)->R1. This is ONE 11-cycle, so the array has exactly one T-face of 110 arcs.

For a symbol x, an interior occurrence `a x b` in row Rr gives `K_x(a)=b` (written `a>b Rr`); the boundary arc is `p(x)>f(x)`, where p(x) precedes x in the row ending at x and f(x) follows x in the row starting at x. The table in §3 lists all ten arcs of every K_x; each K_x is a bijection of the ten symbols other than x. Hence every ordered pair (a,x) and (x,b) is a row adjacency exactly once: all 110 linear adjacencies are distinct (Tuscan-1).

## 3. Completed neighbour permutations

|x|nine interior arcs|boundary arc (ending row/starting row)|cycles|support>=3|
|---|---|---|---|---|
|0|5>6 R1, 10>1 R2, 4>7 R3, 9>2 R4, 8>3 R6, 2>9 R7, 7>4 R8, 1>10 R9, 6>5 R10|3>8 (R5/R11)|(1 10)(2 9)(3 8)(4 7)(5 6)|0|
|1|10>2 R1, 0>3 R2, 9>4 R3, 7>6 R5, 5>8 R7, 4>9 R8, 3>0 R9, 2>10 R10, 6>5 R11|8>7 (R4/R6)|(0 3)(2 10)(4 9)(5 8 7 6)|4|
|2|1>3 R1, 10>5 R3, 0>6 R4, 8>7 R5, 7>8 R6, 6>0 R7, 4>9 R9, 3>1 R10, 5>4 R11|9>10 (R2/R8)|(0 6)(1 3)(7 8)(4 9 10 5)|4|
|3|2>4 R1, 1>5 R2, 8>6 R3, 10>7 R4, 9>0 R5, 0>9 R6, 7>10 R7, 6>8 R8, 5>1 R9|4>2 (R11/R10)|(0 9)(1 5)(2 4)(6 8)(7 10)|0|
|4|3>5 R1, 1>0 R3, 7>8 R4, 10>9 R5, 9>10 R6, 8>7 R7, 0>1 R8, 6>2 R9, 2>3 R11|5>6 (R10/R2)|(0 1)(7 8)(9 10)(2 3 5 6)|4|
|5|4>0 R1, 3>7 R2, 2>8 R3, 6>10 R5, 10>6 R6, 9>1 R7, 7>3 R9, 0>4 R10, 1>2 R11|8>9 (R8/R4)|(0 4)(3 7)(6 10)(1 2 8 9)|4|
|6|0>7 R1, 4>8 R2, 3>9 R3, 2>10 R4, 1>5 R5, 9>3 R8, 8>4 R9, 7>0 R10, 10>1 R11|5>2 (R6/R7)|(0 7)(3 9)(4 8)(1 5 2 10)|4|
|7|6>8 R1, 5>9 R2, 3>4 R4, 2>1 R5, 1>2 R6, 4>3 R7, 10>0 R8, 8>6 R10, 9>10 R11|0>5 (R3/R9)|(1 2)(3 4)(6 8)(0 5 9 10)|4|
|8|6>10 R2, 5>3 R3, 4>1 R4, 2>0 R6, 1>4 R7, 3>5 R8, 10>6 R9, 9>7 R10, 0>9 R11|7>2 (R1/R5)|(1 4)(3 5)(6 10)(0 9 7 2)|4|
|9|7>2 R2, 6>1 R3, 5>0 R4, 4>3 R5, 3>4 R6, 0>5 R7, 1>6 R8, 10>8 R10, 8>7 R11|2>10 (R9/R1)|(0 5)(1 6)(3 4)(2 10 8 7)|4|
|10|9>1 R1, 8>0 R2, 6>3 R4, 5>4 R5, 4>5 R6, 2>7 R8, 0>8 R9, 1>9 R10, 7>6 R11|3>2 (R7/R3)|(0 8)(1 9)(4 5)(2 7 6 3)|4|

Each row's eleven entries appear once in this table (nine interior triples per row plus its two endpoints as boundary contributions), which is how the table was assembled.

## 4. Support and structure

K_0 and K_3 are involutions; each of the other nine K_x is one 4-cycle plus three 2-cycles. Hence

`m = 9*4 = 36`.

Exact structure: every 4-cycle contains exactly one boundary arc and exactly one R11 arc. The centres of R11's nine interior triples (0 8 9, 8 9 7, 9 7 10, 7 10 6, 10 6 1, 6 1 5, 1 5 2, 5 2 4, 2 4 3) are 8,9,7,10,6,1,5,2,4, precisely the nine non-involutive symbols; R11's endpoints 0 and 3 are the two involutive ones. The total cycle count is 2*5+9*4=46, even, consistent with the boundary-turn sign identity (product of sgn K_x equals sgn tau) for the one 11-cycle tau of §2; this is a consistency remark only.

## 5. Distance-2 profile (not Tuscan-2)

Interior distance-2 events are exactly the interior K-arcs. Twenty ordered pairs repeat (centre, row):

(0,9): 3 R6, 8 R11; (1,2): 5 R11, 7 R6; (1,5): 3 R2, 6 R5; (2,10): 1 R10, 6 R4; (3,4): 7 R4, 9 R6; (3,5): 4 R1, 8 R8; (4,3): 7 R7, 9 R5; (4,9): 1 R8, 2 R9; (5,4): 2 R11, 10 R5; (6,5): 0 R10, 1 R11; (6,8): 3 R8, 7 R1; (6,10): 5 R5, 8 R2; (7,6): 1 R5, 10 R11; (7,8): 2 R6, 4 R4; (8,6): 3 R3, 7 R10; (8,7): 2 R5, 4 R7, 9 R11; (9,1): 5 R7, 10 R1; (9,10): 4 R6, 7 R11; (10,1): 0 R2, 6 R11; (10,6): 5 R6, 8 R9.

Nineteen doubles and one triple: 21 excess events, 78 distinct ordered pairs among the 99 interior events. The array is Tuscan-1, not Tuscan-2, as its source states.

## 6. Exact mechanism and two source-family exclusions

Work in F_11. For d in F_11^*, let C_d be the difference cycle x->x+d. Let Q_d be C_d with 0 removed from between -d and d and reinserted between 5d and 6d.

|row|d|0 between|first symbol|cut arc (last,first)|
|---|---|---|---|---|
|R1|1|5,6|9|(8,9)|
|R2|2|10,1|4|(2,4)|
|R3|3|4,7|10|(7,10)|
|R4|4|9,2|5|(1,5)|
|R5|5|3,8|8|(0,8)|
|R6|6|8,3|1|(6,1)|
|R7|7|2,9|6|(10,6)|
|R8|8|7,4|2|(5,2)|
|R9|9|1,10|7|(9,7)|
|R10|10|6,5|3|(4,3)|

Each Rd is Q_d read from the stated first symbol (checked row by row against §1; for example Q_3 from 10 is 10,2,5,8,3,6,9,1,4,0,7, since 8+3=0 was moved). R11 is the path of the ten cut arcs in the order R5,R1,R9,R3,R7,R6,R4,R8,R2,R10: one arc from each row. This is the source's Cutting Method with shifts-pattern (*,8,9,7,10,6,1,5,2,4,3), *=0.

**Lemma 6.1 (the cyclic source).** The ten cycles Q_d use every ordered pair exactly once, and Q_d=d·Q_1 with Q_1=(0,6,7,8,9,10,1,2,3,4,5). Proof: Q_d removes (-d,0),(0,d),(5d,6d) from C_d and adds (-d,d),(5d,0),(0,6d). For e=2d, (5e,6e)=(10d,12d)=(-d,d), so every added (-d,d) replaces exactly one removed arc; x->5x and x->6x are bijections of F_11^*, so the arcs at 0 are each used once. Multiplying Q_1 by d multiplies every arc.

**Lemma 6.2 (uniqueness of single-0 relocation sources).** Suppose each cyclic row d is either C_d or C_d with 0 moved to between u_d and u_d+d (u_d not in {0,-d}), and the ten cyclic rows use every ordered pair exactly once. Then either no row moves 0, or u_d=5d for every d. Proof: if row d moves 0 it adds (-d,d); this arc also lies in C_(2d) unless row 2d moves 0 with u_(2d)=-d. So row d moved forces row 2d moved with u_(2d)=-d. Since 2 generates F_11^* (2,4,8,5,10,9,7,3,6,1), one moved row moves all rows, and then u_e=-e/2=5e for every e.

**Corollary 6.3 (no shifts-pattern gives Tuscan-2(11)).** For either possibility in Lemma 6.2 (the plain difference cycles or the cycles Q_d), no one-rainbow-path insertion, i.e. no choice of one cut per cyclic row whose cut arcs form an eleventh row, is a Tuscan-2 square. Proof: both sources are one orbit of F_11^* acting by multiplication, regular on F_11^* and fixing 0. For Q_1 the cyclic distance-2 pairs at 0 are (0,7) and (4,0); for C_1 they are (0,2) and (9,0); development gives every pair to or from 0. By Corollary 2 of `rainbow-split-and-projective-family-v1.md` (unreviewed; SHA256 `553831a49b73388c5bf72b5440b9a3f39124550920a277150944857e95728014`), 0 is isolated in the source's missing graph, contradicting the required spanning two-path forest. So Etzion's mechanism cannot be tuned to Tuscan-2(11) by any shifts-pattern, and neither can the unmodified multiplication source. This is a source-family exclusion, not a statement about arbitrary arrays.

**Lemma 6.4 (multiplication rows with an inserted 0 never complete).** For each d let P_d=(d,2d,...,10d), and let row d be P_d with 0 inserted into any one of its eleven gaps. No eleventh row makes these eleven rows a Tuscan-1(11) square.

Proof. Let Z0 be the rows with 0 first, Z1 the rows with 0 last, and I the rest, with 0 between k_d·d and (k_d+1)d. Rows in I cover all arcs of difference d except the split arc (k_d d,(k_d+1)d); rows in Z0∪Z1 cover all nonzero arcs of their difference. The eleventh row E must therefore consist of the split arcs (distinct differences, forming I) plus the arcs at 0 not covered by rows. Rows cover 10-|Z0| arcs into 0 and 10-|Z1| out of 0, so E has |Z0| arcs into 0 and |Z1| out; hence |Z0|,|Z1|<=1 and |Z0|+|Z1|>=1.

- Z0={d0}, Z1 empty: E=(e_1,...,e_10,0), whose nine nonzero arcs have the distinct differences F_11^* minus d0, so e_10-e_1=-d0. Arcs out of 0 covered by rows are the heads e_2,...,e_10 of the split arcs and d0; distinctness forces d0=e_1, hence e_10=0, impossible.
- Z1={d1}, Z0 empty: reverse every row; row d becomes P_(-d) with 0 inserted, Z0 and Z1 swap, and the previous case applies.
- Z0={d0}, Z1={d1}: E=(x_0,...,x_(p-1),0,x_(p+1),...,x_10) with 1<=p<=9, and its eight nonzero arcs have the distinct differences F_11^* minus {d0,d1}, so (x_(p-1)-x_0)+(x_10-x_(p+1))=-d0-d1. Arcs into 0 from rows are the split-arc tails and -d1 (row d1 ends ...,-d1,0), so -d1=x_10; arcs out of 0 from rows are the split-arc heads and d0, so d0=x_0. Substituting gives x_(p-1)=x_(p+1), impossible.

QED. Thus the cut must be rotated as in Etzion's rows, and rotated single-0 sources are covered by Lemma 6.2 and Corollary 6.3.

## 7. Consequences for the unrestricted target

1. **Ceiling of every Tuscan-1-only support bound.** An actual Tuscan-1(11) array has m=36. Hence no statement "every Tuscan-1(11) array has m>=k" is true for k>=37. The accepted m>=8 and the later unreviewed m8 candidates are consistent with this control (they concern m=8; the control has m=36 and one face). The one-face regime is nonempty, so one-face results carry meaning only with their support hypotheses.
2. **The ladder cannot settle Tuscan-2(11) by itself.** Tuscan-1(11) arrays exist, so any contradiction must use distance-2 noncollision. Counting with noncollision gives no support bound: m=110-2N2 with N2 the number of 2-cycles; noncollision allows at most one fully interior 2-cycle per unordered pair (55) and at most eleven 2-cycles through a boundary arc, a vacuous bound.
3. **Exact distance-2 identities for any Tuscan-2(11) array** (written, for continuation):
   - Interior K-arcs are pairwise distinct; equivalently the sum of the K_x as 0/1 matrices is J-I-M+GF with M a 0/1 matrix of eleven missing pairs.
   - With c_j(a) the number of rows having a in column j (columns 0..10): deg_out_M(a)=c_9(a) and deg_in_M(a)=c_1(a). Proof: a starts an interior distance-2 event in every row where it sits in columns 0..8, i.e. in 11-c_9(a)-c_10(a)=10-c_9(a) rows (a is last in exactly one row); distinctness leaves c_9(a) missing out-pairs. The in-degree statement is the mirror (a first in exactly one row).
   - In a one-face array the even-position face subsequence s_0,s_2,...,s_108 is a closed trail of 55 distinct arcs (every middle is odd, hence never a cut); all eleven boundary pairs lie on the odd subsequence.

## 8. Residual and status

No literal Tuscan-2(11) table and no all-array obstruction is supplied. The original target remains: a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array, which by §7 must use the distance-2 condition. Construction search would require a separately admitted scientific GO and is not requested. This candidate needs its own complete source-bound gate. All cadence, private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged.
