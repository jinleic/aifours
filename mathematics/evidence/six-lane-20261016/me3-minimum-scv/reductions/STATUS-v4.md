# reductions/ — STATUS v4

Written 2026-10-18 06:58 PDT (host clock) by `MathPhaseType3.ME3Reductions`. This file supersedes `STATUS-v3.md`
(bd081bb7…12f6) and `STATUS-v2.md` (a644d430…d27e) for the items below. Correctness only.
`proof/reductions-v4.md` = `reductions-v3.md` (e5c75b24…b15c) + the fixes of
`institute/runs/six-lane-2026-10-16/review/me3-reductions-claude-v1.note.md` (sha256
68cd8dd933d5e303dcb0472e0425aed70e45b2d85db2f15f773f666471d8ed6e; ACCEPT-WITH-FIXES, 0 FATAL, 0 MAJOR, 6 MINOR).
The Codex resultant fix of v3 is retained verbatim (v4 LF424–425). Nothing is weakened.

## 1. What each claim rests on (v4 labels)

| Label | Claims |
|---|---|
| **Proved in text** (written proof, ordinary imports only) | L1 (1.1, 1.2, L1(a), L1(b) + padding LF172–174, Cor 1.3, 1.4, normal forms); L2 (2.1–2.6, Remark 2.3a); L3 (3.1–3.5, Theorem L3: real-exponent SCV ≥ Δ3); L4(1)–(3), with Δ3 > 1/4 from the SOS identity; Lemmas 5.1–5.5; Cor 5.7 (now proved from Lemma 2.4 + Lemma 5.1); L6 (6.1–6.6); Cor 7.1; **Cor 7.2 (new)** |
| **Text + exact rational certificate** (each step is a finite rational identity, checkable by hand and re-checked by `exact-certs-v1`, `resultant-check-v1`, `alt-route-check-v1`; all exit 0) | L4(3) root isolation, s(x1) < 1/3 < 1/2 < s(x3), h(Δ3) = 0 (remainder) and irreducibility mod 5; v3 resultant remark Res = 432·h; **Lemma 4.2: Δ3 > 553/2000**; Lemma 5.4 tail 428/2125 (> 0.2014) for ω ≤ 1/4; Lemma 5.5 tail constant; **Theorem 5.6**: v_cos ≤ 773/3844 < 0.2014 < 11/50 = T, 773/3844 < 553/2000 < Δ3, attainment and 1/4 < ω_m < 4; Remark 5.6a (hand route via 21/104, middle [1/5, 4]) |
| **Conditional / computational** (library semantics; never used by any proof) | U ball v_cos < U (`ctl-c-v2`, Arb); Sturm brackets and Arb enclosure of Δ3 (`ctl-b-v1`); θ1 table (`ctl-e-v1`); sample checks (`ctl-c-v2` c5, `ctl-a-v1`, `ctl-d-v1`, `ctl-e-v1`); **Theorem 5.8**: 0.20090156350055 ≤ v_cos, OPTIONAL, conditional on `ctl-f-main-v1` / `ctl-f-gradsym-v1` (code and outputs pinned in `STATUS-v2.md` §3) and on the parent primal desk's independent check `review/me3-parent-primal-reductions-v1/RESULT-v1.json` (9a72e3e7…65e3, run `d1b-lower-worker-L`); no assembly step uses it |
| **EXPLORATORY** | Newton point (ω*, φ*) and its value; float grids; contract-band check |

## 2. Fix map (v4 line numbers; review cites reductions-v1 lines "S02:NNN")

* **Header fix map:** LF3–35.
* **MINOR-1** (v1 S02:416): Cor 5.7 LF591–594 now says "equality for some minimizer (Thm 5.6)"; minimizers are
  (ω_m, φ_m) at LF526–527 and LF538 (Thm 5.6) and at LF756–758 (Cor 7.1 proof). (ω*, φ*) remains only the Newton point
  (LF566–576).
* **MINOR-2** (v1 S02:371, 393–401): the exact chain is used throughout.
  * Lemma 5.4 LF494–496 cites Lemma 4.2, and Thm 5.6 LF525–527 and LF536–537 cite Lemma 4.2 and 773/3844.
  * Theorem 5.8 tail input is now the exact Lemma 4.2 (LF641–642).
  * The supplementary labels are at LF511–512 (samples), LF549–551 (U) and LF702–703 (θ1 table); the Sturm bracket
    in L4(4) was already supplementary (v3).
  * Remark 5.6a, LF553–564, is the hand route.
  * The §7 constants (LF798) and Status of the parts (LF787–789) are updated to match.
* **MINOR-3:** Lemma 5.1 LF468–469, Cor 5.7 proof LF596–599, Cor 7.1 proof LF755. "I_1 = v_cos" now comes from
  Lemma 2.4 + Lemma 5.1, never "by definition".
* **MINOR-4:** Corollary 7.2 (strictness per cone) LF760–774; Remark 7.2a LF776–785.
* **MINOR-5:** the conditional label replaces "certified" at:
  * Theorem 5.8 LF609–613;
  * LF615 ("Independent check");
  * LF618–620 (the record's own label, quoted);
  * LF585–587 (band note);
  * LF802–803 (§7).
  It stays optional, and no assembly step uses it.
* **MINOR-6:**
  * (i) multiplicities n_λ at LF167, n_* at LF278–279, n_i and n1 at LF286–293;
  * (ii) the continuous "≢ 0" is noted at LF100–101 (positive mass in §0.2 since v2);
  * (iii) L1(b) now says ME(N) ⊆ ME(≤3) at LF162, with the padding at LF172–174;
  * the review's notes on v1 S02:177–178 and S02:303 need no change.

## 3. Static code note on `code/ctl_f_d1bnb_v1.py` (sha256 508b1488…41b7; static reading only)

1. **Exact parsing (review code item 1): PASS.**
   * LF27 takes the argv strings.
   * LF38 `Lq = sp.Rational(L_str)`: a SymPy Rational of a decimal string is exact, here 20090156350055/10¹⁴.
   * LF33–35 `to_fmpq` uses the integer numerator and denominator, and LF39 calls it.
   * LF40 `La = arb(Lf)` is a ball that contains L exactly (L is not dyadic), so every `… > La` means "> L for certain".
   * LF41–42 `w_lo = sp.Rational("1/4")` and `w_hi = sp.Rational("4")` are exact.
   * The initial box (LF118) and all bisection points are fmpq dyadics, so they are exact.
   * The tails compare exact SymPy rationals (LF57).
   * No float literal or `float()` call occurs in the parse, tail or acceptance paths.
2. **Stopping (review code item 2): PASS** (also `audit-bnb-v2`, B1–B5).
   * Success requires an empty stack, not aborted and not refuted (LF165–167).
   * The box cap (LF129–131) and depth cap (LF152–155) set `aborted`.
   * An exception ends the process with a nonzero exit, before `ctl_f.json` is written (that happens only after the
     loop, LF178).
   * The exit code is 0 iff the outcome equals EXPECT (LF183).
3. **√(u(2−u)) and NaN (review code item 3): PASS.**
   * F_ball LF68–69 clamps with `(u*(2−u)).nonnegative_part()` before `.sqrt()`. This is sound because the true
     u(2−u) ≥ 0 on [0, 2] lies in the ball, hence in its nonnegative part.
   * grad_ball LF79–80 takes `g.sqrt()` unclamped, but it is reached only under LF146 (0 < u_lo and u_hi < 2). If that
     ball still straddles 0, the result is NaN, the mean-value test `(Fc − err) > La` (LF149) is False, and the box is
     split.
   * Every acceptance is a positive strict ball comparison, `> La` (LF135, LF149), and the refutation is `Fc < La`
     (LF143). No predicate has the form `not (x <= L)`.
   * The only `not` in the file are at LF165: `not aborted` (a bool) and `not stack` (the empty-stack test).
   * python-flint returns False for undecided and NaN comparisons (`audit-bnb-v2` C1, C4, C6).
4. **Gradsym scope (review code item 4).** `ctl-f-gradsym-v1` verifies only the F_ball/grad_ball formulas. The driver,
   predicates, initial box and split are covered by the static audit `audit-bnb-v2` (B1–B5), not by gradsym.

## 4. New files (sha256)

| File | sha256 |
|---|---|
| `proof/reductions-v4.md` | be1f7190ba71f06b3e951886581d285cc74435a49e3c2983776cebb6101f6eb1 |
| `proof/reductions-v4.diff-from-v3.txt` (`diff -u`, noclobber) | 5a6a37f44c28d8a9ee68d4fc28a1649b7ec1d70792cd6b843d0835354794b08b |
| `code/alt_route_check_v1.py` | 754f495f2edac0f64c1f661da235344fa8d185ed074195c44fb6bec904c28204 |
| `runs/alt-route-check-v1/alt_route_check.json` | 0e0cbdc3985e7de0a6f18b40b0c8ecb230122ad7b93bebf7b08dff399a53e856 |
| `receipts/alt-route-check-v1-pre.json` | 3e6068b7f968df79108ccb09e3228c394b3c8018a015f1edc26abf1f49ebd72d |
| `receipts/alt-route-check-v1-post.json` | b640d282e5511c294c92a395bed3ce5253773c4b00bc4635931839a2c8531cce |

Run `alt-route-check-v1` exited 0 with 5/5 checks:
* (1/4 − 1/25)/(1 + 1/25) = 21/104;
* 21·3844 = 80724 > 80392 = 773·104;
* d/dω[(1/4 − ω²)/(1 + ω²)] = −(5/2)ω/(1 + ω²)²;
* 21/104 > 0.20090156350055;
* wrong control: the ω ≤ 1/4 tail using only Δ3 > 1/4 gives 3/17, and "3/17 > 773/3844" evaluates to False.

Unchanged: `reductions-v3.md` e5c75b24…b15c, `reductions-v2.md` bd497389…1e3f, `reductions-v1.md` ad6c5091…5536.
