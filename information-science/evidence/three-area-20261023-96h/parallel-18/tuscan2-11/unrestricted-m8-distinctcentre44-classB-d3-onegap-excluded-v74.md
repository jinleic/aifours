# Actual Tuscan11 distinct-centre 4+4, class (b), d = 3, one-gap case — the three remaining sub-cases are excluded

Actual `/bin/date` before this body: **Mon Oct 26 10:16:51 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze). Written after the parent's explicit future-only primary direction (record v64).

## 1. Imports and their status

**From v73** (SHA256 `cacab65beffc1e347212d8aca03df0d70d08ae78033a1d03be1f78fc98e45afc`, UNREVIEWED): the F_2 row list of §2, the T2 result |m3 − beta'| = 4 of §3, the loop conditions delta ∈ {4, 6} with their side conditions of §4, and the b_v placement rule of §5.

The sentence at v73 LF60 receives ZERO credit under parent v60. It is not mined or repaired here, and nothing below relies on it. The alternative that sentence addressed is an F_1 boundary at u = m2, which by the spacing also puts one at m2+10. That is a boundary coincidence with the F_2 cuts L_w[m2] and L_w[m2+10], which the distinct-cut-label rule and (L3) of v57 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`) already exclude.

**The conclusion is conditional on v73 §§2–5 as stated.**

Notation is as in v73: x_s = L(T1[s]), y_s = L(T2[s]) and ν_y = L(L_v[y]). Every row carries 11 distinct labels. For two rows sharing some vertices, the labels of the vertices in one row but not the other equal those of the vertices in the other row but not the first (the **exchange identity**).

**Rows used.** The two F_2 rows containing b_v are
- W_f0 = L_v[10−β'..1], v, T2[1..β']
- W_b0 = T2[m3..1], v, L_v[p−1..10−β']

The two F_1 rows containing b_v are R_a (ending at F_1-position 40 ≡ 0 and continuing into T1) and R_d (containing b_v(2a+q)). With F_1-boundary residue phi0, these are [phi0−10, phi0] and [phi0+20, phi0+30], by v73 §5.

## 2. Case A (m3 = β'+4) with delta = 4: impossible

Here β' ∈ 1..5, m2 ∈ {4,5}, q = 6+2m2, a = 9+β'−m2 ≥ 4+β', p = 16−2β', 2a+q = 24+2β' and phi0 = 3+β'.

- **R_d** = [23+β', 33+β']. It starts in T1^- at s = (24+2β')−(23+β') = β'+1, since a+q = 15+β'+m2 ≤ 23+β'. It reaches L_v at y = 9−β'. So R_d = T1[β'+1..1], v, L_v[1..9−β'].
- **R_a** = [33+β', 43+β']. It runs from L_v at y = 9−β' through b_v into T1, ending at T1[β'+3] (interior, since a ≥ β'+4). So R_a = L_v[9−β'..p−1], v, T1[1..β'+3].

Exchange of W_f0 and R_d. They share b_v and L_v[1..9−β']. So

    {ν_(10−β')} ∪ {y_1..y_β'} = {x_1..x_(β'+1)}.        (A1)

Exchange of W_b0 and R_a. They share b_v and L_v[10−β'..p−1]. So

    {y_1..y_(β'+4)} = {ν_(9−β')} ∪ {x_1..x_(β'+3)}.       (A2)

By (A1), ν_(10−β') ∈ {x_1..x_(β'+1)}. By (A2), that set lies in {y_1..y_(β'+4)}. So ν_(10−β') = y_j for some j ≤ β'+4.

But W_b0 contains both L_v[10−β'] and T2[1..β'+4], whose labels are distinct. Contradiction.

## 3. Case A (m3 = β'+4) with delta = 6: impossible

Here β' ∈ 1..4 (v73 §5), m2 ∈ 4..9 with a ≥ 1, phi0 = 5+β' and 2a+q = 24+2β'.

**R_d** = [25+β', 35+β'] contains b_v(24+2β'), since β' ≥ 1.
- For β' ≥ 2 it starts in T1^- at s = (24+2β')−(25+β') = β'−1. This is valid since a+q = 15+β'+m2 ≤ 25+β'.
- For β' = 1 it starts at b_v itself.
- In all cases R_d ends at L_v[11−β']. So R_d = T1[β'−1..1], v, L_v[1..11−β'], with an empty T1 part when β' = 1.

Exchange of W_f0 and R_d. They share b_v and L_v[1..10−β']. So

    {y_1..y_β'} = {x_1..x_(β'−1)} ∪ {ν_(11−β')}.          (A3)

So ν_(11−β') = y_j for some j ≤ β'.

But W_b0 = T2[β'+4..1], v, L_v[p−1..10−β'] contains T2[j]. It also contains L_v[11−β'], because p−1 = 15−2β' ≥ 11−β' for β' ≤ 4. Two vertices of one row carry the same label. Contradiction. No m2-dependence arises.

## 4. Case B (m3 = β'−4) with delta = 6: impossible

Here β' ∈ 6..9 (v73 §7), m2 ∈ {0,1}, a = 1+β'−m2, q = 14+2m2, p = 24−2β', 2a+q = 16+2β' and phi0 = β'−3.

- **R_a** = [β'+27, β'+37] = L_v[11−β'..p−1], v, T1[1..β'−3].
- **R_d** = [β'+17, β'+27]. It starts in T1^- at s = β'−1, since a+q = 15+β'+m2 ≤ β'+17. So R_d = T1[β'−1..1], v, L_v[1..11−β'].

Exchange of W_b0 and R_a. They share b_v and L_v[11−β'..p−1]. So

    {y_1..y_(β'−4)} ∪ {ν_(10−β')} = {x_1..x_(β'−3)}.      (B1)

Exchange of W_f0 and R_d. They share b_v and L_v[1..10−β']. So

    {y_1..y_β'} = {x_1..x_(β'−1)} ∪ {ν_(11−β')}.          (B2)

By (B1), ν_(10−β') ∈ {x_1..x_(β'−3)}. By (B2), that set lies in {y_1..y_β'}. So ν_(10−β') = y_j with j ≤ β'.

But W_f0 contains both L_v[10−β'] and T2[1..β']. Contradiction.

## 5. Result

Assume the v73 reduction (§§2–5). Then the three sub-cases it left open are impossible:
- Case A with delta = 4;
- Case A with delta = 6;
- Case B with delta = 6.

Case B with delta = 4 was excluded in v73 §6. So class (b) with d = 3 and one gap row is impossible (WRITTEN, conditional on v73 §§2–5).

With v54 (d = 7), v57 (d = 5) and v58 (d = 3 with two gaps), the only class-(b) case left is **d = 1** (r1 = 5, r2 = 6, b = a+5, p+q = 50−2a).

Other open lines are as in manifest v14-delta (SHA256 `2d71c89496eb219b354968f7b806574d01c52d4c79d70bad267d04b42825fce6`): R4 (distinct 3+5 connected), R5 (distinct 3+5 disconnected, except Type I with r_P = 2) and R6 (all m ≥ 9).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the NEW parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
