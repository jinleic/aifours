# Author response to the v150b-A v2 and v150b-B v2 reviews: errata, credited repairs and the F-10 pointer

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4). This is an ADDITIVE author response under Main directions v215 (SHA256 `bde783275d4a153f3b576d015d479aa181a4b60e8c8beb160ff5a4ca92e6ff30`) and v217 (SHA256 `07b025693026704c575984f17bebf40f47fca780221c0019b3d127c525434ecd`).

**Reviews answered:**
- v150b-A v2, by MathSun8-2: `mathematics/evidence/three-area-20261023-96h/parallel-18/sun-coset8/peer-review-v150b-A-v2.md`, SHA256 `bf74f5cad04ac249604817e54d46e59e4216581e58dc14165536efa7be45d744`.
- v150b-B v2, by PhysicsMOQLS8-2: `physics/evidence/three-area-20261023-96h/parallel-18/moqls8/peer-review-v150b-B-v2.md`, SHA256 `9c89e3ac1c462da077f76d0ab9b0592fbdfb39cd71beac2fa183283e93e1184c`.

**Frozen files.** No frozen file is edited, and nothing here is parent-adopted.

**Labels used below.**
- "ADOPTED (credited)" means the author adopts the reviewer's written repair as stated in the cited review, credits it by name and path, and adds nothing to it. Where the author checked a repair against the source, the check is stated.
- "ERRATUM" is the author's own correction.

**Safe ranges (v217).**
- v150b-B v2 lines 19, 69, 126 and 142 are NONINPUT. They are not used, not quoted and not adopted here.
- v150b-A v2 F-10 and §3 are used only as the boundary of what to avoid.

**Method.** It is written reasoning only: no interpreter, enumeration, solver or search was used.

## 1. v150b-A v2 F-10 (dependency MAJOR): W_44db, d = 3, one gap

**Conceded.** The contract sentence "v74/W_44db use only v73 §§2-5; LF60 unused" (S120 LF164, manifest v17) is withdrawn. Under the Main217 ruling:
- v73 LF60, v73 §4 (LF61-67), v73 §§5-8 and v74 §§1-5 are ZERO and NONINPUT;
- W_44db for d = 3 with one gap, and through it W_m8, is not credited.

The author's fresh replacement, which uses only v73 LF1-59 and unquarantined material, is a separate successor file (`unrestricted-m8-distinctcentre44-classB-d3-onegap-fresh-W44DB-R-v1.md`), if completed. Its status and exact remaining gap are recorded there and in the final status record. Until such a proof is admitted, W_44db and W_m8 stay NR.

**D1 of v150b-B v2** is the dependency statement about v74 and v73 §6. It lies on NONINPUT line 19 and is not used. It is answered only by supersession: under Main217 the whole v73 §4-and-later / v74 route is ZERO and is replaced by the fresh proof.

## 2. MINOR findings with reviewer-supplied repairs (ADOPTED, credited)

**F-1 (v72 §3.3, w = b1, P = 8; S221 LF152).**
- Defect: the text says {b19, b20} = {b3, b8} and that T3[8..13] carries b8, which contradicts the preceding line.
- ADOPTED (credited): MathSun8-2, v150b-A v2 §2 F-1.
  - (N) for w gives {a3, b20} = {b8, b3}, so b19 = b2.
  - c7 = b3 forces b20 = b3 and a3 = b8.
  - So T3[8..13] carries {b18, b2, b7, v, b4, a1} and no b8.
  - The (N)-for-v equation needs T3[t]'s neighbours to carry b18 and b8. b8 is absent from T3[7..14], and b4 has no admissible neighbour there, so the branch closes.
- Not independently re-derived by the author here.

**F-2 (v38 §4, cut C|A^-, r = 4; S184 LF28).**
- Defect: the case q_2 = C[8] is omitted, and so is the exclusion of K′ at C[9] when q_2 = C[6].
- ADOPTED (credited): v150b-A v2 §2 F-2.
  - In every placement, some m-copy in C[6..8] has C-degree at most 1.
  - That copy therefore sits at Λ[21] with Λ-neighbours {e*, m′}, which repeats the pair {m, m′} already used at C[6]C[7] or C[7]C[8].
  - For q_2 = C[7], both m's would need Λ[21].
- Not independently re-derived here.

**F-5 (v82 §4(iii)).**
- Defect: pC is not excluded from the equalities L(D[1..ω]) = 𝒪_L and L(C[1..10−g1]) = 𝒪_U.
- ADOPTED (credited): v150b-A v2 §2 F-5. If pC lay in either set, its other B-vertex would fall in the run B[b1+11..14] or B[1..b1−1], which lies in the same row (Q2 or Y0). So pC would appear twice in that row.
- The inequalities alone give g1 ∈ {7, 8}. With this repair the equalities used by v87/v88 hold.

**F-6 (v88), together with v150b-B v2 M1 (the v88 §4 precision cluster).** The author checked the items against v88 LF40-96, as read in this session.
- **F-6(a):** the bound π ≤ ω + 6 must not cite the v81 offset lemma literally, because R_P2 and Q1 share b_w at their far ends. ADOPTED (credited, v150b-A v2 F-6(a)): the same case analysis gives the bound. Shifts k = 2 or 3 force a repeated w-pair at b_w, and k = 1 is impossible.
- **F-6(b) = M1(a):** v88 §4 says "In each of the eight admissible orders of B[3..6], s_w's two neighbours contain exactly one of pA, pC". ERRATUM, crediting v150b-A v2 F-6(b):
  - In six of the eight orders, s_w's two neighbours contain exactly one of pA, pC, and B14 is the other.
  - In the remaining two orders, s_w's neighbours are {pA, pC}. Then the pair {w, B14} (B14 ∈ {pA, pC}) is already used at b_w–B14, an immediate repetition.
  - So w is adjacent to both pA and pC in every surviving order.
- **M1(b), the Q1/Q2 row name:** in v88 §4 LF72 ("the exchanges with Y0 and with Q1 (that is, R_P1 against B[7..14])"), the row is the one given by the explicit description "R_P1 against B[7..14]". The name "Q1" there is read as that row. It is not the §3 row "Q1 = B[13..14], w, D[10..3]" of LF49. Only the explicit description is used.
- **M1(c), the undefined o\*:** in v88 §4 LF78 (p = 4, x = 9), "C11 = o\*" means C11 = ℓB12, the label of B12. The definition is taken from v150b-B v2 §2 (the v88 (2,7) list, a usable line). For the same case, F-6(c) is ADOPTED (credited, v150b-A v2 F-6(c)): "force C7 = v" is overstated. The v-copy sits at C7 or at C10, and in both placements the pair {ℓD2, ℓB7}, already used at A[2..3], is repeated. The contradiction stands. The author adds no placement detail beyond the reviewer's statement.
- **M1(d), the omitted alternative A9 = v at p = 4, x = 10:** ERRATUM. Besides u = D3, which repeats v–pD (LF80), the v-copy may sit at A9 = A[x−1]. A[x−1] is the A-vertex next to b_w: compare LF81, where A10 = A[x−1] at x = 11 is next to b_w. So v at A9 would create a second v–w edge besides the unique edge b_v–A1 (LF72), against Lemma U. This is the reason already given in the p = 3, x = 10 line (LF75), and it uses only the position A[x−1], not p.
- **M1(e), the implicit variant split:** ERRATUM. v88 §§3-4 treat only the pure variant. The through-b_w variant is excluded for every (b1, g1) in v88 §2, as v88 §5 states. The split is exhaustive.

**F-11 (v77 §7; S226 LF82-83).**
- Defect: the S1 restriction (β_P = 6 + t − K, with N1's B-copies in (ρ−10, ρ−5]) and the S2 restriction (K + β_P = 26) are asserted without derivation, and v78 §3 and v83 consume them.
- ADOPTED (credited): MathSun8-2, v150b-A v2 §2 F-11.
  - For S1:
    - with Δ = (ρ − 10) − β_P, rule (R) on the clean pair (R_Pmid, N1) gives |Δ| ∈ {4, 5, 6};
    - τ = 5 + t − K ≥ 1 gives ρ ≥ 16, so Δ ≥ −3;
    - Δ = 5 is the shift-5 chain N2, R_Pmid, N1, R_P*;
    - Δ = 6 is the bd chain on the same rows;
    - so Δ = 4, which is β_P = 6 + t − K;
    - the v/w row-placement argument then puts N1's copies in (ρ−10, ρ−5].
  - For S2: K + β_P = 26, from two inside-A rows at offset 4. Offsets 5 and 6 fall to the shift-5 and bd patterns, and 34 is impossible since K < 25.
- v150b-B v2 independently PAID the S1 phase ("offsets 6 and 5 fall to chains, leaving 4").
- Not independently re-derived by the author here.

## 3. MINOR and EDITORIAL errata (author's own)

**F-3 (v23, citation).**
- v23's citation "v22 §2 (Case S/Case T window complements)" is wrong: v22 §2 contains only (E) and (I).
- ERRATUM: the complement facts used in v23 are the window-complement statements written out in v31 §2. They are elementary consequences of (E), (I) and the window exchange, as v150b-A v2 F-3 re-derives. v23's argument is otherwise unchanged.

**F-4 (v40):**
- **(a) EDITORIAL:** in Λ = B, cut C|D^-, r = 6, "O minus {q_1}" should read **"O minus {q_2}"**.
- **(b) MINOR, ADOPTED (credited, v150b-A v2 F-4(b)):** the r = 4 clause omits x_D = 1. That case is closed by the same extra count as v40 erratum v1 (a).
- **(c) EDITORIAL:** in Λ = B, cut D^-|C^-, t′ = 1, "forces x_C = 2" should read **"forces x_C ∈ {2, 3}"**. The closing window argument applies to both values (v150b-A v2 F-4(c)).

**F-7 (v77, D-lemma, EDITORIAL).** The loose parenthetical about σ < τ is deleted. It is unused in v77, and v91 re-derives its own variant (σ + τ ≥ t).

**F-8 (v34 §5, α = 3, EDITORIAL).** The parenthetical "A[1] = q_2" is deleted. The closing contradiction uses only the copies of e′.

**F-9 (S120 LF166 and manifest v17, documentary MINOR).**
- ERRATUM: the bd-chain and shift-5 imports (v49 §4, v50 §2) are used beyond v60, not "only up to v60":
  - v73 imports them at S222 LF16 and uses them in §3 (LF51-54, inside the admissible LF1-59);
  - v75 imports them at S224 LF15 and uses them at LF64-65;
  - v77 imports them at S226 LF10;
  - v80 imports them at S229 LF16.
- Those uses are valid at their stated hypotheses (v150b-A v2 F-9). No mathematical effect.

**v150b-B v2 D2 (cap and existence wording, MINOR).** ERRATUM to every header phrase "v24 caps the ladder at m<=36" (v29-v93) and to v93 §5's "capped at m ≤ 36" and "shows nothing about Tuscan-2 existence":
- R6 is ALL m ≥ 9, subject only to m + 2N2 + β = 110 with 0 ≤ β ≤ 11.
- The v24 control's finite facts are not replayed or accepted. Even if accepted, it would refute only a universal Tuscan-1-only lower bound m ≥ k for k ≥ 37. It is not an upper cap on Tuscan-1 or Tuscan-2 support.
- Every Tuscan-1 exclusion is a necessary condition on any Tuscan-2(11) square. So "shows nothing about Tuscan-2 existence" should read **"does not decide Tuscan-2(11)"**.
- This matches v150b-A v2 §5 (R6) and B24's NR control clause. The author's earlier post-freeze addendum on cap wording is not backdated.

## 4. Items that need no repair

The NR entries are not findings against the source, as both reviews say:
- v150b-A v2: A_m7, A_v12 exhaustiveness, A_R1, A_R2 and the B24 control clause;
- v150b-B v2: the R-* roots of its §3.

The author offers no rebuttal and no repair for them. The author does not rely on the v24 control quantities (m = 36, 78 D2 events, 21 excess), which v150b-A v2 §4 does not accept.

## 5. Result

**WRITTEN:**
- the errata of §§2-3, with the reviewer repairs credited by name and path;
- the concession of F-10;
- the supersession of D1.

**OPEN:**
- W_44db for d = 3 with one gap, and through it W_m8, until a fresh proof is admitted;
- every NR root named by either review;
- the m = 9 residual;
- every m ≥ 10.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried, and so is the Main217 parent process MAJOR with the author's recorded v215 exposure. This candidate needs its own complete source-bound gate.
