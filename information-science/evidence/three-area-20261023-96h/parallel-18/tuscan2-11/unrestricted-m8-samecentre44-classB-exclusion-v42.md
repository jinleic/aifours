# Actual Tuscan11 same-centre 4+4, class (b) (two threads plus two loops) — impossible

Actual `/bin/date` before this body: **Mon Oct 26 01:49:42 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

v41 (SHA256 `e07d7252b8d15cfca2a7b431f5d29fdd015b1d52a9bbcdd39be4966c07fd0704`) class (b): F_1 = T1 L2 T1^- L1, F_2 = T2 L2^- T2^- L1^-; excesses t1, t2, l1, l2 (the short-copy path Lambda has p+q). Swapping T1 and T2 (loops reversed) exchanges the faces; swapping b1 and b2 exchanges L1 and L2 and fixes each face. So it suffices to treat Lambda=T1 with the cut in F_1 or in F_2, and Lambda=L1 with the cut in F_1. Tools: v37 §1 (all row-local), v20 §4, v30.

## 2. Lambda=T1

- Cut in F_1: every corner of F_1 is an end of T1 or T1^-, and T1, T1^- are not adjacent in F_1, so v20 §4 and v30 exclude every cut.
- Cut in F_2 (F_1 cut-free): in F_1 the loop L2 lies between Lambda's arrival at Lambda[L] and its departure from Lambda[L], and L1 between the arrival at and departure from Lambda[0]. Each loop is covered by the head and tail of the rows at those corners; one of them is pure K' (v31 §2), the other is O minus ({q}+E) for a Q-path endpoint q, so each loop carries only r-1 Q-labelled vertices. Every corner of F_2 has a loop as its first or last gap, which would carry a full window (r Q). Impossible.

## 3. Lambda=L1, cut in F_1 (F_2 cut-free)

The face sums give P+l2+2t1=10 and P+l2+2t2=0, so t2=t1-5. F_2's cyclic band, from g at T2^-|L1^-: g, g+q (w), g+P, g+P+t2, g-t2. Cuts at L1's ends or at the short copy are excluded by v30/v20; the remaining corners are T1|L2 and L2|T1^-.

- Cut T1|L2: e_1..e_4 = l2, l2+t1, l2+t1+p (u), 10-t1, so l2,t1>=1 and D_L=t1-g. D_L>=4 would need the pure-K' tail of T1^- (l2+t1 vertices) to have at most 5 vertices while t1>=g+4>=5. So D_L<=-4; with g-t2<=9 this forces g=t1+4, r=4, and F_2's band after L2^- equals 9. Then the F_2-row at L2^-|T2^- is L2[1,9]+v+T2[last], and the F_1-window L2[1,10] gives label(T2[last])=label(L2[10]); but the F_2-row at T2|L2^- contains both T2[last] (its tail) and L2[10] (its head L2[9,9+l2]). A label repeats. Impossible.
- Cut L2|T1^-: e_1..e_4 = t1, t1+p (u), t1+P, 10-l2, so D_L=t1+l2-g; D_L<=-4 contradicts g-t2<=9, so D_L>=4 and the pure-K' tails are T1[1,t1] (F_1) and T2[1,g] (F_2). The F_2-row at L1^-|T2 gives HEAD(T2) of length 10-g-P with r-1 Q, and 10-g-P exceeds |T2|=4+t1 unless r=4 and HEAD(T2) is all of T2; so r=4, T2 holds three Q, the F_2-band at T2|L2^- is 1 and at L2^-|T2^- is l2+1. The Q-extra count puts one Q in L2[1,l2-1], and the F_1-rows 3, 4 with the window T1[t1,9+t1] force L2[l2] into Q. The F_2-row at T2|L2^- (T2[last]+v+L2[1+l2,9+l2]) with the window L2[l2,9+l2] gives label(T2[last])=label(L2[l2]); the F_2-row at L2^-|T2^- contains L2[1,l2+1] and T2's last 9-l2 vertices, hence both. Impossible.

**Result.** Same-centre 4+4 class (b) is impossible. With v41, same-centre 4+4 reduces to class (a)-II. Remaining m8: same-centre 4+4 (a)-II; distinct-centre 4+4; distinct 3+5 connected or reverse-pair; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
