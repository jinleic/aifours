# Original Tuscan-2(11), entire m = 9 distance-two branch, part 14: the distance-two lemma D2Q, the mirror reduction of types C and E, and type E (1,1,0,0) with x1 = 9 excluded

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-nLambda2-dead-all-types-v124.md` (SHA256 `bcef74d17513f60b8b0405dd5696ef39cd2271d7983899a983b30ab5310eed25`). Notation is that of v116 §2 (type E), with Lemma KS (v120 §1) and the arm table (v115 §2).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. §1 is the first use of the distance-two condition (R3) in this branch. §3 also uses (R1)–(R2).

## 1. Lemma D2Q (uses R3)

**(R3).** Every ordered pair of labels occurs at most once as a distance-two event, that is, as the pair (r_i, r_{i+2}) inside one row. In H, a vertex y that is interior to its row in some passage, with path-neighbours x and z in that passage, produces the event (L(x), L(z)). A 2-vertex passes twice, in opposite directions. So if neither passage of y is on a cut, y produces both orders.

**Lemma D2Q.** Suppose the following:
- P = (a, b, c, d) and P′ are vertex-disjoint 4-vertex paths with L(P) = L(P′) = Q;
- write q1..q4 = L(a), L(b), L(c), L(d);
- the interior vertices of P and of P′ are 2-vertices, and none of their passages is on a cut.

Then:
1. By (E), the six edges of P ∪ P′ carry the six pairs of Q, so P′ = (c, a, d, b) up to reversal.
2. The interior vertices produce both orders of {q1,q3} and {q2,q4} (from P), and of {q3,q4} and {q1,q2} (from P′).
3. Let Π be a sub-path of one row that is vertex-disjoint from P ∪ P′. Two Q-labelled vertices of Π:
   - are never adjacent on Π, by (E);
   - if they are at distance 2 on Π, they form the pair {q1,q4} or {q2,q3}, by (R3), because the middle vertex is interior to that row.

These two remaining pairs are disjoint, so two consecutive gaps of length 2 are impossible. Hence:
- **three Q-labels on Π need |Π| ≥ 6** (gaps 2,3 or 3,2, and the 2-gap pair is one of the remaining pairs);
- **four Q-labels on Π need |Π| ≥ 8** (gaps 2,3,2).

This strengthens Lemma KS. KS alone forbids only three Q-labels inside four consecutive vertices.

## 2. Mirror reduction of types C and E

Row reversal maps a Tuscan-2 array to a Tuscan-2 array. In H it maps type (x,y,z) to (σx, σz, σy) with σ = (1 3) (v114 §1), so C and E map to themselves with t1 and t3 exchanged. A cell (n1, n2, n3, nΛ) therefore maps to (n3, n2, n1, nΛ).

Up to the mirror, the live cells of each of types C and E (after v124) are five:
- (0,2,0,0);
- (1,1,0,0), which covers (0,1,1,0);
- (0,1,0,1);
- (1,0,1,0);
- (1,0,0,1), which covers (0,0,1,1).

## 3. Type E, cell (1,1,0,0), with x1 = 9

### Set-up

**Lengths.** a = 5, b = 6, and:
- ℓ1 = 10 + p1 + u;
- ℓ2 = 15 − u;
- λ = 10 + p2 − p1;
- ℓ3 = 10 − p2 + u.

**The arm table.** With n1 = 1 it gives ρ1 = x1 + 5 ∈ {4, 6}, so x1 ∈ {9, 1}. Take x1 = 9, so ρ1 = 4. Then:
- u ≤ 6;
- x0 ≡ x1 + 5 − p1 forces x0 = 14 − p1, hence p1 ≥ 5.

**F1 rows.**

| Row | Vertices |
|---|---|
| R_out | ℓ, T_int, b4, t1[1..u] |
| r1 | t1[u..u+10] |
| r2 | t1[u+10..u+9+p1], b5, Λ[1..10−p1] |
| r3 | Λ[10−p1..λ−1], b5, t3[ℓ3−1..u] |
| R_in | t3[u..1], b4, T_int, ℓ |

**F2 positions** (mod 60). K3 sits at x0 and t1[j] at 24 + u − j. Then:
- b4 at 24 + u, and t2[j] at 24 + u + j;
- K2 at 39, and Λ[k] at 39 + λ − k;
- K1 at 49 + p2 − p1.

The v-order is K3, V1, V2, K2, K1, V2, with one per row. K1 lies in row 4, so p2 ≤ p1 and λ ≤ 10.

**F2 rows.**

| Row | Vertices |
|---|---|
| s0 | T3, K3, t1[ℓ1−1..u+14] (T3 is the x0 vertices before K3) |
| s1 | t1[u+14..u+4] |
| s2 | t1[u+4..1], b4, t2[1..6−u] |
| s3 | t2[6−u..14−u], K2, Λ[λ−1] |
| s4 | Λ[λ−1..1], K1, A |
| s5 | the rest, up to the s0 cut |

Here A = t2[14+p2−p1−u..14−u], with |A| = 1 + p1 − p2.

s2 must contain V2, so u ≤ 5.

### Exchanges

| Label | Rows exchanged | Result |
|---|---|---|
| (a) | r1, s1 | Q := L(t1[u..u+3]) = L(t1[u+11..u+14]), saturated |
| (b) | r2, s0 | L(T3) = L(t1[u+10..u+13]) ⊔ L(Λ[1..10−p1]) |
| (c) | r2, s4 | L(t1[u+10..u+9+p1]) = L(Λ[11−p1..λ−1]) ⊔ L(A) |
| (d) | r3, s4 | L(t3[u..ℓ3−1]) = L(Λ[1..9−p1]) ⊔ L(A) |

In (a), the paths P = t1[u+11..u+14] and P′ = t1[u..u+3] have interior vertices t1[u+1], t1[u+2], t1[u+12] and t1[u+13]. None is on a cut, because the t1 cuts are at u, u+10, u+4 and u+14. So D2Q applies to Q, with qi = L(t1[u+10+i]).

**Fact (e).** Q ∩ S = {c1}. The row s2 contains t1[1..u+3], so the S-labels on t1[1..u] and the Q-labels on t1[u..u+3] meet only at t1[u].

### Sub-case A: p2 ≤ p1 − 4

Here T3 ⊆ t3[u..ℓ3−1]. By (b), L(Λ[10−p1]) ∈ L(T3). By (d) it then lies in L(Λ[1..9−p1]) ⊔ L(A), and it is not in L(Λ[1..9−p1]) because r2 is a row. So L(Λ[10−p1]) ∈ L(A).

By (c) it is then a label of t1[u+10..u+9+p1]. But r2 also contains Λ[10−p1]. Contradiction.

### Sub-case B: p2 ≥ p1 − 3

Here T3 = t3[u..ℓ3−1] ⊔ B3 with |B3| = 4 + p2 − p1. Comparing (b) with (d), and using (c), which makes L(A) disjoint from L(Λ[1..10−p1]):

    L(A) ⊆ L(t1[u+10..u+13])   and   L(B3) = (L(t1[u+10..u+13]) ∖ L(A)) ⊔ {L(Λ[10−p1])}.

**B3 ⊆ t3[1..u−1]** (that is, u + p1 − p2 ≥ 5). Then s5 = t2[14+p2−p1−u..1], b4, t3[1..p1−p2+u−4]. Exchanging s2 with s5 gives:

    L(t1[1..u+4]) = L(t2[7−u..14+p2−p1−u]) ⊔ L(t3[1..p1−p2+u−4]),

and this contains Q. Two facts restrict where Q can sit:
- The t3 piece lies in t3[1..u−1], so its Q-labels lie in Q ∩ S = {c1}.
- The t2 piece and A both lie in row s3 and meet only at A's first vertex. So at most one label of L(A) lies on the t2 piece.

Since L(B3) ⊆ S, (e) gives |{q1,q2,q3} ∖ L(A)| ≤ 1. So k := |{q1,q2,q3} ∩ L(A)| ≥ 2. These k labels lie in Q, so each sits on the t2 piece (at most one) or on the t3 piece (only c1). Hence:
- k = 2, and c1 ∈ L(A);
- the remaining label q_c ∈ {q1,q2,q3} ∖ L(A) lies in L(B3) ∩ Q ⊆ {c1}, so q_c = c1 ∉ L(A).

Contradiction.

**B3 reaches b4** (e := 4 + p2 − p1 − u ≥ 0). Then B3 = t2[e..1], b4, t3[1..u−1], and s5 = t2[e..e+10] (or t2[10..1], b4 when e = 0). Exchanging s2 with s5 gives:

    L(t2[7−u..e+10]) ⊇ L(t1[1..u+4]) ⊇ Q.

That path is a sub-path of row s3 with 8 + p2 − p1 vertices, disjoint from P ∪ P′. By D2Q, p2 = p1, so |A| = 1.

Now L(B3) holds two labels of {q1,q2,q3}. On B3:
- t2[1..e] lies in row s2 with P′, so it carries no Q-label;
- t3[1..u−1] carries only c1 among Q;
- b4 carries w.

Hence w ∈ Q. A W then lies on each of t1[u+1..u+3], t1[u+11..u+14] and t2[7−u..e+10], which uses all three W's. Row r3 = Λ[10−p1..9], b5, t3[ℓ3−1..u] then contains no w-vertex. Contradiction.

## 4. Result

**WRITTEN, D2Q uses (R3):**
- Lemma D2Q (§1);
- the mirror reduction of types C and E to five cells each (§2);
- type E, cell (1,1,0,0), with x1 = 9 is impossible (§3).

**Residual:**
- Type E (1,1,0,0) with x1 = 1 (ρ1 = 6, p1 ≤ 5, p1 ≤ p2), together with its mirror (0,1,1,0).
- The other type C and E classes, the type A and B b = 3/b = 4 cells with nΛ = 0, and L1 types 1–4 and 7–12, all as in v124 §4.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
