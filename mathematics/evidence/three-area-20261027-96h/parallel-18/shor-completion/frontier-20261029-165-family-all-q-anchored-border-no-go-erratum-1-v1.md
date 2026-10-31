# Erratum 1: f177 MINORs m1–m3 for the 165·2^t all-Q anchored-border candidate

Owner **MathShor-2**, math-5. Native `/bin/date` before writing: **Thu Oct 29 08:42:48 PDT 2026**.

**Additive erratum. Main directed one erratum for the three f177 MINORs; this is it.** It applies to these two immutable files, neither of which is edited:

- candidate `frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md`, SHA256 `20169ac9e398d9d1ef37d263f9b51d0f9168c095c3e3eb21ade47572822d39c6`, 312 LF / 23,071 bytes;
- its checker `frontier-20261029-165-family-all-q-check.py`, SHA256 `4c550a5750a822235f20a9862d582082f3427c307f6196575099149638a4538e`, 234 LF / 9,099 bytes.

The source of the findings is the f177 return `institute/runs/three-area-2026-10-27-96h/review-waves/f177-shor-165-all-tail-finite-audit/review-v1.md` (SHA256 `fed47b9dd99a155617985f0c6ffe7fbef11feca18632ebce01f67319798ce26c`, 231 LF), §7, items m1–m3. Every consumer must read the candidate first and then this erratum.

Nothing here changes a mathematical claim, an import or a scope, and nothing here is a new finding. The f176 written-proof review is still pending. The candidate remains UNREVIEWED as a whole.

## E1 (m1): the sign of one bracket in the d=5 chain

At candidate §6, d=5 chain, step 4 (candidate line 177), the text says "Against x_15 [11, k=1]". Under the bracket convention r−y stated at candidate line 129, it should say **"Against x_15 [−11, k=1]"**.

- The class difference is 4 − 15 = −11 ≡ 22 (mod 33).
- Only the sign of the bracket changes. The shared-coordinate count k=1 (the 11-coordinate) and the conclusion x_4 ≡ 4 (mod 5) stay as written.
- The other 34 brackets in §6 are unaffected. f177 reports that it checked all 35.

## E2 (m2): the order 330 already fails on the anchors

Add this remark to candidate §1, after line 36. It also qualifies the t=1 diagnostics in §8, item 6.

> At t=1 (n=330), the anchors violate Sands' divisor exclusion directly: gcd(8−0, 330) = 2 ∈ G_A(330) and gcd(14−0, 330) = 2 ∈ G_Y(330). So the order 330 is excluded trivially, without §§5–7. The written analysis is still valid at t=1, but it is redundant there. For t ≥ 2, gcd(8, n) ∈ {4, 8}, and G_A(n) ∩ G_Y(n) = ∅. Specifically, G_A(660) = {3, 4, 5, 11}, G_A(n) = {3, 5, 8, 11} for t ≥ 3, and G_Y(n) = {1, 2, 6, 12} for t ≥ 2.

The line "G_Y(n) ∋ 1 and G_A(n) ⊇ {3,5,11}" in §8 item 6 is true for every t, but it does not mention the common element 2 at t=1. f177 also reports that, at t=1, the actual head screen is empty and the actual tail screen contains only the tails 1, 7, 13. The owner has not re-derived those screen facts.

## E3 (m3): fidelity between the checker and the prose

The checker logic and its verdicts are unchanged. Three descriptions are corrected.

**(a) Candidate §8, item 4 (line 266).** The text says the checker confirms nonzero remainders for m ∈ {1, 2, 11, 22, 55, 110}. Read instead:

> the checker *computes and records* the remainder of W modulo Φ_m for m ∈ {1, 2, 5, 10, 11, 22, 55, 110} (output key `lemma5_W_nonzero_mod_Phi_m`), and *asserts* only that it is nonzero for m ∈ {11, 22, 55, 110} and zero for m ∈ {5, 10} (checker lines 169–173).

Lemma 5 needs only the orders divisible by 11, so m ∈ {1, 2} carry no proof weight. For the record, the owner recomputed these values in the kernel on 2026-10-29: W(1) = 15 and W(−1) = 5, both nonzero. This matches f177.

**(b) Section labels in the checker comments.** The comments "Section 4 (e=165)", "Section 5 (e=55…)" and "Section 6 (e=33…)" (checker lines 58, 62, 71) are stale. In the candidate, all three blocks belong to §6: e=165 is d=1, e=55 is d=3 and e=33 is d=5. Read them as "§6 (d=1)", "§6 (d=3)" and "§6 (d=5)". The comment "Section 7 (e=15…)" (line 81) matches §7 and is correct.

**(c) The checker's mirror of Step 5 for classes (0,0) and (2,4).** The step-5 assertion (checker lines 111–113) refutes every odd type of a class with r_3 ∈ {0,2} against the two even reference types E[5] = 110 (class (2,0)) and E[9] = 234 (class (0,4)). The prose (candidate lines 213–214) argues differently for (0,0) and (2,4). It derives x ≡ 3 (resp. x ≡ 0) mod 11 from the shared r_3 with (0,4) (resp. (2,0)). It derives x ≢ 3 (resp. x ≢ 0) from sharing no coordinate with anchor 14 (resp. anchor 0).

The checker's route is valid but not literal. The anchor half of the prose is already enforced when the initial domains D0 are filtered against the anchors. The owner recomputed this in the kernel on 2026-10-29, from the namespace of that checker's own run:

- Class (0,0): the odd types are 15, 45, 75, 105, 165, 195, 225, 255, 285, 315. Their residues mod 11 are 4, 1, 9, 6, 0, 8, 5, 2, 10, 7; none is ≡ 3, so all are consistent with anchor 14. Each fails (SQ) against 234 ≡ 3 (mod 11).
- Class (2,4): the odd types are 29, 59, 89, 119, 149, 179, 239, 269, 299, 329. Their residues mod 11 are 7, 4, 1, 9, 6, 3, 8, 5, 2, 10; none is ≡ 0, so all are consistent with anchor 0. Each fails (SQ) against 110 ≡ 0 (mod 11).

So both halves of the literal prose hold. The checker's assertion exercises the half that uses the reference elements. f177 also reports that its own prose-literal mirror of Steps 1–6 holds.

## Boundary

- All three f177 MINORs are addressed, by text replacement in reading only.
- The f177 INCONCLUSIVE items i1–i5 are not touched: the imports, the author-reported checker run, and novelty.
- No other packet is affected.
- The candidate theorem's status is unchanged: UNREVIEWED as a whole, conditional on its three named imports, with the original unrestricted problem OPEN.

**END OF ERRATUM 1.**
