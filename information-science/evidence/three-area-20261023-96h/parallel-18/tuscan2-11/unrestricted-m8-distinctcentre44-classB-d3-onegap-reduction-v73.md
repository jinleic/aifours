# Actual Tuscan11 distinct-centre 4+4, class (b) with d = 3, one-gap case — reduction

Actual `/bin/date` before this body: **Mon Oct 26 09:45:20 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting

Class (b) and the tools (L1)-(L3) are as in v57 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`). The faces are:
- F_1 = T1 L_w T1^- L_v, with 4 rows;
- F_2 = T2 L_w^- T2^- L_v^-, with 7 rows.

The lengths are a = |T1|, b = a+15, p = |L_v| and q = |L_w|, with p+q = 40-2a.

By v58 §2 (SHA256 `359258f8cb25627b086b6fb5873ff8607540c49865d47a3ffe081d84d0bb46d3`), the remaining case is **n_f = n_b = 3**: each F_2 pass over T2 meets three rows, and one further row lies in a loop gap. Exchanging v and w swaps L_v and L_w and keeps both face words (up to rotation), so take the gap row on L_w.

Further imports:
- the rule (R), bd clash, bd chain and shift-5 lemma of v49 §4 and v50 §2;
- the comparison of rows of the two passes of a doubly traversed thread, as used in v60 §3 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`);
- distinct cut labels.

Labels are x_s = L(T1[s]), y_s = L(T2[s]), ν_y = L(L_v[y]) and ω_u = L(L_w[u]). Coordinates on a loop run in F_1's direction.

## 2. F_2's rows

Put b_v(0) at F_2-position 0. Let beta' in 1..9 be the first forward boundary. (beta' = 10 would put b_v twice in one row, since p >= 1.) Write:
- b = beta'+10+m1;
- b+q = beta'+30+m2;
- 2b+q = beta'+50+m3;

with m1 in 1..10, m2 in 0..9 and m3 in 1..9. Then:
- a = 5+m3-m2;
- q = 10+2m2-m3+beta';
- p = 20-beta'-m3;
- m1 = 10+m3-m2-beta';
- a+q = 15+beta'+m2.

The seven rows, in F_2 order, are:
- W_f0 = L_v[10-beta'..1], v, T2[1..beta']
- W_f1 = T2[beta'..beta'+10]
- W_f2 = T2[beta'+10..b-1], w, L_w[q-1..m2+10]
- O_w = L_w[m2+10..m2]
- W_b2 = L_w[m2..1], w, T2[b-1..10+m3]
- W_b1 = T2[10+m3..m3]
- W_b0 = T2[m3..1], v, L_v[p-1..10-beta']

In T2-coordinates, the forward rows start at beta'-10, beta' and beta'+10, and the backward rows at m3-10, m3 and m3+10.

## 3. The two passes on T2: |m3 - beta'| = 4

W_f1 and W_b1 do not leave T2. Every overlapping pair of opposite-pass rows is clean, except (W_f0, W_b0), which both leave through b_v, and (W_f2, W_b2), which both leave through b_w.
- (W_f1, W_b1) has k = |m3-beta'|. (L3) excludes 0, so this is 4, 5 or 6 when we also use (W_f1, W_b0) or (W_f1, W_b2), each with k = 10-|m3-beta'|.
- **m3-beta' = 5:** (W_b0, W_f1) and (W_b1, W_f2) are clean with starts beta'-5, beta', beta'+5, beta'+10. This is a shift-5 chain.
- **m3-beta' = -5:** (W_f0, W_b1) and (W_f1, W_b2) form a shift-5 chain.
- **m3-beta' = 6:** (W_b0, W_f1) and (W_b1, W_f2) are clean k = 4 pairs with starts beta'-4, beta', beta'+6, beta'+10. This is a bd chain.
- **m3-beta' = -6:** (W_f0, W_b1) and (W_f1, W_b2) form a bd chain.

Hence **m3 = beta'+4 (Case A) or m3 = beta'-4 (Case B)**. In both cases W_f1 and W_b1 end in complementary P4s.

## 4. O_w and the loops: delta in {4, 6}

O_w = [m2, m2+10] in L_w-coordinates does not leave L_w. F_1 has exactly one boundary strictly inside it, at u = m2+delta. (A boundary at u = m2 or m2+10 would coincide with an F_2 cut and cut a label twice.) Both F_1 rows there are clean against O_w, with k = delta and 10-delta, so delta is 4, 5 or 6.
- **delta = 5.** F_1's boundaries sit at F_1-positions ≡ a+m2+delta, so on L_v they sit at y ≡ delta+5-beta' (mod 10). F_2's L_v boundary is y = 10-beta', an interior vertex of L_v. For delta = 5 the two coincide, which cuts a label twice. Hence **delta ≠ 5**.
- **delta = 4.** If m2 >= 6, then (W_b2, F_1-row [m2-6, m2+4]) is clean, and it forms a bd chain (starts m2-10, m2-6, m2, m2+4) with (O_w, [m2+4, m2+14]). So **m2 <= 5**.
- **delta = 6.** (F_1-row [m2-4, m2+6], O_w) and (F_1-row [m2+6, m2+16], W_f2) form a bd chain unless both of the latter leave L_w through b_w(b). That happens iff m2+16 > q, i.e. m1 >= 5. So **m1 >= 5**.

The parameters then are:
- **Case A:** beta' in 1..5, m2 in 4..9, q = 6+2m2, a = 9+beta'-m2, 2a+q = 24+2beta', p = 16-2beta', m1 = 14-m2.
- **Case B:** beta' in 5..9, m2 in 0..5, q = 14+2m2, a = 1+beta'-m2, 2a+q = 16+2beta', p = 24-2beta', m1 = 6-m2.

## 5. F_1's rows and b_v

F_1's boundary residue is phi0 = (a+m2+delta) mod 10. The four rows are [phi0+10k, phi0+10k+10]. b_v(0) lies in the row ending at phi0 (or is that boundary). The row holding b_v(0) = b_v(40) must not also hold b_v(2a+q), so:
- **phi0+20 <= 2a+q < phi0+30**.

This gives:
- Case A with delta = 6: phi0 = 5+beta' (0 if beta' = 5), so **beta' <= 4**.
- Case B with delta = 4: phi0 = beta'-5, so **beta' <= 8**.

## 6. Case B with delta = 4 is impossible

Here the rows R_a = L_v[9-beta'..p-1], v, T1[1..beta'-5] and the F_2 rows W_b0, W_f0 give two exchanges:
- **(7) W_b0 vs R_a:** {y_1..y_(beta'-4)} = {ν_(9-beta'), x_1..x_(beta'-5)}.
- **(5) W_f0 vs R_a:** {ν_1..ν_(8-beta'), y_1..y_beta'} = {ν_(11-beta')..ν_(p-1), x_1..x_(beta'-5)}.

The cases by beta':
- **beta' = 5:** (7) reads y1 = ν4. But T2[1] is the F_2 cut T2[m3] and L_v[4] is the F_1 cut R_d|R_a, so two cuts share a label.
- **beta' = 6:** (7) reads {y1, y2} = {ν3, x1}. The F_2 cut label y2 would have to equal the label of the F_1 cut L_v[3] or of the F_1 cut T1[1].
- **beta' = 7, 8:** by (7), ν_(9-beta') is some y_j with j <= beta'-4, so by (5) it lies in {ν_(11-beta')..ν_(p-1), x_1..x_(beta'-5)}. All of these share the row R_a with L_v[9-beta'], so they differ from ν_(9-beta'). Contradiction.
- **beta' = 9:** excluded by §5.

## 7. Case B with delta = 6 and beta' = 5 is impossible

Here R_a = L_v[11-beta'..p-1], v, T1[1..beta'-3]. W_b0 vs R_a gives {y_1..y_(beta'-4), ν_(10-beta')} = {x_1..x_(beta'-3)}. For beta' = 5 this reads {y1, ν5} = {x1, x2}. Both y1 = T2[m3] and ν5 = L_v[10-beta'] are F_2 cut labels, x2 is the F_1 cut T1[beta'-3], and they cannot both equal x1. Contradiction.

## 8. Result

In class (b) with d = 3 and one gap row (taken on L_w), the following must hold:
- |m3 - beta'| = 4 and delta is 4 or 6;
- Case B with delta = 4 is impossible;
- Case B with delta = 6 needs beta' >= 6 (and m2 <= 1);
- Case A with delta = 6 needs beta' <= 4.

The open sub-cases are:
- **Case A, delta = 4:** beta' in 1..5, m2 in {4, 5};
- **Case A, delta = 6:** beta' in 1..4, m2 in 4..9 with a >= 1;
- **Case B, delta = 6:** beta' in 6..9, m2 in {0, 1}.

Class (b) with d = 1 is untouched here. Other open lines are as in manifest v14-delta (SHA256 `2d71c89496eb219b354968f7b806574d01c52d4c79d70bad267d04b42825fce6`).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
