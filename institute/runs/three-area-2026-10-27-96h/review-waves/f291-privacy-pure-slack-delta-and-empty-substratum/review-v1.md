# review-v1: f291 — corrected pure-slack Δ identity, endpoint emptiness, limited consequences

- Reviewer: ReviewF291Privacy. Same-harness WRITTEN_ONLY review; not human, independent-model-family, formal/kernel, or novelty acceptance.
- Clocks: manifest/freeze observed 2026-10-30T03:39:44-0700 PDT; prebody ACK 03:40:24; checkpoint-1 03:51:44; delivery clock at end.
- Verified bindings: manifest-v1.json sha256 36730f302fed6bdd18e976cd798cbdb775a21434bd3b95523739e290997dbbfd; freeze-receipt-v1.json 65d260fa0061ed9d700772446f8dfcef1871988a20ba51eaf8bb4d6afc1838d8; literal-packet-v1.md 091aa291d9d71da7c2218706065adc1299eb8f433136ad494b9d32676bf5bbda (20443 bytes, 159 LF; complete raw read in <=20LF windows incl. seams S4|19, S5|9).
- Controls read STATUS ONLY; no quarantined episode, selection, confidence or outcome used; excluded links not followed.
- Exact-scope imports used: S8|13-38 (functional, CPL coupling S8|17-19, Z/N tail formulas S8|23-28, block convexity derivatives S8|30-33, roots R0/R1 with clipping S8|35-38); S7|16-23 (corrected two-line rule S7|18-21 with m2's one-way note per S5|8, corner-interval rule S7|23); S5|5-9 (f273 conditional imports at stated scope); S6|13-24 (geometry rows and Leibniz discipline as context only). NONINPUT: S3|5 global-impossibility withdrawals, S4|22-26 sub-stratum sign claim (VOID per S1/S2), S2|7-9 unpaid inequality (vacuous on the empty sub-stratum), all author nonemptiness sketches. S nonemptiness NOT assumed anywhere below.
- No code/CAS/interpreter/solver/enumeration/replay; no selected concrete states, arrays, operators or parameter configurations; written symbolic reasoning only.

## Written reconstruction (basis of all verdicts)

Tail block of h = N − λZ at (t0,t1) = (a,c): b·{(2/3)T4 − 2λT2 + (16/3)cT3 + 4c²T2 − 8λcm + 8∫₀^c ψ1(F1(y),y)dy}, with ψ1(z,y) = T2z + m(z²+y²) + z³/3 + y²z − 4y³/3 − λ(z−y); this matches S4|13 against S8|27-28 exactly (8t1m, 2T2 from Z_tail; (2/3)T4, (16/3)t1T3, 4t1²T2 from N_tail). The C0 block (1−b)(Q0 − λA0) is identical at (a,c) and (a,a+1/2) on S: at both points two-line slack gives F0 = Π0(·;a) = proj(R0(·),[a,2a−y]), a-dependent only. Hence Δ carries factor b and the constants (2/3)T4, 2T2 cancel; retained constant difference (16/3)T3δ + 4T2(c²−(a+1/2)²) − 8λmδ, δ := c−a−1/2 — exactly S4|9/S4|20. True tail profiles on S:

- at (a,c): F1 = Π1(y;c) on [0,a] (slack case S7|20) and on (a+1/2,c] (plain box), but on the corner interval (a,a+1/2] the CPL constraint S8|19 applies and F1 = φc(y) := proj(R1(y), [max(c, 2a+1−y), 2c−y]) (S7|23);
- at (a,a+1/2): F1 = Π1(y;a+1/2) on [0,a]; on (a,a+1/2] the corner feasible interval is DEGENERATE: [max(a+1/2, 2a+1−y), 2a+1−y] = {2a+1−y}, so F1(y) = 2a+1−y forced, for every a ≥ 0.

## Claim 1 — S4|9-11 displayed Δ as an identity on S (stated scope "pure-slack stratum", S4|5): REFUTED (MAJOR, F1)

Finding (LF): S4|5 "slack at every height: Π1(y)>=Π0(y)+1 for all y" covers only the two-line heights y ∈ [0,t0] (S7|18); it does not control the corner interval (a,a+1/2], where only F1 is present under CPL (S8|19, S7|23). S4|14 defines Π1(y;c) as the a-independent BOX projection min(2c−y, max(c,R1(y))), and S4|5 asserts "nothing depends on a inside the blocks". But:

(i) At the edge (a,a+1/2) the corner feasible set is the single point 2a+1−y (upper face 2t1−y = 2a+1−y equals the CPL bound; max(a+1/2,2a+1−y) = 2a+1−y since y ≤ a+1/2), so the true edge profile on (a,a+1/2] is 2a+1−y, while the display's integrand uses Π1(y;a+1/2) = min(2a+1−y, max(a+1/2,R1(y))), which equals 2a+1−y ONLY where R1(y) ≥ 2a+1−y. In particular on the S₊-type regime (a+1/2 ≥ √λ−m) one has R1 ≤ √λ−m ≤ a+1/2 < 2a+1−y on (a,a+1/2), so the display's edge integrand sits at the box LOWER face a+1/2 instead of the forced 2a+1−y — a definite discrepancy on a full-measure subinterval, of both sign and magnitude relevance.
(ii) At (a,c) with c < a+1 the CPL lower bound 2a+1−y exceeds c on (a, 2a+1−c), and there φc(y) > Π1(y;c) wherever R1(y) < 2a+1−y (φc ≥ Π1 always, since the corner interval ⊆ box). For c ≥ a+1, φc = Π1(·;c) identically (2a+1−y ≤ a+1 ≤ c).

Exact gap. TRUE Δ − DISPLAYED Δ = 8b∫_a^{a+1/2}{[ψ1(φc(y),y) − ψ1(2a+1−y,y)] − [ψ1(Π1(y;c),y) − ψ1(Π1(y;a+1/2),y)]}dy, which is not identically zero on S as defined.

Precise repair (either form, additive, no other change):
(a) Hypothesis repair — add to the stratum the CORNER condition R1(y) ≥ 2a+1−y for all y ∈ (a,a+1/2]. Then Π1(y;a+1/2) = 2a+1−y and φc(y) = min(2c−y, max(c,2a+1−y,R1(y))) = min(2c−y,max(c,R1(y))) = Π1(y;c) for every c ≥ a+1/2, so the S4 display becomes an exact identity on S ∩ CORNER. (Equivalently: CPL is inactive at the box-projection minimizer.) Compatibility: CORNER implies R1(a⁺) ≥ a+1, i.e. a+1 ≤ √λ−m, which is exactly the complement regime of the S1-emptiness side; no conflict with S ⊆ {a+1 ≤ √λ−m} (Claim 3). By concavity of G(y) := R1(y) − (2a+1−y) on the real-root region, CORNER is checkable at the two endpoints (R1(a) ≥ a+1 and R1(a+1/2) ≥ a+1/2, root real throughout); where the root is clipped (y > √(λ−v), R1 = −m < 2a+1−y) CORNER fails automatically.
(b) Formula repair — keep S unchanged and replace, inside the last integral of S4|11 on (a,a+1/2], the integrand by [ψ1(φc(y),y) − ψ1(2a+1−y,y)]. This unconditional form is the exact value difference.

Verified components of the display (all SUPPORTED, hence only the corner piece is at fault): factor b (C0 cancels; S4|9), constant terms (16/3)T3δ, 4T2(c²−(a+1/2)²), −8λmδ with 2T2 and (2/3)T4 cancelling (S4|9 vs S8|23-28), added y-range [a+1/2,c] and unchanged range [0,a+1/2] (S4|10-11, S4|20), λ-dependence carried by ψ1, R0/R1 and −8λmδ with λ = V ∈ (1/2,2] standing (S4|3, S8|15), root clipping inside R1 (S4|14 = S8|38), and the profile domain [0,c] with nonempty boxes B1 = [c,2c−y] (y ≤ c). S4|24's bracket δ[(16/3)T3 − 8λm + 4T2(a+1/2+c)] + 8∫_{a+1/2}^c ψ1(Π1(y;c),y)dy is correct algebra (c²−s² = δ(c+s)), status unchanged (its sign use is void per S1/S2).

## Claim 2 — S4|18 face-speed/Danskin identity: SUPPORTED (with scope note; one MINOR attached to S2|9)

Finding (LF): S4|18 is exact for the standalone object 8∫₀^c ψ1(Π1(y;c),y)dy: Π1(y;c) = c on {R1 ≤ c} (speed 1), = R1 on {c < R1 < 2c−y} (speed 0), = 2c−y on {R1 ≥ 2c−y} (speed 2); at the moving limit y = c, Π1(c;c) = min(c, max(c,R1(c))) = c, giving the boundary term 8ψ1(c,c). No moving-branch-boundary residue appears because the branch values coincide at switch heights; a.e. chain rule applies since for every fixed c the tie sets are null: {R1 = c} is the level set of a strictly decreasing function (at most one y; the clipped region gives R1 = −m < 0 < c), and {R1 = 2c−y} requires √(λ−v−y²) = 2c+m−y, where the strictly concave left side cannot meet the line on an interval (and the clipped region gives −m = 2c−y for at most one y ≤ c). Consistent with S6|24 "endpoint speeds are 1 and 2" and with diagonal ties needing directional rules (S6|24); here the ties are automatically null so the pointwise formula stands for every c > a+1/2 ≥ 1/2 > 0.

Scope note: as b⁻¹∂_cΔ (S2|9) this is the derivative of the DISPLAYED Δ; it equals ∂_c of the TRUE Δ only where the display is exact, i.e. on S ∩ CORNER (repair (a)); off that stratum the corner rule φc has its own c-dependent lower bound max(c,2a+1−y) and contributes extra terms not present in S4|18/S2|9. The true edge profile 2a+1−y is c-independent, so no edge-side derivative term is missing.

MINOR (LF S2|9): the fragment "ψ1(c,c)=T2c+2mc²+c³/3+2c³/3·…" is wrong as written: at z=y=c the cubic terms cancel exactly, z³/3 + y²z − 4y³/3 = c³/3 + c³ − 4c³/3 = 0, and −λ(z−y) = 0, so ψ1(c,c) = T2c + 2mc². Harmless to the (void) D1 narrative, but the boundary term of the live Danskin identity is exactly 8ψ1(c,c) = 8(T2c + 2mc²) and future sign work should use the cancelled form.

## Claim 3 — S1|5 emptiness of S ∩ {a+1/2 ≥ √λ−m}: SUPPORTED

Finding (LF): S1's argument verifies at the single height y = a of the edge point (a,a+1/2), which is a two-line height ([0,t0] closed, S7|18) and hence inside S's own definition. There the C0 box [a,2a−a] collapses to {a}, so Π0(a) = proj(R0(a),{a}) = a regardless of R0 (projection identity); slackness requires Π1(a;a+1/2) = min(a+1, max(a+1/2,R1(a))) ≥ a+1, which forces R1(a) ≥ a+1 (a+1/2 < a+1); but R1(a) = √(max(λ−v−a²,0)) − m ≤ √λ − m, so S-membership implies a+1 ≤ √λ−m, contradicting a+1/2 ≥ √λ−m (indeed forcing a+1/2 ≤ √λ−m−1/2). Hence S ∩ {a+1/2 ≥ √λ−m} = ∅ whether or not S itself is nonempty — no nonemptiness assumption used. The stated consequences are correctly bounded: the addendum-4 sub-stratum sign claim is vacuous/VOID (S1|5), no theorem is advertised (S1|5), the D1 unpaid inequality is thereby moot rather than proved (S1|7 "unaffected" = not refuted; it lives on an empty set), and no sign, uniqueness, branch-exclusion or global-value conclusion is drawn. Consistent with S2|11 (D2): nonemptiness remains conditional.

Strengthening remark (written, symbolic, no instances): the same projection identity gives the exact reduction of S's edge condition — since Π0(y) ≥ a and Π1(y;a+1/2) = min(2a+1−y, max(a+1/2,R1(y))) with 2a+1−y ≥ Π0(y)+1 automatically (Π0 ≤ 2a−y), slack at the edge at height y holds iff max(a+1/2,R1(y)) ≥ Π0(y)+1, i.e. iff R1(y) ≥ Π0(y)+1. In particular R1(y) ≥ a+1 on [0,a] is necessary, so S ⊆ {a+1 ≤ R1(a) ≤ √λ−m} ⊆ {a < √2−1−m} under the standing λ ≤ 2. This both confirms S1's mechanism and shows the "large a" regime cannot occur in S (see Claim 5).

## Claim 4 — S4|5 nonemptiness parenthetical ("Nonempty: at large a the upper box faces bind: Π0=2a−y … e.g. c>=a+1 with R1>=2a−y"): UNSUPPORTED sketch (MINOR; already downgraded by S2 D2)

Finding (LF): for a ≥ 2 (any admissible λ ≤ 2) one has R0(y) ≤ √λ ≤ 2 ≤ a on [0,a], so Π0 = proj(R0,[a,2a−y]) sits at the LOWER face a, not the upper face 2a−y; the "large a upper faces bind" description is wrong, and in that regime slack at the edge would need R1 ≥ a+1 on [0,a], impossible for a ≥ 2 (Claim 3 bound). Also, as a slack test, "R1 ≥ 2a−y" does not give Π1 ≥ Π0+1 where Π0 = 2a−y (there R1 ≥ 2a+1−y is needed); the parenthetical is not a valid witness sketch. This does not change status: S2|11 already made S-nonemptiness conditional, and the present review neither assumes nor establishes it.

## Verdict summary

- S4|9-11 displayed Δ on S as defined: REFUTED at stated scope — F1 MAJOR; exact after either precise repair (a) stratum ∩ CORNER {R1 ≥ 2a+1−y on (a,a+1/2]} or (b) corner-rule integrand on (a,a+1/2]; every other component of the display (factor b, constants, moving limits, λ-dependence, root clipping, profile domain) SUPPORTED.
- S4|18 face-speed/Danskin identity: SUPPORTED as a standalone identity (null tie sets for every c; boundary 8ψ1(c,c) = 8(T2c+2mc²)); as ∂_cΔ valid only on S ∩ CORNER — scope condition must travel with it. One MINOR correction at S2|9 (ψ1(c,c) cancellation).
- S1|5 empty-substratum statement: SUPPORTED (exact y=a projection-identity argument; no overreach; no nonemptiness assumed).
- S4|5 nonemptiness parenthetical: UNSUPPORTED (MINOR; moot under S2 D2).
- Totals: 0 FATAL, 1 MAJOR, 2 MINOR. Per the wave's acceptance: the exact conditional identity is the S4 display valid on S ∩ CORNER (or with the corner-rule integrand), and the empty-substratum statement stands; no uniqueness, branch-exclusion, global-value or sign conclusion is asserted or implied by this review.

## Process

Written-only reconstruction from the frozen packet; no prior reviewer body, sibling output, author code, network, withdrawn computation or quarantined payload; no selected concrete instances, no code/CAS/solver/enumeration/replay. Output confined to this wave directory (reviewer-f291-prebody-ack-v1.md, reviewer-f291-checkpoint-1.md, this file, reviewer-f291-delivery-v1.md). Delivery clock recorded in reviewer-f291-delivery-v1.md.
