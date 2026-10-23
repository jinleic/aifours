# Parent verdict: generalized Lemma ZS, ROT-ZS, INV*-ZS and OLSON-ZS (proof-ROT-half-v2), v1

Written 2026-10-18 after 11:50 PDT (host clock read at 11:36:04 and later). Lane: math-2 (Olson / inverse normalization, D_(2p)).

## Verdict

**CORRECTNESS-ACCEPTED at the scope below, for every prime p ≥ 5, as a written proof with the mandatory overlay in this file.** This is a partial theorem under the math-2 continuation contract. It is **not** full INV*(p), not unrestricted ROT(p), and not unrestricted ordered Olson for D_(2p). It is not a new-open-target gate. No novelty claim is made, and priority has not been assessed beyond the lane's existing screens.

Text of record: [proof-ROT-half-v2.md](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/proof-ROT-half-v2.md) (sha256 `7403098f15cbb8b7954364a874cc58646d2a91bf11f3e29fee969c5f7c3748eb`, 16,101 B) **plus overlay items V1–V9 below**. Where they differ, the overlay governs. The v1 text and the [half-range verdict](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-half-range-parent-verdict-v1.md) (`b3afb001…1c3b`) are unchanged and remain in force.

## Accepted statements

Notation as in the text: Y(x) = (1,x) ∈ Z_2 × Z_p = Z_(2p); F(w) is the number of reflection letters; o = o_F(w) is the number of **odd blocks of the maximal cyclic constant reflection-block decomposition** (not reflection runs); κ(w) = p − 1 − (F − o)/2.

1. **Lemma ZS.** Let p ≥ 5 be prime and k, κ integers with (G): k ≥ 1, 3k ≤ 2p + 1, 0 ≤ κ ≤ min(k − 1, p − k). If Y is a sequence of R = 2p + 2κ − k odd elements of Z_(2p) with no zero-sum subsequence of length in [2κ + 2, 2p], then some odd generator g gives cost_g(Y) ≤ k − 1, and every |b| ≤ k for that g.
2. **Theorem ROT-ZS.** Every avoider w of length 4p − 2 over D_(2p) with 3·o_F(w) ≤ 2p + 1 and F(w) ≥ 3·o_F(w) − 2 has all rotation letters in one set {ρ_c, ρ_−c}, c ≠ 0.
3. **Corollary INV*-ZS.** Under the same hypotheses, w satisfies INV*: all rotations lie in one {ρ_c, ρ_−c}, c ≠ 0, and every maximal cyclic reflection run is constant.
4. **Corollary OLSON-ZS.** Every word w of length 4p − 1 over D_(2p) with 3·o_F(w) ≤ 2p + 1 and (o_F(w) ≤ (p+1)/2 or F(w) ≥ 3·o_F(w) − 2) has an identity 2p-subword in increasing index order.

**What is new relative to the accepted union o_F ≤ max(4, (p+1)/2):** avoiders and length-(4p−1) words with (p+1)/2 < o_F ≤ (2p+1)/3 and F ≥ 3·o_F − 2. Examples: p = 7, o_F = 5, F ≥ 13; p = 13, o_F ∈ {8, 9} with F ≥ 22 or F ≥ 25 respectively. Whether such avoiders exist is not claimed. At p = 5 the lemma coincides with v1.

## Mandatory overlay (merged from both reviews)

- **V1 (Codex 1; Claude Z1).** Replace "complete in-file proof" by "complete modulo the imported Lemma MULT (i)–(iii) and (D) = D(Z_(2p)) = 2p". Replace "the proof steps are the v1 steps" by "same nine-step structure, with new justifications in Step 5 (G5) and Step 6 (wrap case, G4)". The parent-accepted v1 statements, with the half-range overlay, remain true.
- **V2 (Claude Z2).** Step 6 obtains its contradiction in τ form: τ({y_1,…,y_j}) = 2p − S_j ∈ [2p − 2k + 2, 2p − k] ⊆ [k, 2p − k] by (G4), contrary to Step 5; for Z−, τ = T_j ∈ [k, 2k − 2] ⊆ [k, 2p − k].
- **V3 (Codex 2; Claude R1, R2, R3).** In ROT-ZS: κ ≥ 0 because, if H ≥ p, GRX's all-plus pattern with zero rotations is already an identity selection (GRX holds for the normal form's representation with genuine empty runs). State |b| ≤ k ≤ p − 2 from Lemma ZS **before** identifying b with the SHgen weight b_x; then x = bc ≢ 0, so no rotation is ρ_0. The normal form, DAV and SHgen-E are used at their own displayed hypotheses; their earlier 5o ≤ 2p + 4 chain imposes no bound on k. SHgen-E's caller obligations hold: k is unchanged along every expansion, and each base word has length 4p − 2, one nonzero rotation pair and o_F = k ≤ (2p+1)/3 ≤ p.
- **V4 (Codex 3; Claude H1).** If the normal form has k = 1, Proposition K1 gives the conclusion (in ROT-ZS and in ROT-HALF). The deduction κ(w) ≤ o − 1 ≤ p − o in ROT-HALF is used only for k ≥ 2.
- **V5 (Codex 4; Claude O1).** OLSON-ZS rests on proof-OLSON-few-v3.md L28–47 and the explicit deletion calculations, not on the absent proof-FEW-p5-lift-v3 ledger: Case 2 (an odd block of length ≥ 3) takes (o, F) to (o − 1, F − 1); Case 3 (rotation deletion, R ≥ 3) takes (o, F) to (o or o − 2, F); no deletion from an even block occurs. In the low branch, INV*-HALF is applied to the deletion word itself.
- **V6 (Codex 5; Claude Z3).** The obstruction is only the single pair (k, κ) = (p, p − 1), outside (G): Y = g^(2p−1)(3g)^(p−1) satisfies (ZP) and (V) and defeats the cost conclusion there. No obstruction is shown for any k < p; no group word realizing Y and no ordered-Olson counterexample is supplied. Nonconstant-sign GRX patterns are one possible further input, not a necessity statement about all proofs.
- **V7 (Codex 6; Claude S3).** KAPPA01 is an unaccepted auxiliary candidate ("would cover", not "covers"); it is excluded from accepted coverage and dependencies.
- **V8 (Codex 7; Claude S1, S2, S3).** The residual is "parameters not covered by these uniform sufficient hypotheses", not a necessity statement. Failure of 3o_F ≤ 2p + 1 does not make MULT unavailable: the actual terminal k or defect e may still satisfy its hypothesis. "For p = 5 and p = 7 nothing is new" is false at p = 7 (o_F = 5, F ≥ 13 is new). The p = 5, o_F = 4 piece of the union rests on the separately accepted finite computer-assisted input.
- **V9 (Claude R4).** Use the cyclic definition of o_F above and restore the INV* definition at the INV*-ZS statement.

## Reviews

| Family | Note | Receipt | Result |
|---|---|---|---|
| Codex gpt-6.1-sol, effort max, read-only snapshot | [note](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-zs-v2-delta-codex-v1.note.md) `a6927723…56af` | `84a79dfb…a1dc` | ACCEPT-WITH-FIXES for generalized ZS, ROT/INV*-ZS, OLSON-ZS and the HALF deduction; 0 FATAL, 0 MAJOR, 7 mandatory MINORs |
| Claude claude-opus-5-5, effort max, no tools | [note](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-rotation-zs-v2-delta-claude-v1.note.md) `abb193d1…f748` | `01596620…08a` | ACCEPT-WITH-FIXES for all four claims; 0 FATAL, 0 MAJOR; MINORs Z1–Z3, R1–R4, H1, O1, S1–S3 |

Both packets contained the same 13 hash-pinned sources (v2, the parent v1→v2 diff `be018e1c…bd28`, v1, the half-range verdict, both v1 reviews and the imported accepted texts).

## Independent parent verification

**Written derivation (parent, by hand).** I re-derived:
- (G1)–(G5) from (G), including (G3) k ≤ p − 2 at p = 5 and p ≥ 7.
- Step 1 (minimal zero-sums have even length ≤ 2κ; a long zero-sum has a prefix product of length in [2κ + 2, 4κ] ⊆ [2κ + 2, 2p − 2]).
- Steps 2–4 and COMP (e = k − 1 − 2κ + |Z| ∈ [0, k − 1]; MULT's hypothesis 3e + 2 ≤ 3k − 1 ≤ 2p; m ≥ 2p − 1 − 2e ≥ 2p − 2k + 1 ≥ k − 1).
- Step 5: the two Step 4 inequalities for U and its complement add to |Z| ≥ 2p − 2k + 2, against |Z| ≤ 2κ ≤ 2p − 2k.
- Step 6 including the wrap case S_j > p: τ = 2p − S_j still lies in [2p − 2k + 2, 2p − k] ⊆ [k, 2p − k] by (G4); singletons give |b| ≤ k − 1 and exclude b = p.
- Step 7: 2p + 1 ≤ σ + k + |Z−| ≤ 2σ + k ≤ 3k − 2 ≤ 2p is impossible. Step 8 via σ ≤ k − 1 ≤ m. Step 9's count gives cost ≤ k − 1.
- ROT-ZS: κ_terminal = κ(w) − (o − k)/2; (G) holds at the terminal word (κ ≤ p − k − 3(o − k)/2); rotation count 4p − 2 − F = 2p + 2κ − k; SHgen (H): 2H ≥ 2k − 2 ≥ E; (K) reduces to 5k ≤ 4p − 1, implied by 3k ≤ 2p + 1 for p ≥ 4.
- ROT-HALF (with V4), INV*-ZS (REFL-few-odd needs o_F ≤ (2p+1)/3 ≤ p), and OLSON-ZS against proof-OLSON-few-v3.md L28–47: Case 1 needs (F − o)/2 ≥ p, which holds since F ≥ 4p − 3 and o ≤ 2p − 3; Cases 2 and 3 as in V5, with F − 1 ≥ 3(o − 1) and F ≥ 3o − 2 ≥ 3o_i − 2.

No gap beyond the overlay items was found.

**Finite aid (not a premise).** [check_olson_zs_v2_lemma_parent_v1.py](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/check_olson_zs_v2_lemma_parent_v1.py) (`df97a022…983d`) enumerates every (ZP) multiset by hereditary DFS and checks min over odd generators of the lemma's cost. [RESULT-v1.json](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-zs-v2-parent-smoke-v1/RESULT-v1.json) (`25feacc0…2e3c`): **all 29 parameter sets PASS, 0 violations, 22.9 s** — every (k, κ) allowed by (G) at p = 5 and p = 7, plus p = 11 with k = 7 and p = 13 with k = 9, all κ. These include parameters that only v2 allows (k > (p+1)/2: (7,5), (11,7), (13,9)); the bound k − 1 is attained in several of them. [Negative controls](/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/olson-zs-v2-parent-smoke-v1/NEGATIVE-CONTROLS-v1.json) (`895a547e…cad`) outside (G) show the enumerator reports failures: at (p,k,κ) = (5,5,4) and (7,7,6) it finds 16 and 36 violating multisets, including Remark (3)'s g^(2p−1)(3g)^(p−1).

## Imports and boundary

- **Imported at accepted scope (hypotheses checked only):** (D); MULT (i)–(iii); GRX, PM*, K1; the normal form with DAV/(V); Theorem SHgen and Lemma SHgen-E; restricted REFL-few-odd; RGR-LONG(p).
- **Not established:** Lemma ZS for p − k < κ ≤ k − 1; any statement outside the hypotheses above; KAPPA01; any word realizing the k = p sequence; unrestricted ROT(p), INV*(p) or ordered Olson.
- **Trust boundary:** written mathematics checked by the parent and two model families; no Lean or formal kernel. Model reviews are advisory evidence. The finite aid checks only the sequence lemma at small parameters.

## Follow-on

The lane has since frozen a separate candidate, proof-ROT-ZX-v1.md (`ad2460b2…815b`), that claims a further extension by a new proof. It is unreviewed and is **not** covered by this verdict.
