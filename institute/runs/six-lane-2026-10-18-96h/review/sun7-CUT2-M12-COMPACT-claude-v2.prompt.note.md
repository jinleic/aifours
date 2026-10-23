# CUT2-M12 second-family proof-path audit (M1/M2)

**Inputs applied:**
- E3 erratum v1, F2 only (F1/F3 superseded) and E3 erratum v2 Z1–Z12.
- SH-DG S2 and G1–G6. G7–G8 are not in the packet.
- The governing DG erratum v1, and the FULL parent erratum v2.
- LEDGER erratum v4 and the CI62 verdict.

I used only the pasted text; no tools were used.

**Governing DG correction.** It replaces DG §5 step 3 (the P_ob exclusion), and its New block holds on its own terms:
- Removing one vertex of C5 leaves a path, so every e in Q has a cycle-neighbour in Q, giving m_e ≤ 2.
- Q has at least two unmarked vertices.
- DG-4 (G4) then gives ≤ 3 + 1.

Neither path cites DG §5 or DG-4. A LF13–14 imports DG-1, DG-3/G3 and the Theorem DG proof. FULL's (1,3) branch (LF91–92) uses only M13-A. The correction changes neither verdict.

**Counts: FATAL 0 · MAJOR 0 · MINOR 3.** All three are completeness/bookkeeping. I found no correctness flaw on either path.

---

## M1: RESOLVED

The diagnostic is E3 LF114–120 (§6 checks and mutation controls) plus Codex LF235–244. I deleted both mentally and re-traced every path:

| E3 path | Literal premises | Cites §6 or Codex? |
|---|---|---|
| Lemma 1 (Z2 LF82–88) | labels at d; P0(b); LFC(c) at \|T\|=4 with Sun(4); LFC(d); INV(a)/E6; INV(b) | no |
| Lemma 2 (LF37–55, Z3–Z5, F2) | labels at v; LFC(c) at \|T\|=2 (Sun(2)); LFC(d); INV(a)/E6, INV(b) | no |
| Lemma 3 (Z6 LF155–170) | L0.1, Lagrange, E1/INV(b) ranges, Lemma 2 when h_d ≥ 1 | no |
| Steps 0–4 (Z7; LF76–79; Z8; LF86–89) | Lemma 1; LFC(a)–(b); Lemma 1 computation at a=1 with Sun(4); coset disjointness and LFC(b); L0.1/Lagrange with Lemma 3; R0 | no |
| Z9, C1 (Z10), C2 (Z11), LF105 | steps 1–3; Lemma 3 chain per Q; Lemma 2 with Z11(a); the Theorem (e_d ≥ 3) | no |

**Every numeric relation is derived in place:**
- Lemma 1: 5/6 + a/12 < 1.
- Lemma 2: val ≥ 6.
- Lemma 3: k ≤ α* ≤ 5, or ≤ 4 when h_d ≥ 1.
- Step 3: 11n_d/4 ≤ 3(n_d − M) + (M − 1).
- Step 4: M ≥ n_d/gcd, hence gcd > 8.
- C2: the bound ≤ 18.

**Step 4 does not use control (2).** Its "gcd > 8" comes from step 3 plus granularity, not from control (2)'s "16 > 8".

**No circularity.** The only e_d input to C1/C2 is the Theorem's own conclusion (Z10 LF260, Z11 LF287), and the Theorem's proof uses neither corollary.

**Downstream re-derivation.** A1(a)/(b) re-derive the a=3 counts and the 4-piece structure from LFC on Γ* (A LF42–48). They use only the exclusion direction, not Codex LF238's "becomes allowed / 13n_d/4" remark.

Non-use follows from this trace, not from the "not an existence claim" wording at E3V LF29.

## M2: RESOLVED

This is relative to the accepted component imports, with the conservative envelope kept.

**Edge and scope.** The chain is FULL LF91–92 (FAM, x=α, α*_(d i*)=3) → FULL LF64 → M13V LF13–14 → A LF18–107.
- FULL's branch is exactly (1,3) with t ∈ O and f* = 1 (OR LF70–75; R LF77–80), and e_d ≥ 4 (E3-T LF59). This is the same scope as M13V LF9.
- FAM's (DG_x) and (C2_x) (LF83–85) are literally DG*(b) (LF88–89) and C2* (LF98).
- r_S = min(e_d, v2 T_α(S)) equals FULL's min(e_d, δ_α(S)), since normalisation fixes every U_j (A LF21).

**Path, each step re-derived:**
- **§0 (LF19–26).**
  - Lemma 1 applied to α* gives t ∈ O, f* = 1 and f_t ≥ 2.
  - Γ* has pieces U_j g_j⁻¹, conjugated family (U_j), d-piece U_d, the same class (INV(a)/E6), and α-matrix α*.
- **A1.**
  - (a) LF42–43: LFC on Γ* gives fibre counts n_d/2 and 3n_d/4.
  - (b) LF44–48: the Z2 gcds at a=3 are all 3 except (t,i*) = 9. Sun(4) then forces every 4-subset of S*_F to contain {t,i*}, so |S*∩O| ≤ 3 and |S*| ≤ 4.
  - (d) LF57–61 is verified.
  - The O-part of A1(c) is exactly the disjointness instance DG-1* needs. The i*-part of A1(c), A1(e) and C1* are not consumed by FAM.
- **DG-1* (LF70–72).** I re-derived this from the G2 text (LF187–194), not from the verdict label at A LF71.
  - G2 uses only O-data (α_dc = α*_dc = 1), LFC(a)–(b), L0.1, Lagrange, the step-3 argument and the Z10 chain; it uses no d–i* entry.
  - On Γ*: the (W_Q, U_d) double-coset fibre counts are positive multiples of n_d/gcd.
  - gcd = 2^min follows from the Z10 chain with α: Lemma 2 for α when h_d ≥ 1, and the E1 bound α_tp ≤ 5 at the two-marker base.
  - This holds for every nonempty Q ⊆ O and every marker placement.
- **DG-2* (LF73–84).** It is pure counting from A1(b) and (d); all identities rechecked.
- **DG*(a) (LF92–95), the G5 argument.**
  - For all five Q, the hypothesis with DG-1* puts N*(Q) in (n_d/16)ℤ.
  - So N*(Q) > n_d/16 forces N*(Q) ≥ n_d/8, which gives N*(O) ≥ n_d/8 + 1/3. This contradicts N*(O) ≤ n_d/8 − 1/2.
  - All ten R are then covered by DG-2*(ii) with DG-1*.
- **DG*(b) (LF96–97), the G6 argument.**
  - Both 10/8 and 19/16 exceed 19/16 − 2/n_d.
  - G3 (LF211–220) on Γ* uses only n_j = 6ℓ_j, Lagrange, the E1 pair index, L0.1, and Lemma 2/Z11(a) for α.
  - G3 gives r_R ≤ 5. It gives r_R ≥ 4 ⇒ (2,4,4) or (4,4,4) with τ ∈ {8,16}. It gives r_R = 5 ⇒ (4,4,4), τ = 16, e_d ≥ 5.
- **C2* (LF99–104).**
  - The sum over pairs of N* equals 2n_d + b4 + 3b5 ≤ 19n_d/8 − 3/2.
  - Each pair has N* ≥ n_d/2^(1+v2 α), since 1 + v2 α ≤ 3 < e_d.
  - All ten O–O α values lie in {1,2,4} (Lemma 2, Z11(a), E1).
  - Hence 4n1 + 2n2 + n4 ≤ 18, so n4 ≥ 2n1 + 2.

**Argument versus statement.** A LF91 re-instantiates the G5/G6 argument with DG-1*/DG-2*. The conditional Theorem DG statement (DG LF50–61) is never invoked on this branch; its α-family form needs α*_(d i*) = 1, which is false in (1,3). FULL invokes that statement only where its premise holds (LF86–91), consistent with LEDGER v4 item 1.

**Genuine premises:**
- **Numeric:** e_d ≥ 4, from E3-T. It is used for integrality at A LF93; LF102 needs only e_d ≥ 3.
- **Coverage:**
  - DG-1* on all 10 pairs, 10 triples and 5 quadruples.
  - G3 on all 10 triples.
  - Lemma 2 with Z11(a) on all 10 α-pairs.
- **Certificate or computation:** none.

**Unreachable from LF18–107, so not used or accepted here:**
- M13 B–D and the A §3 joint budget (M13V item 3).
- D3/D4.
- CAP/DT.
- VFC/L1, which SH-DG G1 LF161–163 withdrew.

Their feasibility is not certified by scalar agreement.

**Boundary.** The operative N56 path uses none of the CAP C1/RC-i*/VFC/L1(T3) imports that M13V LF5 lists for parts A–D. They stay in the conservative closure: FULL parent erratum v2 LF7, LEDGER v4 item 3 (edge N57→N58), and CI62V LF11. Completeness claims about N58/N59 still depend on CI62. The computer-assisted Sun(5)/(6) provenance remains transitive (Z1 LF60–64; A LF15–16).

---

## Findings (all MINOR; documentary; no consequence for consumers)

**m1: e_d ≥ 4 is not declared in A.**
- A LF93 and LF102 use e_d ≥ 4, but A's imports and setting in the supplied text (LF7–30) do not list Theorem K62-E3.
- It arrives only through M13V LF9, LEDGER LF273 (N56←N53)/K04, and FULL LF59.
- Consequence: none for FULL, since E3-T holds for the whole class.
- Repair: add "Theorem K62-E3 (e_d ≥ 4, whole class)" to A LF10.

**m2: DG-3's orientation-free scope is not recorded.**
- A LF88–90 and LF97 apply DG-3 to Γ*, whose d–i* entry is 3.
- Orientation-freeness is recorded only for DG-1 (G2 LF194; SDV LF17; LEDGER v4 "DG-1 (orientation-free)"). K04 (LF208) labels the N55 bundle "conditional DG".
- The literal G3 proof (LF214–220) contains no d-datum or i*-datum, so the application is a valid re-instantiation.
- Repair: tag the N55/K04 export as "DG-3/G3 (orientation-free; O–O data, Z11(a) both families)".

**m3: N56's line coverage omits the load-bearing A §0.**
- LEDGER LF102 records the N56 body as M13 LF32–107, with imports at LF7–16 (LF273). FULL LF64 points at LF85–104.
- A LF18–30 carries the derivation of t ∈ O, f* = 1 and f_t ≥ 2, which A1(b) LF46 uses. It also carries the Γ* identifications that A1 and DG-1* (LF71–72) use. I verified these lines above.
- Repair: read the N56 body as M13 LF18–107.

---

**Process and boundary notes (not counted):**
- **Process:** E3V LF29's existence wording is not a non-use argument; the M1 trace supersedes it.
- **Not in packet:** the M13 parent erratum 99276f6d and SH-DG G7–G8. Reliance on the FULL parent erratum v2 LF11 claim that the M13 erratum touches only A:117–118 (status) is parent metadata, and those lines are outside LF18–107.
- **Priority:** none claimed.
- **Computation:** none used.

This audit does not approve the global graph or order, full K6.2*/K7/Sun7, runtime, novelty or priority, Lean, or human review.
