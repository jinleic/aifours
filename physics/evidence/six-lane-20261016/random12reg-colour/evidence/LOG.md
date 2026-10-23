# Lane log (host clock, PDT, 2026-10-17)

## Setup
- Parent IRC (after 09:21:00): χ8 r3 is CORRECTNESS-ACCEPTED; new target χ(G_{n,12}) = 5 under contract
  `screening/phys-2-random12reg-colour-contract.json`. 09:22:49: SHA verified
  (9b33f97f42179c6b15a50cdd3ae3ec907821cf4e9330663a7dadf43a406f15bb); the lane did not exist yet.
- Contract and χ8 verdict (`review/chi8-parent-verdict.md`) read.
- 09:27:55 created `random12reg-colour/` with `mkdir` (no -p; it refuses an existing directory), plus code/,
  evidence/, review/, archive/ and explore/.
- 09:28:21 (mtime) README §0 frozen protocol written before any computation. SHA-256
  5b48dc983040191001d21cf1a0cb1546aee3be1535b70d2e29682dfbee0674a3. A byte copy is kept as
  `archive/README.protocol-frozen-2026-10-17T092821.md`, because README §1 will be updated with checkpoints.

## Exploration (floats, not evidence)
- 09:29:10–09:29:32 `explore/explore_k5.py` → `explore/explore_k5.json` (+ `.stdout.txt`). Results:
  - E1: minimum (F(u*) − F)/|r − u*|² ≈ 0.0644 on family (x, y⁴) at x ≈ 0.804; local coefficient 0.2497
    (analytic and finite-difference agree). This guided the choice c_row = 1/40 for the supplementary check.
  - E2: KPW's relaxed φ_12: all 320 SLSQP starts end at J; three families stay below J. So there is no evidence of a
    structural failure of the relaxed route at (5, 12). This is recorded as a significance caveat.

## Verifier
- `code/verify_chi12.py` written (general-k; exact/sympy/arb; sections A–G, plus S in floats).
- 09:36:36 first run: TypeError (Fraction × arb in a display line), fixed. Before that run, two placeholder
  booleans were replaced by notes, and the double factorials were cached.
- 09:37:06–09:37:34 full run: all_required_true = true.
- 09:39:10–09:39:37 rerun after adding arb point values of the supplementary slack (section C): all_required_true =
  true. Final SHAs: script aa326a1f54ee15f38138684392d9ae2a50ed98e4662be8a4db179b61be6fbaa1, json
  595b7389559bc4a52863061debaea0e8eca35ff859630ce7229a11456f1b0118, stdout
  16fc8a7915f6583d8fd2a8c59bf5b0bd7c869010e5af3344946303fcd831d2ed.
- Key outputs:
  - (H1) = 5; ratio 11/16; growth 4096/3125; Σλδ² = 8 log(16/5); KPW window {5, 6};
  - residue counts 1, 2704156, 3384731762521200, 235809301462142612780721600;
  - Lemma 6(a) eigenvalues 17 (×16), 12 (×8), 32 (×1); H eigenvalues 125/17, 25/17 (×6), 5/17 (×9);
    det H = 5²⁴/17¹⁶; degree 242;
  - 11⁵ < e¹² via 22 terms; a = 0.2503041193…, κ = 1.0228006668e−3, C_12 = 5.8662053975e−4;
  - supplementary check: 89 centred-form pieces, minimum certified slack 3.68e−6;
  - (4, 8) control reproduces χ8; (5, 13) fails;
  - exact EY control t ≤ 20; k = 4 cross-check equals χ8's rate;
  - first-moment exact control n ≤ 10.

## Proof
- 09:40–09:44 `review/drafts/PROOF_CHI12.r1.DRAFT.md` written (the write tool created `review/drafts/`). Three
  wording precision edits were made before the freeze.
- 09:44:53 (mtime) FROZEN `review/PROOF_CHI12.r1.md`, SHA-256
  0b608b0790887d8ade912b6cf5700ab57df3b2ff57ad7936430eafdb7b35d85e, 634 lines (`cp -n`). The draft was moved with
  `mv -n` to `archive/PROOF_CHI12.r1.DRAFT-working-copy.md`, byte-identical.
- SHA and summary sent to Main. No processes running.

## Reviews of r1 and the r2 draft
- About 09:59: parent IRC. The Codex hostile review is ACCEPT-WITH-FIXES, with no fatal or major finding. Its
  minor finding: W99 Theorem 4.1's first conclusion is overstrong (counterexample Y + 1). The parent instructed:
  - use only W99's contiguity conclusion (LF1519–1548, 1589–1596);
  - prepare changes to §1 (I3) and §5.2;
  - WAIT for the Claude complete review, then freeze a single r2;
  - keep the verifiers unchanged and do not touch previous lanes.
  The parent replay of verify_chi12.py is byte-identical (review/chi12-parent-verifier-replay-v1/parent-result.json,
  read).
- Read: the Codex note (9 checks, all pass after the one minor fix); W99 l.1515–1603 (§4.1 definitions and
  Theorem 4.1); KPW l.150–180 (Theorem 1 proof: its conclusion is the conditional P(Y > 0 | E) → 1, E = {X_1 = 0})
  and l.1542–1562.
- 10:01:00 `review/drafts/PROOF_CHI12.r2.DRAFT.md` started as a `cp -n` byte copy of r1 (SHA 0b608b07…d85e).
  Edits:
  - header (supersession and review status);
  - §1 (I3): full conclusion, W99 definitions, the counterexample, and "only contiguity used";
  - §4 A4;
  - §5.2: contiguity gives P(Y = 0 | X_1 = 0) → 0; the loop equality is a remark, not used; subsequence n = 5t;
  - §5.3 inherited step 1; §9 reliance; §10 item (1);
  - new §11 "Changes from r1".
  sympy check: (a + p)/(m + 1) − a/m − (mp − a)/(m(m + 1)) = 0 (the Y + 1 contiguity-difference identity). The
  slots marked <<CLAUDE-PENDING>> await the Claude review.
- About 10:04 Main informed (draft path and change summary). 10:04:57: the Claude review output is still empty.
- 10:06:27 the watcher saw the Claude review land (`chi12-claude-complete-review-v1.note.md`, SHA f9b2c165…6a9d):
  ACCEPT-WITH-FIXES, no fatal or major finding, minors m1–m6. Parent IRC: freeze ONE r2 = SSC draft + m1–m5 (m6 no
  change); verify the m1 constants independently; any new verifier goes in a NEW file.
- Read KPW l.366–400 (Lemma 4 and its proof), l.526–540 (use at l.534), l.787–830 (Lemmas 6, 7), l.890–912
  (Lemma 8), l.937–998 (S_1; Lemma 4 at l.983) and l.1253–1460 (Lemma 8 proof: (3.20), l.1356, Lemma 4 at l.1436,
  l.1452). A grep for "Lemma 5", "(3.7)", "(3.8)", "(3.9)" and "(3.15)" confirms the row A14 list.
- Hand derivations, all confirmed by the new verifier:
  - second ε-condition: cλ_min = d(k−2)/(2k²(k−1)) = 9/50; D_2 = dk²(k−1)²/(2(k²−2k+2)) = 2400/17; ε² < 51/40000
    (with D_1 = 38400/17 it would be 51/640000);
  - m2: (3.20) needs ε′ > D_1ε², strictly, because of n^{−k²/2};
  - m4: EX_i = [n]_i(d(d−1))^i/(2iΠ(dn−1−2j));
  - m3: N_L ∈ [(dm/2 − 2ℓd)^ℓ, (dm/2)^ℓ], density ratio bounds, the L-uniform decomposition, the expected number of
    extra pairs ≤ C(2ℓ(d−1),2)/(dm−2ℓ−1), and the (d!)^m-to-one map.
- 10:15:25–10:15:39 first run of `code/verify_chi12_r2.py`: all checks true, but two sympy booleans were serialised as
  "True". After casting them with bool(), the final run 10:15:59–10:16:13 gave all_required_true = true. SHAs:
  script 0eca7bc546947fa49eb9c5eaa035401187dac51bf5812ebbd9bb454d513d6086, json
  19e12327af3af6f70496c2d9950e833a740c181887248fd47e36e2acd8b6990f, stdout
  4679c1191154e224d5683b3fdae63dd778bdd68ae0540620e0587a9de2d080ae.
- m1–m5 folded into the draft: header; §1 (I2) (Lemma 4 quote, both ε-conditions), (I4) (EX_i); §4 A9, A10, A14,
  A15; §5.2 (a); §5.3 (inherited step 1 plus a four-step supporting derivation); §8 (r2 verifier); §9; §10 (4)–(6);
  §11 items 2–6. No markers were left.
- 10:19:27 (mtime) FROZEN `review/PROOF_CHI12.r2.md` (`cp -n`), SHA-256
  5fee0295e1ec3716b26924920f015d4a2116e63516ac12f6431724ef1d6e1a00, 781 lines. The draft was moved with `mv -n` to
  `archive/PROOF_CHI12.r2.DRAFT-working-copy.md`, byte-identical. r1 is unchanged (0b608b07…d85e). The diff
  `evidence/r1-to-r2.diff` (c1f8e1eab857b8602775e68e9a614ccb839a6f04025187b3105d37ba0929ba56) has 11 hunks,
  about 186 lines added and 39 removed.
- About 10:31: parent IRC. The Codex delta review of r2 is ACCEPT-WITH-FIXES (two minors). The instruction: freeze
  r3 = r2 + exactly two edits (the EX_i explanation at LF187–189; the m > 4ℓ qualifier at LF535–539), plus
  title/status/§11, with no verifier change.
- 10:32:41 `review/drafts/PROOF_CHI12.r3.DRAFT.md` created as a `cp -n` byte copy of r2. The two edits, title, status
  and §11 items 7–8 were applied.
- 10:33:10 (mtime) FROZEN `review/PROOF_CHI12.r3.md`, SHA-256
  04f5f370f13f84ebf2e0f08ac9421209a07309fc040bd74b05d05e4cfa2c1f39, 801 lines. The draft was moved with `mv -n` to
  `archive/PROOF_CHI12.r3.DRAFT-working-copy.md`, byte-identical. Diff `evidence/r2-to-r3.diff`
  (dd32557b030cc931d4db2d06842876a007cb9e26feae2e405e5f7de7887507b8): 4 hunks, 30 lines added and 11 removed.
