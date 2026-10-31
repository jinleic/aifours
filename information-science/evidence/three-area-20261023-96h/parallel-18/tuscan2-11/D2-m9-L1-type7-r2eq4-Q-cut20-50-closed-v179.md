# Original Tuscan-2(11), entire m = 9 distance-two branch, part 66: L1 type 7 with r2 = 4 — case (Q), cuts at 20 and 50, closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq4-c1-c5-bounds-v-order-pruning-v178.md` (SHA256 `a41c8e7f0fe6593befd2d88d87b3da3ea56ca4ff5196d6681f134f5896e70c78`). Operative imports:
- v173 §1, the full F1/F2 position formulas and arm exchange (SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`);
- v152 §§1–2, anatomy and w's unique cut at ℓ (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v176 §1, Lemma A4 and exactness (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the type-7 mirror of v155 §5, exchanging t1 and t3.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. All variables of the named case remain free until the deductions below.

## 1. Case, coordinates and the short-path restriction

Take case (Q) of v178, with v's cut at t1V = 20. Then n1 = n3 = 1, n2 = nΛ = c′ = 0. Its F1 passages are t in R0, t1V at 20, P2 in R3, P3 in R4, t3V in R5, P5 in R6. Thus:
- ℓ1 ∈ [16,24], ℓ3 ∈ [7,14], ℓ2 = u + 5 and λ + ℓ1 + ℓ3 = 40;
- t1V = t1[u+10], so ℓ1 ≥ u + 11;
- R1 = t1[u..u+10] is pure;
- u ≥ 4 by Lemma A4.

In F2 let A contain b6(0), D contain b6(λ), E contain t3V and C contain t1V, in that cyclic order. Since v has no F2-cut, these are four distinct rows. Write A = [−x,10−x], where 1 ≤ x ≤ 9. Then C = [30−x,40−x]. Since t1V has offset 30−u and is in C's interior, x > u. Put d = x − u.

R1 and C share exactly t1[x..u+10]. Their two differences are vertex-disjoint paths of d vertices: one is t1[u..x−1], and the other is the part of C beyond t1[u+10], running towards b3 and possibly through b3 onto t3. They carry the same label set, since both rows contain every label once.
- d = 1 equates c1, an F1-cut label, with the F2-cut label at C's other endpoint, giving two cuts for one label.
- d = 2 gives two different edges on the same unordered label pair, contrary to (E).
- d = 3 gives two disjoint two-edge paths on the same three labels; four edges cannot use three unordered pairs without repetition, again contrary to (E).

Hence 4 ≤ d ≤ 9 − u. Therefore u ∈ {4,5}; for u = 5, x = 9, and for u = 4, x ∈ {8,9}.

Now P1 = 10−u+ℓ1 lies in [21,30] and P4 = 60+u−ℓ3 in [50,59]. Neither can be a multiple of 10: each is a b3-passage labelled w, whose unique cut is already ℓ. Consequently P1 ∈ [21,29] and P4 ∈ [51,59]. Also P2 ∈ [31,39] and P3 ∈ [41,48].

## 2. At most one F1-cut T_int label

Let τ ∈ T_int have its cut in F1. By anatomy it has one G1-vertex (its T-vertex) and four G2-vertices, with no t2-vertex. The T-vertex supplies R0 and R6. To supply R1..R5, τ needs:
- a t1-vertex in R1;
- a t1-vertex in R2 (whose only other vertices are b3 and t2);
- a Λ-vertex in R3;
- a Λ-vertex in R4;
- a t3-vertex in R5.

Its four G2-passages can cover these five rows only if one of them is a cut serving two adjacent rows among R1..R5. A cut at 10 or 60 would repeat τ in R0 or R6, so the cut is at 20, 30, 40 or 50. Position 20 is v's cut, positions 30 and 50 lie on t2 (P1 ≤ 29 < 30 < P2 and P3 ≤ 48 < 50 < P4), and τ has no t2-vertex. Thus τ's cut must be 40, which lies on Λ because P2 ≤ 39 < 40 < P3. In particular:

**Every F1-cut T_int label is X40, so there is at most one.**

There are four F2-cuts, all different and all in S ∪ T_int: v is cut at 20 and w at ℓ. Since |T_int| = 9 − u:
- u = 4 forces all four F2-cut labels into T_int;
- u = 5 permits at most one F2-cut S-label.

## 3. The case where D contains the whole t3-arm

Write D's upper endpoint as λ + y = 20−x. The endpoint is on t3: b6(λ) lies inside D and t3V lies inside E. Hence 1 ≤ y < ℓ3. The equality y = u would cut c5 twice.

Suppose y ≥ u + 1. A contains b6(0) and the whole t1-arm because x > u. D contains b6(λ) and the whole t3-arm. The arm exchange applied to both rows therefore gives

L(Λ[1..λ−1]) ⊆ {w} ∪ T_int.

Consider an F1-cut s ∈ S \ {c1,c5}. It has one t2-vertex and four G2-vertices, two of which are its arm vertices. As Λ has no S-label, R3 and R4 must both be supplied by the two passes of its single t2-vertex. Its cut can only be 30 or 50: positions 10, 20 and 60 carry c1, v and c5, position 0 carries w, and 40 is on Λ.
- If s = X30, its S_12-pass is 30 and its S_23-pass is 40 + δ, where δ = ℓ1 − ℓ3. (The passes of t2[j] are P2 − j and P3 + j, which sum to P2 + P3 = 70 + δ.) The S_23-pass must lie in R4's interior: δ ≤ 9. Equality δ = 10 would cut the same label again at 50.
- If s = X50, its S_23-pass is 50 and its S_12-pass is 20 + δ. The latter must lie in R3's interior: δ ≥ 11. Equality δ = 10 would cut the same label again at 30.

The two possibilities cannot coexist, so at most one label of S \ {c1,c5} can have its cut in F1.
- For u = 4, all four F2-cuts are T_int-labels, so the two labels in S \ {c1,c5} would both need F1-cuts. Impossible. Moreover u = 4 necessarily has y ≥ u + 1, since the F2-cut t3[y] cannot be an S-label.
- For u = 5 and y ≥ u + 1, at most one F1-cut plus at most one F2-cut can cover the three labels in S \ {c1,c5}. Impossible.

Only u = 5, x = 9, 1 ≤ y ≤ 4 remains.

## 4. The last case: the three T_int cuts and two w-duplications

Here F2's rows are A = [−9,1], D = [1,11], E = [11,21], C = [21,31]. We have λ = 11 − y ∈ [7,10]. Name the four F2-cut labels:
- Z1 = L(Λ[1]);
- Z2 = L(t3[y]) ∈ S;
- Z3 = L(t1[9]);
- Z4 = the cut at offset 21.

There is at most one F2-cut S-label, so Z1, Z3 and Z4 lie in T_int. The fourth T_int label must have an F1-cut, hence is X40 by §2. Thus T_int = {X40,Z1,Z3,Z4}.

A against R0, removing their common t1-arm and b6, gives

L(t1[6..9]) ∪ {Z1} = {w} ∪ T_int,

so L(t1[6..8]) = {w,X40,Z4}.

**If ℓ1 ≥ 20:** C is the pure row t1[9..19]. Against R1 = t1[5..15], it gives

L(t1[16..19]) = L(t1[5..8]) = {c1,w,X40,Z4}.

Since t1[19] is the cut Z4 at offset 21, w lies on t1[16..18]. Its F1-pass is in R2 (positions 21..23), where w also occurs at b3 = P1 ∈ [25,29]. Contradiction.

**If ℓ1 = 19:** b3's F2 offset is 40 − ℓ1 = 21, cutting w a second time. Contradiction.

**If ℓ1 ≤ 18:** b3's offset 40 − ℓ1 is at least 22, so E is the pure row t3[y..y+10]. Its common part with R6 is t3[y..5]. Removing it gives

L(t3[6..10+y]) = {w,v} ∪ T_int ∪ L(t3[1..y−1]).

Hence w lies on t3[6..10+y]. Those F1-positions are 55−y..59, all in R5 because 1 ≤ y ≤ 4. But w also occurs there at P4 ∈ [51,59]. Contradiction.

Every case is impossible. The type-7 mirror gives the same conclusion for the cut at t3V = 50.

## 5. Result

**WRITTEN:** Type 7 with r2 = 4, case (Q) of v178, is impossible when v's cut is 20 or 50, for every allowed value of every variable.

**OPEN (m = 9, L1):**
- type 7 with r2 = 4: case (P) and its mirror; case (Q) with the cut at P2 = 30 or P3 = 40;
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4,5,6};
- type 8 with r1 ∈ {3,4}, and with r1 = 5 and ℓ1 − u ∈ [11,19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
