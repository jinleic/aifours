# peer-review-v170-A-v1 — fresh written review of the MathSun8-2 Sun8 arbitrary-finite-group union (N136, PACK67, S94, F168)

Reviewer **InfoHinfPreview-2** (slot info-3; original owner InfoHinfPreview). Author **MathSun8-2** (math-6). Clock observed with `/bin/date` immediately before writing this body: **Tue Oct 27 05:57:00 PDT 2026**.

**Authority.**

- Explicit full-body release `institute/runs/three-area-2026-10-23-96h/peer-review-v170-A-explicit-body-release-v1.json` (SHA256 `014b52cfb801b9f457abcab86afd00e4ca574bd7c7716d440aa61ad01b6bc73c`, parent clock 2026-10-27T05:32:44-0700). It was issued after Main's actual complete read of my opaque ACK `peer-review-v170-A-opaque-ack-v1.json` (`cf48a82c2303a6fd6e00d90b5876b6e2e8e4218570fcfe6de9ea57dbb4e4ff7d`, 33 LF, 6150 B, pinned 05:32:18).
- Wave record `peer-review-wave-eighteen-v170.json` (`7baab6ae18a95b0ec5ced9782cfa85eb9f4cd85edb5c14eaa41a8e26006f5bc7`), assignment v170-A. The frozen `post_ack_entire_scope` was read verbatim through its jq field and is answered unchanged.
- Packet receipt `peer-review-wave-eighteen-v170-packet-receipt-v1.json` (`76d1d53882b549b4203fb0166969b1974fd25e9f4da2c9d9dc5fea6a03b40a1b`). The ten literal parts carry the release hashes `620c89e1…`, `45dfa62f…`, `23b9f7ad…`, `65f50b79…`, `bd6fee06…`, `bf2f84a0…`, `bbe6be5d…`, `770d99e8…`, `5c1f0faa…`, `f7f79cca…`.

**Coauditor.** v170-B is PhysicsDepol4-2 (manifest metadata only). I did not read its body.

**Assurance ceiling, stated first.** This is a same-harness, written review with disclosed serial contact (§1). It is NOT blind, NOT cross-family, NOT formal or kernel verification, NOT executable verification, NOT novelty or priority clearance and NOT parent adoption. Every identity below was checked by hand in writing. Nothing was machine-checked. No Eval, interpreter, CAS, calculator, program, enumeration, solver or replay was used; my Eval kernel stayed unused. None of the large bounds was evaluated, approximated or written in decimal form.

---

## 0. Results at a glance

Every item gets two verdicts. MATH asks whether the displayed proof is correct at its stated hypotheses. DEP asks which inputs it consumes, whether each is reconstructed here, ordinary, or named NOT_RECONSTRUCTED (NR), and whether the stated application follows at the stated quantifiers.

| Item | MATH | DEP / APPLICATION / TRUST |
|---|---|---|
| N136 §1: β ≤ 6, seven-retention, identities (1), fixed cells and fibres | RECONSTRUCTED | Ordinary index/coset facts only. Holds for every finite G and every vertex, with no minimum used. |
| N136 (BLIND) | RECONSTRUCTED | Uses only the achieved minimum private SUM in the SAME G. The enlargement is an actual subgroup. |
| N136 §2 three-coset index-2 lemma | RECONSTRUCTED | Ordinary coset counting. No Sun3 import. |
| N136 §3 initial types | RECONSTRUCTED | Uses the stated private 2/5/3 ownership and the no-second-α6 hypothesis. |
| N136 §4, six-source (6,1) | RECONSTRUCTED | Cell budget, coprime fibres, lemma, (BLIND). |
| N136 §§5–6, six-source (3,2) | RECONSTRUCTED | Cell budget, coprime fibres, (BLIND). |
| **N136 direct theorem** | **RECONSTRUCTED**: Q ∈ {1, C2, C2×C2} or {C2, C4, C2×C2} | Valid at its full stated quantifiers. Does not consume 142, 200, 99, 181 or NR-NS. |
| N136 §7 application | VALID COMPOSITION at the cuts in §4.9 | 142 + 99 §§2–5 + 181 II.1–II.4 + A6/A7/Eisenstein. Least-order existence is NR-NS. Q ≤ 4 attaches only to a min-SUM family (N-1). |
| **PACK lemma** | **RECONSTRUCTED** | Ordinary unitary/norm/volume facts. Nonabelian simplicity is essential and is used twice. |
| PACK67 application (DIM, GBOUND, INDEX_BOUND) | RECONSTRUCTED given its inputs | Valid for any ASSUMED finite nonabelian simple G with the exact mixed pair at an actual M ≥ U_i. The least-order route to simplicity is NR-NS. Bounds not evaluated. |
| S94 S5 ⇒ COV | RECONSTRUCTED | Ordinary Schur/trace (N-5). |
| **S94 Theorem 1** (200/142 relaxation) | **RECONSTRUCTED** | Every operative step of 200 and 142 audited (§6.2). Valid at those bodies' exact cuts. |
| **S94 Theorem 2** (cases A/B/C) | **RECONSTRUCTED** | Frobenius reciprocity, Schur, base-pair intersection quantization. |
| S94 §3 application | VALID at the stated cuts | Selected 7-free vertex, or ASSUMED simple G. NR-NS for least-order existence. |
| **F168 Theorem A** | **RECONSTRUCTED**: d ≤ 216 (ℓ ∈ {1,6}), d ≤ 720 (ℓ ∈ {2,…,5}) | Ordinary facts only. No F7/NC7 or research import. |
| **F168 Theorem B** | **RECONSTRUCTED** | Ordinary facts plus A. No minimum, 7-freeness or simplicity used. |
| **F168 Theorem C** | **RECONSTRUCTED**: \|G\| < 109^1036800 and all 7r_l, 7s below it | A, B and the packing argument. Simplicity is an explicit hypothesis. |
| F168 §8 transfer and least-order use | Transfer RECONSTRUCTED | Least-order use is conditional on NR-NS. No infinite-G bound. |
| Antecedent 142 (entire) | Operative uses RECONSTRUCTED | F7-P7 at the named inputs. |
| Antecedent 200 (entire) | Operative uses RECONSTRUCTED | F7-P7 at the named inputs. |
| Antecedent 99 §§2–5 | RECONSTRUCTED | 181 II.1–II.4, A6 simplicity. |
| Antecedent 181 part2 II.1–II.4 | RECONSTRUCTED | A7 simplicity, Eisenstein, Sylow/Cauchy. II.5–II.9 are read but not operative (§8.4). |
| Least-order parent cut (S213) | Scope 2 RECONSTRUCTED. Scope-3 consequences RECONSTRUCTED at ASSUMED simplicity. Existence descent NR-NS. Scope 1 NR, not operative. | §8.5 |

**Totals.** 0 FATAL, 0 MAJOR, 0 MINOR in mathematics and in dependency/application. Seven notes (N-1 … N-7, §11) have no severity. Process items are retained in §12, including Main's documentary process MINOR on my stage-1 metadata ordering.

---

## 1. Contacts, independence and exposure

None of the following verdicts is transferred. This review is NOT blind and NOT independent of these contacts.

1. **Own older Sun reviews.** For this review I opened each only at its first line, to identify it. Their verdicts are not inputs.

   | Own review | First line (subject) | LF | SHA256 prefix |
   |---|---|---|---|
   | `peer-review-Sun-degree-seven-v1.md` | "Bounded reconstruction — no degree-seven P7 image and pair generation" | 136 | `fd8e7d4f` |
   | `peer-review-sun8-exact-rank4-normalizer-v1.md` | "v32-C: exact rank-four normalizer reconstruction at named N2/Q4 imports" | 199 | `d887ad7b` |
   | `peer-review-sun8-three-character-global-v1.md` | "v80-B — TC-GLOBAL for arbitrary finite Q…" | 248 | `7441397e` |
   | `peer-review-v129-B-v1.md` | "v129-B — ENTIRE direct-P7 rank-free, same-simple-group, and arbitrary-group existence review" | 299 | `1c7bebc0` |

   **Material overlaps.**
   - The degree-seven review concerned an older degree-seven P7 image argument. That is the same territory as the F7-P7 and NC7 inputs reconstructed in §8.3–§8.4.
   - v129-B reviewed the rank-free 178 body, which is CONTEXT here (S214). Its §§6–7 use the same Farey-gap variance bound and the same unitary minimum-distance packing argument that reappear in F168 §§3–4, §7 and in PACK67 §1. This review is therefore serial, same-author and same-technique.
   - Every verdict below is re-derived from the v170 packet text.
2. **Other own reviews.** The opaque ACK disclosed my other reviews (semigroup, Shor, PH, RQLS, privacy, SPR, depolarizing, AME, Olson v163-A). None contains Sun content used here.
3. **Packet-learned exposure about my own primary.** S204 (parent checkpoint 113) lists wave v166:
   - author InfoHinfPreview-2 (my original preview primary);
   - reviewers MathOlson-2-2 and PhysicsPPT44-2;
   - freeze 04:50:04, releases 04:57:57, "No RETURN yet".

   I learned this from packet content after the release. The v170 author MathSun8-2 is not among those reviewers. I know of no reciprocal review relationship with MathSun8-2. My primary stays STOP v111.
4. **Packet-learned process records about my previous review.** S198–S203 (parent v187–v191 and checkpoint 112) were read as CONTEXT. During v170 work I never opened v163 part16. Physical LF850–859 (S242 original LF52–61) was not revisited, and HELD_C889 was not opened. No content of that window is used.
5. **Context only.** The rank-free 178 body (S214), the author requests (S215–S219) and the parents (S213, S220, S221) are context. The S213 cut is reconstructed separately in §8.5 at its mathematical content. No parent or reviewer verdict is inherited.

---

## 2. Coverage ledger

### 2.1 FIRST phase (completed before any assessment)

- **Stage 1 (pre-release).** Serial reads v9 → v10 → v11 → HOLD → intake envelope, as recorded in the ACK.
- **After release.** The release was read entire. The manifest was read at its top-level fields and the v170-A entry (jq). The receipt was read entire.
- **All ten parts were read raw, through their endings, in order:**
  - **Parts 1–7, S1–S197:** parent errata v9–v11, HOLD v2, parent findings, directions, receipts and checkpoints. Context.
  - **Part 8:**
    - S198–S204 (v187–v191, checkpoints 112/113): context.
    - **S205 N136** 136/136, **S206 PACK67** 67/67, **S207 S94** 94/94, **S208 F168** 168/168.
  - **Part 9:**
    - **S209 mixed142** 142/142, **S210 seven-star200** 200/200, **S211 two-source99** 99/99.
    - **S212 kernel-section part2** 181/181, including its END line.
    - **S213 least-order parent** 51/51.
  - **Part 10:**
    - S214 rank-free 178/178 (context);
    - S215–S219 author union requests v3–v7 (35/31/29/43/30 LF);
    - S220 parent 70/70; S221 parent 76/76.
- **Read-frontier checkpoints:**

  | Checkpoint | Clock | SHA256 prefix |
  |---|---|---|
  | cp1 | 05:34:33 | `25a40e24` |
  | cp2 | 05:35:31 | `f7c5e364` |
  | cp3 | 05:37:33 | `384701ed` |

### 2.2 THEN phase (fresh assessment)

- I re-read N136 (part8 LF318–458), PACK67 and S94 (LF459–629) raw.
- F168 and every antecedent (142, 200, 99, 181, S213) had just been read raw (part8 LF630–801; part9 LF1–701). Those reads were used directly.
- The assessment state was saved as cp4 (05:51:33, `1c96b5d5`).
- **No headline substitution.** Every verdict is taken from the bodies, never from the S215–S219 summaries or the parent tables.

---

## 3. Common foundation: named ordinary facts

These are used repeatedly. The facts marked (re-derived) carry load for the new bodies and were checked in writing.

- **O1 Index arithmetic.** Lagrange and index multiplicativity hold. [G:A∩B] is divisible by both [G:A] and [G:B], and [A:A∩B∩C] ≤ [A:A∩B][A:A∩C].
- **O2 Product formula** (re-derived).
  - |AB| = |A||B|/|A∩B|.
  - xA ∩ yB ≠ ∅ iff x⁻¹y ∈ AB.
  - If gcd([G:A],[G:B]) = 1, then [G:A∩B] ≥ [G:A][G:B], so AB = G and every left A-coset meets every left B-coset.
- **O3 Private-coprime pair factor** (re-derived).
  - For indices 7a, 7b with gcd(a,b) = 1: [G:A∩B] = 7abδ with 1 ≤ δ ≤ 7, and δ = 7 iff AB = G. A disjoint pair of left cosets forces δ ≤ 6.
  - **All-conjugate form.** If A·gBg⁻¹ = G, then A's orbit through gB on G/B has full length 7b. A is then transitive, so its orbit through B is full and AB = G. Hence δ_g ≤ 6 for EVERY g.
- **O4 Orbit quantization** (re-derived). If gcd(t,ab) = 1, every orbit of A∩gBg⁻¹ on G/M ([G:M] = 7t) has length a multiple of t/gcd(t,δ_g). The proof: 7t divides 7abδ_g·ℓ. A union of such orbits has cardinality divisible by t/gcd(t,δ_g).
- **O5 Cells and fibres for U ⊴ N.**
  - [N:N∩U_l] = [Q:UW_l/U]·[U:U∩U_l], where W_l = N∩U_l.
  - A coset meets the cell gN in y(N∩U_l).
  - A coset meets the U-fibre zU in a left coset of U∩U_l.
  - Changing the cell representative left-translates every Q-support by one common element.
- **O6 Finite core.** The intersection of the cores of finitely many finite-index subgroups is normal of finite index. Every relevant coset is a full preimage. N_{G/C}(U/C) = N_G(U)/C.
- **O7 Representations.**
  - Averaging gives an invariant inner product, and modules split orthogonally into irreducibles.
  - Schur's lemma holds. Distinct isotypic components are orthogonal.
  - dim Hom_G(C[G/H], C[G/M]) equals the number of H-orbits on G/M, which equals Σ m_X(π)m_Y(π).
  - A transitive permutation module contains the trivial module exactly once.
  - Frobenius reciprocity: dim Z^H = m(Z, C[G/H]).
- **O8 Incidence Grams** (re-derived). For a G-equivariant 0/1 matrix with column weight κ and row weight ρ, I I* has constant eigenvalue κρ and trace equal to the number of ones.
- **O9 Positivity.** A PSD G-equivariant operator acts on a multiplicity-one irreducible W as a scalar λ ≥ 0. Its trace on 1^⊥ is at least λ·dim W.
- **O10 Algebraic integers and polynomial counts.** A rational eigenvalue of an integer matrix is an integer. The polynomials of degree ≤ 2 with zero constant term in D variables span dimension D + D(D+1)/2.
- **O11 Maximum principle** for symmetric nonnegative stochastic idempotents. It is proved in 142 §5 and re-derived here.
- **O12 Farey determinant identity** (re-derived). If a/b < c/d with bc − ad = 1 and k/g lies strictly between, then g = d(bk − ag) + b(cg − dk) ≥ b + d.
- **O13 Moment bound** (re-derived). If no value of Z lies strictly inside (a,b), then E[(Z−a)(Z−b)] ≥ 0, so Var Z ≥ (μ−a)(b−μ).
- **O14 Norms and volume.**
  - The operator norm is submultiplicative and unitarily invariant, and ‖·‖_F ≥ ‖·‖_op.
  - A unitary d×d matrix has ‖·‖_F = √d.
  - M_d(C) is Euclidean of real dimension 2d². Ball volume scales as radius^(2d²), and disjoint open balls lie inside a containing ball.
- **O15 Classical finite-group facts (named, not re-proved).**
  - A6 and A7 are simple.
  - Sylow theorems and Cauchy.
  - A nontrivial normal subgroup of a primitive group is transitive; a transitive group of prime degree is primitive.
  - Eisenstein's criterion.
  - A7 and S7 are 2-transitive on 7 points and transitive on 2-sets.
  - The order-12 subgroup of S4 is A4.
  - GL3(2) has a nonabelian unitriangular Sylow-2 subgroup, acts transitively on flags and on antiflags, and acts 2-transitively on points and on lines.
  - The order-2m regular-sign kernel (m odd) and the generation of A_n by a connected family of 3-cycles are proved inside 181 II.3.
- **O16 Simplicity.** In a nonabelian simple group every nontrivial representation is faithful, and the subgroup generated by a conjugacy class is normal.

---

## 4. N136 — `sun8-mixed-private-235-entire-normalizer-order-four-v1.md` (`e0c68d42…`, 136 LF)

### 4.1 Statement at full quantifiers

- **Family.** G is finite. It has eight pairwise-disjoint left cosets g_lU_l with [G:U_l] = 7r_l and the r_l pairwise coprime. The family is chosen with **minimum Σr_l among all such families in the same G**.
- **Normalizer.** The selected coset is translated to U = U_i. Put N = N_G(U) and Q = N/U.
- **Ownership hypotheses:**
  - 2 | r_i;
  - a neighbour j6 has 5 | r_{j6} and α_{j6} = 6;
  - a distinct neighbour j5 has 3 | r_{j5} and α_{j5} = 5;
  - no other neighbour has α = 6.
- **Conclusion:**
  - six-source (β,c) = (6,1) ⇒ Q ∈ {1, C2, C2×C2};
  - six-source (β,c) = (3,2) ⇒ Q ∈ {C2, C4, C2×C2}.

### 4.2 §1 — β ≤ 6, seven-retention, (1), fixed cells and fibres

**Re-derivation.**

- **β.** V_l = U∩U_l has [G:V_l] = 7r_ir_lβ_l with β_l ≤ 7 by O3. β_l = 7 would give UU_l = G, contradicting disjointness. Hence β_l ≤ 6 for all seven neighbours, hidden or visible, and [U:V_l] = r_lβ_l.
- **Seven-retention.** Suppose 7 ∤ d = [G:N].
  - Then d | r_i, so d is coprime to each 7r_l. By O2, NU_l = G, so every neighbour coset meets N, and [N:W_l] = 7r_l.
  - By O5, [N:W_l] = c_l r_l β_l, so c_lβ_l = 7, giving β = 1 and c = 7.
  - Each projected support avoids 1_Q; otherwise the neighbour meets U.
  - Two overlapping projected supports would put left V_l- and V_k-cosets of coprime indices r_l, r_k into one U-fibre, and those meet.
  - So seven pairwise-disjoint index-7 cosets of Q avoid 1_Q. Their union has q elements and misses 1_Q, a contradiction.
  - Hence [G:N] = 7s and r_i = sq.
- **Identities (1).** α_l = β_lc_l ≤ 7 and [U_l:W_l] = sα_l. The bound α ≤ 7 follows from |NU_l| ≤ |G|.
- **Fixed cells and fibres.**
  - The neighbour meets exactly sα_l left N-cells.
  - In each hit cell its piece is a left W_l-coset with Q-support a left H_l-coset.
  - In each hit U-fibre its piece is a left V_l-coset of index r_lβ_l.

**MATH: RECONSTRUCTED.** **DEP:** O1–O5 only. This holds for every finite G and every vertex, with no minimum. (N-4: coprimality of s and r_l is not needed for (1).)

### 4.3 (BLIND)

**Re-derivation.**

- Visible supports avoid 1_Q, so c ≥ 2.
- Let L ≤ Q miss every initial support, and let U' = π⁻¹(L).
  - U' ≤ N contains U.
  - U' misses every hidden neighbour, because those miss N.
  - U' misses every visible neighbour, because a common point would project into L ∩ support = ∅.
- So {U'} together with the seven unchanged neighbour cosets is a P7 family. Its selected index is 7r_i/|L|, and r_i/|L| divides r_i, so private coprimality is preserved.
- If |L| > 1 the private sum drops, contradicting the minimum. Hence L = 1.

**MATH: RECONSTRUCTED.** **DEP:** the achieved minimum private SUM in the SAME G. The enlargement is an actual subgroup, not an arithmetic divisor.

### 4.4 §2 — three-coset index-2 lemma

**Re-derivation.** Pairwise disjointness forces every δ_ab = 1, by O3 with ambient factor 2. So [P:L_a∩L_b] = 2u_au_b.

Inside L_1 the indices of L_1∩L_2 and L_1∩L_3 are u_2 and u_3, which are coprime. So [L_1:L_1∩L_2∩L_3] = u_2u_3 and [P:∩] = 2u_1u_2u_3.

Counts over the 8u_1u_2u_3 ordered coset triples:

- |E_ab| = 2u_au_b · 2u_c = 4u_1u_2u_3;
- each pairwise event intersection has 2u_1u_2u_3;
- |E_123| is at least the 2u_1u_2u_3 triples with a common point.

The union therefore has at least (12 − 6 + 2)u_1u_2u_3 = 8u_1u_2u_3, the whole universe. So no triple is pairwise disjoint.

**MATH: RECONSTRUCTED.** **DEP:** ordinary counting. No Sun3 or opaque import.

### 4.5 §3 — initial types

**Re-derivation.**

- **Coprimality.** Ownership makes every neighbour r_l odd. r_{j6} is 3-free, r_{j5} is 5-free, and all other r_l are 3-free and 5-free. Since q | r_i, Q is 3-free and 5-free.
- **The α5 neighbour.** α = 5 with c | q forces (β,c) = (5,1). A full footprint cannot be initial, so j5 is hidden.
- **The α6 neighbour.** α = 6 forces (6,1) or (3,2).
- **Other initial neighbours.** c ≥ 2, c | q, c ≤ 7 and c is free of 3 and 5, so c ∈ {2,4,7}. With βc ≤ 7 the types are exactly A2 = (1,2), B2 = (2,2), C2 = (3,2), A4 = (1,4) and A7 = (1,7).
  - C2 would be a second α6, excluded by hypothesis.
  - A c = 1 neighbour cannot be initial.

**MATH: RECONSTRUCTED.**

### 4.6 §4 — (6,1)

**Re-derivation.**

- **Global exclusion of A2, A4, A7.** j6 hits 6s cells with full Q-footprint. Any β = 1, c ≥ 2 neighbour has U-fibre index r_l, coprime to 6r_{j6}. In a shared cell it would meet j6 inside one U-fibre, which O2 forbids. It hits cs ≥ 2s cells while only s cells are free of j6, so a shared cell exists. Hence A2, A4 and A7 are excluded GLOBALLY.
- **Remaining initial supports.** These are B2 = {λ_l = 1} for nonzero characters λ_l: Q → F2.
- **Embedding.** The common kernel misses all initial supports, so (BLIND) makes it trivial. Q therefore embeds in an elementary abelian 2-group.
- **Rank.** If the character rank were ≥ 3, three independent characters would equal 1 together at some x. The U-fibre xU in the initial cell would then hold three pairwise-disjoint left cosets of indices 2r_a, 2r_b, 2r_c with the r's pairwise coprime, contrary to §4.4.
- **Conclusion.** The rank is ≤ 2, so Q ∈ {1, C2, C2×C2}. Q = 1 exactly when there are no initial supports.

**MATH: RECONSTRUCTED.** The rank bound becomes an order bound only after the kernel is proved trivial, which the body does in that order.

### 4.7 §§5–6 — (3,2)

**Re-derivation.** Let K = ker λ be the index-2 subgroup of j6.

- **A2/B2 share λ.** An A2/B2 neighbour has fibre index r_l or 2r_l, coprime to 3r_{j6}. Its cell budget is 2s or 4s against 6s inside 7s, so a shared cell exists. A different character would make the two halfspaces meet, so every A2/B2 neighbour has the same λ.
- **A4 directions lie in K.** An A4 neighbour meets j6's cells (4s + 6s > 7s) with fibre index r_l coprime to 3r_{j6}. Its index-4 coset lies in the other K-coset, so H_l ≤ K. One cell suffices because H_l is fixed.
- **A7 is excluded.** Index 7 and index 2 are coprime, so the supports always meet, and A7 hits all 7s cells.
- **Initial supports.** Every initial index-2 support (A2, B2, j6 if visible) is Q∖K. Initial A4 cosets are pairwise disjoint, because their fibre indices r_l are coprime. Each has q/4 elements and avoids 1_Q, so at most one lies in K.
- **Case: none in K.** K is blind, so q = 2.
- **Case: one coset gH in K.** gH ∩ H = ∅, so H is blind, H = 1 and q = 4.
- **Conclusion.** q ∈ {2,4}, so Q ∈ {C2, C4, C2×C2}.

**MATH: RECONSTRUCTED.**

### 4.8 The direct theorem

**MATH: RECONSTRUCTED** at its full quantifiers, including:

- arbitrary nonabelian or odd starting Q;
- hidden neighbours;
- a possible private-7 owner, whose A7 type is excluded in both cases.

**DEP / TRUST:**

- ordinary facts O1–O5 plus the in-body lemma and (BLIND);
- no consumption of 142, 200, 99, 181, F7, Sun3 or NR-NS;
- same-harness written support only.

### 4.9 §7 application

**MATH: the composition is VALID** at these exact cuts:

- **(a) Any finite G with a 7-free selected vertex.** Take the min-private-SUM family of G and a selected vertex i with 7 ∤ r_i, where N_G(U_i) carries one exact 6s+s neighbour and one exact 5s+2s neighbour (or an S5 five-source, via S94 Theorem 1).
  - 142's original-family consequence with M = N, t = s gives 2 | s | r_i, 5 | r_{j6} and 3 | r_{j5}. Its hypotheses hold: N ≥ U_i, [G:N] = 7s by §4.2, and gcd(s, r_l) = 1.
  - The two-six capacity (99 §5 via §4 and §3) gives no other α6.
  - So every N136 hypothesis holds.
- **(b) Any ASSUMED finite nonabelian simple G.** Take the min-SUM family within G and use every vertex. The owner pattern is 142 §7 (final paragraph), and the capacity follows because G has no index-7 subgroup (§8.5).
- **(c) A least-order existence example.** This is conditional on NR-NS.

**DEP:**

- 142 entire (§8.1);
- 99 §§2–5 (§8.3), at 181 II.1–II.4 (§8.4) with A6/A7/Eisenstein;
- NR-NS for (c).

**Trust note N-1:** the Q ≤ 4 conclusion attaches only to the min-SUM family.

---

## 5. PACK67 — `sun8-mixed-source-simple-group-packing-bound-v1.md` (`de5e1276…`, 67 LF)

### 5.1 PACK lemma

**Statement.** If G is finite nonabelian simple with a nontrivial complex representation of dimension d, then |G| ≤ (4√d+1)^(2d²).

**Re-derivation.**

- **Faithful and unitary.** The kernel is a proper normal subgroup, hence trivial, so the representation is faithful (O16). Averaging makes it unitary.
- **Minimum distance.** δ = min over g ≠ 1 of ‖g − I‖_op is positive, and every conjugate of a minimizer is also at distance δ.
- **Commutator bound.**
  - ([u,v] − I)·vu = uv − vu.
  - uv − vu = (u−I)(v−I) − (v−I)(u−I).
  - So ‖[u,v] − I‖ ≤ 2δ².
- **δ ≥ 1/2.** If δ < 1/2 then 2δ² < δ, so every such commutator is I. All conjugates then commute and generate a nontrivial abelian normal subgroup, contradicting nonabelian simplicity.
- **Separation.** For a ≠ b, ‖a − b‖_op = ‖I − a⁻¹b‖_op ≥ 1/2. Frobenius distance is at least that.
- **Packing.** The open radius-1/4 balls are disjoint and lie in the radius √d + 1/4 ball. Comparing volumes gives |G|(1/4)^(2d²) ≤ (√d + 1/4)^(2d²).

**MATH: RECONSTRUCTED.** **DEP:** O14 and O16. Nonabelian simplicity is used twice (faithfulness and the abelian-normal contradiction) and is essential. No Jordan theorem, CFSG or catalogue is used.

### 5.2 Application: DIM, GBOUND, INDEX_BOUND

**Re-derivation.**

- **Setting.** Let G be finite nonabelian simple with a P7 family and an actual M ≥ U_i, [G:M] = 7t, carrying exact 6t+t and 5t+2t original sources.
- **DIM from 142.**
  - 3 | r5 holds generically.
  - 5 ∤ r6, d = 6 and odd t each give a seven-block quotient. That quotient is faithful because G is simple, so the original family lives in a faithful transitive degree-7 group, contradicting F7-P7.
  - What remains is 2 | t (so 2 | r_i), 5 | r6, 3 | r5, d ≥ 7, and d ≤ 20 if v2(t) = 1 or d ≤ 160 if v2(t) ≥ 2.
- **GBOUND.**
  - d ≤ 20 gives d < 25, √d < 5 and 4√d + 1 < 21. With 2d² ≤ 800 this yields |G| < 21^(2d²) ≤ 21^800.
  - d ≤ 160 gives d < 169 = 13² and 4√d + 1 < 53. With 2·160² = 51200 this yields |G| < 53^51200.
- **INDEX_BOUND.** 7r_l ≤ |G| and 7t ≤ |G|, since an index is at most the group order.
- **The §3 remark.** r_i = s|Q| ≤ 4s when M = N under N136's hypotheses. It is correctly flagged as unused.

**MATH: RECONSTRUCTED** given DIM.

**DEP:**

- **Simplicity.** The body obtains it from the least-order existence reduction, which is **NR-NS** here. The argument holds verbatim for any ASSUMED finite nonabelian simple G with the stated exact mixed pair (N-2).
- **DIM.** It comes from 142 (§8.1) and F7-P7 (§8.3–§8.4).
- **Bounds.** They are symbolic only and not evaluated. No search or certificate is authorized.

---

## 6. S94 — `sun8-five-one-one-single-isotypic-source-extension-v1.md` (`d08cdc32…`, 94 LF)

### 6.1 S5 ⇒ COV

**Re-derivation.**

- **Column span.** The span of the columns g·1_T is C1 ⊕ W_T. The G-average of (2/7)1 + g·v_T equals (2/7)1, because ⟨v_T,1⟩ = 2t − 2t = 0.
- **Shape of I I*.** I I* is self-adjoint and equivariant with image C1 ⊕ W_T. By Schur on the irreducible W_T it equals a·J + b·E_T.
- **Coefficients.** The constant eigenvalue is 2t·2r = 4tr, so a = 4r/7. The trace is 14tr, so b·d = 10tr.

**MATH: RECONSTRUCTED.** N-5 records where the multiplicity-one clause is genuinely load-bearing.

### 6.2 Theorem 1: audit of every operative step of 200 and 142

The relaxed source needs only:

- T is H5-invariant of size 2t;
- column weight 2t and row weight 2r;
- COV with a multiplicity-one W_T.

Each step was checked against that list.

| Body step | Input actually used | Valid for S5? |
|---|---|---|
| 200 §1 / 142 §1: δ ≤ 6 (all conjugates in 142); orbit quantization | Subgroups and indices only | yes |
| 200 §2 / 142 §2: different types ⇒ constant cross-incidence ⇒ forbidden 4t/7 or 2t/7 invariant intersection | Multiplicity one of each W in X; T H-invariant | yes |
| Equal normalized Grams; integer common counts (200 §3; 142 (3)) | COV and 0/1 rows of weight 2r | yes |
| Row classes; columns are unions of classes; b \| t | 0/1 column structure | yes |
| 200 §§3–5: compression, spectrum, c = (6h+7)/5, interpolation, actual 6-clique, L(K7) | COV and actual columns | yes |
| 142 §§3–6: private-5-free blocks, private-3-free contradiction, odd-t 0/1 grid, d = 6 projector, half/quarter grids | I6 (exact), COV for I5, grid for aT6 ∩ bT5 | yes |
| 200 §§6–7 / 142 §7: stars or blocks, M fixes a two-set or block, all-eight lift | The constructed quotient and M ≥ U_i | yes |

No step uses transitivity of H5 inside T after COV.

**MATH: RECONSTRUCTED.** **DEP:** at the exact cuts of 200 and 142 (7-free selected vertex, or ASSUMED simple G with F7-P7). No old verdict is transferred.

### 6.3 Theorem 2 (5t + t + t)

**Re-derivation.**

- **Multiplicity patterns.** dim Hom = 3, and the constants contribute 1. So Σ_nontrivial m_X·m_Y = 2, which allows exactly:
  - A = (1,1) + (1,1);
  - B = (1,2);
  - C = (2,1).
- **Support of v_T.** v_T is H5-fixed and orthogonal to 1. By Frobenius reciprocity it lies in the shared nontrivial components.
- **SHARE.** If E_R·v_T = 0, then by equivariance the cross incidence with R is (2ℓ_R t/7)J. The R∩H5-invariant set T_R ∩ T would then have size 2ℓ_R t/7, a multiple of t/gcd(t,δ). That forces 7 | 2ℓ_R·gcd(t,δ) with ℓ_R ∈ {1,2} and δ ≤ 6, which is impossible.
- **Case C is impossible.** The only shared type has m_X = 2 while W_R has m_X = 1, so they are different types and SHARE fails.
- **Case B gives S5.** v_T lies in the single copy W, generates it, and SHARE gives W = W_R.
- **Case A.** One component is W_R and has a nonzero projection.
  - If the other projection is zero, S5 holds.
  - If both are nonzero, the cyclic span is W_R ⊕ V, the stated open residual.

**MATH: RECONSTRUCTED.** **DEP:** O7 and O4 at the base pair (R, H5), whose indices are private-coprime to each other and to t.

### 6.4 §3 application

- On the enlarged domain:
  - two S5 five-sources fall under 200;
  - an exact 6+1 source together with an S5 five-source falls under 142;
  - N136 uses only α = 5;
  - PACK67 uses only the common W and its dimension.
- Case C is excluded only when an exact two-orbit neighbour is present.

**VALID** at the 7-free cut or ASSUMED simple G. Least-order existence is NR-NS.

---

## 7. F168 — `sun8-one-six-source-proper-orbit-Farey-finite-branch-v1.md` (`26447798…`, 168 LF)

### 7.1 Theorem A

**Hypotheses.** G is finite; [G:M] = 7t; R and H have indices 7r and 7u, with gcd(r,u) = 1 and gcd(t,ru) = 1; they have disjoint left cosets; R has exactly the orbits 6t + t on Ω = G/M; T is any actual nonempty proper H-invariant set of size ℓt, 1 ≤ ℓ ≤ 6.

**Re-derivation.**

- **Grid.** By O3, δ_g ≤ 6 for every g. By O4, z_(a,b) = |aT_R ∩ bT|/t lies in F6 = {k/g : 0 ≤ k ≤ g ≤ 6, g ≥ 1}, because aT_R ∩ bT is a union of orbits of aRa⁻¹ ∩ bHb⁻¹.
- **(2).** R has Hom-dimension 2, so W has multiplicity one in X and in C[G/R]. I_R I_R* = (r/7)J + (6tr/d)E_W: constant tr, trace 7tr.
- **(3).** I_H I_H* has constant eigenvalue ℓ²tu and trace 7ℓtu. Its nonconstant trace is ℓ(7−ℓ)tu. By O9 it acts on W as λ ≥ 0 with dλ ≤ ℓ(7−ℓ)tu. No image, rank or multiplicity claim is made for H.
- **Moments.**
  - The entry sum of I_R* I_H is 7t·r·ℓu, so mean Z = ℓ/7.
  - tr[(I_R I_R*)(I_H I_H*)] = rt·ℓ²tu + (6tr/d)·λd ≤ [ℓ² + 6ℓ(7−ℓ)/d]t²ru.
  - Dividing by 49ru·t² and subtracting (ℓ/7)² gives VAR-UP: Var Z ≤ 6ℓ(7−ℓ)/(49d).
- **Farey gaps.** The pairs (0/1, 1/6), (1/4, 1/3) and (2/5, 1/2) each have determinant 1 and denominator sum 7. By O12 no element of F6 lies strictly between the endpoints of any pair. The pairs bracket 1/7, 2/7 and 3/7 respectively.
- **Lower bounds** (O13):
  - (1/7)(1/42) = 1/294;
  - (1/28)(1/21) = 1/588;
  - (1/35)(1/14) = 1/490.
- **Dimension bounds.**
  - 36·294/49 = 216;
  - 60·588/49 = 720;
  - 72·490/49 = 720.
- **Reflection.** z ↦ 1−z preserves F6 and the variance and maps the means for ℓ = 4, 5, 6 to 3/7, 2/7, 1/7. The products ℓ(7−ℓ) are symmetric.

**MATH: RECONSTRUCTED.** W is R's shared irreducible (N-6).

**DEP:** O2–O4, O7–O9, O12, O13. No F7/NC7, no classification and no research import.

### 7.2 Theorem B

**Re-derivation.**

- **Normalizer identities.** Seven-retention and (5) hold exactly as in §4.2, with no minimum.
- **The α6 source.** α_R = 6 gives an orbit of size 6s through N. Orbit lengths are multiples of s, so the remaining s points form one orbit, and R is an exact 6s+s source.
- **α7 neighbours.**
  - α = 7 forces (β,c) = (1,7), and such a neighbour hits all 7s cells.
  - Q-index 7 is coprime to c_R ∈ {1,2,3,6}, so the Q-supports meet in every shared cell.
  - The fibre indices are r_H and r_Rβ_R, with gcd = gcd(r_H, β_R). That gcd must exceed 1, so r_H owns 2 or 3 and that prime divides β_R | 6.
  - Private coprimality allows at most two such neighbours.
- **Proper-orbit neighbours.** At least four of the six other neighbours therefore have 1 ≤ α ≤ 6.
- **Applying A.** Each such neighbour's orbit through N is a proper invariant set of size αs, and s | r_i gives the required coprimality. Apply A with t = s and ℓ = α.

**MATH: RECONSTRUCTED.** **DEP:** O1–O5 and A. No 7-freeness, minimum, simplicity, no-second-six, abelian Q or initial visibility is used. Every original neighbour is retained, including hidden ones and a private-7 owner.

### 7.3 Theorem C

**Re-derivation.**

- W is nontrivial, so it is faithful for simple G.
- PACK (§5.1) applies with d ≤ 720 < 729 = 27², so 4√d + 1 < 109.
- The exponent identity is 2·720² = 1036800 (720² = 518400). So |G| < 109^(2d²) ≤ 109^1036800.
- Every original 7r_l and the actual normalizer index 7s are at most |G|.

**MATH: RECONSTRUCTED.** **DEP:** A, B, the packing argument and the explicit simplicity hypothesis. The bound is not evaluated. Groups below it are not excluded.

### 7.4 §8: direct infinite transfer and least-order use

**Re-derivation.** The common core of the eight U_l lies in U_i ≤ N. Normalizers transfer exactly by O6: gUg⁻¹ = U iff g(U/C)g⁻¹ = U/C. Indices, q, s and α are preserved.

**MATH: RECONSTRUCTED.** **DEP:** O6. The statement concerns the finite image only. The least-order sentence (LF164) is conditional on NR-NS. The body states that the α6-absent branch is unbounded by this theorem and that arbitrary-group Sun8 remains NOT_PROVED; both statements are accurate.

---

## 8. Supplied earlier bodies: every operative use reconstructed or NR

### 8.1 142 — `sun8-mixed-six-one-five-two-private-235-obstruction-v1.md` (`97f7e607…`)

**Used by:** N136 §7; PACK67 §2; S94 Theorem 1. All operative steps were re-derived.

- **§1, all-conjugate δ_g ≤ 6 and the grid.** By O3 and O4.
- **§2, one shared W.** A different W would give a constant cross incidence 2t/7, forcing 7 | 2·gcd(t,δ), which is impossible.
- **(2).** I6I6* = (r6/7)J + (6tr6/d)E and I5I5* = (4r5/7)J + (10tr5/d)E. Then B = (5A+J)/3.
- **(3).** 3r6c5 = r5(5c6 + r6) gives r6 | 5c6, k ∈ {0,…,5} and c5/r5 = (k+1)/3. At k = 5 both rows are identical.
- **§3.** If 5 ∤ r6, then c6 ∈ {0, r6}. Each column is exactly one class of size t, giving seven blocks, and M fixes its block.
- **§4.** If 3 ∤ r5, then k ∈ {2,5}. The compressed row sum would be 1 + (7h−1)·2/5 = (14h+3)/5, which exceeds h. Contradiction.
- **§5.** gcd(t,15) = 1, so odd t gives 0/1 entries.
  - mean Z = 2/7 and mean Z² = (4 + 60/d)/49. The Frobenius term is 4r6r5t² + 60t²r6r5/d.
  - So d = 6, A = t(E0 + E) and P = A/t is a nonnegative stochastic projector.
  - O11 makes each component an averaging block. The diagonal value 1 makes each component have size t, giving seven blocks.
- **§6.**
  - Z² ≤ Z gives d ≥ 6.
  - On the half-grid, Z² ≥ Z/2, so 4 + 60/d ≥ 7 and d ≤ 20.
  - On the quarter-grid, (Z − 1/4)(Z − 1/2) ≥ 0 at all five points. So mean Z² ≥ (3/4)(2/7) − 1/8 = 5/56, giving 4 + 60/d ≥ 35/8 and d ≤ 160.
- **§7.** The selected image fixes a block, so it lies in a 7-free point stabilizer, while v7(|F|) = 1. The selected index therefore retains 7 and its kernel index is 7-free. The all-eight lift then gives a contradiction with F7-P7.
  - At ASSUMED simple G the quotient is faithful and no 7-freeness is needed.
  - The finite-core transfer holds.

**MATH: RECONSTRUCTED** (operative uses).

**DEP:**

- F7-P7 (§8.3);
- the least-order "every vertex" clause is NR-NS;
- its §8 union statements are context only.

### 8.2 200 — `sun8-two-five-plus-two-sources-seven-star-quotient-v1.md` (`258442f4…`)

**Used by:** S94 Theorem 1 and the S94 §3 application. All operative steps were re-derived.

- **Shared W.** A different W forces 7 | 4·gcd(t,δ), which is impossible.
- **Row classes and compression.**
  - The common normalized count takes values in {0,1,2}.
  - Classes have size b | t.
  - The compressed spectrum is 4h−2, c−2 (multiplicity d) and −2, with c = 10h/d.
- **Parameters.**
  - c is an integer (O10).
  - trace B² = 7h(4h−2) gives c = (6h+7)/5 and d = 50h/(6h+7).
  - d ≤ 5 forces h = 1 and c = 13/5. d = 6, 7, 8 give h = 3, 49/8 and 28.
  - (28,8) would need 196 independent polynomials in a space of dimension 54. So h = 3, d = 6 and the spectrum is 10, 3, −2 with multiplicities 1, 6, 14.
- **Graph structure.**
  - B² = B + 6I + 4J.
  - An actual column gives a 6-clique Z. The vector w = 1_Z − (2/7)1 has ‖w‖² = 30/7 and w*Bw = 90/7, so it attains the top eigenvalue on 1^⊥ and B1_Z = 3·1_Z + 2·1.
  - The 15 outside vertices biject with the pairs of Z, and the whole graph is L(K7).
- **Stars.**
  - Maximal cliques are stars, and the action on them is faithful.
  - Edge-transitivity gives star-transitivity.
  - M fixes an edge, which is a two-set.
- **§7 lift.** The two-set stabilizer has order 2·5! and is 7-free. The lift is the same as in §8.1.

**MATH: RECONSTRUCTED.** **DEP:** F7-P7. The least-order clause is NR-NS.

### 8.3 99 — `sun8-two-source-seven-free-normalizer-exclusion-v1.md` (`109bcd2d…`)

**Used by:** 142 §7, 200 §7, N136 §7 (capacity) and PACK67 (via 142).

- **§2 F7-P7.**
  - **Affine and GL3(2) cases.** Each a_l divides d or 24, so the primes involved are 2 and 3. At least six a_l equal 1. NC7 makes their complement one index-7 coset xL. The remaining two cosets lie inside xL with coprime relative indices, so they meet. If a = a' = 1 they coincide with xL and still meet.
  - **A7 and S7.** Each a_l divides 360 or 720, and the 5-part is 5. If at least six a_l equal 1, NC7 applies again. Otherwise exactly five equal 1 and the three others own 2, 3 and 5, one of them being a = 5 with index 35.
    - Index-7 subgroups are point stabilizers (§8.4), so the five cosets are constraints forming a rook row or column. Inverting the whole group makes it a row.
    - The complement is {g : g(p) ∈ {y1, y2}}. The index-35 subgroup H then has an orbit of size 1 or 2 on p.
    - An orbit of size 2 puts H in a two-set stabilizer of index 21, but 21 ∤ 35.
    - An orbit of size 1 gives index 5 inside A6 or S6. A6 would embed in S5, impossible by simplicity. For S6, the restriction to A6 is either injective, impossible, or trivial, which puts A6 inside H of order 144, also impossible.
- **§3.** An index-7 overgroup at a 7-free vertex gives the all-eight lift, contradicting F7-P7.
- **§4.** For two 6t+t sources:
  - a different W would force an invariant intersection of size t/7, smaller than any orbit length t/gcd(t,d) ≥ t/6;
  - the normalized counts force c_j ∈ {0, r_j}, giving seven blocks;
  - the block stabilizer L ≥ M ≥ U has index 7, contradicting §3.
- **§5.** At most one α6 neighbour per 7-free vertex (with M = N, t = s), and at most one β = 6 neighbour (with M = U).

**MATH: RECONSTRUCTED.** **DEP:** 181 II.1–II.4 (§8.4), A6 simplicity and O15. The references to the old 45LF parent and to Part3 M1 are context only and not operative.

### 8.4 181 part2 — `sun8-global-kernel-section-complete-v1-part2.md` (`2c8949df…`)

**II.1 (core).** Disjoint index-7 cosets have equal cores: a nontrivial normal image of one core would be transitive, giving HK = G. The quotient by that core is faithful of degree 7, and completions lift.

**II.2 (non-2-transitive).**

- Φ7(x+1) = x^6 + 7x^5 + 21x^4 + 35x^3 + 35x^2 + 21x + 7 is Eisenstein at 7.
- λ_t = λ_u iff tS = uS, and λ_0 is distinct from every other eigenvalue.
- The multiplier stabilizer L of S has order 1, 2 or 3:
  - order 1: Aut = C7;
  - order 2: the 7-cycle or its complement, with Aut = D14;
  - order 3: S = {1,2,4} (a Paley tournament, whose stabilizer has order ≤ 3) or its negative, with Aut of order 21.
- In every case F ≤ AGL(1,7), so F = C7:C_d with d ∈ {1,2,3}.

**II.3 (2-transitive).**

- **With a 3-cycle.** A 3-cycle generates A7, so F = A7 or S7.
- **Without one.** v3(|F|) ≤ 1, so |F| ∈ {42, 84, 168, 336, 210, 420, 840, 1680}.
- **Excluded orders.** 210 and 420 by the odd-105 kernel; 840 and 1680 by A7 simplicity; 84 by a normal Sylow-7.
- **42.** This gives AGL(1,7).
- **168.** The group is simple; its normal-subgroup orders were checked and the order-56 case was examined.
  - A size-7 triple orbit exists, by the order-12 triple stabilizer ≅ A4 and the V4 normalizer of order 24 or 168.
  - So F is the Fano collineation group GL3(2).
- **336.** Excluded via the unique 7-orbit of F ∩ A7.

**II.4 (index-7 subgroups and six-coset mixtures).**

- **Index-7 subgroups.**
  - Affine: the stabilizer of the orbit average.
  - A7/S7: a point stabilizer, since without a fixed point the largest orbit-preserving subgroup has order 240 < 360.
  - GL3(2): a point or a line, since a 3+2+2 orbit pattern would need an elementary-abelian Sylow-2 and a basis stabilizer has order 6.
- **Affine completion.** The missing value is −Σy + bΣx for every b.
- **2-transitive rook rows.**
- **Mixed Fano cases.**
  - A disjoint point/line pair needs an incidence flip.
  - The 1+5 and 5+1 splits are impossible (3 versus 4).
  - Both-input or both-output rectangles give at most 1 or 2 per type.
  - The four 3+3, 4+2, 2+4, 3+3 completions were each checked to preserve every flip.
  - Seven disjoint index-7 cosets partition F.
  - Whole-group inversion gives the other orientation.

**MATH: II.1–II.4 RECONSTRUCTED.** **DEP:** O15 (A7 simplicity, Eisenstein, Sylow/Cauchy, primitivity).

II.5–II.9 were read entire. They are not operative for any v170 target or for 99 §2, because they depend on Part1 objects (B, e, kernels) that are not supplied, and II.8 additionally assumes simple G. They receive no verdict; see NR-181 in §9.

### 8.5 Least-order parent cut — `sun-unrestricted-private-and-least-order-source-union-parent-v1.md` (`cc4394a4…`)

| S213 content | Operative for | Status here |
|---|---|---|
| Scope 2: TWO 6t+t sources at a 7-free selected vertex, any G | N136 §7 (capacity), 142/200 (F7-P7) | RECONSTRUCTED (§8.3) |
| Scope 3, consequence: in a finite nonabelian simple G carrying a direct P7 family there is no index-7 subgroup, and no vertex has two 6+1 sources at any actual 7-retaining overgroup | N136 §7(b), 142/200 every vertex, PACK67, S94 §3 | RECONSTRUCTED at ASSUMED simplicity: an index-7 subgroup gives a faithful degree-7 action, contradicting F7-P7; two sources construct one (99 §4) |
| Scope 3, existence: a least-order direct-P7 example exists and is simple (NS104–169, 63LF `dbfe535…`) | Every least-order sentence | **NR-NS, NAMED NOT_RECONSTRUCTED** |
| Direct normalizer identities (LF35) | N136, F168 | RECONSTRUCTED independently (§4.2) |
| Scope 1 (125LF `317f30a4…`) and "at most FIVE α6 at any finite vertex" | None of the four targets | NR (not supplied, not operative) |

---

## 9. NR cuts and caller propagation

- **NR-NS (least-GROUP-ORDER existence descent).**
  - Content: the NS104–169 range, the 63LF composition `dbfe535…`, and the 88LF part II `b401c139…` cited in S221 but not supplied.
  - Callers: 142 §0/§7, 200 §0/§8, S213 scope 3, N136 §0/§7, PACK67 §§2–4, S94 §3, F168 §8.
  - Propagation: each caller is reconstructed only in the form "for every finite nonabelian simple G carrying a direct P7 family …". The clause "a least-order example exists and is simple" is not established here.
- **NR-125.** S213 scope 1 and its at-most-five-α6 corollary. No caller among the targets.
- **NR-181.** Part1 (246LF `b6e3125a…`), Part3, and the non-operative II.5–II.9. No caller among the targets or in 99 §2.
- **NR-ANC.** General Sun8 → direct-P7 reduction, global Sun7, the old F7/G2 DAG with Sun5/MS/B, R4/N2/Q4/Sun3/Sun4, and the all-Sp parent. No target uses them. They bound what can be said about the original target (§10).

---

## 10. Exactly what remains OPEN for the original unrestricted Sun8 target

1. **No global Sun7 and no unrestricted Sun8.** There is no arbitrary-group proof, and no Sun8 → direct-P7 reduction is reconstructed (NR-ANC).
2. **No bound for all P7 groups.**
   - F168 C bounds only finite nonabelian simple G with an α6 neighbour at some vertex.
   - PACK67 bounds only finite nonabelian simple G with the exact mixed pair at an actual M ≥ U_i.
   - Nonsimple or infinite ambient groups get no order or index bound, because the small constituent may be nonfaithful.
   - α6-absent simple configurations are unbounded by the reviewed bodies. S214's rank-free bound is CONTEXT and receives no verdict here.
3. **No witness and no exclusion below any bound.** There is no finite search, emptiness certificate or evaluation.
4. **No normal-composition closure.** No passage from a nonsimple G to a simple section or composition factor is reconstructed here (NR-NS). Least-order existence is NR. Every every-vertex statement holds only at ASSUMED simplicity.
5. **Structural residuals that remain open:**
   - the mixed private 2/5/3 exception with even outer index and 7 ≤ d ≤ 20 or 160, with Q ∈ {1, C2, C4, C2×C2}, and that Q bound only for min-SUM families;
   - S94's two-component case A with both projections nonzero (F168 A bounds only R's W when an exact 6t+t source coexists);
   - X-multiplicity-2 (case C) sources without an exact two-orbit neighbour;
   - configurations with no forced α6 or high-source pair;
   - α ∈ {1,…,4, 7} with no forcing;
   - private-7-owner vertices outside the simple boundary for the 142/200/99 conclusions;
   - odd, nonabelian, maximal, self-normalizing or private-composite legal-enlargement collisions;
   - full coherence of the hidden-neighbour fibres.

---

## 11. Notes (no severity)

- **N-1 (N136 §7).** The order ≤ 4 conclusion attaches only to the min-private-SUM family of G, or of an assumed simple G. A mixed exception that occurs only in a non-minimal family gets 142's owner pattern but not the Q bound. The body's "If those full hypotheses are verified" and "choose a minimum-private-SUM family WITHIN that SAME least-order G" are consistent with this. The point is stated here for clarity.
- **N-2 (PACK67 §2).** The body calls the least-order reduction "adopted". In this freeze it is NR-NS (frozen scope; S220 LF18). The body's own §4 labels the application CONDITIONAL. The proof works for any finite nonabelian simple G with the exact mixed pair at an actual M ≥ U_i, so the least-order hypothesis is only the route to simplicity.
- **N-3 (PACK67 §2).** The phrase "all simpler branches already produce an ACTUAL seven-point quotient" is loose. The private-3-free five-source branch (142 §4) is impossible generically, with no seven-point quotient involved. The conclusion that these branches do not survive is correct.
- **N-4 (N136 §1; F168 §5).** Identities (1) and the integrality of α = βc follow from U ⊴ N and O5 without gcd(s, r_l) = 1. That coprimality is genuinely used elsewhere: orbit lengths are multiples of s, and it is needed for the A hypotheses. This is harmless redundancy.
- **N-5 (S94 §1).** COV itself needs only irreducibility of W_T, because the image of I I* lies in C1 ⊕ W_T. The multiplicity-one clause of S5 is load-bearing in the identification steps: two S5 sources, or an S5 source and an exact two-orbit source, share the SAME E. The predicate as defined is therefore sufficient and its clause is correctly not dropped.
- **N-6 (F168 §0 A).** In "d ≤ 720 with EVERY other-source representation structure, including the genuine two-component 5+1+1 case", W is the exact 6t+t source R's shared irreducible. The bound says nothing about the other source's own components. The formal statement of A is precise.
- **N-7 (142 §2).** The Hom and Schur step is cited "as in 200 §2". It is an ordinary fact (O7) and was re-derived here, so no dependency on 200's verdict arises.

---

## 12. Retained process findings and histories (not cured by this review)

**This assignment.**

- **Documentary process MINOR (Main, in the release).** The pre-read metadata step listed the stage-1 filenames, including two unopened delivery receipts, and ran wc/shasum on the envelope before v9. It was metadata ordering only, with no content read. It is not blind. It is retained.
- **Cadence for this assignment** (all within 30 minutes):

  | Record | Clock |
  |---|---|
  | whole save cp106 (`8eca8bef`) | 05:30:35 |
  | ACK | 05:32:18 |
  | cp1 | 05:34:33 |
  | cp2 | 05:35:31 |
  | cp3 | 05:37:33 |
  | cp4 | 05:51:33 |
  | this body | from 05:57:00 |

**Own findings.**

- Own findings 1–14: whole75 (items 1–11) and whole80/whole84 (items 12–14).
- The 16 post-84 missed cadence spans cp85–cp100 (findings 15–30).
- The **v182 self-release MAJOR**.
- v163-A v1 (`a47758b4…`) remains HELD.
- v163-A v2 (`c6b38f71…`) was actually returned. v194 declared that duty complete. It is not adopted.

**Parent histories.**

- 179 service-gap MAJOR.
- **187 protected formula-transport MAJOR**, with my actual repeat exposure bound by **188**.

**Original preview primary.** STOP v111 stands. The post56/post60/postS126 guides remain ZERO. v166 (my primary under review by others) is noted in §1.3 only.

**Author histories.** The bodies carry permanent author records: OWN057/047/078, COUNT, M1, v26, v31 (two late findings), v33, and the zero-credit withdrawn trial guidance. They are retained as recorded. This review neither evaluates nor cures them, and its mathematical verdicts are not a process-clean certificate.

---

## 13. Nonclaims and assurance ceiling

**What this report supports.** As written reconstructions at their exact stated hypotheses:

- the N136 direct theorem;
- the PACK lemma;
- S94 COV and Theorems 1–2;
- F168 Theorems A–C and the finite-core transfer;
- the operative uses of 142, 200, 99 and 181 II.1–II.4.

The applications are supported at the 7-free and ASSUMED-simple cuts named above.

**What it does not establish.**

- NR-NS or any least-order existence.
- Global Sun7, unrestricted Sun8 or the Sun8 → P7 ancestry.
- Any all-P7-group bound, any exclusion below the bounds, a witness, or normal-composition closure.
- Any stronger-family promotion or novelty, SOTA or priority status.

**Process.**

- No verdict is transferred from any older review, parent, coauditor or the rank-free 178 context.
- The frozen sources are unedited.
- No noninfluence certificate is given for the disclosed contacts.

**Next steps.**

1. Actual RETURN to Main.
2. A NEW whole post-v170 ACK.
3. Main's actual read and an applicable explicit direction before any primary work.
