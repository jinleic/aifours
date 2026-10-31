# Original Tuscan-2(11), entire m = 9 distance-two branch, part 32: type B (0,2,0,0) with δ ∈ {6, 5, −4} closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L2k3-typeB-0200-setup-delta4-closed-v143.md` (SHA256 `56d58c824eec5be0b3072f555121e3aa7fd529116ad9bd7ad099ab000c9dbb27`), whose notation, rows and anatomy it uses. RC is v134 §1, and (K5) is v141 §1.

This uses (E), (C), RC and pair counting only; no distance-two step is needed. It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. δ = 6

**Set-up.** G = A′ + 6 and H = A′ + 16. Since H ≤ ℓ2 − 1 = A′ + 9 + p3, we have p3 ≥ 7.

**The saturated block.** Exchanging R4 with r2 gives a saturated 4-block Q = L(t2[A′+7..A′+10]). The partner path is the four vertices of r2 after t2[A′], whatever form r2 takes.

**The exchange of R5 with r1.** These rows share t2[A′+10..A′+16], so

    L(t2[A′+6..A′+9]) = L(Π4),   where Π4 = t2[A′+17..A′+9+p3], b5, Λ[14−p1..p4]

is the last four vertices of R5. The left side consists of G\* (at the cut t2[A′+6]) and three Q-labels.

So three Q-labels lie on a 4-vertex path, and two of them are adjacent. That edge repeats a Q-pair, against (E). **δ = 6 is impossible.**

## 2. δ = 5

**Set-up.** G = A′ + 5 and H = A′ + 15, so p3 ≥ 6.

**The blocks.**
- Exchanging R4 with r2 gives Q″ := L(P″) = L(P‴). Here P″ = t2[A′+6..A′+10], and t2[A′+10] is β's cut. P‴ is the five vertices of r2 after t2[A′].
- μ := L(t2[A′+5]) = G\*, which is not in Q″.
- Exchanging R5 with r1 (shared vertices t2[A′+10..A′+15]) gives

      {μ} ∪ (Q″ ∖ {β}) = L(t2[A′+5..A′+9]) = L(Π5),

  where Π5 = t2[A′+16..A′+9+p3], b5, Λ[14−p1..p4] is the last five vertices of R5. Its end π5 = Λ[p4] is λ2\*'s F1 cut.

**(K5).** P″ and P‴ use eight Q″-pairs. Π5 is disjoint from both and has four edges. If μ were an end of Π5, three of those edges would join Q″-labels, against (K5). So μ is interior, and **λ2\* = L(π5) ∈ Q″**.

**RC rules out λ2\* ∈ Q″.**
- λ2\* ≠ w: an F1-cut w consists of b4, the W at its cut and two group-2 W's, and none of these has a passage in R1 (b4's F1-passages lie in R0, R3 and R7). So λ2\* is an ordinary F1-cut label with exactly two group-1 vertices: Λ[p4] and one more, g. Λ[p4] covers R2 (its S_Λ1-passage) and R5, R6 (its cut).
- Rows R0 and R1 contain no group-2 vertex, since their vertices are ℓ, T, b4, t1, b5 and Λ. So g alone must cover both R0 and R1.
- No group-1 vertex has passages in both R0 and R1 without a cut: T also covers R7, a t1-vertex also covers R2 or R3, and a Λ-vertex also covers R5 or R6. The R0/R1 cut belongs to c1, while λ2\*'s cut is Λ[p4].

This uses neither the form of r0 nor that of r2, so it holds for every A′. **δ = 5 is impossible.**

## 3. δ = −4

**Set-up.**
- G = A′ − 4 and H = A′ + 6.
- x = 6 − p3 ≥ 1 gives p3 ≤ 4, so p4 < 10 − p1.
- Exchanging R4 with r1 gives the saturated block Q = L(P) = L(P′), with P = t2[A′−4..A′−1] (in R3 and r1; t2[G] is G\*'s cut) and P′ = t2[A′+7..A′+10] (in R4 and r0; t2[A′+10] is β's cut).
- r2's interior t3-part is t3[1..ℓ1−2], because ℓ3 − x = ℓ1 − 1.

**Excluded labels.**
- **v:** V_a < G, and V_b ∈ t2[A′+1..A′+5].
- **w:** its W on P and b4 would both lie in R3.
- **α:** its own vertex t2[A′] and P both lie in R3.
- **τ3:** its cut covers R3, as does P.
- **H\*, γ0:** they have only two group-2 vertices.
- **c1:** t1[u]'s second passage must avoid R3, so p1 < 5. Then t1[u] covers R0, R1 and R2, P and P′ cover R3 and R4, and the t3-arm covers R7. R5 and R6 remain, and no group-1 vertex covers exactly those two.

**RC for the candidates.** Every F1-cut Q-label has its third group-2 vertex inside r2, on t3.

| Label | Form |
|---|---|
| G\* | {T, Λ[k1] (R1, R6), Λ[k2] (R2, R5), t2[G], P′-vertex} |
| β, T_int form | {T, t1[k] (R1, R2), t3 ∈ R6 ∩ r2, P, P′} |
| β, S form (p1 ≤ 3) | {t1-arm in t1[ℓ1−4..u−1] (R0, R2), Λ (R1, R6), t3-arm ∈ r2, P, P′} |
| λ1\* | T_int only: {T, Λ[10−p1], t3 ∈ R6 ∩ r2, P, P′} |
| λ2\* | S only, p1 ≤ 3: {Λ[p4], t1-arm in t1[ℓ1−4..u−1], t3-arm ∈ r2, P, P′} |
| c2 | S only, p1 ≤ 3: {t3[u], t1-arm in t1[ℓ1−4..u−1], Λ (R1, R5), P, P′} |

Every T_int label of this list other than G\* needs a slot in t3[u+1..ℓ1−2], which has p1 − 2 vertices.

**The four labels.** Q = {β, G\*} together with two of {λ1\*, λ2\*, c2}.
- **λ1\* ∈ Q.** λ1\* needs a slot, so p1 ≥ 3. Its partner (λ2\* or c2) needs p1 ≤ 3, so p1 = 3.
  - The single slot t3[u+1] goes to λ1\*, so β takes its S form.
  - Then β and the partner both need the single arm vertex t1[u−1].
- **Q = {β, G\*, λ2\*, c2}.** λ2\* and c2 need non-adjacent t1-arm vertices in t1[ℓ1−4..u−1], which has 4 − p1 vertices. So p1 = 1, at t1[u−3] and t1[u−1].
  - β then has no slot (p1 − 2 < 1).
  - It also has no third non-adjacent arm position.

**δ = −4 is impossible.**

## 4. Result

**WRITTEN:** type B (0,2,0,0) is impossible for δ ∈ {4, 5, 6, −4}. Here δ = 4 is v143, and the other three are above.

**OPEN residual:**
- type B (0,2,0,0) with δ ∈ {−5, −6};
- type B (0,1,1,0);
- type A (0,2,0,0) and (0,1,1,0).

L1 types 1–4 and 7–12 remain open. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
