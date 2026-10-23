# Hostile written review: PURE-A corner exclusion in columns 2/3 (candidate v2)

**Inputs.** I used only the pasted texts:
- `00`: candidate v2. This is the governing text. v1 was not supplied, so its clock error is preserved and not evaluated.
- `01`: scope freeze.
- `02`: transition.
- `03`: [PRIM] excerpt, physical LF195–225.
- `04`: P1-B3 entry.
- `05`: SB2 excerpt. `05` LF3 is physical LF109.

Every load-bearing step was re-derived in writing. I used no tools, files, code, enumeration or numerics. Hashes, pins and timestamps were treated as metadata, not evidence.

## Counts

**FATAL 0 · MAJOR 0 · MINOR 1.** There are also 4 editorial notes, which are not counted and have no mathematical consequence.

**No mathematical flaw found.** The theorem is the implication H1 ∧ H2 ∧ (B3) ⇒ Q₁(r,c) ∉ V_A for every r∈{1,7} and c∈{2,3} (`00` LF7, LF15–28). It is correct, with no gap or circularity.

LF9 says "the PURE23 family is excluded". Read as a statement about genuine B3 configurations, it is conditional on the premise binding in MINOR-1.

## MINOR-1: row-1 support premise sits outside the frozen premise list

This is a process/scope issue; correctness is unaffected.

**Step.**
- `00` LF25, LF28 and LF165 take supp(q¹)={1,2,3} from [NF]/SB2 (`05` LF3, LF7).
- The frozen premises (`01` LF18) name only [PRIM], standard row 0, and the P1-B3 supports.
- The pasted P1-B3 entry (`04` LF21–47) lists rows 2–7 only. Whether its unit clauses (`04` LF17–19) encode SB2 is not visible.

**Load-bearing?** Yes. It defines corner row 1, and it feeds (1), C4 for q_s¹, and a_d≠0 when r=1.

**Consequence.**
- The theorem as stated is unaffected, because H3 lists this premise.
- LF9 covers genuine B3 configurations only insofar as B3 includes supp(Q₁(1,0))=A in the H2 frame.
- LF28 says the q¹ support is "not a conclusion of the template row list". That is accurate as provenance. Under an exact-support reading of `04`, however, it is derivable:
  - Rows 2–5 ⊆ W and q⁰∝e₀ put q¹ in V_A.
  - Write q⁶=(0,b₂,b₃) and q⁷=(c₁,c₂,c₃). Then q¹ ∝ b̄×c̄ = (conj(b₂c₃−b₃c₂), b̄₃c̄₁, −b̄₂c̄₁).
  - The first coordinate is nonzero. Otherwise (c₂,c₃)∥(b₂,b₃), and ⟨q⁶,q⁷⟩=0 would force c₂=c₃=0.

**Minimal repair.** Either add `05` LF3 to the premise list and state the theorem "under SB2", or replace the import with the derivation above. The derivation needs rows 2–5 as inclusions and rows 6–7 as exact supports. §§2–4 are unchanged either way.

**Robustness check (verified, in the candidate's favour).** Given exact supp(q¹)=A, column-0 orthonormality forces both other supports to be exact:
- supp(q⁶)={2,3}: if b₂=0, then ā₃b₃=0, so q⁶=0, which is impossible. The same holds for b₃.
- supp(q⁷)=A: q⁷ ∝ ā×b̄ = (conj(a₂b₃−a₃b₂), −ā₁b̄₃, ā₁b̄₂), and a₂b₃−a₃b₂ = −b₂(|a₂|²+|a₃|²)/ā₃ ≠ 0.

So it does not matter whether `04` lists exact or merely allowed supports.

## Editorial notes (not counted)

- **E1.** "Interior" is never defined (LF36–40).
  - LF87 uses it to mean column ≥1, yet LF47 applies C2 "at (r,0)".
  - LF47 also states the direct (T) pair (r,0),(0,d), which is valid. C1 and C2 in fact hold at every cell with row ≥1.
  - Repair: state C1–C2 for all cells with row ≥1.
- **E2.** Two citations are compressed.
  - LF74 cites "(5) applied to that coordinate". What is actually needed is the identity V_A∩{e_b,q^r}^⊥=span{ell_b}, i.e. LF61's right-hand equality together with LF70.
  - LF87 says the A-part is "zero by (6)". The missing step: m⊥u∝ell_c and ⟨ell_c,ell_b⟩≠0, so ell_b∉span{m}.
- **E3.** LF157 says the argument would "fail exactly at (10) and (13)". That understates the loss.
  - For c=1, u∝q⁶ and m∝q^{r′}.
  - Only two parts of (10) survive: the 6-part at y and the r′-part at x.
  - Consequently (12)(iii), (13), the e_{t_s}-removal in (14), and (15) all fail.
  - The scope claim itself is correct: column 1 is undecided and not relabelled.
- **E4.** LF159 says "would already contradict the proof"; the intended meaning is "contradicts the theorem". The substance is verified. Every cell used lies in row 0, row r, or column 0 (rows 6, r, r′). So PURE23 partial assignments of rows 0, 1, 7 plus column 0 are also excluded.

## Claim-wise verdicts (`00` unless noted)

| Claim | LF | Verdict | Re-derivation |
|---|---|---|---|
| Theorem | 7–9 | ✓ as implication; LF9 family scope conditional (MINOR-1) | — |
| (T) | 15–19; `03` 1–2, 15–23 | ✓ | ⟨a⊗b,a′⊗b′⟩=⟨a,a′⟩⟨b,b′⟩. Symmetric under s↔t and z↔z′, so tensor-factor order is immaterial. Only orthogonality of the product vectors is used. |
| H2 | 21; `01` 18 | accepted premise | Enters only via C1/C2, using w≠0. |
| (B3) | 25–28; `04` 38–46; `05` 3, 7 | premise matches sources | Exactness is forced (robustness check). Rows 2–5 (`04` 22–37) are unused. |
| (1), P_r | 30–32 | ✓ | Three orthonormal vectors in the 3-dimensional V_A. |
| C1 | 36 | ✓ | Q_s(i,j) ⊥ Q_s(0,j) ∝ e_j. |
| C2 | 38 | ✓ (E1) | (T) at z,(0,d) gives w_{s,d}w_{t,d}·conj(Q_s(z)_d·Q_t(z)_d)=0. |
| C3 | 40 | ✓ | (T) at (k,0),z gives ⟨q₁^k,Q₁(z)⟩⟨q_s^k,Q_s(z)⟩=0. Each factor stays inside its own square; no cross-square substitution. |
| C4, (2) | 42–47 | ✓ | Square 1 is nonzero on A in rows r,r′ and on {2,3} in row 6; add ⊥e₀. |
| (3) | 49–53 | ✓ | Four nonempty disjoint subsets of the 4-set W give singleton bijections. p_s≠t_s by column 0. |
| (4) | 55 | ✓ | Inter-square (T) at (6,0),(0,1), using q⁶'s zero e₁ coordinate. Intra-square column orthonormality alone would not give this. |
| (5), ell_c, 1-dimensional | 59–70 | ✓ | ell_c=ā×e_c, and ⟨q^r,ell_c⟩=ā·(ā×e_c)=0. All nine components recomputed. |
| (6) | 72 | ✓ | ⟨ell_c,ell_b⟩=\|a\|²δ_cb−a_b ā_c. All six ordered pairs checked. |
| supp(m)=A | 74 | ✓ (E2) | A zero coordinate b gives m∥ell_b. If b=c this contradicts m⊥u; if b≠c it contradicts (6). |
| (7) | 76–79 | ✓ | Coordinate 1 of ell_c is −ā₃ (c=2) or ā₂ (c=3), so ≠0, while q⁶ is zero there. u is zero at c while q^{r′} is not. The 2-dimensional complement keeps both coefficients. |
| c=1 contrast | 81 | ✓ | ell₁ ∈ span{e₂,e₃}∩(q^r)^⊥ = span{q⁶}. |
| Other row-r A-parts ∈ span{m}; zero at A∖{c} | 85–87 | ✓ (E2) | Row orthogonality to q^r and u; span{ell_b}∩span{m}={0}. |
| (8) | 89–93 | ✓ | P_A·I·P_A=P_A, and the j=0 term is \|q^r⟩⟨q^r\|. |
| (9), k=1 | 94–100 | ✓ | Slots: 3·2+4·3=18. Squares 2..5 give 12 demands: Parseval for each e_d, d∈A, in row r, where the j=0 term is 0 by C4. Slots are disjoint across squares by C2. So 2+3k+12≤18. The count uses exactly five squares. |
| Q₁(x)=phase·m | 102 | ✓ | Equality case of Cauchy–Schwarz. |
| (10) | 102–106 | ✓ | C3 with k∈{6,r′}, both ≠r. Each of the four nonzero coefficients is consumed: r′ at x→(12)(ii), 6 at x→(12)(iii), r′ at y→(14), 6 at y→(15). |
| (11) | 110–115 | ✓ | \|D∖{j}\|=4, so exactly one d_s=0 and three d_s lie in W. |
| (12), h_s | 117–121 | ✓ | Row r against q_s^r, plus (10) at x. |
| (13) | 121–123 | ✓ | C4 removes 0,2,3; column 0 removes p_s,t_s; (12) removes d_s. |
| (14) | 125–127 | ✓ | C2 removes A∖{c}; C1 removes c; row r removes p_s,d_s; (10) removes t_s. |
| (15) and contradiction | 129–133 | ✓ | ⟨q_s⁶,Q_s(y)⟩=β̄_s·δ_s. β_s=0 forces α_s≠0, and by (4) that happens at most once in I. So at least two squares have Q_s(y)∝e₀, contradicting (T) at y,(0,0) (0≠c). |
| Quantifier sweep | 135 | ✓ | p_s=j and h_s=j are allowed and harmless. The square with d_s=0 is unused. No 1↔7 or 2↔3 symmetry is invoked. |
| Tensor ledger | 139–155 | ✓ | All 11 rows checked; every pair has distinct rows and columns. (9)'s slot disjointness falls under the first row. |
| Scope boundary | 11, 157 | ✓ (E3) | — |
| Partial-assignment remark | 159 | ✓ (E4) | — |
| Import table | 161–172 | consistent with the `03`/`04`/`05` excerpts | Pins and hashes not evaluated. |
| v1→v2 supersession | 3 | not evaluable | v2 governs. |

## Correctness, completeness, process, priority, computation

- **Correctness.** Every load-bearing step is verified, with no counterexample and no circularity. No prior candidate is imported. The three exposure items in `01` LF17 are each re-derived inline: §3, (11), and (7)/(10).
- **Completeness** (against `01` LF11–15 and `02` LF11):
  - The exclusion branch is delivered for every r, c, j∈W, both axis bijections, all phases, and both β cases.
  - The zero coordinate 1 of q₁⁶ is retained, and it is exactly what makes (7) hold.
  - No 2/3 symmetry and no column-1 relabelling is used, so the partial-assignment branch is unnecessary.
  - Not covered, and not claimed: column-1 corners, A-free or mixed corners, full B3, and any 5-MOQLS(8) no-go.
- **Process.**
  - MINOR-1 above.
  - v1 was not supplied.
  - Metadata was not evaluated.
  - The candidate's "no scripts / no numerics" assertions cannot be checked from the packet. Nothing in the argument depends on computation.
- **Priority.** The candidate makes no novelty claim (LF11, LF157), and none is made here.
- **Computation.** None was used or needed, by the candidate or by this review.

**Not approved:** the B3 / 5-MOQLS(8) research target, any Boolean or computed status, and runtime. This verdict covers only the written implication at `00` LF7–135 under H1, H2 and (B3). LF9's family-level scope remains conditional on MINOR-1.
