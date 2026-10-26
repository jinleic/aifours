# Cutting-Method squares: closing-arc characterization, one T-face, and the exact K switch formula

Actual `/bin/date` before this body: **Sun Oct 25 23:05:16 PDT 2026**. InfoRecursiveMDS18-2, slot info-4. NEW WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. Scope

The Cutting Method (one cut per directed Hamilton cycle of a circular source, the cut arcs forming the eleventh row) is the classical mechanism for odd-order Tuscan squares and the mechanism of the actual control v24 (SHA256 `e1fa1bd4dc53a90559b7b40a41bfbcab35ad31f96057f7d0121fb15a37194422`). Its distance-2 obstruction for developed sources is the unreviewed rainbow packet (SHA256 `553831a49b73388c5bf72b5440b9a3f39124550920a277150944857e95728014`). This packet proves Tuscan-1 structure of EVERY such square for order 11 (the arguments hold for any n>=4). Notation: source cycles C_1,...,C_10 partition the 110 arcs; P=(p_0,...,p_10); R^(k) is the source cycle whose cut arc is (p_k,p_(k+1)), read as a row from p_(k+1) to p_k.

## 2. Closing-arc characterization

**Lemma 1.** A Tuscan-1(11) square is a Cutting-Method square iff some row P has as its ten arcs exactly the closing arcs (last R, first R) of the other ten rows R.

Proof. If the square comes from cutting C_j at e_j, the row from C_j starts at the head of e_j and ends at its tail, so its closing arc is e_j, an arc of P. Conversely, closing each row R other than P by its closing arc gives a directed Hamilton cycle; together these cycles use the arcs of the ten rows and the ten arcs of P, i.e. every arc exactly once; cutting each at its closing arc returns the square with P as inserted row.

## 3. Exactly one T-face

**Lemma 2.** Every Cutting-Method square has exactly one T-face, traversing P, R^(9), R^(8), ..., R^(0) and back to P.

Proof. R^(k) ends at p_k. For k>=1 the row starting at p_k is R^(k-1); for k=0 it is P. P ends at p_10, where R^(9) starts. The splicing permutation of the eleven rows is therefore one 11-cycle. (In v24, P=R11 and the face order R11,R10,R2,R8,R4,R6,R7,R3,R9,R1,R5 is exactly this.)

## 4. The exact switch formula

Let K^src_x be the source neighbour permutation: K^src_x(y)=z iff y,x,z are consecutive in some source cycle (ten arcs, one per cycle). Let K_x be the completed neighbour permutation of the final square (nine interior triples plus the boundary arc p(x)->f(x)).

**Theorem 3.** K_(p_0)=K^src_(p_0) and K_(p_10)=K^src_(p_10). For 1<=i<=9, let A_i be the successor of p_i in the cycle containing (p_(i-1),p_i), and B_i the predecessor of p_i in the cycle containing (p_i,p_(i+1)). Then B_i != p_(i-1) and

`K_(p_i) = K^src_(p_i) composed with the transposition (p_(i-1) B_i)`,

i.e. K_(p_i)(p_(i-1))=p_(i+1), K_(p_i)(B_i)=A_i, and all other values agree with the source.

Proof. In the final square p_i (1<=i<=9) is first in R^(i-1), last in R^(i), interior in P and in the eight other rows. The eight other rows keep their source triples. The two source triples through p_i in the cut cycles, p_(i-1)->A_i and B_i->p_(i+1), are replaced by the P triple p_(i-1)->p_(i+1) and the boundary arc B_i->A_i (B_i precedes p_i in the row where p_i is last, A_i follows it in the row where it is first). B_i=p_(i-1) would put the arc (p_(i-1),p_i) in two different cycles. For p_0: it is last in R^(0), first in P, and not first of any other row; its interior triples are the source triples of the nine uncut-at-p_0 cycles, and its boundary arc (predecessor in R^(0), p_1) equals the source triple of the cycle containing (p_0,p_1). The case p_10 is symmetric.

**Corollary 4 (involutive sources give m=36).** If every K^src_x is an involution (for example when the source is closed under reversing cycles, as for the difference cycles x->x+d and for the v24 source Q_d), then each K_(p_i), 1<=i<=9, has exactly one 4-cycle (p_(i-1), p_(i+1), B_i, A_i) and three 2-cycles, K_(p_0), K_(p_10) are involutions, and the support is exactly m=36.

Proof. Composing an involution with a transposition of two points lying in different 2-cycles merges them into one 4-cycle. Here p_(i-1) and B_i lie in different 2-cycles: otherwise K^src(B_i)=p_(i-1), whereas K^src(B_i)=p_(i+1). The four points p_(i-1),p_(i+1),B_i,A_i are distinct (A_i=p_(i+1) would put the arc (p_i,p_(i+1)) in two cycles; A_i=B_i would give K^src(A_i)=p_(i-1)!=p_(i+1)=K^src(B_i)). Nine such symbols give 36.

This explains v24 completely: its m=36, its single face and the fact that every 4-cycle contains one boundary arc and one P arc are forced by the mechanism, not special to Etzion's pattern.

## 5. Consequences and nonclaims

- Every Cutting-Method Tuscan-1(11) square is one-face, and from any reversal-closed source it has support exactly 36. Lower support needs non-involutive sources (switches that split cycles) or non-Cutting-Method rows; nothing here constructs one.
- For Tuscan-2(11), a Cutting-Method square must still satisfy the rainbow conditions (inserted 2-steps absent from the source; every repeated source 2-step destroyed by a cut). The developed sources are excluded there and in v24 §6; general sources remain OPEN.
- No Tuscan-2(11) table and no all-array obstruction is supplied. Original target, HOLD, cutoff/deadline and all process histories, including the checkpoint045 withdrawal, are unchanged. This candidate needs its own complete source-bound gate.
