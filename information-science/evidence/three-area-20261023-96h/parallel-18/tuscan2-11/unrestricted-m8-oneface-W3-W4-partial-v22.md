# Actual Tuscan11 one8/ONE face — general corner lemmas, W3/W4 partial closure and the exact remaining cases

Actual `/bin/date` before this body: **Sun Oct 25 22:06:14 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE (partial), not reviewed/adopted/formal/executable/novelty cleared. Written reasoning only; no interpreter, program, enumeration tool, solver, replay or GO.

## 1. Scope

Continues the unreviewed v20 (SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`: four words W1–W4, v-cut at a branch corner) and v21 (SHA256 `770ed4f5356e2ed1e0084f444c0dda1a33a6c79deaee2c4bb1b981fba02b8589`: W2 impossible). Here

`W3 = A B A^- C B^- D C^- D^-`, `W4 = A B A^- C D B^- C^- D^-`.

Notation and tools are those of v21 §2 (band identity, full loops, cut uniqueness, Lambda windows). Parent-accepted scope remains m>=8 only. This paper does NOT finish W3 or W4; §5 lists exactly what remains.

## 2. Two general corner lemmas

**(E) End-vertex exclusion.** Let z be the vertex next to v at one physical end of a loop X. The face reaches that end once (a traversal P of X arrives, followed by Q) and leaves it once (a traversal R of X leaves, preceded by P'). If neither corner is the cut, the row through the arrival corner contains z and HEAD(Q), and the row through the departure corner contains TAIL(P') and z. Hence label(z) is absent from HEAD(Q) and from TAIL(P'). When Q=P' is one ordinary traversal (pattern X Y X^-), label(z) is absent from all of Y: this is v21's span-2 rule.

**(I) Lambda-incident lemma.** Suppose the cut is at an end of the short loop Lambda and Lambda's traversal from that end starts the face. Measure y from that end, short copy at y=tau. Rows0 and1 are the windows y[0,10], y[10,20]; Lambda's opposite traversal has one whole window y[delta,delta+10]. v20's offset argument gives delta in{4,5,6}, and

`H'=labels y[1,delta-1]`, `K=labels y[delta,9]=labels y[delta+11,20]`, `c10=label y_10`, `O = H' + K + c10`.

The opposite traversal ends at y=0 with tail y[1,delta]; the next traversal N therefore has

`HEAD(N) = (K minus y_delta) plus c10`, consecutive, 10-delta symbols.

delta6: three K labels among four consecutive vertices with K4 exhausted. delta5: at least two new K edges; exactly two only with c10 in the middle, and then K5 would be complete while y_5 has degree<=3. **So delta=4 is forced**, and then: (i) c10 is strictly inside HEAD(N) (at the last position it would repeat the cut label y_10; at the first, HEAD(N) gives four new K edges, fourteen in all with at most three at y_4, while at most ten exist among the other five labels); (ii) y_4 is interior in the path y[15,20], and the ten edges among K minus y_4 are each used exactly once by y[5,9], y[15,20] and HEAD(N); (iii) tau is12 or13, because tau=11 would put four edges on the three labels H'; the three H' edges are then each used exactly once; (iv) writing e for the band value where Lambda's forward traversal arrives at its far end, e is1,2 or3 and that end lies at y=20+e.

The mirror case (Lambda's traversal ENDS the face at the cut) is the same statement for the reversed coordinate, with N replaced by the traversal preceding Lambda's other traversal at the cut end; v21 §§6–7 are instances. Any further adjacency of two labels from K minus y_4, or of two H' labels, is impossible in the delta=4 case.

## 3. Directly closed corners

All corners below have the short-copy loop Lambda as stated; each uses a full loop (v21 (T1)) and the span-2 rule with middle gap index in1..8.

- W3, Lambda=A, gap0 C (cut A^-|C): C full; D C^- D^- has middle index3. Contradiction.
- W3, Lambda=A, gap0 B^- (cut C|B^-): B full; A–B–A^- has middle index6. Contradiction.
- W3, Lambda=A, gap9 B^- (cut B^-|D): B full; A–B–A^- has middle index5. Contradiction.
- W3, Lambda=B, cuts A^-|C (gap0 C) and C|B^- (gap9 C): C full; D C^- D^- has middle index4 or3. Contradiction.
- W4, Lambda=A or C, cuts D|B^- (gap0 B^-) and B^-|C^- (gap9 B^-): B full; A–B–A^- has middle index5, 4, 5, 4 respectively. Contradiction.

W3 has the reversal symmetry A<->D,B<->C, so Lambda in{A,B} suffices; W4 has the reversal symmetry fixing A and B and swapping C,D, so Lambda in{A,B,C} suffices.

## 4. Lambda-incident corners reduce to delta=4

By (I), every corner at an end of Lambda is impossible unless delta=4 with the saturation structure (i)–(iv). This applies to W3 Lambda=A (cuts D^-|A, A|B, B|A^-), W3 Lambda=B (A|B, B|A^-, B^-|D), W4 Lambda=A (D^-|A, A|B, B|A^-, A^-|C), W4 Lambda=B (A|B, B|A^-, D|B^-, B^-|C^-), and W4 Lambda=C (A^-|C, C|D, C^-|D^-).

## 5. Exact remaining one8/ONE-face cases

- delta=4 saturated cases at the Lambda-incident corners listed in §4.
- Interior-Lambda branch corners: W3 Lambda=A cuts D|C^- and C^-|D^-; W3 Lambda=B cuts D^-|A, D|C^-, C^-|D^-; W4 Lambda=A cuts C|D and C^-|D^-; W4 Lambda=B cuts D^-|A, A^-|C, C|D, C^-|D^-; W4 Lambda=C cuts D^-|A, A|B, B|A^-.

Every original length, cut, copy and label condition remains in these cases; no finite search or sufficiency claim is made. W1's branch part is only in unreviewed v19. All other m8 placements and all m>=9 remain open.

**First unproved original step:** a literal11x11 table with110 distinct LINEAR adjacencies and99 distinct LINEAR distance-two events, or a contradiction for every remaining full system. Neither is supplied.

All cadence/private-written-exactness/admission/clock/source histories and the checkpoint045 withdrawal remain unchanged.
