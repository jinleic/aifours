# Actual Tuscan11 distinct-centre 4+4, class (a)-II, two-row P2 carrying both cuts — impossible

Actual `/bin/date` before this body: **Mon Oct 26 03:39:18 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Distinct-centre 4+4, class (a)-II (v44, SHA256 `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`): b_v, b_w of degree 4, threads T1..T4 from b_v to b_w, P2 = T4 T3^-, P6 = T1 T2^- T3 T1^- T2 T4^-, three deg-2 copies each of v and w. A face's rows are its v-visits plus 1 if it holds the v-cut (same for w), so r_P2 = 1+a_v+eps_v = 1+a_w+eps_w with a_x the number of x-copies on T3, T4 (each met once in P2). This packet treats **r_P2 = 2 with a_v = a_w = 0 and both cuts in P2**.

## 2. Rigid structure

P2's only v- and w-visits are b_v and b_w, which are the cuts, so its two rows are v T4[1,9] w and w T3[9,1] v: |T3| = |T4| = 10, T3 and T4 carry no copy, and T3[1,9] and T4[1,9] each list the nine ordinary labels. Then |T1|+|T2| = 35, P6 has nine rows and no v- or w-cut, so every P6-row holds exactly one v and one w. With l = |T1|, P6-positions are: b_v at 0, 35, 45+l; b_w at l, 45, 80; T1 on [0,l] and T1^- on [45,45+l]; T2^- on [l,35] and T2 on [45+l,80]; T3 on [35,45]; T4^- on [80,90]. All six copies lie on T1 or T2, and **each copy has one visit before 35 and one after 45** (a T1-copy at s visits s and 45+l-s, a T2-copy at s visits 35-s and 45+l+s).

The special-free 10-edge T3 puts b_v (35) and b_w (45) at the same band value e in consecutive rows; likewise b_w (80) and b_v (90) share a value f. The row boundaries form one class mod 10, so 35-e = 80-f (mod 10): **f-e = 5 (mod 10)**. The four rows through these corners, compared with the P2-rows, give

`T2[1,e] = {w}+T3[11-e,9]`, `T1's last 10-e = {v}+T3[1,9-e]`, `T2's last f = {v}+T4[1,f-1]`, `T1[1,10-f] = {w}+T4[f+1,9]`,

so these segments contain copies w_A, v_A, v_B, w_B respectively, which are the w or v of those rows; the third copies are v_C, w_C.

## 3. e = f+5 (f in 1..4)

Boundaries at 10k-f. Row 0 = [-f,10-f] holds b_v(0) and w_B; row 3 = [30-f,40-f] holds T2[1,e] (so w_A) and b_v(35); row 4 holds b_w(45) and v_A's visit 45+a (a <= 5-f); row 8 holds v_B's visit 80-d (d <= f) and b_w(80). Hence b_w(l) is in neither row 0 nor row 3, so 10-f < l < 30-f, and b_v(45+l) lies in rows 5-7 = [50-f,80-f]. These three rows need three v's. v_A's visits are l-a and 45+a, v_B's are l+d and 80-d, none in rows 5-7, and v_C has only one visit after 45. So rows 5-7 hold at most two v's. Impossible.

## 4. f = e+5 (e in 1..4)

Boundaries at 10k-5-e. Row 0 = [-5-e,5-e] holds b_v(0) and T1[1,5-e] (so w_B); row 4 = [35-e,45-e] holds T2[1,e] (so w_A) and b_v(35); row 5 holds b_w(45) and v_A's visit in T1^-'s first 10-e; row 8 = [75-e,85-e] holds T2's last 5+e (so v_B) and b_w(80). So b_w(l) avoids rows 0 and 4, and b_v(45+l) avoids rows 5 and 8: 10-e < l < 30-e, and b_w(l) lies in rows 1-3 = [5-e,35-e]. These need three w's. w_B's visits are b <= 5-e (row 0) and 45+l-b, w_A's are 35-c (c < e, row 4) and 45+l+c, so neither meets rows 1-3, and w_C has only one visit before 35. So rows 1-3 hold at most two w's. Impossible.

**Result.** In distinct-centre 4+4 class (a)-II, r_P2 = 2 with both cuts in P2 is impossible. Open in (a)-II: r_P2 = 2 with at least one cut in P6, and r_P2 = 3, 4, 5 (v46 constrains them); class (b); distinct 3+5; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
