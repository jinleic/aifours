# Author response to the v169-A and v169-B reviews: corrected Lemma DP★′, the v95 r_T = 4 replacement, and four errata

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4). This is an ADDITIVE author response under Main directions v215 (`SPR-idle-and-Tuscan-four-review-additive-response-direction-v215.json`, SHA256 `bde783275d4a153f3b576d015d479aa181a4b60e8c8beb160ff5a4ca92e6ff30`) and v217 (`Tuscan-v215-LF60-adjacent-review-statement-reconciliation-and-safe-ranges-v217.json`, SHA256 `07b025693026704c575984f17bebf40f47fca780221c0019b3d127c525434ecd`).

**Reviews answered:**
- v169-A, by InfoSPR7-2: `information-science/evidence/three-area-20261023-96h/parallel-18/robust-spr7/peer-review-v169-A-v1.md`, SHA256 `caaff8b161d41cb5cec13eeb6721f0a0755aa03cb653a38c807b031a2d7f2983`.
- v169-B, by PhysicsMOQLS8-2: `physics/evidence/three-area-20261023-96h/parallel-18/moqls8/peer-review-v169-B-v1.md`, SHA256 `220686cefddce4e48a810d6269b857a8162c5ce6f0f012363bab618d128b23b6`.

**Frozen files.** No frozen or pinned file is edited. Every correction below is a new statement that the parent may adopt or reject. Nothing here is parent-adopted, and none of it is a review verdict.

**Method.** It is written reasoning only: no interpreter, eval, enumeration, solver, program or search was used. It is not reviewed, formal, kernel-checked or novelty-cleared.

## 1. v165 Lemma DP★: answer to v169-A M2 and v169-B F1 (MAJOR)

### 1.1 Concession

The findings are correct. The literal hypothesis of v165 §1 is that every F′-row used shares no vertex with the two F-rows, and that this holds automatically if F′ ≠ F. That hypothesis is never satisfied in the uses made of it:
- the backward rows run along the same physical split vertices θ[j] as the forward rows;
- for example, θ[s+ρ..s+10] is common to θ[s..s+10] and to θ[s+ρ..s+ρ+10];
- different faces do not make the same graph vertices different.

So the literal lemma is vacuous as printed, and the "automatic" sentence is false. The position-range "Disjointness" paragraphs in v165 §2 and v208 §2 do not establish that literal hypothesis either.

### 1.2 Corrected statement: Lemma DP★′

**Hypotheses.**
- θ is a thread or a loop of the split graph H, with interior vertices θ[1..L−1] (all of degree 2) and end vertices θ[0], θ[L] (branches; θ[0] = θ[L] for a loop).
- One pass of θ contains two consecutive pure θ-rows θ[s..s+10] and θ[s+10..s+20], with 1 ≤ s and s + 20 ≤ L − 1. Hence L ≥ 22.
- No face condition and no vertex-disjointness condition is assumed. The other pass may lie in the same face or in another face.

**Conclusion.** The configuration is impossible in any actual Tuscan-1 array, that is, under (R1)–(R2) alone.

**Imports.**
- Actual rows are simple paths of H: a repeated vertex repeats its label in a row.
- Every face of the turn map has period 10r with r ≥ 2 (v1).
- Each label has exactly one cut.
- Exactness (E).
- DP-1 and DP-2 of v114 §2 at their stated hypotheses. These are reconstructed independently in v169-B P6 and v169-A §2.4.

### 1.3 Proof

Index the other pass by the same θ-indices. Let ρ ∈ {0, …, 9} be the shift of its cut grid against the forward cuts at s, s+10 and s+20. A "backward row θ[a..a+10]" is the row of the other pass that runs from index a+10 down to index a.

**ρ = 0, 1, 2, 3, 7, 8, 9.** These are exactly as in v165:
- **ρ = 0** puts two cuts on the vertex θ[s].
- **ρ ∈ {1, 2, 3}:** compare θ[s..s+10] with the backward row θ[s+ρ..s+ρ+10]. Its indices are at most s+13 ≤ L−1, so the row is interior.
- **ρ ∈ {7, 8, 9}:** compare θ[s+10..s+20] with the backward row θ[s+ρ..s+ρ+10]. Its indices lie in [s+7, s+19], so it is interior.

In each case both rows are interior θ-paths, so their common physical vertices are exactly the common index interval. The two difference paths are interior θ-paths at disjoint index intervals, of size ρ or 10 − ρ ∈ {1, 2, 3}. DP-1 applies: size 1 puts one label on two cuts, and sizes 2 and 3 contradict (E).

**ρ ∈ {4, 5} (B-chain, as in v165):**
- P1 = θ[s..s+ρ−1] and P1′ = θ[s+11..s+10+ρ] come from θ[s..s+10] against the interior backward row θ[s+ρ..s+ρ+10].
- P2 = θ[s+10..s+9+ρ].
- P2′ is the part of the backward row R′ = θ[s+10+ρ..s+20+ρ] at backward indices s+21..s+20+ρ.

**ρ = 6 (C-chain, as in v165):**
- P1 = θ[s+17..s+20] and P1′ = θ[s+6..s+9] come from θ[s+10..s+20] against the interior backward row θ[s+6..s+16].
- P2 = θ[s+7..s+10].
- P2′ is the part of the backward row R′ = θ[s−4..s+6] at backward indices s−4..s−1.

In both chains, P1, P1′ and P2 are interior θ-paths, and only R′ can leave θ:
- in the B-chain, past θ[L] when s+20+ρ ≥ L, with at most ρ − 1 ≤ 4 vertices before θ[L] in its face walk;
- in the C-chain, past θ[0] when s ≤ 3, with at most 3 vertices after θ[0].

**Claim.** R′ meets the forward row compared with it (θ[s+10..s+20] in the B-chain, θ[s..s+10] in the C-chain) exactly in the displayed common interval. P2′ shares no vertex with P1, P1′ or P2.

**Proof of the claim.** The interior θ-vertices of R′ at the displayed indices lie in disjoint index intervals, and θ[0], θ[L] are not interior. A vertex of R′ outside θ's displayed range could still be an interior θ-vertex θ[j] in only two ways:

1. **Through the other directed pass of θ** (the forward pass). An interior vertex has degree 2, so the face walk from a forward-pass vertex continues along θ to θ[L]. In the B-chain the walk would have to reach θ[L], leave it and later re-enter θ[L] to start the backward pass, all within R′. In the C-chain it would have to leave through θ[0] and re-enter θ[0] before reaching θ[j]. Either way R′ would contain the end vertex θ[L] (or θ[0]; for a loop, b = θ[0] = θ[L]) twice. That repeats a label in one row, which is impossible.
   - This step is the argument of BDP in v169-A §5.2 ("its exit and reentry would repeat the same θ-end branch in that row"). It is credited to InfoSPR7-2, `peer-review-v169-A-v1.md` §5.2.
2. **Through the same directed pass, by wrapping once around its face.** Let P be the face period. Its face contains all L edges of the backward pass, so P ≥ L ≥ s + 21 ≥ 22.
   - In the B-chain, a backward index i ∈ [s+21, s+20+ρ] would equal a central index j ≥ s. So P = i − j ≤ 20 + ρ ≤ 25.
   - In the C-chain, an index i ∈ [s−4, s−1] would equal a central j ≤ s + 20. So P = j − i ≤ 24.
   - In both chains, if the colliding j lies in the compared forward row, the bound is even smaller: P ≤ 10 + ρ ≤ 15, or P ≤ 14.
   - So 22 ≤ P ≤ 25. No multiple of 10 lies there, which contradicts the period 10r. This face-period guard is also BDP's (v169-A §5.2), credited to InfoSPR7-2.

Hence, in each chain:
- the exchange of R′ with the compared forward row gives L(P2′) = L(P2);
- the first exchange gives L(P1) = L(P1′);
- P1 and P1′ are vertex-disjoint;
- P2 overlaps P1′ in ρ − 1 vertices (B-chain) or 3 vertices (C-chain), which is the shift-by-one of DP-2;
- P2′ is vertex-disjoint from P1 ∪ P1′ ∪ P2, so its edges are new, and it is a simple path because R′ is an actual row.

DP-2 then excludes block sizes 4 and 5, which covers ρ = 4, 5 and 6. All ten shifts are excluded. ∎

### 1.4 Callers

Every use of DP★ in the author files v165–v208 cites exactly the hypothesis of DP★′: two consecutive pure rows of one pass of a thread or loop, with 1 ≤ s and s + 20 ≤ L − 1. The uses were located by grep for "DP★" over the author's files; the lines below are the operative uses.
- **v165 §2:** R6, R7 on Λ.
- **v166 (c), (d) LF58–63 and (e) LF65.**
- **v171 LF32 (DP).**
- **v173:** LF52 (B, C on Λ) and LF71 (the two rows at ΛV).
- **v183:**
  - LF37 (nΛ ≤ 1);
  - LF87 (2,0,0);
  - LF89 (0,2,0);
  - LF92 (DP★ on t1);
  - LF108–109 (on t1 and on Λ);
  - LF120 (on Λ).
- **v185:** §3 LF55–60, Case (i), and LF67 (u ≤ 5).
- **v186:** LF35, LF47, LF51 and LF55.
- **v188:** LF90.
- **v192:** LF19.
- **v195:** LF20.
- **v198:** LF14.
- **v199:** LF13, with its erratum (b).
- **v208 §2:** R2, R3 on t2.

Each of these places verifies that both rows are pure rows of a single pass inside θ's interior. That is the full hypothesis of DP★′, so every such use stands with DP★′ in place of DP★.

The extra "Disjointness" paragraphs (v165 §2, v208 §2) and the "other pass is in F1/F2" remarks are now unnecessary. They are neither used nor claimed to establish the old literal hypothesis.

v196 cites DP★ only in its import line (LF3); grep shows no operative use in its body.

This audit relies on the callers' own texts, re-read only at the grep lines shown. It is an author statement, not a review.

## 2. v95 §6, r_T = 4: answer to v169-A M1 (MAJOR)

### 2.1 Concession

The finding is correct. v95 §6 asserts "A_w = 2 (one w on each middle row)". But the w-vertex of M1 and the w-vertex of M2 may be the single shared cut vertex Λ[u+10]. In that case the w-cut lies in F_T, ε_T = 1 and A_w = 1. The two-distinct-w inference, and the "at least two full loop rows" step built on it, are unproved as printed. (v169-B P3 reconstructs the printed route. v169-A's objection stands, and the author accepts it.)

### 2.2 Replacement proof (no w-count)

In v95 §6 (r_T = 4, λ = 40 − 2t = 2u + 20), F_T has the rows R_out, M1 = Λ[u..u+10], M2 = Λ[u+10..u+20] and R_in (v95 §2). M1 and M2 are consecutive pure Λ-rows of one pass, with s = u ≥ 1 and s + 20 = u + 20 ≤ λ − 1 = 2u + 19.

Lemma DP★′ (§1) excludes this. So **r_T = 4 is impossible** for every tail length, with no assumption about A_w, ε_T or the position of the w-cut. This is B95's argument (v169-A §5.1, InfoSPR7-2), here routed through DP★′.

DP★′ and its imports (v1, v114 §2) do not depend on v95, so the route is not circular. The r_T = 2 and r_T = 3 parts of v95 keep their own printed arguments.

## 3. v107 LF20: answer to v169-A m1 and v169-B F2 (MINOR)

**Erratum.** In v107 LF20, "The other four vertices of c are 2-vertices" should read **"The other three vertices of c are 2-vertices"**.

A non-special label has exactly four 2-vertices in the nine-row component H: d_H = 8 and r_H = 9. One of them is the cut vertex, covering three rows; the other three pair off the remaining six rows. The displayed matchings in v107 use three vertices, as does v113 (M). No conclusion changes.

## 4. v148 LF134: answer to v169-A m2 and v169-B F4 (dependency label)

**Erratum.** v148 LF134 says "(R3) enters through D2Q at δ = 4 only." It should read **"(R3) enters through D2Q at δ = 4 and at δ = −4, in the {c1, γ} subcase of LF127."**

Consequences:
- The δ = −4 exclusion of type A (0,2,0,0) is a T2 statement (it uses (R3)). It is not a T1 statement.
- The whole-cell composition of v148 with v149 is likewise not T1-only.
- v151's (R3) accounting must carry this qualification.
- No T1-only proof of the δ = −4 branch is claimed.

## 5. v185 LF67 heading: answer to v169-B F3 (MINOR) and the v169-A §3 note

**Erratum.** The heading "**u ≤ 6.**" should read **"u ≤ 6 is impossible."** The text under it excludes u ≤ 5 (two pure t1-rows, now by DP★′) and u = 6 (b3 on the cut 30), and the proof continues with u ≥ 7.

## 6. v145 LF37: the v169-A §3 notational slip

**Erratum.** "δ = −5 (m = 5) and δ = −6 (m = 4)" should read **"δ = −5 (m = 5, block size 10 − m = 5) and δ = −6 (m = 6, block size 10 − m = 4)"**. Here m = −δ (v145 LF9), and DP-2 is applied to block size 10 − m ∈ {4, 5}. No value changes.

## 7. Items not answered here

The NR entries of v169-B §§4–5 and of v169-A §6 are not findings against the source. Both reviews say so explicitly. They need no repair or rebuttal, and none is offered.

v169-A §4 (the S308/v73 LF60 boundary) is respected: this file does not open, quote or use v73 LF60, v73 §4 or later, v74, or part19 physical line 843.

## 8. Result

**WRITTEN:**
- Lemma DP★′, with proof (§1.3). Two steps of the proof are credited to BDP (InfoSPR7-2, v169-A §5.2).
- All listed DP★ callers rest on DP★′.
- v95 r_T = 4 is excluded through DP★′ (§2, crediting B95).
- The errata of §§3–6.

**OPEN:**
- Every item of the frozen residual is unchanged:
  - m = 9: types 2/12 with r2 = 2;
  - types 2/12 with r2 = 3 α3 k = 1 (v199 lies outside the freeze);
  - types 1/11 with r1 ∈ {4, 5};
  - type 8 with r1 ∈ {3, 4}.
- Every NR edge named by the reviewers is open.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried, and so is the Main217 parent process MAJOR together with the author's recorded v215 exposure (v150b-B v2 LF1–169 displayed; lines 19, 69, 126 and 142 are NONINPUT and unused). This candidate needs its own complete source-bound gate.
